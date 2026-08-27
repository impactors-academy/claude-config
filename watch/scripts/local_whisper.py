#!/usr/bin/env python3
"""Local Whisper transcription — no API key, no per-minute cost.

Uses faster-whisper (a CTranslate2 reimplementation of Whisper — much faster
and lighter than the original openai-whisper pip package, same model
weights/quality). This is tried BEFORE any paid API fallback.

Model weights (~3 GB for large-v3, less for smaller sizes) download from
Hugging Face on first use and are cached under ~/.cache/huggingface —
after that first download, transcription is fully offline and free.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

DEFAULT_MODEL = "large-v3"
# int8 quantization cuts RAM roughly in half vs float32 with only a small
# accuracy cost — the safer default on memory-constrained machines. Override
# via WATCH_LOCAL_COMPUTE in ~/.config/watch/.env if more headroom exists.
DEFAULT_COMPUTE_TYPE = "int8"
DEFAULT_DEVICE = "auto"


def is_installed() -> bool:
    try:
        import faster_whisper  # noqa: F401
    except ImportError:
        return False
    return True


def install() -> tuple[bool, str]:
    """pip install faster-whisper for the current interpreter.

    Returns (ok, message). Never raises — a failure here just means the
    caller falls back to the paid API path.
    """
    cmd = [sys.executable, "-m", "pip", "install", "--quiet", "--user", "faster-whisper"]
    print("[watch] installing faster-whisper (local Whisper, one-time, ~a few hundred MB)…", file=sys.stderr)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return False, "pip install timed out after 600s"
    if result.returncode != 0:
        return False, (result.stderr or result.stdout or "unknown pip error").strip()[-800:]
    if not is_installed():
        return False, "pip reported success but faster_whisper still isn't importable"
    return True, "installed"


def transcribe_local(
    audio_path: Path,
    model_size: str = DEFAULT_MODEL,
    device: str = DEFAULT_DEVICE,
    compute_type: str = DEFAULT_COMPUTE_TYPE,
) -> list[dict]:
    """Transcribe with a local faster-whisper model. Returns {start, end, text} segments.

    First call with a given model_size downloads weights from Hugging Face
    (cached under ~/.cache/huggingface) — subsequent calls with the same
    model_size are fully offline. Raises RuntimeError on failure so the
    caller can fall back to the API path without crashing /watch.
    """
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError("faster-whisper is not installed") from exc

    print(
        f"[watch] loading local Whisper model ({model_size}, device={device}, "
        f"compute={compute_type})… first run downloads weights, cached after that",
        file=sys.stderr,
    )
    try:
        model = WhisperModel(model_size, device=device, compute_type=compute_type)
        segments_iter, _info = model.transcribe(str(audio_path), vad_filter=True)
        segments: list[dict] = []
        for seg in segments_iter:
            text = (seg.text or "").strip()
            if not text:
                continue
            segments.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "text": text})
    except Exception as exc:  # model load / inference failure — let caller fall back
        raise RuntimeError(f"local Whisper transcription failed: {exc}") from exc

    if not segments:
        raise RuntimeError("local Whisper returned no transcript segments")
    return segments


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: local_whisper.py <audio-path> [model_size]", file=sys.stderr)
        raise SystemExit(2)
    audio = Path(sys.argv[1])
    size = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_MODEL
    segs = transcribe_local(audio, model_size=size)
    import json
    print(json.dumps(segs, indent=2))
