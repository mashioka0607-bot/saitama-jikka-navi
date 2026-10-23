"""Regression tests for published affiliate links and GA4 quality gates.

Tests are offline and use synthetic URLs; no affiliate link or tracking ID is published.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_public_quality.py"
spec = importlib.util.spec_from_file_location("public_quality_under_test", MODULE_PATH)
quality = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(quality)

GA4 = "G-TEST123"
URL = "https://example.invalid/offer?a=1&b=2"


def html(*, href=URL, classes="invert affiliate button", offer_id="primary",
         with_ga4=True, with_event=True, raw_event=False):
    head = (
        '<script src="https://www.googletagmanager.com/gtag/js?id=' + GA4 + '"></script>'
        + "<script>gtag('config','" + GA4 + "');</script>"
    ) if with_ga4 else ""
    event = (
        "<script>gtag('event','affiliate_click',{send_to:'" + GA4 + "'});</script>"
        if with_event else ""
    )
    if raw_event:
        event += "<script>window.dataLayer.push({event:'affiliate_click'});</script>"
    return (
        "<!doctype html><html><head>" + head + "</head><body>"
        + "<a class='" + classes + "' data-offer='" + offer_id
        + "' href='" + href.replace("&", "&amp;") + "'>査定</a>"
        + event + "</body></html>"
    )


class PublicQualityGateTests(unittest.TestCase):
    def run_gate(self, markup, *, offers=None, ga4_id=GA4):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dist = root / "dist"
            dist.mkdir()
            (dist / "index.html").write_text(markup, encoding="utf-8")
            (root / "site_data.json").write_text(
                json.dumps({"ga4_id": ga4_id, "offers": offers if offers is not None
                            else [{"id": "primary", "url": URL}]}),
                encoding="utf-8",
            )
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch.object(quality, "ROOT", root), patch.object(quality, "DIST", dist):
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    code = quality.main()
            return code, stdout.getvalue() + stderr.getvalue()

    def test_valid_cta_with_reordered_css_and_html_escaped_url(self):
        code, log = self.run_gate(html())
        self.assertEqual(code, 0, log)

    def test_missing_cta_blocks_active_offer(self):
        code, log = self.run_gate("<html><head></head><body>情報</body></html>")
        self.assertEqual(code, 1)
        self.assertIn("no matching published affiliate CTA", log)

    def test_wrong_destination_is_rejected(self):
        code, log = self.run_gate(html(href="https://example.invalid/wrong"))
        self.assertEqual(code, 1)
        self.assertIn("URL differs", log)

    def test_unconfigured_offer_id_is_rejected(self):
        code, log = self.run_gate(html(offer_id="unknown"))
        self.assertEqual(code, 1)
        self.assertIn("unconfigured offer ID", log)

    def test_missing_ga4_tag_is_rejected(self):
        code, log = self.run_gate(html(with_ga4=False))
        self.assertEqual(code, 1)
        self.assertIn("missing a GA4 tag", log)

    def test_missing_affiliate_click_handler_is_rejected(self):
        code, log = self.run_gate(html(with_event=False))
        self.assertEqual(code, 1)
        self.assertIn("no gtag affiliate_click handler", log)

    def test_raw_datalayer_event_is_rejected(self):
        code, log = self.run_gate(html(raw_event=True))
        self.assertEqual(code, 1)
        self.assertIn("raw dataLayer push", log)

    def test_active_offer_requires_ga4_id(self):
        code, log = self.run_gate(html(with_ga4=False), ga4_id="")
        self.assertEqual(code, 1)
        self.assertIn("require a GA4 measurement ID", log)

    def test_informational_mvp_without_offers_or_ga4_passes(self):
        code, log = self.run_gate("<html><head></head><body>情報</body></html>",
                                  offers=[], ga4_id="")
        self.assertEqual(code, 0, log)


class AffiliateDeployIntegrationTests(unittest.TestCase):
    """Exercise the actual deploy pipeline with a synthetic approved offer.

    Work in a temporary copy: no real affiliate URL or GA4 ID is committed,
    and deploy.py's source patchers cannot modify the checkout.
    """

    def test_synthetic_offer_survives_full_deploy_and_quality_gate(self):
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "site"
            shutil.copytree(
                source, project,
                ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc"),
            )
            config_path = project / "site_data.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["ga4_id"] = GA4
            config["offers"] = [{
                "id": "primary",
                "name": "架空の査定サービス（CI専用）",
                "url": URL,
                "label": "無料査定",
            }]
            config_path.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")

            completed = subprocess.run(
                [sys.executable, "deploy.py"], cwd=project,
                capture_output=True, text=True, timeout=90,
            )
            self.assertEqual(
                completed.returncode, 0,
                completed.stdout + "\n" + completed.stderr,
            )
            homepage = (project / "dist" / "index.html").read_text(encoding="utf-8")
            parser = quality.AffiliateLinkParser()
            parser.feed(homepage)
            self.assertIn(("primary", URL), parser.links)
            self.assertIn('gtag(\'event\',\'affiliate_click\'', homepage)
            self.assertIn('<span class="pr">PR</span>', homepage)
            self.assertNotIn(quality.RAW_AFFILIATE_EVENT, homepage)

            # Curated static pages are copied after build.py; they still need GA4.
            static_page = (project / "dist" / "tedori-hikaku" / "index.html").read_text(encoding="utf-8")
            self.assertEqual(static_page.count("googletagmanager.com/gtag/js?id=" + GA4), 1)
            diagnosis = (project / "dist" / "shindan" / "index.html").read_text(encoding="utf-8")
            self.assertEqual(diagnosis.count("googletagmanager.com/gtag/js?id=" + GA4), 1)
            self.assertIn("gtag('event','diagnosis_complete'", diagnosis)
            # Approved ASP URL must also appear at the strongest commercial
            # decision point, not only on generated home/area pages.
            self.assertIn('id="tedori-affiliate-next"', static_page)
            self.assertIn('data-context="tedori_compare_complete"', static_page)
            self.assertIn('href="' + URL.replace("&", "&amp;") + '"', static_page)
            self.assertIn("gtag('event','affiliate_click'", static_page)
            self.assertIn('form.addEventListener(\'submit\',function(){next.hidden=false;});', static_page)
            self.assertIn("gtag('event','diagnosis_to_tedori'", diagnosis)
            self.assertNotIn("window.dataLayer.push({event:'diagnosis_", diagnosis)
            self.assertIn("Public quality gate passed:", completed.stdout)


if __name__ == "__main__":
    unittest.main()
