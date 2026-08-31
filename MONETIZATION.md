# Monetization runbook

Updated: 2026-08-31

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED 2026-08-27 from TownLife Affiliate's official recommended-program page: conversion point = free estimate request; payout = 10,000 JPY per approved result (11,000 JPY tax-inclusive display); approval rate approximately 85%. Logged-in dashboard remains authoritative for exact account terms/tracking URL.
   - First monetization test: `片付け費用が高い/払えない + 売却/残置物` traffic.
   - Never insert a guessed tracking URL or imply partnership before approval.

2. Estate-clearance offers
   - Use mainly on cleanup-first intent such as `遠方`, `見積`, `施設入居後`, `立会い不要`.
   - Logged-in ASP dashboard is authoritative for current payout/approval terms.

## Conversion architecture

- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: empty-home/disposition comparison
- `片付けずに売却 / 残置物あり売却 / 実家そのまま売却` → PRIMARY: disposition comparison before full clearance
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → empty-home CTA + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA

## Disposition-first rule for expensive cleanup

For `片付け費用が高い/払えない`, full clearance is not the default prerequisite for valuation or disposition.

1. Secure important documents, valuables, memorial items, and anything the family must retain.
2. Before paying for full clearance, check whether the home can be valued and whether sale, purchase, rental, management, or another route is realistic with contents remaining.
3. Confirm ownership/inheritance constraints and relevant official/local consultation routes before signing irreversible work.
4. Once the likely disposition is known, separate reusable/buyback items and use municipal disposal where lawful/practical for items that actually need removal.
5. Use cleanup-company comparison only for the remaining necessary scope; compare identical scope, extra-charge conditions, and lawful household-waste transport arrangements.

Fresh 2026 SERPs increasingly state that valuation can begin before full clearance and some purchase routes accept contents remaining. Kawagoe City's 2026-06-08 consultation framework likewise covers inheritance, management, rental, sale and demolition rather than assuming cleanup first.

CTA principle after an approved tracking URL exists: `片付け費用を決める前に、家財が残った状態で取れる選択肢を確認`. Do not claim the affiliate service guarantees purchase, contents acceptance, or no-clearance sale.

## Current SERP direction

Competitors increasingly lead with `現状買取`, `残置物あり`, `片付け前に相談/査定`. Avoid generic `川越市 遺品整理おすすめN選` and broad `実家じまい` content hubs.

The useful gap is a decision framework immediately before spending money: compare disposition with contents remaining, reuse/buyback, municipal disposal where practical, cleanup quotes on identical scope, rent/manage, and demolition only after cost/tax checks.

## Trust-first comparison

Keep legitimate non-ad routes visible beside future affiliate CTAs: Kawagoe City's professional empty-home consultation, eligible empty-home-bank registration, management options, and official tax/legal guidance. Do not make the page look like a disguised affiliate landing page.

For inherited vacant homes, check the `被相続人の居住用財産（空き家）の3,000万円特別控除` conditions before casually recommending rental.

## TownLife approval gate

1. Planned placement page: `/kawagoe-shi/katazuke-hiyou-urenai/`.
2. Keep explicit PR disclosure near future commercial CTA.
3. Keep municipal/non-ad alternatives visible.
4. After approval, insert only the issued tracking URL.
5. Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.

## Legal / trust rule for Kawagoe

For cleanup content, verify who transports household waste and under what permit/contract arrangement. Do not imply every cleanup company itself must hold the municipal collection permit if it lawfully coordinates with an authorized carrier.

## Search / indexing status

Search Console URL Inspection / Pages report is the indexing source of truth; public `site:` checks are only supplementary.

Next GSC checks:
- indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`
- query-level impressions and CTR/title performance
- modifiers: `片付け前`, `残置物`, `家財そのまま`, `家財ごと`, `片付け不要`, `売却`, `買取`, `片付け費用 払えない`, `遠方 実家 売却`

If impressions overlap the existing high-intent page, optimize it before creating another page.

## Scaling rule

Do not mass-produce thin city pages. A new location or intent page needs distinct official rules/data, distinct SERP intent, and a plausible monetization path. Until the first commercial page gets meaningful impressions/clicks and the affiliate tracking URL is live, improving decision quality and conversion architecture outranks page count.