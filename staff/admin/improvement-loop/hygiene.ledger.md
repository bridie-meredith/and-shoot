# Hygiene Ledger — and-shoot

Append-only. Each run appends a dated block. Findings are severity-ordered within each block. Actions are stamped after findings.

---

## Run: 2026-06-12

**Scope swept:** admin STM/LTM, showrunner memory (size probe), cascade-checkpoint, parking-lot (open-item state), context/grounding ledger coverage, actors STM, _drafts directory, active-project structure.

**Project state at sweep:** Book 1 complete (20/20 chapters shipped). Series verdict PASS-WITH-NOTES. No-ledger revision run COMPLETE (cascade-checkpoint status: COMPLETE, 2026-06-08). No active cascade in progress.

---

### Findings (severity-ordered)

**[HIGH] admin STM bloated — 127 entries vs documented ~20 cap**

- File: `staff/admin/stm.md`
- STM header: "Pruned to ~20 entries at each session-open; anything still load-bearing gets promoted to LTM first."
- Actual state: full decision history from DEC-0001 (2026-05-24) through DEC-0116 (2026-06-08), 127 entries.
- Full history is safely preserved in `staff/admin/decisions.md` (7627 lines). LTM has 6 standing-preference entries. No load-bearing carry is absent from decisions.md or CLAUDE.md.
- Fix: prune to 20 most recent entries (DEC-0116 through DEC-0097).
- **→ ACTION TAKEN** (see below)

**[MEDIUM] cascade-checkpoint stale `current:` field**

- File: `active-project/staff/showrunner/cascade-checkpoint.md`
- `status: COMPLETE` (2026-06-08) but `current: {chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}` remains from the no-ledger revision setup, never cleared on completion.
- Not load-bearing (status field is authoritative), but any new session reading this file would see a live-looking mid-run pointer on a completed checkpoint.
- Route: showrunner to update or annotate `current:` as `null` / "n/a (run complete)" at next memory pass.
- **→ ROUTED** to showrunner (see routing note below)

**[MEDIUM] parking-lot open items past their resolving command**

- File: `active-project/staff/showrunner/parking-lot.md` (2972 lines)
- Several SOFT open items target commands that have conclusively run and closed (e.g., pl-2026-05-25-006 → /and-facets b01c01; pl-2026-05-25-007 → /and-write b01c01; pl-2026-05-25-011/012/013/015/016 → /and-write b01c01 depth-pass; pl-2026-05-31-001 → depth-pass-recommended-b01c07-apparatus-register). Book production complete; these items will never get a resolution command.
- Admin LTM charges admin with periodic parking-lot administration: "surfacing staleness, promoting recurring patterns, flagging when the lot is filling faster than it drains."
- Parking lot is append-only per spec (entries never deleted). Resolution: admin should do a staleness sweep and stamp `resolved_at` + `resolution_note: "book-complete; resolving command concluded; accepted as terminal open SOFT"` on each item whose window has conclusively closed.
- **→ ROUTED** to admin (see routing note below)

**[LOW] context/grounding ledger gap — c16 and c19**

- Missing: `context-ledger-b01-c16`, `grounding-ledger-b01-c16`, `context-ledger-b01-c19`.
- c16 has neither; c19 has grounding-ledger but no context-ledger.
- Project is complete; these are pipeline artifacts. Could be legitimate pipeline skip (some chapters may not have required ledger entries) or missed emits.
- Route: showrunner to confirm at next memory pass whether c16/c19 facet pipelines skipped ledger generation or artifacts are missing.
- **→ ROUTED** to showrunner (informational; not blocking)

**[LOW] showrunner/_drafts/ 51 working files**

- Dir: `active-project/staff/showrunner/_drafts/`
- 51 intermediate authoring artifacts (bones drafts, chapter drafts, some VOIDED). All date-stamped. Several marked VOIDED.
- Not orphaned — these are the authoring history per pipeline convention. Not clutter in the artur sense; no fix needed.
- Status: NO ACTION — by design.

**[INFO] showrunner memory.md > 1MB**

- File: `active-project/staff/showrunner/memory.md`
- Size expected for 20-chapter book production. Content is the source of truth per CLAUDE.md memory rules. Not actionable.
- Status: NO ACTION — expected.

---

### Action taken

**Fix: pruned admin STM to 20 most recent entries**

- Removed entries DEC-0095 through DEC-0001 (107 entries, lines 33–128 of the original file).
- Retained: header (lines 1–11) + DEC-0116 through DEC-0097 (20 entries, lines 13–32).
- All removed entries are preserved verbatim in `staff/admin/decisions.md`.
- No load-bearing content was dropped: LTM has all standing preferences; CLAUDE.md has all codified rules; decisions.md has the full reasoning trail.

---

### Routing notes

**→ showrunner:** `active-project/staff/showrunner/cascade-checkpoint.md` — clear or annotate `current:` field as completed (status:COMPLETE is correct; stale pointer is cosmetic but confusing). Also: confirm whether c16 and c19 context/grounding ledgers were legitimately skipped or are missing emits.

**→ admin:** `active-project/staff/showrunner/parking-lot.md` — staleness sweep on SOFT open items whose resolving commands have conclusively closed (book complete). Stamp `resolved_at` + `resolution_note: "book-complete; resolving-command-window closed; accepted as terminal open SOFT"` on each. Items in scope at minimum: pl-2026-05-25-006, -007, -011, -012, -013, -015, -016, pl-2026-05-31-001 (depth-pass-recommended-b01c07).
