from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "build.py"


def replace_once(text: str, old: str, new: str) -> tuple[str, bool]:
    count = text.count(old)
    if count > 1:
        raise SystemExit(f"Refusing homepage patch: expected at most 1 match, found {count}: {old[:90]!r}")
    if count == 1:
        return text.replace(old, new, 1), True
    return text, False


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    changed = False

    replacements = [
        (
            "Kawagoe / Inherited Home",
            "Saitama / Inherited Home",
        ),
        (
            "相続した実家や空き家は、先に高額な片付けを契約せず、名義・家族の合意・家の出口を確認してから必要な片付けだけ進めます。",
            "埼玉県の実家や空き家は、片付けや媒介契約を急ぐ前に、名義・家族の合意と市町村ごとの制度条件を確認。通常売却・空き家バンク・公的相談・専門買取を比べてから必要な片付けだけ進めます。",
        ),
        (
            "<strong>2. 現況で出口確認</strong><br>売却・保有・管理・活用を比較",
            "<strong>2. 自治体制度を先に確認</strong><br>空き家バンク等の登録条件は市町村ごとに異なる",
        ),
        (
            "<strong>3. 必要分だけ片付け</strong><br>価値確認後に処分・買取・業者比較へ",
            "<strong>3. 出口を比べてから片付け</strong><br>通常売却・空き家バンク・専門買取を比較",
        ),
        (
            "川越市を中心に、相続した実家を片付ける前に名義・家族合意・売却・活用・管理・解体を整理します。",
            "埼玉県で相続した実家を片付ける前に、名義・家族合意・市町村制度・通常売却・空き家バンク・専門買取の順番を整理します。",
        ),
    ]

    for old, new in replacements:
        text, did = replace_once(text, old, new)
        changed = changed or did

    # patch_build_quality.py used to inject a dated 9/27 event. Remove the entire stale event section
    # while preserving the following affiliate placeholder (which renders only after a verified offer is configured).
    stale_start = '<section class="section warning"><strong>9/27（日）｜予約なしで、解体・不用品回収/買取・相続/不動産をまとめて相談</strong>'
    if stale_start in text:
        start = text.index(stale_start)
        end_marker = "</section>{offer_cta('primary','home')}"
        end = text.find(end_marker, start)
        if end == -1:
            raise SystemExit("Found stale 9/27 event but could not locate its section end")
        end += len("</section>")
        replacement = '''<section class="section notice"><strong>埼玉県内でも空き家バンクの条件は一律ではありません</strong><p>川越市は宅建業者との媒介契約が未締結であることを登録条件にしています。一方、埼玉県北部地域の制度では登録に宅建業者との代理・媒介契約が必要です。先に契約する／しないを県全体で決めつけず、実家の市町村の最新条件を確認してから動くのが安全です。</p><p><a class="public-link" data-context="home_saitama_airbank" href="https://www.pref.saitama.lg.jp/a1107/akiyabanku.html" target="_blank" rel="noopener">埼玉県公式の市町村空き家バンク一覧を見る</a></p><small>制度条件は市町村・時期で変わるため、契約前に各自治体の一次情報を確認してください。</small></section>'''
        text = text[:start] + replacement + text[end:]
        changed = True

    # If the old Kawagoe-only notice still exists without the stale-event injection, replace it directly.
    old_notice = '''<section class="section notice"><strong>川越市にも原則無料の空き家相談窓口があります</strong><p>「何から手をつければいいか」から相続、管理、賃貸、売却、解体まで相談できます。</p><p><a class="public-link" data-context="home_consultation" href="https://www.city.kawagoe.saitama.jp/kurashi/jyutaku/1003031/1020433.html" target="_blank" rel="noopener">川越市公式の相談窓口を見る</a></p></section>'''
    new_notice = '''<section class="section notice"><strong>まず実家の市町村制度を確認</strong><p>埼玉県の空き家バンクは市町村主体で、登録条件や媒介の扱いが自治体ごとに異なります。片付けや媒介契約の前に、対象市町村の一次情報を確認してください。</p><p><a class="public-link" data-context="home_saitama_airbank" href="https://www.pref.saitama.lg.jp/a1107/akiyabanku.html" target="_blank" rel="noopener">埼玉県公式の市町村空き家バンク一覧を見る</a></p></section>'''
    text, did = replace_once(text, old_notice, new_notice)
    changed = changed or did

    forbidden = [
        "Kawagoe / Inherited Home",
        "川越市を中心に、相続した実家を片付ける前に",
        "9/27（日）｜予約なしで",
    ]
    leftovers = [x for x in forbidden if x in text]
    if leftovers:
        raise SystemExit(f"Homepage statewide gate failed; stale strings remain: {leftovers}")

    if changed:
        PATH.write_text(text, encoding="utf-8")
        print("Patched homepage: Saitama-wide positioning, municipality-first airbank gate, stale event removed.")
    else:
        print("Homepage statewide patch already applied; no changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
