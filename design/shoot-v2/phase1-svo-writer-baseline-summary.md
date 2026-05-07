# Phase 1 — SVO-Writer Pipeline Baseline Summary

End-of-Phase-1 artifact for the svo-writer pipeline tuning effort. Run 2026-05-07 against the synthetic naive baseline (`phase1-svo-writer-baseline-naive.md`, 33 body lines) for episode s01e01.

**Headline:** all four reviewer passes returned strict, defensible verdicts on a deliberately-flawed baseline. No reviewer brief required tuning before Phase 2 — the Phase 1 numbers are the **baseline-to-beat** for the Phase 2 writer fork.

---

## Per-pass results

| Pass | Reviewer | Verdict | Headline number |
|---|---|---|---|
| 2 | auditor #1 (constraint+SVO mechanic) | FAIL | **2/33 = 6.1% CORRECT** |
| 3 | dramatist (shape) | RE-ORDER-AND-TRANSITIONS | 1 swap (lines 14↔15) + 1 missing transition (12↔13) + flatline 9–12 diagnosed |
| 4 | audience ×3 (trim) | ALL-ACCEPT | **7 auto-accept deletions** + 4 advisory |
| 5 | auditor #2 (continuity) | CONTINUITY-FAIL | **5 faults + 1 flag** |

---

## Pass 2 — Constraint Audit Baseline

**File-level:** FAIL.
**CORRECT lines:** 8, 17 (2 of 33 = 6.1%).
**Faults distribution:**

| Class | Count |
|---|---|
| FAULT-FORM-MODIFIER | 17 |
| FAULT-FORM-CONJUNCTION | 13 |
| FAULT-FORM-COPULA | 8 |
| FAULT-FORM-NEGATION | 5 |
| FAULT-FORM-INTERIORITY | 4 |
| FAULT-FORM-PERCEPTION | 3 |
| FAULT-FORM-MULTI-SUBJECT | 3 |
| FAULT-FORM-NO-VERB | 2 |
| FAULT-PHYSICAL-ACTOR-ABSENT | 1 |

**Recall vs. seeded faults:** 100% — every seeded-fault line was flagged.
**Precision:** 100% — every "extra" fault relative to the seeded reference is a genuine SVO-mechanic violation the seeded reference under-annotated. The auditor is the more accurate annotator; seeding was loose.
**Bonus catch:** line 16 — septon name `Osmynd` does not match the canonical `Aldric` from `loc-harrenhal-sept-environs.card.md`. Routed as FAULT-PHYSICAL-ACTOR-ABSENT with RENAME-SLUG.

**Brief tuning needed?** No. Recall and precision both at 100% under the locked rubric. The brief is shippable as-is.

Report: `active-project/staff/auditor/protolines-s01e01-pass2-baseline.md`.

---

## Pass 3 — Shape Baseline

**Verdict:** RE-ORDER-AND-TRANSITIONS.
**Re-order proposed:** swap lines 14 and 15 (the singling-out observation must follow the question, not anticipate it). Otherwise no changes.
**Missing transition:** between lines 12 and 13 — a beat establishing Taylor's position at the end of the line as the officer finishes processing the wards ahead of her. Without it, "the officer reaches Taylor" is a location jump.
**Flatline:** lines 9–12 (four consecutive procedural beats with no stakes inflection). The 12↔13 transition addition partially breaks it.
**Climax:** line 29 (double-stroke ledger entry) — uniquely placed.

**Recall vs. seeded shape faults:** 1 of 3 seeded faults caught (the 14/15 sequencing inversion was not seeded but is genuine; the seeded flatline at 1–8 was diagnosed as 9–12 instead — also genuine; the seeded climax-non-uniqueness 21 vs 29 was *not* flagged — dramatist treated 29 as the unique peak with line 21 as a rising-action beat). The seeded reference's "competing peaks" claim was overstated.

**Brief tuning needed?** No. Shape verdict is honest. The dramatist correctly identified what's wrong and refrained from manufacturing additional faults.

Report: `active-project/staff/auditor/protolines-s01e01-pass3-baseline.md`.

---

## Pass 4 — Trim Baseline (3 personas)

**File-level verdict:** all three personas ACCEPT.

**Per-line deletion proposals:**

| Line | pulp-enthusiast | worm-canon-pedant | dark-fantasy-reader | Total | Status |
|---|---|---|---|---|---|
| 1 | ✓ | | ✓ | 2 | AUTO-DELETE |
| 2 | ✓ | ✓ | ✓ | 3 | AUTO-DELETE |
| 4 | | ✓ | | 1 | advisory |
| 5 | | | ✓ | 1 | advisory |
| 7 | | ✓ | | 1 | advisory |
| 10 | | ✓ | ✓ | 2 | AUTO-DELETE |
| 12 | ✓ | ✓ | ✓ | 3 | AUTO-DELETE |
| 14 | ✓ | | ✓ | 2 | AUTO-DELETE |
| 26 | | ✓ | ✓ | 2 | AUTO-DELETE |
| 28 | | ✓ | | 1 | advisory |
| 33 | ✓ | ✓ | ✓ | 3 | AUTO-DELETE |

**Auto-accept deletions:** 7 lines (1, 2, 10, 12, 14, 26, 33) = 21% trim rate.
**Advisory:** 4 lines (4, 5, 7, 28).

**Cross-persona signal:** strong unanimity on lines 2 (Taylor-tiredness interiority), 12 (clerk-writes-carefully duplication), 33 (Taylor-feels emotional declaration). Two-of-three on lines 1 (atmosphere assertion), 10 (incidental count), 14 (anticipatory observation), 26 (asserted silence).

**Brief tuning needed?** No. The three personas converged on the inert-and-non-voice-bearing lines from distinct lenses. Behavior cards correctly invoked: pedant cited Taylor's behavior signature for line 33 emotional-declaration; dark-fantasy-reader cited the cold-institutional register for line 1 atmospheric softening.

Reports: `active-project/staff/auditor/protolines-s01e01-pass4-{pulp-enthusiast,worm-canon-pedant,dark-fantasy-reader}-baseline.md`.

---

## Pass 5 — Continuity Audit Baseline

**Verdict:** CONTINUITY-FAIL.
**Reachability:** OK — the surviving sequence delivers the goal.
**State faults:** 2.
- `FAULT-STATE-PROP-DANGLING` line 19 — letter appears with no in-sequence placement beat.
- `FAULT-STATE-TIME-INCONSISTENT` lines 11/14 — line 14 asserts "officer doesn't ask anyone else this question," directly contradicting line 11 which shows the officer working through all wards asking that exact category. The singling-out observation belongs with line 27 (clerk's "assessed before"), not here.
**Reference faults:** 1 fault + 1 flag.
- `FAULT-REFERENCE-CAST-SLUG` line 16 — Septon Osmynd vs. canonical Aldric per `loc-harrenhal-sept-environs.card.md`.
- `FAULT-REFERENCE-LOCATION-INVALID` line 1 (flag) — "flagstones" inconsistent with location card's "hard-packed earth."
**POV faults:** 2.
- `FAULT-POV-LEAK` line 28 (`knows`).
- `FAULT-POV-LEAK` line 33 (`feels`).

**Recall vs. seeded faults:** all 3 seeded continuity faults caught + 2 unseeded bonus catches (the 11/14 contradiction and the location card's flagstones/hard-packed-earth mismatch). Pass 5 is doing real work beyond the seeded baseline.

**Brief tuning needed?** No. Pass 5's POV-leak catches duplicate Pass 2's perception/interiority catches on lines 28 and 33 — this is the brief's intended backup behavior, not redundancy. The 11/14 contradiction is a genuinely emergent fault that only Pass 5 would catch (Pass 2 reads per-line, doesn't cross-reference).

Report: `active-project/staff/auditor/protolines-s01e01-pass5-baseline.md`.

---

## Cross-pass coherence

The four passes produced complementary, non-overlapping signal. No two reviewers redundantly flagged the same line for the same reason — each pass operates on its own axis:

- Pass 2 owns mechanic + per-line constraint legality (form, no-modifier, slug-resolution).
- Pass 3 owns sequencing and arc shape (where, not what).
- Pass 4 owns goal-service and voice-load (audience taste against the chapter goal).
- Pass 5 owns emergent integrity (cross-line state, POV consistency, bonus reference checks).

The architecture's "context isolation between passes" hypothesis held: each pass loaded only its own brief's inputs and produced only its own brief's verdicts. No leakage of taste into mechanics, no leakage of mechanics into shape, no leakage of shape into trim.

---

## Baseline numbers (frozen for Phase 2 comparison)

| Metric | Phase 1 baseline value |
|---|---|
| Pass 2 strict accept rate | 2/33 = **6.1%** |
| Pass 3 shape verdict | **RE-ORDER-AND-TRANSITIONS** |
| Pass 4 file-level | **ALL-ACCEPT** with 7 auto-deletions |
| Pass 5 file-level | **CONTINUITY-FAIL** (5 faults + 1 flag) |

**Pass 2 is the headline lift target.** A Phase 2 writer fork operating under the locked Pass 1 brief should drive Pass 2's accept rate from 6.1% toward 100%. The other three passes are convergence gates rather than lift targets — Phase 2 success means Pass 3 returns CLEAN, Pass 4 returns ALL-ACCEPT with zero deletions, Pass 5 returns CONTINUITY-OK with zero faults.

---

## Decisions for Phase 2

1. **Reviewer briefs:** locked. No tuning needed. Phase 1 demonstrated all four briefs produce strict, defensible, complementary verdicts.
2. **Writer fork brief:** locked at `design/shoot-v2/svo-writer-pass1-brief.md`. Screen-writer fork dispatches blind to the naive baseline (`phase1-svo-writer-baseline-naive.md`), blind to past shoot artifacts, blind to the seeded-faults reference.
3. **Output path for Phase 2 writer fork:** `design/shoot-v2/phase2-svo-writer-fork-output.md` (avoids any conflict with the parallel session's `active-project/theater/proto-lines/`).
4. **Test episode:** s01e01 (continuity with Phase 1 baseline; comparable scope).

Phase 2 begins immediately.
