# Audit Report — proto-lines s01e01 pass 2 convergence
schema: schemas/audit-report.schema.md
episode: s01e01
file reviewed: design/shoot-v2/phase2-svo-writer-fork-output.md
run: pass 2 (constraint audit) — convergence check against post-repair, post-shape, post-trim file

---

## Summary

```
total non-blank body lines: 50
time-skips: 5  (IDs 7, 16, 26, 49, 54)
deletions (ID gaps): 3  (IDs 6, 41, 52)
CORRECT: 46
faults:
  FAULT-FORM-MODIFIER: 3
  FAULT-PHYSICAL-PROP-ABSENT: 1
  FAULT-FORM-COPULA: 0
  FAULT-FORM-NEGATION: 0
  FAULT-FORM-PERCEPTION: 0
  FAULT-FORM-INTERIORITY: 0
  FAULT-FORM-CONJUNCTION: 0
  FAULT-FORM-COMPOUND-OBJECTS: 0
  FAULT-FORM-NO-VERB: 0
  FAULT-FORM-MULTI-SUBJECT: 0
  FAULT-CONSTRAINT-*: 0
  FAULT-PHYSICAL-ACTOR-ABSENT: 0
  FAULT-PHYSICAL-EXIT-INVALID: 0
  FAULT-HEADER-NARRATOR: 0
  FAULT-HEADER-GOAL: 0
file-level: FAIL
strict accept rate: 92.0%
```

---

## Header

- `narrator: taylor-hebert-westeros` — slug present in episode cast roster. PASS.
- `goal:` present and non-empty. PASS.

---

## Per-Line Verdicts (faults only; all other lines CORRECT)

---

### fault-001

- **id:** fault-001
- **type:** fault
- **line id:** 13
- **line content:** `census-officer speaks to the yard`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** Listener argument `the yard` names a location, not a valid listener entity (cast slug or group slug). The schema form is `<speaker> speaks to <listener-slug-or-group>`. `the yard` is a place, not a person or group. `to the yard` functions as a prepositional location phrase appended to an otherwise complete SVO.
- **why:** A dialogue beat with a location as listener cannot be cited by a dialogue file against a valid listener. Downstream, the dialogue facet author cannot assign spoken content to a recipient. The beat is unresolvable as authored.
- **criteria:** Replace `the yard` with the actual group being addressed — the assembled wards, or `the assembled group`, or individual ward slugs split across separate lines if the speech is directed sequentially. Fixer must produce a listener that is a person, slug, or group of persons, not a place.
- **recommended action:** RECAST-AS-HOLD or SPLIT-INTO-N — recast with a valid listener group (`the assembled wards` or named slugs), or split into separate `speaks to` lines per recipient if multiple.

---

### fault-002

- **id:** fault-002
- **type:** fault
- **line id:** 24
- **line content:** `census-officer speaks to the sept doors`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** Listener argument `the sept doors` names a fixed prop, not a person or group. The sept doors are a physical location element per the location card; they are not a listener entity. `to the sept doors` is a prepositional phrase naming a prop appended to a dialogue beat.
- **why:** Same downstream consequence as fault-001: no dialogue file can be authored against a prop listener. Additionally, this line encodes the dramatic beat of census-officer calling for the septon to open the doors — the actual listener is whoever is inside the sept, not the doors themselves. That information is lost in the current form.
- **criteria:** Replace `the sept doors` with the actual target of the speech — `the sept interior`, `the septon`, or an unnamed-but-person entity (`the ward inside`, `the occupants`). If the beat is a shout with no specific addressee, the dialogue facet can handle that with an unnamed listener slug; the proto-line must still name a person-class entity, not a prop.
- **recommended action:** RECAST-AS-HOLD — recast listener as person or person-group entity.

---

### fault-003

- **id:** fault-003
- **type:** fault
- **line id:** 48
- **line content:** `census-officer speaks to the yard`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** Identical fault to fault-001 at line 13. `the yard` is a location, not a valid listener entity.
- **why:** Same downstream consequence. Dialogue file cannot be authored against a location listener.
- **criteria:** Same as fault-001: replace `the yard` with a valid listener group.
- **recommended action:** RECAST-AS-HOLD — recast listener as person or person-group entity.

---

### fault-004

- **id:** fault-004
- **type:** fault
- **line id:** 58
- **line content:** `taylor-hebert-westeros holds the ledger`
- **fault class:** FAULT-PHYSICAL-PROP-ABSENT
- **what:** The ledger is in the clerk's possession throughout the scene. Line 11 establishes `clerk carries the ledger`. No intervening proto-line transfers the ledger to Taylor. The clerk uses the ledger for entries at lines 20, 45, 46. At line 58 (reordered, appearing after line 46 in the post-trim sequence), Taylor cannot physically hold the ledger because it has not been transferred to her.
- **why:** A hold-SVO against a prop the subject does not possess is physically impossible. The beat as written implies Taylor holds the physical ledger, which contradicts the prop chain. If the intent is Taylor's attention/gaze directed at the ledger, that is a perception beat (FAULT-FORM-PERCEPTION) — either way the line is illegal as authored. Downstream stitcher renders a physically impossible beat.
- **criteria:** Fixer must either (a) delete line 58 if no physical transfer of the ledger to Taylor is intended, (b) insert a prior proto-line establishing ledger transfer to Taylor before line 58, or (c) recast line 58 as a perception/attention beat using a legal form (e.g., a hold against Taylor's own body rather than the prop).
- **recommended action:** DELETE or RECAST-PHYSICAL.

---

## Constraint and Physical Checks — No Additional Findings

All active condition cards checked against all 50 non-blank lines:

- `cond-fauna-control-rules`: No fauna-control use appears in this file. Line 1 (`the ravens lift`) records a physical event with ravens as subject — consistent with ambient fauna behavior, no directed control implied. No constraint violation.
- `cond-impressment-census-120ac`: The census process (census-officer, clerk, ledger, name entry, status determination) is present and procedurally consistent with the card. Ward-protection invoked via letter (lines 27–31) matches the card's documented compliance mechanism. No violation.
- `cond-westerosi-customary-authority`: No deviation from the social physics encoded. Taylor's moves (produces letter, speaks when spoken to, turns when dismissed) are consistent with compliant-but-borderline smallfolk behavior under census authority. No violation.
- `cond-riverlands-120ac-state`: Ambient context consistent. No violation.
- `cond-no-parahuman-infrastructure`: No parahuman capability invoked. No violation.
- `cond-reincarnation-mechanics`: No reincarnation-specific content in proto-lines. No violation.
- `cond-series-tone-constraints`: Constraint applies to register and pace, not to proto-line form. Not evaluated at this pass level (pass 2 is per-line mechanic/constraint/physical only).
- Series laws and lore: No line names a law-violating event. No violation.
- Location card (loc-harrenhal-sept-environs): All actors present in the episode cast. Cart, ledger, ink case, letter are all plausible props for an arriving census party at this location. Exits referenced implicitly (road approach) are valid per the card. No exit-invalid faults.

---

## Fixer Routing

Four faults route to fixer:
- fault-001 (line 13), fault-002 (line 24), fault-003 (line 48): RECAST-AS-HOLD — replace location/prop listener with valid person or group entity.
- fault-004 (line 58): DELETE or RECAST-PHYSICAL — resolve prop possession chain or remove the line.
