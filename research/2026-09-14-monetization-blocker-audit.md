# Monetization / measurement blocker audit — 2026-09-14

## Decision
Do not add thin location pages. The next growth task is not more content: the live generator currently has no configured affiliate offer and no GA4 measurement ID, so revenue and funnel validation are structurally blocked.

## Confirmed in current main
- `site_data.json` has `"offers": []`.
- `site_data.json` has `"ga4_id": ""`.
- `build.py` renders affiliate CTA only when a configured offer exists, therefore the current `offer_cta()` returns an empty string site-wide.
- `build.py` has event code for `affiliate_click` and `diagnosis_complete`, but with GA4 unset these events are not being sent to a configured GA4 property.
- The high-intent page `kawagoe-shi/akiya-kazai-tekkyo` exists but is not in the current `priority` list; monetization logic is also restricted to `priority[:5]`.

## SERP / intent observation
Current competitors increasingly bundle house clearing with resale, property sale, management and demolition. The defensible position remains: determine the home's exit before paying to clear everything. High-intent clusters to validate first:
- 実家 売却 片付け前
- 空き家 残置物 売却
- 実家 荷物 そのまま 売却
- 空き家 家財 撤去 売却
- 実家 売れない 処分

## Primary-source support
Kawagoe City currently provides:
- consultation covering inheritance, management, rental, sale and demolition;
- an empty-house bank for owners wishing to sell or rent;
- management support via the Silver Human Resources Center;
- a 2026 empty-house guide;
- an empty-house / inheritance event scheduled for 2026-09-27.
These support an exit-first decision architecture rather than indiscriminate cleanup lead generation.

## Revenue priority
1. Obtain and verify at least one real offer in the relevant ASP dashboard. Record payout, conversion point, approval/denial conditions, cookie/attribution terms, allowed traffic and prohibited claims. Do not publish guessed payout figures.
2. Configure the approved affiliate URL in `site_data.json` only after the program is verified.
3. Configure GA4 and Search Console ownership/data access. Without this, CTR/CVR prioritization is guesswork.
4. Then change the diagnosis so `sell + items remaining` routes to the high-intent `akiya-kazai-tekkyo` page, and measure `diagnosis_next_click` → `affiliate_click`.
5. Promote that page into the monetized priority set and rewrite it around the decision question: “Do I need to clear everything before selling?”

## GSC next checks once data is available
Evaluate query × page for the five high-intent clusters above. Prioritize pages with impressions and average position roughly 5–20, then pages with adequate impressions but weak CTR. After internal-funnel changes, compare diagnosis completion → next-page click → affiliate click.

## Guardrail
No new municipality/city pages until a page has a distinct decision intent, primary-source value, and a measurable revenue path. Geography alone is not sufficient justification.