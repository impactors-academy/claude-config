#!/usr/bin/env python3
"""Rebuild data/sanzo-wada-348.csv from the source PDF.

Usage:  python3 extract.py "A Dictionary of Color Combinations.pdf" [out.csv]

The HexPot edition stores every swatch as an uncompressed content-stream block:

    q
    1 0 -0 1 <tx> <ty> cm      <- translation = swatch origin (bottom-left)
    <r> <g> <b> scn            <- fill colour, 0..1 per channel
    <path ops> h
    f
    Q

so both the colour and the position are recoverable exactly — nothing here is
sampled, averaged or eyeballed. Three classes of fill are NOT swatches and are
excluded:

  * the page background      — width 2280 (the full MediaBox)
  * the footer logo          — width 236
  * hairline outlines        — a fill whose path closes more than one subpath.
    Exactly one exists (page 3): a 1px grey ring drawn behind a white swatch so
    that it stays visible on the white page. Treating it as a colour invented a
    phantom third member of that combination.

Verify the output with verify.py, which re-renders the PDF and samples the real
pixel at every swatch centre.
"""
import csv
import re
import sys

BLOCK = re.compile(
    r'1\.000000 0\.000000 -0\.000000 1\.000000 ([\d.-]+) ([\d.-]+) cm\s*\n'
    r'([\d.]+) ([\d.]+) ([\d.]+) scn\s*\n(.*?)\nf\b', re.S)


def hexof(r, g, b):
    return '#%02X%02X%02X' % tuple(round(float(v) * 255) for v in (r, g, b))


def swatches(pdf_bytes):
    """Yield (page, x, y, w, h, hex) for every real swatch, in draw order."""
    doc = pdf_bytes.decode('latin-1')
    streams = [m.group(1)
               for m in re.finditer(r'stream\n(.*?)endstream', doc, re.S)
               if 'scn' in m.group(1)]
    # streams[0:3] are the cover art and the two logo marks.
    for page_index, stream in enumerate(streams[3:]):
        for x, y, r, g, b, path in BLOCK.findall(stream):
            if path.count('\nh') > 1:          # compound path = outline, not a fill
                continue
            nums = [float(n) for n in re.findall(r'[\d.]+', path)]
            if not nums:
                continue
            w, h = max(nums[0::2]), max(nums[1::2])
            if not (60 < w < 220):             # page background / footer logo
                continue
            yield page_index + 2, float(x), float(y), w, h, hexof(r, g, b)


def combinations(pdf_bytes):
    """Group swatches into combinations: same row, horizontally adjacent."""
    by_page = {}
    for page, x, y, w, h, hx in swatches(pdf_bytes):
        by_page.setdefault(page, {}).setdefault(round(y, 1), []).append((x, hx, w))

    out = []
    for page in sorted(by_page):
        for y in sorted(by_page[page], reverse=True):     # top row first
            run, prev_x, prev_w = [], None, None
            for x, hx, w in sorted(by_page[page][y]):
                if prev_x is not None and x - prev_x > prev_w + 5:
                    out.append((page, run)); run = []
                run.append(hx); prev_x, prev_w = x, w
            if run:
                out.append((page, run))
    # A lone swatch is a stray layout element, not a combination (one exists).
    return [(p, c) for p, c in out if len(c) >= 2]


def main():
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else 'sanzo-wada-348.csv'
    combos = combinations(open(src, 'rb').read())

    with open(dst, 'w', newline='\n') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['id', 'page', 'n', 'c1', 'c2', 'c3', 'c4'])
        for i, (page, cols) in enumerate(combos, 1):
            w.writerow([i, page, len(cols)] + cols + [''] * (4 - len(cols)))

    sizes = {}
    for _, c in combos:
        sizes[len(c)] = sizes.get(len(c), 0) + 1
    print(f"{len(combos)} combinations -> {dst}")
    for n in sorted(sizes):
        print(f"  {n}-colour: {sizes[n]}")
    print(f"  swatches:  {sum(len(c) for _, c in combos)}")


if __name__ == '__main__':
    main()
