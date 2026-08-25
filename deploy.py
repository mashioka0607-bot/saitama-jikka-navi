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

# Ensure curated pages are discoverable in both sitemap formats.
curated_urls = [
    'https://saitama-jikka-navi.pages.dev/kawagoe-shi/gyosha-erabi/',
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
