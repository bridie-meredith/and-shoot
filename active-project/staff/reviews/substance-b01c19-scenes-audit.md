audit:
  scope: chapter
  target: b01c19
  timestamp: 2026-06-05
  findings:

    - id: fault-001
      type: flag
      what: b01c19s02 chunk body, line 88 — literal text "Shape-language only:" appears inline in chunk prose at the Taylor pattern-naming beat
      why: this is an authoring-layer directive embedded in prose-body position; /and-write Phase 1 scene-decomposition consumes chunk text as narrative description of what happens; the string "Shape-language only:" will read as a renderer instruction that belongs in notes/constraints, not in the chunk prose that becomes the basis for bone-authoring; if /and-write renders it literally as Taylor's voice or as action description, the Earth-Bet fence ceases to be a constraint and becomes a character line
      criteria: the directive must be removed from the chunk prose body and expressed as an authoring constraint in the scene_conflict or substance_delta notes field, where /and-write will read it as a constraint rather than a narrative beat

    - id: fault-002
      type: flag
      what: b01c19s03 chunk body, line 167 — literal text "Cl06 is paid." appears inline in chunk prose between narrative sentences
      why: this is a cost-ledger accounting notation embedded in prose-body position; /and-write will encounter it mid-chunk-text during bone decomposition; it carries no character-facing event content and functions as an authoring-layer state update, not a narrative beat; it risks being inherited into a bone as voice or action content, or causing a bone-boundary ambiguity at the "Clarity forecloses nothing." line immediately following
      criteria: the cost-ledger notation must be removed from the chunk prose body; if the cost-paid status needs to be marked for /and-write awareness, it belongs in the substance_delta notes for the axis, not in the chunk narrative

    - id: fault-003
      type: flag
      what: b01c19s01 chunk lines 29, 38 ("since c12", "since c13"); b01c19s02 chunk lines 90-91 ("through c12 through c18"); b01c19s03 chunk line 141 ("since c14")
      why: bare chapter-slug strings are planning-shorthand that /and-write must convert to narrative-time expressions; this is expected at chunk level (SIGNAL per Check 8 of the audit brief) and does not constitute a contract inconsistency; noted as a downstream-awareness flag so /and-write Phase 1 bone-decomposition does not inherit literal slug strings into bone SVO events; flagged here, not faulted
      criteria: no fixer action required; /and-write is responsible for rendering these as elapsed-time or event-reference language

    # CHECK 1 — SUM-ROLLUP
    - id: fault-004
      type: pass
      what: scene-level axes_in_motion magnitudes summed against chapter contract targets
      why: political_register-prot: s01 +0.5 + s02 +0.5 + s03 +0.5 = +1.5 (target +1.5); moral_legibility_to_self: s02 +0.5 = +0.5 (target +0.5); social_tether-prot-collapse: s04 magnitude 1.5 direction down = -1.5 (target -1.5); position-prot-collapse: s04 magnitude 1.0 direction down = -1.0 (target -1.0); all four sums match the chapter contract within ±0 — no rollup error

    # CHECK 2 — NO-RANK-CLAIM-WITHOUT-DESCRIBED-CAUSE
    - id: fault-005
      type: pass
      what: every axis movement in every scene checked against chunk prose for described cause
      why: all six axis movements (political_register-prot ×3, moral_legibility_to_self ×1, social_tether-prot-collapse ×1, position-prot-collapse ×1) have chunk-prose causes; no axis movement is declared without a corresponding described event in the chunk body

    # CHECK 3 — COST-LEDGER CONSISTENCY
    - id: fault-006
      type: pass
      what: cost_ledger_anchor fields across all four scenes checked against chapter contract cost-ledger entries
      why: political_register-prot gain correctly anchors cl06 in s01, s02, s03; moral_legibility_to_self gain correctly anchors cl07a in s02; social_tether-prot-collapse cost correctly anchors cl07a in s04 (cl07a's cost side per contract); position-prot-collapse cost correctly anchors cl07b in s04; no misanchor found

    # CHECK 4 — THEMATIC-AXIS-UNDECLARED
    - id: fault-007
      type: pass
      what: chapter goal thesis axes checked against scene axes_in_motion/axes_held union
      why: goal thesis = contempt-completion (political_register-prot) + first non-suppressed recognition (moral_legibility_to_self); political_register-prot appears in axes_in_motion for s01, s02, s03; moral_legibility_to_self appears in axes_in_motion for s02; both thesis axes declared; THEMATIC-AXIS-UNDECLARED does not fire

    # CHECK 5 — STAKES-AXIS VALIDITY
    - id: fault-008
      type: pass
      what: each scene's scene_conflict.stakes_axis checked against that scene's axes_in_motion ∪ axes_held
      why: s01 stakes_axis=political_register-prot present in s01 axes_in_motion; s02 stakes_axis=moral_legibility_to_self present in s02 axes_in_motion; s03 stakes_axis=political_register-prot present in s03 axes_in_motion; s04 stakes_axis=social_tether-prot-collapse present in s04 axes_in_motion; all four valid

    # CHECK 6 — CHUNK-TAG WELL-FORMEDNESS
    - id: fault-009
      type: pass
      what: central event tagging in each scene's chunk prose
      why: s01 — [event: new-request-arrives-via-dead-drop] + [event: request-accounting-opens-contempt-color-arrives]; s02 — [event: accounting-catches-its-own-pattern] + [event: suppression-no-longer-fully-operational]; s03 — [event: request-execution-enacted] + [event: contempt-without-refusal-locked]; s04 — [event: ward-contact-stops-responding] + [event: witch-label-reached-upper-city-contact] + [event: tether-node-removed-architecture-still-running]; all central events are tagged with concrete [event:] markers; no scene has its central event buried in abstraction only

    # CHECK 7 — EARTH-BET FENCE
    - id: fault-010
      type: pass
      what: b01c19s02 chunk prose and notes checked for Worm-canon proper noun leak (Khepri, Gold Morning, cape-lore)
      why: the chunk uses shape-language throughout the pattern-naming beat; no Khepri-naming, no Gold Morning reference, no cape-lore terminology appears in either the chunk prose or the substance_delta notes; the EARTH-BET-FENCE holds; the inline "Shape-language only:" directive (see fault-001) is a process issue, not a lore leak

    # CHECK 8 — BARE SLUG META-REFERENCES (SIGNAL per audit brief)
    # already captured in fault-003 above as a flag; no additional entry needed
