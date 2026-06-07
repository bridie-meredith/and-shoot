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
      result_ts: null
      result_note: "Sera establish-leg. UN-DEFERRED 2026-06-07: principal directed 'begin revisions' → AskUserQuestion 'Sera arc (/and-cohere)' (reverses DEC-0108; DEC-0112 confirm-first satisfied by principal answer). Now EXECUTING. Intent: give Sera reader-facing stakes-weight at her c03 introduction (currently a leverage-token, lines 53-56) WITHOUT Taylor naming the Sera-link as motive (fence pl-2026-05-28-002)."
      result: IN-PROGRESS
    - chapter: b01c20
      parking_lot_items: [pl-2026-06-06-cohere-002]
      revise_mode: --from-signals
      executed: false
      result_ts: null
      result_note: "Sera confirm-leg. UN-DEFERRED 2026-06-07 (same principal go). Queued behind c03 establish-leg. Intent: at/near the c20 decommission (line 9, currently 'no person was addressed'), confirm whether the price paid off — Sera's parentage-question status as the arrangement ends — in flat ledger register, fence-respecting."
      result: PENDING
  status: revising
  final_verdict: null   # re-opened 2026-06-07 from dismissed (DEC-0108) per principal go on the Sera arc; executing the revise queue
  closed_at: null
  admin_process_critic:
    - iteration: 0
      verdict: OK-MERGED
      proposal_id: PROP-0042
      summary: "Sera payoff-weight finding merges into PROP-0042 (recurrence 3→4); /and-cohere working as designed; mandatory-before-verdict sequencing rejected; planning-time SOFT flag (PROP-0042) is the strictly-better fix. DEC-0109."
      ts: 2026-06-06T22:30:00Z
  # Phase 3 triage: 1 of 2 load-bearing fails dropped as design-inherent/principal-accepted (DEC-0105).
  # DEC-0108: Phase 4 deferred (analysis posture). REVERSED 2026-06-07: principal directed revisions; AskUserQuestion → "Sera arc (/and-cohere)".
  # Baselines archived: active-project/draft/_archive/2026-06-07-pre-revise-sera/ (c03 + c20).
  # Execution: targeted re-cascade of c03 then c20, then re-thread + re-consolidate + re-cohere c03-c20 to confirm payoff lands.
