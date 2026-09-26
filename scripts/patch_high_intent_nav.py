from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_GENERATED = '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/kawagoe-shi/mitsumori-check/">見積チェック</a><a href="/faq/">FAQ</a></nav>'
NEW = '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/tedori-hikaku/">手残り比較</a><a href="/kaitai-check/">解体前チェック</a><a href="/faq/">FAQ</a></nav>'
# patch_build_quality.py runs before this script and may already install the same
# high-intent links in the opposite order. Treat that state as valid/idempotent.
QUALITY_PATCHED = '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/kaitai-check/">解体前チェック</a><a href="/tedori-hikaku/">手残り比較</a><a href="/faq/">FAQ</a></nav>'
OLD_STATIC = '<nav><a href="/">ホーム</a><a href="/shindan/">進め方診断</a><a href="/tedori-hikaku/">手残り比較</a><a href="/faq/">FAQ</a></nav>'


def replace_once(path: Path, old: str, new: str, accepted=()) -> None:
    text = path.read_text(encoding='utf-8')
    if new in text or any(candidate in text for candidate in accepted):
        return
    if old not in text:
        raise SystemExit(f'expected nav not found: {path}')
    path.write_text(text.replace(old, new, 1), encoding='utf-8')


replace_once(ROOT / 'build.py', OLD_GENERATED, NEW, accepted=(QUALITY_PATCHED,))
for rel in ('static_pages/tedori-hikaku/index.html', 'static_pages/kaitai-check/index.html'):
    replace_once(ROOT / rel, OLD_STATIC, NEW)

print('high-intent navigation patched')
