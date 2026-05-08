# Audit Report — ch09 Pass 2 Re-verify (Post-Fixer)

schema: audit-report
episode: chapter-09
pass: 2 (constraint audit)
run: re-verify (post-fixer)
date: 2026-05-07
auditor: fork (fresh context)
target: active-project/theater/proto-lines/chapter-09.md

---

## Header check

narrator: `taylor-hebert-westeros` — present, resolves to active cast. PASS.
goal: present and non-empty. PASS.

---

## Summary

Total numbered lines (excluding blank time-skips): 92
CORRECT: 79
FAULT: 13
FLAG: 0 (borderline candidates resolved to fault or clean — see notes)

Fault breakdown:
- FAULT-FORM-MODIFIER: 4
- FAULT-FORM-PERCEPTION: 4
- FAULT-FORM-NON-ACTION-VERB: 5

Constraint faults (FAULT-CONSTRAINT-*): 0
Physical faults (FAULT-PHYSICAL-*): 0

---

## Per-fault findings

---

### fault-001

- **id:** fault-001
- **type:** fault
- **line:** 19
- **content:** `the man-at-arms blocks the doorway`
- **fault class:** FAULT-FORM-NON-ACTION-VERB
- **what:** `blocks` names the consequence-state of line 18 (`a man-at-arms steps into the doorway`). It asserts the arrangement ("the man is now blocking") rather than recording a discrete physical act. The observable act is the stepping (line 18); `blocks` is its state-label.
- **why:** State-assertions in the SVO spine corrupt downstream facet reasoning — the shape pass and continuity pass will treat this as a separate action beat, inflating the line count with a non-act. Line 19 is a redundant state-naming of line 18's result.
- **criteria:** DELETE line 19. Line 18 carries the full physical event. If the blocking consequence must be explicit, recast as an act: e.g., `the man-at-arms spreads the arms` — but deletion is preferred.
- **recommended action:** DELETE

---

### fault-002

- **id:** fault-002
- **type:** fault
- **line:** 30
- **content:** `ser-aemon-bracken draws a folded page`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `folded` is an adjective modifying `page`. Modifiers are banned from proto-lines — no adjectives, adverbs, prepositional padding.
- **why:** Modifier smuggles descriptive state into the bone spine. The prop's physical condition belongs in a downstream state-update or location-state facet, not in the SVO line itself.
- **criteria:** Recast as `ser-aemon-bracken draws a page`. Prop condition routes to facet.
- **recommended action:** RECAST-PHYSICAL

---

### fault-003

- **id:** fault-003
- **type:** fault
- **line:** 40
- **content:** `oc-castellan-harrenhal reads the page`
- **fault class:** FAULT-FORM-PERCEPTION
- **what:** `reads` is an explicitly banned perception verb (per both the pass-2 brief and the SVO tuning package). It asserts a cognitive act the spine cannot witness.
- **why:** Perception verbs assert what a character receives from looking, not what an observer would see. The physical observable act is the castellan's eyes moving across the page; what the castellan extracts from reading is facet material. Allowing `reads` into the spine seeds downstream shape/trim/continuity passes with an internal-state beat.
- **criteria:** Recast as the observable physical correlate: e.g., `oc-castellan-harrenhal scans the page` is also a perception verb — instead use `oc-castellan-harrenhal lifts the page` (already on line 39) plus a new `oc-castellan-harrenhal lowers the page` or `oc-castellan-harrenhal pauses over the page`. Alternatively DELETE if line 39 (lifts) plus line 41 (sets aside) already bracket the reading beat adequately for downstream facet citation.
- **recommended action:** DELETE or RECAST-PHYSICAL

---

### fault-004

- **id:** fault-004
- **type:** fault
- **line:** 69
- **content:** `ser-edwyn-celtigar rides beside the cart`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `beside the cart` is a prepositional phrase acting as a spatial modifier on the motion verb `rides`. The proto-line schema bans prepositional padding. The spatial relationship (flanking the cart) is a descriptor of position, not the discrete act.
- **why:** `rides` is the act; where relative to the cart is a state descriptor. Padding on motion verbs contaminates the spine with arrangement-as-action beats, which inflate line count and misrepresent causality in the shape pass.
- **criteria:** Recast as `ser-edwyn-celtigar rides` — pure intransitive motion — or replace with a specific destination: `ser-edwyn-celtigar approaches the postern gate` (which line 73 already handles). Consider DELETE if line 73 covers the same beat.
- **recommended action:** DELETE or RECAST-PHYSICAL

---

### fault-005

- **id:** fault-005
- **type:** fault
- **line:** 70
- **content:** `two riders flank the cart`
- **fault class:** FAULT-FORM-NON-ACTION-VERB
- **what:** `flank` names a spatial arrangement — the riders are positioned on the sides of the cart. It does not record a discrete physical act (the moment of taking up flanking position). As used here (present tense, describing the arriving group's formation), it asserts the arrangement as a state.
- **why:** Spatial arrangement assertions belong in location-state facets. In the SVO spine, `flank` presents as an act but is structurally a stative position-naming — the same banned category as `stands in X` or `sits at Y` when they describe position rather than posture-act.
- **criteria:** Recast as the discrete motion that establishes the flanking: e.g., `a rider moves to the cart side` (two lines if both flanks matter) — or DELETE if the arrival formation is covered adequately by the cart's entry (line 68) and the riders are unnamed environmental detail.
- **recommended action:** DELETE or SPLIT-INTO-N

---

### fault-006

- **id:** fault-006
- **type:** fault
- **line:** 77
- **content:** `the guard examines the document`
- **fault class:** FAULT-FORM-PERCEPTION
- **what:** `examines` is a perception-evaluation verb — it asserts that the guard is looking at and assessing the document. Though not on the explicit banned list by name, it falls under the "other POV-leak verb" clause: it names a cognitive perceptual act (assessment via looking), not a physically discrete motion.
- **why:** An observer sees the guard holding the document and moving their eyes. Whether the guard is "examining" (evaluating) is an interior assertion. Allowing perception-evaluation verbs generates the same downstream contamination as `reads`, `tracks`, or `noted` — the facet passes inherit a cognitive claim the proto-line cannot source.
- **criteria:** Recast as the physical observable: `the guard turns the document`, `the guard holds the document toward the light`, or — if the key beat is just that the guard looks at it before acting — DELETE in favor of the surrounding lines (76: hands, 78: steps aside) which bracket the inspection beat adequately.
- **recommended action:** DELETE or RECAST-PHYSICAL

---

### fault-007

- **id:** fault-007
- **type:** fault
- **line:** 82
- **content:** `oc-castellan-harrenhal receives ser-edwyn-celtigar`
- **fault class:** FAULT-FORM-NON-ACTION-VERB
- **what:** `receives` in the sense of formally receiving a visitor names a social-ceremonial state, not a discrete physical act. It is a social arrangement verb with the same structural profile as the banned possession/containment class: it asserts a relational condition (the castellan is now in the presence of / in formal reception of the visitor) rather than recording a physical motion.
- **why:** Social state-naming in the SVO spine suppresses the physical beats that constitute the reception — approach, greeting gesture, turn-to-face. Leaving `receives` in place gives downstream passes a hollow beat with no physical content to build on.
- **criteria:** Recast as the specific physical act: `oc-castellan-harrenhal turns to ser-edwyn-celtigar`, `oc-castellan-harrenhal crosses to ser-edwyn-celtigar`, or a greeting gesture. Alternatively DELETE if line 83 (`oc-castellan-harrenhal speaks to ser-edwyn-celtigar` — wait, it's `ser-edwyn-celtigar speaks to oc-castellan-harrenhal`, line 83) covers the first contact beat adequately.
- **recommended action:** DELETE or RECAST-PHYSICAL

---

### fault-008

- **id:** fault-008
- **type:** fault
- **line:** 87
- **content:** `ser-edwyn-celtigar examines the document`
- **fault class:** FAULT-FORM-PERCEPTION
- **what:** Same as fault-006. `examines` is a perception-evaluation verb, falling under the "other POV-leak verb" clause.
- **why:** See fault-006. The physical correlate (Celtigar holding and looking at the document) is covered by the surrounding action sequence (line 86: castellan speaks; line 91: Celtigar sets it down). The `examines` beat asserts cognitive assessment the spine cannot record.
- **criteria:** DELETE or recast as physical: `ser-edwyn-celtigar turns the document`, `ser-edwyn-celtigar holds the document to the light`.
- **recommended action:** DELETE or RECAST-PHYSICAL

---

### fault-009

- **id:** fault-009
- **type:** fault
- **line:** 88
- **content:** `ser-edwyn-celtigar examines the page`
- **fault class:** FAULT-FORM-PERCEPTION
- **what:** Same fault class as fault-006 and fault-008. `examines` repeated on a second prop.
- **why:** See fault-006. Both document and page being `examined` in successive lines doubles the perception-verb problem and suggests the fixer repair at fault-008 should be applied consistently to fault-009 simultaneously.
- **criteria:** DELETE or recast as physical. Coordinate fix with fault-008 to ensure the parallel treatment of document and page is consistent (both deleted or both recast in the same physical form).
- **recommended action:** DELETE or RECAST-PHYSICAL

---

### fault-010

- **id:** fault-010
- **type:** fault
- **line:** 96
- **content:** `taylor-hebert-westeros presses the palms flat`
- **fault class:** FAULT-FORM-MODIFIER
- **what:** `flat` is an adverbial/adjectival modifier on the pressing action. Modifiers are banned.
- **why:** Descriptor of the result-state of the press belongs in a downstream facet (feeling-flag, sensory-flag). In the spine it is padding that smuggles a sensory cue into the structural bone.
- **criteria:** Recast as `taylor-hebert-westeros presses the palms` — removing `flat`. If the result-state (flat position achieved) is the load-bearing beat, it belongs in a state-update facet citing this proto-line.
- **recommended action:** RECAST-PHYSICAL

---

### fault-011

- **id:** fault-011
- **type:** fault
- **line:** 97
- **content:** `taylor-hebert-westeros holds the chin angle`
- **fault class:** FAULT-FORM-NON-ACTION-VERB
- **what:** `holds the chin angle` — `the chin angle` is an abstract noun phrase, not a physical object. This matches the explicitly banned `holds`-with-abstract-object pattern (the brief gives `holds the silence` as the paradigm case). A "chin angle" is a positional descriptor, not a grippable physical entity.
- **why:** `holds` with an abstract object is a stative assertion dressed as a physical act. It asserts a maintained physical position, which is state content — it belongs in a state-update facet as a maintained posture condition, not in the SVO spine as an action beat.
- **criteria:** Recast as the physical act that maintains the position: `taylor-hebert-westeros lifts the chin`, `taylor-hebert-westeros sets the jaw` — any discrete physical act that initiates the held position. The persistence of the hold routes to a state-update facet.
- **recommended action:** RECAST-PHYSICAL

---

## Constraint check summary

**cond-westerosi-customary-authority:** No violations. Taylor operates through fauna network only; no direct interaction with authority figures in this chapter. No beats show Taylor speaking to or being observed by men-at-arms or the castellan. Constraint is not activated by the surviving beats.

**cond-riverlands-120ac-state:** No violations. The administrative contest (competing guardianship claims presented to the castellan) is coherent with the ambient faction-pressure the card describes. The document/page exchange between Plumm, Bracken, and the castellan is consistent with the card's depiction of competing lords using administrative machinery.

**cond-fauna-control-rules:** No violations. Species used — raven, sparrow, fly — are all within the card's "in scope" list. Taylor's use is intermittent across time-skips, not continuous 30-minute operation. Single-animal positioning (one raven to the gatehouse sill, line 37) is within the card's concealment guidance. No line places Taylor in extended cross-class simultaneous operation past the cost threshold. The `withdraws` beats (lines 64–65, 95) show active cost management.

**cond-series-tone-constraints:** No violations at the proto-line level. The chapter is action-only (no introspective monologue beats in the spine). Taylor's role as observer rather than actor is structurally enforced by the beat sequence. No register drift flagged.

**Series laws (showrunner memory):** No violations. Taylor does not speak, act, or appear in the argument scenes — consistent with "Taylor retains parallel multithreaded fauna control" as her only active capability here. No parahuman infrastructure implied. No shard buffering assumed. Fauna-control physical cost curve is not contradicted.

---

## Physical check summary

No FAULT-PHYSICAL findings. All named actors resolve to the chapter cast list and series roster. All named locations (outer ward, gatehouse, postern gate, approach road) are fixed props of `loc-harrenhal-exterior`. Props named (document, page, table, reins) are contextually plausible for the location and scene function; none contradict the location card's fixed-prop list or any actor inventory record. `a groom`, `a man-at-arms`, `a garrison guard`, `two riders` are unnamed ambient figures using the permitted `a <noun>` / `the <noun>` form.

---

## Termination status

FAULTS PRESENT. Not CONTINUITY-OK. Fixer dispatch required for fault-001 through fault-011.

After fixer commits changes, pass 2 re-runs on modified lines only. Iterate until report is empty, then advance to pass 3.
