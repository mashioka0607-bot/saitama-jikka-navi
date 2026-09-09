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
    (
        ".adnote{text-align:center;padding:6px 16px;background:#f4f6f5;color:#6d756f;font-size:11px}",
        "",
    ),
]

FORBIDDEN_AFTER = [
    "ASP提携承認後にリンクを設定します。現在は情報提供のみです。",
    "広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。",
    "window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'affiliate_click'",
    ".adnote{text-align:center",
]


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    changed = False
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count > 1:
            raise SystemExit(f"Refusing to patch: expected at most 1 match, found {count}: {old[:80]!r}")
        if count == 1:
            text = text.replace(old, new, 1)
            changed = True

    leftovers = [needle for needle in FORBIDDEN_AFTER if needle in text]
    if leftovers:
        raise SystemExit(f"Quality gate failed; stale public placeholders remain: {leftovers}")

    if changed:
        PATH.write_text(text, encoding="utf-8")
        print("Patched build.py: hidden empty offers, removed placeholder ad note/CSS, switched affiliate_click to gtag.")
    else:
        print("build.py already passes the P0 quality patch checks; no changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
