#!/usr/bin/env python3
"""Normalize _inflight-r2/proto-lines-*.md copies for body-integrity compliance.

R2 authors added free-text annotation brackets (e.g. `[n/a — ...]`,
`[taylor:2 REWRITE-R2]`) after SVO bodies. The cite-index builder's
body-integrity check refuses anything that isn't strict
`<id> <canonical SVO> <[prefix:digits] ...>`.

This pass:
  1. Reads canonical SVO bodies from active-project/theater/proto-lines/<slug>.md
  2. For each _inflight-r2/proto-lines-*.md, rewrites each numbered line as
     `<id> <canonical body> [<valid citation tokens only>]`
  3. Preserves all header / comment lines.

Only `[lowercase-prefix:digits]` brackets are kept. Annotation brackets are
dropped. Order of citations preserved per file (deterministic).

Usage:
  python3 scripts/normalize_inflight_r2.py <slug>
  python3 scripts/normalize_inflight_r2.py b01-c01
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

BRACKET_RE = re.compile(r"\[([^\]\[]*)\]")
CITE_TOKEN_RE = re.compile(r"\b([a-z][a-z0-9-]*):(\d+)\b")
PROTO_RE = re.compile(r"^(\d+)\s+(.*)$")

# Keywords inside a bracket that mean "annotation about the citation, not a fire."
# A bracket containing any of these is treated as non-citation (DELETE / REFUSE / n-a / non-fire).
SKIP_KEYWORDS = re.compile(r"\b(?:DELETED|REFUSED|n/a|REWRITE|n_a|REFUSE)\b", re.IGNORECASE)


def load_canonical(slug: str) -> dict[int, str]:
    path = Path("active-project/theater/proto-lines") / f"{slug}.md"
    bodies: dict[int, str] = {}
    in_body = False
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not in_body:
            if PROTO_RE.match(stripped):
                in_body = True
            else:
                continue
        m = PROTO_RE.match(stripped)
        if not m:
            continue
        pid = int(m.group(1))
        body = m.group(2).strip()
        # Strip trailing strict-citation brackets to get the SVO body.
        trailing_re = re.compile(r"(?:\s*\[[a-z][a-z0-9-]*:\d+\])+\s*$")
        cm = trailing_re.search(body)
        sentence = body[: cm.start()].rstrip() if cm else body
        bodies[pid] = sentence
    return bodies


def normalize_file(path: Path, canonical: dict[int, str]) -> tuple[int, int]:
    """Rewrite path in-place. Returns (lines_normalized, citations_kept)."""
    out_lines: list[str] = []
    norm_count = 0
    cite_count = 0
    in_body = False
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not in_body:
            if PROTO_RE.match(stripped):
                in_body = True
            else:
                out_lines.append(line)
                continue
        m = PROTO_RE.match(stripped)
        if not m:
            out_lines.append(line)
            continue
        pid = int(m.group(1))
        if pid not in canonical:
            # Unknown proto-id — leave the line; cite-index builder will catch.
            out_lines.append(line)
            continue
        # Extract every bracketed expression; per-bracket decide if it carries a fire.
        seen = set()
        ordered_cites = []
        for bracket_content in BRACKET_RE.findall(stripped):
            if SKIP_KEYWORDS.search(bracket_content):
                # Annotation bracket (DELETED / REFUSED / n/a / REWRITE) — not a fire.
                continue
            for prefix, eid in CITE_TOKEN_RE.findall(bracket_content):
                tok = (prefix, int(eid))
                if tok in seen:
                    continue
                seen.add(tok)
                ordered_cites.append(tok)
        body = canonical[pid]
        if ordered_cites:
            cite_str = " ".join(f"[{p}:{i}]" for (p, i) in ordered_cites)
            out_lines.append(f"{pid} {body} {cite_str}")
        else:
            out_lines.append(f"{pid} {body}")
        norm_count += 1
        cite_count += len(ordered_cites)
    path.write_text("\n".join(out_lines) + "\n")
    return norm_count, cite_count


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: normalize_inflight_r2.py <slug>", file=sys.stderr)
        return 1
    slug = argv[1]
    canonical = load_canonical(slug)
    inflight_dir = Path("active-project/theater/facets/_inflight-r2")
    if not inflight_dir.exists():
        print(f"no _inflight-r2/ dir at {inflight_dir}", file=sys.stderr)
        return 1
    files = sorted(inflight_dir.glob("proto-lines-*.md"))
    total_norm = 0
    total_cites = 0
    for path in files:
        norm, cites = normalize_file(path, canonical)
        print(f"  {path.name}: {norm} lines normalized, {cites} citations kept")
        total_norm += norm
        total_cites += cites
    print(f"total: {len(files)} files, {total_norm} lines, {total_cites} citations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
