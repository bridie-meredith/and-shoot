#!/usr/bin/env python3
"""check-threads.py — causal-thread integrity checker for the and-experiment outline.

Parses one or more outline/ledger markdown files for PLANT[...] / FIRE[...] tokens and
reports broken causality:

  * orphaned plants     — a setup that is never paid off (PLANT with no matching FIRE)
  * unplanted fires     — a payoff with no setup  (FIRE  with no matching PLANT)
  * gift -> spend order  — a GIFT spent (FIRE) before it is given (PLANT)
  * curdle-ladder gaps   — rungs R0..R4 not all present across the parsed chapters

The script is story-agnostic. All story-specific exceptions (aliases, plant-only and
payoff-only tokens) live in a config file (default: alongside the first input file as
thread-config.txt), so the baseline reads clean and only NEW breaks surface.

Token normalisation: the key is the text inside [...], truncated at the first '->' or
'→', stripped, upper-cased. GIFT: prefixes are preserved.

Usage:
    check-threads.py FILE [FILE ...] [--config PATH] [--quiet]

Exit code is non-zero if any NEW (non-excepted) break is found.
"""
import argparse
import os
import re
import sys

TOKEN_RE = re.compile(r'\b(PLANT|FIRE)\[([^\]]*)\]')
# chapter headers like:  ### I.1 · the-christening-spoon   /   ## II.10 · the-clerk
CHAPTER_RE = re.compile(r'^#{2,4}\s+(I{1,3}|IV|V|VI{0,3})\.(\d+)\b')
RUNG_RE = re.compile(r'\bR([0-4])\b')
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8}


def norm(raw):
    """Normalise a token body to its causal key."""
    base = re.split(r'→|->', raw)[0].strip().upper()
    return base


def chapter_order(book_roman, num):
    return ROMAN.get(book_roman, 99) * 100 + int(num)


def load_config(path):
    cfg = {"alias": {}, "plant_only": set(), "payoff_only": set()}
    if not path or not os.path.exists(path):
        return cfg
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            parts = line.split(None, 1)
            directive = parts[0].upper()
            rest = parts[1].strip() if len(parts) > 1 else ""
            if directive == "ALIAS":
                # ALIAS <sub-token> = <canonical-token>
                if "=" in rest:
                    a, b = rest.split("=", 1)
                    cfg["alias"][a.strip().upper()] = b.strip().upper()
            elif directive == "PLANT-ONLY":
                cfg["plant_only"].add(rest.upper())
            elif directive == "PAYOFF-ONLY":
                cfg["payoff_only"].add(rest.upper())
    return cfg


def parse_files(paths):
    """Return (plants, fires, rungs) dicts: key -> list of (file, chapter_order, chapter_label)."""
    plants, fires = {}, {}
    rungs = {}  # rung int -> set of chapter labels
    for path in paths:
        cur_order, cur_label = 0, "(preamble)"
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                ch = CHAPTER_RE.match(line)
                if ch:
                    cur_order = chapter_order(ch.group(1), ch.group(2))
                    cur_label = f"{ch.group(1)}.{ch.group(2)}"
                    # a Rung line on/after the header attributes rungs to this chapter
                for kind, body in TOKEN_RE.findall(line):
                    key = norm(body)
                    rec = (os.path.basename(path), cur_order, cur_label)
                    (plants if kind == "PLANT" else fires).setdefault(key, []).append(rec)
                if "Rung" in line or "rung" in line:
                    for r in RUNG_RE.findall(line):
                        rungs.setdefault(int(r), set()).add(cur_label)
    return plants, fires, rungs


def apply_alias(key, alias):
    return alias.get(key, key)


def main():
    ap = argparse.ArgumentParser(description="Causal-thread integrity checker.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--config", default=None,
                    help="exceptions/alias config (default: thread-config.txt beside first file)")
    ap.add_argument("--quiet", action="store_true", help="suppress the KNOWN-exception listing")
    args = ap.parse_args()

    cfg_path = args.config or os.path.join(os.path.dirname(os.path.abspath(args.files[0])),
                                           "thread-config.txt")
    cfg = load_config(cfg_path)
    alias = cfg["alias"]

    plants, fires, rungs = parse_files(args.files)

    # canonicalise keys through aliases
    plant_keys = {apply_alias(k, alias) for k in plants}
    fire_keys = {apply_alias(k, alias) for k in fires}

    orphan_plants = sorted(plant_keys - fire_keys)
    unplanted_fires = sorted(fire_keys - plant_keys)

    new_orphans = [k for k in orphan_plants if k not in cfg["plant_only"]]
    known_orphans = [k for k in orphan_plants if k in cfg["plant_only"]]
    new_unplanted = [k for k in unplanted_fires if k not in cfg["payoff_only"]]
    known_unplanted = [k for k in unplanted_fires if k in cfg["payoff_only"]]

    # gift -> spend ordering
    order_warnings = []
    for k in plant_keys:
        if not k.startswith("GIFT:"):
            continue
        canon_plants = [r for src, recs in plants.items()
                        if apply_alias(src, alias) == k for r in recs]
        canon_fires = [r for src, recs in fires.items()
                       if apply_alias(src, alias) == k for r in recs]
        if canon_plants and canon_fires:
            first_plant = min(o for _, o, _ in canon_plants)
            first_fire = min(o for _, o, _ in canon_fires)
            if first_fire < first_plant:
                order_warnings.append(
                    f"{k}: spent (ch order {first_fire}) BEFORE given (ch order {first_plant})")

    # curdle ladder
    missing_rungs = [r for r in range(5) if r not in rungs]

    def emit(title, items):
        print(f"\n{title} ({len(items)}):")
        for it in items:
            print(f"  - {it}")

    print(f"# thread-check  ·  files: {', '.join(os.path.basename(f) for f in args.files)}")
    print(f"# config: {cfg_path if os.path.exists(cfg_path) else '(none)'}")
    print(f"# plants={len(plant_keys)} fires={len(fire_keys)} "
          f"aliases={len(alias)} plant-only={len(cfg['plant_only'])} "
          f"payoff-only={len(cfg['payoff_only'])}")

    problems = 0
    if new_orphans:
        emit("NEW ORPHANED PLANTS (setup, no payoff)", new_orphans); problems += len(new_orphans)
    if new_unplanted:
        emit("NEW UNPLANTED FIRES (payoff, no setup)", new_unplanted); problems += len(new_unplanted)
    if order_warnings:
        emit("GIFT->SPEND ORDER VIOLATIONS", order_warnings); problems += len(order_warnings)
    if missing_rungs:
        emit("CURDLE-LADDER MISSING RUNGS", [f"R{r}" for r in missing_rungs]); problems += len(missing_rungs)

    if not args.quiet:
        if known_orphans:
            emit("known plant-only (excepted)", known_orphans)
        if known_unplanted:
            emit("known payoff-only (excepted)", known_unplanted)
        present = sorted(rungs)
        print(f"\ncurdle rungs present: " +
              ", ".join(f"R{r}=[{','.join(sorted(rungs[r]))}]" for r in present))

    print()
    if problems:
        print(f"RESULT: {problems} NEW break(s) — FAIL")
        return 1
    print("RESULT: clean (no new breaks beyond accepted exceptions) — PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
