# Audit Report — Chapter 04 Proto-lines, Pass 2 Constraint Re-verification

schema: audit-report
run: pass2-reverify
target: active-project/theater/proto-lines/chapter-04.md
auditor-fork: fresh (no carry-over from prior pass 2 dispatch)
date: 2026-05-07

---

## Summary

| Metric | Count |
|--------|-------|
| Total numbered lines | 98 |
| Blank time-skips (excluded from check) | 2 (lines 51, 95) |
| Lines checked | 96 |
| CORRECT | 88 |
| FAULT | 8 |
| FLAG (advisory, not fault) | 2 |

CONTINUITY-OK: NO. 8 faults present. File does not advance to pass 3 until fixer resolves all faults.

---

## Header Check

- `narrator: taylor-hebert-westeros` — slug present in series cast roster. PASS.
- `goal:` — present and non-empty. PASS.

---

## Faults

---

### fault-001

- **id:** fault-001
- **type:** fault
- **line:** 11
- **content:** `the riders dismount the north track`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `the north track` is a location, not the thing dismounted. `dismount` does not act on a track; the track is implicitly `at the north track` — a prepositional location phrase recast as a false direct object.
- **why:** The verb-object bond is semantically broken. A location masquerading as a direct object is prepositional padding in SVO-stripped form. Shape and downstream facets reading this line will misread the object as something acted upon.
- **criteria:** Recast to strip the false object. Valid forms: `the riders dismount` (intransitive; the horses are implied) or `the riders leave the horses` (if the dismount-and-tie action is the beat). If location context is required, route to a location-state citation at facet time.
- **recommended fixer action:** RECAST-PHYSICAL — drop `the north track` or replace with the physical thing dismounted.

---

### fault-002

- **id:** fault-002
- **type:** fault
- **line:** 17
- **content:** `oc-castellan-harrenhal walks the nave length`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `length` is a measurement abstraction appended to the object `the nave`. `the nave length` is not a named entity or a `the <noun>` naming a physical thing — it is `the nave` plus a padding qualifier that encodes extent.
- **why:** Measurement qualifiers on objects violate the no-modifier rule. The downstream stitcher has no physical anchor for `length`; it reads as decoration.
- **criteria:** Recast as `oc-castellan-harrenhal walks the nave`. The full-length traversal is implied by context and can be specified in a location-state or tensometer citation.
- **recommended fixer action:** DELETE `length` — recast as `oc-castellan-harrenhal walks the nave`.

---

### fault-003

- **id:** fault-003
- **type:** fault
- **line:** 62
- **content:** `oc-castellan-harrenhal turns to the raven`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `to the raven` is a prepositional directional phrase, not a direct object. `turns` does not take `the raven` as a bare direct object; the `to` is structural and names a direction/target, making the phrase prepositional padding.
- **why:** The SVO spine requires objects to be the thing the verb acts upon. Direction-of-motion phrases are location/movement qualifiers, which belong in citations, not in the bone line. Inconsistent handling of `turns to X` across the file corrupts shape decisions.
- **criteria:** Recast as a physical action that names what is acted upon: `oc-castellan-harrenhal faces the raven` (if facing is the observable event) or split into two beats if the rotation and the facing are distinct. Alternatively, confirm `turns to X` is canonically permitted as a directional-verb object form and apply that ruling uniformly to lines 62, 63, and 86; if confirmed, all three flip to CORRECT.
- **recommended fixer action:** RECAST-PHYSICAL — `oc-castellan-harrenhal faces the raven` or equivalent.

---

### fault-004

- **id:** fault-004
- **type:** fault
- **line:** 63
- **content:** `the raven swings the head to oc-castellan-harrenhal`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `to oc-castellan-harrenhal` is a prepositional directional phrase appended after the SVO core `the raven swings the head`. The `to X` phrase names the direction of the swing, not an object acted upon.
- **why:** Same as fault-003. Prepositional directional phrases after a completed SVO are modifier padding. The beat is fully expressed as `the raven swings the head`; the direction is a qualifier that belongs in facet context.
- **criteria:** Recast as `the raven swings the head` (strip the directional phrase). If the target of the head-swing is load-bearing at this level, model it as a separate beat or route to a location-state citation.
- **recommended fixer action:** DELETE `to oc-castellan-harrenhal` — recast as `the raven swings the head`.

---

### fault-005

- **id:** fault-005
- **type:** fault
- **line:** 68
- **content:** `the raven digs the talons`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `the talons` is the raven's own instrument (body part used to dig), not the thing being dug into. The physical target of the action — Taylor's arm — is absent. The implied full form is `the raven digs the talons into [the arm]`, where `into the arm` is the missing prepositional phrase. What remains after stripping the prep is the instrument, not the object.
- **why:** When the retained object is the instrument of the action rather than the thing acted upon, the SVO bond is inverted. The downstream stitcher reads `the talons` as what is acted upon, not as what is acting. This produces a misread beat: the raven acting on its own talons rather than on Taylor.
- **criteria:** Recast to name the thing acted upon: `the raven clamps the arm` or `the raven drives the talons into the arm` — but the latter reintroduces a prepositional phrase. Cleanest: `the raven clamps the arm` (physical grip on Taylor's arm as the direct object).
- **recommended fixer action:** RECAST-PHYSICAL — `the raven clamps the arm` or equivalent where the direct object is the target of the action.

---

### fault-006

- **id:** fault-006
- **type:** fault
- **line:** 75
- **content:** `ser-harwick-plumm completes the sketch`
- **fault class:** FAULT-FORM-NON-ACTION-VERB
- **what:** `completes` is an achievement/state-termination verb. Its primary semantic is the crossing of a completion threshold — a cognitive/relational state — not a discrete observable physical act. What an observer sees is the final stroke of the stylus or the stylus being lowered or lifted away, not "completion."
- **why:** State-termination verbs are in the same prohibited class as state-assertion verbs. They describe the outcome of an action rather than the action itself. Allowing `completes` opens the door to `finishes`, `achieves`, `concludes`, and other state-transition verbs that encode outcome not act.
- **criteria:** Recast as the physical act that constitutes completion: `ser-harwick-plumm lifts the stylus` (drawing ends when the tool leaves the surface) or `ser-harwick-plumm lowers the stylus` (if the motion is setting it down). The completion inference is downstream.
- **recommended fixer action:** RECAST-PHYSICAL — replace `completes the sketch` with the final physical act of the drawing action.

---

### fault-007

- **id:** fault-007
- **type:** fault
- **line:** 78
- **content:** `oc-castellan-harrenhal examines the page`
- **fault class:** FAULT-FORM-PERCEPTION
- **what:** `examines` is a perception-inspection verb. It names a cognitive/sensory process (scrutiny, inspection) rather than a discrete physical action. It belongs to the same prohibited class as `read`, `noted`, `measured`, `tracked` — verbs that name what is happening inside the observer rather than what is happening to the object.
- **why:** Perception verbs are POV-leaks. `examines` names the inspector's internal scrutiny process, not a physical event an outside observer could verify. Allowing it corrupts the bone-only contract and introduces narrator-interiority through the verb choice.
- **criteria:** Recast as the physical observable event: what a bystander sees is the inspector's eyes moving over the page, the page being turned, the inspector tilting the page toward light. Valid recasts: `oc-castellan-harrenhal turns the page` or `oc-castellan-harrenhal holds the page` (licensed use — body-part/prop held against movement, here visual inspection as a holding action). Cleanest: `oc-castellan-harrenhal studies the page` is still a perception verb — avoid. `oc-castellan-harrenhal tilts the page` or `oc-castellan-harrenhal turns the page`.
- **recommended fixer action:** RECAST-PHYSICAL — replace `examines` with the discrete physical act an observer would see.

---

### fault-008

- **id:** fault-008
- **type:** fault
- **line:** 86
- **content:** `oc-castellan-harrenhal turns to the bell tower`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** Identical structure to fault-003. `to the bell tower` is a prepositional directional phrase naming the direction of the turn, not a direct object.
- **why:** Same as fault-003. Directional `to X` phrases are location qualifiers; the bell tower is a destination of the turn's direction, not something being physically acted upon.
- **criteria:** Recast as `oc-castellan-harrenhal faces the bell tower` or `oc-castellan-harrenhal looks to the bell tower` — but note `looks` is also a perception verb. Best recast: `oc-castellan-harrenhal faces the bell tower`. If the ruling on `turns to X` resolves to CORRECT at fault-003, apply that ruling here uniformly.
- **recommended fixer action:** RECAST-PHYSICAL — `oc-castellan-harrenhal faces the bell tower` or equivalent.

---

## Flags (advisory — not faults, no fixer dispatch required)

---

### flag-001

- **id:** flag-001
- **type:** flag
- **lines:** 45, 46, 47
- **content:** `ser-harwick-plumm opens the satchel` / `ser-harwick-plumm produces a page` / `ser-harwick-plumm produces a stylus`
- **what:** The satchel, page, and stylus are not listed as fixed props in `loc-harrenhal-sept-environs.card.md`. They are carry-in props attributable to ser-harwick-plumm's inventory. Actor state files are outside pass 2 scope (pass 5 carries prop-continuity checks).
- **why:** If ser-harwick-plumm's episode-open inventory does not include a satchel, page, and stylus, these lines are FAULT-PHYSICAL-PROP-ABSENT. Pass 2 cannot confirm or deny without the actor state file. The props are plausible for a census/inspection officer but unverified.
- **criteria:** Pass 5 continuity audit must verify ser-harwick-plumm's carry-in inventory includes satchel + page + stylus, or confirm the satchel is a prop introduced at this chapter's open. No fixer action at this pass.

---

### flag-002

- **id:** flag-002
- **type:** flag
- **lines:** 39, 72, 74, 91, 92
- **content:** `the third rider produces a ledger` / `the third rider opens the ledger` / `the third rider marks the ledger` / `the third rider closes the ledger` / `the third rider stows the ledger`
- **what:** The ledger is not a fixed prop of the location and is introduced by `the third rider` at line 39. This is a carry-in prop attributable to the third rider. No actor state file for `the third rider` is available in pass 2 scope.
- **why:** Consistency across all five ledger lines depends on the ledger being introduced at line 39 and remaining in the third rider's hands through line 92. The sequence is internally consistent. Pass 5 must verify no prior deletion disrupts the chain.
- **criteria:** Pass 5 continuity audit should confirm the ledger chain (39 → 72 → 74 → 91 → 92) is unbroken after pass 4 trim. No fixer action at this pass.

---

## CORRECT Lines (not enumerated individually)

Lines 1–10, 12–16, 18–23, 24–32, 33–35, 36–38, 40–50, 52–61, 64–67, 69–74, 76–77, 79–85, 87–94, 96–98 — all CORRECT under SVO mechanics, constraint cards, and physical checks.

---

## Constraint Summary

| Card | Violations found |
|------|-----------------|
| cond-fauna-control-rules | None. Single-raven brief interaction is within 0–5 min cost-free window. Observable anomaly is the chapter's intended event. |
| cond-riverlands-120ac-state | None. Inspection visit is consistent with impressment/administrative pressure described in card. |
| cond-westerosi-customary-authority | None. Taylor does not initiate speech to oc-castellan-harrenhal; all exchanges show castellan speaking first. |
| cond-series-tone-constraints | Not applicable at pass 2 (per-line SVO/physical check only; tone register is pass 3 scope). |

Series laws checked: No violation. No parahuman infrastructure invoked. No Shards, no PRT. Taylor's fauna-control is shown as observable wrongness per law. Physical cost mechanics not violated by single-raven brief use.

---

## Fixer Routing

Dispatch fixer against: fault-001, fault-002, fault-003, fault-004, fault-005, fault-006, fault-007, fault-008.

Recommended actions:
- fault-001 (line 11): RECAST-PHYSICAL — `the riders dismount` (drop false object).
- fault-002 (line 17): RECAST-PHYSICAL — `oc-castellan-harrenhal walks the nave` (drop `length`).
- fault-003 (line 62): RECAST-PHYSICAL — `oc-castellan-harrenhal faces the raven` or canonize `turns to X` and flip all three (62, 63, 86) to CORRECT simultaneously.
- fault-004 (line 63): DELETE directional phrase — `the raven swings the head`.
- fault-005 (line 68): RECAST-PHYSICAL — `the raven clamps the arm`.
- fault-006 (line 75): RECAST-PHYSICAL — `ser-harwick-plumm lifts the stylus` or `ser-harwick-plumm lowers the stylus`.
- fault-007 (line 78): RECAST-PHYSICAL — `oc-castellan-harrenhal turns the page` or equivalent observable physical act.
- fault-008 (line 86): RECAST-PHYSICAL — `oc-castellan-harrenhal faces the bell tower` (or resolve with fault-003 ruling).

Note on fault-003 / fault-008 coupling: if the orchestrator rules that `turns to <named entity>` is a canonically permitted directional-verb form (analogous to `speaks to <listener>`), then fault-003 and fault-008 both flip to CORRECT and no fixer action is needed for those two lines. fault-004 (`swings the head to X`) would need separate ruling. Recommend orchestrator make this ruling before dispatching fixer to avoid two fixer passes on lines 62 and 86.

---

## Termination Status

CONTINUITY-OK: NO. Re-run pass 2 after fixer commits changes. Re-run is scoped to the 8 modified lines only; clean lines are not re-checked.
