# Monetization runbook

Updated: 2026-09-06

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
- `売れない実家 / 空き家を手放したい / 不動産会社に断られた` → PRIMARY: re-check sale/purchase/other exits before irreversible demolition or disposal; SECONDARY: explain official last-resort routes accurately
- `相続登記前 / 名義変更前 + 実家売却・査定` → PRIMARY: explain that consultation/valuation can precede completion of every procedure, while legal completion requirements must be confirmed with the relevant professional; do not promise a sale can close before required registration.
- `空き家 維持費 / 実家 持ち続ける 費用 / 固定資産税 + 管理` → PRIMARY: annual carrying-cost check, then disposition comparison
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

## Sell-failed / hand-it-back angle (validated 2026-09-06)

Kawagoe City updated its official owner-unknown-land prevention page on 2026-07-21 and explicitly points heirs to the national `相続土地国庫帰属制度` and the Saitama Legal Affairs Bureau consultation desk. This creates a useful high-intent adjacent cluster: `売れない実家`, `空き家 手放したい`, `不動産会社に断られた`, `国に返したい`.

Guardrail and conversion logic:
- Do NOT present national reversion as an easy way to hand a house to the government. The national scheme is for qualifying inherited land; land with a building is not eligible for approval.
- Official government guidance states an application fee of JPY 14,000 per parcel and, after approval, a management contribution generally starting at JPY 200,000, with some land calculated by area.
- Therefore a user with a standing inherited house should compare sale/purchase/other realistic exits before paying for demolition merely to pursue national reversion.
- This is commercially stronger than a generic explainer because `売れない/手放したい` indicates an owner already seeking an exit. Bridge to the empty-home/disposition comparison, while keeping Kawagoe City / Legal Affairs Bureau as visible non-ad alternatives.
- Do not create a standalone national-reversion article yet. First test GSC impressions for the modifiers below and add a concise FAQ/decision branch to the existing high-intent page only if demand appears.

## Carrying-cost angle (validated 2026-09-05)

Kawagoe City's 2026 vacant-home guide explicitly lists `空き家を持ち続けることで、どのくらい費用がかかるのか（税金、維持費）` as a typical owner concern. The city's management guidance also requires regular repairs, pruning and weed removal, while current local cleanup SERPs increasingly emphasize recurring garden/management costs after a one-time house clearance.

Strategic implication:
- Add `持ち続ける年間コスト` as a decision input, not as another thin city page.
- Best implementation is a calculator/table inside the existing high-intent decision page: fixed-asset tax + insurance + utilities/minimum services + garden/ventilation/inspection + travel + expected repairs, compared with sale/rent/manage/demolish routes.
- Do not publish generic cost figures without sourced assumptions; let users enter their actual annual amounts where possible.
- Conversion bridge: `片付け代だけでなく、1年持ち続ける総額を見てから出口を決める` → empty-home/disposition comparison.

## Provider demand data: sale-first intent validated (2026-09-05)

TownLife's June 2026 monthly report says its surveyed empty-home users exceeded 1,000. In that provider dataset, 100% selected `売却したい`, 71% also expressed interest in rental/minpaku, 98% owned detached houses, and 73% reported buildings aged 41+ years. Treat these figures as TownLife user data, not population-level statistics.

Strategic implication:
- Keep the primary CTA sale/disposition-first rather than generic cleanup comparison. The commercial audience reaching an empty-home solution service is demonstrably sale-oriented.
- Secondary copy can preserve rental/management as alternatives because users may consider multiple exits, but do not dilute the first CTA with a long equal-weight menu.
- For older detached homes, decision content should explicitly surface `売れるか`, `残置物を先に捨てる必要があるか`, `解体前に査定すべきか`, and `維持費を払い続けるか` before cleanup-company selection.
- Search Console test: segment queries/pages that include `売却`, `買取`, `残置物`, `片付け前`, `解体前` and compare CTR/affiliate-click rate against cleanup-only modifiers. If sale-intent impressions exist, optimize the existing decision page before adding pages.

## Current SERP direction

Competitors increasingly lead with `現状買取`, `残置物あり`, `片付け前に相談/査定`. A newer 2026 SERP pattern also answers `相続登記前でも相談できますか` directly beside `残置物ありで査定できますか`, suggesting these are adjacent pre-sale anxieties rather than separate content silos. Avoid generic `川越市 遺品整理おすすめN選` and broad `実家じまい` content hubs.

The useful gap is a decision framework immediately before spending money: compare disposition with contents remaining, reuse/buyback, municipal disposal where practical, cleanup quotes on identical scope, rent/manage, and demolition only after cost/tax checks.

### 2026-09-05 market validation: whole-home sale is becoming a product category

`イエウリ × カシコシュ` launched `おうちまるごと買取`, explicitly combining remaining-contents sorting/buyback with a property purchase auction. Its official page currently covers Saitama and states that 1,300+ real-estate companies participate in the purchase auction. This directly validates the site's `do not fully clear first; compare the property's exit and reusable contents together` thesis.

Strategic implication:
- Do not copy the service or turn the site into a single-provider advert.
- Strengthen neutral comparison language around `家＋荷物の最終手取り` and the difference between purchase and brokerage.
- Treat HOUSE REVO / イエウリ as a potential direct partnership or referral lead because the product matches the site's highest-intent traffic unusually well. No public ASP payout was confirmed in the 2026-09-05 search, so do not insert a link as an affiliate or state a reward until direct/ASP terms are verified.
- Keep TownLife as the confirmed primary monetization candidate until a better verified commercial agreement exists.

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
- modifiers: `片付け前`, `残置物`, `家財そのまま`, `家財ごと`, `片付け不要`, `売却`, `買取`, `片付け費用 払えない`, `遠方 実家 売却`, `空き家 維持費`, `実家 持ち続ける 費用`, `解体前 査定`, `相続登記前 売却`, `名義変更前 査定`, `売れない実家`, `空き家 手放したい`, `不動産会社 断られた 空き家`, `相続土地 国庫帰属 実家`

If impressions overlap the existing high-intent page, optimize it before creating another page. In particular, do not create a standalone `相続登記前` or `国庫帰属` page until GSC shows distinct demand; first test an FAQ/section inside the existing disposition page if impressions appear.

## Scaling rule

Do not mass-produce thin city pages. A new location or intent page needs distinct official rules/data, distinct SERP intent, and a plausible monetization path. Until the first commercial page gets meaningful impressions/clicks and the affiliate tracking URL is live, improving decision quality and conversion architecture outranks page count.