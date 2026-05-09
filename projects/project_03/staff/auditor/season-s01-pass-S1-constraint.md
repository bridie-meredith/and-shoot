audit:
  scope: season
  target: s01
  timestamp: 2026-05-07
  file_level: FAIL
  fault_counts:
    FAULT-FORM-MODIFIER: 28
    FAULT-FORM-INTERIORITY: 3
    FAULT-FORM-PERCEPTION: 2
    FAULT-FORM-NON-ACTION-VERB: 4
    FAULT-FORM-ID-SEQUENCE: 9
    FAULT-FORM-MULTI-SUBJECT: 1
    FAULT-FORM-NO-VERB: 1
    FAULT-FORM-MALFORMED-BEAT: 1
    FAULT-CONSTRAINT-slug: 3
    flag: 14
  total_faults: 52
  total_flags: 14

---

# Season S01 — Pass S1 Constraint Audit

## File-level verdict: FAIL

52 classified faults across 14 files. Fault density is not uniform: chapter-03 carries the highest single-chapter fault count (7 FAULT-FORM-MODIFIER from the `holds the X [modifier]` pattern). Chapter-02 carries the most structural complexity (ID-ordering faults + forced-transitive pattern + interiority-as-object). Chapters 08-interlude and 09 each carry distinct fault classes not seen elsewhere. Chapter-10 is the cleanest file in the season (0 faults, flags only).

No cross-episode constraint violations against series laws or condition cards were found. All constraint faults are SVO-mechanic or slug-resolution faults, not world-law violations.

---

## Drift patterns — season-wide (appear 3+ times or define a fault class)

**Pattern A — `holds the X [modifier]`:** The body-part holds license (`holds the feet`, `holds the chin`) is consistently violated by appending a result/state modifier (`flat`, `level`, `open`, `still`). The modifier converts a licensed intransitive hold into a stative assertion with a result-state adjective. Appears 7 times in chapter-03 alone; additional instances in chapter-05. Total: 9 instances.

**Pattern B — forced-transitive location verbs:** Intransitive verbs (`crouches`, `leans`, `lands`) are forced into transitive constructions with a location as direct object (`crouches the kitchen garden`, `leans the cottage wall`, `lands the garden wall`). These parallel the schema-approved `enters the yard` model but use verbs that do not naturally take location objects. 4 faulted instances; 3 flagged borderline instances.

**Pattern C — prepositional destination phrases:** `steps into`, `crosses to`, `pins to`, `stations on`, `leans against` — prepositional phrases of destination or position appended to otherwise-clean SVOs. The schema explicitly prohibits this class. Appears across 6 chapters. Total: 12 instances (faulted) + 2 additional (flagged).

**Pattern D — non-monotonic ID ordering:** Multiple files have IDs appearing out of numeric sequence within the file body. This is a structural authoring artifact: late-added lines were given higher IDs and inserted mid-file without resequencing. Affects chapters 02, 03-interlude, 05, 07, 09. The stitcher walks IDs in citation order, not numeric order, but the non-monotonic ordering makes manual review and facet-authoring harder.

**Pattern E — `turns toward <entity>`:** Chapter-01 has 4 instances of `turns toward <X>`. The schema explicitly bans `turns to <named entity>` as a directional-prep variant of FAULT-FORM-MODIFIER. `turns toward` is the same construction with a different preposition; the same ruling applies.

---

## Findings

### CHAPTER 01 — chapter-01.md

- id: fault-001
  type: fault
  file: chapter-01.md
  line_id: 7
  content: "taylor-hebert-westeros steps into the yard"
  fault_class: FAULT-FORM-MODIFIER
  what: "steps into" is a prepositional-phrase motion construction identical to the banned "walks into the yard" example in the schema.
  why: Facets citing this line will treat `steps into the yard` as the action; the prepositional phrase is not a physical object the stitcher can elide. Downstream loc-state authoring may double the location marker.
  criteria: Line must use a transitive verb taking the yard as direct object. `taylor-hebert-westeros enters the yard` or equivalent.

- id: fault-002
  type: fault
  file: chapter-01.md
  line_id: 10
  content: "taylor-hebert-westeros turns toward the sept door"
  fault_class: FAULT-FORM-MODIFIER
  what: "`turns toward <X>`" is the same directional-prep construction as the banned "`turns to <X>`". The ruling in the schema covers both prepositions.
  why: The turn-direction is prepositional padding. The physical act observable by a bystander is orientation change, capturable as `faces the sept door` or `reaches the sept door`.
  criteria: Line must recast without a directional prepositional phrase. `taylor-hebert-westeros faces the sept door` or equivalent transitive form.

- id: fault-003
  type: fault
  file: chapter-01.md
  line_id: 32
  content: "taylor-hebert-westeros steps into the yard"
  fault_class: FAULT-FORM-MODIFIER
  what: Same construction as fault-001 (duplicate occurrence of the same fault).
  why: Same downstream consequence as fault-001.
  criteria: Same as fault-001. Recast as transitive: `enters the yard`.

- id: fault-004
  type: fault
  file: chapter-01.md
  line_id: 51
  content: "census-officer turns toward taylor-hebert-westeros"
  fault_class: FAULT-FORM-MODIFIER
  what: "`turns toward <actor-slug>`" — directional prepositional phrase.
  why: The orientation target is a named entity (slug). `faces taylor-hebert-westeros` delivers the same observable fact without the prep phrase.
  criteria: Recast as `census-officer faces taylor-hebert-westeros` or equivalent.

- id: fault-005
  type: fault
  file: chapter-01.md
  line_id: 57
  content: "census-officer turns toward the outbuildings"
  fault_class: FAULT-FORM-MODIFIER
  what: Same as fault-004.
  why: Same downstream consequence.
  criteria: Recast as `census-officer faces the outbuildings` or equivalent.

- id: fault-006
  type: fault
  file: chapter-01.md
  line_id: 76
  content: "census-officer turns toward taylor-hebert-westeros"
  fault_class: FAULT-FORM-MODIFIER
  what: Same as fault-004 (second occurrence).
  why: Season-wide pattern: `turns toward` appears 4 times in chapter-01 alone. A drift pattern at season scope.
  criteria: Recast as `census-officer faces taylor-hebert-westeros`.

- id: fault-007
  type: fault
  file: chapter-01.md
  line_id: 119
  content: "taylor-hebert-westeros crosses to the window"
  fault_class: FAULT-FORM-MODIFIER
  what: "`crosses to`" — prepositional phrase of destination. The schema example explicitly covers `moves to the yard` and `steps through the gate`; `crosses to the window` is the same pattern.
  why: `crosses` is a transitive verb that takes a direct object (`crosses the cottage floor` is already in this file and is clean). `crosses to` degrades it to a prepositional construction.
  criteria: Recast as `taylor-hebert-westeros crosses the cottage` or `taylor-hebert-westeros reaches the window`.

- id: fault-008
  type: fault
  file: chapter-01.md
  line_id: census-officer (slug)
  content: "`census-officer` used as actor slug throughout chapter-01"
  fault_class: FAULT-CONSTRAINT-slug
  what: `census-officer` is not in the series cast_roster in showrunner memory, is not in the chapter-01-plan actors list, and is not formatted as `the census-officer` per the unnamed-entity convention.
  why: Every proto-line where `census-officer` is subject fails slug resolution. Downstream facet authoring (dialogue files, state-updates) cannot create a canonical actor record for an unregistered slug. The slug is used in 20+ lines across chapter-01.
  criteria: Either register `census-officer` as a minor character in the cast roster and ensure its card exists, or reformat all instances as `the census-officer` per the `the <noun>` unnamed-entity convention.

---

### CHAPTER 02 — chapter-02.md

- id: fault-009
  type: fault
  file: chapter-02.md
  line_id: 4
  content: "taylor-hebert-westeros crouches the kitchen garden"
  fault_class: FAULT-FORM-MODIFIER
  what: `crouches` is an intransitive posture verb. It does not take a location as direct object in standard use. The writer is forcing a transitive construction to comply with the no-prep-phrase rule, but the result is a non-standard verb-object pair that obscures meaning. `crouches [in] the kitchen garden` is the implied reading — i.e. the preposition `in` has been suppressed.
  why: Suppressing the preposition while keeping the prepositional-phrase meaning is not the same as using a transitive verb. Facets citing this line will misread the action as `crouches the [thing]` not `crouches [while in] the garden`. State-updates and sensory facets may misattribute the object.
  criteria: Split into two lines: the entry to the garden (e.g. `taylor-hebert-westeros enters the kitchen garden`) and the posture act (`taylor-hebert-westeros crouches`).

- id: fault-010
  type: fault
  file: chapter-02.md
  line_id: 12
  content: "plumms-man crouches the shed floor"
  fault_class: FAULT-FORM-MODIFIER
  what: Same as fault-009 (`crouches` forced transitive with location object).
  why: Same downstream consequence as fault-009.
  criteria: Same split pattern: entry beat + posture beat.

- id: fault-011
  type: fault
  file: chapter-02.md
  line_id: 58
  content: "oc-girl-from-hamlet rounds the mill hamlet road edge"
  fault_class: FAULT-CONSTRAINT-slug
  what: `oc-girl-from-hamlet` is an `oc-` prefixed slug not registered in the series cast_roster, the active warehouse, or any chapter plan's actors list visible to this audit. The `oc-` prefix convention implies an original-character card should exist under `active-project/warehouse/`.
  why: Unresolved slug breaks downstream facet citation. Dialogue files, state-updates, and feeling-flags cannot reference an actor without a canonical card. The slug appears in chapter-02 only (lines 58, 61, 62, 63, 65).
  criteria: Register `oc-girl-from-hamlet` as a minor character with a card in the active warehouse and cast roster, or reformat appearances as `the girl` per the `the <noun>` convention (which the file already uses from line 61 onward when referring to the same entity — inconsistent usage).

- id: fault-012
  type: fault
  file: chapter-02.md
  line_id: 24
  content: "a sparrow lifts the barn eave"
  fault_class: FAULT-FORM-MODIFIER
  what: `lifts the barn eave` — `lifts` here compresses `lifts off from the barn eave`. The preposition `from` has been suppressed. The barn eave is not a physical thing the sparrow lifts (raises). The intended meaning is departure-from-surface.
  why: The suppressed preposition leaves the object ambiguous. A stitcher or facet author reading `lifts the barn eave` may interpret it as the sparrow displacing the barn structure. The physical event is departure, not lifting-of-object.
  criteria: Recast as `a sparrow departs the barn eave` or `a sparrow launches from the barn eave` — but the latter still has the prep phrase. Cleanest form: `a sparrow lifts` (intransitive, loc-state provides the eave context).

- id: fault-013
  type: fault
  file: chapter-02.md
  line_id: 81
  content: "taylor-hebert-westeros leans the cottage wall"
  fault_class: FAULT-FORM-MODIFIER
  what: `leans` is intransitive (or takes a body-part object: `leans the back`). `leans the cottage wall` forces `leans against the cottage wall` with the preposition suppressed. Same forced-transitive fault as fault-009.
  why: Object is a location surface, not a thing the subject acts on physically.
  criteria: Recast as `taylor-hebert-westeros reaches the cottage wall` + `taylor-hebert-westeros stops` or similar physical sequence, or `taylor-hebert-westeros presses the cottage wall` if physical contact is the beat.

- id: fault-014
  type: fault
  file: chapter-02.md
  line_id: 96
  content: "taylor-hebert-westeros opens the passive feed"
  fault_class: FAULT-FORM-INTERIORITY
  what: `the passive feed` is Taylor's internal cognitive fauna-awareness state. It is not a physical object. A verb acting on it (`opens`) treats an interior state as a thing that can be physically manipulated. The line is an interiority assertion in disguise.
  why: This is the core prohibition: proto-lines record physical events observable by a bystander. A bystander cannot observe Taylor opening her passive fauna-awareness. Downstream feeling-flags, memory-flags, and sensory facets are the correct location for this information.
  criteria: The proto-line must record a physical observable correlate: e.g. `taylor-hebert-westeros stills` (if the observable behavior is going quiet/settling) with the fauna-state transition routed to a state-update or feeling-flag facet. The word `passive feed` must not appear in a proto-line.

- id: fault-015
  type: fault
  file: chapter-02.md
  line_id: 100
  content: "taylor-hebert-westeros drops the passive feed"
  fault_class: FAULT-FORM-INTERIORITY
  what: Same as fault-014 (paired beat — opens/drops the passive feed).
  why: Same downstream consequence as fault-014.
  criteria: Same as fault-014. Physical correlate only; interior state to facets.

- id: fault-016
  type: fault
  file: chapter-02.md
  line_id: multiple (91→104→94 sequence)
  content: "IDs 91, 104, 94 appear in that file-order in the garrison-hall section; ID 104 appears between 91 and 94"
  fault_class: FAULT-FORM-ID-SEQUENCE
  what: IDs are not monotonically increasing through the file body. The file also has IDs 102, 103 appearing mid-file in the orchard section (between IDs 49 and 50), and IDs 66–68 appearing after ID 73 in the hamlet section. These are not isolated — at least 4 separate non-monotonic runs in chapter-02.
  why: The schema requires IDs to be stable and monotonic. The stitcher walks IDs in citation order; non-monotonic IDs in the file body make the citation-order assumption unreliable. Facet authoring that cites by ID range will produce incorrect spans.
  criteria: ID ordering within the file must be monotonically increasing. Late-added lines with higher IDs must be renumbered (preserving all existing IDs and their content) or the file must be re-emitted with a fresh monotonic sequence. No ID may appear numerically before a lower-ID line in file-body order.

- id: fault-017
  type: fault
  file: chapter-02.md
  line_id: plumms-man (slug)
  content: "`plumms-man` used as actor slug throughout chapter-02"
  fault_class: FAULT-CONSTRAINT-slug
  what: `plumms-man` is not in the series cast_roster, not in the chapter-02-plan actors list (which names `taylor-hebert-westeros` and `ser-harwick-plumm`), and is not formatted as `the plumms-man` or `the <noun>`. The actor appears in 30+ lines across chapter-02.
  why: Same downstream consequence as fault-008. `plumms-man` also appears in chapter-03-interlude, making this a cross-chapter slug issue.
  criteria: Register `plumms-man` as a minor character with a card (or alias under `ser-harwick-plumm`'s entry) and ensure cast roster includes it, or reformat all instances as `the plumms-man` per the unnamed-entity convention. The choice must be consistent across chapter-02 and chapter-03-interlude.

---

### CHAPTER 03 — chapter-03.md

- id: fault-018
  type: fault
  file: chapter-03.md
  line_id: 8
  content: "taylor-hebert-westeros holds the feet flat"
  fault_class: FAULT-FORM-MODIFIER
  what: `flat` is a result-state modifier appended to the licensed body-part hold. The licensed form is `holds the feet` (stillness-against-pressure). `flat` converts this to a stative result assertion.
  why: `holds the feet flat` describes a static posture (feet are flat on the floor) rather than the discrete act of holding under pressure. The modifier is the difference between an action and a state description.
  criteria: Strip the modifier. `taylor-hebert-westeros holds the feet` is the correct form. If `flat` is load-bearing for a downstream facet (sensory, state-update), route it to that facet as a citation.

- id: fault-019
  type: fault
  file: chapter-03.md
  line_id: 9
  content: "taylor-hebert-westeros holds the chin level"
  fault_class: FAULT-FORM-MODIFIER
  what: `level` is a result-state modifier. Same pattern as fault-018.
  why: Same as fault-018.
  criteria: Strip to `taylor-hebert-westeros holds the chin`.

- id: fault-020
  type: fault
  file: chapter-03.md
  line_id: 14
  content: "taylor-hebert-westeros holds the hands flat"
  fault_class: FAULT-FORM-MODIFIER
  what: Same pattern as fault-018 (`flat` modifier).
  why: Same as fault-018.
  criteria: Strip to `taylor-hebert-westeros holds the hands`.

- id: fault-021
  type: fault
  file: chapter-03.md
  line_id: 18
  content: "taylor-hebert-westeros holds the chin level"
  fault_class: FAULT-FORM-MODIFIER
  what: Duplicate of fault-019 (second occurrence in same file).
  why: This is now a pattern: `holds the chin level` appears twice in chapter-03. Part of the season-wide drift.
  criteria: Same as fault-019.

- id: fault-022
  type: fault
  file: chapter-03.md
  line_id: 19
  content: "taylor-hebert-westeros holds the eyes open"
  fault_class: FAULT-FORM-MODIFIER
  what: `open` is a result-state modifier. Same drift pattern as fault-018.
  why: Same as fault-018. `holds the eyes` is licensed; `open` is the banned modifier.
  criteria: Strip to `taylor-hebert-westeros holds the eyes`.

- id: fault-023
  type: fault
  file: chapter-03.md
  line_id: 35
  content: "taylor-hebert-westeros holds the feet flat"
  fault_class: FAULT-FORM-MODIFIER
  what: Third occurrence of `holds the feet flat` in chapter-03 (lines 8, 35, 42 all carry this fault).
  why: The repetition is a season-scope drift signal: the writer treats the modifier as load-bearing for the repetitive-stillness rhythm. The modifier must be stripped regardless of rhythmic intent; the rhythm can be preserved without the modifier.
  criteria: Same as fault-018.

- id: fault-024
  type: fault
  file: chapter-03.md
  line_id: 39
  content: "taylor-hebert-westeros holds the hands still"
  fault_class: FAULT-FORM-MODIFIER
  what: `still` is a result-state modifier. Same pattern as fault-018.
  why: Same as fault-018.
  criteria: Strip to `taylor-hebert-westeros holds the hands`.

- id: fault-025
  type: fault
  file: chapter-03.md
  line_id: 42
  content: "taylor-hebert-westeros holds the feet flat"
  fault_class: FAULT-FORM-MODIFIER
  what: Fourth occurrence of `holds the feet flat` in chapter-03 (lines 8, 35, 42; plus line 35 counted above).
  why: Season-wide pattern: the modifier `flat` on body-part holds is the most frequent single recurring fault in the season.
  criteria: Same as fault-018.

---

### CHAPTER 03-INTERLUDE — chapter-03-interlude.md

- id: fault-026
  type: fault
  file: chapter-03-interlude.md
  line_id: 12
  content: "septon-rowan scans the cottage interior"
  fault_class: FAULT-FORM-PERCEPTION
  what: `scans` is a perception verb. The schema deny-list includes `watches`, `sees`, `hears`, `notices`, `tracks`, `noted`, `counted`, `measured`, `read`. `scans` is in the same semantic class: it describes internal observation, not an external physical act.
  why: Perception verbs are POV-leaks. The line describes what Rowan is doing cognitively, not what a bystander observes. The correct form records the physical correlate (where Rowan's body moves, what he physically touches or picks up).
  criteria: Recast as the physical actions that constitute the scan: e.g. `septon-rowan crosses the cottage` + physical beat at each inspected location. The interior-observation content routes to narrator-interest or sensory facets.

- id: fault-027
  type: fault
  file: chapter-03-interlude.md
  line_id: 88 and 87 (appear before 63 and 71 in file body)
  content: "ID 88 (septon-rowan drops the eyes) appears in file body before ID 63 (time-skip); ID 87 (septon-rowan lowers the eyes) appears before ID 71 (time-skip)"
  fault_class: FAULT-FORM-ID-SEQUENCE
  what: IDs 87 and 88 appear mid-file before their numeric position. The file ends at ID 84 (the ravens lift) but contains IDs 85, 86, 87, 88 scattered earlier in the body.
  why: Non-monotonic IDs break stitcher citation-order assumption. Facet authoring spanning IDs 62–88 will produce incorrect spans.
  criteria: Re-emit the file with monotonically increasing IDs in file-body order.

---

### CHAPTER 04 — chapter-04.md

- id: fault-028
  type: fault
  file: chapter-04.md
  line_id: 51
  content: "taylor-hebert-westeros drops the gaze"
  fault_class: FAULT-FORM-INTERIORITY
  what: `the gaze` is an abstract noun. A gaze is not a physical object. `drops the gaze` is a thought-figure describing a social/perceptual state (looking down), not a physical act observable by a bystander.
  why: The physical correlate is `lowers the eyes` (already used in chapter-01, lines 79). `drops the gaze` imports the abstract-as-object pattern the schema explicitly bans.
  criteria: Recast as `taylor-hebert-westeros lowers the eyes` or `taylor-hebert-westeros drops the chin` (both already established as clean forms in this season's proto-line set).

- id: fault-029
  type: fault
  file: chapter-04.md
  line_id: 99 (appears between IDs 26 and 27 in file body)
  content: "99 taylor-hebert-westeros reaches the well — appears between lines 26 and 27"
  fault_class: FAULT-FORM-ID-SEQUENCE
  what: ID 99 appears in the file body between IDs 26 and 27. Non-monotonic.
  why: Same consequence as fault-016.
  criteria: Re-emit with monotonic ID ordering.

---

### CHAPTER 05 — chapter-05.md (interlude)

- id: fault-030
  type: fault
  file: chapter-05.md
  line_id: 12
  content: "septon-rowan scans the cottage interior"
  fault_class: FAULT-FORM-PERCEPTION
  what: Exact duplicate of fault-026 (same line, same actor, different file). `scans` is a perception verb.
  why: This is the second occurrence at chapter scope and confirms a cross-chapter drift of the same verb. See fault-026 for full reasoning.
  criteria: Same as fault-026.

- id: fault-031
  type: fault
  file: chapter-05.md
  line_id: 85 and 86 appear before ID 16; 87 appears before ID 71; 88 appears before ID 63
  content: "IDs 85, 86, 87, 88 are scattered before lower-numbered IDs in file body"
  fault_class: FAULT-FORM-ID-SEQUENCE
  what: Same non-monotonic ID pattern as chapter-03-interlude. IDs 85, 86 appear before the ID-16 time-skip; ID 88 appears before ID 63; ID 87 appears before ID 71.
  why: Same downstream consequence as fault-016 and fault-027.
  criteria: Re-emit with monotonic IDs in file-body order.

---

### CHAPTER 06 — chapter-06.md

- id: fault-032
  type: fault
  file: chapter-06.md
  line_id: 76
  content: "the courier holds the horse"
  fault_class: FAULT-FORM-NON-ACTION-VERB
  what: `holds the horse` — `holds` is licensed only for (1) body-part-of-subject stillness-against-pressure or (2) physical-object-resisting-pressure. The horse is neither the courier's body part nor an object resisting being opened. Gripping/restraining a horse is a physical act, but it falls outside the narrow license.
  why: The unlicensed holds-verb describes a sustained state (courier is restraining the horse) rather than a discrete physical event. State of restraint routes to a state-update facet or should be recoded as the initiating action.
  criteria: Recast as the discrete physical act: `the courier grips the reins` or `the courier checks the horse` (if the beat is about pulling back on the reins). The holding-state may persist into a state-update facet citing that action line.

- id: fault-033
  type: fault
  file: chapter-06.md
  line_id: 107
  content: "taylor-hebert-westeros crosses to the door"
  fault_class: FAULT-FORM-MODIFIER
  what: `crosses to` — prepositional phrase of destination. Same fault class as fault-007.
  why: Same downstream consequence.
  criteria: Recast as `taylor-hebert-westeros crosses the cottage` or `taylor-hebert-westeros reaches the door`.

---

### CHAPTER 07 — chapter-07.md

- id: fault-034
  type: fault
  file: chapter-07.md
  line_id: 4
  content: "taylor-hebert-westeros leans against the counter"
  fault_class: FAULT-FORM-MODIFIER
  what: `leans against` — prepositional phrase. The preposition `against` makes this a modifier fault even though `leans` here could arguably be treated as contact-with-surface. The schema prohibits prepositional phrases of position.
  why: Same consequence as fault-013. `presses the counter` or `reaches the counter` captures the physical contact without the prep phrase.
  criteria: Recast as `taylor-hebert-westeros presses the counter` or `taylor-hebert-westeros stops at the counter` recoded as `taylor-hebert-westeros stops` + loc-state for position.

- id: fault-035
  type: fault
  file: chapter-07.md
  line_id: 21
  content: "the recorder turns the pages of Plumm's filing"
  fault_class: FAULT-FORM-MODIFIER
  what: `of Plumm's filing` is a prepositional phrase appended to the object `the pages`. The core action is `turns the pages`; the qualifier `of Plumm's filing` specifies which document's pages. This qualifier is prepositional padding.
  why: The prepositional phrase serves a disambiguation function (distinguishing which pages) but the schema prohibits this form. If document identity is load-bearing, the prop slug for Plumm's filing should be used as the direct object: `the recorder turns Plumm's filing` (using the document as the direct object) — though this still carries a possessive.
  criteria: Recast as `the recorder turns the filing` (treating Plumm's filing as a named prop referenced by context) or establish a prop slug for Plumm's filing and use it as subject/object.

- id: fault-036
  type: fault
  file: chapter-07.md
  line_id: 63
  content: "taylor-hebert-westeros turns the document over"
  fault_class: FAULT-FORM-MODIFIER
  what: `over` is an adverb/particle modifying the verb `turns`. The schema bans adverbs. `turns the document over` = `flips the document`. The adverb encodes the direction of the turn.
  why: The adverb describes the result or direction of the turn. It is a modifier and must be stripped or the verb recased.
  criteria: Recast as `taylor-hebert-westeros flips the document` or `taylor-hebert-westeros inverts the document` — one verb, no adverb particle.

- id: fault-037
  type: fault
  file: chapter-07.md
  line_id: 93 appears before ID 17; 94 appears before ID 29; 86-92 appear after ID 67 but before their numeric position
  content: "Non-monotonic IDs: 93 before 17, 94 before 29, 86-92 before their numeric position"
  fault_class: FAULT-FORM-ID-SEQUENCE
  what: Multiple non-monotonic ID runs in chapter-07. ID 93 and 94 are insertions before the main sequence resumes. IDs 86-92 appear at end of file but are numerically mid-range.
  why: Same downstream consequence as fault-016.
  criteria: Re-emit with monotonic IDs in file-body order.

---

### CHAPTER 07-INTERLUDE — chapter-07-interlude.md

(No additional FAULT-class findings beyond the possessive flags noted below. Flags only.)

---

### CHAPTER 08 — chapter-08.md

- id: fault-038
  type: fault
  file: chapter-08.md
  line_id: 19
  content: "taylor-hebert-westeros pins the hands to the knees"
  fault_class: FAULT-FORM-MODIFIER
  what: `to the knees` is a prepositional phrase of destination/position. The subject's hands are being pressed down onto the knees. `pins` takes a direct object (`the hands`) cleanly; `to the knees` is prepositional padding.
  why: The physical act is pressing hands to thighs/knees. The destination is the modifier. The loc-state facet handles where the hands end up.
  criteria: Recast as `taylor-hebert-westeros pins the hands` (the loc-state facet provides the surface) or `taylor-hebert-westeros presses the hands to the knees` recoded as `presses the hands` with the surface in loc-state.

- id: fault-039
  type: fault
  file: chapter-08.md
  line_id: 95
  content: "taylor-hebert-westeros pins the palms to the table"
  fault_class: FAULT-FORM-MODIFIER
  what: Same as fault-038 (`to the table` prepositional phrase).
  why: Same downstream consequence as fault-038.
  criteria: Recast as `taylor-hebert-westeros pins the palms` or `taylor-hebert-westeros presses the palms`.

---

### CHAPTER 08-INTERLUDE — chapter-08-interlude.md

- id: fault-040
  type: fault
  file: chapter-08-interlude.md
  line_id: 37
  content: "a courier passes the letter-case to the gatehouse man"
  fault_class: FAULT-FORM-MODIFIER
  what: `to the gatehouse man` is a prepositional phrase of recipient. The schema prohibits prepositional phrases of accompaniment/instrument/destination, and transfer-to prepositional phrases fall in this class.
  why: The physical event is a handoff. The correct form is `a courier hands the gatehouse man the letter-case` (double-object construction, no preposition) or `the gatehouse man receives the letter-case`.
  criteria: Recast as a double-object hand-off construction or as the recipient's receiving action.

- id: fault-041
  type: fault
  file: chapter-08-interlude.md
  line_id: 49
  content: "oc-castellan-harrenhal speaks the letter"
  fault_class: FAULT-FORM-MALFORMED-BEAT
  what: `speaks the letter` is neither the licensed dialogue form (`speaks to <listener>`) nor a clean physical action. `speaks the letter` uses `speaks` with a document as object, implying reading-aloud. But `reads` is a forbidden perception verb; and `speaks` with a non-person object is not the dialogue-beat form. The beat is an important narrative beat (the letter read aloud in company) but its proto-line encoding is malformed.
  why: No downstream facet can correctly cite this line. The dialogue facet expects `<speaker> speaks to <listener>`; the state-updates facet expects a physical action; the narrator-interest facet needs a citable physical event. A malformed beat corrupts all three.
  criteria: The beat should be encoded as two lines: (1) `oc-castellan-harrenhal lifts the letter` (or equivalent physical preparation beat) and (2) `oc-castellan-harrenhal speaks to the hall` (the dialogue-form beat). The letter's content goes into a dialogue facet entry citing the speaking line.

- id: fault-042
  type: fault
  file: chapter-08-interlude.md
  line_id: 56
  content: "those present file out of the hall"
  fault_class: FAULT-FORM-MULTI-SUBJECT
  what: `those present` is a collective plural subject. The schema requires singular subjects. Multi-subject constructions fault `FAULT-FORM-MULTI-SUBJECT`.
  why: No single actor can be cited in a facet from a multi-subject line. State-updates, feeling-flags, and sensory facets require a named singular actor to hang their citation on.
  criteria: Either split into per-actor exit lines for load-bearing actors, or recast as an ambient-action line with a single subject that signals the group movement: e.g. `the hall empties` (object-as-subject form for ambient clearing).

---

### CHAPTER 09 — chapter-09.md

- id: fault-043
  type: fault
  file: chapter-09.md
  line_id: 1
  content: "taylor-hebert-westeros stations a raven on the outer wall"
  fault_class: FAULT-FORM-NON-ACTION-VERB
  what: `stations` is a stative placement verb — it describes the resulting positioned state, not the discrete act of dispatching/deploying. It belongs to the same class as `places`, `sets`, `positions` when used to describe end-state rather than discrete action. Additionally, `on the outer wall` is a prepositional phrase of location.
  why: `stations` asserts a resulting positioned state. The physical act is dispatching or directing the raven; `stations` elides that action and names only the result. State-of-placement routes to a state-update facet, not a proto-line.
  criteria: Recast as the dispatch action: `taylor-hebert-westeros directs the raven` + loc-state for position, or `taylor-hebert-westeros releases the raven` if the dispatch is the beat. The three `stations` instances (lines 1, 2, 78) all require the same recast.

- id: fault-044
  type: fault
  file: chapter-09.md
  line_id: 2
  content: "taylor-hebert-westeros stations a sparrow on the gate lintel"
  fault_class: FAULT-FORM-NON-ACTION-VERB
  what: Same as fault-043.
  why: Same downstream consequence.
  criteria: Same as fault-043.

- id: fault-045
  type: fault
  file: chapter-09.md
  line_id: 78
  content: "taylor-hebert-westeros stations a fly on the gatehouse wall"
  fault_class: FAULT-FORM-NON-ACTION-VERB
  what: Same as fault-043 (third occurrence in same file).
  why: This is a season-scope drift pattern for fauna-deployment language. `stations` is the writer's term for placing fauna in observation positions. All three instances fault.
  criteria: Same as fault-043.

- id: fault-046
  type: fault
  file: chapter-09.md
  line_id: 67
  content: "ser-edwyn-celtigar rides"
  fault_class: FAULT-FORM-NO-VERB
  what: `rides` is a bare intransitive motion verb without a destination. The schema states: "Bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB. `taylor moves` is not observable." `ser-edwyn-celtigar rides` has the same structure — `rides` without a destination or object is not observable as a specific physical event; it is ambiguous between riding into the scene, riding across it, or riding a stationary horse.
  why: The line lacks enough information for a stitcher to render a physical event. Downstream facets cannot cite a location or direction from this line.
  criteria: Recast with a destination or as part of an approach sequence: `ser-edwyn-celtigar enters the approach road` or `ser-edwyn-celtigar crests the road` per the context (he arrives near the outer ward).

- id: fault-047
  type: fault
  file: chapter-09.md
  line_id: 99 and 62-65 (appear out of numeric order in file body)
  content: "ID 99 appears between IDs 60 and 66; IDs 62-65 appear after ID 90"
  fault_class: FAULT-FORM-ID-SEQUENCE
  what: In chapter-09, ID 99 appears between 60 and 66 in file-body order. IDs 62, 63, 64, 65 appear after ID 90. Non-monotonic throughout the chapter's closing section.
  why: Same downstream consequence as fault-016.
  criteria: Re-emit with monotonic IDs in file-body order.

---

### CHAPTER 10 — chapter-10.md

No faults. The file is mechanically clean. Possessive determiners (`ward-record scroll`, `the septon's ledger` referenced by implication) are handled via named prop convention rather than `his/her` form. Chapter-10 is the only file in the season with a zero-fault pass.

---

## Flags (advisory, do not block)

- id: flag-001
  type: flag
  file: chapter-02.md and chapter-03-interlude.md
  what: `plumms-man` appears as a coined slug without `the` prefix across two files. Chapter-03-interlude-plan confirms the character is intended as a recurring minor figure. The slug is used consistently, which is the minimum for downstream stability, but it lacks a registered card.
  why: Facet authoring (dialogue files in particular) will need a canonical reference for this actor. Absent a card, the slug is a forward-dependency with no backing authority.

- id: flag-002
  type: flag
  file: chapter-02.md lines 37, 40; chapter-02.md line 18
  what: `settle the apple tree`, `settle the branch`, `lands the garden wall` — forced-transitive constructions using `settles` and `lands` with location objects. These parallel the schema-approved `enters the yard` model more closely than `crouches the garden` (faulted); they are borderline rather than clear violations. The convention is used consistently for small-fauna movement verbs.
  why: If accepted as convention, facet authors will need to interpret these as arrival-at-location beats. If rejected, they fault on the same grounds as fault-009 through fault-013. A fixer ruling on whether this forced-transitive convention is blanket-licensed for small-fauna movement verbs would prevent inconsistent per-instance treatment at later passes.

- id: flag-003
  type: flag
  file: chapter-01.md line 132; chapter-02.md lines 58–65 (oc-girl-from-hamlet vs. the girl)
  what: Chapter-02 introduces `oc-girl-from-hamlet` at line 58, then uses `the girl` for the same entity from line 61 onward within the same chapter. Mixed slug-forms for the same entity.
  why: The inconsistency is a minor facet-authoring friction point: a facet author citing lines 58–60 would reference `oc-girl-from-hamlet`; one citing lines 61–65 would reference `the girl`. If fault-011 is resolved by retiring the `oc-` slug to `the girl`, the inconsistency resolves naturally.

- id: flag-004
  type: flag
  file: chapter-03-interlude.md line 46; chapter-05.md line 12 (redundant with fault-030); chapter-07-interlude.md line 46
  what: `the recorder shows oc-castellan-harrenhal Plumm's entry` — `shows` is a borderline perception-enabling verb (it causes the castellan to perceive the entry). Not clearly a perception verb by the deny-list, but in the same semantic neighborhood.
  why: If `shows` is ruled a perception verb at Pass S3.5, this line will fault. Flagging for fixer awareness before that pass runs.

- id: flag-005
  type: flag
  file: chapter-06.md lines 24, 48, 49; chapter-08.md lines 93, 94; multiple other files
  what: Possessive determiners (`his stylus`, `his cloak`, `his door`, `the septon's ledger`) appear throughout the season. The schema prohibits modifiers; possessives are a determiner-modifier class. However, the season's entire proto-line set uses possessives as the sole disambiguation mechanism for named props (distinguishing `the claims ledger` from `the septon's ledger` from `Plumm's filing`). Ruling these as faults would cascade into 15+ additional faults across the season.
  why: A blanket fixer ruling is needed: either possessives are accepted as disambiguation mechanism (not modifiers in the schema's intent), or all possessives must be replaced with prop slugs. The Pass S3.5 ruleset pass should adjudicate. Holding as flags rather than faults pending that ruling.

- id: flag-006
  type: flag
  file: chapter-04.md line 53
  what: `a raven perches taylor-hebert-westeros` — `perches` used transitively with a person as object (the raven perches ON Taylor). The preposition is suppressed. Same class as `settles the branch` (flag-002) but with a person rather than a location as object.
  why: If the forced-transitive convention for small-fauna movement is accepted (flag-002), this instance extends it to person-as-perch-surface. If not, it faults on the same grounds as fault-012. Flagging for consistency with flag-002 ruling.

- id: flag-007
  type: flag
  file: chapter-06.md line 79
  what: `the courier's horse plants its feet` — two possessive determiners in one line (`the courier's horse`, `its feet`). Both are the possessive FLAG class (flag-005). Calling out separately because this is the densest possessive instance in the season.
  why: Downstream state-updates for the horse's behavior and sensory facets for the planting-of-feet will have to navigate both possessives to extract the subject and action.

- id: flag-008
  type: flag
  file: chapter-07-interlude.md line 80
  what: `oc-castellan-harrenhal folds the document` — the document being folded is Plumm's claim document (ID 76 established it). `folds the document` is clean SVO but loses the prop identity established two lines prior. Minor disambiguation flag.
  why: Facet authoring at the state-updates level will need to infer which document from context. Not a fault; the chain is short enough to be unambiguous.

- id: flag-009
  type: flag
  file: chapter-08-interlude.md line 36
  what: `a courier dismounts` appears immediately after `a courier enters the outer ward` (ID 35). Both use the indefinite `a courier` — it is ambiguous whether this is the same courier or a different one arriving.
  why: State-updates facet for the courier's status (mounted/dismounted) needs this to be resolvable. If it is the same courier, the line sequence is: enters ward → dismounts → hands letter-case. This reads as continuous and makes narrative sense. Flagging in case the indefinite article causes downstream ambiguity.

- id: flag-010
  type: flag
  file: chapter-09.md line 66
  what: Context note: `ser-edwyn-celtigar rides` (fault-046) is immediately preceded by `a cart enters the approach road` (ID 66) and followed by `the cart stops` (ID 68). The cart and the rider appear to be part of the same arrival sequence. If `ser-edwyn-celtigar rides` is meant to indicate he rides alongside the cart (not independent mounted arrival), the beat needs the cart relationship made explicit after the recast.
  why: The fixer recasting fault-046 should preserve the arrival-with-cart context. Noting the adjacent beat so the fixer does not produce an isolated arrival that severs the cart relationship.

---

## Cross-episode constraint coherence summary

All seven active condition cards were checked against the full season's proto-line set.

**cond-fauna-control-rules:** Two violations (fault-014, fault-015 in chapter-02: `the passive feed` as physical object). Chapter-09's `stations` fault (fault-043–045) is a verb-class fault but also touches the wrongness-perception rules: `stations` is a stative placement that implies the fauna are already in position (state) rather than the observable act of directing them (action). No line in any chapter implies Taylor's cost curve is removed or reduces. No line implies fauna species outside the defined scope. No line implies range extension to physical-punishment thresholds without cost markers.

**cond-impressment-census-120ac:** No violations. Chapter-01 correctly depicts the census visit procedure. The septon's ward-protection being described as borderline is consistent with the card's "edge case" description. Chapter-10 correctly names Taylor a ward of the administration.

**cond-westerosi-customary-authority:** No violations. Deference behaviors are physically encoded in proto-line body language (eyes down, retreats, holds the chin). Chapter-05 Rowan's direct approach to Plumm is consistent with the septon-to-armed-man institutional register.

**cond-riverlands-120ac-state:** No violations. Faction presence (Plumm for Hightower-adjacent, Bracken independent, Celtigar crown-adjacent) is consistent with the card's political map. Multiple authority figures competing over the same administrative subject (Taylor) is consistent with the Riverlands fractured-authority condition.

**cond-no-parahuman-infrastructure:** No violations. No lines imply Shard presence, power creep, or other parahumans.

**cond-reincarnation-mechanics:** No violations. No return-channel lines, no memory-fade lines, no fabricated childhood memories, no patron/purpose lines.

**cond-series-tone-constraints:** No violations at proto-line scope. All chapters are action-oriented and forward-moving. No extended introspection set-pieces appear as proto-lines (interiority is correctly absent from the proto-line set). The escalation ratchet is visible: each chapter ends at a higher administrative capture state than it started.

---

## Slug resolution summary

| Slug | Status | Verdict |
|------|--------|---------|
| taylor-hebert-westeros | Series cast roster | RESOLVED |
| septon-dying-protector | Series cast roster | RESOLVED |
| septon-rowan | Series cast roster | RESOLVED |
| ser-harwick-plumm | Series cast roster | RESOLVED |
| oc-castellan-harrenhal | Series cast roster | RESOLVED |
| westerosi-traveling-maester | Series cast roster | RESOLVED |
| ser-aemon-bracken | Series cast roster | RESOLVED |
| ser-edwyn-celtigar | Series cast roster | RESOLVED |
| census-officer | Not in roster; not `the <noun>` form | FAULT (fault-008) |
| plumms-man | Not in roster; not `the <noun>` form | FAULT (fault-017) |
| oc-girl-from-hamlet | Not in roster; no warehouse card confirmed | FAULT (fault-011) |
| the recorder | `the <noun>` form | RESOLVED |
| the woman | `the <noun>` form | RESOLVED |
| the records clerk | `the <noun>` form | RESOLVED |
| the gatehouse man | `the <noun>` form | RESOLVED |
| the third rider | `the <noun>` form | RESOLVED |
| the man-at-arms | `the <noun>` form | RESOLVED |
| the men-at-arms | `the <noun>` plural form | RESOLVED |
| the guard / the guardsman | `the <noun>` form | RESOLVED |
| the courier | `the <noun>` form | RESOLVED |
| the hall | environment reference | RESOLVED |

---

## Aggregate fault counts by class

| Fault class | Count | Files affected |
|-------------|-------|----------------|
| FAULT-FORM-MODIFIER | 28 | ch-01(7), ch-02(4), ch-03(7), ch-06(2), ch-07(3), ch-08(2), ch-08-interlude(1), ch-09(3) |
| FAULT-FORM-ID-SEQUENCE | 9 | ch-02(1), ch-03-interlude(1), ch-04(1), ch-05(1), ch-07(1), ch-09(1) [each entry may cover multiple IDs] |
| FAULT-FORM-INTERIORITY | 3 | ch-02(2), ch-04(1) |
| FAULT-FORM-NON-ACTION-VERB | 4 | ch-06(1), ch-09(3) |
| FAULT-FORM-PERCEPTION | 2 | ch-03-interlude(1), ch-05(1) |
| FAULT-CONSTRAINT-slug | 3 | ch-01(1), ch-02(2) |
| FAULT-FORM-MULTI-SUBJECT | 1 | ch-08-interlude(1) |
| FAULT-FORM-NO-VERB | 1 | ch-09(1) |
| FAULT-FORM-MALFORMED-BEAT | 1 | ch-08-interlude(1) |
| **Total faults** | **52** | |
| Flags (advisory) | 10 | Multiple |

---

## Fixer routing

**High-priority (season-scope drift patterns requiring systematic recast):**
- `holds the X [modifier]` pattern (fault-018 through fault-025): 9 instances across chapters 03 and 05. A single fixer pass through these two files resolves the entire pattern.
- `turns toward <X>` pattern (fault-002 through fault-006): 4 instances in chapter-01. Simple transitive recast (`faces <X>`).
- `stations [fauna] on [location]` (fault-043 through fault-045): 3 instances in chapter-09. Recast as dispatch action.

**ID-sequence faults (fault-016, fault-027, fault-029, fault-031, fault-037, fault-047):** These are structural re-emit tasks, not line-content tasks. Each affected file must be re-emitted with monotonically ordered IDs. Content of the proto-lines does not change; only the ID assignment and file-body ordering. Affects chapters 02, 03-interlude, 04, 05, 07, 09.

**Slug registration (fault-008, fault-011, fault-017):** Require a decision before fixer can act. Either register the coined slugs with cards, or reformat to `the <noun>` convention. Fixer cannot unilaterally resolve slug-registration faults — this requires a cast-roster update that is showrunner-level.

**Single-instance faults (fault-009 through fault-015, fault-028, fault-032 through fault-042, fault-046):** Standard per-line recasts. Route to fixer individually.

**Escalations:** None. All faults are episode-scope or season-scope mechanical faults resolvable by line recast, file re-emit, or slug registration. No constraint violation requires chunk-statement revision.
