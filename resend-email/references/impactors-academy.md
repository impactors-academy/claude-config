# Impactors Academy — email

## Status (2026-08-08)

**Not yet configured.** Every Resend item in MASTER-CHECKLIST Phase 0D is
unchecked: no confirmed account, no verified sending domain, no DNS records.
Verify against the Resend dashboard before assuming any of the below is live.

## Sending domain

`impactorsacademy.com` — DKIM + SPF + DMARC in Cloudflare DNS, all grey-clouded.

## Addresses (org standard)

```
pro@impactorsacademy.com      → ia-pro enquiries
hello@impactorsacademy.com    → mother site contact
noreply@impactorsacademy.com  → automated system email
loc@impactorsacademy.com      → LOC inquiries (future)
```

## Per-project need

| Project | What it needs email for | Current state |
|---|---|---|
| loc | Inquiry notifications (STAY-4) | `SMTP_*` blank — inquiries are persisted and logged, no mail sent |
| impactors-academy | Contact form | verify |
| ia-pro | Enquiry form → `pro@` | verify |
| prospectbuddy | Not deployed | n/a |

LOC's backend has `EMAIL_FROM` and `SMTP_*` env vars in `docs/DEPLOYMENT.md`.
Moving it to Resend means replacing the SMTP path, not adding alongside it —
leaving both wired is how you end up sending twice.

## Env var

```
RESEND_API_KEY   secret · Vaultwarden → Coolify · runtime only · never NEXT_PUBLIC_*
```

## Related

- `/color-combinations` — any colour in a template. `#8B4E22` on light, never `#C9885C`.
- `/coolify-deployment` — a changed env var does nothing until redeploy.
