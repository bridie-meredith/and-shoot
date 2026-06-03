cohere_state:
  book: b01
  range: c06-c12
  invocation_ts: 20260603T151822Z
  status: converged
  iteration_count: 2
  max_iter: 3
  flags: {strict: false, dry_run: false}
  verdict_trace:
    - iteration: 0
      verdict: FAIL-COHERE
      report_path: active-project/staff/reviews/cohere-b01-c06-c12-20260603T151822Z.md
      failed_axes: [naive-Q6-apparatus-register-cumulative-load]
      load_bearing_fails: 1
    - iteration: 1
      verdict: CAUTION-COHERE
      report_path: active-project/staff/reviews/cohere-naive-b01-c06-c12-20260603T152850Z.md
      failed_axes: []
      caution_axes: [naive-Q6-body-register-residual-c10-c12, naive-Q7-subsection-tells-more-than-climaxes, dramatist-structural-routed-to-pl-2026-06-03-006]
      load_bearing_fails: 0
      note: "prologue-variation (DEC-0081 B) cleared the load-bearing naive-Q6 FAIL->CAUTION (7 distinct openings); residual CAUTIONs non-blocking, routed"
  closed_at: 20260603T152850Z
  revise_queue: []
  final_verdict: CAUTION-COHERE
  combined_file: active-project/staff/reviews/cohere-b01-c06-c12-20260603T151822Z.combined.md
  precondition: "all 7 chapters shipped (c10/c11/c12 SHIPPED-WITH-CAVEATS, c06-c09 PASS-variants); drafts on disk"
  note: "diagnosed concern: apparatus-register density N=7 c06-c12; 3rd consecutive SHIPPED-WITH-CAVEATS (DEC-0072/0074/0078); cohere reaffirmed DEC-0073/0075/0077/0078/0079/0080"
