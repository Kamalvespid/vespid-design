---
name: "vespid-character-generator"
description: "Create, pose, turn or extend the Vespid Kawan cast (Aina, Wei Jie, Priya, Ryan, plus new characters) as export-safe SVG with rooted limbs and locked view rules."
---

# Vespid Character Generator

Use this for anything about the Kawan cast that is **not** a finished badge: a new cast member, a turnaround (front / three-quarter / profile / back), a pose, an expression set, or a scene character for onboarding and empty states. For badges, use the badge generator; it copies the same cast drawings.

## 1. How to read a request

Work out the **mode**, then follow its section:

| Mode | Example request | Section |
|---|---|---|
| Pose | "Ryan holding a phone, celebrating" | §4, §5 |
| Turnaround | "Priya turnaround" / "Aina from the back" | §6 |
| Expression sheet | "Wei Jie expressions" | §5 |
| New character | "A retired uncle who runs a kopitiam" | §7 |

If the character, view, pose or expression is missing, use: front view, arms down, Happy. State the assumption in the spec block.

## 2. Style rules

1. **One hero shape per person:** circle, pill, triangle or square for the current cast; a new character gets a different shape (§7). It sets the silhouette and hints at personality.
2. **Proportions:**
   - Big head (about 40% of height), no neck.
   - Rooted limbs: arms grow from inside the torso (see **Limbs** below). Legs are rounded rects under the torso.
   - Round mitten hands (circles, r ≈ 8–9).
3. **Colour and depth:** flat colour plus one hard shadow. The shadow is the same shape in a darker tone, offset on the right side. No outlines, no gradients.
4. **Shared face kit:**
   - Eyes: ovals `rx 4.2 / ry 5.6` in `ink`, each with one white glint (r 1.5).
   - Brows: bar brows, 11 × 3.6, rounded.
   - Mouth: a single shape.
   - Cheeks: r 4 at 50–60% opacity.
5. **Signature colour:** each person owns one colour, which is never also used as the campaign's face colour.
6. **Specific, not stereotyped:** personality comes from traits and props.
   - Everyday clothes by default.
   - Festive clothes only in festive campaigns, and rotated across the whole cast.
   - Never tie money habits to ethnicity.
7. **Legibility:** must read at 96 px. The head plus one prop carries the meaning.
8. **No branding:** no Vespid or partner branding on clothes or props.

**Limbs (rooted, locked 9 Oct 2026):**
- **L1 Grow from inside.** Each arm is one round-capped stroke whose start point sits at least 8 units inside the torso edge, at shoulder height (y ≈ 102–108). Never start an arm on the torso edge; a visible cap there makes the arm look stuck on.
- **L2 Same colour as its root.** An arm takes the colour of the torso zone it leaves: main side → main colour, shadow side → shadow colour. Draw it after the torso so there is no seam. Draw details such as hoodie strings after the arms.
- **L3 Crossing arms separate.** Only an arm that passes in front of the torso (hugging a prop, folded arms) uses the shadow tone, so it stays readable. It is still rooted.
- **L4 Width.** Arms are 16 units wide. Mitten hands (r 8–9) sit on the arm end.
- **L5 Legs unchanged.** Rounded rects tucked under the torso.
- **L6 One path per arm.** A new pose changes only the arm paths and hand positions. Never redraw the torso or sleeves as one combined shape.

**Views (locked 9 Oct 2026):**
- **V1 Where each view is used.** Front and three-quarter only inside badges. Profile and back only in larger scenes (onboarding, empty states, story moments).
- **V2 Hero shape holds.** Head and torso keep their shape in every view; only the width compresses (three-quarter ≈ 88%, profile ≈ 80%).
- **V3 Face kit slides, nothing new.** Three-quarter: the face shifts 8 units toward the turn, the far eye narrows to rx 3.4 and the far cheek is hidden. Profile: one eye near the front edge, mouth at the edge. Never add a nose or ears.
- **V4 Light stays top-left.** The hard shadow is always on the right. When a pose is mirrored, re-apply the shadow on the right instead of mirroring it.
- **V5 Near in front, far behind.** The far arm is drawn behind the torso in the shadow tone; the far leg and shoe are one step darker.
- **V6 Signature survives.** At least one signature item (hijab, top bun, cap brim, hoodie hood) shows in every view, including the back.

**Cast coordinate space:**
- Full figure is about 200 units tall, centred on x = 0, feet at y ≈ 196.
- Head centre is at y ≈ 52–58.
- The torso starts at y ≈ 94–98.
- Inside a campaign badge, only y < ≈137 is visible (cropped at the split line), so frame the scene as a **bust plus prop**.
- Props can extend to x ≈ ±100 and up to y ≈ −10.

## 3. The cast (working names)

Skin tones are the brightened set from 10 Oct 2026.

| Name | Shape | Personality | Skin | Signature build |
|---|---|---|---|---|
| **Aina** | Circle | The Planner: warm, organised | `#D8A27F` | Teal hijab `#14B8A6` (shade `#0E9384`) framing an oval face; coral pill tunic `#FF7A59` (shade `#E2604A`) |
| **Wei Jie** | Pill | The Spontaneous One: fun, generous | `#F6D2A2` | Tall pill-shaped head; black messy top hair; yellow pill hoodie `#FFC107` (shade `#E0A100`) with white strings; blue jeans, red sneakers |
| **Priya** | Triangle | The Go-getter: ambitious, runs a side hustle | `#A86B3D` | Big dark hair mass with a top bun and side curls; magenta A-line top `#DB2777` (shade `#B0175E`); small gold earrings |
| **Ryan** | Square | The Steady One: calm, practical | `#C99066` | Rounded-square head; orange cap `#F97316` (brim `#EA580C`); green boxy shirt `#22C55E` (shade `#15803D`) with white V collar |

**Colours already taken as signature colours:** teal, coral, yellow, magenta, orange, green. Ink is `#1E1B3A`.

**Using a cast member:** always start from Appendix A. Copy the head, hair or headwear, face kit, skin, torso and legs exactly; change only arms (§4), expression (§5), view (§6) and props. Never redraw a cast member from the description.

## 4. Arm recipes (rooted)

`W` = torso half-width: Aina 34, Wei Jie 30, Ryan 38. Priya's A-line top is narrow at the shoulder, so use the values in brackets. "Main" = torso main colour, "shadow" = torso shadow colour. Viewer's left is the lit (main) side. Width 16, round caps, drawn after the torso. Hands are skin circles r 8–9 at the end point.

| Pose | Left arm (main side) | Right arm (shadow side) |
|---|---|---|
| Down | `M(-W+14) 104 Q(-W-10) 118 (-W-8) 140` main [Priya `M-8 108 Q-30 120 -28 140`] | `M(W-9) 103 Q(W+10) 118 (W+10) 140` shadow [Priya `M10 108 Q30 120 30 140`] |
| Wave | Down | `M(W-9) 103 Q(W+14) 98 (W+16) 74`, hand r 9 at y 68 [Priya `M10 108 Q40 98 44 72`] |
| Celebrate | `M(-W+10) 106 Q(-W-12) 90 (-W-10) 64` main, hand at y 58 | mirror of left, shadow |
| Hold prop at side | `M(-W+14) 104 Q(-W-10) 120 (-W-6) 138` main; prop centred on the hand | Down |
| Hand on chest (Proud) | crossing, shadow: `M(-W+14) 112 Q-6 116 -2 104`, hand at (-2, 104) | Down |
| Hand on chin (Thinking) | Down | crossing, shadow: `M(W-10) 112 Q(W-4) 98 16 86`, hand at (14, 84) |
| Hug prop / folded | crossing, shadow: `M(-W+10) 104 Q(-W-6) 128 -14 134` | mirror, shadow |

Check every arm against L1–L4: start point ≥ 8 units inside the torso edge; colour = zone it leaves unless it crosses the body.

## 5. Expressions

Every cast member uses the same four. Only the face kit and arms change.

| Expression | Eyes | Brows | Mouth | Arms |
|---|---|---|---|---|
| Happy | Default ovals with glint | Default | Open smile `M-7 70 Q0 78 7 70 Z` (adjust y to the face) | Any |
| Celebrate | `^` arcs: `M-16 56 Q-11 49 -6 56 M6 56 Q11 49 16 56`, stroke 3.6 | Raised 3 units | Big open `M-11 66 Q0 86 11 66 Z` + tongue | Celebrate; add 2–3 confetti bits |
| Proud | Closed smile arcs `M-16 56 Q-11 61 -6 56 M6 56 Q11 61 16 56` | Default | Small closed smile stroke | Hand on chest |
| Thinking | Near eye squints (ry 4.4), far eye default | Far brow tilted −12° | Flat wavy stroke, off-centre | Hand on chin; 2 thought dots top-right |

## 6. Turnarounds

Apply V1–V6 (§2). Recipe from the front drawing:

1. **Three-quarter (turned to viewer's right).** Head and torso width × 0.88. Shift eyes, brows, mouth +8 x; far eye rx 3.4, ry 5.4, glint r 1.3; hide far cheek. Hair or headwear grows on the back (left) side. Far arm and far leg drawn **before** the torso (far leg one step darker, e.g. jeans `#2F6BD9`, shoe `#C93636`). Shoes point toward the turn.
2. **Profile (facing right).** Head and torso width × 0.8. One eye near the front edge (x ≈ +15), one brow, cheek behind the eye, mouth on the front edge. No nose, no ears. Hair or headwear covers the back half. The one visible arm crosses the torso, so it uses the shadow tone.
3. **Back.** No face. Hair or headwear mass covers the head to about y 64. Show at least one signature item (hood, hijab drape, bun, cap). Arms as front, rooted.
4. **Facing left.** Mirror the geometry, then put the hard shadow back on the right (V4).

Worked examples (Wei Jie) are in Appendix B.

## 7. New characters

1. **Brief:** name (working), hero shape, personality in one line, everyday outfit, one signature item, one prop that hints at their money habit without stereotyping.
2. **Hero shape:** must differ from the cast. Taken: circle, pill, triangle, square. Good options: half-circle, diamond, rounded star, tall rectangle. Never hexagon, flame shield or half-moon (those are badge-family shapes).
3. **Signature colour:** not in the taken list (§3) and not a badge face colour. Pick a main + shadow pair (shadow ≈ 15–20% darker).
4. **Representation:** specific, not stereotyped (rule 6). Flag anything that ties money habits to ethnicity, religion or age, and recommend a community review.
5. **Deliver a character sheet:** front (arms down, Happy), three-quarter, the four expressions as busts, and a cast-table row. Provide the front drawing as a `<g id="cast-name">` group in cast coordinates, ready to paste into Appendix A of both skills.
6. **Status:** label it **"Candidate — not in cast until approved"**. Do not use a candidate in badges.

## 8. Export-safe SVG

- Plain shapes only: `rect`, `circle`, `ellipse`, `path`, `g`, `transform`. No `<style>`, filters, gradients, masks, `paint-order` or `textPath`.
- Explicit hex fills. No outlines on characters (except white sneakers' light edge, as drawn).
- Cast coordinates, viewBox `-100 -20 200 225` for a single figure; add a ground ellipse `cx 0 cy 198 rx 44 ry 5 fill #E9E6DE`.
- Draw order: ground → far leg/shoe → far arm (if behind) → legs/shoes → torso shadow → torso main → rooted arms → torso details → props → hands → head → hair/headwear → face.

## 9. Output contract

1. A spec block:
```
Character: …   Mode: …   View: …   Pose: …   Expression: …   Props: …
Rules checked: L1–L6, V1–V6, style 1–8
```
2. The SVG (one per figure, or a sheet with figures side by side).
3. For previews, render inline in HTML (not a standalone .svg).
4. One line on anything you assumed or flagged.

## 10. Checklist (run before returning)

- [ ] Cast member copied from Appendix A, not redrawn.
- [ ] Arms rooted: start ≥ 8 units inside, colour = zone, 16 wide.
- [ ] View rules: hero shape held, face kit slid, no nose or ears, shadow on the right.
- [ ] Signature item visible.
- [ ] Reads at 96 px (head + one prop) if used small.
- [ ] No branding, no stereotype.

## Appendix A. Cast reference drawings (copy these, don't redraw)

Full figures in cast coordinates (§2): about 200 units tall, centred on x = 0, feet at y ≈ 196. Keep the head, hair or headwear, face, skin and body; replace only arms (§4 recipes), expression (§5) and props.

### Aina (circle)

```svg
<g id="cast-aina">
  <rect x="-20" y="156" width="15" height="34" rx="7.5" fill="#1E1B3A"/>
  <rect x="5" y="156" width="15" height="34" rx="7.5" fill="#1E1B3A"/>
  <rect x="-24" y="184" width="22" height="12" rx="6" fill="#FFFFFF" stroke="#E3E0D8" stroke-width="2"/>
  <rect x="2" y="184" width="22" height="12" rx="6" fill="#FFFFFF" stroke="#E3E0D8" stroke-width="2"/>
  <rect x="-34" y="96" width="68" height="70" rx="28" fill="#E2604A"/>
  <rect x="-34" y="96" width="56" height="70" rx="28" fill="#FF7A59"/>
  <path d="M-20 106 Q-44 126 -40 150" stroke="#FF7A59" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M24 106 Q48 98 50 76" stroke="#E2604A" stroke-width="16" stroke-linecap="round" fill="none"/>
  <circle cx="-40" cy="153" r="8.5" fill="#D8A27F"/>
  <circle cx="50" cy="71" r="9" fill="#D8A27F"/>
  <path d="M-46 52 A46 46 0 0 1 46 52 L50 102 Q0 116 -50 102 Z" fill="#14B8A6"/>
  <path d="M22 10 A46 46 0 0 1 46 52 L50 102 Q42 105 34 107 L33 56 Q32 28 22 10 Z" fill="#0E9384"/>
  <ellipse cx="0" cy="58" rx="29" ry="32" fill="#D8A27F"/>
  <rect x="-17" y="43" width="11" height="3.6" rx="1.8" fill="#1E1B3A"/>
  <rect x="6" y="43" width="11" height="3.6" rx="1.8" fill="#1E1B3A"/>
  <ellipse cx="-11" cy="56" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <ellipse cx="11" cy="56" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <circle cx="-9.6" cy="54" r="1.5" fill="#FFFFFF"/>
  <circle cx="12.4" cy="54" r="1.5" fill="#FFFFFF"/>
  <circle cx="-19" cy="67" r="4" fill="#E07A5F" opacity="0.6"/>
  <circle cx="19" cy="67" r="4" fill="#E07A5F" opacity="0.6"/>
  <path d="M-7 70 Q0 78 7 70 Z" fill="#7A2E1E"/>
</g>
```

### Wei Jie (pill)

```svg
<g id="cast-wei-jie">
  <rect x="-20" y="156" width="15" height="34" rx="7.5" fill="#3B82F6"/>
  <rect x="5" y="156" width="15" height="34" rx="7.5" fill="#3B82F6"/>
  <rect x="-24" y="184" width="22" height="12" rx="6" fill="#EF4444"/>
  <rect x="2" y="184" width="22" height="12" rx="6" fill="#EF4444"/>
  <rect x="-30" y="94" width="60" height="74" rx="30" fill="#E0A100"/>
  <rect x="-30" y="94" width="50" height="74" rx="25" fill="#FFC107"/>
  <path d="M21 103 Q40 118 42 134" stroke="#E0A100" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M-16 104 Q-40 120 -36 138" stroke="#FFC107" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M-8 98 V114 M6 98 V114" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
  <rect x="-47" y="124" width="21" height="27" rx="5" fill="#F5E6D3"/>
  <circle cx="-41" cy="145" r="2.2" fill="#4A2C2A"/>
  <circle cx="-34" cy="146" r="2.2" fill="#4A2C2A"/>
  <circle cx="-38" cy="140" r="2.2" fill="#4A2C2A"/>
  <rect x="-49" y="120" width="25" height="6" rx="3" fill="#FFFFFF" stroke="#E3E0D8" stroke-width="1.5"/>
  <path d="M-35 120 L-30 106" stroke="#EC4899" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="-36" cy="137" r="8" fill="#F6D2A2"/>
  <circle cx="42" cy="136" r="8" fill="#F6D2A2"/>
  <rect x="-34" y="4" width="68" height="90" rx="34" fill="#F6D2A2"/>
  <path d="M-36 40 Q-40 0 0 -2 Q42 0 36 40 Q34 22 18 18 Q4 26 -10 18 Q-26 22 -36 40 Z" fill="#1E1B3A"/>
  <path d="M-18 41 L-6 38.5 M6 38.5 L18 41" stroke="#1E1B3A" stroke-width="3.6" stroke-linecap="round"/>
  <ellipse cx="-11" cy="52" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <ellipse cx="11" cy="52" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <circle cx="-9.6" cy="50" r="1.5" fill="#FFFFFF"/>
  <circle cx="12.4" cy="50" r="1.5" fill="#FFFFFF"/>
  <circle cx="-20" cy="64" r="4" fill="#F28C6B" opacity="0.5"/>
  <circle cx="20" cy="64" r="4" fill="#F28C6B" opacity="0.5"/>
  <path d="M-10 66 Q0 78 10 66 Z" fill="#7A2E1E"/>
</g>
```

### Priya (triangle)

```svg
<g id="cast-priya">
  <rect x="-18" y="160" width="14" height="30" rx="7" fill="#1E1B3A"/>
  <rect x="4" y="160" width="14" height="30" rx="7" fill="#1E1B3A"/>
  <rect x="-22" y="184" width="20" height="12" rx="6" fill="#FFC107"/>
  <rect x="2" y="184" width="20" height="12" rx="6" fill="#FFC107"/>
  <circle cx="0" cy="50" r="44" fill="#1E1B3A"/>
  <circle cx="0" cy="2" r="16" fill="#1E1B3A"/>
  <circle cx="-41" cy="72" r="9" fill="#1E1B3A"/>
  <circle cx="41" cy="72" r="9" fill="#1E1B3A"/>
  <path d="M-14 98 L14 98 L42 166 Q0 174 -42 166 Z" fill="#B0175E" stroke="#B0175E" stroke-width="8" stroke-linejoin="round"/>
  <path d="M-14 98 L6 98 L24 169 Q-10 174 -42 166 Z" fill="#DB2777" stroke="#DB2777" stroke-width="8" stroke-linejoin="round"/>
  <path d="M10 108 Q40 98 44 72" stroke="#B0175E" stroke-width="16" stroke-linecap="round" fill="none"/>
  <circle cx="44" cy="67" r="9" fill="#A86B3D"/>
  <path d="M-8 108 Q-36 118 -32 132" stroke="#DB2777" stroke-width="16" stroke-linecap="round" fill="none"/>
  <rect x="-48" y="120" width="26" height="33" rx="4" fill="#FFFFFF" stroke="#1E1B3A" stroke-width="3"/>
  <path d="M-43 130 H-28 M-43 137 H-28 M-43 144 H-34" stroke="#C9C6D6" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="-31" cy="135" r="8" fill="#A86B3D"/>
  <circle cx="0" cy="54" r="38" fill="#A86B3D"/>
  <path d="M-38 50 Q-30 14 4 14 Q30 16 38 40 Q14 28 -6 34 Q-24 38 -38 50 Z" fill="#1E1B3A"/>
  <path d="M-18 43 L-6 46.5 M6 46.5 L18 43" stroke="#1E1B3A" stroke-width="3.6" stroke-linecap="round"/>
  <ellipse cx="-11" cy="56" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <ellipse cx="11" cy="56" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <circle cx="-9.6" cy="54" r="1.5" fill="#FFFFFF"/>
  <circle cx="12.4" cy="54" r="1.5" fill="#FFFFFF"/>
  <circle cx="-37" cy="64" r="3" fill="#FFC107"/>
  <circle cx="37" cy="64" r="3" fill="#FFC107"/>
  <path d="M-6 70 Q2 76 10 67" stroke="#3B1A0A" stroke-width="3.6" stroke-linecap="round" fill="none"/>
</g>
```

### Ryan (square)

```svg
<g id="cast-ryan">
  <rect x="-22" y="156" width="17" height="34" rx="8" fill="#6B4F2A"/>
  <rect x="5" y="156" width="17" height="34" rx="8" fill="#6B4F2A"/>
  <rect x="-26" y="184" width="23" height="12" rx="6" fill="#1E1B3A"/>
  <rect x="3" y="184" width="23" height="12" rx="6" fill="#1E1B3A"/>
  <rect x="-38" y="96" width="76" height="66" rx="14" fill="#15803D"/>
  <rect x="-38" y="96" width="64" height="66" rx="14" fill="#22C55E"/>
  <path d="M-10 96 L0 108 L10 96 Z" fill="#FFFFFF"/>
  <path d="M-28 104 Q-44 128 -14 134" stroke="#15803D" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M28 104 Q44 128 14 134" stroke="#15803D" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M0 122 Q-16 104 -6 96 Q2 106 0 122 Z" fill="#4ADE80"/>
  <path d="M0 122 Q16 102 8 94 Q-2 106 0 122 Z" fill="#16A34A"/>
  <path d="M-15 121 L15 121 L11 148 L-11 148 Z" fill="#C2410C" stroke="#C2410C" stroke-width="3" stroke-linejoin="round"/>
  <rect x="-17" y="118" width="34" height="7" rx="3.5" fill="#EA580C"/>
  <circle cx="-13" cy="134" r="8" fill="#C99066"/>
  <circle cx="13" cy="134" r="8" fill="#C99066"/>
  <rect x="-38" y="14" width="76" height="80" rx="24" fill="#C99066"/>
  <rect x="-38" y="36" width="7" height="18" rx="3.5" fill="#1E1B3A"/>
  <rect x="31" y="36" width="7" height="18" rx="3.5" fill="#1E1B3A"/>
  <path d="M-40 42 Q-40 6 0 6 Q40 6 40 42 Z" fill="#F97316"/>
  <rect x="-4" y="36" width="54" height="9" rx="4.5" fill="#EA580C"/>
  <rect x="-17" y="52" width="11" height="3.6" rx="1.8" fill="#1E1B3A"/>
  <rect x="6" y="52" width="11" height="3.6" rx="1.8" fill="#1E1B3A"/>
  <ellipse cx="-11" cy="63" rx="4.2" ry="5.2" fill="#1E1B3A"/>
  <ellipse cx="11" cy="63" rx="4.2" ry="5.2" fill="#1E1B3A"/>
  <circle cx="-9.6" cy="61" r="1.5" fill="#FFFFFF"/>
  <circle cx="12.4" cy="61" r="1.5" fill="#FFFFFF"/>
  <path d="M-8 76 Q0 82 8 76" stroke="#3B1A0A" stroke-width="3.6" stroke-linecap="round" fill="none"/>
</g>
```

## Appendix B. Worked turnaround (Wei Jie)

### Three-quarter

```svg
<g id="wei-jie-three-quarter">
  <ellipse cx="0" cy="198" rx="44" ry="5" fill="#E9E6DE"/>
  <rect x="4" y="156" width="15" height="34" rx="7.5" fill="#2F6BD9"/>
  <rect x="4" y="184" width="25" height="12" rx="6" fill="#C93636"/>
  <rect x="-17" y="156" width="15" height="34" rx="7.5" fill="#3B82F6"/>
  <rect x="-18" y="184" width="25" height="12" rx="6" fill="#EF4444"/>
  <path d="M14 104 Q34 118 32 140" stroke="#E0A100" stroke-width="16" stroke-linecap="round" fill="none"/>
  <circle cx="32" cy="142" r="8.5" fill="#F6D2A2"/>
  <rect x="-26" y="94" width="52" height="74" rx="26" fill="#E0A100"/>
  <rect x="-26" y="94" width="42" height="74" rx="21" fill="#FFC107"/>
  <path d="M-1 98 V114 M11 98 V114" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
  <path d="M-12 104 Q-34 118 -32 140" stroke="#FFC107" stroke-width="16" stroke-linecap="round" fill="none"/>
  <circle cx="-32" cy="142" r="8.5" fill="#F6D2A2"/>
  <rect x="-30" y="4" width="60" height="90" rx="30" fill="#F6D2A2"/>
  <path d="M-32 54 Q-38 -2 2 -2 Q36 0 32 36 Q30 22 20 18 Q8 26 -4 18 Q-14 22 -18 34 Q-26 40 -32 54 Z" fill="#1E1B3A"/>
  <path d="M-9 41 L3 38.5 M13 38.5 L23 41" stroke="#1E1B3A" stroke-width="3.6" stroke-linecap="round"/>
  <ellipse cx="-3" cy="52" rx="4.2" ry="5.6" fill="#1E1B3A"/>
  <ellipse cx="18" cy="52" rx="3.4" ry="5.4" fill="#1E1B3A"/>
  <circle cx="-1.6" cy="50" r="1.5" fill="#FFFFFF"/>
  <circle cx="19.2" cy="50" r="1.3" fill="#FFFFFF"/>
  <circle cx="-12" cy="64" r="4" fill="#F28C6B" opacity="0.5"/>
  <path d="M0 66 Q9 77 17 66 Z" fill="#7A2E1E"/>
</g>
```

### Profile

```svg
<g id="wei-jie-profile">
  <ellipse cx="0" cy="198" rx="44" ry="5" fill="#E9E6DE"/>
  <rect x="-3" y="156" width="15" height="34" rx="7.5" fill="#2F6BD9"/>
  <rect x="-4" y="184" width="28" height="12" rx="6" fill="#C93636"/>
  <rect x="-11" y="156" width="15" height="34" rx="7.5" fill="#3B82F6"/>
  <rect x="-12" y="184" width="28" height="12" rx="6" fill="#EF4444"/>
  <rect x="-22" y="94" width="44" height="74" rx="22" fill="#E0A100"/>
  <rect x="-22" y="94" width="34" height="74" rx="17" fill="#FFC107"/>
  <path d="M15 98 V114" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
  <path d="M-2 102 Q6 122 4 140" stroke="#E0A100" stroke-width="16" stroke-linecap="round" fill="none"/>
  <circle cx="4" cy="142" r="8.5" fill="#F6D2A2"/>
  <rect x="-28" y="4" width="56" height="90" rx="28" fill="#F6D2A2"/>
  <path d="M-30 62 Q-36 -2 2 -2 Q32 0 30 30 Q24 20 12 20 Q2 24 -4 32 Q-8 46 -14 50 Q-24 52 -30 62 Z" fill="#1E1B3A"/>
  <path d="M9 40.5 L20 42" stroke="#1E1B3A" stroke-width="3.6" stroke-linecap="round"/>
  <ellipse cx="15" cy="53" rx="3.8" ry="5.6" fill="#1E1B3A"/>
  <circle cx="16.4" cy="51" r="1.4" fill="#FFFFFF"/>
  <circle cx="6" cy="65" r="4" fill="#F28C6B" opacity="0.5"/>
  <path d="M15 67 Q21 75 27 67 Z" fill="#7A2E1E"/>
</g>
```

### Back

```svg
<g id="wei-jie-back">
  <ellipse cx="0" cy="198" rx="44" ry="5" fill="#E9E6DE"/>
  <rect x="-20" y="156" width="15" height="34" rx="7.5" fill="#3B82F6"/>
  <rect x="5" y="156" width="15" height="34" rx="7.5" fill="#3B82F6"/>
  <rect x="-24" y="184" width="22" height="12" rx="6" fill="#EF4444"/>
  <rect x="2" y="184" width="22" height="12" rx="6" fill="#EF4444"/>
  <rect x="-30" y="94" width="60" height="74" rx="30" fill="#E0A100"/>
  <rect x="-30" y="94" width="50" height="74" rx="25" fill="#FFC107"/>
  <rect x="-24" y="86" width="48" height="24" rx="12" fill="#E0A100"/>
  <path d="M-14 104 Q-40 118 -38 140" stroke="#FFC107" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M21 103 Q40 118 40 140" stroke="#E0A100" stroke-width="16" stroke-linecap="round" fill="none"/>
  <circle cx="-38" cy="142" r="8.5" fill="#F6D2A2"/>
  <circle cx="40" cy="142" r="8.5" fill="#F6D2A2"/>
  <rect x="-34" y="4" width="68" height="90" rx="34" fill="#F6D2A2"/>
  <path d="M-36 62 Q-40 -2 0 -2 Q40 -2 36 62 Q30 68 0 66 Q-30 68 -36 62 Z" fill="#1E1B3A"/>
</g>
```