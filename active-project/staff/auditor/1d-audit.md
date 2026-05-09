```yaml
audit:
  scope: series
  target: taylor-hebert-jaehaerys — 1d constraint card set (14 cards)
  timestamp: 2026-05-09
  findings:

    # ── FAULTS ────────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        Active-control cost curve divergence between taylor-hebert-jaehaerys
        actor card (Stats / ambient_vs_directed NOTE) and warehouse
        cond-fauna-control-rules (Physical Cost Curve — Child-Body Edition).

        Actor card states:
          - headache onset: over 10 minutes of active control
          - nosebleed onset: over 20 minutes
          - blackout risk: over 30 minutes

        Warehouse cond-fauna-control-rules states:
          - headache onset: 3–10 minutes
          - nosebleed onset: 10–20 minutes
          - blackout risk: beyond 20 minutes

        The two sources disagree on every breakpoint. The actor card's
        numbers (10 / 20 / 30) match the adult base-card cost curve from
        the library cond-fauna-control-rules (5–15 / 15–30 / beyond 30,
        compressed to child-body language) but are inconsistent with the
        warehouse override the project explicitly authored to reflect the
        child-body shorter fuse. The warehouse card's numbers (3 / 10 / 20)
        are internally consistent with the child-body rationale and are
        corroborated by the project-scope note in the warehouse card's header
        ("adjusted to reflect Taylor's starting age"). The actor card appears
        not to have been updated when the warehouse override was authored.
      why: >
        The cost curve is a hard constraint that auditor is required to
        enforce against every scene involving Taylor's active swarm use.
        An impersonator loading only the actor card will apply the wrong
        (higher, adult-adjacent) breakpoints and write Taylor sustaining
        active control far longer than the child-body ceiling allows.
        An auditor loading only the actor card will not flag scenes where
        Taylor runs a twelve-minute active swarm without nosebleed — which
        the warehouse card says is a fence violation. The two sources cannot
        both be correct; having both in the project creates silent
        inconsistency that resolves differently depending on which card an
        agent loads first.
      criteria: >
        The actor card's Stats block (ambient_vs_directed NOTE, physical_cost_active
        field, and Action Costs section) and the warehouse cond-fauna-control-rules
        Physical Cost Curve must state the same breakpoints for the age-9 child-body
        tier. The authoritative numbers must be identified (the premise bundle and the
        warehouse card's project-scope note establish the child-body shorter fuse as
        the decided constraint; the warehouse card's 3/10/20 scale is the correct
        reference). The actor card must be updated to match.

    - id: fault-002
      type: fault
      what: >
        Library card cond-fauna-control-rules (cards/conditions/cond-fauna-control-rules.card.md)
        carries scope: project and project: taylor-hebert-westeros — the
        prior 120 AC project, not the current taylor-hebert-jaehaerys project.
        The card is also missing overrides: or supersedes: metadata that would
        connect it to the warehouse project card.

        Additionally, the library card's Interaction Notes reference two
        cards that do not exist in the 84 AC project or its library:
          - cond-impressment-census-120ac (explicitly era-wrong; only exists
            for the Viserys I project)
          - cond-westerosi-customary-authority (non-era-specific slug; the
            correct 84 AC card is cond-westerosi-customary-authority-jaehaerys)
      why: >
        A library card scoped to a closed project is misclassified. It cannot
        be loaded as a library resource for any new project without the project
        scope field being an obstruction. The stale cross-references in the
        Interaction Notes are dead slugs for the 84 AC project — any agent
        following them to context will find wrong-era material
        (cond-impressment-census-120ac) or no material at all. The warehouse
        override exists and correctly handles the project-specific content, but
        the library card's incorrect scope is a schema violation and a
        cross-reference fault.
      criteria: >
        The library card at cards/conditions/cond-fauna-control-rules.card.md
        must be updated so that: (1) scope is set to library; (2) project
        field is cleared or removed; (3) stale Interaction Notes references
        (cond-impressment-census-120ac, cond-westerosi-customary-authority)
        are replaced with the correct 84 AC slugs
        (cond-westerosi-customary-authority-jaehaerys) or removed.
        The warehouse override's correct project field (taylor-hebert-jaehaerys)
        and overrides: metadata are already present and do not need to change.

    - id: fault-003
      type: fault
      what: >
        Library card cond-no-parahuman-infrastructure
        (cards/conditions/cond-no-parahuman-infrastructure.card.md)
        carries scope: project and project: taylor-hebert-westeros.
        The body text also still reads "Hard World-Law for taylor-hebert-westeros"
        in the title and references "120 AC" in the description.

        The warehouse copy (active-project/warehouse/cond-no-parahuman-infrastructure.card.md)
        correctly carries scope: library and the 84–101 AC Shard carve-out, and
        its body text is titled for taylor-hebert-jaehaerys. These two cards
        now have inverted scope fields: the warehouse copy carries scope: library
        while the library card carries scope: project. The schema requires
        scope: library for cards in the cards/ directory tree.
      why: >
        The inverted scope fields mean margit and any agent performing a
        card fetch would load the wrong authoritative source for this card.
        The library card is wrong-scoped and wrong-era in its body text. An
        agent fetching cond-no-parahuman-infrastructure from the library
        (not the warehouse) will find a card that (a) claims scope: project,
        (b) claims project: taylor-hebert-westeros, and (c) does not contain
        the Shard carve-out paragraph — which means the Shard's behavioral-weight
        presence would appear to violate the prohibition rather than being
        explicitly carved out. This is a cross-project contamination risk.
      criteria: >
        The library card at cards/conditions/cond-no-parahuman-infrastructure.card.md
        must be updated so that: (1) scope is set to library; (2) project field
        is cleared or removed; (3) title and description references to
        taylor-hebert-westeros and 120 AC are updated to match the general
        world-law framing (or the card is tombstoned with superseded_by pointing
        to the warehouse variant promoted to library). The warehouse copy's scope
        field must then be corrected to scope: project with project:
        taylor-hebert-jaehaerys, consistent with its role as a project-scope
        working copy.

    - id: fault-004
      type: fault
      what: >
        Both the library card condition-swarm-in-foreign-ecology
        (cards/conditions/condition-swarm-in-foreign-ecology.card.md) and the
        warehouse copy (active-project/warehouse/condition-swarm-in-foreign-ecology.card.md)
        contain Interaction Notes referencing two slugs that do not exist in
        this project or its library:

          - condition-language-barrier
          - condition-war-of-five-kings-riverlands

        These are unresolved cross-references from the prior project's card
        lineage (the Viserys I / 120 AC / War of Five Kings-adjacent project
        context). Neither slug exists in cards/conditions/ or in the warehouse.
        The warehouse copy is an exact duplicate of the library card with no
        project-scope adjustments — it does not carry overrides: metadata,
        it has no project: field, and it makes no reference to the
        taylor-hebert-jaehaerys project. It appears to have been copied
        wholesale without project-scoping.
      why: >
        Dead cross-references in Interaction Notes are schema-adjacent violations
        (unresolved references). An agent following these slugs finds nothing.
        More substantively: the condition-war-of-five-kings-riverlands reference
        in an active 84 AC project condition card is an era-adjacency error —
        the War of Five Kings is approximately 200 years in Taylor's future and
        must not appear as a loaded context for any 84 AC scene. The warehouse
        copy lacking project scope metadata means it is not functioning as a
        project-scoped override; it is a duplicate that adds nothing over the
        library card and provides no 84 AC adjustments.
      criteria: >
        Both copies must have the stale Interaction Notes references removed
        or replaced with correct 84 AC slugs. The warehouse copy must be
        updated to carry scope: project and project: taylor-hebert-jaehaerys,
        and any project-specific adjustments relevant to the 84 AC config
        (seasonal notes, era-correct cross-references) must be present.
        If no project-specific adjustments are needed beyond removing stale
        references, the warehouse copy should at minimum carry overrides:
        condition-swarm-in-foreign-ecology and correct scope metadata.

    - id: fault-005
      type: fault
      what: >
        cond-suppression-policy-progression Stage 4 header reads:
        "Stage 4: Action (~98–101 AC, Council horizon — Taylor age ~21)"

        Under the project's settled arithmetic: Taylor arrives at ~84 AC at
        age 7–8. At 98 AC she is approximately 14–15. At 101 AC she is
        approximately 17. Age ~21 at 98–101 AC is arithmetically impossible
        under this project's parameters (arrival 84 AC, age 7–8 at arrival).

        The correct age range for the 98–101 AC window is approximately 14–17.
      why: >
        Stage 4 is the suppression escalation that converges with the Great
        Council close. Writers and auditors tracking Taylor's age against her
        capability curve (the child-body cost ceiling rising with biological
        development) need correct age anchors at each suppression stage. An
        age annotation of ~21 implies adult capability levels (near-full adult
        cost curve per the warehouse fauna-control card) when the correct age
        (~14–17) sits in the S2–S3 bridge tier — a meaningfully different
        capability state. An impersonator reading this header and calibrating
        Taylor's physical capacity to ~21 will over-extend her swarm capability
        at a critical narrative juncture.
      criteria: >
        The Stage 4 header in cond-suppression-policy-progression must be
        corrected so the age annotation reflects the project arithmetic:
        Taylor at 98–101 AC is approximately 14–17 years old, not ~21.

    # ── FLAGS ─────────────────────────────────────────────────────────────────

    - id: flag-006
      type: flag
      what: >
        cond-suppression-policy-progression Stage 3 header reads:
        "Stage 3: Policy (~91–97 AC, no later than mid-S3 — Taylor age ~14–20)"

        At 91 AC Taylor is ~14–15 (consistent). At 97 AC Taylor is ~20–21, not
        ~20. The upper bound of the age range is off by one year. This is a
        minor imprecision introduced by rounding the arrival age (7–8 at 84 AC)
        inconsistently.
      why: >
        Minor annotation imprecision; no downstream fiction consequence unless
        writers are using the age number rather than the AC number for production
        scheduling. Noted for consistency with fault-005 correction; the
        Stage 3 and Stage 4 headers should be corrected in the same pass.

    - id: flag-007
      type: flag
      what: >
        condition-swarm-in-foreign-ecology (library and warehouse) does not
        reference the project's primary superstition categorization card
        (cond-westerosi-superstition-frame) in its Interaction Notes.
        The wrongness-perception cultural frame in the swarm-foreign-ecology
        card sends the reader to "cultural frame" prose inline but does not
        cross-reference the dedicated card that governs witness categorization
        vocabulary. By contrast, the warehouse cond-fauna-control-rules
        correctly references cond-westerosi-superstition-frame.

        This is a watch item: the swarm-ecology card is the one most likely
        to be loaded by impersonators for scene-level checks, and the missing
        reference means they may not automatically load the superstition frame.
      why: >
        No fiction-level fault; the wrongness-perception section in the
        swarm-ecology card is self-contained. But the cross-reference gap
        creates a load-path gap for impersonators who check the swarm card
        and do not follow onward to the superstition frame. Supporting cast
        impersonators running witness categorization should load both; the
        missing link increases the chance they do not.

    - id: flag-008
      type: flag
      what: >
        The library card cond-fauna-control-rules Interaction Notes reference
        "cond-westerosi-customary-authority" (non-era-specific slug) rather
        than the correct 84 AC slug "cond-westerosi-customary-authority-jaehaerys".
        The generic slug does not exist as a distinct card in cards/conditions/;
        only the era-specific variant exists.

        This is subordinate to fault-002 (the library card's overall
        wrong-project scope) and should be resolved in the same fixer pass.
        Flagged separately because the slug resolution is distinct from the
        scope correction.
      why: >
        An agent following the Interaction Note's slug will find no card at
        the generic name. The era-specific card is the correct referent.

    # ── PASS ITEMS ────────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        Faith Militant era constraint — cross-check across
        cond-faith-of-seven-jaehaerys, cond-westerosi-customary-authority-jaehaerys,
        cond-riverlands-84ac-state, cond-feudal-hierarchy-law.
      why: >
        All four cards state consistently: Faith Militant suppressed by
        Jaehaerys I approximately fifty years before story open. No organized
        Faith violence or armed Faith enforcement in 84–101 AC. Faith tools
        are pastoral and communicative only. No conflict across cards.

    - id: pass-002
      type: pass
      what: >
        Shard / parahuman-infrastructure interaction — cross-check between
        cond-shard-behavioral-weight and warehouse cond-no-parahuman-infrastructure.
      why: >
        The warehouse copy of cond-no-parahuman-infrastructure explicitly
        adds the Shard carve-out paragraph: "The Shard is present at
        behavioral-weight level only. See cond-shard-behavioral-weight."
        The What This Card Does Not Prohibit section lists the Shard's
        behavioral-weight presence. Both cards are consistent with each other
        and with the decided constraint in world-notes (Shard present, dormant
        at Entity-communication level, active at behavioral-weight level).

    - id: pass-003
      type: pass
      what: >
        Suppression-policy deadline — cross-check between
        cond-suppression-policy-progression, cond-series-tone-constraints-84ac,
        and world-notes.
      why: >
        World-notes: "Suppression-as-policy (not incident response) must be
        reached no later than mid-S3." cond-suppression-policy-progression
        Stage 3: "no later than mid-S3" stated in both the header and the
        world-notes-mandate block. cond-series-tone-constraints-84ac Cost-Migration
        Rule: "Suppression-as-policy (not incident response) must be reached
        no later than mid-S3." All three sources agree.

    - id: pass-004
      type: pass
      what: >
        Era drift — general check for wrong-era names, institutions, or events
        across all 14 cards.
      why: >
        No card references Aerys II, Tywin, Rhaegar, Robert, Ned, Lyanna, the
        Faith Militant as active, the Dance as a present event, the War of Five
        Kings as a current context (the dead cross-references in fault-004 are
        slug names, not assertions that the war is happening), or any
        post-Jaehaerys institution. All canonical actors referenced
        (Jaehaerys I, Alysanne, Baelon, Rhaenys, Septon Barth) are correct for
        84–101 AC. Great Council 101 AC is treated as the horizon, not a resolved
        event. Dance of Dragons is treated as the post-series catastrophe.

    - id: pass-005
      type: pass
      what: >
        Westerosi superstition frame coverage — Riverlands old-gods-residue
        layer and categorization vocabulary for impersonators.
      why: >
        cond-westerosi-superstition-frame contains the Riverlands mid-region
        layer (dual-tradition residue, river spirits, insect cultural weight,
        the "touched" category). The card provides explicit vocabulary lists
        (words characters reach for / words they do not reach for). Cross-check
        against supporting cast vibes (from 1c-log): Rowan's vibes carry
        "westerosi-superstition-frame" as a loaded key. Mira's vibes carry
        "smallfolk-political-physics" which is the substrate the superstition
        frame operates through. No actor card in the cast narrates the swarm
        in a way that bypasses the superstition frame's categorization
        constraints — no cast member has vocabulary for "parahuman" or
        "power" in the modern sense.

    - id: pass-006
      type: pass
      what: >
        Schema validation — all 14 cards checked against schemas/card.schema.md
        required fields: name, class, scope, origin, quality; class-appropriate
        body sections.
      why: >
        All 14 cards carry required frontmatter. All are class: condition.
        All carry scope values present in the schema enum. All carry origin
        and quality fields. No card uses a class value outside the five defined.
        Body sections in all cards include Description, Sensory Impact,
        Duration, and Interaction Notes — the condition class body sections
        per schema. No schema violation found beyond the scope-field
        incorrectness already named in fault-002 and fault-003 (wrong enum
        value pairing with wrong project field).

    - id: pass-007
      type: pass
      what: >
        Ambient-vs-directed distinction — presence and consistency across
        cond-fauna-control-rules (warehouse), taylor-hebert-jaehaerys actor
        card, and cond-reincarnation-mechanics-84ac.
      why: >
        Warehouse cond-fauna-control-rules introduces the ambient-vs-directed
        distinction with full mechanics. Taylor's actor card Stats block contains
        the binding NOTE on ambient_vs_directed explicitly. cond-reincarnation-mechanics-84ac
        cross-references cond-shard-behavioral-weight and cond-fauna-control-rules
        and is consistent with the passive-sense-is-free framing. The concept
        is coherent and not contradicted by any card. (The cost-curve number
        divergence is a separate fault — fault-001 — not an ambient/directed
        distinction disagreement.)

    - id: pass-008
      type: pass
      what: >
        Taylor uniqueness constraint — sole displaced soul, no other parahumans.
      why: >
        cond-reincarnation-mechanics-84ac Uniqueness section: "Taylor is the
        only displaced soul in this project." cond-no-parahuman-infrastructure
        warehouse copy: "No other capes." No card in the set contradicts this.
```
