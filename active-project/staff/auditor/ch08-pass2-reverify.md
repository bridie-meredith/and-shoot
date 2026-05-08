---
audit:
  scope: episode
  target: chapter-08 — The Maester's Report (proto-lines, post-fixer)
  timestamp: 2026-05-07
  pass: 2 — constraint audit (re-verify)
  total_lines: 90
  blank_timeskip_lines: 5 (lines 28, 36, 48, 60, 64, 69, 82, 88 — note: file uses multiple blank IDs)
  numbered_content_lines: 95 (IDs 1–95, excluding blank time-skips at IDs 28, 36, 48, 60, 64, 69, 82, 88)
  correct_count: 67
  fault_count: 18
  flag_count: 2
  faults_by_class:
    FAULT-FORM-PERCEPTION: 5
    FAULT-FORM-MODIFIER: 8
    FAULT-FORM-NEGATION: 1
    FAULT-FORM-MULTI-SUBJECT: 2
    FAULT-FORM-NON-ACTION-VERB: 1
    FAULT-FORM-CONJUNCTION: 1
  header_status: CORRECT (narrator and goal both present and valid)
---

# Header Checks

narrator: `taylor-hebert-westeros` — present in series cast roster. CORRECT.
goal: present and populated. CORRECT.

---

# Summary

18 faults across 15 line IDs. All faults are episode-scope. Zero constraint-card violations found (the acts depicted are procedurally consistent with `cond-impressment-census-120ac` and `cond-westerosi-customary-authority`). Zero physical-presence or prop-absent faults (actor transits from prior locations to Harrenhal hall are covered by time-skips at IDs 28, 36, 48). No FAULT-HEADER-* faults.

The most concentrated fault class is FAULT-FORM-PERCEPTION: five instances of `reads` applied to a named subject reading a prop. All five must be recast as the physical event the reading-act produces (e.g., the subject `moves` through the document, or the subject `speaks` its content, or the subject `marks`/`sets down` after the reading-act). The `reads` verb is a POV-leak regardless of whether the reader is the POV character.

---

# Findings

## fault-001
- id: fault-001
- type: fault
- what: line 10 — `taylor-hebert-westeros reads the word-list aloud`
- why: `reads` is a banned perception verb. POV-leak regardless of POV character assignment. Survives into pass 3 and shapes sequence around an illegal spine entry.
- criteria: line must record the physical act observable by a bystander — the subject's mouth moving, the subject producing spoken sounds, or the subject's hand tracing. `reads` must not appear. Recast as the discrete physical event.
- recommended_action: RECAST-PHYSICAL (e.g., `taylor-hebert-westeros speaks the word-list aloud` — but "aloud" is then a modifier fault; preferred: split into two lines: (a) subject speaks the list, (b) maester marks — or recast as `taylor-hebert-westeros traces the word-list` / `taylor-hebert-westeros recites the word-list`)

---

## fault-002
- id: fault-002
- type: fault
- what: line 15 — `the westerosi-traveling-maester produces a sketch — a diagram of grain-measures`
- why: the em-dash appositive `— a diagram of grain-measures` is descriptive padding on the object. The SVO spine carries `produces a sketch`; the appositive adds explanatory content that belongs in a facet, not the bone. No modifiers.
- criteria: object must be a single named prop slug or `the <noun>` without appositional expansion.
- recommended_action: DELETE the appositive tail. Line becomes `the westerosi-traveling-maester produces a sketch`.

---

## fault-003
- id: fault-003
- type: fault
- what: line 19 — `taylor-hebert-westeros presses the hands flat on the knees`
- why: `flat` is an adjectival modifier on the object `the hands`; `on the knees` is a prepositional-location phrase (location context goes in citations, not in the proto-line). Two modifier violations on a single line.
- criteria: line must be clean SVO with no modifiers and no prepositional padding. Location and manner belong in facets.
- recommended_action: DELETE modifiers. Line becomes `taylor-hebert-westeros presses the hands on the knees` — but `on the knees` remains a locative PP. Preferred: `taylor-hebert-westeros presses the hands flat` → still has `flat`; cleanest recast: `taylor-hebert-westeros pins the hands to the knees` (removes `flat`; `to the knees` is destination of the press, borderline but more defensible as object). Fixer determines minimum change.

---

## fault-004
- id: fault-004
- type: fault
- what: line 27 — `taylor-hebert-westeros roots the feet to the floor`
- why: `roots` is a non-action verb — its primary semantic is stative position (being rooted in place) rather than a discrete observable act. Per the schema, stative position-naming verbs that describe a state rather than a posture-act are banned. `roots the feet to the floor` encodes an interior psychological state (frozen by consequence) as a pseudo-action. The physical event it attempts to capture — Taylor does not move — cannot be rendered as SVO action; it is absence of action and belongs in a state-update or feeling facet, not the proto-line spine.
- criteria: line must either (a) be deleted and the state moved to a facet citation, or (b) recast as the one discrete physical act that occurred (e.g., if Taylor sat back down, or braced against a surface, that act is the proto-line).
- recommended_action: DELETE (the interior frozen-state is a feeling-flag or state-update, not a proto-line beat).

---

## fault-005
- id: fault-005
- type: fault
- what: line 42 — `oc-castellan-harrenhal reads the document`
- why: `reads` is a banned perception verb. Same class as fault-001.
- criteria: line must record the physical act a bystander observes when the castellan processes the document — eyes moving, head position, hands on paper. `reads` must not appear.
- recommended_action: RECAST-PHYSICAL (e.g., `oc-castellan-harrenhal reviews the document` is still cognitive; preferred: `oc-castellan-harrenhal moves through the document` or DELETE — the set/speaks sequence around it establishes the reading beat without the perception verb).

---

## fault-006
- id: fault-006
- type: fault
- what: line 47 — `ser-aemon-bracken withdraws from the table`
- why: `withdraws from the table` is a motion verb with source-only (`from the table`), no destination. Per the SVO brief, bare intransitive motion verbs that lose meaning without destination are banned (`taylor moves` with no observable outcome is the cited example). `withdraws from` communicates departure-from-position but specifies no observable landing. The physical action is incomplete as stated.
- criteria: line must specify a destination or recast as a departure with observable terminus (e.g., `ser-aemon-bracken steps back from the table`, `ser-aemon-bracken retreats to the door`). `from` alone is not sufficient.
- recommended_action: RECAST-PHYSICAL — specify destination or replace with `steps back` toward a named location.

---

## fault-007
- id: fault-007
- type: fault
- what: line 53 — `ser-harwick-plumm reads the counter-claim document`
- why: `reads` is a banned perception verb. Same class as fault-001 and fault-005.
- criteria: line must recast `reads` as the observable physical act. `reads` must not appear.
- recommended_action: RECAST-PHYSICAL (same options as fault-005; or DELETE — flanking `takes` and `sets down` lines establish the handling beat without requiring the perception verb).

---

## fault-008
- id: fault-008
- type: fault
- what: line 63 — `taylor-hebert-westeros stops at the chancel step`
- why: `at the chancel step` is a prepositional-location phrase — location context goes in citations to loc-state, not in the proto-line body. The SVO spine is `taylor-hebert-westeros stops`; the location is padding.
- criteria: line must remove the locative prepositional phrase. Location attaches via facet citation at facet-authoring time.
- recommended_action: DELETE the prepositional phrase. Line becomes `taylor-hebert-westeros stops`.

---

## fault-009
- id: fault-009
- type: fault
- what: line 75 — `oc-castellan-harrenhal reads the letter`
- why: `reads` is a banned perception verb. Same class as fault-001, fault-005, fault-007.
- criteria: line must recast `reads` as observable physical act. `reads` must not appear.
- recommended_action: RECAST-PHYSICAL or DELETE — the surrounding lines (removes letter from case, breaks seal, sets letter on table, speaks to hall, lifts letter, reads aloud) establish the beat; the intermediate `reads` before speaking may be redundant and deletable.

---

## fault-010
- id: fault-010
- type: fault
- what: line 79 — `oc-castellan-harrenhal reads the letter aloud`
- why: `reads` is a banned perception verb (fault class same as fault-001); `aloud` is an adverb modifier (FAULT-FORM-MODIFIER). Two violations on one line.
- criteria: line must recast `reads` as observable physical act and remove the adverb `aloud`. The act of speaking the letter's contents to the assembled hall must be expressed through a verb that captures the physical event (voice producing sound, mouth moving, body presenting the document while speaking).
- recommended_action: RECAST-PHYSICAL — e.g., `oc-castellan-harrenhal speaks the letter to the hall` (removes both `reads` and `aloud`); or split: (a) `oc-castellan-harrenhal lifts the letter` [already present at line 78], (b) `oc-castellan-harrenhal speaks the letter` — fixer determines minimum change.

---

## fault-011
- id: fault-011
- type: fault
- what: line 80 — `ser-aemon-bracken draws a controlled breath`
- why: `controlled` is an adjective modifying `breath`. No modifiers permitted. The modifier also imports interiority (that the breath is deliberately controlled signals internal self-regulation — FAULT-FORM-MODIFIER crosses into FAULT-FORM-INTERIORITY territory, though the primary classification is the adjective violation).
- criteria: line must remove the modifier. The physical act is `draws a breath` without characterization of its quality.
- recommended_action: DELETE modifier. Line becomes `ser-aemon-bracken draws a breath`.

---

## fault-012
- id: fault-012
- type: fault
- what: line 81 — `those present do not speak`
- why: (1) FAULT-FORM-NEGATION — `do not speak` is a negation construction. Negations are banned. (2) FAULT-FORM-MULTI-SUBJECT — `those present` is an indefinite plural collective, not a named entity or `the <noun>`. The subject must be a slug, a proper name, or `the <noun>` (singular or group-noun). `Those present` is neither.
- criteria: line must (a) eliminate the negation — silence is a state, not an action; if the beat is load-bearing, recast as the physical observable that signals silence (no movement at the door, stillness in the room); and (b) replace the subject with a named entity or delete if the beat is a state rather than an action.
- recommended_action: DELETE — silence/stillness after the letter is read aloud is a state that belongs in a state-update or feeling-flag facet, not a proto-line action. If the beat is retained, recast around a specific named actor's observable action.

---

## fault-013
- id: fault-013
- type: fault
- what: line 84 — `oc-castellan-harrenhal places the letter beside the sealed roll and the counter-claim`
- why: (1) FAULT-FORM-CONJUNCTION — `and` joins `the sealed roll` and `the counter-claim` in the prepositional object. The SVO rules ban `and` without exception; the conjunction here is in a locative prepositional phrase, not joining two beats, but the rule is stated without exception for the spine. (2) FAULT-FORM-MODIFIER — `beside the sealed roll and the counter-claim` is a prepositional-location phrase specifying placement destination; location goes in citations, not the proto-line.
- criteria: line must remove the locative prepositional phrase. The physical act is the placement; the destination is facet territory.
- recommended_action: DELETE the locative tail. Line becomes `oc-castellan-harrenhal places the letter on the table` — but `on the table` is also a locative PP; cleanest: `oc-castellan-harrenhal places the letter` (destination inferred from context or cited via loc-state).

---

## fault-014
- id: fault-014
- type: fault
- what: line 86 — `those present file out of the hall`
- why: FAULT-FORM-MULTI-SUBJECT — `those present` is an indefinite plural collective, not a named entity or `the <noun>`. Same class as fault-012. The subject must be a named entity, slug, or `the <noun>`.
- criteria: if the group-exit beat is load-bearing, recast around a named actor's exit or a single collective noun (`the hall empties` — object-as-subject form, licensed when actor is unspecified/ambient). If not load-bearing, DELETE.
- recommended_action: RECAST-PHYSICAL — `the hall empties` (object-as-subject, licensed form per SVO brief) or `the assembled men file out` (still plural — not ideal). Fixer determines minimum change; `the hall empties` is the cleanest compliant form.

---

## fault-015
- id: fault-015
- type: fault
- what: line 87 — `ser-aemon-bracken exits last`
- why: `last` is an adverb modifying the verb. No adverbs permitted. The sequencing information (`last`) is temporal/narrative padding that belongs in a facet or is implied by position in the proto-line sequence, not in the SVO spine.
- criteria: line must remove the adverb. The physical act is `ser-aemon-bracken exits the hall` (or exits with destination specified).
- recommended_action: DELETE adverb. Line becomes `ser-aemon-bracken exits the hall`.

---

## fault-016
- id: fault-016
- type: fault
- what: line 92 — `taylor-hebert-westeros sits at the septon's table`
- why: `sits at` is a stative position-naming construction — it describes where the subject is seated (position), not the act of sitting-down (posture-act). Per the schema, `sits` used to describe position rather than a posture-act is banned. Compare to line 8: `taylor-hebert-westeros takes the seat` — that is the correct form for the sitting-down act. `Sits at` encodes arrival-in-position as a state assertion.
- criteria: line must recast as the discrete physical act of sitting-down, not the resulting positional state. The chair/table is the destination of the act, not a location modifier.
- recommended_action: RECAST-PHYSICAL — e.g., `taylor-hebert-westeros takes the seat at the septon's table` — but `at the septon's table` is then a locative PP; cleanest: `taylor-hebert-westeros takes the septon's seat` (names the object acted upon rather than location).

---

## fault-017
- id: fault-017
- type: fault
- what: line 95 — `taylor-hebert-westeros presses the palms flat on the table`
- why: `flat` is an adjectival modifier; `on the table` is a prepositional-location phrase. Two modifier violations. Same fault pattern as fault-003 (line 19).
- criteria: line must be clean SVO with no modifiers and no prepositional padding.
- recommended_action: DELETE modifiers. Same fixer path as fault-003.

---

# Flags (advisory, non-blocking)

## flag-001
- id: flag-001
- type: flag
- what: line 68 and line 70 — `the gatehouse man carries the letter-case to the hall` / blank ID 69 / `the gatehouse man enters the hall`
- why: the time-skip at ID 69 sits between `carries to the hall` and `enters the hall`. Carrying something to the hall and entering the hall are simultaneous or immediately sequential events; a time-skip implying elapsed time between them creates a spatial logic tension (the gatehouse man is in transit between lines 68 and 70 for an unspecified interval). This is not a Pass 2 fault; it is a Pass 3/5 (shape/continuity) concern. Noted here as advisory for the downstream pass.
- criteria: no fixer action at Pass 2. Advisory for Pass 3 dramatist.

---

## flag-002
- id: flag-002
- type: flag
- what: lines 61–63 (taylor-hebert-westeros in the sept nave, approaching the chancel steps)
- why: Taylor's state at chapter-open places her at loc-harrenhal-sept-environs. The cottage in lines 5–8 is the assessment cottage at the smallfolk settlement (consistent with where the maester was). Taylor's transition from the assessment cottage (lines 5–26) to the sept (lines 61–63) is covered by the time-skip at ID 64, but there is no prior time-skip covering the transit between the cottage scene (ending at line 27) and the castellan's-hall scenes (lines 29–59). The castellan's hall scenes are not from Taylor's POV — they are presented as events Taylor cannot directly observe. This is a POV-consistency issue for Pass 5, not a Pass 2 form or constraint fault. Noted as advisory.
- criteria: no fixer action at Pass 2. Advisory for Pass 5 continuity auditor (POV check).

---

# CONTINUITY STATUS

FAULTS PRESENT — 18 faults across 15 line IDs. File does not clear Pass 2. Route to fixer.
Fixer applies minimum-change repairs per criteria above. After fixer commits, Pass 2 re-runs on modified lines only.
