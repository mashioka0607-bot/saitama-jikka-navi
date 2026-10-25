from pathlib import Path
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'

# Apply idempotent source patches before quality/build so deploy output cannot regress.
for patch_name in ('patch_build_quality.py', 'patch_home_saitama_gate.py', 'patch_high_intent_nav.py', 'patch_tedori_precontract_bank.py', 'patch_tedori_subsidy_bridge.py', 'patch_tedori_real_quotes.py', 'patch_tedori_tax_gate.py'):
    patcher = ROOT / 'scripts' / patch_name
    if patcher.exists():
        subprocess.run([sys.executable, str(patcher)], check=True)

# Prevent public subsidy numbers and reviewed source data drifting apart.
subprocess.run([sys.executable, str(ROOT / 'scripts' / 'check_grant_status_consistency.py')], check=True)

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

# Curated pages are copied after the generated layout, so keep the editorial
# disclosure reachable from their footer as well (without editing page content).
editorial_link = '<a href="/editorial-policy/">編集方針</a>'
operator_link = '<a href="/operator/">運営者情報</a>'
for html_path in DIST.rglob('*.html'):
    markup = html_path.read_text(encoding='utf-8')
    if '<footer' not in markup.lower() or editorial_link in markup:
        continue
    if markup.count(operator_link) == 1:
        markup = markup.replace(operator_link, operator_link + ' · ' + editorial_link, 1)
        html_path.write_text(markup, encoding='utf-8')

# The curated static HTML is copied *after* build.py generates GA4-tagged pages.
# Inject the same GA4 config into copied pages, but only when GA4 is enabled.
site_config = json.loads((ROOT / 'site_data.json').read_text(encoding='utf-8'))
ga4_id = (site_config.get('ga4_id') or '').strip()
if ga4_id:
    if not re.fullmatch(r'G-[A-Z0-9]+', ga4_id):
        raise RuntimeError('Invalid GA4 measurement ID in site_data.json')
    ga4_snippet = (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={ga4_id}"></script>'
        '<script>window.dataLayer=window.dataLayer||[];'
        'function gtag(){dataLayer.push(arguments)}'
        "gtag('js',new Date());"
        f"gtag('config','{ga4_id}');</script>"
    )
    for html_path in DIST.rglob('*.html'):
        markup = html_path.read_text(encoding='utf-8')
        if '</head>' not in markup.lower():
            continue  # Google verification file is not a full HTML document.
        if 'googletagmanager.com/gtag/js' in markup:
            continue  # build.py already configured GA4 for generated pages.
        markup = re.sub(r'</head>', lambda m: ga4_snippet + m.group(0), markup, count=1, flags=re.IGNORECASE)
        html_path.write_text(markup, encoding='utf-8')
        print(f'Injected GA4 into static HTML: {html_path.relative_to(DIST)}')

# Curated high-intent pages are copied after build.py, so they do not receive
# build.py's public-link event listener. Measure exits to official sites on
# these pages alongside ASP clicks, without sending any user-entered values.
# Use delegated handling: quote-result links are rendered after form submit.
if ga4_id:
    for relative in ('tedori-hikaku/index.html', 'kaitai-check/index.html'):
        page_path = DIST / relative
        markup = page_path.read_text(encoding='utf-8')
        marker = 'id="official-exit-tracking-v1"'
        if marker in markup:
            continue
        if markup.count('</body>') != 1:
            raise RuntimeError(f'Official-exit tracking insertion failed: {relative}')
        script = """<script id="official-exit-tracking-v1">(function(){
document.addEventListener('click', function(event) {
  const link = event.target && event.target.closest && event.target.closest('a[href]');
  if (!link || typeof window.gtag !== 'function') return;
  let url;
  try { url = new URL(link.href, window.location.href); } catch (_) { return; }
  const host = url.hostname.toLowerCase();
  // Some verified Saitama municipal sites use .saitama.jp, not .lg.jp.
  // Match only exact audited hosts; never allow every .saitama.jp domain.
  const knownMunicipalHosts = new Set([
    'www.city.kawagoe.saitama.jp',
    'www.city.fujimi.saitama.jp',
    'www.town.hatoyama.saitama.jp'
  ]);
  if (!host.endsWith('.lg.jp') && !host.endsWith('.go.jp') &&
      !knownMunicipalHosts.has(host)) return;
  window.gtag('event','official_source_click',{
    context: link.dataset.context || 'curated_static',
    destination_host: host,
    source_page: window.location.pathname
  });
});
})();</script>"""
        markup = markup.replace('</body>', script + '</body>', 1)
        page_path.write_text(markup, encoding='utf-8')
        print(f'Enabled GA4 official-source exit tracking: {relative}')

# Put the approved offer at the point of highest intent, after the user
# finishes the take-home comparison. A configured offer is never invented.
# The static tedori page is copied after build.py, so generated-page CTAs
# alone cannot monetize it.
from html import escape as html_escape
from urllib.parse import urlsplit
primary_offer = next(
    (offer for offer in site_config.get('offers', [])
     if offer.get('id') == 'primary' and (offer.get('url') or '').strip()),
    None,
)
if primary_offer:
    # The ASP's approved tracking URL can record applications before GA4 is set.
    # GA4 is optional for event analytics; never block a legitimate paid CTA.
    offer_url = primary_offer['url'].strip()
    parts = urlsplit(offer_url)
    if parts.scheme != 'https' or not parts.netloc:
        raise RuntimeError('Primary offer requires an approved HTTPS URL')
    tedori_path = DIST / 'tedori-hikaku' / 'index.html'
    markup = tedori_path.read_text(encoding='utf-8')
    # Disclosure must be visible before the comparison hero, not only after
    # a visitor submits the form and sees the affiliate CTA in the result.
    main_anchor = '<main class="wrap">'
    disclosure = (
        '<div id="tedori-ad-disclosure" class="notice" role="note">'
        '<strong>[PR] アフィリエイト広告について</strong>'
        '<p>このページには広告が含まれます。提携先への申込み等により'
        '当サイトが報酬を受け取る場合があります。'
        '掲載サービスへの申込みは任意で、比較計算の結果とは独立しています。</p>'
        '</div>'
    )
    if markup.count(main_anchor) != 1 or 'id="tedori-ad-disclosure"' in markup:
        raise RuntimeError('Tedori first-view ad disclosure anchor missing or duplicated')
    markup = markup.replace(main_anchor, main_anchor + disclosure, 1)
    result_anchor = '<div id="r" class="result" aria-live="polite"></div>'
    if markup.count(result_anchor) != 1 or 'id="tedori-affiliate-next"' in markup:
        raise RuntimeError('Tedori conversion insertion point missing or duplicated')
    callout = (
        '<aside id="tedori-affiliate-next" class="cta" hidden>'
        '<span class="pr">PR</span>'
        '<h2>手取りを比較したら、実際の見積条件を確認</h2>'
        '<p>査定額だけでなく、家財・残置物の扱い、追加費用、引渡し条件も確認してから比較してください。</p>'
        f'<p><strong>{html_escape(primary_offer.get("name") or "提携サービス")}</strong></p>'
        '<a class="button invert affiliate" data-offer="primary" '
        'data-context="tedori_compare_complete" '
        'rel="sponsored noopener" target="_blank" '
        f'href="{html_escape(offer_url, quote=True)}">'
        f'{html_escape(primary_offer.get("label") or "無料相談・見積もりを確認")}</a>'
        '<small>PR・アフィリエイト広告です。成約条件等は遷移先で確認してください。</small>'
        '</aside>'
    )
    markup = markup.replace(result_anchor, result_anchor + callout, 1)
    event_script = """<script>(function(){
const form=document.getElementById('calc');
const next=document.getElementById('tedori-affiliate-next');
if(!form||!next)return;
// Count eligible ad impressions, not just outbound clicks. Repeated submits
// of the same comparison stage must not inflate the view denominator.
const viewedSteps=new Set();
function revealOffer(step){
  next.hidden=false;
  next.dataset.comparisonStep=step;
  // Show an approved offer beside the actual result, before the neutral
  // public-service fallback. A visitor should not have to scroll past
  // an unrelated diagnosis loop to reach the quote next step.
  const result=document.getElementById(step==='estimate'?'r':'quote-result');
  if(result){
    const publicLink=result.querySelector('#result-next');
    const publicParagraph=publicLink&&publicLink.closest('p');
    if(publicParagraph&&publicParagraph.parentNode===result){
      result.insertBefore(next,publicParagraph);
      publicLink.classList.remove('button');
    }else if(next.parentNode!==result){
      result.appendChild(next);
    }
  }
  if(!viewedSteps.has(step)){
    viewedSteps.add(step);
    if(typeof window.gtag==='function'){
      window.gtag('event','cta_view',{
        offer:'primary',context:step,source_page:window.location.pathname
      });
    }
  }
}
form.addEventListener('submit',function(){revealOffer('estimate');});
const quoteForm=document.getElementById('quote-compare');
if(quoteForm){
  quoteForm.addEventListener('submit',function(){
    const priced=[1,2,3].filter(function(i){
      const price=document.getElementById('q'+i+'p');
      return price&&Number(price.value)>0;
    });
    const ready=priced.length>0&&priced.every(function(i){
      const fee=document.getElementById('q'+i+'f');
      return fee&&fee.value.trim()!=='';
    });
    // The real-quote comparison rejects any priced row without a fee.
    // Do not expose the paid CTA after that validation error.
    next.hidden=!ready;
    if(ready)revealOffer(priced.length>=2?'real_quotes_compare':'single_quote');
  });
}
const link=next.querySelector('.affiliate');
link.addEventListener('click',function(){
  if(typeof window.gtag==='function'){
    window.gtag('event','affiliate_click',{offer:'primary',context:next.dataset.comparisonStep||'estimate'});
  }
});
})();</script>"""
    if markup.count('</body>') != 1:
        raise RuntimeError('Tedori body insertion point missing or duplicated')
    markup = markup.replace('</body>', event_script + '</body>', 1)
    tedori_path.write_text(markup, encoding='utf-8')
    print('Injected approved primary offer after tedori comparison with GA4 event')
 
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
# The same-condition quote request lets users acquire comparable real offers
# before returning to the calculated and real-quote comparison steps.
for required in ('id="quote-request-template"', 'id="quote-request-text"', 'id="copy-quote-request"',
                 'quote_request_copy', '処分責任・費用負担'):
    if required not in tedori:
        raise RuntimeError(f'Deploy blocked: real-quote request template missing: {required}')

for required_label in ('家財・不用品の買取額', '残置物の処分・撤去で自己負担する額'):
    if required_label not in tedori:
        raise RuntimeError(f'Deploy blocked: quote comparison field missing: {required_label}')

# Validate the final published HTML, including curated static pages copied after build.py.
# This must run after copytree; source-only SEO checks cannot catch public placeholders.
subprocess.run([sys.executable, str(ROOT / 'scripts' / 'check_public_quality.py')], check=True)

print('Post-build crawl/index/navigation/conversion and public-quality gates passed')
