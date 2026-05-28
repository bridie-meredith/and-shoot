audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  pass: 2
  label: "/and-write b01c05 Phase 2 — constraint + form + delta audit; 34 bones across 3 scenes"

  summary: |
    FINDINGS-PRESENT. 2 HARD faults, 4 SIGNALs, 3 FLAGs.

    Two HARD faults require fixer dispatch before Phase 3 proceeds. fault-001 is a
    FAULT-FORM-PERCEPTION against b01c05s01n05: "the insect-feed returns the provisioner-train
    gait-class" — "returns" with a cognition-class object ("gait-class") is a perception verb
    wrapping. fault-002 is a FAULT-FORM-PERCEPTION cluster covering the five additional uses of
    "returns" where the object is analytical/categorization content rather than a physical thing,
    confirming the verb-as-perception-channel pattern. All other axes clear: no FAULT-CONSTRAINT,
    no FAULT-PHYSICAL, no FAULT-BONE-DELTA-MALFORMED, no FAULT-AGGREGATE-DELTA-MISMATCH,
    no FAULT-COST-LEDGER-UNRESOLVED. The author-flagged s03n06 form is ruled PASS (see
    fault-001 ruling — the distinction between "resentment color" as an object and "gait-class"
    as an object is load-bearing). "maps" verb register is surfaced as a SIGNAL (7 occurrences).
    Rushwick location-card absence is surfaced as a deferred SIGNAL. The 13-bone s03 count is
    ruled ACCEPTABLE for the dramatic discipline. The message-runner pair n07/n08 in s01 is
    ruled appropriate; no collapse recommended.

  findings:

    # ── HARD FAULTS ──────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      class: FAULT-FORM-PERCEPTION
      severity: HARD
      what: |
        b01c05s01n05 SVO: "the insect-feed returns the provisioner-train gait-class"
        b01c05s01n08 SVO: "the insect-feed releases the message-runner at the lane-mouth"
        b01c05s02n01 SVO: "the insect-feed returns the courier at the lane-mouth"
        b01c05s02n04 SVO: "the insect-feed returns the approach-geometry"
        b01c05s02n07 SVO: "the insect-feed logs the courier upright"

        Five bones use the insect-feed as a structural surrogate for Taylor's perception:
        "feed returns X" (×4) and "feed logs X" (×1). The bones.schema.md perception-verb
        ban applies regardless of grammatical subject: when the feed is cast as the agent
        returning/logging a categorization product to Taylor, the verb is doing the work of
        "Taylor perceives / Taylor registers / Taylor reads." The objects in n05, n01, n04
        are analytical categories ("gait-class," "the courier," "approach-geometry"), not
        physical things the feed could physically produce. "Returns" with a categorization
        object is a perception verb in a feed-subject disguise. "Logs" is cognition-as-event.
        "Releases" in n08 is borderline (physical action of dropping coverage range) but is
        included here because the batch pattern needs consistent resolution.

        Note — "releases" (n08) is the weakest member: dropping coverage is arguably a
        physical act. Fixer may judge n08 separately. The other four (n05, s02n01, n04,
        n07) are clear FAULT-FORM-PERCEPTION.

      why: |
        Per bones.schema.md: "perception verbs… describe internal observation, not external
        action." "Returns" with a cognition-class object (gait-class, approach-geometry,
        courier-as-recognized-body) routes perception through the grammatical subject "the
        insect-feed," but the semantic act is Taylor's cognition. The bones file is comment-
        clean SVO; bones that encode perception as the feed's "returns" output will route
        downstream to /and-facets as physical-action bones and be cited as event anchors —
        producing narrator/sensory facet citations against bones that are actually interiority
        beats. The stitcher will render the bones as physical events, doubling the perception
        content in the final draft.

      criteria: |
        Each affected bone must be recast so the SVO records a physical observable act —
        what a bystander would see — not a cognition/categorization product delivered by
        the feed. Physical options for "feed returns X" include: the provisioner train
        crossing / the courier crossing / the three figures' bodies positioning. The
        categorization content ("gait-class named," "enforcement read") belongs in the
        narrator-interest facet citing those physical bones, not in the bone SVOs themselves.
        "Feed logs the courier upright" (n07) must become a physical bone: the courier on
        their feet after the contact ends. "Feed releases the message-runner at the lane-
        mouth" (n08) may be recast as "the message-runner exits the lane-mouth" or reviewed
        by fixer for the physical-action-of-coverage edge.

    - id: fault-002
      type: fault
      class: FAULT-FORM-PERCEPTION (explicit ruling on author-flagged s03n06)
      severity: HARD
      what: |
        b01c05s03n06 SVO: "the rushwick-feed returns the resentment color"
        b01c05s03n05 SVO: "the rushwick-feed returns the provisioner-train color"
        b01c05s03n11 SVO: "the rushwick-feed returns the color"
        b01c05s03n13 SVO: "the rushwick-feed returns the color"

        Author flagged s03n06 for explicit ruling. Four s03 bones use "returns" with abstract
        objects: "resentment color," "provisioner-train color," "the color" (×2).

        EXPLICIT RULING ON s03n06: FAULT-FORM-PERCEPTION — HARD.

        The distinction the author drew between "feed-as-subject returns an abstract object"
        (their chosen form) and "taylor registers X" (the rejected perception-verb form) does
        not escape the ban. Both forms route an abstract cognitive/affective product through
        a perceptual channel. "The rushwick-feed returns the resentment color" means: the
        feed delivers an affective state-result to Taylor's cognition. The object "resentment
        color" is abstract-affective, not physical. Per bones.schema.md: "A physical verb
        whose object is an abstract noun… is a thought-figure, not an event. Faults
        FAULT-FORM-INTERIORITY." The verb "returns" with object "resentment color" also
        triggers FAULT-FORM-INTERIORITY independent of the perception-verb issue. This bone
        carries two form violations simultaneously.

        The same analysis applies to s03n05 ("provisioner-train color"), s03n11 ("the color"),
        s03n13 ("the color"). All four are FAULT-FORM-PERCEPTION + FAULT-FORM-INTERIORITY.

        s03n06 is additionally the +1.5 Δ bone and the cl-d05 anchor. The form fault does
        NOT invalidate the substance delta or the cost anchor — those travel in showrunner
        memory, not in the SVO. The bone must be recast in clean SVO form, but the Δ and
        anchor survive the recast intact.

      why: |
        Four bones in s03 — including the chapter's only axis-moving bone — encode the
        chapter's central dramatic event (political_register-prot account opening) as
        interiority-plus-perception rather than as a physical observable act. These bones
        are the scene's load-bearing spine. If they survive into /and-facets as written,
        the narrator-interest and feeling facets will cite abstract-color-return events as
        physical anchors, and the stitcher will render interiority as event-layer prose.
        The chapter's dramatic peak lands in the rendered draft as Taylor thinking a thought
        rather than a world-event Taylor observes. This degrades the bones-first discipline
        the substance gate is designed to protect.

      criteria: |
        Each of the four affected s03 bones must be recast in clean SVO where the subject
        is a physical entity performing a physical observable act and the object is a physical
        thing or a physically grounded noun form (not an abstract affective quality). The
        axis-move (+1.5 political_register-prot) and the cost_ledger_anchor (cl-d05) on
        s03n06 must be preserved in the recast bone's substance_delta — they are not affected
        by the form correction. Recast examples for fixer's consideration (not prescriptive):
        the provisioner train executing its route through the junction (a physical act Taylor
        observes in replay) is the physical anchor bone; the "color" that the feed returns is
        the narrator-interest facet content citing that bone. The foreclosure-enactment sequence
        (n10–n13) similarly needs physical anchor bones for Taylor's replay acts, with the
        feed's failure-to-resolve as facet content, not as the bone SVO.

    # ── SIGNALS ──────────────────────────────────────────────────────────────────

    - id: signal-001
      type: flag
      class: SIGNAL — verb register: "returns" frequency
      severity: SIGNAL (Phase 6 register-as-mannerism check advisory)
      what: |
        "returns" appears as the primary verb in 9 of 34 bones. Full inventory:
          s01: n05 ("feed returns the provisioner-train gait-class")
          s02: n01 ("feed returns the courier at the lane-mouth"), n04 ("feed returns the
               approach-geometry"), n06 ("side-alley returns the effortful sound")
          s03: n05 ("rushwick-feed returns the provisioner-train color"), n06 ("rushwick-feed
               returns the resentment color"), n09 (not "returns" — not counted), n11
               ("rushwick-feed returns the color"), n13 ("rushwick-feed returns the color")

        8 of the 9 uses have "the feed" or "the alley" as subject. The 8-instance raw count
        exceeds the ~5 graduation threshold flagged in the dispatch instructions.

        After the HARD faults above are resolved, some of these will be recast and the count
        will drop. s02n06 ("the side-alley returns the effortful sound") does NOT share the
        perception-verb pattern (an alley physically producing a sound is a physical act with
        a physical object — PASS on form). Even so, "returns" as the default verb for "the
        feed/environment surfaces X" has become a structural tic across all three scenes.

      why: |
        Phase 6 checks verb+object distinct-pairs for register-as-mannerism. If "feed returns
        [abstract-noun]" recasts in fault-001/002 all substitute a different verb form, the
        register-tic resolves automatically. If the recasts retain "returns" with physical
        objects (e.g. "the feed returns [physical actor]"), the verb still appears in 3–4 bones
        and should be reviewed at Phase 6 for variety. Surface now so Phase 6 has the count.

      criteria: null

    - id: signal-002
      type: flag
      class: SIGNAL — verb register: "maps" frequency
      severity: SIGNAL (Phase 6 register-as-mannerism check advisory)
      what: |
        "taylor-hebert-kl-122ac maps X" appears in 7 bones. Full inventory:
          s01: n06 ("maps the provisioner-train interval"), n09 ("maps the message-runner
               gait-class")
          s02: n02 ("maps the courier gait-signature"), n08 ("maps the enforcement approach-
               geometry"), n11 ("maps the courier body-filing")
          s03: n08 ("maps the resentment-color entry"), n09 ("maps the courier body-record")

        Subject is consistently taylor-hebert-kl-122ac (not the feed). Objects are distinct
        in each case (interval, gait-class, gait-signature, approach-geometry, body-filing,
        resentment-color entry, body-record). The verb+object pairs are technically distinct.
        However, "taylor maps" appears as the default form for Taylor's cognition-in-action
        across all three scenes. 7 occurrences in 34 bones = 21% of all bones use this verb.

        Note: "maps the resentment-color entry" (s03n08) may also carry a form issue if
        "resentment-color entry" is abstract-as-object — fixer should assess this bone when
        resolving fault-002, as it is adjacent to the interiority cluster.

      why: |
        Phase 6 verb+subject-pair gate will catch this if "taylor maps" recurs as the dominant
        form. Seven uses against 34 bones is above the advisory threshold. Distinct objects do
        not eliminate register-tic if the subject-verb pair is invariant across the chapter.
        Surface now for Phase 6 judgment.

      criteria: null

    - id: signal-003
      type: flag
      class: SIGNAL — location card absent: "the rushwick"
      severity: SIGNAL (deferred to Phase 5 / margit)
      what: |
        The Rushwick ward is referenced as a primary location across all 34 bones and all
        three scenes. No oc-rushwick.card.md exists in active-project/warehouse/ or the
        cards/locations/ library. The bones draft refers to: "the rushwick junction," "lane-
        mouth," "side-alley off the east exit," "alley-mouth," "the east exit," "the hill's
        stone skirt." These are spatial sub-features of the ward that will be consumed by the
        studio location-state facet at /and-facets.

        The chapter is consistent with cond-kl-geography-122ac: the Rushwick is described
        as abutting the lower Red Keep servant passages, placing it on the lower slopes of
        Aegon's Hill above Flea Bottom — consistent with the geography card's noble-quarter
        / Aegon's Hill slope description. No geographic violation detected. The location-card
        absence is a missing warehouse artifact, not a bones-layer fault.

      why: |
        Without oc-rushwick.card.md, the studio agent at /and-facets Phase 1 (location-state
        facet) has no card to load for scene-setting. The studio fork will either improvise
        location geometry or flag the missing card. A margit-authored card between Phase 5
        and Phase 7 resolves this cleanly. Classify as SIGNAL rather than FAULT because the
        bones layer itself is not in error — the spatial vocabulary used is internally
        consistent and geography-consistent; only the warehouse card is absent.

      criteria: null

    - id: signal-004
      type: flag
      class: SIGNAL — s03 13-bone count (author-flagged ruling)
      severity: SIGNAL (advisory; not a block)
      what: |
        s03 contains 13 bones against the 8–10 estimate in the chapter's
        bones_per_scene structure range. Author flagged the deliberate overrun and requested
        an explicit ruling on whether the 13-bone count is acceptable for the foreclosure-
        enactment dramatic discipline or should be trimmed at Phase 4.

        RULING: ACCEPTABLE. The over-by-3 is structurally justified.

        The n10/n11 + n12/n13 pairs (Taylor runs the flat-read → feed returns color × 2)
        are the enacted foreclosure. Collapsing each pair to a single bone would produce one
        "Taylor attempts flat-read / flat-read fails" beat where the chapter's substance
        contract requires the reader to experience the failed attempt as a repeated physical
        act, not a stated fact. The chapter chunk explicitly calls for "foreclosure enacted"
        (not merely mentioned), and the chunk notes in showrunner memory name n10/n11 + n12/n13
        as "load-bearing for the foreclosure-as-enacted-capability-failure." The 13-bone count
        performs the chapter's primary dramatic obligation (political_register-prot account
        opens; neutral-instrumentally-observant is foreclosed). Trim pressure at Phase 4 is
        low on these bones. The only candidate for Phase 4 review is whether n03 (Hook-feed
        resolves) is necessary as a baseline-establishment bone or can be served by the scene's
        event-map context — but this is Phase 4 judgment, not a Phase 2 fault.

      criteria: null

    # ── FLAGS ─────────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      class: FLAG — s01 message-runner pair n07/n08 density
      severity: FLAG (advisory; author-flagged)
      what: |
        Author flagged s01 bones n07 ("the message-runner crosses the junction") and n08
        ("the insect-feed releases the message-runner at the lane-mouth") as candidate-for-
        collapse if the scene reads as overlong. s01 is 9 bones against the 8–10 estimate.

        Ruling: Do NOT collapse at Phase 2. n07 is the crossing (movement event); n08 is the
        coverage-release (discipline-enactment event). These are structurally distinct beats:
        the movement and the restraint. The substance contract for s01 holds
        capability + political_register-prot across both bones for different rationale reasons
        (n07 = court-tier body in feed; n08 = feed does not chase it). Collapsing them loses
        the discipline-enactment beat. Phase 4 trim judgment applies if the chapter density
        read flags these as redundant after fault-001/002 recasts change the scene's weight
        distribution. No Phase 2 action required.

        Note: n08 carries the HARD fault from fault-001 (perception verb "releases"). After
        recast, the collapsed vs. separate question may resolve naturally if the physical-
        action form of n08 becomes "the message-runner exits the lane-mouth" — which is n07's
        continuation rather than a new beat. Fixer should flag this to Phase 4.

      criteria: null

    - id: flag-002
      type: flag
      class: FLAG — axes_held[] rationale multi-clause density
      severity: FLAG (non-blocking; carried from prior audit)
      what: |
        Showrunner memory notes this as advisory fault-003 from the /and-substance b01c05
        chunk audit (attempt 1, persisting at attempt 2 as non-blocking). Multiple bones
        across all three scenes have axes_held[] rationale fields that are multi-sentence
        paragraphs rather than one-line schema form. Examples:
          s01n08: axes_held[capability].rationale = "coverage maintenance; feed operates at
            established range; no extension" — acceptable (one compound statement)
          s01n05: axes_held[political_register-prot].rationale = 97-character compound with
            three semantic clauses — borderline
          s02n04: axes_held[political_register-prot].rationale = 185-character compound —
            over schema form

        The bones schema does not define a character limit for rationale fields; this flag
        carries the prior audit's advisory that the rationale fields are denser than the
        one-line schema form implies. This does not affect bones-layer form validity. No
        fixer action required; surface for Phase 6 / showrunner memory cleanup if desired.

      criteria: null

    - id: flag-003
      type: flag
      class: FLAG — bones file header absent from draft
      severity: FLAG (required before Phase 7 emit)
      what: |
        The bones draft at active-project/staff/showrunner/b01c05-bones-draft.md does not
        include the seven-field header required by bones.schema.md §"File header (required)":
          episode: b01c05
          narrator: taylor-hebert-kl-122ac
          goal: <from showrunner memory chapters[b01c05].goal>
          cast: taylor-hebert-kl-122ac
          locations: oc-rushwick (pending card), [other location slugs]
          prior_episode: b01c04
          aggregate_range: 1-34

        The draft is the working authoring file, not the Phase 7 emitted file; the header
        is added at Phase 7 serialization. However, the cast field's slug-grep requirement
        and the locations field's warehouse-resolve requirement should be noted for Phase 7:
        only taylor-hebert-kl-122ac appears as a subject across all 34 bones; the courier,
        three figures, message-runner, and provisioner-train are unnamed noun-forms and are
        NOT cast entries per the schema's "named entity as SUBJECT" rule. The locations field
        must handle oc-rushwick's absent card (see signal-003).

      criteria: null

  # ── CONSTRAINT PASSES (explicit) ──────────────────────────────────────────────

  constraint_passes:

    - constraint: cond-taylor-pov-behavior
      result: PASS
      notes: |
        Bones layer is in third-person named-subject SVO form. This is the required pipeline
        convention; first-person transformation is /and-stitch's responsibility. No bones-layer
        POV violation. No interiority in subjects (all interiority content is in axes_held[]
        rationale or notes fields, not in SVOs). No theme-narration in SVO form.

    - constraint: cond-earth-bet-noun-fence
      result: PASS
      notes: |
        Full substring scan of all 34 SVOs. No parahuman jargon detected. "Insect-feed" and
        "insect-coverage" are project-established substitution-register terms (licensed per
        the card's substitution register section). "Khepri" does not appear in any SVO.
        No cape-name vocabulary, no Earth-Bet geography, no institutional vocabulary from
        Worm canon. CLEAN.

    - constraint: cond-kl-witch-label-formation-122ac
      result: PASS
      notes: |
        This chapter does not contain any witch-label formation event. Taylor's coverage of
        the Rushwick is the operational subject; no scene depicts witnesses observing
        insect-anomaly behavior or label-formation escalation. No stage violation. Not
        applicable to this chapter's content.

    - constraint: cond-override-architecture-residue-122ac
      result: PASS
      notes: |
        No implication of Khepri-mantle capability (human body coordination) anywhere in
        the 34 bones. No range claim exceeds the established four-ward coverage pattern
        (confirmed in s01n02/n03 as "continuation of four-ward map established in c04").
        The feed's behavior-reading capability (gait-class naming, approach-geometry
        categorization) is consistent with the pattern-recognition-as-cognition description
        in the card. No Khepri-rhyming architecture vocabulary in SVOs. CLEAN.

        Watch item: the "feed" vocabulary ("the insect-feed returns X") is a project-
        established substitution form. The feed-as-subject construct does not imply shard
        infrastructure. However, after fault-001/002 recasts, the feed-subject form will be
        reduced in bones SVOs, which additionally reduces any surface-level override-
        architecture-rhyming in the bones layer.

    - constraint: cond-road-to-hell-chain-shape
      result: PASS (chapter-level scope)
      notes: |
        This chapter is a b01c05 chain beat — political_register-prot account opening, not
        an auditable-mistake beat per the chain-shape card's definition. The chapter delivers:
        court-tier content arrives → Taylor reads neutrally → enforcement incident observed
        → routed as movement-pattern → evening replay reveals resentment color → color filed
        as texture → foreclosure enacted. This is the "accumulation that happens regardless
        of categorization" beat, not a cold-utilitarian-correct choice that narrows exits.
        No chain-shape violation at this chapter. The cl-d05 anchor is the correct ledger
        entry for this beat type (opportunity-missed: neutral register foreclosed, not a
        mistake Taylor makes — it is a cost that arrives without a decision attached).
        CLEAN at this chapter scope.

    - constraint: cond-kl-geography-122ac
      result: PASS
      notes: |
        "The Rushwick" is placed as abutting the lower Red Keep servant passages, consistent
        with lower Aegon's Hill slope. The hill's stone skirt (s01n01) is consistent with
        the geography card's hill-slope vocabulary. No gate names invented. No hill
        misattribution. The spatial vocabulary (junction, lane-mouth, side-alley, east exit,
        alley-mouth) is generic and consistent with KL's dense urban geography. CLEAN.

  # ── AGGREGATE DELTA VERIFICATION ──────────────────────────────────────────────

  aggregate_delta_verification:

    - scene: b01c05s01
      contract_axes_in_motion: []
      expected_aggregate: 0
      bones_sum:
        political_register-prot: 0
        capability: 0
        moral_framework: 0
        relational_anchor_status: 0
      result: MATCH
      notes: "All 9 bones are held-only. Zero axis_moves across the scene. Contract expects 0. PASS."

    - scene: b01c05s02
      contract_axes_in_motion: []
      expected_aggregate: 0
      bones_sum:
        political_register-prot: 0
        capability: 0
        moral_framework: 0
        relational_anchor_status: 0
      result: MATCH
      notes: "All 12 bones are held-only. Zero axis_moves across the scene. Contract expects 0. PASS."

    - scene: b01c05s03
      contract_axes_in_motion:
        - axis: political_register-prot
          direction: up
          target_delta_magnitude: 1.5
      expected_aggregate: "+1.5 on political_register-prot"
      bones_sum:
        political_register-prot: "+1.5 (sole axis_move on s03n06)"
      result: MATCH
      notes: |
        One axis-moving bone in s03: s03n06 carries axis_moves[political_register-prot, up,
        1.5]. Contract target_delta_magnitude is 1.5. Sum = 1.5. Within ±1 tolerance.
        The +1.5 magnitude is within the 1.0–3.0 per-bone delta_per_axis range per
        bones.schema.md §magnitude. The 0.5 floor note in the dispatch is satisfied (1.5 ≥ 1.0).
        PASS.

        Note: s03n06's SVO carries fault-002 (FAULT-FORM-PERCEPTION + FAULT-FORM-INTERIORITY).
        The substance_delta and cost_ledger_anchor survive recast; fixer must preserve the
        axis_move block when correcting the SVO form. The aggregate delta math is correct and
        does not change after the form recast.

  # ── COST LEDGER VERIFICATION ──────────────────────────────────────────────────

  cost_ledger_verification:

    - bone: b01c05s03n06
      cost_ledger_anchor: cl-d05
      ledger_entry_exists: true
      ledger_entry_content: |
        id: cl-d05
        gain: "political_register-prot +3"
        cost: "opportunity-missed: resentment becomes the permanent register of court
               observation; the insect-feed now returns color Taylor cannot un-notice;
               neutral-instrumentally-observant is foreclosed from d05 forward"
        anchor: { book: b01, chapter: null, scene: null }
      result: VALID
      notes: |
        cl-d05 exists at memory.md line 1362. This chapter delivers the first tranche of the
        +3 cl-d05 gain (+1.5; noted in showrunner memory). The anchor is chapter-open
        (chapter: null) — consistent with a multi-chapter ledger gain whose first tranche
        lands here. PASS.

  # ── PHYSICAL CAST VERIFICATION ──────────────────────────────────────────────────

  physical_cast_verification:
    result: PASS
    notes: |
      taylor-hebert-kl-122ac is the sole named actor in all 34 SVOs. Courier, three figures,
      message-runner, provisioner-train are unnamed noun-forms functioning as environmental
      subjects — consistent with the chapter's cast (b01c05 cast per handoff: Taylor only;
      Jarvis receives a report but does not appear physically in any scene). No actor appears
      as a subject who is not in the chapter cast. PASS.

  # ── DISPATCH-SPECIFIC RULINGS ──────────────────────────────────────────────────

  dispatch_rulings:

    - item: "s03n06 'the rushwick-feed returns the resentment color' — FAULT-FORM-INTERIORITY?"
      ruling: "FAULT — HARD. See fault-002. Both FAULT-FORM-PERCEPTION and FAULT-FORM-INTERIORITY apply simultaneously. The feed-as-subject form does not rescue the abstract object 'resentment color.' The author's alternative-considered ('taylor registers the resentment color') was correctly rejected as a perception verb; the resolution is not to move the perception to the feed-subject but to identify the physical observable act the resentment-color recognition is anchored to and make that the bone."

    - item: "s01 9 bones vs 8–10 estimate — collapse n07/n08?"
      ruling: "DO NOT COLLAPSE at Phase 2. See flag-001. Distinct beats; discipline-enactment is load-bearing. Phase 4 judgment after fault-001 recast."

    - item: "s03 13 bones vs 8–10 estimate — acceptable?"
      ruling: "ACCEPTABLE. See signal-004. Foreclosure enactment requires the repeated physical attempt sequence. No trim recommended."

  verdict: FINDINGS-PRESENT
  hard_count: 2
  signal_count: 4
  flag_count: 3
  fixer_dispatch_required: true
  fixer_scope: "fault-001 (5 bones: s01n05, s01n08, s02n01, s02n04, s02n07) + fault-002 (4 bones: s03n05, s03n06, s03n11, s03n13) — 9 bones total; s03n06 substance_delta must be preserved exactly through recast"
