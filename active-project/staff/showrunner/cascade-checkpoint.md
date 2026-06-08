# cascade-checkpoint
mode: attended-revision
run: no-ledger-revision b01 (DEC-0115 / PROP-0046-0050)
operator_protocol: RUNBOOK Producing-revisions (book-complete) + worst-first batches
status: IN-PROGRESS
scope: full-book register conversion (ledger -> concrete/human-first)
order: [c01, c02, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c03, c04, c05, c06, c07, c08, c09, c20]
batch: proof (c01, c02) — verify new gates produce the locked voice before full spend
baseline_archive: active-project/draft/_archive/2026-06-08-pre-no-ledger-revise/
voice_target: staff/admin/no-ledger-revision-plan-2026-06-08.md (locked c01-opening re-render) + active-project/voice-exemplar.md
current: {chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}
caps_per_chapter: {bones_retry: 0/1, facet_cycles: 0/3, stitch_p9_retry: 0/1}
note: |
  Register conversion only. Substance arc + signature axes UNCHANGED (DEC-0115 governs prose register,
  not the axis machinery). New gates under test: ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT
  (/and-write Phase 6), LEDGER-REGISTER prohibition (/and-stitch Phase 4), NAIVE-FOLLOW (/and-stitch
  Phase 9). The chain MUST flag the abstract c01 bones (12-14, 18-27) on entry.
