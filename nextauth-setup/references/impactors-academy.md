# Impactors Academy — NextAuth

## Status (2026-08-08)

**Corrected.** An earlier version of this file said no repo used NextAuth. That
was wrong — it came from a failed shell glob, not from reading the files.

**impactors-academy runs NextAuth v4** (`next-auth ^4.24.15`, Next 16) on its
admin dashboard, and it is the org's P2 project.

| Project | Auth today |
|---|---|
| loc | `EDITOR_API_KEY` shared secret + Cloudflare Access (edge + origin JWT). No user accounts — lead-gen, no customer login |
| ia-pro | Marketing + internal tool. Verify whether the admin surface has auth of its own |
| **impactors-academy** | **NextAuth v4, credentials provider, single shared `ADMIN_PASSWORD`.** See below |
| prospectbuddy | Internal tool / SaaS — **the likely first NextAuth consumer**, but check whether it should be Authentik instead (internal tool → Authentik) |
| grindbuddy | Web app, PAUSED, backend stack undecided |

LOC's `docs/BUILD-CHECKLIST.md` mentions `NEXTAUTH_SECRET` in the production
env-var list. That is a **v4 variable name and a leftover** — LOC has no
NextAuth. Do not treat its presence as evidence of an installation.

## impactors-academy dashboard — what is actually there

```
src/auth.ts                          NextAuth v4 options, CredentialsProvider
src/app/admin/login/page.tsx         password-only form (no username)
src/app/admin/(protected)/layout.tsx getServerSession → redirect if absent
  └── posts · contacts · ventures · analytics
```

Three things to know before touching it:

1. **It is v4, not v5.** `getServerSession(authOptions)`, `next-auth/next`,
   `NEXTAUTH_SECRET`. The org standard is v5. Migrating means moving to
   `auth.ts` exporting `{ handlers, auth }` and renaming the env vars — do not
   half-apply v5 patterns into it.
2. **Authentication is a single shared password** (`ADMIN_PASSWORD`, compared
   with `timingSafeEqual`). Same class of weakness as LOC's `EDITOR_API_KEY`:
   no per-person identity, no attribution, no way to revoke one person. Fine as
   a placeholder, wrong for the surface the whole team is meant to work from.
   The credential check itself is written carefully — it refuses the placeholder
   value and uses a constant-time compare.
3. **There is no `middleware.ts`,** so there is no Cloudflare Access origin
   check the way LOC has one. The `(protected)` layout is the only gate, and it
   guards pages — check `src/app/api/admin/*` separately, since route handlers
   are reachable without passing through a page layout.

Target state for the mother dashboard: Authentik SSO + MFA behind Cloudflare
Access (`/authentik-sso`, `/cloudflare-access`) — team identity, not a shared
password. NextAuth stays only if external users ever log in, which is not the
current requirement.

## Deciding for prospectbuddy / grindbuddy

Ask who logs in:

- Internal team only → **Authentik + Cloudflare Access**, not NextAuth
- Paying external users → NextAuth v5
- Both → NextAuth for customers, Access for the admin side. Two doors, not one.

## Env vars (v5 names)

```
AUTH_SECRET          secret · openssl rand -base64 32 · Vaultwarden → Coolify
AUTH_URL             https://<domain>
AUTH_<PROVIDER>_ID / _SECRET
```

Not `NEXTAUTH_URL` / `NEXTAUTH_SECRET` — those are v4.

## Related

- `/authentik-sso` — team auth, and why admin surfaces do not belong here
- `/cloudflare-access` — the layer in front of every admin route
- `/drizzle-orm` — the adapter tables, and read the generated migration
- `/resend-email` — magic-link and verification mail
