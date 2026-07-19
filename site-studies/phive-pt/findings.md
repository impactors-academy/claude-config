# Site Study: phive.pt/en

**URL:** https://phive.pt/en  
**Studied:** 2026-07-18  
**Built by:** Bürocratik (footer credit: "Made by Büro")  
**Viewport (desktop):** 1440×900 | **Viewport (mobile):** 390×844

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

First impression is an immediate high-energy impact: a vivid yellow horizontal band bisects a full-bleed athlete photo, bearing the brand name in massive condensed type running as a scrolling marquee. The eye goes to the yellow stripe first — it cuts across the photograph as a graphic element, creating tension between kinetic type and image.

**Nav pattern — bottom-docked bar.** There is no traditional top nav. A slim horizontal bar pinned to the bottom viewport edge holds three elements: a hamburger/menu icon (left), the brand wordmark centered, and a sound wave/equalizer button (right). Clicking the hamburger opens a full overlay menu with club listings (5 locations, each with a thumbnail image). Language toggle (PT / EN) lives inside that drawer. The bottom bar leaves the hero viewport completely uninterrupted.

The sound button signals ambient audio as a designed feature — a premium brand signal.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png`

The hero is a full-viewport carousel driven by autoplay looping video (muted, `autoplay=true loop=true muted=true`). Four separate videos with club-specific filenames (e.g. `porto-mobile.mp4`, `lisboa-mobile.mp4`) cycle through. Over each video, a yellow horizontal band runs edge-to-edge carrying an infinite scrolling marquee of the brand name and club location in ultra-condensed AcidGrotesk. Status copy and a location link sit within the band. The photo bleeds above and below the yellow stripe.

**3D elements:** No Three.js, Babylon, or Spline runtime detected on `window`. However, 8 canvas elements are present; 1 confirmed WebGL context at full-viewport resolution (1425×900px). The WebGL element is most visible mid-scroll (section 3 below) as a floating 3D weight plate — it likely initializes on load but becomes prominent later. Small canvas icons (48px, 96px) render the sound equalizer and UI button icons.

**Entrance animation:** Each heading element uses split-text character-level markup — every letter wrapped in its own span — indicating a character-by-character stagger entrance animation on load. The easing used throughout the site is `cubic-bezier(0.19, 1, 0.22, 1)`, an expo-out curve: fast departure, very slow arrival, giving motion a springlike physical quality.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll driver:** Lenis confirmed — the `<html>` element carries `class="lenis"`, Lenis's own DOM marker. The entire page has buttery inertia-based smooth scrolling. No GSAP ScrollTrigger detected (no pin-spacers, no `window.ScrollTrigger`). Scroll-linked animation is likely driven by Lenis's scroll-progress events or Intersection Observer, with CSS transitions as the animation layer.

**Page length:** ~15,500px desktop. Sections alternate strictly between vivid yellow and near-black — no intermediate grey or neutral sections.

**Stage 1 (~3000px) — `03-scroll-stage-1.png`:** Near-black background (`#161003`). Facility photos (pools, gym floor, studios) arranged in a scattered collage — intentional misalignment, slight rotation, no grid. A giant yellow AcidGrotesk wordmark overlays the collage at display scale, with secondary "choose your club" copy nested within the letterforms.

**Stage 2 (~6000px) — `03-scroll-stage-2.png`:** The most striking moment. Background flips to vivid yellow. AcidGrotesk at absolute maximum scale — "FITNESS" fills the viewport width, letterforms cropped at both left and right edges. The word is treated as texture, not readable headline. A PureHeart handwritten script word ("go") is inset inside the type. Most notably: a photorealistic 3D branded weight plate floats over the letterforms, rendered in WebGL with realistic materials and studio lighting. As you scroll it appears to follow a slow rotation path. "STRONG" begins to emerge below at the same extreme scale.

**Stage 3 (~9500px) — `03-scroll-stage-3.png`:** Background transitions from yellow to a full-bleed gym interior photo. The same 3D weight plate carries through from the previous section, floating over the photo — it bridges the color-block transition and creates spatial continuity between the typographic and photographic sections.

**Stage 4 (~12500px) — `03-scroll-stage-4.png`:** Returns to near-black. Classes card grid with thumbnail images and category pill tags. Below, an app download section introduces the brand yellow again for the section headline, against a dark background with a phone mockup.

**Stage 5 (~15000px) — `03-scroll-stage-5.png`:** Footer/social section on yellow. Four circular-cropped photos represent social platforms (IG, FB, YT, TK), each labeled with a two-letter abbreviation in condensed black type, arranged in a loose row. Footer below: legal links left, agency credit right.

---

## 4. Micro-interactions

**Button hover — `cubic-bezier(0.19, 1, 0.22, 1)` at 0.25s** — color and background-color transitions on all interactive elements use this expo-out easing. Snappy trigger, slow settle.

**Variable font hover animation — the standout technique.** AcidGrotesk is a variable font (`AcidGroteskVF.woff2`). CSS transitions on `font-variation-settings` and `letter-spacing` run at `0.75s cubic-bezier(0.075, 0.82, 0.165, 1)`. This means hover states can morph the weight, width, or contrast axes of the letterforms fluidly in the browser — no JS required. The effect is subtle and perceptible only as type feeling "alive" on hover, invisible to most users but technically sophisticated.

**Transform entrance animations:** `transform 1.5s cubic-bezier(0.19, 1, 0.22, 1)` on some elements — a very slow, weighty settle that makes entering content feel physically heavy rather than decorative.

**Custom cursor:** None detected. No cursor overlay element in the DOM. System pointer used with `cursor: pointer` on interactable elements.

**Sound button:** Canvas-rendered (48px canvas icon). The equalizer waveform icon animates to represent audio playback state. Ambient audio is a toggleable feature.

---

## 5. Typography & Color

### Type System — 3 Distinct Families

| Role | Font | Notes |
|---|---|---|
| Display headlines | AcidGrotesk (variable, `AcidGroteskVF.woff2`) | Ultra-condensed at viewport-filling scale; `font-variation-settings` animated on hover |
| Body / UI / base | PPFormula (`PPFormula.woff2`) | Custom; used for body copy, captions, functional text |
| Script accent | PureHeart (`PureHeart.ttf`) | Handwritten; used as single-word interjection nested inside display type |

**Display scale strategy:** AcidGrotesk at maximum size fills the full viewport width with letterforms cropped at both edges — type treated as graphic texture, not readable headline. This approach works only with a typeface that has strong, legible stroke weight at extreme scale.

**Three-register contrast:** The system deliberately juxtaposes geometric grotesque (AcidGrotesk) at extreme scale, a functional grotesque (PPFormula) for secondary content, and a flowing script (PureHeart) for tonal moments. The script font appears once or twice on the page; its rarity is what gives it impact.

### Color Palette

| Role | Value | Usage |
|---|---|---|
| Primary / dominant background | `#FFD904` (rgb 255, 217, 4) | Body background; hero band; section backgrounds; nav bar |
| Dark background | `#161003` | Near-black with warm brown undertone (not pure black); alternating sections |
| Text on dark | `#ffffff` | White |
| Text on yellow | `#161003` | Same near-black |

**Two-world system.** The site alternates strictly between yellow and near-black — zero grey, zero midtones, no neutrals. All color richness comes from the video and photo content. This binary palette gives the scroll a strong visual rhythm.

### Grid & Layout

16-column CSS grid system, max-width `106.25rem` (~1700px), fluid gutters and padding via `clamp()`. A fine grid enabling tight editorial control at large viewport widths.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| Nuxt.js (Vue 3) | **Confirmed** | `window.__NUXT__` present; `_nuxt/` bundle chunk URLs in `<script src>` |
| Lenis smooth scroll | **Confirmed** | `window.lenisVersion` string; `class="lenis"` on `<html>` |
| WebGL (custom / bundled) | **Confirmed** | 1 WebGL canvas at 1425×900px; no Three.js / Babylon on `window` — self-contained ES module |
| AcidGrotesk variable font | **Confirmed** | `font-variation-settings` CSS transition; `AcidGroteskVF.woff2` @font-face |
| Autoplay looping video | **Confirmed** | 8 `<video>` elements; 4 autoplay muted loop (hero); 4 loop-on-trigger |
| GSAP / ScrollTrigger | **Not detected** | No `window.gsap`; no pin-spacer elements; motion via CSS transitions |
| Three.js / Babylon / Spline | **Not detected** | No window globals; 3D is self-contained |
| React / Next.js | **Not detected** | Vue/Nuxt architecture |
| Tailwind CSS | **Not detected** | Custom class naming (e.g. `menu-inner`, `sound-btn`, `items-container`) |
| Google Analytics (GA4) | **Confirmed** | GTM + GA4 script tags |
| Facebook Pixel | **Confirmed** | `connect.facebook.net/fbevents.js` |
| TikTok Pixel | **Confirmed** | `analytics.tiktok.com` scripts |
| Umami Analytics | **Confirmed** | `cloud.umami.is/script.js` |
| Cookiebot | **Confirmed** | `consent.cookiebot.com` consent management |

---

## 7. Mobile Pass (390×844)

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**Page height:** ~15,500px desktop → ~7,000px mobile (55% reduction). Significant content consolidation.

**Video assets:** Mobile loads club-specific `-mobile.mp4` variants (separate assets, e.g. `porto-mobile.mp4`), not just responsive sizing of desktop video.

**Layout changes:**
- Bottom nav bar persists — same structure (hamburger | wordmark | sound icon)
- The giant display type on yellow sections maintains its viewport-filling approach at mobile scale; "STRONG" visible filling the 390px width in `07-mobile-section.png`
- The 3D weight plate persists on mobile
- Section sections reflow from side-by-side to stacked single-column
- Social circle section is simplified but carries through

**What's removed/simplified:** Some multi-panel split layouts collapse. The scattered collage layout may simplify. The full page length reduction from 15.5k to 7k px suggests significant consolidation of intermediate sections.

**What's preserved:** Yellow/near-black binary palette, three-typeface system, bottom nav, Lenis smooth scroll (active regardless of viewport), ambient sound toggle, 3D WebGL element.

---

## Summary: Key Patterns Worth Studying

1. **Bottom-docked nav** — inverting the nav to the bottom of the viewport leaves the hero completely uninterrupted and is an unusual structural choice that works because the brand is strong enough to anchor the top without navigation.

2. **Yellow as total environment** — not a section accent or CTA color, but the body background. The near-black sections create their own world; yellow is the ground state everything returns to.

3. **Type as texture** — AcidGrotesk at viewport-filling scale, deliberately cropped at both edges, turns letterforms into graphic elements. Readable content is secondary; the typographic mass is the effect.

4. **WebGL object bridging sections** — the 3D weight plate floats through the yellow typographic section and the photographic gym interior section, providing visual continuity across a background color swap. Using a 3D object as a transition device rather than as a hero centerpiece.

5. **Variable font hover** — animating `font-variation-settings` in CSS means letterforms morph in weight/width on hover without any JavaScript. Invisible to most users, immediately felt as "this type feels different."

6. **Lenis + Nuxt without GSAP** — the full scroll experience is built on CSS transitions + Lenis, no GSAP dependency. Demonstrates that a cinematic scroll feel doesn't require a heavy animation library.

7. **Sound as a first-class feature** — ambient audio with a canvas-rendered waveform icon says the brand has a sonic identity. Rare for fitness brands, common in luxury/lifestyle digital.

8. **`cubic-bezier(0.19, 1, 0.22, 1)` expo-out** — appears consistently across button hover, transform entrances, and color transitions. Worth capturing as a named design system easing constant for this level of premium feel.
