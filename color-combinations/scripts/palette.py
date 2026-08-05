#!/usr/bin/env python3
"""Query Sanzo Wada's 348 combinations and check any palette against WCAG.

Stdlib only. Run `palette.py help` for usage.
"""
import csv
import math
import os
import sys

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "sanzo-wada-348.csv")


# ── color space ────────────────────────────────────────────────────────────
def parse(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def fmt(rgb):
    return "#%02X%02X%02X" % rgb


def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (_lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    """WCAG 2.1 contrast ratio between two hex colors."""
    la, lb = luminance(parse(a)), luminance(parse(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def to_lab(rgb):
    r, g, b = (_lin(c) for c in rgb)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 1.00000
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else (7.787 * t + 16 / 116)
    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def to_lch(rgb):
    L, a, b = to_lab(rgb)
    h = math.degrees(math.atan2(b, a)) % 360
    return (L, math.hypot(a, b), h)


def de2000(c1, c2):
    """CIEDE2000 perceptual distance between two RGB tuples."""
    L1, a1, b1 = to_lab(c1)
    L2, a2, b2 = to_lab(c2)
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7))) if Cb > 0 else 0
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if (a1p or b1) else 0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if (a2p or b2) else 0
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0
    elif abs(h2p - h1p) <= 180:
        dhp = h2p - h1p
    else:
        dhp = h2p - h1p - 360 if h2p > h1p else h2p - h1p + 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp) / 2)
    Lbp = (L1 + L2) / 2
    Cbp = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hbp = (h1p + h2p + 360) / 2
    else:
        hbp = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hbp - 30))
         + 0.24 * math.cos(math.radians(2 * hbp))
         + 0.32 * math.cos(math.radians(3 * hbp + 6))
         - 0.20 * math.cos(math.radians(4 * hbp - 63)))
    dTh = 30 * math.exp(-(((hbp - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7)) if Cbp > 0 else 0
    Sl = 1 + (0.015 * (Lbp - 50) ** 2) / math.sqrt(20 + (Lbp - 50) ** 2)
    Sc = 1 + 0.045 * Cbp
    Sh = 1 + 0.015 * Cbp * T
    Rt = -math.sin(math.radians(2 * dTh)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2
                     + Rt * (dCp / Sc) * (dHp / Sh))


# ── data ───────────────────────────────────────────────────────────────────
def load():
    with open(DATA) as f:
        return [{"id": int(r["id"]), "page": int(r["page"]),
                 "colors": [r[k] for k in ("c1", "c2", "c3", "c4") if r[k]]}
                for r in csv.DictReader(f)]


def swatch(h):
    r, g, b = parse(h)
    return f"\033[48;2;{r};{g};{b}m   \033[0m"


def render(colors):
    return "".join(swatch(c) for c in colors) + "  " + " ".join(colors)


# ── commands ───────────────────────────────────────────────────────────────
def cmd_near(args):
    """near <hex> [count] — closest colors in the book to a target."""
    target = parse(args[0])
    n = int(args[1]) if len(args) > 1 else 12
    seen = {}
    for combo in load():
        for c in combo["colors"]:
            seen.setdefault(c, de2000(target, parse(c)))
    for c, d in sorted(seen.items(), key=lambda kv: kv[1])[:n]:
        L, C, H = to_lch(parse(c))
        print(f"{swatch(c)} {c}  dE {d:5.1f}   L {L:5.1f}  C {C:5.1f}  H {H:5.1f}")


def cmd_with(args):
    """with <hex> [--tol N] [--n 2|3|4] — combos containing a near-match color."""
    target = parse(args[0])
    tol = 12.0
    size = None
    for i, a in enumerate(args):
        if a == "--tol":
            tol = float(args[i + 1])
        if a == "--n":
            size = int(args[i + 1])
    hits = []
    for combo in load():
        if size and len(combo["colors"]) != size:
            continue
        best = min((de2000(target, parse(c)), c) for c in combo["colors"])
        if best[0] <= tol:
            hits.append((best[0], combo))
    hits.sort(key=lambda t: t[0])
    print(f"{len(hits)} combos within dE {tol:g} of {fmt(target)}\n")
    for d, combo in hits:
        print(f"#{combo['id']:<4} dE {d:4.1f}  {render(combo['colors'])}")


def cmd_check(args):
    """check <hex>... — WCAG contrast of each color against common surfaces."""
    surfaces = [("black #030303", "#030303"), ("white #FFFFFF", "#FFFFFF")]
    extra = [a for a in args if a.startswith("+")]
    cols = [a for a in args if not a.startswith("+")]
    surfaces += [(s[1:], s[1:]) for s in extra]
    w = max(len(n) for n, _ in surfaces)
    for c in cols:
        print(f"\n{swatch(c)} {c}")
        for name, s in surfaces:
            r = contrast(c, s)
            tag = ("AAA" if r >= 7 else "AA" if r >= 4.5 else
                   "AA-large" if r >= 3 else "FAIL")
            print(f"   vs {name:<{w}}  {r:5.2f}:1  {tag}")


def cmd_pair(args):
    """pair <hex> <hex> — contrast ratio between two colors."""
    r = contrast(args[0], args[1])
    print(f"{swatch(args[0])}{swatch(args[1])}  {args[0]} on {args[1]}: {r:.2f}:1")


def cmd_scale(args):
    """scale <hex> [steps] — perceptually even tint/shade ramp through OKLab-ish L."""
    base = parse(args[0])
    steps = int(args[1]) if len(args) > 1 else 9
    L, a, b = to_lab(base)
    out = []
    for i in range(steps):
        t = 95 - (90 * i / (steps - 1))
        rgb = at_lightness(base, t)
        out.append(fmt(rgb))
    for i, c in enumerate(out):
        print(f"{swatch(c)} {i * 100 if i else 50:>4}  {c}   L {to_lch(parse(c))[0]:5.1f}")


# ── deriving variants ──────────────────────────────────────────────────────
def at_lightness(rgb, target_L):
    """Same hue and (scaled) chroma at a new CIE lightness."""
    L, a, b = to_lab(rgb)
    if L <= 0:
        L = 0.001
    # Chroma has to shrink as we approach either end or the color clips.
    damp = 1 - abs(target_L - L) / 160
    lin = _lab_to_rgb(target_L, a * damp, b * damp)
    return tuple(min(255, max(0, round(_srgb(v)))) for v in lin)


def variant_for(hexcolor, surface, target=4.5):
    """Nearest-lightness version of a color that clears `target` on `surface`.

    Returns (hex, ratio) or (None, best_ratio) when even black/white can't.
    """
    base = parse(hexcolor)
    if contrast(hexcolor, surface) >= target:
        return hexcolor, contrast(hexcolor, surface)
    start = to_lab(base)[0]
    best = (None, 0.0)
    # Walk outward from the original lightness in both directions.
    for step in range(1, 101):
        for L in (start - step, start + step):
            if not 0 <= L <= 100:
                continue
            cand = fmt(at_lightness(base, L))
            r = contrast(cand, surface)
            if r > best[1]:
                best = (cand, r)
            if r >= target:
                return cand, r
    return (None, best[1]) if best[1] < target else best


# CIELAB hue angles, not HSL — they differ enough that HSL centres misfile deep
# blues as purple.
HUES = [("red", 30), ("orange", 55), ("yellow", 95), ("green", 135),
        ("teal", 195), ("blue", 280), ("purple", 320), ("pink", 355)]


def hue_name(rgb):
    L, C, H = to_lch(rgb)
    if C < 18:
        return "neutral"
    if C < 45 and 20 <= H <= 90 and L < 70:
        return "brown"
    best, bd = "red", 999
    for name, centre in HUES:
        d = min(abs(H - centre), 360 - abs(H - centre))
        if d < bd:
            best, bd = name, d
    return best


def cmd_browse(args):
    """browse [--n 2|3|4] [--hue NAME] [--on HEX] [--limit N] — explore the book."""
    size = hue = None
    ground = None
    limit = 25
    for i, a in enumerate(args):
        if a == "--n":
            size = int(args[i + 1])
        if a == "--hue":
            hue = args[i + 1].lower()
        if a == "--on":
            ground = args[i + 1]
        if a == "--limit":
            limit = int(args[i + 1])
    shown = 0
    for combo in load():
        cols = combo["colors"]
        if size and len(cols) != size:
            continue
        if hue and not any(hue_name(parse(c)) == hue for c in cols):
            continue
        if ground and min(contrast(c, ground) for c in cols) < 4.5:
            continue
        names = "/".join(sorted({hue_name(parse(c)) for c in cols}))
        print(f"#{combo['id']:<4} {render(cols)}   {names}")
        shown += 1
        if shown >= limit:
            break
    print(f"\n{shown} shown"
          + (f" · all members ≥4.5:1 on {ground}" if ground else "")
          + " · use `show <id>` or `tokens <id>` next")


def cmd_tokens(args):
    """tokens <id|hex,hex,...> [--ground dark|light] — combo → verified CSS tokens."""
    ground_pref = "dark"
    for i, a in enumerate(args):
        if a == "--ground":
            ground_pref = args[i + 1]
    src = args[0]
    if "#" in src:
        cols = [c if c.startswith("#") else "#" + c for c in src.split(",")]
    else:
        cols = {c["id"]: c for c in load()}[int(src)]["colors"]

    by_light = sorted(cols, key=lambda c: to_lch(parse(c))[0])
    ground = by_light[0] if ground_pref == "dark" else by_light[-1]
    rest = [c for c in cols if c != ground]
    # Foreground: whatever reads best on the ground.
    fg = max(rest, key=lambda c: contrast(c, ground))
    rest = [c for c in rest if c != fg]
    # Accent: most chromatic of what's left (fall back to fg's neighbour).
    accent = max(rest or [fg], key=lambda c: to_lch(parse(c))[1])
    support = [c for c in rest if c != accent]

    opposite = "#FFFFFF" if ground_pref == "dark" else "#030303"
    acc_deep, acc_deep_r = variant_for(accent, fg)  # accent on the light/paper side

    print(f"/* Generated from {src} — every ratio measured, not estimated. */")
    print(":root {")
    print(f"  --ground:  {ground};  /* {'dark' if ground_pref=='dark' else 'light'} surface */")
    print(f"  --fg:      {fg};  /* {contrast(fg, ground):.2f}:1 on --ground"
          f" — {'AAA' if contrast(fg,ground)>=7 else 'AA' if contrast(fg,ground)>=4.5 else 'FAIL'} */")
    r = contrast(accent, ground)
    print(f"  --accent:  {accent};  /* {r:.2f}:1 on --ground"
          f" — {'AAA' if r>=7 else 'AA' if r>=4.5 else 'AA-large only' if r>=3 else 'FAIL'} */")
    if acc_deep and acc_deep.upper() != accent.upper():
        print(f"  --accent-on-fg: {acc_deep};  /* {acc_deep_r:.2f}:1 on --fg"
              f" — use when the accent sits on the light surface */")
    for i, c in enumerate(support, 1):
        r = contrast(c, ground)
        note = "" if r >= 3 else " — decorative only, never text"
        print(f"  --support-{i}: {c};  /* {r:.2f}:1 on --ground{note} */")
    print("}")

    warn = []
    if contrast(fg, ground) < 4.5:
        warn.append(f"foreground {fg} is only {contrast(fg,ground):.2f}:1 on the ground")
    if contrast(accent, ground) < 3:
        warn.append(f"accent {accent} is {contrast(accent,ground):.2f}:1 — not usable, even large")
    if not acc_deep:
        warn.append(f"no lightness of {accent} clears 4.5:1 on {fg}; pick a different accent")
    for w in warn:
        print(f"/* WARNING: {w} */")
    if not warn:
        print("/* All roles clear their intended surface. */")


def _lab_to_rgb(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    g = lambda t: t ** 3 if t ** 3 > 0.008856 else (t - 16 / 116) / 7.787
    x, y, z = g(fx) * 0.95047, g(fy), g(fz) * 1.08883
    r = 3.2406 * x - 1.5372 * y - 0.4986 * z
    gg = -0.9689 * x + 1.8758 * y + 0.0415 * z
    bb = 0.0557 * x - 0.2040 * y + 1.0570 * z
    return (r, gg, bb)


def _srgb(c):
    c = max(0.0, min(1.0, c))
    return 255 * (12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055)


def cmd_show(args):
    """show <id>... — print combos by book id."""
    by_id = {c["id"]: c for c in load()}
    for a in args:
        c = by_id[int(a)]
        print(f"#{c['id']:<4} p{c['page']}  {render(c['colors'])}")


def cmd_help(_):
    print(__doc__)
    for name, fn in sorted(globals().items()):
        if name.startswith("cmd_") and fn.__doc__:
            print("  " + fn.__doc__.strip().splitlines()[0])


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    fn = globals().get("cmd_" + cmd)
    if not fn:
        print(f"unknown command: {cmd}")
        cmd_help(None)
        sys.exit(1)
    fn(sys.argv[2:])
