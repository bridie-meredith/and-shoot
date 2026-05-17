```yaml
audit:
  scope: series
  target: mirror-tragedy — condition card set (Phase 1d)
  timestamp: 2026-05-17
  findings:

    # ── SCHEMA COMPLIANCE ─────────────────────────────────────────────────────

    - id: finding-001
      type: fault
      what: >
        cond-feudal-hierarchy-law.card.md and cond-smallfolk-political-physics.card.md —
        both carry `scope: library` but both reference each other in their `references:`
        lists. The frontmatter on both cards is otherwise well-formed (class: condition,
        origin: authored, quality: full, world: planetos). However, neither carries a
        `project:` field. This is correct for library-scope cards per schema. No
        compliance fault here.
        RE-CLASSIFIED: pass — see note below.
      why: >
        On review, library-scope cards are not required to carry `project:`. The schema
        requires `project:` only when `scope: project`. Both library cards comply.
      criteria: null
      # Reclassified to pass after verification. Retaining entry to show the check ran.

    - id: finding-002
      type: fault
      what: >
        cond-feudal-hierarchy-law.card.md references `cond-westerosi-customary-authority-jaehaerys`
        and `cond-suppression-policy-progression` in its `references:` list. Neither of
        these cards is present in `active-project/warehouse/` or identified in the 1c
        candidate menu. Both are cited in body text as mandatory companion cards
        ("load this card with cond-westerosi-customary-authority-jaehaerys" in Interaction
        Notes; "Stage 3 threshold in cond-suppression-policy-progression" as a live
        cross-reference in the legal-physics description).
      why: >
        `cond-westerosi-customary-authority-jaehaerys` and `cond-suppression-policy-progression`
        are referenced in the body text of cond-feudal-hierarchy-law as if they are
        companion cards that must be co-loaded for scenes. If they are not present in
        the warehouse, any agent attempting to load cond-feudal-hierarchy-law in full
        will encounter dangling references. The Interaction Notes and the Stage 3
        cross-reference are load-bearing instructions — they direct agents to use those
        cards. Without the cards present, the instruction leads nowhere. This is a
        library-origin card repurposed for a project that may not have stocked all
        library companions.
      criteria: >
        Either (a) the referenced cards are confirmed present in the warehouse or
        library and accessible at load time, or (b) the references are removed or
        annotated as out-of-scope for this project and the body text cross-references
        to Stage 3 thresholds and behavioral-physics companions are scoped appropriately.

    - id: finding-003
      type: fault
      what: >
        cond-smallfolk-political-physics.card.md references
        `cond-westerosi-customary-authority-jaehaerys` in its `references:` list and
        in its Interaction Notes ("Both should be loaded for scenes involving Taylor's
        relationship to smallfolk characters"). The same dangling-reference condition
        as finding-002.
        Additionally, cond-smallfolk-political-physics.card.md references named
        characters in its body text — "Mira Stonefield-Jaehaerys", "Septon Rowan",
        "Aldric Pryor", "Clem Ferris", "Pryor" — who are not members of the approved
        cast from 1c. The 1c-log shows no cast members from the Riverlands; the project
        is set in King's Landing. These named characters appear to be carry-forward
        from an earlier project configuration (the library card was authored for a
        Riverlands-set project).
      why: >
        This is a library card loaded into a King's Landing project. The card's body
        text populates specific named characters (Mira, Septon Rowan, Aldric Pryor,
        Clem Ferris) as if they are active in the project, but none of these appear
        in the approved 1c cast. The Interaction Notes instruct impersonators playing
        "supporting smallfolk characters" to load this card — but the supporting
        smallfolk named in the card are Riverlands-specific, not Flea Bottom-specific.
        An impersonator loading this card for Flea Bottom smallfolk scenes will receive
        character-specific guidance for characters who do not exist in this project,
        and will not receive guidance calibrated to Flea Bottom's specific social
        physics (which is handled by cond-flea-bottom-social-physics, a separate card).
        Risk: impersonator uses wrong social-setting guidance or invents Riverlands-
        context details in a KL-set scene.
      criteria: >
        The Interaction Notes section of cond-smallfolk-political-physics must be
        amended for this project to (a) remove or reframe the named character
        references to those absent from the KL cast, and (b) direct agents to
        cond-flea-bottom-social-physics as the primary smallfolk-physics card for
        KL scenes. Alternatively, a project-scope override card may be authored that
        replaces the Interaction Notes and named-character references.

    - id: finding-004
      type: fault
      what: >
        cond-kl-witch-label-formation.card.md references `cond-westerosi-superstition-frame`
        and `cond-crownlands-superstition-frame-125ac` in its `references:` list. Neither
        of these cards is present in `active-project/warehouse/`.
        The card explicitly notes: "This card is the KL-specific version of
        cond-westerosi-superstition-frame and cond-crownlands-superstition-frame-125ac.
        The prior cards were authored for a project in which Taylor's swarm-control was
        the visible trigger." The card states it supersedes or replaces them for this
        project, yet still lists them as `references:`, which implies they should be
        loadable companions.
      why: >
        If the card was authored to supersede the prior cards for this project, the
        `references:` field should not list them as active references — it should use
        `supersedes:` frontmatter instead (per schema: "new card sets supersedes: [old-slug]").
        As written, the references field points to cards that are either absent from the
        warehouse or have been functionally superseded by this card. An agent following
        the references will look for cards that either don't exist here or whose content
        this card has already incorporated. This is a frontmatter structure fault, not
        a content fault.
      criteria: >
        The references: list should remove cond-westerosi-superstition-frame and
        cond-crownlands-superstition-frame-125ac. If these cards exist in the library
        and this card supersedes them for this project, the appropriate mechanism is
        supersedes: in frontmatter, not references:. If they do not exist, the references
        are simply dangling and should be removed.

    - id: finding-005
      type: fault
      what: >
        cond-shard-deposit-mechanics-mirror.card.md references `cond-no-parahuman-infrastructure`
        in its `references:` list and in its Interaction Notes ("With cond-no-parahuman-infrastructure:
        That library card establishes the general absence of parahuman infrastructure in
        Westeros"). This card is not present in `active-project/warehouse/` and does not
        appear in the 1c candidate menu.
        Additionally, the card's Description states: "This card supersedes
        cond-reincarnation-mechanics-125ac for this project." It does not carry a
        `supersedes:` frontmatter field pointing to cond-reincarnation-mechanics-125ac,
        and does not carry the schema-required structure for supersession (old card
        should carry superseded_by, new card should carry supersedes: [...]).
      why: >
        The dangling reference to cond-no-parahuman-infrastructure is the same
        fault-class as findings 002-004: a referenced card that is not present will
        produce failed loads for agents trying to load the full card stack. The
        supersession claim ("This card supersedes cond-reincarnation-mechanics-125ac")
        in the body text without the corresponding frontmatter structure is a schema
        compliance fault — supersession requires formal frontmatter fields, not body-text
        declaration, per card.schema.md ("Old card sets superseded_by: ... New card sets
        supersedes: [...]").
      criteria: >
        (a) cond-no-parahuman-infrastructure must be stocked in the warehouse or the
        reference removed and the body text reframed. (b) If cond-reincarnation-mechanics-125ac
        exists in the library, the supersession must be formalized per schema: this card
        adds supersedes: [cond-reincarnation-mechanics-125ac] to its frontmatter, and
        the library card adds superseded_by: cond-shard-deposit-mechanics-mirror. If the
        library card does not exist, the body-text claim is harmless but the supersedes:
        frontmatter field is still the correct structural form.

    - id: finding-006
      type: flag
      what: >
        cond-kl-feudal-physics-mirror.card.md references `cond-westerosi-customary-authority-125ac`
        in its `references:` list. This is a different card slug from the
        `cond-westerosi-customary-authority-jaehaerys` referenced by the two library cards
        (findings 002-003). The slug variant `-125ac` vs `-jaehaerys` may indicate two
        separate library cards (period-specific variants: one for 84-101 AC Jaehaerys era,
        one for 125 AC pre-Dance era), or it may indicate a naming inconsistency where
        one card is referenced under two different slugs.
      why: >
        If `-125ac` and `-jaehaerys` are two separate cards: both may be absent from the
        warehouse, and the project needs to stock the appropriate one (the 125 AC variant
        for the KL card). If they are the same card with inconsistent slugs: the slug
        mismatch means one reference will fail at load time. Either way, the absence
        of cond-westerosi-customary-authority-125ac from the warehouse is the same
        dangling-reference fault-class as findings 002-005. Flagged rather than faulted
        because the resolution depends on determining which card(s) exist in the library.
      criteria: null

    # ── WORLD-NOTES CONSISTENCY ────────────────────────────────────────────────

    - id: finding-007
      type: pass
      what: >
        Flicker discipline binding rules (world-notes.md § Taylor's setup state).
        cond-flicker-discipline-mirror.card.md checked against all seven binding rules.
      why: >
        All seven rules are present, sourced to world-notes.md, and correctly stated.
        Rule 1 (involuntary), Rule 2 (unreliable), Rule 3 (must cost), Rule 4 (near-dragon
        louder not more reliable), Rule 5 (Gold Morning pattern-recognition), Rule 6
        (kill-misfire specifics), Rule 7 (hard fences) — all present and correctly
        attributed. No violation found.

    - id: finding-008
      type: pass
      what: >
        Two-register architecture binding rules (world-notes.md § Presentational layer).
        cond-series-tone-mirror.card.md checked against all binding constraints.
      why: >
        Body register (grim-literary, close-third Taylor exclusive, no multi-POV,
        no editorialization), coda register (cold institutional, hard register-break,
        explicit counterfactual naming required, closing-beat order fixed), prohibited
        registers (warmth in coda, ambiguity in counterfactual, melodrama at bad act),
        and register-break structural requirement — all present and correctly stated.
        The single-book scope implications section correctly notes that tone architecture
        is sustained across novel length. No violation found.

    - id: finding-009
      type: pass
      what: >
        Chronicler counterfactual demand (world-notes.md § Plot spine and § Cost/closing,
        binding carry-forwards from 1b Batches C and D).
        cond-series-tone-mirror.card.md § Coda Register, requirement 1.
      why: >
        The card states the requirement correctly: "The coda MUST name the opposite-number's
        counterfactual. Not imply it — name it." This matches world-notes.md verbatim:
        "The chronicler frame MUST name the opposite-number's counterfactual EXPLICITLY
        in the closing pages." Closing-beat ordering (chronicler → cost-bearer's death)
        is also correctly stated with the world-notes "automatic revise" trigger preserved.
        No violation found.

    - id: finding-010
      type: pass
      what: >
        Dragon-claiming canon-adherence binding rules (world-notes.md § Plot spine,
        carry-forward: "wrong-rider mechanic must hold to ASOIAF dragon-claiming lore").
        cond-dragon-bonding-claiming-rules.card.md checked against all lore sections.
      why: >
        Targaryen-blood prerequisite, bonding stages (approach → hostility → mounting →
        recognition), claiming-window mechanics post-bonder-death, Dragonseeds precedent,
        and the project-specific application (wrong-rider claiming via neutral window
        mechanics) — all present and sourced to Fire & Blood / ASOIAF canon. The binding
        lore constraint in the card explicitly prohibits invented dragon-bonding rules.
        No violation found.

    - id: finding-011
      type: pass
      what: >
        Patron's wrong-theory binding rules (world-notes.md § Taylor's political position,
        carry-forward: "patron's wrong-theory-of-Taylor is the structural seam where the
        collision lives"; "BINDING: no agent writes a scene where the patron explicitly
        acknowledges wrong-theory during alignment phase").
        cond-patron-amplification-theory-mirror.card.md § Binding Constraint.
      why: >
        The binding constraint is correctly present and correctly stated. The card
        distinguishes object-level uncertainty (permitted) from meta-level wrong-theory
        acknowledgment before the collision (violation). The structural seam framing
        (collision-not-betrayal) is correctly preserved from world-notes.md. No violation
        found.

    - id: finding-012
      type: pass
      what: >
        Causal chain unambiguity binding rule (world-notes.md § Plot spine, carry-forward:
        "ambient-chaos readings are cost-evasion").
        cond-smallfolk-court-access-mirror.card.md § Access Chain section and auditor-use note.
      why: >
        The access chain card explicitly states: "If any link is missing, the bad act's
        causal responsibility is ambiguous — which is cost-evasion (world-notes.md,
        binding: 'the causal chain from Taylor's kill → wrong-rider outcome must be
        UNAMBIGUOUS in the rendered story')." The eight-step chain from Flea Bottom to
        Dragonpit interior is enumerated. No violation found.

    - id: finding-013
      type: pass
      what: >
        Cost-bearer's death must land cold (world-notes.md § Cost/closing, binding:
        "Death lands cold; the chronicler-frame did the moral work").
        cond-series-tone-mirror.card.md § Prohibited Registers (coda) and § Coda Register.
      why: >
        The card prohibits warmth in the coda and states "The chronicler does not mourn,
        regret, or editorialize sympathetically." The "death lands cold" rule is preserved.
        No violation found.

    - id: finding-014
      type: pass
      what: >
        No parahuman support structure in Westeros (world-notes.md: "no Contessa, Dragon,
        Cauldron, or Worm-context peer who can read what Taylor is").
        cond-shard-deposit-mechanics-mirror.card.md § What Did Not Carry Over and
        § No Other Worm-Universe Entities.
      why: >
        The uniqueness clause is present. Queen Administrator and all other Worm-universe
        powers are listed as absent. The no-parahuman-infrastructure constraint is
        stated. No violation found.

    # ── INTERNAL CONSISTENCY ──────────────────────────────────────────────────

    - id: finding-015
      type: fault
      what: >
        cond-feudal-hierarchy-law.card.md sets the temporal and geographic scope as
        "Riverlands at 84–101 AC (Jaehaerys I)." The card's Hierarchy section describes
        House Ryger of Willow Wood as "the local feudal authority" and populates stages
        of suppression referring to specific Riverlands figures (Tully, Ryger). This
        project is set in King's Landing (~125 AC, Viserys I's declining court, pre-Dance).
        The card's world: planetos and scope: library are correct, but its Description
        scopes it to "Riverlands at 84–101 AC" — a 25+ year period mismatch and a
        geographic mismatch from KL.
        The KL-specific card (cond-kl-feudal-physics-mirror) is correctly scoped to
        ~125 AC King's Landing and explicitly states "This card is the KL-specific layer
        on top of cond-feudal-hierarchy-law." However, the library card's Stage 3/4
        threshold language refers to Tully and Ryger administrative apparatus, which
        does not exist in King's Landing. Auditor-use note in the library card also
        references Taylor's "organizing activities" and "Pryor's assessment" — content
        from the prior Riverlands project that is now misleading for KL deployment.
      why: >
        An impersonator or coach loading cond-feudal-hierarchy-law as context for KL
        scenes will receive feudal-physics guidance for the Riverlands of 84-101 AC,
        not King's Landing of 125 AC. The Stage 3/4 cross-references to Tully and Ryger
        are inoperative in KL. The risk is that agents use the wrong institutional
        framework for enforcement-threat assessments in KL scenes — e.g., writing a
        scene where Taylor fears Tully's administrative apparatus rather than the City
        Watch / Hand's apparatus. The KL card provides the correct override layer, but
        only if agents prioritize the project-scope card over the library card; the
        library card's period/geography mismatch is a drift surface.
      criteria: >
        The Interaction Notes and auditor-use guidance in cond-feudal-hierarchy-law
        must be updated to scope its direct applicability to the Riverlands period and
        to direct KL-project agents explicitly to cond-kl-feudal-physics-mirror as the
        operative card. Alternatively, the loading priority rule for project-scope cards
        over library cards must be stated explicitly in the project-scope KL card.

    - id: finding-016
      type: flag
      what: >
        cond-dance-faction-state-previserys.card.md Dragon-Asset Inventory section lists
        Meleys as "Rhaenys Targaryen, 'the Queen Who Never Was' — a Black-aligned asset
        IF Rhaenys is aligned with the Black faction." The 1c-log names Rhaenys Targaryen
        as the approved patron (false-ally, Black faction). The condition card's hedged
        phrasing ("IF Rhaenys is aligned") introduces uncertainty about a character
        whose factional alignment is now decided.
      why: >
        The conditional phrasing was appropriate when the card was authored (before the
        patron's identity was cast), but after 1c it introduces ambiguity: Rhaenys IS
        the patron AND the patron is Black-faction-adjacent per world-notes.md. An agent
        reading the dragon-asset inventory could treat Rhaenys's Black alignment as
        uncertain when it is decided. Minor drift risk, not a constraint violation —
        the conditional phrasing does not contradict a binding rule, but it could produce
        ambiguous impersonator output for Rhaenys scenes.
      criteria: null

    - id: finding-017
      type: flag
      what: >
        cond-dance-faction-state-previserys.card.md lists Silverwing as a riderless
        dragon at the Dragonpit, described as "Queen Alysanne's former mount; unridden
        since Alysanne's death." The Riderless section also mentions Seasmoke (Laenor
        Velaryon's former mount). The 1c-log confirms Ulf the White as the wrong rider
        who "claims Silverwing in canon Dance — maximal ASOIAF irony." The faction
        card does not name which specific dragon is the opposite-number's target
        (Silverwing is listed but not identified as the pivot dragon in this card).
        cond-dragon-bonding-claiming-rules.card.md § Wrong Rider Claiming Mechanic
        refers to "the opposite-number" and "a dragon" generically.
      why: >
        The pivot dragon (Silverwing, per 1c) is not explicitly named in either
        cond-dance-faction-state-previserys or cond-dragon-bonding-claiming-rules.
        This is an omission, not a contradiction. Both cards describe mechanics that
        apply to the unnamed pivot dragon. The risk is that agents writing the bad
        act or its aftermath do not have a clear authoritative source naming Silverwing
        as the specific dragon involved. The 1c-log is the current authority, but
        it is not a condition card that impersonators and coaches load.
        Flagged (not faulted) because the 1c cast log is definitive; this is a
        cross-card legibility gap, not a constraint violation.
      criteria: null

    - id: finding-018
      type: flag
      what: >
        cond-patron-amplification-theory-mirror.card.md § Patron Uses the Wrong Theory
        states: "The patron arranges consultation sessions at or near the Dragonpit for
        high-stakes questions." cond-smallfolk-court-access-mirror.card.md § Access Chain
        step 5 states "Retainer escort to the Dragonpit exterior approach (first
        dragon-proximity access)" and step 6 states "Dragon-proximity session: patron
        observes Taylor's reaction, interprets as theory confirmation."
        However, cond-smallfolk-court-access-mirror states the patron does not hold
        consultations "at the Red Keep or at any formal court venue" and that the patron
        "reaches down to Taylor's accessible range." These two descriptions are
        consistent — the patron does not bring Taylor to the Red Keep; the patron brings
        Taylor to the Dragonpit under patron escort. No contradiction.
        The flag is for a subtle operational gap: the Dragonpit is not described in
        either card as the patron's primary consultation venue for non-dragon-adjacent
        questions. The patron's standard consultation venues are: "patron's KL premises
        (a townhouse or rented factor space)" and "Sept of Baelor outer courts." The
        Dragonpit sessions are the escalated protocol. This distinction is clear in the
        patron-amplification-theory card but not repeated in the access card, which lists
        the Dragonpit among the patron's accessible venues without flagging that it is
        the high-stakes escalation, not the routine mode.
      why: >
        Minor legibility gap. An agent reading only cond-smallfolk-court-access-mirror
        might treat Dragonpit access as routine rather than escalated-protocol. No
        binding rule is violated since the correct description is present in
        cond-patron-amplification-theory-mirror. Low drift risk.
      criteria: null

    # ── BINDING-FACT COVERAGE CHECK ──────────────────────────────────────────

    - id: finding-019
      type: pass
      what: >
        Binding-fact coverage check: all five binding constraints from world-notes.md
        evaluated for card-set representation.
        (1) Flicker discipline → cond-flicker-discipline-mirror [present, fully covered]
        (2) Two-register architecture → cond-series-tone-mirror [present, fully covered]
        (3) Chronicler counterfactual demand → cond-series-tone-mirror § Coda Register
            [present, fully covered]
        (4) Dragon-claiming canon-adherence → cond-dragon-bonding-claiming-rules
            [present, fully covered]
        (5) Patron's wrong-theory binding constraint → cond-patron-amplification-theory-mirror
            [present, fully covered]
      why: All five binding constraints have dedicated card coverage. No binding fact is uncovered.

    # ── DRIFT RISK ASSESSMENT ────────────────────────────────────────────────

    - id: finding-020
      type: flag
      what: >
        cond-flicker-discipline-mirror.card.md Rule 3 states: "A flicker that confirms
        Taylor's existing beliefs without forcing any reinterpretation or any action-
        commitment under uncertainty is cost-evasion." The positive formulation of the
        cost rule enumerates three forms of interpretive cost: (a) commitment closing
        off alternatives, (b) forced reinterpretation, (c) correct fragment producing
        unanticipated consequence.
        The rule is correctly stated. The drift risk is in the gap between "confirms
        her good intentions" (the world-notes.md phrasing from the 1b carry-forward)
        and the card's general phrasing "confirms Taylor's existing beliefs." An
        impersonator or coach writing a scene where a flicker confirms a tactical
        assessment (not a moral self-justification) might read form (c) of the cost rule
        — "correct but unanticipated consequence" — as sufficient to satisfy the cost
        requirement even if the flicker effectively functioned as a reliable navigation
        tool in that scene.
      why: >
        Form (c) of the cost rule (correct fragment, unanticipated consequence) is the
        loosest of the three forms. A scene where the flicker gives Taylor correct
        information, she acts on it, and a minor unanticipated consequence results
        technically satisfies form (c) while functionally operating as "reliable plot
        device" — which world-notes.md explicitly prohibits ("If it becomes a reliable
        plot device, competence-over-theme concern reactivates" per 1b Batch A literary-
        snob carry-forward). The card's positive formulation does not include the
        literary-snob carry-forward's "reliable plot device" prohibition. The prohibition
        is in the hard-fences section (Rule 7) but Rule 7 as stated addresses "reliable
        information without interpretive cost" and "distinguishing correct from misfire"
        — not "using the flicker as a de facto navigation tool across multiple scenes."
      criteria: null

    - id: finding-021
      type: flag
      what: >
        cond-patron-amplification-theory-mirror.card.md § Binding Constraint states:
        "The patron does not say 'I believe dragon-proximity amplifies your flicker'
        directly; they simply arrange things as if this is true."
        The Interaction Notes with the patron's persona card state: "The patron's voice
        and behavior in scenes must be consistent with the theory being an unexamined
        working assumption, not a stated proposition."
        The Auditor Use note states: "Any scene where the patron explicitly names the
        amplification theory as a belief proposition and affirms it is a mild redundancy
        but not a violation." This is a slight loosening from the binding constraint:
        the binding constraint says the theory is not stated; the auditor note says
        explicit naming is "mild redundancy but not a violation."
      why: >
        The auditor-use note creates a small internal tension: the behavioral rule
        (theory is an unexamined structural assumption, not articulated) and the auditor
        exception (explicit naming-and-affirming is tolerated as "mild redundancy") sit
        slightly in tension. An impersonator writing the patron's dialogue could read the
        auditor note as permission for the patron to articulate the theory explicitly
        during alignment, and justify it via the "mild redundancy" exception. This does
        not violate the binding constraint (which prohibits explicit acknowledgment that
        the theory is WRONG, not articulation that it exists), but it is in tension with
        the behavioral rule that the theory is never stated as a proposition. The
        distinction between "stating the theory" and "questioning the theory" is load-
        bearing for the character's performance, and the current wording could blur it.
      criteria: null

    - id: finding-022
      type: flag
      what: >
        cond-series-tone-mirror.card.md § Prohibited Registers (body) states:
        "Sentimentality: The body's close-third does not dwell in feeling. Emotional
        honesty is present; sentimentality ... is prohibited." The § Tonal Exemptions
        section (Single-Book Scope Implications) states: "minor tonal variance within
        the register ... is permitted as long as the register's core characteristics
        (compression, tactical, not sentimental) are maintained."
        This is not a contradiction — the exemption is for variance within the register
        (quieter scene vs action sequence), not for sentimentality. However, the
        phrasing "minor tonal variance" without a concrete example creates a drift
        surface: an agent authoring a quiet scene (e.g., Taylor with the cost-bearer
        child before the bad act) might read "minor tonal variance" as permission for
        emotional warmth that technically qualifies as sentimentality.
      why: >
        The cost-bearer child (Lyra) scenes are the highest sentimentality-risk scenes
        in the novel. The body register prohibits sentimentality, and world-notes.md
        explicitly prohibits "pathos-scene" rendering of the cost-bearer's death. But the
        approach scenes (Taylor with Lyra before the bad act) are not governed by the
        death-rendering prohibition — only the death itself is specified as "lands cold."
        The approach scenes could drift warm under "minor tonal variance" without a
        specific prohibition. The card does not enumerate the Lyra approach scenes as
        a high-sentimentality-risk context requiring explicit discipline. Low-to-medium
        drift risk.
      criteria: null

    - id: finding-023
      type: flag
      what: >
        cond-flicker-discipline-mirror.card.md Interaction Notes § Close-Third Interiority
        states: "The body text must never give the reader more certainty about the
        flicker's accuracy than Taylor has." This is a correct and important constraint.
        However, no card in the set explicitly addresses the reader-irony mechanic at the
        episode level: the reader with ASOIAF foreknowledge can identify the wrong rider
        from narrative context before Taylor does. The constraint is that Taylor's
        close-third must not tip certainty; it does not prohibit structural clues that
        allow the ASOIAF-literate reader to read ahead of Taylor.
        The concern is not a fault in the flicker-discipline card but in the absence of
        a card that governs the dramatic-irony management at the information-layer level.
        The series-tone card addresses the register but not the dramatic-irony information
        architecture specifically.
      why: >
        The story's irony engine (ASOIAF reader sees the Dance coming, Taylor does not)
        is named in world-notes.md as "the engine of dramatic irony" and the "load-bearing
        mechanism." The condition card set covers tone, flicker, access, and faction physics,
        but does not contain a card governing what structural-dramatic-irony management
        rules apply for the impersonator and coach: how much contextual information about
        faction mechanics is permitted in Taylor's close-third interiority before it
        becomes more-than-Taylor-knows, and how the ASOIAF-literate irony is balanced
        against the Worm-literate reader's perspective. This is a coverage gap at the
        condition-card level, though it may be addressed in the persona card for Taylor.
        Flagged, not faulted, because the existing cards are not wrong — there is no
        card in the set that covers this, which is a gap rather than a contradiction.
      criteria: null

    # ── SUMMARY ──────────────────────────────────────────────────────────────

    - id: finding-024
      type: pass
      what: >
        Internal consistency check — contradiction scan across all 12 cards.
        Specific pairs checked:
        cond-flicker-discipline-mirror vs cond-patron-amplification-theory-mirror
        (Rule 4 vs patron's theory — confirmed consistent: card correctly records theory
        as wrong, flicker card records correct account);
        cond-dragon-bonding-claiming-rules vs cond-dance-faction-state-previserys
        (claiming mechanics vs faction dragon inventory — consistent);
        cond-smallfolk-court-access-mirror vs cond-flea-bottom-social-physics
        (access chain vs district physics — consistent, no overlap violation);
        cond-kl-feudal-physics-mirror vs cond-kl-witch-label-formation
        (institutional architecture vs label escalation — consistent);
        cond-series-tone-mirror vs cond-flicker-discipline-mirror
        (POV constraint vs flicker render rule — consistent, both require close-third
        and both prohibit reader having more certainty than Taylor).
      why: No contradictions found between any pair of cards in the set.
```

---

## Finding Summary

| ID | Type | Domain |
|----|------|--------|
| finding-001 | pass (reclassified) | schema compliance — library scope |
| finding-002 | fault | dangling references: cond-westerosi-customary-authority-jaehaerys, cond-suppression-policy-progression (cond-feudal-hierarchy-law) |
| finding-003 | fault | dangling reference (same card) + named-character contamination from Riverlands prior project (cond-smallfolk-political-physics) |
| finding-004 | fault | references: field misuse — should use supersedes: not references: (cond-kl-witch-label-formation) |
| finding-005 | fault | dangling reference (cond-no-parahuman-infrastructure) + body-text supersession claim without frontmatter structure (cond-shard-deposit-mechanics-mirror) |
| finding-006 | flag | slug variant ambiguity: -125ac vs -jaehaerys, possible dangling reference |
| finding-007 | pass | flicker discipline binding rules — fully covered |
| finding-008 | pass | two-register architecture binding rules — fully covered |
| finding-009 | pass | chronicler counterfactual demand — fully covered |
| finding-010 | pass | dragon-claiming canon-adherence — fully covered |
| finding-011 | pass | patron wrong-theory binding constraint — fully covered |
| finding-012 | pass | causal chain unambiguity — fully covered |
| finding-013 | pass | cost-bearer death rendered cold — fully covered |
| finding-014 | pass | no parahuman support structure — fully covered |
| finding-015 | fault | period and geography mismatch: cond-feudal-hierarchy-law Riverlands 84-101 AC in KL 125 AC project — drift surface in auditor-use guidance |
| finding-016 | flag | Rhaenys Black-faction alignment conditionally hedged in faction card after cast is decided |
| finding-017 | flag | pivot dragon (Silverwing) not named in either dragon-mechanics card; 1c-log is sole authority |
| finding-018 | flag | Dragonpit consultation framed as routine in access card vs escalated-protocol in patron card |
| finding-019 | pass | all five binding constraints have card coverage |
| finding-020 | flag | flicker cost Rule 3 form (c) could be read as permitting de facto reliable-plot-device use |
| finding-021 | flag | patron explicit-naming auditor-exception creates slight tension with behavioral rule |
| finding-022 | flag | "minor tonal variance" exemption in tone card is a sentimentality drift surface for Lyra scenes |
| finding-023 | flag | no card explicitly governs dramatic-irony information architecture (ASOIAF-literate reader vs Taylor's POV) |
| finding-024 | pass | internal consistency — no contradictions found across all 12 cards |

**HARD findings (fault): 5** — findings 002, 003, 004, 005, 015
**SOFT findings (flag): 7** — findings 006, 016, 017, 018, 020, 021, 022, 023
**SIGNAL findings: 0**
**PASS findings: 11**
