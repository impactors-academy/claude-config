# Impactors Academy — Drizzle

## Where Drizzle is actually used

| Project | State |
|---|---|
| ia-pro | **Live.** Turborepo: `packages/db` (config + migrations) and `apps/pro` |
| prospectbuddy | No Drizzle found — built, not deployed. Verify before assuming |
| grindbuddy | No Drizzle found. PAUSED, backend stack undecided |
| impactors-academy | No database — marketing site |
| loc | **Not Drizzle.** Python: SQLAlchemy 2 + Alembic. Use `/migration-architect` |

## ⚠ ia-pro has two schema files, and they have drifted

Verified 2026-08-08:

```
packages/db/src/schema.ts        19 lines — projects only
apps/pro/src/lib/db/schema.ts    37 lines — projects + posts
```

`packages/db/drizzle.config.ts` points at `./src/schema.ts` — the **19-line one,
which has no `posts` table**. But `packages/db/migrations/` contains
`0001_posts.sql`, so `posts` exists in the database.

**Running `npx drizzle-kit generate` in `packages/db` today will generate a
migration that DROPS the posts table.** It will look like an ordinary diff.

Fix before the next schema change: make `packages/db/src/schema.ts` canonical
(add `posts` to it), have `apps/pro` import from the package rather than keep
its own copy, and delete `apps/pro/src/lib/db/schema.ts`. Then `generate` and
confirm the diff is empty — an empty diff is the proof the two are reconciled.

Until that is done, **read every generated migration with particular care in
this repo.**

## Migrations that exist

```
packages/db/migrations/0000_init.sql
packages/db/migrations/0001_posts.sql
```

## Conventions in the existing schema

- `serial` primary keys, `text` slugs with `.unique()`
- `timestamp(..., { withTimezone: true }).defaultNow()`
- Text enums: `status: text('status', { enum: [...] })`
- `snake_case` columns, `$inferSelect` / `$inferInsert` exported per table

## Env

```
DATABASE_URL   secret · Vaultwarden → Coolify · Postgres container in the same stack
```

`drizzle.config.ts` reads `process.env.DATABASE_URL` directly and runs in plain
Node — it does not pick up `.env.local` the way Next does. Export it in the shell
or use `dotenv -e` when running drizzle-kit.

## Related

- `/migration-architect` — migration strategy, and Alembic for LOC
- `/database-schema-designer` — schema design before you write the table
- `/coolify-deployment` — never run a production migration in the same motion as the deploy
