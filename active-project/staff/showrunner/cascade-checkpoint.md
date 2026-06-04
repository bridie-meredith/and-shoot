cascade:
  root: b01c16
  invoked_at: 2026-06-04T15:10:00Z
  invoked_command: /and-substance chapter b01c16 --cascade
  mode: unattended
  last_completed:
    level: null
    slug: null
    completed_at: null
  next:
    command: /and-substance
    args: [chapter, b01c16]
  reason: chapter-production-start
  failure: null
  pending_depth_passes: [b01c14, b01c15]   # gate book-close, NOT c16; carried forward
  pending_threading_holds: []   # b01c16 Phase 0 CLEAR per aggregate-state through c15
