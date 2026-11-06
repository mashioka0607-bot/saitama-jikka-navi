'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync('static_pages/shindan/index.html', 'utf8');
const match = html.match(/<script>([\s\S]*?)<\/script>/);
assert.ok(match, 'diagnosis script missing');

function diagnose({state='empty', exit='unknown', registration='unknown', distance='yes', deadline='no'} = {}) {
  const values = {state, exit, registration, distance, deadline};
  let onSubmit;
  const result = {innerHTML:'', style:{}, scrollIntoView(){}};
  const document = {
    getElementById(id) {
      if (id === 'diag') return {addEventListener(type, handler) {
        assert.equal(type, 'submit'); onSubmit = handler;
      }};
      if (id === 'r') return result;
      assert.ok(Object.hasOwn(values,id), 'unexpected form field '+id);
      return {value: values[id]};
    },
    querySelector() { return null; }
  };
  const calls = [];
  vm.runInNewContext(match[1], {document, gtag:(...args)=>calls.push(args)});
  assert.equal(typeof onSubmit,'function');
  onSubmit({preventDefault(){}});
  const completed = calls.find(call=>call[1]==='diagnosis_complete');
  assert.ok(completed, 'diagnosis completion event missing');
  return {html:result.innerHTML, route:completed[2].route};
}

const undecided = diagnose({state:'inherited',exit:'unknown',registration:'done'});
assert.equal(undecided.route, 'inheritance_undecided');
assert.match(undecided.html, /無料相談/);
assert.match(undecided.html, /空き家バンク/);
assert.doesNotMatch(undecided.html, /href="\/tedori-hikaku\/"/);

const notRegistered = diagnose({state:'inherited',exit:'unknown',registration:'notdone'});
assert.equal(notRegistered.route, 'inheritance_registration');
assert.match(notRegistered.html, /法務省/);
assert.match(notRegistered.html, /無料相談/);
assert.doesNotMatch(notRegistered.html, /href="\/tedori-hikaku\/"/);

const cleanupOnly = diagnose({state:'inherited',exit:'clear',registration:'notdone'});
assert.equal(cleanupOnly.route, 'inheritance_registration');
assert.doesNotMatch(cleanupOnly.html, /href="\/tedori-hikaku\/"/);

const selling = diagnose({state:'inherited',exit:'sell',registration:'done'});
assert.equal(selling.route, 'sell_tedori');
assert.match(selling.html, /href="\/tedori-hikaku\/"/);

const sellingPendingRegistration = diagnose({state:'inherited',exit:'sell',registration:'notdone'});
assert.equal(sellingPendingRegistration.route, 'inheritance_registration');
assert.match(sellingPendingRegistration.html, /href="\/tedori-hikaku\/"/);

const keeping = diagnose({state:'inherited',exit:'keep',registration:'done'});
assert.equal(keeping.route, 'keep_prefecture');
assert.doesNotMatch(keeping.html, /href="\/tedori-hikaku\/"/);
const sellingUrgent = diagnose({state:'inherited', exit:'sell', registration:'done', deadline:'yes'});
assert.equal(sellingUrgent.route, 'sell_tedori');
assert.match(sellingUrgent.html, /期限優先の確認/);
assert.match(sellingUrgent.html, /追加料金・解約料/);
const sellingNotUrgent = diagnose({state:'inherited', exit:'sell', registration:'done', deadline:'no'});
assert.doesNotMatch(sellingNotUrgent.html, /期限優先の確認/);
const cleanupUrgent = diagnose({state:'empty', exit:'clear', deadline:'yes'});
assert.equal(cleanupUrgent.route, 'clear_prefecture');
assert.match(cleanupUrgent.html, /期限優先の確認/);
const registrationUrgent = diagnose({state:'inherited', exit:'sell', registration:'notdone', deadline:'yes'});
assert.equal(registrationUrgent.route, 'inheritance_registration');
assert.match(registrationUrgent.html, /権限を確認/);
const inheritedUnverifiedSale = diagnose({state:'inherited',exit:'sell',registration:'unknown'});
assert.equal(inheritedUnverifiedSale.route, 'ownership_unverified');
assert.match(inheritedUnverifiedSale.html, /登記名義/);
assert.match(inheritedUnverifiedSale.html, /司法書士/);
assert.doesNotMatch(inheritedUnverifiedSale.html, /href="\/tedori-hikaku\/"/);

const inheritedUnverifiedCleanup = diagnose({state:'inherited',exit:'clear',registration:'unknown'});
assert.equal(inheritedUnverifiedCleanup.route, 'ownership_unverified');
assert.doesNotMatch(inheritedUnverifiedCleanup.html, /href="\/tedori-hikaku\/"/);

const inheritedInconsistentRegistration = diagnose({state:'inherited',exit:'sell',registration:'na'});
assert.equal(inheritedInconsistentRegistration.route, 'ownership_unverified');

const nonInheritedUnverifiedSale = diagnose({state:'empty',exit:'sell',registration:'unknown'});
assert.equal(nonInheritedUnverifiedSale.route, 'ownership_unverified');

const nonInheritedCleanup = diagnose({state:'empty',exit:'clear',registration:'unknown'});
assert.equal(nonInheritedCleanup.route, 'clear_prefecture');
assert.match(nonInheritedCleanup.html, /一般廃棄物|家庭ごみ/);
assert.match(nonInheritedCleanup.html, /古物商や産業廃棄物収集運搬業/);
assert.match(nonInheritedCleanup.html, /https:\/\/www\.pref\.saitama\.lg\.jp\/b0304\/shohisoudan\/jirei\/sumai\/20200625\.html/);
assert.ok(html.includes('id="saitama-clearance-permit-check"'), 'statewide permit guidance should be crawlable HTML');
assert.ok(html.includes('一般廃棄物収集運搬業'), 'municipal licensing requirement missing');
assert.ok(html.includes('追加料金'), 'cost-disclosure checklist missing');

console.log('Diagnosis routing passed: undecided/registration/cleanup/sale/keep + ownership unverified cases.');


// Both city-event banners must stop prompting for applications after the
// published cutoff, and disappear after the event (Japan local date).
function consultationAt(pageHtml, sectionId, applyThrough, eventThrough, date) {
  const open = pageHtml.match(new RegExp('<section[^>]*id="' + sectionId + '"[^>]*>'));
  assert.ok(open, 'published event section missing: ' + sectionId);
  assert.ok(open[0].includes('data-consultation-application-through="' + applyThrough + '"'));
  assert.ok(open[0].includes('data-consultation-event-through="' + eventThrough + '"'));
  const eventBody = pageHtml.slice(pageHtml.indexOf(open[0]), pageHtml.indexOf('</section>', pageHtml.indexOf(open[0])));
  assert.ok(eventBody.includes('data-consultation-application-closed hidden'), 'closed-state fallback missing');
  const guard = pageHtml.split('<script id="municipal-consultation-deadline-guard">')[1]?.split('</script>')[0];
  assert.ok(guard, 'date guard missing');
  const note = {hidden:true};
  const section = {
    hidden:false,
    dataset:{consultationApplicationThrough:applyThrough, consultationEventThrough:eventThrough},
    querySelector:selector => selector === '[data-consultation-application-closed]' ? note : null
  };
  const doc = {querySelectorAll:selector => {
    assert.equal(selector, '[data-consultation-event-through]');
    return [section];
  }};
  const fakeIntl = {DateTimeFormat:class {
    constructor(locale, opts) {assert.equal(opts.timeZone, 'Asia/Tokyo');}
    format() {return date;}
  }};
  vm.runInNewContext(guard, {document:doc, Intl:fakeIntl, Date});
  return {hidden:section.hidden, deadlineNoticeVisible:!note.hidden};
}
const priceHtml = fs.readFileSync('static_pages/tedori-hikaku/index.html','utf8');
const diagnosisHtml = fs.readFileSync('static_pages/shindan/index.html','utf8');
for (const [page, id, cutoff, event, cases] of [
  [priceHtml, 'saitama-price-consult-20261124','2026-11-13','2026-11-24', [
    ['2026-11-07',false,false],['2026-11-13',false,false],
    ['2026-11-14',false,true],['2026-11-24',false,true],['2026-11-25',true,false]
  ]],
  [diagnosisHtml, 'saitama-nov2026-free-consult','2026-11-27','2026-11-28', [
    ['2026-11-07',false,false],['2026-11-27',false,false],
    ['2026-11-28',false,true],['2026-11-29',true,false]
  ]]
]) {
  for (const [day, hidden, notice] of cases) {
    const outcome = consultationAt(page,id,cutoff,event,day);
    assert.equal(outcome.hidden,hidden,id+': visibility on '+day);
    assert.equal(outcome.deadlineNoticeVisible,notice,id+': cutoff notice on '+day);
  }
}
console.log('Japan-time municipal consultation application and event expiry passed.');
