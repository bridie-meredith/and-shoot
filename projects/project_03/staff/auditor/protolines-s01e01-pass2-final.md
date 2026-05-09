## Summary
total non-blank body lines: 48
CORRECT: 43
faults: FAULT-FORM-NO-VERB: 4 | FAULT-FORM-INTERIORITY: 1
file-level: FAIL
strict accept rate: 89.6%

---

```yaml
audit:
  scope: episode
  target: s01e01
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: fault
      what: proto-line 4 — "mira-stonefield moves"
      why: bare movement verb with no destination or object gives an observer no physical information; fails the schema requirement that the verb produce what an observer would see. FAULT-FORM-NO-VERB. Downstream stitcher cannot render a meaningful beat from an undirected move.
      criteria: line must name a transitive movement verb with a physical destination as direct object (per SVO discipline: prefer transitive verbs that take the location as direct object)

    - id: fault-002
      type: fault
      what: proto-line 5 — "edric-cray moves"
      why: same as fault-001 — bare movement verb, no physical specificity. FAULT-FORM-NO-VERB.
      criteria: line must name a transitive movement verb with a physical destination as direct object

    - id: fault-003
      type: fault
      what: proto-line 15 — "taylor-hebert-westeros moves"
      why: same as fault-001 — bare movement verb, no physical specificity. FAULT-FORM-NO-VERB.
      criteria: line must name a transitive movement verb with a physical destination as direct object

    - id: fault-004
      type: fault
      what: proto-line 53 — "the cart moves"
      why: same as fault-001 — bare movement verb on an inanimate subject gives no physical directionality. FAULT-FORM-NO-VERB. Stitcher cannot distinguish departure, approach, or pass-through from this line.
      criteria: line must name a transitive movement verb with a physical destination or trajectory as direct object, or use a more specific intransitive verb (e.g., "the cart departs")

    - id: fault-005
      type: fault
      what: proto-line 57 — "the yard holds"
      why: "the yard holds" with no named physical object is a state assertion in disguise — the yard holding means the yard is still/quiet, which is an abstract ambient state, not a physical act on a named object. The brief explicitly names "the yard holds the silence" as FAULT-FORM-INTERIORITY; the objectless form is the same violation. State assertions belong in loc-state facets. FAULT-FORM-INTERIORITY.
      criteria: line must either be deleted (and the beat moved to a loc-state facet) or recast as a hold-verb with a named physical object the yard or a character acts upon
```
