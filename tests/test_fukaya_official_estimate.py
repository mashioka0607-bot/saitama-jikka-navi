"""深谷市の無料概算ツールを実際の査定やASP成果と混同しない。"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FukayaOfficialEstimateTests(unittest.TestCase):
    def test_fukaya_official_estimate_links_and_guards(self):
        html = (ROOT / "static_pages/tedori-hikaku/index.html").read_text(encoding="utf-8")
        self.assertEqual(html.count('id="fukaya-official-estimate"'), 1)
        block = html.split('id="fukaya-official-estimate"', 1)[1].split("</section>", 1)[0]
        for phrase in (
            "深谷市内", "無料で概算", "解体後の土地の市場価格",
            "現況査定", "2026年11月30日は事前調査の申込期限",
            "補助金は0円", "物件ごとの買取価格",
            "市が紹介する民間サービス",
            "https://www.city.fukaya.saitama.jp/soshiki/kyoudou/jiti/tanto/akiya/18969.html",
            "https://www.city.fukaya.saitama.jp/soshiki/kyoudou/jiti/tanto/akiya/akiyahojyo/14716.html",
            'href="/kaitai-check/"',
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, block)
        self.assertLess(html.index('id="saitama-official-estimate"'), html.index('id="fukaya-official-estimate"'))
        self.assertLess(html.index('id="fukaya-official-estimate"'), html.index('id="handover-three-routes"'))


if __name__ == "__main__":
    unittest.main()
