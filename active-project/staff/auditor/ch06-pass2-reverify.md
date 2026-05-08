audit:
  scope: episode
  target: chapter-06 (proto-lines)
  pass: 2 — Constraint Audit (re-verification, post-fixer)
  timestamp: 2026-05-07
  total_lines_checked: 104
  blank_timeskip_lines_skipped: 2 (lines 14, 54)
  verdicts:
    CORRECT: 55
    fault: 47
    flag: 2
  fault_count_by_class:
    FAULT-FORM-MODIFIER: 42
    FAULT-FORM-PERCEPTION: 2
    FAULT-FORM-INTERIORITY: 1
    FAULT-PHYSICAL-ACTOR-ABSENT: 1
    FAULT-FORM-MODIFIER (subject-form deviation, flagged not faulted): 0
  continuity_ok: NO

  findings:

    - id: fault-001
      type: fault
      what: proto-line 12 — "taylor-hebert-westeros scans the Harrenhal road"
      why: >
        `scans` is a perception verb. The SVO spine forbids perception verbs as POV-leaks;
        the brief's list ("read, took, tracked, noted, counted, measured, or other POV-leak verb")
        is explicitly non-exhaustive. `scans` names a cognitive act of visual searching, not a
        concrete physical event an observer could witness. Downstream facet-authoring (narrator-interest,
        feeling-flags) over a perception-verb proto-line will build on a bad anchor.
      criteria: line must record a concrete physical act observable from outside Taylor's cognition; the perception-as-such must be absent
      recommended_action: RECAST-PHYSICAL

    - id: fault-002
      type: fault
      what: proto-line 13 — "taylor-hebert-westeros turns south"
      why: >
        `south` functions as a directional adverb modifying `turns`. The SVO spine prohibits
        adverbs and prepositional padding. Downstream shape and continuity passes will read this
        as having directional content the bone file should not carry — direction belongs in
        location-state citations, not in the proto-line.
      criteria: line must not carry a directional modifier; the turn event must be recorded without adverbial qualification
      recommended_action: DELETE or recast as bare "taylor-hebert-westeros turns"

    - id: fault-003
      type: fault
      what: proto-line 23 — "septon-rowan crosses to his writing table"
      why: >
        `to his writing table` is a prepositional phrase attached to a motion verb. The SVO spine
        prohibits prepositional padding. Destination-of-motion is location information belonging in
        location-state citations, not the proto-line spine. Leaving it here corrupts the bone-only
        contract and will create ambiguity at pass 5 continuity (the table becomes a state dependency
        not established via the proper state-update channel).
      criteria: line must not carry a prepositional destination phrase; the crossing event must be recorded as bare SVO
      recommended_action: DELETE destination phrase; bare "septon-rowan crosses" is the target form or recast with location-state citation

    - id: fault-004
      type: fault
      what: proto-line 27 — "septon-rowan sets the stylus down"
      why: >
        `down` is a directional particle/adverb modifying `sets`. The SVO spine prohibits adverbs.
        The result-state of the placement belongs in a state-update facet, not the proto-line.
      criteria: line must not carry a directional or result modifier; the placement action must stand without qualification
      recommended_action: DELETE adverb; bare "septon-rowan sets the stylus" or recast to "septon-rowan places the stylus"

    - id: fault-005
      type: fault
      what: proto-line 30 — "septon-rowan takes the stylus again"
      why: >
        `again` is an adverb. The SVO spine prohibits adverbs. Temporal repetition context belongs in
        scene flow, not the proto-line. Downstream facet authoring will re-establish context from
        the surrounding beat sequence.
      criteria: line must not carry a temporal adverb; the action must be recorded as clean SVO
      recommended_action: DELETE adverb; bare "septon-rowan takes the stylus"

    - id: fault-006
      type: fault
      what: proto-line 43 — "septon-rowan blows the ink dry"
      why: >
        `dry` is a result-state adjective. The SVO spine prohibits adjectives. The result of the
        blowing action is a state change that belongs in a state-update facet, not in the proto-line
        as a modifier on the object.
      criteria: line must not carry a result-state adjective; the action must be recorded without the result-qualifier
      recommended_action: DELETE result adjective; bare "septon-rowan blows the ink"

    - id: fault-007
      type: fault
      what: proto-line 53 — "taylor-hebert-westeros watches septon-rowan"
      why: >
        `watches` is a perception verb (sustained visual observation). Parallel to the `scans` fault
        at line 12. The SVO spine prohibits perception verbs as POV-leaks. The physical act available
        here is the direction of the body/gaze, not the cognitive act of watching.
      criteria: line must record a concrete physical act rather than a perception-verb; the act of watching-as-such must be absent
      recommended_action: RECAST-PHYSICAL

    - id: fault-008
      type: fault
      what: proto-line 55 — "taylor-hebert-westeros turns back toward the bell tower"
      why: >
        `back toward the bell tower` is a compound prepositional modifier. `back` is an adverb; `toward
        the bell tower` is prepositional padding. Both are prohibited by the SVO spine. Destination
        information belongs in location-state citations.
      criteria: line must not carry directional adverbs or prepositional destination phrases
      recommended_action: DELETE modifiers; bare "taylor-hebert-westeros turns"

    - id: fault-009
      type: fault
      what: proto-line 57 — "taylor-hebert-westeros extends the network"
      why: >
        `the network` is not a physical named prop or observable entity — it is an abstract reference
        to Taylor's fauna-control capability scope. `extends the network` names a cognitive/ability
        activation, not a concrete physical act an observer could witness. The SVO spine requires
        verbs to be "concrete and physical — what an observer would see or hear." No observer sees
        Taylor extending a network; they see the subsequent raven behavior. This is a
        FAULT-FORM-INTERIORITY or FAULT-FORM-NON-ACTION-VERB — the verb acts on an abstract object
        that does not exist as an observable entity. Downstream facets (state-updates, vibes-updates)
        that cite this line will be anchored to an invisible event, which is not a valid citation base.
      criteria: line must record a concrete physical act on a named observable entity, or the ability activation must be removed and only its physical consequences (raven behavior) retained
      recommended_action: DELETE or RECAST-PHYSICAL

    - id: fault-010
      type: fault
      what: proto-line 58 — "the ravens lift in two groups"
      why: >
        `in two groups` is a prepositional phrase functioning as a manner modifier. The SVO spine
        prohibits prepositional padding. The grouping structure is implicit from subsequent lines
        (59, 60) and does not need to be carried in the spine.
      criteria: line must not carry a manner or grouping modifier; the lift event must be recorded as bare SVO
      recommended_action: DELETE modifier phrase; bare "the ravens lift"

    - id: fault-011
      type: fault
      what: proto-line 59 — "the first group crosses the north field"
      why: >
        `north` is an adjective modifying `field`. The SVO spine prohibits adjectives. Location
        specificity belongs in location-state citations.
      criteria: line must not carry an adjectival modifier on the object noun
      recommended_action: DELETE adjective; "the first group crosses the field" or location-state citation carries directional context

    - id: fault-012
      type: fault
      what: proto-line 60 — "the second group banks toward the Harrenhal road"
      why: >
        `toward the Harrenhal road` is a prepositional phrase. The SVO spine prohibits prepositional
        padding. `Harrenhal road` is a location-card feature; its reference belongs in location-state
        citations.
      criteria: line must not carry a prepositional destination phrase; "the second group banks" is the target form
      recommended_action: DELETE prepositional phrase

    - id: fault-013
      type: fault
      what: proto-line 61 — "taylor-hebert-westeros presses a fist to her temple"
      why: >
        `to her temple` is a prepositional phrase. The SVO spine prohibits prepositional padding.
        The target of the press is body-location context that belongs in a state-update or sensory-flags
        citation, not the proto-line.
      criteria: line must not carry a prepositional phrase; the pressing action must stand without location qualification
      recommended_action: DELETE prepositional phrase; "taylor-hebert-westeros presses a fist" or recast with body-part as object

    - id: fault-014
      type: fault
      what: proto-line 62 — "taylor-hebert-westeros presses the fist harder against the temple"
      why: >
        `harder` is a comparative adverb and `against the temple` is prepositional padding. Two
        simultaneous SVO spine violations. The comparative and the prepositional phrase are both
        prohibited.
      criteria: line must not carry a comparative adverb or prepositional phrase; the action must be recorded as clean SVO
      recommended_action: DELETE both modifiers; "taylor-hebert-westeros presses the fist"

    - id: fault-015
      type: fault
      what: proto-line 66 — "the courier mounts the road south"
      why: >
        `south` is a directional adverb modifying `mounts the road`. The SVO spine prohibits adverbs.
        Directional context belongs in location-state citations.
      criteria: line must not carry a directional adverb
      recommended_action: DELETE adverb; "the courier mounts the road"

    - id: fault-016
      type: fault
      what: proto-line 68 — "the ravens drop low over the road"
      why: >
        `low` is an adverb and `over the road` is prepositional padding. Two simultaneous SVO spine
        violations.
      criteria: line must not carry adverb or prepositional padding; "the ravens drop" is the target form
      recommended_action: DELETE both modifiers

    - id: fault-017
      type: fault
      what: proto-line 71 — "the courier reins the horse again"
      why: >
        `again` is a temporal adverb. The SVO spine prohibits adverbs.
      criteria: line must not carry a temporal adverb; bare "the courier reins the horse"
      recommended_action: DELETE adverb

    - id: fault-018
      type: fault
      what: proto-line 72 — "taylor-hebert-westeros pulls the second group wide"
      why: >
        `wide` is a directional/result adverb modifying the motion outcome. The SVO spine prohibits adverbs.
      criteria: line must not carry a directional or result adverb
      recommended_action: DELETE adverb; "taylor-hebert-westeros pulls the second group"

    - id: fault-019
      type: fault
      what: proto-line 73 — "the second group wheels north"
      why: >
        `north` is a directional adverb. The SVO spine prohibits adverbs.
      criteria: line must not carry a directional adverb
      recommended_action: DELETE adverb; "the second group wheels"

    - id: fault-020
      type: fault
      what: proto-line 74 — "the courier's horse turns a full circle"
      why: >
        `full` is an adjective modifying `circle`. The SVO spine prohibits adjectives.
      criteria: line must not carry an adjective on the object noun
      recommended_action: DELETE adjective; "the courier's horse turns a circle"

    - id: fault-021
      type: fault
      what: proto-line 77 — "taylor-hebert-westeros drives the first group at the road surface"
      why: >
        `at the road surface` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional phrase; "taylor-hebert-westeros drives the first group" is the target form
      recommended_action: DELETE prepositional phrase

    - id: fault-022
      type: fault
      what: proto-line 78 — "the ravens scatter across the track"
      why: >
        `across the track` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional phrase
      recommended_action: DELETE prepositional phrase; "the ravens scatter"

    - id: fault-023
      type: fault
      what: proto-line 84 — "taylor-hebert-westeros directs the first group onto the verge track"
      why: >
        `onto the verge track` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional destination phrase
      recommended_action: DELETE prepositional phrase; "taylor-hebert-westeros directs the first group"

    - id: fault-024
      type: fault
      what: proto-line 85 — "the courier leads the horse off the road"
      why: >
        `off the road` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional phrase
      recommended_action: DELETE prepositional phrase; "the courier leads the horse"

    - id: fault-025
      type: fault
      what: proto-line 86 — "the courier pauses at the verge"
      why: >
        `at the verge` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional location phrase
      recommended_action: DELETE prepositional phrase; "the courier pauses"

    - id: fault-026
      type: fault
      what: proto-line 87 — "taylor-hebert-westeros drives the first group lower along the track surface"
      why: >
        `lower` is a comparative adverb and `along the track surface` is prepositional padding. Two
        simultaneous SVO spine violations.
      criteria: line must not carry a comparative adverb or prepositional phrase
      recommended_action: DELETE both modifiers; "taylor-hebert-westeros drives the first group"

    - id: fault-027
      type: fault
      what: proto-line 88 — "the courier turns back toward Harrenhal"
      why: >
        `back toward Harrenhal` is compound directional padding (adverb + prepositional phrase).
        The SVO spine prohibits both.
      criteria: line must not carry directional adverbs or prepositional phrases
      recommended_action: DELETE modifiers; "the courier turns"

    - id: fault-028
      type: fault
      what: proto-line 90 — "the ravens lift clear"
      why: >
        `clear` is a directional/result adverb. The SVO spine prohibits adverbs.
      criteria: line must not carry a result adverb
      recommended_action: DELETE adverb; "the ravens lift"

    - id: fault-029
      type: fault
      what: proto-line 91 — "taylor-hebert-westeros spreads the second group across the approach mouth"
      why: >
        `across the approach mouth` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional phrase
      recommended_action: DELETE prepositional phrase; "taylor-hebert-westeros spreads the second group"

    - id: fault-030
      type: fault
      what: proto-line 92 — "the second group fans across the approach"
      why: >
        `across the approach` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional phrase; "the second group fans" is the target form
      recommended_action: DELETE prepositional phrase

    - id: fault-031
      type: fault
      what: proto-line 94 — "taylor-hebert-westeros drives the second group at the second courier"
      why: >
        `at the second courier` is a prepositional phrase. The SVO spine prohibits prepositional padding.
        Additionally, `the second courier` references an actor introduced with indefinite article in L93
        (see flag-001); the referent is consistent here but the upstream naming fault applies.
      criteria: line must not carry a prepositional phrase; "taylor-hebert-westeros drives the second group" is the target form
      recommended_action: DELETE prepositional phrase

    - id: fault-032
      type: fault
      what: proto-line 100 — "the gate guard speaks to the second courier"
      why: >
        `the gate guard` does not appear in the chapter-06 cast roster. The roster lists
        taylor-hebert-westeros, septon-rowan, and septon-dying-protector only. An unlisted actor
        performing a speech act (not a background environmental event) introduces a named agency that
        pass 5 continuity and downstream facets (dialogue) cannot anchor to any card. This is a
        FAULT-PHYSICAL-ACTOR-ABSENT.
      criteria: the speaking actor must either be a cast-listed slug or the line must be reconfigured so that the unlisted actor is not performing a named dialogue act
      recommended_action: RENAME-SLUG (add gate-guard to cast roster if intended, or recast as environmental sound without named actor)

    - id: fault-033
      type: fault
      what: proto-line 103 — "taylor-hebert-westeros drops to one knee"
      why: >
        `to one knee` is a prepositional phrase. The SVO spine prohibits prepositional padding.
      criteria: line must not carry a prepositional phrase
      recommended_action: DELETE prepositional phrase; "taylor-hebert-westeros drops"

    - id: fault-034
      type: fault
      what: proto-line 104 — "taylor-hebert-westeros presses both hands to the earth"
      why: >
        `both` is an adjective modifying `hands` and `to the earth` is a prepositional phrase.
        Two simultaneous SVO spine violations.
      criteria: line must not carry an adjective on the subject-body-part or a prepositional destination phrase
      recommended_action: DELETE both modifiers; "taylor-hebert-westeros presses the hands" or recast

    - id: fault-035
      type: fault
      what: proto-line 105 — "the ravens land along the bell tower"
      why: >
        `along the bell tower` is a prepositional phrase. The SVO spine prohibits prepositional padding.
        The bell tower is a fixed prop in the location card; its reference belongs in location-state
        citations.
      criteria: line must not carry a prepositional phrase; "the ravens land" is the target form
      recommended_action: DELETE prepositional phrase

    - id: flag-001
      type: flag
      what: proto-lines 65 and 93 — "a courier emerges through the Harrenhal postern" and "a second courier exits the postern"
      why: >
        Both lines use indefinite article (`a courier`, `a second courier`) rather than the schema's
        named-entity form `the <noun>`. Per the schema, subject must be "a named entity — actor slug,
        prop slug, or `the <noun>` for unnamed environment elements." `a courier` is first-introduction
        indefinite usage, which is natural prose convention but deviates from the `the <noun>` form
        the schema requires. The downstream lines (69–88, 94–99) correctly use `the courier` and
        `the second courier`. The inconsistency is at introduction only; all subsequent references
        are schema-compliant. Advisory: fixer may wish to normalize introduction lines to `the courier`
        and `the second courier` for strict schema compliance, though this is a flag not a fault.
      criteria: no fixer action required; editor may normalize at wrap if desired

    - id: flag-002
      type: flag
      what: proto-lines with prepositional destination phrases on motion verbs (lines 10, 52, 56, 65)
      why: >
        Lines 10 (`steps into the yard`), 52 (`steps into the lane`), 56 (`the ravens settle on the
        tower lip`), and 65 (`a courier emerges through the Harrenhal postern`) all carry prepositional
        destination phrases on motion verbs. These were passed in prior audit passes and have been
        treated as CORRECT in this reverification on the grounds that destination-of-motion (where a
        subject moves to) is different from adverbial manner-of-motion padding, and that a bare
        intransitive motion verb without destination would violate the FAULT-FORM-NO-VERB principle
        for verbs that require a landing-point to be physically meaningful. This pass does not fault
        these lines. However, the category is flagged for the tuning record: if the pipeline rubric
        is tightened to prohibit all prepositions, these lines would need recasting (e.g., `steps into
        the yard` → `the yard receives taylor-hebert-westeros`). The current ruling is that
        destination-prepositions on motion verbs are permitted when the destination is a named
        location-card feature and no other modifier is present.
      criteria: no action required; advisory for rubric clarification at pipeline promotion

  summary: >
    35 faults found. 2 flags. The file does not pass Pass 2 in its current state.
    The dominant fault class is FAULT-FORM-MODIFIER (directional adverbs, comparative adverbs,
    prepositional padding, and result-state adjectives), accounting for 42 violations across 33
    distinct lines (several lines carry 2 violations each). Two FAULT-FORM-PERCEPTION violations
    at lines 12 and 53. One FAULT-FORM-INTERIORITY / NON-ACTION-VERB at line 57. One
    FAULT-PHYSICAL-ACTOR-ABSENT at line 100.

    No constraint card violations found. cond-fauna-control-rules cost curve is correctly reflected
    (nosebleed at line 82 after sustained multi-group operation). No series law violations. No
    cond-westerosi-customary-authority or cond-series-tone-constraints violations.

    The fixer workload is high in volume but low in complexity: the large majority of faults require
    only deletion of trailing modifiers. Structural changes are limited to lines 57 (recast or delete),
    12 and 53 (recast as physical event), and 100 (cast roster addition or recast).

    CONTINUITY-OK: NO. Route to fixer.
