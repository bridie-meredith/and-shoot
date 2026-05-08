audit:
  scope: season
  target: s01
  timestamp: 2026-05-07
  file_level: FAIL
  fault_counts:
    FAULT-FORM-MODIFIER: 8
    FAULT-FORM-NO-VERB: 1
  total_faults: 9
  total_flags: 10

---

# Season S01 — Pass S1 Constraint Re-Verify (post-fixer)

## File-level verdict: FAIL

9 confirmed faults remain after the S1 fixer pass. All 52 original faults are confirmed resolved or were false positives against prior file versions — the fixer log's accounting is correct for those. The remaining faults are **new introductions** from fixer repairs and structural rewrites (ch07-fault-002, season-S2 structural pass, ch07-pass3-batch), plus one instance carried forward from the original file that the S1 fixer pass did not reach.

No world-law, condition-card, or lore constraint violations found. No FAULT-POV, FAULT-FORM-INTERIORITY, FAULT-FORM-PERCEPTION, FAULT-FORM-MULTI-SUBJECT, FAULT-FORM-NON-ACTION-VERB, FAULT-FORM-CONJUNCTION, FAULT-CONSTRAINT-slug, or FAULT-FORM-ID-SEQUENCE violations remain.

---

## Drift patterns — post-fixer (appear 2+ times)

**Pattern F — `crosses to <destination>`:** The fixer introduced `crosses to` at chapter-07 line 5 while recasting a stative-posture fault. The same form (`crosses to the materials`, `the men-at-arms cross to the yard entrance`) survived from prior pass-2 repairs in chapter-01. Three instances across two files. The form was explicitly named as a fault class in the original S1 audit (fault-007 type) and in the schema example. The fixer inadvertently reintroduced the pattern while fixing a different fault.

**Pattern G — `toward <destination>` prepositional direction phrase:** `drives a raven toward the road` (ch03 line 45, added by season-S2 structural pass) and `bends over the ledger` (ch03-interlude line 18) are directional-prep constructions. The former is a clear instance of the banned pattern.

**Pattern H — bare intransitive pivot verbs:** `taylor-hebert-westeros turns` (ch01 line 123, ch02 line 67), `oc-plumms-man turns` (ch02 line 25, 78), `the sparrow turns` (ch02 line 26), `septon-rowan turns` (ch05 line 73), `ser-harwick-plumm turns` (ch05 line 33), `oc-castellan-harrenhal turns` (ch04 line 89), `the courier pivots` (ch06 line 88). These are bare intransitive orientation verbs without a destination or object. The prior S1 audit targeted `turns toward <X>` as FAULT-FORM-MODIFIER. Bare `turns` is ambiguous: the schema bans bare intransitive motion verbs without destination (the `taylor moves` prohibition) but also separately treats `turns to <X>` as the specific banned form. Bare `turns` / `pivots` without a named target is a weaker case than `turns toward <X>`. Classified as flags, not faults, pending a ruling on whether bare intransitive pivot verbs (with no destination and no directional phrase) are the same fault class. (If ruled faults, all ~8 instances would be FAULT-FORM-NO-VERB.)

---

## Findings

### CHAPTER 01 — chapter-01.md

- id: fault-001
  type: fault
  file: chapter-01.md
  line_id: 41
  content: "taylor-hebert-westeros crosses to the materials"
  fault_class: FAULT-FORM-MODIFIER
  what: "`crosses to` is a prepositional destination construction. The preposition `to` makes this identical to the banned `crosses to the window` (original S1 fault-007). The fixer's pass2-fault-012 repair stripped the modifier `writing` from the object but left `crosses to` intact, preserving the FAULT-FORM-MODIFIER fault class."
  why: "Downstream loc-state and state-update facets citing this line will read `crosses to the materials` as the action; the prepositional phrase is not a direct object the stitcher can treat as a destination. Same consequence as original fault-007."
  criteria: "Line must use a transitive verb that takes the destination as direct object without a preposition. `taylor-hebert-westeros crosses the cottage` (with position in loc-state) or `taylor-hebert-westeros reaches the materials` are both clean forms."

- id: fault-002
  type: fault
  file: chapter-01.md
  line_id: 56
  content: "the men-at-arms cross to the yard entrance"
  fault_class: FAULT-FORM-MODIFIER
  what: "`cross to` — same prepositional destination construction as fault-001. This line was introduced by pass2-fault-011 (fixer stripped the numeral and `beside` modifier from `two men-at-arms take position beside the official` → `the men-at-arms follow census-officer`) but the current file shows `the men-at-arms cross to the yard entrance`. The fixer log entry pass2-fault-011 shows the result as `the men-at-arms follow census-officer` but the current file reads differently — indicating a subsequent edit introduced this line. Either the fixer log is incomplete or a structural pass overwrote it. Regardless, the current line faults."
  why: "Same consequence as fault-001. The prepositional phrase is not elided by the schema's transitive model."
  criteria: "Line must use a transitive verb taking the destination as direct object. `the men-at-arms enter the yard entrance` or `the men-at-arms cross the yard` (with loc-state for position at the entrance)."

### CHAPTER 02 — chapter-02.md

- id: fault-003
  type: fault
  file: chapter-02.md
  line_id: 68
  content: "taylor-hebert-westeros walks the sept road"
  fault_class: FAULT-FORM-MODIFIER
  what: "`walks` is an intransitive motion verb. `walks the sept road` forces it transitive with a road as object, suppressing the preposition `along` or `on`. This is the same forced-transitive fault class as original fault-009 (`crouches the kitchen garden`). The road is not a physical thing the subject acts upon — it is the surface traversed. Additionally, `sept road` is a modified noun (the modifier `sept` qualifying `road`)."
  why: "Facets citing this line will misread `walks the sept road` as an action where the road is the direct object, not the surface. Same downstream confusion as fault-009. Also, the `sept` modifier on `road` is an adjectival qualifier violating the no-modifier rule."
  criteria: "Recast as a transitive verb that takes a landmark as direct object: `taylor-hebert-westeros takes the sept road` (road-taking idiom is physically interpretable) or split into `taylor-hebert-westeros crosses the field` + loc-state for the road, or `taylor-hebert-westeros enters the sept yard` if the destination is what matters."

### CHAPTER 03 — chapter-03.md

- id: fault-004
  type: fault
  file: chapter-03.md
  line_id: 45
  content: "taylor-hebert-westeros drives a raven toward the road"
  fault_class: FAULT-FORM-MODIFIER
  what: "`toward the road` is a prepositional phrase of direction/destination. The schema explicitly bans prepositional phrases of direction (same ruling that covers `turns toward <X>` and `walks into the yard`). This line was introduced by the season-S2 structural pass (svo-chapter-fix-log.md Revision 1) and was not present in the original S1 audit target."
  why: "The prepositional phrase encodes the direction of the fauna drive. Downstream loc-state and narrator-interest facets citing this line will treat `toward the road` as the destination — but it is not a direct object, it is a directional qualifier. The stitcher cannot elide it."
  criteria: "Line must name a concrete destination as direct object without a preposition, or drop the destination and let loc-state carry it. `taylor-hebert-westeros drives a raven` (intransitive fauna-drive, direction in loc-state) or `taylor-hebert-westeros drives a raven past the yard wall` if the specific physical motion is load-bearing."

### CHAPTER 03-INTERLUDE — chapter-03-interlude.md

- id: fault-005
  type: fault
  file: chapter-03-interlude.md
  line_id: 18
  content: "ser-harwick-plumm bends over the ledger"
  fault_class: FAULT-FORM-MODIFIER
  what: "`over the ledger` is a prepositional phrase of position. The schema explicitly bans prepositional phrases of position/place/destination. `bends over the ledger` means `bends [forward over] the ledger` — the preposition `over` locates the body relative to the object. The ledger is not the direct object of `bends`."
  why: "Downstream sensory and state-update facets will cite this line expecting a clean SVO where `the ledger` is the direct object of `bends`. It is not — it is a prepositional object. The physical act is observable but the encoding is not schema-compliant."
  criteria: "Recast as a transitive verb that takes the ledger as direct object without a preposition: `ser-harwick-plumm leans the head over the ledger` still has the prep phrase. Cleanest form: `ser-harwick-plumm leans` (intransitive, loc-state for the ledger proximity) or `ser-harwick-plumm reads the entry` — but `reads` is a perception verb (banned). Preferred: `ser-harwick-plumm drops the head` (head drops toward the page, physical body-part action) or split: separate body-posture beat from the examination beat."

- id: fault-006
  type: fault
  file: chapter-03-interlude.md
  line_id: 31
  content: "oc-plumms-man walks the road"
  fault_class: FAULT-FORM-MODIFIER
  what: "Same forced-transitive fault as fault-003 (`walks the sept road` in ch02). `walks` is intransitive; `walks the road` suppresses `along the road`. The road is a surface traversed, not a physical object the subject acts upon."
  why: "Same downstream consequence as fault-003. Object-misreading by facet authors and the stitcher."
  criteria: "Recast as an arrival or traversal beat with a transitive motion verb: `oc-plumms-man takes the road` or `oc-plumms-man exits the postern gate` (if the chapter's final beat is departure rather than road-walking, the prior line already provides the exit)."

### CHAPTER 07 — chapter-07.md

- id: fault-007
  type: fault
  file: chapter-07.md
  line_id: 5
  content: "septon-rowan crosses to the counter"
  fault_class: FAULT-FORM-MODIFIER
  what: "`crosses to` — prepositional destination construction. Introduced by fixer ch07-fault-002, which changed `septon-rowan stands at the counter` (stative) → `septon-rowan crosses to the counter` (arrival). The fix resolved the stative fault but introduced FAULT-FORM-MODIFIER. Same fault class as the original S1 fault-007 (`crosses to the window`) and current fault-001 and fault-002."
  why: "The fixer replaced one fault with a different fault. `crosses to the counter` reads identically to the banned `crosses to the window` form. Downstream facet authoring will treat `crosses to the counter` as the physical action, with `to the counter` as prepositional padding that cannot be elided."
  criteria: "Line must use a transitive verb taking the destination as direct object without a preposition. `septon-rowan crosses the floor` (loc-state positions him at the counter) or `septon-rowan reaches the counter`."

- id: fault-008
  type: fault
  file: chapter-07.md
  line_id: 75
  content: "taylor-hebert-westeros crosses the sept door"
  fault_class: FAULT-FORM-MODIFIER
  what: "`the sept door` is a door, not a traversal surface or threshold. `crosses` works transitively when the direct object is a space, floor, yard, or threshold (a traversal zone). A door is an aperture/barrier, not a traversable surface. `crosses the sept door` implies crossing the barrier itself rather than crossing through the doorway — the encoding is forced. Additionally, `sept` is a modifier on `door` (adjectival qualifier)."
  why: "Facets citing this line will read `the sept door` as the direct object of `crosses`, producing ambiguity: did Taylor physically cross (traverse) the door object, or exit through the door? The modifier `sept` adds a qualifier violating the no-modifier rule. The physical event (exiting the sept) is better encoded with a transitive exit verb."
  criteria: "Recast as a transitive exit verb: `taylor-hebert-westeros exits the sept` (if this precedes crossing the outer ward at line 94) or `taylor-hebert-westeros grips the sept doorframe` is already at line 92 and this line should encode a distinct physical beat. The most likely intent is exiting: `taylor-hebert-westeros exits the sept`."

### CHAPTER 10 — chapter-10.md

- id: fault-009
  type: fault
  file: chapter-10.md
  line_id: 19
  content: "oc-castellan-harrenhal returns to the table"
  fault_class: FAULT-FORM-MODIFIER
  what: "`returns to the table` is a prepositional destination construction. The preposition `to` makes `the table` a prepositional object, not a direct object. This is the same fault class as `crosses to the window` (original S1 fault-007). The prior S1 audit identified chapter-10 as clean (zero faults); this line was present in the file at that time, indicating the original auditor missed it, or the file has been modified since."
  why: "Same downstream consequence as fault-001 through fault-002. `to the table` is prepositional padding the stitcher cannot elide. Downstream loc-state facets will have to carry the table-position context that should be in the proto-line itself via transitive verb."
  criteria: "Recast as a transitive motion verb taking the table as direct object: `oc-castellan-harrenhal crosses to the table` — but this is the same fault! Correct form: `oc-castellan-harrenhal reaches the table` or `oc-castellan-harrenhal takes the table` (if `takes` = occupies position at) or split into `oc-castellan-harrenhal crosses the hall` + loc-state for table position."

---

## Flags (advisory, do not block)

- id: flag-001
  type: flag
  file: chapter-01.md lines 112, 123; chapter-02.md lines 25, 26, 67, 78; chapter-04.md line 89; chapter-05.md lines 33, 73; chapter-06.md line 88
  what: "Bare intransitive pivot verbs without a destination or orientation target: `the riders turn` (ch01:112), `taylor-hebert-westeros turns` (ch01:123, ch02:67), `oc-plumms-man turns` (ch02:25, 78), `the sparrow turns` (ch02:26), `oc-castellan-harrenhal turns` (ch04:89), `ser-harwick-plumm turns` (ch05:33), `septon-rowan turns` (ch05:73), `the courier pivots` (ch06:88). These are bare intransitive orientation-change verbs."
  why: "The schema bans bare intransitive motion verbs without destination (`taylor moves` → FAULT-FORM-NO-VERB). Pivot verbs (`turns`, `pivots`) are orientation changes rather than translational motion, making them closer to `exhales` (licensed intransitive) than to `moves` (banned). However, the specific ruling targeting `turns to <X>` was motivated by the directional-prep pattern, not the bare form. If bare `turns` / `pivots` is ruled the same class as `taylor moves`, all ~10 instances above would fault FAULT-FORM-NO-VERB. Holding as flags pending ruling. If the next pass's rubric addresses these, fixer should apply a standard recast (orientation-target as direct object: `faces <X>`, `pivots toward <X>` if motion is required)."

- id: flag-002
  type: flag
  file: chapter-02.md lines 18, 37, 40; chapter-04.md line 53
  what: "Forced-transitive constructions for small-fauna and person-as-perch-surface: `a fly lands the garden wall` (ch02:18), `three ravens settle the apple tree` (ch02:37), `the ravens settle the branch` (ch02:40), `a raven perches taylor-hebert-westeros` (ch04:53)."
  why: "Prior S1 audit held these as flags (flag-002, flag-006) pending a ruling on whether forced-transitive is blanket-licensed for small-fauna movement verbs. No ruling has been issued. Still advisory. If ruled faults, all four instances would fault FAULT-FORM-MODIFIER (suppressed preposition on intransitive verb)."

- id: flag-003
  type: flag
  file: chapter-06.md line 23
  what: "`septon-rowan crosses` — bare intransitive without destination. `crosses` is a motion verb."
  why: "The schema's FAULT-FORM-NO-VERB prohibition covers `taylor moves` (bare intransitive motion). `crosses` is a stronger case than `turns` (bare pivot) because `crosses` implies traversal to a destination that is not named. If the schema ruling is that all bare motion verbs without destination fault, this is a clean FAULT-FORM-NO-VERB. Holding as a flag rather than fault because the prior audit noted `crosses` in other files as licensed only when it has a direct object — here it has none, which is the failure mode. Fixer should add a destination: `septon-rowan crosses the room` or `septon-rowan crosses to the table` (though the latter introduces FAULT-FORM-MODIFIER, so `crosses the room` is preferred)."

- id: flag-004
  type: flag
  file: chapter-06.md lines 24, 30, 48; chapter-08.md line 93
  what: "Possessive determiners on prop objects: `his stylus` (ch06:24, 30), `his cloak` (ch06:48), `the septon's ledger` (ch08:93). Prior S1 audit flag-005 held these as advisory pending a ruling on whether possessives are accepted as disambiguation mechanism vs. modifier-class violations."
  why: "No ruling has been issued. Still advisory. If ruled faults, approximately 15+ additional instances across the season would fault FAULT-FORM-MODIFIER (possessive as adjective modifier on object noun)."

- id: flag-005
  type: flag
  file: chapter-07-interlude.md line 46
  what: "`the recorder shows oc-castellan-harrenhal Plumm's entry` — `shows` is a perception-enabling verb. Prior S1 audit flag-004."
  why: "Still unresolved. If `shows` is ruled a perception verb, this line faults FAULT-FORM-PERCEPTION. Additionally, `Plumm's entry` carries a possessive (flag-004 class)."

- id: flag-006
  type: flag
  file: chapter-09.md lines 34, 35, 99
  what: "`taylor-hebert-westeros repositions the raven` (lines 34, 35, 99), `taylor-hebert-westeros repositions the sparrow` (line 35). `repositions` is a stative-result verb — it implies moving fauna to a new position (result-state) rather than the discrete action of directing or dispatching."
  why: "The original S1 audit faulted `stations` on exactly this logic (fault-043: 'asserts resulting positioned state'). `repositions` is in the same semantic class. The difference is that `repositions` implies a change-of-position (more action-like) vs. `stations` which implies initial placement. The distinction is narrow. If `repositions` is ruled the same fault class as `stations`, these three lines would fault FAULT-FORM-NON-ACTION-VERB. Holding as flags because the schema's `stations` ruling was based on the specific example; `repositions` is borderline. Fixer should be aware: if ruled faults, recast as `taylor-hebert-westeros redirects the raven` or `taylor-hebert-westeros moves the raven` (though `moves` is the explicitly cited FAULT-FORM-NO-VERB example). `shifts the raven` is likely the cleanest alternative."

- id: flag-007
  type: flag
  file: chapter-05.md line 26
  what: "`septon-rowan takes the Harrenhal road` — `takes the road` as a travel-initiation idiom. The road is the direct object of `takes`."
  why: "The forced-transitive pattern for roads and paths (suppressing `along the road`) is related to flag-002 (small-fauna) and fault-003 (`walks the sept road`). `takes the road` is more idiomatic than `walks the road` — `takes` in the sense of travel-initiation is physically interpretable (grasping a route). Less clearly a fault than fault-003. Advisory only."

- id: flag-008
  type: flag
  file: chapter-02.md line 23
  what: "`oc-plumms-man turns the head` — `turns` with body-part object (head rotation). Physical act."
  why: "Not a fault under the narrow holds license review — this is `turns` not `holds`. A head-turn is a discrete physical action. However, it uses the same head/body-part + verb construction. If the schema's no-modifier / body-part-object rules are interpreted strictly, `the head` as direct object of `turns` may warrant scrutiny. Holding as flag; current read is clean."

- id: flag-009
  type: flag
  file: chapter-08-interlude.md lines 48 and 49
  what: "Two consecutive identical lines: `oc-castellan-harrenhal speaks to the hall` at IDs 48 and 49."
  why: "Not a mechanic fault — duplicate dialogue beats at different IDs can serve different narrative moments. However, the back-to-back identical beat is unusual and may indicate a duplication artifact from the ch08-pass3-shape split. If a dialogue facet author assigns content to both, the duplication is structural. Advisory only."

- id: flag-010
  type: flag
  file: chapter-07.md line 75; chapter-01.md line 41
  what: "Minor cross-file note: the fixer-log for ch07-fault-004 shows `septon-rowan crosses to the sept door` was the pre-fix state. The current file shows `taylor-hebert-westeros crosses the sept door` at line 75 — a different actor and slightly different form. This line may be a net-new introduction from the ch07-pass3-batch re-order and is not traceable to a specific fixer-log entry."
  why: "If this line was not reviewed in any prior pass, it is unaudited. Flagging for continuity purposes."

---

## Slug resolution — post-fixer

| Slug | Status | Verdict |
|------|--------|---------|
| taylor-hebert-westeros | Series cast roster | RESOLVED |
| septon-dying-protector | Series cast roster | RESOLVED |
| septon-rowan | Series cast roster | RESOLVED |
| ser-harwick-plumm | Series cast roster | RESOLVED |
| oc-castellan-harrenhal | Series cast roster | RESOLVED |
| westerosi-traveling-maester | Series cast roster | RESOLVED |
| ser-aemon-bracken | Series cast roster | RESOLVED |
| ser-edwyn-celtigar | Series cast roster | RESOLVED |
| oc-census-officer | Escalated to showrunner; oc-prefix applied in file | ESCALATED (prior pass) |
| oc-plumms-man | Escalated to showrunner; oc-prefix applied in file | ESCALATED (prior pass) |
| the recorder | `the <noun>` form | RESOLVED |
| the woman | `the <noun>` form | RESOLVED |
| the records clerk | `the <noun>` form | RESOLVED |
| the gatehouse man | `the <noun>` form | RESOLVED |
| the third rider | `the <noun>` form | RESOLVED |
| the man-at-arms / the men-at-arms | `the <noun>` form | RESOLVED |
| the guard / the guardsman | `the <noun>` form | RESOLVED |
| the courier | `the <noun>` form | RESOLVED |

No new unregistered slugs found in any file.

---

## ID-sequence status — post-fixer

All files examined. No non-monotonic ID sequences found in any current file. The re-ordering done by ch07-pass3-batch (placing ID 93 before 17 in file-body, 94 before 29) is schema-valid per the fixer log's cited ruling: "ID order != numeric order; IDs are stable, stitcher walks citation order not numeric order." No FAULT-FORM-ID-SEQUENCE findings.

---

## Aggregate fault counts by class (post-fixer)

| Fault class | Count | Files affected |
|-------------|-------|----------------|
| FAULT-FORM-MODIFIER | 8 | ch-01(2), ch-02(1), ch-03(1), ch-03-interlude(2), ch-07(2), ch-10(1) |
| FAULT-FORM-NO-VERB | 1 | ch-07(1) — crossed the sept door |
| **Total faults** | **9** | |
| Flags (advisory) | 10 | Multiple |

*Note: fault-008 (ch07 line 75 `crosses the sept door`) is classified FAULT-FORM-MODIFIER (modifier `sept` on object noun) rather than FAULT-FORM-NO-VERB; the no-verb designation above is an error in the count header — corrected count is 0 FAULT-FORM-NO-VERB, 9 FAULT-FORM-MODIFIER total.*

Corrected aggregate:

| Fault class | Count | Files affected |
|-------------|-------|----------------|
| FAULT-FORM-MODIFIER | 9 | ch-01(2), ch-02(1), ch-03(1), ch-03-interlude(2), ch-07(2), ch-10(1) |
| **Total faults** | **9** | |
| Flags (advisory) | 10 | Multiple |

---

## Fixer routing

**High-priority (pattern recurrence — 3+ instances of same form):**
- `crosses to <destination>` pattern (fault-001, fault-002, fault-007): ch-01 lines 41, 56 and ch-07 line 5. Simple transitive recast: `reaches <destination>` or `crosses <space>`.

**Single-instance faults:**
- fault-003 (`walks the sept road` ch02:68): recast as `takes the sept road` or arrival verb.
- fault-004 (`drives a raven toward the road` ch03:45): strip directional phrase; `drives a raven` or name a concrete destination.
- fault-005 (`bends over the ledger` ch03-interlude:18): recast body-posture without prep phrase.
- fault-006 (`walks the road` ch03-interlude:31): same class as fault-003.
- fault-008 (`crosses the sept door` ch07:75): recast as `exits the sept`.
- fault-009 (`returns to the table` ch10:19): recast as `reaches the table` or `crosses the hall`.

**Flags — no action required unless ruling changes:**
- flag-001 (bare pivot verbs): fixer awareness only until ruling issued.
- flag-002 (fauna forced-transitive): same.
- flag-003 (`septon-rowan crosses` ch06:23): borderline FAULT-FORM-NO-VERB; recommend fixer add destination.
- flag-004 (possessives): no action until ruling.
- flag-005 (`shows` perception-enabling): no action until ruling.
- flag-006 (`repositions` stative-result): no action until ruling.
- flag-007 (`takes the Harrenhal road`): advisory.
- flag-008 (`turns the head`): advisory.
- flag-009 (duplicate speaks-to-the-hall): advisory.
- flag-010 (ch07:75 provenance gap): advisory.

**Escalations:** None. All faults are episode-scope mechanical faults resolvable by line recast. No slug-registration decisions outstanding beyond the two already escalated to showrunner in the prior pass.
