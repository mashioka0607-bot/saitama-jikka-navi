"""Crawlable grant alerts: prevent returning to JS-only official deadline notices."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GrantAlertHtmlTests(unittest.TestCase):
    def test_recent_2026_primary_status_is_indexable_and_sourced(self):
        page = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        # This is intentionally static HTML: the JS city selector does not expose
        # its hidden options to search crawlers or script-disabled visitors.
        notice = page.split('id="grant-2026-primary-alert"', 1)[1].split("</section>", 1)[0]
        for phrase in ("上尾市", "2026年10月13日", "受付終了", "川口市",
                       "2026年10月30日", "11月13日", "2027年1月29日",
                       "早期終了", "2026年10月26日"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, notice)
        for official_url in (
            "https://www.city.ageo.lg.jp/page/421263.html",
            "https://www.city.kawaguchi.lg.jp/soshiki/01130/040/akiyatoutaisaku/27633.html",
        ):
            self.assertIn(official_url, notice)
        self.assertIn("期限内でも当日の受理・予算残額を保証するものではありません", notice)


if __name__ == "__main__":
    unittest.main()
