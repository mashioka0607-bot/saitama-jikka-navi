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
                       "早期終了", "2026年10月27日", "白岡市", "2026年10月13日時点",
                       "30万円", "家財道具の処分費用は対象外",
                       "工事完了から30日以内", "2027年3月12日",
                       "2027年3月31日", "2028年3月10日",
                       "解体後の固定資産税等にも別の補助制度", "最大2年度",
                       "解体後すぐに売却する場合は受給を前提に手残りへ加算しない",
                       "10月1日更新", "公図の写し", "地番図を代わりに提出できるかは未確認", "久喜支局"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, notice)
        for official_url in (
            "https://www.city.ageo.lg.jp/page/421263.html",
            "https://www.city.kawaguchi.lg.jp/soshiki/01130/040/akiyatoutaisaku/27633.html",
            "https://www.city.shiraoka.lg.jp/soshiki/seikatsukeizaibu/kankyoka/1_1/7523.html",
            "https://www.city.shiraoka.lg.jp/soshiki/seikatsukeizaibu/kankyoka/1_1/7524.html",
            "https://www.city.shiraoka.lg.jp/soshiki/soumubu/zeimuka/4/5/9997.html",
        ):
            self.assertIn(official_url, notice)
        self.assertIn("期限内でも当日の受理・予算残額を保証するものではありません", notice)
        js = (ROOT / "static_pages/kaitai-check/grants.js").read_text(encoding="utf-8")
        self.assertIn("市は2026-10-01更新ページで公図交付の廃止を案内", js)
        self.assertIn("地番図を代用できるかは環境課に確認", js)
        self.assertIn("https://www.city.shiraoka.lg.jp/soshiki/soumubu/zeimuka/4/5/9997.html", js)


if __name__ == "__main__":
    unittest.main()
