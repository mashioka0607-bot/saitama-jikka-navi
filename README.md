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

## GSC実績の取得（標準画面だけでもページ別に監査可能）

Search Console標準画面の「クエリ」と「ページ」は通常**別々のCSV**であり、2つを機械的に結合してquery×pageを推定してはいけません。APIでは `dimensions: ["query", "page"]` で同時取得できますが、認証設定は未導入です。

**GSCの画面で行う場合**：検索パフォーマンス（検索結果）→期間を過去28日（または90日）→「＋新規」→「ページ」→「URLが次と完全一致」→ `https://saitama-jikka-navi.pages.dev/tedori-hikaku/` を指定→「クエリ」タブ→エクスポート→ `Queries.csv` を保存。その後、手元で次を実行します。

```bash
python scripts/audit_gsc_csv.py Queries.csv --window 28 --page-filter https://saitama-jikka-navi.pages.dev/tedori-hikaku/ --json report_tedori_28.json
```

`/kaitai-check/` と90日についても**ページフィルタを切り替えてから**別々にエクスポートしてください。**フィルタなしのクエリCSVへ `--page-filter` を指定してはいけません。** スクリプトはGSC画面のフィルタ状態を検証できず、ページの紐付けは操作者の申告として警告を表示します。GSC自体へのAPI接続・実測値取得を行うものではありません。Google公式：[パフォーマンスレポート](https://support.google.com/webmasters/answer/7576553) / [高度なフィルタ](https://support.google.com/webmasters/answer/17011165) / [Search Analytics API](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)。

