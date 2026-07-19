# Site Study: Apple (apple.com)

**Date:** 2026-07-18  
**Viewport studied:** 1440×900 desktop, 390×844 mobile  
**URL:** https://www.apple.com/

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

**First thing the eye hits:** The nav bar (ultra-thin, 44px) is nearly invisible — then immediately below it, a full-bleed product tile grid fills the entire viewport. No hero "image" in the traditional sense; the products *are* the hero, each tile occupying a large slab of space.

**Nav pattern:** Fixed sticky. Position `fixed`, z-index `9999`, always present at the top.

**Frosted glass nav:** Background is `rgba(255,255,255,0.8)` with `backdrop-filter: saturate(1.8) blur(20px)` — the canonical Apple frosted-glass treatment, giving a sense of depth without a heavy visual footprint.

**Nav contents:** Apple logo left, product category text links center, search icon + bag icon right. Extremely minimal — no mega-menu visible at rest. Submenus appear on hover/click inline.

**Body-level class hints:** `ac-nav-overlap globalnav-scrim globalheader-light` — the hero content runs underneath the nav (overlap pattern), and a "scrim" class adjusts nav text color based on hero brightness.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png`

**3D element:** None. Zero canvas elements on the page. No Three.js, Babylon, Spline, or any WebGL runtime detected.

**Animation approach — video-based:** The hero section (`section.section-hero`, height 2100px) contains 4 embedded `<video>` elements served as WebM files from Apple's own CDN. Each product tile has its own looping animation video (e.g., `anim/hero/largetall.webm`, `anim/solo-1/largetall.webm`, `anim/solo-2/largetall.webm`). This is Apple's signature technique: pre-rendered, high-quality video clips that look like realtime 3D or motion graphics but are not.

**Tile structure:** Three `tile-wrapper` children per row. The first visible tile (Education/Back to School) uses an animated image of students; the iPhone tile plays a product-spin or reveal animation; the MacBook Air tile uses a similar video reveal. Product image `alt` attributes describe the visual precisely.

**Entrance animation:** Not detectable via static JS inspection (no GSAP/CSS animation classes visible). Apple's `inline-media.built.js` almost certainly triggers video playback at scroll thresholds — tiles appear pre-positioned, with videos autoplay on load or on scroll-into-view.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll type:** Native browser scroll — confirmed. No Lenis, Locomotive Scroll, GSAP ScrollTrigger, or any smoothing library found on `window`.

**Page dimensions:** Total scrollable height ~5103px at 1440px wide (6003px body height). Approximately 5.7 viewport heights of content.

**Hero occupies 2100px** — more than 2 full viewport heights. As you scroll, new product tiles enter the view progressively: Education → iPhone → MacBook Air (first 2100px), then iPad Air → MacBook Pro → Apple Watch → iPad Pro → Trade-In → Apple Card in the second grid section (~2100–3600px range).

**Layout changes through scroll:**
- Stage 1 (~1200px): Mid-hero, second product row revealed — tile grid continues full-bleed
- Stage 2 (~2400px): Second product section with a denser multi-tile grid (smaller tiles, 2- and 3-column mixed)
- Stage 3 (~3600px): "Endless entertainment" section begins — dark/rich background shift, tab-based gallery for Apple TV+, Apple Music, Arcade etc.
- Stage 4 (~4800px): Entertainment gallery continues with services tiles
- Stage 5 (~5103px/bottom): Footer — comprehensive link directory, legal footnotes, language/region selector

**Scroll-linked animation:** No `data-parallax` or `data-scroll` attributes found. Apple's proprietary `home.built.js` and `inline-media.built.js` handle any scroll-linked video triggering internally.

**No horizontal scroll hijacking, no pinned sections detected.**

---

## 4. Micro-Interactions

**Custom cursor:** None. Standard browser pointer cursor throughout.

**Nav link hover:** Color transitions at `color 0.32s cubic-bezier(0.4, 0, 0.6, 1)` — a gentle ease-in-out deceleration curve, barely perceptible but perfectly smooth. No scale, no underline, just color shift.

**Product tiles:** `.tile-link` and `.button` elements both use `transition: all` — Apple's shorthand that covers opacity, background-color, box-shadow, and potentially transform simultaneously on hover. The exact effect (subtle lift/shadow, or opacity) is in Apple's stylesheet rather than inspectable as computed values at rest.

**CTA buttons:** Pill-shaped (`border-radius: 980px`), 17px text, `padding: 11px 21px`. Primary variant: solid Apple blue (`rgb(0, 113, 227)`). Secondary variant: transparent background, same blue text. No scale or skew animation visible — hover likely swaps to a slightly darker blue (Apple's standard).

**No magnetic cursor-follow, no particle effects, no WebGL post-processing on hover.**

---

## 5. Typography & Color

**Typeface:** SF Pro Text exclusively — Apple's proprietary system font. Cascade: `"SF Pro Text", "SF Pro Icons", "Helvetica Neue", Helvetica, Arial, sans-serif`. Not a web font (no Google Fonts, Adobe Fonts, or `@font-face` for SF Pro) — it's served as a system font where available, else falls to Helvetica Neue.

**Type scale:**
| Role | Size | Weight | Letter-spacing |
|------|------|--------|----------------|
| Tile headline (h2) | 56px | 600 (SemiBold) | −0.28px (tight) |
| Body / button | 17px | 400 | default |
| Nav items | ~12–14px | 400 | default |

**Core palette:**
| Token | Value | Approx hex |
|-------|-------|------------|
| Page background | `rgb(255, 255, 255)` | `#FFFFFF` |
| Tile background | `rgb(245, 245, 247)` | `#F5F5F7` — Apple's signature off-white |
| Primary text | `rgb(29, 29, 31)` | `#1D1D1F` — Apple's near-black |
| Nav text | `rgba(0, 0, 0, 0.8)` | ~`#000000CC` |
| Primary button | `rgb(0, 113, 227)` | `#0071E3` — Apple blue |
| Secondary/link | `rgb(0, 102, 204)` | `#0066CC` |

**No decorative accent colors, no gradients in the product tile grid.** Each tile's color scheme comes from the product photography/video itself — Apple relies entirely on the product as the visual element.

---

## 6. Tech Fingerprint

**Confirmed absent (window-level check):**
- Three.js / react-three-fiber — ✗
- GSAP / ScrollTrigger — ✗
- Lenis / Locomotive Scroll — ✗
- React / Next.js (`__NEXT_DATA__`) — ✗
- Framer Motion — ✗
- Canvas elements — ✗ (0 found)

**Confirmed present:**
| Script | Confidence | Notes |
|--------|-----------|-------|
| `globalheader.umd.js` | Confirmed | Apple's custom UMD nav component |
| `inline-media.built.js` | Confirmed | Handles in-viewport video autoplay |
| `endless-entertainment-gallery.built.js` | Confirmed | Tab-based services carousel |
| `home.built.js` | Confirmed | Page-level orchestration |
| `ac-analytics.js` + `data-relay.js` + `auto-relay.js` | Confirmed | Apple's analytics stack |
| `localeswitcher.built.js` | Confirmed | Country/region modal |

**Inferred architecture:** Apple's own internal component system — bundled as `.built.js` UMD modules. No React, no framework. Likely vanilla JS or a proprietary rendering layer. The `umd.js` naming convention suggests independent, self-contained web components.

**Video CDN pattern:** `https://www.apple.com/105/media/us/home/[hash]/anim/[section]/largetall.webm` — versioned, region-scoped, responsive-suffix (`largetall` for desktop, presumably `small`/`medium` for mobile).

---

## 7. Mobile Pass

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**Viewport tested:** 390×844 (iPhone-equivalent)

**Nav on mobile:** Grows slightly from 44px to 48px. The product category links disappear from the top bar entirely — only Apple logo + search + bag remain. Navigation moves behind a menu trigger (Apple's globalnav system expands inline on mobile rather than using a traditional hamburger drawer — the menu opens below the nav bar in a full-screen overlay).

**Tile layout:** All tiles collapse to single-column full-width stacks. Each tile measures 375×500px — exactly viewport width × fixed tall aspect. The 2- and 3-column desktop grids become a linear scroll down the page.

**What's simplified:**
- Product category nav links removed from visible bar
- Multi-column tile grids flatten to single column
- Video sources likely switch to smaller format (`small.webm`) — Apple uses responsive `<source>` tags keyed to viewport breakpoints
- Entertainment gallery tabs still present but scaled to touch targets

**What persists on mobile:** Frosted glass nav, same color palette, same SF Pro Text typeface, same pill-button shape, same tile-bg `#F5F5F7`. The design system is fully consistent — layout changes, aesthetics don't.

---

## Summary — Technique Patterns Worth Noting

1. **Video-as-animation over WebGL:** Apple gets cinematic quality from pre-rendered WebM clips rather than realtime 3D. Zero runtime overhead, perfect visual fidelity across all devices.
2. **Frosted glass nav:** `backdrop-filter: saturate(1.8) blur(20px)` on a white-translucent background — the definitive Apple nav signature.
3. **`#F5F5F7` tile backgrounds:** Apple's off-white creates the sense of "cards floating on white" without any shadow or border. The 10-unit gap between white page and near-white tile is enough.
4. **Tight type tracking at large sizes:** 56px headings at −0.28px letter-spacing — barely negative, but at display scale it reads as confidently compact.
5. **Pill CTAs at body size:** 17px pill buttons with `border-radius: 980px` — the radius value is intentionally exaggerated (larger than the element) to guarantee a perfect pill regardless of content length.
6. **No third-party animation libs:** Every motion behavior is encapsulated in Apple's own `.built.js` bundles. Native scroll + proprietary video-trigger system replaces GSAP/Lenis entirely.
7. **System font dependency:** SF Pro Text is only available on Apple devices — non-Apple visitors get Helvetica Neue. Apple accepts this inconsistency as a brand statement.
