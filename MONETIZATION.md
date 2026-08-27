# Monetization runbook

Updated: 2026-08-27

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED 2026-08-27 from TownLife Affiliate's official recommended-program page: conversion point = free estimate request; payout = 10,000 JPY per approved result (11,000 JPY tax-inclusive display); approval rate approximately 85%; target includes Tokyo/Kanagawa/Saitama/Chiba plus Shizuoka/Aichi/Osaka/Kyoto/Hyogo/Hiroshima. The page notes payout can vary by acquisition method, so the logged-in dashboard remains authoritative for the exact account/tracking link.
   - TownLife's public series page exposes a diagnosis-version LP and chatbot/form assets.
   - This is the current first monetization test for `片付け費用が高い/払えない + 売却/残置物` traffic because the query bridges cleanup pain to a free property-disposition comparison.
   - Prepare the commercial-intent page before applying; do not insert a guessed tracking URL or imply partnership before approval.

2. Estate-clearance offers
   - Life Reset is publicly listed at 7,300 JPY (tax excluded) via TownLife Affiliate in current third-party ASP comparison data; still treat the logged-in dashboard as authoritative before implementation because cross-ASP pricing differs.
   - Use cleanup offers mainly on `遠方`, `見積`, `施設入居後`, `立会い不要` and similar cleanup-first intent.
   - Heart Service 13,200 JPY promotion was previously observed as ended. Do not plan around it unless a live ASP dashboard independently confirms a current equivalent.

## Conversion architecture

Prioritize request-stage intent rather than broad informational traffic:

- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: TownLife Empty Home Solution
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → empty-home CTA + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 「どこに頼む？」＋一般廃棄物の収集運搬確認 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA
- 施設入居後の実家片付け → cleanup CTA, then disposition CTA if home will become vacant
- 貴重品探索 / 買取相殺 → cleanup CTA

### Reuse-first cost reduction funnel (added 2026-08-27)

Kawagoe City's official bulky-waste page, updated 2026-06-03, explicitly recommends considering reuse before disposal and links residents to the `おいくら` bulk purchase-estimate service under the City's reuse partnership. The City also operates `つばさ館`, which accepts certain reusable clothing, miscellaneous goods, bags, tableware, ceramics and books; it does not accept PCs, appliances or large furniture through that reuse intake.

For readers whose core problem is `片付け費用が高い/払えない`, use a trust-first cost-minimization sequence before the property-disposition CTA:

1. Separate potentially saleable/reusable items first and obtain a reuse/buyback estimate where appropriate.
2. For items the owner can lawfully and safely handle, compare municipal collection/self-delivery options and their practical constraints.
3. Obtain cleanup-company estimates only for the remaining workload, comparing the same scope and total-cost conditions.
4. If the remaining cleanup cost is still disproportionate, or a sale/demolition deadline exists, compare disposing of the property with contents remaining before committing to full clearance.

This is an editorial decision framework, not a promise that reuse will generate meaningful proceeds. Do not imply `おいくら` is operated by Kawagoe City; describe it accurately as an external service the City links to under its reuse initiative. Do not turn the municipal link into an affiliate link unless a separately approved commercial relationship exists and is clearly disclosed.

### Trust-first disposition comparison

Do not make the high-intent sale page look like a disguised affiliate landing page. Kawagoe City has an official empty-home bank for owners/managers who want to sell or rent eligible vacant homes; the owner-facing page was updated 2026-06-08. On disposition-intent pages, present three legitimate paths before the commercial CTA:

1. ordinary private-market appraisal / brokerage or purchase consultation;
2. Kawagoe City's empty-home bank where the property/owner meets its requirements;
3. consultation about sale with remaining contents when cleanup cost or deadline makes pre-clearance impractical.

CRITICAL CURRENT-STATUS NOTE (verified 2026-08-27): Kawagoe City's buyer/tenant page says there are currently NO registered properties and it is not accepting utilization applications at present. The owner-facing page still accepts eligible property registration, subject to requirements (including no existing brokerage agreement). Therefore describe the bank as a municipal registration option for eligible owners, NOT as a currently stocked marketplace or an immediate buyer-finding route. Re-check this status before publishing time-sensitive availability claims.

Kawagoe City also has a newer official consultation route (verified 2026-08-27; city page updated 2026-06-08) under its cooperation agreement with the Saitama Real Estate Transaction Association, Western Saitama Branch. Owners, managers and heirs can seek generally free consultation from licensed real-estate professionals about inheritance, management, rental, sale and demolition. Use this as a neutral non-ad option on high-intent pages for readers who genuinely do not know whether to clean, sell, rent or demolish first. Do not imply that downstream brokerage, demolition or inheritance work is free; the city states those services can become paid under a separate contract.

This non-ad municipal option improves decision quality and trust. Link to the official Kawagoe City source rather than paraphrasing eligibility too aggressively. Do not imply the empty-home bank guarantees a buyer or is suitable for every property.

## Current SERP gap (verified 2026-08-27)

Broad `川越市 遺品整理` remains a poor first battlefield. Current local operators already emphasize free estimates, no-additional-fee promises, remote handling, valuables search, vacant-home contents and concrete room-size pricing. Do not publish another generic `おすすめ5選` clone.

The useful gap is not another price table; it is a **same-condition total-cost comparison**. On estimate/comparison content, require readers to compare: initial quoted total, what is excluded, conditions that trigger extra charges, cancellation fee, amount/room scope used for the quote, appliance-recycling treatment, valuables/hold-box handling, buyback credit, and who transports household waste under what lawful arrangement. This directly answers the uncertainty competitors leave after saying `追加料金なし`.

`片付け費用が払えない実家 + 売却/残置物` remains the highest-value bridge between cleanup and property disposition. Strengthen the existing high-intent page rather than spawning overlapping city-name pages.

When an offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- For `片付け費用が高い/払えない`, `退去・売却期限`, and `空き家家財撤去`, test two distinct decisions: `片付け見積を比較` vs `片付け前に空き家の解決方法を無料比較`.
- For TownLife Empty Home Solution, test its diagnosis-version LP against the standard request LP if the dashboard provides both tracking links.
- Keep lower-intent pages informational and route internally to high-intent decision pages.
- Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.
- Do not claim an advertiser is a 川越市許可業者 unless verified from the municipality's current list.
- Keep PR/ad disclosure adjacent to commercial links and avoid unsupported superiority claims.

### TownLife approval gate — do this before applying

TownLife's official promotion instructions currently state that site publishers must first create at least one page relevant to the advertised service, then apply for media/program partnership. Their review checks whether the media content matches the ad, whether PR activity is disclosed, and whether the page avoids excessive or disparaging claims; the stated review target is within about 3 business days.

Therefore, before applying for `タウンライフ空き家解決`:

1. Use `/kawagoe-shi/katazuke-hiyou-urenai/` as the planned placement page.
2. Keep an explicit PR disclosure visible before/near the future commercial CTA.
3. Keep the municipal consultation/empty-home-bank/reuse alternatives visible so the page is not a disguised affiliate-only landing page.
4. Apply in the TownLife dashboard only after the disclosure is live.
5. After approval, insert only the issued tracking URL; never guess or hard-code a non-issued affiliate URL.

## Legal / trust rule for Kawagoe

Kawagoe's current official waste guidance states that household-waste collection requires municipal authorization; industrial-waste, secondhand-dealer, or another municipality's authorization is not enough to collect Kawagoe household waste. For cleanup/estate-clearance content, ask users to confirm who actually transports disposal items and under what permit/contract arrangement. This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

Kawagoe's self-delivery guidance also matters operationally: self-delivery is principally limited to the person who generated the household waste, unloading is generally done by the person bringing it, and identification may be requested. Do not present self-delivery as an effortless substitute for professional clearance, especially for remote heirs or large/heavy contents.

## Search / indexing status

- Public Google `site:` checks are not authoritative enough to treat as an indexing source of truth. Search Console URL Inspection / Pages report is the source of truth.
- Do not spend another cycle debugging sitemap submission unless Search Console reports a crawl/discovery problem.
- Next Search Console checks: query-level impressions, indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`, and CTR/title performance.
- Specifically watch for `買取`, `リユース`, `処分費用`, `片付け費用`, `残置物`, `売却`, `解体` modifiers before creating a separate reuse article. If impressions emerge, strengthen the existing page first.
- Next URL-inspection priority after the homepage: `/kawagoe-shi/katazuke-hiyou-urenai/`, because it maps to the strongest commercial-intent bridge.
- Use URL inspection requests selectively rather than bulk submission.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
