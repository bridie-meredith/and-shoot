# Hygiene Ledger

Append-only. Each run adds a dated entry: sweep findings (severity-ordered) + action taken.

---

## Run 2026-06-12 — branch: claude/gifted-hawking-aptpzz

**Project state:** taylor-westeros-good-intentions — COMPLETE. All 20 chapters shipped; verdict PASS-WITH-NOTES (2026-06-06). Active-project directory in-place as archive per ARCHIVE_NOTE.md.

### Findings — severity ordered

**MEDIUM-1 — Orphaned intermediate drafts in showrunner root**
Seven intermediate draft files sit directly in `active-project/staff/showrunner/` rather than in the `_drafts/` subdirectory that exists for exactly this purpose:
- `b01c09-bones-draft-2026-05-31.md`
- `b01c11-bones-draft.md`
- `b01c11-draft.md`
- `b01c15-bones-draft.md`
- `b01c15-draft.md`
- `b01c19-bones-draft.md`
- `b01c20-draft.md`

The `_drafts/` subdirectory holds analogous files for c01–c08 and c13–c20 (timestamped). These seven lack the `_drafts/` prefix, likely because the and-experiment authoring path (used for later chapters) emitted them to the directory root. The canonical bones files are all present in `theater/bones/`; these are intermediate authoring artifacts only. Route to **oskar** for disposition (move to `_drafts/` or note as tolerable archive clutter).

**MEDIUM-2 — Proto-lines exact duplicate: `b01c19.md` ≡ `b01-c19.md`**
`active-project/theater/proto-lines/` contains two files with identical content (39 lines, diff-empty):
- `b01-c19.md` — canonical naming convention (hyphens)
- `b01c19.md` — non-canonical (no hyphens; inconsistent with all other proto-line files)

The directory contains only three chapters (c18, c19, c20); both c19 variants are present. The non-canonical `b01c19.md` appears to have been created by accident. Route to **oskar** for deletion of the non-canonical copy. (Cannot delete without surfacing first per hygiene rules.)

**LOW-3 — Admin STM bloat: 128 entries vs ~20 design limit**
`staff/admin/stm.md` header states "Pruned to ~20 entries at each session-open; anything still load-bearing gets promoted to LTM first." The file contains all 128 decisions (DEC-0001–DEC-0116) from the full project run. Since the project is COMPLETE, this will not grow further and poses no operational risk. But the file is 6.4× its design size and would be an unnecessary context load if a new project were opened from this repo state. Route to **ingrid** for LTM promotion triage at next project activation.

**LOW-4 — Missing context-ledger for b01-c16**
All other chapters with ledgers (c07–c20) have both a `context-ledger-b01-c<NN>.md` and a `grounding-ledger-b01-c<NN>.md` in `active-project/staff/showrunner/`. Chapter c16 has neither. Since c16's draft shipped and the project is complete, this is a historical documentation gap — the chapter ran without the ledgers or they were lost. No action required; noted for completeness.

**LOW-5 — Parking-lot open SOFT items on completed chapters**
Approximately 25 SOFT parking-lot items target future invocations of `/and-write`, `/and-facets`, `/and-stitch` on chapters that have all shipped. These are normal accumulation on an archived project (depth-pass debt, optional quality improvements) and are not actionable without principal greenlight. Per schema, they remain open as-is; this is expected state for a closed book.

### Action taken

**Routing: MEDIUM-1 → oskar; MEDIUM-2 surfaced in parking-lot (pl-2026-06-12-hygiene-001).**

Parking-lot entry pl-2026-06-12-hygiene-001 filed for the proto-lines duplicate (the most concrete single-artifact finding). MEDIUM-1 routing note to oskar is this ledger entry; oskar should decide move-to-`_drafts/` vs. accept-as-archive-clutter.
