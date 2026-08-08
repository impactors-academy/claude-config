---
name: cloudflare-access
description: "Protect admin and editor routes with Cloudflare Access (Zero Trust) across Impactors Academy projects. Use when putting an /admin route behind auth, adding someone to or removing them from an admin surface, verifying that an admin route is actually protected, debugging an Access redirect loop or a 403 after login, wiring service tokens for machine-to-machine calls, or verifying the Access JWT at the origin. Triggers: 'protect /admin', 'Cloudflare Access', 'Zero Trust', 'lock down the dashboard', 'who can reach admin', 'Access policy', 'is admin protected', 'redirect loop on admin', 'service token', 'CF_Authorization'."
---

# Cloudflare Access

Every `/admin*` and editor-only route in the org sits behind Cloudflare Access.
This is Phase 0C, non-negotiable, and it is layer **one** of two.

Org application map and current verified state:
`references/impactors-academy.md` — read before changing any policy.

---

## The rule that matters most

**Access at the edge only protects traffic that arrives through Cloudflare.**

A request that reaches the origin container directly never meets the policy:

- someone who knows the VPS origin IP
- another container on the same Docker network
- a hop that bypasses the proxy (grey-clouded DNS record, split-horizon DNS)
- an Access policy that gets deleted, disabled, or scoped to the wrong path

So Access alone is one layer. The org rule is two independent layers, either
holding alone. **The second layer is verifying the Access JWT at the origin.**

This matters most where a route holds credentials of its own. LOC's
`/api/admin/[...path]` proxy attaches `EDITOR_API_KEY` to everything it forwards
and carries no authentication of its own by design. Without an origin check,
anything that lands on that container is a fully authorised write to the API —
and a read of every lead record. Edge-only protection is not enough there.

---

## Verifying the JWT at the origin (Next.js)

Reference implementation, verified in production: `loc/frontend/middleware.ts`.

```ts
import { createRemoteJWKSet, jwtVerify } from "jose"

const TEAM_DOMAIN = process.env.CF_ACCESS_TEAM_DOMAIN
const AUD = process.env.CF_ACCESS_AUD
const JWKS = TEAM_DOMAIN
  ? createRemoteJWKSet(new URL(`https://${TEAM_DOMAIN}/cdn-cgi/access/certs`))
  : null

export async function middleware(req: NextRequest) {
  if (!JWKS || !AUD) {
    // Unconfigured in production is a broken deployment, not a reason to
    // serve the admin surface open. Fail closed.
    if (process.env.NODE_ENV === "production") return deny(503, "Access not configured")
    return NextResponse.next()   // no Access in front of a dev server
  }
  const token =
    req.headers.get("Cf-Access-Jwt-Assertion") ?? req.cookies.get("CF_Authorization")?.value
  if (!token) return deny(403, "Missing Cloudflare Access token.")
  try {
    await jwtVerify(token, JWKS, { issuer: `https://${TEAM_DOMAIN}`, audience: AUD })
  } catch {
    return deny(403, "Invalid Cloudflare Access token.")
  }
  return NextResponse.next()
}

export const config = { matcher: ["/admin/:path*", "/api/admin/:path*"] }
```

Points that are easy to get wrong:

- **Match the API paths too, not just the pages.** `/admin` alone leaves the
  route handlers the dashboard calls wide open. They are the actual write path.
- **Fail closed on missing config.** Defaulting to "allow" when the env vars are
  absent converts a config mistake into an open admin panel.
- **Stand aside in development.** There is no Access in front of `next dev`;
  a check that cannot pass locally gets disabled locally, and then in prod.
- **Never echo the JWT parse error** to the caller. It tells an unauthenticated
  client which part of the token to fix.
- `jose` works on the Edge runtime; `jsonwebtoken` does not. Use `jose`.
- `createRemoteJWKSet` caches the key set. Do not construct it per request.

`CF_ACCESS_TEAM_DOMAIN` and `CF_ACCESS_AUD` are **not secrets** — the AUD tag is
on the Access application's Overview page. They still belong in the deploy
environment, not in the repo, so the same value is not assumed across projects.

For FastAPI, verify the same header with `PyJWT` + the same JWKS URL as a
dependency, and apply it alongside the existing key check — not instead of it.

---

## Verifying an admin route is actually protected

Status codes, not opinions. Run this against production after any policy change:

```bash
for p in / /admin /api/admin/leads; do
  printf "%-20s %s\n" "$p" "$(curl -s -o /dev/null -w '%{http_code}' https://<domain>$p)"
done
```

Expected: public route `200`, admin routes `302` to
`<team>.cloudflareaccess.com`. Confirm the redirect target, not just the 302 —
a `302` to a login page you do not control is not protection:

```bash
curl -s -D - -o /dev/null https://<domain>/admin | grep -i '^location'
```

Then confirm the **origin** independently, bypassing Cloudflare:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://<origin-ip>:3000/api/admin/leads   # want 403
```

A `200` there means the second layer is missing, whatever the edge says.

---

## Policies

Keep them boring:

- **Include** by email or by group — team emails only. Prefer a group so
  offboarding is one edit, not one per application.
- **Session duration** — 24h for admin surfaces. Longer defeats the point.
- **Require MFA** — Access delegates to the identity provider, so MFA is
  enforced there (Authentik for team SSO). Do not treat Access as MFA on its own.
- **Bypass policies are almost always a mistake.** A "bypass for our IP" rule
  turns into permanent unprotected access the day the IP changes hands.

### Service tokens

For machine-to-machine calls (CI, a cron job, an uptime check) use a **service
token**, not a bypass rule. The client sends `CF-Access-Client-Id` and
`CF-Access-Client-Secret`; the policy includes that specific service token.

Health checks are the common case: `/health` usually should sit **outside** the
Access application rather than hold a token, since it must answer for Coolify's
own container checks.

---

## Debugging

| Symptom | Usual cause |
|---|---|
| Redirect loop after login | Access application path overlaps the login callback, or the app covers `/` including `/cdn-cgi/*` |
| `403` after a successful login | Policy matched the app but the user is not in the include rule — check the group, not the email |
| Works in browser, `403` from CI | Browser has the `CF_Authorization` cookie; CI needs a service token |
| Origin returns `200` unauthenticated | No origin-side JWT verification — the actual hole |
| `aud` mismatch in origin logs | Wrong `CF_ACCESS_AUD`; each application has its own tag |
| Everything `403` after a deploy | Access env vars not set on the new container — fail-closed working as intended |

---

## Claude cannot do this for you

There is no Cloudflare API token on the dev machine and there should not be.
Access policies, applications and service tokens are configured **in the
Cloudflare Zero Trust dashboard by the operator.** Claude must not accept a
pasted API token — it is a live production credential for the whole estate.

What Claude can do: write and verify the origin-side check, run the status-code
probes above, and hand you the exact dashboard steps.

---

## Never do this

- Never rely on `robots.txt` or a `noindex` meta tag as access control. They are
  crawler hints. LOC's admin layout says this in a comment for a reason.
- Never protect the pages and leave the API routes they call unprotected.
- Never add a bypass rule to "temporarily" unblock someone.
- Never assume the checklist. Probe the running system — Access was already live
  on LOC while the build checklist still listed it as pending.
