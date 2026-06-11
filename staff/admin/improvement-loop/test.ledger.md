# Improvement-Loop / Test Ledger

Rotation order: (a) pipeline → (b) consistency/tree → (c) ablate → (d) targeted auditor → repeat

---

## Run log

<!-- Each entry: date | lens | verdict | findings filed | next lens -->

| # | Date | Lens | Verdict | Findings | Next |
|---|------|------|---------|----------|------|
| 1 | 2026-06-11 | `/and-review pipeline` | PASS-WITH-SIGNALS | 3 faults + 8 flags filed; 4 parking-lot items (pl-2026-06-11-pipeline-001 through 004); rubric axis incomplete | (b) consistency/tree |

---

### Run 1 — 2026-06-11 — `/and-review pipeline`

**Verdict:** PASS-WITH-SIGNALS  
**Report:** `active-project/staff/reviews/pipeline-2026-06-11T000000Z.md`

**Faults (3 — actionable, fixer-class):**
- `fault-001` — `schemas/audit-report.schema.md` retains live R2 decision-shard section (DEC-0116 retired R2; stale Phase 6 reference). → `pl-2026-06-11-pipeline-001` (SOFT)
- `fault-002` — `and-write.md` Phase 4 loads `series.theme` which does not exist in showrunner-memory schema. → `pl-2026-06-11-pipeline-002` (HARD)
- `fault-003` — `and-facets.md` Phase 5c reads orchestrator-critic from wrong path (`staff/audience/and-facets-orchestrator-critic/`) instead of `staff/orchestrator-critic/card.md`. → `pl-2026-06-11-pipeline-003` (HARD)

**Flags (8 — advisory, no fixer dispatch):**
- `fault-004` — `scene-map.schema.md` uses `scene_id` but memory schema uses `slug`
- `fault-005` — CLAUDE.md schema table missing `aggregate-state` + `cohere-state`; command table missing `/and-cohere`
- `fault-006` — `dialogue.schema.md` example uses old `s01e01` episode format
- `fault-007` — `facet.schema.md` tensometer section at definition depth; `@<proto-line-id>` vs `flat_id` vocab drift
- `fault-008` — `and-stitch.md` Phase 0.6 references "R1+R2" post DEC-0116
- `fault-009` — `chapters[].cohere_review` absent from memory schema (pending PROP-0030 triage)
- `fault-010` — `chapters[].coherence_review` absent from memory schema (active pipeline write) → `pl-2026-06-11-pipeline-004` (SOFT)
- `fault-011` — `and-project.md` Phase 1 stub uses `series.substance: ~` null vs complex-object schema shape

**Scope gap:** Rubric axis (`design/shoot-v2/rubric-*.md`) was not completed in this pass. A follow-on rubric pass is needed before this tri-walk is fully closed on all 5 axes.

**Next lens:** (b) `/and-review consistency` or `/and-review tree` on a recent chapter
