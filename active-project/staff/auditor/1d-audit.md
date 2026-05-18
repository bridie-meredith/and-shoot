```yaml
audit:
  scope: series
  target: 1d-constraint-card-set
  timestamp: 2026-05-17
  findings:

    # ── SCHEMA CONFORMANCE ──────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        cond-khepri-residue-122ac frontmatter declares both `scope: library`
        and `project: taylor-hebert-kl-122ac`. Per card schema, `project:` is
        required only when `scope: project`. A library-scoped card must not
        carry a project field — the two fields are mutually exclusive.
      why: >
        If Margit loads this card expecting library scope, the project field
        creates an ambiguous ownership signal. If another project later fetches
        this card as a library resource, the project field implies it is
        project-scoped and may be treated as non-portable. Downstream audits
        that check scope cannot trust the field.
      criteria: >
        Either remove the `project:` field (if this card is genuinely
        library-portable) or change `scope` to `project` and supply the
        correct project slug. Given the card's content is highly
        project-specific (122 AC KL open-state power config), scope: project
        is the accurate declaration.

    - id: fault-002
      type: fault
      what: >
        cond-taylor-pov-behavior, cond-westerosi-witness-vocabulary, and
        cond-maester-chronicler-voice each declare `subclass: behavior` on a
        card with `class: condition`. The schema defines `subclass: behavior`
        as a value only within `class: behavior` cards. No recognized subclass
        values for `class: condition` cards are enumerated in the schema (the
        schema's §Subclass values lists only `agent-persona`). Using `behavior`
        as a condition subclass is a non-schema value.
      why: >
        Margit's validation will either reject these cards or silently drop
        the subclass field. Downstream agents loading on `subclass: behavior`
        will miss these cards or mismatch them. The three cards cover
        load-bearing authoring constraints (POV register, witness vocabulary,
        coda structure); a Margit fetch failure or silent mismatch on any of
        them is a production risk.
      criteria: >
        Remove the `subclass:` field from all three cards, or replace it with
        a value that is valid for `class: condition`. If the intent was to
        signal that these cards govern authoring behavior rather than
        environmental state, that distinction should be documented in the
        Description body section, not in the subclass field.

    - id: fault-003
      type: fault
      what: >
        cond-fauna-control-rules and cond-shard-behavioral-weight have no
        `subclass:` field. Per schema, subclass is optional for condition
        cards, so absence is not a schema violation. However, cond-shard-
        behavioral-weight declares `references: [taylor-hebert-flea-bottom,
        cond-no-parahuman-infrastructure, cond-series-tone-constraints-125ac]`.
        Two of these references — `taylor-hebert-flea-bottom` and
        `cond-series-tone-constraints-125ac` — are cards from the prior
        `mirror-tragedy` project. Neither exists in the current project's
        card set or confirmed library. A card with dead references cannot be
        fully resolved at load time.
      why: >
        `cond-shard-behavioral-weight` is a required load for any scene
        involving Taylor's internal decision-making (its own auditor-use
        section states this; cond-taylor-pov-behavior references it). If the
        reference chain is broken, an agent loading this card for a
        scene-level constraint check receives partial context. The
        `cond-series-tone-constraints-125ac` reference is particularly
        significant — the Interaction Notes section treats that card as
        additive to this card's escalation rule, meaning the current project
        has a documented dependency on a card that does not exist in its
        constraint set.
      criteria: >
        Verify whether `taylor-hebert-flea-bottom` and
        `cond-series-tone-constraints-125ac` exist in the current project's
        library. If they do not, either: (a) remove the dead references and
        inline the relevant constraints, or (b) author replacement cards
        scoped to this project. The escalation-rule dependency on
        `cond-series-tone-constraints-125ac` must be resolved before
        /and-series, since it is cited as additive to this card's core mechanic.

    # ── CROSS-CARD CONSISTENCY ──────────────────────────────────────────────

    - id: fault-004
      type: fault
      what: >
        cond-dance-faction-state-previserys has `scope: project` with
        `project: mirror-tragedy`. It is being reused in this project (listed
        as a reused card), but its scope field declares it as owned by a
        different project. The card's body references four
        mirror-tragedy-specific condition cards that do not exist in this
        project: `cond-flicker-discipline-mirror`,
        `cond-patron-amplification-theory-mirror`, `cond-dragon-bonding-
        claiming-rules`, and `cond-flea-bottom-social-physics`. The
        Interaction Notes sections point auditors and impersonators to these
        cards for constraint resolution that cannot be completed.
      why: >
        Agents loading cond-dance-faction-state-previserys for this project
        will follow the Interaction Notes to cards that do not exist. The
        "opposite-number" mechanics in the body section (the invented OC
        Rhaenyra-adjacent rider claiming a contested dragon) are defined in
        terms of mirror-tragedy project mechanics. In this project, the
        opposite-number is Aemond Targaryen (from world-notes.md) — not an
        invented OC. The card's body-level description of the opposite-number
        role is a factual mismatch with this project's 1b resolutions.
      criteria: >
        Either (a) author a project-scoped override card
        (`cond-dance-faction-state-122ac`, scope: project, project:
        taylor-hebert-kl-122ac, overrides: cond-dance-faction-state-previserys)
        that replaces the mirror-tragedy-specific body sections with this
        project's opposite-number (Aemond) and removes references to
        mirror-tragedy cards, or (b) retire the reuse decision and author
        a fresh lore card scoped to this project. The 122 AC faction-state
        information in cond-kl-court-state-122ac already covers the essential
        political ambient; the override card's delta is the opposite-number
        mechanics and the strategic dragon-asset inventory.

    - id: fault-005
      type: fault
      what: >
        cond-kl-witch-label-formation has `scope: project` with
        `project: mirror-tragedy` and references five mirror-tragedy-specific
        cards: `cond-crownlands-superstition-frame-125ac`,
        `cond-flea-bottom-social-physics`, `cond-kl-feudal-physics-mirror`,
        `cond-patron-amplification-theory-mirror`, and
        `cond-flicker-discipline-mirror`. None of these exist in the current
        project. The body of this card is also built around a "flicker"
        mechanic (the involuntary behavioral expression of near-future
        foreknowledge), which is a mirror-tragedy power-config that differs
        from this project's power-config: in this project, Taylor's capability
        is insect-control and pattern-recognition precog (not foreknowledge
        expressed as behavioral flicker). The card's witch-label-formation
        mechanism (behavioral-pattern-not-event-trigger) is not wrong for this
        project, but its stated trigger is the wrong capability.
      why: >
        If this card is loaded for constraint review in this project, the
        trigger mechanism (flicker as involuntary foreknowledge-expression) is
        incorrect — it imports a power-config that is explicitly sealed in
        this project. Writers authoring the witch-label formation arc would
        follow a trigger that does not apply here, producing label-formation
        scenes built around a power this project's Taylor does not have.
        The five dead references create the same resolution-failure risk as
        fault-004.
      criteria: >
        Do not load cond-kl-witch-label-formation for this project without
        a project-scoped override. Author a replacement or override card that:
        (a) describes witch-label formation triggered by insect-network
        behavioral anomalies (flies moving wrong, animal massing, the Watch's
        observation of animal-uncanny behavior near Taylor) rather than
        flicker-behavior, (b) references only cards that exist in this
        project, and (c) is scoped to this project. The KL institutional
        escalation mechanics (Watch → noble quarter → Hightower network) in
        the existing card body are valid for this project and can be carried
        forward.

    - id: flag-001
      type: flag
      what: >
        cond-westerosi-superstition-frame has scope: library but its body is
        explicitly scoped to "Riverlands, 84–101 AC." Its description says
        "How Westerosi culture categorizes uncanny events in the Riverlands at
        84–101 AC." Its references include `cond-riverlands-84ac-state` and
        `cond-faith-of-seven-jaehaerys` — cards from a prior Riverlands
        project. The specific witness vocabulary (the Ashford child, Septon
        Rowan, the ignition event at the market square ~86 AC) is entirely
        Riverlands-project-specific.
      why: >
        This card is listed as a reuse but its body provides Riverlands-84AC
        witness vocabulary samples that are not applicable to 122 AC KL.
        Agents loading it for this project will encounter reference to
        specific prior-project events and characters as if they are generic
        Westerosi superstition. cond-westerosi-witness-vocabulary (a new card)
        provides KL-122AC-specific vocabulary organized by class, which is
        the correct load for this project. If both cards are loaded together,
        agents may draw from the Riverlands card's character-specific examples
        as if they are KL-generic. No hard conflict exists, but the card is
        misleadingly generic for what is a period-and-region-specific card.
      # No criteria field: flag only

    - id: flag-002
      type: flag
      what: >
        Khepri-residue power-state across three cards. cond-khepri-residue-
        122ac says the pattern-recognition precog "surfaces as ordinary
        cognition" and Taylor "cannot distinguish it from ordinary analytical
        skill." cond-shard-behavioral-weight says the Shard is "active at
        behavioral-weight level" and creates a "persistent bias in Taylor's
        judgment." cond-taylor-pov-behavior's moral-accounting section says
        the ledger is "rigorous within its frame; the frame is wrong." These
        are complementary and consistent. However, cond-shard-behavioral-weight
        was authored for a different power-config (mirror-tragedy, where
        a "flicker" mechanic was active). The card's scene-level guidance
        for impersonators references "coalition-building" and "OQ-9/C"
        which are mirror-tragedy arc structures, not this project's single-
        book arc. The scene-level guidance is therefore calibrated to a
        multi-episode series, not a single-book story.
      why: >
        Impersonators loading cond-shard-behavioral-weight for this project
        will receive coalition-arc and multi-episode framing that does not
        match the structural reality (one book, 18–24 chapters, no season-
        arc). The escalation-weight heuristics in the Mechanics section are
        generic enough to be valid; the arc-level framing in the Pressure-
        Multiplier Effect section is not. This is advisory — no hard conflict
        with this project's constraints — but an impersonator following the
        arc framing literally could generate misaligned decision-beats.
      # No criteria field: flag only

    - id: flag-003
      type: flag
      what: >
        cond-kl-court-state-122ac states Daemon Targaryen is "In Pentos at
        122 AC (canonical F&B)." cond-dance-faction-state-previserys (reused,
        ~125 AC) describes Daemon as "Rhaenyra's husband by this period."
        The 125 AC version's faction description includes Daemon as an active
        Black faction asset ("volatile; a dragon-rider; a destabilizing force").
        The 122 AC card correctly notes Daemon's absence; the 125 AC card
        correctly reflects his return. The explicit interaction note in
        cond-kl-court-state-122ac ("do not import 125 AC specifics into 122 AC
        scenes") addresses this.
      why: >
        The divergence is intentional and documented, not a conflict. However,
        given that cond-dance-faction-state-previserys is a project-scoped
        card from mirror-tragedy (see fault-004), it should not be the
        production load for faction state in this project regardless. This flag
        is advisory: if the card is replaced per fault-004's criteria, the
        Daemon-timing divergence resolves naturally.
      # No criteria field: flag only

    # ── COVERAGE GAPS ────────────────────────────────────────────────────────

    - id: fault-006
      type: fault
      what: >
        No card in the set binds the cost-bearer behavior rule. The 1b
        resolution states: "Nessa — at least one scene per act. Closing-image
        cost is her death." No condition card enforces this structural
        requirement. The cond-maester-chronicler-voice card requires Nessa's
        death be recorded in the coda, but nothing binds the act-level
        appearance rule or the closing-image shape. cond-taylor-pov-behavior's
        moral-accounting section mentions "the one item she does not put in
        the ledger" implying Nessa as accounting-anomaly, but does not declare
        the structural frequency rule.
      why: >
        Without a card binding Nessa's scene-frequency rule, the substance
        pipeline has no constraint-checkable anchor for the cost-bearer's
        presence. An /and-substance chapter pass or /and-write bone-gate has
        no card to cite when checking whether an act has Nessa coverage. The
        1b resolution's structural rule ("at least one scene per act") is
        load-bearing for the road-to-hell chain — without visible accumulation
        of Taylor's relationship with Nessa across acts, the closing-image cost
        has no earned weight. This gap will not surface until /and-substance
        book, at which point fixing it requires retroactive restructuring.
      criteria: >
        Author a condition card (suggested slug: cond-nessa-cost-bearer-rule,
        subclass omitted, scope: project) that declares: (a) Nessa's identity
        and 122 AC age (approximately 8, Flea Bottom Hook resident from scene
        one), (b) the frequency rule (at least one scene per act in which
        Taylor and Nessa share screen time — not off-stage mentions), (c) the
        closing-image requirement (Nessa's death in Flea Bottom violence of
        the Dance opening is the final cost image), and (d) the ledger-anomaly
        rule (Nessa is the one item Taylor does not enumerate in her moral
        accounting — any scene where Taylor explicitly cost-accounts Nessa is
        a violation). Register to library index at creation.

    - id: fault-007
      type: fault
      what: >
        No card binds the four-beat road-to-hell chain shape. The 1b
        resolution establishes: (1) good intention (prevent Lucerys's death),
        (2) first trade as auditable mistake (Taylor becomes Otto's intelligence
        asset), (3) end-place locus (both — Taylor dead/expelled, Dance
        ignites, Nessa dies). The thematic spine requires each load-bearing
        choice to be "readable backward from the end-revelation to the prior
        choice's auditable mistake." No card establishes: the number of
        beats, what constitutes an auditable mistake, the retroactive-
        revelation rule, or the chain-coherence requirement (that each bad
        act must be traceable to the prior good-intention beat). The
        cond-maester-chronicler-voice card requires the coda to name "the
        explicit counterfactual" but does not define the chain that precedes
        it.
      why: >
        Without a card binding the road-to-hell chain structure, there is no
        constraint-checkable definition of what makes a choice "load-bearing"
        versus merely plot-advancing. The substance pipeline's dramatic-shape
        checks (at /and-substance chapter level) will have no structural rule
        to cite when evaluating whether a scene's bone-level decisions are
        contributing to the chain. The /and-review verdict pass will have no
        criterion for chain-coherence. The absence of this card means the
        road-to-hell thematic requirement is advisory rather than enforceable
        through the audit pipeline.
      criteria: >
        Author a condition card (suggested slug: cond-road-to-hell-chain-rule,
        scope: project) that declares: (a) the chain structure (the story
        requires a minimum of three auditable-mistake beats between the
        inciting good intention and the closing-image cost; each beat must be
        causal — the next beat's bad act follows from the prior beat's choice,
        not from external fate), (b) the auditable-mistake definition (a choice
        Taylor makes that is, at the time, the cold-utilitarian-correct
        decision given her information and that is, in retrospect, identifiable
        as the step that narrowed the exit), (c) the retroactive-revelation
        requirement (the chain must be fully reconstructible backward from the
        closing image by a reader; no beat in the chain may be legible only
        forward), and (d) the prohibition on authorial correction (the prose
        does not signal which choices are mistakes at the time of making them).

    # ── DUPLICATE / NEAR-DUPLICATE CHECK ────────────────────────────────────

    - id: flag-004
      type: flag
      what: >
        cond-kl-social-physics-122ac and the reused cond-smallfolk-political-
        physics and cond-feudal-hierarchy-law and cond-westerosi-customary-
        authority together cover overlapping territory. cond-kl-social-physics-
        122ac explicitly describes itself as "the KL-specific version of the
        existing Riverlands-calibrated social physics cards." The new card adds
        genuine KL-specific content (Watch structure, Hightower network,
        currency-as-social-indicator). No duplicate fault: the new card's
        Interaction Notes correctly cite the reused cards as prior-layer and
        the new card adds 122AC-KL-specific delta. However, cond-kl-social-
        physics-122ac references `cond-westerosi-customary-authority` in its
        Interaction Notes but that card does not appear in its frontmatter
        `references:` list. The body cites it; the frontmatter does not
        declare it.
      why: >
        A Margit reference resolution that walks only frontmatter `references:`
        fields will not follow the dependency to cond-westerosi-customary-
        authority when loading cond-kl-social-physics-122ac. The body reference
        is effectively invisible to automated resolution.
      # No criteria field: flag only — fixer may add the reference to frontmatter

    - id: flag-005
      type: flag
      what: >
        cond-westerosi-witness-vocabulary references `cond-kl-witch-label-
        formation` in its frontmatter. As established in fault-005,
        cond-kl-witch-label-formation is a mirror-tragedy project card with
        a mismatch trigger mechanism for this project. Loading
        cond-westerosi-witness-vocabulary will follow its reference chain to
        a card that should not be production-loaded unmodified for this project.
      why: >
        If fault-005 is resolved (an override or replacement card is authored),
        this reference should be updated to point to the new card slug. If
        fault-005 is not resolved before /and-series, any constraint check
        that loads cond-westerosi-witness-vocabulary and follows its references
        will reach the incorrect trigger-mechanism card.
      # No criteria field: flag only — resolves when fault-005 is fixed

    # ── PLAN QUALITY / PROCESS SIGNAL ───────────────────────────────────────

    - id: flag-006
      type: flag
      what: >
        cond-kl-geography-122ac has a factual note that may require
        monitoring: the body states the Great Sept "is not yet called 'of
        Baelor' in 122 AC — Baelor I reigns 170s AC; in 122 AC it is the
        Grand Sept of King's Landing." This is a correct F&B-sourced
        distinction. However, the world-notes.md and prompt-binding.md both
        use "Great Sept of Baelor" as the reference name (world-notes.md:
        "Great Sept of Baelor — Faith seat"). If writers draw from world-notes
        rather than the condition card, scenes may use the anachronistic name.
      why: >
        Not a cross-card conflict — the condition card's correction is right
        and world-notes is technically inaccurate for 122 AC. In practice,
        most readers including the target audience will recognize "Great Sept
        of Baelor" as the standard KL reference even for pre-Baelor periods
        (HOTD uses it without correction). Whether to enforce the historically
        accurate 122 AC name or permit the anachronistic convention is a
        production decision. No constraint violation until a scene uses the
        wrong name and the auditor is asked to check it. Advisory carry-forward.
      # No criteria field: flag only
```

OVERALL: FAULT-7
