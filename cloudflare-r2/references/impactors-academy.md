# Impactors Academy — R2

## Status (2026-08-08)

**Not provisioned.** All R2 items in MASTER-CHECKLIST Phase 0D are unchecked.
The buckets below are the agreed standard; confirm in the Cloudflare dashboard
before writing code against them.

## Standard buckets

| Bucket | Visibility | Contents |
|---|---|---|
| `ia-media` | public | Marketing media, course thumbnails, product images |
| `loc-media` | public | Experience / stay / product imagery |
| `platform-media` | public | Shared platform assets |
| `ia-backups` | **private** | Encrypted DB and site backups, own retention |

Private user files (documents, certificates, exports) need a private bucket per
project — signed URLs only. None exists yet; create rather than reusing a media
bucket.

## Current file handling

| Project | Today | Notes |
|---|---|---|
| loc | `images` JSONB column holds URLs | Points at external URLs (Unsplash allowlisted in `next.config.ts`). No uploads yet — the migration path is upload → R2 → store key |
| impactors-academy | static assets in repo | Fine for marketing assets; not for user uploads |
| ia-pro | verify | Has a blog/projects surface — check where images go |

## Env vars

```
R2_ACCOUNT_ID          not secret
R2_ACCESS_KEY_ID       secret · Vaultwarden → Coolify
R2_SECRET_ACCESS_KEY   secret · Vaultwarden → Coolify · never NEXT_PUBLIC_*
R2_BUCKET              per project
```

## Related

- `/coolify-deployment` — volumes vs R2, and why a changed env var needs a redeploy
- Backups also appear in MASTER-CHECKLIST Phase 0C (encrypted backups to R2, GDPR)
