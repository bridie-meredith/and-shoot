# write-b01c01-pass2 audit report — RE-AUDIT: ROUND 3
phase: /and-write b01c01 Phase 2 constraint audit (round 3 — three-patch confirmation)
date: 2026-05-25
auditor: auditor
artifact_audited: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
re_audit_trigger: three faults from round 2 patched by fixer; full re-scan from clean context
bone_count: 26 (s01=6, s02=11, s03=9)

---

summary:
  total_bones: 26
  correct: 26
  faults: 0
  flags: 2  # carried from round 2; no new flags
  verdict: CLEAN

---

audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-25
  findings:

    # -------------------------------------------------------------------------
    # PATCH VERIFICATION — three round-2 faults
    # -------------------------------------------------------------------------

    - id: patch-verify-001
      type: pass
      what: "bone b01c01s02n05 — svo now reads: 'the lane-mouth presses the crowd'"
      why: "Round 2 fault-001 (FAULT-FORM-MODIFIER: 'inward' adverb) is resolved. 'the lane-mouth presses the crowd' is transitive; 'the crowd' is the direct object; no adverb, no prepositional modifier; 'presses' is not on any deny list; crowd-compression semantic preserved. The substance_delta (axes_held: political_register-prot) is unaffected by the SVO patch and remains well-formed."

    - id: patch-verify-002
      type: pass
      what: "bone b01c01s03n06 — svo now reads: 'the gap closes'"
      why: "Round 2 fault-002 (FAULT-FORM-MODIFIER: 'in the lane' prepositional phrase of place) is resolved. 'closes' is a physical-process intransitive verb — not a motion verb implying destination, not stative, not a copula, not a perception verb, not a non-action verb. The intransitive-lands-cleanly exception applies: 'closes' describes a physical process (gap elimination) analogous to 'thins' (s03n01), 'compresses' (s02n03), 'propagates' (s02n06, s02n08) — all cleared in rounds 1 and 2 on the same exception. The lane-gap-closing semantic is fully legible from the bare intransitive. The substance_delta (axes_held: moral_framework) is unaffected and well-formed."

    - id: patch-verify-003
      type: pass
      what: "s01 event_map entry 'ward read only at surfaces — bodies moving, foot traffic, smell' — covered_by now reads: [b01c01s01n02, b01c01s01n07]"
      why: "Round 2 fault-003 (FAULT-EVENT-MAP-STALE-REFERENCE: dead reference to dropped bone b01c01s01n05) is resolved. Both referenced bones exist in the patched draft. Substantive coverage verified: s01n02 ('the tallow smoke crosses the stitch-house lane') covers the olfactory surface-read ('smell' component of the event); s01n07 ('taylor exhales') carries the relocated political_register-prot axes_held rationale ('Taylor holds the ward-read at structural baseline rank 1; the ward is smallfolk-only; no court-layer material enters the drain angle; the exhalation closes the morning scan without a court-encounter') which directly covers the 'bodies moving, foot traffic' surface-read semantic. Dead reference eliminated. Coverage is substantive, not nominal."

    # -------------------------------------------------------------------------
    # FULL RE-SCAN — 26 bones
    # -------------------------------------------------------------------------

    - id: full-scan-001
      type: pass
      what: "Full 26-bone SVO re-scan complete"
      why: "No new faults introduced by the three patches or by the surrounding context. All findings below."

---

# PER-BONE VERDICT TABLE — ROUND 3 (26 bones)

scene: b01c01s01 (6 bones)

  b01c01s01n01  CLEAN — 'the drain water threads the angle-gap': transitive; 'angle-gap' compound noun direct object; no modifier; 'threads' not on deny list. substance_delta: axis_moves: [], axes_held: [social_tether-prot-rise] — well-formed.

  b01c01s01n02  CLEAN — 'the tallow smoke crosses the stitch-house lane': transitive; 'stitch-house lane' compound noun direct object; no modifier; 'crosses' not on deny list. substance_delta: axis_moves: [], axes_held: [relational_anchor_status] — well-formed. Also covers s01 event_map 'ward read only at surfaces — smell' component (confirmed above).

  b01c01s01n03  CLEAN — 'taylor holds the feet': holds-license satisfied — body part of subject; stillness-against-pressure rationale confirmed ('Taylor's feet planted while the insect-range pulls'). substance_delta: axes_held: [capability, moral_framework] — well-formed.

  b01c01s01n04  CLEAN — 'the insects propagate': bare intransitive physical-process verb; not a motion verb implying destination; intransitive-lands-cleanly exception applies. substance_delta: axes_held: [capability, moral_framework] — well-formed.

  b01c01s01n06  CLEAN — 'the angle-wall narrows the lane': transitive geometry-action; 'the lane' direct object; no modifier. substance_delta: axes_held: [social_tether-prot-rise] — well-formed.

  b01c01s01n07  CLEAN — 'taylor exhales': canonical intransitive-lands-cleanly example (explicitly cited in schema). Three axes_held (moral_legibility_to_self, moral_framework, political_register-prot): schema imposes no cap on axes_held[] count; the axis_moves cap of 1-2 per-bone applies only to in-motion axes (confirmed round 1 schema reading). Third axes_held entry is the relocated political_register-prot rationale from dropped s01n05 — load-bearing for both held-axis coverage and the s01 event_map 'ward read only at surfaces' entry. substance_delta well-formed.

scene: b01c01s02 (11 bones)

  b01c01s02n01  CLEAN — 'the fish-cart blocks the lane': transitive; 'the lane' direct object; no modifier. substance_delta: axes_held: [social_tether-prot-rise] — well-formed.

  b01c01s02n02  CLEAN — 'the ground transmits the child's breath': transitive; 'transmits' not on deny list; 'the child's breath' is a concrete physical bio-signal (vibration/respiratory output transmitted through cobbles) — not abstraction-as-object. substance_delta: axes_held: [capability] — well-formed.

  b01c01s02n03  CLEAN — 'the crowd compresses': bare intransitive physical-process; intransitive-lands-cleanly applies. substance_delta: axes_held: [moral_framework] — well-formed.

  b01c01s02n04  CLEAN — 'taylor holds the feet': holds-license satisfied (same as s01n03). substance_delta: axes_held: [moral_framework, capability] — well-formed.

  b01c01s02n05  CLEAN — 'the lane-mouth presses the crowd': transitive (patched from round 2 fault-001); 'the crowd' direct object; no adverb; no prepositional modifier; crowd-compression semantic preserved. substance_delta: axes_held: [political_register-prot] — well-formed. Patch verified above (patch-verify-001).

  b01c01s02n06  CLEAN — 'the insects propagate': bare intransitive physical-process; intransitive-lands-cleanly applies. Moving bone: axis_moves: [capability, up, magnitude: 1]; cost_ledger_anchor: cl01a. substance_delta well-formed.

  b01c01s02n07  FLAG (carried from round 2, flag-001) — 'the nearest dozen bodies yield': subject adjective 'nearest' noted; not hard-faulted per round 2 ruling (subject-identifier disambiguation for unnamed crowd subsets; no schema authority explicitly bans adjectives in subject-identifier slot for unnamed entities). 'yield' is intransitive physical-process (observable crowd-movement); intransitive-lands-cleanly applies. substance_delta: axes_held: [moral_framework] — well-formed. No new finding.

  b01c01s02n08  CLEAN — 'the gap propagates': bare intransitive physical-process; intransitive-lands-cleanly applies. substance_delta: axes_held: [capability] — well-formed.

  b01c01s02n09  CLEAN — 'taylor faces the child': transitive posture-act (licensed by schema SVO trap review); 'the child' direct object; no modifier. substance_delta: axes_held: [relational_anchor_status] — well-formed.

  b01c01s02n10  CLEAN — 'taylor lifts the hands': transitive discrete physical act; body-part direct object; not a perception verb. substance_delta: axes_held: [social_tether-prot-rise] — well-formed.

  b01c01s02n11  CLEAN — 'taylor raises the voice': transitive; 'raises' not on deny list; 'the voice' is the physical vocal-sound output (not abstract communication-content). substance_delta: axes_held: [moral_legibility_to_self] — well-formed.

scene: b01c01s03 (9 bones)

  b01c01s03n01  CLEAN — 'the crowd thins': bare intransitive physical-process; intransitive-lands-cleanly applies. substance_delta: axes_held: [political_register-prot] — well-formed.

  b01c01s03n02  CLEAN — 'the fish-cart man faces taylor': transitive posture-act (licensed); compound-noun subject is clean unnamed-entity form. substance_delta: axes_held: [social_tether-prot-rise] — well-formed.

  b01c01s03n03  CLEAN — 'the two women face the lane': transitive posture-act; collective unnamed-entity subject is not FAULT-FORM-MULTI-SUBJECT (that fault targets named-actor conjunctions; collective noun phrases are permitted, per round 2 ruling). substance_delta: axes_held: [social_tether-prot-rise] — well-formed.

  b01c01s03n04  CLEAN — 'oswyn-mudway-flea-bottom-elder takes the lane-mouth': transitive discrete act; 'takes' not on any deny list; 'the lane-mouth' compound noun direct object; no prepositional phrase. Moving bone: axis_moves: [social_tether-prot-rise, up, magnitude: 1]; cost_ledger_anchor: cl01b. substance_delta well-formed.

  b01c01s03n05  CLEAN — 'the child clears the lane': transitive; 'clears' not on deny list; 'the lane' as direct-object destination satisfies the motion-verb-destination requirement (resolves the original bare-intransitive 'departs' fault from pass 1). substance_delta: axes_held: [capability] — well-formed.

  b01c01s03n06  CLEAN — 'the gap closes': bare intransitive physical-process (patched from round 2 fault-002); intransitive-lands-cleanly exception applies ('closes' is a physical-process verb, not a motion verb implying destination). Patch verified above (patch-verify-002). substance_delta: axes_held: [moral_framework] — well-formed.

  b01c01s03n07  CLEAN — 'taylor faces the alley-mouth': transitive posture-act; 'the alley-mouth' compound noun direct object; no modifier. substance_delta: axes_held: [relational_anchor_status, moral_legibility_to_self] — well-formed.

  b01c01s03n08  CLEAN — 'the tallow smoke layers the lane-floor': transitive; 'layers' not on deny list; 'the lane-floor' compound noun direct object (not a prepositional phrase). substance_delta: axes_held: [relational_anchor_status] — well-formed.

  b01c01s03n09  CLEAN — 'oswyn-mudway-flea-bottom-elder lifts the chin': transitive discrete physical act; body-part direct object; observable posture-gesture. substance_delta: axes_held: [social_tether-prot-rise] — well-formed.

---

# AGGREGATE DELTA CHECKS — ROUND 3

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

s03:
  axis: social_tether-prot-rise
  direction: up
  moving_bones: [b01c01s03n04 — magnitude: 1]
  sum: 1
  target: 1.0
  verdict: CLEAN

---

# HELD-AXIS COVERAGE CHECKS — ROUND 3

s01 (held: moral_framework, capability, relational_anchor_status, moral_legibility_to_self, political_register-prot, social_tether-prot-rise):
  moral_framework: s01n03 ✓, s01n04 ✓, s01n07 ✓
  capability: s01n03 ✓, s01n04 ✓
  relational_anchor_status: s01n02 ✓
  moral_legibility_to_self: s01n07 ✓
  political_register-prot: s01n07 ✓  (relocated from dropped s01n05; load-bearing; s01 event_map coverage confirmed)
  social_tether-prot-rise: s01n01 ✓, s01n06 ✓
  verdict: CLEAN — all 6 held axes covered by surviving bones

s02 (held: moral_framework, relational_anchor_status, moral_legibility_to_self, political_register-prot, social_tether-prot-rise):
  moral_framework: s02n03 ✓, s02n04 ✓, s02n07 ✓
  relational_anchor_status: s02n09 ✓
  moral_legibility_to_self: s02n11 ✓
  political_register-prot: s02n05 ✓ (SVO clean post-patch; substance_delta unaffected)
  social_tether-prot-rise: s02n01 ✓, s02n10 ✓
  verdict: CLEAN — all 5 held axes covered

s03 (held: moral_framework, relational_anchor_status, moral_legibility_to_self, political_register-prot, capability):
  moral_framework: s03n06 ✓ (SVO clean post-patch; substance_delta unaffected)
  relational_anchor_status: s03n07 ✓, s03n08 ✓
  moral_legibility_to_self: s03n07 ✓
  political_register-prot: s03n01 ✓
  capability: s03n05 ✓
  verdict: CLEAN — all 5 held axes covered

---

# COST LEDGER CHECKS — ROUND 3

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

# EVENT MAP CHECKS — ROUND 3

s01 event_map:
  - "Taylor sleeping in the covered drain angle" — covered_by: [s01n01, s01n06] — both exist. CLEAN.
  - "insects held at subsistence range" — covered_by: [s01n03, s01n04] — both exist. CLEAN.
  - "ward read only at surfaces — bodies moving, foot traffic, smell" — covered_by: [s01n02, s01n07] — both exist; substantive coverage confirmed (patch-verify-003). CLEAN.
  - "stitch-house smell two lanes over" — covered_by: [s01n02] — exists. CLEAN.
  - "prohibition-maintenance" — covered_by: [s01n07] — exists. CLEAN.
  - "protagonist_force" — covered_by: [s01n03, s01n04] — both exist. CLEAN.
  - "opposing_force" — covered_by: [s01n04, s01n07] — both exist. CLEAN.
  - "ward anonymity" — covered_by: [s01n01, s01n06] — both exist. CLEAN.

s02 event_map: all covered_by[] slugs reference existing bones. CLEAN.

s03 event_map: all covered_by[] slugs reference existing bones. CLEAN.

---

# CAST RESOLUTION — ROUND 3

  taylor: protagonist actor slug — appears throughout as subject. CLEAN.
  oswyn-mudway-flea-bottom-elder: named actor slug — appears at s03n04, s03n09 as subject. CLEAN.
  unnamed entities ('the drain water', 'the tallow smoke', 'the insects', 'the angle-wall', 'the fish-cart', 'the ground', 'the crowd', 'the lane-mouth', 'the nearest dozen bodies', 'the gap', 'the child', 'the fish-cart man', 'the two women'): all 'the <noun>' form for unnamed environment elements per schema. CLEAN.

---

# STANDING FLAGS (carried from round 2; no new flags)

  flag-001 (round 2): b01c01s02n07 subject adjective 'nearest' — not hard-faulted; editorial awareness. Still stands. No fixer dispatch.
  flag-002 (round 2): decomposer_notes SUBSTANCE ARITHMETIC block references 'political_register-prot: n05' (dropped bone) — annotation inconsistency; not schema-governed; editorial awareness only. Still stands. No fixer dispatch.

---

verdict: CLEAN

fault_count: 0
flag_count: 2 (both carried from round 2; no new flags; no new faults)

round_3_determination: All three round-2 faults are resolved correctly. No new violations introduced by the patches or found elsewhere in the 26-bone artifact. Full re-scan across all SVO forms, substance_delta well-formedness, aggregate sums, cost-ledger anchors, held-axis coverage, event_map reference integrity, and cast resolution returns CLEAN. Orchestrator may advance to Phase 3.
