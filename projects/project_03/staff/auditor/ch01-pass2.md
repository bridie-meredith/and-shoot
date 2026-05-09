# Audit Report — chapter-01.md Pass 2
schema: audit-report
gate: pass-2-constraint
target: design/shoot-v2/season-chapters-run/chapter-01.md
date: 2026-05-07

## Summary
total non-blank: 121
CORRECT: 74
faults:
  FAULT-FORM-MODIFIER: 27
  FAULT-FORM-PERCEPTION: 9
  FAULT-FORM-NON-ACTION-VERB: 6
  FAULT-FORM-INTERIORITY: 3
  FAULT-FORM-COPULA: 1
  FAULT-FORM-dialogue-beat-invalid-listener: 1
  FAULT-PHYSICAL-ACTOR-ABSENT: 1 (structural; covers all oc-castellan-harrenhal's officer subject lines)
file-level: FAIL
strict accept rate: 61.2%

---

## Header

- `narrator: taylor-hebert-westeros` — slug present in series cast roster. PASS.
- `goal:` — present and non-empty. PASS.

---

## Findings

### FAULT-FORM-MODIFIER

**fault-001**
- id: fault-001
- type: fault
- what: Line 3 — `septon-dying-protector breathes in the cottage below`
- why: "in the cottage below" is prepositional + adjectival padding. Schema: place goes in location-state citations, not in the proto-line.
- criteria: Remove "in the cottage below". Recast: `septon-dying-protector breathes`
- recommended: RECAST-PHYSICAL

**fault-002**
- id: fault-002
- type: fault
- what: Line 6 — `the ravens call in the bell tower`
- why: "in the bell tower" is prepositional padding. Place is a location-state citation concern.
- criteria: Remove "in the bell tower". Recast: `the ravens call`
- recommended: RECAST-PHYSICAL

**fault-003**
- id: fault-003
- type: fault
- what: Line 13 — `the sept candles gutter low`
- why: "low" is an adverb modifier on the verb.
- criteria: Remove "low". Recast: `the sept candles gutter`
- recommended: RECAST-PHYSICAL

**fault-004**
- id: fault-004
- type: fault
- what: Line 14 — `taylor-hebert-westeros lights a candle at the altar`
- why: "at the altar" is prepositional padding. Place is a location-state citation.
- criteria: Remove "at the altar". Recast: `taylor-hebert-westeros lights a candle`
- recommended: RECAST-PHYSICAL

**fault-005**
- id: fault-005
- type: fault
- what: Line 15 — `taylor-hebert-westeros opens a book at the altar table`
- why: "at the altar table" is prepositional padding.
- criteria: Remove "at the altar table". Recast: `taylor-hebert-westeros opens a book`
- recommended: RECAST-PHYSICAL

**fault-006**
- id: fault-006
- type: fault
- what: Line 18 — `a village woman knocks at the cottage door`
- why: "at the cottage door" is prepositional padding.
- criteria: Remove "at the cottage door". Recast: `a village woman knocks`; or recast object as `the cottage door` making "knocks" transitive on the door: `a village woman knocks the cottage door` — if that is the physical act. Simplest clean form: `a village woman knocks at the door` retains directional object but schema strictness requires full removal; fixer judges.
- recommended: RECAST-PHYSICAL

**fault-007**
- id: fault-007
- type: fault
- what: Line 24 — `septon-dying-protector stirs on the bed`
- why: "on the bed" is prepositional padding.
- criteria: Remove "on the bed". Recast: `septon-dying-protector stirs`
- recommended: RECAST-PHYSICAL

**fault-008**
- id: fault-008
- type: fault
- what: Line 25 — `the village woman sets the broth pot on the table`
- why: "on the table" is a place indicator. Schema rule: place goes in citations to location-state, not in the proto-line.
- criteria: Remove "on the table". Recast: `the village woman sets the broth pot`
- recommended: RECAST-PHYSICAL

**fault-009**
- id: fault-009
- type: fault
- what: Line 31 — `the ravens flush from the bell tower`
- why: "from the bell tower" is prepositional padding.
- criteria: Remove "from the bell tower". Recast: `the ravens flush`
- recommended: RECAST-PHYSICAL

**fault-010**
- id: fault-010
- type: fault
- what: Line 34 — `three riders crest the road from the north`
- why: "from the north" is prepositional directional padding.
- criteria: Remove "from the north". Recast: `three riders crest the road`
- recommended: RECAST-PHYSICAL

**fault-011**
- id: fault-011
- type: fault
- what: Line 44 — `the riders stop at the sept yard gate`
- why: "at the sept yard gate" is prepositional padding.
- criteria: Remove "at the sept yard gate". Recast: `the riders stop`; or make the gate the direct object: `the riders stop at the gate` — fixer judges minimum change. Cleanest: `the riders stop`
- recommended: RECAST-PHYSICAL

**fault-012**
- id: fault-012
- type: fault
- what: Line 53 — `taylor-hebert-westeros steps back`
- why: "back" is an adverb modifying direction of the step. No named destination object.
- criteria: Recast to named destination: `taylor-hebert-westeros steps away` is still adverbial; best form names a location: `taylor-hebert-westeros steps to the yard edge` or `taylor-hebert-westeros retreats` — fixer judges minimum change.
- recommended: RECAST-PHYSICAL

**fault-013**
- id: fault-013
- type: fault
- what: Line 59 — `oc-castellan-harrenhal's officer knocks at the cottage door`
- why: "at the cottage door" is prepositional padding (same as fault-006 pattern).
- criteria: Remove "at the cottage door". Recast: `oc-castellan-harrenhal's officer knocks`
- recommended: RECAST-PHYSICAL

**fault-014**
- id: fault-014
- type: fault
- what: Line 68 — `oc-castellan-harrenhal's officer makes a notation on the scroll`
- why: "on the scroll" is prepositional padding. Place/surface goes to location-state citations.
- criteria: Remove "on the scroll". Recast: `oc-castellan-harrenhal's officer makes a notation`
- recommended: RECAST-PHYSICAL

**fault-015**
- id: fault-015
- type: fault
- what: Line 72 — `septon-dying-protector falls back`
- why: "back" is an adverb.
- criteria: Recast to named surface: `septon-dying-protector falls to the bed` — fixer notes "to the bed" would itself be a modifier; cleanest: `septon-dying-protector falls`
- recommended: RECAST-PHYSICAL

**fault-016**
- id: fault-016
- type: fault
- what: Line 81 — `oc-castellan-harrenhal's officer produces a writing quill`
- why: "writing" is an adjective modifier on the noun.
- criteria: Remove "writing". Recast: `oc-castellan-harrenhal's officer produces a quill`
- recommended: RECAST-PHYSICAL

**fault-017**
- id: fault-017
- type: fault
- what: Line 89 — `the quill drops to the floor`
- why: "to the floor" is a prepositional place indicator. Schema: place goes in citations.
- criteria: Remove "to the floor". Recast: `the quill drops`
- recommended: RECAST-PHYSICAL

**fault-018**
- id: fault-018
- type: fault
- what: Line 92 — `oc-castellan-harrenhal's officer marks the scroll again`
- why: "again" is an adverb.
- criteria: Remove "again". Recast: `oc-castellan-harrenhal's officer marks the scroll`
- recommended: RECAST-PHYSICAL

**fault-019**
- id: fault-019
- type: fault
- what: Line 102 — `a man-at-arms produces a second scroll`
- why: "second" is an adjective modifier on "scroll".
- criteria: Remove "second". Recast: `a man-at-arms produces a scroll` — if scroll identity is load-bearing, the distinction belongs in a location-state or state-update facet, not the proto-line.
- recommended: RECAST-PHYSICAL

**fault-020**
- id: fault-020
- type: fault
- what: Line 103 — `oc-castellan-harrenhal's officer makes a notation on the second scroll`
- why: "on the second scroll" is prepositional padding; "second" is adjective modifier.
- criteria: Remove "on the second scroll". Recast: `oc-castellan-harrenhal's officer makes a notation`
- recommended: RECAST-PHYSICAL

**fault-021**
- id: fault-021
- type: fault
- what: Line 107 — `taylor-hebert-westeros holds the feet in the yard`
- why: "holds the feet" is a licensed holds-use (body-part + stillness-against-pressure). "in the yard" is appended prepositional padding that corrupts an otherwise legal line.
- criteria: Remove "in the yard". Recast: `taylor-hebert-westeros holds the feet`
- recommended: RECAST-PHYSICAL

**fault-022**
- id: fault-022
- type: fault
- what: Line 112 — `the riders turn north on the Harrenhal road`
- why: "north" is an adverb; "on the Harrenhal road" is prepositional padding.
- criteria: Remove both modifiers. Recast: `the riders turn` — or if direction is load-bearing, recast as motion toward destination: `the riders turn toward Harrenhal`; "toward Harrenhal" is still a modifier — fixer judges. Cleanest: `the riders turn`
- recommended: RECAST-PHYSICAL

**fault-023**
- id: fault-023
- type: fault
- what: Line 122 — `the ravens resettle in the bell tower`
- why: "in the bell tower" is prepositional padding.
- criteria: Remove "in the bell tower". Recast: `the ravens resettle`
- recommended: RECAST-PHYSICAL

**fault-024**
- id: fault-024
- type: fault
- what: Line 123 — `taylor-hebert-westeros turns from the window`
- why: "from the window" is prepositional directional padding. Place goes in location-state citations.
- criteria: Remove "from the window". Recast: `taylor-hebert-westeros turns`
- recommended: RECAST-PHYSICAL

**fault-025**
- id: fault-025
- type: fault
- what: Line 124 — `taylor-hebert-westeros takes the septon's writing materials`
- why: "writing" is an adjective modifier embedded in the object phrase.
- criteria: Remove "writing". Recast: `taylor-hebert-westeros takes the septon's materials`
- recommended: RECAST-PHYSICAL

**fault-026**
- id: fault-026
- type: fault
- what: Line 126 — `taylor-hebert-westeros sets the book down`
- why: "down" is an adverb.
- criteria: Remove "down". Recast: `taylor-hebert-westeros sets the book` — fixer note: "sets" without destination is still valid (intransitive landing); or substitute verb: `taylor-hebert-westeros places the book`
- recommended: RECAST-PHYSICAL

**fault-027**
- id: fault-027
- type: fault
- what: Line 130 — `taylor-hebert-westeros kneels at the altar`
- why: "at the altar" is prepositional padding.
- criteria: Remove "at the altar". Recast: `taylor-hebert-westeros kneels`
- recommended: RECAST-PHYSICAL

---

### FAULT-FORM-PERCEPTION

**fault-028**
- id: fault-028
- type: fault
- what: Line 8 — `taylor-hebert-westeros scans the Harrenhal road`
- why: "scans" is a POV-leak perception verb (same class as "read," "tracked," "noted" — per svo-split-notes pain-points and pass 2 brief "other POV-leak verb"). The observable act is turning/looking toward; the scanning-and-reading is interior.
- criteria: DELETE this proto-line and route perception content to narrator/feel facet citing the physical motion proto-line; or recast as physical orientation: `taylor-hebert-westeros looks toward the Harrenhal road` — fixer note: "looks toward" may itself edge into perception; safest is DELETE + facet.
- recommended: DELETE

**fault-029**
- id: fault-029
- type: fault
- what: Line 16 — `taylor-hebert-westeros reads the page`
- why: "reads" is explicitly listed as a FAULT-FORM-PERCEPTION verb in the pass 2 brief.
- criteria: DELETE. Reading comprehension is interior/perception; the physical act is `taylor-hebert-westeros scans the page` — but "scans" is itself a perception verb. The act of moving eyes across a page is not a clean physical SVO; route to narrator/feel facet citing line 15 (opens a book).
- recommended: DELETE

**fault-030**
- id: fault-030
- type: fault
- what: Line 28 — `the village woman glances toward the Harrenhal road`
- why: "glances" is a perception-class verb — it describes a brief look, which is a perceptual act. The physical act for an observer is "the village woman turns toward the Harrenhal road" or similar.
- criteria: Recast as physical orientation: `the village woman turns toward the Harrenhal road` — note "toward the Harrenhal road" is then a modifier fault; cleanest: `the village woman turns`
- recommended: RECAST-PHYSICAL

**fault-031**
- id: fault-031
- type: fault
- what: Line 33 — `taylor-hebert-westeros scans the Harrenhal road`
- why: Same as fault-028. Repeat instance.
- criteria: DELETE + facet (same as fault-028).
- recommended: DELETE

**fault-032**
- id: fault-032
- type: fault
- what: Line 51 — `oc-castellan-harrenhal's officer looks at taylor-hebert-westeros`
- why: "looks at" is a perception verb. An observer sees the officer turn or orient; the looking-and-seeing is interior to the officer.
- criteria: Recast as physical orientation: `oc-castellan-harrenhal's officer turns toward taylor-hebert-westeros` — but line 76 already covers a similar turn. Fixer may DELETE if beat is redundant or RECAST-PHYSICAL.
- recommended: RECAST-PHYSICAL

**fault-033**
- id: fault-033
- type: fault
- what: Line 57 — `oc-castellan-harrenhal's officer scans the outbuildings`
- why: "scans" is a FAULT-FORM-PERCEPTION verb.
- criteria: DELETE + facet; or recast as physical orientation: `oc-castellan-harrenhal's officer turns toward the outbuildings`
- recommended: DELETE

**fault-034**
- id: fault-034
- type: fault
- what: Line 62 — `oc-castellan-harrenhal's officer sees septon-dying-protector on the bed`
- why: "sees" is an explicit perception verb. Also "on the bed" is prepositional modifier. Double fault; primary is perception.
- criteria: DELETE perception proto-line; the physical fact (septon is on the bed) belongs in a location-state or state-update facet. Or recast as physical event if there is a discoverable action: e.g., the officer steps toward the bed — but that beat may be covered by line 61 (enters cottage). Recommend DELETE.
- recommended: DELETE

**fault-035**
- id: fault-035
- type: fault
- what: Line 78 — `taylor-hebert-westeros meets the officer's eyes`
- why: "meets the officer's eyes" is an idiomatic perception/social act. The physical observable act is orientation of the face or raising of the head; the eye-contact content is interior perception. Analogous to the POV-leak class.
- criteria: Recast as physical body-orientation: `taylor-hebert-westeros raises her eyes` or `taylor-hebert-westeros lifts her chin` — fixer judges which physical act is the accurate rendering.
- recommended: RECAST-PHYSICAL

**fault-036**
- id: fault-036
- type: fault
- what: Line 120 — `taylor-hebert-westeros scans the Harrenhal road`
- why: "scans" — same as fault-028 and fault-031. Third instance.
- criteria: DELETE + facet.
- recommended: DELETE

---

### FAULT-FORM-NON-ACTION-VERB

**fault-037**
- id: fault-037
- type: fault
- what: Line 35 — `two men-at-arms flank a mounted official`
- why: "flank" describes a static spatial arrangement (positional state), not a discrete observable act of moving into position. The brief lists "stative position-naming (`lies`, `sits`, `stands` describing position not posture-act)" — "flank" is in the same class. "Mounted" is also an adjective modifier on "official".
- criteria: Recast as the discrete positioning act: `two men-at-arms take position beside the official` — but "beside" is then a modifier. Cleaner: split the arrival into a motion beat; or SPLIT-INTO-N to cover the act of riding to flanking positions. Alternatively: DELETE if the flanking is rendered by line 46 (men-at-arms dismount) in context.
- recommended: RECAST-PHYSICAL

**fault-038**
- id: fault-038
- type: fault
- what: Line 36 — `a packaged scroll protrudes from the official's saddlebag`
- why: "protrudes" is a stative position verb (the scroll is in a state of protruding). "packaged" is an adjective modifier. This line describes an environment-observation state, not a discrete physical act. Per svo-split-notes #10: persistence-of-environment is a loc-state assertion, not a proto-line, unless a character interacts with it.
- criteria: DELETE — route to location-state facet noting the census scroll is visible in the saddlebag; or recast when the officer produces it (line 47 already covers the producing act). This line is redundant with line 47.
- recommended: DELETE

**fault-039**
- id: fault-039
- type: fault
- what: Line 56 — `the men-at-arms flank the yard entrance`
- why: Same as fault-037. "flank" = stative position. The act of moving to flanking positions is what belongs as a proto-line.
- criteria: Recast as discrete positioning act or DELETE if redundant with entry sequence.
- recommended: RECAST-PHYSICAL

**fault-040**
- id: fault-040
- type: fault
- what: Line 88 — `septon-dying-protector's hand fails`
- why: "fails" names a stative result, not a discrete physical act. Additionally, "septon-dying-protector's hand" as subject is a body-part-as-actor construction; per svo-split-notes #11, the actor should be restored as subject. The physical event is the hand ceasing to produce the required motion.
- criteria: Recast with actor as subject and physical act: `septon-dying-protector drops the quill` — but line 89 covers the quill dropping. Fixer may recast as: `septon-dying-protector's hand stops` is still stative; cleanest: `septon-dying-protector releases the quill` and DELETE line 89 (since quill-drop is downstream of release). Fixer judges.
- recommended: RECAST-PHYSICAL

**fault-041**
- id: fault-041
- type: fault
- what: Line 121 — `the riders diminish on the northern road`
- why: "diminish" is a stative/gradual-change verb describing a perceptual state of growing smaller in the distance. Not a discrete physical act observable as a single beat. "on the northern road" is also prepositional modifier; "northern" is adjective.
- criteria: DELETE — this is a perception/narrator-interest observation that belongs in a facet, not a proto-line. Or recast as a location-state entry. The physical event is the riders continuing north (covered by line 112–113).
- recommended: DELETE

**fault-042**
- id: fault-042
- type: fault
- what: Line 131 — `taylor-hebert-westeros holds the position`
- why: "holds" with abstract object "the position" is explicitly an unlicensed holds use per the pass 2 brief: "hold-with-abstract-object like `holds the silence`." "The position" is an abstract state, not a body part. Licensed holds require a body-part-as-object for stillness-against-pressure.
- criteria: Recast to name the specific body part being held: `taylor-hebert-westeros holds the knees` or `taylor-hebert-westeros holds the spine` — fixer determines which body part is the accurate rendering of kneeling-at-altar stillness.
- recommended: RECAST-PHYSICAL

---

### FAULT-FORM-INTERIORITY

**fault-043**
- id: fault-043
- type: fault
- what: Line 71 — `septon-dying-protector attempts to rise`
- why: "attempts" is a modal intent/effort verb — it names a volitional state (the intent to perform an act) rather than a discrete physical act observable from outside. The observable act is the beginning of a rise: `septon-dying-protector rises` (if even partial); the attempt-and-failure structure is two beats or expressed through the subsequent fall.
- criteria: SPLIT-INTO-N: (a) `septon-dying-protector rises` and (b) `septon-dying-protector falls` — or collapse into line 72's fall by deleting line 71 and recasting line 72 to carry the failed-rise.
- recommended: SPLIT-INTO-N

**fault-044**
- id: fault-044
- type: fault
- what: Line 79 — `taylor-hebert-westeros drops her gaze`
- why: "her gaze" is a perception-construct object (the gaze is the perceptual act, not a physical object). This names an interior/social act using a perception-noun as the object. Compare with the licensed `taylor-hebert-westeros lowers her eyes` where eyes are a physical body part.
- criteria: Recast with body-part object: `taylor-hebert-westeros lowers her eyes`
- recommended: RECAST-PHYSICAL

**fault-045**
- id: fault-045
- type: fault
- what: Line 87 — `septon-dying-protector attempts a signature`
- why: Same class as fault-043. "attempts" = intent/effort. The observable act is the physical motion: `septon-dying-protector marks the scroll` (partial, incomplete) — differentiated from the officer's successful marking by what line 88 carries.
- criteria: Recast: `septon-dying-protector marks the scroll` — the failure state belongs in fault-040's resolution for line 88.
- recommended: RECAST-PHYSICAL

---

### FAULT-FORM-COPULA

**fault-046**
- id: fault-046
- type: fault
- what: Line 9 — `the road shows empty`
- why: "shows empty" is functionally equivalent to "the road is empty" — a stative copula construction dressed with "shows." The verb's primary semantic is being (empty state), not doing. Per FAULT-FORM-COPULA: copula-equivalent stative constructions.
- criteria: DELETE — the road-empty observation is a perception act belonging in a narrator/feel facet or location-state facet. There is no physical act to preserve as a proto-line; the road's emptiness is the absence of action.
- recommended: DELETE

---

### FAULT-FORM-dialogue-beat-invalid-listener

**fault-047**
- id: fault-047
- type: fault
- what: Line 48 — `oc-castellan-harrenhal's officer speaks to the yard`
- why: Per schema, the dialogue beat shape is `<speaker> speaks to <listener-slug-or-group>`. "The yard" is a location, not a named entity or group. A location cannot be a valid listener in the proto-line format. The intended meaning — the officer addresses the open yard / anyone present — requires a valid listener slug or collective group designation.
- criteria: Recast listener to a valid entity or group: `oc-castellan-harrenhal's officer speaks to the sept grounds` is still a location. Correct form: the officer speaks to whoever is present — e.g., `oc-castellan-harrenhal's officer speaks to the household` or `oc-castellan-harrenhal's officer calls out` (if no addressee can be named, make it a non-dialogue physical act). Fixer determines accurate rendering.
- recommended: RECAST-PHYSICAL

---

### FAULT-PHYSICAL-ACTOR-ABSENT

**fault-048**
- id: fault-048
- type: fault
- what: Lines 45, 47, 48, 51, 52, 55, 57, 58, 59, 61, 62, 63, 65, 66, 68, 70, 74, 76, 77, 82, 84, 85, 90, 91, 92, 93, 95, 98, 99, 101, 103, 104, 106, 109, 111 — subject slug `oc-castellan-harrenhal's officer`
- why: The slug `oc-castellan-harrenhal's officer` does not appear in the series cast_roster (`active-project/staff/showrunner/memory.md`). The series roster contains `oc-castellan-harrenhal` (the castellan) but not a derivative "officer" slug. The episode cast (from dispatch context) lists `census-officer` as the correct slug for this character. The file uses an unregistered possessive-derivative slug throughout, which will break facet cross-referencing, dialogue-file authoring, and state-update routing for the entire chapter.
- criteria: RENAME-SLUG — replace all instances of `oc-castellan-harrenhal's officer` with the registered episode cast slug `census-officer` throughout the file.
- recommended: RENAME-SLUG
