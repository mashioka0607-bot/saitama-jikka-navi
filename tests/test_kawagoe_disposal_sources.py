"""Regression: distinguish scheduled bulky-waste pickup from walk-in self-delivery.

Checked against Kawagoe City's primary sources on 2026-11-01:
- https://www.city.kawagoe.saitama.jp/kurashi/gomi/1002469/1002474/1002476.html
- https://www.city.kawagoe.saitama.jp/faq/faq-gomi/1012638/1012643.html
- https://www.city.kawagoe.saitama.jp/kurashi/gomi/1002380/1002397.html
"""
from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "data" / "pages.json"
DIST = ROOT / "dist"


class KawagoeDisposalPrimarySources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {
            item["slug"]: item
            for item in json.loads(PAGES.read_text(encoding="utf-8"))
        }

    def _page_html(self, slug):
        path = DIST / slug / "index.html"
        self.assertTrue(path.exists(), f"Missing built article: {path}")
        return path.read_text(encoding="utf-8")

    def test_self_delivery_not_mislabeled_as_reservation_required(self):
        slug = "kawagoe-shi/sodaigomi-rule"
        item = self.pages[slug]
        article = " ".join(x for _heading, bullets in item["sections"] for x in bullets)
        self.assertNotIn("自己搬入も事前予約が必要です", article)
        self.assertIn("予約不要", article)
        self.assertIn("戸別収集は予約制", article)
        built = self._page_html(slug)
        self.assertIn("予約不要", built)
        self.assertIn("立ち会って品目を確認", built)

    def test_official_municipal_links_are_rendered_as_links(self):
        for slug in ("kawagoe-shi/sodaigomi-rule", "kawagoe-shi/tachiai-fuyo"):
            with self.subTest(slug=slug):
                built = self._page_html(slug)
                sources = self.pages[slug].get("official_sources") or []
                self.assertTrue(sources)
                for source in sources:
                    self.assertTrue(source["url"].startswith("https://www.city.kawagoe.saitama.jp/"))
                    self.assertIn('href="' + source["url"] + '"', built)

    def test_no_attendance_guide_discloses_city_pickup_attendance(self):
        built = self._page_html("kawagoe-shi/tachiai-fuyo")
        self.assertIn("市の粗大ごみ戸別収集は立ち会いが必要", built)
        self.assertIn("建物内からの大型家具搬出", built)
        self.assertIn("民間の片付け業者", built)


if __name__ == "__main__":
    unittest.main()
