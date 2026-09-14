# 2026-09-14 SERP / monetization decision

## New finding
A recently indexed competitor, 「空き家片付けセンター」, now uses almost the same broad promise as generic one-stop sites: inherited home / residual belongings / estate sorting / sale / management / demolition, and explicitly says users do not need to decide whether to clean, sell, or keep before consulting.

This reduces the defensibility of a generic 「片付けからその先まで」 positioning.

## Decision change
Do **not** compete as another one-stop cleanup portal. Strengthen the site as a **decision-first, municipal-evidence-backed navigator**:

1. ownership / inheritance status
2. family agreement
3. desired exit (sell / keep / use / undecided)
4. current-condition exit check before full cleanup
5. valuables / reuse check
6. only then paid cleanup / disposal / sale service

The monetization funnel remains: diagnosis -> high-intent decision page -> suitable commercial offer. Do not add thin city-name pages.

## Highest-intent page to prioritize
`/kawagoe-shi/akiya-kazai-tekkyo/`

Rewrite/expand around the question: **「売却前に家財を全部撤去する必要があるのか」** rather than generic disposal instructions. The page should distinguish:
- sell as-is / ask buyer or broker what must be removed
- valuables and reuse before disposal
- lawful municipal disposal route
- demolition only after the exit decision

## Primary-source support checked
- Kawagoe City (2026-06-08): free consultation path covers inheritance, management, rent, sale and demolition.
- Kawagoe City (2026-06-03): recommends reuse / bulk purchase estimates before bulky-waste disposal.
- Kawagoe City (2026-06-08): vacant-house bank for owners wanting to sell or rent.
- Kawagoe City (2026-09-27 event): seminar topics include inherited family homes and house-closing / demolition.

## Measurement / revenue blockers
Current `site_data.json` still has `offers: []` and empty `ga4_id`. Therefore affiliate CTA and GA4 event code cannot produce revenue/measurement yet. Do not fabricate ASP economics until actual approved offer URL, reward, conversion point and rejection terms are available.

## Next GSC test once connected
Query x page, last 28/90 days. Prioritize impressions with avg position 5-20 around:
- 実家 売却 片付け前
- 空き家 残置物 売却
- 実家 荷物 そのまま 売却
- 売れない 実家 処分
- 空き家 家財 撤去 売却

Improve only pages with demonstrated impressions/near-page-one potential before expanding geography.
