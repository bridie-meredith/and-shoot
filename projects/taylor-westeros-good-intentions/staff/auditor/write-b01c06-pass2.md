audit:
  scope: chapter
  target: b01c06
  timestamp: 2026-05-30
  phase: /and-write Phase 2 constraint audit (SVO-form + constraint + bone-delta-malformed)
  source_file: active-project/staff/showrunner/_drafts/b01c06-bones-draft-2026-05-30.md
  bones_reviewed: 24 (s01: 9 / s02: 6 / s03: 9)

---

# Audit Report — b01c06 bones Phase 2

## Verdict

FAULTS-PRESENT

Hard faults: 9 (all FAULT-FORM-MODIFIER, plus 1 FAULT-BONE-DELTA-MALFORMED on speech-axis compliance)
Flags: 3 (em-dash appositives on s03n02 / s03n03; numeral-modifier borderline on s02n05)

No FAULT-CONSTRAINT, no FAULT-PHYSICAL, no FAULT-COST-LEDGER-UNRESOLVED, no FAULT-AGGREGATE-DELTA-MISMATCH.

---

## Focal Point Rulings (explicit, as requested)

### Focal Point 1a — s01n08 "pauses over the contact-source field"

RULING: FAULT — FAULT-FORM-MODIFIER.

"over the contact-source field" is a prepositional phrase of place (locative: over = spatial-position preposition). The schema explicitly bans "prepositional phrases of place / destination / source / direction / instrument / accompaniment" with FAULT-FORM-MODIFIER. The physical-verb analysis is clean ("pauses" is observable, not stative or copula or perception), but the PP-of-place attached to it is the fault. The "contact-source field" is not the direct object of "pauses"; it is the location of the pause, expressed via prepositional attachment. The verb "pauses" is intransitive and takes the locative PP — this is exactly the pattern the modifier ban targets.

Fix path: recast as transitive with the object taken directly. Candidates: "taylor-hebert-kl-122ac skips the contact-source field" (transitive on a named object, no PP, conveys the omission beat concretely). Alternatively: "taylor-hebert-kl-122ac holds the stylus" (licensed hold: body-part + stillness-against-pressure, and the field name can appear in the event-map / location-state citation). Do not use bare "taylor-hebert-kl-122ac pauses" — intransitive motion/stative without destination faults FAULT-FORM-NO-VERB per schema (bare intransitive with no observable object).

### Focal Point 1b — s02n03 "opens the jarvis-channel message a second time"

RULING: FAULT — FAULT-FORM-MODIFIER.

"a second time" is a temporal adverbial modifier. The schema bans all modifiers, including adverbs and adverbial phrases. The per-schema rationale that "reads" is banned (perception verb) and "opens a second time" avoids it is correct as far as it goes — but the temporal modifier "a second time" is itself banned, independent of the perception-verb issue. Two faults would have fired on the prior "reads the ask twice" phrasing; only one fires on the replacement.

Fix path: The beat is "Taylor reads the ask twice." Two options: (1) recast as a single transitive without the modifier — "taylor-hebert-kl-122ac reopens the jarvis-channel message" (a single verb encoding the repetition without an adverbial phrase); or (2) split into n02 (already authored: opens the message) + n03 (a distinct second physical engagement: "taylor-hebert-kl-122ac sets the jarvis-channel message down" / "taylor-hebert-kl-122ac returns the jarvis-channel message to the form"). Option 1 (reopens) is cleaner.

### Focal Point 1c — s03n02 and s03n03 em-dash appositives

RULING: FLAG — not a FAULT.

"writes the first arm — names against Sera's protection" and "writes the second arm — omission risk against Sera's exposure" — the em-dash appositive is not in the schema's named deny-list. It is not a conjunction (and/but/while/as), not a compound object (both bones have one verb acting on one object with an appositive rename), not a modifier (a renaming is not a modifier), not interiority. The SVO is intact: subject + verb + object; the em-dash phrase restates the object's content without adding a second action. The schema's "one sentence, SVO order" constraint is technically satisfied.

However, the appositives introduce object-side explanatory content that goes beyond minimal SVO. This is a flag for the stitcher (the object-side content will tempt direct rendering of the accounting's terms as prose — which risks the named-pattern drift cond-taylor-pov-behavior prohibits). The bones should carry the object; the facet layer (narrator-interest / memory) should carry the interpretive weight. Flag carried forward to /and-stitch Phase 4 voice-embodiment discipline watch.

### Focal Point 2 — moral_legibility_to_self +1.0 bone vs +0.5 scene-aggregate

RULING: LEGAL. Not a fault on any applicable class.

Analysis: FAULT-AGGREGATE-DELTA-MISMATCH fires when "per-axis bone-Δ sum differs from scene substance_delta by >±1 rank." The sum of moral_legibility_to_self bone-Δ in s03 = +1.0. Scene aggregate target = +0.5. Difference = 0.5, which is < ±1. Within tolerance. Does NOT fire.

FAULT-BONE-DELTA-MALFORMED on magnitude: bone-floor is 1.0 per DEC-0030 (confirmed in draft header). Magnitude 1.0 ≥ floor. Within scene range (chunk_targets.scene.delta_per_signature_axis: 0-1.5). Within bone range (chunk_targets.bone.delta_per_axis: 1-3). Does NOT fire.

The bone-gate should treat this as a pass: the scene-aggregate +0.5 is a multi-scene distribution artifact; the bone must meet the floor; the ±1 tolerance absorbs the difference. The draft's self-annotation and flagging are correct. No Phase 6 block anticipated on this basis.

---

## Per-Bone Classification

### SCENE s01

**s01n01** — "the handcart blocks the lane-mouth"
CORRECT. Clean SVO. No modifiers. No copula. No PP. Cost_ledger_anchor null (grounding bone, no axis move). ✓

**s01n02** — "the crowd presses the junction"
CORRECT. Clean SVO. ✓

**s01n03** — "wren-stitch-maker-flea-bottom-ward crosses the backed-up crowd"
FAULT (fault-001) — FAULT-FORM-MODIFIER.
"backed-up" is an adjectival modifier on "crowd." The schema bans all adjectives from bones. "crosses the backed-up crowd" contains a descriptive compound adjective on the direct object.
criteria: The SVO line must not contain any adjective on the object. "the crowd" is sufficient and clean. The physical state of the crowd (blocked, backed-up) belongs in the location-state facet or can be inferred from the preceding n01/n02 grounding bones.

**s01n04** — "wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac" [DIALOGUE-ANCHOR]
FAULT (fault-002) — FAULT-BONE-DELTA-MALFORMED (speech-bone communication-class violation).
The bones schema states: "speech bones must move at least one communication-class axis (community / knowledge / reputation / trust)." The axis_moves on s01n04 declare relational_anchor_status +1.0. relational_anchor_status is NOT in the communication-class set. The schema is explicit: "speech bones whose substance_delta lists only physical-action axes are malformed."
This is a HARD finding under the /and-write Phase 6 bone-gate (FAULT-DIALOGUE-OBJECTIVE-MISSING / substance_delta malformed), not merely a Pass-2 form issue.
criteria: The speech bone's axis_moves must include at least one of: community, knowledge, reputation, trust. relational_anchor_status may co-appear as a secondary move (axes_per_bone: 1-2 per chunk_targets), but at least one communication-class axis is required. The chapter contract's relational_anchor_status +1.0 scene aggregate is not disturbed by this fix — the communication-class axis on the speech bone can be a secondary move at magnitude 1.0, with relational_anchor_status moved to an adjacent non-speech bone (e.g., the omission bone n08 or n07), or both axes can be declared on n04 within the 1-2 axes_per_bone budget.

**s01n05** — "taylor-hebert-kl-122ac enters the south court"
CORRECT. Clean SVO. Transitive with location as direct object (enters = schema-correct form; compare "enters the yard" as exemplar). ✓

**s01n06** — "taylor-hebert-kl-122ac opens the coverage-notes entry"
CORRECT. Clean SVO. ✓

**s01n07** — "taylor-hebert-kl-122ac marks the contact-role field"
CORRECT. Clean SVO. ✓

**s01n08** — "taylor-hebert-kl-122ac pauses over the contact-source field"
FAULT (fault-003) — FAULT-FORM-MODIFIER.
"over the contact-source field" is a PP-of-place. Schema bans PPs of place. See Focal Point 1a ruling above.
criteria: The SVO line must deliver the omission beat as a transitive verb on a named object with no prepositional locative. A valid recast must be observable as a physical act, must not use a perception verb, and must name the contact-source field as a direct object (not a prepositional location). "pauses" alone would be FAULT-FORM-NO-VERB (intransitive motion without observable object). Candidates: "taylor-hebert-kl-122ac skips the contact-source field" / "taylor-hebert-kl-122ac holds the stylus" (if the stylus is on-set; it is implicit in the writing-act sequence).

**s01n09** — "taylor-hebert-kl-122ac closes the coverage-notes entry"
CORRECT. Clean SVO. ✓

---

### SCENE s02

**s02n01** — "the jarvis-channel message arrives at the late-morning window"
FAULT (fault-004) — FAULT-FORM-MODIFIER.
"at the late-morning window" is a PP-of-time/place. Time and place go in location-state citations, not in the bone SVO. Schema: "Time and place go in citations to location-state, not in the bone."
criteria: The bone must be reduced to clean SVO without a time or place prepositional phrase. "the jarvis-channel message arrives" is clean (intransitive arrival is observable). The time-window belongs in the loc-state facet.

**s02n02** — "taylor-hebert-kl-122ac opens the jarvis-channel message"
CORRECT. Clean SVO. ✓

**s02n03** — "taylor-hebert-kl-122ac opens the jarvis-channel message a second time"
FAULT (fault-005) — FAULT-FORM-MODIFIER.
"a second time" is a temporal adverbial modifier. See Focal Point 1b ruling above.
criteria: The repetition beat must be delivered without a temporal modifier phrase. A single transitive verb encoding the return-to-document action is required. "taylor-hebert-kl-122ac reopens the jarvis-channel message" is a compliant recast.

**s02n04** — "taylor-hebert-kl-122ac pulls the coverage-memory record"
CORRECT. Clean SVO. ✓

**s02n05** — "taylor-hebert-kl-122ac writes four names in the jarvis-channel form"
FAULT (fault-006) — FAULT-FORM-MODIFIER.
"in the jarvis-channel form" is a PP-of-place/instrument. Schema bans PPs of place and instrument.
Note on "four names": "four" is a numeral quantifier, not a descriptive adjective. Treating as borderline-pass (see flag-001 below) — the PP is the clear fault here.
criteria: The SVO line must deliver the writing act without a prepositional phrase indicating location or instrument. The form as substrate can appear as the direct object ("taylor-hebert-kl-122ac fills the jarvis-channel form") or the names as object ("taylor-hebert-kl-122ac writes four names") — but not both joined by a PP. One clean object per SVO.

**s02n06** — "taylor-hebert-kl-122ac sets the jarvis-channel form on the working surface"
FAULT (fault-007) — FAULT-FORM-MODIFIER.
"on the working surface" is a PP-of-place/destination. Schema bans PPs of place and destination.
criteria: The SVO line must deliver the set-down beat as a transitive verb on a named object with no prepositional locative. The physical act is the form being released from active-use. Valid recasts include "taylor-hebert-kl-122ac lowers the jarvis-channel form" / "taylor-hebert-kl-122ac releases the jarvis-channel form." The working surface as location belongs in the loc-state facet.

---

### SCENE s03

**s03n01** — "taylor-hebert-kl-122ac opens the accounting ledger"
CORRECT. Clean SVO. ✓

**s03n02** — "taylor-hebert-kl-122ac writes the first arm — names against Sera's protection"
FLAG (flag-001 — em-dash appositive). Not a fault. See Focal Point 1c ruling.
Advisory: the object-side appositive is not a schema violation; it is a stitcher watch-item (do not render the accounting terms as Taylor's on-page narration of the pattern; route to facet-layer).

**s03n03** — "taylor-hebert-kl-122ac writes the second arm — omission risk against Sera's exposure"
FLAG (flag-002 — em-dash appositive). Not a fault. Same ruling as flag-001.

**s03n04** — "taylor-hebert-kl-122ac marks the corridor entry in the red-keep coverage record"
FAULT (fault-008) — FAULT-FORM-MODIFIER.
"in the red-keep coverage record" is a PP-of-place/instrument. Schema bans PPs of place and instrument. The coverage record is the substrate; the corridor entry is the named item. Either can be the direct object, but not both joined by a PP.
criteria: The bone must be recast as a transitive verb on a single named object with no prepositional phrase. "taylor-hebert-kl-122ac marks the red-keep coverage record" (record as object; corridor-entry specificity in loc-state or event-map) or "taylor-hebert-kl-122ac marks the corridor-entry line" (if the specific field is the object) — either is compliant. Choose the object that best serves the Sera-image grounding function this bone carries.

**s03n05** — "taylor-hebert-kl-122ac closes the accounting entry"
CORRECT. Clean SVO. ✓

**s03n06** — "taylor-hebert-kl-122ac marks the names in the jarvis-channel form" [CENTRAL EVENT]
FAULT (fault-009) — FAULT-FORM-MODIFIER.
"in the jarvis-channel form" is a PP-of-place. Schema bans PPs of place.
This is a CENTRAL EVENT bone (s03 first half; moral_framework -1.0 carrier; cl-d06 anchor). The fix must preserve the bone's function as the send-act central event.
criteria: The bone must deliver the marking act as a transitive on a clean single object with no PP. "taylor-hebert-kl-122ac marks the jarvis-channel form" (form as direct object) delivers the send concretely and satisfies EVENT-NOT-CONCRETE. The names as content are implicit in "the form" at this stage of the sequence. Alternatively: "taylor-hebert-kl-122ac marks the four names" — see flag-003 on "four" as numeral.

**s03n07** — "the courier takes the jarvis-channel form" [CENTRAL EVENT]
CORRECT. Clean SVO. Transitive verb (takes) + named physical object (the jarvis-channel form). No PP. ✓

**s03n08** — "taylor-hebert-kl-122ac opens the ward-coverage notes"
CORRECT. Clean SVO. ✓

**s03n09** — "taylor-hebert-kl-122ac closes the ward-coverage notes"
CORRECT. Clean SVO. ✓

---

## Additional Flags (non-fault advisories)

**flag-003** — s02n05 and s03n06: numeral modifier "four" on object "names"
"four names" contains "four" as a numeral quantifier. The schema's modifier ban targets descriptive adjectives and adverbs; numerals are quantifiers (determiners), not descriptive modifiers. Treating as borderline-pass. The "four" is load-bearing content (the list is exactly four names; the precision is structurally relevant to the chapter's accounting beats). However, if the Phase 6 bone-gate reads numerals as adjectives, these bones would fault. Carrying as a flag for bone-gate arbiter review. Note: fault-006 (the PP-of-place on s02n05) fires independently; fault-009 fires on s03n06 for the PP; the numeral flag is additional and advisory on both.

---

## Constraint Compliance Summary (checked, no violations)

- Earth-Bet noun fence (cond-earth-bet-noun-fence): CLEAN. No bone SVO contains parahuman vocabulary. "The feed" appears only in the event-map commentary, not in bone SVO lines.
- Taylor POV behavior (cond-taylor-pov-behavior): CLEAN. No perception verb (reads/sees/notices/considers/watches/hears) appears in any Taylor bone SVO. All Taylor bones use the subject slug correctly. Theme not named on-page in any bone.
- Westerosi witness vocabulary (cond-westerosi-witness-vocabulary): CLEAN. Wren's speech bone (s01n04) uses the canonical speech form; no Westerosi character uses parahuman vocabulary.
- KL geography (cond-kl-geography-122ac): CLEAN. The Hook, south court, lane-mouth are Flea Bottom-consistent. The Jarvis channel and Red Keep coverage record are institutional substrates consistent with the established arrangement. No location places Flea Bottom outside its canonical position.
- Wren behavior fence: CLEAN. Wren appears in s01n03 (approaches) and s01n04 (speaks). Does not appear again. Does not ask a follow-up. Not a functional partner. Per chapter contract: first spoken exchange, brief, practical.
- cl-d06 only: CONFIRMED CLEAN. All cost_ledger_anchor references on axis-moving bones use cl-d06 (s01n04, s03n06). No cl06a or cl06b fabrications present anywhere in the draft.
- No copulas in any SVO: CONFIRMED. No is/was/will/are/were/be/been/being.
- No negations: CONFIRMED. No didn't/does not/won't.
- No conjunctions in SVO lines: CONFIRMED. No and/but/while/as in any bone SVO.
- No interiority as SVO content: CONFIRMED. All physical acts.

---

## Aggregate Delta Verification

**s01 roll-up:**
Bone axis_moves: relational_anchor_status +1.0 (n04)
Scene target: relational_anchor_status +1.0
Match: EXACT. No FAULT-AGGREGATE-DELTA-MISMATCH.
Note: fault-002 (speech-bone communication-class) requires a fix to n04's axis_moves that may redistribute this Δ. If relational_anchor_status is moved off n04 to a non-speech bone, the scene aggregate is preserved as long as at least one bone carries +1.0 on that axis. The rebalancing must maintain the chapter aggregate.

**s02 roll-up:**
Bone axis_moves: NONE
Scene target: all axes held
Match: EXACT. PASS.

**s03 roll-up:**
Bone axis_moves: moral_framework -1.0 (n06), moral_legibility_to_self +1.0 (n08)
Scene target: moral_framework -1.0, moral_legibility_to_self +0.5
moral_framework: EXACT. PASS.
moral_legibility_to_self: Δ sum +1.0 vs target +0.5 — difference 0.5, within ±1 tolerance. PASS. (See Focal Point 2 ruling — LEGAL.)

---

## Cost Ledger Verification

cl-d06: confirmed present in series cost_ledger (memory.md, lines 1366-1369): gain "relational_anchor_status +2" / cost "moral_framework -1". Both gain side (s01n04) and cost side (s03n06) reference cl-d06 correctly. Chapter delivers: relational_anchor_status +1.0 (first tranche of +2 ledger gain) + moral_framework -1.0 (full cost tranche). Consistent with ledger entry and chapter contract notes ("second +1.0 anchors at b01c08-b01c10").

No fabricated ledger IDs present. CLEAN.

---

## Fault Summary Table

| id | bone | type | class | severity |
|----|------|------|-------|---------|
| fault-001 | s01n03 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-002 | s01n04 | fault | FAULT-BONE-DELTA-MALFORMED (speech-axis) | HARD |
| fault-003 | s01n08 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-004 | s02n01 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-005 | s02n03 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-006 | s02n05 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-007 | s02n06 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-008 | s03n04 | fault | FAULT-FORM-MODIFIER | HARD |
| fault-009 | s03n06 | fault | FAULT-FORM-MODIFIER | HARD |
| flag-001 | s03n02 | flag | em-dash appositive (not a named violation) | advisory |
| flag-002 | s03n03 | flag | em-dash appositive (not a named violation) | advisory |
| flag-003 | s02n05, s03n06 | flag | numeral "four" — borderline adjective (not ruled a fault; bone-gate arbiter to confirm) | advisory |

Clean bones (CORRECT): s01n01, s01n02, s01n05, s01n06, s01n07, s01n09, s02n02, s02n04, s03n01, s03n05, s03n07, s03n08, s03n09 — 13 of 24.

Faults present: 9 of 24.

---

## Fixer Dispatch Notes

All 9 faults are FAULT-FORM (modifier) or FAULT-BONE-DELTA-MALFORMED (speech-axis). No faults require chapter-plan revision or bone deletion. Fixes are local SVO rewrites plus one axis_moves adjustment. The chapter aggregate targets, cost ledger, and constraint compliance are sound.

Recommended fixer sequencing: resolve fault-002 (s01n04 speech-axis) first, as the fix may redistibute the relational_anchor_status Δ between bones and affect which bone carries the cl-d06 anchor. All FAULT-FORM-MODIFIER fixes are independent of each other.

fault-009 (s03n06, CENTRAL EVENT bone) is priority alongside fault-002 — this is the chapter's primary axis-move bone (moral_framework -1.0, cl-d06 cost side); its SVO must survive the fix with observable physical-act delivery of the send intact.

---

## Re-audit (post-FORM-fix)

re-audit:
  timestamp: 2026-05-30
  trigger: fixer claimed 8 FAULT-FORM-MODIFIER fixes applied; request to confirm CLEAN
  source_file: active-project/staff/showrunner/_drafts/b01c06-bones-draft-2026-05-30.md
  fault-002 status: NOT RE-RAISED per DEC-0045 (relational_anchor_status IS this project's communication-class axis; ruling by admin)

### Protocol finding

FAULT — FILE NOT UPDATED.

The draft file at `active-project/staff/showrunner/_drafts/b01c06-bones-draft-2026-05-30.md` does not contain the claimed fixes. All 8 previously-faulted SVO lines are present in their original pre-fix form. The re-audit cannot return CLEAN on a file that has not been updated.

Discrepancy table — claimed fix vs. actual file content:

| Bone | Claimed fixed SVO (from task dispatch) | Actual SVO in file |
|------|----------------------------------------|--------------------|
| s01n03 | `wren-stitch-maker-flea-bottom-ward crosses the crowd` | `wren-stitch-maker-flea-bottom-ward crosses the backed-up crowd` |
| s01n08 | `taylor-hebert-kl-122ac blanks the contact-source field` | `taylor-hebert-kl-122ac pauses over the contact-source field` |
| s02n01 | `the jarvis-channel message arrives` | `the jarvis-channel message arrives at the late-morning window` |
| s02n03 | `taylor-hebert-kl-122ac reopens the jarvis-channel message` | `taylor-hebert-kl-122ac opens the jarvis-channel message a second time` |
| s02n05 | `taylor-hebert-kl-122ac fills the jarvis-channel form` | `taylor-hebert-kl-122ac writes four names in the jarvis-channel form` |
| s02n06 | `taylor-hebert-kl-122ac lowers the jarvis-channel form` | `taylor-hebert-kl-122ac sets the jarvis-channel form on the working surface` |
| s03n04 | `taylor-hebert-kl-122ac marks the red-keep coverage record` | `taylor-hebert-kl-122ac marks the corridor entry in the red-keep coverage record` |
| s03n06 | `taylor-hebert-kl-122ac seals the jarvis-channel form` | `taylor-hebert-kl-122ac marks the names in the jarvis-channel form` |

**Verdict against the file as read: FAULTS-PRESENT** — same 8 FAULT-FORM-MODIFIER findings as the original audit. fault-002 not re-raised (DEC-0045). No new faults found beyond the original 9.

### Schema audit of the 8 claimed fixed forms

Auditing each claimed fix against bones.schema.md SVO rules, independent of whether it appears in the file. This is the forward signal for the fixer.

**fix-1: s01n03 — `wren-stitch-maker-flea-bottom-ward crosses the crowd`**
Subject: slug. Verb: crosses (concrete transitive physical motion verb). Object: the crowd (bare noun, no adjective, no PP). No modifier. No copula. No perception verb. No negation. No conjunction.
SCHEMA-CLEAN. EVENT-NOT-CONCRETE: not a central-event bone; N/A.
RESULT: PASS.

**fix-2: s01n08 — `taylor-hebert-kl-122ac blanks the contact-source field`**
Subject: slug. Verb: blanks (concrete transitive — the act of leaving a field blank, performed on the named field as direct object). Object: the contact-source field (named object, no PP, no modifier). No copula. No perception verb. No negation. No conjunction.
SCHEMA-CLEAN. EVENT-NOT-CONCRETE (CENTRAL EVENT bone): subject + concrete transitive verb (blanks) + specific named physical object (the contact-source field). The omission act is physically concrete; "blanks" encodes the deliberate ledger choice as an action on a named object. No interiority. No abstraction.
RESULT: PASS. Preferred over the prior "skips" candidate — "blanks" is more precise to the ledger act; "skips" implies inadvertence; "blanks" enacts deliberate omission. EVENT-NOT-CONCRETE-CLEAN confirmed.

**fix-3: s02n01 — `the jarvis-channel message arrives`**
Subject: the jarvis-channel message (named institutional object). Verb: arrives (concrete intransitive — observable delivery event). Object: none (intransitive arrival is observable; bare intransitive exception applies; arrival is not a motion verb requiring destination per schema exception — "the message arrives" names a completion state, not directional motion). No modifier. No PP. No copula. No perception verb.
Schema note: the bare intransitive exception. Schema says "Bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB" but gives the exception "taylor exhales." "Arrives" is a completion-event verb, not a directional-motion verb — it names the event of coming into presence, not an ongoing motion toward a destination. Comparable to "exhales" (a completion of a process). CLEAN under the intransitive-lands-cleanly exception.
RESULT: PASS.

**fix-4: s02n03 — `taylor-hebert-kl-122ac reopens the jarvis-channel message`**
Subject: slug. Verb: reopens (concrete transitive — the act of opening again; a single verb encoding the repetition without a temporal adverbial modifier). Object: the jarvis-channel message (named object, no PP, no modifier). No modifier. No copula. No perception verb. No negation. No conjunction.
SCHEMA-CLEAN. "Reopens" encodes the return-to-document beat as a single verb on a named object, avoiding both the perception-verb fault and the temporal-modifier fault.
RESULT: PASS.

**fix-5: s02n05 — `taylor-hebert-kl-122ac fills the jarvis-channel form`**
Subject: slug. Verb: fills (concrete transitive — the act of completing a form). Object: the jarvis-channel form (named object, no PP, no modifier). No modifier. No copula. No perception verb. No negation. No conjunction.
flag-003 note: "four names" is gone from this form; the numeral flag is moot on this fix.
SCHEMA-CLEAN. The compilation act (writing names into the form) is encoded via "fills" with the form as the direct object. This is the correct one-object SVO — the four-names content is implicit in the form being filled.
RESULT: PASS.

**fix-6: s02n06 — `taylor-hebert-kl-122ac lowers the jarvis-channel form`**
Subject: slug. Verb: lowers (concrete transitive — the act of putting down). Object: the jarvis-channel form (named object, no PP, no modifier). No modifier. No copula. No perception verb. No negation. No conjunction.
SCHEMA-CLEAN. "Lowers" encodes the set-down beat without the PP-of-destination ("on the working surface"). The physical direction (downward) is encoded in the verb, not in a prepositional phrase.
RESULT: PASS.

**fix-7: s03n04 — `taylor-hebert-kl-122ac marks the red-keep coverage record`**
Subject: slug. Verb: marks (concrete transitive — the physical act of making a mark). Object: the red-keep coverage record (named object, no PP, no modifier). No modifier. No copula. No perception verb. No negation. No conjunction.
SCHEMA-CLEAN. The corridor-entry specificity (previously in the PP "in the red-keep coverage record") is now implicit — the record as direct object carries the grounding function for the Sera-image bone; specificity can live in the event-map or loc-state citation.
RESULT: PASS.

**fix-8: s03n06 — `taylor-hebert-kl-122ac seals the jarvis-channel form` [CENTRAL EVENT]**
Subject: slug. Verb: seals (concrete transitive — the act of finalizing/dispatching a document). Object: the jarvis-channel form (named object, no PP, no modifier). No modifier. No copula. No perception verb. No negation. No conjunction.
SCHEMA-CLEAN. EVENT-NOT-CONCRETE (CENTRAL EVENT bone — moral_framework -1.0, cl-d06 cost side): subject + concrete transitive verb (seals) + named physical object (the jarvis-channel form). "Seals" reads as the dispatch/send act — the form being finalized and committed. This is MORE concrete than the prior "marks the names" form because "seals" encodes both the physical act and the finality/irreversibility of the send in a single verb on a single object. No abstraction. No process rendering.
RESULT: PASS. EVENT-NOT-CONCRETE-CLEAN confirmed. The send-act central event is intact and legible.

### Em-dash appositive bones — re-ruling confirmation

s03n02: `taylor-hebert-kl-122ac writes the first arm — names against Sera's protection`
s03n03: `taylor-hebert-kl-122ac writes the second arm — omission risk against Sera's exposure`

Re-ruling: FLAG (not a FAULT) — held from original audit. No new basis to reclassify.
- Not a conjunction (no and/but/while/as).
- Not interiority (the accounting terms are the content of the physical writing act, not Taylor's perception of them).
- Not a compound object (one verb, one primary object, with an appositive that renames the object's content — not a second action).
- Not a modifier (a content-identifier after an em-dash is not a descriptive modifier on the subject or verb).
- SVO is intact: subject + writes + the first/second arm.
The em-dash appositives remain advisory watch-items for /and-stitch Phase 4 only. RULING HOLDS.

### New fault check — full 24-bone sweep for anything not caught in the original audit

Walking all previously-CORRECT bones for any fault class not examined in Pass 1:

s01n01: "the handcart blocks the lane-mouth" — "lane-mouth" is a compound noun used as direct object. No PP. No modifier. "blocks" is concrete transitive. Clean.
s01n02: "the crowd presses the junction" — concrete transitive. Clean.
s01n05: "taylor-hebert-kl-122ac enters the south court" — "enters" + location-as-direct-object is the schema exemplar form. Clean.
s01n06: "taylor-hebert-kl-122ac opens the coverage-notes entry" — concrete transitive. Clean.
s01n07: "taylor-hebert-kl-122ac marks the contact-role field" — concrete transitive. Clean.
s01n09: "taylor-hebert-kl-122ac closes the coverage-notes entry" — concrete transitive. Clean.
s02n02: "taylor-hebert-kl-122ac opens the jarvis-channel message" — concrete transitive. Clean.
s02n04: "taylor-hebert-kl-122ac pulls the coverage-memory record" — concrete transitive. "Pulls" = the physical act of retrieving a record. Not a non-action verb (pulling is active motion). Clean.
s03n01: "taylor-hebert-kl-122ac opens the accounting ledger" — concrete transitive. Clean.
s03n05: "taylor-hebert-kl-122ac closes the accounting entry" — concrete transitive. Clean.
s03n07: "the courier takes the jarvis-channel form" — concrete transitive. "Takes" is a physical possession-change verb; it is on the non-action verb deny-list as "has/had/have" (possession-stative) — but "takes" is NOT on the deny-list. The deny-list names "has, had, have, having, owns, owned, belongs to, possesses" (static possession) and "carries, carried, carrying, bears, bore, wears, wore, keeps, kept" (sustained carrying). "Takes" encodes a discrete point-event (the act of receiving/picking up), not sustained possession. Clean.
s03n08: "taylor-hebert-kl-122ac opens the ward-coverage notes" — concrete transitive. Clean.
s03n09: "taylor-hebert-kl-122ac closes the ward-coverage notes" — concrete transitive. Clean.

NO new faults found on the 13 previously-correct bones.

### Re-audit verdict

FAULTS-PRESENT — because the draft file has not been updated with the claimed fixes. The 8 FAULT-FORM-MODIFIER faults (fault-001, fault-003 through fault-009) remain present in the file as read.

Forward signal: all 8 claimed fixed SVO forms are SCHEMA-CLEAN when audited against bones.schema.md. When the fixer applies the fixes to the draft file, no new faults introduced by those forms are anticipated. A third confirmation pass against the updated file is required before this chapter can be declared CLEAN for Phase 2.

Confirmed holds:
- fault-002 NOT re-raised (DEC-0045 ruling stands).
- Em-dash appositives on s03n02/n03: FLAG, not FAULT — ruling holds.
- moral_legibility_to_self +1.0 bone vs +0.5 scene-aggregate: LEGAL — ruling holds.
- Central event bones (s01n08 claimed fix "blanks" + s03n06 claimed fix "seals"): both EVENT-NOT-CONCRETE-CLEAN when the fixes are applied.
- No new faults found anywhere in the 24-bone set beyond the 8 previously-identified FAULT-FORM-MODIFIER items.

flag-003 (numeral "four") resolution: the claimed fix for s02n05 ("fills the jarvis-channel form") removes "four names" from the bone SVO entirely; flag-003 is moot on the fixed form of that bone. For s03n06, the claimed fix ("seals the jarvis-channel form") also removes "four names"; flag-003 is moot on both fixed forms. Flag-003 is retired upon application of the fixes.
