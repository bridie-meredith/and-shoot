# Aggregate State — taylor-westeros-good-intentions

# Rolling forward-feed channel for cross-chapter narrative continuity (schema: schemas/aggregate-state.schema.md).
# Producer: /and-stitch Phase 10 (forward-thread). Consumer: /and-substance chapter b01c09 Phase 0.
# This is version 1 — initial emit, scoped through b01c08.
#
# DERIVATION NOTES (for principal sanity-check):
#   - axis ranks summed from per-chapter substance_delta (chapter-contract axes_in_motion + substance_delta_measured
#     where present: c01 roll-up, c03/c04/c05 measured blocks). Where measured ≠ contract, measured wins.
#   - capability: measured-delta path = 5.5 (start 2 + c01 +1.0 + c04 +2.0 + c08 +0.5). Handoff_out narratives
#     carry rank 5.0 (a stale lineage from before the c04 /and-write Phase 1 redo that raised c04 capability
#     +1.5 → +2.0; the handoff character_state strings were never re-synced past the +0.5 redo delta). Recorded
#     at measured-authoritative 5.5; flagged ESTIMATE-DIVERGENCE so b01c09 Phase 0 can reconcile if needed.
#   - collapse-axes (position-prot-collapse start 7, social_tether-prot-collapse start 8) have NOT begun
#     collapsing — collapse phase opens at d10+. They sit at start_rank; last_movement_at null.
#   - political_register-world has not moved yet (first world political-register tranche anchors at d07/cl-world-d07,
#     not yet reached in c01-c08). Sits at start_rank 5; last_movement_at null.
#
# CAST DE-COLLISION NOTE (not a revision_layer entry): the c08 living Hook-ward feed-body was renamed
#   wenna-cobb → meryn-cobb (DEC-0065) to de-collide with c07's DEAD six-year-old "Wenna Cobb" (the founding
#   entry in Taylor's grave-count, named-in-dialogue dead child). Both recorded in characters[] below.

aggregate_state:
  version: 1
  project: taylor-westeros-good-intentions
  through_book: b01
  through_chapter: b01c08
  last_updated: 2026-06-01T05:00:33Z
  last_updated_by: and-stitch-phase-10

  axis_state:
    - axis: moral_framework
      rank: 0
      start_rank: 2
      delta_since_start: -2
      last_movement_at: b01c06
      last_updated_by: and-stitch-phase-10
      notes: "monotonic collapse; c03 first price-tagged breach (-1.0, cl02) + c06 first named-person delivery (-1.0, cl-d06); rank 0 = prohibition fully a calculable variable; c07/c08 HELD (consolidation + un-logged Oswyn integration, no new breach in Taylor's accounting)"

    - axis: capability
      rank: 5.5
      start_rank: 2
      delta_since_start: 3.5
      last_movement_at: b01c08
      last_updated_by: and-stitch-phase-10
      notes: "ESTIMATE-DIVERGENCE — measured-delta path (c01 +1.0 / c04 +2.0 measured / c08 +0.5) = 5.5; handoff_out narratives carry 5.0 (stale lineage pre-c04 +1.5→+2.0 /and-write redo). Recorded at measured-authoritative 5.5. c08 added Oswyn watcher-network integration (Khepri-echo in method); c02/c03/c05/c06/c07 HELD"

    - axis: position-prot-rise
      rank: 3
      start_rank: 1
      delta_since_start: 2
      last_movement_at: b01c04
      last_updated_by: and-stitch-phase-10
      notes: "rise phase; c03 +1.0 (Otto awareness, cl02) + c04 +1.0 (acceptance confirmed, conduit role). Peaks ~7 at d07; HELD c05-c08"

    - axis: position-prot-collapse
      rank: 7
      start_rank: 7
      delta_since_start: 0
      last_movement_at: null
      last_updated_by: and-stitch-phase-10
      notes: "collapse phase dormant until d10 (non-extractable confirmed); sits at peak-state start_rank 7 through c08; cl07b not yet anchored"

    - axis: relational_anchor_status
      rank: 3
      start_rank: 1
      delta_since_start: 2
      last_movement_at: b01c06
      last_updated_by: and-stitch-phase-10
      notes: "HIGH=WORST; c02 +1.0 (Wren enters coverage map as named function-node, account opens) + c06 +1.0 (first spoken exchange; weight added by Wren's omission from deliverable, cl-d06). c08 HELD (Wren in coverage, no new weight). cl-d06 second tranche +1.0 DEFERRED to c09/c10 (pl-2026-05-30-001)"

    - axis: moral_legibility_to_self
      rank: 5
      start_rank: 4
      delta_since_start: 1
      last_movement_at: b01c06
      last_updated_by: and-stitch-phase-10
      notes: "non-linear; c02 +0.5 (coverage-map recognition arrives + suppressed under harm-reduction) + c06 +0.5 (honest accounting of name-delivery deepens the crack). c07 genuine-engagement-with-Halvard but resolution deferred not advanced; c08 HELD"

    - axis: political_register-prot
      rank: 3
      start_rank: 1
      delta_since_start: 2
      last_movement_at: b01c07
      last_updated_by: and-stitch-phase-10
      notes: "monotonic; c05 +1.5 (first resentment color, cl-d05 first tranche; neutral-instrumentally-observant foreclosed) + c07 +0.5 (Halvard encounter forces articulation of resentment's object). c08 HELD (Aemond feed-ref is logistics, not behavioral; resentment does not advance on logistics noise)"

    - axis: social_tether-prot-rise
      rank: 6
      start_rank: 1
      delta_since_start: 5
      last_movement_at: b01c07
      last_updated_by: and-stitch-phase-10
      notes: "rise phase; c01 +1.0 (Oswyn ward-embedding at rescue) + c03 +1.0 (cl01b court-layer half, Otto awareness via Jarvis) + c04 +2.0 (network-build, cl03b future-cost collateral) + c07 +1.0 (Halvard precinct-node engagement). Peaks ~8 at d07; HELD c05/c06/c08. NOTE: handoff narratives lag (carry rank 3 pre-c04); measured-delta path authoritative at 6"

    - axis: social_tether-prot-collapse
      rank: 8
      start_rank: 8
      delta_since_start: 0
      last_movement_at: null
      last_updated_by: and-stitch-phase-10
      notes: "collapse phase dormant until d10 (non-extractable confirmed); sits at peak-state start_rank 8 through c08; cl07a not yet anchored"

    - axis: social_tether-antag
      rank: 3.5
      start_rank: 1
      delta_since_start: 2.5
      last_movement_at: b01c04
      last_updated_by: and-stitch-phase-10
      notes: "Otto's leverage; c03 +1.5 (offer tendered, leverage embryonic, cl-antag-d03) + c04 +1.0 (acceptance solidifies leverage, cl-antag-d03 third tranche). +1.5 of cl-antag-d03 outstanding for d05-d10; cl-antag-d10 not yet opened. HELD c05-c08"

    - axis: position-world
      rank: 6
      start_rank: 5
      delta_since_start: 1
      last_movement_at: b01c04
      last_updated_by: and-stitch-phase-10
      notes: "Green consolidation; c04 +1.0 (Flea Bottom intelligence layer delivered, cl-world-d04 — first KL street-layer intel). HELD c05-c08; cl07b/cl-world-d07 increments not yet reached"

    - axis: political_register-world
      rank: 5
      start_rank: 5
      delta_since_start: 0
      last_movement_at: null
      last_updated_by: and-stitch-phase-10
      notes: "ESTIMATE — no world political-register tranche has settled through c08; first anchor cl-world-d07 (+2, journey-required cl02) lands at the d07 formalization, not yet reached. Sits at start_rank 5"

  open_hooks:
    - hook_id: hook-0001
      description: "Rushwick courier-attack / enforcement thread: introduced c05 (enforcement-incident; nameless courier held the Rushwick-pass). c08 lands the courier-FACE leg (Oswyn names 'Corwick'); the enforcement PAYOFF leg remains open."
      introduced_at: b01c05
      expected_payoff: c09-c10
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0002
      description: "cf-d10-courier-face: the courier observed in c05 (and held in Taylor's memory c06/c07) gets a name + function this chapter — Oswyn names 'Corwick, runs errands for someone above his station, up the hill twice this month.' The FACE/NAME leg is PAID at c08; the patron-up-the-hill (the someone above his station) is unnamed — open sub-thread feeding d10."
      introduced_at: b01c05
      expected_payoff: c10
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0003
      description: "Wren stitch-maker name-withholding: c06 left the contact-source field blank — Taylor deliberately did NOT name Wren in the deliverable. The second relational-anchor tranche (cl-d06 +1.0) is DEFERRED to c09/c10 (pl-2026-05-30-001). Wren remains in coverage at anchor rank 3, un-priced."
      introduced_at: b01c06
      expected_payoff: c09-c10
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0004
      description: "Oswyn-Mudway at the rendering junction: held hook per cohere report. Oswyn's ward-protection watcher-network now subsumed into Taylor's coverage architecture without his knowledge (the Khepri-echo override); the recognition gap (reader sees it, Taylor does not log it) is left open."
      introduced_at: b01c08
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0005
      description: "Sera coverage-continuance / Sera-protection architecture: the quiet on Sera's question still holds (per c07 prologue). Otto's shielding of Sera's succession exposure (the c03 proposal consideration) remains the live protection Taylor's trades buy; not revisited on-page since c03."
      introduced_at: b01c03
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0006
      description: "Aemond-adjacent pressure: c08 PLANTS the Aemond name (logistics object in the Jarvis handler-rotation; Vhagar's handler rotation referenced) at low intensity — the escalation engine becoming visible at feed edges. Off-stage but logistically present; newly-introduced forward hook this chapter."
      introduced_at: b01c08
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0007
      description: "Halvard counter-argument: c07 first genuine engagement of the principled-slower argument; ends without resolution; Taylor has a counter she believes (the named-death body-count). Halvard does not appear on-page in c08 (held offstage; referenced in prologue as 'the argument the septon left in my hand'). Foreclosure-of-engagement scheduled for d09."
      introduced_at: b01c07
      expected_payoff: c09
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0008
      description: "Black-faction elder list consequences: the four ward-elders named to Otto at c06 — operational follow-through pending; faction-violence sub-pressure flagged to produce on-page consequences. Not revisited c07/c08."
      introduced_at: b01c06
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0009
      description: "cl03b future-cost collateral: the c04 social_tether-prot-rise +2.0 tether gain is logged as downstream -7 risk (the network Taylor builds to survive is the architecture that makes her non-extractable). Trap loading; not yet visible to Taylor; collapse handed to social_tether-prot-collapse at d14."
      introduced_at: b01c04
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

  characters:
    - slug: taylor-hebert-kl-122ac
      introduced_at: b01c01
      last_appearance: b01c08
      reader_legibility: high
      legibility_notes: "POV narrator throughout; full interior access; Worm-Taylor identity + insect-feed mechanism + atonement-frame + the arrangement-with-Otto all reader-legible by c08"
      last_updated_by: and-stitch-phase-10

    - slug: wren-stitch-maker-flea-bottom-ward
      introduced_at: b01c01
      last_appearance: b01c06
      reader_legibility: partial
      legibility_notes: "reader knows occupation (stitch-maker, two lanes over) + Taylor's coverage-map function-node categorization + one spoken exchange (c06) + Taylor's protective omission from the deliverable; NAME deliberately withheld in deliverable. Not on-page in c08"
      last_updated_by: and-stitch-phase-10

    - slug: oswyn-mudway-flea-bottom-elder
      introduced_at: b01c01
      last_appearance: b01c08
      reader_legibility: partial
      legibility_notes: "Hook ward-elder; ran his own informal watcher-network (revealed c08, now subsumed into Taylor's coverage without his knowledge); names Corwick at c08 close. Function + ward-standing legible; interior opaque (non-POV)"
      last_updated_by: and-stitch-phase-10

    - slug: jarvis-coin-kl-courier
      introduced_at: b01c03
      last_appearance: b01c08
      reader_legibility: partial
      legibility_notes: "Otto's courier / the channel up to Otto; reader knows function (carries proposal c03, delivers packets c08) + Earth-Bet-fence-clean voice; standing opaque"
      last_updated_by: and-stitch-phase-10

    - slug: otto-hightower-offstage
      introduced_at: b01c03
      last_appearance: b01c08
      reader_legibility: cipher
      legibility_notes: "cipher-by-design — never on-page; reader knows him only as the patron the arrangement routes to (the proposal-maker, the apparatus). Referenced through Jarvis + the handler-rotation"
      last_updated_by: and-stitch-phase-10

    - slug: septon-halvard-flea-bottom
      introduced_at: b01c04
      last_appearance: b01c07
      reader_legibility: partial
      legibility_notes: "Septon Halvard; minor presence c04, major c07 (the unresolved principled-slower argument — counter-argument genuinely engaged, not won). Voice + theological stance legible after c07. NOT on-page c08 (held offstage; only referenced in prologue)"
      last_updated_by: and-stitch-phase-10

    - slug: corwick
      introduced_at: b01c08
      last_appearance: b01c08
      reader_legibility: partial
      legibility_notes: "the named courier — 'runs errands for someone above his station; up the hill twice this month' (Oswyn-supplied). Reader has name + function + frequency; the patron (someone above his station) is unnamed. Body-map building since c05 (was the nameless courier)"
      last_updated_by: and-stitch-phase-10

    - slug: meryn-cobb
      introduced_at: b01c08
      last_appearance: b01c08
      reader_legibility: cipher
      legibility_notes: "a living Hook-ward feed-body; no lines, no substance — a bare name on the coverage map ('the feed returned Meryn Cobb where the lane-coordinates had been holding her'). Renamed wenna-cobb → meryn-cobb (DEC-0065) to de-collide with c07's dead child Wenna Cobb"
      last_updated_by: and-stitch-phase-10

    - slug: wenna-cobb-dead-child
      introduced_at: b01c07
      last_appearance: b01c07
      reader_legibility: cipher
      legibility_notes: "named-in-dialogue DEAD six-year-old — the founding entry in Taylor's grave-count (the named body that justifies the arrangement, c07 Halvard counter). Not a living cast member; recorded for de-collision traceability against meryn-cobb"
      last_updated_by: and-stitch-phase-10

  world_state:
    - key: calendar
      kind: calendar
      state: "KL 122 AC; the Faith's Crone's stretch; ~third month of the arrangement (two-months-plus functional at c07, same season at c08). Bay-damp cold season — bay-damp settled on the morning stone, not lifting before the first bell. Viserys I on the throne; succession informally contested"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

    - key: the-feed-station
      kind: location
      state: "Taylor's intake point for the Jarvis channel — fixed-point inside the coverage radius; the Hook's enclosed quiet; standard-channel standard-receipt at standard hour. c08: Aemond-name + bread-price report received here"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

    - key: the-chandler-corner
      kind: location
      state: "established as Septon Halvard's recurring fixture corner (c04 + c07; the sept corner / chandler's storehouse, Flea Bottom Hook); appears in c08 as terrain — circuit node, returned by the feed without remark; apprentice posted at the chandler's door"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

    - key: the-hook-ward
      kind: location
      state: "Taylor's home coverage ward (the Hook precinct, Flea Bottom); anchored by Oswyn Mudway's ward network + Septon Halvard's sept. Witch-label formation active since c01. c08: Oswyn's watcher-network subsumed into Taylor's coverage; standard-density circuit, evening + morning passes"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

    - key: the-rushwick
      kind: location
      state: "ward introduced c05; abuts the lower Red Keep servant passages, court-tier-adjacent; a lane-cluster pressed between the hill's stone skirt and the city's upward lean. c08: the lane-junction at the Rushwick margin is Taylor's circuit-start coordinate"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

    - key: oswyn-watcher-network
      kind: condition
      state: "Oswyn Mudway's informal ward-protection network (watchers who notify him of strangers in the Hook) — revealed + mapped by Taylor at c08 and integrated into her surveillance architecture WITHOUT Oswyn's knowledge; coverage-matrix subsumes the watcher-positions. The c08 Khepri-echo override; not logged in Taylor's ledger"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

    - key: coverage-map
      kind: condition
      state: "Taylor's insect-feed surveillance architecture — ~40+ bodies (c02 baseline forty-three), extended across Flea Bottom + Rushwick + Red Keep servant-passage ward by c08; harm-reduction framed; routing calibrated intelligence to Otto via Jarvis since c04"
      last_changed_at: b01c08
      last_updated_by: and-stitch-phase-10

  revision_layer:
    - entry_id: rev-0001
      chapter: b01c08
      hunk_summary: "added calendar anchor to c08 prologue (Crone's stretch / bay-damp / first bell) — c07 season register re-stated for cross-chapter clock continuity"
      class: presentation-reinforcement
      acknowledged: true
      acknowledged_at: 2026-06-01T05:00:33Z
      applied_at: 2026-06-01T05:00:33Z
      applied_by: and-stitch-phase-10
      target_consumer_chapter: b01c09

  conflict_log: []

  books: []
