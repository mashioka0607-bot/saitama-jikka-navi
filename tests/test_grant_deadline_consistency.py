"""Regression tests: every reviewed municipal subsidy deadline must be public.

The official source for Fujimi City's 2026 program lists three distinct dates:
application, post-work report, and property-tax subsidy application.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import check_grant_status_consistency as guard


class PublishedGrantDeadlineTests(unittest.TestCase):
    def test_current_reviewed_deadlines_are_all_visible(self):
        self.assertEqual(guard.check(), [])

    def test_missing_separate_deadline_is_rejected(self):
        source = guard.PUBLIC_JS.read_text(encoding="utf-8")
        for date in ("2027-03-31", "2027-03-15"):
            with self.subTest(date=date):
                # Simulate publishing the application date but accidentally
                # omitting either post-work or tax-subsidy deadline.
                broken = source.replace(date, "期日未掲載")
                self.assertNotEqual(broken, source)
                with tempfile.TemporaryDirectory() as td:
                    fake_js = Path(td) / "grants.js"
                    fake_js.write_text(broken, encoding="utf-8")
                    with patch.object(guard, "PUBLIC_JS", fake_js):
                        issues = guard.check()
                self.assertTrue(
                    any("富士見市: reviewed deadline " + date in issue
                        for issue in issues),
                    issues,
                )


    def test_sayama_and_kawajima_decision_gates_are_public(self):
        import json
        rows = guard.public_rows(guard.PUBLIC_JS.read_text(encoding="utf-8"))
        data = json.loads(guard.DATA.read_text(encoding="utf-8"))
        reviewed = {item["municipality"]: item for item in data["municipalities"]}
        for city in ("狭山市", "川島町"):
            self.assertIn(city, rows)
            self.assertEqual(rows[city][4], reviewed[city]["official_url"])
            self.assertIn("未確認", " ".join(rows[city][1:4]))
            self.assertIn("交付決定", rows[city][3])
        sayama = rows["狭山市"][3]
        for gate in ("3,000万円特別控除", "市内業者上限50万円",
                     "市外業者上限40万円", "建築確認", "両方"):
            self.assertIn(gate, sayama)
        kawajima = rows["川島町"][3]
        for gate in ("家財整理", "上限25万円", "解体", "上限100万円",
                     "併用可否は未確認", "相続人全員"):
            self.assertIn(gate, kawajima)


if __name__ == "__main__":
    unittest.main()
