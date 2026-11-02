"""Koshigaya: avoid suggesting a grant for all vacant houses or live budget availability."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = "https://www.city.koshigaya.saitama.jp/kurashi_shisei/kurashi/sumai/akiya/koshigaya_contents_akiyakaisyuu.html"


class KoshigayaGrantTests(unittest.TestCase):
    def test_official_conditions_are_shared_by_data_public_selector_and_static_page(self):
        data = json.loads((ROOT / "data/demolition_grants_2026.json").read_text(encoding="utf-8"))
        city = next(x for x in data["municipalities"] if x["municipality"] == "越谷市")
        self.assertEqual(city["official_url"], OFFICIAL)
        self.assertEqual(city["status_as_of"], "2026-11-03")
        self.assertNotIn("受付中", city["status"])
        self.assertIn("未接道敷地なら上限50万円", city["note"])
        self.assertIn("特定空家等", city["note"])
        self.assertIn("交付決定前", city["contract_timing"])
        js = (ROOT / "static_pages/kaitai-check/grants.js").read_text(encoding="utf-8")
        row = next(x for x in js.splitlines() if x.startswith("['越谷市'"))
        for value in ("2026-04-06", "特定空家等", "未接道敷地は上限50万円",
                      "交付決定前", "市内事業者", "予算残額・受付可否は未確認", OFFICIAL):
            self.assertIn(value, row)
        page = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        section = page.split('id="koshigaya-grant-2026"', 1)[1].split("</p>", 1)[0]
        for value in ("特定空家等", "未接道敷地なら上限50万円", "現在の受付可否・予算残額は未確認",
                      "交付決定前", "/tedori-hikaku/", OFFICIAL):
            self.assertIn(value, section)


if __name__ == "__main__":
    unittest.main()
