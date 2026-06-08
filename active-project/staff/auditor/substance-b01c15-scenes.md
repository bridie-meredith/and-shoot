# CHUNK-VS-CONTRACT AUDIT — b01c15 scenes

scope: chapter | target: b01c15 | timestamp: 2026-06-04
reviewer: auditor (/and-substance chapter b01c15 Phase 5)

## Summary
2 faults (both episode-scope, fixable before /and-write Phase 0), 1 flag, 4 passes. No escalations.

## Findings

- finding-001 — PASS — Check 1 chunk-text-vs-contract fidelity: all six in-motion axis claims
  (S1 political_register-prot + capability; S2 social_tether-antag + capability; S3
  relational_anchor_status + social_tether-antag) have physically described causes in chunk text.

- finding-002 — PASS — Check 2 sum roll-up (exact): social_tether-antag +1.5 (S2 0.75 + S3 0.75);
  relational_anchor_status +1.5 (S3); political_register-prot +0.5 (S1); capability +1.0
  (S1 0.5 + S2 0.5). social_tether-prot-rise delivered 0 against HELD target.

- finding-003 — PASS — Check 3 cost-ledger: cl-antag-d03 prior 2.5 (c03 1.5 + c04 1.0) + c15 1.5
  = 4.0 = grant (COMPLETE). cl04 prior 1.0 (c14) + c15 1.5 = 2.5; +0.5 remains declared (no overdraw).
  cl05 gain c12 1.0 + c15 1.0 = 2.0 = grant (COMPLETE); cl05 moral_framework -1 cost paid at c12,
  not re-paid in c15. No double-count.

- finding-004 — PASS — Check 4 THEMATIC-AXIS-UNDECLARED: goal themes map to political_register-prot,
  social_tether-antag, relational_anchor_status, capability (axes_in_motion) + social_tether-prot-rise
  (axes_held). No goal-axis absent from contract.

- finding-005 — FAULT (fault-001) — Check 5: social_tether-prot-rise still in axes_in_motion +0.5 in
  the b01c15 chapter substance_delta block in memory.md (~lines 8789-8800). Scene-level draft correctly
  reconciles to axes_held (aggregate 8.5; c13-c15 HOLD). memory.md chapter-level block not updated.
  WHY: /and-write Phase 0 reads chapter contract from memory.md; will see +0.5 in motion while scenes
  deliver 0 → false SUBSTANCE-FLAT / manual-resolution requirement at bone-gate.
  CRITERIA: move social_tether-prot-rise from axes_in_motion to axes_held in the b01c15 chapter block,
  rationale citing the Phase 0 aggregate-read handoff_conflicts note. Fix before /and-write Phase 0.

- finding-006 — PASS — Check 6: S4 axes_in_motion:[] legitimate (falling accounting-close beat; all
  four chapter moves delivered S1-S3; held axes at documented post-S3 values). Not a dropped move.

- finding-007 — FLAG (flag-001) — S4 scene_conflict.stakes_axis: relational_anchor_status with empty
  axes_in_motion. Per c07s01 precedent, stakes_axis on an empty-in-motion scene is a conflict-frame
  label, NOT a bone-Δ mandate. Advisory for /and-write Phase 1: no relational_anchor_status bone-Δ
  required/permitted in S4. No fixer dispatch.

- finding-008 — FAULT (fault-002) — Check 7: axis-slug literals in chunk narrative body (not YAML):
  S1 "the political_register-prot entry does not change..."; S2 "the social_tether-antag reaches its
  accounting weight here..."; S3 "the relational_anchor_status advances..."; S4 "the
  relational_anchor_status does not change what she does...". Contaminates /and-write Phase 1 event_map
  extraction (slug could survive into bone SVO / Taylor's voiced register; theme-silence + Earth-Bet-
  register risk). S2 highest-risk (POV-proximate, load-bearing).
  CRITERIA: replace all four with plain-language story-content before /and-write Phase 1:
    S1 → "the contempt-register finding she named by c13 deepens by accumulation, not addition"
    S2 → remove/collapse into the existing "the full load of that architecture is in the same reading"
    S3 → "the exclusion acquires a weight it did not carry before — no longer abstract accounting, now a shape the feed shows"
    S4 → "the gap's new visibility does not change what she does with it"
  YAML substance_delta fields unaffected.
