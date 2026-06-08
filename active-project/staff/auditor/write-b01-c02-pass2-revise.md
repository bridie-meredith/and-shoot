# /and-write b01c02 revise — Phase 2 constraint audit
# Date: 2026-05-26
# Auditor: auditor (fork)

## Verdict
FAIL (7 faults)

---

## Bone-by-bone classification

- s01n01: CORRECT
- s01n02: CORRECT
- s01n03: CORRECT
- s01n04: FAULT-FORM (see below)
- s01n05: CORRECT
- s01n06: CORRECT
- s01n07: CORRECT
- s01n08: CORRECT
- s01n09: CORRECT
- s01n10: FAULT-FORM (see below)
- s01n11: CORRECT
- s01n12: CORRECT
- s01n13: CORRECT
- s01n14: CORRECT
- s02n01: CORRECT
- s02n02: CORRECT
- s02n03: CORRECT
- s02n04: CORRECT
- s02n05: CORRECT
- s02n06: FAULT-FORM (see below)
- s02n07: CORRECT
- s02n08: CORRECT
- s02n09: CORRECT
- s02n10: CORRECT
- s02n11: CORRECT
- s02n12: CORRECT
- s02n13: CORRECT
- s02n14: FAULT-FORM (see below)
- s02n15: FAULT-FORM (see below)
- s03n01: CORRECT
- s03n02: CORRECT
- s03n03: FAULT-FORM (see below)
- s03n04: CORRECT
- s03n05: FAULT-FORM (see below)
- s03n06: CORRECT
- s03n07: CORRECT
- s03n08: CORRECT
- s03n09: CORRECT
- s03n10: CORRECT
- s03n11: CORRECT
- s03n12: FAULT-FORM (see below)
- s03n13: CORRECT
- s03n14: CORRECT
- s03n15: CORRECT
- s03n16: CORRECT
- s03n17: CORRECT
- s03n18: CORRECT

---

## Faults

### FAULT-FORM

**fault-001** — s01n04: `"the fever-cluster returns three heat-signatures without a common room"`
- The phrase "without a common room" is a negation modifier (PP expressing an absent condition).
- Schema: "No negations" (`FAULT-FORM-NEGATION`) and "No modifiers — no prepositional padding" (`FAULT-FORM-MODIFIER`). A non-event is not a bone; "without a common room" describes what the heat-signatures do not share, not what they do.
- Why it matters: the fever-cluster ambiguity (the motivating unresolved question for this scene) is narratively load-bearing. If this bone carries it, the form is the wrong carrier. Recast to what the insects return positively: e.g., "the fever-cluster returns three heat-signatures across two alleys" or split into the two bones that each describe a signature location.
- Criteria: rewrite to remove "without" construction; encode the ambiguity as a positive return that cannot resolve to a single room (e.g., separate location-return bones for the three signatures, or a bone for each alley the feed maps without anchoring).

**fault-002** — s01n10: `"the feed taxes the peripheral attention"`
- Two violations: (a) "peripheral" is an adjective modifier on "attention" (`FAULT-FORM-MODIFIER`); (b) "attention" is an interior/abstract noun object — a thought-figure, not a physical object or observable event (`FAULT-FORM-INTERIORITY`). "Taxes" is also a metaphorical verb whose semantic is a ratio-relationship, not a concrete observable act.
- Why it matters: the suppression-cost grounding is a new fix-queue item (item 1) that must survive the form gate to reach facets. Interiority-as-object at this bone means the physical cost has no physical bone; the facet will have nothing concrete to cite.
- Criteria: rewrite to a physical event the suppression cost enacts on the body — e.g., "the orbital ridge tightens" or "the alley-back drops from the feed" (the peripheral zone going dark as a physical feed-event). Subject should be Taylor or a feed element; verb should be a concrete physical act.

**fault-003** — s02n06: `"taylor-hebert-kl-122ac takes the drain angle at the grey hour"`
- "at the grey hour" is a PP of time. Schema: "Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned (`FAULT-FORM-MODIFIER`)." Time-PP falls under this prohibition — time goes in location-state citations, not in the SVO line.
- Why it matters: the PP is not trivial padding here; it carries the time-of-return signal this bone is authored to provide (fix-queue item 4, bridging bone). But the signal must route through location-state citation, not inline PP.
- Criteria: remove "at the grey hour" from the SVO field. Time-of-day goes in a loc-state citation or a companion environmental bone (the grey-hour physical marker is already s03n03 at the scene close — a forward seam bone, not a location in s02). The bare form "taylor-hebert-kl-122ac takes the drain angle" is correct.

**fault-004** — s02n14: `"the insects return the attenuated signal at the junction-lane boundary"`
- "at the junction-lane boundary" is a PP of place/location appended to the object. Schema: PPs of place are banned (`FAULT-FORM-MODIFIER`). The object "the attenuated signal" does not intrinsically encode location; the PP is doing work the SVO form cannot carry.
- Why it matters: this is the SOFT-WATCH-2 compliance bone (gap staged as feed-event). The fix-queue item is structurally important. The location qualifier needs to move into a loc-state citation or the object noun must be refactored to carry the spatial identity (e.g., "the junction-lane signal attenuates" is not SVO-clean either). Best recast: "the insects return the junction-lane signal attenuated" fails because "attenuated" becomes an adjective. Clean path: "the insects return the junction-lane void" (the attenuation is already implied by "void") — but this collapses s02n14 and s02n15. Alternatively: "the insects reach the junction-lane boundary" (separate action bone) + "the insects return the attenuated signal" (no PP). Either path is fixer-territory.
- Criteria: remove the PP "at the junction-lane boundary" from the SVO. Spatial identity either moves to loc-state citation, is embedded in the object noun as a compound (junction-lane-signal or junction-lane-return), or requires a separate positioning bone.

**fault-005** — s02n15: `"the coverage map holds the junction-lane void"`
- Narrow `holds` license applies only to: (1) body part of subject with stillness-against-pressure, or (2) physical object resisting pressure. "The coverage map" is neither a body nor a door; "the junction-lane void" is an abstract noun (an absence, a negative space). Both conditions for the license fail. Additionally, a void/absence as object is abstraction-as-object, which faults `FAULT-FORM-INTERIORITY`.
- Why it matters: this bone is the s02 scene-close — the gap held as a specific spatial absence. The narrative content is load-bearing (SOFT-WATCH-2 compliance). The form invalidates it; the stitcher cannot cite this bone as a physical event.
- Criteria: recast to a physical action the coverage map performs on a physical object, or recast the subject/verb pair. E.g., "the coverage map opens the junction-lane gap" (if an opening action is the bone) or "the insects stop at the junction-lane boundary" (physical stop, concrete actor). The absence must be encoded as a positive physical event whose result is readable as absence.

**fault-006** — s03n03: `"the drain angle fills with shadow"`
- "with shadow" is a PP of instrument/accompaniment (`FAULT-FORM-MODIFIER`). "Shadow" is borderline between physical phenomenon and abstract quality; "fills with shadow" reads as a process PP, not a direct transitive object. The clean transitive form would be "shadow fills the drain angle" (subject-verb-object reversal), which is fine — but the current form has the angle as the subject and "with shadow" as the PP modifier on the act.
- Why it matters: this is a time-marker bone (fix-queue item 7, seam-bridging beat). Low narrative weight; form fault is correctable by subject-swap.
- Criteria: rewrite as "the shadow fills the drain angle" (subject: the shadow; verb: fills; object: the drain angle). This is a clean SVO where shadow is a concrete physical thing doing a physical act on a physical location.

**fault-007** — s03n12: `"the feed holds the ward-junction void in the open count"`
- Multiple violations: (a) "holds" is unlicensed — "the feed" is not a body performing stillness-against-pressure; "the ward-junction void" is not a physical object resisting pressure (`FAULT-FORM-NON-ACTION-VERB`); (b) "ward-junction void" is an abstract noun (absence), so this is also abstraction-as-object (`FAULT-FORM-INTERIORITY`); (c) "in the open count" is a PP of location/circumstance, banned as modifier padding (`FAULT-FORM-MODIFIER`).
- Why it matters: this is the SOFT-WATCH-1 holding-bone (recognition → holding → suppression). It is structurally load-bearing: the three-bone decomposition at s03n11–n13 is the SOFT-WATCH-1 compliance mechanism. A form fault at the middle bone means the holding beat has no valid physical event to cite; the three-bone structure exists on paper but the facet cannot build on the center bone.
- Criteria: recast the holding-bone as a concrete physical act that enacts the pause without interiority-as-object. E.g., "the feed returns the ward-junction void" (subject: the feed; verb: returns; object: the junction-lane void — still has the "void" problem) — or better: "taylor-hebert-kl-122ac stills the count" (Taylor's body stilling as a physical act) or "the insect-feed pauses at the ward-junction lane" (also has a PP; needs care). Cleanest path: make Taylor the subject performing a concrete physical stillness-act that the holding-beat enacts, e.g., "taylor-hebert-kl-122ac holds the count" (if the count can be read as a physical object she is physically not-closing — borderline licensed under physical-object-resisting-pressure if "the count" is treated as a physical tally act rather than an abstract state). Fixer to evaluate; the beat intent is clear.

---

### FAULT-CONSTRAINT
None found. All SVO lines are free of Earth-Bet parahuman jargon (no Khepri, Skitter, Brockton Bay, parahuman, cape, PRT, shard, trigger, or related vocabulary). KL court-state lore not invoked; no Daemon in KL, no age-of-Lucerys references. Taylor POV is first-person consistent per cond-taylor-pov-behavior (subject is taylor-hebert-kl-122ac or the <noun> ambient form throughout). No theme-narration in any SVO line.

### FAULT-PHYSICAL
None found. All action is located in the Hook precinct (drain angle, alleys, ward-junction, stitch-house lane) consistent with b01c02 handoff_in and the chapter location architecture established in b01c01. No actors appear outside their established locations. No props referenced that are not on-set.

### FAULT-BONE-DELTA-MALFORMED
None found. All axis slugs in axis_moves[] and axes_held[] are valid state_axes slugs (capability, moral_framework, moral_legibility_to_self, relational_anchor_status, social_tether-prot-rise, political_register-prot — all confirmed in memory.md state_axes). The two axis-movers (s02n13: relational_anchor_status +1.0 up; s03n11: moral_legibility_to_self +1.0 up) use valid directions and magnitudes. Both magnitudes are within bone-level delta_per_axis range (1–3). cost_ledger_anchor: null on both is consistent with the chapter contract (both chapter-level axes_in_motion carry cost_ledger_anchor: null). All held bones carry non-empty rationales naming the discipline the bone enacts; no generic placeholder text found.

### FAULT-AGGREGATE-DELTA-MISMATCH
None found. See aggregate-axis verification below.

### FAULT-COST-LEDGER-UNRESOLVED
None found. No axis-mover references a cost_ledger[] id. Both use null, consistent with the chapter contract.

---

## Aggregate-axis verification

- **s01:** axes_in_motion target: empty (all held). No bone in s01 carries axis_moves[]. CONFIRMED.
- **s02:** relational_anchor_status target +1.0 (up). Delivered: s02n13 is the sole axis-mover at +1.0 up. No other bone in s02 carries axis_moves[]. Aggregate: +1.0 EXACT. CONFIRMED.
- **s03:** moral_legibility_to_self target +0.5 (up); prior bone-gate confirmed +1.0 within ±1 tolerance. Delivered: s03n11 is the sole axis-mover at +1.0 up. No other bone in s03 carries axis_moves[]. Aggregate: +1.0, within ±1 of 0.5 target. CONFIRMED.

---

## Held-axis-witnessed check

For each scene's contract `axes_held[]`, the bone that witnesses each held axis (i.e., has that axis in its own `axes_held[]`):

**s01 contract axes_held:** capability, moral_framework, moral_legibility_to_self, relational_anchor_status, social_tether-prot-rise, political_register-prot

| axis | witnessing bone(s) |
|---|---|
| capability | n01, n02, n03, n04, n05, n06, n07, n08, n09, n10, n11, n13 |
| moral_framework | n04, n10, n12 |
| moral_legibility_to_self | **none** |
| relational_anchor_status | **none** |
| social_tether-prot-rise | **none** |
| political_register-prot | **none** |

Four contract-held axes carry zero bone-level witnesses in s01. These axes (moral_legibility_to_self, relational_anchor_status, social_tether-prot-rise, political_register-prot) are held at the scene level but no individual bone in s01 declares them as rationale-axes. This is a **flag** (diagnostic gap, not a hard fault under the current schema, since the schema mandates rationale on declared axes_held but does not require every scene-level held axis to have a bone-level witness — the substance_delta per-bone lives in showrunner memory and the draft uses a simpler format). However, it means the stitcher has no bone to anchor these held-axis rationales to in s01.

**s02 contract axes_held:** capability, moral_framework, moral_legibility_to_self, social_tether-prot-rise, political_register-prot

| axis | witnessing bone(s) |
|---|---|
| capability | n02, n03, n06, n09, n12 |
| moral_framework | n09, n12 |
| moral_legibility_to_self | **none** |
| social_tether-prot-rise | **none** |
| political_register-prot | **none** |

Same pattern: moral_legibility_to_self, social_tether-prot-rise, political_register-prot unwitnessed in s02.

**s03 contract axes_held:** capability, moral_framework, relational_anchor_status, social_tether-prot-rise, political_register-prot

| axis | witnessing bone(s) |
|---|---|
| capability | n01, n02, n03, n04, n05, n06, n07, n08, n15, n16, n18 |
| moral_framework | n12, n13, n14 |
| relational_anchor_status | n09, n10, n17 |
| social_tether-prot-rise | **none** |
| political_register-prot | **none** |

`social_tether-prot-rise` and `political_register-prot` are unwitnessed in s03 as well.

**Summary:** `social_tether-prot-rise` and `political_register-prot` are contract-held axes with zero bone-level witnesses across all three scenes. `moral_legibility_to_self` is unwitnessed in s01 and s02 (correctly it only fires in s03 as an axis-mover, so its held status in s01/s02 is legitimate — the absence of a witness bone for it in those scenes reflects that no bone needed to specifically argue for its held status). The social_tether-prot-rise and political_register-prot gaps are more notable: the chapter contract holds these explicitly but no bone performs any work to enact the discipline. This is consistent with the chapter's narrowly scoped content (Flea Bottom, solo Taylor, no patron/court content) — but means the held-axis witness gap is an authoring choice, not a schema error. Flagging for fixer awareness; not escalating.

---

## Summary of findings requiring fixer action

7 hard faults, all FAULT-FORM. Distributed: s01 (2), s02 (3), s03 (2).

| id | bone | fault-class | one-line summary |
|---|---|---|---|
| fault-001 | s01n04 | FAULT-FORM-NEGATION / FAULT-FORM-MODIFIER | "without a common room" is a negation PP; remove and recast as positive return bones |
| fault-002 | s01n10 | FAULT-FORM-MODIFIER / FAULT-FORM-INTERIORITY | "peripheral attention" — adjective modifier + abstract-as-object; recast as physical body-event |
| fault-003 | s02n06 | FAULT-FORM-MODIFIER | "at the grey hour" is a time-PP; remove from SVO |
| fault-004 | s02n14 | FAULT-FORM-MODIFIER | "at the junction-lane boundary" is a place-PP; remove from SVO |
| fault-005 | s02n15 | FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY | "holds" unlicensed; "void" is abstraction-as-object; recast as physical act |
| fault-006 | s03n03 | FAULT-FORM-MODIFIER | "fills with shadow" is a PP form; recast as "the shadow fills the drain angle" |
| fault-007 | s03n12 | FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY / FAULT-FORM-MODIFIER | "holds" unlicensed, "void" is abstraction, "in the open count" is a PP; recast as concrete physical hold-act |

Constraint compliance: CLEAN. Physical presence: CLEAN. Delta math: CLEAN. Cost ledger: CLEAN. Axis-slug validity: CLEAN.
