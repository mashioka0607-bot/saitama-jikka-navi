#!/usr/bin/env python3
"""Audit an *exported* Search Console query CSV; never fabricate live metrics.

Usage:
  python scripts/audit_gsc_csv.py exports/queries_28d.csv --window 28
  python scripts/audit_gsc_csv.py exports/query_page_90d.csv --window 90 --json report.json

Accepts Japanese or English column headers. A query-only export can rank
queries/clusters, but CANNOT determine which landing page received the query:
page-specific suggestions require query+page rows in the same file.
Only local CSV data are processed; no credentials, network calls, or PII.

The standard GSC UI exports Queries and Pages as separate tables. To audit a
specific landing page without API credentials, apply the GSC *exact page* filter
BEFORE exporting the Queries table, then supply the exact URL with --page-filter.
The CSV does not prove which filter was used; this is an explicitly labeled
manual assertion, never an inferred sitewide query/page join.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

HEADERS = {
    "query": ("query", "queries", "上位のクエリ", "検索クエリ", "クエリ"),
    "page": ("page", "pages", "上位のページ", "ページ"),
    "clicks": ("clicks", "クリック数", "クリック"),
    "impressions": ("impressions", "表示回数", "表示"),
    "position": ("position", "掲載順位", "平均掲載順位", "平均順位"),
}
# First matching class wins. These are hypotheses, not keyword-volume estimates.
CLUSTERS = (
    ("片付け前・残置物あり売却", "/tedori-hikaku/",
     re.compile(r"(?:片[付づ]け|残置物|家財).*(?:売|買取|査定)|(?:売|買取|査定).*(?:片[付づ]け|残置物|家財)")),
    ("解体前・補助金判断", "/kaitai-check/",
     re.compile(r"解体|除却|更地")),
    ("相続した実家の売却", "/shindan/",
     re.compile(r"相続.*(?:実家|家|売|登記|名義)|実家.*(?:売|相続)")),
)


def _column(fieldnames: list[str], key: str) -> str | None:
    aliases = {name.casefold() for name in HEADERS[key]}
    return next((name for name in fieldnames if name.strip().casefold() in aliases), None)


def _number(value: str | None) -> float:
    s = (value or "").strip().replace(",", "").replace("％", "%")
    if s.endswith("%"):
        return float(s[:-1]) / 100
    return float(s) if s else 0.0


def _path(value: str) -> str:
    if not value:
        return ""
    parsed = urlparse(value.strip())
    path = parsed.path if parsed.scheme and parsed.netloc else value.split("?")[0]
    return "/" + path.strip("/") + ("/" if path.strip("/") else "")


def attach_page_filter(rows: list[dict], has_page: bool, filter_url: str) -> tuple[list[dict], bool]:
    """Bind a query-only CSV to an explicitly asserted GSC exact-page filter.

    This is ONLY valid if the operator set the same exact page filter in GSC
    before exporting Queries.csv. The CSV cannot prove the filter was set.
    """
    if has_page:
        raise ValueError("--page-filter cannot be used with an export containing a Page column")
    parsed = urlparse(filter_url.strip())
    if parsed.scheme != "https" or not parsed.hostname or not parsed.path.startswith("/"):
        raise ValueError("--page-filter requires the full HTTPS page URL used in GSC")
    if parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError("--page-filter must be a clean exact page URL without credentials, query or fragment")
    page = _path(filter_url)
    return ([dict(row, page=page) for row in rows], True)


def read_export(path: Path) -> tuple[list[dict], bool]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames or []
        columns = {key: _column(fields, key) for key in HEADERS}
        missing = [key for key in ("query", "clicks", "impressions", "position")
                   if columns[key] is None]
        if missing:
            raise ValueError("Missing Search Console columns: " + ", ".join(missing) +
                             ". Query-only or query+page export required; "
                             "a page-only CSV cannot support query intent analysis.")
        result = []
        for line, raw in enumerate(reader, 2):
            query = (raw.get(columns["query"]) or "").strip()
            if not query or query.lower() in ("total", "合計"):
                continue
            try:
                impressions = int(_number(raw.get(columns["impressions"])))
                clicks = int(_number(raw.get(columns["clicks"])))
                position = _number(raw.get(columns["position"]))
            except (ValueError, TypeError) as exc:
                raise ValueError(f"Invalid Search Console metric at CSV line {line}") from exc
            if impressions < 0 or clicks < 0 or clicks > impressions or position < 0:
                raise ValueError(f"Impossible Search Console metric at CSV line {line}")
            if impressions == 0:
                continue
            page = _path(raw.get(columns["page"]) or "") if columns["page"] else ""
            result.append({"query": query, "page": page, "clicks": clicks,
                           "impressions": impressions, "position": position})
    return result, bool(columns["page"])


def classify(query: str) -> tuple[str, str]:
    normal = re.sub(r"\s+", "", query).casefold()
    for name, target, pattern in CLUSTERS:
        if pattern.search(normal):
            return name, target
    return "その他・未分類", ""


def analyze(rows: list[dict], has_page: bool, window: int, source_kind: str = "csv") -> dict:
    groups: dict[str, dict] = defaultdict(lambda: {
        "clicks": 0, "impressions": 0, "position_weighted": 0.0, "queries": set(),
        "pages": set(), "target": "",
    })
    # Query intent may land on multiple different URLs. Keep the observed
    # query×page pairs separate: aggregate cluster averages cannot identify
    # which *actual* page should be rewritten.
    page_groups: dict[tuple[str, str], dict] = defaultdict(lambda: {
        "clicks": 0, "impressions": 0, "position_weighted": 0.0,
        "queries": set(), "suggested_target": "",
    })
    for row in rows:
        name, target = classify(row["query"])
        group = groups[name]
        group["clicks"] += row["clicks"]
        group["impressions"] += row["impressions"]
        group["position_weighted"] += row["impressions"] * row["position"]
        group["queries"].add(row["query"])
        if has_page and row["page"]:
            group["pages"].add(row["page"])
        group["target"] = target
        if has_page and row["page"]:
            page_group = page_groups[(name, row["page"])]
            page_group["clicks"] += row["clicks"]
            page_group["impressions"] += row["impressions"]
            page_group["position_weighted"] += row["impressions"] * row["position"]
            page_group["queries"].add(row["query"])
            page_group["suggested_target"] = target

    clusters = []
    for name, g in groups.items():
        impressions = g["impressions"]
        ctr = round(g["clicks"] / impressions, 5)
        position = round(g["position_weighted"] / impressions, 2)
        # 50 impressions and 8–20 position are a triage rule, NOT a
        # statistically validated CTR benchmark or automatic new-page trigger.
        rewrite = (name != "その他・未分類" and impressions >= 50
                   and 8 <= position <= 20 and ctr < 0.02)
        clusters.append({
            "cluster": name, "target": g["target"], "clicks": g["clicks"],
            "impressions": impressions, "ctr": ctr, "average_position": position,
            "query_count": len(g["queries"]), "observed_pages": sorted(g["pages"]),
            "action": "既存ページのtitle・導入・内部リンクを優先検証" if rewrite
                      else "継続観測（新規記事量産は保留）",
            "priority": "rewrite" if rewrite else "observe",
        })
    clusters.sort(key=lambda c: (c["priority"] != "rewrite", -c["impressions"]))
    page_intents = []
    for (name, page), g in page_groups.items():
        impressions = g["impressions"]
        ctr = round(g["clicks"] / impressions, 5)
        position = round(g["position_weighted"] / impressions, 2)
        suggested = g["suggested_target"]
        # "target" is only an editorial hypothesis. The page in this record
        # is the landing URL actually reported in a GSC query×page row.
        differs = bool(suggested and suggested != page)
        rewrite = (name != "その他・未分類" and impressions >= 50
                   and 8 <= position <= 20 and ctr < 0.02)
        if differs and impressions >= 50:
            action = "実流入先と推奨意図ページの違いを精査（自動移転はしない）"
            priority = "review_intent"
        elif rewrite:
            action = "この実流入ページのtitle・導入・内部リンクを精査"
            priority = "rewrite"
        else:
            action = "継続観測（実流入先の改稿を即断しない）"
            priority = "observe"
        page_intents.append({
            "cluster": name, "observed_page": page, "suggested_target": suggested,
            "intent_mismatch": differs, "clicks": g["clicks"],
            "impressions": impressions, "ctr": ctr, "average_position": position,
            "query_count": len(g["queries"]), "action": action, "priority": priority,
        })
    order = {"review_intent": 0, "rewrite": 1, "observe": 2}
    page_intents.sort(key=lambda p: (order[p["priority"]], -p["impressions"], p["observed_page"]))
    warnings = [
        "このレポートは提供されたCSVだけに基づきます。GSCに接続していません。",
        "Search Consoleは匿名化・行数上限があり、行合計はサイト総計とは限りません。",
        "掲載順位は表示回数重みの参考平均、CTRはクリック数÷表示回数で再計算しています。",
        f"{window}日間は引数で指定された集計期間でありCSVファイルから検証していません。",
    ]
    if source_kind == "manual_page_filter":
        warnings.append("ページとの対応はGSC画面でページ完全一致フィルタを設定したという--page-filterの申告によります。CSV単体ではその設定を検証できません。")
    if not has_page:
        warnings.append("クエリのみのCSVです。検索語と個別ページを結び付けた改善提案はできません。")
    else:
        warnings.append("実流入ページはquery×page行からのみ集計しています。推奨ページは仮説であり実流入先と同一とは限りません。")
    return {"window_days_label": window, "query_page_rows": has_page,
            "source_kind": source_kind,
            "row_count": len(rows), "clusters": clusters, "page_intents": page_intents,
            "warnings": warnings,
            "next_step": ("page_intentsの実流入先を優先して検索意図と既存ページを照合"
                          if has_page else
                          "Search Consoleでページ×クエリの同時データを取得して着地先を特定")}


def markdown(report: dict) -> str:
    lines = [f"# Search Console CSV監査（申告期間：直近{report['window_days_label']}日）",
             f"入力行：{report['row_count']}（公式のサイト総計ではありません）",
             "",
             "| 検索意図 | 表示 | クリック | CTR | 参考順位 | 優先判断 |",
             "|---|---:|---:|---:|---:|---|"]
    for c in report["clusters"]:
        lines.append(f"| {c['cluster']} | {c['impressions']} | {c['clicks']} | "
                     f"{c['ctr']:.1%} | {c['average_position']:.1f} | {c['action']} |")
    if report["query_page_rows"]:
        lines.extend(["", "## 実流入先×検索意図（CSVの同一行に基づく）",
                      "| 実流入先 | 検索意図 | 表示 | クリック | CTR | 参考順位 | 精査 |",
                      "|---|---|---:|---:|---:|---:|---|"])
        for p in report["page_intents"][:20]:
            lines.append(f"| {p['observed_page']} | {p['cluster']} | {p['impressions']} | "
                         f"{p['clicks']} | {p['ctr']:.1%} | {p['average_position']:.1f} | {p['action']} |")
        if len(report["page_intents"]) > 20:
            lines.append(f"上位20件を表示（総数{len(report['page_intents'])}件）。JSON出力で全件確認。")
    lines.extend(["", "**次の検証**：" + report["next_step"], "", "**注意**"])
    lines.extend("- " + warning for warning in report["warnings"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="GSC queries CSV (query or query+page)")
    parser.add_argument("--window", type=int, choices=(28, 90), required=True,
                        help="Chosen 28- or 90-day period (cannot be verified from CSV)")
    parser.add_argument("--json", type=Path, help="Write structured result as UTF-8 JSON")
    parser.add_argument("--page-filter", metavar="EXACT_HTTPS_URL",
                        help="Use ONLY when GSC Queries.csv was exported with this exact page URL filter active; never for a sitewide export")
    args = parser.parse_args(argv)
    try:
        rows, has_page = read_export(args.csv_file)
        source_kind = "csv"
        if args.page_filter:
            rows, has_page = attach_page_filter(rows, has_page, args.page_filter)
            source_kind = "manual_page_filter"
        if not rows:
            raise ValueError("No nonempty query rows found")
        report = analyze(rows, has_page, args.window, source_kind=source_kind)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(markdown(report))
    if args.json:
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
