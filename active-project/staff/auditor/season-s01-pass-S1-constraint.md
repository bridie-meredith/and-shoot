```yaml
audit:
  scope: season
  target: s01
  timestamp: 2026-05-09
  pass: FAIL
  fault_count: 2
  flag_count: 5
  findings:

    - id: fault-001
      type: fault
      what: >
        Insert-at bone ID 916 (`# insert-at: 48 — shape-001`):
        `the fly settles at the mordant-beam joint`
      why: >
        The phrase `at the mordant-beam joint` is a prepositional phrase of place,
        which is explicitly banned (FAULT-FORM-MODIFIER) under the harsh-SVO discipline
        and proto-line schema §SVO discipline. Inserted bones carry the same schema
        obligations as authored bones. The prepositional phrase routes placement to the
        proto-line rather than to a loc-state facet citation. This bone was not in the
        Phase 2 Pass 2 convergence set; it entered at insert time and escaped prior audit.
      criteria: >
        The bone must resolve to a clean SVO with no prepositional phrase of place.
        Acceptable resolutions include dropping the location phrase entirely (`the fly
        settles`) and letting loc-state carry placement, or using a transitive verb that
        takes the surface as direct object without a preposition (`the fly lands the
        mordant-beam joint`), provided `lands` is defensible as a transitive taking a
        surface object. Fixer chooses the minimum change that removes the preposition.

    - id: fault-002
      type: fault
      what: >
        ID 909: `the ferryman receives the folio` — appearing after the established
        possession chain: ID 893 (maester draws folio), ID 894 (maester passes ferryman
        the folio), ID 895 (ferryman takes the folio), ID 898 (ferryman grips the folio),
        ID 906 (the ferry folio crosses the water).
      why: >
        The ferryman already took and gripped the folio at IDs 895 and 898. ID 906
        renders the folio in transit on the ferry. ID 909 then depicts the ferryman
        receiving the folio again — a second possession transfer with no intervening
        release beat. As proto-lines, these constitute a possession continuity fault:
        the ferryman cannot receive an object he demonstrably already holds. The insert-at
        bone 923 (`the town reeve passes the maester the folio`) correctly closes the
        earlier possession gap (IDs 809→893); no equivalent closing bone exists for the
        ferryman's duplicate receipt. If ID 909 was intended to represent a different
        party receiving the folio from the ferryman at the far bank, the subject is wrong.
      criteria: >
        The possession state of the folio must be coherent across IDs 893–909. Either
        ID 909 must be deleted (the ferryman's receipt is already established at ID 895
        and the folio's transit is established at ID 906), or if ID 909 intends a
        new recipient at the far bank of the river, the subject must be a different
        actor slug (not `the ferryman`) and an intervening release beat for the ferryman
        must exist. Fixer resolves with minimum change — deletion of ID 909 is the
        simplest path if no second recipient is required by the beat sequence.

    - id: flag-001
      type: flag
      what: >
        IGNITION beat aftermath: IDs 502–519 (post-swarm sequence following the
        animal-pen flies event at IDs 455–480). Taylor's physical cost from the
        involuntary swarm is absent from the proto-line bones. The sequence shows:
        jaw clench (ID 504), exhale (ID 505), speaking (ID 507), being drawn away
        (ID 508), and a multi-beat time-skip (IDs 509–513) before the lane-facing
        beat (ID 518).
      why: >
        Per `cond-fauna-control-rules`, involuntary activation is "slightly more
        costly than deliberate controlled use at the same duration." At age ~9, even
        a sub-two-minute involuntary swarm has a cost signal. The card confirms
        recovery within hours, so the cost need not be severe — but some physical
        signal (temples, breath, physical degradation) is required to maintain the
        established cost curve. The time-skips (IDs 509–513) could absorb this if
        facet authors render it there, but no proto-line bone anchors the cost event
        for facet citation. Editor and facet authors should note this gap. No fixer
        action required unless Phase 4 split identifies a structural problem.

    - id: flag-002
      type: flag
      what: >
        `the maester` slug usage throughout networked-surveillance beat (IDs 802–897).
        Season plan section G names the slug `oc-maester-traveler`; the aggregate
        renders him as `the maester` (unnamed-element `the <noun>` form).
      why: >
        Per proto-line schema, `the <noun>` form is permitted for unnamed environment
        elements. Season plan explicitly designates `oc-maester-traveler` as a walk-on
        who "does not join the series cast roster," which supports the `the <noun>`
        form. However, if downstream facet authoring or Phase 4 split requires
        actor-slug references for this character's dialogue beats, the `the maester`
        form creates an unresolvable reference — dialogue files need a slug, not a
        descriptive noun. Facet authors will need a resolution convention before
        authoring dialogue for IDs 834, 839, 845, 850, 852, 855, 858, 862, 868, 874,
        880. No proto-line fault; flag for Phase 4 split and facet dispatch.

    - id: flag-003
      type: flag
      what: >
        ID 334: `a mounted man leads the column` and insert-at bone ID 914
        (`# split-from: 334`): `a mounted man follows the column`. Both use the
        slug form `a mounted man` but describe opposite positions in the retinue.
      why: >
        If the stitcher treats `a mounted man` as the same unnamed actor across both
        bones, the resulting prose has a single figure simultaneously leading and
        following the column — a physical contradiction. The `split-from: 334`
        comment suggests ID 914 is a bone split off from what was originally one
        compound ID 334, implying two different mounted men. But the `a <noun>` form
        does not distinguish them. Facet authors authoring against IDs 334 and 914
        in the same episode will need a disambiguation convention (e.g., `the lead
        rider` vs. `a mounted man` or indexed forms). No schema fault; flag for Phase
        4 split to resolve before facet dispatch.

    - id: flag-004
      type: flag
      what: >
        ID 421: `the garrison man faces the square`. The slug `the garrison man`
        appears only at this ID and has no prior appearance in the aggregate.
      why: >
        The IGNITION beat begins at approximately ID 421 with `the garrison man`
        already present. Per `cond-suppression-policy-progression`, the collection
        event features the collector's retinue (collector, collector's men, weighing
        apparatus). A garrison man's presence implies a standing local garrison
        member, distinct from the lord's traveling retinue. The aggregate does not
        establish this actor before ID 421, so the stitcher has no position or
        backstory anchor. Low severity — the `the <noun>` form is licensed and the
        character is minor — but facet authors should note the cold-entry.

    - id: flag-005
      type: flag
      what: >
        ID 290: `oc-child-peer points the cart`. The verb `points` with `the cart`
        as direct object.
      why: >
        `points` as a transitive verb with an inanimate object is a physical gesture
        (indicating action). It is not on the perception-verb deny-list and passes
        the SVO mechanical check. However, the semantic of pointing is inherently
        communicative/demonstrative rather than purely physical, and the verb form
        `points the cart` (rather than `points at the cart` which would be
        FAULT-FORM-MODIFIER) is slightly unusual. The line survives schema review
        but the stitcher will need to render it as a pointing gesture rather than a
        manipulation action. Editor advisory only.
```
