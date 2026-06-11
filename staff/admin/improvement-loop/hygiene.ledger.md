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
