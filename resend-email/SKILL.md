---
name: resend-email
description: "Send transactional email from any Impactors Academy platform via Resend. Use when wiring a contact or enquiry form to email, sending auth email (verification, password reset, magic link), receipts or order confirmations, notifying the team about a new lead, building or changing an email template, configuring the sending domain and DNS, or debugging mail that lands in spam or never arrives. Triggers: 'send an email', 'contact form', 'enquiry notification', 'transactional email', 'Resend', 'password reset email', 'email template', 'email goes to spam', 'DKIM', 'SPF', 'DMARC', 'sending domain'."
---

# Resend — transactional email

All transactional email in the org goes through **Resend**. No SendGrid, no
Mailchimp for transactional, no raw SMTP credentials in application code.

Org domains, addresses and current status: `references/impactors-academy.md`.

---

## Status: not yet configured

MASTER-CHECKLIST Phase 0D has every Resend item unchecked. The account, the
sending domain and the DNS records are **not confirmed set up**. Before writing
send code, verify what actually exists rather than assuming this skill's
defaults are live. LOC currently logs inquiries with `SMTP_*` blank and sends
nothing — that is the pre-Resend state, not a Resend integration.

---

## The rule that matters most

**Email is a side effect, not a response.** A form handler that awaits an email
send and returns its result will fail the user's submission when Resend has a
bad minute.

```
1. Validate input (Zod / Pydantic)
2. Persist the record          ← the actual job
3. Return success to the user  ← do not block on mail
4. Send the email              ← failure here is logged, not surfaced
```

Losing a lead because the notification email failed is the failure mode to
design against. The database row is the lead; the email is a convenience.

---

## Sending

```ts
import { Resend } from "resend"

const resend = new Resend(process.env.RESEND_API_KEY)

const { error } = await resend.emails.send({
  from: "LOC <noreply@impactorsacademy.com>",   // must be on a verified domain
  to: recipient,
  replyTo: enquiry.email,                        // so a reply reaches the human
  subject: `New enquiry — ${enquiry.name}`,
  text: plain,                                   // always
  html: rendered,                                // optional, but never alone
})
if (error) log.error({ err: error }, "resend send failed")   // never throw at the user
```

Non-negotiables:

- **Always include a `text` part.** HTML-only mail scores badly with spam
  filters and is unreadable in text clients. No image-only emails, ever.
- **`from` must be on a verified domain.** Sending as a Gmail address you do not
  control fails DMARC and lands in spam.
- **Set `replyTo` to the human** on notification email, or replies go to
  `noreply` and are lost.
- **Never put the API key in the browser.** No `NEXT_PUBLIC_RESEND_*`. Server
  routes and server actions only.
- **Idempotency** — a retried webhook that resends a receipt is a support
  ticket. Key sends off a stable id where retries are possible.

---

## Templates

Plain HTML plus a text fallback. Tables for layout, inline CSS, no external
stylesheets, no web fonts — mail clients strip all three. Keep the width under
600px.

Brand colours in email: use **`#8B4E22` on light backgrounds, never `#C9885C`**
(2.51:1 on cream — fails WCAG). Most mail clients render light by default and
many ignore dark-mode CSS entirely, so design for light and let dark degrade.
Any colour decision goes through `/color-combinations` first.

React Email works well with Resend if templates grow past a couple of files.
Do not reach for it for two emails.

---

## Domain and DNS

Resend verifies a sending domain with three records in Cloudflare DNS:

| Record | Purpose | Failure mode if missing |
|---|---|---|
| DKIM (`resend._domainkey`) | Signs the message | Fails authentication, spam folder |
| SPF (TXT) | Authorises Resend to send | Fails authentication, spam folder |
| DMARC (`_dmarc`) | Policy + reporting | Spoofable domain; Gmail/Yahoo bulk rejection |

Set these as **DNS-only (grey cloud)**. Proxying a TXT record is meaningless,
but proxying a subdomain used for mail breaks it.

Start DMARC at `p=none` with a reporting address, read the reports, then move to
`p=quarantine`. Going straight to `p=reject` before reading reports is how you
discover you were sending legitimate mail from a service you forgot about.

**Unsubscribe headers are a legal requirement** on all non-critical email.
Transactional receipts are exempt; anything marketing-adjacent is not.

---

## Debugging

| Symptom | Check first |
|---|---|
| Nothing arrives, no error | Wrong `to`, or the send is in a code path that never runs — log before the call |
| Lands in spam | DKIM/SPF/DMARC not all passing. Check the received headers, not the dashboard |
| `403` from Resend | API key wrong, or the `from` domain is not verified on that account |
| Works locally, not in prod | `RESEND_API_KEY` missing in Coolify, and a changed env var does nothing until redeploy |
| Arrives blank | HTML-only with a client that strips it — add the text part |

Read the **received headers** on a real delivered message. The dashboard says
"delivered" once the recipient's server accepts it — including into spam.

---

## Claude cannot do this for you

The Resend API key is a secret. It lives in **Vaultwarden** and is set in
Coolify by the operator. Claude must not accept a pasted key. DNS records are
added in the Cloudflare dashboard.

Claude can write the send code, the templates, and the exact record values to
add — then hand it over.
