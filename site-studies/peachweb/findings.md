# Site Study: peachweb.io

**URL:** https://www.peachweb.io/  
**Studied:** 2026-07-18  
**Type:** No-code WebGL 3D website builder product  
**Viewport (desktop):** 1440×900 | **Viewport (mobile):** 390×844

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

The immediate first impression is a full-screen photorealistic 3D scene — a stylized fish floats above a reflective water surface with purple/pink mountains in the background; two large glass soap-bubble spheres float in the foreground. The eye goes to the fish first, then the landscape. Text is secondary.

**Nav pattern:** Traditional horizontal top bar — logo left, four dropdown nav links center (Product, Use Cases, Resources, Pricing), three auth buttons right (Login, Talk to Us, Get Started — with "Get Started" in an accent orange/peach fill). The nav is sticky; it compresses as you scroll. A Webflow "W." award badge floats on the right viewport edge as a persistent social proof marker.

The bottom-left carries the hero headline and CTAs in white, bottom-right has a "Scroll down & dive in" directional prompt — confirming this is a scroll-narrative experience.

---

## 2. Hero Section

**Screenshot:** `screenshots/01-hero-desktop.png`

**3D element — confirmed, custom engine.** A WebGL canvas at 1296×810px (90% of viewport) sits in a `pwb-scene` wrapper. No Three.js, Babylon, or Spline detected on `window`. The renderer is PeachWeb's own custom WebGL engine — the site is literally built with the product it sells, making it a live demo of the builder's output. Font files are hosted on `files.peachworlds.com`, confirming the CDN is their own infrastructure.

The 3D scene is interactive: the fish and bubbles respond to mouse movement. The scene is highly polished — realistic water reflection, soft atmospheric lighting, and physically-based materials on the fish.

**Entrance animation:** The 3D scene loads as the primary entrance. HTML content fades in over it with `opacity 0.4s`. No loader screen was visible — the 3D scene renders directly.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll driver:** Lenis confirmed via `class="lenis"` on `<html>`. Smooth momentum scroll throughout.

**The defining pattern: one continuous 3D world scrolled like a camera path.**

The entire page is not a series of discrete sections with different backgrounds — it is one persistent WebGL environment that the "camera" moves through as you scroll. The HTML UI elements (text blocks, cards, CTAs) sit as transparent overlays at specific scroll positions in this world. The 3D scenes transition:

- **Hero (~0–2000px):** Purple/pink sky landscape with floating fish and bubbles — above-ground environment
- **Transition (~2000–4000px) — `03-scroll-stage-1.png`:** Scene darkens as the camera descends. A product walkthrough section appears as an HTML overlay (3-step onboarding: Tell Us About Yourself → Pick Your Theme → Edit & Launch, each with a small 3D environment thumbnail). Background shifts to near-black.
- **Transition (~4000–6000px) — `03-scroll-stage-2.png`:** Camera enters underwater. The fish reappears but now swimming through coral and bioluminescent elements. A CTA section overlay ("Start building magic today.") appears.
- **Pure 3D (~6000–8000px) — `03-scroll-stage-3.png`:** Dark undersea environment — minimal HTML overlay, mostly the 3D scene alone. A services/expertise section shows briefly on the left.
- **Underwater reef (~8000–10000px) — `03-scroll-stage-4.png`:** Full lush underwater coral reef — pink/purple corals, glowing white jellyfish, deep blue water. No text overlay at this scroll position — pure environmental storytelling.
- **Footer CTA (~10000px+) — `03-scroll-stage-5.png`:** The fish is centered in the underwater scene. CTA section with full footer navigation links appears below the 3D stage.

**Scroll-linked behavior:** All animation is driven by the WebGL engine interpreting the Lenis scroll position — the CSS layer only uses `opacity 0.4s` for showing/hiding HTML overlays. No GSAP, no ScrollTrigger, no CSS scroll-linked animations on the UI layer.

---

## 4. Micro-interactions

**3D scene mouse interaction:** The fish, bubbles, and environment respond to cursor position — the 3D objects rotate and drift in reaction to mouse movement, creating a parallax-within-parallax effect. This is handled entirely by the WebGL engine.

**Video hover previews:** 12 video elements are present (`video-hover-wrapper` parent class). These appear to be use-case demos (product, ecommerce, storytelling, etc.) that autoplay on hover — hover over a thumbnail and a looping demo video previews. This is a common SaaS marketing pattern but executed here with the videos auto-muted and loop-ready.

**CTA buttons:** Standard hover states with color transitions at `opacity 0.4s`. Orange/peach "Get Started" button uses a solid fill; secondary "Talk to Us" is outlined.

**Custom cursor:** None. Standard browser cursor throughout.

**Nav compression:** The full nav bar compresses slightly on scroll, reducing padding and potentially hiding some links — a functional sticky nav that stays usable.

---

## 5. Typography & Color

### Type System — 2 Families

| Role | Font | Size | Notes |
|---|---|---|---|
| Primary display | Neue Haas Display Roman | 72px / 57.6px / 48px | Regular weight (400); clean geometric sans |
| Body | Neue Haas Display Light | Smaller sizes | Thinner weight variant |
| Serif accent | Instrument Serif Regular + Italic | Accent use | Used for the word "magic" in CTAs; adds warmth |

**Pairing rationale:** Neue Haas Display Roman is the neo-grotesque workhorse — neutral, confident, works over any background including the 3D scene. Instrument Serif Italic appears as a single-word accent (the word "magic"), injecting warmth and humanity into an otherwise technical product pitch.

**All hero text is white** — the dark-to-light values in the 3D scene are managed to ensure legibility, but all HTML text overlays are uniformly white (#ffffff or rgba(255,255,255,0.8)).

### Color Palette

| Role | Value | Usage |
|---|---|---|
| Background (body HTML) | `#ffffff` | Below the 3D canvas, seen in plain content sections |
| 3D scene dominant | Purple/pink gradient ≈ `#7B4FC8`→`#E88EC5` | Hero skyscape environment |
| 3D scene secondary | Deep blue ≈ `#0A1A4A` | Underwater environment |
| Accent / CTA | Orange/peach ≈ `#FF6B35`–`#FF8C42` | "Get Started" button, logo highlight |
| Text | `rgb(255, 255, 255)` | All hero/overlay text |
| Social proof cards (mobile) | Deep violet ≈ `#2D1B8C` | Award cards in mobile content sections |

**Palette approach:** The color "palette" is largely the 3D scene itself — the HTML elements inherit the scene's mood. The only fixed brand colors are the orange/peach CTA accent and white text. The violet/purple of the 3D world becomes the brand's dominant environmental color even though it's rendered, not designed as CSS.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| PeachWeb custom WebGL | **Confirmed** | `class="pwb-scene"`, `pwb-` prefix class system; `window.THREE` undefined; custom renderer |
| Lenis (smooth scroll) | **Confirmed** | `class="lenis"` on `<html>` |
| Custom font CDN | **Confirmed** | Fonts loaded from `files.peachworlds.com` — their own infrastructure |
| Video hover previews | **Confirmed** | 12 `<video>` elements in `video-hover-wrapper` and `video-container` parents |
| GSAP / ScrollTrigger | **Not detected** | No `window.gsap`; no CSS scroll-linked animation on HTML layer |
| Three.js / Babylon / Spline | **Not detected** | None on `window`; custom engine only |
| React / Next.js / Vue | **Not detected** | Single `script.js` bundle; no framework fingerprints |
| Framer Motion | **Not detected** | Confirmed absent |
| Tailwind CSS | **Inferred absent** | `pwb-` prefix classes are builder output; no utility-class patterns |
| AI chat widget | **Confirmed** | `helpaipeach.vercel.app/widget.js` — their own AI assistant product |

**Architecture:** The product and the marketing site are the same thing. A single `script.js` bundle runs the entire page — both the WebGL engine and the UI logic. The `pwb-` prefix DOM elements are the builder's runtime output. The site is literally a live demo of itself.

---

## 7. Mobile Pass (390×844)

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

**Mobile page height:** 12,794px vs 11,188px desktop — slightly *taller* on mobile (unusual; likely due to content stacking).

**Hero on mobile (`07-mobile-hero.png`):**
- The full-bleed 3D scene fills the entire mobile viewport — the purple sky, fish, and bubbles take up 100% of screen width and height
- Logo top-left, hamburger menu icon top-right in a dark pill/badge
- The hero overlay text (headline + CTAs) is not visible at this scroll position — either pushed below the fold or removed on mobile
- A "Need help?" chat widget in bottom-right corner
- The 3D scene renders and is interactive on mobile — the engine adapts to the smaller viewport

**Content section on mobile (`07-mobile-section.png`):**
- Dark near-black background section
- Content organized as stacked cards with deep violet/purple fills and rounded corners
- Award proof cards: "4x No-Code Site of the Month" (with Webflow W. badge) and "Top Web Design Trend 2025" (with Muzli badge)
- Clean Neue Haas Display type at proportionally scaled sizes
- "Get Started →" and "Explore Now →" link-style CTAs within each card
- This appears to be below the 3D hero — the mobile layout shifts to more traditional card stacking for mid-page social proof content

**What's simplified on mobile:**
- The 3-step onboarding section (Tell/Pick/Edit) likely collapses to single column or is simplified
- Horizontal video hover grids become stacked cards
- The nav collapses to hamburger
- The 3D scene may be lighter/more limited on mobile GPU

**What's preserved:**
- The full-bleed 3D hero scene runs on mobile
- Lenis smooth scroll
- Brand color palette and typography

---

## Summary: Key Patterns Worth Studying

1. **Single continuous 3D world as the entire scroll experience** — the most distinctive pattern. The page isn't sections; it's a camera path through one 3D environment. From sky to underwater, the user navigates a world, not a document. HTML content floats through this world at specific camera positions.

2. **The product is the marketing site** — PeachWeb built peachweb.io using PeachWeb. The `pwb-` class system is the builder's live output. The best proof that a product works is running the demo on your own homepage.

3. **WebGL canvas at 90% viewport size** — not a small embedded 3D element but a near-full-viewport rendering surface. Everything else (nav, text, buttons) is an HTML overlay layer with `z-index` sitting above the canvas.

4. **Instrument Serif Italic as a single-word accent** — the word "magic" appears in italic serif within a display sans headline. One word breaks the type register and adds humanity. A technique worth noting: a serif italic for single emotional words within a sans-serif system.

5. **Mouse parallax without scroll** — the 3D objects respond to cursor hover/movement independently of scroll position. Two layers of motion: horizontal (mouse) and vertical (scroll). The fish floats where your attention is.

6. **Video hover previews** — 12 product demo videos that trigger on hover. Lazy loading inferred (src is empty until hover). A common SaaS pattern for showing diverse use cases without navigating away.

7. **White-on-3D text** — all HTML text is white, trusting the 3D scene to provide enough contrast via its own dark/light zones. A risk in a CSS sense, mitigated by controlling the 3D lighting to ensure dark areas where text lives.

8. **Neue Haas Display as the default no-code-but-refined choice** — Neue Haas is the typographic safe harbor for technology products that want to look editorial without being flashy. Its appearance here signals the target audience: designers and brand-focused builders, not developers.
