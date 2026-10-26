'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

// Run the shipped script from the actual deploy artifact.
const html = fs.readFileSync('dist/tedori-hikaku/index.html', 'utf8');
const match = html.match(/<script id="tedori-comparison-freshness-v1">([\s\S]*?)<\/script>/);
assert.ok(match, 'stale-comparison guard is missing from published artifact');

function runFixture({estimateText='<h2>片付け＋仲介 2,000万円</h2>', quotesText='<h3>実質受取額順</h3>', offerOwner='r'}={}) {
  const handlers = {};
  const results = {};
  function output(text) {
    return {
      innerHTML: text,
      style: {display:'block'},
      querySelector() { return /<h[23]\b|<ol\b/i.test(this.innerHTML) ? {} : null; },
      contains(node) { return node.owner===this; }
    };
  }
  results.r = output(estimateText);
  results['quote-result'] = output(quotesText);
  const offer = {hidden:false, owner:results[offerOwner]};
  const form = name => ({addEventListener(type, cb) {
    assert.equal(type, 'input');
    handlers[name] = cb;
  }});
  const fields = {
    calc:form('calc'),
    'quote-compare':form('quote-compare'),
    r:results.r,
    'quote-result':results['quote-result'],
    'tedori-affiliate-next':offer
  };
  vm.runInNewContext(match[1], {document:{getElementById:id=>fields[id]||null}});
  assert.equal(typeof handlers.calc, 'function');
  assert.equal(typeof handlers['quote-compare'], 'function');
  return {handlers, results, offer};
}

{
  const f=runFixture();
  f.handlers.calc();
  assert.match(f.results.r.innerHTML, /再計算してください/);
  assert.doesNotMatch(f.results.r.innerHTML, /2,000万円/);
  assert.equal(f.offer.hidden, true, 'stale commercial CTA must be hidden');
  assert.match(f.results['quote-result'].innerHTML, /実質受取額順/, 'independent quote result must remain');
}
{
  const f=runFixture({offerOwner:'quote-result'});
  f.handlers['quote-compare']();
  assert.match(f.results['quote-result'].innerHTML, /再計算してください/);
  assert.equal(f.offer.hidden, true, 'stale quote CTA must be hidden');
  assert.match(f.results.r.innerHTML, /2,000万円/, 'independent estimate result must remain');
}
{
  const f=runFixture({estimateText:'',quotesText:'<p>仲介手数料を入力してください</p>'});
  f.handlers.calc();
  f.handlers['quote-compare']();
  assert.equal(f.results.r.innerHTML, '');
  assert.match(f.results['quote-result'].innerHTML, /仲介手数料を入力してください/);
}
{
  const f=runFixture({offerOwner:'quote-result'});
  f.handlers.calc();
  assert.equal(f.offer.hidden, false, 'editing a different form must preserve a valid CTA');
}
console.log('Stale calculation guard passed: 2 modes, no pre-result reset, CTA context isolation.');
