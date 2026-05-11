---
report: mechanic-audit
scope: season
target: s01 — Window 2 (IDs 159–328)
pass: S10 Phase 3 Sweep B
window: 2
timestamp: 2026-05-11
auditor-classes: AP-SCAN | CURVE-SHAPE | FREQUENCY-BAND
verdict: MECHANIC-FAIL-AP-SCAN
---

# Season s01 — Pass S10 Mechanic Audit — Window 2

## Scope

Proto-lines s01.bones.md IDs 159–328 (beats 9–17).

## CURVE-SHAPE

CANNOT-EVALUATE. No tensometer facet file exists at `active-project/theater/facets/tensometer.md`. CURVE-SHAPE review requires tensometer scalars. Unblocked pending tensometer authoring.

## FREQUENCY-BAND

CANNOT-EVALUATE. Same dependency. No tensometer file present. Unblocked pending tensometer authoring.

## AP-SCAN

FAIL. Findings below.

---

## Findings

### FAULTS

---

- id: fault-001
  type: fault
  what: ID 166 — `oc-tanner-father holds the step`
  why: Fails the narrow `holds` license. The object "the step" is not a body part of the subject and not a physical object resisting pressure. It is an idiomatic expression for "pauses motion" — an internal decision, not a physical hold action. FAULT-FORM-NON-ACTION-VERB.
  criteria: The beat must be recast as the discrete physical act visible to an observer (e.g., the subject stops, freezes, or stills), or deleted if redundant with adjacent beats.

---

- id: fault-002
  type: fault
  what: ID 226 — `the headache wakes taylor-hebert-flea-bottom`
  why: "The headache" as subject externalizes an internal physiological condition into the proto-line subject position. A headache is not a named actor slug, a prop slug, or an unnamed environment element (`the <noun>`). The beat encodes interiority (pain as cause-of-waking) as proto-line form. FAULT-FORM-INTERIORITY.
  criteria: The beat must be recast with a physical-observable subject and verb (e.g., the subject wakes, or a physical stimulus causes the waking), or the interiority must be routed to the appropriate facet that cites a physical proto-line.

---

- id: fault-003
  type: fault
  what: ID 237 — `the neighbors press the doorways`
  why: "The neighbors" is a plural unnamed group as subject. Schema rule: "Subject MUST be singular; multi-subject faults FAULT-FORM-MULTI-SUBJECT." FAULT-FORM-MULTI-SUBJECT.
  criteria: The beat must be recast with a singular subject (e.g., "the neighbor presses the doorway," or the beat is split, or a collective singular form consistent with the bones convention is adopted and documented).

---

- id: fault-004
  type: fault
  what: ID 241 — `the neighbors withdraw`
  why: Same as fault-003. "The neighbors" is a plural unnamed group as subject. FAULT-FORM-MULTI-SUBJECT.
  criteria: Same as fault-003. Singular subject required or documented collective singular convention.

---

- id: fault-005
  type: fault
  what: ID 274 — `the headache wakes taylor-hebert-flea-bottom`
  why: Identical form fault to fault-002 (ID 226). FAULT-FORM-INTERIORITY. This is a repeated pattern across at least two beats (226 and 274); both must be resolved.
  criteria: Same criteria as fault-002.

---

- id: fault-006
  type: fault
  what: ID-sequence violations — IDs 500, 508, 501, 502, 505, 496 appear out-of-monotonic-order within the file body
  why: Proto-line schema rule: "Monotonic positive integer, file-scoped... once assigned, never reused, never reassigned." The file contains the following out-of-sequence IDs embedded in the 199–207 range: 500 (after 204), 508 (after 500), 501 (after 508), 502 (after 501); and in the 274–277 range: 505 (after 275); and in the 298–299 range: 496 (after 298). These IDs are larger than the surrounding IDs and appear mid-file, meaning the sequence is not monotonic at those insertion points. The stitcher walks IDs in citation order; disordered IDs corrupt the ordering contract. FAULT-FORM-ID-SEQUENCE.
  criteria: All out-of-sequence IDs must either be renumbered to fit their physical position in the sequence (with any downstream citation mappings updated), or the bones file must be restructured so that ID ordering matches physical insertion order. The schema's stability rule applies: if these IDs were inserted as amendments after initial authoring, they must be assigned the next available ID at the tail, not inserted mid-range. A clean resolution is to reassign each out-of-sequence ID to its correct monotonic position value. All six affected IDs are: 500, 508, 501, 502, 505, 496.

---

### FLAGS

---

- id: flag-001
  type: flag
  what: ID 166 — also covered by fault-001; no additional flag needed.

---

- id: flag-002
  type: flag
  what: IDs 187, 190, 200, 209, 214, 216, 266, 267, 269, 287, 296, 297, 298 — relay/spread lines with abstract compound nouns as objects
  why: Lines of the form `the <insect-group> relay the <abstract-noun-phrase>` use abstract or event-noun objects ("the junction conversation," "the Fish Gate margin traffic," "the weather-pattern data," "the overnight network," "the junction return," "the south-wall return," "the autumn-density network," "the dock-side relay," "the eastern-quarter relay," "the register," "the rhythm," "the phrase"). The schema states "Abstraction-as-object is INTERIORITY" and faults FAULT-FORM-INTERIORITY. These lines are systematically borderline: "relay" is a physical transmission act, but when the object is an event-abstraction ("conversation," "return," "network," "rhythm"), the object is not a physical entity the observer can see being relayed. This is a pervasive pattern (13+ instances in Window 2 alone) that may be a systematic authoring drift. Flagged rather than faulted because the insect-relay convention appears to be an intentional mechanical device, but the abstract-object form should be reviewed by screen-writer and ruled on before facet authoring begins. If ruled a fault, this becomes a pattern-level kickback.
  criteria: N/A (flag). Screen-writer or fixer should determine whether relay/spread objects must be physical locations/entities (e.g., "the flies relay oc-dock-runner," "the beetles relay the door lintel") or whether abstract signal-nouns are permitted in this bones file's established convention. A ruling should be issued before Window-scope facet authoring.

---

- id: flag-003
  type: flag
  what: IDs 223–224 — consecutive `taylor-hebert-flea-bottom writes the entry` with no intervening content
  why: Two identical SVO beats in immediate sequence with no differentiation. May represent two distinct log entries (e.g., writing two separate observations) or may be a duplication artifact. No schema rule explicitly prohibits identical consecutive beats, but each proto-line should record a distinct observable event. If these represent two separate physical acts of writing, they are formally clean but should be differentiated by context (e.g., separated by a time-skip marker). If they represent a duplication error, one should be deleted.
  criteria: N/A (flag). Editor or screen-writer should verify intent and insert a time-skip or differentiated object if two distinct acts are intended.

---

- id: flag-004
  type: flag
  what: IDs 271–272 — consecutive `taylor-hebert-flea-bottom writes the entry` with no intervening content
  why: Same pattern as flag-003. Second occurrence of the duplicate consecutive write beat.
  criteria: N/A (flag). Same guidance as flag-003.

---

- id: flag-005
  type: flag
  what: IDs 234–235 — `the lords-man's man` as subject
  why: "The lords-man's man" is a possessive compound used as subject. The schema specifies valid subject forms as actor slug, prop slug, or `the <noun>` for unnamed environment elements. A possessive compound descriptor is not a standard named entity form. This entity appears to lack a slug; the possessive is functioning as an improvised identifier. Not a clear FAULT-FORM violation since the schema text does not enumerate a deny-list for non-slug subjects beyond the multi-subject rule, but the non-slug form is inconsistent with the convention of the bones file and may cause slug-resolution failures downstream.
  criteria: N/A (flag). If this entity recurs, it should be given a proper slug (e.g., `the lords-man-aide` or equivalent) for consistency with the bones naming convention.

---

- id: flag-006
  type: flag
  what: Plural insect-group subjects throughout Window 2 — "the flies," "the wasps," "the beetles," "the spiders" — appear as subjects for relay/spread beats
  why: "The flies," "the wasps," etc. are grammatically plural. The schema requires singular subjects. However, this is a consistent convention across the entire bones file (well-established from Window 1 onward), and these function as named collective entities, similar to "the flock" or "the chorus." If ruled as a collective-singular exception in the bones convention, no fault. If ruled as FAULT-FORM-MULTI-SUBJECT, this is a pervasive pattern affecting dozens of lines across the season aggregate. Flagged rather than faulted pending that ruling.
  criteria: N/A (flag). A convention ruling is needed: are insect-group collectives ("the flies," etc.) treated as singular named entities for schema compliance purposes? Ruling should be issued at session level and recorded in the bones file header or a convention note.

---

## Summary

**AP-SCAN: FAIL**

Hard faults: 6
- fault-001: ID 166 — `holds the step` — FAULT-FORM-NON-ACTION-VERB
- fault-002: ID 226 — headache as subject — FAULT-FORM-INTERIORITY
- fault-003: ID 237 — plural "the neighbors" as subject — FAULT-FORM-MULTI-SUBJECT
- fault-004: ID 241 — plural "the neighbors" as subject — FAULT-FORM-MULTI-SUBJECT
- fault-005: ID 274 — headache as subject (repeat) — FAULT-FORM-INTERIORITY
- fault-006: IDs 500, 508, 501, 502, 505, 496 — out-of-monotonic-sequence ID insertions — FAULT-FORM-ID-SEQUENCE

Flags: 6
- flag-002: Pervasive abstract-object relay/spread pattern (13+ instances) — pending convention ruling
- flag-003: Duplicate consecutive write beat, IDs 223–224
- flag-004: Duplicate consecutive write beat, IDs 271–272
- flag-005: Possessive compound subject `the lords-man's man`, IDs 234–235
- flag-006: Plural insect-group subjects throughout — pending collective-singular ruling

**CURVE-SHAPE: CANNOT-EVALUATE** — tensometer facet not yet authored.

**FREQUENCY-BAND: CANNOT-EVALUATE** — tensometer facet not yet authored.

**Combined verdict: MECHANIC-FAIL-AP-SCAN**
