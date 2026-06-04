cascade:
  root: b01c16
  invoked_at: 2026-06-04T15:10:00Z
  invoked_command: /and-substance chapter b01c16 --cascade
  mode: unattended
  last_completed:
    level: bones
    slug: b01c16
    completed_at: 2026-06-04T15:40:00Z   # /and-write Phase 7 emit: 27 bones / 3 scenes; bone-gate PASS (0 HARD, 2 advisory SIGNAL accepted); audience 3/3 SUBSTANCE-FELT
  next:
    command: /and-review
    args: [bones, b01c16]
  reason: continue
  failure: null
  pending_depth_passes: [b01c14, b01c15]   # gate book-close, NOT c16; carried forward
  pending_threading_holds: []   # b01c16 Phase 0 CLEAR per aggregate-state through c15
