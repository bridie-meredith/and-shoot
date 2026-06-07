---
audit:
  scope: chapter
  target: b01c04
  gate: /and-facets Phase 5 — full graph flag-only
  timestamp: 2026-05-27
  auditor: claude-sonnet-4-6
  mode: flag-only (findings surface for Phase 5b + fixer triage; no fixer dispatch from this gate)
  files-loaded:
    - active-project/theater/proto-lines/b01-c04.md
    - active-project/theater/dialogue/taylor-hebert-kl-122ac.md (c04 section)
    - active-project/theater/dialogue/jarvis-coin-kl-courier.md (c04 section)
    - active-project/theater/facets/location-state-b01-c04.md
    - active-project/theater/facets/interest-narrator-b01-c04.md
    - active-project/theater/facets/sensory-b01-c04.md
    - active-project/theater/facets/state-updates.md (consolidated)
    - active-project/theater/facets/memory-b01-c04.md
    - active-project/theater/facets/feeling.md (consolidated)
    - active-project/theater/facets/metaphor-b01-c04.md
    - active-project/theater/facets/vibes-b01-c04.md
    - active-project/theater/facets/exposition-b01-c04.md
    - active-project/theater/facets/scene-map-b01-c04.md
    - active-project/theater/facets/_cite-index.md (post-R2)
    - active-project/theater/facets/.r2-decisions.md (consolidated)
    - active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md
    - active-project/staff/dialogue-writer/jarvis-coin-kl-courier.drafts.md
    - cards/dialects/taylor-hebert-westeros.card.md
    - cards/dialects/westeros-smallfolk.card.md
    - schemas/facet.schema.md
    - schemas/dialogue.schema.md
    - schemas/audit-report.schema.md
  findings:

    # ── CLASS 1: STRUCTURAL ──────────────────────────────────────────────────

    - id: fault-001
      type: fault
      class: STRUCTURAL — dialogue ID monotonicity
      what: >
        active-project/theater/dialogue/taylor-hebert-kl-122ac.md contains entries for
        both b01c03 and b01c04 in the same file. The c03 section uses IDs 1, 2, 3.
        The c04 section re-uses ID 1 (entry: "1 @7 | deliver the yes..."). The
        dialogue schema states IDs are "monotonic positive integer, scoped to this
        character file" starting at 1. The c04 section restarts the count at 1 rather
        than continuing from 4. The citation token [taylor-hebert-kl-122ac:1] in
        proto-line @7 of b01-c04.md is therefore ambiguous within the file — it
        matches both c03 entry 1 (@11, c03 accept-preamble) and c04 entry 1 (@7,
        c04 yes-delivery).
        Jarvis's c04 entries (IDs 8 and 9) correctly continue monotonically from
        the c03 sequence (IDs 1-7), confirming the expected behavior.
      why: >
        The stitcher resolves character dialogue by `<character-slug>:<id>` within
        the character file. A duplicate ID makes the proto-line @7 citation
        ([taylor-hebert-kl-122ac:1]) ambiguous; the stitcher may retrieve the c03
        utterance instead of the c04 acceptance line. The c04 chapter's central
        speech act — Taylor delivering the yes — would be misrendered or absent.
      criteria: >
        The c04 entry in taylor-hebert-kl-122ac.md must be renumbered to ID 4
        (continuing from c03's highest ID of 3). The citation token in
        active-project/theater/proto-lines/b01-c04.md at proto-line @7 must be
        updated from [taylor-hebert-kl-122ac:1] to [taylor-hebert-kl-122ac:4].
        The cite-index entry for taylor-hebert-kl-122ac:1 @7 must be updated to
        taylor-hebert-kl-122ac:4 @7. No other entries are affected.

    - id: fault-002
      type: fault
      class: STRUCTURAL — forward citation at proto-line @9
      what: >
        active-project/theater/proto-lines/b01-c04.md proto-line @9 cites [state:2].
        In the consolidated state-updates.md, state entry 2 is: "2 @13 studio.active_location:
        oc-cooper-yard-eel-alley → oc-pig-tallow-lane". Proto-line @9 is in scene-A
        (bones @1-@12 per scene-map). State entry 2's canonical anchor is @13, which is
        the scene-B open — four bones after @9. Proto-line @9 therefore cites a state
        update that has not yet occurred in the narrative sequence at that beat. This is
        a forward-reference in the citation graph.
        The cite-index confirms: narrator:3 @9 co-citation list includes state:2.
        State:2 @13 back=Y entry in the cite-index records @13 as the anchor.
      why: >
        The stitcher rendering proto-line @9 (scene-A; Jarvis confirms the routing
        arrangement at the cooper's yard) will read state:2 as context, which declares
        the location as oc-pig-tallow-lane. The acceptance beat takes place at the
        cooper's yard; the pig-tallow-lane location state belongs to scene-B. Inserting
        the scene-B location context at scene-A's dialogue peak produces a spatial
        contradiction in the rendered prose.
      criteria: >
        The [state:2] citation token must be removed from proto-line @9. Proto-line @9
        does not require a location-state citation — the cooper's yard context is already
        carried by loc-state:1 @1 (back-referenced on @1) and the stitcher will correctly
        infer the @1 environment through @12. The cite-index must be regenerated to remove
        state:2 from the narrator:3 @9 co-citation list.

    - id: fault-003
      type: fault
      class: STRUCTURAL — forward citation at proto-line @22
      what: >
        active-project/theater/proto-lines/b01-c04.md proto-line @22 cites [state:5].
        In the consolidated state-updates.md, state entry 5 is: "5 @25 studio.time_of_day:
        first-bell-morning-day-1 → early-morning-grey-day-2". Proto-line @22 is in
        scene-B (bones @13-@24 per scene-map). State entry 5's canonical anchor is @25,
        which is the scene-C open and the day-2 temporal transition — three bones after @22.
        Proto-line @22 therefore cites a state update that has not yet occurred.
        This is confirmed by the cite-index pile-up section, which lists state:5 among
        the 8 co-located facets at @22: "mem:2, narrator:6, state:4, state:5, vibes:9-12".
        State:5 @25 back=Y records @25 as its anchor.
      why: >
        Proto-line @22 is the Wren-anchor-discipline bone — scene-B's load-bearing
        protected-pattern bone (insect-feed returns Wren; Taylor holds the feet). The
        stitcher at @22 receives state:5's day-2 morning temporal state as rendering
        context. Scene-B takes place on day-1 morning. The day-2 transition is the
        chapter's inter-scene time-skip (from @24 to @25). Inserting the day-2 temporal
        context at @22 collapses the scene-B/scene-C temporal boundary and misplaces
        the chapter's structural time-skip. The @22 pile-up (8 co-fires) amplifies
        the stitcher signal load; state:5 is a contaminating signal among 7 legitimate
        ones.
      criteria: >
        The [state:5] citation token must be removed from proto-line @22. State:5
        belongs at its canonical anchor @25 and is already back-referenced there via
        loc-state:4, sensory:3 co-citations. The @22 pile-up drops from 8 to 7
        co-fires after removal. The cite-index must be regenerated to remove state:5
        from the @22 pile-up entry.

    - id: flag-001
      type: flag
      class: STRUCTURAL — cite-index integrity gaps
      what: >
        active-project/theater/facets/_cite-index.md has three internal inconsistencies
        after the forward-citation faults above are accounted for:
        (a) state:13 @37 is listed as back=N, but proto-line @37 ("taylor-hebert-kl-122ac
        runs the ward-feed [state:13]") explicitly cites it. State:13 = env entry
        "13 @37 studio.actors_in_yard: [taylor-hebert-kl-122ac] → []" — a studio-scope
        entry that should be back=Y.
        (b) The pile-up section at @22 includes state:5 in the 8-count, but state:5's
        own cite-index entry anchors at @25. This is resolved by fault-003 removal, but
        the pile-up count should be corrected to 7 on regeneration.
        (c) State:7 @27's co-citation list includes state:6. Proto-line @27 cites both
        [state:6] and [state:7], but the cite-index entry for state:6 only records @26
        as its anchor — the @27 cross-citation of state:6 is not reflected in state:6's
        own cite-index entry.
      why: >
        Consumers reading the cite-index for back=N signals (e.g., to identify orphaned
        entries) will incorrectly treat state:13 as unreachable. The pile-up count error
        propagates to any tool that reads the pile-up section for stitcher prioritization.
        The state:6 dual-anchor gap means the cite-index does not fully represent the
        proto-line citation graph. These should be corrected on the next cite-index
        regeneration pass (which is triggered by faults 002 and 003 anyway).

    - id: flag-002
      type: flag
      class: STRUCTURAL — NI ID gaps
      what: >
        active-project/theater/facets/interest-narrator-b01-c04.md ID sequence: 1, 3,
        4, 6, 7, 8, 9, 10, 11, 12, 13, 14. IDs 2 and 5 are absent. These are the
        positions of narrator:2 and narrator:5, deleted at R2 (AP10 chassis cleanup
        per .r2-decisions.md). Per the delete-only edit rule and the bones schema's
        "flat IDs are preserved" principle applied to facets, gaps after deletion are
        expected behavior — IDs are stable.
      why: >
        Not a fault. Flagged for awareness: any downstream tool assuming contiguous
        IDs will miscount total entries. The gaps are documented in .r2-decisions.md
        (narrator-interest row: "deleted 2"). No fixer action required.

    # ── CLASS 2: FREQUENCY-BAND ──────────────────────────────────────────────

    - id: fault-004
      type: fault
      class: FREQUENCY-BAND — NI above-band without carve-out preamble
      what: >
        active-project/theater/facets/interest-narrator-b01-c04.md declares
        density: 31% (12 fires / 39 bones). The NI rubric band is 15-25%. The file's
        frontmatter acknowledges the density but provides no rubric-carve-out preamble
        block in the file body per the format specified by schemas/facet.schema.md
        § Rubric carve-out preamble. The .r2-decisions.md does not document a
        band-overshoot carve-out for NI — only AP10 chassis cleanup and the
        SEAM-NI-CO-CITATION requirement. The R2 add-cap (5/5 adds) being exhausted
        does not constitute a carve-out for the density result.
        Compare: state-updates.md env slice provides the template for a valid carve-out
        preamble (multi-ward / multi-day chapter structure; per-entry strip-test pass;
        authority-test pass; each entry's rationale annotated).
      why: >
        NI at 31% is 6 points above the 25% ceiling. Above-band NI produces
        over-narrated prose — Taylor's interior monologue appears at 12 of 39 bones,
        which conflicts with the chapter's operational-enactment register (the
        four-ward feed runs as continuous background infrastructure; excess NI voices
        it as foregrounded accounting). The missing carve-out preamble means the
        /and-stitch Phase 0 rubric scan will flag this file as an undefended violation.
      criteria: >
        Option A: Delete NI entries whose multi-justification is weakest until density
        falls to ≤25% (≤9 entries / 39 bones). Candidates are narrator:1 @6 (lonely,
        no co-citations; insect-feed anticipation carried by scene-A structure), and
        narrator:12 @23 (lonely; held-bone Wren-discipline carry — but the protected-
        pattern designation in scene-map already marks this; NI may be redundant).
        Option B: Add a rubric-carve-out preamble block to the NI file in the format
        specified by facet.schema.md §Rubric carve-out preamble, documenting why the
        multi-ward / multi-day / four-scene-peak structure necessitates above-band NI
        for this chapter, with per-entry annotations naming the carve-out clause.

    - id: flag-003
      type: flag
      class: FREQUENCY-BAND — sensory geometry-floor conflict
      what: >
        active-project/theater/facets/sensory-b01-c04.md — 3 entries / 39 bones = 7.7%.
        Rubric band is 3-6%. No carve-out preamble. The three entries fire exactly once
        per scene at scene-open anchors (sensory:1 @1 / sensory:2 @13 / sensory:3 @25).
        For a 3-scene chapter under 39 bones, the minimum-fire rate if every scene
        gets one scene-open sensory entry is 3/39 = 7.7%, which is above the 6%
        ceiling by design geometry.
      why: >
        The overshoot is architectural, not authoring excess: 3 scenes × 1 required
        scene-open sensory entry = 3 minimum fires; 3/39 = 7.7% > 6% regardless of
        authoring choices. The rubric's 3-6% band was calibrated for single-scene or
        2-scene chapters (implied by s01e01 archetype reference in state-updates
        carve-out). No fixer action appropriate. Flagged as a rubric-calibration
        signal: the sensory band needs a scene-count floor clause for 3+ scene chapters.

    - id: flag-004
      type: flag
      class: FREQUENCY-BAND — exposition above-band without preamble-block format
      what: >
        active-project/theater/facets/exposition-b01-c04.md — 3 entries / 39 bones =
        7.7%. Rubric band is 1-5%. The file provides an inline prose justification
        (two new Flea Bottom wards introduced as the substance payload; both required
        for the chapter's structural arc; per-episode caps satisfied; b01c02 precedent
        at 8.5% accepted). The justification is in a narrative section, not in a
        rubric-carve-out preamble block per facet.schema.md format.
      why: >
        The overshoot is structurally defensible (two new ward first-mentions are the
        capability-axis-up payload; neither can be dropped without leaving a load-
        bearing place-introduction unanchored). However, the carve-out is in narrative
        prose form rather than the machine-parsable preamble-block format. If the
        /and-stitch Phase 0 parser reads the exposition file for carve-out headers,
        the inline prose will not be recognized. No fixer action expected for the
        density itself. Preamble-block reformatting is lower-urgency than the HARD
        faults.

    # ── CLASS 3: METADATA-INCONSISTENCY ─────────────────────────────────────

    - id: flag-005
      type: flag
      class: METADATA-INCONSISTENCY — episode slug format
      what: >
        Episode-slug format is inconsistent across facet files in b01c04:
        - interest-narrator-b01-c04.md: episode: b01c04 (no hyphen)
        - memory-b01-c04.md: episode: b01-c04 (hyphen)
        - feeling.md taylor slice: episode: b01-c04 (hyphen)
        - feeling.md jarvis slice: episode: b01c04 (no hyphen)
        - exposition-b01-c04.md: episode: b01-c04 (hyphen)
        - state-updates.md taylor slice: episode: b01-c04 (hyphen)
        - state-updates.md jarvis slice: episode: b01c04 (no hyphen)
        - .r2-decisions.md: episode: b01c04 (no hyphen)
        - scene-map-b01-c04.md field: scene-map: b01c04 (no hyphen in field value)
        The canonical slug per the scene-map and r2-decisions appears to be b01c04.
      why: >
        Inconsistent slug format produces silent mismatches in any pipeline tool that
        filters by the episode field. The inconsistency is confined to frontmatter
        metadata and does not affect the citation graph (which uses proto-line IDs,
        not episode slugs). Low severity; no immediate functional failure. Should be
        normalized before the next chapter's facet authoring.

    - id: flag-006
      type: flag
      class: METADATA-INCONSISTENCY — NI author field
      what: >
        active-project/theater/facets/interest-narrator-b01-c04.md frontmatter:
        author: taylor-hebert-kl-122ac. The facet schema specifies NI is authored by
        "dialogue-writer fork for the POV character" — the agent, not the character.
        Compare: feeling.md taylor slice: "author: impersonator-taylor-hebert-kl-122ac"
        and memory-b01-c04.md: "author: impersonator-taylor-hebert-kl-122ac" — both
        use the agent slug format.
      why: >
        The author field is the traceability signal for redispatch on revision. An
        author field naming the character slug rather than the agent slug will fail
        any automated redispatch lookup. Low severity for the current chapter; should
        align with the convention used by all other dialogue-writer-fork-authored
        facets.

    # ── CLASS 4: CURVE-SHAPE ─────────────────────────────────────────────────

    - id: pass-001
      type: pass
      class: CURVE-SHAPE
      what: >
        Chapter dramatic_shape declared as "rising" (memory-b01-c04.md frontmatter
        chapter-dramatic-shape: rising; implicit in scene-map structure).
        Scene-map rhythm-shapes: scene-A rising / scene-B rising-to-peak /
        scene-C rising-to-peak-to-trail. The arc builds through A (first-bell
        acceptance) and B (ward-expansion / Wren-anchor-discipline), peaks at @36
        in C (world-axis pivot: intelligence enters Otto's channel), and trails at
        @37-@39 (continuous four-ward feed; Wren-anchor unexamined; chapter-close
        exit). Collective arc is consistent with rising dramatic shape.
      why: No finding.

    # ── CLASS 5: CONTRADICTION ───────────────────────────────────────────────

    # forward-citation contradictions covered under fault-002 and fault-003 (STRUCTURAL).
    # No additional same-anchor incompatible-state contradictions found.

    - id: pass-002
      type: pass
      class: CONTRADICTION
      what: >
        Beyond the forward-citation structural faults (fault-002 and fault-003),
        no incompatible state declarations exist on the same anchor. The state:1 @1
        time-of-day transition (third-bell-noon → first-bell-morning) is a chapter-open
        reset from the prior chapter's close-state, not a contradiction with loc-state:1's
        predawn designation — the transition records where the clock was at the prior
        chapter's close and where it opens for c04. No sequential-same-field contradiction
        on any anchor.
      why: No additional finding.

    # ── CLASS 6: DEDUP ───────────────────────────────────────────────────────

    - id: flag-007
      type: flag
      class: DEDUP — vibes:9 / vibes:10 semantic adjacency at @22
      what: >
        active-project/theater/facets/vibes-b01-c04.md — vibes:9 and vibes:10 both
        target actor:wren-stitch-maker-flea-bottom-ward at @22:
        vibes:9: ++ rising entrapment: [confirmed-in-the-feed-and-confirmed-outside-
          the-report, anchor-discipline-not-equivalent-to-anchor-safety, feed-touching-
          the-stitch-house-without-logging]
        vibes:10: ++ mutual-silence: [ledger-exclusion-as-form-of-action, not-noting-
          as-choice-with-information, un-examined-distinction-as-the-operative-
          distinction]
        The file's AP11 advisory defends these as distinct (rising-entrapment biases
        toward locked-accounting register; mutual-silence biases toward active-not-
        logging operational register). Token bundles do not overlap by string match.
      why: >
        The semantic overlap is thin — both describe Wren's placement in the feed
        without report inclusion, from two framings of the same fact. If the stitcher
        collapses vibes by entity rather than by keyword-label, both entries produce
        the same bias on Wren, inflating her thematic weight at the chapter's most-
        decorated anchor (@22 pile-up). The AP11 defense is documented and the tokens
        are technically distinct; this is advisory for stitcher-profile configuration
        rather than a fixer instruction. No action required if the stitcher discriminates
        by keyword-label.

    # ── CLASS 7: SUPERFLUOUS ─────────────────────────────────────────────────

    - id: fault-005
      type: fault
      class: SUPERFLUOUS — vibes:7 @19 inert (bare proto-line, back=N)
      what: >
        active-project/theater/facets/vibes-b01-c04.md — vibes:7 @19 targets
        actor:oswyn-mudway-flea-bottom-elder (++ social-tether-substrate) and anchors
        at @19. Proto-line @19 is bare: "19 taylor-hebert-kl-122ac maps the oswyn-
        mudway-flea-bottom-elder interval" — confirmed bare by the cite-index bare-
        protolines list ("@2, @3, @8, @10, @12, @14, @16, @19, @20, @21, @24,
        @30, @34") and by cite-index entry vibes:7 @19 back=N.
        The vibes schema permits optional anchoring ([@<proto-line-id>] is optional)
        for off-screen/inter-episode reflective context, but @19 is an on-screen bone
        in scene-B. Vibes:6 @18 already adds actor:oswyn ++ the-unknowing-contact on
        the immediately preceding bone (@18 back=Y, cited in the @18 pile-up).
        The file's AP11 advisory argues vibes:6 and vibes:7 have distinct downstream
        operator behavior (contact-register vs substrate-register), but vibes:7 is
        unreachable via the citation graph — no proto-line cites it, so the stitcher
        never loads it as context for any rendering pass.
      why: >
        An on-screen-anchored vibe entry with back=N is inert: downstream operators
        that load vibes by cite-index traversal will not encounter vibes:7 at @19 and
        the AP11 defense is moot. The social-tether-substrate signal for Oswyn is
        fully carried by vibes:6 @18 (back=Y; reachable). vibes:7 contributes nothing
        to the operator-bias graph as currently structured.
      criteria: >
        Delete vibes:7 from vibes-b01-c04.md. The Oswyn social-tether-substrate signal
        is carried by vibes:6 @18. If the substrate-register distinction from the AP11
        advisory is judged load-bearing, the citation token [vibes:7] must be added to
        proto-line @19 in b01-c04.md to make the entry reachable — but this requires
        evaluating whether a bare proto-line should receive a vibe citation without other
        co-fires. Deletion is the minimum change.

    # ── CLASS 8: CONSTRAINT ──────────────────────────────────────────────────

    - id: pass-003
      type: pass
      class: CONSTRAINT — memory NI-spine co-citation
      what: >
        mem:2 @22: cite-index co-citation list includes narrator:6. PASS.
        mem:4 @38: cite-index co-citation list includes narrator:9. PASS.
        Both surviving memory entries are co-cited with a narrator-interest entry on
        the same anchor. The memory-NI-spine requirement is satisfied for both entries.
      why: No finding.

    - id: fault-006
      type: fault
      class: CONSTRAINT — narrator:14 @33 orphan (mem:3 deleted)
      what: >
        active-project/theater/facets/interest-narrator-b01-c04.md — narrator:14 @33
        is a lonely NI entry (confirmed in _cite-index.md lonely-entries list). The
        .r2-decisions.md bidirectional-loop candidates section explicitly flags:
        "@33 — narrator:14 ADD; previously paired with mem:3 (now DELETED in memory R2);
        POTENTIAL ORPHAN — narrator:14 may now be lonely."
        Memory R2 deleted mem:3 @33 (per memory-b01-c04.md: "r2-deletes: mem:3 @33
        (spineless + forced-fit + insider-only audience-meaningfulness)"). narrator:14
        was added at R2 specifically to pair with mem:3. Without mem:3, narrator:14
        has no co-citing facets at @33. No state update fires at @33; no feeling,
        vibes, or sensory entry fires at @33. The NI entry stands alone at a held-bone
        (scene-C protected-pattern held-bone trio @33-@35).
        NI entry text: "the pattern-shape holds the ward-count; the names that would
        price the wards do not enter the sheet." Without the Westerosi-monument clamp
        that mem:3 would have provided, this reads as a restatement of the @22 omission
        theme without the monument-resonance ground.
      why: >
        narrator:14 was authored to function within a paired citation context that no
        longer exists. At the stitcher, @33 renders with narrator:14 as the sole
        interior signal. The cost-tracking observation ("the names that would price the
        wards do not enter the sheet") duplicates the @22 theme (Wren as un-priced
        anchor) without adding the monument-register that was the add's justification.
        The R2 add motive (graph-coherence with mem:3) is now broken; the entry
        fails on its own merit under the multi-justification threshold for NI at
        held-bones where no state update fires.
      criteria: >
        Option A: Delete narrator:14 from interest-narrator-b01-c04.md. The held-bone
        trio @33-@35 is a protected-pattern (scene-map: "held-bone trio @33-@35
        moral_framework + political_register-prot + position-prot-rise all held through
        the pause-after-receipt"). The held quality is registered by scene-map
        structure; narrator:7 @31 immediately precedes and frames the handoff moment;
        narrator:8 @36 frames the exit. The interior does not require coverage at @33
        itself. This is the minimum-change resolution.
        Option B: Author a replacement memory entry at @33 that passes the
        both-meaningful gate for the active audience (worm-canon-pedant +
        cape-fic-reader + dark-fantasy-reader) without requiring ASOIAF source-fluency.
        The prior mem:3 candidate failed this gate; any replacement must identify a
        monument-family or callback anchor that clears it. This restores the co-citation
        pair that justified narrator:14.

    - id: pass-004
      type: pass
      class: CONSTRAINT — actor:taylor NI co-citation (SEAM-NI-CO-CITATION)
      what: >
        Per state-updates.md taylor slice SEAM-NI-CO-CITATION, NI must co-cite at:
        @9, @15, @18, @22, @27, @31.
        Cite-index confirms NI co-citations at all six required anchors:
        narrator:3 @9 (state:1/2/vibes:2/3 co-cites); narrator:11 @15 (state:3/vibes:5);
        narrator:4 @18 (state:4/vibes:6/7); narrator:6 @22 (mem:2/state:4/5/vibes:9-12);
        narrator:13 @27 (state:6/7/vibes:13); narrator:7 @31 (state:7/10). All 6 PASS.
      why: No finding.

    - id: pass-005
      type: pass
      class: CONSTRAINT — Earth-Bet hard-fence
      what: >
        Full scan of all text fields across all 10 facet files and both c04 dialogue
        files: NI entry bodies, exposition gloss text, dialogue utterances, feeling
        somatic-tell descriptions, memory gloss text, vibes token bundles, state-update
        field values, sensory notes, location-state sensory clauses.
        No Earth-Bet proper nouns detected: Brockton Bay, Skitter, Khepri, Lung, PRT,
        parahuman, Endbringer, Gold Morning, Scion, trigger event, shard, swarm,
        Undersiders, cape (as parahuman designation), Wards, Protectorate — all absent.
        The exposition file and both dialogue drafts sidecars carry their own internal
        Earth-Bet scans confirming clean. The insect-feed / the count / the flies /
        the courier are all register-resident clinical vocabulary substitutes, not
        Earth-Bet proper nouns. PASS.
      why: No finding.

    - id: pass-006
      type: pass
      class: CONSTRAINT — scene-map coverage (URI-SCENE-WINDOW)
      what: >
        scene-map declares "coverage: 39/39 bones in exactly one scene" with no gaps
        or overlaps. Scene-A @1-@12 (12 bones) + scene-B @13-@24 (12 bones) + scene-C
        @25-@39 (15 bones) = 39 total. All scenes contiguous; no bone appears in two
        scenes; no bone is unassigned. PASS.
      why: No finding.

    - id: pass-007
      type: pass
      class: CONSTRAINT — scene-map per-scene caps
      what: >
        Sensory: 1 entry per scene at scene-open anchors (sensory:1 @1 / sensory:2 @13
        / sensory:3 @25). Cap ≤3 per scene. PASS.
        Feeling per-character per-scene: feel:1 @7 Taylor scene-A; feel:2 @39 Taylor
        scene-C. One entry per character per scene. Cap ≤1 per character per scene.
        Jarvis: 0 entries (card-fenced; documented and rubric-valid). PASS.
        Metaphor: 0 entries in any scene. Cap ≤1 per scene. PASS.
        Scene-open-orient: 0 fires. All 3 scene-boundary refusals documented in
        exposition file under fire-audit (all three refuse per fire-rule clause-b:
        loc-state fires at each scene-open anchor). PASS.
      why: No finding.

    # ── CLASS 9: AP-SCAN ─────────────────────────────────────────────────────

    - id: flag-008
      type: flag
      class: AP-SCAN — AP10 chassis at 17% (below saturation; advisory)
      what: >
        active-project/theater/facets/interest-narrator-b01-c04.md — two NI entries
        carry the inverted-predicate / closed-accounting chassis (AP10 pattern):
        narrator:3 @9: "the lever is no longer a question of whether; it has just
          become a question of how much"
        narrator:7 @31: "the half-step of yard-air between her hand and his is the
          exposure she has just paid in full"
        2 of 12 entries = 17%. URI-AP-SCAN-SATURATION threshold: ≥40%. 17% is below
        threshold. The .r2-decisions.md surfaces narrator:7 @31 as a "chassis-carry
        above cap" editor-revise candidate: "verb-driven closure swap recommended."
      why: >
        At 17% the AP10 chassis does not trip the HARD saturation gate. Advisory
        per the R2 decision shard: if a Phase 5b editor-revise pass fires, narrator:7
        @31 is the priority target for a verb-driven closure swap (replacing "is the
        exposure she has just paid in full" with a direct action-verb construction
        that preserves the half-step / yard-air image without the chassis template).
        narrator:3 @9 is the lower-priority target (peak-bone; "is no longer a question
        of whether" is a stronger structural use of the chassis than narrator:7's close).

    # ── CLASS 10: TASTE-FLAG ─────────────────────────────────────────────────

    - id: flag-009
      type: flag
      class: TASTE-FLAG — @22 pile-up stitcher-overload risk
      what: >
        After fault-003 resolution, proto-line @22 carries 7 co-located facets:
        mem:2, narrator:6, state:4, vibes:9, vibes:10, vibes:11, vibes:12.
        This is the chapter's highest-density anchor. The bone is "the insect-feed
        returns wren-stitch-maker-flea-bottom-ward" — the Wren-anchor-discipline
        protected-pattern bone in scene-B. The chapter goal declares this as the
        "load-bearing future-cost-collateral plant" (state-updates preamble
        SEAM-WREN-ANCHOR-DISCIPLINE).
      why: >
        Seven simultaneous facet inputs at @22 create a stitcher-overload risk for the
        worm-canon-pedant persona, which expects Taylor's interiority to register as
        sparse and operational at the precise beats where she holds back. A pile-up of
        7 at the held-back moment risks producing prose that explicates the holding-back
        rather than enacting it. The stitcher profile for b01c04 should configure the
        @22 vibes as bias signals (operator-bias mode) rather than as renderable content
        layers — mem:2 and narrator:6 carry the renderable interior; the 4 vibes carry
        operator bias only.

    - id: flag-010
      type: flag
      class: TASTE-FLAG — NI above-band prose-register risk
      what: >
        Interest-narrator-b01-c04.md at 31% density (12 fires / 39 bones). Even if
        fault-004 is resolved by carve-out preamble rather than deletion, the cape-fic-
        reader persona expects economical interiority for Taylor in an operational chapter.
        The chapter goal is "running the four-ward feed as continuous operation" — a mode
        in which Taylor's interior should register as disciplined background process,
        not foregrounded commentary.
      why: >
        Above-band NI at 31% across 39 bones means Taylor's interior monologue appears
        roughly every third bone. At the stitcher, this produces a prose register where
        narration competes with action for sentence-priority. The cape-fic-reader persona
        attack vector: the interiority reads as self-conscious rather than embedded. If
        fault-004 is resolved by deletion (Option A), this taste risk resolves
        automatically. If resolved by carve-out preamble (Option B), the stitcher profile
        should configure NI entries at held-bones and trail-bones as compression candidates
        (render only when the prose requires an interior bridge).

    # ── CLASS 11: PILE-UP REVIEW ─────────────────────────────────────────────

    - id: pass-008
      type: pass
      class: PILE-UP — @7 (4 co-fires)
      what: >
        @7 co-fires: feel:1, narrator:10, taylor-hebert-kl-122ac:1 (dialogue), vibes:1.
        Bone: "taylor-hebert-kl-122ac speaks to jarvis-coin-kl-courier."
        Each fire is independently warranted: dialogue is structural (speech bone);
        NI at the acceptance moment is mandatory (cost-tracking); feeling at the spoken
        yes (expressed: no / hand-closes-on-shed-wall) is the somatic-tell for the
        formal commitment; vibes:1 opens the atonement-as-repetition bundle on Taylor
        at the event-trigger. No forward-citation fault at @7. The state:1 back-
        reference in the cite-index co-list for narrator:10 is a back-reference to the
        @1 time-of-day entry (valid; @7 > @1). PASS.
      why: No finding.

    - id: flag-011
      type: flag
      class: PILE-UP — @9 (6 co-fires after fault-002 resolution; cross-anchor back-ref)
      what: >
        @9 after fault-002 removal of state:2: 6 co-fires remain: jarvis-coin-kl-courier:8,
        jarvis-coin-kl-courier:9, narrator:3, state:1 (back-reference), vibes:2, vibes:3.
        State:1 at @9 is a back-reference to the @1 time-of-day entry
        (studio.time_of_day: third-bell-noon → first-bell-morning). This is not a
        forward-citation fault (@9 > @1) but it is an atypical cross-anchor citation:
        @9 is citing a state entry authored at @1, pulling the chapter-open temporal
        context into the scene-A dialogue peak bone. Both @1 and @9 are in scene-A at
        first-bell-morning, so no temporal contradiction exists; the stitcher receives
        consistent temporal context.
      why: >
        Cross-anchor back-references are not prohibited, but the pattern (a scene-A bone
        re-citing a chapter-open state entry) is non-standard. The stitcher at @9 receives
        the @1 studio.time_of_day value as active rendering context. This is likely
        intentional (maintaining the first-bell temporal anchor through the acceptance
        scene) but is not annotated in the state-updates carve-out preamble. Flagged for
        awareness; not elevated to fault because the back-reference produces no
        contradiction and the temporal context is correct for @9.

    - id: pass-009
      type: pass
      class: PILE-UP — @36 (3 co-fires)
      what: >
        @36 co-fires: narrator:8, state:12, and the back-references from state:7 @27
        and state:8 @29 listed in the cite-index co-list for narrator:8. The cite-index
        entry for narrator:8 @36 co=[state:7, state:8, state:12] — state:7 and state:8
        are back-references (anchored at @27 and @29 respectively; both before @36).
        No forward-citations. Bone: "jarvis-coin-kl-courier exits the cooper's yard."
        World-axis peak bone: NI for the routing-cycle completion, state:12 for the
        actors_in_yard transition. Density appropriate for the chapter's peak bone. PASS.
      why: No finding.

    # ── CLASS 12: RUBRIC-FIDELITY ────────────────────────────────────────────

    - id: fault-007
      type: fault
      class: RUBRIC-FIDELITY — memory single-register without preamble-block carve-out
      what: >
        active-project/theater/facets/memory-b01-c04.md — post-R2 the file has 2 entries
        (mem:2 @22 + mem:4 @38), both in the earth-bet-displacement / un-priced-anchor
        family. Zero Westerosi-monument clamp entries. The file frontmatter documents:
        "doubled-register: earth-bet-displacement-x2 / westerosi-monument-clamp-x0
        (single-register per-episode; per-season coverage preserved; both-meaningful gate
        forced single-register selection — see decision shard PATTERN-SCAN)."
        The rubric-memory-flags.md doubled-register file-level requirement specifies
        ≥1 Earth-Bet displacement AND ≥1 Westerosi-monument clamp per episode file.
        The carve-out invoked (audience-meaningfulness failure for monument candidates
        without ASOIAF source-fluency) is documented in frontmatter metadata and in
        the .r2-decisions.md shard. However, no rubric-carve-out preamble block is
        present in the memory file body per the format specified by facet.schema.md
        §Rubric carve-out preamble. The .r2-decisions.md pre-flags this as
        "HARD candidate (RUBRIC-FIDELITY)" for Phase 5 auditor evaluation.
        Per facet.schema.md: "Carve-outs propagate to audit time: the auditor's
        RUBRIC-FIDELITY class checks per-entry annotations against the carve-out
        preamble; entries claiming a carve-out without annotation FAIL."
      why: >
        Two layers: (1) The per-episode doubled-register shape gate is not met —
        the file is single-register Earth-Bet displacement only. The carve-out
        rationale (audience-meaningfulness failure for monument candidates) may be
        valid, but without the preamble-block format the auditor cannot machine-verify
        it and the /and-stitch Phase 0 rubric scan will flag the file as an undefended
        violation. (2) The frontmatter-only documentation is explicitly insufficient
        per the schema's carve-out propagation rule.
      criteria: >
        Option A: Add a rubric-carve-out preamble block to memory-b01-c04.md in the
        format specified by facet.schema.md §Rubric carve-out preamble. The preamble
        must document: (a) the doubled-register rubric section being carved out of;
        (b) the scope (file-level; all entries); (c) the rule (per-episode single-
        register is permitted when monument candidates fail the both-meaningful gate
        for the active audience trio); (d) the coverage justification (per-season
        coverage preserved; ASOIAF-fluency gate fails for cape-fic-reader and
        worm-canon-pedant, which together constitute 2 of 3 active personas); (e)
        per-entry annotations: neither mem:2 nor mem:4 is a Westerosi-monument clamp
        candidate; carve-out applies to file-level shape gate only.
        Option B: Author a replacement Westerosi-monument clamp entry that passes the
        both-meaningful gate for the active audience trio without requiring ASOIAF
        source-fluency. The prior candidates (mem:1 @4 and mem:3 @33) both failed;
        any replacement must identify a monument or callback anchor that clears the gate
        for all three active personas.

    - id: fault-008
      type: fault
      class: RUBRIC-FIDELITY — NI band overshoot without machine-parsable carve-out
      what: >
        active-project/theater/facets/interest-narrator-b01-c04.md — density 31%
        exceeds the 15-25% rubric band ceiling. The file acknowledges this in
        frontmatter ("density: 31%") but provides no rubric-carve-out preamble block
        in the body per facet.schema.md §Rubric carve-out preamble.
        Per the schema: "entries claiming a carve-out without annotation FAIL."
        This is the RUBRIC-FIDELITY classification of the same finding as fault-004
        (FREQUENCY-BAND). The two findings share the same root cause (missing carve-out
        preamble for NI density overshoot) and share the same resolution path.
      why: >
        Without the machine-parsable preamble-block, the RUBRIC-FIDELITY check at
        /and-stitch Phase 0 cannot distinguish a defended overshoot from an undefended
        one. All entries in an undocumented above-band file implicitly "fail" the carve-out
        propagation rule. This blocks the stitcher's ability to validate the NI layer
        without triggering a false-positive redo cycle.
      criteria: >
        Congruent with fault-004 criteria. If fault-004 is resolved by deletion (Option A:
        reduce to ≤25%), fault-008 resolves automatically. If resolved by carve-out
        preamble (Option B), the preamble must be in the standard block format with
        per-entry annotations per facet.schema.md §Rubric carve-out preamble, not in
        narrative prose.

  # ── AUDIT SUMMARY ────────────────────────────────────────────────────────────

  summary:
    verdict: FINDINGS-PRESENT
    hard_count: 8
    signal_count: 11
    pass_count: 9
    total_findings: 28

    blocking_for_stitch: true
    blocking_reason: >
      fault-001 (Taylor dialogue ID collision; cite-graph ambiguity on the chapter's
      central utterance), fault-002 and fault-003 (forward-citations inserting wrong
      location and temporal state into @9 and @22 respectively), and fault-006
      (narrator:14 @33 orphan rendering without monument-ground) are the four
      pre-stitch blockers. fault-007/008 (carve-out format deficiencies) should also
      be resolved to prevent Phase 0 rubric-scan false-positive redo. fault-004/005
      (NI density + inert vibes entry) are fixer-scope corrections.

    class_breakdown:
      STRUCTURAL:       faults: [fault-001, fault-002, fault-003]  flags: [flag-001, flag-002]  passes: []
      FREQUENCY-BAND:   faults: [fault-004]                        flags: [flag-003, flag-004]  passes: []
      METADATA:         faults: []                                  flags: [flag-005, flag-006]  passes: []
      CURVE-SHAPE:      faults: []                                  flags: []                    passes: [pass-001]
      CONTRADICTION:    faults: []                                  flags: []                    passes: [pass-002]
      DEDUP:            faults: []                                  flags: [flag-007]             passes: []
      SUPERFLUOUS:      faults: [fault-005]                        flags: []                    passes: []
      CONSTRAINT:       faults: [fault-006]                        flags: []                    passes: [pass-003, pass-004, pass-005, pass-006, pass-007]
      AP-SCAN:          faults: []                                  flags: [flag-008]             passes: []
      TASTE-FLAG:       faults: []                                  flags: [flag-009, flag-010]  passes: []
      PILE-UP:          faults: []                                  flags: [flag-011]             passes: [pass-008, pass-009]
      RUBRIC-FIDELITY:  faults: [fault-007, fault-008]             flags: []                    passes: []

    priority_queue:
      - fault-001: STRUCTURAL / Taylor dialogue ID collision. Rename c04 entry to ID 4; update proto-line @7 citation.
      - fault-002: STRUCTURAL / proto-line @9 forward-cites state:2 @13. Remove [state:2] from @9; regenerate cite-index.
      - fault-003: STRUCTURAL / proto-line @22 forward-cites state:5 @25. Remove [state:5] from @22; regenerate cite-index.
      - fault-006: CONSTRAINT / narrator:14 @33 orphan. Delete entry OR author replacement memory at @33 passing both-meaningful gate.
      - fault-007: RUBRIC-FIDELITY / memory single-register; missing carve-out preamble block. Add preamble OR author monument replacement.
      - fault-008: RUBRIC-FIDELITY / NI band overshoot; missing carve-out preamble block. Resolved by fault-004 action.
      - fault-004: FREQUENCY-BAND / NI 31% vs 25% ceiling. Delete entries or add preamble.
      - fault-005: SUPERFLUOUS / vibes:7 @19 inert (bare proto-line, back=N). Delete entry.

    clean_passes_summary:
      Earth-Bet hard-fence: PASS — all text fields across all 12 files clean; no parahuman proper nouns.
      Scene-map coverage: PASS — 39/39 bones; no gaps; no overlaps.
      Scene-map per-scene caps: PASS — sensory ≤3/scene; feeling ≤1/char/scene; metaphor 0; scene-orient 0.
      Memory NI-spine: PASS — mem:2 @22 co-cites narrator:6; mem:4 @38 co-cites narrator:9.
      Taylor NI co-citation (SEAM): PASS — all 6 required anchors (@9/@15/@18/@22/@27/@31) covered.
      Curve-shape: PASS — rising dramatic shape; scene rhythm-shapes consistent A→B→C.
      Dialogue card-resolution: PASS — taylor-hebert-westeros.card.md and westeros-smallfolk.card.md both exist.
      AP10 chassis saturation: PASS — 17% < 40% threshold.
      Exposition fence-audit: PASS — all first-mention entries outside the {5..11} speech-bone fence window.
      Contradiction: PASS — no same-anchor incompatible-state beyond the forward-citation faults.
      Metaphor: PASS — 0 entries; zero-fire register-correct for transactional acceptance chapter.
      Feeling Jarvis: PASS — empty slice rubric-valid; card Hard Fence #2 documented; per-scene cap satisfied.
---
