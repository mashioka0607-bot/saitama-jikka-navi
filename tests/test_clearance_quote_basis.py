import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "static_pages" / "tedori-hikaku" / "index.html"
OUTPUT = ROOT / "dist" / "tedori-hikaku" / "index.html"


class ClearanceQuoteBasisTests(unittest.TestCase):
    def test_gross_net_example_survives_build_and_credits_source(self):
        for file in (SOURCE, OUTPUT):
            html = file.read_text(encoding="utf-8")
            self.assertEqual(html.count('id="real-clearance-quote-example"'), 1)
            self.assertIn("https://ikki-inc.net/removal", html)
            self.assertIn("片付け費用60万円・家財の買取額18万円・支払額42万円", html)
            self.assertIn("事業者の自己申告による1件の事例", html)
            self.assertIn("平均相場", html)
            self.assertIn("42万円と18万円を同時に入力すると買取分を二重に差し引き", html)

    def test_input_disclaimer_is_next_to_the_2_separate_cost_fields(self):
        html = OUTPUT.read_text(encoding="utf-8")
        self.assertEqual(html.count('id="clearance-gross-net-note"'), 1)
        self.assertLess(html.index('id="clear"'), html.index('id="reuse"'))
        self.assertLess(html.index('id="reuse"'), html.index('id="clearance-gross-net-note"'))
        self.assertLess(html.index('id="clearance-gross-net-note"'), html.index('id="calc"') + 5000)
        self.assertIn("買取額は0円にしてください", html)
        self.assertIn('href="#real-clearance-quote-example"', html)
        self.assertIn("appliedSubsidy", html)

    def test_municipal_clearance_subsidy_is_not_assumed_for_sale(self):
        for file in (SOURCE, OUTPUT):
            html = file.read_text(encoding="utf-8")
            self.assertEqual(html.count('id="grant-clearance-eligibility-example"'), 1)
            text = html.split('id="grant-clearance-eligibility-example"', 1)[1].split("</p>", 1)[0]
            for required in (
                "白岡市", "家財処分費用は対象外",
                "鳩山町", "上限10万円", "一般廃棄物処理業者等の許可書",
                "解体せず現況売却", "0万円として比較",
                "https://www.city.shiraoka.lg.jp/soshiki/seikatsukeizaibu/kankyoka/1_1/7523.html",
                "https://www.town.hatoyama.saitama.jp/kurashi/sumai_hikkosi/rifomujyokyakuhojyo/page001560.html",
            ):
                with self.subTest(required=required):
                    self.assertIn(required, text)
            self.assertLess(
                html.index('id="grant-clearance-eligibility-example"'),
                html.index('id="calc"'),
            )

    def test_no_pseudo_affiliate_url_is_added(self):
        html = SOURCE.read_text(encoding="utf-8")
        segment = html.split('id="real-clearance-quote-example"')[1].split("</section>")[0]
        self.assertNotIn('class="affiliate"', segment)
        self.assertNotIn('data-affiliate', segment)
        self.assertIn("広告提携を意味するものではありません", segment)


if __name__ == "__main__":
    unittest.main()
