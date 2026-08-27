---
name: watch
version: "0.3.0"
description: Watch a video (URL or local path). Downloads with yt-dlp, extracts auto-scaled frames with ffmpeg, pulls the transcript from captions (or local Whisper, or Whisper API as a last resort), and hands the result to Claude so it can answer questions about what's in the video.
argument-hint: "<video-url-or-path> [question]"
allowed-tools: Bash, Read, AskUserQuestion
homepage: https://github.com/bradautomates/claude-video
repository: https://github.com/bradautomates/claude-video
author: bradautomates
license: MIT
user-invocable: true
---

> **Impactors Academy fork note:** upstream falls back straight to the paid
> Whisper API when captions are missing. This copy adds a free local
> `faster-whisper` option (`scripts/local_whisper.py`, new) and, more
> importantly, never installs anything or calls a paid API without asking
> first — when a video has no captions, the user is asked to choose between
> local Whisper (free, one-time download) and an API key (paid, no download)
> before either happens. See "Transcription consent" below and `CREDIT.md`
> in the repo root for upstream attribution.

# /watch

You don't have a video input; this skill gives you one. A Python script gets captions first, optionally downloads the video, extracts frames as JPEGs (scene-aware, or fast keyframes at `efficient` detail), gets a timestamped transcript (native captions first, then local Whisper, then the Whisper API as a last resort), and prints frame paths. You then `Read` each frame path to see the images and combine them with the transcript to answer the user.

## Resolve `SKILL_DIR` (do this before any command)

Every `python3 ...` command below runs a bundled script under `SKILL_DIR/scripts/`. Set `SKILL_DIR` to the **absolute path of the directory containing THIS SKILL.md you just Read** — your harness told you that path in the Read result. The scripts are always a direct sibling of this file (`SKILL_DIR/scripts/watch.py`), in every install layout:

```
Read ~/.claude/plugins/cache/claude-video/watch/<ver>/skills/watch/SKILL.md → SKILL_DIR=…/skills/watch
Read ~/.codex/skills/watch/SKILL.md                                          → SKILL_DIR=~/.codex/skills/watch
Read ~/.agents/skills/watch/SKILL.md                                         → SKILL_DIR=~/.agents/skills/watch
```

Substitute that literal path for `${SKILL_DIR}` in every command. This works on every harness (Claude Code, Codex, Cursor, Gemini CLI, …) without relying on any harness-specific environment variable. Guard once at the start of a run:

```bash
SKILL_DIR="<absolute path of the directory containing the SKILL.md you Read>"
if [ ! -f "$SKILL_DIR/scripts/watch.py" ]; then
  echo "ERROR: scripts/watch.py not found under SKILL_DIR=$SKILL_DIR" >&2
  echo "Re-check the directory of the SKILL.md you Read and substitute it as SKILL_DIR." >&2
  exit 1
fi
```

## Step 0 — Setup preflight (runs every `/watch` invocation, silent on success)

**Python interpreter:** every `python3 ...` command in this skill is for macOS/Linux. On **Windows**, substitute `python` — the `python3` command on Windows is the Microsoft Store stub and will not run the script.

This step is about `ffmpeg`/`ffprobe`/`yt-dlp` only — those are needed for /watch to work at all and cost nothing but a small download. It has nothing to do with transcription; local Whisper and API keys are handled later, per-video, only when a specific video turns out to have no captions (see "Transcription consent" below).

On the first `/watch` invocation in a session:

```bash
python3 "${SKILL_DIR}/scripts/setup.py" --check
```

This is a <100ms lookup. Exit 0 means the binaries are present — proceed to Step 1 without comment, no output to announce. On exit 2, run the installer:

```bash
python3 "${SKILL_DIR}/scripts/setup.py"
```

On macOS with Homebrew, it auto-installs `ffmpeg` and `yt-dlp` and scaffolds `~/.config/watch/.env` (mode `0600`). On Linux/Windows, it prints the exact install commands for the user to run themselves.

**First-run watch preference:** the first time the installer creates `~/.config/watch/.env` in a session, use `AskUserQuestion` to ask one question about default frame detail:

- Present these as `AskUserQuestion` options in this exact order — lightest to heaviest — and keep `(recommended)` on `balanced` even though it is not first (do **not** reorder to put the recommended option first):
  - `transcript` — no frames at all, transcript only (skips video download when captions exist).
  - `efficient` — fast keyframe pass (cap 50).
  - `balanced` (recommended) — scene-aware frames (cap 100, default).
  - `token-burner` — scene-aware, uncapped (maximum fidelity; high token cost).

Write the answer directly into `~/.config/watch/.env` by setting the bare key on its own line — **no trailing inline comment** (a `# note` after the value can break parsing):

```bash
WATCH_DETAIL=balanced
```

Use the user's selected value. If they skip the question, keep the recommended default. Do not ask this preference question again once it's been set.

Within a single session, you can skip Step 0 on follow-up `/watch` calls — once `--check` returned 0, nothing about the environment changes between turns.

## Transcription consent (only when a video actually has no captions)

Local Whisper and the paid Whisper API are **never** touched proactively — not during Step 0, not in the background, not "just in case." Both cost the user something real: local Whisper is a one-time ~3GB download, the API costs real money per minute. Neither happens without the user saying yes to that specific video.

Here's how it plays out mechanically:

1. You run `watch.py` as normal (Step 1 below). If the video has captions, transcription never comes up — nothing to do here.
2. If the video has **no captions** and neither local Whisper nor an API key is already configured, `watch.py` does not install or call anything. Its stdout report contains a `> **TRANSCRIPTION_CONSENT_NEEDED**` block laying out the same three options below. Its stderr also prints a one-line version. Frames (if any) are still returned — you already have a usable result even before this is resolved.
3. Ask the user with `AskUserQuestion` — three options, this order:
   - **Local Whisper (recommended if they're not in a hurry)** — free forever, no API key, but a one-time ~3GB download of the `large-v3` model on the first video that needs it (cached after that, fully offline from then on).
   - **API key (Groq or OpenAI)** — no download, instant, but costs a small amount per minute of audio (Groq ≈ $0.04/hour, OpenAI ≈ $0.36/hour — pennies at normal usage, but real money).
   - **Skip — frames only** — proceed without a transcript for this video (or pass `--no-whisper` going forward to stop being asked).
4. Act on the answer:
   - **Local Whisper** → run `python3 "${SKILL_DIR}/scripts/setup.py" --install-local-whisper`, then re-run the exact same `/watch` command (the ~3GB download happens transparently on that re-run, as part of the transcription attempt).
   - **API key** → ask which provider (Groq preferred — cheaper, faster) if they didn't already say, then `AskUserQuestion` or otherwise get the key value, write it into `~/.config/watch/.env` as `GROQ_API_KEY=...` or `OPENAI_API_KEY=...`, then re-run the same `/watch` command.
   - **Skip** → proceed with the frames-only result already in hand. If they want this to stop being asked every time, offer to add `--no-whisper` to future calls or set `WATCH_LOCAL_WHISPER=false` in `.env` (only if they ask for that — don't default to silencing it).

Once local Whisper is installed or a key is set, it's used automatically on every future video with no captions — this consent step only fires again if that configuration is later removed. `has_local_whisper` / `has_api_key` in `setup.py --json`'s output tell you what's already configured, if you want to check proactively rather than waiting for the report.

**Structured mode (optional):** `python3 "${SKILL_DIR}/scripts/setup.py" --json` emits `{status, can_proceed, first_run, setup_complete, missing_binaries, has_local_whisper, whisper_backend, has_api_key, config_file, watch_detail, platform}`. `can_proceed` here is about binaries only, per Step 0 above — `has_local_whisper`/`has_api_key` are informational, not gates.

## When to use

- User pastes a video URL (YouTube, Vimeo, X, TikTok, Twitch clip, most yt-dlp-supported sites) and asks about it.
- User points at a local video file (`.mp4`, `.mov`, `.mkv`, `.webm`, etc.) and asks about it.
- User types `/watch <url-or-path> [question]`.

## Recommended limits

- **Best accuracy: videos under 10 minutes.** Frame coverage scales inversely with duration.
- **Universal rate cap: 2 fps.** The script never samples faster than 2 fps, even when a budget or `--fps` would imply more.
- **The frame ceiling is set by the detail mode** (`WATCH_DETAIL` in `~/.config/watch/.env`, or `--detail`), not a single global cap:
  - `transcript` → no frames
  - `efficient` → up to **50** (keyframes)
  - `balanced` (default) → up to **100** (scene-aware)
  - `token-burner` → **uncapped** (scene-aware; a soft warning prints past 250 frames)
  - `--max-frames N` overrides whichever cap the mode would otherwise use.
- **Full-video frame budget by duration.** Token cost grows with frame count, so the script targets a budget by duration. This budget sets the fps and the uniform-sampling fallback; scene-aware selection can fill up to the detail cap above, whichever is lower:
  - ≤30s → ~12-30 frames
  - 30s-1min → ~40 frames
  - 1-3min → ~60 frames
  - 3-10min → ~80 frames
  - \>10min → up to the detail cap, sparsely spaced (warning printed)
- If the user hands you a long video, consider asking whether they want a specific section before burning tokens on a sparse scan.

## How to invoke

**Step 1 — parse the user input.** Separate the video source (URL or path) from any question the user asked. Example: `/watch https://youtu.be/abc what language is this in?` → source = `https://youtu.be/abc`, question = `what language is this in?`.

**Step 2 — run the watch script.** Pass the source verbatim. Do not shell-escape it yourself beyond normal quoting:

```bash
python3 "${SKILL_DIR}/scripts/watch.py" "<source>"
```

Optional flags:
- `--detail transcript|efficient|balanced|token-burner` — fidelity/speed dial. `transcript` = no frames (transcript only, skips video download when captions exist); `efficient` = fast keyframes (cap 50); `balanced` = scene-aware frames (cap 100); `token-burner` = scene-aware, uncapped.
- `--start T` / `--end T` — focus on a section. Accepts `SS`, `MM:SS`, or `HH:MM:SS`. When either is set, fps auto-scales denser (see "Focusing on a section" below).
- `--timestamps T1,T2,…` — grab a frame at each of these absolute timestamps (`SS`, `MM:SS`, or `HH:MM:SS`). Use this after reading the transcript to capture deictic moments the presenter flags ("look here", "as you can see", "notice this") that visual selection alone may miss. See "Transcript-cue frames" below.
- `--max-frames N` — override the preset cap for tighter token budget (e.g. `--max-frames 40`)
- `--resolution W` — change frame width in px (default 512; bump to 1024 only if the user needs to read on-screen text)
- `--fps F` — override auto-fps (clamped to 2 fps max)
- `--out-dir DIR` — keep working files somewhere specific (default: an auto-generated tmp dir)
- `--whisper local|groq|openai` — force a specific transcription backend (default: prefer local Whisper, then Groq, then OpenAI)
- `--no-local-whisper` — skip the local Whisper attempt and go straight to the API fallback (e.g. if the local model would be too slow for a quick answer)
- `--no-whisper` — disable transcription fallback entirely (frames-only if no captions)
- `--no-dedup` — keep near-duplicate frames. By default a frame-delta pass drops frames that are visually near-identical to the previous kept one (held slides, static screen recordings, paused video) so the frame budget goes to distinct content; the report's **Frames** line notes how many were dropped. Pass this only if the user needs every sampled frame (e.g. judging subtle frame-to-frame motion).

### Focusing on a section (higher frame rate)

When the user asks about a specific moment — "what happens at the 2 minute mark?", "zoom into 0:45 to 1:00", "the first 10 seconds" — pass `--start` and/or `--end`. The script switches to focused-mode budgets, which are denser than full-video budgets (still capped at 2 fps, and still bounded by the detail-mode cap — the counts below assume the default `balanced` cap of 100; `efficient` tops out at 50):

- ≤5s → 2 fps (up to 10 frames)
- 5-15s → 2 fps (up to 30 frames)
- 15-30s → ~2 fps (up to 60 frames)
- 30-60s → ~1.3 fps (up to 80 frames)
- 60-180s → ~0.6 fps (100 frames, capped)

Focused mode is the right call for:
- Any moment/range the user names explicitly ("around 2:30", "the intro", "the last 30 seconds").
- Any video longer than ~10 minutes where the user's question is about a specific part — running focused on the relevant section is far more useful than a sparse scan of the whole thing.
- Re-runs after a full scan didn't have enough detail in some region.

Transcript is auto-filtered to the same range. Frame timestamps are absolute (real video timeline, not offset-from-start).

Examples:
```bash
# Last 10 seconds of a 1 minute video
python3 "${SKILL_DIR}/scripts/watch.py" video.mp4 --start 50 --end 60

# Zoom into 2:15 → 2:45 at 2 fps (60 frames)
python3 "${SKILL_DIR}/scripts/watch.py" "$URL" --start 2:15 --end 2:45 --fps 2

# From 1h12m to the end of the video
python3 "${SKILL_DIR}/scripts/watch.py" "$URL" --start 1:12:00
```

**Step 3 — Read every frame path the script lists.** The Read tool renders JPEGs directly as images for you. Read all frames in a single message (parallel tool calls) so you see them together. The frames are in chronological order with a `t=MM:SS` timestamp so you can align them to the transcript.

**Step 4 — answer the user.** You now have two streams of evidence:
- **Frames** — what's on screen at each timestamp
- **Transcript** — what's said at each timestamp. The report's header shows the source (`captions` = yt-dlp pulled native subs; `whisper (groq)` or `whisper (openai)` = transcribed by API).

If the user asked a specific question, answer it directly citing timestamps. If they didn't ask anything, summarize what happens in the video — structure, key moments, notable visuals, spoken content.

This holds for `transcript` detail too: even with no frames, produce a **summary** like the other modes — do not paste the full transcript into chat. Synthesize structure, key moments, and spoken content with timestamps; quote only the lines that matter. Offer the raw transcript only if the user explicitly asks for it.

**Step 5 — clean up.** The script prints a working directory at the end. If the user isn't going to ask follow-ups about this video, delete it with `rm -rf <dir>`. If they might, leave it in place.

## Detail and frames

Default behavior comes from `~/.config/watch/.env`:

- `WATCH_DETAIL=transcript|efficient|balanced|token-burner` (default: `balanced`)

At `transcript` detail, captions are enough to return a report without downloading video. If captions are missing, the script downloads audio only and tries Whisper. If no transcript can be produced, it reports the limitation clearly; re-run with `--detail balanced` for frames.

At `efficient` detail, the script downloads the video and extracts **keyframes only** (`ffmpeg -skip_frame nokey`) — a near-instant pass that lands frames on scene cuts. If a clip has fewer than 4 keyframes it falls back to uniform sampling.

At `balanced` / `token-burner` detail, the script extracts **scene-aware** frames: ffmpeg scene-change selection first, falling back to uniform sampling only when the video is effectively static. `balanced` caps at 100 frames; `token-burner` is uncapped. Frame report lines include both timestamp and selection reason. Extracted images are clamped to a maximum 1998px height for Claude Read compatibility.

## Transcript-cue frames

Visual frame selection (scene/keyframe) can miss the moments a presenter explicitly flags — "look here", "as you can see", "notice this", "watch what happens" — because pointing at a slide is often a *low* visual change. `--timestamps` lets you force a frame at those exact moments. **You** decide which moments matter, by reading the transcript:

1. Run once at `--detail transcript` (or any detail) to get the timestamped transcript.
2. Scan it for deictic cues — phrases where the speaker directs attention to something on screen. This is a judgment call (ignore rhetorical "look, the point is…"); that's why it's done by you, not a regex.
3. Re-run with `--timestamps 4:32,7:10,9:55` (absolute source times). For a URL, point the second run at the **downloaded local file** in the work dir so it doesn't re-download.

Behavior:
- **Additive by default.** Cue frames (`reason=transcript-cue`) are merged into whatever `--detail` already selected, in chronological order.
- **Pinned and counted first.** Cue frames are reserved against the frame cap before the detail engine runs, so they're never evicted by even-sampling.
- **Honors focus mode.** With `--start/--end`, any cue timestamp outside the window is dropped (reported in the summary). Coordinates are always absolute source time.
- **Cue-only frames.** `--detail transcript --timestamps …` skips scene/keyframe sampling and returns *only* the cue frames (it will download the video to do so, since frames need pixels).

## Transcription

The script gets a timestamped transcript in one of three ways, tried in order:

1. **Native captions (free, preferred).** yt-dlp pulls manual or auto-generated subtitles from the source platform if available.
2. **Local Whisper (free, no key, tried first when captions are missing AND already installed).** `watch.py` never installs this itself — it only uses `faster-whisper` if it's already there, which only happens after the user has explicitly agreed via the consent flow above and `setup.py --install-local-whisper` has run. Once installed, it transcribes on this machine with the `large-v3` model — the same weights the paid API runs, at zero per-minute cost. First use with a given model downloads weights from Hugging Face (~3GB for `large-v3`, this is the download the user already consented to) and caches them under `~/.cache/huggingface`; every run after that is fully offline. Default compute type is `int8` (lower RAM, small accuracy tradeoff) — override with `WATCH_LOCAL_COMPUTE=float16` or `float32` in `~/.config/watch/.env` if there's RAM to spare. Skip this path with `--no-local-whisper` or `WATCH_LOCAL_WHISPER=false`.
3. **Whisper API fallback (only if local Whisper isn't installed, and only if a key is already in `.env`).** `watch.py` never asks the user for a key itself — it only uses one that's already been written to `~/.config/watch/.env` (again, only after consent). If present, the script extracts audio (`ffmpeg -vn -ac 1 -ar 16000 -b:a 64k`, ~0.5 MB/min) and uploads it:
   - **Groq** — `whisper-large-v3`. Preferred default: cheaper, faster. Get a key at console.groq.com/keys.
   - **OpenAI** — `whisper-1`. Fallback. Get a key at platform.openai.com/api-keys.

Both keys live in `~/.config/watch/.env`, only consulted once local Whisper is unavailable. The script prefers local, then Groq, then OpenAI; override with `--whisper local|groq|openai` to force a specific one. Use `--no-whisper` to skip transcription entirely. If a video has no captions and neither local Whisper nor a key is configured, the script installs/calls nothing and instead reports `TRANSCRIPTION_CONSENT_NEEDED` — see "Transcription consent" above.

## Failure modes and handling

- **Setup preflight failed** → run `python3 "${SKILL_DIR}/scripts/setup.py"` (auto-installs ffmpeg/yt-dlp via brew on macOS, scaffolds the `.env`). This never touches transcription — see the consent flow above for that.
- **No transcript available, consent needed** → captions missing AND neither local Whisper nor an API key configured. This is expected, not an error — follow "Transcription consent" above rather than treating it as a failure.
- **Local Whisper is slow** → CPU transcription of a long video can take a while (no GPU acceleration on most dev machines). If a quick answer matters more than avoiding API cost, pass `--no-local-whisper` to go straight to Groq/OpenAI (which transcribes in seconds) — but only if a key is already configured; otherwise this still needs the consent flow.
- **Long video warning printed** → acknowledge it in your answer. Offer to re-run focused on a specific section via `--start`/`--end` rather than a sparse full-video scan.
- **Download fails** → yt-dlp's error goes to stderr. If it's a login-required or region-locked video, tell the user plainly; do not keep retrying.
- **Whisper API request fails** → the error is printed to stderr (likely: invalid key or rate limit). Audio over the API's 25 MB upload cap is split into chunks and transcribed automatically, so length alone won't fail it; if some chunks fail the transcript is partial and the dropped chunks are noted on stderr. The report will say "none available" only if every chunk fails. You can retry with `--whisper openai` if Groq failed (or vice versa).

## Token efficiency

This skill burns tokens primarily on frames. Order of magnitude:
- 80 frames at 512px wide is roughly 50-80k image tokens depending on aspect ratio.
- The transcript is cheap (a few thousand tokens at most for a 10-minute video).
- Bumping `--resolution` to 1024 roughly quadruples the image tokens per frame. Only do it when necessary.

If you already watched a video this session and the user asks a follow-up, do **not** re-run the script — you already have the frames and transcript in context. Just answer from what you have.

## Security & Permissions

**What this skill does:**
- Runs `yt-dlp` locally to download the video and pull native captions when the source supports them (public data; the request goes directly to whatever host the URL points at)
- Runs `ffmpeg` / `ffprobe` locally to extract frames as JPEGs and, when transcription is needed, a mono 16 kHz audio clip
- Installs `faster-whisper` via `pip install --user`, but **only** when the user has explicitly agreed via `setup.py --install-local-whisper` — never automatically, never as part of Step 0. Once installed, transcribes locally when captions are missing — this downloads model weights from Hugging Face on first use (`huggingface.co`, cached under `~/.cache/huggingface`) but sends no audio anywhere; transcription happens entirely on this machine
- Sends the extracted audio clip to Groq's Whisper API (`api.groq.com/openai/v1/audio/transcriptions`) when local Whisper isn't installed and `GROQ_API_KEY` is already set in `.env` (never asks for one itself — see "Transcription consent" above)
- Sends the extracted audio clip to OpenAI's audio transcription API (`api.openai.com/v1/audio/transcriptions`) when local Whisper isn't available, `OPENAI_API_KEY` is already set and Groq is not, or when `--whisper openai` is forced
- Writes the downloaded video, frames, audio, and an intermediate transcript to a working directory under the system temp dir (or `--out-dir` if specified) so Claude can `Read` them
- Reads / creates `~/.config/watch/.env` (mode `0600`) to store the Whisper API key(s) and a `SETUP_COMPLETE` marker. As a fallback, also reads `.env` in the current working directory

**What this skill does NOT do:**
- Does not upload the video itself to any API — only the extracted audio goes out, and only when native captions are missing, local Whisper is unavailable, AND transcription is not disabled with `--no-whisper`
- Does not send audio anywhere at all for local transcription — `faster-whisper` runs the model on-device; only the one-time model weight download touches the network
- Does not access any platform account (no login, no session cookies, no posting) — yt-dlp only ever requests public data
- Does not share API keys between providers (Groq key only goes to `api.groq.com`, OpenAI key only goes to `api.openai.com`)
- Does not log, cache, or write API keys to stdout, stderr, or output files
- Does not persist anything outside the working directory, `~/.config/watch/.env`, and `~/.cache/huggingface` (local model weights) — clean up the working directory when you're done (Step 5)

**Bundled scripts:** `scripts/watch.py` (entry point), `scripts/download.py` (yt-dlp wrapper), `scripts/frames.py` (ffmpeg frame extraction), `scripts/transcribe.py` (caption parsing), `scripts/local_whisper.py` (local faster-whisper transcription — tried first), `scripts/whisper.py` (Groq / OpenAI API clients — fallback), `scripts/setup.py` (preflight + installer)

Review scripts before first use to verify behavior.
