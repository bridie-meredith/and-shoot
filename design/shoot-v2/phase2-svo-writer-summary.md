# Phase 2 — SVO-Writer Pipeline Run Summary

End-of-Phase-2 (writer-fork-and-review) artifact for the svo-writer pipeline tuning effort. Run 2026-05-07. Same episode (s01e01), same locked reviewer briefs as Phase 1 baseline.

**Headline:** the screen-writer fork (rubric-aware, blind to the naive baseline and to past shoot artifacts) produced a structurally correct file. Pass 5 returned CONTINUITY-OK on first try. Pass 2 lifted from the Phase 1 baseline of 6.1% to **45.3% (+39.2pp)**, with a single dominant residual fault class (FAULT-FORM-MODIFIER, 27 instances) traced to a brief gap on prepositional padding. Brief tuned in-flight; fixer dispatched to apply minimum-change repairs to the existing output.

---

## Trajectory (Pass 2)

| Round | File | CORRECT | Faults | Lift |
|---|---|---|---|---|
| Phase 1 baseline | `phase1-svo-writer-baseline-naive.md` | 2 / 33 = **6.1%** | 9 fault classes, 31 fault-bearing lines | — |
| Phase 2 fork output | `phase2-svo-writer-fork-output.md` | 24 / 53 = **45.3%** | 2 fault classes, 29 faults | **+39.2pp** |

Lift is real but well below convergence. Comparison to facet runs shows the writer-fork pattern lifts harder for facets than for the SVO writer at first attempt — the facet runs lifted into the 75–97% range. Reasons:

- The SVO writer's authority surface is harsher (every line must be legal under multiple bans simultaneously) than a facet writer's (one entry, one rubric category).
- The brief gap on prepositional padding caused systematic, uniformly-distributed fault re-introduction — the writer self-reported clean output, indicating the rule was internalized as "no adjective/adverb" rather than "no prepositional phrase."

---

## Pass 2 fault distribution

- **FAULT-FORM-MODIFIER:** 27 — all prepositional phrases of place/destination/source/direction/instrument/accompaniment appended to otherwise-clean SVOs. Examples: `moves to the yard`, `lift from the bell tower`, `steps through the gate`, `crests the road from the north`, `holds the feet on the flagstones`, `exits with the ledger sealed in the case`.
- **FAULT-FORM-INTERIORITY:** 2 — both on the line `the yard holds the silence` (lines 26 and 41). Abstraction (`silence`) used as object of a hold-verb. The hold pattern is correct for physical objects under pressure; abstractions belong in loc-state or feeling-flag facets.

No FAULT-FORM-COPULA, FAULT-FORM-NEGATION, FAULT-FORM-PERCEPTION, FAULT-FORM-CONJUNCTION, FAULT-FORM-INTERIORITY (besides the abstraction case), FAULT-FORM-MULTI-SUBJECT, FAULT-FORM-NO-VERB. **All the harshly-tuned rules from the Phase 1 brief held.** Only the under-specified modifier rule and the un-named abstraction-as-object pattern broke through.

---

## Pass 3 (Shape) — Phase 2

**Verdict:** RE-ORDER-AND-TRANSITIONS (1 reorder + 1 transition).
- Re-order: lines 41–42 (`the yard holds the silence`, `the wards hold their positions`) belong AFTER line 46 (the double-stroke notation), not before. As authored, they bleed tension out of the approach to the irreversible act.
- Missing transition: between (re-ordered) line 46 and line 47 — Taylor's perception of the double-stroke notation has no anchor. The episode's load-bearing climax collapses from clerk-notation directly to officer-departing-words. One Taylor-POV beat needed.

**Curve verdict:** rise-peak-fall correct; peak correctly placed at line 46 (ledger entry); only structural fault is the misplaced deflation beats.

Report: `active-project/staff/auditor/protolines-s01e01-pass3-phase2.md`.

---

## Pass 4 (Trim) — Phase 2

| Persona | Deletion proposals | File-level verdict |
|---|---|---|
| pulp-enthusiast | 6 (lines 6, 12, 19, 20, 42, 52) | ACCEPT |
| worm-canon-pedant | 1 (line 52) | ACCEPT |
| dark-fantasy-reader | 5 (lines 4, 5, 6, 50, 51) | ACCEPT |

**File-level: ALL-ACCEPT.** All three personas accepted.

**≥2-persona threshold (auto-accept) deletions:**
- Line 6 (`the other wards move into the yard`) — pulp + dark.
- Line 52 (`clerk closes the ink case`) — pulp + pedant.

**1-persona advisory:** lines 4, 5, 12, 19, 20, 42, 50, 51.

Reports: `active-project/staff/auditor/protolines-s01e01-pass4-{pulp-enthusiast,worm-canon-pedant,dark-fantasy-reader}-phase2.md`.

---

## Pass 5 (Continuity) — Phase 2

**Verdict:** CONTINUITY-OK on first run. **Zero faults across all four sweeps** (reachability, state, reference, POV).

Notable: the writer correctly held the septon off-stage via `the sept doors hold closed` and never named him, sidestepping the Phase 1 baseline's septon-name discrepancy. The four time-skips fall at compatible location-state transitions. All five actors have coherent presence-arcs. Letter, ledger, and ink case all track cleanly through placement, use, and return.

The bone-only format (no perception verbs, no modifiers — except the modifier faults caught at Pass 2) was structurally sufficient to pass continuity on first attempt.

Report: `active-project/staff/auditor/protolines-s01e01-pass5-phase2.md`.

---

## Brief tuning (in-flight, applied 2026-05-07)

`design/shoot-v2/svo-writer-pass1-brief.md` §"SVO discipline" — modifier clause expanded:

- Names prepositional padding explicitly across place / destination / source / direction / instrument / accompaniment.
- Provides the verb-choice solution: prefer transitive verbs that take location/destination as direct object (`enters the yard` not `moves to the yard`; `crosses the gate` not `steps through the gate`).
- Names abstraction-as-object as a distinct sub-failure and routes it to FAULT-FORM-INTERIORITY.

This is the first reviewer-tuning round in the pipeline tuning effort. Phase 1 declared "no tuning needed" but the Phase 2 writer-fork results revealed a brief gap that only became visible at scale. Lesson: declaring brief-locked at end of Phase 1 was premature; brief gaps surface under writer-fork pressure, not under naive-baseline review.

---

## Next steps

The phase 2 output has three independent improvement tracks queued (Phase 2.5 / 2.6 / 2.7 / 2.8 in the task list):

1. **Phase 2.5 — fixer repair + pass 2 reconverge.** Apply 27 modifier strips + 2 abstraction-as-object recasts. Re-run pass 2. Loop until clean.
2. **Phase 2.6 — apply pass 3 reorders + transition addition.** Move 41–42 after 46. Dispatch screen-writer for one transition between new-46 and 47 (Taylor-POV perception of the entry).
3. **Phase 2.7 — apply pass 4 deletions, re-run pass 4.** Apply auto-accept deletions on lines 6 and 52. Re-run pass 4 to verify all-ACCEPT survives.
4. **Phase 2.8 — re-run pass 5 continuity.** After all upstream changes, re-verify CONTINUITY-OK still holds.

Convergence target: end-to-end clean run (all five passes return clean in sequence) within 1–2 iterations of repair. If achieved, advance to Phase 3 (adversarial seams) against the converged file. If not achieved, return to brief-tuning before re-attempting writer-fork.
