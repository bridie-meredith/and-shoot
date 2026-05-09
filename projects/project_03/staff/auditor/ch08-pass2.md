audit:
  scope: episode
  target: chapter-08
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: fault
      what: line 63 — "taylor-hebert-westeros holds the position at the chancel"
      why: "the position" is an abstraction-as-object; "holds the position" is stative spatial expression, not a discrete physical action on a physical object. FAULT-FORM-NON-ACTION-VERB. Writer self-reported; confirmed not licensed.
      criteria: line must name a discrete physical action performed by taylor-hebert-westeros at the chancel — body contacts stone, hand finds the rail, feet stop on the step, or similar concrete act

    - id: fault-002
      type: fault
      what: line 81 — "the hall holds the silence"
      why: "the hall" is a location-as-agent and "the silence" is an abstraction-as-object; neither is a concrete physical actor performing a physical action. FAULT-FORM-NON-ACTION-VERB. Writer self-reported; confirmed not licensed.
      criteria: line must name a concrete physical actor (a person present in the hall) performing or withholding a discrete physical action, or be replaced by a physical beat that renders the silence through a character's body

    - id: fault-003
      type: fault
      what: line 19 — "taylor-hebert-westeros holds the eyes on the table"
      why: "the eyes" as object and "holds" as stative-gaze-direction is the same abstraction-as-object pattern as lines 63 and 81; gaze-direction is not a discrete physical action. FAULT-FORM-NON-ACTION-VERB.
      criteria: line must name a discrete physical action performed by taylor-hebert-westeros — a body contact, a held breath, hands flat on knees, or equivalent concrete act that renders the avoidance without stative gaze framing

    - id: fault-004
      type: fault
      what: line 27 — "taylor-hebert-westeros holds the feet on the floor"
      why: "the feet" as object and "holds" as stative-placement is the same class as lines 19, 63, 81. Not a discrete physical action on a physical object. FAULT-FORM-NON-ACTION-VERB.
      criteria: line must name a discrete physical action performed by taylor-hebert-westeros that renders the stillness through a concrete physical act

    - id: fault-005
      type: fault
      what: line 80 — "ser-aemon-bracken holds the chin level"
      why: "the chin" as object and "holds" as stative body-part-position is the same class. Not a discrete physical action on a physical object. FAULT-FORM-NON-ACTION-VERB.
      criteria: line must name a discrete physical action performed by ser-aemon-bracken — a controlled breath, jaw press, hands at sides, or equivalent concrete act

    - id: fault-006
      type: fault
      what: line 95 — "taylor-hebert-westeros holds the hands on the table"
      why: "the hands" as object and "holds" as stative-placement is the same pattern as lines 19, 27, and 80. FAULT-FORM-NON-ACTION-VERB.
      criteria: line must name a discrete physical action performed by taylor-hebert-westeros that renders stillness through a concrete act

    - id: fault-007
      type: fault
      what: line 86 — "the hall empties"
      why: "the hall" is a location acting as agent; a location cannot perform an action. FAULT-FORM-NON-ACTION-VERB.
      criteria: line must name a concrete physical actor (or a named set of actors) performing the exit action — "the men in the hall file out," "those present turn for the door," or equivalent — replacing the location-as-agent construction

    - id: flag-001
      type: flag
      what: line 4 — "an armed man positions at the cottage door"
      why: "positions" is intransitive stative-placement; the subject does move to the door but the verb describes a resulting state rather than naming a discrete physical act (stands, steps, plants). Borderline FAULT-FORM-NON-ACTION-VERB; flagged for fixer review.
