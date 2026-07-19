# Site Studies — UI/UX Reference Library

A curated collection of deep UI/UX/motion audits of reference websites, plus a
synthesized recommendation document. Use this as design calibration context before
building any new page, section, or component.

## What's in here

- **`SYNTHESIS.md`** — Cross-site synthesis: recurring patterns, unique standouts,
  tech stack rollup, and build recommendations for the Impactors Academy stack
  (Next.js + R3F + GSAP ScrollTrigger + Framer Motion + Tailwind).
- **`{slug}/findings.md`** — Per-site deep audits covering nav, hero, scroll
  behavior, micro-interactions, typography, color, tech fingerprint, and mobile pass.

## Sites studied (2026-07-18)

| Slug | Type | Key patterns |
|---|---|---|
| agencefoudre | Social media agency | Section-per-color, clip-path reveals, Lenis, two-corner floating nav |
| all-football-everything | Nike campaign (archived 2017) | Chapter scroll narrative, looping video, cultural motto as hero |
| apple | Product landing | Pre-rendered video-as-3D, frosted-glass nav, tile grid |
| cula-tech | B2B SaaS (Framer) | Scroll-driven 3D story (pre-rendered), pill nav, LED brand moment |
| ducati-superleggera-v4-centenario | Luxury product microsite | Canvas scrollytelling, gated entry ritual, chromatic restraint |
| no-football-colors | Fashion editorial | Marquee ticker, ticket-flip button, Lottie CTA, no accent color |
| nymphai-cosmetics | Luxury skincare (Shopify) | GSAP ScrollTrigger pin, Lenis, Spline inline in text, custom cursor |
| peachweb | WebGL builder | Continuous 3D world as scroll path (sky→underwater), Lenis |
| phive-pt | Fitness club (Nuxt) | Bottom-docked nav, variable font hover, WebGL object bridging sections |
| primal-training-club | Fitness (EXPIRED) | Domain dead — skip |
| the-watch | Luxury watch (Three.js) | Three.js r162, 34,625px scroll budget, component explode, no nav |
| voxelo-ai | AI SaaS (Next.js) | Custom WebGL "Peach" framework, Lenis, glitch-decode text |
| xnrgy-club | Padel/fitness club (WP) | 187px Helvetica hero, Lenis, split-text entrance, custom cursor |

## How to use

When starting any design or build task, read `SYNTHESIS.md` Section 4
(Recommendations) to identify which patterns apply. Reference individual
`{slug}/findings.md` if you need the mechanism detail for a specific technique.

## How to add a new study

Run `/user:study-site-step1 <URL>` in the target project. After all sites are
studied, run `/user:study-site-step2` to regenerate the synthesis, then copy the
updated `SYNTHESIS.md` and new `{slug}/findings.md` files back here and commit.
