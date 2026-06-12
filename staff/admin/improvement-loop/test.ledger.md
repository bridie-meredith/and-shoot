# Improvement-loop TEST ledger

Tracks which test lens ran each pass, in rotation, so each lens gets a turn.

## Rotation order

```
a. /and-review pipeline   — schema vs command-body vs rubric tri-walk
b. /and-review consistency or tree — cross-level / cross-chapter sweep on a recent chapter or spine
c. /and-ablate             — facet ablation on a shipped chapter (which facets earn their place)
d. targeted auditor fork   — constraint/state/drift check on the most-recently-changed artifact
```

---

## Ledger

### Pass 1 — 2026-06-12

**Lens:** (a) `/and-review pipeline`

**Trigger:** First run; ledger initialized. Prior pipeline runs (2026-06-07) predated
DEC-0115 (no-ledger overhaul, 2026-06-08) and DEC-0116 (slim /and-facets, retire R2 +
Phase 5b audience-gate, 2026-06-12). This pass focused on post-DEC-0115/0116 drift.

**Report:** `active-project/staff/reviews/pipeline-20260612T071006Z.md`

**Verdict:** 3 HARD + 2 SIGNAL

**Headline:** R2 retirement left three live zombie references in command bodies and schemas;
CLAUDE.md schema table has two missing live schemas.

**Findings filed:**

| ID | Severity | Location | Description |
|----|----------|----------|-------------|
| pl-2026-06-12-pipeline-001 | SOFT | `schemas/audit-report.schema.md` + `staff/orchestrator-critic/card.md` | STRUCT-NEW-001: R2 decision-shard infrastructure (F-R2 classes, `.r2-decisions.md`, B7/F7-r2 verdict trigger) is retired under DEC-0116 but remains live in both files. |
| pl-2026-06-12-pipeline-002 | SOFT | `and-stitch.md` + `schemas/stitch-render-log.schema.md` | STRUCT-NEW-002: `refused-at-R2` field in Phase 8 STATS is undefined in the render-log schema. |
| pl-2026-06-12-pipeline-003 | SOFT | `.claude/commands/and-cut.md` | STRUCT-NEW-003: `faceted-r2` listed as valid current chapter status without RETIRED annotation, contrary to showrunner-memory.schema.md. |
| pl-2026-06-12-pipeline-004 | SOFT | `CLAUDE.md` | STRUCT-NEW-004: schema authority table missing `cohere-state.schema.md` + `aggregate-state.schema.md`; directory map missing `theater/facets/_inflight/` + `theater/facets/_archive/`. |
| pl-2026-06-12-pipeline-005 | SOFT | `.claude/commands/and-stitch.md` | STRUCT-NEW-005: lines 204 + 349 describe exposition authoring as "R1+R2"; post-DEC-0116 it is R1 only. |

**Open parking-lot items surfaced (Rule 14):**
- pl-2026-05-25-018 (SOFT, open): axes_held schema ambiguity — still needs pipeline tri-walk disposition.

**Next lens in rotation:** (b) `/and-review consistency` or `/and-review tree` on a recent
chapter (candidate: the and-experiment spine or b01 final chapter b01c20).
