# improvement-loop/test — lens rotation ledger

Tracks which structural test lens was run last so each gets a turn.

Lenses (rotation order):
  a. /and-review pipeline — schema ↔ command-body ↔ rubric tri-walk
  b. /and-review consistency OR /and-review tree on a recent chapter / and-experiment spine
  c. /and-ablate on a shipped chapter (facet contribution evidence)
  d. targeted auditor fork on the most-recently-changed artifact

---

## Runs

### Run 1 — 2026-06-12T08:10:39Z
lens: a — /and-review pipeline (schema ↔ command-body ↔ rubric tri-walk)
verdict: FAIL (HARD: 1, SIGNAL: 2, TASTE: 3)
report: active-project/staff/reviews/pipeline-2026-06-12T081039Z.md

findings filed:
  - STRUCT-001 (HARD) → pl-2026-06-12-pipeline-001
      orchestrator-critic card (staff/orchestrator-critic/card.md) calibrated against
      retired /and-season command; dead criteria applied to /and-review verdict. Book-level
      quality gate is a non-gate. Requires principal dispatch to rewrite the card.
  - STRUCT-002 (SIGNAL) → pl-2026-06-12-pipeline-002
      schemas/audit-report.schema.md §"R2 decision-shard frontmatter" not marked retired;
      references /and-facets-r2 + Phase 6 (neither exists in current chain).
  - STRUCT-003 (SIGNAL) → pl-2026-06-12-pipeline-003
      CLAUDE.md schema authority table missing aggregate-state.schema.md and
      cohere-state.schema.md.
  - TASTE-001/002/003: episode:-field compat, historical /and-season lift-source
    reference in and-review.md, /and-season version history in card. No action.

next lens in rotation: b — /and-review consistency OR /and-review tree on a recent chapter
