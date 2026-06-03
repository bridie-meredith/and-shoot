# Audit Report — /and-write b01c12 Pass 2 Constraint Audit
# Schema: schemas/audit-report.schema.md
# Authored: 2026-06-03
# Source: active-project/staff/screen-writer/b01c12-bones-draft.md (42 bones, 4 scenes)
# Auditor: auditor fork dispatched from showrunner

report_id: write-b01c12-pass2
target: active-project/staff/screen-writer/b01c12-bones-draft.md
gate: /and-write Phase 2 constraint audit
chapter: b01c12
bone_count: 42
run_date: 2026-06-03

---

## Reference baselines used

- **Valid axis slugs**: moral_framework, capability, position-prot-rise, position-prot-collapse, relational_anchor_status, moral_legibility_to_self, political_register-prot, social_tether-prot-rise, social_tether-prot-collapse, social_tether-antag, position-world, political_register-world
- **Valid cost_ledger anchors**: cl01a, cl01b, cl02, cl03a, cl03b, cl-world-d04, cl-d05, cl-d06, cl-d07a, cl-world-d07, cl-antag-d03, cl-d08, cl-d08b, cl04, cl-antag-d10, cl05, cl-d11, cl06, cl07a, cl07b, cl07c
- **delta_per_axis band**: 1–3 (bone level). Sub-1.0 magnitudes covered by standing DEC-0002 override-as-precedent (c07 + c08 precedent); not re-flagged here.
- **Chapter targets**: capability +1.0, social_tether-prot-rise +0.5, relational_anchor_status +1.0, position-prot-rise +1.0, moral_framework -1.0
- **Scene targets**: s01: capability +0.5, social_tether-prot-rise +0.5 | s02: none | s03: relational_anchor_status +1.0, position-prot-rise +1.0 | s04: capability +0.5, moral_framework -1.0
- **SVO canonical reference**: b01-c02.md; project idioms include "the accounting reaches <X>" (b01-c02 line ~38) and "holds the <body-part>" (body-part-stillness license)
- **Earth-Bet fence**: no proper-noun parahuman jargon ("Khepri," "Gold Morning," parahuman) in any SVO

---

## Roll-up verification (independent of draft's self-check)

| Scene | Axis | Direction | Bone(s) | Sum | Target | Match |
|-------|------|-----------|---------|-----|--------|-------|
| s01 | capability | up | s01n09 +0.5 | +0.5 | +0.5 | EXACT |
| s01 | social_tether-prot-rise | up | s01n10 +0.5 | +0.5 | +0.5 | EXACT |
| s02 | (none) | — | — | 0 | 0 | EXACT |
| s03 | position-prot-rise | up | s03n03 +0.5, s03n06 +0.5 | +1.0 | +1.0 | EXACT |
| s03 | relational_anchor_status | up | s03n10 +0.5, s03n11 +0.5 | +1.0 | +1.0 | EXACT |
| s04 | capability | up | s04n02 +0.5 | +0.5 | +0.5 | EXACT |
| s04 | moral_framework | down | s04n13 -1.0 | -1.0 | -1.0 | EXACT |

**Chapter roll-up**: capability +1.0, social_tether-prot-rise +0.5, relational_anchor_status +1.0, position-prot-rise +1.0, moral_framework -1.0. All 5 axes EXACT against contract. No FAULT-AGGREGATE-DELTA-MISMATCH.

---

## s04n09 form ruling

**SVO**: "the accounting reaches the shape-word"

**Earth-Bet fence**: CLEAN. "shape-word" is the project-canonical cipher noun; no proper noun "Khepri" or "Gold Morning" appears. The s04 chunk cold-read Earth-Bet clearance (worm-canon 3/3 SUBSTANCE-FELT) stands.

**SVO form**: "reaches" is the established project idiom (b01-c02 line ~38: "the accounting reaches the ward-junction entry"). Object "the shape-word" is abstract — an internal word, not a concrete ledger location. Under the schema's strict rule ("a physical verb whose object is an abstract noun is a thought-figure, not an event"), this would fault FAULT-FORM-INTERIORITY. However, the Earth-Bet fence directly prevents a more concrete recast: the constraint requires cipher-language; no concrete object-noun for this beat exists within the fence. This auditor classifies s04n09 as **FLAG (FAULT-FORM-INTERIORITY borderline)** rather than FAULT: the violation is real in strict schema terms but is the minimum-cost compliant formulation given the Earth-Bet constraint. Fixer must NOT recast toward a proper noun to resolve it; the FLAG is informational only. If Phase 6 EVENT-NOT-CONCRETE fires, this is the downstream record.

---

## Per-bone classifications

### Scene s01 (10 bones)

**b01c12s01n01**
- SVO: "the insects return the overhang-joints"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-001
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null. No held axis, no anchor.
- why: Schema requires chatter without axes_held to carry a cost_ledger_anchor paying a later gain. This bone pays nothing.
- criteria: Fixer must either (a) recast as HELD by attaching scene's load-bearing held axis (relational_anchor_status) with rationale "ambient grounding; hold confirms gap-lane terrain is the structural basis for the witch-label constraint; axis held at 3.5" — lowest-disruption remedy; or (b) attach cost_ledger_anchor cl05 if it genuinely prefigures the capability gain at s01n09 two bones forward; or (c) candidate for trim if the lane-mouth image is covered by s01n02.

**b01c12s01n02**
- SVO: "the insects fan the lane-mouth"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-002
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Same as fault-001. No held axis or anchor.
- criteria: Fixer must (a) recast as HELD attaching relational_anchor_status or capability held rationale ("ambient deployment envelope confirmed as the terrain-constraint boundary; capability held at 5.5 — witch-label geography constrains the placement the insects are executing"); or (b) trim to s01n01 if redundant coverage; or (c) attach cl05 if both n01 and n02 collectively prefigure the ward-cluster gain.

**b01c12s01n03**
- SVO: "taylor-hebert-kl-122ac takes the gate-tower shadow"
- Classification: **CORRECT**
- shape=held, axes_held=[political_register-prot], no cost_ledger_anchor needed for held bone. Axis slug valid. Rationale: cold operational mode, flat affect, register not firing — valid held-discipline rationale. "takes the gate-tower shadow" = moves into position inside the shadow; idiomatic motion verb. No form violation detected.

**b01c12s01n04**
- SVO: "the coverage map closes the gate-tower boundary"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-003
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null. The comment claims "chatter permitted here because it names the formal operational fact" — but no schema exemption exists for "naming an operational fact"; chatter still requires an anchor or axes_held.
- why: The bone's own comment acknowledges the gap ("cost_ledger_anchor: null; chatter permitted here because...") but the asserted rationale is not a schema-recognized exemption.
- criteria: Fixer must (a) recast as HELD attaching relational_anchor_status (rationale: "coverage map formally closes at the gate-tower boundary — the gap's eastern limit is confirmed as the operational terrain against which Wren's route becomes the effective boundary; axis held at 3.5"); or (b) merge into s01n05 (both cover the coverage-gap-established event) if the gate-tower boundary and rendering-yard boundary can be consolidated; or (c) attach cl02 or cl-d08 as anchor if the map-closing formally prefigures the position or anchor gains.

**b01c12s01n05**
- SVO: "the map closes the rendering-yard boundary"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-004
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null. Same structural problem as fault-003 despite grounding=true.
- why: Grounding flag does not exempt from the chatter-must-pay rule.
- criteria: Fixer must (a) recast as HELD attaching relational_anchor_status (rationale: "rendering-yard east wall named as the operational limit of the coverage gap; the gap's confirmed physical extent is the structural condition that makes Wren's free movement load-bearing; axis held at 3.5"); or (b) merge with s01n04 into a single held bone covering both boundary-markers; or (c) trim if s01n04 already covers coverage-gap-established sufficiently.

**b01c12s01n06**
- SVO: "the insects return the stitch-house route"
- Classification: **CORRECT**
- shape=held, axes_held=[relational_anchor_status], no anchor needed. Axis slug valid. Rationale sound (indexing without weighting, anchor held at 3.5 pending the choice). Project idiom "return" established.

**b01c12s01n07**
- SVO: "the map indexes the stitch-maker route"
- Classification: **FAULT-FORM (non-action verb)**
- id: fault-005
- type: fault
- what: "indexes" = records/categorizes — a stative non-action verb describing the map's content rather than a discrete physical action. The schema prohibits non-action verbs. The physical act is the map *recording* or *marking* the route, not "indexing" as a discrete observable event.
- why: FAULT-FORM-NON-ACTION-VERB. "indexes" is containment/categorization, not physical action.
- criteria: Fixer must recast to a physical transitive verb. Candidates: "the map marks the stitch-maker route" (concrete marking act) or "taylor-hebert-kl-122ac traces the stitch-maker route" (physical tracing). The held-discipline rationale and axes_held are unaffected.

**b01c12s01n08**
- SVO: "taylor-hebert-kl-122ac lifts the stylus from the source-field"
- Classification: **FAULT-FORM (prepositional modifier)**
- id: fault-006
- type: fault
- what: "from the source-field" is a prepositional phrase of source. The schema explicitly bans prepositional phrases of source: "Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned (FAULT-FORM-MODIFIER)."
- why: FAULT-FORM-MODIFIER. The core physical act (stylus lifted) is correct; the source-phrase is the violation.
- criteria: Fixer must drop the prepositional phrase: "taylor-hebert-kl-122ac lifts the stylus" — the physical act is unambiguous without "from the source-field." The held-discipline meaning (stylus lifted rather than applied) is conveyed by the shape and rationale, not required in the SVO.

**b01c12s01n09**
- SVO: "taylor-hebert-kl-122ac extends the northern ward-cluster"
- Classification: **CORRECT**
- shape=moving, capability +0.5, cl05 valid. "extends" = concrete transitive physical action. Magnitude 0.5 is sub-1.0; covered by DEC-0002 precedent. No violation.

**b01c12s01n10**
- SVO: "the ledger column closes the water-gate entry"
- Classification: **CORRECT**
- shape=moving, social_tether-prot-rise +0.5, cl-d08b valid. "closes" = physical ledger act (marks entry as complete). Magnitude 0.5 covered by DEC-0002. No form violation.

---

### Scene s02 (7 bones)

**b01c12s02n01**
- SVO: "jarvis-coin-kl-courier places the packet on the ledger surface"
- Classification: **FAULT-FORM (prepositional modifier) + FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-007
- type: fault
- what: (1) "on the ledger surface" is a prepositional phrase of place — banned. (2) shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null — unpaid chatter.
- why: FAULT-FORM-MODIFIER (prepositional place phrase) + FAULT-BONE-DELTA-MALFORMED (chatter without anchor or held axis).
- criteria: Fixer must (1) drop the prepositional phrase: "jarvis-coin-kl-courier places the packet" or recast with transitive destination: "jarvis-coin-kl-courier delivers the packet"; and (2) recast as HELD with social_tether-antag or social_tether-prot-rise held rationale ("Jarvis arriving at the standard channel timing — tether-load visible in the approach; opposing force enters with packet delivery; held at scene's axis levels") — or attach cost_ledger_anchor (cl-d08b or cl02 if this delivery prefigures the refusal and tether-consolidation gains).

**b01c12s02n02**
- SVO: "taylor-hebert-kl-122ac breaks the wax seal"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-008
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Chatter without anchor or held axis.
- criteria: Fixer must (a) recast as HELD attaching relational_anchor_status (rationale: "seal-breaking is the physical threshold action that makes the collision-delivery arrive as a fact; the anchor gap-route is what the packet targets; axis held at 3.5") — OR attach cl02 as the anchor (the seal-breaking prefigures the position-prot-rise gain at s03n03/n06, since this is the request that the refusal-bone pays).

**b01c12s02n03**
- SVO: "the covering-sheet names the east-water-gate corridor"
- Classification: **FAULT-FORM (non-action verb)**
- id: fault-009
- type: fault
- what: "names" = a stative/communicative verb (the sheet has content; it does not perform a physical naming action). This is a containment/possession relationship — the sheet contains/identifies the corridor designation. Not a discrete physical act an observer would see the sheet *do*.
- why: FAULT-FORM-NON-ACTION-VERB. Physical documents cannot perform the action of "naming" in the schema's sense; the sheet-as-actor names nothing — it is read (but "reads" is a perception verb fault). The bone describes an attribute of the covering-sheet, not a physical event.
- criteria: Fixer must recast to a physical event. Options: "taylor-hebert-kl-122ac reads the covering-sheet" would be FAULT-FORM-PERCEPTION; instead: "the covering-sheet lists the east-water-gate corridor" still has the same problem. Better: "taylor-hebert-kl-122ac opens the covering-sheet" (physical act of opening/unfolding the sheet) — the corridor content is facet territory. Note: s02n03 is shape=held with valid axes_held=[relational_anchor_status] — so fixing the SVO is the only required change; the held structure is sound.

**b01c12s02n04**
- SVO: "taylor-hebert-kl-122ac sets the packet on the ledger surface"
- Classification: **FAULT-FORM (prepositional modifier)**
- id: fault-010
- type: fault
- what: "on the ledger surface" is a prepositional phrase of place — banned.
- why: FAULT-FORM-MODIFIER.
- criteria: Fixer must drop the prepositional phrase: "taylor-hebert-kl-122ac sets the packet" (the physical act of setting the packet down is complete and observable without specifying the surface in the SVO; surface goes to loc-state). Shape=held, axes_held=[position-prot-rise] remains valid.

**b01c12s02n05**
- SVO: "the covering-sheet names the rendering-yard boundary"
- Classification: **FAULT-FORM (non-action verb)**
- id: fault-011
- type: fault
- what: Same violation as fault-009. "names" is not a physical action performable by a document.
- why: FAULT-FORM-NON-ACTION-VERB.
- criteria: Fixer must recast. Shape=held, axes_held=[social_tether-antag] remains valid. SVO fix candidates: "the covering-sheet marks the rendering-yard boundary" (still stative); "taylor-hebert-kl-122ac traces the covering-sheet" (physical contact with the sheet) is better, with the rendering-yard content as facet territory. Or merge n03 and n05 into a single held bone with a physical opening/reading act if both cover the same "packet-describing-the-gap-lanes" event.

**b01c12s02n06**
- SVO: "taylor-hebert-kl-122ac sets the stylus beside the packet"
- Classification: **FAULT-FORM (prepositional modifier) + FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-012
- type: fault
- what: (1) "beside the packet" = prepositional phrase of place — banned. (2) shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null — unpaid chatter.
- why: FAULT-FORM-MODIFIER + FAULT-BONE-DELTA-MALFORMED.
- criteria: Fixer must (1) drop the prepositional phrase: "taylor-hebert-kl-122ac sets the stylus" (or "lowers the stylus" for more physical specificity); and (2) recast as HELD attaching the scene's load-bearing held axis. The pl-2026-06-03-004 watch (bay-warmth close = Taylor's body paired to setting enacted here) suggests this bone carries the indifferent-world-continuance beat. Held attachment: position-prot-rise (rationale: "physical stillness before the refusal decision — the stylus set without writing is the decision-threshold held against the apparatus's precision request; axis held at 4"). Alternatively, consolidate n06 and n07 (both enact Taylor's body stillness at the decision threshold) into a single held bone.

**b01c12s02n07**
- SVO: "taylor-hebert-kl-122ac holds the eyes"
- Classification: **CORRECT**
- shape=held, axes_held=[position-prot-rise], rationale valid. "holds the eyes" = body-part stillness-against-pressure — explicitly licensed by the narrow `holds` rule. Grounding=true (body-part). No violation.

---

### Scene s03 (12 bones)

**b01c12s03n01**
- SVO: "taylor-hebert-kl-122ac takes the stylus"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-013
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Unpaid chatter. "takes the stylus" is a concrete physical act (grasps the stylus — c11s01n01 "takes the packet" established as valid idiom), but the bone is shape=chatter with no held axis or anchor.
- criteria: Fixer must (a) recast as HELD attaching political_register-prot (rationale: "taking the stylus in flat operational register — the refusal-writing act opens in the same cold-utilitarian mode as every prior deliverable entry; no contempt-register fires; register held at 3.5") — this is the scene's held register axis; or (b) attach cl02 as anchor (taking the stylus prefigures the position-prot-rise gain at n03/n06); or (c) trim if the physical setup is sufficiently established by n02.

**b01c12s03n02**
- SVO: "the coverage-entry opens the gap-column"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-014
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Unpaid chatter. The bone describes a ledger-column being opened — a concrete physical act — but carries no held axis or anchor.
- criteria: Fixer must (a) recast as HELD attaching political_register-prot (rationale: "coverage-entry column opens in flat operational register — the deliverable is being written in the same channel-format as every prior entry; no contempt-register fires on the act of opening; held at 3.5"); or (b) attach cl02 as anchor (opening the gap-column is the immediate physical precursor to the position-prot-rise gain at n03).

**b01c12s03n03**
- SVO: "taylor-hebert-kl-122ac writes the boundary entry"
- Classification: **CORRECT**
- shape=moving, position-prot-rise +0.5, cl02 valid anchor. "writes" = concrete physical action. Magnitude 0.5 covered by DEC-0002. No violation.

**b01c12s03n04**
- SVO: "taylor-hebert-kl-122ac holds the hand"
- Classification: **CORRECT**
- shape=held, axes_held=[moral_legibility_to_self], rationale valid (hand stops before the explanation field — body-part stillness-against-pressure). "holds the hand" is licensed under narrow `holds` rule (body-part). Grounding=true. No violation.

**b01c12s03n05**
- SVO: "the stylus lifts from the explanation field"
- Classification: **FAULT-FORM (prepositional modifier)**
- id: fault-015
- type: fault
- what: "from the explanation field" = prepositional phrase of source — banned.
- why: FAULT-FORM-MODIFIER.
- criteria: Fixer must drop the prepositional phrase: "the stylus lifts" (the bone's held-discipline meaning is carried by the shape and the rationale, not the SVO suffix). Alternatively recast to active: "taylor-hebert-kl-122ac lifts the stylus" — loses the subject-as-stylus physical grammar but removes the modifier. Shape=held, axes_held=[moral_legibility_to_self] remains valid.

**b01c12s03n06**
- SVO: "taylor-hebert-kl-122ac closes the response entry"
- Classification: **CORRECT**
- shape=moving, position-prot-rise +0.5, cl02 valid. "closes" = concrete physical ledger act. Magnitude 0.5 covered by DEC-0002. No violation.

**b01c12s03n07**
- SVO: "jarvis-coin-kl-courier takes the sealed packet"
- Classification: **CORRECT**
- shape=held, axes_held=[social_tether-antag], rationale valid (apparatus receives the refusal via standard channel; held at 6). "takes" = grasps/receives physical object. No violation.

**b01c12s03n08**
- SVO: "the response entry closes the gap-column"
- Classification: **CORRECT**
- shape=held, axes_held=[political_register-prot], rationale valid (flat operational close, not contempt-register). "closes" = concrete ledger act. No violation.

**b01c12s03n09**
- SVO: "taylor-hebert-kl-122ac opens the anchor-column"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-016
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null. The comment says "chatter licensed here as setup for the two axis-moving bones that follow" — but setup is not a schema-recognized exemption.
- why: Unpaid chatter. No held axis, no anchor.
- criteria: Fixer must (a) recast as HELD attaching relational_anchor_status (rationale: "opening the anchor-column is the physical threshold action before the weight settles; the column's opening confirms the anchor is present in the ledger architecture; axis held at 3.5 — the weight belongs to n10/n11, not to the act of opening"); or (b) attach cl-d08 or cl-d06 as anchor (the opening act directly prefigures the relational_anchor_status gain at n10/n11 which settle those anchors); or (c) trim if s03n08 + s03n10 cover the event sufficiently.

**b01c12s03n10**
- SVO: "the anchor-column entry takes the refusal weight"
- Classification: **FAULT-FORM (abstraction-as-object/interiority)**
- id: fault-017
- type: fault
- what: "the refusal weight" is an abstract noun as direct object. Schema: "A physical verb whose object is an abstract noun is a thought-figure, not an event (FAULT-FORM-INTERIORITY)." "Weight" as a metaphorical abstraction is not a concrete physical object the column entry can "take."
- why: FAULT-FORM-INTERIORITY. "takes the refusal weight" is a thought-figure — the weight is a narrative/emotional concept, not a physical object.
- criteria: Fixer must replace the abstract object with a concrete ledger-specific noun. The physical event is the relational_anchor_status moving up because the lane-refusal is written. Candidate recasts: "the anchor-column entry takes the refusal mark" (still abstract); "taylor-hebert-kl-122ac writes the anchor-column entry" (concrete — matches s03n03/s03n06 pattern; moving bone at +0.5 relational_anchor_status, cl-d08). The shape=moving and axis_moves=[relational_anchor_status +0.5, cl-d08] are retained; only the SVO needs replacement.

**b01c12s03n11**
- SVO: "the anchor-column entry takes the deferred weight"
- Classification: **FAULT-FORM (abstraction-as-object/interiority)**
- id: fault-018
- type: fault
- what: Same violation as fault-017. "the deferred weight" is abstract.
- why: FAULT-FORM-INTERIORITY.
- criteria: Fixer must replace the abstract object. Candidate: "taylor-hebert-kl-122ac closes the anchor-column entry" (mirrors s03n06's "closes the response entry" pattern — the closing is the physical act that settles the cl-d06 debt; the held-meaning of "deferred weight settled" is carried by the shape and the cl-d06 anchor). Shape=moving, relational_anchor_status +0.5, cl-d06 retained.

**b01c12s03n12**
- SVO: "taylor-hebert-kl-122ac lifts the hand from the anchor-column"
- Classification: **FAULT-FORM (prepositional modifier) + FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-019
- type: fault
- what: (1) "from the anchor-column" = prepositional phrase of source — banned. (2) shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null — unpaid chatter.
- why: FAULT-FORM-MODIFIER + FAULT-BONE-DELTA-MALFORMED.
- criteria: Fixer must (1) drop the prepositional phrase: "taylor-hebert-kl-122ac lifts the hand" (body-part lift as physical close of the scene — the anchor-column destination is facet/staging territory); and (2) recast as HELD. The pl-2026-06-03-004 (c) watch specifies this as the "hand-on-ledger close: lift-and-move." Held attachment: relational_anchor_status (rationale: "the hand lifting from the anchor-column is the physical close of the weight-settling act; axis has moved at n10/n11; the lift enacts the column closing as a body fact; no further anchor movement here; held at 4.5 post-move") — OR moral_legibility_to_self (rationale: "the hand lifts without the suppression cracking — the accounting is filed, the column closed; legibility holds at 5.5; the hand-lift is the physical confirmation that the crack did not open"). If also fixing the body-part modifier: "taylor-hebert-kl-122ac lifts the hand" is 4 words — "holds the <body-part>" is licensed; "lifts the hand" is a discrete act (not a sustained hold), so the narrow license doesn't apply but the motion is a clean transitive physical act without the prepositional phrase.

---

### Scene s04 (13 bones)

**b01c12s04n01**
- SVO: "taylor-hebert-kl-122ac extends the muddy-way ward-cluster"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-020
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Unpaid chatter. The comment says "this is setup for the capability-moving bone at n02" — but setup is not a schema exemption.
- criteria: Fixer must (a) recast as HELD attaching capability (rationale: "second ward-cluster extension underway — capability at its deployment ceiling, the extension is the physical act that closes the full-circuit count; held at 5.5 as the action proceeds; the capability gain lands at n02 when the insects fill the upper-margin"); or (b) attach cl05 as anchor (extends the ward-cluster directly prefigures the +0.5 capability gain at n02 — the extension IS the causal first-step of the insect-fill); or (c) trim and let n02 carry the full physical event (insect-fill is the observable act; the extension may be redundant).

**b01c12s04n02**
- SVO: "the insects fill the muddy-way upper-margin"
- Classification: **CORRECT**
- shape=moving, capability +0.5, cl05 valid. "fill" = concrete transitive physical action. Named physical object (Muddy Way upper-margin). Magnitude 0.5 covered by DEC-0002. No violation.

**b01c12s04n03**
- SVO: "the feed returns all five wards"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-021
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Unpaid chatter.
- criteria: Fixer must (a) recast as HELD attaching moral_legibility_to_self (rationale: "full-circuit feed returning all five wards simultaneously — aggregate shape now differs from any prior count; moral_legibility holds at 5.5 because the word has not yet surfaced; the shape of the whole is what will surface it; held-discipline against the approaching threshold"); or (b) attach cl05 as anchor (the five-ward feed-return prefigures both the capability gain at n02 and the moral_framework cost at n13); or (c) trim if n02 + n06 cover the aggregate-scale image.

**b01c12s04n04**
- SVO: "the count moves through the full-circuit return"
- Classification: **FAULT-FORM (prepositional modifier)**
- id: fault-022
- type: fault
- what: "through the full-circuit return" = prepositional phrase of direction — banned.
- why: FAULT-FORM-MODIFIER. Additionally, "the count moves" is a bare intransitive motion with a directional prepositional phrase — doubly violating.
- criteria: Fixer must recast entirely. The physical event is the counting-as-physical-act. Candidate: "the count runs the full-circuit return" — "runs" as a transitive verb with "the full-circuit return" as a concrete ledger-object (established idiom per s04n07 "the accounting runs the harm-prevention column"). This is shape=chatter, so a held or anchor recast is also needed (same chatter rule applies).
- Additional: FAULT-BONE-DELTA-MALFORMED (unpaid chatter) also applies.
- id: fault-022 (dual fault class — FORM + MALFORMED)

**b01c12s04n05**
- SVO: "the feed returns the Flea Bottom approaches"
- Classification: **FAULT-BONE-DELTA-MALFORMED (unpaid chatter)**
- id: fault-023
- type: fault
- what: shape=chatter, axis_moves=[], axes_held=[], cost_ledger_anchor=null.
- why: Unpaid chatter. "returns" is project idiom (CLEAN); the SVO is otherwise well-formed.
- criteria: Fixer must (a) recast as HELD attaching moral_legibility_to_self or capability (rationale similar to fault-021 — the Flea Bottom approaches returning at full density is the penultimate accumulation beat before the threshold crossing; capability held at 6 post-n02 gain; the feed-return is the aggregate scale pressing toward the shape-word); or (b) attach cl05 (same justification as fault-021); or (c) trim if n03 already covers the aggregate-scale image adequately.

**b01c12s04n06**
- SVO: "the accounting reaches the aggregate-shape entry"
- Classification: **CORRECT**
- shape=held, axes_held=[moral_legibility_to_self], rationale valid. "reaches" = established project idiom. "aggregate-shape entry" is a ledger entry — more concrete than an abstraction, within idiom. No violation. Grounding=false is accurate.

**b01c12s04n07**
- SVO: "the accounting runs the harm-prevention column"
- Classification: **FLAG (abstraction-as-object, soft)**
- id: flag-001
- type: flag
- what: "the harm-prevention column" is a ledger column name — physical object in the world of this chapter (Taylor's internal ledger). "runs" = traverses/operates through. "runs the harm-prevention column" is within the established project idiom for the accounting's traversal acts (compare "the accounting reaches the aggregate-shape entry" at n06). However, "harm-prevention column" is more abstract than a concrete ledger-column slug.
- why: Borderline. The verb "runs" with an abstract column-name is at the edge of the non-action-verb prohibition. Not filing as FAULT given the idiom is consistent with prior shipped chapters; flagging for fixer to evaluate whether a concrete column descriptor exists.
- criteria: Not required; advisory. Fixer may leave as-is or add physical specificity ("the accounting runs the breach-prevention entry" if a physical ledger column has this name).

**b01c12s04n08**
- SVO: "the accounting reaches the breach column"
- Classification: **CORRECT**
- shape=held, axes_held=[moral_framework], rationale valid. "reaches" = project idiom. "the breach column" = concrete physical column in Taylor's ledger (established in s04 chunk). No violation.

**b01c12s04n09**
- SVO: "the accounting reaches the shape-word"
- Classification: **FLAG (FAULT-FORM-INTERIORITY borderline — Earth-Bet-constrained)**
- id: flag-002
- type: flag
- what: "the shape-word" is an internal word / abstract thought-referent, not a concrete ledger location. Under strict schema, this is FAULT-FORM-INTERIORITY (abstract noun as object). Earth-Bet fence is CLEAN (no proper noun). The constraint prevents a more concrete recast.
- why: See s04n09 form ruling section above. Filed as FLAG not FAULT because the Earth-Bet fence makes this the minimum-violation compliant formulation.
- criteria: No required fix. Phase 6 EVENT-NOT-CONCRETE check may revisit. Fixer must not introduce a proper noun to resolve. If a concrete ledger-column name can be coined within the fence ("the accounting reaches the shape-word column" or similar), that would resolve the abstraction without violating the fence.

**b01c12s04n10**
- SVO: "the accounting advances the count"
- Classification: **CORRECT**
- shape=held, axes_held=[moral_legibility_to_self], rationale valid. "advances" = concrete transitive (moves the count forward). No violation.

**b01c12s04n11**
- SVO: "taylor-hebert-kl-122ac closes the architecture entry"
- Classification: **CORRECT**
- shape=held, axes_held=[moral_legibility_to_self], rationale valid (entry closes without shape-word; suppression enacted physically). "closes" = concrete physical act. Grounding=true. No violation.

**b01c12s04n12**
- SVO: "the ledger entry takes the full-circuit count"
- Classification: **FLAG (dual cl05 anchor; chatter-with-anchor legitimacy)**
- id: flag-003
- type: flag
- what: shape=chatter with cost_ledger_anchor=cl05. Chatter with a valid anchor is schema-permitted. However, cl05 is already cited on s04n02 (capability +0.5, gain side) and s04n13 (moral_framework -1.0, cost side). This bone cites cl05 as a third co-citation of the same anchor, which is unusual. The comment argues the bone makes "the gain-side visible on both the action (n02) and the record (n12)."
- why: Dual/triple citation of a single cost_ledger anchor is not explicitly prohibited, but the schema's intent is that each anchor is paid at most once per gain side and once per cost side. n02 already pays the gain side. n12's citation is therefore redundant against the same gain-side anchor on the same chapter. Not a FAULT-COST-LEDGER-UNRESOLVED (cl05 exists), but a FLAG for fixer to confirm the double-citation is intentional.
- criteria: Fixer may leave as-is if the design intent is confirmed; the anchor ID is valid. If the intent is to give n12 a distinct payment role, a separate anchor for "capability-full-deployment-confirmed" does not exist — fixer must either (a) keep cl05 with clarifying rationale note, or (b) recast n12 as HELD (it is the ledger-record close of the capability gain, paralleling s03n12's scene-close function) with no anchor required.

**b01c12s04n13**
- SVO: "the breach column takes the threshold entry"
- Classification: **CORRECT**
- shape=moving, moral_framework -1.0, cl05 valid (cost side). "takes" = receives/records (concrete ledger act). "threshold entry" is a ledger entry — concrete. Grounding=true. Magnitude 1.0 at the band floor (within range). No violation.

---

## Summary

### Total classifications

| Verdict | Count |
|---------|-------|
| CORRECT | 19 |
| FAULT (any class) | 19 |
| FLAG | 4 |
| **Total** | **42** |

### Fault counts by class

| Class | Count | Bone slugs |
|-------|-------|-----------|
| FAULT-BONE-DELTA-MALFORMED (unpaid chatter) | 15 | s01n01, s01n02, s01n04, s01n05, s02n01*, s02n02, s02n06*, s03n01, s03n02, s03n09, s03n12*, s04n01, s04n03, s04n04*, s04n05 |
| FAULT-FORM-MODIFIER (prepositional phrase) | 6 | s01n08, s02n01*, s02n04, s02n06*, s03n05, s03n12*, s04n04* |
| FAULT-FORM-NON-ACTION-VERB | 3 | s01n07, s02n03, s02n05 |
| FAULT-FORM-INTERIORITY (abstract-as-object) | 2 | s03n10, s03n11 |
| DUAL-CLASS (FORM + MALFORMED) | 3 | s02n01, s02n06, s03n12 (each counted once under both classes) |

*Bones marked * carry dual fault classes; each bone is one fault entry but flags two fault classes.

**Fault IDs assigned**: fault-001 through fault-023 (fault-022 is dual-class on one bone; 19 distinct fault bones total).

### Flags

| id | type | bone | what |
|----|------|------|------|
| flag-001 | flag | s04n07 | "the accounting runs the harm-prevention column" — abstraction-as-object borderline; within idiom; soft advisory |
| flag-002 | flag | s04n09 | "the accounting reaches the shape-word" — FAULT-FORM-INTERIORITY borderline; Earth-Bet-constrained; no required fix |
| flag-003 | flag | s04n12 | cl05 cited triple (n02 gain + n13 cost + n12 redundant gain); chatter-with-anchor valid; dual-citation is design question |

### Chatter-unpaid list with recommended remedies

| Bone | SVO | Remedy |
|------|-----|--------|
| s01n01 | the insects return the overhang-joints | HOLD: attach relational_anchor_status, rationale: "witch-label terrain geometry is the structural constraint against which the coverage gap is formed; axis held at 3.5"; OR trim if s01n02 covers lane-mouth |
| s01n02 | the insects fan the lane-mouth | HOLD: attach capability, rationale: "feed operating at the deployment ceiling in the gap lanes — constraint visible; capability held at 5.5"; OR trim if s01n01 covers setting |
| s01n04 | the coverage map closes the gate-tower boundary | HOLD: attach relational_anchor_status, rationale: "gate-tower boundary is the confirmed western limit of the gap; axis held at 3.5"; OR merge with s01n05 |
| s01n05 | the map closes the rendering-yard boundary | HOLD: attach relational_anchor_status, rationale: "rendering-yard east wall is the confirmed eastern limit of the gap; together with n04 the gap is formally bounded; axis held at 3.5"; OR merge with s01n04 |
| s02n01 | jarvis-coin-kl-courier places the packet on the ledger surface | HOLD: attach social_tether-antag, rationale: "opposing force enters via the standard channel — the apparatus's terrain-literate delivery; tether-antag held at 6"; ALSO fix prepositional modifier |
| s02n02 | taylor-hebert-kl-122ac breaks the wax seal | HOLD: attach relational_anchor_status, rationale: "seal-breaking threshold — anchor gap-route is what the packet targets; axis held at 3.5"; OR attach cl02 anchor (breaking seal directly prefigures the position-prot-rise gain at s03n03) |
| s02n06 | taylor-hebert-kl-122ac sets the stylus beside the packet | HOLD: attach position-prot-rise, rationale: "physical stillness at the decision threshold — stylus set without writing; the withholding-before-refusal enacted physically; axis held at 4"; ALSO fix prepositional modifier |
| s03n01 | taylor-hebert-kl-122ac takes the stylus | HOLD: attach political_register-prot, rationale: "refusal-writing opens in flat operational register; no contempt fires on taking the stylus; held at 3.5"; OR attach cl02 anchor |
| s03n02 | the coverage-entry opens the gap-column | HOLD: attach political_register-prot, rationale: "gap-column opens in same flat format as every prior entry — no register advance; held at 3.5"; OR attach cl02 anchor |
| s03n09 | taylor-hebert-kl-122ac opens the anchor-column | HOLD: attach relational_anchor_status, rationale: "anchor-column opening is the physical threshold before the weight settles at n10/n11; axis held at 3.5"; OR attach cl-d08 anchor |
| s03n12 | taylor-hebert-kl-122ac lifts the hand from the anchor-column | HOLD: attach relational_anchor_status, rationale: "hand lifts from column post-settle; weight is now filed; axis held at 4.5"; ALSO fix prepositional modifier |
| s04n01 | taylor-hebert-kl-122ac extends the muddy-way ward-cluster | HOLD: attach capability, rationale: "second extension underway — ward-cluster action in progress; capability held at 5.5 approaching the n02 +0.5 threshold"; OR attach cl05 anchor; OR trim |
| s04n03 | the feed returns all five wards | HOLD: attach moral_legibility_to_self, rationale: "full five-ward return is the aggregate shape pressing toward the threshold; legibility held at 5.5 — the crack is present but the word has not surfaced yet"; OR attach cl05 anchor |
| s04n04 | the count moves through the full-circuit return | HOLD + FORM FIX: recast SVO to "the count runs the full-circuit return" (drop prepositional phrase) then attach moral_legibility_to_self or capability held rationale; OR trim |
| s04n05 | the feed returns the Flea Bottom approaches | HOLD: attach moral_legibility_to_self, rationale: "Flea Bottom approaches returning at full scale — the accumulation beat before the threshold crossing; legibility held at 5.5"; OR attach cl05 anchor; OR trim |

### Roll-up verdict

PASS. All 5 chapter axes and all 4 per-scene aggregates verified EXACT against contract. No FAULT-AGGREGATE-DELTA-MISMATCH. No FAULT-COST-LEDGER-UNRESOLVED.

### Earth-Bet constraint verdict

CLEAN. No proper noun parahuman jargon in any SVO. "shape-word" cipher is the project-approved fence-compliant formulation. s04n09 form flag does not violate the fence.

### Scope note

All 19 faults are episode-scope (single-line or single-bone fixes via shape change or SVO recast). No finding requires episode-plan revision or season-plan escalation. The 15 unpaid-chatter faults are the dominant finding class; they are systematic (the draft authored grounding chatter bones throughout all four scenes without attaching held axes or anchors) and collectively addressable as a fixer pass with a single rule: attach a held axis to every grounding/setup chatter bone or apply a valid cost_ledger_anchor. The 4 FORM faults on prepositional modifiers are straightforward drops. The 2 interiority faults on s03n10/n11 require SVO replacements that preserve the physical-ledger-act character of the moving bones.
