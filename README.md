# 埼玉実家片付けナビ

遠方からの実家片付け・遺品整理について、自治体一次情報と依頼直前の検索意図を軸に検証するSEO MVPです。

## Cloudflare Pages
- Framework preset: None
- Build command: `python deploy.py`
- Build output directory: `dist`
- Root directory: `/`

## 方針
- 「遺品整理 おすすめ」の正面勝負は避ける
- 遠方 / 立ち会い不要 / 鍵預かり / 一軒家 / 退去期限 / 貴重品探索 / 許可・廃棄物ルールを優先
- 地名だけを差し替えた量産ページは作らない
- ASP承認までは広告リンクを無効化
- 公開後はSearch Consoleの実クエリを基に増強・撤退判断をする

## 公開後に更新するもの
`site_data.json` の以下を更新します。
- `base_url`: Cloudflare Pagesの本番URL
- `ga4_id`: GA4導入時
- `offers[].url`: ASP承認後の専用URL
- `contact_email`: 必要に応じて

## ローカルビルド
```bash
python deploy.py
```

`build.py` は基本ページの生成のみです。`deploy.py` は SEO 品質チェック、手取り比較・解体チェックなどの静的ページの統合、サイトマップ・robots・Search Console 検証ファイルの検査まで実施します。本番の Cloudflare Pages でも必ず `python deploy.py` を使用してください。

## ASP正式提携の最短手順（2026-10-27・公式情報確認）

未提携のまま仮の広告リンクや一般サービスURLを成果リンクとして公開しない。公開用データの `offers: []` は正規の成果URL取得まで維持する。

1. [タウンライフアフィリエイト公式・登録手順](https://townlife-aff.com/lp/how_to_start/)を起点に、運営主体の正確な氏名・住所・生年月日（法人の場合は法人情報）、振込先、当サイトURLを用意し、運営者自身が媒体登録を申請する。口座情報やパスワードを公開リポジトリ・GitHub issue・チャットに貼らない。
2. 公式案内による媒体審査の目安は**5営業日以内**。登録承認後、**案件ごとに別途提携申請**する。公式の[広告掲載フロー](https://townlife-aff.com/post_flow.html)では、案件の提携審査も原則**5営業日以内が目安**（自動承認案件は例外）。承認や成果は保証されない。
3. まず「空き家解決」診断版／売却査定特集を、相続・名義課題では「不動産相続」を候補にする。正式な**成果地点、対象地域・物件条件、否認・重複条件、媒体別単価、LP別の承認済みトラッキングURL**を管理画面で確認し、媒体・案件審査の結果に応じて選ぶ。[公式シリーズ案件一覧](https://townlife-aff.com/townlife_series.html)は一般公開の候補確認用であり、掲載許諾や当サイトの成果条件を意味しない。
4. 正式承認後に `site_data.json > offers` に専用URLを設定し、GA4で `cta_view`→`affiliate_click`、ASP側で承認成果・実報酬を照合する。GSCの検索意図別の検証は下記手順で行う。

**優先順位**：問い合わせメールへの返信待ちを開始条件にせず、公式の媒体登録→案件提携申請→正規成果リンク取得を先に進める。本人確認や銀行情報が必要な登録は運営者の作業。会員向けの個別条件は公開ドキュメントに転載しない。

## GSC実績の取得（標準画面だけでもページ別に監査可能）

Search Console標準画面の「クエリ」と「ページ」は通常**別々のCSV**であり、2つを機械的に結合してquery×pageを推定してはいけません。APIでは `dimensions: ["query", "page"]` で同時取得できますが、認証設定は未導入です。

**GSCの画面で行う場合**：検索パフォーマンス（検索結果）→期間を過去28日（または90日）→「＋新規」→「ページ」→「URLが次と完全一致」→ `https://saitama-jikka-navi.pages.dev/tedori-hikaku/` を指定→「クエリ」タブ→エクスポート→ `Queries.csv` を保存。その後、手元で次を実行します。

```bash
python scripts/audit_gsc_csv.py Queries.csv --window 28 --page-filter https://saitama-jikka-navi.pages.dev/tedori-hikaku/ --json report_tedori_28.json
```

`/kaitai-check/` と90日についても**ページフィルタを切り替えてから**別々にエクスポートしてください。**フィルタなしのクエリCSVへ `--page-filter` を指定してはいけません。** スクリプトはGSC画面のフィルタ状態を検証できず、ページの紐付けは操作者の申告として警告を表示します。GSC自体へのAPI接続・実測値取得を行うものではありません。Google公式：[パフォーマンスレポート](https://support.google.com/webmasters/answer/7576553) / [高度なフィルタ](https://support.google.com/webmasters/answer/17011165) / [Search Analytics API](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)。

**データ帰属の安全確認**：監査ツールは `site_data.json > base_url` と異なるドメインのページ行・完全一致フィルタを拒否します。`?` 付きURLの行も、同じパスへ合算して誤認しないため拒否します。GSCの対象プロパティ、正規URL、エクスポート対象を確認し、サイト移転時は `base_url` を更新してから分析してください。CSVから本当のGoogleインデックス状況は判定できません。
