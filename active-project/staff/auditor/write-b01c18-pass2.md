audit:
  scope: chapter
  target: b01c18
  timestamp: 2026-06-05
  pass: 2 — SVO-form constraint audit (bones draft)
  source: active-project/staff/screen-writer/b01c18-bones-draft.md

  summary:
    total_bones: 46
    fault_count: 37
    fault_by_class:
      FAULT-FORM-PERCEPTION: 6
      FAULT-FORM-MODIFIER: 24
      FAULT-FORM-NON-ACTION-VERB: 7
      FAULT-FORM-NEGATION: 1
      FAULT-FORM-CONJUNCTION: 1
      FAULT-AGGREGATE-DELTA-MISMATCH: 0
      FAULT-COST-LEDGER-UNRESOLVED: 0
      FAULT-CONSTRAINT: 0
      FAULT-PHYSICAL: 0
    clean_bones: [b01c18s01n01, b01c18s01n05, b01c18s02n02-partial-see-fault-009, b01c18s04n02, b01c18s05n03, b01c18s05n04, b01c18s05n06, b01c18s05n08, b01c18s05n09]
    note: >
      Several bones carry multiple simultaneous violations. Each violation is listed
      separately with its own fault-id. Recast suggestions are minimal-change: preserve
      the bone's substance_delta, event-coverage role, and ambient-actor register.

  findings:

    # ─── SCENE s01 ──────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      bone: b01c18s01n02
      svo_offending: "taylor-hebert-kl-122ac reads the margin-cipher addendum"
      offending_span: "reads"
      what: >
        `reads` is on the schema's explicit FAULT-FORM-PERCEPTION deny-list
        (bones.schema.md line 97: "read … are POV-leaks; they describe internal
        observation, not external action").
      why: >
        Perception verbs route to narrator-interest / sensory facets. A bone with
        `reads` as its verb is not an observable physical act; it is interiority
        rendered as action. The bone cannot anchor dialogue or sensory facets
        correctly if its verb is itself the observation.
      criteria: >
        The verb must be a concrete physical act an external observer would see.
        The substance_delta (all-held: moral_framework, political_register-prot)
        and event-coverage role (reads margin-cipher addendum) must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac lifts the margin-cipher addendum"

    - id: fault-002
      type: fault
      bone: b01c18s01n03
      svo_offending: "the cipher addendum names the succession-mechanism window"
      offending_span: "names"
      what: >
        `names` is a declarative/semantic verb: a document "naming" a thing is an
        interior-legibility event, not an observable physical act. Faults
        FAULT-FORM-PERCEPTION (perception-surrogate category) or
        FAULT-FORM-INTERIORITY. The addendum does not perform a visible physical
        action; it communicates content to a reader — an internal event.
      why: >
        The bone's event-coverage role is "request-scope-named" — the scope content
        of the addendum becoming known. That event belongs in narrator-interest /
        sensory facets, not in the bone itself. A bone whose verb is `names` cannot
        be the physical anchor for downstream facets because there is no observable
        external act.
      criteria: >
        The verb must be a concrete physical act. The substance_delta (all-held:
        position-world, political_register-world) and event-coverage role
        (succession-mechanism window disclosed) must be preserved. Acceptable
        recasts use an ambient-actor physical form (the addendum as object-as-subject
        performing a discrete physical act).
      recast_suggestion: "the cipher addendum opens the succession-mechanism column"

    - id: fault-003
      type: fault
      bone: b01c18s01n04
      svo_offending: "taylor-hebert-kl-122ac reads the addendum a second time"
      offending_span: "reads"
      what: >
        Same FAULT-FORM-PERCEPTION violation as fault-001. `reads` is explicitly
        banned. Additionally, `a second time` is a time-modifier adverb phrase
        (FAULT-FORM-MODIFIER), compounding the violation.
      why: >
        The bone's event-coverage role is "protagonist-reads-to-end" — the
        precipice-behavior of Taylor holding the weight of the ask. This narrative
        function is load-bearing for the moral_framework axes_held rationale. A
        perception verb cannot carry this role cleanly.
      criteria: >
        The verb must be a concrete physical act. The `a second time` modifier must
        be removed — repetition can be implied by the verb choice or the object.
        The substance_delta (all-held: moral_framework, relational_anchor_status)
        must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac returns the addendum to the first column"

    - id: fault-004
      type: fault
      bone: b01c18s01n07
      svo_offending: "taylor-hebert-kl-122ac names the count"
      offending_span: "names"
      what: >
        `names` as an interior act: Taylor internally naming a count is interiority
        rendered as action (FAULT-FORM-PERCEPTION / FAULT-FORM-INTERIORITY). There
        is no dialogue_anchor flag and no dialogue file, confirming this is interior
        naming, not a spoken act.
      why: >
        The bone's event-coverage role is "scope-recognized-not-yet-executed" and the
        axes_held rationale describes "naming enacts stillness-against-pressure" —
        this is the precipice close of s01. A physical action must enact that
        stillness, not an interior declarative.
      criteria: >
        The verb must be a concrete physical act enacting stillness-against-pressure
        (the schema licenses `holds the feet` / `holds the eyes` for this pattern).
        The substance_delta (all-held: moral_framework, moral_legibility_to_self)
        and the precipice-close function must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac holds the feet"

    # ─── SCENE s02 ──────────────────────────────────────────────────────────────

    - id: fault-005
      type: fault
      bone: b01c18s02n01
      svo_offending: "taylor-hebert-kl-122ac opens the bottlefly routes under the Fishmonger Gate"
      offending_span: "under the Fishmonger Gate"
      what: >
        `under the Fishmonger Gate` is a prepositional phrase of place (PP-place),
        explicitly banned by bones.schema.md line 107: "Prepositional phrases of
        place / destination / source / direction / instrument / accompaniment are
        explicitly banned (FAULT-FORM-MODIFIER)."
      why: >
        The location belongs in citations to location-state facets, not in the bone.
        The grounding: true flag confirms this bone is a spatial anchor — the
        location detail should migrate to a loc-state entry and cite this bone.
      criteria: >
        The PP must be removed. The verb `opens` and the object `the bottlefly routes`
        are clean. The substance_delta (all-held: capability, moral_framework) and
        grounding role must be preserved. The Fishmonger Gate location is handled
        by a co-emitted loc-state entry.
      recast_suggestion: "taylor-hebert-kl-122ac opens the bottlefly routes"

    - id: fault-006
      type: fault
      bone: b01c18s02n02
      svo_offending: "taylor-hebert-kl-122ac opens the moth-corridor through the chandler quarter"
      offending_span: "through the chandler quarter"
      what: >
        `through the chandler quarter` is a prepositional phrase of direction/place.
        FAULT-FORM-MODIFIER per bones.schema.md line 107.
      why: >
        Same as fault-005. The direction-PP pads the object; location detail belongs
        in loc-state citation. The bone's axes_held rationale does not depend on the
        PP being in the SVO.
      criteria: >
        The PP must be removed. The substance_delta (all-held: capability,
        social_tether-prot-rise) and event-coverage role (second channel activated)
        must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac opens the moth-corridor"

    - id: fault-007
      type: fault
      bone: b01c18s02n03
      svo_offending: "the feed-lines activate across the Gate of the Gods and the Iron Gate and the River Gate"
      offending_span: "across the Gate of the Gods and the Iron Gate and the River Gate"
      what: >
        Two simultaneous violations:
        (1) `across …` is a PP of place/direction — FAULT-FORM-MODIFIER.
        (2) `and the Iron Gate and the River Gate` chains two conjunctions — the
        schema bans `and` as a conjunction (FAULT-FORM-CONJUNCTION; bones.schema.md
        line 110: "No and, but, while, as. If two things happen, they are two bones").
      why: >
        The PP and conjunction stack make this bone compound-event: three gates
        activating. If the event is the simultaneous three-gate activation as a
        unified structural fact (the outer-ring corridors reaching full coverage),
        the conjunction must be removed and replaced with a comma-list object or a
        collective object noun. The PP must be removed.
      criteria: >
        The conjunction `and…and` must be eliminated. The PP `across …` must be
        removed. If the three-gate object is meaningful as a set, use a comma-list
        without `and`, or collapse to a collective object. The substance_delta
        (all-held: capability, position-prot-collapse) and event-coverage role
        (outer-ring corridors activated) must be preserved.
      recast_suggestion: "the feed-lines activate the outer-gate corridors"
      alternate_recast: "the feed-lines activate the Gate of the Gods, the Iron Gate, the River Gate"

    - id: fault-008
      type: fault
      bone: b01c18s02n04
      svo_offending: "taylor-hebert-kl-122ac holds the east-of-water-gate lanes blank"
      offending_span: "holds … blank"
      what: >
        Two simultaneous violations:
        (1) `holds` with object `east-of-water-gate lanes` — unlicensed use.
        bones.schema.md line 105: narrow holds license requires the object to be a
        body part of the subject (stillness-against-pressure) or a physical object
        resisting pressure. Lanes are neither. FAULT-FORM-NON-ACTION-VERB.
        (2) `blank` is an adjectival modifier appended after the object.
        FAULT-FORM-MODIFIER.
      why: >
        The bone enacts the Wren-gap maintenance — the east-of-water-gate corridor
        kept blank during maximum-density deployment. This is a load-bearing
        event-coverage entry for the relational_anchor_status axes_held rationale.
        A licensed physical verb must replace `holds … blank`.
      criteria: >
        The verb must be a licensed physical act. `blank` modifier must be removed.
        The substance_delta (all-held: relational_anchor_status, moral_framework)
        and the Wren-gap event must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac skips the east-of-water-gate lanes"
      alternate_recast: "taylor-hebert-kl-122ac leaves the east-of-water-gate lanes"

    - id: fault-009
      type: fault
      bone: b01c18s02n05
      svo_offending: "wren-stitch-maker-flea-bottom-ward crosses the blank lane"
      offending_span: "blank"
      what: >
        `blank` is an adjective modifying `lane`. FAULT-FORM-MODIFIER per
        bones.schema.md line 107 (no adjectives).
      why: >
        The bone is grounding: true and enacts Wren crossing her corridor screened.
        The adjective `blank` carries the Wren-gap information that belongs in a
        loc-state or state-update facet, not in the bone SVO.
      criteria: >
        The adjective must be removed. `wren-stitch-maker-flea-bottom-ward crosses
        the lane` is the minimal clean form. The substance_delta (all-held:
        relational_anchor_status) and grounding function must be preserved.
      recast_suggestion: "wren-stitch-maker-flea-bottom-ward crosses the lane"

    - id: fault-010
      type: fault
      bone: b01c18s02n06
      svo_offending: "the moth-corridor feed returns noise on the chandler-quarter passage"
      offending_span: "on the chandler-quarter passage"
      what: >
        `on the chandler-quarter passage` is a PP of place. FAULT-FORM-MODIFIER.
      why: >
        The op-friction event (one node degraded by smelt-fire) is the event-coverage
        role. The PP appends a location that belongs in loc-state citation. Removing
        it does not lose the event: the feed returning noise is observable without
        the PP.
      criteria: >
        The PP must be removed. The substance_delta (all-held: capability,
        moral_framework) and op-friction event must be preserved.
      recast_suggestion: "the moth-corridor feed returns noise"

    - id: fault-011
      type: fault
      bone: b01c18s02n07
      svo_offending: "the architecture runs all nodes simultaneously"
      offending_span: "simultaneously"
      what: >
        `simultaneously` is an adverb modifying `runs`. FAULT-FORM-MODIFIER per
        bones.schema.md line 107 (no adverbs).
      why: >
        This is the central-event bone for s02 (the full-architecture-open threshold
        crossing) and carries moral_framework DOWN 1.0 (cost_ledger_anchor: cl02).
        An adverb on the central-event moving bone is a HARD violation — the bone
        is the substance anchor for the cl02 cost-ledger entry.
      criteria: >
        The adverb must be removed. The substance_delta (moral_framework DOWN 1.0,
        cl02 anchor) and the full-architecture-open event must be preserved. The
        simultaneous quality of the activation can be implied by the verb choice or
        handled in a sensory/state-update facet.
      recast_suggestion: "the architecture opens every node"
      alternate_recast: "the architecture completes the full-coverage activation"

    - id: fault-012
      type: fault
      bone: b01c18s02n08
      svo_offending: "the count crosses the prior number"
      offending_span: "prior"
      what: >
        `prior` is an adjective modifying `number`. FAULT-FORM-MODIFIER per
        bones.schema.md line 107 (no adjectives). This bone carries position-prot-
        collapse DOWN 0.5 (cost_ledger_anchor: cl07b) — a moving axis bone.
      why: >
        The Khepri-echo register-split is noted in the draft NOTES as depending on
        `prior number` being shape-language rather than a named self-reference. That
        rationale does not exempt the adjective from the SVO ban. The schema's
        modifier rule is absolute. An adjective on a moving-axis bone faults HARD.
      criteria: >
        `prior` must be removed. The bone must read as a count-subject crossing a
        threshold. The substance_delta (position-prot-collapse DOWN 0.5, cl07b)
        and the threshold-crossing event must be preserved.
      recast_suggestion: "the count crosses the threshold"
      alternate_recast: "the count reaches the limit"

    - id: fault-013
      type: fault
      bone: b01c18s02n09
      svo_offending: "taylor-hebert-kl-122ac runs the count into the fortnight"
      offending_span: "into the fortnight"
      what: >
        `into the fortnight` is a PP of direction/time. FAULT-FORM-MODIFIER.
        This bone carries social_tether-prot-collapse DOWN 0.5 (cost_ledger_anchor:
        cl07a) — a moving axis bone.
      why: >
        Time-PPs belong in loc-state/time-context facets. A PP on a moving-axis bone
        faults HARD.
      criteria: >
        The PP must be removed. The substance_delta (social_tether-prot-collapse
        DOWN 0.5, cl07a) and the fortnight-deployment event must be preserved.
        The time-span can be carried in loc-state or state-update facets.
      recast_suggestion: "taylor-hebert-kl-122ac extends the count"

    - id: fault-014
      type: fault
      bone: b01c18s02n10
      svo_offending: "the tallow-render room floor holds the folded cipher-bundle"
      offending_span: "holds … folded"
      what: >
        Two violations:
        (1) `holds` with object `the folded cipher-bundle` — unlicensed holds. The
        object is not a body part of the subject and is not resisting pressure. The
        floor "holding" an object is stative containment / positional description.
        FAULT-FORM-NON-ACTION-VERB.
        (2) `folded` is an adjective modifying `cipher-bundle`. FAULT-FORM-MODIFIER.
      why: >
        The bone is the s02 scene-close grounding image (the folded bundle on the
        floor). It carries moral_framework axes_held (the unanswered-ask enacted).
        The static-state description must become a discrete physical act.
      criteria: >
        Both violations must be resolved. The substance_delta (all-held:
        moral_framework) and the grounding role (cipher-bundle on tallow-render room
        floor as precipice-enacted image) must be preserved.
      recast_suggestion: "the cipher-bundle rests on the tallow-render room floor"
      note: >
        `rests` is stative-adjacent; preferred alternative:
        "the cipher-bundle settles on the tallow-render room floor" (discrete
        arrival event, licenses a loc-state citation for the room).

    # ─── SCENE s03 ──────────────────────────────────────────────────────────────

    - id: fault-015
      type: fault
      bone: b01c18s03n01
      svo_offending: "the groom carries the saddlebag at the wrong hour"
      offending_span: "carries … at the wrong hour … wrong"
      what: >
        Three simultaneous violations:
        (1) `carries` is on the explicit deny-list: "Sustained carrying: carries,
        carried, carrying, bears, bore…" FAULT-FORM-NON-ACTION-VERB.
        (2) `at the wrong hour` is a time-PP. FAULT-FORM-MODIFIER.
        (3) `wrong` is an adjective within the PP. FAULT-FORM-MODIFIER.
      why: >
        This is the first compound-eye specific bone (grounding: true) and the
        central-event anchor for s03's court-apparatus-read-at-scale event. It
        carries political_register-prot axes_held. The event-coverage role (groom
        whose saddlebag-timing mismatches the tilting-yard schedule) is preserved
        by a discrete physical act at the wrong position.
      criteria: >
        `carries` must become a discrete physical act. Time-PP and adjective must be
        removed. The substance_delta (all-held: political_register-prot) and the
        groom/saddlebag compound-eye image must be preserved. The schedule-mismatch
        detail moves to a narrator-interest or state-update facet.
      recast_suggestion: "the groom lifts the saddlebag"
      alternate_recast: "the groom shoulders the saddlebag"

    - id: fault-016
      type: fault
      bone: b01c18s03n02
      svo_offending: "the maid crosses the corridor toward the third contact point"
      offending_span: "toward the third contact point … third"
      what: >
        Two violations:
        (1) `toward the third contact point` is a PP of direction. FAULT-FORM-MODIFIER.
        (2) `third` is an ordinal adjective. FAULT-FORM-MODIFIER.
      why: >
        The maid's irregular corridor pattern is the compound-eye specific image.
        The direction-PP and the ordinal adjective both pad the object. The
        political_register-prot axes_held rationale (maid's pattern indexes to three
        contact points) belongs in a narrator-interest facet.
      criteria: >
        Both modifiers must be removed. `the maid crosses the corridor` is the
        minimal clean form. The substance_delta (all-held: political_register-prot)
        and the corridor-crossing image must be preserved.
      recast_suggestion: "the maid crosses the corridor"

    - id: fault-017
      type: fault
      bone: b01c18s03n03
      svo_offending: "the knight grips the pommel in the small-space method"
      offending_span: "in the small-space method … small-space"
      what: >
        Two violations:
        (1) `in the small-space method` is a PP of instrument/manner. FAULT-FORM-MODIFIER.
        (2) `small-space` is an adjective compound within the PP. FAULT-FORM-MODIFIER.
      why: >
        The enclosed-space grip is the compound-eye specific image; the style-detail
        belongs in a narrator-interest facet. The bone's substance_delta
        (political_register-prot axes_held) and the pommel-grip event are preserved
        by stripping the manner-PP.
      criteria: >
        The PP and adjective must be removed. The substance_delta and the
        knight/pommel grounding image must be preserved.
      recast_suggestion: "the knight grips the pommel"

    - id: fault-018
      type: fault
      bone: b01c18s03n04
      svo_offending: "the septa crosses the outer court at the handoff interval"
      offending_span: "outer … at the handoff interval"
      what: >
        Two violations:
        (1) `outer` is an adjective modifying `court`. FAULT-FORM-MODIFIER.
        (2) `at the handoff interval` is a time-PP. FAULT-FORM-MODIFIER.
      why: >
        The septa's timing mapping to the ward-elder circuit handoff interval is the
        compound-eye specific image. The timing detail belongs in a narrator-interest
        or loc-state facet.
      criteria: >
        Both modifiers must be removed. `the septa crosses the court` is the minimal
        clean form. The substance_delta (all-held: political_register-prot) must be
        preserved.
      recast_suggestion: "the septa crosses the court"

    - id: fault-019
      type: fault
      bone: b01c18s03n05
      svo_offending: "the feed returns the court as system"
      offending_span: "as system"
      what: >
        `as system` is a manner/predicate-complement construction appended to the
        object `the court`. It functions as a modifier on the object, characterizing
        what the court is rather than naming a physical object. FAULT-FORM-MODIFIER.
      why: >
        The event-coverage role (four bodies resolving into one pattern) is the
        mechanism bone for s03. The modifier `as system` describes an interpretation
        of what the feed returns, which is interiority/characterization, not an
        observable physical object. The bone's political_register-prot axes_held
        rationale (court-as-system) belongs in narrator-interest.
      criteria: >
        `as system` must be removed. A concrete object noun must replace `the court
        as system`. The substance_delta (all-held: political_register-prot,
        relational_anchor_status) must be preserved.
      recast_suggestion: "the feed returns the court-pattern"
      alternate_recast: "the feed returns the apparatus-read"

    - id: fault-020
      type: fault
      bone: b01c18s03n06
      svo_offending: "taylor-hebert-kl-122ac files the seventh-day entry"
      offending_span: "seventh-day"
      what: >
        `seventh-day` is an adjective compound modifying `entry`. FAULT-FORM-MODIFIER.
      why: >
        The ordinal-day modifier characterizes the entry type; this detail belongs in
        a state-update or exposition facet. The bone's axes_held (moral_framework,
        capability) do not depend on the ordinal being in the SVO.
      criteria: >
        The adjective compound must be removed. `taylor-hebert-kl-122ac files the
        entry` is the minimal clean form, or a bare noun that does not require an
        adjective. The substance_delta must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac files the day-entry"
      note: >
        `day-entry` is a compound noun functioning as a named object class, not
        an adjective-modified noun. Preferred: "taylor-hebert-kl-122ac files the
        court-entry" (names the content class).

    - id: fault-021
      type: fault
      bone: b01c18s03n07
      svo_offending: "taylor-hebert-kl-122ac files the first-day entry"
      offending_span: "first-day"
      what: >
        `first-day` is an adjective compound modifying `entry`. FAULT-FORM-MODIFIER.
        Same violation class as fault-020.
      why: >
        The ironic-repetition event (first-day filing identical to seventh-day filing)
        is the event-coverage role for the `protagonist-files-each-entry` force tag.
        The ordinal detail is the irony's mechanism but belongs in narrator-interest
        or state-update facets.
      criteria: >
        Same as fault-020. The adjective must be removed. The substance_delta
        (all-held: political_register-prot, moral_legibility_to_self) must be
        preserved.
      recast_suggestion: "taylor-hebert-kl-122ac files the opening-entry"

    - id: fault-022
      type: fault
      bone: b01c18s03n08
      svo_offending: "the insect-feed returns the apparatus complete"
      offending_span: "complete"
      what: >
        `complete` is an adjectival/adverbial modifier appended after the object
        `the apparatus`. FAULT-FORM-MODIFIER. This bone is a moving-axis bone
        (political_register-prot UP 1.0, cost_ledger_anchor: cl06).
      why: >
        A modifier on a moving-axis bone is a HARD violation. The `complete`
        qualifier belongs in a narrator-interest or state-update facet.
      criteria: >
        `complete` must be removed. The substance_delta (political_register-prot
        UP 1.0, cl06 anchor) and the event-coverage role (insect-feed returns the
        apparatus) must be preserved.
      recast_suggestion: "the insect-feed returns the apparatus"

    - id: fault-023
      type: fault
      bone: b01c18s03n09
      svo_offending: "the contempt arrives at the register"
      offending_span: "at the register"
      what: >
        `at the register` is a PP of destination. FAULT-FORM-MODIFIER. This bone
        carries political_register-prot UP 0.5 (cost_ledger_anchor: cl06) — a
        moving-axis bone.
      why: >
        A PP on a moving-axis bone is HARD. The destination detail belongs in a
        state-update facet. Additionally, `contempt arrives` uses an abstract noun
        as subject performing an intransitive motion verb — acceptable in project
        precedent (abstract-subject bones) but only if the verb is clean. The PP
        is the primary fault.
      criteria: >
        The PP must be removed. The substance_delta (political_register-prot UP 0.5,
        cl06) must be preserved. `the contempt arrives` is the minimal clean form
        if abstract-subject ambient-actor bones are accepted (per project precedent
        for "the accounting prices" / "the ledger returns" register).
      recast_suggestion: "the contempt arrives"

    - id: fault-024
      type: fault
      bone: b01c18s03n10
      svo_offending: "taylor-hebert-kl-122ac files the seventh-day entry the same way"
      offending_span: "seventh-day … the same way"
      what: >
        Two violations:
        (1) `seventh-day` is an adjective compound. FAULT-FORM-MODIFIER (same as
        fault-020).
        (2) `the same way` is a manner adverb phrase. FAULT-FORM-MODIFIER.
      why: >
        This is the contempt-without-exit enacted bone: the seventh-day filing
        identical to the first. The manner phrase encodes the irony as a modifier
        rather than as an observable physical act. The irony belongs in
        narrator-interest / state-update facets.
      criteria: >
        Both modifiers must be removed. The substance_delta (all-held:
        political_register-prot) and the filing-repetition event must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac files the court-entry"
      note: >
        The ironic-repetition meaning (identical gesture) is carried by this bone's
        position in the event_map alongside s03n06/n07 filings; it does not need to
        be encoded in the SVO modifier.

    # ─── SCENE s04 ──────────────────────────────────────────────────────────────

    - id: fault-025
      type: fault
      bone: b01c18s04n01
      svo_offending: "taylor-hebert-kl-122ac drops the third packet at the dead drop"
      offending_span: "third … at the dead drop"
      what: >
        Two violations:
        (1) `third` is an ordinal adjective. FAULT-FORM-MODIFIER.
        (2) `at the dead drop` is a PP of place. FAULT-FORM-MODIFIER.
      why: >
        The bone is grounding: true and the central-event anchor for s04 (drop of
        the third packet). The ordinal and location both add modifier padding. The
        location belongs in loc-state; the ordinal belongs in a narrator-interest or
        state-update facet noting the delivery sequence.
      criteria: >
        Both modifiers must be removed. The substance_delta (all-held: capability,
        moral_framework) and the intelligence-delivery event must be preserved.
        `drops the packet` is acceptable; `drops the intelligence-packet` names
        the object class without an ordinal.
      recast_suggestion: "taylor-hebert-kl-122ac drops the intelligence-packet"

    - id: fault-026
      type: fault
      bone: b01c18s04n03
      svo_offending: "the counter-bundle returns the margin-cipher single line"
      offending_span: "margin-cipher … single"
      what: >
        Two violations:
        (1) `margin-cipher` is an adjective compound modifying `line`. FAULT-FORM-MODIFIER.
        (2) `single` is an adjective modifying `line`. FAULT-FORM-MODIFIER.
      why: >
        The bone enacts the physical delivery of the confirmation (counter-bundle
        returning its margin-cipher). Both adjectives describe the line's character
        rather than naming it as a discrete physical object. The substance_delta
        (all-held: position-world, political_register-world) is preserved by
        naming the object cleanly.
      criteria: >
        Both adjectives must be removed. The counter-bundle and the line-delivery
        event must be preserved. `the counter-bundle returns the confirmation-line`
        or `the counter-bundle returns the cipher-line` are acceptable.
      recast_suggestion: "the counter-bundle returns the confirmation-line"

    - id: fault-027
      type: fault
      bone: b01c18s04n04
      svo_offending: "taylor-hebert-kl-122ac reads the cipher line"
      offending_span: "reads"
      what: >
        `reads` is on the FAULT-FORM-PERCEPTION deny-list. Fourth occurrence of
        this violation across the chapter draft.
      why: >
        The bone enacts the confirmation receipt (Taylor reads the succession outcome).
        The axes_held (political_register-prot, relational_anchor_status) rationale
        is load-bearing for the s04 substance contract.
      criteria: >
        `reads` must become a concrete physical act. The substance_delta
        (all-held: political_register-prot, relational_anchor_status) must be
        preserved.
      recast_suggestion: "taylor-hebert-kl-122ac lifts the cipher line"
      alternate_recast: "taylor-hebert-kl-122ac opens the counter-bundle"

    - id: fault-028
      type: fault
      bone: b01c18s04n06
      svo_offending: "the Green faction holds the succession mechanism"
      offending_span: "holds … succession"
      what: >
        Two violations:
        (1) `holds` with object `the succession mechanism` — unlicensed holds. The
        object is not a body part of the subject and is not a physical object
        resisting pressure. A faction "holding" a mechanism is stative
        consolidation-description. FAULT-FORM-NON-ACTION-VERB.
        (2) `succession` is an adjective modifier on `mechanism`. FAULT-FORM-MODIFIER.
        This bone carries political_register-world UP 1.0 (cost_ledger_anchor: cl07c)
        — a moving-axis bone.
      why: >
        A compound violation (unlicensed holds + adjective modifier) on a moving-axis
        bone is HARD. The s04 NOTES confirm this bone uses "OPERATIVE accountability
        language, NOT axis-slug labels" — but operative language must still pass
        SVO-form. `holds` fails the narrow-holds license independent of the
        adjective.
      criteria: >
        Both violations must be resolved. The substance_delta (political_register-world
        UP 1.0, cl07c) and the Green-faction succession event must be preserved.
        Use a transitive physical verb that enacts the faction's consolidation of the
        mechanism.
      recast_suggestion: "the Green faction secures the succession channel"
      alternate_recast: "the Green faction closes the succession access"

    - id: fault-029
      type: fault
      bone: b01c18s04n07
      svo_offending: "taylor-hebert-kl-122ac writes nothing in the record"
      offending_span: "nothing … in the record"
      what: >
        Two violations:
        (1) `writes nothing` — the schema bans negations: "didn't, does not, won't,
        etc. are banned (FAULT-FORM-NEGATION)." The object `nothing` is a negation
        of the expected act. bones.schema.md line 96: "A non-event is not a bone;
        the bone records what did happen."
        (2) `in the record` is a PP of place. FAULT-FORM-MODIFIER.
      why: >
        The event-coverage role is "protagonist-reads-line-writes-nothing" — the
        suppression of the moral_legibility recognition. The not-writing is the
        substantive event. However, bones must record positive physical acts. The
        suppression must be recast as a positive act of setting the stylus aside or
        closing the record without entry.
      criteria: >
        `nothing` must be replaced with a positive act object. The PP must be removed.
        The substance_delta (all-held: moral_legibility_to_self, moral_framework)
        and the suppression-enacted event must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac closes the record"
      alternate_recast: "taylor-hebert-kl-122ac sets the stylus aside"

    - id: fault-030
      type: fault
      bone: b01c18s04n08
      svo_offending: "the ward runs at maximum density"
      offending_span: "at maximum density … maximum"
      what: >
        Two violations:
        (1) `at maximum density` is a PP of manner/state. FAULT-FORM-MODIFIER.
        (2) `maximum` is an adjective within the PP. FAULT-FORM-MODIFIER.
      why: >
        The bone enacts the deployment continuing on the fourteenth day. The density
        qualifier belongs in a state-update or loc-state facet. The substance_delta
        (all-held: capability) is preserved without the PP.
      criteria: >
        Both modifiers must be removed. The substance_delta and the ward-running
        event must be preserved.
      recast_suggestion: "the ward runs"
      note: >
        The bare intransitive `the ward runs` is observable (the network is
        operational). If the scene requires a more discrete physical event,
        "the ward architecture holds the full deployment" — but `holds` is
        unlicensed; prefer "the ward returns the full deployment" or "the
        ward sustains the coverage" — `sustains` also risks non-action. Safest:
        "the ward runs" per the intransitive-lands-cleanly exception.

    # ─── SCENE s05 ──────────────────────────────────────────────────────────────

    - id: fault-031
      type: fault
      bone: b01c18s05n01
      svo_offending: "taylor-hebert-kl-122ac closes the ward-elder routes ward by ward"
      offending_span: "ward by ward"
      what: >
        `ward by ward` is an adverb phrase of manner/sequence. FAULT-FORM-MODIFIER.
      why: >
        The standdown sequence (routes closed one ward at a time) is the event-coverage
        role. The sequencing detail belongs in a narrator-interest or state-update
        facet. The bone's axes_held (capability, moral_framework) do not require the
        manner-phrase in the SVO.
      criteria: >
        The adverb phrase must be removed. The substance_delta and the standdown
        initiation event must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac closes the ward-elder routes"

    - id: fault-032
      type: fault
      bone: b01c18s05n02
      svo_offending: "the east-of-water-gate gap closes last"
      offending_span: "last"
      what: >
        `last` is an adverb modifier on the verb `closes`. FAULT-FORM-MODIFIER.
      why: >
        The Wren-gap-closes-last event is the relational_anchor_status axes_held
        anchor (Wren's corridor held blank through the entire fortnight, closing last
        in the standdown). The ordinal-sequence information belongs in a narrator-interest
        or state-update facet.
      criteria: >
        `last` must be removed. `the east-of-water-gate gap closes` is the minimal
        clean form. The substance_delta (all-held: relational_anchor_status) must
        be preserved.
      recast_suggestion: "the east-of-water-gate gap closes"

    - id: fault-033
      type: fault
      bone: b01c18s05n05
      svo_offending: "the ledger entry names the deployment above the prior number"
      offending_span: "names … above the prior number … prior"
      what: >
        Three violations in one bone:
        (1) `names` is a declarative/perception verb — same class as fault-002 and
        fault-004. FAULT-FORM-PERCEPTION (or FAULT-FORM-INTERIORITY).
        (2) `above the prior number` is a PP of place/comparison. FAULT-FORM-MODIFIER.
        (3) `prior` is an adjective. FAULT-FORM-MODIFIER.
      why: >
        The bone enacts the ledger recording the threshold-crossing (naming the
        deployment above the prior number). The axes_held (moral_framework) rationale
        is that the bone documents what was crossed. A perception verb on a ledger-
        recording bone routes the documentation event inward; the bone must record
        a physical act.
      criteria: >
        All three violations must be resolved. The substance_delta (all-held:
        moral_framework) and the ledger-documentation event must be preserved. The
        threshold-crossing detail moves to a state-update or narrator-interest facet.
      recast_suggestion: "the ledger entry records the threshold-crossing"
      alternate_recast: "the ledger entry closes the deployment column"

    - id: fault-034
      type: fault
      bone: b01c18s05n07
      svo_offending: "the contempt sits in the same column as every other entry"
      offending_span: "sits … in the same column as every other entry"
      what: >
        Two violations:
        (1) `sits` is stative position-naming — "lies, sits, stands describing position
        not posture-act" faults FAULT-FORM-NON-ACTION-VERB (bones.schema.md line 102).
        `the contempt sits in the same column` describes a state of being-located,
        not a discrete posture-act (unlike `taylor stands` meaning the act of rising).
        (2) `in the same column as every other entry` is a PP of place with a
        comparison clause. FAULT-FORM-MODIFIER.
      why: >
        The bone enacts the contempt-without-exit as a ledger fact. The axes_held
        (political_register-prot) rationale requires the contempt's column-position
        to be established. But `sits` is stative, not a discrete observable act, and
        the PP chains a comparison that belongs in a narrator-interest facet.
      criteria: >
        Both violations must be resolved. The substance_delta (all-held:
        political_register-prot) and the contempt-as-ledger-entry event must be
        preserved. Use a physical act that places or positions the contempt-entry.
      recast_suggestion: "the contempt-entry lands in the column"
      alternate_recast: "the column receives the contempt-entry"

    - id: fault-035
      type: fault
      bone: b01c18s05n10
      svo_offending: "the blank column stays blank"
      offending_span: "blank … stays … blank"
      what: >
        Two violations:
        (1) `stays` is a copula-adjacent stative verb (sustained state) —
        FAULT-FORM-NON-ACTION-VERB. "Sustained" state verbs route to state-update
        facets. `stays blank` describes a persistent condition, not a discrete
        observable act.
        (2) `blank` (as subject modifier adjective) + `blank` (as object complement)
        are adjectives. FAULT-FORM-MODIFIER (both).
      why: >
        This is the chapter-closing image bone: the blank column as the enacted form
        of suppression-continuing (moral_legibility_to_self axes_held). The blank
        column staying blank is the most load-bearing single image in the chapter.
        However, a stative verb + adjective-modifier + adjective-complement cannot
        stand under the schema. The event must be recast as a discrete physical act
        that enacts the blankness.
      criteria: >
        The stative verb and both adjectives must be resolved. The substance_delta
        (all-held: moral_legibility_to_self) and the blank-column-as-suppression
        closing image must be preserved. A positive physical act that enacts the
        non-writing is required.
      recast_suggestion: "taylor-hebert-kl-122ac passes the recognition column"
      note: >
        Subject change from ambient-object to Taylor is acceptable for a chapter-
        closing bone. The column as object-as-subject form is also possible:
        "the recognition column receives no entry" — but `no entry` is negation.
        Best: "the recognition column holds no mark" — but `holds` is unlicensed
        and `no mark` is negation. Cleanest discrete act:
        "taylor-hebert-kl-122ac closes the recognition column" (closes without
        writing = the enacted suppression; the blankness is in the state-update).

    - id: fault-036
      type: fault
      bone: b01c18s05n11
      svo_offending: "taylor-hebert-kl-122ac sets the stylus beside the closed ledger"
      offending_span: "beside the closed ledger … closed"
      what: >
        Two violations:
        (1) `beside the closed ledger` is a PP of place/accompaniment. FAULT-FORM-MODIFIER.
        (2) `closed` is an adjective modifying `ledger`. FAULT-FORM-MODIFIER.
      why: >
        This is the grounding: true chapter-close bone (stylus set beside the ledger
        as accounting-as-discipline enacted). The axes_held (moral_framework)
        rationale depends on the gesture's completeness. But the PP and adjective are
        modifier padding; the placement detail belongs in loc-state or state-update
        facets.
      criteria: >
        Both modifiers must be removed. `taylor-hebert-kl-122ac sets the stylus`
        is the minimal clean form if the placement is handled in loc-state. Or
        use a transitive verb that names the placement without a PP.
        The substance_delta (all-held: moral_framework) and the stylus-set grounding
        event must be preserved.
      recast_suggestion: "taylor-hebert-kl-122ac sets the stylus"

    # ─── SYSTEM CHECKS ──────────────────────────────────────────────────────────

    - id: fault-037
      type: pass
      what: "FAULT-AGGREGATE-DELTA-MISMATCH check — all five scenes"
      why: N/A
      note: >
        Per-scene axis_moves sums verified against the draft NOTES claims:
        s01: 0 moves, all-held (EXACT).
        s02: moral_framework -1.0 / position-prot-collapse -0.5 / social_tether-prot-collapse -0.5 (EXACT).
        s03: political_register-prot +1.5 (+1.0 at n08 + +0.5 at n09) (EXACT).
        s04: position-world +1.0 / political_register-world +1.0 (EXACT).
        s05: political_register-prot +0.5 / position-prot-collapse -0.5 / social_tether-prot-collapse -0.5 (EXACT).
        All five MATCH. No FAULT-AGGREGATE-DELTA-MISMATCH.

    - id: fault-038
      type: pass
      what: "FAULT-COST-LEDGER-UNRESOLVED check — cl02, cl06, cl07a, cl07b, cl07c"
      why: N/A
      note: >
        All five cost_ledger_anchor IDs verified against memory.md cost_ledger:
        cl02 (moral_framework cost; b01c18s02n07) — EXISTS.
        cl06 (political_register-prot +5; b01c18s03n08, s03n09, s05n06) — EXISTS.
        cl07a (social_tether-prot-collapse cost; b01c18s02n09, s05n09) — EXISTS.
        cl07b (position-prot-collapse cost; b01c18s02n08, s04n05, s05n08) — EXISTS.
        cl07c (political_register-world cost; b01c18s04n06) — EXISTS.
        No FAULT-COST-LEDGER-UNRESOLVED.

    - id: fault-039
      type: pass
      what: "FAULT-BONE-DELTA-MALFORMED check — axis slugs, directions, magnitudes"
      why: N/A
      note: >
        All axis slugs verified against memory.md state_axes: moral_framework,
        position-prot-collapse, social_tether-prot-collapse, political_register-prot,
        position-world, political_register-world — all valid.
        All directions ∈ {up, down}. All magnitudes > 0 (0.5 and 1.0).
        The 0.5 half-allocations are explicitly licensed by the scene contracts
        (s02 allocates three axes at 1.0/0.5/0.5; s03 at 1.0+0.5; s05 at 0.5/0.5/0.5).
        All axes_held entries carry rationale and valid axis slugs. No chatter bones
        identified (all non-moving bones carry axes_held with rationale).
        No FAULT-BONE-DELTA-MALFORMED.

    - id: fault-040
      type: pass
      what: "FAULT-CONSTRAINT check — laws, lore, Earth-Bet fence, Khepri register-split"
      why: N/A
      note: >
        Khepri register-split (pl-2026-06-05-c18-001): verified held throughout.
        No bone gives Taylor an interior self-naming as Khepri. s02n07
        architecture-as-subject, s02n08 count-as-subject confirmed as shape-language.
        Earth-Bet proper-noun fence: no parahuman jargon in bone SVOs.
        Westerosi geography (Fishmonger Gate, Gate of Gods, Iron Gate, River Gate,
        east-of-water-gate, tallow-render room, chandler quarter, dead drop): all
        consistent with cond-kl-geography-122ac and prior chapter deployments
        (c12-c17). Flea Bottom ward geography (ward-elder routes, ward-by-ward
        standdown) consistent with established network architecture.
        No FAULT-CONSTRAINT. No FAULT-PHYSICAL.

    - id: fault-041
      type: flag
      bone: b01c18s01n06
      svo_offending: "the tallow-render room floor receives the bundle"
      what: >
        `receives` as a verb applied to an inanimate ambient-actor (the floor).
        "Receives" as a stative-containment verb is borderline — the floor does
        not perform a discrete physical act; the bundle is placed on it by an agent
        not visible in this bone. However, in the ambient-actor register (object-as-
        subject bones permitted by the preamble "Object-as-subject form is allowed
        for ambient actors"), `receives` has been accepted in this project (cf. b01c01
        "the ground transmits the child's breath"). No prior Pass 2 fault has been
        recorded for `receives` in ambient-actor position.
      why: >
        The bone is grounding: true and the precipice-enacted image (the ask sitting
        unanswered). Faulting it would require a recast that risks losing the image.
        Flagged for fixer consideration but not classified as a fault.
      criteria: null

    - id: fault-042
      type: flag
      bone: b01c18s04n05
      svo_offending: "the succession document clears the Small Council access window"
      what: >
        `Small Council` is a proper-noun compound functioning as an adjective modifier
        on `access window`. However, in this project `Small Council` operates as an
        established world-proper-noun (equivalent to a named location), and
        `Small Council access window` may be read as a named compound noun (the
        specific procedural mechanism) rather than an adjective-modified noun.
        Prior project bones have used established proper-noun compounds in object
        position without fault (e.g., `the Fishmonger Gate bottlefly routes` is
        treated as a compound name above — though that is also faulted at fault-005
        for the PP, not for `Fishmonger Gate` as modifier). Borderline: the proper-
        noun compound is ambiguous.
      why: >
        This is a moving-axis bone (position-world UP 1.0, cost_ledger_anchor: cl07b).
        If `Small Council` is treated as an adjective, it is FAULT-FORM-MODIFIER
        on a moving-axis bone (HARD). Flagging for fixer determination. If fixer
        classifies this as an adjective modifier, recast to:
        "the succession document clears the Council access" or
        "the succession document clears the Small Council window."
      criteria: null

  # ─── FAULT-FORM PATTERN SUMMARY ─────────────────────────────────────────────

  pattern_summary:
    FAULT-FORM-PERCEPTION:
      count: 6
      bones: [b01c18s01n02, b01c18s01n03, b01c18s01n04, b01c18s01n07, b01c18s04n04, b01c18s05n05]
      verbs_offending: [reads ×4, names ×2]
      note: >
        `reads` appears at s01n02, s01n04, s04n04 — identical violation three times.
        `names` appears at s01n03, s01n07, s05n05. The chapter's interiority-heavy
        register (ledger-discipline, counting, recognizing) repeatedly generates
        perception-verb bones. All six must be recast to discrete physical acts.
    FAULT-FORM-MODIFIER:
      count: 24
      moving_axis_bones_affected: [s02n07 (mf-1.0), s02n08 (ppc-0.5), s02n09 (stpc-0.5), s03n08 (prp+1.0), s03n09 (prp+0.5), s04n06 (prw+1.0)]
      note: >
        Six of the 24 modifier faults are on moving-axis bones — these are HARD
        under the substance bone-gate (the axis-move cannot be confirmed if the
        bone's SVO is formally defective). Prepositional padding (place/direction/time
        PPs) accounts for the majority. Adjective modifiers (ordinals, compound
        adjectives, qualifiers) account for the remainder. The pattern is systematic
        across all five scenes.
    FAULT-FORM-NON-ACTION-VERB:
      count: 7
      bones: [s02n04 (holds), s02n10 (holds), s03n01 (carries), s04n06 (holds), s05n07 (sits), s05n10 (stays), s05n11-via-fault-036-adjacent-see-fault-035]
      note: >
        Three unlicensed `holds` usages: s02n04 (lanes), s02n10 (cipher-bundle on
        floor), s04n06 (succession mechanism). All fail the narrow holds license.
        `carries` at s03n01 is on the explicit deny-list. `sits` (s05n07) and `stays`
        (s05n10) are stative position-naming verbs.
    FAULT-FORM-NEGATION:
      count: 1
      bones: [s04n07 (writes nothing)]
    FAULT-FORM-CONJUNCTION:
      count: 1
      bones: [s02n03 (and the Iron Gate and the River Gate)]

  clean_bones_confirmed:
    - b01c18s01n01  # lifts the cipher-bundle — CLEAN
    - b01c18s01n05  # folds the cipher-bundle — CLEAN
    - b01c18s04n02  # jarvis-coin-kl-courier collects the access-window packet — CLEAN
    - b01c18s05n03  # the chandler-quarter moths settle the eaves — CLEAN
    - b01c18s05n04  # opens the cost-ledger column — CLEAN
    - b01c18s05n06  # closes the protection-entry line — CLEAN
    - b01c18s05n08  # writes the standdown line — CLEAN
    - b01c18s05n09  # the ledger closes the disposal-calculus entry — CLEAN
    note: >
      b01c18s01n06 and b01c18s04n05 are flagged (fault-041, fault-042) but not
      faulted; fixer may pass or fault-and-recast based on project-precedent call.
      b01c18s02n02 (opens the moth-corridor through the chandler quarter) carries
      only a PP fault (fault-006), not a verb or conjunction fault.
