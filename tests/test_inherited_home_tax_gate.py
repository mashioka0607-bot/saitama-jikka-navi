import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "static_pages" / "tedori-hikaku" / "index.html"
OUTPUT = ROOT / "dist" / "tedori-hikaku" / "index.html"


class InheritedVacantHomeTaxGateTests(unittest.TestCase):
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
            self.assertLess(html.index('id="calc"'), html.index('id="inherited-home-tax-check"'))
            self.assertLess(html.index('id="inherited-home-tax-check"'), html.index('id="quote-request-template"'))
            self.assertNotIn("class=\"affiliate\"", segment)
            self.assertNotIn("data-affiliate", segment)


if __name__ == "__main__":
    unittest.main()
