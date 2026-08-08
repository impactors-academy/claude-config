---
name: drizzle-orm
description: "Design schemas, write queries and run migrations with Drizzle ORM on Impactors Academy Postgres projects. Use when adding or changing a table or column, generating and applying migrations, writing typed queries or joins, setting up Drizzle in a new project, seeding data, or debugging a migration that fails or a type that will not narrow. Triggers: 'Drizzle', 'add a table', 'add a column', 'schema change', 'migration', 'drizzle-kit generate', 'drizzle push', 'db query', 'relations', 'seed the database'."
---

# Drizzle ORM

Postgres via **Drizzle** is the org standard for all new Node projects.
(LOC is the exception — it is Python and uses SQLAlchemy + Alembic.)

Per-project layout and a live schema-drift warning:
`references/impactors-academy.md` — **read it before running `generate`.**

---

## The rule that matters most

**One schema file per database, and `drizzle.config.ts` must point at it.**

Drizzle generates migrations by diffing your schema file against the migration
history. If a second copy of the schema exists somewhere else in the repo, the
copy the config points at *is* the truth — and anything only in the other copy
looks, to `drizzle-kit`, like something you deleted.

Running `generate` in that state produces a migration that **drops the tables
that are missing from the canonical file.** It is silent, it looks routine, and
it is data loss.

ia-pro is in exactly this state right now. See the reference file.

---

## Migrations

```bash
npx drizzle-kit generate     # diff schema → write a .sql migration
npx drizzle-kit migrate      # apply pending migrations
```

**Always read the generated SQL before applying it.** Every time. The diff is
where an accidental `DROP TABLE` announces itself, and it is the only warning
you get.

Order of operations, never compressed:

```
1. Change the schema file
2. generate
3. READ the .sql
4. Apply to STAGING
5. Verify the app works against the new schema
6. Apply to PRODUCTION
7. Only then merge
```

- **`drizzle-kit push` is for local prototyping only.** It applies the diff with
  no migration file, so there is no history and no review step. Never against
  staging or production.
- Migrations are forward-only in practice. Backups are the real undo — confirm a
  recent one exists before anything destructive.
- Renaming a column: Drizzle cannot tell a rename from a drop-plus-add. It will
  offer you the choice interactively; if you are running non-interactively it
  guesses. Hand-write the `ALTER TABLE ... RENAME` instead.

### Destructive changes need two deploys

Dropping a column that running code still selects breaks the old container
during the swap. Split it:

```
Deploy 1: stop writing/reading the column (code only)
Deploy 2: drop the column (migration only)
```

Same for `NOT NULL` on an existing table: add nullable, backfill, then constrain.

---

## Schema

```ts
export const projects = pgTable('projects', {
  id: serial('id').primaryKey(),
  slug: text('slug').notNull().unique(),
  status: text('status', { enum: ['launched', 'building'] }).notNull().default('building'),
  created_at: timestamp('created_at', { withTimezone: true }).defaultNow(),
})

export type Project = typeof projects.$inferSelect
export type NewProject = typeof projects.$inferInsert
```

House conventions, matching what is already in the repos:

- **`timestamp(..., { withTimezone: true })`** — always. A naive timestamp is a
  bug waiting for a user in another timezone.
- **Export `$inferSelect` / `$inferInsert` types** next to each table. They are
  the point of using Drizzle; hand-written row interfaces drift.
- Text enums via `text(..., { enum: [...] })` keep it in TypeScript without a
  Postgres enum type, which is painful to alter later.
- `snake_case` columns, matching the SQL. Do not fight the database's casing.
- Index anything you filter or join on. Drizzle will not notice that you did not.

---

## Queries

```ts
const rows = await db.select().from(projects).where(eq(projects.is_public, true))
```

- **Never interpolate user input into `sql``` templates.** Use the parameterised
  helpers (`eq`, `and`, `inArray`). `sql.raw` with user input is an injection.
- Select the columns you need. `select()` on a wide table pulls everything over
  the wire on every request.
- `db.query` with `relations` gives nested reads without manual joins — define
  the relations, or you will hand-roll the same join in five places.
- Wrap multi-statement writes in `db.transaction`. A half-applied write is worse
  than a failed one.

---

## Debugging

| Symptom | Check first |
|---|---|
| `generate` produces a `DROP TABLE` you did not ask for | Two schema files — the config points at the one missing that table |
| Migration applies locally, fails in prod | Prod has data that violates a new constraint. Backfill first |
| Types will not narrow | Re-export `$inferSelect`; a hand-written interface has drifted from the table |
| `DATABASE_URL` undefined in `drizzle.config.ts` | The config runs in Node, not Next — it does not read `.env.local` automatically |
| Connection exhaustion in serverless | Use a pooled driver / connection limit — one client per invocation exhausts Postgres |

---

## Never do this

- Never run `generate` without reading the SQL it produced.
- Never run `push` against staging or production.
- Never keep two copies of a schema in one repo.
- Never ship a destructive migration in the same deploy as the code change.
- Never run a migration against production before staging has proved it.
