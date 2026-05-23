---
audit:
  scope: chapter
  target: b01c01
  gate: write-phase-6-substance-bone-gate
  input: active-project/staff/screen-writer/b01c01-phase1-decomposition.md
  timestamp: 2026-05-23
  run: redo (third fork — /and-write b01c01 redo)
  chapter_class: standard
  bone_gate_exemption: none
  hard_count: 0
  signal_count: 0
  flag_count: 4
  gate_verdict: PASS
  emit_blocked: false

findings:

  # -----------------------------------------------------------------------
  # SCENE S01 — per-bone verdicts (9 bones: n01, n03, n04, n05, n06, n07, n08, n09, n10)
  # n02 deleted Phase 4 (2-of-3 vote); slug preserved in skip.
  # -----------------------------------------------------------------------

  - id: bone-001
    type: pass
    what: b01c01s01n01 — "taylor-hebert-kl-122ac pays the building-keeper" (moving, knowledge +0.03)
    why: SVO IS the anonymous-entry transaction event. Knowledge tick caused by the payment: currency names the place-and-class register; operating rule confirmed viable at street threshold. Bonefide check PASS.
    criteria: ~

  - id: bone-002
    type: pass
    what: b01c01s01n03 — "taylor-hebert-kl-122ac crosses the drain-channel" (moving, knowledge +0.02)
    why: SVO IS the yard-geometry-traversal event. Knowledge tick caused by traversal: drain-channel is the first Flea Bottom surface feature; block layout legible at ground level. Bonefide check PASS.
    criteria: ~

  - id: bone-003
    type: pass
    what: b01c01s01n04 — "coll-net-mender-flea-bottom lifts the eyes" (moving, knowledge +0.04)
    why: SVO IS the surveillance-response event. Knowledge tick caused by Coll's eye-lift: Taylor's appearance in the open yard registered by a block-level witness who does not name what he sees; proximity-as-cover-without-arrangement becomes visible. Bonefide check PASS. Opposing-force bone.
    criteria: ~

  - id: bone-004
    type: pass
    what: b01c01s01n05 — "coll-net-mender-flea-bottom works the net" (held, capability)
    why: >
      Discipline-enactment check PASS. SVO is bare-action with discipline rationale:
      "Coll's feigned-indifference is the opposing-force enacted: surveillance-without-naming;
      his return to work holds the social register at the Flea Bottom courtesy level —
      does not name what he sees in a neighbor's work; needle-criterion signaled by action."
      Rationale names the discipline enacted (feigned-indifference = social-cover-physics hold).
      Held axis (capability) is in parent scene's axes_held[]. HELD-AXIS-UNCONTRACTED: N/A.
      HELD-AXIS-NOT-ENACTED: N/A (rationale is present and names the mechanism).
    criteria: ~

  - id: bone-005
    type: pass
    what: b01c01s01n06 — "taylor-hebert-kl-122ac passes the tallow-stall" (moving, knowledge +0.02)
    why: SVO IS the olfactory-landmark event during the ward circuit. Knowledge tick caused by passage: tallow-stall names the block's sensory landscape; smoke-register of the place enters the ledger. Bonefide check PASS.
    criteria: ~

  - id: bone-006
    type: pass
    what: b01c01s01n07 — "taylor-hebert-kl-122ac circles the block" (moving, knowledge +0.05)
    why: SVO IS the ward-circuit event. Knowledge tick caused by the circuit: ward inventory established (stone, feast-shortage-levy rhythm, who-owes-the-well-step, alley-and-court geometry). Block layout legible at ground level. Bonefide check PASS.
    criteria: ~

  - id: bone-007
    type: pass
    what: b01c01s01n08 — "taylor-hebert-kl-122ac drops the pack" (chatter — axis_moves:[], axes_held:[])
    why: >
      Cost-ledger payment check PASS: cost_ledger_anchor "knowledge-gain-unanchored-baseline" present.
      Entry anchor in memory.md: {book: b01, chapter: b01c01, scene: ~} — chapter-wide scope;
      resolves at-or-under this scene. Entry is bookkeeping-only (no axis tick in either direction;
      chatter establishes conditions for the passive read to land as legible).
      Density-cap check: 1 chatter bone / 9 total bones = 0.11 ≤ cap floor(0.4 × 9) = 3. PASS.
    criteria: ~

  - id: bone-008
    type: pass
    what: b01c01s01n09 — "coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac" (moving, knowledge +0.03)
    why: SVO IS the needle-criterion-exchange event. Knowledge tick caused by Coll's speech: confirmed social physics — proximity-as-cover is available without arrangement; no name given, no claim made. Bonefide check PASS.
    criteria: ~

  - id: bone-009
    type: pass
    what: b01c01s01n10 — "taylor-hebert-kl-122ac holds the feet" (held, capability)
    why: >
      Discipline-enactment check PASS. "holds" is a licensed body-part-stillness verb
      per schemas/bones.schema.md. Rationale names the discipline:
      "stillness-against-pressure — insect-sense runs at the passive threshold;
      capability available and held at rank 3 by discipline enacted; this is the CHOOSING bone —
      Taylor declines to do what Khepri-Taylor would do; the inverted establishing fact
      ('no one here has a power that requires containing') is the context this bone enacts."
      Opposing-force named in rationale: "the capability is awake and the information is available."
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  # -----------------------------------------------------------------------
  # SCENE S01 — per-scene verdicts
  # -----------------------------------------------------------------------

  - id: scene-s01-event-presence
    type: pass
    what: b01c01s01 event-coverage check (9 event_map entries)
    why: >
      event-01 (Taylor arrives / pays copper stars): n01 exists and IS the payment event.
        n02 deleted at Phase 4; event_map still lists n02 as a covering bone — stale reference
        noted below as flag-001; coverage is not absent.
      event-02 (crosses drain-channel): n03 exists and IS the traversal event. PASS.
      event-03 (Coll lifts eyes): n04 exists and IS the surveillance-response event. PASS.
      event-04 (Coll works net): n05 exists and IS the feigned-indifference event. PASS.
      event-05 (ward inventory / tallow-stall): n06 + n07 both exist and together cover the circuit. PASS.
      event-06 (drops the pack): n08 exists and IS the settling event. PASS.
      event-07 (Coll speaks): n09 exists and IS the needle-criterion exchange. PASS.
      event-08 (holds feet): n10 exists and IS the capability-hold event. PASS.
      event-09 (inverted establishing fact): covered by n10 rationale per omission_rationale;
        "the absence is Taylor's interior register of what she observes during the ward-circuit;
        it is the content of the holding, not a separate physical event." Rationale valid. PASS.
      Central event (chunk: "no one here has a power that requires containing"): covered by n10. PASS.
      protagonist_force ("establishing presence without incurring debt, claim, or visibility"):
        carried by n01 (anonymous transaction) + n07 (foot-survey not insect-survey) + n10 (holds capability passive). PASS.
    criteria: ~

  - id: scene-s01-axis-delta
    type: pass
    what: b01c01s01 per-axis Δ: knowledge delivered 0.19 vs target 0.2 (Δ = 0.01)
    why: >
      n01:0.03 + n03:0.02 + n04:0.04 + n06:0.02 + n07:0.05 + n09:0.03 = 0.19.
      Difference from target: 0.01. Within ±1 rank band. PASS.
      No other axes_in_motion for s01; capability is held (zero by definition). N/A.
    criteria: ~

  - id: scene-s01-stakes-axis-dominance
    type: pass
    what: b01c01s01 stakes_axis = capability; resolves to axes_held — dominance check N/A
    why: When stakes_axis is in axes_held[], held axes deliver zero by definition. URI-WRITE-STAKES-AWARE check does not apply. N/A.
    criteria: ~

  - id: scene-s01-underdelivery
    type: pass
    what: b01c01s01 underdelivery check: knowledge 0.19 / target 0.2 = 95% — no axis below 50% threshold
    why: N/A. No underdelivery.
    criteria: ~

  - id: scene-s01-sensory-grounding
    type: pass
    what: b01c01s01 sensory-grounding check (URI-WRITE-SENSORY-GROUNDING)
    why: >
      Grounding bones: n01 (copper-stars / currency-register, place-named),
      n03 (drain-channel / mud surface, Flea Bottom physical feature),
      n06 (tallow-stall / smoke, olfactory anchor),
      n07 (block-circuit / stone geometry, foot-survey).
      Count 4 ≥ required ≥1. PASS.
    criteria: ~

  - id: scene-s01-held-axis-witnessed
    type: pass
    what: b01c01s01 held axes have bone-level enactment: capability
    why: Parent axes_held = [capability]. Bone-level enactment: n05 (Coll-net / feigned-indifference = social-cover-physics hold on capability) + n10 (taylor-feet / stillness-against-pressure = capability hold). 2 bones ≥ required ≥1. PASS.
    criteria: ~

  - id: scene-s01-stakes-axis-in-union
    type: pass
    what: b01c01s01 stakes_axis = capability — resolves to axes_held[capability]. In union.
    why: PASS.
    criteria: ~

  - id: scene-s01-opposing-force
    type: pass
    what: b01c01s01 opposing_force visible
    why: >
      n04 (coll lifts the eyes): surveillance-response = Flea Bottom vouching-physics made
      physically visible; proves a stranger alone reads as wrong without social cover.
      n10 axes_held rationale names: "the capability is awake and the information is available."
      Both bones satisfy the check independently. PASS.
    criteria: ~

  - id: scene-s01-cost-ledger
    type: pass
    what: b01c01s01 cost-ledger entries resolving at-or-under this scene
    why: >
      "knowledge-gain-unanchored-baseline" anchor is {book: b01, chapter: b01c01, scene: ~} —
      chapter-wide, resolves here. n08 carries matching cost_ledger_anchor. PASS.
      No other cost_ledger[] entries have anchor at-or-under b01c01s01.
    criteria: ~

  # -----------------------------------------------------------------------
  # SCENE S02 — per-bone verdicts (10 bones: n01, n03, n04, n05, n06, n07, n08, n09, n10, n11)
  # n02 deleted Phase 4 (3-of-3 vote); slug preserved in skip.
  # -----------------------------------------------------------------------

  - id: bone-010
    type: pass
    what: b01c01s02n01 — "taylor-hebert-kl-122ac threads the needle" (chatter — axis_moves:[], axes_held:[])
    why: >
      Cost-ledger payment check PASS: cost_ledger_anchor "knowledge-gain-unanchored-baseline" present.
      Anchor resolves chapter-wide (at-or-under this scene). Entry is bookkeeping-only.
      Notes: "working-day rhythm opener; the needle is a grounding object — names the physical tool
      of the cover; chatter pays the read that follows."
      Density-cap check deferred to scene-level aggregate. PASS.
    criteria: ~

  - id: bone-011
    type: pass
    what: b01c01s02n03 — "the needle crosses the mesh" (moving, knowledge +0.02)
    why: SVO IS the hands-find-rhythm event. Knowledge tick caused: working rhythm opens the accounting-mind's background process; ward-pattern orientation begins. Bonefide check PASS.
    criteria: ~

  - id: bone-012
    type: pass
    what: b01c01s02n04 — "the insects fill the block" (moving, knowledge +0.05; held, capability)
    why: >
      Moving check PASS: ambient-drift verb "fill" signals passive read. Knowledge tick caused:
      population density across the Hook registered passively; density map enters the ledger.
      Bonefide: passive-fill IS the insect-sense reading event.
      Held check PASS: rationale cites ambient-drift license and names opposing-force explicitly:
      "the read content is available; deployment would require one further act Taylor does not take;
      capability held at the observation-only threshold; this bone is the opposing-force made visible:
      the information is here and the rule is the only thing holding it at 3."
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-013
    type: pass
    what: b01c01s02n05 — "the walls cool" (moving, knowledge +0.04; held, capability)
    why: >
      Moving check PASS: ambient-drift verb "cool." Knowledge tick caused: temperature gradient
      registered passively; occupation pattern read (which walls are peopled, which empty).
      Bonefide: the cooling IS the thermal-read event.
      Held check PASS: "the temperature read is available for routing; the rule holds it at
      observation; opposing-force: the walls' geometry is legible for deployment; Taylor does not deploy."
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-014
    type: pass
    what: b01c01s02n06 — "taylor-hebert-kl-122ac passes the well-step" (moving, knowledge +0.03)
    why: SVO IS the movement-corridor-content event. Knowledge tick caused: well-step is a Flea Bottom social locus; passing it delivers who-owes-it, which route smallfolk use vs. which gaps they leave. Bonefide check PASS.
    criteria: ~

  - id: bone-015
    type: pass
    what: b01c01s02n07 — "taylor-hebert-kl-122ac holds the hands" (held, capability)
    why: >
      Discipline-enactment check PASS. "holds" is a licensed body-part-stillness verb.
      Pass 2 fixer corrected the SVO from unlicensed "holds the needle" (needle is not a body
      part or resisting-pressure object) to licensed "holds the hands" (body-part-stillness).
      Rationale names the discipline: "hands-held-at-work is the physical enactment of the
      prohibition — hands at the needle, read running through the walls, rule holding the gap
      open between available-capability and deployed-capability; the hands carry the cover-work
      and the hold simultaneously."
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-016
    type: pass
    what: b01c01s02n08 — "the boots strike the cobbles" (moving, knowledge +0.02)
    why: SVO IS the auditory-approach-signal event. Knowledge tick caused: footfall on stone establishes the patrol as an incoming physical event; boots-on-cobbles IS the auditory grounding for the watch sequence. Bonefide check PASS.
    criteria: ~

  - id: bone-017
    type: pass
    what: b01c01s02n09 — "the city-watch passes the hook" (moving, knowledge +0.04)
    why: SVO IS the patrol-rotation-confirmation event. Knowledge tick caused: watch spatial position relative to the Hook confirmed; patrol geometry enters the passive ledger. Bonefide check PASS.
    criteria: ~

  - id: bone-018
    type: pass
    what: b01c01s02n10 — "taylor-hebert-kl-122ac holds the eyes" (held, capability)
    why: >
      Discipline-enactment check PASS. "holds" is a licensed body-part-stillness verb.
      Rationale names the discipline and the opposing-force:
      "the watch is near, the insect-sense could route the bodies, the rule holds the hand still;
      eye-direction is the pressure surface — Taylor holds the eyes against the trained pull
      toward completing the route-map; the watch passing is the opposing force, the hold is the response."
      This is the scene's load-bearing discipline beat; watch-pass is the pressure moment.
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-019
    type: pass
    what: b01c01s02n11 — "coll-net-mender-flea-bottom folds the net" (chatter — axis_moves:[], axes_held:[])
    why: >
      Cost-ledger payment check PASS: cost_ledger_anchor "knowledge-gain-unanchored-baseline" present.
      Anchor resolves chapter-wide.
      Phase 1 self-correction note: initial malformed s02n11 (magnitude:0, moving shape) reclassified
      to chatter in the same authoring pass. The canonical chatter form is the operative entry.
      Density-cap check deferred to scene-level aggregate. PASS.
    criteria: ~

  # -----------------------------------------------------------------------
  # SCENE S02 — per-scene verdicts
  # -----------------------------------------------------------------------

  - id: scene-s02-event-presence
    type: pass
    what: b01c01s02 event-coverage check (8 event_map entries)
    why: >
      event-01 (Taylor and Coll work nets): n01 exists and IS the working-day-rhythm event.
        n02 deleted at Phase 4; event_map still lists n02 as a covering bone — stale reference
        noted below as flag-002; coverage not absent (Phase 4 deletion note states "Stitch-carry:
        working-day rhythm cover now carried by s02n01 alone").
      event-02 (Taylor opens background read): n03 exists and IS the needle-crosses-mesh event enabling the read. PASS.
      event-03 (population density): n04 exists and IS the insects-fill-the-block event. PASS.
      event-04 (walls cool / occupation patterns): n05 exists and IS the walls-cool event. PASS.
      event-05 (movement corridors / well-step): n06 exists and IS the well-step-passing event. PASS.
      event-06 (watch-rotation geometry): n08 + n09 both exist; n08 IS the boots-approach event; n09 IS the watch-pass event. PASS.
      event-07 (holds eyes as watch passes): n10 exists and IS the capability-hold-under-watch-pressure event. PASS.
      event-08 (day closes): n11 exists and IS the net-fold / day-close event. PASS.
      Central event (chunk: "needle moves; awareness runs; prohibition holds" — watch-pressure discipline):
        covered by n10. PASS.
      protagonist_force ("reading ward through insect-sense while holding prohibition against deployment"):
        carried by n04 + n05 (passive reads running) + n07 (hands held) + n10 (eyes held). PASS.
    criteria: ~

  - id: scene-s02-axis-delta
    type: pass
    what: b01c01s02 per-axis Δ: knowledge delivered 0.20 vs target 0.2 (exact)
    why: >
      n03:0.02 + n04:0.05 + n05:0.04 + n06:0.03 + n08:0.02 + n09:0.04 = 0.20.
      Exact match. PASS.
    criteria: ~

  - id: scene-s02-stakes-axis-dominance
    type: pass
    what: b01c01s02 stakes_axis = capability; resolves to axes_held — dominance check N/A
    why: Held axes deliver zero by definition. N/A.
    criteria: ~

  - id: scene-s02-underdelivery
    type: pass
    what: b01c01s02 underdelivery check: knowledge 0.20 / target 0.2 = 100% — no axis below 50% threshold
    why: N/A. Exact delivery.
    criteria: ~

  - id: scene-s02-sensory-grounding
    type: pass
    what: b01c01s02 sensory-grounding check (URI-WRITE-SENSORY-GROUNDING)
    why: >
      Grounding bones: n03 (mesh / needle surface), n04 (block / insects in walls — Flea Bottom physical particular),
      n05 (walls cool / stone temperature, occupation-sense), n06 (well-step / place-locus),
      n07 (hands / physical instrument of cover-work), n08 (boots on cobbles / auditory surface).
      Count 6 ≥ required ≥1. PASS.
    criteria: ~

  - id: scene-s02-held-axis-witnessed
    type: pass
    what: b01c01s02 held axes have bone-level enactment: capability
    why: >
      Parent axes_held = [capability]. Bone-level enactment:
      n04 (insects fill / ambient-drift opposing-force),
      n05 (walls cool / ambient-drift opposing-force),
      n07 (holds hands / mid-day discipline),
      n10 (holds eyes / watch-pressure discipline).
      4 bones ≥ required ≥1. PASS.
    criteria: ~

  - id: scene-s02-stakes-axis-in-union
    type: pass
    what: b01c01s02 stakes_axis = capability — resolves to axes_held[capability]. In union.
    why: PASS.
    criteria: ~

  - id: scene-s02-opposing-force
    type: pass
    what: b01c01s02 opposing_force visible
    why: >
      n04 axes_held rationale: "the information is here and the rule is the only thing holding it at 3."
      n09 (city-watch passes): the patrol passing IS the pressure event that makes n10 load-bearing;
      watch presence is the opposing-force enacted as a physical event.
      Two bones satisfy independently. PASS.
    criteria: ~

  - id: scene-s02-cost-ledger
    type: pass
    what: b01c01s02 cost-ledger entries resolving at-or-under this scene
    why: "knowledge-gain-unanchored-baseline" (chapter-wide anchor). n01 + n11 both carry matching cost_ledger_anchor. PASS.
    criteria: ~

  - id: scene-s02-chatter-cap
    type: pass
    what: b01c01s02 chatter density: 2 chatter bones (n01, n11) / 10 total bones = 0.20 ≤ cap floor(0.3 × 10) = 3
    why: 2 ≤ 3. PASS.
    criteria: ~

  # -----------------------------------------------------------------------
  # SCENE S03 — per-bone verdicts (8 bones: n01, n02, n03, n04, n05, n06, n07, n08)
  # n09 deleted Phase 4 (2-of-3 vote); slug preserved in skip.
  # -----------------------------------------------------------------------

  - id: bone-020
    type: pass
    what: b01c01s03n01 — "wren-stitch-maker-flea-bottom-ward enters the alley-mouth" (moving, knowledge +0.02; held, capability)
    why: >
      Moving check PASS: entry IS the face-registration event; knowledge tick caused:
      Wren's face registers in Taylor's field at the alley-mouth; proximity initiates
      face-entry at street-corner granularity. Bonefide.
      Held check PASS: "assessment-pattern initiates on contact; the trained reading fires
      automatically on new-face; rule present but not yet engaged; capability rank unchanged."
      This is the initiation of the automated assessment; rationale names the discipline
      (rule present, initiating but not yet engaged = still-within-normal-passive-threshold).
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-021
    type: pass
    what: b01c01s03n02 — "wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac" (moving, knowledge +0.03)
    why: SVO IS Wren's first-question event. Knowledge tick caused: Wren's question confirms observation-radius (she has been counting Taylor's circuits); distributed social accounting demonstrated, not labelled. Bonefide check PASS.
    criteria: ~

  - id: bone-022
    type: flag
    what: >
      b01c01s03n03 — "taylor-hebert-kl-122ac lifts the eyes" — Phase 1 decomposition file classifies
      this bone as shape: held (axis_moves: [], axes_held: [capability]). Memory.md canonical
      post-Phase-7 record classifies the same bone as moving (knowledge +0.01) with axes_held capability.
    why: >
      Classification divergence between the audited file and the canonical downstream record.
      In the Phase 1 file: n03 is held; s03 aggregate knowledge = 0.09 (within ±1 of target 0.1).
      In memory.md: n03 is moving; s03 aggregate knowledge = 0.10 (exact target match).
      Neither version produces a HARD finding — both are within the ±1 tolerance band.
      But the divergence means the Phase 1 file does not match the stitched-output record,
      which creates a reconciliation risk for any /and-review bones pass that reads Phase 1
      as the source of truth.
      Per-bone held-discipline check on the Phase 1 version (held form) conducted below.
    criteria: ~

  - id: bone-022-held-discipline
    type: pass
    what: b01c01s03n03 held-form discipline-enactment check (Phase 1 file version)
    why: >
      SVO "lifts the eyes" is bare-action. Rationale:
      "the assessment is the opposing-force enacted internally: trained pattern-reading initiates
      on direct orientation — node-id, observation-radius, trust-network map, access-point all
      fire automatically; the rule catches mid-cycle; Taylor holds the eye-lift against the
      trained pull toward completing the assessment; the hold IS the discipline."
      Rationale names the mechanism (hold against trained-pull; assessment running is the proof
      the rule is under load). Opposing-force for this scene named explicitly:
      "Taylor's own trained reading." Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-023
    type: pass
    what: b01c01s03n04 — "taylor-hebert-kl-122ac speaks to wren-stitch-maker-flea-bottom-ward" (moving, knowledge +0.01)
    why: SVO IS the deflection-speech event. Knowledge tick caused: deflection confirms rule functioning at verbal level (no name given, no claim made, no information exchanged). Small magnitude (0.01) is appropriate for a minimum-surface response. Bonefide check PASS.
    criteria: ~

  - id: bone-024
    type: pass
    what: b01c01s03n05 — "wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac" (moving, knowledge +0.03)
    why: SVO IS Wren's second-question event. Knowledge tick caused: Wren names the meat-stall and the flies not being on Taylor; the cost-bearer's seeing is demonstrated (she sees what adults pretend not to see); ward social geometry opens one additional layer. Bonefide check PASS.
    criteria: ~

  - id: bone-025
    type: pass
    what: b01c01s03n06 — "taylor-hebert-kl-122ac holds the eyes" (held, capability)
    why: >
      Discipline-enactment check PASS. "holds" is a licensed body-part-stillness verb.
      Rationale: "load-bearing held bone: the rule catches the assessment before completion;
      Taylor holds gaze-direction fixed against the trained pull toward completing the node-map;
      capability is not deployed; assessment-run is interrupted by the operating rule; Wren is
      not filed as a node."
      Distinct from n03 in structural function: n03 = assessment initiating, n06 = rule catching
      and closing. Both are valid holds at different moments of the same collision.
      Opposing-force named ("the trained pull toward completing the node-map").
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  - id: bone-026
    type: pass
    what: b01c01s03n07 — "wren-stitch-maker-flea-bottom-ward crosses the street" (chatter — axis_moves:[], axes_held:[])
    why: >
      Cost-ledger payment check PASS: cost_ledger_anchor "knowledge-gain-unanchored-baseline" present.
      Anchor resolves chapter-wide. Notes: "Wren's departure is the cost-bearer-placement beat:
      she leaves un-named-as-significant, recurring in ward geometry without being filed; chatter
      pays the chapter's final accounting."
      Density-cap check deferred to scene-level aggregate. PASS.
    criteria: ~

  - id: bone-027
    type: pass
    what: b01c01s03n08 — "taylor-hebert-kl-122ac lifts the needle" (held, capability)
    why: >
      Discipline-enactment check PASS. SVO is bare-action with discipline rationale:
      "closing bone — the return to physical task is the operating rule's verdict on what just
      happened: the assessment is closed, the ledger is not opened, Wren is not filed; brevity
      of return-to-task is the tell (child, present, noted, not filed); the gap between this moment
      and the future ledger-pricing of Wren begins here; the held bone enacts the rule's
      persistence — the needle-lift is not relief, it is the rule continuing to hold."
      Rationale names what the hold enacts (rule's verdict / persistence).
      Held axis (capability) in parent scene's axes_held[]. PASS.
    criteria: ~

  # -----------------------------------------------------------------------
  # SCENE S03 — per-scene verdicts
  # -----------------------------------------------------------------------

  - id: scene-s03-event-presence
    type: pass
    what: b01c01s03 event-coverage check (9 event_map entries, including event-09 with omission_rationale)
    why: >
      event-01 (Wren enters alley-mouth): n01 exists and IS the entry event. PASS.
      event-02 (Wren's first question): n02 exists and IS the first-question event. PASS.
      event-03 (Taylor's trained assessment initiates): n03 exists (Phase 1: held bone). The held
        rationale explicitly names the assessment initiating ("node-id, observation-radius,
        trust-network map, access-point all fire automatically"). The bone IS the assessment-initiation
        event in held form (assessment-running-and-being-caught). PASS.
      event-04 (Taylor speaks deflection): n04 exists and IS the deflection-speech event. PASS.
      event-05 (Wren's second question / meat-stall): n05 exists and IS the second-question event;
        meat-stall named in Wren's speech. PASS.
      event-06 (Taylor holds eyes / rule catches): n06 exists and IS the rule-catch-close event. PASS.
      event-07 (Wren crosses street): n07 exists and IS the departure event. PASS.
      event-08 (Taylor lifts needle): n08 exists and IS the return-to-task event. PASS.
      event-09 (meat-stall as physical locus): omission_rationale present and valid —
        "the meat-stall does not require a separate grounding bone — Wren's speech bone names it,
        and the stall is anchored in the existing draft at L28; a separate bone would add a
        chatter beat with no structural function." Valid. PASS.
      Central event (chunk: "the rule catches it; Taylor declines to file Wren as a node"):
        covered by n06. PASS.
      protagonist_force ("Taylor refusing to complete the instrumental assessment of Wren"):
        carried by n03 (assessment held mid-cycle) + n06 (rule catches and closes). PASS.
      n09 (bridge bone deleted at Phase 4): deletion note states coverage absorbed by n02.
        n02 IS the Wren-approaches-and-speaks event; bridge was redundant. No uncovered event. PASS.
    criteria: ~

  - id: scene-s03-axis-delta
    type: pass
    what: b01c01s03 per-axis Δ (Phase 1 file): knowledge delivered 0.09 vs target 0.1 (Δ = 0.01)
    why: >
      n01:0.02 + n02:0.03 + n04:0.01 + n05:0.03 = 0.09.
      (n03 classified held in Phase 1 file — 0 knowledge contribution from this version.)
      Difference from target: 0.01. Within ±1 rank band. PASS.
      Constrained delta is the load-bearing event per chunk: "minimal gain because Taylor
      deliberately refuses full assessment." The shortfall is structurally motivated and
      within the tolerance band.
    criteria: ~

  - id: scene-s03-stakes-axis-dominance
    type: pass
    what: b01c01s03 stakes_axis = knowledge (axes_in_motion); delivered 0.09 is the sole axis movement in the scene
    why: >
      All s03 bones with axis_moves carry only knowledge moves.
      No non-knowledge axis is in axes_in_motion[].
      knowledge is therefore dominant by construction (only axis present).
      URI-WRITE-STAKES-AWARE: PASS.
    criteria: ~

  - id: scene-s03-underdelivery
    type: pass
    what: b01c01s03 underdelivery check: knowledge 0.09 / target 0.1 = 90% — no axis below 50% threshold
    why: N/A. No underdelivery.
    criteria: ~

  - id: scene-s03-sensory-grounding
    type: pass
    what: b01c01s03 sensory-grounding check (URI-WRITE-SENSORY-GROUNDING)
    why: >
      Grounding bones: n01 (alley-mouth / specific Flea Bottom passage-locus),
      n05 (meat-stall / flies / Flea Bottom sensory particular named by Wren's speech),
      n07 (street-crossing / physical street-space action).
      Count 3 ≥ required ≥1. PASS.
    criteria: ~

  - id: scene-s03-held-axis-witnessed
    type: pass
    what: b01c01s03 held axes have bone-level enactment: capability
    why: >
      Parent axes_held = [capability]. Bone-level enactment:
      n01 (assessment-initiates / rule-present-not-yet-engaged),
      n03 (assessment-runs-caught / rule-catches-mid-cycle),
      n06 (rule-catches-closes / Wren-not-filed),
      n08 (closing-verdict / rule-persists).
      4 bones ≥ required ≥1. PASS.
    criteria: ~

  - id: scene-s03-stakes-axis-in-union
    type: pass
    what: b01c01s03 stakes_axis = knowledge — resolves to axes_in_motion[knowledge]. In union.
    why: PASS.
    criteria: ~

  - id: scene-s03-opposing-force
    type: pass
    what: b01c01s03 opposing_force visible
    why: >
      n03 axes_held rationale: "trained pattern-reading initiates on direct orientation —
      node-id, observation-radius, trust-network map, access-point all fire automatically;
      opposing-force for this scene is Taylor's own trained reading."
      The opposing-force is named explicitly and the bone IS the opposing-force enacted
      (the pull fires automatically; the rule must catch it).
      PASS.
    criteria: ~

  - id: scene-s03-cost-ledger
    type: pass
    what: b01c01s03 cost-ledger entries resolving at-or-under this scene
    why: "knowledge-gain-unanchored-baseline" (chapter-wide anchor). n07 carries matching cost_ledger_anchor. PASS.
    criteria: ~

  - id: scene-s03-chatter-cap
    type: pass
    what: b01c01s03 chatter density: 1 chatter bone (n07) / 8 total bones = 0.125 ≤ cap floor(0.3 × 8) = 2
    why: 1 ≤ 2. PASS.
    criteria: ~

  # -----------------------------------------------------------------------
  # CHAPTER-LEVEL FLAGS (advisory; no gate consequence)
  # -----------------------------------------------------------------------

  - id: flag-001
    type: flag
    what: b01c01s01 event_map entry event-01 lists covering bone b01c01s01n02, which was deleted at Phase 4 trim
    why: >
      The event_map was not updated after n02's deletion. The event ("Taylor arrives and pays copper
      stars") is still covered by n01 alone; coverage is intact. But a future automated event-coverage
      check reading event_map slugs against the live bone set will encounter a missing-slug ghost.
      Phase 4 deletion note in Phase 1 file confirms n01 carries the transaction sufficiently.
      No fixer dispatch required; advisory update of event_map recommended if Phase 1 file is
      revised.
    criteria: ~

  - id: flag-002
    type: flag
    what: b01c01s02 event_map entry event-01 lists covering bone b01c01s02n02, which was deleted at Phase 4 trim
    why: >
      Same class as flag-001. event_map lists n02 as covering event-01 but n02 was deleted.
      Coverage carried by n01 alone per Phase 4 deletion note ("Stitch-carry: working-day rhythm
      cover now carried by s02n01 alone"). Coverage is intact; map reference is stale.
    criteria: ~

  - id: flag-003
    type: flag
    what: b01c01s03n03 bone-shape divergence between Phase 1 file (held, no knowledge tick) and memory.md canonical record (moving, knowledge +0.01, plus axes_held capability)
    why: >
      Phase 1 file and memory.md disagree on whether n03 has a knowledge axis_move (+0.01).
      The s03 aggregate in Phase 1 is 0.09 (held form); in memory.md it is 0.10 (moving form).
      Both are within ±1 of target 0.1. No HARD consequence in either version.
      The divergence indicates Phase 1 file was not updated when the canonical record was written
      (or vice versa). Any /and-review bones pass using Phase 1 as input will compute 0.09
      while memory.md records 0.10.
    criteria: ~

  - id: flag-004
    type: flag
    what: Phase 1 decomposition file (b01c01-phase1-decomposition.md) is stale relative to memory.md canonical post-Phase-7 record; s01 and s02 bone SVOs differ between the two files
    why: >
      memory.md b01c01 s01 bone set begins with n01="enters the corner-room" / n02="pays the
      building-keeper" (with n03+n11 deleted at Phase 4). Phase 1 file has n01="pays the
      building-keeper" (with n02 deleted at Phase 4). The memory.md flat_id assignment at
      lines 710-712 reflects the canonical post-Phase-7 set, which differs from Phase 1 in
      s01 (n01 SVO) and s02 (n01/n02/n03 SVOs).
      memory.md already records substance_bone_gate_verdict: PASS (prior run).
      This redo run re-confirms PASS against the Phase 1 file as instructed. The stale Phase 1
      file poses no gate risk for the current run but should be reconciled with memory.md if
      /and-review bones b01c01 is dispatched against it in a future session.
    criteria: ~

summary:
  gate_verdict: PASS
  hard_count: 0
  signal_count: 0
  flag_count: 4
  emit_blocked: false
  per_scene_event_presence:
    s01: PASS — all 9 events covered; n02 stale map ref flagged (flag-001); no uncovered event
    s02: PASS — all 8 events covered; n02 stale map ref flagged (flag-002); no uncovered event
    s03: PASS — all 9 events covered (event-09 omission_rationale valid); no uncovered event
  per_bone_shape_summary:
    moving: 17 bones — all bonefide; axis ticks caused by SVO
    held: 9 bones — all discipline-enacted; rationales name the mechanism; body-part-stillness license applied where "holds" verb used; all held axes contracted to parent scene
    chatter: 4 bones (s01:n08; s02:n01,n11; s03:n07) — all cost_ledger_anchor present and resolving; chatter caps not exceeded in any scene (s01:1/3, s02:2/3, s03:1/2)
  axis_delta_delivery:
    s01_knowledge: "0.19 / target 0.2 — within ±1 PASS"
    s02_knowledge: "0.20 / target 0.2 — exact PASS"
    s03_knowledge: "0.09 / target 0.1 — within ±1 PASS (Phase 1 held-form for n03; memory.md moving-form yields 0.10 exact)"
  opposing_force_visible: PASS all three scenes
  sensory_grounding: PASS all three scenes (s01:4 bones, s02:6 bones, s03:3 bones)
  held_axis_witnessed: PASS all three scenes (s01:2 bones, s02:4 bones, s03:4 bones)
  stakes_axis_in_union: PASS all three scenes
  cost_ledger_paid: PASS all three scenes (knowledge-gain-unanchored-baseline chapter-wide anchor covers all chatter anchors)
  underdelivery: N/A all three scenes (all axes at ≥90% of target; none below 50% threshold)
