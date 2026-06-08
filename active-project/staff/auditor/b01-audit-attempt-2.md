=== auditor re-review — b01 draft attempt 2 ===
scope: book
target: b01
timestamp: 2026-05-24
prior_report: active-project/staff/auditor/b01-audit.md

---

attempt-1 HARD findings resolution:

  fault-001 (b01c10 position-world wrong-type anchor cl-world-d07):
    status: RESOLVED
    basis: b01c10 position-world cost_ledger_anchor is now cl-world-d04 (gain: "position-world +2").
           cl-world-d04 draws: b01c04 +1.0 + b01c10 +1.0 = 2.0 vs. stated gain +2. Balanced.

  fault-002 (cl-antag-d10 overdraw 5.5 vs. +4; double-completion):
    status: RESOLVED
    basis: b01c15 social_tether-antag anchor changed to cl-antag-d03.
           cl-antag-d03 draws: b01c03 +1.5 + b01c04 +1.0 + b01c15 +1.5 = 4.0 vs. stated gain +4. Balanced.
           cl-antag-d10 draws: b01c10 +1.5 + b01c11 +1.0 + b01c14 +1.5 = 4.0 vs. stated gain +4. Balanced.
           Single completion claim for cl-antag-d10 (at c14 only). Single completion claim for
           cl-antag-d03 (at c15). No double-completion.

  fault-003 (cl-d07a overdraw 2.5 vs. +2; b01c10 1.5 draw):
    status: RESOLVED
    basis: b01c10 position-prot-rise target_delta_magnitude reduced 1.5 → 1.0.
           cl-d07a draws: b01c10 +1.0 + b01c14 +1.0 = 2.0 vs. stated gain +2. Balanced.

  fault-004 (cl05 cost overdraw -2.0 vs. -1; b01c17 anchor cl05):
    status: RESOLVED
    basis: b01c17 moral_framework cost_ledger_anchor changed to cl03a.
           cl05 cost draws: b01c12 -1.0 only = -1.0 vs. stated cost -1. Balanced.
           cl03a cost draws: b01c10 -1.0 + b01c17 -1.0 = -2.0 vs. stated cost -2. Balanced.

---

new HARD findings:

  - fault-005
    id: fault-005
    class: LEDGER-MISMATCH
    type: fault
    target: b01c15 substance_delta.axes_in_motion[relational_anchor_status].cost_ledger_anchor (cl-d08)
    what: >
      cl-d08 stated gain is "relational_anchor_status +2". Chapters drawing against cl-d08
      gain: b01c12 +1.0 (anchor cl-d08, notes "cl-d08 cost paid") + b01c15 +1.5 (anchor
      cl-d08, notes "cl-d08 echo at d10"). Total drawn: 2.5 against stated gain of +2.
      Overdraw of 0.5 ranks.

      This draw is new in attempt 2: b01c15 relational_anchor_status cost_ledger_anchor
      was null in attempt 1 (flagged as flag-006). Adding cl-d08 as the anchor resolves
      the null-anchor flag but introduces an overdraw because the cl-d08 gain capacity
      (+2) was already 1.0 consumed at b01c12, leaving only +1.0 remaining — insufficient
      for b01c15's +1.5 draw.
    why: >
      Per-entry overdraw is a HARD class regardless of aggregate arithmetic. cl-d08 is
      funded by a named journey-required mechanism (cl03b coverage-gap architecture). An
      overdrawn cl-d08 means either the gain entry must be revised upward or b01c15's draw
      must be redirected or reduced. Candidate resolution: cl04 (gain "relational_anchor_status
      +3"; drawn at b01c14 +1.0 of +3; remaining +2.0) has sufficient capacity for a +1.5
      draw, or cl-d08 gain entry can be revised from +2 to +2.5 with a note that the
      Vhagar-proximity perceptual mechanism is a distinct event from the original gap-lane
      coverage-gap mechanism. Only one chapter may claim cl-d08 completion.
    criteria: >
      Either (a) cl-d08 gain entry is revised to "relational_anchor_status +2.5" to
      accommodate b01c12 +1.0 + b01c15 +1.5 = 2.5 total, or (b) b01c15 relational_anchor_
      status draw is redirected to an anchor with remaining capacity (cl04 has +2.0
      remaining; cl-d11 has +1.0 gain, not yet drawn). The cl-d08 completion annotation
      must appear in only one chapter.
    scope: episode (b01c15 anchor field or memory.md cl-d08 gain value)

---

per-ledger-entry balance check:

  cl-world-d04:
    stated_gain: "position-world +2"
    draws: b01c04 +1.0 + b01c10 +1.0 = 2.0
    remaining: 0.0
    status: BALANCED

  cl-antag-d03:
    stated_gain: "social_tether-antag +4"
    draws: b01c03 +1.5 + b01c04 +1.0 + b01c15 +1.5 = 4.0
    remaining: 0.0
    status: BALANCED

  cl-antag-d10:
    stated_gain: "social_tether-antag +4"
    draws: b01c10 +1.5 + b01c11 +1.0 + b01c14 +1.5 = 4.0
    remaining: 0.0
    status: BALANCED

  cl-d07a:
    stated_gain: "position-prot-rise +2"
    draws: b01c10 +1.0 + b01c14 +1.0 = 2.0
    remaining: 0.0
    status: BALANCED

  cl05:
    stated_gain: "capability +2"
    gain_draws: b01c12 +1.0 + b01c15 +1.0 = 2.0
    gain_remaining: 0.0
    stated_cost: "moral_framework -1"
    cost_draws: b01c12 -1.0 = 1.0
    cost_remaining: 0.0
    status: BALANCED (both sides)

  cl03a:
    stated_gain: "capability +3"
    gain_draws: b01c04 +1.5 = 1.5
    gain_remaining: +1.5
    stated_cost: "moral_framework -2"
    cost_draws: b01c10 -1.0 + b01c17 -1.0 = 2.0
    cost_remaining: 0.0
    status: BALANCED (cost side); gain side has 1.5 unused — not an error, but b01c17
            capability null anchor (flag-007) could draw here if anchored

  cl-d08:
    stated_gain: "relational_anchor_status +2"
    draws: b01c12 +1.0 + b01c15 +1.5 = 2.5
    remaining: -0.5
    status: OVERDRAWN 0.5 — NEW HARD FINDING (fault-005)

---

attempt-1 soft findings resolution:

  flag-001 (b01c07 political_register-prot null): OUTSTANDING — anchor remains null
  flag-002 (b01c07 social_tether-prot-rise null): OUTSTANDING — anchor remains null
  flag-003 (b01c09 two null anchors): OUTSTANDING — both anchors remain null
  flag-004 (b01c11 political_register-world null): OUTSTANDING — anchor remains null
  flag-005 (b01c13 two null anchors): OUTSTANDING — both anchors remain null
  flag-006 (b01c15 relational_anchor_status null + social_tether-prot-rise null):
    PARTIALLY ADDRESSED — relational_anchor_status now anchored (cl-d08), but anchor
    introduces fault-005 overdraw; social_tether-prot-rise null unchanged
  flag-007 (b01c17 capability null anchor): OUTSTANDING — anchor remains null;
    cl03a gain has +1.5 remaining capacity but no anchor is declared; still elevated
    INFERENTIAL-ANCHOR (cl05 gain now confirmed exhausted at b01c12 + b01c15)
  flag-008 (roll-up note self-contradiction): RESOLVED — attempt-2 roll-up note no
    longer claims a fix is pending for an already-present field; the roll-up block
    correctly describes the b01c07 contribution as included
  flag-009 (b01c20 chunk text vs. YAML delta discrepancy 2.0 vs. 1.5): RESOLVED —
    b01c20 relational_anchor_status target_delta_magnitude changed to 1.5; chunk text
    and YAML now agree
  flag-010 (b01c04 premature cl02 completion claim): OUTSTANDING — notes still read
    "cl02 gain completed" at b01c04; cl02 gain +4 has only 2.0 drawn at that chapter
    (b01c03 +1.0 + b01c04 +1.0); completion claim remains premature

  resolved: 2 of 10 (flag-008, flag-009)
  outstanding: 8 of 10

---

aggregate: REVISE (1 HARD)

hard_findings: [fault-005]

soft_findings:
  - flag-001 (INFERENTIAL-ANCHOR: b01c07 political_register-prot null)
  - flag-002 (INFERENTIAL-ANCHOR: b01c07 social_tether-prot-rise null)
  - flag-003 (INFERENTIAL-ANCHOR: b01c09 two null anchors)
  - flag-004 (INFERENTIAL-ANCHOR: b01c11 political_register-world null)
  - flag-005 (INFERENTIAL-ANCHOR: b01c13 two null anchors)
  - flag-006 (INFERENTIAL-ANCHOR: b01c15 social_tether-prot-rise null; relational_anchor_status anchor present but overdrawn — see fault-005)
  - flag-007 (INFERENTIAL-ANCHOR: b01c17 capability null; cl03a gain has capacity but not declared)
  - flag-010 (NAMING-INCONSISTENCY: b01c04 premature cl02 completion claim)

---

notes:
  Three of four attempt-1 HARD faults are cleanly resolved. One new HARD fault emerged
  from the attempt-2 edit: adding cl-d08 to b01c15 relational_anchor_status resolves
  the null-anchor but overdraws cl-d08 by 0.5 (b01c12 already drew 1.0 of the 2.0
  gain). The fix is narrow: either redirect b01c15's draw to cl04 (remaining capacity
  +2.0) or cl-d11 (gain +1.0, undrawn), or revise cl-d08 gain upward to +2.5 with
  justification that the Vhagar-proximity perceptual mechanism is a distinct gain event
  from the original coverage-gap mechanism. No chapter restructuring required.

  cl03a is now balanced on both sides: gain +3 with 1.5 used (b01c04) + 1.5 remaining;
  cost -2 fully consumed (b01c10 + b01c17). The remaining gain capacity could anchor
  b01c17's null capability draw (flag-007) if declared.

  Roll-up totals and all other ledger entries not named above pass without new findings.
  Thematic-axis coverage, schema compliance, carry-forward obligations, and slug sequence
  unchanged from attempt-1 pass status.
