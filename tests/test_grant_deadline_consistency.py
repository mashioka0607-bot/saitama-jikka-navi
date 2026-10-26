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


if __name__ == "__main__":
    unittest.main()
