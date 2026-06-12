# improvement-loop/test — lens rotation ledger
#
# Each row records one test run. Lenses rotate a→b→c→d→a...
# a = /and-review pipeline (schema vs command-body vs rubric tri-walk)
# b = /and-review consistency or /and-review tree (cross-level sweep or recent chapter)
# c = /and-ablate on a shipped chapter (facet earn-their-place evidence)
# d = targeted auditor fork on most-recently-changed artifact

runs:

  - run: 1
    date: 2026-06-12
    lens: a  # /and-review pipeline
    report: active-project/staff/reviews/pipeline-20260612T061200Z.md
    scope: >
      Full tri-walk scoped to post-2026-06-07 delta (DEC-0116 slim-facets +
      DEC-0115 no-ledger). All five legs covered. Prior pipeline pair
      (20260607T004417Z + legs23-20260607T010305Z) provided the baseline.
    verdict: FINDINGS-PRESENT
    hard_count: 1
    signal_count: 7
    pass_count: 3
    headline: >
      1 HARD (STRUCT-026: rubric-exposition.md dead pointer in and-facets.md
      Phase 4 RUBRIC-FIDELITY source enumeration — incomplete DEC-0111 fix).
      4 SIGNAL: STRUCT-027 (rubric-dialogue path missing), STRUCT-028 (two
      schemas absent from CLAUDE.md table), RESIDUE-001 (audit-report R2 section
      undeprecated), RESIDUE-002 (orchestrator-critic F7-r2/B7 dead machinery).
      1 parking-lot item resolved inline (pl-2026-05-31-009 cross-chapter aliveness
      → routed to /and-review cohere Q6). 5 new parking-lot items opened (pl-2026-06-12-pipeline-001 through -005).
    findings_filed:
      - pl-2026-06-12-pipeline-001  # HARD: STRUCT-026 rubric-exposition dead pointer
      - pl-2026-06-12-pipeline-002  # SOFT: STRUCT-027 rubric-dialogue path missing
      - pl-2026-06-12-pipeline-003  # SOFT: RESIDUE-001 audit-report R2 undeprecated
      - pl-2026-06-12-pipeline-004  # SOFT: RESIDUE-002 orchestrator-critic dead machinery
      - pl-2026-06-12-pipeline-005  # SOFT: STRUCT-028 CLAUDE.md schema table gap
    parking_lot_resolved:
      - pl-2026-05-31-009  # cross-chapter aliveness question → /and-review cohere Q6
    next_lens: b  # /and-review consistency or /and-review tree on a recent chapter
    next_lens_suggestion: >
      /and-review consistency b01 — cross-level sweep on the completed book,
      especially the chapter handoff chain for the and-experiment arc (Book II
      is now complete per recent commits). Or /and-review tree b01c20 if a
      per-chapter depth check is more useful.
