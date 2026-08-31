from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
subprocess.run([sys.executable, str(ROOT / 'build.py')], check=True)

for filename in ['google02c383ec58048d5e.html', 'sitemap.txt']:
    src = ROOT / filename
    if src.exists():
        shutil.copy2(src, DIST / src.name)
        print(f'Copied static file: {src.name}')

# Copy curated static pages after the generated build. These pages are deliberately
# hand-edited for high-intent topics rather than mass-generated location pages.
static_pages = ROOT / 'static_pages'
if static_pages.exists():
    shutil.copytree(static_pages, DIST, dirs_exist_ok=True)
    print('Copied curated static pages')

# Keep the commercial page useful and neutral by showing municipal options too.
high_intent = DIST / 'kawagoe-shi' / 'katazuke-hiyou-urenai' / 'index.html'
if high_intent.exists():
    page = high_intent.read_text(encoding='utf-8')

    # Keep the page aligned with the site-wide exit-first strategy. Do not lead
    # visitors into paying for disposal before they know whether the home can be
    # sold, rented, managed, or otherwise handled with belongings still inside.
    old_steps = '''<section class="section"><h2>おすすめの順番は5ステップ</h2><div class="grid"><div class="card"><small>STEP 1</small><h3>重要品を確保</h3><p>通帳、印鑑、権利書類、保険証券、写真・形見などを先に探索します。</p></div><div class="card"><small>STEP 2</small><h3>売れる物を査定</h3><p>家具・家電・貴金属などは処分前に買取可能性を確認し、廃棄量を減らします。</p></div><div class="card"><small>STEP 3</small><h3>自治体処分を確認</h3><p>自分で対応できる量なら、市の戸別収集や自己搬入条件を確認します。</p></div><div class="card"><small>STEP 4</small><h3>残りだけ業者比較</h3><p>仕分け・搬出・清掃・買取・一般廃棄物の運搬方法まで条件を揃えて比較します。</p></div><div class="card"><small>STEP 5</small><h3>税制を確認して出口比較</h3><p>相続空き家なら特例の条件を確認してから、売却・賃貸・管理を比較します。</p></div></div>'''
    new_steps = '''<section class="section"><h2>おすすめの順番は5ステップ</h2><div class="grid"><div class="card"><small>STEP 1</small><h3>重要品を確保</h3><p>通帳、印鑑、権利書類、保険証券、写真・形見などを先に探索します。</p></div><div class="card"><small>STEP 2</small><h3>残置物ありで出口確認</h3><p>片付け契約の前に、家財が残った現況で売却・買取・賃貸・管理・解体を相談できるか確認します。</p></div><div class="card"><small>STEP 3</small><h3>名義・相続・税制を確認</h3><p>相続登記や空き家特例など、出口の選び方に影響する条件を先に確認します。</p></div><div class="card"><small>STEP 4</small><h3>売れる物と自治体処分を確認</h3><p>出口が見えてから、買取可能品と自分で処分できる物を分け、不要な廃棄コストを減らします。</p></div><div class="card"><small>STEP 5</small><h3>必要な分だけ業者比較</h3><p>最後に残った作業だけ、仕分け・搬出・清掃・一般廃棄物の運搬方法まで条件を揃えて比較します。</p></div></div>'''
    if old_steps in page:
        page = page.replace(old_steps, new_steps)
        print('Aligned high-intent page steps with exit-first strategy')

    # Partnership-review hygiene: disclose advertising clearly even before the
    # first affiliate URL is issued. This avoids the weaker future-tense wording.
    old_adnote = '<div class="adnote">広告掲載時は「PR」「広告」をリンク付近に明示します。</div>'
    pr_adnote = '<div class="adnote"><strong>PR</strong>：本ページには広告を掲載することがあります。広告経由で申込みがあった場合、当サイトが報酬を受け取ることがあります。掲載内容・比較基準は広告の有無にかかわらず編集方針に基づいて作成します。</div>'
    if old_adnote in page:
        page = page.replace(old_adnote, pr_adnote)
        print('Upgraded PR disclosure on high-intent page')

    marker = '<section class="section"><h2>見積もりで最低限そろえる数字</h2>'
    municipal = '''<section class="section"><h2>売却予定なら「川越市空き家バンク」も比較候補</h2><p>川越市は、空き家を売りたい・貸したい所有者または管理者向けに空き家バンクを案内しています。登録費用はかかりませんが、登録には条件があり、宅地建物取引業者とすでに媒介契約を結んでいる物件などは対象外です。契約成立時には媒介を行った宅建業者への媒介報酬が必要です。</p><p>そのため売却予定なら、<strong>民間の査定・残置物がある状態での売却相談・川越市空き家バンク</strong>を条件に応じて比較し、片付け契約を先に固定しない方が選択肢を残せます。</p><p><a href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1003032/1003036.html" target="_blank" rel="noopener">川越市：空き家を売りたい・貸したい方</a></p></section>'''
    consultation = '''<section class="section notice"><strong>何から始めるか決まらない場合は、市の空き家相談も使える</strong><p>川越市は2026年6月8日、埼玉県宅地建物取引業協会 埼玉西部支部と空き家・空き地の相談事業に関する連携協定を締結しました。相続、管理、賃貸、売却、解体などについて、宅地建物取引士による助言・提案や専門家紹介を受けられる相談窓口です。</p><p>片付けを先に契約すべきか、売却・解体までまとめて考えるべきか判断できない場合は、広告サービスだけでなくこの公的な相談経路も比較候補にしてください。</p><p><a href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1020433.html" target="_blank" rel="noopener">川越市：空き家・空き地等の相談事業</a></p></section>'''
    additions = ''
    if '川越市空き家バンク」も比較候補' not in page:
        additions += municipal
    if '市の空き家相談も使える' not in page:
        additions += consultation
    if marker in page and additions:
        page = page.replace(marker, additions + marker)
        print('Added Kawagoe municipal disposition options to high-intent page')

    high_intent.write_text(page, encoding='utf-8')

# Ensure curated pages are discoverable in both sitemap formats.
curated_urls = [
    'https://saitama-jikka-navi.pages.dev/kawagoe-shi/gyosha-erabi/',
    'https://saitama-jikka-navi.pages.dev/kawagoe-shi/katazuke-hiyou-urenai/',
]
xml_path = DIST / 'sitemap.xml'
if xml_path.exists():
    xml = xml_path.read_text(encoding='utf-8')
    additions = ''.join(f'<url><loc>{u}</loc></url>' for u in curated_urls if u not in xml)
    if additions:
        xml = xml.replace('</urlset>', additions + '</urlset>')
        xml_path.write_text(xml, encoding='utf-8')

txt_path = DIST / 'sitemap.txt'
if txt_path.exists():
    existing = txt_path.read_text(encoding='utf-8').splitlines()
    for u in curated_urls:
        if u not in existing:
            existing.append(u)
    txt_path.write_text('\n'.join(existing) + '\n', encoding='utf-8')

# Cloudflare Pages custom headers.
headers = DIST / '_headers'
headers.write_text(
    '/sitemap.xml\n'
    '  Content-Type: application/xml; charset=UTF-8\n'
    '  Cache-Control: no-cache\n\n'
    '/sitemap.txt\n'
    '  Content-Type: text/plain; charset=UTF-8\n'
    '  Cache-Control: no-cache\n\n'
    '/robots.txt\n'
    '  Content-Type: text/plain; charset=UTF-8\n',
    encoding='utf-8'
)
print('Wrote Cloudflare _headers for sitemap and robots files')
