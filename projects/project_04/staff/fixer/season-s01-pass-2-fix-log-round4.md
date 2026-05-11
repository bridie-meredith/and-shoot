# Fixer Log — season s01 Pass 2 Round 4 (pattern-sweep)
session: 2026-05-09

---

## SESSION-START — 2026-05-09T13:00:00Z — season-s01-pass-2-round4-pattern-sweep
dispatch: fixer round 4 — close 11 surviving instances + pattern-sweep entire file for identical forms
target: active-project/theater/proto-lines/s01.aggregate.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint-reaudit-r4.md
findings-queued: 11 named + N pattern-sweep candidates
note: this iteration is justified by missed-pattern-sweep (not new classes). Round-5 audit verifies convergence.

## SESSION-START — 2026-05-09T14:00:00Z — season-s01-pass-2-round4-pattern-sweep
dispatch: fixer round 4 — close 11 surviving instances + pattern-sweep entire file for identical forms
target: active-project/theater/proto-lines/s01.aggregate.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint-reaudit-r4.md
findings-queued: 11 named + N pattern-sweep candidates
note: this iteration is justified by missed-pattern-sweep (not new classes). Round-5 audit verifies convergence.

---

## r4-fault-001 — RESOLVED-PRE-EXISTING
fault: ID 466 `the lead horse rears` — adjective `lead` on subject
scope: line
change: No edit required. Current file reads `the horse rears`. Already fixed.
criteria met: yes

## r4-fault-002 — RESOLVED-PRE-EXISTING
fault: ID 206 `septon-rowan offers the second volume` — ordinal `second` on object
scope: line
change: No edit required. Current file reads `septon-rowan offers the volume`. Already fixed.
criteria met: yes

## r4-fault-003 — RESOLVED-PRE-EXISTING
fault: ID 895 `the ferryman takes the return folio` — adjective `return` on object
scope: line
change: No edit required. Current file reads `the ferryman takes the folio`. Already fixed.
criteria met: yes

## r4-fault-004 — RESOLVED-PRE-EXISTING
fault: ID 898 `the ferryman grips the return folio` — adjective `return` on object
scope: line
change: No edit required. Current file reads `the ferryman grips the folio`. Already fixed.
criteria met: yes

## r4-fault-005 — RESOLVED-PRE-EXISTING
fault: ID 372 `the fishwife steps to the table` — destination prep phrase `to the table`
scope: line
change: No edit required. Current file reads `the fishwife approaches the table`. Already fixed.
criteria met: yes

## r4-fault-006 — RESOLVED-PRE-EXISTING
fault: ID 849 `the maester crosses to the workshop center` — destination prep phrase `to the workshop center`
scope: line
change: No edit required. Current file reads `the maester reaches the workshop center`. Already fixed.
criteria met: yes

## r4-fault-007 — RESOLVED-PRE-EXISTING
fault: ID 761 `oc-craftsman-mother crosses to the shelf` — destination prep phrase `to the shelf`
scope: line
change: No edit required. Current file reads `oc-craftsman-mother approaches the shelf`. Already fixed.
criteria met: yes

## r4-fault-008 — RESOLVED-PRE-EXISTING
fault: ID 547 `the inquiry rider draws the sealed letter` — adjective `sealed` on object
scope: line
change: No edit required. Current file reads `the inquiry rider draws the letter`. Already fixed.
criteria met: yes

## r4-fault-009 — RESOLVED-PRE-EXISTING
fault: ID 234 `septon-rowan draws a second volume` — ordinal `second` on object
scope: line
change: No edit required. Current file reads `septon-rowan draws a volume`. Already fixed.
criteria met: yes

## r4-fault-010 — RESOLVED-PRE-EXISTING
fault: ID 314 `the square insects shift` — environment-state collective
scope: line
change: No edit required. Current file shows ID 314 as blank (time-skip). Already deleted.
criteria met: yes

## r4-fault-011 — RESOLVED-PRE-EXISTING
fault: ID 835 `oc-craftsman-father draws the door wider` — modifier `wider` appended after direct object
scope: line
change: No edit required. Current file reads `oc-craftsman-father draws the door`. Already fixed.
criteria met: yes

---

## PATTERN-SWEEP — Cluster B (destination prepositions on motion verbs)

Swept entire file for: `crosses to X`, `steps to X`, `moves to X`, `walks to X`, `turns to X`, `steps from X`.

### r4-sweep-1 — scope: Cluster B (source prep) — ID 558
fault: `mira-stonefield-jaehaerys steps from the alley entrance` — `from the alley entrance` is a banned source prepositional phrase appended to motion verb
scope: line
change: recast → `mira-stonefield-jaehaerys exits the alley`
criteria met: yes

### Cluster B borderline advisory (not fixed)
- ID 337: `a townsman steps back` — `back` directional adverb. Audit r4 passed as advisory, not fault. Consistent with r3 pass. No action.
- ID 439: `oc-craftsman-father steps forward` — `forward` directional adverb. Same form as ID 337. Audit passed `steps back` as advisory; `steps forward` treated identically. No action.
- ID 562: `mira-stonefield-jaehaerys steps back` — same form as ID 337. Advisory. No action.

---

## PATTERN-SWEEP — Cluster E (adjective modifiers on nouns)

Swept entire file for adjective+noun constructions: ordinals, descriptive adjectives, participial adjectives.

### r4-sweep-2 — scope: Cluster E — ID 238
fault: `taylor-hebert-jaehaerys marks the practice column` — `practice` is an adjective modifier on `column`
scope: line
change: stripped `practice` → `taylor-hebert-jaehaerys marks the column`
criteria met: yes

### Cluster E compound-noun passes (not fixed — compound noun readings confirmed by audit)
The following were reviewed and confirmed as compound nouns or already-passed borderlines; no fault:
- ID 88: `market satchel` — compound noun prop (audit-confirmed PASS)
- ID 107: `account ledger` — compound noun prop
- ID 144: `winter-candle` — hyphenated compound noun prop
- ID 246: `morning light` / `east window` — audit flagged as advisory r4-flag-003, not fault
- ID 248: `altar cloth` — compound noun prop
- ID 268: `the two children` — audit flagged as advisory r4-flag-005, not fault
- ID 298: `grain-stall fence rail` — compound noun structural element
- ID 360: `household entry column` — compound noun (audit-confirmed PASS)
- ID 399: `sept literacy folio` — compound noun document type
- ID 496: `incident folio` — compound noun
- ID 604: `inquiry folio` — compound noun

---

## PATTERN-SWEEP — Cluster G (environment-state subjects)

Swept entire file for `the <space-noun> <verb>` patterns where verb describes ambient/collective state.

No new instances found. All environment-state subjects previously fixed (IDs 54, 77, 122, 146, 153, 154, 225, 258, 262, 300, 301, 329, 350, 413, 416, 419, 420, 425, 432, 490, 509, 513, 515, 517, 535, 556, 566, 646, 671, 703, 733, 734, 736, 740, 750, 792, 813, 819, 820, 887, 902, 908 are all time-skip or recast).

Discrete prop-as-subject events (doors opening/closing, lamp catching, ferry grounding) confirmed PASS — not environment-state, they are physical discrete events.

---

## SESSION-END — 2026-05-09T14:30:00Z — season-s01-pass-2-round4-pattern-sweep
named-findings-applied: 0 (all 11 RESOLVED-PRE-EXISTING)
sweep-findings-applied: 2 (r4-sweep-1: ID 558; r4-sweep-2: ID 238)
findings-pre-existing: 11
findings-skipped: 0
exit: CLEAN
