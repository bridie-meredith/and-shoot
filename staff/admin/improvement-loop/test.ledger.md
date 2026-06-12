# Improvement-loop / TEST — lens rotation ledger

Tracks which structural test lens has been run each pass so lenses rotate
and each gets a turn. Append-only.

Lens rotation order:
  (a) /and-review pipeline          — schema ↔ command-body ↔ rubric tri-walk
  (b) /and-review consistency|tree  — cross-level / cross-chapter sweep
  (c) /and-ablate <chapter>         — facet-ablation, evidence for facet triage
  (d) targeted auditor fork         — constraint/state/drift on most-recently-changed artifact

---

## Pass 1 — 2026-06-12

**Lens:** (a) `/and-review pipeline`

**Report:** `active-project/staff/reviews/pipeline-2026-06-12T000000Z.md`

**Verdict:** HARD-FINDINGS — 5 HARD, 1 SIGNAL, 10 TASTE-FLAGs

**Headline findings:**
- STRUCT-001 + RESIDUE-001: `schemas/audit-report.schema.md` R2 decision-shard section
  (lines 106-158) undeprecated despite R2 RETIRED under DEC-0116; URI-026 appears as primary
  authority label in the heading (not a historical annotation).
- STRUCT-002: CLAUDE.md schema authority table missing `cohere-state.schema.md` and
  `aggregate-state.schema.md` — both actively consumed by operational commands.
- STRUCT-003: `design/shoot-v2/rubric-exposition.md` referenced in `and-facets.md` Phase 4
  RUBRIC-FIDELITY source enumeration but does not exist on disk.
- STRUCT-004: `design/shoot-v2/rubric-dialogue.md` referenced in `and-facets.md` Phase 4
  AP-SCAN + RUBRIC-FIDELITY and in `and-write.md` Phase 1.5b but does not exist at either path.
- STRUCT-005 (SIGNAL): `chapters[].cohere_review` field in `and-review.md` not in showrunner
  memory schema — acknowledged-pending PROP-0030 triage, fallback documented.

**Findings filed:** parking-lot items pl-2026-06-12-pipeline-001 through pl-2026-06-12-pipeline-004
(all SOFT; routed to owning agents per audit report § Scope notes).

**Next lens:** (b) `/and-review consistency` or `/and-review tree` on a recent chapter or
the and-experiment spine.
