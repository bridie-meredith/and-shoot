```yaml
audit:
  scope: chapter
  target: b01c20
  timestamp: 2026-06-05
  pass: 2
  label: "constraint + SVO-form audit — /and-write Phase 2"
  findings:

    # ── FAULTS ────────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      bone: b01c20s01n02
      svo: "the wrong doors open"
      what: >
        "wrong" is an adjective modifying "doors." The schema bans adjectives
        in bone SVOs (FAULT-FORM-MODIFIER). The modifier is characterization
        (these are not the expected doors) rather than an observable physical
        property of the subject.
      why: >
        An adjective-modified subject smuggles a narrator interpretation into
        the SVO layer. The physical event (doors open) is distinct from the
        evaluative framing (they are wrong-doors). Facets carry that
        interpretation; the bone records only the event. The modifier also
        contributes to the chatter-anchor fault (fault-003) by making the bone
        harder to recast as a valid held bone.
      criteria: >
        The bone SVO must not contain any adjective modifier on the subject or
        object. The physical event (doors opening in a specific sequence Taylor
        can read as anomalous) must be preserved. Suggested minimum-change
        recast: "the doors open" — the anomaly lives in context and the
        cost-ledger_anchor resolution (see fault-003). If the drafters wish to
        preserve more specificity without modifiers, a transitive approach is
        available: "the wrong-sequence doors open" is still a modifier compound;
        prefer the bare "the doors open" and let facets carry the anomaly reading.

    - id: fault-002
      type: fault
      bone: b01c20s02n02
      svo: "the wrong men enter the ward junctions"
      what: >
        "wrong" is an adjective modifying "men." Same class as fault-001:
        FAULT-FORM-MODIFIER. The physical event (men enter the ward junctions)
        is observable; "wrong" is narrator characterization, not an observable
        physical property of the subject.
      why: >
        Adjective modifiers on subjects in moving bones embed interpretation
        at the physical-event layer. This bone carries a magnitude-2 draw on
        the chapter's dominant axis (social_tether-prot-collapse); if the
        bone is malformed its axis-movement is in jeopardy at Phase 6
        bone-gate re-check. Removing the modifier does not reduce the event's
        coverage — the ward junctions are the specific named geography, and
        the violence-entering event is preserved bare.
      criteria: >
        The bone SVO must not contain an adjective modifier. "The men enter
        the ward junctions" is the minimum-change recast; it preserves the
        subject, verb, and named-object geography without the characterization
        modifier. Event-map coverage of "wrong men moving fast through right
        intersections" is carried by scene context and facets, not the bone's
        SVO modifier.

    - id: fault-003
      type: fault
      bone: b01c20s01n02
      svo: "the wrong doors open"
      what: >
        Chatter bone (axis_moves: [], axes_held: []) with no cost_ledger_anchor.
        The schema rule: "a chatter bone (axis_moves:[] + no axes_held) without
        cost_ledger_anchor" = FAULT-BONE-DELTA-MALFORMED (CHATTER-UNPAID).
        The screen-writer's defense — that this bone is a grounding subordinate
        to n01's position-world draw — is insufficient: a grounding bone that
        is ALSO a chatter bone still requires either (a) axes_held with rationale
        or (b) a cost_ledger_anchor paying a later gain. Neither is present.
        The draft comment acknowledges this: "strictly, no cost_ledger_anchor
        here" and attempts to defer payment to n01's already-settled draw.
        That is not a valid anchor; n01's cl07b is settled by n01, not
        deferred to n02.
      why: >
        Chatter-unpaid bones are not load-bearing in the substance contract.
        If the bone proceeds with neither axes_held nor a cost_ledger_anchor,
        the bone-gate will HARD-fault it at Phase 6. The physical event
        (specific door-sequence reading as anomalous) is narratively
        load-bearing for event-coverage of viserys-death-in-feed; it cannot
        be absent, but it cannot be unpaid chatter in its current shape.
      criteria: >
        One of the following must be true:
        (a) Add axes_held with a rationale that witnesses the held discipline
        (e.g., moral_framework or capability held at this bone), converting
        the bone from chatter to held-discipline; or
        (b) Add a cost_ledger_anchor (cl07b or cl07a) paying forward to a
        later gain in this scene, with the bone explicitly acknowledged as
        an unpaid-grounding-subordinate to n04's or another paying bone's
        move. The cost_ledger_anchor must be valid (cl07a / cl07b / cl07c)
        and the paying gain must be identified. Note: after fault-001 recast
        removes "wrong," the bare "the doors open" may still justify a held
        bone with capability or moral_framework rationale.

    - id: fault-004
      type: fault
      bone: b01c20s02n01
      svo: "the succession bell rings"
      what: >
        Chatter bone (axis_moves: [], axes_held: []) with no cost_ledger_anchor.
        The draft comment acknowledges it is a "Chatter bone with
        cost_ledger_anchor: the bell is..." — but the actual YAML has no
        cost_ledger_anchor field (it is absent from the substance_delta block).
        This is FAULT-BONE-DELTA-MALFORMED (CHATTER-UNPAID) by the same rule
        as fault-003.
      why: >
        Same consequence as fault-003: the bone will HARD-fault at Phase 6
        bone-gate if it reaches Phase 6 with no axes_held and no
        cost_ledger_anchor. The comment description "Chatter bone with
        cost_ledger_anchor" is aspirational, not authored into the schema
        field. The bell-rings bone is grounding for the scene's opening
        event; it must be paid.
      criteria: >
        One of the following must be true:
        (a) Add axes_held with rationale (e.g., social_tether-antag held at
        rank 9 — the bell is the structural apparatus executing at its locked
        rank; or political_register-prot held — the contempt-without-refusal
        register that Taylor witnesses the announcement through); or
        (b) Add a cost_ledger_anchor (cl07a, cl07b, or cl07c) for a forward
        gain this bone is purchasing. Given the scene's axes, cl07a (paying
        toward social_tether-prot-collapse draws or moral_legibility draws)
        or cl07b (paying toward position-prot-collapse draws) are candidates.
        The screen-writer's comment ("grounding value is load-bearing for
        EVENT-NOT-CONCRETE") suggests axes_held is the correct resolution,
        converting this to a held-discipline bone.

    - id: fault-005
      type: fault
      bone: b01c20s02n06
      svo: "the passage-counts fill the violence"
      what: >
        FAULT-FORM-INTERIORITY. The object "the violence" is an abstract noun.
        Per schema: "Abstraction-as-object is INTERIORITY. A physical verb whose
        object is an abstract noun faults FAULT-FORM-INTERIORITY." The subject
        (the passage-counts) and verb (fill) are physically grounded, but "the
        violence" is not a nameable physical object — it is an abstraction
        standing in for "the spaces/routes where violence moves." A physical
        verb with an abstract object is a thought-figure, not an observable event.
      why: >
        This bone carries a position-prot-collapse axis move (magnitude 1,
        cl07b) and axes_held for two locked axes. If the SVO is incoherent
        (abstract object), the bone cannot pass Phase 6 bone-gate's
        EVENT-NOT-CONCRETE check. The event being covered (passage-counts are
        the entry points the violence uses) is narratively load-bearing;
        it cannot be absent from event-coverage. The incoherence is in the
        object, not the subject-verb pair.
      criteria: >
        The object must be a named physical entity, not an abstraction.
        The event is: the passage-count data Taylor entered into Jarvis
        reports is now the operational geometry the violence moves through.
        Minimum-change recasts that preserve SVO discipline:
        — "the passage-counts orient the faction-movement" (faction-movement
          is still somewhat abstract; weaker)
        — "the faction-movement follows the passage-counts" (subject/object
          swap; cleaner; faction-movement as named event-class)
        — "the violence-flow traces the passage-count entries" (violence-flow
          as compound noun naming the physical phenomenon)
        The fixer should prefer the recast where the verb is transitive and
        the object is the most physical possible referent for the
        violence-infrastructure link. Event-map coverage of
        routes-become-roadmap must be preserved.

    - id: fault-006
      type: fault
      bone: b01c20s05n03
      svo: "the architecture returns to substrate"
      what: >
        FAULT-FORM-MODIFIER. "to substrate" is a prepositional phrase of
        destination. Per schema: "Prepositional phrases of place / destination /
        source / direction / instrument / accompaniment are explicitly banned
        (FAULT-FORM-MODIFIER). Use a transitive verb that takes the location
        as direct object." "Returns to substrate" uses a prepositional
        destination phrase; it does not use a transitive verb taking the
        location as its direct object.
      why: >
        Prepositional padding in destination position is the most common
        FAULT-FORM-MODIFIER shape after adjective modifiers. "Returns to
        substrate" cannot reach the Phase 6 bone-gate in this form.
        This bone carries two axis moves (social_tether-prot-collapse and
        position-world) and is the semantic pivot for the chapter's
        "what disperses is what was hers" image; it cannot be absent.
      criteria: >
        The destination phrase must be eliminated. Options:
        (a) Intransitive recast without destination: "the architecture
        disperses" — clean but may duplicate s05n02's "the insects disperse."
        (b) Transitive recast: "the architecture releases the coverage" —
        subject acts on the named object. Or: "the coverage dissolves" /
        "the architecture releases." The screen-writer's recast offer
        ("the insects drop below surveillance range") also has a prepositional
        phrase ("below surveillance range") — it does not resolve the
        FAULT-FORM-MODIFIER. The correct recast uses either a pure
        intransitive or a transitive verb with a named direct object,
        not a preposition of destination. Suggested: "the architecture
        releases" (pure intransitive; the coverage is released without
        naming the destination) — keeps the pivot without the prepositional
        fault, and s05n02's "the insects disperse" provides the physical
        substrate detail.

    # ── FLAGS ─────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      bone: b01c20s01n01
      svo: "the servant-passages empty"
      what: >
        "Empty" used as an intransitive verb is borderline. The copula reading
        ("the passages ARE empty") is ruled out by the intransitive verb usage
        ("to empty" = to become empty), which is a licensed English verb form
        connoting a physical state-change. The schema bans copulas but does not
        ban intransitive state-change verbs that describe a concrete physical
        transition. However, the bone is acknowledged as grounding, and the
        cleaner-SVO recast ("the last bodies leave the servant-passages") is
        unambiguously transitive and passes without interpretation.
      why: >
        No downstream consequence if this passes as-is; the bone carries
        a legitimate axis move (position-world +1, cl07b) and is not
        chatter. However if Phase 6 auditor takes a strict reading of
        "empty" as copula-adjacent, the bone will fault. The screen-writer's
        offered recast removes all ambiguity at zero event-coverage cost.
      # No criteria field — flag does not block; fixer may apply the offered
      # recast as a zero-cost cleanup if the screen-writer and showrunner accept.

    - id: flag-002
      type: flag
      bone: b01c20s01 (aggregate)
      what: >
        s01 has three moving axes: position-world +0.5, political_register-world
        +0.5, moral_legibility_to_self +0.2 (scene contract). At bone level,
        all three draw magnitude 1 each (n01 position-world +1, n03
        political_register-world +1, n04 moral_legibility_to_self +1).
        The schema requires the dominant axis to get the largest bone aggregate.
        Position-world and political_register-world are tied dominant; moral_
        legibility is the secondary axis. At bone level, all three are equal
        (magnitude 1 each). The dominant axes do not have a larger aggregate
        than the secondary axis.
      why: >
        The minimum bone delta is 1; there is no magnitude 0 available. With
        only one paying bone per axis, equality is forced by the design. This
        is within the established proportional-distribution scheme from c01-c19
        (where minimum-granularity produces proportional imprecision). It does
        not exceed ±1 rank tolerance. Non-blocking; advisory only.

    - id: flag-003
      type: flag
      bone: b01c20s05 (aggregate)
      what: >
        s05 scene contract has moral_legibility_to_self at +0.1 — the smallest
        moving axis in the scene. At bone level, moral_legibility receives
        magnitude 1 (n05, cl07a), which equals position-world's bone total
        (+1, n03 magnitude 1) despite position-world having a larger contract
        target (+0.2 vs +0.1). By strict proportional-distribution, moral_
        legibility should be the smallest bone aggregate; it is tied with
        position-world.
      why: >
        Same minimum-granularity constraint as flag-002. With only one paying
        bone per axis and a minimum magnitude of 1, proportional precision
        below 0.2 is architecturally unachievable. Within ±1 rank tolerance.
        Non-blocking; advisory only.

    # ── SPECIFIC-ITEM RULINGS (screen-writer self-flags) ──────────────────────

    - id: ruling-001
      type: pass
      item: "s01n01 — 'the servant-passages empty' (intransitive verb question)"
      ruling: >
        CORRECT as authored. "Empty" used as an intransitive verb ("to empty"
        = to become empty/clear) is a licensed concrete physical action
        describing an observable state-change. It is not a copula; the schema
        bans "is/was/are/were/be/been/being" in their copula use, not verbs
        that describe physical transitions. The bone is not FAULT-FORM-COPULA.
        See flag-001 for the advisory recast offer.

    - id: ruling-002
      type: fault
      item: >
        s01n02 — 'the wrong doors open' (adjective modifier + chatter-unpaid):
        see fault-001 and fault-003 above. Both apply.

    - id: ruling-003
      type: fault
      item: >
        s02n02 — 'the wrong men enter the ward junctions' (adjective modifier):
        see fault-002 above. FAULT-FORM-MODIFIER. Recast "the men enter the
        ward junctions" preserves event-coverage. No event-coverage weakening:
        the ward-junction catalogue geography names the specific location; the
        physical event (men entering named geography) is complete without the
        characterization modifier.

    - id: ruling-004
      type: fault
      item: >
        s01n02 and s02n01 — chatter bones without cost_ledger_anchor:
        see fault-003 and fault-004 above. Both are FAULT-BONE-DELTA-MALFORMED.
        The grounding-bone defense is not sufficient to waive the chatter-unpaid
        rule: per the command, "a grounding bone is a normal moving/held/chatter
        bone; the quota is about SVO concreteness, not a new shape — so a
        grounding bone that is ALSO chatter still needs the chatter
        cost_ledger_anchor." Fixer must either (a) add axes_held with rationale
        or (b) add a valid cost_ledger_anchor.

    - id: ruling-005
      type: fault
      item: >
        s02n06 — 'the passage-counts fill the violence' (abstract object):
        see fault-005 above. FAULT-FORM-INTERIORITY. The SVO is semantically
        incoherent at the object position ("the violence" is not a named
        physical entity).

    - id: ruling-006
      type: fault
      item: >
        s05n03 — 'the architecture returns to substrate' (prepositional destination):
        see fault-006 above. FAULT-FORM-MODIFIER. The recast offered by the
        screen-writer ("the insects drop below surveillance range") also contains
        a prepositional phrase of destination and does not resolve the fault.

    - id: ruling-007
      type: pass
      item: >
        s05n05 — 'runs the ledger' / s05n01 — 'closes the feed' /
        s02n05 — 'opens the feed' / s03n05 — 'opens the ledger':
        CORRECT. "Runs," "closes," and "opens" are licensed concrete physical
        verbs in these usages. "Runs the ledger" = the stylus moves across
        entries (physical act, not perception). "Opens/closes the feed/ledger"
        = physical acts on a physical object (ledger cover, feed-state). None
        are perception verbs (reads/sees/knows/feels/notices); none are
        non-action verbs (has/holds/carries/wears). CLEAN.

    - id: ruling-008
      type: pass
      item: "Earth-Bet fence scan — all 30 bones"
      ruling: >
        CLEAN. No SVO contains a Worm-canon proper noun (Khepri, Gold Morning,
        Skitter, Weaver, shard, trigger, parahuman, PRT, Undersiders, Birdcage,
        or any cape name). "Architecture" is licensed functional description
        of Taylor's insect network, not a parahuman term. "Substrate" is a
        physical referent (ambient insect population). "Feed" is established
        project-vocabulary for Taylor's insect-sense output. No Earth-Bet
        fence violations in any SVO.

  summary:
    verdict: FAULT
    fault_count: 6
    fault_classes:
      FAULT-FORM-MODIFIER: 3  # fault-001 (s01n02 "wrong doors"), fault-002 (s02n02 "wrong men"), fault-006 (s05n03 "returns to substrate")
      FAULT-BONE-DELTA-MALFORMED: 2  # fault-003 (s01n02 chatter-unpaid), fault-004 (s02n01 chatter-unpaid)
      FAULT-FORM-INTERIORITY: 1  # fault-005 (s02n06 "fill the violence")
    flag_count: 3  # all non-blocking minimum-granularity or borderline-verb advisories
    constraint_violations: 0  # cond-earth-bet-noun-fence CLEAN; cond-westerosi-magic-dormant CLEAN; cond-override-architecture-residue CLEAN; cond-kl-witch-label CLEAN; cond-taylor-pov-behavior CLEAN (bones layer; first-person transformation is /and-stitch responsibility)
    aggregate_delta_check: PASS-WITH-FLAGS  # chapter and scene totals match contracts; bone proportional distribution within ±1 rank tolerance at minimum-granularity floor; two advisory flags (s01 and s05 moral_legibility equal to larger-contract axes)
    cost_ledger_check: PASS  # all anchors are cl07a / cl07b / cl07c (valid for this chapter); no orphaned anchors
    earth_bet_fence: CLEAN
    fixer_routing: >
      Route to fixer with fault-001 through fault-006. Fixer may apply
      flag-001's recast (s01n01) as a zero-cost cleanup if accepted.
      Flags 002 and 003 require no fixer action — advisory only.
      After fixer resolution, bones draft returns to /and-write Phase 3
      (shape pass) before Phase 6 bone-gate.
```
