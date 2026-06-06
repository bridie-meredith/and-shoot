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
      result_note: "naive-q6 dropped at triage (DEC-0105 design-accepted); only Sera-payoff item survives; Phase 4 fire-vs-defer routed to principal per Rule 13"
  status: open
  final_verdict: null
  closed_at: null
  admin_process_critic: []
  # Phase 3 triage: 1 of 2 load-bearing fails dropped as design-inherent/principal-accepted (DEC-0105).
  # Book is complete+shipped+verdict-PASSED. Phase 4 NOT auto-fired; principal decision pending.
