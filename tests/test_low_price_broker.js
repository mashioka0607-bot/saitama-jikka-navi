'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

// Run the same browser calculator logic shipped to visitors, not a parallel fee formula.
const html = fs.readFileSync('static_pages/tedori-hikaku/index.html', 'utf8');
const scripts = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].map(match => match[1]);
const calculator = scripts.find(source => source.includes('net_proceeds_compare'));
assert.ok(calculator, 'comparison script is missing');
assert.match(calculator, /lowPriceFeeScenario/, 'low-price fee scenario is missing');

function compare({sale=300, broker=15.4, buy=275}={}) {
  const fields = {sale, clear:0, reuse:0, repair:0, demolition:0,
    demolitionSubsidy:0, clearSubsidy:0, broker, months:0,
    buy, buycost:0, buymonths:0, monthly:0};
  let onSubmit;
  const output = {innerHTML:'', style:{}, scrollIntoView() {}};
  const document = {
    getElementById(id) {
      if (id === 'calc') return {addEventListener(type, listener) {
        assert.equal(type, 'submit'); onSubmit = listener;
      }};
      if (id === 'r') return output;
      assert.ok(Object.hasOwn(fields, id), 'unexpected calculator field ' + id);
      return {value: fields[id]};
    }
  };
  vm.runInNewContext(calculator, {document, window:{}});
  assert.equal(typeof onSubmit, 'function');
  onSubmit({preventDefault() {}});
  return output.innerHTML;
}

const lower = compare();
assert.match(lower, /片付け＋仲介：約284\.6万円/);
assert.match(lower, /税込33万円で事前に合意/);
assert.match(lower, /約267万円/);
assert.match(lower, /約17\.6万円減/);
assert.match(lower, /比較結果が逆転/);
assert.match(lower, /国交省の公式説明/);

// Do not silently overwrite user-entered actual brokerage fees.
assert.doesNotMatch(compare({broker:33}), /low-price-fee-scenario/);
assert.match(compare({broker:35}), /特例上限（税込33万円）を超えています/);
// The special ceiling applies only to sale prices <= 8 million yen.
assert.doesNotMatch(compare({sale:801, broker:33}), /low-price-fee-scenario/);
assert.doesNotMatch(compare({sale:0, broker:0, buy:0}), /low-price-fee-scenario/);
console.log('Brokerage fee special-case guard passed: 300/800 threshold, 33 limit, no silent override.');
