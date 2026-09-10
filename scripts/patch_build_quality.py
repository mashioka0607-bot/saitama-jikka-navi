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
        "window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'diagnosis_complete'});",
        "if(typeof gtag==='function'){gtag('event','diagnosis_complete')};",
    ),
    (
        ".adnote{text-align:center;padding:6px 16px;background:#f4f6f5;color:#6d756f;font-size:11px}",
        "",
    ),
]

# Insert discovery-file generation immediately before the build's final summary print.
# Appending it after the module body is unsafe because build.py executes top-to-bottom;
# an appended block can end up after the completion message or after future exit logic.
SEO_BLOCK = r'''
# SEO discovery files: keep these generated from the same build as the HTML.
urls = [canonical('/')]
urls += [canonical('/' + p['slug'].strip('/') + '/') for p in PAGES]
urls += [canonical('/shindan/'), canonical('/faq/'), canonical('/operator/'), canonical('/advertising-policy/'), canonical('/privacy/')]
urls = list(dict.fromkeys(urls))
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{esc(u)}</loc></url>\n' for u in urls) + '</urlset>\n', encoding='utf-8')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + canonical('/sitemap.xml') + '\n', encoding='utf-8')
'''

FORBIDDEN_AFTER = [
    "ASP提携承認後にリンクを設定します。現在は情報提供のみです。",
    "広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。",
    "window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'affiliate_click'",
    "window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'diagnosis_complete'});",
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

    if "DIST/'sitemap.xml'" not in text:
        marker = "print('built',len(PAGES),'pages + core pages')"
        count = text.count(marker)
        if count != 1:
            raise SystemExit(f"Refusing SEO patch: expected exactly 1 build-summary marker, found {count}")
        text = text.replace(marker, SEO_BLOCK.strip() + "\n\n" + marker, 1)
        changed = True

    leftovers = [needle for needle in FORBIDDEN_AFTER if needle in text]
    if leftovers:
        raise SystemExit(f"Quality gate failed; stale public placeholders or unguarded analytics remain: {leftovers}")
    if "DIST/'sitemap.xml'" not in text or "DIST/'robots.txt'" not in text:
        raise SystemExit("SEO quality gate failed: sitemap.xml or robots.txt generation is missing")

    if changed:
        PATH.write_text(text, encoding="utf-8")
        print("Patched build.py: P0 quality fixes plus sitemap.xml and robots.txt generation before build completion.")
    else:
        print("build.py already passes the P0 + SEO discovery patch checks; no changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
