from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "build.py"

REPLACEMENTS = [
    (
        "    return f'''<aside class=\"cta muted\"><span class=\"pr\">準備中</span><h2>{esc(o['name'])}</h2><p>ASP提携承認後にリンクを設定します。現在は情報提供のみです。</p></aside>'''",
        "    return ''",
    ),
    (
        "</header><div class=\"adnote\">広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。</div><main class=\"wrap\">",
        "</header><main class=\"wrap\">",
    ),
    (
        "window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'affiliate_click',offer:a.dataset.offer,context:a.dataset.context}})",
        "if(typeof gtag==='function'){{gtag('event','affiliate_click',{{offer:a.dataset.offer,context:a.dataset.context}})}}",
    ),
]


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"Refusing to patch: expected exactly 1 match, found {count}: {old[:80]!r}")
        text = text.replace(old, new, 1)

    if text == original:
        raise SystemExit("No changes made")
    PATH.write_text(text, encoding="utf-8")
    print("Patched build.py: hidden empty offers, removed placeholder ad note, switched affiliate_click to gtag.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
