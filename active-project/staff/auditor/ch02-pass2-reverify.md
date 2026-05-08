audit:
  scope: episode
  target: active-project/theater/proto-lines/chapter-02.md
  timestamp: 2026-05-07
  pass: 2 (constraint audit — re-verification after fixer)
  verdict: FAIL
  summary:
    total_lines_reviewed: 97
    blank_timeskip_lines: 4 (28, 49, 79, 95)
    correct: 70
    fault_count: 27
    fault_by_class:
      FAULT-FORM-MODIFIER: 19
      FAULT-FORM-NON-ACTION-VERB: 2
      FAULT-FORM-NEGATION: 2
      FAULT-PHYSICAL-ACTOR-ABSENT: 2 (one structural slug, one missing card)
      FAULT-FORM-MODIFIER+NEGATION combined: 2 (lines 89, 91 counted in both classes above)
  header_check: PASS (narrator slug in cast roster; goal present and non-empty)

findings:

  - id: fault-001
    type: fault
    what: >
      Line 2: "plumms-man mounts the road south"
      "south" is an adverb modifying the action of mounting.
    why: Adverbial modifiers are banned per SVO spine. Directional information belongs in a
      location-state facet citation, not on the proto-line. Survives into pass 3 as a shape-
      corrupting artifact.
    criteria: Line must name only the physical act and its object. Direction removed.
    recommended_action: RECAST — remove "south"

  - id: fault-002
    type: fault
    what: >
      Line 8: "the raven crosses the south field"
      "south" is an adjective modifying "field."
    why: Adjective modifier on the object. Named locations must be undecorated slugs or bare
      common nouns. "south field" is a named place but "south" is functioning as a descriptor,
      not a proper name used throughout.
    criteria: Object must be an unmodified location noun or registered slug.
    recommended_action: RECAST — "the field" or register "south-field" as a slug

  - id: fault-003
    type: fault
    what: >
      Line 9: "plumms-man reaches the first farmstead boundary"
      "first" is an ordinal adjective modifying "farmstead boundary."
    why: Ordinal modifiers are adjective modifiers banned by the no-modifier rule. If sequence
      tracking is load-bearing it belongs in a state-update facet or continuity note, not the
      proto-line.
    criteria: Object must be an unmodified noun. Ordinal removed.
    recommended_action: RECAST — "plumms-man reaches the farmstead boundary"

  - id: fault-004
    type: fault
    what: >
      Line 27: "plumms-man marks the ledger a second time"
      "a second time" is an adverbial modifier on the marking action.
    why: Frequency and sequence modifiers are banned. The fact that this is a second marking is
      continuity information; it belongs in a state-update facet citation, not the proto-line.
    criteria: Proto-line must contain only the SVO core. Modifier removed.
    recommended_action: RECAST — "plumms-man marks the ledger"

  - id: fault-005
    type: fault
    what: >
      Line 32: "plumms-man mounts the road again"
      "again" is an adverb modifying the mounting action.
    why: Same class as fault-004. Repetition information belongs downstream.
    criteria: Proto-line must contain only the SVO core. "again" removed.
    recommended_action: RECAST — "plumms-man mounts the road"

  - id: fault-006
    type: fault
    what: >
      Line 33: "plumms-man crests the low rise"
      "low" is an adjective modifying "rise."
    why: Adjective modifier on the object. Terrain descriptors belong in location-state facets.
    criteria: Object must be an unmodified noun.
    recommended_action: RECAST — "plumms-man crests the rise"

  - id: fault-007
    type: fault
    what: >
      Line 34: "plumms-man reaches the second location — the dead orchard boundary"
      "second" is an ordinal adjective; "dead" is an adjective on "orchard"; the em-dash clause
      is an appositional descriptor.
    why: Multiple modifier violations on a single line. The em-dash annotation pattern is a
      prose construction importing descriptor content that belongs in facets. "dead orchard
      boundary" contains two modifiers ("dead", implied structural "boundary" with "dead").
    criteria: Object must be unmodified. Em-dash clause removed. Single clean location noun.
    recommended_action: RECAST — "plumms-man reaches the orchard boundary" (or register "dead-orchard" as a location slug)

  - id: fault-008
    type: fault
    what: >
      Line 37: "three ravens settle the dead apple tree"
      "dead" is an adjective modifying "apple tree."
    why: Adjective modifier on the object. Terrain/flora descriptors belong in location-state.
    criteria: Object must be an unmodified noun.
    recommended_action: RECAST — "three ravens settle the apple tree"

  - id: fault-009
    type: fault
    what: >
      Line 40: "the ravens hold the branch"
      "holds" with a perch-surface as object in stative resting context. Ravens are resting on
      the branch; this is a position state, not a licensed holds-use. Licensed holds: body-part
      for stillness-against-pressure, or physical-object resisting external force. A branch is
      neither.
    why: FAULT-FORM-NON-ACTION-VERB. Stative position disguised as action verb. The holding
      describes ongoing resting state, not a discrete act. Downstream shape and trim agents
      will treat this as an action beat and miscalculate tension.
    criteria: Line must describe the discrete observable action (settling, perching, not moving)
      rather than the resulting stative position.
    recommended_action: RECAST — e.g. "the ravens do not flush" is negation (banned); recast as
      "the ravens settle the branch" (discrete landing action) if that beat is not already covered

  - id: fault-010
    type: fault
    what: >
      Line 45: "plumms-man marks the ledger a third time"
      "a third time" is an adverbial modifier.
    why: Same class as fault-004. Sequence tracking belongs in state-update facets.
    criteria: Proto-line must contain only the SVO core.
    recommended_action: RECAST — "plumms-man marks the ledger"

  - id: fault-011
    type: fault
    what: >
      Line 46: "plumms-man marks a fourth entry — date, location"
      "fourth" is an ordinal adjective; the em-dash clause "date, location" is a content
      descriptor appended to the object.
    why: Ordinal modifier plus em-dash annotation. Same class as fault-007 pattern.
    criteria: Object must be unmodified; em-dash annotation removed.
    recommended_action: RECAST — "plumms-man marks the entry"

  - id: fault-012
    type: fault
    what: >
      Line 52: "blood marks the lip"
      "marks" here does not describe a discrete physical act — it names the resulting state
      (blood is visible on the lip). The blood does not perform an action; it is present.
    why: FAULT-FORM-NON-ACTION-VERB. State assertion dressed as action. The proto-line records
      the physical event (nosebleed blood reaching the lip surface), which is a one-direction
      flow event, not a marking action performed by blood as agent. Downstream facet authors
      reading this line as an action beat will misattribute agency.
    criteria: Line must describe the discrete observable physical event (blood reaching, blood
      appearing) rather than a state-description in action-verb form. Alternatively, the prior
      action causing the blood's appearance should be the proto-line, not the state.
    recommended_action: RECAST — e.g. "blood reaches the lip" (flow event, not state) or DELETE
      if line 51/53 context makes it redundant

  - id: fault-013
    type: fault
    what: >
      Line 70: "plumms-man marks the girl's description"
      "girl's" is a possessive adjective modifying "description."
    why: Possessive modifier on the object. Under strict SVO rules modifiers of all kinds are
      banned. The object must be a bare noun or registered slug.
    criteria: Object must be unmodified. Possessive construction removed.
    recommended_action: RECAST — "plumms-man marks the description" (with referent established
      by prior proto-line context)

  - id: fault-014
    type: fault
    what: >
      Line 71: "plumms-man marks the location — mill hamlet road"
      The em-dash clause "mill hamlet road" is a content descriptor appended to the object.
    why: Same em-dash annotation pattern as fault-007 and fault-011. Content annotations belong
      in facets, not the proto-line.
    criteria: Em-dash clause removed; object is bare.
    recommended_action: RECAST — "plumms-man marks the location"

  - id: fault-015
    type: fault
    what: >
      Line 73: "the girl rounds the road bend"
      "road" modifies "bend."
    why: Adjective/compound-noun modifier on the object. Under strict reading "road bend" names
      a specific feature but "road" functions as a descriptor.
    criteria: Object must be unmodified or the compound must be registered as a location slug.
    recommended_action: RECAST — "the girl rounds the bend"

  - id: fault-016
    type: fault
    what: >
      Line 84: "plumms-man reaches Harrenhal's outer wall"
      "Harrenhal's" is a possessive; "outer" is an adjective modifying "wall."
    why: Double modifier on the object. "outer wall" contains an adjective; the possessive
      "Harrenhal's" further modifies. Named location elements must appear as registered slugs
      or bare nouns.
    criteria: Object must be a registered location slug or unmodified noun.
    recommended_action: RECAST — "plumms-man reaches the outer wall" (if "outer wall" is an
      established location element per loc-harrenhal-exterior) or "plumms-man reaches Harrenhal"

  - id: fault-017
    type: fault
    what: >
      Line 89: "plumms-man transcribes the first entry — grain shed, no vermin sign"
      "first" is an ordinal adjective; the em-dash clause contains "no vermin sign" which is a
      negation embedded in a descriptor annotation.
    why: FAULT-FORM-MODIFIER + FAULT-FORM-NEGATION. The em-dash annotation imports prose
      content (the entry's content) directly onto the proto-line, violating the bone-only
      contract. The negation "no vermin sign" additionally imports an absence-assertion.
      Downstream facet authors cannot distinguish proto-line from facet content when annotations
      are embedded.
    criteria: Ordinal and em-dash annotation removed. No negation on any proto-line. The
      ledger-entry content lives in a state-update or continuity facet, not the proto-line.
    recommended_action: RECAST — "plumms-man transcribes the entry"

  - id: fault-018
    type: fault
    what: >
      Line 90: "plumms-man transcribes the second entry — sparrow, unnatural turn"
      "second" is an ordinal adjective; the em-dash clause contains "unnatural" which is an
      adjective importing interpretive content.
    why: FAULT-FORM-MODIFIER. Ordinal plus interpretive adjective in annotation. "Unnatural
      turn" is an interpretive description of observed animal behavior — Plumm's man's
      assessment — which belongs in a narrator or feeling facet, not the proto-line.
    criteria: Ordinal and em-dash annotation removed.
    recommended_action: RECAST — "plumms-man transcribes the entry"

  - id: fault-019
    type: fault
    what: >
      Line 91: "plumms-man transcribes the third entry — ravens, orchard, no flush"
      "third" is an ordinal adjective; "no flush" is a negation embedded in the annotation.
    why: FAULT-FORM-MODIFIER + FAULT-FORM-NEGATION. Same pattern as fault-017.
    criteria: Ordinal and em-dash annotation removed. No negation.
    recommended_action: RECAST — "plumms-man transcribes the entry"

  - id: fault-020
    type: fault
    what: >
      Line 92: "plumms-man transcribes the fourth entry — girl, starlings, mill hamlet road"
      "fourth" is an ordinal adjective; em-dash clause is a content annotation.
    why: FAULT-FORM-MODIFIER. Same em-dash annotation pattern.
    criteria: Ordinal and em-dash annotation removed.
    recommended_action: RECAST — "plumms-man transcribes the entry"

  - id: fault-021
    type: fault
    what: >
      Line 93: "plumms-man transcribes the fifth entry — girl, bell tower raven, sept boundary"
      "fifth" is an ordinal adjective; em-dash clause is a content annotation.
    why: FAULT-FORM-MODIFIER. Same em-dash annotation pattern.
    criteria: Ordinal and em-dash annotation removed.
    recommended_action: RECAST — "plumms-man transcribes the entry"

  - id: fault-022
    type: fault
    what: >
      STRUCTURAL — slug "plumms-man" used as subject on approximately 40 lines (1, 2, 9, 10,
      11, 12, 13, 14, 15, 16, 22, 23, 25, 27, 32, 33, 34, 35, 36, 38, 39, 45, 46, 47, 48,
      55, 56, 57, 59, 60, 65, 69, 70, 71, 72, 74, 75, 77, 78, 84, 85, 87, 88, 89, 90, 91,
      92, 93, 94, 101).
      "plumms-man" does not appear in the series cast roster (showrunner/memory.md
      cast_roster), nor in the chapter-02-plan.md actors list. The chapter plan actors field
      names "ser-harwick-plumm"; the chunk text explicitly describes this character as "Ser
      Harwick Plumm's man" — a retainer, not Plumm himself. No oc-* card exists for this
      character in active-project/warehouse/.
    why: FAULT-PHYSICAL-ACTOR-ABSENT. An unregistered slug used as subject throughout the file
      cannot be resolved by downstream facet authors, the stitcher, or continuity checks. Pass
      5 will flag every one of these lines. The slug also breaks the cast-roster contract that
      every actor appearing in a proto-line resolves to an active actor card.
      If the character is intentional (Plumm's retainer as a real narrative figure), an oc-*
      card must be authored and the slug registered before this file can be locked. If the
      intent was to use ser-harwick-plumm as the observer, the slug must be corrected
      throughout.
    criteria: Either (a) an oc-* card for this character must be authored, the slug registered
      in the chapter cast, and all uses of the slug confirmed consistent; or (b) all
      occurrences of "plumms-man" must be replaced with "ser-harwick-plumm" if Plumm himself
      is the intended subject. Resolution before pass 3 advance.
    recommended_action: RENAME-SLUG (after card authoring) or RECAST to registered slug

  - id: fault-023
    type: fault
    what: >
      Line 58: "oc-girl-from-hamlet rounds the mill hamlet road edge"
      Subject slug "oc-girl-from-hamlet" — no card at
      active-project/warehouse/oc-girl-from-hamlet.card.md (file not found). The slug appears
      again in narrative reference ("the girl") on lines 61, 62, 63, 64, 73.
    why: FAULT-PHYSICAL-ACTOR-ABSENT. Same contract violation as fault-022. Downstream facet
      authors and continuity pass cannot resolve this slug. If this character is load-bearing
      (she is — she is the recurring figure in Plumm's man's observation log entries 92 and
      93), the card must exist before the file locks.
    criteria: An oc-* card for oc-girl-from-hamlet must be authored and placed in
      active-project/warehouse/ before this line is legal. Alternatively if this character maps
      to an existing slug, rename throughout.
    recommended_action: RENAME-SLUG (if existing card) or card must be authored then slug confirmed

notes:
  - The em-dash annotation pattern (lines 34, 46, 71, 89, 90, 91, 92, 93) is a systematic
    fixer pattern that survived into this file. All eight instances carry the same class of
    fault (modifier and/or negation embedded in annotation). Fixer should treat these as a
    batch with a single repair pattern: strip em-dash clause, retain bare SVO core.
  - Ordinal modifiers ("first," "second," "third," "fourth," "fifth") appear 7 times across
    the transcription sequence (lines 89–93) and also on lines 9, 27, 34, 45, 46. All are
    FAULT-FORM-MODIFIER. The ordinal content belongs in state-update facets or continuity
    tracking, not the proto-line.
  - Lines 89–93 (the transcription block) are the densest fault cluster: every line carries
    at least one modifier fault; two also carry negation faults. After fixer repair, all five
    lines will read "plumms-man transcribes the entry" — which collapses five distinct beats
    into five identical lines. Fixer should flag this to orchestrator: if sequence
    differentiation is load-bearing for pass 3 shape, the transcription block may need
    restructuring rather than simple stripping.
  - "plumms-man" slug (fault-022) is the highest-priority structural fault. It affects half
    the file. Resolution requires a card decision before any downstream pass can proceed on
    those lines.
