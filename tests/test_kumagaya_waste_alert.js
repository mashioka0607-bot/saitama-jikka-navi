'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const html = fs.readFileSync('dist/faq/index.html', 'utf8');
assert.match(html, /id="kumagaya-waste-bulletin-202611" hidden/);
assert.match(html, /https:\/\/www\.city\.kumagaya\.lg\.jp\/kurashi\/kankyo\/gomirecycle\/hannyuteishi\.html/);
assert.match(html, /https:\/\/www\.city\.kumagaya\.lg\.jp\/kurashi\/kankyo\/gomirecycle\/oosatokouikihasaiki\.html/);
const match = html.match(/<script id="kumagaya-waste-bulletin-date-guard">([\s\S]*?)<\/script>/);
assert.ok(match, 'Japan-date expiry guard should be present');

function flags(atUtc) {
  const elements = {
    'kumagaya-waste-bulletin-202611': { hidden: true },
    'kumagaya-crusher-bulletin-202611': { hidden: false },
  };
  const fixed = new Date(atUtc);
  class FakeDate extends Date {
    constructor(...args) { super(...(args.length ? args : [fixed])); }
  }
  vm.runInNewContext(match[1], {
    Intl,
    Date: FakeDate,
    document: { getElementById(id) { return elements[id]; } },
  });
  return elements;
}

// Date boundaries use Japan calendar date, including after UTC midnight.
assert.equal(flags('2026-11-08T14:59:00Z')['kumagaya-waste-bulletin-202611'].hidden, true);
assert.equal(flags('2026-11-08T15:01:00Z')['kumagaya-waste-bulletin-202611'].hidden, false);
assert.equal(flags('2026-11-20T12:00:00Z')['kumagaya-crusher-bulletin-202611'].hidden, false);
assert.equal(flags('2026-11-24T00:00:00Z')['kumagaya-crusher-bulletin-202611'].hidden, true);
assert.equal(flags('2026-12-15T13:00:00Z')['kumagaya-waste-bulletin-202611'].hidden, false);
assert.equal(flags('2026-12-15T15:01:00Z')['kumagaya-waste-bulletin-202611'].hidden, true);
console.log('Kumagaya municipal waste alert: Japan-time display and expiration passed');
