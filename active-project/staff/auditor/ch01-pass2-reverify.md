audit:
  scope: episode
  target: chapter-01 (proto-lines)
  timestamp: 2026-05-07
  pass: 2 (constraint audit — mechanic + per-line legality, post-fixer re-verification)
  verdict: FAIL

summary:
  total_lines_checked: 120  # numbered lines excluding blank time-skips (lines 8, 9, 11, 16, 30, 33, 36, 43, 54, 62, 69, 80, 89, 97, 108, 114, 120, 121)
  correct: 98
  faults: 22
  by_class:
    FAULT-FORM-MODIFIER: 18
    FAULT-FORM-NON-ACTION-VERB: 3
    FAULT-FORM-SUBJECT-ARTICLE: 1

---

findings:

  - id: fault-001
    type: fault
    what: "line 13: the sept candles gutter"
    why: >
      "sept" is an adjectival modifier on the noun "candles." No-modifier rule prohibits adjectives on
      any SVO component. Even if read as a compound noun, it is structurally an adjective+noun, not a
      named entity slug.
    criteria: >
      Subject must be a bare named entity using the prescribed `the <noun>` form without internal
      adjective. If disambiguation is needed, "the candles" is sufficient in context.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-002
    type: fault
    what: "line 18: a village woman knocks"
    why: >
      Two violations. (1) Subject uses indefinite article "a" instead of the prescribed `the <noun>` form
      for unnamed environment elements. Schema requires `the <noun>`. (2) "village" is a modifier on
      "woman." The combined form "a village woman" is doubly non-compliant.
    criteria: >
      Subject must be in `the <noun>` form without internal modifier. Fixer must adopt a consistent
      identifier for this character (e.g., "the woman") and apply it at all subsequent appearances.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-003
    type: fault
    what: "line 21: the village woman lifts the broth pot"
    why: >
      (1) "village" modifies "woman" — same subject-modifier fault as line 18. (2) "broth" modifies
      "pot" — compound noun object with internal adjective. No-modifier rule applies to object
      components as well as subject.
    criteria: >
      Subject must resolve to `the <noun>` form without internal modifier. Object must be a bare
      named prop or `the <noun>` without adjectival component. "The pot" is sufficient once context
      establishes which pot.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-004
    type: fault
    what: "line 23: the village woman enters the cottage"
    why: >
      "village" modifies "woman." Same subject-modifier fault. Applies at every occurrence of
      "the village woman."
    criteria: >
      Subject must be in bare `the <noun>` form without internal modifier.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-005
    type: fault
    what: "line 25: the village woman sets the broth pot"
    why: >
      (1) Subject "the village woman" carries modifier "village." (2) Object "the broth pot" carries
      modifier "broth." Both violations same class as fault-003.
    criteria: >
      Both subject and object must resolve to bare `the <noun>` forms.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-006
    type: fault
    what: "line 26: the village woman speaks to taylor-hebert-westeros"
    why: >
      Subject "the village woman" carries modifier "village."
    criteria: >
      Subject must be in bare `the <noun>` form.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-007
    type: fault
    what: "line 27: taylor-hebert-westeros speaks to the village woman"
    why: >
      Object/addressee "the village woman" carries modifier "village."
    criteria: >
      Listener reference must use bare `the <noun>` form consistent with the identifier chosen for
      this character.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-008
    type: fault
    what: "line 28: the village woman turns"
    why: >
      Subject "the village woman" carries modifier "village."
    criteria: >
      Subject must be in bare `the <noun>` form.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-009
    type: fault
    what: "line 29: the village woman exits the cottage"
    why: >
      Subject "the village woman" carries modifier "village."
    criteria: >
      Subject must be in bare `the <noun>` form.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-010
    type: fault
    what: "line 34: three riders crest the road"
    why: >
      "three" is a numeral modifier on the subject "riders." The no-modifier rule applies to
      numerals on subjects. Schema prescribes `the <noun>` for unnamed group entities; the numeral
      "three" is adjectival padding on the subject, not an actor slug. In subsequent lines this group
      is correctly rendered as "the riders."
    criteria: >
      Subject must be in bare `the <noun>` form without numeral modifier. "The riders" is already
      the correct form used at lines 44, 112, 113.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-011
    type: fault
    what: "line 35: two men-at-arms take position beside the official"
    why: >
      (1) "two" is a numeral modifier on the subject "men-at-arms." (2) "beside the official" is
      prepositional padding on the verb — "take position beside X" names the relative spatial result
      rather than the discrete physical act. The position-naming is a stative description, not a
      physical event verb. (3) "the official" as object is an undeclared entity slug — no actor slug
      "the official" appears in the cast roster or location card. The census officer has been slugged
      as "census-officer" elsewhere in the file; "the official" introduces a second unnamed reference
      for what may be the same actor.
    criteria: >
      Subject must be bare `the <noun>` without numeral modifier. Verb phrase must be a discrete
      physical act without prepositional spatial result. The object/destination must either be omitted
      (if the act is intransitive) or resolve to a consistent slug that matches the census-officer
      identifier used elsewhere.
    recommended_action: RECAST-PHYSICAL

  - id: fault-012
    type: fault
    what: "line 41: taylor-hebert-westeros crosses to the writing materials"
    why: >
      "writing" modifies "materials" — adjectival component inside the object. No-modifier rule
      applies to object noun phrases as well as subjects.
    criteria: >
      Object must be a bare named prop or `the <noun>` form. "The writing materials" should resolve
      to a clean prop identifier. "The materials" is sufficient in context given the location card
      establishes the septon's writing materials as a fixed prop.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-013
    type: fault
    what: "line 47: census-officer produces the census scroll"
    why: >
      "census" modifies "scroll" — adjectival component inside the object. Under strict no-modifier
      rule, compound nouns with internal descriptive components are non-compliant. Applies to every
      use of "the census scroll" in the file (lines 47, 65, 75, 93, 105).

      NOTE: Line 75 does not actually contain "census scroll" — correction: line 75 is a dialogue
      beat. Lines containing "census scroll": 47, 65, 93. Line 75 is
      "taylor-hebert-westeros speaks to census-officer."
    criteria: >
      Prop must be referenced by a bare name or an established prop slug without internal modifier.
      "The scroll" is sufficient once context establishes which scroll. Alternatively, if the writer
      requires disambiguation (multiple scrolls on set — see also line 102's "a scroll"), adopt a
      clean slug (e.g., "the ledger," "the census-scroll" as a hyphenated slug equivalent) that
      does not embed an adjectival modifier.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-014
    type: fault
    what: "line 65: census-officer unrolls the census scroll"
    why: >
      Same modifier fault as fault-013. "census" is adjectival on "scroll."
    criteria: >
      Same as fault-013. Bare prop identifier required.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-015
    type: fault
    what: "line 78: taylor-hebert-westeros raises her eyes"
    why: >
      "her" is a possessive pronoun modifier on "eyes." No-modifier rule covers possessives as
      determiners. The prescribed form for body-part acts on a single named actor is bare:
      "raises the eyes" unambiguously refers to the line's subject.
    criteria: >
      Possessive pronoun must be replaced with definite article. "Taylor-hebert-westeros raises
      the eyes" is unambiguous given the single actor subject.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-016
    type: fault
    what: "line 79: taylor-hebert-westeros lowers her eyes"
    why: >
      Same possessive-pronoun modifier fault as fault-015.
    criteria: >
      Same as fault-015. "Lowers the eyes."
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-017
    type: fault
    what: "line 86: septon-dying-protector reaches for the quill"
    why: >
      "for" in "reaches for" is prepositional padding. The no-modifier rule prohibits prepositional
      padding. The discrete physical act is the extension of the hand toward the quill; the correct
      form is a direct transitive: "septon-dying-protector reaches the quill" or a more precise act
      verb ("extends a hand toward the quill" is compound — so the clean form is a bare transitive).
    criteria: >
      Verb phrase must not contain a prepositional particle that adds spatial padding. Direct
      transitive verb with object is required.
    recommended_action: RECAST-PHYSICAL

  - id: fault-018
    type: fault
    what: "line 93: census-officer rolls the census scroll"
    why: >
      "census" modifies "scroll." Same modifier fault as fault-013/014.
    criteria: >
      Same as fault-013. Bare prop identifier.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-019
    type: fault
    what: "line 96: taylor-hebert-westeros holds the chin angle"
    why: >
      "holds the chin angle" — "the chin angle" is not a body part; it is a positional abstraction
      (a description of angular orientation). The licensed `holds` form requires body-part-as-object
      for stillness-against-pressure. "Chin angle" describes an angular state, not an anatomical
      part that can be held. This is a FAULT-FORM-NON-ACTION-VERB: "holds" with an abstract object
      is a stative state assertion, not a physical act.
    criteria: >
      Line must be recast as either: (a) a physical body-part hold in the licensed form (e.g.,
      "taylor-hebert-westeros holds the chin" — the anatomical chin, not its angle), or (b) a
      discrete physical act that produces the stillness (e.g., "taylor-hebert-westeros lifts the
      chin"). The abstract positional concept must not appear as the verb's object.
    recommended_action: RECAST-AS-HOLD or RECAST-PHYSICAL

  - id: fault-020
    type: fault
    what: "line 102: a man-at-arms produces a scroll"
    why: >
      Subject "a man-at-arms" uses indefinite article "a" rather than the prescribed `the <noun>`
      form for unnamed environment elements. Schema requires `the <noun>`. The indefinite article
      also creates a second, distinct scroll entity ("a scroll") that has not been established on
      the set, potentially conflicting with the census scroll already in play.
    criteria: >
      Subject must be in `the <noun>` form (e.g., "a man-at-arms" → "the man-at-arms" if referring
      to an established group member, or a consistent slug if this is a new named figure). The
      scroll produced must be a distinct named prop if different from the census scroll, or the same
      prop referenced cleanly.
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-021
    type: fault
    what: "line 118: septon-dying-protector closes his eyes"
    why: >
      "his" is a possessive pronoun modifier on "eyes." Same class as fault-015/016.
    criteria: >
      Possessive pronoun must be replaced with definite article. "Septon-dying-protector closes
      the eyes."
    recommended_action: RECAST-AS-BARE-NOUN

  - id: fault-022
    type: fault
    what: "line 131: taylor-hebert-westeros holds the spine"
    why: >
      "the spine" is ambiguous between (a) anatomical body part (the vertebral column, valid for
      licensed stillness-against-pressure hold) and (b) the spine of a book (a prop reference,
      which would be a physical grip action — acceptable — but the book whose spine is referenced
      has not been established in hand at this beat, as line 126 places the book and line 127 exits
      the cottage). Under strict bias: the ambiguity itself is a fault. If this is the anatomical
      spine (kneeling stillness), the form is licensed but the ambiguity is unresolvable without
      context that would require a modifier. If this is a book prop, the prop's placement has been
      lost since line 126.
    criteria: >
      Fixer must resolve the ambiguity. If anatomical: "taylor-hebert-westeros holds the spine"
      is valid only if "spine" is unambiguously a body-part reference — fixer may retain the line
      with a note that disambiguation is Pass 5 scope. If prop: the book must be re-established
      in hand before this line; the line should not be the point of reintroduction.
    recommended_action: RECAST-PHYSICAL

---

flags:

  - id: flag-001
    type: flag
    what: >
      Actor slug "census-officer" appears in 35+ lines but is not listed in the chapter-01-plan.md
      actors field (which lists taylor-hebert-westeros, septon-dying-protector, oc-castellan-harrenhal)
      and is not in the series cast_roster in showrunner memory.md. "oc-castellan-harrenhal" is in
      the cast roster but does not appear anywhere in the proto-line file.
    why: >
      If census-officer is a new OC slug, it has no actor card. If it is oc-castellan-harrenhal or
      his deputy, the slug should match the card slug. Pass 5 will catch actor-slug resolution
      failures formally; flagged here for fixer awareness.

  - id: flag-002
    type: flag
    what: >
      Line 35 introduces "the official" as an unnamed entity reference for what appears to be the
      census-officer. "The official" does not resolve to the census-officer slug and creates a
      second reference for the same actor within the same file.
    why: >
      Inconsistent slugging corrupts downstream facet citations. Every facet that cites this beat
      will reference "the official" while the rest of the file uses "census-officer." Pass 5 would
      catch this formally; fault-011 covers the mechanic violations on the same line.

  - id: flag-003
    type: flag
    what: >
      Lines 39 and 40 (septon-dying-protector opens his eyes / septon-dying-protector speaks to
      taylor-hebert-westeros) — possessive "his eyes" at line 39 carries the same modifier class
      as fault-015/016/021. However, line 39 is NOT in the fault list above because this pass
      verifies post-fixer output; if the previous fixer corrected the pronoun form at lines 78,
      79, and 118 but missed line 39, a residual fault exists.
    why: >
      Line 39 reads "septon-dying-protector opens his eyes" — "his" is a possessive modifier.
      Under strict rule this is the same fault class as fault-021. Listing as flag pending fixer
      re-check; if the fixer dispatch for fault-021 does not also address line 39, this should
      be promoted to fault in the next re-verification.

---

verdict: FAIL
fault_count: 22
flag_count: 3
advance_condition: >
  CONTINUITY-OK when fault count reaches zero. Orchestrator must dispatch fixer against all 22
  faults before re-running pass 2. Pay particular attention to:
  (1) All "village woman" / "broth pot" / "census scroll" occurrences — systematic rename required.
  (2) Line 96 "holds the chin angle" — non-trivial recast, not a simple rename.
  (3) Line 131 "holds the spine" — requires disambiguation decision before fixer can act.
  (4) Line 35 "the official" — must be resolved to census-officer or a consistent named slug.
  (5) Line 39 possessive "his eyes" — see flag-003; promote to fault if not corrected with fault-021.
