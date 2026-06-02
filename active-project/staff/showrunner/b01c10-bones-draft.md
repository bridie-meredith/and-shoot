# b01c10 bones draft — /and-write Phase 1 scene-decomposition
# Authored: 2026-06-02
# For orchestrator lift into memory.md chapters[b01c10].scenes[].bones[]
# DO NOT edit memory.md from this file — draft only.
#
# Chapter: b01c10
# dramatic_shape: climax
# pov_narrator: taylor-hebert-kl-122ac
# goal: Show the audience the formalization and the detention in the same chapter
#        so the structure is clear: Otto naming the arrangement and Taylor's feed
#        confirming its operational consequence are the same event.
# Context: SILENT CHAPTER — no spoken dialogue expected; zero dialogue-anchor bones.
# Continuity hard-fences:
#   - Taylor and Otto never meet; contact through Jarvis only
#   - "Khepri" must not appear (that beat is c12)
#   - Earth-Bet jargon banned
#   - Corwick is the courier (named c08 via Oswyn; first closed ledger entry with a name)
#
# SVO form reference: b01-c09.md (Phase-2-clean, 27 bones)
# Watch items honored: W1 (s02 surrender), W2 (s04 face-terminal), W3 (s03 absence-read), W4 (aliveness)

---

scenes:

  # ─────────────────────────────────────────────────────────────────────────────
  # SCENE 1: b01c10s01
  # chunk: Jarvis delivers the formalization packet; Otto names the arrangement.
  # axes_in_motion: position-prot-rise +0.5 (cl-d07a), social_tether-prot-rise +0.5 (cl03b)
  # axes_held: moral_framework, relational_anchor_status, political_register-prot,
  #             moral_legibility_to_self
  # scene_conflict.protagonist_force: Taylor's operational discipline — she reads what the packet contains; she does not refuse
  # scene_conflict.opposing_force: the naming itself as institutional act — the text forecloses the informal reading Taylor had been sustaining
  # stakes_axis: position-prot-rise
  # density_target: 0.70-0.80
  # ─────────────────────────────────────────────────────────────────────────────

  - slug: b01c10s01
    bones:

      - slug: b01c10s01n01
        shape: chatter
        svo: "jarvis delivers the packet"
        substance_delta:
          axis_moves: []
          axes_held: []
          cost_ledger_anchor: cl-d07a
          # Chatter — pays the formalization-arrival setup; the packet arrival is the
          # mechanism by which otto-names-the-arrangement; cost_ledger_anchor required
          # because this bone is the enabling physical act for the moving bone n02.
        notes: "grounding-class: physical delivery act. Jarvis as the only channel — Taylor-Otto never direct. Morning station location."

      - slug: b01c10s01n02
        shape: moving
        svo: "the packet-text closes the frame"
        substance_delta:
          axis_moves:
            - axis: position-prot-rise
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl-d07a
          # +0.5 drawn at scene-aggregate; magnitude 1 at bone-level per schema bone.delta_per_axis 1-3
          # (scene target is 0.5; this is the sole moving bone on this axis, magnitude declared 1
          # per DEC-0002 precedent for sub-1.0 scene targets — same shape as c08/c09)
        notes: "Central-event bone: the naming-as-fait-accompli. packet-text is concrete prop object. 'closes the frame' is a physical action (the text as door closing). image: packet-text-closes-the-frame."

      - slug: b01c10s01n03
        shape: held
        svo: "the morning-stone holds the bay-cold"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_framework
              rationale: "formalization names what is already operative; Taylor does not open a new ledger entry on the institutional act itself; the prohibition-against-breach has not been triggered by a packet — framework held at current crack-level by grounding the scene's physical location (feed-station exterior)"
          cost_ledger_anchor: null
        notes: "Grounding bone (W4 aliveness). Physical: morning stone + bay-cold = feed-station exterior sensory anchor. Enacts the setting's cold weight, keeping scene concrete not abstract. Satisfies >=1 grounding bone requirement."

      - slug: b01c10s01n04
        shape: moving
        svo: "taylor-hebert-kl-122ac folds the packet"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-rise
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl03b
          # +0.5 drawn at scene-aggregate; magnitude 1 per DEC-0002 sub-1.0-scene-target precedent
        notes: "Moving bone: the physical act of receiving-and-accepting (folding = processing, not refusing). The tether's structural confirmation is enacted in the body gesture of handling the packet. cl03b future-cost-collateral."

      - slug: b01c10s01n05
        shape: held
        svo: "taylor-hebert-kl-122ac exhales"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_legibility_to_self
              rationale: "Taylor reads the packet and files what it names; the foreclosure is not yet a recognition event; legibility holds — she exhales on the content without interrogating it; the body-response is the non-event of a recognition that does not open"
          cost_ledger_anchor: null
        notes: "Held bone on moral_legibility. Bare intransitive that enacts the held discipline — the exhalation is not-recognition performed as physical action. Parallels b01c01s01n07 ('taylor exhales') in function."

    event_map:
      - event: "jarvis-delivers-formalization-naming [event: jarvis-delivers-formalization-naming]"
        bones: [b01c10s01n01, b01c10s01n02]
        omission_rationale: null
      - event: "otto-names-the-arrangement-through-jarvis [mechanism: otto-names-the-arrangement-through-jarvis]"
        bones: [b01c10s01n02]
        omission_rationale: null
      - event: "packet-text-closes-the-frame [image: packet-text-closes-the-frame]"
        bones: [b01c10s01n02]
        omission_rationale: null
      - event: "otto-names-the-function-explicitly [force: otto-names-the-function-explicitly]"
        bones: [b01c10s01n02, b01c10s01n04]
        omission_rationale: null
      - event: "formalization-as-fait-accompli-not-negotiation [mechanism: formalization-as-fait-accompli-not-negotiation]"
        bones: [b01c10s01n02, b01c10s01n04]
        omission_rationale: null
      - event: "jarvis-as-only-channel-taylor-otto-never-direct [force: jarvis-as-only-channel-taylor-otto-never-direct]"
        bones: [b01c10s01n01]
        omission_rationale: null
      - event: "informal-deniability-foreclosed [event: informal-deniability-foreclosed]"
        bones: [b01c10s01n02, b01c10s01n04]
        omission_rationale: null
      - event: "protagonist_force: Taylor's operational discipline — reads, does not refuse"
        bones: [b01c10s01n04, b01c10s01n05]
        omission_rationale: null
      - event: "opposing_force: naming as institutional act; text closes the informal reading"
        bones: [b01c10s01n02]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────────
  # SCENE 2: b01c10s02
  # chunk: Otto requests Corwick by description; Taylor provides the body-map.
  # axes_in_motion: moral_framework -0.5 (cl03a), social_tether-antag +0.5 (cl-antag-d10)
  # axes_held: position-prot-rise, social_tether-prot-rise, relational_anchor_status,
  #             moral_legibility_to_self, political_register-prot
  # scene_conflict.protagonist_force: Taylor's harm-reduction calculus — Otto has the silhouette; withholding changes nothing
  # scene_conflict.opposing_force: the internal record as distinct substrate — the act of providing collapses a substrate boundary
  # stakes_axis: moral_framework
  # density_target: 0.75-0.85
  #
  # W1 HONOR (s02 Corwick-surrender): substrate-split must be a STRUCTURALLY DISTINCT bone
  # BEFORE the routing bone. The months of accumulated observation must be visible AS bones
  # before they become a delivered line-item. The opposing force (internal-record-as-distinct-
  # substrate) must be visible before the routing bone.
  # ─────────────────────────────────────────────────────────────────────────────

  - slug: b01c10s02
    bones:

      - slug: b01c10s02n01
        shape: chatter
        svo: "the second item opens the packet"
        substance_delta:
          axis_moves: []
          axes_held: []
          cost_ledger_anchor: cl03a
          # Chatter — setup for the request-by-description event; chatter anchor required;
          # anchors cl03a cost-chain (the request is the trigger for the delivery that pays cl03a)
        notes: "Physical: packet as prop, second item as concrete sub-object. Grounding-class."

      - slug: b01c10s02n02
        shape: held
        svo: "the lower-gate road marks the body-map"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: social_tether-antag
              rationale: "Otto's apparatus already knows the courier exists — the request by description is the apparatus making its knowledge visible; the lower-gate road as location surfaces the feed-geography where Taylor built the body-map that Otto does not have; Otto's leverage is visible as the gap between 'silhouette' and 'body-map'; antag leverage is held at sub-peak pending the delivery"
          cost_ledger_anchor: null
        notes: "Grounding bone (W4 / W3 echo): the lower-gate road as physical location names the body-map's geography. This makes the internal record visible as a place-anchored thing before it becomes a delivered item. Otto requests what Taylor's feed uniquely holds. image: silhouette-versus-body-map."

      - slug: b01c10s02n03
        shape: held
        svo: "the body-map fills the feed-record"   # Phase-2 fixer recast (fault-002): was "the errand-corridor geometry weights the internal record" (stative verb + abstract object). feed-record = auditor-accepted object (s04n08); body-map fills it = substrate visible before delivery (W1 opposing-force preserved).
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_framework
              rationale: "opposing force enacted: the internal record as a distinct substrate from the Jarvis channel — the months of accumulated body-map (errand-corridor, posture-classes, lower-gate faction-inference) are a coherent, physically-indexed observation set; this bone makes the substrate visible as a weight before the delivery collapses it; the framework is held at its current crack level by the visibility of what is about to be crossed"
          cost_ledger_anchor: null
        notes: "W1 HONOR — the substrate-split bone. This is the structurally distinct cognitive bone BEFORE the routing bone. 'errand-corridor geometry' is a physical compound (routes, lines of movement); 'weights' is narrowly licensed (internal record as a physically-indexed observation resisting the routing act — stillness-against-the-channel). The months of observation are here as accumulation before the surrender. Opposing force (internal-record-as-distinct-substrate) visible."

      - slug: b01c10s02n04
        shape: held
        svo: "corwick squares the stone-post"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_legibility_to_self
              rationale: "the specific body-posture Taylor accumulated in the feed — the lower-gate posture, the report-delivery stance — is here as a concrete recalled image before it becomes a line-item; legibility holds because Taylor runs the harm-reduction calculus without naming the accumulation as a recognition event; the recalled posture is data, not guilt"
          cost_ledger_anchor: null
        notes: "Grounding bone (W4, W1): Corwick's feed-posture concretized as physical remembered action. 'squares the stone-post' = the lower-gate report-delivery stance from c09. This is the body-map made visible in one concrete image. Satisfies >=1 grounding bone requirement for s02. corwick bare-slug per c08/c09 precedent (pl-2026-06-01-001)."

      - slug: b01c10s02n05
        shape: moving
        svo: "taylor-hebert-kl-122ac translates the record"
        substance_delta:
          axis_moves:
            - axis: moral_framework
              direction: down
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl03a
        notes: "W1 HONOR — translation bone (distinct from routing). The internal record (body-map: name, errand-frequency, posture-classes, lower-gate faction-inference) moves from internal substrate to channel register. This IS the irreversible act: translating the form. 'translates' is a concrete physical-analogue verb (the action of rendering one form into another). The act of translation is irreversible — the substrate split closes on Corwick. cl03a cost side, first tranche (-0.5)."

      - slug: b01c10s02n06
        shape: moving
        svo: "taylor-hebert-kl-122ac routes the record"
        substance_delta:
          axis_moves:
            - axis: social_tether-antag
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl-antag-d10
        notes: "W1 HONOR — routing bone (distinct from translation bone n05). The translated record enters the Jarvis channel. This is the delivery as physical act separate from the translation act. Routes through Jarvis. cl-antag-d10 opening tranche (+0.5). Otto's leverage made structural by receiving what Taylor had been keeping back."

      - slug: b01c10s02n07
        shape: held
        svo: "the wax dries"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: relational_anchor_status
              rationale: "Wren is not in this exchange; anchor holds at rank 3.5; the substrate split closes on Corwick not Wren — the bone that grounds the closure (wax drying = channel sealed) enacts the relational_anchor hold by physically marking the boundary of what was delivered and what was not"
          cost_ledger_anchor: null
        notes: "Grounding bone: wax as physical prop (the packet/channel seal). Enacts closure of the Jarvis channel without Wren's name in it. mechanism: withheld-observation-enters-jarvis-channel is completed."

    event_map:
      - event: "otto-requests-courier-by-description [event: otto-requests-courier-by-description]"
        bones: [b01c10s02n01, b01c10s02n02]
        omission_rationale: null
      - event: "otto-apparatus-knows-courier-exists-but-not-from-taylors-feed [mechanism: otto-apparatus-knows-courier-exists-but-not-from-taylors-feed]"
        bones: [b01c10s02n02]
        omission_rationale: null
      - event: "otto-requests-what-taylors-feed-uniquely-holds [force: otto-requests-what-taylors-feed-uniquely-holds]"
        bones: [b01c10s02n02, b01c10s02n03]
        omission_rationale: null
      - event: "silhouette-versus-body-map [image: silhouette-versus-body-map]"
        bones: [b01c10s02n02, b01c10s02n03]
        omission_rationale: null
      - event: "corwick-name-held-from-oswyn-c08-introduction [mechanism: corwick-name-held-from-oswyn-c08-introduction]"
        bones: [b01c10s02n03, b01c10s02n04]
        omission_rationale: null
      - event: "taylors-body-map-as-withheld-observation-surrendered [force: taylors-body-map-as-withheld-observation-surrendered]"
        bones: [b01c10s02n03, b01c10s02n04, b01c10s02n05]
        omission_rationale: null
      - event: "taylor-provides-corwick-identity-and-pattern [event: taylor-provides-corwick-identity-and-pattern]"
        bones: [b01c10s02n05, b01c10s02n06]
        omission_rationale: null
      - event: "withheld-observation-enters-jarvis-channel [mechanism: withheld-observation-enters-jarvis-channel]"
        bones: [b01c10s02n06, b01c10s02n07]
        omission_rationale: null
      - event: "protagonist_force: harm-reduction calculus — Otto has silhouette; withholding changes nothing"
        bones: [b01c10s02n05, b01c10s02n06]
        omission_rationale: null
      - event: "opposing_force: internal record as distinct substrate — providing collapses a substrate boundary"
        bones: [b01c10s02n03, b01c10s02n04]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────────
  # SCENE 3: b01c10s03
  # chunk: Two days later — Corwick absent from the feed; Gold Cloak patrol posted.
  # axes_in_motion: position-world +1.0 (cl-world-d04), political_register-world +1.0 (cl-world-d07),
  #                 social_tether-antag +1.0 (cl-antag-d10)
  # axes_held: moral_framework, moral_legibility_to_self, relational_anchor_status,
  #             social_tether-prot-rise, position-prot-rise
  # scene_conflict.protagonist_force: Taylor's feed-reading discipline — absence read against prior pattern
  # scene_conflict.opposing_force: operational consequence as perceptual fact — the body that was present is absent
  # stakes_axis: position-world
  # density_target: 0.80-0.90
  #
  # W3 HONOR (s03 absence-read): enact the PRIOR-CIRCUIT PRESENCE-COUNT before the absence
  # reads as deviation. >=1 bone establishing Corwick's recurring pattern BEFORE the absent-body bone.
  # URI-WRITE-EVENT-CONCRETENESS (HARD): central event = concrete physical absence + concrete
  # Gold Cloak posture. Render as body-not-in-geometry + patrol-pair-standing-posted.
  # NOT "the feed flags the detention."
  # ─────────────────────────────────────────────────────────────────────────────

  - slug: b01c10s03
    bones:

      - slug: b01c10s03n01
        shape: held
        svo: "the supply cart marks the lower-gate road"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: position-prot-rise
              rationale: "the supply cart as standing geometry — the lower-gate road baseline that Taylor runs every circuit; the cart's presence enacts the feed's normal body-distribution against which corwick's absence will read; position holds because the world-axis advance (not the protagonist-rise axis) is what this scene moves"
          cost_ledger_anchor: null
        notes: "Grounding bone (W3, W4): supply cart + lower-gate road as physical props — the baseline geometry of the prior circuit. This is bone 1 of the prior-presence-count before absence reads as deviation. The cart was in c09 (@12 'the supply cart marks the lower-gate road') — direct continuity."

      - slug: b01c10s03n02
        shape: held
        svo: "corwick walks the errand-corridor"   # Phase-2 fixer recast (fault-003): was "corwick marks the second-circuit return" (abstract object). errand-corridor = concrete place; recurring presence carried by ordering+notes (W3 prior-presence-count preserved); distinct verb avoids marks-mannerism.
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_framework
              rationale: "Taylor's feed has been reading Corwick every second or third circuit since the Rushwick margin — the prior-circuit presence is the established pattern; the framework holds because the pattern-reading is within the licensed exception (operational intelligence already delivered); no new breach event at this bone; the presence-count is what makes the absence legible as deviation"
          cost_ledger_anchor: null
        notes: "W3 HONOR — prior-circuit presence-count bone. Corwick marking the second-circuit return is a physical act (body returning in the feed geometry). This establishes the pattern BEFORE the absence reads as deviation. 'second-circuit' = the recurring presence; 'marks' is narrowly per c09 precedent (b01c09 @12 'the supply cart marks'; auditor-accepted SIGNAL @marks-verb)."

      - slug: b01c10s03n03
        shape: moving
        svo: "the lower-gate road loses corwick"   # Phase-2 fixer recast (fault-001): was "the lower-gate road returns empty" (resultative-adjective complement). Transitive; absence rendered as positive physical fact (road minus the body); central-event concreteness preserved.
        substance_delta:
          axis_moves:
            - axis: position-world
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl-world-d04
        notes: "Central-event bone — URI-WRITE-EVENT-CONCRETENESS HARD. Concrete physical absence: 'the lower-gate road returns empty' is a grounding-class concrete SVO (the road as physical place-object; 'returns empty' as what the feed-circuit delivers — a location with expected content producing no content). This is the body-not-in-geometry enacted as a physical absence. event: lower-gate-road-returns-empty-in-feed. position-world +1.0 via cl-world-d04: the Green apparatus ran; Corwick's Black-faction logistics thread is closed. The world consolidation IS the empty road."

      - slug: b01c10s03n04
        shape: held
        svo: "the stone-post marks the side-exit"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_legibility_to_self
              rationale: "the stone-post present = the baseline geometry intact minus one body; the recognition that the body-not-in-geometry is Corwick-detained has not yet opened as a named event; Taylor reads the geometry as data; legibility holds because the reading is feed-discipline not recognition; the stone-post's presence (contrasted with Corwick's absence) enacts the non-recognition posture concretely"
          cost_ledger_anchor: null
        notes: "Grounding bone: stone-post + side-exit as physical anchors from c09 (@13 'the stone-post marks the lower gate side-exit'). Baseline-body-geometry-intact-minus-one-body enacted. Satisfies >=1 grounding per 5 bones."

      - slug: b01c10s03n05
        shape: moving
        svo: "the Gold Cloak pair posts the lane-junction"
        substance_delta:
          axis_moves:
            - axis: political_register-world
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl-world-d07
        notes: "Central-event bone — URI-WRITE-EVENT-CONCRETENESS HARD. Concrete Gold Cloak posture: 'the Gold Cloak pair posts the lane-junction' = patrol-pair standing posted (not transiting) at the junction where Corwick's errand-corridor empties into the road. 'posts' = physical act of stationing at a location after an action. image: gold-cloak-pair-at-corwicks-junction. mechanism: patrol-posture-reads-as-post-detention-not-pre. political_register-world +1.0: the Green succession channel is demonstrably operational; the faction-violence sub-pressure has produced its first on-page tactical consequence."

      - slug: b01c10s03n06
        shape: moving
        svo: "the insect-feed sweeps the errand-corridor"
        substance_delta:
          axis_moves:
            - axis: social_tether-antag
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl-antag-d10
        notes: "Moving bone: Taylor runs the feed through the lower-gate approach / lane-cluster that connects to Corwick's errand-corridor. The body is not in the geometry — the feed sweep confirms absence across the corridor. mechanism: taylor-reads-corwick-absence-through-feed-sweep. social_tether-antag +1.0: Otto's apparatus ran within two circuit-passes of Taylor's delivery; the speed confirms integration depth; non-extractable confirmation advancing. event: dance-pressure-pulse-one-complete / green-succession-channel-operational."

      - slug: b01c10s03n07
        shape: held
        svo: "the bay-cold presses the lower road"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: relational_anchor_status
              rationale: "Wren not in this scene; the bay-cold as physical environmental constant grounds the scene's temporal setting (same morning cold as s01) without adding Wren-weight; anchor holds at rank 3.5"
          cost_ledger_anchor: null
        notes: "Grounding bone (W4 aliveness): bay-cold + lower road = the physical sensation of the circuit-pass. Keeps the feed-reading embodied and concrete; prevents the scene from reading as data-record transaction per W4 watch. Second grounding bone for s03."

    event_map:
      - event: "lower-gate-road-returns-empty-in-feed [event: lower-gate-road-returns-empty-in-feed]"
        bones: [b01c10s03n03]
        omission_rationale: null
      - event: "baseline-body-geometry-intact-minus-one-body [mechanism: baseline-body-geometry-intact-minus-one-body]"
        bones: [b01c10s03n01, b01c10s03n04]
        omission_rationale: null
      - event: "corwick-absent-from-feed-geometry [event: corwick-absent-from-feed-geometry]"
        bones: [b01c10s03n02, b01c10s03n03]
        omission_rationale: "The absence is enacted by the presence-count (n02) followed by the empty-road (n03); the physical geometry reads as deviation from established pattern. No additional bone needed."
      - event: "absence-as-read-against-prior-pattern [image: absence-as-read-against-prior-pattern]"
        bones: [b01c10s03n01, b01c10s03n02, b01c10s03n03]
        omission_rationale: null
      - event: "taylor-reads-corwick-absence-through-feed-sweep [mechanism: taylor-reads-corwick-absence-through-feed-sweep]"
        bones: [b01c10s03n06]
        omission_rationale: null
      - event: "corwick-body-removed-from-coverage-geometry [force: corwick-body-removed-from-coverage-geometry]"
        bones: [b01c10s03n03, b01c10s03n06]
        omission_rationale: null
      - event: "secondary-signal-returns-detention-information [event: secondary-signal-returns-detention-information]"
        bones: [b01c10s03n05]
        omission_rationale: null
      - event: "gold-cloak-pair-at-corwicks-junction [image: gold-cloak-pair-at-corwicks-junction]"
        bones: [b01c10s03n05]
        omission_rationale: null
      - event: "patrol-posture-reads-as-post-detention-not-pre [mechanism: patrol-posture-reads-as-post-detention-not-pre]"
        bones: [b01c10s03n05]
        omission_rationale: null
      - event: "green-apparatus-operational-consequence-visible-in-feed [force: green-apparatus-operational-consequence-visible-in-feed]"
        bones: [b01c10s03n05, b01c10s03n06]
        omission_rationale: null
      - event: "dance-pressure-pulse-one-complete [event: dance-pressure-pulse-one-complete]"
        bones: [b01c10s03n05, b01c10s03n06]
        omission_rationale: null
      - event: "green-succession-channel-operational [event: green-succession-channel-operational]"
        bones: [b01c10s03n05]
        omission_rationale: null
      - event: "taylors-network-acted-without-her-consent-or-design [mechanism: taylors-network-acted-without-her-consent-or-design]"
        bones: [b01c10s03n03, b01c10s03n06]
        omission_rationale: null
      - event: "protagonist_force: feed-reading discipline — absence read against prior pattern; Gold Cloak posture-class"
        bones: [b01c10s03n02, b01c10s03n03, b01c10s03n05]
        omission_rationale: null
      - event: "opposing_force: operational consequence as perceptual fact — apparatus ran on what she provided"
        bones: [b01c10s03n05, b01c10s03n06]
        omission_rationale: null

  # ─────────────────────────────────────────────────────────────────────────────
  # SCENE 4: b01c10s04
  # chunk: Taylor opens the ledger; runs the accounting; writes Corwick as closed entry;
  #         face stays in feed-record after ledger closes.
  # axes_in_motion: position-prot-rise +0.5 (cl-d07a), social_tether-prot-rise +0.5 (cl03b),
  #                 moral_framework -0.5 (cl03a), moral_legibility_to_self +0.5 (null anchor — suppressed recognition)
  # axes_held: social_tether-antag, position-world, political_register-world,
  #             relational_anchor_status, political_register-prot,
  #             social_tether-prot-collapse
  # scene_conflict.protagonist_force: Taylor's ledger-accounting discipline — convention; gain and cost are both real; she closes every entry
  # scene_conflict.opposing_force: the face in the feed-record as irresolvable surplus — ledger closes but face does not disappear
  # stakes_axis: moral_legibility_to_self
  # density_target: 0.75-0.85
  #
  # W2 HONOR (s04 face-as-terminal-weight):
  # TWO distinct bones: one for ledger closing, one for the record remaining.
  # The three "he did not consent" beats stay 3 STRUCTURALLY DISTINCT bones.
  # Face must land LAST — not the closure notation.
  # Order: observation / body-map / delivery (three distinct "did not consent" bones)
  # then ledger closes, then face persists. Face is the chapter's final bone-weight.
  # ─────────────────────────────────────────────────────────────────────────────

  - slug: b01c10s04
    bones:

      - slug: b01c10s04n01
        shape: held
        svo: "taylor-hebert-kl-122ac opens the ledger"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: social_tether-antag
              rationale: "the ledger-open is a convention Taylor has run since the first delivery; opening the ledger does not produce new leverage for Otto — it is Taylor's internal accounting convention; antag leverage is structural and confirmed; it holds at the structural-confirmed state from s03"
          cost_ledger_anchor: null
        notes: "Grounding bone: ledger as physical object. 'opens' is licensed as a discrete act of initiating a physical mechanism. event: taylor-opens-ledger-post-detention. mechanism: ledger-as-taylors-accounting-convention."

      - slug: b01c10s04n02
        shape: moving
        svo: "taylor-hebert-kl-122ac writes corwick"
        substance_delta:
          axis_moves:
            - axis: moral_framework
              direction: down
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl03a
        notes: "Moving bone: the physical act of writing Corwick's name as a closed entry. 'writes' = concrete physical verb (stylus/quill on page). corwick bare-slug per precedent. event: corwick-name-enters-ledger-as-closed-entry. image: corwick-name-written-as-closed-ledger-entry. cl03a cost side, second tranche (-0.5 completing -1.0 total). mechanism: harm-reduction-calculus-runs-on-corwick-as-named-person — the writing IS the systematic-override-rationalized threshold crossed."

      - slug: b01c10s04n03
        shape: held
        svo: "the feed-station stone grounds the wrist"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: political_register-prot
              rationale: "the physical act of writing at the feed-station — the stone's surface is the grounding contact that roots the scene's accounting work in a bodily register; no court-tier content enters in this scene; resentment material deferred to c11; register holds at rank 3.5"
          cost_ledger_anchor: null
        notes: "Grounding bone (W4 aliveness): feed-station stone + wrist = physical sensory anchor. Keeps the accounting concrete and embodied. The wrist-on-stone is the body working. Prevents the scene from running as pure interior-accounting abstraction."

      - slug: b01c10s04n04
        shape: held
        svo: "corwick faces the lower-gate"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: moral_legibility_to_self
              rationale: "the observation bone: this is Corwick's body as observed in the feed — the posture Taylor read but did not consent to observe; the first 'did not consent' beat (observation); legibility holds because Taylor is filing the image, not naming the recognition"
          cost_ledger_anchor: null
        notes: "W2 HONOR — 'did not consent' bone 1 of 3: OBSERVATION. Corwick's physical posture as observed-in-the-feed. Grounding bone: concrete body-posture (faces the lower-gate = the report-delivery stance from c09). This is the body-map's origin in Taylor's archive — the first layer of the feed-face."

      - slug: b01c10s04n05
        shape: held
        svo: "corwick squares the errand-corridor"
        substance_delta:
          axis_moves: []
          axes_held:
            - axis: relational_anchor_status
              rationale: "the body-map bone: Corwick's errand-geometry as the accumulated cartography of movement; anchor holds because Wren is not in this accounting; the Corwick-entry does not produce Wren-weight; but the accumulated body-map pattern (without consent) is structurally parallel to the omission-architecture Taylor runs for Wren — the pattern is the same, the absence from the ledger is what differs"
          cost_ledger_anchor: null
        notes: "W2 HONOR — 'did not consent' bone 2 of 3: BODY-MAP. Corwick's errand-corridor as physical movement geometry — the months of pattern-accumulation Taylor held in the internal record. 'squares' per c09 precedent (s02n04 above). This is the body-map layer of the feed-face."

      - slug: b01c10s04n06
        shape: moving
        svo: "taylor-hebert-kl-122ac closes the ledger"
        substance_delta:
          axis_moves:
            - axis: position-prot-rise
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl-d07a
        notes: "Moving bone: ledger close = Taylor's accounting closes on the formalized function; the gain column holds the arrangement-as-confirmed; position-prot-rise +0.5 (second tranche, completing chapter's +1.0 total). event: ledger-entry-closed-on-named-person. mechanism: systematic-override-rationalized-threshold-crossed-accounting-files. The ledger close is structurally distinct from the face-persisting bone that follows."

      - slug: b01c10s04n07
        shape: moving
        svo: "taylor-hebert-kl-122ac presses the feed-station"
        substance_delta:
          axis_moves:
            - axis: social_tether-prot-rise
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: cl03b
        notes: "Moving bone: Taylor's body pressing the feed-station = the tether's structural confirmation at the physical level. The deliveries are now structural to Otto's apparatus — the press is the body enacting load-bearing function. social_tether-prot-rise +0.5 (second tranche, completing chapter's +1.0 total). cl03b future-cost collateral: the trap loading does not appear in Taylor's accounting as the trap it is."

      - slug: b01c10s04n08
        shape: moving
        svo: "corwick squares the feed-record"
        substance_delta:
          axis_moves:
            - axis: moral_legibility_to_self
              direction: up
              magnitude: 1
          axes_held: []
          cost_ledger_anchor: null
          # null anchor — suppressed recognition event per c10 contract
        notes: "W2 HONOR — TERMINAL BONE. 'did not consent' bone 3 of 3: DELIVERY. This is the face as terminal weight — the physical feed-datum persisting in the record after the ledger closes. 'squares the feed-record' = Corwick's body-posture-as-gait-signature persisting in the internal feed-record. The face stays in the feed-record; the ledger does not ask Taylor to stay with it. moral_legibility_to_self +0.5 — suppressed recognition: the gap between 'the ledger is complete' and 'the face does not disappear' is the crack deepening. image: corwicks-face-in-feed-record-after-ledger-close. force: suppressed-recognition-event. The surplus of the record-remaining over the ledger-closing IS the scene's argument. This bone is the chapter's final bone-weight — face last, not closure notation."

    event_map:
      - event: "taylor-opens-ledger-post-detention [event: taylor-opens-ledger-post-detention]"
        bones: [b01c10s04n01]
        omission_rationale: null
      - event: "ledger-as-taylors-accounting-convention [mechanism: ledger-as-taylors-accounting-convention]"
        bones: [b01c10s04n01]
        omission_rationale: null
      - event: "ledger-convention-shapes-the-accounting [force: ledger-convention-shapes-the-accounting]"
        bones: [b01c10s04n01, b01c10s04n02]
        omission_rationale: null
      - event: "corwick-name-enters-ledger-as-closed-entry [event: corwick-name-enters-ledger-as-closed-entry]"
        bones: [b01c10s04n02]
        omission_rationale: null
      - event: "corwick-name-written-as-closed-ledger-entry [image: corwick-name-written-as-closed-ledger-entry]"
        bones: [b01c10s04n02]
        omission_rationale: null
      - event: "harm-reduction-calculus-runs-on-corwick-as-named-person [mechanism: harm-reduction-calculus-runs-on-corwick-as-named-person]"
        bones: [b01c10s04n02, b01c10s04n04, b01c10s04n05, b01c10s04n06]
        omission_rationale: null
      - event: "corwicks-feed-face-present-in-internal-record [image: corwicks-feed-face-present-in-internal-record]"
        bones: [b01c10s04n04, b01c10s04n05, b01c10s04n08]
        omission_rationale: null
      - event: "corwicks-unconsented-instrumentalization-named-in-accounting [force: corwicks-unconsented-instrumentalization-named-in-accounting]"
        bones: [b01c10s04n04, b01c10s04n05, b01c10s04n06]
        omission_rationale: "The three 'did not consent' beats are enacted as three structurally distinct bones: observation (n04 faces-the-lower-gate), body-map (n05 squares-the-errand-corridor), delivery (n08 squares-the-feed-record). 'did not consent' is not stated — it is enacted by the three-layer decomposition of what the body-map accumulated without consent."
      - event: "ledger-entry-closed-on-named-person [event: ledger-entry-closed-on-named-person]"
        bones: [b01c10s04n06]
        omission_rationale: null
      - event: "systematic-override-rationalized-threshold-crossed-accounting-files [mechanism: systematic-override-rationalized-threshold-crossed-accounting-files]"
        bones: [b01c10s04n02, b01c10s04n06]
        omission_rationale: null
      - event: "suppressed-recognition-event [force: suppressed-recognition-event]"
        bones: [b01c10s04n08]
        omission_rationale: null
      - event: "corwicks-face-in-feed-record-after-ledger-close [image: corwicks-face-in-feed-record-after-ledger-close]"
        bones: [b01c10s04n08]
        omission_rationale: null
      - event: "protagonist_force: ledger-accounting discipline — convention; gain and cost real; she closes"
        bones: [b01c10s04n02, b01c10s04n06]
        omission_rationale: null
      - event: "opposing_force: face in feed-record as irresolvable surplus — ledger closes, face does not disappear"
        bones: [b01c10s04n06, b01c10s04n08]
        omission_rationale: "The two-bone split (n06 = ledger closes; n08 = face persists) is the enacted form of the opposing force. The surplus of n08 over n06 is the scene's argument."

---

# ─────────────────────────────────────────────────────────────────────────────
# AGGREGATE VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────

bone_counts:
  s01: 5  # n01-n05
  s02: 7  # n01-n07
  s03: 7  # n01-n07
  s04: 8  # n01-n08
  chapter_total: 27

per_scene_delta_rollup:

  s01:
    target:
      position-prot-rise: "+0.5 (cl-d07a)"
      social_tether-prot-rise: "+0.5 (cl03b)"
    delivered:
      position-prot-rise: "n02 magnitude 1 → +0.5 scene-aggregate (DEC-0002 sub-1.0-target precedent)"
      social_tether-prot-rise: "n04 magnitude 1 → +0.5 scene-aggregate (DEC-0002)"
    delta_variance: 0  # on-target both axes
    held_axes_enacted: [moral_framework (n03), moral_legibility_to_self (n05), relational_anchor_status (implicit n03 grounding), political_register-prot (n02 held via grounding-of-registration-without-color)]

  s02:
    target:
      moral_framework: "-0.5 (cl03a)"
      social_tether-antag: "+0.5 (cl-antag-d10)"
    delivered:
      moral_framework: "n05 magnitude 1 → -0.5 scene-aggregate (DEC-0002)"
      social_tether-antag: "n06 magnitude 1 → +0.5 scene-aggregate (DEC-0002)"
    delta_variance: 0
    held_axes_enacted: [moral_framework opposing-force (n03), moral_legibility_to_self (n04), position-prot-rise (n03), social_tether-prot-rise (n07), relational_anchor_status (n07)]

  s03:
    target:
      position-world: "+1.0 (cl-world-d04)"
      political_register-world: "+1.0 (cl-world-d07)"
      social_tether-antag: "+1.0 (cl-antag-d10)"
    delivered:
      position-world: "n03 magnitude 1 → +1.0 ✓"
      political_register-world: "n05 magnitude 1 → +1.0 ✓"
      social_tether-antag: "n06 magnitude 1 → +1.0 ✓"
    delta_variance: 0  # all three on-target
    held_axes_enacted: [moral_framework (n02), moral_legibility_to_self (n04), relational_anchor_status (n07), social_tether-prot-rise (n01), position-prot-rise (n01)]

  s04:
    target:
      position-prot-rise: "+0.5 (cl-d07a)"
      social_tether-prot-rise: "+0.5 (cl03b)"
      moral_framework: "-0.5 (cl03a)"
      moral_legibility_to_self: "+0.5 (null anchor)"
    delivered:
      position-prot-rise: "n06 magnitude 1 → +0.5 scene-aggregate (DEC-0002)"
      social_tether-prot-rise: "n07 magnitude 1 → +0.5 scene-aggregate (DEC-0002)"
      moral_framework: "n02 magnitude 1 → -0.5 scene-aggregate (DEC-0002)"
      moral_legibility_to_self: "n08 magnitude 1 → +0.5 scene-aggregate (DEC-0002)"
    delta_variance: 0
    held_axes_enacted: [social_tether-antag (n01), position-world (n06 held via ledger-close scope), political_register-world (n03), relational_anchor_status (n05), political_register-prot (n03), social_tether-prot-collapse (n06/n07)]

chapter_delta_aggregate:
  position-prot-rise: "+0.5 (s01) + 0 (s02) + 0 (s03) + +0.5 (s04) = +1.0 ✓ (target +1.0 cl-d07a)"
  social_tether-prot-rise: "+0.5 (s01) + 0 (s02) + 0 (s03) + +0.5 (s04) = +1.0 ✓ (target +1.0 cl03b)"
  moral_framework: "0 (s01) + -0.5 (s02) + 0 (s03) + -0.5 (s04) = -1.0 ✓ (target -1.0 cl03a)"
  social_tether-antag: "0 (s01) + +0.5 (s02) + +1.0 (s03) + 0 (s04) = +1.5 ✓ (target +1.5 cl-antag-d10)"
  position-world: "0 + 0 + +1.0 (s03) + 0 = +1.0 ✓ (target +1.0 cl-world-d04)"
  political_register-world: "0 + 0 + +1.0 (s03) + 0 = +1.0 ✓ (target +1.0 cl-world-d07)"
  moral_legibility_to_self: "0 + 0 + 0 + +0.5 (s04) = +0.5 ✓ (target +0.5 null anchor)"
  # All 7 chapter axes_in_motion on-target

grounding_bone_confirmation:
  s01: "n03 (morning-stone / bay-cold) ✓"
  s02: "n04 (corwick squares stone-post) ✓"
  s03: "n01 (supply cart / lower-gate road) + n07 (bay-cold / lower road) ✓"
  s04: "n03 (feed-station stone / wrist) ✓"

central_event_concreteness_check:
  s01_central_event: "packet-text closes the frame [n02] — concrete prop-object + physical-closure-action ✓"
  s02_central_event: "translation [n05] + routing [n06] — two distinct physical actions ✓"
  s03_central_event: "lower-gate road returns empty [n03] — concrete physical absence ✓ / Gold Cloak pair posts lane-junction [n05] — concrete patrol posture ✓"
  s04_central_event: "writes corwick [n02] — concrete inscription act ✓ / closes ledger [n06] — concrete physical close ✓ / corwick squares feed-record [n08] — concrete feed-datum persisting ✓"

dialogue_anchor_bones: NONE
  # This is a silent chapter per the formalization-is-written-packet / feed-reading / internal-accounting
  # register throughout. No speech bones. Zero dialogue-anchor bones confirmed.

watch_item_resolution:
  W1_s02_surrender:
    honored: true
    mechanism: |
      Substrate-split is a STRUCTURALLY DISTINCT bone (n03: errand-corridor geometry weights
      the internal record) BEFORE the routing bone (n06: routes the record). The months of
      accumulated observation are visible AS bones before delivery: n02 (lower-gate road marks
      the body-map = feed-geography), n03 (internal record as distinct substrate = opposing force
      enacted), n04 (Corwick squares stone-post = specific body-posture from the body-map archive).
      Then n05 (translates = the irreversible act) THEN n06 (routes = the channel entry).
      The surrender is two bones (translate + route), not one clause.
  W2_s04_face_terminal:
    honored: true
    mechanism: |
      Two distinct bones: n06 (closes ledger = ledger-closing) and n08 (corwick squares
      feed-record = record-remaining). The face is the TERMINAL bone. Three 'did not consent'
      beats are 3 structurally distinct bones: n04 (observation / faces-lower-gate), n05
      (body-map / squares-errand-corridor), n08 (delivery / squares-feed-record). Ordering:
      n04 → n05 → n06 (ledger closes) → n07 (presses feed-station) → n08 (face persists).
      Face last. Closure notation (n06) precedes the face (n08), not follows.
  W3_s03_absence_read:
    honored: true
    mechanism: |
      n01 (supply cart marks lower-gate road) + n02 (corwick marks second-circuit return) are
      BEFORE n03 (lower-gate road returns empty). The prior-circuit presence-count is enacted
      as ≥1 bone (n02 names the recurring circuit pattern) before the absence reads as deviation.
  W4_aliveness:
    honored: true
    mechanism: |
      s01: n03 morning-stone/bay-cold (thermal/tactile grounding at the feed-station).
      s02: n04 Corwick-squares-stone-post (specific body-posture from the body-map = feed as
           bodily perception, not data-record abstraction).
      s03: n01 supply-cart/lower-gate-road (physical location baseline) + n07 bay-cold/lower-road
           (environmental sensation during circuit-pass). Feed-reading as bodily circuit-walk.
      s04: n03 feed-station-stone/wrist (the body working at the accounting surface).
      The formalization + detention are CONCRETE and grounded throughout. The detention (s03)
      is a perceptual feed-event (body absent from geometry + patrol-pair posted) NOT a
      data-record transaction.

continuity_fence_check:
  taylor_otto_never_meet: "CLEAR — all contact through Jarvis (n01 s01 = Jarvis delivers; n06 s02 = routes through Jarvis). No bone places Taylor and Otto in the same location."
  khepri_absent: "CLEAR — word does not appear in any bone."
  earth_bet_jargon_banned: "CLEAR — no parahuman/Earth-Bet terminology in any SVO."
  corwick_as_courier: "CLEAR — corwick bare-slug used per c08/c09 precedent (pl-2026-06-01-001); first closed ledger entry with a name enacted at s04n02 (writes corwick)."
