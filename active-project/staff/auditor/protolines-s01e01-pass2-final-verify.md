# Audit Report — s01e01 Proto-lines Pass 2 Final Verify
schema: audit-report
episode: s01e01
run: pass2-final-verify
auditor: fork
date: 2026-05-07

---

## Summary
total non-blank body lines: 47
CORRECT: 47
faults: 0
flags: 1 (advisory — no fixer action required)
file-level: PASS
strict accept rate: 100%

---

## Header

| check | result |
|---|---|
| narrator: taylor-hebert-westeros | PASS — slug present in episode cast |
| goal: present and non-empty | PASS |

---

## Per-line verdicts

| id | line | verdict |
|---|---|---|
| 1 | the ravens lift | CORRECT |
| 2 | taylor-hebert-westeros holds the feet | CORRECT |
| 3 | the cart crests the road | CORRECT |
| 4 | mira-stonefield enters the yard | CORRECT |
| 5 | edric-cray reaches the gate post | CORRECT |
| 8 | the cart stops | CORRECT |
| 9 | census-officer steps | CORRECT |
| 10 | clerk steps | CORRECT |
| 11 | clerk carries the ledger | CORRECT |
| 13 | census-officer speaks to the wards | CORRECT |
| 14 | the wards assemble | CORRECT |
| 15 | taylor-hebert-westeros joins the wards | CORRECT |
| 17 | census-officer speaks to the first ward | CORRECT |
| 18 | clerk opens the ledger | CORRECT |
| 19 | census-officer advances | CORRECT |
| 20 | clerk enters each name | CORRECT |
| 21 | census-officer reaches taylor-hebert-westeros | CORRECT |
| 22 | census-officer speaks to taylor-hebert-westeros | CORRECT |
| 23 | taylor-hebert-westeros speaks to census-officer | CORRECT |
| 24 | census-officer speaks to the wards | CORRECT |
| 25 | the sept door holds | CORRECT |
| 27 | taylor-hebert-westeros produces the letter | CORRECT — see flag F-01 |
| 28 | census-officer takes the letter | CORRECT — see flag F-01 |
| 29 | census-officer unfolds the letter | CORRECT — see flag F-01 |
| 30 | census-officer folds the letter | CORRECT — see flag F-01 |
| 31 | census-officer returns the letter | CORRECT — see flag F-01 |
| 32 | census-officer speaks to taylor-hebert-westeros | CORRECT |
| 33 | taylor-hebert-westeros turns | CORRECT |
| 34 | taylor-hebert-westeros speaks to mira-stonefield | CORRECT |
| 35 | mira-stonefield holds the eyes | CORRECT |
| 36 | taylor-hebert-westeros turns | CORRECT |
| 37 | taylor-hebert-westeros speaks to edric-cray | CORRECT |
| 38 | edric-cray turns | CORRECT |
| 39 | edric-cray steps | CORRECT |
| 40 | the sept door closes | CORRECT |
| 42 | the wards hold | CORRECT |
| 43 | clerk speaks to taylor-hebert-westeros | CORRECT |
| 44 | taylor-hebert-westeros speaks to clerk | CORRECT |
| 45 | clerk enters taylor-hebert-westeros | CORRECT |
| 46 | clerk marks the entry | CORRECT |
| 58 | taylor-hebert-westeros holds the eyes | CORRECT |
| 47 | census-officer speaks to taylor-hebert-westeros | CORRECT |
| 48 | census-officer speaks to the wards | CORRECT |
| 50 | census-officer steps | CORRECT |
| 53 | the cart departs | CORRECT |
| 55 | taylor-hebert-westeros holds the letter | CORRECT — see flag F-01 |
| 56 | taylor-hebert-westeros holds the feet | CORRECT |

---

## Flags (advisory — no fixer action required)

### F-01
- id: F-01
- type: flag
- lines: 27, 28, 29, 30, 31, 55
- what: "the letter" named as prop across six lines. The letter does not appear in loc-harrenhal-sept-environs fixed props list.
- why: Location card lists fixed props only; carried props are actor-state territory. cond-impressment-census-120ac explicitly establishes that Taylor's septon ward documentation exists as her core protection mechanism ("Documentation of protected status: produce evidence of septon ward status") and that "a dying septon can, in principle, formally certify his ward's status." The prop is narratively established by constraint card and is an actor-carried item, not a location-fixed prop. FAULT-PHYSICAL-PROP-ABSENT does not apply to actor-carried props — that class is location-card-scoped. No fixer action warranted. Advisory: facet pass (state-updates) should confirm the letter appears in taylor-hebert-westeros actor state at episode open.

---

## Constraint checks

All constraint cards loaded: cond-fauna-control-rules, cond-impressment-census-120ac, cond-riverlands-120ac-state, cond-westerosi-customary-authority, cond-no-parahuman-infrastructure, cond-series-tone-constraints.

No proto-line violates any constraint. Fauna-control is not invoked in any line. No parahuman acts appear. No interiority attributed to a proto-line. The census procedure as rendered (assembly, ledger, name entry, document inspection, special mark) is consistent with cond-impressment-census-120ac process steps. Taylor's production of the letter and the census-officer's inspection sequence is consistent with the "Documentation of protected status" pathway defined in that card. The `clerk marks the entry` beat (line 46) is consistent with "flagged case" notation described in cond-impressment-census-120ac §"What the Maester Specifically Does."

---

## Physical checks

All five actors (taylor-hebert-westeros, census-officer, clerk, mira-stonefield, edric-cray) appear in the episode cast roster. No actor appears who is not on the roster. No exit named that does not exist in loc-harrenhal-sept-environs (the sept door, the gate post, and the yard are all confirmed features of the location). No invalid exit used.

---

## Non-monotonic ID note

IDs 6, 12, 41, 51, 52, 57 are gaps (deletions). ID 58 appears between IDs 46 and 47. All noted in task brief as expected. No schema fault — the proto-line schema states "Deletions leave the ID gap visible. A skipped ID = a deleted proto-line. Do not renumber to fill gaps." Non-monotonic order is structural, not a violation.

---

## Termination

Zero faults. File is CONTINUITY-OK. Orchestrator may advance to pass 3.
