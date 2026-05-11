---
reviewer: cape-fic-reader
facet: state-updates
cycle: 2
episode: s01e02
date: 2026-05-11
verdict: accept
---

# Verdict reasoning

The type-mismatch on state:5 (oc-broken-maester slice, consolidated) is confirmed repaired — old-state `anomaly-noted` and new-state `phrase-isolated` are both string ordinals on the same documentation-sharpening axis. The field-extension comment names the widening explicitly; the anti-pattern defenses are present and specific. The broken-maester slice is clean.

The fauna_control_radius_m split across @73 (studio.fauna_sense_status.operational_radius) and @117 (actor:taylor-hebert-flea-bottom.fauna_control_radius_m) was noted in cycle 1 as an asymmetry. On re-read: these are two legitimately distinct tracked fields — the studio target tracks the operational field-state of the shard's active radius (environment-side, relevant for downstream encounters), and the actor target tracks Taylor's known and explicitly recorded radius (knowledge/capability-side, what she logged at @122). The two fields answer different questions and carry forward to different consumers. A reader tracking what Taylor can do vs. what the world-state registers as her operational footprint would want both. This is not a duplication; it is a dual-write that cape-fic style coverage of a power-state change requires. The @73/@117 gap is load-bearing: the env entry fires when the network achieves the radius; the actor entry fires when Taylor confirms and logs it at @117. The split earns its keep.

The state:8 stance-on-tya-category ungrounded old-state (dark-fantasy flag, cycle 1, not addressed) is not this reader's hard concern. The old-state `privately-concluded-not-tya` is a first-touch extension on oc-tanner-father and is defensible as a setup-assumption from s01e01 prior episode — the field did not change in s01e01, so the first-touch is the pre-episode state carried from the prior episode's characterization. Cape-fic accepts this: the card is explicit ("He has reached a conclusion his wife has not"), and the old-state simply names what the card establishes as his entry-state. The field-extension comment is present.

Overall the state-updates graph tracks a rule-legible expansion event with correctly split dual-field writes, a load-bearing grief-closure record, and a documentation-sharpening write-back that earns its notation. The asymmetry flag is answered; the type-mismatch is repaired. Accept.

# Entry-level callouts (revise / fail only)

None.

# Convergence trace (orchestrator-critic input)

No callouts to trace against Phase 5 audit findings. The state:5 type-mismatch fix was confirmed clean in audit r3 (Item 5 verification). The fauna_control_radius_m @73/@117 asymmetry was not flagged as HARD or SIGNAL in any audit pass (not a mechanical issue, an interpretation question). The stance-on-tya-category old-state was not raised in the mechanical audit.
