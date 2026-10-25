# Monetization runbook

Updated: 2026-10-26

## 2026-10-25 重要：idea社の公開案内に報酬額・成果確定時点の不一致（契約前検証必須）

**同一事業者による2026年10月25日現在の公式掲載内容に矛盾があるため、idea社案件の期待報酬と入金時期を確定値として扱わない。**

| 出所 | 仲介成立時・税込 | idea買取時 | 買取案件の報酬発生条件 |
|---|---|---|---|
| [idea公式パートナーLP](https://i-dea.co.jp/akiya-partner/)（2026-10-25閲覧、2026年8月改定と記載） | 1,000万円以下22万円／1,000万超3,000万円以下33万円／3,000万円超44万円 | 価格帯を問わず33万円 | idea社自身の買取決済完了。第三者転売を待たないと明記 |
| [idea社配信プレスリリース](https://www.rbbtoday.com/release/dreamnews/20260908/1352347.html)（2026-09-08、8月24日改定を告知） | 同22万円／33万円／55万円 | 仲介・買取とも価格帯別22万円／33万円／55万円と記載 | idea社が第三者に転売し、その決済が完了 |

**確認できたこと：** 現行LP内にも「仲介・買取を問わず同額」という説明と、価格帯によって買取欄が仲介欄と異なる表が同居している。プレスリリースの対象は遺品整理・不用品回収・生前整理事業者と明記される一方、現行LPはリフォーム・介護・葬祭等も例示している。**別契約・別プログラム、表示更新漏れ、規程改定のいずれかは未確定**。どちらか一方が当サイトに適用されると推定しない。

**次の具体的アクション（P0）:** idea社にSEOメディア単独の参加可否、対象業態・対象エリア、現行の委託契約書と情報提供料規程、価格帯別の適用額、idea買取案件で「直接買取決済」と「転売決済」のどちらが成果時点か、確定・支払・取消条件、事前接点/重複判定、書面同意のWeb運用可否、紹介文面事前承認の方法を**書面で確認**。署名・広告文面承認・本人同意導線の確定まで、個人情報収集フォームも紹介導線も公開しない。

**収益順位変更：** ideaを「最大44万円確定」等として優先投資せず、申込段階が成果地点のタウンライフ不動産相続／空き家解決（ただし個別提携承認・報酬規程・専用URL取得が必要）を短期収益の主軸とする。現時点の `site_data.json` は `offers: []`・`ga4_id: ""` であり、実際の承認成果およびGSCの直近28/90日データも未取得。推定と実績を混同しない。

---

## 2026-10-25 ASP再評価: 相続意図と空き家処分意図を分ける

**一次情報:** [タウンライフアフィリエイト公式のシリーズおすすめ案件](https://townlife-aff.com/townlife_recommended.html)（2026-10-25再確認）。「空き家解決」だけでなく「不動産相続」も、実家相続ニーズに合う成果地点が無料見積もり請求。

| 公式公開案件 | 公開税抜単価/成果 | 参考承認率 | 公開対象地域・年齢 | 向く検索意図（仮説） |
|---|---:|---:|---|---|
| タウンライフ不動産相続 | 12,000円 | 95% | 全国、30～70代 | 相続登記・遺産分割・税務・実家売却の相談 |
| タウンライフ空き家解決 | 10,000円（獲得手法別単価あり） | 約85% | 1都3県など、30～60代 | 空き家の現況売却・解体・活用のプラン比較 |

**2026-10-26 成果地点の重要な補足（一次確認）：** [タウンライフアフィリエイト公式の2026-09-15新案件案内](https://townlife-aff.com/info.php?id=6a9a6906ee0f3&type=news) は、不動産相続の成果地点を **「WEBからの無料見積もり・提案依頼完了（不動産会社2社以上選択）」** と明記している。したがって単純な「1社への無料相談・査定申込み」を成果としてカウントしてはならない。上表の参考単価・承認率は個別媒体への保証ではなく、**2社以上を選べる物件/地域であるか、士業のみの依頼が成果対象となるか**も未確認。管理画面でプログラムID・この追加条件・対象エリア/選択社数・有効リード定義・重複否認・個別報酬を一次確認するまで、実装も収益予測の確定も保留する。

**CV仮説への影響：** 所有権・遺産分割の相談と売却希望を混同せず、「2社以上比較する意思と選択可能性がある相続売却層」についてだけ不動産相続を候補とする。通常の現況査定・残置物処分/解体の比較には空き家解決を優先検証する。単価12,000円対10,000円だけで優先順位を決めず、実際のクリック→有効申込→承認収益（EPC）で比較する。正式な成果URL取得前に一般サービスURLを広告として設置しない。

公式の**参考承認率**と公開単価を機械的に掛けると、計上候補1件あたり期待承認額は不動産相続11,400円、空き家解決8,500円（いずれも税抜）という単純なシナリオになる。ただしこの計算は**同じ成果候補の定義、報酬単価の適用、公開承認率がこのサイトに再現される**と仮置きしたもので、サイトの実績/収益予測ではない。クリック→申込率や無効条件が異なるため、単価・承認率だけでは優劣は決められない。

**判断変更:** 「空き家解決」1本化を前提にせず、提携審査は「不動産相続」も並行確認する。名義/遺産分割/税の相談が主なら不動産相続、残置物を残した現況売却/解体/活用比較が主なら空き家解決へ出し分ける候補とする。売却/申込意図が確認できない読者には埼玉県の公的窓口を残す。**正式提携承認・当アカウントの単価・否認条件・指定文言・発行成果URLを取得するまでは、どちらも本番リンクに投入しない。**

最初の効果検証は、`/shindan/` と `/tedori-hikaku/` の intent 別 `cta_view`→`affiliate_click`→ASP承認成果/実報酬。GSCで「相続した実家 売却」「相続登記してない 実家 売却」対「残置物あり 売却」「片付け前 査定」をページ/クエリ別に観察する。GSC実測値・GA4 ID・正式ASP URLはいずれも未取得/未設定のため、導線実験はまだ開始できない。

---


## 2026-10-25 P0: idea株式会社の現行公式パートナー報酬を確認（旧試算を更新）

**公式一次情報**: https://i-dea.co.jp/akiya-partner/ （2026-10-25確認、ページ上「2026年8月に改定」）。同社の現行ページは、古い広報資料で扱った「9万〜35万円」「引越業者向け22万〜55万円」という分け方と一致しない。**公開案内が食い違うため、現行の書面契約条件の照合が最優先**で、以下はあくまで公開案内であり当サイトでの適用報酬ではない。

| 売買代金（消費税相当額除く） | 仲介成立時（税込） | idea社による買取（税込） |
|---|---:|---:|
| 1,000万円以下 | 220,000円 | 330,000円 |
| 1,000万円超〜3,000万円以下 | 330,000円 | 330,000円 |
| 3,000万円超 | 440,000円 | 330,000円 |

**成果地点は問い合わせや査定申込みではない。** ideaが媒介報酬全額を実際に受領、または同社買取の決済完了が必要。翌月末までの支払予定。本人による**書面同意**がない案件、事前接点・他経路が先の案件、紹介から12か月超の売買契約は対象外。解除・取消し・無効や媒介報酬返還時には既払報酬の返還可能性がある。提携には情報調査・提供業務の委託契約が必要。サイト上の紹介文は同社指定の文言を同じ画面の見やすい位置に載せ、**事前承認**が必要と案内されている。個人情報を取得・送付するフォームや紹介リンクを、契約・同意フローの確認なしに実装しない。

**重要な未確認点:** 現行のパートナー案内は遺品整理・リフォーム・介護・葬祭など現場の事業者向けであり、当サイトのような**純粋なSEOメディア/ウェブ送客の参加可否は未確認**。参加できない可能性がある。資格のない媒体が不動産売買を請け負うと誤解される広告も不可。現行報酬を「本サイトが必ず受け取れる」と説明しない。

**収益化の優先順位**:
1. 短期: タウンライフなど成果地点が査定申込のASPについて、管理画面で提携承認・成果条件・正式URLを確認。公表単価と当サイトの単価は分ける。
2. 並行: ideaへメディア運営者の参加可否、紹介手段・ウェブ文面事前承認、対象地域・物件条件、書面同意、重複案件、12か月制限、返還・税務処理、成果確定/支払を確認。**回答が取れるまで不動産ASPからの切替はしない。**
3. 検証: 問い合わせ→有効リード→査定→売買成立の月次コホートと承認報酬EPCを比較。単価だけで優劣を判断しない。例：ASP1万円/承認とidea33万円/成約なら、仮に同一有効リードでASP承認率85%、idea成約率2%なら期待報酬はそれぞれ8,500円と6,600円（説明用、実績ではない）。
4. SEO: 「相続した実家 売却 残置物」「片付け前査定」「残置物付き 現況買取」で「売る」意思がある検索から /tedori-hikaku/ に絞り、自治体の無料相談先と比較条件を併記。地名差替え量産をしない。

自治体一次情報の直近期限：川口市公式（2026-07-01更新）https://www.city.kawaguchi.lg.jp/soshiki/01130/040/akiyatoutaisaku/27633.html による2026年度の事前診断依頼期限は**10月30日**、交付申請期限は**11月13日**。予算到達で早期終了あり。受付中を保証せず、期限情報は年度をまたいで再確認する。

GSC/計測：直近28日・90日の query×page・表示回数・CTR・順位、特に /tedori-hikaku/ → 実査定比較の遷移、CTA表示→クリック→承認成果の欠損を確認する。現時点でGSCの実測値は確認できていないため検索需要は推定に留める。

---

## 2026-09-26 strategic update: one-stop property + contents sale is now a direct competitor

Fresh SERP review found a materially stronger competitor pattern: HOUSE REVO's `イエウリ` and Haseko-group `カシコシュ` launched `おうちまるごと買取`, covering Saitama as well as Tokyo/Kanagawa/Chiba. It combines real-estate purchase valuation with furniture/appliance/household-goods/estate-item appraisal, clearance and buyback in one window, explicitly selling the idea of maximizing the TOTAL economic outcome of real property + movable property rather than merely avoiding cleanup before sale.

Implication: `残置物そのまま売却` and even generic `手残り比較` are no longer sufficient moats by themselves. Do not imitate this with a thin “one-stop” landing page. Our defensible role should be the **neutral pre-contract audit before choosing any vendor**: ownership/inheritance readiness → likely exit → property value with contents remaining → movable-property value / clearance cost → brokerage vs purchase vs retain/rent → municipal/official alternatives → demolition/subsidy/asbestos/tax/rebuild checks → final net proceeds and irreversible-action warnings.

Conversion implication: `/tedori-hikaku/` should ultimately compare TOTAL net outcome, not just property sale price minus cleanup cost. The model should explicitly include (a) property proceeds, (b) separately recoverable contents value, (c) clearance/disposal cost, (d) brokerage/transaction cost, (e) carrying cost/time, and (f) demolition/repair only where actually required. This is a better trust position than pretending one commercial vendor is always optimal.

New GSC tests when data is available: `家ごと 家財ごと 売却`, `不動産 家財 一括買取`, `実家 家財 そのまま 売却`, `空き家 家財 買取 手残り`, `片付け費用 売却価格 比較`. If impressions appear, strengthen `/tedori-hikaku/` first; do not create city pages.

## 2026-09-26 strategic update: official free consultation is a real SERP/conversion competitor

Fresh Saitama primary-source review found two official routes that materially affect positioning:

- Saitama Prefecture's 2026 `空き家コーディネーター` is a **principally free** general consultation desk for Saitama vacant-home owners/prospective owners. It can propose concrete solution methods, introduce specialists, estimate necessary costs, and match owners with prospective users.
- Saitama Prefecture's `空き家の持ち主応援隊` lets owners search local real-estate businesses for management, sale, rental and demolition. As of 2026-03-31 it reports **359 registered businesses and 393 completed cases**, including 175 sales and 67 demolitions.

Implication: `空き家 どこに相談` / generic consultation intent is a weak place to force an affiliate CTA because a strong free official alternative exists. Do not try to beat government pages with generic “相談先まとめ” content. Our monetizable differentiation should be the **decision immediately before a costly/irreversible action**: should I sell with contents remaining, clear first, rent/retain, or demolish; what produces the best net outcome; and what must be checked before contracting.

Trust/conversion rule: on undecided/general-consultation intent, surface the prefectural coordinator or official local-business route as a neutral option. Reserve commercial valuation/referral CTAs for visitors showing clear sale/disposition intent. This should improve trust and reduce mismatched affiliate clicks rather than maximizing raw outbound clicks.

New GSC intent split to test when data is available:
- informational/official-intent: `空き家 どこに相談 埼玉`, `実家 空き家 相談 埼玉`, `空き家 コーディネーター 埼玉` → official route / no hard sell
- commercial-decision intent: `実家 片付けずに売る`, `残置物そのまま 買取`, `解体する前 査定`, `片付けてから売る どっち` → net-proceeds comparison + commercial CTA
Measure revenue per 1,000 organic sessions separately for these intent classes; do not judge them on CTR alone.

## ARCHIVE — 2026-09-26 idea partner payout scope (superseded by official 2026-10-25 check)

Historical September note; **do not use these older amounts for current forecasting**. Fresh source verification found an important scope distinction. idea株式会社's 2026-08-04 **multi-industry inheritance-vacant-home partner program** (葬儀・遺品整理・家財整理・リフォーム・解体・士業等) publicly states a success-based information fee of **90,000–350,000 JPY** and includes Saitama. A separate 2026-09-04 announcement for an **引越事業者向け** partner program states **220,000 / 330,000 / 550,000 JPY** according to sale price. Do NOT treat 220,000–550,000 JPY as the general website/media referral rate unless idea confirms in writing that this site/business qualifies for that program and those terms.

Implication: keep idea as a high-value direct-partnership candidate, but do not build revenue forecasts around 220k–550k. For this site's current position, the verified multi-industry public range is 90k–350k on completed sales; exact eligibility, media/site participation, consent/privacy flow, attribution, exclusions, and payment terms must be confirmed directly before implementation.

## 2026-09-25 strategic finding: municipality-backed calculators are now a SERP competitor

Fresh primary-source review found that Saitama municipalities are increasingly linking residents to Crassone's municipality-specific `すまいの終活ナビ`. Kazo City says its version provides demolition-cost estimates, post-demolition land-sale price estimates, a fixed-asset-tax simulator, and a nuisance-risk diagnosis. Fukaya City likewise officially promotes a tool that estimates demolition cost and land-sale price after its 2025-09-01 cooperation agreement with Crassone. A 2026-02 announcement says Crassone had agreements with 26 Saitama municipalities, covering 48.9% of the prefecture's population.

Implication: do NOT try to win `解体費用 相場 + 市名` by mass-producing generic city pages. Municipality-backed tools have stronger trust and useful calculators. Our defensible layer is the decision BEFORE demolition: contents-remaining valuation -> net-proceeds comparison -> subsidy/contract timing -> asbestos/permit checks -> only then demolition quote where needed. `/kaitai-check/` and `/tedori-hikaku/` should remain linked as one decision flow.

New high-intent tests: `解体する前 査定`, `解体してから売る どっち`, `空き家 解体費用 売却価格`, `実家 更地 売却 手残り`, `空き家 解体 補助金 契約前`. If GSC impressions emerge, improve the existing two tools first rather than creating municipality pages.

Trust rule: where a visitor's municipality offers an official/municipality-endorsed calculator, it may be shown as a neutral benchmark. Do not disguise an external commercial calculator as a government service, and do not sacrifice the user's net outcome merely to preserve an affiliate click.

## Primary monetization path

1. HIGHEST PRIORITY — TownLife Empty Home Solution (`タウンライフ空き家解決`)
   - CONFIRMED 2026-08-27 from TownLife Affiliate's official recommended-program page: conversion point = free estimate request; payout = 10,000 JPY per approved result (11,000 JPY tax-inclusive display); approval rate approximately 85%. Logged-in dashboard remains authoritative for exact account terms/tracking URL.
   - First monetization test: `片付け費用が高い/払えない + 売却/残置物` traffic.
   - Never insert a guessed tracking URL or imply partnership before approval.

2. DIRECT PARTNERSHIP CANDIDATE — idea株式会社 `相続空き家 多業種パートナー制度`
   - UPDATED 2026-10-25 against the **current official partner page** (https://i-dea.co.jp/akiya-partner/): Saitama is in scope; public schedule for intermediated sales is 220k / 330k / 440k JPY (incl. tax, by transaction value); if idea purchases directly, 330k JPY (incl. tax) regardless of value. It says amended in August 2026. These replace older publicity amounts for research purposes, NOT as an approved payout for this media site.
   - CONVERSION POINT IS CLOSED SALE, not a lead. Eligibility is limited by written subject consent, previous contact / duplicate channels, and 12-month deadline. Written agency agreement, approved site copy and consent workflow are mandatory. Whether a pure SEO publisher is eligible is **not verified**. No production lead form or referral link is authorized.
   - This remains materially higher-value than ordinary cleanup leads, but it is a B2B referral partnership rather than a normal click-based ASP program. Do not place a referral form/link or transmit owner information until a partnership agreement, consent flow, privacy handling, and exact qualification/payment conditions are confirmed.
   - Best-fit traffic if approved: `相続した実家を売りたい`, `売れない実家`, `残置物あり売却`, `片付け費用が高い`, `遠方の相続空き家` where the visitor has decided or strongly intends to sell.
   - Keep TownLife as the live-test priority until this direct agreement is actually signed and operational.

3. Estate-clearance offers
   - Use mainly on cleanup-first intent such as `遠方`, `見積`, `施設入居後`, `立会い不要`.
   - Logged-in ASP dashboard is authoritative for current payout/approval terms.

4. REUSE / BUYBACK — secondary micro-conversion, not the primary revenue path
   - Kawagoe City officially directs residents to consider reuse before disposing of bulky waste and specifically links to Market Enterprise's `おいくら` bulk appraisal service under its reuse partnership.
   - This creates a trust-first branch for `処分費を下げたい / 売れる物が分からない / 粗大ごみに出す前` visitors, but ONLY after sale/disposition intent is checked.
   - 2026-09-16 SERP review shows Saitama empty-home buyers explicitly competing on `家財ごとそのまま買取` / `残置物そのまま買取`. Therefore do not automatically strip or sell household contents before the property is valued when the owner intends to sell. Removing contents first can add work and may destroy the convenience/value proposition of a contents-included purchase.
   - Correct order for sale-intent users: secure documents/keepsakes → get property/disposition valuation with contents remaining → confirm whether buyer accepts/includes contents and how that affects net proceeds → only then separately appraise reusable items if economically useful → dispose/clear only the residual scope.
   - A 2026 third-party ASP survey reports consumer `おいくら` programs at roughly 253 JPY (afb) / 300 JPY (A8.net). Treat these amounts as UNCONFIRMED until the logged-in ASP dashboard is checked; do not publish or implement guessed tracking links.
   - Even if confirmed, the payout is too small to displace the higher-value empty-home/disposition path. Use it only where it reduces cleanup cost and increases trust/engagement.

## Conversion architecture

- FIRST QUESTION: likely exit = `売る方向 / まだ未定 / 残す・貸す`. This determines whether contents should be left in place for a property valuation before reuse/clearance.
- `片付け費用が高い／払えない + 売却・残置物` → PRIMARY: empty-home/disposition comparison with contents remaining
- `片付けずに売却 / 残置物あり売却 / 実家そのまま売却` → PRIMARY: disposition comparison before full clearance; explicitly compare contents-included purchase vs clear-then-sell on net proceeds/time, not headline price alone
- `売れない実家 / 空き家を手放したい / 不動産会社に断られた` → PRIMARY: re-check sale/purchase/other exits before irreversible demolition or disposal; SECONDARY: explain official last-resort routes accurately
- `相続登記前 / 名義変更前 + 実家売却・査定` → PRIMARY: explain that consultation/valuation can precede completion of every procedure, while legal completion requirements must be confirmed with the relevant professional; do not promise a sale can close before required registration.
- `2024-04-01以前の相続 + 親名義のまま` → DEADLINE-FIRST: show the official 2027-03-31 inheritance-registration deadline and route unresolved users to legal/official confirmation before irreversible work; if sale intent is already clear, valuation/disposition research may proceed in parallel without implying that closing can bypass required registration.
- `空き家 維持費 / 実家 持ち続ける 費用 / 固定資産税 + 管理` → PRIMARY: annual carrying-cost check, then disposition comparison
- `売るか貸すか迷う / しばらく使わない / 将来戻る可能性あり` → PRIMARY: compare sale with Saitama/Kawagoe official rental options before pushing a sale lead.
- `処分費を下げたい / 粗大ごみに出す前 / 売れる物が分からない` + NO near-term property sale → PRIMARY: official reuse-before-disposal path; SECONDARY: cleanup quote only for remaining scope
- `処分費を下げたい` + SALE intent → property valuation first; reuse/buyback only after confirming whether contents-included sale is preferable
- 退去・売却期限あり → empty-home CTA + cleanup CTA
- 空き家の家財撤去 → ask exit intent first; sale-intent = empty-home CTA before reuse/cleanup; cleanup-intent = reuse check + cleanup CTA
- 相続した空き家をどうするか → empty-home CTA
- 見積書チェック / 追加料金条件 → cleanup CTA
- 遠方・立ち会い不要 → cleanup CTA

## Current SERP direction

2026-09-26 fresh SERP review still shows commercial winners leading with `相続した空き家、そのまま`, `残置物・家財そのまま`, `片付け・解体前でも査定`, and free valuation CTAs. A stronger direct competitor now also bundles real-estate valuation with household-goods appraisal/clearance and explicitly markets total economic benefit. Therefore our moat is not “contents can remain”; it is neutral pre-contract decision quality and a more complete total-net-outcome comparison.

A notable 2026 competitor pattern is the rise of structured Saitama municipality-by-municipality demolition-subsidy databases and municipality-backed decision calculators. Do not answer this by mass-producing similar city pages. Only create a municipal page where official rules materially change the user's decision (application-before-contract deadline, eligibility, tax/rebuild consequence, or a unique official route) and there is measurable search demand or a monetizable downstream action.

The useful gap remains a decision framework immediately before spending money: ownership/inheritance check → decide likely exit → compare disposition with contents remaining → if selling, compare contents-included vs separate buyback/clearance on NET outcome → municipal/reuse options where appropriate → cleanup quotes only for necessary scope → demolition only after tax/rebuild/subsidy checks.

## TownLife approval gate

1. Planned placement pages: `/tedori-hikaku/`, `/kaitai-check/`, and high-intent sale/cleanup-cost pages only where the CTA matches intent.
2. Keep explicit PR disclosure near future commercial CTA.
3. Keep municipal/non-ad alternatives visible.
4. After approval, insert only the issued tracking URL.
5. Track `affiliate_click` by page/context/offer in GA4 before scaling traffic.

## Search / indexing status

Search Console URL Inspection / Pages report is the indexing source of truth; public `site:` checks are only supplementary.

Next GSC checks:
- indexed status of `/kawagoe-shi/katazuke-hiyou-urenai/`, `/tedori-hikaku/`, `/kaitai-check/`
- query-level impressions and CTR/title performance
- intent split: official/general consultation queries vs commercial decision queries; compare revenue per 1,000 organic sessions, not only CTR
- bundled-house/contents modifiers: `家ごと 家財ごと 売却`, `不動産 家財 一括買取`, `実家 家財 そのまま 売却`, `空き家 家財 買取 手残り`, `片付け費用 売却価格 比較`
- demolition-decision modifiers: `解体する前 査定`, `解体してから売る どっち`, `空き家 解体費用 売却価格`, `実家 更地 売却 手残り`, `空き家 解体 補助金 契約前`
- contents-included modifiers: `家財そのまま 売却`, `残置物そのまま 買取`, `実家 片付けずに売る`, `空き家 家財ごと 買取`, `片付けてから売る どっち`
- deadline/registration modifiers: `相続登記 2027年3月31日`, `実家 親名義のまま`, `昔の相続 名義変更`, `相続登記してない 実家 売却`, `相続登記 期限 実家`
- sale-intent modifiers: `相続した実家 売りたい`, `相続 空き家 売却 残置物`, `実家 売却 片付け前`, `売れない 相続空き家`, `遠方 相続実家 売却`

Do not infer rankings, CTR, or indexing from public search alone. Use actual GSC data before deciding whether a new standalone page is warranted.
