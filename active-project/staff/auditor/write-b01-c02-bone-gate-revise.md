# /and-write b01c02 revise — Phase 6 substance bone-gate (auditor fork)
# Date: 2026-05-26
# Auditor: auditor (third fork, fresh context)

audit:
  scope: chapter
  target: b01c02
  timestamp: 2026-05-26
  findings:

    - id: signal-001
      type: flag
      what: "chapter-level: social_tether-prot-rise and political_register-prot are declared held in the chapter contract (memory.md lines 2469–2477) but no bone in any of the three scenes enacts discipline-against-pressure for either axis; neither axis appears in any bone's axes_held[] across all 47 bones"
      why: "strict HELD-AXIS-NOT-WITNESSED protocol requires a held axis to have at least one bone-level enactment of stillness-against-pressure. Without it, a reviewer cannot distinguish 'axis held under pressure' from 'axis not tracked.' Downstream: if c03 introduces court-tier content that moves social_tether-prot-rise, there is no established bone-level discipline anchor to contrast against."
      disposition: "ACCEPTED — carries Phase 2 constraint-audit disposition. This chapter's content (Taylor alone, no patron, no court encounter, no active tether-building) produces no material pressure on either axis. The held-but-unwitnessed pattern is consistent with a dormancy-prefigure chapter by design. Chapter contract rationale on-record at memory.md lines 2551–2554. SIGNAL not HARD."

    - id: signal-002
      type: flag
      what: "chapter-level: 'takes the drain angle' (VERB: takes, OBJECT: the drain angle) appears as an exact VERB OBJECT pair at s01n03, s02n06, and s03n01 — 3 occurrences, meeting the register-as-mannerism threshold of ≥3"
      why: "a VERB OBJECT pair repeated three times across a 47-bone chapter risks rendering the gesture as a verbal tic rather than a narratively distinct return. The drain-angle departure is structurally load-bearing as a chapter-open / seam-bridge / chapter-close marker, but identical SVO phrasing at all three instances collapses the distinction between them. The stitcher will need surface-level differentiation (rhythm, surrounding sentence weight, time-marker placement) to avoid the cold-reader 'same line' read the staging audit flagged at the original bones pass."
      disposition: "ACCEPTED at SIGNAL — does not block emission. The repetition is architecturally motivated: the drain angle is the chapter's physical anchor point and the three instances mark scene-boundary transitions. Advisory forwarded to /and-stitch Phase 5 voice transform."

## Per-bone verification

Moving bones (2 total):
- s02n13 ("the insects file the ward-junction contact"): axis_moves relational_anchor_status +1.0 up. PASS bonefide. Filing the contact in the feed IS the physical causal act that opens the anchor account; no cost-ledger entry because no value traded (structural opening only, per memory.md line 2591). cost_ledger_anchor null confirmed.
- s03n11 ("taylor-hebert-kl-122ac stalls the count"): axis_moves moral_legibility_to_self +1.0 up. PASS bonefide. Stalling the count IS the physical causal act through which recognition arrives — the count will not close cleanly at the ward-junction entry, and the refusal to close is the crack. cost_ledger_anchor null confirmed (off-ledger by design, per memory.md line 2638). Delivered 1.0 vs target 0.5; within ±1 tolerance.

Held bones (45 total): 45 PASS.
All 45 non-moving bones declare axes_held[] with at least one axis and a rationale naming the discipline or dormancy function. No bone carries axes_holds[] and axis_moves[] both empty (chatter). Spot-checks:
- s03n12 ("taylor-hebert-kl-122ac holds the breath"): canonical body-part stillness-against-pressure license. Holds moral_legibility_to_self (crack arrived, not yet suppressed) and moral_framework (suppression mechanism not yet invoked). SOFT-WATCH-1 bridge bone. PASS.
- s02n15 ("the insects reach the junction-lane edge"): absence encoded as positive physical act. Holds relational_anchor_status. Physical actor + physical verb + physical object. SOFT-WATCH-2 compliance confirmed. PASS.
- s02n14 ("the insects return the junction-lane attenuation"): gap as perceptual feed-event, not retrospective label. SOFT-WATCH-2 compliance confirmed. PASS.
- social_tether-prot-rise, political_register-prot: unwitnessed in all scenes. See signal-001.

Chatter bones: 0. N/A.

## Per-scene verification

### s01 (14 bones; no axes_in_motion)
Event-presence (HARD, URI-WRITE-EVENT-COVERAGE):
- [force: Taylor's decision to extend coverage]: covered — s01n04 (fever-cluster as causal precipitant), s01n11 (extends the range). PASS.
- [event: Taylor notices a fever-cluster she cannot locate]: covered — s01n04 (fever-cluster returns three heat-signatures across two alleys; ambiguity encoded as spread). PASS.
- [mechanism: insect-feed fever-reading without contact]: covered — s01n01 (flies return heat-signatures), s01n02 (beetles return threshold-count), s01n09 (four hundred bodies in the feed). PASS.
- [event: Taylor makes the explicit decision to run coverage]: covered — s01n11 (extends the range). PASS.
- [force: harm-reduction framing contains the decision]: covered — s01n12 (draws the line; prohibition-check), s01n10 (alley-back drops; rationale names harm-reduction as operational justification for accepting the cost). PASS.
- [event: Taylor begins the first precinct sweep]: covered — s01n05 (insects fan the alleys), s01n13 (insects fill the Hook). PASS.

Per-axis Δ: N/A (no axes_in_motion in s01).
Underdelivery-rationale: N/A.
Sensory-grounding (HARD): PASS at s01n01 (flies / heat-signatures — concrete physical agent, physical return, physical referent) and s01n02 (beetles / threshold-count — physical actors, physical substrate).
Opposing-force visible (HARD): s01n04 (fever-cluster names the ceiling — the unlocatable cluster is the opposing pressure), s01n10 (alley-back drops from feed — suppression cost as physical event confirming the ceiling), s01n12 (draws the line — prohibition checked as active resistance). PASS.
Stakes-axis (HARD): moral_framework in s01 axes_held; s01n12 enacts prohibition-check directly. PASS.

### s02 (15 bones; relational_anchor_status +1.0)
Event-presence (HARD, URI-WRITE-EVENT-COVERAGE):
- [event: Wren enters the insect-feed repeatedly across multiple survey sweeps]: covered — s02n04 (beetles return stitch-house threshold-crossings), s02n05 (threshold-crossings repeat the weight-on-stone sequence). PASS.
- [image: Wren's movement pattern]: covered — s02n04+n05 (pattern accumulates across days), s02n10 (function-signature returned through live encounter). PASS.
- [mechanism: coverage-map categorization without contact]: covered — s02n03 (coverage map anchors stitch-house threshold), s02n10+n11 (function-signature returned; connector-type assigned). PASS.
- [event: Taylor categorizes Wren as a ward-junction contact in her internal accounting]: covered — s02n11 (map assigns junction-body connector-type), s02n13 (insects file the ward-junction contact; axis-mover). PASS.
- [force: Taylor's discipline against approaching Wren]: covered — s02n09 (yields the alley-mouth), s02n12 (turns from the alley-mouth). PASS.
- [force: Wren's network-centrality as opposing pressure]: covered — s02n14 (insects return junction-lane attenuation — Wren's territory as feed-boundary), s02n15 (insects reach the junction-lane edge — gap as positive physical limit). PASS.
- [event: relational_anchor_status account opens]: covered — s02n13 (axis-mover: +1.0). PASS.

Per-axis Δ (HARD): relational_anchor_status target +1.0; delivered +1.0 at s02n13. EXACT. PASS.
Underdelivery-rationale: N/A (100% delivery).
Stakes-axis-dominant (HARD): relational_anchor_status is the sole axis_in_motion for s02 and IS the stakes_axis. PASS.
Sensory-grounding (HARD): PASS at s02n02 (tallow smoke marks the stitch-house lane — concrete sensory substance, physical action, place-situated).
Opposing-force visible (HARD): s02n09 (yields the alley-mouth — discipline live against approach-risk), s02n12 (turns from alley-mouth — not-looking-closer enacted), s02n14+n15 (junction-lane attenuation; insects reach edge — Wren's territory as perceptual wall). PASS.
Stakes-axis (HARD): relational_anchor_status in axes_in_motion; sole mover IS stakes_axis. PASS.

### s03 (18 bones; moral_legibility_to_self +1.0 within ±1 of +0.5 target)
Event-presence (HARD, URI-WRITE-EVENT-COVERAGE):
- [event: Taylor does the full accounting of the precinct survey]: covered — s03n04 (runs the map), s03n05+n06 (fever-cluster corner; dark-junction corner staged), s03n07+n08 (map returns bodies; accounting closes count). PASS.
- [image: the scope of the map — forty-three people categorized without their knowledge]: covered — s03n07 (map returns the bodies), s03n08 (accounting closes the count — forty-three registered). PASS.
- [force: the recognition arriving at the edge of the accounting]: covered — s03n09 (accounting reaches ward-junction entry), s03n10 (ward-junction corner returns junction-lane void — recognition arriving through the gap). PASS.
- [event: Taylor recognizes the coverage map as surveillance]: covered — s03n11 (stalls the count; axis-mover; recognition arrives as the stall). PASS.
- [event: Taylor suppresses the recognition and files the map under harm-reduction]: covered — s03n12 (holds the breath — holding beat), s03n13 (draws the line — suppression executing), s03n14 (closes against drain angle — physical correlate). PASS.
- [mechanism: the suppression mechanism — harm-reduction accounting closes the ledger before reckoning can open it]: covered — s03n13 (draws the line; rationale names the mechanism), s03n15+n16+n17 (accounting/ledger closes entries). PASS.
- [force: the ledger closing as active discipline]: covered — s03n13+n14 (suppression executing + physical correlate), s03n17 (ward-junction contact closing differentiated — half-beat longer). PASS.
- [event: chapter closes with the coverage map intact and the ledger closed]: covered — s03n17 (ledger closes the ward-junction contact), s03n18 (exhale — chapter-close). PASS.

Per-axis Δ (HARD): moral_legibility_to_self target +0.5; delivered +1.0 at s03n11. |delivered − target| = 0.5, within ±1 tolerance. PASS.
Underdelivery-rationale: N/A (overdelivery at 200%; within tolerance band).
Stakes-axis-dominant (HARD): moral_legibility_to_self is the sole axis_in_motion for s03 and IS the stakes_axis. PASS.
Sensory-grounding (HARD): PASS at s03n02 (insects return from lane-mouth sweep — physical actors, physical action, spatial referent) and s03n03 (shadow fills the drain angle — concrete physical object, place-situated).
Opposing-force visible (HARD): s03n09+n10 (accounting reaches ward-junction entry; corner returns junction-lane void — recognition approaching through the gap), s03n11 (stall — the opposing force's peak push; recognition cannot be deflected until it arrives). PASS.
Stakes-axis (HARD): moral_legibility_to_self in axes_in_motion; sole mover IS stakes_axis. PASS.

## Per-chapter verification

### Cost-ledger entries
No cost-ledger entries resolve at or before c02. cl01b anchored at c03 (pl-2026-05-25-001). cl02 / cl-antag-d03 are c03+. Both axis-movers carry cost_ledger_anchor: null. PASS.

### HELD-AXIS-NOT-WITNESSED disposition
See signal-001. ACCEPTED. social_tether-prot-rise and political_register-prot held at chapter level, no bone-level witness in any scene. Consistent with dormancy-prefigure chapter architecture — no court-tier content, no patron, no active tether pressure. Phase 2 disposition carried forward unchanged.

### Register-as-mannerism
See signal-002. SIGNAL. One pair at threshold:
- "takes the drain angle": s01n03, s02n06, s03n01 — 3 exact occurrences.

All other candidates under threshold:
- "draws the line": s01n12, s03n13 — 2 occurrences.
- "closes the [entry/contact]": s03n15 (fever-cluster entry), s03n16 (dark-junction entry), s03n17 (ward-junction contact) — objects differ; strict pair "closes the [X] entry" matches n15+n16 only (2 with same object form). Under threshold.
- "returns the [X]": widespread across chapter but with distinct objects at every occurrence — no single VERB OBJECT pair reaches 3.

## HARD findings
None.

## SIGNAL findings

signal-001: HELD-AXIS-NOT-WITNESSED (social_tether-prot-rise, political_register-prot)
  Disposition: ACCEPTED — dormancy chapter; no pressure on these axes exists in chapter content; Phase 2 carried forward. No remediation required.

signal-002: REGISTER-AS-MANNERISM ("takes the drain angle" x3 at s01n03, s02n06, s03n01)
  Disposition: ACCEPTED with stitcher advisory. Architecturally motivated; drain angle is chapter's physical anchor point; three instances mark scene-boundary transitions. Advisory: /and-stitch Phase 5 voice transform should surface-differentiate these three instances to avoid cold-reader 'same line' read. Does not block emission.

## Summary

PASS — 0 HARD findings, 2 SIGNAL findings (both accepted with documented rationale).

All 47 bones verified. Both axis-movers (s02n13, s03n11) are causally bonefide and deliver within tolerance. All chunk event-tags have covering bones across all three scenes. Sensory-grounding, opposing-force visibility, and stakes-axis dominance confirmed per scene. Cost-ledger: no entries resolve at c02. SOFT-WATCH-1 (recognition → holding → suppression at s03n11→n12→n13) and SOFT-WATCH-2 (gap-as-feed-event at s02n14→n15) structurally honored. HELD-AXIS-NOT-WITNESSED and register-as-mannerism carried at SIGNAL without remediation requirement.

Phase 7 emission unblocked.
