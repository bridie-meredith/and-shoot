cascade:
  root: b01c16
  invoked_at: 2026-06-04T15:10:00Z
  invoked_command: /and-substance chapter b01c16 --cascade
  mode: unattended
  last_completed:
    level: draft
    slug: b01c16
    completed_at: 2026-06-04T16:50:00Z   # chapter-production COMPLETE: Phase 9 SHIPPED-WITH-CAVEATS (Class-B DEC-0090 coupling) + Phase 10 PASS-THREAD
  next:
    command: null   # run complete
    args: []
  reason: complete
  failure: null
  pending_depth_passes: [b01c14, b01c15, b01c16]   # all three gate book-close (mandatory before /and-substance book b02 + /and-review verdict b01); c16 = pl-2026-06-04-c16-001
  pending_threading_holds: []   # Phase 10 PASS-THREAD; b01c17 Phase 0 CLEAR (0 unack-substantive in aggregate-state through c16)
