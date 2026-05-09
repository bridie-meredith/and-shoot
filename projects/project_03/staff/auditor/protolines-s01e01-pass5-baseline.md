## Summary
file-level: CONTINUITY-FAIL
faults:
  FAULT-STATE: 2
  FAULT-REFERENCE: 2
  FAULT-POV: 2
  FAULT-REACHABILITY: 0

---

```yaml
audit:
  scope: episode
  target: s01e01-proto-lines-baseline-naive
  timestamp: 2026-05-07
  verdict: CONTINUITY-FAIL
  findings:

    - id: fault-001
      type: fault
      class: FAULT-STATE-PROP-DANGLING
      what: line 19 — "Taylor takes out the septon's written letter and presents it"
      why: >
        No line in the sequence establishes that Taylor is carrying the letter before line 19.
        The letter appears in her hands without prior placement. If a trim removed an earlier
        placement beat, this is a dangling prop reference. As a pre-scene inventory item the
        fault is lower-severity, but the file provides no in-sequence evidence Taylor had it.
      criteria: >
        Either a line preceding line 19 must establish that Taylor is carrying or has retrieved
        the letter, or the letter must be confirmed as pre-scene inventory via a header note or
        explicit earlier beat so its appearance at line 19 is not unsupported.
      recommended_fixer_action: RE-ADD-PREDECESSOR

    - id: fault-002
      type: fault
      class: FAULT-STATE-TIME-INCONSISTENT
      what: lines 11 and 14 — internal contradiction on what questions were posed to other wards
      why: >
        Line 11 shows the officer working through all assembled wards asking "names and ages
        and blood-claims." Line 14 then asserts "The officer doesn't ask anyone else this
        question" immediately before line 15, where the officer asks Taylor for "her name and
        age and wardship." The wardship/blood-claim question at line 15 is the same category
        as the questions posed in line 11 to all wards. Line 14's assertion directly contradicts
        line 11. The singling-out observation belongs with line 27 (the "assessed before"
        question), not here. A downstream reader of the proto-line sequence cannot reconcile
        lines 11 and 14 without one of them being wrong.
      criteria: >
        Line 14 must not assert that the question at line 15 is unique to Taylor when line 11
        already shows that question was posed to all wards. The singling-out observation (if
        retained) must attach only to the question that was demonstrably not asked of other
        wards — i.e., the clerk's "assessed before" query at line 27.
      recommended_fixer_action: DELETE or REORDER

    - id: fault-003
      type: fault
      class: FAULT-REFERENCE-CAST-SLUG
      what: line 16 — "Septon Osmynd holds her wardship"
      why: >
        The active location card (loc-harrenhal-sept-environs) names the septon as "Septon
        Aldric." The series cast roster uses the slug septon-dying-protector, with the
        location card as the canonical name authority. The name "Osmynd" does not appear in
        any loaded card or roster. This is a name mismatch against the location card authority;
        if the septon's canonical name is Aldric, any dialogue reference to him must use that
        name or a valid alias established in his card.
      criteria: >
        The septon's name in line 16 must match the canonical name established in his card
        (currently "Aldric" per loc-harrenhal-sept-environs). If "Osmynd" is the intended
        canonical name, the location card must be updated as the authority; the proto-line
        file cannot be the authority for a name that conflicts with an existing card.
      recommended_fixer_action: RENAME-SLUG

    - id: fault-004
      type: flag
      class: FAULT-REFERENCE-LOCATION-INVALID
      what: line 1 — "The morning is bright on the sept flagstones"
      why: >
        The active location card (loc-harrenhal-sept-environs) describes the exterior yard as
        "Hard-packed earth," not flagstones. The sept interior has a cracked stone floor, but
        the sequence takes place in the courtyard/yard. "Flagstones" is inconsistent with the
        location card's sensory authority for the exterior space. This is a flag rather than a
        fault because it is a sensory-vocabulary inconsistency, not a structural location error,
        but it should be reconciled before final draft.
      why: >
        If a later facet or studio pass uses the location card as ground truth for sensory
        detail, "flagstones" will conflict with "hard-packed earth" and require a correction
        at that stage.

    - id: fault-005
      type: fault
      class: FAULT-POV-LEAK
      what: line 28 — "Taylor knows this question was put to no other ward"
      why: >
        "Knows" is a cognition/perception verb applied to the narrator (taylor-hebert-westeros).
        The file's POV contract requires narrator perception to be externally observable or
        action-expressed; internal certainty claims ("knows") are a POV leak. Taylor can observe
        that the clerk did not ask this of other wards — but "knows" asserts internal epistemic
        state rather than observed fact.
      criteria: >
        Line 28 must express the singling-out observation as something Taylor can externally
        perceive or deduce from observable behavior, not as an internal certainty claim.
      recommended_fixer_action: REWRITE-AS-OBSERVABLE

    - id: fault-006
      type: fault
      class: FAULT-POV-LEAK
      what: line 33 — "Taylor feels the moment the window closes"
      why: >
        "Feels" is a perception/sensation verb applied to the narrator. Internal emotional or
        phenomenological states expressed through "feels" constitute a POV leak under the
        harsh-SVO / narrator-consistency contract. This line assigns an affective interior
        experience to Taylor that is not action or observable behavior.
      criteria: >
        Line 33 must express the closing-window beat as observable action or external state
        rather than as Taylor's felt interior experience.
      recommended_fixer_action: REWRITE-AS-OBSERVABLE
```
