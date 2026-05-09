```yaml
audit:
  scope: episode
  target: chapter-03 proto-lines (post-fixer re-verification)
  timestamp: 2026-05-07
  run: pass-2-reverify (fresh fork)
  verdict: FAIL

  summary:
    total_lines: 119
    blank_timeskip_lines: 11
    numbered_content_lines: 108
    correct: 93
    fault_count: 15
    flag_count: 3
    fault_breakdown:
      FAULT-FORM-MODIFIER: 9
      FAULT-CONSTRAINT-cond-fauna-control-rules: 6

  findings:

    # ── FORM FAULTS ────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: "line 67 — `the steward produces the daily administrative summary`"
      why: >
        Object phrase contains two adjective modifiers: "daily" and "administrative."
        Per SVO discipline, no adjectives are permitted anywhere in the line.
        Modifier-laden object names corrupt downstream shape and stitcher decisions
        by embedding descriptive content that belongs in state-update or loc-state facets.
      criteria: >
        Object must be a bare noun or established prop slug with no inline adjective
        modifiers. "The daily administrative summary" must be reduced to a slug or
        bare noun (e.g., `the summary scroll`, `the administrative summary` is still
        two adjectives — needs reduction to one noun or a prop slug).
      recommended_action: RENAME-SLUG

    - id: fault-002
      type: fault
      what: "line 68 — `oc-castellan-harrenhal takes the daily administrative summary`"
      why: >
        Same object phrase as fault-001. "Daily" and "administrative" are adjective
        modifiers on the object. Same downstream consequence.
      criteria: >
        Object must match the resolved slug or bare noun from fault-001's fix.
        All four occurrences of this prop name must resolve to the same bare reference.
      recommended_action: RENAME-SLUG

    - id: fault-003
      type: fault
      what: "line 69 — `oc-castellan-harrenhal traces the daily administrative summary`"
      why: >
        Same object phrase. Third occurrence of the adjective-modifier violation
        on this prop.
      criteria: >
        Same as fault-001. Object must match the clean slug resolved across this block.
      recommended_action: RENAME-SLUG

    - id: fault-004
      type: fault
      what: "line 72 — `the steward takes the daily administrative summary`"
      why: >
        Fourth and final occurrence of the modified prop phrase. Same violation.
      criteria: >
        Same as fault-001.
      recommended_action: RENAME-SLUG

    - id: fault-005
      type: fault
      what: "line 82 — `oc-castellan-harrenhal traces the first anomaly entry`"
      why: >
        Object phrase contains the ordinal adjective "first" modifying "anomaly entry."
        Ordinals are adjectives and are forbidden. The distinction between first/second/
        third anomaly entries is narrative content that belongs in a state-update or
        dialogue facet citing these proto-lines, not in the SVO bone itself.
      criteria: >
        Object must be `the anomaly entry` without ordinal modifier. If three distinct
        anomaly-entry beats are load-bearing, they must be three proto-lines each
        referencing `the anomaly entry` (the sequence ordering is carried by ID
        monotonicity, not by inline modifiers).
      recommended_action: RECAST-PHYSICAL

    - id: fault-006
      type: fault
      what: "line 83 — `oc-castellan-harrenhal traces the second anomaly entry`"
      why: >
        Ordinal adjective "second" on the object. Same violation as fault-005.
      criteria: >
        Same as fault-005. Object: `the anomaly entry`.
      recommended_action: RECAST-PHYSICAL

    - id: fault-007
      type: fault
      what: "line 84 — `oc-castellan-harrenhal traces the third anomaly entry`"
      why: >
        Ordinal adjective "third" on the object. Same violation as fault-005.
      criteria: >
        Same as fault-005.
      recommended_action: RECAST-PHYSICAL

    - id: fault-008
      type: fault
      what: "line 85 — `oc-castellan-harrenhal traces the recurring-figure notation`"
      why: >
        "Recurring-figure" is a compound adjective modifier on "notation." The
        hyphenated compound describes the notation rather than naming it. The
        SVO bone must not carry descriptive content about what the notation says.
      criteria: >
        Object must be reduced to a bare noun: `the notation` or an established
        prop slug. Descriptive content about what the notation records belongs
        in a downstream facet.
      recommended_action: RENAME-SLUG

    - id: fault-009
      type: fault
      what: "line 96 — `taylor-hebert-westeros releases the chin hold`"
      why: >
        "Chin" is an adjective modifier on "hold." `the chin hold` is a descriptive
        phrase, not a slug. The SVO bone cannot carry modifier-qualified object names.
        Note: the licensed-hold form (body-part-as-object) applies to `holds the chin`
        (body part as object), not to `the chin hold` as a modified-noun object.
        This release beat should mirror the hold form: `releases the chin` not
        `releases the chin hold`.
      criteria: >
        Recast to `taylor-hebert-westeros releases the chin` or equivalent bare form
        that names the body part as the direct object, not a modified compound noun.
      recommended_action: RECAST-PHYSICAL

    # ── CONSTRAINT FAULTS ──────────────────────────────────────────────

    - id: fault-010
      type: fault
      what: >
        Lines 11–27 (plumms-man scroll-completion / records-hall delivery block):
        lines 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27
      why: >
        File header declares `narrator: taylor-hebert-westeros`. These lines depict
        events occurring inside plumms-man's study (scroll completion) and inside
        Harrenhal's records hall (delivery and logging). Harrenhal's outer walls are
        half a league (~2.5 km) from the sept environs, per loc-harrenhal-exterior
        and loc-harrenhal-sept-environs cards. Taylor's maximum fauna-control range
        under extreme focus is 600 meters (cond-fauna-control-rules). She cannot
        reach Harrenhal via fauna-sense from the sept. She is not physically present
        at these locations. No fauna-feed beat in the file establishes a raven or
        rat as a relay observer inside Harrenhal for this block.

        A proto-line file with `narrator: taylor-hebert-westeros` asserts Taylor-POV
        access to every observable event it records. These lines assert events she
        cannot physically or fauna-sense observe. This violates cond-fauna-control-rules
        (range hard ceiling) and the narrator-header contract.

        Downstream consequence: facet authors (dialogue, state-updates, narrator-interest)
        will cite these lines as Taylor-accessible beats and produce POV-violating facet
        content. The corruption is systematic, not line-local.
      criteria: >
        One of two resolutions must be achieved before this block can pass:
        (A) The narrator header is changed to a non-Taylor slug (e.g., an omniscient
        or plumms-man narrator) for this chapter, and the chapter is split or reframed
        to reflect that structural choice; OR
        (B) A fauna-feed relay mechanism is established — prior beats must show Taylor
        dispatching a raven or deploying a rat into Harrenhal range before this block
        begins, with a fauna-control-rules cost beat accompanying it, and the range
        problem must be resolved (noting that 2.5 km exceeds even the 600m maximum).
        Resolution (B) is physically blocked by the range ceiling; resolution (A)
        is the viable path unless the chapter location is changed so these events
        occur within Taylor's range.
      recommended_action: RECAST-PHYSICAL

    - id: fault-011
      type: fault
      what: >
        Lines 33–57 (ser-harwick-plumm outer-ward and records-hall block):
        lines 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57
      why: >
        Same range/narrator violation as fault-010. These events occur in Harrenhal's
        outer ward and records hall. Taylor is in the sept loft during this block
        (confirmed by the flanking loft-hold beats at lines 29–30 and 61–63).
        Harrenhal is half a league from the sept — beyond her 600m maximum range.
        No fauna relay is established in the file for this block.
      criteria: >
        Same as fault-010. The resolution must address the entire multi-block
        inaccessibility pattern, not each block individually.
      recommended_action: RECAST-PHYSICAL

    - id: fault-012
      type: fault
      what: >
        Lines 65–94 (oc-castellan-harrenhal antechamber / second records-hall block):
        lines 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82,
        83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94
      why: >
        Same range/narrator violation as faults 010–011. These events occur in
        Harrenhal's antechamber and records hall. Taylor remains at or near the sept
        during this block. Range ceiling from cond-fauna-control-rules is not met.
        This is the largest inaccessible block in the file (28 lines) and the one
        that most directly drives the chapter goal ("the damage is in writing").
        Paradoxically, the chapter goal depends on Taylor *not knowing* these events
        — which makes the Taylor-narrator framing structurally contradictory: she
        cannot know, and the file presents these events as knowable proto-lines in
        her POV file.
      criteria: >
        Same as fault-010. The contradiction between the chapter goal ("she has not
        yet been told") and the narrator-header contract ("these are Taylor-observable
        beats") must be resolved structurally. The most direct resolution is to
        change the narrator header to reflect that this chapter is not Taylor-POV
        for its Harrenhal sequences — and to establish what narrator does operate
        for those sequences.
      recommended_action: RECAST-PHYSICAL

    - id: fault-013
      type: fault
      what: >
        Lines 100–101 — `plumms-man exits the postern gate` / `plumms-man walks
        the south road`
      why: >
        Plumms-man is now moving south on the road toward the sept. These lines
        occur after the castellan has reviewed the scroll (line 86–89 block).
        The narrator is Taylor at the sept. Is plumms-man within Taylor's range
        on the south road? The south road from Harrenhal to the sept is half a
        league. As plumms-man walks south, he eventually enters Taylor's range —
        but at line 100 (postern gate exit) he is still at Harrenhal, which is
        beyond 600m. At line 101 (walks the south road), his position is undefined
        mid-transit. Neither line specifies his position relative to Taylor's range.

        Under cond-fauna-control-rules, Taylor can observe plumms-man only once he
        comes within ~200m (normal load) range of her. Lines 100–101 show him
        departing Harrenhal, which is still beyond that threshold. The file does not
        establish that Taylor has detected or observed him yet.
      criteria: >
        Lines 100–101 must either: (A) be removed from the Taylor-narrator file and
        assigned to whatever narrator covers the Harrenhal sequences (per the
        fault-010 structural resolution); OR (B) be relocated in the sequence to
        a point where plumms-man has entered Taylor's observable range, with an
        establishing beat showing her fauna-sense detecting his approach.
      recommended_action: RECAST-PHYSICAL

    # ── FLAGS ──────────────────────────────────────────────────────────

    - id: fault-014
      type: flag
      what: "lines 31 and 63 — `blood marks the lip` (appears twice)"
      why: >
        "Marks" is borderline between a physical-event verb and a state-assertion
        verb. An observer sees blood appearing on the lip; "marks" captures that.
        However, under strict SVO, a state-result ("blood marks" = blood is now
        visible on / has left a mark on) is closer to a copula-adjacent assertion
        than a discrete action. If the intent is the physical act of blood appearing,
        a more clearly action-form might be `blood reaches the lip` or `blood breaks
        at the lip`. Not a blocking fault at pass-2; flagged for pass-3 shape review
        to determine if the verb should be crisper.
      criteria: ~

    - id: fault-015
      type: flag
      what: "line 49 — `ser-harwick-plumm bends over the ledger`"
      why: >
        "Over the ledger" is a directional prepositional phrase. Under maximum
        strictness, directional prepositions that specify spatial relationship
        rather than being the verb's sole argument qualify as prepositional padding.
        Mitigating factor: `bends` without a directional argument is ambiguous
        (bends what?). The phrase functions as the complete action unit. Borderline
        — not a blocking fault but flagged for pass-3 review if shape pass wants
        stricter SVO on this actor's physical beats.
      criteria: ~

    - id: fault-016
      type: flag
      what: >
        Lines 13 and 98 — `plumms-man marks the recurring-figure notation` (line 13)
        and `the loft boards creak` (line 98)
      why: >
        Line 13: "recurring-figure" is a compound modifier on "notation" — same
        issue as fault-008 (line 85), but in plumms-man's study block, which is
        flagged for constraint issues (fault-010) anyway. If the constraint fault
        is resolved and this block survives, line 13 will need the same modifier
        repair as fault-008. Noting here to ensure the modifier fault is not missed
        if the block is restructured rather than deleted.

        Line 98: `the loft boards creak` — clean SVO, no fault. Noted positively:
        this is the correct fauna-feed / environment-event form for a physical
        observable. Included here only to confirm it was evaluated.
      criteria: ~
```
