---
name: cloudflare-r2
description: "Store files, media and backups on Cloudflare R2 for any Impactors Academy project. Use when adding image or document upload, serving user-uploaded media, generating signed URLs for private files, setting up database or site backups, configuring buckets and lifecycle rules, or debugging uploads that fail or files that 403. Triggers: 'file upload', 'image upload', 'store files', 'R2', 'S3 bucket', 'signed URL', 'presigned', 'media storage', 'backups', 'where do uploads go', 'CORS on upload'."
---

# Cloudflare R2 — files, media, backups

All user-uploaded files, media and backups go to **R2**. No files in Postgres,
no files on the container filesystem, no S3.

Org buckets and status: `references/impactors-academy.md`.

---

## Status: not yet provisioned

Every R2 item in MASTER-CHECKLIST Phase 0D is unchecked. The buckets below are
the **standard**, not confirmed existing infrastructure. Check the Cloudflare
dashboard before writing code that assumes a bucket name.

---

## The rule that matters most

**Files on the container filesystem do not survive a deploy.**

Coolify replaces the container on every deploy. Anything written to local disk
that is not a declared volume is gone — silently, with the upload succeeding and
the file 404ing days later. This is the failure this standard exists to prevent.

The corollary: **never store files in Postgres either.** It bloats backups,
slows restores, and turns every image request into a database query.

---

## Public vs private — decide before writing code

| | Public bucket | Private bucket |
|---|---|---|
| Contents | Product images, course thumbnails, marketing media | User documents, certificates, exports, backups |
| Access | Custom domain, cached at the edge | Signed URLs only, short TTL |
| If leaked | Embarrassing at worst | An incident |

Putting a user document in the public bucket because signed URLs were awkward is
the mistake this table exists to prevent. Private is the default for anything a
user uploaded about themselves.

---

## Uploading

R2 is S3-compatible — use `@aws-sdk/client-s3` with an R2 endpoint.

```ts
const s3 = new S3Client({
  region: "auto",
  endpoint: `https://${process.env.R2_ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID!,
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY!,
  },
})
```

**Prefer presigned upload URLs over proxying bytes through your server.** The
browser PUTs straight to R2; your server only signs. Proxying uploads through a
Next route burns memory on the container and hits body-size limits.

```
1. Client asks the server for an upload URL (authenticated)
2. Server validates type + size, generates a key, returns a presigned PUT
3. Client PUTs the file directly to R2
4. Client tells the server the upload is done; server records the key in Postgres
```

Store the **key**, not a full URL. URLs change when you move to a custom domain
or rotate a bucket; keys do not.

Validate on the server before signing: content type against an allowlist, and a
maximum size. A presigned URL is a capability — do not mint one for a file you
have not agreed to accept.

Never trust the client-supplied filename as the key. Generate it
(`uuid` + extension) and keep the original name as metadata. A filename with
`../` or a duplicate name overwrites someone else's file.

---

## Serving

- Public bucket → **custom domain** (`media.<domain>`), proxied, cached at the
  edge. Do not serve from the `r2.cloudflarestorage.com` endpoint directly.
- Private bucket → presigned GET, short TTL (minutes, not days). A signed URL
  with a week-long expiry that ends up in a shared document is a leak with a
  long tail.
- **Cloudflare Images** on public image buckets handles resizing — do not build
  a thumbnail pipeline before checking `/TOOLS-REGISTRY.md`.

---

## Lifecycle and backups

- Temp/incomplete uploads: auto-delete after 24h. Without this, abandoned
  uploads accumulate forever and you pay for them.
- Backups go to a **separate bucket** from media, encrypted, with their own
  retention. A backup in the same bucket as the thing it backs up is not a backup.
- **A backup you have never restored is not a backup.** Test a restore into a
  scratch database before relying on it.

---

## Debugging

| Symptom | Check first |
|---|---|
| Upload fails from the browser, works with curl | CORS rules on the bucket — R2 CORS is per-bucket, set in the dashboard |
| `403` on a presigned URL | Clock skew, or the URL expired — TTLs are short by design |
| `SignatureDoesNotMatch` | `region` must be `"auto"` for R2, not a real AWS region |
| File uploaded but 404 on read | Serving from the wrong bucket, or the key was stored with a leading `/` |
| Works locally, not in prod | R2 env vars missing in Coolify; a changed env var needs a redeploy |

---

## Claude cannot do this for you

R2 access keys are secrets — **Vaultwarden → Coolify**, set by the operator.
Buckets, custom domains, CORS rules and lifecycle policies are configured in the
Cloudflare dashboard. Claude must not accept a pasted key.

Claude can write the upload flow, the signing code, the validation and the exact
CORS/lifecycle JSON to paste in.

---

## Never do this

- Never write uploads to the container filesystem.
- Never store files in Postgres.
- Never use the client's filename as the object key.
- Never put a user's private document in the public bucket.
- Never expose `R2_SECRET_ACCESS_KEY` to the browser — no `NEXT_PUBLIC_*`.
