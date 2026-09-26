const grants=[
['川越市','解体補助は個別確認','契約前に市の空き家窓口・対象制度を確認','空き家バンクは売却・賃貸の出口。解体や改修を先に契約せず、現況査定と公的制度の対象可否を確認してから判断','https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1003032/1003036.html'],
['白岡市','受付中・残額少','締切は公式で最新確認','最新の市公式条件を申請前に再確認','https://www.city.shiraoka.lg.jp/soshiki/seikatsukeizaibu/kankyoka/1_1/7523.html'],
['川口市','受付中','事前診断 2026-10-30／交付申請 2026-11-13','事前診断・交付申請の条件を確認してから契約判断','https://www.city.kawaguchi.lg.jp/soshiki/01130/040/akiyatoutaisaku/27633.html'],
['上尾市','受付中','交付申請 2026-10-30','本申請前に市へ事前相談。受付状況確認後に契約判断','https://www.city.ageo.lg.jp/page/421263.html'],
['東松山市','受付中','申請 2026-12-28（予算到達で早期終了）','本申請前に市へ事前相談。補助対象可否を確認してから契約・着工判断','https://www.city.higashimatsuyama.lg.jp/soshiki/37/52176.html'],
['富士見市','受付中','除却補助申請 2027-01-31','補助金交付決定後に工事。交付決定前の契約・着工を前提に進めない','https://www.city.fujimi.saitama.jp/kurashi_tetsuzuki/sumai/2018-0511-1113-58/akiyahojoseido.html'],
['深谷市','受付中','事前調査申込 2026-11-30／工事完了 2027-01-29','不良住宅の事前調査を受け、補助金交付決定後に工事を進める','https://www.city.fukaya.saitama.jp/soshiki/kyoudou/jiti/tanto/akiya/akiyahojyo/14716.html'],
['ときがわ町','受付中','申請 2026-12-25／完了報告 2027-02-26','交付決定前の工事契約NG','https://www.town.tokigawa.lg.jp/Info/3493'],
['坂戸市','受付終了','2026-05-18 上限到達で終了','受付再開を公式で確認するまで補助前提で契約しない','https://www.city.sakado.lg.jp/soshiki/37/28358.html']];
const sel=document.getElementById('grant-city'),out=document.getElementById('grant-result');
if(sel&&out){grants.forEach(g=>{const o=document.createElement('option');o.value=g[0];o.textContent=g[0];sel.appendChild(o)});sel.addEventListener('change',()=>{const g=grants.find(x=>x[0]===sel.value);if(!g){out.innerHTML='';return}const closed=g[1].includes('終了');out.innerHTML=`<h3>${g[0]}：${g[1]}</h3><p><strong>期限：</strong>${g[2]}</p><p><strong>契約判断：</strong>${g[3]}</p><p><strong>${closed?'今やること':'契約前にやること'}：</strong>${closed?'補助前提で進めず、再開有無と別の出口を確認':'自治体へ対象可否・受付状況を確認 → 現況査定 → 見積取得 → 申請/交付決定 → 契約'}</p><p><a class="button" target="_blank" rel="noopener" href="${g[4]}">${g[0]}公式情報を確認</a></p><small>制度は予算・年度で変わります。表示は2026-09-26確認DBに基づき、契約前に公式ページで再確認してください。</small>`})}