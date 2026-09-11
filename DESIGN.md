---
version: alpha
name: Impactors-Academy-design-analysis
description: A copper-on-black editorial system for Impactors Academy, built from the exact color sampled off the brand logo mark and extended through Sanzo Wada's "A Dictionary of Color Combinations" (1918), verified against WCAG 2.1 at every pairing. The canvas defaults to near-black (#030303) with warm cream body copy; copper is the brand's single accent color, spent scarcely. Display type runs Clash Grotesk (uppercase, wide-tracked) against a humanist General Sans body and JetBrains Mono for code/meta. Section-level "color worlds" (ink / paper / obsidian / slate / copper) let the same component re-skin per section while keeping contrast ratios locked. Motion is glass-morphic and editorial — nav blur, clip-path reveals, split-text — never decorative for its own sake.

colors:
  black: "#030303"
  obsidian: "#15110E"
  white: "#fafafa"
  cream: "#F2EDE4"
  copper: "#C9885C"
  copper-light: "#D99E73"
  copper-pale: "#F2AD78"
  copper-deep: "#8B4E22"
  umber: "#5E4017"
  slate: "#1B3644"
  sand: "#EBD999"
  gray-200: "#e5e5e5"
  gray-400: "#a3a3a3"
  gray-600: "#525252"
  gray-900: "#171717"
  success-on-dark: "#40C945"
  success-on-light: "#00592E"
  warning-on-dark: "#E0B81F"
  warning-on-light: "#8C6510"
  danger-on-dark: "#FF616B"
  danger-on-light: "#A10B2B"

typography:
  hero:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: "clamp(2.25rem, 8vw, 10rem)"
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  hero-sm:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: "clamp(1.5rem, 5.5vw, 4.5rem)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.02em
  display-4xl:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: 2.25rem
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.015em
  display-3xl:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: 1.875rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.015em
  display-2xl:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  display-xl:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: 1.25rem
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "General Sans, system-ui, sans-serif"
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "General Sans, system-ui, sans-serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "General Sans, system-ui, sans-serif"
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "General Sans, system-ui, sans-serif"
    fontSize: 0.75rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  button:
    fontFamily: "Clash Grotesk, sans-serif"
    fontSize: 0.875rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  code:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
  brand-button: 0px

spacing:
  1: 0.25rem
  2: 0.5rem
  4: 1rem
  6: 1.5rem
  8: 2rem
  12: 3rem
  16: 4rem
  24: 6rem
  32: 8rem
  section: "clamp(5rem, 10vw, 10rem)"

motion:
  fast: 150ms
  base: 300ms
  slow: 600ms
  xslow: 900ms
  ease-out: "cubic-bezier(0.16, 1, 0.3, 1)"
  ease-in-out: "cubic-bezier(0.87, 0, 0.13, 1)"
  ease-spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"

components:
  nav-glass:
    backgroundColor: "rgba(10, 10, 10, 0.55)"
    backgroundColorScrolled: "rgba(10, 10, 10, 0.82)"
    borderColor: "rgba(242, 237, 228, 0.08)"
    height: "{nav.h}"
    backdropFilter: "blur(20px) saturate(160%)"
  mobile-menu:
    backgroundColor: "rgba(10, 10, 10, 0.97)"
    backdropFilter: "blur(24px)"
    textColor: "{colors.cream}"
  btn-brand:
    backgroundColor: transparent
    fillColorOnHover: "{colors.copper}"
    textColor: "{colors.cream}"
    textColorOnHover: "{colors.black}"
    typography: "{typography.button}"
    border: "1.5px solid currentColor"
    rounded: "{rounded.brand-button}"
    padding: "0.75em 1.75em"
  btn-ghost:
    backgroundColor: transparent
    backgroundColorOnHover: "rgba(242, 237, 228, 0.06)"
    textColor: "{colors.cream}"
    typography: "{typography.button}"
    border: "1.5px solid rgba(242, 237, 228, 0.25)"
    borderOnHover: "{colors.cream}"
    padding: "0.75em 1.75em"
  glass-card:
    backgroundColor: "rgba(8, 8, 8, 0.72)"
    border: "1px solid rgba(242, 237, 228, 0.1)"
    backdropFilter: "blur(28px) saturate(160%)"
  glass-chip:
    backgroundColor: "rgba(255, 255, 255, 0.06)"
    backgroundColorOnHover: "rgba(255, 255, 255, 0.12)"
    border: "1px solid rgba(255, 255, 255, 0.14)"
    backdropFilter: "blur(18px) saturate(150%)"
  contact-input:
    backgroundColor: "rgba(255, 255, 255, 0.07)"
    borderColor: "rgba(242, 237, 228, 0.18)"
    borderColorFocused: "{colors.copper}"
    backgroundColorFocused: "rgba(201, 136, 92, 0.1)"
    textColor: "{colors.cream}"
    typography: "{typography.body-md}"
    padding: "0.75rem 1rem"
  badge-copper:
    backgroundColor: "{colors.copper}"
    textColor: "{colors.black}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
  marquee-track:
    animation: "marquee-x 22s linear infinite"
    pausesOnHover: true
  world-ink:
    backgroundColor: "{colors.black}"
    textColor: "{colors.cream}"
    accent: "{colors.copper}"
  world-paper:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.black}"
    accent: "{colors.copper-deep}"
  world-obsidian:
    backgroundColor: "{colors.obsidian}"
    textColor: "{colors.cream}"
    accent: "{colors.copper-light}"
  world-slate:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.cream}"
    accent: "{colors.copper-pale}"
  world-copper:
    backgroundColor: "{colors.copper}"
    textColor: "{colors.black}"
    accent: "{colors.black}"
---

## Overview

Impactors Academy's system is built backwards from a single fixed point: **the exact copper sampled off the logo mark** (`{colors.copper}` — #C9885C). Nothing in the palette was picked first and matched to the logo after — the logo hex *is* token zero, and every other color in the system (tints, the cream paper tone, the Wada-sourced supporting hues, even the semantic success/warning/danger pairs) was chosen to sit correctly around that fixed copper, at a verified WCAG contrast, on a verified ground. This is the opposite of most marketing-site palettes, which start from a mood board and never check whether the "brand color" clears AA anywhere it's actually used.

The default canvas is **near-black** (`{colors.black}` — #030303), not a dark gray — the logo's own ground. Body copy runs warm cream (`{colors.cream}` — #F2EDE4), never pure white, so text and background both sit inside the same warm-neutral family as the copper accent. Copper itself is spent scarcely: CTA fills, focus rings, list markers, blockquote rules, hover states — never large background fields, except in the one deliberate full-bleed "logo" moment (the `copper` world, black text on a copper field).

Display type is **Clash Grotesk**, always uppercase on buttons and nav labels, wide letter-spacing (0.04em) — a grotesque, not a serif, which puts Impactors Academy in different territory from the cream-serif-editorial AI brands (Claude, etc.) despite a similarly warm palette. Body copy runs **General Sans**, a humanist sans that keeps long-form reading comfortable against the dark ground. **JetBrains Mono** handles anything code- or meta-adjacent.

The system's most distinctive mechanic is **color worlds** — `[data-world="…"]` attributes that re-skin an entire section (background, foreground, accent, muted-text alpha, border alpha) as one atomic swap. Five worlds exist: `ink` (black/cream/copper — the default), `paper` (cream/black/copper-deep — the one light section), `obsidian` (a copper-warmed near-black, for elevated panels), `slate` (the system's only cool section, a deliberate counterweight that keeps the warmth from reading as monotone), and `copper` (full-bleed logo colors, black on copper). Components are written once and re-themed by whichever world wraps them — a feature-card doesn't know if it's rendering in `ink` or `obsidian`, it just reads `--world-*` custom properties.

**Key Characteristics:**
- Near-black canvas (`{colors.black}` — #030303) with warm cream text (`{colors.cream}` — #F2EDE4). Never pure white-on-black — every "white" in the system is warm-tinted.
- Copper (`{colors.copper}` — #C9885C) is the *only* accent color and is sampled directly from the logo, not approximated. A retired lime/acid green (`#C8F135`) was the prior primary accent and is explicitly gone — see "Removed: the lemon green" below.
- Five section-level "color worlds" (`ink`/`paper`/`obsidian`/`slate`/`copper`) swap background/foreground/accent/muted/border together via `[data-world]` attributes, each independently verified to clear WCAG AA.
- Clash Grotesk display type: uppercase, 600 weight, wide tracking (0.04em) on buttons/nav; tighter negative tracking (-0.015 to -0.02em) at hero sizes.
- Buttons are square-cornered (`{rounded.brand-button}` = 0px) with a signature fill-wipe hover: a copper `::before` layer scales in from the left on `:hover`, text flips to black mid-transition.
- Every surface material is glass — `nav-glass`, `glass-card`, `glass-chip`, the mobile-menu overlay — `backdrop-filter: blur()` over translucent black/white, never an opaque flat card.
- Motion is restrained and functional: clip-path reveals, split-text word wrapping, a slow 22s-loop marquee — governed by three duration tokens (`{motion.fast}` 150ms / `{motion.base}` 300ms / `{motion.slow}` 600ms) and three easings, all respecting `prefers-reduced-motion`.
- Section rhythm is fluid, not fixed: `{spacing.section}` is `clamp(5rem, 10vw, 10rem)` — 80px on mobile scaling to 160px on wide desktop, rather than a single hard-coded value.

## Colors

### Brand
- **Copper** (`{colors.copper}` — #C9885C): The brand's one accent color, sampled directly from the logo mark — not a designer's approximation. 7.03:1 on black (AAA). Used for CTA fills, focus-ring outlines, blockquote rules, list-marker dots, inline links, active toolbar states.
- **Copper Light** (`{colors.copper-light}` — #D99E73): Hover/emphasis variant on dark grounds, 8.93:1 on black. Also the default focus-ring color site-wide.
- **Copper Pale** (`{colors.copper-pale}` — #F2AD78): Subtle accent on dark, 10.8:1 on black. Used as the `slate` world's accent so it stays legible against the cool ground.
- **Copper Deep** (`{colors.copper-deep}` — #8B4E22): The **only** copper variant permitted on light surfaces — full-strength copper on cream is 2.51:1 and fails outright. 5.61:1 on cream (AA).

### Ground & Paper
- **Black** (`{colors.black}` — #030303): Default page canvas, the logo's own ground.
- **Obsidian** (`{colors.obsidian}` — #15110E): Elevated dark surface, warmed toward copper rather than neutral gray — used for the editor toolbar dropdown and other "raised" dark panels.
- **Cream** (`{colors.cream}` — #F2EDE4): Primary text color on dark, and the background of the `paper` world. 17.7:1 on black.
- **White** (`{colors.white}` — #fafafa): Rarely used directly; present as a neutral reference point, not a section ground.

### Supporting — Wada combination #296
- **Umber** (`{colors.umber}` — #5E4017): Decorative-only dividers and borders on dark surfaces (2.18:1 — never for text).
- **Slate** (`{colors.slate}` — #1B3644): The system's one cool-toned world background — a deliberate counterweight so the copper reads as an event rather than the wallpaper.
- **Sand** (`{colors.sand}` — #EBD999): Warm muted text on dark (14.7:1), secondary paper tone.

### Semantic (state)
Each state ships **two** values — one per surface — because no single hex clears 4.5:1 on both a black and a cream ground.
- **Success**: `{colors.success-on-dark}` #40C945 (9.5:1 on black) / `{colors.success-on-light}` #00592E (7.3:1 on cream).
- **Warning**: `{colors.warning-on-dark}` #E0B81F (10.9:1 on black) / `{colors.warning-on-light}` #8C6510 (4.5:1 on cream).
- **Danger**: `{colors.danger-on-dark}` #FF616B (7.1:1 on black) / `{colors.danger-on-light}` #A10B2B (6.9:1 on cream).

### Removed: the lemon green
`#C8F135` was formerly the site's primary accent, and **there is no token for it** — not demoted to a restricted role, removed outright. The color was book-attested (Sanzo Wada pairs that hue neighborhood with the brand's tan on plate 32, and the retired hex sits dE 1.8 from Wada's own `#BDF226`), and it was still the wrong call: the fault was that a non-logo color was carrying accent, CTA, focus-ring, and full-bleed-section duty simultaneously, so the *site's* brand was lime while the *logo's* brand was copper. Once copper-on-black was settled as the actual brand, keeping a restricted slot open for the lime was just deferring a decision that was already made. If a moment needs to shout, reach for `{colors.copper-pale}` on dark or `{colors.sand}` — both live inside the brand.

## Typography

### Font Family
Two self-hosted variable-weight families plus one monospace: **Clash Grotesk** (`--font-display`, weights 400/500/600/700, self-hosted `.woff2`) for all headlines, nav, and buttons; **General Sans** (`--font-body`, self-hosted) for body copy; **JetBrains Mono** (loaded from Google Fonts, weights 400/500) for code, kbd hints, and editor meta text. Fallback stacks: `sans-serif` for both display and body, `monospace` for code — no serif appears anywhere in the system.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero}` | clamp(2.25rem, 8vw, 10rem) | 600 | 1.0 | -0.02em | Homepage hero headline — the system's largest, fully fluid type |
| `{typography.hero-sm}` | clamp(1.5rem, 5.5vw, 4.5rem) | 600 | 1.05 | -0.02em | Secondary hero / sub-page headline |
| `{typography.display-4xl}` | 2.25rem | 600 | 1.15 | -0.015em | H1, major section heads |
| `{typography.display-3xl}` | 1.875rem | 600 | 1.2 | -0.015em | H2, sub-section heads |
| `{typography.display-2xl}` | 1.5rem | 600 | 1.2 | -0.01em | H3, card titles |
| `{typography.display-xl}` | 1.25rem | 600 | 1.25 | 0 | H4, small headers |
| `{typography.body-lg}` | 1.125rem | 400 | 1.6 | 0 | Intro paragraphs, lead text |
| `{typography.body-md}` | 1rem | 400 | 1.6 | 0 | Default running text, form inputs |
| `{typography.body-sm}` | 0.875rem | 400 | 1.6 | 0 | Secondary text, footer copy |
| `{typography.caption}` | 0.75rem | 400 | 1.5 | 0.02em | Fine print, editor footnotes |
| `{typography.button}` | 0.875rem | 600 | 1.2 | 0.04em, uppercase | All button and toolbar labels |
| `{typography.code}` | 0.875rem | 400 | 1.6 | 0 | Code blocks, kbd hints |

### Principles
Clash Grotesk carries the entire type-voice contrast on its own — it never appears below 600 weight for anything with brand presence (buttons, hero, section heads), and it's the *only* place uppercase + wide tracking (0.04em) is used. General Sans stays at 400 weight for all body copy; the system does not use a bold body weight anywhere — emphasis is carried by color (copper) or by switching to Clash Grotesk, not by weight within General Sans. Negative tracking scales with size: -0.02em at hero, tightening to 0 by the time headlines drop to `display-xl` — the letterforms get roomier as they get smaller so nothing at readable sizes over-tightens.

## Layout

### Spacing System
- **Base unit:** 4px (0.25rem), following an 8pt grid above the smallest tokens.
- **Tokens:** `{spacing.1}` 4px · `{spacing.2}` 8px · `{spacing.4}` 16px · `{spacing.6}` 24px · `{spacing.8}` 32px · `{spacing.12}` 48px · `{spacing.16}` 64px · `{spacing.24}` 96px · `{spacing.32}` 128px.
- **Section padding:** `{spacing.section}` — `clamp(5rem, 10vw, 10rem)` vertically, `clamp(1.25rem, 5vw, 6rem)` horizontally. Fluid rather than a fixed breakpoint value, so section rhythm scales continuously with viewport instead of jumping at a media query.
- **Max content width:** `.content-w` caps at 1320px, centered.

### Grid & Container
- Content is capped at 1320px (`.content-w`) and centered; section padding handles the outer gutter so inner grids rarely need their own margin.
- Feature/card grids follow standard responsive column drops (see Responsive Behavior below) rather than a fixed 12-column system baked into tokens.

### Whitespace Philosophy
Because `{spacing.section}` is a `clamp()` rather than a fixed value, the page's vertical rhythm compresses gracefully on small screens instead of needing a separate mobile override — the same token does both jobs. Cards and glass surfaces keep generous internal padding (`{spacing.6}`–`{spacing.8}`) so the blur/translucency effect reads as a distinct material rather than a thin outline.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no blur, body background shows through | Body copy sections, most of the `ink`/`paper`/`obsidian` world bands |
| Hairline border | 1px border at low alpha (`rgba(242,237,228,0.08–0.15)`) | Nav bottom edge, dividers, table cells |
| Glass card | `.glass-card` — 72%-opacity black + 28px blur + 1px hairline | Feature/content cards that need to read as "raised" without a hard shadow |
| Glass chip | `.glass-chip` — 6%-white fill + 18px blur + inset highlight + drop shadow | Icon buttons, small floating controls |
| Nav glass | `.nav-glass` — 55%→82% opacity black + 20px blur, thickens on scroll | The persistent top nav, the one component whose elevation is stateful |
| Full-bleed color | A `[data-world]` background fill, no shadow | Section-level color changes — depth comes from hue/value shift, not shadow |

The elevation philosophy is **glass-first, shadow rare**. Nearly every "raised" surface in the system is a translucent, blurred material over the world background rather than an opaque card with a drop shadow — this is consistent with the near-black canvas, where a conventional shadow barely reads anyway. The one true drop-shadow in the system lives inside `.glass-chip` (`0 6px 20px rgba(0,0,0,0.28)`), reserved for small floating controls that need to visually detach from a busy background.

### Decorative Depth
- `nav-glass.scrolled` thickens its own blur/opacity on scroll — the only component whose elevation changes based on page state rather than interaction state.
- `.marquee-track` runs a continuous 22s linear horizontal loop, pausing on hover — used for logo strips / partner rows.
- Clip-path reveals (`.clip-hidden` → `.clip-visible`) and split-text word wrapping (`.split-word-wrap`) drive most entrance motion; both respect `prefers-reduced-motion`.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.brand-button}` | 0px | `btn-brand` and `btn-ghost` — square corners are a deliberate brand signature, not an oversight |
| `{rounded.sm}` | 4px | Small inline chips, kbd tags, toolbar buttons |
| `{rounded.md}` | 8px | Inputs, embeds/iframes, editor toolbar |
| `{rounded.lg}` | 16px | Larger content cards, glass panels |
| `{rounded.full}` | 9999px | Badges, pills, avatar crops |

The zero-radius buttons are the system's sharpest brand tell: everything else in the UI (cards, inputs, embeds) is softly rounded, but the two primary CTA components are hard-cornered rectangles outlined in `currentColor` — closer to a stamped label than a typical rounded SaaS button.

### Photography & Illustrations
The marketing surface leans on typography, glass materials, and color-world transitions rather than photography as the primary hero device — hero sections are dominantly type-led (`{typography.hero}` at up to 10rem). Where imagery appears (blog embeds, testimonials), it sits inside rounded (`{rounded.md}`) containers with a neutral placeholder fill (`rgba(255,255,255,0.04)`) shown before load, so nothing flashes white against the black canvas.

## Components

### Navigation

**`nav-glass`** — Fixed top nav, blurred glass over the current world. Default `rgba(10,10,10,0.55)` background at `20px` blur; thickens to `rgba(10,10,10,0.82)` once `.scrolled` is applied. 1px bottom hairline border that also intensifies on scroll. Height token `{nav.h}` (4rem / 64px).

**`mobile-menu`** — Full-screen overlay, `rgba(10,10,10,0.97)` + `24px` blur, slides in via `translateY` with `ease-in-out` at 450ms. Centered flex column, `2.5rem` gap between links.

### Buttons

**`btn-brand`** — The signature CTA. Transparent by default, `1.5px solid currentColor` border, square corners (`{rounded.brand-button}`), Clash Grotesk uppercase label (`{typography.button}`). On hover, a copper `::before` layer scales in from the left (`transform: scaleX(0)→scaleX(1)`, `{motion.base}` / `{motion.ease-out}`) while the text color flips to black — a fill-wipe rather than a simple background swap. A variant pairs this with `btn-slide-text`, a vertically-sliding two-line text swap synced to the same hover.

**`btn-ghost`** — Secondary button. Transparent background, `1.5px solid rgba(242,237,228,0.25)` border, cream text, same square corners and uppercase Clash Grotesk label as `btn-brand`. Hover only brightens the border to full cream and adds a faint `rgba(242,237,228,0.06)` fill — no color-flip, so it stays visually subordinate to `btn-brand`.

### Cards & Surfaces

**`glass-card`** — General-purpose elevated content container. `rgba(8,8,8,0.72)` background, `28px` blur + `160%` saturate, `1px` hairline border at `rgba(242,237,228,0.1)`.

**`glass-chip`** — Small floating control (icon buttons, compact actions). `rgba(255,255,255,0.06)` fill, `18px` blur, inset top highlight plus a real drop shadow (`0 6px 20px rgba(0,0,0,0.28)`) — the one component that lifts on hover (`translateY(-1px)`) and settles on press.

**`contact-input`** — Form field. `rgba(255,255,255,0.07)` fill with `12px` blur, `1px` border at `rgba(242,237,228,0.18)`. On focus, border shifts to `{colors.copper}` and the fill warms to `rgba(201,136,92,0.1)` — the only place the copper accent tints a background fill rather than sitting as a stroke or text color.

### Color Worlds

**`world-ink`** (default) — Black background, cream text, copper accent. Muted text at `rgba(242,237,228,0.52)` (4.8:1).

**`world-paper`** — Cream background, black text, copper-**deep** accent (full-strength copper fails on cream). Muted text `rgba(10,10,10,0.60)` (4.9:1).

**`world-obsidian`** — Obsidian (`#15110E`) background, cream text, copper-light accent. The "elevated dark" world, used where a section needs to read as raised above pure black without leaving the dark family.

**`world-slate`** — Slate (`#1B3644`) background, cream text, copper-**pale** accent. The system's only cool-hued section — included deliberately so copper keeps reading as an event against a warm palette rather than fading into a monotone.

**`world-copper`** — Full copper background, **black** text and accent — the literal logo, full-bleed. Muted text needs a much higher alpha here (`rgba(3,3,3,0.82)`, 5.72:1) than on a light or dark ground, because copper is a mid-tone: alpha values are re-measured per world, never copied across.

### Other Surfaces

**`badge-copper`** — Pill badge, copper fill, black text, `{typography.caption}`, `{rounded.full}`.

**`marquee-track`** — Horizontal auto-scroll strip (logos, partner names), `22s` linear loop, pauses on hover.

## Do's and Don'ts

### Do
- Treat `{colors.copper}` as sampled-from-logo and fixed. Any change to it is a change to a locked org standard, not a design tweak — flag it explicitly rather than adjusting the hex in passing.
- Use `{colors.copper-deep}` — never full-strength copper — on any light/cream surface. Full copper on cream is 2.51:1 and fails WCAG outright.
- Pick a `[data-world]` deliberately per section and let its bundled muted/border alphas travel with it. Don't copy a muted-text alpha from one world into another — they're independently measured per ground.
- Keep buttons square (`{rounded.brand-button}` = 0px) and uppercase Clash Grotesk. This is one of the system's clearest brand signatures.
- Reach for glass materials (`glass-card`, `glass-chip`, `nav-glass`) before reaching for a flat card with a drop shadow — the near-black canvas is where blur reads best.
- Respect `prefers-reduced-motion` on every transition — it's wired into the button-hover and reveal animations already; extend new motion the same way.

### Don't
- Don't reintroduce `#C8F135` (the old lemon-green accent) in any form, restricted or otherwise. It's removed, not demoted — see "Removed: the lemon green."
- Don't round the brand buttons. A rounded `btn-brand`/`btn-ghost` breaks the one shape rule that reads as intentional rather than default.
- Don't use pure white or pure black in place of `{colors.cream}` / `{colors.black}` — every neutral in the system is warm-tinted on purpose.
- Don't bold General Sans for emphasis. Emphasis comes from color (copper) or from switching families to Clash Grotesk, not from a heavier body weight.
- Don't put copper on a large background field outside the dedicated `world-copper` moment — it's an accent, not a section fill.
- Don't skip the light-surface variant of a semantic color. Every state (success/warning/danger) needs both an on-dark and an on-light hex; neither clears 4.5:1 on both grounds.

## Responsive Behavior

### Breakpoints
The system leans on fluid `clamp()` values (hero type, section padding) rather than hard breakpoint jumps for its most prominent tokens, so most "breakpoint behavior" is really continuous scaling. Discrete layout changes (nav → hamburger, grid column drops) still follow standard mobile / tablet / desktop steps.

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | `nav-glass` collapses to hamburger, opening `.mobile-menu` full-screen; hero type sits near the low end of its `clamp()`; section padding compresses toward `5rem`/`1.25rem` |
| Tablet | 768–1024px | Nav stays horizontal but tightens; card grids typically drop to 2-up |
| Desktop | 1024–1440px | Full horizontal nav; card grids at full column count; hero type scales up within its `clamp()` |
| Wide | > 1440px | Hero type and section padding approach their `clamp()` ceiling (10rem hero, 10rem/6rem section padding); `.content-w` still caps at 1320px |

### Touch Targets
- `btn-brand` / `btn-ghost` padding (`0.75em 1.75em`) keeps tap targets comfortably above 44px at body-text sizes.
- `.glass-chip` icon buttons should be sized to at least 40–44px even though the base style doesn't hard-code a size — treat the visual chip size as a floor, not a cap.
- `contact-input` padding (`0.75rem 1rem`) plus 1rem body text clears standard form touch-target guidance.

### Collapsing Strategy
- Nav collapses to `.mobile-menu` below 768px — a full-screen blurred overlay, not a dropdown, consistent with the system's glass-first elevation language.
- Marquee tracks keep running at all widths (they're width-independent by design — `width: max-content` plus a translateX loop).
- Card grids reduce columns before they shrink card padding — glass materials need enough internal space for the blur/border treatment to read.

### Image / Embed Behavior
- Embeds (`.post-embed`, `iframe`) hold a fixed `16/9` aspect ratio at every width and paint a neutral `rgba(255,255,255,0.04)` placeholder before load, so nothing flashes white against the black canvas.
- Code blocks inside the editor/blog surfaces scroll horizontally rather than wrapping, keeping monospace alignment intact at narrow widths.

## Iteration Guide

1. Every color decision starts and ends at `{colors.copper}` — #C9885C, sampled from the logo. New colors get checked against it via the `color-combinations` skill (`palette.py check`), not eyeballed.
2. Work one `[data-world]` at a time. A component's own styles should never hard-code a background/foreground — they read `--world-bg` / `--world-fg` / `--world-accent` so the same markup re-skins across worlds.
3. Keep buttons square. If a new CTA variant needs rounding, that's a strong enough deviation from the system to flag explicitly, not slip in.
4. Reference tokens (`{colors.*}`, `{typography.*}`, `{spacing.*}`, `{motion.*}`) rather than inlining hex/px — this file and `globals.css` should never drift apart.
5. New semantic states need both an on-dark and an on-light hex verified at 4.5:1 before they ship — one value has never cleared both grounds in this system.
6. Motion additions should reuse the existing three durations and three easings (`{motion.fast/base/slow}` × `ease-out/ease-in-out/ease-spring`) and must respect `prefers-reduced-motion`.
7. When in doubt about emphasis: color (copper) or family-switch to Clash Grotesk, before reaching for a heavier weight.

## Known Gaps

- Clash Grotesk and General Sans are self-hosted `.woff2` files (`next/font/local`), not published web fonts — there's no public CDN substitute documented here; treat them as licensed brand assets, same as the logo.
- This file documents the **marketing surface**. The `/admin` post-editor (ProseMirror-based block editor, toolbar, slash-menu) shares tokens but adds many admin-only components (`.post-editor-*`, `.tb-*`, `.tippy-box` overrides) that are internal-tool surfaces, not marketing components — see `~/.claude/skills/obs-design-critique/references/impactors-academy.md` for the internal-tool-vs-marketing critique split.
- Full component inventory (hero variants, pricing cards, testimonial layout, footer structure) has not been extracted from rendered pages — this pass is built from `globals.css` tokens and utility classes, not a page-by-page audit. A `/site-studies`-style pass against the live site would round this out.
- Animation choreography beyond the documented durations/easings (specific hero entrance sequencing, marquee content, clip-path reveal triggers per section) lives in component code, not tokens.
- Sister properties (ia-pro, loc, prospectbuddy) share the core `--ia-*` color tokens per `~/.claude/skills/color-combinations/references/brands/impactors-academy.md`, including four venture-specific accent colors (Loc amber, Beyond the Football Pitch olive, IA Business & Finance burnt orange, IA Pro pale wheat) not detailed in this file — see that reference for the full venture-color system.
