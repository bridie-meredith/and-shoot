audit:
  scope: chapter
  target: b01c09
  timestamp: 2026-05-31
  pass: Phase 2 constraint + SVO form + delta audit
  bones_file: active-project/staff/showrunner/b01c09-bones-draft-2026-05-31.md
  bone_count: 22
  scenes: [b01c09s01, b01c09s02, b01c09s03]

  summary:
    FAULT-FORM: 10
    FAULT-BONE-DELTA-MALFORMED: 2
    FAULT-CONSTRAINT: 0
    FAULT-PHYSICAL: 0
    FAULT-AGGREGATE-DELTA-MISMATCH: 0
    FAULT-COST-LEDGER-UNRESOLVED: 0
    flag: 1
    pass: 9
    verdict: NEEDS-FIXER

  roll_up_check:
    s01_relational_anchor_status: "+0.5 from n04 (moving). Scene contract +0.5. EXACT."
    s02_political_register_prot: "+0.5 from n06 (moving). Scene contract +0.5. EXACT."
    s03_axes_in_motion: "zero. Scene contract zero. EXACT."
    verdict: CLEAN

  cost_ledger_check:
    cl-d08: "present at memory line 1382. RESOLVED."
    cl-d05: "present at memory line 1362. RESOLVED."
    verdict: CLEAN

  findings:

    # ── s01 BONES ─────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      scope: bone
      target: b01c09s01n04
      class: FAULT-BONE-DELTA-MALFORMED
      what: >
        s01n04 axis_moves: relational_anchor_status, direction up, magnitude 0.5.
        The bone delta band is 1–3 per axis per bone (memory line 1465:
        `bone: { delta_per_axis: 1-3 }`). Magnitude 0.5 is below the floor of 1.
      why: >
        The moving bone's magnitude violates the bone-level delta contract. At Phase 6
        the bone-gate will fire SUBSTANCE-FLAT on this bone. The chapter-level target
        (+0.5 for s01) is itself within the chapter band (0.5–1.5) and is the correct
        chapter Δ — but the bone delivering it must carry magnitude ≥ 1. The conflict
        is between the chapter-level target (+0.5) and the bone-level floor (1.0
        minimum). Because the chapter target itself is 0.5, no single bone can satisfy
        both the chapter target and the bone floor simultaneously without overshoot.
        This is a structural tension that fixer cannot resolve by adjusting magnitude
        alone; the resolution is to note that the chapter Δ target (+0.5) itself falls
        below the bone floor, which means the chapter target may need to be accepted
        as a soft-floor exception OR the bone delta band's floor must be treated as
        not applying to sub-tranche draws on multi-chapter cost-ledger arcs. Fixer
        should flag this to showrunner rather than silently adjusting magnitude to 1.0
        (which would overshoot the chapter target).
      criteria: >
        Either (a) confirm that sub-tranche draws (cl-d08 first-tranche +0.5 of +2)
        are exempt from the bone delta floor and document this exception, OR (b) split
        the +0.5 chapter Δ across two bones with the moving bone carrying magnitude 1.0
        and a compensating scene-level note that the chapter target is the sum, not the
        single bone. Do not silently adjust magnitude to 1.0 without resolving the
        overshoot against the chapter target.

    - id: fault-002
      type: fault
      scope: bone
      target: b01c09s01n05
      class: FAULT-FORM-MODIFIER
      what: >
        s01n05 SVO: "wren-stitch-maker-flea-bottom-ward stops at the bread-seller corner."
        "at the bread-seller corner" is a prepositional phrase of place.
        Schema (bones.schema.md § SVO discipline): "Prepositional phrases of place /
        destination / source / direction / instrument / accompaniment are explicitly
        banned (FAULT-FORM-MODIFIER)."
      why: >
        The PP is padding; "stops" requires a direct object or becomes a bare intransitive.
        As written, the bone uses the PP as the locating adjunct rather than making the
        location the direct object via a transitive verb. Downstream facets and stitcher
        will inherit the PP register if not corrected.
      criteria: >
        Recast to transitive SVO with compound-noun direct object, no PP adjunct.
        Minimum-change recast: "wren-stitch-maker-flea-bottom-ward reaches the
        bread-seller corner" — transitive, location as direct object, no PP.
        Preserve bone's substance role (waypoint in daily circuit making pattern legible).

    - id: fault-003
      type: fault
      scope: bone
      target: b01c09s01n06
      class: FAULT-FORM-MODIFIER
      what: >
        s01n06 SVO: "taylor-hebert-kl-122ac sets wren's route in the internal map."
        "in the internal map" is a prepositional phrase of place/instrument.
        Schema: PP of place / direction / instrument banned (FAULT-FORM-MODIFIER).
      why: >
        The internal-map is the destination/instrument of the filing act; its correct
        form is as a direct object via a transitive verb, not a PP adjunct. The PP
        form is the contamination pattern the dispatch brief specifically flags (listed
        in the calibration note as an example to classify). Downstream stitcher renders
        from the SVO; a PP in the bone seeds the prose register.
      criteria: >
        Recast to transitive SVO with compound-noun direct object, no PP.
        Minimum-change recast: "taylor-hebert-kl-122ac files wren's route"
        (c02 precedent: "the insects file the ward-junction contact"; "the accounting
        closes the count"). Filing IS the internal-map act; the internal map is the
        substrate, not a named destination in the bone. Preserve the bone's
        event-map coverage of [force: wren-pattern-noted-in-internal-map].

    # ── s02 BONES ─────────────────────────────────────────────────────────────

    - id: fault-004
      type: fault
      scope: bone
      target: b01c09s02n02
      class: FAULT-FORM (NON-ACTION-VERB + MODIFIER)
      what: >
        s02n02 SVO: "the supply cart rests at the road below the lower gate."
        Two violations:
        (1) "rests" — stative position-naming verb. Schema deny-list (bones.schema.md):
        "Stative position-naming: lies, sits, stands describing position not posture-act"
        are banned (FAULT-FORM-NON-ACTION-VERB). "rests" is in the same semantic class —
        it names the supply cart's static position, not a discrete act.
        (2) "at the road below the lower gate" — PP of place + PP of relative position.
        Schema: PP of place explicitly banned (FAULT-FORM-MODIFIER).
      why: >
        The bone is a grounding/environment anchor (role: held; grounding: true).
        As written, it violates two SVO discipline rules simultaneously. Downstream
        facets (loc-state, sensory) cite the bones file; a stative verb in a grounding
        bone seeds an unclear event anchor for the stitcher.
      criteria: >
        Recast to transitive SVO: a concrete physical verb that takes the location or
        the cart as its direct object, with no PP adjunct. The PP "below the lower gate"
        must be absorbed into a compound-noun object.
        Minimum-change recast: "the supply cart marks the lower-gate road"
        — transitive, compound-noun direct object, no PP. Preserve the bone's
        event-map function as the baseline-body-distribution environmental anchor.

    - id: fault-005
      type: fault
      scope: bone
      target: b01c09s02n04
      class: FAULT-FORM-MODIFIER
      what: >
        s02n04 SVO: "corwick angles the body toward the second man."
        "toward the second man" is a prepositional phrase of direction.
        Schema: "Prepositional phrases of place / destination / source / direction /
        instrument / accompaniment are explicitly banned (FAULT-FORM-MODIFIER)."
        The schema also explicitly notes: "'turns to <named entity>' is banned as a
        directional-prep variant of FAULT-FORM-MODIFIER. The 'to <X>' is a
        prepositional padding phrase." The same structural rule applies to
        "angles the body toward the second man."
      why: >
        The directional PP is padding; the correct form uses a transitive verb that
        takes the second man as direct object. The dispatch brief explicitly lists this
        bone pattern ("corwick holds the delivery-stance at the stone-post") as a PP
        to classify — but fault-005 targets n04's directional PP. The SW-3 physical-
        signature function (courier body-posture before categorization) must be preserved
        in the recast.
      criteria: >
        Recast to transitive SVO with the second man as direct object, no directional PP.
        Minimum-change recast: "corwick faces the second man"
        — transitive, direct object, no PP. Schema allows "faces <X>" as a concrete
        physical posture-act (cf. b01c07 bones-review: "recast flat15->'plants the feet'"
        and "faces" explicitly cleared in that precedent). Preserve the bone's role as
        SW-3 physical-signature part 1.

    - id: fault-006
      type: fault
      scope: bone
      target: b01c09s02n05
      class: FAULT-FORM (NON-ACTION-VERB + MODIFIER)
      what: >
        s02n05 SVO: "corwick holds the delivery-stance at the stone-post."
        Two violations:
        (1) "holds the delivery-stance" — narrow holds-license violation.
        Schema: "holds is licensed only when (1) the object is a body part of the
        subject and the action is stillness-against-pressure, or (2) the object is a
        physical object resisting pressure." "delivery-stance" is a posture-class label
        (an abstraction), not a body part or physical object resisting pressure.
        FAULT-FORM-NON-ACTION-VERB.
        Additionally: "Abstraction-as-object is INTERIORITY. A physical verb whose
        object is an abstract noun is a thought-figure, not an event."
        FAULT-FORM-INTERIORITY (border case — delivery-stance is a posture label).
        (2) "at the stone-post" — PP of place. FAULT-FORM-MODIFIER.
      why: >
        The dispatch brief explicitly lists this bone as requiring classification.
        The bone is SW-3 part 2 (physical-signature continued); the held-stance is the
        observable that the categorization at n06 processes. A malformed SVO here
        undermines the SW-3 split's physical-data chain. Both violations must be cleared
        for the bone to pass Phase 6.
      criteria: >
        Recast to transitive SVO with a concrete body-act direct object, no PP of place,
        no abstraction-object. The stone-post as location must be either absorbed into a
        compound-noun or dropped (the location is established by n03).
        Minimum-change recast: "corwick plants the feet at the stone-post" is still PP.
        Better: "corwick braces the stone-post" (using the post as the direct object of
        a stabilizing act, no PP). Or: "corwick grounds the stance" — but stance is
        still semi-abstract. Cleanest: "corwick squares the shoulders" — concrete body
        part as direct object, stillness-against-pressure licensed form. The exact SVO
        is fixer's determination; the criteria are: concrete physical act, body-part or
        physical-object direct object, no PP, SW-3 physical-signature function preserved.

    - id: fault-007
      type: fault
      scope: bone
      target: b01c09s02n06
      class: FAULT-FORM-MODIFIER
      what: >
        s02n06 SVO: "taylor-hebert-kl-122ac sets the posture-class in the feed-record."
        "in the feed-record" is a prepositional phrase of place/instrument.
        Schema: PP of place / instrument explicitly banned (FAULT-FORM-MODIFIER).
        Listed in dispatch brief's calibration note as a specific example to classify.
      why: >
        This is the moving bone for s02 (political_register-prot +0.5, cl-d05). A PP
        in the moving bone seeds the downstream register for the central-event delivery.
        The feed-record as destination belongs in a compound-noun direct object.
      criteria: >
        Recast to transitive SVO with compound-noun direct object, no PP.
        Minimum-change recast: "taylor-hebert-kl-122ac files the posture-class"
        (c02 precedent: "the insects file the ward-junction contact"; c06 precedent:
        "the accounting closes the fever-cluster entry"). The feed-record is the
        substrate the filing act uses; it need not appear in the bone if it is
        contextually established. Preserve moving-bone's event-map coverage of
        [event: black-faction-contact-inferred] and [event: courier-dragonpit-observation-logged].

    - id: fault-008
      type: fault
      scope: bone
      target: b01c09s02n06
      class: FAULT-BONE-DELTA-MALFORMED
      what: >
        s02n06 axis_moves: political_register-prot, direction up, magnitude 0.5.
        Bone delta band: `bone: { delta_per_axis: 1-3 }` (memory line 1465).
        Magnitude 0.5 is below the floor of 1.
      why: >
        Same structural tension as fault-001. The chapter-level target for
        political_register-prot is +0.5, which is itself below the bone-floor minimum
        of 1.0. The bone delivering this Δ cannot simultaneously satisfy the chapter
        target (+0.5) and the bone floor (≥1.0). This is a cross-contract tension
        that requires a fixer/showrunner judgment call, not a simple recast.
      criteria: >
        Same resolution path as fault-001: either (a) confirm sub-tranche draws on
        multi-chapter cost-ledger arcs (cl-d05 continuation) are exempt from the bone
        floor and document the exception, OR (b) restructure the scene's Δ allocation
        so the moving bone carries magnitude 1.0 and the chapter contract is revised
        accordingly. Do not silently inflate magnitude without resolving the chapter
        target conflict.

    - id: fault-009
      type: fault
      scope: bone
      target: b01c09s02n07
      class: FAULT-FORM-MODIFIER
      what: >
        s02n07 SVO: "taylor-hebert-kl-122ac logs the observation in the feed-record."
        "in the feed-record" is a prepositional phrase of place/instrument.
        Schema: PP of place / instrument explicitly banned (FAULT-FORM-MODIFIER).
        Listed in dispatch brief's calibration note as a specific example to classify.
      why: >
        The bone is a held bone (post-move hold after n06); the PP duplicates the
        substrate reference already implied by the scene. The stitcher inherits the
        PP register.
      criteria: >
        Recast to transitive SVO with compound-noun direct object, no PP.
        Minimum-change recast: "taylor-hebert-kl-122ac closes the observation-entry"
        (c02 precedent: "the accounting closes the fever-cluster entry"; "the ledger
        closes the dark-junction entry"). Preserve event-map coverage of
        [event: courier-dragonpit-observation-logged] and
        [force: courier-observation-withheld-from-jarvis-channel].

    # ── s03 BONES ─────────────────────────────────────────────────────────────

    - id: fault-010
      type: fault
      scope: bone
      target: b01c09s03n03
      class: FAULT-FORM-MODIFIER
      what: >
        s03n03 SVO: "taylor-hebert-kl-122ac brings the seal down on the packet."
        "down on the packet" contains:
        (1) "down" — directional/manner adverb (FAULT-FORM-MODIFIER: adverbs banned).
        (2) "on the packet" — PP of place (FAULT-FORM-MODIFIER: PP of place banned).
        Schema: "No modifiers. No adjectives, no adverbs, no prepositional padding."
      why: >
        This is the CENTRAL EVENT bone for s03 per the draft comments. A modifier-laden
        SVO on the central-event bone is a HARD issue at Phase 6 (URI-WRITE-EVENT-
        CONCRETENESS: "EVENT-NOT-CONCRETE" fires if the central-event bone is not a
        clean SVO). The scene's thesis-image function requires a clean, concrete SVO.
      criteria: >
        Recast to transitive SVO, no adverb, no PP.
        Minimum-change recast: "taylor-hebert-kl-122ac seals the packet"
        (c06 direct precedent: "taylor-hebert-kl-122ac seals the jarvis-channel form").
        Preserve the bone's role as central-event anchor for [image: seal-down-on-packet-
        contents] and [event: daily-accounting-closes].

    - id: fault-011
      type: fault
      scope: bone
      target: b01c09s03n04
      class: FAULT-FORM (NON-ACTION-VERB + MODIFIER)
      what: >
        s03n04 SVO: "the ward-coverage notes rest on the station surface."
        Two violations:
        (1) "rest" — stative position-naming verb (same class as lies/sits/stands
        describing position, not posture-act). FAULT-FORM-NON-ACTION-VERB.
        (2) "on the station surface" — PP of place. FAULT-FORM-MODIFIER.
      why: >
        Thesis-image bone for the two-substrates close. Both violations must be cleared
        for Phase 6 to pass. A stative verb on a grounding bone that is part of the
        thesis-image sequence is particularly load-bearing: if the bone is malformed,
        the sensory/location-state facets citing it inherit a non-event anchor.
      criteria: >
        Recast to transitive SVO with no stative verb and no PP of place.
        The station surface location must be absorbed into a compound-noun direct object
        or dropped if contextually established by s03n01 ("takes the feed-station").
        Minimum-change recast: "the ward-coverage notes cover the station-left"
        (compounding the spatial information into the object) OR "the ward-coverage
        notes anchor the station surface" (if the surface is used as direct object of
        a transitive act). Fixer determines minimum-change form that satisfies
        FAULT-FORM discipline. Preserve thesis-image function: the notes as a physical
        object with a defined location on the surface, distinct from the sealed packet.

    - id: fault-012
      type: fault
      scope: bone
      target: b01c09s03n05
      class: FAULT-FORM (NON-ACTION-VERB + INTERIORITY)
      what: >
        s03n05 SVO: "the internal map holds wren's route."
        Two violations:
        (1) "holds wren's route" — narrow holds-license violation.
        Schema: "holds is licensed only when (1) object is a body part of the subject
        and action is stillness-against-pressure, or (2) the object is a physical object
        resisting pressure. Anything else faults FAULT-FORM-NON-ACTION-VERB."
        "Wren's route" is an abstraction (a pattern/circuit), not a body part or
        physical object resisting pressure.
        (2) "Abstraction-as-object is INTERIORITY. A physical verb whose object is an
        abstract noun is a thought-figure, not an event. Faults FAULT-FORM-INTERIORITY."
        "Wren's route" is an abstract entity (a daily movement pattern).
      why: >
        This is a SW-1 compliance bone: the internal map holding the pattern is the
        chapter's load-bearing structural fact separating the two substrates. A
        malformed SVO on this bone undermines the thesis-image's physical grounding.
        The holds-abstraction form is exactly the class the b01c07 bone-gate flagged
        and resolved ("holds the silence" → FAULT at b01c07; resolved to "exhales").
      criteria: >
        Recast to transitive SVO with a concrete physical-act verb and an object that
        is either a concrete noun or a compound-noun, not an abstraction.
        The internal map as subject is correct; the act of containing/filing the route
        must be a concrete write-act.
        Minimum-change recast: "the internal map files wren's route"
        (c02 precedent: "the insects file the ward-junction contact") — transitive,
        the route is the concrete thing filed, no holds-abstraction. Preserve
        event-map coverage of [force: wren-pattern-in-internal-map-not-deliverable].

    - id: fault-013
      type: fault
      scope: bone
      target: b01c09s03n06
      class: FAULT-FORM (NON-ACTION-VERB + INTERIORITY)
      what: >
        s03n06 SVO: "the feed-record holds the courier observation."
        Two violations identical in class to fault-012:
        (1) "holds the courier observation" — narrow holds-license violation.
        "Courier observation" is an abstraction (a logged data entry), not a body part
        or physical object resisting pressure. FAULT-FORM-NON-ACTION-VERB.
        (2) "Courier observation" as abstraction-object. FAULT-FORM-INTERIORITY.
      why: >
        This is the SW-2 compliance bone: the feed-record holding the observation
        (not the Jarvis channel) is the structural fact enacting the substrate split.
        Same consequence as fault-012: a malformed SVO here undermines the thesis-image
        and the event-map coverage of [force: courier-observation-in-internal-map-not-
        deliverable] and [image: two-substrates-one-station-surface].
      criteria: >
        Recast to transitive SVO with concrete act and non-abstraction direct object.
        Minimum-change recast: "the feed-record closes the courier entry"
        (c02 parallel: "the ledger closes the dark-junction entry"; "the accounting
        closes the fever-cluster entry") — transitive, concrete filing-close act,
        the courier entry is a record object, not an abstraction. Preserve event-map
        coverage of both [force: courier-observation-in-internal-map-not-deliverable]
        and [image: two-substrates-one-station-surface].

    - id: fault-014
      type: fault
      scope: bone
      target: b01c09s03n07
      class: FAULT-FORM-MODIFIER
      what: >
        s03n07 SVO: "the seal dries on the packet."
        "on the packet" is a prepositional phrase of place.
        Schema: PP of place explicitly banned (FAULT-FORM-MODIFIER).
        "the seal dries" as a bare intransitive is licensed (the intransitive-lands-
        cleanly exception: "taylor exhales" passes; the seal drying is an observable
        physical process). The PP adjunct is the sole violation.
      why: >
        The thesis-image close bone. The PP is redundant padding — the packet is
        established as the subject's substrate by context (n02/n03). Dropping it
        yields a clean intransitive. Small fix, high-priority as closing image.
      criteria: >
        Drop the PP adjunct. Minimum-change recast: "the seal dries"
        — bare intransitive, clean, licensed by the intransitive-lands-cleanly
        exception. Preserve the bone's event-map function as the closing sensory
        anchor for [mechanism: accounting-closes-with-split-substrate-intact] and
        [image: two-substrates-one-station-surface].

    # ── FLAG ──────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      scope: bone
      target: b01c09s02n07
      class: PERCEPTION-VERB-ADJACENT
      what: >
        s02n07 verb "logs" is perception-data-recording adjacent. The schema deny-list
        names: "read, took, tracked, noted, counted, measured, watches, sees, hears,
        notices" as FAULT-FORM-PERCEPTION. "logs" is not on the explicit list and is
        classified as a physical write-act (an observer could see Taylor writing in a
        record). However, it occupies the same semantic register as "noted" (which is
        banned) and may attract a PERCEPTION challenge at Phase 6 review.
        Primary finding for this bone is fault-009 (PP of place); this flag is advisory
        on the verb.
      why: >
        If the recast required by fault-009 replaces "logs" with a c02-register verb
        (e.g. "closes the observation-entry"), the perception-verb-adjacent risk is
        resolved automatically. Flag is informational only; no separate fixer action
        required if fault-009 recast adopts a c02-class verb.
      criteria: null

    # ── PASS ANNOTATIONS ──────────────────────────────────────────────────────

    # s01n01: CLEAN — "enters the lane-south-of-the-hook": transitive, compound-noun
    #   direct object, no PP, no modifier. C02 register ("leaves the drain angle").
    # s01n02: CLEAN — "the insect-feed threads the stitch-shop lane": transitive, no PP.
    # s01n03: CLEAN — "the stitch-shop door opens the lane-mouth": transitive, no PP.
    # s01n07: CLEAN — "the ward-coverage notes receive the boundary geometry": transitive.
    # s02n01: CLEAN — "enters the dragonpit-margin lane": transitive, no PP.
    # s02n03: CLEAN — "the stone-post marks the lower gate side-exit": transitive,
    #   compound-noun object. C02 parallel (line 17: "the coverage map anchors the
    #   stitch-house threshold").
    # s02n08: CLEAN — "taylor-hebert-kl-122ac completes the circuit": transitive.
    # s03n01: CLEAN — "taylor-hebert-kl-122ac takes the feed-station": C02 canonical
    #   form ("takes the drain angle").
    # s03n02: CLEAN — "taylor-hebert-kl-122ac folds the packet": transitive, concrete.

  fixer_summary:
    total_faults: 14   # 12 FAULT-FORM + 2 FAULT-BONE-DELTA-MALFORMED
    bones_requiring_recast:
      - b01c09s01n05   # fault-002: PP of place ("at the bread-seller corner")
      - b01c09s01n06   # fault-003: PP of place/instrument ("in the internal map")
      - b01c09s02n02   # fault-004: stative verb + PP of place
      - b01c09s02n04   # fault-005: PP of direction ("toward the second man")
      - b01c09s02n05   # fault-006: holds-abstraction + PP of place
      - b01c09s02n06   # fault-007: PP of place ("in the feed-record"); also fault-008
      - b01c09s02n07   # fault-009: PP of place ("in the feed-record")
      - b01c09s03n03   # fault-010: adverb + PP of place (CENTRAL EVENT bone — HIGH PRIORITY)
      - b01c09s03n04   # fault-011: stative verb + PP of place
      - b01c09s03n05   # fault-012: holds-abstraction + interiority
      - b01c09s03n06   # fault-013: holds-abstraction + interiority
      - b01c09s03n07   # fault-014: PP of place (bare "the seal dries" is the recast)
    bones_requiring_showrunner_judgment:
      - b01c09s01n04   # fault-001: bone Δ magnitude 0.5 < bone floor 1.0; chapter target conflict
      - b01c09s02n06   # fault-008: bone Δ magnitude 0.5 < bone floor 1.0; chapter target conflict
    bones_clean: 9
      # s01n01, s01n02, s01n03, s01n07, s02n01, s02n03, s02n08, s03n01, s03n02

  minimum_change_recasts:
    # For fixer reference. Fixer determines exact form; these are minimum-change guidance.
    b01c09s01n05: "wren-stitch-maker-flea-bottom-ward reaches the bread-seller corner"
    b01c09s01n06: "taylor-hebert-kl-122ac files wren's route"
    b01c09s02n02: "the supply cart marks the lower-gate road"
    b01c09s02n04: "corwick faces the second man"
    b01c09s02n05: "[fixer to determine: concrete body-act verb, body-part or physical-object direct object, no PP; e.g. 'corwick squares the shoulders' or 'corwick braces the stone-post']"
    b01c09s02n06: "taylor-hebert-kl-122ac files the posture-class"
    b01c09s02n07: "taylor-hebert-kl-122ac closes the observation-entry"
    b01c09s03n03: "taylor-hebert-kl-122ac seals the packet"
    b01c09s03n04: "[fixer to determine: transitive verb, no stative, no PP; e.g. 'the ward-coverage notes cover the station-left' or 'the ward-coverage notes anchor the station surface']"
    b01c09s03n05: "the internal map files wren's route"
    b01c09s03n06: "the feed-record closes the courier entry"
    b01c09s03n07: "the seal dries"
