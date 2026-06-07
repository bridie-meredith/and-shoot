audit:
  scope: chapter
  target: b01c11
  timestamp: 2026-06-02
  source_file: active-project/staff/showrunner/b01c11-draft.md
  checks_run:
    - sum-roll-up
    - no-rank-without-cause
    - thematic-axis-undeclared
    - stakes-axis-union
    - direction-magnitude-wellformed
    - cost-ledger-consistency
    - chunk-tag-protocol
    - held-axis-discipline

  summary: 0 HARD / 2 SOFT / 0 escalate / 6 axes pass-clean

  findings:

    - id: fault-001
      type: flag
      what: >
        s02 axes_in_motion[social_tether-antag +0.5] notes field — "Otto's structural
        leverage advances because what Taylor withholds is becoming more consequential;
        non-extractable confirmation in progress."
      why: >
        The notes assert Otto's leverage gain as a consequence of Taylor's withholding,
        but Otto is not on-page in s02 and no chunk event directly shows Otto receiving
        or being unable to receive the withheld content. The mechanism is inferential:
        Taylor withholds → substrate split deepens → Otto's positional leverage increases
        by proxy. This is structurally correct per the series contract (cl-antag-d10 gain
        is the substrate-split accumulation), but the notes claim the advance as a
        demonstrated consequence rather than an accumulated-across-chapter one. At
        /and-write Phase 6 this annotation pattern can produce a SUBSTANCE-SUSPECT-cheap-gain
        finding if the bone-gate auditor reads the s02 notes as claiming a completed
        lever-advance rather than a tranche of the chapter-level +1.0 accumulation.
        Partial drift: the notes would be tighter if they framed s02's +0.5 as the
        first tranche of the substrate-split accumulation rather than asserting Otto's
        leverage advance as an event.
      criteria: null

    - id: fault-002
      type: flag
      what: >
        position-prot-rise absent from axes_held in all four scenes. The task
        dispatch named it as an expected held axis (alongside relational_anchor_status,
        moral_framework, political_register-prot, moral_legibility_to_self). The draft
        lists six or seven held axes per scene but position-prot-rise and
        position-prot-collapse appear in none.
      why: >
        By c11, position-prot-rise is a rise-phase axis in its non-extractable-confirmed
        state (d10 peak confirmed at c10). Whether it should be held or omitted depends
        on whether the book contract treats it as depleted (no further rise-delta possible)
        or as a maintained held position requiring rationale. If the axis is treated as
        exhausted at its d10 peak and no longer requiring chapter-by-chapter held
        rationale, the omission is correct but unannounced. If it is still active and
        relevant to the c11 scene content (the arrangement-as-cover events in s03 are
        directly position-prot-rise adjacent — cover works because Taylor has that
        position), omitting it from axes_held leaves an uncontracted held position
        at /and-write Phase 6. position-prot-collapse is similarly absent. Neither
        axis appears anywhere in the four-scene contract.
        Downstream risk: /and-write Phase 6 HELD-AXIS-UNCONTRACTED could fire on any
        bone that touches the cover/arrangement (s03, s04) if those bones carry
        position-prot-rise or position-prot-collapse holds.
      criteria: null

    - id: pass-001
      type: pass
      what: >
        Check 1 — Sum roll-up (axes_in_motion only).
      why: >
        social_tether-prot-rise: s01 +0.5 + s04 +0.5 = +1.0 vs chapter target +1.0. EXACT.
        social_tether-antag: s02 +0.5 + s03 +0.5 = +1.0 vs chapter target +1.0. EXACT.
        political_register-world: s02 +0.5 = +0.5 vs chapter target +0.5. EXACT.
        All held axes contribute zero. No ±1 tolerance breach.

    - id: pass-002
      type: pass
      what: >
        Check 2 — No rank claim without described cause (excluding fault-001 flag on s02
        social_tether-antag notes framing).
      why: >
        s01 social_tether-prot-rise +0.5: three chunk events (Jarvis structural exchange,
        Oswyn unknowing junction baseline, ward contacts via prior-service reciprocity)
        directly named and tagged. Grounded.
        s02 political_register-world +0.5: merchant burn event (thermal-and-smoke catch),
        Dragonstone-awareness inference from burn-as-standing-protocol, courier-thread
        confirmation. All tagged and causally described.
        s03 social_tether-antag +0.5: two-withheld-observations-in-succession event and
        substrate-split mechanism both tagged. Grounded.
        s04 social_tether-prot-rise +0.5: all-four-nodes-simultaneously-load-bearing via
        evening count enumeration. Tagged. Grounded.

    - id: pass-003
      type: pass
      what: >
        Check 3 — THEMATIC-AXIS-UNDECLARED.
      why: >
        "Social tether at full load": declared via social_tether-prot-rise (s01, s04
        axes_in_motion) and social_tether-antag (s02, s03 axes_in_motion); the full-load
        reading encompasses both protagonist-tether and antagonist-leverage faces.
        "First Rhaenyra-pressure signal": declared via political_register-world (s02
        axes_in_motion); s02 notes and chunk explicitly name the Dragonstone-awareness
        consequence.
        "Dragonstone-distance irony": covered by political_register-world and the
        [force: taylor-withholds-rhaenyra-signal-from-jarvis] tag in s02. No separate
        axis required; the irony is a narratorial observation riding declared axes.
        No thesis element from the chapter goal is left under-declared.

    - id: pass-004
      type: pass
      what: >
        Check 4 — scene_conflict.stakes_axis union.
      why: >
        s01 stakes_axis social_tether-prot-rise: in axes_in_motion. PASS.
        s02 stakes_axis political_register-world: in axes_in_motion. PASS.
        s03 stakes_axis social_tether-antag: in axes_in_motion. PASS.
        s04 stakes_axis social_tether-prot-rise: in axes_in_motion. PASS.

    - id: pass-005
      type: pass
      what: >
        Check 5 — direction/magnitude well-formedness; no axis in both lists.
      why: >
        All axes_in_motion entries: direction = up, target_delta_magnitude > 0 in all
        four scenes.
        All axes_held entries: rationale present and non-empty in all four scenes.
        Cross-list check: no axis appears in both axes_in_motion and axes_held in any
        single scene. No duplication found.

    - id: pass-006
      type: pass
      what: >
        Check 6 — cost_ledger consistency.
      why: >
        cl03b: gain declared "social_tether-prot-rise +4" (book-level ledger). s01 and
        s04 take +0.5 tranches totaling +1.0 for this chapter. s04 notes correctly
        acknowledge the cl07a future-cost collateral relationship. Tranche model valid.
        cl-antag-d10: gain declared "social_tether-antag +4" (book-level ledger). s02
        and s03 take +0.5 tranches totaling +1.0. The journey-required cl04 dependency
        is acknowledged in s04 axes_held rationale with cross-reference to pl-2026-06-02-002
        (open advisory parking-lot item). No over-draw.
        political_register-world null anchor: s02 carries cost_ledger_anchor: null with
        explicit "world-tick, no series-cost paid" notation. The book-level +4 target
        is anchored at cl-world-d07 + cl07c; the +0.5 tick here is within the trajectory
        narrative fill tolerance (~+2 attributed to cl07c / trajectory-narrative). Acceptable.

    - id: pass-007
      type: pass
      what: >
        Check 7 — chunk-tag protocol.
      why: >
        All four scene chunks carry [event:], [image:], [force:], and [mechanism:] tags
        on every load-bearing span. No obviously load-bearing event or mechanism found
        untagged across the four chunks. Coverage density is high; tag-to-event
        correspondence aligns with content that would become /and-write event_map entries.

    - id: pass-008
      type: pass
      what: >
        Check 8 — Held-axis discipline; parking-lot resolution consistency.
      why: >
        relational_anchor_status held flat all four scenes, rank 3.5. s01 axes_held
        rationale carries the HARD PARKING-LOT RESOLUTION note for pl-2026-06-02-
        stitch-thread-002 (DEC-0071 re-window to b01c12). s04 confirms re-window.
        Consistent with parking-lot resolution_note.
        hook-0007 / Halvard foreclosure: s03 moral_legibility_to_self held-axis
        rationale carries the HARD PARKING-LOT RESOLUTION note for pl-2026-06-02-
        stitch-thread-001 (DEC-0071 foreclose-at-c13). The chunk enacts the thinning
        ([mechanism: halvard-argument-inactive-in-taylors-operational-register-not-refuted])
        without staging a new engagement. Consistent with parking-lot resolution_note.
        All five explicitly named held axes (relational_anchor_status, moral_framework,
        political_register-prot, moral_legibility_to_self, social_tether-antag / 
        social_tether-prot-rise as applicable per scene) carry non-empty rationales.
        political_register-prot rationale in s03 correctly distinguishes Halvard-thinning
        as a legibility-register event, not a contempt-register event.
