# Audit Report — Season s01 Pass S3.5 — Ruleset Compliance (Mechanic-Strictness)
# schema: schemas/audit-report.schema.md
# generated: 2026-05-11
# auditor-fork: Phase 3 Pass S3.5 cycle 2 re-fire (post-fixer)
# target: active-project/theater/proto-lines/s01.bones.md
# cycle: 2 re-fire (cycle-2 report archived prior to this overwrite)
# file-level verdict: RULESET-FAIL

---

## Scope

Full walk of all numbered non-blank lines in `active-project/theater/proto-lines/s01.bones.md` against:
- Cycle-2 fix verification (bones 66, 19; IDs 213/273/354 exhales recasts)
- URI-007 idiom-depletion re-check: `exhales` (post-recast count), `stills`, `holds <body-part>`
- New violations introduced by cycle-2 fixes
- All standing flags and faults from cycle-2

---

## Cycle-2 fix verification

| cycle-2 id | bone | claimed fix | file state | verdict |
|---|---|---|---|---|
| fault-002 | 66 | `the reeve slows` (abstract object `the step` removed) | Line reads `66 the reeve slows` | RESOLVED. Intransitive. Abstract object removed. flag-008 carries from cycle-2. |
| fault-003 | 19 | `oc-tanner-father enters the yard` (modifier dropped) | Line reads `19 oc-tanner-father enters the yard` | RESOLVED. Transitive SVO, location as direct object. Clean. |
| fault-004 (partial) | 213 | `rolls the shoulders` (was `exhales`) | Line reads `213 taylor-hebert-flea-bottom rolls the shoulders` | RESOLVED for this bone. |
| fault-004 (partial) | 273 | `flexes the hand` (was `exhales`) | Line reads `273 taylor-hebert-flea-bottom flexes the hand` | RESOLVED for this bone. |
| fault-004 (partial) | 354 | `drops the gaze` (was `exhales`) | Line reads `354 taylor-hebert-flea-bottom drops the gaze` | RESOLVED for this bone. |

---

## Idiom-depletion re-count (URI-007)

### `exhales` — full file count

Dispatch claims: "Total `exhales` count now 9 — below URI-007 threshold of 10."

File scan result:

| bone | actor | line |
|---|---|---|
| 2 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 31 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 218 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 221 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 225 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 253 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 323 | oc-tanner-mother | `oc-tanner-mother exhales` |
| 433 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 448 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |
| 516 | taylor-hebert-flea-bottom | `taylor-hebert-flea-bottom exhales` |

**Actual count: 10 instances.** The dispatch claim of 9 is incorrect. Bone 323 (`oc-tanner-mother exhales`) was not in the cycle-2 report's `exhales` inventory — the cycle-2 auditor's count covered only taylor-hebert-flea-bottom instances plus bone 516 and missed bone 323. Bone 323 is present in the file and contains the verb `exhales`; it counts toward URI-007 idiom-depletion totals regardless of subject.

URI-007 threshold is 10. At exactly 10 instances, the threshold is met. The depletion flag triggers at ≥10 per the rule as stated. fault-004 is NOT resolved — it is reduced from 12 to 10, but 10 meets the threshold exactly and the fault condition persists.

**fault-004 status: STANDING.** One additional recast is required to bring the count to 9 (below threshold).

### `stills` — full file count

| bone | actor |
|---|---|
| 14 | oc-tanner-father |
| 166 | oc-tanner-father |
| 170 | oc-tanner-father |
| 171 | oc-tanner-mother |
| 496 | taylor-hebert-flea-bottom |
| 504 | taylor-hebert-flea-bottom |
| 517 | taylor-hebert-flea-bottom |

**Count: 7 instances.** Matches cycle-2 report. Unchanged. Below 10-instance threshold. flag-005 carries forward.

### `holds <body-part>` — full file count

| bone | idiom |
|---|---|
| 13 | `holds the chin` |
| 42 | `holds the eyes` |
| 89 | `holds the feet` |
| 142 | `holds the feet` |
| 227 | `holds the eyes` |
| 275 | `holds the eyes` |
| 288 | `holds the feet` |
| 356 | `holds the eyes` |
| 450 | `holds the eyes` |
| 463 | `holds the feet` |
| 472 | `holds the feet` |
| 503 | `holds the feet` |

**Count: 12 instances.** Unchanged from cycle-2. Per-idiom breakdown: `holds the chin` ×1, `holds the eyes` ×5, `holds the feet` ×6. All per-idiom counts below the 10-instance threshold. flag-004 carries forward.

---

## New findings this cycle

None. No new violations introduced by the cycle-2 fixes. The five recasts (bones 66, 19, 213, 273, 354) are all clean per ruleset.

---

## Standing findings — all cycles

### fault-004 (cycle-2, STANDING — not resolved)

- **id:** fault-004
- **type:** fault
- **bone:** 2, 31, 218, 221, 225, 253, 323, 433, 448, 516 (10 remaining instances)
- **what:** `exhales` appears 10 times in the file after cycle-2 recasts (bones 213, 273, 354 resolved). URI-007 triggers at ≥10 instances. The dispatch claimed the count reached 9 but bone 323 (`oc-tanner-mother exhales`) was not counted in the prior cycle's inventory, bringing the actual total to 10. Threshold is met; fault persists.
- **why:** At 10 instances, URI-007 depletion is triggered. The stitcher has no variation signal for the pause/reset breath beat.
- **fault-class:** FAULT-IDIOM-DEPLETION (URI-007)
- **criteria:** One additional `exhales` instance must be recast to an alternative physical-pause verb or transitive action encoding the same beat. After the recast, the total must stand at 9 or fewer. Bone 323 (`oc-tanner-mother exhales`) is the lowest-disruption candidate: it is the sole non-taylor-hebert instance and naturally distinct in context. Alternatively any single instance from the mid-season cluster (218, 221, 225) may be recast, as those three appear in close proximity.
- **scope:** season-scope — minimum 1 additional recast required.
- **route:** fixer.

---

### flag-001 (carried from cycles 1–2)

- **id:** flag-001
- **type:** flag
- **bone:** 318
- **line:** `oc-tanner-mother sits`
- **what:** Intransitive `sits` — ambiguous between discrete act (licensed) and stative position descriptor (deny-list). No screen-writer confirmation received through two cycles.
- **why:** If stative, non-action verb contaminates the bone layer.
- **criteria:** N/A (flag). Screen-writer must confirm intent.
- **scope:** episode — single bone.
- **route:** screen-writer for intent confirmation; fixer if stative confirmed.

---

### flag-003 (carried from cycles 1–2)

- **id:** flag-003
- **type:** flag
- **bone:** 235
- **line:** `the lords-man's man moves the family possessions`
- **what:** Generic transitive `moves` with collective-noun object. Not a fault. Under-specified physical act.
- **why:** Stitcher has no specific manner encoded.
- **criteria:** N/A (screen-writer optional).
- **scope:** episode — single bone.
- **route:** screen-writer optional.

---

### flag-004 (carried from cycles 1–2)

- **id:** flag-004
- **type:** flag
- **bone:** season aggregate
- **what:** `holds <body-part>` — 12 licensed instances. `holds the chin` ×1, `holds the eyes` ×5, `holds the feet` ×6. Count unchanged across all cycles. 25% recast recommendation from cycle-1 not actioned.
- **why:** Idiom density; prose repetition at stitching layer.
- **criteria:** N/A (flag). Screen-writer: diversify minimum 3 of 12 before Phase 4 split.
- **scope:** season-scope.
- **route:** screen-writer.

---

### flag-005 (carried from cycles 1–2)

- **id:** flag-005
- **type:** flag
- **bone:** 14, 166, 170, 171, 496, 504, 517
- **what:** `stills` — 7 instances. Count matches cycle-2. Unchanged.
- **why:** Sustained growth across cycles. If Phase 4 additions push to 10, depletion flag auto-triggers.
- **criteria:** N/A (flag). No new `stills` bones without diversity review.
- **scope:** season-scope.
- **route:** screen-writer monitoring.

---

### flag-006 (carried from cycles 1–2)

- **id:** flag-006
- **type:** flag
- **bone:** N/A (file-level structure)
- **what:** `s01.bones.md` still contains no episode-section delimiters (`# === episode: <slug> ===`) and no per-section `narrator:` / `goal:` headers. No resolution across two cycles.
- **why:** Schema aggregate format not satisfied. Pass 5 narrator-consistency and Phase 4 Step 3.2 extended-header generation depend on resolvable per-episode headers.
- **criteria:** N/A (flag). Confirm format intent and add delimiters or document flat-format exception.
- **scope:** season-scope.
- **route:** showrunner or screen-writer.

---

### flag-007 (new in cycle-2, carried)

- **id:** flag-007
- **type:** flag
- **bone:** 29, 112, 130, 137, 190, 200, 214, 216, 238, 287, 296, 297, 298, 403, 416, 502
- **what:** Fauna-relay bones with abstract-noun objects. 16 instances. Showrunner design ruling not yet recorded. Bone 200 currently reads `the flies relay the wind` — more concrete than `the weather-pattern data` cited in the cycle-2 report. Whether this bone was recast between cycles or the cycle-2 report mis-cited its content is unresolved.
- **why:** Schema FAULT-FORM-INTERIORITY applies to abstract objects per strict reading. Fauna-relay design may constitute a licensed exception, but no exception is documented.
- **criteria:** N/A (flag — requires design ruling). Showrunner to rule: license exception (document) or mandatory recast. Separately confirm whether bone 200 was modified between cycles.
- **scope:** season-scope.
- **route:** showrunner for design ruling.

---

### flag-008 (new in cycle-2, carried)

- **id:** flag-008
- **type:** flag
- **bone:** 66
- **line:** `the reeve slows`
- **what:** `slows` (intransitive) encodes a kinematic process — gradual deceleration — rather than a single discrete physical act. It is not on any deny-list. The fault-002 criteria are satisfied (abstract object removed). `slows` sits at the boundary between a licensed discrete-onset verb and a process descriptor: `stills` = onset of stillness (discrete point); `slows` = ongoing deceleration (more state-like). Not a fault.
- **why:** Borderline process verb. Stitcher may render as ongoing state rather than event onset. Low risk.
- **criteria:** N/A (flag). Screen-writer may confirm or recast to `stills` / `stops` if the beat is a complete pause.
- **scope:** episode — single bone.
- **route:** screen-writer optional.

---

## Checks confirmed clean (post-fix re-verification)

| Check | Result |
|---|---|
| Copulas | CLEAN |
| Negations | CLEAN |
| Perception verbs | CLEAN |
| Conjunctions | CLEAN |
| Multi-subject lines | CLEAN |
| Dialogue form | CLEAN |
| Deny-list: possession, sustained-carrying, containment, `lies`, `stands` | CLEAN |
| `holds` narrow license | CLEAN — 12 instances, all body-part objects, 0 unlicensed |
| Bone 19 post-fix | CLEAN — `enters the yard` is licensed transitive SVO |
| Bones 213/273/354 post-recast | CLEAN — `rolls the shoulders`, `flexes the hand`, `drops the gaze` are licensed transitive SVO |
| Bone 66 post-fix | CLEAN (fault resolved; flag-008 borderline raised) |

---

## Verdict

**RULESET-FAIL**

fault-004 (`exhales` idiom depletion) is not resolved. The cycle-2 fixer recast 3 of 12 instances (213, 273, 354), reducing the count from 12 to 10. The dispatch claimed 9, but bone 323 (`oc-tanner-mother exhales`) was omitted from the prior cycle's inventory and brings the actual count to 10, which meets the URI-007 ≥10 trigger exactly. One additional recast is required.

fault-002 and fault-003 are confirmed resolved. No new faults introduced by the cycle-2 fixes.

### Fault routing summary

| id | type | bone(s) | route | action required |
|---|---|---|---|---|
| fault-004 | fault | 2, 31, 218, 221, 225, 253, 323, 433, 448, 516 | fixer | `exhales` at 10 instances — one additional recast required to bring total to ≤9; bone 323 is lowest-disruption candidate |
| flag-001 | flag | 318 | screen-writer | Confirm `sits` is discrete act |
| flag-003 | flag | 235 | screen-writer optional | Consider recasting `moves` |
| flag-004 | flag | season-wide | screen-writer | `holds <body-part>` density (12 instances); diversify minimum 3 |
| flag-005 | flag | 14, 166, 170, 171, 496, 504, 517 | screen-writer | `stills` at 7; no new instances without diversity review |
| flag-006 | flag | file-level | showrunner/screen-writer | Add episode-section delimiters or document flat-format exception |
| flag-007 | flag | 29, 112, 130, 137, 190, 200, 214, 216, 238, 287, 296, 297, 298, 403, 416, 502 | showrunner | Fauna-relay abstract objects: design ruling required; verify bone 200 content against cycle-2 report description |
| flag-008 | flag | 66 | screen-writer optional | `slows` borderline process verb; confirm or recast to `stills`/`stops` if beat is a complete pause |
