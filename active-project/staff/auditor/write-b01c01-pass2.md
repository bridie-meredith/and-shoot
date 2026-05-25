# write-b01c01-pass2 audit report — RE-AUDIT: ROUND 2
phase: /and-write b01c01 Phase 2 constraint audit (re-audit after fixer pass)
date: 2026-05-25
auditor: auditor
artifact_audited: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
re_audit_trigger: fixer applied 14 SVO recasts + 1 bone drop (s01n05); re-scan from clean context
bone_count_post_patch: 26 (s01=6, s02=11, s03=9)

---

summary:
  total_bones: 26
  correct: 23
  faults: 2
  flags: 2
  fault_breakdown:
    FAULT-FORM-MODIFIER: 2
    FAULT-EVENT-MAP-STALE-REFERENCE: 1   # see fault-003 below; classified as fault not flag because the event_map is a schema-governed field checked at Phase 6 event-presence gate
    FAULT-FORM: 1                         # s02n05 'inward' adverb (missed in pass 1)
  note: "fault-003 is the event_map stale reference; the FAULT-FORM-MODIFIER count above refers to s02n05 and s03n06. Total distinct faults: 3 (two SVO form faults + one event_map structural fault)."

---

audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-25
  findings:

    # -------------------------------------------------------------------------
    # FAULT — s02n05: 'inward' adverb of direction (MISSED IN PASS 1)
    # -------------------------------------------------------------------------

    - id: fault-001
      type: fault
      what: "bone b01c01s02n05 — svo: 'the lane-mouth presses the crowd inward'"
      why: "'inward' is an adverb of direction. schemas/bones.schema.md § field rules: 'No modifiers. No adjectives, no adverbs, no prepositional padding.' Adverbs are banned without qualification. The first pass faulted and patched 'inward' at the former s02n06 ('the insects propagate inward' → 'the insects propagate') and 'outward' at the former s02n08 ('the gap propagates outward' → 'the gap propagates') on exactly this rule. The same adverb appears in s02n05's SVO and was not flagged in pass 1. The fixer did not patch this bone. The adverb survives into the patched draft."
      criteria: "The svo for b01c01s02n05 must not contain 'inward' or any other adverb or prepositional modifier. The crowd-compression semantic must be preserved; the direction of compression is scene context and does not need to appear in the bone."
      class: FAULT-FORM-MODIFIER
      priority: normal
      recast_hint: "'the lane-mouth presses the crowd' — direct object retained; adverb dropped; the compression direction is implied by a lane-mouth pressing a crowd and can be carried in loc-state facet"

    # -------------------------------------------------------------------------
    # FAULT — s03n06: 'in the lane' prepositional phrase of place (MISSED IN PASS 1)
    # -------------------------------------------------------------------------

    - id: fault-002
      type: fault
      what: "bone b01c01s03n06 — svo: 'the gap closes in the lane'"
      why: "'in the lane' is a prepositional phrase of place. schemas/bones.schema.md § field rules: 'Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned (FAULT-FORM-MODIFIER).' The first pass faulted and patched: 'at the edge of range' (s01n04 original), 'at the lane-mouth' (s03n04 original), 'at the lane-level' (s03n08 original), 'under the angle' (s01n01 original), 'from the stitch-house' (s01n02 original) — all prepositional phrases of place/source. 'in the lane' is the same class. The first pass missed this bone; it was listed as passing. The fixer did not patch it."
      criteria: "The svo for b01c01s03n06 must not contain 'in the lane' or any other prepositional phrase of place. The lane-gap-closing semantic must be preserved. The physical event (the crowd-gap that the insect deployment opened is now closed) must remain legible."
      class: FAULT-FORM-MODIFIER
      priority: normal
      recast_hint: "'the gap closes' — bare intransitive; 'closes' is a physical-process verb analogous to 'thins' (s03n01) and 'propagates'; closes without destination does not imply a motion-to-destination gap; OR: 'the lane closes the gap' — transitive, lane as subject acting on the gap"

    # -------------------------------------------------------------------------
    # FAULT — s01 event_map: stale reference to dropped bone b01c01s01n05
    # -------------------------------------------------------------------------

    - id: fault-003
      type: fault
      what: "s01 event_map entry: event 'ward read only at surfaces — bodies moving, foot traffic, smell' — covered_by: [b01c01s01n05] — bone b01c01s01n05 was dropped by the fixer; the event_map entry was not updated"
      why: "The event_map is a schema-governed field checked at /and-write Phase 6 event-presence gate, which validates that every named bone in covered_by[] still exists. b01c01s01n05 does not exist in the patched draft. The event_map entry is a dead reference: the coverage is empty (no surviving bone covers this event) and the reference is to a non-existent slug. The fixer relocated the political_register-prot held rationale from s01n05 to s01n07 but did not update the event_map. The event 'ward read only at surfaces' is now uncovered in the event_map — either the coverage must be reassigned to an existing bone or an omission_rationale must be added. The Phase 6 event-presence gate reads event_map[] and will fault this missing bone at gate-time."
      criteria: "The s01 event_map entry for 'ward read only at surfaces — bodies moving, foot traffic, smell' must either (a) have covered_by[] updated to reference an existing bone that covers this event, or (b) have covered_by[] set to [] with omission_rationale explaining that the ward-read event is now carried by the facet layer (narrator-interest or sensory) rather than a dedicated bone, citing the relevant bones those facets will attach to. The dead reference to b01c01s01n05 must be removed."
      class: FAULT-EVENT-MAP-STALE-REFERENCE
      priority: HIGH — Phase 6 event-presence gate reads this field; a dead bone slug will halt the gate check

    # -------------------------------------------------------------------------
    # FLAG — s02n07: subject adjective 'nearest' in 'the nearest dozen bodies'
    # -------------------------------------------------------------------------

    - id: flag-001
      type: flag
      what: "bone b01c01s02n07 — svo: 'the nearest dozen bodies yield' — subject contains adjective 'nearest'"
      why: "schemas/bones.schema.md § field rules: 'No adjectives.' The subject identifier 'the nearest dozen bodies' contains the superlative adjective 'nearest.' The prior audit (pass 1) tolerated subject-identifier disambiguating tags for unnamed entities (ruling on 'the man with the fish-cart' and 'the two women from the upper alley') and did not fault adjective/numeral qualifiers in the subject position. 'Dozen' is a numeral-collective (analogous to 'the crowd'); 'nearest' is a pure spatial-positional adjective with no numeral or collective function. The pass-1 tolerance reasoning applies to disambiguating tags (prepositional or numeral-collective); it does not clearly cover pure adjectives. This auditor declines to hard-fault on the basis of the established subject-identifier tolerance precedent but surfaces the adjective for editorial awareness."
      why_not_faulted: "The schema's 'no adjectives' rule targets the verb/object modifier positions explicitly ('No modifiers. No adjectives, no adverbs, no prepositional padding. Time and place go in citations to location-state, not in the bone. Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned'). Subject-identifier disambiguation for unnamed crowd subsets requires some differentiating marker; the 'nearest' adjective performs this function. No schema authority explicitly bans adjectives in the subject-identifier slot for unnamed entities. Not escalated to fault."

    # -------------------------------------------------------------------------
    # FLAG — decomposer_notes stale coverage map (annotation only; not schema-governed)
    # -------------------------------------------------------------------------

    - id: flag-002
      type: flag
      what: "decomposer_notes SUBSTANCE ARITHMETIC block (lines 460-461): 's01 held axes — political_register-prot: n05' — references dropped bone s01n05"
      why: "The decomposer_notes block is an authoring annotation, not a schema-governed field. However, the coverage map at lines 460-461 states 'political_register-prot: n05' which references the dropped bone. The actual coverage is now s01n07 (per the fixer's relocation). If downstream readers consult the decomposer_notes to verify held-axis coverage, they will find a stale annotation pointing to a non-existent bone. This is an annotation inconsistency, not a schema fault. No fixer dispatch required; the fixer may update the annotation as a courtesy if editing the draft for other reasons."
      why_not_faulted: "decomposer_notes is free-text annotation; no schema field governs its accuracy. The actual axes_held[] entries on s01n07 correctly carry political_register-prot. The schema-governed coverage is correct; the annotation is stale."

---

# PER-BONE VERDICT TABLE (26 bones)

scene: b01c01s01 (6 bones after s01n05 drop)

  b01c01s01n01  CORRECT — 'the drain water threads the angle-gap': transitive; 'the angle-gap' is a compound noun direct object; no modifiers; verb not on deny list; substance_delta well-formed.

  b01c01s01n02  CORRECT — 'the tallow smoke crosses the stitch-house lane': transitive; 'the stitch-house lane' is a compound noun direct object; 'crosses' not on deny list; no modifiers; pl-002 SOFT relational_anchor_status plant preserved; substance_delta well-formed.

  b01c01s01n03  CORRECT — 'taylor holds the feet': holds-license satisfied (body part of subject; stillness-against-pressure against insect-range pull per rationale); substance_delta well-formed (axes_held: capability, moral_framework).

  b01c01s01n04  CORRECT — 'the insects propagate': bare intransitive physical-process verb; intransitive-lands-cleanly exception applies ('propagate' is not a motion verb implying destination; it describes a physical spread/multiply process analogous to 'thins'); substance_delta well-formed (axes_held: capability, moral_framework).

  b01c01s01n06  CORRECT — 'the angle-wall narrows the lane': transitive geometry-action; 'narrows' not on deny list; no modifiers; substance_delta well-formed (axes_held: social_tether-prot-rise).

  b01c01s01n07  CORRECT — 'taylor exhales': intransitive-lands-cleanly exception applies explicitly (canonical schema example); substance_delta well-formed. Three axes_held entries (moral_legibility_to_self, moral_framework, political_register-prot): schema defines no cap on axes_held[] count; chunk_targets.bone.axes_per_bone governs axis_moves[] count (moving axes), not the axes_held[] list; the third entry is a relocation from the dropped s01n05 and is load-bearing for political_register-prot held-axis coverage.

scene: b01c01s02 (11 bones)

  b01c01s02n01  CORRECT — 'the fish-cart blocks the lane': transitive; direct object retained; 'crosswise' adverb dropped by fixer; substance_delta well-formed.

  b01c01s02n02  CORRECT — 'the ground transmits the child's breath': 'transmits' is transitive and not on deny list; 'the child's breath' is the physical bio-signal (vibration/respiratory output transmitted through cobbles) — concrete physical phenomenon, not abstraction-as-object; substance_delta well-formed.

  b01c01s02n03  CORRECT — 'the crowd compresses': bare intransitive physical-process verb; intransitive-lands-cleanly exception applies; substance_delta well-formed.

  b01c01s02n04  CORRECT — 'taylor holds the feet': same holds-license as s01n03 (body part; stillness-against-pressure confirmed by rationale); substance_delta well-formed.

  b01c01s02n05  FAULT-FORM-MODIFIER — 'the lane-mouth presses the crowd inward': 'inward' is a banned adverb of direction. See fault-001.

  b01c01s02n06  CORRECT — 'the insects propagate': bare intransitive physical-process verb; intransitive-lands-cleanly exception applies; moving bone (capability +1, cl01a); substance_delta well-formed; axis_moves: [capability, up, magnitude: 1], cost_ledger_anchor: cl01a.

  b01c01s02n07  FLAG — 'the nearest dozen bodies yield': subject adjective 'nearest' (see flag-001). Bone is not hard-faulted. 'yield' is an intransitive physical-process verb (the crowd-subset yields to insect-presence — observable physical movement); intransitive-lands-cleanly exception applies; no modifier on verb or object; substance_delta well-formed.

  b01c01s02n08  CORRECT — 'the gap propagates': bare intransitive physical-process verb; intransitive-lands-cleanly exception applies; 'outward' adverb dropped by fixer; substance_delta well-formed.

  b01c01s02n09  CORRECT — 'taylor faces the child': 'faces' licensed as transitive posture-act (confirmed by schema's own SVO trap review); no modifiers; substance_delta well-formed.

  b01c01s02n10  CORRECT — 'taylor lifts the hands': discrete physical act; body-part object; visible posture-signal, not perception-surrogate; substance_delta well-formed.

  b01c01s02n11  CORRECT — 'taylor raises the voice': 'raises' is transitive and not on deny list; 'the voice' is the physical vocal-sound output, not an abstract communication-content object (not abstraction-as-object); substance_delta well-formed.

scene: b01c01s03 (9 bones)

  b01c01s03n01  CORRECT — 'the crowd thins': bare intransitive physical-process verb; intransitive-lands-cleanly exception applies; substance_delta well-formed.

  b01c01s03n02  CORRECT — 'the fish-cart man faces taylor': 'faces' licensed transitive posture-act; compound-noun subject is cleaner unnamed-entity form; substance_delta well-formed.

  b01c01s03n03  CORRECT — 'the two women face the lane': 'the two women' is a collective unnamed-entity form (parallel to 'the crowd'); no FAULT-FORM-MULTI-SUBJECT — schema's multi-subject fault targets named-actor conjunctions (e.g. 'taylor and rowan walk'), not collective noun phrases; 'face' is licensed transitive posture-act; substance_delta well-formed.

  b01c01s03n04  CORRECT — 'oswyn-mudway-flea-bottom-elder takes the lane-mouth': 'takes' is transitive and discrete (not on any deny list; not a stative position-naming verb); 'the lane-mouth' is a compound-noun direct object (no prepositional phrase); moving bone (social_tether-prot-rise +1, cl01b); substance_delta well-formed.

  b01c01s03n05  CORRECT — 'the child clears the lane': transitive; 'the lane' as direct object resolves FAULT-FORM-NO-VERB from the original 'the child departs'; motion-with-destination-as-direct-object form; substance_delta well-formed.

  b01c01s03n06  FAULT-FORM-MODIFIER — 'the gap closes in the lane': 'in the lane' is a banned prepositional phrase of place. See fault-002.

  b01c01s03n07  CORRECT — 'taylor faces the alley-mouth': 'faces' licensed transitive posture-act; 'the alley-mouth' compound noun direct object; no modifiers; substance_delta well-formed (axes_held: relational_anchor_status, moral_legibility_to_self).

  b01c01s03n08  CORRECT — 'the tallow smoke layers the lane-floor': 'layers' is transitive and not on deny list; 'the lane-floor' is a compound noun direct object (not a prepositional phrase); pl-002 SOFT stitch-house continuity preserved; substance_delta well-formed.

  b01c01s03n09  CORRECT — 'oswyn-mudway-flea-bottom-elder lifts the chin': discrete physical act; body-part object; visible posture gesture (observable to Taylor); not perception-surrogate; substance_delta well-formed.

---

# AGGREGATE DELTA CHECKS

s01:
  axes_in_motion: none
  moving_bones: 0
  sum: 0
  target: 0
  verdict: CLEAN

s02:
  axis: capability
  direction: up
  moving_bones: [b01c01s02n06 — magnitude: 1]
  sum: 1
  target: 1.0
  verdict: CLEAN
  note: "s02n05 is faulted FAULT-FORM-MODIFIER ('inward') but carries no axis_moves; fault is in the SVO form; aggregate unaffected."

s03:
  axis: social_tether-prot-rise
  direction: up
  moving_bones: [b01c01s03n04 — magnitude: 1]
  sum: 1
  target: 1.0
  verdict: CLEAN
  note: "s03n06 is faulted FAULT-FORM-MODIFIER ('in the lane') but carries no axis_moves; fault is in the SVO form; aggregate unaffected."

---

# HELD-AXIS COVERAGE CHECKS

s01 (held: moral_framework, capability, relational_anchor_status, moral_legibility_to_self, political_register-prot, social_tether-prot-rise):
  moral_framework: s01n03 ✓, s01n04 ✓, s01n07 ✓
  capability: s01n03 ✓, s01n04 ✓
  relational_anchor_status: s01n02 ✓
  moral_legibility_to_self: s01n07 ✓
  political_register-prot: s01n07 ✓  (relocated from dropped s01n05)
  social_tether-prot-rise: s01n01 ✓, s01n06 ✓
  verdict: CLEAN — all 6 held axes covered by surviving bones

s02 (held: moral_framework, relational_anchor_status, moral_legibility_to_self, political_register-prot, social_tether-prot-rise):
  moral_framework: s02n03 ✓, s02n04 ✓, s02n07 ✓
  relational_anchor_status: s02n09 ✓
  moral_legibility_to_self: s02n11 ✓
  political_register-prot: s02n05 ✓ (faulted SVO; axes_held well-formed)
  social_tether-prot-rise: s02n01 ✓, s02n10 ✓
  verdict: CLEAN — all 5 held axes covered; s02n05's FAULT-FORM-MODIFIER is a SVO fault, not a substance_delta fault; the axes_held entry is well-formed and the coverage stands

s03 (held: moral_framework, relational_anchor_status, moral_legibility_to_self, political_register-prot, capability):
  moral_framework: s03n06 ✓ (faulted SVO; axes_held well-formed)
  relational_anchor_status: s03n07 ✓, s03n08 ✓
  moral_legibility_to_self: s03n07 ✓
  political_register-prot: s03n01 ✓
  capability: s03n05 ✓
  verdict: CLEAN — all 5 held axes covered; s03n06's FAULT-FORM-MODIFIER is a SVO fault, not a substance_delta fault; the axes_held entry is well-formed and the coverage stands

---

# COST LEDGER CHECKS

cl01a:
  used_at: [b01c01s02n06]
  bone_axis: capability / up / magnitude: 1
  ledger_gain_axis: capability
  axis_match: true
  verdict: CLEAN

cl01b:
  used_at: [b01c01s03n04]
  bone_axis: social_tether-prot-rise / up / magnitude: 1
  ledger_gain_axis: social_tether-prot-rise
  axis_match: true
  partial_settlement: 1 of +2 total; remaining +1 deferred to b01c03 per pl-2026-05-25-001 HARD
  verdict: CLEAN

---

# EVENT MAP CHECKS

s01 event_map:
  - event: "Taylor sleeping in the covered drain angle" — covered_by: [b01c01s01n01, b01c01s01n06] — both bones exist. CLEAN.
  - event: "insects held at subsistence range" — covered_by: [b01c01s01n03, b01c01s01n04] — both bones exist. CLEAN.
  - event: "ward read only at surfaces — bodies moving, foot traffic, smell" — covered_by: [b01c01s01n05] — STALE REFERENCE: b01c01s01n05 does not exist. FAULT (see fault-003).
  - event: "stitch-house smell two lanes over" — covered_by: [b01c01s01n02] — bone exists. CLEAN.
  - event: "prohibition-maintenance" — covered_by: [b01c01s01n07] — bone exists. CLEAN.
  - event: "protagonist_force" — covered_by: [b01c01s01n03, b01c01s01n04] — both bones exist. CLEAN.
  - event: "opposing_force" — covered_by: [b01c01s01n04, b01c01s01n07] — both bones exist. CLEAN.
  - event: "ward anonymity" — covered_by: [b01c01s01n01, b01c01s01n06] — both bones exist. CLEAN.

s02 event_map: all covered_by[] slugs reference existing bones. CLEAN.

s03 event_map: all covered_by[] slugs reference existing bones. CLEAN.

---

verdict: FAULTS-PRESENT

fault_count: 3
  - fault-001: b01c01s02n05 — FAULT-FORM-MODIFIER ('inward') — normal priority; SVO fault; axes_held coverage unaffected; recast required before Phase 3
  - fault-002: b01c01s03n06 — FAULT-FORM-MODIFIER ('in the lane') — normal priority; SVO fault; axes_held coverage unaffected; recast required before Phase 3
  - fault-003: s01 event_map stale reference to b01c01s01n05 — HIGH priority; Phase 6 event-presence gate reads this field; dead slug must be removed and event coverage resolved

flag_count: 2
  - flag-001: b01c01s02n07 subject adjective 'nearest' — not hard-faulted; editorial awareness
  - flag-002: decomposer_notes stale coverage annotation — not schema-governed; editorial awareness

fixer_scope: "Three targeted fixes. (1) s02n05: strip 'inward' from SVO. (2) s03n06: strip 'in the lane' from SVO (bare intransitive 'the gap closes' or transitive recast). (3) s01 event_map: remove dead reference to b01c01s01n05 from the 'ward read only at surfaces' entry and either assign covered_by[] to an existing bone or add omission_rationale. No substance_delta changes required for any fix. Moving bone substance_deltas (s02n06, s03n04) are unaffected."

high_priority_items:
  - fault-003: s01 event_map stale reference — HARD at Phase 6 event-presence gate

moving_bones_status:
  - s02n06 (capability +1, cl01a): CORRECT — no faults on this bone
  - s03n04 (social_tether-prot-rise +1, cl01b): CORRECT — no faults on this bone
