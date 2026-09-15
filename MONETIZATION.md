# Monetization runbook

Updated: 2026-09-15

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED 2026-08-27 from TownLife Affiliate's official recommended-program page: conversion point = free estimate request; payout = 10,000 JPY per approved result (11,000 JPY tax-inclusive display); approval rate approximately 85%. Logged-in dashboard remains authoritative for exact account terms/tracking URL.
   - First monetization test: `片付け費用が高い/払えない + 売却/残置物` traffic.
   - Never insert a guessed tracking URL or imply partnership before approval.

2. DIRECT PARTNERSHIP CANDIDATE — idea株式会社 `相続空き家 多業種パートナー制度`
   - Publicly announced 2026-08-04: Saitama is in scope; registration/annual fee zero; information fee 90,000–350,000 JPY when idea closes the property sale; amount slides with property size/profit. Entry does not equal contract, and exact partner terms must be confirmed before use.
   - This is materially higher-value than ordinary cleanup leads, but it is a B2B referral partnership rather than a normal click-based ASP program. Do not place a referral form/link or transmit owner information until a partnership agreement, consent flow, privacy handling, and exact qualification/payment conditions are confirmed.
   - Best-fit traffic if approved: `相続した実家を売りたい`, `売れない実家`, `残置物あり売却`, `片付け費用が高い`, `遠方の相続空き家` where the visitor has decided or strongly intends to sell.
   - Keep TownLife as the live-test priority until this direct agreement is actually signed and operational.

3. Estate-clearance offers
   - Use mainly on cleanup-first intent such as `遠方`, `見積`, `施設入居後`, `立会い不要`.
   - Logged-in ASP dashboard is authoritative for current payout/approval terms.

4. REUSE / BUYBACK — secondary micro-conversion, not the primary revenue path
   - Kawagoe City officially directs residents to consider reuse before disposing of bulky waste and specifically links to Market Enterprise's `おいくら` bulk appraisal service under its reuse partnership.
   - This creates a strong trust-first branch for `処分費を下げたい / 売れる物が分からない / 粗大ごみに出す前` visitors: valuables/keepsakes → reuse appraisal → municipal disposal for true waste → paid cleanup only for the remaining necessary scope.
   - A 2026 third-party ASP survey reports consumer `おいくら` programs at roughly 253 JPY (afb) / 300 JPY (A8.net). Treat these amounts as UNCONFIRMED until the logged-in ASP dashboard is checked; do not publish or implement guessed tracking links.
   - Even if confirmed, the payout is too small to displace the higher-value empty-home/disposition path. Use it only where it reduces cleanup cost and increases trust/engagement.

## Conversion architecture

- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: empty-home/disposition comparison
- `片付けずに売却 / 残置物あり売却 / 実家そのまま売却` → PRIMARY: disposition comparison before full clearance
- `売れない実家 / 空き家を手放したい / 不動産会社に断られた` → PRIMARY: re-check sale/purchase/other exits before irreversible demolition or disposal; SECONDARY: explain official last-resort routes accurately
- `相続登記前 / 名義変更前 + 実家売却・査定` → PRIMARY: explain that consultation/valuation can precede completion of every procedure, while legal completion requirements must be confirmed with the relevant professional; do not promise a sale can close before required registration.
- `2024-04-01以前の相続 + 親名義のまま` → DEADLINE-FIRST: show the official 2027-03-31 inheritance-registration deadline and route unresolved users to legal/official confirmation before irreversible work; if sale intent is already clear, valuation/disposition research may proceed in parallel without implying that closing can bypass required registration.
- `空き家 維持費 / 実家 持ち続ける 費用 / 固定資産税 + 管理` → PRIMARY: annual carrying-cost check, then disposition comparison
- `売るか貸すか迷う / しばらく使わない / 将来戻る可能性あり` → PRIMARY: compare sale with Saitama/Kawagoe official rental options before pushing a sale lead.
- `処分費を下げたい / 粗大ごみに出す前 / 売れる物が分からない` → PRIMARY: official reuse-before-disposal path; SECONDARY: cleanup quote only for remaining scope
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → reuse check + empty-home CTA + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA

## 2026-09-15 deadline opportunity: old inheritance still in parent's name

The Ministry of Justice currently highlights a concrete near-term deadline: for real estate inherited before 2024-04-01 where the inheritance was already known, inheritance registration is required by 2027-03-31. The obligation also applies to older inheritances, and unjustified noncompliance can be subject to a fine of up to 100,000 JPY.

SERP implication: competitors are now publishing deadline-led pages specifically around `2027年3月31日`, `親名義のまま`, and `実家 相続登記`. This is no longer just evergreen legal background; it is a time-bounded intent cluster that can bring inherited-home owners into the site's core decision flow.

Implementation rule:
1. Add a diagnosis question/notice for `親名義のまま / 2024-04-01以前の相続 / 登記未了` rather than creating thin municipality pages.
2. Use the Ministry of Justice as the primary factual source and state the deadline precisely; do not manufacture countdown urgency.
3. If ownership/heirs are unresolved, show official/legal confirmation before disposal, demolition or a sale-closing CTA.
4. If the visitor already intends to sell, allow valuation/disposition comparison to run in parallel with registration preparation, but never claim that required registration can be skipped.
5. Keep the monetization destination aligned with sale intent (TownLife now; direct inherited-vacant-home referral only if contracted), not a generic legal-lead detour unless a separately vetted legal offer later proves economically and editorially appropriate.

GSC test before a standalone article: `相続登記 2027年3月31日`, `実家 親名義のまま`, `昔の相続 名義変更`, `相続登記してない 実家 売却`, `相続登記 期限 実家`. If these queries start appearing on an existing inheritance/sale page, improve that page first. Create a dedicated deadline page only if GSC shows distinct demand and the existing page cannot satisfy intent cleanly.

## 2026-09-15 reuse-before-disposal finding

Kawagoe City's current bulky-waste page explicitly asks residents to consider reuse before disposal and links to `おいくら`, following a city partnership with Market Enterprise. This is more useful than another generic `不用品回収おすすめ` page because it is an official local decision rule and directly reduces the amount that needs paid removal.

Implementation rule:
1. Preserve documents, valuables, memorial items and family keepsakes first.
2. For potentially reusable items, show the official reuse option before presenting paid disposal/cleanup.
3. For actual waste, show lawful municipal disposal/self-delivery where practical.
4. Only then compare cleanup providers for the remaining volume, with lawful household-waste transport checks.
5. If an `おいくら` affiliate program is confirmed in the logged-in ASP dashboard, disclose PR and test it as a secondary CTA; never replace the city's neutral route with a disguised ad.

Economic implication: do not chase a ~300 JPY reuse lead at the expense of a 10,000 JPY approved empty-home lead or a potential 90,000–350,000 JPY closed-sale referral. The reuse branch is valuable because it lowers visitor cost, builds trust, and qualifies what actually needs removal.

GSC test before creating any new article: `粗大ごみ 売れるもの`, `実家片付け 買取`, `遺品 買取 処分 どっち`, `川越市 粗大ごみ 買取`, `片付け費用 買取 相殺`. First enrich the existing cleanup-cost / household-goods-removal flow if impressions appear; do not create five location pages.

## 2026-09-15 monetization implication: qualify sale intent before cleanup intent

A newly launched direct referral program publicly advertises 90,000–350,000 JPY per completed inherited-vacant-home sale in Saitama. This does not replace the confirmed TownLife test yet, but it changes the economic value of accurately identifying `売却意思あり` visitors.

Strategic implication:
- The diagnosis should capture `売る方向 / まだ未定 / 残す` before asking how much cleanup is needed.
- For `売る方向`, preserve the disposition-first path: do not encourage full clearance or demolition before checking sale options.
- For `まだ未定`, keep municipal consultation, management, and decision support visible; do not force a commercial sale lead.
- For `相続放棄検討中 / ownership unresolved`, suppress irreversible disposal/sale CTAs until the user has confirmed the legal path.
- If the direct partnership is signed, measure qualified-lead rate and closed-sale revenue separately from ordinary affiliate clicks; a lower-volume sale-intent page can economically outperform broad cleanup traffic.

## Disposition-first rule for expensive cleanup

For `片付け費用が高い/払えない`, full clearance is not the default prerequisite for valuation or disposition.

1. Secure important documents, valuables, memorial items, and anything the family must retain.
2. Before paying for full clearance, check whether the home can be valued and whether sale, purchase, rental, management, or another route is realistic with contents remaining.
3. Confirm ownership/inheritance constraints and relevant official/local consultation routes before signing irreversible work.
4. Once the likely disposition is known, separate reusable/buyback items and use municipal disposal where lawful/practical for items that actually need removal.
5. Use cleanup-company comparison only for the remaining necessary scope; compare identical scope, extra-charge conditions, and lawful household-waste transport arrangements.

## Current SERP direction

A notable 2026 competitor pattern is the rise of structured Saitama municipality-by-municipality demolition-subsidy databases. Do not answer this by mass-producing similar city pages. Only create a municipal page where official rules materially change the user's decision (application-before-contract deadline, eligibility, tax/rebuild consequence, or a unique official route) and there is measurable search demand or a monetizable downstream action.

Competitors also increasingly combine `相続した実家`, `残置物`, `売却`, `管理`, `解体`, and `片付け` on one commercial landing page. Local cleanup providers still lead with speed, free estimates, buyback, and one-stop handling. Avoid competing primarily on generic `おすすめ業者` or city-name pages.

The useful gap remains a decision framework immediately before spending money: ownership/inheritance check → decide likely exit → compare disposition with contents remaining → reuse/buyback and municipal disposal where practical → cleanup quotes only for necessary scope → demolition only after tax/rebuild/subsidy checks.

## Trust-first comparison

Keep legitimate non-ad routes visible beside future affiliate CTAs: Kawagoe City's professional empty-home consultation, eligible empty-home-bank registration, management options, official reuse option, official rental/JTI option, and official tax/legal guidance. Do not make the page look like a disguised affiliate landing page.

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
- deadline/registration modifiers: `相続登記 2027年3月31日`, `実家 親名義のまま`, `昔の相続 名義変更`, `相続登記してない 実家 売却`, `相続登記 期限 実家`
- sale-intent modifiers: `相続した実家 売りたい`, `相続 空き家 売却 残置物`, `実家 売却 片付け前`, `売れない 相続空き家`, `遠方 相続実家 売却`
- reuse modifiers: `粗大ごみ 売れるもの`, `実家片付け 買取`, `遺品 買取 処分 どっち`, `川越市 粗大ごみ 買取`, `片付け費用 買取 相殺`
- existing modifiers: `片付け前`, `残置物`, `家財そのまま`, `片付け不要`, `売却`, `買取`, `片付け費用 払えない`, `空き家 維持費`, `解体前 査定`, `相続登記前 売却`, `売れない実家`, `不動産会社 断られた 空き家`

If impressions overlap the existing high-intent page, optimize it before creating another page. Do not create standalone pages until GSC shows distinct demand.

## Scaling rule

Do not mass-produce thin city pages. A new location or intent page needs distinct official rules/data, distinct SERP intent, and a plausible monetization path. Until the first commercial page gets meaningful impressions/clicks and a monetization agreement/tracking URL is live, improving decision quality and conversion architecture outranks page count.
