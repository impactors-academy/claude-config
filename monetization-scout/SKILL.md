---
name: monetization-scout
description: "This skill should be used when the user wants to find and rank real, currently-operating monetization opportunities for a given topic, niche, product, or audience — affiliate programs, UGC/creator deals, sponsorships, brand-partner programs, and ebook/course marketplaces. It searches the field, ranks candidates two ways (market leadership vs. best payout), and returns for each one either a direct application link or, when no public signup exists, verified contact details (email prioritized) to reach out through. Use when the user mentions 'find affiliate programs for X', 'who sponsors X content', 'monetization opportunities in [niche]', 'partner programs for [topic]', 'who pays the most for [niche] UGC', 'ebook/course platforms for [topic]', or similar. Distinct from pricing-strategy (pricing a product we own) and referral-program (designing a program we run) — this skill finds external programs to join, not ones to build. Hands off to prospecting-outreach for the actual first-touch contact."
license: MIT
metadata:
  version: 1.0.0
  category: commercial
  updated: 2026-08-15
---

# Monetization Scout

Finds and ranks real monetization opportunities for a specific topic or niche
— not generic advice about "how affiliate marketing works," but an actual
list of programs worth applying to, sourced live.

## When this fires

- "Find affiliate programs for [topic/niche/product category]"
- "Who sponsors [type of] content / who pays for UGC in [niche]"
- "What partner/reseller programs exist for [tool category]"
- "Where can we sell/license an ebook or course about [topic]"
- "Monetization opportunities for [platform/audience]" — run every
  monetization type unless the user narrows it

Not for: pricing our own product (`pricing-strategy`), designing a program we
run for others to join (`referral-program`), or reviewing an inbound partner
proposal (`partnerships-architect`). If the ask is any of those, say so and
redirect rather than running the search anyway.

## Workflow

1. **Confirm scope.** Topic/niche (required), and which monetization types to
   search — affiliate, UGC/creator, sponsorship, partner/reseller,
   ebook/course marketplace, or all. If the user didn't say, ask once; don't
   default silently to "all" on a broad topic where that means 40+ searches.

2. **Search per type**, using the query patterns and leader/payout signals in
   `references/rubric.md` — read it before the first search, it has the
   specific things to look for per category so the results are actually
   comparable to each other, not five random lists in five different shapes.

3. **Verify before including anything.** A candidate only makes the list if
   its program page (or a recent, dated source) actually confirms it's live
   right now. Note the check date. A defunct or "coming soon" program does
   not belong in a list someone is about to spend time applying to.

4. **Get the application path.** For each candidate, find one of:
   - A direct affiliate/partner/creator-program signup URL — link it.
   - If no public signup exists: a real contact, **email prioritized** over
     a contact form or a generic "Contact us" link. Check the site's
     press/partnerships/team pages and LinkedIn for the right role
     (partnerships, marketing, business development — not a generic
     support inbox) before falling back to a contact form.
   - **Never fabricate an email.** A pattern-guessed address
     (`firstname@company.com` inferred from a naming convention) must be
     labeled `(inferred, unverified)` in the output, never presented as
     confirmed. If nothing real can be found, say so — an honest "no public
     contact found" is more useful than a guess dressed as a fact.

5. **Rank two ways, separately** — they are usually different lists:
   - **Leaders**: market position/reach/reputation in this specific niche
     (not overall company size — a mid-size player can be the leader in a
     narrow niche).
   - **Best payout**: commission %, flat CPA, revenue share, or sponsorship
     rate, whichever the program actually publishes. Where a program doesn't
     publish rates, say so rather than omitting the row silently — "rates
     not published, apply to find out" is itself useful information.

6. **Output as one table per monetization type requested:**

   | Program | Category | Why it's a leader here | Payout | Apply link / Contact |
   |---|---|---|---|---|

   Follow each table with a one-line note on anything that couldn't be
   verified, and the date the search was run (programs and rates change).

## Guardrails

- Real, dated, sourced information only — no reciting "affiliate programs
  typically pay 5-30%" as if it answered the question. Go find the actual
  ones.
- If a search comes back thin (a genuinely niche topic), say so plainly
  rather than padding the list with loosely-related programs to look
  thorough.
- This skill finds the opportunity and the contact path. It does not draft
  the outreach message or place a call — hand off to `prospecting-outreach`
  for that next step.
