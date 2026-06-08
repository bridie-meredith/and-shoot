audit: facets-final-r1
episode: b01-c01
date: 2026-05-25
mode: flag-only
status: FINDINGS-PRESENT
totals: 21 findings across 8 facets / facet-graph surfaces
cite_index_hash_checked: 0241e0529031804fa83d25c0fb7a5e0db2491571d2d83d9d9436c734627eca40

---

## STRUCTURAL

---

audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-25
  findings:

    - id: fault-001
      type: fault
      what: >
        proto-lines/b01-c01.md @12 cites [state:1] [state:2]; proto-lines @21 cites [state:4].
        In the consolidated state-updates.md, state:1=oswyn.location@21, state:2=oswyn.relationship@26,
        state:4=taylor.capability_axis@12. The actual taylor entries for bone @12 are state:3
        (deployment-state) and state:4 (capability_axis); both carry back=N in the cite-index
        (not back-linked from any proto-line). The actual taylor entry for bone @21 is state:6
        (social_tether_prot_axis); it also carries back=N.
        The proto-lines file was authored using pre-consolidation per-source slice IDs (taylor
        slice was 1-indexed internally before oswyn's two entries were prepended at consolidation).
        After consolidation, taylor's pre-consolidation IDs 1,2 became consolidated IDs 3,4;
        taylor's pre-consolidation ID 4 (social_tether@21) became consolidated ID 6. The proto-lines
        were not updated to reflect the new consolidated IDs.
      why: >
        The stitcher resolves [state:N] citations from the consolidated state-updates file by ID.
        At @12 the stitcher will read state:1 (oswyn location change @21) and state:2 (oswyn
        relationship change @26) instead of the taylor deployment and capability entries. At @21
        it will read state:4 (taylor capability_axis, anchored at @12) instead of the taylor
        social_tether entry. The oswyn state entries will be decorated onto the wrong bones;
        the taylor capability and social-tether state entries will be invisible to the stitcher.
        The chapter's two canonical axis-move moments (capability+1 at @12, social_tether+1 at @21)
        are the load-bearing substance anchors; stitcher mis-read of these is a downstream
        render fault.
      criteria: >
        proto-lines/b01-c01.md @12 must cite [state:3] [state:4] (the consolidated IDs for
        taylor's deployment-state and capability_axis entries). proto-lines @21 must cite [state:6]
        (the consolidated ID for taylor's social_tether_prot_axis entry). The cite-index must
        be regenerated after the proto-lines correction so that state:3 and state:4 carry back=Y
        anchored @12, and state:6 carries back=Y anchored @21.

    - id: fault-002
      type: fault
      what: >
        proto-lines/b01-c01.md @10 cites [feel:1] [feel:2]. In the consolidated feeling.md,
        feel:1 is the oswyn entry anchored @21 ("the hands settle at the apron-front");
        feel:2 is the taylor entry anchored @10 ("her breath empties out"). The cite-index
        shows feel:1 back=Y keyed to anchor @21 (from the @21 proto-line citation), not @10.
        feel:2 back=Y keyed to @10 (correct). The [feel:1] citation at @10 therefore references
        an entry whose canonical anchor is @21.
      why: >
        The stitcher at @10 will attempt to render feel:1 (oswyn's apron-front hand-settle,
        a post-rescue composure tell belonging to @21) alongside the scene-B approach-to-peak
        bone "taylor holds the feet." The oswyn somatic tell is contextually wrong at @10
        (Oswyn has not arrived on stage yet). The spurious feel:1 citation at @10 will either
        produce an incorrect co-decoration or create an unresolvable anchor mismatch depending
        on stitcher resolution logic.
      criteria: >
        proto-lines/b01-c01.md @10 must cite only [feel:2]. The spurious [feel:1] at @10
        must be removed. The cite-index must be regenerated to confirm feel:1 back=Y is
        anchored exclusively to @21.

    - id: fault-003
      type: fault
      what: >
        proto-lines/b01-c01.md @24 cites [feel:2] [feel:3] [narrator:8] [state:5]. In the
        consolidated feeling.md, feel:2 is the taylor entry anchored @10 ("her breath empties
        out"). feel:3 is the taylor entry anchored @24 ("her head fixes toward the alley-mouth").
        The cite-index shows feel:2 back=Y keyed to @10. The [feel:2] citation at @24 references
        an entry whose canonical anchor is @10. The cite-index does not show a second back-link
        for feel:2 from @24.
      why: >
        Same class of defect as fault-002: the stitcher at @24 will attempt to decorate the
        "taylor faces the alley-mouth" bone with feel:2 (the breath-empties-out tell from @10),
        which belongs to the scene-B approach zone and is temporally and contextually misplaced
        at @24 (scene-C post-peak trailing-edge). The chapter's cost-bearer-exclusion moment
        at @24 will carry an incorrect somatic decoration.
      criteria: >
        proto-lines/b01-c01.md @24 must cite only [feel:3] [narrator:8] [state:5]. The spurious
        [feel:2] at @24 must be removed. The cite-index must be regenerated.

    - id: flag-001
      type: flag
      what: >
        interest-narrator-b01-c01.md entries 7 (@3) and 8 (@24) are R2 adds. In the file as
        written, IDs are monotonic (1 through 8) but the anchor-order is non-monotonic: ID 7
        is anchored @3 (precedes IDs 1-6 anchor-wise) and ID 8 is anchored @24 (precedes ID 6
        anchored @27). The schema requires ID monotonicity per file; anchor-order monotonicity
        is not required by schema but produces a non-sequential reading order.
      why: >
        Per audit brief specification: "note as STRUCTURAL-NOTE, not block." No stitcher
        resolution failure results because IDs are monotonic. The anchor-order non-monotonicity
        may confuse manual review. No downstream consequence beyond inspection friction.

    - id: flag-002
      type: flag
      what: >
        state-updates.md and feeling.md are consolidated files (per r3-signal-001 single
        top-of-file frontmatter). Both files contain embedded secondary frontmatter blocks
        mid-file: state-updates.md has an oswyn-slice frontmatter at approximately line 52-56
        and a wren-slice frontmatter at approximately line 74-78 (with the wren block's opening
        `---` absent, producing a malformed YAML boundary). feeling.md has an embedded taylor-slice
        frontmatter at approximately lines 17-22 and a wren-slice frontmatter at approximately
        lines 29-33.
      why: >
        Per-slice frontmatter blocks are process artifacts from pre-consolidation authoring.
        In a properly consolidated file the single top-of-file frontmatter is the only YAML
        block; subsequent per-slice headers are prose comments (prefixed `#`), not frontmatter.
        A YAML parser or schema-validator reading the consolidated file will encounter multiple
        document-start signals. The wren slice in state-updates.md has a missing opening `---`,
        creating an unparseable YAML segment. If the schema-validator is strict, this produces
        a parse error on the wren state-updates slice.

    - id: flag-003
      type: flag
      what: >
        location-state-b01-c01.md contains zero entries. The bones header `locations:` is empty;
        no location-card slugs are declared for b01c01. The studio documented this as a
        rubric-carve-out (no slugs available; every movement-verb gate walk BLOCKED).
      why: >
        Per audit brief instruction: surface as STRUCTURAL-NOTE / process-gap, NOT a HARD finding.
        Phase 0 step 6 is satisfied trivially. Downstream consequence: (a) the stitcher has no
        loc-state tissue for any of the 27 bones; the spatial/orienting axis is entirely
        facet-bare. (b) The transition-run continuity license for scene-A @1-@6 (fusion-eligible)
        cannot fire — the `continuity-from` token would dangle with no prior loc-state entry.
        The three seams flagged by studio in the file (SEAM-LOC-CARDS-ABSENT,
        SEAM-TRANSITION-RUN-BARE, SEAM-001 fish-cart, SEAM-002 time-of-day baseline) are
        carried forward as known open items.

---

## FREQUENCY-BAND

---

    - id: fault-004
      type: fault
      what: >
        taylor-hebert-kl-122ac.md (dialogue file) contains 3 utterances from a single speaker
        (taylor-hebert-kl-122ac) all anchored at @16. The audit-class spec for dialogue states
        per-anchor cap ≤3 AND per-speaker per-anchor ≤1. The R2 decision shard for the dialogue
        facet treats only the total cap (≤3) as operative and does not acknowledge the per-speaker
        sub-cap. With all 3 utterances from the same speaker at the same anchor, the per-speaker
        per-anchor ≤1 constraint is breached regardless of the total count.
      why: >
        The per-speaker ≤1 sub-cap exists to prevent a single character from holding the
        floor at one bone beyond one utterance, which is a compression discipline (multiple
        utterances from one speaker at one bone collapse the chapter's cadence and are
        redundant by definition if the per-anchor total is the only gate). The R2 shard's
        per-anchor-only reading may be correct if the rubric text grants the ≤3 total as
        overriding — but that interpretation has not been verified against the rubric document.
        If the per-speaker ≤1 rule is the binding constraint, 2 of the 3 utterances are
        unauthorized at @16.
      criteria: >
        Fixer must determine whether the operative cap is per-anchor ≤3 total OR per-speaker
        per-anchor ≤1. If per-speaker per-anchor ≤1 is confirmed as the binding rule,
        the dialogue file must be reduced to 1 utterance at @16 for taylor-hebert-kl-122ac,
        with any cut utterances either deleted or relocated to a defensible anchor if one exists.
        If per-anchor ≤3 total is confirmed as the overriding rule, this fault is downgraded to
        a flag with a note that the audit-class spec is ambiguous and should be clarified.

    - id: flag-004
      type: flag
      what: >
        interest-narrator-b01-c01.md: 8 entries / 27 proto-lines = 29.6%. Rubric band is 15-25%.
        Over-band by 4.6 percentage points. The R2 decision shard justifies the over-band on
        two grounds: (1) mem:1 @3 required a NI co-citation per the cross-facet memory-needs-
        NI-spine contract (R2 add narrator:7 @3 addresses the AP7 spineless-fire risk);
        (2) the un-priced-anchor mechanic at @24/@27 required a two-step interior register
        (narrator:8 @24 + narrator:6 @27) that the rubric flags as a legitimate over-band motive.
      why: >
        The over-band is documented and attributed to specific cross-facet contract demands,
        not to unconstrained authoring. No stitcher render consequence is expected. Flag for
        post-stitch cold-read assessment to confirm the NI density reads as voice rather than
        over-registration.

    - id: flag-005
      type: flag
      what: >
        sensory-b01-c01.md: 2 entries / 27 proto-lines = 7.4%. Rubric band is 3-6%.
        Over-band by 1.4 percentage points. Both entries are in different scenes and different
        modalities (smell @2, sound @16); per-scene cap ≤3 satisfied in both scenes.
      why: >
        Small-denominator artifact of the 27-bone bones-only chapter. With 2 entries the
        percentage is dominated by rounding; one fewer entry would drop to 3.7% (within band).
        The over-band is not actionable unless the stitcher cold-read returns a
        sensory-heavy verdict.

    - id: flag-006
      type: flag
      what: >
        feeling.md (taylor-hebert-kl-122ac slice): 2 entries / 27 proto-lines = 7.4%.
        Rubric band is 2-5% per character. Over-band by 2.4 percentage points. Both entries
        are in different scenes (feel:2 @10 scene-B, feel:3 @24 scene-C); per-character
        per-scene cap ≤1 satisfied.
      why: >
        Same small-denominator artifact as flag-005. The per-scene cap is the operative hard
        gate; the frequency-band is a denominator artifact at 27 bones. Not actionable unless
        cold-read returns an over-somatic verdict for Taylor.

    - id: flag-007
      type: flag
      what: >
        exposition-b01-c01.md: 9 entries / 27 proto-lines = 33.3%. Rubric band is 1-5%.
        Over-band by 28.3 percentage points. The R2 shard explicitly validates this overage:
        under URI-SUBSTANCE-OVERHAUL bones-only chapter structure (27 anchors = 1 per bone),
        the per-episode caps are the binding constraint, not the sparsity band. Caps met:
        3 episode-open (≤4), 5 first-mention (≤12), 1 scene-orient (≤2).
      why: >
        The sparsity band's denominator assumption (100+ proto-lines for a pre-overhaul shoot)
        does not hold for a 27-bone bones-only chapter. The per-episode caps are the correct
        gate and all caps pass. The over-band percentage is a structural artifact with no
        actionable consequence unless the stitcher cold-read returns an exposition-dense verdict
        at Phase 9.

---

## METADATA-INCONSISTENCY

---

    - id: flag-008
      type: flag
      what: >
        feeling.md entry feel:3 was revised by R2 (VERDICT: REVISE) from the R1 text
        "her shoulders set down and back | expressed: yes" to
        "her head fixes toward the alley-mouth, away from the stitch-house lane | expressed: partial".
        The revised text appears in feeling.md. However, the R2 decision shard for feeling-taylor
        (section in .r2-decisions.md) describes the revision rationale in detail but the f-r2-4
        count in the taylor shard is 1 (graph-incoherence: the settle-register cross-character
        pattern between Oswyn @21 and Taylor @24 was the flagged finding). The consolidated
        f-r2-counts in the top frontmatter show f-r2-4: 1 total. This is structurally consistent.
        Note: the revision is complete and the revised text is the canonical form. This flag
        records that f-r2-4 = 1 is attributable to the feel:3 settle-pattern finding, and the
        resolution (revision) is in-file.
      why: >
        The f-r2-4: 1 count in the consolidated R2 decisions frontmatter must be traceable.
        It is traceable to the taylor feeling shard. No downstream consequence; the revision
        is already applied.

---

## CURVE-SHAPE

---

    - id: flag-009
      type: flag
      what: >
        Chapter dramatic_shape is `rising`. Scene-A (flat-low) → Scene-B (peak-and-release @12)
        → Scene-C (peak-and-release @21). Facet distribution by scene:
        NI: A=2 entries, B=3, C=3. State: A=0, B=3, C=4 (including @26). Vibes: A=2 off-anchor,
        B=3 (@12), C=3 (@21)+2 (@27). Feeling: A=0, B=1, C=3 (oswyn+taylor+wren).
        The per-scene citation density escalates: scene-A has 4-5 anchored decorations,
        scene-B has 7-9 (pile-up at @12), scene-C has 10-12 (pile-up at @21 + @27 cluster).
        Curve is structurally consistent with `rising` and both scene-B and scene-C
        `peak-and-release` patterns.
        Note: scene-C peak at @21 carries 8 co-located citations vs. scene-B peak at @12 with
        6 — scene-C is heavier-decorated than scene-B, which is correct for a rising arc where
        the social consequence (witch-label assembling) outweighs the capability event
        (prohibition crack) in register weight.
      why: >
        Curve-shape verdict: PASS. No structural deviation from declared `dramatic_shape: rising`
        detected. Recording as a flag (positive check result) per audit format.

---

## CONTRADICTION

---

    - id: flag-010
      type: flag
      what: >
        No cross-facet contradictions found. Checked:
        (a) state:3 @12 (deployment-state: passive -> active) vs. state:4 @12 (capability_axis:
            2 -> 3) — different fields, complementary not contradictory.
        (b) mem:1 @3 (Earth-Bet discipline residue) vs. exposition:1 @0 (function-form Khepri
            reference) — same monument, different registers; no contradiction.
        (c) feel:1 @21 (oswyn hands settle) vs. narrator:5 @21 (elder did the work a word would
            do in a week — R2 revised form) — different facet types, consistent at the same bone.
        (d) vibes:5/6/7 @21 (witch-label-assembling cluster) vs. mem:2 @26 (the chin-lift
            as word-finding-person) — temporal sequence is consistent (assembling @21,
            completing @26).
      why: >
        Recording as a flag (positive check result). No fixer action required.

---

## DEDUP

---

    - id: flag-011
      type: flag
      what: >
        Potential near-overlap between narrator:8 @24 and feel:3 @24. NI content:
        "she set the body to the alley-mouth so the stitch-house lane would not need
        to be registered again." feel:3 content: "her head fixes toward the alley-mouth,
        away from the stitch-house lane | expressed: partial." Both entries address the
        same body-orientation move at @24, with the same directional marker
        ("alley-mouth") and the same exclusion-reference ("stitch-house lane").
      why: >
        The facets serve different functions: NI renders the interior motive
        ("so the stitch-house lane would not need to be registered again") while
        the feeling renders the somatic tell ("head fixes toward") at expressed: partial.
        These are distinct facet-type outputs and the stitcher uses them in different
        render phases. The overlap in referent (alley-mouth / stitch-house) is thematic,
        not redundant. Flag as near-overlap for stitcher attention; not a fault unless
        the cold-read returns the two entries as a doubled register.

---

## SUPERFLUOUS

---

    (No findings. Lonely entries identified in cite-index — narrator:1@4, narrator:2@8,
    narrator:3@11, sensory:1@2, exposition:1-3@0, exposition:6@7, exposition:7@18 — were
    each reviewed against the three-axis superfluous test. R2 shard provides per-entry
    justification with at-rest cold reads. No entry fails the three-axis test. No
    superfluous findings.)

---

## CONSTRAINT

---

    - id: fault-005
      type: fault
      what: >
        vibes-b01-c01.md entry vibes:3 [@12] token "instinct-preceded-the-ledger-entry"
        within the token bundle [prohibition-crossed-before-it-was-filed,
        instinct-preceded-the-ledger-entry, deployment-preceding-permission].
        The token "instinct-preceded-the-ledger-entry" parses as a complete sentence:
        subject (instinct) + finite verb (preceded) + object (the-ledger-entry).
        The schema rule for vibes tokens is explicit: "a token is forbidden if it parses
        as a complete sentence with subject + finite verb + object."
      why: >
        A sentence-parseable token in the vibes bundle crosses the schema's token-form
        boundary. The vibes schema intends tokens as compressed noun-phrases for
        word-algebra operator use; a parseable sentence introduces a predication that
        a noun-phrase operator cannot safely consume. The stitcher or bias-consumer
        that reads this token may interpret it as a prose instruction rather than a
        word-algebra bias, producing uncontrolled output.
      criteria: >
        The token must be revised to a noun-phrase form that preserves the semantic
        content without a parseable subject-verb-object structure. Acceptable forms:
        "instinct-preceding-the-ledger-entry" (gerund, not finite verb) or
        "the-ledger-entry-outrun-by-instinct" (nominalised form with no finite verb).

    - id: flag-012
      type: flag
      what: >
        mem:2 @26 NI spine gap. No interest-narrator entry fires at @26. The cross-facet
        contract (memory-flags require NI co-citation) is unresolved at this anchor.
        The R2 shard defends mem:2 on multi-justification grounds (monument-grade
        Westerosi clamp + state:2/@26 and state:6/@21 co-citation + multi-justification
        convergence) and notes the spine gap as a plausible upstream-NI-fire defect
        rather than a memory-entry defect. AP7 (spineless fire) applies in strict reading.
      why: >
        The NI layer is silent at @26 ("oswyn lifts the chin"), which is the chapter's
        witch-label-completion beat. Taylor's interior read of the chin-lift (the
        foreknowledge-clamp that the older stories frame) is carried entirely by mem:2.
        Without NI at @26, the stitcher has no interior-register decoration at the
        categorization-completing bone except the memory callback. The chapter does not
        fail, but the @26 interior is thinner than the @12 and @21 peaks by one layer.

    - id: flag-013
      type: flag
      what: >
        mem:1 target-ref slug is `cond-override-architecture-residue-122ac` (a condition
        card at active-project/warehouse/). mem:2 target-ref slug is
        `cond-kl-witch-label-formation-122ac` (a condition card at active-project/warehouse/).
        The R2 memory shard notes both as SIGNAL-not-HARD: the memory rubric expects
        `monument-*` slug format for target-refs; condition-card slugs are used instead.
        Gloss-clarity at-rest tests pass (the condition cards' content is semantically
        appropriate for the memory callback), but the slug form violates the rubric's
        monument-slug convention.
      why: >
        Downstream citation resolution uses the target-ref slug as the canonical
        monument-card pointer. If a future run requires monument-card resolution
        (e.g., orchestrator-critic book verdict or /and-review consistency run), the
        condition-card slugs will not resolve as `monument-*` cards. The gloss content
        is correct; the slug form is wrong. A margit referral to author `monument-*`
        wrapper cards for these two targets would resolve the inconsistency without
        changing the memory entries' substance.

    - id: flag-014
      type: flag
      what: >
        exposition-b01-c01.md preamble (exposition:1 @0) contains "Two hundred metres
        of them, dense as the air." The taylor-hebert-westeros behavior card §Vocabulary
        explicitly replaces "meter" with "paces, stones, the length of the long field"
        for Westerosi-context authoring. The base card (taylor-hebert) uses metric
        specificity ("About three meters") as an in-register interior voice tell.
        The preamble renders as inner monologue / first-person Taylor and is not dialogue.
        The hard fence per cond-earth-bet-noun-fence applies to "proper nouns, institutional
        terms, and cape-register jargon" — metres is a unit of measure, not a proper noun.
        The conflict is between the base card's metric-specificity voice-tell and the
        westeros-variant card's vocabulary restriction.
      why: >
        The exposition preamble is the project's first reader-facing Taylor voice. If
        the westeros-variant vocabulary restriction applies to inner monologue as well
        as dialogue, "Two hundred metres" is a card violation. If the base card's
        interior-voice metric specificity governs preamble register, it is in-voice.
        The ambiguity between base-card interior register and westeros-variant vocabulary
        override should be resolved before /and-stitch. If the westeros card governs,
        the preamble must substitute a period-plausible Westerosi range descriptor.

---

## AP-SCAN

---

    (fault-005 above is the operative AP-SCAN finding under CONSTRAINT.
     Additional AP-SCAN results by class:)

    - id: flag-015
      type: flag
      what: >
        AP-001 (definitional-collapse "X is/was Y") count in interest-narrator-b01-c01.md:
        1 instance (narrator:4 @12: "the telling was a thing she would not name").
        The ≤1-per-file cap for strict AP-001 template is satisfied. narrator:5 @21 was
        revised (R2 VERDICT: REVISE) specifically to remove the second AP-001 instance.
        No other entries contain the template. Scan result: PASS at-cap.
        Recording as a flag (positive check result with at-cap note) for completeness.
      why: >
        At-cap is not a violation but is a proximity alert. Any future /and-facets revise
        or add targeting this file must treat the AP-001 slot as consumed. A second AP-001
        instance added in a future run would breach the cap.

    - id: flag-016
      type: flag
      what: >
        Dialogue AP chassis-contamination scan (em-dash, semicolon in spoken-line text):
        "Fever. Not the croup." — no chassis punctuation. "She needs air. Stand back." —
        no chassis punctuation. "Who knows her? Fetch them." — no chassis punctuation.
        Scan result: PASS. Anachronism scan: "Fetch," "the croup," "Stand back" — all
        period-plausible per taylor-hebert-westeros §Vocabulary. PASS. AP-modern-hr-speak,
        AP-deposition-cadence, AP-nominalization: none present. PASS.
        Earth-Bet proper-noun scan (Brockton Bay, Skitter, Khepri, PRT, Endbringer,
        Gold Morning, Cauldron, etc.): absent from all three utterances. PASS.
        Recording as a flag (positive check result) per completeness requirement.
      why: >
        All dialogue AP classes pass. No fixer action required.

---

## TASTE-FLAG

---

    - id: flag-017
      type: flag
      what: >
        scene-A (bones @1-@6, flat-low rhythm) renders facet-bare on the spatial/orienting
        axis (loc-state zero-entry, no loc-state decoration anywhere in the chapter) and
        thin on interior register: only narrator:7 @3, narrator:1 @4, and sensory:1 @2
        carry this 6-bone run. No feeling entries in scene-A. No memory entries (mem:1
        anchors @3 but is categorized as a scene-A entry). No vibes-with-anchor in scene-A
        (vibes:1 and vibes:2 are off-anchor). The prohibition-maintenance subsistence run
        has limited decoration for the stitcher to work with.
      why: >
        The studio loc-state file flagged SEAM-TRANSITION-RUN-BARE: scene-A @1-@6 is
        fusion-eligible and facet-bare, with risk of metronomic render. The sensory facet
        (sensory:1 @2) is the primary live mitigation. If the stitcher renders @1-@6 with
        only NI@3/@4 and sensory@2 as decoration, the opening six bones may read as
        undifferentiated environmental description. Not a fault at the facet layer; watch
        at /and-stitch Phase 9 cold-read.

    - id: flag-018
      type: flag
      what: >
        interest-narrator-b01-c01.md: 5 of 8 entries use past-perfect tense as the primary
        construction (narrator:2 "had carried," narrator:3 "was already priced," narrator:4
        "had told," narrator:5 "had taken," narrator:7 "cost... paid"). The R2 shard
        identifies this as the pre-calc signature (actions completed before the scene's
        present moment). All five uses are structurally justified per the R2 judge.
        At 62.5% saturation, the single-tense concentration is a voice-sameness risk
        for stitcher prose rendering.
      why: >
        Individual entries are justified; aggregate tense-concentration may produce a
        repetitive interior rhythm if the stitcher renders the NI entries in close proximity.
        Watch at /and-stitch Phase 4 (local flow + speaker-paragraph breaks) to confirm
        past-perfect entries do not cluster into consecutive paragraph-opening beats.

---

## PILE-UP REVIEW

---

    - id: flag-019
      type: flag
      what: >
        @21 pile-up (8 co-located facets): exposition:8, feel:1, narrator:5, state:1,
        state:4 (pre-consolidation ID; corrected to state:6 per fault-001), vibes:5,
        vibes:6, vibes:7 at "oswyn-mudway-flea-bottom-elder takes the lane-mouth."
        After fault-001 correction the count remains 8 (state:4 → state:6 is a
        same-count substitution).
      why: >
        Verdict: WARRANTED. Scene-C peak-bone (social_tether-prot-rise +1 axis-move,
        witch-label assembly). Each entry serves a distinct structural purpose: exposition:8
        (identity introduction for reader), feel:1 (Oswyn somatic tell), narrator:5
        (Taylor's foreknowledge-clamp on the categorization), state:1 (Oswyn location
        state-change), state:6 (Taylor axis-move), vibes:5 (Oswyn as categorizing witness),
        vibes:6 (Taylor entering ward accounting), vibes:7 (episode witch-label-assembling
        scope). Eight facet types, eight structural roles. Metaphor correctly refused at
        this anchor on pile-up-saturation grounds. No over-decoration finding.

    - id: flag-020
      type: flag
      what: >
        @12 pile-up (6 co-located facets): narrator:4, state:1, state:2, vibes:3, vibes:4,
        vibes:8 at "the insects propagate." After fault-001 correction the citations are
        narrator:4, state:3, state:4, vibes:3, vibes:4, vibes:8 (same count, corrected IDs).
      why: >
        Verdict: WARRANTED. Scene-B peak-bone (capability +1 axis-move, prohibition-crack
        threshold crossing). Each entry: narrator:4 (interior rupture — "the telling was a
        thing she would not name"), state:3 (deployment-state axis-move), state:4
        (capability_axis axis-move), vibes:3 (actor-level the-first-crack), vibes:4
        (episode threshold-crossed-unconsented), vibes:8 (loc-flea-bottom rescue-witnessed).
        Six entries, six structural roles. No over-decoration finding.

---

## RUBRIC-FIDELITY

---

    - id: flag-021
      type: flag
      what: >
        state-updates.md entry state:5 @17 (taylor posture: in-the-gap ->
        hands-up-mouth-shut-witness-facing) carries no NI or feeling co-citation.
        The cite-index shows state:5 @17 back=N co=[state:3]. No feeling entry fires
        at @17 (feel:2 is @10, feel:3 is @24). No NI entry fires at @17 (NI fires at
        @12 and @21 in the vicinity). The rubric's POV co-citation discipline (state
        entries for the POV character should be co-cited with NI or feeling to confirm
        the interior axis-move registers) is not satisfied at @17.
      why: >
        state:5's posture-shift (in-the-gap → hands-up-mouth-shut-witness-facing) is a
        persistent state that runs from @17 through @22 and is load-bearing for the
        witness-categorization beats (@19, @20, @21) in scene-B's resolution. Without
        NI or feeling co-citation, the stitcher has no interior-spine anchor at @17 to
        pair with the posture-change. The hands-up-mouth-shut image is the chapter's
        key public-frame transition and lacks interior registration at its bone. Compare:
        state:3/@12 has narrator:4 co-citation; state:6/@21 has narrator:5 co-citation.
        @17 is the outlier.

---

## Parking-lot

---

    pl-2026-05-25-004 (SOFT — target /and-facets b01c01):
      Resolution: RESOLVED by routing (a). Bone 16 SVO "taylor-hebert-kl-122ac raises
      the voice" (physical-action shape) was accepted as the dialogue anchor per routing
      option (a) — the chunk text is explicit that the voice carries instruction; the
      verb "raises" is the bone-of-record for the speech-act; flat_id stability preserved
      across all 27 bones. Three utterances authored at @16 within the total per-anchor
      cap (≤3). The dialogue file carries `routing_note: Routing (a) per pl-2026-05-25-004`.
      resolved_at: 2026-05-25
      resolved_by: /and-facets b01c01 Phase 5 audit (routing (a) confirmed operational)
      resolution_note: >
        Dialogue author elected routing (a); bone 16 treated as dialogue anchor.
        Three utterances authored matching chunk three-part information delivery
        (fever / air / known-adult). Citation completeness resolved at R2.
        Parking-lot item closed. Per-speaker per-anchor cap question surfaced as
        fault-004 in this report — separate finding, does not re-open this item.

    pl-2026-05-25-003 (SOFT — target /and-write scope `*`):
      Not in /and-facets scope. Per brief instruction: noted in summary only.
      (a) SOFT-CURVE-moral_framework — bone-level moral_framework movements should
      respect concentration at d03/d07/d12 rather than uniform distribution.
      (b) 8 INFERENTIAL-ANCHOR / NAMING-INCONSISTENCY findings on the cost_ledger.
      Both remain open as /and-write watch-items. No /and-facets action.

---

## Audit summary

Total findings: 21
  - fault (blocking): 5 (fault-001, fault-002, fault-003, fault-004, fault-005)
  - flag (non-blocking): 16 (flag-001 through flag-021, excluding fault slots)

Hard findings (fault type): 5
Signal findings (flag type): 16

Classes with findings:
  STRUCTURAL: 6 (fault-001, fault-002, fault-003, flag-001, flag-002, flag-003)
  FREQUENCY-BAND: 5 (fault-004, flag-004, flag-005, flag-006, flag-007)
  METADATA-INCONSISTENCY: 1 (flag-008)
  CURVE-SHAPE: 1 (flag-009 — PASS)
  CONTRADICTION: 1 (flag-010 — PASS)
  DEDUP: 1 (flag-011)
  SUPERFLUOUS: 0
  CONSTRAINT: 5 (fault-005, flag-012, flag-013, flag-014, flag-015 grouped by class; note fault-005 filed under CONSTRAINT above)
  AP-SCAN: 2 (flag-015, flag-016)
  TASTE-FLAG: 2 (flag-017, flag-018)
  PILE-UP REVIEW: 2 (flag-019, flag-020 — both WARRANTED)
  RUBRIC-FIDELITY: 1 (flag-021)

Curve-shape verdict: PASS — chapter pressure-signal curve is consistent with
  `dramatic_shape: rising` and per-scene rhythm shapes (flat-low → peak-and-release
  → peak-and-release). Scene-C peak (@21, 8 citations) correctly outweighs scene-B
  peak (@12, 6 citations) in facet density, consistent with a rising arc where the
  social consequence (witch-label formation) registers above the capability event
  (prohibition crack) in structural weight.

R2 consolidated f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 1}.
  f-r2-4 = 1 (attributable to feel:3 settle-pattern revision). Threshold: f-r2-1 > 0
  is HARD (not triggered); f-r2-2 + f-r2-3 + f-r2-4 > 2 is SIGNAL (1 ≤ 2, not triggered).
  F-R2 gates: PASS.

Dominant fault class: STRUCTURAL — three citation-ID faults in the proto-lines file
  (fault-001, fault-002, fault-003) all stem from the same root cause: the proto-lines
  file uses pre-consolidation per-source slice IDs that were invalidated when state-updates
  and feeling slices were merged into consolidated files with a shared ID namespace.
  These three faults share a single fix: regenerate the proto-lines citation tags from
  the consolidated files' IDs and regenerate the cite-index.

---

## Routing

  fault-001, fault-002, fault-003 → fixer: proto-lines citation correction.
    Root cause is shared; fix should be executed as a single pass.
    After proto-lines correction: cite-index must be regenerated.
    Downstream: /and-stitch Phase 0 must re-check the cite-index hash.

  fault-004 → fixer: determine operative per-speaker per-anchor cap from the
    dialogue rubric document; if ≤1 is confirmed, reduce dialogue file to 1
    utterance at @16 for taylor-hebert-kl-122ac.

  fault-005 → fixer: revise vibes:3 token "instinct-preceded-the-ledger-entry"
    to a noun-phrase form (no finite verb).

  flag-012, flag-013 → margit referral recommended: monument-* cards for
    cond-override-architecture-residue-122ac and cond-kl-witch-label-formation-122ac
    would resolve the target-ref slug-form inconsistency without touching the
    memory entries' substance.

  flag-014 → screen-writer or exposition-author: clarify whether the westeros-variant
    vocabulary restriction (meter → paces) applies to preamble inner monologue.
    If it does, revise exposition:1 preamble "Two hundred metres" to a
    period-plausible Westerosi range descriptor.

  flag-021 → note for /and-facets revise if NI re-run is dispatched: consider
    adding a narrator entry at @17 to co-register the posture-shift interior.

  All remaining flags → /and-stitch attention. No fixer dispatch required.
    Phase 9 cold-read gate is the downstream checkpoint for flag-017 (scene-A thin),
    flag-018 (past-perfect tense saturation), and the frequency-band over-band flags
    (flag-004 through flag-007).
