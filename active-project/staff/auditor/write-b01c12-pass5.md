audit:
  scope: chapter
  target: b01c12
  timestamp: 2026-06-03
  pass: write-b01c12-pass5
  verdict: CONTINUITY-OK-WITH-FLAGS
  # No FAULT findings. Two FLAGS on handoff_out documentation errors. Goal and handoff_out
  # substance are delivered by the bones. No FAULT-REACHABILITY, FAULT-STATE, FAULT-REFERENCE,
  # FAULT-POV, or FAULT-HANDOFF-IN-MISMATCH on any bone.

  findings:

    - id: fault-001
      type: pass
      what: "FAULT-REACHABILITY — goal delivery check"
      why: |
        Goal: "Show the audience the gap, the choice, and the suppression — Taylor choosing
        Wren's safety over the deliverable without naming what she is doing — and the Khepri
        word surfacing and being pushed back down."
        Verification:
          Gap shown: b01c12s01n03-n08 (gate-tower/rendering-yard boundary formally bounded;
            stylus lifts at n08 without writing the source-field). PRESENT.
          Choice/refusal made: b01c12s03n01-n07 (stylus taken → gap-column opened → boundary
            entry written → hand holds → stylus lifts → response entry closes → Jarvis takes
            packet). PRESENT. The refusal is enacted as a physical stopping-before-writing
            sequence (n04 hand holds; n05 stylus lifts from explanation field; n06 response
            closes without explanation clause).
          Khepri-suppression: b01c12s04n06-n11 (accounting reaches aggregate-shape entry →
            harm-prevention column → breach column → shape-word surfaces at n09 for one count
            → accounting advances the count at n10 → architecture entry closes at n11 without
            the word). PRESENT.
        Handoff_out claims verified against bones:
          - coverage gap confirmed in deliverable: s01 + s02 + s03 execute this fully. ✓
          - Khepri threshold named-internally-and-closed: s04n09 (shape-word surfaces) + n10-n11
            (suppression enacted). ✓
          - capability full-deployment: s04n02 (muddy-way fills) + n14 (fifth-ward circuit closes)
            + n12 (ledger takes full-circuit count). ✓
          - Wren anchor 4.5 structurally-necessary: relational_anchor +1.0 at s03n10-n11
            (takes 3.5 → 4.5); the mechanism (lane-refusal IS the mechanism for Wren's route
            becoming load-bearing eastern boundary) is visible in s03n08 (gap-column closes)
            and s03n07 (Jarvis takes the sealed packet without press). ✓
          - moral_framework -2: s04n13 "the breach column takes the threshold entry" (moving,
            moral_framework -1.0, cl05 cost side). Entering rank -1 → exits -2. ✓
        VERDICT: goal fully delivered; handoff_out substance claims verified in bones. PASS.

    - id: fault-002
      type: pass
      what: "FAULT-STATE — prop/location/time consistency check"
      why: |
        Props: stylus used across s01, s02, s03 (n08 "lifts the stylus"; s02n06 "sets the
          stylus"; s03n01 "takes the stylus"; s03n05 "the stylus lifts"; s03n12 "lifts the
          hand"). No stylus appears after deletion or before introduction. Ledger, packet,
          wax seal, covering-sheet — all introduced and then operated on in sequence. No
          prop used out of order.
        Actors in one place: taylor-hebert-kl-122ac is the sole POV subject throughout.
          jarvis-coin-kl-courier appears twice: s02n01 (delivers packet) and s03n07 (takes
          sealed packet). Both appearances are at the standard exchange location (the feed-
          station / standard channel point per world_state). No location contradiction.
        Time progression: s01 morning circuit (east-water-gate lanes mapping + first ward-
          cluster addition at n09-n10); s02 standard-hour packet delivery (jarvis arrives);
          s03 response writing and routing (same day, mid-morning to midday, same location
          as s02); s04 late-afternoon second ward-cluster (muddy-way extension). Progression:
          morning → standard hour → response → late afternoon. Coherent.
        VERDICT: PASS.

    - id: fault-003
      type: pass
      what: "FAULT-REFERENCE — slug resolution check"
      why: |
        jarvis-coin-kl-courier: active cast; last_appearance b01c11 per aggregate-state;
          appears in c12 at s02n01 and s03n07. Valid forward appearance.
        wren-stitch-maker-flea-bottom-ward: referenced as route/pattern (s01n06 "stitch-house
          route"; s01n07 "stitch-maker route"; s02n03 covering-sheet opened without her name
          entering the request) — consistent with indexed-but-unwritten state. Not a scene
          partner on-page, only her route as an operational fact. No state violation.
        otto-hightower-offstage: present only as apparatus and request, never on-page.
          Consistent with cipher status. Valid.
        East-water-gate lanes (s01n01-n08), gate-tower (s01n03-n04), rendering-yard (s01n05),
          muddy-way (s04n01, n02, n14): all within cond-kl-geography-122ac and consistent
          with the c12 chunk geography. "Fifth-ward circuit" at s04n14 consistent with c12
          chunk's "all five wards and the Flea Bottom approaches mapped and simultaneous."
        No un-introduced named entity found in any bone SVO.
        VERDICT: PASS.

    - id: fault-004
      type: pass
      what: "FAULT-POV — perception-verb leak check"
      why: |
        POV narrator: taylor-hebert-kl-122ac. Tight-third/interior chapter. Bone SVO
        subjects audited across all 42 bones:
          Physical-act subjects: taylor-hebert-kl-122ac, jarvis-coin-kl-courier (on-page
            actor), the insects, the ledger column, the coverage map, the map, the feed,
            the accounting, the breach column, the muddy-way entry, the count, the ledger
            entry, the response entry, the coverage-entry, the anchor-column entry.
          None of the above are perception-verb forms (sees/hears/notices/smells/feels/
            perceives) with Taylor as the perceiver subject.
          s04n09: "the accounting reaches the shape-word" — established ledger-idiom per
            the project (b01-c02 canonical form: "the accounting reaches the ward-junction
            entry"). Not a perception-verb; interiority is carried in the "accounting"
            idiom which represents physical ledger-action in the project's fiction-physics.
            The shape-word's arrival is enacted via the accounting (the established physical
            process), not via Taylor noticing or perceiving. CLEAN under project idiom.
        VERDICT: PASS.

    - id: fault-005
      type: pass
      what: "FAULT-HANDOFF-IN-MISMATCH — opening bones vs aggregate close-of-c11"
      why: |
        Aggregate close-of-c11 (authoritative source):
          social_tether-prot-rise: 8, capability: 5.5, relational_anchor: 3.5,
          position-prot-rise: 4, moral_framework: -1.
        Opening bones alignment:
          s01 opens with capability +0.5 (target 5.5 incoming ✓ — n09 moves capability
            from 5.5 → 6.0); social_tether-prot-rise +0.5 (n10 moves from 8 → 8.5); all
            other axes held at aggregate values.
          relational_anchor held at 3.5 through s01/s02 (rationale: choice has not yet
            arrived; axis held until s03). Aggregate 3.5 ✓.
          position-prot-rise held at 4 through s01/s02 (s02n04 rationale: "held at 4").
            Aggregate 4 ✓.
          moral_framework held at -1 through s01-s03, moves -1.0 at s04n13. Aggregate -1 ✓.
        Open threads honored:
          "social tether at near-peak": s01 moves 8 → 8.5. ✓
          "withholding-from-Otto pattern: two withheld": s02-s03 delivers the third
            withhold (the lane-coverage refusal) as the chapter's central mechanism. ✓
          "Wren: anchor rank 3.5; in coverage; daily pattern surveilled": s01n06-n07
            reconfirm Wren's stitch-house route as the gap's operative eastern boundary
            at 3.5 before the axis moves. ✓
          "cf-rhaenyra/Dragonstone-aware": this open thread is not expected to pay in
            c12 (c12 chunk and goal do not include the Dragonstone signal; hook-0012
            remains open-dormant). No contradiction.
        VERDICT: PASS. No genuine thread or world contradiction found.

    - id: flag-001
      type: flag
      what: |
        handoff_out character_state: "Taylor: ... social_tether-prot-rise rank 5.5"
        Source: memory.md chapters[b01c12].handoff_out.character_state (line ~7914).
      why: |
        The aggregate close-of-c11 value is 8 (confirmed in aggregate-state.md axis_state
        social_tether-prot-rise rank 8, last_movement_at b01c11). b01c12 bones deliver
        +0.5 at b01c12s01n10 (cl-d08b), taking the axis from 8 → 8.5. The bones are
        correct. The handoff_out character_state string "5.5" is a stale book-author
        lineage value (the handoff_conflicts block at b01c12 records the stale incoming
        prediction of 5 and resolves aggregate-wins at 8, but the outgoing value was
        not updated). The actual close-of-c12 value is 8.5.
        b01c13 Phase 0 will read this handoff_out and may anchor its calculations at 5.5
        rather than 8.5, creating a handoff_conflict that could be misread as a genuine
        state discrepancy rather than a known documentation error.
        This is a documentation fault in handoff_out only — not a bones execution error.
        The bones deliver correctly.

    - id: flag-002
      type: flag
      what: |
        handoff_out character_state: "Taylor: capability rank 6"
        Source: memory.md chapters[b01c12].handoff_out.character_state (line ~7914).
      why: |
        Aggregate close-of-c11: capability 5.5 (per aggregate-state.md, ESTIMATE-DIVERGENCE
        noted, measured-authoritative 5.5). b01c12 bones deliver capability +1.0 total
        (+0.5 at b01c12s01n09, cl05 gain; +0.5 at b01c12s04n02, cl05 gain second tranche).
        Close-of-c12 capability = 5.5 + 1.0 = 6.5.
        The handoff_out says "capability rank 6" — this is a documentation error, not a
        bones error. The bones execute +1.0 exactly (per the chapter roll-up check at the
        top of the bones file: "capability: +0.5 (s01) + 0 (s02) + 0 (s03) + 0.5 (s04) =
        +1.0 ✓"). The substance_delta_measured at chapter close should record 6.5.
        b01c13 Phase 0 reading capability rank 6 instead of 6.5 will need to resolve a
        handoff_conflict on the same pattern as the c11-c12 ESTIMATE-DIVERGENCE.
        Documentation fault in handoff_out only — not a bones execution error.

  # -----------------------------------------------------------------------
  # GOAL DELIVERY CONFIRMATION
  # -----------------------------------------------------------------------
  # Three required goal elements and their bone carriers:
  #   (1) Gap shown: b01c12s01n03-n08 (gate-tower + rendering-yard boundaries closed;
  #       stylus lifts without writing source-field). DELIVERED.
  #   (2) Choice/refusal made: b01c12s03n01-n07 (refusal written, sealed, routed to Jarvis;
  #       hand stops before explanation field; gap-column closes without source clause).
  #       DELIVERED.
  #   (3) Khepri suppression: b01c12s04n09 (shape-word surfaces in accounting) + n10-n11
  #       (accounting advances the count; architecture entry closes without the word).
  #       DELIVERED.
  #
  # HANDOFF_OUT SUBSTANCE (bones-delivered values, correcting documentation):
  #   capability: 6.5 (bones deliver +1.0 on 5.5 aggregate)
  #   social_tether-prot-rise: 8.5 (bones deliver +0.5 on 8 aggregate)
  #   relational_anchor_status: 4.5 (bones deliver +1.0 on 3.5 aggregate; s03n10+n11)
  #   position-prot-rise: 5 (bones deliver +1.0 on 4 aggregate; s03n03+n06)
  #   moral_framework: -2 (bones deliver -1.0 on -1 aggregate; s04n13)
  #   [social_tether-antag: 6, held — no movement this chapter per contract]
  # -----------------------------------------------------------------------
