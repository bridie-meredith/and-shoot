```yaml
audit:
  scope: chapter
  target: b01-c12
  gate: /and-facets Phase 5 — final mechanical audit (12 classes; flag-only)
  timestamp: 2026-06-03
  status: FINDINGS-PRESENT
  hard_count: 0
  signal_count: 5
  earth_bet_fence: CLEAN
  grounding_exemption_resolution: PASS (all 3 exemptions resolve; 0 dangling)
  curve_shape_verdict: WARRANTED (two-peak convergence structurally sound; see flag-003)

  findings:

    # ─────────────────────────────────────────────
    # CLASS: STRUCTURAL
    # ─────────────────────────────────────────────

    - id: flag-001
      type: flag
      class: STRUCTURAL
      what: >
        exposition:1 @0 — cite-index shows back=N (no proto-line anchor).
        The entry is a pre-chapter interval bridge (@0-SYNTHETIC); no proto-line
        exists at position 0 by design. The cite-index correctly marks it lonely.
        The R2 exposition shard confirms this is the correct disposition for a
        prior-episode-bridge (same pattern as c06/c11 bridges; promotes zero new
        register entries). No functional gap.
      why: >
        Advisory only. The back=N flag in cite-index is structurally expected for
        a @0-SYNTHETIC entry but may mislead a future reviewer scanning lonely-entry
        tables if the rationale is not visible. No downstream authoring or rendering
        impact — /and-stitch will see the @0 bridge as a renders-as:italic-preamble
        exposition entry with no proto-line decoration required.
      criteria: null

    # ─────────────────────────────────────────────
    # CLASS: FREQUENCY-BAND
    # ─────────────────────────────────────────────

    - id: flag-002
      type: flag
      class: FREQUENCY-BAND
      what: >
        memory — 2 fires / 42 bones = 4.8%, just below the 5-12% chapter floor.
        mem:2 @24 was deleted at R2 on three converging grounds (monument-trigger
        fail, spineless-fire, G5 position-gate). The R2 memory shard explicitly
        accepts the floor-breach as load-bearing sparsity: both legs of the
        doubled-register gate pass (mem:1 @3 Westerosi-monument + mem:3 @38
        Earth-Bet displacement), and the per-scene cap is clean (scene-A cap
        spent on @3; scene-D cap spent on @38; scenes B and C correctly silent).
        The floor-breach is driven entirely by the scene-C delete, which the R2
        judge classified as mandatory.
      why: >
        Advisory only — the doubled-register gate (which is the structural
        requirement for a climax chapter's memory layer) PASSES. This SIGNAL
        is consistent with the task dispatch's instruction to classify the
        floor-breach as advisory given the doubled-register gate. No re-fire
        is warranted; forcing an add to reach 5% would re-introduce the spineless
        functional-callback the R2 delete just removed.
      criteria: null

    # ─────────────────────────────────────────────
    # CLASS: METADATA-INCONSISTENCY
    # ─────────────────────────────────────────────
    # No findings. All facet-file headers (facet slug, episode, author) are
    # consistent with the canonical facet directory. State-updates consolidated
    # frontmatter notes sources correctly as [env-b01-c12, taylor-hebert-kl-122ac-b01-c12].
    # Feeling.md consolidated header lists sources: [taylor-hebert-kl-122ac-b01-c12].
    # Scene-map generated date is 2026-06-03 and emitter is /and-write Phase 7.
    # Cite-index generated date is 2026-06-03. R2-decisions date is 2026-06-03.
    # All consistent. PASS.

    # ─────────────────────────────────────────────
    # CLASS: CURVE-SHAPE
    # ─────────────────────────────────────────────

    - id: flag-003
      type: flag
      class: CURVE-SHAPE
      what: >
        Chapter dramatic_shape = climax. The facet graph shows two convergence
        peaks: @38 (mem:3 + meta:1 + narrator:8 + vibes:13 + vibes:14 = 5 facets)
        and @42 (loc-state:8 + narrator:9 + sensory:5 + state:15 + state:16 +
        state:24 + vibes:15 + vibes:17 + vibes:18 + vibes:19 = 10 facets). Scene-C
        (@17-@28) carries the chapter's enacted decision peaks (peak-bones @19, @22,
        @27). The facet layer correctly concentrates at scene-D interior climax
        (@38/@42) rather than scene-C, which is carried by narrator-interest and
        state-updates (not memory/metaphor convergence). The scene-map names @38
        as INTERIOR CLIMAX and @42 as the terminal cost-filing. Curve-shape verdict:
        the two-peak structure (interior recognition @38 + cold ledger close @42) is
        WARRANTED for the chapter's stated dramatic_shape; neither peak is decoration.
        The @42 10-facet pile-up is dense but structurally earned (the moral_framework
        -1.0 cost-filing is the chapter's terminal event; all 10 entries are distinct
        facets firing on the same terminal bone for convergent structural reasons —
        no redundancy class overlaps; see PILE-UP class below).
      why: >
        Advisory confirmation for /and-stitch. The two-peak structure means the
        stitch phase must NOT flatten @38 into @39 or @40 compression — the
        surface-and-suppress beat requires the @38 peak to register distinctly
        before the advancing-past at @39. The @42 pile-up must render as the same
        flat register despite the facet density, not as a release point. The
        BREACH-AS-COLD-LEDGER-FACT protected pattern in the scene-map governs.
      criteria: null

    # ─────────────────────────────────────────────
    # CLASS: CONTRADICTION
    # ─────────────────────────────────────────────

    - id: flag-004
      type: flag
      class: CONTRADICTION
      what: >
        vibes:13 @38 and vibes:14 @38 both carry `licensed-by: memory:2` in the
        vibes facet file. vibes:19 @42 also carries `licensed-by: memory:2`.
        mem:2 was DELETED at R2 (the memory R2 shard records DELETE with cascade-1).
        The correct memory anchor at @38 is mem:3 (confirmed by the cite-index:
        mem:3 @38 back=Y co=[meta:1, narrator:8, vibes:13, vibes:14]; and by the
        metaphor R2 shard which explicitly corrected the same R1 error in meta:1's
        licensed-by field from memory:2 to memory:3). The cite-index also records
        vibes:13 lic-out as [memory:2, feeling:2, ...] — the stale reference
        propagated from the R1 vibes author (who wrote before the memory R2 delete)
        into the cite-index lic-out fields. The vibes facet file was authored R1-BLIND
        and the vibes R2 pass (if it ran as graph-aware) did not correct the stale
        memory:2 citations in vibes:13, vibes:14, and vibes:19. No vibes R2 shard
        appears in the consolidated .r2-decisions.md (shards list: interest-narrator,
        memory, feeling-taylor-hebert-kl-122ac, metaphor, exposition-author).
      why: >
        The licensed-by references in vibes:13, vibes:14, and vibes:19 point to a
        deleted facet entry (mem:2). Downstream, /and-stitch's Phase 0 cite-index
        consistency check and any future /and-review pipeline pass will surface a
        broken license reference if the vibes file and cite-index lic-out fields
        are not corrected to reflect mem:3. The structural licensing for vibes:13
        and vibes:14 at @38 is valid — the co-location with mem:3 @38 is
        bidirectionally confirmed in the cite-index (back=Y, co=[...]), so the
        entries themselves are not at risk; only the licensed-by attribution is stale.
        vibes:19's memory:2 citation is similarly stale but the structural validity
        of the entry holds through its other licensed-by sources (feeling:2,
        state-update:8, proto:38/:39/:42, world-build:cl05-Khepri-repetition-suppressed).
      criteria: null

    # ─────────────────────────────────────────────
    # CLASS: DEDUP
    # ─────────────────────────────────────────────
    # No findings. Checked: no two vibes entries on the same target carry the same
    # keyword. The vibe-set gate-2 coherence audit in the vibes file (hint-3) confirms
    # vibes:17 (++) extends vibes:10 (+) within the same episode facet file, which is
    # permitted per the rubric (the + establishes the keyword for the ++ in the same
    # facet, provided the + appears first — confirmed: vibes:10 @27 precedes vibes:17
    # @42 in file order). Feeling entries: feel:1 @20 (hand) and feel:2 @40 (breath)
    # — distinct somatic vocabulary, no saturation, no dup. NI entries: no two narrator
    # entries on the same proto-line (narrator:10 @24 is a distinct position from
    # narrator:5 @19 and narrator:7 @27). No dedup issue found.

    # ─────────────────────────────────────────────
    # CLASS: SUPERFLUOUS
    # ─────────────────────────────────────────────
    # No findings. The chapter total is 73 facet entries across 42 bones (26/42 proto-lines
    # decorated). Every entry in the graph has a structural role confirmed by the R2
    # decision shards (where R2 shards exist) or by the R1 author's refuse-log (where R2
    # was not separately dispatched). The 10 lonely entries in the cite-index are all
    # confirmed load-bearing in the relevant facet rubric context (see cite-index lonely
    # table; each is validated by the R2 judge's KEEP verdict or by R1 STRUCTURAL need:
    # loc-state:3 @8 = feed-station sub-anchor for circuit-close; narrator:2 @7 = Wren-
    # route withheld spine first reaching page; narrator:4 @14 = WEAVE-FIXABLE confirmed
    # KEEP by NI R2; narrator:6 @21 = body-fact withhold seal; narrator:10 @24 = R2 KEEP
    # on own NI merits; sensory:2 @16 = thermal up tag, bay-warmth body-paired to @16 scene-B
    # close; state:5 @13 = covering-sheet-open first-touch; state:14 @32 = five-ward
    # coverage-scale aggregate threshold; feel:1 @20 = R2 KEEP 5/5; exposition:1 @0 = @0-
    # SYNTHETIC interval bridge, no proto-line by design). No superfluous entry identified.

    # ─────────────────────────────────────────────
    # CLASS: CONSTRAINT
    # ─────────────────────────────────────────────

    - id: flag-005
      type: flag
      class: CONSTRAINT
      subclass: RUBRIC-FIDELITY / card-resolution
      what: >
        mem:1 @3 target reference `cond-kl-witch-label-formation-122ac` — flagged
        for margit-referral in the memory R2 shard (signal: the target slug may not
        resolve to a warehouse card at current canonicalization). The R2 shard ships
        the entry flagged-not-deleted, concluding the gloss is structurally clear and
        the target reference is narratively correct. The dispatch brief instructs this
        class as SIGNAL / card-resolution / margit-referral (not HARD if gloss is clear
        and author defense exists). Both conditions are met: the gloss defines the
        Westerosi-current monument clamp explicitly ("the word these streets keep for
        women like her"), and the R2 shard provides the author defense. Similarly,
        vibes:4 @9 (loc:east-water-gate-lanes) and vibes:16 @30 (loc:the-muddy-way)
        reference location slugs that have no warehouse card confirmed in the file
        (vibes file hint-2 notes east-water-gate-lanes has no warehouse card; the slug
        is drawn from the bones header locations field). The muddy-way appears in the
        scene-map as the second-cluster location but no standalone warehouse card is
        confirmed.
      why: >
        If these slugs are not resolved by margit before /and-stitch, the stitcher's
        state-grounding pass may encounter unresolvable location references in the
        vibes facet. The gloss-text in the vibes entries is structurally readable
        without warehouse card resolution, so /and-stitch is unlikely to hard-fail,
        but the card-resolution gap is a known open item. Margit-referral is the
        correct channel; no fixer action required before stitching.
      criteria: null

    # ─────────────────────────────────────────────
    # CLASS: AP-SCAN
    # ─────────────────────────────────────────────
    # No findings. Checked all 10 narrator-interest entries against AP-SCAN classes:
    # AP10 inverted-predicate ("is what"/"is the"/"means today" sentence-final): 0
    # instances across all 10 NI fires (confirmed by NI R2 PATTERN-SCAN). Checked
    # feeling entries against URI-FACETS-CYCLE-1 REJECT signatures: no named-feeling
    # vocab, no hedge, no simile, no metaphor, no compound-naming, no subject-shift to
    # abstraction-noun. Checked metaphor against AP1–AP7/AP12: all clear per meta:1
    # R2 shard. No AP-SCAN class finding.

    # ─────────────────────────────────────────────
    # CLASS: TASTE-FLAG
    # ─────────────────────────────────────────────
    # No findings. The R2 decisions consolidated file records f-r2-counts:
    # {f-r2-1: 0, f-r2-2: 1, f-r2-3: 0, f-r2-4: 0}. The single f-r2-2 (motive-honesty
    # flag from the memory R2 shard, mem:2 @24 delete classified as adjacent/prior-context-
    # dependency) is a logged delete, not a surviving entry. No living taste-flag pattern
    # earns TASTE-FLAG class promotion here. The bones-review REGISTER-AS-MANNERISM advisory
    # (closes-the-X x5 / reaches-the-X x3) is a carry-to-stitch signal per the scene-map,
    # not a facet-layer TASTE-FLAG. No new pattern flagged at this gate that would earn
    # AP-SCAN promotion.

    # ─────────────────────────────────────────────
    # CLASS: PILE-UP
    # ─────────────────────────────────────────────
    # Pile-ups confirmed from cite-index:
    #   @38 (5): mem:3, meta:1, narrator:8, vibes:13, vibes:14 — WARRANTED.
    #     The accounting-reaches-the-shape-word bone is the INTERIOR CLIMAX; the 5-facet
    #     convergence is load-bearing (memory displacement clamp + metaphor callback cipher
    #     + narrator foreknowledge-clamp + two distinct vibes expansions on atonement-as-
    #     repetition and khepri-memory-as-standard). No two entries carry the same load.
    #   @42 (10): loc-state:8, narrator:9, sensory:5, state:15, state:16, state:24,
    #     vibes:15, vibes:17, vibes:18, vibes:19 — WARRANTED.
    #     The breach-column-takes-the-threshold-entry bone is the terminal event
    #     (moral_framework -1.0 cost-filing, chapter close). 3 distinct state entries target
    #     3 distinct fields (breach-column-entry, time_of_day, moral_framework_axis). 4 vibes
    #     entries target 3 distinct entities (actor:taylor x1, loc:feed-station x2, episode x1)
    #     on 4 distinct keywords. loc-state and narrator carry the structural close. sensory:5
    #     carries licensed-grounding grd-002. No redundancy class overlap identified.
    #   @30 (5): sensory:3, state:13, state:23, vibes:12, vibes:16 — WARRANTED.
    #     The insects-fill-muddy-way-upper-margin bone is the capability +0.5 peak-shadow;
    #     licensed-grounding grd-001 accounts for sensory:3; the two state entries target
    #     distinct fields (ward-coverage-notes.content and fauna_sense_status.coverage-scale
    #     via state:23); the two vibes entries target distinct entities (actor:taylor and
    #     loc:the-muddy-way) on distinct keywords (residue-not-spectacle and fifth-ward-
    #     circuit-closed).
    # Verdict: all three pile-ups WARRANTED. No PILE-UP finding issued.

    # ─────────────────────────────────────────────
    # CLASS: RUBRIC-FIDELITY
    # ─────────────────────────────────────────────
    # No hard RUBRIC-FIDELITY findings beyond the card-resolution signal captured
    # under flag-005 (CONSTRAINT/RUBRIC-FIDELITY overlap). All R2 judge passes that
    # produced shards (NI, memory, feeling, metaphor, exposition) confirm their
    # respective rubric disciplines. Vibes has no R2 shard in the consolidated file,
    # which means a full graph-aware R2 pass for the vibes layer was not formalized —
    # this is the precondition that allowed the stale memory:2 citations (flag-004)
    # to survive. The absence of a vibes R2 shard is itself noted as a process gap
    # (the vibes file has R1-provisional anchor-hints but no R2 judge disposition block
    # signed with a cite_index_hash). This is a SIGNAL, not a HARD finding, because
    # the cite-index co-citation structure for vibes entries is independently bidirectional
    # and all vibes entries resolve structurally through the graph.

  # ─────────────────────────────────────────────
  # SPECIAL CHECKS (per dispatch brief)
  # ─────────────────────────────────────────────

  earth_bet_scan:
    verdict: CLEAN
    scope_checked: >
      All text fields of every facet entry: NI rationale fields (10 entries),
      memory target-refs + gloss text (2 entries surviving), metaphor figure +
      licensed-by text (1 entry), vibes entity-targets + keyword arrays (19 entries),
      feeling somatic-tells (2 entries), sensory notes (5 entries), exposition
      gloss-text (2 entries), state old/new values (24 entries), location-state
      facet description fields (8 entries).
    findings: >
      No Worm-canon proper nouns found in any text field across all facets.
      Specifically: no "Khepri", no "Gold Morning", no "Gold-Morning", no "Brockton
      Bay", no "Skitter", no "PRT", no "parahuman", no "shard", no cape names, no
      Endbringer names. The @38 cipher reads throughout as "the shape-word" / "the
      thing she did when the world was ending" / "the older shape, built in a different
      city" / "the thing-she-did-at-Gold-Morning word" (the last appearing only in the
      scene-map narrative description field, not in any renderable facet entry). The
      scene-map's narrative field ("the thing-she-did-at-Gold-Morning word" @scene-D
      description) is a production-internal document, not a rendered facet; the facet
      entries themselves carry only shape-language. The exposition file confirms: "Earth-Bet
      fence confirmation: CLEAN." Memory R2 shard: "Earth-Bet hard-fence: CLEAN."
      Metaphor R2: "Earth-Bet fence: metaphor text — 'the architecture is the older shape,
      built in a different city.' No proper nouns." NI R2 @38: "shape-language only, no
      proper noun (no Khepri, no Gold Morning)." FENCE CLEAN on full scan.

  grounding_exemption_resolution:
    verdict: PASS
    grd-001:
      status: satisfied
      resolved_by: [sensory:3 @30, sensory:4 @40]
      ledger_license: GROUNDING-REQUIRED
      cite_index_back: sensory:3 back=Y, sensory:4 back=Y
      finding: >
        Both entries carry licensed-grounding-exception: grd-001 in the sensory
        facet file. The grounding-ledger records status: satisfied, satisfied_by:
        sensory:3, sensory:4, with a resolution_note confirming scope and content.
        These entries are EXEMPT from the sensory FREQUENCY-BAND cap per the dispatch
        brief. They do not count toward the 3-6% countable-sensory band. No
        FAULT-GROUNDING-LICENSE-DANGLING.
    grd-002:
      status: satisfied
      resolved_by: [sensory:5 @42]
      ledger_license: GROUNDING-REQUIRED
      cite_index_back: sensory:5 back=Y
      finding: >
        Entry carries licensed-grounding-exception: grd-002. The grounding-ledger
        records status: satisfied, satisfied_by: sensory:5, with resolution_note
        confirming scope (light: late-afternoon-surface-brightness -> end-of-day-dimming
        at @42; grounding the breach-column filing as a person at a surface; BREACH-AS-
        COLD-LEDGER-FACT preserved; @38 cipher untouched). No FAULT-GROUNDING-LICENSE-DANGLING.
    countable_sensory_verification:
      countable_entries: [sensory:1 @12, sensory:2 @16]
      exempt_entries: [sensory:3 @30, sensory:4 @40, sensory:5 @42]
      countable_rate: 2/42 = 4.8%
      band: 3-6%
      verdict: IN-BAND

  memory_ni_spine_check:
    mem_1_at_3: narrator:1 @3 present in cite-index (back=Y, co=[loc-state:2, mem:1, vibes:3]). NI SPINE CONFIRMED.
    mem_3_at_38: narrator:8 @38 present in cite-index (back=Y, co=[mem:3, meta:1, vibes:13, vibes:14]). NI SPINE CONFIRMED.
    mem_2_deleted: mem:2 @24 was deleted at R2; spine gap is moot; NI fires @24 on own merits (narrator:10 @24 is a KEEP on independent NI grounds).

  scene_map_coverage:
    total: 42/42 bones in exactly one scene
    scene_A: @1-@10 (10 bones)
    scene_B: @11-@16 (6 bones)
    scene_C: @17-@28 (12 bones)
    scene_D: @29-@42 (14 bones)
    gaps: none
    overlaps: none
    dialogue: none (silent chapter — zero dialogue-anchor bones; no per-character dialogue files; FAULT-UPSTREAM-LEAK check trivially clean)
    sensory_per_scene_caps:
      scene_A: sensory:1 @12 (1 countable — IN-CAP ≤3)
      scene_B: sensory:2 @16 (1 countable — IN-CAP ≤3)
      scene_C: 0 countable
      scene_D: sensory:3/@30, sensory:4/@40, sensory:5/@42 all licensed-grounding-exempt — cap N/A per dispatch brief
    verdict: CLEAN

  # ─────────────────────────────────────────────
  # SUMMARY
  # ─────────────────────────────────────────────

  summary:
    hard_count: 0
    hard_list: []
    signal_count: 5
    signal_list:
      - flag-001 (STRUCTURAL — exposition:1 @0 back=N expected for @0-SYNTHETIC; advisory)
      - flag-002 (FREQUENCY-BAND — memory 4.8% just under 5% floor; load-bearing sparsity; doubled-register gate PASSES)
      - flag-003 (CURVE-SHAPE — two-peak @38/@42 WARRANTED verdict; /and-stitch protection noted)
      - flag-004 (CONTRADICTION — vibes:13, vibes:14, vibes:19 licensed-by cites deleted mem:2; correct anchor is mem:3; stale reference; structural validity of entries intact)
      - flag-005 (CONSTRAINT/RUBRIC-FIDELITY — three card-resolution gaps: cond-kl-witch-label-formation-122ac target unconfirmed in warehouse; loc:east-water-gate-lanes and loc:the-muddy-way no warehouse card; margit-referral recommended; gloss-text readable without resolution)

    convergence_input: >
      0 HARD findings. 5 SIGNAL (advisory) findings. Chapter is mechanically CLEAN
      at this gate. Carry-to-stitch items:
      (1) flag-004: vibes:13/14/19 stale memory:2 citations — fixer may correct to
          memory:3 before /and-stitch if cite-index consistency check is blocking;
          otherwise treat as informational.
      (2) flag-005: margit-referral for three unresolved location/condition slugs —
          non-blocking for /and-stitch but should be resolved before project-stable.
      (3) The bones-review REGISTER-AS-MANNERISM advisory and ABSTRACTION-DOMINANT
          advisory (both accept-with-rationale per scene-map Phase-6 bone-gate) carry
          into /and-stitch Phase 4 per scene-map protected-patterns; these are
          stitch-layer concerns, not facet-layer faults.
      (4) DEC-0076 Phase 8.5 checks (KHEPRI-SURFACE-AND-SUPPRESS at @38 register-
          must-not-bury; CAUSAL-BRIDGE-@31 legibility) are stitch-layer verifications,
          armed here by the scene-map; facet layer has no action.
```
