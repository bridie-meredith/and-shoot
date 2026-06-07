audit:
  scope: chapter
  target: b01c07
  timestamp: 2026-05-30
  phase_coverage: [Phase-2-constraint, Phase-5-continuity, Phase-6-bone-gate]
  source_files:
    bones_draft: active-project/staff/showrunner/_drafts/b01c07-bones-draft-2026-05-30.md
    dialogue_halvard: active-project/theater/dialogue/septon-halvard-flea-bottom.md
    dialogue_taylor: active-project/theater/dialogue/taylor-hebert-kl-122ac.md
    contract: active-project/staff/showrunner/memory.md § b01c07 block
    schema: schemas/bones.schema.md

  summary:
    headline: "FINDINGS-PRESENT — HARD: 4"
    phase_2_findings: 4 HARD, 1 SIGNAL
    phase_5_findings: 1 FLAG
    phase_6_findings: 2 HARD, 1 SIGNAL
    total_hard: 6
    total_signal: 2
    total_flag: 1
    bone_gate_verdict: FAIL

  # ─────────────────────────────────────────────────────────────────
  # PHASE 2 — CONSTRAINT AUDIT (SVO form + schema + Earth-Bet fence)
  # ─────────────────────────────────────────────────────────────────

  findings:

    - id: fault-001
      type: fault
      phase: 2
      class: FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY
      bone: b01c07s02n06
      what: |
        SVO: "the compound-corruption thesis lands"
        Subject is an abstraction ("the compound-corruption thesis"). Verb "lands" is used here in its
        metaphorical sense — "thesis lands on Taylor" — not as a concrete physical act observable by
        a witness. The object is absent (intransitive abstract-arrival). This bone describes an interior
        reception event, not an observable physical action. Under schema rules: "Abstraction-as-object
        is INTERIORITY" (bones.schema.md §SUBJECT VERB OBJECT) and the schema also forbids stative
        position-naming. "lands" as metaphor-for-cognitive-impact is interiority routed through a
        passive-reception SVO that has no physical-world referent.
      why: |
        This bone is the chapter's designated thesis-landing beat — the WATCH-2 causality-gap closure
        bone, the beat that makes Taylor's genuine engagement motivated rather than asserted. If the bone
        cannot stand as a concrete SVO, /and-facets cannot cite it as a real physical anchor; the
        narrator-interest facet that must carry the causality resolution will be floating without a
        genuine bones anchor. EVENT-NOT-CONCRETE is a HARD at Phase 6 (see fault-007 below for the
        Phase 6 classification of this same bone); this Phase 2 finding names the form violation
        independently.
      criteria: |
        The bone at this position must record a concrete, physically-observable act by a named subject.
        The thesis-landing as Taylor's cognitive event is facet material (narrator-interest), not bone
        material. The bone must record an observable action — Taylor's physical posture, movement, or
        enacted response that signals engagement — that the narrator-interest facet can then cite as
        the physical anchor for the interior landing. The abstract "thesis lands" form cannot stand.

    - id: fault-002
      type: fault
      phase: 2
      class: FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY
      bone: b01c07s02n07
      what: |
        SVO: "taylor-hebert-kl-122ac turns the thesis"
        "turns" is used here in its cognitive/evaluative sense — "turns it over mentally" — not as a
        concrete physical rotation. The object ("the thesis") is an abstraction. Under schema rules:
        "Abstraction-as-object is INTERIORITY" (bones.schema.md §Subject Verb Object) — "taylor carries
        the weight" / "taylor turns the thesis" are explicitly named as thought-figures, not events.
        FAULT-FORM-INTERIORITY.
        Additionally, this is the moving bone where political_register-prot advances +0.3. A moving bone
        whose SVO is an interiority-form cannot witness its own axis movement per Phase 6 rules (the
        MOVING bone must be a concrete actor-verb-object). This doubles as a Phase 6 SUBSTANCE-FLAT
        (see fault-008 below); the form fault is named here independently.
      why: |
        The +0.3 political_register-prot move depends on this bone being a concrete SVO that witnesses
        the articulation-demand. If the bone is an interiority form, the axis-move has no concrete
        witness and becomes SUBSTANCE-FLAT-political_register-prot. Downstream: /and-facets narrator-
        interest cannot cite an interiority bone as a physical anchor; /and-stitch will render an
        abstraction at what should be a sharpening beat.
      criteria: |
        The bone must be recast as a concrete physical act by taylor-hebert-kl-122ac that an observer
        would see or hear — an act whose SVO object is a physical-world entity, not "the thesis." The
        evaluative cognitive turning is narrator-interest facet material. The bone records the observable
        act (e.g., a physical gesture, a posture change, a verbal act if a speech bone is appropriate,
        a return gaze, any concrete enacted response to the argument) that the facet then glosses as
        "taking the argument seriously." The axis-move must be witnessed by the concrete SVO.

    - id: fault-003
      type: fault
      phase: 2
      class: FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY
      bone: b01c07s03n04
      what: |
        SVO: "the named death lands"
        Same interiority-form violation as fault-001. Subject is "the named death" (an abstraction);
        verb "lands" is metaphorical cognitive-impact. No concrete physical act is present. Per schema:
        abstraction-as-subject driving a metaphorical arrival verb is a FAULT-FORM-INTERIORITY pattern.
        Compare the explicit schema example: "the yard holds the silence" → FAULT-FORM-INTERIORITY.
        "The named death lands" is structurally identical: abstract subject, non-physical verb, no object.
      why: |
        This bone is tagged in the event_map as "[image: named-death-as-ledger-entry]" — it is meant
        to ground the chapter's WATCH-1 concrete-death beat. An interiority form at this position means
        the image tag has no physical-world anchor. /and-stitch Phase 8.5 central-event-muffle check
        (armed by PASS-CHUNK-VOICE-RISK) specifically scrutinizes whether the named-death renders
        concrete. An interiority bone here means the muffle check will fire on the concrete-event test.
      criteria: |
        The bone must be recast as a concrete observable act — either a physical response by Halvard
        (absorbing, receiving, going still, whatever he physically does when the named death lands) or
        by Taylor (completing the act of naming, placing the ledger-entry, speaking the person's name
        to Halvard). The interior quality of the impact is narrator-interest material; the bone records
        the physical event from which that impact can be inferred.

    - id: fault-004
      type: fault
      phase: 2
      class: FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY
      bone: b01c07s03n09
      what: |
        SVO: "the argument completes"
        Subject is an abstraction ("the argument"); verb "completes" is stative-terminative describing
        a cognitive/social state, not a concrete observable physical act. No actor is performing an
        observable action. This is the moving bone for social_tether-prot-rise +0.5 in s03 — the
        scene's single axis-move witness. An interiority/abstraction form at the chapter's second
        tether-deepening bone means this axis move has no concrete witness.
      why: |
        social_tether-prot-rise +0.5 at s03n09 is the second half of the chapter's +1.0 tether target.
        SUBSTANCE-FLAT-social_tether-prot-rise fires when the moving bone cannot be witnessed by its
        own SVO. The tether-deepening at b01c07 is one of the chapter's two in-motion axes; if the
        witness bone is an interiority form, the entire s03 tether increment is unwitnessed and the
        Phase 6 bone-gate must reject it as HARD. This also means the chapter's social_tether total
        +1.0 is only 50% witnessed (s02n10 "taylor-hebert-kl-122ac stays in the argument" is
        physically-observable; s03n09 is not), producing a SUBSTANCE-FLAT finding at the chapter level.
      criteria: |
        The bone must be recast as a concrete physically-observable act by a named actor that an observer
        could witness as a social-embedding event — the physical act that constitutes both parties having
        completed the argument rather than merely closed it. The cognitive/social quality of "completion
        vs. closure" is narrator-interest material; the bone records the physical act (e.g., a leave-taking
        gesture, a moment of mutual stillness, Taylor's physical departure, Halvard's response) from which
        the completion-not-closure can be inferred.

    - id: signal-001
      type: flag
      phase: 2
      class: FAULT-FORM-NON-ACTION-VERB (borderline; promoted to SIGNAL for review)
      bone: b01c07s02n12
      what: |
        SVO: "the exchange continues without resolution"
        Subject is an abstraction ("the exchange"); verb "continues" is stative-durational; "without
        resolution" is a negation modifier. The schema bans negation forms (FAULT-FORM-NEGATION) and
        non-action verbs ("continues" in this stative-durational sense). The bone is a held bone in a
        scene that has already moved its axes; it carries no axis-move and is described as
        [mechanism: engagement-without-resolution]. However: held bones are permitted to record
        observable-state-continuations if the SVO is a concrete observable act. "The exchange continues"
        is not. It is an abstraction narrating a state.
        Classified SIGNAL rather than HARD because (a) the bone is held/non-moving and (b) the mechanism
        tag it carries is genuinely load-bearing for /and-facets context-weave. The violation is real;
        the downstream damage is lower than the moving-bone violations.
      why: |
        /and-facets will attempt to cite this bone as a physical anchor for the [mechanism: engagement-
        without-resolution] event. If the SVO is not a concrete observable act, the citation will
        reference an abstraction. SIGNAL because the bone is held and the fix is a recast to a concrete
        equivalent (e.g., a physical act of waiting, the silence, a gesture).
      criteria: null

  # ─────────────────────────────────────────────────────────────────
  # PHASE 5 — CONTINUITY AUDIT (c06 handoff_out → c07 handoff_in)
  # ─────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      phase: 5
      class: continuity-advisory
      what: |
        b01c06 handoff_out records Taylor's moral_legibility_to_self rank as 5 (via chapter
        substance_delta_measured: moral_legibility_to_self +1.0 from rank 4 to 5 notional post-c06,
        though the handoff_out character_state says "moral_legibility rank 5" explicitly). b01c07
        handoff_in states "moral_legibility rank 5." This is consistent. However, the b01c06
        substance_delta shows moral_legibility_to_self as a +0.5 planned advance in the chapter
        contract while the actual bone-gate delivered +1.0 (noted in substance_delta_measured as
        "+1.0" with a Phase 6 SIGNAL disposition for "mls +0.5→+1.0 overdelivery"). The b01c07
        contract treats moral_legibility_to_self as held at rank 5, which matches the handoff_out
        rank 5 — so the overdelivery was absorbed into rank 5 and the c07 contract is internally
        consistent. No fault; minor reconciliation note.
        Geography and timeline: "sept corner / Flea Bottom Hook; two months on" — matches handoff_out
        "KL 122 AC; arrangement two months functional." Halvard "latent → active" — bones confirm
        Halvard appears in s01 and speaks in s02/s03. Wren anchor rank 3 confirmed (handoff_out:
        anchor rank 3). political_register-prot rank 2.5 confirmed (handoff_out character_state).
        social_tether-prot-rise rank 3 confirmed at s01 entry (handoff_out rank 3 + chapter's +1.0
        target = rank 4 at handoff_out, consistent with the chapter's delivered total).
        All continuity checks pass. This flag is advisory only.
      why: |
        The c06 moral_legibility overdelivery (+0.5 planned, +1.0 delivered) lands as a rank-5 absorb
        that leaves no visible inconsistency at c07. But it creates a fractional ambiguity in the
        series roll-up (is the post-c06 rank 4.5 or 5?). The c07 contract treats it as 5. That is
        acceptable under the ±1 tolerance in chunk_targets but should be noted for the book-level
        /and-review verdict roll-up.
      criteria: null

  # ─────────────────────────────────────────────────────────────────
  # PHASE 6 — SUBSTANCE BONE-GATE
  # ─────────────────────────────────────────────────────────────────

  # --- EVENT-NOT-CONCRETE verdicts ---
  event_not_concrete_verdicts:

    central_event_bones:
      - bone: b01c07s03n01
        svo: "taylor-hebert-kl-122ac names the body count"
        verdict: PASS
        rationale: |
          Concrete SVO. Named actor (taylor-hebert-kl-122ac), physical-vocal verb (names),
          concrete object (the body count). Observable: someone watching would see/hear Taylor
          deliver a statement. This is also the +0.2 political_register-prot moving bone and
          its SVO witnesses the axis-move by recording the articulation-demand being executed.

      - bone: b01c07s03n02
        svo: "taylor-hebert-kl-122ac speaks to septon-halvard-flea-bottom"
        verdict: PASS
        rationale: |
          Canonical speech form per schema (speaker speaks to listener). Dialogue-anchor bone.
          Concrete and schema-compliant. The dialogue content at [taylor-hebert-kl-122ac:1]
          delivers the specific-body naming (Wenna Cobb, Pig-Tallow Lane, fever two years
          back, eleven-day failure, maester-call-not-routed). WATCH-1 honored at this speech
          bone + the dialogue file. PASS.

      - bone: b01c07s03n03
        svo: "taylor-hebert-kl-122ac names the specific body"
        verdict: PASS
        rationale: |
          Concrete SVO. Named actor, action-verb (names), concrete object (the specific body).
          Post-speech follow-through on the n02 dialogue anchor. The WATCH-1 evidentiary
          precision (specific person in the ledger, not the category) is carried here as a
          concrete held bone. PASS.

      - bone: b01c07s03n04
        svo: "the named death lands"
        verdict: FAIL — EVENT-NOT-CONCRETE (HARD)
        rationale: |
          Abstract subject ("the named death"), metaphorical-cognitive verb ("lands" in the
          sense of "registers with impact"), no concrete physical object. A witness cannot
          observe "the named death landing." This is an interiority-form bone at a central-event
          position. Covered by fault-003 above. HARD.

      - bone: b01c07s02n06
        svo: "the compound-corruption thesis lands"
        verdict: FAIL — EVENT-NOT-CONCRETE (HARD)
        rationale: |
          Abstract subject ("the compound-corruption thesis"), metaphorical-cognitive verb
          ("lands"), no physical-world object. Same structure as fault-003. This is the
          chapter's thesis-reception beat — load-bearing for WATCH-2 causality — and it
          is an interiority form. HARD. Covered by fault-001 above.

      - bone: b01c07s02n07
        svo: "taylor-hebert-kl-122ac turns the thesis"
        verdict: FAIL — EVENT-NOT-CONCRETE (HARD) + SUBSTANCE-FLAT-political_register-prot
        rationale: |
          Named actor (pass) but object "the thesis" is an abstraction, and "turns" is used
          in the cognitive-evaluative sense ("turns it over mentally"). An observer cannot
          watch Taylor "turn the thesis." FAULT-FORM-INTERIORITY. This is also the +0.3
          moving bone for political_register-prot — a moving bone whose SVO is an interiority
          form cannot witness its own axis movement. SUBSTANCE-FLAT-political_register-prot.
          HARD. Covered by fault-002 above.

      - bone: b01c07s03n09
        svo: "the argument completes"
        verdict: FAIL — EVENT-NOT-CONCRETE (HARD) + SUBSTANCE-FLAT-social_tether-prot-rise
        rationale: |
          Abstract subject ("the argument"), stative-terminative verb ("completes"), no
          concrete physical-world object. Not observable. This is the +0.5 moving bone for
          social_tether-prot-rise in s03. A moving bone whose SVO is an interiority/abstraction
          form cannot witness its own axis movement. SUBSTANCE-FLAT-social_tether-prot-rise.
          HARD. Covered by fault-004 above.

  # --- ABSTRACTION-DOMINANCE per-scene ratios ---
  abstraction_dominance:
    note: |
      Threshold: ≥25% physically-grounded bones per scene (concrete physical-action bones /
      total scene bones). This chapter is PASS-CHUNK-VOICE-RISK / seminar-risk — the ratio
      check matters here.
    method: |
      "Concrete physical-action" = bone whose SVO records an observable physical act by a
      named entity: motion, physical gesture, speaking, blocking, physical-world state change.
      Excluded from "concrete": bones whose SVO subject is an abstraction, or whose verb is
      cognitive/evaluative/stative regardless of subject.

    scene_01:
      total_bones: 11
      concrete_physical_bones:
        - b01c07s01n01: "taylor-hebert-kl-122ac completes the ward-coverage circuit" — CONCRETE (motion/action)
        - b01c07s01n02: "the insect-feed returns" — borderline (feed-action; physical-world entity acting); COUNTED
        - b01c07s01n03: "the handcart blocks the sept-corner passage" — CONCRETE (physical obstruction)
        - b01c07s01n04: "septon-halvard-flea-bottom faces the handcart man" — CONCRETE (physical orientation act)
        - b01c07s01n05: "taylor-hebert-kl-122ac pauses at the sept-corner" — CONCRETE (motion halt)
        - b01c07s01n06: "septon-halvard-flea-bottom names the sick child" — CONCRETE (speech/naming act)
        - b01c07s01n08: "the insect-feed places septon-halvard-flea-bottom" — borderline; COUNTED (feed-action locating)
        - b01c07s01n09: "the handcart clears the passage" — CONCRETE (physical movement)
        - b01c07s01n10: "taylor-hebert-kl-122ac enters the sept-corner" — CONCRETE (motion)
        - b01c07s01n11: "taylor-hebert-kl-122ac acknowledges septon-halvard-flea-bottom" — CONCRETE (enacted gesture/nod)
      non_concrete:
        - b01c07s01n07: "taylor-hebert-kl-122ac receives the plain acknowledgment" — borderline cognitive-reception; EXCLUDED
      concrete_count: 10
      ratio: "10/11 = 91%"
      verdict: PASS (well above 25% threshold)

    scene_02:
      total_bones: 14
      concrete_physical_bones:
        - b01c07s02n01: "septon-halvard-flea-bottom describes the fever's progress" — CONCRETE (speech act)
        - b01c07s02n02: "taylor-hebert-kl-122ac remains at the sept-corner" — CONCRETE (positional act; enacted staying)
        - b01c07s02n03: "septon-halvard-flea-bottom names the maester's cost" — CONCRETE (speech/naming)
        - b01c07s02n04: "septon-halvard-flea-bottom turns from the sick-child account" — CONCRETE (physical pivot/redirection)
        - b01c07s02n05: "septon-halvard-flea-bottom speaks to taylor-hebert-kl-122ac" — CONCRETE (canonical speech form)
        - b01c07s02n10: "taylor-hebert-kl-122ac stays in the argument" — CONCRETE (enacted positional hold; physically observable)
        - b01c07s02n11: "septon-halvard-flea-bottom holds the silence" — CONCRETE (licensed stillness-against-pressure form)
        - b01c07s02n13: "taylor-hebert-kl-122ac releases the rebuttal" — borderline (cognitive release); EXCLUDED
        - b01c07s02n14: "the sept-corner ground grips" — CONCRETE (physical sensory-grounding bone; place-action)
      non_concrete (interiority/abstraction):
        - b01c07s02n06: "the compound-corruption thesis lands" — INTERIORITY (fault-001/007)
        - b01c07s02n07: "taylor-hebert-kl-122ac turns the thesis" — INTERIORITY (fault-002/008)
        - b01c07s02n08: "taylor-hebert-kl-122ac reads the thesis for structural soundness" — INTERIORITY (perception-cognitive)
        - b01c07s02n09: "taylor-hebert-kl-122ac locates the rebuttal" — INTERIORITY (cognitive location)
        - b01c07s02n12: "the exchange continues without resolution" — ABSTRACTION (signal-001)
        - b01c07s02n13: also excluded above
      concrete_count: 8 (n01, n02, n03, n04, n05, n10, n11, n14)
      ratio: "8/14 = 57%"
      verdict: PASS (57% > 25% threshold)
      note: |
        The 4 interiority/abstraction bones (n06, n07, n08, n09) form a consecutive cognitive
        block in the scene's middle third, which is the seminar-risk zone. While the overall
        ratio passes, the concentration of non-concrete bones at the argument's core is the
        mechanism behind the PASS-CHUNK-VOICE-RISK classification. The concrete bones (n10,
        n11, n14) at scene-close bring the ratio above threshold. ABSTRACTION-DOMINANCE SIGNAL
        is nonetheless noted for this zone: the n06-n09 block is 4 consecutive non-concrete bones
        at the chapter's argumentative heart. The HARD faults on n06 and n07 must be resolved;
        the recast will affect this ratio positively.

    scene_03:
      total_bones: 13
      concrete_physical_bones:
        - b01c07s03n01: "taylor-hebert-kl-122ac names the body count" — CONCRETE (naming/speech act)
        - b01c07s03n02: "taylor-hebert-kl-122ac speaks to septon-halvard-flea-bottom" — CONCRETE (canonical speech)
        - b01c07s03n03: "taylor-hebert-kl-122ac names the specific body" — CONCRETE (naming act)
        - b01c07s03n05: "septon-halvard-flea-bottom absorbs the counter" — borderline (physical reception stance); COUNTED
        - b01c07s03n06: "septon-halvard-flea-bottom speaks to taylor-hebert-kl-122ac" — CONCRETE (canonical speech)
        - b01c07s03n08: "taylor-hebert-kl-122ac remains at the sept-corner" — CONCRETE (enacted positional hold)
        - b01c07s03n10: "taylor-hebert-kl-122ac leaves the sept-corner" — CONCRETE (motion/departure)
        - b01c07s03n11: "the sept-corner lane holds the cold" — CONCRETE (sensory-grounding; physical place-state)
        - b01c07s03n13: "taylor-hebert-kl-122ac clears the Hook" — CONCRETE (motion)
      non_concrete (interiority/abstraction):
        - b01c07s03n04: "the named death lands" — INTERIORITY (fault-003)
        - b01c07s03n07: "the two accountings sit" — ABSTRACTION (subject=abstract plural; "sit" stative)
        - b01c07s03n09: "the argument completes" — ABSTRACTION (fault-004)
        - b01c07s03n12: "the argument remains available" — ABSTRACTION ("remains" stative; abstract subject)
      concrete_count: 9
      ratio: "9/13 = 69%"
      verdict: PASS (69% > 25% threshold)
      note: |
        s03n07 ("the two accountings sit") and s03n12 ("the argument remains available") are
        stative-abstraction forms that are not counted as concrete. Neither is a moving bone.
        They are not the most egregious violations but both use "sit" / "remains" in stative-
        position senses the schema bans under FAULT-FORM-NON-ACTION-VERB. These are not HARD
        (neither is a moving bone) but are flagged as advisory for /and-write recast.

  # --- SENSORY-GROUNDING quota (HARD: ≥1 per scene) ---

    - id: fault-005
      type: pass
      phase: 6
      class: SENSORY-GROUNDING
      what: |
        s01: b01c07s01n03 "the handcart blocks the sept-corner passage" — concrete place-situated
        physical action. QUOTA MET.
        s02: b01c07s02n14 "the sept-corner ground grips" — physical sensory-grounding bone explicitly
        designated and structurally grounded (cold stone, chandler's storefront, lane-sound per
        rationale). QUOTA MET.
        s03: b01c07s03n11 "the sept-corner lane holds the cold" — physical environmental grounding.
        "holds" here is borderline: per the schema, "holds" is licensed only for (1) body-part
        stillness-against-pressure or (2) physical-object resisting pressure. "The lane holds the
        cold" uses "holds" in a containment/stative sense ("the lane holds [contains] the cold"),
        which the schema classifies as FAULT-FORM-NON-ACTION-VERB under "Containment: contains,
        houses, occupies, inhabits". However, this bone is designated as the sensory-grounding
        quota bone — it is a sensory-grounding quota PASS at the intent level, though the SVO
        form needs recast. Marking as PASS for grounding-quota purposes with a note that the
        SVO form must be revised to a concrete physical-world equivalent (e.g., "the lane-cold
        grips the sept corner" or "the lane-stone holds" where "holds" is structural resistance).
      why: Grounding quota met across all three scenes. Not a blocking HARD on quota.
      criteria: null
      note: |
        ADVISORY: b01c07s03n11 SVO "the sept-corner lane holds the cold" uses "holds" in the
        containment sense (FAULT-FORM-NON-ACTION-VERB per schema §Narrow holds license). The bone
        is a held non-moving bone so this is not a SUBSTANCE-FLAT finding, but the form should be
        recast in /and-write to a concrete physical-world equivalent. Classified here as advisory
        within the PASS verdict rather than as a standalone fault because (a) the bone is non-moving,
        (b) the grounding intent is clear, and (c) this does not block the gate independently.

  # --- DIALOGUE CHECKS (HARD) ---

    - id: fault-006
      type: pass
      phase: 6
      class: DIALOGUE-COVERAGE
      what: |
        Anchor bones requiring dialogue citations:
        - b01c07s02n05 (septon-halvard-flea-bottom speaks to taylor-hebert-kl-122ac) → [septon-halvard-flea-bottom:1]
        - b01c07s03n02 (taylor-hebert-kl-122ac speaks to septon-halvard-flea-bottom) → [taylor-hebert-kl-122ac:1]
        - b01c07s03n06 (septon-halvard-flea-bottom speaks to taylor-hebert-kl-122ac) → [septon-halvard-flea-bottom:2]
        All three are confirmed in the dialogue files:
          septon-halvard-flea-bottom.md: entry 1 @b01c07s02n05 (errand-man compound-corruption thesis)
          taylor-hebert-kl-122ac.md: entry 1 @b01c07s03n02 (Wenna Cobb counter-argument)
          septon-halvard-flea-bottom.md: entry 2 @b01c07s03n06 (cost-acknowledgment; no retraction)
        DIALOGUE-MISSING-AT-ANCHOR: NONE. Coverage PASS.
      why: All three dialogue-anchor bones have corresponding citable utterances. PASS.
      criteria: null

    - id: fault-007
      type: pass
      phase: 6
      class: DIALOGUE-CARD-COMPLIANCE (Earth-Bet fence)
      what: |
        Earth-Bet proper-noun fence check across all three dialogue entries:
        septon-halvard-flea-bottom.md entry 1: No Earth-Bet proper nouns. Vocabulary is fully
        Westerosi in register ("Lane man," "bread, not coin," "house," "debt," "interest accumulates").
        CLEAN.
        taylor-hebert-kl-122ac.md entry 1: No Earth-Bet proper nouns. "Wenna," "Pig-Tallow Lane,"
        "the Hook," "maester-call," "fever season two years back" — fully Westerosi and KL-local
        register. "The account has to carry the interval" — Taylor's moral-ledger idiom is generic,
        not parahuman-vocabulary. CLEAN.
        septon-halvard-flea-bottom.md entry 2: No Earth-Bet proper nouns. CLEAN.
        FAULT-DIALOGUE-EARTH-BET-FENCE: NONE. PASS.
      why: Earth-Bet fence honored in all dialogue. PASS.
      criteria: null

    - id: fault-008
      type: pass
      phase: 6
      class: DIALOGUE-OBJECTIVE-MATCHED
      what: |
        Objective alignment check:
        septon-halvard-flea-bottom.md entry 1 | objective: "name what is wrong with the Lane man's
        arrangement, working it through honestly, not aimed at Taylor" → content delivers exactly
        this: Halvard describes the errand-man's bread-payment arrangement, arrives at the compound-
        corruption thesis (debt doesn't gather from the slow refusal), does not address Taylor. MATCH.
        taylor-hebert-kl-122ac.md entry 1 | objective: "deploy the counter by naming the specific
        cost the slower method already exacted — the body that justifies the arrangement" → content
        delivers: Wenna Cobb, Pig-Tallow Lane, fever season, eleven-day fever death, maester-call
        not routed, "She's why I'm in Flea Bottom at all." MATCH (strong; WATCH-1 concreteness honored:
        name + street + failure-mechanism present).
        septon-halvard-flea-bottom.md entry 2 | objective: "acknowledge the cost of his own position
        honestly without retracting it or claiming she is wrong" → content delivers: "I know the slow
        way has a cost... I've buried by the slow way before... I haven't an answer that makes your
        dead breathe. I've only the one I can live beside." MATCH. Does not retract; does not claim
        Taylor is wrong. PASS.
        FAULT-DIALOGUE-OBJECTIVE-MISSING: NONE. PASS.
      why: All three dialogue entries deliver their licensed speech-act objectives. PASS.
      criteria: null

  # --- Speech-bone form check (per schema §Dialogue-anchor bones) ---
    - id: fault-009
      type: pass
      phase: 6
      class: SCHEMA-SPEECH-BONE-COMMUNICATION-AXIS
      what: |
        Per schema: speech bones must move at least one communication-class axis. Checking the three
        speech bones:
        b01c07s02n05 (Halvard speaks): shape=held; no axis_moves. The speech bone's axes_held lists
        social_tether-prot-rise as held (not moved). The schema states: "speech bones must move at
        least one communication-class axis (community / knowledge / reputation / trust) per the
        substance bone-gate; speech bones whose substance_delta lists only physical-action axes are
        malformed." The parking-lot ruling at pl-2026-05-30-003 states: "relational_anchor_status
        and social_tether-prot-rise ARE this project's communication-class axes." The speech bone
        holds social_tether-prot-rise (pre-deepening) with the explanation that the tether-move
        fires at n10. The schema makes no explicit exception for a held speech bone when the
        communication-class axis fires at a different bone in the same scene; the design intent
        appears to be that Halvard's speech is the setup for the tether-deepening, not the
        tether-deepening itself. This is borderline. The pl-2026-05-30-003 ruling designates
        social_tether-prot-rise as a communication-class axis for this project. A held speech bone
        with a held communication-class axis is technically compliant with "social_tether is present
        in axis_held" — the schema says moves AT LEAST ONE but holding a communication-axis while
        signaling its pre-move status may satisfy the presence requirement. Classified PASS with note.
        b01c07s03n02 (Taylor speaks): shape=held; axes_held includes political_register-prot (post-
        move hold after n01's +0.2 move) and social_tether-prot-rise (pre-move). The +0.2 move fires
        at n01 not n02 — the speech bone carries the post-move hold on political_register-prot. This
        is consistent with the sub-firing structure. PASS.
        b01c07s03n06 (Halvard speaks): shape=held; axes_held includes social_tether-prot-rise (pre-
        move at rank 3.5). Same structure as s02n05. PASS with same borderline note.
      why: No FAULT-DIALOGUE-CARD-VIOLATION found. PASS.
      criteria: null

  # --- OPPOSING-FORCE-VISIBLE ---

    - id: fault-010
      type: pass
      phase: 6
      class: OPPOSING-FORCE-VISIBLE
      what: |
        s01: Opposing force = Halvard's plain-contact register vs. Taylor's ledger-discipline.
        Enacted in: n04 (Halvard faces the handcart man — his social engagement in action), n06
        (Halvard names the sick child — the plain-acknowledgment register made concrete), n08
        (insect-feed places Halvard — the surveillance architecture encountering someone it cannot
        categorize in relational terms). Force visible through enacted bones. PASS.
        s02: Opposing force = Halvard's principled-slower thesis as the argument Taylor cannot
        dismiss. Enacted in: n05 (Halvard speaks — the thesis delivered through the speech anchor),
        n11 (Halvard holds the silence — the not-pressing that confirms he is not manipulating).
        NOTE: n06 ("the compound-corruption thesis lands") is a HARD fault (fault-001/EVENT-NOT-
        CONCRETE) — this means the thesis-landing bone itself is non-concrete and the opposing
        force's moment of impact has no valid physical anchor. The opposing force is visible in
        the delivery (n05) but its landing-effect is not validly witnessed at bone level. The
        opposing-force-visible check passes on delivery; the landing is broken at the form level.
        s03: Opposing force = Halvard's sustained thesis / no-retraction. Enacted in: n05
        (Halvard absorbs the counter without dismissal), n06 (Halvard speaks — acknowledges cost,
        does not retract). PASS; both bones are concrete speech/action forms.
      why: Opposing force visible in all three scenes, though the s02 landing bone (n06) is non-
           concrete and will require recast per fault-001. The force-presence itself passes.
      criteria: null

  # --- AXIS-MOVEMENT VERIFICATION (per-bone + scene-aggregate Δ) ---

    - id: fault-011
      type: fault
      phase: 6
      class: SUBSTANCE-FLAT-political_register-prot (s02 moving bone)
      bone: b01c07s02n07
      what: |
        b01c07s02n07 is the moving bone for political_register-prot +0.3 in s02. Its SVO is
        "taylor-hebert-kl-122ac turns the thesis" — an interiority form (fault-002 above). A moving
        bone's SVO must witness its axis movement through a concrete physical act. An interiority-form
        SVO cannot witness the political_register-prot +0.3 move. SUBSTANCE-FLAT-political_register-prot.
        This is a HARD finding per /and-write Phase 6 rules: "SUBSTANCE-FLAT-<axis>... HARD findings."
        The s02 scene target for political_register-prot is +0.3 and this is the sole witness bone.
        Scene aggregate Δ cannot be confirmed as delivered when the witnessing bone is non-concrete.
      why: |
        The chapter's political_register-prot target is +0.5 (s02 +0.3 + s03 +0.2). If s02n07 is
        non-concrete and cannot witness the +0.3, the chapter delivers only the s03 +0.2 as a witnessed
        increment. The unwitnessed increment cannot be counted as delivered by the bone-gate. HARD.
      criteria: |
        The moving bone at s02n07 (or its replacement) must be a concrete physical SVO by
        taylor-hebert-kl-122ac that an observer could witness, whose concrete act is interpretable
        as the articulation-sharpening event delivering political_register-prot +0.3. The axis-move
        must be witnessed by the bone's own SVO. The cognitive turning is facet material.

    - id: fault-012
      type: fault
      phase: 6
      class: SUBSTANCE-FLAT-social_tether-prot-rise (s03 moving bone)
      bone: b01c07s03n09
      what: |
        b01c07s03n09 is the moving bone for social_tether-prot-rise +0.5 in s03. Its SVO is
        "the argument completes" — an interiority/abstraction form (fault-004 above). SUBSTANCE-FLAT-
        social_tether-prot-rise. HARD.
        The s03 scene target for social_tether-prot-rise is +0.5 and this is the sole witness bone.
        The s02 +0.5 at n10 ("taylor-hebert-kl-122ac stays in the argument") is concrete and passes;
        the s03 +0.5 at n09 does not.
      why: |
        The chapter's social_tether-prot-rise target is +1.0 (s02 +0.5 + s03 +0.5). The s02 +0.5
        is witnessed (n10 is concrete). The s03 +0.5 is unwitnessed (n09 is non-concrete). Chapter
        delivers only +0.5 as witnessed toward a +1.0 target. HARD per bone-gate rules.
      criteria: |
        The moving bone at s03n09 (or its replacement) must be a concrete physical SVO by a named
        actor that witnesses the tether-deepening event — the social embedding completion. The "argument
        completes" framing must be replaced with an observable physical act (departure gesture, sustained
        contact, a concrete leave-taking beat, or similar) from which the completion-not-closure can be
        inferred at the facet layer. The axis-move +0.5 must be witnessed by a concrete SVO.

  # --- SIGNAL: ABSTRACTION-DOMINANCE (s02 zone) ---

    - id: signal-002
      type: flag
      phase: 6
      class: ABSTRACTION-DOMINANCE (SIGNAL)
      what: |
        s02 bones n06/n07/n08/n09 form a 4-bone consecutive block of non-concrete (interiority/
        abstraction) SVOs at the chapter's argumentative core:
          n06: "the compound-corruption thesis lands" — INTERIORITY
          n07: "taylor-hebert-kl-122ac turns the thesis" — INTERIORITY
          n08: "taylor-hebert-kl-122ac reads the thesis for structural soundness" — INTERIORITY
          n09: "taylor-hebert-kl-122ac locates the rebuttal" — INTERIORITY
        The scene-aggregate ratio is 57% concrete (passes the 25% threshold) but the concentration
        of 4 consecutive abstract/interior bones at the central-event zone is the mechanism behind the
        PASS-CHUNK-VOICE-RISK seminar-risk classification. The 25% threshold is a floor, not an
        endorsement of concentrated abstract blocks at peak positions.
        Classified SIGNAL per spec ("ABSTRACTION-DOMINANT" flag vs. HARD). The HARD findings on n06
        and n07 (EVENT-NOT-CONCRETE) must be resolved; if their recasts are concrete, the block reduces
        to n08+n09 (both held, non-moving), which is an acceptable 2-bone interiority segment at a
        seminar-chapter's argument middle. SIGNAL is informational for /and-write resolution scope.
      why: |
        The PASS-CHUNK-VOICE-RISK /and-stitch Phase 8.5 arm will scrutinize the assembled prose at
        this zone for central-event muffle. Resolving fault-001 (n06) and fault-002 (n07) to concrete
        bones will reduce the block and lower the muffle risk. The n08/n09 interiority pair will remain
        and are design-inherent for the evaluative-pause beat; the facet layer must carry them with
        sufficient physicality in the narrator-interest anchors to prevent cold-read seminar-feel.
      criteria: null

  # ─────────────────────────────────────────────────────────────────
  # SUMMARY TABLE
  # ─────────────────────────────────────────────────────────────────

  summary_table:
    phase_2:
      faults_hard:
        - fault-001: b01c07s02n06 SVO interiority (EVENT-NOT-CONCRETE / FAULT-FORM-INTERIORITY)
        - fault-002: b01c07s02n07 SVO interiority (EVENT-NOT-CONCRETE / FAULT-FORM-INTERIORITY)
        - fault-003: b01c07s03n04 SVO interiority (EVENT-NOT-CONCRETE / FAULT-FORM-INTERIORITY)
        - fault-004: b01c07s03n09 SVO interiority (EVENT-NOT-CONCRETE / FAULT-FORM-INTERIORITY)
      signals:
        - signal-001: b01c07s02n12 borderline non-action-verb / negation (SIGNAL)

    phase_5:
      flags:
        - flag-001: c06 moral_legibility overdelivery absorb note (advisory, non-blocking)

    phase_6:
      faults_hard:
        - fault-011: b01c07s02n07 SUBSTANCE-FLAT-political_register-prot (moving bone non-concrete)
        - fault-012: b01c07s03n09 SUBSTANCE-FLAT-social_tether-prot-rise (moving bone non-concrete)
      signals:
        - signal-002: s02 n06-n09 abstraction-dominance zone (SIGNAL; PASS-CHUNK-VOICE-RISK context)
      passes:
        - fault-005 (sensory-grounding quota): PASS (advisory on s03n11 "holds" form)
        - fault-006 (dialogue coverage): PASS
        - fault-007 (Earth-Bet fence): PASS
        - fault-008 (dialogue-objective-matched): PASS
        - fault-009 (speech-bone communication-axis): PASS with borderline note
        - fault-010 (opposing-force-visible): PASS

    totals:
      hard: 6
      signal: 2
      flag: 1
      pass: 6

    bone_gate_verdict: FAIL
    reason: "HARD=6 (> 0 threshold). Four FAULT-FORM-INTERIORITY faults on bones s02n06, s02n07, s03n04, s03n09 (Phase 2 + Phase 6 joint findings); two SUBSTANCE-FLAT faults on the same moving bones (s02n07 political_register-prot +0.3 unwitnessed; s03n09 social_tether-prot-rise +0.5 unwitnessed). All six HARDs share a root cause: the evaluative/cognitive argument-middle was decomposed with interiority-form SVOs at the central-event and moving-bone positions."

    fix_scope: |
      Minimum repair: four bone recasts (s02n06, s02n07, s03n04, s03n09) to concrete observable SVOs.
      The axis-move witnesses (s02n07, s03n09) must be recast as concrete acts that enact the axis
      movements they carry. s02n06 and s03n04 must be recast to concrete physical-response bones whose
      cognitive/interior dimension transfers to narrator-interest facets citing the new SVOs.
      Resolving the four recasts will also resolve the two SUBSTANCE-FLAT HARDs (they are the same
      bones) and reduce the signal-002 abstraction-dominance block from 4 bones to 2.
      s02n12 (signal-001 borderline) and s03n07/s03n11/s03n12 (advisory non-action forms on held
      bones) are lower-priority recasts that can be addressed in the same pass or deferred.

  event_not_concrete_summary:
    bones_tested: [b01c07s03n01, b01c07s03n02, b01c07s03n03, b01c07s03n04, b01c07s02n06, b01c07s02n07, b01c07s03n09]
    pass: [b01c07s03n01, b01c07s03n02, b01c07s03n03]
    fail: [b01c07s03n04, b01c07s02n06, b01c07s02n07, b01c07s03n09]

  abstraction_dominance_ratios:
    s01: "91% (10/11) — PASS"
    s02: "57% (8/14) — PASS overall; 4-bone abstract block at n06-n09 flagged as SIGNAL"
    s03: "69% (9/13) — PASS"
