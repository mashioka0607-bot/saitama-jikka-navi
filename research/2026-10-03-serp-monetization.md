# 2026-10-03 SERP / monetization review

## Decision
Do not create thin municipality pages. Keep the primary intent cluster around **片付け前に出口を決める** and especially **残置物・家財を残した現況売却**.

## Fresh SERP evidence
- 縁リアルエステート: 「相続した空き家、そのままの状態で買い取ります」「残置物・家財はそのままで可」「解体・修繕・片付けは不要」。This confirms that users with inherited homes and remaining belongings are directly monetizable through a sale/appraisal path, not only a cleanup path.
  - https://en-re.jp/akiya
- さいたま市空き家相談専門店 A-HOME: inheritance + vacant-home sale consultation is a live local SERP competitor.
  - https://www.a-home-saitama.com/akiya-support/
- Homebank: 空き家・相続・実家じまい + 売却査定/買取 + 相続登記をワンストップで訴求。
  - https://home-bank.biz/

## Official primary sources checked
- 埼玉県「県内空き家の現状」(2026-09-04): 約356万戸の住宅、空き家約33.0万戸、利用目的のない空き家約13.6万戸（3.8%）。
  - https://www.pref.saitama.lg.jp/a1106/akiyataisaku1.html
- 埼玉県「空き家対策」(2026-09-28): 利用目的のない空き家約13万戸、20年で約1.8倍。県の3つのサポート体制を案内。
  - https://www.pref.saitama.lg.jp/a1106/akiyataisaku.html
- 埼玉県「住生活月間」(2026-10-01): 2026-10-01〜10-31。今月の鮮度ある一次情報として確認。
  - https://www.pref.saitama.lg.jp/a1107/news/page/news2026100101.html
- 市町村空き家バンク / 既存住宅流通促進ネットワークは引き続き公的な出口として有効。

## High-intent clusters to validate in GSC
1. 実家 片付け前 売却
2. 空き家 残置物 そのまま 売却 埼玉
3. 家財 そのまま 買取 埼玉
4. 相続 実家 売却 埼玉

Do not infer ranking without actual Search Console data. Expand content only when query/page data supports it.

## Site-quality finding (P0)
`build.py` still has a Kawagoe-only nav link, `Kawagoe / Inherited Home`, a Kawagoe-centered homepage description, and a Kawagoe-only public consultation block. This conflicts with the Saitama-wide site name and the monetization strategy. The next code change should remove the Kawagoe lock from global/home UI while retaining strong Kawagoe pages as a local cluster.

## Monetization / ASP
`site_data.json` still has `offers: []` and an empty `ga4_id`. Do not invent affiliate URLs or approval conditions. Connect the monetization CTA only after the actual approved program URL and conditions are available. The best-fit CTA placement remains after diagnosis when the user indicates sale / comparison intent, rather than showing an indiscriminate cleanup ad.
