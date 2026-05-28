```yaml
audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  pass: write-b01c05-pass5 (second fork — fresh context; supersedes prior file)
  findings:

    # ── REACHABILITY ──────────────────────────────────────────────────────────

    - id: r-001
      type: pass
      what: >
        Chapter goal element 1 — "moment the insect-feed stops being neutral."
        s03n06 (taylor-hebert-kl-122ac stops the rushwick-pass) carries the
        sole axis_move in the bone set: +1.5 political_register-prot at cl-d05.
        The bone notes explicitly state "the cessation IS the recognition event."
        Cessation event is delivered.
      why: null
      criteria: null

    - id: r-002
      type: pass
      what: >
        Chapter goal element 2 — "color arrives before Taylor names it."
        Sequence: s03n05 (the provisioner-train re-crosses the junction in the
        replay — color arrives without a label per axes_held rationale "the color
        arrives in the replay without a label") → s03n06 (stops the pass —
        recognition/cessation bone) → s03n08 (closes the evening review — filing-
        as-texture bone; notes confirm "the closing IS the filing-as-texture
        protagonist_force"). Taylor categorizes without naming the color as
        resentment. Sequence honored.
      why: null
      criteria: null

    - id: r-003
      type: pass
      what: >
        Chapter goal element 3 — "plant the courier figure whose face will matter
        at d10." s02n02: gait-signature recognition (third sighting, heel-first).
        s02n11: cf-d10-courier-face thread initiated (notes: "recurring body,
        three observations, enforcement incident attached"). s03n07: courier-face
        surfaces in the rushwick replay. s03n09: cf-d10-courier-face thread
        confirmed open. Goal element delivered.
      why: null
      criteria: null

    - id: r-004
      type: pass
      what: >
        Handoff_out character_state: "Taylor: political_register-prot rank 2.5
        (resentment color present)." Bone set delivers: starting rank per
        handoff_in = 1 (axis not yet active before b01c05; b01c04 handoff_out
        does not list political_register-prot as having moved). s03n06 delivers
        +1.5 at cl-d05. 1 + 1.5 = 2.5. Consistent.
      why: null
      criteria: null

    - id: r-005
      type: pass
      what: >
        Handoff_out world_state: "extended coverage now touching Red Keep
        servant-passage ward." Bones s01n01-n03 establish Taylor entering the
        Rushwick (chapter chunk defines the Rushwick as "a ward that abuts the
        lower Red Keep servant passages") and coverage filling the junction.
        Delivered.
      why: null
      criteria: null

    - id: r-006
      type: pass
      what: >
        Handoff_out world_state: "faction-violence sub-pressure: first on-page
        enforcement incident observed by Taylor." s02n03-n10 deliver the
        enforcement incident (three figures, side-alley, courier pinned, effortful
        sound, courier recovers, figures depart purposive walk). Delivered.
      why: null
      criteria: null

    - id: r-007
      type: pass
      what: >
        Handoff_out open_thread: "cf-d10-courier-face thread: courier body
        observed three times; not yet named; filed as operational texture."
        s02n11 initiates; s03n09 confirms open. s03n09 notes: "courier body-record
        mapped as recurring with enforcement-incident attached." Not named anywhere
        in the bone set. Filed as operational texture in s03n08 (closes the
        evening review) and s03n09. Delivered.
      why: null
      criteria: null

    # ── HANDOFF-IN CHECKS ─────────────────────────────────────────────────────

    - id: hi-001
      type: pass
      what: >
        Handoff_in: "Taylor: capability rank 4.5; … moral_framework cracked
        (licensed exception active)." s01n02 axes_held capability rationale:
        "coverage extension to Rushwick is continuation of four-ward map
        established in c04; not a new expansion event; the range is confirmed
        active." s01n06 axes_held moral_framework rationale: "categorizing
        court-logistics bodies as intelligence substrate is already inside the
        licensed exception; d04 rationalization runs unchanged." Neither bone
        reads the starting state as fresh or uncracked. Handoff-in honored.
      why: null
      criteria: null

    - id: hi-002
      type: pass
      what: >
        Handoff_in: "Wren: in expanded coverage map; anchor rank 2." Wren is
        absent from the chapter. s01n09 axes_held relational_anchor_status:
        "no relational content in this ward; Wren not present; anchor not
        activated." s02n11 and s03n09 both hold relational_anchor_status with
        rationale "courier not a relational anchor." Anchor held at rank 2;
        not activated or altered. Handoff-in honored.
      why: null
      criteria: null

    - id: hi-003
      type: pass
      what: >
        Handoff_in: "Flea Bottom intelligence layer: routing to Otto through
        Jarvis." Jarvis routing active in s02n09 (taylor delivers the enforcement
        report-entry to Jarvis as offstage destination). No bone claims Jarvis
        is physically present on set. The SVO "taylor-hebert-kl-122ac delivers
        the enforcement report-entry" does not name Jarvis as subject. Handoff-in
        honored.
      why: null
      criteria: null

    # ── STATE / REFERENCE CHECKS ──────────────────────────────────────────────

    - id: sr-001
      type: fault
      what: >
        active-project/actors/taylor-hebert-kl-122ac/state.md records:
        political_register_prot_axis: 1. Bone b01c05s03n06 delivers axis_moves:
        [{axis: political_register-prot, direction: up, magnitude: 1.5,
        cost_ledger_anchor: cl-d05}]. The chapter handoff_out (memory.md line
        3454) records Taylor's political_register-prot rank as 2.5 after this
        chapter. The actor state file has not been updated to reflect the +1.5
        move delivered in this chapter.
        Additionally, the state file shows moral_framework_axis: 2 and
        capability_axis: 2 against b01c04 handoff_out character_state of
        "moral_framework rank 1 (cracked)" and "capability rank 4.5." These
        axis values appear to be the series-open initialization values, never
        updated across any delivered chapter.
      why: >
        The memory rules are absolute: "nothing changes without being recorded."
        If b01c06 authoring reads the state file and finds political_register_prot_axis: 1,
        capability_axis: 2, and moral_framework_axis: 2, it will author against
        the wrong baseline for all three axes. The handoff_out records the correct
        post-c05 values but the actor state file — the per-session-open source
        of truth — is stale since series open.
      criteria: >
        Actor state file must record axis values consistent with the b01c05
        handoff_out before Phase 6 proceeds. Minimum: political_register_prot_axis
        updated to 2.5 (post-c05 delivered value). Full reconciliation against
        all delivered chapter handoff_out values across b01c01-b01c05 is the
        correct resolution given the systemic staleness.

    - id: sr-002
      type: pass
      what: >
        Rushwick internal geography — "east-lane" (s01n05) and "east exit"
        (s02n03 notes, "side-alley off the east exit"). The bones do not
        establish whether these are the same feature under different noun-forms
        or two adjacent elements. However: s01n05 places the provisioner-train
        exiting the junction into the east-lane (a direction/lane), while s02n03
        places the three figures entering a side-alley off the east exit (an
        alley off an exit-mouth). These can be read as two distinct features
        (lane vs. side-alley) on the east side of the junction without spatial
        contradiction. No internal inconsistency within the bones themselves; both
        uses are stable to their own context. No bones fault.
      why: null
      criteria: null

    - id: sr-003
      type: pass
      what: >
        All noun-form references consistent within the bone set: the courier
        (s02n01 through s03n13), the three figures (s02n03-s02n10), the
        provisioner-train (s01n04-s01n05, s03n05, s03n11), the message-runner
        (s01n07-s01n08), the room-floor (s03n01 only). No actor appears in a
        location they have not been moved to. No prop is referenced from inventory
        Taylor does not carry (Taylor's inventory in state file is empty; no
        inventory prop is called upon in any bone). No reference fault.
      why: null
      criteria: null

    - id: sr-004
      type: pass
      what: >
        oc-rushwick.card.md — no card exists (pre-existing Phase 2 signal-003).
        Within the bones, no claim requires card-level authority (no specific
        distances asserted, no fixed named proprietors, no features that would
        require canonical card validation). The bones establish the Rushwick
        as a ward through internally consistent geography noun-forms. No new
        bones-level fault generated by the card's absence.
      why: null
      criteria: null

    # ── POV CHECKS ────────────────────────────────────────────────────────────

    - id: pov-001
      type: pass
      what: >
        All 34 bones examined for perception-verb leaks and first-person pronouns.
        SVO subjects across all bones are physical observables or the physical
        actor slug. Phase 2 recasts (s01n05, s01n08, s02n01, s02n04, s02n07,
        s03n05, s03n06, s03n08, s03n11, s03n13) all carry notes confirming the
        recast. No perception-verb subject on any Taylor SVO. No first-person
        leak. POV constraint honored across all 34 bones.
      why: null
      criteria: null

    # ── TIME / SEQUENCE CHECKS ────────────────────────────────────────────────

    - id: ts-001
      type: pass
      what: >
        s01: "second morning after the Roper's Court report" — b01c04 handoff_out
        world_state confirms "Green faction receives first street-layer intel"
        (the Roper's Court report delivery). s01 opening on the second morning
        is consistent with c04 closing on the report-handoff.
        s02: "five days into the Rushwick coverage" (s02n02 rationale). Day-count
        from s01 (day 1) to s02 (day 5) allows three separate sightings of the
        courier across the coverage window. Internally consistent.
        s03: "that evening" (same day as s02). s03n01 grounds Taylor at the
        room-floor for the evening review, consistent with returning from field
        work. Sequence intact. No time fault.
      why: null
      criteria: null

    # ── DUPLICATE SVO ADVISORY ────────────────────────────────────────────────

    - id: dup-001
      type: flag
      what: >
        Bones b01c05s03n10 and b01c05s03n12 carry identical SVOs:
        "taylor-hebert-kl-122ac runs the rushwick flat-read." The duplication
        is intentional by design (notes on s03n12: "try-flat-read sequence re-run
        bone 3: Taylor runs the pass again — second attempt; the repeat is
        load-bearing for the foreclosure-as-enacted-capability-failure"). The
        event_map entry "Taylor runs the pass again — same result (foreclosure
        enacted)" sources both bones.
      why: >
        Identical SVOs in distinct bones are not a bones fault when the substance
        rationale distinguishes them — and it does here (n10 = first attempt,
        n12 = second attempt; n11 and n13 provide the counterpart held-bones
        showing failure). However, a renderer reading only the SVO list without
        the notes may produce duplicate surface prose. The prose obligation at
        /and-stitch is to render n10 and n12 as distinguishable attempts, not
        as a flat repetition of the same sentence. This is a renderer advisory,
        not a bones block.
      criteria: null

    # ── WORM-CANON SOFT-WATCH COMPLIANCE ─────────────────────────────────────

    - id: sw-001
      type: pass
      what: >
        Parking-lot SOFT-WATCH (carried from chunk review): "worm-canon-pedant —
        courier gait-signature + approach-geometry read + filing must be
        structurally distinct bones in s02 + s03, not collapsed to single logging
        assertion."
        s02n02 (gait-signature recognition, notes "SOFT-WATCH bone 1 of 3"),
        s02n04 (approach-geometry read, notes "SOFT-WATCH bone 2 of 3"),
        s02n08 (filing / approach-geometry to Jarvis format, notes "SOFT-WATCH
        bone 3 of 3") are structurally distinct bones with distinct SVOs and
        distinct substance rationales. Soft-watch obligation satisfied.
      why: null
      criteria: null

    # ── PLAN QUALITY ──────────────────────────────────────────────────────────

    - id: pq-001
      type: pass
      what: >
        Phase 5 attempt log (memory.md lines 3459-3464): attempt 1 produced
        REVISE (dark-fantasy-reader REVISE, auditor 1 HARD + 1 SIGNAL + 3 FLAGS);
        attempt 2 produced ACCEPT across all reviewers (dramatist ACCEPT att 1;
        cape-fic ACCEPT att 1; worm-canon ACCEPT att 1; dark-fantasy REVISE →
        ACCEPT att 2; auditor 0-HARD att 2). Review cycle properly converged on
        acceptance without attempt exhaustion. No plan quality escalation.
      why: null
      criteria: null

  verdict: FINDINGS-PRESENT
  verdict_classification: >
    1 HARD fault (sr-001 — actor state file stale since series open; must be
    updated before Phase 6 substance bone-gate proceeds).
    1 non-blocking FLAG (dup-001 — duplicate SVO on s03n10/n12; renderer advisory
    for /and-stitch).
    All reachability checks, handoff-in checks, POV checks, time/sequence checks,
    and reference checks pass.
    Clear to Phase 6 once sr-001 is resolved.
```
