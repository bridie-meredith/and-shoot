# Admin Decisions Log
# Append-only. One DEC-NNNN entry per dispatch.
# Format: ## DEC-<NNNN> | <date> | <mode> | <verdict>
#
# Fields: question/trigger, context, decision, rationale, follows (if applicable)

## DEC-0001 | 2026-05-26 | process-critic | OK

trigger: Phase 6.5 dispatch — /and-write b01c02 revise bone-gate, 0 HARD, 2 SIGNAL accepted
source_report: active-project/staff/auditor/write-b01-c02-bone-gate-revise.md
gate_path: .claude/commands/and-write.md#phase-6

findings_reviewed:
  - signal-001: HELD-AXIS-NOT-WITNESSED (social_tether-prot-rise + political_register-prot)
    recurrence_count: 1 (first formal emission as SIGNAL; prior b01c01 reference was fixer
    avoidance-note only, not a gate firing; b01c02 original bone-gate contained no match)
    catastrophic: no (dormancy chapter; cleanly dispositioned; no downstream damage)
    process_gap: none — the gate correctly classified SIGNAL (not HARD), accepted-with-rationale
    path executed per spec. One occurrence; premature proposal anti-pattern applies.

  - signal-002: REGISTER-AS-MANNERISM ("takes the drain angle" x3)
    recurrence_count: 1 (first formal emission of this finding class across all chapter reports;
    b01c02 original bone-gate had a near-threshold consideration for "closes [entry]" that was
    ACCEPTED as suppression rhythm — pre-threshold, different class)
    catastrophic: no (stitcher advisory forwarded; not a content loss)
    process_gap: none — gate caught pattern, SIGNAL disposition + advisory forwarded to /and-stitch
    Phase 5 is precisely the designed path. The mechanism is working.

decision: OK — no process change warranted. Both findings are first-occurrence, non-catastrophic.
  Existing gate handles both classes correctly. Wait for recurrence before proposing.

rationale: Per methodology — premature promotion of a one-off SIGNAL is the explicit anti-pattern.
  Recurrence threshold not met for either finding class. Gate disposition path for both SIGNALs
  executed correctly per /and-write.md Phase 6 spec (accepted-with-rationale, advisory forwarded).
  A modify proposal here would add noise without signal.

## DEC-0002 | 2026-05-31 | user-proxy | OK-OVERRIDE

question: /and-write b01c08 Phase 2 auditor flagged b01c08s01n06 (capability +0.5) as
  FAULT-BONE-DELTA-MALFORMED because chunk_targets.bone.delta_per_axis floor is "1-3" and 0.5
  is below 1.0. Override, fix, or escalate?

context:
  - Chapter contract declares capability target_delta_magnitude: 0.5 (staging chapter, sub-1.0 Δ
    by design).
  - c07 shipped clean with four sub-1.0 bone magnitudes (0.3, 0.5, 0.2, 0.5) that passed Phase 6
    bone-gate and /and-stitch. Evidence: _drafts/b01c07-bones-draft-2026-05-30-rev2.md lines
    402, 430, 544, 632. Precedent is concrete and multi-occurrence.
  - Fixer path has no clean fix: can't raise chapter Δ (breaks staging design + book roll-up),
    can't split (split bones would each still need ≥1.0), can't remove (AXIS-DELTA-MISMATCH).
  - Fix path would loop back to override anyway. Net cost: 1 wasted dispatch.

decision: OVERRIDE (option O). Ratify the c07 precedent. Fault-001 (FAULT-BONE-DELTA-MALFORMED
  on b01c08s01n06, capability +0.5) is dispositioned-as-precedent: sub-1.0 bone-floor exception
  applies when the chapter target_delta_magnitude is itself sub-1.0. Cascade continues.
  Parking-lot SOFT item to be appended for principal to ratify the schema edit at next
  /and-review pipeline pass (formalize the exception in chunk_targets or revise bone floor to
  0.5-3.0).

rationale:
  - LTM: no prior ruling on this exact question; first occurrence.
  - Goals: forward motion; don't block a staging-chapter design on a schema floor that predates
    staging chapters.
  - Methodology (reversibility): override is fully reversible — parking-lot SOFT ensures the
    schema gap is not silently dropped. Fix path is irreversible in the sense that it can only
    produce a schema violation or a broken chapter contract; no path to a clean fix exists.
  - Methodology (cost): override = 0 dispatches; fix = 1 dispatch + likely re-loop.
  - Methodology (blast radius): override affects only this one bone on this one chapter.
    Schema edit (deferred to parking lot) is larger-blast but is a SOFT, not a block.
  - c07 multi-occurrence precedent (4 sub-1.0 bones, all PASS) makes this a pattern, not a
    one-off. The gate is misfiring against established project practice.
