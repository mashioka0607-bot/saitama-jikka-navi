# 2026-09-18 SERP gap: full cleanup should not precede sale-method check

## Decision
For users who may sell an inherited home, do **not** present full household-goods removal as the default step before deciding the sale route.

Recommended decision order:
1. Preserve valuables / documents / keepsakes.
2. Confirm title / family decision-makers.
3. Get an as-is valuation and confirm whether the likely route is brokerage or direct purchase.
4. Compare expected net proceeds: brokerage after cleanup vs. purchase with remaining contents vs. hold/manage.
5. Only then pay for the cleanup scope that is actually necessary.

## Why this changed
Fresh SERPs in September 2026 are converging on this exact high-intent question. A new 2026-09-14 competitor page explicitly states that appraisal can happen before cleanup and recommends `appraisal -> sale method -> cleanup scope -> handover`. Other competitors similarly say remaining household goods can sometimes stay for direct purchase, while brokerage generally requires an empty handover.

A competing information site currently describes the broad flow as `family decision -> sort -> junk/estate cleanup -> decide hold or sell`, which leaves a useful differentiation opportunity: **decide the exit before paying to empty the house**.

## Existing-site correction to make
`data/pages.json` contains `kawagoe-shi/akiya-kazai-tekkyo` with an `おすすめの順番` that currently ends in `室内清掃 -> 売却・解体への引き渡し`. This can imply cleanup before sale-route confirmation. Revise that page so sale-method / as-is appraisal comparison occurs before full removal and cleaning.

Suggested section:
- Important documents / keepsakes
- Identify items worth reselling
- If sale is possible, obtain an as-is appraisal before bulk disposal
- Compare brokerage (usually empty handover) vs direct purchase (remaining contents may be accepted) and expected net proceeds
- Decide only the required cleanup scope
- Use municipal rules / licensed haulers for disposal

## Monetization implication
The highest-value user is not necessarily someone ready to hire a cleanup company. A user about to spend 150k-300k+ on removal may first be a real-estate valuation lead. Route sale-intent users to the valuation offer first once a verified tracking URL is available. Keep cleanup / reuse / municipal disposal as secondary paths.

## GSC queries to validate next
- 実家 売る前 片付け
- 実家 片付け前 査定
- 片付けずに売る 実家
- 残置物 そのまま 売却
- 空き家 片付け前 査定
- 仲介 買取 片付け どっち

Do not create city-name variants until query impressions justify them.
