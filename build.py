from __future__ import annotations
import json, html, pathlib, shutil
from urllib.parse import urljoin
ROOT=pathlib.Path(__file__).resolve().parent
DIST=ROOT/'dist'
SITE=json.loads((ROOT/'site_data.json').read_text(encoding='utf-8'))
PAGES=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))

def esc(s): return html.escape(str(s),quote=True)
def canonical(path='/'): return urljoin(SITE['base_url'].rstrip('/')+'/',path.lstrip('/'))
def nav(): return '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/kaitai-check/">解体前チェック</a><a href="/tedori-hikaku/">手取り比較</a><a href="/faq/">FAQ</a></nav>'
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
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | {esc(SITE['site_name'])}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{esc(canonical(path))}"><meta name="robots" content="index,follow,max-image-preview:large"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)} | {esc(SITE['site_name'])}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{esc(canonical(path))}"><link rel="stylesheet" href="/assets/style.css">{ga()}{st}</head><body><header><div class="wrap header"><a class="brand" href="/">{esc(SITE['site_name'])}</a>{nav()}</div></header><main class="wrap">{body}</main><footer><div class="wrap footer"><div><strong>{esc(SITE['site_name'])}</strong><p>{esc(SITE['tagline'])}</p></div><div><a href="/operator/">運営者情報</a> · <a href="/editorial-policy/">編集方針</a> · <a href="/advertising-policy/">広告ポリシー</a> · <a href="/privacy/">プライバシー</a></div></div></footer><script>document.querySelectorAll('.affiliate').forEach(a=>a.addEventListener('click',()=>{{if(typeof window.gtag==='function'){{window.gtag('event','affiliate_click',{{offer:a.dataset.offer,context:a.dataset.context,source_page:window.location.pathname}})}}}}));</script></body></html>'''
def write(path,content):
    out=DIST/path
    if out.suffix!='.html':out=out/'index.html'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(content,encoding='utf-8')

if DIST.exists():shutil.rmtree(DIST)
(DIST/'assets').mkdir(parents=True)
CSS=r''':root{--ink:#15221c;--sub:#5a6761;--line:#dae5df;--paper:#fbfdfc;--soft:#eef6f1;--accent:#17633f;--accent2:#103d2b;--warn:#fff7df}*{box-sizing:border-box}body{margin:0;color:var(--ink);background:var(--paper);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans JP",sans-serif;line-height:1.8}a{color:var(--accent)}.wrap{max-width:1080px;margin:auto;padding:0 22px}header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10}.header{display:flex;align-items:center;justify-content:space-between;min-height:68px;gap:20px}.brand{font-weight:900;text-decoration:none;color:var(--ink)}nav{display:flex;gap:15px;font-size:14px;flex-wrap:wrap}nav a{text-decoration:none;color:var(--sub)}.hero{padding:64px 0 34px}.eyebrow{font-size:12px;font-weight:800;letter-spacing:.08em;color:var(--accent);text-transform:uppercase}.hero h1{font-size:clamp(31px,5vw,56px);line-height:1.16;letter-spacing:-.035em;margin:.25em 0}.lead{font-size:18px;color:var(--sub);max-width:790px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.card,.fact{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;text-decoration:none;color:var(--ink)}.section{padding:25px 0}.section h2{font-size:27px;line-height:1.4}.notice{background:var(--soft);border-left:4px solid var(--accent);padding:18px 20px;border-radius:8px}.warning{background:var(--warn);border-left:4px solid #d9a515;padding:18px 20px;border-radius:8px}.cta{margin:30px 0;padding:26px;border-radius:14px;background:var(--accent2);color:#fff}.cta .pr{font-size:11px;font-weight:900;border:1px solid currentColor;border-radius:99px;padding:2px 7px}.button{display:inline-block;border:0;cursor:pointer;background:var(--accent);color:#fff;padding:13px 20px;border-radius:9px;font-weight:900;text-decoration:none}.button.invert{background:#fff;color:var(--accent2)}.cta small{display:block;margin-top:8px}.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.diagnosis{display:grid;gap:16px;max-width:780px}.diagnosis label{font-weight:800}.diagnosis select{width:100%;padding:12px;border:1px solid #bac8bf;border-radius:8px;background:#fff}.hint{display:block;font-weight:400;color:var(--sub);font-size:13px}.result{display:none;margin-top:24px;padding:24px;background:#fff;border:2px solid var(--accent);border-radius:12px}.result h2{margin-top:0}.result-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.result-box{padding:16px;border-radius:10px;background:var(--soft)}.stop{background:var(--warn)}.public-link{display:inline-block;margin-top:8px}.footer{display:grid;grid-template-columns:2fr 1fr;gap:20px;padding:40px 22px}footer{margin-top:70px;background:#f0f4f1;border-top:1px solid var(--line);font-size:14px}@media(max-width:760px){.header{align-items:flex-start;padding-top:14px;padding-bottom:14px;flex-direction:column}.grid,.facts,.footer,.result-grid{grid-template-columns:1fr}.hero{padding-top:42px}.hero h1{font-size:35px}}'''
(DIST/'assets/style.css').write_text(CSS,encoding='utf-8')

priority=['kawagoe-shi/jikka-katazuke-enkaku','kawagoe-shi/tachiai-fuyo','kawagoe-shi/mitsumori-check','kawagoe-shi/taikyo-kigen','kawagoe-shi/ikkenya-katazuke','kawagoe-shi/ippan-haikibutsu','kawagoe-shi/kichohin-tansaku','kawagoe-shi/shisetsu-nyukyo','kawagoe-shi/kaitori-sousai']
lookup={p['slug']:p for p in PAGES};selected=[lookup[x] for x in priority if x in lookup]
cards=''.join(f'<a class="card" href="/{esc(p["slug"])}/"><small>{esc(p["eyebrow"])}</small><h3>{esc(p["h1"])}</h3><p>{esc(p["description"])}</p></a>' for p in selected)
body=f'''<section class="hero"><div class="eyebrow">Saitama / Inherited Home</div><h1>実家を片付ける前に、<br>家の出口を比べる。</h1><p class="lead">埼玉県の実家や空き家は、片付けや媒介契約を急ぐ前に、名義・家族の合意と市町村の制度を確認し、現況売却・管理・活用・解体を比較してから必要な片付けを進めます。</p><p><a class="button" href="/shindan/">3分で進め方を整理する</a></p><p>すでに売却を検討中の方は、<a href="/tedori-hikaku/">片付け前に仲介・現況買取の税前手取りを比較</a>できます。</p></section><section class="section"><div class="facts"><div class="fact"><strong>1. 名義と家族合意</strong><br>売却や処分を進められる状態か確認</div><div class="fact"><strong>2. 現況で出口確認</strong><br>売却・保有・管理・活用を比較</div><div class="fact"><strong>3. 必要分だけ片付け</strong><br>価値確認後に処分・買取・業者比較へ</div></div></section><section class="section notice"><strong>売却方針が未定なら、埼玉県の公的相談を先に</strong><p>埼玉県の空き家コーディネーターは、県内にある空き家の所有者等を対象に、売却・賃貸・管理・解体の相談に原則無料で対応します（専門家への依頼は一部有料）。空き家バンクの登録条件は市町村ごとに異なるため、媒介契約や片付けの前に公式情報を確認してください。</p><p><a class="public-link" data-context="home_pref_coordinator" href="https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html" target="_blank" rel="noopener">埼玉県公式：空き家コーディネーター</a> ／ <a class="public-link" data-context="home_pref_airbank" href="https://www.pref.saitama.lg.jp/a1107/akiyabanku.html" target="_blank" rel="noopener">埼玉県公式：市町村空き家バンク一覧</a></p></section><section class="section"><h2>川越市の詳細ガイド（県内制度の具体例）</h2><p>以下は川越市の制度・実務に関する記事です。他市町村では許可業者や補助制度が異なるため、実家の所在地で確認してください。県内共通の進め方は<a href="/shindan/">進め方診断</a>、売却条件の比較は<a href="/tedori-hikaku/">手取り比較</a>をご利用ください。</p><div class="grid">{cards}</div></section>'''
write('index.html',layout('相続した実家を片付ける前に｜売却・活用・管理・解体を比較','埼玉県の実家じまいで、片付け・媒介契約前に名義、家族合意、現況売却・管理・活用・解体を比較し、市町村制度と税前手取りを確認します。',body,'/'))

for p in PAGES:
    secs=''.join(f'<section class="section"><h2>{esc(h)}</h2><ul>'+''.join(f'<li>{esc(x)}</li>' for x in items)+'</ul></section>' for h,items in p['sections'])
    # Cleanup-intent readers have not decided to sell. Do not show a vacant-home
    # appraisal affiliate CTA on their editorial page just because an offer exists.
    # Let them opt into the paid path via the comparison tool after clarifying intent.
    mid = (
        '<section class="section notice"><strong>この実家を売る可能性もある場合</strong>'
        '<p>片付け費用を契約する前に、家財が残った状態で売却できるか、'
        '仲介と現況買取の税前手取りを比較してください。'
        '売却予定がなければ、片付け条件と一般廃棄物の処理方法の確認を優先してください。</p>'
        '<p><a href="/tedori-hikaku/">片付け前に税前手取りを比較する</a></p></section>'
    ) if p['slug'] in priority[:5] else ''
    body=f'''<section class="hero"><div class="eyebrow">{esc(p['eyebrow'])}</div><h1>{esc(p['h1'])}</h1><p class="lead">{esc(p['lead'])}</p></section>{secs}{mid}<section class="section notice"><strong>自治体情報も確認</strong><p>制度・処分方法は川越市の最新公式情報も確認してください。</p></section>'''
    write(p['slug'],layout(p['title'],p['description'],body,'/'+p['slug']+'/'))

shindan='''<section class="hero"><div class="eyebrow">Diagnosis</div><h1>実家の「今やること・まだやらないこと」診断</h1><p class="lead">6つの状況から、片付けや査定を急ぐ前に確認すべき順番を整理します。診断は法律・税務上の個別判断ではありません。</p></section><section class="section"><form id="diag" class="diagnosis"><label>1. 親御さん・実家の状態<select id="status"><option value="alive">親が住んでいる／将来が心配</option><option value="facility">施設入居などで空き家</option><option value="deceased">亡くなり相続が発生</option></select></label><label>2. 名義・相続登記<select id="title"><option value="known">名義・登記状況を確認済み</option><option value="unknown">誰の名義か／登記状況が不明</option><option value="pending">相続手続き中</option></select></label><label>3. 家族・共同相続人の方針<select id="family"><option value="agreed">売る／残す等の方針は合意済み</option><option value="not_agreed">まだ話し合っていない／意見が違う</option><option value="solo">自分だけで判断できる</option></select></label><label>4. 今の希望<select id="exit"><option value="undecided">まだ決めていない</option><option value="sell">売却を検討</option><option value="keep">当面保有・管理したい</option><option value="use">住む／貸すなど活用したい</option></select></label><label>5. 家財・残置物<select id="items"><option value="many">かなり残っている</option><option value="some">一部残っている</option><option value="clear">ほぼ空</option></select><span class="hint">重要書類・形見・価値ある物を確認する前の一括処分は避けます。</span></label><label>6. 距離・期限<select id="distance"><option value="local">現地へ行きやすい</option><option value="far">遠方で何度も行けない</option><option value="urgent">退去・売却など期限が迫っている</option></select></label><button class="button" type="submit">診断結果を見る</button></form><div id="r" class="result" aria-live="polite"><h2 id="result-title"></h2><div class="result-grid"><div class="result-box"><strong>今日やること</strong><p id="do"></p></div><div class="result-box stop"><strong>今はやらないこと</strong><p id="dont"></p></div></div><p id="why"></p><p id="public"></p></div></section><script>
const $=id=>document.getElementById(id);const push=x=>{window.dataLayer=window.dataLayer||[];window.dataLayer.push(x)};
$('diag').addEventListener('submit',e=>{e.preventDefault();let s=$('status').value,t=$('title').value,f=$('family').value,x=$('exit').value,i=$('items').value,d=$('distance').value;let type='undecided',blocked='none',title='まず「決める前の情報」を揃える',todo='埼玉県の空き家コーディネーター等も使い、名義・家族の意向・維持費・売却/活用の選択肢を1枚に整理する。',dont='片付け・解体・売却を勢いで契約しない。',why='出口が未定の段階では、先に費用をかけると選択肢を狭めることがあります。';
if(t!=='known'){type='inheritance';blocked='title';title='最優先は名義・相続関係の確認';todo='固定資産税資料や登記事項を確認し、誰が手続きを進められるか整理する。';dont='名義が曖昧なまま売却契約や大規模処分を進めない。';why='売却希望があっても、まず権利関係を確認する方が手戻りを減らせます。'}
else if(f==='not_agreed'){type='inheritance';blocked='family_agreement';title='先に家族の方針を揃える';todo='「売る/残す」「誰が管理」「費用負担」「形見・家財」の4点を共同相続人等と確認する。';dont='一人の判断で家財処分や売却を確定しない。';why='家族合意がない状態では、査定額より先に意思決定条件を揃える方が安全です。'}
else if(x==='sell'){type='sale';title='片付け前に現況で売却条件を確認';todo='家財が残る状態での査定可否と、残置物を残す場合/撤去する場合の条件差を確認する。';dont=i==='clear'?'査定前に高額なリフォームや解体を決めない。':'重要書類・形見・価値ある家財を確認せず一括処分しない。';why='片付け費用を先払いする前に、現況価格と必要費用を比較します。'}
else if(x==='keep' || d==='far'){type='manage';title='まず管理空白を止める';todo='郵便、換気、通水、庭木、外観確認の管理頻度を決める。遠方なら埼玉県の「空き家の持ち主応援隊」から所在地に対応する事業者を確認する。';dont='管理方法がないまま長期間放置しない。';why='売却を急がない場合でも、管理不全化を防ぐことが先です。'}
else if(x==='use'){type='reuse';title='活用条件と費用を先に比較';todo='住む・貸す場合の修繕費、管理、法的/物理的条件を確認する。';dont='活用可能性を確認せず解体や全処分をしない。';why='活用案ごとの初期費用と継続費を比較してから片付け範囲を決めます。'}
if(s==='deceased'&&t==='known'&&type==='undecided'){type='inheritance';title='相続後の出口を比較する';todo='売却・保有・活用の3案と税務上の期限/要件を専門家・一次情報で確認する。';dont='税制要件を確認せず貸す・壊す・売る判断を確定しない。';why='相続空き家には条件付きの税制措置等があるため、行動順序が重要です。'}
$('result-title').textContent=title;$('do').textContent=todo;$('dont').textContent=dont;$('why').textContent=why;$('public').innerHTML='<a class="public-link" target="_blank" rel="noopener" href="https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html">埼玉県公式：空き家コーディネーター（原則無料の相談）</a>'+(type==='manage'?'<br><a class="public-link" target="_blank" rel="noopener" href="https://www.pref.saitama.lg.jp/a1106/akiyakanrisyatouroku.html">埼玉県公式：空き家の持ち主応援隊（管理・売却等）</a>':'');$('r').style.display='block';$('r').scrollIntoView({behavior:'smooth',block:'start'});push({event:'diagnosis_complete',diagnosis_result:type,blocked_action:blocked,status:s,title_status:t,family_status:f,exit_intent:x,items:i,distance:d});});
</script>'''
write('shindan',layout('実家片付けの進め方診断','6つの状況から、埼玉県内の実家・空き家で今やることと契約前の確認順序、公的相談先を整理します。',shindan,'/shindan/'))

faq='''<section class="hero"><h1>よくある質問</h1></section><section class="section"><h2>片付けてから査定すべき？</h2><p>必ずしも先に全処分する必要はありません。重要書類・形見・価値ある物を確認し、家財が残る状態での査定可否や処分費負担を確認してから処分範囲を決めてください。</p><p><a href="/tedori-hikaku/">片付け後の仲介と現況買取の手取りを比較する</a></p><h2>家財の買取と不用品回収を、一括で頼んでも大丈夫？</h2><p>売れる可能性のある家具・家電・骨董品・楽器などは、捨てる前に買取の可否を確認できます。ただし「中古品を買い取ること」と「売れなかった家庭ごみを収集・運搬すること」は別の業務です。家庭ごみの収集運搬は、原則として実家の所在地の市区町村による一般廃棄物収集運搬業の許可・委託等を受けた主体に依頼してください。古物商許可や産業廃棄物収集運搬業許可だけで家庭ごみを回収できるわけではありません。</p><p>見積時には「買取対象と金額」「売れない物の収集運搬主体と許可・委託」「処分費・追加料金」を分けて確認しましょう。買取が成立しない品もあるため、査定額を確定した収入として先に計上しないでください。</p><p><a href="https://www.city.fujimino.saitama.jp/soshikiichiran/kankyoka/haikibutsutaisakugakari/kateigomi/17310.html" target="_blank" rel="noopener">ふじみ野市公式：無許可の回収業者への注意</a>／<a href="/tedori-hikaku/">買取額と家財処分費を別々にして手取りを比較する</a></p><h2>遠方で管理できません</h2><p>郵便物の確認・換気・通水・庭木の手入れなど必要な管理を整理し、鍵預かり、作業写真の報告、追加料金を同じ条件で比較してください。市町村ごとに事業者・サービス範囲が異なるため、県の公的案内から実家の所在地に対応する相談先を確認できます。</p><p><a href="https://www.pref.saitama.lg.jp/a1106/akiyakanrisyatouroku.html" target="_blank" rel="noopener">埼玉県公式：空き家の持ち主応援隊（管理・売却等の相談先）</a></p></section>'''
write('faq',layout('よくある質問','実家片付け・相続空き家のよくある質問。',faq,'/faq/'))
# Editorial transparency and data-use disclosure: render from the actual deployment config.
# Do not publish fictitious contact information or claim GA4/ASP activation before configured.
contact_email = (SITE.get('contact_email') or '').strip()
analytics_enabled = bool((SITE.get('ga4_id') or '').strip())
advertising_enabled = any((o.get('url') or '').strip() for o in SITE.get('offers', []))

operator_html = f'''<section class="hero"><h1>運営者情報</h1></section>
<section class="section"><h2>サイトについて</h2>
<p>サイト名：{esc(SITE['site_name'])}</p>
<p>運営・編集：{esc(SITE.get('operator_name') or '埼玉実家片付けナビ編集部')}</p>
<p>埼玉県内の実家じまい・空き家の売却、片付け、管理、解体を検討する方向けに、公的な一次情報と意思決定のチェックポイントを整理しています。自治体・公的機関が運営するサイトではありません。</p>
<p>内容の更新時には自治体などの公式情報を確認しますが、補助金の受付状況・契約条件等は変わります。申請・契約前に必ず関係機関や専門家へご確認ください。</p>'''
if contact_email:
    operator_html += f'<p>連絡先：<a href="mailto:{esc(contact_email)}">{esc(contact_email)}</a></p>'
else:
    operator_html += '<p>現在、当サイト専用の問い合わせ窓口は設けていません。物件・制度の個別相談は、掲載している自治体等の公式窓口へ直接ご確認ください。</p>'
operator_html += '</section>'
write('operator', layout('運営者情報', '埼玉実家片付けナビの運営方針と情報の確認方法。', operator_html, '/operator/'))

ad_status = ('現在、提携済み広告URLは設定されていません。' if not advertising_enabled
             else '広告リンクには「PR」表示を付け、外部のサービスに移動することを明示します。')
ad_html = f'''<section class="hero"><h1>広告ポリシー</h1></section>
<section class="section"><h2>広告・アフィリエイトについて</h2>
<p>当サイトは、今後の運営費用を賄うために広告・アフィリエイトプログラムを利用する場合があります。広告経由の申し込みによってサイト側に報酬が発生する場合があります。</p>
<p>{esc(ad_status)}</p>
<p>広告の有無と無関係に、自治体の公式窓口・空き家バンク等の選択肢も紹介します。掲載順やおすすめが必ずしも利用者ごとの最適解となるわけではありません。</p>
<p>費用、サービス提供範囲、個人情報の取扱い、契約・キャンセル条件は、申込先の事業者に確認してください。広告先の契約は本サイトとの契約ではありません。</p>
<p>広告クリックなどのアクセス解析の取扱いは<a href="/privacy/">プライバシーポリシー</a>をご確認ください。</p></section>'''
write('advertising-policy', layout('広告ポリシー', '広告の有無、アフィリエイト報酬、記事の独立性について。', ad_html, '/advertising-policy/'))

# Published editorial policy: no fictional author, reviewer, approval or contact.
editorial_html = '''<section class="hero"><h1>編集方針・情報の検証方法</h1><p class="lead">最終更新：2026年10月25日。契約・売却・解体前の判断を助けるため、確認できた事実と試算上の仮定を分けて示します。</p></section>
<section class="section"><h2>一次情報を優先</h2>
<p>補助金、自治体の相談窓口、登記、税制、廃棄物処理の説明では、自治体・国の公式ページや法令を優先します。民間事業者の説明は、利用条件や料金の比較対象として扱い、行政の決定と区別します。</p>
<p>制度の更新日・確認日と受付状況は同じ意味ではありません。年度・予算残額・交付決定前の契約や着工の可否は変わり得るため、公式ページに期限が書かれていても「今、申請できる」とは保証しません。必ず申請先に確認してください。</p>
<h2>比較・計算の扱い</h2>
<p>手取り比較の売却価格・買取価格・家財処分費などの初期入力は説明用です。地域の実際の相場・個別の査定額ではありません。税前概算には譲渡所得税、登記費用、ローン残債など含まれない項目があるため、結果だけで契約や解体を判断しないでください。</p>
<p>自治体補助や家財の買取価格は、未確認の段階では受給・売却できるものとして加算しないよう案内します。物件の条件、追加費用、期間をそろえて比較することを推奨します。</p>
<h2>広告・評価の独立性</h2>
<p>広告やアフィリエイトがある場合はPR表示を行い、報酬の有無と関係なく公的相談先も案内します。報酬単価の高低だけで事業者を推奨しません。現時点の広告設定は<a href="/advertising-policy/">広告ポリシー</a>に記載しています。</p>
<h2>執筆・確認と訂正</h2>
<p>記事は「埼玉実家片付けナビ編集部」が作成し、公的情報の確認内容に応じて更新します。資格保有者や専門家による監修は、実際に確認した場合を除き表示しません。情報に齟齬が見つかったときは原典を照合し、本文と確認日の修正を行います。</p>
<p>現在、専用の問い合わせ窓口は設けていません。確認済みでない連絡先や監修者を記載しません。運営主体の表示は<a href="/operator/">運営者情報</a>をご覧ください。</p>
<h2>ご自身で確認できる公式相談先</h2>
<p><a href="https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html" rel="noopener" target="_blank">埼玉県「空き家コーディネーター」</a>は、県内の空き家所有者などが原則無料で相談できる公的案内です。個別の税・法律・不動産売買については、自治体や適切な専門家に確認してください。</p>
</section>'''
write('editorial-policy', layout('編集方針・情報の検証方法', '公的な一次情報の確認、試算の前提、広告の区別、訂正方針を公開しています。', editorial_html, '/editorial-policy/'))

analytics_status = ('現在、当サイトのGoogle Analytics 4（GA4）計測タグは有効化していません。' if not analytics_enabled
                    else '当サイトではGoogle Analytics 4（GA4）を使用し、閲覧ページ・操作イベント・外部リンクのクリック等を集計してサイト改善に利用しています。')
privacy_html = f'''<section class="hero"><h1>プライバシーポリシー</h1><p class="lead">最終更新：2026年10月23日</p></section>
<section class="section"><h2>本サイトと収集する情報</h2>
<p>本サイトは公的な相談窓口ではありません。サイトの閲覧時には、サイト配信・セキュリティ維持のため、配信事業者がIPアドレスやアクセス日時等の技術的なログを取り扱う場合があります。</p>
<p>ブラウザ上で金額を入力する比較ツールがあります。氏名・住所・電話番号などをサイト内で直接入力させる会員登録・問い合わせフォームは、現在設置していません。</p>
<h2>Google Analytics 4（GA4）とCookie</h2>
<p>{esc(analytics_status)}</p>
<p>GA4を有効にした場合、Cookieや類似の識別子、閲覧ページ・参照元・端末やブラウザに関する情報・操作イベント等がGoogleに送信されることがあります。取得情報は、サイトの利用状況の分析、使いやすさの改善、広告導線の効果測定に利用します。</p>
<p>Googleによる情報の取扱いは<a href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener">Googleのサービスを使用するサイトやアプリから収集した情報の使用</a>を参照してください。Cookieの設定はブラウザから変更でき、<a href="https://tools.google.com/dlpage/gaoptout?hl=ja" target="_blank" rel="noopener">Google Analyticsオプトアウトアドオン</a>も利用できます。</p>
<h2>外部サイト・広告について</h2>
<p>自治体の公式情報や民間事業者の外部サイトに移動した後は、移動先の利用規約・プライバシーポリシーが適用されます。当サイトは外部事業者の申し込みフォームで送信される情報を直接管理しません。</p>
<p>当サイトの広告掲載状況は<a href="/advertising-policy/">広告ポリシー</a>で確認できます。</p>
<h2>改定と問い合わせ</h2>
<p>利用する解析サービスや広告サービスを変更した場合は、本ページの説明を見直します。運営者情報は<a href="/operator/">運営者情報</a>をご確認ください。</p></section>'''
write('privacy', layout('プライバシーポリシー', 'アクセスログ・GA4・Cookie・外部広告サイトに関する情報の取扱い。', privacy_html, '/privacy/'))
urls=['/','/shindan/','/faq/','/operator/','/editorial-policy/','/advertising-policy/','/privacy/']+[f'/{p["slug"]}/' for p in PAGES]
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{esc(canonical(u))}</loc></url>' for u in urls)+'</urlset>',encoding='utf-8')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+canonical('/sitemap.xml')+'\n',encoding='utf-8')
print(f'Built {len(urls)} indexable URLs -> {DIST}')