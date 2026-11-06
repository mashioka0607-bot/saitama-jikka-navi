"""Keep the editorial policy discoverable from high-intent decision tools.

These static pages replace build.py-generated versions at deploy time, so
checking build.py's shared layout alone is not sufficient.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ("shindan", "tedori-hikaku", "kaitai-check")


class StaticTrustFooterTests(unittest.TestCase):
    def test_decision_tools_link_to_editorial_policy(self):
        for slug in TOOLS:
            with self.subTest(page=slug):
                page = (ROOT / "static_pages" / slug / "index.html").read_text(encoding="utf-8")
                footer = page.split("<footer>", 1)[1].split("</footer>", 1)[0]
                self.assertIn('href="/editorial-policy/"', footer)
                self.assertIn('href="/advertising-policy/"', footer)
                self.assertIn('href="/operator/"', footer)


    def test_saitama_november_2026_public_consult_is_city_scoped(self):
        page = (ROOT / "static_pages" / "shindan" / "index.html").read_text(encoding="utf-8")
        notice = page.split('id="saitama-nov2026-free-consult"', 1)[1].split("</section>", 1)[0]
        for phrase in ("さいたま市内の実家", "2026年11月28日",
                       "武蔵浦和コミュニティセンター", "11月5日〜27日",
                       "12組", "募集終了・内容変更",
                       "https://www.city.saitama.lg.jp/001/154/007/001/p133208.html",
                       'href="/tedori-hikaku/"',
                       "他市町村に一律適用される制度ではなく"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, notice)



    def test_item_safekeeping_before_clearance_warning(self):
        page = (ROOT / "static_pages" / "shindan" / "index.html").read_text(encoding="utf-8")
        self.assertEqual(page.count('id="valuable-items-before-clearance"'), 1)
        notice = page.split('id="valuable-items-before-clearance"', 1)[1].split("</section>", 1)[0]
        for phrase in (
            "貴金属・時計・ブランド品",
            "家族・相続人",
            "買取見込額は確定するまで収入とみなさない",
            "貴金属を強引に買い取られる",
            "https://www.pref.saitama.lg.jp/b0304/shohisoudan/jirei/sonota/houmonkounyu.html",
            "この案内は特定の買取業者への紹介ではありません",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, notice)


if __name__ == "__main__":
    unittest.main()
