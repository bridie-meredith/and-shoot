audit:
  scope: episode
  target: s01e01 — proto-line inventory (phase2 screen-writer fork)
  timestamp: 2026-05-07
  pass: 2 — constraint audit

## Summary
total body lines: 53
CORRECT: 24
faults: 29 (FAULT-FORM-MODIFIER: 27, FAULT-FORM-INTERIORITY: 2)
file-level: FAIL

---

## Header findings

No header faults. `narrator: taylor-hebert-westeros` resolves to an active cast member. `goal:` is present and non-empty.

---

## Fault entries

- id: fault-001
  type: fault
  what: "line 1 — `the ravens lift from the bell tower`"
  why: `from the bell tower` is a prepositional place-specifier. Schema rule: time and place belong in location-state citations, not in the proto-line body. Prepositional padding present.
  criteria: line must be reducible to SVO without the place phrase; location context belongs in a loc-state citation accrued at facet-authoring time.
  recommended-action: DELETE trailing phrase → `the ravens lift`

- id: fault-002
  type: fault
  what: "line 2 — `taylor-hebert-westeros holds the feet on the flagstones`"
  why: `on the flagstones` is a prepositional place-specifier appended to the object. Schema: no prepositional padding.
  criteria: line must terminate at the named object without a location phrase.
  recommended-action: DELETE trailing phrase → `taylor-hebert-westeros holds the feet`

- id: fault-003
  type: fault
  what: "line 3 — `the cart crests the road from the north`"
  why: `from the north` is a directional prepositional phrase. No prepositional padding permitted.
  criteria: line must terminate at the object; directional context belongs in loc-state citation.
  recommended-action: DELETE trailing phrase → `the cart crests the road`

- id: fault-004
  type: fault
  what: "line 4 — `mira-stonefield moves to the yard`"
  why: `to the yard` is a destination prepositional phrase. Schema: place belongs in loc-state citations, not in the proto-line body.
  criteria: destination must be removed from the proto-line; location-state facet carries the placement.
  recommended-action: DELETE destination phrase → `mira-stonefield moves` OR RECAST-AS-HOLD with a destination-neutral verb

- id: fault-005
  type: fault
  what: "line 5 — `edric-cray moves to the gate post`"
  why: `to the gate post` is a destination prepositional phrase. Same rule as fault-004.
  criteria: destination removed; location context in loc-state citation.
  recommended-action: DELETE destination phrase → `edric-cray moves`

- id: fault-006
  type: fault
  what: "line 6 — `the other wards move into the yard`"
  why: Two violations. (1) `other` is an adjective modifier on the subject `wards`. (2) `into the yard` is a destination prepositional phrase.
  criteria: subject must be an unmodified named entity or `the <noun>`; destination phrase must be removed.
  recommended-action: RECAST subject to `the wards` and DELETE destination phrase → `the wards move`

- id: fault-007
  type: fault
  what: "line 8 — `the cart stops at the sept gate`"
  why: `at the sept gate` is a location prepositional phrase. Schema: place belongs in citations.
  criteria: location phrase removed; loc-state citation carries the placement.
  recommended-action: DELETE trailing phrase → `the cart stops`

- id: fault-008
  type: fault
  what: "line 9 — `census-officer steps through the sept gate`"
  why: `through the sept gate` is a place-specifying prepositional phrase. Schema: no prepositional padding; place goes in citations.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `census-officer steps`

- id: fault-009
  type: fault
  what: "line 10 — `clerk steps through the sept gate`"
  why: `through the sept gate` is a place-specifying prepositional phrase. Same rule as fault-008.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `clerk steps`

- id: fault-010
  type: fault
  what: "line 14 — `the wards assemble in the yard`"
  why: `in the yard` is a location prepositional phrase. Schema: place belongs in citations.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `the wards assemble`

- id: fault-011
  type: fault
  what: "line 15 — `taylor-hebert-westeros moves to stand with the assembled wards`"
  why: Multiple violations. (1) `to stand with the assembled wards` is a compound purpose-clause prepositional phrase, not a clean object. (2) `assembled` is an adjective on `wards`. Schema: no prepositional padding, no modifiers.
  criteria: line must reduce to a single SVO without purpose-clause or adjectival modifier.
  recommended-action: DELETE purpose clause → `taylor-hebert-westeros moves` (destination loc-state carries placement)

- id: fault-012
  type: fault
  what: "line 19 — `census-officer works through the ward line`"
  why: `through the ward line` is a prepositional phrase functioning as directional padding. The SVO spine does not permit path-specifiers.
  criteria: line must reduce to a clean SVO or be SPLIT/RECAST to a more specific physical act.
  recommended-action: RECAST to a more specific physical verb without the path-phrase, e.g. `census-officer advances`; or DELETE if covered by adjacent lines.

- id: fault-013
  type: fault
  what: "line 20 — `clerk enters each name into the ledger`"
  why: `into the ledger` is a destination prepositional phrase. Schema: no prepositional padding.
  criteria: destination phrase removed; ledger placement context in loc-state or object citation.
  recommended-action: DELETE trailing phrase → `clerk enters each name`

- id: fault-014
  type: fault
  what: "line 25 — `the sept doors hold closed`"
  why: `closed` is an adjective complement describing a state. This is a state assertion (`the sept doors are closed`) expressed through the hold-verb. Adjective present in the proto-line violates the no-modifiers rule.
  criteria: line must not contain an adjectival state complement; if the non-action is load-bearing, the physical observable event should be expressed as a positive hold or deleted (state belongs in loc-state facet).
  recommended-action: RECAST-AS-HOLD without the adjective → `the sept doors hold` OR DELETE (place in loc-state citation)

- id: fault-015
  type: fault
  what: "line 26 — `the yard holds the silence`"
  why: `the silence` is an abstraction, not a named physical entity. The yard cannot physically hold silence in any manner an observer would see. This is an ambient-state or interiority expression (atmosphere, tension) dressed as a physical action. FAULT-FORM-INTERIORITY.
  criteria: line must be replaced by a physically observable action, or deleted and its atmospheric content placed in a tensometer or narrator-interest facet citing adjacent proto-lines.
  recommended-action: DELETE; route atmospheric content to tensometer/narrator facet

- id: fault-016
  type: fault
  what: "line 31 — `census-officer returns the letter to taylor-hebert-westeros`"
  why: `to taylor-hebert-westeros` is a recipient prepositional phrase appended to the ditransitive verb. Schema: no prepositional padding; the indirect-object `to` phrase must be removed or the line split.
  criteria: line must express the physical act without the `to` recipient phrase, or be SPLIT into two beats.
  recommended-action: SPLIT-INTO-2 → `census-officer returns the letter` / `taylor-hebert-westeros takes the letter` OR DELETE trailing phrase

- id: fault-017
  type: fault
  what: "line 33 — `taylor-hebert-westeros turns toward mira-stonefield`"
  why: `toward mira-stonefield` is a directional prepositional phrase. Schema: no prepositional padding; direction/place belongs in citations.
  criteria: directional phrase removed.
  recommended-action: DELETE trailing phrase → `taylor-hebert-westeros turns`

- id: fault-018
  type: fault
  what: "line 35 — `mira-stonefield holds the eyes on the yard stones`"
  why: `on the yard stones` is a location prepositional phrase appended as padding after the object. Schema: no prepositional padding.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `mira-stonefield holds the eyes`

- id: fault-019
  type: fault
  what: "line 36 — `taylor-hebert-westeros turns toward edric-cray`"
  why: `toward edric-cray` is a directional prepositional phrase. Same rule as fault-017.
  criteria: directional phrase removed.
  recommended-action: DELETE trailing phrase → `taylor-hebert-westeros turns`

- id: fault-020
  type: fault
  what: "line 38 — `edric-cray turns toward the sept door`"
  why: `toward the sept door` is a directional prepositional phrase. Same rule as fault-017.
  criteria: directional phrase removed.
  recommended-action: DELETE trailing phrase → `edric-cray turns`

- id: fault-021
  type: fault
  what: "line 39 — `edric-cray steps through the sept door`"
  why: `through the sept door` is a place-specifying prepositional phrase. Same rule as fault-008.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `edric-cray steps`

- id: fault-022
  type: fault
  what: "line 41 — `the yard holds the silence`"
  why: Duplicate of fault-015 (line 26). `the silence` is an abstraction; not a physically observable act. FAULT-FORM-INTERIORITY.
  criteria: same as fault-015 — delete and route atmospheric content to tensometer/narrator facet.
  recommended-action: DELETE

- id: fault-023
  type: fault
  what: "line 45 — `clerk enters taylor-hebert-westeros into the ledger`"
  why: `into the ledger` is a destination prepositional phrase. Schema: no prepositional padding.
  criteria: destination phrase removed.
  recommended-action: DELETE trailing phrase → `clerk enters taylor-hebert-westeros`

- id: fault-024
  type: fault
  what: "line 46 — `clerk marks the entry with a double stroke`"
  why: `with a double stroke` is an instrumental prepositional phrase (manner/method modifier). Schema: no prepositional padding; no adverbial modifiers.
  criteria: instrumental phrase removed; the method detail belongs in a downstream facet if load-bearing.
  recommended-action: DELETE trailing phrase → `clerk marks the entry`

- id: fault-025
  type: fault
  what: "line 50 — `census-officer steps through the sept gate`"
  why: `through the sept gate` is a place-specifying prepositional phrase. Same rule as fault-008.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `census-officer steps`

- id: fault-026
  type: fault
  what: "line 51 — `clerk steps through the sept gate`"
  why: `through the sept gate` is a place-specifying prepositional phrase. Same rule as fault-008.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `clerk steps`

- id: fault-027
  type: fault
  what: "line 53 — `the cart moves off down the road`"
  why: `off down the road` is a compound directional prepositional phrase. Schema: no prepositional padding; direction/place belongs in citations.
  criteria: directional phrase removed.
  recommended-action: DELETE trailing phrase → `the cart moves`

- id: fault-028
  type: fault
  what: "line 56 — `taylor-hebert-westeros holds the feet on the flagstones`"
  why: `on the flagstones` is a location prepositional phrase appended after the object. Same rule as fault-002.
  criteria: location phrase removed.
  recommended-action: DELETE trailing phrase → `taylor-hebert-westeros holds the feet`

- id: fault-029
  type: fault
  what: "line 57 — `the yard holds empty`"
  why: `empty` is an adjective complement describing a state. Same fault class as fault-014 (line 25). State assertion via hold-verb with adjectival complement violates the no-modifiers rule.
  criteria: adjectival complement removed; if the emptiness of the yard is narratively load-bearing, place it in a loc-state facet citing this proto-line position.
  recommended-action: DELETE adjective → `the yard holds` OR DELETE line entirely (route to loc-state facet)

---

## Constraint check findings

No FAULT-CONSTRAINT findings. All lines are consistent with:
- cond-impressment-census-120ac: census procedure, letter-production as compliance move, customary handling present.
- cond-westerosi-customary-authority: social physics and deference pattern plausible in the sequence.
- cond-no-parahuman-infrastructure: no parahuman act implied in any line.
- cond-reincarnation-mechanics: no return-path, no memory-degradation, no physical-capacity violation implied.
- Series laws: no law violated; Taylor is a ward, baseborn, no title asserted.
- Series lore: Harrenhal, 120 AC, impressment-census context all honored.

---

## Physical check findings

No FAULT-PHYSICAL findings.
- All actors named (taylor-hebert-westeros, census-officer, clerk, mira-stonefield, edric-cray) are in the active cast roster.
- No prop is named that contradicts the location card's fixed-prop list or would require an absent actor's inventory. The letter (line 27) is Taylor's ward documentation, consistent with cond-impressment-census-120ac's compliance options; confirmed as actor-carried, not a location-fixed prop.
- The sept gate, sept door, and yard are all within loc-harrenhal-sept-environs. No exit referenced is invalid.

---

## Termination status

FAIL. 29 faults present. Route to fixer. Re-run pass 2 on modified file after fixer commits. Dominant fault class is FAULT-FORM-MODIFIER (27/29 faults), uniformly caused by prepositional phrases left attached to proto-lines. All are mechanical strip repairs; none require structural changes to beat sequence.
