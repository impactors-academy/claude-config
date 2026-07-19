# Site Study: Nymphai Cosmetics
**URL:** https://nymphaicosmetics.com/  
**Studied:** 2026-07-18  
**Slug:** nymphai-cosmetics

Italian donkey's-milk skincare brand. Custom Shopify theme with a heavily animated, editorial presentation. The overall impression is luxury Italian beauty — classical references (marble pedestals, orchids, archival typography) fused with contemporary motion design.

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

The very first draw is a full-width editorial split: left panel product-on-marble still life, right panel a close-up beauty shot, with large display words overlaid across both panels. The composition is intentionally fragmented — two halves that only make visual sense together, forcing the eye to scan the full width.

**Nav pattern:** Fixed, fully transparent, ultra-sparse. Only two navigation nodes appear as sparse all-caps labels: "HOME" flush left, "PRODOTTI" flush right. The logo mark sits centered. The cart label ("CARRELLO") and an IT/EN language toggle occupy the far right alongside PRODOTTI. There are no dropdowns, no mega-menu — the entire navigation is five elements maximum.

The visual weight is so low the nav nearly disappears into the hero image, functioning more as an orientation artifact than a wayfinding system.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png` → transitions captured in `screenshots/03-scroll-stage-1.png`

The hero is a full-viewport slideshow — product name fragments ("Siero Viso" / "Illuminante") overlay the split panels as large typographic elements, not as a traditional headline block. They appear at different scales and positions, treating the text as a design layer rather than a message layer.

**3D element:** Yes — Spline is integrated via a custom Shopify section asset (`linee-spline.js`). Three canvas elements are embedded in the products section. The wavy cream-texture element visible in the later "ingredients" section (an image embedded inline between text words: "Latte [3D-texture] d'asina") appears to be a Spline-rendered WebGL scene rather than a static image. No Three.js, no Babylon.

Engine confirmation via `window.Shopify` and script tag analysis: Spline runtime loaded as a custom theme asset, not via CDN. This is a deliberate, tightly integrated implementation.

**Entrance animation:** Lenis initiates smooth scroll from load. GSAP with CustomEase likely handles staggered reveals — product image and typographic elements appear to enter from slight vertical offsets. The hero is already mid-state when the page loads (no dramatic splash screen or loader).

---

## 3. Scroll Behavior

**Screenshots:** `03-scroll-stage-1.png` through `03-scroll-stage-5.png`

**Scroll type:** Smoothed via Lenis 1.1.18 (confirmed via script tag). Native scroll events are intercepted and re-emitted with inertia, giving a buttery deceleration on all devices.

**Section transitions — three distinct palette zones:**

| Zone | Background tone | Section IDs |
|------|----------------|-------------|
| Warm cream-stone | ~#c5b8a3 | Hero + product group |
| Muted slate blue-grey | ~#8fa0ac | Brand story + product showcase |
| Warm golden-tan | ~#b8956a | Ingredients/ingredients hero + footer approach |

These are full-bleed background color transitions, not gradient fades — they appear to flip on ScrollTrigger markers as sections enter the viewport.

**Pinned section (key mechanic):** The product showcase section ("prodotti") is a GSAP ScrollTrigger pin. A thin progress bar runs along the bottom of the viewport, and a counter (01/03 → 02/03 → 03/03) ticks up as the user scrolls through the pinned panel. Each product slides in horizontally within the fixed frame: left side shows a pill/arch-shaped botanical photo, right side shows the product bottle floating isolated. The scroll distance on this section is long (it accounts for a large portion of the 13,211px total page height).

**Watermark typography:** In the brand section, the product line name is rendered at enormous scale (~400px+) as a near-invisible watermark below the visible text block. It scrolls at a different rate (parallax offset), acting as a kinetic background texture.

**No horizontal scroll hijacking.** All scroll is vertical.

**Other scroll-linked effects observed:**
- The "Formule performanti" section uses inline image replacement — a rendered cream-texture appears embedded between two words of a headline, suggesting a Spline canvas inserted into flowing text layout.
- Multiple model faces appear at varying scales within a large typographic composition, implying a GSAP Flip or ScrollTrigger-driven layout transition.

---

## 4. Micro-interactions

**Custom cursor:** Confirmed present (`[class*="cursor"]` element found). It renders as a minimal circle outline (visible as a hollow circle in `03-scroll-stage-2.png`). Size and opacity likely shift on hover — appears to swell or fill on interactive elements, which is consistent with the luxury sector standard.

**Buttons/CTAs:** Styled as all-caps spaced labels with a minimal arrow or underline — no filled pill buttons. Text color is warm cream (#f0ede6) on dark backgrounds. CTA labels are "EXPLORE" and "SCOPRI LINEA" — never "Buy" or "Shop" at this funnel level.

**Product thumbnail strip:** A row of 3 small product thumbnails appears at the bottom-right of the pinned product section, acting as a timeline/dot navigation. Active product is highlighted. These likely respond to both scroll and click.

**Language switcher:** IT/EN toggle visible in nav — switches locale inline without full reload.

---

## 5. Typography & Color

**Typeface:** Tenor Sans (confirmed via computed `font-family` on headings). A geometric, optically refined sans-serif with classical proportions — narrow letterforms, high stroke contrast for a sans. Well-suited to Italian luxury beauty: contemporary but not cold.

**Type scale (desktop computed):**
- h1: 51.2px
- h2: 43.2px
- Body (p): 12.8px — notably small, creates a dense, editorial rhythm

Display text used throughout is significantly larger (estimated 80–200px based on visual proportion) — rendered via inline styles or custom classes rather than semantic heading tags.

**Color palette:**

| Role | Value | Note |
|------|-------|------|
| Body base | `#0a0a0a` | Near-black, used as transition/loading base |
| Hero background | ~`#c5b8a3` | Warm cream-stone, organic |
| Brand section | ~`#8fa0ac` | Muted slate blue-grey, dusty/cool |
| Ingredients section | ~`#b8956a` | Warm golden-tan |
| Primary text (dark bg) | `#f0ede6` | Warm cream-white |
| Nav text (light bg) | `#2a2520` | Dark warm brown, near-black |

Three background colors = three acts. No brand color is "electric" or high-chroma — all tones are desaturated and warm. This is a deliberate soft-luxury palette with no shock value.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|-----------|--------|----------|
| Shopify | **Confirmed** | `window.Shopify`, CDN paths, `/cdn/shop/t/2/assets/` |
| Custom Shopify theme | **Confirmed** | Theme name "nymphai", schema "Generated Data Theme" — not a marketplace theme |
| GSAP 3.12.7 | **Confirmed** | Script tags: gsap.min.js + ScrollTrigger + Observer + CustomEase + Flip + Draggable |
| Lenis 1.1.18 | **Confirmed** | `unpkg.com/lenis@1.1.18/dist/lenis.min.js` |
| Spline | **Confirmed** | `linee-spline.js` (custom asset), 3 canvas elements in products section |
| Custom cursor | **Confirmed** | DOM element with `cursor` class |
| Facebook Pixel | Confirmed | `fbevents.js` + signal config |
| Google Analytics | Confirmed | `gtag/js?id=G-850RF49X0C` |
| React / Next.js | **Not present** | No `window.React`, no `__NEXT_DATA__` |
| Tailwind CSS | **Not confirmed** | No matching utility class patterns |
| Three.js | **Not present** | No `window.THREE` |
| Locomotive Scroll | **Not present** | No `window.LocomotiveScroll` |

The GSAP suite is unusually complete — all six plugins loaded. Observer plugin suggests gesture-aware or velocity-based interactions (drag-to-scrub or swipe detection). Draggable likely powers the product thumbnail strip or a touch-drag affordance. Flip is typically used for layout-to-layout morphing transitions.

---

## 7. Mobile Pass (390×844)

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**Hero mobile:** Single-product centered layout. The product bottle is the dominant element at full width, with a model face visible in a smaller card below. A "01/03" counter indicates the hero is swipeable (horizontal product carousel rather than the pinned-scroll mechanic used on desktop). CTA "SCROLL DOWN" appears at the bottom — explicit affordance that the desktop version omits.

**Nav mobile:** Hamburger (≡) top-left, logo centered, cart icon + IT dropdown top-right. The sparse two-node desktop nav collapses to a standard hamburger. The overall chrome remains minimal — same floating-over-content treatment.

**Brand section mobile:** Stacked single-column. The large centered editorial headline runs to 5+ lines at 390px, which creates an immersive full-screen text block before the supporting photo card appears. This is intentional — the long heading becomes a pacing device. The supporting image card uses a standard rounded-rectangle crop rather than the pill/arch format used on desktop, likely a simpler asset swap.

**What's removed/simplified:**
- Pinned scroll-driven product sequence replaced by a swipeable carousel
- Watermark typography may be scaled down or removed (not visible in captured section)
- Spline canvas elements — unclear if rendered on mobile; not visible in hero capture (may lazy-load or be suppressed at narrow viewport)
- Custom cursor removed (cursor is pointer/touch device)
- Progress bar at bottom may still be present but not visible in these captures

---

## Summary / Patterns Worth Stealing

1. **Three-act palette:** Hard section color transitions (not gradients) across three warm-but-distinct tones give the page a chapter structure without any text-based section dividers. The color IS the navigation.

2. **Pinned scroll product theater:** A GSAP ScrollTrigger pin turns linear scroll into a product showcase with a bottom progress bar + counter — gives multiple products sustained dwell time without requiring click navigation.

3. **Inline Spline texture in typography:** Embedding a 3D-rendered WebGL texture between two words of a headline ("Latte [texture] d'asina") is an unusual and high-craft technique. The 3D element becomes punctuation.

4. **Nav as near-invisible chrome:** Only five elements in the fixed nav, transparent, never distracting. Trust in the product imagery to carry the experience — the nav is a last resort, not a primary tool.

5. **Watermark type as kinetic texture:** Giant, near-opacity-zero line name scrolling behind body text creates depth without a dedicated background graphic or image.

6. **Tenor Sans as the flex point:** The typeface does the aesthetic heavy lifting — editorial, Italian, refined — so the color palette and layout can stay restrained.
