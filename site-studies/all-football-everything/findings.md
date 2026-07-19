# Site Study: All Football Everything (Nike × HY.AM STUDIOS)
**Original URL:** https://www.all-football-everything.com/  
**Status:** OFFLINE — domain expired/not resolving as of 2026  
**Studied via:** Awwwards listing + Wayback Machine archive (web.archive.org/web/20180816010417)  
**Award:** Awwwards Honorable Mention — October 13, 2017  
**Studio:** HY.AM STUDIOS  
**Note:** The live site is fully down. Analysis is reconstructed from the Awwwards preview image (`screenshots/01-hero-desktop-awwwards-preview.png`), the Wayback Machine archive (`screenshots/01-hero-desktop.png`), and confirmed JavaScript/DOM data from the archived version. The archived JS fails to initialize scroll/video behavior, so screenshots show only partial rendering.

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`, `screenshots/01-hero-desktop-awwwards-preview.png`

The Awwwards preview image shows a **full-bleed black viewport** with a single large white heading — no traditional navigation bar visible. This is a **linear, single-page campaign experience**, not a conventional nav-driven site. The page appears to function as a guided scroll narrative, where scrolling moves from club chapter to club chapter.

First impression is total contrast arrest: pure black background, maximum white headline typography, zero UI chrome. The eye goes immediately to the oversized display text.

**Nav pattern:** Minimal or absent. This is a promotional campaign landing page — the only visible UI element in the preview is a "Shop the look" CTA at the bottom of each section. No sticky header detected.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop-awwwards-preview.png`

The hero presents the campaign's central statement split across three lines in oversized heavy type: the three words of the site name stacked on left, with a subtitle phrase contrasting "performance" and "lifestyle" woven between. The background is pure black with what appears to be a looping background video (confirmed: 5 `<video autoplay loop>` elements in the DOM).

**No 3D.** No `<canvas>` elements. No Three.js, Spline, or Babylon in window scope.

**Video backgrounds confirmed:** 5 video elements with `autoplay` and `loop` attributes — one per club chapter. These play silently behind the text, providing cinematic motion without JS-driven animation.

**Entrance animation:** Likely a fade or vertical slide-up of the headline text on page load (consistent with jQuery + custom `trigger.js` in the bundle), but not observable in the archived version due to JS failures.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png`, `screenshots/03-scroll-stage-2.png`

**Scroll is native with parallax overlay.** The bundled script includes `jquery.paroller.js`, a lightweight jQuery parallax library that creates scroll-linked depth effects on background images/videos.

**Page structure (from archived DOM snapshot):**

The page is organized as a sequence of full-viewport "club chapters," each triggered by scroll position:

| Chapter | City motto | Kit label |
|---|---|---|
| Intro | "All Football Everything / from performance to lifestyle" | — |
| PSG | "ici, c'est paris." | 3rd kit |
| Barcelona | "Mes Que Un Club." | 3rd kit |
| Berlin (Hertha BSC) | "Ich bin ein Berliner." | 3rd kit |
| + 2–3 more clubs | Additional city mottos | 3rd kit |

Each chapter uses the club's cultural identity tagline as the hero text rather than product copy — a content strategy decision, not just a design one.

**Scroll behavior observed:** Native scroll. Parallax via `jquery.paroller.js` on background layers. An Owl Carousel handles the horizontal product image strip within each chapter ("Shop the look" section with numbered navigation). Masonry handles any grid layout in the lower e-commerce section.

---

## 4. Micro-interactions

Based on script bundle contents (partially verifiable in archive):

- **Parallax depth on scroll:** `jquery.paroller.js` creates foreground/background layer separation as user scrolls — background video/image moves slower than content text.
- **Scroll trigger reveals:** `trigger.js` in the bundle is a custom or lightweight scroll-observation utility — likely triggers class additions on elements entering the viewport (fade-in, slide-in).
- **Image lazy loading:** `lazysizes.js` defers image loads until near-viewport.
- **Touch/swipe support:** `jquery.mobile-events.min.js` adds swipe gesture handling, enabling touch-scroll navigation between sections.
- **Product carousel:** Owl Carousel 2.2.1 with numbered navigation (visible "1" counter in snapshot = slide indicator).
- **No custom cursor** detected. No magnetic hover effects. Interactions are gestural (scroll/swipe) rather than cursor-based.

---

## 5. Typography & Color

### Type

| Element | Font | Notes |
|---|---|---|
| All display text | `Avenir LT W01_85 Heavy` | Adobe Fonts delivery; Avenir 85 Heavy — a clean, geometric grotesque at maximum weight |
| Body / labels | `Avenir LT W01_85 Heavy` | Single typeface system — no contrast between display and body families |

**Typography approach:** One font, one weight (Heavy), at extreme scale contrasts. City mottos appear to run at 80–120px+ based on the preview image proportion. Kit labels ("3rd kit") run small as captions. This single-weight monoculture creates cohesion across disparate cultural content.

### Color Palette (from Awwwards listing)

| Role | Hex | Usage |
|---|---|---|
| Background | `#000000` | Full-bleed black throughout |
| Accent | `#D14836` | Nike red — CTAs, highlights |
| Text | `#ffffff` | All display and body copy |

Stark three-value palette: no grays, no gradients. The black ground makes looping video backgrounds visible as texture without competing for attention. Nike red is used sparingly as the single brand signal.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| **WordPress** | Confirmed | `wp-content/themes/all-football-everything/` in script paths |
| **jQuery 2.2.3** | Confirmed | Bundled explicitly in minified script URL |
| **jquery.paroller.js** | Confirmed | Bundled in footer script — provides parallax scrolling |
| **Owl Carousel 2.2.1** | Confirmed | Bundled — product image carousels |
| **Masonry 4.2.0** | Confirmed | Bundled — grid layout engine |
| **lazysizes** | Confirmed | Bundled — lazy image loading |
| **imagesloaded** | Confirmed | Bundled — fires callbacks after images load |
| **Modernizr** | Confirmed | Bundled — feature detection |
| **mobile-detect.js** | Confirmed | Bundled — device/browser detection |
| **Autoloop background video** | Confirmed | 5 `<video autoplay loop>` elements in DOM |
| **GSAP / TweenMax** | Not detected | Not in window scope (archived) |
| **Three.js / WebGL** | Not detected | No canvas, no window.THREE |
| **React / Vue / Next.js** | Not detected | WordPress + jQuery architecture |

**Build era:** This is a 2017 site. The stack is pre-React-dominance WordPress with jQuery plugins — the standard high-quality agency approach for that year. The sophistication is in the concept and content strategy, not the JS framework.

---

## 7. Mobile Pass

Mobile screenshots not directly capturable from the dead domain, but the Awwwards tags include **"Responsive Design"** and the script bundle includes `mobile-detect.js` + `jquery.mobile-events.min.js`, confirming:

- Responsive layouts built into the WordPress theme
- Touch/swipe gesture support replacing the click-scroll interaction
- The club chapter navigation likely collapses to a swipe gesture on mobile
- Owl Carousel has built-in touch support

**Expected mobile simplifications:**
- Large display type would scale down proportionally
- Background videos may be replaced by static poster images on iOS (standard `playsinline` behaviour of that era)
- Parallax depth effect likely disabled on mobile (common `jquery.paroller.js` behavior)

---

## Summary: Key Patterns Worth Studying

1. **Club chapter scrolling narrative** — a single-page site where each full-viewport section = one cultural identity. Content is a travel itinerary, not a product catalogue. The user scrolls through cities, not through SKUs.

2. **Cultural motto as hero text** — using the club/city's own tagline at display scale rather than any brand or product headline. Positions Nike as the connector of cultural identities, not the hero.

3. **Looping video backgrounds per chapter** — 5 silent autoloop videos provide cinematic motion at zero interaction cost. No play button, no user decision — motion is ambient.

4. **Single heavy typeface, infinite scale contrast** — Avenir 85 Heavy at ~120px vs. 14px caption creates a reading hierarchy with no secondary typeface needed.

5. **Three-value color palette** — black / white / Nike red, nothing else. All "color" comes from the video backgrounds, which reinforces the idea that the clubs bring the color and Nike brings the frame.

6. **Scroll as chapter-turning** — parallax depth + scroll trigger reveals make the act of scrolling feel like page-turning in a lookbook, not like browsing a website.
