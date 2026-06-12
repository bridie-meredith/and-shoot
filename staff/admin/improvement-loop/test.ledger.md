# improvement-loop/test ledger

Tracks which test lens was run each pass so they rotate evenly.
Schema: each entry is a YAML block appended chronologically.

Lens rotation order: pipeline → consistency/tree → ablate → targeted-auditor → (repeat)

---

## Pass 1 — 2026-06-12

```yaml
pass: 1
date: 2026-06-12
lens: /and-review pipeline
target: pipeline (series-wide schema-vs-command-body-vs-rubric tri-walk)
report: active-project/staff/reviews/pipeline-20260612T130757Z.md
verdict: PASS-WITH-NOTES
hard_count: 0
signal_count: 5
taste_count: 1
findings_filed:
  - pl-2026-06-12-pipeline-001  # STRUCT-001: schemas/dialogue.schema.md says R2 judge remains (DEC-0116 retired it)
  - pl-2026-06-12-pipeline-002  # STRUCT-002: schemas/audit-report.schema.md R2 decision-shard section not retired
  - pl-2026-06-12-pipeline-003  # STRUCT-003: and-stitch.md Phase 0.7 misdescribes dialogue as authored at /and-facets
  - pl-2026-06-12-pipeline-004  # STRUCT-004: and-stitch.md Phase 0.5 + Phase 8 retain dead refused-at-R2 field
  - pl-2026-06-12-pipeline-005  # STRUCT-005: and-facets.md Phase 5c orchestrator-critic path in wrong taxonomy dir
  - pl-2026-06-12-pipeline-006  # STRUCT-006: CLAUDE.md schema authority table missing aggregate-state + cohere-state
headline: "6 documentation-drift findings (all SOFT). Schemas + rubrics are post-DEC-0116 correct everywhere except dialogue.schema.md and audit-report.schema.md still reference the retired R2 round. No live tensometer/tens:/URI-026 residue anywhere."
next_lens: /and-review consistency OR /and-review tree (on a recent chapter or the and-experiment spine)
```
