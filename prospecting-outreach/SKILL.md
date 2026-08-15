---
name: prospecting-outreach
description: "This skill should be used when the user wants to actually get in touch with a specific person, company, or list of leads — finding verified contact details (email prioritized over contact forms or DMs), picking the right outreach channel and tool for the volume and urgency involved, and producing the first-touch message. Use when the user mentions 'find their contact', 'who do I email at X', 'prospect this list', 'reach out to X', 'cold call script', 'outreach tool', 'dialer', or hands over a list of companies/programs to contact (including output from monetization-scout). Complements cold-email, which owns the actual email copywriting craft — this skill is the step before and around it: contact discovery, channel choice, tool recommendation, and handing the copy pass to cold-email rather than duplicating it."
license: MIT
metadata:
  version: 1.0.0
  category: commercial
  updated: 2026-08-15
---

# Prospecting & Outreach

Turns a name, a company, or a list (e.g. from `monetization-scout`) into an
actual first contact — the discovery-and-dispatch layer around outreach, not
the copywriting itself.

## When this fires

- "Find the right contact at [company]"
- "Who do I email about [partnership/sponsorship/affiliate application]"
- "Help me reach out to this list" / "prospect these leads"
- "What should I use to cold call / send outreach at volume"
- Any handoff from `monetization-scout` that ends in "apply" or "contact" —
  this skill is what actually executes that step

Not for: writing the email copy itself once the contact and channel are
settled — call `cold-email` for that pass rather than redoing it here. Not
for lifecycle/nurture emails to people who already opted in — that's
`email-sequence`.

## Workflow

1. **Take the target.** A person, a company, or a list. If it came from
   `monetization-scout`, the "Apply link / Contact" column already has a
   head start — use it, don't re-search from zero.

2. **Contact discovery, email-first.** In order of preference:
   - A named individual's email on the company's own team/press/partnerships
     page.
   - A role-based inbox clearly meant for this purpose
     (`partnerships@`, `press@`, `affiliates@`) over a generic `info@`/`support@`.
   - LinkedIn, to find the *right role* (partnerships, BD, marketing — not
     just "whoever's most senior") when no email is public, then check
     whether that person's email is published anywhere before resorting to
     LinkedIn DM as the channel.
   - A contact form, only once the above are exhausted.
   - **A pattern-guessed email** (e.g. `first.last@company.com` inferred
     from a known company convention) is a last resort and must be labeled
     `(inferred, unverified — confirm before relying on it)`. Never presented
     as a confirmed address. Don't send anything to a guessed address without
     saying plainly that it's a guess.

3. **Pick the channel and, if volume warrants it, a tool** — see
   `references/tooling.md` for the actual options, split into self-hosted and
   commercial (flag any new commercial SaaS dependency per the org's
   self-hosted-by-default standard, if operating inside a project that has
   one). One-off outreach to a handful of contacts needs no tool at all —
   don't recommend standing up infrastructure for five emails.

4. **Compose the first touch.** For email, invoke `cold-email` to actually
   write it — that skill owns tone, structure, subject lines, and follow-up
   sequencing; don't duplicate its guidance here. For a call, use
   `references/tooling.md`'s call-prep notes: a short opener, the one
   specific reason this contact and not a generic pitch, and what a "yes"
   from this call actually looks like (a meeting, a warm email follow-up —
   decide before dialing, not during).

5. **Compliance, briefly** — this skill is not legal advice, but say the
   obvious things out loud: real sender identity and an opt-out on cold
   email (CAN-SPAM/GDPR basics), and awareness of do-not-call rules before
   cold calling at any real volume. Flag to route anything at scale through
   proper legal review rather than trying to resolve it here.

## Guardrails

- No fabricated contact info, ever — see step 2. An honest "couldn't verify
  an email, here's the contact form" beats a confident-looking guess.
- No recommending a paid tool as the default when a one-off or a
  self-hosted option genuinely covers the need — see the tooling reference
  for which is which.
- This skill finds the door and knocks once. Ongoing sequence/CRM management
  belongs to whatever tool was chosen in step 3, not to repeated invocations
  of this skill per follow-up.
