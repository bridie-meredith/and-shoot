# Audit Report — Season s01 Aggregate — Pass S3.5 Ruleset Compliance r2
# schema: schemas/audit-report.schema.md
# generated: 2026-05-09
# target: active-project/theater/proto-lines/s01.aggregate.md
# scope: S3.5 ruleset re-verification post fixer round 10

---

## File-level verdict: RULESET-CLEAN

---

## Verification: Prior Faults Resolved

---

### fault-001 (prior) — holds-the-breath ×5 — RESOLVED

- **IDs checked:** 75, 172, 203, 261, 778
- **Status:** All 5 recasts confirmed clean.
  - ID 75: `taylor-hebert-jaehaerys stills` — licensed intransitive, no `holds` involved.
  - ID 172: `taylor-hebert-jaehaerys stills` — clean.
  - ID 203: `taylor-hebert-jaehaerys tightens the jaw` — transitive, anatomical object, clean.
  - ID 261: `taylor-hebert-jaehaerys stills` — clean.
  - ID 778: `taylor-hebert-jaehaerys tightens the jaw` — clean.
- **Finding:** pass

---

### fault-002 (prior) — ID 916 FAULT-FORM-MODIFIER — RESOLVED

- **ID checked:** 916
- **Current form:** `the fly touches the mordant-beam joint`
- **Status:** Transitive verb + direct object. No trailing prepositional phrase. Form matches the established pattern of IDs 27 and 194. Clean.
- **Finding:** pass

---

## New Bones: 925–933

---

### ID 925
- **Line:** `taylor-hebert-jaehaerys lays the volume`
- **Analysis:** Transitive SVO. `lays` is a concrete physical disposition verb. `the volume` is an established prop. No modifier tail.
- **Finding:** pass

---

### ID 926
- **Line:** `taylor-hebert-jaehaerys enters the workshop`
- **Analysis:** Standard location-entry form. Consistent with the aggregate's established pattern.
- **Finding:** pass

---

### ID 927
- **Line:** `taylor-hebert-jaehaerys reaches the sept lane`
- **Analysis:** Standard motion-to-location form. Clean.
- **Finding:** pass

---

### ID 928
- **Line:** `taylor-hebert-jaehaerys enters the sept`
- **Analysis:** Standard location-entry form. Clean.
- **Finding:** pass

---

### ID 929
- **Line:** `mira-stonefield-jaehaerys enters the alley`
- **Analysis:** Standard location-entry form. Clean.
- **Finding:** pass

---

### IDs 930, 931, 932
- **Lines:** blank beats (time-skip breaks)
- **Analysis:** Structural markers. Not subject to deny-list SVO check. Clean.
- **Finding:** pass

---

### ID 933
- **Line:** `taylor-hebert-jaehaerys holds the face`
- **Analysis:** `face` is a licensed anatomical body part under the `holds` narrow license (stillness-against-pressure). Consistent with the established set (`holds the feet`, `holds the eyes`, `holds the chin`, `holds the head`, `holds the face`, `holds the mouth`, `holds the shoulder`). Clean.
- **Finding:** pass

---

## In-Place Recasts: IDs 354 and 398

---

### ID 354
- **Line:** `oc-lords-steward calls`
- **Analysis:** Intransitive. Consistent with ID 302 (`oc-child-peer calls`) and ID 911 (`oc-craftsman-mother calls`). No object required; the call event is observable without naming a recipient in the proto-line. Clean.
- **Finding:** pass

---

### ID 398
- **Line:** `oc-lords-steward calls`
- **Analysis:** Same form as ID 354. Clean.
- **Finding:** pass

---

## Drift-Pattern Ruling: `traces` on written text ×6

- **IDs:** 25, 188, 250, 683, 843, 872
- **Carried from prior audit as:** flag-001 (fixer discretion)
- **Fixer round 10 disposition:** PRE-EXISTING, left as flag per fixer discretion.
- **Ruling:** Retain as flag. Promote to fault not supported.

**Reasoning:** `traces` is not on the closed deny-list. The physical contact event (finger on surface) is observable and distinct from pure perception. The deny-list is closed, not open-ended by analogy. Promoting to fault at r2 would require `traces` to constitute a deny-list violation on its own terms, not merely by functional resemblance to `read`. The perception inference (reading comprehension) belongs in narrator/feel facets; the proto-line records the physical act. Six instances across the season represent a concentration risk at the facet-authoring stage, but that is an editor advisory, not a schema fault. The flag classification stands.

---

## Flags Carried from Prior Audit (Unchanged)

The following flags from the prior audit (flag-002 through flag-007) were not in fixer round 10 scope and remain unresolved. They are carried forward unchanged. No new finding is warranted; they are noted for the editor pass.

| ID | Flag | Status |
|---|---|---|
| flag-001 | `traces` ×6 on written text | Retained as flag (see above) |
| flag-002 | ID 73: `lowers his voice` — property-as-object | Carried |
| flag-003 | IDs 285, 803: possessive-qualified subjects | Carried |
| flag-004 | ID 841: `ledger query` — abstract compound noun | Carried |
| flag-005 | ID 906: inanimate folio as agent-of-crossing | Carried |
| flag-006 | ID 918: `cradles the head` — sustained-carry adjacency | Carried |
| flag-007 | Aggregate header missing `narrator:` / `goal:` | Carried (Phase 4 split action) |

---

## Full-File Scan: Additional Findings

No new deny-list violations, FAULT-FORM-MODIFIER instances, unlicensed `holds` objects, or abstraction-as-object constructions were identified in any line not previously catalogued. The 914, 916–924 bones from prior fixer rounds are clean. The 925–933 bones introduced in fixer round 10 are clean.

---

## Summary

```yaml
audit:
  scope: season
  target: s01-aggregate
  timestamp: 2026-05-09
  verdict: RULESET-CLEAN
  findings:
    - id: pass-001
      type: pass
      what: fault-001 prior — holds-the-breath ×5 (IDs 75, 172, 203, 261, 778)
      why: All 5 recasts confirmed clean. No residual unlicensed holds-the-breath form present.

    - id: pass-002
      type: pass
      what: fault-002 prior — ID 916 FAULT-FORM-MODIFIER
      why: ID 916 now reads "the fly touches the mordant-beam joint" — transitive verb, direct object, no prepositional tail. Clean.

    - id: pass-003
      type: pass
      what: new bones 925–933
      why: All 9 new bones are clean. No deny-list violations, no unlicensed holds forms, no modifier tails.

    - id: pass-004
      type: pass
      what: in-place recasts IDs 354 and 398
      why: Both recast to "calls" (intransitive). Consistent with established aggregate pattern.

    - id: flag-001
      type: flag
      what: traces on written text ×6 — IDs 25, 188, 250, 683, 843, 872
      why: Pattern unchanged from prior audit. Retained as flag. Not promoted to fault — closed deny-list does not include traces; physical contact event is observable. Concentration risk at facet-authoring stage; editor advisory.
```

- **Fault count:** 0
- **Flag count:** 7 (all carried from prior audit; none new; none promoted)
- **No fixer dispatch required.**
- **Phase 4 split action remains:** per-episode files must carry full extended headers per schema.
