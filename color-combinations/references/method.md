# Method notes

Detail behind the steps in SKILL.md.

## Contrast thresholds worth memorising

| Ratio | Meaning |
|---|---|
| 3:1 | large text (≥24px, or ≥19px bold), UI component boundaries, focus rings |
| 4.5:1 | AA body text — the floor for anything a user must read |
| 7:1 | AAA body text — aim here for long-form copy |

A color's ratio is **not** a property of the color. It is a property of the pair.
`check` reports against black and white by default; add `+#HEX` for the surface you
actually ship on.

## Why one accent is never enough

Luminance is a single axis. A hex bright enough to sit on black is, by definition,
too bright to sit on cream. Concretely:

```
#C9885C  on #030303  →  7.03:1  AAA
#C9885C  on #F2EDE4  →  2.51:1  FAIL
```

So every brand color needs at least two shipped values. Name them by the surface
they belong to (`--brand` / `--brand-deep`), never by an aesthetic label like
"primary" and "secondary" — the latter tells nobody where it is safe to use.

## Picking a family for a set of categories

For ventures, chart series, tags, team colors — anything where N things need N
distinguishable colors. Draw them from a single Wada combination and filter:

```python
import sys; sys.path.insert(0, 'scripts')
from palette import load, contrast, to_lch, parse, swatch

GROUND = '#030303'
best = []
for c in load():
    cols = c["colors"]
    if len(cols) != 4:
        continue
    ratios = [contrast(x, GROUND) for x in cols]
    if min(ratios) < 4.5:                       # all must be legible on the ground
        continue
    hues = [to_lch(parse(x))[2] for x in cols]
    sep = min(min(abs(a - b), 360 - abs(a - b))
              for i, a in enumerate(hues) for b in hues[i + 1:])
    best.append((sep, c["id"], cols, ratios))

for sep, i, cols, r in sorted(best, reverse=True)[:8]:
    print(f"#{i:<4} hue-sep {sep:5.1f}  " + "".join(swatch(x) for x in cols))
```

Rules of thumb: hue separation ≥ 30° to be tellable apart, ≥ 50° to be tellable apart
*at a glance* or at small sizes. Never rely on hue alone — pair every category color
with a label, shape or position, because ~8% of men cannot separate red from green.

## Extracting a brand color from a logo

Do not trust the hex in the CSS. Sample the file:

```python
from PIL import Image
from collections import Counter
im = Image.open('logo.png').convert('RGB')
for col, n in Counter(im.getdata()).most_common(6):
    print('#%02X%02X%02X' % col, n)
```

Ignore anti-aliasing artefacts (low counts, values between two dominant colors). The
two or three colors with counts in the thousands are the real mark.

## Auditing an existing palette

```bash
cd <project>
grep -rohE "#[0-9a-fA-F]{6}\b" --include="*.css" --include="*.tsx" src | sort | uniq -c | sort -rn
```

The count column is the finding. Whatever is used most **is** the brand, regardless
of what the logo or the brand doc says. If those disagree, that is the bug — and it
is a hierarchy bug, not a hue bug. Fixing it means moving colors between roles, not
inventing new ones.

Then check where each is used: a color used as a background needs its foreground
verified, and a color used on multiple grounds probably needs splitting into a ramp.

## Re-extracting and verifying the dataset

```bash
python3 scripts/extract.py "references/A Dictionary of Color Combinations.pdf" data/sanzo-wada-348.csv
python3 scripts/verify.py  "references/A Dictionary of Color Combinations.pdf"
```

`extract.py` parses the PDF's uncompressed content streams — each swatch is a
`q … cm / r g b scn / path / f / Q` block, so the fill color and the translation are
both recoverable exactly. Nothing is sampled or averaged. Four classes of fill are
excluded:

| Fill | Test | Why |
|---|---|---|
| Page background | width 2280 | the full MediaBox |
| Footer logo | width 236 | HexPot's mark, on every page |
| Hairline outline | path closes >1 subpath | a drawn border, not a color |
| Orphan swatch | group of 1 | a stray element on page 7 |

Result: exactly 348 — 120 two-color, 120 three-color, 108 four-color, 1032 swatches.

### Why the outline rule matters

Page 3 carries a white swatch, which would be invisible on a white page, so the
designer drew a 1px grey ring behind it. In the content stream that ring is just
another fill, and a naive parser reads `#979797` as a third color in the plate. It
gives itself away geometrically: it closes many subpaths, where a real swatch closes
exactly one.

**The count did not catch this.** The total was 348 either way — the phantom simply
moved one plate from the two-color set into the three-color set. Only rendering the
PDF and sampling the actual pixel found it.

### Why verification is a separate step

Parsing tells you what a PDF *contains*; it does not tell you what it *renders*. A
fill can be clipped, hidden behind another, or painted over. `verify.py` re-renders
the PDF with Ghostscript at 72dpi — where one PDF unit is one pixel, so a swatch's
centre maps directly, remembering that PDF y-origin is bottom-left and raster
y-origin is top-left — and compares the real pixel at every swatch centre against the
CSV. Current state: 1032/1032 exact, 0 mismatches.

Apply the same discipline to any data you extract from a rendered format. If you have
not compared against the rendering, you have a plausible parse, not a verified one.
