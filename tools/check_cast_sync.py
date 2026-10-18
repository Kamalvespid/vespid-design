#!/usr/bin/env python3
"""Check that both skills carry identical cast reference drawings.

The badge generator (Appendix B) and the character generator (Appendix A)
each embed the same <g id="cast-..."> groups. If one is edited and the other
is not, characters drift between badges and scenes. This script fails if
the two copies differ, and can regenerate the standalone SVGs in assets/cast/.

Usage:
  python3 tools/check_cast_sync.py            # check only
  python3 tools/check_cast_sync.py --export   # check, then write assets/cast/*.svg
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BADGE = ROOT / "skills/vespid-badge-generator/SKILL.md"
CHAR = ROOT / "skills/vespid-character-generator/SKILL.md"
OUT = ROOT / "assets/cast"

# Only whole drawing blocks: opening tag alone on its line, closing </g> alone on its line.
GROUP_RE = re.compile(r'^<g id="(cast-[a-z-]+)">$.*?^</g>$', re.S | re.M)


def groups(path):
    text = path.read_text(encoding="utf-8")
    return {m.group(1): m.group(0).strip() for m in GROUP_RE.finditer(text)}


def main():
    b, c = groups(BADGE), groups(CHAR)
    ok = True
    for name in sorted(set(b) | set(c)):
        if name not in b:
            print(f"MISSING in badge generator: {name}")
            ok = False
        elif name not in c:
            print(f"MISSING in character generator: {name}")
            ok = False
        elif b[name] != c[name]:
            print(f"DRIFT: {name} differs between the two skills")
            ok = False
        else:
            print(f"ok    {name}")
    if not ok:
        print("\nCast drawings are out of sync. Update both skills together.")
        sys.exit(1)

    if "--export" in sys.argv:
        OUT.mkdir(parents=True, exist_ok=True)
        for name, g in c.items():
            label = name.replace("cast-", "").replace("-", " ").title()
            svg = (
                '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="225" '
                f'viewBox="-100 -20 200 225" role="img" aria-label="{label}">\n'
                '  <ellipse cx="0" cy="198" rx="44" ry="5" fill="#E9E6DE"/>\n'
                f"  {g}\n</svg>\n"
            )
            (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
            print(f"wrote assets/cast/{name}.svg")


if __name__ == "__main__":
    main()
