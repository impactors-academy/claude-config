#!/usr/bin/env python3
"""Prove data/sanzo-wada-348.csv matches the PDF, pixel for pixel.

Usage:  python3 verify.py "A Dictionary of Color Combinations.pdf" [data.csv]

Parsing a PDF's content streams is not the same as knowing what it renders: a
fill can be hidden, clipped, or drawn over. So this renders the PDF with
Ghostscript at 72dpi (where 1 PDF unit == 1 pixel) and samples the real pixel at
the centre of every swatch the extractor claims exists, then compares the whole
sequence against the CSV.

Requires ghostscript on PATH and Pillow.
"""
import csv
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import swatches, combinations  # noqa: E402


def main():
    src = sys.argv[1]
    data = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'sanzo-wada-348.csv')
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow is required: pip install pillow")

    pdf = open(src, 'rb').read()
    tmp = tempfile.mkdtemp()
    subprocess.run(
        ['gs', '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=png16m', '-r72',
         f'-sOutputFile={tmp}/p%02d.png', src],
        check=True, capture_output=True)

    pages, checked, bad = {}, 0, []
    for page, x, y, w, h, hx in swatches(pdf):
        if page not in pages:
            pages[page] = Image.open(f'{tmp}/p{page:02d}.png').convert('RGB')
        im = pages[page]
        # PDF origin is bottom-left; raster origin is top-left.
        px = im.getpixel((int(round(x + w / 2)), int(round(im.size[1] - (y + h / 2)))))
        got = '#%02X%02X%02X' % px
        checked += 1
        if got != hx:
            bad.append((page, round(x), round(y), hx, got))

    print(f"swatches sampled from the rendered PDF : {checked}")
    print(f"exact RGB matches                      : {checked - len(bad)}")
    print(f"mismatches                             : {len(bad)}")
    for b in bad[:20]:
        print("   page %d @ (%d,%d): extracted %s, rendered %s" % b)

    rows = list(csv.DictReader(open(data)))
    csv_seq = [c for r in rows for c in (r['c1'], r['c2'], r['c3'], r['c4']) if c]
    derived = [c for _, combo in combinations(pdf) for c in combo]
    same = csv_seq == derived
    sizes = {}
    for r in rows:
        sizes[int(r['n'])] = sizes.get(int(r['n']), 0) + 1

    print(f"\nCSV combinations                       : {len(rows)}"
          f"  ({', '.join(f'{v}x{k}-colour' for k, v in sorted(sizes.items()))})")
    print(f"CSV colour values                      : {len(csv_seq)}")
    print(f"CSV identical to re-extraction         : {same}")

    ok = not bad and same and len(rows) == 348
    print("\n" + ("PASS — the CSV is the PDF." if ok else "FAIL — see above."))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
