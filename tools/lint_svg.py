#!/usr/bin/env python3
"""Export-safety lint for Vespid SVGs (badge steering §2.5, §2.6, §8).

Checks every .svg under exports/ (or the paths given):
  - has an aria-label
  - no <text> left (badges must be outlined; characters never have text)
  - no paint-order, <textPath>, <style>, filters, gradients or class=

Usage:
  python3 tools/lint_svg.py                 # lint exports/
  python3 tools/lint_svg.py path/to/a.svg   # lint specific files
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RULES = [
    (r"<text[\s>]", "live <text> found: run skills/vespid-badge-generator/scripts/outline_text.py"),
    (r"paint-order", "paint-order is not export-safe"),
    (r"<textPath", "<textPath> is not export-safe"),
    (r"<style", "<style> blocks are not allowed; use fill/stroke attributes"),
    (r"<filter|filter=", "filters are not allowed"),
    (r"Gradient", "gradients are not allowed (flat fills only)"),
    (r'\sclass="', "CSS classes are not allowed"),
]


def lint(path):
    text = path.read_text(encoding="utf-8")
    problems = [msg for pat, msg in RULES if re.search(pat, text)]
    if "aria-label=" not in text:
        problems.append("missing aria-label")
    return problems


def main():
    args = [Path(a) for a in sys.argv[1:]]
    files = args or sorted((ROOT / "exports").rglob("*.svg"))
    if not files:
        print("No SVGs to lint yet.")
        return
    failed = 0
    for f in files:
        problems = lint(f)
        rel = f.relative_to(ROOT) if f.is_absolute() and ROOT in f.parents else f
        if problems:
            failed += 1
            for p in problems:
                print(f"FAIL  {rel}: {p}")
        else:
            print(f"ok    {rel}")
    if failed:
        print(f"\n{failed} file(s) failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
