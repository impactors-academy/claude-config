# Loc — brand palette

Loc is a light-surface venture site (cream/white grounds, near-black ink text) —
the inverse of impactors-academy's black-ground "ink" world. It shares the org's
warm hue family but does not use the org's black-ground theme itself.

Applies to `loc/frontend` only. Tokens live in `app/globals.css`
(`--loc-*` custom properties), consumed via `tailwind.config.ts`
(`text-loc-terracotta`, `bg-loc-amber`, etc.).

## Core

| Token | Hex | Role | Contrast |
|---|---|---|---|
| `--loc-terracotta` | `#A16036` | working accent on light — links, CTAs, active nav | 4.95:1 on white — AA |
| `--loc-sand` | `#F7EDD8` | highlight backgrounds, stat strips | — |
| `--loc-amber` | `#FFB852` | **org-assigned venture color** (impactors-academy.md "Venture colors" table — L80 in the shared warm family) | 12.01:1 on black, 9.87:1 on `--loc-night` — AAA. **1.72:1 on white — fails.** Dark-surface / decorative only, same as before this was corrected from a non-canonical `#D4A44C`. |
| `--loc-night` | `#231B15` | heading ink, dark section backgrounds (footer, CTA) | 16.95:1 on white — AAA. 1.22:1 on true black `#030303` — do not pair with the org's `--ia-black`, they're too close |
| `--loc-stone` | `#7F694D` | body/meta text | 5.21:1 on white, 4.80:1 on `--loc-cream` — AA |
| `--loc-cream` | `#FAF5EC` | card/surface warm white | — |
| `--loc-copper` | `#C9885C` | logo mark only — the org's exact copper | 7.03:1 on black, 2.93:1 on white |
| `--loc-slate` | `#1B3644` | cool anchor (Wada #296 companion) | 12.67:1 on white |

## Usage rules

- `--loc-amber` text only ever appears on `--loc-night` or a dark hero
  scrim/overlay — confirmed across every current usage site
  (`HeroSection`, `Footer`, homepage Partner CTA, `PropertyCard`/
  `ExperienceCard` badges pairing it with `--loc-night` text on top of it).
  Never use it as text on `--loc-cream` or white — it fails outright (1.72:1).
- `--loc-terracotta` is the light-surface equivalent of the org's
  `--ia-copper-deep` rule: on light grounds, don't reach for the org's
  literal copper (`#C9885C`, only 2.93:1 on white) — use terracotta instead.
- `--loc-night` reads as nearly black but is **not** the org's `--ia-black`
  (`#030303`) — they're 1.22:1 apart and must not be used as a pair (e.g.
  don't put loc-night text on ia-black, or vice versa, expecting AAA).

## Why loc is light-mode, not the org's black "ink" world

The org's shared "ink" world (`--ia-black` ground, cream text, copper accent)
is impactors-academy's own execution of the brand, not a mandate that every
venture site shares one literal dark theme. Loc's site was built light-mode
from the start (cream/white grounds throughout stays/experiences/blog/store),
and a full re-skin to the org's dark "ink" world would touch essentially
every component in `loc/frontend` — treated as a separate, larger project,
not bundled into a content/IA pass. What *is* shared and enforced today: the
one color the org explicitly assigns to Loc (`--loc-amber` → `#FFB852`) now
matches the canonical value in `impactors-academy.md`'s venture-colors table,
so the one point of required consistency actually holds.

## Reproduce any number here

```bash
S=~/.claude/skills/color-combinations
python3 $S/scripts/palette.py check "#FFB852" +"#231B15"
python3 $S/scripts/palette.py check "#A16036" +"#FFFFFF"
```
