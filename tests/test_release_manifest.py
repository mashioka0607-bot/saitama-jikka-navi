"""A healthy stale deployment must fail the commit freshness check."""
import json
import unittest
from unittest.mock import patch
from scripts.check_live_site import PROBES, inspect, validate_release_manifest


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

    def test_stale_manifest_waits_without_probing_old_pages(self):
        """A stale but healthy release must use one request per retry."""
        base = "https://example.invalid"
        urls = []

        class Response:
            status = 200

            def __init__(self, url):
                self.url = url

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def geturl(self):
                return self.url

            def read(self, size):
                return json.dumps({"git_sha": self_sha}).encode()[:size]

        self_sha = self.OLD

        def fake_urlopen(request, timeout):
            urls.append(request.full_url)
            return Response(request.full_url)

        with patch("scripts.check_live_site.urlopen", side_effect=fake_urlopen):
            problems = inspect(base, self.NEW)
        self.assertEqual(urls, [base + "/release.json"])
        self.assertEqual(len(problems), 1)
        self.assertIn("stale production commit", problems[0])

    def test_current_manifest_probes_every_public_resource(self):
        """Once Pages serves the right commit, run all seven HTTP checks."""
        base = "https://example.invalid"
        seen = []

        class Response:
            status = 200

            def __init__(self, url, payload):
                self.url = url
                self.payload = payload

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def geturl(self):
                return self.url

            def read(self, size):
                return self.payload.encode("utf-8")[:size]

        def fake_urlopen(request, timeout):
            url = request.full_url
            seen.append(url)
            path = url.removeprefix(base)
            if path == "/release.json":
                content = json.dumps({"git_sha": self.NEW})
            else:
                content = PROBES[path]
            return Response(url, content)

        with patch("scripts.check_live_site.urlopen", side_effect=fake_urlopen):
            self.assertEqual(inspect(base, self.NEW), [])
        self.assertEqual(seen[0], base + "/release.json")
        self.assertEqual(seen[1:], [base + path for path in PROBES])


if __name__ == "__main__":
    unittest.main()
