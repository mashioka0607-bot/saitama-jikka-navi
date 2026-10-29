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


    def test_fukaya_separate_tax_reduction_is_sourced_and_not_sale_income(self):
        import json
        data = json.loads((ROOT / "data/demolition_grants_2026.json").read_text(encoding="utf-8"))
        fukaya = next(m for m in data["municipalities"] if m["municipality"] == "深谷市")
        relief = fukaya["post_demolition_tax_relief"]
        self.assertEqual(relief["duration_years"], 3)
        page = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        notice = page.split('id="grant-2026-primary-alert"', 1)[1].split("</section>", 1)[0]
        js = (ROOT / "static_pages/kaitai-check/grants.js").read_text(encoding="utf-8")
        for phrase in ("深谷市", "最大3年間", "固定資産税・都市計画税", "別途減免申請", "解体後すぐに売却", "売却等で納税義務者が変わった場合"):
            self.assertIn(phrase, notice)
        for phrase in ("深谷市", "最大3年間", "即時売却", "減免申請", "納税義務者", relief["official_url"]):
            self.assertIn(phrase, js)
        self.assertIn(relief["official_url"], notice)

    def test_municipality_selector_is_above_lengthy_deadline_alert(self):
        page = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        selector_title = '自治体を選んで「今、契約してよいか」確認'
        alert_id = 'id="grant-2026-primary-alert"'
        self.assertLess(page.index(selector_title), page.index(alert_id))
        selector = page.split(selector_title, 1)[1].split("</section>", 1)[0]
        self.assertIn('id="grant-city"', selector)
        self.assertIn('href="/tedori-hikaku/"', selector)



    def test_sakado_renovation_eligibility_is_not_sold_as_clearance_subsidy(self):
        import json
        data = json.loads((ROOT / "data/demolition_grants_2026.json").read_text(encoding="utf-8"))
        sakado = next(m for m in data["municipalities"] if m["municipality"] == "坂戸市")
        alternative = sakado["alternative_renovation_grant"]
        self.assertIn("5年以上", alternative["ownership_and_occupancy"])
        self.assertIn("売却", alternative["repayment"])
        self.assertIn("改修工事を伴わない家財処分は対象外", alternative["scope"])
        page = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        for phrase in ("5年以上居住", "改修工事を伴う家財処分", "5年以内に売却", "家財道具の処分費を対象外", alternative["official_url"]):
            self.assertIn(phrase, page)
        js = (ROOT / "static_pages/kaitai-check/grants.js").read_text(encoding="utf-8")
        for phrase in ("坂戸市", "5年以上の自己居住", "5年以内の売却", "改修を伴う家財処分", alternative["official_url"]):
            self.assertIn(phrase, js)

if __name__ == "__main__":
    unittest.main()
