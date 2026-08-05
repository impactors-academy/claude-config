# Impactors Academy — brand palette

**Brand = the logo: copper on black.** Everything else is drawn from Sanzo Wada's
*A Dictionary of Color Combinations* and verified against WCAG 2.1.

Applies org-wide: impactors-academy, ia-pro, loc, prospectbuddy, and any new IA
property. Adopt these tokens rather than re-deriving a palette per project.

## Core

| Token | Hex | Provenance | Contrast |
|---|---|---|---|
| `--ia-black` | `#030303` | logo ground | — |
| `--ia-copper` | `#C9885C` | **sampled from the logo mark** | 7.03:1 on black — AAA |
| `--ia-copper-light` | `#D99E73` | Wada (dE 6.3 from the logo) | 8.93:1 on black — AAA |
| `--ia-copper-pale` | `#F2AD78` | Wada | 10.8:1 on black — AAA |
| `--ia-copper-deep` | `#8B4E22` | — | 5.61:1 on cream — AA |
| `--ia-cream` | `#F2EDE4` | paper | 17.7:1 on black — AAA |

The copper is the **exact** logo value, not an approximation. The old `--ia-terra`
`#C87B3F` was close but wrong, and it never appeared in the logo.

Two copper variants exist because one cannot serve both grounds: `#C9885C` on cream
is only 2.51:1 and fails outright. **On light surfaces always use `--ia-copper-deep`.**

## Supporting — Wada combination #296

`#F5F5B8` cream · `#D99E73` tan · `#5E4017` umber · `#1B3644` slate

| Token | Hex | Role |
|---|---|---|
| `--ia-umber` | `#5E4017` | dividers, borders on dark — decorative only, 2.18:1 |
| `--ia-slate` | `#1B3644` | the cool anchor; keeps the warmth from going flat |
| `--ia-sand` | `#EBD999` | warm muted text on dark (14.7:1), secondary paper |

## States

Each has a dark- and a light-surface variant; one value cannot clear 4.5:1 on both.

| | dark surface | light surface |
|---|---|---|
| success | `#40C945` (9.5:1) | `#00592E` (7.3:1) |
| warning | `#E0B81F` (10.9:1) | `#8C6510` (4.5:1) |
| danger | `#FF616B` (7.1:1) | `#A10B2B` (6.9:1) |

## The lemon green — removed

`#C8F135` was the site's primary accent. There is **no token for it.** Not demoted,
not restricted — removed. Do not reintroduce it.

It was first kept as a restricted `--ia-signal` on the argument that the hue is
book-attested: Wada pairs that neighbourhood with the brand tan on plate 32
(`#D99E73 + #7AFF00`), and `#C8F135` sits dE 1.8 from his `#BDF226`. That argument is
true and was still the wrong call. A token that exists gets reused, and the
restriction lives in a document nobody opens at the moment of writing CSS. If
something needs to shout, `--ia-copper-pale` on dark or `--ia-sand` does it inside
the brand.

The original fault was hierarchy, not hue — a non-logo color held accent, CTA,
focus-ring and a full-bleed section, so the site's brand was lime while the logo said
copper. But once the brand is settled as copper on black, the lime has no role left
to play, and keeping a slot open for it is just deferring the decision.

## Color worlds

Section-level themes. `[data-world="…"]` sets bg / fg / accent together.

| World | Ground | Text | Accent |
|---|---|---|---|
| `ink` | black | cream | copper |
| `paper` | cream | black | copper-deep |
| `obsidian` | `#15110E` | cream | copper-light |
| `slate` | `#1B3644` | cream | copper-pale |
| `copper` | copper | **black** | black |

`copper` is the logo full-bleed — black on copper, 7.03:1. The old `terra` world put
cream on the same ground at ~2.5:1 and was unreadable.

## Venture colors — one warm family

All Sanzo Wada values inside the brand's own hue neighbourhood: a **46° arc**, told
apart by **lightness** (L 50 / 68 / 80 / 95), not hue.

| Venture | Hex | L | on black |
|---|---|---|---|
| Loc | `#FFB852` amber | 80 | 12.01:1 |
| Beyond the Football Pitch | `#A3AD00` olive | 68 | 8.38:1 |
| IA Business & Finance | `#B85E00` burnt orange | 50 | 4.56:1 |
| IA Pro | `#F5F5B8` pale wheat | 95 | 18.30:1 |

**Do not spread these further around the wheel.** The first pass did: it filtered the
book for the four-color plate with *maximum* hue separation and landed on plate 282
(magenta / tan / mint / violet, a 308° span). Maximising hue separation selects, by
construction, the least cohesive set available — and the constraint was imaginary.
Each orb already carries a name label and a fixed position in the scene, and the
method's own rule is never to rely on hue alone for categories. Hue separation was
bought with brand cohesion and paid for nothing.

The general lesson, which applies well beyond this brand: **decide what is actually
distinguishing your categories before optimising for hue distance.** If a label,
position, or ordering already does it, spend the freedom on cohesion instead.

## Reproduce any number here

```bash
S=~/.claude/skills/color-combinations
python3 $S/scripts/palette.py check "#C9885C" +#F2EDE4
python3 $S/scripts/palette.py show 32 282 296
```
