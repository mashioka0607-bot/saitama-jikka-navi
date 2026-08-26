# Monetization runbook

Updated: 2026-08-27

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED 2026-08-27 from TownLife Affiliate's official recommended-program page: conversion point = free estimate request; payout = 10,000 JPY per approved result (11,000 JPY tax-inclusive display); approval rate approximately 85%; target includes Tokyo/Kanagawa/Saitama/Chiba plus Shizuoka/Aichi/Osaka/Kyoto/Hyogo/Hiroshima. The page notes payout can vary by acquisition method, so the logged-in dashboard remains authoritative for the exact account/tracking link.
   - TownLife's public series page exposes a diagnosis-version LP and chatbot/form assets.
   - This is the current first monetization test for `片付け費用が高い/払えない + 売却/残置物` traffic because the query bridges cleanup pain to a free property-disposition comparison.
   - Prepare the commercial-intent page before applying; do not insert a guessed tracking URL or imply partnership before approval.

2. Estate-clearance offers
   - Life Reset public comparison data has shown conflicting values by ASP/source; therefore dashboard terms are authoritative before implementation.
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

### Trust-first disposition comparison

Do not make the high-intent sale page look like a disguised affiliate landing page. Kawagoe City has an official empty-home bank for owners/managers who want to sell or rent eligible vacant homes; the owner-facing page was updated 2026-06-08. On disposition-intent pages, present three legitimate paths before the commercial CTA:

1. ordinary private-market appraisal / brokerage or purchase consultation;
2. Kawagoe City's empty-home bank where the property/owner meets its requirements;
3. consultation about sale with remaining contents when cleanup cost or deadline makes pre-clearance impractical.

CRITICAL CURRENT-STATUS NOTE (verified 2026-08-27): Kawagoe City's buyer/tenant page says there are currently NO registered properties and it is not accepting utilization applications at present. The owner-facing page still accepts eligible property registration, subject to requirements (including no existing brokerage agreement). Therefore describe the bank as a municipal registration option for eligible owners, NOT as a currently stocked marketplace or an immediate buyer-finding route. Re-check this status before publishing time-sensitive availability claims.

This non-ad municipal option improves decision quality and trust. Link to the official Kawagoe City source rather than paraphrasing eligibility too aggressively. Do not imply the empty-home bank guarantees a buyer or is suitable for every property.

SERP note (2026-08-27): broad `川越市 遺品整理` remains a poor first battlefield. Current local operators already emphasize no-additional-fee estimates, vacant-home contents, valuables, remote/photo reporting and related features. Do not publish another generic `おすすめ5選` clone.

SERP note (2026-08-27): `片付け費用が払えない実家 + 売却/残置物` remains explicitly commercial in Kawagoe. A local real-estate article dated 2026-04-03 directly targets inability to pay cleanup costs and sale with contents remaining. Continue treating this as the highest-value bridge between cleanup and property disposition.

When an offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- For `片付け費用が高い/払えない`, `退去・売却期限`, and `空き家家財撤去`, test two distinct decisions: `片付け見積を比較` vs `片付け前に空き家の解決方法を無料比較`.
- For TownLife Empty Home Solution, test its diagnosis-version LP against the standard request LP if the dashboard provides both tracking links.
- Keep lower-intent pages informational and route internally to high-intent decision pages.
- Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.
- Do not claim an advertiser is a 川越市許可業者 unless verified from the municipality's current list.
- Keep PR/ad disclosure adjacent to commercial links and avoid unsupported superiority claims.

## Legal / trust rule for Kawagoe

Kawagoe's current official waste-carrier list was updated 2026-04-06. It shows 14 permit holders in the `引越` category for household waste temporarily generated in large quantities. Kawagoe's FY2026 waste plan says temporary large-volume household waste should be self-delivered to city facilities or entrusted to designated Kawagoe general-waste collection/transport permit holders (with a limited fallback for unavoidable cases). For cleanup/estate-clearance content, ask users to confirm who actually transports disposal items and under what permit/contract arrangement. This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

## Search / indexing status

- Public Google `site:` checks are not authoritative enough to treat as an indexing source of truth. Search Console URL Inspection / Pages report is the source of truth.
- Do not spend another cycle debugging sitemap submission unless Search Console reports a crawl/discovery problem.
- Next Search Console checks: query-level impressions, indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`, and CTR/title performance.
- Next URL-inspection priority after the homepage: `/kawagoe-shi/katazuke-hiyou-urenai/`, because it maps to the strongest commercial-intent bridge.
- Use URL inspection requests selectively rather than bulk submission.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
