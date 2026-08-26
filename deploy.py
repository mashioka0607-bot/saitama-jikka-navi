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

# Keep the commercial page useful and neutral by showing the municipal option too.
# Kawagoe City updated its vacant-home-bank owner guidance on 2026-06-08.
high_intent = DIST / 'kawagoe-shi' / 'katazuke-hiyou-urenai' / 'index.html'
if high_intent.exists():
    page = high_intent.read_text(encoding='utf-8')
    marker = '<section class="section"><h2>見積もりで最低限そろえる数字</h2>'
    municipal = '''<section class="section"><h2>売却予定なら「川越市空き家バンク」も比較候補</h2><p>川越市は、空き家を売りたい・貸したい所有者または管理者向けに空き家バンクを案内しています。登録費用はかかりませんが、登録には条件があり、宅地建物取引業者とすでに媒介契約を結んでいる物件などは対象外です。契約成立時には媒介を行った宅建業者への媒介報酬が必要です。</p><p>そのため売却予定なら、<strong>民間の査定・残置物がある状態での売却相談・川越市空き家バンク</strong>を条件に応じて比較し、片付け契約を先に固定しない方が選択肢を残せます。</p><p><a href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1003032/1003036.html" target="_blank" rel="noopener">川越市：空き家を売りたい・貸したい方（2026年6月8日更新）</a></p></section>'''
    if marker in page and '川越市空き家バンク」も比較候補' not in page:
        page = page.replace(marker, municipal + marker)
        high_intent.write_text(page, encoding='utf-8')
        print('Added Kawagoe vacant-home-bank comparison to high-intent page')

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
