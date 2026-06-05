```yaml
audit:
  scope: chapter
  target: b01c19
  timestamp: 2026-06-05
  findings:

    # ── FAULT-FORM-MODIFIER (PP tails) ──────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        b01c19s01n01 (flat_id 1):
        `taylor-hebert-kl-122ac lifts the cipher-bundle from the trough`
        Violating token: `from the trough` — prepositional phrase of source.
      why: >
        PP-ban violation. The source location is grounding-load-bearing (the trough
        IS the dead-drop; this is the chapter's first grounding bone per the notes).
        Stripping without recast loses the URI-WRITE-SENSORY-GROUNDING quota anchor.
        Fixer must preserve the trough as grounding via a separate object-as-subject
        bone or a transitive verb that takes the trough as direct object.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). The trough must
        remain present in the scene's grounding record — either through a recast of
        this bone to a transitive that takes the trough as direct object (e.g.
        `taylor-hebert-kl-122ac clears the trough`) or through a companion
        object-as-subject grounding bone (e.g. `the trough releases the
        cipher-bundle`). One of the two grounding bones in s01 must name the trough.

    - id: fault-002
      type: fault
      what: >
        b01c19s01n02 (flat_id 2):
        `taylor-hebert-kl-122ac opens the sheet under the grey-dark`
        Violating token: `under the grey-dark` — prepositional phrase of location/
        instrument.
      why: >
        PP-ban violation. The grey-dark reading-light is the axes_held rationale for
        moral_framework (eleven months' repetition). Stripping it removes the only
        grounding element for this axis's rationale. Fixer must recast so the
        grey-dark appears as a scene element without living in a PP tail — object-as-
        subject form is the c18 canonical model.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). If the grey-dark is
        narratively load-bearing for the moral_framework hold rationale, it must
        remain reachable as a separate grounding bone (e.g. `the grey-dark covers
        the sheet`) rather than as a modifier inside this bone.

    - id: fault-003
      type: fault
      what: >
        b01c19s01n04 (flat_id 4):
        `taylor-hebert-kl-122ac sets the sheet on the tallow-render room floor`
        Violating token: `on the tallow-render room floor` — prepositional phrase of
        destination/location.
      why: >
        PP-ban violation. The notes mark this bone as a GROUNDING bone for the
        tallow-render room floor. Stripping the PP removes the only explicit location-
        naming for this scene's setting. Fixer must recast to a transitive that takes
        the floor as direct object, or add a companion object-as-subject grounding bone.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). The tallow-render
        room floor must remain present in the scene's grounding record. The
        precipice-posture (sheet set unanswered in the room) must remain recoverable
        from the bone sequence.

    - id: fault-004
      type: fault
      what: >
        b01c19s03n02 (flat_id 19):
        `the chamberlain crosses the pillar junction before dawn`
        Violating token: `before dawn` — prepositional phrase of time.
      why: >
        PP-ban violation. The time-anchor is cited in the axes_held rationale for
        capability (pre-dawn courier hand-off). The pillar junction as direct object
        of "crosses" is clean; only the time-PP is the fault. Stripping `before dawn`
        does not lose grounding since the pillar junction carries the grounding work.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). `the chamberlain
        crosses the pillar junction` is the clean residual form. The pre-dawn
        time-fact may live in a location-state facet citation rather than in the bone.

    - id: fault-005
      type: fault
      what: >
        b01c19s03n05 (flat_id 22):
        `taylor-hebert-kl-122ac drops the compiled-reading through the Jarvis channel`
        Violating token: `through the Jarvis channel` — prepositional phrase of
        instrument/path.
      why: >
        PP-ban violation. The Jarvis channel is the notes-named "GROUNDING bone"
        subject for this scene. With the PP stripped, the grounding element is lost.
        Fixer must recast to preserve the Jarvis channel — either as a transitive
        target (`taylor-hebert-kl-122ac opens the Jarvis channel` + companion drop
        bone) or object-as-subject (`the Jarvis channel receives the compiled-
        reading`).
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). The Jarvis channel
        must remain present in the scene's grounding record, because the notes
        designate it as the scene's institutional grounding anchor. The request-
        completion loop (compiled-reading delivered) must remain covered.

    - id: fault-006
      type: fault
      what: >
        b01c19s03n08 (flat_id 25):
        `taylor-hebert-kl-122ac sets the stylus beside the ledger`
        Violating token: `beside the ledger` — prepositional phrase of location/
        accompaniment.
      why: >
        PP-ban violation. This is CFR-2 BONE 2 — the beside-placement is the
        structural enacted distinction (contempt adjacent to the accounting without
        entering it). The spatial relationship is load-bearing: the substance
        contract's "contempt sits alongside not inside" depends on `beside` being
        expressed. Fixer must find a clean SVO that encodes the spatial adjacency
        without a PP tail. This is the hardest recast in the set; a new object-as-
        subject bone (`the stylus lands the ledger-edge`) or an alternative transitive
        (`taylor-hebert-kl-122ac edges the stylus`) paired with a grounding companion
        may be required.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). The spatial
        relationship of beside-not-away-from (CFR-2 enacted distinction) must remain
        recoverable from the bone or a companion grounding bone in the same scene.
        The two-bone CFR-2 sequence (n07 lift → n08 beside-set) must continue to
        deliver the enacted distinction as physical choreography.

    - id: fault-007
      type: fault
      what: >
        b01c19s04n01 (flat_id 27):
        `taylor-hebert-kl-122ac takes the Tallow Croft corner position at the
        second-bell interval`
        Violating token: `at the second-bell interval` — prepositional phrase of time.
      why: >
        PP-ban violation. The time-anchor (second-bell) is load-bearing for the
        event_map entry `empty-corner-second-bell` and for the narrative contrast with
        the third-bell approach. However, the Tallow Croft corner as object of "takes"
        is clean; only the time-PP faults. Second-bell may live in a location-state
        facet citation.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). `taylor-hebert-
        kl-122ac takes the Tallow Croft corner position` is the clean residual form.
        The second-bell time-fact may live in a location-state citation.

    - id: fault-008
      type: fault
      what: >
        b01c19s04n04 (flat_id 30):
        `taylor-hebert-kl-122ac holds the lane-position at the third-bell interval`
        Violating tokens: (1) `at the third-bell interval` — prepositional phrase of
        time; (2) `holds the lane-position` — `holds` used as sustained-position
        stative verb, outside the narrow holds license (not a body part against
        pressure, not an object resisting pressure).
      why: >
        Double fault: PP-ban + non-action-verb. The `holds` fault is independent of
        the PP fault — removing the PP tail still leaves a non-licensed `holds`.
        The third-bell time-fact is load-bearing for the second approach confirmation
        (pl-2026-06-05-c19-001). The lane-position occupancy must be expressed as a
        concrete physical act (e.g. `takes`, `occupies` is banned, `plants`, `marks`
        — fixer must choose a licensed transitive).
      criteria: >
        The bone must satisfy clean SVO: no PP tail and a licensed action verb. The
        third-bell time-fact may live in a location-state citation. The physical act
        of taking/holding the lane-position for the second approach must remain
        present in the bone sequence.

    - id: fault-009
      type: fault
      what: >
        b01c19s04n08 (flat_id 34):
        `taylor-hebert-kl-122ac writes daven out of the coverage-map`
        Violating token: `out of the coverage-map` — prepositional phrase of
        destination/source.
      why: >
        PP-ban violation. The coverage-map is the grounding-designated object for
        this bone per the notes. The act of removing Daven from the coverage-map is
        the tether-node's formal removal; the PP is carrying the object the action
        acts on. Fixer may recast to a two-bone sequence (e.g. `taylor-hebert-
        kl-122ac strikes the daven entry` + `the coverage-map closes the daven node`)
        or a transitive that avoids the PP while retaining the coverage-map reference.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). The coverage-map
        must remain the named grounding object for this bone (per scene s04's
        grounding quota). The formal removal of Daven from the coverage-map must
        remain covered by the resulting bone(s).

    # ── FAULT-FORM-MODIFIER (adjective / adverb on bone) ─────────────────────

    - id: fault-010
      type: fault
      what: >
        b01c19s01n06 (flat_id 6):
        `the protection-line ratio runs clean`
        Violating token: `clean` — adverb/predicate adjective modifying the verb.
      why: >
        Adverb modifier on verb. The schema bans adverbs as FAULT-FORM-MODIFIER.
        `runs clean` is `runs [adv]`. The intended meaning (the ratio returns without
        anomaly) must be expressed through a clean transitive or a companion bone.
      criteria: >
        The bone must satisfy clean SVO (no adverb/adjective modifier). The fact that
        the protection-line accounting returns without anomaly must remain recoverable —
        either through the verb choice alone or through the bones sequence context.

    - id: fault-011
      type: fault
      what: >
        b01c19s01n07 (flat_id 7):
        `the standing-coverage bottlefly nodes return the ambient outer-ring feed`
        Violating tokens: (1) `standing-coverage` — adjectival modifier on subject
        noun; (2) `ambient` — adjective modifier on object noun.
      why: >
        Double adjective modifier fault. The schema bans adjectives as FAULT-FORM-
        MODIFIER. `standing-coverage` is a participial adjectival phrase modifying
        `bottlefly nodes`; `ambient` is an adjective modifying `outer-ring feed`. The
        subject should be a named entity slug (e.g. `the bottlefly nodes` or a
        specific node slug); the object should be `the outer-ring feed` without the
        `ambient` qualifier.
      criteria: >
        The bone must satisfy clean SVO with no adjective modifiers on subject or
        object. The subject must be the named node set without adjectival qualification.
        The object must be the outer-ring feed without `ambient` or equivalent
        adjective.

    - id: fault-012
      type: fault
      what: >
        b01c19s04n03 (flat_id 29):
        `the vat-house shutter closes the east-facing window`
        Violating token: `east-facing` — adjectival participial modifier on object noun.
      why: >
        Adjective modifier fault. `east-facing` is a directional participial adjective
        on `window`. Per schema, adjectives on objects are FAULT-FORM-MODIFIER.
        Compound nouns are acceptable tokens but `east-facing` is a participial
        adjective (facing east), not a compound noun. The shutter closing the window
        is the load-bearing grounding event (per pl-2026-06-05-c19-001); the
        directional qualifier is not essential to the bone's narrative function.
      criteria: >
        The bone must satisfy clean SVO (no adjective on object). `the vat-house
        shutter closes the window` is the clean residual form. If the east-facing
        orientation is required for location-state purposes it lives in a facet
        citation, not in the bone.

    # ── FAULT-FORM-NON-ACTION-VERB ────────────────────────────────────────────

    - id: fault-013
      type: fault
      what: >
        b01c19s01n08 (flat_id 8):
        `the column stays open`
        Violating token: `stays open` — stative verb + predicate adjective.
        `stays` is a sustained-state verb (stative position-naming class);
        `open` is a predicate adjective.
      why: >
        Non-action-verb fault. `stays` describes a continuing state, not a discrete
        observable act. This is the first MOVING bone (political_register-prot +0.5,
        cl06 anchor). The axis move requires a bone that enacts a concrete physical
        event — not a stative description of the column's condition. The move must
        be carried by an observable action.
      criteria: >
        The bone must satisfy clean SVO with a concrete action verb. The
        political_register-prot +0.5 move anchored to cl06 must remain attached to a
        discrete physical act in s01. The verb must describe what an observer would
        see happen, not a state that persists.

    - id: fault-014
      type: fault
      what: >
        b01c19s02n01 (flat_id 9):
        `the cost-ledger column holds eleven months of entries`
        Violating token: `holds` — containment use outside narrow license.
        (Not a body part against pressure; not a physical object resisting pressure;
        this is a possession/containment `holds`.)
      why: >
        Non-action-verb fault. The schema explicitly lists containment `holds` as
        disallowed. This is a GROUNDING bone intended to establish the eleven-month
        weight of the accounting. A concrete physical action must carry that grounding
        (e.g. `the cost-ledger column spans eleven months of entries` is also stative
        — fixer must find a discrete enactment: `the cost-ledger column opens to
        eleven months of entries` or similar). The axis hold for moral_framework must
        remain attached.
      criteria: >
        The bone must satisfy clean SVO with a licensed action verb (not `holds` in
        containment sense, not `spans`, not `contains`). The eleven-month weight as a
        concrete fact of the document must remain present in the scene's grounding
        record.

    - id: fault-015
      type: fault
      what: >
        b01c19s02n07 (flat_id 15):
        `the factional-reading structure continues to assemble`
        Violating token: `continues to assemble` — aspectual auxiliary `continues`
        + infinitive. `continues` is a stative/non-action aspectual construction
        describing ongoing state, not a discrete observable act.
      why: >
        Non-action-verb fault. `continues to [verb]` describes persistence of an
        existing state, which is stative. The schema requires concrete physical verbs
        describing what an observer would see happen at a discrete moment. The
        recognition-beginning-not-terminal mechanism and the axes_held for
        moral_legibility_to_self + the two collapse axes must be carried by a bone
        that names a concrete physical act.
      criteria: >
        The bone must satisfy clean SVO with a discrete action verb (not `continues`,
        not `keeps`, not `resumes`). The bone must name the concrete observable act
        that enacts the factional-reading structure's continuation — the assembly
        event, not the ongoing state of assembling.

    - id: fault-016
      type: fault
      what: >
        b01c19s04n02 (flat_id 28):
        `the Tallow Croft corner holds empty`
        Violating token: `holds empty` — `holds` + predicate adjective `empty`,
        outside the narrow holds license. The corner is not a body part against
        pressure nor an object resisting pressure.
      why: >
        Non-action-verb fault. The schema's narrow `holds` license does not cover
        location-state description. This is CONCRETE BONE 1 of the pl-2026-06-05-
        c19-001 inference instrument; the empty corner at second-bell is the
        first opposing-force signal and the first social_tether-prot-collapse /
        position-prot-collapse held bone. A stative description of the corner's
        emptiness does not satisfy the schema's discrete-observable-act requirement.
        Fixer must recast as what did happen at the corner (e.g. `the Tallow Croft
        corner returns no contact` — but "returns" may be perception; the object-as-
        subject form is the c18 model: something the corner does that enacts the
        absence concretely).
      criteria: >
        The bone must satisfy clean SVO with a licensed action verb. The empty corner
        at second-bell must remain the concrete opposing-force enactment for
        social_tether-prot-collapse and position-prot-collapse held rationale. The
        absence must be expressed through a positive physical action (per no-negation
        rule), not through a stative description of emptiness.

    # ── FAULT-FORM-PERCEPTION ──────────────────────────────────────────────────

    - id: fault-017
      type: fault
      what: >
        b01c19s02n02 (flat_id 10):
        `taylor-hebert-kl-122ac counts the factional-reading entries`
        Violating token: `counts` — perception/observation verb.
        The schema deny-list includes `counted`; `counts` is the same root.
      why: >
        Perception-verb fault. `counts` describes an internal observation act (the
        POV character performing arithmetic). The schema bans perception verbs as
        POV-leaks that describe internal observation, not external action. The notes
        explicitly argue CFR-1 compliance via "physical enumeration act" — but the
        schema's deny-list does not carve out a CFR exception for perception verbs.
        The accounting pattern-recognition must be delivered through a concrete
        non-perception verb. The axes_held for moral_legibility_to_self must remain.
      criteria: >
        The bone must satisfy clean SVO with a non-perception verb. The enumeration
        act that carries the CFR-1 pattern-recognition mechanism (counting as physical
        act, not interior observation) must be recast to a verb an external observer
        would see: e.g. `taylor-hebert-kl-122ac runs the factional-reading column`
        (if `runs` is clean in context) or another transitive that names the concrete
        accounting gesture without invoking perception vocabulary.

    # ── FAULT-FORM-INTERIORITY ─────────────────────────────────────────────────

    - id: fault-018
      type: fault
      what: >
        b01c19s02n05 (flat_id 13):
        `taylor-hebert-kl-122ac marks the recurrence`
        Violating token: `the recurrence` — abstract noun as direct object.
        `recurrence` is an abstraction, not a physical entity or document element.
      why: >
        Abstraction-as-object fault. The schema classifies "a physical verb whose
        object is an abstract noun" as FAULT-FORM-INTERIORITY. `recurrence` is
        abstract — it names a temporal pattern, not a physical mark-able surface.
        The notes claim this is a "concrete accounting act, not an interior naming,"
        but the object of `marks` must be a concrete physical entity (a ledger cell,
        a column entry, a line in the document) for the bone to be clean. The
        moral_legibility_to_self held axis and the CFR-1 marking act must remain.
      criteria: >
        The bone must satisfy clean SVO with a concrete physical object (not an
        abstract noun). The marking act that enacts the pattern-recognition recording
        must name the concrete document element being marked: e.g. `taylor-hebert-
        kl-122ac marks the column entry` or `taylor-hebert-kl-122ac notches the
        ledger line` — a physical surface, not the abstract fact of recurrence.

    - id: fault-019
      type: fault
      what: >
        b01c19s03n09 (flat_id 26):
        `the contempt occupies the column's edge`
        Violating tokens: (1) `contempt` as subject — abstraction as actor;
        (2) `occupies` — explicitly listed in the schema deny-list as a containment
        non-action verb.
      why: >
        Double fault: non-action-verb + abstraction-as-subject/interiority. `contempt`
        is an interior state; it cannot be the subject of a bones-file action. The
        schema states "a physical verb whose object is an abstract noun" is interiority
        — the same logic applies to abstraction-as-subject. `occupies` is
        independently banned in the containment deny-list. This bone is the final
        image bone for s03 (contempt-alongside-the-accounting); the image must be
        delivered through a concrete physical subject performing a concrete action.
      criteria: >
        The bone must satisfy clean SVO with a concrete physical subject (not an
        abstract noun) and a licensed action verb (not `occupies`, not `sits`,
        not `fills`). The contempt-alongside image must be delivered through a
        physical object that carries the spatial-adjacency meaning — the stylus, the
        ledger edge, or a named physical surface taking a concrete action that
        embodies the `alongside-not-inside` relationship.

    # ── FAULT-FORM: BARE DIRECTIONAL MOTION ───────────────────────────────────

    - id: fault-020
      type: fault
      what: >
        b01c19s03n03 (flat_id 20):
        `the courier goes east-by-service-gate`
        Violating token: `goes east-by-service-gate` — bare intransitive motion verb
        `goes` + directional compound acting as a prepositional phrase of direction/
        destination. The schema requires a transitive verb that takes the location as
        direct object (`taylor enters the yard`, not `taylor walks into the yard`).
      why: >
        Directional-motion PP fault. `goes` is an intransitive motion verb; `east-by-
        service-gate` is a directional modifier (prepositional in function, compressed
        into a compound). The schema bans prepositional phrases of direction and
        requires transitive form. The courier's directional movement is load-bearing
        for the capability axis hold (confirming the contact interval's direction).
      criteria: >
        The bone must satisfy clean SVO with a transitive motion verb taking the exit
        or gate as direct object. The courier's east-by-service-gate direction must
        remain recoverable as the indexing fact for the capability-axis hold. Recast
        to a form such as `the courier exits the service-gate` or `the courier takes
        the east service-gate`.

    # ── FAULT-FORM: LANE-SHAPE GROUNDING BONE ─────────────────────────────────

    - id: fault-021
      type: fault
      what: >
        b01c19s02n04 (flat_id 12):
        `the lane-shape wears into the stone`
        Violating token: `into the stone` — prepositional phrase of destination/
        direction (PP-ban).
      why: >
        PP-ban violation on the grounding bone for s02. The lane-stone worn track is
        the scene's physical image for the column-shape (axes_held: moral_legibility_
        to_self). Stripping `into the stone` risks losing the grounding anchor for
        s02 — if the fixer strips only the PP, `the lane-shape wears` is a bare
        intransitive that loses the stone surface entirely. Recast must preserve the
        stone as the object of a transitive or as a companion bone. The c18 model is
        object-as-subject: `the stone receives the lane-shape`.
      criteria: >
        The bone must satisfy clean SVO (no prepositional tail). The stone surface
        as concrete grounding element must remain present for s02's grounding quota.
        Recast as a transitive taking the stone as direct object (`the lane-shape
        marks the stone`) or add a companion object-as-subject bone (`the stone
        takes the lane-shape`).

    # ── STRUCTURAL FAULT: ORPHANED EVENT_MAP REFERENCE ────────────────────────

    - id: fault-022
      type: fault
      what: >
        Scene b01c19s03 event_map, row:
        `author-noticed: CFR-2 stylus placement — beside not away from | author |
        b01c19s03n10`
        Bone b01c19s03n10 is referenced in the event_map but does not exist in the
        bones file. s03 contains bones n01 through n09 only (9 bones). flat_id 26
        (b01c19s03n09) is the last bone in s03.
      why: >
        Orphaned event_map reference. The event_map entry will fail validation at
        `/and-review bones` Phase 0 (event-coverage check: every event_map entry must
        resolve to at least one existing bone). The CFR-2 stylus placement is
        substantively covered by n07 and n08 — n10 appears to be a redundant entry
        that was not removed when the event was distributed across n07/n08. If this
        is a genuine missing bone, the coverage is incomplete; if it is an authoring
        bookkeeping error, the event_map row must point to n07 and/or n08.
      criteria: >
        The event_map row citing b01c19s03n10 must either (a) be corrected to cite the
        existing covering bones (n07 and/or n08) if CFR-2 coverage is already present
        there, or (b) a new bone b01c19s03n10 must be authored if the coverage is
        genuinely incomplete. The event_map must contain no references to non-existent
        bone IDs.

    # ── SUMMARY PASS ──────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        Aggregate per-axis delta sums vs. chapter targets.
        political_register-prot: bones sum +1.5 = target +1.5 EXACT.
        moral_legibility_to_self: bones sum +0.5 = target +0.5 EXACT.
        social_tether-prot-collapse: bones sum -1.5 = target -1.5 EXACT.
        position-prot-collapse: bones sum -1.0 = target -1.0 EXACT.
        All held axes (moral_framework, relational_anchor_status, capability,
        social_tether-antag) carry rationales on every bone that holds them.
      why: No action required.

    - id: pass-002
      type: pass
      what: >
        Cost-ledger anchors: cl06 (flat_ids 8, 24, 27), cl07a (flat_ids 14, 32),
        cl07b (flat_id 33). All three anchor IDs confirmed present in series
        cost_ledger per dispatch context.
      why: No action required.

    - id: pass-003
      type: pass
      what: >
        axes_held entries: all 35 bones with axes_held[] carry non-empty rationale
        strings on every held-axis entry. No chatter bones (empty axis_moves + empty
        axes_held without cost_ledger_anchor). No FAULT-BONE-DELTA-MALFORMED detected
        on axis names, direction values, or rationale presence. Fractional 0.5
        magnitudes accepted per project-established practice (c14–c18).
      why: No action required.

    - id: pass-004
      type: pass
      what: >
        Grounding quota: ≥1 grounding bone per scene verified. s01: 2 grounding
        bones (n01, n04 — both now bear PP faults that must be remediated without
        losing grounding coverage). s02: 2 grounding bones (n01, n04 — n01 bears
        non-action-verb fault, n04 bears PP fault; both require recast that preserves
        grounding). s03: 2 grounding bones (n02, n05 — n02 PP fault on `before dawn`
        only; stripping time-PP leaves pillar junction intact). s04: 3 grounding bones
        (n01 PP fault, n03 adjective fault, n08 PP fault; all require grounding-
        preserving recast). The quota is at risk if fixer strips PP/adjective faults
        without recasting as object-as-subject or transitive-object companions.
        NOTE FOR FIXER: URI-WRITE-SENSORY-GROUNDING quota (≥1 grounding bone/scene)
        must be preserved across all remediations.
      why: >
        Flagged for fixer awareness. The grounding quota passes in the current draft
        but several grounding bones carry faults that, if stripped without recast,
        would drop scenes below quota. Fixer must track grounding quota bone-by-bone.

    - id: pass-005
      type: pass
      what: >
        Earth-Bet fence: no Khepri / Gold Morning / Skitter / Brockton Bay / cape
        lore in any bone. All 35 bones contain only Westerosi location names,
        physical objects, and in-world accounting vocabulary.
      why: No action required.

    - id: pass-006
      type: pass
      what: >
        Zero speech bones confirmed. All 35 bones are physical actions. No dialogue
        anchors. Chapter declared as silent/solitary throughout. No FAULT-DIALOGUE-
        MISSING-AT-ANCHOR exposure.
      why: No action required.

    - id: pass-007
      type: pass
      what: >
        Opposing-force visible per scene: s01 (n03, n06), s02 (n01, n03), s03
        (n08, n09 — n09 carries its own faults but opposing-force is visible across
        n08 in the scene), s04 (n02, n03, n05). Per-scene opposing-force requirement
        met or recoverable after recast.
      why: No action required.

    - id: pass-008
      type: pass
      what: >
        Constraint check: no series laws, lore facts, or cond-* card constraints
        identified as violated by any bone content. The chapter is solitary, no
        actor interactions; no prop-possession or location-presence state conflicts
        detected in the bones as written.
      why: No action required.
```
