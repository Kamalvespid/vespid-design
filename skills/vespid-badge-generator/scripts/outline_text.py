#!/usr/bin/env python3
"""Convert every <text> in a Vespid badge SVG to an outlined <path>.

Standard library only. Glyph shapes come from vespid_glyphs.json (Anton,
Baloo 2 ExtraBold, Nunito Sans ExtraBold - all SIL Open Font Licence), so no
installed fonts or network are needed.

Usage:
    python3 outline_text.py badge.svg                 # writes badge.outlined.svg
    python3 outline_text.py badge.svg -o out.svg
    python3 outline_text.py a.svg b.svg c.svg         # several files
    cat badge.svg | python3 outline_text.py - > out.svg

Supports the attributes the badge templates use: x, y, text-anchor,
font-family, font-size, letter-spacing, fill, stroke, stroke-width,
stroke-linejoin, opacity, transform. Fails loudly on anything it cannot
outline (unknown font, missing character, <tspan>), rather than guessing.
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GLYPHS = json.load(open(os.path.join(HERE, "vespid_glyphs.json"), encoding="utf-8"))

TEXT_RE = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)
ATTR_RE = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')
NUM_RE = re.compile(r"-?\d*\.?\d+(?:e-?\d+)?")
CMD_RE = re.compile(r"([MLQCZHV])([^MLQCZHV]*)", re.I)
KEEP = ("fill", "stroke", "stroke-width", "stroke-linejoin", "stroke-linecap",
        "opacity", "fill-opacity", "stroke-opacity", "transform", "id", "class")


class OutlineError(Exception):
    pass


def pick_font(family):
    for name in [f.strip().strip("'\"") for f in family.split(",")]:
        for key in GLYPHS:
            if key.lower() == name.lower():
                return key
    raise OutlineError(f"font-family '{family}' is not bundled (have: {', '.join(GLYPHS)})")


def fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def place(d, scale, dx, dy):
    """Scale glyph path (font units, y already flipped) and move it to (dx, dy)."""
    out = []
    for cmd, args in CMD_RE.findall(d):
        nums = [float(n) for n in NUM_RE.findall(args)]
        if cmd in "Zz":
            out.append("Z")
            continue
        if cmd in "Hh":
            out.append("H" + " ".join(fmt(n * scale + dx) for n in nums))
            continue
        if cmd in "Vv":
            out.append("V" + " ".join(fmt(n * scale + dy) for n in nums))
            continue
        pts = []
        for i in range(0, len(nums), 2):
            pts.append(fmt(nums[i] * scale + dx))
            pts.append(fmt(nums[i + 1] * scale + dy))
        out.append(cmd.upper() + " ".join(pts))
    return "".join(out)


def outline(attrs_src, content):
    if "<" in content:
        raise OutlineError("nested markup inside <text> (e.g. <tspan>) is not supported; use one <text> per line")
    a = dict(ATTR_RE.findall(attrs_src))
    text = html.unescape(content).strip()
    if not text:
        return ""
    font = GLYPHS[pick_font(a.get("font-family", ""))]
    size = float(a.get("font-size", "16").replace("px", ""))
    ls = float(a.get("letter-spacing", "0").replace("px", ""))
    x = float(a.get("x", "0"))
    y = float(a.get("y", "0"))
    scale = size / font["upem"]
    glyphs, kern = font["glyphs"], font["kern"]

    missing = sorted({c for c in text if c not in glyphs})
    if missing:
        raise OutlineError(f"characters not in the bundled font: {missing!r} in '{text}'")

    # advances in user units (letter-spacing after every character, like browsers)
    adv = []
    for i, ch in enumerate(text):
        w = glyphs[ch]["adv"]
        if i + 1 < len(text):
            w += kern.get(ch + text[i + 1], 0)
        adv.append(w * scale + ls)
    total = sum(adv)
    anchor = a.get("text-anchor", "start")
    pen = x - (total / 2 if anchor == "middle" else total if anchor == "end" else 0)

    parts = []
    for ch, w in zip(text, adv):
        d = glyphs[ch]["d"]
        if d:
            parts.append(place(d, scale, pen, y))
        pen += w

    keep = " ".join(f'{k}="{v}"' for k, v in a.items() if k in KEEP)
    if "fill" not in a:
        keep = ('fill="#000000" ' + keep).strip()
    label = html.escape(text, quote=True)
    return f'<path data-text="{label}" {keep} d="{"".join(parts)}"></path>'


def convert(svg):
    count = 0

    def sub(m):
        nonlocal count
        count += 1
        return outline(m.group(1), m.group(2))

    out = TEXT_RE.sub(sub, svg)
    if re.search(r"<text\b", out):
        raise OutlineError("a <text> element could not be matched (self-closing or malformed)")
    return out, count


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    out_path = None
    if "-o" in argv:
        i = argv.index("-o")
        out_path = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if argv == ["-"]:
        res, n = convert(sys.stdin.read())
        sys.stdout.write(res)
        print(f"outlined {n} text element(s)", file=sys.stderr)
        return 0
    for p in argv:
        res, n = convert(open(p, encoding="utf-8").read())
        dst = out_path or re.sub(r"\.svg$", "", p) + ".outlined.svg"
        open(dst, "w", encoding="utf-8").write(res)
        print(f"{p} -> {dst}: outlined {n} text element(s)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except OutlineError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
