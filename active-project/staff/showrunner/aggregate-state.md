# Aggregate State — taylor-westeros-good-intentions

# Rolling forward-feed channel for cross-chapter narrative continuity (schema: schemas/aggregate-state.schema.md).
# Producer: /and-stitch Phase 10 (forward-thread). Consumer: /and-substance chapter b01c11 Phase 0.
# Scoped through b01c10. c10 rolled (climax, d10; from chapters[b01c10].substance_delta_measured + handoff_out):
#   position-prot-rise +1.0 (->4), social_tether-prot-rise +1.0 (->7), social_tether-antag +1.5 (->5),
#   position-world +1.0 (->7), political_register-world +1.0 (->6; FIRST movement off start_rank 5),
#   moral_framework -1.0 (->-1; systematic-override entered), moral_legibility_to_self +0.5 (->5.5; suppressed crack).
#   relational_anchor_status + political_register-prot + social_tether-prot-collapse HELD.
# c09 rolled: relational_anchor_status +0.5 (cl-d08 Wren route-indexing) +
#   political_register-prot +0.5 (cl-d05 continuation, lower-gate faction-inference). All other axes HELD.
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
  through_chapter: b01c10
  last_updated: 2026-06-02T00:00:00Z   # c10 climax (d10) threaded: 7 axes moved, 2 hooks paid, 3 hooks opened, hook-0007 window-passed-open; rev-0004 Wren-callback applied
  last_updated_by: and-stitch-phase-10

  axis_state:
    - axis: moral_framework
      rank: -1
      start_rank: 2
      delta_since_start: -3
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "monotonic collapse; c03 first price-tagged breach (-1.0, cl02) + c06 first named-person delivery (-1.0, cl-d06) + c10 -1.0 (cl03a cost side: Corwick body-map delivered and deployed against a named person now detained; systematic-override-rationalized threshold crossed). rank -1 = prohibition fully a calculable variable, override now systematic; c07/c08 HELD (consolidation + un-logged Oswyn integration); c09 HELD"

    - axis: capability
      rank: 5.5
      start_rank: 2
      delta_since_start: 3.5
      last_movement_at: b01c08
      last_updated_by: and-stitch-phase-10
      notes: "ESTIMATE-DIVERGENCE — measured-delta path (c01 +1.0 / c04 +2.0 measured / c08 +0.5) = 5.5; handoff_out narratives carry 5.0 (stale lineage pre-c04 +1.5→+2.0 /and-write redo). Recorded at measured-authoritative 5.5. c08 added Oswyn watcher-network integration (Khepri-echo in method); c02/c03/c05/c06/c07 HELD"

    - axis: position-prot-rise
      rank: 4
      start_rank: 1
      delta_since_start: 3
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "rise phase; c03 +1.0 (Otto awareness, cl02) + c04 +1.0 (acceptance confirmed, conduit role) + c10 +1.0 (cl-d07a: formalization of the arrangement — Otto names the function explicitly; position confirmed at near-peak; informal-deniability foreclosed; 1.0 of 2.0 drawn, 1.0 remains for cl-d07a completion at c14). Peaks ~7 at d07; HELD c05-c09"

    - axis: position-prot-collapse
      rank: 7
      start_rank: 7
      delta_since_start: 0
      last_movement_at: null
      last_updated_by: and-stitch-phase-10
      notes: "collapse phase dormant until d10 (non-extractable confirmed); sits at peak-state start_rank 7 through c08; cl07b not yet anchored"

    - axis: relational_anchor_status
      rank: 3.5
      start_rank: 1
      delta_since_start: 2.5
      last_movement_at: b01c09
      last_updated_by: and-stitch-phase-10
      notes: "HIGH=WORST; c02 +1.0 (Wren enters coverage map as named function-node, account opens) + c06 +1.0 (first spoken exchange; weight added by Wren's omission from deliverable, cl-d06) + c09 +0.5 (cl-d08 first tranche: Wren now a mapped pattern/route in the internal map — 'the map takes Wren's pattern... clean, indexed, kept' — structurally present without ledger entry). c08 HELD. NOTE: cl-d06 second tranche +1.0 still DEFERRED to c10 (pl-2026-05-30-001); the c09 +0.5 is the distinct cl-d08 route-indexing tranche, not the deferred deliverable-omission tranche"

    - axis: moral_legibility_to_self
      rank: 5.5
      start_rank: 4
      delta_since_start: 1.5
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "non-linear; c02 +0.5 (coverage-map recognition arrives + suppressed under harm-reduction) + c06 +0.5 (honest accounting of name-delivery deepens the crack) + c10 +0.5 (detention visible in feed; Taylor runs the accounting and files Corwick as a closed entry — suppressed recognition event, crack deepens but does not open; the lower-gate face persists in the feed-record where the ledger keeps no column). c07 genuine-engagement-with-Halvard but resolution deferred not advanced; c08/c09 HELD"

    - axis: political_register-prot
      rank: 3.5
      start_rank: 1
      delta_since_start: 2.5
      last_movement_at: b01c09
      last_updated_by: and-stitch-phase-10
      notes: "monotonic; c05 +1.5 (first resentment color, cl-d05 first tranche; neutral-instrumentally-observant foreclosed) + c07 +0.5 (Halvard encounter forces articulation of resentment's object) + c09 +0.5 (cl-d05 continuation: resentment-color deepens on a named particular — the lower-gate/Corwick faction-inference, 'a thing already written... a direction I did not infer so much as recognize'). c08 HELD (Aemond feed-ref is logistics, not behavioral)"

    - axis: social_tether-prot-rise
      rank: 7
      start_rank: 1
      delta_since_start: 6
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "rise phase; c01 +1.0 (Oswyn ward-embedding at rescue) + c03 +1.0 (cl01b court-layer half, Otto awareness via Jarvis) + c04 +2.0 (network-build, cl03b future-cost collateral) + c07 +1.0 (Halvard precinct-node engagement) + c10 +1.0 (cl03b: arrangement formalized = tether load-bearing confirmed; tether now structural in Otto's architecture). Peaks ~8 at d07; HELD c05/c06/c08/c09. NOTE: handoff narratives lag (carry rank 3 pre-c04); measured-delta path authoritative at 7"

    - axis: social_tether-prot-collapse
      rank: 8
      start_rank: 8
      delta_since_start: 0
      last_movement_at: null
      last_updated_by: and-stitch-phase-10
      notes: "collapse phase dormant until d10 (non-extractable confirmed); sits at peak-state start_rank 8 through c08; cl07a not yet anchored"

    - axis: social_tether-antag
      rank: 5
      start_rank: 1
      delta_since_start: 4
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "Otto's leverage; c03 +1.5 (offer tendered, leverage embryonic, cl-antag-d03) + c04 +1.0 (acceptance solidifies leverage, cl-antag-d03 third tranche) + c10 +1.5 (cl-antag-d10 opening: non-extractable confirmed in progress; Otto's leverage structural post-formalization). HELD c05-c09. NOTE: cl-antag-d10 not fully drawn (pl-2026-06-02-002 tracks cl04/cl-antag-d10 partial-settle family)"

    - axis: position-world
      rank: 7
      start_rank: 5
      delta_since_start: 2
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "Green consolidation; c04 +1.0 (Flea Bottom intelligence layer delivered, cl-world-d04 — first KL street-layer intel) + c10 +1.0 (cl-world-d04: arrangement formalized = Green succession channel solidifies; position-world gain from the intelligence architecture Taylor accepted; 1.0 of 2.0 remaining, journey-required cl03a). HELD c05-c09"

    - axis: political_register-world
      rank: 6
      start_rank: 5
      delta_since_start: 1
      last_movement_at: b01c10
      last_updated_by: and-stitch-phase-10
      notes: "c10 +1.0 (cl-world-d07 FIRST tranche: Green succession channel solidifies through the formalized arrangement — political_register-world's first movement off start_rank 5). FIRST tranche +1.0 of +2.0; balance +1.0 remains for future allocation (NOT completed — c10 contract auditor fault-003 noted). Held flat c01-c09"

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
      description: "cf-d10-courier-face: the courier observed in c05 gets a name + function at c08 (Oswyn names 'Corwick, runs errands for someone above his station'). c09 ADVANCES (beat 2): Corwick now carries a tracked FACE in the feed (resolved at the Dragonpit-margin lower-gate, evening circuit) plus an inferred Black-faction contact — he faces a second man at the lower gate, the Dragonpit's court-margin / heir's-business side under Rhaenys's Hill (NOT a Green-faction gate). Identity of the second man + the errand remain withheld BY DESIGN. The d10 accounting payoff (the patron-up-the-hill named, the faction-contact errand resolved) is still future — NOT paid."
      introduced_at: b01c05
      expected_payoff: c10
      status: paid
      paid_at: b01c10
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10
      # PAID at c10: Corwick named, body-map surrendered to Otto via Jarvis (s02), detained within two days, written into the ledger as the first closed entry with a name (s04). The d10 accounting payoff delivered.

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
      description: "Halvard counter-argument: c07 first genuine engagement of the principled-slower argument; ends without resolution; Taylor has a counter she believes (the named-death body-count). Halvard does not appear on-page in c08/c09/c10 (held offstage). WINDOW PASSED: expected_payoff c10 reached unpaid — c10 (climax) pays the courier thread but does not return to Halvard, and the c10 contract deliberately holds him offstage (handoff_out: 'counter-argument unresolved; Taylor's engagement becoming thinner'). NOT paid, NOT abandoned: the foreclosure/resolution is axis-movement that belongs to a future scene-chunk, not a draft-layer edit. Routed to parking-lot HARD pl-2026-06-02-stitch-thread-001 targeting /and-substance chapter b01c11 Phase 3 (resolve / foreclose / formally abandon). Window-passed-open per ft-c10-001."
      introduced_at: b01c07
      expected_payoff: c10
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

    - hook_id: hook-0010
      description: "Corwick / lower-gate faction-inference: c09 second circuit returns Corwick at the Dragonpit-margin lower gate (the heir's-business / court-margin side under Rhaenys's Hill — a NOT-Green gate) facing a second man at the wrong hour. Taylor reads the gate's loyalty to a direction (a Black-faction contact) but NOT a name; she prices the posture-class small, closes the observation-entry, and does NOT route it onward — a filed-but-unrouted observation. Quiet open thread: the faction-contact significance is on the page for the reader but withheld from the channel by design; feeds the d10 courier-thread accounting (the errand + the patron-up-the-hill)."
      introduced_at: b01c09
      expected_payoff: c10
      status: paid
      paid_at: b01c10
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10
      # PAID at c10: the c09 filed-but-unrouted lower-gate faction-inference observation is routed to Otto via Jarvis (s02); the d10 accounting runs in s04. Thread foreclosed — courier detained.

    - hook_id: hook-0011
      description: "arrangement-now-formal: c10 s01 — Otto names the arrangement outright as an ongoing function (Taylor = the lower-city intelligence instrument); the informal-deniability Taylor carried through every prior errand is foreclosed ('there was no version of the sentence I could fold back into a question'). The function is now a named standing role, not a contingent exchange. Forward consequence: Taylor can no longer treat the arrangement as deniable/exitable; feeds the non-extractable confirmation (social_tether-prot-collapse opens at d10+)."
      introduced_at: b01c10
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0012
      description: "Dance-pressure pulse 1 / cf-rhaenyra-pressure staging: c10 actively forecloses a Black-faction logistics thread (Corwick detained = the war's logic moved through Taylor's network without her consent or design). Rhaenyra/Dragonstone-adjacent consequences are pending AT A REMOVE — Rhaenyra's agents are not on-page, but the architecture Taylor built has now produced its first Black-faction casualty. The first Dance-pressure pulse; downstream Black-faction counter-response is the open thread."
      introduced_at: b01c10
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

    - hook_id: hook-0013
      description: "Corwick-face-persists-in-feed-record: c10 s04 — after Taylor closes the ledger entry on Corwick, the lower-gate face (gait-signature, set of shoulders) holds in the feed-record 'where the ledger kept no column for it'; her gaze stays on it and does not turn away. The moral-legibility crack made physical: the suppressed recognition that the record keeps what the ledger will not price. Forward thread for moral_legibility_to_self / the d14 full-recognition payoff; the recognition is suppressed not opened (c10 suppressed-recognition fence)."
      introduced_at: b01c10
      expected_payoff: null
      status: open
      paid_at: null
      abandoned_at: null
      abandonment_reason: null
      last_updated_by: and-stitch-phase-10

  characters:
    - slug: taylor-hebert-kl-122ac
      introduced_at: b01c01
      last_appearance: b01c10
      reader_legibility: high
      legibility_notes: "POV narrator throughout; full interior access; Worm-Taylor identity + insect-feed mechanism + atonement-frame + the arrangement-with-Otto all reader-legible. c10: the arrangement she serves is now a NAMED standing function (informal-deniability foreclosed); she surrenders the withheld Corwick body-map, reads his detention in the feed, and files him as the ledger's first named closed entry — the suppressed-recognition crack (moral_legibility 5.5) made physical in her gaze holding the lower-gate face the ledger keeps no column for"
      last_updated_by: and-stitch-phase-10

    - slug: wren-stitch-maker-flea-bottom-ward
      introduced_at: b01c01
      last_appearance: b01c10
      reader_legibility: partial
      legibility_notes: "reader knows occupation (stitch-maker) + Taylor's coverage-map function-node categorization + one spoken exchange (c06) + Taylor's protective omission from the deliverable (NAME deliberately withheld). c09: now the surveillance-pattern SUBJECT — her daily route (door / corner / one-entrance lane) is mapped + indexed in Taylor's internal map; reader-legible via the @0 prologue bridge restatement. c10: PARTIAL appearance only — the rev-0004 prologue callback ('the stitch-maker's days indexed in the record like any other route and kept out of the deliverable') restates her indexed-but-unwritten state at the exact contrast point where Corwick becomes the ledger's first named closed entry; she is the standing counter-example. Still OUTSIDE the formal ledger; relational_anchor_status held at 3.5 (no movement). Not on-page in c07/c08; not in the c10 scene-bodies"
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
      last_appearance: b01c10
      reader_legibility: partial
      legibility_notes: "the named courier — 'runs errands for someone above his station' (Oswyn-supplied, c08). c09: tracked-courier ON-PAGE in the feed at the Dragonpit-margin lower gate (a NOT-Green / heir's-business gate = a Black-faction contact, read as a direction not a name). c10: RESOLVED as a thread — Taylor surrenders the withheld body-map to Otto via Jarvis (s02); the apparatus runs and the corridor returns a body short within two passes (s03: a Gold Cloak / City Watch pair posted at the emptied corridor = detained); Taylor writes him into the ledger as the first named closed entry (s04). Reader now has name + function + frequency + faction-direction + outcome (detained, foreclosed). STILL unnamed: the patron up the line + the specific errand. The lower-gate FACE (gait-signature, set of shoulders) persists in the feed-record after the ledger entry closes — the suppressed-recognition residue. Body-map building since c05 (was the nameless courier)"
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
      state: "KL 122 AC; the Faith's Crone's stretch; ~third month of the arrangement (two-months-plus functional at c07, same season at c08/c09). Bay-damp cold season — bay-cold settled on the morning stone, not lifting before the first bell. c10 prologue CONTINUES the same anchor (Crone's stretch / bay-cold on the morning stone / first bell), holding the c09->c10 clock continuous; c10's central span runs ~two days (formalization morning -> 'two days later' detention -> day's-end accounting). Viserys I on the throne; succession informally contested"
      last_changed_at: b01c10
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
      state: "Taylor's insect-feed surveillance architecture — ~40+ bodies (c02 baseline forty-three), extended across Flea Bottom + Rushwick + Red Keep servant-passage ward by c08; c09 the evening (second) circuit extends coverage to the Dragonpit margin / lower-gate; Wren's daily route indexed as a tracked pattern in the internal map. c10: confirmed OPERATIONALLY LOAD-BEARING for Otto's apparatus — Taylor's delivery of the held Corwick body-map (s02) produces a detention within two circuit-passes (s03), 'the war's logic moved through my own network without my consent or my design.' Harm-reduction framed; routing calibrated intelligence to Otto via Jarvis since c04"
      last_changed_at: b01c10
      last_updated_by: and-stitch-phase-10

    - key: the-dragonpit-margin
      kind: location
      state: "established c09 (reader-established, uncarded per DEC-0063): the outer lanes south of the Hook, toward the hill — Taylor's evening (second) circuit terrain. Hill-lanes lose the day's heat first; warmth of the hook-ward stone gone out of the air. Court-margin terrain abutting Rhaenys's Hill"
      last_changed_at: b01c09
      last_updated_by: and-stitch-phase-10

    - key: the-lower-gate
      kind: location
      state: "established c09 (reader-established, uncarded per DEC-0063): the Dragonpit's court-margin side-gate under Rhaenys's Hill, on the lower-gate road — where bodies on the heir's business pass and not the Queen's; explicitly NOT a Green-faction gate (a faction-loyalty signature Taylor reads off the gate). Site of the c09 Corwick faction-inference encounter. c10: the errand-corridor mouth here returns 'a body short' after the detention (s03) — a Gold Cloak pair posted at rest where Corwick's corridor emptied; the stone-post at the side-exit holds the shape of the emptying"
      last_changed_at: b01c10
      last_updated_by: and-stitch-phase-10

    - key: the-arrangement
      kind: condition
      state: "Taylor's intelligence-for-Sera's-protection exchange with Otto Hightower (via Jarvis). c10 s01: FORMALIZED — Otto names it outright as an ongoing standing function ('the lower city's intelligence delivered up the line'), Sera's protection the stated consideration the function is owed against. The informal-deniability Taylor carried through every prior errand is FORECLOSED ('there was no version of the sentence I could fold back into a question'). No longer a contingent exchange; now a named role. Feeds the non-extractable confirmation (social_tether-prot-collapse opens at d10+)"
      last_changed_at: b01c10
      last_updated_by: and-stitch-phase-10

    - key: green-succession-channel
      kind: condition
      state: "established c10: the Green-faction succession/intelligence channel running through the now-formalized arrangement is OPERATIONAL — the Corwick detention demonstrates the channel converts Taylor's feed-intelligence into apparatus action (position-world 7, political_register-world 6 first-tranche). The institutional mechanism by which Taylor's deliveries consolidate Green control"
      last_changed_at: b01c10
      last_updated_by: and-stitch-phase-10

    - key: black-faction-logistics-thread
      kind: condition
      state: "the Black-faction logistics corridor Corwick served (lower-gate errands facing 'the wrong way for the Queen's business'). c10: ACTIVELY FORECLOSED — Corwick detained two days after Taylor's report; the first Black-faction casualty produced by the architecture Taylor built (the first Dance-pressure pulse). Rhaenyra/Dragonstone-adjacent counter-response pending at a remove (agents not on-page)"
      last_changed_at: b01c10
      last_updated_by: and-stitch-phase-10

    - key: gold-cloaks-city-watch
      kind: condition
      state: "the City Watch — the crown's armed guard in King's Landing. FIRST project-prose appearance c10 s03 (a Gold Cloak pair posted at rest at the emptied errand-corridor = the visible face of the detention apparatus). Glossed in-prose on first use; the register is now resident for downstream chapters (no re-gloss needed)"
      last_changed_at: b01c10
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

    - entry_id: rev-0002
      chapter: b01c09
      hunk_summary: "added calendar/season anchor to c09 prologue (Crone's stretch / bay-damp on the morning stone / cold not lifting before the first bell) — reinforces rev-0001's c08->c09 clock; continues the cross-chapter season-register continuity into c10"
      class: presentation-reinforcement
      acknowledged: true
      acknowledged_at: 2026-06-01T06:30:00Z
      applied_at: 2026-06-01T06:30:00Z
      applied_by: and-stitch-phase-10
      target_consumer_chapter: b01c10

    - entry_id: rev-0003
      chapter: b01c09
      hunk_summary: "depth-pass re-render of c09 (DEC-0068): +4 embodiment/grounding bones (person-on-cold-lane open; cold-stiffened-hand de-fog of the s01 filing thesis; grounded evening watch) + calendar fold into the exposition preamble. Zero substance Δ — axes, hooks, characters, world-state all unchanged from rev-0002 state. Readability improvement only (resolved the Phase-9 AIRLESS; depth_pass_resolved). No new threading needs (PASS-THREAD)."
      class: presentation-reinforcement
      acknowledged: true
      acknowledged_at: 2026-06-01T18:50:00Z
      applied_at: 2026-06-01T18:50:00Z
      applied_by: and-stitch-phase-10
      target_consumer_chapter: b01c10

    - entry_id: rev-0004
      chapter: b01c10
      hunk_summary: "added Wren coverage-callback clause to c10 prologue (ft-c10-002): 'the stitch-maker's days indexed in the record like any other route and kept out of the deliverable' — restates the c09-established Wren-indexed-but-unwritten state at the exact contrast point where Corwick becomes the ledger's first named closed entry. Uses role-noun ('the stitch-maker'), no recognition event, suppressed-register safe. Zero substance Δ — relational_anchor_status held at 3.5; no new event, no axis-movement, no new declared fact (restatement of aggregate characters[wren].legibility_notes)."
      class: presentation-reinforcement
      acknowledged: true
      acknowledged_at: 2026-06-02T00:00:00Z
      applied_at: 2026-06-02T00:00:00Z
      applied_by: and-stitch-phase-10
      target_consumer_chapter: b01c11
      # NOTE: the two SUBSTANTIVE forward-thread findings (ft-c10-001 hook-0007 Halvard counter-argument
      #   payoff; ft-c10-004 hook-0003 Wren cl-d06 +1.0 second tranche) are NOT logged as revision_layer
      #   entries — they require axis-movement the c10 contract holds and the bone-faithfulness fence
      #   forbids at the draft layer. Per schema (substantive surfaces via parking-lot only; do NOT create
      #   acknowledged:false substantive entries that would HARD-abort c11 Phase 0), both route to the
      #   parking lot as forward-hooks for /and-substance chapter b01c11 Phase 3:
      #   pl-2026-06-02-stitch-thread-001 (hook-0007) + pl-2026-06-02-stitch-thread-002 (hook-0003 / cl-d06,
      #   extends pl-2026-05-30-001). The cl-d06 relational_anchor second tranche is tracked there, not here.

  conflict_log: []

  books: []
