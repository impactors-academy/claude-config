# Site Study: cula.tech
**Date:** 2026-07-18
**Viewport studied:** 1440×900 (desktop), 390×844 (mobile)

---

## 1. Navigation & First Impression

**Screenshot:** `screenshots/01-hero-desktop.png`

The very first impression is a full-bleed dark scene — a cinematic 3D environment fills the entire viewport with a globe/wireframe grid backdrop. The word mark and tagline float over the top of it. The "SCROLL TO BEGIN" prompt with a down-arrow sits at the bottom center, making the scroll intent explicit.

**Nav pattern:** The nav floats as a contained pill/capsule centered at the top of the screen — not full-bleed, not sidebar. It holds three text links (Home / Insights / About) plus a separate dark-filled CTA button ("→ Talk to us"). On scroll this nav stays fixed at position top: 0px. The background behind the nav links is light/translucent — the logo and nav sit on top of whatever scene is below. On mobile the three links collapse into a hamburger icon; the logo and CTA remain visible.

---

## 2. Hero Section

**Screenshot:** `screenshots/03-scroll-stage-1.png`

The hero is a scroll-driven cinematic 3D sequence — the entire upper portion of the page (roughly 6,500–7,000px of scroll height) is a pinned "stage" that advances through a series of photorealistic 3D environments as the user scrolls. This is not a WebGL/Three.js canvas: no `<canvas>` elements were detected, no `window.THREE` is present. The visuals are pre-rendered 3D imagery (likely video frames or high-res image sequences) with scroll-position-linked playback managed by Framer's native scroll animation engine.

**Sequence of scenes (scroll-linked):**
1. **Globe wireframe** — A technical grid/sphere wireframe on a pale background. "SCROLL TO BEGIN" anchors the bottom.
2. **Ground-level 3D truck scene** — A photorealistic semi-truck sits on a grid-tile platform surrounded by glowing electric-blue data points and particle clusters floating at sensor locations. Dark background, high contrast. The tagline appears bottom-left; a secondary line bottom-right.
3. **Aerial industrial flyover** — Camera perspective shifts to an overhead drone view of a real-world carbon removal facility. Caption "Any Technology" fades in bottom-left, implying the platform-agnostic pitch.
4. **Tighter aerial zoom** — Same facility, tighter angle, different building cluster. Caption transitions from "Any Technology" to "Any Scale" using a vertical slide, suggesting a looping concept stack within the same pinned zone.
5. **LED logo reveal** — A full-viewport dark scene where the Cula logomark renders as a glowing dot-matrix / LED grid. Very dramatic pause in the scroll-story. Text "All your data collection / Fully automated" overlays.

There is no entrance animation on load that was observable; the first frame appears immediately on navigation.

---

## 3. Scroll Behavior

**Screenshots:** `screenshots/03-scroll-stage-1.png` through `03-scroll-stage-5.png`

- **Page height:** 15,682px — exceptionally tall due to pinned scroll sections.
- **Scroll type:** Native browser scroll (`scroll-behavior: auto`, no Lenis or Locomotive Scroll detected). Framer manages all scroll-linked animation internally via its own runtime.
- **Pattern:** Multiple sticky/pinned sections (several `position: sticky; top: 0px` and one `position: fixed; top: 0px` nav). Each section pins the viewport and advances its internal animation state proportional to scroll progress.
- **Horizontal scroll:** None detected.
- **Parallax:** Implicit through the scene-transition mechanism — the 3D scenes themselves create depth as they shift, but no classic CSS parallax layering.
- **After the scroll-story:** The page returns to a standard vertical layout for features (cards with product UI), logo marquees (standards and clients), an insights grid, and a featured case study card.

---

## 4. Micro-Interactions

**Nav link hover:** Each nav link contains two identical text paragraphs stacked in the DOM (confirmed in the accessibility snapshot). This is Framer's standard hover text-slide pattern: one text layer slides out upward while the clone slides in from below, creating a smooth "text roll" hover state. Low footprint, high refinement.

**CTA button ("→ Talk to us"):** Deep navy fill (#0D2039 approx), rounded corners (8px), with an external link arrow glyph prefix. The class references in the snapshot suggest light/dark cursor variants fire on hover — likely a subtle invert or fill shift.

**Cursor:** No custom cursor DOM element was detected. The site uses the browser's default cursor, though CSS cursor-variant class names appear on elements (`cursor-light`, `cursor-dark`) — these appear to be Framer component variants, not a global cursor replacement.

**Logo marquees:** Two infinite-scroll ticker rows (standards logos, client logos) run in opposite directions — a common credibility-stacking pattern. No hover-pause was directly tested but the implementation is standard Framer marquee.

---

## 5. Typography & Color

**Typeface:** **Geist** (Vercel's open-source geometric sans-serif) — single typeface used system-wide with no serif or display secondary.

| Element | Size | Weight |
|---|---|---|
| Footer tagline H1 | 48px | 600 |
| Section H2 | 32px | 600 |
| Body paragraph | 18px | 600 |

All weights are semibold (600) — there is no light or regular weight variant in use; the hierarchy is created through size alone, not weight contrast.

**Palette:**
| Role | Value | Approximate Hex |
|---|---|---|
| Background | rgb(252, 253, 254) | #FCFDFE — near-white, cool tint |
| Primary text & UI | rgb(13, 32, 57) | #0D2039 — deep navy |
| CTA button fill | rgb(13, 32, 57) | same deep navy |
| Accent (in imagery) | Electric teal-blue | ~#00AAFF — in 3D scene lighting, not in CSS |

The overall palette is two-tone (navy on near-white) — maximum contrast, zero distraction. The blue-teal "accent" only exists within the pre-rendered 3D imagery and the LED logo scene, not as a CSS color anywhere in the UI layer.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| **Framer** | Confirmed | `framerusercontent.com/sites/.../script_main.*.mjs`, `events.framer.com/script?v=2` |
| **PostHog** | Confirmed | `eu-assets.i.posthog.com` analytics script |
| **Google Analytics** | Confirmed | `gtag.js?id=G-16XCTCH4BQ` |
| **Three.js / WebGL** | Not present | No `<canvas>`, no `window.THREE` |
| **Spline** | Not present | No Spline runtime detected |
| **GSAP / ScrollTrigger** | Not present | No `window.gsap` or `window.ScrollTrigger` |
| **Lenis / Locomotive Scroll** | Not present | Not on `window`, not in scripts |
| **React / Next.js** | Not present | No `window.__NEXT_DATA__`; Framer generates its own React bundle |
| **Tailwind CSS** | Not present | No utility class patterns; Framer's scoped CSS handles styling |

**Notable:** 104 elements carry animation properties (`will-change`, `transform`, or `data-framer-appear-id`). All scroll-linked animation is handled by Framer's internal runtime — no third-party scroll library is needed. The 3D "video" sequence is almost certainly pre-rendered image frames or a video element with `currentTime` driven by scroll position (a technique Framer supports natively).

---

## 7. Mobile Pass

**Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`

- **Nav:** Collapses to logo + hamburger icon only. The "Talk to us" CTA disappears from the top bar on mobile.
- **Hero:** The full-bleed wireframe globe/grid scene scales to fill the 390px-wide viewport. The tagline and "SCROLL TO BEGIN" prompt remain. The scroll-driven 3D sequence appears to persist on mobile (the aerial "Any Technology" scene is visible at 1800px scroll).
- **Typography:** Headline text is significantly smaller on mobile — the two-line treatment wraps tighter. The subtagline sits right-aligned below (same split as desktop).
- **Simplifications:** No visible layout reflow beyond nav collapse and type scaling. The same scene-transition scroll story appears to run on mobile, making this a mobile-first or at minimum mobile-parity experience.

---

## Key Design Patterns to Note

1. **Scroll-story as hero** — The entire "above the fold" experience is a pinned, scroll-driven cinematic narrative. Users commit to scrolling through ~7,000px of story before reaching conventional content. High-risk, high-reward: it communicates the product's precision/depth through its own storytelling format.

2. **Two-tone plus 3D** — The light UI layer (near-white + navy) is deliberately minimal so that the full-color 3D imagery feels like a window cut through the page, not a decoration added to it.

3. **Geist single-weight** — Using one typeface at one weight (600 semibold) everywhere flattens hierarchy to size-only. Works because the type never has to compete with itself — the imagery does all the visual work.

4. **LED/dot-matrix brand moment** — The Cula logo rendered as glowing dots mid-scroll is a brand "pause" that burns the mark into memory at exactly the moment the user has invested the most scroll effort. Smart placement.

5. **Dual text-layer nav hover** — Text roll on nav links is a low-cost, high-craft detail that rewards close attention without announcing itself.
