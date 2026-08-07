# Impactors Academy — Coolify estate

Read before touching any service. Verify against the Coolify UI if anything here
looks stale — this file is a map, not the source of truth.

## Services and domains

| Project | Production domain | Repo | Notes |
|---|---|---|---|
| impactors-academy | `impactorsacademy.com` | `impactors-academy/impactors-academy` | Marketing site |
| ia-pro | `pro.impactorsacademy.com` | `impactors-academy/ia-pro` | Marketing + admin. Turborepo (`apps/pro`, `packages/db`) |
| loc | `loctravels.com` | `impactors-academy/loc` | Next frontend + FastAPI backend (`api.loctravels.com`) |
| prospectbuddy | — | `impactors-academy/prospectbuddy` | Internal tool / SaaS |
| grindbuddy | — | `impactors-academy/grindbuddy` | PAUSED |

## Branch → environment

```
feature/*  →  PR  →  develop  →  staging.<domain>     (auto-deploy)
develop    →  PR  →  main     →  <domain>             (auto-deploy)
```

**Reality check (2026-08-07):** no `develop` branch exists in any repo. Phase 0B is
still aspirational — everything currently goes `feature/* → PR → main`, so **every
merge to `main` is a production deploy with no staging gate.** Treat main merges
accordingly until `develop` exists.

## Observed deploy latency

| service | merge → live |
|---|---|
| loc | ~3 min |
| impactors-academy | ~8 min |
| ia-pro | longer than both |

`404 → 503 → 200` on a changed asset is the redeploy signature. No `503` at all after
the slowest known time is the first real evidence of a webhook problem.

## Stack the deploys assume

```
Email       Resend
Payments    Stripe (one org account, products per venture)
Files       Cloudflare R2
Database    Postgres via Drizzle (Node) / Alembic (LOC)
Secrets     Vaultwarden
Edge        Cloudflare — DNS, SSL, WAF, rate limiting
Admin       Cloudflare Access (Zero Trust) in front of every /admin*
Analytics   Umami everywhere, GA4 on sites, PostHog on apps
```

## Per-project gotchas

**ia-pro** — Turborepo. Root scripts run through `turbo`, which refuses to resolve the
workspace without a `packageManager` field in the root `package.json`. Build from the
repo root, not from `apps/pro`. Blog and projects need `DATABASE_URL` but must degrade
to an empty state without it — the build checks that promise, so do not add it just to
make a build pass.

**loc** — two deployables from one repo: Next frontend and FastAPI backend. Its dev
server runs on **:3002**, not 3000 or 3001. CI is `.github/workflows/ci.yml` and covers
both halves.

**impactors-academy** — **no CI at all.** Nothing verifies a PR. It also carries known
pre-existing lint errors, so a green-looking merge means nothing there. Port ia-pro's
workflow when you get the chance, and check its lockfile for the missing-transitive-
dependency defect ia-pro had before trusting any lint result.

## Local dev ports

```
3000  impactors-academy
3001  ia-pro
3002  loc frontend
```

Check all of them before any build: `lsof -nP -iTCP -sTCP:LISTEN`.
