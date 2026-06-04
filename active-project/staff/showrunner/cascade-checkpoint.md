cascade:
  root: b01c15
  invoked_at: 2026-06-04T00:00:00Z
  invoked_command: /and-substance chapter b01c15 --cascade
  mode: unattended
  last_completed:
    level: chapter
    slug: b01c15
    completed_at: 2026-06-04T00:00:00Z   # Phase 2-6 complete: 4 scenes + contracts persisted; chunk cold-read CHUNK-CLASS-B -> P (DEC-0087); auditor fault-001/002 fixed
  next:
    command: /and-write b01c15
    args: [b01c15]
  reason: continue
  failure: null
  pending_depth_passes: [b01c14]   # DEC-0085 mandatory before book-close (pl-2026-06-04-002); independent of c15
  pending_threading_holds: []
  carried_watches:
    - pl-2026-06-04-c15-001   # HARD at /and-write Phase 6: feed-texture concreteness + S4 ledger-act + axis-slug fence
  armed_downstream:
    - "stitch Phase 8.5 Check 3 (central-event muffle) — chunk_cold_read.voice_risk Signal B"
    - "stitch Phase 9 (auto SHIPPED-WITH-CAVEATS on same Class-B categories per DEC-0087) — cold_read_risk_carry"
