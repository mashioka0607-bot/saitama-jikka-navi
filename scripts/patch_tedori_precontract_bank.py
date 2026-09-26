from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'static_pages/tedori-hikaku/index.html'
MARKER = '<section class="section"><h2>片付ける前に比較する順番</h2>'
BLOCK = '''<section class="section warning"><h2>川越市の実家なら、媒介契約の前に空き家バンク適格性を確認</h2><p><strong>川越市空き家バンクは、宅地建物取引業者と媒介契約が締結されていない空き家を登録要件の一つにしています。</strong>売却を急いで不動産会社と媒介契約を結ぶ前に、空き家バンクを選択肢として残すか確認してください。</p><p>空き家バンクは必ず高く売れる制度ではなく、登録できても成約を保証するものではありません。ただ、先に媒介契約を結ぶと登録要件から外れるため、比較前に失う可能性がある公的な出口です。片付け・解体・媒介契約の前に、現況査定とあわせて確認する順番をおすすめします。</p><p><a class="public-link" data-context="tedori_kawagoe_airbank_precontract" href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1003032/1003036.html" target="_blank" rel="noopener">川越市公式｜空き家バンクの登録条件を確認する</a></p></section>'''

text = PATH.read_text(encoding='utf-8')
if 'tedori_kawagoe_airbank_precontract' in text:
    print('pre-contract airbank gate already present')
elif MARKER not in text:
    raise SystemExit('expected comparison-order marker not found')
else:
    PATH.write_text(text.replace(MARKER, BLOCK + MARKER, 1), encoding='utf-8')
    print('added pre-contract airbank gate to tedori-hikaku')
