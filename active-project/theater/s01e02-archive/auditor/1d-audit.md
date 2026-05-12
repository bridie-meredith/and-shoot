```yaml
audit:
  scope: series
  target: flea-bottom-dance — 1d constraint card set
  timestamp: 2026-05-10
  findings:

    - id: fault-001
      type: fault
      what: >
        cond-shard-behavioral-weight frontmatter — references field lists
        taylor-hebert-jaehaerys (prior project persona slug) instead of
        taylor-hebert-flea-bottom. The card body also names taylor-hebert-jaehaerys
        in its Interaction Notes section ("With taylor-hebert-jaehaerys persona card").
      why: >
        Margit loads the references field to resolve card dependencies. An auditor
        or dialogue-writer loading this card via the reference chain will follow the
        slug to a prior-project persona card rather than the active one. The body
        Interaction Notes compounds this by telling readers to load the wrong card.
        Any constraint check that follows the reference to verify persona Hard Fences
        will reach the wrong source. This is the specific gap the dispatch task flagged.
      criteria: >
        The references field of cond-shard-behavioral-weight must include
        taylor-hebert-flea-bottom, not taylor-hebert-jaehaerys. The body's
        Interaction Notes section must cite taylor-hebert-flea-bottom in place of
        taylor-hebert-jaehaerys.

    - id: fault-002
      type: fault
      what: >
        cond-shard-behavioral-weight frontmatter — references field lists
        cond-series-tone-constraints-84ac (84 AC Jaehaerys I config tone law) not
        cond-series-tone-constraints-125ac (this project's tone law). The card body's
        Interaction Notes section repeats the wrong slug: "With
        cond-series-tone-constraints-84ac: The escalation rule in the tone card and
        the Shard's behavioral weight are additive." The for-auditor-use section also
        cites cond-series-tone-constraints-84ac as the violation destination.
      why: >
        The 84ac tone card is the fast-pulpy-dramatic config explicitly designated as
        NOT this project's register by cond-series-tone-constraints-125ac. An auditor
        loading cond-shard-behavioral-weight and following its cross-reference loads the
        wrong tone law. Any scene-level escalation-reflex check that uses the 84ac tone
        card as the additive partner will be evaluating against a register this project
        is specifically not running in. All fault-routing from this card for register
        violations is misdirected.
      criteria: >
        The references field of cond-shard-behavioral-weight must include
        cond-series-tone-constraints-125ac in place of (or in addition to, if the 84ac
        card is a genuine dependency for other reasons) cond-series-tone-constraints-84ac.
        The Interaction Notes section and for-auditor-use section must cite the 125ac
        card as the active tone law for this project.

    - id: fault-003
      type: fault
      what: >
        cond-crownlands-superstition-frame-125ac frontmatter — scope is set to
        "library" with variant-project: flea-bottom-dance. The card body is deeply
        project-specific: it names Taylor, the Tya-situation, the tanner-family, the
        Flea Bottom community, and the specific 125 AC arrival config. The card's
        Interaction Notes reference flea-bottom-dance conditions directly. The schema
        defines scope:library as "canonical card available across all projects."
      why: >
        A scope:library card is loaded without project filtering by margit and any
        downstream agent. A card with project-specific content (the Tya-situation, the
        tanner-family's specific grief-interrupted dynamics, Flea Bottom register at
        this config) being in library scope creates two downstream risks: (1) it will
        be available to future projects where the 125 AC Tya config does not apply, and
        (2) its project-specific auditor-use section will be authoritative for contexts
        that don't share this project's cast. The variant-project field exists precisely
        to document project origin; the scope should match.
      criteria: >
        scope must be changed to "project" and project: flea-bottom-dance added to the
        frontmatter of cond-crownlands-superstition-frame-125ac. The library index entry
        should be updated accordingly (scope:library bucket → project:flea-bottom-dance
        bucket).

    - id: fault-004
      type: fault
      what: >
        cond-clinical-self-erasure frontmatter — scope is set to "library" with no
        project field. The card body is entirely project-specific: it describes s1-s4
        of flea-bottom-dance by name, names the broken maester, the Fish Gate margin
        subject, the density-saturation failure event, and Taylor's specific log
        practice. Its executable form notes are written as instructions for flea-bottom-dance
        prose writers and auditors only.
      why: >
        Same structural problem as fault-003. scope:library makes this card available
        as a canonical cross-project card. Its content is not transferable — a future
        project with Taylor in Westeros will not necessarily have the same s1–s3 clinical
        drift arc, the same subjects, or the same foreclosure shape. Worse, the
        executable form notes in this card (what prose MUST and MUST NOT show) are
        load-bearing auditor gates for this project specifically. If a future project
        loads this card and misapplies its "must" rules, it will produce false violations.
      criteria: >
        scope must be changed to "project" and project: flea-bottom-dance added to the
        frontmatter of cond-clinical-self-erasure. The library index should reflect
        the corrected scope.

    - id: fault-005
      type: fault
      what: >
        cond-reincarnation-mechanics-125ac body states: "This card supersedes and
        replaces cond-reincarnation-mechanics (taylor-hebert-westeros) for this project.
        The 120 AC / septon-ward / Harrenhal-adjacent config is the wrong config."
        The frontmatter carries no supersedes: field. The prior card slug is given in
        parenthetical prose only.
      why: >
        The schema's supersede chain mechanism (old card sets superseded_by, new card
        sets supersedes) is what allows margit to auto-follow to the correct card on
        fetch. Without supersedes: in this card's frontmatter, any fetch of the prior
        config card will not automatically redirect. An agent loading the wrong config
        card will not be warned that a replacement exists. If the prior card
        (cond-reincarnation-mechanics at the 120 AC config, or whichever slug applies)
        also lacks superseded_by pointing here, the chain is broken in both directions.
      criteria: >
        The frontmatter of cond-reincarnation-mechanics-125ac must include
        supersedes: [<prior-slug>] where <prior-slug> is the slug of the card this
        replaces for this project. The prior card must be updated with
        superseded_by: cond-reincarnation-mechanics-125ac. If the prior card is
        cond-reincarnation-mechanics (general) rather than a project-scope card,
        fixer should determine whether overrides: rather than supersedes: is the
        correct relation and use the appropriate frontmatter field.

    - id: flag-001
      type: flag
      what: >
        The world-notes LAW (OQ-3): "Hypothesis-falsification structure governs the
        arcane research arc. Each major capability extension follows: theory → test →
        partial/full falsification → revised theory. 'She tested it and it worked' is
        a violation." This specific discipline — the requirement that every capability
        extension follow the falsification arc, not just the s4 experiment — is not
        explicitly articulated as an auditable constraint in any condition card.
        cond-fauna-control-rules-125ac-addendum covers the s4 falsification event and
        names the working hypothesis. cond-clinical-self-erasure covers the hypothesis
        chain's appearance in prose. Neither card states the general rule: any scene
        in which a capability extension succeeds without a prior falsification step is
        a violation.
      why: >
        Without an explicit card-level constraint statement of the hypothesis-falsification
        discipline, auditors reviewing individual scenes have no card to cite when a
        capability extension arrives cleanly. The world-notes source is available for
        reference but is not in the load set for scene-level review (auditors load
        cards, not world-notes at scene level). The gap is particularly live for s1
        and s2 capability extensions (before the s4 event) where the falsification
        discipline should be enforced but the only card coverage is the s4-specific text.
        This is advisory; fixer may choose to add a single constraint sentence to
        cond-fauna-control-rules-125ac-addendum's auditor-use section to close it.

    - id: flag-002
      type: flag
      what: >
        cond-smallfolk-political-physics scope is "library" with body text scoped to
        "Riverlands, 84–101 AC" (Jaehaerys I config). The card names prior-project
        characters (Mira Stonefield-Jaehaerys, Septon Rowan, Aldric Pryor, Clem Ferris,
        the Fairstead market town). The flea-bottom-dance project is 125 AC,
        Crownlands/KL, Flea Bottom. This card is referenced by
        cond-crownlands-superstition-frame-125ac (its Interaction Notes cite
        cond-smallfolk-political-physics) and is a functional dependency for modeling
        Flea Bottom community dynamics.
      why: >
        The card's content (learned invisibility, informal credit, whisper networks,
        reeve-as-membrane, septon's charity node, community-legitimacy problem) is
        substantively applicable to Flea Bottom with adaptation. However its named
        figures, geographic references, and period label are wrong-config. Any agent
        loading the card to model Flea Bottom smallfolk will encounter Riverlands-84ac
        character names as examples and may import wrong-cast context. The card should
        either have a Crownlands-125ac addendum (parallel to what was done for the
        superstition frame) or the Flea Bottom cast should be explicitly named in
        project-scope notes. This is a flag not a fault because the underlying
        mechanics transfer; the named examples do not.

    - id: flag-003
      type: flag
      what: >
        cond-crownlands-superstition-frame-125ac references field includes
        cond-fauna-control-rules (base card, 200m config) but not
        cond-fauna-control-rules-125ac-addendum (this project's overriding config).
        The base card and addendum carry different range numbers and different
        wrongness-perception context.
      why: >
        If an agent loads the superstition frame card and follows its references to
        understand the fauna-control mechanics that produce the wrongness-perception
        events this card narrates, they will reach the base card (200m, no Khepri-mantle
        content, no glass-candle relay) rather than the project-specific addendum.
        The superstition frame card's Interaction Notes (second block: "With
        cond-reincarnation-mechanics-125ac") correctly cite the project-specific card;
        the fauna-control reference is not similarly updated. Advisory for fixer to
        add cond-fauna-control-rules-125ac-addendum to the references field.

    - id: pass-001
      type: pass
      what: >
        Coverage of all named OQ-2 LAWs (range/ceiling/Khepri-sealed/glass-candle-relay)
        in condition cards.
      why: >
        cond-fauna-control-rules-125ac-addendum carries all six OQ-2 LAWs explicitly
        and adds auditor-use enforcement guidance for each. No gap found.

    - id: pass-002
      type: pass
      what: >
        Coverage of OQ-3 s4 foreclosure event and insect-network/candle theory
        carry-forwards.
      why: >
        cond-fauna-control-rules-125ac-addendum (mechanism section and glass-candle
        relay section) and cond-clinical-self-erasure (executable form notes items 2
        and 4) jointly carry the foreclosure event and the pre-s4 hypothesis-visibility
        requirement. No gap found.

    - id: pass-003
      type: pass
      what: >
        Coverage of OQ-8 demonstration-Khepri-register rule and Khepri-unlock
        sequencing carry-forward.
      why: >
        cond-series-tone-constraints-125ac covers both: the Demonstration Rule section
        requires Khepri-register and names the violation; the Khepri-Unlock Sequencing
        Rule section specifies visible causal ordering and names the structural violation
        if collapsed. cond-fauna-control-rules-125ac-addendum (Override 2) reinforces
        the sequencing. No gap found.

    - id: pass-004
      type: pass
      what: >
        Clinical-register self-erasure carry-forward coverage.
      why: >
        Dedicated card cond-clinical-self-erasure carries all eight 1b carry-forward
        execution watches for this arc: named-subject density gradient, hypothesis chain
        visible in prose, at least one s1 maester-responsiveness scene, Fish Gate subject
        in surveillance and not in log, physiological data present in early records and
        absent later, no meta-awareness, no single-decision erasure scene, no redemptive
        notation. All are explicitly stated. No gap found.

    - id: pass-005
      type: pass
      what: >
        S2 Khepri-cause visible in s02 prose carry-forward coverage.
      why: >
        cond-series-tone-constraints-125ac (Khepri-Unlock Sequencing Rule, final
        paragraph) and cond-fauna-control-rules-125ac-addendum (Override 2, "Visible
        sequencing" section) both state this requirement explicitly as an auditable
        on-page requirement, not plan-level. No gap found.

    - id: pass-006
      type: pass
      what: >
        No contradictory range specifications across the card set.
      why: >
        cond-fauna-control-rules (base) specifies 200m normal / 400m extended.
        cond-fauna-control-rules-125ac-addendum explicitly states it overrides these
        figures with 300m normal / ~500-600m extended / 1.5km ceiling. The override
        mechanism is stated explicitly in the addendum's opening. No implicit conflict;
        the override is clean.

    - id: pass-007
      type: pass
      what: >
        No contradictory Khepri-mantle rules across the card set.
      why: >
        cond-fauna-control-rules (base) does not mention Khepri-mantle. The addendum
        introduces it and is the sole governing card for Khepri-mantle mechanics. No
        conflict.

    - id: pass-008
      type: pass
      what: >
        cond-reincarnation-mechanics-125ac and cond-clinical-self-erasure
        non-contradiction check.
      why: >
        Reincarnation card specifies Taylor's episodic memory is intact (does not
        degrade). Clinical-self-erasure card specifies Taylor's research record
        deteriorates. The clinical-self-erasure card's Interaction Notes explicitly
        addresses this apparent tension ("Taylor remembers everything she observed;
        she records decreasing amounts of what she observed") and resolves it correctly.
        No contradiction.

    - id: pass-009
      type: pass
      what: >
        Uniqueness constraint (one displaced soul) coverage.
      why: >
        cond-reincarnation-mechanics-125ac contains explicit "Uniqueness" section:
        "Taylor is the only displaced soul in this project. No other reincarnated
        Earth-Bet parahumans, no other isekai arrivals... This constraint is absolute
        for the series duration." cond-no-parahuman-infrastructure reinforces from
        the infrastructure side. No gap.

    - id: pass-010
      type: pass
      what: >
        cond-fauna-control-rules-125ac-addendum schema compliance check.
      why: >
        Frontmatter complete: name, class, scope, project, world, origin, quality,
        variant-of, variant-reason, references. All required fields for a project-scope
        variant card present. Parent card cited correctly in both variant-of and
        references. PASS.

    - id: pass-011
      type: pass
      what: >
        cond-series-tone-constraints-125ac schema compliance check.
      why: >
        Frontmatter complete: name, class, scope, project, world, origin, quality,
        variant-of, variant-reason, references. All required fields present. Parent
        card cited in variant-of. References field contains the relevant project cards
        (taylor-hebert-flea-bottom, cond-shard-behavioral-weight, cond-clinical-self-erasure).
        PASS.

    - id: pass-012
      type: pass
      what: >
        cond-reincarnation-mechanics-125ac schema compliance check (frontmatter fields
        excluding the supersedes gap noted in fault-005).
      why: >
        name, class, scope, project, world, origin, quality, references all present.
        references includes all four load-dependencies correctly (taylor-hebert-flea-bottom,
        cond-no-parahuman-infrastructure, cond-fauna-control-rules-125ac-addendum,
        cond-crownlands-superstition-frame-125ac). The only gap is the missing supersedes
        field, classified separately as fault-005.
```
