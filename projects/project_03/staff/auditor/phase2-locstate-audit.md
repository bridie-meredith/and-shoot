---
task: phase2-locstate-audit
target-corpus: design/shoot-v2/phase2-locstate-output.md
rubric-version: V2 locked (design/shoot-v2/rubric-location-state.md)
date: 2026-05-06
---

# Phase 2 Location-State Audit

---

### Intent C

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (first beat anchoring distance-read at Harrenhal exterior, strip test fails without it); interestingness passes (one focus-element: amber smear); frugality passes (first entry for this sub-location in this episode).
NOTES: Form is well-shaped — 5 pipe-delimited fields, conditions slot carries gatehouse-lantern-on, sensory note is 4 words and names a single perceptible element.

---

### Intent 1

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (episode-open transitional verb, entry-through-gate is the scene's first movement anchor); interestingness passes (one focus-element: gate threshold with packed-dirt yard); frugality passes (no prior entry, licenses subsequent yard beats).
NOTES: Conditions slot carries two values (gate-open, cond-impressment-census-120ac) — both are observable active conditions, not actor-state; permissible. Sensory note is 5 words and names a single location fact.

---

### Intent 2

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (door-state change from shut to open, PL12 crouching beat requires established aperture; strip test fails); interestingness passes (one focus-element: swept granary floor — new, revealed by the opening); frugality passes (records state-change, not inherited re-naming).
NOTES: Form clean. Conditions slot records resulting state (door-open), not the action-verb itself. Sensory note is 4 words.

---

### Intent 3

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (arch is a distinct threshold from the side-door already in inherited state; new sub-location boundary, strip test fails for zone disambiguation); interestingness passes (two elements named in sensory note — "arch threshold distinct from side door" is directional but the conditions slot carries rushes-underfoot separately; sensory note names one location fact); frugality passes (first entry for arch sub-location; prior inherited state covers side-door area only).
NOTES: The chosen draft C's sensory note reads "arch threshold distinct from side door" — this is a relational description rather than a single named perceptible element. It does not fail the pointing test (one thing named: the arch threshold) but the "distinct from side door" clause is explanatory, not perceptible. Marginal on interestingness; rubric does not explicitly prohibit relational clauses; not a violation. Rushes-underfoot properly in conditions slot.

---

### Intent 4

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (door-state changes from shut to open; PL57 "the cold arrives" requires established aperture; strip test fails); interestingness passes (one focus-element: cold air at the threshold); frugality passes (records state-change since last cited entry with door-shut).
NOTES: Form clean. "exterior-cold" in conditions is an observable environmental state, not actor-state. Sensory note is 5 words.

---

### Intent 5

VERDICT: FIRE-INCORRECT
RUBRIC CHECK: Necessity passes (new sub-location crossing, interior vs. exterior, strip test fails). Frugality passes (new sub-location, prior entry held exterior). Interestingness FAILS — the chosen sensory note "nave interior, yard drops off the plane" contains two focus-elements: (1) the nave interior itself and (2) "yard drops off the plane." The rubric requires one focus-element only. The conditions slot also carries "channel-reindexed" which is an internal perceptual state (interiority pushed into the conditions field) — conditions must record observable location states, not actor perception-channel states. Anti-pattern: interiority in conditions slot (rubric §necessity REJECT: "interiority pushed into physical SVO").
NOTES: The sensory note has two elements (fails axis 2). The conditions slot carries "channel-reindexed" which is actor-state / interiority, not an observable location condition (violates form rule: no actor-state in conditions slot per rubric example and the schema's location-state definition).

---

### Intent 6

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (first beat at new location, village-common; new-location first-beat exception applies; strip test fails for subsequent trestle/bench beats); interestingness passes (one focus-element: kiln wall at the common's margin — selected over open ground and bench); frugality passes (first entry for this location in this episode).
NOTES: "authority-day-configuration" in conditions is an observable scene-configuration condition (not actor-state). Sensory note is 6 words — slightly over the rubric's ≤5 word preference but not a hard violation. One focus-element named.

---

### Intent 7

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (episode-open scene-anchor for PL1–71; no prior entries; multiple subsequent beats depend on wall-position; strip test fails); interestingness passes (one focus-element: south face of the sept wall at the yard); frugality passes (no prior entry, licenses entire predawn watch sequence).
NOTES: Sensory note is 8 words — exceeds the ≤5 word preference. One focus-element is present (the south wall face) but "at the yard" is positional filler. Marginal on form but not a schema violation; ≤5 words is flagged as preference not hard rule in the rubric.

---

### Intent 8

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (state-change at remote location: one light → two lights; previous-entry test passes since inherited state has one light, not two); interestingness passes (one focus-element: the second lantern kindling, beside-ness named); frugality passes (first state-change at loc-harrenhal-exterior since PL10).
NOTES: Form clean. Sensory note is 5 words. Conditions slot records the new state (gatehouse-two-lights), not the event.

---

### Intent 9

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (gate-state changes from closed to parting; PL60 "gate opens outward" needs a prior parting state; strip test fails); interestingness passes (one focus-element: bar half-out of the brackets — mechanism, not the resulting view); frugality passes (state-change: gate-closed → gate-parting; no prior entry for this transition).
NOTES: Form clean. Sensory note is 6 words — slightly over ≤5 preference, one focus-element present. Conditions slot records gate-parting as observable state.

---

### Intent 10

VERDICT: FIRE-CORRECT
RUBRIC CHECK: Necessity passes (new sub-location: drying-yard, physical contact anchor; PL87–88 require established sub-location; strip test fails); interestingness passes (one focus-element: chamomile on the rack, selected over the rack geometry itself, and load-bearing for PL88); frugality passes (new sub-location, prior entry held lane exterior).
NOTES: Form clean. Sensory note is 4 words. Rubric correctly identifies chamomile as the more load-bearing element over rack height.

---

### Intent 11

VERDICT: NONE-CORRECT
RUBRIC CHECK: Necessity fails — PL19 is a perception-feed beat (mouse-shape perceived at Taylor's position), not a movement or positioning beat that depends on a location fact. Strip test passes: the beat resolves in inherited scene-anchor from PL1. Anti-pattern 3 (persistence-as-state): wall-seam is a location-card feature, not a state-change.
NOTES: Refusal is supported on necessity axis alone; no signature feature was missed.

---

### Intent 12

VERDICT: NONE-CORRECT
RUBRIC CHECK: Frugality fails — PL12 is a within-scene continuation beat; officer stepping to yard center does not change any environmental condition; gate-open and yard are already inherited from PL11 entry; officer's position is actor-state. Strip test passes. Anti-pattern 4 (inherited re-naming).
NOTES: Refusal is supported on frugality axis; no warranted firing signature present.

---

### Intent 13

VERDICT: NONE-CORRECT
RUBRIC CHECK: Necessity fails — PL37 is actor-positioning within an established location; the spatial arrangement of two actors narrowing the channel is actor-state, not a location-state condition. Strip test passes: the beat resolves in inherited yard state. Anti-pattern 3 (persistence-as-state: yard holds its shape, actors reposition within it).
NOTES: Refusal is supported. The "twelve feet of packed dirt" note from PL14 being already inherited is correctly cited as the ground that makes this refusal clean.

---

### Intent 14

VERDICT: NONE-CORRECT
RUBRIC CHECK: Necessity fails — PL44 is a prop-placement beat; spreading scroll across trestle does not change any location condition; trestle is already present in inherited scene-anchor (Intent 6). Strip test passes. Anti-pattern 5 (plan-bullet residue: prop movements belong in state-updates facet).
NOTES: Refusal is supported. Routing to state-updates facet is the correct downstream disposition.

---

### Intent 15

VERDICT: NONE-CORRECT
RUBRIC CHECK: Frugality fails — PL73 is within-scene navigation to an already-established fixture (the trestle). No location condition changes. Strip test passes. Anti-pattern 4 (inherited re-naming of the common for a movement within it).
NOTES: Refusal is supported on frugality axis alone.

---

### Intent 16

VERDICT: NONE-CORRECT
RUBRIC CHECK: Necessity fails — PL21 is an environmental persistence beat ("holds its three-week shape"), which is the definition of anti-pattern 3. Location-state fires on change, not on hold. Strip test passes completely.
NOTES: Refusal is supported. The beat names the absence of change; that is not a state-change entry.

---

### Intent 17

VERDICT: NONE-CORRECT
RUBRIC CHECK: Necessity fails — Taylor is sealed inside the nave; the road is not perceptible from her position; firing a loc-state entry for an exterior location outside the POV's current perception channel contradicts the necessity axis (the perceptible thing must be perceptible at the anchor beat). Anti-pattern 2 (mood-painting on stillness: "the grey holds the road" is atmospheric persistence, not a movement beat).
NOTES: Refusal is supported on necessity on two independent grounds: imperceptibility and persistence-not-change.

---

### Intent 18

VERDICT: NONE-CORRECT
RUBRIC CHECK: Necessity fails — PL67 is an auditory detection beat; the sound source location (Harrenhal gatehouse cobbles) is already established in inherited state from prior harrenhal-exterior entries. Firing a new entry here would be anti-pattern 4 (inherited re-naming). Strip test passes: the proto-line resolves against the already-established harrenhal-exterior station.
NOTES: Refusal is supported. The distinction between a new-movement anchor and an auditory event at an already-established remote location is cleanly applied.

---

## Final Block

```
TOTAL FIRE: 11 (10/1)
TOTAL NONE: 8 (8/0)
ACCEPTED ENTRIES: 10 / 19 = 53%
SYSTEMIC NOTES:
- Conditions slot contamination: Intent 5's "channel-reindexed" is interiority in the conditions field; one instance corpus-wide but a pattern to watch if fauna-control beats increase.
- Sensory note word count: Intents 7 and 9 exceed the ≤5-word preference; not hard violations but fraying at the form edge.
- NONE decisions are consistently clean: all 8 refusals apply one or more rubric axes correctly with no missed warranted firing; the refusal logic is well-calibrated.
- Draft selection is consistently correct where multiple drafts were shown: rejected drafts illustrate the right failure modes (two elements, actor-state in conditions, paraphrase-of-anchor, architectural description).
```
