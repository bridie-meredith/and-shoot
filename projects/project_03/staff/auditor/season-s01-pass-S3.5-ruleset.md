audit:
  scope: season
  target: s01 (chapter-01 through chapter-10)
  timestamp: 2026-05-07
  pass: S3.5 — mechanic-strictness (deny-list, bans, borderline adjudication)

---

## Findings

findings:

  # ── CHECK 1: TRAILING PREPOSITIONAL PHRASES ─────────────────────────────────

  - id: fault-001
    type: fault
    file: chapter-01.md
    line_id: 1
    content: "taylor-hebert-westeros wakes in the loft"
    what: "in the loft" is a prepositional phrase of place appended to a clean SVO.
    why: Place/destination routing must go to location-state citations, not into the proto-line body. Modifier pollution sets a template for downstream stitcher confusion.
    criteria: The proto-line must name only the physical action without prepositional padding. The location is available from context and location-state facets.

  - id: fault-002
    type: fault
    file: chapter-01.md
    line_id: 41
    content: "taylor-hebert-westeros crosses to the materials"
    what: "to the materials" is a prepositional destination phrase attached to a motion verb. FAULT-FORM-MODIFIER.
    why: The schema explicitly bans "crosses to X" as a trailing prep variant; it instructs use of a transitive verb that takes the destination as direct object (e.g., "reaches the materials").
    criteria: Recast as a transitive verb whose direct object is the destination entity, with no prepositional phrase.

  - id: fault-003
    type: fault
    file: chapter-01.md
    line_id: 56
    content: "the men-at-arms cross to the yard entrance"
    what: "to the yard entrance" is a prepositional destination phrase. FAULT-FORM-MODIFIER.
    why: Same as fault-002. "cross to X" is the banned form.
    criteria: Recast as a transitive-takes-destination verb with no trailing prep phrase (e.g., "the men-at-arms reach the yard entrance" or "the men-at-arms enter the yard entrance").

  - id: fault-004
    type: fault
    file: chapter-01.md
    line_id: 58
    content: "oc-census-officer crosses to the cottage door"
    what: "to the cottage door" is a prepositional destination phrase. FAULT-FORM-MODIFIER.
    why: Same as fault-002.
    criteria: Recast as transitive-takes-destination with no trailing prep phrase (e.g., "oc-census-officer reaches the cottage door").

  - id: fault-005
    type: fault
    file: chapter-01.md
    line_id: 100
    content: "taylor-hebert-westeros follows to the yard"
    what: "to the yard" is a prepositional destination phrase appended to a motion verb. FAULT-FORM-MODIFIER.
    why: "follows to X" is the banned `motion verb + to <X>` form. Additionally, "follows" without a named entity being followed loses the observable event.
    criteria: Recast so the motion is expressed as a transitive verb taking the destination as direct object (e.g., "taylor-hebert-westeros enters the yard") and the following relationship, if load-bearing, is expressed in a separate proto-line or facet.

  - id: fault-006
    type: fault
    file: chapter-03.md
    line_id: 30
    content: "taylor-hebert-westeros kneels at the altar"
    what: "at the altar" is a prepositional phrase of place. FAULT-FORM-MODIFIER.
    why: The schema bans prepositional phrases of place/destination/source/direction. The kneeling location must route to location-state citations.
    criteria: The proto-line must reduce to the bare action without prepositional padding ("taylor-hebert-westeros kneels").

  - id: fault-007
    type: fault
    file: chapter-08.md
    line_id: 4
    content: "an armed man plants the feet at the cottage door"
    what: "at the cottage door" is a prepositional phrase of place appended to the SVO. FAULT-FORM-MODIFIER.
    why: Place routing belongs in location-state citations. The prep phrase also adds a result-state modifier to the "plants the feet" action (holds-modifier license issue — see fault-016 below).
    criteria: The proto-line must reduce to the bare action without the prepositional place phrase. The location context is available from the surrounding beat.

  - id: fault-008
    type: fault
    file: chapter-09.md
    line_id: 6
    content: "the rider hands the reins to a groom"
    what: "to a groom" is a prepositional indirect-object phrase. Even though "hands X to Y" is a standard ditransitive form, the schema bans prepositional phrases of accompaniment/destination/instrument appended after the direct object. FAULT-FORM-MODIFIER.
    why: The schema does not carve out an exception for ditransitive verbs. All trailing prep phrases are banned. The event of transfer can be expressed with a transitive verb (e.g., "the rider passes the reins" or split into two beats: "the rider extends the reins / the groom takes the reins").
    criteria: The proto-line must express the transfer without a trailing "to <entity>" prepositional phrase.

  - id: fault-009
    type: fault
    file: chapter-10.md
    line_id: 19
    content: "oc-castellan-harrenhal returns to the table"
    what: "to the table" is a prepositional destination phrase. FAULT-FORM-MODIFIER.
    why: Motion verb + "to <X>" is the banned form. The destination must be the direct object of a transitive verb.
    criteria: Recast as a transitive-takes-destination verb with no trailing prep phrase (e.g., "oc-castellan-harrenhal reaches the table").

  # ── CHECK 2: `turns to X` / `turns toward X` BAN ────────────────────────────

  # No instances of "turns to <named entity>" or "turns toward <named entity>" found across all 10 chapters.
  # Bare "turns" (intransitive, no destination) appears at: ch01-112 (the riders turn), ch01-123 (taylor turns),
  # ch02-25 (oc-plumms-man turns), ch02-26 (the sparrow turns), ch02-78 (oc-plumms-man turns),
  # ch04-89 (oc-castellan-harrenhal turns), ch05-33 (ser-harwick-plumm turns), ch05-73 (septon-rowan turns).
  # All are bare intransitive with no destination implied by prepositional phrase. All licensed.

  - id: fault-010
    type: pass
    what: turns-to-X / turns-toward-X ban
    why: No instances found. All bare "turns" occurrences are intransitive with no destination phrase.

  # ── CHECK 3: DIRECTIONAL ADVERBS ────────────────────────────────────────────

  - id: fault-011
    type: fault
    file: chapter-01.md
    line_id: 48
    content: "oc-census-officer calls out"
    what: "out" is a directional adverb appended to the verb. FAULT-FORM-MODIFIER.
    why: Directional adverbs are banned. The observable action of calling aloud can be expressed without the adverb (e.g., "oc-census-officer calls" or a dialogue beat).
    criteria: The proto-line must not carry a trailing directional adverb.

  - id: fault-012
    type: fault
    file: chapter-07.md
    line_id: 56
    content: "septon-rowan sets the satchel down"
    what: "down" is a directional adverb appended to the verb-object pair. FAULT-FORM-MODIFIER.
    why: Directional adverbs are banned. "sets the satchel" is the clean SVO; "down" specifies direction and is padding.
    criteria: The proto-line must reduce to "septon-rowan sets the satchel" (or a transitive equivalent) without the directional adverb.

  # ── CHECK 4: POSSESSIVE DETERMINER BAN ──────────────────────────────────────

  - id: fault-013
    type: fault
    file: chapter-01.md
    line_id: 124
    content: "taylor-hebert-westeros takes the septon's materials"
    what: "septon's" is a possessive determiner on a prop/object. Should be "the materials" or "the septon materials." Possessive determiners are banned; all body-parts and props use "the <object>."
    why: Possessive determiners introduce character-ownership framing into the bone structure that belongs in state-update facets, not proto-lines.
    criteria: The possessive must be replaced with the definite article form ("the materials") or a slug-qualified form, with no possessive apostrophe construction.

  - id: fault-014
    type: fault
    file: chapter-06.md
    line_id: 24
    content: "septon-rowan takes his stylus"
    what: "his stylus" — possessive determiner "his" on a prop. Should be "the stylus."
    why: Same as fault-013.
    criteria: Possessive must be replaced with definite article ("the stylus").

  - id: fault-015
    type: fault
    file: chapter-06.md
    line_id: 48
    content: "septon-rowan takes his cloak"
    what: "his cloak" — possessive determiner "his" on a prop. Should be "the cloak."
    why: Same as fault-013.
    criteria: Possessive must be replaced with definite article ("the cloak").

  - id: fault-016
    type: fault
    file: chapter-06.md
    line_id: 49
    content: "septon-rowan opens his door"
    what: "his door" — possessive determiner "his" on a prop. Should be "the door."
    why: Same as fault-013.
    criteria: Possessive must be replaced with definite article ("the door").

  # ── CHECK 5: HOLDS-MODIFIER LICENSE ─────────────────────────────────────────

  # Reviewed all "holds" occurrences:
  # ch01-107: holds the feet — body-part, stillness-against-pressure. LICENSED.
  # ch01-131: holds the spine — body-part of subject, stillness-against-pressure. LICENSED.
  # ch03-8,9,14,18,19,35,39,42: all body-part holds. LICENSED.
  # ch05-8 (ch05 file): septon-rowan interlude — holds the eyes. Body-part. LICENSED.
  # ch05-81,82,83: holds the eyes, holds the eyes, holds the chin. Body-part. LICENSED.
  # ch10-26: holds the chin — body-part. LICENSED.
  # ch10-37: holds the feet — body-part. LICENSED.
  # No "holds the <body-part> <modifier>" (result-state modifier form) found.

  - id: fault-017
    type: pass
    what: holds-modifier license check
    why: All "holds" uses are body-part stillness-against-pressure. No result-state modifier variants found. All licensed.

  # ── CHECK 6: NON-ACTION VERB DENY-LIST (STATIVE, PERCEPTION, COGNITION, COPULA, NEGATION) ──

  # Stative position verbs:
  # ch01-130: "taylor-hebert-westeros kneels" — the act of going to knees (transition to position). The schema example
  # distinguishes "taylor stands at the door" (FAULT) from "taylor stands" (licensed as discrete act of rising).
  # "kneels" is the act of kneeling, not a description of the kneeled position. By the same schema logic, LICENSED
  # as the discrete transition act. However, see ambiguity call AC-04 below for the borderline reasoning.

  # ch05-21 (file chapter-05.md, line 21): "septon-rowan kneels" — same analysis. LICENSED as transition act.

  # ch05-30 (file chapter-05.md, line 30): "taylor-hebert-westeros kneels at the altar" — already caught as fault-006
  # (trailing prep phrase). The bare "kneels" component is licensed; the fault is the appended "at the altar."

  # ch07-88: "taylor-hebert-westeros kneels" — licensed.

  # No `sees`, `hears`, `feels`, `notes`, `watches`, `observes`, `marks` (cognitive), `reads`, `examines`, `scans`,
  # `surveys`, `considers`, `decides`, `realizes`, `understands`, `is/was/are/were/be`, `does not <V>`, `fails to <V>`
  # found in any chapter.

  # ch01-134: "septon-dying-protector marks the scroll" — "marks" here is a concrete physical action (making a mark
  # on parchment with a writing instrument), not the cognitive perception sense. LICENSED.
  # ch02-16,22,27,45,46,47: "oc-plumms-man marks the ledger/entry/description/location/date" — same physical-marking
  # sense. LICENSED throughout.
  # ch04-61,74: "ser-harwick-plumm marks the page / the third rider marks the ledger" — same. LICENSED.

  - id: fault-018
    type: pass
    what: non-action verb deny-list (stative position, perception, cognition, copula, negation)
    why: No instances of banned verb classes found. "marks" throughout is the physical inscription action, not the cognitive perception sense. "kneels" occurrences are transition-acts, not stative position descriptions.

  # ── CHECK 7: MULTI-SUBJECT LINES ────────────────────────────────────────────

  - id: fault-019
    type: pass
    what: multi-subject check
    why: No compound subjects found across all 10 chapters. All proto-lines name a single subject.

  # ── ADDITIONAL FAULTS FOUND (bare motion, bare intransitive, other modifier forms) ──

  - id: fault-020
    type: fault
    file: chapter-06.md
    line_id: 23
    content: "septon-rowan crosses"
    what: Bare intransitive motion verb with no destination and no object. FAULT-FORM-NO-VERB per schema: "Bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB. `taylor moves` is not observable; `taylor enters the yard` is." The intransitive-lands-cleanly exception applies to verbs like `exhales`; it does not extend to motion verbs that imply destination.
    why: "crosses" is a motion verb that implies traversal of a space. Without a destination or object, the observable event is undefined.
    criteria: The proto-line must supply the space or destination as direct object of the motion verb (e.g., "septon-rowan crosses the cottage").

---

## Ambiguity Adjudication — 15 Borderline Cases

These are cases where reasonable readers might split. Each receives a LICENSE or DENY call with binding reason. These calls set the ruleset for the next pipeline pass.

  AC-01:
    file: chapter-01.md
    line_id: 35
    content: "the men-at-arms follow oc-census-officer"
    call: LICENSE
    reason: "follow <entity>" takes the entity as direct object. This is a transitive construction where the named entity is the grammatical object of the verb, not a prepositional complement. The motion implied is governed by the entity being followed, not by a "to/toward/into" phrase. No prepositional phrase is present. The schema's ban targets "follows to X" (see fault-005), not "follows X."

  AC-02:
    file: chapter-01.md
    line_id: 49
    content: "taylor-hebert-westeros approaches the gate"
    call: LICENSE
    reason: "approaches <entity>" is transitive; "the gate" is the direct object. "Approaches" is a motion verb of convergence that idiomatically takes its destination as direct object, not as a prepositional phrase. This is the same pattern as "reaches the doorway" (ch01-5), which is uncontested. LICENSE.

  AC-03:
    file: chapter-01.md
    line_id: 53
    content: "taylor-hebert-westeros retreats"
    call: LICENSE
    reason: "retreats" is intransitive by strong convention; it does not imply a specific destination the way "crosses" or "walks" do. An observer can witness a retreat without knowing the destination. This falls into the intransitive-lands-cleanly exception alongside "exhales" and "stills." LICENSE. If a destination is narratively load-bearing, a separate proto-line should supply it.

  AC-04:
    file: chapter-01.md (also ch03, ch05, ch07)
    line_id: 130 (representative)
    content: "taylor-hebert-westeros kneels"
    call: LICENSE
    reason: The schema distinguishes stative-position-naming (FAULT) from discrete-act-of-transition (LICENSE). "stands at the door" faults because it names a sustained position with location context; "stands" (as the act of rising) licenses. "kneels" names the act of lowering to the knees — a discrete physical transition, not a description of a sustained kneeling position. Applied consistently: bare "kneels" is the transition act and is licensed. A line reading "kneels at the altar" faults only because of the appended prep phrase (fault-006), not because of the verb.

  AC-05:
    file: chapter-01.md
    line_id: 130
    content: "taylor-hebert-westeros holds the spine"
    call: LICENSE
    reason: "the spine" is a body part of the subject. The narrow holds-license explicitly covers "the object is a body part of the subject and the action is stillness-against-pressure." Holding the spine flat/still (against gravity or pain) is the stillness-against-pressure paradigm. LICENSE.

  AC-06:
    file: chapter-02.md
    line_id: 23
    content: "oc-plumms-man turns the head"
    call: LICENSE
    reason: "turns the head" — the head is a body part of the subject; turning the head is a discrete, observable physical action (rotation of the head). This is not the banned "turns to <named entity>" form (no destination entity present). It is also not a stative verb; it names the act of rotating a body part. LICENSE.

  AC-07:
    file: chapter-02.md
    line_id: 68
    content: "taylor-hebert-westeros walks the sept road"
    call: LICENSE
    reason: "walks the sept road" — in established English idiom, "walks a road/path" is transitive; "the sept road" is the direct object naming the path traversed. The schema bans "walks to the yard" (motion verb + destination prep phrase) but licenses "enters the yard" (transitive verb + direct object). "walks the sept road" follows the transitive-verb-takes-path pattern. This parallels "crosses the cottage floor" (ch01-4) and "walks the nave" (ch04-17). LICENSE. Note: this is a borderline set; see AC-08 for the cross-application.

  AC-08:
    file: chapter-04.md
    line_id: 17
    content: "oc-castellan-harrenhal walks the nave"
    call: LICENSE
    reason: Same analysis as AC-07. "walks the nave" is transitive-takes-path. The verb "walks" idiomatically licenses a space as direct object when the space is the surface of traversal (nave, road, yard). This differs from the banned "walks to the nave" (destination prep phrase). LICENSE. Note: the pipeline should treat "walks <space>" as consistently licensed to avoid fixer churn — all such instances across chapters 02 and 04 receive the same ruling.

  AC-09:
    file: chapter-04.md
    line_id: 53
    content: "a raven perches taylor-hebert-westeros"
    call: DENY
    reason: "perches taylor-hebert-westeros" attempts a transitive usage of "perches" where the direct object is a person (the landing surface). Standard usage of "perches" is intransitive or takes the surface as subject ("the raven perches on the arm"). Making Taylor the direct object of "perches" is a semantic inversion that is not observable as stated — a reader cannot parse this without inferring "on." The missing "on" is a suppressed prepositional phrase, not a genuine transitive object. FAULT-FORM-MODIFIER (suppressed prep phrase). Recast: "a raven lands on taylor-hebert-westeros" is also a prep phrase fault; correct form: "the raven lands the arm" (treating the body part as the surface/direct object, as in perching-on-arm idiom) or split into "the raven descends / the raven clamps the arm."

  AC-10:
    file: chapter-06.md
    line_id: 61
    content: "taylor-hebert-westeros presses a fist"
    call: LICENSE
    reason: "presses a fist" — the fist is a body part being pressed (against a surface implied but unstated). Under the narrow holds-license, "presses" is a pressure action on a body part. The surface being pressed against is not stated as a prepositional phrase (no "against the wall" is present). The act of pressing a fist is physically observable. LICENSE. If the surface is narratively load-bearing, a separate location-state citation handles it.

  AC-11:
    file: chapter-07.md
    line_id: 91
    content: "taylor-hebert-westeros crosses the sept door"
    call: DENY
    reason: "crosses the sept door" — a door is not a traversable space; one crosses a floor, yard, or road, not a door. The intended action is passing through a threshold. "Crosses the sept door" as stated is a semantic misfire: the direct object of "crosses" should be a space, not a door. This is not a modifier fault; it is a malformed SVO where the object does not fit the verb's semantics. Recast: "taylor-hebert-westeros passes the sept door" (passes through/beyond the door as direct object) or "taylor-hebert-westeros exits the sept." FAULT-FORM-NON-ACTION-VERB does not apply; the correct classification is that the line fails the observable-event standard — an observer cannot determine what happened.

  AC-12:
    file: chapter-02.md
    line_id: 57
    content: "oc-plumms-man enters the mill hamlet track"
    call: LICENSE
    reason: "enters the mill hamlet track" — a track/road can be entered (stepped onto). This is idiomatic for stepping onto a path. "Enters" is the licensed transitive-takes-destination verb form. "The mill hamlet track" is the direct object (the space entered). LICENSE.

  AC-13:
    file: chapter-01.md
    line_id: 4
    content: "taylor-hebert-westeros crosses the cottage floor"
    call: LICENSE
    reason: "crosses the cottage floor" — "the cottage floor" is the traversable surface as direct object of "crosses." This is the canonical transitive-takes-path pattern. LICENSE. Consistent with AC-07 and AC-08 rulings.

  AC-14:
    file: chapter-05.md (septon-rowan interlude, chapter-05.md file)
    line_id: 26
    content: "septon-rowan takes the Harrenhal road"
    call: LICENSE
    reason: "takes the Harrenhal road" — "takes a road" is an established idiomatic transitive (to take a road = to travel it). "The Harrenhal road" is the direct object. No prepositional phrase present. LICENSE. Consistent with AC-07 treatment of walk-the-road pattern.

  AC-15:
    file: chapter-07.md
    line_id: 75
    content: "taylor-hebert-westeros crosses the sept door"
    call: DENY (same entity, different file-location than AC-11)
    reason: This is ch07-91 re-checked under the chapter-07 numbering. See AC-11 for the ruling. DENY — semantic mismatch between verb and object; "door" is not a space that can be crossed. Recast to "exits the sept" or "passes the sept door."

---

## Summary counts

  total_findings: 20
  faults: 13 (fault-001 through fault-009, fault-011, fault-012, fault-013 through fault-016, fault-020)
  passes: 4 (fault-010, fault-017, fault-018, fault-019)
  flags: 0
  escalations: 0
  ambiguity_calls: 15 (AC-01 through AC-15)
  license_calls: 11 (AC-01, AC-02, AC-03, AC-04, AC-05, AC-06, AC-07, AC-08, AC-10, AC-12, AC-13, AC-14)
  deny_calls: 3 (AC-09, AC-11, AC-15)

## DENY calls converting to faults

  - id: fault-021
    type: fault
    file: chapter-04.md
    line_id: 53
    content: "a raven perches taylor-hebert-westeros"
    what: Suppressed prepositional phrase. "perches <person>" is not a valid transitive construction; the "on" is absent and the line is not parseable as an observable event. See AC-09.
    why: Stitcher cannot render an unambiguous physical beat from this line.
    criteria: Recast as a transitive verb that takes a body part as direct object with no prepositional phrase, or split into two beats (e.g., "the raven descends" / "the raven clamps the arm").

  - id: fault-022
    type: fault
    file: chapter-07.md
    line_id: 91
    content: "taylor-hebert-westeros crosses the sept door"
    what: Semantic mismatch — "crosses" requires a traversable space as direct object; a door is a threshold, not a space. Line does not meet the observable-event standard. See AC-11.
    why: Stitcher cannot determine what physical event occurred.
    criteria: Recast with a verb whose semantics match the object (e.g., "taylor-hebert-westeros passes the sept door" or "taylor-hebert-westeros exits the sept").
