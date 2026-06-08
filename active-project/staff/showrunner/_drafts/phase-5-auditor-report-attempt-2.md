audit:
  scope: series
  target: series
  timestamp: 2026-05-24
  findings:

    # ── SCHEMA CONFORMANCE ──────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        v2 state_axes — all twelve entries carry unique slugs.
        No slug appears more than once across all entries.
        fault-001 (SCHEMA-SLUG-COLLISION) is resolved.
      why: n/a
      criteria: n/a

    - id: pass-002
      type: pass
      what: >
        All 21 cost_ledger entries carry singular gain and singular cost.
        No comma-separated multi-axis gain or cost strings present.
        fault-002 (SCHEMA-GAIN-MULTI-AXIS) and fault-003 (SCHEMA-COST-MALFORMED) are resolved.
      why: n/a
      criteria: n/a

    - id: pass-003
      type: pass
      what: >
        All cost_ledger entries carry anchor: { book: b01, chapter: null, scene: null }.
        Schema requires "/and-substance series writes anchor.book only" — all 21 entries conform.
      why: n/a
      criteria: n/a

    - id: pass-004
      type: pass
      what: >
        cl07c cost field uses opportunity-missed form. Schema line 130 permits
        opportunity-missed:<one line>. The [HIGH = WORST ...] annotation is embedded
        inline in the cost string value, not in a separate schema-undefined field.
        No separate cost_note field exists in the schema; the annotation is syntactically
        conformant as a string value.
      why: n/a
      criteria: n/a

    # ── COST-LEDGER INTEGRITY ───────────────────────────────────────────────

    - id: pass-005
      type: pass
      what: >
        LEDGER SUM RECONCILIATION table verified against actual cost_ledger entries.
        All twelve axes reconcile:

        capability: cl01a(+1) + cl03a(+3) + cl05(+2) = +6; declared +6. EXACT.
        moral_framework: cl02(−3) + cl03a(−2) + cl-d06(−1) + cl05(−1) = −7;
          declared arc +6 (rank 2→8); −7 within ±1 tolerance. WITHIN TOLERANCE.
        position-prot-rise: cl02(+4) + cl-d07a(+2) = +6; declared +6 (1→7). EXACT.
        position-prot-collapse: cl07b cost (−6); declared −6 (7→1). EXACT.
        relational_anchor_status: cl-d06(+2) + cl-d08(+2) + cl04(+3) + cl-d11(+1) = +8;
          declared +8 (1→9). EXACT.
        moral_legibility_to_self: cl07a(+4); declared +4 (4→8). EXACT.
        political_register-prot: cl-d05(+3) + cl06(+5) = +8; declared +8 (1→9). EXACT.
        social_tether-prot-rise: cl01b(+2) + cl03b(+4) + cl-d08b(+1) = +7;
          declared +7 (1→8). EXACT.
        social_tether-prot-collapse: cl07a cost (−7); declared −7 (8→1). EXACT.
        social_tether-antag: cl-antag-d03(+4) + cl-antag-d10(+4) = +8;
          declared +8 (1→9). EXACT.
        position-world: cl-world-d04(+2) + cl07b(+2) = +4; declared +4 (5→9). EXACT.
        political_register-world: cl-world-d07(+2) + cl07c(+2) = +4;
          declared +4 (5→9). EXACT.

        fault-004 (COST-LEDGER-DELTA-MISMATCH) is resolved on all four previously
        flagged axes.
      why: n/a
      criteria: n/a

    # ── REFERENCE INTEGRITY ─────────────────────────────────────────────────

    - id: pass-006
      type: pass
      what: >
        All axis-slug references in cost_ledger gain fields resolve to declared
        state_axes[].slug entries. All axis-slug references in cost fields with
        axis-cost form resolve to declared slugs. All journey-required references
        name valid cost_ledger entry IDs (cl01a, cl03a, cl03b, cl02, cl-d08 —
        all present). All antagonist_pressure axis fields resolve to declared slugs.
        Zero dangling references.
      why: n/a
      criteria: n/a

    # ── RANK-CAUSE COHERENCE ────────────────────────────────────────────────

    - id: pass-007
      type: pass
      what: >
        Rise+collapse axis pair handoff ranks are consistent.
        position-prot-rise end_rank (7) equals position-prot-collapse start_rank (7). Match.
        social_tether-prot-rise end_rank (8) equals social_tether-prot-collapse
        start_rank (8). Match.
        No handoff gap or overlap present.
      why: n/a
      criteria: n/a

    - id: pass-008
      type: pass
      what: >
        Trajectory anchors for the eight previously-existing ledger entries (cl02, cl03a,
        cl03b, cl04, cl05, cl06, cl07a, cl07b) are unchanged from attempt-1 and remain
        verified against series-trajectory.md.
      why: n/a
      criteria: n/a

    - id: pass-009
      type: pass
      what: >
        New trajectory anchors verified for: cl-d05 (d05), cl-d06 (d06), cl-d07a (d07),
        cl-d08 (d08), cl-d11 (d11), cl-world-d04 (d04), cl-world-d07 (d07),
        cl-antag-d03 (d03), cl-antag-d10 (d10).

        cl-d05 → d05: trajectory shifts political_register_toward_elite
          neutral→readable-resentment; cl-d05 +3 (1→~4) consistent with resentment onset.
        cl-d06 → d06: trajectory d06 cause states "she begins choosing which trades to
          rationalize by asking whether they keep the network intact" — moral_framework
          fracture; relational_anchor_status shift explicitly declared. Both claims supported.
        cl-d07a → d07: trajectory d07 shifts position to Otto's-unofficial-instrument;
          cl-d07a +2 closes position-prot-rise to 7; opportunity-missed cost maps to
          Otto naming the arrangement explicitly as described in d07 cause.
        cl-d08 → d08: trajectory d08 shifts relational_anchor_status to
          load-bearing-in-network; cl-d08 +2 and cost referencing cl03b both map to
          d08 cause description of [cost-bearer] as coverage-map anchor.
        cl-d11 → d11: trajectory d11 shifts relational_anchor_status and
          moral_legibility_to_self; cl-d11 +1 and opportunity-missed cost map directly
          to d11 cause describing Taylor screening the use-vector as "protection."
        cl-world-d04 → d04: d04 cause describes network build delivering intelligence
          to Otto; position-world +2 is a direct consequence; shifts block does not
          declare a world axis but cause content strongly supports the inference.
        cl-world-d07 → d07: d07 cause describes Otto formalizing the arrangement and
          Taylor delivering faction intelligence; political_register-world +2 is a
          consequence of Green succession channel solidifying; shifts block does not
          declare a world axis but cause content supports the inference.
        cl-antag-d03 → d03: d03 cause describes Taylor accepting the offer; Otto gains
          leverage proportional to the acceptance; social_tether-antag +4 is coherent
          with d03 cause even though d03 shifts block does not name an antagonist axis.
        cl-antag-d10 → d10: d10 cause states Taylor cannot withdraw and is too
          load-bearing; this is the non-extractable confirmation that directly anchors
          social_tether-antag final structural leverage.

        All trajectory claims supported.
      why: n/a
      criteria: n/a

    # ── FLAGS ───────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: >
        cl-d08b (social_tether-prot-rise +1 at d08) trajectory anchor is inferential.
        series-trajectory.md d08 shifts block declares "relational_anchor_status:
        structurally-at-risk → load-bearing-in-network" only. No social_tether shift
        is declared in the d08 shifts block. The cl-d08b entry allocates social_tether-prot-rise
        +1 at d08 on the basis of [cost-bearer]'s free movement consolidating the tether —
        this reading is supported by the d08 cause narrative but is not trajectory-shift-declared.
        The +1 is arithmetically required to close the social_tether-prot-rise ledger sum
        to +7 (declared); without it, the sum is +6 (1 under declared).
      why: >
        If series-trajectory.md is treated as the authoritative shifts source,
        cl-d08b lacks a trajectory-declared anchor. This will not cause a schema violation
        but may cause /and-substance book Phase 3 to question the cl-d08b allocation when
        the d08 chapter contract is authored — the trajectory's shifts block is what
        Phase 3 reads to establish which axes are in motion at each delta. The +1 may be
        challenged as unanchored at that phase if the reviewer works from shifts blocks
        rather than cause narratives.
      criteria: n/a

    - id: flag-002
      type: flag
      what: >
        Slug naming convention is hybrid across the twelve state_axes entries. Base slugs
        that are non-suffixed use underscores throughout: moral_framework, capability,
        relational_anchor_status, moral_legibility_to_self. Perspective-suffixed slugs
        use hyphens to separate the suffix from the base, but the base component retains
        underscores: political_register-prot, political_register-world, social_tether-prot-rise,
        social_tether-prot-collapse, social_tether-antag. Fully-hyphenated slugs omit
        underscores entirely: position-prot-rise, position-prot-collapse, position-world.
        Three distinct conventions exist within the same state_axes block.
      why: >
        No downstream system will fail — all references in cost_ledger and antagonist_pressure
        match the declared slugs exactly. However, the mixed convention (underscore base +
        hyphen suffix) for social_tether-prot-rise versus fully-hyphenated position-prot-rise
        is not derivable from a consistent rule. /and-substance book Phase 3 authors
        populating axis references by analogy may produce mismatched references (e.g.,
        authoring "social_tether_prot_rise" after seeing "position-prot-rise" as the
        model). The inconsistency is a latent authoring-time confusion risk, not a
        current fault.
      criteria: n/a

    - id: flag-003
      type: flag
      what: >
        cl07c cost field is verbose for the opportunity-missed form. The schema specifies
        opportunity-missed:<one line>. The cl07c cost field contains: "opportunity-missed:
        relational_anchor_status reaches rank 9 — unprotected-at-burn [HIGH = WORST on
        this axis; rank 9 = [cost-bearer] dies before Taylor can spend the protection
        she built everything to provide; the un-priced item is the one the calculus came
        for]." The bracketed annotation substantially extends the field beyond a single-line
        description. This is not a schema-breaking violation (the schema has no hard
        character limit), but it sets a precedent for elaborated opportunity-missed fields
        that diverges from the schema's brevity intent.
      why: >
        The annotation content is valuable for downstream authoring context, but the
        relational_anchor_status axis notes field already carries "HIGH = WORST" and the
        end_rank semantics. Duplication is not harmful but the verbosity in the cost field
        may prompt /and-write Phase 6 bone-gate to attempt parsing the bracketed annotation
        as structured content, depending on implementation. No immediate downstream risk.
      criteria: n/a

    - id: flag-004
      type: flag
      what: >
        actor_baselines: [] — empty. Carried forward from attempt-1 flag-004. Cast is not
        yet assigned (series_audit.approved_at: null). The HARD-ABORT annotation is present
        and correct. Recording as pass-with-note for completeness: the empty state is
        intentional and properly annotated.
      why: >
        No action at this phase. Will HARD-ABORT /and-substance book Phase 0 if not
        populated after /and-cast. The annotation documents this correctly.
      criteria: n/a
