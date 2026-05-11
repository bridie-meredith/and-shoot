```yaml
audit:
  scope: season
  target: s01
  pass: 2-reaudit-r3 (round 3 of 3 — iteration cap)
  timestamp: 2026-05-09
  verdict: FAIL
  verdict_summary: >
    Round 3 re-audit confirms all 30 round-2 findings remain resolved (per round-2-prime fixer
    confirmation). However, a large body of pre-existing faults unaudited across all three prior
    passes is present in the file: 60+ surviving violations spanning FAULT-FORM-MODIFIER
    (prepositional padding of all banned types, adjective/adverb modifiers on subjects and objects),
    FAULT-FORM-NON-ACTION-VERB (environment-state lines, collective-state lines), and
    FAULT-FORM-NO-VERB (bare intransitive motion verbs without destination). The 3 borderline
    items from the fixer dispatch: ID 250 and ID 702 confirmed faults; ID 905 remains advisory flag.
    This is the iteration cap. The Phase 2 Pass 2 convergence loop is exhausted. Escalation to
    user required with the full surviving fault inventory below.
```

---

# Season s01 Pass-2 Constraint Re-Audit — Round 3 (Final)

**File:** `active-project/theater/proto-lines/s01.aggregate.md`
**Prior audits:** rounds 1 and 2 (see paths in dispatch)
**Round-2-prime fixer confirmation:** all 30 round-2 findings RESOLVED-PRE-EXISTING in file
**This round scope:** full re-walk per dispatch; bias toward thoroughness
**Iteration status:** Round 3 of 3 — cap hit

---

## SECTION 0 — Verification of Round-2 Resolutions

All 30 round-2 fault findings confirmed resolved in the current file. Spot-checked:

| ID | Prior finding | Current state |
|---|---|---|
| 124 | fault-R001 recast regression | `the swallow stills` — CLOSED |
| 194 | fault-R002a | `the fly touches the basin rim` — CLOSED |
| 264 | fault-R002b | `the fly touches the pen rail` — CLOSED |
| 914 | fault-R003 bare intransitive | `a mounted man follows the column` — CLOSED |
| 915 | fault-R004 ordinal modifier | blank — CLOSED |
| 511 | fault-R004 ordinal modifier | `the collector's man rights the table` — CLOSED |
| 192 | fault-NUA-001 holds the pace | blank — CLOSED |
| 25 | fault-MIS-001 instrument phrase | `traces the column` — CLOSED |
| 97 | fault-MIS-003 source phrase | `pulls taylor-hebert-jaehaerys's hair` — CLOSED |
| 356 | fault-MIS-013 bare follows | `follows oc-craftsman-father` — CLOSED |
| 908 | fault-MIS-024 swarm-sense extends | blank — CLOSED |
| 911 | fault-MIS-025 voice rises | `oc-craftsman-mother calls` — CLOSED |

All other round-2 resolutions verified consistent with round-2-prime fixer log. **30/30 CLOSED.**

---

## SECTION 1 — Borderline Items (Fixer-Flagged for This Audit)

### ID 250: `taylor-hebert-jaehaerys traces the column again`

**Verdict: FAULT — confirmed.**

`again` is an adverb modifier. The schema bans all adverbs. The same pattern was corrected at ID 284 (fault-010, round 1) and ID 454 (fault-MIS-017, round 2). ID 250 was not in either prior finding set. The `again` context is recoverable from ID 25 (`traces the column`) earlier in the file.

---

### ID 702: `oc-craftsman-mother crosses to the sept lane entrance`

**Verdict: FAULT — confirmed.**

`to the sept lane entrance` is a prepositional phrase of destination. The schema explicitly bans `crosses to <X>` as a prepositional destination form; the fix is a transitive motion verb taking the destination as direct object. This pattern was corrected at IDs 666 and 679 (fault-MIS-019, round 2) and ID 693 (fault-MIS-022, round 2). ID 702 was not in either prior finding set.

---

### ID 905: `the dock mosquito circles`

**Verdict: FLAG — retained advisory, not promoted to fault.**

`circles` bare intransitive describes a motion pattern. The prior audit (flag-RA-003, round 2) treated this as a borderline flag rather than a fault, consistent with the treatment of `the hearth fire pops` (PASS — discrete object-as-subject acoustic event). `circles` is closer to a patterned motion than a destination-implied motion verb; the schema's bare-intransitive rule specifically targets motion verbs that `imply a destination.` A circling mosquito does not imply a specific destination. Retained as flag (Pass 4 trim candidate), not faulted.

---

## SECTION 2 — Surviving Faults Not in Any Prior Finding Set

The following faults were present in the file before any fixer pass and survived all three rounds undetected. They are clustered by fault class. All are line-scope.

---

### CLUSTER A — Adverb modifier `again` (FAULT-FORM-MODIFIER)

Same class as round-1 fault-010, round-2 fault-MIS-017.

- **r3-fault-001** — ID 250: `taylor-hebert-jaehaerys traces the column again`
  - `again` is an adverb modifier. Clean form: `taylor-hebert-jaehaerys traces the column`.

- **r3-fault-002** — ID 618: `oc-lords-steward marks the folio again`
  - `again` is an adverb modifier. Clean form: `oc-lords-steward marks the folio`.

---

### CLUSTER B — Prepositional destination `returns to X` / `crosses to X` / `rolls onto X` (FAULT-FORM-MODIFIER)

Same class as round-2 fault-MIS-019, fault-MIS-022.

- **r3-fault-003** — ID 20: `taylor-hebert-jaehaerys returns to the workshop doorway`
  - `to the workshop doorway` is a prepositional destination phrase. Recast with transitive motion verb: `taylor-hebert-jaehaerys approaches the workshop doorway` or `reaches the workshop doorway`.

- **r3-fault-004** — ID 47: `oc-craftsman-mother returns to the mordant station`
  - `to the mordant station` is a prepositional destination phrase. Clean form: `oc-craftsman-mother approaches the mordant station`.

- **r3-fault-005** — ID 120: `taylor-hebert-jaehaerys returns to the ledger bench`
  - `to the ledger bench` is a prepositional destination phrase. Clean form: `taylor-hebert-jaehaerys approaches the ledger bench` or `reaches the ledger bench`.

- **r3-fault-006** — ID 702: `oc-craftsman-mother crosses to the sept lane entrance`
  - (Already confirmed in Section 1 above.) Same fix: transitive motion verb.

- **r3-fault-007** — ID 67: `taylor-hebert-jaehaerys rolls onto the pallet`
  - `onto the pallet` is a prepositional destination phrase. The schema bans all prepositional padding. Recast: `taylor-hebert-jaehaerys reaches the pallet` (if motion-to is the beat) or split the roll gesture from the destination.

---

### CLUSTER C — Prepositional source `from X` (FAULT-FORM-MODIFIER)

Same class as round-2 fault-MIS-003, fault-MIS-005, fault-MIS-021.

- **r3-fault-008** — ID 28: `the fly lifts from the ink-pot rim`
  - `from the ink-pot rim` is a prepositional source phrase. Clean form: `the fly lifts`.

- **r3-fault-009** — ID 55: `taylor-hebert-jaehaerys rises from the bench`
  - `from the bench` is a prepositional source phrase. Clean form: `taylor-hebert-jaehaerys rises`.

- **r3-fault-010** — ID 59: `oc-craftsman-mother fills the bowl from the pot`
  - `from the pot` is a prepositional source phrase. Clean form: `oc-craftsman-mother fills the bowl`.

- **r3-fault-011** — ID 125: `the swallow lifts from the gutter`
  - `from the gutter` is a prepositional source phrase. Clean form: `the swallow lifts`.

- **r3-fault-012** — ID 160: `septon-rowan rises from the altar cloth`
  - `from the altar cloth` is a prepositional source phrase. Clean form: `septon-rowan rises`.

- **r3-fault-013** — ID 263: `a fly lifts from the livestock pen corner`
  - `from the livestock pen corner` is a prepositional source phrase. Clean form: `a fly lifts`.

- **r3-fault-014** — ID 668: `oc-craftsman-mother pulls her hands from the mordant cloth`
  - `from the mordant cloth` is a prepositional source phrase. Clean form: `oc-craftsman-mother pulls her hands`.

- **r3-fault-015** — ID 704: `oc-craftsman-mother enters the sept from the south lane`
  - `from the south lane` is a prepositional source phrase; `south` is additionally an adjective modifier on `lane`. Clean form: `oc-craftsman-mother enters the sept`.

---

### CLUSTER D — Prepositional location `at X` / `on X` (FAULT-FORM-MODIFIER)

Same class as round-2 fault-MIS-004, fault-MIS-020, fault-MIS-023.

- **r3-fault-016** — ID 11: `the flies cluster at the dye-yard drain`
  - `at the dye-yard drain` is a prepositional location phrase. Clean form: `the flies cluster`. Note: `the flies` is also a plural subject (multi-subject concern — see Cluster H).

- **r3-fault-017** — ID 13: `the beetles trace the floor seam by the vat`
  - `by the vat` is a prepositional location phrase. Additionally `the beetles` is plural (Cluster H). Clean form: `the beetles trace the floor seam` (modifier stripped; multi-subject concern separate).

- **r3-fault-018** — ID 54: `the dye-yard flies regroup at the drain`
  - `at the drain` is a prepositional location phrase. Clean form: `the dye-yard flies regroup`. Note: `regroup` is also borderline stative-collective (see Cluster G).

- **r3-fault-019** — ID 70: `the moth lands at the vent edge`
  - `at the vent edge` is a prepositional location phrase. Clean form: `the moth lands`.

- **r3-fault-020** — ID 353: `a clerk sets the census roll on the table`
  - `on the table` is a prepositional location phrase. Clean form: `a clerk sets the census roll`.

- **r3-fault-021** — ID 436: `the first townsman sets the coin on the table`
  - `on the table` is a prepositional location phrase; `first` is an ordinal adjective (Cluster E). Clean form: `the first townsman sets the coin` (both violations need correction; ordinal correction in Cluster E).

- **r3-fault-022** — ID 443: `the second townsman sets the grain sack on the stone`
  - `on the stone` is a prepositional location phrase; `second` is an ordinal adjective (Cluster E). Clean form: strip both.

- **r3-fault-023** — ID 479: `the animal-pen flies return to the rail`
  - `to the rail` is a prepositional destination phrase. Clean form: `the animal-pen flies return` (if return is sufficiently anchored by prior beats) or recast with transitive form.

---

### CLUSTER E — Adjective and adverb modifiers on subjects and objects (FAULT-FORM-MODIFIER)

Same class as round-1 fault-010, fault-008; round-2 fault-MIS-010, fault-MIS-016, fault-R004.

#### Ordinal adjectives on subjects (`first`, `second`, `lead`)

- **r3-fault-024** — ID 452: `the collector's man grabs the second townsman's sleeve`
  - `second` ordinal adjective in the possessive chain modifying `townsman`. Schema bans all adjectives. Strip `second`: `the collector's man grabs the townsman's sleeve`.

- **r3-fault-025** — ID 453: `the second townsman pulls the sleeve`
  - `second` ordinal on subject. Clean form: `the townsman pulls the sleeve`.

- **r3-fault-026** — ID 457: `the second townsman shoves the collector's man`
  - `second` ordinal on subject. Clean form: `the townsman shoves the collector's man`.

- **r3-fault-027** — ID 463: `the second horse shies`
  - `second` ordinal on subject. Clean form: `the horse shies`.

- **r3-fault-028** — ID 471: `the first collector scrambles`
  - `first` ordinal on subject. Clean form: `the collector scrambles`. Note: `scrambles` bare intransitive — see also Cluster F.

- **r3-fault-029** — ID 472: `the first collector's man runs`
  - `first` ordinal on subject. Also `runs` is a bare intransitive motion verb without destination (Cluster F). Both violations.

- **r3-fault-030** — ID 473: `the second collector's man covers his face`
  - `second` ordinal on subject. Clean form: `the collector's man covers his face`.

- **r3-fault-031** — ID 480: `the lead horse settles`
  - `lead` adjective on subject. Additionally `settles` is borderline stative (see Cluster G flag). Clean form for the adjective: `the horse settles`.

- **r3-fault-032** — ID 481: `the first collector's man wipes the forearm`
  - `first` ordinal on subject. Clean form: `the collector's man wipes the forearm`.

- **r3-fault-033** — ID 491: `the second collector's man lifts the levy roll`
  - `second` ordinal on subject. Clean form: `the collector's man lifts the levy roll`.

- **r3-fault-034** — ID 495: `the second collector speaks to oc-lords-steward`
  - `second` ordinal on subject. Clean form: `the collector speaks to oc-lords-steward`.

#### Ordinal adjectives on objects and listeners

- **r3-fault-035** — ID 436: `the first townsman sets the coin on the table`
  - `first` ordinal on subject. (Already logged under Cluster D for the location phrase; ordinal is a second fault on the same line.)

- **r3-fault-036** — ID 441: `the second townsman approaches the table`
  - `second` ordinal on subject. Clean form: `the townsman approaches the table`.

- **r3-fault-037** — ID 443: `the second townsman sets the grain sack on the stone`
  - `second` ordinal on subject. (Already logged under Cluster D; ordinal is a second fault.)

- **r3-fault-038** — ID 444: `the collector's man speaks to the second townsman`
  - `second` ordinal on listener object. Clean form: `the collector's man speaks to the townsman`.

- **r3-fault-039** — ID 445: `the second townsman speaks to the collector's man`
  - `second` ordinal on subject. Clean form: `the townsman speaks to the collector's man`.

- **r3-fault-040** — ID 448: `the second townsman speaks to the collector`
  - `second` ordinal on subject. Clean form: `the townsman speaks to the collector`.

- **r3-fault-041** — ID 450: `the second townsman speaks to the collector`
  - `second` ordinal on subject. (Duplicate of r3-fault-040 pattern at a second ID.)

- **r3-fault-042** — ID 464: `rymer-hedge grabs the second horse's bridle`
  - `second` ordinal in possessive chain on object. Clean form: `rymer-hedge grabs the horse's bridle`.

- **r3-fault-043** — ID 482: `rymer-hedge steadies the second horse`
  - `second` ordinal on object. Clean form: `rymer-hedge steadies the horse`.

- **r3-fault-044** — ID 494: `oc-lords-steward speaks to the second collector`
  - `second` ordinal on listener object. Clean form: `oc-lords-steward speaks to the collector`.

- **r3-fault-045** — ID 500: `oc-lords-steward speaks to the first collector`
  - `first` ordinal on listener object. Clean form: `oc-lords-steward speaks to the collector`.

- **r3-fault-046** — ID 516: `rymer-hedge releases the second horse's bridle`
  - `second` ordinal in possessive chain on object. Clean form: `rymer-hedge releases the horse's bridle`.

#### Other adjective / adverb modifiers

- **r3-fault-047** — ID 7: `taylor-hebert-jaehaerys reaches the front shutter`
  - `front` adjective on object. Clean form: `taylor-hebert-jaehaerys reaches the shutter`.

- **r3-fault-048** — ID 24: `oc-craftsman-father sets the ledger open`
  - `open` adjective/adverb modifier appended after the direct object. Same class as round-1 fault-008 (`holds the chin level`). Clean form: `oc-craftsman-father sets the ledger`.

- **r3-fault-049** — ID 69: `taylor-hebert-jaehaerys holds the eyes open`
  - `open` adjective/adverb modifier appended after the direct object. Same class as fault-048. Clean form: `taylor-hebert-jaehaerys holds the eyes`.

- **r3-fault-050** — ID 78: `the dye-yard spiders repair the drain-side web`
  - `drain-side` compound adjective on object `web`. Clean form: `the dye-yard spiders repair the web`.

- **r3-fault-051** — ID 148: `the new candle catches`
  - `new` adjective on subject. Clean form: `the candle catches`.

- **r3-fault-052** — ID 156: `taylor-hebert-jaehaerys opens the nearest volume`
  - `nearest` superlative adjective on object. Clean form: `taylor-hebert-jaehaerys opens the volume`.

- **r3-fault-053** — ID 182: `septon-rowan draws a second stool`
  - `second` ordinal on object. Clean form: `septon-rowan draws a stool`.

- **r3-fault-054** — ID 184: `septon-rowan opens a second volume`
  - `second` ordinal on object. Clean form: `septon-rowan opens a volume`.

- **r3-fault-055** — ID 235: `septon-rowan opens the second volume`
  - `second` ordinal on object. Clean form: `septon-rowan opens the volume`.

- **r3-fault-056** — ID 243: `septon-rowan returns the second volume to the shelf`
  - `second` ordinal on object; also `to the shelf` is a prepositional destination phrase (dual fault: Cluster B + this cluster). Clean form: `septon-rowan returns the volume` (both violations stripped; verb `returns` takes the volume as direct object).

- **r3-fault-057** — ID 326: `oc-craftsman-mother lifts the marketing basket`
  - `marketing` adjective/gerund modifier on object. Clean form: `oc-craftsman-mother lifts the basket`.

- **r3-fault-058** — ID 378: `oc-lords-steward draws the disputed column`
  - `disputed` past-participle adjective on object. Clean form: `oc-lords-steward draws the column`.

- **r3-fault-059** — ID 379: `the clerk marks the disputed entry`
  - `disputed` adjective on object. Clean form: `the clerk marks the entry`.

- **r3-fault-060** — ID 396: `oc-lords-steward faces the next household`
  - `next` adjective on object. Clean form: `oc-lords-steward faces the household`.

- **r3-fault-061** — ID 510: `the garrison man approaches the overturned table`
  - `overturned` past-participle adjective on object. Clean form: `the garrison man approaches the table`.

- **r3-fault-062** — ID 648: `rymer-hedge faces the east entrance`
  - `east` adjective on object. Clean form: `rymer-hedge faces the entrance`.

- **r3-fault-063** — ID 656: `oc-craftsman-father draws the workshop door closed`
  - `closed` adjective/adverb modifier appended after the direct object. Same class as fault-048, fault-049. Clean form: `oc-craftsman-father draws the workshop door`.

- **r3-fault-064** — ID 794: `oc-craftsman-mother sets the cup down`
  - `down` adverb modifier appended after the direct object. Clean form: `oc-craftsman-mother sets the cup`.

- **r3-fault-065** — ID 796: `the evening lamp catches`
  - `evening` adjective on subject. Clean form: `the lamp catches`.

- **r3-fault-066** — ID 802: `the traveling maester enters Fairstead`
  - `traveling` present-participle adjective on subject. Clean form: `the maester enters Fairstead`. Note: this is the first appearance of the maester slug; after this line the maester is referenced as `the maester` throughout. The `traveling` modifier is the only deviation.

- **r3-fault-067** — ID 808: `the maester draws the sealed folio`
  - `sealed` adjective on object. Clean form: `the maester draws the folio`.

- **r3-fault-068** — ID 893: `the maester draws the sealed return folio`
  - `sealed` adjective on object; `return` also functions as an adjective on `folio`. The prop is distinguished from other folios in the beat by these modifiers. Clean form: `the maester draws the folio` (context disambiguates which folio if prior beats establish it).

- **r3-fault-069** — ID 330: `the flat-bottom ferry grounds the near bank`
  - `flat-bottom` compound adjective on subject; `near` adjective on object. Dual FAULT-FORM-MODIFIER. Clean form: `the ferry grounds the bank`.

---

### CLUSTER F — Bare intransitive motion verbs without destination (FAULT-FORM-NO-VERB)

Same class as round-2 fault-MIS-013 (ID 356 `follows`, fixed), round-1 fault-038 (bare `follows`, fixed), round-2 fault-R003 (ID 914 `rides`, fixed).

- **r3-fault-070** — ID 322: `oc-craftsman-mother approaches`
  - `approaches` is a bare intransitive motion verb. No destination named. Clean form: add a destination slug or recast as a transitive motion verb taking the destination as direct object.

- **r3-fault-071** — ID 335: `rymer-hedge rides`
  - `rides` is a bare intransitive motion verb without destination. This is the same fault that was corrected at ID 914 (`a second mounted man rides` → `a mounted man follows the column`). `rymer-hedge rides` states only that the character is mounted and moving; it names no destination and records no discrete observable event.

- **r3-fault-072** — ID 400: `septon-rowan approaches`
  - `approaches` is a bare intransitive motion verb. No destination named. Same as r3-fault-070.

- **r3-fault-073** — ID 471: `the first collector scrambles`
  - `scrambles` is a bare intransitive motion verb (chaotic movement without destination). Ordinal modifier also faulted under Cluster E (r3-fault-028). Dual violation.

- **r3-fault-074** — ID 472: `the first collector's man runs`
  - `runs` is a bare intransitive motion verb without destination. Ordinal modifier also faulted under Cluster E (r3-fault-029). Dual violation.

---

### CLUSTER G — Environment-state and collective-state non-action verbs (FAULT-FORM-NON-ACTION-VERB)

Same class as prior-round fault clusters (fault-013 through fault-029, fault-036, etc.).

- **r3-fault-075** — ID 146: `the lamp glow shifts`
  - Subject `the lamp glow` is an ambient element. `shifts` describes the quality of light changing — an environment-state description, not a discrete physical act. Comparable to deleted lines `the square traffic adjusts` (fault-030, round 1) and `the workshop murmur rises` (fault-029, round 1). Route to loc-state facet.

- **r3-fault-076** — ID 413: `the retinue remounts`
  - `the retinue` is a collective multi-subject. `remounts` is a collective-state description (the group returning to mounts). Same class as `the column reassembles` (fault-036, round 1, deleted). The discrete physical act would be a named actor: `oc-lords-steward mounts` (ID 415 already exists).

- **r3-fault-077** — ID 416: `the column crosses the dock apron`
  - `the column` is a collective multi-subject. Same class as `the column halts` (ID 342, fixed to `a mounted man draws rein`). FAULT-FORM-MULTI-SUBJECT (collective). The discrete physical act for the column's crossing is covered by per-actor lines; delete or replace with a named actor.

- **r3-fault-078** — ID 517: `the column exits the square`
  - `the column` is a collective multi-subject. Same class as r3-fault-077 and prior closed faults. FAULT-FORM-MULTI-SUBJECT (collective).

- **r3-fault-079** — ID 733: `the workshop lane branches`
  - `the workshop lane` does not perform an act of branching; this is an environment-state/spatial-topology description. Loc-state facet material. FAULT-FORM-NON-ACTION-VERB.

- **r3-fault-080** — ID 734: `the market lane branches`
  - Same pattern as r3-fault-079. FAULT-FORM-NON-ACTION-VERB.

- **r3-fault-081** — ID 740: `the reeve's house door faces the lane`
  - `faces` here is a stative position-naming (the door is oriented toward the lane — a spatial fact, not a physical act). Compare to the schema's prohibition on `lies`, `sits`, `stands` as stative position-naming. `faces` used to describe a fixed architectural orientation is stative. FAULT-FORM-NON-ACTION-VERB. Route to loc-state facet.

- **r3-fault-082** — ID 54: `the dye-yard flies regroup at the drain`
  - `regroup` is a collective-state reform description (same class as `the square traffic re-forms`, fault-037, round 1, deleted). Subject is a fauna collective performing a stative-collective act. FAULT-FORM-NON-ACTION-VERB (collective-state). Additionally, `at the drain` is a location prepositional phrase (r3-fault-018 in Cluster D).

---

### CLUSTER H — Interiority: abstract noun as object of physical verb (FAULT-FORM-INTERIORITY)

- **r3-fault-083** — ID 468: `the lead horse throws its weight`
  - `its weight` is an abstract noun (weight is a quality, not a physical object). The physical act is the horse rearing/lunging; the `throws its weight` construction is a thought-figure for that motion. Compare to `the dock crowd shifts its weight` (fault-029, round 1, deleted). Additionally `lead` is an adjective modifier on subject (r3-fault-031 covers the ordinal; this is the interiority fault). The two faults are discrete: the adjective on subject plus the abstract object.

---

### CLUSTER I — Destination prepositional phrase appended to complete transitive SVO (FAULT-FORM-MODIFIER)

- **r3-fault-084** — ID 894: `the maester hands the return folio to the ferryman`
  - `to the ferryman` is a prepositional phrase of recipient/destination appended after the direct object. The schema bans all prepositional padding. Recast: `the maester passes the ferryman the return folio` (double-object form, no prepositional phrase) or `the maester offers the ferryman the return folio`. Note: `return folio` carries an adjective `return` modifier (r3-fault-068); both must be corrected.

---

## SECTION 3 — Items Confirmed Passing (Previously Contested or Now Checked)

| ID | Line | Status | Basis |
|---|---|---|---|
| 51 | `the hearth fire pops` | PASS | Object-as-subject discrete event, licensed |
| 68 | `a moth circles the loft vent gap` | PASS | `circles` transitive with location as direct object |
| 93 | `a horsefly circles the yard post` | PASS | Same |
| 159 | `a fly circles the baptismal basin rim` | PASS | Same |
| 247 | `the baptismal basin fly orbits the basin rim` | PASS | Transitive, object as direct object |
| 330 verb | `grounds the near bank` verb form | PASS (verb) | Transitive taking location as direct object; adjective modifiers faulted separately |
| 333 | `the retinue rounds the river bend` | PASS (verb+object) | Transitive; prior audits passed after adjective strip; collective concern below threshold for established precedent |
| 412 | `rymer-hedge shifts the eyes` | FLAG (retained from round 2) | Borderline gaze-direction; editor advisory |
| 675 | `the workshop door closes` | PASS | Object-as-subject discrete event, licensed |
| 904 | `the sept fly orbits the baptismal basin rim` | PASS | Transitive with location as direct object |
| 905 | `the dock mosquito circles` | FLAG | See Section 1 |

---

## SECTION 4 — Structure and Constraint Checks

### Header and POV markers

All 5 POV markers present and correctly slugged. Verified:
- Before ID 1: `# pov: taylor-hebert-jaehaerys` ✓
- Before ID 565: `# pov: mira-stonefield-jaehaerys` ✓
- Before ID 645: `# pov: taylor-hebert-jaehaerys` ✓
- Before ID 701: `# pov: oc-craftsman-mother` ✓
- Before ID 789: `# pov: taylor-hebert-jaehaerys` ✓

No per-episode delimiters. Top-of-file 4-line comment header intact. **PASS.**

### Constraint-coherence

No new constraint-coherence violations identified. Active-cost ceiling: correctly depicted in IGNITION beat with Taylor's headache onset (IDs 490, 519 now blank — cost is left implicit in surrounding beats, appropriate). Suppression-policy stage: maester beat is correctly Stage 1 (documentary). Smallfolk political physics: Mira's behavior consistent with card. No parahuman vocabulary. **PASS.**

### ID gaps

ID 389 (legal deletion), ID 752 (legal deletion between 751 and 753), IDs 901–903 (pre-existing deletions), ID 913 (pre-existing deletion), ID 915 (blank per fault-R004 resolution). All confirmed legal. **PASS.**

### Slug resolution

No orphan slugs. All slugs resolved per round-1 verification, unchanged. **PASS.**

---

## SECTION 5 — Consolidated Fault Inventory

| Fault ID | IDs affected | Class | Cluster |
|---|---|---|---|
| r3-fault-001 | 250 | FAULT-FORM-MODIFIER (adverb `again`) | A |
| r3-fault-002 | 618 | FAULT-FORM-MODIFIER (adverb `again`) | A |
| r3-fault-003 | 20 | FAULT-FORM-MODIFIER (destination `returns to`) | B |
| r3-fault-004 | 47 | FAULT-FORM-MODIFIER (destination `returns to`) | B |
| r3-fault-005 | 120 | FAULT-FORM-MODIFIER (destination `returns to`) | B |
| r3-fault-006 | 702 | FAULT-FORM-MODIFIER (destination `crosses to`) | B |
| r3-fault-007 | 67 | FAULT-FORM-MODIFIER (destination `onto`) | B |
| r3-fault-008 | 28 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-009 | 55 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-010 | 59 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-011 | 125 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-012 | 160 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-013 | 263 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-014 | 668 | FAULT-FORM-MODIFIER (source `from`) | C |
| r3-fault-015 | 704 | FAULT-FORM-MODIFIER (source `from` + adjective) | C+E |
| r3-fault-016 | 11 | FAULT-FORM-MODIFIER (location `at`) | D |
| r3-fault-017 | 13 | FAULT-FORM-MODIFIER (location `by`) | D |
| r3-fault-018 | 54 | FAULT-FORM-MODIFIER (location `at`) + NON-ACTION-VERB | D+G |
| r3-fault-019 | 70 | FAULT-FORM-MODIFIER (location `at`) | D |
| r3-fault-020 | 353 | FAULT-FORM-MODIFIER (location `on`) | D |
| r3-fault-021 | 436 | FAULT-FORM-MODIFIER (location `on`) + ordinal | D+E |
| r3-fault-022 | 443 | FAULT-FORM-MODIFIER (location `on`) + ordinal | D+E |
| r3-fault-023 | 479 | FAULT-FORM-MODIFIER (destination `to`) | D |
| r3-fault-024 | 452 | FAULT-FORM-MODIFIER (ordinal in possessive) | E |
| r3-fault-025 | 453 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-026 | 457 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-027 | 463 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-028 | 471 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-029 | 472 | FAULT-FORM-MODIFIER (ordinal) + NO-VERB | E+F |
| r3-fault-030 | 473 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-031 | 480 | FAULT-FORM-MODIFIER (adjective on subject) | E |
| r3-fault-032 | 481 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-033 | 491 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-034 | 495 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-035 | 436 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-036 | 441 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-037 | 443 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-038 | 444 | FAULT-FORM-MODIFIER (ordinal on listener) | E |
| r3-fault-039 | 445 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-040 | 448 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-041 | 450 | FAULT-FORM-MODIFIER (ordinal on subject) | E |
| r3-fault-042 | 464 | FAULT-FORM-MODIFIER (ordinal in possessive) | E |
| r3-fault-043 | 482 | FAULT-FORM-MODIFIER (ordinal on object) | E |
| r3-fault-044 | 494 | FAULT-FORM-MODIFIER (ordinal on listener) | E |
| r3-fault-045 | 500 | FAULT-FORM-MODIFIER (ordinal on listener) | E |
| r3-fault-046 | 516 | FAULT-FORM-MODIFIER (ordinal in possessive) | E |
| r3-fault-047 | 7 | FAULT-FORM-MODIFIER (adjective on object) | E |
| r3-fault-048 | 24 | FAULT-FORM-MODIFIER (modifier appended after object) | E |
| r3-fault-049 | 69 | FAULT-FORM-MODIFIER (modifier appended after object) | E |
| r3-fault-050 | 78 | FAULT-FORM-MODIFIER (compound adjective on object) | E |
| r3-fault-051 | 148 | FAULT-FORM-MODIFIER (adjective on subject) | E |
| r3-fault-052 | 156 | FAULT-FORM-MODIFIER (superlative adjective on object) | E |
| r3-fault-053 | 182 | FAULT-FORM-MODIFIER (ordinal on object) | E |
| r3-fault-054 | 184 | FAULT-FORM-MODIFIER (ordinal on object) | E |
| r3-fault-055 | 235 | FAULT-FORM-MODIFIER (ordinal on object) | E |
| r3-fault-056 | 243 | FAULT-FORM-MODIFIER (ordinal + destination) | E+B |
| r3-fault-057 | 326 | FAULT-FORM-MODIFIER (gerund adjective on object) | E |
| r3-fault-058 | 378 | FAULT-FORM-MODIFIER (participial adjective on object) | E |
| r3-fault-059 | 379 | FAULT-FORM-MODIFIER (participial adjective on object) | E |
| r3-fault-060 | 396 | FAULT-FORM-MODIFIER (adjective on object) | E |
| r3-fault-061 | 510 | FAULT-FORM-MODIFIER (participial adjective on object) | E |
| r3-fault-062 | 648 | FAULT-FORM-MODIFIER (adjective on object) | E |
| r3-fault-063 | 656 | FAULT-FORM-MODIFIER (modifier appended after object) | E |
| r3-fault-064 | 794 | FAULT-FORM-MODIFIER (adverb appended after object) | E |
| r3-fault-065 | 796 | FAULT-FORM-MODIFIER (adjective on subject) | E |
| r3-fault-066 | 802 | FAULT-FORM-MODIFIER (participial adjective on subject) | E |
| r3-fault-067 | 808 | FAULT-FORM-MODIFIER (adjective on object) | E |
| r3-fault-068 | 893 | FAULT-FORM-MODIFIER (adjective on object) | E |
| r3-fault-069 | 330 | FAULT-FORM-MODIFIER (adjective on subject + object) | E |
| r3-fault-070 | 322 | FAULT-FORM-NO-VERB (bare intransitive motion) | F |
| r3-fault-071 | 335 | FAULT-FORM-NO-VERB (bare intransitive motion) | F |
| r3-fault-072 | 400 | FAULT-FORM-NO-VERB (bare intransitive motion) | F |
| r3-fault-073 | 471 | FAULT-FORM-NO-VERB (bare intransitive motion) | F |
| r3-fault-074 | 472 | FAULT-FORM-NO-VERB (bare intransitive motion) | F |
| r3-fault-075 | 146 | FAULT-FORM-NON-ACTION-VERB (environment-state) | G |
| r3-fault-076 | 413 | FAULT-FORM-MULTI-SUBJECT (collective) | G |
| r3-fault-077 | 416 | FAULT-FORM-MULTI-SUBJECT (collective) | G |
| r3-fault-078 | 517 | FAULT-FORM-MULTI-SUBJECT (collective) | G |
| r3-fault-079 | 733 | FAULT-FORM-NON-ACTION-VERB (environment-state) | G |
| r3-fault-080 | 734 | FAULT-FORM-NON-ACTION-VERB (environment-state) | G |
| r3-fault-081 | 740 | FAULT-FORM-NON-ACTION-VERB (stative position-naming) | G |
| r3-fault-082 | 54 | FAULT-FORM-NON-ACTION-VERB (collective-state) | G |
| r3-fault-083 | 468 | FAULT-FORM-INTERIORITY (abstract object) | H |
| r3-fault-084 | 894 | FAULT-FORM-MODIFIER (destination `to`) | I |

**Total distinct fault findings: 84**
**Distinct IDs affected: approximately 70** (some IDs carry two fault classes)

---

## SECTION 6 — Advisory Flags (no fixer dispatch)

| Flag ID | ID | What | Status |
|---|---|---|---|
| r3-flag-001 | 905 | `the dock mosquito circles` — bare intransitive, borderline | Retained advisory from round 2 (flag-RA-003) |
| r3-flag-002 | 412 | `rymer-hedge shifts the eyes` — borderline gaze-direction | Retained advisory from round 2 (flag-RA-002) |
| r3-flag-003 | 763 | `oc-craftsman-mother fills the two cups` — possible compound-object | Retained advisory from round 1 (fault-017) |
| r3-flag-004 | 344 | `a mounted man tethers the horses` — `the horses` plural object; possible compound-object | New advisory; if tethering is sequential, two proto-lines required |
| r3-flag-005 | 793 | `taylor-hebert-jaehaerys faces the table surface` — `surface` borderline specification vs. compound noun | Advisory for editor |
| r3-flag-006 | 480 | `the lead horse settles` — `settles` borderline stative after rearing | `lead` adjective faulted under r3-fault-031; `settles` advisory only |
| r3-flag-007 | 855 | `the maester speaks to taylor-hebert-jaehaerys` — dialogue-beat advisory | Retained from round 1 (flag-001) |
| r3-flag-008 | 302 | `oc-child-peer calls` — bare vocalization advisory | Retained from round 1 (flag-002) |

---

## SECTION 7 — Routing Recommendation

| Fault cluster | IDs | Recommended fix action |
|---|---|---|
| Cluster A — adverb `again` | 250, 618 | Strip `again` |
| Cluster B — destination prep phrases | 20, 47, 67, 120, 243, 479, 702 | Replace `returns to X` / `crosses to X` with transitive motion verb |
| Cluster C — source prep phrases | 28, 55, 59, 125, 160, 263, 668, 704 | Strip `from X` |
| Cluster D — location prep phrases | 11, 13, 54, 70, 353, 436, 443 | Strip `at/on/by X` |
| Cluster E — adjective modifiers | 7, 24, 69, 78, 148, 156, 182, 184, 235, 243, 326, 330, 378, 379, 396, 436, 441, 443, 444, 445, 448, 450, 452, 453, 457, 463, 464, 471, 472, 473, 480, 481, 482, 491, 494, 495, 500, 510, 516, 648, 656, 794, 796, 802, 808, 893 | Strip adjective/ordinal/participial modifiers |
| Cluster F — bare intransitive motion | 322, 335, 400, 471, 472 | Add named destination or recast |
| Cluster G — environment/collective state | 54, 146, 413, 416, 517, 733, 734, 740 | Delete or replace with named-actor discrete-act alternative |
| Cluster H — abstract object | 468 | Recast `throws its weight` as the discrete physical motion |
| Cluster I — destination prep on complete SVO | 894 | Recast `hands X to Y` using double-object or alternative transitive form |

**No escalation above season scope is required for any individual finding.** All faults are line-scope and editable in place.

---

## SECTION 8 — Iteration Cap Notice

This is **Round 3 of 3** of the Phase 2 Pass 2 convergence loop. The loop is now exhausted.

**Verdict: FAIL.**

The prior three rounds closed 43 + 30 = 73 faults. The 84 surviving findings in this report were present in the file throughout all three rounds but were not caught by either the round-1 or round-2 audits. They fall into two overlapping categories:

1. **Systemic prepositional phrase violations** (Clusters B, C, D, I): `from X`, `to X`, `at X`, `on X` patterns that appear throughout the file from the earliest beats. These are the most common writer-failure mode noted in the Pass 1 brief but were inconsistently audited in prior rounds.

2. **Adjective modifier violations** (Cluster E): ordinal adjectives (`first`, `second`, `lead`) and descriptive adjectives (`new`, `nearest`, `overturned`, `disputed`, `sealed`, `traveling`, `evening`, `marketing`, `drain-side`) on subjects and objects throughout. These were corrected only at the specific IDs the prior auditors named (IDs 284, 454, 511, 915) but the same pattern persisted at 40+ additional IDs.

**Phase 2 Pass 3 (shape / dramatist) cannot dispatch.** The Pass 2 constraint pass has not converged.

**Escalation to user required.** The failing-finding list is the complete inventory in Section 5 above (r3-fault-001 through r3-fault-084). The user must decide: (a) authorize a fourth fixer pass against this expanded finding set, extending the loop past the 3-iteration cap; (b) accept the file with surviving violations and proceed to Pass 3 with known defects; or (c) route the entire aggregate back to the screen-writer for a clean re-authoring pass against the strict SVO discipline brief, using the surviving-fault inventory as a constraint list.
