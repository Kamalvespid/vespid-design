---
name: vespid-badge-generator
description: Generate Vespid badges (Milestone, Streak, Campaign) as export-safe SVG with text outlined to paths, following the Vespid badge steering guide. Use when asked to design, create or review a Vespid badge.
---

# Vespid Badge Steering File

Use this file as the system guideline whenever you generate a Vespid badge. Paste it in (or attach it), then add one short request, for example:

> I need a Milestone badge for Budgeting mastery.

The generator must follow every rule below, ask nothing it can work out from this file, and return the output described in **§9 Output contract**.

---

## 1. How to read a request

Work through these steps in order before drawing anything.

1. **Family.** Decide which of the three families the request belongs to (§3–§5). If the request names none, infer it: counts of lessons, paths, quizzes or categories → Milestone; consecutive days → Streak; a dated event, festival or partner series → Campaign.
2. **Sub-type** (Milestone only). Lesson completion, Learning Path (LP) completion, Quiz score, or Category mastery.
3. **Tier or threshold.** Use the tier or day count the request gives. If it gives none, produce **all tiers** for Milestone, or the single named threshold for Streak.
4. **Name.** Apply the naming rules for that family.
5. **Emblem or character.** Milestone uses an icon, Streak uses the flame, Campaign uses a cast character with a prop.
6. **Render** the badge from the template for that family. Never invent a new shape.

If something is truly ambiguous (e.g. "a badge for saving" could be a milestone or a campaign), choose the most likely reading. State the assumption in one line at the top of your answer.

---

## 2. Global rules (all families)

| Rule | Detail |
|---|---|
| Shape = family | Hexagon = Milestone · Shield = Streak · Half-moon medal = Campaign. Never mix them. |
| Colour = tier / intensity | Colours come only from the token tables in this file. |
| Emblem = what was achieved | One emblem per badge, white, with a drop shadow in the badge's lip colour. |
| Rendering | Flat fills, rounded corners. Depth comes from a darker "lip" offset below the shape, never from black outlines or gradients. |
| Premium effects are rationed | Sparkles and light rays only where §3 and §4 allow them. |
| **No mascot** | The Vespid mascot never appears on a badge. Badges must stay white-label and co-brandable. |
| Learning, not products | Badges reward learning behaviour only. Never reward buying, trading or signing up for a financial product, and never show a product as the hero. |
| White-label | Every colour, font and character is a token or swappable asset. Do not bake brand marks into the art. |
| Partner logos | Never draw or trace a real company's logo. Use a logo file the requester supplies, placed in the partner chip (§5.6); if none is supplied, use the grey placeholder. |
| No regulated titles | Badge names must not use licensed professional titles: Adviser/Advisor, Planner, Consultant, Broker, Agent, Certified, Licensed. If a requested title contains one, flag it and suggest an alternative (e.g. Money Advisor → Money Mentor / Money Buddy); proceed with the original only if the requester confirms. |
| Accessibility | Every SVG has an `aria-label` with the badge name. Text is converted to outlined paths in the final file (§2.6), so the `aria-label` is what screen readers use. |

### 2.1 Fonts (tokens)

| Token | Default | Used for |
|---|---|---|
| `font.display` | Anton | Campaign big word |
| `font.rounded` | Baloo 2, weight 800 | Streak day number, UI labels |
| `font.label` | Nunito Sans, weight 800 | Campaign kicker |

### 2.2 Core colours (tokens)

| Token | Hex | Role |
|---|---|---|
| `ink` | `#1E1B3A` | Tags, ribbons, outlines on campaign type |
| `ink.deep` | `#0F0D24` | Lip under ink elements |
| `honey` | `#FFC233` | Kicker text, the "limited-time" signal |
| `paper` | `#F5F3EE` | Background the badges sit on |
| `white` | `#FFFFFF` | Emblems, highlights |

### 2.3 Sizes

| Size | px | Where | Adjustments |
|---|---|---|---|
| Hero | 144–160 | Unlock celebration, detail sheet | Full detail |
| Moment | 80–100 | Profile grid | Full detail |
| Micro | 40–48 | Chips, toasts | Drop sparkles and rays. Campaign: **always omit the partner chip** (circle or pill), including in previews; this is mandatory. |

### 2.4 States

| State | Treatment |
|---|---|
| Earned | Full colour |
| Newly earned | Full colour, plus a soft honey glow behind the badge and a red `NEW` pill (`#E8391C`, white text) until it is first viewed |
| In progress | Locked colours (below), plus a honey `#FFB800` progress stroke (6 px) tracing the badge edge, and progress text under the badge (e.g. "6 / 10 lessons") |
| Locked | Face `#DAD7E4`, inner `#E9E7F0`, lip `#B5B1C6`. Emblem replaced by `lock-simple` in `#8A869E` at 70% of normal emblem size. No shine, no emblem shadow, no sparkles. |
| Campaign: coming soon | Locked colours, dashed rim, a `?` in the top half, and the kicker tag reading `SOON` |
| Campaign: missed / expired | Hidden from users who missed it; never shown greyed in their cabinet |

### 2.5 Export-safe SVG (Figma, Illustrator, apps)

Every SVG must open correctly in Figma, not just in a browser:

- **No `paint-order`**, no `<textPath>`, no filters, no `<style>` blocks or CSS classes. Put colours in `fill` / `stroke` attributes.
- **Outlines behind text** are separate layers (see §5.3), never a stroke on the visible text.
- **Fonts** are referenced by their exact Google Fonts names (`Anton`, `Baloo 2`, `Nunito Sans`) so Figma can match them.
- **Build with live `<text>`, deliver outlines.** Write the badge with `<text>` exactly as the template shows (all geometry rules in §5.3 assume it), then convert every `<text>` to `<path>` before delivering (§2.6). The final file never depends on installed fonts.
- **`clip-path` is fine.** Figma imports it as a mask.
- **Previewing:** preview the **outlined** SVG. Because the type is already shapes, it looks the same everywhere: in a chat preview, as a standalone `.svg`, in Figma and in the app. Only if outlining was not possible (§2.6 fallback) do you need an inline HTML preview that loads the three Google Fonts (`Anton`, `Baloo 2:wght@800`, `Nunito Sans:wght@800`).

### 2.6 Outlining text (final output)

The skill folder ships `scripts/outline_text.py` and `scripts/vespid_glyphs.json` (glyph shapes for Anton, Baloo 2 ExtraBold and Nunito Sans ExtraBold, SIL Open Font Licence). The script uses only the Python standard library, so it needs no installs, fonts or network.

1. Save the finished live-text SVG, e.g. `price-buster.svg`.
2. Run, from the skill folder or with the full path to the script:
   ```
   python3 scripts/outline_text.py price-buster.svg
   ```
   This writes `price-buster.outlined.svg`. Several files can be passed at once.
3. Check that the outlined file contains no `<text>` elements. Each `<text>` becomes one `<path>` that keeps its `fill`, `stroke`, `stroke-width` and `stroke-linejoin`, so the three-layer big word (shadow, outline, white) survives as three paths. Each path carries the original word in `data-text`.
4. Deliver the **outlined** file as the badge. Keep the live-text file only if the requester asks for an editable version.

**If the script reports an error:**
- *Characters not in the bundled font:* the glyph set covers printable ASCII plus `· ’ ‘ “ ” – — × … • é`. Rename or respell; never swap in another font.
- *Nested markup (`<tspan>`):* rewrite as one `<text>` per line, as the templates do.

**Fallback (no code execution available, e.g. some other AI tools):** deliver the live-text SVG, state clearly "Text is not outlined yet", and tell the requester to outline it in Figma (select the text layers → Flatten, ⌘/Ctrl + E) before exporting for the app.

---

## 3. Milestone: chunky hexagon

Rewards depth of learning. There are four sub-types, each with four tiers.

### 3.1 Sub-types

| Sub-type | Track name | Phosphor icon (Fill) | Example tier thresholds *(illustrative; confirm with product)* |
|---|---|---|---|
| Lesson completion | **Bookworm** | `book-open` | 10 / 50 / 150 / 500 lessons |
| Learning Path (LP) completion | **Pathfinder** | `flag-banner` | 1 / 5 / 15 / 30 paths |
| Quiz score | **Sharpshooter** | `target` | 5 / 25 / 100 / 250 perfect quizzes |
| Category mastery | **one persona per category** (see 3.2) | per category (see 3.2) | Basics / Intermediate / Advanced / Mastered within that category |

### 3.2 Category mastery: persona and icon

Vespid says **category**, not "topic". Each category gets a one-word persona name and one icon:

| Category | Persona name | Icon |
|---|---|---|
| Saving | Saver | `piggy-bank` |
| Budgeting | Budgeter | `calculator` |
| Investing | Investor | `trend-up` |
| Debt & credit | Debt Buster | `credit-card` |
| Protection & insurance | Protector | `shield-check` |
| Tax | Tax Pro | `receipt` |
| Retirement / EPF | Retire Ready | `hand-coins` |
| Housing | Homeowner | `house` |

**A category not listed above:**
- **Name:** a positive persona noun of at most 12 characters (e.g. "Earner", "Giver").
- **Icon:** the Phosphor Fill icon that most literally depicts it.
- **Never reuse** the `book-open`, `flag-banner` or `target` icons; they belong to the other three sub-types.

### 3.3 Naming

Format: `<Track or persona> <Roman tier>`, e.g. `Bookworm III` or `Budgeter II`.

| Roman | Tier |
|---|---|
| I | Bronze |
| II | Silver |
| III | Gold |
| IV | Royal |

### 3.4 Tier tokens

| Tier | face | inner | lip | Sparkles (`spark`) | Light rays (`ray`) |
|---|---|---|---|---|---|
| I Bronze | `#F29A4A` | `#F7B06B` | `#B9611F` | none | none |
| II Silver | `#A9B8CC` | `#BFCBDA` | `#6F7F96` | none | none |
| III Gold | `#FFC107` | `#FFD23F` | `#D18E00` | `#FFB300` | none |
| IV Royal | `#8B5CF6` | `#A27BFF` | `#5B2FC9` | `#8B5CF6` | `#E3D6FF` |

### 3.5 SVG template

viewBox `-12 -12 144 144`. Replace the `{tokens}`. `{icon}` is the path `d` from the Phosphor **Fill** icon's 256×256 SVG (`@phosphor-icons/core/assets/fill/<name>-fill.svg`, MIT licence).

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="-12 -12 144 144" role="img" aria-label="{name}">
  <!-- Royal only: light rays -->
  <circle cx="60" cy="62" r="36" fill="none" stroke="{ray}" stroke-width="72" stroke-dasharray="7 11.85"/>
  <!-- lip, face, inner (rounded via stroke) -->
  <path d="M60 21 L100 44 L100 90 L60 113 L20 90 L20 44 Z" fill="{lip}" stroke="{lip}" stroke-width="12" stroke-linejoin="round"/>
  <path d="M60 14 L100 37 L100 83 L60 106 L20 83 L20 37 Z" fill="{face}" stroke="{face}" stroke-width="12" stroke-linejoin="round"/>
  <path d="M60 25 L90 42.5 L90 77.5 L60 95 L30 77.5 L30 42.5 Z" fill="{inner}" stroke="{inner}" stroke-width="8" stroke-linejoin="round"/>
  <!-- shine -->
  <path d="M28 32.4 L44 23.2" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity="0.6"/>
  <!-- emblem: shadow then white -->
  <g transform="translate(33.12 36.12) scale(0.20625)" fill="{lip}"><path d="{icon}"/></g>
  <g transform="translate(33.12 33.12) scale(0.20625)" fill="#FFFFFF"><path d="{icon}"/></g>
  <!-- Gold and Royal only: sparkles -->
  <g fill="{spark}">
    <path d="M108 4 Q108 14 118 14 Q108 14 108 24 Q108 14 98 14 Q108 14 108 4 Z"/>
    <path d="M8 92 Q8 99 15 99 Q8 99 8 106 Q8 99 1 99 Q8 99 8 92 Z"/>
    <path d="M118 84 Q118 89 123 89 Q118 89 118 94 Q118 89 113 89 Q118 89 118 84 Z"/>
  </g>
</svg>
```

Delete the rays element unless the tier is Royal. Delete the sparkles group for Bronze and Silver.

---

## 4. Streak: chunky flame shield

Rewards daily return. Each threshold is earned permanently and is never removed if the streak later breaks.

### 4.1 Thresholds and tokens

| Days | Name | face | inner | lip | flame | core | Sparkles | Rays |
|---|---|---|---|---|---|---|---|---|
| 3 | Spark | `#FFB25B` | `#FFD199` | `#DB7A1F` | `#FF8A1F` | `#FFE066` | none | none |
| 7 | Kindled | `#FF9A3D` | `#FFC28A` | `#CC5F12` | `#FF6A13` | `#FFD43B` | none | none |
| 14 | Blazing | `#FF7A45` | `#FFB08F` | `#C8431A` | `#F2441D` | `#FFD43B` | `#FF7A45` | none |
| 30 | On Fire | `#F2503B` | `#FF9A86` | `#B32615` | `#D91E0F` | `#FFC107` | `#F2503B` | none |
| 60 | Blue Flame | `#3D7BFF` | `#8FB3FF` | `#1F4FC9` | `#1D4ED8` | `#BDF4FF` | `#3D7BFF` | none |
| 100 | Centurion | `#FFC107` | `#FFE07A` | `#D18E00` | `#FF6A13` | `#FFF3B0` | `#FFB300` | `#FFE9A8` |
| 365 | Legend | `#8B5CF6` | `#B99BFF` | `#5B2FC9` | `#FFC107` | `#FFF3B0` | `#8B5CF6` | `#E3D6FF` |

**A new threshold** (e.g. 200 days): interpolate between the two neighbouring rows, and give it a one- or two-word "heat" name.

### 4.2 SVG template

viewBox `-12 -12 144 144`.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="-12 -12 144 144" role="img" aria-label="{name}, {days}-day streak">
  <circle cx="60" cy="56" r="36" fill="none" stroke="{ray}" stroke-width="72" stroke-dasharray="7 11.85"/><!-- 100+ only -->
  <path d="M60 13 L100 25 V60 C100 86 83 102 60 111 C37 102 20 86 20 60 V25 Z" fill="{lip}" stroke="{lip}" stroke-width="10" stroke-linejoin="round"/>
  <path d="M60 6 L100 18 V53 C100 79 83 95 60 104 C37 95 20 79 20 53 V18 Z" fill="{face}" stroke="{face}" stroke-width="10" stroke-linejoin="round"/>
  <path d="M60 16 L91 25.5 V53 C91 73 78 86 60 93 C42 86 29 73 29 53 V25.5 Z" fill="{inner}" stroke="{inner}" stroke-width="6" stroke-linejoin="round"/>
  <path d="M26 16.2 L44 10.8" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity="0.6"/>
  <path transform="translate(0 3)" d="M60 22 C65 34 80 40 80 58 C80 71 71 80 60 80 C49 80 40 71 40 58 C40 48 46 42 51 36 C51 44 54 48 59 49 C59 40 55 32 60 22 Z" fill="{lip}"/>
  <path d="M60 22 C65 34 80 40 80 58 C80 71 71 80 60 80 C49 80 40 71 40 58 C40 48 46 42 51 36 C51 44 54 48 59 49 C59 40 55 32 60 22 Z" fill="{flame}"/>
  <path d="M60 50 C64 56 70 60 70 66 C70 72 65 76 60 76 C55 76 50 72 50 66 C50 60 55 58 60 50 Z" fill="{core}"/>
  <g fill="{spark}"><!-- 14+ only -->
    <path d="M108 2 Q108 12 118 12 Q108 12 108 22 Q108 12 98 12 Q108 12 108 2 Z"/>
    <path d="M10 70 Q10 77 17 77 Q10 77 10 84 Q10 77 3 77 Q10 77 10 70 Z"/>
    <path d="M114 62 Q114 67 119 67 Q114 67 114 72 Q114 67 109 67 Q114 67 114 62 Z"/>
  </g>
  <rect x="32" y="92" width="56" height="24" rx="12" fill="{lip}"/>
  <rect x="32" y="88" width="56" height="24" rx="12" fill="#FFFFFF"/>
  <text x="60" y="105.5" text-anchor="middle" font-family="Baloo 2, sans-serif" font-weight="800" font-size="16" fill="#1E1B3A">{days}</text>
</svg>
```

---

## 5. Campaign: half-moon medal + breakout type

Rewards taking part in a time-limited, usually partner-backed campaign.

### 5.1 Anatomy (top to bottom)

1. **Top half:** a sky-tinted window with a cast character (§6) acting out the badge name. The character may break out above the window and rim, by at most about 10% of the badge width.
2. **Split line:** a thin bar in the lip colour.
3. **Kicker tag:** an `ink` tag centred on the split line, holding the small word(s) in `honey`. This tag is the "limited-time" signal.
4. **Big word:** condensed `font.display`, white fill with an `ink` outline and an `ink` drop shadow, always level, never tilted.
5. **Partner chip:** a white, **outline-free** chip on the bottom rim holding the partner logo. It is a circle for symbol logos and a pill for wordmarks (§5.6). Its drop shadow uses the badge's lip colour.
6. **No date on the badge.** The campaign period lives on the detail screen and in the Events tab.

### 5.2 Splitting the name into kicker + big word

- The badge name is split into **kicker** (first word or words) + **big word** (the last, most "heroic" word).
- **Examples:**
  - Price Buster → PRICE / BUSTER
  - Fine Print Detective → FINE PRINT / DETECTIVE
  - Under the Hood Expert → UNDER THE HOOD / EXPERT
  - Protection Pro → PROTECTION / PRO
- **Big word:** ≤ 9 letters. If the last word is longer, rephrase or abbreviate with product sign-off; never shrink it below 24 pt.
- **Kicker:** ≤ 14 characters, uppercase.

### 5.3 Typography geometry (must hold; prevents overlap)

**Kicker tag:** `y = 51`, height `14`, `rx = 3`, centred at x = 60. The tag bottom is therefore at **65**.

| Kicker length | Tag width | Kicker font |
|---|---|---|
| ≤ 6 chars | 50 | 8.5 pt, letter-spacing 2, baseline y = 61.5 |
| 7–10 chars | 80 | 8.5 pt, letter-spacing 1.5, baseline y = 61.5 |
| 11–14 chars | 92 | 7.5 pt, letter-spacing 1, baseline y = 61 |

**Big word: size and baseline by letter count.** Use these values exactly. Don't calculate your own.

| Letters | ≤ 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|
| Size (pt) | 31 | 30 | 29 | 28 | 26 | 24 |
| Baseline y | 98 | 97.5 | 97 | 96.5 | 95.8 | 94.9 |

**Why these numbers:**
- Anton's capital letters are **0.86 of the font size** (measured from the font file).
- The word block runs from the top of the caps (outline included) to the bottom of the shadow.
- That block is **vertically centred between the tag bottom (y 65) and the partner chip top (y 107)**, with about 4 units clear on each side.
- Formula, for reference only: `baseline = 84.6 + 0.43 × size`.

- **Maximum size is 31 pt; minimum 24 pt.**
- **The shadow** is a copy of the word at `x + 1.5`, `baseline + 2.5`, with fill and stroke `ink`, stroke 5.
- **The outline** is a second copy at the same position, fill and stroke `ink`, stroke 4.5.
- **The main word** is a third copy on top: white fill, **no stroke**. Never use `paint-order`; Figma and many tools ignore it and draw the outline over the letters.

### 5.4 Colour sets (choose one per campaign)

Choose a set that contrasts with the character's signature colour (§6.2). Within one series, don't repeat a set until all eight have been used.

| Set | face | lip | sky |
|---|---|---|---|
| Red | `#EF4444` | `#B91C1C` | `#FECACA` |
| Blue | `#3B82F6` | `#1D4ED8` | `#BFDBFE` |
| Orange | `#FF8A1F` | `#C2570C` | `#FFD9B0` |
| Violet | `#8B5CF6` | `#5B2FC9` | `#DDD6FE` |
| Amber | `#F59E0B` | `#B45309` | `#FDE68A` |
| Green | `#22C55E` | `#15803D` | `#BBF7D0` |
| Teal | `#14B8A6` | `#0F766E` | `#99F6E4` |
| Pink | `#EC4899` | `#BE185D` | `#FBCFE8` |

### 5.5 SVG template

viewBox `-16 -14 152 152`. The character group uses **cast coordinates** (§6.1) and is scaled into the window.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="152" height="152" viewBox="-16 -14 152 152" role="img" aria-label="{name}">
  <defs><clipPath id="{uid}-win"><rect x="-16" y="-14" width="152" height="74"/></clipPath></defs>
  <circle cx="60" cy="66" r="54" fill="{lip}"/>
  <circle cx="60" cy="60" r="54" fill="{face}"/>
  <path d="M14 60 A46 46 0 0 1 106 60 Z" fill="{sky}"/>
  <path d="M30 60 A30 30 0 0 1 90 60 Z" fill="#FFFFFF" opacity="0.35"/>
  <g clip-path="url(#{uid}-win)">
    <g transform="translate(60 2.5) scale(0.42)">
      <!-- CHARACTER + PROP in cast coordinates (§6) -->
    </g>
  </g>
  <rect x="14" y="58" width="92" height="4" rx="2" fill="{lip}"/>
  <rect x="{60 - tagW/2}" y="51" width="{tagW}" height="14" rx="3" fill="#1E1B3A"/>
  <text x="60" y="61.5" text-anchor="middle" font-family="Nunito Sans, sans-serif" font-weight="800" font-size="8.5" letter-spacing="2" fill="#FFC233">{KICKER}</text>
  <text x="61.5" y="{baseline + 2.5}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{size}" fill="#1E1B3A" stroke="#1E1B3A" stroke-width="5" stroke-linejoin="round">{BIG WORD}</text>
  <text x="60" y="{baseline}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{size}" fill="#1E1B3A" stroke="#1E1B3A" stroke-width="4.5" stroke-linejoin="round">{BIG WORD}</text>
  <text x="60" y="{baseline}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{size}" fill="#FFFFFF">{BIG WORD}</text>
  <!-- partner chip: circle version (symbol logos); see §5.6 for the pill version -->
  <circle cx="60" cy="121" r="11" fill="{lip}"/>
  <circle cx="60" cy="118" r="11" fill="#FFFFFF"/>
  <rect x="54.5" y="112.5" width="11" height="11" rx="3" fill="#6E6A85"/><!-- placeholder: replace with the supplied logo, fitted in the 14×14 box centred on (60,118) -->
</svg>
```

**No partner:** for a Vespid-only campaign, remove the chip elements.

### 5.6 Partner chip rules

- **No outline**, ever. The chip is plain white; depth comes from its shadow in the badge's `{lip}` colour, offset 3 units down.
- **Choose the chip shape from the logo's shape:**

| Logo type | Test | Chip | Logo box |
|---|---|---|---|
| Symbol / mark | width ÷ height ≤ 1.6 | Circle, r 11, centre (60, 118) | 14 × 14, centred |
| Wordmark | width ÷ height > 1.6 | Pill, 44 × 20, rx 10, centred on (60, 118) | 36 × 12, centred |

The chip sits half over the medal's bottom edge. Its top is at y 107, which is the lower limit for the big word (§5.3).

Pill version:

```svg
<rect x="38" y="111" width="44" height="20" rx="10" fill="{lip}"/>
<rect x="38" y="108" width="44" height="20" rx="10" fill="#FFFFFF"/>
<!-- supplied wordmark, scaled uniformly to fit 36×12, centred on (60,118) -->
```

- **Placing a supplied logo:** scale uniformly (never stretch), keep the partner's original colours, and don't add effects. If the logo is white or very light, ask for a dark or full-colour version rather than recolouring it.
- **Micro size:** omit the chip completely (§2.3).

---

## 6. Characters (Campaign only)

### 6.1 Style rules

1. **One hero shape per person:** circle, pill, triangle or square. It sets the silhouette and hints at personality.
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

### 6.2 The cast (working names)

Skin tones are the brightened set from 10 Oct 2026.

| Name | Shape | Personality | Skin | Signature build |
|---|---|---|---|---|
| **Aina** | Circle | The Planner: warm, organised | `#D8A27F` | Teal hijab `#14B8A6` (shade `#0E9384`) framing an oval face; coral pill tunic `#FF7A59` (shade `#E2604A`) |
| **Wei Jie** | Pill | The Spontaneous One: fun, generous | `#F6D2A2` | Tall pill-shaped head; black messy top hair; yellow pill hoodie `#FFC107` (shade `#E0A100`) with white strings; blue jeans, red sneakers |
| **Priya** | Triangle | The Go-getter: ambitious, runs a side hustle | `#A86B3D` | Big dark hair mass with a top bun and side curls; magenta A-line top `#DB2777` (shade `#B0175E`); small gold earrings |
| **Ryan** | Square | The Steady One: calm, practical | `#C99066` | Rounded-square head; orange cap `#F97316` (brim `#EA580C`); green boxy shirt `#22C55E` (shade `#15803D`) with white V collar |

**Assigning cast members:**
- **Always start from the reference drawing in Appendix B.** Copy the person's head, hair or headwear, face kit, skin and body exactly, then change only the arms, expression and props for the scene. Never redraw a cast member from the description alone; that is how characters drift between badges.
- **Rotate the cast** across a series so each person leads at least once. A person may open and close a series as a story arc.
- **Swap headwear when a prop or role needs it** (e.g. Ryan's detective hat). Body shape and signature colour stay.
- **Check names against the lesson copy.** If a cast name is already used for a different person in that campaign's quiz scenarios, flag it.

### 6.3 Turning a badge name into a scene

Use this formula: **verb + prop that makes the name literal and playful.** The prop must be readable at 96 px.

| Badge name | Scene |
|---|---|
| Price Buster | Snaps an "RM" price tag in two, one half in each raised hand |
| Risk Tamer | Holds a leash on a grumpy little storm cloud with a lightning bolt |
| Myth Slayer | Slices a "?" speech bubble with a foam sword |
| Fine Print Detective | Wears a detective hat, holds a magnifying glass over one eye, holds a document of tiny lines |
| Under the Hood Expert | Goggles on forehead, screwdriver raised, an opened phone showing a gear |
| Protection Pro | Holds a shield with a tick, gives a thumbs up, wears a small cape |

**Expressions:** use one of the four shared expressions.

| Expression | Face | Use for |
|---|---|---|
| Happy | Default face | Default |
| Celebrate | Arms up, eyes as `^` arcs, open mouth | Most campaign wins |
| Proud | Eyes closed as smile arcs, hand on chest | Completion-type badges |
| Thinking | Asymmetric brows, hand on chin, thought dots | Not used on badges |

---

## 7. Copy rules

| Element | Rule |
|---|---|
| Badge name | Title Case, ≤ 3 words, a positive persona or achievement. Never a financial product name, and never a regulated professional title (§2). |
| Unlock rule | One sentence, starts with a verb: "Complete…", "Finish…", "Score…". |
| Language | English by default. If bilingual copy is requested, the BM name goes on the detail screen only; the badge art keeps one language. |
| Partner credit | "with [Partner]" on the detail screen. Never inside the art except as the logo chip. |

---

## 8. Do / Don't checklist (run before returning)

- [ ] Correct family shape. Colours only from the token tables.
- [ ] Sparkles and rays only where §3.4 and §4.1 allow them.
- [ ] Emblem is a Phosphor **Fill** icon, white, with a lip-coloured shadow (Milestone).
- [ ] Campaign big word ≤ 9 letters; size and baseline taken from the §5.3 table (max 31 pt); centred between the tag and the chip. Kicker tag at y = 51. Chip centred at y 118. No date on the badge.
- [ ] No mascot. No drawn or traced real logos. No Vespid branding on characters.
- [ ] Partner chip has no outline, uses the lip-coloured shadow, and is the right shape (circle for marks, pill for wordmarks).
- [ ] At Micro size the partner chip is gone.
- [ ] Badge name has no regulated title (Adviser, Planner, Consultant, Broker, Agent, Certified, Licensed).
- [ ] Cast member copied from Appendix B, not redrawn.
- [ ] Character respects the §6.1 rules and reads at 96 px.
- [ ] Arms are rooted (L1–L4) and the view is front or three-quarter (V1).
- [ ] `aria-label` present. Text outlined with `scripts/outline_text.py` (no `<text>` left), or the fallback note given.
- [ ] Export-safe (§2.5): no `paint-order`, no `textPath`, no `<style>`; the big word's outline is its own layer under the white text.

---

## 9. Output contract

Return, in this order:

1. **One-line assumption** (only if you had to infer something).
2. **Spec block:**
   ```yaml
   family: Milestone | Streak | Campaign
   subtype: Lesson completion | LP completion | Quiz score | Category mastery   # Milestone only
   name: "Budgeter III"
   tier: III Gold            # or days: 30, or campaign: "#1 The True Cost"
   unlock_rule: "Complete the Advanced level of the Budgeting category."
   colours: { face: "#FFC107", inner: "#FFD23F", lip: "#D18E00" }
   emblem: calculator        # or character: "Wei Jie — snaps a price tag"
   partner: none | "[Partner name]"
   ```
3. **One self-contained, outlined SVG per badge** (§2.6), built from the family template, at Hero size (144 px; Campaign 152 px).
4. **If the request implies a set** (e.g. "Budgeting mastery" with no tier), return all four tiers in order I → IV.

---

## 10. Example prompts

| Prompt | What the generator does |
|---|---|
| "I need a Milestone badge for Budgeting mastery." | Category mastery; persona **Budgeter**; icon `calculator`; returns Budgeter I–IV in Bronze → Royal. Gold gets sparkles; Royal gets sparkles and rays. |
| "Milestone badge for completing 5 learning paths." | LP completion; **Pathfinder II** (Silver); icon `flag-banner`. |
| "Streak badge for 200 days." | New threshold between Centurion and Legend; interpolated colours; a new heat name (e.g. "Star Flame"); rays allowed. |
| "Campaign badge 'Bill Buster' for the April utilities series with a partner." | Kicker BILL / big word BUSTER (6 letters → 29 pt, baseline 97); Ryan (copied from Appendix B) with a torn utility bill; a colour set not used yet in the series; placeholder partner chip (no real logo drawn). |
| "Campaign badge 'Money Advisor' with Grab, logo attached." | Flags "Advisor" as a regulated title and suggests Money Mentor; on confirmation builds MONEY / ADVISOR (7 letters → 28 pt, baseline 96.5). Grab's logo is a wordmark → pill chip, no outline, original colours. |

---

## Appendix A. Icon path data (Phosphor Icons v2.1.1, Fill weight, MIT licence)

Use these `d` values directly as `{icon}` in the Milestone template (256×256 source, already matched to the template transform). For any icon not listed here, take the path from `@phosphor-icons/core/assets/fill/<name>-fill.svg`; never draw an icon freehand.

**book-open**
```
M240,56V200a8,8,0,0,1-8,8H160a24,24,0,0,0-24,23.94,7.9,7.9,0,0,1-5.12,7.55A8,8,0,0,1,120,232a24,24,0,0,0-24-24H24a8,8,0,0,1-8-8V56a8,8,0,0,1,8-8H88a32,32,0,0,1,32,32v87.73a8.17,8.17,0,0,0,7.47,8.25,8,8,0,0,0,8.53-8V80a32,32,0,0,1,32-32h64A8,8,0,0,1,240,56Z
```

**flag-banner**
```
M239.22,59.44l-45.63,95.82a3.54,3.54,0,0,1-.16.34l-34.21,71.84a8,8,0,1,1-14.44-6.88L173.62,160H40a8,8,0,0,1-5.66-13.66L76.69,104,34.34,61.66A8,8,0,0,1,40,48H232a8,8,0,0,1,7.22,11.44Z
```

**target**
```
M221.87,83.16A104.1,104.1,0,1,1,195.67,49l22.67-22.68a8,8,0,0,1,11.32,11.32L167.6,99.71h0l-37.71,37.71-23.95,23.95a40,40,0,0,0,62-35.67,8,8,0,1,1,16-.9,56,56,0,0,1-95.5,42.79h0a56,56,0,0,1,73.13-84.43L184.3,60.39a87.88,87.88,0,1,0,23.13,29.67,8,8,0,0,1,14.44-6.9Z
```

**piggy-bank**
```
M226,88.08c-.4-1-.82-2-1.25-3a87.93,87.93,0,0,0-30.17-37H216a8,8,0,0,0,0-16H112a88.12,88.12,0,0,0-87.72,81A32,32,0,0,0,0,144a8,8,0,0,0,16,0,16,16,0,0,1,8.57-14.16A87.69,87.69,0,0,0,46,178.22l12.56,35.16A16,16,0,0,0,73.64,224H86.36a16,16,0,0,0,15.07-10.62l1.92-5.38h57.3l1.92,5.38A16,16,0,0,0,177.64,224h12.72a16,16,0,0,0,15.07-10.62L221.64,168H224a24,24,0,0,0,24-24V112A24,24,0,0,0,226,88.08ZM152,72H112a8,8,0,0,1,0-16h40a8,8,0,0,1,0,16Zm28,56a12,12,0,1,1,12-12A12,12,0,0,1,180,128Z
```

**calculator**
```
M200,24H56A16,16,0,0,0,40,40V216a16,16,0,0,0,16,16H200a16,16,0,0,0,16-16V40A16,16,0,0,0,200,24ZM88,200a12,12,0,1,1,12-12A12,12,0,0,1,88,200Zm0-40a12,12,0,1,1,12-12A12,12,0,0,1,88,160Zm40,40a12,12,0,1,1,12-12A12,12,0,0,1,128,200Zm0-40a12,12,0,1,1,12-12A12,12,0,0,1,128,160Zm40,40a12,12,0,1,1,12-12A12,12,0,0,1,168,200Zm0-40a12,12,0,1,1,12-12A12,12,0,0,1,168,160Zm16-56a8,8,0,0,1-8,8H80a8,8,0,0,1-8-8V64a8,8,0,0,1,8-8h96a8,8,0,0,1,8,8Z
```

**trend-up**
```
M240,56v64a8,8,0,0,1-13.66,5.66L200,99.31l-58.34,58.35a8,8,0,0,1-11.32,0L96,123.31,29.66,189.66a8,8,0,0,1-11.32-11.32l72-72a8,8,0,0,1,11.32,0L136,140.69,188.69,88,162.34,61.66A8,8,0,0,1,168,48h64A8,8,0,0,1,240,56Z
```

**credit-card**
```
M224,48H32A16,16,0,0,0,16,64V192a16,16,0,0,0,16,16H224a16,16,0,0,0,16-16V64A16,16,0,0,0,224,48ZM136,176H120a8,8,0,0,1,0-16h16a8,8,0,0,1,0,16Zm64,0H168a8,8,0,0,1,0-16h32a8,8,0,0,1,0,16ZM32,88V64H224V88Z
```

**shield-check**
```
M208,40H48A16,16,0,0,0,32,56v56c0,52.72,25.52,84.67,46.93,102.19,23.06,18.86,46,25.26,47,25.53a8,8,0,0,0,4.2,0c1-.27,23.91-6.67,47-25.53C198.48,196.67,224,164.72,224,112V56A16,16,0,0,0,208,40Zm-34.32,69.66-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35a8,8,0,0,1,11.32,11.32Z
```

**receipt**
```
M216,40H40A16,16,0,0,0,24,56V208a8,8,0,0,0,11.58,7.15L64,200.94l28.42,14.21a8,8,0,0,0,7.16,0L128,200.94l28.42,14.21a8,8,0,0,0,7.16,0L192,200.94l28.42,14.21A8,8,0,0,0,232,208V56A16,16,0,0,0,216,40ZM176,144H80a8,8,0,0,1,0-16h96a8,8,0,0,1,0,16Zm0-32H80a8,8,0,0,1,0-16h96a8,8,0,0,1,0,16Z
```

**hand-coins**
```
M128.09,57.38a36,36,0,0,1,55.17-27.82,4,4,0,0,1-.56,7A52.06,52.06,0,0,0,152,84c0,1.17,0,2.34.12,3.49a4,4,0,0,1-6,3.76A36,36,0,0,1,128.09,57.38ZM240,160.61a24.47,24.47,0,0,1-13.6,22l-.44.2-38.83,16.54a6.94,6.94,0,0,1-1.19.4l-64,16A7.93,7.93,0,0,1,120,216H16A16,16,0,0,1,0,200V160a16,16,0,0,1,16-16H44.69l22.62-22.63A31.82,31.82,0,0,1,89.94,112H140a28,28,0,0,1,27.25,34.45l41.84-9.62A24.61,24.61,0,0,1,240,160.61Zm-16,0a8.61,8.61,0,0,0-10.87-8.3l-.31.08-67,15.41a8.32,8.32,0,0,1-1.79.2H112a8,8,0,0,1,0-16h28a12,12,0,0,0,0-24H89.94a15.86,15.86,0,0,0-11.31,4.69L56,155.31V200h63l62.43-15.61,38-16.18A8.56,8.56,0,0,0,224,160.61ZM168,84a36,36,0,1,0,36-36A36,36,0,0,0,168,84Z
```

**house**
```
M224,120v96a8,8,0,0,1-8,8H160a8,8,0,0,1-8-8V164a4,4,0,0,0-4-4H108a4,4,0,0,0-4,4v52a8,8,0,0,1-8,8H40a8,8,0,0,1-8-8V120a16,16,0,0,1,4.69-11.31l80-80a16,16,0,0,1,22.62,0l80,80A16,16,0,0,1,224,120Z
```

**lock-simple**
```
M208,80H176V56a48,48,0,0,0-96,0V80H48A16,16,0,0,0,32,96V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V96A16,16,0,0,0,208,80ZM96,56a32,32,0,0,1,64,0V80H96Z
```

---

## Appendix B. Cast reference drawings (copy these, don't redraw)

Full figures in cast coordinates (§6.1): about 200 units tall, centred on x = 0, feet at y ≈ 196. Inside a campaign badge, place the figure in the `translate(60 2.5) scale(0.42)` group; everything below y ≈ 137 is hidden by the split line. Keep the head, hair or headwear, face, skin and body; replace the arms and props for each scene, and swap expression using the face kit (§6.1 and §6.3).

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
