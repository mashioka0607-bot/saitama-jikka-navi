"""解体後の税・建築リスクを手取り概算の前に明示する。"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DemolitionTaxRebuildCheckTests(unittest.TestCase):
    def test_before_sale_demolition_guard_and_sources(self):
        for path in (
            ROOT / "static_pages" / "tedori-hikaku" / "index.html",
            ROOT / "dist" / "tedori-hikaku" / "index.html",
        ):
            html = path.read_text(encoding="utf-8")
            self.assertEqual(html.count('id="demolition-tax-rebuild-check"'), 1)
            segment = html.split('id="demolition-tax-rebuild-check"', 1)[1].split("</section>", 1)[0]
            for required in (
                "毎年1月1日",
                "日割りではありません",
                "住宅用地",
                "翌年から3年間",
                "別途申請",
                "即時売却",
                "市街化調整区域",
                "建替え",
                "自動判定しません",
                "https://www.city.fukaya.saitama.jp/soshiki/shiminseikatsu/shisanzei/tanto/koteisisanzei/1391307358865.html",
                "https://www.city.fukaya.saitama.jp/soshiki/kyoudou/jiti/tanto/akiya/1603180013582.html",
            ):
                with self.subTest(path=path, required=required):
                    self.assertIn(required, segment)
            self.assertLess(html.index('id="handover-three-routes"'),
                            html.index('id="demolition-tax-rebuild-check"'))
            self.assertLess(html.index('id="demolition-tax-rebuild-check"'),
                            html.index('id="calc"'))
            self.assertNotIn("data-affiliate", segment)


if __name__ == "__main__":
    unittest.main()
