audit:
  scope: series
  target: series
  timestamp: 2026-05-24
  findings:

    # ── SCHEMA CONFORMANCE ──────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        memory.md series.substance.state_axes — three slug collisions: `position`
        appears twice (lines 109-118 protagonist, 120-129 world); `social_tether`
        appears twice (lines 131-140 protagonist, 142-151 antagonist);
        `political_register_toward_elite` appears twice (lines 175-184 protagonist,
        186-195 world). Schema line 96 defines slug as a plain string identifier
        with no multi-perspective aliasing provision.
      why: >
        Downstream consumers keyed on slug (cost_ledger axis references, antagonist_pressure
        axis references, /and-substance book axes_in_motion lookups) cannot resolve
        which entry a bare slug names when the slug appears twice. Reference-integrity
        checks at book and chapter authoring time will produce ambiguous matches or
        silent first-match wins. The world-perspective axes are load-bearing (Green-faction
        consolidation is the thematic mirror of protagonist deterioration) and must be
        individually addressable.
      criteria: >
        Each state_axes entry must carry a unique slug. Disambiguate the three colliding
        pairs. Acceptable forms: append a perspective suffix to the world/antagonist
        entries (e.g. `position_world`, `social_tether_antagonist`,
        `political_register_toward_elite_world`), or use any other slug form that makes
        each entry individually addressable. All cost_ledger and antagonist_pressure
        references that targeted the colliding slugs must be updated to match whichever
        slug disambiguation is chosen.

    - id: fault-002
      type: fault
      what: >
        memory.md cost_ledger cl01 gain field: `"capability +2, social_tether +2"`.
        memory.md cost_ledger cl03 gain field: `"capability +3, social_tether +4"`.
        Schema line 129: `gain: <axis-slug> +<delta>` — singular form.
      why: >
        Multi-axis gain in a single gain field violates the singular gain contract.
        /and-write Phase 6 bone-gate resolves bones against cost_ledger entries; a
        bone referencing cl01 or cl03 as its cost_ledger_anchor expects a single
        gain axis to verify against. A multi-axis string in the gain field makes that
        resolution ambiguous and may cause the bone-gate to fail or skip the second
        axis silently.
      criteria: >
        cl01 and cl03 must each be split into separate ledger entries, one per gain
        axis, with a shared or per-entry cost assignment that preserves the
        cost-paid relationship. If the cost is indivisible across both gain axes,
        one entry carries the cost and the other carries `journey-required:` or
        `opportunity-missed:` that references the paired entry.

    - id: fault-003
      type: fault
      what: >
        memory.md cost_ledger cl07 cost field: `"relational_anchor_status +4,
        social_tether -7, position -6"`. Three issues: (a) three axes in a single
        cost field — schema line 130 permits one cost form per entry; (b)
        `relational_anchor_status +4` carries a positive delta in the cost field —
        schema/Field Notes line 258 states "cost is always negative on its axis (or
        the axis moves toward its damaging end)"; a +4 with no cost_note pattern
        invocation is a wrong-sign cost entry; (c) the multi-axis cascade in cost
        mirrors the schema-bend in fault-002 for gain.
      why: >
        The cl07 entry encodes the series collapse event (d14: social_tether severed,
        position dead/expelled, relational_anchor_status unprotected at burn). This
        entry is the most load-bearing single ledger entry in the series — it prices
        the climax. Ambiguous sign and multi-axis packing prevent bone-gate from
        correctly validating bones that anchor against cl07. The +4 on
        relational_anchor_status, if read as a gain rather than a cost, will cause
        bones that pay this cost to be scored as substance-positive when they should
        be scored as substance-negative (collapse event).
      criteria: >
        cl07 must be split into separate entries per axis. The
        `relational_anchor_status` entry in cl07 must carry a negative delta or use
        `opportunity-missed:`/`journey-required:` form if the cost is
        non-quantifiable-as-rank-loss; the current +4 in a cost field must be
        resolved to a semantically correct sign and form. Each split entry anchors at
        book: b01 with null chapter/scene.

    # ── COST-LEDGER DELTA RECONCILIATION ───────────────────────────────────

    - id: fault-004
      type: fault
      what: >
        Cost-ledger delta sums do not reconcile against state_axes start/end deltas
        for four axes. (All math below treats higher rank = more of the named quality,
        regardless of whether more is "better" or "worse" in story terms.)

        capability: state_axes declares +6 (start 2, end 8).
          Ledger gains: cl01 +2, cl03 +3, cl05 +2 = +7. No capability costs.
          Discrepancy: +1 unaccounted.

        moral_framework: state_axes declares +6 (start 2, end 8 — framework consumed
          = higher rank = worse; costs in ledger represent rank increase).
          Ledger costs: cl02 -3, cl03 -3, cl05 -2 = -8 total cost
          (which represents +8 rank increase in deterioration terms).
          State_axes net movement: +6. Ledger implies +8. Discrepancy: +2 over-priced.

        political_register_toward_elite (protagonist): state_axes declares +8
          (start 1, end 9). Ledger gains: cl06 +5 only. Discrepancy: +3 unaccounted.

        relational_anchor_status: state_axes declares +8 (start 1, end 9).
          Ledger explicit gain: cl04 +3. cl07 cost carries "relational_anchor_status +4"
          which is ambiguous-sign (see fault-003) — even if read as gain, total is +7.
          Discrepancy: +1 (minimum; +5 if cl07 cost is correctly negative).
      why: >
        The cost ledger is the mechanism by which /and-substance book and /and-write
        Phase 6 verify that per-chapter deltas sum to the series-level arc. Unreconciled
        discrepancies mean either the ledger is incomplete (missing entries that
        price the gap) or the state_axes start/end ranks are incorrectly set. Either
        way, the bone-gate's cost-paid check will produce false results against any
        chapter that sources these axes. For moral_framework the over-pricing by +2
        means two units of framework deterioration are priced but not declared in the
        arc — a silent inflation that will make the series feel over-deteriorated at
        the chapter level.
      criteria: >
        For each discrepancy: either (a) add ledger entries that price the gap, with
        anchors at book: b01, or (b) revise the state_axes start/end ranks to match
        the sum the ledger actually prices. The ledger and the state_axes must be
        mutually consistent. capability gap +1, moral_framework over-price +2,
        political_register_toward_elite gap +3, relational_anchor_status gap +1
        minimum must each be resolved with a documented rationale.

    # ── FLAGS ───────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: >
        memory.md state_axes: position (protagonist) start_rank=1 end_rank=1;
        social_tether (protagonist) start_rank=1 end_rank=1. The rise-then-collapse
        curve (position peaks ~6-7 at d07/d10, social_tether peaks ~7-8 at d04/d07)
        is recorded only in the notes field.
      why: >
        /and-substance book Phase 3 reads start_rank/end_rank to compute axes_in_motion
        vs axes_held. A net-zero axis (start = end) may be classified as axes_held
        rather than a rise-then-collapse axis requiring two phases of motion. If the
        book-level authoring loop skips these axes on the basis of "net 0," the peak
        states (position-of-no-exit at d10, non-extractable at d10) will never appear
        in per-chapter substance_delta contracts, and /and-write Phase 6 bone-gate
        will have no rise-phase target to validate bones against. The trajectory
        assigns six deltas to these two axes (d01, d03, d04, d07, d10, d14) —
        this is not a held-flat arc.
      why_downstream: >
        The collapse at d14 is the climax event. If the rise is never contracted at
        book level, the collapse bones will have no priced peak to fall from — the
        bone-gate will see a collapse with no corresponding rise and flag it as
        substance-flat or cheap-gain in reverse.

    - id: flag-002
      type: flag
      what: >
        memory.md cost_ledger: position (protagonist) and social_tether (protagonist)
        axes carry net zero in the declared state_axes (start_rank=end_rank=1).
        The cost_ledger has cl02 gain +4 on position, cl07 cost -6 on position
        (net -2 in ledger); cl01 gain +2 + cl03 gain +4 on social_tether, cl07
        cost -7 on social_tether (net -1 in ledger). Neither axis reconciles to
        a net-zero ledger sum. The ledger implies net position = -2 and net
        social_tether = -1, not the 0 declared by start/end ranks.
      why: >
        This is the flip side of fault-004 for the rise-then-collapse axes. If the
        intention is that the end_rank=1 absorbs the collapse back to start_rank=1,
        then the ledger correctly prices a rise and a collapse, and the net is
        intentional. But the discrepancy is not documented. A reader of the ledger
        without the notes will see net -2 on position and net -1 on social_tether
        and conclude the end states should be below the start states. The sign
        mismatch needs an explicit note or a reconciliation annotation in the ledger.
        This is a flag, not a fault, because the intent is reconstructable from
        context — but fixer should add a reconciliation note.

    - id: flag-003
      type: flag
      what: >
        memory.md chunk_targets book bone_count: 270-500. The series structure
        declares 18-22 chapters, 3-5 scenes/chapter, 5-15 bones/scene. The structural
        minimum is 18 × 3 × 5 = 270 bones; the structural maximum is 22 × 5 × 15 =
        1650 bones. The book-level target (270-500) sets an upper bound at ~30% of
        structural maximum.
      why: >
        The lower bound (270) is tight: a 18-chapter, 3-scene-per-chapter book at
        exactly 5 bones/scene hits this floor with no headroom. Any authoring decision
        to add a scene or expand a scene to 6 bones immediately busts the bone_count
        ceiling (500). The chapter target of 15-75 bones × 18 chapters = 270-1350,
        which is wider than the book-level range. The book-level target is therefore
        the binding constraint — but it is tighter than the series structure permits,
        creating a tension that may produce SUBSTANCE-FLAT findings at the scene level
        if authors hold to the book bone-count ceiling while trying to meet
        density_target 0.7-0.9. This is a design choice, not a schema fault — flag
        for downstream awareness.

    - id: flag-004
      type: flag
      what: >
        memory.md series.substance.actor_baselines: []. The schema comment reads
        "AUTHORED AT STEP 4d (post-cast); HARD-ABORT on first /and-substance book
        Phase 0 if empty." Cast is not yet assigned (series_audit.approved_at: null).
      why: >
        The empty value is correct at this pre-cast stage. Recording as a pass-with-note:
        the comment annotation is present and the downstream hard-abort gate is
        correctly documented. No action needed at this phase; this finding is a
        confirmation that the empty state is intentional and properly annotated.

    # ── RANK-CAUSE COHERENCE ────────────────────────────────────────────────

    - id: fault-005
      type: pass
      what: >
        Rank claims for moral_framework (start 2, end 8), capability (start 2, end 8),
        relational_anchor_status (start 1, end 9), moral_legibility_to_self (start 4,
        end 8), political_register_toward_elite protagonist (start 1, end 9), and all
        world/antagonist axes have defensible trajectory anchors in series-trajectory.md.
        Each axis's one/five/nine anchors map to named states in the trajectory's
        start_state, end_state, and deltas. No rank claims without cause.
      why: n/a
      criteria: n/a

    # ── REFERENCE INTEGRITY ─────────────────────────────────────────────────

    - id: fault-006
      type: pass
      what: >
        All axis slug references in cost_ledger gain/cost strings and antagonist_pressure
        axis fields resolve to slugs present in state_axes[]. No dangling references.
        (Note: the slug collision fault-001 means references to `position`, `social_tether`,
        and `political_register_toward_elite` are currently ambiguous as to which of
        the two entries they target — this is covered under fault-001, not a separate
        reference-integrity finding.)
      why: n/a
      criteria: n/a

    # ── ANCHOR DISCIPLINE ───────────────────────────────────────────────────

    - id: fault-007
      type: pass
      what: >
        All seven cost_ledger entries carry anchor: { book: b01, chapter: null,
        scene: null }. Matches schema Field Notes: "/and-substance series writes
        anchor.book only." Pass.
      why: n/a
      criteria: n/a
