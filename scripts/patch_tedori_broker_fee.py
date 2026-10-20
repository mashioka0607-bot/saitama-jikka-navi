"""Add a sale-price-linked brokerage fee reference to the static take-home calculator.

The normal fee estimate follows the entered sale price until the user edits
the fee field.  The exceptional fee is never selected without a click.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "static_pages" / "tedori-hikaku" / "index.html"
MARKER = "broker_fee_reference_v1"
html = PAGE.read_text(encoding="utf-8")
if MARKER in html:
    print("Brokerage reference already present")
    raise SystemExit(0)

anchor = '<label>仲介手数料等（万円・概算を入力）'
if html.count(anchor) != 1 or html.count("</body>") != 1:
    raise SystemExit("Brokerage reference insertion anchors not unique")

reference = """<div id="broker_fee_reference_v1" class="notice" style="margin:1em 0" aria-live="polite">
<strong>仲介手数料の参考上限（税込）</strong>
<p id="broker-fee-summary">売却価格に応じて表示します。</p>
<p><button id="apply-standard-fee" type="button">通常上限で自動計算に戻す</button>
<button id="apply-special-fee" type="button" hidden>800万円以下の特例上限を反映</button></p>
<p><small>通常上限の参考額は自動入力され、費用欄を手動編集した後は上書きしません。特例上限33万円は利用者が選んだ場合だけ反映し、売却価格が800万円を超えたら自動解除します。<br>2024年7月1日施行の国土交通省の報酬規制に基づく概算。通常上限は売買価格の消費税等相当額を除いた額で計算します。800万円以下の宅地・建物は、媒介に要する費用等を勘案し、事前合意のうえ税込33万円まで受領できる特例があります。33万円が必ず請求されるわけではありません。実際の報酬額は媒介契約前に確認してください。ボタンで反映するのは仲介手数料のみです。登記・測量等の他費用があれば費用欄に加算してください。<a href="https://www.mlit.go.jp/totikensangyo/const/1_6_bf_000013.html" target="_blank" rel="noopener">国土交通省の公式説明</a></small></p>
</div>"""
html = html.replace(anchor, reference + anchor, 1)
script = """<script id="broker-fee-reference-script">
(function(){
  const sale = document.getElementById('sale');
  const broker = document.getElementById('broker');
  const summary = document.getElementById('broker-fee-summary');
  const special = document.getElementById('apply-special-fee');
  const standard = document.getElementById('apply-standard-fee');
  if (!sale || !broker || !summary || !special || !standard) return;
  const round1 = n => Math.round(n * 10) / 10;
  function values(){
    const price = Math.max(0, Number(sale.value) || 0);
    const base = Math.min(price,200)*.05 + Math.min(Math.max(price-200,0),200)*.04 + Math.max(price-400,0)*.03;
    return {price, usual:round1(base*1.1), exceptional:price>0 && price<=800?33:null};
  }
  let mode = 'auto'; // auto, special, or manual
  broker.addEventListener('input',()=>{ mode='manual'; });
  function render(){
    const v=values();
    if(mode==='special' && v.exceptional===null) mode='auto';
    if(mode==='auto') broker.value=v.usual;
    summary.textContent='通常の上限目安：'+v.usual.toLocaleString('ja-JP')+'万円'
      +(v.exceptional===null?'。800万円超のため低廉な空家等の特例対象外です。':
      ' ／ 低廉な空家等の特例上限：33万円（適用・請求額は媒介契約前に確認）。');
    special.hidden=v.exceptional===null;
  }
  standard.addEventListener('click',()=>{mode='auto';render();broker.focus();});
  special.addEventListener('click',()=>{
    const v=values();
    if(v.exceptional!==null){mode='special';broker.value=v.exceptional;broker.focus();}
  });
  sale.addEventListener('input',render);
  render();
})();
</script>"""
html = html.replace("</body>", script + "</body>", 1)
PAGE.write_text(html, encoding="utf-8")
print("Added price-linked brokerage reference (standard and low-value exception)")
