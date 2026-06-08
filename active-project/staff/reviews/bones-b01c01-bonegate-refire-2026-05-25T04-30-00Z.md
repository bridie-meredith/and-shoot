```yaml
audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-25T04:30:00Z
  run_type: bone-gate-refire
  verdict: PASS-WITH-NOTES

  summary: |
    27 bones across 3 scenes. 2 axis-moving bones (s02n06 capability +1 / cl01a;
    s03n04 social_tether-prot-rise +1 / cl01b). 25 held-with-rationale bones.
    0 chatter bones. Aggregate Δ matches chapter contract exactly on both
    in-motion axes. Cost-paid: cl01a opportunity-missed cost enacted in s03
    (witch-label assembly, Oswyn watching); cl01b journey-required cl01a satisfied
    (s02n06 precedes s03n04). Opposing forces enacted in all three scenes.
    No SUBSTANCE-FLAT. No SUBSTANCE-SUSPECT-cheap-gain. substance_delta_measured
    roll-up confirmed correct. Two non-blocking SIGNALs noted.

  findings:

    - id: fault-001
      type: pass
      what: >
        Per-bone bonefide — b01c01s02n06 ("the insects propagate"):
        axis_moves capability +1, cost_ledger_anchor cl01a.
        SVO states insects propagate (deploy outward through the crowd).
        Scene chunk confirms first active deployment since arrival:
        "The insects move. The nearest dozen bodies get the sensation of something
        at ankle-height and yield." capability axis rank 1 = fully suppressed,
        start_rank 2; +1 move at first deployment is correct direction and
        defensible magnitude for d01 of a 6-rank book arc.
      why: n/a — pass

    - id: fault-002
      type: pass
      what: >
        Per-bone bonefide — b01c01s03n04 ("oswyn-mudway-flea-bottom-elder takes
        the lane-mouth"): axis_moves social_tether-prot-rise +1,
        cost_ledger_anchor cl01b.
        SVO states Oswyn takes the lane-mouth. Scene chunk confirms Oswyn stands
        at the lane mouth and watches, composing a category for Taylor — Taylor
        moves from invisible to present in his accounting. social_tether-prot-rise
        rank 1 = nil; +1 move for ward-layer embedding onset is correct direction
        and magnitude for the partial cl01b settlement declared in the chapter
        contract (ward-layer half only; court-layer half deferred to b01c03).
      why: n/a — pass

    - id: fault-003
      type: pass
      what: >
        Per-scene aggregate Δ — all three scenes.
        s01: axes_in_motion [] declared; bones confirm zero axis_moves.
        s02: capability +1.0 declared; exactly one bone (s02n06) carries
        capability +1; sum = 1.0. Matches target.
        s03: social_tether-prot-rise +1.0 declared; exactly one bone (s03n04)
        carries social_tether-prot-rise +1; sum = 1.0. Matches target.
        Chapter aggregate: capability +1.0 + social_tether-prot-rise +1.0.
        Matches chapter contract axes_in_motion exactly.
      why: n/a — pass

    - id: fault-004
      type: pass
      what: >
        substance_delta_measured roll-up (memory.md lines 2231-2234).
        Declared: capability +1.0 / cl01a / anchor_bone b01c01s02n06;
        social_tether-prot-rise +1.0 / cl01b / anchor_bone b01c01s03n04.
        Independent measurement matches on all four fields for both entries.
        Roll-up is correct.
      why: n/a — pass

    - id: fault-005
      type: pass
      what: >
        Cost-paid check — cl01a (capability +1).
        Ledger entry: gain "capability +1", cost type "opportunity-missed":
        rescue witnessed; witch-label formation begins; [cost-bearer] enters
        exposure radius. Opportunity-missed costs require the missed opportunity
        to be visible on-page, not a paired cost entry.
        s03 enacts the cost: Oswyn watching and composing the witch-label
        (s03n04, s03n09), fish-cart man watching Taylor instead of the child
        (s03n02), two women holding position (s03n03), and handoff_out records
        "witch-label formation active in Hook precinct." Cost is present and
        enacted. Not a cheap gain.
      why: n/a — pass

    - id: fault-006
      type: pass
      what: >
        Cost-paid check — cl01b (social_tether-prot-rise +1).
        Ledger entry: gain "social_tether-prot-rise +2", cost type
        "journey-required: cl01a (same rescue event; tether embedding is the
        other face of witch-label exposure)."
        Chapter contract notes this anchor closes only the ward-layer half (+1
        of the full +2); court-layer half deferred to b01c03.
        Journey-required condition: cl01a must precede cl01b settlement.
        cl01a fires at s02n06 (flat_id 12 in scene 2); cl01b fires at s03n04
        (flat_id 21 in scene 3). Sequential order satisfied within the chapter.
        Not a cheap gain.
      why: n/a — pass

    - id: fault-007
      type: pass
      what: >
        Opposing-force enactment — all three scenes.
        s01 opposing_force "physical difficulty of suppression in a ward dense
        with bodies and signal": enacted at s01n04 ("the insects swell" —
        opposing force enacted per bone rationale: insect-pull at threshold) and
        s01n07 ("taylor-hebert-kl-122ac exhales" — morning argument; body's
        verdict on another day of choosing the prohibition). Pass.
        s02 opposing_force "crowd's compression, and the prohibition against
        deploying insect-control on unconsenting persons": enacted at s02n03
        ("the crowd compresses" — bone rationale explicitly names
        "prohibition-against-using-insects-on-persons now runs against") and
        s02n04 ("taylor-hebert-kl-122ac holds the feet" — last prohibition-
        maintenance beat before the crack). Pass.
        s03 opposing_force "Oswyn Mudway's watching; witch-label assembling in
        the gap": enacted at s03n04 ("oswyn-mudway-flea-bottom-elder takes the
        lane-mouth" — the social_tether axis-moving bone is also the opposing-
        force vehicle; Oswyn's categorization IS the tether forming and the
        label assembling simultaneously) and s03n09 ("oswyn-mudway-flea-bottom-
        elder lifts the chin" — bone rationale: "Oswyn's chin-lift is the
        composing-of-the-word"). Pass.
      why: n/a — pass

    - id: fault-008
      type: pass
      what: >
        SUBSTANCE-FLAT check — all axes declared in-motion at chapter level.
        capability: moves in s02 exactly as contracted (s02n06).
        social_tether-prot-rise: moves in s03 exactly as contracted (s03n04).
        No in-motion axis shows zero aggregate movement across the chapter.
        No SUBSTANCE-FLAT finding on any axis.
      why: n/a — pass

    - id: fault-009
      type: pass
      what: >
        SUBSTANCE-SUSPECT-cheap-gain check — both axis-moving bones.
        s02n06 capability +1 / cl01a: opportunity-missed cost enacted in-chapter
        (see fault-005). Not a cheap gain.
        s03n04 social_tether-prot-rise +1 / cl01b: journey-required cost
        satisfied by cl01a in-chapter (see fault-006). Not a cheap gain.
        No SUBSTANCE-SUSPECT-cheap-gain finding on any axis.
      why: n/a — pass

    - id: fault-010
      type: pass
      what: >
        axes_held rationale honesty — chapter-level and per-bone.
        moral_framework (held across all 27 bones): prohibition not yet licensed;
        crack is real but Taylor has not filed it as a violation; self-accounting
        has not opened. Rationale is "held-and-load-bearing" — the chapter's
        structural premise depends on moral_framework being held as load-bearing
        dormancy, not absent-and-ignored.
        relational_anchor_status (held across all 27 bones): Wren present but
        not in Taylor's calculus; anchor noticed only by the reader. Held as
        structural dormancy per chapter goal second-clause plant. Load-bearing.
        political_register-prot (held): no court content, no insect-feed above
        ward-layer in any scene. Held at structural baseline rank 1. Honest.
        moral_legibility_to_self (held): self-accounting running as maintenance
        not reckoning (s01); deployment not yet filed (s02); ledger deferred (s03).
        Load-bearing across all three scenes (the deferral IS the chapter's
        thematic setup).
        social_tether-prot-rise (held in s01, s02): s01 anonymity intact at nil;
        s02 witnesses present but ward-embedding not yet registered. Both honest
        descriptions of the axis state before s03n04 fires.
        capability (held in s01, s03): s01 suppressed by discipline, threshold
        established. s03 at new floor, deployment confirmed visible, no further
        deployment. Honest.
        No rationale found that describes "absent-and-ignored" rather than
        "held-and-load-bearing." All held rationales pass.
      why: n/a — pass

    - id: fault-011
      type: pass
      what: >
        Bones file vs memory.md cross-check (flat_ids and SVO text).
        27 bones declared (memory.md bones_count: 27, aggregate_range: 1-27).
        Bones file b01-c01.md: 27 lines (1-27).
        s01 flat_ids 1-6 (n05 dropped; n06→5, n07→6): file lines 1-6 match
        SVOs exactly.
        s02 flat_ids 7-17 (n11 at 16, n10 at 17 per dramatist reorder): file
        lines 7-17 match SVOs and ordering exactly.
        s03 flat_ids 18-27 (including added n10 at 27): file lines 18-27 match
        SVOs exactly.
        No orphaned flat_ids. No missing bones. No SVO divergence.
      why: n/a — pass

    - id: signal-001
      type: flag
      what: >
        b01c01s01n07 ("taylor-hebert-kl-122ac exhales"): three axes_held entries
        (moral_legibility_to_self, moral_framework, political_register-prot).
        chunk_targets.bone specifies axes_per_bone: 1-2. Three held entries on
        a single bone exceeds the upper target bound.
        The overage was a deliberate repair move at authoring time (political_
        register-prot rationale relocated from dropped s01n05 to n07 to avoid
        losing the held coverage), and the bone-gate at authoring time accepted
        the signal (gate_verdict signals: [ACCEPT-axes-held-overage-repair-move]).
        No axes_moves entry exists on this bone (all three are axes_held only).
        The overage does not create a false or absent rationale — all three held
        rationales are honest. But the structure is outside the 1-2 spec, and
        a future fixer or refactor at this scene should know the bone carries
        a relocated axis.
      why: >
        If the bones file is used as a mechanical audit input by downstream tools
        that enforce axes_per_bone: 1-2 as a hard constraint, this bone will
        trigger a false HARD. The repair-move disposition is only recorded in
        memory.md (gate_verdict.signals); it is not visible from the flat bones
        file alone. Downstream commands reading only b01-c01.md have no record
        of the exception.

    - id: signal-002
      type: flag
      what: >
        s02 scene contract: stakes_axis is declared as moral_framework.
        s02 axes_in_motion is capability +1.0 (not moral_framework).
        The scene_conflict.opposing_force names "the prohibition against deploying
        insect-control on unconsenting persons" as a stakes element, but
        moral_framework stays held (load-bearing dormancy — the crack is real but
        unfiled by Taylor). The bone that delivers the axis movement (s02n06
        capability +1) is also the bone at which moral_framework's prohibition is
        transgressed in fact, if not in Taylor's accounting.
        This is not a schema violation: the spec does not require stakes_axis and
        axes_in_motion to match. The held rationale for moral_framework is honest
        (the crack is present but not acknowledged). However, the surface read is:
        a scene with stakes_axis: moral_framework that delivers no movement on
        moral_framework. The disambiguation — "the crack is load-bearing dormancy
        by design, and capability is the mechanical expression of that crack" —
        is present in the rationales but not in the contract field itself.
      why: >
        If a future auditor fires on s02 in isolation and checks whether the
        stakes_axis moved, the answer is "no" without the rationale context.
        The stakes_axis: moral_framework declaration invites a false SUBSTANCE-FLAT
        finding on moral_framework for this scene if checked without the full
        per-bone rationale corpus. Non-blocking; the chapter-level contract and
        the per-bone held rationales are consistent. Flagged for /and-substance
        chapter revise if b01c01 is ever re-run.
```
