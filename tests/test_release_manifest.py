"""A healthy stale deployment must fail the commit freshness check."""
import json
import unittest
from scripts.check_live_site import validate_release_manifest


class ReleaseManifestTests(unittest.TestCase):
    NEW = "a" * 40
    OLD = "b" * 40

    def test_current_release_passes(self):
        self.assertIsNone(validate_release_manifest(json.dumps({"git_sha": self.NEW}), self.NEW))

    def test_stale_deployment_fails(self):
        problem = validate_release_manifest(json.dumps({"git_sha": self.OLD}), self.NEW)
        self.assertIn("stale production commit", problem)

    def test_missing_or_invalid_manifest_fails(self):
        self.assertIn("invalid JSON", validate_release_manifest("<html>old deploy</html>", self.NEW))
        self.assertIn("missing or invalid git_sha", validate_release_manifest("{}", self.NEW))
        self.assertIn("missing or invalid git_sha", validate_release_manifest("[]", self.NEW))


if __name__ == "__main__":
    unittest.main()
