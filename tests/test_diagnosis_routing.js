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

console.log('Diagnosis routing passed: undecided/registration/cleanup/sale/keep + ownership unverified cases.');
