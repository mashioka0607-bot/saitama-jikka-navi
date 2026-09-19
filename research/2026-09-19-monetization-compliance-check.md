# 2026-09-19 monetization / compliance check

## Decision
Do not create more municipality pages. The next revenue step is to activate the already-identified TownLife Empty Home Solution offer after account approval and insert it into the existing high-intent decision flow.

## Official ASP confirmation (checked 2026-09-19)
TownLife Affiliate's public recommended-program page currently lists `タウンライフ空き家解決` with:
- conversion: free estimate request
- payout: 10,000 JPY per result (11,000 JPY tax-inclusive display)
- note: payout can vary by acquisition method
- approval rate: approximately 85%
- target: ages 30–60, including the Tokyo metropolitan 1-to-3 prefecture area (therefore Saitama is in the published target area)
- positioning: users can receive and compare multiple solution plans such as sale, demolition, and renovation

Source: https://townlife-aff.com/townlife_recommended.html

The same official site says an affiliate must apply for a program and receive advertiser approval before placing the ad. Never invent a tracking URL.
Source: https://townlife-aff.com/beginner.html

## Important compliance finding
TownLife's official PR guidance requires TWO PR disclosures for pages carrying TownLife-series advertising:
1. `[PR]` in the first view, e.g. near the article title/top;
2. another `[PR]` at an arbitrary location within the article.
After adding the disclosures, TownLife asks partners to notify its affiliate office.
Source: https://townlife-aff.com/lp/pr_sample/

Implementation gate: when the real approved tracking URL is added, implement both PR placements at the same time. A single disclosure beside the CTA is not enough under TownLife's published guidance.

## Current site blocker
`site_data.json` still has `affiliate_url: ""`, `offers: []`, `ga4_id: ""`, and `contact_email: ""` as of this check. Therefore:
- revenue attribution is not live;
- commercial CTA testing is not live;
- GA4 event analysis is not live;
- a public contact route is still absent from config, which should be fixed before/alongside monetization for trust and accountability.

Do not fabricate any of these values. They require real account/configuration data.

## Revenue architecture
Highest-value existing flow remains:
`相続した実家 / 空き家` → decide likely exit → compare as-is vs clear-then-sell net proceeds → show legitimate municipal/non-ad alternatives → if sale/disposition intent is high, show approved TownLife CTA → measure CTA click and approved lead economics.

Use `/tedori-hikaku/` as the pre-CV decision asset. Do not turn it into a biased ad calculator; the affiliate destination should come after the neutral comparison result.

## SERP / keyword direction
Continue testing decision-stage terms rather than generic city-name cleanup terms:
- 空き家 売却 解体 どっち
- 空き家 解決策 比較
- 実家 売却 片付ける前
- 残置物 そのまま 売却
- 仲介 買取 手残り
- 空き家 解体費用 売却

TownLife itself publicly identifies `空き家`, `空き家問題`, `解決策`, `解体費用`, `売却`, `活用方法`, `おすすめ`, `比較` as effective keyword families. Treat that as commercial-intent evidence, not as permission to keyword-stuff or mass-produce thin pages.

## Primary-source freshness
Saitama Prefecture's 2026-09-04 page reports about 330,000 vacant homes statewide and about 136,000 vacant homes without a use purpose, the latter up about 12,000 from the previous survey. The prefecture's current vacant-home page also advertises the 2026-09-27 vacant-home/inheritance problem-solving event.
Sources:
- https://www.pref.saitama.lg.jp/a1106/akiyataisaku1.html
- https://www.pref.saitama.lg.jp/a1106/akiyataisaku.html

## GSC next check
Before publishing another standalone article, inspect whether impressions/clicks are already appearing for the decision-stage clusters above and which existing URL receives them. Improve that URL first. If `/tedori-hikaku/` gets impressions but weak CTR, test title/meta intent match; if it gets no impressions, strengthen contextual internal links from the strongest sale/cleanup-cost pages before creating more content.
