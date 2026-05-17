```yaml
audit:
  scope: series
  target: dragon-gate-foreclosure / phase-1d constraint-card audit
  timestamp: 2026-05-17
  findings:

    # ──────────────────────────────────────────────
    # CRITICAL INFRASTRUCTURE: WAREHOUSE FILE ABSENCE
    # ──────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        All 14 condition cards and all 5 location cards listed in the 1c-log
        as "provisioned to active-project/warehouse/" are absent as physical
        files. Every read attempt against the warehouse directory returned
        "File does not exist." The 7 library condition cards (cond-shard-behavioral-weight,
        cond-feudal-hierarchy-law, cond-smallfolk-political-physics,
        cond-no-parahuman-infrastructure, cond-westerosi-superstition-frame,
        cond-fauna-control-rules, cond-reincarnation-mechanics) and all 7
        new project-scoped condition cards (cond-patron-dialect-operational-model,
        cond-watch-persons-risk-sweep, cond-kl-authority-dragon-gate-129ac,
        cond-fauna-control-rules-dragon-gate-addendum,
        cond-dragon-gate-arrival-and-witch-label,
        cond-series-tone-dragon-gate,
        cond-reincarnation-mechanics-dragon-gate) exist only as stub entries
        in cards/conditions/INDEX.md — none have physical file bodies in
        active-project/warehouse/. The 5 location cards (loc-dragon-gate-block,
        loc-dragon-gate-guardhouse, loc-miras-workshop,
        loc-black-adjacent-contact-premises, loc-dragon-gate-market-alley)
        are similarly absent. The 7 new project-scoped cards also lack
        quality assignments in the INDEX (they are not listed under by_quality),
        confirming they are stubs only.
      why: >
        Agents cannot load conditions or locations at shoot time if the physical
        files do not exist. All 10 audit classes below are dependent on reading
        the condition card bodies to verify constraint encoding; without the
        files, most encoding checks cannot be completed. More critically: the
        constraints encoded in the project-scoped condition cards ARE the
        structural enforcement mechanism for OQ-1 (range cap), OQ-2 (witch-label
        permanence), OQ-5 (patron-dialect ladder + reader-inference law), OQ-6
        (closing shape + final image), OQ-7 (cast scope + interiority rules),
        and tone law. Their absence means that shoot, facet, and stitch phases
        have no card-level enforcement to load — the constraints live only in
        world-notes.md and actor card Hard Fences, which are actor-context files
        not condition-slot enforcement.
      criteria: >
        Each card listed in 1c-log under "Conditions provisioned to
        active-project/warehouse/" and "Locations provisioned to
        active-project/warehouse/" must exist as a physical .md file at
        active-project/warehouse/<slug>.md with a complete card body meeting
        the condition/location schema (schemas/card.schema.md). The 7 new
        project-scoped condition cards must additionally receive quality
        assignments in the INDEX (full is required for the load-bearing cards;
        scant is acceptable only for locations at margit's discretion). The
        7 library cards must be copied from the library into the warehouse as
        project copies or referenced via their library paths — whichever the
        pipeline's load mechanism requires.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 1: RANGE/CAP CONSISTENCY
    # ──────────────────────────────────────────────

    - id: fault-002
      type: fault
      what: >
        cond-fauna-control-rules-dragon-gate-addendum: physical file absent
        (fault-001). Cannot verify that it enforces the ~100–150m hard constant
        as required by OQ-1. The addendum is referenced in Taylor's card
        (cards/personas/taylor-hebert-dragon-gate.card.md) and in
        active-project/actors/taylor-hebert-dragon-gate/card.md but cannot
        be inspected for content.
      why: >
        OQ-1 is a LAW: the range cap is a physical constant, not a plot brake.
        Without the addendum's card body, there is no schema-level enforcement
        document specifying the hard constant. Actor card Hard Fences carry
        the constraint for Taylor's impersonator context, but the addendum is
        the condition-slot enforcement loaded by studio and shoot infrastructure.
        Missing addendum = missing enforcement layer.
      criteria: >
        cond-fauna-control-rules-dragon-gate-addendum must be authored as a
        physical file and must explicitly state: (1) fauna-control range is
        hard-capped at ~100–150m, a physical constant of Taylor's condition in
        this world, non-expanding, non-contracting; (2) Khepri-mantle is sealed
        for full project duration with no unlock condition; (3) passive sense
        is ambient-not-directed, always-on, cannot be disabled.

    - id: pass-001
      type: pass
      what: >
        Taylor card range field (both library copy and project actor copy):
        fauna_control_radius stated as "~100–150m. Hard constant. Does not
        expand organically. Does not contract." Hard Fence 1 in both copies
        confirms "Range cap ~100–150m, non-expanding." This is fully consistent
        with OQ-1 binding.
      why: ~

    - id: pass-002
      type: pass
      what: >
        taylor-hebert-flea-bottom library card was NOT provisioned to
        active-project/actors/ (confirmed by 1c-log and actor directory scan).
        No flea-bottom card copy is in the warehouse either. The flea-bottom
        variant's 300m range with organic expansion cannot contaminate this
        project's constraint stack via that vector.
      why: ~

    - id: pass-003
      type: pass
      what: >
        cond-fauna-control-rules (base library card): not readable as a file
        (library card body not accessible), but the INDEX shows it is a
        library-scope card without project-specific overrides for the
        dragon-gate project. Taylor's actor card explicitly references BOTH
        cond-fauna-control-rules (base) and cond-fauna-control-rules-dragon-gate-addendum
        (project addendum) — the addendum pattern correctly layers the range
        restriction on top of the base rather than modifying the base.
        No evidence of a contradicting clause in the base card accessible
        through current reads.
      why: ~

    # ──────────────────────────────────────────────
    # AUDIT CLASS 2: PATRON-DIALECT OPERATIONAL MODEL INTEGRITY
    # ──────────────────────────────────────────────

    - id: fault-003
      type: fault
      what: >
        cond-patron-dialect-operational-model: physical file absent (fault-001).
        Cannot verify: (a) 6-rung ladder with all six rungs specified (M4,
        M9–10, M14–15, M18–19, M24, M27–28); (b) M14–15 enforcement-overshoot
        beat named explicitly as dramatist C1; (c) M27–28 falsification-on-belief
        constraint named as dramatist C2; (d) lit-snob non-negotiable C4
        encoded (model-falsification meta-statement MUST NEVER appear in
        prose — reader-inference only); (e) each rung's patron-channel specified.
      why: >
        This card is named "THE MECHANICAL SPINE" in 1c-log. It is the
        structural enforcement document for the entire foreclosure mechanism.
        Without it as a physical file, screen-writer, shoot, and auditor have
        no card-level source to verify rung-by-rung patron-channel assignments,
        no enforcement of the C4 literary-snob constraint (the most
        consequential prose discipline in the book), and no binding document
        for the C1/C2 dramatist conditions. The actor card Hard Fence 3 carries
        the C4 prohibition for Taylor's impersonator context only; the
        condition card is required to enforce it across all authoring phases.
      criteria: >
        cond-patron-dialect-operational-model must be authored as a physical
        file encoding: all six rungs of the ladder with month-marker, framing
        type, patron-channel, and named outcome; the M14–15 enforcement-overshoot
        beat explicitly flagged as C1 (seed of M27–28 sweep); the M27–28
        recognition-failure beat flagged as C2; and the C4 prohibition in
        explicit, unambiguous terms: the prose MUST NOT articulate
        "her reports were heard as authorizations, not calibrations" or any
        equivalent meta-statement in Taylor's interiority — reader-inference
        only, non-negotiable.

    - id: pass-004
      type: pass
      what: >
        Taylor actor card (library copy and project copy) encodes all 6 rungs
        in the "6-Rung Ladder" section with correct month markers, patron
        channels, and outcome labels. Hard Fence 3 prohibits naming the
        patron-dialect model in prose. Voice section explicitly names C4
        prohibition. The rung structure is internally consistent with
        world-notes.md LAW (OQ-5 resolved, six-rung ladder).
      why: >
        Pass on actor-card encoding. Fault-003 remains open on condition
        card physical existence.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 3: WITCH-LABEL PERMANENCE
    # ──────────────────────────────────────────────

    - id: fault-004
      type: fault
      what: >
        cond-dragon-gate-arrival-and-witch-label: physical file absent
        (fault-001). Cannot verify that it encodes permanent operational
        infrastructure, prohibits "lifting" or "correcting" the label, and
        specifies that the captain's tolerance is "layered" not "rescinded."
      why: >
        OQ-2 is a LAW. The witch-label is permanent operational infrastructure
        — a structural fact, not a plot variable. Without the condition card,
        there is no load-bearing schema document that a shoot-phase reviewer
        can cite to block a scene that incorrectly resolves or lifts the label.
      criteria: >
        cond-dragon-gate-arrival-and-witch-label must be authored as a physical
        file encoding: (1) the arrival sequence (market fire, insects lifting
        visibly, three gold cloaks, septon shouts "witch," overnight detention,
        released as "lunatic-not-worth-paperwork"); (2) the witch-label as
        permanent operational infrastructure — cannot be corrected without
        disclosing what Taylor actually is; (3) no card clause permits the
        label to be lifted, rescinded, or corrected at any point in the book's
        timeline; (4) the captain's tolerance is explicitly characterized as
        "layered on top of" the witch-label, not as a replacement or rescinding.

    - id: pass-005
      type: pass
      what: >
        Taylor actor card Hard Fence 7: "The witch-label is never lifted.
        Never corrected. Only layered." Voice section confirms: "Never uses
        the witch-label as a claim or a correction." Septon card
        (oc-ward-septon-dragon-gate): Hard Fence "Does not recant; holds
        the witch-classification." Captain card: Hard Fence language does
        not contain any clause permitting label removal. World-notes LAW
        (OQ-4 resolved): "The witch-label is not rescinded by his tolerance —
        it is layered." All actor-card-level encoding is consistent and
        non-contradictory.
      why: ~

    # ──────────────────────────────────────────────
    # AUDIT CLASS 4: CAST SCOPE DISCIPLINE
    # ──────────────────────────────────────────────

    - id: pass-006
      type: pass
      what: >
        Cast count: active-project/actors/ contains exactly 9 named recurring
        actor directories: taylor-hebert-dragon-gate, oc-watch-captain-dragon-gate,
        mira-stonefield-dragon-gate, oc-black-adjacent-contact, oc-persons-risk-officer,
        oc-rung3-steward, oc-ward-septon-dragon-gate, oc-block-fixture,
        oc-contacts-business-partner. This matches the 1c-log final cast list
        exactly. OQ-7 binding of 9 named recurring characters is satisfied.
      why: ~

    - id: pass-007
      type: pass
      what: >
        Named family for Mira: mira-stonefield-dragon-gate card contains no
        named family members. Aliases are [mira] only. References do not
        include any family-member card slugs. No family names appear in the
        card body's Critical Project-Scope Facts.
      why: ~

    - id: flag-001
      type: flag
      what: >
        oc-black-adjacent-contact card (Daveth): frontmatter aliases include
        [the-contact, daveth] and the card body states "Essosi-origin family
        (Braavosi grandfather)." OQ-7 LAW states "No named family for Mira
        or the Black-adjacent contact." The Braavosi grandfather is mentioned
        as backstory origin context, not as a named recurring character, and
        the grandfather is not given a name or introduced as a cast member.
      why: >
        The OQ-7 prohibition reads "no named family for [...] the Black-adjacent
        contact." The grandfather mention is one level removed — it establishes
        Daveth's Essosi origin register, not a named family member. However,
        if "Essosi-origin family (Braavosi grandfather)" is ever used in prose
        to introduce a named family scene or relationship, the fence is crossed.
        As encoded in the card it is backstory shorthand, not a named family
        introduction, so this is advisory rather than a hard fault. Screen-writer
        and shoot should not develop this into a scene.
      why: >
        Minor disambiguation risk. No current fence violation; advisory flag
        to prevent drift at shoot phase.

    - id: pass-008
      type: pass
      what: >
        Captain card (oc-watch-captain-dragon-gate): Hard Fence 1 is "No
        interiority rendered." Critical Project-Scope Facts state "Interiority:
        CLOSED. Readable through institutional behavior only. Never POV."
        This satisfies OQ-7 binding requirement for captain opacity and
        interiority disclaimer.
      why: ~

    - id: pass-009
      type: pass
      what: >
        Contact card (oc-black-adjacent-contact): Hard Fence 1 is "No
        interiority rendered; last hours external only." Critical Project-Scope
        Facts state "Interiority: CLOSED." This satisfies OQ-7 binding
        requirement for no-interiority on the contact.
      why: ~

    - id: pass-010
      type: pass
      what: >
        Block-fixture card (oc-block-fixture): "EXPLICITLY DISCLAIMS
        CONFIDANT-ROLE." Hard Fences include "No confidant role," "No
        operational role," "No interiority rendered." This satisfies OQ-7
        binding that the block-fixture is "non-confidant role."
      why: ~

    # ──────────────────────────────────────────────
    # AUDIT CLASS 5: AU DIVERGENCE LEGIBILITY
    # ──────────────────────────────────────────────

    - id: pass-011
      type: pass
      what: >
        Taylor actor card (library copy): Voice section, "The passive-sense
        texture" subsection explicitly states the cap is "a hard constant of
        her condition in this world, not an organic ceiling." Stats section:
        "The cap is a physical constant of her condition in this world, not
        a plot brake." Hard Fence 1: "Any scene implying organic range
        expansion is a mechanics violation." World-notes LAW (OQ-1 resolved):
        "The divergence must be legible in the text (named, observed, or
        acknowledged) and not silently elided."
      why: >
        The AU divergence (range-capped vs. canon shard behavior) is encoded
        as a fact Taylor has tested and knows — "she has tested it exactly
        once and the edge is sharp" — and the card explicitly prohibits
        prose treating it as organic or expanding. This satisfies the
        legibility requirement at the actor-card level.
      why: ~

    - id: flag-002
      type: flag
      what: >
        No condition card currently enforces the prose-legibility obligation
        for AU divergence at the condition-slot level (the relevant card,
        cond-fauna-control-rules-dragon-gate-addendum, is absent per fault-002).
        The legibility requirement is currently carried only by the actor card,
        not by a condition card that studio and shoot infrastructure can load
        scene-by-scene.
      why: >
        If fault-002 is resolved, this flag is satisfied automatically.
        Flagging to ensure the addendum's authored body includes legibility
        language and not just the mechanical cap values.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 6: CLOSING-SHAPE COMMITMENTS
    # ──────────────────────────────────────────────

    - id: fault-005
      type: fault
      what: >
        cond-watch-persons-risk-sweep: physical file absent (fault-001).
        Cannot verify that it encodes: (a) Taylor is processed by the same
        sweep; (b) final image is her own insects registering her stillness;
        (c) no clause admits Taylor surviving the close.
      why: >
        OQ-6 is a LAW and carries a "binding execution obligation" subcondition.
        The closing image — insects at range-cap registering no movement inside
        the guardhouse — must be enforced as a structural constraint from the
        condition card, not just from the actor card's internal Hard Fences.
        If this card does not exist, the closing-shape has no external
        enforcement document for screen-writer or shoot phases.
      criteria: >
        cond-watch-persons-risk-sweep must be authored as a physical file
        encoding: (1) the M27–28 sweep mechanism and its kill chain (contact
        detained, escalation Taylor did not author, contact killed in custody);
        (2) Taylor's arrest three days after contact's death under the same
        persons-risk protocols her ladder helped construct; (3) Taylor dies
        in the Dragon Gate guardhouse — not executed, not martyred, processed;
        (4) the final image: Taylor's own insects at range-cap registering
        no movement inside the building she is in; (5) no surviving clause —
        no card language permits Taylor to survive the close or escape the
        sweep.

    - id: pass-012
      type: pass
      what: >
        Taylor actor card (library and project copies): "The close" section
        explicitly states "Taylor dies in the Dragon Gate guardhouse — not
        executed, not martyred, processed. The final image is the insects at
        range-cap registering no movement inside the building she is in."
        Hard Fence 9: "The insect-ambient-register is a consistent prose
        mechanism throughout. The closing image — insects at range cap
        registering no movement inside the guardhouse she is dying in —
        must be EARNED." World-notes LAW (OQ-6 resolved): closing image
        confirmed, Taylor absent from terminus as subject, no surviving clause.
      why: >
        Actor-card level encoding is clean. Fault-005 remains open on
        condition card.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 7: FORECLOSURE-NOT-RECOGNITION TRAGEDY STRUCTURAL COMMITMENT
    # ──────────────────────────────────────────────

    - id: fault-006
      type: fault
      what: >
        No standalone condition card encodes the foreclosure-not-recognition
        structural commitment as a series-level constraint. cond-series-tone-dragon-gate
        is the expected carrier, but it is absent as a physical file (fault-001).
        The relevant law is in world-notes.md: LAW (OQ-6 resolved, structural
        shape): "The world's verdict, not Taylor's, is at the final image.
        Taylor is absent from the terminus as a subject." And THEME: "The
        shape is foreclosure — each defensible choice closes off a better
        outcome that was still possible. The book's verdict is the final state."
        And TONE: "No moral narration."
      why: >
        Without a condition card carrying this as an enforceable constraint
        readable by screen-writer and shoot, the structural commitment exists
        only in world-notes.md (showrunner memory, not a loadable condition).
        Any scene where Taylor recognizes the moral — where the prose articulates
        the theme rather than structuring it — has no card-level fence to cite
        against.
      criteria: >
        cond-series-tone-dragon-gate (or another designated carrier card)
        must encode: (1) the prose never names the moral — world's verdict
        not protagonist's; (2) theme-as-structure not theme-as-statement;
        (3) Taylor is absent as a subject from the terminus — she does not
        understand, does not choose, does not register the moral; (4) the
        foreclosure shape is: each defensible choice closes off a better
        outcome that was still possible; (5) this is not a recognition tragedy.

    - id: pass-013
      type: pass
      what: >
        Taylor actor card Hard Fence 3: "The patron-dialect model is NOT named
        by Taylor." Voice section: "The meta-recognition is reader-inference
        from the 6-rung consequence chain. Any prose articulating the model
        in Taylor's interiority is a literary-snob-C4 violation." Thematic
        Purpose section: "She does not understand this when it closes. The
        book's verdict is the final state." These are actor-scope enforcements
        of the structural commitment.
      why: >
        Actor-card level encoding is consistent. Fault-006 remains open
        on condition-card enforcement.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 8: SERIES-TONE / NO-MORAL-NARRATION DISCIPLINE
    # ──────────────────────────────────────────────

    - id: fault-007
      type: fault
      what: >
        cond-series-tone-dragon-gate: physical file absent (fault-001).
        Cannot verify that it encodes: (a) no aestheticized cruelty;
        (b) no moral narration; (c) structural deceleration into bureaucratic
        processing.
      why: >
        TONE laws in world-notes.md are not condition cards. Screen-writer
        and shoot agents load condition cards from the warehouse; they read
        world-notes.md only through showrunner context passing. A tone law
        that lives only in world-notes.md is not enforced at the card-load
        layer. Without cond-series-tone-dragon-gate, the tone constraints
        have no schema-level vehicle for scene-by-scene enforcement.
      criteria: >
        cond-series-tone-dragon-gate must be authored encoding: (1) grimdark
        with honest weight — bleakness earned by causal chains the reader can
        reconstruct, not aestheticized cruelty; (2) no moral narration —
        the book does not tell the reader what to think about Taylor's choices;
        (3) tragedy-of-competence pacing — structural deceleration into
        catastrophe, not pulp escalation; (4) the mode of death is bureaucratic,
        not dramatic; (5) foreclosure is structural, not person-authored.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 9: EARTH-BET NO-INTRUSION FENCE
    # ──────────────────────────────────────────────

    - id: pass-014
      type: pass
      what: >
        World-notes LAW (OQ-1 resolved): "Earth-Bet does not intrude. No
        portals open, no other capes appear, no Tinker tech is at hand."
        Taylor card (library copy): "Khepri-mantle: SEALED for full single-book
        duration. No unlock." Stats: "khepri_mantle: SEALED. No unlock condition
        in single-book timeline... Any trigger other than full-project-revision
        is a mechanics violation." References section lists no Earth-Bet
        cards in the actor's reference stack (only planetos cards referenced).
        No actor card in active-project/actors/ references an Earth-Bet persona
        or location card.
      why: ~

    - id: fault-008
      type: fault
      what: >
        cond-no-parahuman-infrastructure: library card is listed in the
        conditions INDEX as a library card but its physical file is not
        readable in cards/conditions/ — the file body cannot be accessed.
        Additionally, the warehouse copy was supposed to be provisioned from
        the library for this project but no physical file exists in
        active-project/warehouse/ (fault-001 covers this). Cannot verify
        the card body explicitly closes the Earth-Bet intrusion fence.
      why: >
        LAW: "Earth-Bet does not intrude. No portals open, no other capes
        appear, no Tinker tech is at hand." This is one of the four binding
        source-fact LAWs. Without a readable condition card encoding it, the
        fence exists only in world-notes.md and Taylor's actor card Khepri-mantle
        SEALED entry. That is insufficient enforcement at the condition-load
        layer for shoot and stitch phases.
      criteria: >
        cond-no-parahuman-infrastructure must be provisioned to
        active-project/warehouse/ as a physical file. Its body must encode:
        Earth-Bet parahuman infrastructure does not exist in Planetos; no
        Earth-Bet portals, no other capes, no Tinker tech; Taylor's Khepri-mantle
        being sealed is a consequence of this condition. The card must not
        contain any language implying the condition could lift or change within
        the book's scope.

    # ──────────────────────────────────────────────
    # AUDIT CLASS 10: SMALLFOLK-AS-SUBSTRATE DISCIPLINE
    # ──────────────────────────────────────────────

    - id: pass-015
      type: pass
      what: >
        World-notes LAW (OQ-7 resolved): "The block is hostile-and-indifferent,
        not soft-and-adopting. The reader holds the world as substrate, not
        as Taylor's community." Block-fixture card (oc-block-fixture): "EXPLICITLY
        DISCLAIMS CONFIDANT-ROLE. Not a community member. Not a voice for the
        block's perspective on Taylor. Not a resource Taylor uses or cultivates."
        Thematic Purpose for block-fixture: "World-going-on-without-Taylor,
        NOT community-Taylor-is-part-of." Taylor actor card: "The block is
        hostile-and-indifferent, not soft-and-adopting."
      why: ~

    - id: fault-009
      type: fault
      what: >
        cond-smallfolk-political-physics: library card listed in INDEX but
        physical file not readable (same access pattern as all condition cards).
        Warehouse copy absent (fault-001). Cannot verify the card encodes
        smallfolk-as-substrate, no community-Taylor-is-part-of dynamics,
        no protagonist-fodder framing.
      why: >
        LORE: "smallfolk number in the hundreds of thousands and live as
        substrate, not citizens." LAW (OQ-7): the block is hostile-and-indifferent.
        Without cond-smallfolk-political-physics in the warehouse, this
        structural requirement has no condition-card enforcement for the
        shoot and stitch phases.
      criteria: >
        cond-smallfolk-political-physics must be provisioned to
        active-project/warehouse/ as a physical file. If the existing library
        card body does not already encode: smallfolk are substrate not
        protagonist-fodder; no named-community-Taylor-is-part-of dynamics;
        block hostility and indifference as the default register — then a
        project addendum or override must add this language.

    # ──────────────────────────────────────────────
    # ADDITIONAL FINDINGS: INTERNAL CONSISTENCY CHECKS
    # ACROSS AVAILABLE ACTOR CARDS
    # ──────────────────────────────────────────────

    - id: pass-016
      type: pass
      what: >
        Mira card: death is ON-PAGE, late Act 3. This is consistent with
        world-notes LORE (OQ-7): "Her death in the Watch persons-risk sweep
        expansion is ON-PAGE in late Act 3." No contradiction between actor
        card and world-notes.
      why: ~

    - id: pass-017
      type: pass
      what: >
        Contact card (Daveth) Hard Fences: "Names Taylor as his source before
        dying (protocol, not betrayal)." This is consistent with world-notes
        LORE (OQ-6): "The contact killed in custody at Rung 6 names Taylor
        as his source before dying." No contradiction.
      why: ~

    - id: pass-018
      type: pass
      what: >
        Business-partner card (Corwyn Bane): Hard Fences encode "Present at
        Rung 4 — concrete mutual dependency shown [...] ABSENT at Rung 6 —
        not killed, not fleeing, simply not there; the reason is not dramatized."
        This satisfies the 1c-log dramatist condition S1 (concrete mutual
        dependency at Rung 4; absence-as-cost at Rung 6).
      why: ~

    - id: pass-019
      type: pass
      what: >
        Persons-risk officer card (Ser Rowan Vane): Hard Fence "Not cruel —
        procedurally correct throughout." This is consistent with world-notes
        LAW (OQ-7): "The antagonist is the patron-machinery itself [...] not
        in any person's choices." No contradiction.
      why: ~

    - id: pass-020
      type: pass
      what: >
        Steward card (Aldric Fenwick): Hard Fence "Does not harm anyone
        intentionally; applies correct tools for the category he received."
        Act 2 recurrence is "routine, not dramatic." This encodes the
        enforcement-overshoot seed mechanism (OQ-5, Rung 3) correctly as
        an inadvertent, category-limit-driven outcome, not deliberate harm.
      why: ~

    - id: pass-021
      type: pass
      what: >
        Septon card (Septon Aldyn): Hard Fence "Does not recant; holds the
        witch-classification." Watch management note limits action but not
        assessment. Three appearances total (arrival, one mid-book hostility
        beat, absent from close). This is consistent with OQ-7 cast-scope
        specification for the septon.
      why: ~

    - id: flag-003
      type: flag
      what: >
        Taylor actor card (library copy) variant-of field: "taylor-hebert-flea-bottom."
        The flea-bottom variant card has stats fauna_control_radius of "300m
        at story open [...] Expands organically through use toward hard ceiling
        of ~1.5km by late s2." The dragon-gate variant's range (~100–150m,
        hard constant) is dramatically different and explicitly documented
        as "significantly below flea-bottom-dance config due to different
        shard-seeding conditions in this world-arrival context." This AU
        divergence is documented and the variant-reason captures it. However,
        agents loading this card must not inherit the flea-bottom range from
        the parent. The card schema's variant-of: does not retire the base
        card (per schemas/card.schema.md §Variant cards), and the composition
        directive in the card's composes: field lists taylor-hebert-flea-bottom.
        Any agent that does composition without fully resolving the range
        override in favor of the dragon-gate variant's hard cap will import
        the parent's organic-expansion stat. This is a composition-logic risk,
        not a card-content error.
      why: >
        Flagging for screen-writer, coach, and facet pipeline: when loading
        taylor-hebert-dragon-gate, the dragon-gate Stats section fauna_control_radius
        (~100–150m hard constant) OVERRIDES the parent card's fauna_control_radius
        (300m, organic). The override is correctly encoded in the variant card.
        Risk surfaces only if an agent loads parent stats without applying
        the override.

    # ──────────────────────────────────────────────
    # CONDITION CARD INDEX QUALITY ASSIGNMENT FAULT
    # ──────────────────────────────────────────────

    - id: fault-010
      type: fault
      what: >
        cards/conditions/INDEX.md by_quality section: all 7 new project-scoped
        condition cards (cond-patron-dialect-operational-model,
        cond-watch-persons-risk-sweep, cond-kl-authority-dragon-gate-129ac,
        cond-fauna-control-rules-dragon-gate-addendum,
        cond-dragon-gate-arrival-and-witch-label,
        cond-series-tone-dragon-gate, cond-reincarnation-mechanics-dragon-gate)
        are NOT listed under by_quality. They appear only under by_world
        with "[project: dragon-gate-foreclosure — warehouse only]" notation.
        No quality (full/scant) is assigned to any of them in the INDEX.
      why: >
        Per schemas/card.schema.md §Card quality: "Any persona used on-stage
        must be quality: full. Scant + used = blocking rescue before cast entry."
        The quality gate applies to personas strictly, but condition cards
        without quality assignments are also unclassified — margit cannot
        assess load-readiness and agents cannot determine whether these cards
        have sufficient content for enforcement use. More significantly, the
        absence of quality assignments confirms these are stubs authored to
        INDEX only, not as full card files.
      criteria: >
        Each project-scoped condition card must receive a quality assignment
        in the INDEX at the time of physical file authoring. The 5 load-bearing
        constraint-encoding cards (cond-patron-dialect-operational-model,
        cond-watch-persons-risk-sweep, cond-fauna-control-rules-dragon-gate-addendum,
        cond-dragon-gate-arrival-and-witch-label, cond-series-tone-dragon-gate)
        should be quality: full. The remaining 2 (cond-kl-authority-dragon-gate-129ac,
        cond-reincarnation-mechanics-dragon-gate) may be quality: scant at
        margit's discretion if their constraint content is fully covered by
        world-notes and actor cards.
```
