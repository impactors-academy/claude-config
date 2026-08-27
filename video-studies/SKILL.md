# Video Studies — Findings Library

A curated collection of findings from videos studied with `/watch` — tutorials,
competitor demos, ad breakdowns, talks, whatever's worth a structured writeup
instead of a one-off answer. Same pattern as `site-studies/` (the UI/UX
reference library), applied to video instead of live sites.

## What's in here

- **`{slug}/findings.md`** — Per-video structured writeup: what it's about,
  key moments with timestamps, notable techniques/patterns, and any
  screenshots worth keeping.
- **`{slug}/frames/`** — Selected frames saved out of `/watch`'s temp working
  directory (only the ones worth keeping — not a full dump of every extracted
  frame).

## Videos studied

_(none yet — first study adds a row here)_

| Slug | Source | Type | Key takeaways |
|---|---|---|---|

## How a study gets added

Run `/study-video-step1` (in `commands/`) with a video URL or local path. It
uses `/watch` to pull frames + transcript, writes structured findings to
`{slug}/findings.md`, saves any frames worth keeping to `{slug}/frames/`, and
adds a row to the table above.

## Standing rule

Same IP boundary as `site-studies/`: capture technique and pattern, not the
video's actual content. Findings describe *how* something was done (pacing,
structure, a specific visual/audio technique, a UI flow being demoed) —
never a transcript dump or a scene-by-scene reproduction of someone else's
work. Quote a line only when the wording itself is the finding (e.g. a CTA
phrasing worth studying).
