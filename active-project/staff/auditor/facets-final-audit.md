```yaml
audit:
  scope: chapter
  target: b01c16
  timestamp: 2026-06-04
  gate: /and-facets Phase 5 — mechanical cross-cutting facet audit

  findings:

    # ── CLASS 1: STRUCTURAL ────────────────────────────────────────────────────

    - id: fault-001
      type: pass
      what: "Bones 1-27 all present in proto-lines. Every [prefix:id] token on every proto-line resolves
        to a facet entry. Full forward walk: [state:1-12], [loc-state:1-5], [sensory:1-2], [narrator:1-7],
        [memory:1], [feeling:1-3], [vibes:1-4], [septon-halvard-flea-bottom:1-2] — all resolve.
        Reverse walk: every facet entry has a corresponding proto-line token. Per-facet ID monotonicity
        confirmed across all facets."
      why: "Structural integrity PASS."

    # ── CLASS 2: EARTH-BET FENCE ──────────────────────────────────────────────

    - id: fault-002
      type: pass
      what: "Full scan of all facet files and both dialogue utterances for: Khepri, Skitter, Brockton,
        Gold-Morning, Scion, cape, shard, parahuman, PRT. Exposition file self-declares CLEAN.
        Dialogue utterances are purely Westerosi register (Muggers' Row, fishmonger's lane, sennight).
        Zero hits across all files."
      why: "Earth-Bet HARD fence: 0 violations."

    # ── CLASS 3: SCENE-MAP COVERAGE ───────────────────────────────────────────

    - id: fault-003
      type: pass
      what: "scene-map frontmatter: 27 bones / 3 scenes. Ranges: scene-A @1-@8 (8 bones) + scene-B
        @9-@18 (10 bones) + scene-C @19-@27 (9 bones) = 27. No gaps, no overlaps. Totals match header."
      why: "URI-SCENE-WINDOW PASS."

    # ── CLASS 4: DIALOGUE ─────────────────────────────────────────────────────

    - id: fault-004
      type: pass
      what: "Proto-line @10 carries [septon-halvard-flea-bottom:1] and @17 carries [septon-halvard-flea-bottom:2].
        Dialogue file has exactly 2 entries, both with stated objectives. Utterance 1 names specific
        survivors, disclaims the count, offers no alternative. Utterance 2 explicitly disclaims any
        demand to do differently. No accusation, no claim of knowing what Taylor is, no theological
        jargon. behavior-card: westeros-septon fences satisfied."
      why: "Dialogue coverage and card-compliance PASS."

    # ── CLASS 5: CONSTRAINT / RUBRIC-FIDELITY ─────────────────────────────────

    - id: fault-005
      type: pass
      what: "State-updates actor:taylor axis rank-movers and NI co-citation: state:5 @19
        (moral_legibility 4→4.5) co-cites narrator:5 @19 ✓. state:8 @27 (position) co-cites
        narrator:7 @27 ✓. state:6 @21 (halvard_engagement_state: engaged→foreclosed) is a
        behavioral-label state, not an independent substance-axis rank-mover; the moral_legibility
        rank-mover for @21 is already covered by state:5 @19 (split +0.25 stop / +0.25 turn per
        scene-map) with NI at @19. No co-citation gap on substance axes."
      why: "NI co-citation for POV axis rank-movers PASS."

    - id: fault-006
      type: pass
      what: "Vibes licensed-by anchors: vibes:1 (proto:21/17/26, memory:1), vibes:2 (proto:23/24/27),
        vibes:3 (proto:21/19/20, feeling:1), vibes:4 (proto:27/25) — all citations resolve to
        present proto-line or facet entries."
      why: "Vibes licensed-by PASS."

    - id: fault-007
      type: pass
      what: "loc-state entries: all 5 use descriptive state-change parentheticals, not action
        verbs in the state-description field. Transitional-verb rubric satisfied."
      why: "loc-state verb-class PASS."

    - id: fault-008
      type: flag
      what: "memory:1 @10 cites '-> e07:halvard-corner-first-counter' as a cross-episode
        callback to the first Halvard corner encounter (c07/c09/c13 trail). The 'e07' slug is a
        production-internal reference; it does not resolve to any same-chapter bone or active
        warehouse card. The exposition file independently confirms this as an established
        cross-episode register notation, not a new entity. Dispatch instruction: accept as
        legitimate cross-episode memory gloss; SIGNAL at most."
      why: "The e07 slug is unresolvable by a reader consulting only the b01c16 facet set —
        a downstream reader cannot verify the prior-chapter anchor without consulting earlier
        chapter records. Not a structural failure because the memory entry is a callback gloss,
        not a cite-index dependency. Advisory only."

    # ── CLASS 6: FREQUENCY-BAND ───────────────────────────────────────────────

    - id: fault-009
      type: flag
      what: "NI density: 7/27 = 25.9%. Band ceiling 25%. Marginal overage: +0.9% (1 entry over
        the ceiling; the 27-bone short-chapter compounds the ratio)."
      why: "Advisory. One additional NI entry on a longer chapter would be within band; the short
        chapter tightens the ratio mechanically. Not a structural failure; SIGNAL per dispatch."

    - id: fault-010
      type: flag
      what: "Sensory density: 2/27 = 7.4%. Band 3-6%. Short-chapter exception applies (27-bone
        chapter; 2 entries is minimal absolute coverage). Both entries are structurally warranted
        onset inflections (tallow-wax @6, fence-rail cold-iron @13)."
      why: "Advisory. No grounding-ledger license required for 2 entries — the short-chapter
        disposition mitigates. SIGNAL per dispatch."

    - id: fault-011
      type: flag
      what: "Feeling density for septon-halvard-flea-bottom: 2 entries (feeling:2 @15, feeling:3 @26)
        out of 27 bones = 7.4%. Band ≤5%/char. Marginal overage."
      why: "Advisory. Both entries are somatic physical-register (weight-even stance @15,
        face-to-eaves-line @26), partial expressed. The two-entry disposition is borderline for a
        non-POV character who is the chapter's named counterpart across all three scenes. SIGNAL
        per dispatch."

    # ── CLASS 7: CURVE-SHAPE ──────────────────────────────────────────────────

    - id: fault-012
      type: pass
      what: "scene-map rhythm-shapes: scene-A 'falling-arc establishment,' scene-B 'falling —
        chapter's pressure-peak,' scene-C 'falling-arc climax-then-fall.' Substance dramatic_shape:
        falling. Arc coherent: arrival/geometry → counter-delivered/arithmetic-visible → walk-away/
        foreclosure-complete → circuit-resumed-unchanged. Peak at scene-C walk-away, fall into
        unchanged environment. No curve mismatch."
      why: "CURVE-SHAPE coherent with falling dramatic_shape. SHAPE-OK."

    # ── SUMMARY ───────────────────────────────────────────────────────────────

    - id: summary-001
      type: pass
      what: "HARD count: 0. SIGNAL count: 4 (fault-008 memory cross-episode gloss unverifiable
        from chapter-local files; fault-009 NI 25.9% marginally over 25% ceiling; fault-010 sensory
        7.4% over 6% ceiling, short-chapter; fault-011 Halvard feeling 7.4% over 5%/char ceiling).
        Headline: CLEAN."
      why: "Phase 5 gate clears. HARD=0 satisfied."
```
