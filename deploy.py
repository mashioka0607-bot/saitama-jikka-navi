from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
subprocess.run([sys.executable, str(ROOT / 'build.py')], check=True)

verification = ROOT / 'google02c383ec58048d5e.html'
if verification.exists():
    shutil.copy2(verification, DIST / verification.name)
    print(f'Copied Search Console verification file: {verification.name}')

# Cloudflare Pages custom headers. This makes the sitemap unambiguously XML for crawlers.
headers = DIST / '_headers'
headers.write_text(
    '/sitemap.xml\n'
    '  Content-Type: application/xml; charset=UTF-8\n'
    '  Cache-Control: no-cache\n\n'
    '/robots.txt\n'
    '  Content-Type: text/plain; charset=UTF-8\n',
    encoding='utf-8'
)
print('Wrote Cloudflare _headers for sitemap.xml and robots.txt')
