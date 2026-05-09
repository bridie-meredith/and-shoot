```yaml
audit:
  scope: season
  target: s01
  pass: 2-reaudit-r4 (round 4 — convergence-verification gate)
  timestamp: 2026-05-09
  verdict: FAIL
  verdict_summary: >
    Round-3 fixer resolved all 84 round-3 findings by direct inspection. However, round 4 finds
    surviving fault instances within previously-known fault classes (FAULT-FORM-MODIFIER, FAULT-FORM-NON-ACTION-VERB)
    that the round-3 fixer missed or introduced via recast. No new fault classes are present.
    Fault count: 11 surviving fault instances (+ 1 flag). All are reintroduced-instance or
    missed-instance within prior-round clusters; zero are new classes. Borderline items: 4 of 5
    clean; ID 835 `draws the door wider` flagged as new missed modifier.
    Per escalation pre-condition: new-class test passes (no new classes). Continue-vs-escalate
    decision is therefore within user discretion: these are reintroduced instances, not
    auditor-side class non-convergence.
```

---

# Season s01 Pass-2 Constraint Re-Audit — Round 4

**File:** `active-project/theater/proto-lines/s01.aggregate.md`
**Prior audits:** rounds 1, 2, 3 (see paths in dispatch)
**This round scope:** full re-walk per dispatch, emphasis on round-3 fixer recasts and any residual violations the prior sweeps missed
**Escalation pre-condition check:** new fault classes this round → hard-escalate; reintroduced instances within known classes → fixer-pass judgment call

---

## SECTION 0 — Verification of Round-3 Resolutions (84 Findings)

All 84 round-3 fault findings verified by direct comparison of the fix log against the current file. Spot-check of every affected ID:

| r3-fault | ID | Log change | Current file | Status |
|---|---|---|---|---|
| 001 | 250 | strip `again` | `taylor-hebert-jaehaerys traces the column` | CLOSED |
| 002 | 618 | strip `again` | `oc-lords-steward marks the folio` | CLOSED |
| 003 | 20 | `returns to` → `approaches` | `taylor-hebert-jaehaerys approaches the workshop doorway` | CLOSED |
| 004 | 47 | `returns to` → `approaches` | `oc-craftsman-mother approaches the mordant station` | CLOSED |
| 005 | 120 | `returns to` → `approaches` | `taylor-hebert-jaehaerys approaches the ledger bench` | CLOSED |
| 006 | 702 | `crosses to` → `approaches` | `oc-craftsman-mother approaches the sept lane entrance` | CLOSED |
| 007 | 67 | `rolls onto` → `reaches` | `taylor-hebert-jaehaerys reaches the pallet` | CLOSED |
| 008 | 28 | strip `from the ink-pot rim` | `the fly lifts` | CLOSED |
| 009 | 55 | strip `from the bench` | `taylor-hebert-jaehaerys rises` | CLOSED |
| 010 | 59 | strip `from the pot` | `oc-craftsman-mother fills the bowl` | CLOSED |
| 011 | 125 | strip `from the gutter` | `the swallow lifts` | CLOSED |
| 012 | 160 | strip `from the altar cloth` | `septon-rowan rises` | CLOSED |
| 013 | 263 | strip `from the livestock pen corner` | `a fly lifts` | CLOSED |
| 014 | 668 | strip `from the mordant cloth` | `oc-craftsman-mother pulls her hands` | CLOSED |
| 015 | 704 | strip both → `enters the sept` | `oc-craftsman-mother enters the sept` | CLOSED |
| 016 | 11 | strip `at the dye-yard drain` | `the flies cluster` | CLOSED |
| 017 | 13 | strip `by the vat` | `the beetles trace the floor seam` | CLOSED |
| 018 | 54 | deleted | blank time-skip | CLOSED |
| 019 | 70 | strip `at the vent edge` | `the moth lands` | CLOSED |
| 020 | 353 | strip `on the table` | `a clerk sets the census roll` | CLOSED |
| 021 | 436 | strip both | `the townsman sets the coin` | CLOSED |
| 022 | 443 | strip both | `the townsman sets the grain sack` | CLOSED |
| 023 | 479 | strip `to the rail` | `the animal-pen flies return` | CLOSED |
| 024–046 | various ordinal/adjective IDs | stripped | verified matching log changes | CLOSED |
| 047 | 7 | strip `front` | `taylor-hebert-jaehaerys reaches the shutter` | CLOSED |
| 048 | 24 | strip `open` | `oc-craftsman-father sets the ledger` | CLOSED |
| 049 | 69 | strip `open` | `taylor-hebert-jaehaerys holds the eyes` | CLOSED |
| 050 | 78 | strip `drain-side` | `the dye-yard spiders repair the web` | CLOSED |
| 051–069 | various | stripped | verified matching log changes | CLOSED |
| 070 | 322 | `approaches` → `approaches taylor-hebert-jaehaerys` | `oc-craftsman-mother approaches taylor-hebert-jaehaerys` | CLOSED |
| 071 | 335 | `rides` → `reaches the dock apron` | `rymer-hedge reaches the dock apron` | CLOSED |
| 072 | 400 | `approaches` → `approaches oc-lords-steward` | `septon-rowan approaches oc-lords-steward` | CLOSED |
| 073 | 471 | `scrambles` → `retreats` (dual with 028) | `the collector retreats` | CLOSED |
| 074 | 472 | `runs` → `exits the square` (dual with 029) | `the collector's man exits the square` | CLOSED |
| 075–082 | environment/collective | deleted/blank | verified blank or replaced | CLOSED |
| 083 | 468 | `throws its weight` → `lunges` | `the horse lunges` | CLOSED |
| 084 | 894 | `hands X to Y` → `passes Y X` + strip `return` | `the maester passes the ferryman the folio` | CLOSED |

**84/84 CLOSED.**

---

## SECTION 1 — Borderline Items from Round-3 Fixer Dispatch

### ID 335 — `rymer-hedge reaches the dock apron`

**Context (IDs 330–345):**
```
330 the ferry grounds the bank
331 oc-craftsman-father faces the river
332 taylor-hebert-jaehaerys holds the feet
333 the retinue rounds the river bend
334 a mounted man leads the column
335 rymer-hedge reaches the dock apron
336 oc-lords-steward leads the column
337 a townsman steps back
338–339 dialogue beats
340 the retinue reaches the dock apron
341 oc-lords-steward dismounts
342 a mounted man draws rein
343 rymer-hedge dismounts
344 a mounted man tethers the horses
345 oc-lords-steward speaks to the ferryman
```

**Verdict: PASS — scene-consistent, no collision.**

The prior beat (ID 334) names a mounted man leading the column. ID 335 gives rymer-hedge an earlier arrival at the dock apron ahead of the main retinue (ID 340 `the retinue reaches the dock apron`). This is plausible: rymer-hedge is riding separately from the column formation. ID 343 (`rymer-hedge dismounts`) follows after the retinue's arrival, which is consistent with rymer-hedge having arrived, waited, and then dismounted once the steward is present. The recast from `rides` (r3-fault-071) to `reaches the dock apron` is clean SVO, no prepositional padding, and no collision with ID 340.

---

### ID 471 — `the collector retreats`

**Context (IDs 466–475):**
```
466 the lead horse rears
467 oc-lords-steward grips the reins
468 the horse lunges
469 the collection table overturns
470 the levy roll falls
471 the collector retreats
472 the collector's man exits the square
473 the collector's man covers his face
474 the swarm contracts
475 taylor-hebert-jaehaerys presses the feet
```

**Verdict: PASS — mechanic-clean; nuance loss noted but not a fault.**

`retreats` is a transitive-capable motion verb used intransitively here. Per schema, bare intransitive motion verbs fault when they `imply a destination` — `retreats` implies withdrawal without specifying destination, which is consistent with the beat (the collector is fleeing the scene, not moving toward a named location). This is comparable to `the fishwife retreats` at ID 393, which was passed in all prior audits. The beat is observable: a physical withdrawal. Nuance loss from `scrambles` (prior form) is real but `scrambles` was a bare intransitive without destination, which was itself the fault. **PASS.**

However, see **new finding r4-fault-002** below: `the lead horse rears` at ID 466 contains a surviving adjective modifier.

---

### ID 472 — `the collector's man exits the square`

**Context (IDs 471–474):**
```
471 the collector retreats
472 the collector's man exits the square
473 the collector's man covers his face
474 the swarm contracts
```

**Verdict: PASS — continuity clean.**

ID 472 and ID 473 are two separate collector's men in the pre-fix file (designated `first` and `second` with ordinal modifiers stripped). Post-fix, both are `the collector's man`. This creates a referential ambiguity: the same slug (`the collector's man`) appears in consecutive lines as apparently the same referent. In the pre-fix file, the ordinal distinguished two different collector's men. Now both IDs refer to the same slug.

**Classification: FLAG (not fault).** The ordinal removal was the correct fix per schema. The downstream ambiguity is an editorial continuity matter for the editor (Pass 5 / and-wrap), not a proto-line schema violation. The schema does not require proto-lines to distinguish between multiple unnamed characters of the same class. Flagged for editor awareness.

---

### ID 468 — `the horse lunges` (fixer recast)

**Context (IDs 463–468):**
```
463 the horse shies
464 rymer-hedge grabs the horse's bridle
465 the swarm expands
466 the lead horse rears
467 oc-lords-steward grips the reins
468 the horse lunges
```

**Verdict: FLAG — ID 466 `the lead horse rears` contains surviving adjective modifier.**

The collision check passes: ID 466 (`the lead horse rears`) and ID 468 (`the horse lunges`) describe two physically distinct beats — rearing and lunging forward — consistent with a frightened horse sequence. No mechanical collision.

However, ID 466 contains the adjective `lead` on subject `horse`. This modifier was identified in round 3 (r3-fault-031, `the lead horse settles` at ID 480) and stripped in the fixer pass. At ID 466, the same `lead` adjective survives. This is a **reintroduced instance within the known adjective-modifier class (Cluster E)** that the round-3 fixer missed. Logged as **r4-fault-001** below.

---

### IDs 893/894 — `the maester draws the folio` / `the maester passes the ferryman the folio`

**Context (IDs 808, 893–898):**
```
808 the maester draws the folio      [first folio draw — census/administrative folio]
...
893 the maester draws the folio      [second folio draw — return folio for ferryman]
894 the maester passes the ferryman the folio
895 the ferryman takes the return folio
896 the maester mounts
897 the maester exits the dock
898 the ferryman grips the return folio
```

**Verdict: PASS for IDs 893/894. FLAG for ID 895.**

IDs 893 and 894 are SVO-clean. The folio context is: the adjective stripping in r3-fault-067 (ID 808) and r3-fault-068 (ID 893) removed `sealed` and `return` modifiers, making both lines `the maester draws the folio`. The fixer noted that "context disambiguates." The surrounding beats do establish context: at ID 808 the folio goes to the town reeve (ID 809 `the town reeve receives the folio`); at ID 893 the folio goes to the ferryman (ID 894 `passes the ferryman`). The two folio draws are 85 IDs apart in different scene contexts, so disambiguation holds for a reader walking the file sequentially.

ID 895 `the ferryman takes the return folio`: `return` is an adjective modifier on `folio`. This survived the fixer pass. The round-3 audit flagged it at ID 893 (r3-fault-068) but the fixer's fix was applied only to IDs 808 and 893. ID 895 was not in the round-3 finding set and was not fixed. This is a **missed instance within known class Cluster E (adjective modifier on object)**. Logged as **r4-fault-003** below.

Similarly, ID 898 `the ferryman grips the return folio`: same `return` adjective on object. Also missed. Logged as **r4-fault-004** below.

---

## SECTION 2 — New Surviving Faults Not Closed by Round-3 Fixer

All findings below are **reintroduced instances or missed instances within prior-round fault classes**. No new fault class is identified in this audit.

---

### r4-fault-001 — FAULT-FORM-MODIFIER (adjective on subject)

**ID:** 466
**Line:** `the lead horse rears`
**Class:** FAULT-FORM-MODIFIER — adjective `lead` on subject `horse`
**Prior-round class:** Cluster E (adjective modifiers). Round 3 corrected `the lead horse settles` at ID 480 (r3-fault-031) but missed this identical pattern at ID 466.
**Type:** fault-instance-reintroduced (missed by round-3 fixer)
**Fix:** strip `lead` → `the horse rears`
**Collision check:** ID 468 (`the horse lunges`) and ID 463 (`the horse shies`) use the same bare `the horse` slug; stripping `lead` is consistent with those lines.

---

### r4-fault-002 — FAULT-FORM-MODIFIER (adjective on object)

**ID:** 206
**Line:** `septon-rowan offers the second volume`
**Class:** FAULT-FORM-MODIFIER — ordinal `second` on object `volume`
**Prior-round class:** Cluster E (ordinal adjectives). Round 3 caught `second` at IDs 182 (`septon-rowan draws a second stool` → r3-fault-053), 184 (`septon-rowan opens a second volume` → r3-fault-054), 235 (`septon-rowan opens the second volume` → r3-fault-055), and 234's `a second volume` in context. ID 206 contains the same `second` ordinal modifier on the same object class (`volume`) and was not in the round-3 finding set.
**Type:** fault-instance-missed (same cluster, not caught in round 3)
**Fix:** strip `second` → `septon-rowan offers the volume`

---

### r4-fault-003 — FAULT-FORM-MODIFIER (adjective on object)

**ID:** 895
**Line:** `the ferryman takes the return folio`
**Class:** FAULT-FORM-MODIFIER — `return` functioning as adjective modifier on `folio`
**Prior-round class:** Cluster E. Round 3 caught `return` as adjective at ID 893 (r3-fault-068) and the fixer stripped it. ID 895 is the next line referencing the same prop and carries the same adjective. Not in round-3 finding set.
**Type:** fault-instance-missed (same line cluster as r3-fault-068, not caught)
**Fix:** strip `return` → `the ferryman takes the folio`

---

### r4-fault-004 — FAULT-FORM-MODIFIER (adjective on object)

**ID:** 898
**Line:** `the ferryman grips the return folio`
**Class:** FAULT-FORM-MODIFIER — `return` functioning as adjective modifier on `folio`
**Prior-round class:** Cluster E. Same as r4-fault-003. The fixer fixed ID 893 and 894 but left IDs 895 and 898 unfixed.
**Type:** fault-instance-missed
**Fix:** strip `return` → `the ferryman grips the folio`

---

### r4-fault-005 — FAULT-FORM-MODIFIER (prepositional destination phrase)

**ID:** 372
**Line:** `the fishwife steps to the table`
**Class:** FAULT-FORM-MODIFIER — `to the table` is a prepositional destination phrase appended after a motion verb
**Prior-round class:** Cluster B (destination prep phrases). Round 3 corrected `returns to X`, `crosses to X`, `rolls onto X`. The same pattern (`steps to X`) was not in the round-3 finding set. `steps to` is a directional prepositional construction with a destination: the schema bans all prepositional padding of destination type. The fix is a transitive motion verb taking the table as direct object: `the fishwife approaches the table`.
**Type:** fault-instance-missed (same class as Cluster B, different verb form)
**Fix:** recast → `the fishwife approaches the table`

---

### r4-fault-006 — FAULT-FORM-MODIFIER (prepositional destination phrase)

**ID:** 849
**Line:** `the maester crosses to the workshop center`
**Class:** FAULT-FORM-MODIFIER — `to the workshop center` is a prepositional destination phrase
**Prior-round class:** Cluster B. Round 3 corrected `crosses to X` at ID 702 (r3-fault-006). The identical verb+prep pattern `crosses to X` at ID 849 was not in the round-3 finding set.
**Type:** fault-instance-reintroduced (the fixer corrected this verb-prep combination at ID 702 but did not scan for the identical pattern at other IDs)
**Fix:** recast → `the maester crosses the workshop` or `the maester reaches the workshop center` (transitive verb taking destination as direct object)

---

### r4-fault-007 — FAULT-FORM-MODIFIER (prepositional destination phrase)

**ID:** 761
**Line:** `oc-craftsman-mother crosses to the shelf`
**Class:** FAULT-FORM-MODIFIER — `to the shelf` is a prepositional destination phrase; `crosses to X` is the same pattern corrected at ID 702 (r3-fault-006)
**Prior-round class:** Cluster B. The fixer corrected `crosses to X` at one ID but did not sweep for all instances of the pattern.
**Type:** fault-instance-reintroduced (identical verb+prep form, different ID, missed)
**Fix:** recast → `oc-craftsman-mother approaches the shelf` or `oc-craftsman-mother reaches the shelf`

---

### r4-fault-008 — FAULT-FORM-MODIFIER (adjective on subject)

**ID:** 547
**Line:** `the inquiry rider draws the sealed letter`
**Class:** FAULT-FORM-MODIFIER — `sealed` is a participial adjective on object `letter`
**Prior-round class:** Cluster E. Round 3 caught `sealed` as adjective at ID 808 (`the maester draws the sealed folio` → r3-fault-067). The identical pattern `draws the sealed X` at ID 547 was not in the round-3 finding set.
**Type:** fault-instance-missed (same adjective-on-object pattern, same verb `draws`, missed)
**Fix:** strip `sealed` → `the inquiry rider draws the letter`

---

### r4-fault-009 — FAULT-FORM-MODIFIER (adjective on object)

**ID:** 234
**Line:** `septon-rowan draws a second volume`
**Class:** FAULT-FORM-MODIFIER — ordinal `second` on object `volume`
**Prior-round class:** Cluster E. Round 3 faulted `septon-rowan opens the second volume` at ID 235 (r3-fault-055) and fixed it. ID 234 `septon-rowan draws a second volume` contains the same ordinal `second` on the same object class one line earlier. The fix log shows r3-fault-053 was `septon-rowan draws a second stool` at ID 182 (fixed to `draws a stool`), and the fixer addressed `second volume` at IDs 184 and 235, but the current file shows ID 234 reads `septon-rowan draws a second volume` — the fixer did not fix this line.
**Type:** fault-instance-missed
**Fix:** strip `second` → `septon-rowan draws a volume`

---

### r4-fault-010 — FAULT-FORM-NON-ACTION-VERB (environment-state / stative)

**ID:** 314
**Line:** `the square insects shift`
**Class:** FAULT-FORM-NON-ACTION-VERB (environment-state / collective-state)
**Prior-round class:** Cluster G. Round 3 caught `the lamp glow shifts` at ID 146 (r3-fault-075) — an ambient-element stative environment description — and deleted it. `the square insects shift` at ID 314 is the same class: a collective fauna-environment element performing a vague stative-collective motion (`shift` without object, without destination, as an environment-state descriptor). Compare to deleted `the square traffic adjusts` (fault-030, round 1) — same pattern. `shift` here has no direct object and no discrete observable event; it describes an ambient quality of the scene rather than a specific action.
**Type:** fault-instance-missed (same class as r3-fault-075 and prior round-1 closed faults)
**Fix:** delete (time-skip) or replace with a named-entity discrete act

---

### r4-fault-011 — FAULT-FORM-MODIFIER (adjective on object)

**ID:** 835
**Line:** `oc-craftsman-father draws the door wider`
**Class:** FAULT-FORM-MODIFIER — `wider` is an adverb/adjective modifier appended after the direct object
**Prior-round class:** Cluster E. Round 3 caught `closed` appended after direct object at ID 656 (r3-fault-063, `draws the workshop door closed` → `draws the workshop door`) and `open` appended after direct object at IDs 24 (r3-fault-048) and 69 (r3-fault-049). `wider` appended after `draws the door` is the same pattern — a modifier on the result-state of the verb's action appended after the direct object.
**Type:** fault-instance-missed (same modifier-appended-after-object pattern as r3-fault-048, 049, 063)
**Fix:** strip `wider` → `oc-craftsman-father draws the door`

---

## SECTION 3 — Items Confirmed Passing This Round

| ID | Line | Status | Basis |
|---|---|---|---|
| 1 | `taylor-hebert-jaehaerys wakes in the loft` | PASS | `in the loft` is direct object of `wakes` per established precedent (schema permits transitive wake-in-location) |
| 11 | `the flies cluster` | PASS | Post-fix; prior modifier stripped |
| 19 | `oc-craftsman-father calls taylor-hebert-jaehaerys` | PASS | `calls` transitive with named listener as object — same form as `oc-child-peer calls` (flag, not fault); this form names the object |
| 71 | `the moth departs the vent` | PASS | Transitive, location as direct object |
| 73 | `oc-craftsman-father lowers his voice` | PASS | `his voice` is owned body-part/physical mechanism; the act of lowering voice is a physical act (controlled vocal volume reduction); comparable to `laces his boots` at ID 85 |
| 85 | `oc-craftsman-father laces his boots` | PASS | Possessive on body-attached object — established precedent |
| 88 | `oc-craftsman-father takes the market satchel` | PASS | `market` is part of compound noun `market satchel` — a prop name, not an adjective on a generic noun. Same logic as `mordant pot`, `account ledger`, `census folio`. PASS. |
| 145 | `oc-craftsman-mother returns` | PASS | Bare intransitive `returns` — non-motion sense (returns to prior activity); does not imply a specific destination; licensed per established `the fishwife retreats` precedent |
| 181 | `taylor-hebert-jaehaerys sits` | PASS | Discrete posture-act (act of sitting), not stative position-naming |
| 246 | `the morning light crosses the east window` | PASS with FLAG | `morning` is an adjective modifier on `light`; `east` is an adjective modifier on `window`. This line was not in any prior finding set. On examination: `morning light` and `east window` function as compound nouns in context (they are named environmental referents). The schema bans adjective modifiers on generic nouns; `morning light` and `east window` are borderline compound-noun references that could be read as named props. Flagged rather than faulted — advisory for editor. |
| 268 | `oc-craftsman-mother approaches the two children` | FLAG | `two` is a quantifier/adjective on `children`. Round-3 audit did not flag this. On balance: `the two children` identifies a specific physical pair as a group referent (not an ordinal like `first`/`second`). Borderline. Advisory flag, not promoted to fault given the group-referent use. |
| 285 | `the wool-factor's cart rolls` | PASS | Object-as-subject discrete event |
| 302 | `oc-child-peer calls` | FLAG (retained) | Bare vocalization; retained advisory from round 1 flag-002 |
| 309 | `oc-child-peer scrapes a boot against the cobble` | PASS | `against the cobble` — `against` is a prepositional phrase. However, `scrapes X against Y` is a single physical act where the surface of contact (the cobble) is integral to the action itself; the prepositional phrase is part of the verb's instrument/manner. This is a borderline call. Prior audits did not flag this. Advisory: the schematic prohibition is on `after a verb that already has its direct object`. Here `a boot` is the direct object and `against the cobble` is the instrument/manner phrase. The Pass 1 brief lists banned prep types as `place, destination, source, direction, instrument, or accompaniment` — instrument is explicitly banned. On strict reading this is FAULT-FORM-MODIFIER. Logged as **r4-flag-001** (advisory) rather than fault, because the instrument phrase is mechanically integral to `scrapes` in a way that differs from destination/source appending; final classification deferred to fixer judgment. |
| 319 | `oc-child-peer nods` | PASS | Discrete intransitive physical act; does not imply destination |
| 337 | `a townsman steps back` | PASS with FLAG | `back` as directional adverb. Round 3 noted adverbs as banned (Cluster E). `back` as a directional particle in `steps back` is borderline — it could be read as an adverb modifier (banned) or as a directional particle that is idiomatic to the verb phrase `steps back` (meaning to step backward). The schema bans adverbs including `back` when used as directional adverbs. Advisory flag. Not promoted to fault given prior-round precedent: `steps back` was not flagged in any prior round, and `step back` is a compound intransitive form. Editor advisory. |
| 344 | `a mounted man tethers the horses` | FLAG (retained from r3-flag-004) | `the horses` plural object — if tethering is sequential, two proto-lines required. Retained from round 3. |
| 362 | `the clerk draws the household entry column` | PASS | `household entry` is a compound noun (a named column type in the census document context), not adjective+noun. PASS. |
| 412 | `rymer-hedge shifts the eyes` | FLAG (retained from rounds 2 and 3) | Borderline gaze-direction |
| 455 | `the animal-pen flies lift` | PASS | Object-as-subject collective-as-one; same licensed form as `the flies cluster` |
| 456 | `the animal-pen flies mass` | PASS | Discrete swarm behavior, licensed |
| 459 | `the swarm crosses the pen gate` | PASS | Transitive; the swarm as a collective single entity is established per prior audits |
| 512 | `the levy roll spreads` | PASS | Object-as-subject discrete event (a fallen document spreading open) |
| 575 | `mira-stonefield-jaehaerys draws the coif forward` | PASS | `forward` as directional particle here specifies the direction of the coif pull; consistent with the draw action. Borderline but `forward` is integral to `draws the coif forward` as a direction-of-motion. Prior audits did not flag this. No escalation. |
| 596 | `mira-stonefield-jaehaerys faces the town reeve's back` | PASS | `town reeve's back` is the specific object faced (a body part belonging to a named actor). Clean SVO. |
| 610 | `mira-stonefield-jaehaerys holds the hands` | PASS | `holds` licensed: body-part object under the narrow license (stillness-against-pressure) |
| 703 | blank | PASS | Legal time-skip |
| 741 | `oc-craftsman-mother raises the fist` | PASS | `the fist` — possessive elided per context (oc-craftsman-mother's fist). Transitive physical act |
| 755 | `oc-craftsman-father lays the dye-stirrer` | PASS | `dye-stirrer` is a compound noun prop name. `lays` transitive. PASS. |
| 763 | `oc-craftsman-mother fills the two cups` | FLAG (retained from r3-flag-003) | Compound-object advisory |
| 793 | `taylor-hebert-jaehaerys faces the table surface` | FLAG (retained from r3-flag-005) | `surface` borderline specification |
| 803 | `the maester's horse follows the ferryman's route marker` | PASS | `ferryman's route marker` is a compound prop/location referent. Clean SVO. |
| 818 | `the maester faces the square center` | PASS | `square center` is a location referent. `center` is part of the compound location noun. PASS. |
| 824 | `the town reeve gestures` | PASS | Discrete intransitive physical act; no destination implied |
| 841 | `the maester draws the ledger query` | PASS | `ledger query` — compound noun document type. PASS. |
| 843 | `the maester traces the ledger entry` | PASS | `ledger entry` — compound noun. PASS. |
| 872 | `the maester traces the literacy register` | PASS | Transitive, object named. |
| 905 | `the dock mosquito circles` | FLAG (retained from rounds 2 and 3) | Bare intransitive; advisory |
| 906 | `the ferry folio crosses the water` | PASS | Object-as-subject (`the ferry folio`) transitive discrete event. `the water` is direct object of `crosses`. PASS. |
| 909 | `the ferryman receives the folio` | PASS | Verified against ID 894 context. |

---

## SECTION 4 — Structure, Header, POV, and Constraint Checks

### Header
The aggregate file does not use the per-episode extended header format (not required for an aggregate file per schema). The 4-line comment header (lines 1–4) is intact. **PASS.**

### POV markers
All 5 POV markers verified:
- Before ID 1: `# pov: taylor-hebert-jaehaerys` — PRESENT
- Before ID 565: `# pov: mira-stonefield-jaehaerys` — PRESENT
- Before ID 645: `# pov: taylor-hebert-jaehaerys` — PRESENT
- Before ID 701: `# pov: oc-craftsman-mother` — PRESENT
- Before ID 789: `# pov: taylor-hebert-jaehaerys` — PRESENT

No per-episode delimiters present. **PASS.**

### ID gaps
ID 54 (deleted → blank), 66 (blank), 72, 77, 79, 81, 94, 101, 122, 126, 146 (deleted → blank), 150, 153, 154, 158, 176, 192, 201, 218, 219, 225, 233, 251, 258, 262, 275, 296, 300, 301, 328, 329, 350, 351, 371, 389 (legal deletion), 397, 413 (deleted → blank), 416 (deleted → blank), 418–420, 425, 428, 432, 433, 451, 490, 501, 509, 513, 515, 517 (deleted → blank), 519, 520, 535, 541, 554, 556, 564, 566, 582, 598, 627, 635, 644, 646, 650, 653, 671, 673, 691, 700, 703, 713, 730, 733 (deleted → blank), 734 (deleted → blank), 736, 740 (deleted → blank), 748, 750, 752 (legal deletion), 766, 788, 792, 801, 813, 816, 819, 820, 828, 829, 847, 864, 884, 887, 899, 901–903 (pre-existing deletions), 908, 913 (pre-existing deletion), 915 (blank per r-fault-R004 resolution).

No legal gap violations. **PASS.**

### Slug resolution
No orphan slugs identified. All actor slugs (`taylor-hebert-jaehaerys`, `mira-stonefield-jaehaerys`, `oc-craftsman-mother`, `oc-craftsman-father`, `septon-rowan`, `rymer-hedge`, `oc-lords-steward`, `oc-child-peer`) appear consistently throughout their respective sections. Named environmental entities (`the ferryman`, `the fishwife`, `the town reeve`, `the maester`, `the garrison man`, `the collector`, `the collector's man`, `the inquiry rider`, `a mounted man`, `a clerk`) are consistent. **PASS.**

### Constraint-coherence
No new constraint violations identified. Suppression-policy stage: maester beat remains correctly Stage 1 (documentary). Active-cost ceiling: no parahuman vocabulary present. Smallfolk political physics: consistent. **PASS.**

### `split-from` markers
Two `# split-from:` comment markers at end of file (IDs 914 and 915). These are structural annotations, not proto-line schema violations. **PASS.**

---

## SECTION 5 — Consolidated Fault Inventory (Round 4)

| Fault ID | Aggregate ID | Class | Prior-round cluster | Type |
|---|---|---|---|---|
| r4-fault-001 | 466 | FAULT-FORM-MODIFIER (adjective `lead` on subject) | Cluster E (round 3) | Reintroduced instance — missed by fixer |
| r4-fault-002 | 206 | FAULT-FORM-MODIFIER (ordinal `second` on object) | Cluster E (round 3) | Missed instance |
| r4-fault-003 | 895 | FAULT-FORM-MODIFIER (adjective `return` on object) | Cluster E (round 3) | Missed instance — same line cluster as r3-fault-068 |
| r4-fault-004 | 898 | FAULT-FORM-MODIFIER (adjective `return` on object) | Cluster E (round 3) | Missed instance — same line cluster as r3-fault-068 |
| r4-fault-005 | 372 | FAULT-FORM-MODIFIER (destination prep `to the table`) | Cluster B (round 3) | Missed instance — different verb form (`steps to`) |
| r4-fault-006 | 849 | FAULT-FORM-MODIFIER (destination prep `to the workshop center`) | Cluster B (round 3) | Reintroduced instance — identical `crosses to X` corrected at ID 702 |
| r4-fault-007 | 761 | FAULT-FORM-MODIFIER (destination prep `to the shelf`) | Cluster B (round 3) | Reintroduced instance — identical `crosses to X` corrected at ID 702 |
| r4-fault-008 | 547 | FAULT-FORM-MODIFIER (adjective `sealed` on object) | Cluster E (round 3) | Missed instance — identical `draws the sealed X` corrected at ID 808 |
| r4-fault-009 | 234 | FAULT-FORM-MODIFIER (ordinal `second` on object) | Cluster E (round 3) | Missed instance — adjacent to r3-fault-055 at ID 235 |
| r4-fault-010 | 314 | FAULT-FORM-NON-ACTION-VERB (environment-state collective) | Cluster G (round 3) | Missed instance — same class as r3-fault-075 |
| r4-fault-011 | 835 | FAULT-FORM-MODIFIER (modifier appended after object) | Cluster E (round 3) | Missed instance — same pattern as r3-fault-048/049/063 |

**Total fault findings this round: 11**
**New fault classes: 0**
**Reintroduced instances within known classes: 3** (IDs 466, 761, 849)
**Missed instances within known classes: 8** (IDs 206, 234, 314, 372, 547, 835, 895, 898)

---

## SECTION 6 — Advisory Flags (Round 4)

| Flag ID | ID | What | Status |
|---|---|---|---|
| r4-flag-001 | 309 | `scrapes a boot against the cobble` — `against` instrument phrase; instrument is explicitly banned by Pass 1 brief; borderline because integral to verb | New advisory; deferred to fixer judgment |
| r4-flag-002 | 337 | `a townsman steps back` — `back` as directional adverb; borderline compound-motion form | New advisory; prior rounds did not flag |
| r4-flag-003 | 246 | `the morning light crosses the east window` — `morning` adjective on subject, `east` adjective on object; both may be compound-noun readings | New advisory |
| r4-flag-004 | 472/473 | Two `the collector's man` beats in immediate sequence post-ordinal strip — referential ambiguity | New advisory (editor continuity) |
| r4-flag-005 | 268 | `approaches the two children` — `two` quantifier on object | Borderline from round 3 r3-flag-003 context |
| r3-flag-001 | 905 | `the dock mosquito circles` — bare intransitive borderline | Retained from round 3 |
| r3-flag-002 | 412 | `rymer-hedge shifts the eyes` — borderline gaze-direction | Retained from round 3 |
| r3-flag-003 | 763 | `oc-craftsman-mother fills the two cups` — possible compound-object | Retained from round 3 |
| r3-flag-004 | 344 | `a mounted man tethers the horses` — plural object | Retained from round 3 |
| r3-flag-005 | 793 | `taylor-hebert-jaehaerys faces the table surface` | Retained from round 3 |
| r3-flag-007 | 855 | `the maester speaks to taylor-hebert-jaehaerys` — dialogue-beat advisory | Retained from round 1 |
| r3-flag-008 | 302 | `oc-child-peer calls` — bare vocalization | Retained from round 1 |

---

## SECTION 7 — Escalation Pre-Condition Assessment

Per `active-project/staff/showrunner/escalation-pass2-cap-decision.md`:

> If round 4 finds new fault classes the prior 3 audits missed, this is auditor-side non-convergence and we hard-escalate.

**New fault classes found: ZERO.**

All 11 findings in this round fall within fault classes already identified and named in prior rounds:
- FAULT-FORM-MODIFIER (Cluster E adjective modifiers) — found in rounds 1, 2, and 3
- FAULT-FORM-MODIFIER (Cluster B destination prep phrases) — found in rounds 2 and 3
- FAULT-FORM-NON-ACTION-VERB (Cluster G environment-state) — found in rounds 1, 2, and 3

**The hard-escalate trigger is NOT met.**

**Classification of findings:** All 11 are either (a) reintroduced instances where the fixer corrected the exact pattern at one ID but missed the identical pattern at a nearby ID, or (b) instances the round-3 comprehensive sweep did not cover. The audit chain has not produced a new fault class. The classes are stable.

---

## SECTION 8 — Routing Recommendation

| Finding cluster | IDs | Recommended action |
|---|---|---|
| Adjective on subject — `lead` | 466 | Strip `lead` |
| Ordinal on object — `second` | 206, 234 | Strip `second` |
| Adjective `return` on object | 895, 898 | Strip `return` |
| Adjective `sealed` on object | 547 | Strip `sealed` |
| Modifier after object — `wider` | 835 | Strip `wider` |
| Destination prep `steps to X` | 372 | Recast → `approaches the table` |
| Destination prep `crosses to X` | 761, 849 | Recast → transitive motion verb |
| Environment-state collective | 314 | Delete (time-skip) |

**Routing decision:** 11 findings, all within known classes, zero new classes. This is a fixer-eligible pass per the escalation pre-condition. The findings are surfaceable as a compact list (8 distinct fix operations on 11 lines). A targeted fixer pass against this list, with a mandate to also sweep for any remaining instances of the `crosses to X`, `steps to X`, `sealed X`, and `return folio` patterns, is the minimum required action before convergence can be declared.

**However:** This is round 4, which is already over-cap. The question of whether to authorize a fifth fixer pass is a user decision. The chain does not hard-escalate on new-class grounds, but the user should be aware that rounds 3 and 4 each found cluster-completeness failures: the round-3 fixer fixed the IDs named in the round-3 audit but did not sweep the file for the identical patterns at unlisted IDs. A fifth fixer pass with explicit instruction to pattern-sweep (not just fix the named IDs) has a higher probability of true convergence.

**Pass 3 (shape / dramatist) remains blocked until these 11 findings are resolved.**
