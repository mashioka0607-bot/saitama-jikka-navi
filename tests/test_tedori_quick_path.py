import re
import unittest
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "dist" / "tedori-hikaku" / "index.html"


class TedoriQuickPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.markup = SITE.read_text(encoding="utf-8")

    def test_shortcuts_target_real_calculators(self):
        html = self.markup
        self.assertEqual(html.count('id="tedori-quick-path"'), 1)
        self.assertIn('href="#calc" data-compare-stage="estimate"', html)
        self.assertIn('href="#tedori_real_quotes_v2" data-compare-stage="real_quotes"', html)
        self.assertIn('id="calc"', html)
        self.assertIn('id="tedori_real_quotes_v2"', html)

    def test_paths_are_visible_above_explanations(self):
        html = self.markup
        self.assertLess(html.index('id="tedori-quick-path"'), html.index('id="sample-value-disclosure"'))
        self.assertLess(html.index('id="tedori-quick-path"'), html.index('id="calc"'))
        self.assertLess(html.index('id="tedori-quick-path"'), html.index('id="tedori_real_quotes_v2"'))

    def test_tracking_has_no_user_entered_data_and_no_affiliate_url(self):
        html = self.markup
        self.assertEqual(html.count('id="tedori-quick-path-measure"'), 1)
        block = re.search(r'<script id="tedori-quick-path-measure">([\s\S]*?)</script>', html)
        self.assertIsNotNone(block)
        script = block.group(1)
        self.assertIn("'compare_path_select'", script)
        self.assertIn("comparison_stage:link.dataset.compareStage", script)
        self.assertIn("source_page:window.location.pathname", script)
        self.assertNotIn(".value", script)
        self.assertNotIn("affiliate_click", script)
        nav = re.search(r'<section class="section notice" id="tedori-quick-path"[\s\S]*?</section>', html)
        self.assertIsNotNone(nav)
        self.assertNotIn('href="https:', nav.group(0))
        self.assertNotIn('class="affiliate"', nav.group(0))


if __name__ == "__main__":
    unittest.main()
