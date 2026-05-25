=== auditor review — b01 draft ===
scope: book
target: b01
timestamp: 2026-05-24

---

hard_findings:

  - finding_id: fault-001
    class: LEDGER-MISMATCH
    target: b01c10 substance_delta.axes_in_motion[position-world].cost_ledger_anchor
    severity: HARD
    description: >
      b01c10 cites cl-world-d07 as the anchor for a position-world +1.0 gain. The
      ledger entry cl-world-d07 gain is "political_register-world +2" — it covers
      political_register-world, not position-world. The correct anchor for a
      position-world draw is cl-world-d04 (gain: position-world +2, journey-required
      cl03a) or cl07b (gain: position-world +2). cl-world-d04 has only 1.0 drawn
      against its 2.0 gain at this point (b01c04), leaving 1.0 available. The
      misattribution is not arithmetic-breaking (the totals still sum to 4.0) but the
      per-entry accounting is wrong: cl-world-d07 is being charged for a movement it
      does not cover, and cl-world-d04's remaining balance is undocumented.
    criteria: >
      b01c10 position-world cost_ledger_anchor must reference a ledger entry whose
      stated gain type is position-world (either cl-world-d04 or cl07b). cl-world-d07
      may remain as the anchor for b01c10 political_register-world (that use is correct).

  - finding_id: fault-002
    class: LEDGER-MISMATCH
    target: b01c14 substance_delta.axes_in_motion[social_tether-antag].cost_ledger_anchor + b01c15 same
    severity: HARD
    description: >
      cl-antag-d10 is stated in the ledger as gain: "social_tether-antag +4." Chapters
      drawing against it: b01c10 +1.5, b01c11 +1.0, b01c14 +1.5, b01c15 +1.5 = 5.5
      total drawn against a +4 gain entry. The overdraw is 1.5 ranks. Both b01c14 and
      b01c15 note "cl-antag-d10 completed" — a double-completion claim against the same
      ledger entry — which is the symptom of the overdraw. The total book-level social_
      tether-antag sum (8.0) is within tolerance, but it is partially sourced from an
      overdrawn ledger entry rather than a named gain source.
    criteria: >
      Either the cl-antag-d10 gain entry must be revised upward to cover the full 5.5
      draw, or one chapter among b01c10/c11/c14/c15 must redirect its social_tether-antag
      draw to a different anchor (e.g., cl-antag-d03 has 1.5 underdraw capacity remaining:
      2.5 drawn vs. +4 gain). Only one chapter may claim completion of cl-antag-d10.

  - finding_id: fault-003
    class: LEDGER-MISMATCH
    target: b01c14 substance_delta.axes_in_motion[position-prot-rise].cost_ledger_anchor
    severity: HARD
    description: >
      cl-d07a is stated in the ledger as gain: "position-prot-rise +2." Chapters drawing
      against it: b01c10 +1.5 (notes "cl-d07a opens") and b01c14 +1.0 (notes "cl-d07a
      completed"). Total drawn: 2.5 against stated gain of +2.0. Overdraw of 0.5 ranks.
      b01c14 cannot close a ledger entry that was already exhausted by b01c10's 1.5 draw.
    criteria: >
      Either the cl-d07a gain entry must be revised to +2.5 or higher, or b01c10 must
      reduce its draw to 1.0 (leaving 1.0 for b01c14), or b01c14 must redirect its
      position-prot-rise draw to a different anchor with remaining capacity. Only one
      chapter may carry the "cl-d07a completed" note.

  - finding_id: fault-004
    class: LEDGER-MISMATCH
    target: b01c17 substance_delta.axes_in_motion[moral_framework].cost_ledger_anchor (cl05)
    severity: HARD
    description: >
      cl05 is stated in the ledger as cost: "moral_framework -1." Chapters drawing
      against this cost: b01c12 moral_framework -1.0 (anchor cl05, notes "cl05 cost
      side") and b01c17 moral_framework -1.0 (anchor cl05, notes "third material breach
      in the cascade sequence"). Total cost drawn: -2.0 against stated cost of -1.0.
      Overdraw of 1.0 rank. The book-level moral_framework total (-6.0) is arithmetically
      correct only because cl02 is underdrawn (-2.0 drawn vs. -3.0 cost). The
      per-entry accounting is wrong regardless of the aggregate.
    criteria: >
      Either cl05 cost must be revised to moral_framework -2, or b01c17 must redirect
      its moral_framework draw to a ledger entry with remaining cost capacity (cl02 has
      -1.0 remaining; cl03a has -1.0 remaining). b01c12 may retain cl05 as anchor.

---

soft_findings:

  - finding_id: flag-001
    class: INFERENTIAL-ANCHOR
    target: b01c07 substance_delta.axes_in_motion[political_register-prot].cost_ledger_anchor (null)
    severity: SOFT
    description: >
      b01c07 political_register-prot +0.5 has no cost_ledger_anchor. The ledger entry
      cl-d05 covers political_register-prot +3 (the resentment-becomes-permanent anchor).
      A sub-advance with mechanism described in notes but no anchor ID is inferentially
      attached. Not blocking — mechanism is named.

  - finding_id: flag-002
    class: INFERENTIAL-ANCHOR
    target: b01c07 substance_delta.axes_in_motion[social_tether-prot-rise].cost_ledger_anchor (null)
    severity: SOFT
    description: >
      b01c07 social_tether-prot-rise +1.0 has no cost_ledger_anchor. The applicable
      ledger entries are cl01b (+2 gain, journey-required cl01a) and cl03b (+4 gain,
      future-cost collateral). The Halvard encounter mechanism is named in notes
      ("deepens Taylor's precinct social embedding"), which addresses rank-claim-without-
      cause, but the ledger attachment is inferred not declared. Carry-forward from
      series-level flag-001 (cl-d08b inferential anchor chain). Not blocking.

  - finding_id: flag-003
    class: INFERENTIAL-ANCHOR
    target: b01c09 substance_delta.axes_in_motion[relational_anchor_status and political_register-prot] (null anchors)
    severity: SOFT
    description: >
      b01c09 carries two sub-advances (relational_anchor_status +0.5, political_register-prot
      +0.5) both with null anchors. Mechanisms are named in notes. Not blocking — both are
      sub-increments within the trajectory of established ledger entries (cl-d08 and cl-d05
      respectively), but the ledger connection is inferential.

  - finding_id: flag-004
    class: INFERENTIAL-ANCHOR
    target: b01c11 substance_delta.axes_in_motion[political_register-world].cost_ledger_anchor (null)
    severity: SOFT
    description: >
      b01c11 political_register-world +0.5 has no anchor. The ledger entry cl-world-d07
      (gain: political_register-world +2) is the applicable entry and has remaining
      capacity after b01c10's 1.0 draw. Mechanism is described (courier detention
      leveraged for succession-channel consolidation). Not blocking.

  - finding_id: flag-005
    class: INFERENTIAL-ANCHOR
    target: b01c13 substance_delta.axes_in_motion[political_register-prot and political_register-world] (null anchors)
    severity: SOFT
    description: >
      b01c13 carries political_register-prot +1.5 and political_register-world +0.5,
      both null-anchored. cl-d05 (remaining capacity) and cl-world-d07 (remaining
      capacity) are the applicable entries. Mechanisms detailed in notes; the
      articulate-contempt threshold event is the cause. Not blocking.

  - finding_id: flag-006
    class: INFERENTIAL-ANCHOR
    target: b01c15 substance_delta.axes_in_motion[relational_anchor_status and social_tether-prot-rise] (null anchors)
    severity: SOFT
    description: >
      b01c15 relational_anchor_status +1.5 (no anchor; cl04 has remaining capacity) and
      social_tether-prot-rise +0.5 (no anchor; cl-d08b has remaining capacity) are both
      null-anchored. Mechanisms named in notes. Not blocking.

  - finding_id: flag-007
    class: INFERENTIAL-ANCHOR
    target: b01c17 substance_delta.axes_in_motion[capability].cost_ledger_anchor (null)
    severity: SOFT
    description: >
      b01c17 capability +1.0 has no anchor. cl05 gain side (capability +2) was cited in
      b01c12 and b01c15 (totaling 2.0, which exhausts cl05 gain). If cl05 gain is
      exhausted, capability +1.0 at b01c17 has no open ledger entry to draw from. This
      compounds fault-004: cl05 is simultaneously overdrawn on cost and fully drawn on
      gain. The capability draw here may need to open a new ledger entry or redirect.
      Elevated from pure inferential — the null anchor here may reflect an unresolved
      ledger gap rather than a simple omission. Monitor if fault-004 is fixed.

  - finding_id: flag-008
    class: NAMING-INCONSISTENCY
    target: b01-draft.md roll-up comment block (lines 1698-1704)
    severity: SOFT
    description: >
      The roll-up correction note states "b01c07 has social_tether-prot-rise in axes_held
      (held flat)" and proposes promoting it to axes_in_motion. However the actual b01c07
      YAML already places social_tether-prot-rise in axes_in_motion at +1.0. The note
      describes a fix that has already been applied. The note is self-contradictory and
      misleading — a reader following the roll-up block as an action list would believe a
      fix is still required. Not blocking; no YAML action needed.

  - finding_id: flag-009
    class: NAMING-INCONSISTENCY
    target: b01c20 chunk text vs. substance_delta.axes_in_motion[relational_anchor_status].target_delta_magnitude
    severity: SOFT
    description: >
      The b01c20 chunk narrative summary ("What shifts") states relational_anchor_status
      +1.5 but the YAML target_delta_magnitude field is 2.0. The YAML is the authoritative
      binding field; the chunk text is prose and non-binding. No mechanical consequence,
      but the discrepancy would create confusion at /and-write when the screen-writer reads
      the "What shifts" summary against the YAML.

  - finding_id: flag-010
    class: INFERENTIAL-ANCHOR
    target: b01c04 substance_delta.axes_in_motion[position-prot-rise].notes (premature completion claim)
    severity: SOFT
    description: >
      b01c04 position-prot-rise +1.0 cites cl02 with note "cl02 gain completed." The
      cl02 gain is position-prot-rise +4. b01c04 draws only 1.0 at that point (prior
      draws from cl02 gain: b01c03 position-prot-rise +1.0 = 2.0 total vs. +4 gain).
      The completion claim is premature — 2.0 of 4.0 remains. The actual completion
      of cl02 gain occurs across later chapters. Not blocking but the "completed" note
      will mislead future-chapter authors at /and-write.

---

aggregate: REVISE (4 HARD)

notes:
  Four HARD ledger-mismatch faults require resolution before /and-write proceeds.
  All four are per-entry overdraw or wrong-type citation problems; none requires
  restructuring the chapter arc or the book substance_delta targets. The aggregate
  totals across all 12 axes are within ±1 tolerance (per the roll-up check), so the
  arithmetic is salvageable by ledger-entry adjustment rather than chapter restructuring.

  The most constrained fix is fault-002 (cl-antag-d10 overdraw): redirect 1.5 of the
  social_tether-antag draws from cl-antag-d10 to cl-antag-d03, which has 1.5 of
  remaining capacity (c03 + c04 drew 2.5 vs. +4 gain). This keeps totals intact.

  Fault-004 (cl05 cost overdraw) and flag-007 (cl05 gain exhausted but b01c17 capability
  draw is null-anchored) are linked: if cl05 is the only cost entry funding b01c17
  moral_framework, and cl05 cost is -1 but two chapters draw from it, one chapter needs
  to redirect to cl02 (underdrawing -1.0 remaining) or cl03a (underdrawing -1.0 remaining).
  b01c17's null-anchor capability draw also needs a new ledger entry or an explicit note
  that it draws from a trajectory not yet given a named entry.

  Carry-forward series flags (flag-001 on cl-d08b inferential anchor) remain non-blocking
  at book level. All three carry-forward obligations (cf-wren-d14-perceptual-mechanism,
  cf-d10-courier-face, cf-rhaenyra-pressure-staging) are resolved in the chapter contracts.
  Slug sequence, POV, schema fields, and thematic-axis coverage all pass.
