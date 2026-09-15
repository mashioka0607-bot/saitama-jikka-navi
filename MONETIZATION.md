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

## Conversion architecture

- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: empty-home/disposition comparison
- `片付けずに売却 / 残置物あり売却 / 実家そのまま売却` → PRIMARY: disposition comparison before full clearance
- `売れない実家 / 空き家を手放したい / 不動産会社に断られた` → PRIMARY: re-check sale/purchase/other exits before irreversible demolition or disposal; SECONDARY: explain official last-resort routes accurately
- `相続登記前 / 名義変更前 + 実家売却・査定` → PRIMARY: explain that consultation/valuation can precede completion of every procedure, while legal completion requirements must be confirmed with the relevant professional; do not promise a sale can close before required registration.
- `空き家 維持費 / 実家 持ち続ける 費用 / 固定資産税 + 管理` → PRIMARY: annual carrying-cost check, then disposition comparison
- `売るか貸すか迷う / しばらく使わない / 将来戻る可能性あり` → PRIMARY: compare sale with Saitama/Kawagoe official rental options before pushing a sale lead. Kawagoe promotes JTI's マイホーム借上げ制度; because of the Saitama–JTI agreement, Saitama properties can use the scheme without the ordinary 50+ age requirement. Treat this as a non-ad trust route, not an affiliate offer.
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → empty-home CTA + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA

## 2026-09-15 monetization implication: qualify sale intent before cleanup intent

A newly launched direct referral program publicly advertises 90,000–350,000 JPY per completed inherited-vacant-home sale in Saitama. This does not replace the confirmed TownLife test yet, but it changes the economic value of accurately identifying `売却意思あり` visitors.

Strategic implication:
- The diagnosis should capture `売る方向 / まだ未定 / 残す` before asking how much cleanup is needed.
- For `売る方向`, preserve the disposition-first path: do not encourage full clearance or demolition before checking sale options.
- For `まだ未定`, keep municipal consultation, management, and decision support visible; do not force a commercial sale lead.
- For `相続放棄検討中 / ownership unresolved`, suppress irreversible disposal/sale CTAs until the user has confirmed the legal path.
- If the direct partnership is signed, measure qualified-lead rate and closed-sale revenue separately from ordinary affiliate clicks; a lower-volume sale-intent page can economically outperform broad cleanup traffic.
- GSC priority additions: `相続した実家 売りたい`, `相続 空き家 売却 残置物`, `実家 売却 片付け前`, `売れない 相続空き家`, `遠方 相続実家 売却`. Optimize existing decision/disposition pages first; do not create five new articles.

## Saitama-specific rent-before-sale branch

Kawagoe City's official guidance promotes JTI's `マイホーム借上げ制度` for homes left unused after moving or inheritance. The municipality states that JTI rents the home and provides monthly rent payments regardless of tenant occupancy, subject to the scheme's conditions. Crucially, while the scheme ordinarily has a 50+ age condition, the Saitama Prefecture–JTI cooperation removes that age restriction for properties in Saitama.

Implication:
- This is a real Saitama-specific differentiator and a reason not to force every undecided owner into a sale CTA.
- Add/strengthen a diagnosis branch for `将来戻る可能性がある / 売却はまだ決めていない / 貸すことも検討` and show the official rental route beside sale/management choices.
- Do not monetize this branch unless a legitimate, disclosed commercial program is separately confirmed. Its role is trust, decision quality, and preventing low-quality sale leads.
- Before recommending rental to an inherited-home visitor, flag that renting can interact with tax/legal conditions (including the inherited-vacant-home special deduction); do not make a categorical tax recommendation.
- GSC test before creating content: `相続 実家 貸す 売る`, `空き家 売るか貸すか`, `実家 貸す 方法 埼玉`, `マイホーム借上げ制度 埼玉`. Prefer enriching the existing decision page/diagnosis if impressions overlap.

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

Competitors increasingly combine `相続した実家`, `残置物`, `売却`, `管理`, `解体`, and `片付け` on one commercial landing page. Local cleanup providers still lead with speed, free estimates, buyback, and one-stop handling. Avoid competing primarily on generic `おすすめ業者` or city-name pages.

The useful gap remains a decision framework immediately before spending money: ownership/inheritance check → decide likely exit → compare disposition with contents remaining → reuse/buyback and municipal disposal where practical → cleanup quotes only for necessary scope → demolition only after tax/rebuild/subsidy checks.

Kawagoe City also continues to support inheritance prevention education and empty-home management through official programs, reinforcing the trust-first path for visitors who are not ready to sell.

## Trust-first comparison

Keep legitimate non-ad routes visible beside future affiliate CTAs: Kawagoe City's professional empty-home consultation, eligible empty-home-bank registration, management options, official rental/JTI option, and official tax/legal guidance. Do not make the page look like a disguised affiliate landing page.

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
- sale-intent modifiers: `相続した実家 売りたい`, `相続 空き家 売却 残置物`, `実家 売却 片付け前`, `売れない 相続空き家`, `遠方 相続実家 売却`
- rent-vs-sale modifiers: `相続 実家 貸す 売る`, `空き家 売るか貸すか`, `実家 貸す 方法 埼玉`, `マイホーム借上げ制度 埼玉`
- existing modifiers: `片付け前`, `残置物`, `家財そのまま`, `片付け不要`, `売却`, `買取`, `片付け費用 払えない`, `空き家 維持費`, `解体前 査定`, `相続登記前 売却`, `売れない実家`, `不動産会社 断られた 空き家`

If impressions overlap the existing high-intent page, optimize it before creating another page. Do not create standalone pages until GSC shows distinct demand.

## Scaling rule

Do not mass-produce thin city pages. A new location or intent page needs distinct official rules/data, distinct SERP intent, and a plausible monetization path. Until the first commercial page gets meaningful impressions/clicks and a monetization agreement/tracking URL is live, improving decision quality and conversion architecture outranks page count.
