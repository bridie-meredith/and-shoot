audit:
  scope: episode
  target: chapter-10 (season finale — Ward of the Administration)
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: fault
      what: chapter-10.md line 42 — "the wax sets"
      why: Subject is the inanimate prop "the wax," not a cast actor. Verb "sets" is stative/intransitive with no performing agent. FAULT-FORM-NON-ACTION-VERB class: every line must have a cast actor as subject executing an action verb. "The wax" is not in the chapter-10 cast list.
      criteria: The line must name a cast actor as the performing subject executing an action verb; the physical fact of the wax hardening must be rendered as something a cast actor observes, marks, or acts on — or be removed.

    - id: fault-002
      type: fault
      what: chapter-10.md line 49 — "the hall holds"
      why: Subject is the set itself ("the hall"), not a cast actor. "Holds" is atmospheric/stative. No cast actor is executing an action. Same FAULT-FORM-NON-ACTION-VERB class violation as fault-001.
      criteria: The line must name a cast actor as the performing subject executing an action verb; the atmospheric beat the line attempts must be delivered through a cast actor's body or action — or be removed.

    - id: fault-003
      type: flag
      what: chapter-10.md line 26 and line 48 — "taylor-hebert-westeros holds the chin angle" appears at both positions
      why: Identical bullet repeated at two separate positions in the same chapter. Not an audience-retry duplicate (different bullet numbers), but a beat-duplication that risks producing identical or near-identical prose output at two points in the chapter. Editor flag; not a constraint violation.
      criteria: ~
