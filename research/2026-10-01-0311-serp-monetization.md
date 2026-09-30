# 2026-10-01 SERP / monetization check

## Decision
Do not publish more thin municipality pages. Keep the site focused on the decision immediately before disposal/sale.

## New SERP signal
A local Saitama operator (質KONDO) is now explicitly positioning around "実家整理" and "捨てる前に価値を見極める", including old watches, cameras, coins and tea utensils. This confirms that "valuable contents before bulk disposal" is a commercial-intent branch worth testing, but it should be integrated into the diagnosis rather than expanded into many city pages.

## High-intent queries to validate in Search Console
- 実家 片付け 買取 捨てる前
- 遺品 捨てる前 査定
- 実家 片付けずに売る
- 空き家 残置物 売却 埼玉
- 相続 共有名義 家 売却
- 再建築不可 相続 売却

Only build a dedicated page after impressions/query evidence appears; otherwise keep the topic inside /shindan/ and the core guide.

## Funnel
1. STOP: ownership / inheritance registration / co-heir agreement
2. VALUE CHECK: documents, valuables and items that should not be bulk-disposed
3. PROPERTY DIFFICULTY: access/rebuilding, shared ownership, leasehold, condition, remaining contents
4. EXIT: normal brokerage / as-is purchase / hold-use / public consultation
5. Only then: cleanup, purchase of contents, disposal and contractor comparison

This adds a value-preservation step before cleanup and gives the site a clearer reason to exist than generic cleanup-company comparison.

## ASP check
ASPLAY officially confirms a real-estate-focused performance affiliate network, but public pages do not expose campaign-level publisher payout/approval conditions. A third-party page reports Cramore/afb at JPY 4,230 incl. tax per result; do not put that number into production until confirmed inside the ASP dashboard.

## Primary public sources checked
- Saitama Prefecture vacant-home policy page, updated 2026-09-28: about 130k vacant homes without a utilization purpose; about 1.8x over 20 years.
- Saitama detailed statistics, updated 2026-09-04: 330k total vacant homes; 136k without a utilization purpose (3.8%).
- Saitama municipal vacant-home bank: public sell/rent exit remains available.

## Site-quality P0 still blocking growth
Current build.py still contains Kawagoe-specific global navigation, hero eyebrow, home description and municipal consultation copy. Fix those before publishing new content. Then connect GA4, one approved monetization offer, and validate query->page->diagnosis->affiliate_click.
