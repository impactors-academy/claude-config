# Impactors Academy — NextAuth

## Status (2026-08-08)

No NextAuth installation found in any repo — `next-auth` is not in any
`package.json` checked. It is the **standard for external users**, not something
currently deployed.

| Project | Auth today |
|---|---|
| loc | `EDITOR_API_KEY` shared secret + Cloudflare Access. No user accounts — LOC is lead-gen, no customer login |
| ia-pro | Marketing + internal tool. Verify whether the admin surface has auth of its own |
| impactors-academy | Marketing site, no auth |
| prospectbuddy | Internal tool / SaaS — **the likely first NextAuth consumer**, but check whether it should be Authentik instead (internal tool → Authentik) |
| grindbuddy | Web app, PAUSED, backend stack undecided |

LOC's `docs/BUILD-CHECKLIST.md` mentions `NEXTAUTH_SECRET` in the production
env-var list. That is a **v4 variable name and a leftover** — LOC has no
NextAuth. Do not treat its presence as evidence of an installation.

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
