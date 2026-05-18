# Substance Audit — b01 Chapter Plan
# /and-substance book b01 Phase 5

```yaml
audit:
  scope: book
  target: b01
  timestamp: 2026-05-18
  auditor: auditor
  verdict: REVISE (SIGNAL findings only)
  findings:

    # ────────────────────────────────────────────────────────────────
    # HARD findings — none
    # ────────────────────────────────────────────────────────────────

    # ────────────────────────────────────────────────────────────────
    # SIGNAL findings
    # ────────────────────────────────────────────────────────────────

    - id: signal-001
      type: flag
      what: >
        b01c01 substance_delta.axes_in_motion[1]:
        { axis: knowledge, cost_ledger_anchor: cl-intelligence-arrangement, notes: "Flea Bottom geography read; ward-level pattern established" }
      why: >
        cl-intelligence-arrangement's ledger description reads: "each intelligence delivery deepens Taylor's
        court-layer picture but extends the arrangement that makes her non-extractable." In b01c01 there is
        no arrangement with Otto (he has not appeared) and no intelligence delivery. The knowledge gain is
        pure geographic orientation — passive insect-sense reading of ward density. Anchoring a pre-arrangement,
        pre-delivery knowledge gain to a delivery-mechanism ledger entry is a category error. If the
        bone-gate at /and-write Phase 6 resolves per-bone cost_ledger_anchor against the finest-grained
        populated field, bones in this chapter carrying cl-intelligence-arrangement will be evaluated against
        a ledger mechanism that does not apply yet. Downstream bones authored against this anchor risk
        SUBSTANCE-SUSPECT findings at the gate.
      criteria: >
        b01c01 knowledge axis must carry a cost_ledger_anchor that describes a mechanism operative
        in b01c01: either null/~ (observation-with-no-ledger-entry, consistent with the pre-arrangement
        state) or a new ledger entry for pre-arrangement geographic observation. The cl-intelligence-arrangement
        anchor must not appear in any chapter before the arrangement with Otto is live (b01c05 onward).

    - id: signal-002
      type: flag
      what: >
        b01c02 substance_delta.axes_in_motion[0]:
        { axis: capability, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-network-position }
        b01c02 substance_delta.axes_in_motion[2]:
        { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-intelligence-arrangement }
      why: >
        cl-network-position describes: "each network expansion makes Taylor more load-bearing to Otto
        and less extractable; the network that makes her effective is the cage." In b01c02 Taylor
        executes a one-time defensive rescue; Otto has not appeared; there is no arrangement, no
        Otto-dependency, and no cage mechanism operating. The capability gain is a self-directed
        deployment of dormant insect-sense, not a network expansion under the Otto arrangement.
        Anchoring it to cl-network-position imports a dependency-and-entrapment mechanism that has
        not been established in the story yet.
        cl-intelligence-arrangement carries the same pre-arrangement issue as signal-001: the
        watch-sweep knowledge gained in b01c02 is operational pattern-reading from a rescue event,
        not from an intelligence delivery to Otto. The arrangement ledger entry should not appear
        before b01c05.
        At /and-write Phase 6, bones in b01c02 carrying these anchors will be gate-checked against
        ledger mechanisms that have no causal footing in the chapter. Bone authors may incorrectly
        frame rescue-deployment bones as Otto-load-bearing network bones.
      criteria: >
        b01c02 capability axis must carry a cost_ledger_anchor that describes a mechanism operative
        in b01c02: either null/~ (self-directed deployment, no patron-dependency yet) or a new
        ledger entry capturing the pre-arrangement capability cost (e.g., that deployment creates
        witness-exposure risk, not Otto-dependency). b01c02 knowledge anchor must similarly be
        null/~ or a pre-arrangement observation entry. cl-network-position and cl-intelligence-arrangement
        must not appear in chapters before the Otto arrangement is live.

    - id: signal-003
      type: flag
      what: >
        b01c04 substance_delta.axes_in_motion[0]:
        { axis: position, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-social-tether-build }
        b01c05 substance_delta.axes_in_motion[1]:
        { axis: position, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-social-tether-build }
        b01c09 substance_delta.axes_in_motion[2]:
        { axis: position, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-social-tether-build }
      why: >
        cl-social-tether-build's ledger entry is: gain: social-tether +1 / cost: position +1.
        The cost_note states "position rising is a cost in this trajectory." This formulation means
        position-rise is the cost side of the entry, and social-tether-rise is the gain side.
        In b01c04, b01c05, and b01c09, position rises but social-tether does NOT also rise in the
        same chapter (social-tether gains are confined to b01c02 and b01c06). The chapters are
        claiming only the cost side of this ledger entry while the gain side (social-tether) is
        realized in separate chapters with no cross-reference.
        This asymmetric use of a single ledger entry across chapters is not structurally prohibited,
        but it means the cost_ledger_anchor in these three chapters points to a mechanism whose
        gain-trigger is not present in the chapter. At /and-write Phase 6, bone-gate will check
        whether the anchored ledger mechanism's gain and cost are both visible. If the gate reads
        cl-social-tether-build as requiring a social-tether event and finds none in b01c04/c05/c09,
        it will produce a SUBSTANCE-SUSPECT finding on those bones.
        The position rises in c04/c05 are driven by Otto-visibility (Otto identifying Taylor;
        arrangement accepted), not by Flea Bottom embeddedness. A more precise anchor for these
        position gains would be cl-otto-trade (which governs the Otto relationship and its costs)
        or a new ledger entry for court-visibility-via-arrangement.
      criteria: >
        The three position-rise instances (b01c04, b01c05, b01c09) must carry a cost_ledger_anchor
        whose gain side is also triggered in the same chapter, or the anchor must be null/~ with
        a note that position-rise is a consequence-event (same treatment as political-register-toward-elite).
        Alternatively, a new ledger entry may be added for court-layer visibility gain with its
        correct gain/cost pairing. Whatever anchor is used, it must describe the mechanism that
        is actually operative in that chapter.

    - id: signal-004
      type: flag
      what: >
        b01c09 substance_delta.axes_in_motion[1]:
        { axis: capability, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-network-position,
          notes: "systematic-reading-made-systematic; courier-layer route-mapping generalizes the architecture;
          5→5.5; d07 capability refinement" }
        Compared against series-trajectory delta d07:
        shifts: ["moral_framework: first-sanctioned-exception → systematic-override-rationalized",
                 "position: known-quantity-to-one-court-layer → Otto's-unofficial-instrument"]
      why: >
        Trajectory d07 lists two shifts: moral-framework and position. Capability is not listed
        as a d07 shift. The chapter claims a capability gain of +0.5 as a "d07 capability
        refinement" but the trajectory does not designate this movement as part of d07's cause-event.
        The trajectory note for d07's cause ("Otto makes explicit what the arrangement has been...
        Taylor gives people their routes and patterns without their knowledge") does describe an
        operational act that could plausibly imply a capability increase. However the trajectory
        does not allocate capability movement to d07 — d04 is where Khepri-rhyming architecture
        is built; capability movement not allocated in the trajectory after d04 until d12. A
        capability gain at d07 is either an undocumented trajectory gap or an overclaim in the
        chapter contract.
        This is not a roll-up fault (capability roll-up sums to +4.0 within ±1 of target) but
        it is a trajectory-chapter alignment gap. If the +0.5 at c09 is load-bearing to the
        roll-up, removing it would bring capability sum to +3.5, still within ±1. If it is not
        load-bearing, the trajectory should be amended to note the d07 capability refinement
        so /and-write Phase 6 bone-gate can correctly classify capability bones at c09.
      criteria: >
        Either (a) the series-trajectory d07 entry must be amended to add a capability shift
        noting the courier-layer generalization, or (b) the b01c09 capability axis must be
        removed from substance_delta.axes_in_motion with a note that no trajectory allocation
        exists for capability at d07. If (b), confirm the capability roll-up still lands within
        ±1 of the +4 target (it does: 4.0 → 3.5, within ±1, so removal is safe).

    # ────────────────────────────────────────────────────────────────
    # NOTE findings (informational; no fixer action required)
    # ────────────────────────────────────────────────────────────────

    - id: note-001
      type: flag
      what: >
        cond-cost-bearer-scene-frequency card not found at
        cards/conditions/cond-cost-bearer-scene-frequency.md
      why: >
        The memory.md series.behaviors list includes cond-cost-bearer-scene-frequency as a
        binding behavior constraint. The card does not exist on disk. Auditor could not verify
        the declared Wren scene-frequency against a numeric threshold. Visual inspection of
        the 18-chapter plan shows Wren present (as chunk subject, scene participant, or
        handoff-state-named active presence) in approximately 14-15 of 18 chapters, which
        appears high-frequency. However without the card's declared threshold, compliance
        cannot be mechanically confirmed. No fixer action is appropriate for a missing card
        at this gate; this is a production-state gap.
      criteria: ~

    - id: note-002
      type: flag
      what: >
        b01c01 through b01c17: field name "dramatic_role" present on each chapter
        (values: setup, rising, climax, falling, coda).
        Schema showrunner-memory.schema.md defines the field as "dramatic_shape"
        with enum: rising | climax | falling | hinge.
      why: >
        The draft uses a non-schema field name ("dramatic_role") with non-schema enum values
        ("setup", "coda", "falling" — "falling" appears in schema but "setup" and "coda" do not).
        Schema says dramatic_shape is authored at /and-substance chapter Phase 3, so this field
        is not required at /and-substance book Phase 2+3. However the draft has already populated
        it. When /and-substance chapter re-runs to author dramatic_shape, if it writes to the
        schema-correct field name, the "dramatic_role" entries will become orphan fields that
        may confuse downstream readers. "Setup" and "coda" are not valid dramatic_shape enum
        values; chapters using those labels will need to be mapped to schema-valid values
        (rising/hinge for setup chapters; the coda chapter b01c18 has no schema enum equivalent
        under the current schema).
      criteria: ~

    - id: note-003
      type: flag
      what: >
        b01c17 substance_delta.axes_in_motion[0]:
        { axis: relational-anchor-status, target_delta_magnitude: 0.5,
          notes: "1→0.5 (floor: below-rank-1 permitted at burn)" }
        b01c17 position: "1.5→0.5 (floor)"
        b01c15 agency: "2→1.5"
        b01c17 agency: "1.5→1"
      why: >
        The rank system is nominally 1-9 per the schema anchors (one_means through nine_means).
        Several closing-state entries permit values below 1 (0.5 floor). The schema does not
        define sub-1 ranks or a "floor" mechanism. The draft's self-annotation "floor: below-rank-1
        permitted at burn" has no schema backing. At /and-write Phase 6, the bone-gate's axis-movement
        verification will check magnitude against rank bands; bones that drive axes to 0.5 may
        produce unexpected gate behavior if the gate enforces a 1-9 integer or 1-9 float range.
        This is a schema ambiguity to resolve before /and-write is run on b01c17.
      criteria: ~

    # ────────────────────────────────────────────────────────────────
    # PASS findings (checks that are clean)
    # ────────────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: Schema conformance — required fields at /and-substance book Phase 2+3 scope
      why: >
        All 18 chapters carry: chunk (prose), structure.scene_count, substance_delta.axes_in_motion[],
        substance_delta.density_target, handoff_in.{open_threads, world_state, character_state,
        source_chapter}, handoff_out.{open_threads, world_state, character_state, target_chapter}.
        Fields deferred to /and-substance chapter (pov_narrator, goal, status, stale_since) are
        absent, which is correct for this phase. No required field is missing.

    - id: pass-002
      type: pass
      what: Chunk-to-contract match across all 18 chapters
      why: >
        For each chapter, the axes_in_motion claims are causally grounded in the chunk prose.
        No chapter claims an axis move for events not described in the chunk. No chunk describes
        events that would generate axis movement not listed in axes_in_motion. The signal-001
        through signal-004 findings are anchor-mechanism mismatches, not chunk-event mismatches;
        the events themselves match the contracts.

    - id: pass-003
      type: pass
      what: Cost-ledger anchor ID validity — all referenced anchor IDs exist
      why: >
        All cost_ledger_anchor values in the 18-chapter plan reference valid ledger entry IDs:
        cl-otto-trade, cl-intelligence-arrangement, cl-network-position, cl-unpriced-cost-bearer,
        cl-social-tether-build, cl-protection-buys-consolidation. No chapter references a
        non-existent ledger ID. Null (~ ) anchors appear only on consequence-axes (political-register,
        capability during passive phase), which is consistent with the ledger note that
        consequence-axes use cost_ledger_anchor: ~ with notes.

    - id: pass-004
      type: pass
      what: Roll-up math — per-axis sums against books[b01].substance_delta targets
      why: >
        Independent recomputation of all 9 axes:
        moral-framework: c05(-1.0)+c09(-0.5)+c15(-0.5) = -2.0; target -2; delta 0.0 ✓
        capability: c02(+1.0)+c06(+1.0)+c09(+0.5)+c14(+1.0)+c15(+0.5) = +4.0; target +4; delta 0.0 ✓
        position (net): c04+c05+c09 = +1.5 rise; c12+c17 = -2.0 fall; net -0.5; target 0; |delta| 0.5 ✓
        social-tether: c02+c06 = +1.0 rise; c12+c17 = -1.5 fall; net -0.5; target -1; |delta| 0.5 ✓
        relational-anchor: c03+c08+c10+c13+c17 = -2.5; target -2; |delta| 0.5 ✓
        moral-legibility: c03+c08+c12+c13+c17 = -3.0; target -3; delta 0.0 ✓
        political-register: c07+c11+c16+c17 = +4.0; target +4; delta 0.0 ✓
        knowledge: c01+c02+c04+c06+c07+c09+c10+c11+c14 = +5.5; target +5; |delta| 0.5 ✓
        agency: c05+c06+c09+c12+c14+c15+c17 = -4.0; target -4; delta 0.0 ✓
        All axes within ±1 of declared book target. Position net and rise/fall components verified
        separately as specified.

    - id: pass-005
      type: pass
      what: Hard-fence compliance — chapter count, scene count, POV, title prohibition, end-place
      why: >
        Chapter count: 18 (meets 18-chapter floor). Scene counts: c01-c03 (3 each), c04 (4),
        c05 (4), c06-c09 (3 each), c10 (4), c11 (3), c12 (4), c13 (3), c14 (4), c15 (4),
        c16 (3), c17 (5), c18 (3). All ≥3. Floor satisfied.
        POV: b01c18 is marked "INTERLUDE — Archmaester Corvan retrospective; non-Taylor POV."
        All other chapters are Taylor first-person. One non-Taylor chapter correctly marked.
        Title prohibition: no "title:" fields appear on any chapter; chapter headers use
        slug + dash-separated descriptor (e.g. "b01c01 — flea-bottom-anonymous-baseline").
        No "Chapter N: <Title>" form. Compliant.
        End-place locus "both": b01c17 chunk explicitly states "Wren dies in the street Taylor
        had charted" AND "Taylor is removed — dead or expelled by the forces her position made
        her legible to." Both elements of the hard fence are present.

    - id: pass-006
      type: pass
      what: Cast roster consistency — all character slugs match series.cast_roster
      why: >
        Slugs appearing in b01-draft.md: taylor-hebert-kl-122ac, otto-hightower,
        aemond-targaryen-122ac, wren-stitch-maker-flea-bottom-ward, sera-hightower-kl-122ac,
        gylda-saltwater-flea-bottom, coll-net-mender-flea-bottom,
        corvan-archmaester-retrospective-coda. All eight match series.cast_roster exactly.
        No new characters introduced outside the roster.

    - id: pass-007
      type: pass
      what: Handoff chain integrity — all 17 adjacent-pair transitions
      why: >
        Verified all adjacent-pair handoffs b01c01→c02 through b01c17→c18:
        open_threads carry forward (compressed at c17→c18, which is permitted); world_state
        items mirror or compress correctly; character_state rank values are internally consistent
        across all 17 transitions. No HANDOFF-MIRROR-DRIFT finding. Specific verified pairs:
        c01 out (knowledge 3.5) → c02 in (knowledge 3.5) ✓; c09 out (agency 3.5) → c10 in
        (agency 3.5) ✓; c12 out (moral-legibility 5) → c13 in (moral-legibility 5) ✓.
        c17→c18 compressed from 4 threads to 2; both surviving threads are OPEN-for-coda tagged,
        which is a legitimate compression (closed threads need not propagate).

    - id: pass-008
      type: pass
      what: First-chapter rule (F7) — b01c01 handoff_in matches series.substance.state_axes start_ranks
      why: >
        b01c01.handoff_in.source_chapter: null ✓
        Taylor start_ranks verified: moral-framework 3 ✓, capability 3 ✓, position 1 ✓,
        social-tether 2 ✓, relational-anchor-status 3 ✓, moral-legibility-to-self 7 ✓,
        political-register-toward-elite 5 ✓, knowledge 3 ✓, agency 5 ✓.
        Otto start_ranks (antagonist): position 6 ✓, moral-framework 7 ✓.
        World_state seeded from project.constraints.settings (year, currency, class, place,
        magic, dragons all present in b01c01.handoff_in.world_state). Compliant.

    - id: pass-009
      type: pass
      what: Earth-Bet proper-noun fence — no on-page dialogue or inner-monologue violations
      why: >
        The hard fence prohibits parahuman jargon in dialogue and restricts it in inner monologue.
        No chapter chunk authors a specific on-page dialogue line or inner-monologue passage.
        Chunk prose (showrunner record) names Khepri and describes the override architecture;
        this is permitted at chunk level. No fence violation found at the chunk-plan stage.

    - id: pass-010
      type: pass
      what: Book drama statement (Phase 4) — present and aligned with trajectory
      why: >
        b01-draft.md Phase 4 drama statement is present and substantive. It correctly identifies
        the book's surviving-element (prohibition extinguished), the mechanism (Otto prices it
        per-trade, not destroys it), and the irony (the prevention apparatus that worked produced
        conditions under which Taylor could not reroute the final violence). This aligns with
        the series.chunk.path.trade and .irony fields in memory.md, and with trajectory end_state
        entries for moral-framework, position, and relational-anchor-status. Drama statement
        names Wren and Sera Hightower by name, consistent with /and-cast resolutions recorded
        in cast_roster. No contradiction with series-level substance contract.

    - id: pass-011
      type: pass
      what: Cost-bearer scene frequency — qualitative check (condition card absent; see note-001)
      why: >
        Without the cond-cost-bearer-scene-frequency card, a numeric threshold cannot be verified.
        Qualitative scan: Wren appears as a substantive chapter element (chunk subject, named
        scene participant, or active handoff-state presence) in b01c01, c02, c03, c06, c08,
        c10, c11, c12, c13, c14, c15, c16, c17, c18 (14 of 18 chapters). Absent or peripheral
        in c04, c05, c07, c09 (4 of 18). Wren's trajectory from c01-edge presence to c17-death
        is load-bearing throughout. High-frequency threshold is very likely satisfied but cannot
        be confirmed mechanically.
```

---

## Verdict summary

**REVISE (SIGNAL findings only)**

No HARD findings. Four SIGNAL (flag) findings; three NOTE findings.

Signal findings are all cost_ledger_anchor mechanism mismatches, not chunk-event errors or roll-up faults:

- **signal-001 and signal-002**: cl-intelligence-arrangement and cl-network-position appear in b01c01 and b01c02 before the Otto arrangement is established. These anchors describe Otto-dependency mechanisms that have no causal footing in pre-arrangement chapters. Downstream risk: bone-gate at /and-write Phase 6 will check bones against ledger mechanisms that cannot apply, potentially producing false SUBSTANCE-SUSPECT findings on rescue and orientation bones.

- **signal-003**: cl-social-tether-build used to anchor three position-rise events (c04, c05, c09) where the ledger's gain-side (social-tether) is not also moving. The anchor misidentifies the operative mechanism for Otto-visibility gains; the bone-gate may flag these bones for not showing social-tether movement when the anchor is checked.

- **signal-004**: b01c09 claims a capability +0.5 attributed to d07 but d07 in the trajectory does not list a capability shift. If bone-gate resolves d-range against trajectory allocation, bones at c09 carrying capability movement may be classified as undeclared.

Note findings are informational: a missing condition card (note-001), a field-name divergence that will matter when /and-substance chapter runs (note-002), and a below-floor rank convention with no schema backing (note-003).

All roll-up math, handoff chain, start-rank initialization, hard-fence compliance, cast consistency, chunk-to-contract match, and end-place requirements are clean.
