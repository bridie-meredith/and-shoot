# b01c12 bones draft — screen-writer Phase 1 (scene-decomposition)
# /and-write b01c12 Phase 1 — 2026-06-03
# SVO reference form: b01-c02.md (canonical clean Phase-2 form)

# ============================================================
# per-scene roll-up check
# ============================================================
# s01: capability +0.5 (target +0.5 ✓), social_tether-prot-rise +0.5 (target +0.5 ✓)
#      HELD relational_anchor_status ✓, political_register-prot ✓
#      bone-Δ sum: capability +0.5, social_tether-prot-rise +0.5 — EXACT
#
# s02: axes_in_motion EMPTY (target: none ✓)
#      HELD relational_anchor_status ✓, position-prot-rise ✓, social_tether-antag ✓
#      bone-Δ sum: 0 axis moves — EXACT (held-discipline + chatter-with-anchor scene)
#
# s03: relational_anchor_status +1.0 (target +1.0 ✓), position-prot-rise +1.0 (target +1.0 ✓)
#      HELD political_register-prot ✓, social_tether-antag ✓, moral_legibility_to_self ✓
#      bone-Δ sum: relational_anchor_status +1.0, position-prot-rise +1.0 — EXACT
#
# s04: capability +0.5 (target +0.5 ✓), moral_framework -1.0 (target -1.0 ✓)
#      HELD moral_legibility_to_self ✓, political_register-prot ✓, social_tether-antag ✓
#      bone-Δ sum: capability +0.5, moral_framework -1.0 — EXACT
#
# chapter roll-up:
#   capability: +0.5 (s01) + 0 (s02) + 0 (s03) + 0.5 (s04) = +1.0  ✓ (contract +1.0)
#   social_tether-prot-rise: +0.5 (s01) = +0.5  ✓ (contract +0.5)
#   relational_anchor_status: +1.0 (s03) = +1.0  ✓ (contract +1.0)
#   position-prot-rise: +1.0 (s03) = +1.0  ✓ (contract +1.0)
#   moral_framework: -1.0 (s04) = -1.0  ✓ (contract -1.0)
# ALL 5 chapter axes EXACT. ✓
# ============================================================

scenes:

  - slug: b01c12s01
    event_map:
      - event: "east-of-water-gate-lanes [image]"
        covers: [b01c12s01n01, b01c12s01n02]
        omission_rationale: null
      - event: "witch-label-trigger-geometry [mechanism]"
        covers: [b01c12s01n03]
        omission_rationale: null
      - event: "coverage-gap-established [event]"
        covers: [b01c12s01n04, b01c12s01n05]
        omission_rationale: null
      - event: "wren-daily-pattern-through-gap [image]"
        covers: [b01c12s01n06]
        omission_rationale: null
      - event: "wren-as-effective-eastern-boundary [mechanism]"
        covers: [b01c12s01n07, b01c12s01n08]
        omission_rationale: null
      - event: "first-ward-cluster-added [event]"
        covers: [b01c12s01n09, b01c12s01n10]
        omission_rationale: null

    bones:
      - slug: b01c12s01n01
        svo: "the insects return the overhang-joints"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "witch-label terrain geometry is the structural constraint against which the coverage gap is formed; the overhang-joints are the specific feature that makes dense placement readable as witch-label and forces the gap; axis held at 3.5"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: eaves/gutter-joints of the upper stories — the specific terrain feature that makes dense placement readable as witch-label.
        # Phase-2 fix: fault-001 — chatter→held; relational_anchor_status attached (s01 declared held axis)

      - slug: b01c12s01n02
        svo: "the insects fan the lane-mouth"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "ambient deployment in the gap lanes — the feed at its placement ceiling is the terrain-constraint that makes Wren's route the boundary; anchor held at 3.5"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # Phase-2 fix: fault-002 — chatter→held; relational_anchor_status attached per meta-rule 2 override (not capability — s01 does not declare capability as a held axis)

      - slug: b01c12s01n03
        svo: "taylor-hebert-kl-122ac takes the gate-tower shadow"
        shape: held
        axis_moves: []
        axes_held:
          - axis: political_register-prot
            rationale: "the gap-mapping is a cold technical accounting act; no resentment register fires here; Taylor operates in flat operational mode, no contempt-register action"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: the gate-tower shadow as a named physical coordinate; Taylor's body placed inside the lane geometry.
        # opposing_force visible: the lane's geometry enforces the constraint — the inhabited upper stories refuse clean placement.

      - slug: b01c12s01n04
        svo: "the coverage map closes the gate-tower boundary"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "gate-tower boundary is the confirmed western limit of the coverage gap; the gap's eastern limit is defined against it; axis held at 3.5"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # Phase-2 fix: fault-003 — chatter→held; relational_anchor_status attached (s01 declared held axis)

      - slug: b01c12s01n05
        svo: "the map closes the rendering-yard boundary"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "rendering-yard east wall is the confirmed eastern limit of the coverage gap; together with n04 the gap is formally bounded; Wren's free movement in the gap is the structural condition the anchor depends on; axis held at 3.5"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: rendering yard east wall named as a specific physical landmark bounding the gap.
        # Phase-2 fix: fault-004 — chatter→held; relational_anchor_status attached (s01 declared held axis)

      - slug: b01c12s01n06
        svo: "the insects return the stitch-house route"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "Wren's daily pattern through the gap is re-confirmed as an operational indexed fact; the anchor-axis move (cl-d06 settlement via the choice) belongs in s03; held at 3.5 here because the choice has not yet arrived — this is the indexing-without-weighting beat that sets up the collision"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s01n07
        svo: "the map marks the stitch-maker route"
        shape: held
        # Phase-2 fix: fault-005 — "indexes" (non-action verb) → "marks" (concrete transitive physical act)
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "Wren's route indexed as the gap's operative eastern boundary — not an anchor-status advance, a held confirmation; the entry goes nowhere else; held-discipline against the opposing-force push of the lane geometry"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s01n08
        svo: "taylor-hebert-kl-122ac lifts the stylus"
        shape: held
        # Phase-2 fix: fault-006 — dropped PP "from the source-field" (banned source-preposition)
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "The stylus lifts without writing the source — the indexed-but-unwritten state re-enacted as a physical stopping-before-writing beat; the route goes down, the source-field is not reached; opposing-force (the apparatus's expectation of a priced source) held off by the physical withdrawal of the stylus; anchor held at 3.5"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: stylus as named physical object; the source-field as the specific target not reached.

      - slug: b01c12s01n09
        svo: "taylor-hebert-kl-122ac extends the northern ward-cluster"
        shape: moving
        axis_moves:
          - axis: capability
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl05
        grounding: false
        dialogue_anchor: false
        # cl05 gain side, first partial tranche (+0.5 of +1.0 across chapter).

      - slug: b01c12s01n10
        svo: "the ledger column closes the water-gate entry"
        shape: moving
        axis_moves:
          - axis: social_tether-prot-rise
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl-d08b
        grounding: true
        dialogue_anchor: false
        # grounding: the ledger column as a physical surface; the entry closing is a concrete physical act.
        # cl-d08b: gap-boundary confirmation consolidates tether — Wren's free movement in uncovered lanes closes the map without entering the architecture.

  - slug: b01c12s02
    event_map:
      - event: "jarvis-delivers-new-request [event]"
        covers: [b01c12s02n01, b01c12s02n02]
        omission_rationale: null
      - event: "otto-requests-east-water-gate-lane-coverage [event]"
        covers: [b01c12s02n03]
        omission_rationale: null
      - event: "packet-describing-the-gap-lanes [image]"
        covers: [b01c12s02n03, b01c12s02n04]
        omission_rationale: null
      - event: "request-collides-with-gap-boundary [mechanism]"
        covers: [b01c12s02n04, b01c12s02n05]
        omission_rationale: null
      - event: "otto-apparatus-knowing-the-terrain [force]"
        covers: [b01c12s02n05]
        omission_rationale: null
      - event: "collision-between-request-and-gap-confirmed [event]"
        covers: [b01c12s02n05, b01c12s02n06]
        omission_rationale: null

    bones:
      - slug: b01c12s02n01
        svo: "jarvis-coin-kl-courier places the packet"
        shape: held
        axis_moves: []
        axes_held:
          - axis: social_tether-antag
            rationale: "opposing force enters via the standard channel — the apparatus's terrain-literate delivery; tether-antag held at 6"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: packet as named physical object; physical delivery act.
        # opposing_force enters with Jarvis.
        # Phase-2 fix: fault-007 — dropped PP "on the ledger surface" (banned PP of place); chatter→held; social_tether-antag attached (s02 declared held axis)

      - slug: b01c12s02n02
        svo: "taylor-hebert-kl-122ac breaks the wax seal"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "seal-breaking is the physical threshold action that makes the collision-delivery arrive as a fact; the anchor gap-route is what the packet targets; axis held at 3.5"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: wax seal as concrete physical object.
        # Phase-2 fix: fault-008 — chatter→held; relational_anchor_status attached (s02 declared held axis)

      - slug: b01c12s02n03
        svo: "taylor-hebert-kl-122ac opens the covering-sheet"
        shape: held
        axis_moves: []
        axes_held:
          - axis: relational_anchor_status
            rationale: "The request arrives naming the exact lanes that constitute the anchor's boundary; the collision is delivered but the axis-move belongs to the response (s03), not the delivery. Held at 3.5; the opposing-force (the apparatus's terrain-literate precision request) is now fully visible"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # Phase-2 fix: fault-009 — "the covering-sheet names the east-water-gate corridor" (non-action verb/stative document-content) → "taylor-hebert-kl-122ac opens the covering-sheet" (physical act); corridor content is facet territory

      # Phase-3 dramatist REVISE-1 reorder: n05 (second boundary-name) now precedes n04 (packet-set reaction) so the
      # full irony lands (BOTH gate-tower west + rendering-yard east named) BEFORE the stilling-reaction. List order = n03,n05,n04,n06,n07. Slugs unchanged.
      - slug: b01c12s02n05
        svo: "taylor-hebert-kl-122ac turns the covering-sheet"
        shape: held
        # Phase-2 fix: fault-011 — "the covering-sheet names the rendering-yard boundary" (non-action verb/stative document-content) → "taylor-hebert-kl-122ac turns the covering-sheet" (physical act distinct from n03's opening); boundary content is facet territory
        axis_moves: []
        axes_held:
          - axis: social_tether-antag
            rationale: "Otto's apparatus targets the gap lanes as a structural leverage expression — the apparatus knows the territory, names the exact corridor. Leverage is structural but not advancing this chapter (Otto has not noticed the pattern of withholding); held at 6. The opposing-force enacted: the request carries the shape of prior intelligence, reading back the gap with precision"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s02n04
        svo: "taylor-hebert-kl-122ac sets the packet"
        shape: held
        # Phase-2 fix: fault-010 — dropped PP "on the ledger surface" (banned PP of place)
        axis_moves: []
        axes_held:
          - axis: position-prot-rise
            rationale: "The withholding-from-Otto position-move (cl02) belongs to the refusal act in s03; the request arriving is the condition, not the decision; held at 4. The opposing-force push: the request is precise, terrain-literate, the kind of ask that expects a corresponding deliverable"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: packet returned to ledger surface — physical act of setting down against pressure to comply.
        # Phase-3 dramatist REVISE-1: this stilling-reaction now lands AFTER both corridor boundaries are named (n03 opens sheet / gate-tower; n05 turns sheet / rendering-yard), so the collision is complete before Taylor stills.

      - slug: b01c12s02n06
        svo: "taylor-hebert-kl-122ac sets the stylus"
        shape: held
        # Phase-2 fix: fault-012 — dropped PP "beside the packet" (banned PP of place); chatter→held; position-prot-rise attached (s02 declared held axis per meta-rule 2)
        axis_moves: []
        axes_held:
          - axis: position-prot-rise
            rationale: "physical stillness at the decision threshold — stylus set without writing; the withholding-before-refusal enacted physically; axis held at 4"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: stylus as named physical object; the stylus set (not applied) is the physical closing of the collision-delivery scene.
        # This enacts the pl-2026-06-03-004 (a) watch: the bay-warmth close is Taylor's body paired to setting.
        # The warm-on-held-hand is the indifferent-world-continuance beat; enacted here as body-paired-to-object, not atmospheric description.
        # NOTE: this bone (n06, stylus set) is the sole carrier of the pl-2026-06-03-004 (a) bay-warmth watch after the Phase-4 trim of n07.

      # Phase-4 trim (dark-fantasy DELETE-PROPOSE, orchestrator-accepted on 1-persona advisory): b01c12s02n07 ("taylor holds the eyes")
      # removed — third consecutive body-stillness bone in s02 (n04 packet-set / n06 stylus-set / n07 eyes-held); the bay-warmth watch
      # resolves on n06 (concrete grounded object-bone); n07 extended the stillness into camera-linger, against the chapter's own
      # lift-and-move discipline (pl-2026-06-03-004). s02 retains 4 grounding bones + position-prot-rise held (n04) + opposing-force (n05).
      # Slug n07 retired (no renumber, per Phase-4 do-not-renumber rule). s02 now 6 bones.

  - slug: b01c12s03
    event_map:
      - event: "taylor-drafts-refusal-to-otto [event]"
        covers: [b01c12s03n01, b01c12s03n02]
        omission_rationale: null
      - event: "bare-source-field-in-the-response [image]"
        covers: [b01c12s03n03]
        omission_rationale: null
      - event: "refusal-without-explanation [mechanism]"
        covers: [b01c12s03n04, b01c12s03n05]
        omission_rationale: null
      - event: "response-sealed-and-routed-to-jarvis [event]"
        covers: [b01c12s03n06, b01c12s03n07]
        omission_rationale: null
      - event: "taylor-withholding-the-gap [force]"
        covers: [b01c12s03n05, b01c12s03n08]
        omission_rationale: null
      - event: "apparatus-accepting-the-boundary [force]"
        covers: [b01c12s03n07]
        omission_rationale: null
      - event: "ledger-entry-anchor-column-opened [event]"
        covers: [b01c12s03n09]
        omission_rationale: null
      - event: "cl-d06-settlement-via-cl-d08-refusal-act [mechanism]"
        covers: [b01c12s03n10, b01c12s03n11]
        omission_rationale: null
      - event: "relational-anchor-weight-settles [event]"
        covers: [b01c12s03n11, b01c12s03n12]
        omission_rationale: null

    bones:
      - slug: b01c12s03n01
        svo: "taylor-hebert-kl-122ac takes the stylus"
        shape: held
        # Phase-2 fix: fault-013 — chatter→held; political_register-prot attached (s03 declared held axis per meta-rule 2)
        axis_moves: []
        axes_held:
          - axis: political_register-prot
            rationale: "taking the stylus in flat operational register — the refusal-writing act opens in the same cold-utilitarian mode as every prior deliverable entry; no contempt-register fires; register held at 3.5"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: stylus as named physical object; taking up the stylus is the concrete opening of the refusal-writing act.

      - slug: b01c12s03n02
        svo: "the coverage-entry opens the gap-column"
        shape: held
        # Phase-2 fix: fault-014 — chatter→held; political_register-prot attached (s03 declared held axis per meta-rule 2)
        axis_moves: []
        axes_held:
          - axis: political_register-prot
            rationale: "gap-column opens in the same flat format as every prior entry — no register advance; no contempt fires on the act of opening; held at 3.5"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s03n03
        svo: "taylor-hebert-kl-122ac writes the boundary entry"
        shape: moving
        axis_moves:
          - axis: position-prot-rise
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl02
        grounding: false
        dialogue_anchor: false
        # First half of position-prot-rise +1.0: the refusal written into the channel record as a structural limit.
        # cl02: withholding-from-Otto (hook-0014 third instance). The named gap now enters the deliverable.

      - slug: b01c12s03n04
        svo: "taylor-hebert-kl-122ac holds the hand"
        shape: held
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The hand stops before reaching the explanation field — physical enactment of the withholding-before-writing beat (pl-2026-06-03-004 (b)); the stylus does not reach the source-clause; the suppression-pattern is enacted physically (not an interior enumeration); moral_legibility_to_self held at 5.5 — the crack is present in this pause, not opening"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: the hand as a body-part executing the physical stop; narrow holds license — body-part stillness-against-pressure.

      - slug: b01c12s03n05
        svo: "the stylus lifts"
        shape: held
        # Phase-2 fix: fault-015 — dropped PP "from the explanation field" (banned source-preposition)
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The stylus does not reach the field that would name the gap's contents; the physical withholding (not-writing what lives inside the gap) is the held-discipline beat; opposing-force visible: the channel expects an explanation; Taylor's hand goes elsewhere"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: stylus as physical object; the field (a specific column on the ledger surface) as the target that is not reached.

      - slug: b01c12s03n06
        svo: "taylor-hebert-kl-122ac closes the response entry"
        shape: moving
        axis_moves:
          - axis: position-prot-rise
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl02
        grounding: false
        dialogue_anchor: false
        # Second half of position-prot-rise +1.0: the refusal sealed — withholding now load-bearing and recorded in the channel.

      - slug: b01c12s03n07
        svo: "jarvis-coin-kl-courier takes the sealed packet"
        shape: held
        axis_moves: []
        axes_held:
          - axis: social_tether-antag
            rationale: "The apparatus receives the refusal via the standard channel without press; Otto's leverage is structural but not advancing — the lane-refusal does not reduce leverage because Otto has not noticed the pattern. Held at 6; the opposing-force enacted: the apparatus accepts the boundary, as it always accepts coverage limits, which makes Taylor's withholding structurally invisible"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: the sealed packet in Jarvis's hand is a concrete physical act; the covering-sheet flat over the seal.

      - slug: b01c12s03n08
        svo: "the response entry closes the gap-column"
        shape: held
        axis_moves: []
        axes_held:
          - axis: political_register-prot
            rationale: "The gap-column closes in flat operational register — a tactical operational close, not a contempt-register event; no resentment-color fires in the refusal; political_register-prot held at 3.5; the opposing-force enacted: the channel entry is now a named gap in the deliverable, load-bearing and visible, but delivered in the same flat register as every prior entry"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # This enacts pl-2026-06-03-004 (b): the un-routed content (what the gap protects) is the absence in the closed entry — NOT interior enumeration. The physical closing of the column without the explanation clause is the stopping-before-writing enacted.

      - slug: b01c12s03n09
        svo: "taylor-hebert-kl-122ac opens the anchor-column"
        shape: chatter
        # Phase-2 fix: fault-016 — chatter-with-anchor per meta-rule 2 override (do NOT hold relational_anchor_status — s03 MOVES that axis; instead attach cl-d08 anchor prefiguring n10 settlement)
        axis_moves: []
        axes_held: []
        cost_ledger_anchor: cl-d08
        grounding: true
        dialogue_anchor: false
        # grounding: the ledger as a physical object opened to a specific column; the anchor-column as a named surface. Prefigures the relational_anchor_status +0.5 at n10 (cl-d08 gain side); resolves at-or-under s03.

      - slug: b01c12s03n10
        svo: "taylor-hebert-kl-122ac writes the anchor-column entry"
        shape: moving
        # Phase-2 fix: fault-017 — "the anchor-column entry takes the refusal weight" (abstract object / interiority) → concrete ledger-act "taylor-hebert-kl-122ac writes the anchor-column entry"; axis_moves PRESERVED per meta-rule 1
        axis_moves:
          - axis: relational_anchor_status
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl-d08
        grounding: false
        dialogue_anchor: false
        # cl-d08 mechanism: the lane-refusal IS the mechanism by which Wren's free movement becomes the map's load-bearing eastern boundary. First 0.5 of the +1.0 relational_anchor_status move; settles cl-d08.

      - slug: b01c12s03n11
        svo: "taylor-hebert-kl-122ac closes the anchor-column entry"
        shape: moving
        # Phase-2 fix: fault-018 — "the anchor-column entry takes the deferred weight" (abstract object / interiority) → concrete ledger-act "taylor-hebert-kl-122ac closes the anchor-column entry"; mirrors n06 "closes the response entry" pattern; axis_moves PRESERVED per meta-rule 1
        axis_moves:
          - axis: relational_anchor_status
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl-d06
        grounding: false
        dialogue_anchor: false
        # cl-d06 debt: the outstanding second tranche (+1.0 total across n10+n11), settling cl-d06 per DEC-0071. This is the second 0.5; the combined n10+n11 deliver the full +1.0. Closes pl-2026-05-30-001 / pl-2026-06-02-stitch-thread-002.

      - slug: b01c12s03n12
        svo: "taylor-hebert-kl-122ac lifts the hand"
        shape: held
        # Phase-2 fix: fault-019 — dropped PP "from the anchor-column" (banned source-preposition); chatter→held; moral_legibility_to_self attached (s03 declared held axis per meta-rule 2 override — do NOT hold relational_anchor_status since s03 MOVES that axis)
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "the hand lifts without the suppression cracking — the accounting is filed, the column closed; legibility holds at 5.5; lift-and-move, no linger (pl-2026-06-03-004 c)"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: the hand as a body-part lifting from the physical ledger surface; enacts pl-2026-06-03-004 (c): hand-on-ledger close is lift-and-move — the hand lifts, the column closes. No camera-linger.

  - slug: b01c12s04
    event_map:
      - event: "second-ward-cluster-added [event]"
        covers: [b01c12s04n01, b01c12s04n02]
        omission_rationale: null
      - event: "aggregate-feed-scale-at-full-deployment [image]"
        covers: [b01c12s04n14, b01c12s04n03, b01c12s04n04]
        omission_rationale: null
      # n14 (Phase-3 dramatist REVISE-2 causal bridge): the muddy-way entry closes the fifth-ward circuit -> the aggregate completes for the first time.
      - event: "khepri-threshold-crossed-in-aggregate [mechanism]"
        covers: [b01c12s04n05, b01c12s04n06]
        omission_rationale: null
      - event: "internal-accounting-runs-at-full-scale [event]"
        covers: [b01c12s04n07, b01c12s04n08]
        omission_rationale: null
      - event: "khepri-word-surfaces-in-accounting [event]"
        covers: [b01c12s04n09]
        omission_rationale: null
      - event: "khepri-suppression-act [mechanism]"
        covers: [b01c12s04n10, b01c12s04n11]
        omission_rationale: null
      - event: "feed-continuing-past-the-suppression [image]"
        covers: [b01c12s04n11, b01c12s04n12]
        omission_rationale: null
      - event: "capability-full-deployment-confirmed [event]"
        covers: [b01c12s04n12]
        omission_rationale: null
      - event: "moral-framework-ledger-entry-for-threshold [event]"
        covers: [b01c12s04n13]
        omission_rationale: null

    bones:
      - slug: b01c12s04n01
        svo: "taylor-hebert-kl-122ac extends the muddy-way ward-cluster"
        shape: chatter
        # Phase-2 fix: fault-020 — chatter-with-anchor per meta-rule 2 override (do NOT hold capability — s04 MOVES that axis; instead attach cl05 anchor prefiguring the n02 capability gain, resolves at-or-under s04)
        axis_moves: []
        axes_held: []
        cost_ledger_anchor: cl05
        grounding: false
        dialogue_anchor: false
        # The second ward-cluster extension begins; prefigures the capability +0.5 at n02 (cl05 gain side); resolves at-or-under s04.

      - slug: b01c12s04n02
        svo: "the insects fill the muddy-way upper-margin"
        shape: moving
        axis_moves:
          - axis: capability
            direction: up
            magnitude: 0.5
        axes_held: []
        cost_ledger_anchor: cl05
        grounding: true
        dialogue_anchor: false
        # grounding: the Muddy Way upper-margin as a named physical location in the coverage geography.
        # cl05 gain side, second partial tranche (completing +1.0 across s01+s04).
        # Central-event bone for capability-full-deployment: concrete SVO — insects (subject) fill (transitive physical verb) named location (object). EVENT-NOT-CONCRETE check: passes.

      - slug: b01c12s04n14
        svo: "the muddy-way entry closes the fifth-ward circuit"
        shape: held
        # Phase-3 dramatist REVISE-2: causal-bridge bone inserted between n02 and n03 (positionally; slug n14 monotonic).
        # Addresses cold-read s04-seam + admin DEC-0076: makes the full-deployment threshold a CONSEQUENCE of this afternoon's
        # muddy-way fill (n02), not an asserted fact at n03. The muddy-way ledger-entry closing the fifth-ward circuit is the
        # physical act that completes the five-ward aggregate for the first time. No exposition, no proper noun, no axis-move.
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "the muddy-way entry completing the fifth-ward circuit is the physical cause of the full-deployment aggregate — the last accumulation beat before the threshold; legibility held at 5.5 (the shape-word has not surfaced yet); the held-discipline against the approaching threshold. This is the causal connective the cold-read flagged missing (s04-seam / DEC-0076): muddy-way filled (n02) -> fifth-ward circuit closes (here) -> feed returns all five (n03) as a new complete total"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: the muddy-way ledger-entry + the fifth-ward circuit as named physical ledger surfaces; concrete close-act.

      - slug: b01c12s04n03
        svo: "the feed returns all five wards"
        shape: held
        # Phase-2 fix: fault-021 — chatter→held; moral_legibility_to_self attached (s04 declared held axis per meta-rule 2)
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "full-circuit feed returning all five wards simultaneously — aggregate shape now differs from any prior count; moral_legibility holds at 5.5 because the word has not yet surfaced; the shape of the whole is what will surface it; held-discipline against the approaching threshold"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # The aggregate shape at full deployment, establishing the referent-weight that makes the shape-word land.

      - slug: b01c12s04n04
        svo: "the count runs the full-circuit return"
        shape: held
        # Phase-2 fix: fault-022 — dropped PP "through the full-circuit return" (banned direction-preposition); bare intransitive motion recast to transitive "runs" + concrete ledger-object (established idiom per s04n07 "the accounting runs the harm-prevention column"); chatter→held; moral_legibility_to_self attached (s04 declared held axis per meta-rule 2)
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "the count runs the full-circuit return at full deployment — the aggregate scale establishing the referent-weight that presses toward the threshold; legibility held at 5.5 as the shape of the whole is yet to surface the word"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # The counting-as-physical-act (the count as it always runs); establishes the aggregate scale before the threshold-cross.

      - slug: b01c12s04n05
        svo: "the feed returns the Flea Bottom approaches"
        shape: held
        # Phase-2 fix: fault-023 — chatter→held; moral_legibility_to_self attached (s04 declared held axis per meta-rule 2)
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "Flea Bottom approaches returning at full scale — the accumulation beat before the threshold crossing; legibility held at 5.5; the word has not surfaced yet but the density of the full-feed presses toward it"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # Accumulates the referent-weight — rhymes-with-framing building: full-feed density established before the word surfaces.

      - slug: b01c12s04n06
        svo: "the accounting reaches the aggregate-shape entry"
        shape: held
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The aggregate-shape entry is the threshold where the internal accounting's natural shape-word surfaces; the accounting reaches this entry and the architecture's own scope becomes the opposing-force; moral_legibility_to_self held at 5.5 — the crack is present but not opening; the suppression is what keeps it held"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # opposing_force visible: the aggregate scale itself is the pressure; the architecture's scope pushes toward the shape-word.

      - slug: b01c12s04n07
        svo: "the accounting runs the harm-prevention column"
        shape: held
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The harm-prevention column is the rational framework Taylor uses to suppress the shape-word's claim; the accounting runs it as it always runs — the gap between surveillance-and-inference and the override-method is the held reality; the crack does not open because the harm-prevention logic is still functional; held at 5.5"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s04n08
        svo: "the accounting reaches the breach column"
        shape: held
        # Pre-Phase-6 fix (orchestrator): held axis changed moral_framework -> moral_legibility_to_self to avoid held-on-in-motion
        # (moral_framework is s04's MOVING axis at n13; holding it here would fire HELD-AXIS-UNCONTRACTED since moral_framework is not
        # in s04's declared axes_held). moral_legibility_to_self IS s04's declared held axis and is the truer discipline for this beat:
        # the accounting reaching the breach column at full scale WITHOUT yet recording it as the shape-word is the suppression-discipline.
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The accounting reaches the breach column where the cost-side weight will land — but the entry is not yet written (the moral_framework axis-move belongs to n13). The accounting reaching the column without recording it as what it rhymes with is the suppression-discipline: legibility held at 5.5; the crack does not open. Opposing-force: the breach column's accumulation at full scale is what the shape-word names; the held discipline is the refusal to write it as that."
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s04n09
        svo: "the accounting reaches the shape-word"
        shape: held
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The accounting reaches the shape-word at full-feed density — the word the internal record's own shape produces, the thing-she-did-at-Gold-Morning word, surfaces in one count. EARTH-BET FENCE HOLD: 'the shape-word' — no proper noun. The suppression-discipline is what keeps moral_legibility_to_self from opening; the word is there for the duration of one count; the axis stays held at 5.5 because the word does not settle. Opposing-force: the architecture's own aggregate scale is the pressure — irreducible, not argument"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # Central-event bone for Khepri-word-surfaces: the accounting (established subject-idiom from b01-c02) reaches (established verb-idiom from b01-c02 line 38: "the accounting reaches the ward-junction entry") the shape-word (object). Earth-Bet fence clean. Accumulated referent-weight from n03-n08 makes this land as felt weight. EVENT-NOT-CONCRETE check: "reaches" with "the shape-word" as object is borderline — the shape-word is an abstraction. However: the accounting reaching for a word in an internal ledger IS the concrete physical act of this world (the feed-accounting is the physical process); "the shape-word" is the project's established cipher-noun for the Khepri-referent within the Earth-Bet fence. Acceptable under the project idiom; closest possible concrete formulation within the fence constraint.

      - slug: b01c12s04n10
        svo: "the accounting advances the count"
        shape: held
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The accounting advances the count forward without settling on the shape-word — the suppression act enacted as a physical ledger-progression; the count continues; the word is not in the next entry because the next entry does not require it; held at 5.5; opposing-force: the architecture's irrevocable scope presses for the shape-word's settlement and the accounting routes around it"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false

      - slug: b01c12s04n11
        svo: "taylor-hebert-kl-122ac closes the architecture entry"
        shape: held
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "The architecture entry closes without the shape-word in it — the suppression is complete in physical-ledger form; the feed continues past the suppression at full deployment; the crack is held shut. The indifferent-world-continuance: the feed running on after the suppression is the physical fact that the suppression succeeded at holding the axis. Opposing-force: the architecture's own scope (irrevocable, structural, not walkable-back by pulling any single node) presses for the shape-word's settlement; Taylor closes the entry instead"
          - axis: political_register-prot
            # Phase-6 fix fault-003: s04 contract declares political_register-prot held but no bone enacted it (HELD-AXIS-NOT-WITNESSED). Enacted here.
            rationale: "The architecture entry closes in flat operational register — the Khepri-suppression is internal, not feed-facing; no contempt-register fires on the close; the accounting runs as it always runs, the same cold-utilitarian mode as every prior entry; political_register-prot held at 3.5 through the suppression sequence"
        cost_ledger_anchor: null
        grounding: true
        dialogue_anchor: false
        # grounding: Taylor's hand closing a specific physical column in the ledger record (the architecture entry = a named surface in the ledger). Named physical act.

      - slug: b01c12s04n12
        svo: "the ledger entry takes the full-circuit count"
        shape: held
        # Phase-2 fix: flag-003 — recast from chatter-with-cl05 to held; removes redundant third cl05 citation (n02 gain + n13 cost already exhaust cl05); capability +0.5 stays solely on n02
        axis_moves: []
        axes_held:
          - axis: moral_legibility_to_self
            rationale: "the ledger-record close of the capability gain — the full-circuit count filed; legibility held at 5.5; record-close parallel to s03n12"
          - axis: social_tether-antag
            # Phase-6 fix fault-004: s04 contract declares social_tether-antag held but no bone enacted it (HELD-AXIS-NOT-WITNESSED). Enacted here.
            rationale: "the full-circuit count filed in the ledger-record is what the standard deliverable-update to Otto's channel is built from — the apparatus receives the second-ward-cluster confirmation as a routine update; the Khepri-suppression event does not become visible to Otto; his leverage holds structural at 6, does not press, does not advance; social_tether-antag held"
        cost_ledger_anchor: null
        grounding: false
        dialogue_anchor: false
        # The capability axis Δ (+0.5) is fully allocated to n02 (the insect-placement bone, the physical cause). This bone records the formal ledger-side confirmation that the threshold was crossed — a downstream accounting of the n02 action. Held (not anchored) to remove redundant third cl05 citation.

      - slug: b01c12s04n13
        svo: "the breach column takes the threshold entry"
        shape: moving
        axis_moves:
          - axis: moral_framework
            direction: down
            magnitude: 1.0
        axes_held: []
        cost_ledger_anchor: cl05
        grounding: true
        dialogue_anchor: false
        # grounding: the breach column as a named physical surface; the entry going down as a concrete ledger-act.
        # cl05 cost side: the irrevocable-Khepri-repetition threshold crossed; systematic-override now irrevocable at full scale; the ledger records the cost-side weight without the shape-word in it. Central-event bone for [event: moral-framework-ledger-entry-for-threshold] — concrete SVO: the breach column takes the entry. EVENT-NOT-CONCRETE check: "takes" is a concrete transitive verb with physical object ("the threshold entry"); passes.
        # This is the chapter's last axis-moving bone; takes moral_framework -1 → -2.
