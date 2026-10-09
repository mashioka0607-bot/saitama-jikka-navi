from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
page = ROOT / "static_pages/tedori-hikaku/index.html"
html = page.read_text(encoding="utf-8")
marker = 'id="broker-fee-guide-v1"'
if marker in html:
    print("Broker fee guide already present")
    raise SystemExit(0)

anchor = '<label>仲介手数料等（万円・概算を入力）'
if anchor not in html:
    raise RuntimeError("Broker fee input anchor not found; refusing to patch")

guide = '''<div class="notice" id="broker-fee-guide-v1" aria-live="polite">
<strong>売却価格に応じた仲介手数料の参考上限（税込）</strong>
<p id="broker-fee-estimate">売却価格を入力すると、一般的な上限額の目安を表示します。</p>
<p>800万円以下の宅地・建物は、低廉な空家等の特例により、媒介に要する費用を勘案して税込33万円まで受領できる場合があります。実際の報酬は契約時に確認してください。上限額が必ず請求されるわけではありません。</p>
<p>下の「仲介手数料等」は手数料以外の費用も含めて入力する欄です。参考額を自動で上書きしません。</p>
<p><small>出典：<a href="https://www.mlit.go.jp/totikensangyo/const/1_6_bf_000013.html" target="_blank" rel="noopener">国土交通省｜不動産取引に関するお知らせ（媒介報酬の上限・低廉な空家等の特例）</a></small></p>
</div>'''
html = html.replace(anchor, guide + anchor, 1)
script = '''<script>(function(){
  const sale = document.getElementById('sale');
  const output = document.getElementById('broker-fee-estimate');
  if (!sale || !output) return;
  function regularFee(price) {
    if (price <= 0) return 0;
    const pretax = price <= 200 ? price * 0.05
      : price <= 400 ? price * 0.04 + 2
      : price * 0.03 + 6;
    return pretax * 1.1;
  }
  function render() {
    const price = Math.max(0, Number(sale.value) || 0);
    const normal = regularFee(price);
    const yen = n => n.toLocaleString('ja-JP', {maximumFractionDigits: 2});
    output.textContent = '通常の仲介手数料の上限目安：約' + yen(normal)
      + '万円（税込）。' + (price > 0 && price <= 800
        ? '低廉な空家等の特例を適用する場合の上限は33万円（税込）です。'
        : '800万円以下の特例対象価格ではありません。');
  }
  sale.addEventListener('input', render);
  render();
})();</script>'''
if '</body></html>' not in html:
    raise RuntimeError("HTML end anchor missing; refusing to patch")
html = html.replace('</body></html>', script + '</body></html>', 1)
page.write_text(html, encoding="utf-8")
print("Added price-aware broker fee reference without overwriting user costs")
