```yaml
audit:
  scope: chapter
  target: b01c17
  timestamp: 2026-06-04
  findings:

    - id: fault-001
      type: fault
      what: >
        b01c17 scene-roll-up comment (b01c17-draft.md lines 13-18) asserts
        "cl03a cost side completes" at s03 moral_framework anchor. cl03a
        ledger entry (memory.md ~line 1350-1353) records cost as
        "moral_framework -2". c17 chapter contract delivers moral_framework
        -1.0 total (s02 -0.5 + s03 -0.5, both anchored to cl03a). -1.0 ≠ -2.
        The notes for s03 moral_framework repeat the completion claim ("cl03a
        cost side completes: the intelligence-network-build rolls over into
        use-vector-deployment; the third material breach"). No prior chapter's
        allocation of the remaining -1.0 is cited. If prior chapters have
        already delivered -1.0 of cl03a cost, the completion is coherent but
        undocumented here; if they have not, the completion claim is false and
        the ledger is overclaimed.
      why: >
        A false "cost side completes" claim means the moral_framework axis
        can be re-drawn against cl03a in a later chapter without triggering
        a double-count alert. The cost-ledger is the cross-chapter tracking
        mechanism; an incorrect completion flag corrupts that tracking.
        /and-write Phase 6 substance bone-gate checks cost_ledger_anchor
        consistency against the ledger; an incorrect completion claim here
        will either produce a false-pass or a spurious HARD finding downstream.
      criteria: >
        Either (a) cite the prior chapter(s) in which the remaining -1.0 of
        cl03a cost was delivered, confirming c17 completes the residual; or
        (b) revise the s03 notes to remove the "cost side completes" claim
        and replace with a partial-allocation statement ("second allocation of
        cl03a cost: -0.5 here; -0.5 at s02; prior -X.X at cNN; total delivered
        -N.N of -2.0"). The chapter substance contract must reflect the correct
        ledger state.

    - id: fault-002
      type: fault
      what: >
        cl-d11 ledger entry (memory.md ~line 1402-1405) records gain as
        "relational_anchor_status +1". The chapter contract (memory.md ~line
        9803) and s04 substance_delta (b01c17-draft.md lines 354-366) both
        claim target_delta_magnitude: 0.5, citing cl-d11. s04 notes say
        "cl-d11 delivers" without acknowledging or accounting for the
        remaining +0.5 of the ledger's gain-side. No deferred-settle note,
        no partial-settle annotation, no downstream chapter flagged for the
        remainder. The partial-settle pattern (recurring in this project per
        dispatch context) requires the remaining balance to be explicitly
        accounted or the ledger entry to be revised to match the planned
        magnitude.
      why: >
        An unaccounted +0.5 remainder on cl-d11's gain-side creates an
        orphaned balance. A future chapter may claim the full +1 or the
        remaining +0.5 without a clean reference point, producing either an
        over-delivery on relational_anchor_status or a silent gap. The
        "cl-d11 delivers" language in the s04 notes implies closure, which
        is incorrect if only half the gain lands in c17.
      criteria: >
        Either (a) annotate the s04 cost_ledger_anchor notes to state that
        cl-d11 delivers +0.5 of its +1 gain in c17 and identify the
        chapter/condition under which the remaining +0.5 settles (or explain
        why the partial-settle is the terminal form of this ledger entry); or
        (b) revise the ledger entry cl-d11 to record gain as
        "relational_anchor_status +0.5" if the full gain was always intended
        to land in c17 and the ledger magnitude is wrong. Remove the
        unqualified "cl-d11 delivers" language unless the entry is fully closed.

    - id: flag-001
      type: flag
      what: >
        s03 social_tether-prot-collapse -1.0 (b01c17-draft.md lines 274-284).
        The chunk text describes writing the false attribution (act on-page) but
        does not describe any consequence to the tether architecture. The
        cause-mechanism for the collapse allocation — "false attribution is now
        a structural element of the tether; an unwind would require resolving
        what Taylor has written" — appears only in the substance_delta notes,
        not in the chunk prose. The cause-event (writing the false record) is
        present in the chunk; the mechanism linking that act to tether-collapse
        is not.
      why: >
        At /and-write Phase 6, the bone-gate verifies per-bone axis-movement
        with cause visible on-page. If the tether-collapse cause-mechanism is
        notes-only at scene level, the bones for s03 will be authored without
        that mechanism as a content target, and the bone-gate will have no
        on-page text to verify against for social_tether-prot-collapse. The
        collapse arc's first allocation may land without its logic being
        legible to the audience.

    - id: flag-002
      type: flag
      what: >
        s03 position-prot-collapse -1.0 (b01c17-draft.md lines 262-273).
        The chunk text describes the act of writing the false attribution but
        does not describe the positional-entrapment consequence. The cause
        for the collapse allocation — "extraction would now require Taylor to
        also resolve the false attribution; the non-exit deepens" — is in the
        substance_delta notes only. The cause-event is present; the
        position-deepening mechanism is absent from the chunk prose.
      why: >
        Same downstream risk as flag-001: bones authored from this chunk will
        target the false-attribution act but not the position-entrapment logic.
        The collapse axis gets its first allocation without the audience seeing
        WHY this act deepens the no-exit. The act and the irony are on-page;
        the trap-tightening is not.

    - id: flag-003
      type: flag
      what: >
        s03 capability +1.0 cost_ledger_anchor is null (b01c17-draft.md
        line 240). The notes explain: "no cost_ledger_anchor because the
        capability gain here is subsumed by cl03a's cost-side completion —
        the gain is structural, the anchor fires on moral_framework." But
        cl03a's ledger entry records gain as "capability +3" (memory.md
        ~line 1351). c17's +1.0 capability gain is presumably a partial draw
        against that +3 gain-side, not a new unlisted gain. Anchoring the
        gain-side draw to cl03a (even as a secondary reference) would make
        the ledger relationship explicit; the null anchor with a prose
        explanation in notes is fragile against the cross-chapter consistency
        check.
      why: >
        If the +1.0 capability gain at s03 is a draw against cl03a's +3
        gain-side, omitting the anchor means there is no machine-readable
        link between the gain event and the ledger entry. Future audits at
        book or series scope cannot confirm the cumulative capability draw
        against cl03a's total without relying on prose notes.

    - id: pass-001
      type: pass
      what: Sum-roll-up arithmetic (b01c17-draft.md lines 5-18)
      why: >
        All five moving axes verified against chapter contract
        (memory.md ~lines 9800-9825): moral_framework s02(-0.5)+s03(-0.5)=-1.0
        (contract -1.0); capability s03(+1.0)=+1.0 (contract +1.0);
        relational_anchor_status s04(+0.5)=+0.5 (contract +0.5);
        position-prot-collapse s03(-1.0)=-1.0 (contract -1.0);
        social_tether-prot-collapse s03(-1.0)=-1.0 (contract -1.0).
        All five exact. No ±1 margin invoked.

    - id: pass-002
      type: pass
      what: THEMATIC-AXIS-UNDECLARED check
      why: >
        Chapter goal names protection (relational_anchor_status) and
        Khepri-echo/override-architecture thesis (moral_framework). Both are
        present in axes_in_motion with direction and magnitude. No
        goal-named thesis axis is absent from the contract.

    - id: pass-003
      type: pass
      what: Stakes-axis validity — all four scenes
      why: >
        s01 stakes_axis relational_anchor_status: present in axes_held. s02
        stakes_axis moral_framework: present in axes_in_motion. s03
        stakes_axis capability: present in axes_in_motion. s04 stakes_axis
        relational_anchor_status: present in axes_in_motion. All four pass
        the union-membership check.

    - id: pass-004
      type: pass
      what: Schema-form validation — all scenes
      why: >
        All axes_in_motion entries carry direction ∈ {up, down} and
        target_delta_magnitude > 0. All axes_held entries carry rationale.
        s01 has empty axes_in_motion and populated axes_held (8 entries),
        which is explicitly licit per check instructions. No schema-form
        violations found.

    - id: pass-005
      type: pass
      what: cl07a / cl07b gain-side non-claim check
      why: >
        s03 explicitly states "cl07a gain-side (moral_legibility_to_self +4)
        is not a chapter-17 event" and "cl07b gain-side (position-world +2)
        is not a chapter-17 event." Neither gain appears in any scene's
        axes_in_motion. The collapse axes fire on cost-side only, consistent
        with ledger entries at memory.md ~lines 1410-1417.
```
