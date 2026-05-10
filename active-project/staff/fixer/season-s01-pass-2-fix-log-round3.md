# Fixer Log — season s01 pass-2 round 3 (over-cap iteration)

## SESSION-START — 2026-05-09T00:30:00Z — season-s01-pass-2-round3-overcap
dispatch: fixer round 3 — apply round-3 audit findings (84 new faults: prep-padding cluster + adjective-modifier cluster)
target: active-project/theater/proto-lines/s01.aggregate.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint-reaudit-r3.md
findings-queued: 84 (read audit to confirm exact count)
note: over-cap iteration. User authorized via "get this shit fixed" + full permissions. Rationale in escalation-pass2-cap-decision.md.

## SESSION-RESUME — 2026-05-09T00:31:00Z
findings-queued: confirmed 84 fault findings (r3-fault-001 through r3-fault-084) across ~70 distinct IDs.
clusters: A(2) B(7) C(8) D(8) E(46) F(5) G(8) H(1) I(1) — some IDs carry dual faults, counted once per fault-ID.
note: Some fault IDs share the same aggregate line ID (e.g., IDs 436 and 443 each carry two separate faults). Will apply all corrections to each line in a single edit pass.

## SESSION-START — 2026-05-09T12:00:00Z — season-s01-pass-2-round3-overcap
dispatch: fixer round 3 — apply round-3 audit findings (84 new faults: prep-padding cluster + adjective-modifier cluster)
target: active-project/theater/proto-lines/s01.aggregate.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint-reaudit-r3.md
findings-queued: 84 (confirmed by audit Section 5)
note: over-cap iteration. User authorized. Rationale in escalation-pass2-cap-decision.md.

## SESSION-RESUME — 2026-05-09T12:01:00Z
findings-queued: confirmed 84 fault findings (r3-fault-001 through r3-fault-084) across ~70 distinct IDs.
clusters: A(2) B(7) C(8) D(8) E(46) F(5) G(8) H(1) I(1) — some IDs carry dual faults, counted once per fault-ID.

## r3-fault-001 — RESOLVED
fault: ID 250 adverb `again` on `traces the column again`
scope: line
change: stripped `again` → `taylor-hebert-jaehaerys traces the column`
criteria met: yes

## r3-fault-002 — RESOLVED
fault: ID 618 adverb `again` on `marks the folio again`
scope: line
change: stripped `again` → `oc-lords-steward marks the folio`
criteria met: yes

## r3-fault-003 — RESOLVED
fault: ID 20 destination prep phrase `returns to the workshop doorway`
scope: line
change: recast → `taylor-hebert-jaehaerys approaches the workshop doorway`
criteria met: yes

## r3-fault-004 — RESOLVED
fault: ID 47 destination prep phrase `returns to the mordant station`
scope: line
change: recast → `oc-craftsman-mother approaches the mordant station`
criteria met: yes

## r3-fault-005 — RESOLVED
fault: ID 120 destination prep phrase `returns to the ledger bench`
scope: line
change: recast → `taylor-hebert-jaehaerys approaches the ledger bench`
criteria met: yes

## r3-fault-006 — RESOLVED
fault: ID 702 destination prep phrase `crosses to the sept lane entrance`
scope: line
change: recast → `oc-craftsman-mother approaches the sept lane entrance`
criteria met: yes

## r3-fault-007 — RESOLVED
fault: ID 67 destination prep phrase `rolls onto the pallet`
scope: line
change: recast → `taylor-hebert-jaehaerys reaches the pallet`
criteria met: yes

## r3-fault-008 — RESOLVED
fault: ID 28 source prep phrase `from the ink-pot rim`
scope: line
change: stripped → `the fly lifts`
criteria met: yes

## r3-fault-009 — RESOLVED
fault: ID 55 source prep phrase `from the bench`
scope: line
change: stripped → `taylor-hebert-jaehaerys rises`
criteria met: yes

## r3-fault-010 — RESOLVED
fault: ID 59 source prep phrase `from the pot`
scope: line
change: stripped → `oc-craftsman-mother fills the bowl`
criteria met: yes

## r3-fault-011 — RESOLVED
fault: ID 125 source prep phrase `from the gutter`
scope: line
change: stripped → `the swallow lifts`
criteria met: yes

## r3-fault-012 — RESOLVED
fault: ID 160 source prep phrase `from the altar cloth`
scope: line
change: stripped → `septon-rowan rises`
criteria met: yes

## r3-fault-013 — RESOLVED
fault: ID 263 source prep phrase `from the livestock pen corner`
scope: line
change: stripped → `a fly lifts`
criteria met: yes

## r3-fault-014 — RESOLVED
fault: ID 668 source prep phrase `from the mordant cloth`
scope: line
change: stripped → `oc-craftsman-mother pulls her hands`
criteria met: yes

## r3-fault-015 — RESOLVED
fault: ID 704 dual: source phrase `from the south lane` + adjective `south`
scope: line
change: stripped both → `oc-craftsman-mother enters the sept`
criteria met: yes

## r3-fault-016 — RESOLVED
fault: ID 11 location prep phrase `at the dye-yard drain`
scope: line
change: stripped → `the flies cluster`
criteria met: yes

## r3-fault-017 — RESOLVED
fault: ID 13 location prep phrase `by the vat`
scope: line
change: stripped → `the beetles trace the floor seam`
criteria met: yes

## r3-fault-018 — RESOLVED
fault: ID 54 dual: location phrase `at the drain` + collective-state `regroup`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-019 — RESOLVED
fault: ID 70 location prep phrase `at the vent edge`
scope: line
change: stripped → `the moth lands`
criteria met: yes

## r3-fault-020 — RESOLVED
fault: ID 353 location prep phrase `on the table`
scope: line
change: stripped → `a clerk sets the census roll`
criteria met: yes

## r3-fault-021 — RESOLVED
fault: ID 436 dual: location phrase `on the table` + ordinal `first`
scope: line
change: stripped both → `the townsman sets the coin`
criteria met: yes

## r3-fault-022 — RESOLVED
fault: ID 443 dual: location phrase `on the stone` + ordinal `second`
scope: line
change: stripped both → `the townsman sets the grain sack`
criteria met: yes

## r3-fault-023 — RESOLVED
fault: ID 479 destination prep phrase `to the rail`
scope: line
change: stripped → `the animal-pen flies return`
criteria met: yes

## r3-fault-024 — RESOLVED
fault: ID 452 ordinal `second` in possessive chain
scope: line
change: stripped → `the collector's man grabs the townsman's sleeve`
criteria met: yes

## r3-fault-025 — RESOLVED
fault: ID 453 ordinal `second` on subject
scope: line
change: stripped → `the townsman pulls the sleeve`
criteria met: yes

## r3-fault-026 — RESOLVED
fault: ID 457 ordinal `second` on subject
scope: line
change: stripped → `the townsman shoves the collector's man`
criteria met: yes

## r3-fault-027 — RESOLVED
fault: ID 463 ordinal `second` on subject
scope: line
change: stripped → `the horse shies`
criteria met: yes

## r3-fault-028 — RESOLVED
fault: ID 471 ordinal `first` on subject (dual with r3-fault-073)
scope: line
change: stripped ordinal + recast bare intransitive → `the collector retreats`
criteria met: yes

## r3-fault-029 — RESOLVED
fault: ID 472 ordinal `first` on subject (dual with r3-fault-074)
scope: line
change: stripped ordinal + added destination → `the collector's man exits the square`
criteria met: yes

## r3-fault-030 — RESOLVED
fault: ID 473 ordinal `second` on subject
scope: line
change: stripped → `the collector's man covers his face`
criteria met: yes

## r3-fault-031 — RESOLVED
fault: ID 480 adjective `lead` on subject
scope: line
change: stripped → `the horse settles`
criteria met: yes

## r3-fault-032 — RESOLVED
fault: ID 481 ordinal `first` on subject
scope: line
change: stripped → `the collector's man wipes the forearm`
criteria met: yes

## r3-fault-033 — RESOLVED
fault: ID 491 ordinal `second` on subject
scope: line
change: stripped → `the collector's man lifts the levy roll`
criteria met: yes

## r3-fault-034 — RESOLVED
fault: ID 495 ordinal `second` on subject
scope: line
change: stripped → `the collector speaks to oc-lords-steward`
criteria met: yes

## r3-fault-035 — RESOLVED
fault: ID 436 ordinal `first` on subject (same line as r3-fault-021 — single combined edit)
scope: line
change: handled in r3-fault-021 combined edit
criteria met: yes

## r3-fault-036 — RESOLVED
fault: ID 441 ordinal `second` on subject
scope: line
change: stripped → `the townsman approaches the table`
criteria met: yes

## r3-fault-037 — RESOLVED
fault: ID 443 ordinal `second` on subject (same line as r3-fault-022 — single combined edit)
scope: line
change: handled in r3-fault-022 combined edit
criteria met: yes

## r3-fault-038 — RESOLVED
fault: ID 444 ordinal `second` on listener object
scope: line
change: stripped → `the collector's man speaks to the townsman`
criteria met: yes

## r3-fault-039 — RESOLVED
fault: ID 445 ordinal `second` on subject
scope: line
change: stripped → `the townsman speaks to the collector's man`
criteria met: yes

## r3-fault-040 — RESOLVED
fault: ID 448 ordinal `second` on subject
scope: line
change: stripped → `the townsman speaks to the collector`
criteria met: yes

## r3-fault-041 — RESOLVED
fault: ID 450 ordinal `second` on subject
scope: line
change: stripped → `the townsman speaks to the collector`
criteria met: yes

## r3-fault-042 — RESOLVED
fault: ID 464 ordinal `second` in possessive on object
scope: line
change: stripped → `rymer-hedge grabs the horse's bridle`
criteria met: yes

## r3-fault-043 — RESOLVED
fault: ID 482 ordinal `second` on object
scope: line
change: stripped → `rymer-hedge steadies the horse`
criteria met: yes

## r3-fault-044 — RESOLVED
fault: ID 494 ordinal `second` on listener
scope: line
change: stripped → `oc-lords-steward speaks to the collector`
criteria met: yes

## r3-fault-045 — RESOLVED
fault: ID 500 ordinal `first` on listener
scope: line
change: stripped → `oc-lords-steward speaks to the collector`
criteria met: yes

## r3-fault-046 — RESOLVED
fault: ID 516 ordinal `second` in possessive on object
scope: line
change: stripped → `rymer-hedge releases the horse's bridle`
criteria met: yes

## r3-fault-047 — RESOLVED
fault: ID 7 adjective `front` on object
scope: line
change: stripped → `taylor-hebert-jaehaerys reaches the shutter`
criteria met: yes

## r3-fault-048 — RESOLVED
fault: ID 24 modifier `open` appended after direct object
scope: line
change: stripped → `oc-craftsman-father sets the ledger`
criteria met: yes

## r3-fault-049 — RESOLVED
fault: ID 69 modifier `open` appended after direct object
scope: line
change: stripped → `taylor-hebert-jaehaerys holds the eyes`
criteria met: yes

## r3-fault-050 — RESOLVED
fault: ID 78 compound adjective `drain-side` on object `web`
scope: line
change: stripped → `the dye-yard spiders repair the web`
criteria met: yes

## r3-fault-051 — RESOLVED
fault: ID 148 adjective `new` on subject
scope: line
change: stripped → `the candle catches`
criteria met: yes

## r3-fault-052 — RESOLVED
fault: ID 156 superlative adjective `nearest` on object
scope: line
change: stripped → `taylor-hebert-jaehaerys opens the volume`
criteria met: yes

## r3-fault-053 — RESOLVED
fault: ID 182 ordinal `second` on object
scope: line
change: stripped → `septon-rowan draws a stool`
criteria met: yes

## r3-fault-054 — RESOLVED
fault: ID 184 ordinal `second` on object
scope: line
change: stripped → `septon-rowan opens a volume`
criteria met: yes

## r3-fault-055 — RESOLVED
fault: ID 235 ordinal `second` on object
scope: line
change: stripped → `septon-rowan opens the volume`
criteria met: yes

## r3-fault-056 — RESOLVED
fault: ID 243 dual: ordinal `second` + destination `to the shelf`
scope: line
change: stripped both → `septon-rowan returns the volume`
criteria met: yes

## r3-fault-057 — RESOLVED
fault: ID 326 gerund adjective `marketing` on object `basket`
scope: line
change: stripped → `oc-craftsman-mother lifts the basket`
criteria met: yes

## r3-fault-058 — RESOLVED
fault: ID 378 participial adjective `disputed` on object
scope: line
change: stripped → `oc-lords-steward draws the column`
criteria met: yes

## r3-fault-059 — RESOLVED
fault: ID 379 participial adjective `disputed` on object
scope: line
change: stripped → `the clerk marks the entry`
criteria met: yes

## r3-fault-060 — RESOLVED
fault: ID 396 adjective `next` on object
scope: line
change: stripped → `oc-lords-steward faces the household`
criteria met: yes

## r3-fault-061 — RESOLVED
fault: ID 510 participial adjective `overturned` on object
scope: line
change: stripped → `the garrison man approaches the table`
criteria met: yes

## r3-fault-062 — RESOLVED
fault: ID 648 adjective `east` on object
scope: line
change: stripped → `rymer-hedge faces the entrance`
criteria met: yes

## r3-fault-063 — RESOLVED
fault: ID 656 modifier `closed` appended after direct object
scope: line
change: stripped → `oc-craftsman-father draws the workshop door`
criteria met: yes

## r3-fault-064 — RESOLVED
fault: ID 794 adverb `down` appended after direct object
scope: line
change: stripped → `oc-craftsman-mother sets the cup`
criteria met: yes

## r3-fault-065 — RESOLVED
fault: ID 796 adjective `evening` on subject
scope: line
change: stripped → `the lamp catches`
criteria met: yes

## r3-fault-066 — RESOLVED
fault: ID 802 participial adjective `traveling` on subject
scope: line
change: stripped → `the maester enters Fairstead`
criteria met: yes

## r3-fault-067 — RESOLVED
fault: ID 808 adjective `sealed` on object
scope: line
change: stripped → `the maester draws the folio`
criteria met: yes

## r3-fault-068 — RESOLVED
fault: ID 893 dual: adjective `sealed` + adjective `return` on object
scope: line
change: stripped both → `the maester draws the folio`
criteria met: yes

## r3-fault-069 — RESOLVED
fault: ID 330 dual: compound adjective `flat-bottom` on subject + adjective `near` on object
scope: line
change: stripped both → `the ferry grounds the bank`
criteria met: yes

## r3-fault-070 — RESOLVED
fault: ID 322 bare intransitive motion `approaches` without destination
scope: line
change: added destination slug → `oc-craftsman-mother approaches taylor-hebert-jaehaerys`
criteria met: yes

## r3-fault-071 — RESOLVED
fault: ID 335 bare intransitive motion `rides` without destination
scope: line
change: recast with destination → `rymer-hedge reaches the dock apron`
criteria met: yes

## r3-fault-072 — RESOLVED
fault: ID 400 bare intransitive motion `approaches` without destination
scope: line
change: added destination slug → `septon-rowan approaches oc-lords-steward`
criteria met: yes

## r3-fault-073 — RESOLVED
fault: ID 471 bare intransitive `scrambles` (dual with r3-fault-028)
scope: line
change: handled in r3-fault-028 combined edit → `the collector retreats`
criteria met: yes

## r3-fault-074 — RESOLVED
fault: ID 472 bare intransitive `runs` (dual with r3-fault-029)
scope: line
change: handled in r3-fault-029 combined edit → `the collector's man exits the square`
criteria met: yes

## r3-fault-075 — RESOLVED
fault: ID 146 environment-state `the lamp glow shifts`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-076 — RESOLVED
fault: ID 413 collective multi-subject `the retinue remounts`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-077 — RESOLVED
fault: ID 416 collective multi-subject `the column crosses the dock apron`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-078 — RESOLVED
fault: ID 517 collective multi-subject `the column exits the square`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-079 — RESOLVED
fault: ID 733 environment-state `the workshop lane branches`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-080 — RESOLVED
fault: ID 734 environment-state `the market lane branches`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-081 — RESOLVED
fault: ID 740 stative position-naming `the reeve's house door faces the lane`
scope: line
change: deleted (time-skip marker)
criteria met: yes

## r3-fault-082 — RESOLVED
fault: ID 54 dual: collective-state `regroup` + location phrase `at the drain`
scope: line
change: handled in r3-fault-018 combined edit (deleted)
criteria met: yes

## r3-fault-083 — RESOLVED
fault: ID 468 dual: abstract object `throws its weight` + adjective `lead` on subject
scope: line
change: recast → `the horse lunges`
criteria met: yes

## r3-fault-084 — RESOLVED
fault: ID 894 destination prep `to the ferryman` on complete SVO + `return` adjective on object
scope: line
change: recast to double-object form + stripped adjective → `the maester passes the ferryman the folio`
criteria met: yes

## SESSION-END — 2026-05-09T12:30:00Z — season-s01-pass-2-round3-overcap
findings-applied: 84 (all RESOLVED; 0 pre-existing; 0 skipped)
findings-pre-existing: 0
findings-skipped: 0
concurrent-write-detections: none
dependency-conflicts: none
exit: CLEAN
