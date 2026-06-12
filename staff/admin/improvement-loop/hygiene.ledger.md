# Hygiene Ledger — artur

Schema: append-only. Each pass adds a dated block.

---

## Pass 2026-06-11

**Branch:** `claude/bold-thompson-6yrk3o`
**Sweep scope:** `active-project/`, `staff/admin/`, `staff/showrunner/`, `active-project/theater/proto-lines/`

### Findings (severity order)

1. **MEDIUM — Naming-convention violation (trivial fix: delete).**
   `active-project/theater/proto-lines/b01c19.md` violates the `<book>-<chapter>.md` proto-lines convention (missing hyphen).
   Exact duplicate of the correctly-named `active-project/theater/proto-lines/b01-c19.md` (diff clean).
   **Action taken:** deleted `b01c19.md`. Nothing downstream references the malformed path; the correct `b01-c19.md` is the live file consumed by `/and-stitch` and `/and-facets`.

2. **LOW — Context ledger absent for c16 and c19.**
   `context-ledger-b01-c16.md` and `context-ledger-b01-c19.md` are missing despite shipped drafts for both chapters.
   Grounding ledger also absent for c16 (`grounding-ledger-b01-c16.md`).
   These ledgers are authored during `/and-facets` Phase 2.5. Their absence may be intentional (chapters that cleared context/aliveness review without licensed adds) or an authoring miss.
   **Routed to oskar:** confirm whether the Phase 2.5 ledger was skipped intentionally for c16/c19 or should be back-filled. No fix taken.

3. **LOW — Open parking-lot items targeting already-completed chapters.**
   Several SOFT items (pl-2026-05-25-006, -007, -011, -012, -013, -014, -015, -016, pl-2026-05-31-001, pl-2026-05-31-004) remain `status: open` with `target.command: /and-write` or `/and-facets` scoped to chapters (b01c01, b01c02, b01c04, b01c07) that are shipped and terminal. These are all opt-in depth-pass candidates, not blocking. Schema says entries are never deleted — surfaced only.
   **No action.** Per schema, parking-lot entries are append-only; soft items surface in Phase 7 summaries. Not a drift finding.

4. **INFORMATIONAL — Admin STM size.**
   `staff/admin/stm.md` is 128 lines. Within normal range; no bloat flag.

5. **INFORMATIONAL — Showrunner STM is empty.**
   `staff/showrunner/stm.md` is 0 bytes. Normal at project close / between sessions; not a defect.

### Action taken

Deleted `active-project/theater/proto-lines/b01c19.md` (malformed duplicate of `b01-c19.md`).

---

## Pass 2026-06-12 — branch claude/bold-thompson-6yrk3o

**Scope swept:** active-project/, staff/, proto-lines, facets, parking-lot open items, internal path refs.

### Findings (severity-ordered)

**1. HIGH — Foreign directory: `staff/screener-personas/` (19 files)**
19 persona cards + INDEX.md from a different project (`resume-targeting`, 2026-05 Catherine Olver career-pivot analysis) sit inside the fiction pipeline's `staff/` directory. The INDEX.md labels them a "preservation copy" with no fiction-pipeline connection. No command body, schema, or routing table references this directory. Foreign content in `staff/` will accumulate context noise at every staff-sweep.
→ Route: **oskar** (owns process + tooling). Parking-lot entry pl-2026-06-12-hygiene-001.

**2. MEDIUM — Stale live content in `active-project/theater/facets/`**
- Full c07 facets remain in the live `theater/facets/` directory, but c07 is also fully archived at `theater/_archive/20260531T050032Z-b01c07-facets/`. All other chapters' facets have been cleaned from the live dir after archiving. c07's live copy is a stale orphan.
- `.r2-decisions.md` in the live facets dir references c13 (retired R2 shard from DEC-0116 era). Belongs with the c13 archive at `theater/_archive/20260604T003328Z-b01c13-facets/`.
→ Route: **oskar**. Not trivially fixable (deletion of live files; surface first per Rule 4).

**3. MEDIUM — Parking-lot context_refs path drift**
pl-2026-05-25-005, -006, -007 (all SOFT/OPEN) reference:
- `active-project/theater/facets/memory-b01-c01.md`
- `active-project/theater/facets/sensory-b01-c01.md`
- `active-project/theater/facets/state-updates-b01-c01.md`
- `active-project/theater/dialogue/taylor-hebert-kl-122ac.drafts.md`
All four paths moved to archive or do not exist at the listed paths. Files are recoverable (c01 facets are in `theater/_archive/20260526T031937Z-b01c01-facets/`; the drafts file is at `staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md`). Parking-lot is append-only per schema — refs cannot be corrected in-place. Impact: low (SOFT items only; human can trace to archive).
→ Surface only. No routing action.

**4. LOW — Duplicate proto-line file** *(superseded by Pass 2026-06-11 finding #1 — file already deleted)*
`active-project/theater/proto-lines/b01c19.md` was observed as an exact duplicate of canonical `b01-c19.md`. The 2026-06-11 pass already deleted it.

**5. LOW — Missing context/grounding ledgers for c06 and c16**
`context-ledger-b01-c06.md` and `grounding-ledger-b01-c06.md` absent (c06 may have been produced at the mechanism's first live boundary). `context-ledger-b01-c16.md` and `grounding-ledger-b01-c16.md` absent (no clear reason). `context-ledger-b01-c19.md` absent (only grounding ledger exists). All three chapters shipped to draft; no forward impact.
→ Surface only. Historical artifact gap.

### Action taken

**Top finding routes to oskar.** Parking-lot entry pl-2026-06-12-hygiene-001 appended to
`active-project/staff/showrunner/parking-lot.md` with routing note for `staff/screener-personas/`
cleanup decision. No files deleted; no files merged.
