# Monetization runbook

Updated: 2026-08-29

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED 2026-08-27 from TownLife Affiliate's official recommended-program page: conversion point = free estimate request; payout = 10,000 JPY per approved result (11,000 JPY tax-inclusive display); approval rate approximately 85%; target includes Tokyo/Kanagawa/Saitama/Chiba plus Shizuoka/Aichi/Osaka/Kyoto/Hyogo/Hiroshima. The page notes payout can vary by acquisition method, so the logged-in dashboard remains authoritative for the exact account/tracking link.
   - This remains the first monetization test for `片付け費用が高い/払えない + 売却/残置物` traffic.
   - Do not insert a guessed tracking URL or imply partnership before approval.

2. Estate-clearance offers
   - Use cleanup offers mainly on `遠方`, `見積`, `施設入居後`, `立会い不要` and similar cleanup-first intent.
   - Treat the logged-in ASP dashboard as authoritative for current payout/approval terms before implementation.

## Conversion architecture

Prioritize request-stage intent rather than broad informational traffic:

- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: TownLife Empty Home Solution
- `片付けずに売却 / 残置物あり売却 / 実家そのまま売却` → PRIMARY: disposition comparison before full clearance
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → empty-home CTA + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA

## NEW 2026-08-29 — unsellable inherited land / final-exit intent

Kawagoe City updated its official `所有者不明土地の発生予防` guidance on 2026-07-21 and explicitly points heirs to the national `相続土地国庫帰属制度`. Saitama Legal Affairs Bureau confirms the system is available for inherited land, with consultation by reservation and a standard processing period of about 8 months. The Ministry of Justice states that approval requires the land not to fall within statutory rejection/non-approval categories and that an approved owner must pay a management-cost contribution before ownership transfers to the state.

Important editorial boundary: this is a **land** exit route, not a shortcut for handing an intact vacant house to the state. Ministry of Justice eligibility rules include land with a building among the rejection categories. Therefore do not tell a reader with an inherited house to demolish merely to qualify; demolition cost, tax consequences, sale-with-building/contents, brokerage/purchase, municipal consultation and management options must be compared first.

Commercial implication: this creates a useful bottom-of-funnel branch for queries such as `相続した土地 売れない`, `実家 売れない 手放したい`, `空き家 売れない どうする`, `相続土地 処分`, and `負動産 手放す`. The affiliate CTA should still come **before** the national-surrender route for a house/lot that may have market value: first test whether it can be sold or otherwise resolved commercially; only then explain the national system as a constrained fallback for eligible inherited land. This strengthens trust without cannibalizing the primary empty-home offer.

Do not create a standalone page yet. First watch Search Console for impressions containing `売れない`, `手放したい`, `処分`, `国庫帰属`, `負動産`. If those modifiers appear on the existing high-intent page, add a compact `売れない場合の最終ルート` section there. A dedicated article is justified only after query evidence or clear ranking opportunity appears.

## Current SERP direction

Current competitors increasingly lead with `現状買取`, `残置物あり`, `片付け前に相談/査定`, while broader inherited-home consultation competitors lead with situation diagnosis rather than generic contractor rankings. Continue to avoid generic `川越市 遺品整理おすすめN選` content.

The useful gap remains a decision framework: before paying full clearance cost, compare reuse/buyback, municipal disposal where practical, cleanup quotes on identical scope, sale with contents/building, rent/manage, demolition only after cost/tax checks, and—only for eligible inherited land that truly cannot be resolved otherwise—the national land-surrender system.

## Trust-first disposition comparison

Do not make the high-intent sale page look like a disguised affiliate landing page. Keep legitimate non-ad routes visible: Kawagoe City's professional empty-home consultation route, eligible-owner empty-home-bank registration, management options, and official tax guidance. The municipal consultation route covers inheritance, management, rental, sale and demolition; downstream paid work is a separate contract.

For inherited vacant homes, check the `被相続人の居住用財産（空き家）の3,000万円特別控除` conditions before casually recommending rental. Do not present `とりあえず貸す` as neutral because use after inheritance can affect eligibility.

## Reuse-first cost reduction funnel

For readers whose core problem is `片付け費用が高い/払えない`:

1. Separate important documents/valuables and potentially reusable items.
2. Compare reuse/buyback before disposal where appropriate.
3. Use municipal collection/self-delivery only where lawful and practical.
4. Compare cleanup companies on the same scope, including extra-charge conditions and lawful household-waste transport arrangements.
5. If cleanup remains disproportionate or a sale deadline exists, compare disposition with contents remaining before committing to full clearance.

## TownLife approval gate

Before applying/implementing:

1. Use `/kawagoe-shi/katazuke-hiyou-urenai/` as the planned placement page.
2. Keep explicit PR disclosure visible near future commercial CTA.
3. Keep municipal/non-ad alternatives visible.
4. After approval, insert only the issued tracking URL; never guess it.
5. Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.

## Legal / trust rule for Kawagoe

Kawagoe's official waste guidance states that household-waste collection requires the appropriate municipal authorization. For cleanup content, ask who actually transports disposal items and under what permit/contract arrangement. Do not imply every cleanup company itself must hold the permit if it lawfully coordinates with an authorized carrier.

## Search / indexing status

- Public Google `site:` checks are not authoritative enough to treat as indexing truth. Search Console URL Inspection / Pages report is the source of truth.
- Next Search Console checks: query-level impressions; indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`; CTR/title performance.
- Priority modifiers now include: `片付け費用`, `残置物`, `売却`, `片付けずに売却`, `そのまま売却`, `解体`, `管理`, `貸す`, `売るか貸すか`, plus NEW `売れない`, `手放したい`, `処分`, `国庫帰属`, `負動産`.
- Strengthen the existing high-intent page before creating overlapping pages when impressions emerge.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
