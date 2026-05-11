```yaml
audit:
  scope: season
  target: s01
  pass: 2-reaudit (convergence verification)
  timestamp: 2026-05-09
  verdict: FAIL
  verdict_summary: >
    3 recast regressions introduced by the fixer; 1 confirmed pre-existing unaudited fault (ID 192,
    flagged by fixer); 16 pre-existing faults missed by the original audit and untouched by the fixer;
    2 faults partially resolved but with a modifier residue in the split lines.
    All findings are line-scope. No constraint-coherence new faults. No POV-structure faults.
    No escalations. File does not converge; re-route to fixer for a targeted second pass.
```

---

# Season s01 Pass-2 Constraint Re-Audit (Convergence Verification)

**File:** `active-project/theater/proto-lines/s01.aggregate.md`
**Prior audit:** `active-project/staff/auditor/season-s01-pass-2-constraint.md`
**Fixer log:** `active-project/staff/fixer/season-s01-pass-2-fix-log.md`
**Schema:** `schemas/proto-line.schema.md`, `design/shoot-v2/svo-writer-pass1-brief.md`

---

## Verification checks (pass/fail summary before findings)

| Check axis | Result |
|---|---|
| All 42 fixer actions confirmed applied | PASS |
| All 39 deletions converted to blank time-skip markers | PASS |
| 20 recasts confirmed at correct IDs | PASS (with exceptions — see recast regressions below) |
| Split lines 914, 915 appended with split-from comments | PASS (with modifier fault on 915 — see below) |
| POV markers: 5 present, correctly slugged | PASS |
| No per-episode delimiters | PASS |
| Top-of-file comment header intact | PASS |
| Constraint-coherence (cost ceiling, suppression stage, behavior cards) | PASS — no new violations |
| ID drift anomalies (513/563, 716/736, 509/563) | CONFIRMED RESOLVED — gaps correctly blank |
| Pre-existing gaps 901–903, 913 | CONFIRMED — absent as pre-existing deletions |
| ID 192 unaudited fault | CONFIRMED PRESENT — fault-NUA-001 below |

---

## SECTION 1 — Recast Regressions (faults introduced by the fixer)

### fault-R001 — ID 124: `the swallow holds position`

**Type:** fault
**What:** The fixer recast `taylor-hebert-jaehaerys holds the swallow neutral` → `the swallow holds position`. The subject (`the swallow`) is now the fauna performing the hold. However, `position` is an abstract noun, not a body part of the swallow. Under the narrow holds license: (1) body-part-as-object under stillness-against-pressure — not met; (2) physical object resisting pressure — not met. `position` is an abstract quality, identical in structure to `holds the pace` (fault-004 in the original audit). The recast introduces a new FAULT-FORM-INTERIORITY / FAULT-FORM-NON-ACTION-VERB (unlicensed holds, abstract object).
**Why:** Downstream stitcher cannot render `holds position` as an observable physical event; it is a state assertion.
**Criteria:** The beat must express the swallow's physical behavior without `holds` applied to an abstract object. Clean forms: `the swallow grips the gutter edge`, `the swallow stills on the gutter`, or `the swallow holds the gutter rim` (if the rim is being physically gripped against resistance). The abstract noun `position` must not be the object.

---

### fault-R002 — IDs 194 and 264: `the fly holds the basin rim` / `the fly holds the pen rail edge`

**Type:** fault
**What:** The fixer recast `taylor-hebert-jaehaerys holds the fly` (both instances) as fauna-subject holds-on-physical-object. ID 194: `the fly holds the basin rim`; ID 264: `the fly holds the pen rail edge`. In both cases the subject is the fly, the object is an external physical surface (not the fly's body part). The narrow holds license does not extend to this pattern: `the fly holds the basin rim` means the fly is gripping the rim — a stative grip, not stillness-against-external-pressure applied to the object. The prior audit's fault-003 identified `[subject] holds the bench edge` as faulty precisely because the held object is an external surface and the hold is a stative grip rather than resistance-against-pressure. Both IDs fault identically for the same reason.
**Why:** Same downstream failure as fault-003 in the original audit. The physical event is the fly perching or landing, not a holds-under-pressure act.
**Criteria:** Recast as the fly's discrete observable physical behavior. Clean forms: `the fly lands on the basin rim`, `the fly grips the pen rail edge` (if `grips` passes — note: `grips` is also borderline stative; prefer `the fly lands`, `the fly clings`, or similar action-event forms). Both IDs must be revised.

---

### fault-R003 — ID 914: `a second mounted man rides`

**Type:** fault
**What:** The split-appended bone at ID 914 (split-from: 334) reads `a second mounted man rides`. `rides` is a bare intransitive motion verb without destination. Under the schema: "Bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB." `a second mounted man rides` states that a person is in the act of riding, but names no destination, no route, and no object — it is a state description (being-in-a-riding-state), not a discrete observable physical event with direction.
**Why:** The stitcher cannot render `rides` as a positioned physical act. The bone is content-free beyond confirming the mounted man is mounted.
**Criteria:** The bone must express a discrete observable physical act: `a second mounted man follows the column`, `a second mounted man reins behind oc-lords-steward`, or an equivalent transitive/directional form that names what the actor does.

---

### fault-R004 — ID 915: `the second collector's man rights the table`

**Type:** fault
**What:** The split-appended bone at ID 915 (split-from: 511) carries `second` as an ordinal modifier on `collector's man`. The schema explicitly bans all adjectives and adverbs: "No modifiers — no adjectives, no adverbs, no prepositional padding." `second` is an ordinal adjective. The parallel bone at ID 511 uses `the first collector's man`, which carries the same fault. Both ordinal modifiers are FAULT-FORM-MODIFIER.
**Why:** Modifier on the subject slug violates schema discipline. If the two collector's men need to be distinguished, they must be differentiated by role slug or by context — not by ordinal adjective.
**Criteria:** The bone must not carry the ordinal modifier. Either (a) introduce a distinguishing role slug (`the lead collector's man`, `the standing collector's man`) or (b) the action sufficiently identifies the actor without the ordinal, and the ordinal is dropped. Note: ID 511 carries the same fault (`the first collector's man`) and must be corrected simultaneously — otherwise the split pair is asymmetric and both are non-compliant.

*Note on ID 511 ordinal: The prior audit's fault-033 criteria said "split into `the first collector's man rights the table` and a second proto-line." The fixer followed that prescription literally, but the criteria language `first` was descriptive shorthand in the auditor's criteria field, not a license for ordinal adjectives in the bone. The bone itself must not carry `first` or `second`.*

---

## SECTION 2 — Unaudited Fault (flagged by fixer, confirmed present)

### fault-NUA-001 — ID 192: `taylor-hebert-jaehaerys holds the pace`

**Type:** fault
**What:** ID 192 carries `taylor-hebert-jaehaerys holds the pace`. `pace` is an abstract quality, not a physical object. This is identical in structure and fault class to fault-004 in the original audit (`holds the pace` at IDs 258, 301, 560, 650, 820, 828 — all deleted by the fixer). ID 192 was not listed in the original audit's fault-004 ID set and was therefore not actioned. The fixer correctly flagged it and left it untouched per scope rules. It is now the only surviving `holds the pace` instance in the file.
**Why:** `holds the pace` is interiority expressed as a physical verb. Not observable by a witness. Identical downstream failure to the six instances the fixer deleted.
**Criteria:** Delete or replace with the observable physical action that constitutes the beat (e.g., the physical behavior that constitutes Taylor maintaining pace — if she does not accelerate, the proto-line should record what she does instead of what she does not do).

---

## SECTION 3 — Pre-existing Faults Missed by Original Audit

All items in this section were present before the fixer pass, were not in the original audit's finding set, and were not touched by the fixer. They are confirmed still present in the post-fix file.

---

### fault-MIS-001 — ID 25: `taylor-hebert-jaehaerys traces the column with one finger`

**Type:** fault
**What:** `with one finger` is a prepositional phrase of instrument. FAULT-FORM-MODIFIER. The clean form is `taylor-hebert-jaehaerys traces the column`. The instrument prepositional phrase is padding per the schema's explicit list of banned prepositional forms.
**Why:** Modifier pollutes the bone; downstream stitcher may fix the detail into prose, generating tonal inconsistency.
**Criteria:** Line must read `taylor-hebert-jaehaerys traces the column` with no trailing prepositional phrase.

---

### fault-MIS-002 — ID 94: `taylor-hebert-jaehaerys continues the wipe`

**Type:** fault
**What:** `continues` applied to `the wipe` (an action-noun). `continues` is a stative persistence verb — it describes an ongoing state, not a discrete physical act. `the wipe` as object is an abstraction (a nominalized action). FAULT-FORM-NON-ACTION-VERB. The physical act is `taylor-hebert-jaehaerys wipes the vat rim` (already at ID 92).
**Why:** A persistence verb is not a proto-line-level event; it describes state continuation, not a new physical occurrence.
**Criteria:** Delete or replace with the discrete physical act that constitutes the continued wiping (e.g., a second pass: `taylor-hebert-jaehaerys wipes the vat rim` if a second distinct physical stroke is intended; otherwise delete as redundant given ID 92).

---

### fault-MIS-003 — ID 97: `oc-craftsman-mother pulls taylor-hebert-jaehaerys's hair back from the vat rim`

**Type:** fault
**What:** `back from the vat rim` is a prepositional phrase of direction and source appended after the object. FAULT-FORM-MODIFIER. The clean form is `oc-craftsman-mother pulls taylor-hebert-jaehaerys's hair`.
**Why:** Prepositional padding.
**Criteria:** Line must terminate at the direct object. Strip `back from the vat rim`.

---

### fault-MIS-004 — IDs 103 and 659: `[subject] sets the satchel on the table`

**Type:** fault
**What:** ID 103: `oc-craftsman-father sets the satchel on the table`. ID 659: `oc-craftsman-father sets the satchel on the table`. In both, `on the table` is a prepositional phrase of location. FAULT-FORM-MODIFIER.
**Why:** Prepositional padding. Both instances identical.
**Criteria:** Both lines must read `oc-craftsman-father sets the satchel` with no trailing prepositional phrase.

---

### fault-MIS-005 — ID 121: `taylor-hebert-jaehaerys lifts the cloth from the basket`

**Type:** fault
**What:** `from the basket` is a prepositional phrase of source. FAULT-FORM-MODIFIER.
**Why:** Prepositional padding.
**Criteria:** Line must read `taylor-hebert-jaehaerys lifts the cloth`.

---

### fault-MIS-006 — ID 145: `oc-craftsman-mother returns with the candle`

**Type:** fault
**What:** `with the candle` is a prepositional phrase of accompaniment. FAULT-FORM-MODIFIER. The schema explicitly bans prepositional phrases of accompaniment. The clean form is `oc-craftsman-mother returns` (if the candle-carrying state lives in a state-update facet) or `oc-craftsman-mother carries the candle` is banned (sustained carrying verb) — so the correct approach is to split: `oc-craftsman-mother returns` and a separate bone for taking/drawing the candle (ID 144 already covers the draw; ID 145 should be the motion only).
**Why:** Prepositional accompaniment phrase is padding.
**Criteria:** Line must not carry `with the candle`. If the arrival and the candle are both necessary as a single beat, recast as `oc-craftsman-mother sets the candle` at the destination, with motion implied by prior beats.

---

### fault-MIS-007 — ID 153: `the sept vaulted space rises above the entry`

**Type:** fault
**What:** `vaulted` is an adjective modifier on `space`. `above the entry` is a prepositional phrase of location. Dual FAULT-FORM-MODIFIER. Additionally, `the sept vaulted space rises above the entry` is an environment-state description (the architectural fact of the vaulted ceiling) — a location-state facet assertion, not a discrete physical event.
**Why:** Adjective modifier plus prepositional modifier plus environment-state pattern.
**Criteria:** Delete and route the architectural description to a loc-state facet, or recast as a discrete physical event by a named actor (e.g., `taylor-hebert-jaehaerys lifts the gaze` to imply looking up into the vault, with the vault's properties handled by loc-state).

---

### fault-MIS-008 — ID 154: `four books fill the lectern shelf`

**Type:** fault
**What:** `four` is an ordinal/quantifier adjective on `books`. FAULT-FORM-MODIFIER. Additionally, `fill the lectern shelf` is a stative containment/placement description (the books occupy the shelf — an environment-state, not a discrete act performed by the books). FAULT-FORM-NON-ACTION-VERB (stative containment).
**Why:** Adjective modifier plus stative environment-state description.
**Criteria:** Delete and route the shelf contents to a loc-state facet, or recast with a named actor placing books (if the stacking is part of the narrative beat).

---

### fault-MIS-009 — ID 329: `the river-ferry dock fills`

**Type:** fault
**What:** `the river-ferry dock fills` is an environment-state description (the dock accumulating people/activity). Subject `the river-ferry dock` performs no discrete physical act. FAULT-FORM-NON-ACTION-VERB. Identical structure to the original audit's fault-013 (IDs 300, 556: `the square fills`). The original audit caught the square-fills pattern but missed this dock-fills instance.
**Why:** Environment-state belongs in loc-state facets.
**Criteria:** Delete; route dock crowd density to a loc-state facet citing adjacent actor proto-lines.

---

### fault-MIS-010 — ID 333: `the institutional retinue rounds the river bend`

**Type:** fault
**What:** `institutional` is an adjective modifier on `retinue`. FAULT-FORM-MODIFIER. Additionally, `the institutional retinue` may be a collective multi-subject. Primary fault: FAULT-FORM-MODIFIER (adjective on subject noun).
**Why:** Adjective modifier on subject slug.
**Criteria:** Line must not carry the adjective modifier. Clean form: `the retinue rounds the river bend` — or, if the multi-subject concern applies, recast as a lead actor performing the act.

---

### fault-MIS-011 — ID 342: `the column halts`

**Type:** fault
**What:** `the column` is a collective multi-subject. `halts` applied to a column describes a collective state-change, not a discrete physical act by a named singular entity. FAULT-FORM-MULTI-SUBJECT (collective noun as subject) and FAULT-FORM-NON-ACTION-VERB (collective-state description). Identical structure to original audit's fault-036 (`the column reassembles` at ID 515) and similar to other collective-subject lines.
**Why:** Collective subject; the downstream stitcher cannot render a single character performing the act.
**Criteria:** Replace with a named actor performing the discrete physical act that anchors the column's halt (e.g., `oc-lords-steward raises the hand`, `a mounted man draws rein`) or delete if halt is already implied by surrounding beats.

---

### fault-MIS-012 — ID 350: `the swarm-sense maps the dock perimeter`

**Type:** fault
**What:** The original audit's fault-021 listed `the swarm-sense maps` at IDs 158, 262, 819 — all deleted by the fixer. ID 350 carries the same pattern (`the swarm-sense maps the dock perimeter`) and was not in the fault-021 ID set. Still present. Subject `the swarm-sense` is an internal cognitive faculty; `maps the dock perimeter` is a perception/cognitive act, not an observable physical event. FAULT-FORM-INTERIORITY (same basis as fault-021).
**Why:** Same failure mode as the deleted instances — internal cognitive faculty as subject, cognitive mapping as verb.
**Criteria:** Delete; route swarm-sense awareness to narrator/feel facets citing adjacent physical fauna-behavior proto-lines.

---

### fault-MIS-013 — ID 356: `taylor-hebert-jaehaerys follows`

**Type:** fault
**What:** `follows` is a bare intransitive motion verb without destination. The original audit's fault-038 identified this pattern at the former ID 563 (which was the same bare `follows`). That instance was recast to `taylor-hebert-jaehaerys follows mira-stonefield-jaehaerys` (a correct fix). However, ID 356 carries a separate, independent `taylor-hebert-jaehaerys follows` that was not in the original audit's finding set. Still present. FAULT-FORM-NO-VERB (bare intransitive motion without destination).
**Why:** `follows` without a named destination/entity is not an observable physical act — it describes a positional relationship, not a discrete event.
**Criteria:** Add a destination: `taylor-hebert-jaehaerys follows oc-craftsman-father` (using context from surrounding beats) or recast as a discrete motion act.

---

### fault-MIS-014 — ID 419: `the market square fills`

**Type:** fault
**What:** `the market square fills` is an environment-state description (the square accumulating crowd/activity for the levy collection). Subject `the market square` performs no discrete physical act. FAULT-FORM-NON-ACTION-VERB. The original audit caught this pattern at IDs 300 and 556 but missed ID 419.
**Why:** Environment-state assertion belongs in loc-state facet.
**Criteria:** Delete; route to loc-state facet citing adjacent actor proto-lines.

---

### fault-MIS-015 — ID 420: `the collection table fills the square center`

**Type:** fault
**What:** `fills the square center` — the collection table occupying the square center is a stative placement description. `fills` here is a containment/placement verb (the table filling a space), a stative position-naming. FAULT-FORM-NON-ACTION-VERB (stative placement / containment pattern). The square center is also abstract as a direct object.
**Why:** The table being placed is a state; the discrete physical act that initiated that state (someone carrying/setting the table) would be the valid proto-line.
**Criteria:** Delete and route to loc-state facet, or replace with the named actor who places or arranges the collection table.

---

### fault-MIS-016 — ID 422: `two mounted collectors enter the square`

**Type:** fault
**What:** `two` is a quantifier adjective modifier on `mounted collectors`. `mounted` is an adjective modifier on `collectors`. Dual FAULT-FORM-MODIFIER. Additionally, `two mounted collectors` is a plural multi-subject (FAULT-FORM-MULTI-SUBJECT). Primary classification: FAULT-FORM-MULTI-SUBJECT with compound FAULT-FORM-MODIFIER.
**Why:** Plural subject and adjective modifiers.
**Criteria:** Split into two per-actor proto-lines with the adjective modifiers stripped. If the collectors are distinguishable by role, use role slugs.

---

### fault-MIS-017 — ID 454: `the collector's man grabs the sleeve again`

**Type:** fault
**What:** `again` is an adverb modifier. FAULT-FORM-MODIFIER. The original audit caught this pattern at ID 284 (`tilts the head again`) as fault-010 but missed this instance.
**Why:** Adverb modifier banned by schema.
**Criteria:** Line must read `the collector's man grabs the sleeve`. The `again` context is established by ID 452 (`the collector's man grabs the second townsman's sleeve`); the repetition is recoverable without the modifier.

---

### fault-MIS-018 — ID 475: `taylor-hebert-jaehaerys presses the feet into the cobbles`

**Type:** fault
**What:** `into the cobbles` is a prepositional phrase of destination. FAULT-FORM-MODIFIER. The clean form is `taylor-hebert-jaehaerys presses the feet`.
**Why:** Prepositional destination padding.
**Criteria:** Line must terminate at `the feet`.

---

### fault-MIS-019 — IDs 666 and 679: `taylor-hebert-jaehaerys crosses to the bench`

**Type:** fault
**What:** `to the bench` is a prepositional phrase of destination. FAULT-FORM-MODIFIER. The schema explicitly targets this class: "prefer transitive verbs that take the location as direct object." Clean form: `taylor-hebert-jaehaerys approaches the bench` or `taylor-hebert-jaehaerys reaches the bench`. Both IDs carry the identical fault.
**Why:** Prepositional destination phrase.
**Criteria:** Both lines must replace `crosses to` with a transitive motion verb that takes the bench as direct object.

---

### fault-MIS-020 — ID 680: `oc-craftsman-father sets the ledger on the bench`

**Type:** fault
**What:** `on the bench` is a prepositional phrase of location. FAULT-FORM-MODIFIER.
**Why:** Prepositional location padding.
**Criteria:** Line must read `oc-craftsman-father sets the ledger`.

---

### fault-MIS-021 — ID 692: `oc-craftsman-mother enters the workshop from the lane`

**Type:** fault
**What:** `from the lane` is a prepositional phrase of source/origin. FAULT-FORM-MODIFIER.
**Why:** Prepositional source phrase.
**Criteria:** Line must read `oc-craftsman-mother enters the workshop`.

---

### fault-MIS-022 — ID 693: `oc-craftsman-mother crosses to the mordant station`

**Type:** fault
**What:** `to the mordant station` is a prepositional phrase of destination. Same pattern as fault-MIS-019.
**Why:** Prepositional destination phrase.
**Criteria:** Replace with a transitive motion verb: `oc-craftsman-mother approaches the mordant station` or `oc-craftsman-mother reaches the mordant station`.

---

### fault-MIS-023 — ID 701: `oc-craftsman-mother sets the market basket on the table`

**Type:** fault
**What:** `on the table` is a prepositional phrase of location. Same pattern as fault-MIS-004.
**Why:** Prepositional location padding.
**Criteria:** Line must read `oc-craftsman-mother sets the market basket`.

---

### fault-MIS-024 — ID 908: `the swarm-sense extends`

**Type:** fault
**What:** `the swarm-sense extends` — subject `the swarm-sense` is an internal cognitive faculty (same basis as fault-020/021 in the original audit). `extends` here describes the passive sense expanding — an internal event, not observable by a witness. FAULT-FORM-INTERIORITY. This ID was not in the original audit's fault-020 set (which listed IDs 10, 432, 903 — all deleted).
**Why:** Internal cognitive faculty as subject; the extension of Taylor's passive sense awareness is interiority, not a physical event a witness can observe.
**Criteria:** Delete; route to narrator/feel facet citing adjacent physical fauna-behavior proto-lines.

---

### fault-MIS-025 — ID 911: `oc-craftsman-mother's voice rises`

**Type:** fault
**What:** Subject is `oc-craftsman-mother's voice`. A voice rising is a sound-level state change description — comparable to the original audit's fault-029 (`the workshop murmur rises`, deleted). The subject is a possessed abstract entity (a voice as a disembodied sound-level measure). FAULT-FORM-NON-ACTION-VERB (sound-level state description, not a discrete physical act).
**Why:** Same failure mode as fault-029. `voice rises` is an ambient-level description, not an event.
**Criteria:** Delete and route to a loc-state or sensory facet, or replace with the discrete physical act the subject performs (e.g., `oc-craftsman-mother raises the voice` is borderline — better: `oc-craftsman-mother speaks to oc-craftsman-father` if a dialogue beat is intended, or `oc-craftsman-mother calls` as a vocalization event).

---

## SECTION 4 — Advisory Flags (no fixer dispatch)

### flag-RA-001 — ID 511 ordinal `first` (see fault-R004)

The criteria for fault-R004 note that ID 511 (`the first collector's man rights the table`) carries the same ordinal modifier fault as ID 915. These are paired split lines. Fixer must address both simultaneously.

---

### flag-RA-002 — ID 412: `rymer-hedge shifts the eyes`

`shifts the eyes` is borderline: it could be read as a physical act (physically turning the eyeballs) or as a gaze-direction perception event. If gaze-direction, this is FAULT-FORM-PERCEPTION. The original audit did not flag this. Editor advisory: verify in dialogue context whether this is a gaze-shift (perception → route to facet) or a physical head/eye movement.

---

### flag-RA-003 — ID 905: `the dock mosquito circles`

`circles` as bare intransitive. The prior audit treated `oc-child-peer calls` (also bare intransitive vocalization) as flag-002 and did not fault it. `circles` is a bare intransitive motion verb; under the strict reading it faults FAULT-FORM-NO-VERB. The prior audit passed `the hearth fire pops` as a licensed object-as-subject discrete event. `circles` describes a motion pattern rather than a discrete event with a destination. Advisory: if tightening is desired, recast as `the dock mosquito orbits the folio` or similar transitive form; otherwise leave for Pass 4 trim.

---

### flag-RA-004 — Retained advisory flags from prior audit

Prior-audit flags flag-001 (ID 855 dialogue advisory) and flag-002 (ID 302 `oc-child-peer calls`) remain applicable. Neither was touched by the fixer. Both are editor-advisory only.

---

## SECTION 5 — Verified Resolutions (prior faults confirmed closed)

The following prior-audit fault clusters are confirmed resolved in the current file:

| Fault cluster | IDs actioned | Status |
|---|---|---|
| fault-001 — holds the swallow neutral | 124 recast | Partial — recast introduced fault-R001 |
| fault-002 — holds the fly (x2) | 194, 264 recast | Partial — recasts introduced fault-R002 |
| fault-003 — holds the bench edge | 722, 797 recast to `grips` | CLOSED |
| fault-004 — holds the pace (6 instances) | 258, 301, 560, 650, 820, 828 deleted | CLOSED (ID 192 survives — fault-NUA-001) |
| fault-005 — holds the pause | 635, 713 deleted | CLOSED |
| fault-006 — holds the temple pressure | 490, 519 deleted | CLOSED |
| fault-007 — releases the radius check | 79 deleted | CLOSED |
| fault-008 — holds the chin level | 14 recast | CLOSED |
| fault-009 — releases the angle | 53 deleted | CLOSED |
| fault-010 — tilts the head again | 284 recast | CLOSED |
| fault-011 — points the finger at the line | 191 recast | CLOSED |
| fault-012 — waits (x2) | 219, 428 deleted | CLOSED |
| fault-013 — the square fills (x2) | 300, 556 deleted | CLOSED |
| fault-014 — the lane empties | 750 deleted | CLOSED |
| fault-015 — releases the fly/moth | 28, 71 recast | CLOSED |
| fault-016 — releases the pen grip | 249 recast | CLOSED |
| fault-018 — advances the queue | 439 recast | CLOSED |
| fault-020 — swarm-sense fills radius | 10, 432 deleted (903 pre-existing gap) | CLOSED |
| fault-021 — swarm-sense maps | 158, 262, 819 deleted | CLOSED (ID 350 survives — fault-MIS-012) |
| fault-022 — workshop settles | 792 deleted | CLOSED |
| fault-023 — square traffic flows | 646, 887 deleted | CLOSED |
| fault-024 — district/alley/lane opens/closes | 225, 566, 703, 716, 736 deleted | CLOSED |
| fault-025 — workshop murmur continues | 72 deleted | CLOSED |
| fault-026 — points to the first line | 169 recast | CLOSED |
| fault-027 — household/workshop quiets | 77, 122, 535, 671 deleted | CLOSED |
| fault-028 — workshop murmur rises | 902 pre-existing gap | CLOSED |
| fault-029 — dock crowd shifts its weight | 337 recast | CLOSED |
| fault-030 — square traffic adjusts | 813 deleted | CLOSED |
| fault-031 — townspeople form the queue | 425 deleted | CLOSED |
| fault-032 — collection queue breaks | 513 deleted (audit listed as 563) | CLOSED |
| fault-033 — two of the collector's men | 511 recast + 915 split | Partial — ordinal modifiers survive (fault-R004) |
| fault-034 — two mounted men lead the column | 334 recast + 914 split | Partial — 914 introduces fault-R003 |
| fault-035 — lamp glow reaches loft beam | 66, 913 deleted/pre-existing gap | CLOSED |
| fault-036 — column reassembles | 515 deleted | CLOSED |
| fault-037 — square traffic re-forms | 509, 563 deleted | CLOSED |
| fault-038 — loft closes | 901 pre-existing gap | CLOSED |
| fault-039 — oc-craftsman-mother answers | 74 recast | CLOSED |
| fault-040 — matches the pace | 222 recast | CLOSED |
| fault-041 — levy roll spreads on resettled table | 512 recast | CLOSED |
| fault-043 — folio changes hands | 909 pre-existing fix confirmed | CLOSED |
| fault-017 (flag) — fills the two cups | 763 retained | OPEN as prior flag |

---

## SECTION 6 — ID Coherence Verification

**Fixer anomaly 1 (ID drift):**
- Audit ID 563 for `the collection queue breaks` → was actually at file ID 513. ID 513 is now blank ✓
- Audit ID 716 for `the market lane opens` → was at file ID 736. ID 736 is now blank. ID 716 in current file = `septon-rowan speaks to oc-craftsman-mother` (valid dialogue beat) ✓
- Audit ID 563 for `re-forms` → was at file ID 509. ID 509 is now blank ✓

**Fixer anomaly 2 (ID 192):** Confirmed present as fault-NUA-001 above.

**Pre-existing gaps confirmed absent:** IDs 901, 902, 903, 913 do not appear in the file. All faults referencing those IDs from the prior audit are treated as resolved via pre-existing deletion.

**Split-from comment format:** ID 914 carries `# split-from: 334`; ID 915 carries `# split-from: 511`. Both comments are present and correctly formatted. Split-from IDs match the recast source lines. ✓

---

## Consolidated Finding Count

| Category | Count |
|---|---|
| Recast regressions (new faults introduced by fixer) | 4 (fault-R001, fault-R002 [2 IDs], fault-R003, fault-R004) |
| Unaudited fault confirmed present (fixer-flagged) | 1 (fault-NUA-001) |
| Pre-existing faults missed by original audit | 25 (fault-MIS-001 through fault-MIS-025, some covering multiple IDs) |
| Advisory flags | 4 (flag-RA-001 through flag-RA-004) |
| Prior faults confirmed closed | 42 |

**Total open faults requiring fixer action:** 30 fault findings (spanning approximately 40+ IDs)

---

## Routing

- **Fixer dispatch required:** fault-R001 through fault-R004, fault-NUA-001, fault-MIS-001 through fault-MIS-025
- **Editor advisory retained:** flag-RA-001 through flag-RA-004, prior-audit flag-001, flag-002, fault-017
- **No escalations**
- **Phase 2 Pass 3 (shape) cannot dispatch** until the fixer pass above resolves and a third convergence re-audit confirms PASS
