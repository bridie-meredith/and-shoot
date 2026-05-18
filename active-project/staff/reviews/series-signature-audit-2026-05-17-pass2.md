# Series Signature Audit — taylor-hebert-westeros-good-intentions
# Pass 2 — 2026-05-17

```yaml
audit:
  scope: series
  target: series.substance.* + books[0] (b01 chunk + substance_delta) — revised artifacts
  timestamp: 2026-05-17
  pass: 2
  prior_report: active-project/staff/reviews/series-signature-audit-2026-05-17.md
  findings:

    # ─── RESOLVED FROM PASS 1 ────────────────────────────────────────────────
    # Listed here for traceability. No action required.

    - id: fault-001
      type: pass
      what: >
        books[0].substance_delta.axes_in_motion[position]: direction field.
      why: >
        Prior fault: `direction: up` with `target_delta_magnitude: 0` was a logical
        contradiction. Revised: `direction: ~` (null). Semantically consistent with
        0-net rise-and-fall arc. Notes field retains the intra-book shape description.
        RESOLVED.

    - id: fault-002
      type: pass
      what: >
        series.substance.cost_ledger: relational-anchor-status two-entry sum vs
        declared -2 arc.
      why: >
        Prior fault: cl-protection-buys-consolidation had `gain: relational-anchor-status +1`
        (opposing direction) so the two entries summed to 0, not -2. Revised:
        cl-protection-buys-consolidation now has `gain: relational-anchor-status -1`.
        Both entries are -1; sum is -2, matching declared target_delta_magnitude: 2.
        axes_in_motion for RAS now lists both anchors in array form:
        `cost_ledger_anchor: [cl-unpriced-cost-bearer, cl-protection-buys-consolidation]`.
        cl-unpriced-cost-bearer description includes explicit compounding note.
        RESOLVED.

    - id: fault-003
      type: pass
      what: >
        books[0].chunk: social-tether cause-language absent.
      why: >
        Prior fault: no mechanism given for social-tether decline in the b01 chunk.
        Revised chunk contains: "she becomes embedded in Flea Bottom because the network
        requires it, and the embedding becomes the same thing that makes her visible to
        Otto's apparatus — community-as-tether and community-as-trap braid the same rope."
        This gives both the build (embedding) and the inversion (same tether = exposure
        vector = eventual severance at d14). Causal anchor is present and decomposable
        by screen-writer at /and-substance book.
        RESOLVED.

    - id: fault-004
      type: pass
      what: >
        books[0].chunk: position rise-to-5 cause-language absent.
      why: >
        Prior fault: no mechanism given for position rising to peak 5 despite Otto
        offering a function-not-rank. Revised chunk contains: "The function Otto gave her
        has no title and no rank, but it has visibility — she is known to one court layer
        as a functional asset, identifiable to the actors who use her." Causal anchor
        for the informal-visibility rise is now present.
        RESOLVED.

    - id: fault-005
      type: pass
      what: >
        series.substance.cost_ledger: cl-knowledge-contempt + cl-protection-buys-consolidation
        +1-as-cost convention undocumented in cl-protection-buys-consolidation.
      why: >
        Prior fault: cl-knowledge-contempt had the explanatory note; cl-protection-buys-consolidation
        did not. Revised: cl-knowledge-contempt is eliminated and replaced by
        cl-intelligence-arrangement, which does not touch political-register-toward-elite
        at all (gain: knowledge +1, cost: agency -1 — standard-direction entries,
        schema-conformant). cl-protection-buys-consolidation now has an explicit
        cost_note: "note: political-register-toward-elite +1 is structurally a cost —
        axis nine_means = contempt-without-refusal; cost recorded as +1 because the axis
        moves toward its damaging end." Convention is now explicit in the entry that uses it.
        cl-intelligence-arrangement schema-conformance verified: gain and cost fields use
        standard positive/negative direction on normal-direction axes.
        RESOLVED.

    - id: fault-006
      type: pass
      what: >
        series.substance.chunk_targets.series: delta_per_signature_axis floor override
        (was 4→3, now 4→1) and compounding risk with fault-003.
      why: >
        Prior fault: 3-rank floor with missing social-tether cause-language created
        compounding downstream risk. Both dimensions resolved: floor is now 1 (with tuning
        note explaining the rationale for loss-arc tragedy with small-magnitude signature
        axes); fault-003 is resolved so the missing-cause-language risk is closed.
        RESOLVED.

    - id: fault-007
      type: pass
      what: >
        series.substance.cost_ledger[cl-unpriced-cost-bearer]: STRUCTURAL ERROR ENTRY
        label and negative gain field.
      why: >
        Intentional design choice; flagged in pass 1 for reviewer awareness only.
        YAML retains the "STRUCTURAL ERROR ENTRY" label and description. No action
        required; downstream bone-gate auditors should treat negative-gain-field as
        TASTE not HARD per the entry's explicit documentation.
        NO CHANGE REQUIRED — CONFIRMED PRESENT.

    - id: fault-008
      type: pass
      what: >
        series.substance.cost_ledger[cl-social-tether-build]: cost: position +1
        as mixed-valence cost coding.
      why: >
        Intentional design choice; flagged in pass 1 for reviewer awareness only.
        cost_note field is present. No action required.
        NO CHANGE REQUIRED — CONFIRMED PRESENT.

    # ─── NEW CHECKS ──────────────────────────────────────────────────────────

    - id: check-001
      type: pass
      what: >
        books[0].chunk d03 refusal-beat insert vs series-trajectory.md d03 amendment.
      why: >
        Dispatch asked auditor to verify the b01 chunk's new refusal-beat language
        is consistent with the trajectory d03 two-beat structure.
        b01 chunk: "She refuses first; she names the prohibition that is supposed to hold;
        the prohibition holds long enough to make the second answer audible as a choice."
        Trajectory d03 cause: "Two-beat structure: Taylor refuses first — she names the
        prohibition (atonement-via-refusal-of-control, no one becomes an instrument again)
        and holds it. Otto does not press; the calculation does. She finds no path that
        keeps [protect-target] alive and the prohibition intact simultaneously. The refusal
        holds long enough to make the second answer legible as a choice, not as an
        inevitability."
        Chunk and trajectory are consistent: both encode the prohibition-named → held →
        calculation-not-Otto-breaks-it → second-answer-as-choice sequence. The chunk
        is appropriately compressed for book-level; the trajectory carries the full
        mechanism. No drift.
        PASS.

    - id: check-002
      type: pass
      what: >
        series.substance.state_axes[capability].nine_means reframe vs
        cond-khepri-residue-122ac hard fence on multi-shard hijack.
      why: >
        Dispatch asked auditor to verify the capability nine_means reframe ("insect
        network threaded through multiple wards reading bodies and routing intelligence
        at scale — the morally-rhyming repetition, not the architectural one;
        surveillance + unconsented instrumentalization, not control-override") and
        the b01 chunk language ("she builds something that rhymes with Khepri in the
        only register left to her — observation without consent, movement without
        knowledge, decision-making at a remove from the people whose lives she is routing")
        do not violate cond-khepri-residue-122ac.

        Card fence: "Multi-shard hijack: gone... Any scene implying Taylor can coordinate
        or override human nervous systems is a fence violation."

        nine_means explicitly excludes the prohibited capability: "not control-override."
        Trajectory d04 makes the sin-type unambiguous: "The sin is surveillance and
        unconsented instrumentalization of movement patterns, not override of nervous
        systems."

        The b01 chunk phrase "movement without knowledge" is the only language requiring
        scrutiny: in isolation it could be read as physically routing people's bodies.
        In context (immediately preceded by "observation without consent" and followed by
        "decision-making at a remove from the people whose lives she is routing") it reads
        as intelligence routing — routing information derived from observed movement
        patterns, not routing people's physical motion. The trajectory d04 language
        disambiguates. No fence violation.
        PASS — with the annotation that /and-substance book and /and-write should carry
        cond-khepri-residue-122ac as an active constraint, and the "movement without
        knowledge" phrase should not be used without the surrounding disambiguation
        at those levels.

  summary:
    pass_1_faults_resolved: 6    # fault-001 through fault-006
    pass_1_taste_confirmed: 2    # fault-007, fault-008 — no change needed, confirmed present
    new_findings_pass2: 0
    total_open_findings: 0
    verdict: PASS
```
