cascade:
  root: b01c08
  invoked_at: 2026-05-31T16:00:00Z
  invoked_command: /and-substance chapter b01c08 --cascade
  last_completed:
    level: stitch-failed
    slug: b01c08
    completed_at: 2026-05-31T21:00:00Z
  next:
    command: /and-write
    args: [b01c08, revise, --from-signals]
  reason: halted-on-failure
  failure: |
    /and-stitch b01c08 Phase 9 FAIL.
    - Cold-read: CONTINUE=no, AIRLESS, central events recovered. Complaint matches
      chunk_cold_read.cold_read_risk_carry verbatim ("two names logged + a wider
      coverage map" → "two thin beats, no identifiable narrator").
    - Staging-review: 8 SIGNAL / 4 spine-promotion BLOCKING; finding-002 STAGE on
      @6 (sole axis-move central-event bone) = unconditional FAIL per URI-STITCH-
      SPINE-STAGING (un-staged central event = decomposition defect).
    - Phase 8.5 coherence PASS (substance-aware-reader) but separated-scoring
      AIRLESS-on-central-event = FAIL per PROP-0022.
    - Even though cold-read leg matches pre-disposed Class B (DEC-0060) and would
      route to SHIPPED-WITH-CAVEATS alone, the staging spine-promotion FAIL is
      INDEPENDENT — re-decompose, do not polish.
    Route: /and-write b01c08 revise --from-signals (consume staging report's 4
    spine-promotion findings + cold-read AIRLESS findings; re-cascade /and-facets
    + /and-stitch).
