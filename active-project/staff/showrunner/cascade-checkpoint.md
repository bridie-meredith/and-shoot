# cascade-checkpoint
mode: attended-revision
run: no-ledger-revision b01 (DEC-0115 / PROP-0046-0050)
operator_protocol: RUNBOOK Producing-revisions (book-complete) + worst-first batches
status: COMPLETE
scope: full-book register conversion (ledger -> concrete/human-first)
order: [c01, c02, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c03, c04, c05, c06, c07, c08, c09, c20]
batch: ALL 20 chapters converted + rendered (bones concrete, drafts no-ledger, manuscript + export rebuilt)
completed_at: 2026-06-08
outcome: |
  All 20 chapters re-authored concrete (every ABSTRACTION-AS-SUBJECT bone eliminated; ~330 across the
  book) and re-rendered no-ledger. Final residual ledger-subject sweep across all 20 drafts: CLEAN.
  Consolidated manuscript (active-project/draft/b01-manuscript.md) + reader export
  (completed-works/.../book-one.md + .txt, pure ASCII) rebuilt + colophon updated.
  NOT YET RUN (optional follow-ups): full /and-facets + /and-stitch pipeline per chapter (this was a
  combined revise+render pass, not the 10-facet/8-phase chain); /and-cohere cross-chapter pass on the
  c10-c19 stretch to break any residual structural repetition; /and-review verdict re-judge.
baseline_archive: active-project/draft/_archive/2026-06-08-pre-no-ledger-revise/
voice_target: staff/admin/no-ledger-revision-plan-2026-06-08.md (locked c01-opening re-render) + active-project/voice-exemplar.md
current: {chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}
caps_per_chapter: {bones_retry: 0/1, facet_cycles: 0/3, stitch_p9_retry: 0/1}
note: |
  Register conversion only. Substance arc + signature axes UNCHANGED (DEC-0115 governs prose register,
  not the axis machinery). New gates under test: ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT
  (/and-write Phase 6), LEDGER-REGISTER prohibition (/and-stitch Phase 4), NAIVE-FOLLOW (/and-stitch
  Phase 9). The chain MUST flag the abstract c01 bones (12-14, 18-27) on entry.
