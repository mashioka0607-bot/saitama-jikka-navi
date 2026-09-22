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
    (
        '<p><a href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1020433.html" target="_blank" rel="noopener">川越市公式の相談窓口を見る</a></p></section>{offer_cta(\'primary\',\'home\')}',
        '<p><a href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1020433.html" target="_blank" rel="noopener">川越市公式の相談窓口を見る</a></p></section><section class="section warning"><strong>9/27（日）｜予約なしで、解体・不用品回収/買取・相続/不動産をまとめて相談</strong><p>埼玉県・川越市などが案内する「空き家・相続もんだい解決フェスタ」が、ワカバウォークで10:00〜16:00に開催されます。実家の相続、家じまい・解体、不用品回収・買取など、片付け契約の前に整理したい論点を無料で確認できます。</p><p><a class="public-link" href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1022509.html" target="_blank" rel="noopener">川越市公式の開催案内を見る</a></p><hr><strong>次の公的情報｜9/23から遺言書説明会の申込開始</strong><p>10/23（金）に川越市立中央図書館で、法務局職員が相続ルール・遺言書作成のメリット・自筆証書遺言書保管制度を説明します。無料・要申込（9/23 9:30〜10/8 19:00）。相談会ではありません。</p><p><a class="public-link" href="https://www.city.kawagoe.saitama.jp/kosodate/kyouiku/1004652/1004661/1016300/1017711/1022809.html" target="_blank" rel="noopener">川越市公式の申込案内を見る</a></p><small>2026年9月22日時点の川越市公式情報。終了後は最新の公的な相続・空き家情報へ差し替えます。</small></section>{offer_cta(\'primary\',\'home\')}',
    ),
]

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
        print("Patched build.py: P0 quality fixes, current/next official-event CTA, sitemap.xml and robots.txt generation.")
    else:
        print("build.py already passes the P0 + SEO discovery patch checks; no changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
