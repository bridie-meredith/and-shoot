audit:
  scope: episode
  target: chapter-05 (proto-lines — pass 2 re-verification, post-fixer)
  timestamp: 2026-05-07
  narrator: septon-rowan
  total_lines: 77
  time_skip_lines: 7  # lines 16, 24, 29, 71, 74 (blank), plus lines not numbered sequentially are gaps not time-skips; actual blank numbered lines: 16, 24, 29, 71, 74
  audited_lines: 72
  correct_count: 38
  fault_count: 34
  fault_breakdown:
    FAULT-FORM-MODIFIER: 28
    FAULT-FORM-NON-ACTION-VERB: 3
    FAULT-FORM-PERCEPTION: 1
  flag_count: 1

  findings:

    # ── FAULT-FORM-MODIFIER ────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: "line 2 — septon-rowan drops his travel pack against the rain-barrel"
      why: "against the rain-barrel" is prepositional padding; "his" is a possessive modifier on the object. Both violate the no-modifier rule. A dropped pack's final resting place is a state-update / location-state facet concern, not a SVO spine detail.
      criteria: line must resolve to a clean SVO with no prepositional tail and no possessive modifier on the object
      recommended_action: RECAST-PHYSICAL

    - id: fault-002
      type: fault
      what: "line 3 — taylor-hebert-westeros crosses the yard toward septon-rowan"
      why: "toward septon-rowan" is a prepositional phrase appended beyond the direct object. The object of "crosses" is "the yard"; "toward septon-rowan" is additional directional padding.
      criteria: line must resolve to SVO with no prepositional tail beyond the direct object of the verb
      recommended_action: RECAST-PHYSICAL

    - id: fault-003
      type: fault
      what: "line 8 — taylor-hebert-westeros holds her eyes on septon-rowan"
      why: "her" is a possessive modifier on "eyes." The licensed form for body-part stillness-hold is bare ("holds the eyes"), not possessive. "on septon-rowan" is additionally prepositional.
      criteria: line must use the bare licensed form with no possessive determiner and no prepositional tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-004
      type: fault
      what: "line 11 — septon-rowan sets the travel pack on the table"
      why: "on the table" is prepositional padding. Placement destination belongs in a location-state or state-update facet, not the SVO spine.
      criteria: line must resolve to a clean SVO with no prepositional destination tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-005
      type: fault
      what: "line 13 — septon-rowan opens the septon's ledger on the table"
      why: "on the table" is prepositional padding appended after the direct object. The ledger's physical position when opened is a state-update concern, not a spine concern.
      criteria: line must resolve to SVO with no prepositional tail after the direct object
      recommended_action: RECAST-PHYSICAL

    - id: fault-006
      type: fault
      what: "line 18 — septon-rowan crosses the yard to the sept door"
      why: "to the sept door" is a prepositional destination phrase beyond the direct object "the yard." Per strict SVO discipline, motion-verb destination phrases are prepositional padding.
      criteria: line must resolve to SVO with no prepositional tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-007
      type: fault
      what: "line 20 — septon-rowan advances to the chancel"
      why: "to the chancel" is a prepositional phrase. The verb "advances" has no direct object; the destination is carried as a prepositional phrase, which is padding under strict discipline.
      criteria: line must resolve to a concrete SVO with no prepositional phrase, or be recast as a motion verb with the destination as direct object (e.g., enters / reaches)
      recommended_action: RECAST-PHYSICAL

    - id: fault-008
      type: fault
      what: "line 21 — septon-rowan kneels at the altar table"
      why: "at the altar table" is a prepositional phrase locating the action. Location annotation belongs in facets citing this proto-line, not in the SVO spine.
      criteria: line must resolve to bare intransitive SVO with no prepositional locating phrase
      recommended_action: RECAST-PHYSICAL

    - id: fault-009
      type: fault
      what: "line 22 — septon-rowan rises from the altar table"
      why: "from the altar table" is a prepositional phrase. The separation from a location is a stative/positional detail belonging in a facet, not the SVO spine.
      criteria: line must resolve to bare intransitive SVO with no prepositional origin phrase
      recommended_action: RECAST-PHYSICAL

    - id: fault-010
      type: fault
      what: "line 25 — septon-rowan exits the sept yard through the gate"
      why: "through the gate" is prepositional padding. The exit route is a location-state concern.
      criteria: line must resolve to SVO with no prepositional tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-011
      type: fault
      what: "line 26 — septon-rowan takes the Harrenhal road north"
      why: "north" is a directional adverb modifying how or where the road-taking goes. Adverbs are banned under the no-modifier rule.
      criteria: line must resolve to SVO with no adverbial modifier
      recommended_action: RECAST-PHYSICAL

    - id: fault-012
      type: fault
      what: "line 28 — septon-rowan continues the road north toward Harrenhal"
      why: "north" is a directional adverb; "toward Harrenhal" is a prepositional phrase. Both are modifiers on the verb or object.
      criteria: line must resolve to SVO with no adverb and no prepositional tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-013
      type: fault
      what: "line 33 — ser-harwick-plumm turns toward septon-rowan"
      why: "toward septon-rowan" is a prepositional phrase. The bare intransitive "turns" requires no object but the appended phrase is padding.
      criteria: line must resolve to bare SVO with no prepositional tail, or recast so the object of "turns" is the direct object rather than a prepositional target
      recommended_action: RECAST-PHYSICAL

    - id: fault-014
      type: fault
      what: "line 42 — ser-harwick-plumm draws the record book from his satchel"
      why: "from his satchel" is a prepositional origin phrase; "his" is a possessive modifier. Both are banned.
      criteria: line must resolve to a clean SVO draw action with no prepositional origin and no possessive modifier
      recommended_action: RECAST-PHYSICAL

    - id: fault-015
      type: fault
      what: "line 47 — ser-harwick-plumm touches the nib to the page"
      why: "to the page" is a prepositional destination phrase. The placing of nib on page is a single physical action but the destination is expressed as a prepositional phrase rather than direct object.
      criteria: line must resolve to SVO where the page is the direct object of the action verb, or be recast without a prepositional tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-016
      type: fault
      what: "line 48 — ser-harwick-plumm writes rowan's name into the record book"
      why: "into the record book" is a prepositional destination phrase; "rowan's" is a possessive modifier on the direct object.
      criteria: line must resolve to SVO with direct object naming what is written, no possessive modifier, no prepositional destination tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-017
      type: fault
      what: "line 52 — ser-harwick-plumm touches the nib to the page"
      why: duplicate of fault-015 (same line repeated at line 52). Same violation.
      criteria: same as fault-015
      recommended_action: RECAST-PHYSICAL

    - id: fault-018
      type: fault
      what: "line 53 — ser-harwick-plumm writes the sept entry into the record book"
      why: "into the record book" is a prepositional destination phrase.
      criteria: line must resolve to SVO with no prepositional destination tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-019
      type: fault
      what: "line 55 — ser-harwick-plumm numbers the entry in the record book"
      why: "in the record book" is a prepositional locating phrase. The record book as the surface being acted on should be the direct object of the verb, not a prepositional complement.
      criteria: line must resolve to SVO where the record book (or the entry) is the direct object and no prepositional phrase trails the object
      recommended_action: RECAST-PHYSICAL

    - id: fault-020
      type: fault
      what: "line 61 — ser-harwick-plumm touches the nib to the page"
      why: duplicate of fault-015 and fault-017 (same line pattern at third occurrence). Same violation.
      criteria: same as fault-015
      recommended_action: RECAST-PHYSICAL

    - id: fault-021
      type: fault
      what: "line 62 — ser-harwick-plumm writes taylor's name into the record book"
      why: "into the record book" is a prepositional destination phrase; "taylor's" is a possessive modifier on the direct object.
      criteria: line must resolve to SVO with direct object naming what is written, no possessive modifier, no prepositional destination tail
      recommended_action: RECAST-PHYSICAL

    - id: fault-022
      type: fault
      what: "line 66 — ser-harwick-plumm returns the record book to his satchel"
      why: "to his satchel" is a prepositional destination; "his" is a possessive modifier.
      criteria: line must resolve to SVO with no prepositional tail and no possessive modifier
      recommended_action: RECAST-PHYSICAL

    - id: fault-023
      type: fault
      what: "line 69 — ser-harwick-plumm turns through the postern gate"
      why: "through the postern gate" is a prepositional phrase. The action of turning into or passing the gate is a motion event whose destination/path is expressed as prepositional padding.
      criteria: line must resolve to a motion verb with no prepositional path phrase, or be split into a turn and an enter
      recommended_action: SPLIT-INTO-N

    - id: fault-024
      type: fault
      what: "line 73 — septon-rowan turns south on the Harrenhal road"
      why: "south" is a directional adverb; "on the Harrenhal road" is a prepositional locating phrase.
      criteria: line must resolve to SVO with no adverb and no prepositional locating phrase
      recommended_action: RECAST-PHYSICAL

    - id: fault-025
      type: fault
      what: "line 76 — taylor-hebert-westeros rises from the garden wall"
      why: "from the garden wall" is a prepositional origin phrase. Where Taylor was sitting is a state-update / location-state concern, not a SVO spine detail.
      criteria: line must resolve to bare intransitive SVO with no prepositional origin phrase
      recommended_action: RECAST-PHYSICAL

    - id: fault-026
      type: fault
      what: "line 81 — septon-rowan holds his eyes on taylor-hebert-westeros"
      why: "his" is a possessive modifier on "eyes." The licensed body-part stillness-hold form is bare ("holds the eyes"). "on taylor-hebert-westeros" is additionally a prepositional phrase.
      criteria: line must use the licensed bare form with no possessive determiner and no prepositional tail
      recommended_action: RECAST-PHYSICAL

    # ── FAULT-FORM-NON-ACTION-VERB ─────────────────────────────────────────

    - id: fault-027
      type: fault
      what: "line 30 — ser-harwick-plumm stands at the gatehouse postern"
      why: "stands" describes a stative position, not a posture-act. The brief explicitly names "stands describing position not posture-act" as FAULT-FORM-NON-ACTION-VERB. This line asserts Plumm is already stationed at the postern — a state, not an action. "at the gatehouse postern" is additionally prepositional.
      criteria: line must be recast as the action that placed Plumm at the postern (e.g., his arrival, his step to position) or removed if his presence is established by location-state; if the intent is to establish his presence at chapter-open, a state-update facet citing the flanking line is the correct instrument
      recommended_action: RECAST-PHYSICAL

    - id: fault-028
      type: fault
      what: "line 72 — septon-rowan holds his position at the gatehouse wall"
      why: "holds his position" uses "holds" with an abstract object ("his position"). The brief explicitly calls out "holds with abstract object" as a banned form. "his position" is not a physical object being gripped; it is a state description. "at the gatehouse wall" is additionally prepositional.
      criteria: line must be recast as a concrete physical stillness-hold using a licensed form (body-part as object for stillness-against-pressure) or collapsed into a bare intransitive that records Rowan's inaction as an act (e.g., "septon-rowan stops")
      recommended_action: RECAST-PHYSICAL

    - id: fault-029
      type: fault
      what: "line 83 — taylor-hebert-westeros holds the chin angle"
      why: "holds the chin angle" uses "holds" with an abstract object ("the chin angle"). "chin angle" is an abstract description of posture, not a physical body-part being held against pressure. The licensed body-part form would be "holds the chin," not "holds the chin angle."
      criteria: line must be recast using the bare licensed body-part form ("holds the chin") or a different physical posture-act verb
      recommended_action: RECAST-PHYSICAL

    # ── FAULT-FORM-PERCEPTION ──────────────────────────────────────────────

    - id: fault-030
      type: fault
      what: "line 27 — septon-rowan crests the rise where the castle walls come into view"
      why: "where the castle walls come into view" is a subordinate clause expressing what the narrator perceives at the crest of the rise. "Come into view" is a perception event — the walls becoming visible to Rowan — embedded in a SVO spine line. This is a POV-leak perception clause. The proto-line spine records physical acts, not perceptual events. Additionally this constitutes a subordinate/conjunction-style clause appended to the main SVO (FAULT-FORM-CONJUNCTION boundary case).
      criteria: line must record only Rowan's physical act of cresting the rise; the perceptual consequence (castle walls visible) belongs in a location-state or narrator facet citing this line, not in the spine itself
      recommended_action: RECAST-PHYSICAL

    # ── FLAG ───────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: "line 10 — septon-rowan enters the septon's cottage"
      why: "septon's" is a possessive in the location name. The location card (loc-harrenhal-sept-environs) uses "the septon's cottage" as the canonical name for this outbuilding. If the possessive is part of the canonical location name, it is not a novel modifier and the line is clean. If fixer normalizes all possessives in location names, this line would also need recasting. Advisory: confirm whether "septon's cottage" should be treated as an atomic location slug before fixer acts on possessives in location names elsewhere.
      # No criteria — flag only, no fixer dispatch required unless fixer establishes a rule during repair of other lines.

    # ── POV OBSERVABILITY ─────────────────────────────────────────────────
    # All non-fault lines where Taylor or Plumm act are physically observable by septon-rowan as
    # POV narrator. No POV-observability faults found beyond fault-030 (perception clause).

    # ── CONSTRAINT CHECKS ─────────────────────────────────────────────────
    # cond-westerosi-customary-authority: no violations. Rowan's intercession at the gatehouse
    #   (not forcing entry, engaging the inspector at the threshold) is consistent with the
    #   "invoke competing authority" resistance mode. Plumm recording both names is the expected
    #   "deviation noted" consequence.
    # cond-riverlands-120ac-state: no violations. Plumm's role as official recorder at the
    #   gatehouse is consistent with impressment-census operations described in the card.
    # cond-series-tone-constraints: not applicable at proto-line spine level.
    # Series laws and lore (memory.md): no violations found in the SVO spine.

    # ── PHYSICAL / PROP CHECKS ────────────────────────────────────────────
    # travel pack: introduced line 2, consistent with newly arrived septon. No fault.
    # septon's ledger: fixed prop in loc-harrenhal-sept-environs. Present on set. No fault.
    # record book and stylus: Plumm's official kit, drawn from his satchel (line 42). Consistent
    #   with inspector role. No fault beyond the MODIFIER faults on the draw/return lines.
    # rain-barrel: fixed prop in loc-harrenhal-sept-environs. No fault.
    # altar table: fixed prop in loc-harrenhal-sept-environs. No fault.
    # postern gate: named fixed prop in loc-harrenhal-exterior. No fault.
    # garden wall: physically coherent with the kitchen garden described in loc-harrenhal-sept-environs. No fault.

    # ── HEADER ────────────────────────────────────────────────────────────
    # narrator: septon-rowan — present in series cast_roster (memory.md). PASS.
    # goal: present and non-empty. PASS.
