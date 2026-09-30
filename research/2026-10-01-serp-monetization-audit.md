# 2026-10-01 SERP / monetization audit

## Decision
Do not publish thin municipality pages. Keep the site focused on the decision immediately before a costly cleanup or property-sale contract.

## Current SERP signal
- `家じまいガイド` already offers pre-cleanup valuation, a 4-exit diagnosis, inheritance-registration stop checks, and sale/purchase comparisons. A generic “diagnosis” or “check value before cleanup” is no longer differentiated.
- `空き家片付けセンター` markets a national one-stop path from cleanup through sale, management and demolition. “One stop” is not a defensible USP.
- `MK-HOME` directly targets inherited/vacant homes with belongings left in place and fast direct purchase.
- Search results for shared ownership are dominated by specialist/legal content. This is high intent but needs careful, sourced treatment rather than generic SEO copy.

## High-intent cluster to validate in Search Console
Prioritize query×page data for:
1. 相続した実家 共有名義 売却
2. 実家 片付けずに売る
3. 空き家 残置物 売却 埼玉
4. 実家 解体してから売る そのまま売る
5. 再建築不可 相続 売却

Only deepen a cluster after impressions / ranking movement or clear conversion evidence appears. Do not generate city-name variants just to increase page count.

## Primary-source facts worth using
- 埼玉県「空き家対策」掲載日 2026-09-28: 利用目的のない空き家は約13万戸、20年で約1.8倍。
- 埼玉県「県内空き家の現状」掲載日 2026-09-04: 空き家約33.0万戸、利用目的のない空き家約13.6万戸（3.8%）。
- 埼玉県既存住宅流通促進ネットワーク: 官民連携で既存住宅流通を促進。
- 埼玉県空き家バンク等活性化支援事業: 自治体の空き家流通・改修支援も出口候補。

## ASP / monetization
- ASPLAY officially states it specializes in real-estate / recruiting affiliate advertising, but public pages do not establish a specific publisher payout for a suitable vacant-home sale offer.
- A third-party ASP tracker reports クラモア不動産売却 at afb 4,230円(税込)/成果. Treat this as discovery only; do not ship an affiliate link until the logged-in ASP screen confirms current payout, achievement point, approval/denial conditions, geographic/property restrictions, cookie attribution and permitted promotional wording.

## Site-quality blocker confirmed on current main
`build.py` still contains:
- nav link fixed to `/kawagoe-shi/mitsumori-check/`
- homepage eyebrow `Kawagoe / Inherited Home`
- homepage meta description beginning `川越市を中心に`
- homepage municipal consultation block fixed to 川越市

`site_data.json` still has `ga4_id` empty and `offers` empty, so the revenue funnel cannot yet be measured end-to-end.

## Implementation order
P0: remove Kawagoe-only framing from global/home UI while preserving genuinely useful Kawagoe pages as local evidence pages.
P1: pass regression checks and ensure all global links are prefecture-wide.
P2: install GA4 and measure `diagnosis_start`, `diagnosis_result`, and `affiliate_click`.
P3: add exactly one approved ASP offer with verified conditions.
P4: use GSC query×page evidence to choose the first deep commercial page.

## Product direction
The defensible product is not “cleanup company comparison” and not generic “one stop”. It is a pre-contract triage layer:
1. STOP: title / inheritance registration / co-owner agreement / legal blocker.
2. PROPERTY DIFFICULTY: rebuildability/access/leasehold/condition/belongings/urgency.
3. EXIT: ordinary brokerage / as-is purchase / hold-manage / public-professional consultation.
4. CLEANUP: only after the exit is chosen, determine what actually needs removal.

This structure aligns user value with monetization: users with a normal sale path can see brokerage/valuation offers; difficult/as-is cases can see suitable purchase offers; blocked cases should be sent to primary-source or professional help rather than monetized prematurely.