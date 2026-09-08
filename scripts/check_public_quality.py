from __future__ import annotations

import pathlib
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
    for path in html_files:
        text = path.read_text(encoding="utf-8")

        for phrase in FORBIDDEN_PUBLIC_PHRASES:
            if phrase in text:
                violations.append(f"{path.relative_to(ROOT)}: public placeholder: {phrase}")

        has_affiliate = 'class="button invert affiliate"' in text
        has_ga4 = "googletagmanager.com/gtag/js" in text
        if has_affiliate and has_ga4 and RAW_AFFILIATE_EVENT in text:
            violations.append(
                f"{path.relative_to(ROOT)}: affiliate_click uses raw dataLayer push; use gtag('event', ...)"
            )

    if violations:
        print("Public quality gate failed:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print(f"Public quality gate passed: {len(html_files)} HTML files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
