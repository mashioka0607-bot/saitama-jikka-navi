# Monetization runbook

Updated: 2026-08-26

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED from TownLife Affiliate's public recommended-program page on 2026-08-26:
     - conversion: free estimate/request (`無料見積もり請求`)
     - payout: 10,000 JPY per approved result (11,000 JPY tax-inclusive display)
     - stated approval rate: about 85%
     - target includes Tokyo/Saitama/Chiba/Kanagawa, so Kawagoe is in target geography
     - note: payout can vary by acquisition method, so the logged-in program screen remains the final source before implementation
   - This is now the best verified monetization fit for the site's high-intent `片付け費用が高い/払えない + 売却/残置物` traffic.
   - TownLife also provides a diagnosis-version LP and form materials. After affiliate approval, prefer a context-matched landing path rather than a generic banner.
   - Prepare commercial-intent pages before applying; TownLife publicly instructs site publishers to create the planned placement page first, then apply for the program.
   - Do not insert a guessed tracking URL or imply partnership before approval.

2. Estate-clearance offers
   - Life Reset public comparison data currently shows a TownLife listing at 7,300 JPY (tax excluded), targeting users including people who live far from the property. Because third-party comparison data can lag, verify the exact logged-in reward, conversion point, exclusions, approval window and service area before implementing.
   - Use cleanup offers mainly on `遠方`, `見積`, `施設入居後`, `立会い不要` and similar cleanup-first intent.
   - Heart Service 13,200 JPY promotion was previously observed as ended. Do not plan around it unless a live ASP dashboard independently confirms a current equivalent.

## Conversion architecture

Prioritize request-stage intent rather than broad informational traffic:

- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: TownLife Empty Home Solution
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → empty-home CTA + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 「どこに頼む？」＋一般廃棄物の収集運搬確認 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA
- 施設入居後の実家片付け → cleanup CTA, then disposition CTA if home will become vacant
- 貴重品探索 / 買取相殺 → cleanup CTA

SERP note (2026-08-26): broad `川越市 遺品整理` remains a poor first battlefield because local operators and large comparison sites dominate generic intent. Do not publish another generic `おすすめ5選` clone. Win on decision quality: who transports household waste, what is included in the estimate, what happens to valuables, and what changes when there is a move-out/sale deadline.

SERP note (2026-08-26): `片付け費用が払えない実家 + 売却/残置物` has explicit commercial content in the Kawagoe market, including a 2026-04 local real-estate article directly targeting this problem. Treat this as the highest-value bridge between cleanup and property disposition.

When an offer is approved:

- Insert CTA above the fold only on the 3–5 highest-intent pages.
- For `片付け費用が高い/払えない`, `退去・売却期限`, and `空き家家財撤去`, test two distinct decisions rather than stacking generic ads: `片付け見積を比較` vs `片付け前に空き家の解決方法を無料比較`.
- For TownLife Empty Home Solution, test its diagnosis-version LP against the standard request LP if the dashboard provides both tracking links.
- Keep lower-intent pages informational and route internally to high-intent decision pages.
- Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.
- Do not claim an advertiser is a 川越市許可業者 unless verified from the municipality's current list.
- Keep PR/ad disclosure adjacent to commercial links and avoid unsupported superiority claims.

## Legal / trust rule for Kawagoe

Kawagoe's current official list was updated 2026-04-06. It shows 14 permit holders in the `引越` category for household waste temporarily generated in large quantities. Kawagoe's FAQ says such waste should be taken directly to a city facility, put out in smaller batches, or entrusted for a fee to a permitted private operator. For cleanup/estate-clearance content, ask users to confirm who actually transports disposal items and under what permit/contract arrangement. This is a trust differentiator, not a scare tactic. Avoid implying that every cleanup company itself must hold the collection permit if it lawfully coordinates with an authorized carrier.

## Search / indexing status

- Public Google results have surfaced the site homepage, so discovery has started.
- Do not spend another cycle debugging sitemap submission while pages are discoverable.
- Next Search Console checks: query-level impressions, indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`, and CTR/title performance.
- Next URL-inspection priority after the homepage: `/kawagoe-shi/katazuke-hiyou-urenai/`, because it now maps to the strongest verified payout path.
- Use URL inspection requests selectively rather than bulk submission.

## Go / no-go checkpoints

Do not add thin city-name pages before data arrives.

Scale only after at least one of the following appears:

- Search Console impressions on high-intent Kawagoe queries.
- Affiliate approval and measurable outbound clicks.
- A page begins ranking within roughly top 30 for a commercial-intent query.

If there are impressions but poor CTR, rewrite titles/descriptions before adding more content. If there are clicks but no affiliate conversions, change offer/CTA before expanding page count.
