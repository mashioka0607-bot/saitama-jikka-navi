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
    fields.append(f'''<fieldset><legend>{i}社目</legend><label>提示の種類<select id="q{i}t"><option value="unknown">選択してください</option><option value="broker">仲介の売却査定（成約額未確定）</option><option value="buyout">不動産会社の直接買取提示</option></select></label><label>会社名（任意）<input id="q{i}n" type="text" placeholder="{name}"></label><label>不動産の査定額（万円）<input id="q{i}p" type="number" min="0" step="1"></label><label>家財・不用品の買取額（万円）<input id="q{i}r" type="number" min="0" step="1" value="0"></label><label>残置物の処分・撤去で自己負担する額（万円）<input id="q{i}d" type="number" min="0" step="1" value="0"></label><label>仲介手数料等（万円・直接買取では通常0）<input id="q{i}f" type="number" min="0" step="0.1" placeholder="買取なら0と入力"></label><label>その他の自己負担費用（万円）<input id="q{i}c" type="number" min="0" step="1" value="0"></label><label>売却・決済までの見込期間（月）<input id="q{i}m" type="number" min="0" step="1" value="0"></label></fieldset>''')
section = '''<section class="section" id="tedori_real_quotes_v2"><div class="eyebrow">査定が届いた人向け</div><h2>家財ごと査定した3社を「実質受取額」で比較</h2><p>空き家の査定額だけでなく、家財の買取額を足し、残置物の処分・撤去費、仲介手数料等とその他の自己負担を引いて比較します。片付け前・荷物が残った状態で査定を取った後に使ってください。<strong>家財買取額は不動産査定額とは別に受け取れる金額だけ入力</strong>してください。査定額に含まれる場合は0万円とし、二重計上を防いでください。</p><p class="notice" id="quote-clearance-net-warning-v1"><strong>片付け費の二重計上にも注意：</strong>家財買取18万円を差し引いた後の請求額42万円を「残置物の処分・撤去で自己負担する額」に入力するなら、「家財・不用品の買取額」は0万円にしてください。相殺前の片付け費60万円を入力する場合だけ、別受取の家財買取額18万円を加算します。請求書に記載された支払額が相殺前・相殺後のどちらか確認してください。</p><p class="notice" id="quote-type-disclosure-v1"><strong>仲介査定額は成約価格の保証ではありません。</strong>直接買取の提示価格と同じ確実性ではないため、見込みの手取り差だけで選ばず、価格の根拠・提示の有効期限・売却見込期間・残置物の引渡条件を比べてください。直接買取も売買契約前の提示条件を確認してください。<a href="https://suumo.jp/baikyaku/" target="_blank" rel="noopener">査定と売却の流れ（SUUMO）</a></p><form id="quote-compare" class="diagnosis">''' + ''.join(fields) + '''<label>月間維持費（万円・各社共通）<input id="quote-monthly" type="number" min="0" step="0.1" value="1"></label><p><small>空き家の税金・管理・保険・交通費などの月額を入力。見込期間が不明な社は0か月で計算され、実際の維持費が過小になる可能性があります。</small></p><button class="button" type="submit">維持費まで差し引いて比較する</button></form><div id="quote-result" class="result" aria-live="polite"></div><p><small>仲介手数料は業者ごとの見積・媒介条件で確認して入力してください。査定額を入力した会社は仲介手数料等も入力してください（直接買取の場合は0万円と入力）。直接買取では通常、仲介手数料は発生しません。<a href="https://www.mlit.go.jp/totikensangyo/const/1_6_bf_000013.html" target="_blank" rel="noopener">国土交通省：仲介手数料の説明</a></small></p><details id="quote-handover-check" class="notice"><summary>契約前チェック：残置物ありの査定を同じ条件で比べる</summary><ul><li>引渡時に残す家財・撤去する家財を写真や一覧で特定する</li><li>処分する当事者と費用負担、追加請求の条件を見積書・契約書で確認する</li><li>引渡期限、契約不適合責任、その他の売主負担を含む条件を各社へ書面で確認する</li></ul><p><small>「現況買取」でも家財を無条件で引き取るとは限りません。査定額が最も高い会社が手取りも最大とは限らないため、各社の合意条件で最終判断してください。</small></p></details></section>'''
text = text.replace(anchor, section + anchor, 1)
script_anchor = '</body></html>'
script = '''<script>(function(){const f=document.getElementById('quote-compare');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();const num=function(id){return Math.max(0,Number(document.getElementById(id).value)||0)};const r=document.getElementById('quote-result');if([1,2,3].some(function(i){return num('q'+i+'p')>0&&document.getElementById('q'+i+'t').value==='unknown';})){r.innerHTML='<p>査定額を入力した会社について、提示の種類（仲介の売却査定／直接買取提示）を選択してください。</p>';r.style.display='block';return;}if([1,2,3].some(function(i){return num('q'+i+'p')>0&&document.getElementById('q'+i+'f').value.trim()==='';})){r.innerHTML='<p>査定額がある会社は仲介手数料等を入力してください。直接買取は0万円と入力してください。</p>';r.style.display='block';return;}const monthly=num('quote-monthly');const rows=[1,2,3].map(function(i){const mode=document.getElementById('q'+i+'t').value,price=num('q'+i+'p'),reuse=num('q'+i+'r'),disposal=num('q'+i+'d'),other=num('q'+i+'c'),fee=num('q'+i+'f'),months=num('q'+i+'m'),name=document.getElementById('q'+i+'n').value.trim()||i+'社目';return{name:name,mode:mode,price:price,reuse:reuse,disposal:disposal,other:other,fee:fee,months:months,holding:months*monthly,net:price+reuse-disposal-fee-other-months*monthly};}).filter(function(x){return x.price>0;}).sort(function(a,b){return b.net-a.net;});if(!rows.length){r.innerHTML='<p>不動産の査定額を1社以上入力してください。</p>';r.style.display='block';return;}r.innerHTML=(rows.length===1?'<h3>1社の実質受取額（まだ比較前）</h3><p>他社の査定も入力すると、残置物負担を含む手取り差を比較できます。</p>':'<h3>実質受取額順</h3>')+'<ol>'+rows.map(function(x){return '<li><strong>'+x.name.replace(/[&<>\"']/g,'')+'（'+(x.mode==='buyout'?'直接買取の提示':x.mode==='broker'?'仲介の査定':'提示の種類未選択')+'）：約'+x.net.toLocaleString()+'万円</strong><br>不動産 '+x.price.toLocaleString()+'万円 ＋ 家財買取 '+x.reuse.toLocaleString()+'万円 − 残置物処分 '+x.disposal.toLocaleString()+'万円 − 仲介手数料等 '+x.fee.toLocaleString()+'万円 − その他 '+x.other.toLocaleString()+'万円 − 維持費 '+x.holding.toLocaleString()+'万円（'+x.months.toLocaleString()+'か月）</li>';}).join('')+'</ol><p><strong>表示順位は入力金額を基にした税前の見込みです。仲介の査定額は成約保証ではなく、直接買取の提示も契約前には条件変更の可能性があります。</strong>提示価格の根拠・有効期限・引渡条件を確認してください。</p><p>金額以外の契約条件も揃えてから決めてください。</p><p><a href="https://www.pref.saitama.lg.jp/a1106/akiya/r7_akiyacoodinator.html" target="_blank" rel="noopener">埼玉県の無料相談窓口を確認</a> ／ <a href="https://www.pref.saitama.lg.jp/a1107/akiyabanku.html" target="_blank" rel="noopener">所在地の空き家バンク条件を確認</a></p>';r.style.display='block';if(typeof window.gtag==='function'){window.gtag('event',rows.length>=2?'real_appraisal_compare':'real_appraisal_single_quote',{comparison_version:'v3',quote_count:rows.length});}});})();</script>'''
if script_anchor not in text:
    raise SystemExit('body anchor not found')
text = text.replace(script_anchor, script + script_anchor, 1)
path.write_text(text, encoding='utf-8')
print('added real appraisal comparison v2 with furniture/disposal split')
