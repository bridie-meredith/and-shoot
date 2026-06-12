# Improvement-loop TEST ledger
# Schema: one entry per run, append-only.
# Rotation: a, b, c, d (four lenses). Each lens gets a turn before repeating.
# Lenses:
#   a) /and-review pipeline — schema vs command-body vs rubric tri-walk
#   b) /and-review consistency or /and-review tree on a recent chapter
#   c) /and-ablate on a shipped chapter
#   d) targeted auditor fork on the most-recently-changed artifact

---

## Run 1 — 2026-06-12T151320Z

lens: a — /and-review pipeline (schema vs command-body vs rubric tri-walk)
report: active-project/staff/reviews/pipeline-2026-06-12T151320Z.md
verdict: FAIL
hard_count: 2
signal_count: 7
taste_flag_count: 2

headline: Two HARDs from DEC-0116 retirement residue not yet cleaned up.
  dialogue.schema.md:3 still describes R2 dialogue judge as "remains" (STRUCT-030 HARD);
  audit-report.schema.md lines 106-157 R2 decision-shard section undeprecated (STRUCT-031 HARD).
  Seven SIGNALs covering refused-at-R2 stale fields, missing dialogue-citation
  exception in and-write.md + bones.schema.md, stale rubric-exposition.md ghost path,
  stale stitch-profile R2 description, wrong Phase 5 vs Phase 4 in facet.schema.md,
  and CLAUDE.md authority table missing aggregate-state + cohere-state schemas.

findings_filed:
  - pl-2026-06-12-pipeline-001 → fixer: schemas/dialogue.schema.md line 3 (HARD)
  - pl-2026-06-12-pipeline-002 → fixer: schemas/audit-report.schema.md R2 section (HARD)
  - pl-2026-06-12-pipeline-003 → fixer: and-facets.md line 333 ghost rubric (SOFT)
  - pl-2026-06-12-pipeline-004 → fixer: stitch-profile.schema.md R2 description (SOFT)
  - pl-2026-06-12-pipeline-005 → fixer: and-stitch.md refused-at-R2 x3 (SOFT)
  - pl-2026-06-12-pipeline-006 → fixer: and-write.md + bones.schema.md dialogue-citation (SOFT)
  - pl-2026-06-12-pipeline-007 → fixer: facet.schema.md scene-map Phase 5 vs 4 (SOFT)
  - pl-2026-06-12-pipeline-008 → fixer: CLAUDE.md schema table 2 missing entries (SOFT)
  - pl-2026-06-12-pipeline-009 → fixer: CLAUDE.md proto-lines consumption stale (SOFT)

next_lens: b — /and-review consistency or /and-review tree on a recent chapter
  Suggestion: /and-review tree b01 or /and-review consistency (cross-chapter
  handoff sweep) — the and-experiment track has progressed through Book II;
  a consistency run on that experimental spine would surface handoff drift.
  Alternatively: /and-review consistency on the active-project (b01) cross-chapter
  handoff chain since /and-substance book was last run.
