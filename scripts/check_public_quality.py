from __future__ import annotations

import json
from html.parser import HTMLParser
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

class AffiliateLinkParser(HTMLParser):
    """Read published affiliate anchors, not just configured offers."""
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        values = dict(attrs)
        if "affiliate" in (values.get("class") or "").split():
            self.links.append((values.get("data-offer") or "", values.get("href") or ""))


def main() -> int:
    if not DIST.exists():
        print("dist/ not found. Run build.py first.", file=sys.stderr)
        return 2

    html_files = list(DIST.rglob("*.html"))
    if not html_files:
        print("No generated HTML found in dist/.", file=sys.stderr)
        return 2

    violations: list[str] = []

    # Approved ASP links may go live before GA4: the ASP's own tracking records
    # applications/approved commissions. Validate GA4 only if configured.
    # Never invent an offer URL or relax the offer-ID/destination checks.
    config = json.loads((ROOT / "site_data.json").read_text(encoding="utf-8"))
    active_offers = [o for o in config.get("offers", []) if (o.get("url") or "").strip()]
    active_by_id = {o.get("id"): o["url"].strip() for o in active_offers if o.get("id")}
    if len(active_by_id) != len(active_offers):
        violations.append("site_data.json: affiliate offers need unique, nonempty IDs")
    rendered_offer_ids: set[str] = set()
    ga4_id = (config.get("ga4_id") or "").strip()
    if ga4_id and not re.fullmatch(r"G-[A-Z0-9]+", ga4_id):
        violations.append("site_data.json: invalid GA4 measurement ID")

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

        # Compare published affiliate hrefs with configured approved URLs.
        # HTMLParser decodes &amp; in query parameters before comparison.
        parser = AffiliateLinkParser()
        parser.feed(text)
        for offer_id, href in parser.links:
            expected_url = active_by_id.get(offer_id)
            if not expected_url:
                violations.append(f"{path.relative_to(ROOT)}: affiliate CTA uses unconfigured offer ID {offer_id!r}")
            elif href != expected_url:
                violations.append(f"{path.relative_to(ROOT)}: affiliate CTA URL differs from configured offer {offer_id!r}")
            else:
                rendered_offer_ids.add(offer_id)

        # Detect affiliate CTAs by parsed class tokens, independent of class order,
        # whitespace, or whether the HTML uses single/double quoted attributes.
        has_affiliate = bool(parser.links)
        has_ga4 = "googletagmanager.com/gtag/js" in text
        if has_affiliate and ga4_id and not has_ga4:
            violations.append(f"{path.relative_to(ROOT)}: affiliate CTA is missing a GA4 tag")
        if has_affiliate and RAW_AFFILIATE_EVENT in text:
            violations.append(
                f"{path.relative_to(ROOT)}: affiliate_click uses raw dataLayer push; use gtag('event', ...)"
            )
        if has_affiliate and ga4_id and "gtag('event','affiliate_click'" not in text:
            violations.append(f"{path.relative_to(ROOT)}: affiliate CTA has no gtag affiliate_click handler")

    for offer_id in active_by_id:
        if offer_id not in rendered_offer_ids:
            violations.append(f"site_data.json: active offer {offer_id!r} has no matching published affiliate CTA")

    # A prefecture-wide landing page must not send undecided visitors to
    # Kawagoe-only consultation or use Kawagoe-only metadata. Regional
    # article cards are allowed when explicitly labelled as Kawagoe examples.
    statewide_checks = {
        'index.html': (
            ('Kawagoe / Inherited Home', '川越市を中心に', '川越市にも原則無料の空き家相談窓口'),
            ('https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html',
             'https://www.pref.saitama.lg.jp/a1107/akiyabanku.html',
             '川越市の詳細ガイド（県内制度の具体例）'),
        ),
        'shindan/index.html': (
            ('川越市の相談先を整理', 'www.city.kawagoe.saitama.jp', '川越市の空き家管理連携先'),
            ('https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html',
             'https://www.pref.saitama.lg.jp/a1106/akiyakanrisyatouroku.html'),
        ),
    }
    for relative, (forbidden, required) in statewide_checks.items():
        page_path = DIST / relative
        if not page_path.exists():
            violations.append(f"{relative}: missing statewide page")
            continue
        page_text = page_path.read_text(encoding='utf-8')
        nav_match = re.search(r'<nav\b[^>]*>(.*?)</nav>', page_text, flags=re.DOTALL)
        if not nav_match:
            violations.append(f"{relative}: missing common navigation")
        else:
            for href in ('/tedori-hikaku/', '/kaitai-check/'):
                if f'href="{href}"' not in nav_match.group(1):
                    violations.append(f"{relative}: nav does not link to {href}")
            if '/kawagoe-shi/mitsumori-check/' in nav_match.group(1):
                violations.append(f"{relative}: statewide nav routes to Kawagoe-only estimate")
        for item in forbidden:
            if item in page_text:
                violations.append(f"{relative}: old Kawagoe-only scope: {item}")
        for item in required:
            if item not in page_text:
                violations.append(f"{relative}: statewide official route or regional scope missing: {item}")

    if violations:
        print("Public quality gate failed:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print(f"Public quality gate passed: {len(html_files)} HTML files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
