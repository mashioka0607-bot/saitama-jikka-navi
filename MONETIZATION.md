# Monetization runbook

Updated: 2026-08-26

## Primary monetization path

1. TownLife Affiliate — Life Reset (遺品整理)
   - Public comparison data currently shows Life Reset at 7,300 JPY (tax excluded) per result through TownLife, and explicitly lists people living far away who cannot attend estate clearance as a target. Treat this as public-reference data only; confirm the exact reward, result point, exclusions and approval window inside the logged-in ASP screen before publishing monetary claims.
   - Target fit remains strong for users who live far away and cannot attend the cleanup.
   - IMPORTANT: TownLife's public promotion guidance says that for article/site promotion, the page on which the TownLife product is planned to be introduced should be created before applying for program partnership. Therefore do not wait until approval to create the commercial-intent landing context. Prepare the relevant comparison/decision page first, but do not insert a guessed tracking URL or imply partnership before approval.
   - Do not publish a guessed affiliate URL. Only insert the exact approved tracking URL after partnership approval.

2. Adjacent monetization test — inherited/empty-home sale after cleanup
   - New SERP evidence on 2026-08-26 shows local real-estate content targeting `川越 実家 片付け 費用 払えない 売却 残置物`, including selling with contents left in place / financing disposal from sale proceeds.
   - TownLife's current company/service pages also list `タウンライフ空き家解決`, `タウンライフ遺品整理`, and a July 22, 2026 launch of `タウンライフメモリーマッチ`.
   - This creates a second revenue path with higher downstream value than cleanup alone: cleanup decision -> empty-home / inherited-home disposition. Research active affiliate programs and exact conversion conditions before implementing links.
   - Build this only as a decision page for users already facing sale/disposition; do not dilute the site into generic real-estate SEO.

3. Fallback / comparison candidates
   - BannerBridge — Life Reset: current public comparison data shows handling; economics must be rechecked inside the ASP before use.
   - Rentracks — multiple 遺品整理 offers: evaluate individually for service area, approval point, cancellation policy and brand-search restrictions.
   - Heart Service 13,200 JPY promotion: public affiliate database marks this promotion as ended. Do NOT plan monetization around it unless an ASP dashboard independently shows a currently active equivalent campaign.

## Conversion architecture

Prioritize pages with request-stage intent rather than broad informational traffic:

- 見積書チェック / 追加料金条件
- 「どこに頼む？」＋一般廃棄物の収集運搬確認
- 遠方・立ち会い不要
- 退去・売却期限あり
- `片付け費用が高い／払えない + 売却・残置物`（adjacent monetization test）
- 一般廃棄物の収集運搬方法
- 施設入居後の実家片付け
- 貴重品探索
- 買取相殺

Current SERP note (2026-08-26): broad `川越市 遺品整理` remains a poor first battlefield because local operators and large comparison sites dominate generic comparison intent. Do not publish another generic `おすすめ5選` clone. Win on decision quality: who transports household waste, what is included in the estimate, what happens to valuables, and what changes when there is a move-out/sale deadline.

New SERP note (2026-08-26): `片付け費用が払えない実家 + 売却/残置物` has explicit commercial content in the Kawagoe market. Treat this as a high-intent bridge between cleanup and property disposition. Before publishing, verify whether the recommended path is economically/legal appropriate and avoid claims such as `手出し0円` unless a specific provider's current written terms support it.

When the primary offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- Keep lower-intent pages informational and route internally to the high-intent comparison pages.
- Track `affiliate_click` by page/context in GA4 before scaling traffic.
- Do not claim that an advertiser is a 川越市許可業者 unless verified from the municipality's current list.
- Keep PR/ad disclosure adjacent to the commercial link and avoid unsupported superiority claims.

## Legal / trust rule for Kawagoe

Kawagoe's current official list was updated 2026-04-06 and is dated 2026-04-01. It identifies general-waste collection/transport permit holders and handled categories. The city explicitly says household-waste collectors need municipal permission and that industrial-waste permission, secondhand-dealer permission, or another municipality's general-waste permission does not by itself authorize collection of Kawagoe household waste. For cleanup/estate-clearance content, ask users to confirm who actually transports disposal items and under what permit/contract arrangement. This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

The current municipal list states 14 permit holders handle the `引越` category, defined as temporary large quantities of household waste such as from moving. The city FAQ also offers three routes for large quantities: direct facility drop-off, split disposal over time, or paid use of a permitted private operator.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
