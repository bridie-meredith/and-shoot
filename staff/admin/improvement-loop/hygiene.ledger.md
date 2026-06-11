# Artur hygiene ledger
# Append-only. Each pass appends a dated entry.

---

## Pass 2026-06-11

**Scope:** full repo sweep (active-project/staff/showrunner/, parking-lot, draft/, theater/, memory staleness, index drift)

### Findings (severity-ordered)

**MED-1 — 7 loose draft/bones files at showrunner root (should be in _drafts/)**
Files deposited at `active-project/staff/showrunner/` root rather than `active-project/staff/showrunner/_drafts/`:
- `b01c09-bones-draft-2026-05-31.md`
- `b01c11-bones-draft.md`
- `b01c11-draft.md`
- `b01c15-bones-draft.md`
- `b01c15-draft.md`
- `b01c19-bones-draft.md`
- `b01c20-draft.md`

The `_drafts/` subdirectory holds dated equivalents for some (c11, c15, c20), but root copies lack timestamps — possibly older/incomplete drafts or differently-keyed versions. Clutter impedes Phase 0 quick-scans of the showrunner root. Artur does NOT move/delete these without surfacing — move is not on the trivial-fix allowlist.
→ **Routing: oskar** (owns state-file organization / studio housing). Decision: confirm whether root copies are superseded by the dated _drafts/ versions and can be moved; or if they carry distinct content that warrants dated naming + migration.
→ Parking-lot entry: `pl-hygiene-2026-06-11-001`

**LOW-1 — Open SOFT parking-lot items for chapters c01–c07 (unelected depth-passes)**
60 open items total in parking-lot.md. The majority target shipped chapters (c01–c07 era) and represent unelected depth-passes, advisory watches, and process-design questions that accumulated during production. These are not orphaned per schema (parking-lot items are never deleted), but the density adds navigational overhead at Phase 0. No action possible from artur — these remain until principal elects depth-passes or `/and-cohere` resolves them.
→ **Surfacing only.** No route needed.

**LOW-2 — Missing context-ledger for b01-c16 and b01-c19**
`context-ledger-b01-c16.md` and `context-ledger-b01-c19.md` absent from showrunner root, while `grounding-ledger-b01-c16.md` and `grounding-ledger-b01-c19.md` both exist. May be by design (no exposition adds required at those chapters' `/and-facets` Phase 2.5), or oversight. Non-blocking.
→ **Surfacing only.**

**LOW-3 — No stale_since markers (clean)**
All `stale_since` fields in `memory.md` are null. No stale staleness-cascade markers present.
→ No action.

**LOW-4 — _drafts/ render-brief files (b01c06–b01c08) and surgical notes**
`active-project/staff/stitcher/` holds `_render-brief-b01c06.md`, `_render-brief-b01c07.md`, `_render-brief-b01c08.md`, `c03-sera-surgical.md`, `c20-sera-surgical.md`. All chapters are shipped. These are intermediate artifacts; no schema violation. Non-blocking.
→ **Surfacing only.**

### Action taken

**Routing note → oskar** re: MED-1 (7 loose draft files at showrunner root).
Parking-lot entry `pl-hygiene-2026-06-11-001` appended.
Ledger created (this file).
