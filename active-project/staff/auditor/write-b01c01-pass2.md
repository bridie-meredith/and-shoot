# write-b01c01-pass2 audit report
phase: /and-write b01c01 Phase 2 constraint audit
date: 2026-05-25
auditor: auditor
artifact_audited: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md

summary:
  total_bones: 27
  correct: 14
  faults: 13
  fault_breakdown:
    FAULT-FORM: 12
    FAULT-CONSTRAINT: 0
    FAULT-PHYSICAL: 0
    FAULT-BONE-DELTA-MALFORMED: 0
    FAULT-AGGREGATE-DELTA-MISMATCH: 0
    FAULT-COST-LEDGER-UNRESOLVED: 0
    FAULT-CAST-SLUG: 1

---

faults:

  # --- SCENE 1 ---

  - bone: b01c01s01n01
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — No modifiers: 'Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned.' 'under the angle' is a prepositional phrase of place/direction."
    quote: "the drain water threads under the angle"
    priority: normal
    recast_hint: "the drain water threads the angle-gap" — takes the location as direct object of a transitive reading of 'threads'

  - bone: b01c01s01n02
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — 'from the stitch-house' is a prepositional phrase of source, explicitly banned."
    quote: "the tallow smoke drifts from the stitch-house"
    priority: normal
    note: "This is a sensory-grounding bone resolving pl-002 SOFT. The recast must preserve the stitch-house as a concrete named entity — the anchor plant is load-bearing."
    recast_hint: "the tallow smoke crosses the stitch-house lane" — transitive reading places stitch-house as direct object

  - bone: b01c01s01n04
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — 'at the edge of range' is a prepositional phrase of place. Schema: 'Time and place go in citations to location-state, not in the bone.'"
    quote: "the insects propagate at the edge of range"
    priority: normal
    recast_hint: "the insects propagate" — the range-threshold context is facet material; the bare intransitive is acceptable here since propagate is a physical process verb, not a motion verb implying destination (compare: 'the gap propagates outward' — same intransitive form, addressed separately at s02n08)

  - bone: b01c01s01n05
    class: FAULT-FORM-PERCEPTION
    rule: "schemas/bones.schema.md § field rules — 'No perception verbs. ... sees, hears, notices are POV-leaks.' 'lifts the eyes' is a perception-adjacent surrogate: lifting eyes toward a target is the mechanism of the perception act (scanning), not a discrete physical action separable from the POV-leak. The bone's event_map entry names it 'ward read only at surfaces — bodies moving, foot traffic, smell' — confirming the bone carries a reading/scanning event, which is perception."
    quote: "taylor lifts the eyes"
    priority: normal
    note: "Disambiguation note: 'lifts the eyes' is not on the explicit deny list. The auditor classification rests on the combination of (a) the bone's stated function in the event_map ('ward read only at surfaces') which is observational/perceptual rather than a physical act, and (b) the semantic content: eye-lifting to scan is the mechanism of the perception act, making this a perception-verb surrogate. The deny-list entry 'watches' would fault clearly; 'lifts the eyes' faults because the object 'the eyes' makes the scanning-act the bone's semantic payload. If the bone's function were non-perceptual — e.g., Taylor lifting her eyes as a posture signal visible to another actor — it would pass. In a solo scene with no other person to observe the gesture, it cannot carry that load."
    recast_hint: "taylor scans the alley" would re-introduce perception; better: drop this bone and move the ward-read to narrator-interest facet citing a grounding bone. Or: recast to the physical posture that is observable and not perceptual — but in a solo scene, no such recast is available. Recommend: fold the political_register-prot-held rationale into another bone's axes_held (e.g., s01n07) and drop s01n05, or recast to an action that places Taylor in an observational posture visibly (e.g., 'taylor straightens against the angle-wall' — posture-act with ward-register-held rationale).

  - bone: b01c01s01n06
    class: FAULT-FORM-INTERIORITY
    rule: "schemas/bones.schema.md § field rules — 'Abstraction-as-object is INTERIORITY. A physical verb whose object is an abstract noun ... is a thought-figure, not an event.' 'the angle-wall' could be read as concrete, but 'press' is not the correct physics here: cobbles do not exert pressure against a wall as a discrete observable event. The bone's substance rationale confirms interiority: 'the physical geometry of the drain angle is what anonymity looks like' — the bone is carrying an abstracted conceptual observation (what anonymity looks like) through an ostensibly physical SVO. The event is not observable; it is a thought-figure dressed as environment-action."
    quote: "the cobbles press the angle-wall"
    priority: normal
    note: "This is a borderline fault. 'Cobbles press the angle-wall' could be defended as literal physical description of tight-fit masonry geometry. The fault classification holds because (a) cobbles pressing a wall is a static condition, not a discrete observable act, and (b) the event_map and rationale confirm the bone's function is conceptual-location-naming ('the geometry of the drain angle'), not an event. Stative physical conditions route to location-state facet, not bones."
    recast_hint: "the angle-wall narrows the lane" — subject is the wall, verb is transitive and describes a physical geometry-fact as an action; or drop and route to loc-state facet

  - bone: b01c01s02n02
    class: FAULT-FORM-NON-ACTION-VERB
    rule: "schemas/bones.schema.md § field rules — 'Sustained carrying: carries, carried, carrying, bears, bore, wears, wore, keeps, kept' — explicit deny list entry. 'carries' is on the list."
    quote: "the ground carries the child's breath"
    priority: normal
    note: "Additionally, 'the child's breath' is borderline abstraction-as-object (breath transmitted through ground is a physical fact, but the transmission mechanism is the insect-sense, not a literal event of ground carrying). The FAULT-FORM-NON-ACTION-VERB is sufficient; FAULT-FORM-INTERIORITY is not separately cited since the primary fault is the banned verb."
    recast_hint: "the ground transmits the child's breath" — 'transmits' is not on the deny list and is a discrete directional action; or: "the child's breath reaches taylor through the cobbles" — but this has 'through' as a prepositional phrase of instrument (FAULT-FORM-MODIFIER). Cleanest: "the child's breath surfaces through the lane" or recast entirely to environment-as-subject: "the cobbles carry the fever-read" — but 'carry' is also banned. Best: "the lane floor delivers the child's fever" — concrete, transitive, not on deny list.

  - bone: b01c01s02n06
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — 'inward' is an adverb of direction. 'No modifiers. No adjectives, no adverbs, no prepositional padding.' Adverbs are explicitly banned."
    quote: "the insects propagate inward"
    priority: HIGH — this is the chapter's primary moving bone (capability +1, cl01a anchor); a fault here blocks the substance movement. Recast must preserve the deployment semantics and the cost-ledger anchor.
    recast_hint: "the insects propagate" — the direction (inward, into the crowd) is context supplied by the scene; the bone records the deployment event. Bare intransitive is acceptable for a physical-process verb with no destination implied (propagate ≠ motion verb with implied destination). Alternatively: "the insects propagate the crowd-gap" — transitive, taking the structural result as direct object.

  - bone: b01c01s02n08
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — 'outward' is an adverb of direction. Same rule as s02n06."
    quote: "the gap propagates outward"
    priority: normal
    recast_hint: "the gap propagates" — same bare-intransitive logic as s02n06 recast

  - bone: b01c01s02n11
    class: FAULT-FORM-INTERIORITY
    rule: "schemas/bones.schema.md § field rules — 'Abstraction-as-object is INTERIORITY.' 'the instruction' is an abstract noun (a piece of communication content, not a physical object). 'gives the instruction' is a transfer-of-abstraction, not a transfer-of-physical-object."
    quote: "taylor gives the instruction"
    priority: normal
    note: "Secondary fault candidate: 'gives' in the transfer-of-communication sense routes through the speech-bone form per schema: 'For dialogue beats, the bone shape is: <speaker-slug> speaks to <listener-slug-or-group>.' A vocal act whose content matters should be a dialogue bone; a vocal act whose physical fact (sound projected at the crowd) is what the scene records should be recast to the physical action. Since this chapter has no dialogue file requirement (no direct speech content), the bone must be recast as a physical act, not an abstraction-transfer."
    recast_hint: "taylor projects the voice" — 'projects' is transitive and concrete; 'the voice' is a physical thing (the vocal output), not the content. Alternative: "taylor raises the voice" — same form; carries physical-act semantics.

  - bone: b01c01s03n02
    class: FAULT-FORM-PERCEPTION
    rule: "schemas/bones.schema.md § field rules — 'watches' is on the explicit perception-verb deny list."
    quote: "the man with the fish-cart watches taylor"
    priority: normal
    note: "Additionally, 'the man with the fish-cart' carries a prepositional modifier in the subject-identifier ('with the fish-cart'). The schema states 'Subject is a named entity — actor slug, prop slug, or the <noun> for unnamed environment elements.' 'The man' is the entity; 'with the fish-cart' is a disambiguating modifier. The schema bans modifiers in the SVO bone but the subject-identifier form 'the <noun>' conventionally may need disambiguation for unnamed crowd members. This is a judgment call — the subject-modifier ban is primarily aimed at the VERB and OBJECT positions. The FAULT-FORM-PERCEPTION on 'watches' is the primary fault. The subject-prepositional-modifier is flagged as a secondary concern but not separately classified as a fault: the schema's 'no modifiers' rule applies to the bone's VERB and OBJECT by explicit formulation ('No adjectives, no adverbs, no prepositional padding'); the subject-identifier convention ('the <noun>') does not have an explicit ban on disambiguating prepositional tags. This auditor declines to extend the modifier ban to subject-identification tags without explicit schema authority. Subject-modifier: NOT FAULTED."
    recast_hint: "the fish-cart holder turns toward taylor" — uses the identifying prop as the subject-anchor; 'turns toward' is not the banned 'turns to <X>' form (see schema exception for posture-toward that does not use the prep-phrase form... actually: 'turns toward' is prepositional. Cleaner: "the fish-cart man faces taylor" — 'faces' is licensed as a transitive posture-act per the schema's own SVO trap review. Or: a new slug for this crowd figure if he recurs.

  - bone: b01c01s03n03
    class: FAULT-FORM-NON-ACTION-VERB
    rule: "schemas/bones.schema.md § field rules — 'Stative position-naming: lies, sits, stands describing position not posture-act ... faults.' 'stay' is a stative position-naming verb in the same category — it names continued occupancy of a position, not a discrete act. The schema's deny list is explicitly non-exhaustive ('Non-exhaustive deny-list'). 'stay' is stative, not the discrete act of arriving at or departing from a position."
    quote: "the two women from the upper alley stay"
    priority: normal
    note: "Same subject-prepositional-modifier question as s03n02 applies to 'from the upper alley'. Same ruling: subject-disambiguating tag not separately faulted. The primary fault is the stative verb."
    recast_hint: "the two women face the lane" — 'faces' as transitive posture-act; preserves the witnesss-remaining-in-position semantic without stative naming. Alternatively: "the two women hold the lane-mouth" — but 'hold' is outside the narrow license (body-part-stillness-against-pressure only). Best: "the two women plant at the lane-mouth" if 'plant' reads as a discrete act of taking-position.

  - bone: b01c01s03n04
    class: FAULT-FORM-NON-ACTION-VERB
    rule: "schemas/bones.schema.md § field rules — 'stands describing position not posture-act (taylor stands at the door faults; taylor stands as the discrete act of rising from sitting passes).' Here: 'oswyn-mudway-flea-bottom-elder stands at the lane-mouth' describes Oswyn's occupied position at the lane-mouth, not the discrete act of rising from sitting. The prepositional 'at the lane-mouth' confirms this is position-naming, not posture-act. FAULT-FORM-MODIFIER also applies: 'at the lane-mouth' is a prepositional phrase of place."
    quote: "oswyn-mudway-flea-bottom-elder stands at the lane-mouth"
    priority: HIGH — this is the chapter's primary s03 moving bone (social_tether-prot-rise +1, cl01b anchor). A fault here blocks the chapter's second substance movement. The recast must carry the moving axis.
    note: "Two faults apply to this bone: FAULT-FORM-NON-ACTION-VERB ('stands' as stative position-naming) and FAULT-FORM-MODIFIER ('at the lane-mouth' as prepositional phrase of place). Primary classification is FAULT-FORM-NON-ACTION-VERB since it is the more fundamental fault. The recast must be transitive or a discrete posture-act to clear both."
    recast_hint: "oswyn-mudway-flea-bottom-elder takes the lane-mouth" — transitive discrete act, takes the location as direct object; reads as deliberate positioning. The substance_delta (social_tether-prot-rise +1, cl01b) carries over unchanged.

  - bone: b01c01s03n05
    class: FAULT-FORM-NO-VERB
    rule: "schemas/bones.schema.md § field rules — 'Bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB. taylor moves is not observable; taylor enters the yard is. The intransitive-lands-cleanly exception (taylor exhales) does not extend to motion verbs that imply destination.' 'departs' is a motion verb that implies destination; the child goes somewhere after departing the scene."
    quote: "the child departs"
    priority: normal
    recast_hint: "the child leaves the lane" — transitive with destination as direct object. Or: "the child clears the lane" — transitive; lane as direct object; implies departure and frees the scene without stating where the child goes.

  - bone: b01c01s03n08
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — 'at the lane-level' is a prepositional phrase of place, explicitly banned."
    quote: "the tallow smoke settles at the lane-level"
    priority: normal
    note: "Load-bearing for pl-002 SOFT resolution (stitch-house sensory plant). The recast must preserve the stitch-house reference concretely — the plant is the continuity of the smoke as a locating signal."
    recast_hint: "the tallow smoke settles the lane" — transitive reading; 'settles the lane' carries the grounding-at-this-level semantic without the prepositional place-marker. Or: "the tallow smoke layers the lane-floor" — transitive, concrete.

---

# BONES PASSING ALL CHECKS (14)

  b01c01s01n03  CORRECT — 'taylor holds the feet': `holds` licensed (body-part + stillness-against-pressure against the insect-range pull). substance_delta well-formed (held: capability, moral_framework; 0 moving; no cost_ledger_anchor; 2 axes_held ≤ limit). No modifier, no negation, no copula, no conjunction. SVO clean.

  b01c01s01n07  CORRECT — 'taylor exhales': intransitive-lands-cleanly exception applies explicitly per schema. substance_delta well-formed (held: moral_legibility_to_self, moral_framework). SVO clean.

  b01c01s02n01  CORRECT — 'the fish-cart blocks the lane crosswise': 'crosswise' is an adverb. FAULT-FORM-MODIFIER candidate. However: 'crosswise' here modifies the manner in which the blocking occurs and is embedded in common usage as a compound-action descriptor ('blocks crosswise' = positions at right angles). The schema ban targets 'prepositional phrases of place / destination / source / direction / instrument / accompaniment' and adverbs more broadly. 'Crosswise' is an adverb of manner, not of place or direction, and is not a prepositional phrase. Schema says 'No adverbs' without qualifier. FAULT confirmed on plain text of the rule. Reclassifying:

  b01c01s02n01
    class: FAULT-FORM-MODIFIER
    rule: "schemas/bones.schema.md § field rules — 'No modifiers. No adjectives, no adverbs, no prepositional padding.' 'crosswise' is an adverb."
    quote: "the fish-cart blocks the lane crosswise"
    priority: low
    recast_hint: "the fish-cart blocks the lane" — the lane is direct object; the crosswise geometry is implied by a cart blocking a lane and can be carried in loc-state facet

---

# CORRECTION — revised CORRECT/FAULT count after reclassifying s02n01:

summary (corrected):
  total_bones: 27
  correct: 13
  faults: 14
  fault_breakdown:
    FAULT-FORM: 13
    FAULT-CONSTRAINT: 0
    FAULT-PHYSICAL: 0
    FAULT-BONE-DELTA-MALFORMED: 0
    FAULT-AGGREGATE-DELTA-MISMATCH: 0
    FAULT-COST-LEDGER-UNRESOLVED: 0
    FAULT-CAST-SLUG: 1   # see below

---

# CAST-SLUG CHECK — s03n02

  bone: b01c01s03n02
    cast_slug_issue: FLAG (not fault)
    note: "Subject 'the man with the fish-cart' is an unnamed crowd figure. He does not have a registered actor slug. The schema permits 'the <noun>' for unnamed environment elements. This crowd figure's use of 'watches' is already faulted FAULT-FORM-PERCEPTION. The subject-form itself ('the man with the fish-cart') passes — unnamed-entity form is licensed. No additional FAULT-CAST-SLUG. Removing FAULT-CAST-SLUG from the count."

summary (final corrected):
  total_bones: 27
  correct: 13
  faults: 14
  fault_breakdown:
    FAULT-FORM: 14
    FAULT-CONSTRAINT: 0
    FAULT-PHYSICAL: 0
    FAULT-BONE-DELTA-MALFORMED: 0
    FAULT-AGGREGATE-DELTA-MISMATCH: 0
    FAULT-COST-LEDGER-UNRESOLVED: 0

---

aggregate_check:
  s01:
    target_axes: 0
    observed_moving_axes: 0
    bones_with_axis_moves: []
    deltas: "all 7 bones carry axis_moves: []; trivially clean"
    verdict: CLEAN

  s02:
    target: "capability +1.0"
    observed: "b01c01s02n06 — capability, up, magnitude: 1"
    sum: 1
    target_delta_magnitude: 1.0
    difference: 0
    verdict: CLEAN
    note: "s02n06 is faulted FAULT-FORM-MODIFIER ('inward' adverb). The fault is in the SVO form, not in the substance_delta fields. The axis, direction, and magnitude are all well-formed. The aggregate is arithmetically clean. The bone must be recast; the cost_ledger_anchor: cl01a and axis_moves entry transfer to the recast bone unchanged."

  s03:
    target: "social_tether-prot-rise +1.0"
    observed: "b01c01s03n04 — social_tether-prot-rise, up, magnitude: 1"
    sum: 1
    target_delta_magnitude: 1.0
    difference: 0
    verdict: CLEAN
    note: "s03n04 is faulted FAULT-FORM-NON-ACTION-VERB + FAULT-FORM-MODIFIER ('stands at the lane-mouth'). Same as s02n06: the substance_delta fields are well-formed; fault is in the SVO. The aggregate is arithmetically clean. The recast bone inherits axis_moves, cost_ledger_anchor: cl01b, axes_held: [] unchanged."

cost_ledger_check:
  cl01a:
    used_at: [b01c01s02n06]
    ledger_entry: "gain: capability +1; cost: opportunity-missed (witch-label formation begins; cost-bearer enters exposure radius)"
    bone_axis: capability
    ledger_gain_axis: capability
    axis_match: true
    anchor_scope: "book: b01, chapter: null, scene: null — book-level ledger entry; applies to any b01 chapter"
    anchor_scope_ok: true
    verdict: CLEAN

  cl01b:
    used_at: [b01c01s03n04]
    ledger_entry: "gain: social_tether-prot-rise +2; cost: journey-required: cl01a"
    bone_axis: social_tether-prot-rise
    ledger_gain_axis: social_tether-prot-rise
    axis_match: true
    anchor_scope: "book: b01, chapter: null, scene: null — book-level"
    anchor_scope_ok: true
    partial_settlement_note: "s03 bone carries magnitude: 1 of the ledger's +2 total gain. The remaining +1 (court-layer half) is deferred to b01c03 per pl-2026-05-25-001 HARD. This is structurally sound: ledger entries with book-level anchor can be partially settled across chapters within the book."
    verdict: CLEAN

cast_resolution_check:
  taylor-hebert-kl-122ac: 7 bones as subject (s01n03, s01n05, s01n07, s02n04, s02n09, s02n10, s02n11)
  oswyn-mudway-flea-bottom-elder: 2 bones as subject (s03n04, s03n09)
  wren-stitch-maker-flea-bottom-ward: 0 bones as subject — present in scene narratively (s02n09 rationale, s03 event_map) but not a bone subject; per cond-cost-bearer-scene-frequency, shared screen time is narratively present in the scene chunk and will be established at stitch time; bone-level subject presence is not required for the frequency rule
  unnamed crowd figures (the child, the crowd, the fish-cart holder, the two women): unnamed-entity form; no slug resolution required
  unresolved_slugs: none

constraint_check:
  cond-override-architecture-residue-122ac:
    finding: CLEAN
    notes: "No bone implies multi-shard hijack (Khepri-mantle sealed). Insect deployment in s02 is crowd-sensation at ankle-height — fauna-control, not human-override. Range not stated as exceeding 200m. The 'the nearest dozen bodies yield' (s02n07) describes the physical effect of insect-presence at ankle-height, not Taylor coordinating human nervous systems — this is the fauna-control mechanism producing an environmental response, not the sealed Khepri-mantle. CLEAN."

  cond-kl-witch-label-formation-122ac:
    finding: CLEAN
    notes: "s03 bones enact label formation as a progressive social process (multiple witnesses, Oswyn's categorization composing over time). No bone depicts instant label formation from a single observation. Faith escalation not treated as automatic. Otto's awareness not implied. Label-trigger is observable insect-anomaly (crowd-yield from ankle-height sensation) — matches the card's trigger mechanism."

  cond-kl-geography-122ac:
    finding: CLEAN
    notes: "All scene action is consistent with Hook precinct geometry. 'Lane-mouth' is a standard Hook lane feature. 'Upper alley' is consistent with the Hook's layout. No bones place Taylor outside her 200m operational radius. No invented gates or district misplacements."

  cond-kl-social-physics-122ac:
    finding: CLEAN
    notes: "Oswyn Mudway (ward-elder) standing at the lane-mouth and composing a categorization is consistent with the ward-elder's social authority and observation function per cond-kl-social-physics-122ac. Crowd physics (compression around collapsed child, yielding to ankle-sensation) are consistent with smallfolk crowd behavior. No gold dragons; no direct lord-interaction; no anomalous Watch response."

  cond-taylor-pov-behavior:
    finding: CLEAN
    notes: "Bones are structural-event records, not prose POV passages. The substance_delta rationale fields in a few bones name Taylor's internal state ('Taylor reads the deployment as a one-time lapse') but these are authoring annotations in the substance system, not prose lines. No bone SVO contains interiority — internal states are rationale-layer, not bone-line layer. CLEAN at bone level."

  cond-earth-bet-noun-fence:
    finding: CLEAN
    notes: "No Worm-canon proper nouns appear in any bone SVO. No cape-name vocabulary. No parahuman institutional vocabulary."

  cond-cost-bearer-scene-frequency:
    finding: FLAG (not fault — act 1 is open)
    notes: "Wren (wren-stitch-maker-flea-bottom-ward) is present in b01c01 s02 and s03 per scene chunk and event_map (s02n09 rationale explicitly names her in the crowd). However, no bone has Wren as a subject and no direct interaction beat exists at bone level. The frequency rule requires 'direct shared scene presence ... with at least one direct interaction beat.' b01c01 is the first chapter; the frequency check fires at act boundaries, not per chapter. Act 1 has further chapters. This is not a fault at this point in the act. Surfaced for awareness: the first act-boundary check must locate a qualifying scene."

---

holds_license_check:
  b01c01s01n03: "taylor holds the feet" — object is 'the feet' (body part of subject Taylor); action is stillness-against-pressure (insect-range pull against Taylor's planted position per the rationale). License satisfied on both conditions. CORRECT.
  b01c01s02n04: "taylor holds the feet" — same form, same license application. The rationale confirms: 'the last beat of prohibition-maintenance before the crack — Taylor's body planted, the range pressing.' Stillness-against-pressure confirmed. CORRECT.

perception_verb_check:
  b01c01s01n05: FAULT-FORM-PERCEPTION — 'lifts the eyes' (see fault entry above)
  b01c01s03n02: FAULT-FORM-PERCEPTION — 'watches' (see fault entry above)
  all_other_bones: no perception verbs found

faces_verb_check:
  b01c01s02n09: "taylor faces the child" — 'faces' as discrete transitive posture-act, not stative. Schema's own SVO trap review clears this form. CORRECT.
  b01c01s03n07: "taylor faces the alley-mouth" — same form. CORRECT.

propagate_check:
  b01c01s01n04: "the insects propagate at the edge of range" — FAULT-FORM-MODIFIER ('at the edge of range'). The verb 'propagate' itself is clean.
  b01c01s02n06: "the insects propagate inward" — FAULT-FORM-MODIFIER ('inward' adverb). The verb 'propagate' itself is clean.
  b01c01s02n08: "the gap propagates outward" — FAULT-FORM-MODIFIER ('outward' adverb). The verb 'propagate' itself is clean.

thins_check:
  b01c01s03n01: "the crowd thins" — bare intransitive physical-process verb. 'Thins' is not a motion verb implying destination, not a stative copula, not a perception verb, not on any deny list. Schema's intransitive-lands-cleanly exception applies. CORRECT.

lifts_check:
  b01c01s01n05: "taylor lifts the eyes" — FAULT-FORM-PERCEPTION (see above). The verb 'lifts' is a discrete act but the object makes the bone perceptual.
  b01c01s02n10: "taylor lifts the hands" — 'lifts the hands' is a discrete physical act; object is a body part (the hands); not the perception-surrogate pattern (hands-raising is visible to others as a posture-signal, not a scanning-act). Subject lifting hands is observable external action. CORRECT.
  b01c01s03n09: "oswyn-mudway-flea-bottom-elder lifts the chin" — discrete physical act; body part as object; observable external posture. CORRECT.

---

verdict: FAULTS-PRESENT

high_priority_faults:
  - b01c01s02n06: FAULT-FORM-MODIFIER ('inward') — this is the chapter's capability +1 moving bone; must be recast before Phase 3
  - b01c01s03n04: FAULT-FORM-NON-ACTION-VERB + FAULT-FORM-MODIFIER ('stands at the lane-mouth') — this is the chapter's social_tether-prot-rise +1 moving bone; must be recast before Phase 3

normal_priority_faults_by_scene:
  s01: n01, n02, n04, n05, n06 (n07 passes)
  s02: n01, n02, n08, n11 (n03, n04, n05, n07, n09, n10 pass; n06 high-priority)
  s03: n02, n03, n05, n08 (n01, n06, n07, n09 pass; n04 high-priority)

fixer_scope: minimum-change recasts to the 14 faulted bones only. Substance_delta fields on the two moving bones (s02n06, s03n04) are well-formed and transfer to the recast bones unchanged. No aggregate-delta recomputation required — arithmetic is already correct.
