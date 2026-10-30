import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "patch_tedori_real_quotes.py"
OUTPUT = ROOT / "dist" / "tedori-hikaku" / "index.html"


class QuoteTypeDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.script = SCRIPT.read_text(encoding="utf-8")
        cls.html = OUTPUT.read_text(encoding="utf-8")

    def test_each_quote_identifies_the_kind_of_price(self):
        for i in (1, 2, 3):
            self.assertIn(f'<select id="q{i}t">', self.html)
        for token in (
            'value="unknown"',
            'value="broker"',
            'value="buyout"',
            '仲介の売却査定（成約額未確定）',
            '不動産会社の直接買取提示',
        ):
            self.assertIn(token, self.html)

    def test_price_reliability_warning_before_comparison(self):
        self.assertEqual(self.html.count('id="quote-type-disclosure-v1"'), 1)
        self.assertLess(
            self.html.index('id="quote-type-disclosure-v1"'),
            self.html.index('id="quote-compare"'),
        )
        self.assertIn('仲介査定額は成約価格の保証ではありません', self.html)
        self.assertIn('https://suumo.jp/baikyaku/', self.html)

    def test_unclassified_prices_cannot_be_ranked_or_unlock_paid_cta(self):
        self.assertIn('id="quote-clearance-net-warning-v1"', self.html)
        self.assertIn('相殺後の請求額', self.html)
        self.assertIn("document.getElementById('q'+i+'t').value==='unknown'", self.html)
        self.assertIn('提示の種類（仲介の売却査定／直接買取提示）を選択してください', self.html)
        deploy = (ROOT / 'deploy.py').read_text(encoding='utf-8')
        self.assertIn("quoteType&&quoteType.value!=='unknown'", deploy)

    def test_result_labels_quotes_without_claiming_completed_sale(self):
        self.assertIn("const mode=document.getElementById('q'+i+'t').value", self.html)
        self.assertIn("mode:mode,price:price", self.html)
        self.assertIn("x.mode==='buyout'?'直接買取の提示'", self.html)
        self.assertIn("x.mode==='broker'?'仲介の査定'", self.html)
        self.assertIn('表示順位は入力金額を基にした税前の見込みです', self.html)
        self.assertIn('提示価格の根拠・有効期限・引渡条件を確認', self.html)
        self.assertNotIn("gtag('event','affiliate_click'", self.script)


if __name__ == '__main__':
    unittest.main()
