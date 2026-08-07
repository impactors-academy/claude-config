---
name: coolify-deployment
description: "Deploy and operate services on the Impactors Academy Coolify VPS. Use when deploying or redeploying any project, setting up a new service, adding or rotating environment variables, configuring staging vs production, wiring GitHub auto-deploy webhooks, rolling back a bad deploy, debugging a build that fails on Coolify but works locally, adding persistent volumes, or verifying that a merge actually reached production. Triggers: 'deploy', 'redeploy', 'ship it', 'push to staging', 'it's merged but the site hasn't changed', 'roll back', 'set an env var', 'the build fails on Coolify', 'is it live yet', 'trigger a deploy', 'Coolify'."
---

# Coolify Deployment

Coolify runs on the org VPS and deploys every Impactors Academy service. Cloudflare
sits in front of it for DNS, SSL and WAF.

Org-specific service map, domains and branch mapping:
`references/impactors-academy.md` — read it before touching any service.

---

## The single most important rule

**"Merged" is not "deployed", and "deployed" is not "correct".**

A merge to `main` fires a webhook. The webhook may not fire. The build may fail. The
build may succeed and ship the wrong artifact. None of that is visible from GitHub.

Never report a deploy as done because a PR merged. **Verify the artifact.**

```bash
bash scripts/verify-deploy.sh https://pro.impactorsacademy.com/favicon.ico path/in/repo.ico
```

That script polls the live URL until it changes, then compares its SHA-256 against the
file in the repo. Byte-identical is the only proof that the thing you shipped is the
thing being served.

---

## Deploy timing — do not panic

Measured on this estate, same merge minute, three services:

| service | 404 → 503 → 200 |
|---|---|
| loc | ~3 minutes |
| impactors-academy | ~8 minutes |
| ia-pro | noticeably longer still |

`503` is the signature of a Coolify redeploy in progress: the old container has stopped
and the new one has not answered yet. Seeing `503` is **good news** — it means the
webhook fired.

**A service that has not moved after ten minutes is not proof of a broken webhook.**
This has been called wrongly before. Poll, wait, and only investigate the webhook after
the slowest known service time has passed with no `503` at all.

---

## Triggering a deploy manually

Normal path is automatic: push to the mapped branch → GitHub webhook → Coolify pulls,
builds, swaps containers. You should rarely need a manual trigger.

When you do, in order of preference:

1. **Coolify UI** → the service → **Redeploy**. Always available, no credentials to
   handle, shows build logs live.
2. **Deploy webhook** — each service has a URL under its *Webhooks* tab.
3. **API** — `Authorization: Bearer <token>`, base `https://<instance>/api/v1`. Tokens
   come from **Security → API Tokens** and need the `deploy` permission scope. The token
   is shown once.

**Discover the exact deploy endpoint from the instance rather than guessing** — it has
moved between Coolify versions:

```bash
curl -s -H "Authorization: Bearer $COOLIFY_TOKEN" \
  "https://<instance>/api/v1/openapi.json" | jq -r '.paths | keys[]' | grep -i deploy
```

### Claude cannot do this for you

There is no Coolify token or instance URL on the dev machine, and there should not be —
secrets live in **Vaultwarden**, never in git and never in chat. Claude must not accept
a pasted token or deploy-hook URL: a deploy hook is a live production trigger.

If a manual deploy is needed, **say so and hand it to the operator.** Offer the UI path.
Do not improvise around missing credentials.

---

## Environment variables

Set in the **Coolify UI only**, never in code, never in the repo.

**A changed env var does nothing until the service is redeployed.** This is the single
most common "I changed it and nothing happened".

Rotating a secret:

1. Generate the new value
2. Store it in Vaultwarden
3. Update it in Coolify
4. **Redeploy**
5. Remove the old value everywhere it still exists

Build-time vs runtime matters in Next.js: anything `NEXT_PUBLIC_*` is baked into the
bundle at build time. Changing it requires a rebuild, not just a restart.

---

## Rollback

Coolify keeps previous builds. Service → **Deployments** → pick the last good one →
**Redeploy**. Two clicks.

**Know where that button is before shipping anything risky.** A rollback you have to
find under pressure is not a rollback.

Rollback reverts the *container*, not the *database*. A deploy that ran a destructive
migration is not undone by redeploying the old image — see the migration rule below.

---

## Database migrations

Never ship code and run its migration against production in the same motion.

```
1. Write the migration (Drizzle for Node projects, Alembic for LOC)
2. Run it against STAGING first
3. Verify the staging app works with the new schema
4. Run it against PRODUCTION
5. Only then merge to main
```

Migrations are forward-only in practice. Backups are the real undo — confirm one exists
and is recent before any destructive change.

---

## Debugging a build that works locally and fails on Coolify

Check in this order — cheapest first:

1. **Lockfile drift.** `npm ci` fails on a lockfile out of step with `package.json`.
   It can also *succeed* and install a broken tree: a lockfile can declare a dependency
   and omit its package entry, so the install completes and the tool crashes at runtime.
   Reproduce with a clean clone plus `npm ci` — never trust the local `node_modules`.
2. **Missing env var at build time.** Anything read during `next build`, including
   `NEXT_PUBLIC_*`, must exist in Coolify before the build, not just at runtime.
3. **Case sensitivity.** macOS is case-insensitive, the Linux container is not.
   `import Nav from './nav'` works locally and fails in the build.
4. **Node version.** Match the container's Node to local. Pin via `packageManager` and
   `engines` so both agree.
5. **Build resources.** A large Next build can exhaust memory on a small VPS. The
   symptom is a killed process, not a compile error.

---

## Never do this

- **Never run `npm run build` against a directory a dev server is serving.** It rewrites
  `.next` underneath the running server; the stylesheet starts 404ing and the site
  renders unstyled. Check **every** listening port first — not the two you expect:
  `lsof -nP -iTCP -sTCP:LISTEN`. This has been done here and cost real time.
- Never push straight to `main`. `feature/* → PR → develop → staging → PR → main`.
- Never put a secret in the repo, a commit message, or a chat message.
- Never verify a deploy by fetching the HTML through Cloudflare with curl — see below.

---

## Cloudflare is in front of everything

Cloudflare bot-challenges **HTML** for non-browser clients: `curl` and WebFetch get
`403 cf-mitigated: challenge`. **Static assets are not challenged** and return normally.

So verify deploys against an **asset** (`/favicon.ico`, a hashed JS chunk, an image),
never the page. If you need the rendered `<head>`, read it from the local dev server, or
use the Chrome extension against production — do not attempt to work around the
challenge.
