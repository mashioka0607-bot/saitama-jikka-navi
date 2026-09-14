# 2026-09-14 SERP / CV gap review

## Decision
Do not add thin location pages. The highest-priority change is to connect the existing diagnosis to the existing high-intent page `kawagoe-shi/akiya-kazai-tekkyo` and make that page monetizable.

## Confirmed code gap
- `kawagoe-shi/akiya-kazai-tekkyo` exists in `data/pages.json`.
- It is absent from the `priority` array in `build.py`.
- Affiliate CTA insertion is limited to `priority[:5]`.
- The diagnosis can return `type='sale'`, but the result has no next-step CTA to the commercial page.
- `affiliate_click` and `diagnosis_complete` already exist, so the missing measurement is the diagnosis-to-next-page click.

## Next implementation
1. Move `kawagoe-shi/akiya-kazai-tekkyo` into the top five `priority` entries.
2. For diagnosis result `sale` with `items != clear`, show a CTA to `/kawagoe-shi/akiya-kazai-tekkyo/`.
3. Track the CTA as `diagnosis_next_click` with `diagnosis_result`, `items`, and destination.
4. Rewrite the page angle from generic removal to: `売却前に家財を全部片付けるべきか`.
5. Preserve the sequence: title/family agreement -> exit decision -> current-condition sale check -> valuables/reuse check -> only necessary disposal.

## SERP observation
Current competitors already cover whole-house cleanup, remote handling, purchase/reuse, and one-stop real-estate support. A generic `川越市 + 片付け` page is not enough differentiation. The site's stronger position is decision support before spending money on disposal.

## Primary-source support
川越市 currently provides: (a) an owner consultation route covering inheritance, management, rental, sale and demolition; (b) an empty-home bank for owners who want to sell or rent; (c) management cooperation with the Silver Human Resources Center; and (d) a 2026 empty-home countermeasure guide. This supports routing users by exit rather than sending everyone to a cleanup vendor.

## Search Console next test
Evaluate query x page for high-intent themes such as:
- 実家 売却 片付け前
- 空き家 残置物 売却
- 実家 荷物 そのまま 売却
- 空き家 家財 撤去 売却

Prioritize pages with impressions but weak CTR, and queries ranking roughly 5-20 before creating new content.

## ASP rule
Do not model revenue from third-party payout tables until the actual ASP dashboard confirms payout, conversion point, approval/denial rules, service area, and whether this site is eligible. Prefer exit-matched offers (sale / cleanup / management / hard-to-sell property) over a single generic cleanup CTA.