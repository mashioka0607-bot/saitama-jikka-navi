import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "static_pages" / "tedori-hikaku" / "index.html"
OUTPUT = ROOT / "dist" / "tedori-hikaku" / "index.html"


class InheritedVacantHomeTaxGateTests(unittest.TestCase):
    def test_inherited_title_deadline_is_actionable_and_sourced(self):
        for file in (SOURCE, OUTPUT):
            html = file.read_text(encoding="utf-8")
            self.assertEqual(html.count('id="inherited-title-deadline"'), 1)
            section = html.split('id="inherited-title-deadline"', 1)[1].split("</section>", 1)[0]
            for expected in (
                "親名義のままの実家",
                "2027年3月31日",
                "2024年4月1日",
                "相続人申告登記",
                "所有権移転の相続登記",
                "登記費用を含めていません",
                "https://houmukyoku.moj.go.jp/niigata/page000001_00192.html",
                "https://www.gov-online.go.jp/article/202512/entry-10431.html",
                'href="#quote-request-template"',
            ):
                with self.subTest(file=file.name, expected=expected):
                    self.assertIn(expected, section)
            self.assertLess(html.index('id="calc"'), html.index('id="inherited-title-deadline"'))
            self.assertLess(html.index('id="inherited-title-deadline"'), html.index('id="inherited-home-tax-check"'))
            self.assertNotIn("data-affiliate", section)


    def test_inheritance_tax_gate_is_specific_and_sourced(self):
        for file in (SOURCE, OUTPUT):
            html = file.read_text(encoding="utf-8")
            self.assertEqual(html.count('id="inherited-home-tax-check"'), 1)
            segment = html.split('id="inherited-home-tax-check"', 1)[1].split("</section>", 1)[0]
            for expected in (
                "譲渡所得から最高3,000万円",
                "相続人が3人以上の場合は最高2,000万円",
                "1981年5月31日以前",
                "3年を経過する日の属する年の12月31日",
                "1億円以下",
                "翌年2月15日",
                "2027年12月31日",
                "確定申告",
                "https://www.nta.go.jp/taxes/shiraberu/taxanswer/joto/3306.htm",
                "この計算機に控除額を「補助金」として入力しない",
            ):
                with self.subTest(file=file.name, expected=expected):
                    self.assertIn(expected, segment)
            self.assertEqual(segment.count('id="inherited-home-care-facility"'), 1)
            self.assertIn("要介護・要支援認定等", segment)
            self.assertIn("入所していたという理由だけで対象外と決めつけない", segment)
            self.assertIn("https://www.nta.go.jp/taxes/shiraberu/taxanswer/joto/3307.htm", segment)
            self.assertEqual(segment.count('id="inherited-home-2026-deadline"'), 1)
            self.assertIn("2023年に相続が始まった実家", segment)
            self.assertIn("2026年12月31日", segment)
            self.assertIn("相続ごとの期限と制度全体の期限", segment)
            self.assertLess(html.index('id="calc"'), html.index('id="inherited-home-tax-check"'))
            self.assertLess(html.index('id="inherited-home-tax-check"'), html.index('id="quote-request-template"'))
            self.assertNotIn("class=\"affiliate\"", segment)
            self.assertNotIn("data-affiliate", segment)


if __name__ == "__main__":
    unittest.main()
