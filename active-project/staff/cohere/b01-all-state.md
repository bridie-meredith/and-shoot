# Cohere State — b01 / all — schema: schemas/cohere-state.schema.md

cohere_state:
  version: 1
  book: b01
  range: all
  invocation_ts: 2026-06-06T00:00:00Z
  last_touched_ts: 2026-06-06T00:00:00Z
  iteration_count: 1
  max_iter: 3
  flags:
    strict: false
    dry_run: false
  verdict_trace:
    - iteration: 0
      verdict: FAIL-COHERE
      report_path: active-project/staff/reviews/cohere-b01-all-20260606T215813Z.md
      ts: 2026-06-06T22:00:00Z
      failed_axes: [naive-q6, dramatist-promise-payoff]
      caution_axes: [naive-q2, naive-q3, naive-q4, naive-q5, naive-q7, naive-q8, dramatist-arc, dramatist-antagonist, dramatist-scene-shape]
      load_bearing_fails: 2
  revise_queue:
    - chapter: b01c03
      parking_lot_items: [pl-2026-06-06-cohere-001]
      revise_mode: --from-signals
      executed: false
      result: null
      result_ts: null
      result_note: "naive-q6 dropped at triage (DEC-0105 design-accepted); only Sera-payoff item survives; Phase 4 DEFERRED per DEC-0108 (accept-with-notes; book complete+accepted; surface as analysis input)"
      result: SKIPPED
  status: dismissed
  final_verdict: null   # FAIL-COHERE on record, but principal-accepted-with-notes per DEC-0108 (not converged, not held — explicit revise-dismissal on a finished+accepted book)
  closed_at: 2026-06-06T22:15:00Z
  admin_process_critic:
    - iteration: 0
      verdict: OK-MERGED
      proposal_id: PROP-0042
      summary: "Sera payoff-weight finding merges into PROP-0042 (recurrence 3→4); /and-cohere working as designed; mandatory-before-verdict sequencing rejected; planning-time SOFT flag (PROP-0042) is the strictly-better fix. DEC-0109."
      ts: 2026-06-06T22:30:00Z
  # Phase 3 triage: 1 of 2 load-bearing fails dropped as design-inherent/principal-accepted (DEC-0105).
  # DEC-0108: Phase 4 NOT fired. Sera-payoff drop recorded as SOFT pl-2026-06-06-cohere-001, folded into analysis.
  # Book stands as shipped (PASS-WITH-NOTES). Chain re-runnable on demand if analysis reveals material damage.
