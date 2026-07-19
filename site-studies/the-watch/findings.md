# Site Study: The Watch by 60fps
**URL:** https://thewatch.60fps.fr/
**Slug:** the-watch
**Date:** 2026-07-18
**Viewport studied:** 1440×900 desktop, 390×844 mobile

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

No traditional navigation exists. The page has a `<header>` element with a computed height of `0px` — it's invisible infrastructure. Instead, floating HUD-style labels (`SWAP`, `HOLD TO EXPLORE`, `SELECT MODEL`) are overlaid directly on the WebGL canvas as absolutely-positioned UI affordances. There is no hamburger, no sticky bar, no link list.

The very first thing the eye goes to is the collision of two things at once: a monumental display logotype spanning the full viewport width, and a photorealistic 3D watch model floating inside the letterforms, occupying the negative space of the "6". The two elements feel designed together — not text beside a product shot, but one unified graphic.

Nav pattern: none. The only "navigation" is scroll — the entire page is a single vertical tunnel.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png`

The hero is a full-viewport WebGL2 canvas behind all text. The background renders as a radial silver/grey gradient — warm metallic, not flat white.

A 3D watch model sits at center, with a faint radial guide circle behind it (like a clock-face or compass rose, very light, structural). The model is fully lit and PBR-rendered (reflections visible on bracelet links and case).

The display logotype ("FS 60P") is split across the watch: "FS" left, "60P" right, with the watch physically occupying the gap. At the bottom-left, "MODEL / 146GR" appears in a compact two-line label with a color selector ("Silver Steel") inline.

**3D engine confirmed:** Three.js r162 (`window.__THREE__ === "162"`). A single WebGL2 canvas covers the full viewport (1425×900). The bundle is a single Vite-compiled JS file (`/assets/index-Ck-pEZ8v.js`) — no CDN script, no Spline embed, no iframe. The Three.js scene is custom-built.

Entrance animation: Not capturable via static scroll, but the HOLD TO EXPLORE label and the 34,625px page height suggest the initial state is a posed model and the scroll itself is the entrance mechanic — you pull the scene into motion.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll type: native.** No Lenis, no Locomotive Scroll, no GSAP ScrollTrigger detected in the window object. The page uses raw `scrollY` to drive the Three.js `requestAnimationFrame` loop — a direct, dependency-light approach.

Page height: **34,625px** on desktop. This is the scroll budget. The 3D scene's timeline is mapped to this distance.

**Stage 1 (~2000px):** `screenshots/03-scroll-stage-1.png`
The watch transitions from hero pose to a close-up, slightly elevated floating view on a lighter grey field. Two feature columns appear at right, with tiny caps labels above each block of body copy. The watch occupies roughly the left 60% of the viewport. No UI chrome — just product and text.

**Stage 2 (~7000px):** `screenshots/03-scroll-stage-2.png`
The most technically ambitious section: an **exploded 3D diagram** of the watch movement. Components (Dial, Tourbillon, Mainplate, Barrel, Backplate, Weight) split apart horizontally in 3D space, labeled below in small caps. A "Click to explore" affordance appears top-center — this section has a click/interaction layer on top of the scroll progression. The explosion depth gives a sense of the watch being disassembled in real time as you scroll.

**Stage 3 (~14000px):** `screenshots/03-scroll-stage-3.png`
A single-word hero moment: "ELEGANT" in large ghosted/transparent text, with the assembled watch re-emerging below it on a slightly warmer grey. The text functions as a watermark behind the product, not a heading above it.

**Stage 4 (~22000px):** `screenshots/03-scroll-stage-4.png`
Model selector section. Multiple 3D crown/pusher components (the knob on the watch side) appear spread across the viewport at different scales and angles — each representing a different model variant ("SLIM", "B PRO" visible overlapping as ghost text). It reads like a showroom shelf rendered in WebGL.

**Stage 5 (~30000px):** `screenshots/03-scroll-stage-5.png`
A darker grey background (~#3a3a3a) takes over. The variant name — "SILVER STEEL" — fills most of the viewport in enormous, light-coloured letterforms. The watch sits centered and small by comparison, anchoring the text. This pattern (large text + small watch) is the inverse of the hero and creates a strong beat at the end of the scroll.

**Scroll-linked patterns used:**
- Camera orbit / position interpolation (Three.js scene moves through the product)
- Component spread/explode triggered by scroll depth
- Background tone shifts (light silver → dark grey)
- Text watermarking layered behind 3D objects

---

## 4. Micro-Interactions

**Custom cursor:** Present on desktop, hidden on mobile/tablet via `.hide-mobile.hide-tablet` class. It's a 40×40px fixed-position `<div>`, no border-radius (not a circle — likely rendered as a crosshair or minimal indicator). z-index: 4. Mix-blend-mode is `normal` (no difference/exclusion blend). The cursor element itself is transparent — its visual appearance is driven by CSS class changes on hover states, not inline styles captured at rest.

**HUD affordances:** `SWAP`, `HOLD TO EXPLORE`, `SELECT MODEL` are not standard buttons. "HOLD TO EXPLORE" implies a pointer-hold gesture triggers a 3D rotation mode (free orbit of the watch model). "SWAP" implies a tap/click cycles between color variants. These are interaction verbs, not labels.

**Buttons:** Two `<button>` elements in the nav area (prev/next for color variants). Both have transparent backgrounds and black text — no border, no shadow. Transition behavior not captured without live hover testing, but the overall design language suggests scale or opacity shifts rather than color fills.

---

## 5. Typography & Color

### Type Scale

| Role | Font | Size |
|------|------|------|
| Display / H1 | Nekst (custom/licensed) | 350px |
| Section heading | H3, likely Nekst | 60px |
| Body copy | Inter | ~9px |
| Secondary labels | Times New Roman | varies (small) |

The H1 at 350px is not hyperbole — it is literally viewport-spanning. The "FS 60P" fills the full 1440px width. At 9px, body copy is more of a texture than readable text at a normal reading distance; it rewards zooming in, reinforcing the luxury/editorial register.

Times New Roman appears for some secondary labels — a deliberate serif-meets-grotesque contrast, playing an archival/horological role (watch brands use historical typefaces as credibility signals).

### Color Palette

| Role | Value (approx) |
|------|----------------|
| Background (hero/light sections) | Radial gradient, ~#c8c8c8 → #e8e8e8 (silver-grey) |
| Background (dark section) | ~#3a3a3a (charcoal) |
| Primary text (light bg) | #000000 |
| Primary text (dark bg) | #ffffff |
| 3D model palette | Chromium silver, black dial, gold movement accents |

No accent colour. The entire palette is monochromatic and metallic — black, white, and greys. The only colour is in the 3D model's gold/brass movement components, which serve as the sole warm contrast element.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| Three.js r162 | **Confirmed** | `window.__THREE__ === "162"` |
| WebGL2 | **Confirmed** | Canvas context type |
| Vite (build tool) | **Confirmed** | Single bundle `/assets/index-Ck-pEZ8v.js` hash pattern |
| Custom scroll-to-Three.js bridge | **Confirmed (inferred)** | 34,625px page height, native scroll, no scroll library |
| Inter (typeface) | **Confirmed** | `getComputedStyle` on `<p>` |
| Nekst (typeface) | **Confirmed** | `getComputedStyle` on `<h1>` |
| Times New Roman (typeface) | **Confirmed** | `getComputedStyle` on `<body>` |
| React / Next.js | Not present | No `__NEXT_DATA__`, no React devtools hook |
| GSAP / ScrollTrigger | Not present | Not found in window |
| Lenis / Locomotive Scroll | Not present | Not found in window |
| Spline | Not present | No `<spline-viewer>`, no Spline runtime |
| Framer Motion | Not present | Not found in window |
| Custom cursor system | **Confirmed** | Fixed DIV with `.hide-mobile.hide-tablet` |

**Architecture summary:** Single-page vanilla JS application, Vite-compiled, with a custom Three.js scene as the primary UI surface. No framework, no animation library beyond Three.js itself. Extremely lean dependency footprint for what is a technically complex experience.

---

## 7. Mobile Pass

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**Hero (390×844):** `screenshots/07-mobile-hero.png`
The massive logotype is still present but the letters bleed off-screen left and right — only "FS" and "0P" are visible at the edges, with the "6" hidden behind/around the watch. The watch takes center stage even more aggressively on mobile because the text frame becomes purely atmospheric. The radial guide circle, the "Color: Silver Steel" label, and "MODEL / 146GR" all remain visible at the bottom. The layout holds.

**Scroll section (5000px depth):** `screenshots/07-mobile-section.png`
The exploded 3D view persists — components are still rendered in WebGL and spread in space. However, the component labels (Dial, Tourbillon, etc.) appear absent or not visible, simplifying the information layer. The "FS 60P" logotype letters overlap the 3D components in this frame, suggesting the text and 3D z-layers collapse into each other more aggressively on mobile.

**What's removed/simplified on mobile:**
- Custom cursor (hidden via `.hide-mobile.hide-tablet`)
- Component labels in exploded view (appear hidden)
- The logotype becomes a framing device rather than a readable title (letters bleed out)
- No layout switch — there is no "mobile version", just the same 3D scene with the camera/typography adapting to the narrower frame

The 3D experience is not degraded to a video or static fallback on mobile — the full WebGL scene renders. This is a notable commitment to consistency across breakpoints.
