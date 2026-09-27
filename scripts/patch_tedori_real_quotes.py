from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'static_pages/tedori-hikaku/index.html'
text = path.read_text(encoding='utf-8')
MARKER = 'tedori_real_quotes_v1'
if MARKER in text:
    print('real appraisal comparison already present')
    raise SystemExit(0)

anchor = '<section class="section notice"><strong>重要：これは税前の概算比較です</strong>'
if anchor not in text:
    raise SystemExit('real appraisal insertion anchor not found')

section = '''<section class="section" id="tedori_real_quotes_v1"><div class="eyebrow">査定が届いた人向け</div><h2>実際の買取査定を3社まで、手残りで比べる</h2><p>査定額だけで決めず、残置物処分など自己負担になる費用を引いた金額で比較します。会社名は端末内の表示だけに使い、送信しません。</p><form id="quote-compare" class="diagnosis"><label>1社目 名前（任意）<input id="q1n" type="text" placeholder="A社"></label><label>査定額（万円）<input id="q1p" type="number" min="0" step="1"></label><label>自己負担費用（万円）<input id="q1c" type="number" min="0" step="1" value="0"></label><label>2社目 名前（任意）<input id="q2n" type="text" placeholder="B社"></label><label>査定額（万円）<input id="q2p" type="number" min="0" step="1"></label><label>自己負担費用（万円）<input id="q2c" type="number" min="0" step="1" value="0"></label><label>3社目 名前（任意）<input id="q3n" type="text" placeholder="C社"></label><label>査定額（万円）<input id="q3p" type="number" min="0" step="1"></label><label>自己負担費用（万円）<input id="q3c" type="number" min="0" step="1" value="0"></label><button class="button" type="submit">実査定の手残りを比較する</button></form><div id="quote-result" class="result" aria-live="polite"></div><p><small>比較後は、残置物の扱い・引渡し条件・契約不適合責任・追加費用の有無を各社へ確認してください。最高査定額が最高手残りとは限りません。</small></p></section>'''
text = text.replace(anchor, section + anchor, 1)
script_anchor = '</body></html>'
script = '''<script>(function(){const f=document.getElementById('quote-compare');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();const rows=[1,2,3].map(function(i){const p=Math.max(0,Number(document.getElementById('q'+i+'p').value)||0),c=Math.max(0,Number(document.getElementById('q'+i+'c').value)||0),name=document.getElementById('q'+i+'n').value.trim()||i+'社目';return{name:name,price:p,cost:c,net:p-c};}).filter(function(x){return x.price>0;}).sort(function(a,b){return b.net-a.net;});const r=document.getElementById('quote-result');if(!rows.length){r.innerHTML='<p>査定額を1社以上入力してください。</p>';r.style.display='block';return;}r.innerHTML='<h3>実質手残り順</h3><ol>'+rows.map(function(x){return '<li><strong>'+x.name.replace(/[&<>\"']/g,'')+'：約'+x.net.toLocaleString()+'万円</strong>（査定 '+x.price.toLocaleString()+'万円 − 自己負担 '+x.cost.toLocaleString()+'万円）</li>';}).join('')+'</ol><p>金額以外の契約条件も揃えてから決めてください。</p>';r.style.display='block';window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'real_appraisal_compare',quote_count:rows.length});});})();</script>'''
if script_anchor not in text:
    raise SystemExit('body anchor not found')
text = text.replace(script_anchor, script + script_anchor, 1)
path.write_text(text, encoding='utf-8')
print('added real appraisal comparison mode')
