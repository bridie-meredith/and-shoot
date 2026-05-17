---
reviewer: dark-fantasy-reader
facet: state-updates
cycle: 2
episode: s01e02
verdict: revise
---

# Verdict reasoning

The type-mismatch repair on state:5 (oc-broken-maester slice) is confirmed — `anomaly-noted -> phrase-isolated` holds the correct ordinal shape and the field-extension comment names what widened. That flag is closed.

The stance-on-tya-category problem was named in cycle 1 and is not addressed. The entry reads: `@22 actor:oc-tanner-father.stance-on-tya-category: privately-concluded-not-tya -> bodily-committed-withdrawal`. The old-state `privately-concluded-not-tya` is a first-touch on a field-extension with no prior state-update establishing it. The field-extension comment says the field is "new" — which means the old-state is being asserted, not read from a prior canonical entry. The assertion is drawn from the card description ("He has reached a conclusion his wife has not"), but card description is not canonical state. A state-update's old-state must be verifiable from prior state, not inferred from characterization. The card tells us his disposition; a state-update entry's old-state is a claim about what the canonical memory file says. There is no s01e01 state-update establishing `privately-concluded-not-tya` as the exit-state of s01e01 — that field did not exist in s01e01. The correct first-touch form would either (a) leave old-state as `none` (field does not yet exist in canonical memory) with a note that the field is initialized here at first-use, or (b) be defended against the specific s01e01 state-update that established the prior value. As written, the old-state claims a pre-existing canonical value it cannot cite. This is exactly the kind of unverifiable setup-assumption that state-updates is supposed to refuse — a promise to canonical memory that cannot be honored on inspection.

The fauna_control_radius_m @73/@117 beat asymmetry (not my cycle-1 flag; worm-canon's flag and cape-fic noted it) is not a grimdark registration problem. I have no separate concern with the dual-field structure on re-read.

# Entry-level callouts (revise / fail only)

- [state:8] @22 — old-state `privately-concluded-not-tya` is asserted without a prior canonical state-update entry establishing it. Field-extension with a card-characterization derivation is not the same as a verifiable prior value. Either anchor to a specific s01e01 state-entry (which does not exist; the field was not tracked in e01), or correct the old-state to `none` with an initialization note, or delete and flag for margit card-schema work.

# Convergence trace (orchestrator-critic input)

The mechanical auditor (audit r3) did not flag state:8. The old-state verification problem is not a schema-format violation detectable by the mechanical scan — it is a canonical-memory-integrity question the auditor does not exercise. No convergence with audit findings. This is an audience-only callout at Phase 5b.
