---
name: color-combinations
description: "Pick colors that are defensible instead of guessed. Wraps Sanzo Wada's 'A Dictionary of Color Combinations' (1918) — all 348 combinations as queryable data — plus a WCAG/CIEDE2000 tool and a method for turning a brand color into a full token system. Use when choosing or auditing ANY color: brand palette, accent color, CTA color, dark/light surfaces, chart series, venture or category colors, state colors (success/warning/danger), or when asked 'is this color right', 'what goes with X', 'our brand color is X', 'fix the palette', 'these colors clash', 'pick a color scheme'. Also use before writing color tokens into globals.css, tailwind.config, or a design-system file."
---

# Color Combinations

Two failure modes this skill exists to prevent:

1. **Colors picked by vibe.** A hex chosen because it looked good in the editor, on
   one screen, against one background. Wada's 348 combinations are a corpus of
   pairings that a color theorist spent years testing — use them as the source
   instead of inventing.
2. **A palette that can't survive contact with a real UI.** One accent value cannot
   clear 4.5:1 on both a black and a cream surface. Palettes that ignore this ship
   unreadable buttons.

## The data

`data/sanzo-wada-348.csv` — all 348 combinations, extracted from the vector fills of
the HexPot PDF edition, not retyped or eyeballed. 120 two-color, 120 three-color,
108 four-color; 1032 swatches.

**Verified against the rendering, not just the parse:** `scripts/verify.py` re-renders
the PDF and compares the real pixel at every swatch centre to the CSV — currently
1032/1032 exact, 0 mismatches. `scripts/extract.py` rebuilds the CSV from the PDF, so
the whole dataset is reproducible rather than trusted. See `references/method.md`.

The source PDF sits at `references/A Dictionary of Color Combinations.pdf` on local
machines but is **not committed** to the public `claude-config` mirror — it is a
third-party file, and redistributing it isn't ours to do. The CSV is measured data and
carries everything the tooling needs. Re-download the PDF from hexpot.com if you want
the plates themselves; `references/method.md` documents how it was parsed.

```
id,page,n,c1,c2,c3,c4
1,2,2,#DE4500,#29BDAD,,
```

## The tool

`scripts/palette.py` — stdlib only, no install. Prints color swatches directly in
the terminal via ANSI truecolor.

```bash
S=~/.claude/skills/color-combinations/scripts/palette.py

# Starting from an existing brand color
python3 $S near "#C9885C" 10        # closest book colors (CIEDE2000)
python3 $S with "#C9885C" --tol 8   # combos containing that color
python3 $S with "#C9885C" --n 4     # ...only 4-color combos

# Starting from nothing
python3 $S browse --n 3 --hue teal            # explore by size and hue family
python3 $S browse --n 4 --on "#030303"        # only combos legible on your ground
python3 $S tokens 296 --ground dark           # combo → CSS tokens, roles assigned,
python3 $S tokens "#1B3644,#F5F5B8,#D99E73"   #   every ratio measured and warned on

# Verifying anything
python3 $S check "#C9885C" +#F2EDE4   # WCAG vs black, white and a custom surface
python3 $S pair  "#C9885C" "#030303"  # one contrast ratio
python3 $S show  282 296              # print combos by id
python3 $S scale "#C9885C" 9          # tint/shade ramp at even lightness steps
```

`with` and `near` match perceptually (CIEDE2000), so a brand hex that isn't literally
in the book still finds its neighbourhood. dE ≤ 2 is invisible, ≤ 10 is the same color
family, ≥ 20 is a different color.

`tokens` is the one that does real work: it assigns ground / foreground / accent /
support by lightness and chroma, derives the missing light-surface accent variant by
walking lightness until it clears 4.5:1, and **warns instead of silently emitting a
palette that fails**. If the combination has no colour dark (or light) enough to be a
ground, it refuses outright and tells you the plate is a *category* palette — good for
chart series or tags over your own neutral, useless as a UI surface. Pass an explicit
ground as the first hex to override. Never hand-write a token block when this can
generate it.

## Two starting points

**Greenfield — no brand color yet.** Don't invent one. Pick a *plate*, then assign
roles from it:

```bash
python3 $S browse --n 4 --on "#0B0908"   # 4-colour plates legible on your ground
python3 $S show 272 282 294              # look at the shortlist properly
python3 $S tokens 282 --ground dark      # the winner → verified CSS tokens
```

Then read Method steps 3–7 below to turn that token block into a real system. The
plate gives you colors that already work together; the method makes them survive a UI.

**Existing brand.** Start at Method step 1 and work down.

## Method

Work in this order. Do not skip to picking hexes.

### 1. Find the brand color, don't invent it

If there is a logo, **sample it** rather than trusting any value already in the CSS —
they drift. The existing token is often a stale approximation.

```bash
python3 -c "
from PIL import Image; from collections import Counter
print(Counter(Image.open('logo.png').convert('RGB').getdata()).most_common(5))"
```

### 2. Anchor it in the book

`near <brand-hex>` gives the closest Wada color; `with <brand-hex>` gives every
combination built on that neighbourhood. Those partner colors are the palette's
candidate supporting colors — they arrive pre-tested against the brand hue.

### 3. Build a ramp, not a color

A single brand hex cannot serve both grounds. Verify, don't assume:

| Role | Requirement |
|---|---|
| `--brand` | ≥ 4.5:1 on the dark surface (≥ 7:1 to use for body text) |
| `--brand-light` | ≥ brand, for hover/emphasis on dark |
| `--brand-deep` | ≥ 4.5:1 on the **light** surface — this is the one people forget |

Check every one with `check`. Record the ratio in a comment next to the token so the
next person doesn't have to re-derive it.

### 4. Give states two variants each

success / warning / danger each need a dark-surface and a light-surface value, for
the same reason. Pull them from the book — Wada has deep greens, golds and crimsons
that sit with earth tones far better than `#22c55e` / `#dc2626`.

### 5. Assign roles, then enforce hierarchy

The most common brand failure is not a wrong hue — it is the **wrong color in the
primary role**. If the logo is copper and the site's accent, CTA, focus ring and
hero section are all lime, the brand is lime, whatever the logo says.

- The brand color takes accent, CTA and focus.
- A trend color, if kept at all, is demoted to a named utility token with a written
  restriction ("never a CTA, max once per view"). An unrestricted token gets reused.
- Roughly 60% ground / 30% supporting / 10% accent. If the accent is everywhere, it
  has stopped being an accent.

### 6. Families for sets

Category colors — ventures, chart series, tags — should come from **one** combination
rather than being picked one at a time. Filter for: every member clears 4.5:1 on the
background, and minimum pairwise hue separation is large enough to tell them apart
(≥ 30°, ideally ≥ 50°). See `references/method.md` for the filter script.

### 7. Warm and cool

An all-warm palette goes flat and an all-cool one goes clinical. One cool anchor
surface in a warm palette (or the reverse) makes the brand color read as an event.
Wada's combinations do this constantly — steal the pairing.

## Established palettes

Brand palettes derived with this method live in `references/brands/`. Read the
relevant one before touching colors on that project; do not re-derive or "improve"
it ad hoc — the values there are measured, and a casual tweak silently breaks a
contrast guarantee.

- `references/brands/impactors-academy.md` — copper `#C9885C` on black, the org-wide
  brand. Covers impactors-academy, ia-pro, prospectbuddy and any new IA property.

**Adding a brand:** derive it with the method, then write one file in that directory
following the same shape — token table with provenance and measured ratios, states,
and any restricted tokens with the restriction written down. A palette nobody wrote
down gets re-invented within a month.

## Cautions

- Wada's originals are **1918 print pigments** converted CMYK→HEX. They are a
  starting point for screen, not a spec — always re-check contrast after picking.
- Several combinations are gorgeous and completely unusable as UI (two mid-tone
  colors with 1.2:1 between them). Beauty in a swatch pair says nothing about
  legibility as text.
- WCAG 2.1 ratios are the floor, not the goal. Large display type can sit at 3:1;
  body text should clear 7:1 where the palette allows it.
