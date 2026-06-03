# b01c12 scene chunks — /and-substance chapter b01c12 Phases 2–4
# authored: 2026-06-03
# pov_narrator: taylor-hebert-kl-122ac
# dramatic_shape: climax
# scene_count: 4

# ---------------------------------------------------------------------------
# roll-up check
# ---------------------------------------------------------------------------
# axis                       s01    s02    s03    s04    SUM    TARGET   OK?
# moral_framework             0      0      0     -1.0   -1.0   -1.0     YES
# capability                 +0.5    0      0     +0.5  +1.0   +1.0     YES
# relational_anchor_status    0      0     +1.0    0    +1.0   +1.0     YES
# social_tether-prot-rise    +0.5    0      0      0    +0.5   +0.5     YES
# position-prot-rise          0      0     +1.0    0    +1.0   +1.0     YES
# ---------------------------------------------------------------------------
# held axes verified present in axes_held[] on load-bearing scenes:
#   political_register-prot  — s03 (refusal is tactical, not contempt-feed-facing)
#   moral_legibility_to_self — s04 (Khepri-word suppressed; crack held, not opened)
#   social_tether-antag      — s03 (Otto accepts the map boundary; leverage structural, not advancing)
# ---------------------------------------------------------------------------

scenes:

  - slug: b01c12s01
    chunk: |
      Taylor runs the morning circuit east of the water-gate — [image: east-of-water-gate-lanes]
      the lanes that spool off the Gate Road and press into the lower city's
      older skin, where the stone-work pre-dates the Conqueror's harbor improvements
      and the overhangs are close enough to pass messages hand-to-hand across the
      gap. [mechanism: witch-label-trigger-geometry] The insect-cover problem in those
      lanes is structural: any placement dense enough to read traffic requires anchoring
      in the eaves and gutter-joints of the inhabited upper stories, and the inhabitants
      of the east-water-gate lanes know a thing crawling in a close overhang for
      what it is — or what they have agreed to call it — and the label travels faster
      than any observation she could collect. [event: coverage-gap-established] Taylor
      maps the gap's exact boundaries as a formal operational fact: the lanes begin
      where the old gate-tower's shadow falls at second bell and end at the rendering
      yard's east wall, and she has no clean placement inside that boundary without
      the community-safety cost. [image: wren-daily-pattern-through-gap] Wren moves
      through those lanes every morning and every evening — stitch-work pickup, return,
      the wool-merchant at the corner, the back-and-forth a stitch-maker's day makes
      across the same ground — and her movement reads the gap the way a finger traces
      the seam in a thing that is otherwise closed. [mechanism: wren-as-effective-eastern-boundary]
      The coverage map's eastern boundary is Wren's free movement through it: the gap
      exists because the boundary holds, and the boundary holds because Wren passes
      through unindexed-by-Otto, unpriced, her route a fact inside Taylor's internal
      record that goes nowhere else. Taylor extends two new ward-clusters northward off
      the water-gate approach — first of the two additions — and the aggregate shifts
      under her hand. [event: first-ward-cluster-added] The mapping entry closes cleanly.
      The eastern lanes are not in it.
    substance_delta:
      axes_in_motion:
        - axis: capability
          direction: up
          target_delta_magnitude: 0.5
          cost_ledger_anchor: cl05
          notes: >
            First of two ward-cluster additions this chapter; northern approach
            off the water-gate incorporated; aggregate coverage expands;
            cl05 gain side (partial tranche — second 0.5 in s04).
        - axis: social_tether-prot-rise
          direction: up
          target_delta_magnitude: 0.5
          cost_ledger_anchor: cl-d08b
          notes: >
            Coverage-gap boundary-confirmation consolidates tether: Wren's
            free movement in the uncovered lanes closes the map without
            entering the architecture. The consolidation is structural —
            the gap is what keeps the tether intact. cl-d08b. Takes
            social_tether-prot-rise from 8 to 8.5 (at peak).
      axes_held:
        - axis: relational_anchor_status
          rationale: >
            Wren's route is re-mapped and the gap re-confirmed as a
            formal operational fact, but the anchor-status axis-move
            (the cl-d06 settlement) requires the CHOICE — the
            withholding of lane access — as its mechanism. Choice has
            not yet arrived; axis held at 3.5 until s03.
        - axis: political_register-prot
          rationale: >
            Gap-mapping is technical accounting, not contempt-register
            action; no register advance here.
    scene_conflict:
      protagonist_force: >
        Taylor mapping the gap's exact legal boundaries — what the
        coverage can reach without triggering witch-label responses —
        as a cold operational act with no resolution sentence in it.
      opposing_force: >
        The structural geometry of the east-of-water-gate lanes: close
        overhangs, inhabited upper stories, community-label-formation
        already active; the terrain refuses clean placement.
      stakes_axis: social_tether-prot-rise

  - slug: b01c12s02
    chunk: |
      Jarvis arrives at the standard hour with the standard packet — [event: jarvis-delivers-new-request]
      wax, weight, the covering-sheet folded down in the motion Taylor has learned
      to read before she opens anything. The new ask is inside in Otto's flat register:
      [event: otto-requests-east-water-gate-lane-coverage] a Black-faction courier-adjacent
      figure has been using the lanes east of the water-gate to pass messages — not
      carrying them himself but staging handoffs in the rendered dark of the overhangs
      where the street-facing traffic cannot resolve direction. The apparatus wants a
      route-pattern, a frequency, a body-map of the handoff points. [image: packet-describing-the-gap-lanes]
      The ask names the lanes by the gate-tower's old designation and the rendering
      yard's east wall — the exact boundary-marks Taylor spent the morning circuit
      confirming as outside her coverage. [mechanism: request-collides-with-gap-boundary]
      She holds the packet and reads it twice. The ask is precise; it has the shape
      of intelligence that reaches back to someone who already knows the territory
      — [force: otto-apparatus-knowing-the-terrain] not a random survey request but
      a targeted corridor, the kind of request that comes when the apparatus has
      spotted a shape it does not have the resolution to fill. The packet asks for
      exactly what the gap cannot give. [event: collision-between-request-and-gap-confirmed]
      Taylor sets it on the ledger surface. She does not open the coverage-map column
      yet. She re-reads the lane designation. The corridor the packet wants is the
      corridor Wren walks twice a day in both directions, the corridor the map holds
      open because the boundary holds, and the boundary holds because Taylor has
      not placed anything inside it that would cost the boundary what it is worth.
      She sets the stylus down beside the packet. The morning is already warm with
      the kind of warm that comes before the bay-wind clears it.
    substance_delta:
      axes_in_motion: []
      axes_held:
        - axis: relational_anchor_status
          rationale: >
            The collision arrives — the request targets precisely the lanes
            that constitute the gap, the gap that the anchor inhabits — but
            the axis-move belongs to the response (s03), not the delivery
            of the demand. No movement here; held at 3.5.
        - axis: position-prot-rise
          rationale: >
            The withholding-from-Otto position-move (cl02) belongs to the
            refusal act in s03; the request arriving is the condition, not
            the decision. Held at 4.
        - axis: social_tether-antag
          rationale: >
            Otto's apparatus targeting the gap lanes is structural leverage
            expression, not an advance in leverage itself; the request does
            not move the tether-antag axis — that moves only when Otto
            notices the pattern of withholding. He has not noticed yet.
    scene_conflict:
      protagonist_force: >
        Taylor reading the new request against the coverage map she
        spent the morning confirming — holding the packet beside the
        gap it requires her to fill.
      opposing_force: >
        The apparatus's request, precise and terrain-literate: a
        courier-adjacent figure using exactly the lanes Taylor cannot
        enter without paying the community-safety cost to the coverage
        boundary that the east lanes constitute.
      stakes_axis: relational_anchor_status

  - slug: b01c12s03
    chunk: |
      Taylor writes the response. [event: taylor-drafts-refusal-to-otto]
      It is a short entry — the channel expects the flat register the
      deliverables have always used, and what she has to say in flat
      register is brief: the lanes east of the water-gate are not accessible
      within the current coverage parameters; [image: bare-source-field-in-the-response]
      the gap is a structural limit of the architecture, not a temporary
      absence. She does not write why. [mechanism: refusal-without-explanation]
      The explanation would require her to write what lives inside the gap,
      and what lives inside the gap does not go into the channel — it has
      never gone into the channel, not in the source-field of the
      wool-dyer's observation, not in the lane-pattern that returned the
      stitch-maker's route indexed and kept. The response seals without
      a clause added to it. [event: response-sealed-and-routed-to-jarvis]
      She routes it to Jarvis at the standard hour, the packet sitting
      in his hand the way every packet has, the covering-sheet flat
      over the seal, no word added that the contents do not already carry.
      [force: taylor-withholding-the-gap] What she does not route is
      the full operational shape of the gap: the fact that the boundary's
      depth is Wren's pattern through it, that the gap holds because a
      route she keeps only internally moves freely through it each day,
      that the lane-refusal is not a coverage failure but a coverage
      decision she is not naming as one. [force: apparatus-accepting-the-boundary]
      Otto's apparatus does not press — the channel will return an alternate
      arrangement for the courier-adjacent figure's corridor; that is how
      the apparatus handles a coverage limit. Taylor seals the entry.
      She opens the ledger to the relational-anchor column. [event: ledger-entry-anchor-column-opened]
      The column has not moved since the route-indexing tranche — Wren
      indexed, kept, the stitch-maker's days in the internal record and
      out of the deliverable; one tranche settled, one deferred.
      [mechanism: cl-d06-settlement-via-cl-d08-refusal-act]
      She does not write a name. The weight in the column is not a name;
      it is a decision about what the coverage map can reach, and the
      decision's anchor is structural to the architecture that the
      response just confirmed. The entry goes down as a record of the
      gap's operational status. The weight in the column settles under
      her hand — [event: relational-anchor-weight-settles]
      the second tranche of what was already owed, arriving not as a
      payment-date but as a physical fact in the architecture: the lane
      refusal is the mechanism by which the anchor becomes load-bearing
      in the map, because the map now holds the gap as confirmed-and-named,
      and the gap's weight is Wren's free movement through it without
      an entry anywhere that names the reason. She closes the ledger column.
      Her hand stays on it a moment before she lifts it.
    substance_delta:
      axes_in_motion:
        - axis: relational_anchor_status
          direction: up
          target_delta_magnitude: 1.0
          cost_ledger_anchor: [cl-d08, cl-d06]
          notes: >
            Lane-refusal enacted: Wren's free movement constitutes the
            coverage map's eastern boundary without entering the ledger
            (cl-d08 mechanism). SETTLEMENT (DEC-0071): this +1.0 axis-move
            simultaneously settles the outstanding cl-d06 2nd tranche (+1.0)
            that reached end of c08–c10 window unsettled while the axis was
            held flat c08–c11. cl-d08 = mechanism; cl-d06 = the debt.
            One axis-move settles both. Takes relational_anchor_status 3.5
            → 4.5. Closes pl-2026-05-30-001 / pl-2026-06-02-stitch-thread-002.
        - axis: position-prot-rise
          direction: up
          target_delta_magnitude: 1.0
          cost_ledger_anchor: cl02
          notes: >
            Third and most consequential withholding-from-Otto (hook-0014
            third instance). The refusal of lane coverage is no longer
            a quiet pattern — it is a named gap confirmed in the channel,
            a structural limit Taylor has written into the deliverable.
            Position moves toward non-exit confirmation; withholding now
            load-bearing for position, not just a quiet operational
            choice. cl02. Takes position-prot-rise 4 → 5.
      axes_held:
        - axis: political_register-prot
          rationale: >
            The gap-refusal is a tactical operational decision delivered
            in flat channel register. It is not a contempt-register event;
            it is not feed-facing resentment. Held at 3.5.
        - axis: social_tether-antag
          rationale: >
            Otto's apparatus accepts the coverage limit and arranges an
            alternate route. Leverage is structural but not advancing;
            Otto has not noticed the pattern of withholds. Held at 6.
        - axis: moral_legibility_to_self
          rationale: >
            The ledger-column entry is an operational record, not a
            recognition event. Taylor does not name what she is doing
            as protection; she does not notice she is doing the same
            thing she did with Wren's route-indexing. The crack is
            present — it is the same suppression pattern — but it does
            not open this scene. Deferred to d10 suppression event.
    scene_conflict:
      protagonist_force: >
        Taylor writing the refusal in flat operational register — a
        coverage limit, a structural boundary, no explanation appended —
        and sealing the response without the clause that would name what
        the gap protects.
      opposing_force: >
        The apparatus's precision request and what it costs Taylor to
        decline it: a named gap in the deliverable, a withholding that
        is now load-bearing and visible in the channel record, the
        relational-anchor weight settling in the ledger column without
        a name to carry it.
      stakes_axis: position-prot-rise

  - slug: b01c12s04
    chunk: |
      The second ward-cluster addition runs in the late afternoon —
      [event: second-ward-cluster-added] the coverage extending past
      the water-gate approach northward into the Muddy Way's upper
      margin, filling a gap in the existing architecture that has been
      a planning entry for two circuits without becoming an action.
      [image: aggregate-feed-scale-at-full-deployment] Taylor works
      the placement across the standard circuit, the count moving in
      her the way the count has always moved, and then the aggregate
      is different — not in any single node but in the shape of the
      whole, the feed returning the city at a density and a completeness
      that it has not returned before, all five wards and the
      Flea Bottom approaches mapped and simultaneous. [mechanism: khepri-threshold-crossed-in-aggregate]
      She is reading bodies she has never asked, routes she has never
      offered to keep, the architecture complete in scope and structural
      to the channel in a way that cannot be walked back by pulling
      any single node — the pull would leave a shape the whole could
      not hold. She holds the feed at full scale for the count.
      [event: internal-accounting-runs-at-full-scale]
      The accounting runs the way the accounting always runs: the gain
      set against the cost, the harm-prevention column against the
      breach column, the architecture's scope against what the
      scope rhymes with. It is not an exact rhyme. It was never an
      exact rhyme. The gap between the surveillance-and-inference method
      and the override method is real and she has built her entire
      operating framework on the reality of that gap. The gap is still
      real. The aggregate scale is also real. At full scale, running
      the accounting at full-feed density, the word her internal record
      reaches for is [event: khepri-word-surfaces-in-accounting] not
      a description of the architecture but the name of the thing it
      rhymes with — the shape-word, the thing-she-did-at-Gold-Morning
      word, the word she has not used in any column because the column
      does not require it and because the gap is real. The word is
      there in the accounting for the duration of one count.
      [mechanism: khepri-suppression-act] She does not let it settle.
      The accounting moves past the count — the gain column, the cost
      column, the harm-prevention logic, the architecture's operational
      necessity — and the word is not in the next entry because the
      next entry does not require it, and the gap is real, and the
      word does not help the count run. [image: feed-continuing-past-the-suppression]
      The feed returns the city at full scale. She closes the
      architecture entry. [event: capability-full-deployment-confirmed]
      The ledger entry for the second ward-cluster goes down clean.
      The breach column receives its entry: the threshold crossed,
      the scope irrevocable, the shape of the accounting that reached
      for the shape-word and was given something else to do instead.
      The entry does not contain the word. [event: moral-framework-ledger-entry-for-threshold]
      The entry contains what happened: the architecture at full scale,
      the count completed, the harm-prevention logic intact, and the
      cost side receiving its full weight. She closes the ledger. The
      feed runs on at full deployment the way it will run for every
      circuit that follows this one, the coverage complete, the
      architecture structural, the gap east of the water-gate
      the one place the map does not go.
    substance_delta:
      axes_in_motion:
        - axis: capability
          direction: up
          target_delta_magnitude: 0.5
          cost_ledger_anchor: cl05
          notes: >
            Second of two ward-cluster additions (first in s01);
            full-deployment threshold crossed — architecture complete
            in scope, all five wards + Flea Bottom approaches mapped
            simultaneously; cl05 gain side (second partial tranche,
            completing the +1.0 across s01+s04). Takes capability
            5.5 + 1.0 → 6.5 across the chapter.
        - axis: moral_framework
          direction: down
          target_delta_magnitude: 1.0
          cost_ledger_anchor: cl05
          notes: >
            Irrevocable-Khepri-repetition threshold crossed: aggregate
            scale at full-feed density reaches the point where the
            internal accounting's natural shape-word is the Khepri
            name; word surfaces in one count and is suppressed;
            the suppression IS the ledger entry (the breach column
            receives full weight); cl05 cost side. Systematic-override
            now irrevocable at this scale — framework consumed as
            compass not yet (that is end-rank 8), but this chapter's
            -1.0 confirms the threshold named internally and filed.
            Takes moral_framework -1 → -2.
      axes_held:
        - axis: moral_legibility_to_self
          rationale: >
            The Khepri-word surfaces and is suppressed — this IS the
            suppressed-recognition pattern, and the ledger records the
            cost-side weight — but the crack does not open fully this
            scene; the recognition is pushed back down, not received.
            Legibility crack deferred to d10 suppression event. Held
            at 5.5. This is the load-bearing held-discipline stakes axis
            for this scene: the suppression is what keeps the axis from
            moving, and the suppression is the chapter's interior climax.
        - axis: political_register-prot
          rationale: >
            Khepri-suppression is internal, not feed-facing; no register
            advance. Held at 3.5.
        - axis: social_tether-antag
          rationale: >
            Otto's channel receives the second ward-cluster confirmation
            via the standard deliverable update; his leverage structural,
            not advancing. Held at 6.
    scene_conflict:
      protagonist_force: >
        Taylor completing the second ward-cluster addition and running
        the full-scale accounting — the architecture at full deployment,
        the harm-prevention logic intact, the count moving forward.
      opposing_force: >
        The aggregate scale itself: at full-feed density, the internal
        accounting reaches for the Khepri shape-word — the architecture's
        own scope is the pressure, internal, irreducible, the thing that
        cannot be argued down because it is not argument.
      stakes_axis: moral_legibility_to_self
