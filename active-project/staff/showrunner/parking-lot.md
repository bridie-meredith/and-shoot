# parking-lot — schema: schemas/parking-lot.schema.md
#
# Cross-chunk watch-items targeting future command invocations.
# Append-only. Resolution stamps add fields; entries are never deleted.
# Read by Phase 0 of every re-runnable command per CLAUDE.md Rule 14.

parking_lot:
  version: 1
  items:

    - id: pl-2026-05-25-001
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-substance chapter b01c01 Phase 5 (fixer fault-001)"
      target:
        command: /and-substance
        scope: "chapter b01c03"
        phase: Phase 3
      severity: HARD
      description: |
        cl01b in series.substance.cost_ledger declares gain "social_tether-prot-rise +2"
        but only +1 settled at b01c01s03 (ward-layer half — Oswyn-categorization).
        The remaining +1 (court-layer half — Otto's awareness of the rescue via
        Jarvis Coin) must anchor at b01c03. b01c03's chapter contract currently
        holds social_tether-prot-rise in axes_held ("tether has not formed through
        Jarvis yet; the offer is pending"). Phase 3 at b01c03 must move
        social_tether-prot-rise into axes_in_motion with
        target_delta_magnitude: 1.0 and cost_ledger_anchor: cl01b. Otherwise the
        +2 cl01b gain remains under-anchored and the book-level roll-up's tether
        accounting carries an undeclared partial-settle indefinitely.
      context_refs:
        - active-project/staff/showrunner/memory.md:1698  # b01c01 persist comment
        - active-project/staff/showrunner/memory.md:1821  # b01c01s03 notes field
        - active-project/staff/reviews/b01c01-scenes-audit-2026-05-25.md
        - active-project/staff/showrunner/_drafts/b01c01-draft-2026-05-25.md  # authoring notes G4 block
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-002
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-substance chapter b01c01 Phase 5 (audience trio soft watch)"
      target:
        command: /and-write
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        Audience trio (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant)
        flagged at /and-substance chapter b01c01 Phase 5: the Wren stitch-house
        plant must land as quietly loaded, not background noise. Dormancy framing
        is structurally correct at the contract level — but bones in s01 and s03
        that touch the stitch-house (smell two lanes over, Taylor not looking
        toward it) need prose texture that makes the sensory plant intentional
        rather than ambient detail. Not a contract change; a write-time prose
        discipline.
      context_refs:
        - active-project/audience/cape-fic-reader/stm.md
        - active-project/audience/dark-fantasy-reader/stm.md
        - active-project/audience/worm-canon-pedant/stm.md
        - active-project/staff/showrunner/memory.md:1701  # b01c01 persist comment SOFT-WATCH line
      status: resolved
      resolved_at: 2026-05-25T00:00:00Z
      resolved_by: "/and-write b01c01 Phase 7 emit"
      resolution_note: |
        Stitch-house plant authored as three concrete physical bones, not ambient detail:
        s01n02 (flat_id 2) "the tallow smoke crosses the stitch-house lane" — opening
        sensory ground naming the stitch-house as a working-class craft district fact;
        s03n08 (flat_id 25) "the tallow smoke layers the lane-floor" — chapter-close
        confirming the smell continues as the cost-bearer's location physical-presence;
        s03n07 (flat_id 24) "taylor faces the alley-mouth" — the body-direction that
        excludes the stitch-house, enacted positively per the no-negation rule.
        s03n10 (flat_id 27) "wren-stitch-maker-flea-bottom-ward faces taylor-hebert-kl-122ac"
        (added at Phase 5) delivers the chapter-close cost-bearer orientation that
        the handoff_out asserts. Audience Phase 6 bone-gate verdicts: all three personas
        SUBSTANCE-FELT; cape-fic-reader specifically noted "three-station dormancy arc
        complete (s01n02 smoke → s02n09 in the crowd unregistered → s03n10 orienting
        toward Taylor), reader knows who it is, Taylor does not." Decoration test passed.

    - id: pl-2026-05-25-003
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-substance book b01 Phase 5 (auditor soft findings, backfilled 2026-05-25)"
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Two non-blocking soft findings carried from /and-substance book b01
        Phase 5 ACCEPT (attempt 3) into /and-write runs across the book:
        (a) SOFT-CURVE-moral_framework — the book contract distributes the
            6-rank moral_framework collapse across chapters as uniform drops;
            the series trajectory concentrates the collapse at 3 specific
            deltas (d03 first crack, d07 systematic-override-rationalized,
            d12 irrevocable-Khepri-repetition). Per-chapter bone-level
            moral_framework movements should respect concentration rather than
            uniform distribution.
        (b) 8 INFERENTIAL-ANCHOR / NAMING-INCONSISTENCY findings on the
            cost_ledger — inference-derived anchor relationships and a mixed
            slug naming convention. Non-blocking but noted for /and-write
            cross-checks on cost-ledger entries.
      context_refs:
        - active-project/staff/showrunner/memory.md:1601  # book b01 persist soft-findings comment
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null
