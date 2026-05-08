audit:
  scope: episode
  target: chapter-07 (proto-lines post-fixer)
  timestamp: 2026-05-07
  pass: 2 — constraint audit (re-run)

summary:
  total_content_lines: 83
  blank_timeskip_lines: 9  # IDs 16, 28, 35, 42, 51, 67, 72, 82, 85
  correct: 66
  fault_form: 16
  fault_physical: 1
  flag: 1
  fault_constraint: 0

findings:

  - id: fault-001
    type: fault
    what: line 2 — `the recorder scans Rowan's filing`
    why: >
      "scans" is a perception verb (reads, reviews, examines document content — naming an interior cognitive act
      rather than an observable physical event). Falls under the "or other POV-leak verb" catchall in the
      FAULT-FORM-PERCEPTION class. The recorder's review of the document is not observable as a discrete physical
      motion by an outside witness. Downstream: facet authors have no physical anchor to cite; dialogue and
      state-update facets have nothing to hang on.
    fault_class: FAULT-FORM-PERCEPTION
    criteria: >
      Line must record the observable physical event, not the cognitive act of reading. Recast as the discrete
      physical act the recorder performs (e.g., opening the filing, running a finger down the page) or split
      into a physical handling beat. No perception verb may survive.
    recommended_action: RECAST-PHYSICAL

  - id: fault-002
    type: fault
    what: line 4 — `taylor-hebert-westeros leans against the counter`
    why: >
      "leans against the counter" names a sustained positional state, not the initiation of a discrete
      physical act. "Leans" here is stative position-naming (parallel to flagged uses of `sits`, `stands`,
      `lies`). The proto-line schema requires the verb to be the concrete physical act, not the resulting
      position. Downstream: the beat records a condition rather than an event; facets have no action to cite.
    fault_class: FAULT-FORM-NON-ACTION-VERB
    criteria: >
      Line must record the discrete act that initiates or terminates a positional state (e.g., the step
      to the counter, the shoulder-press into the counter surface). The achieved position is a state-update
      or location-state facet, not the proto-line body.
    recommended_action: RECAST-PHYSICAL

  - id: fault-003
    type: fault
    what: line 25 — `the recorder notes the cross-reference to Rowan's entry`
    why: >
      "notes" is an explicitly listed perception/cognitive-act verb (FAULT-FORM-PERCEPTION). It names the
      act of registering or recording a cognitive observation rather than a discrete physical event observable
      from the outside. The "cross-reference" is the administrative outcome; the physical act (writing a
      reference, adding a mark, drawing a line between entries) is elided. Downstream: dialogue and
      state-update facets cannot cite a physical beat that does not exist.
    fault_class: FAULT-FORM-PERCEPTION
    criteria: >
      Line must record the physical writing/marking act, not the notational-cognition act. Recast as the
      concrete physical motion the recorder makes (writes, marks, draws) with the cross-reference entry as
      the object. No "notes" or equivalent perception verb may survive.
    recommended_action: RECAST-PHYSICAL

  - id: fault-004
    type: fault
    what: line 37 — `taylor-hebert-westeros stops on the road`
    why: >
      "on the road" is a prepositional modifier attaching location context to the verb "stops." The brief
      prohibits prepositional padding; location context belongs in location-state facet citations, not in
      the proto-line body. The act (stops) is complete without the prepositional phrase.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Line must be stripped to subject-verb with no trailing prepositional location phrase. Location of the
      stop is a location-state facet concern.
    recommended_action: DELETE (prepositional tail); recast as `taylor-hebert-westeros stops`

  - id: fault-005
    type: fault
    what: line 38 — `taylor-hebert-westeros turns back toward Harrenhal`
    why: >
      "back toward Harrenhal" is a prepositional modifier on "turns." The direction of the turn is
      location/orientation context that belongs in a location-state or state-update facet, not the
      proto-line body. Two prepositional phrases compound the padding.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Line must be stripped to the discrete physical act with no prepositional direction qualifier.
      `taylor-hebert-westeros turns` is the legal form; directional context accrues in facets.
    recommended_action: DELETE (prepositional tail); recast as `taylor-hebert-westeros turns`

  - id: fault-006
    type: fault
    what: line 54 — `taylor-hebert-westeros sits at the table`
    why: >
      "sits at the table" names the achieved positional state rather than the discrete physical act of
      sitting down. "Sits" here is stative position-naming (the position, not the motion). Parallel to
      flagged uses of `stands`, `lies`. Downstream: no physical event to cite; the beat anchors nothing
      for dialogue or feeling facets.
    fault_class: FAULT-FORM-NON-ACTION-VERB
    criteria: >
      Line must record the physical act of seating (the lowering-into-chair event), not the resulting
      position. Recast as the initiation act (e.g., `taylor-hebert-westeros takes the chair`,
      `taylor-hebert-westeros drops into the chair`).
    recommended_action: RECAST-PHYSICAL

  - id: fault-007
    type: fault
    what: line 56 — `septon-rowan sets his satchel on the table`
    why: >
      "his" is a possessive determiner — a modifier on "satchel." The brief prohibits adjectives. Possessive
      determiners are adjective-class modifiers. "On the table" is also a prepositional location phrase
      (placement destination). Both are disallowed. Downstream: modifier creep propagates into downstream
      facets if not caught here.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Remove possessive determiner. Remove placement prepositional phrase. The prop-identity context (whose
      satchel, where it lands) accrues in facets. Legal form: `septon-rowan sets the satchel down` or
      `septon-rowan sets the satchel on the counter` — but the "on the counter/table" placement phrase is
      itself banned. Cleanest legal form: `septon-rowan sets the satchel down` with location facet
      handling the table placement.
    recommended_action: RECAST-PHYSICAL

  - id: fault-008
    type: fault
    what: line 61 — `septon-rowan opens his satchel`
    why: >
      "his" is a possessive determiner — modifier on "satchel." Same class as fault-007.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Remove possessive determiner. Legal form: `septon-rowan opens the satchel`.
    recommended_action: DELETE (modifier only; minimal recast)

  - id: fault-009
    type: fault
    what: line 64 — `taylor-hebert-westeros sets the document on the table`
    why: >
      "on the table" is a prepositional placement phrase. Location of prop placement belongs in
      location-state facet, not the proto-line body.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Strip to `taylor-hebert-westeros sets the document down`. Placement destination accrues in facets.
    recommended_action: DELETE (prepositional tail)

  - id: fault-010
    type: fault
    what: line 68 — `a raven launches from the bell tower`
    why: >
      "from the bell tower" is a prepositional phrase specifying the launch origin. Origin location context
      belongs in location-state facet citation, not the proto-line body.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Strip to `a raven launches`. Origin location accrues in facets.
    recommended_action: DELETE (prepositional tail)

  - id: fault-011
    type: fault
    what: line 70 — `taylor-hebert-westeros stops at the garden wall`
    why: >
      "at the garden wall" is a prepositional location phrase on "stops." Same pattern as fault-004.
      Location context belongs in location-state facets.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Strip to `taylor-hebert-westeros stops`. Wall-arrival context accrues in facets.
    recommended_action: DELETE (prepositional tail)

  - id: fault-012
    type: fault
    what: line 71 — `taylor-hebert-westeros grips the top of the garden wall`
    why: >
      "of the garden wall" is a prepositional phrase modifying the object "top." The object identification
      chain (top-of-the-garden-wall) adds prepositional padding to name what "top" refers to. Location
      context for which surface is gripped belongs in facets.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Simplify object to a single named entity without trailing prepositional chain. If "the wall" is
      sufficient to identify the object, use `taylor-hebert-westeros grips the wall`. If the top-surface
      specificity is load-bearing for downstream facets, it should be established in location-state, not
      embedded in the proto-line as a prepositional chain.
    recommended_action: DELETE (prepositional chain on object)

  - id: fault-013
    type: fault
    what: line 83 — `the recorder adds a notation to Plumm's entry`
    why: >
      "to Plumm's entry" is a prepositional destination phrase. Destination context belongs in facets.
      Additionally, "Plumm's" is a possessive modifier on "entry." Two modifier violations compound.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Strip prepositional destination phrase and possessive modifier. The physical act of writing/adding
      is the legal core. Recast toward: `the recorder writes a notation` or `the recorder adds a notation`
      with destination context in location-state/state-update facets. The possessive identifying which
      entry is modified is facet-level context.
    recommended_action: DELETE (prepositional tail and possessive)

  - id: fault-014
    type: fault
    what: line 88 — `taylor-hebert-westeros kneels at the altar`
    why: >
      "at the altar" is a prepositional location phrase. Location context belongs in facets.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Strip to `taylor-hebert-westeros kneels`. Altar-position context accrues in facets.
    recommended_action: DELETE (prepositional tail)

  - id: fault-015
    type: fault
    what: line 89 — `taylor-hebert-westeros rises from the altar`
    why: >
      "from the altar" is a prepositional origin phrase. Origin context belongs in facets.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Strip to `taylor-hebert-westeros rises`. Origin context accrues in facets.
    recommended_action: DELETE (prepositional tail)

  - id: fault-016
    type: fault
    what: line 91 — `taylor-hebert-westeros crosses to the sept door`
    why: >
      "to the sept door" is a prepositional destination phrase. The brief prohibits prepositional padding;
      destinations belong in facets. Compare with CORRECT uses of destination-as-object (e.g., "crosses
      the yard" where "the yard" is the grammatical object of "crosses" not a prepositional phrase).
      "Crosses to the sept door" uses the preposition "to" before the destination, placing it in
      prepositional phrase structure rather than direct object structure.
    fault_class: FAULT-FORM-MODIFIER
    criteria: >
      Recast destination as direct object rather than prepositional phrase, or strip. Legal form:
      `taylor-hebert-westeros crosses the sept door` (if the door is what is being crossed to) or
      restructure so the destination is the grammatical object without the "to" preposition.
    recommended_action: RECAST-PHYSICAL

  - id: fault-017
    type: fault
    what: >
      line 18 — `ser-harwick-plumm sets a document on the counter`;
      line 76 — `ser-harwick-plumm produces the claim document`
    why: >
      Ser-harwick-plumm's state file records inventory as empty at chapter-07 open. The document he
      files (lines 18, 76) is not listed in his inventory. A prop that is not in an actor's inventory
      and is not established on the set at episode-open cannot appear in the actor's hands without
      a prior placement beat. No prior beat in this file establishes Plumm receiving or carrying
      this document. The chapter plan confirms his filing action, but the state file is the physical
      record of truth. Downstream: Pass 5 continuity will reject this as a state fault; fixer
      intervention now is cheaper.
    fault_class: FAULT-PHYSICAL-PROP-ABSENT
    criteria: >
      Ser-harwick-plumm must have a preceding beat in which he acquires or is shown carrying the
      claim document before he can set it down or produce it. Either: (a) add an inventory-establishment
      beat before his entry (line 17) — e.g., a beat outside the recorder's room where he carries the
      document — or (b) confirm with state manager that his inventory was not updated at session-close
      and add the document to his episode-open inventory. The document must be traceable to a recorded
      source before it appears in his hands.
    recommended_action: RECAST-PHYSICAL (add prior inventory beat or update state)

  - id: flag-001
    type: flag
    what: >
      Lines 17, 24, 25, 26, 27, 43, 44, 45, 46, 47, 48, 49, 50 — repeated reference to "the recorder's room"
      as the scene location
    why: >
      The active warehouse location cards for this project are `loc-harrenhal-sept-environs` and
      `loc-harrenhal-exterior`. The recorder's room is an interior Harrenhal space referenced throughout
      chapter-07 but has no corresponding `loc-*.card.md` in the active warehouse. The exterior card
      documents the outer ward and postern gate at surface level; it does not define interior rooms,
      their fixed props, or their exits. This is not a proto-line form fault — the lines themselves
      use "the recorder's room" as a valid `the <noun>` unnamed environment element — but the absence
      of a location card means physical-possibility checks for this scene cannot be fully grounded.
      Pass 5 continuity audit will also lack a physical-possibility reference for this space.
      Editor note: a location card for the recorder's room (or a section added to the Harrenhal
      exterior card covering interior administrative spaces) would close this gap before Pass 5.
    why_no_fault: >
      Pass 2 physical checks require that props named must be on the active set per location cards or
      in actor inventories. The proto-lines do not name specific props within the recorder's room that
      are unattested; they reference the room itself as a named space. The room's existence within
      Harrenhal is consistent with the exterior card's administrative framing and the chapter plan's
      chunk description. Escalating to fault would be overcalibrated at this pass. Flagged for Pass 5
      and for the location-card author.
