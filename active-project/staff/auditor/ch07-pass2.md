```yaml
audit:
  scope: episode
  target: chapter-07
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: fault
      what: chapter-07.md line 4 — "taylor-hebert-westeros holds still at the counter"
      why: stative posture; no action verb; FAULT-FORM-NON-ACTION-VERB class violation
      criteria: line must use a concrete action verb as its predicate, not a stative posture construction

    - id: fault-002
      type: fault
      what: chapter-07.md line 5 — "septon-rowan stands at the counter"
      why: stative position; no action verb; FAULT-FORM-NON-ACTION-VERB class violation
      criteria: line must use a concrete action verb as its predicate, not a bare positional stative

    - id: fault-003
      type: fault
      what: chapter-07.md line 76 — "taylor-hebert-westeros holds the garden wall"
      why: stative grip; no action verb; FAULT-FORM-NON-ACTION-VERB class violation
      criteria: line must use a concrete action verb as its predicate

    - id: fault-004
      type: fault
      what: chapter-07.md line 96 — "taylor-hebert-westeros stands at the sept door"
      why: stative position; no action verb; FAULT-FORM-NON-ACTION-VERB class violation
      criteria: line must use a concrete action verb as its predicate, not a bare positional stative

    - id: fault-005
      type: fault
      what: chapter-07.md line 97 — "taylor-hebert-westeros holds the sept doorframe"
      why: stative grip; no action verb; FAULT-FORM-NON-ACTION-VERB class violation
      criteria: line must use a concrete action verb as its predicate

    - id: fault-006
      type: flag
      what: chapter-07.md lines 37 and 75 — "taylor-hebert-westeros stops on the road" and "taylor-hebert-westeros stops at the garden wall"
      why: cessation-of-movement verbs ("stops") name a result state, not a performed action; borderline FAULT-FORM-NON-ACTION-VERB candidates; editor to assess

    - id: fault-007
      type: flag
      what: chapter-07.md lines 17–27 vs. chapter-07-plan.md goal — "Taylor watches the outcome shift against her through the same procedure she tried to use"
      why: Taylor exits the recorder's room (line 14–15) before Plumm arrives (line 17); she is not present for and receives no confirmed in-chapter delivery of Plumm's successful filing; the goal's watchpoint is not formally executed — closest candidate is lines 63–68 (document from Rowan's satchel) but content of that document is not specified in the chapter; partial drift on the goal's witnessing beat
```
