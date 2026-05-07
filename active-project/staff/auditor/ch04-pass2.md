## Summary
total non-blank: ~96
faults: 7 (FAULT-FORM-NON-ACTION-VERB ×7), 1 flag (borderline)
file-level: FAIL

```yaml
audit:
  scope: episode
  target: chapter-04
  timestamp: 2026-05-07
  findings:

    - id: fault-001
      type: fault
      what: line 55 — "taylor-hebert-westeros holds the arm"
      why: Static-position verb. FAULT-FORM-NON-ACTION-VERB.
      criteria: Replace with active beat that establishes arm-extension as result of a move.

    - id: fault-002
      type: fault
      what: line 58 — "the raven holds the perch"
      why: State-continuation, not action. FAULT-FORM-NON-ACTION-VERB.
      criteria: Name an observable action that demonstrates the perch-holding under anomaly pressure.

    - id: fault-003
      type: fault
      what: line 68 — "the raven holds the perch" (second instance)
      why: Repeat. FAULT-FORM-NON-ACTION-VERB.
      criteria: Same as fault-002.

    - id: fault-004
      type: fault
      what: line 70 — "the raven holds the perch" (third instance)
      why: Third repeat dilutes anomaly. FAULT-FORM-NON-ACTION-VERB.
      criteria: Action escalates anomaly register, not state-restate.

    - id: fault-005
      type: fault
      what: line 62 — "oc-castellan-harrenhal faces the raven"
      why: Static orientation, not action. FAULT-FORM-NON-ACTION-VERB.
      criteria: Name the action of turning toward.

    - id: fault-006
      type: fault
      what: line 63 — "the raven targets oc-castellan-harrenhal"
      why: Static aim-state. FAULT-FORM-NON-ACTION-VERB.
      criteria: Active verb (locks, fixes, swings head toward).

    - id: fault-007
      type: fault
      what: line 86 — "oc-castellan-harrenhal faces the bell tower"
      why: Same as fault-005.
      criteria: Name the turn-action, not the resulting orientation.

    - id: fault-008
      type: flag
      what: line 101 — "taylor-hebert-westeros grips the wall stone"
      why: Borderline; "grips" is initial grasp but reads as static hold in context. Editor advisory.
```
