// Regression for published Japan-time grant deadlines. No live budget claims.
// Eligibility and amount in the Kawaguchi selector must not become a generic grant promise.

const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const all = fs.readFileSync('static_pages/kaitai-check/grants.js', 'utf8');
const kawaguchi = all.split('\n').find(line => line.startsWith("['川口市'"));
assert.ok(kawaguchi && kawaguchi.includes('地方税完納') && kawaguchi.includes('事例紹介') && kawaguchi.includes('上限100万円') && kawaguchi.includes('満額支給とは限らない'), 'Kawaguchi official eligibility and payout caveat missing');
assert.ok(kawaguchi.includes('完了報告 2027-01-29'), 'Kawaguchi post-demolition report deadline missing from published selector');
assert.ok(kawaguchi.includes('2026年度受付終了') && kawaguchi.includes('2026-11-02') && kawaguchi.includes('当初の交付申請期限') && !kawaguchi.includes('公表期限内・対象限定'), 'Kawaguchi selector must show official closure rather than remaining deadline');
const kuki = all.split('\n').find(line => line.startsWith("['久喜市'"));
assert.ok(kuki && kuki.includes('2026-11-30') && kuki.includes('上限30万円') &&
  kuki.includes('事前診断') && kuki.includes('2026-12-31') &&
  kuki.includes('即時売却') && kuki.includes('市街化調整区域'), 'Kuki primary-source subsidy precheck missing');
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
  ['2026-11-22', '久喜市', ''],
  ['2026-11-24', '久喜市', '残り6日'],
  ['2026-11-30', '久喜市', '本日'],
  ['2026-12-01', '久喜市', '公表期限'],
  ['2026-11-02', '川口市', '受付終了'],
  ['2026-11-05', '川口市', '受付終了'],
  ['2026-11-06', '川口市', '受付終了'],
  ['2026-11-12', '川口市', '受付終了'],
  ['2026-11-13', '川口市', '受付終了'],
  ['2026-11-14', '川口市', '受付終了'],
  ['2027-04-01', '川口市', '過年度情報']
];
for (const [date, city, expected] of cases) {
  const outcome = check(date, city);
  if (expected) assert.ok(outcome.warning.includes(expected), date + ' / ' + city + ': ' + JSON.stringify(outcome));
  else assert.equal(outcome.warning, '', date + ' / ' + city);
}

for (const date of ['2026-11-02', '2026-11-06', '2026-11-12', '2026-11-13']) {
  const warning = check(date, '川口市');
  assert.ok(warning.warning.includes('11月13日は当初の交付申請期限') &&
    warning.warning.includes('受付中という意味ではありません'),
    'closed grant must not count down to obsolete application deadline: ' + JSON.stringify(warning));
  assert.ok(warning.title.includes('2026年度受付終了'), 'closure must be prominent: ' + date);
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
  ['2026-11-02','受付終了',true],
  ['2026-11-05','受付終了',true],
  ['2026-11-06','受付終了',true],
  ['2026-11-12','受付終了',true],
  ['2026-11-13','受付終了',true],
  ['2026-11-14','受付終了',true],
  ['2027-04-01','過年度情報',true]
]) {
  const note=checkPrimary(today);
  assert.equal(!note.hidden, visible, 'primary alert visibility on '+today);
  if(expected)assert.ok(note.textContent.includes(expected), 'primary alert text on '+today+': '+note.textContent);
}

for (const [time, expected] of [['16:30', '9:00～16:30'], ['16:31', '窓口受付'], ['17:15', '電話の公表受付時間'], ['17:16', 'ともに終了'], ['18:05', 'ともに終了']]) {
  const afterHours = checkPrimary('2026-10-30', time);
  assert.ok(afterHours.textContent.includes(expected), 'primary '+time+': '+afterHours.textContent);
}

for (const time of ['16:31', '17:16']) {
  const closed = checkPrimary('2026-11-13', time);
  assert.ok(closed.textContent.includes('受付終了') && closed.textContent.includes('当初の交付申請期限'),
    'published closure overrides deadline-day office hours: '+time);
}
assert.ok(checkPrimary('2026-11-14').textContent.includes('受付終了'),
  'current-year notice must clearly show closure');
assert.ok(checkPrimary('2027-04-01').textContent.includes('過年度'),
  'FY2026 should only be called past-year information from April 2027');
const dayPrimary = checkPrimary('2026-10-30');
assert.ok(dayPrimary.textContent.includes('9:00～16:30') && dayPrimary.textContent.includes('8:30～17:15') && dayPrimary.textContent.includes('048-229-7805'), 'primary deadline warning must show official contact hours');
assert.ok(checkPrimary('2026-10-30','18:05').textContent.includes('郵送先') && check('2026-10-30','川口市','18:05').warning.includes('消印有効'), 'after-hours notices must distinguish official postal destination from unknown postmark acceptance');
assert.ok(primaryHtml.includes('川口市：2026年11月2日更新') && primaryHtml.includes('2026年度の新規受付が続いている意味ではありません'), 'crawlable primary alert must show FY2026 closure');

console.log('Japan-time grant closure and historical deadline regression cases passed');
