```yaml
audit:
  scope: chapter
  target: b01c20
  timestamp: 2026-06-06
  mode: flag-only
  status: FINDINGS-PRESENT
  totals: 8 findings (1 HARD, 7 SIGNAL) across 9 facets reviewed

  findings:

    # ── STRUCTURAL (0 findings) ──────────────────────────────────────────────
    # All facet files present. ID monotonicity confirmed per-file (loc-state:1-7,
    # narrator:2/4/5/6/8, sensory:1-5, mem:2/3, feel:1-3, vibes:1-6, exposition:1-3).
    # DELETED entries in narrator:1/3/7, mem:1, feel:4 leave gaps (1,3,7; 1; 4) —
    # gap-IDs expected post-R2 delete; not a STRUCTURAL fault.
    # Cite-index bidirectional check: all 63 entries cross-resolve. back=Y on all.
    # No proto-body divergence observed (canonical proto-lines carry matching SVOs).
    # No dialogue files present (zero-dialogue chapter; solitary/interior; confirmed
    # by scene-map header "0 dialogue-anchor speakers"). No STRUCTURAL dialogue findings.

    # ── FREQUENCY-BAND (2 findings) ─────────────────────────────────────────

    - id: signal-001
      type: flag
      what: "exposition-b01-c20.md: 3 entries / 30 bones = 10.0% (band 1-5%)"
      why: >
        Above the 1-5% standard band. Author self-flags: small-denominator solitary
        chapter (30 bones; same disposition family as c14 [6.5%] / c17 [5.6%] /
        c19 [8.6%] silent-chapter cohort). All three entries are load-bearing:
        exposition:1 is the series-terminal episode-open bridge; exposition:2 closes
        the Wren NAME-OPACITY HARD-WATCH; exposition:3 orients the new-this-chapter
        decommission mechanism. Context-ledger is EMPTY (0 CONTEXT-REQUIRED), so no
        ledger-licensed add is in play here — these are standard entries whose
        load-bearing rationale is documented but the band breach is real.
        Disposition: SIGNAL with small-denominator note; consistent with c14/c17/c19
        silent-chapter precedent; no fixer action required.

    - id: signal-002
      type: flag
      what: "feeling-b01-c20.md: 3 entries / 30 bones = 10.0% (band 2-5%)"
      why: >
        Above the 2-5% standard band. Chapter is solitary/interior/falling with
        Taylor as the sole POV actor; feeling fires at @4, @14, @24 — three distinct
        scene-level inflection points (stylus-lift s01 peak, decommission-read s03
        peak, held-blank s04 recognition). Per-scene cap ≤1 is MET (s01=1, s02=0,
        s03=1, s04=1, s05=0). Small-denominator effect (30 bones; 3/30 = 10% vs.
        3/60 = 5% in a standard chapter). No per-scene over-cap breach; all three
        entries are peak or peak-shadow anchors; the fourth fire (feel:4 @30) was
        deleted by R2 on G5 post-peak grounds. Same small-denominator disposition
        as exposition signal-001 above.
        Disposition: SIGNAL with small-denominator note; no fixer action required.

    # sensory: 2 standard entries / 30 bones = 6.7% (marginally over 6% ceiling;
    # authorized by BONES-AIRLESS-RISK upper-biasing per c19 precedent). 3 additional
    # grounding-licensed entries (sensory:3/4/5) EXEMPT per grounding-ledger
    # grd-c20-001/002/003 (all status: satisfied). Standard-only band: 6.7% — marginal
    # breach, BONES-AIRLESS-RISK authorization documented in sensory file header.
    # No FREQUENCY-BAND fault fires on sensory (grounding-licensed entries excluded per
    # PROP-0022 / URI-READABILITY-TWIN; standard-only breach covered by documented
    # AIRLESS-RISK upper-bias). No separate FREQUENCY-BAND finding emitted for sensory.

    # NI: 5 entries / 30 bones = 16.7% — in-band (15-25%). PASS.
    # memory: 2 entries / 30 bones = 6.7% — in-band (5-12%). PASS.
    # vibes: 6 entries / 30 bones = 20.0% — not band-capped (vibes unconstrained by
    #   frequency-band rule; licensed-by mandatory per-entry; all six resolve). PASS.
    # metaphor: 0 entries / 30 bones = 0.0% — in-band (0-3%). PASS.
    # loc-state: 7 entries / 30 bones = 23.3% — loc-state has no % frequency band cap
    #   (it is a coverage-driven facet, not a sparsity-driven one). Per-entry scrutiny
    #   at SUPERFLUOUS. PASS on band class.

    # ── METADATA-INCONSISTENCY (0 findings) ─────────────────────────────────
    # metaphor file header states "memory-b01-c20.md: does not exist" and "feeling-
    # b01-c20.md: does not exist" as basis for empty licensing pool. BOTH files exist.
    # This is a metadata inconsistency — but it is a stale-licensing-pool note from R1
    # authoring, not a claim the auditor relies on for constraint checks. The metaphor
    # file's actual conclusion (0 entries; refuse-by-default) is correct regardless
    # of which licensed-pool note is written (both memory and feeling are present but
    # carry no peaks eligible for metaphor under AP7 + AP1; the conclusion stands).
    # Classification: the note is technically wrong but the ruling it produces is
    # correct and self-reinforcing. Emitting as SIGNAL below under RUBRIC-FIDELITY
    # rather than METADATA-INCONSISTENCY (the wrong factual claim is in a comment,
    # not in a frontmatter field that downstream tools read).

    # ── CURVE-SHAPE verdict ──────────────────────────────────────────────────
    # Episode-level: dramatic_shape = falling. Five scenes with declared rhythm-shape:
    #   scene-A: flat-mid | scene-B: peak-and-release | scene-C: rising-to-peak |
    #   scene-D: double-peak | scene-E: rising-to-peak
    # Assessment: flat-mid open → peak-and-release transition → rising-to-peak
    # institutional action → double-peak recognition → rising-to-peak terminal
    # departure. This is a chapter whose three-scene escalation (B→C→D) builds toward
    # the central event (s04 recognition) then a compressed terminal departure — the
    # falling dramatic_shape is driven by the chapter's register (suppressed affect,
    # contempt-complete, cold-accounting), not by a descending pressure curve. The
    # scene-map uses "falling" as a narrative-posture label (per the DEC-0102/DEC-0099
    # precedent for c14-c20 silent-chapter disposition), not as a claim that
    # rhythm-shape values descend. The five declared rhythm-shapes are internally
    # coherent and the vibes/NI pressure fires (vibes:1→2→3→4→5→6, NI:2→4→5→6→8)
    # follow the escalation spine. No peak-standalone violations visible in the
    # cite-index (@22 and @30 both carry peak-standalone-compliant NI entries without
    # fusion). SHAPE-OK under the established falling/silent-chapter disposition family.

    # ── CONTRADICTION (0 findings) ───────────────────────────────────────────
    # State-chain checked for internal consistency:
    #   studio.time_of_day: after-third-bell → before-dawn (@1) → morning (@6) →
    #   midday (@12) → afternoon (@18) → dusk (@25). Monotonic advance. PASS.
    #   fauna_sense_status.coverage-scale: standdown-complete → active-lower-city (@10)
    #   → absorbed-into-apparatus-network (@15) → feed-closed-dispersing (@25) →
    #   dispersed-below-threshold (@27). Coherent. PASS.
    #   fauna_sense_status.eastern-gap-status: closed-at-standdown → open-wren-lanes-
    #   active (@10) → signal-dropped (@22) → blank-recognition-complete (@23) →
    #   dispersed-with-coverage (@27). Coherent. PASS.
    #   oc-ledger.condition: closed → open-succession-entries-in-progress (@5) →
    #   open-decommission-accounting (@16) → open-decommission-entries-marked (@17) →
    #   final-run-complete (@29). Coherent. PASS.
    #   actor:taylor.ledger-work-posture: at-rest-stylus-set → active-marking (@17) →
    #   stylus-lifted-no-line-opened (@24) → final-full-run-closed-complete (@29).
    #   Coherent. PASS.
    #   No paired incompatible states found on same anchor.

    # ── DEDUP (0 findings) ───────────────────────────────────────────────────
    # Cross-facet register check at high-density anchors:
    # @14 (6 co-located): exposition:3 orients mechanism NI is blind to (off-Jarvis
    #   channel + @15 absorption); NI:4 carries interior withhold and trigger-ambiguity;
    #   feel:2 stages body; loc-state:3 anchors place; state:12/26 record field flips.
    #   Distinct registers. No DEDUP.
    # @30 (6 co-located): loc-state:7 records place; NI:8 carries departure-as-motion;
    #   sensory:5 grounds threshold-light; state:25/32 record position lock; vibes:6
    #   LOCKS contempt-complete terminal. Distinct registers. No DEDUP.
    # @29 (mem:3 + state:24/31): mem:3 surfaces witch-label monument; states are field
    #   flips; no interior overlap. No DEDUP.
    # @24 (feel:3 + mem:2 + NI:6 + state:28): three distinct registers (somatic-held-
    #   blank, override-architecture shape, not-descending-as-entry, ledger-work-
    #   posture flip). No DEDUP.
    # No within-facet-different-anchor repetition flagged by R2 pattern-scans (NI
    #   pattern-scan SHAPE-OK; memory pattern-scan clean).

    # ── SUPERFLUOUS (0 findings) ──────────────────────────────────────────────
    # Lonely entries (no co-cites per cite-index):
    #   loc-state:1 @2: the doors open. Anchors a real state-change (before-dawn feed
    #     receives succession-execute). Passes necessity/interestingness/frugality:
    #     the door-state is the spatial confirmation that the holdfast routes activating
    #     (@3) is a received fact, not a noise signal. PASS.
    #   sensory:4 @20: thermal grounding-licensed (grd-c20-002; status satisfied).
    #     Exempt from SUPERFLUOUS evaluation per URI-READABILITY-TWIN.
    #   state:2 @3: holdfast-routes activate. Load-bearing field-change (first apparatus
    #     world-state confirmation). No SUPERFLUOUS.
    #   state:4 @5: ledger marks. Ledger-lifecycle fire. Distinct from @4 (stylus-
    #     position). No SUPERFLUOUS.
    #   state:11 @13: burn propagating through catalogue. Sequential state advance from
    #     state:10 @12. No SUPERFLUOUS.
    #   state:13 @15: apparatus absorbs coverage. New field-value. No SUPERFLUOUS.
    #   state:14 @16: ledger opens for decommission. Ledger-lifecycle advance. No
    #     SUPERFLUOUS.
    #   state:17 @19: smoke fills lanes. Ambient-condition first-step of physics
    #     cascade (PHYSICS-CASCADE protected-pattern @19-@22). No SUPERFLUOUS.
    #   exposition:1 @0: episode-open bridge. Covered by FREQUENCY-BAND signal-001.
    #     Necessity: series-terminal entering-state refresh no lens facet supplies
    #     (R2 judge confirmed). No SUPERFLUOUS.

    # ── CONSTRAINT (2 findings) ───────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        mem:3 @29 — memory entry (witch-label monument; cond-kl-witch-label-
        formation-122ac) — no NI co-citation present on @29. cite-index mem:3 @29
        co=[state:24, state:31] only. narrator:7 @29 was DELETED by R2 NI judge
        (AP-010 inverted-predicate cap breach + register-duplication). No NI entry
        remains at @29.
      why: >
        The rubric-memory cross-facet contract (RUBRIC-FIDELITY class (c), below)
        requires every memory entry to carry a narrator-interest spine on its own
        @-anchor. The R2 memory judge confirmed this requirement in the shard:
        "mem:3 @29 spine: narrator:7 @29 present in the cite-index (locked R1 graph).
        Standard narrator-interest co-citation satisfied." That statement was true at
        R1 graph lock. It became false when narrator:7 was deleted by the NI R2 judge
        in the same round. The NI and memory judges operated in parallel and were
        each graph-aware against the R1 graph — the NI judge's deletion was not
        visible to the memory judge within the same R2 round. The post-R2 cite-index
        at PHASE 4 is the authority; it shows mem:3 @29 with no NI co-citation.
        Downstream consequence: a spineless memory entry at the ledger-close anchor
        violates the rubric's cross-facet contract and creates a RUBRIC-FIDELITY
        hard fault (see rubric-fidelity-001 below). The entry is NOT deleted by this
        finding — auditor does not delete. The question is whether mem:3 stands or
        requires either (a) fixer restores an NI at @29, or (b) fixer deletes mem:3.
        Adjudication of the "leads into @30 narrator:8" defensibility argument: the
        rubric requires NI spine "on its own @-anchor" — not within a window, not on
        the adjacent bone. narrator:8 @30 is at a different anchor. The @30 NI does
        not satisfy the @29 requirement. This is HARD, not defensible as window-
        adjacent. Remediation: fixer must either (a) restore a minimal NI entry at
        @29 that does not reintroduce the AP-010 inverted-predicate or register-
        duplication grounds that caused narrator:7 to be deleted, or (b) delete mem:3
        if no compliant NI can be authored without those violations. The restored NI,
        if authored, must carry a distinct register from vibes:6 @30 (contempt-LOCK)
        and must not duplicate the "balancing IS the contempt" chassis narrator:7
        carried. The witch-label monument itself (the label-beside-the-line, the
        name-in-the-count-after-cover-fails) is an unduplicated register that a
        compliant NI could carry if the inverted-predicate chassis is avoided.
      criteria: >
        mem:3 @29 must have an NI co-citation on @29 that resolves in the
        post-fix cite-index, OR mem:3 must be deleted. The restored NI, if
        authored, must satisfy the rubric: distinct register from vibes:6 @30
        and from feel:3 @24; no AP-010 inverted-predicate chassis; no register-
        duplication with mem:3's own content. The witch-label monument and the
        running-ledger-at-the-gate as the contempt's spatial form are both
        available register surfaces for a compliant NI. A spineless mem:3 is
        not acceptable at Phase 5b.

    - id: signal-003
      type: flag
      what: >
        CONSTRAINT — state-updates POV co-citation: seven taylor.* actor-state
        entries (@14, @17, @24, @25, @28, @29, @30) vs. NI anchors present
        (@7, @14, @22, @24, @30). Checking each taylor.* entry against NI:
        @14: state:26 actor-taylor (standing-in-apparatus flip) — NI:4 @14 PRESENT. PASS.
        @17: state:27 actor-taylor (ledger-work-posture active-marking) — NI ABSENT @17. FLAG.
        @24: state:28 actor-taylor (ledger-work-posture stylus-lifted) — NI:6 @24 PRESENT. PASS.
        @25: state:29 actor-taylor (feed-deployment flip) — NI ABSENT @25. FLAG.
        @28: state:30 actor-taylor (pack: none → lifted) — NI ABSENT @28. FLAG.
        @29: state:31 actor-taylor (ledger-work-posture final-run) — NI ABSENT @29 (see fault-001). FLAG.
        @30: state:32 actor-taylor (position departure LOCK) — NI:8 @30 PRESENT. PASS.
      why: >
        The rubric-state-updates cross-facet contract (§ Cross-facet contract) states
        that every actor:taylor-hebert-kl-122ac.* state entry should pair with an NI
        entry on the same beat. @17, @25, @28 have no NI co-citation. These are
        non-peak-bone anchors (peak-shadow for @17 and @28; peak for @25) in the
        scenes where NI fires on peaks only. The contract's "should" language (not
        "must") and the author's documented rationale in DECISIONS-NOT-FIRE (e.g.
        @25 covered by NI @24/@30 bracket; @28 is pack-lift choreography) defensibly
        shift these to SIGNAL rather than HARD. The @17 absence is the
        most exposed: it is the tether-severance marking, a scene-C midday peak-bone,
        and while vibes:4 carries the register, the state-updates cross-facet contract
        expects NI. Noted; not HARD because author rationale is present in the file's
        DECISIONS-NOT-FIRE block.
        @29 NI-absent is the HARD case (fault-001 above; the NI was deleted mid-R2).
        @17, @25, @28 NI-absent are SIGNAL cases: documented sparsity decisions.

    # ── AP-SCAN (1 finding) ──────────────────────────────────────────────────

    - id: signal-004
      type: flag
      what: >
        metaphor-b01-c20.md header comment: "memory-b01-c20.md: does not exist —
        no memory facet authored for this chapter" and "feeling-b01-c20.md: does
        not exist — no feeling facet authored for this chapter." Both files exist
        at active-project/theater/facets/memory-b01-c20.md and feeling-b01-c20.md.
      why: >
        The metaphor author's licensing-pool rationale rests on a false factual
        premise (both files exist). The ruling it produces (0 entries; licensing
        pool empty) happens to be correct on independent grounds: even with both
        files present, every candidate memory/feeling anchor in those files either
        (a) fires at a peak-bone that the EXPULSION-AMBIGUITY-PRESERVED or
        PHYSICS-CASCADE / RECOGNITION-HELD-BLANK protected-patterns prohibit
        metaphor on (scene-map HARD watch), or (b) is a peak-shadow at a non-hinge-
        magnitude bone where AP7 default-refuse applies. The 0-entry conclusion
        stands. However, if the Phase 5b audience's metaphor reviewer reads the
        licensing-pool note and accepts it at face value, they inherit a false premise.
        Downstream: Phase 5b reviewer can still reach the correct verdict on
        independent grounds, but the note is a craft defect in the file.
        AP-SCAN class: author-meta (the comment describes the authoring context
        with a factual error; it is not a rubric-enumerated anti-pattern but is
        a hollow-prose-adjacent authoring-note defect). Routing: metaphor author.

    # ── TASTE-FLAG (1 finding) ───────────────────────────────────────────────

    - id: signal-005
      type: flag
      what: >
        NI file scene-A: after narrator:1 @4 is deleted, scene-A (@1-@5) carries
        zero NI fires. The chapter's flat-mid opening is interior-silent at the
        NI layer; vibes:1 @4 and feel:1 @4 carry the s01 register but no interior
        voice-channel fires.
      why: >
        The R2 NI judge's PATTERN-SCAN acknowledged this: "scene-A ambient
        (@1-@6 less @4-deleted) correctly silent." The defense is that flat-mid
        opens of falling chapters need not carry NI. The taste risk is that an
        audience reader expecting any interior presence in s01 receives only
        state-updates and sensory scaffolding for the first five bones. For the
        worm-canon-pedant and dark-fantasy-reader this is likely fine (they carry
        Taylor's interior from nineteen chapters); for the cape-fic-reader the
        s01 opener may read as purely procedural. This is a warm-up not a content
        failure; VOICE-FIXABLE at /and-stitch Phase 4 voice-embodiment discipline.
        TASTE-FLAG class: atmosphere-thin / voice-fidelity (the s01 interior is
        carried by facets that are not voice-channel fires — vibes and feeling —
        rather than by NI). Non-blocking. Routing: /and-stitch Phase 4.

    # ── PILE-UP REVIEW (1 finding) ───────────────────────────────────────────

    - id: signal-006
      type: flag
      what: >
        @14 (6 co-located): exposition:3, feel:2, loc-state:3, narrator:4,
        state:12, state:26. Bone: "the decommission message arrives."
        @30 (6 co-located): loc-state:7, narrator:8, sensory:5, state:25,
        state:32, vibes:6. Bone: "taylor-hebert-kl-122ac exits the south gate."
      why: >
        @14: warranted. This is the chapter's institutional-contempt peak (scene-C
        rising-to-peak; peak-bone per scene-map). The scene-map's
        EXPULSION-AMBIGUITY-PRESERVED protected-pattern fires here and
        requires simultaneous co-presence of the event register (state:12/26),
        location anchor (loc-state:3), NI withhold (narrator:4), feeling-tell
        (feel:2), and exposition mechanism (exposition:3). Six fires at the
        chapter's most architecturally loaded bone is proportionate.
        @30: warranted. Chapter-terminal peak-bone carrying both LOCK confirmations
        (position-prot-collapse rank 1 + political_register-world rank 9). Six
        fires are proportionate: the departure acts simultaneously as a spatial
        event (loc-state:7), a physical threshold (sensory:5), the terminal
        state-records (state:25/32), the NI not-stopping voice-channel (narrator:8),
        and the contempt-LOCK vibe (vibes:6). Each fires a distinct register at
        the chapter's single most load-bearing bone. No over-decoration.
        Verdict: both pile-ups WARRANTED.

    # ── RUBRIC-FIDELITY (2 findings) ─────────────────────────────────────────

    - id: fault-001-rf
      type: fault
      what: >
        mem:3 @29 — rubric-fidelity-cross-facet-co-citation — memory without
        NI-spine at @29. Cross-facet contract (rubric-memory-flags.md § Cross-facet
        contract): "every memory entry must carry a narrator-interest co-citation on
        its own @-anchor under the standard rule." The chapter is dramatic_shape:
        falling — V3 feel-as-spine carve-out unavailable (condition (1) fails).
        Post-R2 cite-index: mem:3 @29 co=[state:24, state:31] only; no narrator
        entry at @29.
      why: >
        This is the same finding as CONSTRAINT fault-001 above, classified under
        RUBRIC-FIDELITY as well per the cross-facet co-citation rule enumerated in
        rubric-memory-flags.md. The finding is not double-penalized — it is one
        fault with two class citations. Remediation is identical: NI at @29 or
        deletion of mem:3.
      criteria: >
        mem:3 @29 must have an NI co-citation on @29, OR mem:3 must be deleted.
        Identical criteria to CONSTRAINT fault-001.

    - id: signal-007
      type: flag
      what: >
        RUBRIC-FIDELITY (d) — card-resolution: state-updates-env-b01-c20.md names
        6 new field-extensions with MARGIT REFERRAL RECOMMENDED:
        (1) studio.apparatus-holdfast-routes.status @3
        (2) studio.oc-ledger.condition @5 (distinct from studio.cost-ledger.*)
        (3) studio.patron-channel.sequence @8
        (4) studio.ambient_conditions.outer-ward-burn @12
        (5) studio.east-of-water-gate-lanes.ambient @19
        (6) prop:oc-decommission-message @14 (new prop, no warehouse card)
        Also: location-state-b01-c20.md flags oc-south-gate as a NEW slug @30
        with "MARGIT REFERRAL recommended" — no loc-card confirmed.
        Also: state-updates-env mentions prop:oc-pack (first-touch @28; no warehouse
        card; MARGIT REFERRAL noted; fire deferred pending card existence).
      why: >
        RUBRIC-FIDELITY (d) requires that every facet entry naming a card slug must
        resolve to an existing card in cards/ or active-project/warehouse/. The six
        field-extensions above are classified as new-slug introductions (first-touch
        in c20), not dangling references to established slugs. For a series-terminal
        chapter, "new slugs introduced at departure" (south-gate, decommission-
        message, pack, holdfast-routes, oc-ledger, patron-channel, burn-ambient,
        lanes-ambient) are narratively first-appearances, not card-resolution
        failures in the traditional sense. The state-updates-env author correctly
        flagged all six for MARGIT REFERRAL rather than asserting they resolve.
        However the rubric's card-resolution check fires when the slug does not
        resolve in the warehouse — that is the mechanical condition here.
        Classification decision: SIGNAL rather than HARD because:
        (a) the author flagged all six explicitly and recommended margit referral
        (the "documented author defense" rubric carve-out for borderline cases);
        (b) this is a series-terminal chapter — no downstream chapter will consume
        these slugs; the risk of unresolved card references propagating into
        further /and-substance or /and-write runs is zero;
        (c) prop:oc-decommission-message, prop:oc-pack, and loc:oc-south-gate are
        genuine first-appearances with no prior chapters to establish them, making
        margit referral the correct resolution path, not a fixer rewrite.
        Routing: margit. Referral candidates: prop:oc-decommission-message,
        prop:oc-pack, loc:oc-south-gate, plus the six studio.* sub-field extensions
        (confirm against existing warehouse cards for studio.succession-document-status,
        studio.cost-ledger.*, and the dead-drop/channel sub-fields from c17-c19 to
        determine whether any are already captured under existing card definitions).

    # ── EARTH-BET HARD-FENCE SCAN ────────────────────────────────────────────
    # Full text-field scan across all 9 facet files + cite-index + scene-map.
    # Scan targets: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer,
    #   Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil,
    #   Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea.
    # Also: slug-component scan (khepri-, gold-morning-, skitter-, prt-, etc.).
    #
    # Findings:
    # vibes-b01-c20.md header: "EARTH-BET FENCE (HARD): no Khepri / Gold Morning /
    #   Skitter / Scion / Brockton Bay / parahuman / cape proper-noun in any vibe-text."
    #   — This is a fence declaration, not a fence content; it does NOT contain the
    #   banned terms.
    # exposition-b01-c20.md: "Earth-Bet fence (HARD): no Khepri / Gold Morning /
    #   Skitter / Brockton Bay / Scion / parahuman / shard / cape in any gloss-text."
    #   — Fence declaration only; gloss bodies are clean.
    # memory-b01-c20.md R2 shard: "Earth-Bet hard-fence: CLEAN across both surviving
    #   descriptions (no Khepri, no Gold Morning, no Skitter/cape, no Dance/year stamp;
    #   the @24 cue is pure shape-language..."
    # memory-b01-c20.md actual entry text at mem:2 @24: "the same routing, the same
    #   reach held open over bodies that did not know the reach was there, in a
    #   different place for reasons that did not hold" — shape-language only; no proper
    #   noun. CLEAN.
    # state-updates: cond-override-architecture-residue-122ac slug component does not
    #   contain banned terms (slug is mechanism-descriptive, not Khepri-slug).
    #   Memory target references: cond-override-architecture-residue-122ac (@24) and
    #   cond-kl-witch-label-formation-122ac (@29) — neither slug contains Earth-Bet
    #   proper nouns. CLEAN.
    # Full scan: CLEAN. No Earth-Bet hard-fence violations found across any facet
    #   entry text fields, target references, or slug components.

    # ── SCENE-MAP COVERAGE (URI-SCENE-WINDOW) ────────────────────────────────
    # Coverage field: "30/30 bones in exactly one scene." Gaps: empty. Overlaps: empty.
    # Verification against proto-lines:
    #   Bones @0-@30 (31 items including @0 preamble; scene-map covers @1-@30 = 30):
    #   scene-A: @1-@5 (5 bones). scene-B: @6-@11 (6 bones). scene-C: @12-@17 (6 bones).
    #   scene-D: @18-@24 (7 bones). scene-E: @25-@30 (6 bones). Total: 30 = total-bones.
    #   @0 (preamble) is exposition:1's anchor; the scene-map header explicitly notes it
    #   as a chapter-open preamble. The scene-map's @1-@30 coverage range correctly
    #   excludes @0 (which is a pre-scene structural anchor, not a narrative bone in
    #   the 30-bone count). Total-bones: 30 confirmed. Total-scenes: 5 confirmed.
    #   No gaps. No overlaps. No dangling anchors. URI-SCENE-WINDOW: PASS.

    # ── CONSTRAINT STATE-UPDATES POV CO-CITATION (detailed) ─────────────────
    # Covered under signal-003. The @17, @25, @28 SIGNAL cases are documented above.
    # @29 is the HARD case (fault-001).

---

## Audit summary

Total entries reviewed: 63 facet entries (9 facet files; 0 dialogue files — zero-dialogue chapter)
Total proto-lines: 31 (including @0 preamble)

HARD findings: 1
  CONSTRAINT: 1 (fault-001 — mem:3 @29 spineless, NI deleted mid-R2)
  RUBRIC-FIDELITY: 1 (fault-001-rf — same finding, cross-class citation; not a separate fault count)
  Note: fault-001 and fault-001-rf are the same fault classified under two audit classes.
  Hard count for gate purposes: 1 HARD finding requiring remediation before Phase 5b.

SIGNAL findings: 7
  FREQUENCY-BAND: 2 (exposition 10%; feeling 10%; both small-denominator noted)
  CONSTRAINT: 1 (signal-003 — state-updates POV co-citation @17/@25/@28 documented)
  AP-SCAN: 1 (signal-004 — metaphor file false licensing-pool note)
  TASTE-FLAG: 1 (signal-005 — scene-A NI-silent; VOICE-FIXABLE at stitch)
  PILE-UP REVIEW: 1 (signal-006 — @14 and @30 both WARRANTED)
  RUBRIC-FIDELITY: 1 (signal-007 — 6 new margit-referral slugs; documented; terminal chapter)

CURVE-SHAPE: SHAPE-OK (falling/silent-chapter disposition; DEC-0099/DEC-0102 precedent)
Scene-map coverage: PASS (30/30 bones; no gaps/overlaps/dangling)
Earth-Bet hard-fence: CLEAN

HARD class breakdown:
  STRUCTURAL: 0
  CONTRADICTION: 0
  DEDUP: 0
  SUPERFLUOUS: 0
  CONSTRAINT: 1 (fault-001)
  RUBRIC-FIDELITY: 1 (fault-001-rf — same fault, second class citation)

SIGNAL class breakdown:
  FREQUENCY-BAND: 2
  METADATA-INCONSISTENCY: 0
  AP-SCAN: 1
  TASTE-FLAG: 1
  PILE-UP: 1
  CONSTRAINT (SIGNAL): 1
  RUBRIC-FIDELITY (SIGNAL): 1

F-R2 counts (from available shards): all-zero across NI, memory, exposition shards.
  NI: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}
  memory: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}
  exposition: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}
  feeling shard: absent (staff/feeling/r2-decision-shard.md not found)
  — feeling's absence from the shard set is noted for Phase 4a/6 consolidation.

---

## Routing

fault-001 / fault-001-rf → fixer.
  mem:3 @29 spineless post-R2 delete. Route: taylor-hebert-kl-122ac NI-author (impersonator,
  judge mode) OR fixer with authority to: (a) author a minimal NI at @29 that avoids
  AP-010 inverted-predicate chassis and avoids register-duplication with vibes:6 @30,
  OR (b) delete mem:3 @29 and cascade the [mem:3] citation from @29 in the canonical
  proto-lines. Fixer must re-run cite-index update after either choice. This is the
  only blocking finding; Phase 5b cannot fire until this resolves.

signal-001 → advisory; no fixer action. Disposition: small-denominator silent-chapter cohort.
signal-002 → advisory; no fixer action. Disposition: small-denominator silent-chapter cohort.
signal-003 → advisory; no fixer action. @17/@25/@28 NI-absent documented in state-updates file.
signal-004 → metaphor author. Remove or correct the false licensing-pool note.
  Non-blocking. Can be corrected alongside Phase 5b prep.
signal-005 → /and-stitch Phase 4 voice-embodiment discipline. Non-blocking.
signal-006 → no action. Both pile-ups WARRANTED.
signal-007 → margit referral. Candidates: prop:oc-decommission-message, prop:oc-pack,
  loc:oc-south-gate, studio.apparatus-holdfast-routes.status, studio.oc-ledger.condition,
  studio.patron-channel.sequence, studio.ambient_conditions.outer-ward-burn,
  studio.east-of-water-gate-lanes.ambient. Series-terminal chapter; referral is
  archival documentation, not a blocking gate.
```
