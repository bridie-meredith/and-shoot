```yaml
audit:
  scope: chapter
  target: b01c17
  gate: /and-facets Phase 5 mechanical audit (flag-only, full-graph)
  timestamp: 2026-06-05
  headline: FINDINGS-PRESENT — HARD: 0 / SIGNAL: 9
  hard_to_proceed: 0
  note: >
    HARD count is 0. Chapter is clear to proceed to the audience-gate.
    Nine SIGNAL findings follow. None block. All are advisory or R2-resolvable.

  findings:

    - id: signal-001
      type: flag
      axis: RUBRIC-FIDELITY / FREQUENCY-BAND (vibes schema)
      what: >
        vibes entries :1 (@6), :2 (@7), :7 (@22), :10 (@34), :11 (@30) use keyword
        forms with interior spaces: "cold-utilitarian interiority" and "rising entrapment".
        The facet schema (facet.schema.md vibes section) requires "hyphenated index handle"
        for keyword fields. The hyphenated forms would be "cold-utilitarian-interiority"
        and "rising-entrapment". The pre-seeded keywords in Taylor's and Wren's vibes.md
        appear to have been stored with the space-form, so the ++ ops are internally
        consistent, but the keyword shape is malformed against schema.
      why: >
        A downstream cite-index builder or operator doing keyword-match lookup on
        "rising-entrapment" would miss entries indexed as "rising entrapment". The
        space-form creates a schema-drift risk across chapters if some entries use hyphens
        and others use spaces. If a future chapter authors "rising-entrapment" (hyphenated)
        as a new + keyword for an entity that already carries "rising entrapment" (spaced),
        the op-coherence gate will not catch the duplication.
      note: >
        No fixer criteria — this is a SIGNAL. Recommend: (a) confirm the pre-seeded
        keyword form in Taylor's and Wren's vibes.md; (b) if the source uses spaces,
        normalize all chapter files to the source form and treat as a known deviation
        from schema until the pre-seeded cloud is corrected; if the source uses hyphens,
        correct the five vibes entries at R2.

    - id: signal-002
      type: flag
      axis: STRUCTURAL (namespace)
      what: >
        The state-updates facet is split across two files (state-updates-env-b01-c17.md
        and state-updates-taylor-hebert-kl-122ac-b01-c17.md), both with IDs starting at
        1. Both files contribute to a single flat "state:" citation namespace in the
        proto-lines and cite-index. This produces non-unique IDs within the namespace:
        env:state:6 fires at @22 (norren-attribution: absent -> first-line-written) AND
        taylor:state:6 fires at @23 (social_tether_prot_collapse_axis: 8 -> 7). Both
        are cited as "state:6" in the proto-lines at their respective anchors. Similarly
        env:state:7 (@23) and taylor state:7 (@30) share the ID "state:7".
        At the per-anchor level these resolve without collision (no two same-ID entries
        fire at the same anchor from different files), but the cite namespace is
        non-unique across the chapter.
      why: >
        A stitcher or auditor resolving "state:6" without anchor context cannot
        determine which file's entry is meant. The cite-index header correctly reports
        "state=20" (13 env + 7 taylor = 20 entries), but the index itself lists only the
        flat "state:<id>" token, not the file-source. If the stitcher's state-lookup
        routine fetches by ID only (not by ID+anchor), it could retrieve the wrong entry.
        Risk is low given the per-anchor pattern but the namespace ambiguity is structural.
      note: >
        No fixer criteria — this is a SIGNAL. The per-anchor resolution is sufficient
        at stitch time provided the stitcher resolves by (anchor, state_id) pair. Flag
        for the stitcher's cite-lookup implementation. If multi-file state is a recurring
        pattern, consider namespacing by file (e.g., "state-env:<id>" / "state-taylor:<id>")
        in future chapters.

    - id: signal-003
      type: flag
      axis: FREQUENCY-BAND (PILE-UP)
      what: >
        Three bones carry more than 4 co-located facet entries:
        @22 — 6 entries: narrator:5, state:3 (taylor), state:4 (taylor), state:6 (env),
              vibes:5, vibes:7
        @23 — 6 entries: narrator:6, state:5 (taylor), state:6 (taylor), state:7 (env),
              vibes:6, vibes:8
        @29 — 7 entries: exposition:1, loc-state:6, state:9 (env), state:10 (env),
              state:11 (env), vibes:16, vibes:17
      why: >
        At @22/@23: The density is structurally justified — these are the chapter's
        declared peak bones (collapse-cascade co-fire + false-attribution write); the
        dual state-updates files (env + taylor) each legitimately fire at the peak, and
        NI + vibes are both load-bearing. The stitcher Phase 1 fold-in will receive
        simultaneous signals from six facets on two adjacent bones; if any two signals
        point in different tonal directions, the stitcher's render will need to arbitrate.
        At @29: The three-day skip + scene-D open fires three structural env state entries
        (time + location + dead-drop-channel) simultaneously with loc-state, exposition,
        and two vibes. The scene-open bone carries the full scene-transition payload.
        Pile-up density is explained by structural co-fires, not decoration inflation,
        but the stitcher signal density is above the comfortable ceiling.
      note: >
        No fixer criteria — SIGNAL. Advisory for the stitcher: at @22/@23, the two
        vibes per bone are tonal modifiers (atonement-as-repetition + rising-entrapment
        for Taylor; protected-by-falsification + act-site for Wren/location) — they do
        not conflict with NI, they reinforce it. At @29, the scene-bridge exposition
        renders first (scene-open-orient), then loc-state, then the data-return bone —
        the facet ordering insulates the scene-open from signal collision.

    - id: signal-004
      type: flag
      axis: STRUCTURAL / CONSTRAINT (exposition fire-rule)
      what: >
        exposition:1 @29 carries scope: scene-open-orient. The schema's conditional
        fire-rule for scene-open-orient (facet.schema.md) states condition (b): "loc-state
        does NOT fire at the scene-open anchor (loc-state at-establishment carries the
        time/place; if it fires, the scene-orient is wallpaper)." loc-state:6 fires at
        @29 with content: "the-gap-lanes-east-water-gate | morning | none |
        corridor-open, ward-foot-traffic-active". Condition (b) is therefore triggered —
        loc-state fires at the same anchor.
      why: >
        The fire-rule condition (b) is technically violated. However the condition's
        rationale ("loc-state carries the time/place; scene-orient is wallpaper") does
        not hold here: loc-state:6's rendered line contains "morning" and the corridor
        conditions but does NOT carry the three-day interval. The three-day gap between
        scene-C (night deployment) and scene-D (cost-settle) is the genuine reader gap
        licensed by ctx-001 (context-ledger CONTEXT-REQUIRED carry from bones-review
        follow_check PASS-WITH-NOTES). The exposition entry is non-wallpaper because
        loc-state does not carry the interval duration.
        The tension is: the fire-rule's letter (condition b triggers) vs its spirit
        (loc-state actually carries the content). ctx-001 resolves the anti-exposition
        penalty exemption but does not explicitly override condition (b) of the fire-rule.
      note: >
        No fixer criteria — SIGNAL. The ctx-001 licensing is adequate and the entry is
        substantively non-wallpaper. Recommend the R2 pass confirm that ctx-001 is
        understood as overriding condition (b) as well as the penalty; or alternatively,
        document that condition (b) applies only when loc-state fully carries the
        time-passage content (which it does not here). This distinction should be recorded
        in the exposition fire-rule commentary for future chapters.

    - id: signal-005
      type: flag
      axis: RUBRIC-FIDELITY (state-updates POV co-citation)
      what: >
        state-updates-taylor entry 2 (@21, capability_axis 7.5 -> 8.0) carries the
        annotation "co-cite narrator-interest @22-cluster (deployment spine), NI:5 @22."
        NI:5 is anchored at @22, not @21. The rubric-state-updates §3 cross-facet
        contract requires POV co-citation; all other taylor state entries co-cite NI at
        the same anchor (@12/NI:3 @12, @22/NI:5 @22, @22/NI:5 @22, @23/NI:6 @23,
        @30/NI:7 @30). State entry 2 at @21 is the only entry where the NI co-cite
        fires at an adjacent anchor rather than the same anchor.
      why: >
        If the cross-facet contract requires same-anchor co-citation, state:2 @21 fails
        the test. The narrative logic is coherent — @21 (opens the Norren entry-cluster,
        capability first concrete deployment step) and @22 (writes the first attribution
        line, NI:5 full interiority) are sequentially adjacent peak-spine bones, and the
        capability delta at @21 is preparatory to the NI moment at @22. But the rubric's
        mechanical test is anchor-match. If the rubric reads "co-citation" as
        "same-anchor NI entry exists," this entry fails; if it reads "NI entry covers
        the same narrative event cluster," this entry passes.
      note: >
        No fixer criteria — SIGNAL. Rubric-state-updates §3 should be consulted at R2
        to confirm whether cluster-level co-citation satisfies the cross-facet contract.
        If same-anchor is required, state:2 @21 needs an NI entry at @21 (or the
        capability delta should be moved to @22). If cluster-level is acceptable, the
        author's annotation is sufficient.

    - id: signal-006
      type: flag
      axis: STRUCTURAL (frontmatter consistency)
      what: >
        exposition-b01-c17.md frontmatter carries "episode: b01-c17" (dashed form).
        All other facet files for this chapter use the undashed slug "b01c17":
        location-state (episode: b01c17), interest-narrator (episode: b01c17),
        sensory (episode: b01c17), state-updates-env (no episode field), state-updates-
        taylor (no episode field), memory (episode: b01c17), feeling (episode: b01c17),
        metaphor (episode: b01c17), vibes (episode: b01c17), scene-map (scene-map: b01c17).
        The dispatch note specifies "facet headers use episode: b01c17 (undashed) — accept
        as valid." The dashed form in exposition is inconsistent with all other files.
      why: >
        A downstream parser matching episode slugs by string comparison will see "b01-c17"
        and "b01c17" as different keys. Cross-episode cite-index tools that group by
        episode slug will split this file from its siblings. Low risk at stitch time
        (stitcher reads files by path, not by frontmatter slug), but creates ambiguity
        for any audit or reporting tool that aggregates by episode slug.
      note: >
        No fixer criteria — SIGNAL. Normalize to "b01c17" at any convenient pass.

    - id: signal-007
      type: flag
      axis: RUBRIC-FIDELITY (memory monument-card resolution)
      what: >
        memory:2 (@16) and memory:3 (@36) use free-text glosses as target references
        rather than margit-resolved monument-* card slugs:
        mem:2 target: "the architecture-she-came-to-set-down (override-as-shape; no proper noun)"
        mem:3 target: "the prohibition-arrived-with: present-as-refusal, enacted-as-protection"
        The memory facet schema (facet.schema.md) allows "a free-text gloss when no formal
        target exists yet." The author self-flagged this in the facet header.
      why: >
        These memory callbacks are to the chapter's central structural argument (the
        override-architecture prohibition Taylor carried across from Earth-Bet). Monument
        cards for this architecture are not yet in the cards/ library. Without monument
        slugs, downstream cross-chapter memory tracking (which callbacks across the book
        reference the same monument) must be done by semantic matching rather than
        slug-lookup. The fence is clean (no Earth-Bet proper nouns in either gloss). This
        is an authoring gap, not a constraint violation.
      note: >
        No fixer criteria — SIGNAL, per rubric-memory-flags monument-card-resolution-test
        (self-flagged by author as SIGNAL). Margit referral to author monument cards for
        the override-architecture prohibition and the architecture-she-came-to-set-down
        construct; resolve at next margit pass or chapter book-close.

    - id: signal-008
      type: flag
      axis: RUBRIC-FIDELITY (vibes op-coherence — Wren pre-seed unverifiable)
      what: >
        vibes:2 (@7), vibes:9 (@27), and vibes:11 (@30) use the ++ op for
        actor:wren-stitch-maker-flea-bottom-ward keywords "rising entrapment" (vibes:2,
        vibes:11) and "tragic-causal" (vibes:9). The ++ op requires the keyword to already
        exist in the target entity's vibe-set. The chapter contract header confirms Taylor's
        pre-seeded keywords (cold-utilitarian-interiority / atonement-as-repetition /
        rising-entrapment / tragic-causal) but does not explicitly confirm Wren's
        pre-seeded keywords. The author's note states "Fresh + only on new targets
        (Wren / locations / episode-scope)" — but then uses ++ for Wren's
        rising-entrapment and tragic-causal, which implies these ARE pre-seeded for Wren
        from prior chapters. Wren's vibes.md was not read at this audit pass.
      why: >
        If rising-entrapment and tragic-causal are not pre-seeded for Wren in her vibes.md,
        these should be + (new keyword) not ++ (extend existing). A ++ op on a non-existent
        keyword is an op-coherence failure (gate-2). If they are pre-seeded (from Wren's
        appearances in b01c01 and other chapters), the ++ ops are correct.
      note: >
        No fixer criteria — SIGNAL. Verify Wren's vibes.md carries rising-entrapment and
        tragic-causal as pre-seeded keywords from prior chapter authoring. If confirmed,
        signal resolves. If not, vibes:2/:9/:11 need their ops changed from ++ to +.

    - id: signal-009
      type: flag
      axis: STRUCTURAL (env state seams — R2 open)
      what: >
        state-updates-env-b01-c17.md carries five author-flagged SEAM items:
        SEAM-C17-ENV-001: prop:oc-coverage-log first-touch — old-state "absent" and
          "writing-active" are inferred, no prior card exists; reconcile with
          prop:oc-coverage-record from b01c15.
        SEAM-C17-ENV-002: studio.dead-drop-channel.query-status old-state "active" is
          inferred from s01 channel-delivery; no prior explicit state record.
        SEAM-C17-ENV-003: prop:apparatus-picture — new prop, no prior card; slug inferred
          from scene-map.
        SEAM-C17-ENV-004: prop:cost-ledger — possible identity with prop:oc-feed-ledger
          from b01c12-b01c14; margit referral needed.
        SEAM-C17-ENV-005: studio.location @29 old-state "the-tallow-render-works" — the
          three-day skip implies an off-screen transit from tallow-render-works to
          gap-lanes; no intervening location-change bone.
      why: >
        Four new props / field extensions without margit-authored cards mean the state
        tracker has unregistered entities. If future chapters reference prop:oc-coverage-log
        or prop:apparatus-picture, those references will have no authoritative card to
        validate against. The SEAM-C17-ENV-005 location gap (@29 old-state) is the
        most structurally significant: if the canonical location state at chapter-close
        of s03 is the-tallow-render-works, and @29 fires "the-tallow-render-works -> the-
        gap-lanes-east-water-gate" on the scene-open bone, the three-day transit is
        implied-off-screen. This is a common pattern for time-skips but should be
        confirmed at R2 as the correct anchor for the location flip.
      note: >
        No fixer criteria — SIGNAL. All five are author-flagged for R2 resolution. The
        margit referrals (new cards for prop:oc-coverage-log, prop:apparatus-picture,
        prop:cost-ledger, studio.dead-drop-channel field-extension) should be dispatched
        before the book-close state-write-back. SEAM-C17-ENV-005 should be confirmed at
        R2 as the correct off-screen transit anchor.
```
