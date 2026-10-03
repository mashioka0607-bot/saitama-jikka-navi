# 2026-10-03 SERP / monetization decision

## Decision change
Generic 「片付け前に査定」「4つの出口診断」「名義で停止」 is no longer a defensible differentiator. A current SERP competitor (家じまいガイド) now exposes almost the same sequence: pre-cleanup valuation, 4-exit diagnosis, registration stop, and cleanup decision.

Therefore Saitama Jikka Navi should NOT compete by cloning another generic diagnosis funnel.

## New moat: Saitama public-route decision layer
The product should answer one question better than generic national sites:

> 埼玉のこの実家は、民間査定へ送る前に、どの公的・準公的ルートを確認すべきか？

Use primary Saitama sources as the decision layer:
- 埼玉県「3つのサポート体制」
- 市町村空き家バンク（売りたい・貸したい所有者の出口）
- 埼玉県既存住宅流通促進ネットワーク（不動産・相続・金融の官民連携）
- 市町村ごとの補助・相談制度 only where a real program exists

Primary sources checked 2026-10-03:
- https://www.pref.saitama.lg.jp/a1106/akiyataisaku.html
- https://www.pref.saitama.lg.jp/a1107/akiyabanku.html
- https://www.pref.saitama.lg.jp/a1107/jyutaku-shienseido/network.html
- https://www.pref.saitama.lg.jp/a1106/akiyataisaku1.html

## Commercial funnel
1. ownership / family agreement unresolved -> STOP; public / professional information first
2. exit undecided -> compare public routes, keep/manage/use/sell
3. sell intent + ownership confirmed + family agreement confirmed -> commercial valuation CTA eligible
4. cleanup CTA only after the exit is chosen and cleanup is actually necessary

Do not place a valuation CTA merely because a visitor has an inherited/empty home.

## High-intent query cluster to validate in Search Console
Priority order after data is available:
1. 実家 売却 片付け
2. 実家じまい 埼玉
3. 空き家 残置物 売却 埼玉
4. 相続 実家 売却 埼玉
5. 空き家 片付ける前 売却

Promote queries/pages with impressions and average position roughly 8-30 before creating new geography pages. Diagnose CTR only after impressions are meaningful.

## Geography gate
No thin city-name mass production. A municipality page is allowed only when at least one is true:
- GSC shows meaningful local high-intent demand; or
- the municipality has a materially distinct primary-source program (bank/subsidy/consultation/disposal rule) that changes the user's decision.

## ASP gate
Public third-party information currently reports クラモア不動産売却 / afb at 4,230円（税込） per result, but this is NOT sufficient for production activation. Before adding an offer URL, verify inside the actual ASP/account:
- current reward
- exact conversion event
- approval/rejection conditions
- Saitama/property coverage
- prohibited traffic / wording

No unverified affiliate URL should be added to `site_data.json`.

## P0 implementation order
1. Remove Kawagoe-only framing from home hero/meta/navigation.
2. Replace Kawagoe-only public notice with the Saitama public-route decision layer.
3. Keep the diagnosis, but make its value the Saitama-specific next route rather than generic 3/4-exit logic.
4. Show commercial valuation CTA only for sell + title confirmed + family agreed/solo.
5. Add GA4/GSC measurement before expanding content inventory.

## Current primary-data anchor
Saitama Prefecture reports about 3.30M? NO: do not use this typo. Correct current figures from the prefecture page are approximately 3.56 million housing units, 330,000 vacant homes, and 136,000 vacant homes without a utilization purpose (3.8%). Always render figures from the cited prefectural source, not this note, if they are placed on-page.
