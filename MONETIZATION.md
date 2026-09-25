# Monetization runbook

Updated: 2026-09-25

## 2026-09-25 strategic finding: municipality-backed calculators are now a SERP competitor

Fresh primary-source review found that Saitama municipalities are increasingly linking residents to Crassone's municipality-specific `すまいの終活ナビ`. Kazo City says its version provides demolition-cost estimates, post-demolition land-sale price estimates, a fixed-asset-tax simulator, and a nuisance-risk diagnosis. Fukaya City likewise officially promotes a tool that estimates demolition cost and land-sale price after its 2025-09-01 cooperation agreement with Crassone. A 2026-02 announcement says Crassone had agreements with 26 Saitama municipalities, covering 48.9% of the prefecture's population.

Implication: do NOT try to win `解体費用 相場 + 市名` by mass-producing generic city pages. Municipality-backed tools have stronger trust and useful calculators. Our defensible layer is the decision BEFORE demolition: contents-remaining valuation -> net-proceeds comparison -> subsidy/contract timing -> asbestos/permit checks -> only then demolition quote where needed. `/kaitai-check/` and `/tedori-hikaku/` should remain linked as one decision flow.

New high-intent tests: `解体する前 査定`, `解体してから売る どっち`, `空き家 解体費用 売却価格`, `実家 更地 売却 手残り`, `空き家 解体 補助金 契約前`. If GSC impressions emerge, improve the existing two tools first rather than creating municipality pages.

Trust rule: where a visitor's municipality offers an official/municipality-endorsed calculator, it may be shown as a neutral benchmark. Do not disguise an external commercial calculator as a government service, and do not sacrifice the user's net outcome merely to preserve an affiliate click.

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
   - This creates a trust-first branch for `処分費を下げたい / 売れる物が分からない / 粗大ごみに出す前` visitors, but ONLY after sale/disposition intent is checked.
   - 2026-09-16 SERP review shows Saitama empty-home buyers explicitly competing on `家財ごとそのまま買取` / `残置物そのまま買取`. Therefore do not automatically strip or sell household contents before the property is valued when the owner intends to sell. Removing contents first can add work and may destroy the convenience/value proposition of a contents-included purchase.
   - Correct order for sale-intent users: secure documents/keepsakes → get property/disposition valuation with contents remaining → confirm whether buyer accepts/includes contents and how that affects net proceeds → only then separately appraise reusable items if economically useful → dispose/clear only the residual scope.
   - A 2026 third-party ASP survey reports consumer `おいくら` programs at roughly 253 JPY (afb) / 300 JPY (A8.net). Treat these amounts as UNCONFIRMED until the logged-in ASP dashboard is checked; do not publish or implement guessed tracking links.
   - Even if confirmed, the payout is too small to displace the higher-value empty-home/disposition path. Use it only where it reduces cleanup cost and increases trust/engagement.

## Conversion architecture

- FIRST QUESTION: likely exit = `売る方向 / まだ未定 / 残す・貸す`. This determines whether contents should be left in place for a property valuation before reuse/clearance.
- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: empty-home/disposition comparison with contents remaining
- `片付けずに売却 / 残置物あり売却 / 実家そのまま売却` → PRIMARY: disposition comparison before full clearance; explicitly compare contents-included purchase vs clear-then-sell on net proceeds/time, not headline price alone
- `売れない実家 / 空き家を手放したい / 不動産会社に断られた` → PRIMARY: re-check sale/purchase/other exits before irreversible demolition or disposal; SECONDARY: explain official last-resort routes accurately
- `相続登記前 / 名義変更前 + 実家売却・査定` → PRIMARY: explain that consultation/valuation can precede completion of every procedure, while legal completion requirements must be confirmed with the relevant professional; do not promise a sale can close before required registration.
- `2024-04-01以前の相続 + 親名義のまま` → DEADLINE-FIRST: show the official 2027-03-31 inheritance-registration deadline and route unresolved users to legal/official confirmation before irreversible work; if sale intent is already clear, valuation/disposition research may proceed in parallel without implying that closing can bypass required registration.
- `空き家 維持費 / 実家 持ち続ける 費用 / 固定資産税 + 管理` → PRIMARY: annual carrying-cost check, then disposition comparison
- `売るか貸すか迷う / しばらく使わない / 将来戻る可能性あり` → PRIMARY: compare sale with Saitama/Kawagoe official rental options before pushing a sale lead.
- `処分費を下げたい / 粗大ごみに出す前 / 売れる物が分からない` + NO near-term property sale → PRIMARY: official reuse-before-disposal path; SECONDARY: cleanup quote only for remaining scope
- `処分費を下げたい` + SALE intent → property valuation first; reuse/buyback only after confirming whether contents-included sale is preferable
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → ask exit intent first; sale-intent = empty-home CTA before reuse/cleanup; cleanup-intent = reuse check + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA

## Current SERP direction

A notable 2026 competitor pattern is the rise of structured Saitama municipality-by-municipality demolition-subsidy databases and, now, municipality-backed decision calculators. Do not answer this by mass-producing similar city pages. Only create a municipal page where official rules materially change the user's decision (application-before-contract deadline, eligibility, tax/rebuild consequence, or a unique official route) and there is measurable search demand or a monetizable downstream action.

Competitors increasingly combine `相続した実家`, `残置物`, `売却`, `管理`, `解体`, and `片付け` on one commercial landing page. A more specific current pattern is `残置物・家財そのまま買取`. Local cleanup providers still lead with speed, free estimates, buyback, and one-stop handling. Avoid competing primarily on generic `おすすめ業者` or city-name pages.

The useful gap remains a decision framework immediately before spending money: ownership/inheritance check → decide likely exit → compare disposition with contents remaining → if selling, compare contents-included vs separate buyback/clearance on NET outcome → municipal/reuse options where appropriate → cleanup quotes only for necessary scope → demolition only after tax/rebuild/subsidy checks.

## TownLife approval gate

1. Planned placement pages: `/tedori-hikaku/`, `/kaitai-check/`, and high-intent sale/cleanup-cost pages only where the CTA matches intent.
2. Keep explicit PR disclosure near future commercial CTA.
3. Keep municipal/non-ad alternatives visible.
4. After approval, insert only the issued tracking URL.
5. Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.

## Search / indexing status

Search Console URL Inspection / Pages report is the indexing source of truth; public `site:` checks are only supplementary.

Next GSC checks:
- indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`, `/tedori-hikaku/`, `/kaitai-check/`
- query-level impressions and CTR/title performance
- NEW demolition-decision modifiers: `解体する前 査定`, `解体してから売る どっち`, `空き家 解体費用 売却価格`, `実家 更地 売却 手残り`, `空き家 解体 補助金 契約前`
- contents-included modifiers: `家財そのまま 売却`, `残置物そのまま 買取`, `実家 片付けずに売る`, `空き家 家財ごと 買取`, `片付けてから売る どっち`
- deadline/registration modifiers: `相続登記 2027年3月31日`, `実家 親名義のまま`, `昔の相続 名義変更`, `相続登記してない 実家 売却`, `相続登記 期限 実家`
- sale-intent modifiers: `相続した実家 売りたい`, `相続 空き家 売却 残置物`, `実家 売却 片付け前`, `売れない 相続空き家`, `遠方 相続実家 売却`

Do not infer rankings, CTR, or indexing from public search alone. Use actual GSC data before deciding whether a new standalone page is warranted.
