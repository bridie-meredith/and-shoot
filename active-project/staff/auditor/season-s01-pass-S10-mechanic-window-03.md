```yaml
audit:
  scope: season
  target: s01 — Window 3, IDs 330–494 + inserts 497/498/499/503/507 + boundary beats 513/514 + cycle-3 additions 522/523/524
  timestamp: 2026-05-11
  pass: S10 Sweep B — Mechanic verdict cycle 3 (re-fire of cycle 2 STRUCTURAL-RESIDUAL; URI-026 cap = 2, iteration 2)
  source: active-project/theater/proto-lines/s01.bones.md
  tensometer: active-project/theater/facets/tensometer-s01-window-03.md
  combined_verdict: MECHANIC-CLEAN

  cycle_3_resolutions:
    - tens-gate-residual-W3-Scene-330-342: RESOLVED — ID 522 ("the clerk crosses the Fish Gate")
        added at tensometer position 7a, rated 3. Axis: stakes-visibility + reversal-proximity peaks.
        The file physically leaves Taylor's observable range; the recording is beyond reach. Rubric
        parallel: "the stylus stops on the board" (3) — departure IS the reversal. Scene 330-342
        now carries a legitimate rupture beat.
    - tens-gate-residual-W3-Scene-361-375: RESOLVED — ID 523 ("the second clerk releases the record
        book") added at tensometer position 36a, rated 3. Axis: stakes-visibility peaks (single axis
        at peak intensity, satisfying rubric's "OR a single axis at peak intensity" criterion for
        rung 3). The entry is sealed; the second commit is irreversible. Scene 361-375 now carries
        a legitimate rupture beat.
    - tens-gate-residual-W3-Scene-477-494: RESOLVED — ID 524 ("taylor-hebert-flea-bottom faces the
        wall") added at tensometer position 150a, rated 3. Axis: reversal-proximity + body-charge
        (two axes light; satisfies multi-axis criterion). Wall-facing IS the commit before the log
        entries; body-charge peaks at the decision-point. Scene 477-494 now carries a legitimate
        registration beat.
    - fault-001-c3: RESOLVED — Frequency-band section updated: now reads "3s: 7/155 ≈ 4.5%"
        (correct: 7 active 3s at @394, @395, @417, @468, @522, @523, @524; denominator 155 =
        2 boundary-carry + 153 body entries including cycle-3 additions). Stale "6/154 = 3.9%"
        arithmetic is gone. Screen-writer kickback section now present and names all three scene
        deficiencies as RESOLVED (not merely an advisory). Criteria for fault-001-c3 met.

  frequency_band_status:
    count_3s: 7
    denominator: 155
    frequency: "4.5% (below 5% floor; noted)"
    verdict: >
      Below-floor frequency is honest. Anti-pattern 4 (scalar inflation) prohibits manufactured
      improvement. Scene-level structural criteria are the rubric's judgment axis for structural
      acceptance. All named scene deficiencies resolved. Season-average 3-frequency remaining
      below floor is a carried note for screen-writer awareness; it does not re-trigger
      MECHANIC-FAIL at scene-level resolution.

  findings:

    - id: flag-001-c3
      type: flag
      what: >
        ID 524 ("taylor-hebert-flea-bottom faces the wall") at tensometer position 150a rated 3.
        Immediate adjacency: @490 rated 1 (enters loc-flea-bottom-base) precedes; @491 rated 1
        (opens the log) follows. No 2-rated beat immediately adjacent. Broader scene run has 2s
        at @482 and @488, but neither is adjacent to @524.
      why: >
        Rubric adjacency test: "a 3 surrounded by 1s is either a misrating (the lead-in should
        be 2) or a true sudden turn (rare; flag for review)." The citation frames this as a
        commit-beat (sudden physical orientation as decision), which is the rubric's "true sudden
        turn" exception. Two axes light (reversal-proximity + body-charge), satisfying the multi-
        axis criterion for rung 3. Rating is defensible. Flagged for editor awareness at
        and-wrap; stitcher should confirm the beat earns its full-render treatment given the
        1-1 adjacency pattern.
      criteria: ~

    - id: flag-002-c3
      type: flag
      what: >
        Boundary-beat ratings @513 (2) and @514 (2) at tensometer positions 0a and 0b.
        No per-entry axis citations provided. Carried from cycle-2 flag-001-c2.
      why: >
        Rubric rung-2 test: "a facet entry rated 2 must answer: what specifically is charged on
        the face of this beat?" Header context ("Boundary-carry bones (W3 open)") is present but
        per-entry citations are absent. Both ratings remain defensible in surveillance context
        (dispatch acknowledged). No fixer dispatch needed. Editor should confirm axis justification
        for @513 and @514 is stable before stitcher-lock.
      criteria: ~

    - id: flag-003-c3
      type: flag
      what: >
        2-frequency at approximately 30.3% (47/155). Upper edge of the 20-30% target band.
      why: >
        Cycle-3 additions were all rung-3 (no new 2s added); the 2-band overage is carried from
        prior cycles. Not a fault: marginally over-band 2-frequency was not actioned in cycle 1
        or cycle 2 and no individual 2-entry has been identified as a misrating in any prior pass.
        Carried for editor awareness only. No fixer dispatch.
      criteria: ~

    - id: flag-004-c3
      type: flag
      what: >
        ID gaps within Window 3 carried from prior cycles: 348/349, 418/419, 442/443
        (prior deletions); 353, 447, 462, 493 (cycle-1 fault-004 resolution).
        Orphan comment lines at former positions 124 and 153 (tensometer) confirm removals.
      why: >
        No fault. Deletions are legal; gaps must remain visible per schema. Carrying for
        editor awareness. Phase 7 split must not attempt to fill or recover gaps.
      criteria: ~

  prior_cycle_archive:
    cycle_2_combined_verdict: MECHANIC-FAIL
    cycle_2_structural_residuals:
      - CURVE-SHAPE: Scenes 330-342, 361-375, 477-494 had no 3-rated beat and no dramatist
          exception flag. Bones-deficit condition.
      - FREQUENCY-BAND: 4/155 = 2.6%. Below 5% floor. Acknowledged as bones-deficit, not
          miscalibration.
    cycle_2_fault_001_c3: >
      Tensometer frequency-band section read stale arithmetic ("6/154 = 3.9%") and lacked
      the rubric-mandated screen-writer kickback flag naming the three deficient scenes.
      Both resolved in cycle 3.
```
