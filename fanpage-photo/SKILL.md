---
name: fanpage-photo
description: |
  Use when the user asks to download, save, back up or repost a photo for one of the
  Impactors Academy fan pages (Ronaldo, Messi, Yamal, Mbappe), or to set a fan page
  profile or cover photo from a player's own official page. Runs the fan page photo
  checks, gets the image, and files it into content/fanpages/<page>/photoN with a
  source record. Not for videos (use the watch skill) and not for our own pages
  (Beyond the Courts, The Impactors Code).
---
# Fan page photo

Get a photo from a player's own official page, check it against our rules, and file it
so it is backed up. Rules live in `content/strategy/FANPAGE-ACCOUNT-SAFETY-ADAPTED.md`
(guidelines 3, 5, 5a and 19). Read it if a case is unclear.

## Step 1: Check the photo before touching it

All must be true, or pick another photo:

| Check | Rule |
|---|---|
| Source | The player's own official page or account, never an agency, media site or fan account |
| People | The player alone or with adults. No children, ever (guideline 3) |
| Content | A photo. No broadcast clips, match footage or copyrighted music |
| Logos | A crest or sponsor logo only as incidental kit detail. Never as the subject or cropped in on |
| Likeness | Real photo posted by the player. Never a photoreal AI image of a real person (guideline 6) |

Show the candidate to the user and get a clear yes before downloading (state the source
and file type). Downloading needs explicit permission every time.

## Step 2: Get the image

Try these in order.

**A. The user downloads it (works today).** In the photo viewer on the official page, click
the "..." next to the player's name, then Download. Automated clicks on that menu do not
save a file (Chrome blocks it), and reading Facebook's signed image links from the page
is blocked by the browser tool, so do not try to script around either.

**B. gallery-dl, if installed.** It supports public Facebook photos and albums:
```bash
which gallery-dl && gallery-dl -d ~/Downloads/gallery-dl-output "<photo url>"
```
It is not installed by default. Ask before running `brew install gallery-dl`. Never use
`--cookies-from-browser` without asking, it hands the browser's logged in cookies to the tool.

**C. yt-dlp is for videos only.** It does not support Facebook photo posts.

Never scrape, script logins, or use unofficial tools against the fan page accounts
themselves (guideline 11). This step only reads a public photo from a player's page.

## Step 3: File it

```bash
python3 ~/.claude/skills/fanpage-photo/scripts/save_photo.py \
  --page fans-of-cristiano-ronaldo \
  --file ~/Downloads/<downloaded file> \
  --source-url "<url of the photo or post>" \
  --player "Cristiano Ronaldo" \
  --note "<why chosen>"
```

- Result: `content/fanpages/<page>/photoN.<ext>` plus `photoN.meta.json` (source, date,
  size, hash). N is the next free number. Re-filing the same file does nothing.
- The original is copied, not moved. Add `--move` only if the user wants Downloads cleared.
- **Never delete filed photos.** They are the backup.
- Page folder names use the corrected page name, lowercase with dashes.
  Pages: `fans-of-cristiano-ronaldo` and the Messi, Yamal and Mbappe pages as they are created.

## Step 4: Use it

- **Profile or cover photo:** show the crop to the user and get approval first, then upload
  through the page's own edit controls. A profile picture cannot be shared natively, so it
  is the re-upload route.
- **Posts:** share natively where the platform allows it (Facebook Share, Instagram repost or
  Collab). Caption names the source, has 5 hashtags, and the brand tags follow guideline 19.
- Record what was done in `content/research/FANPAGE-ROLLOUT-HANDOFF.md`.

## Accepted risk

Crediting a source is not a licence. Meta can still act on a reupload, and repeat infringers
are removed. If a page gets a copyright warning, stop reposting photos on it the same day.
