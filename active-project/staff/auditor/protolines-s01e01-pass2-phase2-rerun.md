# Audit Report — proto-lines s01e01 pass 2 phase 2.5 re-run
schema: schemas/audit-report.schema.md
episode: s01e01
file reviewed: design/shoot-v2/phase2-svo-writer-fork-output.md (post-fixer)
run: pass 2 re-run after 29-fault fixer repair

---

## Summary

```
total body lines (non-blank): 51
blank lines (time-skips): 6
CORRECT: 50
faults: 1
  FAULT-FORM-INTERIORITY: 1
file-level: FAIL
strict accept rate: 98.0%
```

---

## Header check

- `narrator: taylor-hebert-westeros` — slug present in active cast roster. PASS.
- `goal:` — present and non-empty. PASS.

---

## Time-skip validity

All six blank lines (IDs 7, 16, 26, 41, 49, 54) sit between beats with a defensible temporal gap. None appear between continuous-action beats with no elapsed time. All VALID.

---

## Findings

### fault-001

- **id:** fault-001
- **type:** fault
- **line id:** 42
- **line content:** `42 the wards hold their positions`
- **fault class:** FAULT-FORM-INTERIORITY
- **what:** Object `their positions` is a spatial abstraction, not a concrete physical object. Compare: `the yard holds the silence` (banned example from svo-split-notes / svo-writer-pass1-brief — abstraction-as-object). `positions` is not a named physical thing an observer can point to; it is a relational spatial concept.
- **why:** Abstraction-as-object lines import state-assertion content (the wards are in a particular spatial disposition) into a proto-line slot. This contaminates the SVO bone layer with content that belongs in loc-state facets and causes the stitcher to treat a state-assertion as a physical event beat.
- **criteria:** Replace `their positions` with no object (intransitive `the wards hold`) or split into per-actor lines (`taylor-hebert-westeros holds`, `mira-stonefield holds`, `edric-cray holds`) if individual actor distinction is narratively required.
- **recommended fixer action:** RECAST-AS-HOLD — drop the object entirely: `42 the wards hold`

---

## Per-line verdicts (non-blank lines)

| ID | Line | Verdict |
|----|------|---------|
| 1 | the ravens lift | CORRECT |
| 2 | taylor-hebert-westeros holds the feet | CORRECT |
| 3 | the cart crests the road | CORRECT |
| 4 | mira-stonefield moves | CORRECT |
| 5 | edric-cray moves | CORRECT |
| 6 | the wards move | CORRECT |
| 8 | the cart stops | CORRECT |
| 9 | census-officer steps | CORRECT |
| 10 | clerk steps | CORRECT |
| 11 | clerk carries the ledger | CORRECT |
| 12 | clerk carries the ink case | CORRECT |
| 13 | census-officer speaks to the yard | CORRECT |
| 14 | the wards assemble | CORRECT |
| 15 | taylor-hebert-westeros moves | CORRECT |
| 17 | census-officer speaks to the first ward | CORRECT |
| 18 | clerk opens the ledger | CORRECT |
| 19 | census-officer advances | CORRECT |
| 20 | clerk enters each name | CORRECT |
| 21 | census-officer reaches taylor-hebert-westeros | CORRECT |
| 22 | census-officer speaks to taylor-hebert-westeros | CORRECT |
| 23 | taylor-hebert-westeros speaks to census-officer | CORRECT |
| 24 | census-officer speaks to the sept doors | CORRECT |
| 25 | the sept doors hold | CORRECT |
| 27 | taylor-hebert-westeros produces the letter | CORRECT |
| 28 | census-officer takes the letter | CORRECT |
| 29 | census-officer unfolds the letter | CORRECT |
| 30 | census-officer folds the letter | CORRECT |
| 31 | census-officer returns the letter | CORRECT |
| 32 | census-officer speaks to taylor-hebert-westeros | CORRECT |
| 33 | taylor-hebert-westeros turns | CORRECT |
| 34 | taylor-hebert-westeros speaks to mira-stonefield | CORRECT |
| 35 | mira-stonefield holds the eyes | CORRECT |
| 36 | taylor-hebert-westeros turns | CORRECT |
| 37 | taylor-hebert-westeros speaks to edric-cray | CORRECT |
| 38 | edric-cray turns | CORRECT |
| 39 | edric-cray steps | CORRECT |
| 40 | the sept door closes | CORRECT |
| 42 | the wards hold their positions | FAULT-FORM-INTERIORITY |
| 43 | clerk speaks to taylor-hebert-westeros | CORRECT |
| 44 | taylor-hebert-westeros speaks to clerk | CORRECT |
| 45 | clerk enters taylor-hebert-westeros | CORRECT |
| 46 | clerk marks the entry | CORRECT |
| 47 | census-officer speaks to taylor-hebert-westeros | CORRECT |
| 48 | census-officer speaks to the yard | CORRECT |
| 50 | census-officer steps | CORRECT |
| 51 | clerk steps | CORRECT |
| 52 | clerk closes the ink case | CORRECT |
| 53 | the cart moves | CORRECT |
| 55 | taylor-hebert-westeros holds the letter | CORRECT |
| 56 | taylor-hebert-westeros holds the feet | CORRECT |
| 57 | the yard holds | CORRECT |

---

## Constraint audit

- **cond-fauna-control-rules:** Line 1 (`the ravens lift`) records a physical act without asserting fauna-control. No constraint violation.
- **cond-impressment-census-120ac:** Census sequence (arrival, ledger open, name-entry, mark, departure) is procedurally consistent with the card. Ward-status claim via letter (lines 27–31) is consistent with the card's septon-last-intervention provision. No violation.
- **cond-riverlands-120ac-state:** No violation.
- **cond-westerosi-customary-authority:** Ward compliance posture throughout the sequence is consistent with the card's compliance-and-document option. No violation.
- **cond-no-parahuman-infrastructure:** No parahuman act implied by any line. No violation.
- **cond-series-tone-constraints:** Not applicable at SVO bone layer (tone constraints govern prose register, not proto-line content). No applicable fault.
- **Series laws:** No law violated across all 51 lines.

---

## Physical audit

- `the letter` (lines 27–31, 55): consistent with septon-ward certification documentation established by cond-impressment-census-120ac. No FAULT-PHYSICAL-PROP-ABSENT.
- `the ledger` (line 11 establishes clerk carries it; used at lines 18, 20, 45, 46): prop present. PASS.
- `the ink case` (line 12 establishes clerk carries it; closed at line 52): prop present. PASS.
- `the sept door` / `the sept doors` (lines 24, 25, 40): location card confirms west-entry door exists. PASS.
- `the cart` (lines 3, 8, 53): location card confirms road approach from Harrenhal; cart is physically possible at this location. PASS.
- All actors (taylor-hebert-westeros, census-officer, clerk, mira-stonefield, edric-cray, `the wards`) are present in the active cast or as valid unnamed-group entities. No FAULT-PHYSICAL-ACTOR-ABSENT.
- No invalid exits named. PASS.
