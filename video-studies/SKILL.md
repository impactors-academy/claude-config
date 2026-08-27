# Video Studies — Study Driver

A reusable driver for turning a video into structured findings via `/watch`.
This skill holds the *tool* only — the prompt in `commands/`. The findings
it produces do **not** live here; they go into the relevant project's own
`docs/video-studies/{slug}/findings.md` (org-wide topics go in the workspace
root's `docs/video-studies/`), same as `site-studies/` audits belong in a
project's `docs/`, not in the global skills repo.

## Why findings live in the project, not here

This repo (`claude-config`) is global config synced across machines — it's
not the right home for a specific project's research artifacts. A study
about, say, an Impactors Academy UGC workflow is Impactors Academy content
and should travel with that project's docs, get reviewed in that project's
PRs, and show up when someone opens that project's `docs/` folder — not be
buried in a skills backup repo.

## How a study gets added

`commands/study-video-step1.md` is a reference prompt, not a registered
slash command — follow it manually (or paste its contents as your prompt).
It runs `/watch` on the video, reads the frames + transcript, then writes
structured findings to `<project>/docs/video-studies/{slug}/findings.md`
and saves any frames worth keeping to `<project>/docs/video-studies/{slug}/frames/`.
Pick `<project>` by what the video is actually relevant to:

- **Org-wide topic** (applies across ventures — marketing, ops, general
  technique) → the workspace root's `docs/video-studies/`.
- **Project-specific topic** → that project's own `docs/video-studies/`.

Add an index entry to that project's `docs/video-studies/README.md` (or
`docs/INDEX.md` if it's the workspace root) after writing the findings.

## Standing rule

Same IP boundary as `site-studies/`: capture technique and pattern, not the
video's actual content. Findings describe *how* something was done (pacing,
structure, a specific visual/audio technique, a UI flow being demoed) —
never a transcript dump or a scene-by-scene reproduction of someone else's
work. Quote a line only when the wording itself is the finding.
