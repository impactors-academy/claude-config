# About `artifact-to-spec`

## What it is

A Claude Code skill that turns a folder of raw, messy, real-world business
artifacts — spreadsheets, ledgers, exported bank statements, registers,
scanned forms — into a structured software project plan. It's the missing
step between "here's the client's stuff" and "here's a spec I can hand to a
code-generation skill."

## Why it exists

Most client handoffs don't come with requirements documents. They come with
a spreadsheet someone has hand-maintained for years: tabs with names like
"MEMBER LISTING" or "LOAN LEDGER," formulas nobody re-derives from scratch,
columns whose meaning is implicit in how they're used. That spreadsheet *is*
the requirements — it just needs to be read correctly instead of guessed at.

Existing skills in this setup (`spec-to-repo`, `saas-scaffolder`) assume you
already have a clear feature list. `product-discovery` assumes you're
validating an idea through interviews. Neither covers "reverse-engineer an
existing manual process from its own artifacts." This skill fills that gap.

## What it actually does

1. **Inventory** — list and classify every file in the handoff folder.
2. **Extract** — run `scripts/inspect_workbook.py` (bundled with the skill)
   against spreadsheets to dump every sheet's headers, sample rows, and
   formulas, so nothing has to be opened and read by hand one tab at a time.
3. **Reverse-engineer the domain model** — turn sheets into entities, headers
   into fields, formulas into plain-language business rules, and repeated
   manual patterns (copying a balance between tabs, recomputing a % by hand)
   into flagged pain points.
4. **Draft a plan** — a single `PROJECT_PLAN.md`: source summary, domain
   model, business rules, proposed features, user roles, and a short list of
   real open questions (not padding).
5. **Hand off** — the skill stops at the plan. It does not write code. The
   plan is meant to feed directly into `spec-to-repo` (generic app) or
   `product-team/saas-scaffolder` (multi-tenant SaaS with auth/billing).

## What it deliberately does not do

- Does not invent business rules it didn't observe — anything inferred
  rather than read directly off a formula or explicit text gets flagged as
  "inferred, confirm with client."
- Does not mirror every spreadsheet tab 1:1 as a database table — duplicate
  or derived views get collapsed into one normalized entity.
- Does not silently drop messy data (blank cells, `#DIV/0!` errors) — those
  are surfaced as pain points, since they're often exactly why the client
  wants something new.
- Does not generate code. That's a separate, deliberate handoff to
  `spec-to-repo` or `saas-scaffolder`.

## Where it lives

`~/.claude/skills/artifact-to-spec/`
- `SKILL.md` — the workflow Claude follows when the skill is invoked
- `scripts/inspect_workbook.py` — structural dump tool for xlsx/xls/ods/csv
- `about.md` — this file
