---
name: authentik-sso
description: "Team SSO and MFA via self-hosted Authentik for Impactors Academy internal tools and admin surfaces. Use when giving the team single sign-on to an internal app, onboarding or offboarding a team member, wiring an app to Authentik over OIDC or SAML, enforcing MFA, connecting Authentik as the identity provider behind Cloudflare Access, or debugging a failed SSO login. Triggers: 'SSO', 'single sign-on', 'Authentik', 'team login', 'MFA', 'OIDC', 'SAML', 'identity provider', 'onboard a team member', 'offboard', 'revoke access'."
---

# Authentik — team SSO

**Authentik + MFA is mandatory for all team authentication.** Internal tools,
admin surfaces, and the identity behind Cloudflare Access.

Org state and per-project wiring: `references/impactors-academy.md`.

---

## Status: not yet stood up

MASTER-CHECKLIST Phase 0C lists Authentik as required and unchecked — there is
no confirmed running instance. Anything below describes the target state.
**Do not tell anyone team SSO is enforced until the instance exists and a real
login has been tested.** Verify before claiming.

---

## Authentik vs Cloudflare Access — they are not alternatives

This is the distinction that gets muddled:

| | Cloudflare Access | Authentik |
|---|---|---|
| Answers | *May this request reach this app?* | *Who is this person, and have they proved it?* |
| Enforces | Authorisation, at the edge | Authentication + MFA |
| Lives | Cloudflare Zero Trust | Self-hosted on the VPS (Coolify) |

Access delegates authentication to Authentik as its OIDC identity provider. You
need both: Access without an IdP has nothing to check identity against;
Authentik without Access leaves the route reachable by anyone who can find it.

**MFA is enforced in Authentik, not in Access.** Configuring Access alone and
assuming MFA is on is a false sense of security — check the Authentik flow.

See `/cloudflare-access` for the edge half, including origin-side JWT verification.

---

## Team vs external users

**Authentik is for the team. It is not for customers.**

| Audience | Use |
|---|---|
| Team, staff, admin | Authentik SSO + MFA |
| External users of a Next.js app | NextAuth v5 — see `/nextauth-setup` |
| External users on Supabase platforms | Supabase Auth |

Putting customers in Authentik turns your identity provider into a customer
database and couples your public signup flow to internal infrastructure.

---

## Wiring an app (OIDC)

Prefer OIDC. Reach for SAML only when the application supports nothing else.

```
1. Authentik → Applications → create the application
2. Create an OAuth2/OIDC provider, note client id + secret
3. Redirect URI must match the app exactly, including scheme and trailing slash
4. Bind a group to the application — never bind individual users
5. App side: standard OIDC client (NextAuth supports a generic OIDC provider)
```

**Bind groups, never individuals.** Offboarding then means removing one group
membership, not auditing every application. This is the single decision that
determines whether offboarding is a five-minute job or an afternoon.

Scope claims deliberately — `email`, `profile`, `groups`. Do not ship extra
claims into tokens that end up in logs.

---

## Offboarding

The reason SSO exists. In order:

```
1. Deactivate the user in Authentik   ← kills new logins everywhere at once
2. Revoke active sessions/tokens      ← existing sessions do NOT die on deactivate
3. Remove from Cloudflare Access groups
4. Rotate any shared secret they held (see /coolify-deployment)
```

Step 2 is the one that gets skipped. Deactivation stops the next login; it does
not always end the session someone already has open.

---

## Operating it

Authentik is **self-hosted on the org VPS via Coolify**, which makes it
infrastructure you own:

- It needs Postgres and Redis of its own — do not point it at an app's database.
- **If Authentik is down, nobody can log in to anything.** Know the restore path
  before you depend on it. Back up its database with the rest (`/cloudflare-r2`).
- Keep a break-glass local admin account with a long unique password in
  Vaultwarden, MFA enrolled, used never. Locking yourself out of the IdP that
  guards everything else is the failure worth designing against.
- Put the Authentik admin interface itself behind Cloudflare Access.

---

## Debugging

| Symptom | Check first |
|---|---|
| `redirect_uri_mismatch` | Exact string match — scheme, port, trailing slash |
| Login succeeds, app says unauthorised | Group not bound to the application, or the `groups` claim not in scope |
| MFA not prompted | The authentication flow does not include the MFA stage — it is per-flow, not global |
| Access still shows its own login | Authentik not set as the Access IdP, or the app uses a different login policy |
| Works for you, not for a new starter | You are in a group they are not — test with a fresh account, not your own |

---

## Claude cannot do this for you

Authentik admin credentials, client secrets and MFA enrolment are operator
tasks. Secrets live in **Vaultwarden**. Claude must not accept a pasted client
secret or admin password.

Claude can write the OIDC client code, the group model, and the exact
provider/application settings to enter.
