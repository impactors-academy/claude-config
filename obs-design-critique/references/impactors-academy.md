# Impactors Academy — critique context

## Brand

```
Copper  #C9885C   on   Black #030303      — all platforms
Light surfaces: #8B4E22, NEVER #C9885C (2.51:1 on cream — fails WCAG)
```

Full palette and WCAG ratios: `/color-combinations` →
`references/impactors-academy.md`. That skill is the single entry point for
every colour decision org-wide — do not eyeball a hex in a critique.

The palette is **sampled from the logo** and locked. A critique that proposes a
new brand colour is proposing a change to a locked org standard: say so
explicitly rather than slipping it in as a suggestion.

## Surfaces

| Project | Type | Critique emphasis |
|---|---|---|
| impactors-academy | Marketing site, LAUNCHED | Hierarchy above the fold, 3D perf on real devices (open checklist item) |
| ia-pro | Marketing + internal tool | Two audiences, two standards — do not critique the admin surface by marketing criteria |
| loc | Marketing + admin CMS | Public pages are conversion surfaces; `/admin` is an internal tool where density beats polish |
| prospectbuddy | Internal tool | Density and speed over aesthetics |
| grindbuddy | PAUSED | — |

**Internal tools and marketing pages fail differently.** A dense admin table
with small type is correct in a CMS and wrong on a landing page. Establish which
you are looking at before the first pass.

## Baselines that are pass/fail, not taste

From MASTER-CHECKLIST Phase 0D — these are org requirements, so they belong in
the **blocking** tier of any critique:

```
WCAG 2.1 AA · keyboard navigation · prefers-reduced-motion respected
LCP < 2.5s · CLS < 0.1 · Lighthouse ≥ 90
```

## Related

- `/color-combinations` — every colour decision, first
- `/minimalist` — the restraint pass, deeper
- `/ui-ux-pro-max` — design decisions rather than review
- `/a11y-audit` — when the accessibility pass needs to be exhaustive
- `~/.claude/skills/site-studies/SYNTHESIS.md` §4 — motion reference before any motion critique
