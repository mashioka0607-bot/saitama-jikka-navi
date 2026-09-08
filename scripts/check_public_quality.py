from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

# Public pages must not expose implementation/ASP placeholders.
FORBIDDEN_WITHOUT_AFFILIATE = (
    "準備中",
    "ASP提携承認後",
    "広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。",
)


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
        has_affiliate = 'class="button invert affiliate"' in text
        if not has_affiliate:
            for phrase in FORBIDDEN_WITHOUT_AFFILIATE:
                if phrase in text:
                    violations.append(f"{path.relative_to(ROOT)}: {phrase}")

    if violations:
        print("Public quality gate failed:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print(f"Public quality gate passed: {len(html_files)} HTML files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
