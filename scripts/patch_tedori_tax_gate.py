from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'static_pages/tedori-hikaku/index.html'
text = path.read_text(encoding='utf-8')
MARKER = 'tedori_tax_gate_v1'
if MARKER in text:
    print('tax eligibility gate already present')
    raise SystemExit(0)

anchor = '<section class="section notice"><strong>重要：これは税前の概算比較です</strong>'
if anchor not in text:
    raise SystemExit('tax gate insertion anchor not found')

section = '''<section class="section" id="tedori_tax_gate_v1"><div class="eyebrow">税引後手取りの前に</div><h2>相続空き家の3,000万円特別控除は「使える可能性」を先に確認</h2><p>相続した実家では、一定の要件を満たすと譲渡所得から最高3,000万円を控除できる特例があります。令和6年1月1日以後の譲渡で相続人が3人以上の場合は1人あたり最高2,000万円です。売却額から直接3,000万円引かれる制度ではなく、適用可否で税引後の手取りが大きく変わるため、このページでは税額を自動断定しません。</p><div class="facts"><div class="fact"><strong>① 相続した実家か</strong><br>被相続人が相続開始直前まで居住していた家屋・敷地等か確認</div><div class="fact"><strong>② 建築時期など</strong><br>昭和56年5月31日以前の建築など、国税庁の対象要件を確認</div><div class="fact"><strong>③ 売却期限・価格など</strong><br>売却時期、譲渡価額、耐震・取壊し等を含む要件を確認</div></div><p><a class="button" href="https://www.nta.go.jp/taxes/shiraberu/taxanswer/joto/3306.htm" target="_blank" rel="noopener">国税庁 No.3306 で適用要件を確認する</a></p><p><small>2026年4月1日現在の国税庁案内を参照。個別の適用可否・税額は税務署または税理士へ確認してください。</small></p></section>'''
text = text.replace(anchor, section + anchor, 1)
path.write_text(text, encoding='utf-8')
print('added inherited-home tax eligibility gate')
