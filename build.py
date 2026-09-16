from __future__ import annotations
import json, html, pathlib, shutil
from urllib.parse import urljoin
ROOT=pathlib.Path(__file__).resolve().parent
DIST=ROOT/'dist'
SITE=json.loads((ROOT/'site_data.json').read_text(encoding='utf-8'))
PAGES=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))

def esc(s): return html.escape(str(s),quote=True)
def canonical(path='/'): return urljoin(SITE['base_url'].rstrip('/')+'/',path.lstrip('/'))
def nav(): return '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/kawagoe-shi/akiya-kazai-tekkyo/">売却・解体前</a><a href="/kawagoe-shi/mitsumori-check/">見積チェック</a><a href="/faq/">FAQ</a></nav>'
def ga():
    g=SITE.get('ga4_id','').strip()
    if not g:return ''
    return f'''<script async src="https://www.googletagmanager.com/gtag/js?id={esc(g)}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{esc(g)}');</script>'''
def offer_cta(offer_id='primary',context='content'):
    o=next((x for x in SITE.get('offers',[]) if x.get('id')==offer_id),None)
    if not o or not o.get('url','').strip():return ''
    return f'''<aside class="cta"><span class="pr">PR</span><h2>{esc(o['name'])}</h2><p>依頼条件・対応範囲・料金を確認し、必要に応じて複数社を比較してください。</p><a class="button invert affiliate" data-offer="{esc(offer_id)}" data-context="{esc(context)}" rel="sponsored noopener" target="_blank" href="{esc(o['url'])}">{esc(o.get('label','無料見積もりを確認'))}</a><small>広告・アフィリエイトリンクです。利用者の追加負担はありません。</small></aside>'''
def layout(title,desc,body,path='/',schema=None):
    st=''.join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in ([schema] if isinstance(schema,dict) else (schema or [])))
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | {esc(SITE['site_name'])}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{esc(canonical(path))}"><meta name="robots" content="index,follow,max-image-preview:large"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)} | {esc(SITE['site_name'])}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{esc(canonical(path))}"><link rel="stylesheet" href="/assets/style.css">{ga()}{st}</head><body><header><div class="wrap header"><a class="brand" href="/">{esc(SITE['site_name'])}</a>{nav()}</div></header><main class="wrap">{body}</main><footer><div class="wrap footer"><div><strong>{esc(SITE['site_name'])}</strong><p>{esc(SITE['tagline'])}</p></div><div><a href="/operator/">運営者情報</a> · <a href="/advertising-policy/">広告ポリシー</a> · <a href="/privacy/">プライバシー</a></div></div></footer><script>document.querySelectorAll('.affiliate').forEach(a=>a.addEventListener('click',()=>{{window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'affiliate_click',offer:a.dataset.offer,context:a.dataset.context}})}}));</script></body></html>'''
def write(path,content):
    out=DIST/path
    if out.suffix!='.html':out=out/'index.html'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(content,encoding='utf-8')

if DIST.exists():shutil.rmtree(DIST)
(DIST/'assets').mkdir(parents=True)
CSS=r''':root{--ink:#15221c;--sub:#5a6761;--line:#dae5df;--paper:#fbfdfc;--soft:#eef6f1;--accent:#17633f;--accent2:#103d2b;--warn:#fff7df}*{box-sizing:border-box}body{margin:0;color:var(--ink);background:var(--paper);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans JP",sans-serif;line-height:1.8}a{color:var(--accent)}.wrap{max-width:1080px;margin:auto;padding:0 22px}header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10}.header{display:flex;align-items:center;justify-content:space-between;min-height:68px;gap:20px}.brand{font-weight:900;text-decoration:none;color:var(--ink)}nav{display:flex;gap:15px;font-size:14px;flex-wrap:wrap}nav a{text-decoration:none;color:var(--sub)}.hero{padding:64px 0 34px}.eyebrow{font-size:12px;font-weight:800;letter-spacing:.08em;color:var(--accent);text-transform:uppercase}.hero h1{font-size:clamp(31px,5vw,56px);line-height:1.16;letter-spacing:-.035em;margin:.25em 0}.lead{font-size:18px;color:var(--sub);max-width:790px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.card,.fact{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;text-decoration:none;color:var(--ink)}.section{padding:25px 0}.section h2{font-size:27px;line-height:1.4}.notice{background:var(--soft);border-left:4px solid var(--accent);padding:18px 20px;border-radius:8px}.warning{background:var(--warn);border-left:4px solid #d9a515;padding:18px 20px;border-radius:8px}.cta{margin:30px 0;padding:26px;border-radius:14px;background:var(--accent2);color:#fff}.cta .pr{font-size:11px;font-weight:900;border:1px solid currentColor;border-radius:99px;padding:2px 7px}.button{display:inline-block;border:0;cursor:pointer;background:var(--accent);color:#fff;padding:13px 20px;border-radius:9px;font-weight:900;text-decoration:none}.button.invert{background:#fff;color:var(--accent2)}.cta small{display:block;margin-top:8px}.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.diagnosis{display:grid;gap:16px;max-width:780px}.diagnosis label{font-weight:800}.diagnosis select{width:100%;padding:12px;border:1px solid #bac8bf;border-radius:8px;background:#fff}.hint{display:block;font-weight:400;color:var(--sub);font-size:13px}.result{display:none;margin-top:24px;padding:24px;background:#fff;border:2px solid var(--accent);border-radius:12px}.result h2{margin-top:0}.result-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.result-box{padding:16px;border-radius:10px;background:var(--soft)}.stop{background:var(--warn)}.public-link{display:inline-block;margin-top:8px}.footer{display:grid;grid-template-columns:2fr 1fr;gap:20px;padding:40px 22px}footer{margin-top:70px;background:#f0f4f1;border-top:1px solid var(--line);font-size:14px}@media(max-width:760px){.header{align-items:flex-start;padding-top:14px;padding-bottom:14px;flex-direction:column}.grid,.facts,.footer,.result-grid{grid-template-columns:1fr}.hero{padding-top:42px}.hero h1{font-size:35px}}'''
(DIST/'assets/style.css').write_text(CSS,encoding='utf-8')

priority=['kawagoe-shi/akiya-kazai-tekkyo','kawagoe-shi/mitsumori-check','kawagoe-shi/jikka-katazuke-enkaku','kawagoe-shi/tachiai-fuyo','kawagoe-shi/taikyo-kigen','kawagoe-shi/ikkenya-katazuke','kawagoe-shi/ippan-haikibutsu','kawagoe-shi/kichohin-tansaku','kawagoe-shi/shisetsu-nyukyo','kawagoe-shi/kaitori-sousai']
lookup={p['slug']:p for p in PAGES};selected=[lookup[x] for x in priority if x in lookup]
cards=''.join(f'<a class="card" href="/{esc(p["slug"])}/"><small>{esc(p["eyebrow"])}</small><h3>{esc(p["h1"])}</h3><p>{esc(p["description"])}</p></a>' for p in selected)
body=f'''<section class="hero"><div class="eyebrow">Kawagoe / Inherited Home</div><h1>実家を片付ける前に、<br>家の出口を比べる。</h1><p class="lead">相続した実家や空き家は、先に高額な片付けを契約せず、名義・家族の合意・家の出口を確認してから必要な片付けだけ進めます。</p><p><a class="button" href="/shindan/">3分で進め方を整理する</a></p></section><section class="section"><div class="facts"><div class="fact"><strong>1. 名義と家族合意</strong><br>売却や処分を進められる状態か確認</div><div class="fact"><strong>2. 現況で出口確認</strong><br>売却・保有・管理・活用を比較</div><div class="fact"><strong>3. 必要分だけ片付け</strong><br>価値確認後に処分・買取・業者比較へ</div></div></section><section class="section warning"><strong>先に媒介契約や大量処分を進める前に、公的な選択肢を確認</strong><p>川越市には空き家バンクや空き家相談があります。売却・賃貸・管理・解体の選択肢を確認してから、必要な家財だけ撤去する順番をおすすめします。</p><p><a href="/kawagoe-shi/akiya-kazai-tekkyo/">売却・解体前の家財撤去チェックを見る</a></p></section><section class="section notice"><strong>川越市にも原則無料の空き家相談窓口があります</strong><p>「何から手をつければいいか」から相続、管理、賃貸、売却、解体まで相談できます。</p><p><a href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1020433.html" target="_blank" rel="noopener">川越市公式の相談窓口を見る</a></p></section>{offer_cta('primary','home')}<section class="section"><h2>片付けが必要になったら確認すること</h2><div class="grid">{cards}</div></section>'''
write('index.html',layout('相続した実家を片付ける前に｜売却・活用・管理・解体を比較','川越市を中心に、相続した実家を片付ける前に名義・家族合意・売却・活用・管理・解体を整理します。',body,'/'))

for p in PAGES:
    secs=''.join(f'<section class="section"><h2>{esc(h)}</h2><ul>'+''.join(f'<li>{esc(x)}</li>' for x in items)+'</ul></section>' for h,items in p['sections'])
    mid=offer_cta('primary',p['slug']) if p['slug'] in priority[:5] else ''
    body=f'''<section class="hero"><div class="eyebrow">{esc(p['eyebrow'])}</div><h1>{esc(p['h1'])}</h1><p class="lead">{esc(p['lead'])}</p></section>{secs}{mid}<section class="section notice"><strong>自治体情報も確認</strong><p>制度・処分方法は川越市の最新公式情報も確認してください。</p></section>'''
    write(p['slug'],layout(p['title'],p['description'],body,'/'+p['slug']+'/'))

# Remaining diagnosis/static/sitemap generation is preserved in repository history; this focused change updates homepage priority and navigation.
# NOTE: build.py is intentionally kept generated-site oriented; use git history if extending auxiliary pages.
