# 2026-09-30 SERP / monetization brief

## Decision
Do not publish additional thin municipality pages. The next content/product unit should be a prefecture-wide **pre-disposal decision page** that answers one commercial question: **should I pay to clear the house before I know whether it can be sold as-is?**

## SERP evidence checked 2026-09-30
- `埼玉 実家じまい 片付け 売却`: iezimai.com is explicitly positioning `遺品整理 × 不動産買取` as a one-stop service across Saitama.
- `埼玉 相続 空き家 売却 残置物`: SA ranks with a strong `残置物・老朽化も現況から整理` proposition and examples where disposal/demolition costs are evaluated before sale.
- Generic information alone is therefore weak. The useful gap is a neutral **order-of-operations / net-proceeds decision tool** before users commit to disposal.

## Primary-source evidence
Saitama Prefecture published material on 2026-09-17 citing approximately **330,000 vacant homes and a 9.3% vacancy rate** in the prefecture. Earlier prefectural material also shows that homes with no intended use have been increasing even when total vacant-home counts are not. Use prefectural/municipal primary sources for factual claims; do not manufacture local statistics for SEO pages.

## High-intent keyword cluster to test in Search Console
Treat this as one intent cluster, not separate thin pages:
- `実家 片付けてから売る`
- `実家 片付けずに売却`
- `空き家 残置物 そのまま 売却 埼玉`
- `相続した家 片付ける前 査定`
- `実家じまい 片付け 費用 売却`

The underlying job is: **avoid paying unnecessary disposal cost before the property's exit is known**.

## Conversion architecture
1. Entry: article / SERP landing page.
2. Decision: title/estate status -> family agreement -> sell/keep/use -> amount of belongings -> distance/deadline.
3. If sale intent exists: show `現況査定を先に取る` and net-proceeds comparison.
4. If undecided: route to public Saitama vacant-home consultation / official municipality resources rather than forcing an affiliate CTA.
5. Only after intent is clear: commercial comparison / affiliate CTA, clearly marked PR.

Measure `diagnosis_start`, `diagnosis_complete`, `net_proceeds_view`, `affiliate_click` by landing page and query cluster. Do not judge only by pageviews.

## ASP / revenue condition
Do not hard-code an unverified reward or approval condition into user-facing copy. Publicly discoverable program descriptions can be used for prioritisation, but the actual account-specific reward, approval rules, prohibited promotion methods, and tracking URL must be checked in the logged-in ASP dashboard before activation.

## Current implementation blocker found in repository
`build.py` still contains province-expansion debt:
- navigation points to `/kawagoe-shi/mitsumori-check/`;
- home eyebrow is `Kawagoe / Inherited Home`;
- home description says `川越市を中心に`;
- home public consultation is fixed to Kawagoe City;
- priority content list is entirely `kawagoe-shi/*`.

This is a higher priority than publishing a new article because it conflicts with the current Saitama-wide positioning and can misroute non-Kawagoe users.

## Next implementation order
P0: replace Kawagoe-fixed global navigation/home copy/public consultation with Saitama-wide neutral equivalents while preserving useful Kawagoe pages as local evidence pages.

P0: activate analytics and affiliate tracking only after real IDs/URLs are available; never invent them.

P1: build one `片付け前に現況査定・手残り比較` decision page and internally link diagnosis -> comparison -> commercial CTA.

P1 measurement gate: after enough impressions, compare this intent cluster on impressions, average position, CTR, diagnosis completion and affiliate CTR. Expand only if it demonstrates either organic demand or conversion signal.

## Sources checked
- Saitama Prefecture, 2026-09-17: https://www.pref.saitama.lg.jp/a0503/super-city/2026matching/r8businesspitch-enjoyworks.html
- Saitama Prefectural Assembly, vacant-home statistics/background: https://www.pref.saitama.lg.jp/e1601/gikai-gaiyou/r0606/4/d/0610.html
- Competitive SERP example: https://iezimai.com/
- Competitive SERP example: https://sakk.jp/service/service04/
