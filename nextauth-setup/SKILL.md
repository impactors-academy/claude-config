---
name: nextauth-setup
description: "Set up and operate NextAuth (Auth.js) v5 for external user authentication in Impactors Academy Next.js projects. Use when adding signup or login for customers, wiring OAuth or magic-link providers, protecting app routes and server actions, managing sessions and roles, adding a Drizzle adapter, or debugging a session that is null or a callback that fails. Triggers: 'NextAuth', 'Auth.js', 'add login', 'add signup', 'user auth', 'magic link', 'OAuth provider', 'session is null', 'protect this route', 'auth adapter', 'AUTH_SECRET'."
---

# NextAuth v5 (Auth.js) — external users

NextAuth v5 is the org standard for **external user** authentication in Next.js
projects. Team authentication is Authentik — see `/authentik-sso`.

Per-project state: `references/impactors-academy.md`.

---

## Decide who you are authenticating first

| Audience | Use |
|---|---|
| Customers, external users, app signups | **NextAuth v5** |
| Team, staff, admin surfaces | Authentik SSO + MFA, behind Cloudflare Access |
| Supabase-based platforms | Supabase Auth (per PLATFORM-STANDARDS) |

Building a NextAuth login for an internal admin panel is the common mistake. An
admin surface should be behind Cloudflare Access with team identity — not a
username and password you now have to operate, reset and rate-limit yourself.

---

## v5 is not v4

The migration bites in specific places:

- Config lives in **`auth.ts` at the project root**, exporting
  `{ handlers, auth, signIn, signOut }` from `NextAuth(...)`.
- Route handler is `app/api/auth/[...nextauth]/route.ts` re-exporting `handlers`.
- **`auth()` replaces `getServerSession()`** — no `authOptions` argument.
- Env vars are `AUTH_SECRET`, `AUTH_URL` and `AUTH_<PROVIDER>_ID` / `_SECRET`.
  The `NEXTAUTH_*` names are v4.
- Providers are imported from `next-auth/providers/*` and it is now edge-aware —
  a database adapter cannot run on the edge runtime. Split the config
  (`auth.config.ts` for edge-safe middleware, full config for Node) if you use
  both middleware and an adapter.

Do not mix v4 tutorials into a v5 project. The symptom is `session` always null
with no error.

---

## Session strategy

| | JWT (default) | Database |
|---|---|---|
| Revocation | Cannot revoke before expiry | Delete the row, session dies |
| Cost | No DB read per request | One read per request |
| Use when | Simple apps, short sessions | You need real logout-everywhere, or roles that change |

**If you need to ban a user or end a session immediately, JWT alone will not do
it.** Choose database sessions before you build the feature that needs them.

Keep sessions short for anything with write access. Refresh on activity rather
than issuing a 30-day token.

---

## Authorisation is not authentication

`auth()` tells you *who* — never *whether they may*.

```ts
const session = await auth()
if (!session?.user) return unauthorized()
if (session.user.role !== "admin") return forbidden()   // separate, explicit check
```

- **Check on the server, in the route or server action** that does the work.
  Middleware is a convenience layer, not the boundary — a server action is
  reachable without passing through the page it lives on.
- **Never trust a role from the client**, and never trust it from a JWT you did
  not verify server-side.
- Put roles in the database and read them, or accept that a role baked into a
  JWT is stale until the token expires.

---

## Adapter (Drizzle)

`@auth/drizzle-adapter` with the standard `users` / `accounts` / `sessions` /
`verificationTokens` tables. Generate the migration and **read the SQL** before
applying — see `/drizzle-orm`, which documents a live schema-drift hazard in
ia-pro that makes this more than boilerplate advice.

Email/magic-link providers send mail — that goes through **Resend**
(`/resend-email`), not a separate SMTP setup.

---

## Debugging

| Symptom | Check first |
|---|---|
| `session` always null | v4 patterns in a v5 project, or `AUTH_SECRET` unset |
| Works locally, fails in prod | `AUTH_URL` wrong, or OAuth callback URL not registered for the prod domain |
| `MissingSecret` | `AUTH_SECRET` not set — generate with `openssl rand -base64 32` |
| Adapter errors in middleware | Database adapter on the edge runtime — split the config |
| Callback redirects to `/` silently | Provider callback URL mismatch, exact string including trailing slash |
| Session does not update after a role change | JWT strategy — the token holds the old role until expiry |

---

## Never do this

- Never expose `AUTH_SECRET` or a provider secret to the browser. No `NEXT_PUBLIC_*`.
- Never rely on middleware alone to protect a mutation.
- Never use NextAuth for team/admin access — that is Authentik + Cloudflare Access.
- Never roll your own password hashing alongside it. If you need credentials,
  use the framework's, and prefer a provider or magic link over passwords.
- Never skip rate limiting on auth routes — Phase 0C requires it at the
  Cloudflare edge (5 req/min on `*/auth/*`).
