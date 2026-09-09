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
    if failures:
        print("SEO/quality gate failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("SEO/quality gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
