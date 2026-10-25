"""Check deployed public pages, not just generated static files.

GitHub Actions success proves build validity, not that Cloudflare's public URL
serves those files. This read-only probe runs after main pushes and reports
external failures separately; it never asserts GSC indexing or ASP revenue.
"""
from __future__ import annotations

import json
import os
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


def inspect(base_url: str) -> list[str]:
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
    return problems


def main() -> int:
    config = json.loads((ROOT / "site_data.json").read_text(encoding="utf-8"))
    base_url = str(config.get("base_url") or "").strip()
    if urlsplit(base_url).scheme != "https" or not urlsplit(base_url).hostname:
        print("Invalid public base_url; live-site verification cannot run.")
        return 1
    # The Pages deployment may complete shortly after a GitHub push.
    attempts = 4
    for attempt in range(1, attempts + 1):
        problems = inspect(base_url)
        if not problems:
            summary = f"✅ Public HTTP smoke check passed ({len(PROBES)} resources): {base_url}"
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
