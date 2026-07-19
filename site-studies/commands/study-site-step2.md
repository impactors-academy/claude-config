# study-site-step2

Run this only after `study-site-step1` has been run against every reference site on
the list, and each write-up has been saved to disk at
`docs/site-studies/[slug]/findings.md` (one folder per site, per site's own
screenshots/ subfolder alongside it).

---

## Prompt

```
Read every file matching docs/site-studies/*/findings.md — these are individual
UI/UX/motion audits of reference sites, produced by study-site-step1, one per
site-slug folder (each folder also contains that site's screenshots/ subfolder,
which you can reference but don't need to re-view unless a finding is unclear from
the text alone).

Synthesize them into one summary document with these sections:

1. RECURRING PATTERNS
   Which specific techniques (scroll behavior, hero treatment, micro-interactions,
   tech choices) show up across multiple sites? For each, name it, note which sites
   used it, and describe the mechanism (not just "it looked cool" — the actual
   how: e.g. "GSAP ScrollTrigger pins the hero and scrubs a Three.js camera dolly
   0-100% over the first viewport height").

2. UNIQUE STANDOUTS
   Techniques that appeared on only one site but are strong enough to be worth
   considering anyway. Name the site, the technique, and why it stood out.

3. TECH STACK CONFIRMED ACROSS SITES
   A rollup of which libraries/engines showed up repeatedly (Three.js/R3F, GSAP,
   Framer Motion, Lenis, etc.) — this tells us what's actually proven and common
   practice vs. niche.

4. RECOMMENDATION FOR THE IMPACTORS ACADEMY + IA PRO BUILD
   Given our actual stack (Next.js + React Three Fiber + GSAP ScrollTrigger + Framer
   Motion, self-hosted on Coolify, must perform on mobile/lower-end devices) —
   which patterns from sections 1-2 are realistic to build, which are too costly or
   risky for our timeline/team size, and which should we deliberately skip even
   though they looked impressive on the reference site.

   For each recommended pattern, name the specific installed skill that should
   implement it: `/react-three-fiber` and `/threejs-webgl` for any 3D-hero pattern,
   `/gsap-scrolltrigger` for scroll-linked motion, `/motion-framer` for
   micro-interactions/hover states, `/21st-dev` or `/animated-component-libraries`
   for any component-level pattern that has a pre-built equivalent worth starting
   from, `/ui-ux-pro-max` for any palette/style-level observation. If a recurring
   pattern doesn't map to any installed skill, say so explicitly rather than
   forcing a fit.

Save this as docs/site-studies/SYNTHESIS.md (at the top level of site-studies/, not
inside any individual site folder). Do not reproduce any copy, imagery, or literal
layout from the source sites — this is a technique summary, not a copy.
```

---

## After this runs

`docs/site-studies/SYNTHESIS.md` is what should replace the vague "calibrate against
these reference sites" line in the website build prompt (Phase 2 / Phase 4) — swap
in the actual named techniques from section 4 instead of a general instruction to
"look at these sites."
