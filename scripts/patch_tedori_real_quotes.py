from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'static_pages/tedori-hikaku/index.html'
text = path.read_text(encoding='utf-8')
MARKER = 'tedori_real_quotes_v2'
if MARKER in text:
    print('real appraisal comparison v2 already present')
    raise SystemExit(0)

# Upgrade an older deploy-patched version cleanly before inserting v2.
old_start = '<section class="section" id="tedori_real_quotes_v1">'
if old_start in text:
    end = text.find('</section>', text.find(old_start))
    if end != -1:
        text = text[:text.find(old_start)] + text[end + len('</section>'):]
    script_start = "<script>(function(){const f=document.getElementById('quote-compare');"
    pos = text.find(script_start)
    if pos != -1:
        send = text.find('</script>', pos)
        if send != -1:
            text = text[:pos] + text[send + len('</script>'):]

anchor = '<section class="section notice"><strong>重要：これは税前の概算比較です</strong>'
if anchor not in text:
    raise SystemExit('real appraisal insertion anchor not found')

fields = []
for i, name in ((1,'A社'),(2,'B社'),(3,'C社')):
    fields.append(f'''<fieldset><legend>{i}社目</legend><label>会社名（任意）<input id="q{i}n" type="text" placeholder="{name}"></label><label>不動産の査定額（万円）<input id="q{i}p" type="number" min="0" step="1"></label><label>家財・不用品の買取額（万円）<input id="q{i}r" type="number" min="0" step="1" value="0"></label><label>残置物の処分・撤去で自己負担する額（万円）<input id="q{i}d" type="number" min="0" step="1" value="0"></label><label>仲介手数料等（万円・直接買取では通常0）<input id="q{i}f" type="number" min="0" step="0.1" placeholder="買取なら0と入力"></label><label>その他の自己負担費用（万円）<input id="q{i}c" type="number" min="0" step="1" value="0"></label></fieldset>''')
section = '''<section class="section" id="tedori_real_quotes_v2"><div class="eyebrow">査定が届いた人向け</div><h2>家財ごと査定した3社を「実質受取額」で比較</h2><p>空き家の査定額だけでなく、家財の買取額を足し、残置物の処分・撤去費、仲介手数料等とその他の自己負担を引いて比較します。片付け前・荷物が残った状態で査定を取った後に使ってください。</p><form id="quote-compare" class="diagnosis">''' + ''.join(fields) + '''<button class="button" type="submit">不動産＋家財－処分費で比較する</button></form><div id="quote-result" class="result" aria-live="polite"></div><p><small>仲介手数料は業者ごとの見積・媒介条件で確認して入力してください。査定額を入力した会社は仲介手数料等も入力してください（直接買取の場合は0万円と入力）。直接買取では通常、仲介手数料は発生しません。<a href="https://www.mlit.go.jp/totikensangyo/const/1_6_bf_000013.html" target="_blank" rel="noopener">国土交通省：仲介手数料の説明</a></small></p><p><small>比較後は、残置物の扱い、引渡し条件、契約不適合責任、追加費用の有無を各社へ確認してください.最高査定額が最高手残りとは限りません。</small></p></section>'''
text = text.replace(anchor, section + anchor, 1)
script_anchor = '</body></html>'
script = '''<script>(function(){const f=document.getElementById('quote-compare');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();const num=function(id){return Math.max(0,Number(document.getElementById(id).value)||0)};const r=document.getElementById('quote-result');if([1,2,3].some(function(i){return num('q'+i+'p')>0&&document.getElementById('q'+i+'f').value.trim()==='';})){r.innerHTML='<p>査定額がある会社は仲介手数料等を入力してください。直接買取は0万円と入力してください。</p>';r.style.display='block';return;}const rows=[1,2,3].map(function(i){const price=num('q'+i+'p'),reuse=num('q'+i+'r'),disposal=num('q'+i+'d'),other=num('q'+i+'c'),fee=num('q'+i+'f'),name=document.getElementById('q'+i+'n').value.trim()||i+'社目';return{name:name,price:price,reuse:reuse,disposal:disposal,other:other,fee:fee,net:price+reuse-disposal-fee-other};}).filter(function(x){return x.price>0;}).sort(function(a,b){return b.net-a.net;});if(!rows.length){r.innerHTML='<p>不動産の査定額を1社以上入力してください。</p>';r.style.display='block';return;}r.innerHTML='<h3>実質受取額順</h3><ol>'+rows.map(function(x){return '<li><strong>'+x.name.replace(/[&<>\"']/g,'')+'：約'+x.net.toLocaleString()+'万円</strong><br>不動産 '+x.price.toLocaleString()+'万円 ＋ 家財買取 '+x.reuse.toLocaleString()+'万円 − 残置物処分 '+x.disposal.toLocaleString()+'万円 − 仲介手数料等 '+x.fee.toLocaleString()+'万円 − その他 '+x.other.toLocaleString()+'万円</li>';}).join('')+'</ol><p>金額以外の契約条件も揃えてから決めてください。</p><p><a href="https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html" target="_blank" rel="noopener">埼玉県の無料相談窓口を確認</a> ／ <a href="https://www.pref.saitama.lg.jp/a1107/akiyabanku.html" target="_blank" rel="noopener">所在地の空き家バンク条件を確認</a></p>';r.style.display='block';if(typeof window.gtag==='function'){window.gtag('event','real_appraisal_compare',{comparison_version:'v2',quote_count:rows.length});}});})();</script>'''
if script_anchor not in text:
    raise SystemExit('body anchor not found')
text = text.replace(script_anchor, script + script_anchor, 1)
path.write_text(text, encoding='utf-8')
print('added real appraisal comparison v2 with furniture/disposal split')
