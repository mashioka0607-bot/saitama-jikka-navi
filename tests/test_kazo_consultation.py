"""Regression: short-lived Kazo consultation must be sourced and self-expire."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class KazoConsultationTests(unittest.TestCase):
    def test_kazo_free_consultation_is_sourced_and_not_misrepresented(self):
        html = (ROOT / "static_pages/tedori-hikaku/index.html").read_text(encoding="utf-8")
        marker = 'id="kazo-akiya-consult-20261124"'
        self.assertEqual(html.count(marker), 1)
        fragment = html.split(marker, 1)[1].split("</section>", 1)[0]
        for expected in (
            'data-consultation-application-through="2026-11-24"',
            'data-consultation-event-through="2026-11-24"',
            "加須市役所1階ギャラリー",
            "2026年11月24日（火）10時〜15時",
            "宅地建物取引士・弁護士・税理士",
            "1組30分・予約なしで来場可",
            "https://www.city.kazo.lg.jp/soshiki/koutsuu/akiya/17943.html",
            "現況買取・売却価格や税務上の取り扱いの保証ではありません",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, fragment)
        self.assertIn('id="municipal-consultation-deadline-guard"', html)
        self.assertIn("if(now>section.dataset.consultationEventThrough){section.hidden=true", html)
        # A temporary local event may be added within the existing comparison
        # page, but must never create a duplicate thin location landing page.
        self.assertNotIn('href="/kazo-shi/"', html)


if __name__ == "__main__":
    unittest.main()
