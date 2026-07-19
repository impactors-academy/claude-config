# Site Study: agencefoudre.com

**URL:** https://www.agencefoudre.com/  
**Studied:** 2026-07-18  
**Type:** French social media agency (Agence Foudre)  
**Viewport (desktop):** 1440×900 | **Viewport (mobile):** 390×844

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

First impression is playful and immediate: a giant dark-green display wordmark fills the top of the viewport from edge to edge, partially cropped at left and right. Beneath it is a loose photo collage — rounded-corner cards of people and workplace scenes, with emoji sticker overlays (lightning bolts, stars) scattered on the photos.

**Nav pattern — two floating corner buttons, no traditional bar.** A small circular pink button (hamburger icon) sits top-left; a WhatsApp circle button sits top-right. No horizontal nav bar at all. This is the full navigation chrome. Clicking the hamburger reveals a full-screen split overlay in forest green, with Beni 80px links on the right and supplementary info on the left.

The bottom-left of the hero carries a secondary tagline headline in the display font at large scale, while the bottom-right has a small floating "case study" card showing a client project — a persistent widget that reappears throughout the scroll.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png`

The hero composition:
- Top band: display wordmark in dark green at viewport-filling scale, cropped at both sides
- Center: a collage of 3 rounded-corner photo cards arranged loosely — not a grid, a scattered layout with slight rotation and overlap
- Emoji/icon stickers overlaid directly on the photos as decorative elements (lightning bolt, star shapes, platform icons)
- Bottom-left: secondary display headline in Beni Black, magenta/hot pink color
- Bottom-right: floating "case du mois" client card in a rounded card format

**3D elements:** None. No canvas elements used for 3D — the 3 canvas elements on the page are all 80×48px, consistent with toggle switch UI components. No Three.js, Spline, or WebGL detected.

**Entrance animation:** The body class `-hideLogo -once` and the hero class `-active -once` indicate an entrance sequence that fires once on load and marks itself complete. The Lenis 1.1.9 smooth scroll is active from the start. Transitions throughout use `clip-path` reveals (a content wipe/mask approach) and `opacity` + `transform` fades at 0.4s–0.8s with expo-out and spring easings.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll driver:** Lenis 1.1.9, confirmed via `window.lenisVersion` and `class="lenis"` on `<html>`. Smooth inertia scrolling throughout.

**Page length:** 25,062px desktop. The page cycles through distinct color worlds as you scroll — each major section has its own background.

**Data-scroll attributes** on multiple `<div>` elements serve as Lenis/IntersectionObserver hooks for scroll-triggered transitions.

**Stage 1 (~4500px) — `03-scroll-stage-1.png`:** Background shifts from cream to a warm dark olive/khaki. Client projects displayed as a full-viewport horizontal card carousel — each card is a large rounded-corner panel showing a project photo with a bold name overlay. Cards are arranged side by side, partially overlapping the next card to imply there are more. Left side carries a display headline.

**Stage 2 (~9500px) — `03-scroll-stage-2.png`:** Background shifts to a cool lavender/periwinkle. Two massive organic pink blob shapes appear on the left and right viewport edges — decorative SVG elements with rounded, amoeba-like silhouettes that frame the center content. Center text (Beni, hot pink, large) is mid-animation — appears caught in a clip-path reveal scroll-linked to progress. This is a manifesto/positioning section.

**Stage 3 (~14500px) — `03-scroll-stage-3.png`:** Lavender background continues. A services/expertise layout: left copy block + center editorial photo + right services list (text only). Below, three rounded-corner category cards in hot pink act as tap targets for the three service areas. The persistent "Case du mois" client widget reappears bottom-right.

**Stage 4 (~19500px) — `03-scroll-stage-4.png`:** Background explodes to full hot pink/magenta. Beni Black in light cream/blush at absolute maximum scale — a three-word question fills the entire viewport. The letterforms are enormous; the text extends to viewport edges. This is the "why choose us" section rendered as a pure typographic impact moment.

**Stage 5 (~24162px) — `03-scroll-stage-5.png`:** Soft pink background. Two overlapping cards in the center: a team photo card (white background, rounded corners, slightly rotated) and a contact/CTA card (hot pink background with Beni headline and a quiz CTA). At the very bottom, the wordmark in dark green reappears as a decorative footer treatment.

**Scroll-linked effects observed:**
- Background color transitions between sections (cream → olive → lavender → hot pink → soft pink)
- Text revealed via `clip-path` animation as sections enter the viewport
- The "Case du mois" floating card persists across sections
- No pinned scroll sections; native Lenis-smoothed vertical scroll throughout

---

## 4. Micro-interactions

**Spring-bounce hover:** The primary easing on interactive elements is `transform 0.4s cubic-bezier(0.17, 0.67, 0.3, 1.33)`. The control point at `1.33` exceeds the 0–1 range, creating an overshoot/spring-back effect — hovering a button causes it to scale past its target and settle back. Gives interactions a bouncy, energetic quality matching the brand personality.

**Clip-path reveals:** `clip-path 0.4s cubic-bezier(0.23, 1, 0.32, 1)` — text and content blocks animate in via a clipping mask that expands to reveal content. A wipe/curtain technique that feels modern without being overly flashy.

**Slow opacity/transform fades:** `opacity 0.8s cubic-bezier(0.86, 0, 0.07, 1)` and `transform 0.8s cubic-bezier(0.86, 0, 0.07, 1)` — heavier elements use a slower, more symmetrical in-out ease (cubic-bezier approximating ease-in-out-expo). Feels weighty and deliberate for large content blocks.

**Custom cursor:** None. Standard browser cursor throughout. No cursor overlay element in the DOM.

**WhatsApp CTA:** A persistent top-right circular button (pink, WhatsApp icon) that stays fixed across all scroll positions. Treated as a primary conversion action at the same level of prominence as the menu. A bold UX statement about the agency's preferred contact channel.

---

## 5. Typography & Color

### Type System — 2 Families

| Role | Font | Source | Notes |
|---|---|---|---|
| Display / headlines / nav | Beni Black | `/assets/fonts/beni-black.woff2` | Only one weight used; all-caps, very heavy, rounded letterforms |
| Body / UI / labels | Clash Grotesk | `/assets/fonts/clash-grotesk-medium.woff2` + bold | Geometric grotesque; both medium and bold variants |

**Display approach:** Beni Black is used at up to 80px (confirmed) for nav links and display headlines. At viewport scale the letterforms become graphic elements — the "why choose Foudre" section uses text that fills the full 1440px width. Clash Grotesk handles all functional text, body copy, button labels, and service descriptions.

**Class naming convention for type:** `tx-md` (medium size), `tx-l` (large), `tx-menu` (menu size), `tx-upp` (uppercase), `tx-700` (bold weight), `tx-labl` (label) — a token-like atomic system for typographic modifiers.

### Color Palette — 5 Core Values

| Name (CSS class) | Value | Usage |
|---|---|---|
| Green (`.‑bggreen` / `.‑clrgreen`) | `rgb(0, 82, 45)` ≈ `#00522D` | Primary brand; wordmark, menu background, nav hover states |
| Hot pink (`.‑bgpink-2`) | `rgb(242, 158, 189)` ≈ `#F29EBD` | CTA buttons, interactive elements, sticker accents |
| Blush (`.‑bgpink-3`) | `rgb(252, 229, 223)` ≈ `#FCE5DF` | Soft backgrounds, skip-link |
| Cream (`.‑clrwhite`) | `rgb(255, 248, 246)` ≈ `#FFF8F6` | Text on dark/green backgrounds; warm off-white |
| Magenta (section bg) | ≈ `#D43F8D` | Full-section background for the "why choose us" moment |
| Lavender (section bg) | ≈ `#E8E5EE` | Manifesto and expertise sections |
| Olive (section bg) | ≈ `#6B6B3A`–`#5C5830` | Projects/case studies section |

**Palette approach:** The site uses distinct background colors for each content section rather than a single consistent background. The experience shifts between cream, olive, lavender, magenta, and soft pink as you scroll — like moving through rooms, each with its own personality. The fixed forest green and pink accent color unify across these worlds.

### Grid & BEM Architecture

The CSS class naming uses a structured atomic BEM system:
- `o-` prefix = Objects (layout components: `o-header`, `o-menu`, `o-homeHero`)
- `a-` prefix = Atoms (smallest UI: `a-button`)
- `m-` prefix = Molecules (composed components: `m-whatsappCard`, `m-popin`)
- `t-` prefix = Templates (page-level: `t-home`, `t-page`)
- `-` prefix modifier = State/variant modifiers: `-bggreen`, `-clrpink`, `-md`, `-icon`, `-once`, `-active`

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| Lenis (smooth scroll) | **Confirmed** | `window.lenisVersion = "1.1.9"`; `class="lenis"` on `<html>`; `data-scroll` attributes on elements |
| Vanilla JS (no framework) | **Confirmed** | Single bundle `site.C7F8jf3L.js`; no React/Vue/Nuxt/Next detected on `window` |
| GSAP | **Not detected** | No `window.gsap`; animation via CSS transitions only |
| Three.js / WebGL | **Not detected** | 3 canvas elements all 80×48px — UI toggles, not 3D |
| React / Next.js | **Not detected** | No `window.React` or `__NEXT_DATA__` |
| Vue / Nuxt | **Not detected** | No `window.__NUXT__` |
| Tailwind CSS | **Not detected** | Custom atomic BEM class system |
| Google reCAPTCHA | **Confirmed** | Script from `gstatic.com/recaptcha/` — contact form protection |
| Custom color theming | **Confirmed** | `html.-pinklight` class + CSS rules per theme variant (e.g. loader colors change per theme) |

**Architecture summary:** Vanilla JS + Lenis + CSS transitions. No build-chain framework. Single JS bundle. This is a fully bespoke build where every animation is handled by CSS transitions triggered via class manipulation and IntersectionObserver/Lenis scroll hooks. No dependencies beyond Lenis and reCAPTCHA.

---

## 7. Mobile Pass (390×844)

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**Page height mobile:** 13,048px vs 25,062px desktop (48% reduction).

**Hero on mobile (`07-mobile-hero.png`):**
- "FOUDRE" wordmark fills the full 390px width in dark green
- Photo cards below are stacked in a tighter column arrangement
- "Agence social média" subtitle in smaller Clash Grotesk
- "SOCIAL CLUB" tagline in Beni at large scale on the hot pink section below
- Nav buttons stay in the same two-corner positions (hamburger bottom-left, WhatsApp bottom-right) — on mobile they're pushed to lower corners of the visible viewport area

**Content section on mobile (`07-mobile-section.png`):**
- Full hot pink background
- Multi-line Beni display text fills the viewport — very dense, stacked vertically
- Text at mobile size is still very large relative to screen width; the typographic impact is preserved
- Content reflows to single column throughout

**What changes on mobile:**
- Photo collage in hero adapts from a 3-column scatter to a stacked card swipe arrangement
- Horizontal card carousel for projects likely becomes a vertically stacked or swipe-able format
- The two-column expert/service layout collapses to single column
- No visible desktop-only elements removed entirely — the design scales down but preserves all content

**What's preserved:**
- All five section backgrounds (cream, olive, lavender, magenta, pink)
- Both fonts at proportionally reduced but still impactful scale
- The floating WhatsApp + hamburger corner buttons
- Lenis smooth scroll
- The "Case du mois" floating widget

---

## Summary: Key Patterns Worth Studying

1. **Two-corner floating nav** — hamburger top-left + WhatsApp top-right, both as pill/circle buttons. No nav bar. The WhatsApp button being treated as a primary CTA at nav level is a bold conversion-first design decision.

2. **Section-per-color world** — each content section has its own background color (cream → olive → lavender → magenta → pink). Rather than a unified page background, the scroll becomes a journey through distinct visual rooms. Unifying elements (wordmark, nav buttons, floating widget) provide continuity.

3. **Beni Black at typographic extremes** — the "why choose Foudre" section uses display type that fills the full viewport. Text as texture/impact, not just communication. Similar to Phive's approach but applied to a different typeface with softer, rounder letterforms.

4. **Organic blob shapes as decoration** — large SVG amoeba shapes in hot pink appear on section edges (lavender section), not as backgrounds but as floating foreground decoration. The blobs are on-brand (playful, organic, social-media energy) and create visual rhythm.

5. **Clip-path reveals** — text and content use `clip-path` CSS transitions for scroll-triggered reveals. A mask expands to uncover content as it enters the viewport. Cleaner than translate-based reveals; works well for large type.

6. **Spring easing (`cubic-bezier(0.17, 0.67, 0.3, 1.33)`)** — the overshoot control point (>1.0) gives hover interactions a bouncy, playful spring-back. Perfectly matched to the brand personality.

7. **Emoji stickers as editorial elements** — lightning bolts, star shapes, and platform icons overlaid directly on photos. These aren't just decorative; they signal "social media native" brand identity without any additional copy.

8. **Persistent floating client widget** — the "Case du mois" card in the bottom-right corner drifts through multiple sections. A persistent proof-point that travels with the user rather than being buried in one section.

9. **Vanilla JS + Lenis, no framework** — a one-bundle bespoke build. All interaction is CSS transition classes toggled via JS. Demonstrates that a rich, motion-forward site doesn't need React or GSAP.
