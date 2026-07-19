# Reference Site Study — Prompt for Claude Code (via Playwright MCP)

Run once per site, or paste the whole reference list and let it work through them in
sequence. Requires `@playwright/mcp` installed first (`claude mcp add playwright npx
@playwright/mcp@latest`).

---

## The prompt

```
Using Playwright MCP, study this site from top to bottom for its UI/UX, motion, and
(where present) 3D design: [URL]

FIRST: derive a slug from the site (e.g. "voxelo-ai" for voxelo.ai, "the-watch" for
thewatch.60fps.fr) and create this folder structure before doing anything else:

docs/site-studies/[slug]/
docs/site-studies/[slug]/screenshots/

All screenshots from this study go in the screenshots/ subfolder, named by section
(e.g. 01-hero-desktop.png, 02-hero-mobile.png, 03-scroll-stage-1.png, etc.). The
written findings go in docs/site-studies/[slug]/findings.md — not printed only in
the terminal, not left in the default screenshot location.

Go through it in this order:

1. NAVIGATION & FIRST IMPRESSION
   - Screenshot the initial viewport (desktop, 1440x900) → screenshots/01-hero-desktop.png
   - What's the very first thing the eye is drawn to?
   - Nav pattern: sticky/hidden-on-scroll/hamburger/full-bleed?

2. HERO SECTION
   - Screenshot it (reuse 01-hero-desktop.png if the same view)
   - Is there a 3D element? If so, run window.THREE, check for a canvas element, and
     inspect script tags/network requests to identify the engine (Three.js, Spline
     runtime, Babylon, etc.)
   - Describe the entrance animation, if any (fade/wipe/particle assemble/etc.)

3. SCROLL BEHAVIOR
   - Scroll in 4-5 stages through the full page, screenshotting each stage to
     screenshots/03-scroll-stage-N.png
   - Note: is scroll native or hijacked/smoothed (check for Lenis, Locomotive Scroll,
     GSAP ScrollTrigger via window.gsap and window.ScrollTrigger)?
   - Note any scroll-linked animation: parallax, pinned sections, horizontal scroll
     hijacking, camera movement if 3D is present

4. MICRO-INTERACTIONS
   - Hover states on buttons/links/cards — describe the transition (scale/color/
     magnetic cursor-follow/etc.)
   - Cursor customization — is there a custom cursor? Does it react to hoverable
     elements?

5. TYPOGRAPHY & COLOR
   - Identify the type scale (rough sizes for h1/h2/body)
   - Identify the core palette (background/text/accent) — approximate hex if visible
     via computed styles

6. TECH FINGERPRINT
   - Check window object and script/link tags for: React/Next.js, GSAP, Framer Motion,
     Three.js/react-three-fiber, Lenis/Locomotive Scroll, Tailwind (via class name
     patterns)
   - List what you find with confidence level (confirmed vs. inferred)

7. MOBILE PASS
   - Reload at 390x844 (iPhone viewport), screenshot hero and one more section to
     screenshots/07-mobile-hero.png and screenshots/07-mobile-section.png
   - Note what's simplified or removed for mobile

Write the full structured write-up (all 7 sections, referencing the screenshot
filenames inline where relevant) to docs/site-studies/[slug]/findings.md. Do not copy
any actual copy/text content from the site verbatim — describe patterns and
techniques only, not the site's actual words or image assets.
```

Result after running this once per site: one self-contained folder per site, e.g.

```
docs/site-studies/
├── voxelo-ai/
│   ├── findings.md
│   └── screenshots/
│       ├── 01-hero-desktop.png
│       ├── 03-scroll-stage-1.png
│       └── 07-mobile-hero.png
├── the-watch/
│   ├── findings.md
│   └── screenshots/
└── agencefoudre/
    ├── findings.md
    └── screenshots/
```

---

## After all sites are done

Once every site has its own `docs/site-studies/[slug]/findings.md`, run
`/study-site-step2` (separate command) to synthesize all of them into one summary.

---

## One standing rule worth keeping in the CLAUDE.md for this project

Study technique, never copy asset or copy. The output of this exercise should be
"they use X pattern for Y effect," never a reproduction of their actual layout, imagery,
or text — same IP boundary as before, just enforced automatically at the tool level now
that Claude Code can actually see these sites rendered.
