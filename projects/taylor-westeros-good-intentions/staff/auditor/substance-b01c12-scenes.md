audit:
  scope: chapter
  target: b01c12
  timestamp: 2026-06-03
  gate: /and-substance chapter b01c12 Phase 5 contract audit
  sources_read:
    - active-project/staff/showrunner/b01c12-draft.md
    - active-project/staff/showrunner/memory.md (chapters[b01c12] + series.substance + cost_ledger)
    - active-project/staff/showrunner/aggregate-state.md (close-of-c11 authoritative axis ranks)

  findings:

    # -------------------------------------------------------------------------
    # CHECK 1 — SUM ROLL-UP ±1
    # -------------------------------------------------------------------------

    - id: fault-001
      type: pass
      what: >
        Roll-up comment table (b01c12-draft.md lines 10–15) vs independent
        scene-by-scene tally from axes_in_motion[] entries.
      why: >
        Independent tally matches the draft's own comment table exactly on all
        five chapter-target axes. No discrepancy.
      criteria: null
      detail: |
        axis                       s01    s02    s03    s04    SUM    TARGET   MATCH
        moral_framework             0      0      0     -1.0   -1.0   -1.0     EXACT
        capability                 +0.5    0      0     +0.5  +1.0   +1.0     EXACT
        relational_anchor_status    0      0     +1.0    0    +1.0   +1.0     EXACT
        social_tether-prot-rise    +0.5    0      0      0    +0.5   +0.5     EXACT
        position-prot-rise          0      0     +1.0    0    +1.0   +1.0     EXACT
        All five axes within ±0 of target (exact match; ±1 tolerance not consumed).

    # -------------------------------------------------------------------------
    # CHECK 2 — SCHEMA VALIDITY PER SCENE
    # -------------------------------------------------------------------------

    - id: fault-002
      type: pass
      what: >
        Schema validity of axes_in_motion[] and axes_held[] entries across all
        four scenes (b01c12s01–s04).
      why: >
        All in-motion entries carry direction (up|down), target_delta_magnitude
        > 0, and valid axis slugs. All held entries carry axis + rationale.
        s02 has axes_in_motion: [] and three axes_held[] entries — schema
        minimum satisfied. No schema violation found.
      criteria: null

    # -------------------------------------------------------------------------
    # CHECK 3 — STAKES_AXIS VALIDITY
    # -------------------------------------------------------------------------

    - id: fault-003
      type: pass
      what: >
        stakes_axis field for each scene checked against the union of that
        scene's axes_in_motion[] and axes_held[].
      why: >
        All four scenes pass.
        s01: stakes_axis=social_tether-prot-rise → in axes_in_motion[]. PASS.
        s02: stakes_axis=relational_anchor_status → in axes_held[]. PASS.
        s03: stakes_axis=position-prot-rise → in axes_in_motion[]. PASS.
        s04: stakes_axis=moral_legibility_to_self → in axes_held[]. PASS.
      criteria: null

    # -------------------------------------------------------------------------
    # CHECK 4 — NO RANK CLAIM WITHOUT DESCRIBED CAUSE
    # -------------------------------------------------------------------------

    - id: fault-004
      type: pass
      what: >
        Each axis-move's notes field checked against described causal events
        in the scene chunk text.
      why: >
        All six axis-move notes name a described cause present in the
        corresponding chunk. Specific verifications:
        s01 capability +0.5: "first-ward-cluster-added" event in chunk.
        s01 social_tether-prot-rise +0.5: coverage-gap confirmation + Wren
          free-movement mechanism explicit in chunk.
        s03 relational_anchor_status +1.0: lane-refusal enacted in chunk;
          [mechanism: cl-d06-settlement-via-cl-d08-refusal-act] present;
          "relational-anchor-weight-settles" event explicit.
        s03 position-prot-rise +1.0: refusal written and routed to Jarvis in
          chunk; named gap confirmed in channel record; "hook-0014 third
          instance" description consistent with chunk's "she does not write why."
        s04 capability +0.5: "second-ward-cluster-added" event in chunk;
          full-deployment threshold crossed explicit.
        s04 moral_framework -1.0: "khepri-word-surfaces-in-accounting" event
          in chunk; "khepri-suppression-act" mechanism; breach column entry
          explicit; suppression is the ledger entry per chunk.
        No bare assertion found.
      criteria: null

    # -------------------------------------------------------------------------
    # CHECK 5 — COST-LEDGER CONSISTENCY
    # -------------------------------------------------------------------------

    - id: fault-005
      type: pass
      what: >
        Cost-ledger anchor IDs used in b01c12-draft.md checked against
        memory.md cost_ledger[].id list: cl02, cl05, cl-d06, cl-d08, cl-d08b.
      why: >
        All five IDs are present in memory.md cost_ledger. Definitions are
        consistent with the gain-axis assignments:
          cl05: gain capability +2, cost moral_framework -1. Used for
            s01/s04 capability gains and s04 moral_framework cost. Consistent.
          cl-d08b: gain social_tether-prot-rise +1. Used for s01
            social_tether-prot-rise +0.5 (partial draw). Consistent.
          cl02: gain position-prot-rise +4. Used for s03 position-prot-rise
            +1.0. Consistent (partial draw of cl02's +4 total).
          [cl-d08, cl-d06] dual-anchor for s03 relational_anchor_status:
            DEC-0071 settlement note is present in s03 axes_in_motion[].notes;
            cl-d06 2nd-tranche close is recorded; pl-2026-05-30-001 and
            pl-2026-06-02-stitch-thread-002 closure is recorded. Consistent.
        No invalid anchor ID. No anchor used on a mismatched axis.
      criteria: null

    # -------------------------------------------------------------------------
    # CHECK 6 — THEMATIC-AXIS-UNDECLARED
    # -------------------------------------------------------------------------

    - id: fault-006
      type: pass
      what: >
        Chapter goal specifies moral turn (Khepri-suppression / choosing Wren's
        safety). Checked whether moral_framework and moral_legibility_to_self
        appear in axes_in_motion[] or axes_held[] somewhere in the four scenes.
      why: >
        moral_framework: declared in s04 axes_in_motion[] (direction:down,
        magnitude 1.0). PRESENT.
        moral_legibility_to_self: declared in s04 axes_held[] with rationale
        "The Khepri-word surfaces and is suppressed... the suppression is what
        keeps the axis from moving... load-bearing held-discipline stakes axis
        for this scene." PRESENT.
        THEMATIC-AXIS-UNDECLARED does not fire.
      criteria: null

    # -------------------------------------------------------------------------
    # CHECK 7 — SOCIAL_TETHER-PROT-RISE PEAK TENSION (KNOWN TENSION)
    # -------------------------------------------------------------------------

    - id: fault-007
      type: flag
      what: >
        Close-of-c11 aggregate rank for social_tether-prot-rise = 8 (per
        aggregate-state.md). Series substance declares end_rank: 8 and "peaks
        ~8 at d07." The s01 +0.5 (cl-d08b) takes the running rank to 8.5,
        which exceeds the declared series ceiling of 8 and the book-level
        target_delta_magnitude (7; 1→8, already achieved at c11).
      why: >
        The series substance end_rank is a ceiling contract, not an approximate
        target. The chapter takes the axis 0.5 past that ceiling. This creates
        a contract inconsistency: the series says the axis tops at 8; the c12
        contract produces 8.5.

        Mitigating factors (basis for SOFT/flag rather than fault):
        (1) cl-d08b was authored at the series-level substance phase with
            gain: "social_tether-prot-rise +1" — the ledger anticipated this
            draw and the series audit accepted the contract with cl-d08b in
            it (Phase 5 attempt 2 ACCEPT, auditor flag-001 non-blocking).
        (2) The series trajectory note uses "~8 at d07" — approximation
            language that implies a tolerance band.
        (3) The chapter-level book contract notes cl-d08b as a downstream
            watch-item: "cl-d08b social_tether-prot-rise +1 at d08
            inferentially-anchored (auditor flag-001); /and-substance book
            Phase 3 may challenge." That challenge was not raised at the
            book-level audit (b01-audit.md records 3 attempts, all 12 axes
            within ±1 tolerance).
        (4) Downstream c13–c15 all hold social_tether-prot-rise, so the 8.5
            vs 8 difference does not cascade into further overrun.

        Ruling: SOFT — within-tolerance adjudication of a series-approved
        inferential anchor. The 0.5 overrun past end_rank is a known tension
        pre-adjudicated by the series audit; it does not require a fix at this
        scope. Carrying forward for /and-substance book reconciliation if a
        strict-ceiling enforcement pass is run before close.
      criteria: null

    # -------------------------------------------------------------------------
    # CHECK 8 — HELD-ON-IN-MOTION SCHEMA AMBIGUITY
    # -------------------------------------------------------------------------

    - id: fault-008
      type: pass
      what: >
        Each scene checked for any axis appearing in both axes_in_motion[] and
        axes_held[] in the same scene (the pl-2026-05-25-018 ambiguity class).
      why: >
        No overlap found in any scene. s01: capability and social_tether-prot-
        rise in motion; relational_anchor_status and political_register-prot
        held — no overlap. s02: nothing in motion; three held — no overlap.
        s03: relational_anchor_status and position-prot-rise in motion;
        political_register-prot, social_tether-antag, moral_legibility_to_self
        held — no overlap. s04: capability and moral_framework in motion;
        moral_legibility_to_self, political_register-prot, social_tether-antag
        held — no overlap.
      criteria: null

    # -------------------------------------------------------------------------
    # RANK ARITHMETIC CROSS-CHECK (supplemental; not a required check axis)
    # -------------------------------------------------------------------------

    - id: fault-009
      type: pass
      what: >
        Rank arithmetic for all five moving axes cross-checked against
        aggregate-state.md close-of-c11 values.
      why: >
        moral_framework: aggregate rank -1; chapter delta -1.0; result -2.
          s04 note states "Takes moral_framework -1 → -2." MATCH.
        capability: aggregate rank 5.5; chapter delta +1.0; result 6.5.
          s04 note states "Takes capability 5.5 + 1.0 → 6.5 across the
          chapter." MATCH.
        relational_anchor_status: aggregate rank 3.5; chapter delta +1.0;
          result 4.5. s03 note states "Takes relational_anchor_status 3.5 →
          4.5." MATCH.
        social_tether-prot-rise: aggregate rank 8; chapter delta +0.5; result
          8.5. s01 note states "Takes social_tether-prot-rise from 8 to 8.5."
          ARITHMETIC CORRECT (ceiling tension classified separately as
          fault-007 flag).
        position-prot-rise: aggregate rank 4; chapter delta +1.0; result 5.
          s03 note states "Takes position-prot-rise 4 → 5." MATCH.
      criteria: null

    # -------------------------------------------------------------------------
    # AXIS SLUG VALIDITY
    # -------------------------------------------------------------------------

    - id: fault-010
      type: pass
      what: >
        All axis slugs used in b01c12-draft.md checked against the canonical
        list of series.substance.state_axes[].slug values in memory.md.
      why: >
        Slugs used: moral_framework, capability, relational_anchor_status,
        social_tether-prot-rise, position-prot-rise, political_register-prot,
        social_tether-antag, moral_legibility_to_self. All eight are present
        in the series state_axes list with exact slug matches. No invalid or
        misnamed axis slug found.
      criteria: null

  # ---------------------------------------------------------------------------
  # AGGREGATE VERDICT
  # ---------------------------------------------------------------------------

  verdict: PASS
  hard_findings: none
  flag_count: 1
  soft_count: 1
  notes: >
    All eight checks complete. No HARD findings. No faults. One FLAG (fault-007:
    social_tether-prot-rise 8 → 8.5 at c12, 0.5 past series end_rank ceiling;
    classified SOFT per prior series-audit adjudication of cl-d08b; does not
    block). THEMATIC-AXIS check passed (both moral_framework and
    moral_legibility_to_self declared). DEC-0071 settlement note verified
    present with parking-lot closures recorded. Roll-up exact on all five
    axes. Axis slugs valid. Stakes_axis membership verified all four scenes.
    Contract is ready to proceed.
