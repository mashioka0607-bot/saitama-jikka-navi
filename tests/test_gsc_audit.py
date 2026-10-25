"""Offline tests: never send Search Console exports to third parties."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "audit_gsc_csv.py"
spec = importlib.util.spec_from_file_location("audit_gsc_csv", MODULE)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class GSCExportTests(unittest.TestCase):
    def parse(self, csv_text):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "gsc.csv"
            path.write_text(csv_text, encoding="utf-8-sig")
            return audit.read_export(path)

    def test_japanese_export_and_weighted_ctr(self):
        rows, has_page = self.parse(
            "上位のクエリ,上位のページ,クリック数,表示回数,CTR,掲載順位\n"
            "実家 片付け前 売却,https://saitama-jikka-navi.pages.dev/tedori-hikaku/,1,70,1.43%,10\n"
            "残置物 そのまま 売却,https://saitama-jikka-navi.pages.dev/tedori-hikaku/,0,30,0%,18\n"
            "解体してから売る,https://saitama-jikka-navi.pages.dev/kaitai-check/,4,40,10%,4\n"
        )
        self.assertTrue(has_page)
        report = audit.analyze(rows, has_page, 28)
        cluster = next(x for x in report["clusters"] if x["cluster"] == "片付け前・残置物あり売却")
        self.assertEqual(cluster["impressions"], 100)
        self.assertEqual(cluster["clicks"], 1)
        self.assertEqual(cluster["ctr"], .01)
        self.assertEqual(cluster["average_position"], 12.4)
        self.assertEqual(cluster["priority"], "rewrite")
        self.assertEqual(cluster["observed_pages"], ["/tedori-hikaku/"])
        self.assertTrue(any(x["priority"] == "observe" for x in report["clusters"]))

    def test_query_only_does_not_invent_landing_page(self):
        rows, has_page = self.parse(
            "Query,Clicks,Impressions,CTR,Position\n"
            "相続 実家 売却,1,60,1.7%,13\n"
        )
        self.assertFalse(has_page)
        report = audit.analyze(rows, has_page, 90)
        cluster = report["clusters"][0]
        self.assertEqual(cluster["target"], "/shindan/")
        self.assertEqual(cluster["observed_pages"], [])
        self.assertIn("結び付けた", " ".join(report["warnings"]))
        self.assertIn("同時データ", report["next_step"])

    def test_actual_landing_page_is_not_assumed_from_query_intent(self):
        rows, has_page = self.parse(
            "Query,Page,Clicks,Impressions,Position\n"
            "残置物 そのまま 売却,https://saitama-jikka-navi.pages.dev/shindan/,0,70,11\n"
            "残置物 そのまま 売却,https://saitama-jikka-navi.pages.dev/tedori-hikaku/,1,70,11\n"
        )
        report = audit.analyze(rows, has_page, 28)
        observed = {p["observed_page"]: p for p in report["page_intents"]}
        mismatch = observed["/shindan/"]
        self.assertEqual(mismatch["suggested_target"], "/tedori-hikaku/")
        self.assertTrue(mismatch["intent_mismatch"])
        self.assertEqual(mismatch["priority"], "review_intent")
        matched = observed["/tedori-hikaku/"]
        self.assertFalse(matched["intent_mismatch"])
        self.assertEqual(matched["priority"], "rewrite")
        self.assertIn("実流入先", audit.markdown(report))

    def test_cluster_average_does_not_trigger_false_page_rewrite(self):
        rows, has_page = self.parse(
            "Query,Page,Clicks,Impressions,Position\n"
            "残置物 売却,https://saitama-jikka-navi.pages.dev/tedori-hikaku/,0,50,3\n"
            "残置物 売却,https://saitama-jikka-navi.pages.dev/shindan/,0,50,25\n"
        )
        report = audit.analyze(rows, has_page, 28)
        self.assertEqual(report["clusters"][0]["priority"], "rewrite")
        self.assertTrue(all(p["priority"] != "rewrite" for p in report["page_intents"]))

    def test_gsc_ui_exact_page_filtered_queries(self):
        rows, has_page = self.parse(
            "Query,Clicks,Impressions,CTR,Position\n"
            "残置物 そのまま 売却,0,70,0%,11\n"
        )
        self.assertFalse(has_page)
        rows, has_page = audit.attach_page_filter(
            rows, has_page, "https://saitama-jikka-navi.pages.dev/tedori-hikaku/")
        report = audit.analyze(rows, has_page, 28, source_kind="manual_page_filter")
        self.assertEqual(report["source_kind"], "manual_page_filter")
        self.assertEqual(report["page_intents"][0]["observed_page"], "/tedori-hikaku/")
        self.assertEqual(report["page_intents"][0]["priority"], "rewrite")
        self.assertIn("CSV単体では", " ".join(report["warnings"]))

    def test_page_filter_cannot_be_inferred_or_combined(self):
        rows, has_page = self.parse(
            "Query,Clicks,Impressions,Position\n残置物 売却,0,70,11\n")
        with self.assertRaisesRegex(ValueError, "full HTTPS"):
            audit.attach_page_filter(rows, has_page, "/tedori-hikaku/")
        rows, has_page = audit.attach_page_filter(
            rows, has_page, "https://saitama-jikka-navi.pages.dev/tedori-hikaku/")
        with self.assertRaisesRegex(ValueError, "Page column"):
            audit.attach_page_filter(rows, has_page, "https://saitama-jikka-navi.pages.dev/")

    def test_invalid_and_page_only_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Missing Search Console columns"):
            self.parse("ページ,クリック数,表示回数,掲載順位\n/test/,1,30,10\n")
        with self.assertRaisesRegex(ValueError, "Impossible"):
            self.parse("Query,Clicks,Impressions,Position\nfoo,101,100,10\n")

    def test_csv_totals_are_not_double_counted(self):
        rows, _ = self.parse("Query,Clicks,Impressions,Position\n"
                             "合計,11,120,10\n"
                             "残置物 売却,1,20,12\n")
        self.assertEqual(len(rows), 1)
        self.assertEqual(audit.analyze(rows, False, 28)["clusters"][0]["impressions"], 20)


if __name__ == "__main__":
    unittest.main()
