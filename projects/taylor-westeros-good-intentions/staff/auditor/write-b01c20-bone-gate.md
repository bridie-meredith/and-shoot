# /and-write Phase 6 — SUBSTANCE BONE-GATE AUDIT
# chapter: b01c20
# chapter_class: standard (NOT frame-coda; gate runs fully)
# authored: 2026-06-05
# auditor: auditor

---

## Source materials read
- `active-project/staff/screen-writer/b01c20-bones-draft.md` (30 bones / 5 scenes)
- `active-project/staff/showrunner/memory.md` — chapters[b01c20].scenes[] contracts + substance_delta
- `active-project/staff/showrunner/memory.md` — series.substance.state_axes[]; cost_ledger (cl07a/cl07b/cl07c); chunk_targets

---

## Chapter-level contract summary (from memory.md)

| Scene | stakes_axis | axes_in_motion | target_delta |
|-------|------------|----------------|-------------|
| s01 | position-world | position-world +0.5, political_register-world +0.5, moral_legibility_to_self +0.2 | tied top: pos-world/pol-reg-world +0.5 each |
| s02 | social_tether-prot-collapse | social_tether-prot-collapse −1.0, moral_legibility_to_self +0.2, position-prot-collapse −0.7 | dominant: soc-tether-prot-collapse −1.0 |
| s03 | social_tether-prot-collapse | social_tether-prot-collapse −1.5, position-prot-collapse −1.0, position-world +0.3, political_register-world +0.2 | dominant: soc-tether-prot-collapse −1.5 |
| s04 | relational_anchor_status | relational_anchor_status +1.5, moral_legibility_to_self +0.5 | dominant: relational_anchor_status +1.5 |
| s05 | position-prot-collapse | position-prot-collapse −1.3, social_tether-prot-collapse −1.0, moral_legibility_to_self +0.1, position-world +0.2, political_register-world +0.3 | dominant: position-prot-collapse −1.3 |

Cost-ledger anchors active this chapter:
- cl07a: moral_legibility_to_self +4 / social_tether-prot-collapse −7
- cl07b: position-world +2 / position-prot-collapse −6
- cl07c: political_register-world +2 / relational_anchor_status (opportunity-missed → rank 9 LOCKED)

---

## PER-BONE AUDIT

### SCENE 1 (b01c20s01) — 5 bones

**b01c20s01n01** `"the servant-passages empty"`
- Type: MOVING bone. axis_moves: position-world up/1, cost_ledger_anchor: cl07b.
- Bonefide check: servant-passage traffic ceasing IS the physical enactment of Viserys's death arriving in the apparatus before any bell. The SVO physically causes position-world to move: the succession-machine's first physical event (a high-value node, the Red Keep passage network, goes silent) is a Green-faction consolidation indicator. Cause-to-rank-claim visible. BONEFIDE: PASS.
- Grounding: true. Concrete place-situated physical action. PASS.

**b01c20s01n02** `"the doors open"`
- Type: HELD bone. axis_moves:[], axes_held: capability.
- Held axis ∈ scene axes_held? Capability is in the chapter-level axes_held list (held throughout chapter). Rationale: apparatus reading the door-sequence is full-deployment held; no new deployment event. HELD-AXIS-ENACTED: the door-opening IS the apparatus reading a specific event sequence — the held discipline is the feed parsing the sequence without a new deployment trigger. PASS.
- Grounding: true. PASS.

**b01c20s01n03** `"the Holdfast routes activate"`
- Type: MOVING bone. axis_moves: political_register-world up/1, cost_ledger_anchor: cl07c.
- Bonefide check: Holdfast access routes showing new traffic of the right people is the succession-machine executing — a direct Green-faction succession-position event. SVO causes the declared political_register-world up. Holdfast control is the dimension's nine_means. BONEFIDE: PASS.
- Grounding: true. PASS.

**b01c20s01n04** `"taylor-hebert-kl-122ac lifts the stylus"`
- Type: MOVING bone + HELD bone. axis_moves: moral_legibility_to_self up/1, cl07a. axes_held: moral_framework, capability.
- Bonefide check: lifting the stylus to mark the ledger — the act of entering the two facts — IS the aperture-opening of moral_legibility. The apparatus ran without her signal; the cleanliness of the mark is the first recognition-pressure. The SVO physically causes a small aperture on moral_legibility. BONEFIDE: PASS.
- Held axes: moral_framework held (no new breach; consequence arriving, not a new decision) ∈ chapter axes_held. Capability held (full-deployment, no new event) ∈ chapter axes_held. Both rationales name the discipline. PASS.
- Grounding: false. No grounding claim on this bone. (s01 grounding is covered by n01, n02, n03.)

**b01c20s01n05** `"taylor-hebert-kl-122ac marks the ledger"`
- Type: HELD bone. axis_moves:[], axes_held: political_register-prot, social_tether-antag.
- Held axes check: political_register-prot LOCKED rank 9 per chapter contract axes_held. social_tether-antag LOCKED rank 9 per chapter contract axes_held. Both ∈ chapter axes_held list. Rationales name the discipline (the act of marking correctly confirms rather than advances the locked contempt; the apparatus executing correctly produces no new contempt-event). HELD-AXIS-ENACTED: marking the ledger while the contempt is locked is the discipline of the locked contempt — exactly what the contempt-without-refusal form looks like at the bone level. PASS.
- Grounding: false. (s01 grounding covered.)

**Scene 1 aggregate:**
- position-world: n01 (+1 mag). Contract target +0.5. Single bone delivers the scene's magnitude-1 draw. Proportional: mag-1 is the only draw; maps to the scene's +0.5 fractional target. PASS.
- political_register-world: n03 (+1 mag). Contract target +0.5. Same as above. PASS.
- moral_legibility_to_self: n04 (+1 mag). Contract target +0.2 (intentionally small per contract note). This is a 3-magnitude system; a single mag-1 draw for a +0.2 fractional target is proportionally appropriate (it is the smallest draw in the scene). PASS.
- Stakes-axis check (position-world, per corrected s01 stakes_axis): position-world delivers +1 magnitude; political_register-world also delivers +1 magnitude — they tie. The contract note states: "NOTE s01: position-world ties political_register-world at the top (both +0.5) and no axis delivers larger — that satisfies 'largest' (the failure condition is a NON-stakes axis delivering LARGER)." The stakes_axis is position-world. The non-stakes axis delivering equal is political_register-world. moral_legibility_to_self delivers mag-1 as well. Wait — all three moving axes deliver magnitude 1. Let me re-examine: n01 position-world +1, n03 political_register-world +1, n04 moral_legibility_to_self +1. All three deliver magnitude 1. The contract specifies moral_legibility_to_self is intentionally small (+0.2 fractional). The STAKES-AXIS-DOMINANT check at the bone-gate level asks whether a NON-stakes axis delivers larger than the stakes axis. The stakes axis delivers magnitude 1. No axis delivers larger than magnitude 1. Stakes-axis is not dominated by a non-stakes axis. STAKES-AXIS-DOMINANT: PASS (no non-stakes axis delivers larger).
- NOTE on moral_legibility_to_self tying at magnitude 1: the proportional calibration note in the dispatch states moral_legibility is intentionally small (aperture-opening; peak is s04). A magnitude-1 draw maps to the declared +0.2 fractional which is the smallest fractional in the scene. The tie at the integer level is a consequence of the 1-3 integer system — the fractional mapping differentiates them. No fault fires.
- Sensory grounding: n01 (servant-passages empty), n02 (doors open), n03 (Holdfast routes activate) — three grounding bones. PASS.
- UNDERDELIVERY check: all axes_in_motion deliver ≥1 magnitude; no axis delivers 0. PASS.
- EVENT-PRESENCE check (detailed below).
- Opposing force visible: n01+n03+n04 collectively cover the opposing_force entry "apparatus ran without her signal; correctness is the pressure." n01 (passages empty = apparatus running pre-signal) and n03 (Holdfast routes = machine executing) are the physical fact that the apparatus needed no signal. PASS.

---

### SCENE 2 (b01c20s02) — 6 bones

**b01c20s02n01** `"the succession bell rings"`
- Type: CHATTER bone. axis_moves:[], axes_held:[] (neither moving nor held). cost_ledger_anchor: cl07c.
- Chatter-bone check: must have cost_ledger_anchor resolving at-or-under scene. Anchor is cl07c. cl07c gain = political_register-world +2 / cost = opportunity-missed on relational_anchor_status reaching rank 9. The succession bell propagates the announcement that cl07c locks political_register-world for. cl07c is the chapter-level anchor governing political_register-world LOCK events. The bell is a causal precondition for the political_register-world moves paid by cl07c (the succession is the event cl07c has been building toward). Anchor resolves at-or-under scene: cl07c fires across chapter; the bell in s02 is a cl07c-paid event. CHATTER-PAID: PASS.
- Grounding: true. Named physical sound event, place-situated. PASS.

**b01c20s02n02** `"the men enter the ward junctions"`
- Type: MOVING bone. axis_moves: social_tether-prot-collapse down/2, cost_ledger_anchor: cl07a.
- Bonefide check: wrong men moving fast through the right intersections — Taylor's catalogued ward junctions. Her mapped nodes are the violence's entry points. This SVO physically causes social_tether-prot-collapse: her network's routing intelligence becomes the violence's infrastructure. The node-entry IS the tether's structural dissolution beginning — the architecture is now being used against the people it was meant to protect. Rank claim visible: magnitude 2 = large draw on the −1.0 scene total, half of it. BONEFIDE: PASS.
- Grounding: true. Ward junctions named, specific physical geography. PASS.

**b01c20s02n03** `"the patron channel shifts sequence"`
- Type: MOVING bone. axis_moves: social_tether-prot-collapse down/2, cost_ledger_anchor: cl07a.
- Bonefide check: patron channel running a different sequence — not requiring Taylor's active delivery. The structural dissolution of the tether begins alongside the physical violence-entry. Magnitude 2 = second large draw; combined with n02 gives magnitude 4 total vs −1.0 contract. Wait: contract specifies −1.0 target. Bone aggregate: n02 (mag 2) + n03 (mag 2) + n06 (mag 1) = 5 magnitude total for social_tether-prot-collapse in s02. Let me recount: s02 contract is social_tether-prot-collapse −1.0. Using the proportional framework: the fractional rank-delta of −1.0 across the chapter's total of −3.5 means s02 accounts for roughly 28.6% of the chapter total. Bone magnitudes aggregate to 5 units (2+2+1). The total chapter-level social_tether-prot-collapse bones (s02+s03+s05) gives (5 in s02) + (s03 mag 2+2+2=6) + (s05 mag 2+1=3) = 14 total magnitude across the chapter. s02's 5/14 = 35.7% of chapter magnitude. Contract target proportion: s02 is −1.0/−3.5 = 28.6%. Difference: 35.7% vs 28.6% = 7.1 percentage points. This is within the ±1 magnitude per-axis PER-SCENE check tolerance. The magnitude total in s02 for social_tether-prot-collapse is 5 vs what would be needed for exact proportionality (5 × 28.6/35.7 = 4.0). Difference = 1 magnitude unit. Within ±1. PER-AXIS Δ: PASS.
- Grounding: false.

**b01c20s02n04** `"the gate-side routes fill"`
- Type: MOVING bone. axis_moves: position-prot-collapse down/1, cost_ledger_anchor: cl07b.
- Bonefide check: gate-side routes filling with factional movement — Taylor's mapped flow-points. position-prot-collapse begins its terminal descent as the apparatus runs without Taylor's active signal. SVO physically causes position-prot-collapse: the mapped routes being used by violence IS the position-of-no-use beginning to manifest. Rank claim visible: magnitude 1 is a small draw on the scene's −0.7 contract. BONEFIDE: PASS.
- Grounding: true. Gate-side routes are specific physical geography. PASS.

**b01c20s02n05** `"taylor-hebert-kl-122ac opens the feed"`
- Type: MOVING bone + HELD bone. axis_moves: moral_legibility_to_self up/1, cl07a. axes_held: capability, moral_framework.
- Bonefide check: Taylor opens (holds) the feed wide — routes-become-roadmap recognition visible in real time, one intersection at a time. The catalogue-as-map observation is the ledger becoming legible in real time. Opening/holding the feed wide IS the moral_legibility aperture widening — she sees her work becoming the violence's roadmap and cannot close coverage. Rank claim visible. BONEFIDE: PASS.
- Held axes: capability ∈ chapter axes_held (full-deployment; holding feed open is the discipline; no new deployment event). moral_framework ∈ chapter axes_held (violence propagating through routes is consequence, not new decision). Both rationales name the discipline. PASS.
- Grounding: false. (s02 grounding covered by n01, n02, n04.)

**b01c20s02n06** `"the faction-movement follows the passage-counts"`
- Type: MOVING bone + HELD bone. axis_moves: position-prot-collapse down/1, cl07b. axes_held: political_register-prot, social_tether-antag.
- Bonefide check: faction movement following Taylor's passage-counts IS position-prot-collapse — the instrument is confirmed dispensable/superseded; position declines as the apparatus doesn't need her active signal anymore. BONEFIDE: PASS.
- Held axes: political_register-prot LOCKED rank 9 ∈ chapter axes_held. social_tether-antag LOCKED rank 9 ∈ chapter axes_held. Rationales name the discipline (contempt is the register; leverage is terminal). PASS.
- Grounding: false.

**Scene 2 aggregate:**
- social_tether-prot-collapse: n02 (−2) + n03 (−2) + n06 implicit via social_tether-antag held... wait. n06 moves position-prot-collapse, not social_tether-prot-collapse. Let me recount social_tether-prot-collapse in s02: n02 (mag 2) + n03 (mag 2) = 4 total magnitude. The scene also has n06 moving position-prot-collapse. Wait — the bones-draft shows n06 axis_moves: position-prot-collapse down/1. So s02 social_tether-prot-collapse magnitude = n02(2) + n03(2) = 4. Contract target for s02 is −1.0. This is 4 magnitude units for a −1.0 target. Need to check per-axis Δ ±1 check. s02 delivers 4 units of social_tether-prot-collapse magnitude. The chapter-wide social_tether-prot-collapse total = s02(4) + s03(n01(2)+n02(2)+n06(2)=6) + s05(n03(2)+n04(1)=3) = 13 total. s02 target as fraction of total: −1.0/−3.5 = 28.6%. s02 actual as fraction: 4/13 = 30.8%. Difference is 2.2 percentage points — within ±1 magnitude unit tolerance. PASS.
- position-prot-collapse: n04 (−1) + n06 (−1) = 2 magnitude. Contract target −0.7. Chapter total position-prot-collapse: s02(2) + s03(n03(2)+n05(1)=3) + s05(n01(2)+n02(1)+n06(2)=5) = 10. s02 fraction: 2/10 = 20%. Contract fraction: 0.7/3.0 = 23.3%. Within ±1 unit. PASS.
- moral_legibility_to_self: n05 (+1) = 1 magnitude. Contract target +0.2. Within proportional tolerance (smallest draw). PASS.
- Stakes-axis: social_tether-prot-collapse is the declared stakes_axis. It delivers 4 magnitude. No other axis in s02 delivers more than 2. STAKES-AXIS-DOMINANT: PASS.
- Sensory grounding: n01 (bell — concrete physical sound event), n02 (ward junctions — physical geography), n04 (gate-side routes — physical geography). Three grounding bones. PASS.
- Opposing force visible: n02 and n03 are explicitly tagged as covering opposing_force (catalogue is the war's roadmap; patron channel shifting). PASS.
- Chatter: n01 is the only chatter bone, anchor cl07c. PASS.

---

### SCENE 3 (b01c20s03) — 6 bones

**b01c20s03n01** `"the burn reaches the outer wards"`
- Type: MOVING bone. axis_moves: social_tether-prot-collapse down/2, cl07a.
- Bonefide check: fire physically reaching Taylor's mapped outer wards IS social_tether-prot-collapse — the burn follows the ward-junction catalogue, which is the physical fact that the tether's architecture is now the violence's roadmap. SVO physically causes the declared Δ. BONEFIDE: PASS.
- Grounding: true. Fire on physical streets, outer-ward geography. PASS.

**b01c20s03n02** `"the fire traces the ward-junction catalogue"`
- Type: MOVING bone. axis_moves: social_tether-prot-collapse down/2, cl07a.
- Bonefide check: burn-line tracing the catalogue like a hand running down a list — the architecture visible in the fire's path. This is the mechanism of how the tether's content became the violence's skeleton. SVO physically causes the declared Δ. BONEFIDE: PASS.
- Grounding: true. Fire on physical streets, ward-junction geography. PASS.

**b01c20s03n03** `"the decommission message arrives"`
- Type: MOVING bone. axis_moves: position-prot-collapse down/2, cl07b.
- Bonefide check: the message through a non-Jarvis channel, addressing the function not the name — this IS position-prot-collapse. The instrument is declared expendable; position-of-no-exit becomes position-of-no-use. SVO physically causes the declared Δ. BONEFIDE: PASS.
- Grounding: false.

**b01c20s03n04** `"the apparatus network absorbs the coverage"`
- Type: MOVING bone. axis_moves: position-world up/1 (cl07b), political_register-world up/1 (cl07c).
- Bonefide check: apparatus absorbing Taylor's coverage into its own network — self-sustaining without the architect. This SVO physically causes position-world and political_register-world to move: the Green apparatus demonstrating self-sufficiency IS the succession position locking without Taylor active. BONEFIDE: PASS.
- Dual-axis bone: 2 axis_moves. Within axes_per_bone: 1-2 per chunk_targets. PASS.
- Grounding: false.

**b01c20s03n05** `"taylor-hebert-kl-122ac opens the ledger"`
- Type: MOVING bone + HELD bone. axis_moves: position-prot-collapse down/1, cl07b. axes_held: moral_framework, capability.
- Bonefide check: Taylor opens the ledger to mark entries — opening the ledger to enter the decommission data IS position-prot-collapse continuing its descent (she is marking her own expulsion). BONEFIDE: PASS.
- Held axes: moral_framework ∈ chapter axes_held (expulsion is consequence not a decision). capability ∈ chapter axes_held (feed still active; full-deployment holds through decommission receipt). Rationales name the discipline. PASS.
- Grounding: false.

**b01c20s03n06** `"taylor-hebert-kl-122ac marks the social_tether entry"`
- Type: MOVING bone + HELD bone. axis_moves: social_tether-prot-collapse down/2, cl07a. axes_held: political_register-prot, social_tether-antag.
- Bonefide check: marking the social_tether entry — patron channel closed, network transferred, tether severing — IS social_tether-prot-collapse. The physical act of marking confirms the decommission. BONEFIDE: PASS.
- Held axes: political_register-prot LOCKED rank 9 ∈ chapter axes_held. social_tether-antag LOCKED rank 9 ∈ chapter axes_held. Rationales name the discipline (function-addressed = contempt made institutional; instrument discarded = leverage terminal). PASS.
- Grounding: false.

**Scene 3 aggregate:**
- social_tether-prot-collapse: n01(2) + n02(2) + n06(2) = 6 magnitude. Contract target −1.5. Chapter total s03 fraction: 6/13 = 46.2%. Contract fraction: 1.5/3.5 = 42.9%. Difference ~3.3 ppt = ~0.43 magnitude units. Within ±1. PASS.
- position-prot-collapse: n03(2) + n05(1) = 3 magnitude. Contract target −1.0. Chapter total s03 fraction: 3/10 = 30%. Contract fraction: 1.0/3.0 = 33.3%. Within ±1. PASS.
- position-world: n04(+1). Contract target +0.3. Chapter s03 fraction: 1/(s01(1)+s03(1)+s05(1)) = 1/3 = 33.3%. Contract fraction: 0.3/1.0 = 30%. Within ±1. PASS.
- political_register-world: n04(+1). Contract target +0.2. Chapter s03 fraction: 1/3 = 33.3%. Contract fraction: 0.2/1.0 = 20%. Difference ~13 ppt = ~0.4 magnitude units. Within ±1. PASS.
- Stakes-axis: social_tether-prot-collapse is the declared stakes_axis. It delivers 6 magnitude. Next highest: position-prot-collapse at 3. STAKES-AXIS-DOMINANT: PASS.
- Sensory grounding: n01 (fire on outer wards — grounded), n02 (fire traces ward-junction streets — grounded). Two grounding bones. PASS.
- Opposing force visible: n03 and n04 are tagged covering opposing_force. PASS.
- UNDERDELIVERY check: moral_legibility_to_self is axes_in_motion at the chapter level but is not allocated to s03 in the scene contract — the scene contract shows no moral_legibility_to_self in s03 axes_in_motion. Correct: s03 contract axes_in_motion lists only social_tether-prot-collapse, position-prot-collapse, position-world, political_register-world. moral_legibility_to_self is not in s03's axes_in_motion; no delivery expected. PASS.

---

### SCENE 4 (b01c20s04) — 7 bones

**b01c20s04n01** `"the insect-feed runs in the east-of-water-gate lanes"`
- Type: HELD bone. axis_moves:[], axes_held: capability.
- Held axis ∈ chapter axes_held (capability full deployment). Rationale: feed active and held wide in the lanes Taylor maintained open; this is the held state visible, not a new deployment act. HELD-AXIS-ENACTED: the feed running in those specific lanes IS the capability-discipline enacted (the gap she held for Wren exists because the feed was managed around it). PASS.
- Grounding: true. Feed active in named geography. PASS.

**b01c20s04n02** `"the smoke fills the east-of-water-gate lanes"`
- Type: MOVING bone. axis_moves: relational_anchor_status up/2, cl07c.
- Bonefide check: PHYSICS ARRIVAL. Smoke physically filling the named lanes is the event that will disperse the insects — this is the causal initiator of the recognition chain. The SVO physically causes relational_anchor_status to begin its dominant move: the smoke's arrival IS the beginning of Wren's lanes going blank, which IS the un-priced item arriving. BONEFIDE: PASS. Concrete actor-verb-object physical action: "the smoke" (actor) "fills" (verb) "the east-of-water-gate lanes" (object). NOT perception-rendering. EVENT-NOT-CONCRETE: PASS.
- Grounding: true. Smoke on physical streets. PASS.

**b01c20s04n03** `"the heat disperses the insects"`
- Type: MOVING bone. axis_moves: relational_anchor_status up/2, cl07c.
- Bonefide check: heat (actor) dispersing insects (object) — PHYSICS, not perception. The heat acting on the insects is the mechanism by which the feed goes dark. This SVO physically causes relational_anchor_status to move: the dispersal IS the recognition mechanism operating. BONEFIDE: PASS. Concrete SVO: "the heat" acts on "the insects." EVENT-NOT-CONCRETE: PASS.
- Grounding: true. Heat + insect-scatter are sensory-physical particulars. PASS.

**b01c20s04n04** `"the insects scatter"`
- Type: MOVING bone. axis_moves: relational_anchor_status up/1, cl07c.
- Bonefide check: insects (actor) scatter (verb) — the feed losing coherence in the gap she kept. PHYSICS, not perception. The scatter IS the signal degrading. BONEFIDE: PASS. Concrete SVO. EVENT-NOT-CONCRETE: PASS.
- Grounding: true. PASS.

**b01c20s04n05** `"the signal drops from the lanes"`
- Type: MOVING bone + HELD bone. axis_moves: moral_legibility_to_self up/2, cl07a. axes_held: social_tether-prot-collapse, position-prot-collapse.
- Bonefide check: signal (actor) drops (verb) from the lanes (object). PHYSICS, not "Taylor perceives the signal dropping." The signal's physical departure IS the recognition arriving — the feed going blank in the lanes she held for Wren is the moral_legibility event (recognition-too-late bulk draw). BONEFIDE: PASS. Concrete SVO. EVENT-NOT-CONCRETE: PASS.
- Held axes: social_tether-prot-collapse (tether already structurally severed in s03; held at post-severing state) ∈ s04 contract axes_held. position-prot-collapse (expulsion already in motion from s03; held at current collapse state) ∈ s04 contract axes_held. Both rationales name the discipline. PASS.
- Grounding: true. The signal dropping is a concrete physical state change. PASS.

**b01c20s04n06** `"the east-of-water-gate lanes go blank"`
- Type: MOVING bone + HELD bone. axis_moves: moral_legibility_to_self up/1, cl07a. axes_held: moral_framework, political_register-prot, social_tether-antag.
- Bonefide check: "the lanes go blank" — the lanes (actor) go blank (verb+state). PHYSICS: the positive physical event of the lanes going blank. Not "Taylor notices the lanes are blank." BONEFIDE: PASS. Concrete SVO. EVENT-NOT-CONCRETE: PASS.
- Held axes: moral_framework ∈ chapter axes_held (recognition event is not a new framework decision — it is the consequence of the framework's final state arriving). political_register-prot LOCKED rank 9 ∈ chapter axes_held. social_tether-antag LOCKED rank 9 ∈ chapter axes_held. All three rationales name the discipline. PASS.
- Grounding: true. Place-situated physical state change. PASS.

**b01c20s04n07** `"taylor-hebert-kl-122ac lifts the stylus"`
- Type: HELD bone. axis_moves:[], axes_held: capability, relational_anchor_status.
- Held axes: capability ∈ chapter axes_held (feed going blank is physics not capability-failure; feed remains open; held at full deployment). relational_anchor_status — LOCK confirmed at rank 9 after n02-n06 moved it. The LOCK confirms means the axis is at terminal state; held-discipline bone enacts the LOCK completion (lifting the stylus and NOT opening a ledger line is the physical form of the LOCK). rationale: "LOCK confirms at rank 9 — the recognition-event has arrived complete; held at terminal state." Is relational_anchor_status ∈ axes_held for s04? The s04 contract (memory.md) axes_held does not explicitly list relational_anchor_status but its notes state "ALL other axes HELD — no collapse-axis or world-axis movement here." relational_anchor_status is the scene's stakes_axis and is in axes_in_motion — its motion is captured by n02-n04; by n07 it has reached LOCK and is now held at terminal state. The bone's rationale recognizes this correctly. HELD-AXIS-ENACTED: the physical act of lifting the stylus and not opening a line IS the LOCK-at-terminal-state discipline. PASS.
- Grounding: false. (Not marked as grounding. s04 grounding covered by n01-n06.)

**Scene 4 aggregate:**
- relational_anchor_status: n02(2) + n03(2) + n04(1) = 5 magnitude. Contract target +1.5. Chapter total relational_anchor_status = s04 only (5). s04/total = 100%. Contract target = 1.5/1.5 = 100%. PASS.
- moral_legibility_to_self: n05(2) + n06(1) = 3 magnitude. Contract target +0.5. Chapter total moral_legibility_to_self = s01(1) + s02(1) + s04(3) + s05(1) = 6. s04 fraction: 3/6 = 50%. Contract fraction: 0.5/1.0 = 50%. EXACT. PASS.
- Stakes-axis: relational_anchor_status is the declared stakes_axis. It delivers 5 magnitude. moral_legibility_to_self delivers 3. No other axis in s04 moves. STAKES-AXIS-DOMINANT: PASS.
- Sensory grounding: n01 (feed in named lanes — grounded), n02 (smoke on streets — grounded), n03 (heat + insects — grounded), n04 (insects scatter — grounded), n05 (signal drops — grounded), n06 (lanes go blank — grounded). Six grounding bones. PASS.
- CENTRAL-EVENT-CONCRETENESS (per dispatch CRITICAL case): the smoke-heat-insects-signal spine (n02-n06) — confirmed concrete actor-verb-object physics. None of these SVOs express Taylor's perception or the feed "flagging" a loss. Every bone in the spine acts on a physical subject performing a physical verb. EVENT-NOT-CONCRETE: PASS (the critical case is clean).
- Opposing force visible: n02-n05 are tagged covering opposing_force (physics of smoke/heat dispersing insects in the held gap). PASS.

---

### SCENE 5 (b01c20s05) — 6 bones

**b01c20s05n01** `"taylor-hebert-kl-122ac closes the feed"`
- Type: MOVING bone + HELD bone. axis_moves: position-prot-collapse down/2, cl07b. axes_held: capability.
- Bonefide check: feed closure is the expulsion's final confirmation — Taylor actively closes the feed, insects disperse to ambient range. The SVO physically causes position-prot-collapse: the closure IS the instrument's final act, the position's terminal descent. BONEFIDE: PASS.
- Held axis: capability ∈ chapter axes_held. Rationale: feed closure is the final capability act; the architecture returns to substrate; capability axis ends at terminal state. HELD-AXIS-ENACTED: closing the feed IS the terminal capability discipline — the architecture fulfilled to the last moment. PASS.
- Grounding: false.

**b01c20s05n02** `"the insects disperse"`
- Type: MOVING bone. axis_moves: position-prot-collapse down/1, cl07b.
- Bonefide check: insects (actor) disperse (verb) — the physical substrate of the feed returning to ambient range. This SVO physically causes position-prot-collapse: eleven months of KL deployment dissolving IS the position's terminal collapse at the physical level. BONEFIDE: PASS.
- Grounding: true. The insects' dispersal is the architecture returning to substrate — concrete physical action. PASS.

**b01c20s05n03** `"the architecture releases the wards"`
- Type: MOVING bone. axis_moves: social_tether-prot-collapse down/2 (cl07a), position-world up/1 (cl07b).
- Bonefide check: architecture (actor) releases the wards (object). The coverage she held herself is no longer held. What disperses is what was hers. social_tether-prot-collapse: the tether-network releasing IS the LOCK confirmation — patron dissolved, network transferred. position-world: apparatus becoming self-sustaining (the wards being "theirs now") IS position-world LOCK confirmation. BONEFIDE: PASS on both axes.
- Dual-axis: 2 axis_moves. Within axes_per_bone: 1-2. PASS.
- Grounding: false.

**b01c20s05n04** `"taylor-hebert-kl-122ac lifts the pack"`
- Type: MOVING bone. axis_moves: social_tether-prot-collapse down/1, cl07a.
- Bonefide check: Taylor lifts the pack — the departure begins. The physical act of lifting the pack IS social_tether-prot-collapse final draw: the person with no coin above subsistence lifting what she carries IS the tether's severing enacted in the body. BONEFIDE: PASS.
- Grounding: true. The pack is a physical object; departure made concrete. PASS.
- NOTE: "lifts" flagged in screen-writer note as a discrete physical act (the pack rising from the floor). Licensed as distinct from a sustained-carrying action. Consistent with chapter-level mannerism check (addressed below).

**b01c20s05n05** `"taylor-hebert-kl-122ac runs the ledger"`
- Type: MOVING bone + HELD bone. axis_moves: moral_legibility_to_self up/1, cl07a. axes_held: moral_framework, relational_anchor_status.
- Bonefide check: Taylor runs the full ledger at the gate. The physical act of running the ledger (stylus moving across entries) IS moral_legibility_to_self terminal close draw: the accuracy is the record of what she did and what it cost and what she refused to price and what the refusal cost. BONEFIDE: PASS.
- Held axes: moral_framework ∈ chapter axes_held (framework consumed-as-compass; departure is not a new decision-point; terminal state). relational_anchor_status — LOCKED rank 9 from s04; the recognition-event has completed; no further movement possible or required. relational_anchor_status is in chapter axes_held (listed under the s05 contract as "LOCKED rank 9 from scene 4"). PASS. Both rationales name the discipline. PASS.
- Grounding: false.

**b01c20s05n06** `"taylor-hebert-kl-122ac exits the south gate"`
- Type: MOVING bone + HELD bone. axis_moves: position-prot-collapse down/2 (cl07b), political_register-world up/2 (cl07c). axes_held: political_register-prot, social_tether-antag.
- Bonefide check: Taylor exits the south gate — the departure. position-prot-collapse LOCK: the physical departure IS position → rank 1 LOCKED. The instrument has left. political_register-world: the departure without notification IS the LOCK confirmation — Green succession apparatus runs without the instrument; locked. SVOs physically cause both declared Δs. BONEFIDE: PASS on both.
- Held axes: political_register-prot LOCKED rank 9 ∈ chapter axes_held. social_tether-antag LOCKED rank 9 ∈ chapter axes_held. Rationales name the discipline. PASS.
- Dual-axis: 2 axis_moves. Within axes_per_bone: 1-2. PASS.
- Grounding: true. South gate is a specific physical location; terminal departure bone. PASS.

**Scene 5 aggregate:**
- position-prot-collapse: n01(2) + n02(1) + n06(2) = 5 magnitude. Contract target −1.3. Chapter fraction: 5/10 = 50%. Contract fraction: 1.3/3.0 = 43.3%. Difference ~6.7 ppt = ~0.67 magnitude units. Within ±1. PASS.
- social_tether-prot-collapse: n03(2) + n04(1) = 3 magnitude. Contract target −1.0. Chapter fraction: 3/13 = 23.1%. Contract fraction: 1.0/3.5 = 28.6%. Difference ~5.5 ppt = ~0.72 magnitude units. Within ±1. PASS.
- moral_legibility_to_self: n05(1). Contract target +0.1. Smallest draw in chapter. Chapter fraction: 1/6 = 16.7%. Contract fraction: 0.1/1.0 = 10%. Within ±1. PASS.
- position-world: n03(1). Contract target +0.2. Chapter fraction: 1/3 = 33.3%. Contract fraction: 0.2/1.0 = 20%. Within ±1. PASS.
- political_register-world: n06(2). Contract target +0.3. Chapter fraction: 2/3 = 66.7%. Contract fraction: 0.3/1.0 = 30%. Difference = 36.7 ppt = 1.1 magnitude units. This is marginally over ±1. However: the chapter has only 3 scenes with political_register-world allocations (s01: 1 unit, s03: 1 unit, s05: 2 units). The contract allocations are s01 +0.5, s03 +0.2, s05 +0.3. The proportional issue is that s05 delivers 2 magnitude units for a +0.3 target while s01 and s03 each deliver 1 unit for larger targets (+0.5 and +0.2 respectively). The s05 target is the smallest but gets the largest magnitude. This is a SIGNAL-level proportionality mismatch, not a HARD finding, since the overall chapter-level political_register-world aggregate (1+1+2 = 4 units total) correctly maps to the chapter target of +1.0 (three-scene 1:1:2 ratio; the LOCK-confirmation bone at s05 appropriately carrying the largest single draw). The per-scene proportional issue is within the ±2-unit tolerance for SIGNAL rather than HARD classification.
- Stakes-axis: position-prot-collapse is the declared stakes_axis. It delivers 5 magnitude. Next highest: social_tether-prot-collapse at 3. STAKES-AXIS-DOMINANT: PASS.
- Sensory grounding: n02 (insects disperse — concrete physical), n04 (lifts the pack — concrete physical object), n06 (exits south gate — specific physical location). Three grounding bones. PASS.
- Opposing force visible: n05 covers opposing_force (ledger accuracy is the trap; nothing to refuse). PASS.

---

## EVENT-PRESENCE CHECKS (per-scene)

### Scene 1 event_map validation
Chunk tags: [event: viserys-death-in-feed], [event: succession-move-in-feed], [image: two-facts-one-moment], [mechanism: how-apparatus-executes], [force: protagonist_force], [force: opposing_force].

Event-map entries in bones-draft:
- `viserys-death-in-feed` → covered_by: [s01n01, s01n02]. Bone n01 ("servant-passages empty") IS the death in the feed (passages cease = death signal). Bone n02 ("doors open") is the door-sequence. Both exist and their SVOs physically ARE the event. COVERED. PASS.
- `succession-move-in-feed` → covered_by: [s01n03]. Bone n03 ("Holdfast routes activate") IS the succession-move. COVERED. PASS.
- `two-facts-one-moment` → covered_by: [s01n01, s01n03]. Image of two facts in one feed-window — n01 (death) and n03 (succession-machine). COVERED. PASS.
- `how-apparatus-executes` → covered_by: [s01n03]. Holdfast routes = apparatus execution mechanism. COVERED. PASS.
- `protagonist_force` → covered_by: [s01n04, s01n05]. Taylor reading + marking. COVERED. PASS.
- `opposing_force` → covered_by: [s01n01, s01n03, s01n04]. Apparatus running without her signal. COVERED. PASS.

Chunk tag → event_map completeness:
- [force: protagonist_force] in chunk → event_map has "protagonist_force" entry. PASS.
- [event: viserys-death-in-feed] → event_map has entry. PASS.
- [event: succession-move-in-feed] → event_map has entry. PASS.
- [image: two-facts-one-moment] → event_map has entry. PASS.
- [mechanism: how-apparatus-executes] → event_map has entry. PASS.
- [force: opposing_force] → event_map has entry. PASS.
EVENT-MAP-INCOMPLETE check: all chunk tags covered in event_map. PASS.

Central event (from contract): Viserys death + succession executes in feed. Covered by n01+n02 (death) and n03 (succession-move). PASS.
Protagonist_force bone: Taylor reads death + succession, marks ledger → n04 (lifts stylus) + n05 (marks ledger). PASS.

### Scene 2 event_map validation
Chunk tags: [event: succession-announcement-propagates], [event: factional-violence-enters-lower-city], [image: routes-become-roadmap], [mechanism: how-routes-become-roadmap], [force: opposing_force], [force: protagonist_force].

Event-map entries:
- `succession-announcement-propagates` → covered_by: [s02n01]. Bell rings = announcement propagates. COVERED. PASS.
- `factional-violence-enters-lower-city` → covered_by: [s02n02, s02n04]. Men enter ward junctions + gate-side routes fill. COVERED. PASS.
- `routes-become-roadmap` → covered_by: [s02n02, s02n06]. Men following the ward junctions + faction-movement following passage-counts. COVERED. PASS.
- `how-routes-become-roadmap` → covered_by: [s02n02, s02n06]. Mechanism: the junction/passage-count data IS the map. COVERED. PASS.
- `protagonist_force` → covered_by: [s02n05]. Taylor holds feed wide. COVERED. PASS.
- `opposing_force` → covered_by: [s02n02, s02n03]. Catalogue is the war's roadmap; patron channel shifting. COVERED. PASS.

Chunk tag → event_map completeness: all chunk tags present in event_map. PASS.
Central event: factional violence enters lower city. Covered by n02 + n04. PASS.
Protagonist_force: Taylor holds feed wide, reads violence through catalogue → n05. PASS.

### Scene 3 event_map validation
Chunk tags: [event: burn-reaches-outer-wards], [image: burn-line-traces-catalogue], [mechanism: how-coverage-becomes-violence-path], [event: expulsion-mechanism-first-move], [mechanism: how-expulsion-triggers], [force: opposing_force], [force: protagonist_force].

Event-map entries:
- `burn-reaches-outer-wards` → covered_by: [s03n01]. COVERED. PASS.
- `burn-line-traces-catalogue` → covered_by: [s03n02]. Image: fire tracing the ward-junction catalogue. COVERED. PASS.
- `how-coverage-becomes-violence-path` → covered_by: [s03n02]. Mechanism: fire traces the catalogue. COVERED. PASS.
- `expulsion-mechanism-first-move` → covered_by: [s03n03]. Decommission message arrives. COVERED. PASS.
- `how-expulsion-triggers` → covered_by: [s03n03]. Mechanism: message through non-Jarvis channel, function-addressed. Ambiguity preserved (discovered OR no-longer-needed). COVERED. PASS.
- `protagonist_force` → covered_by: [s03n05, s03n06]. Taylor marks decommission accurately. COVERED. PASS.
- `opposing_force` → covered_by: [s03n03, s03n04]. Apparatus absorbed coverage; function-addressed. COVERED. PASS.

Chunk tag → event_map completeness: all chunk tags present in event_map. PASS.
Central event: burn reaches outer wards + decommission message arrives. n01 (burn) + n03 (decommission). PASS.
Protagonist_force: Taylor marks decommission accurately in ledger → n05 + n06. PASS.

### Scene 4 event_map validation
Chunk tags: [event: feed-active-in-wren-lanes], [image: coverage-gap-held-open], [mechanism: how-coverage-gap-was-maintained], [mechanism: how-smoke-and-heat-disperse-insects], [event: smoke-heat-disperses-insects], [image: feed-going-dark-in-wrens-lanes], [event: feed-signal-loss-from-wren-lanes], [event: recognition-too-late-arrives], [image: un-priced-item-is-the-one-the-calculus-came-for], [mechanism: why-wren-cannot-be-entered-as-loss], [force: protagonist_force], [force: opposing_force].

Event-map entries:
- `feed-active-in-wren-lanes` → covered_by: [s04n01]. COVERED. PASS.
- `coverage-gap-held-open` → covered_by: [s04n01]. COVERED. PASS.
- `how-coverage-gap-was-maintained` → covered_by: [s04n01]. COVERED. PASS.
- `how-smoke-and-heat-disperse-insects` → covered_by: [s04n02, s04n03, s04n04]. COVERED. PASS.
- `smoke-heat-disperses-insects` → covered_by: [s04n02, s04n03, s04n04]. COVERED. PASS.
- `feed-going-dark-in-wrens-lanes` → covered_by: [s04n05, s04n06]. COVERED. PASS.
- `feed-signal-loss-from-wren-lanes` → covered_by: [s04n05, s04n06]. COVERED. PASS.
- `recognition-too-late-arrives` → covered_by: [s04n05, s04n06, s04n07]. COVERED. PASS.
- `un-priced-item-is-the-one-the-calculus-came-for` → covered_by: [s04n07]. COVERED. PASS.
- `why-wren-cannot-be-entered-as-loss` → covered_by: [s04n07]. COVERED. PASS.
- `protagonist_force` → covered_by: [s04n01, s04n07]. COVERED. PASS.
- `opposing_force` → covered_by: [s04n02, s04n03, s04n04, s04n05]. COVERED. PASS.

Chunk tag → event_map completeness: all chunk tags present in event_map. PASS.
Central event (recognition spine): smoke fills lanes / heat disperses insects / insects scatter / signal drops / lanes go blank — covered by n02+n03+n04+n05+n06. PASS.
Protagonist_force: Taylor holds feed open in Wren's lanes, holds on blank → n01 (grounding) + n07 (holds on blank). PASS.

### Scene 5 event_map validation
Chunk tags: [event: feed-closed-before-departure], [mechanism: how-feed-closure-is-enacted], [force: opposing_force], [event: expulsion-final-departure], [image: departure-through-south-gate-unregistered], [event: position-collapse-completes], [event: social-tether-severed-confirmed], [force: protagonist_force], [image: ledger-accurate-nothing-to-refuse], [event: contempt-complete], [image: closing-image-contempt-complete-ledger-accurate-nothing-to-refuse], [event: chapter-close-nothing-remaining].

Event-map entries:
- `feed-closed-before-departure` → covered_by: [s05n01]. COVERED. PASS.
- `how-feed-closure-is-enacted` → covered_by: [s05n01, s05n02]. COVERED. PASS.
- `expulsion-final-departure` → covered_by: [s05n04, s05n06]. COVERED. PASS.
- `departure-through-south-gate-unregistered` → covered_by: [s05n06]. COVERED. PASS.
- `position-collapse-completes` → covered_by: [s05n01, s05n06]. COVERED. PASS.
- `social-tether-severed-confirmed` → covered_by: [s05n03]. COVERED. PASS.
- `ledger-accurate-nothing-to-refuse` → covered_by: [s05n05]. COVERED. PASS.
- `contempt-complete` → covered_by: [s05n05, s05n06]. COVERED. PASS.
- `chapter-close-nothing-remaining` → covered_by: [s05n06]. COVERED. PASS.
- `closing-image-contempt-complete-ledger-accurate-nothing-to-refuse` → covered_by: [s05n05, s05n06]. COVERED. PASS.
- `protagonist_force` → covered_by: [s05n01, s05n05, s05n06]. COVERED. PASS.
- `opposing_force` → covered_by: [s05n05]. COVERED. PASS.

Chunk tag → event_map completeness: all chunk tags present in event_map. PASS.
Central event: Taylor closes feed, runs ledger at gate, exits south gate. n01 (closes feed) + n05 (runs ledger) + n06 (exits south gate). PASS.
Protagonist_force: closes feed, runs ledger, departs → n01+n05+n06. PASS.

---

## COST-LEDGER VERIFICATION

### cl07a (moral_legibility_to_self +4 / social_tether-prot-collapse −7)
Gain side (moral_legibility_to_self +4 across book): b01c20 draws +1.0 chapter total. Bones: s01n04 (+1 cl07a), s02n05 (+1 cl07a), s04n05 (+2 cl07a), s04n06 (+1 cl07a), s05n05 (+1 cl07a) = 6 units magnitude, maps to +1.0 fractional gain. cl07a gain-side visible in bones with matching direction. PASS.
Cost side (social_tether-prot-collapse −7 across book): b01c20 draws −3.5 chapter total. Bones: s02n02 (−2), s02n03 (−2), s03n01 (−2), s03n02 (−2), s03n06 (−2), s05n03 (−2), s05n04 (−1) = 13 units magnitude, maps to −3.5 fractional draw. cl07a cost-side visible in bones with matching direction. PASS.

### cl07b (position-world +2 / position-prot-collapse −6)
Gain side (position-world): s01n01 (+1), s03n04 (+1), s05n03 (+1) = 3 units, maps to +1.0 fractional gain for chapter. cl07b gain-side visible. PASS.
Cost side (position-prot-collapse): s02n04 (−1), s02n06 (−1), s03n03 (−2), s03n05 (−1), s05n01 (−2), s05n02 (−1), s05n06 (−2) = 10 units, maps to −3.0 fractional draw. cl07b cost-side visible in bones with matching direction. PASS.

### cl07c (political_register-world +2 / opportunity-missed → relational_anchor_status rank 9)
Gain side (political_register-world): s01n03 (+1), s03n04 (+1), s05n06 (+2) = 4 units, maps to +1.0 fractional gain. cl07c gain-side visible. PASS.
Opportunity-missed side (relational_anchor_status LOCK): s04n02 (+2), s04n03 (+2), s04n04 (+1) = 5 units, maps to +1.5 fractional draw to LOCK. cl07c cost-side (opportunity-missed: un-priced item is what the calculus came for) is visible through the relational_anchor_status bones anchored to cl07c in s04. PASS.

---

## HELD AXES WITNESSED (chapter-level)

Chapter axes_held per contract:
- moral_framework: witnessed in s01n04, s01n05, s02n05, s02n06... multiple bones across all 5 scenes. PASS.
- capability: witnessed in s01n02, s01n04, s02n05, s03n05, s04n01, s04n07, s05n01. PASS.
- political_register-prot (LOCKED rank 9): witnessed in s01n05, s02n06, s03n06, s04n06, s05n06, plus several held-rationale bones. PASS.
- social_tether-antag (LOCKED rank 9): witnessed in s01n05, s02n06, s03n06, s04n07 (via held rationale), s05n06. PASS.

Intra-scene held witnesses:
- s01 axes_held in bones: moral_framework (n04, n05), capability (n02, n04), political_register-prot (n05), social_tether-antag (n05). All held entries named in bones. PASS.
- s02 axes_held: moral_framework (n05), capability (n05), political_register-prot (n06), social_tether-antag (n06). All witnessed. PASS.
- s03 axes_held: moral_framework (n05), capability (n05), political_register-prot (n06), social_tether-antag (n06). All witnessed. PASS.
- s04 axes_held: capability (n01, n07), social_tether-prot-collapse (n05), position-prot-collapse (n05), moral_framework (n06), political_register-prot (n06), social_tether-antag (n06). All witnessed. PASS.
- s05 axes_held: capability (n01), moral_framework (n05), relational_anchor_status (n05), political_register-prot (n06), social_tether-antag (n06). All witnessed. PASS.

---

## OPPOSING FORCE VISIBLE

Per scene:
- s01: n01 + n03 + n04 cover the opposing_force (apparatus ran without her signal). PASS.
- s02: n02 + n03 cover the opposing_force (catalogue is war's roadmap; patron channel shifting). PASS.
- s03: n03 + n04 cover the opposing_force (apparatus absorbed coverage; function-addressed). PASS.
- s04: n02 + n03 + n04 + n05 cover the opposing_force (physics of smoke/heat dispersing insects in the held gap). PASS.
- s05: n05 covers the opposing_force (ledger accuracy is the trap; nothing to refuse). PASS.

---

## ABSTRACTION-DOMINANCE CHECK

Grounding bones per scene (marked grounding: true):
- s01: n01, n02, n03 = 3 grounding out of 5 total bones. Non-chatter: 5 (n01 = moving, n02 = held, n03 = moving, n04 = moving+held, n05 = held). Threshold: ceil(0.25 × 5) = 2. Grounding = 3 ≥ 2. PASS.
- s02: n01, n02, n04 = 3 grounding out of 6 total. Non-chatter: 5 (n01 is chatter). Threshold: ceil(0.25 × 5) = 2. Grounding = 3 ≥ 2. PASS.
- s03: n01, n02 = 2 grounding out of 6 total non-chatter bones = 6. Threshold: ceil(0.25 × 6) = 2. Grounding = 2 = threshold. PASS (exactly at threshold).
- s04: n01, n02, n03, n04, n05, n06 = 6 grounding out of 7 total non-chatter = 7. Threshold: ceil(0.25 × 7) = 2. Grounding = 6 >> 2. PASS.
- s05: n02, n04, n06 = 3 grounding out of 6 total non-chatter = 6. Threshold: ceil(0.25 × 6) = 2. Grounding = 3 ≥ 2. PASS.

No scene fires ABSTRACTION-DOMINANT.

---

## REGISTER-AS-MANNERISM CHECK (chapter-level)

Scanning for any single VERB+OBJECT pair (subject-independent) appearing in ≥3 bones.

Per the dispatch note, specific pairs to check:
- "lifts the stylus": s01n04 ("lifts the stylus"), s04n07 ("lifts the stylus") = 2 occurrences. Does not reach threshold of 3. PASS.
- "lifts the pack": s05n04 ("lifts the pack") = 1 occurrence. PASS.
- "marks the ledger": s01n05 ("marks the ledger") = 1 occurrence. PASS.
- "opens the feed": s02n05 ("opens the feed") = 1 occurrence. PASS.
- "opens the ledger": s03n05 ("opens the ledger") = 1 occurrence. PASS.

Scanning all verbs across all 30 bones for any pair at ≥3:
- "lifts": s01n04 (lifts the stylus), s04n07 (lifts the stylus), s05n04 (lifts the pack). Three "lifts" verb instances but with two different objects: "the stylus" (×2) and "the pack" (×1). The VERB+OBJECT pair "lifts the stylus" appears exactly 2 times (threshold is 3). "lifts the pack" appears once. No VERB+OBJECT pair reaches 3. PASS.
- "marks": s01n05 ("marks the ledger"), s03n06 ("marks the social_tether entry"). Same verb, different objects. Each appears once as a VERB+OBJECT pair. PASS.
- "opens": s02n05 ("opens the feed"), s03n05 ("opens the ledger"). Two different VERB+OBJECT pairs, each once. PASS.

No REGISTER-AS-MANNERISM finding. PASS.

---

## SIGNAL FINDINGS

### signal-001 (ADVISORY — s05 political_register-world proportional skew)
Scene 5 delivers magnitude 2 on political_register-world against a +0.3 fractional target, while scenes 1 and 3 each deliver magnitude 1 against larger targets (+0.5 and +0.2). The skew is ~1.1 magnitude units above strict proportionality. This is within the ±2-unit SIGNAL classification range. The s05n06 bone ("exits the south gate") carries both position-prot-collapse (−2) and political_register-world (+2) simultaneously as a LOCK-confirmation bone — the magnitude-2 draw on political_register-world is structurally coupled to the LOCK event (the departure IS the Green succession locking without Taylor). The pairing is load-bearing; reducing the political_register-world magnitude on this bone would require a separate LOCK-confirmation bone, which would increase bone count rather than resolve the proportional issue. Disposition: ACCEPT-WITH-RATIONALE. The s05 exit bone's dual-magnitude coupling serves the LOCK-confirmation function; the proportional skew is structural not incidental.

---

## SUMMARY TABLE

| id | type | bone | finding |
|----|------|------|---------|
| signal-001 | signal | s05n06 | political_register-world magnitude skew in s05 (~1.1 unit over strict proportionality); LOCK-event coupling accepted with rationale |

HARD findings: 0
SIGNAL findings: 1 (accepted with rationale; non-blocking)

---

## VERDICT: PASS

Zero HARD findings. One SIGNAL finding disposed as ACCEPT-WITH-RATIONALE.

All per-bone checks:
- SUBSTANCE-FLAT: none
- HELD-AXIS-NOT-ENACTED: none
- HELD-AXIS-UNCONTRACTED: none
- CHATTER-UNPAID: none (s02n01 cl07c-anchored; PASS)
- EVENT-UNCOVERED: none
- EVENT-MAP-INCOMPLETE: none
- STAKES-AXIS-NOT-DOMINANT: none (all 5 scenes PASS)
- AXIS-DELTA-MISMATCH (gross): none
- SENSORY-GROUNDING-ABSENT: none (all 5 scenes have ≥2 grounding bones)
- EVENT-NOT-CONCRETE: none (s04 recognition spine — smoke fills lanes / heat disperses insects / insects scatter / signal drops / lanes go blank — all confirmed concrete physics-as-actor SVOs)
- OPPOSING-FORCE-MISSING: none
- COST-LEDGER-UNPAID: none

---

## GATE VERDICTS — PER BONE

```
b01c20s01n01: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s01n02: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s01n03: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s01n04: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s01n05: gate_verdict: { bonefide: true, flat: false, signals: [] }

b01c20s02n01: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s02n02: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s02n03: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s02n04: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s02n05: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s02n06: gate_verdict: { bonefide: true, flat: false, signals: [] }

b01c20s03n01: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s03n02: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s03n03: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s03n04: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s03n05: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s03n06: gate_verdict: { bonefide: true, flat: false, signals: [] }

b01c20s04n01: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s04n02: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s04n03: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s04n04: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s04n05: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s04n06: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s04n07: gate_verdict: { bonefide: true, flat: false, signals: [] }

b01c20s05n01: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s05n02: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s05n03: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s05n04: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s05n05: gate_verdict: { bonefide: true, flat: false, signals: [] }
b01c20s05n06: gate_verdict: { bonefide: true, flat: false, signals: [] }
```

---

## SPECIAL NOTES FOR DOWNSTREAM PHASES

1. **s04 recognition spine confirmed concrete.** All five physics-as-actor SVOs (smoke fills lanes / heat disperses insects / insects scatter / signal drops / lanes go blank) pass EVENT-NOT-CONCRETE. The /and-facets dispatch may proceed without a spine-concreteness risk flag.

2. **moral_legibility_to_self s01 aperture note.** The contract note states this is intentionally small (aperture-opening; peak is s04). The magnitude-1 draw in s01 maps to the +0.2 fractional target. This is correct; the ledger-auditor notes confirm this rationale is accepted and does NOT fire as an underdelivery fault.

3. **"lifts the stylus" count = 2 across chapter** (s01n04, s04n07). Below the ≥3 REGISTER-AS-MANNERISM threshold. Clean.

4. **s05n06 dual-axis LOCK bone** (position-prot-collapse −2 / political_register-world +2). The political_register-world side carries the signal-001 proportional skew note. Non-blocking. Carry to /and-write Phase 7 emit: ensure the bone's dual-axis gate_verdict captures signal-001 as ACCEPTED.
```
b01c20s05n06: gate_verdict: { bonefide: true, flat: false, signals: [ACCEPTED-signal-001-political-register-world-lock-skew] }
```
(Updated above entry to reflect the signal carry.)

---

report_path: active-project/staff/auditor/write-b01c20-bone-gate.md
audited_at: 2026-06-05
