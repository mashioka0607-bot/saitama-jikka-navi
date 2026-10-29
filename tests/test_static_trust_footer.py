"""Keep the editorial policy discoverable from high-intent decision tools.

These static pages replace build.py-generated versions at deploy time, so
checking build.py's shared layout alone is not sufficient.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ("shindan", "tedori-hikaku", "kaitai-check")


def test_decision_tools_link_to_editorial_policy():
    for slug in TOOLS:
        page = (ROOT / "static_pages" / slug / "index.html").read_text(encoding="utf-8")
        footer = page.split("<footer>", 1)[1].split("</footer>", 1)[0]
        assert 'href="/editorial-policy/"' in footer, f"{slug}: editorial policy missing"
        assert 'href="/advertising-policy/"' in footer, f"{slug}: advertising policy missing"
        assert 'href="/operator/"' in footer, f"{slug}: operator info missing"
