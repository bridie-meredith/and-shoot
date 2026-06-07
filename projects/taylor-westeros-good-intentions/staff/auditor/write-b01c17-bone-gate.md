```yaml
audit:
  scope: chapter
  target: b01c17
  timestamp: 2026-06-04
  gate: /and-write Phase 2 (constraint/form) + Phase 6 (substance bone-gate)
  bone_gate_verdict: FAIL
  fail_reasons:
    - FAULT-FORM-MODIFIER (23 bones; HARD)
    - FAULT-FORM-NEGATION (3 bones; HARD)
    - FAULT-FORM-CONJUNCTION (1 bone; HARD)
    - FAULT-COST-LEDGER-UNRESOLVED (1 bone; HARD)
  enactment_gate: MET  # pl-2026-06-04-c17-002 resolves at this Phase 6
  signals:
    - ABSTRACTION-DOMINANT (s02; accept-with-rationale)
    - STAKES-AXIS-NOT-DOMINANT (s03; co-dominant; accept-with-rationale)
    - REGISTER-AS-MANNERISM (VERB+OBJECT "returns the Norren attribution" × 3)

  findings:

    # ── PHASE 2: CONSTRAINT / FORM ──────────────────────────────────────────

    - id: fault-001
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s01n03 — "the query returns a height-and-gait pattern across six
        observation points" — PP "across six observation points" appended to SVO.
      why: >
        Prepositional phrases of place, extent, or accompaniment are banned per
        bones.schema.md § FAULT-FORM-MODIFIER. PP padding survives into the
        stitched prose as register-weight and creates the hyphen-compound density
        pattern that prior cold-reads have flagged as readability drag.
      criteria: >
        Bone SVO must be bare subject-verb-object with no prepositional phrase.
        The six-observation-point detail belongs in the event_map or a sensory
        facet citation, not the bone itself.

    - id: fault-002
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s01n05 — "taylor-hebert-kl-122ac stops at the water-trough" — PP
        "at the water-trough" appended to intransitive motion-stop verb.
      why: >
        PP of place on a motion-stop verb is banned. "stops" without a destination
        object is an intransitive motion verb; the location belongs in a location-
        state facet citation, not the bone.
      criteria: >
        Recast as a transitive form with the location as direct object
        (e.g., "taylor-hebert-kl-122ac stops the walk" with the trough as
        the environment cited via loc-state), or use a verb that takes the
        location as direct object.

    - id: fault-003
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s01n06 — "the feed returns the second-step hesitation across the
        east-of-water-gate interval" — PP "across the east-of-water-gate interval"
        appended to SVO.
      why: >
        PP of extent appended to SVO. The interval is environmental context, not
        part of the bare action. Same structural form as fault-001.
      criteria: >
        Bare SVO only. The east-of-water-gate interval detail routes to event_map
        entry or loc-state citation.

    - id: fault-004
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s01n07 — "the coverage log matches the eleven-day interval to the
        stitch-house rotation" — PP "to the stitch-house rotation" appended to SVO.
      why: >
        PP of destination/association appended to verb. "matches X to Y" is a
        two-object construction where "to Y" is a prepositional phrase, not a
        direct object.
      criteria: >
        Recast as bare transitive SVO. The stitch-house rotation detail routes
        to event_map or memory facet.

    - id: fault-005
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s02n02 — "the accounting prices the name-option to its terminus" —
        PP "to its terminus" appended to SVO.
      why: >
        PP of destination appended to verb. "to its terminus" is directional
        padding; the bare action is "the accounting prices the name-option."
      criteria: >
        Strip "to its terminus." If the terminus detail is load-bearing, it
        routes to a memory or narrator-interest facet citing this bone.

    - id: fault-006
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s02n03 — "the ledger returns the exposure-entry for the name-option"
        — PP "for the name-option" appended to SVO.
      why: >
        PP of purpose/qualification appended to SVO. The bare action is
        "the ledger returns the exposure-entry."
      criteria: >
        Strip the PP. The name-option association routes to event_map or
        facet citation.

    - id: fault-007
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s02n05 — "the accounting prices the false-attribution cost against
        the ward-elder" — PP "against the ward-elder" appended to SVO.
      why: >
        PP of comparison/opposition appended to verb. "against the ward-elder"
        is a prepositional modifier, not a direct object.
      criteria: >
        Recast as bare SVO. If the ward-elder's role is load-bearing (as it is —
        this is the false-attribution target), the bone should name the ward-elder
        as the direct object via a transitive verb, not via a PP.

    - id: fault-008
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER + FAULT-FORM-NEGATION
      scope: bone
      what: >
        b01c17s02n06 — "the ledger returns no resolution across both entries" —
        (1) "no resolution" negates the object; (2) "across both entries" is a PP
        of extent.
      why: >
        Double fault. FAULT-FORM-NEGATION: "no resolution" records a non-event
        (what did NOT happen). Bones record what DID happen; non-events route to
        facets. FAULT-FORM-MODIFIER: "across both entries" is a PP of extent.
        The bone currently records an absence, which per the schema is not a
        valid bone content.
      criteria: >
        Recast as a positive physical act that enacts the same held-axis
        discipline (e.g., the physical gesture Taylor makes when the accounting
        fails to resolve — a step, a continued walk, a pen set down). The
        absence-of-resolution is the facet layer's territory; the bone must
        record what physically occurred.

    - id: fault-009
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s02n08 — "the accounting returns the screen-option shape against
        the override-architecture shape" — PP "against the override-architecture
        shape" appended to SVO.
      why: >
        PP of comparison appended to verb. Same structural form as fault-007.
      criteria: >
        Strip the PP. If the override-architecture parallel is load-bearing
        (it is — it is the chapter's central irony), it routes to the
        event_map entry for override-architecture-recognition-begins or a
        memory/narrator-interest facet citation.

    - id: fault-010
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s02n09 — "taylor-hebert-kl-122ac extends the walk along the
        Hook's edge" — PP "along the Hook's edge" appended to SVO.
      why: >
        PP of direction/path appended to intransitive motion verb. Per the schema,
        intransitive motion verbs without destination fault FAULT-FORM-NO-VERB;
        adding a path PP instead of a destination object is the same form error.
      criteria: >
        Recast with a transitive verb taking the location as direct object, or
        drop the PP and route the location to loc-state facet citation.

    - id: fault-011
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s03n02 — "taylor-hebert-kl-122ac pulls the coverage log from the
        east-of-water-gate corridor" — PP "from the east-of-water-gate corridor"
        appended to SVO.
      why: >
        PP of source appended to transitive verb. The source-location is
        environmental context that belongs in a loc-state citation.
      criteria: >
        Strip the PP. "taylor-hebert-kl-122ac pulls the coverage log" is the
        bare SVO; the source-location routes to loc-state.

    - id: fault-012
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s03n06 — "the pen adds two supplementary observation lines to the
        Norren entry-cluster" — PP "to the Norren entry-cluster" appended to SVO.
      why: >
        PP of destination appended to transitive verb. "to the Norren
        entry-cluster" is directional padding; the bare action is
        "the pen adds two supplementary observation lines."
      criteria: >
        Strip the PP. The Norren entry-cluster as target can be carried by the
        event_map (ward-elder-substitution already covers this) or by a loc-state
        citation naming the log as the active document.

    - id: fault-013
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s03n07 — "taylor-hebert-kl-122ac sets the pen beside the coverage
        log" — PP "beside the coverage log" appended to SVO.
      why: >
        PP of location appended to transitive placement verb. The placement
        destination is environmental context.
      criteria: >
        Recast with a transitive verb taking the location as direct object, or
        strip the PP and route the "beside the log" detail to a sensory/grounding
        facet citation. The physical act of setting-down is the bone; the spatial
        relationship is facet territory.

    - id: fault-014
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s03n08 — "the coverage log returns the Norren attribution across
        the east-of-water-gate interval" — PP "across the east-of-water-gate
        interval" appended to SVO.
      why: >
        PP of extent appended to SVO. Same structural form as fault-003.
      criteria: >
        Bare SVO only. Strip the interval PP.

    - id: fault-015
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s03n09 — "taylor-hebert-kl-122ac slides the updated log segment
        toward the Jarvis drop-channel" — PP "toward the Jarvis drop-channel"
        appended to SVO.
      why: >
        PP of direction appended to transitive verb. "toward" is a directional
        preposition, not a direct-object marker. The schema bans directional PPs.
      criteria: >
        Recast with a transitive verb that takes the drop-channel as direct object
        (e.g., "routes the updated log segment to the Jarvis channel" is still PP,
        but "delivers the updated log segment" with destination in loc-state is
        cleaner). The destination detail routes to loc-state or event_map.

    - id: fault-016
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s03n10 — "the coverage log returns the false-attribution shape
        against the override-architecture shape" — PP "against the override-
        architecture shape" appended to SVO.
      why: >
        PP of comparison appended to SVO. Same structural form as fault-009.
      criteria: >
        Strip the PP. The override-architecture parallel routes to the event_map
        entry for override-architecture-parallel and to a memory or narrator-
        interest facet citation.

    - id: fault-017
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n01 — "the dead drop returns the morning ward-read without a
        follow-up query" — PP "without a follow-up query" is negation-adjacent
        (records the absence of a query) and functions as a PP modifier.
      why: >
        FAULT-FORM-NEGATION: "without a follow-up query" records what did NOT
        arrive; bones record what DID happen. FAULT-FORM-MODIFIER: "without X"
        is a PP of accompaniment (negative). The no-query-arrival is the
        apparatus-query-closes event; the bone must record the positive physical
        event, not the negative attribute.
      criteria: >
        Recast as the positive event that constitutes query-closure (e.g.,
        "the dead drop returns the morning ward-read" as the bare act; the
        absence of a follow-up is a consequence delivered via the event_map
        apparatus-query-closes entry and a facet citation).

    - id: fault-018
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n02 — "the apparatus picture returns the Norren attribution
        as the east-of-water-gate entry" — PP/appositive "as the east-of-water-
        gate entry" appended to SVO.
      why: >
        "as X" is a resultative complement functioning as a modifier. The bare
        SVO is "the apparatus picture returns the Norren attribution"; the
        appositive extends the object with qualifying information.
      criteria: >
        Strip "as the east-of-water-gate entry." The attribution-as-closed-entry
        detail routes to the event_map apparatus-query-closes entry.

    - id: fault-019
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n03 — "wren crosses the morning ward-read through the east-of-
        water-gate corridor" — PP "through the east-of-water-gate corridor"
        appended to motion verb.
      why: >
        PP of path appended to transitive motion verb. The corridor is the
        location context, not the direct object of crossing.
      criteria: >
        Recast so the corridor is the direct object ("wren crosses the east-of-
        water-gate corridor") or strip the PP and route to loc-state.

    - id: fault-020
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n04 — "the morning ward-read returns the second-step hesitation
        across the scar-tissue interval" — PP "across the scar-tissue interval"
        appended to SVO.
      why: >
        PP of extent appended to SVO. Same structural form as fault-003/fault-014.
      criteria: >
        Strip the interval PP. The scar-tissue detail routes to the event_map
        entry for wren-second-step-interval or a sensory facet.

    - id: fault-021
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n05 — "taylor-hebert-kl-122ac lifts the pen from the cost-
        ledger page" — PP "from the cost-ledger page" appended to SVO.
      why: >
        PP of source appended to transitive verb. Same structural form as
        fault-011.
      criteria: >
        Strip the PP. The cost-ledger page as the source-context routes to
        a loc-state or grounding facet citation.

    - id: fault-022
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER + FAULT-FORM-NEGATION
      scope: bone
      what: >
        b01c17s04n06 — "the cost-ledger page returns the entry-slot without
        an inscription" — (1) "without an inscription" is a negation (records
        the absence of inscription); (2) it is also a PP modifier.
      why: >
        Double fault matching fault-008. The absence-of-inscription is the
        enacted-absence that the enactment gate (pl-2026-06-04-c17-002 point 4)
        requires. The gate IS met via n05 (positive act: Taylor lifts the pen),
        but n06 in its current form records what did NOT happen rather than what
        DID. The enacted absence must be rendered as a positive physical act.
      criteria: >
        Recast as the positive physical act that enacts the absence (e.g.,
        the ledger page as a physical surface with a characteristic that is
        observable — the column's blank state expressed through what the page
        shows rather than what it lacks). The enacted-absence gate is preserved
        through n05; n06 must record a positive event.

    - id: fault-023
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n07 — "the coverage log returns the Norren attribution as a
        permanent structural feature" — PP/complement "as a permanent structural
        feature" appended to SVO.
      why: >
        "as X" resultative complement functioning as modifier, same form as
        fault-018. "permanent structural feature" is also an adjective-heavy
        description that the schema explicitly bans (no modifiers, including
        adjectives in the object position used as qualifiers).
      criteria: >
        Strip "as a permanent structural feature." The permanence/structural
        consequence routes to the event_map (false-attribution-now-structural)
        and a state-update or memory facet.

    - id: fault-024
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      scope: bone
      what: >
        b01c17s04n08 — "the accounting returns the override-architecture shape
        against the protection-delivered shape" — PP "against the protection-
        delivered shape" appended to SVO.
      why: >
        PP of comparison, same form as fault-009 and fault-016. The irony
        comparison belongs in the event_map (irony-made-explicit) and facet layer.
      criteria: >
        Strip the PP. "the accounting returns the override-architecture shape"
        is the bare bone; the protection-delivered parallel routes to the
        event_map entry for irony-made-explicit.

    - id: fault-025
      type: fault
      severity: HARD
      class: FAULT-FORM-CONJUNCTION
      scope: bone
      what: >
        b01c17s03n03 — "the coverage log returns the entry-cluster across
        eleven days and six observation points" — "and" joins "eleven days"
        and "six observation points" within the object-qualifying phrase.
        Additionally "across eleven days" is itself a PP modifier.
      why: >
        Conjunction "and" within the bone violates FAULT-FORM-CONJUNCTION
        regardless of whether it appears in the main clause or a qualifying
        phrase. The schema states: "No conjunctions. No `and`, `but`, `while`,
        `as`." The PP "across eleven days and six observation points" also
        carries a FAULT-FORM-MODIFIER.
      criteria: >
        Strip the entire qualifying phrase. The bare SVO "the coverage log
        returns the entry-cluster" is the bone; the eleven-day / six-point
        detail routes to event_map or a memory/sensory facet.

    # ── PHASE 6: SUBSTANCE BONE-GATE ────────────────────────────────────────

    - id: fault-026
      type: fault
      severity: HARD
      class: FAULT-COST-LEDGER-UNRESOLVED
      scope: bone
      what: >
        b01c17s03n06 — cost_ledger_anchor field contains only "cl07b" but the
        bone delivers two axis movements: (1) position-prot-collapse DOWN 1.0
        (cl07b cost side) and (2) social_tether-prot-collapse DOWN 1.0 (cl07a
        cost side). cl07a is not cited in the cost_ledger_anchor field.
      why: >
        The scene substance_delta for b01c17s03 specifies social_tether-prot-
        collapse DOWN 1.0 with cost_ledger_anchor: cl07a. The bone annotation
        explicitly acknowledges that cl07a fires alongside cl07b on this bone.
        But the bone's cost_ledger_anchor field does not cite cl07a. A cost-
        ledger entry's cost side must be anchored by citation in the delivering
        bone's cost_ledger_anchor field, or the ledger entry's cost-side settlement
        is untracked. At book-close roll-up, cl07a's cost allocation in this chapter
        will appear as unanchored in the ledger accounting.
      criteria: >
        The bone's cost_ledger_anchor field must include both cl07b and cl07a.
        Both collapse axes' cost sides fire on this bone and both ledger entries
        must be cited.

    # ── SIGNALS ──────────────────────────────────────────────────────────────

    - id: signal-001
      type: flag
      severity: SIGNAL
      class: ABSTRACTION-DOMINANT
      scope: scene
      what: >
        b01c17s02 — 2 grounding bones out of 9 total = 22%. Threshold is
        ceil(0.25 × 9) = 3 grounding bones. s02 falls 1 bone below the
        25% floor.
      why: >
        The abstraction-dominant signal at s02 means the pricing/recognition
        scene has no physical anchor beyond the chapter-open walk (n01) and
        the walk-continuation (n09). All interior accounting content is
        non-grounded. This is by design (s02 is explicitly the interior-
        accounting scene), but the signal fires per the gate definition.
      disposition: >
        ACCEPT-WITH-RATIONALE. s02 is the scene-class that is legitimately
        interior: Taylor pricing two options while walking, no physical action
        beyond walking. The 2-grounding-bone count (n01: Hook's southern edge;
        n09: Hook's edge) anchors the physical frame. The chapter contract's
        density_target of 0.70-0.80 acknowledges the interior-heavy load. No
        remediation required; note should carry to /and-stitch Phase 4
        voice-embodiment for grounding-ledger awareness.

    - id: signal-002
      type: flag
      severity: SIGNAL
      class: STAKES-AXIS-NOT-DOMINANT
      scope: scene
      what: >
        b01c17s03 — stakes_axis is capability (+1.0 delivered). Two non-stakes
        axes also deliver magnitude 1.0: position-prot-collapse (-1.0) and
        social_tether-prot-collapse (-1.0). capability is tied for largest
        magnitude, not strictly dominant.
      why: >
        The gate requires the stakes_axis's delivered aggregate to be "the
        largest in the scene." capability at +1.0 is co-dominant (tied with
        each collapse axis at 1.0 absolute magnitude) rather than strictly
        dominant. Strictly read, this fires STAKES-AXIS-NOT-DOMINANT.
      disposition: >
        ACCEPT-WITH-RATIONALE. The co-dominance is load-bearing by design:
        s03's structural argument is that the capability gain and the
        collapse activations are the SAME event (the pen-on-page fires all
        three simultaneously). Making capability strictly larger than the
        collapse axes would require either reducing the collapse magnitude
        (below contract target) or inflating capability (above contract
        target). Neither is correct. The co-dominant structure reflects the
        chapter's irony: protection and trap-tightening are mechanically
        identical. No remediation required; this disposition should be
        noted in the scene annotation.

    - id: signal-003
      type: flag
      severity: SIGNAL
      class: REGISTER-AS-MANNERISM
      scope: chapter
      what: >
        VERB+OBJECT pair "returns the Norren attribution" appears in 3 bones:
        b01c17s03n08 ("the coverage log returns the Norren attribution across
        the east-of-water-gate interval"), b01c17s04n02 ("the apparatus picture
        returns the Norren attribution as the east-of-water-gate entry"),
        b01c17s04n07 ("the coverage log returns the Norren attribution as a
        permanent structural feature"). Threshold is ≥3 instances of the same
        VERB+OBJECT pair across the chapter.
      why: >
        Three identical VERB+OBJECT pairs signal register-as-mannerism: the
        false attribution is being delivered via the same mechanical formula
        each time rather than through differentiated action. At /and-stitch
        this creates a triple-repetition risk in the rendered prose regardless
        of how the PP modifiers are varied. The three bones also all carry
        FAULT-FORM-MODIFIER faults (fault-014, fault-018, fault-023), so the
        form rewrites required by those faults may naturally differentiate the
        verbs. Recommended: fixer assess whether the three bones can be
        distinguished at verb level during the fault-remediation pass (the
        attribution-as-confirmed, attribution-as-closed-entry, and attribution-
        as-permanent-structure are three distinct events and warrant three
        distinct verb forms).
      disposition: >
        REMEDIATE-DURING-FAULT-PASS. The form fault rewrites (fault-014,
        fault-018, fault-023) require these bones to be recast anyway. During
        those rewrites, differentiate the verb for each of the three uses.

    # ── ENACTMENT GATE ──────────────────────────────────────────────────────

    - id: gate-001
      type: pass
      class: ENACTMENT-GATE
      scope: chapter
      what: >
        Parking-lot item pl-2026-06-04-c17-002 — four required enactment points
        assessed at Phase 6.
      why: N/A (pass)
      disposition: >
        MET across all four points.

        Point 1 (s03 collapse-axis activation with physical form): s03n05
        (taylor writes the first attribution line — pen on page; record changed)
        + s03n06 (pen adds two supplementary observation lines — the false record
        now sits in the log; extraction now requires resolving what is written).
        The structural difference before/after is in the physical record.
        ENACTMENT POINT 1: MET.

        Point 2 (Norren false-attribution as present-tense physical write-action):
        s03n05 (taylor writes first attribution line) + s03n06 (pen adds two
        supplementary observation lines). No future-tense or summary framing.
        ENACTMENT POINT 2: MET.

        Point 3 (s01 wren-identification = feed/log-event bone, not Taylor-
        cognition): s01n06 subject = "the feed" / s01n07 subject = "the coverage
        log." Neither bone has Taylor as the identifying subject.
        ENACTMENT POINT 3: MET.

        Point 4 (echo-naming closes on shape-language + s04 enacted-absence as
        positive form): s03n10 (coverage log returns the false-attribution shape
        — shape-language, no proper-noun leak) → s03n11 (taylor leaves the pen
        beside the open log — positive physical gesture, scene closes). s04
        enacted-absence: s04n05 (taylor lifts the pen from the cost-ledger page —
        positive physical act). NOTE: s04n06 carries FAULT-FORM-NEGATION (fault-022)
        via "without an inscription," but the enacted-absence gate is met through
        n05's positive form; n06's fault does not ungate point 4.
        ENACTMENT POINT 4: MET.

        Parking-lot item pl-2026-06-04-c17-002 RESOLVES at this Phase 6.
        Status should be updated to resolved upon fixer completing all HARD
        findings and re-gate PASSING.

    # ── PASSING CHECKS (summary) ─────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: Axis-sum verification against scene and chapter targets.
      why: N/A
      disposition: >
        All per-scene and chapter-level axis sums match contracted targets.
        s01 all-held confirmed. s02 moral_framework -0.5 confirmed. s03
        capability +1.0 / moral_framework -0.5 / position-prot-collapse -1.0
        / social_tether-prot-collapse -1.0 all confirmed. s04
        relational_anchor_status +0.5 confirmed. Chapter total:
        relational_anchor_status +0.5 / capability +1.0 / moral_framework -1.0
        / position-prot-collapse -1.0 / social_tether-prot-collapse -1.0.
        All match memory.md substance_delta targets at chapter level.

    - id: pass-002
      type: pass
      what: Per-bone axis movement physical causation (moving bones).
      why: N/A
      disposition: >
        s02n04 (accounting opens screen-option entry → moral_framework -0.5):
        Borderline — "the accounting" is the chapter's established functional-
        mechanism idiom, not Taylor-cognition introduced fresh. Prior chapters
        (c15/c16) shipped identical idiom through bone-gate. Accepted as chapter-
        licensed abstract-subject bone under the established project precedent.
        s03n04/n05 (capability +0.5 each): concrete physical actions (opens
        entry-cluster / writes attribution line) physically cause the declared
        Δ. s03n06 (pen adds lines → collapse axes -1.0 each): concrete
        instrument-as-subject physically causes both collapse-axis activations.
        s04n02 (apparatus picture returns Norren attribution → relational_anchor
        +0.5): functional mechanism delivers the protection-confirmation; gate
        passes on project-established idiom.

    - id: pass-003
      type: pass
      what: Held-axis enactment (all held bones).
      why: N/A
      disposition: >
        All held bones name the discipline/stillness rationale. No
        HELD-AXIS-NOT-ENACTED finding. Held axes in bones are all consistent
        with the scene-level axes_held[] declaration or axes_in_motion[]
        (post-move holding; precedent pl-2026-05-25-018 applies throughout).

    - id: pass-004
      type: pass
      what: EVENT-presence and EVENT-MAP-INCOMPLETE.
      why: N/A
      disposition: >
        All four scenes: every event_map[] entry has covering bones; every
        chunk tag has a matching event_map entry. Central events and
        protagonist_force events are each covered by ≥1 bone.

    - id: pass-005
      type: pass
      what: Opposing-force visible (all four scenes).
      why: N/A
      disposition: >
        s01: apparatus query content (n04 + n08). s02: accounting pricing
        mechanism (n02-n03-n05-n06-n08). s03: override-architecture enacted
        (n06 + n10). s04: permanent false attribution in record (n07 + n08).
        Opposing force present and physical in all four scenes.

    - id: pass-006
      type: pass
      what: Cost-ledger entries cl03a and cl-d11 paid correctly.
      why: N/A
      disposition: >
        cl03a (moral_framework down): cost side fires at s02n04 (cl03a cited,
        -0.5) and s03n05 (cl03a cited, -0.5). Total = -1.0. Direction correct.
        cl-d11 (relational_anchor_status up): gain side fires at s04n02
        (cl-d11 cited, +0.5). Direction correct.

    - id: pass-007
      type: pass
      what: cl07b paid correctly at s03n06.
      why: N/A
      disposition: >
        position-prot-collapse DOWN 1.0 at s03n06 with cost_ledger_anchor: cl07b.
        cl07b cost side = position-prot-collapse -6 total; -1.0 first allocation.
        Direction and anchor correct. The cl07a fault (fault-026) is a separate
        finding on the missing co-anchor for the same bone.

    - id: pass-008
      type: pass
      what: Earth-Bet fence — no Khepri/Gold Morning/parahuman/shard proper nouns.
      why: N/A
      disposition: >
        36 bones audited. Zero Earth-Bet proper nouns. Override-architecture
        parallel uses shape-language only ("override-architecture shape,"
        "override-architecture parallel," "false-attribution shape"). Fence clean.

    - id: pass-009
      type: pass
      what: Dialogue check — zero dialogue-anchor bones required.
      why: N/A
      disposition: >
        Chapter is solitary (taylor-hebert-kl-122ac alone; Jarvis is dead-drop
        courier channel, no on-page speech). Zero bones use "speaks to" form.
        Zero bones require dialogue-anchor citations. Dialogue checks N/A.

    - id: pass-010
      type: pass
      what: Sensory grounding quota (≥1 grounding bone per 5 bones, all scenes).
      why: N/A
      disposition: >
        s01: 4/8 = 50%. s02: 2/9 = 22% (ABSTRACTION-DOMINANT signal fires
        separately; quota ≥1 per 5 → ≥2 per 9 → met with 2). s03: 8/11 = 73%.
        s04: 5/8 = 63%. All scenes meet the grounding quota minimum.

    - id: pass-011
      type: pass
      what: Valid axis slugs — all axis_moves and axes_held entries use valid slugs.
      why: N/A
      disposition: >
        All slugs audited against the valid slug list: moral_framework,
        capability, position-prot-rise, position-prot-collapse,
        relational_anchor_status, moral_legibility_to_self,
        political_register-prot, social_tether-prot-rise,
        social_tether-prot-collapse, social_tether-antag, position-world,
        political_register-world. No invalid slugs found.

    - id: pass-012
      type: pass
      what: FAULT-PHYSICAL / FAULT-CONSTRAINT — cast and location constraints.
      why: N/A
      disposition: >
        Cast = taylor-hebert-kl-122ac (solitary). All bones use Taylor as actor
        where a named actor is subject, or use a physical mechanism/prop/instrument
        as subject (the feed, the coverage log, the pen, the accounting, the ledger,
        the apparatus picture, the dead drop, the cipher-sheet). Wren appears in
        s04n03 as a physical subject — Wren is the chapter's anchor figure and her
        physical presence in the east-of-water-gate corridor is the protection-
        confirmed event. No constraint violation.
        Locations: the room above the tallow-render works (s03), the Hook's
        southern edge (s02), the east-of-water-gate corridor (s01/s03/s04),
        the Fishmonger Gate water-trough (s01). All are in the declared location
        set for this chapter. No FAULT-PHYSICAL.

    - id: pass-013
      type: pass
      what: FAULT-AGGREGATE-DELTA-MISMATCH — per-scene and chapter totals.
      why: N/A
      disposition: >
        All per-scene bone-Δ sums confirmed equal to the scene substance_delta
        targets within ±0 (exact match in all cases). Chapter totals confirmed
        equal to chapter substance_delta targets. No mismatch.

  # ── BONE-GATE VERDICT ────────────────────────────────────────────────────
  verdict: FAIL
  hard_finding_count: 26
    # fault-001 through fault-025: FAULT-FORM-MODIFIER (23) + FAULT-FORM-NEGATION
    #   (3, overlapping with modifier faults at fault-008/fault-017/fault-022) +
    #   FAULT-FORM-CONJUNCTION (1, fault-025) = 25 form faults on 26 bones
    #   (some bones carry multiple classes; unique bone count = see below)
    # fault-026: FAULT-COST-LEDGER-UNRESOLVED (1)
  affected_bones_form:
    # Bones with ≥1 HARD form fault:
    # s01: n03, n05, n06, n07
    # s02: n02, n03, n05, n06, n08, n09
    # s03: n02, n03, n06, n07, n08, n09, n10
    # s04: n01, n02, n03, n04, n05, n06, n07, n08
    # Total affected: 25 of 36 bones carry ≥1 form fault
    # Unaffected (form-clean): s01n01, s01n02, s01n04, s01n08;
    #   s02n01, s02n04, s02n07; s03n01, s03n04, s03n05, s03n11;
    #   s04n (none unaffected in s04 except s04n01 is also faulted)
    # Strictly form-clean: s01n01, s01n02, s01n04, s01n08, s02n01,
    #   s02n04, s02n07, s03n01, s03n04, s03n05, s03n11 = 11 bones
  affected_bones_substance:
    # Bones with ≥1 HARD substance fault:
    # s03n06 (FAULT-COST-LEDGER-UNRESOLVED: cl07a uncited)
  fixer_dispatch_note: >
    Fixer must: (1) recast all 25 form-faulted bones to bare SVO — strip all
    prepositional phrases, eliminate "no/without" negation forms, break the
    s03n03 conjunction — preserving the axis_moves and axes_held structure;
    (2) add cl07a to s03n06's cost_ledger_anchor field alongside cl07b;
    (3) during form rewrites, differentiate the verb for the three
    "returns the Norren attribution" instances (signal-003 remediation-during-
    fault-pass). Substance contracts, event_map assignments, axis_moves
    magnitudes, and axes_held rationales are CORRECT and must be preserved
    unchanged; only the SVO text and the cost_ledger_anchor field require
    modification.
  enactment_gate_resolution: >
    pl-2026-06-04-c17-002 is MET at bone level. The gate resolves upon
    fixer completing all HARD findings and the revised bones file passing
    a re-gate. Update parking-lot status to resolved at that point.
```
