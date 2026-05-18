# Series Signature Audit — taylor-hebert-westeros-good-intentions
# 2026-05-17

```yaml
audit:
  scope: series
  target: series.substance.* + books[0] (b01 chunk + substance_delta)
  timestamp: 2026-05-17
  findings:

    # ─── HARD ───────────────────────────────────────────────────────────────

    - id: fault-001
      class: HARD
      type: fault
      what: >
        books[0].substance_delta.axes_in_motion[position]:
        { axis: position, direction: up, target_delta_magnitude: 0 }
      why: >
        `direction: up` with `target_delta_magnitude: 0` is a logical contradiction.
        The position axis has start_rank 1 and end_rank 1 (net delta = 0). An `up`
        direction on a 0-magnitude delta is meaningless and misleading to downstream
        consumers (/and-write Phase 6 bone-gate, /and-substance book). The tuning note
        correctly describes this as an intentional rise-and-fall, but the direction
        field should reflect the net arc, not the intended intra-book shape (which is
        not expressible in the `direction` enum at this level). A downstream bone-gate
        or reviewer reading `direction: up` will expect the axis to move upward, not
        return to start.
      criteria: >
        `direction` must be semantically consistent with `target_delta_magnitude`.
        For a 0-net axis, direction must be `~` (null), `flat`, or an explicitly
        supported enum value indicating no net movement. If the rise-and-fall shape
        needs to be preserved for downstream consumers, it belongs in the `notes`
        field, not in `direction`.

    # ─── SIGNAL ─────────────────────────────────────────────────────────────

    - id: fault-002
      class: SIGNAL
      type: flag
      what: >
        series.substance.cost_ledger: relational-anchor-status net-delta gap.
        cl-unpriced-cost-bearer: gain: relational-anchor-status -1 (negative gain = axis
        moves down). cl-protection-buys-consolidation: gain: relational-anchor-status +1
        (positive gain = axis moves up). Net from both entries: 0.
        Declared substance_delta for RAS: direction: down, target_delta_magnitude: 2
        (3→1 = -2 net).
      why: >
        The two ledger entries acting on relational-anchor-status cancel each other
        (one -1, one +1). No third entry covers the remaining -2 magnitude. The
        declared arc cannot be arithmetically derived from the ledger entries in scope.
        At /and-substance book Phase 5 (dramatist check), the cost-ledger is verified
        against the declared axes_in_motion; this gap will surface as a SIGNAL there.
        More critically, at /and-write Phase 6 (bone-gate), per-bone cost_ledger_anchor
        for RAS-declining bones will point only to cl-unpriced-cost-bearer, and the
        bone-gate may flag the -2 magnitude as under-priced relative to the single
        ledger entry cited.
      criteria: >
        Either (a) add a third cost-ledger entry that accounts for the full -2 net
        on relational-anchor-status (or revise magnitudes in the two existing entries
        so they sum to -2), or (b) add a note in both existing entries explaining
        the compounding/repeating mechanism that produces -2 net despite the opposing
        signs, so downstream bone-gate auditors can verify against the note rather
        than a missing entry.

    - id: fault-003
      class: SIGNAL
      type: flag
      what: >
        books[0].chunk (prose): social-tether axis (2→1, direction: down,
        magnitude: 1). The chunk does not describe a cause for this loss.
        The irony paragraph implies "[cost-bearer] dies in the street" but the
        social-tether loss (Flea Bottom embeddedness severed) is not given an
        explicit cause-description in the chunk text. All other axis motions
        (moral-framework, capability, political-register, knowledge, agency,
        relational-anchor-status, moral-legibility-to-self) have traceable causal
        language in the chunk.
      why: >
        The series chunk at book level is supposed to give cause-language for every
        declared axis motion so that /and-substance book can decompose it into
        chapter-level deltas. A missing cause-description leaves screen-writer
        without a causal anchor when authoring social-tether-moving chapters, and
        increases the risk of SUBSTANCE-FLAT-social-tether at the bone-gate.
      criteria: >
        The b01 chunk must contain language that describes the mechanism by which
        social-tether declines from 2 to 1 — e.g., the Flea Bottom embeddedness
        that once provided cover becoming the vector of exposure, or the death/departure
        of [cost-bearer] severing the community layer. The language does not need to
        be a separate sentence; it can be integrated into the existing irony or trade
        paragraphs.

    - id: fault-004
      class: SIGNAL
      type: flag
      what: >
        books[0].chunk (prose): position axis rise-and-fall (peak 5 at d07, collapse
        to 1 at d14). The chunk says Otto offers Taylor "a function instead of a rank"
        — actively refusing explicit position — but does not describe the mechanism
        by which position rises to peak 5 (mid-arc). The collapse to 1 is described
        ("removed from the story's scope") but the rise is not.
      why: >
        The position axis is declared as intentional rise-and-fall with peak 5 at
        d07. Without a cause-description for the rise, /and-substance book has no
        causal anchor for the chapters that move position upward. This risk is lower
        than fault-003 because the position 0-net is flagged as intentional and the
        chunk_targets tuning note explicitly warns reviewers not to flag SUBSTANCE-FLAT
        on position — but the absence of a rise-cause still leaves a decomposition gap.
      criteria: >
        The b01 chunk should contain language describing how Taylor acquires
        informal court-layer visibility despite refusing formal rank — the mechanism
        that makes her "known to one court layer as a functional asset" by d07.
        May be brief; the goal is a causal anchor for screen-writer at /and-substance book.

    - id: fault-005
      class: SIGNAL
      type: flag
      what: >
        series.substance.cost_ledger[cl-knowledge-contempt]: cost field uses a
        positive direction (+1) on political-register-toward-elite.
        series.substance.cost_ledger[cl-protection-buys-consolidation]: same pattern.
        Both entries use cost: political-register-toward-elite +1 to mean "contempt
        grows" (axis moves toward rank 9 = contempt-without-refusal).
      why: >
        The cost field in the cost_ledger schema uses `-<delta>` for costs per the
        schema definition (`cost: <axis-slug> -<delta>`). Using `+1` as a cost is
        non-standard and will cause confusion at /and-write Phase 6 bone-gate when
        cost_ledger_anchor is resolved — the bone-gate may expect negative-direction
        cost entries and misread these as gains. The axis direction is not inherently
        bad (the axis end-state being rank 9 as the story's "bad" outcome is a valid
        design choice) but the ledger notation is schema-divergent.
        cl-knowledge-contempt description explicitly explains the non-standard pattern,
        which mitigates the risk; cl-protection-buys-consolidation does not include
        an equivalent explanation note.
      criteria: >
        Either (a) add an explanation note to cl-protection-buys-consolidation matching
        the explanatory note in cl-knowledge-contempt, making the +1-as-cost convention
        explicit in both entries, or (b) normalize both cost fields to a negative
        direction (e.g. cost: contempt -1 using a renamed axis that makes "up" bad)
        and update the axis definition accordingly. Fixer should choose the minimum-
        change resolution — (a) is preferred since the axis is already defined with
        rank 9 as bad and reversing would cascade to state_axes.

    - id: fault-006
      class: SIGNAL
      type: flag
      what: >
        series.substance.chunk_targets.series: delta_per_signature_axis: 3-8.
        Default per design/substance/delta-targets.md: 4-8. Lower bound overridden
        from 4 to 3. Tuning note in memory.md explains this: "series delta_min
        lowered 4→3 to accommodate small-magnitude loss moves (social-tether −1,
        moral-framework −2) in this loss-arc tragedy."
      why: >
        The override is documented and coherent for a loss-arc tragedy with several
        small-magnitude axes. The per-axis deltas that triggered the override
        (social-tether −1, moral-framework −2) are genuinely below the default 4-rank
        floor. However, these same axes are the ones with the weakest causal coverage
        in the chunk (social-tether noted in fault-003). If a downstream reviewer
        reads the 3-rank floor without the tuning note, they may incorrectly flag
        SUBSTANCE-FLAT on these axes. Flagging for awareness only; the override
        itself is permissible per delta-targets.md.
      criteria: >
        No fix required unless fault-003 is left unresolved — in which case the
        3-rank floor and the missing cause-language on social-tether create a
        compounding risk for the bone-gate. Closing fault-003 fully resolves the
        downstream risk this flag identifies.

    # ─── TASTE ──────────────────────────────────────────────────────────────

    - id: fault-007
      class: TASTE
      type: flag
      what: >
        series.substance.cost_ledger[cl-unpriced-cost-bearer]: described as
        "STRUCTURAL ERROR ENTRY — no realized gain" with gain: relational-anchor-status
        -1 (a loss, not a gain). This is an intentional non-standard ledger pattern
        per the description.
      why: >
        The cl-unpriced-cost-bearer entry is a deliberate structural oddity encoding
        the story's central irony: the un-priced relationship is itself the cost.
        This is thematically coherent. Any downstream check that flags this as a
        "missing gain" or "gain-field negative" should treat the flag as TASTE, not
        HARD, per the audit dispatch instructions. Noted here for reviewer awareness
        so bone-gate auditors do not auto-escalate it.
      criteria: ~

    - id: fault-008
      class: TASTE
      type: flag
      what: >
        series.substance.cost_ledger[cl-social-tether-build]: cost: position +1.
        The cost of Flea Bottom embeddedness is increased visibility (position moves
        up, toward rank 5 = known-to-court). This is an up-direction cost on an axis
        where "up" is mixed-valence (formal rank is partially a gain, partially an
        exposure). The cost is described adequately in the entry notes.
      why: >
        Not a fault. Noted because "cost: position +1" is only harmful in the
        story because visibility leads to non-extractability, not because rank itself
        is bad. The axis definition at rank 5 ("known to one court layer as a
        functional asset; unranked; identifiable to users") is neutral-to-slightly-bad
        for Taylor. This ambiguity does not create a downstream structural problem
        but a reviewer may question whether position-up is appropriately coded as
        a cost. The entry is self-consistent.
      criteria: ~
```
