# /and-substance book b01 — Phase 5 pass 2 audit

```yaml
audit:
  scope: book
  target: b01
  pass: 2 of 3
  timestamp: 2026-05-18
  auditor: auditor
  verdict: PASS

  # ────────────────────────────────────────────────────────────────
  # Pass-1 SIGNAL resolution
  # ────────────────────────────────────────────────────────────────

  signal_resolution:

    - id: signal-001
      resolution: RESOLVED
      evidence: >
        b01c01 substance_delta.axes_in_motion[knowledge]:
        cost_ledger_anchor: ~ (was: cl-intelligence-arrangement)
        note now reads: "passive orientation; pre-arrangement; unanchored knowledge gain at baseline"
        The pre-arrangement anchor is gone. Criteria met.

    - id: signal-002
      resolution: RESOLVED
      evidence: >
        b01c02 capability axis: cost_ledger_anchor: ~ (was: cl-network-position)
        note: "first-deployment; self-directed rescue; pre-Otto-arrangement, not yet network expansion"
        b01c02 knowledge axis: cost_ledger_anchor: ~ (was: cl-intelligence-arrangement)
        note: "watch-sweep-pattern observation; pre-arrangement; unanchored"
        Both pre-arrangement anchors removed. Criteria met.

    - id: signal-003
      resolution: RESOLVED
      evidence: >
        b01c04 position: cost_ledger_anchor: cl-otto-trade (was: cl-social-tether-build)
        note: "identification-as-asset; pre-acceptance position-visibility shift through Otto
        recognizing Taylor's capability"
        b01c05 position: cost_ledger_anchor: cl-otto-trade (was: cl-social-tether-build)
        note: "acceptance formalizes asset-identification; position visibility crystallizes
        through the first trade"
        b01c09 position: cost_ledger_anchor: cl-otto-trade (was: cl-social-tether-build)
        note: "Otto's-unofficial-instrument; arrangement named; position-visibility now formal
        in the one court layer that uses Taylor"
        All three re-anchored to cl-otto-trade, whose gain side (Otto-arrangement activation
        and deepening) is operative in each respective chapter. Criteria met.

    - id: signal-004
      resolution: RESOLVED
      evidence: >
        b01c09 axes_in_motion contains: moral-framework, position, knowledge, agency.
        No capability entry present. The c09 handoff_out character_state note reads:
        "capability 5 (no trajectory allocation for capability at d07; see signal-004 resolution)"
        confirming the removal was intentional and correctly annotated.
        Capability roll-up recomputed: c02(+1.0)+c06(+1.0)+c14(+1.0)+c15(+0.5) = +3.5.
        |3.5 − 4| = 0.5. Within ±1 of book target +4. Criteria met.

    - id: note-002
      resolution: RESOLVED
      evidence: >
        All chapter headers now use comment-line format:
        # dramatic_shape (informational): <value>; trajectory_deltas_carried: [...]
        No YAML field named dramatic_role or trajectory_deltas_carried appears in any chapter
        block. The comment-line approach correctly sidesteps the field-name drift without
        introducing invalid enum values into the schema-controlled field namespace.
        Criteria met.

  # ────────────────────────────────────────────────────────────────
  # Drift check on revised chunks (c04, c05, c11)
  # ────────────────────────────────────────────────────────────────

  drift_check:

    - chapter: b01c04
      verdict: CLEAN
      notes: >
        Chunk now names Otto, names Sera Hightower explicitly with her succession-calculus
        position, the threat-shape, and the probability distribution on her survival — all
        per the HARD-2 resolution mandate. Otto leaves the calculation to Taylor; the refusal
        holds. The evening insect-read of the Green-faction courtier mapping the ward is
        present, establishing world-pressure between c04 close and c05 open. The c04 handoff_out
        open_threads list correctly carries Sera Hightower's probability picture as an
        unresolved model entry.
        substance_delta position +0.5 anchored to cl-otto-trade: consistent with chunk — Taylor
        is now a known quantity to one court-adjacent agent, which is exactly the position shift
        described. No substance-contract mismatch.

    - chapter: b01c05
      verdict: CLEAN
      notes: >
        Chunk explicitly attributes the Sera Hightower probability model to two sources:
        (a) what Otto named in the c04 meeting (primary) and (b) Taylor's systematic
        ward-layer reading in the intervening days filling in from rumor-pickup and
        courier-transit patterns. The information-source chain is now visible.
        The chunk holds the refusal through one full iteration, then a second, before Taylor
        crosses. The acceptance is framed as a genuine second-answer choice, not coercion.
        substance_delta: moral-framework −1.0 (cl-otto-trade), position +0.5 (cl-otto-trade),
        agency −0.5 (cl-otto-trade). All three match the chunk events: prohibition crossed,
        position formalizes as asset on acceptance, first commitment-to-arrangement.
        No substance-contract mismatch.

    - chapter: b01c11
      verdict: CLEAN
      notes: >
        Chunk contains the specific contempt-arrival image as required by HARD-1 resolution:
        displacement report on smallfolk delivered to a Maegor's Holdfast chamber, received
        by the senior Green-faction figure, registered by weight, placed unopened to one side;
        twenty minutes later (by insect-reckoning) the same figure signs the succession
        instrument routing the political play through the same ward. The document is still
        unread. The naming of the ward's people as invisible-as-paper is present.
        Taylor names whose names in the ledger (Green-faction inner circle, succession-instrument
        signatories); individual-name roster deferred to /and-substance chapter b01c11
        (correctly noted in chunk comment).
        substance_delta: political-register-toward-elite +1.5 (anchor ~, consequence-axis,
        consistent with the threshold-crossing image producing a concluded observation rather
        than a causal trade). knowledge +0.5 (cl-intelligence-arrangement, consistent with
        court picture completing to "more complete than most Small Council members").
        No substance-contract mismatch.

  # ────────────────────────────────────────────────────────────────
  # Roll-up re-verification (9 axes, post-revise)
  # ────────────────────────────────────────────────────────────────

  rollup_reverification:
    method: >
      Capability recomputed from chapter data after c09 removal. All other axes carried
      forward from pass-1 pass-004 (unchanged chapters, unchanged magnitudes).

    axes:
      - axis: moral-framework
        contributors: "c05(−1.0)+c09(−0.5)+c15(−0.5)"
        sum: −2.0
        target: −2
        delta: 0.0
        result: PASS

      - axis: capability
        contributors: "c02(+1.0)+c06(+1.0)+c14(+1.0)+c15(+0.5)"
        sum: +3.5
        target: +4
        delta: 0.5
        result: PASS

      - axis: position_net
        contributors: "rise c04+c05+c09 = +1.5; fall c12+c17 = −2.0; net −0.5"
        sum: −0.5
        target: 0
        delta: 0.5
        result: PASS

      - axis: social-tether
        contributors: "rise c02+c06 = +1.0; fall c12+c17 = −1.5; net −0.5"
        sum: −0.5
        target: −1
        delta: 0.5
        result: PASS

      - axis: relational-anchor-status
        contributors: "c03+c08+c10+c13+c17 = −2.5"
        sum: −2.5
        target: −2
        delta: 0.5
        result: PASS

      - axis: moral-legibility-to-self
        contributors: "c03+c08+c12+c13+c17 = −3.0"
        sum: −3.0
        target: −3
        delta: 0.0
        result: PASS

      - axis: political-register-toward-elite
        contributors: "c07+c11+c16+c17 = +4.0"
        sum: +4.0
        target: +4
        delta: 0.0
        result: PASS

      - axis: knowledge
        contributors: "c01+c02+c04+c06+c07+c09+c10+c11+c14 = +5.5"
        sum: +5.5
        target: +5
        delta: 0.5
        result: PASS

      - axis: agency
        contributors: "c05+c06+c09+c12+c14+c15+c17 = −4.0"
        sum: −4.0
        target: −4
        delta: 0.0
        result: PASS

    summary: All 9 axes within ±1 of book target. Roll-up clean.

  # ────────────────────────────────────────────────────────────────
  # New findings introduced by the revise
  # ────────────────────────────────────────────────────────────────

  new_findings: none

  # ────────────────────────────────────────────────────────────────
  # Scope note on c04 knowledge anchor
  # ────────────────────────────────────────────────────────────────

  scope_note: >
    b01c04 knowledge axis carries cost_ledger_anchor: cl-intelligence-arrangement.
    This entry was present in the pass-1 draft and was not flagged in pass-1 (it was
    covered by pass-003, which found all anchor IDs valid). The revise did not touch
    this entry. Per the pass-2 charge, pass-1 non-flagged items not touched by the
    revise are assumed compliant. This anchor is therefore out of scope for pass-2
    and is not classified as a new finding. It is noted here for transparency: the
    arrangement is accepted in c05, not c04; if a future audit re-runs the full anchor
    sweep, c04's knowledge entry warrants review under the same pre-arrangement
    criterion applied to c01/c02 in pass-1 signals 001 and 002.
```

---

## Verdict: PASS

All four pass-1 SIGNAL findings are RESOLVED. note-002 is RESOLVED. No new HARD findings were introduced by the revise. Drift checks on the three revised chunks (c04, c05, c11) are clean — chunk text matches substance contracts, and re-anchored entries are causally grounded in each chapter's events. Nine-axis roll-up verified; all axes within ±1 of book target after capability recomputation (new sum: +3.5, delta 0.5 from target +4).

Pass-1 NOTE findings (note-001, note-003) and deferred items remain open per their original classifications; none escalated by this revise.

The draft is cleared for `/and-substance chapter b01c01` cascade initiation.
