"""Fail deploy if public demolition-grant statuses drift from reviewed source data.

This is a consistency guard, not an assertion that municipality budgets are live.
The latest acceptance status still needs checking on each official municipality page.
"""
from __future__ import annotations

import ast
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "demolition_grants_2026.json"
PUBLIC_JS = ROOT / "static_pages" / "kaitai-check" / "grants.js"


def public_rows(source: str) -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for line in source.splitlines():
        line = line.strip()
        if not line.startswith("['"):
            continue
        # Each entry is a one-line JS array of five single-quoted strings;
        # this is also a Python list literal. The final entry ends in "]];".
        if line.endswith("]];"):
            literal = line[:-2]
        elif line.endswith("],"):
            literal = line[:-1]
        else:
            raise ValueError("Unrecognized public grant row ending")
        record = ast.literal_eval(literal)
        if not isinstance(record, list) or len(record) != 5 or not all(isinstance(x, str) for x in record):
            raise ValueError("Unexpected public grant record shape")
        city = record[0]
        if city in rows:
            raise ValueError(f"Duplicate public grant city: {city}")
        rows[city] = record
    if not rows:
        raise ValueError("No grants found in public grants.js")
    return rows


def check() -> list[str]:
    source_data = json.loads(DATA.read_text(encoding="utf-8"))
    rows = public_rows(PUBLIC_JS.read_text(encoding="utf-8"))
    problems: list[str] = []
    for item in source_data["municipalities"]:
        city = item["municipality"]
        row = rows.get(city)
        if row is None:
            problems.append(f"{city}: reviewed municipality missing in public selector")
            continue
        status, public_status = item["status"], row[1]
        if row[4] != item["official_url"]:
            problems.append(f"{city}: public official URL differs from reviewed source")
        if "受付終了" in status and "受付終了" not in public_status:
            problems.append(f"{city}: reviewed CLOSED status is not reflected publicly")
        if "受付終了" not in status and "受付終了" in public_status:
            problems.append(f"{city}: public CLOSED status contradicts reviewed source")
        if "受付再開" in status and "再開" not in public_status:
            problems.append(f"{city}: reviewed REOPENED status is not reflected publicly")
        # Specific contractor eligibility must travel with the public CTA;
        # a user choosing a noneligible vendor could lose the grant.
        if "市内に本社" in (item.get("contract_timing") or "") and "市内に本社" not in " ".join(row[1:4]):
            problems.append(f"{city}: eligible local-headquarters contractor rule missing publicly")
        # For dated budget snapshots, check amount, as-of date and remaining
        # full-grant count; status and URL checks alone miss stale figures.
        note = item.get("note", "")
        budget = re.search(r"予算残額\s*([0-9,]+)万円", note)
        if budget:
            public_text = " ".join(row[1:4])
            amount = budget.group(1)
            if not re.search(r"予算残(?:額)?\s*" + re.escape(amount) + r"万円", public_text):
                problems.append(f"{city}: reviewed budget {amount}万円 missing from public text")
            if item["status_as_of"] not in public_text:
                problems.append(f"{city}: budget snapshot date {item['status_as_of']} missing publicly")
            remaining = re.search(r"残り\s*(\d+)件分", note)
            if remaining and not re.search(r"残り\s*" + remaining.group(1) + r"件分", public_text):
                problems.append(f"{city}: remaining full-grant count differs from source")
        # A reopening or closing date must be shown, so users can distinguish
        # a dated municipality announcement from today's unverified budget status.
        if "受付終了" in status or "受付再開" in status:
            date = item["status_as_of"]
            if date not in " ".join(row[1:4]):
                problems.append(f"{city}: announcement date {date} missing in public text")
    return problems


def main() -> int:
    try:
        problems = check()
    except (OSError, ValueError, KeyError, SyntaxError) as exc:
        print(f"Grant consistency gate error: {exc}", file=sys.stderr)
        return 1
    if problems:
        for problem in problems:
            print("Grant consistency failed: " + problem, file=sys.stderr)
        return 1
    print("Grant consistency passed: reviewed municipality status, dated changes, and official URLs align.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
