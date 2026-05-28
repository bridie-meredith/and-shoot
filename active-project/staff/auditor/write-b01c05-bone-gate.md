```yaml
audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  phase: /and-write Phase 6 substance bone-gate
  bone_count: 34
  verdict: FINDINGS-PRESENT
  hard_count: 8
  signal_count: 1
  flag_count: 2

  findings:

    # ─────────────────────────────────────────────
    # HARD FINDINGS — block Phase 7 emit
    # ─────────────────────────────────────────────

    - id: fault-001
      type: fault
      severity: HARD
      class: FAULT-FORM-PERCEPTION
      bones: [b01c05s01n06, b01c05s01n09, b01c05s02n02, b01c05s02n08, b01c05s02n11, b01c05s03n09]
      what: >
        Six bones use "maps" as the Taylor-subject verb with an abstract noun as object:
        s01n06 "maps the provisioner-train interval",
        s01n09 "maps the message-runner gait-class",
        s02n02 "maps the courier gait-signature",
        s02n08 "maps the enforcement approach-geometry",
        s02n11 "maps the courier body-filing",
        s03n09 "maps the courier body-record".
        The objects in every case are cognitive/categorical abstractions, not physical spaces.
        "Maps" in this usage describes Taylor's internal categorization and logging process —
        the same semantic class as the banned verbs "noted", "measured", "tracked" in the
        bones schema §SVO discipline. These bones record the recognition/categorization act
        (interiority/perception), not an external physical observable.
      why: >
        Perception verbs with abstract objects route interiority into the bones layer,
        bypassing the facets that carry Taylor's cognition (narrator-interest, feeling).
        If these bones stand, the facet layer doubles up on the same cognitive content,
        producing redundancy the stitcher cannot resolve cleanly. Six uses across all three
        scenes means the interiority contamination is chapter-wide.
      criteria: >
        Each of the six bones must present a physical observable as its SVO. The
        categorization/logging act that "maps" describes must migrate to the narrator-interest
        or memory facet citing the physical bone. If no physical external act underlies the
        cognitive categorization at that beat, the bone is chatter and must be removed or
        replaced by the physical event that triggered the categorization.

    - id: fault-002
      type: fault
      severity: HARD
      class: FAULT-FORM-MODIFIER
      bones: [b01c05s02n03, b01c05s02n05, b01c05s02n06]
      what: >
        Three bones carry banned prepositional or adjectival modifiers:
        s02n03 "the three figures enter the side-alley off the east exit" —
          "off the east exit" is a prepositional phrase of source/location (schema: PP of
          place/direction/source explicitly banned);
        s02n05 "the three figures pin the courier against the stone" —
          "against the stone" is a prepositional phrase of location/instrument;
        s02n06 "the side-alley returns the effortful sound" —
          "effortful" is an adjective modifying "sound" (schema: "No adjectives, no adverbs,
          no prepositional padding").
      why: >
        Modifier violations accumulate as prose-surface contamination at the bones layer.
        The stitcher is designed to receive clean SVO and add texture from facets; modifiers
        baked into bones pre-empt facet authoring and create double-layering. The three
        affected bones are in the chapter's central incident scene (s02), where form
        discipline is load-bearing for the subsequent held-discipline read.
      criteria: >
        s02n03: strip "off the east exit" — the alley is sufficient destination. Any
        locational specificity belongs in the location-state facet or scene-map.
        s02n05: strip "against the stone" — "the three figures pin the courier" is the
        physical act; surface detail routes to sensory facet.
        s02n06: strip "effortful" — "the side-alley returns the sound" is the bone; the
        quality of the sound routes to the sensory or narrator-interest facet that cites
        this bone.

    - id: fault-003
      type: fault
      severity: HARD
      class: FAULT-FORM-INTERIORITY + FAULT-FORM-MODIFIER
      bones: [b01c05s03n07]
      what: >
        s03n07 "the courier-face surfaces in the rushwick replay" carries two concurrent
        faults:
        (1) FAULT-FORM-INTERIORITY: "the courier-face surfaces" in a "replay" is a
        memory-image arising — a cognitive/perceptual event occurring inside Taylor, not
        an external physical observable. There is no body in the room. The courier is not
        present. The face appearing is Taylor's recall, which is interiority by definition.
        (2) FAULT-FORM-MODIFIER: "in the rushwick replay" is a prepositional phrase of
        location/context (banned: PP of place/instrument).
      why: >
        A memory-image arising as a bone directly violates the schema's core rule: "Internal
        states are facets, not bones." If this bone stands, the facet layer (narrator-interest,
        memory) has no non-redundant home for the courier-face recognition — it will either
        duplicate the bone or cite an interiority bone, both of which corrupt the facet graph.
        This bone is in s03, the chapter's peak scene where cl-d05 anchors; interiority at
        this structural position is particularly disruptive.
      criteria: >
        The bone must present a physical external observable that grounds the courier-face
        beat. If Taylor's attention to the courier's physical body-file is the event, the
        bone should describe a physical action Taylor performs (e.g., the body-record or
        a physical artifact she handles). If there is no physical act, the courier-face
        beat is facet-only and this bone must be removed.

    - id: fault-004
      type: fault
      severity: HARD
      class: HELD-AXIS-NOT-WITNESSED
      bones: [b01c05s02 — no bone lists capability in axes_held]
      what: >
        Scene b01c05s02's substance_delta.axes_held includes "capability" with rationale
        "no new coverage expansion; Rushwick coverage operational." No bone in s02 lists
        capability in its bone-level axes_held. The twelve s02 bones' axes_held entries
        cover: political_register-prot (all), moral_framework (n01, n03, n04, n05, n06,
        n07, n08, n09, n10), relational_anchor_status (n11) — but capability does not
        appear on any s02 bone.
      why: >
        The held-axis-not-witnessed rule exists because a scene-level held declaration
        without a witnessing bone is structurally unverifiable — the facet layer has no
        bone to cite when authoring capability-related texture in s02. Downstream, the
        substance bone-gate for the book's aggregate capability hold cannot be confirmed
        against s02's contribution.
      criteria: >
        At least one s02 bone must list capability in its bone-level axes_held with a
        rationale that enacts the stillness-against-pressure discipline for that axis
        (coverage maintenance, no new extension, existing range confirmed active).

    - id: fault-005
      type: fault
      severity: HARD
      class: HELD-AXIS-NOT-WITNESSED
      bones: [b01c05s03 — no bone lists social_tether-prot-rise in axes_held]
      what: >
        Scene b01c05s03's substance_delta.axes_held includes "social_tether-prot-rise"
        with rationale "tether load-bearing in formation per c04; no new structural
        addition this scene." No bone in s03 lists social_tether-prot-rise in its
        bone-level axes_held. The thirteen s03 bones' axes_held entries cover:
        political_register-prot, capability (n01), moral_framework (n02, n08),
        relational_anchor_status (n07, n09), moral_legibility_to_self (n08, n10, n12,
        n13) — but social_tether-prot-rise does not appear on any s03 bone.
      why: >
        Same structural consequence as fault-004. The social_tether-prot-rise axis is
        chapter-level held, which means the chapter contributes to the book's aggregate
        tether-hold. Without a witnessing bone in s03, the facet layer has no cite-anchor
        for tether-texture in the chapter's peak scene. The tether axis is antagonist-
        tracked (Otto's non-extractable-formation pressure) and must be witnessed to
        carry downstream.
      criteria: >
        At least one s03 bone must list social_tether-prot-rise in its bone-level
        axes_held with a rationale that enacts the stillness-against-pressure discipline
        (tether formation load-bearing but no new structural addition).

    # ─────────────────────────────────────────────
    # SIGNAL FINDINGS — surfaced; disposition required
    # ─────────────────────────────────────────────

    - id: signal-001
      type: flag
      severity: SIGNAL
      class: REGISTER-AS-MANNERISM
      bones: [b01c05s01n06, b01c05s01n09, b01c05s02n02, b01c05s02n08, b01c05s02n11, b01c05s03n09]
      what: >
        "maps" as Taylor-subject verb appears 6 times across 34 bones (17.6% of the
        chapter's bone inventory). Each instance uses a distinct object (no single VERB
        OBJECT pair repeats ≥3 times), placing this below the strict per-pair threshold,
        but the verb-level frequency — 6 uses in a chapter-sized corpus — constitutes a
        mannerism pattern. The dispatch audit note flagged this pattern at 7+ uses in
        prior chapter passes. The 6-use count here confirms the pattern persists at
        chapter scope. Note: this signal partially overlaps fault-001 (if the "maps" bones
        are recast as physical observables, the mannerism is dissolved structurally).
      why: >
        A single verb dominating the Taylor-subject bone inventory will surface in the
        rendered prose as repetition the stitcher cannot vary without changing semantics.
        The pattern will be auditable at /and-review bones as a FREQUENCY-BAND flag.
      disposition: >
        Remediation is entailed by fault-001: recasting the six "maps" bones as physical
        observables dissolves the mannerism. If any "maps" bones survive fault-001 resolution
        (i.e., a physical recast retains "maps" as a licit physical verb in a specific
        instance), resurface for per-instance judgment. No independent fix action required
        beyond fault-001 resolution.

    # ─────────────────────────────────────────────
    # FLAG FINDINGS — non-blocking; advisory
    # ─────────────────────────────────────────────

    - id: flag-001
      type: flag
      severity: FLAG
      bones: [b01c05s03n10, b01c05s03n12]
      what: >
        s03n10 and s03n12 share an identical SVO: "taylor-hebert-kl-122ac runs the
        rushwick flat-read." The bones schema does not explicitly prohibit duplicate SVOs,
        and the bone notes explain that the repetition is load-bearing (second attempt
        enacts foreclosure confirmation). The substance_delta rationales distinguish them
        (foreclosure bone 1 vs. foreclosure bone 3). However, two bones with identical
        SVO strings with no distinguishing surface element create ambiguity for downstream
        renderers: flat_id is the only differentiator visible in the bones file.
      why: >
        The stitcher receives a bones file with flat_ids; if it encounters two identical
        SVOs, it may render one and treat the other as a duplicate, losing the second-pass
        load-bearing narrative beat. This is a renderer-ambiguity risk, not a schema
        violation.
      criteria: null

    - id: flag-002
      type: flag
      severity: FLAG
      bones: [b01c05s03n03]
      what: >
        s03n03 "the Hook-feed resolves" uses "resolves" as an intransitive completion
        verb. The bones schema's non-action verb list includes stative verbs; "resolves"
        describes a state attained (the feed having completed processing) rather than a
        discrete physical act an observer would see. It is analogous to the disallowed
        stative position-naming uses of "lies/sits/stands." The intransitive-lands-cleanly
        exception ("taylor exhales") was written for biological/physiological events, not
        abstract-system completions.
      why: >
        If the bone is treated as a FAULT-FORM-NON-ACTION-VERB at /and-review bones,
        fixer will need to recast. The downstream consequence is bounded (one bone in the
        s03 baseline comparison sequence), but the comparison structure (Hook resolves /
        Rushwick does not) is narratively load-bearing for the foreclosure arc. A recast
        that loses the contrast risks disrupting s03's dramatic shape.
      criteria: null

  # ─────────────────────────────────────────────
  # PASS CONFIRMATIONS (summary)
  # ─────────────────────────────────────────────
  pass_confirmations:
    - check: bone_count_in_range
      result: PASS
      note: "34 bones; chapter target 15-75"
    - check: axis_delta_delivered_s01
      result: PASS
      note: "s01 axes_in_motion empty; bone-Δ sum 0; exact"
    - check: axis_delta_delivered_s02
      result: PASS
      note: "s02 axes_in_motion empty; bone-Δ sum 0; exact"
    - check: axis_delta_delivered_s03
      result: PASS
      note: "s03 political_register-prot delivered +1.5 (s03n06); target +1.5; exact"
    - check: cost_ledger_paid_cl-d05
      result: PASS
      note: "cl-d05 paid at s03n06 axis_moves; chapter-anchor resolved"
    - check: bonefide_s03n06
      result: PASS
      note: "stopping the rushwick-pass is the physical anchor for recognition/foreclosure; cessation IS the event the +1.5 Δ lives in; bonefide confirmed"
    - check: stakes_axis_in_union_all_scenes
      result: PASS
      note: "s01 political_register-prot in axes_held; s02 moral_framework in axes_held; s03 political_register-prot in axes_in_motion"
    - check: opposing_force_visible_all_scenes
      result: PASS
      note: "s01 n09 rationale names novel weight directly (held-discipline satisfaction); s02 n04/n05 rationale names enforcement specificity; s03 n05/n06 rationale names accumulation-without-label"
    - check: sensory_grounding_all_scenes
      result: PASS
      note: "s01 n01 geography; s02 n01 courier entry; s03 n01 room-floor"
    - check: event_map_bones_present
      result: PASS
      note: "all bones named in event_map entries exist in post-trim bone set"
    - check: chunk_tag_completeness_all_scenes
      result: PASS
      note: "all [event:]/[image:]/[force:]/[mechanism:] tags in s01/s02/s03 chunk text have corresponding event_map entries"
    - check: holds_license_s03n11_s03n13
      result: PASS
      note: "both bones satisfy condition 2 (physical object resisting pressure); PP-free; licensed"
    - check: held_axis_witnessed_s01
      result: PASS
      note: "political_register-prot, capability, moral_framework, relational_anchor_status all witnessed in s01 bones"
    - check: held_axis_witnessed_s03_all_except_social_tether
      result: PASS
      note: "moral_framework, capability, relational_anchor_status, moral_legibility_to_self all witnessed; social_tether-prot-rise not witnessed (fault-005)"
    - check: worm_canon_soft_watch_structural_distinctness
      result: PASS
      note: "s02 courier gait (n02) + approach-geometry read (n04/n08) + filing (n11) are structurally distinct bones; SOFT-WATCH carried from chunk review resolved"
    - check: dialogue_anchor_bones
      result: PASS
      note: "no dialogue_anchor: true bones in the set; all dialogue_anchor fields are false; no FAULT-DIALOGUE-MISSING-AT-ANCHOR applicable"
    - check: per_scene_delta_sum_not_underdelivered
      result: PASS
      note: "no underdelivery; s03 delivered exactly target; N/A for s01/s02 (no axes_in_motion)"
```
