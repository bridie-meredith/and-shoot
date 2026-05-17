```yaml
audit:
  scope: series
  target: dragon-gate-foreclosure / series-plan gate
  timestamp: 2026-05-17
  findings:

    # ──────────────────────────────────────────────
    # CLASS 1: OQ → SERIES-PLAN CONSISTENCY
    # ──────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        OQ-1 (range cap): series-plan.md LAW block correctly states "range-capped
        to ~one city block (~100–150m, hard constant). Khepri-vector inert. AU
        divergence must be legible in prose." Matches world-notes LAW (OQ-1).
        No contradiction.
      why: ~

    - id: pass-002
      type: pass
      what: >
        OQ-2 (arrival + witch-label): series-plan.md Plot "Start" matches
        world-notes verbatim — mid-market-fire, three gold cloaks, septon shouts
        "witch," held overnight, released as "lunatic-not-worth-paperwork." LAW
        block encodes witch-label as permanent operational infrastructure, never
        lifted, never corrected. Matches world-notes LAW (OQ-2).
      why: ~

    - id: pass-003
      type: pass
      what: >
        OQ-3 (time window + back-loaded compression): series-plan.md states
        arrival 126 AC late summer; 36-month back-loaded compression with
        three-act structure matches world-notes LAW (OQ-3). Act 1/2/3 boundary
        months (M12, M26, M28–36) match. Recognition-failure beat at M27–28 is
        present as Rung 6 in the ladder. Viserys off-page near M36 is consistent.
      why: ~

    - id: pass-004
      type: pass
      what: >
        OQ-4 (faction proximity): series-plan.md correctly records Watch-track
        via captain; Hightower-controlled promotion channels; Green-adjacent
        one-remove; captain opaque. Matches world-notes LAW (OQ-4).
      why: ~

    - id: pass-005
      type: pass
      what: >
        OQ-5 (patron-dialect model + 6-rung ladder): series-plan.md Plot block
        contains the full 6-rung ladder with correct month markers, patron
        channels, and outcome labels. M14–15 enforcement-overshoot (REQUIRED
        ENFORCEMENT-OVERSHOOT BEAT) is present. M18–19 Mira-rung correctly
        shows model "working" on someone she cares about. M27–28 recognition-
        failure (RECOGNITION-FAILURE BEAT) is correctly encoded. LAW block encodes
        C4 prohibition ("model-falsification meta-statement MUST NEVER appear in
        prose"). Matches world-notes LAW (OQ-5).
      why: ~

    - id: pass-006
      type: pass
      what: >
        OQ-6 (closing shape): series-plan.md End entry matches world-notes
        verbatim — Taylor processed by Watch sweep, captain signs paperwork, dies
        in guardhouse, not executed not martyred, processed. Final image: insects
        at range-cap registering no movement inside the building. Viserys off-page;
        war begun off-page. Matches world-notes LAW (OQ-6).
      why: ~

    - id: pass-007
      type: pass
      what: >
        OQ-7 (cast scope): series-plan.md cast roster lists 9 named recurring
        with correct function tags and 2 off-page canon references (otto-hightower,
        viserys-i-targaryen). "Off-page (cards exist; NOT in active-project/actors/)"
        note is explicit. All match world-notes LORE (OQ-7). No named family for
        Mira or contact listed. No canon figure given on-page speech. Canon
        carriage glimpse is recorded as Act 2; Viserys as street-crier. Matches
        LAW (OQ-7).
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 2: MEMORY-WRITE COMPLETENESS
    # ──────────────────────────────────────────────

    - id: pass-008
      type: pass
      what: >
        memory.md series block contains: theme (1 line), laws (10 items), lore
        (3 items), behaviors (3 items), plot (start / end / protagonist_arc /
        series_question — all populated, no ~ placeholders), cast_roster (9
        slugs), off_page_canon (2 slugs), stage_elements (5 slugs). No mandatory
        schema field carries a ~ placeholder.
      why: ~

    - id: fault-001
      type: fault
      what: >
        memory.md seasons block: the s01 entry has `slug: s01` and `chunk:` but
        is missing the `status:` field. The showrunner-memory.schema.md format
        explicitly lists `status: active | complete | planned` as a named field
        on season entries. The s01 entry contains only two keys (slug, chunk);
        status is absent.
      why: >
        `/and-season s01` Phase 0 and Phase 1 read the seasons block to determine
        whether a season is active/planned/complete. An absent status field means
        the season entry is schema-incomplete and may not be machine-parseable at
        `/and-season` dispatch. At minimum it creates ambiguity about whether s01
        has been started, planned, or is fresh.
      criteria: >
        The s01 entry in memory.md seasons block must include a `status:` field
        with value `planned` (the correct state at series-plan completion,
        pre-/and-season).

    # ──────────────────────────────────────────────
    # CLASS 3: NO-TITLE DISCIPLINE
    # ──────────────────────────────────────────────

    - id: pass-009
      type: pass
      what: >
        series-plan.md heading is "Series Plan — Dragon Gate Foreclosure
        (one-book series)" — this is a document heading, not a title field.
        The document body carries "Slug-only references throughout (no titles)"
        as an explicit discipline note. The s01 section heading is "s01 (only
        season; this is a one-book series)" — slug only, no title. memory.md
        seasons entry has `slug: s01` only. No title field present in either
        document at series or season level.
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 4: CAST ROSTER RECONCILIATION
    # ──────────────────────────────────────────────

    - id: pass-010
      type: pass
      what: >
        series-plan.md cast roster: 9 named recurring slugs. memory.md
        cast_roster: 9 slugs — all 9 match series-plan exactly. 1c-log final
        cast: 9 actor directories in active-project/actors/ — all 9 slugs
        confirmed. Off-page references (otto-hightower, viserys-i-targaryen)
        are in memory.md off_page_canon, not in cast_roster. No mismatch
        across series-plan / memory / actor directories.
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 5: STAGE ELEMENTS RECONCILIATION
    # ──────────────────────────────────────────────

    - id: pass-011
      type: pass
      what: >
        series-plan.md stage elements: 5 location slugs (loc-dragon-gate-block,
        loc-dragon-gate-guardhouse, loc-miras-workshop, loc-black-adjacent-contact-
        premises, loc-dragon-gate-market-alley). memory.md stage_elements: same
        5 slugs. 1c-log "Locations provisioned to active-project/warehouse/":
        same 5 slugs, all labeled as "new authorings (all required)." Full
        three-way match.
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 6: CHUNK-STATEMENT FORMAT COMPLIANCE
    # ──────────────────────────────────────────────

    - id: pass-012
      type: pass
      what: >
        series-plan-log Attempt 2: screen-writer produced revised two-sentence
        chunk; dramatist ACCEPT confirmed sentence one names structural collision
        (patronage chain harvesting infrastructure it appears to commission),
        sentence two names what it produces and what cannot survive (the closed
        loop). The chunk in series-plan.md matches the Attempt 2 text verbatim,
        word for word. Memory.md seasons[s01].chunk also matches verbatim. Two
        sentences. External, structural. No psychology.
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 7: EXECUTION-OBLIGATION COMPLETENESS
    # ──────────────────────────────────────────────

    - id: pass-013
      type: pass
      what: >
        series-plan.md "Execution obligations carried into all downstream
        production" lists 11 items numbered 1–11 with source citations.
        Cross-reference against 1b-log binding conditions and OQ decisions:
        item 1 maps to OQ-6 insect-ambient obligation; item 2 to OQ-5/C3/OQ-7/E3
        Mira credibility; item 3 to OQ-7/E1 steward tracking; item 4 to OQ-4
        Hightower architecture doubled-accumulation; item 5 to OQ-5/C4
        model-falsification prohibition; item 6 to lit-snob round 10 road-to-hell
        vocabulary; item 7 to OQ-7/E1 captain opacity; item 8 to OQ-5/C1
        enforcement-overshoot; item 9 to OQ-5/C2 falsification-on-belief; item
        10 to 1c-log/S1 business-partner concrete dependency; item 11 to OQ-2
        witch-label permanence. All 11 are retrievable and traceable to upstream
        audience/dramatist decisions.
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 8: SERIES-LEVEL FENCE AGAINST /AND-SEASON SCOPE CREEP
    # ──────────────────────────────────────────────

    - id: pass-014
      type: pass
      what: >
        series-plan.md s01 section contains: (1) the two-sentence chunk
        statement; (2) a "Season scope" sentence that explicitly delegates drama
        statement, vibe-cloud delta, and content beats to "/and-season s01
        Phase 1." No drama statement for s01 appears in series-plan.md. No
        vibe-cloud delta is present. No content beats (scene- or episode-level)
        appear. The series-plan correctly delineates its own scope boundary.
      why: ~

    # ──────────────────────────────────────────────
    # CLASS 9: SCHEMA FENCE
    # ──────────────────────────────────────────────

    - id: pass-015
      type: pass
      what: >
        series-plan.md: document structure is well-formed prose with clearly
        delimited sections matching the series-plan companion document description
        in showrunner-memory.schema.md (theme, laws, lore, behaviors, seasons,
        execution obligations). No broken yaml blocks; no missing mandatory
        sections; no ~ placeholders in content fields.
      why: ~

    - id: pass-016
      type: pass
      what: >
        memory.md: YAML structure is valid. All mandatory top-level keys present
        (routing, series, seasons, active). routing fields populated correctly
        (season_plan: ~ is appropriate pre-/and-season). active.season and
        active.episode are ~ which is correct at series-plan completion before
        /and-season runs. No broken YAML blocks detected.
      why: ~

    # fault-001 (seasons.status) is already filed under CLASS 2 above.
    # It also counts as a schema fence finding; no duplicate entry needed.
```
