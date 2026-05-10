```yaml
audit:
  scope: season
  target: s01
  pass: PASS
  timestamp: 2026-05-09
  prior_audit: season-s01-pass-S1-constraint.md
  fault_count: 0
  flag_count: 0
  findings: []
```

## Verification log

### ID 916 (prior fault-001: prep modifier)

Current text: `the fly touches the mordant-beam joint`

`touches` is transitive; `the mordant-beam joint` is the direct object. No prepositional phrase of place. The prior `at the mordant-beam joint` form is gone. CLEAN.

### ID 909 (prior fault-002: possession redundancy)

ID 909 is absent from the aggregate. The possession chain for the folio reads cleanly: maester draws (893), passes ferryman (894), ferryman takes (895), ferryman grips (898), ferry folio crosses the water (906). Duplicate-receipt fault resolved by deletion. CLEAN.

### New bones IDs 925–933

- 925 `taylor-hebert-jaehaerys lays the volume` — transitive, clean SVO. CLEAN.
- 926 `taylor-hebert-jaehaerys enters the workshop` — canonical entry form. CLEAN.
- 927 `taylor-hebert-jaehaerys reaches the sept lane` — transitive, clean SVO. CLEAN.
- 928 `taylor-hebert-jaehaerys enters the sept` — canonical entry form. CLEAN.
- 929 `mira-stonefield-jaehaerys enters the alley` — canonical entry form. CLEAN.
- 930, 931, 932 — blank-numbered time-skip markers. Schema-compliant. CLEAN.
- 933 `taylor-hebert-jaehaerys holds the face` — body-part object, licensed under the narrow `holds` license. CLEAN.

No fault patterns introduced by the new bones.

### Recast IDs 354 and 398 (`calls`)

Both read: `oc-lords-steward calls`

`calls` is a bare intransitive vocalization verb — not a motion verb. The FAULT-FORM-NO-VERB rule targets bare intransitive *motion* verbs ("taylor moves"). The intransitive-lands-cleanly exception covers physical output verbs whose act is observable without a destination or object (schema names `exhales`; `calls` is the vocalization parallel). The summoning function is scene-legible at both positions (dock registration at ID 354; folio sequence at ID 398). Both are acceptable. PASS.

### Full-aggregate walk

No new SVO violations found beyond the five flags carried forward from the prior audit (flag-001 through flag-005). Those flags remain advisory and are not re-examined here. No possession-chain faults introduced by fixer round 10. No copulas, negations, conjunctions, perception verbs, or prepositional phrases of place detected in any new or recast line.
```
