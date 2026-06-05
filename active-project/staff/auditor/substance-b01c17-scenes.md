```yaml
audit:
  scope: chapter
  target: b01c17
  timestamp: 2026-06-04
  findings:

    - id: fault-001
      type: flag
      what: >
        b01c17s03 chunk text vs. axes_in_motion for position-prot-collapse -1.0 (cl07b) and
        social_tether-prot-collapse -1.0 (cl07a). Both collapse axes claim their first
        allocation in s03. The s03 chunk prose describes the false-attribution act in full
        (writing three lines in her own hand, attributing Elder Norren's pattern to Wren's
        movements, naming the Khepri-echo parallel) — the cause-event is on-page. However,
        the mechanism linking that act to each collapse axis appears only in the
        substance_delta notes, not in the chunk prose:
          - position-prot-collapse cause ("extraction would now require Taylor to also resolve
            the false attribution; the non-exit deepens") — notes only, not in chunk text.
          - social_tether-prot-collapse cause ("false attribution is now a structural element
            of the tether; an unwind would require resolving what Taylor has written") — notes
            only, not in chunk text.
        The chunk's final lines name the prohibition-echo and Khepri-parallel; they do not
        state that the act deepens Taylor's entrapment or that the tether now carries the
        false record as a structural constraint on exit.
      why: >
        Check axis 2 (chunk-text-matches-contract) requires that the chunk prose describe a
        CAUSE for each claimed axis move — not only the notes field. The chunk is the content
        contract for bones authoring at /and-write. If the trap-tightening and tether-structural
        consequence are notes-only, bones authored to this scene will target the act and the
        moral-echo but not the collapse mechanisms. The bone-gate at /and-write Phase 6 will
        then have no on-page text to verify against for the collapse axes, and the collapse
        arc's first allocation will land without its logic being legible in the prose.

    - id: fault-002
      type: flag
      what: >
        cl-d11 partial settlement without deferral note. Ledger entry cl-d11 (memory.md
        ~line 1402-1405) records gain as "relational_anchor_status +1". The chapter contract
        (memory.md ~line 9803) and s04 substance_delta (b01c17-draft.md lines 354-366) both
        claim target_delta_magnitude: 0.5, citing cl-d11. The s04 notes state "cl-d11
        delivers" without acknowledging the remaining +0.5 or identifying when it will
        settle. No deferred-settle annotation, no parking-lot item, no downstream chapter
        flagged for the remainder.
      why: >
        The "cl-d11 delivers" language implies closure. If only +0.5 of the +1 gain lands in
        c17, the language is incorrect and the remaining +0.5 is an untracked ledger balance.
        A future chapter may claim the full +1 or the remaining +0.5 without a clean reference
        point, producing either over-delivery on relational_anchor_status or a silent ledger
        gap at /and-review verdict b01. Compare the worm-canon-pedant partial-settlement
        pattern: partial settles require explicit remainder accounting.

    - id: fault-003
      type: flag
      what: >
        cl03a "cost side completes" claim (b01c17s03 substance_delta notes, moral_framework
        entry; b01c17-draft.md ~line 255). cl03a ledger entry (memory.md ~lines 1350-1353)
        records cost as "moral_framework -2". c17 delivers moral_framework -1.0 total across
        s02+s03, both anchored to cl03a. For the completion claim to be correct, prior
        chapters must have already delivered the remaining -1.0 of cl03a's cost. That
        prior-chapter consumption is outside the scope of c17 artifacts and was not
        supplied to this audit — the claim cannot be verified from c17 data alone.
      why: >
        If prior chapters have not consumed -1.0 of cl03a cost, the "completes" claim is
        premature and the ledger remains open. A future chapter author who reads the c17
        notes will treat cl03a as exhausted and will not allocate against it, creating a
        silent gap in the moral_framework arc's cost accounting. This is a traceability
        problem, not a current blocking fault, but it will surface as a ledger-consistency
        issue at /and-review verdict b01.

    - id: fault-004
      type: flag
      what: >
        b01c17s03 capability +1.0 has cost_ledger_anchor: null (b01c17-draft.md line 240).
        The notes explain the null by saying the capability gain is "subsumed by cl03a's
        cost-side completion." cl03a's ledger entry records gain as "capability +3" (memory.md
        ~line 1351). c17's +1.0 is presumably a partial draw against that +3 gain-side. The
        prose explanation in notes does not create a machine-readable link between this gain
        event and cl03a's gain-side; the anchor field is the standard link mechanism.
      why: >
        Future audits at book or series scope cannot confirm the cumulative capability draw
        against cl03a's total without relying on prose notes. If cl03a's gain-side has drawn
        +1.0 here (plus whatever prior chapters drew), that running total should be traceable
        to the ledger entry. The null anchor with prose explanation is fragile. This is a
        documentation-quality flag, not a structural fault — the notes are sufficient for
        c17-scope verification but insufficient for cross-chapter accumulation tracking.

    - id: pass-001
      type: pass
      what: Check 1 — sum-roll-up arithmetic (b01c17-draft.md lines 5-18)
      why: >
        All five moving axes verified against chapter contract (memory.md ~lines 9800-9825):
          moral_framework:             s02(-0.5) + s03(-0.5) = -1.0  contract -1.0  MATCH
          capability:                  s03(+1.0)             = +1.0  contract +1.0  MATCH
          relational_anchor_status:    s04(+0.5)             = +0.5  contract +0.5  MATCH
          position-prot-collapse:      s03(-1.0)             = -1.0  contract -1.0  MATCH
          social_tether-prot-collapse: s03(-1.0)             = -1.0  contract -1.0  MATCH
        Roll-up comment is arithmetically correct. No ±1 margin invoked.

    - id: pass-002
      type: pass
      what: Check 3 — cl07a / cl07b gain-side non-reclaim
      why: >
        cl07a gain side (moral_legibility_to_self +4): not present in any scene's
        axes_in_motion; moral_legibility_to_self is in axes_held throughout with rationale
        "crack-level, not full recognition." cl07b gain side (position-world +2): does not
        appear in any scene's axes_in_motion or axes_held. s03 notes explicitly state both
        gain sides are not c17 events. Consistent with cost-side-only firing per contract.

    - id: pass-003
      type: pass
      what: Check 4 — THEMATIC-AXIS-UNDECLARED
      why: >
        Chapter goal names the Khepri-echo/override-architecture-as-protection thesis, which
        maps to moral_framework (prohibition crack completing to enacted breach) and capability
        (protection deployment). Both are present in axes_in_motion with direction and
        magnitude declared. No goal-named thesis axis is absent from the contract.

    - id: pass-004
      type: pass
      what: Check 5 — stakes-axis validity, all four scenes
      why: >
        s01 stakes_axis relational_anchor_status: present in axes_held. PASS.
        s02 stakes_axis moral_framework: present in axes_in_motion. PASS.
        s03 stakes_axis capability: present in axes_in_motion. PASS.
        s04 stakes_axis relational_anchor_status: present in axes_in_motion. PASS.
        All four pass the union-membership check (axes_in_motion ∪ axes_held).

    - id: pass-005
      type: pass
      what: Check 6 — schema-form validation, all scenes
      why: >
        All axes_in_motion entries carry direction ∈ {up, down} and target_delta_magnitude
        > 0. All axes_held entries carry rationale strings. s01 has empty axes_in_motion
        with populated axes_held (8 entries) — explicitly licit per check instructions.
        No schema-form violations found across any of the four scenes.
```

## Verdict: PASS-WITH-FLAGS

No HARD faults. No escalations. Four flags (fault-001 through fault-004). Pipeline progression
is not blocked.

**Flag priority order for showrunner attention:**

fault-001 (highest — affects /and-write): s03 chunk text does not carry the cause-mechanism
for position-prot-collapse or social_tether-prot-collapse. Both collapse axes fire at -1.0 in
s03 as their first allocation. Bones authored from the current chunk will target the
false-attribution act and the moral-echo, but not the trap-tightening logic. Recommend adding
a brief causal statement to the s03 chunk prose that names the extraction-complexity deepening
and the tether-structural consequence before /and-write runs.

fault-002 (medium — affects book ledger): The residual +0.5 on cl-d11 should be parked in the
parking lot or noted in showrunner memory as a deferred remainder. The "cl-d11 delivers"
language in s04 notes should be qualified as a partial settle.

fault-003 (low — traceability): Showrunner should confirm prior-chapter cl03a cost draws sum
to -1.0 before treating the c17 "cost side completes" claim as verified. This is a
ledger-housekeeping check.

fault-004 (low — documentation): The s03 capability gain's null cost_ledger_anchor weakens
cross-chapter accumulation tracking against cl03a's +3 gain-side. Consider adding a secondary
anchor reference.
