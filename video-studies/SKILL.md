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

| Slug | Source | Type | Key takeaways |
|---|---|---|---|
| [adam-mitka-ugc-workflow](adam-mitka-ugc-workflow/findings.md) | youtu.be/lVYNwbCalkY (Adam Mitka) | Creator-education talking-head + whiteboard | Finding → Pitching → Stacking outreach-and-delivery pattern; "free value before the ask" pitch structure; persistent whiteboard-map presentation device |

## How a study gets added

`commands/study-video-step1.md` is a reference prompt, not a registered slash
command — follow it manually (or paste its contents as your prompt): run
`/watch` on the video, read the frames + transcript it returns, then write
structured findings to `{slug}/findings.md`, save any frames worth keeping to
`{slug}/frames/`, and add a row to the table above.

## Standing rule

Same IP boundary as `site-studies/`: capture technique and pattern, not the
video's actual content. Findings describe *how* something was done (pacing,
structure, a specific visual/audio technique, a UI flow being demoed) —
never a transcript dump or a scene-by-scene reproduction of someone else's
work. Quote a line only when the wording itself is the finding (e.g. a CTA
phrasing worth studying).
