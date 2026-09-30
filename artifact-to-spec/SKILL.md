---
name: artifact-to-spec
description: "Use when a client or team hands over a folder of raw legacy artifacts — spreadsheets, ledgers, paper-process exports, forms, .ods/.xlsx workbooks, scanned records — and wants to know what could be built from them, or wants them turned into a webapp/tool/system. Triggers on 'study this folder', 'what can we build from this', 'digitize this process', 'turn this spreadsheet into an app', 'reverse-engineer this into software', 'client intake', 'these are the client's files, make sense of them'. Produces a domain model and project plan, not code — hand the result to spec-to-repo or saas-scaffolder to actually build it."
---

# Artifact to Spec

Reverse-engineer a working software spec out of the artifacts a business already uses to run itself — usually spreadsheets, but also forms, exported bank/ledger statements, registers, and scanned paperwork. The client didn't write requirements; their spreadsheet formulas, column layouts, and duplicated tabs *are* the requirements. This skill extracts them.

**Not this skill** once you already have a clear feature list / PRD — go straight to `spec-to-repo` or `product-team/saas-scaffolder`. This skill is specifically for the "here's a folder of messy real-world stuff" starting point.

## Core principle

Every hand-built spreadsheet encodes a data model and a set of business rules whether or not anyone wrote them down. Column headers are fields. Separate tabs are entities or views. Formulas are business logic. Repeated manual patterns (copy this balance into that sheet, recompute this % by hand) are the exact pain points a webapp should remove. Your job is archaeology, not guessing — read what's actually there before proposing anything.

## Workflow

### Phase 1 — Inventory

List every file in the folder (`ls -la`, recurse if nested). Classify each by type: spreadsheet (xlsx/xls/ods/csv), document (docx/pdf/txt), image/scan, other. Note file names carefully — they often carry domain vocabulary (e.g. "LOAN LISTING", "MEMBERS DUE PAYMENT") that should survive into the spec's terminology so the client recognizes their own process.

### Phase 2 — Extract structure

For spreadsheets, run the bundled script instead of opening each file by hand:

```bash
python3 scripts/inspect_workbook.py "<path-to-folder-or-file>" --rows 5
```

If it reports `openpyxl`/`odfpy` missing, create a throwaway venv rather than touching system Python:
```bash
python3 -m venv /tmp/inspect_venv && /tmp/inspect_venv/bin/pip install --quiet openpyxl odfpy
/tmp/inspect_venv/bin/python scripts/inspect_workbook.py "<path>" --rows 5
```

For each sheet/tab, capture:
- **Header row** → candidate field names
- **Sample rows** → data types, formats (dates, currency, %), value ranges
- **Formulas** → business rules (running balances, interest calcs, % of total splits, lookups across sheets)
- **Sheet name and position** → candidate entity or report name
- **Blank / error cells** (`#DIV/0!`, empty required-looking fields) → existing pain points, validation gaps

For documents/PDFs/text, read them directly (Read tool). For images/scans, describe what's visible and flag anything you can't confidently transcribe rather than guessing at numbers.

### Phase 3 — Reverse-engineer the domain model

Synthesize across all files into:

1. **Entities** — e.g. Member, Loan, Transaction, NonMemberLoan, Payment. A sheet is often an entity; sometimes several sheets are really one entity viewed differently (e.g. "MEMBERS DUE PAYMENT" and "MEMBERS STATEMENT" may both derive from one Member + Ledger model — say so, don't just mirror the tabs 1:1).
2. **Fields per entity** — name, inferred type, whether computed (and from what formula) or entered.
3. **Relationships** — foreign keys implied by shared names/IDs across sheets (e.g. a name appearing in both a roster and a loan ledger).
4. **Business rules** — every formula translated into plain language ("member share = monthly due / total deposits × general interest pool"). Flag any rule you're inferring rather than reading directly from a formula.
5. **Roles/actors** — who fills in which sheet, who reads which report (infer from context — treasurer, member, admin — and flag as inferred).
6. **Existing pain points** — manual re-entry across sheets, formula errors, no audit trail, single point of failure (one spreadsheet file), no concurrent access.

### Phase 4 — Draft the plan

Produce a single markdown document (don't scatter across chat) with these sections:
- **Source summary** — what was in the folder, one line per file
- **Domain model** — entities, fields, relationships (table or bullet form)
- **Business rules** — the translated formulas
- **Proposed features** — mapped 1:1 to what the artifacts already do, plus the obvious next step (e.g. "auto-computed member statements" instead of "someone copies numbers between four tabs")
- **User roles** — who uses the eventual app and what they can do
- **Open questions** — anything genuinely ambiguous (max ~5, only real ambiguities — don't pad)
- **Suggested stack** — only if the user wants that now; otherwise leave for `spec-to-repo`

Save it as `PROJECT_PLAN.md` in the client's project folder (next to the source artifacts) unless the user wants it elsewhere.

### Phase 5 — Confirm, then hand off

Ask the open questions (batch them, don't drip one at a time). Once resolved, tell the user the plan is ready to feed into `spec-to-repo` (generic app) or `product-team/saas-scaffolder` (SaaS with auth/billing) as the next step — don't scaffold code yourself in this skill.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Proposing a generic CRUD app without reading the actual sheets | Always run the inspection script first; ground every feature in something observed |
| Mirroring every tab as a database table 1:1 | Sheets are views; collapse duplicated/derived sheets into one normalized entity and say so |
| Inventing business rules | Only state a rule as fact if you saw the formula or explicit text; otherwise mark it "inferred — confirm with client" |
| Silently dropping messy data (errors, blanks) | Surface them as pain points — they're often exactly why the client wants a new system |
| Writing code in this skill | This skill ends at the plan; build happens in `spec-to-repo` / `saas-scaffolder` |
| Asking questions one at a time | Batch clarifying questions (AskUserQuestion or a single numbered list) |

## Cross-references
- Next step: `spec-to-repo` — turns the finished plan into a runnable repo
- Next step: `product-team/saas-scaffolder` — if the plan calls for a multi-tenant SaaS with auth/billing
- Related: `product-discovery` — use instead when there's no existing artifact trail, only stakeholder interviews/assumptions to validate
