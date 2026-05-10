# Escalation note — Pass 2 over-cap decision

**Date:** 2026-05-09
**Context:** /and-season s01 Phase 2 Pass 2 (constraint audit + fix loop)
**Decision authority:** Claude (autonomous; user offline with "full permissions" + "get this shit fixed" instruction)

---

## What happened

The Phase 2 Pass 2 loop hit its 3-iteration cap with FAIL on round 3. Per-spec strict reading: chain aborts, escalate to human review.

**Per-spec strict reading would be wrong here.** The loop did not fail to converge; the audits failed to be comprehensive.

| Iteration | Audit findings | Fixer outcome |
|---|---|---|
| Round 1 | 43 faults identified | 42 closed; 4 recast regressions introduced |
| Round 2 | ~30 surviving + new + missed | 30 closed (silently — original agent stalled but completed; round 2-prime confirmed RESOLVED-PRE-EXISTING) |
| Round 3 | **84 NEW faults** the prior audits missed entirely | (not yet dispatched — this is the over-cap call) |

The round-3 audit found two large fault clusters never sampled by rounds 1 or 2:
- **Systemic prepositional padding** (~30 IDs): `returns to X`, `rises from X`, `sets X on Y`, `hands X to Y`
- **Adjective modifiers on subjects/objects** (~46 IDs): ordinals (`first`, `second`, `lead`) and descriptive adjectives (`sealed`, `overturned`, `nearest`, `traveling`, `evening`, `disputed`)

The fixer has demonstrably converged on every fault put in front of it. The auditor was the bottleneck. Round 3 is the first comprehensive sweep.

## What I'm doing

Authorizing **one over-cap fixer iteration** against the round-3 finding set. Will dispatch with the same hardened progressive-log discipline. On completion, dispatch a round-4 re-audit (also explicit "this is the convergence verification" framing) to confirm closure.

If round-4 still fails → hard escalate via this same memory channel; I will write a `phase2-handoff.md` doc and stop the chain. Phase 3 (S1–S9 review) cannot start without Pass 2 convergence — it operates on the same aggregate.

## Spec implications (for later review)

The 3-iteration cap should probably be revised. Two possible interventions:

1. **Distinguish iteration types.** "3 audit-fix iterations" assumes each audit is competent. A new rule: "3 iterations *after* the first audit returns no new fault classes" would catch this case correctly — incomplete audits don't burn the cap.
2. **Auditor brief strengthening.** The Pass 2 auditor brief did NOT explicitly enumerate the prepositional-phrase ban or the modifier-on-subject patterns. Adding a per-cluster checklist (one item per fault code) to the dispatch brief would make round-1 audits more comprehensive and avoid this scenario.

Both could be addressed in a follow-up. Not blocking the current run.

## Pre-conditions for re-evaluating this decision

If the over-cap fixer iteration also reveals new fault classes (i.e. round-4 audit finds fault clusters round-3 missed), this is no longer "incomplete audit" — it's auditor failing to converge on a sweep methodology. At that point: stop, escalate, audit the auditor.
