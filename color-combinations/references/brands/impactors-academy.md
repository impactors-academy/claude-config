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

## Signal — the lemon green

`--ia-signal` `#C8F135` is **not a brand color**. It was the site's primary accent;
it is now a restricted utility token: live/new markers, code marks, data-viz maximum.
**Never a CTA, never a focus ring, never a full section, max once per view.**

Worth knowing: the green is not a mistake of taste. Wada pairs this exact
neighbourhood with the brand tan — combination #32 is `#D99E73 + #7AFF00`, and
`#C8F135` sits dE 1.8 from Wada's `#BDF226`. The problem was never the hue. It was
that a non-logo color held accent, CTA, focus-ring and a full-bleed section, which
made the site's brand lime while the logo said copper. Hierarchy, not hue.

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

## Venture colors — Wada combination #282

One combination, so the ventures read as a family instead of a rainbow. All clear
4.5:1 on black; minimum pairwise hue separation 51.8°.

| Venture | Hex | on black |
|---|---|---|
| Loc | `#94FF94` | 16.7:1 |
| Beyond the Football Pitch | `#B875EB` | 6.7:1 |
| IA Business & Finance | `#C2975A` | 7.7:1 |
| IA Pro | `#E62E73` | 4.9:1 |

IA Business & Finance carries the tan because it is the venture closest to the
parent brand.

## Reproduce any number here

```bash
S=~/.claude/skills/color-combinations
python3 $S/scripts/palette.py check "#C9885C" +#F2EDE4
python3 $S/scripts/palette.py show 32 282 296
```
