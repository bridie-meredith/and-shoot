# /and-write phase 2 audit — b01c02

scope: 25 bones across 3 scenes (s01:10, s02:8, s03:7)
date: 2026-05-21

---

## verdict

FAIL — 5 findings (4 faults, 1 flag)

---

## findings

### FAULT-FORM

- bone: b01c02s01n03
  svo: the water-carrier steps into the doorway
  reason: "steps into" is a prepositional phrase of destination, banned by the modifier rule; the correct form uses a transitive verb that takes the destination as direct object.
  fix-hint: replace with `the water-carrier enters the doorway` or equivalent transitive-destination form.

- bone: b01c02s01n08
  svo: the two witnesses face the alley-mouth
  reason: "the two witnesses" is a grammatical plural, not a singular subject; the schema requires subjects to be singular; "the two witnesses" as subject is the same structural violation as "taylor and rowan walk."
  fix-hint: recast to a single subject — choose one witness as the primary actor (e.g., `the near witness faces the alley-mouth`) or reframe as `a witness faces the alley-mouth`.

- bone: b01c02s02n05
  svo: the two witnesses cross the lane
  reason: same multi-subject violation as s01n08 — "the two witnesses" is plural, not singular.
  fix-hint: recast to singular subject: `a witness crosses the lane` or equivalent.

- bone: b01c02s03n04
  svo: taylor-hebert-kl-122ac strikes the line
  shape: held
  reason: shape `held` is contradicted by SVO `strikes the line`, which is a discrete action verb, not a stillness-against-pressure hold. Held bones require a holds/stillness SVO. Additionally, the axes_held rationale invokes "licensed holds form on body part" but the object `the line` is a ledger mark, not a body part of the subject and not a physical object resisting external pressure — so even if recast as a holds-verb, the narrow holds license would not apply.
  fix-hint: the bone must either (a) be reclassified to shape `moving` with axis_moves instead of axes_held, and the capability/moral-framework discipline registered elsewhere, or (b) the SVO must be replaced with a genuine stillness-against-pressure hold on a body part (e.g., `taylor-hebert-kl-122ac holds the hand`). The narrative function — closing the ledger entry as restraint — should be preserved in the replacement SVO's physical anchor.

- bone: b01c02s03n06
  svo: taylor-hebert-kl-122ac holds the pen
  reason: "the pen" is neither a body part of the subject nor a physical object resisting external pressure; the narrow holds license is not satisfied. The schema licenses `holds` for (1) a body part of the subject under stillness-against-pressure, or (2) a physical object braced against an opposing force. A pen held motionless above a page fails both criteria — the pressure is internal/narrative, not an external physical force acting on the pen.
  fix-hint: the SVO must be recast to a licensed holds form (body part: e.g., `taylor-hebert-kl-122ac holds the hand`) or replaced with a different physical stillness anchor that does not use `holds` with a non-body-part object.

### FAULT-BONE-DELTA-MALFORMED

- bone: b01c02s01n10
  svo: coll-net-mender-flea-bottom works the net
  reason: cost_ledger_anchor is cl-social-tether-build, whose declared gain/cost axes are social-tether/position. The bone's axis_moves declare knowledge up magnitude 1. Knowledge appears in neither gain nor cost axis of the anchor. The anchor does not match any axis this bone moves, making the ledger linkage incoherent. (Note: knowledge IS in the scene's axes_in_motion, so this is not a scene-scope fault; it is the anchor-to-bone-axis mismatch that fails.)
  fix-hint: either (a) remove the cost_ledger_anchor from this bone — knowledge gains in this scene are unanchored per the scene substance_delta — or (b) change the bone's axis_moves to social-tether if the narrative intent is social-cover-as-tether-confirmation, which would make the cl-social-tether-build anchor valid.

### FLAG

- bone: b01c02s02n02
  svo: coll-net-mender-flea-bottom pulls the net
  shape: held
  axes_held: capability
  reason: the bone's axes_held carry Taylor's capability axis with a non-Taylor subject (Coll). The schema does not explicitly prohibit this, but the held-axis pattern in b01c01 and b01c02 has consistently used the subject's own body or the protagonist's own body to anchor the hold. Coll carrying Taylor's capability-held axis via proxy enacts a structurally valid narrative reading (mirroring) but could be misread at facet-authoring time as Coll possessing a capability axis of his own. This is a flag, not a fault — the fixer should not change it; facet authors should be aware the axes_held here is proxy-relational, not subject-direct.
  fix-hint: no change required; note for facet-authoring team that the capability hold here is Taylor's baseline (rank 4) carried through Coll's resumption of work, not Coll's own capability axis.

---

## scale-interpretation ruling

**Ruling: bone magnitudes are sub-rank ticks, not full ranks. 1 tick = 0.1 rank.**

Rationale:

The scene-level substance_delta entries in showrunner memory declare fractional target_delta_magnitudes (s01 capability +1.0, knowledge +0.2, social-tether +0.1; s02 social-tether +0.3, knowledge +0.2; s03 social-tether +0.1, knowledge +0.1). These are not whole-rank numbers. If bone magnitudes were full ranks, a single bone with magnitude 1 would move an axis one full rank, and the scene aggregate would be the count of bones on that axis — producing scene aggregates of 3-7 ranks on knowledge in s01, which is incoherent against a target of +0.2.

The /and-substance chapter Phase 5 PASS (audience 3-of-3, dramatist ACCEPT, auditor ACCEPT per memory line 1061-1062) was achieved with these fractional targets in place. The system accepted sub-rank fractional scene targets at that gate. The downstream evidence is unambiguous: the targets were authored and passed as sub-rank fractional values.

Therefore: bone magnitude 1 = 0.1 rank-unit. The chunk_targets.bone band `delta_per_axis: 1-3` means 0.1 to 0.3 rank-units per bone per axis. This is the interpretation Phase 6 aggregate-Δ checks must use.

**Aggregate-Δ summary under this interpretation (Phase 2 surface only; Phase 6 owns the HARD/SIGNAL classification):**

s01:
- capability: 3 ticks = 0.3 rank vs target 1.0 (gap -0.7 — within ±1 of target)
- knowledge: 7 ticks = 0.7 rank vs target 0.2 (gap +0.5 — within ±1 of target; note: 6 ticks if s01n08 is fixed as a single-subject bone, still 0.6 vs 0.2, gap +0.4, still within ±1)
- social-tether: 1 tick = 0.1 rank vs target 0.1 (exact)

s02:
- social-tether: 4 ticks = 0.4 rank vs target 0.3 (gap +0.1 — within ±1)
- knowledge: 3 ticks = 0.3 rank vs target 0.2 (gap +0.1 — within ±1; note: 2 ticks if s02n05 is fixed as single-subject, 0.2 vs 0.2, exact)

s03:
- knowledge: 3 ticks = 0.3 rank vs target 0.1 (gap +0.2 — within ±1)
- social-tether: 1 tick = 0.1 rank vs target 0.1 (exact)

All scene aggregates are within ±1 of their targets under this interpretation. No HARD aggregate-Δ faults are surfaced at Phase 2. Phase 6 will confirm with SIGNAL/HARD classification.

---

## bones cleared

b01c02s01n01, b01c02s01n02, b01c02s01n04, b01c02s01n05, b01c02s01n06, b01c02s01n07, b01c02s01n09, b01c02s02n01, b01c02s02n02 (flag only), b01c02s02n03, b01c02s02n04, b01c02s02n06, b01c02s02n07, b01c02s02n08, b01c02s03n01, b01c02s03n02, b01c02s03n03, b01c02s03n05, b01c02s03n07
