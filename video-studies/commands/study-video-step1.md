# Video Study — Prompt for Claude Code (via /watch)

Run once per video, or paste a list and work through them in sequence.
Requires the `/watch` skill (ffmpeg + yt-dlp; transcription is optional —
if the video has no captions, `/watch` will ask before installing or
downloading anything).

---

## The prompt

```
Using /watch, study this video and write up structured findings: [URL or path]
[optional: what to focus on — "the onboarding flow", "the ad's hook", "their
pricing page walkthrough", etc.]

FIRST: derive a slug from the video (e.g. "acme-onboarding-demo" for a demo
video, "competitor-x-pricing-walkthrough" for a walkthrough) and create this
folder structure before doing anything else:

video-studies/[slug]/
video-studies/[slug]/frames/

Run /watch on the video. Read the frames and transcript it returns. Then
write the findings — do NOT just paste /watch's raw report.

Go through it in this order:

1. OVERVIEW
   - What is this video (type, length, source, who made it)?
   - What's it trying to do (teach, sell, demo, entertain)?

2. STRUCTURE & PACING
   - How is it organized — chapters, a single continuous demo, a narrative arc?
   - Pacing: how long before the hook/point lands? Any dead air or padding?

3. KEY MOMENTS (with timestamps)
   - The 3-8 moments actually worth remembering, each with a `t=MM:SS` and
     one or two sentences on why it matters.
   - For any moment worth a visual reference, save that frame:
     video-studies/[slug]/frames/NN-short-description.jpg (copy it out of
     /watch's tmp working dir before that dir gets cleaned up).

4. TECHNIQUE / PATTERN NOTES
   - Whatever the actual point of the study is — a UI flow, an ad structure,
     a presentation technique, a specific visual or audio trick. Describe the
     technique, not the content ("uses a before/after split-screen at 0:42 to
     contrast old vs new flow" — not what was said during it).

5. TAKEAWAYS
   - 2-4 bullet points: what's worth reusing or avoiding, and why.

Write the full structured write-up to video-studies/[slug]/findings.md — not
printed only in the terminal. Then add one row to the "Videos studied" table
in video-studies/SKILL.md: slug, source, type, and a one-line key takeaway.

Do not paste transcript excerpts beyond a short quote where the specific
wording is the finding (e.g. a CTA line). Do not reproduce the video's actual
narrative/content — describe technique and pattern only, same boundary as
site-studies/.
```

Result after running this once per video:

```
video-studies/
├── acme-onboarding-demo/
│   ├── findings.md
│   └── frames/
│       ├── 01-empty-state.jpg
│       └── 04-completion-screen.jpg
└── competitor-x-pricing-walkthrough/
    ├── findings.md
    └── frames/
```

---

## If /watch asks about transcription setup

Some videos have no native captions. When that happens `/watch` won't install
local Whisper or call a paid API on its own — it'll ask the user to choose
between installing local Whisper (free, one-time ~3GB download) or providing
a Groq/OpenAI API key (paid, no download), or skipping transcription for that
video. Handle that choice as it comes up, then re-run `/watch` and continue
the study. Frames alone are often enough for a technique/pattern study even
without a transcript.
