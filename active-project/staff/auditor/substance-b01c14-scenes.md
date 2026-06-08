```yaml
audit:
  scope: chapter
  target: b01c14
  timestamp: 2026-06-03
  findings:

    - id: fault-001
      type: fault
      what: >
        handoff_out character_state (memory.md line 8346) claims "social_tether-antag rank 9
        (non-extractable confirmed)" and open_threads (line 8340) repeats "social tether: at
        structural peak; non-extractable." The scene draft's roll-up table shows start 6.0 +
        delta 1.5 = 7.5. S04 substance_delta notes themselves state "held at 7.5" — the scene
        author correctly computed the endpoint but the handoff_out carries a contradicting value
        (+1.5 above what the chapter's own deltas deliver). The claimed rank 9 would require
        +3.0 of movement from start 6.0, not the +1.5 this chapter allocates.
      why: >
        handoff_out is the source consumed by b01c15 Phase 0 as its starting baseline for
        social_tether-antag. A handoff asserting rank 9 when the measured endpoint is 7.5
        overstates the axis by 1.5 and will cause b01c15 to author from a false floor, compounding
        ledger error forward. Remaining cl-antag-d03 and cl-antag-d10 capacity is miscalculated
        as zero when +1.5 remains undrawn.
      criteria: >
        handoff_out character_state and open_threads must assert social_tether-antag at the rank
        that follows from start 6.0 plus this chapter's declared delta of +1.5, i.e. rank 7.5.
        If any undistributed cl-antag-d03 tranche is intended to be drawn in this chapter, the
        scene contracts must declare it explicitly with a corresponding delta increase; otherwise
        the handoff_out must reflect 7.5.

    - id: fault-002
      type: fault
      what: >
        handoff_out character_state (memory.md line 8346) claims "position-prot-rise rank 6.5"
        and open_threads (line 8340) states "position-prot-rise at peak (rank 6.5)." The scene
        draft's roll-up table shows start 5.0 + delta 1.0 = 6.0. S04 substance_delta notes state
        "peak position confirmed at 6.0." The handoff_out is +0.5 above the chapter's declared
        and computed endpoint.
      why: >
        b01c15 Phase 0 will read handoff_out as its authoritative starting baseline. An overstated
        position-prot-rise baseline of 6.5 (rather than the earned 6.0) will misdirect any future
        position-axis allocation and misrepresent cl-d07a completion. cl-d07a total gain is +2.0;
        the chapter contract correctly draws the final +1.0 here (confirming c10's prior +1.0 draw),
        completing the ledger at 6.0. The handoff claiming 6.5 implicitly invents an extra +0.5
        draw that no scene accounts for.
      criteria: >
        handoff_out character_state and open_threads must assert position-prot-rise at the rank
        that follows from start 5.0 plus this chapter's declared delta of +1.0, i.e. rank 6.0.
        The cl-d07a completion note remains valid at rank 6.0.

    - id: fault-003
      type: fault
      what: >
        S04 substance_delta notes for cl04 state "cl04 COMPLETES: figure detained, outcome
        recorded, closure retroactively naming the Wren omission via shared column-logic — cl04
        closed." S03 notes state "cl04 first half complete." Together S03 and S04 draw +0.5 + +0.5
        = +1.0 of relational_anchor_status in this chapter. The cl04 ledger entry (memory.md
        line 1390–1393) declares a total gain of relational_anchor_status +3. The chapter
        contract (memory.md line 8289) declares target_delta_magnitude: 1.0 for cl04 at c14,
        with the audit brief confirming "+1.5 more at c15." The COMPLETES language in S04 is
        therefore false at the chapter scope: cl04 draws only +1.0 of its +3 total here; it does
        not complete. Only the c14 chapter-level tranche of cl04 completes.
      why: >
        "cl04 COMPLETES" in S04 notes and "cl04 closed" are unambiguous ledger-closure language.
        A reader of these scene notes (including /and-write Phase 6 bone-gate and /and-review bones)
        will treat cl04 as fully settled, which contradicts the remaining +2.0 allocation slated
        for c15 and beyond. If this language propagates to the handoff_out or the bones file, it
        will suppress the c15 cl04 draw.
      criteria: >
        S04 notes for cl04 must not claim the ledger entry closes or completes at the book or
        series level. The correct language is that the c14 chapter-level tranche of cl04 is
        complete (+1.0 drawn of +3.0 total), with +2.0 remaining for future chapters. The
        retroactive Wren-naming event may remain as a narrative beat for this tranche.

    - id: flag-001
      type: flag
      what: >
        Roll-up table and scene contracts are internally consistent and match aggregate-state.md
        baselines on all four moving axes: relational_anchor_status start 4.5, social_tether-antag
        start 6.0, position-prot-rise start 5.0, moral_legibility_to_self start 5.5. Scene-level
        sums: +1.0 / +1.5 / +1.0 / +0.5 all match chapter targets exactly.
      why: >
        No action required. Noting for completeness that roll-up arithmetic and baseline sourcing
        are clean.

    - id: flag-002
      type: flag
      what: >
        All four chunk-tag axes ([event:]/[image:]/[force:]/[mechanism:]) are applied to
        load-bearing spans across all four scenes. Central event (figure detained in S04),
        causal mechanism (confirmation written to response-sheet in S03, detention-mechanism-via-
        feed in S04, dragonstone-inference-from-absence in S01), how confirmation reaches Otto
        (jarvis-packet-arrives / response-sheet-sealed-for-jarvis / cl04-ledger-closure all
        tagged), and how cloth-merchant absence signals Dragonstone (mechanism: dragonstone-
        inference-from-absence / force: dragonstone-pressure-mediated) are all tagged.
      why: >
        No action required. Chunk-tag protocol satisfied.

    - id: flag-003
      type: flag
      what: >
        moral_legibility_to_self is declared in axes_in_motion at S03 (+0.25) and S04 (+0.25),
        totaling +0.5. The chapter goal names the moral_legibility thesis as central. Both scene
        chunks provide concrete cause: S03's accounting run with the stylus held above the closed
        entry and the accuracy named; S04's held look at the two column-positions (closed entry /
        Wren non-entry). THEMATIC-AXIS-UNDECLARED check: PASS.
      why: >
        No action required.

    - id: flag-004
      type: flag
      what: >
        All held axes carry rationale in every scene. No axis appears to move in prose while
        listed held, and no axis listed in motion lacks a described prose event driving it.
        Held-axis discipline is clean.
      why: >
        No action required.

    - id: flag-005
      type: flag
      what: >
        S02 density_target is declared 0.7-0.9, S03 and S04 are 0.8-1.0. The schema band for
        scene is 0.6-0.9. S03 and S04 upper bounds of 1.0 exceed the declared scene band
        ceiling of 0.9. This is a ceiling overshoot on the target declaration, not on measured
        density (measured density is not yet computed at chunk phase). The chunk_targets scene
        band in memory.md line 1464 states density 0.6-0.9.
      why: >
        Overstating the density ceiling target invites /and-write to author above the schema
        band. Not a blocking fault at this phase since bones are not yet authored, but worth
        correcting in the scene contracts before /and-write runs.
      
```
