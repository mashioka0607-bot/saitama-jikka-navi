"""Kuki City's demolition and community-use renovation grants are distinct."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMOLITION = "https://www.city.kuki.lg.jp/kurashi/sumai/akiya/1003481.html"
REUSE = "https://www.city.kuki.lg.jp/kurashi/sumai/akiya/1003477.html"


class KukiDistinctGrantTests(unittest.TestCase):
    def test_kuki_primary_application_deadline_is_demolition_only(self):
        data = json.loads((ROOT / "data/demolition_grants_2026.json").read_text(encoding="utf-8"))
        row = next(x for x in data["municipalities"] if x["municipality"] == "久喜市")
        self.assertEqual(row["official_url"], DEMOLITION)
        self.assertIn("2026-11-30", row["deadline"])
        self.assertIn("11月2日", row["note"])
        self.assertIn("利活用補助金", row["note"])
        self.assertIn(REUSE, row["note"])

    def test_crawlable_html_discloses_expired_reuse_consultation(self):
        page = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        self.assertIn('id="kuki-2026-deadline"', page)
        reuse = page.split('id="kuki-reuse-2026-deadline"', 1)[1].split("</p>", 1)[0]
        for value in ("解体", "別制度", "11月2日", "経過済み", "11月30日", "未確認", REUSE):
            with self.subTest(value=value):
                self.assertIn(value, reuse)

    def test_city_selector_does_not_use_reuse_deadline_for_demolition(self):
        js = (ROOT / "static_pages/kaitai-check/grants.js").read_text(encoding="utf-8")
        row = next(line for line in js.splitlines() if line.startswith("['久喜市'"))
        for value in ("2026-11-30", "11月2日", "別制度", "新規受理可否は未確認", DEMOLITION, REUSE):
            with self.subTest(value=value):
                self.assertIn(value, row)


if __name__ == "__main__":
    unittest.main()
