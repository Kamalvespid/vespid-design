# Changelog

Locked decisions and changes to the Vespid design system. Newest first.

## 2026-10-18 — Repo created
- Imported `vespid-badge-generator` and `vespid-character-generator` skills.
- **Fixed:** badge generator still used the pre-10 Oct skin tones in its cast table and Appendix B drawings (Aina `#C68863`, Wei Jie `#F1C27D`, Priya `#8D5524`, Ryan `#B57B4C`). Updated to the brightened set so badges match the character generator, the project steering doc and the cast summary.
- Added `tools/check_cast_sync.py` and `tools/lint_svg.py`, plus CI to run both on every push and PR.
- Exported standalone cast reference SVGs to `assets/cast/`.

## 2026-10-10 — Skin tones brightened
- Aina `#D8A27F`, Wei Jie `#F6D2A2`, Priya `#A86B3D`, Ryan `#C99066`.

## 2026-10-09 — Limbs and views locked
- Rooted limbs L1–L6 and view rules V1–V6 (front and three-quarter only inside badges).

## Open
- **Uncle Halim** (half-circle, "The Saver") is a candidate only. To resolve before adding to the skills: persona name clashes with the "Saver" category badge, grey brows, community review.
- **Milestone tier thresholds** are illustrative (§3.1 of the badge skill). Need product sign-off before badges ship.
