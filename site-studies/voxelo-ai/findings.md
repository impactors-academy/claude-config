# Site Study: Voxelo.ai
**URL:** https://www.voxelo.ai/  
**Date:** 2026-07-18  
**Viewport (desktop):** 1440×900 | **Viewport (mobile):** 390×844

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

The first impression is total immersion: the entire viewport is a rendering of a single 3D product (a sneaker) floating on a near-black background, with a dramatic orange fire-ring glow cast beneath it. The eye goes directly to the 3D model, which occupies roughly 60% of the viewport on the right side. The H1 on the left registers second, then the orange CTA button.

**Nav pattern:** Sticky top nav that remains fixed during the WebGL scroll experience. It's nearly invisible at load — the glassmorphism background (`rgba(14,14,11,0.55)`) blends into the dark scene — but the orange "TRY FOR FREE →" pill reads as the only strongly-colored element in the nav. Center links (Product ▾, Solution ▾, Gallery, Pricing) are white at low opacity; ghost-border "LOGIN" and "BOOK DEMO" buttons are on the right. The nav never hides on scroll.

Above the nav: a thin announcement bar with a horizontal marquee ticker (CSS-animated duplication pattern via `.announce-item--dup`) containing a product benefit statement and a linked CTA.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png`

**3D element:** Yes — a full-viewport WebGL 2.0 canvas (`1440×900`) renders the entire hero experience. The canvas is not a `<canvas>` overlay but is part of the page flow, driven by a proprietary in-house framework called **"Peach"** (identified via class names `peach-scroll-doc`, `peach-track-section`, `peach-pinned`, etc., and a custom preloader animation named `peachPreloaderTickWave`).

- `window.THREE` is not exposed, so the 3D engine is either bundled without a global or is a custom WebGL renderer — not a standard Three.js or Babylon.js drop-in
- No Spline iframes or runtime scripts detected
- The canvas uses WebGL 2.0 (`OpenGL ES 3.0 Chromium`)

**3D content:** A photorealistic product model (sneaker) with subsurface scattering-quality material, a volumetric emission ring (fire/glow) beneath it, and a floating "voxelo.ai" holographic brand badge attached to the product. The model is the hero — there's no background image or video.

**Entrance animation:** A custom preloader fires first — staggered horizontal white tick-bars animate in a wave pattern (`peachPreloaderTickWave`, 1.8s ease-in-out, ~8 staggered bars at 0.08s offsets). The scene reveals after the loader exits via `opacity: 0 → 1` transition (350ms ease-out).

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll type:** Smoothed — Lenis confirmed via `window.Lenis` global and `.lenis` class on `<body>`. Native momentum is replaced with Lenis easing.

**Scroll architecture (the "Peach" system):** The most distinctive technical pattern on the site. The WebGL canvas stays pinned/fixed while scroll-linked sections drive camera and scene changes:

- **`peach-track-section`** — 4 sections, each exactly 1080px tall, that act as scroll "tracks." As the user scrolls through each track, the Peach system updates the WebGL scene (camera angle, model state, overlaid UI) without the canvas itself moving
- **`peach-transition-section`** — 270px transition zones between tracks that blend between scene states
- **`peach-pinned peach-overlay-slot`** — the text/UI layer that sits above the canvas and updates per-scene
- **`peach-2d-section`** — the final section that exits the WebGL experience entirely and reverts to a standard dark background

**What changes per scroll stage:**

| Stage | Y offset | Scene state |
|---|---|---|
| 01 (`03-scroll-stage-1.png`) | ~1300px | Camera moves closer; H2 headline swaps; a smartphone prop floats in from left alongside the sneaker — showing the "capture" step; a floating metrics annotation card appears anchored in 3D space |
| 02 (`03-scroll-stage-2.png`) | ~2400px | Heading text mid-transition shows a **letter-scramble/decode animation** — characters appear as corrupted glyphs before resolving; a horizontal filmstrip of product thumbnail images fades in at the bottom of the viewport |
| 03 (`03-scroll-stage-3.png`) | ~3600px | Third headline resolves; the filmstrip is fully visible and appears to be a horizontal auto-scroll of output variants |
| 04 (`03-scroll-stage-4.png`) | ~4800px | Scene exits WebGL; switches to a **warm cream / light background section** showing static product renders in 3 orientations (studio, dark, room-context), followed by a stat-counter row (+24%, 76%, 2hrs, 40%) in a large monospace typeset |
| 05 (`03-scroll-stage-5.png`) | ~5574px | Dark background resumes; full-width testimonial cards with large quote body text; final CTA section before minimal footer |

**Scroll-linked effects:** No horizontal scroll hijacking. No GSAP ScrollTrigger detected. The scroll-to-3D-camera-movement effect is entirely custom (Peach framework).

---

## 4. Micro-Interactions

**Cursor:** No custom cursor detected — standard OS cursor throughout.

**Buttons:** CTAs use gradient backgrounds (see Section 5) with white text. Hover states were not capturable via static screenshot, but button class naming (`btn-accent`, `btn-ghost`, `btn-ghost-dark`) suggests state variants are CSS-driven.

**Nav dropdowns:** The "Product ▾" and "Solution ▾" nav triggers open **mega-panel** dropdowns with a cream `rgb(245,241,232)` background — a sharp contrast against the dark site. Panels contain `mega-card` link items (white `rgb(255,255,255)` background). The backdrop uses `rgba(10,10,8,0.35)` scrim. Mobile nav opens a `mnav-panel` drawer with the same cream palette.

**Announcement bar:** CSS `animation: marquee` pattern via duplicated items — text loops continuously without JavaScript.

**Floating annotation card:** In scroll stages 1–3, a glassmorphic info-card is anchored near the 3D model in the WebGL scene, displaying live stats (model count, format support) — appears to be a 2D DOM overlay positioned to look spatially attached to the model.

---

## 5. Typography & Color

### Type scale

| Level | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H1 | Bricolage Grotesque | 108px | 500 | Hero only; line breaks mid-phrase ("Build Buyer / Confidence Fast.") |
| H2/scene headings | Bricolage Grotesque | ~56–72px | 500 | Inferred from scroll stages; updates per WebGL scene |
| H3 / section labels | Bricolage Grotesque | 22px | 500–600 | Nav mega-menu labels, section identifiers |
| Body | Bricolage Grotesque | 15px | 400 | Primary paragraph text, 1.7 line-height |
| Detail/mono labels | DM Mono | 10–13px | 400 | Attribution lines, stat labels, small metadata — monospace |
| Secondary body | Montserrat | 13px | 400 | Supporting descriptive text |

Single font family drives the bulk of the UI (Bricolage Grotesque, a variable grotesque). DM Mono provides a sharp editorial contrast for small technical labels. Montserrat appears in select body contexts.

### Palette

| Role | Value | Notes |
|---|---|---|
| Background (primary) | `#0a0c10` / `rgb(10,12,16)` | Near-black, slight cool-blue tint |
| Background (announce bar) | `#0a0a08` / `rgb(10,10,8)` | Near-black, very slight warm tint |
| Text primary | `rgba(255,255,255,0.9)` | Near-white with 10% transparency |
| Text secondary | `#f4f4ec` / `rgb(244,244,236)` | Warm near-white for ghost buttons |
| Nav glass | `rgba(14,14,11,0.55)` | Semi-transparent warm-dark glassmorphism |
| Mega-panel / mobile nav | `#f5f1e8` / `rgb(245,241,232)` | Warm cream — stark contrast for dropdowns |
| Accent CTA (standard) | `linear-gradient(135deg, #fb5e01 → #ea4a05)` | Orange gradient |
| Accent CTA (scene hero) | `linear-gradient(343deg, #f00d33 → #fb5e01 → #f4b71d)` | Red → orange → yellow tri-color "fire" gradient |
| Light section bg | ~`#f8f4ed` (warm cream) | Used in the 2D stats/gallery section (stage 4) |

**Palette character:** Extreme contrast — deep near-black versus warm near-white, with a single fire-palette accent applied only to CTAs. No mid-tones, no secondary accent colors. The mega-panel cream creates a deliberate light/dark contrast moment in the nav.

---

## 6. Tech Fingerprint

| Technology | Confidence | Evidence |
|---|---|---|
| **Next.js** (App Router) | Confirmed | `/_next/static/chunks/` script paths; `turbopack-*` chunk name; `#__NEXT_DATA__` element present |
| **Custom "Peach" WebGL framework** | Confirmed | Class names `peach-scroll-doc`, `peach-track-section`, `peach-transition-section`, `peach-pinned`, `peach-2d-section`, `peach-overlay-slot`; animation `peachPreloaderTickWave`; no matching public library |
| **WebGL 2.0** | Confirmed | `canvas.getContext('webgl2')` returns active context; reported as `OpenGL ES 3.0 Chromium` |
| **Lenis** (smooth scroll) | Confirmed | `window.Lenis` defined; `.lenis` class on `<body>` |
| **PostHog** | Confirmed | `eu-assets.i.posthog.com/static/array.js` loaded |
| **Google Tag Manager + GA4** | Confirmed | GTM and `gtag.js` scripts loaded |
| **HubSpot** | Confirmed | `js-eu1.hs-scripts.com` loaded |
| **GSAP / ScrollTrigger** | Not detected | `window.gsap` is null; `window.ScrollTrigger` is false |
| **Three.js** | Not detected (may be bundled) | `window.THREE` null; canvas is WebGL but engine not exposed |
| **Framer Motion** | Not detected | `window.MotionGlobalConfig` undefined |
| **Locomotive Scroll** | Not detected | `window.LocomotiveScroll` undefined |
| **Tailwind CSS** | Not detected | No `flex`, `px-`, `text-` etc. class patterns; uses custom BEM-adjacent naming (`vx-*`, `btn-*`, `nav-*`, `peach-*`) |

---

## 7. Mobile Pass

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**What changes on mobile:**

- H1 scales from 108px → 33px — dramatic compression but still large relative to mobile viewport
- Nav links (`.nav-links`) hidden (`display: none`); hamburger burger icon takes over; opens the `mnav-panel` drawer
- The WebGL canvas resizes to 390×844 — the 3D model is preserved and renders full-width, not swapped for a static image. The product fill and fire-ring glow scale down but remain visible
- The announcement bar persists at the top as a scrolling ticker
- Below the hero, a "POWERED BY UG3D®" block appears earlier in the mobile flow (it was below the fold on desktop)
- Scene CTAs become "Start creating →" in the full fire-gradient
- Page height expands (6987px mobile vs 6474px desktop) — content reflows vertically rather than compressing
- The floating annotation card and product filmstrip persist on mobile but are stacked rather than side-by-side
- Stats row (+24%, 76%, 2hrs, 40%) appears to display in a 2-column grid at mobile width

**Simplifications/removals for mobile:** Nav mega-menus replaced entirely by the drawer pattern; no desktop-specific hover states; testimonial cards stack full-width.
