```yaml
audit:
  scope: chapter
  target: b01-c13
  gate: /and-facets Phase 5 — final facets audit (12-class cross-cutting graph)
  timestamp: 2026-06-03
  status: FINDINGS-PRESENT
  hard_count: 1
  signal_count: 4
  earth_bet_fence: CLEAN
  curve_shape_verdict: SHAPE-OK
  seam_env_005_ruling: NOT-HARD-CONTRADICTION (persists as flag; see flag-002)
  vibes_ap11_ruling: DOES-NOT-FIRE (4 fires; distinct event-frames; no string-overlap)
  pile_up_19_verdict: WARRANTED
  pile_up_7_verdict: WARRANTED

  findings:

    # ─────────────────────────────────────────────
    # CLASS 1: STRUCTURAL
    # ─────────────────────────────────────────────

    - id: fault-001
      type: fault
      class: STRUCTURAL
      what: >
        state-updates.md (taylor-hebert-kl-122ac source slice), per-entry
        annotation block (lines 148–151): the annotation for state:16 and state:17
        (both @16) reads "POV-co-cite-RESOLVED (NI:4 @16)". The inline comment on
        state:16 entry reads "NI:4 fires here." No NI entry exists at @16 in the
        locked NI file. The NI file has NI:3 @17 ("his name on her list, now his
        hands flat on the table") and NI:4 @19 ("the word arrives... it is
        contempt"). The R2 NI decision log (active-project/theater/facets/
        .r2-decisions.md, NI shard, line 28) explicitly acknowledges this identity
        confusion: "the dispatch refers to 'NI:3 @16' — the locked R1 entry NI:3
        anchors @17... the @16 figure is the adjacent state-updates re-anchor for
        the POV register-state, not the NI anchor."
      why: >
        The POV-actor state-updates rubric requires every actor POV register-state
        entry to carry a narrator-interest co-citation. State:16 and state:17 are
        anchored @16 and claim NI co-citation; the NI entry the carve-out intends
        (NI:3) fires @17, not @16. As annotated, the co-citation claim is for a
        non-existent NI:4 @16. A stitcher, fixer, or reviewer reading only the
        per-entry annotation lines will find "RESOLVED (NI:4 @16)" and find no
        such NI entry, breaking the audit trail and leaving the co-citation
        requirement apparently unmet. The carve-out prose reasoning (lines 125–136
        of state-updates.md) does articulate the design intent — fire once across
        the @16–@17 approach-peak window per § Cross-facet do-not-double-fire —
        but the label and inline comment contradict it.
      criteria: >
        The per-entry annotation for state:16 and state:17 must correctly name the
        NI entry providing the co-citation spine. The annotation must read
        "NI:3 @17 (adjacent-beat spine — carve-out: single-fire across approach-peak
        window per § Cross-facet do-not-double-fire)" and the inline comment on
        the state:16 entry must not say "NI:4 fires here." The carve-out rationale
        in lines 125–136 is defensible and need not change; only the annotation
        labels must match the actual NI entry id (NI:3) and anchor (@17).

    # Structural: all other checks pass
    # — ID monotonicity: all facet IDs within each file strictly monotonically
    #   increasing; mem:1 absent (deleted at R2, IDs preserved per rubric). PASS.
    # — Bidirectional citation: every [<prefix>:<id>] token in proto-lines resolves
    #   to a facet entry; every entry has back=Y except exposition:1 @0 (back=N,
    #   legitimately uncited as the synthetic pre-chapter preamble). PASS.
    # — Behavior-card headers: halvard dialogue file declares westeros-septon
    #   (card exists); taylor dialogue file declares taylor-hebert-kl-122ac (actor
    #   card present). Both resolve. PASS.
    # — Dialogue anchor resolution: proto-lines @26/27/28 carry halvard:1,
    #   taylor:1, halvard:2. All three resolve to dialogue file entries. PASS.

    # ─────────────────────────────────────────────
    # CLASS 2: FREQUENCY-BAND
    # ─────────────────────────────────────────────

    - id: flag-001
      type: flag
      class: FREQUENCY-BAND
      what: >
        Sensory density: 4 entries / 31 bones = 12.9%. Standard ceiling is 3–6%.
        No GROUNDING-REQUIRED license was issued (grounding-ledger has 0 open
        entries; Phase 2.5 verdict was GROUNDED with no licensed adds). The sensory
        file carries a self-authored density defense (modality-diversity: 3
        distinct modalities across 4 fires; per-brief grounding priority for all
        4 key anchor zones; per-scene cap compliance: s01=1, s02=0, s03=1, s04=2;
        scene-B zero-fire gradient preserved). The grounding-ledger confirmed no
        airless stretch requiring above-band fires.
      why: >
        Above-band sensory density without a grounding-ledger GROUNDING-REQUIRED
        license is a SIGNAL. Does not block Phase 5b (no airless risk confirmed;
        per-scene caps clean). Advisory for stitcher: if /and-stitch Phase 4
        voice-embodiment review identifies any sensory fire as redundant at its
        anchor, it may be culled without structural damage. If all four fires are
        confirmed load-bearing at Phase 9 cold-read, no action needed.
      criteria: null

    # Other frequency-band checks pass:
    # — Memory 6.5% (2/31): in-band 5–12%. PASS.
    # — Feeling 6.5% consolidated (2/31): per-character per-scene cap ≤1 clean
    #   (Taylor 1 fire scene-C; Halvard 1 fire scene-D). Soft advisory per R2
    #   shard (31-bone short chapter; two characters; defensible). PASS.
    # — Metaphor 0%: in-band 0–3%. PASS.
    # — NI 22.6% (7/31): in-band 15–25%. PASS.
    # — Exposition 3.2% (1 body-line / 31 bones; @0 bridge is synthetic pre-body):
    #   in-band 1–5%. PASS.
    # — Dialogue per-anchor cap ≤3: @26=1, @27=1, @28=1. All under cap. PASS.

    # ─────────────────────────────────────────────
    # CLASS 3: METADATA-INCONSISTENCY
    # ─────────────────────────────────────────────

    # All nine facet file headers checked. episode: consistently b01-c13.
    # Facet type declarations match file names. Author fields present.
    # R2-judged fields present where applicable. Consolidated files (feeling.md,
    # state-updates.md) carry correct multi-source frontmatter format per
    # r3-signal-001. No metadata inconsistencies. PASS.

    # ─────────────────────────────────────────────
    # CLASS 4: CURVE-SHAPE
    # ─────────────────────────────────────────────

    # CURVE-SHAPE VERDICT: SHAPE-OK.
    # dramatic_shape: hinge. Four scenes: s01 low-heat establishment (@1–@9),
    # s02 rising (@10–@18), s03 hinge-fulcrum peak (@19–@23), s04 held-breath
    # enactment then cold-close (@24–@31).
    # NI distribution: fires cluster at s02 peaks (@15, @17), s03 hinge (@19,
    # @23), s04 foreclosure/carry (@28, @30); silent across establishment and
    # mechanism bones. Vibes: 3 fires @7 (s01 peak), 3 @15/@17 (s02 peaks), 3
    # @19 (s03 hinge), 6 across s04 (@26–@31). Memory: quiet-beat placement
    # (@23 post-hinge, @30 post-departure) per rubric. R2 NI pattern-scan
    # independently confirms density-aligns-with-pressure. SHAPE-OK.

    # ─────────────────────────────────────────────
    # CLASS 5: CONTRADICTION
    # ─────────────────────────────────────────────

    - id: flag-002
      type: flag
      class: CONTRADICTION
      what: >
        SEAM-ENV-005 @24 time-of-day residual: state-updates-env entry state:11
        (@24) records "studio.time_of_day: evening -> morning" (carve-out: scene-D
        time inferred from circuit-walk context, multi-day gap). Location-state:6
        (@24) records "the-hook-lower-water-trough | afternoon." Both entries are
        anchored @24 (the scene-D trough entry / place-anchor). The two values
        ("morning" and "afternoon") are inconsistent. The state-updates carve-out
        preamble explicitly acknowledged the inference and called for R2 ratification
        (SEAM-C13-ENV-003). The R2 pass did not explicitly align the two values.
      why: >
        The stitcher receives conflicting time-of-day signals for scene-D from two
        different facets. Morning vs. afternoon affects ambient light description
        and sensory texture at the trough. Not structurally blocking (scene-D is
        all-held; no narrative axis depends on exact time of day). Advisory for
        stitcher: adopt loc-state:6 "afternoon" as the authoritative value.
        Loc-state:6 is the scene-open place-anchor authored with scene-context; it
        post-dates the state-updates inference and is more specifically anchored to
        the scene open. If the stitcher chooses "morning," no narrative harm results,
        but "afternoon" is the better-sourced value.
      criteria: null

    # No other incompatible state values found on the same anchor across any
    # facet pair. Location-state and state-updates-env agree on all other
    # transitions. Prop holder chain (oc-d06-document: green-apparatus-possession
    # → table-surface @11 → magistrate-hand @15) is monotonic. No actor at
    # unvisited location. No prop used without possession. PASS.

    # ─────────────────────────────────────────────
    # CLASS 6: DEDUP
    # ─────────────────────────────────────────────

    # @28 DEDUP VERDICT: COMPLEMENTARY — BOTH KEPT.
    # halvard:2 @28 = Halvard's spoken words (lament aloud). NI:6 @28 = Taylor's
    # interior read of them ("the long way off is her, and he does not know it is
    # a mirror he is holding up"). His words / her recognition of the dramatic
    # irony are distinct content layers. The dramatic irony requires both
    # simultaneously. Confirmed by R2 dialogue judge. No yield warranted. PASS.
    #
    # @19 (9 entries) and @7 (7 entries): each entry carries a distinct semantic
    # payload confirmed in the cite-index and per-facet R2 decisions. No two
    # entries duplicate the same load at the same anchor. See Class 11 for full
    # warrant review. PASS.

    # ─────────────────────────────────────────────
    # CLASS 7: SUPERFLUOUS (lonely-entry three-axis test)
    # ─────────────────────────────────────────────

    # Seven lonely entries in cite-index: loc-state:2 @2, sensory:2 @20,
    # sensory:3 @25, state:7 @13, feel:2 @21, exposition:1 @0, exposition:2 @12.
    # Three-axis test applied per entry:
    # — loc-state:2 @2: trestle-table active, household-agent posted; the @3–@9
    #   confrontation geometry depends on this placement. Axis 1 (spatial grounding
    #   for downstream scene geometry). NOT SUPERFLUOUS.
    # — sensory:2 @20 (tallow-smoke): scene-C entry just after the hinge; locates
    #   the naming in a body on known lane ground. Axis 2 (grounding requirement per
    #   scene-map). NOT SUPERFLUOUS.
    # — sensory:3 @25 (trough-rim-cool): scene-D trough arrival; locates both bodies
    #   at the water-point. Axis 2. NOT SUPERFLUOUS.
    # — state:7 @13 (procedural-form blank→inscribed): VERDICT-BEFORE-SPEECH protected
    #   pattern; prop-state cue the stitch layer requires. Axis 3 (narrative load-
    #   bearing prop mutation). NOT SUPERFLUOUS.
    # — feel:2 @21 (breath/weight): s03 hinge somatic; the body bearing the naming
    #   word; confirmed load-bearing by R2 judge (without it reader gets cognition
    #   but not the body bearing it). Axis 3. NOT SUPERFLUOUS.
    # — exposition:1 @0: prior-episode-bridge; @0-SYNTHETIC; legitimately uncited;
    #   structurally necessary (no lens facet can hold the pre-chapter interval recap).
    #   NOT SUPERFLUOUS.
    # — exposition:2 @12: first-mention gloss; ctx-001 depends on it; always-gloss
    #   class. NOT SUPERFLUOUS.
    # All seven lonely entries pass. PASS.

    # ─────────────────────────────────────────────
    # CLASS 8: CONSTRAINT
    # ─────────────────────────────────────────────

    # Memory NI-spine:
    # mem:2 @23 ↔ narrator:5 @23: co-located and back-cited. SATISFIED.
    # mem:3 @30 ↔ narrator:7 @30: co-located and back-cited. SATISFIED.
    # (mem:1 deleted at R2; spine requirement vacated by deletion.) PASS.
    #
    # State-updates actor-POV NI co-citation:
    # state:14/15 @7 → narrator:1 @7: NI:1 fires @7. SATISFIED.
    # state:16/17 @16 → NI:3 @17 (adjacent-beat spine; see fault-001 for label
    #   error): carve-out rationale is substantively sound; NI:3 exists and fires @17.
    #   Co-citation substantively present across the approach-peak window per § Cross-
    #   facet single-fire rule. Label error noted at fault-001.
    # state:18/19 @19 → narrator:4 @19: NI:4 fires @19. SATISFIED.
    # state:20 @30 → narrator:7 @30: NI:7 fires @30. SATISFIED. PASS.
    #
    # EARTH-BET HARD-FENCE — full scan result: CLEAN.
    # Scanned: interest-narrator (7), memory (2), sensory (4), location-state (7),
    # metaphor (0), vibes (17), exposition (2), feeling (2), state-updates (20),
    # scene-map protected-patterns fields, dialogue halvard (2 utterances + 2
    # objectives), dialogue taylor (1 utterance + 1 objective), both drafts sidecars.
    # Zero instances of: Khepri / Brockton Bay / Skitter / Gold Morning / shard /
    # parahuman / cape / swarm / Endbringer / PRT / Scion / Cauldron / trigger (cape
    # sense) / Worm / Queen Administrator / Undersiders / Protectorate / Wards / Lung.
    # mem:2's "a coming fire will spend them, as weather" is shape-language in the
    # persona's own functional vocabulary — confirmed clean per R2 memory judge. CLEAN.
    #
    # Exposition source-traceability and license-completeness:
    # exposition:1 @0: all sources trace to showrunner-memory:b01c13, exposition-
    #   b01-c05:sera-protection-architecture, glossed-terms:the-report-sheet/jarvis-
    #   coin-kl-courier, cond-kl-court-state-122ac. Three audience-gap licenses present
    #   and substantiated. PASS.
    # exposition:2 @12: sources trace to showrunner-memory:b01c13s02.chunk, scene-map
    #   b01-c13, glossed-terms:ward-elder. ctx-001 satisfied. PASS.
    #
    # Exposition scene-open fire-rule: loc-state fires at all four scene-opens (@1,
    #   @10, @19, @24), so condition (b) fails for all four. Exposition correctly fires
    #   0 scene-open-orient entries. PASS.
    #
    # First-mention coverage: Aldric is the only new named individual. exposition:2
    #   @12 covers him. Household-agent, magistrate, green-faction-clerk, supplier's-son
    #   are noun-form minor figures with decodable role-labels; appropriately excluded per
    #   R2 exposition judge. First-mention coverage complete. PASS.
    #
    # Scene-map coverage (URI-SCENE-WINDOW): 31/31 protolines in exactly one scene;
    #   gaps: none; overlaps: none. SATISFIED.
    #
    # Per-scene caps: sensory ≤3/scene: s01=1, s02=0, s03=1, s04=2. All within cap.
    #   Feeling ≤1/char/scene: Taylor 1 in scene-C only; Halvard 1 in scene-D only.
    #   Both within cap. Metaphor ≤1/scene: 0 everywhere. Exposition scene-orient ≤1:
    #   0 fires. All caps clean. PASS.

    # ─────────────────────────────────────────────
    # CLASS 9: AP-SCAN
    # ─────────────────────────────────────────────

    # VIBES AP11 — contempt-without-refusal 4 fires on Taylor (@7, @17, @19, @29):
    # DOES NOT FIRE.
    # The four fires are distinct event-frames:
    #   vibes:1 @7: s01 satisfied-coercion-posture (resentment acquires specific
    #     object; apparatus-coercion first observed as discrete event).
    #   vibes:6 @17: s02 consequence-image (abstraction-of-the-list-now-a-body-at-a-
    #     table; her intelligence delivery ending in hands flat on a table).
    #   vibes:9 @19: s03 naming (contempt as a finding-not-a-decision; chapter spine).
    #   vibes:14 @29: s04 enactment (departure-mid-speech-the-contempt-made-physical;
    #     not-pretending-the-counter-is-open).
    # Tag-list strings: zero string-overlap across the four entries. Each names a
    # categorically distinct scene-event (coercion-observation / consequence-image /
    # naming-threshold / enactment-departure). AP11 does not fire: four fires are
    # warranted for a four-scene chapter where contempt-without-refusal is the chapter
    # register and each scene delivers one distinct axis of it. PASS.
    #
    # NI register-tic (AP10 inverted-predicate template): R2 NI pattern-scan checked
    # the "is what" / "is the X" / "means today" sentence-final chassis across all 7
    # NI entries. Zero instances. (@28 "the long way off is her" is mid-sentence
    # identification, not the sentence-final definitional-collapse chassis.) PASS.
    #
    # AP-CHASSIS-CONTAMINATION (Halvard must not carry Taylor's em-dash/semicolon
    # chassis): halvard:1 @26 uses one em-dash as a breath-extension ("I knew him —
    # knew the lanes he walked") within the stated allowance per the drafts sidecar
    # anti-pattern ("the occasional plain dash only as a breath, never the semicolon-
    # spine"). halvard:2 @28: zero em-dashes, zero semicolons — pure period-stop +
    # "And"-start structure. taylor:1 @27 carries the em-dash chassis appropriate to
    # her card. No chassis contamination of Halvard. PASS.

    # ─────────────────────────────────────────────
    # CLASS 10: TASTE-FLAG
    # ─────────────────────────────────────────────

    - id: flag-003
      type: flag
      class: TASTE-FLAG
      what: >
        taylor:1 @27 — "both columns, all the way down" is the closest the
        chapter's dialogue comes to ledger-as-metaphor language that a hostile
        Phase 5b reviewer could flag as theme-adjacent or self-narrativizing. The
        R2 dialogue judge holds it clean: "operational accounting language about
        THIS specific case, not a meta-gesture at her own story."
      why: >
        Advisory for Phase 5b audience gate. If all three reviewers accept it, no
        action. If a reviewer objects, the documented defense is available (it is
        a count of the specific situation — Halvard's slower-method cost and her
        own protection arithmetic — not a meta-gesture at the road-to-hell irony).
      criteria: null

    - id: flag-004
      type: flag
      class: TASTE-FLAG
      what: >
        halvard:2 @28 — "a wiser hand wrote off": the R2 dialogue judge notes
        this is the only place Halvard's register edges toward implied comparative
        self-judgment rather than pure naming. Held within §Voice-tells ("names
        his own uncertainty / does not claim superior judgment").
      why: >
        Advisory for Phase 5b. If a reviewer flags this as self-deprecation
        stepping outside the septon's plain-witness register, the defense is that
        "wiser hand" concedes others could read better (§Voice-tells: does not
        claim superior judgment), consistent with the card. Does not claim he IS
        the wiser hand.
      criteria: null

    # ─────────────────────────────────────────────
    # CLASS 11: PILE-UP REVIEW
    # ─────────────────────────────────────────────

    # @19 (9 facets): WARRANTED.
    # Entries: loc-state:5 (scene-C place-anchor / scene-open required); narrator:4
    # (naming interior / chapter spine, the s03 peak cannot deliver without it);
    # state:9 (time-of-day evening advance, required at scene-open with multi-day gap);
    # state:10 (location magistrate-hall→hook-lane, required at scene-open); state:18
    # (political_register_prot_axis 4.5→5.0, one of the two canonical state mutations
    # the chapter delivers); state:19 (knowledge contempt-standing, the other); vibes:7
    # (actor contempt-without-refusal crystallized); vibes:8 (loc contempt-crystallized-
    # here); vibes:9 (episode contempt-named). Every entry is structurally required at
    # this anchor. No entry survives removal without losing load-bearing information.
    # NOT over-decoration.
    #
    # @7 (7 facets): WARRANTED.
    # Entries: narrator:1 (read-discipline / pre-calc registration of coercion-as-
    # confirmation); state:3 (prop oc-fish-account-ledger open→closed, the physical
    # event the peak is built on); state:14 (axis +0.5, first of two POV state
    # mutations at @7); state:15 (knowledge diffuse→fixed, second POV mutation);
    # vibes:1 (actor contempt-without-refusal at s01 peak); vibes:2 (loc apparatus-
    # coercion-register); vibes:3 (episode apparatus-as-friction-surface). Each fires
    # for a distinct structural reason. No entry is redundant. NOT over-decoration.

    # ─────────────────────────────────────────────
    # CLASS 12: RUBRIC-FIDELITY
    # ─────────────────────────────────────────────

    # Per-facet REJECT-signature and file-level shape:
    # — NI: no AP10 chassis; no register-tic repetition (6 distinct channels confirmed
    #   by R2 pattern-scan); 7/31 in-band; lonely entries all justified. PASS.
    # — Memory: no monument fired without spine (mem:1 deleted for missing spine);
    #   surviving entries have NI co-citation; Earth-Bet fence clean (shape-language
    #   only); doubled-register confirmed in mem:2 (@23). PASS.
    # — Feeling: no named-feeling vocabulary; no hedge/simile/metaphor; no abstraction-
    #   noun subject-shift; per-character per-scene cap clean; NI non-redundancy contract
    #   clean (NI silent @21). PASS.
    # — Sensory: rubric-carve-out preamble for old-state sourcing complete; per-scene cap
    #   clean; modality diversity present (smell/tactile/sound); no cross-facet silent-gap
    #   obligation (loc-state carries no sensory notes at its anchors). Above-band density
    #   at flag-001 (SIGNAL). PASS conditional on stitcher review.
    # — Location-state: all 7 entries carry required location|time|condition|notes format;
    #   state-change entries note persistent mutation; place-anchor entries note scene-entry
    #   geometry. PASS.
    # — Vibes: all 17 entries carry licensed-by citations; no entry lacks a proto or
    #   peak-bone citation (vibes:16 @31 uses feeling:1 + proto:31); actor/loc/episode
    #   tiers present across key pile-ups. PASS.
    # — Exposition: scene-open-orient 0 fires correct; prior-episode-bridge ≤120w (68w);
    #   first-mention ≤30w (27w); no new plot content; no author-meta; Earth-Bet fence
    #   clean; dialogue-adjacency fence clean. PASS.
    # — Metaphor: refuse-by-default honored; per-beat audit log complete; all 5 anchor
    #   beats reviewed with documented rationale; 0 entries in 0–3% band. PASS.
    # — State-updates: rubric carve-out preamble complete; all 4 first-touch field-
    #   extensions declared with margit referrals noted; SEAM flags documented;
    #   decisions-not-fire section present; no held-against-turn fires. PASS conditional
    #   on fault-001 annotation correction.
    #
    # Cross-facet co-citation graph integrity: all co-cited pairs verified against
    # cite-index. No entry cites a deleted entry (mem:1 deleted; no surviving entry
    # co-cites it). Informational note: vibes:4 @15 lic-out lists "memory:1" (a
    # since-deleted entry); lic-out is a license-chain field, not a co-citation
    # requirement; vibes:4 stands on its other licensors (state-updates:3/4, proto:15,
    # peak-bone:15). Not a blocking fault; fixer may update for hygiene.
    #
    # Card-resolution for all target-reference / licensed-by / prop slugs:
    # — Location slugs: oc-hook-upper-provisioning (card exists), oc-magistrate-hall
    #   (card exists), oc-hook-lane (card exists), oc-hook-lower-water-trough (card
    #   exists). All 4 new location cards resolve.
    # — Prop slugs: oc-fish-account-ledger (exists), oc-d06-document (exists),
    #   oc-procedural-form (exists), oc-water-skin (exists). All 4 new prop cards
    #   resolve.
    # — Condition slug: cond-kl-court-state-122ac (exists at
    #   active-project/warehouse/cond-kl-court-state-122ac.md). Resolves.
    # — Behavior card slugs: westeros-septon (exists at cards/dialects/);
    #   taylor-hebert-kl-122ac actor card present. Both resolve.
    # NO dangling slugs. The 8 new oc-* cards authored by margit successfully resolve
    # all previously-unconfirmed location and prop references in b01c13. PASS.

  # ─────────────────────────────────────────────
  # SUMMARY
  # ─────────────────────────────────────────────

  summary:
    hard_count: 1
    hard_list:
      - fault-001 (CLASS 1 STRUCTURAL — state-updates.md per-entry annotation for
          state:16 and state:17 incorrectly labels the NI co-citation spine as
          "NI:4 @16"; correct label is "NI:3 @17"; inline comment on state:16 also
          incorrect; annotation-only error, no substantive facet content change
          required)
    signal_count: 4
    signal_list:
      - flag-001 (CLASS 2 FREQUENCY-BAND — sensory 12.9% above 3–6% band; no
          grounding-ledger license; advisory for stitcher; per-scene caps clean)
      - flag-002 (CLASS 5 CONTRADICTION — @24 time-of-day: loc-state:6 "afternoon"
          vs. state:11 "morning"; R2 did not align; stitcher advisory: adopt
          loc-state:6 "afternoon" as authoritative)
      - flag-003 (CLASS 10 TASTE-FLAG — taylor:1 "both columns, all the way down"
          taste seam; advisory for Phase 5b)
      - flag-004 (CLASS 10 TASTE-FLAG — halvard:2 "a wiser hand wrote off" taste
          seam; advisory for Phase 5b)
    phase_5_gate:
      verdict: BLOCKED
      reason: HARD count = 1 (fault-001). Phase 5b requires HARD = 0.
      fix_routing:
        - fault-001 routes to fixer
        - target: active-project/theater/facets/state-updates.md
        - scope: per-entry annotation block for state:16 and state:17 (lines 148–
            149 of the taylor-hebert-kl-122ac source slice)
        - fix_type: annotation label correction only; no substantive facet content
            change; no proto-line modification; no cite-index modification
```
