---
name: obs-design-critique
description: "Structured observational critique of a UI or page — visual hierarchy, spacing, typography, restraint and brand fit — for Impactors Academy surfaces. Use when reviewing a page or component someone has built, deciding why a design feels off, cutting visual noise, checking hierarchy before launch, or getting a second opinion on a layout. Triggers: 'critique this', 'review this design', 'does this look right', 'something feels off', 'too busy', 'visual hierarchy', 'design review', 'is this on brand', 'make it cleaner'."
---

# Design critique — observational

A critique is a **description of what you observe, then a judgement about
whether it serves the goal.** Not a list of preferences.

Org palette, type and the surfaces this applies to:
`references/impactors-academy.md`.

---

## Observe before judging

The order matters. Judgement offered before observation is taste; judgement
after observation is critique.

```
1. Squint. What do you see first, second, third?
2. Is that the order the page NEEDS?
3. Only then: what change would fix the order?
```

If the first thing you see is not the thing the page is for, nothing else in the
critique matters yet. Fix the hierarchy before discussing the border radius.

---

## The passes, in order

Work down. Do not start at colour — it is the most visible layer and the least
often the actual problem.

### 1. Hierarchy

- What is first, second, third by visual weight? Does it match the page's job?
- Is there exactly **one** primary action in view? Two primaries is zero.
- Is anything competing purely through size or saturation rather than importance?

### 2. Spacing and rhythm

- Is spacing on a consistent scale, or ad hoc per component?
- Is related content grouped closer than unrelated content? (Proximity does more
  work than any border or divider.)
- Is whitespace being treated as waste? It is the cheapest hierarchy tool there is.
- Does the vertical rhythm survive at 320px and at 1920px?

### 3. Typography

- How many sizes and weights are in play? More than 4–5 sizes is usually drift.
- Is line length in the 45–75 character range for body copy?
- Is line height loose enough at small sizes and tight enough at display sizes?
- Is emphasis achieved by weight and size, or by piling on colour, italics,
  underline and caps at once?

### 4. Colour

Any colour decision goes through **`/color-combinations` first** — it is the
single entry point for colour, org-wide.

- Is colour carrying meaning, or decoration? Decorative colour dilutes the
  meaningful kind.
- Does the accent appear rarely enough to still read as an accent?
- **Contrast is a pass/fail, not an opinion.** Check the ratio.
  On light surfaces use `#8B4E22` — never `#C9885C` (2.51:1 on cream, fails).

### 5. Restraint

The subtractive pass, and the one most often skipped:

- What can be **removed** without loss? Remove it.
- Are there borders doing a job that spacing already does?
- Are there shadows, gradients and animation stacked on the same element?
- Does every icon earn its place, or are some decorating a label that was
  already clear?

### 6. Motion

- Does motion clarify a relationship, or perform?
- Does it respect `prefers-reduced-motion`?
- Would the page still make sense with motion off? It must.

### 7. State and edge cases

The pass that separates a mockup from a design:

- Empty, loading, error, and "one item" as well as "fifty items"
- Long strings: a 60-character name, a missing image, a null field
- Keyboard focus visible on every interactive element
- Touch targets ≥ 44px

---

## Delivering the critique

Be specific and falsifiable. "Feels cluttered" is not actionable; "there are six
competing weights above the fold, and the CTA is the fourth thing you see" is.

For each point: **observation → why it matters → the smallest change that fixes it.**

Separate the tiers explicitly, because they are not equally urgent:

- **Blocking** — fails accessibility, breaks hierarchy, breaks at a real viewport
- **Should fix** — real friction, not a launch blocker
- **Taste** — say so plainly, and hold it lightly

**Say what works and why.** A critique that only lists faults gives no signal
about what to preserve in the next revision, and gets ignored.

---

## Never do this

- Never open with colour. It is rarely the real problem and it derails the rest.
- Never critique from the code alone — look at the rendered page, at more than
  one viewport. Use `/run` or the Chrome tools.
- Never give a preference the authority of a rule. Say which it is.
- Never rewrite the design in the critique. Name the problem; leave the solution
  space open unless asked.
- Never skip the states pass. Most design failures in production are empty,
  loading, or long-string failures — not aesthetic ones.
