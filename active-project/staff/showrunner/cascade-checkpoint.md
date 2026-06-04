cascade:
  root: b01c16
  invoked_at: 2026-06-04T15:10:00Z
  invoked_command: /and-substance chapter b01c16 --cascade
  mode: unattended
  last_completed:
    level: facets
    slug: b01c16
    completed_at: 2026-06-04T16:20:00Z   # /and-facets: 10/10 facets audience-gate ACCEPT (2 cycles; NI:6 DEC-0090 fix); audit 0 HARD; FOLLOWABLE+ALIVE
  next:
    command: /and-stitch
    args: [b01c16]
  reason: continue
  failure: null
  pending_depth_passes: [b01c14, b01c15]   # gate book-close, NOT c16; carried forward
  pending_threading_holds: []   # b01c16 Phase 0 CLEAR per aggregate-state through c15
