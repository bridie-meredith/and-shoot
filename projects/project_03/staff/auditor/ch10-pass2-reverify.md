# Audit Report — Chapter 10 Pass 2 Re-verify
# schema: schemas/audit-report.schema.md

run: ch10-pass2-reverify
date: 2026-05-07
target: active-project/theater/proto-lines/chapter-10.md
auditor: fork (fresh context)
pass: 2 — constraint audit (post-fixer)
scope: all 50 numbered lines

---

## Summary

total-lines: 50
correct: 42
faults: 7
flags: 1
escalate: 0

fault-breakdown:
  FAULT-FORM-MODIFIER: 4  (lines 4, 10, 41, 42)
  FAULT-FORM-NON-ACTION-VERB: 1  (line 26)
  FAULT-FORM-INTERIORITY: 1  (line 48, primary)
  FAULT-FORM-MODIFIER (secondary on line 48): counted under line 48 entry
  FAULT-FORM-MODIFIER total: 5 (lines 4, 10, 41, 42, 48)

corrected-fault-breakdown (per-line unique):
  FAULT-FORM-MODIFIER: lines 4, 10, 41, 42 — 4 faults
  FAULT-FORM-NON-ACTION-VERB: line 26 — 1 fault
  FAULT-FORM-INTERIORITY + FAULT-FORM-MODIFIER (compound): line 48 — 1 fault entry (2 classes)

CONTINUITY-OK: NO — 6 fault lines present.

header-check: PASS
  narrator: taylor-hebert-westeros — slug in cast roster.
  goal: present and non-empty.

constraint-checks: PASS (no FAULT-CONSTRAINT-* findings)
physical-actor-checks: PASS (all five chapter-plan actors present; no extraneous actors)

non-actionable gap (not a fault):
  The scene location "the hall" has no corresponding warehouse location card
  (loc-harrenhal-hall or equivalent). FAULT-PHYSICAL-EXIT-INVALID cannot be
  adjudicated for lines 1, 16, 30, 35, 44, 47 without a card defining exits and
  fixed props. Physical-prop-absent cannot be adjudicated for the census file,
  ward-record scroll, stylus, seal, and wax without actor inventory records at
  chapter-open. These are pipeline gaps, not line-level faults — route to
  orchestrator for location card authoring before pass 5.

watches-verb check (per dispatch brief):
  "watches" does not appear anywhere in the file. Prior transient fault cleared.

---

## Findings

---

### fault-001
id: fault-001
type: fault
line-id: 4
line: ser-harwick-plumm sets the census file on the table
fault-class: FAULT-FORM-MODIFIER
what: Prepositional phrase "on the table" appended to the SVO frame.
why: Time and place belong in location-state facet citations, not in the proto-line body. Destination padding in the spine corrupts downstream shape and state-update decisions that cite this line.
criteria: Remove "on the table." Recast as: `ser-harwick-plumm sets the census file`.
recommended-action: RECAST-PHYSICAL

---

### fault-002
id: fault-002
type: fault
line-id: 10
line: oc-castellan-harrenhal sets the census file down
fault-class: FAULT-FORM-MODIFIER
what: Directional adverb "down" appended to the verb.
why: Adverbs are banned. The directional information is implicit in "sets" when the prior state is "lifts" (line 7). "Down" is padding that leaks spatial assertion into the spine.
criteria: Remove "down." Recast as: `oc-castellan-harrenhal sets the census file`.
recommended-action: RECAST-PHYSICAL

---

### fault-003
id: fault-003
type: fault
line-id: 26
line: taylor-hebert-westeros holds the chin angle
fault-class: FAULT-FORM-NON-ACTION-VERB
what: Object "chin angle" is an abstract positional descriptor, not a body part or physical object. This is the disallowed "hold-with-abstract-object" form per the pass-2 brief: "hold-with-abstract-object like `holds the ledger` when clerk has it, hold-with-location-as-object."
why: Licensed `holds` uses require either a body-part-as-object for stillness-against-pressure (e.g., `holds the feet`, `holds the eyes`) or a physical-object-resisting-pressure. "Chin angle" is a compound noun describing a postural state — it is an abstraction, not the body part itself. Allowing this form would expand the licensed exception beyond its definition and corrupt downstream facet authoring.
criteria: Recast to the licensed form using the body part directly: `taylor-hebert-westeros holds the chin`. Alternatively, split into the physical act that initiated the stillness if the intent is a hold-against-pressure event.
recommended-action: RECAST-AS-HOLD

---

### fault-004
id: fault-004
type: fault
line-id: 41
line: ser-harwick-plumm presses the seal into the wax
fault-class: FAULT-FORM-MODIFIER
what: Prepositional phrase "into the wax" appended to the SVO frame.
why: Destination / manner of the press belongs in location-state or state-update facet citations. The prepositional tail is spatial padding in the spine.
criteria: Remove "into the wax." Recast as: `ser-harwick-plumm presses the seal`. If contact with the wax is narratively required as a separate beat, it routes to a state-update facet citing this line.
recommended-action: RECAST-PHYSICAL

---

### fault-005
id: fault-005
type: fault
line-id: 42
line: ser-harwick-plumm lifts the seal off the wax
fault-class: FAULT-FORM-MODIFIER
what: Prepositional phrase "off the wax" appended to the SVO frame.
why: Source / departure direction is prepositional padding. The SVO spine records the physical act (lift); the relationship to the wax is spatial state, not action.
criteria: Remove "off the wax." Recast as: `ser-harwick-plumm lifts the seal`. The seal-impression state routes to a state-update facet.
recommended-action: RECAST-PHYSICAL

---

### fault-006
id: fault-006
type: fault
line-id: 48
line: taylor-hebert-westeros drops the gaze to the floor
fault-class: FAULT-FORM-INTERIORITY (primary); FAULT-FORM-MODIFIER (secondary)
what: (Primary) Object "the gaze" names a perceptual/attentional state, not a physical object or body part. "Drops the gaze" is an idiomatic expression for a perceptual act — lowering visual attention — not a concrete physical action. The object is internal and perceptual, placing this in the interiority category alongside thought, intent, and feeling. (Secondary) "to the floor" is prepositional padding.
why: A proto-line with a perceptual/attentional object violates the no-interiority rule. The verb "drops" applied to "the gaze" does not describe what an outside observer would see; it describes the direction of Taylor's attention. Facets (specifically feeling-flags or narrator-interest) are the correct destination for this beat.
criteria: If the physical act intended is a postural downward head movement, recast to the body part: `taylor-hebert-westeros drops the chin`. If the intent is attentional/perceptual only, delete from the spine and route to the appropriate facet.
recommended-action: RECAST-PHYSICAL or DELETE (orchestrator decides based on intent)

---

## Flag (non-fault)

---

### flag-001
id: flag-001
type: flag
line-id: 19
line: oc-castellan-harrenhal returns to the table
what: Verb "returns" carries a stative-restoration implication (going back to a prior position). It is not a banned verb and is not stative position-naming. Physical motion with destination. Not a fault.
why: Noted because the verb is weaker than directional motion verbs (`crosses`, `enters`, `exits`). Does not violate any rule; flagged for pass-3 shape awareness only.
criteria: None required. Pass-3 may prefer a stronger motion verb if the beat serves escalation.

---

## Non-fault pipeline gaps (route to orchestrator, not fixer)

gap-001:
  what: No warehouse location card for "the hall" (the chapter-10 scene location).
  why: FAULT-PHYSICAL-EXIT-INVALID and FAULT-PHYSICAL-PROP-ABSENT cannot be adjudicated for enter/exit beats (lines 1, 16, 30, 35, 44, 47) or for props (census file, ward-record scroll, stylus, seal, wax) without a card defining the hall's exits and fixed inventory.
  route: Author loc-harrenhal-administrative-hall (or equivalent) before pass 5. Pass 5 continuity audit requires a card to check actor presence-arcs and prop state against.

---

## Line-by-line verdict table

1   CORRECT
2   CORRECT
3   CORRECT
4   FAULT-FORM-MODIFIER (fault-001)
5   CORRECT
6   CORRECT
7   CORRECT
8   CORRECT
9   CORRECT
10  FAULT-FORM-MODIFIER (fault-002)
11  CORRECT
12  CORRECT
13  CORRECT
14  CORRECT
15  CORRECT
16  CORRECT
17  CORRECT
18  CORRECT
19  CORRECT (flag-001 noted)
20  CORRECT
21  CORRECT
22  CORRECT
23  CORRECT
24  CORRECT
25  CORRECT
26  FAULT-FORM-NON-ACTION-VERB (fault-003)
27  CORRECT
28  CORRECT
29  CORRECT
30  CORRECT
31  CORRECT
32  CORRECT
33  CORRECT
34  CORRECT
35  CORRECT
36  CORRECT
37  CORRECT
38  CORRECT
39  CORRECT
40  CORRECT
41  FAULT-FORM-MODIFIER (fault-004)
42  FAULT-FORM-MODIFIER (fault-005)
43  CORRECT
44  CORRECT
45  CORRECT
46  CORRECT
47  CORRECT
48  FAULT-FORM-INTERIORITY + FAULT-FORM-MODIFIER (fault-006)
49  CORRECT
50  CORRECT
