# 埼玉実家片付けナビ

遠方からの実家片付け・遺品整理について、自治体一次情報と依頼直前の検索意図を軸に検証するSEO MVPです。

## Cloudflare Pages
- Framework preset: None
- Build command: `python build.py`
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
python build.py
```
