---
phase: 1
artifact: seeded-faults reference (NOT for reviewer dispatch)
purpose: The author's-eye-view of which faults were seeded into phase1-svo-writer-baseline-naive.md, used after Phase 1 reviewer reports come back to compute recall (faults caught) and precision (false positives).
---

The naive baseline is hand-synthesized to be a plausible chunk-only author's output without SVO discipline. Each line has zero or more deliberately-seeded faults. Reviewers run blind to this file.

## Pass 2 (constraint audit) — SVO mechanic faults

| Line | Seeded fault(s) |
|---|---|
| 1 | FAULT-FORM-COPULA (`is`), FAULT-FORM-MODIFIER (`bright`) |
| 2 | FAULT-FORM-COPULA (`is`), FAULT-FORM-INTERIORITY (`tired`) |
| 3 | FAULT-FORM-MODIFIER (`loudly`), borderline FAULT-FORM-INTERIORITY (reported speech rendered as paraphrase rather than `<speaker> speaks to <listener>`) |
| 4 | FAULT-FORM-CONJUNCTION (`and`), FAULT-FORM-MODIFIER (`out`) |
| 5 | FAULT-FORM-PERCEPTION (`reads`, `notes`), FAULT-FORM-INTERIORITY |
| 7 | FAULT-FORM-COPULA (`is`), FAULT-FORM-MODIFIER (`heavy`) |
| 10 | FAULT-FORM-PERCEPTION (`counts`) |
| 11 | borderline COMPOUND-OBJECTS — single dictation event acting on a list (acceptable per rubric §plural-object); auditor should call CORRECT |
| 12 | FAULT-FORM-MODIFIER (`carefully`) |
| 14 | FAULT-FORM-NEGATION (`doesn't ask`) |
| 16 | FAULT-FORM-CONJUNCTION (`and`), FAULT-REFERENCE-CAST-SLUG candidate (Septon Osmynd not in cast — though as off-stage referent in dialogue content this is open) |
| 18 | FAULT-FORM-COPULA (`are closed`), FAULT-FORM-CONJUNCTION (`and`) |
| 19 | FAULT-FORM-CONJUNCTION (`and`); also pass 5 candidate (no prior placement of letter) |
| 20 | FAULT-FORM-CONJUNCTION (`and` ×2) |
| 23 | FAULT-FORM-MODIFIER (`while everyone watches`), FAULT-FORM-CONJUNCTION (`and`) |
| 24 | FAULT-FORM-CONJUNCTION (`and`) |
| 25 | FAULT-FORM-NEGATION (`does not speak`), FAULT-FORM-CONJUNCTION (`and`) |
| 26 | FAULT-FORM-COPULA (`is silent`) |
| 28 | FAULT-FORM-PERCEPTION (`knows`), FAULT-FORM-INTERIORITY |
| 29 | FAULT-FORM-CONJUNCTION (`and`) |
| 31 | FAULT-FORM-CONJUNCTION (`and`) — likely; "with the ledger sealed in the case" is also borderline modifier |
| 33 | FAULT-FORM-INTERIORITY (`feels`), FAULT-FORM-PERCEPTION (`feels`) |

**Total fault-bearing lines:** 22 of 33 (67%).
**Lines without seeded faults:** 6, 8, 9, 13, 15, 17, 21, 22, 27, 30, 32 (11 of 33 = 33%).

## Pass 3 (shape) — curve faults

- Flatlined opening (lines 1–8 are exposition without rising tension).
- Climax non-uniqueness: lines 21 (refusal of attestation) and 29 (ledger entry) compete.
- Missing transition: between lines 18 (sept doors closed) and 19 (Taylor produces letter).

## Pass 4 (trim) — filler candidates

- Line 2 (Taylor's tiredness — does not serve goal).
- Line 10 (incidental count).
- Line 26 (atmosphere only).
- Line 33 (interiority closer; observed beat is line 32).

## Pass 5 (continuity) — state/reference faults

- Line 19: letter introduced with no prior placement / scene-open establishment.
- Line 16: Septon Osmynd referenced — out-of-cast or off-stage-only-reference (open call).
- Lines 5, 28, 33: POV-leak (perception applied to narrator) — should be caught at pass 2 already; pass 5 backup.

## Aggregate baseline expectation (lift target)

If the four reviewers tuned correctly:
- Pass 2 strict baseline: ~6 of 33 lines CORRECT (= 18%). Faults caught: high recall on FORM-COPULA, FORM-NEGATION, FORM-PERCEPTION; moderate on FORM-MODIFIER, FORM-CONJUNCTION; case-by-case on COMPOUND-OBJECTS (line 11).
- Pass 3: SHAPE-FAIL with named flatline + climax-non-uniqueness + 1 missing transition.
- Pass 4: ≥3 deletions across personas (lines 2, 10, 26, 33 candidates).
- Pass 5: 1 reachability flag (letter setup), 1 reference flag (off-cast slug), 0–3 POV backups.

The pipeline at Phase 5 (post-tuning) should drive these numbers to 100% per-pass clean on a fresh writer dispatch.
