from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'

# Apply idempotent source patches before quality/build so deploy output cannot regress.
for patch_name in ('patch_build_quality.py', 'patch_high_intent_nav.py'):
    patcher = ROOT / 'scripts' / patch_name
    if patcher.exists():
        subprocess.run([sys.executable, str(patcher)], check=True)

quality_gate = ROOT / 'scripts' / 'check_seo_quality.py'
if quality_gate.exists():
    subprocess.run([sys.executable, str(quality_gate)], check=True)

subprocess.run([sys.executable, str(ROOT / 'build.py')], check=True)

for filename in ['google02c383ec58048d5e.html', 'sitemap.txt']:
    src = ROOT / filename
    if src.exists():
        shutil.copy2(src, DIST / src.name)
        print(f'Copied static file: {src.name}')

static_pages = ROOT / 'static_pages'
if static_pages.exists():
    shutil.copytree(static_pages, DIST, dirs_exist_ok=True)
    print('Copied curated static pages')

curated_urls = [
    'https://saitama-jikka-navi.pages.dev/kawagoe-shi/gyosha-erabi/',
    'https://saitama-jikka-navi.pages.dev/kawagoe-shi/katazuke-hiyou-urenai/',
    'https://saitama-jikka-navi.pages.dev/tedori-hikaku/',
    'https://saitama-jikka-navi.pages.dev/kaitai-check/',
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

required_files = [
    DIST / 'index.html',
    DIST / 'sitemap.xml',
    DIST / 'robots.txt',
    DIST / 'google02c383ec58048d5e.html',
]
missing = [str(p.relative_to(DIST)) for p in required_files if not p.exists()]
if missing:
    raise RuntimeError(f'Deploy blocked: missing generated SEO files: {missing}')

xml = (DIST / 'sitemap.xml').read_text(encoding='utf-8')
if '<urlset' not in xml or '</urlset>' not in xml:
    raise RuntimeError('Deploy blocked: sitemap.xml is not a valid URL-set artifact')
for url in curated_urls:
    if url not in xml:
        raise RuntimeError(f'Deploy blocked: curated high-intent URL missing from sitemap.xml: {url}')

robots = (DIST / 'robots.txt').read_text(encoding='utf-8')
if 'Disallow: /' in robots:
    raise RuntimeError('Deploy blocked: robots.txt contains a sitewide crawl block')
if 'sitemap.xml' not in robots.lower():
    raise RuntimeError('Deploy blocked: robots.txt does not advertise sitemap.xml')

verification = (DIST / 'google02c383ec58048d5e.html').read_text(encoding='utf-8').lower()
if 'google-site-verification' not in verification:
    raise RuntimeError('Deploy blocked: Google Search Console verification artifact is invalid')

# Navigation regression gate: high-intent tools must remain discoverable sitewide.
for rel in ('index.html', 'tedori-hikaku/index.html', 'kaitai-check/index.html'):
    page = (DIST / rel).read_text(encoding='utf-8')
    for href in ('/tedori-hikaku/', '/kaitai-check/'):
        if f'href="{href}"' not in page:
            raise RuntimeError(f'Deploy blocked: {href} missing from {rel} navigation/content')

print('Post-build crawl/index/navigation gate passed')
