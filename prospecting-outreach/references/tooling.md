# Outreach tooling, by need

Match the tool to the actual volume and channel — don't reach for
infrastructure a handful of emails or calls don't need. Self-hosted/open-
source listed first in each category; commercial SaaS flagged as a
dependency to weigh, not a default.

## Email finding & verification

Needed once outreach moves past "the email is already on their team page"
into "find it from a name and a domain."

- **Self-hosted / free:** manual pattern inference from a company's known
  format (checked against any email already public, e.g. a press contact) —
  free but must be labeled unverified per the main skill's guardrail. A
  simple SMTP-handshake verification script (checks whether a mail server
  accepts a given address without actually sending) can confirm a guessed
  pattern without a paid API — mail servers increasingly block this, so
  treat a "can't confirm" result as inconclusive, not proof the address is
  wrong.
- **Commercial:** Hunter.io, Snov.io, Apollo.io (also does list-building and
  enrichment beyond just email lookup) — usage-based pricing, no long
  contract needed for occasional use. Verification-only services: NeverBounce,
  ZeroBounce — worth it before any real send volume, since a bad bounce rate
  damages sender reputation for everything sent afterward.

## Sending outreach at volume (beyond a handful of one-off emails)

- **Self-hosted:** Listmonk (Go, AGPL, handles sending + basic sequencing),
  Mailtrain (Node, self-hosted newsletter/sequence tool) — both need a
  properly warmed sending domain and SPF/DKIM/DMARC set up correctly, or
  self-hosted sending lands in spam faster than a reputable ESP would.
  `/resend-email` covers transactional sending if that's already the org's
  provider — cold outreach is a different sending pattern (unsolicited,
  needs warmup) and shouldn't share a sending domain/reputation with
  transactional mail.
- **Commercial:** Instantly, Smartlead — built specifically for cold-email
  deliverability at scale (inbox rotation, automatic warmup). Worth it once
  volume is genuinely high (hundreds+ per week); overkill for a
  monetization-scout-sized list of a dozen programs.

## CRM / pipeline tracking for a list of prospects

- **Self-hosted:** Twenty (modern, open-source, actively maintained),
  EspoCRM, ERPNext's CRM module — any of these covers "track who I've
  contacted and what they said" without a subscription.
- **Commercial:** HubSpot free tier, Pipedrive, Attio — fine for a small list
  where self-hosting isn't worth the setup time; check whether the org
  already has one before spinning up a new tool for one campaign.

## Cold calling

Genuinely thin on the self-hosted side — real dialer infrastructure is the
one category here without a mature, easy open-source option.

- **Closest to self-hosted:** Asterisk or FreePBX (self-hosted PBX) paired
  with a click-to-call/power-dialer script against a usage-based calling API
  (e.g. Twilio Voice) — pay per minute/call rather than a per-seat SaaS
  subscription, but requires real setup and phone-system knowledge. Worth it
  only at real recurring call volume, not a handful of calls.
- **Commercial power/AI dialers:** Orum, Nooks, Aircall — per-seat SaaS,
  built for SDR teams doing dozens+ of calls a day. Flag as a new SaaS
  dependency before adopting one, per the org's self-hosted-by-default
  standard, and confirm the actual call volume justifies it first.
- **For occasional, low-volume calls:** no tool needed — a phone and a
  three-line prep note (see the main SKILL.md's call-prep guidance) covers
  it. Don't recommend dialer software for five calls a month.

## A note on "which tool" in general

Recommend the smallest thing that actually covers the stated volume, and say
plainly when the honest answer is "no tool, just do it manually" — that is
correct far more often than these lists suggest, since most outreach
prospecting-outreach gets asked to help with is a handful of high-value
contacts (partnership leads, sponsorship contacts), not a cold-email
campaign at scale.
