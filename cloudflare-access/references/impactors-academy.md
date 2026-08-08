# Impactors Academy — Cloudflare Access estate

A map, not the source of truth. Verify in the Zero Trust dashboard if anything
here looks stale, and re-probe with curl before trusting any row.

## Team domain

```
delicate-king-3ab8.cloudflareaccess.com
```

Verified 2026-08-08 from the live redirect on `loctravels.com/admin`.

## Applications

| Project | Protected paths | Edge status | Origin JWT check |
|---|---|---|---|
| loc | `/admin`, `/api/admin/*` | **LIVE** — verified 2026-08-08 | `frontend/middleware.ts` (PR #17) |
| impactors-academy | — | not verified | none |
| ia-pro | admin surface exists | not verified | none |
| prospectbuddy | not deployed | n/a | none |
| grindbuddy | PAUSED | n/a | none |

**ia-pro has an admin surface and its Access state has not been probed.** That is
the first thing to check when this skill is next used.

## Verified state of loc (2026-08-08)

```
https://loctravels.com/                       200   public, correct
https://loctravels.com/admin                  302 → Access
https://loctravels.com/api/admin/experiences  302 → Access
https://loctravels.com/api/admin/leads        302 → Access
https://api.loctravels.com/health             200   health check, outside Access
https://api.loctravels.com/api/v1/leads/      403   EDITOR_API_KEY, fail-closed
```

The backend on `api.loctravels.com` is **not** behind Access — it is gated by
`require_editor_key` instead. That is deliberate: the browser calls it directly
for public reads. Write endpoints and all `/leads` routes fail closed without the
key. Do not "fix" this by putting Access in front of the whole API host; it would
break the public site.

## Env vars the origin check needs

Set in Coolify per service, runtime, never build args, never `NEXT_PUBLIC_*`:

```
CF_ACCESS_TEAM_DOMAIN   delicate-king-3ab8.cloudflareaccess.com
CF_ACCESS_AUD           <per-application AUD tag — Access → Applications → Overview>
```

Neither is secret. Both are required in production: unset means `/admin` and
`/api/admin/*` return 503 rather than serving unauthenticated.

## Identity

Team SSO is **Authentik + MFA** (org standard, Phase 0C). Access delegates
authentication to it — see `/authentik-sso`. Access enforces *authorisation*
(who may reach this app); Authentik enforces *authentication* (who they are, and
MFA). Neither replaces the other.

**Status:** Authentik is not yet stood up (MASTER-CHECKLIST Phase 0C unchecked),
so Access policies currently authenticate against whatever IdP the Zero Trust
account has configured — confirm in the dashboard before assuming MFA is enforced.
