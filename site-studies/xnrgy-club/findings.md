# Site Study: XNRGY Club
**URL:** https://xnrgyclub.com/  
**Study date:** 2026-07-18  
**Slug:** xnrgy-club  

---

## 1. Navigation & First Impression

**→ Screenshot:** `screenshots/01-hero-desktop.png`

The first thing the eye lands on is the massive H1 headline — displayed at ~187px with extreme negative letter-spacing (−10px) and light weight (300) in NeueHelvetica Pro. It dominates the viewport against a dark (near-black) hero background, creating immediate typographic impact before any imagery registers.

**Nav pattern:** Full horizontal bar fixed over the hero. Logo anchored left, primary nav links centered, two CTA buttons ("Book padel lessons" / "Book a court") right-aligned. Nav text renders in off-white (#EBEBEB) against the dark hero. On scroll, the nav transitions (likely to dark-on-light) as the hero gives way to the off-white body background. No hamburger at desktop.

---

## 2. Hero Section

**→ Screenshot:** `screenshots/01-hero-desktop.png`

The hero is a full-viewport dark section with the oversized H1 as its anchor. There is no 3D element: no `<canvas>` exists on the page, `window.THREE` is absent, and no WebGL engine scripts are loaded.

**Entrance animation:** Each word (and potentially each character) of the H1 is individually wrapped in its own `<span>`-equivalent element in the DOM, strongly indicating a character- or word-by-word stagger reveal on load — a classic split-text entrance. The small label above the H2 ("Introduction") follows the same per-character wrapping pattern, suggesting a consistent text-reveal system across all animated headings.

Below the hero, the page transitions to an off-white (#EBEBEB) background. The first content section pairs a large H2 with a small monospaced label in Space Mono — establishing a typographic rhythm that repeats throughout.

---

## 3. Scroll Behavior

**→ Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll type:** Lenis smooth scroll — confirmed via `document.documentElement.classList` containing `"lenis"` and `"hydrated"`. Native scroll events are intercepted and eased.

No Locomotive Scroll, no GSAP ScrollTrigger detected on the `window` object. Custom animation logic is bundled into the theme's own `app.js`.

**Page structure (5 scroll stages):**
- **Stage 1 (~1400px):** Intro section — H2 + body copy split into two columns, with a large editorial image. Section uses generous whitespace and asymmetric grid.
- **Stage 2 (~2800px):** "Evolving Energy" section — another H2 + body copy pairing, with a prominent full-bleed or large image. A numbered list of club locations begins.
- **Stage 3 (~4200px):** Club listing section — two cards labeled "01–02 / 02–02" for Almere and Amsterdam, presented in a horizontal split. A "[Keep scrolling]" label nudges users forward.
- **Stage 4 (~5600px):** Gym section — mirrors the intro section's two-column layout. Same letter-stagger on the heading "Where movement and progression meet."
- **Stage 5 (~6800px, bottom):** "Measure Motion" manifesto section + footer. Footer uses a multi-column grid: brand/contact left, nav links center, social + CTA right.

No horizontal scroll hijacking observed. No pinned sections detected. Scroll-linked parallax is likely present on images (the generous section heights suggest images move at a different rate than text) but not confirmed via ScrollTrigger.

---

## 4. Micro-Interactions

**Custom cursor:** A `.cursor-follower` element exists — `position: fixed`, ~85px wide × ~26px tall. Its non-circular dimensions suggest it's a text label cursor (e.g. "View →" or similar) rather than a dot or ring. It tracks the pointer and likely swaps its label text on hover over different interactive elements.

**Button hover states (from CSS rules):**
- `.btn--outline`: A `::before` pseudo-element fades out on hover while `::after` scales in from the right (`right: 0; scale: 1`) — a solid fill-wipe that covers the button background. Color shifts to off-white on the filled state.
- `.btn--nav` (arrow/link buttons): `padding-left` increases by 0.625rem on hover (a subtle indent nudge) while the SVG icon rotates 45° (northeast arrow effect).
- `.btn--primary`: Same fill-wipe mechanism as `--outline` via a scaling `::after` pseudo-element.

No magnetic cursor-follow on link elements detected in CSS. The cursor-follower movement logic lives in JavaScript.

**Nav link hover:** No underline or color shift visible in the site's own stylesheet — transitions appear minimal on nav items.

---

## 5. Typography & Color

### Type scale
| Level | Font | Size (desktop) | Size (mobile) | Weight | Notes |
|---|---|---|---|---|---|
| H1 | NeueHelvetica Pro | 187px | 95px | 300 (Light) | Letter-spacing −10px |
| H2 | NeueHelvetica Pro | 75px | 38px | 400 (Regular) | Normal letter-spacing |
| Labels | Space Mono | 10.5px | — | 400 | Monospace, all-caps feel |
| Body | Space Mono | 10.5px | — | 400 | Monospace body copy |

The combination of oversized Light Helvetica headings with tiny monospaced body text is intentional contrast — editorial scale versus technical precision.

### Palette
| Role | Value | Notes |
|---|---|---|
| Background | `rgb(235, 235, 235)` / `#EBEBEB` | Warm off-white, dominant across all light sections |
| Text | `rgb(0, 0, 0)` / `#000000` | Pure black |
| Hero background | Dark / near-black | Contrasts nav off-white links |
| Primary accent | `rgb(25, 43, 136)` / `#192B88` | Deep navy-indigo; used for primary CTAs and form radio hover states |
| Secondary | `rgb(15, 19, 32)` / `#0F1320` | Near-black dark navy; used as an alternative CTA color |

No bright accent color. The palette is extremely restrained: off-white, black, and one deep blue. No gradients, no color noise.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| WordPress | **Confirmed** | Body class: `wp-theme-xnergy`, `/app/themes/`, `/app/plugins/` URL paths |
| WP Rocket | **Confirmed** | Script tag for WP Rocket lazyload JS |
| Lenis smooth scroll | **Confirmed** | `<html class="lenis hydrated">` |
| Custom theme build | **Confirmed** | `manifest.js`, `vendor.js`, `app.js` from `dist/js/` |
| Gravity Forms | **Confirmed** | Extensive `.gform_*` CSS rules |
| Google Tag Manager | **Confirmed** | Script tag for GTM container |
| Google Analytics (GA4) | **Confirmed** | `gtag.js` with GA4 ID |
| Zapier Interfaces | **Confirmed** | `zapier-interfaces.esm.js` web component (likely powers the chat widget) |
| Three.js / WebGL | **Not found** | No canvas, no THREE on window |
| GSAP | **Not found** | Not on window; not in script src tags |
| Framer Motion | **Not found** | — |
| React / Next.js | **Not found** | — |
| Locomotive Scroll | **Not found** | — |
| Tailwind CSS | **Not found** | No `tw-` or utility class patterns visible |

**Built by:** Every Day (Dutch digital agency — credited in footer).  
**Animation approach:** Custom vanilla JS bundled into `app.js`, with Lenis for scroll smoothing. Text animations are almost certainly handled via a custom split-text implementation (not GSAP SplitText), given the individual DOM wrapping of characters observed in the snapshot.

---

## 7. Mobile Pass

**→ Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`  
**Viewport tested:** 390×844 (iPhone 14 Pro)

**Nav:** Full horizontal nav collapses to a hamburger (`<button class="btn-toggle-offcanvas" aria-label="Open offcanvas menu">`). Slides in as an offcanvas overlay.

**Typography scaling:** H1 drops from 187px → 95px (roughly halved). H2 drops from 75px → 38px (halved). Proportions and font choices remain identical — only size adjusts.

**Layout:** Two-column sections collapse to single-column stacking. Large editorial images remain present but reflow below their text blocks. Page height stays comparable (~7400px mobile vs. ~7188px desktop), suggesting limited content removal — mobile gets the same sections, just reflowed.

**What's simplified:** The horizontal split layouts compress to vertical stacks. The custom cursor follower likely deactivates on touch devices (no pointer hardware). The "Keep scrolling" label persists.

**What's removed:** Side-by-side editorial grids collapse; no horizontal scroll or multi-column typography on mobile.
