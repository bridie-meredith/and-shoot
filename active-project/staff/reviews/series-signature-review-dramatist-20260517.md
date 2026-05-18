# series-signature-review — dramatist — 2026-05-17

project: taylor-hebert-westeros-good-intentions
scope: series + book b01 chunk, substance_delta, cost_ledger, chunk_targets, antagonist_pressure
reviewer: dramatist

---

verdict: REVISE — 5 structural issues; 2 are schema-contradictions that block clean downstream authoring.

---

## Structural shape — overall

Shape: rise-peak-fall. PASSES.

d01–d12: rise. Stakes accumulate across all 9 axes. Each delta point closes off a prior option (d03 first-trade → d07 irrevocable-instrument → d10 no-exit-confirmed → d12 full-deployment). Try-fails are load-bearing: the exit calculation at d10 costs Taylor the ability to pretend extraction is possible. Antagonist pressure is a force with its own moves (Otto's ask-ratchet is priced below refusal-threshold by design, compounds each accepted trade). Peak at d12: network is structural to Greens' intelligence picture, protect-target survives, architecture irrevocable. No rollback possible. Fall: d13–d14. Resolution discharges exactly the stakes set up: cost-bearer dies in the street Taylor charted; ledger delivers final output; contempt is the recognition that came too late. End state ≠ start state on all 9 axes.

b01 chunk: collision-language honored. "The first trade is the auditable mistake that makes the rest of them necessary" is the right register — not synopsis. Chunk names real collision (refusal-of-control vs. Otto's offer), names what cannot survive (the prohibition), names the stakes (cost-bearer burns / protect-target dies / war comes). Sound.

Sum-roll-up: clean. book_count=1, b01 IS the series arc. All 9 axes: direction and magnitude in book substance_delta match series start_rank→end_rank exactly.

Structural commitments: all honored. Single POV ✓. world_evolution=evolving ✓. series_end_shape=tragic ✓. chapter_count correctly deferred to /and-substance book b01.

---

## Issues requiring revision

### Issue 1 — chunk_targets floor self-contradiction [BLOCKING]
Location: `substance.chunk_targets` + `books[0].substance_delta.axes_in_motion`

The tuning note lowered delta_per_signature_axis floor from 4→3. Two axes in the declared signature fall below 3:
- social-tether: target_delta_magnitude 1 (2→1)
- moral-framework: target_delta_magnitude 2 (3→1)

The plan contradicts itself. Fix: one of
(a) lower the floor to 1 and update the tuning note explicitly permitting small-magnitude loss moves as signature axes;
(b) reclassify social-tether and moral-framework as support axes at series level (consequence axes, not primary dramatic axes);
(c) re-examine start_rank assignments for these axes to see if the spread is too narrow.

### Issue 2 — cl-knowledge-contempt is tautological [BLOCKING for scene authoring]
Location: `cost_ledger.cl-knowledge-contempt`

Entry declares gain: knowledge +1, cost: political-register-toward-elite +1; description confirms they are "the same event." A cost-ledger entry requires gain = something wanted, cost = something paid as separate transactions. This entry describes a correlation, not a trade. A scene-level author using this as a cost-gate finds no dramatizable tension: the character cannot get knowledge without also getting contempt, so there is no moment of exchange to stage.

Fix: replace with a ledger entry that has genuine trade structure. Candidate: the cost of each intelligence delivery (knowledge gain) is extension of the arrangement that makes her non-extractable (agency −1). Contempt becomes an axis moving independently via the d05/d09/d13 delta sequence — it does not need a ledger entry binding it to knowledge, because it is not a trade; it is a consequence.

### Issue 3 — cl-protection-buys-consolidation direction contradiction [BLOCKING]
Location: `cost_ledger.cl-protection-buys-consolidation`

Entry declares gain: relational-anchor-status +1. Series trajectory has relational-anchor-status (protagonist) at start_rank: 3, end_rank: 1 — net down. Axis nine_means: "fully priced + held openly + entered as a protected node" (best outcome). A +1 gain direction says the relationship moves toward the protected node — but the locked end state and every d-number in the trajectory move away from it.

The description conflates two relational objects: protect-target's survival and cost-bearer's ledger position. These are different things. The axis tracks cost-bearer. Each trade extending protect-target's protection does not move cost-bearer toward the ledger — it moves further from it (Taylor keeps refusing to price them).

Fix: clarify which relationship this entry tracks. If protect-target's survival, that is a different axis or a sub-dimension not defined in the signature. If cost-bearer's ledger position, the gain direction is wrong — reverse to −1 (each protect-target extension is another deferral of cost-bearer's entry into the ledger).

### Issue 4 — cl-social-tether-build axis semantics ambiguity [FLAG]
Location: `cost_ledger.cl-social-tether-build`

Entry: gain: social-tether +1 / cost: position +1. Both recorded as directional rises. Description explains position rising is the trap (visibility = non-extractable). But position axis five_means reads as ambiguously useful, not dangerous. A downstream author reads two gains, not a gain and a cost.

Fix: add an inline note to the cost field confirming position rising is a cost in this context (higher position = more legible to Otto = less extractable). Alternatively, revise position axis five_means to make the midpoint structurally dangerous, not neutral.

### Issue 5 — position axis doing double work [FLAG]
Location: `state_axes` (position, protagonist) + `series-trajectory.md` d03, d07, d10, d14

The rise (d03→d07) tracks court-visibility / patron-recognition. The fall (d10→d14) tracks extraction-viability / structural-entrapment. These are distinct dimensions sharing one label. The 0-net (1→5→1) is numerically accurate but semantically false: what ends at 1 (expelled) is not the same dimension as what started at 1 (anonymous). This does not corrupt the trajectory — the d-sequence tells the right story — but will produce confused axis-gate checks at /and-write Phase 6 when a bone is checked against "position" without knowing which sub-dimension is active.

Fix: either
(a) split into two axes — "court-visibility" (rises d01–d09) and "extraction-viability" (collapses d10–d14);
(b) add a sub-dimension note to the position axis definition distinguishing visibility-phase (d01–d09) from entrapment-phase (d10–d14) for bone-gate reviewers.

---

## Non-issues confirmed

- Antagonist pressure: 4 entries, 4 structurally distinct curves. No collapse. Pass.
- cl-unpriced-cost-bearer: self-labeled STRUCTURAL ERROR ENTRY with no realized gain — defensible design statement for loss-arc tragedy. Pass with note: scene-level cost-gate use requires downstream author to understand both fields record losses.
- cl-otto-trade: structurally real. Pass.
- cl-network-position: structurally real (cage mechanic). Pass.
- Sum-roll-up: clean on all 9 axes. Pass.
- Series structural commitments: all honored. Pass.
- b01 chunk register: collision-language, not synopsis. Pass.

---

issues: 5
blocking: 2 (Issue 1, Issue 3)
flagged-blocking-for-downstream: 1 (Issue 2)
flagged: 2 (Issue 4, Issue 5)
