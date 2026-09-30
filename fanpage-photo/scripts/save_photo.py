#!/usr/bin/env python3
"""File a fan page photo into the backup repository with a source record.

Usage:
    python3 save_photo.py --page fans-of-cristiano-ronaldo \
        --file ~/Downloads/photo.jpg \
        --source-url "https://www.facebook.com/photo.php?fbid=..." \
        --player "Cristiano Ronaldo" [--note "solo, smiling"] [--move]

Result:
    <FANPAGES_DIR>/<page>/photoN.<ext>        the image, N = next free number
    <FANPAGES_DIR>/<page>/photoN.meta.json    where it came from and when

FANPAGES_DIR defaults to ~/MendDevs/Impactors Academy/content/fanpages (override with the
FANPAGES_DIR environment variable).
Photos are never deleted by this script. Without --move the original file is
left where it was.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ROOT = str(Path.home() / "MendDevs" / "Impactors Academy" / "content" / "fanpages")
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def next_number(folder: Path) -> int:
    highest = 0
    for p in folder.glob("photo*"):
        m = re.match(r"^photo(\d+)\.", p.name)
        if m:
            highest = max(highest, int(m.group(1)))
    return highest + 1


def main() -> int:
    ap = argparse.ArgumentParser(description="File a fan page photo with a source record")
    ap.add_argument("--page", required=True, help="fan page folder slug, e.g. fans-of-cristiano-ronaldo")
    ap.add_argument("--file", required=True, help="path to the downloaded image")
    ap.add_argument("--source-url", required=True, help="URL of the photo or post it came from")
    ap.add_argument("--player", required=True, help="whose official page it came from")
    ap.add_argument("--note", default="", help="free text, e.g. why it was chosen")
    ap.add_argument("--move", action="store_true", help="move the file instead of copying it")
    args = ap.parse_args()

    if not SLUG_RE.match(args.page):
        print(f"Error: page slug '{args.page}' must be lowercase letters, digits and dashes", file=sys.stderr)
        return 2

    src = Path(os.path.expanduser(args.file))
    if not src.is_file():
        print(f"Error: file not found: {src}", file=sys.stderr)
        return 2
    ext = src.suffix.lower()
    if ext not in IMAGE_EXTS:
        print(f"Error: '{ext}' is not an image type we file ({', '.join(sorted(IMAGE_EXTS))})", file=sys.stderr)
        return 2
    if not args.source_url.startswith(("http://", "https://")):
        print("Error: --source-url must be a full http(s) URL", file=sys.stderr)
        return 2

    root = Path(os.environ.get("FANPAGES_DIR", DEFAULT_ROOT))
    folder = root / args.page
    folder.mkdir(parents=True, exist_ok=True)

    digest = sha256(src)
    for meta_file in folder.glob("photo*.meta.json"):
        try:
            if json.loads(meta_file.read_text(encoding="utf-8")).get("sha256") == digest:
                print(f"Already filed as {meta_file.name.replace('.meta.json', '')} (same file). Nothing done.")
                return 0
        except (OSError, ValueError):
            continue

    n = next_number(folder)
    dest = folder / f"photo{n}{ext}"
    if args.move:
        shutil.move(str(src), dest)
    else:
        shutil.copy2(src, dest)

    meta = {
        "file": dest.name,
        "page": args.page,
        "player": args.player,
        "source_url": args.source_url,
        "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bytes": dest.stat().st_size,
        "sha256": digest,
        "note": args.note,
    }
    (folder / f"photo{n}.meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Saved: {dest}")
    print(f"Size: {meta['bytes']} bytes")
    print(f"Record: {folder / f'photo{n}.meta.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
