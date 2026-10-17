from pathlib import Path
import json
import shutil
import subprocess
import sys
from urllib.parse import urljoin, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'

# Apply idempotent source patches before quality/build so deploy output cannot regress.
for patch_name in ('patch_build_quality.py', 'patch_home_saitama_gate.py', 'patch_high_intent_nav.py', 'patch_tedori_precontract_bank.py', 'patch_tedori_subsidy_bridge.py', 'patch_tedori_real_quotes.py', 'patch_tedori_tax_gate.py'):
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

# Derive both sitemaps from the canonical site URL and actual built pages.
# Never retain the historical, manually copied sitemap.txt list.
site = json.loads((ROOT / 'site_data.json').read_text(encoding='utf-8'))
base_url = site['base_url'].rstrip('/')
parsed_base = urlsplit(base_url)
if parsed_base.scheme != 'https' or not parsed_base.netloc or parsed_base.path not in ('', '/'):
    raise RuntimeError('Deploy blocked: base_url must be an HTTPS origin')

curated_paths = [
    '/kawagoe-shi/gyosha-erabi/',
    '/kawagoe-shi/katazuke-hiyou-urenai/',
    '/tedori-hikaku/',
    '/kaitai-check/',
]
curated_urls = [urljoin(base_url + '/', path.lstrip('/')) for path in curated_paths]
xml_path = DIST / 'sitemap.xml'
if not xml_path.exists():
    raise RuntimeError('Deploy blocked: sitemap.xml not generated')
ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', ns)
tree = ET.parse(xml_path)
root = tree.getroot()
if root.tag != f'{{{ns}}}urlset':
    raise RuntimeError('Deploy blocked: unexpected sitemap namespace')
existing = {node.text for node in root.findall(f'{{{ns}}}url/{{{ns}}}loc')}
for path, url in zip(curated_paths, curated_urls):
    if not (DIST / path.lstrip('/') / 'index.html').is_file():
        raise RuntimeError(f'Deploy blocked: curated page missing: {path}')
    if url not in existing:
        ET.SubElement(ET.SubElement(root, f'{{{ns}}}url'), f'{{{ns}}}loc').text = url
        existing.add(url)
tree.write(xml_path, encoding='utf-8', xml_declaration=True)
txt_path = DIST / 'sitemap.txt'
txt_path.write_text('\n'.join(node.text for node in root.findall(f'{{{ns}}}url/{{{ns}}}loc') if node.text) + '\n', encoding='utf-8')

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

required_files = [DIST / 'index.html', DIST / 'sitemap.xml', DIST / 'robots.txt', DIST / 'google02c383ec58048d5e.html']
missing = [str(p.relative_to(DIST)) for p in required_files if not p.exists()]
if missing:
    raise RuntimeError(f'Deploy blocked: missing generated SEO files: {missing}')

xml = (DIST / 'sitemap.xml').read_text(encoding='utf-8')
if '<urlset' not in xml or '</urlset>' not in xml:
    raise RuntimeError('Deploy blocked: sitemap.xml is not a valid URL-set artifact')
for url in curated_urls:
    if url not in xml:
        raise RuntimeError(f'Deploy blocked: curated high-intent URL missing from sitemap.xml: {url}')

xml_urls = [node.text for node in ET.parse(xml_path).getroot().findall(f'{{{ns}}}url/{{{ns}}}loc')]
txt_urls = txt_path.read_text(encoding='utf-8').splitlines()
if xml_urls != txt_urls or len(xml_urls) != len(set(xml_urls)):
    raise RuntimeError('Deploy blocked: XML/TXT sitemap mismatch or duplicate URL')

robots = (DIST / 'robots.txt').read_text(encoding='utf-8')
if 'Disallow: /' in robots:
    raise RuntimeError('Deploy blocked: robots.txt contains a sitewide crawl block')
if 'sitemap.xml' not in robots.lower():
    raise RuntimeError('Deploy blocked: robots.txt does not advertise sitemap.xml')

verification = (DIST / 'google02c383ec58048d5e.html').read_text(encoding='utf-8').lower()
if 'google-site-verification' not in verification:
    raise RuntimeError('Deploy blocked: Google Search Console verification artifact is invalid')

for rel in ('index.html', 'tedori-hikaku/index.html', 'kaitai-check/index.html'):
    page = (DIST / rel).read_text(encoding='utf-8')
    for href in ('/tedori-hikaku/', '/kaitai-check/'):
        if f'href="{href}"' not in page:
            raise RuntimeError(f'Deploy blocked: {href} missing from {rel} navigation/content')

tedori = (DIST / 'tedori-hikaku/index.html').read_text(encoding='utf-8')
if 'tedori_kawagoe_airbank_precontract' not in tedori:
    raise RuntimeError('Deploy blocked: Kawagoe pre-contract airbank gate missing from tedori-hikaku')
if 'tedori_subsidy_bridge' not in tedori:
    raise RuntimeError('Deploy blocked: subsidy-to-take-home bridge missing from tedori-hikaku')
if 'tedori_real_quotes_v2' not in tedori or 'real_appraisal_compare' not in tedori:
    raise RuntimeError('Deploy blocked: real appraisal comparison v2 missing from tedori-hikaku')
if 'tedori_tax_gate_v1' not in tedori or 'www.nta.go.jp/taxes/shiraberu/taxanswer/joto/3306.htm' not in tedori:
    raise RuntimeError('Deploy blocked: inherited-home tax eligibility gate missing from tedori-hikaku')
for required_label in ('家財・不用品の買取額', '残置物の処分・撤去で自己負担する額'):
    if required_label not in tedori:
        raise RuntimeError(f'Deploy blocked: quote comparison field missing: {required_label}')

print('Post-build crawl/index/navigation/conversion gate passed')
