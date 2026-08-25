from __future__ import annotations
import json, html, pathlib, shutil
from urllib.parse import urljoin
ROOT=pathlib.Path(__file__).resolve().parent
DIST=ROOT/'dist'
SITE=json.loads((ROOT/'site_data.json').read_text(encoding='utf-8'))
PAGES=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))

def esc(s): return html.escape(str(s),quote=True)
def canonical(path='/'):
    base=SITE['base_url'].rstrip('/')+'/'
    return urljoin(base,path.lstrip('/'))
def nav(): return '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/kawagoe-shi/mitsumori-check/">見積チェック</a><a href="/faq/">FAQ</a></nav>'
def ga():
    g=SITE.get('ga4_id','').strip()
    if not g:return ''
    return f'''<script async src="https://www.googletagmanager.com/gtag/js?id={esc(g)}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{esc(g)}');</script>'''
def offer_cta(offer_id='primary',context='content'):
    o=next((x for x in SITE.get('offers',[]) if x.get('id')==offer_id),None)
    if not o:return ''
    u=o.get('url','').strip()
    if u:
        return f'''<aside class="cta"><span class="pr">PR</span><h2>{esc(o['name'])}</h2><p>依頼条件・対応範囲・料金を確認し、必要に応じて複数社を比較してください。</p><a class="button invert affiliate" data-offer="{esc(offer_id)}" data-context="{esc(context)}" rel="sponsored noopener" target="_blank" href="{esc(u)}">{esc(o.get('label','無料見積もりを確認'))}</a><small>広告・アフィリエイトリンクです。利用者の追加負担はありません。</small></aside>'''
    return f'''<aside class="cta muted"><span class="pr">準備中</span><h2>{esc(o['name'])}</h2><p>ASP提携承認後にリンクを設定します。現在は情報提供のみです。</p></aside>'''
def layout(title,desc,body,path='/',schema=None):
    st=''.join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in ([schema] if isinstance(schema,dict) else (schema or [])))
    og=f'''<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)} | {esc(SITE['site_name'])}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{esc(canonical(path))}">'''
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | {esc(SITE['site_name'])}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{esc(canonical(path))}"><meta name="robots" content="index,follow,max-image-preview:large">{og}<link rel="stylesheet" href="/assets/style.css">{ga()}{st}</head><body><header><div class="wrap header"><a class="brand" href="/">{esc(SITE['site_name'])}</a>{nav()}</div></header><div class="adnote">広告を掲載する場合は「PR」「広告」をリンク付近にも明示します。</div><main class="wrap">{body}</main><footer><div class="wrap footer"><div><strong>{esc(SITE['site_name'])}</strong><p>{esc(SITE['tagline'])}</p></div><div><a href="/operator/">運営者情報</a> · <a href="/advertising-policy/">広告ポリシー</a> · <a href="/privacy/">プライバシー</a></div></div></footer><script>document.querySelectorAll('.affiliate').forEach(a=>a.addEventListener('click',()=>{{window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'affiliate_click',offer:a.dataset.offer,context:a.dataset.context}})}}));</script></body></html>'''
def write(path,content):
    out=DIST/path
    if out.suffix!='.html':out=out/'index.html'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(content,encoding='utf-8')

if DIST.exists(): shutil.rmtree(DIST)
(DIST/'assets').mkdir(parents=True)
CSS=r''':root{--ink:#15221c;--sub:#5a6761;--line:#dae5df;--paper:#fbfdfc;--soft:#eef6f1;--accent:#17633f;--accent2:#103d2b;--warn:#fff7df}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--ink);background:var(--paper);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans JP",sans-serif;line-height:1.8}a{color:var(--accent)}.wrap{max-width:1080px;margin:auto;padding:0 22px}header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10}.header{display:flex;align-items:center;justify-content:space-between;min-height:68px;gap:20px}.brand{font-weight:900;text-decoration:none;color:var(--ink);letter-spacing:-.02em}nav{display:flex;gap:15px;font-size:14px;flex-wrap:wrap}nav a{text-decoration:none;color:var(--sub)}.adnote{text-align:center;padding:6px 16px;background:#f4f6f5;color:#6d756f;font-size:11px}.hero{padding:64px 0 34px}.eyebrow{font-size:12px;font-weight:800;letter-spacing:.08em;color:var(--accent);text-transform:uppercase}.hero h1{font-size:clamp(31px,5vw,56px);line-height:1.16;letter-spacing:-.035em;margin:.25em 0}.lead{font-size:18px;color:var(--sub);max-width:790px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;text-decoration:none;color:var(--ink);transition:.15s}.card:hover{transform:translateY(-1px);border-color:#9db5a8}.card small{color:var(--accent);font-weight:800}.card h2,.card h3{margin:.3em 0;line-height:1.45}.section{padding:25px 0}.section h2{font-size:27px;line-height:1.4;margin-bottom:10px}.section ul,.section ol{padding-left:1.25em}.notice{background:var(--soft);border-left:4px solid var(--accent);padding:18px 20px;border-radius:8px}.warning{background:var(--warn);border-left:4px solid #d9a515;padding:18px 20px;border-radius:8px}.cta{margin:30px 0;padding:26px;border-radius:14px;background:var(--accent2);color:#fff}.cta h2{margin:.25em 0}.cta .pr{display:inline-block;font-size:11px;font-weight:900;border:1px solid currentColor;border-radius:99px;padding:2px 7px}.button{display:inline-block;border:0;cursor:pointer;background:var(--accent);color:#fff;padding:13px 20px;border-radius:9px;font-weight:900;text-decoration:none}.button.invert{background:#fff;color:var(--accent2)}.cta small{display:block;margin-top:8px;opacity:.82}.cta.muted{background:#eef2ef;color:var(--ink)}.crumb{font-size:13px;color:var(--sub);padding-top:20px}.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.fact{border:1px solid var(--line);padding:18px;border-radius:12px;background:#fff}.diagnosis{display:grid;gap:16px;max-width:760px}.diagnosis label{font-weight:800}.diagnosis select,.diagnosis input{width:100%;padding:11px;border:1px solid #bac8bf;border-radius:8px;background:#fff}.result{display:none;margin-top:20px;padding:22px;background:#fff;border:2px solid var(--accent);border-radius:12px}.sources{font-size:14px}.sources li{margin-bottom:7px}.footer{display:grid;grid-template-columns:2fr 1fr;gap:20px;padding-top:40px;padding-bottom:40px}footer{margin-top:70px;background:#f0f4f1;border-top:1px solid var(--line);font-size:14px}@media(max-width:760px){.header{align-items:flex-start;padding-top:14px;padding-bottom:14px;flex-direction:column}nav{gap:10px}.grid,.facts,.footer{grid-template-columns:1fr}.hero{padding-top:42px}.hero h1{font-size:35px}.lead{font-size:16px}}'''
(DIST/'assets/style.css').write_text(CSS,encoding='utf-8')

priority=['kawagoe-shi/jikka-katazuke-enkaku','kawagoe-shi/tachiai-fuyo','kawagoe-shi/mitsumori-check','kawagoe-shi/taikyo-kigen','kawagoe-shi/ikkenya-katazuke','kawagoe-shi/ippan-haikibutsu','kawagoe-shi/kichohin-tansaku','kawagoe-shi/shisetsu-nyukyo','kawagoe-shi/kaitori-sousai']
lookup={p['slug']:p for p in PAGES}; selected=[lookup[x] for x in priority if x in lookup]
cards=''.join(f'<a class="card" href="/{esc(p["slug"])}/"><small>{esc(p["eyebrow"])}</small><h3>{esc(p["h1"])}</h3><p>{esc(p["description"])}</p></a>' for p in selected)
body=f'''<section class="hero"><div class="eyebrow">Kawagoe / Family Home Cleanup</div><h1>遠方からの実家片付けを、<br>迷わず進める。</h1><p class="lead">川越市を中心に、立ち会い不要・鍵預かり・一軒家・貴重品探索・施設入居後・退去期限など「依頼直前の困りごと」から手順を整理します。</p><p><a class="button" href="/shindan/">3分で進め方を整理する</a></p></section><section class="section"><div class="facts"><div class="fact"><strong>自治体一次情報</strong><br>廃棄物ルール・許可業者を公式情報で確認</div><div class="fact"><strong>遠方向け</strong><br>鍵預かり・写真報告・立ち会い条件を整理</div><div class="fact"><strong>比較重視</strong><br>安さだけでなく見積条件を揃える</div></div></section><section class="section"><h2>まず確認したいこと</h2><div class="grid">{cards}</div></section><section class="section notice"><strong>川越市の重要ルール</strong><p>家庭の遺品整理で出る不用品は一般廃棄物です。川越市は自己搬入または対応可能な一般廃棄物収集運搬業許可業者への依頼を案内しています。</p><p><a href="https://www.city.kawagoe.saitama.jp/kurashi/gomi/1002380/1019544.html" target="_blank" rel="noopener">川越市公式案内</a></p></section>{offer_cta('primary','home')}'''
write('index.html',layout('遠方からの実家片付け・遺品整理ガイド','川越市を中心に、遠方からの実家片付け、立ち会い不要、鍵預かり、遺品整理の見積比較と自治体ルールを整理します。',body,'/'))

for p in PAGES:
    secs=''
    for heading,items in p['sections']:
        lis=''.join(f'<li>{esc(x)}</li>' for x in items)
        secs+=f'<section class="section"><h2>{esc(heading)}</h2><ul>{lis}</ul></section>'
    mid=offer_cta('primary',p['slug']) if p['slug'] in priority[:5] else ''
    body=f'''<div class="crumb"><a href="/">ホーム</a> / {esc(p['eyebrow'])}</div><section class="hero"><div class="eyebrow">{esc(p['eyebrow'])}</div><h1>{esc(p['h1'])}</h1><p class="lead">{esc(p['lead'])}</p></section>{secs}{mid}<section class="section notice"><strong>自治体情報も確認</strong><p>川越市では、家庭から出る遺品整理の不用品は一般廃棄物として扱われます。</p></section>'''
    write(p['slug'],layout(p['title'],p['description'],body,'/'+p['slug']+'/'))

# simple diagnostic
shindan='''<section class="hero"><div class="eyebrow">Diagnosis</div><h1>実家片付けの進め方診断</h1><p class="lead">遠方・立ち会い・退去期限の有無から、最初に確認する順番を整理します。</p></section><section class="section"><form class="diagnosis" onsubmit="event.preventDefault();document.getElementById('r').style.display='block';window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'diagnosis_complete'});"><label>立ち会いできますか？<select><option>できる</option><option>難しい</option></select></label><label>退去期限がありますか？<select><option>ない</option><option>ある</option></select></label><button class="button">診断する</button></form><div id="r" class="result"><strong>まず見積条件を揃えて比較してください。</strong><p>立ち会いが難しい場合は、鍵預かり・作業前後の写真・貴重品探索・追加料金条件を先に確認すると進めやすくなります。</p></div></section>'''
write('shindan',layout('実家片付けの進め方診断','遠方からの実家片付けで最初に確認する順番を整理します。',shindan,'/shindan/'))

faq='''<section class="hero"><h1>よくある質問</h1></section><section class="section"><h2>立ち会いなしでも依頼できますか？</h2><p>対応可否は業者ごとに異なります。鍵の受け渡し方法、作業前後写真、貴重品探索、追加料金条件を確認してください。</p><h2>家庭ごみを誰でも運べますか？</h2><p>家庭から出る一般廃棄物の収集運搬には自治体の許可が関係します。必ず自治体公式情報を確認してください。</p></section>'''
write('faq',layout('よくある質問','実家片付け・遺品整理のよくある質問。',faq,'/faq/'))

for slug,title,text in [('operator','運営者情報',f"運営者：{SITE.get('operator_name','')}"),('advertising-policy','広告ポリシー','当サイトは今後アフィリエイト広告を掲載する場合があります。広告リンク付近にPR・広告表示を行います。'),('privacy','プライバシーポリシー','アクセス解析を導入する場合があります。個人情報は目的外利用しません。')]:
    write(slug,layout(title,title,f'<section class="hero"><h1>{esc(title)}</h1></section><section class="section"><p>{esc(text)}</p></section>','/'+slug+'/'))

urls=['/','/shindan/','/faq/','/operator/','/advertising-policy/','/privacy/']+[f'/{p["slug"]}/' for p in PAGES]
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{esc(canonical(u))}</loc></url>' for u in urls)+'</urlset>',encoding='utf-8')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+canonical('/sitemap.xml')+'\n',encoding='utf-8')
print(f'Built {len(urls)} indexable URLs -> {DIST}')
