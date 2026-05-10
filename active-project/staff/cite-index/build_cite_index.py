#!/usr/bin/env python3
"""
Cite-index builder for Step B of the and-facets pipeline.

Reads:
  - active-project/theater/proto-lines/<slug>.md
  - active-project/theater/facets/*.md

Writes:
  - active-project/theater/facets/_cite-index.md

Output is a derivation — pure transformation of the existing files. No
judgment, no rewriting. Run after every facet round to refresh.

Usage:
  python3 build_cite_index.py <episode-slug>
  python3 build_cite_index.py s01e01
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Iterable

# --- File-prefix mapping ---------------------------------------------------

# Filename -> citation prefix used in protoline [<prefix>:<id>] accruals.
FACET_FILES: dict[str, str] = {
    "tensometer.md": "tens",
    "location-state.md": "loc-state",
    "interest-narrator.md": "narrator",
    "sensory.md": "sensory",
    "state-updates.md": "state",
    "memory.md": "mem",
    "feeling.md": "feel",
    "metaphor.md": "meta",
    "vibes.md": "vibes",
}

# Per-facet entry-line regex.
# Form: "<entry-id> @<proto-id> <rest>" or
#       "<entry-id> [@<proto-id>] <rest>" (vibes off-anchor uses bracket form)
ENTRY_RE = re.compile(r"^(\d+)\s+\[?@(\d+)\]?\s+(.*)$")

# Off-anchor vibes lines (no @<proto-id> at all).
ENTRY_OFF_RE = re.compile(r"^(\d+)\s+(?!\[?@\d)(.*)$")

# Protoline regex: "<id> SUBJECT VERB OBJECT [optional citations]".
# Captures: id, body (with brackets if present).
PROTO_RE = re.compile(r"^(\d+)\s+(.*)$")

# Citation-token regex (inside [...] on protoline or licensed-by clauses).
CITE_TOKEN_RE = re.compile(r"([a-z][a-z0-9-]*):(\d+)")


# --- Parsing ---------------------------------------------------------------


def parse_facet_file(path: Path, prefix: str) -> list[dict]:
    """Returns a list of entry dicts for one facet file.

    Each entry: {id, anchor (proto-id or None), rest, licenses, rating (tens only)}
    """
    entries: list[dict] = []
    if not path.exists():
        return entries
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("---"):
            continue
        if ":" in line and line.split()[0].rstrip(":") in (
            "facet", "episode", "author", "authors", "round",
        ):
            continue
        m = ENTRY_RE.match(line)
        if m:
            eid = int(m.group(1))
            anchor = int(m.group(2))
            rest = m.group(3)
        else:
            m2 = ENTRY_OFF_RE.match(line)
            if not m2:
                continue
            eid = int(m2.group(1))
            anchor = None
            rest = m2.group(2)
        licenses = _extract_licenses(rest)
        rating = None
        if prefix == "tens":
            rm = re.match(r"^([123])\b", rest)
            if rm:
                rating = int(rm.group(1))
        entries.append({
            "id": eid,
            "anchor": anchor,
            "rest": rest,
            "licenses": licenses,
            "rating": rating,
        })
    return entries


def _extract_licenses(rest: str) -> list[tuple[str, int]]:
    """Pull citation tokens from a 'licensed-by:' clause if present.

    Used by metaphor and vibes facets. Returns list of (prefix, id).
    """
    if "licensed-by:" not in rest:
        return []
    after = rest.split("licensed-by:", 1)[1]
    return [(p, int(i)) for p, i in CITE_TOKEN_RE.findall(after)]


def parse_protolines(path: Path) -> tuple[dict[int, str], dict[int, list[tuple[str, int]]]]:
    """Returns (proto_body_by_id, citations_by_id).

    proto_body_by_id: protoline-id -> SVO sentence (without brackets).
    citations_by_id: protoline-id -> [(facet-prefix, entry-id), ...]
    """
    bodies: dict[int, str] = {}
    cites: dict[int, list[tuple[str, int]]] = defaultdict(list)
    in_body = False
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if not in_body:
            # Skip header until first numbered line.
            if PROTO_RE.match(line.strip()):
                in_body = True
            else:
                continue
        if not in_body:
            continue
        m = PROTO_RE.match(line.strip())
        if not m:
            continue
        pid = int(m.group(1))
        body = m.group(2).strip()
        # Split off citation list.
        if "[" in body and body.endswith("]"):
            sentence, _, bracketed = body.rpartition("[")
            sentence = sentence.strip()
            bracketed = bracketed[:-1]
            for prefix, eid in CITE_TOKEN_RE.findall(bracketed):
                cites[pid].append((prefix, int(eid)))
        else:
            sentence = body
        bodies[pid] = sentence
    return bodies, dict(cites)


# --- Index construction ----------------------------------------------------


def build_index(episode: str, facets_dir: Path, protoline_path: Path) -> str:
    proto_bodies, proto_cites = parse_protolines(protoline_path)

    # entries_by_facet: prefix -> list of entry dicts
    entries_by_facet: dict[str, list[dict]] = {}
    for fname, prefix in FACET_FILES.items():
        entries_by_facet[prefix] = parse_facet_file(facets_dir / fname, prefix)

    # Build (prefix, id) -> entry index for cross-lookup
    entry_index: dict[tuple[str, int], dict] = {}
    for prefix, ents in entries_by_facet.items():
        for e in ents:
            entry_index[(prefix, e["id"])] = e

    # For each entry: compute back_cited + co_located
    # back_cited: True iff (prefix, id) appears in cites[anchor]
    # co_located: list of (prefix, id) sharing the entry's anchor protoline (excluding self)
    for prefix, ents in entries_by_facet.items():
        for e in ents:
            anchor = e["anchor"]
            if anchor is None:
                e["back_cited"] = None  # off-anchor — N/A
                e["co_located"] = []
                continue
            line_cites = proto_cites.get(anchor, [])
            e["back_cited"] = (prefix, e["id"]) in line_cites
            e["co_located"] = [
                (p, i) for (p, i) in line_cites
                if not (p == prefix and i == e["id"])
            ]

    # Stats
    total_entries = sum(len(v) for v in entries_by_facet.values())
    decorated_protos = sorted(proto_cites.keys())
    total_decorated = len(decorated_protos)
    total_bones = len(proto_bodies)

    # Lonely entries: zero co-location AND zero inbound license references.
    # Special case: tens entries with rating=1 are never back-cited by convention
    # (saves write volume). They are not deletion candidates — exclude from lonelies.
    inbound_licenses: dict[tuple[str, int], list[tuple[str, int]]] = defaultdict(list)
    for prefix, ents in entries_by_facet.items():
        for e in ents:
            for (lp, lid) in e["licenses"]:
                inbound_licenses[(lp, lid)].append((prefix, e["id"]))
    lonelies = []
    for prefix, ents in entries_by_facet.items():
        for e in ents:
            if e["co_located"]:
                continue
            if inbound_licenses.get((prefix, e["id"])):
                continue
            if e["anchor"] is None:
                continue  # off-anchor vibes are intentionally context-free
            if prefix == "tens" and e.get("rating") == 1:
                continue  # 1-rated tens don't back-cite by convention
            lonelies.append((prefix, e["id"], e["anchor"]))

    # Pile-ups: protolines with > 4 distinct facet citations
    pileups = sorted(
        ((pid, cites_list) for pid, cites_list in proto_cites.items() if len(cites_list) > 4),
        key=lambda x: -len(x[1]),
    )

    # Density distribution
    density_buckets = defaultdict(int)
    for pid, cites_list in proto_cites.items():
        density_buckets[len(cites_list)] += 1

    # --- Render ------------------------------------------------------------
    out: list[str] = []
    out.append(f"# Cite-Index — {episode}")
    out.append(f"generated: {date.today().isoformat()}")
    out.append(f"source: {protoline_path} + {facets_dir}/")
    out.append(f"scope: 9 facet files + 1 proto-lines file")
    out.append(
        f"totals: {total_entries} facet entries; "
        f"{total_decorated}/{total_bones} protolines decorated "
        f"({100 * total_decorated / max(1, total_bones):.1f}%)"
    )
    out.append("")

    # Density
    out.append("## Density distribution (protolines by citation count)")
    out.append("")
    out.append("| cites/line | count |")
    out.append("|------------|-------|")
    bare_count = total_bones - total_decorated
    out.append(f"| 0 (bare)   | {bare_count} |")
    for k in sorted(density_buckets):
        out.append(f"| {k}          | {density_buckets[k]} |")
    out.append("")

    # Per-facet
    out.append("## Per-facet entries")
    out.append("")
    for fname, prefix in FACET_FILES.items():
        ents = entries_by_facet[prefix]
        out.append(f"### {prefix} ({len(ents)} entries)")
        if not ents:
            out.append("_(no entries)_")
            out.append("")
            continue
        for e in ents:
            anchor = f"@{e['anchor']}" if e["anchor"] is not None else "@-"
            if prefix == "tens" and e.get("rating") is not None:
                back_field = f"r={e['rating']}"
                if e["rating"] == 1 and not e["back_cited"]:
                    pass  # convention: r=1 has no back-cite, don't flag
                elif e["back_cited"]:
                    back_field += " back=Y"
                else:
                    back_field += " back=N"
            else:
                back = "Y" if e["back_cited"] else ("-" if e["back_cited"] is None else "N")
                back_field = f"back={back}"
            co = ", ".join(f"{p}:{i}" for (p, i) in e["co_located"])
            lic = ", ".join(f"{p}:{i}" for (p, i) in e["licenses"])
            inbound = inbound_licenses.get((prefix, e["id"]), [])
            inb = ", ".join(f"{p}:{i}" for (p, i) in inbound)
            parts = [f"{prefix}:{e['id']}", anchor, back_field]
            if co:
                parts.append(f"co=[{co}]")
            if lic:
                parts.append(f"lic-out=[{lic}]")
            if inb:
                parts.append(f"lic-in=[{inb}]")
            out.append("  " + " ".join(parts))
        out.append("")

    # Pile-ups
    out.append("## Pile-ups (>4 facets co-located on one protoline)")
    out.append("")
    if not pileups:
        out.append("_(none)_")
    else:
        for pid, cites_list in pileups:
            cite_str = ", ".join(f"{p}:{i}" for (p, i) in cites_list)
            body = proto_bodies.get(pid, "")
            out.append(f"- **@{pid}** ({len(cites_list)}): {cite_str}")
            if body:
                out.append(f"    `{body}`")
    out.append("")

    # Lonely entries
    out.append("## Lonely entries (no co-location, no inbound license)")
    out.append("_Round-2 deletion candidates — but check the rubric before cutting._")
    out.append("")
    if not lonelies:
        out.append("_(none)_")
    else:
        for prefix, eid, anchor in lonelies:
            body = proto_bodies.get(anchor, "")
            out.append(f"- {prefix}:{eid} @{anchor}  `{body}`")
    out.append("")

    # Bare protolines
    out.append("## Bare protolines (no citations accrued)")
    out.append("_Round-2 add candidates if the rubric licenses a fire here._")
    out.append("")
    bare = sorted(set(proto_bodies) - set(proto_cites))
    if not bare:
        out.append("_(none — full coverage)_")
    else:
        out.append(", ".join(f"@{p}" for p in bare))
    out.append("")

    return "\n".join(out)


# --- CLI -------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} <episode-slug>", file=sys.stderr)
        return 2
    episode = argv[1]
    project_root = Path("active-project")
    facets_dir = project_root / "theater" / "facets"
    protoline_path = project_root / "theater" / "proto-lines" / f"{episode}.md"
    if not facets_dir.exists():
        print(f"facets dir not found: {facets_dir}", file=sys.stderr)
        return 1
    if not protoline_path.exists():
        print(f"protoline file not found: {protoline_path}", file=sys.stderr)
        return 1
    output = build_index(episode, facets_dir, protoline_path)
    out_path = facets_dir / "_cite-index.md"
    out_path.write_text(output)
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
