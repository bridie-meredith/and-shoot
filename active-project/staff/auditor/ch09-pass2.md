```yaml
audit:
  scope: episode
  target: chapter-09
  timestamp: 2026-05-07
  findings:

    - id: fault-001
      type: fault
      what: chapter-09.md line 66 — "taylor-hebert-westeros exhales"
      why: >
        "Exhales" is an intransitive involuntary physiological response with no object or
        location. Bullet format is [subject] [verb] [object/location]; an objectless reflex
        verb names internal state (tension release) rather than a directed external action.
        FAULT-FORM-NON-ACTION-VERB class. The surrounding withdrawal sequence (lines 64–65,
        67 blank) gives the beat structural space; the bullet occupies a slot that should
        carry a directed action or be cut.
      criteria: >
        Line 66 must either be replaced with a directed external action that belongs to the
        withdrawal beat, or removed. The bullet must not name a physiological reflex as its
        sole verb.

    - id: fault-002
      type: pass
      what: Constraints — cond-fauna-control-rules, cond-westerosi-customary-authority, cond-riverlands-120ac-state, cond-series-tone-constraints
      why: >
        Fauna deployments are brief and episodic (station / reposition / withdraw); no
        sustained-use cost-curve violation present at bullet level. Administrative contest
        (documents, castellan adjudication, seal-of-authority mechanics) is correct
        customary-authority social physics. Escalation holds: chapter opens with two active
        competing claims and closes with a crown agent on the ground forcing resolution —
        escalation-ratchet not violated. Tone is external-action-dominant throughout;
        no introspection-dominant register in the bullet set.
      criteria: null

    - id: fault-003
      type: pass
      what: Bullet-to-plan drift — chunk change arc vs. chapter-09 bullet sequence
      why: >
        Plan change: "Two rival claims active, castellan has not yet acted → Celtigar's
        agent on the ground, castellan must resolve before crown visibility removes his
        discretion." Chapter delivers exactly this arc across three distinct scenes (Plumm
        and Bracken contesting the file; Taylor repositioning surveillance; Celtigar's agent
        arriving and presenting documents). Taylor holds observer position throughout —
        no bullet places her as a participant in the contest, consistent with the plan goal.
        No drift found.
      criteria: null

    - id: fault-004
      type: pass
      what: Form check — all remaining bullets
      why: >
        Lines 96–97 ("presses the palms flat", "holds the chin angle") follow [subject]
        [verb] [object] form with directed physical objects, consistent with the body-state
        bullet pattern used in chapter-08. All other bullets carry transitive or directionally
        complete action verbs with explicit objects or locations. No additional
        FAULT-FORM-NON-ACTION-VERB violations found outside line 66.
      criteria: null
```
