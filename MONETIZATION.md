# Monetization runbook

Updated: 2026-08-26

## Primary monetization path

1. TownLife Affiliate / estate-clearance offers
   - IMPORTANT CORRECTION (2026-08-26): do not use the previously recorded 7,300 JPY Life Reset figure in forecasts or public copy. Fresh public affiliate-comparison data currently shows Life Reset at 2,255 JPY through Rentracks and 1,352 JPY through BannerBridge; another Life Reset special-cleaning listing is 977 JPY. The exact TownLife logged-in reward for the estate-clearance offer is not publicly verified in this run.
   - TownLife remains strategically relevant because its current company pages list both estate-clearance and empty-home services, and it launched TownLife Memory Match on 2026-07-22 as a free comparison service matching users with up to three estate-clearance providers.
   - Treat every payout as unverified until confirmed in the logged-in ASP program screen. Record exact reward, conversion point, exclusions, approval window, service area and paid-search restrictions before implementing.
   - TownLife's public promotion guidance says article/site promotion should have the planned product-introduction page prepared before partnership application. Prepare the commercial-intent page first, but do not insert a guessed tracking URL or imply partnership before approval.

2. Adjacent monetization test — inherited/empty-home sale after cleanup
   - Current Kawagoe SERP contains explicit commercial content targeting `片付け費用が払えない実家 + 売却 + 残置物`, including sale with contents remaining. This confirms demand at the cleanup-to-sale decision boundary.
   - TownLife's current service portfolio includes `タウンライフ空き家解決` as well as estate-clearance services. This supports testing a second revenue path: cleanup decision -> inherited/empty-home disposition.
   - Build only decision content for users already facing sale/disposition; do not dilute the site into generic real-estate SEO.
   - Never repeat provider claims such as `手出し0円` as general advice unless current written terms for that specific provider support the claim.

3. Current comparison candidates
   - Rentracks — Life Reset: public comparison data currently shows 2,255 JPY. Verify inside ASP before use.
   - BannerBridge — Life Reset: public comparison data currently shows 1,352 JPY; conversion requires a new web estimate application and identity confirmation within two days, with Saitama included in the service area. Verify inside ASP before use.
   - Rentracks — White Rock: public comparison data shows 2,640 JPY, focused on Saitama City / Saitama residents. Lower fit for Kawagoe, so do not force it into Kawagoe pages unless service coverage is confirmed.
   - Heart Service 13,200 JPY promotion: previously observed as ended. Do not plan around it unless a live ASP dashboard independently confirms a current equivalent.

## Conversion architecture

Prioritize request-stage intent rather than broad informational traffic:

- 見積書チェック / 追加料金条件
- 「どこに頼む？」＋一般廃棄物の収集運搬確認
- 遠方・立ち会い不要
- 退去・売却期限あり
- `片付け費用が高い／払えない + 売却・残置物`
- 一般廃棄物の収集運搬方法
- 施設入居後の実家片付け
- 貴重品探索
- 買取相殺

SERP note (2026-08-26): broad `川越市 遺品整理` remains a poor first battlefield because local operators and large comparison sites dominate generic intent. Do not publish another generic `おすすめ5選` clone. Win on decision quality: who transports household waste, what is included in the estimate, what happens to valuables, and what changes when there is a move-out/sale deadline.

SERP note (2026-08-26): `片付け費用が払えない実家 + 売却/残置物` has explicit commercial content in the Kawagoe market. Treat this as a high-intent bridge between cleanup and property disposition.

When an offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- Keep lower-intent pages informational and route internally to high-intent decision pages.
- Track `affiliate_click` by page/context in GA4 before scaling traffic.
- Do not claim an advertiser is a 川越市許可業者 unless verified from the municipality's current list.
- Keep PR/ad disclosure adjacent to commercial links and avoid unsupported superiority claims.

## Legal / trust rule for Kawagoe

Kawagoe's current official list was updated 2026-04-06 and is dated 2026-04-01. It identifies general-waste collection/transport permit holders and handled categories. For cleanup/estate-clearance content, ask users to confirm who actually transports disposal items and under what permit/contract arrangement. This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
