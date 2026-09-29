"""Regression guard: shared site UI must not accidentally become Kawagoe-only again.

Kawagoe-specific editorial pages may remain in data/pages.json; this test only protects
shared/home UI in build.py, where prefecture-wide positioning is required.
"""
from pathlib import Path

BUILD = Path(__file__).resolve().parents[1] / "build.py"
text = BUILD.read_text(encoding="utf-8")

FORBIDDEN_SHARED_MARKERS = {
    'href="/kawagoe-shi/mitsumori-check/"': "shared nav points to a Kawagoe-only quote page",
    "Kawagoe / Inherited Home": "home hero is branded as Kawagoe-only",
    "川越市を中心に": "home meta description narrows the prefecture-wide site to Kawagoe",
}


def test_shared_ui_is_not_kawagoe_locked():
    found = {marker: reason for marker, reason in FORBIDDEN_SHARED_MARKERS.items() if marker in text}
    assert not found, "Prefecture-wide regression detected: " + "; ".join(found.values())
