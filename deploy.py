from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'

# Apply the idempotent P0/SEO patch before every deploy. This closes the gap where
# patch_build_quality.py existed in the repo but deploy.py never executed it, so
# sitemap.xml / robots.txt and the public-placeholder fixes could be absent from
# the actual Cloudflare Pages artifact.
patcher = ROOT / 'scripts' / 'patch_build_quality.py'
if patcher.exists():
    subprocess.run([sys.executable, str(patcher)], check=True)

# Fail the deployment if the source still violates the quality gate.
quality_gate = ROOT / 'scripts' / 'check_seo_quality.py'
if quality_gate.exists():
    subprocess.run([sys.executable, str(quality_gate)], check=True)

subprocess.run([sys.executable, str(ROOT / 'build.py')], check=True)

for filename in ['google02c383ec58048d5e.html', 'sitemap.txt']:
    src = ROOT / filename
    if src.exists():
        shutil.copy2(src, DIST / src.name)
        print(f'Copied static file: {src.name}')

# Copy curated static pages after the generated build. High-intent editorial copy
# lives in static_pages itself so repository source and deployed output stay aligned.
static_pages = ROOT / 'static_pages'
if static_pages.exists():
    shutil.copytree(static_pages, DIST, dirs_exist_ok=True)
    print('Copied curated static pages')

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

# Post-build crawl/index gate. Source checks are not enough: Google only sees the
# generated artifact. Refuse to publish when the artifact is missing the files or
# URLs required for discovery and Search Console ownership verification.
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

print('Post-build crawl/index gate passed')
