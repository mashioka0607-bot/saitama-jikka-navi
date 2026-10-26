"""Check deployed public pages, not just generated static files.

GitHub Actions success proves build validity, not that Cloudflare's public URL
serves those files. This read-only probe runs after main pushes and reports
external failures separately; it never asserts GSC indexing or ASP revenue.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PROBES = {
    "/": "埼玉実家片付けナビ",
    "/shindan/": 'id="diag"',
    "/tedori-hikaku/": 'id="calc"',
    "/kaitai-check/": 'id="grant-city"',
    "/robots.txt": "sitemap.xml",
    "/sitemap.xml": "/tedori-hikaku/",
    "/google02c383ec58048d5e.html": "google-site-verification",
}


def validate_release_manifest(payload: str, expected_sha: str) -> str | None:
    """An HTTP 200 from an older release must not be counted as deployed."""
    try:
        data = json.loads(payload)
    except (TypeError, ValueError):
        return "/release.json: invalid JSON"
    actual = data.get("git_sha") if isinstance(data, dict) else None
    if not isinstance(actual, str) or not re.fullmatch(r"[0-9a-f]{40}", actual):
        return "/release.json: missing or invalid git_sha"
    if actual != expected_sha:
        return f"/release.json: stale production commit {actual[:12]} (expected {expected_sha[:12]})"
    return None


def inspect(base_url: str, expected_sha: str | None = None) -> list[str]:
    """A failed fetch means unverified external availability, not proven outage."""
    problems = []
    host = urlsplit(base_url).hostname
    for path, expected in PROBES.items():
        url = base_url.rstrip("/") + path
        try:
            request = Request(url, headers={"User-Agent": "Saitama-Jikka-Navi-ReleaseCheck/1.0"})
            with urlopen(request, timeout=10) as response:
                status = response.status
                final_host = urlsplit(response.geturl()).hostname
                body = response.read(1_000_000).decode("utf-8", errors="replace")
            if status != 200:
                problems.append(f"{path}: HTTP {status}")
            elif final_host != host:
                problems.append(f"{path}: redirected off configured hostname ({final_host})")
            elif expected not in body:
                problems.append(f"{path}: expected public content not found")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            problems.append(f"{path}: {type(exc).__name__}: {str(exc)[:150]}")
    if expected_sha:
        path = "/release.json"
        try:
            request = Request(base_url.rstrip("/") + path, headers={
                "User-Agent": "Saitama-Jikka-Navi-ReleaseCheck/1.0",
                "Cache-Control": "no-cache",
            })
            with urlopen(request, timeout=10) as response:
                status = response.status
                final_host = urlsplit(response.geturl()).hostname
                body = response.read(8192).decode("utf-8", errors="replace")
            if status != 200:
                problems.append(f"{path}: HTTP {status}")
            elif final_host != host:
                problems.append(f"{path}: redirected off configured hostname ({final_host})")
            else:
                failure = validate_release_manifest(body, expected_sha)
                if failure:
                    problems.append(failure)
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            problems.append(f"{path}: {type(exc).__name__}: {str(exc)[:150]}")
    return problems


def main() -> int:
    config = json.loads((ROOT / "site_data.json").read_text(encoding="utf-8"))
    base_url = str(config.get("base_url") or "").strip()
    if urlsplit(base_url).scheme != "https" or not urlsplit(base_url).hostname:
        print("Invalid public base_url; live-site verification cannot run.")
        return 1
    expected_sha = os.getenv("GITHUB_SHA", "").strip().lower()
    if expected_sha and not re.fullmatch(r"[0-9a-f]{40}", expected_sha):
        print("Invalid GITHUB_SHA; cannot validate public deployment freshness.")
        return 1
    # The Pages deployment may complete shortly after a GitHub push.
    attempts = 6
    for attempt in range(1, attempts + 1):
        problems = inspect(base_url, expected_sha or None)
        if not problems:
            summary = f"✅ Public HTTP + commit freshness check passed ({len(PROBES) + (1 if expected_sha else 0)} resources): {base_url}"
            print(summary)
            if os.getenv("GITHUB_STEP_SUMMARY"):
                with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
                    fh.write(summary + "\n")
            return 0
        print(f"Live-site check {attempt}/{attempts}: " + " | ".join(problems), flush=True)
        if attempt < attempts:
            time.sleep(12)
    print("::warning title=Public site not verified::GitHub build can pass while the deployed URL is unreachable or stale. Check Cloudflare Pages deployment and DNS.")
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(f"⚠️ Public HTTP smoke check could not verify {base_url} after {attempts} attempts.\n")
            fh.write("\n".join("- " + problem for problem in problems) + "\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
