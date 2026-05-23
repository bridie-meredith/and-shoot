audit:
  scope: /and-write Phase 2 constraint audit
  target: b01c01 (29 bones, 3 scenes — Phase 1 decomposition)
  phase: 2
  timestamp: 2026-05-23
  findings:

    # ── FAULT-FORM ───────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      class: FAULT-FORM
      what: b01c01s02n07 — svo "taylor-hebert-kl-122ac holds the needle"
      why: >
        Schema narrow holds license permits (1) object is a body part of the subject
        and the action is stillness-against-pressure, or (2) a physical object
        resisting pressure. "The needle" is neither a body part of Taylor nor an
        object resisting pressure — it is an instrument being gripped during work.
        The schema explicitly classifies "taylor holds the ledger" as the canonical
        FAULT-FORM-NON-ACTION-VERB example; "holds the needle" is the same pattern.
        Downstream: stitcher renders this SVO verbatim; the stative-possession verb
        survives into the draft in violation of hard-SVO discipline.
      criteria: >
        The bone must express the mid-day discipline beat (hands engaged with tool,
        capability held against available read) using a verb that passes the
        narrow holds license or is a different licensed concrete verb entirely.
        If the intent is a held-capability bone with hands-at-work as the physical
        surface, the SVO should describe the discrete action performed (e.g., the
        act of taking up the tool, placing it, or a posture-act). The axes_held
        entry and its rationale must be preserved unchanged. The resulting SVO
        must not use "holds" with a non-body-part, non-resisting-pressure object.

    # ── FAULT-COST-LEDGER-UNRESOLVED ────────────────────────────────────────────
    # All six instances share the same missing anchor id.
    # A single cost_ledger[] addition to series.substance resolves all six.

    - id: fault-002
      type: fault
      class: FAULT-COST-LEDGER-UNRESOLVED
      what: b01c01s01n02 — cost_ledger_anchor "knowledge-gain-unanchored-baseline"
      why: >
        The anchor id "knowledge-gain-unanchored-baseline" does not appear in
        series.substance.cost_ledger[]. The six entries present are: cl-otto-trade,
        cl-intelligence-arrangement, cl-network-position, cl-unpriced-cost-bearer,
        cl-social-tether-build, cl-protection-buys-consolidation. Per schema, a
        chatter bone's cost_ledger_anchor must point at an existing ledger entry;
        an anchor that resolves to nothing leaves the chatter bone's accounting
        unresolvable at the /and-facets Phase 5 substance gate.
      criteria: >
        Either (a) replace the anchor with an id that exists in
        series.substance.cost_ledger[], or (b) add a new entry to cost_ledger[]
        with id "knowledge-gain-unanchored-baseline" whose description covers the
        pre-arrangement, unanchored passive knowledge orientation at b01c01 (no
        trade, no prior arrangement; baseline ward-geography read before Otto
        contact). Option (b) requires the showrunner-memory cost_ledger[] edit
        before fixer closes this bone. All six instances (fault-002 through
        fault-007) share this anchor and are resolved by the same single fix.

    - id: fault-003
      type: fault
      class: FAULT-COST-LEDGER-UNRESOLVED
      what: b01c01s01n08 — cost_ledger_anchor "knowledge-gain-unanchored-baseline"
      why: Same missing anchor as fault-002.
      criteria: Same as fault-002 criteria.

    - id: fault-004
      type: fault
      class: FAULT-COST-LEDGER-UNRESOLVED
      what: b01c01s02n01 — cost_ledger_anchor "knowledge-gain-unanchored-baseline"
      why: Same missing anchor as fault-002.
      criteria: Same as fault-002 criteria.

    - id: fault-005
      type: fault
      class: FAULT-COST-LEDGER-UNRESOLVED
      what: b01c01s02n02 — cost_ledger_anchor "knowledge-gain-unanchored-baseline"
      why: Same missing anchor as fault-002.
      criteria: Same as fault-002 criteria.

    - id: fault-006
      type: fault
      class: FAULT-COST-LEDGER-UNRESOLVED
      what: b01c01s02n11 (canonical second instance) — cost_ledger_anchor "knowledge-gain-unanchored-baseline"
      why: Same missing anchor as fault-002.
      criteria: Same as fault-002 criteria.

    - id: fault-007
      type: fault
      class: FAULT-COST-LEDGER-UNRESOLVED
      what: b01c01s03n07 — cost_ledger_anchor "knowledge-gain-unanchored-baseline"
      why: Same missing anchor as fault-002.
      criteria: Same as fault-002 criteria.

    # ── FLAG ─────────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      class: ~
      what: b01c01s02n04 — svo "the insects fill the block"
      why: >
        "fill" sits at the edge of the schema's non-action-verb deny-list:
        semantically equivalent to "occupies / inhabits" (the insects are
        present throughout the block — a state-description). A prior auditor pass
        already classified this as SIGNAL (showrunner memory line 703:
        worm-canon-pedant informational flag on 'fill' verb stability). Not
        escalated to fault because "fill" can be read as describing discrete
        ambient-drift motion and the prior bone-gate passed it SUBSTANCE-FELT
        9/9. If this bone is touched during fault-001 repair, consider recasting
        to a verb more clearly describing a discrete observable action.
      criteria: none — bone is not faulted; advisory only

summary:
  bones_audited: 29
  faults: 7
  faults_by_class:
    FAULT-FORM: 1
    FAULT-CONSTRAINT: 0
    FAULT-PHYSICAL: 0
    FAULT-BONE-DELTA-MALFORMED: 0
    FAULT-AGGREGATE-DELTA-MISMATCH: 0
    FAULT-COST-LEDGER-UNRESOLVED: 6
  flags: 1
  verdict: FINDINGS-PRESENT

# Aggregate delta verification (pass — no FAULT-AGGREGATE-DELTA-MISMATCH):
#   s01 knowledge: 0.03+0.02+0.04+0.02+0.05+0.03 = 0.19 vs target 0.20 (within ±1 rank) PASS
#   s02 knowledge: 0.02+0.05+0.04+0.03+0.02+0.04 = 0.20 vs target 0.20 (exact) PASS
#   s03 knowledge: 0.02+0.03+0.01+0.03 = 0.09 vs target 0.10 (within ±1 rank) PASS
#   chapter knowledge: 0.48 vs target 0.50 (within ±1 rank) PASS
#   capability: held across all 3 scenes — axes_held present in all required bones PASS

# Constraint checks (all pass):
#   cond-override-architecture-residue-122ac: no Khepri-mantle, no range violation, passive-only
#   cond-earth-bet-noun-fence: no Worm-canon proper nouns in any SVO
#   cond-westerosi-magic-dormant-122ac: no native Westerosi magic mechanic invoked
#   cond-kl-social-physics-122ac: copper stars consistent with Taylor's story-open position;
#     Watch patrol timing consistent with cond latency rules (patrol observation,
#     not emergency response); no gold dragons
#   cond-dragon-proximity-122ac: no dragon interaction
#   cond-kl-witch-label-formation-122ac: no visible accumulation event for the label

# Physical checks (all pass):
#   All actors present on set per cast_roster and chapter handoff_in
#   All props (needle, net, pack) consistent with scene context
#   All locations (Flea Bottom / the Hook / alley-mouth / well-step) consistent with
#     cond-kl-geography-122ac and world-notes
