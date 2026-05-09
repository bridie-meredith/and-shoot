# SVO Writer Phase 2 Fix Log

source-file: design/shoot-v2/phase2-svo-writer-fork-output.md
audit-report: active-project/staff/auditor/protolines-s01e01-pass2-phase2.md
date: 2026-05-07
faults-in: 29
faults-applied: 29
faults-skipped: 0

---

| id | action | before | after |
|----|--------|--------|-------|
| fault-001 | DELETE trailing phrase | `the ravens lift from the bell tower` | `the ravens lift` |
| fault-002 | DELETE trailing phrase | `taylor-hebert-westeros holds the feet on the flagstones` | `taylor-hebert-westeros holds the feet` |
| fault-003 | DELETE trailing phrase | `the cart crests the road from the north` | `the cart crests the road` |
| fault-004 | DELETE destination phrase | `mira-stonefield moves to the yard` | `mira-stonefield moves` |
| fault-005 | DELETE destination phrase | `edric-cray moves to the gate post` | `edric-cray moves` |
| fault-006 | RECAST subject + DELETE destination phrase | `the other wards move into the yard` | `the wards move` |
| fault-007 | DELETE trailing phrase | `the cart stops at the sept gate` | `the cart stops` |
| fault-008 | DELETE trailing phrase | `census-officer steps through the sept gate` | `census-officer steps` |
| fault-009 | DELETE trailing phrase | `clerk steps through the sept gate` | `clerk steps` |
| fault-010 | DELETE trailing phrase | `the wards assemble in the yard` | `the wards assemble` |
| fault-011 | DELETE purpose clause | `taylor-hebert-westeros moves to stand with the assembled wards` | `taylor-hebert-westeros moves` |
| fault-012 | RECAST to specific verb without path-phrase | `census-officer works through the ward line` | `census-officer advances` |
| fault-013 | DELETE trailing phrase | `clerk enters each name into the ledger` | `clerk enters each name` |
| fault-014 | RECAST-AS-HOLD without adjective | `the sept doors hold closed` | `the sept doors hold` |
| fault-015 | DELETE (abstraction-as-object; FAULT-FORM-INTERIORITY) | `the yard holds the silence` (line 26) | blank numbered line (time-skip form) |
| fault-016 | DELETE trailing recipient phrase (SPLIT-OR-DELETE; chose delete to avoid adding new IDs without directive) | `census-officer returns the letter to taylor-hebert-westeros` | `census-officer returns the letter` |
| fault-017 | DELETE trailing phrase | `taylor-hebert-westeros turns toward mira-stonefield` | `taylor-hebert-westeros turns` |
| fault-018 | DELETE trailing phrase | `mira-stonefield holds the eyes on the yard stones` | `mira-stonefield holds the eyes` |
| fault-019 | DELETE trailing phrase | `taylor-hebert-westeros turns toward edric-cray` | `taylor-hebert-westeros turns` |
| fault-020 | DELETE trailing phrase | `edric-cray turns toward the sept door` | `edric-cray turns` |
| fault-021 | DELETE trailing phrase | `edric-cray steps through the sept door` | `edric-cray steps` |
| fault-022 | DELETE (abstraction-as-object; FAULT-FORM-INTERIORITY; duplicate of fault-015) | `the yard holds the silence` (line 41) | blank numbered line (time-skip form) |
| fault-023 | DELETE trailing phrase | `clerk enters taylor-hebert-westeros into the ledger` | `clerk enters taylor-hebert-westeros` |
| fault-024 | DELETE trailing phrase | `clerk marks the entry with a double stroke` | `clerk marks the entry` |
| fault-025 | DELETE trailing phrase | `census-officer steps through the sept gate` (line 50) | `census-officer steps` |
| fault-026 | DELETE trailing phrase | `clerk steps through the sept gate` (line 51) | `clerk steps` |
| fault-027 | DELETE trailing phrase | `the cart moves off down the road` | `the cart moves` |
| fault-028 | DELETE trailing phrase | `taylor-hebert-westeros holds the feet on the flagstones` (line 56) | `taylor-hebert-westeros holds the feet` |
| fault-029 | DELETE adjective complement | `the yard holds empty` | `the yard holds` |

---

## Notes

fault-015 / fault-022: Both `the yard holds the silence` instances (lines 26 and 41) converted to blank numbered lines. Atmospheric content (tension, silence) should be routed to tensometer/narrator facets citing adjacent proto-line IDs per audit recommended-action.

fault-016: Recommended-action offered SPLIT-INTO-2 or DELETE. Split would require inserting a new line between 31 and 32, displacing IDs or consuming an unassigned ID — neither is sanctioned without showrunner direction. Minimum-change option (DELETE trailing phrase) applied. `taylor-hebert-westeros takes the letter` beat is absent; flagged for showrunner if the beat is narratively load-bearing.
