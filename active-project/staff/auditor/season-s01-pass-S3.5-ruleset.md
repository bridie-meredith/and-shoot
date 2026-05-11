# Audit Report — Season s01 Pass S3.5 — Ruleset Compliance (Mechanic-Strictness)
# schema: schemas/audit-report.schema.md
# generated: 2026-05-11
# auditor-fork: Phase 3 Pass S3.5 cycle 2 re-fire
# target: active-project/theater/proto-lines/s01.bones.md
# cycle: 2 (cycle-1 archived at season-s01-pass-S3.5-ruleset-cycle1.md)
# file-level verdict: RULESET-FAIL

---

## Scope

Full walk of all numbered non-blank lines in `active-project/theater/proto-lines/s01.bones.md` (active bones, IDs 1–517 with gaps, following cycle-2 additions). Evaluated against:
- Non-action-verb deny-list (full list per brief + schema)
- `holds` narrow license
- Mechanic re-check: copulas, negations, perception verbs, modifiers, conjunctions, abstractions-as-objects
- Drift-pattern report (verb ≥5 instances as borderline state-verb)
- Idiom-depletion check (URI-007, 2026-05-10): physical-stasis idioms ≥10 instances
- Cycle-1 fault + flag resolution verification
- New bones 509–517 deny-list scan

Bias: when in doubt, flag.

---

## Cycle-1 resolution check

| cycle-1 id | type | bone(s) | resolution status |
|---|---|---|---|
| fault-001 | fault | 166 — `oc-tanner-father holds the step` | RESOLVED. Bone 166 now reads `oc-tanner-father stills`. Licensed intransitive stasis. |
| flag-002 | flag | 226, 274, 355, 449 — `the headache wakes taylor` | RESOLVED. All 4 instances recast to `taylor-hebert-flea-bottom wakes`. Interiority-as-subject removed. |
| flag-001 | flag | 318 — `oc-tanner-mother sits` | STANDING. Bone 318 still reads `oc-tanner-mother sits`. No recast. Cycle-1 flagged for screen-writer intent confirmation; no confirmation recorded. Carry forward as flag-001. |
| flag-003 | flag | 235 — `moves the family possessions` | STANDING. Screen-writer optional; no change made. Carry forward as flag-003. |
| flag-004 | flag | season-wide `holds <body-part>` pattern | STANDING. Count unchanged at 12 licensed instances. No systematic recast performed. Carry forward as flag-004 with updated `stills` count context. |
| flag-005 | flag | 14, 170, 171, 496, 504 — `stills` count | UPDATED. Count now 7 (was 5 at cycle-1; fault-001 fix added bone 166, new bone 517 adds a 7th). See idiom-depletion section below. |
| flag-006 | flag | file-level structure — no narrator/goal headers | STANDING. File still has no episode-section delimiters or narrator/goal headers. Carry forward as flag-006. |

Dispatch claim: "6 abstract-object relay beats recast." Verified by absence — no abstract-relay faults were found in cycle-1; the 6 recasts occurred prior to cycle-1 and the cycle-1 auditor treated surviving relay beats as within the established fauna-relay design. Remaining abstract-relay beats are accounted under flag-007 below.

---

## Checks run — clean passes

| Check | Result |
|---|---|
| Copulas (`is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being`) | CLEAN — zero instances |
| Negations (`didn't`, `does not`, `won't`, etc.) | CLEAN — zero instances |
| Perception verbs (`read`, `took`, `tracked`, `noted`, `counted`, `measured`, `watches`, `sees`, `hears`, `notices`) | CLEAN — zero instances |
| Conjunctions (`and`, `but`, `while`, `as`) | CLEAN — zero instances |
| Multi-subject lines | CLEAN — zero instances |
| Dialogue form (`speaks to <listener>`) | CLEAN — all dialogue beats follow licensed form; no spoken content embedded |
| Deny-list: possession verbs | CLEAN |
| Deny-list: sustained-carrying verbs | CLEAN |
| Deny-list: containment verbs | CLEAN |
| Deny-list: `lies`, `stands` | CLEAN |
| `holds` narrow license | CLEAN — 12 licensed instances (body-part stillness only), 0 unlicensed. Cycle-1 fault-001 resolved. |
| Idiom-depletion (URI-007): `holds the feet` | 6 instances (bones 89, 142, 288, 463, 472, 503) — below 10-instance threshold. No depletion flag. |
| Idiom-depletion (URI-007): `holds the eyes` | 5 instances (bones 42, 227, 275, 356, 450) — below 10-instance threshold. No depletion flag. |
| Idiom-depletion (URI-007): `holds the chin` | 1 instance (bone 13) — below threshold. |
| Idiom-depletion (URI-007): `stills` | 7 instances (bones 14, 166, 170, 171, 496, 504, 517) — below 10-instance threshold. No depletion flag. See flag-005 carry-forward for monitoring note. |
| New bones 509–517: deny-list scan | CLEAN — see detailed scan below. |

---

## New bones 509–517 — deny-list scan

| bone | line | verdict |
|---|---|---|
| 509 | `the flies relay the carter` | CLEAN. Subject: fauna. Verb: `relay`. Object: role-noun (person), concrete. |
| 510 | `the carter exits the junction` | CLEAN. Standard transitive motion SVO. |
| 511 | `taylor-hebert-flea-bottom faces the junction` | CLEAN. `faces` transitive with location object. |
| 512 | `oc-tanner-elder faces the road` | CLEAN. Same form. |
| 513 | `the beetles relay the base room` | CLEAN. Object is a concrete location. |
| 514 | `the beetles relay oc-broken-maester` | CLEAN. Object is an actor slug. |
| 515 | `taylor-hebert-flea-bottom writes the entry` | CLEAN. Established pattern throughout file. |
| 516 | `taylor-hebert-flea-bottom exhales` | CLEAN. Licensed intransitive. |
| 517 | `taylor-hebert-flea-bottom stills` | CLEAN. Licensed intransitive stasis onset; adds 1 to `stills` count (now 7, below 10-instance threshold). |

No deny-list violations in bones 509–517.

---

## Findings

---

### fault-002

- **id:** fault-002
- **type:** fault
- **bone:** 66
- **line:** `the reeve slows the step`
- **what:** Transitive verb `slows` with object `the step`. `the step` is a motion-unit abstraction — the word denotes a locomotion increment ("mid-stride"), not a physical object that can be acted upon. `slows the step` encodes deceleration of pace, which is a kinematic-state modification, not a discrete physical act on a concrete object. This is the same pattern as cycle-1 fault-001 (`oc-tanner-father holds the step`): a motion-unit idiom disguised as transitive SVO. Per schema: "Abstraction-as-object is INTERIORITY. A physical verb whose object is an abstract noun faults FAULT-FORM-INTERIORITY." `the step` is abstract; the FAULT-FORM-INTERIORITY rule applies. Cycle-1 did not identify this bone; it is a new finding in cycle-2.
- **why:** The stitcher receives a transitive SVO implying a concrete object was acted upon. The rendered prose will encode the reeve acting on `the step` as if it were a physical thing. The facet pass has no concrete object to anchor sensory or location-state facets against this beat.
- **fault-class:** FAULT-FORM-INTERIORITY (abstract object)
- **criteria:** Recast bone 66 to an observable physical act encoding deceleration. Options: `the reeve slows` (intransitive — if the verb lands cleanly without a destination); `the reeve shortens the stride` (if stride is treated as a body-part analog under the narrow holds license, though it is not a body part — reject this path); preferred recast: `the reeve stills` or `the reeve stops` if the pause is complete, or delete and let the context carry the deceleration, or add a new bone for the physical act the deceleration precedes. Do not use `the step` as object.
- **scope:** episode — single bone.
- **route:** fixer

---

### fault-003

- **id:** fault-003
- **type:** fault
- **bone:** 19
- **line:** `oc-tanner-father steps toward the yard`
- **what:** Motion verb `steps` followed by prepositional phrase `toward the yard`. Per schema: "Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned (FAULT-FORM-MODIFIER)." `toward the yard` is a prepositional phrase of direction. The schema's licensed form for directional orientation is `pivots toward <X>`, explicitly named in the schema; no other verb is licensed to take `toward` as a directional prepositional phrase. `steps toward` is not on the license list. The schema instructs: "prefer transitive verbs that take the location as direct object — `enters the yard` is clean; `moves to the yard` is not." `steps toward the yard` follows the same structure as the banned `moves to the yard`. Cycle-1 reported modifier check as CLEAN but did not identify this bone; the cycle-1 clean-pass for modifiers was erroneous with respect to bone 19.
- **why:** `toward the yard` is prepositional padding appended to a complete intransitive SVO (`oc-tanner-father steps`). The stitcher inherits a directional modifier that belongs in a loc-state facet, not the bone itself. Downstream: the motion direction is baked into the bone rather than available as a facet citation.
- **fault-class:** FAULT-FORM-MODIFIER
- **criteria:** Recast to a transitive verb with the location as direct object. Options: `oc-tanner-father enters the yard` (if the entry is what the beat encodes); `oc-tanner-father crosses the yard` (if traversal is intended). If the beat encodes orientation-only (not yet entry), use `oc-tanner-father faces the yard`. Choose whichever encodes the actual physical event. Do not use `steps toward`.
- **scope:** episode — single bone.
- **route:** fixer

---

### flag-001 (carried from cycle-1)

- **id:** flag-001
- **type:** flag
- **bone:** 318
- **line:** `oc-tanner-mother sits`
- **what:** Intransitive `sits` — ambiguous between discrete act of sitting down (licensed) and stative position descriptor (FAULT-FORM-NON-ACTION-VERB). Context (bones 315–316: mother enters room, enters base room; bone 317: faces taylor; bone 318: sits; bone 319: taylor faces mother) most plausibly encodes the discrete act of sitting. However, no screen-writer confirmation has been recorded.
- **why:** Ambiguity propagates to stitcher. If stative, non-action verb contaminates the bone layer.
- **criteria:** N/A (flag). Screen-writer must confirm: discrete act → no change; stative → recast or route to loc-state facet.
- **scope:** episode — single bone.
- **route:** screen-writer for intent confirmation; fixer if stative confirmed.

---

### flag-003 (carried from cycle-1)

- **id:** flag-003
- **type:** flag
- **bone:** 235
- **line:** `the lords-man's man moves the family possessions`
- **what:** Generic transitive `moves` with collective-noun object `the family possessions`. Not on deny-list; not a clear fault. Signal: under-specified physical act.
- **why:** Stitcher has no specific physical manner encoded (drag, carry, stack). Minor weakening of action signal.
- **criteria:** N/A (screen-writer optional). Consider recasting to more specific transitive (`clears`, `removes`, `carries out`).
- **scope:** episode — single bone.
- **route:** screen-writer optional.

---

### flag-004 (carried from cycle-1, updated)

- **id:** flag-004
- **type:** flag
- **bone:** all active bones (season aggregate)
- **drift-pattern:** `holds <body-part>` — 12 licensed instances. Breakdown: `holds the chin` ×1 (bone 13), `holds the eyes` ×5 (bones 42, 227, 275, 356, 450), `holds the feet` ×6 (bones 89, 142, 288, 463, 472, 503). Count unchanged from cycle-1. No mandatory recast action taken.
- **what:** `holds <body-part>` remains the dominant physical-stasis encoding pattern across the season bones. The verb-object construction is individually licensed but collectively dense. The 25% recast recommendation from cycle-1 was not actioned.
- **why:** Idiom fatigue at stitching time.
- **criteria:** N/A (flag). Screen-writer: review and diversify at minimum 3 of the 12 instances before Phase 4 split.
- **scope:** season-scope.
- **route:** screen-writer.

---

### flag-005 (carried from cycle-1, updated)

- **id:** flag-005
- **type:** flag
- **bone:** 14, 166, 170, 171, 496, 504, 517
- **drift-pattern:** `stills` — 7 instances (up from 5 in cycle-1; cycle-1 predicted 6 after fault-001 fix; bone 517 adds a 7th). Bones: 14 (`oc-tanner-father stills`), 166 (`oc-tanner-father stills`, cycle-1 fix), 170 (`oc-tanner-father stills`), 171 (`oc-tanner-mother stills`), 496 (`taylor-hebert-flea-bottom stills`), 504 (`taylor-hebert-flea-bottom stills`), 517 (`taylor-hebert-flea-bottom stills`, new bone).
- **what:** Seven instances of `stills`. Approaching pattern density. Below 10-instance depletion threshold. However, each addition has grown the count: cycle-1 predicted 6 and the new bone pushed it to 7. If additional bones continue using `stills`, the depletion threshold may be reached in Phase 4.
- **why:** Sustained growth across cycles. At 7 instances, `stills` is now alongside `holds the eyes` (5) in frequency and surpasses it if counted per-verb rather than per-idiom. No immediate depletion trigger; threshold monitoring required.
- **criteria:** N/A (flag). Screen-writer: no new `stills` bones without a corresponding diversity review. If Phase 4 additions push to 10, depletion flag auto-triggers.
- **scope:** season-scope.
- **route:** screen-writer monitoring.

---

### flag-006 (carried from cycle-1)

- **id:** flag-006
- **type:** flag
- **bone:** N/A (file-level structure)
- **what:** `s01.bones.md` still contains no episode-section delimiters (`# === episode: <slug> ===`) and no per-section `narrator:` / `goal:` headers. The file header remains a comment block only. No resolution from cycle-1.
- **why:** Schema aggregate format not satisfied. Pass 5 narrator-consistency and Phase 4 Step 3.2 extended-header generation both depend on resolvable per-episode headers.
- **criteria:** N/A (flag). Before Phase 4 split: either add delimiters and headers, or document in the file header that this file is a flat season-bones artifact operating outside the aggregate spec (and confirm that Pass 5 will receive narrator context by another path).
- **scope:** season-scope (file structure).
- **route:** showrunner or screen-writer to confirm format intent.

---

### flag-007 (new)

- **id:** flag-007
- **type:** flag
- **bone:** 29, 112, 130, 137, 190, 200, 214, 216, 238, 287, 296, 297, 298, 403, 416, 502
- **what:** Fauna-relay and fauna-relay-adjacent bones with abstract-noun objects. The dispatch confirmed 6 abstract-relay beats were recast prior to this cycle; the surviving instances listed here are the remaining abstract-object relay beats. Catalog:
  - 29: `the wasps relay the south-wall return` — `the south-wall return` is a directional-pattern abstraction
  - 112: `the beetles relay the sound` — maximally abstract object
  - 130: `the beetles relay the south-wall footfall` — sound-event abstraction
  - 137: `the flies relay the Watch position` — state-of-position abstraction
  - 190: `the wasps relay the Fish Gate margin traffic` — flow-aggregate abstraction
  - 200: `the flies relay the weather-pattern data` — data/information abstraction (most abstract in the file)
  - 214: `the flies relay the junction return` — directional-pattern abstraction
  - 216: `the beetles relay the south-wall return` — directional-pattern abstraction (duplicate pattern of 29)
  - 238: `the flies relay the alley event` — event-as-noun abstraction
  - 287: `the beetles relay the register` — ambiguous (voice register = abstract; document register = concrete)
  - 296: `the beetles relay the rhythm` — sound-pattern abstraction
  - 297: `the beetles relay the phrase` — linguistic-unit abstraction
  - 298: `the beetles relay the rhythm` — sound-pattern abstraction (duplicate of 296)
  - 403: `the beetles relay the footfall` — sound-event abstraction
  - 416: `the beetles relay the pen-scratch` — sound-event abstraction
  - 502: `the wasps relay the pass` — action-as-noun abstraction
- **why:** Per schema: "Abstraction-as-object is INTERIORITY. A physical verb whose object is an abstract noun faults FAULT-FORM-INTERIORITY." The `relay` verb with abstract objects places interiority (sensory information, directional patterns, sound events) into the bone layer as if they were physical objects being acted upon. This pattern was partially addressed pre-cycle-1 (6 beats recast) but 16 instances remain. The cycle-1 auditor did not flag these, likely treating fauna-relay as a design convention. Raising now as a flag rather than fault because (a) cycle-1 passed them, (b) the fauna-relay design is systemic and flagging all as faults would require a design-level ruling, not single-bone fixes. However, the abstract-object rule is unambiguous in the schema. Escalation to fault classification requires showrunner ruling on fauna-relay design intent.
- **criteria:** N/A (flag — requires design ruling). Showrunner to rule: (a) fauna-relay with abstract objects is a licensed exception to FAULT-FORM-INTERIORITY (document in file header or in a design note), or (b) all abstract-relay objects must be recast to physical referents (e.g., `the beetles relay the footfall` → `the beetles relay the floor vibration`; `the flies relay the Watch position` → `the flies relay the Watch patrol`). Bone 200 (`the weather-pattern data`) is the most abstract and is the strongest candidate for mandatory recast regardless of the design ruling, as `data` is a meta-information noun with no physical analog.
- **scope:** season-scope — 16 bones. If escalated to fault, all route to fixer. If design exception documented, close this flag.
- **route:** showrunner for design ruling; then fixer (if fault) or close (if exception documented).

---

## Idiom-depletion summary (URI-007)

| idiom | count | threshold | status |
|---|---|---|---|
| `holds the feet` | 6 | 10 | below — no flag |
| `holds the eyes` | 5 | 10 | below — no flag |
| `holds the chin` | 1 | 10 | below — no flag |
| `stills` (intransitive) | 7 | 10 | below — monitoring (flag-005) |
| `exhales` (intransitive) | 9 | 10 | WARNING — at 9, one addition triggers depletion flag |

`exhales` count: bones 2, 31, 213, 218, 221, 225, 253, 273, 354, 433, 448 — wait, re-count against file:

Bones with `exhales`: 2, 31, 213, 218, 221, 225, 253, 273, 354 (line 422 `354 taylor-hebert-flea-bottom exhales`), 433, 448, 516. Let me recount from the file:

- 2: `taylor-hebert-flea-bottom exhales`
- 31: `taylor-hebert-flea-bottom exhales`
- 213: `taylor-hebert-flea-bottom exhales`
- 218: `taylor-hebert-flea-bottom exhales`
- 221: `taylor-hebert-flea-bottom exhales`
- 225: `taylor-hebert-flea-bottom exhales`
- 253: `taylor-hebert-flea-bottom exhales`
- 273: `taylor-hebert-flea-bottom exhales`
- 354: `taylor-hebert-flea-bottom exhales`
- 433: `taylor-hebert-flea-bottom exhales`
- 448: `taylor-hebert-flea-bottom exhales`
- 516: `taylor-hebert-flea-bottom exhales` (new bone, cycle-2)

Total: 12 instances. `exhales` has exceeded the 10-instance depletion threshold. URI-007 depletion flag triggered.

**Correction to table above — `exhales` depletion fault below.**

---

### fault-004

- **id:** fault-004
- **type:** fault
- **bone:** 2, 31, 213, 218, 221, 225, 253, 273, 354, 433, 448, 516 (pattern-level)
- **line (representative):** `taylor-hebert-flea-bottom exhales`
- **what:** `exhales` appears 12 times across the season bones (bones 2, 31, 213, 218, 221, 225, 253, 273, 354, 433, 448, 516). The URI-007 idiom-depletion check triggers at ≥10 instances of a physical-stasis idiom. `exhales` is the reset/pause breath marker used throughout the file — it encodes the narrator's emotional-pause beat. At 12 instances it has crossed the depletion threshold. Notably, bone 516 is a new bone added in this cycle; prior to cycle-2's additions the count stood at 11 (already over threshold). The cycle-1 auditor did not count `exhales` in the idiom-depletion table (it was not listed among the three checked idioms). This is a new finding.
- **why:** At 12 instances, `exhales` as a single physical-stasis idiom exceeds the depletion threshold and will produce prose repetition at the stitching layer. Every emotional pause, reset, and held-breath moment in the season is encoded by the same verb-only bone. The stitcher has no variation signal.
- **fault-class:** FAULT-IDIOM-DEPLETION (URI-007)
- **criteria:** Minimum 3 of the 12 `exhales` instances must be recast to alternative physical-pause verbs or expanded to transitive actions that encode the same beat more specifically. Options: `taylor-hebert-flea-bottom lowers the shoulders`, `taylor-hebert-flea-bottom drops the chin`, `taylor-hebert-flea-bottom releases the breath` (if breath as object is licensed — treat as concrete body-part process), `taylor-hebert-flea-bottom straightens the spine` (already used in bone 3, so check for redundancy), `taylor-hebert-flea-bottom turns the face` (if orientation change is intended). Selection of which 3 instances to recast is screen-writer's; prefer the mid-season cluster (bones 213–225) where four consecutive `exhales` appear within a short span.
- **scope:** season-scope — pattern across 12 bones; minimum 3 recasts required.
- **route:** fixer (coordinate with screen-writer for selection of instances to recast).

---

## Verdict

**RULESET-FAIL**

Two new faults (fault-002: bone 66 abstract object; fault-003: bone 19 unlicensed modifier; fault-004: `exhales` idiom depletion) trigger RULESET-FAIL. Cycle-1 fault-001 and flag-002 are confirmed resolved. All other cycle-1 flags carry forward. One new flag (flag-007: fauna-relay abstract objects) added; requires showrunner design ruling before fault/pass classification.

### Fault routing summary

| id | type | bone(s) | route | action required |
|---|---|---|---|---|
| fault-002 | fault | 66 | fixer | Recast `the reeve slows the step` — abstract object; replace with observable physical act or licensed intransitive |
| fault-003 | fault | 19 | fixer | Recast `oc-tanner-father steps toward the yard` — unlicensed directional prep phrase; use transitive location-as-object |
| fault-004 | fault | 2, 31, 213, 218, 221, 225, 253, 273, 354, 433, 448, 516 | fixer + screen-writer | `exhales` idiom depletion (12 instances, threshold 10); recast minimum 3 instances to alternative physical-pause verbs |
| flag-001 | flag | 318 | screen-writer | Confirm `sits` is discrete act; recast if stative |
| flag-003 | flag | 235 | screen-writer optional | Consider recasting `moves` to more specific transitive verb |
| flag-004 | flag | season-wide | screen-writer | `holds <body-part>` pattern density (12 licensed instances); diversify minimum 3 before Phase 4 split |
| flag-005 | flag | 14, 166, 170, 171, 496, 504, 517 | screen-writer | `stills` at 7 instances; no new `stills` bones without diversity review; depletion threshold 10 |
| flag-006 | flag | file-level | showrunner/screen-writer | Confirm aggregate format; add episode-section delimiters + narrator/goal headers or document flat-format exception |
| flag-007 | flag | 29, 112, 130, 137, 190, 200, 214, 216, 238, 287, 296, 297, 298, 403, 416, 502 | showrunner | Fauna-relay abstract objects: design ruling required (license exception or mandatory recast); bone 200 `weather-pattern data` is strongest candidate for mandatory recast regardless of ruling |
