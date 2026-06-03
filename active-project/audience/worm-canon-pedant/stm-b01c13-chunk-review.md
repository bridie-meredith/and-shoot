## b01c13 /and-substance chapter Phase 5 chunk review — 2026-06-03

chapter: b01c13
reviewer: worm-canon-pedant
date: 2026-06-03
phase: substance-chapter-chunk-review
dispatch: 3-persona chunk-quality review (hinge chapter; contempt-without-refusal first appearance)

verdict_per_scene:
  b01c13s01: SUBSTANCE-FELT
  b01c13s02: SUBSTANCE-FELT
  b01c13s03: SUBSTANCE-FELT
  b01c13s04: SUBSTANCE-FELT

hard_findings: none
SUBSTANCE-FLAT: none
SUBSTANCE-SUSPECT: none

chapter_verdict: SUBSTANCE-FELT
overall: ACCEPT

### Earth-Bet proper-noun fence check

Full four-scene scan. Result: CLEAN.

- Khepri name: absent from all four scenes. s3 naming event produces the word "contempt." Not Khepri. No Khepri surfacing this chapter. Correct per aggregate-state c12 pattern (c12 suppression was the last/most-intense pre-opening event; c13 is a separate arc).
- Worm-specific jargon: absent. No Thinker rating, no trigger event, no shard, no Manton effect, no cluster trigger, no parahuman taxonomy terms.
- Earth-Bet location names: absent.
- Feed vocabulary: "compound eyes," "blowfly," "the feed," "passive layer," "compound-eye witness," "fly," "feed-record" — all functional-descriptive, within established project register. Clean.

### Khepri suppression check

s3 specifically reviewed. The naming event produces "contempt." Not a Khepri-shape recurrence. The mechanism language ("the specific way the apparatus uses the smallfolk as friction-surface") is feed-reading/political-register language, not shard-awareness language. Inner-monologue-rare cap untested (no Gold Morning reference). CLEAN.

### d06 list → Aldric continuity check

Aggregate-state confirms moral_framework -1.0 at c06 for "first named-person delivery." The substance-delta note reads: "a ward-elder whose name is on the list Taylor delivered to Jarvis at d06 — she knew him as [force: black-faction-adjacent-ward-elder] by pattern-inference, not certainty." This matches the aggregate-state c06 entry exactly ("first named-person delivery"; Black-sympathizer network language). Pretext charge is "receiving stolen cord" — correctly a pretext (apparatus using intelligence for enforcement without Taylor delivering a direct accusation). Continuity clean.

### Character-knowledge checks

- Taylor knows Aldric is on her list: she put him there. No unmotivated knowledge.
- The magistrate has a Green-faction clerk's document: plausible given Taylor's list traveled through Jarvis (Green conduit). Taylor does not know the specific transmission path; she reads the proceeding and infers the connection. Correct epistemic scope.
- Halvard does not know Taylor is responsible: correct. He says "someone made a determination about this man from outside the precinct." He does not name Taylor. He does not know. Clean.

### Halvard continuity

Prior encounters at "d07, d09" (in-narrative dating). Memory.md confirms Halvard encounters at c07 and c09 (the d07/d09 within-narrative events map to the correct chapters). Pattern-of-prior-encounters correctly built. No new information in Halvard's mouth that exceeds his in-world knowledge. Clean.

### political_register-world handoff discrepancy (DOCUMENTATION FLAG — not a substance finding)

Aggregate-state shows political_register-world at rank 6.5 entering c13. Chapter adds +0.5 (Scene 2). Correct handoff_out value: 7.0.

memory.md handoff_out (line 8079) reads "political_register-world rank 8." This does not match.

Root cause: memory.md handoff_in (line 8065) carries "political_register-world rank 7.5" — a stale/incorrect entering value. The handoff_out 8 was computed as 7.5 + 0.5, not as 6.5 + 0.5. The aggregate-state measured value (6.5) is authoritative.

Classification: DOCUMENTATION ERROR in the handoff narrative. The per-scene delta allocation is correct (+0.5 in Scene 2, confirmed in the roll-up table). This is not a chunk-substance finding and does not block proceed. It is a continuity documentation error that must be corrected in memory.md before /and-write to prevent the handoff_out stale-number from propagating into the c13→c14 boundary.

Corrected handoff_out value: political_register-world rank 7.0 (aggregate-state 6.5 + c13 delta +0.5 = 7.0).

### Axis aggregate check (against chapter contract)

| axis | scene 1 | scene 2 | scene 3 | scene 4 | total | contract | match |
|------|---------|---------|---------|---------|-------|----------|-------|
| political_register-prot | +0.5 | +0.5 | +0.5 | — | +1.5 | +1.5 | EXACT |
| political_register-world | — | +0.5 | — | — | +0.5 | +0.5 | EXACT |

Math tracks. No over-delivery. No shortfall.

### Held-axis continuity check

- moral_framework held at -2 across all four scenes: correct per aggregate-state (last movement b01c12; observation is not a breach event in Taylor's accounting; she watches but does not file a new breach column entry)
- relational_anchor_status held at 4.5 across all four scenes: correct (Wren not in scene; no new weight added)
- moral_legibility_to_self held at 5.5 across all four scenes: correct (contempt directed outward; recognition-of-repetition not opened; Taylor runs evidence against the apparatus, not against the ledger)
- social_tether-antag held at 6 across all four scenes: correct (Halvard has no lever on Otto's channel; foreclosure is Taylor-unilateral)

All held-axis values consistent with aggregate-state entering values.

### Canonicity confirmation

The contempt-naming event is canonically Taylor. She uses her own evidentiary standard to evaluate the word before accepting it. She runs the evidence. This is the ledger-register applied to an internal state — correct pattern. "It is a finding, not a decision" — correct Taylor accounting taxonomy (the ledger opens on decisions; findings are classified separately). Taylor resumes walking. This is the contempt-without-refusal shape: the finding does not change the route. Taylor-register accurate throughout.

### Corrections required before /and-write

HARD: none.
SOFT:
  - handoff_out political_register-world in memory.md must be corrected from 8 to 7.0 before /and-write; the handoff_in entering value (7.5 in memory.md) is also stale against aggregate-state (6.5); both should be reconciled to aggregate-state authority

### Running tally

b01c01 through b01c13: 0 Earth-Bet fence violations. 0 Khepri-name leaks. 0 power-mechanic overshoot findings. 0 character-knowledge lore-leaks. 1 documentation continuity error (handoff_out political_register-world rank; correctable before /and-write).
