"""Public documentation must not republish subscriber-only ASP offer terms.

The public repository contains commercial research, but confidential program
terms received by email or seen only after ASP login must be kept out of it.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicAspResearchTest(unittest.TestCase):
    def test_public_runbook_has_privacy_rule(self):
        doc = (ROOT / "MONETIZATION.md").read_text(encoding="utf-8")
        self.assertIn("会員向けメール", doc)
        self.assertIn("公開GitHubリポジトリ", doc)

    def test_public_runbook_does_not_republish_member_only_offer(self):
        doc = (ROOT / "MONETIZATION.md").read_text(encoding="utf-8")
        self.assertNotIn("detail-not-partnered", doc)
        self.assertNotIn("メルマガ記載の成果区分", doc)
        self.assertNotIn("プログラム最新情報」メール", doc)
        self.assertIsNone(
            re.search(
                r"(?:会員向けメール|メルマガ).{0,150}(?:報酬|成果条件).{0,80}[0-9,]+円",
                doc,
                flags=re.S,
            )
        )


if __name__ == "__main__":
    unittest.main()
