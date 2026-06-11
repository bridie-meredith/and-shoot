# improvement-loop/test — lens rotation ledger

Tracks which lens ran each pass so the routine rotates evenly.
Append-only. One entry per run.

Lens rotation order:
  a. /and-review pipeline — schema vs command-body vs rubric tri-walk
  b. /and-review consistency or /and-review tree — recent chapter or and-experiment spine
  c. /and-ablate — shipped chapter (facet earn-their-place evidence)
  d. targeted auditor fork — most-recently-changed artifact

---

## Pass 1 — 2026-06-11

**Lens:** a — `/and-review pipeline` (schema vs command-body vs rubric tri-walk)

**Verdict:** FINDINGS-PRESENT — 4 HARD, 4 SIGNAL (+ 2 TASTE-FLAGs, no action)

**Report:** `active-project/staff/reviews/pipeline-2026-06-11T000000Z.md`

**Findings filed (parking-lot):**
- pl-2026-06-11-pipeline-001 (HARD) — STRUCT-001: `dialogue.schema.md` describes retired R2 judge as active → fixer
- pl-2026-06-11-pipeline-002 (HARD) — STRUCT-002: `audit-report.schema.md` R2 decision-shard section has no RETIRED annotation → fixer
- pl-2026-06-11-pipeline-003 (HARD) — STRUCT-003: `facet.schema.md` routes per-scene cap enforcement to Phase 5 (should be Phase 4) → fixer
- pl-2026-06-11-pipeline-004 (HARD) — STRUCT-004: `aggregate-state.schema.md` absent from CLAUDE.md schema authority table → fixer
- pl-2026-06-11-pipeline-005 (SOFT) — STRUCT-005: `and-facets.md` Phase 5c wrong orchestrator-critic card path → fixer
- pl-2026-06-11-pipeline-006 (SOFT) — STRUCT-006: CLAUDE.md Rule 13 Phase 4.5 / Phase 5c description incorrect → fixer
- pl-2026-06-11-pipeline-007 (SOFT) — STRUCT-007: `and-write.md` Phase 7 Notes citation claim stale re URI-WRITE-DIALOGUE-COBONDED → fixer
- pl-2026-06-11-pipeline-008 (SOFT) — STRUCT-008: `showrunner-memory.schema.md` Phase 4.6 ref stale (should be Phase 3) → fixer

**Headline finding:** All 4 HARDs trace to DEC-0116 (R2 round retirement) being incompletely propagated across schemas and CLAUDE.md. Axes 2+3 (rubric field refs + rubric residue scan) CLEAN.

**Next lens:** b — `/and-review consistency` or `/and-review tree` on a recent chapter
