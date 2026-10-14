from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

# These implementation placeholders must never appear on public pages.
FORBIDDEN_PUBLIC_PHRASES = (
    "準備中",
    "ASP提携承認後",
    "広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。",
)

# Affiliate clicks should be sent through GA4's gtag API when GA4 is configured,
# rather than relying only on a raw dataLayer push.
RAW_AFFILIATE_EVENT = "window.dataLayer.push({event:'affiliate_click'"


def main() -> int:
    if not DIST.exists():
        print("dist/ not found. Run build.py first.", file=sys.stderr)
        return 2

    html_files = list(DIST.rglob("*.html"))
    if not html_files:
        print("No generated HTML found in dist/.", file=sys.stderr)
        return 2

    violations: list[str] = []

    # An approved offer must not go live without a configured conversion meter.
    # No offers configured => informational MVP is still allowed to deploy.
    config = json.loads((ROOT / "site_data.json").read_text(encoding="utf-8"))
    active_offers = [o for o in config.get("offers", []) if (o.get("url") or "").strip()]
    ga4_id = (config.get("ga4_id") or "").strip()
    if ga4_id and not re.fullmatch(r"G-[A-Z0-9]+", ga4_id):
        violations.append("site_data.json: invalid GA4 measurement ID")
    if active_offers and not ga4_id:
        violations.append("site_data.json: active affiliate offers require a GA4 measurement ID")

    for path in html_files:
        text = path.read_text(encoding="utf-8")

        for phrase in FORBIDDEN_PUBLIC_PHRASES:
            if phrase in text:
                violations.append(f"{path.relative_to(ROOT)}: public placeholder: {phrase}")

        # All full HTML pages must be measurable, even before an ASP link is approved.
        # The verification HTML is deliberately excluded because it has no <head>.
        if ga4_id and "</head>" in text.lower():
            expected_src = f"googletagmanager.com/gtag/js?id={ga4_id}"
            if expected_src not in text:
                violations.append(f"{path.relative_to(ROOT)}: configured GA4 tag is missing or uses a different ID")
            if text.count("googletagmanager.com/gtag/js") != 1:
                violations.append(f"{path.relative_to(ROOT)}: GA4 script tag must appear exactly once")
            if f"gtag(\'config\',\'{ga4_id}\')" not in text:
                violations.append(f"{path.relative_to(ROOT)}: GA4 config call is missing or mismatched")

        has_affiliate = 'class="button invert affiliate"' in text
        has_ga4 = "googletagmanager.com/gtag/js" in text
        if has_affiliate and not has_ga4:
            violations.append(f"{path.relative_to(ROOT)}: affiliate CTA is missing a GA4 tag")
        if has_affiliate and RAW_AFFILIATE_EVENT in text:
            violations.append(
                f"{path.relative_to(ROOT)}: affiliate_click uses raw dataLayer push; use gtag('event', ...)"
            )
        if has_affiliate and "gtag('event','affiliate_click'" not in text:
            violations.append(f"{path.relative_to(ROOT)}: affiliate CTA has no gtag affiliate_click handler")

    if violations:
        print("Public quality gate failed:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print(f"Public quality gate passed: {len(html_files)} HTML files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
