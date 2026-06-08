---
audit:
  scope: chapter
  target: b01c13
  timestamp: 2026-06-03
  gate: substance-chapter-phase-5
  verdict: ACCEPT
  hard_count: 0
  soft_count: 0
  signal_count: 1
  findings:

    - id: signal-001
      type: flag
      what: "cost_ledger entry cl06 (memory.md line 1406): gain declared as 'political_register-prot +5'; b01c13 draws +1.5 of that total; cost_ledger_anchor: null on all b01c13 axes_in_motion."
      why: "cl06 is a series-level ledger line (anchor: {book: b01, chapter: null, scene: null}), which matches the established pattern — no chapter-level anchor is required here. However, the remaining +3.5 of cl06's gain has no chapter-destination nominated in the current draft. This is not a fault (per the cost_ledger schema, anchor null means the cost/gain is allocated at the event-series level, not per-chapter), but downstream contracts for c14-c16 must draw the balance without double-counting the c13 portion. If cl06's full +5 is treated as a single event at one chapter, a miscount is possible. Signal for showrunner to confirm the per-chapter cl06 draw schedule when authoring b01c14 substance."
      criteria: null

---

## Audit narrative

### Check 1 — Chunk-text-vs-contract

**Scene 1 (The Provisioning Feed):** Claims political_register-prot +0.5. Chunk text describes the provisioning-humiliation observed through compound eyes: the household agent's posture of satisfied coercion, the copper-fraction dispute as exercise-of-power-not-commerce, the supplier's son with the empty crate. The notes field states "resentment-color shifts from ambient to specific-object." The described cause is present and adequate for the claimed +0.5 increment. PASS.

**Scene 2 (The Fly in the Hall):** Claims political_register-prot +0.5 and political_register-world +0.5. For the prot claim: resentment acquires operational specificity through the magistrate proceeding — the apparatus using Taylor's d06 list, Aldric's hands on the table. Cause present. PASS. For the world claim: the stated cause in the notes is "ward-elder pretext charge: Green apparatus operationalizes Taylor's d06 list; succession-enforcement channel advances through this proceeding." The chunk text shows Aldric's name on the d06 list, the pretext charge, the Green-faction clerk setting a document before the proceeding, the magistrate writing before Aldric finishes speaking. The operationalization of the list is on the page. Cause present and adequate. PASS.

**Scene 3 (She Names It):** Claims political_register-prot +0.5. Chunk describes the naming event in full: Taylor holds the two events together, arrives at "contempt" as a verdict with specific evidence (the household agent's body, the magistrate's document order, the ward-elder list), runs the evidence, names it by name, resumes walking. The articulate-contempt threshold is crossed on the page. Cause adequate. PASS.

**Scene 4 (The Halvard Foreclosure):** axes_in_motion: []. No movement claimed. Chunk describes Taylor running the counter-argument, not waiting for Halvard's response, moving on while Halvard is still speaking. The rationale in axes_held for political_register-prot is explicit: "the naming event was scene 3; the foreclosure is the enactment of what the naming makes possible — contempt-without-refusal shape — not a further movement." Consistent with no axis movement claimed. PASS.

---

### Check 2 — Axis-slug validity

All six slugs used across the four scenes and roll-up table:
- political_register-prot: canonical (memory.md state_axes line 156). VALID.
- political_register-world: canonical (memory.md state_axes line 211). VALID.
- moral_framework: canonical (line 90). VALID.
- relational_anchor_status: canonical (line 134). VALID.
- moral_legibility_to_self: canonical (line 145). VALID.
- social_tether-antag: canonical (line 189). VALID.

No unrecognized or invented slugs. PASS.

---

### Check 3 — Schema conformance

Scenes 1, 2, 3: all axes_in_motion entries carry direction (up) and target_delta_magnitude (0.5). Both fields non-null and magnitude > 0. PASS.

All axes_held entries across all four scenes carry rationale strings. No bare entry. PASS.

Scene 4: axes_in_motion is an empty list; axes_held contains five entries with rationale. The schema requirement (≥1 of axes_in_motion/axes_held non-empty) is satisfied by the non-empty axes_held. chapter_class is standard (not frame-coda), and the empty axes_in_motion list is a valid structural choice when all movement was completed in the prior scene and this scene enacts the consequence. No malformed structure. PASS.

---

### Check 4 — stakes_axis membership

- Scene 1: stakes_axis = political_register-prot. Present in axes_in_motion. PASS.
- Scene 2: stakes_axis = political_register-world. Present in axes_in_motion. PASS.
- Scene 3: stakes_axis = political_register-prot. Present in axes_in_motion. PASS.
- Scene 4: stakes_axis = moral_legibility_to_self. axes_in_motion is empty; must be in axes_held. Present in axes_held (b01c13-draft.md line 139). PASS.

---

### Check 5 — Roll-up sum within ±1

Chapter contract (memory.md lines 8029-8038):
- political_register-prot target_delta_magnitude: 1.5
- political_register-world target_delta_magnitude: 0.5

Scene-level sums:
- political_register-prot: S1 +0.5 + S2 +0.5 + S3 +0.5 + S4 0 = **1.5**. Contract = 1.5. Delta = 0. WITHIN ±1. PASS.
- political_register-world: S1 0 + S2 +0.5 + S3 0 + S4 0 = **0.5**. Contract = 0.5. Delta = 0. WITHIN ±1. PASS.

Roll-up table in the draft (b01c13-draft.md lines 161-164) matches these calculations exactly.

---

### Check 6 — chunk_targets bands

Applicable bands (memory.md lines 1463-1464):
- Chapter: delta_per_signature_axis 0.5–1.5; density 0.5–0.9.
- Scene: delta_per_signature_axis 0–1.5; density 0.6–0.9.

Chapter totals: prot 1.5 (within 0.5–1.5); world 0.5 (within 0.5–1.5). Chapter density target stated as 0.6–0.8, within the 0.5–0.9 band. PASS.

Scene totals per axis:
- Scene 1: prot 0.5 (within 0–1.5); density 0.6–0.8 (within 0.6–0.9). PASS.
- Scene 2: prot 0.5, world 0.5 (both within 0–1.5); density 0.6–0.8. PASS.
- Scene 3: prot 0.5 (within 0–1.5); density 0.7–0.9 (within 0.6–0.9). PASS.
- Scene 4: no axes_in_motion; implied delta 0 per axis (within 0–1.5); density 0.6–0.8. PASS.

---

### Check 7 — THEMATIC-AXIS-UNDECLARED (URI-CONTRACT-THEMATIC-AXIS, HARD gate)

Chapter goal (memory.md lines 8051-8052): "Show the audience Taylor naming the contempt with precision and then demonstrating that naming changes nothing about what she does next — the contempt-without-refusal shape at its first appearance."

Thesis axis: political_register-prot.
- Chapter level: declared in axes_in_motion (memory.md line 8029). DECLARED.
- Scene level: declared in axes_in_motion for Scenes 1, 2, 3; declared in axes_held for Scene 4 with explicit rationale tying the foreclosure to the scene-3 naming. FULLY DECLARED across all scenes.

"Naming changes nothing" discipline axis: moral_legibility_to_self.
- Chapter level: declared in axes_held (memory.md line 8045). DECLARED HELD.
- Scene level: declared in axes_held for all four scenes, each with a rationale articulating why recognition-of-repetition is not opening this chapter. It is the stakes_axis of Scene 4. FULLY DECLARED HELD.

No THEMATIC-AXIS-UNDECLARED finding. PASS.

---

### Check 8 — cost_ledger consistency

All b01c13 axes_in_motion carry cost_ledger_anchor: null. The relevant ledger entry for the c13 movement is cl06 (memory.md line 1406-1409): gain "political_register-prot +5"; cost "opportunity-missed: contempt arrives with no exit attached; clarity forecloses nothing." cl06 anchor is {book: b01, chapter: null, scene: null} — a series-level allocation, not chapter-anchored. This is consistent with the c13 contract setting anchor: null; no chapter-level cost entry was required and none was introduced.

No new cost_ledger entries are introduced by the c13 draft. No orphaned anchors. No double-anchored entries. The established ledger is not altered. PASS.

See signal-001 for a downstream note on cl06 draw-schedule.

---

## Summary

| Check | Result |
|-------|--------|
| 1. Chunk-text-vs-contract | PASS — all four scenes |
| 2. Axis-slug validity | PASS — all six slugs canonical |
| 3. Schema conformance | PASS — direction/magnitude non-null, held rationales present, S4 empty axes_in_motion valid |
| 4. stakes_axis membership | PASS — all four scenes |
| 5. Roll-up sum ±1 | PASS — both axes exact match |
| 6. chunk_targets bands | PASS — chapter and scene levels |
| 7. THEMATIC-AXIS-UNDECLARED | PASS — both thesis and discipline axis fully declared |
| 8. cost_ledger consistency | PASS — no orphaned/double-anchored entries |

**Verdict: ACCEPT. 0 HARD findings. 0 SOFT findings. 1 SIGNAL (cl06 draw-schedule advisory; no blocking action required).**
