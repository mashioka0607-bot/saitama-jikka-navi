# Monetization runbook

Updated: 2026-08-26

## Primary monetization path

1. TownLife Affiliate — Life Reset (遺品整理)
   - Public comparison data still shows TownLife as a current handling ASP for Life Reset; confirm the exact reward and approval condition inside the logged-in ASP screen before publishing claims.
   - Target fit remains strong for users who live far away and cannot attend the cleanup.
   - Do not publish a guessed affiliate URL. Only insert the exact approved tracking URL after partnership approval.

2. Fallback / comparison candidates
   - BannerBridge — Life Reset: current public comparison data shows handling; economics must be rechecked inside the ASP before use.
   - Rentracks — multiple 遺品整理 offers: evaluate individually for service area, approval point, cancellation policy and brand-search restrictions.
   - Heart Service 13,200 JPY promotion: public affiliate database now marks this promotion as ended. Do NOT plan monetization around it unless an ASP dashboard independently shows a currently active equivalent campaign.

## Conversion architecture

Prioritize pages with request-stage intent rather than broad informational traffic:

- 見積書チェック / 追加料金条件
- 「どこに頼む？」＋一般廃棄物の収集運搬確認
- 遠方・立ち会い不要
- 退去・売却期限あり
- 一般廃棄物の収集運搬方法
- 施設入居後の実家片付け
- 貴重品探索
- 買取相殺

Current SERP note (2026-08-26): broad `川越市 遺品整理` is crowded by local operators and large comparison sites. Mitsumoa exposes hundreds of nearby providers and review/price comparison; EPARK and operator-owned list pages also target the generic comparison intent. Do not respond by publishing another generic `おすすめ5選` clone. Win on decision quality: who transports household waste, what is included in the estimate, what happens to valuables, and what changes when there is a move-out/sale deadline.

When the primary offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- Keep lower-intent pages informational and route internally to the high-intent comparison pages.
- Track `affiliate_click` by page/context in GA4 before scaling traffic.
- Do not claim that an advertiser is a 川越市許可業者 unless verified from the municipality's current list.

## Legal / trust rule for Kawagoe

Kawagoe's current official list (updated 2026-04-06; list dated 2026-04-01) identifies general-waste collection/transport permit holders and their handled categories. The city's facilities also accept eligible household waste by self-haul; current posted household processing fee is 50 JPY per 10 kg, subject to excluded items and facility rules.

For cleanup/estate-clearance content, ask users to confirm who actually transports disposal items and under what permit/contract arrangement. This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
