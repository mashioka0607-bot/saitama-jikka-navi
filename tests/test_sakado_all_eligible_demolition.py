"""Sakado municipal primary-source gate: all eligible buildings on a lot must be removed."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SakadoEligibleDemolitionTests(unittest.TestCase):
    def test_source_public_selector_and_crawlable_notice_match(self):
        data = json.loads((ROOT / "data/demolition_grants_2026.json").read_text(encoding="utf-8"))
        city = next(m for m in data["municipalities"] if m["municipality"] == "坂戸市")
        js = (ROOT / "static_pages/kaitai-check/grants.js").read_text(encoding="utf-8")
        row = next(line for line in js.splitlines() if line.startswith("['坂戸市'"))
        html = (ROOT / "static_pages/kaitai-check/index.html").read_text(encoding="utf-8")
        for phrase in ("補助対象物件すべてを除却", "一部"):
            self.assertIn(phrase, city["note"])
            self.assertIn(phrase, row)
        self.assertIn("敷地内の補助対象物件すべてを除却する工事", html)
        self.assertIn(city["official_url"], row)
        self.assertIn(city["official_url"], html)
        # Official city wording means all *eligible* buildings, not every shed or structure.
        self.assertNotIn("敷地内すべての建物を除却", row)


if __name__ == "__main__":
    unittest.main()
