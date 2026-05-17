```yaml
audit:
  scope: series
  target: flea-bottom-dance — series-level human-checkpoint audit
  timestamp: 2026-05-10
  findings:

    # -----------------------------------------------------------------------
    # FIXER RESIDUALS — fault-001 through fault-005 from 1d-audit.md
    # -----------------------------------------------------------------------

    - id: res-001
      type: pass
      what: >
        fault-001 (1d): cond-shard-behavioral-weight references field and
        Interaction Notes — taylor-hebert-jaehaerys slug.
      why: >
        FIXED. References field now lists taylor-hebert-flea-bottom. Interaction
        Notes body ("With taylor-hebert-flea-bottom persona card") cites the
        correct slug throughout. No residue of the prior jaehaerys slug found.

    - id: res-002
      type: pass
      what: >
        fault-002 (1d): cond-shard-behavioral-weight references field and
        Interaction Notes — cond-series-tone-constraints-84ac slug.
      why: >
        FIXED. References field lists cond-series-tone-constraints-125ac.
        Interaction Notes reads "With cond-series-tone-constraints-125ac."
        For-auditor-use section cites the 125ac card. No residue of the 84ac
        slug found.

    - id: res-003
      type: fault
      what: >
        fault-003 (1d): cond-crownlands-superstition-frame-125ac frontmatter
        scope field. Current value: scope: library. Required value: scope:
        project. The card body remains deeply project-specific (names Taylor,
        the Tya-situation, the tanner-family, Flea Bottom community, 125 AC
        arrival config). The variant-project: flea-bottom-dance field is
        present but scope: library overrides it for margit load logic.
      why: >
        A scope:library card is fetched without project filtering. The
        project-specific auditor-use rules in this card will be treated as
        canonical constraints in any future project that loads it. Downstream
        risk: a future 125 AC project with a different protagonist or a
        different community structure will load a card whose for-auditor-use
        section names Taylor's tanner-family situation as the violation target.
        Margit's library index also needs a corresponding scope correction.
        fault-003 from the 1d audit is not resolved.
      criteria: >
        scope must be changed to "project" and project: flea-bottom-dance
        confirmed in the frontmatter of cond-crownlands-superstition-frame-125ac.
        The library index entry for this card must be moved from the
        scope:library bucket to a project:flea-bottom-dance bucket or annotated
        as project-scope. The variant-project field alone is not sufficient.

    - id: res-004
      type: fault
      what: >
        fault-004 (1d): cond-clinical-self-erasure frontmatter scope field.
        Current value: scope: library. Required value: scope: project. The
        card body is entirely project-specific: it names s1–s4 of
        flea-bottom-dance by structural reference, names the broken maester,
        the Fish Gate margin surviving subject, the density-saturation failure
        event, and Taylor's specific log practice. Its executable form notes
        are written as binding instructions for flea-bottom-dance prose writers
        and auditors only.
      why: >
        Same structural risk as res-003: a future project loading this card
        will receive binding MUST and MUST NOT instructions calibrated to
        flea-bottom-dance's four-season arc. The instruction "subjects must
        still be named in s1 records and not named by s3" is only meaningful
        if s1–s3 are the flea-bottom-dance research arc. A project with a
        different arc length or different clinical-register mechanism will
        produce false violations if it loads this card as a library-scope
        canonical constraint. fault-004 from the 1d audit is not resolved.
      criteria: >
        scope must be changed to "project" and project: flea-bottom-dance
        confirmed in the frontmatter of cond-clinical-self-erasure. Library
        index must reflect the corrected scope.

    - id: res-005
      type: fault
      what: >
        fault-005 (1d): cond-reincarnation-mechanics-125ac missing supersedes
        field. The card body states it supersedes cond-reincarnation-mechanics
        (taylor-hebert-westeros). The frontmatter has no supersedes: field.
        Checked current card: references field contains
        cond-fauna-control-rules-125ac-addendum and cond-crownlands-superstition-frame-125ac
        but no supersedes: entry.
      why: >
        The schema supersede chain mechanism requires the new card to declare
        supersedes: and the prior card to declare superseded_by:. Without this,
        margit and any loading agent following the reference chain from the
        prior config card will not be redirected. The prior card
        (cond-reincarnation-mechanics scoped to taylor-hebert-westeros) is also
        not confirmed to carry superseded_by: pointing here. The chain is broken
        in both directions at schema level. fault-005 from the 1d audit is not
        resolved.
      criteria: >
        cond-reincarnation-mechanics-125ac frontmatter must include
        supersedes: [cond-reincarnation-mechanics] (or the exact slug of the
        prior project-scope card). The prior card must be updated with
        superseded_by: cond-reincarnation-mechanics-125ac. If the relationship
        is an override rather than a supersede (both cards remain valid for
        their respective project configs), fixer determines which schema
        relation is correct and applies the appropriate field to both cards.

    # -----------------------------------------------------------------------
    # NEW — CONSISTENCY
    # -----------------------------------------------------------------------

    - id: fault-006
      type: fault
      what: >
        cond-shard-behavioral-weight H1 heading reads: "Shard Behavioral
        Weight — Taylor Hebert in Westeros (Jaehaerys I Config)". The
        Jaehaerys I Config label in the document heading is residue from the
        prior project. The card body and frontmatter are correctly updated
        (references and Interaction Notes both cite flea-bottom-dance
        resources), but the heading advertises the wrong project config to
        any agent reading the card.
      why: >
        Agents loading the card who read only the heading and the body's first
        paragraph will see "Jaehaerys I Config" and may cross-check against
        the wrong persona card or the wrong set of constraints, particularly
        during season planning for s01 where the jaehaerys config is a known
        rejected option. The heading inconsistency is not a schema fault but
        is a documentation fault that will produce confusion in the impersonator
        load-set when the heading and the references field disagree about which
        project this card belongs to.
      criteria: >
        The H1 heading of cond-shard-behavioral-weight must not reference
        the Jaehaerys I config. The heading must identify this as the
        flea-bottom-dance config (125 AC) or drop the era label entirely.

    - id: fault-007
      type: fault
      what: >
        cond-westerosi-customary-authority provisioned in the warehouse has
        frontmatter: scope: project, project: taylor-hebert-westeros. This is
        the 120 AC / Riverlands / Harrenhal-adjacent config card for the
        prior Westeros project. Its body contains: age-11-in-Westeros framing,
        Harrenhal-specific failure paths ("a potential path to Harrenhal"),
        cross-house Lannister-Hightower deputization at 120 AC, literacy
        framing for an 11yo septon-ward child, and cond-impressment-census-120ac
        as a paired card. None of this is applicable to the 125 AC
        Crownlands/KL config. The 1c-candidate-menu.md recommended selecting
        the non-jaehaerys-specific variant and confirming era coverage;
        the card provisioned is instead a taylor-hebert-westeros project-scope
        card, not the era-general variant.
        Memory.md laws section lists cond-westerosi-customary-authority without
        a variant qualifier. Loading this card as the authoritative customary
        authority for flea-bottom-dance produces wrong-project behavioral
        rules (Harrenhal pathways, Lannister-Hightower 120 AC cross-deputization,
        age-11 social exposure framing, septon-ward cover story) in the
        constraint set for a 17yo tanner in the 125 AC Crownlands.
      why: >
        Any impersonator or auditor loading the laws section of memory.md and
        following cond-westerosi-customary-authority will receive behavioral
        rules scoped to the wrong era, wrong geography, and wrong protagonist
        age. The specific failure modes: (1) literacy red-flag framing is for
        a child whose literacy is surprising; Taylor at 17 is being treated
        differently by Crownlands social physics than an 11yo in Harrenhal's
        shadow; (2) Harrenhal path-to-failure is irrelevant in Crownlands/KL
        context; (3) Lannister-Hightower 120 AC administrative cross-deputization
        is wrong era and wrong faction configuration for 125 AC Dance period;
        (4) the card's interaction notes pair it with cond-impressment-census-120ac
        which does not exist in this project's constraint set.
        This is the most operationally dangerous wrong-config card in the
        warehouse because it governs Taylor's daily social environment.
      criteria: >
        The warehouse must not contain the taylor-hebert-westeros scoped
        cond-westerosi-customary-authority as the active card for this project.
        Either: (a) a 125 AC / Crownlands / KL-proximate config of customary
        authority must be authored and provisioned, accounting for the 17yo
        female social position in Flea Bottom rather than the 11yo septon-ward
        in Riverlands; or (b) the era-general Westerosi customary authority
        card (if one exists without Jaehaerys or westeros project scoping)
        must be confirmed as era-applicable to 125 AC Dance and provisioned
        in its place; or (c) memory.md must be updated to reference the
        correct variant slug and the wrong-project card removed from the
        warehouse. The 120 AC / Harrenhal / Lannister-Hightower content must
        not be the operative constraint set for this project.

    - id: fault-008
      type: fault
      what: >
        cond-smallfolk-political-physics (scope: library) and
        cond-feudal-hierarchy-law (scope: library) both carry named
        Jaehaerys-era characters and wrong-era geography as their primary
        illustrative content. cond-smallfolk-political-physics body references:
        Mira Stonefield-Jaehaerys (named as the operative community-elder
        figure), Septon Rowan, Aldric Pryor, Clem Ferris, Fairstead,
        "Blue Fork spirits," reeve-as-membrane for Fairstead. The card's
        Interaction Notes state "With Mira Stonefield-Jaehaerys: The peer-
        authority-earned key in Mira's vibes is a direct expression of this
        card" — referencing a character who does not exist in this project.
        cond-feudal-hierarchy-law body references: House Ryger of Willow Wood
        as the local feudal authority; Taylor's literacy exposure specific to
        the septon-ward situation; "path from strange-child → flagged-for-
        review → held-at-harrenhal-pending-determination" as the failure path;
        Aldric Pryor's record; "Stage 3/4" threshold from cond-suppression-
        policy-progression (a card not in this project's constraint set).
        The 1d audit flagged this as flag-002 (advisory). At series-level
        this is a fault because season planning for s01 will load these cards
        to model Flea Bottom community dynamics and the Lord's administrative
        apparatus and will receive Fairstead/House Ryger/Mira Stonefield as
        the operative examples.
      why: >
        Season planning agents loading these cards to establish the political
        physics of 125 AC Flea Bottom will encounter: Mira Stonefield-Jaehaerys
        as the operative community-elder template (wrong project, wrong era,
        wrong geography); House Ryger of Willow Wood as the local feudal
        authority (wrong lord for the Crownlands; the relevant authority
        structures in Crownlands/KL are Crown-proximate, not a Tully bannerman
        minor house); Harrenhal as the failure-path destination (wrong for KL-
        adjacent; the Crown's apparatus and the Red Keep are the relevant
        institutions); cond-suppression-policy-progression as a paired card
        that is not in this project's warehouse. Any agent modeling how
        Flea Bottom's tanner-elder, dock-runner, or labor web interacts with
        authority will be working from Riverlands Fairstead physics, not
        Crownlands KL-proximate urban physics. The flag-002 classification
        from 1d-audit was appropriate for that audit's scope (constraint card
        review only); at series-level with season planning imminent it
        escalates because the wrong-era named characters will be mistakenly
        loaded as this project's operative cast.
      criteria: >
        Both cards require Crownlands/KL-proximate addenda that: (1) replace
        Mira Stonefield-Jaehaerys with the correct project-cast elder figure
        (oc-tanner-elder) in the Interaction Notes and operative examples;
        (2) replace House Ryger of Willow Wood and Fairstead with the correct
        Crown-proximate authority structures for 125 AC Crownlands (Crown
        steward apparatus, City Watch, Red Keep administrative reach); (3)
        replace the Harrenhal failure path with the appropriate KL failure path;
        (4) remove or quarantine references to cond-suppression-policy-
        progression and cond-westerosi-customary-authority-jaehaerys in
        the Interaction Notes. Addenda can follow the same pattern as
        cond-crownlands-superstition-frame-125ac: project-scope cards that
        override named examples without replacing the underlying structural
        content.

    # -----------------------------------------------------------------------
    # NEW — COVERAGE
    # -----------------------------------------------------------------------

    - id: flag-001
      type: flag
      what: >
        oc-tanner-mother and oc-tanner-father references fields both list
        cond-westerosi-superstition-frame (the base Riverlands 84–101 AC card)
        but not cond-crownlands-superstition-frame-125ac. These characters are
        the primary carriers of the "Tya who came back wrong" Stranger-leavings
        frame. The project-specific vocabulary for that frame (the folk terms,
        the tanner-family grief-interrupted dynamics, the flinch-tell) lives
        in the crownlands card, not the base card.
      why: >
        An impersonator loading the tanner-mother or tanner-father card and
        following the references chain will reach the base card's Riverlands
        vocabulary (Blue Fork spirits, 84 AC folk terms) rather than the
        crownlands 125 AC vocabulary the characters should use. This is
        advisory because the base card is not wrong in its structural content
        and the crownlands card states "load alongside the base card" — but
        actors will miss the Crownlands-specific vocabulary if the reference
        chain does not include it.
      criteria: ~

    - id: flag-002
      type: flag
      what: >
        oc-broken-maester references field includes cond-westerosi-superstition-
        frame but not cond-crownlands-superstition-frame-125ac. The maester
        is the character who most closely observes the wrongness-perception
        dynamic (through-wall insects; his own framing of what Taylor is doing
        in his rooms), and the Crownlands-urban vocabulary for that perception
        (dragon weather, guild work gone wrong, maester-proximity deferral)
        is in the crownlands card.
      why: >
        Same advisory gap as flag-001. The maester operating in KL's eastern
        quarter will perceive Taylor's fauna-control through the Crownlands-
        urban register, not the Riverlands Jaehaerys-era register. The
        impersonator for this character should have the crownlands card in
        their reference chain.
      criteria: ~

    - id: flag-003
      type: flag
      what: >
        Three audience execution watches have been carried through every OQ
        review and the series plan review without resolution at plan level.
        They are execution-level watches appropriate for shoot and wrap audits,
        but they are load-bearing enough that they should be explicitly
        captured in the series plan or a carry-forward document so they
        survive into /and-season-plan s01. Currently they live only in
        audience STM files (worm-canon-pedant, dark-fantasy-reader,
        cape-fic-reader). The watches are:
        (1) Taylor's in-world theory for why insect-network density interacts
        with the glass-candle relay apparatus must appear in prose before the
        s4 experiment — not as exposition, as visible reasoning;
        (2) Physical distance from Taylor's Flea Bottom base to the broken
        maester's eastern-quarter apothecary must be established with
        precision at least once in prose (300m hard limit compliance);
        (3) Relay-load accumulation must be legible as the cause of the S2
        Khepri-mantle crossing in the prose — behavioral change alone is
        insufficient; the load-cause chain must be recoverable by the reader.
      why: >
        These watches are the direct downstream requirement of accepted plans.
        If they are only in audience STM files, they risk being missed by the
        screen-writer at /and-season-plan s01 (who loads the series plan and
        memory.md, not the audience STM). The s01 plan could be built without
        establishing the maester-distance check or the early hypothesis chain,
        and the failure would only surface at shoot review — after prose is
        committed. Carrying them explicitly into a planning constraint would
        front-load the check. This is advisory; the watches are findable in
        STM; the risk is that they are not in the planning agent's load-set.
      criteria: ~

    # -----------------------------------------------------------------------
    # COVERAGE — carry-forwards check
    # -----------------------------------------------------------------------

    - id: pass-001
      type: pass
      what: >
        1b carry-forward: "earlier audible maester scene" dramatist constraint.
      why: >
        Captured in cond-clinical-self-erasure executable form note #3:
        "At least one s1-or-early-s2 scene where Taylor hears the broken
        maester through the network and adjusts her behavior in response."
        Also in 1c-proposed-cast.md carry-forward to /and-season-plan s01.
        Will survive into season planning via the condition card load-set.

    - id: pass-002
      type: pass
      what: >
        1b carry-forward: s4 experimental subjects deferred to s4 planning.
      why: >
        Correctly deferred in 1c-candidate-menu.md (B7/B8) and 1c-proposed-cast.md.
        Not in series cast roster. No premature authoring found.

    - id: pass-003
      type: pass
      what: >
        1b carry-forward: loc-dance-climax-site deferred to s3 planning.
      why: >
        Correctly deferred in 1c-candidate-menu.md (C6) and 1c-proposed-cast.md.
        Not in stage_elements in memory.md. No premature authoring found.

    - id: pass-004
      type: pass
      what: >
        1b carry-forward: cond-density-saturation-protocol deferred to s2+
        pre-work.
      why: >
        Correctly deferred in 1c-candidate-menu.md. Not in constraint card
        set. No premature authoring found.

    # -----------------------------------------------------------------------
    # SEQUENCING — s2 threshold / s3 demonstration / s4 foreclosure
    # -----------------------------------------------------------------------

    - id: pass-005
      type: pass
      what: >
        Sequencing check — Khepri threshold (s2), demonstration (s3),
        foreclosure (s4): explicit separation enforced, required ordering
        maintained.
      why: >
        Series plan chunks explicitly separate events across season boundaries.
        cond-series-tone-constraints-125ac Khepri-Unlock Sequencing Rule states:
        "These must be visibly sequenced" with the causal chain s2 crossing →
        behavioral change → Taylor arrives in s3 already changed → s3
        demonstration as downstream consequence. cond-fauna-control-rules-125ac-
        addendum Override 2 states: "Visible sequencing with s3 demonstration:
        the Khepri-mantle threshold crosses in late s2. The s3 demonstration
        occurs in s3. These are explicitly separated by a season boundary...
        Any story beat that collapses the threshold crossing and the
        demonstration into a single scene or single episode is a structure
        violation." The foreclosure is explicitly positioned as detonating
        AFTER the war ends, never simultaneous with the demonstration.
        World-notes BEHAVIOR: "The demonstration must land in the Khepri-
        register, NOT the triumph-register. The Dance ending is consequence,
        not reward." All three constraints are present and non-contradictory.
        No sequencing violation found at series-plan scope.

    - id: pass-006
      type: pass
      what: >
        Foreclosure NOT simultaneous with demonstration — explicit enforcement.
      why: >
        World-notes OQ-9: "s4 FORECLOSURE EVENT...DETONATES here — after the
        demonstration, never simultaneous with it." Series plan s04 chunk:
        "detonates after the war ends." cond-series-tone-constraints-125ac:
        "No exhale between demonstration and foreclosure." These three sources
        are consistent and mutually reinforcing. PASS.

    # -----------------------------------------------------------------------
    # SCHEMA COMPLIANCE
    # -----------------------------------------------------------------------

    - id: pass-007
      type: pass
      what: >
        Schema compliance: cond-fauna-control-rules-125ac-addendum,
        cond-series-tone-constraints-125ac, cond-reincarnation-mechanics-125ac,
        cond-no-parahuman-infrastructure — frontmatter required fields.
      why: >
        All four cards carry: name, class, scope, world, origin, quality.
        Project-scope cards additionally carry project field. Variant cards
        carry variant-of and variant-reason. References fields populated with
        load-dependencies. No missing required fields found (supersedes gap
        in cond-reincarnation-mechanics-125ac classified separately as res-005).

    - id: pass-008
      type: pass
      what: >
        Schema compliance: actor cards — taylor-hebert-flea-bottom frontmatter.
      why: >
        name, class, scope, world, persona-purpose, variant-of, variant-reason,
        variant-project, aliases, composes, references, origin, quality, tier
        all present. Working copy note points to library source of truth. PASS.

    - id: pass-009
      type: pass
      what: >
        Memory.md series block completeness against schema/showrunner-memory.schema.md.
      why: >
        routing, series (theme, laws, lore, behaviors, plot, cast_roster,
        stage_elements), seasons (four entries with slug, chunk, status), active
        (season ~, episode ~) all present. Laws block lists 8 entries; lore
        block lists 2; behaviors block lists 2. Cast roster lists all 12
        provisioned personas in correct order. Stage elements lists all 5
        provisioned locations.

    - id: flag-004
      type: flag
      what: >
        memory.md laws section lists cond-westerosi-customary-authority without
        a variant qualifier. Given fault-007 above (the provisioned warehouse
        card is the taylor-hebert-westeros project-scope card), this slug
        reference in memory.md is currently unresolvable to the correct card.
        After fault-007 is resolved (correct card provisioned or new card
        authored), this memory.md entry will need to reference the correct
        slug of whatever card replaces it.
      why: >
        After fault-007 is resolved, if the replacement card has a different
        slug (e.g., cond-westerosi-customary-authority-125ac), the memory.md
        laws entry must be updated to match. This is a dependency flag on
        fault-007, not a standalone fault.
      criteria: ~

    # -----------------------------------------------------------------------
    # CONSISTENCY — vibes clouds cross-check
    # -----------------------------------------------------------------------

    - id: pass-010
      type: pass
      what: >
        Series vibes cloud (vibes.md) vs. world-notes constraints and series
        plan — consistency check.
      why: >
        Tonal keys: grimdark-register entries (costs-accrue, no-cheap-horror,
        contemplative-not-momentum, demonstration-not-triumph) match world-notes
        DECIDED commitments and cond-series-tone-constraints-125ac
        prohibitions. Faustian-pressure and clinical-self-erasure keys match
        the OQ-3 register requirement. Khepri-weight entries match OQ-2 and
        OQ-9 constraints. Posture keys (spurns-nobility, protects-smallfolk-
        experimentally, cowing-through-fear) match world-notes DECIDED posture
        commitments. Pressure keys (the-Tya-shaped-debt, the-burned-log,
        the-brake-that-does-not-stop-her, the-air-gap) match OQ-1, OQ-3, and
        OQ-7 carry-forwards. No contradiction between vibes cloud and
        constraint card set found.

    - id: pass-011
      type: pass
      what: >
        taylor-hebert-flea-bottom vibes.md vs. world-notes and persona card
        Hard Fences — consistency check.
      why: >
        Active world-keys match series vibes cloud on all overlapping axes.
        Private associations add actor-level specificity without contradicting
        series-level constraints. khepri-mantle-sealed entry correctly
        frames the sealed status as "door she walks past" — sealed, present,
        pressuring, not accessible. clinical-register private association
        ("the log is honest by its own terms; what leaves the log was never
        there; she does not experience this as dishonesty; this is the horror")
        is precisely aligned with cond-clinical-self-erasure's executable
        form notes. No contradiction found.

    - id: pass-012
      type: pass
      what: >
        Cast posture consistency — rhaenyra-targaryen project addendum.
      why: >
        rhaenyra-targaryen actor card carries explicit "Project Posture —
        flea-bottom-dance (CRITICAL)" section. Items 1–5 explicitly prohibit:
        ally relationship, romantic dynamic, anything beyond witness-figure
        function, patronage offer, and faction-aligned vs. smallfolk alignment.
        This matches world-notes DECIDED: "Both Targaryen factions...are cowed
        by fear, not converted or allied with." No contradiction.

    - id: pass-013
      type: pass
      what: >
        Cast posture consistency — antagonist-instrument restriction on all
        Targaryen/Hightower cast.
      why: >
        All four Targaryen/Hightower actor cards (rhaenyra, aegon-ii, otto,
        aemond) carry Hard Fence prohibitions against conversion, alliance,
        or romantic relationship with Taylor. All four are marked as
        witnesses-to-demonstration or antagonist-instruments. No card
        contradicts the world-notes posture rule.

    # -----------------------------------------------------------------------
    # CAST GAP
    # -----------------------------------------------------------------------

    - id: pass-014
      type: pass
      what: >
        Cast gap check — 1b carry-forwards against provisioned cast.
      why: >
        All cast members required by 1b carry-forwards are provisioned:
        tanner-family (oc-tanner-mother, oc-tanner-father); tanner-elder
        (oc-tanner-elder); dock-runner (oc-dock-runner); tallow-chandler
        fence (oc-tallow-chandler); broken maester (oc-broken-maester);
        s4 subjects deferred (correctly). Locations from 1b carry-forwards:
        all five provisioned (tanner-village, flea-bottom, flea-bottom-base,
        eastern-quarter-apothecary, red-keep-outer-ring). No gap found.

    - id: pass-015
      type: pass
      what: >
        Cast gap check — series plan implied cast against active-project/actors.
      why: >
        Series plan requires: protagonist, Tya-origin cost-surface characters,
        Flea Bottom embedder, operational legs, glass-candle channel, sole
        research witness, black faction antagonist-instrument, green faction
        figurehead antagonist, Hightower intelligence architect, green faction
        coercive instrument, background king (pre-Dance). All 12 provisioned
        actors map to these roles without gap. Witness-from-both-factions
        at s3 demonstration: rhaenyra (black), aegon-ii (green), aemond (green)
        cover both sides. The series plan's "witnesses from both factions"
        requirement is satisfied.

    # -----------------------------------------------------------------------
    # PLAN QUALITY SIGNAL
    # -----------------------------------------------------------------------

    - id: pass-016
      type: pass
      what: >
        Plan quality signal — OQ review attempt counts and revise/accept history.
      why: >
        OQ-1: attempt 1, ACCEPT (all). OQ-2: attempt 1, ACCEPT (all). OQ-3:
        attempt 2 — dramatist REVISE at attempt 1 (rise-without-peak); attempt
        2 added s4 foreclosure event and was ACCEPT (all). OQ-4/5: attempt 1,
        ACCEPT (all). OQ-6/7/8/9: attempt 2 — dramatist REVISE at attempt 1
        (S2 rise-without-peak); attempt 2 moved Khepri-mantle threshold to S2
        as dedicated peak and was ACCEPT (all). Series plan: attempt 1,
        ACCEPT (all). No OQ reached attempt exhaustion forcing screen-writer
        proceed. No case where both audience and dramatist returned REVISE.
        No plan-quality signal applies.

    # -----------------------------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------------------------
    # Active faults requiring fixer dispatch: res-003, res-004, res-005,
    # fault-006, fault-007, fault-008.
    # Flags (advisory, no fixer dispatch): flag-001, flag-002, flag-003,
    # flag-004.
    # Passes: res-001, res-002, pass-001 through pass-016.
    #
    # Critical priority for fixer before human presentation:
    # fault-007 is the most operationally dangerous — the wrong-project
    # customary-authority card is the operative constraint for Taylor's
    # daily social environment and will corrupt season planning if not
    # resolved.
    # res-003 and res-004 (scope corrections) are low-effort and should
    # accompany fault-007 dispatch.
    # fault-008 (Jaehaerys-era smallfolk card addenda) can be dispatched
    # in the same batch.
    # fault-006 (heading residue) is a one-line fix.
    # res-005 (supersedes chain) requires touching two cards.
    # -----------------------------------------------------------------------
```
