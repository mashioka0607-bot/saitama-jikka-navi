from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'static_pages/tedori-hikaku/index.html'
MARKER = '<section class="section"><form id="calc" class="diagnosis">'
BLOCK = '''<section class="section notice" id="subsidy-bridge"><h2>解体・家財処分の補助金があるなら、先に差し引いて比較</h2><p><strong>自治体によっては、解体費や家財処分費の一部が補助対象になります。</strong>補助を使える物件で自己負担が下がると、「そのまま買取」と「片付け・解体して売る」の手残り差が変わります。</p><p>ただし、制度によっては<strong>契約・着工前の申請や交付決定</strong>が必要です。先に業者と契約すると対象外になることがあるため、下の比較へ費用を入れる前に所在地の制度を確認してください。</p><p><a class="button" data-context="tedori_subsidy_bridge" href="/kaitai-check/">埼玉の解体・家財補助を契約前に確認</a></p><p><small>確認後は、補助見込額そのものではなく「補助後に自分で負担する片付け費・解体費」を下の欄へ入力してください。補助の採択・支給を保証するものではありません。</small></p></section>'''

text = PATH.read_text(encoding='utf-8')
if 'tedori_subsidy_bridge' in text:
    print('subsidy bridge already present')
elif MARKER not in text:
    raise SystemExit('expected calculator marker not found')
else:
    PATH.write_text(text.replace(MARKER, BLOCK + MARKER, 1), encoding='utf-8')
    print('added subsidy bridge to tedori-hikaku')
