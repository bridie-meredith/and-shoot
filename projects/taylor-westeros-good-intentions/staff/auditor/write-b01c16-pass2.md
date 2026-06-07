```yaml
audit:
  scope: chapter
  target: b01c16
  timestamp: 2026-06-04
  pass: 2 — SVO constraint audit (SVO form + cond-card + physical-possibility)
  findings:

    # ── s01 ──────────────────────────────────────────────────────────────────

    - id: fault-001
      type: pass
      what: s01n01 — "the storehouse eaves shadow the clearing-ground"
      why: Ambient-environment subject; "shadow" is a concrete observable (cast shadow is physical light-occlusion). Not a perception verb. No modifier. Clean SVO.

    - id: fault-002
      type: fault
      what: s01n02 — "the reed-mat leans the storehouse wall"
      why: >
        "Leans" used as a stative position-naming verb describing the mat's resting
        orientation against the wall. The schema deny-list includes stative
        position-naming verbs ("lies/sits/stands describing position not posture-act");
        "leans" is structurally identical — the mat is not performing a discrete act
        of leaning, it is already positioned leaning. No discrete initiation or
        termination event is encoded. Downstream: the stitcher renders a positional
        state as if it were an action, producing false dynamism or ambiguity.
      criteria: >
        The bone must encode either the discrete event that caused the mat's
        position (e.g., the mat was placed against the wall — a placement act by
        an actor, or the mat falling into position), or the state must be routed
        to a location-state or state-update facet entry that cites a real action
        bone. The revised bone must not use a stative position verb.

    - id: fault-003
      type: fault
      what: s01n03 — "the two crates stack the kneeling-bench position"
      why: >
        "Two" is a pre-nominal quantifying modifier (numeral adjective). The schema
        bans all modifiers — "No adjectives, no adverbs, no prepositional padding."
        There is no explicit exception for quantifiers or numerals; the subject rule
        is "the <noun>" for unnamed environment elements, not "the <adjective> <noun>."
        Additionally, "the kneeling-bench position" is a compound noun encoding
        a spatial relationship (position relative to the kneeling bench) rather than
        a named prop or named sub-zone. "Stack" as a transitive verb with a location
        as object is borderline — stacking implies vertical accumulation onto a surface,
        which could be read as a stative result-state rather than a discrete act.
        Primary fault: modifier on subject. Secondary concern: location-as-object may
        encode direction/placement in a way that blurs with "stack the bench" (placing)
        vs. "are stacked at the bench position" (stative). Downstream: the "two"
        modifier creates a precedent for descriptive adjective use in subjects; the
        ambiguous stacking-vs-placement verb creates stitcher ambiguity about whether
        this is an action beat or a set-dressing note.
      criteria: >
        The subject must be a bare named element without numerical modifier (e.g.,
        "the crate-stack" or "the crates" if pair-identity is established from
        context). If distinguishing two individual crates is narratively necessary,
        they must appear as separate bones or as a named unit. The verb must be
        either a discrete action ("the crate-stack rests the bench" fails for the
        same stative reason — recast to a placement action by an actor, or route
        the set-state to a location-state facet entry).

    - id: fault-004
      type: pass
      what: s01n04 — "the old man straightens the back"
      why: Discrete physical act (rising from bent posture). "Straightens" is a concrete observable posture-change, not stative. Clean SVO.

    - id: fault-005
      type: fault
      what: s01n05 — "the child leans the woman's side"
      why: >
        "Leans" is the same stative position-naming fault as s01n02. The child's
        leaning against the woman is a positional state, not a discrete act of
        leaning. There is no initiation event encoded — the child is already
        positioned this way. Downstream: identical to s01n02 — stitcher treats a
        positional state as an action beat, producing false dynamism or confusion
        about whether the child is moving or is already settled.
      criteria: >
        The bone must encode the discrete act that establishes the positional
        relationship (the child moving to lean against the woman, or the child
        placing the weight on the woman's side), or the state must be routed
        to a location-state / state-update facet entry citing the bone that
        represents the prior positioning action. The revised bone must not use
        a stative position verb.

    - id: fault-006
      type: pass
      what: s01n06 — "septon-halvard-flea-bottom lifts the head"
      why: Discrete physical act (raising the head). Clean SVO.

    - id: fault-007
      type: pass
      what: s01n07 — "taylor-hebert-kl-122ac enters the clearing-diagonal"
      why: >
        "Enters" is a clean transitive motion verb; "the clearing-diagonal" functions
        as a named sub-zone compound (naming the diagonal approach path into the
        clearing) rather than as a prepositional phrase of direction. The form is
        "enters [direct object named zone]" not "enters [into/across] [destination]."
        The schema bans "walks into the yard" but permits "enters the yard." This
        bone follows the permitted transitive form.

    - id: fault-008
      type: pass
      what: s01n08 — "the storehouse-eaves flies return the clearing-bodies"
      why: >
        Ambient-actor subject (flies); "return" as a motion verb with a destination
        object ("the clearing-bodies" = the bodies in the clearing) is a concrete
        observable movement. Not a Taylor perception verb — the subject is the flies
        themselves performing the action. No modifier. Clean SVO.

    # ── s02 ──────────────────────────────────────────────────────────────────

    - id: fault-009
      type: pass
      what: s02n01 — "septon-halvard-flea-bottom matches the pace"
      why: Discrete concrete act (adjusting gait to match Taylor's). "Matches" is observable behavior. Clean SVO.

    - id: fault-010
      type: pass
      what: s02n02 — "septon-halvard-flea-bottom speaks to taylor-hebert-kl-122ac"
      why: Canonical speech form. Correctly uses "speaks to <listener-slug>." Dialogue-anchor form is licensed.

    - id: fault-011
      type: fault
      what: s02n03 — "the rendering-yard fence crosses the clearing-margin"
      why: >
        "The rendering-yard fence" is a static physical structure; it cannot perform
        the action of crossing anything. "Crosses the clearing-margin" describes
        where the fence is located (it is positioned so that it intersects the
        clearing's margin), not a discrete act the fence performs. This is a stative
        existence/location statement disguised as an action verb — structurally
        equivalent to the banned copula form ("the fence is at the clearing-margin")
        with the copula replaced by a spurious action verb. Faults FAULT-FORM-COPULA
        (or equivalently FAULT-FORM-NON-ACTION-VERB: a non-action verb whose primary
        semantic is positional existence rather than doing).
        Downstream: the stitcher cannot render this as a discrete event — it is
        set-dressing that belongs in a location-state facet entry, not a bone.
      criteria: >
        The positional relationship between the fence and the clearing margin is
        set-dressing, not a bone-level event. Either (a) route the fence's position
        to a location-state facet entry citing a real action bone at this scene
        position, or (b) if a bone is genuinely needed for the spatial information,
        recast as a discrete action by a named actor that involves the fence
        (e.g., an actor reaching/touching the fence establishes its presence as a
        physical encounter without requiring the fence to "act").

    - id: fault-012
      type: pass
      what: s02n04 — "taylor-hebert-kl-122ac presses the fence-rail"
      why: Discrete physical act (applying pressure to the rail). Clean SVO.

    - id: fault-013
      type: pass
      what: s02n05 — "septon-halvard-flea-bottom stops the pace"
      why: Discrete physical act (halting movement). Clean SVO.

    - id: fault-014
      type: pass
      what: s02n06 — "septon-halvard-flea-bottom faces taylor-hebert-kl-122ac"
      why: >
        "Faces" as a discrete posture-orientation act (turning to face someone) is
        licensed as a concrete observable. This is not the banned "turns to <X>"
        form — the schema bans "turns to" as a directional-prep variant but explicitly
        says "faces <X>" is the correct recast. Clean SVO.

    - id: fault-015
      type: fault
      what: s02n07 — "taylor-hebert-kl-122ac holds the fence-rail"
      why: >
        "Holds" fails the schema's narrow license test. The license permits "holds"
        only when (1) object is a body part of the subject and the action is
        stillness-against-pressure, or (2) the object is a physical thing resisting
        pressure (e.g., "the door holds"). "The fence-rail" is neither — it is a
        physical object the subject is gripping in a sustained state, which falls
        under the general deny-list for "holds" as sustained carrying/gripping.
        Downstream: sustained gripping is a positional state; the stitcher receives
        a state-bone rather than an event-bone, confusing the rhythm of action beats.
      criteria: >
        The bone must encode the discrete act of gripping or grasping the fence-rail
        (the initiation event) rather than the sustained state of holding it. A verb
        encoding the grip-taking action (e.g., "grips," "grasps," "seizes," "takes")
        is required. Alternatively, if the sustained grip was established in a prior
        bone, this bone should be removed and the state routed to a state-update
        or location-state facet entry.

    - id: fault-016
      type: fault
      what: s02n08 — "the gout-swollen foot rests the clearing-edge"
      why: >
        Two independent faults:
        (1) FAULT-FORM-MODIFIER: "gout-swollen" is a hyphenated adjectival compound
        modifying "foot." Unlike compound-nouns that name a location or object by
        function ("rendering-yard," "kneeling-bench"), "gout-swollen" encodes a
        physical property/condition of the noun. The schema bans all adjectives in
        bones subjects; "gout-swollen" is an adjective regardless of its hyphenation.
        (2) FAULT-FORM-NON-ACTION-VERB: "rests" is a stative position verb. The foot
        resting at the clearing edge is a positional state (the foot is positioned
        there, at rest), not a discrete observable act of placing or lowering.
        Downstream: the modifier breach sets a precedent for descriptive adjectives
        in subjects; the stative verb produces a state-bone rather than an event-bone.
      criteria: >
        Both faults must be resolved independently.
        For the modifier: the subject must be a bare noun without adjectival modifier
        ("the foot" or a named prop slug if the foot is a named prop). If the
        gout-condition is narratively load-bearing at this beat, it belongs in a
        sensory or state facet entry citing this bone, not in the bone subject itself.
        For the stative verb: the bone must encode a discrete act (Halvard placing
        weight on his foot, or lowering into a resting position — the initiation event)
        rather than the resulting state of the foot being at rest. Alternatively,
        if this is pure set-dressing, route to location-state facet and remove the bone.

    - id: fault-017
      type: pass
      what: s02n09 — "septon-halvard-flea-bottom speaks to taylor-hebert-kl-122ac"
      why: Canonical speech form. Correctly uses "speaks to <listener-slug>." Dialogue-anchor form is licensed.

    - id: fault-018
      type: pass
      what: s02n10 — "taylor-hebert-kl-122ac releases the fence-rail"
      why: >
        "Releases" is the discrete act of letting go — the termination of a grip state.
        It is a concrete observable physical action (the hand opens and the rail is
        freed). This is the licensed counterpart to the sustained-hold that was faulted
        at s02n07; this bone correctly encodes the termination event. Clean SVO.

    # ── s03 ──────────────────────────────────────────────────────────────────

    - id: fault-019
      type: fault
      what: s03n01 — "taylor-hebert-kl-122ac stops the forward-step"
      why: >
        "The forward-step" is an abstract motion concept, not a physical object.
        The schema rule: "Abstraction-as-object is INTERIORITY. A physical verb whose
        object is an abstract noun [...] is a thought-figure, not an event."
        "The forward-step" names a motion intention/trajectory rather than a physical
        thing Taylor can physically stop. The physical event is simply Taylor halting;
        the object "the forward-step" imports an interiority frame (the step she was
        about to take). FAULT-FORM-INTERIORITY (abstract object).
        Note: "taylor-hebert-kl-122ac stops" as a bare intransitive is licit — "stops"
        is not a motion verb requiring a destination object; it is the cessation of
        motion (analogous to "exhales"), so the intransitive form clears the
        FAULT-FORM-NO-VERB bar.
        Downstream: the stitcher receives an interiority signal embedded in the bone
        object, which belongs in a narrator-interest facet entry.
      criteria: >
        Remove the abstract object. The bone must be the bare intransitive
        "taylor-hebert-kl-122ac stops" (or equivalent concrete action without abstract
        object). If the narrative needs to convey that Taylor was mid-stride and
        interrupted herself, that information belongs in a narrator-interest facet
        entry citing this bone.

    - id: fault-020
      type: fault
      what: s03n02 — "the storehouse-eaves flies return halvard's stillness"
      why: >
        "Halvard's stillness" is an abstract noun (a state-of-being, not a physical
        object). The schema rule: "Abstraction-as-object is INTERIORITY." The flies
        cannot physically return a stillness — "halvard's stillness" is a
        thought-figure encoding Taylor's (or the narrative's) perception of Halvard's
        state, not a physical event performed by the flies. FAULT-FORM-INTERIORITY.
        If the intent is that the flies have repositioned to hover around Halvard in
        his stillness (registering his body-position), the bone must name the concrete
        physical destination (Halvard's body / position) rather than an abstraction
        derived from his state.
        Downstream: the abstract object corrupts the bone as a physical-event anchor;
        facets citing this bone receive a misleading event signal.
      criteria: >
        The object must be a concrete physical target — a named entity (the actor slug)
        or a named physical location/zone (e.g., "halvard's position," but that itself
        borders on abstraction — prefer "halvard" as direct object if the flies are
        returning to hover around his body). The bone must describe a physical
        observable action by the flies on or toward a concrete physical object.

    - id: fault-021
      type: pass
      what: s03n03 — "taylor-hebert-kl-122ac turns the clearing"
      why: >
        "Turns the clearing" with the clearing as a direct object (Taylor pivoting
        within or toward the clearing, "turning" the corner/space) is not the
        explicitly banned "turns to <named entity>" prepositional form. It reads as
        a transitive: Taylor executes a turn that takes her into/through the clearing.
        Borderline but does not match any named fault class precisely enough to hard-fault.
        Flagged as marginal form — "turns the clearing" is unusual idiom and a writer
        asked to clarify might say "enters the clearing from a new angle," but the bone
        does not violate a named schema rule as written.

    - id: fault-022
      type: pass
      what: s03n04 — "taylor-hebert-kl-122ac walks the rendering-yard approach"
      why: >
        "Walks" used transitively with a path as direct object ("walks the road,"
        "walks the approach") is a standard transitive construction encoding traversal.
        The schema example of the banned form is "walks into the yard" (prepositional
        phrase); "walks the approach" uses the path as direct object without a
        prepositional phrase. Clean SVO.

    - id: fault-023
      type: fault
      what: s03n05 — "the reed-mat stands the wall"
      why: >
        Identical class of fault to s01n02. "Stands" is explicitly on the schema's
        stative deny-list: "stative position-naming: lies, sits, stands describing
        position not posture-act." The reed mat cannot perform the discrete act of
        standing — it is an inanimate prop. "Stands the wall" means "is positioned
        standing against the wall," which is a positional state, not a discrete event.
        FAULT-FORM-NON-ACTION-VERB.
        Downstream: stitcher receives a state-bone without an initiating event,
        producing an orphaned location-state note that belongs in a facet entry.
      criteria: >
        Route the mat's positional state to a location-state facet entry citing the
        appropriate scene-position anchor bone. If a bone is genuinely needed (e.g.,
        Taylor or another actor physically places or notices the mat), recast as a
        discrete actor-driven action. The mat itself cannot be the subject of a
        non-ambient action without an external force acting on it.

    - id: fault-024
      type: fault
      what: s03n06 — "the old man holds the clearing-edge"
      why: >
        "Holds the clearing-edge" fails the narrow holds license. The two licensed uses
        are (1) body part of subject held still against pressure, or (2) physical
        object resisting pressure. "The clearing-edge" is a spatial zone, not a body
        part of the old man or a physical object the old man can grip in the
        pressure-resistance sense. "The old man holds the clearing-edge" means the
        old man remains stationed at the clearing's edge — a stative presence, not
        a discrete act. FAULT-FORM-NON-ACTION-VERB.
        Downstream: stitcher receives a positional-state bone rather than an event-bone;
        the old man's presence at the clearing edge is set-dressing that belongs in
        a location-state facet or was established by a prior action bone.
      criteria: >
        The old man's presence at the clearing edge must be encoded as either (a) the
        discrete act by which he arrived or stationed himself there (a prior bone) with
        his position carried in a location-state facet entry, or (b) if a beat-marker
        is needed at this scene position, a concrete observable physical action the
        old man performs while at the clearing edge (not a stative verb).

    - id: fault-025
      type: pass
      what: s03n07 — "taylor-hebert-kl-122ac reaches the rendering-yard fence"
      why: >
        "Reaches" as a motion verb meaning "arrives at" is a concrete observable
        (Taylor's body arrives at the fence's physical location). Clean transitive
        SVO. No modifier, no abstraction, no copula.

    - id: fault-026
      type: fault
      what: s03n08 — "the angle-line moves halvard past the eaves-edge"
      why: >
        "Past the eaves-edge" is a prepositional phrase of direction/place. The
        schema explicitly bans "prepositional phrases of place / destination / source
        / direction / instrument / accompaniment" — FAULT-FORM-MODIFIER.
        Secondary concern: "the angle-line" as subject designates a geometric abstraction
        (a line defined by an angle), not a named physical entity (actor slug, prop
        slug, or "the <noun>" for a named environment element). A geometric/architectural
        line is not a physical actor that can move another actor. This is closer to
        a thought-figure or a staging description than a bone-level observable event.
        If the intent is that Halvard moves along an angular path relative to the eaves,
        the subject must be Halvard (the actor performing the action) with the path
        as the direct object, not a geometric abstraction as agent.
        Primary fault: FAULT-FORM-MODIFIER (prepositional phrase as object).
        Secondary fault: subject is a geometric abstraction, not a named entity.
        Downstream: the prepositional phrase encodes directional movement that must
        be part of the verb+object pair; the abstract subject makes this bone
        unrenderable as a physical event by the stitcher.
      criteria: >
        Both faults must be resolved. The subject must be a named physical entity
        (the actor performing the movement — septon-halvard-flea-bottom, if he is
        the one moving). The directional information ("past the eaves-edge") must
        be encoded as a transitive verb+destination-as-direct-object construction
        without a prepositional phrase (e.g., "passes the eaves-edge" with the eaves-
        edge as direct object), or the movement must be split into a discrete positional
        transition bone using a destination-naming transitive form.

    - id: fault-027
      type: pass
      what: s03n09 — "taylor-hebert-kl-122ac runs the next circuit-segment"
      why: >
        "Runs" used transitively with a path/zone as direct object is structurally
        identical to "walks the approach" (s03n04). "The next circuit-segment" names
        a physical route, not an abstraction. Clean SVO.

    # ── Constraint / physical-possibility scan ──────────────────────────────

    - id: fault-028
      type: pass
      what: Full chapter — cond-taylor-pov-behavior
      why: >
        No bones use perception verbs for Taylor. Bones using ambient-actor subjects
        (flies, eaves, fence) are correctly constructed with those elements as subjects,
        not as objects of Taylor's perception. No first-person pronoun intrusion in
        bone form (expected at bones layer per card's pipeline-convention note).
        No theme-narration in bone content. Pass.

    - id: fault-029
      type: pass
      what: Full chapter — cond-earth-bet-noun-fence
      why: >
        No bones contain Earth-Bet proper nouns (no shard terminology, no cape names,
        no institutional vocabulary, no Earth-Bet geography). Pass.

    - id: fault-030
      type: pass
      what: Full chapter — cond-override-architecture-residue-122ac
      why: >
        "The storehouse-eaves flies return the clearing-bodies" (s01n08) and
        "the storehouse-eaves flies return halvard's stillness" (s03n02) use flies
        as ambient actors consistent with Taylor's passive insect-network in KL Flea
        Bottom. No bone implies range beyond 200m. No bone implies Khepri-mantle
        capability (no human-body coordination). No bone describes the passive
        awareness as quiet or without suppression cost. s03n02 is faulted on
        SVO form grounds (abstract object) but not on power-mechanics grounds.
        Pass on constraint axis.

    - id: fault-031
      type: pass
      what: Full chapter — cond-kl-geography-122ac
      why: >
        Scene is set at the sept corner (oc-sept-corner), which the location card
        places in the Hook, within Flea Bottom. No bone places Flea Bottom on the
        wrong side of the city. No invented gates or landmarks. The rendering-yard
        fence and clearing are consistent with the Hook's mixed-industrial geography.
        Pass.

    - id: fault-032
      type: pass
      what: Full chapter — cond-westerosi-witness-vocabulary
      why: >
        No dialogue bones in this chapter use Taylor's parahuman vocabulary. The two
        speech bones (s02n02, s02n09) are Halvard speaking to Taylor — no vocabulary
        constraint on Halvard's speech that is checkable at bone level (content
        is in dialogue files, not bones). No constraint violation detectable at
        bone-form level. Pass.

    - id: fault-033
      type: pass
      what: Full chapter — physical-possibility / actor-on-set check
      why: >
        Cast on set (taylor-hebert-kl-122ac, septon-halvard-flea-bottom, unnamed old
        man, unnamed woman + child) matches all actors appearing in the bones.
        No actor appears in a location they have not moved to within the scene sequence.
        No prop is used that is not established in the location card's fixed props
        or in the scene's set-state. The fence-rail referenced in s02n04/07/10 is
        consistent with the rendering-yard fence established in s02n03. The reed-mat
        (s01n02, s03n05) and two crates (s01n03) are set-dressing items consistent
        with the sept-corner location card's description of the storehouse and its
        surrounds. The kneeling-bench (s01n03) is consistent with the sept bay
        described in oc-sept-corner. Pass.
```
