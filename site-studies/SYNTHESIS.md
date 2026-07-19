# Site Studies — Synthesis

**Sources:** 12 completed studies across agencefoudre, all-football-everything (archived), apple, cula-tech, ducati-superleggera-v4-centenario, no-football-colors, nymphai-cosmetics, peachweb, phive-pt, the-watch, voxelo-ai, xnrgy-club. (primal-training-club: domain expired, excluded.)

---

## 1. Recurring Patterns

### 1.1 Lenis Smooth Scroll
**Sites:** agencefoudre, nymphai-cosmetics, peachweb, phive-pt, voxelo-ai, xnrgy-club (6 of 12 confirmed; cula-tech uses Framer's equivalent)

**Mechanism:** Lenis replaces native browser scroll by intercepting the `wheel`/`touch` events and re-emitting scroll progress through its own RAF loop with configurable easing (typically `lerp: 0.1`). The `<html>` or `<body>` element carries `class="lenis"` as a DOM marker. All other scroll-linked animations (GSAP ScrollTrigger, IntersectionObserver, Three.js `scrollY` readers) hook into Lenis's emitted scroll value rather than `window.scrollY`. No site in this study used Locomotive Scroll — Lenis 1.x has fully replaced it as the default.

---

### 1.2 Section-per-Color-World
**Sites:** agencefoudre (5 zones: cream → olive → lavender → magenta → pink), nymphai-cosmetics (3 zones: cream-stone → slate-grey → golden-tan), phive-pt (binary: yellow ↔ near-black)

**Mechanism:** Each major section has its own `background-color`. These are hard cuts at section boundaries, not CSS gradients. Transitions are triggered by IntersectionObserver or ScrollTrigger `onEnter`/`onLeave` callbacks toggling a class on the section element. Fixed/persistent elements (nav, floating widgets) use a separate color variable that updates in sync. The scroll becomes a journey through distinct visual rooms — unifying elements (logo, nav) provide continuity across the color changes. On mobile, all color zones survive; layout reflows but the color rhythm persists.

---

### 1.3 Display Type at Viewport Scale
**Sites:** agencefoudre (Beni Black, ~full 1440px width), phive-pt (AcidGrotesk cropped at both edges), xnrgy-club (187px NeueHelvetica, −10px letter-spacing), the-watch (350px Nekst), voxelo-ai (108px Bricolage Grotesque), no-football-colors (120px Obviously Narrow)

**Mechanism:** Headline font-size set to `clamp()` values that reach 150–350px+ on desktop. Letterforms are intentionally cropped at viewport edges via `overflow: hidden` on the parent — the text is not meant to be fully read, it becomes graphic texture. Always paired with a much smaller secondary typeface for actual readable content. The technique works only with high-stroke-weight faces; thin fonts collapse into noise at this scale.

---

### 1.4 Split-Text Character-Level Entrance Animations
**Sites:** phive-pt (every character wrapped in individual `<span>`, cubic-bezier(0.19, 1, 0.22, 1) expo-out), xnrgy-club (per-character DOM wrapping for stagger), cula-tech (dual text-layer nav roll via Framer)

**Mechanism:** Each letter of a headline is wrapped in its own `<span>` (either pre-rendered in the HTML or via a JS split-text utility at runtime). On load or scroll-enter, a staggered animation fires: `opacity: 0 → 1` + `translateY(20px → 0)` with a per-character delay of `i * 0.03s`. The expo-out easing (`cubic-bezier(0.19, 1, 0.22, 1)`) gives each character a fast departure and slow landing, producing a physical wave-snap quality rather than a mechanical uniform fade.

---

### 1.5 Infinite Horizontal Marquee / Ticker
**Sites:** phive-pt (brand name over hero band, continuous), no-football-colors (counter-direction dual-row: "No. Clubs. No Colors."), voxelo-ai (announcement bar above nav)

**Mechanism:** The content element is duplicated exactly once and both copies placed end-to-end in a row. `animation: marquee linear infinite` translates the pair `translateX(-50%)`, so when the first copy exits left the second is already aligned. Speed is set via `animation-duration`. Pausing on hover: `animation-play-state: paused` on `mouseenter`/`mouseleave`. The counter-direction variant on no-football-colors runs a second row at `translateX(50%)` creating two opposing lanes.

---

### 1.6 Looping Video as Ambient Background
**Sites:** apple (4 WebM clips per product tile, CDN-served), all-football-everything (5 club-chapter videos, `<video autoplay loop>`), phive-pt (4 club-specific `-mobile.mp4` variants for hero carousel)

**Mechanism:** `<video autoplay muted loop playsinline>` elements placed as position-absolute backgrounds behind text. No interaction required — motion is ambient. Mobile gets distinct video files (not just CSS resizing): phive-pt's `-mobile.mp4` naming and Apple's `largetall.webm` / `small.webm` responsive `<source>` suffixes show the pattern. On iOS, `playsinline` is required or the video fullscreens. Quality comes from pre-rendering — these sites achieve "3D quality" cinematics without any real-time 3D engine.

---

### 1.7 Scroll-Linked 3D Camera / Scene Progression
**Sites:** cula-tech (Framer scroll-driven image sequence through pre-rendered 3D environments, ~6,500px pin zone), ducati (canvas scrollytelling 20,104px; scroll position changes the canvas-rendered frame), peachweb (custom WebGL world scrolled like a camera path, sky → underwater, 11,188px), the-watch (Three.js r162, 34,625px, raw `scrollY` drives camera interpolation), voxelo-ai (Peach framework: 4 × 1080px track sections drive WebGL scene state)

**Mechanism:** A WebGL canvas (or Framer scroll container) is pinned fixed while the page accumulates scroll distance. Scroll progress `(scrollY / maxScroll)` is mapped to a 3D timeline: camera position, model rotation, scene state, component explosion offset. At 0% progress = opening frame; at 100% = final frame. The HTML UI layer (text blocks, CTAs) is a separate DOM layer (`z-index` above canvas) that fades in/out at specific progress thresholds. Page height is the "scroll budget" — these pages run 10,000–35,000px precisely because 3D storytelling needs distance.

---

### 1.8 Minimal / Non-Standard Navigation
**Sites:** agencefoudre (two floating corner circles, no bar), phive-pt (bottom-docked slim bar), ducati (fully transparent, disappears during intro), nymphai-cosmetics (5 elements maximum, transparent), cula-tech (centered pill capsule), the-watch (no nav at all — zero-height header)

**Mechanism:** The nav is architecturally deprioritized so the hero/scroll experience reads as uninterrupted. Common treatments: `position: fixed` with `background: transparent`, minimal visible elements (logo + one CTA + hamburger at most), hiding on initial load then reappearing on first scroll, or docking to the bottom edge. The hamburger drawer is used universally on mobile — but many of these sites use it on desktop too rather than exposing inline links.

---

### 1.9 Button Hover — Text Slide / Fill-Wipe
**Sites:** no-football-colors (DOM-duplicate vertical slide: label exits up, clone enters from below), xnrgy-club (`::before`/`::after` pseudo-element fill-wipe expanding from right), cula-tech (same dual-layer slide on nav links)

**Mechanism — text slide variant:** Two identical `<span>` elements stacked inside the button with `overflow: hidden` on the outer container. On hover, CSS `translateY(-100%)` slides the top label out and pulls the bottom clone into place. Zero JS. **Mechanism — fill-wipe variant:** `::after` pseudo-element starts at `scale(0)` anchored to the right edge, transitions to `scale(1)` on hover, painting a solid background over the button from right to left. The text color swaps via a `color` transition slightly delayed so the fill arrives just before the text changes.

---

### 1.10 Glassmorphism / Frosted-Glass UI
**Sites:** apple (canonical: `backdrop-filter: saturate(1.8) blur(20px)` on `rgba(255,255,255,0.8)` nav), voxelo-ai (dark-mode variant: `rgba(14,14,11,0.55)` nav + floating annotation cards), cula-tech (pill nav with translucent fill)

**Mechanism:** `background: rgba(r,g,b,alpha)` where alpha is 0.55–0.85, combined with `backdrop-filter: blur(N px)`. The blur samples pixels behind the element from the rendered compositor layer, creating the "frosted" effect. Must add `-webkit-backdrop-filter` for Safari. Works best when the element stays positioned above content that has enough visual variety to show the frosting; flat color behind it looks identical to a solid background.

---

## 2. Unique Standouts

**phive-pt — Variable font hover (font-variation-settings)**
AcidGrotesk is a variable font (`AcidGroteskVF.woff2`). CSS transitions on `font-variation-settings` and `letter-spacing` at `0.75s cubic-bezier(0.075, 0.82, 0.165, 1)` cause letterforms to morphing in weight/width on hover without any JavaScript. The effect is almost imperceptible to casual users — it reads as "this type feels alive" — but is technically sophisticated. Worth attempting only if IA's chosen display face is variable.

**phive-pt — WebGL object bridging section transitions**
The 3D weight plate floats from the yellow typographic section into the photographic gym interior section, continuing across a full background color swap. Rather than a 3D hero centerpiece, the object is used as a visual continuity bridge. The 3D element earns its weight by doing scene-transition work that nothing else can do.

**the-watch — 3D component explode (movement teardown)**
At ~7,000px scroll depth, the watch's movement components (Dial, Tourbillon, Mainplate, Barrel, Backplate, Weight) spread apart horizontally in 3D space with labeled callouts. It's a product teardown rendered live in Three.js driven by raw `scrollY` progress — no animation library. Exceptionally high craft signal for a technical product; communicates complexity without a single word of body copy.

**nymphai-cosmetics — Inline Spline texture in typography**
A 3D-rendered cream texture (Spline canvas) is embedded between two words of a headline: "Latte [3D-texture] d'asina". The WebGL element becomes typographic punctuation within flowing text layout. Unusual and high-craft; requires a Spline asset pre-designed to fit the inline context.

**voxelo-ai — Letter-scramble / glitch-decode text reveal**
During scroll stage 2, heading text appears as corrupted/scrambled glyphs before resolving to readable copy. The glyphs act as visual noise that snaps to signal — a data-aesthetic that reinforces the AI/tech brand. Implementable with a character-swap timeout loop in JS; no library required.

**cula-tech — LED / dot-matrix brand moment mid-scroll**
The Cula logo renders as glowing dots in a dot-matrix grid at exactly the scroll position where the user has invested the most effort (after 3,500px of 3D story). Strategic placement: the brand mark appears at maximum user engagement, not at entry. Burned into memory precisely because it's earned.

**ducati — Gated experience ritual**
Mandatory video intro before any content is accessible. A "Commencer l'expérience" pill button must be clicked; the video plays before any scrollable content appears. Works only because the brand prestige (100th-anniversary limited motorcycle) justifies the friction. "Passer" (skip) is deliberately subordinate to the entry CTA. Do not import this pattern without equivalent brand equity.

**apple — Pre-rendered WebM as 3D substitute**
Product animation clips (file suffixes: `largetall.webm`, `small.webm`, `medium.webm`) replace realtime 3D. The videos look like 3D renders because they are — offline-rendered then served as lightweight autoplay-loop clips. Zero GPU runtime cost, consistent quality across all devices. The insight: users can't tell the difference between a good pre-render and live WebGL, and the pre-render is always faster.

**agencefoudre — Persistent floating client proof-point widget**
The "Case du mois" card drifts through multiple sections — it's not anchored to one scroll position but follows the user through the page. Implemented as `position: fixed` or sticky, updating its content per section. Keeps a conversion-relevant proof-point visible throughout the scroll without requiring a dedicated section.

---

## 3. Tech Stack Confirmed Across Sites

| Library / Engine | Sites | Prevalence | Notes |
|---|---|---|---|
| **Lenis** (smooth scroll) | agencefoudre, nymphai, peachweb, phive-pt, voxelo-ai, xnrgy-club | **6/12 — 50%** | Clear default for premium/editorial sites. Replaces Locomotive Scroll entirely in this cohort. |
| **Custom WebGL** (no named engine exposed) | phive-pt, peachweb, voxelo-ai, ducati | **4/12 — 33%** | Studios roll their own WebGL rather than using Three.js/R3F. Indicates Three.js is bundled but not globally exposed, or fully proprietary. |
| **Autoplay muted loop video** | apple, all-football-everything, phive-pt | **3/12 — 25%** | The easiest path to cinematic hero motion. Underused given the quality-to-cost ratio. |
| **Three.js** | the-watch (confirmed r162) | **1/12 confirmed** | The-watch is the only site with a global `window.__THREE__`. Others likely bundle it privately. |
| **Next.js** | ducati, no-football-colors, voxelo-ai | **3/12** | App Router pattern (no `window.__NEXT_DATA__` on some). |
| **GSAP** | nymphai-cosmetics (full suite) | **1/12 confirmed** | Nymphai runs all 6 plugins (ScrollTrigger, Observer, CustomEase, Flip, Draggable). Others achieve equivalent motion via CSS transitions + Lenis without GSAP. |
| **Framer** (no-code) | cula-tech | **1/12** | Full scroll-driven 3D experience, zero code — proves Framer can match complex scroll stories. |
| **Spline** | nymphai-cosmetics | **1/12 confirmed** | Used for inline-in-text 3D texture only, not a hero element. |
| **Tailwind CSS** | ducati, no-football-colors | **2/12** | Both are Next.js App Router builds. Tailwind is not universal — agencefoudre, phive-pt, the-watch, peachweb all use custom class systems. |
| **react-fast-marquee** | no-football-colors | **1/12** | `rfm-marquee` class confirmed. Viable drop-in; alternatives are pure CSS. |
| **Vanilla JS / no framework** | agencefoudre, the-watch, peachweb | **3/12** | All three are high-craft experiences built without React/Vue/Nuxt. Framework is not required for motion quality. |
| **Shopify** | nymphai-cosmetics | **1/12** | Custom theme, not a marketplace template. |
| **WordPress** | all-football-everything (2017), xnrgy-club | **2/12** | Both are content-first; neither is motion-first. |
| **Nuxt/Vue** | phive-pt | **1/12** | Only non-Next JS framework in the cohort (excluding Framer and Shopify). |

**Summary conclusion:** Lenis is the only library with genuine consensus (50% adoption). GSAP ScrollTrigger is present in one site but its effects are replicated by CSS transitions + Lenis in five others, meaning GSAP is valuable but not required for cinematic scroll. Three.js/WebGL is the differentiator for 3D hero sites but is never paired with a high-level framework like R3F — it's always bundled as a self-contained scene. Tailwind CSS appears in exactly the sites that use Next.js App Router; correlation is near-perfect.

---

## 4. Recommendation for the Impactors Academy + IA Pro Build

**Our actual stack:** Next.js App Router + React Three Fiber + GSAP ScrollTrigger + Framer Motion + Tailwind CSS, self-hosted on Coolify. Must perform on mobile and lower-end devices. Timeline and team are lean.

The patterns below are sorted: **Build** (realistic, high value), **Defer** (valuable but scoped/risky), **Skip** (impressive elsewhere, wrong for IA).

---

### BUILD: Lenis smooth scroll
Lenis is the single most-adopted pattern in this cohort and costs almost nothing to add. Wire it to GSAP's ticker via `gsap.ticker.add(() => lenis.raf())` so ScrollTrigger reads the Lenis-smoothed scroll position. This is the baseline that makes everything else feel more premium.
**Skill:** `/gsap-scrolltrigger`

---

### BUILD: Section-per-color-world
Distinct background colors per major section — done right this gives the scroll a chapter structure with zero additional assets. Use ScrollTrigger `onEnter`/`onLeave` to toggle CSS custom properties on the `<body>` or section element. Three to four zones maximum (e.g. dark hero → light content → dark CTA → accent section). Mobile-safe; pure CSS change.
**Skill:** `/gsap-scrolltrigger` for trigger logic; `/ui-ux-pro-max` for palette decisions (the accent color must be confirmed before committing — see the placeholder note in design direction memory).

---

### BUILD: Clip-path reveal for text and content blocks
The cleanest scroll-entrance technique in the cohort — a clipping mask expands to reveal content without any "jumping" positional shift. Implementation: `clip-path: inset(0 100% 0 0)` → `clip-path: inset(0 0% 0 0)` as a GSAP `fromTo` tween triggered by `ScrollTrigger.create()` with `start: "top 80%"`. Works on all devices; pure GPU-accelerated CSS property.
**Skill:** `/gsap-scrolltrigger`

---

### BUILD: Display type at viewport scale
Zero runtime cost — this is a CSS/HTML decision. Size key headlines to `clamp(4rem, 12vw, 14rem)` and let them fill or overflow at the viewport edge. The effect is immediate and device-consistent. Keep it to one or two moments in the page (the hero H1 and possibly one interior "statement" section). Don't apply to more than 3 headings or the impact dilutes.
**Skill:** `/ui-ux-pro-max` for selecting which font can hold up at this scale; `/gsap-scrolltrigger` if adding a split-text entrance.

---

### BUILD: Split-text character entrance animations
GSAP's SplitText plugin (available with a Club GreenSock license, or use a lightweight custom implementation that splits on `innerHTML`) staggers each character's entry. Use expo-out easing (`power4.out` in GSAP terms). Budget ~2 headings per page — overuse kills the effect. Safe on mobile: the animation is opacity + translateY, which is GPU-composited.
**Skill:** `/gsap-scrolltrigger`

---

### BUILD: Horizontal marquee / ticker
A single piece of repeated content (e.g. "Impactors Academy · Impact Starts Here · ") looped continuously makes an excellent visual separator and brand moment between content sections. Use `react-fast-marquee` (npm, no-football-colors confirms it; `rfm-marquee-container` class) or a pure CSS `animation: marquee linear infinite` approach. Pause on hover is one CSS property.
**Skill:** `/animated-component-libraries` (likely has a ready marquee component)

---

### BUILD: Button hover — text slide (ticket-flip)
The DOM-duplicate text-slide hover is a pure CSS implementation that rewards close attention without being flashy. Two `<span>` elements inside a button, `overflow: hidden` container, `translateY` transition on hover. Cost: ~10 lines of Tailwind/CSS. Applies to every primary CTA on the site.
**Skill:** `/motion-framer` (Framer Motion `AnimatePresence` can do the swap cleanly in React) or `/animated-component-libraries`

---

### BUILD: Glassmorphism nav
`backdrop-filter: blur(16px)` on a `rgba(255,255,255,0.75)` (light mode) or `rgba(10,10,10,0.65)` (dark mode) nav background. Add `-webkit-backdrop-filter` for Safari. This is the most recognized premium-web visual signal in the cohort (Apple, Voxelo, Cula all use it). Performs fine on mobile — it's a CSS compositor operation.
**Skill:** `/ui-ux-pro-max` for color values; `/senior-frontend` for the CSS implementation

---

### BUILD (selective): Looping video as hero background
For the IA Pro hero specifically, a well-produced autoplay WebM (15–30s, muted, loop) showing the platform in motion would deliver cinematic quality at near-zero GPU cost versus a live Three.js scene. Apple's approach: pre-render offline, serve from CDN, let the browser play it. This is the right mobile strategy for any 3D-feeling hero that must work on a 2019 iPhone. Serve WebM with MP4 fallback. Suppress the `<video>` on `prefers-reduced-motion`.
**Skill:** No installed skill maps to video production/export. Flag as a production asset task, not a code task. Once the video file exists, the implementation is 20 lines of HTML + a few Tailwind classes.

---

### DEFER: Scroll-linked R3F pinned scene
React Three Fiber + GSAP ScrollTrigger can implement the cula-tech or the-watch camera-orbit pattern. The architecture: one pinned `<Canvas>` section, `ScrollTrigger.create({ pin: true, scrub: 1 })`, and a `useFrame()` hook that lerps camera/object transforms toward scroll-progress targets. Start with one simple interaction: a single 3D object (logo or course card mockup) that rotates as you scroll through the hero. Expand only if perf budget holds on mid-range Android.

**Risk:** Full-viewport R3F on mid-range mobile is a real GPU budget concern. If building this, cap canvas at 60% viewport max-height on desktop and swap to a static image below 768px until perf validation is done. Build the static fallback first.
**Skill:** `/react-three-fiber` for the scene; `/gsap-scrolltrigger` for the pin/scrub wiring; `/threejs-webgl` if building a custom shader for the material.

---

### DEFER: GSAP ScrollTrigger pinned product/course showcase
Nymphai's pinned product theater (pin + horizontal-slide + progress bar + counter) is the most polished "browse multiple items without leaving the section" pattern in the cohort. For IA, this would mean: pin a "courses" section, scroll drives the active course from 01/N → N/N, each course slides into view horizontally. Scope it as a stretch feature for Phase 2 if the MVP is shipping cleanly. The GSAP implementation is proven; the design work (3 course slides at matching visual weight) is the real effort.
**Skill:** `/gsap-scrolltrigger`

---

### SKIP: Custom WebGL engine
phive-pt, peachweb, and voxelo-ai all rolled proprietary WebGL. We have React Three Fiber, which is more capable than any of those custom engines and maps to our stack. Don't replicate the custom engine pattern — use R3F instead if 3D is needed.

---

### SKIP: Mandatory gated experience / video intro
Ducati's gated ritual works because the product is a €100k+ limited motorcycle. IA's goal is enrollments, not exclusivity theater. Friction at the entry point kills conversion rates for educational platforms. Skip entirely.

---

### SKIP: Custom cursor
Three sites (nymphai, xnrgy-club, the-watch) use a custom cursor overlay. On any touch device (50%+ of web traffic) it's completely invisible. The implementation adds DOM complexity and `mousemove` event load for zero mobile benefit. The craft signal it provides is not worth the maintenance cost for IA.

---

### SKIP: Variable font hover (font-variation-settings)
phive-pt's AcidGrotesk hover morphing is compelling but depends entirely on having a variable font with useful axes. Unless IA's chosen display typeface (currently Playfair Display, which has limited variable axes) supports meaningful weight/width variation on hover, this technique has no implementation path. Don't select a font based on this technique alone.

---

### SKIP: Inline Spline texture in typography (nymphai pattern)
High-craft but requires Spline design work, adds a WebGL context per usage, and serves a very specific luxury-editorial aesthetic. Not proportionate for an educational platform's content sections.

---

### SKIP: Glyph-scramble / glitch-decode text (voxelo-ai)
The data-glitch aesthetic fits AI/tech brands (Voxelo's product is AI-generated product photography). It would read as out-of-tone for IA's "transformational education" positioning. Skip unless the brand direction explicitly calls for a tech-forward identity layer.

---

### Easing constants to adopt (from the cohort)

These specific curves appeared repeatedly across high-quality sites and are worth naming as design system constants:

| Name | Curve | Used by | Character |
|---|---|---|---|
| `expo-out` | `cubic-bezier(0.19, 1, 0.22, 1)` | phive-pt (all hover + entrance) | Fast departure, very slow land. Physical, snappy. |
| `spring-back` | `cubic-bezier(0.17, 0.67, 0.3, 1.33)` | agencefoudre (hover) | Overshoot + settle. Bouncy, energetic. |
| `smooth-out` | `cubic-bezier(0.23, 1, 0.32, 1)` | agencefoudre (clip-path reveals) | Clean reveal. Slightly softer than expo-out. |
| `clip-out` | `cubic-bezier(0.86, 0, 0.07, 1)` | agencefoudre (heavy elements) | Symmetric in-out expo. Deliberate, weighty. |

In GSAP terms: `expo-out` ≈ `power4.out`; `spring-back` has no direct GSAP equivalent — implement as a CSS transition on the element while GSAP handles position/opacity separately.
