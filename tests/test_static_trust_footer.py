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


if __name__ == "__main__":
    unittest.main()
