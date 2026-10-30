// Regression for published Japan-time grant deadlines. No live budget claims.
// Eligibility and amount in the Kawaguchi selector must not become a generic grant promise.

const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const all = fs.readFileSync('static_pages/kaitai-check/grants.js', 'utf8');
const kawaguchi = all.split('\n').find(line => line.startsWith("['川口市'"));
assert.ok(kawaguchi && kawaguchi.includes('地方税完納') && kawaguchi.includes('事例紹介') && kawaguchi.includes('上限100万円') && kawaguchi.includes('満額支給とは限らない'), 'Kawaguchi official eligibility and payout caveat missing');
assert.ok(kawaguchi.includes('完了報告 2027-01-29'), 'Kawaguchi post-demolition report deadline missing from published selector');
assert.ok(kawaguchi.includes('事前診断10/30公表期限') && !kawaguchi.includes('公表期限内・対象限定'), 'Kawaguchi crawlable selector must not describe an elapsed deadline as still within the window');
const guard = all.slice(all.indexOf('/* Dynamic guard for 2026 municipal grant deadlines.'));
assert.ok(guard.startsWith('/* Dynamic guard'), 'Guard marker missing');

function check(today, city, time = '12:00') {
  let onChange;
  const citySelect = { value: city, addEventListener: (_, fn) => { onChange = fn; } };
  const title = { textContent: city + '：受付中' };
  const notices = [];
  const result = {
    firstChild: {},
    querySelector: () => title,
    insertBefore: note => { notices.push(note.textContent); }
  };
  const document = {
    getElementById: id => id === 'grant-city' ? citySelect : id === 'grant-result' ? result : null,
    createElement: () => ({ setAttribute() {}, textContent: '' })
  };
  const IntlFake = { DateTimeFormat: class { constructor(_, opts) { this.isTime = Boolean(opts.hour); } format() { return this.isTime ? time : today; } } };
  vm.runInNewContext(guard, { document, Intl: IntlFake, Date });
  assert.equal(typeof onChange, 'function');
  onChange();
  return { title: title.textContent, warning: notices.join(' ') };
}

const cases = [
  ['2026-10-22', '川口市', ''],
  ['2026-10-24', '川口市', '残り6日'],
  ['2026-10-30', '川口市', '本日'],
  ['2026-10-31', '川口市', '期限'],
  ['2026-10-24', '東松山市', ''],
  ['2026-11-07', '川口市', '期限'],
  ['2027-04-01', '川口市', '過年度情報']
];
for (const [date, city, expected] of cases) {
  const outcome = check(date, city);
  if (expected) assert.ok(outcome.warning.includes(expected), date + ' / ' + city + ': ' + JSON.stringify(outcome));
  else assert.equal(outcome.warning, '', date + ' / ' + city);
}

const deadlineDay = check('2026-10-30', '川口市');
assert.ok(deadlineDay.warning.includes('9:00～16:30') && deadlineDay.warning.includes('8:30～17:15') && deadlineDay.warning.includes('048-229-7805'), 'municipal contact hours must appear on deadline day');
assert.ok(deadlineDay.warning.includes('郵送先') && deadlineDay.warning.includes('必着'), 'postage destination exists but deadline-day receipt/postmark policy is unverified');
assert.ok(!check('2026-10-24', '川口市').warning.includes('9:00～16:30'), 'last-day contact hours should only appear on the last day');

for (const [time, expected] of [['16:30', '9:00～16:30'], ['16:31', '窓口受付'], ['17:15', '電話の公表受付時間'], ['17:16', 'ともに終了'], ['18:05', 'ともに終了']]) {
  const afterHours = check('2026-10-30', '川口市', time);
  assert.ok(afterHours.warning.includes(expected), 'selector '+time+': '+afterHours.warning);
  if (time >= '17:16') assert.ok(afterHours.title.includes('受付時間終了'), 'selector title '+time);
}

const primaryHtml=fs.readFileSync('static_pages/kaitai-check/index.html','utf8');
const primaryScript=primaryHtml.split('<script id="kawaguchi-primary-deadline-guard">')[1]?.split('</script>')[0];
assert.ok(primaryScript, 'primary municipality alert must have a date-aware guard');
function checkPrimary(today, time = '12:00') {
  const note={hidden:true,textContent:''};
  const IntlFake={DateTimeFormat:class{constructor(_,opts){this.isTime=Boolean(opts.hour);}format(){return this.isTime?time:today;}}};
  vm.runInNewContext(primaryScript,{document:{getElementById:id=>id==='kawaguchi-deadline-status'?note:null},Intl:IntlFake,Date});
  return note;
}
for (const [today,expected,visible] of [
  ['2026-10-22','',false],
  ['2026-10-26','残り4日',true],
  ['2026-10-30','本日',true],
  ['2026-10-31','事前診断依頼の公表期限',true],
  ['2026-11-13','交付申請の公表期限',true],
  ['2026-11-14','ともに経過',true],
  ['2027-04-01','過年度の制度情報',true]
]) {
  const note=checkPrimary(today);
  assert.equal(!note.hidden, visible, 'primary alert visibility on '+today);
  if(expected)assert.ok(note.textContent.includes(expected), 'primary alert text on '+today+': '+note.textContent);
}

for (const [time, expected] of [['16:30', '9:00～16:30'], ['16:31', '窓口受付'], ['17:15', '電話の公表受付時間'], ['17:16', 'ともに終了'], ['18:05', 'ともに終了']]) {
  const afterHours = checkPrimary('2026-10-30', time);
  assert.ok(afterHours.textContent.includes(expected), 'primary '+time+': '+afterHours.textContent);
}

const dayPrimary = checkPrimary('2026-10-30');
assert.ok(dayPrimary.textContent.includes('9:00～16:30') && dayPrimary.textContent.includes('8:30～17:15') && dayPrimary.textContent.includes('048-229-7805'), 'primary deadline warning must show official contact hours');
assert.ok(checkPrimary('2026-10-30','18:05').textContent.includes('郵送先') && check('2026-10-30','川口市','18:05').warning.includes('消印有効'), 'after-hours notices must distinguish official postal destination from unknown postmark acceptance');
assert.ok(primaryHtml.includes('窓口受付時間は9:00～16:30') && primaryHtml.includes('期限日必着か当日消印有効かは明記されていません'), 'crawlable primary notice must show hours without promising postal acceptance');

console.log('Seven selector and seven primary-alert Japan-time grant deadline cases passed');
