# Site Study: No Football Colors (NOFC)
**URL:** https://nofootballcolors.com/  
**Study date:** 2026-07-18  
**Slug:** no-football-colors  

---

## 1. Navigation & First Impression

**→ Screenshot:** `screenshots/01-hero-desktop.png`

The site immediately redirects to `/fr` (French locale). The first thing the eye hits is a large-format editorial hero: a full-bleed image with a "Issue N°2" magazine-style label, an oversized H1 headline in Obviously Narrow, and a bordered CTA button. The layout reads as a magazine front cover, not a typical landing page.

**Nav pattern:** Fixed, transparent over the hero. Logo anchored left, three nav links centered (shop, editorial section, about), and a language switcher + icon button on the right. On scroll-down the header transitions to a white background (via a hidden `<div>` with `-translate-y-full` that slides in). On mobile, the nav becomes a full-width slide-down white drawer triggered by a toggle button.

---

## 2. Hero Section

**→ Screenshot:** `screenshots/01-hero-desktop.png`

No 3D element. No `<canvas>`, no WebGL, `window.THREE` absent.

The hero is a large linked card spanning most of the viewport: editorial image left (or full-bleed), text block with "Issue" number label, H1, author attribution, and a CTA button. The CTA button is notable — it contains an embedded **Lottie animation** (a football/soccer ball SVG rendered with `content-visibility: visible` and `transform: translate3d(0,0,0)`) bundled inside the Next.js JS chunks. The ball animates on idle or interaction.

The hero card is wrapped in an `<a>` tag (the whole card is the link), with the CTA button acting as a visual affordance rather than the actual click target.

No entrance animation observable via static CSS inspection — transitions are likely handled in React component state on mount.

---

## 3. Scroll Behavior

**→ Screenshots:** `screenshots/03-scroll-stage-1.png` through `screenshots/03-scroll-stage-5.png`

**Scroll type:** Native browser scroll. No Lenis, no Locomotive Scroll, no GSAP ScrollTrigger detected on `window`. Page height is ~6022px desktop.

**Page sections in scroll order:**

- **Stage 1 (~1200px):** Shop/collection section — full-bleed cover image with collection name overlay and a "DISCOVER" bordered CTA button (same double-text animation pattern as hero). Alongside: brand tagline in two lines of large type, plus two article cards in a side-by-side grid.
- **Stage 2 (~2400px):** Brand manifesto section — large H2 heading, body copy, "Notre vision" CTA link. Below it: a "Play video" button with a static cover image. Clicking would open a modal (no `<video>` element in DOM until triggered).
- **Stage 3 (~3600px):** Infinite marquee banner — the "No. Clubs. No Colors. No games." phrase repeats in an autoscrolling horizontal ticker. Built with **react-fast-marquee** (`rfm-marquee-container` / `rfm-marquee` classes). The `--pause-on-hover` CSS variable pauses it on hover.
- **Stage 4 (~4800px):** A second marquee row running in the opposite direction (mirrored speed), giving a two-lane counter-scroll effect.
- **Stage 5 (bottom):** Footer — newsletter subscription form with email input, contact link, social icons (Instagram, X, TikTok). Legal links and copyright row below separator.

No pinned sections, no horizontal scroll hijacking, no scroll-linked 3D camera movement.

---

## 4. Micro-Interactions

**No custom cursor.** All `cursor-pointer` instances are standard CSS — no `.cursor-follower` or custom cursor element found.

**Button hover — text slide animation:** CTA buttons carry a DOM structure with the label text duplicated three times across nested flex containers. On hover, CSS transform animates the visible text upward (out) and the duplicate slides in from below — a vertical marquee/ticket-flip effect. This is pure CSS using `overflow: hidden` on the outer container plus `transition` on the inner text rows. The `group` Tailwind class on the button enables `group-hover:` utilities on children.

**Link hover underline:** A `.link-hover-line` class is used on text links to reveal an underline via a pseudo-element or `transform: scaleX()` transition.

**Marquee pause on hover:** The `rfm-marquee-container` respects `--pause-on-hover: paused`, which freezes the scrolling ticker when the user hovers over it.

**`kickFloat` keyframe:** Defined as `opacity: 1 → 0` with `translateY(0 → -50px)`, center-anchored. Used for a feedback element (likely an add-to-cart notification bubble that floats up and fades out).

**Cart button:** Small icon-only button in the nav. Likely opens a slide-in cart drawer.

---

## 5. Typography & Color

### Type scale
| Level | Font | Size (desktop) | Size (mobile) | Weight | Notes |
|---|---|---|---|---|---|
| H1 | Obviously Narrow | 120px | 64px | 500 | Clean condensed grotesque |
| H2 | Obviously Narrow | 64px | 40px | 500 | Same face, scaled down |
| Body | Polymath Text | 16px | 16px | 400 | Custom editorial serif/text face |
| UI labels | Obviously Narrow | varies | varies | 500 | `!text-obviously` Tailwind token |

The html root carries `class="font-polymath"`, making Polymath Text the default document font. Obviously Narrow is the display/heading override applied via Tailwind `font-obviously` tokens.

### Palette
| Role | CSS Variable | Approximate value | Notes |
|---|---|---|---|
| Background | `--background` | `#FFFFFF` (pure white) | `lab(100% 0 0)` |
| Text / Foreground | `--foreground` | `#050505` (near-black) | `lab(2.75%)` |
| Primary | `--primary` | `#111111` (near-black) | `lab(7.78%)` |
| Secondary / Accent / Muted | `--secondary` / `--accent` | `#F5F5F5` (near-white) | `lab(96.52%)` — same value |
| Muted foreground | `--muted-foreground` | ≈ medium gray | `lab(48.5%)` |
| Border | `--border` | Light gray | `lab(90.95%)` |

**No accent color at all.** The entire UI is executed in black, white, and grays — a deliberate expression of the brand name "No Colors." Color comes only from editorial photography.

Colors are defined in CSS `lab()` color space (CSS Color Level 4), not hex or hsl — a modern and precise approach.

---

## 6. Tech Fingerprint

| Technology | Status | Evidence |
|---|---|---|
| Next.js (App Router) | **Confirmed** | `_next/static/chunks/` script paths; Turbopack build (`turbopack-*.js`) |
| Vercel hosting | **Confirmed** | `_vercel/insights/script.js`, `_vercel/speed-insights/script.js` |
| Tailwind CSS | **Confirmed** | Utility class patterns: `flex`, `items-center`, `pb-[2px]`, `rounded-none`, `text-nowrap`, `border-2`, etc. |
| react-fast-marquee | **Confirmed** | `rfm-marquee-container` and `rfm-marquee` class names; `--pause-on-hover` CSS variable |
| Lottie (bundled) | **Confirmed** | SVG with `content-visibility: visible` and `transform: translate3d` inside button; bundled into Next.js chunks |
| Cloudflare Turnstile | **Confirmed** | `challenges.cloudflare.com/turnstile/v0/api.js` script |
| tarteaucitron.js | **Confirmed** | French cookie consent library — `tarteaucitron.min.js` |
| Google Analytics GA4 | **Confirmed** | `gtag/js?id=G-8YJ4ECT2RV` |
| CSS lab() color space | **Confirmed** | All color tokens use `lab()` syntax |
| GSAP | **Not found** | — |
| Framer Motion | **Not found** | No `data-framer-*` attributes |
| Lenis / Locomotive Scroll | **Not found** | — |
| Three.js / WebGL | **Not found** | No canvas, no THREE on window |
| React (standalone) | **Inferred** | Part of Next.js stack; not separately exposed on `window` |

---

## 7. Mobile Pass

**→ Screenshots:** `screenshots/07-mobile-hero.png`, `screenshots/07-mobile-section.png`  
**Viewport tested:** 390×844 (iPhone 14 Pro)

**Nav:** Fixed transparent header collapses to logo + two icon buttons (language toggle + cart). A third button triggers a full-width slide-down white drawer (`-translate-y-full` → `translate-y-0`) containing the navigation links.

**Typography scaling:**
- H1: 120px → 64px
- H2: 64px → 40px  
- Body: 16px unchanged

**Layout changes:** Page height compresses from ~6022px to ~4638px. The two-column article card grid collapses to a single-column vertical stack. The collection section stacks text below image. The two marquee rows remain — they scale gracefully on narrow viewports.

**What's simplified:** Multi-column grids become single-column. The editorial header with centered nav is replaced by a minimal bar. The Lottie button may be hidden or simplified on touch.

**What's preserved:** All content sections present; marquee tickers; editorial photography at full bleed; brand typography hierarchy intact.
