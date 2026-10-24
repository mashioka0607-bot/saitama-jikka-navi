// Regression for published Japan-time grant deadlines. No live budget claims.
const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const all = fs.readFileSync('static_pages/kaitai-check/grants.js', 'utf8');
const guard = all.slice(all.indexOf('/* Dynamic guard for 2026 municipal grant deadlines.'));
assert.ok(guard.startsWith('/* Dynamic guard'), 'Guard marker missing');

function check(today, city) {
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
  const IntlFake = { DateTimeFormat: class { format() { return today; } } };
  vm.runInNewContext(guard, { document, Intl: IntlFake, Date });
  assert.equal(typeof onChange, 'function');
  onChange();
  return { title: title.textContent, warning: notices.join(' ') };
}

const cases = [
  ['2026-10-22', '川口市', ''],
  ['2026-10-24', '川口市', '残り6日'],
  ['2026-10-30', '川口市', '残り0日'],
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
console.log('Seven Japan-time grant deadline cases passed');
