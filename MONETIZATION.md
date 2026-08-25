# Monetization runbook

Updated: 2026-08-25

## Primary monetization path

1. TownLife Affiliate — Life Reset (遺品整理)
   - Publicly observed reward: 7,300 JPY (tax excluded) per approved result.
   - Target explicitly includes users who live far away and cannot attend the cleanup, which matches this site's main intent cluster.
   - Do not publish a guessed affiliate URL. Only insert the exact approved tracking URL after partnership approval.

2. Fallback / comparison candidates
   - BannerBridge — Life Reset: publicly observed reward 1,352 JPY; much weaker economics than TownLife, so use only if TownLife is unavailable.
   - Rentracks — WhiteRock (さいたま市): publicly observed reward 2,640 JPY, new application + identity confirmation; location fit is narrower than this Kawagoe-first site.
   - Rentracks — other 遺品整理 offers: evaluate individually for service area, approval point, cancellation policy and brand-search restrictions.

## Conversion architecture

Prioritize pages with request-stage intent rather than broad informational traffic:

- 見積書チェック / 追加料金条件
- 遠方・立ち会い不要
- 退去・売却期限あり
- 一般廃棄物の収集運搬方法
- 施設入居後の実家片付け
- 貴重品探索
- 買取相殺

When the primary offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- Keep lower-intent pages informational and route internally to the high-intent comparison pages.
- Track `affiliate_click` by page/context in GA4 before scaling traffic.
- Do not claim that an advertiser is a 川越市許可業者 unless verified from the municipality's current list.

## Legal / trust rule for Kawagoe

Kawagoe treats household cleanup waste as general waste. For temporary large quantities, the city plan points users to self-haul or designated/authorized general-waste collection carriers. The site should therefore ask users to confirm who actually transports disposal items and under what permit/contract arrangement.

This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
