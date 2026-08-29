# Monetization runbook

Updated: 2026-08-30

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

## NEW 2026-08-30 — local freshness opportunity: Sep 27 empty-home/inheritance event

Kawagoe City published an official `空き家・相続もんだい解決フェスタ` for 2026-09-27 at Wakaba Walk. The agenda directly overlaps this site's decision funnel: inherited-home basics, demolition, reuse/buyback, real-estate utilization, inheritance/trust/finance, and free individual consultation. Reservations for the individual consultation open 2026-09-01 at 09:00 through Kawagoe City's empty-home counter.

Decision: **do not create an event page** and do not chase event traffic with a disposable article. This is short-lived informational intent, not the core revenue wedge. Instead, use it as a freshness/trust signal on the existing Kawagoe high-intent page only if Search Console begins showing `川越 空き家 相談`, `川越 相続 相談`, `実家 相続 相談 埼玉`, or similar queries before the event. If added, mark the date clearly and remove/replace the notice after 2026-09-27 so stale event copy does not remain.

Strategic implication: the city's own event bundles `不用品回収・買取 + 相続 + 不動産 + 解体 + 利活用`, independently validating the site's decision-order architecture. Keep the commercial page focused on comparing these routes before committing to full clearance; do not turn it into a generic event/news site.

## NEW 2026-08-30 — `家＋残置物をまとめて解決` is becoming a product category

A concrete market signal now validates the site's core wedge beyond ordinary SEO copy: HOUSE REVO's `イエウリ` and Haseko-group `カシコシュ` launched `おうちまるごと買取` in February 2026, explicitly combining real-estate sale with remaining-household-goods handling. Their stated problem is the burden of separately coordinating a real-estate company, clearance/estate-cleanout company and reuse shop, especially for distant heirs. This is stronger evidence that `残置物あり + 売却` is not merely an article keyword; providers are productizing the exact job-to-be-done.

Decision: strengthen the existing high-intent page around the **decision sequence**, not a specific provider: `家財を全部処分してから査定` should not be presented as the default. First determine whether the property can be valued/sold with contents remaining, then compare the net result and responsibility split against separate clearance. Keep municipal/reuse routes visible for items the owner wants to retain or dispose of independently.

New GSC watch modifiers: `家財そのまま 売却`, `家財ごと 売却`, `家と家財 まとめて`, `残置物 処分込み 買取`, `片付け不要 不動産買取`, `遠方 実家 片付け 売却`. If impressions appear, optimize `/kawagoe-shi/katazuke-hiyou-urenai/` before creating another page.

CTA implication: when the TownLife tracking link is available, test wording closer to the job-to-be-done — `片付け費用を決める前に、家財が残った状態で取れる選択肢を確認` — rather than generic `空き家を無料相談`. Do not claim TownLife itself buys contents or guarantees no-clearance sale; the CTA must promise only comparison/consultation that the actual offer supports.

## NEW 2026-08-30 — generic `実家じまい` SERP is becoming crowded

Fresh SERP review shows multiple purpose-built sites now occupying the broad `実家じまい` journey: some present themselves as neutral editorial media with expert/editorial-policy trust signals, others use situation diagnosis (`親が亡くなった / 施設入居 / 空き家 / 遠方`), and others lead directly with `片付ける前・解体する前に査定`. This means a broad `実家じまい 完全ガイド` or generic portal clone is no longer a good next-page bet for this site.

Decision: do **not** pivot into a generic `実家じまい` content hub and do not compete by adding many broad lifecycle articles. Keep the Kawagoe/local-primary-source advantage and bottom-of-funnel wedge: `片付け費用が高い/払えない`, `残置物あり`, `片付けずに売却`, `遠方`, `名義が親のまま`, and other concrete blockers immediately before a commercial decision.

Quality implication: competitors are increasingly publishing explicit editorial/monitoring credentials and structured decision paths. Before scaling page count, strengthen visible trust on existing pages: explain what is official/local information vs editorial guidance, keep municipal/non-ad routes beside commercial routes, disclose PR clearly when affiliate links go live, and avoid claiming neutrality if revenue can arise from referrals.

GSC implication: watch `実家じまい` only as a discovery modifier, not as a primary target. If it appears, combine it with the blocker that generated the impression (`費用`, `売却`, `残置物`, `遠方`, `相続登記`, etc.) and optimize the existing blocker page instead of creating a generic `実家じまい` page.

## NEW 2026-08-29 — unsellable inherited land / final-exit intent

Kawagoe City updated its official `所有者不明土地の発生予防` guidance on 2026-07-21 and explicitly points heirs to the national `相続土地国庫帰属制度`. Saitama Legal Affairs Bureau confirms the system is available for inherited land, with consultation by reservation and a standard processing period of about 8 months. The Ministry of Justice states that approval requires the land not to fall within statutory rejection/non-approval categories and that an approved owner must pay a management-cost contribution before ownership transfers to the state.

Important editorial boundary: this is a **land** exit route, not a shortcut for handing an intact vacant house to the state. Ministry of Justice eligibility rules include land with a building among the rejection categories. Therefore do not tell a reader with an inherited house to demolish merely to qualify; demolition cost, tax consequences, sale-with-building/contents, brokerage/purchase, municipal consultation and management options must be compared first.

Commercial implication: this creates a useful bottom-of-funnel branch for queries such as `相続した土地 売れない`, `実家 売れない 手放したい`, `空き家 売れない どうする`, `相続土地 処分`, and `負動産 手放す`. The affiliate CTA should still come **before** the national-surrender route for a house/lot that may have market value: first test whether it can be sold or otherwise resolved commercially; only then explain the national system as a constrained fallback for eligible inherited land. This strengthens trust without cannibalizing the primary empty-home offer.

Do not create a standalone page yet. First watch Search Console for impressions containing `売れない`, `手放したい`, `処分`, `国庫帰属`, `負動産`. If those modifiers appear on the existing high-intent page, add a compact `売れない場合の最終ルート` section there. A dedicated article is justified only after query evidence or clear ranking opportunity appears.

## NEW 2026-08-29 — inherited-home sale paperwork intent

Current SERPs show fresh 2026 content targeting `亡くなった親の家を売る + 必要書類/流れ`, which is commercially useful because the reader is already close to a sale decision. Kawagoe City's primary information gives a local, concrete angle: heirs can request fixed-asset certificates by counter or mail; the city lists a land/building valuation certificate as usable for ownership-transfer registration and a `名寄帳` as a way to see the deceased owner's land/building holdings in the city. For a deceased owner, the city requires documents showing death and the applicant's inheritance relationship, with a certified legal-heir information list accepted as an alternative in the stated cases. Fees are 200 JPY per stated unit for valuation certificates and the property ledger.

Editorial accuracy rule: do **not** say `名寄帳 is required for inheritance registration`. It is useful for identifying holdings/avoiding omissions, while the exact documents required for registration or sale depend on the case. Keep legal-procedure claims tied to Legal Affairs Bureau / professional guidance.

Commercial implication: add GSC watch terms `実家 売却 必要書類`, `亡くなった親の家 売る 流れ`, `相続 不動産 評価証明`, `相続 名寄帳`, `川越 相続 評価証明`. Do not create a standalone paperwork article yet. If impressions appear, first add a compact local checklist to the existing high-intent sale page, ending in `書類を全部揃える前でも、現状の売却可能性を確認` rather than delaying the valuation/solution CTA.

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
- Priority modifiers now include: `片付け費用`, `残置物`, `売却`, `片付けずに売却`, `そのまま売却`, `解体`, `管理`, `貸す`, `売るか貸すか`, `売れない`, `手放したい`, `処分`, `国庫帰属`, `負動産`, plus sale-readiness terms `必要書類`, `売る流れ`, `評価証明`, `名寄帳`, one-stop-disposition terms `家財そのまま`, `家財ごと`, `処分込み`, `片付け不要`, `遠方 実家 片付け 売却`, and short-lived local discovery terms `川越 空き家 相談`, `川越 相続 相談`, `実家 相続 相談 埼玉` through 2026-09-27.
- Treat `実家じまい` as a modifier/discovery term rather than a standalone page target unless GSC proves otherwise.
- Strengthen the existing high-intent page before creating overlapping pages when impressions emerge.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
