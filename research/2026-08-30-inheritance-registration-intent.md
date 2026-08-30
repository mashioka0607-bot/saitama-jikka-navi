# Inherited-home registration blocker intent — 2026-08-30

## Decision
Treat `親名義のまま / 相続登記未了` as a bottom-of-funnel blocker, not as a reason to build a broad legal-content hub.

The monetization sequence should be:

1. Reader discovers the inherited home is still registered to the deceased parent.
2. Explain that inheritance registration has been mandatory since 2024-04-01 and point to Legal Affairs Bureau guidance / professional help for the legal procedure.
3. Keep the commercial decision alive in parallel: before paying for full clearance or demolition, compare whether the home can be sold/used with contents remaining once title issues are resolved.
4. Route sale/disposition intent to the primary empty-home comparison CTA once the approved affiliate tracking URL exists.

Do not imply that an affiliate service performs inheritance registration, and do not state that every old inheritance has the same deadline.

## Primary/local evidence

- Legal Affairs Bureau guidance (updated 2026-03-31) confirms inheritance registration became mandatory on 2024-04-01 and provides flows for inheritance registration, heir-declaration registration, legal-heir information and the national land-surrender system: https://houmukyoku.moj.go.jp/nagoya/page000489.html
- Kawagoe City provides free registration consultation: judicial scriveners handle consultations concerning inheritance-related real-estate registration; reservation required: https://www.city.kawagoe.saitama.jp/kurashi/sodan/1002247/1002253.html
- Kawagoe City also has a 2026-06-08 empty-home consultation partnership covering inheritance, management, rental, sale and demolition, which supports the site's existing `solve the blocker, then compare exits` architecture: https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1020433.html

## SERP observation
Current results for inherited-home/name problems include specialist inheritance/legal publishers and consultation businesses. This makes a generic `相続登記とは` page unattractive. The site's differentiator should remain the practical inherited-home decision immediately around cleanup/sale, with official local routes visible.

## GSC watch terms

- 実家 名義 親のまま 売却
- 相続登記してない 実家 売却
- 親名義の家 売却 相続
- 空き家 相続登記
- 川越 相続登記 相談
- 実家 売却 名義変更

## Build gate
Do not create a standalone article yet. If GSC shows impressions for these modifiers, first add a compact section to the existing high-intent sale/cleanup page. Only create a dedicated page if query evidence shows a distinct ranking opportunity and the page can add local primary-source value beyond generic legal explanation.
