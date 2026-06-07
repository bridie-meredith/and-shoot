audit:
  scope: chapter
  target: b01c19
  timestamp: 2026-06-05
  gate: /and-facets Phase 5 mechanical facet audit (pre-audience-gate)
  mode: flag-only (no fixer dispatch; audience-gate fires if HARD=0)

  summary:
    hard_count: 0
    signal_count: 6
    status: CLEAN
    gate_disposition: PROCEED to Phase 5b audience-gate

  classes_run:
    - STRUCTURAL
    - SCENE-MAP (URI-SCENE-WINDOW)
    - FREQUENCY-BAND
    - EARTH-BET
    - CONSTRAINT
    - RUBRIC-FIDELITY
    - CONTRADICTION
    - DEDUP
    - SUPERFLUOUS
    - PILE-UP
    - AP-SCAN
    - CURVE-SHAPE

  findings:

    # ── HARD findings ──────────────────────────────────────────────────────────

    # (none)

    # ── SIGNAL findings ────────────────────────────────────────────────────────

    - id: signal-001
      type: flag
      class: FREQUENCY-BAND
      what: >
        interest-narrator (NI): 10 entries / 35 bones = 28.6%.
        Band ceiling: 25%. Over by 3.6 percentage points.
        Anchors: @8, @11, @14, @17, @24, @25, @28, @29, @32, @35.
      why: >
        NI is over the 15–25% band. Mitigating disposition: this is a silent
        solitary interior chapter (0 dialogue speakers; Taylor alone on-page throughout);
        NI is the chapter's primary event-delivery mechanism. The scene-map
        and bones-review both carry the "narration is the chapter" characterisation.
        NI is concentrated on peaks and peak-shadows (not distributed to connective
        tissue). Orchestrator disposition question: whether the silent-solitary-interior
        chapter class warrants a band ceiling lift to ~30% or whether 28.6% is
        accepted as a within-tolerance excess given the chapter class. If the stitch
        layers all 10 NI entries at full weight the prose risks register saturation.
      criteria: advisory only — no fixer dispatch. Orchestrator-critic to flag
        disposition at /and-review verdict b01 if the NI density creates a Phase 9
        cold-read signal.

    - id: signal-002
      type: flag
      class: FREQUENCY-BAND
      what: >
        feeling: 2 entries / 35 bones = 5.7%. Band ceiling: 5%.
        Over by 0.7 percentage points.
        Anchors: @14 (feel:1), @32 (feel:2).
      why: >
        Marginally over the 2–5% band. Short-chapter exemption precedent
        pl-2026-05-25-017 applies (small chapter denominator inflates percentage;
        both entries are at peak-bones; both are unexpressed [expressed: no],
        which is the correct register for this chapter's suppression thesis).
        The over is arithmetically trivial (0.7pp on a 35-bone denominator =
        less than one entry's worth of margin). Accepted under the same
        silent-chapter self-flag disposition as c14/c17/c18.
      criteria: advisory only — no fixer dispatch.

    - id: signal-003
      type: flag
      class: FREQUENCY-BAND
      what: >
        exposition: 3 entries / 35 bones = 8.6%. Band: 1–5%.
        In-body first-mention only (excluding @0 episode-open bridge): 2/35 = 5.7%.
        Anchors: @0 (episode-open bridge), @3 (chamberlain first-mention), @27 (Daven + label-reach first-mention).
      why: >
        Over the 1–5% band on the raw count. Author self-flagged with the same
        c14 [6.5%] / c17 [5.6%] / c18 [6.5%] silent-chapter denominator disposition;
        all caps held (episode-open ≤4: 1 entry; first-mention ≤12: 2 entries).
        Both first-mention entries are followability-load items confirmed by the
        chunk_cold_read (jargon/abstraction-density carry; s04 label-reach). The
        @0 bridge is structurally necessary for reader-state refresh at a penultimate
        chapter with high context-load. Disposition: accepted under silent-chapter
        precedent family.
      criteria: advisory only — no fixer dispatch.

    - id: signal-004
      type: flag
      class: CONSTRAINT
      what: >
        memory:2 @9 has no NI co-citation at its anchor. Cite-index @9: [mem:2] only.
        The nearest NI fires at @11 (narrator:2), two bones later.
      why: >
        The memory-without-NI-spine constraint prefers co-citation at the same anchor.
        mem:2 @9 ("the column carries eleven months of entries and the weight of them
        is the floor under this one") is a weight-of-accumulation entry feeding the
        pattern-recognition that fires in NI at @11. The relationship is causal and
        adjacent (the weight at @9 produces the recurrence observation at @11) but
        the NI spine-bond is across rather than at the anchor. This is not a
        violation of the HARD constraint (the entry is not NI-orphaned; NI:2 at @11
        is its immediate consequence) but the gap is present.
      criteria: advisory only — no fixer dispatch. Stitch should treat mem:2 @9 and
        narrator:2 @11 as a two-bone cause-effect pair rather than independent entries.

    - id: signal-005
      type: flag
      class: DEDUP / RUBRIC-FIDELITY
      what: >
        feeling:2 @32 and narrator:9 @32 share the phrase "the lane runs on under her"
        verbatim. feel:2: "her stride does not break at the empty corner and her hands
        stay loose at her sides as the lane runs on under her | expressed: no."
        narrator:9: "the corner stays empty and she walks past the place she would have
        stopped; the lane runs on under her, one node lighter, and the architecture does
        not register the gap the way the corner does."
      why: >
        A verbatim phrase shared across two facets at the same anchor is a surface-level
        duplication. At stitch, both entries will be drawn on for the same bone; if both
        the feeling-register and NI-register arrive at the stitch with identical phrasing,
        the stitcher faces a layering conflict at the chapter's largest single axis-move
        bone (social_tether-prot-collapse -1.5). The feeling layer and NI layer are
        complementary (body's non-expression vs architecture's non-registration) but the
        shared phrase risks collapsing the distinction into a single register.
      criteria: advisory only — no fixer dispatch. Stitch Phase 3 voice-embodiment pass
        should vary the surface phrase between the two layers so the feeling register
        (body/hands) and the NI register (architecture/node) remain distinct.

    - id: signal-006
      type: flag
      class: SUPERFLUOUS
      what: >
        state-updates entry state:7 @25: prop:oc-stylus.position
        in-hand-post-column-close -> approaching-ledger-edge.
        Author flagged as a collapse candidate in the state-updates summary.
      why: >
        The "approaching-ledger-edge" old/new state is a transient intermediate with
        no independently stable prop-condition. Reading state:6 (@24: ledger-edge-beside
        -> in-hand-post-column-close) and state:8 (@26: approaching-ledger-edge ->
        beside-ledger-edge-closed-column) together, the information content of state:7
        is fully subsumed: the approach exists solely to fill the gap between lifting
        and landing. The CFR-2 DO-NOT-FUSE instruction is a stitch directive (three
        distinct physical beats); it does not require three state-entries. The scene-map
        protected-pattern requires the choreography to be rendered as three beats at
        stitch, not that three prop-state records be maintained in the facet.
        The superfluous intermediate adds density without adding information.
      criteria: advisory only — no fixer dispatch. If state-update density is reduced
        in a revision pass, state:7 @25 is the first collapse candidate; collapsing it
        to a single @26 entry recording the completed beside-placement against the @24
        starting position is the minimum reduction.

  # ── Class verdicts ───────────────────────────────────────────────────────────

  class_verdicts:
    STRUCTURAL: PASS — all 56 citations bidirectional; all @anchors resolve to bones 1-35
      (or @0 preamble); id monotonicity clean across all 9 facets.
    SCENE-MAP: PASS — 4 scenes, 35 bones, no gaps/overlaps; ranges contiguous
      (@1-8, @9-17, @18-26, @27-35); frontmatter totals correct.
    FREQUENCY-BAND: SIGNAL (3 flags — NI over, feeling marginal-over, exposition over;
      all with accepted precedent or disposition questions; no HARD).
    EARTH-BET: CLEAN — no Khepri / Gold Morning / Skitter / Brockton Bay / Scion /
      parahuman / shard / cape in any facet text field across all 9 facets. Shape-only
      Earth-Bet callbacks at @11/@12/@14 confirmed shape-language only; no proper-noun
      leak. EARTH-BET HARD fence: PASS.
    CONSTRAINT: SIGNAL (1 flag — mem:2 @9 NI adjacency gap; no HARD violations;
      grounding-license entries resolved; feeling/NI complementarity confirmed).
    RUBRIC-FIDELITY: SIGNAL (1 flag — feel:2/narrator:9 @32 shared phrase; NI
      peak-concentration correct; sensory modality floor met [3 modalities]; state-updates
      registration-vocabulary clean; memory doubled-register clean [distinct anchors]).
    CONTRADICTION: PASS — no state contradictions found; all old-states consistent
      with prior chapter-close; location transitions coherent. Note: prop:oc-stylus
      old-state at state:6 @24 is implicit (no formal b01c18 prop entry); author
      flagged as MARGIT REFERRAL — not a contradiction, a gap in prior registration.
    DEDUP: PASS on entries; 1 SIGNAL on shared phrase across feeling/NI (see signal-005).
    SUPERFLUOUS: SIGNAL — state:7 @25 (approaching-ledger-edge transient; collapse
      candidate; see signal-006).
    PILE-UP: SIGNAL — @24 (5 citations) and @27 (5 citations) are the two highest-load
      bones. Both are structurally justified (peak-bone + scene-open respectively);
      advisory for stitch Phase 3/4 to avoid mechanical layering.
    AP-SCAN: no anomalous patterns beyond frequency-band items. NI over-density is the
      primary AP-SCAN observation; disposition noted under signal-001.
    CURVE-SHAPE: PASS — dramatic_shape falling; four scene rhythm-shapes (falling-
      establishment / falling-recognition / falling-lock / falling-close) form a coherent
      four-beat falling arc; no counter-movement; NI distribution reinforces the shape.

  # ── Phase 5 gate disposition ─────────────────────────────────────────────────

  gate_disposition:
    hard_findings: 0
    signal_findings: 6
    proceed_to_phase_5b: YES
    notes: >
      All HARD classes pass. The 6 signals are advisory. The three frequency-band
      signals carry accepted precedent (silent-solitary-interior chapter class, c14/c17/c18
      family). The constraint and rubric-fidelity signals are stitch-guidance items, not
      facet structural problems. The PILE-UP at @24/@27 is expected for a chapter of this
      type (peak-bone + scene-open concentration). No fixer dispatch required before
      audience-gate. All signals should be forwarded to /and-stitch as carry notes.
