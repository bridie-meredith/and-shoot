#!/usr/bin/env python3
"""
Phase-1 → Phase-2 merge + cite-index builder for /and-facets.

Runs between Round 1 (parallel blind authoring) and Round 2 (parallel
graph-aware judging). Each R1 author writes its own facet file and its own
annotated copy of the proto-lines file under `_inflight/`. This tool folds
those copies back into the canonical proto-lines file and consolidates any
per-character slice facet files, then builds the cross-cutting cite-index.

Pipeline:
  1. Body-integrity check.   Every _inflight/proto-lines-<facet>.md copy
                             must have SVO bodies identical to the base
                             proto-lines file (authors append citations
                             only; bones are immutable).
  2. Citation union.         Per proto-line ID, union the bracketed
                             [<prefix>:<id>] tokens across the base and
                             every author copy. Deterministic order
                             (prefix alphabetical, id ascending). Write
                             back to the canonical proto-lines/<slug>.md.
  3. Slice consolidation.    Concatenate feeling-<slug>.md slices into
                             feeling.md; concatenate state-updates-<slug>.md
                             slices and state-updates-env.md (if present)
                             into state-updates.md. IDs renumbered
                             monotonically; per-character source preserved
                             in an inline `# source: <slug>` comment.
  4. Stale-citation check.   Every [<prefix>:<id>] on a proto-line must
                             resolve to an entry in the corresponding
                             facet file post-consolidation. Unresolved
                             citations are a build defect; abort.
  5. Cite-index build.       Same as legacy build_cite_index.py — pure
                             derivation off the canonical merged state.

Reads:
  - active-project/theater/proto-lines/<slug>.md           (base; upstream tens cites)
  - active-project/theater/facets/_inflight/proto-lines-*.md (per-author copies)
  - active-project/theater/facets/<facet>.md               (R1-authored)
  - active-project/theater/facets/{feeling,state-updates}-<slug>.md (slices)

Writes:
  - active-project/theater/proto-lines/<slug>.md           (canonical merge)
  - active-project/theater/facets/feeling.md               (if slices present)
  - active-project/theater/facets/state-updates.md         (if slices present)
  - active-project/theater/facets/_cite-index.md

Usage:
  python3 build_cite_index.py <episode-slug>
  python3 build_cite_index.py s01e01

Flags:
  --skip-merge       Run cite-index only (legacy mode; no _inflight read).
                     Used by R2/R3 which mutate the canonical state directly.
  --facets-dir DIR   Override the facets directory location. Defaults to
                     active-project/theater/facets. Used by retrofits running
                     against an archived episode directory.
  --only-prefix P    Restrict the merge to a single facet prefix. Only the
                     matching _inflight/proto-lines-<P>.md file is consulted;
                     slice consolidation is skipped. Used to retrofit a new
                     facet onto a previously-finalised episode without
                     regressing post-R2 fixer edits on the other facets.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

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

# Exposition is authored per-episode as `exposition-<slug>.md`. Resolved at
# runtime from the episode slug rather than carried as a fixed filename, but
# the citation prefix is stable.
EXPOSITION_PREFIX = "exposition"


def resolve_facet_files(facets_dir: Path, episode: str) -> dict[str, str]:
    """Return the filename->prefix map for THIS episode (adds exposition if present)."""
    files = dict(FACET_FILES)
    expo = facets_dir / f"exposition-{episode}.md"
    if expo.exists():
        files[expo.name] = EXPOSITION_PREFIX
    return files

# Facets that are written as per-character slices in R1 parallel mode.
# slice-file pattern: <slice-base>-<character-slug>.md
# Consolidated into the canonical single file (no schema-reader changes downstream).
SLICED_FACETS: dict[str, str] = {
    # consolidated-filename -> slice-prefix
    "feeling.md": "feeling",
    "state-updates.md": "state-updates",
}

# Per-facet entry-line regex.
# Form: "<entry-id> @<proto-id> <rest>" or
#       "<entry-id> [@<proto-id>] <rest>" (vibes off-anchor uses bracket form)
ENTRY_RE = re.compile(r"^(\d+)\s+\[?@(\d+)\]?\s+(.*)$")

# Off-anchor vibes lines (no @<proto-id> at all).
ENTRY_OFF_RE = re.compile(r"^(\d+)\s+(?!\[?@\d)(.*)$")

# Protoline regex: "<id> SUBJECT VERB OBJECT [optional citations]".
PROTO_RE = re.compile(r"^(\d+)\s+(.*)$")

# Citation-token regex (inside [...] on protoline or licensed-by clauses).
CITE_TOKEN_RE = re.compile(r"([a-z][a-z0-9-]*):(\d+)")


# --- Proto-line parsing ----------------------------------------------------


def parse_proto_file(path: Path) -> tuple[list[str], dict[int, str], dict[int, list[tuple[str, int]]], dict[int, int]]:
    """Return (header_lines, bodies_by_id, cites_by_id, line_no_by_id).

    header_lines preserves everything before the first numbered SVO line so
    the canonical writer can pass it through unchanged.
    """
    header: list[str] = []
    bodies: dict[int, str] = {}
    cites: dict[int, list[tuple[str, int]]] = defaultdict(list)
    line_no: dict[int, int] = {}
    in_body = False
    for idx, raw in enumerate(path.read_text().splitlines()):
        line = raw.rstrip()
        stripped = line.strip()
        if not in_body:
            if PROTO_RE.match(stripped):
                in_body = True
            else:
                header.append(line)
                continue
        m = PROTO_RE.match(stripped)
        if not m:
            # Blank lines and inline comments inside the body are passed
            # through by storing them under a synthetic negative key so
            # ordering is preserved. (Skipped here; canonical writer
            # rebuilds body solely from sorted bodies dict.)
            continue
        pid = int(m.group(1))
        body = m.group(2).strip()
        # Strip ALL trailing [prefix:id] citation blocks (whitespace-separated).
        trailing_re = re.compile(r"(?:\s*\[[a-z][a-z0-9-]*:\d+\])+\s*$")
        cm = trailing_re.search(body)
        if cm:
            sentence = body[: cm.start()].rstrip()
            for prefix, eid in CITE_TOKEN_RE.findall(cm.group(0)):
                cites[pid].append((prefix, int(eid)))
        else:
            sentence = body
        bodies[pid] = sentence
        line_no[pid] = idx
    return header, bodies, dict(cites), line_no


def render_proto_file(header: list[str], bodies: dict[int, str], cites: dict[int, list[tuple[str, int]]]) -> str:
    """Render canonical proto-line file. Citations sorted deterministically."""
    out: list[str] = list(header)
    # Ensure exactly one blank line between header and body.
    while out and out[-1].strip() == "":
        out.pop()
    out.append("")
    for pid in sorted(bodies):
        body = bodies[pid]
        line_cites = cites.get(pid, [])
        if line_cites:
            seen = set()
            uniq = []
            for tok in sorted(line_cites, key=lambda x: (x[0], x[1])):
                if tok in seen:
                    continue
                seen.add(tok)
                uniq.append(tok)
            cite_str = " ".join(f"[{p}:{i}]" for (p, i) in uniq)
            out.append(f"{pid} {body} {cite_str}")
        else:
            out.append(f"{pid} {body}")
    return "\n".join(out) + "\n"


# --- Facet parsing ---------------------------------------------------------


def parse_facet_file(path: Path, prefix: str) -> list[dict]:
    """Return list of entry dicts for one facet file."""
    entries: list[dict] = []
    if not path.exists():
        return entries
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("---"):
            continue
        if ":" in line and line.split()[0].rstrip(":") in (
            "facet", "episode", "author", "authors", "round", "source",
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
    """Pull citation tokens from a 'licensed-by:' clause if present."""
    if "licensed-by:" not in rest:
        return []
    after = rest.split("licensed-by:", 1)[1]
    return [(p, int(i)) for p, i in CITE_TOKEN_RE.findall(after)]


# --- Phase 1: Body-integrity check ----------------------------------------


def body_integrity_check(base_bodies: dict[int, str], inflight_files: list[Path]) -> list[str]:
    """Verify all _inflight/proto-lines-*.md copies have bodies matching base.

    Authors are forbidden from mutating SVO bones; only the trailing [...]
    citation list may differ. Any body divergence is a build defect.
    """
    errors: list[str] = []
    for path in inflight_files:
        _, bodies, _, _ = parse_proto_file(path)
        base_ids = set(base_bodies)
        in_ids = set(bodies)
        for pid in sorted(base_ids - in_ids):
            errors.append(f"{path.name}: missing proto-line @{pid}")
        for pid in sorted(in_ids - base_ids):
            errors.append(f"{path.name}: extra proto-line @{pid} (not in base)")
        for pid in sorted(base_ids & in_ids):
            if bodies[pid] != base_bodies[pid]:
                errors.append(
                    f"{path.name}: body mismatch @{pid}\n"
                    f"    base:    {base_bodies[pid]}\n"
                    f"    inflight: {bodies[pid]}"
                )
    return errors


# --- Phase 2: Citation union ----------------------------------------------


def _facet_prefix_from_inflight_name(path: Path) -> str | None:
    """Extract the facet prefix from an _inflight/ proto-lines copy filename.

    Filename shapes:
      proto-lines-<prefix>.md
      proto-lines-<prefix>-<character-slug>.md   (sliced facets: feel-<slug>, state-<slug>)

    Returns the canonical facet prefix as used in the bracket-token form
    `[<prefix>:<id>]` on proto-lines. None if the name does not match.
    """
    stem = path.stem  # e.g. "proto-lines-mem" or "proto-lines-feel-taylor-hebert-flea-bottom"
    if not stem.startswith("proto-lines-"):
        return None
    tail = stem[len("proto-lines-"):]
    # Multi-segment facet prefixes used in citations: loc-state.
    # Single-segment prefixes per FACET_FILES values.
    if tail.startswith("loc-state"):
        return "loc-state"
    head = tail.split("-", 1)[0]
    # Slice facet author files write slug-suffixed citations under the base prefix.
    # feeling -> feel; state-updates env+actor -> state; per FACET_FILES.
    return head


def union_citations(
    base_cites: dict[int, list[tuple[str, int]]],
    inflight_files: list[Path],
) -> dict[int, list[tuple[str, int]]]:
    """Merge citation lists across base + all _inflight copies.

    URI-030 fix (2026-05-11): citations are unioned per-(proto-id, facet-prefix)
    with a deletion cascade — when an _inflight-r2/ copy is present for a facet
    prefix, IT is the source of truth for that prefix's citations on every
    proto-line it covers, including the absence of a citation (i.e., a R2-deleted
    citation token does NOT get re-added from an older _inflight/ copy under
    union). Other prefixes are unioned across both rings as before.

    Without this rule, a R2 judge that strips `[mem:5]` from its
    _inflight-r2/proto-lines-mem.md copy after DELETing mem:5 sees the citation
    re-added by union with _inflight/proto-lines-mem.md (which was authored
    pre-R2 and still has the bracket token). The R2 delete-cascade is silently
    reverted in the canonical merge.

    The owning-prefix rule: each inflight copy is responsible for its own
    facet prefix only. A copy's bracket tokens for OTHER prefixes are
    ignored — only the original-prefix author for those other prefixes
    can claim authorship. This preserves the design contract that authors
    cite their own facet, not others.
    """
    # Bucket inflight files by ring (r1 = _inflight, r2 = _inflight-r2) and prefix.
    r1: dict[str, list[Path]] = defaultdict(list)
    r2: dict[str, list[Path]] = defaultdict(list)
    for path in inflight_files:
        prefix = _facet_prefix_from_inflight_name(path)
        if prefix is None:
            continue
        bucket = r2 if path.parent.name == "_inflight-r2" else r1
        bucket[prefix].append(path)

    # Establish the authoritative ring per prefix: R2 wins if present.
    authoritative_by_prefix: dict[str, list[Path]] = {}
    for prefix, paths in r2.items():
        authoritative_by_prefix[prefix] = paths
    for prefix, paths in r1.items():
        authoritative_by_prefix.setdefault(prefix, paths)

    # base_cites carries upstream `tens:` citations. Seed merged with all of
    # those EXCEPT for prefixes whose authoritative ring will replace them.
    authoritative_prefixes = set(authoritative_by_prefix.keys())
    merged: dict[int, set[tuple[str, int]]] = defaultdict(set)
    for pid, cites in base_cites.items():
        for prefix, eid in cites:
            if prefix in authoritative_prefixes:
                continue
            merged[pid].add((prefix, eid))

    # For each prefix, pull citations only of THAT prefix from its
    # authoritative copies. Absence of a token in the authoritative copy is
    # interpreted as a delete (URI-030 fix).
    for prefix, paths in authoritative_by_prefix.items():
        for path in paths:
            _, _, cites, _ = parse_proto_file(path)
            for pid, toks in cites.items():
                for tok in toks:
                    if tok[0] == prefix:
                        merged[pid].add(tok)

    return {pid: sorted(toks) for pid, toks in merged.items()}


# --- Phase 3: Slice consolidation -----------------------------------------


def consolidate_slices(facets_dir: Path) -> dict[str, tuple[Path, list[Path]]]:
    """Concatenate per-character slice facet files into single canonical files.

    Returns a map of {target_filename: (target_path, [source_slice_paths])}
    for any consolidation that ran. IDs are renumbered monotonically across
    slices in lexical slice order; per-slice provenance is preserved via
    inline `# source: <slug>` comments.

    Existing canonical file (e.g., state-updates-env.md authored by studio
    as a non-slice base) is folded in first if present.
    """
    report: dict[str, tuple[Path, list[Path]]] = {}
    for target_name, slice_prefix in SLICED_FACETS.items():
        target_path = facets_dir / target_name
        env_path = facets_dir / f"{slice_prefix}-env.md"
        slice_paths = sorted(facets_dir.glob(f"{slice_prefix}-*.md"))
        # Drop slice-env from per-character slice list if present; handled separately.
        slice_paths = [p for p in slice_paths if p != env_path]
        # Exclude the consolidated target itself from slices.
        slice_paths = [p for p in slice_paths if p.name != target_name]
        sources = ([env_path] if env_path.exists() else []) + slice_paths
        if not sources:
            continue
        out_lines: list[str] = []
        # Emit a single top-of-file frontmatter for the consolidated target
        # (r3-signal-001 fix). Slices are expected to use plain-comment
        # headers (not YAML); the consolidator owns the canonical frontmatter.
        source_slugs = [src.stem[len(slice_prefix) + 1:] for src in sources]
        out_lines.append("---")
        out_lines.append(f"facet: {slice_prefix}")
        out_lines.append(f"sources: [{', '.join(source_slugs)}]")
        out_lines.append("note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.")
        out_lines.append("---")
        out_lines.append("")
        next_id = 1
        # Build a remap table so we can rewrite stale-cites later if needed,
        # though authors should cite their own entries with slice-local IDs
        # only and the consolidation rewrites those onto a canonical run.
        for src in sources:
            slug = src.stem[len(slice_prefix) + 1:]  # drop "<prefix>-"
            out_lines.append(f"# source: {slug}")
            for raw in src.read_text().splitlines():
                line = raw.rstrip()
                stripped = line.strip()
                if not stripped or stripped.startswith("#") or stripped.startswith("---"):
                    out_lines.append(line)
                    continue
                m = ENTRY_RE.match(stripped)
                if m:
                    _, anchor, rest = m.group(1), m.group(2), m.group(3)
                    out_lines.append(f"{next_id} @{anchor} {rest}")
                    next_id += 1
                    continue
                m2 = ENTRY_OFF_RE.match(stripped)
                if m2:
                    _, rest = m2.group(1), m2.group(2)
                    out_lines.append(f"{next_id} {rest}")
                    next_id += 1
                    continue
                # Non-entry line — pass through.
                out_lines.append(line)
            out_lines.append("")
        target_path.write_text("\n".join(out_lines).rstrip() + "\n")
        report[target_name] = (target_path, sources)
    return report


# --- Phase 4: Stale-citation check ----------------------------------------


def stale_citation_check(
    cites_by_id: dict[int, list[tuple[str, int]]],
    facets_dir: Path,
    facet_files: dict[str, str],
) -> list[str]:
    """Every [<prefix>:<id>] on a proto-line must resolve to an entry."""
    errors: list[str] = []
    entries_by_prefix: dict[str, set[int]] = {}
    for fname, prefix in facet_files.items():
        ents = parse_facet_file(facets_dir / fname, prefix)
        entries_by_prefix[prefix] = {e["id"] for e in ents}
    for pid, toks in cites_by_id.items():
        for prefix, eid in toks:
            if prefix not in entries_by_prefix:
                errors.append(f"@{pid}: unknown facet prefix '{prefix}:{eid}'")
                continue
            if eid not in entries_by_prefix[prefix]:
                errors.append(f"@{pid}: stale citation [{prefix}:{eid}] (no such entry)")
    return errors


# --- Phase 5: Cite-index build --------------------------------------------


def build_index(
    episode: str,
    facets_dir: Path,
    proto_bodies: dict[int, str],
    proto_cites: dict[int, list[tuple[str, int]]],
    protoline_path: Path,
    facet_files: dict[str, str],
) -> str:
    entries_by_facet: dict[str, list[dict]] = {}
    for fname, prefix in facet_files.items():
        entries_by_facet[prefix] = parse_facet_file(facets_dir / fname, prefix)

    for prefix, ents in entries_by_facet.items():
        for e in ents:
            anchor = e["anchor"]
            if anchor is None:
                e["back_cited"] = None
                e["co_located"] = []
                continue
            line_cites = proto_cites.get(anchor, [])
            e["back_cited"] = (prefix, e["id"]) in line_cites
            e["co_located"] = [
                (p, i) for (p, i) in line_cites
                if not (p == prefix and i == e["id"])
            ]

    total_entries = sum(len(v) for v in entries_by_facet.values())
    decorated_protos = sorted(proto_cites.keys())
    total_decorated = len(decorated_protos)
    total_bones = len(proto_bodies)

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
                continue
            if prefix == "tens" and e.get("rating") == 1:
                continue
            lonelies.append((prefix, e["id"], e["anchor"]))

    pileups = sorted(
        ((pid, cites_list) for pid, cites_list in proto_cites.items() if len(cites_list) > 4),
        key=lambda x: -len(x[1]),
    )

    density_buckets: dict[int, int] = defaultdict(int)
    for pid, cites_list in proto_cites.items():
        density_buckets[len(cites_list)] += 1

    out: list[str] = []
    out.append(f"# Cite-Index — {episode}")
    out.append(f"generated: {date.today().isoformat()}")
    out.append(f"source: {protoline_path} + {facets_dir}/")
    out.append(f"scope: {len(facet_files)} facet files + 1 proto-lines file")
    out.append(
        f"totals: {total_entries} facet entries; "
        f"{total_decorated}/{total_bones} protolines decorated "
        f"({100 * total_decorated / max(1, total_bones):.1f}%)"
    )
    out.append("")

    out.append("## Density distribution (protolines by citation count)")
    out.append("")
    out.append("| cites/line | count |")
    out.append("|------------|-------|")
    bare_count = total_bones - total_decorated
    out.append(f"| 0 (bare)   | {bare_count} |")
    for k in sorted(density_buckets):
        out.append(f"| {k}          | {density_buckets[k]} |")
    out.append("")

    out.append("## Per-facet entries")
    out.append("")
    for fname, prefix in facet_files.items():
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
                    pass
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
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("episode", help="episode slug, e.g. s01e01")
    parser.add_argument(
        "--skip-merge",
        action="store_true",
        help="cite-index only; skip _inflight merge + slice consolidation",
    )
    parser.add_argument(
        "--facets-dir",
        default=None,
        help="override the facets directory (defaults to active-project/theater/facets)",
    )
    parser.add_argument(
        "--only-prefix",
        default=None,
        help="restrict merge to a single facet prefix; skip slice consolidation. "
             "Used to retrofit a new facet without regressing post-R2 fixer edits.",
    )
    args = parser.parse_args(argv[1:])

    episode = args.episode
    project_root = Path("active-project")
    facets_dir = Path(args.facets_dir) if args.facets_dir else project_root / "theater" / "facets"
    protoline_path = project_root / "theater" / "proto-lines" / f"{episode}.md"

    if not facets_dir.exists():
        print(f"facets dir not found: {facets_dir}", file=sys.stderr)
        return 1
    if not protoline_path.exists():
        print(f"protoline file not found: {protoline_path}", file=sys.stderr)
        return 1

    facet_files = resolve_facet_files(facets_dir, episode)
    header, base_bodies, base_cites, _ = parse_proto_file(protoline_path)

    if not args.skip_merge:
        # Phase 1: body integrity — read both _inflight/ (R1) and _inflight-r2/ (R2) if present.
        inflight_files: list[Path] = []
        for d in sorted(facets_dir.glob("_inflight*")):
            if d.is_dir():
                inflight_files.extend(sorted(d.glob("proto-lines-*.md")))
        if args.only_prefix:
            # Retrofit mode: consider only the named prefix's _inflight copy.
            only = args.only_prefix
            inflight_files = [
                p for p in inflight_files
                if _facet_prefix_from_inflight_name(p) == only
            ]
        if inflight_files:
            body_errors = body_integrity_check(base_bodies, inflight_files)
            if body_errors:
                print("BODY-INTEGRITY FAIL — author copies mutated SVO bones:", file=sys.stderr)
                for err in body_errors:
                    print(f"  {err}", file=sys.stderr)
                return 2

        # Phase 2: citation union → canonical proto-lines
        merged_cites = union_citations(base_cites, inflight_files) if inflight_files else base_cites
        canonical_text = render_proto_file(header, base_bodies, merged_cites)
        protoline_path.write_text(canonical_text)
        print(f"merged {len(inflight_files)} author copies → {protoline_path}")

        # Phase 3: slice consolidation. Skipped in --only-prefix retrofit mode
        # because re-consolidating from slices on an already-finalised episode
        # would clobber post-Phase-5 fixer edits applied directly to the
        # consolidated files.
        if not args.only_prefix:
            slice_report = consolidate_slices(facets_dir)
            for target, (path, sources) in slice_report.items():
                src_names = ", ".join(s.name for s in sources)
                print(f"consolidated {target} from [{src_names}]")

        # Refresh post-merge state for downstream checks
        _, base_bodies, merged_cites, _ = parse_proto_file(protoline_path)

        # Phase 4: stale-citation check
        stale_errors = stale_citation_check(merged_cites, facets_dir, facet_files)
        if stale_errors:
            print("STALE-CITATION FAIL — citations don't resolve to facet entries:", file=sys.stderr)
            for err in stale_errors:
                print(f"  {err}", file=sys.stderr)
            return 3
    else:
        merged_cites = base_cites

    # Phase 5: cite-index
    index_text = build_index(episode, facets_dir, base_bodies, merged_cites, protoline_path, facet_files)
    out_path = facets_dir / "_cite-index.md"
    out_path.write_text(index_text)
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
