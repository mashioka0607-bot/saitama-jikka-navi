from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / "build.py"

FORBIDDEN = {
    "empty ASP placeholder": "ASP提携承認後にリンクを設定します。現在は情報提供のみです。",
    "global ad placeholder": "広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。",
    "unguarded affiliate dataLayer": "window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'affiliate_click'",
    "unguarded diagnosis dataLayer": "window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'diagnosis_complete'});",
}


def main() -> int:
    text = BUILD.read_text(encoding="utf-8")
    failures = [name for name, needle in FORBIDDEN.items() if needle in text]
    if "sitemap.xml" not in text:
        failures.append("build does not generate sitemap.xml")
    if "robots.txt" not in text:
        failures.append("build does not generate robots.txt")
    # deploy.py applies the quote-comparison patch before this gate.
    # Verify the published source offers both official next steps, not just a calculation.
    tedori = (ROOT / "static_pages/tedori-hikaku/index.html").read_text(encoding="utf-8")
    if "tedori_real_quotes_v2" not in tedori:
        failures.append("real appraisal comparison v2 missing from curated page")
    if "window.gtag('event',rows.length>=2?'real_appraisal_compare':'real_appraisal_single_quote'" not in tedori:
        failures.append("GA4 must distinguish single quote from real multi-quote comparison")
    if "window.dataLayer.push({event:'real_appraisal_compare'" in tedori:
        failures.append("real_appraisal_compare uses raw dataLayer instead of gtag event")
    for url in (
        "https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html",
        "https://www.pref.saitama.lg.jp/a1107/akiyabanku.html",
    ):
        if url not in tedori:
            failures.append(f"official next-step link missing from quote comparison: {url}")
    if failures:
        print("SEO/quality gate failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("SEO/quality gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
