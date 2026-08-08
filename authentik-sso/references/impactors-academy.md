# Impactors Academy — Authentik

## Status (2026-08-08)

**Not stood up.** MASTER-CHECKLIST Phase 0C lists "Team auth: Authentik SSO +
MFA (mandatory, no exceptions)" and the item is unchecked. No confirmed
instance, no confirmed integrations.

Consequence to be honest about: **team authentication is currently whatever each
app does on its own**, and Cloudflare Access authenticates against whichever IdP
the Zero Trust account has configured — confirm in the dashboard rather than
assuming MFA is enforced.

## Target deployment

Self-hosted on the Hostinger VPS via Coolify, with its own Postgres + Redis.
Admin interface behind Cloudflare Access. See `/coolify-deployment`.

## What should sit behind it

| Surface | Today |
|---|---|
| loc `/admin` + `/api/admin/*` | Cloudflare Access (live) + origin JWT check. Editor writes also gated by `EDITOR_API_KEY` |
| ia-pro admin | verify |
| prospectbuddy (internal tool) | not deployed |
| Coolify admin panel | strong password + 2FA per Phase 0C-1 |
| Authentik itself | behind Cloudflare Access |

## Interim reality on loc

`EDITOR_API_KEY` is a **single shared secret**, not per-person identity. It
cannot be attributed to a user and cannot be revoked for one person without
rotating for everyone. That is acceptable only until Authentik exists — it is
the reason Phase 1 lists moving editor access to SSO.

## Related

- `/cloudflare-access` — the authorisation half, and the origin JWT check
- `/nextauth-setup` — external users, which do **not** belong in Authentik
- `/coolify-deployment` — deploying and backing up Authentik itself
