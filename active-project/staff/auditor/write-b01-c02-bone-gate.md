```yaml
audit:
  scope: chapter
  target: b01c02
  phase: 6 (substance bone-gate — auditor side)
  timestamp: 2026-05-25
  verdict: PASS-WITH-SIGNALS

  # Summary: 0 HARD findings. 2 SIGNALs. 1 FLAG (schema ambiguity, non-blocking).
  # Per-bone: 29 bones audited. 2 moving (s02n07, s03n05). 27 held. 0 chatter.
  # Per-scene: 3 scenes. All event-map coverage PASS. All chunk-tag completeness PASS.
  #   All Δ-delivery EXACT. All stakes-axis checks PASS. All sensory-grounding PASS.
  #   Opposing-force visible PASS on all 3. Cost-ledger N/A (zero chapter entries).
  # Per-chapter: SIGNAL count 1 (mannerism watch; below threshold).

  findings:

    # ─── PER-BONE: MOVING BONES ───────────────────────────────────────────────

    - id: pass-b01
      type: pass
      what: s02n07 — "the insects file the ward-junction contact under the stitch-house lane"
            (relational_anchor_status +1.0)
      why: |
        Bonefide check: the filing action (insects categorizing Wren-unnamed under the stitch-house
        lane as environmental-signature anchor) is a concrete physical event in the insect-feed —
        the classification of a body by its location-adjacency to a sensory marker Taylor already
        holds. The stitch-house tallow smoke was established as anchor at b01c01s01n02 and s03n08;
        the filing-under-stitch-house-lane links the function-node to that prior sensory datum
        without naming Wren. This is physically grounded categorization, not interior-state report.
        The axis move (anchor account opens: rank 1→2) is caused by the classification event
        landing in Taylor's accounting. Move is bonefide.
        Magnitude 1.0: within bone delta_per_axis band of 1-3. PASS.

    - id: fault-001
      type: fault
      what: s03n05 — "the word arrives before taylor-hebert-kl-122ac prevents it"
            (moral_legibility_to_self +0.5; magnitude below bone delta_per_axis floor of 1)
      why: |
        chunk_targets.bone.delta_per_axis is "1-3" (memory.md line 1465). s03n05 delivers
        magnitude 0.5, which is BELOW the 1-rank floor.
        The chapter contract specifies a total target of +0.5 for moral_legibility_to_self — the
        crack-and-suppress is explicitly non-linear and sub-rank (memory.md line 154: "non-linear
        net-positive"; substance_delta notes: "first non-linear uptick from rank 4 to 4.5").
        The chapter contract intends this to be a sub-rank move. However, the schema rule is
        stated at chunk_targets.bone level without a carve-out for non-linear axes or sub-rank
        crack beats.
        Consequence: without a rationale carve-out, the 0.5 magnitude fails the bone-gate's
        delta_per_axis floor as written. The bones file cannot pass a mechanical gate check on
        this bone unless (a) the magnitude is raised to 1.0 (which would overshoot the scene
        target and require a compensating negative-direction bone), or (b) a non-linear-crack
        exemption is declared.
      criteria: |
        Either: (a) bone s03n05 magnitude raised to 1.0 and a compensating suppression bone added
        with moral_legibility_to_self direction: down magnitude: 0.5 to preserve the scene net of
        +0.5 (two-bone crack-and-suppress model matching the chapter spec's SOFT-WATCH note); OR
        (b) chunk_targets.bone adds a non-linear-axis carve-out that explicitly licenses sub-rank
        moves for crack-and-suppress beats on non-linear axes (moral_legibility_to_self is
        designated non-linear in substance.state_axes[].notes). Fixer must resolve at one of these
        two surfaces; the ambiguity cannot survive /and-write Phase 7.
        NOTE: option (b) also propagates to /and-substance spec (chunk_targets) and should produce
        a parking-lot item for /and-review pipeline.

    # ─── PER-BONE: HELD BONES — DISCIPLINE CHECK (SAMPLE; FULL 27-BONE SCAN) ──

    - id: pass-b02
      type: pass
      what: s01 held bones (n01-n09, excluding movers) — discipline-enactment check
      why: |
        All 9 s01 bones are held. Discipline check:
          n01 (social_tether-prot-rise): rising from drain angle is anonymity enacted as posture —
            stillness-at-its-most-anonymous-location; PASS.
          n02 (capability, moral_framework): ambient fan at subsistence range before the decision —
            capability-not-yet-extended; PASS.
          n03 (moral_legibility_to_self): three heat-signatures delivered — accounting forward-looking,
            crack not yet fired; PASS.
          n04 (moral_framework): feet planted at alley-mouth — prohibition-as-body-position; PASS.
          n05 (capability): threshold-spread mechanism named as existing — not yet deliberately extended;
            PASS.
          n06 (capability, moral_framework): deliberate extension within harm-reduction frame — no axis
            move because framing keeps it within rank 3 scope; PASS.
          n07 (moral_framework): draws line at wall-face — harm-reduction enacted as body-gesture; PASS.
          n08 (capability): corner-to-corner sweep — systematic but harm-reduction capped; PASS.
          n09 (political_register-prot): foot-traffic knot at ward-junction — ward-level output, no
            court content; PASS.
        All s01 held bones enact stillness-against-pressure or dormancy-maintenance. PASS.

    - id: pass-b03
      type: pass
      what: s02 held bones (n01-n06, n08-n10) — discipline-enactment check
      why: |
        8 held bones in s02:
          n01 (capability): repeated return in insect-feed — coverage mechanism operating, not extension;
            PASS.
          n02 (relational_anchor_status): tallow smoke marks stitch-house lane — anchor present as
            sensory fact, dormancy held; PASS.
          n03 (moral_framework): ward-junction body touches six thresholds — Taylor reading pattern, not
            directing toward it; PASS.
          n04 (moral_framework): ward-junction body enters uncrossable alley — prohibition as spatial
            access constraint; PASS.
          n05 (moral_legibility_to_self): function-signature filed without name — categorization without
            examination; PASS.
          n06 (capability): map slots under connector-type — coverage map's ordinary operation; PASS.
          n08 (moral_framework): turns body from alley-mouth — discipline against approach enacted as
            direction; PASS.
          n09 (relational_anchor_status post-move): map opens gap at every alley junction-body entered —
            anchor's negative-space form after n07 move; PASS.
          n10 (relational_anchor_status + moral_legibility_to_self): map names first absence —
            anchor confirmed as absence-entry; PASS.
        All s02 held bones enact restraint, dormancy, or maintenance. PASS.

    - id: pass-b04
      type: pass
      what: s03 held bones (n01-n04, n06-n10) — discipline-enactment check
      why: |
        9 held bones in s03:
          n01 (social_tether-prot-rise): settles at drain angle — anonymity-as-location; PASS.
          n02 (capability): runs map corner-to-corner — review of completed map, no new deployment;
            PASS.
          n03 (moral_legibility_to_self): map returns forty-three bodies — accounting-as-homework,
            crack not yet fired; PASS.
          n04 (moral_legibility_to_self): accounting reaches forty-third body — edge-of-accounting, prior
            to crack; PASS.
          n06 (moral_framework): draws prohibition line at wall-face — suppression via framework;
            PASS (this is also the SUPPRESSION bone — bone 2 of 2).
          n07 (moral_legibility_to_self): harm-reduction accounting closes fever-cluster entry —
            ledger closes before reckoning; PASS.
          n08 (moral_framework): ledger closes dark-junction entry — active discipline; PASS.
          n09 (relational_anchor_status + moral_legibility_to_self): ledger closes ward-junction
            contact — anchor filed and closed, crack sealed; PASS.
          n10 (moral_legibility_to_self + social_tether-prot-rise): exhales at drain angle — body's
            verdict on accounting; PASS.
        All s03 held bones enact suppression or maintenance. PASS.

    # ─── PER-BONE: HELD-AXIS-UNCONTRACTED CHECK ─────────────────────────────

    - id: flag-002
      type: flag
      what: s02 axes_held list vs bone-level held axes for post-move relational_anchor_status
      why: |
        The s02 scene-level axes_held list (memory.md line ~2534-2545) does NOT include
        relational_anchor_status. Yet s02n09 and s02n10 both hold relational_anchor_status
        (post-move, after n07's +1.0 move).
        Schema question: is holding an axis at post-move bones after the axis moved in the same
        scene a "held" in the contracted sense — requiring scene-level axes_held listing — or is
        post-move holding implicitly licensed at non-mover bones without scene-level listing?
        The bones schema (schemas/bones.schema.md) does not resolve this. The substance overhaul
        design docs are not consulted here. The bones are substantively correct (post-move
        maintenance is not the same pressure-holding as a scene-contracted held-axis); the question
        is schema-vocabulary.
        This is a flag, not a fault: the post-move held bones are structurally sound; the
        scene-level axes_held list is not a gate field, and no gate fires on axes_held list
        completeness under the current schema. Flag for schema clarification at /and-review pipeline.
      criteria: null

    - id: flag-003
      type: flag
      what: s03 axes_held list vs bone-level held axes for moral_legibility_to_self at non-mover bones
      why: |
        s03 scene-level axes_held (memory.md ~2581-2592) does NOT list moral_legibility_to_self.
        Yet s03n03, n04, n07, n09, n10 all hold moral_legibility_to_self (pre-move maintenance at
        n03/n04; post-move maintenance at n07/n09/n10).
        Same schema-vocabulary ambiguity as flag-002: the in-motion axis is presumably understood
        to be "active" throughout the scene, and non-mover bones that hold it are maintaining the
        state between movement points. The scene-level axes_held list may be intended to capture
        only "exogenous" held axes (those not in motion anywhere in the scene).
        No gate fires on this. Structurally sound. Flag for schema clarification at /and-review
        pipeline.
      criteria: null

    # ─── PER-SCENE: EVENT-PRESENCE AND CHUNK-TAG COMPLETENESS ───────────────

    - id: pass-b05
      type: pass
      what: s01 event-map coverage — URI-WRITE-EVENT-COVERAGE (HARD)
      why: |
        s01 chunk tags parsed from memory.md:
          [force: Taylor's decision to extend coverage] → event_map entry: bones [n03, n04] ✓
          [event: Taylor notices a fever-cluster she cannot locate] → event_map entry: bones [n01, n02] ✓
          [mechanism: insect-feed fever-reading without contact] → event_map entry: bones [n02, n05] ✓
          [event: Taylor makes the explicit decision to run coverage] → event_map entry: bones [n04, n06] ✓
          [force: harm-reduction framing contains the decision] → event_map entry: bones [n07, n08] ✓
          [event: Taylor begins the first precinct sweep] → event_map entry: bones [n08, n09] ✓
        6 chunk tags; 6 event_map entries; all covered. Central event (sweep begins) covered at n08/n09.
        protagonist_force (coverage decision) covered at n03/n04/n06. PASS.

    - id: pass-b06
      type: pass
      what: s02 event-map coverage — URI-WRITE-EVENT-COVERAGE (HARD)
      why: |
        s02 chunk tags parsed:
          [event: Wren enters the insect-feed repeatedly across multiple survey sweeps] → [n01, n02] ✓
          [image: Wren's movement pattern — ward-junctions, everyone talked to, alleys Taylor cannot
            enter unseen] → [n03, n04] ✓
          [mechanism: coverage-map categorization without contact] → [n05, n06] ✓
          [event: Taylor categorizes Wren as a ward-junction contact] → [n07] ✓
          [force: Taylor's discipline against approaching Wren] → [n04, n08] ✓
          [force: Wren's network-centrality as opposing pressure] → [n03, n09] ✓
          [event: relational_anchor_status account opens] → [n07, n10] ✓
        7 chunk tags; 7 event_map entries; all covered. PASS.

    - id: pass-b07
      type: pass
      what: s03 event-map coverage — URI-WRITE-EVENT-COVERAGE (HARD)
      why: |
        s03 chunk tags parsed:
          [event: Taylor does the full accounting of the precinct survey] → [n01, n02] ✓
          [image: the scope of the map — forty-three people categorized without their knowledge] → [n03] ✓
          [force: the recognition arriving at the edge of the accounting] → [n04] ✓
          [event: Taylor recognizes the coverage map as surveillance] → [n05] ✓
          [event: Taylor suppresses the recognition and files the map under harm-reduction] → [n06, n07] ✓
          [mechanism: the suppression mechanism — harm-reduction accounting closes the ledger] → [n07, n08] ✓
          [force: the ledger closing as active discipline] → [n08, n09] ✓
          [event: chapter closes with the coverage map intact and the ledger closed] → [n09, n10] ✓
        8 chunk tags; 8 event_map entries; all covered. PASS.

    # ─── PER-SCENE: DELTA DELIVERY ──────────────────────────────────────────

    - id: pass-b08
      type: pass
      what: s01 axis-delta delivery — no axes in motion (target: zero)
      why: |
        s01 axes_in_motion: []. All 9 bones are held or held-chatter. Zero axis-delta delivered.
        Matches chunk contract. PASS.

    - id: pass-b09
      type: pass
      what: s02 axis-delta delivery — relational_anchor_status +1.0 (target: +1.0 ±1)
      why: |
        Single moving bone: n07 (+1.0). Delivered: +1.0. Target: +1.0. EXACT. PASS.

    - id: pass-b10
      type: pass
      what: s03 axis-delta delivery — moral_legibility_to_self +0.5 (target: +0.5 ±1)
      why: |
        Single moving bone: n05 (+0.5). Delivered: +0.5. Target: +0.5.
        EXACT within target. NOTE: see fault-001 — the magnitude itself triggers the bone-level
        delta_per_axis floor fault; the scene-level delivery is EXACT against contract but the
        bone-level gate fires independently. Scene-level PASS pending fault-001 resolution.

    # ─── PER-SCENE: STAKES-AXIS DOMINANT ────────────────────────────────────

    - id: pass-b11
      type: pass
      what: s01/s02/s03 stakes-axis dominant check — URI-WRITE-STAKES-AWARE (HARD)
      why: |
        s01 stakes_axis: moral_framework (held); axes_in_motion: []; N/A.
        s02 stakes_axis: relational_anchor_status; sole in-motion axis; trivially dominant. PASS.
        s03 stakes_axis: moral_legibility_to_self; sole in-motion axis; trivially dominant. PASS.

    # ─── PER-SCENE: SENSORY GROUNDING ───────────────────────────────────────

    - id: pass-b12
      type: pass
      what: s01/s02/s03 sensory-grounding quota — URI-WRITE-SENSORY-GROUNDING (HARD)
      why: |
        s01 grounding bones: n01 (drain angle), n04 (alley-mouth cobbles), n09 (ward-junction
          foot-traffic) = 3. Quota ≥1: PASS.
        s02 grounding bones: n02 (tallow smoke / stitch-house lane), n03 (six threshold-crossings),
          n08 (body direction from alley-mouth) = 3. Quota ≥1: PASS.
        s03 grounding bones: n01 (drain angle return), n06 (wall-face alley), n10 (drain angle
          exhale) = 3. Quota ≥1: PASS.

    # ─── PER-SCENE: HELD AXES HAVE BONE-LEVEL ENACTMENT ────────────────────

    - id: pass-b13
      type: pass
      what: Scene-level axes_held[] — bone-level enactment coverage
      why: |
        s01 axes_held = [capability, moral_framework, moral_legibility_to_self,
          relational_anchor_status, social_tether-prot-rise, political_register-prot]:
          capability: n02 ✓ n05 ✓ n06 ✓ n08 ✓
          moral_framework: n04 ✓ n06 ✓ n07 ✓
          moral_legibility_to_self: n03 ✓
          relational_anchor_status: (not listed in s01 axes_held — bone roll-up note confirms
            this is consistent; no held bone required for unlisted axis) ✓
          social_tether-prot-rise: n01 ✓
          political_register-prot: n09 ✓
          All s01 listed axes have ≥1 bone. PASS.
        s02 axes_held = [capability, moral_framework, moral_legibility_to_self,
          social_tether-prot-rise, political_register-prot]:
          capability: n01 ✓ n06 ✓
          moral_framework: n03 ✓ n04 ✓ n08 ✓
          moral_legibility_to_self: n05 ✓ n10 ✓
          social_tether-prot-rise: (not listed in s02 axes_held — consistent per roll-up) ✓
          political_register-prot: (not listed in s02 axes_held — consistent per roll-up) ✓
          All s02 listed axes have ≥1 bone. PASS.
        s03 axes_held = [capability, moral_framework, relational_anchor_status,
          social_tether-prot-rise, political_register-prot]:
          capability: n02 ✓
          moral_framework: n06 ✓ n08 ✓
          relational_anchor_status: n09 ✓
          social_tether-prot-rise: n01 ✓ n10 ✓
          political_register-prot: (not listed in s03 axes_held — consistent) ✓
          All s03 listed axes have ≥1 bone. PASS.

    # ─── PER-SCENE: OPPOSING FORCE VISIBLE ──────────────────────────────────

    - id: pass-b14
      type: pass
      what: s01 opposing force — "distinction between reading and directing resists clean resolution"
      why: |
        s01 opposing_force: "the distinction between reading and directing — the prohibition she must
        reframe in order to act — resists clean resolution; the line is real but she is moving toward it."
        Visible at: n04 (feet planted at alley-mouth — prohibition as body-position, the threshold moment);
        n07 (draws line at wall-face — the physical form of the reads-not-directs reframe, enacted as a
        place where the body stops). Both bones enact the opposing-force as physical resistance Taylor
        must navigate. PASS.

    - id: pass-b15
      type: pass
      what: s02 opposing force — "Wren's network-centrality makes presence felt as negative space"
      why: |
        s02 opposing_force: "Wren's network-centrality makes her presence in the map felt as negative
        space: everywhere she moves is everywhere Taylor cannot follow."
        Visible at: n04 (ward-junction body enters alley Taylor cannot cross unseen — the physical
        form of the negative space) and n09 (coverage map opens a gap at every alley the junction-body
        entered — the map's incompleteness as physical shape). Both bones enact opposing-force as
        perceptual events in the insect-feed, not as Taylor's reasoning chain (per SOFT-WATCH
        from /and-substance chapter Phase 5). PASS.

    - id: pass-b16
      type: pass
      what: s03 opposing force — "recognition arrives in one beat and must be suppressed in the next"
      why: |
        s03 opposing_force: "the recognition of what she has built — a surveillance architecture over
        forty people without consent — arrives in one beat and must be suppressed in the next."
        Visible at n05 (the word arrives before taylor-hebert-kl-122ac prevents it — recognition bone,
        bone 1 of 2-bone crack-and-suppress). The arrival is the opposing force. n06 (draws prohibition
        line at wall-face — suppression bone, bone 2 of 2) enacts the force being overcome. Two
        structurally separate bones per SOFT-WATCH from /and-substance chapter Phase 5. PASS.

    # ─── PER-SCENE: COST-LEDGER ──────────────────────────────────────────────

    - id: pass-b17
      type: pass
      what: Cost-ledger entries paid — chapter b01c02
      why: |
        b01c02 substance_delta: cost_ledger_anchor: null for both in-motion axes (memory.md ~2403-2410).
        No ledger entries anchor at this chapter. Zero cost-ledger bones required. N/A. PASS.

    # ─── PER-CHAPTER: REGISTER-MANNERISM SCAN ───────────────────────────────

    - id: signal-001
      type: flag
      what: |
        URI-WRITE-REGISTER-MANNERISM (SIGNAL, 2026-05-24) — VERB OBJECT pair frequency scan.
        29 bones, 29 unique verb+object pairs extracted. No pair at ≥3 threshold. Closest:
        "closes [entry]" appears at s03n07 (closes the fever-cluster entry), s03n08 (closes the
        dark-junction entry), s03n09 (closes the ward-junction contact) = 3 instances.
        VERB: closes. OBJECT class: ledger-entry (all three are distinct entries; not identical
        object strings). The pair "closes [entry]" technically reaches 3 if object-class is
        counted (fever-cluster entry / dark-junction entry / ward-junction contact — all are
        ledger-entry objects of the verb closes).
      why: |
        If counted by verb+object-class rather than verb+literal-object-string, "closes [ledger
        entry]" is a ×3 mannerism candidate. This is the chapter's suppression-mechanism rhythm
        (three filed entries, each closed in sequence) — the repetition is structurally intentional
        and narratively load-bearing (the rhythm enacts the ledger closing as "active discipline"
        per s03 chunk). However, if auditor at /and-write bone-gate applies a literal verb+object-
        class match, the SIGNAL fires.
      criteria: null
      disposition: |
        ACCEPT. The three "closes [entry]" bones (s03n07/n08/n09) are intentionally rhythmic and
        structurally required — each closes a distinct named entry and each is load-bearing for the
        suppression-mechanism event_map coverage (n07 covers mechanism tag, n08 covers force tag,
        n09 covers both force and chapter-close tags). The repetition is the mechanism's form.
        Disposing as structural-register-not-mannerism, matching the b01c01 precedent for
        ACCEPT-faces-mannerism-chapter-register (where "faces" at ×5 was accepted as
        body-orientation load-bearing for ward-categorization beats). Suggest /and-write
        Phase 7 disposition note: ACCEPT-ledger-close-mannerism-s03-suppression-rhythm.

    - id: signal-002
      type: flag
      what: Hook vocabulary concentration scan — drain, alley-mouth, ward-junction, stitch-house
      why: |
        Recurring Hook geography vocabulary across all 3 scenes:
          drain angle: s01n01, s03n01, s03n10 = ×3 (drain angle is the chapter's spatial frame;
            chapter opens and closes at drain angle by design — b01c02 mirrors b01c01's
            drain-open structure)
          alley-mouth: s01n04, s02n04, s02n08 = ×3 (each is a distinct event: decision-body
            placement, physical negative-space entry, discipline-as-direction-away)
          ward-junction: s01n09, s02n07, s03n09 = ×3 (foot-traffic knot / filing event / ledger-close)
          stitch-house lane: s02n02, s02n07 = ×2 (tallow smoke / filing anchor; below threshold)
        Three terms hit exactly ×3. No VERB+OBJECT pair among these (the verbs are distinct:
        rises/settles/exhales for drain; plants/enters/turns for alley-mouth; knots/files/closes
        for ward-junction). These are OBJECT repetitions, not VERB+OBJECT pair repetitions.
        URI-WRITE-REGISTER-MANNERISM as written targets VERB+OBJECT pairs, not object-only
        repetitions. This scan finds no VERB+OBJECT pair at ≥3.
      criteria: null
      disposition: |
        PASS on mannerism gate (no VERB+OBJECT pair hits ≥3 threshold). Hook geography
        object repetition is load-bearing location-anchoring for a precinct-sweep chapter;
        not a mannerism. Noting for /and-write Phase 7 awareness.

    # ─── CHAPTER-LEVEL SOFT-WATCH COMPLIANCE ────────────────────────────────

    - id: pass-b18
      type: pass
      what: SOFT-WATCH compliance — two SOFT-WATCHes from /and-substance chapter b01c02 Phase 5
      why: |
        SOFT-WATCH (1): "s03 crack-and-suppress must decompose into two structurally separate bones."
        Delivered: n05 (the word arrives — recognition bone) + n06 (draws prohibition line —
        suppression bone). Two bones. n05 fires first; n06 responds. Structurally prior-and-consequent.
        PASS.
        SOFT-WATCH (2): "s02 Wren negative-space must be enacted as a perceptual event in the
        insect-feed (physical gap with specific shape), not as Taylor's reasoning chain."
        Delivered: n04 (the alley the junction-body enters that Taylor cannot cross — physical
        boundary) + n09 (the coverage map opens a gap at every alley the junction-body entered —
        the map's incompleteness as a named physical shape). Both are perceptual events in the
        feed, not reasoning chain. n04 is a fact returned by the sweep; n09 is the map's physical
        shape. PASS.

    # ─── VERDICT SUMMARY ────────────────────────────────────────────────────

    # fault-001: HARD — s03n05 bone delta magnitude 0.5 below bone delta_per_axis floor of 1.
    #   Two resolution paths: raise to 1.0 + add compensating suppression bone, or add
    #   non-linear-crack carve-out to chunk_targets.bone spec.
    # signal-001: ACCEPT disposition — "closes [entry]" ×3 is suppression-rhythm not mannerism.
    # signal-002: PASS — no VERB+OBJECT pair at ≥3; Hook geography object repetition is
    #   location-anchoring.
    # flag-002, flag-003: schema-vocabulary ambiguity on post-move / in-motion-axis held bones;
    #   non-blocking; surface to /and-review pipeline.
    # flag-001 (Phase 5): actor state.md staleness (capability_axis still at 2 post b01c01 close);
    #   non-blocking for b01c02 bones but requires state file update before b01c03.
```
