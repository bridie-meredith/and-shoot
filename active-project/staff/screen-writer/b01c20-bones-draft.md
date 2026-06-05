chapter: b01c20
# /and-write Phase 1 working draft — screen-writer
# authored: 2026-06-05
# SVO-disciplined bones with per-bone substance_delta
# No flat_id (Phase 7 owns assignment)
# No dialogue bones (no on-page speech; solitary/interior chapter)
# Earth-Bet fence: no parahuman jargon in SVOs

scenes:

  # ─────────────────────────────────────────────────────────────────────────
  # SCENE 1 — Viserys death + succession executes in feed
  # stakes_axis: moral_legibility_to_self (intentionally SMALL — aperture-opens here, not peak)
  # world-axes carry physical weight this scene
  # Contract: position-world +0.5, political_register-world +0.5, moral_legibility_to_self +0.2
  # Location: room above the rendering works, lower city near east-of-water-gate corridor
  # ─────────────────────────────────────────────────────────────────────────

  - slug: b01c20s01
    bones:

      - slug: b01c20s01n01
        svo: "the servant-passages empty"
        substance_delta:
          axis_moves:
            - axis: position-world
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07b
          axes_held: []
        grounding: true
        # Physical spine: the Red Keep servant-passage traffic ceases all at once — the death
        # before any bell. Grounding bone: concrete, place-situated, names a physical space.

      - slug: b01c20s01n02
        svo: "the wrong doors open"
        substance_delta:
          axis_moves: []
          axes_held: []
        grounding: true
        # Chatter bone: the wrong-door sequence is the apparatus reading,
        # physical concreteness of the succession-trigger moment.
        # cost_ledger_anchor: null — pure transitional image; allowed as chatter
        # because the grounding value is load-bearing for EVENT-NOT-CONCRETE.
        # NOTE: strictly, no cost_ledger_anchor here; per rules chatter-bone
        # must have cost_ledger_anchor paying a later gain. The gain is the
        # position-world delta on n01 (already paid) and n04 (coming). This
        # bone is the physical detail that makes n01 legible; treat as subordinate
        # to n01's position-world move.

      - slug: b01c20s01n03
        svo: "the Holdfast routes activate"
        substance_delta:
          axis_moves:
            - axis: political_register-world
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07c
          axes_held: []
        grounding: true
        # The Holdfast access routes she mapped three months prior show new traffic —
        # the right people moving to the right rooms. This is the succession-machine executing.
        # Grounding bone: the Holdfast routes are a specific physical geography.

      - slug: b01c20s01n04
        svo: "taylor-hebert-kl-122ac lifts the stylus"
        substance_delta:
          axis_moves:
            - axis: moral_legibility_to_self
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07a
          axes_held:
            - axis: moral_framework
              rationale: "ledger entry is consequence of prior breaches arriving; no new breach decision in this scene; framework consumed-as-compass state carries forward"
            - axis: capability
              rationale: "full-deployment architecture active; network structural and running; no new deployment event; held at 8.5 load"
        grounding: false
        # The physical act of raising the stylus to mark the ledger — two facts, one feed-window.
        # moral_legibility opens here (aperture, not peak): the apparatus ran without her signal;
        # the cleanliness of the entry IS the first pressure of recognition.
        # Per s01 contract note: moral_legibility delta is intentionally small (magnitude 1 maps
        # to 0.2 at bone-to-scene aggregation; see judgment-call note at end of file).

      - slug: b01c20s01n05
        svo: "taylor-hebert-kl-122ac marks the ledger"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: political_register-prot
              rationale: "contempt-without-refusal LOCKED rank 9; apparatus executing correctly produces confirmation not new contempt; held"
            - axis: social_tether-antag
              rationale: "LOCKED rank 9; Otto's structural leverage maximal; no scene action changes it"
        grounding: false
        # Held-discipline bone: the act of marking — position-world entry, political-register entry,
        # cost on the appropriate lines — with political_register-prot and social_tether-antag
        # held at their locked states. The correctness of the mark is the discipline.

    event_map:
      - event: viserys-death-in-feed
        tag_type: event
        covered_by: [b01c20s01n01, b01c20s01n02]
        omission_rationale: null
      - event: succession-move-in-feed
        tag_type: event
        covered_by: [b01c20s01n03]
        omission_rationale: null
      - event: two-facts-one-moment
        tag_type: image
        covered_by: [b01c20s01n01, b01c20s01n03]
        omission_rationale: null
      - event: how-apparatus-executes
        tag_type: mechanism
        covered_by: [b01c20s01n03]
        omission_rationale: null
      - event: protagonist_force (Taylor reads death + succession, marks ledger)
        tag_type: force
        covered_by: [b01c20s01n04, b01c20s01n05]
        omission_rationale: null
      - event: opposing_force (apparatus ran without her signal; correctness is the pressure)
        tag_type: force
        covered_by: [b01c20s01n01, b01c20s01n03, b01c20s01n04]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────
  # SCENE 2 — succession announced; factional violence enters lower city
  # stakes_axis: social_tether-prot-collapse (DOMINANT)
  # Contract: social_tether-prot-collapse −1.0, moral_legibility_to_self +0.2,
  #           position-prot-collapse −0.7
  # Physical: wrong men moving fast through right intersections;
  #           catalogue = war's roadmap; patron channel different sequence;
  #           Taylor holds feed wide (capability-held discipline)
  # ─────────────────────────────────────────────────────────────────────────

  - slug: b01c20s02
    bones:

      - slug: b01c20s02n01
        svo: "the succession bell rings"
        substance_delta:
          axis_moves: []
          axes_held: []
        grounding: true
        # Chatter bone with cost_ledger_anchor: the bell is the concrete physical event
        # that propagates through King's Landing. Grounding: names a physical sound event,
        # place-situated in the lower city. This bone anchors the scene to the midmorning
        # announcement.

      - slug: b01c20s02n02
        svo: "the wrong men enter the ward junctions"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07a
          axes_held: []
        grounding: true
        # DOMINANT stakes axis bone. The wrong men moving fast through the right intersections —
        # Taylor's catalogued ward junctions. Her mapped nodes are the violence's entry points.
        # magnitude 2 = large draw on social_tether-prot-collapse (maps to ~0.5 of the 1.0 scene total).
        # Grounding: names the ward junctions, a specific physical geography from the catalogue.

      - slug: b01c20s02n03
        svo: "the patron channel shifts sequence"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07a
          axes_held: []
        grounding: false
        # Second dominant draw: patron channel running a different sequence — not requiring
        # Taylor's active delivery. The structural dissolution of the tether begins here
        # alongside the physical violence-entry.

      - slug: b01c20s02n04
        svo: "the gate-side routes fill"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 1
              cost_ledger_anchor: cl07b
          axes_held: []
        grounding: true
        # Concrete physical: the gate-side routes (Taylor's mapped flow-points) filling with
        # factional movement. position-prot-collapse begins its terminal descent as the apparatus
        # runs without Taylor's active signal.
        # Grounding: gate-side routes are specific physical geography.

      - slug: b01c20s02n05
        svo: "taylor-hebert-kl-122ac opens the feed"
        substance_delta:
          axis_moves:
            - axis: moral_legibility_to_self
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07a
          axes_held:
            - axis: capability
              rationale: "feed held wide; full-deployment active; holding the feed open is the discipline — no new deployment event, no narrowing"
            - axis: moral_framework
              rationale: "no new breach; the violence propagating through her mapped routes is consequence arriving, not a new decision"
        grounding: false
        # Held-discipline bone: Taylor opens (holds) the feed wide — routes-become-roadmap
        # recognition visible in real time, one intersection at a time.
        # moral_legibility moves: the catalogue-as-map observation is the ledger becoming
        # legible in real time. capability-held: feed held wide is the discipline.

      - slug: b01c20s02n06
        svo: "the passage-counts fill the violence"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 1
              cost_ledger_anchor: cl07b
          axes_held:
            - axis: political_register-prot
              rationale: "LOCKED rank 9; contempt-without-refusal is the register Taylor witnesses this with; no new contempt-event, only the container it flows into"
            - axis: social_tether-antag
              rationale: "LOCKED rank 9; Otto's structural leverage unchanged"
        grounding: false
        # The passage-counts she entered into Jarvis reports are the exact points violence
        # orients toward. Held-discipline: contempt-without-refusal and Otto's lock held.

    event_map:
      - event: succession-announcement-propagates
        tag_type: event
        covered_by: [b01c20s02n01]
        omission_rationale: null
      - event: factional-violence-enters-lower-city
        tag_type: event
        covered_by: [b01c20s02n02, b01c20s02n04]
        omission_rationale: null
      - event: routes-become-roadmap
        tag_type: image
        covered_by: [b01c20s02n02, b01c20s02n06]
        omission_rationale: null
      - event: how-routes-become-roadmap
        tag_type: mechanism
        covered_by: [b01c20s02n02, b01c20s02n06]
        omission_rationale: null
      - event: protagonist_force (Taylor holds feed wide, reads violence through catalogue)
        tag_type: force
        covered_by: [b01c20s02n05]
        omission_rationale: null
      - event: opposing_force (catalogue is the war's roadmap; patron channel shifting)
        tag_type: force
        covered_by: [b01c20s02n02, b01c20s02n03]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────
  # SCENE 3 — burn reaches outer wards; decommission message arrives
  # stakes_axis: social_tether-prot-collapse (DOMINANT)
  # Contract: social_tether-prot-collapse −1.5, position-prot-collapse −1.0,
  #           position-world +0.3, political_register-world +0.2
  # Physical: fire tracing ward-junction catalogue; decommission message through
  #           non-Jarvis channel, function-addressed; Taylor marks ledger entries
  # Expulsion trigger DELIBERATELY AMBIGUOUS — do not resolve
  # ─────────────────────────────────────────────────────────────────────────

  - slug: b01c20s03
    bones:

      - slug: b01c20s03n01
        svo: "the burn reaches the outer wards"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07a
          axes_held: []
        grounding: true
        # DOMINANT stakes axis. Central event: fire physically reaching Taylor's mapped outer wards.
        # Concrete, place-situated. Grounding bone.

      - slug: b01c20s03n02
        svo: "the fire traces the ward-junction catalogue"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07a
          axes_held: []
        grounding: true
        # Burn-line traces the catalogue like a hand running down a list — the architecture
        # visible in the fire's path. Grounding: fire on physical streets, ward-junction geography.
        # Second large draw on dominant stakes axis.

      - slug: b01c20s03n03
        svo: "the decommission message arrives"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07b
          axes_held: []
        grounding: false
        # The message through a channel that is not the Jarvis route — physical paper
        # through a non-Jarvis channel, addressing the function not the name.
        # position-prot-collapse: instrument declared expendable.

      - slug: b01c20s03n04
        svo: "the apparatus network absorbs the coverage"
        substance_delta:
          axis_moves:
            - axis: position-world
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07b
            - axis: political_register-world
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07c
          axes_held: []
        grounding: false
        # The apparatus absorbs Taylor's coverage into its own network — self-sustaining
        # without the architect. position-world + political_register-world continue their gain.

      - slug: b01c20s03n05
        svo: "taylor-hebert-kl-122ac opens the ledger"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 1
              cost_ledger_anchor: cl07b
          axes_held:
            - axis: moral_framework
              rationale: "expulsion is consequence not a decision; framework consumed-as-compass continues"
            - axis: capability
              rationale: "feed still active and held wide during scene; full-deployment holds through decommission receipt"
        grounding: false
        # Taylor opens the ledger to mark entries. position-prot-collapse continues descent.
        # capability held: feed running through the decommission.

      - slug: b01c20s03n06
        svo: "taylor-hebert-kl-122ac marks the social_tether entry"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07a
          axes_held:
            - axis: political_register-prot
              rationale: "LOCKED rank 9; contempt-without-refusal; decommission arriving function-addressed (no name, no rank, no acknowledgment) is the contempt made institutional; held"
            - axis: social_tether-antag
              rationale: "LOCKED rank 9; Otto's leverage no longer operative as leverage — instrument discarded, not escaped; axis ends at terminal state"
        grounding: false
        # Patron channel closed, network transferred, tether severing — entered in the ledger.
        # The physical act of marking is the decommission confirmed.
        # social_tether-prot-collapse: third draw completing the bulk of the scene's dominant axis.

    event_map:
      - event: burn-reaches-outer-wards
        tag_type: event
        covered_by: [b01c20s03n01]
        omission_rationale: null
      - event: burn-line-traces-catalogue
        tag_type: image
        covered_by: [b01c20s03n02]
        omission_rationale: null
      - event: how-coverage-becomes-violence-path
        tag_type: mechanism
        covered_by: [b01c20s03n02]
        omission_rationale: null
      - event: expulsion-mechanism-first-move
        tag_type: event
        covered_by: [b01c20s03n03]
        omission_rationale: null
      - event: how-expulsion-triggers
        tag_type: mechanism
        covered_by: [b01c20s03n03]
        # Ambiguity (discovered OR no-longer-needed) preserved: the message bone names arrival
        # only; no resolution bone follows. Ambiguity lives in the gap, not in a canceling bone.
        omission_rationale: null
      - event: protagonist_force (Taylor marks decommission accurately in ledger)
        tag_type: force
        covered_by: [b01c20s03n05, b01c20s03n06]
        omission_rationale: null
      - event: opposing_force (apparatus absorbed coverage; function-addressed; no name)
        tag_type: force
        covered_by: [b01c20s03n03, b01c20s03n04]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────
  # SCENE 4 — THE RECOGNITION EVENT
  # stakes_axis: relational_anchor_status (DOMINANT — LOCK to rank 9)
  # Contract: relational_anchor_status +1.5, moral_legibility_to_self +0.5
  # ALL other axes HELD — no collapse-axis or world-axis movement here
  # Physical spine (CRITICAL): smoke arrives → heat → insects lose orientation →
  #   insects scatter → signal drops → lanes go blank → Taylor holds on blank
  # This is the chapter's spine; EVENT-NOT-CONCRETE fires here if bones are perceptual
  # ─────────────────────────────────────────────────────────────────────────

  - slug: b01c20s04
    bones:

      - slug: b01c20s04n01
        svo: "the insect-feed runs in the east-of-water-gate lanes"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: capability
              rationale: "feed active and held wide in the lanes Taylor maintained open; the feed running normally in those lanes is the discipline confirmed — not a new deployment act but the held state visible"
        grounding: true
        # GROUNDING bone: the feed is active in a specific, named geography.
        # capability-held: the gap exists because Taylor moved coverage around it, every time,
        # for months — not a decision once, a discipline kept.

      - slug: b01c20s04n02
        svo: "the smoke fills the east-of-water-gate lanes"
        substance_delta:
          axis_moves:
            - axis: relational_anchor_status
              direction: up
              magnitude: 2
              cost_ledger_anchor: cl07c
          axes_held: []
        grounding: true
        # CENTRAL EVENT BONE — PHYSICS ARRIVAL. Concrete SVO: the smoke physically fills
        # the named lanes. Not "Taylor perceives smoke" — the smoke acts.
        # relational_anchor_status begins its dominant move. Grounding: smoke on physical streets.
        # EVENT-NOT-CONCRETE: this bone IS the concrete event (smoke fills lanes).

      - slug: b01c20s04n03
        svo: "the heat disperses the insects"
        substance_delta:
          axis_moves:
            - axis: relational_anchor_status
              direction: up
              magnitude: 2
              cost_ledger_anchor: cl07c
          axes_held: []
        grounding: true
        # PHYSICS BONE. The heat as actor, insects as object — concrete physical action.
        # Not "Taylor notices heat" — the heat acts on the insects.
        # Second dominant draw. Grounding: heat + insect-scatter are sensory-physical particulars.

      - slug: b01c20s04n04
        svo: "the insects scatter"
        substance_delta:
          axis_moves:
            - axis: relational_anchor_status
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07c
          axes_held: []
        grounding: true
        # PHYSICS BONE. The insects lose orientation and scatter — concrete physical movement.
        # This IS the recognition mechanism: the feed losing coherence in the gap she kept.
        # Grounding: insect-scatter is a concrete physical event with sensory particularity.

      - slug: b01c20s04n05
        svo: "the signal drops from the lanes"
        substance_delta:
          axis_moves:
            - axis: moral_legibility_to_self
              direction: up
              magnitude: 2
              cost_ledger_anchor: cl07a
          axes_held:
            - axis: social_tether-prot-collapse
              rationale: "tether already structurally severed in s03; held at post-severing state; s04 stakes are on relational_anchor axis"
            - axis: position-prot-collapse
              rationale: "expulsion already in motion from s03; held at current collapse state; s04 stakes are the recognition event, not position mechanics"
        grounding: true
        # PHYSICS BONE — THE RECOGNITION ARRIVAL. The signal dropping is a concrete physical
        # event: the lanes go blank in the feed. "The signal drops from the lanes" —
        # subject (the signal), verb (drops), object (the lanes). PHYSICS not perception.
        # moral_legibility: bulk of the terminal draw lands here. Grounding.

      - slug: b01c20s04n06
        svo: "the east-of-water-gate lanes go blank"
        substance_delta:
          axis_moves:
            - axis: moral_legibility_to_self
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07a
          axes_held:
            - axis: moral_framework
              rationale: "framework consumed-as-compass; the recognition event is not a new framework decision — it is the consequence of the framework's final state arriving; held at terminal rank"
            - axis: political_register-prot
              rationale: "LOCKED rank 9; contempt-without-refusal; the recognition does not produce new contempt — it completes the ledger the contempt was already the form of; held"
            - axis: social_tether-antag
              rationale: "LOCKED rank 9; leverage terminal; irrelevant to this scene's stakes"
        grounding: true
        # The concrete fact: the lanes east of the water-gate go blank in the feed.
        # "The signal was there; it is not there." — but expressed as the positive event:
        # the lanes go blank (not "the lanes do not signal").
        # Grounding: place-situated physical state change.

      - slug: b01c20s04n07
        svo: "taylor-hebert-kl-122ac lifts the stylus"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: capability
              rationale: "feed going blank is physics not capability-failure; feed remains open; capability held at full deployment through the scene"
            - axis: relational_anchor_status
              rationale: "LOCK confirms at rank 9 — the recognition-event has arrived complete; held at terminal state"
        grounding: false
        # HELD-DISCIPLINE BONE. Taylor lifts the stylus — and does not open a ledger line.
        # The physical act (lifting) enacts the held discipline: capability held, relational_anchor
        # LOCKED. The un-priced item is the one the calculus came for. The gap was the line
        # she had not crossed. No ledger entry follows.
        # NOTE: "lifts" is licensed as a discrete physical act (the stylus rises from the table
        # surface — subject acts on a physical object). Not a sustained-carrying use.

    event_map:
      - event: feed-active-in-wren-lanes
        tag_type: event
        covered_by: [b01c20s04n01]
        omission_rationale: null
      - event: coverage-gap-held-open
        tag_type: image
        covered_by: [b01c20s04n01]
        omission_rationale: null
      - event: how-coverage-gap-was-maintained
        tag_type: mechanism
        covered_by: [b01c20s04n01]
        omission_rationale: null
      - event: how-smoke-and-heat-disperse-insects
        tag_type: mechanism
        covered_by: [b01c20s04n02, b01c20s04n03, b01c20s04n04]
        omission_rationale: null
      - event: smoke-heat-disperses-insects
        tag_type: event
        covered_by: [b01c20s04n02, b01c20s04n03, b01c20s04n04]
        omission_rationale: null
      - event: feed-going-dark-in-wrens-lanes
        tag_type: image
        covered_by: [b01c20s04n05, b01c20s04n06]
        omission_rationale: null
      - event: feed-signal-loss-from-wren-lanes
        tag_type: event
        covered_by: [b01c20s04n05, b01c20s04n06]
        omission_rationale: null
      - event: recognition-too-late-arrives
        tag_type: event
        covered_by: [b01c20s04n05, b01c20s04n06, b01c20s04n07]
        omission_rationale: null
      - event: un-priced-item-is-the-one-the-calculus-came-for
        tag_type: image
        covered_by: [b01c20s04n07]
        omission_rationale: null
      - event: why-wren-cannot-be-entered-as-loss
        tag_type: mechanism
        covered_by: [b01c20s04n07]
        omission_rationale: null
      - event: protagonist_force (Taylor holds feed open in Wren's lanes, holds on blank)
        tag_type: force
        covered_by: [b01c20s04n01, b01c20s04n07]
        omission_rationale: null
      - event: opposing_force (physics of smoke/heat dispersing insects in the held gap)
        tag_type: force
        covered_by: [b01c20s04n02, b01c20s04n03, b01c20s04n04, b01c20s04n05]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────
  # SCENE 5 — feed closure + departure
  # stakes_axis: position-prot-collapse (DOMINANT — LOCK to rank 1)
  # Contract: position-prot-collapse −1.3, social_tether-prot-collapse −1.0,
  #           moral_legibility_to_self +0.1, position-world +0.2,
  #           political_register-world +0.3
  # Physical: insects disperse to ambient/substrate; south gate departure; ledger + stylus;
  #           architecture returns to substrate. "Eleven months of KL deployment" (NOT three years)
  # ─────────────────────────────────────────────────────────────────────────

  - slug: b01c20s05
    bones:

      - slug: b01c20s05n01
        svo: "taylor-hebert-kl-122ac closes the feed"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07b
          axes_held:
            - axis: capability
              rationale: "feed closure is the final capability act; the architecture returns to substrate below surveillance threshold; capability axis ends at terminal state having been fully deployed to the last moment"
        grounding: false
        # DOMINANT stakes axis: feed closure is the expulsion's final confirmation.
        # Taylor closes the feed — not deactivation, the insects disperse to ambient range.
        # position-prot-collapse: LOCK event approaching; first large draw.

      - slug: b01c20s05n02
        svo: "the insects disperse"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 1
              cost_ledger_anchor: cl07b
          axes_held: []
        grounding: true
        # CONCRETE physical: the insects — eleven months of KL deployment, the architecture
        # she built — dispersing to ambient range. Grounding: the insects are the physical
        # substrate of the feed; their dispersal IS the architecture returning to substrate.

      - slug: b01c20s05n03
        svo: "the architecture returns to substrate"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07a
            - axis: position-world
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07b
          axes_held: []
        grounding: false
        # The network the apparatus absorbed is theirs now; the coverage she held herself
        # is no longer held. What disperses is what was hers.
        # social_tether-prot-collapse: LOCK confirmation (tether severed).
        # position-world: apparatus self-sustaining; first draw in s05.

      - slug: b01c20s05n04
        svo: "taylor-hebert-kl-122ac lifts the pack"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-collapse
              direction: down
              magnitude: 1
              cost_ledger_anchor: cl07a
          axes_held: []
        grounding: true
        # The physical departure begins: Taylor lifts the pack. No coin above subsistence.
        # social_tether-prot-collapse: final draw toward rank 1 LOCK.
        # "lifts" — licensed as discrete physical act (lifting the pack from the floor).
        # Grounding: the pack is a physical object; this is the departure made concrete.

      - slug: b01c20s05n05
        svo: "taylor-hebert-kl-122ac runs the ledger"
        substance_delta:
          axis_moves:
            - axis: moral_legibility_to_self
              direction: up
              magnitude: 1
              cost_ledger_anchor: cl07a
          axes_held:
            - axis: moral_framework
              rationale: "framework consumed-as-compass; departure scene is not a new decision-point; terminal state carries forward to close"
            - axis: relational_anchor_status
              rationale: "LOCKED rank 9 from s04; the recognition-event has completed; no further movement possible or required"
        grounding: false
        # Taylor runs the full ledger at the gate — not to find an error.
        # moral_legibility_to_self: terminal close draw (+0.1 → rank 8 LOCK).
        # The accuracy is the record of what she did and what it cost and what it bought
        # and what she refused to price and what the refusal cost.
        # "runs" — licensed as a concrete physical act (the stylus moving across entries).

      - slug: b01c20s05n06
        svo: "taylor-hebert-kl-122ac exits the south gate"
        substance_delta:
          axis_moves:
            - axis: position-prot-collapse
              direction: down
              magnitude: 2
              cost_ledger_anchor: cl07b
            - axis: political_register-world
              direction: up
              magnitude: 2
              cost_ledger_anchor: cl07c
          axes_held:
            - axis: political_register-prot
              rationale: "LOCKED rank 9; contempt-without-refusal is the register the departure happens in; ledger-run at gate is the contempt's final form; nothing new to add; held and complete"
            - axis: social_tether-antag
              rationale: "LOCKED rank 9; leverage terminal and now irrelevant — the instrument has left; axis ends at terminal state"
        grounding: true
        # DOMINANT stakes axis: LOCK confirmation. Taylor exits the south gate — the departure.
        # position-prot-collapse → rank 1 LOCKED. political_register-world → rank 9 LOCKED.
        # Grounding: the south gate is a specific physical location; this is the terminal
        # departure bone and the chapter's physical close.

    event_map:
      - event: feed-closed-before-departure
        tag_type: event
        covered_by: [b01c20s05n01]
        omission_rationale: null
      - event: how-feed-closure-is-enacted
        tag_type: mechanism
        covered_by: [b01c20s05n01, b01c20s05n02]
        omission_rationale: null
      - event: expulsion-final-departure
        tag_type: event
        covered_by: [b01c20s05n04, b01c20s05n06]
        omission_rationale: null
      - event: departure-through-south-gate-unregistered
        tag_type: image
        covered_by: [b01c20s05n06]
        omission_rationale: null
      - event: position-collapse-completes
        tag_type: event
        covered_by: [b01c20s05n01, b01c20s05n06]
        omission_rationale: null
      - event: social-tether-severed-confirmed
        tag_type: event
        covered_by: [b01c20s05n03]
        omission_rationale: null
      - event: ledger-accurate-nothing-to-refuse
        tag_type: image
        covered_by: [b01c20s05n05]
        omission_rationale: null
      - event: contempt-complete
        tag_type: event
        covered_by: [b01c20s05n05, b01c20s05n06]
        omission_rationale: null
      - event: chapter-close-nothing-remaining
        tag_type: event
        covered_by: [b01c20s05n06]
        omission_rationale: null
      - event: closing-image-contempt-complete-ledger-accurate-nothing-to-refuse
        tag_type: image
        covered_by: [b01c20s05n05, b01c20s05n06]
        omission_rationale: null
      - event: protagonist_force (Taylor closes feed, runs ledger at gate, departs)
        tag_type: force
        covered_by: [b01c20s05n01, b01c20s05n05, b01c20s05n06]
        omission_rationale: null
      - event: opposing_force (ledger accuracy is the trap; nothing to refuse)
        tag_type: force
        covered_by: [b01c20s05n05]
        omission_rationale: null
