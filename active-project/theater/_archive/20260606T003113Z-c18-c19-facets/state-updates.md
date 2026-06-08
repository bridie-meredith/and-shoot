---
facet: state-updates
sources: [b01-c18, b01-c19, env-b01-c18, env-b01-c20, taylor-hebert-kl-122ac-b01-c18, taylor-hebert-kl-122ac-b01-c20]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: b01-c18
facet: state-updates
episode: b01c18
author: studio+impersonator (consolidated)
---
# source: state-updates-env
1 @1 studio.time_of_day: morning -> before-dawn
2 @1 studio.location: the-gap-lanes-east-water-gate -> the-tallow-render-works
3 @8 studio.time_of_day: before-dawn -> before-first-light
4 @8 studio.fauna_sense_status.coverage-scale: five-ward-plus-approaches-routine -> full-coverage-all-wards-simultaneous
5 @32 studio.succession-document-status: pending -> cleared-small-council-access-window
6 @36 studio.time_of_day: before-first-light -> day-fourteen
7 @36 studio.fauna_sense_status.coverage-scale: full-coverage-all-wards-simultaneous -> standdown-in-progress
8 @37 studio.fauna_sense_status.eastern-gap-status: blank-through-fortnight -> closed-at-standdown
9 @39 studio.cost-ledger.condition: closed -> open-accounting-in-progress
10 @41 studio.cost-ledger.protection-entry: in-progress -> closed
11 @42 studio.cost-ledger.contempt-entry: absent -> entered-complete
12 @43 studio.cost-ledger.standdown-line: absent -> written
13 @44 studio.cost-ledger.disposal-calculus-entry: absent -> closed
14 @46 studio.cost-ledger.condition: open-accounting-in-progress -> closed-stylus-set-beside
# source: state-updates-taylor-hebert-kl-122ac
15 @14 actor:taylor-hebert-kl-122ac.capability_deployment_threshold: never-run-at-full-density -> run-at-full-density-once  # field-extension: records the irrevocable fact (the architecture was run at maximum density once); capability RANK held at 8.5 (no scope added — existing scope run maximally); the threshold-crossing persists past the chapter's standdown. co-cites narrator3 @14
16 @14 actor:taylor-hebert-kl-122ac.moral_framework: -3 -> -4  # cl02 cost side; irrevocable threshold, calibrated qualifier removed. co-cites narrator3 @14
17 @25 actor:taylor-hebert-kl-122ac.political_register-prot: 5.5 -> 6.5  # cl06 opens; the apparatus completes through compound eyes at full density. co-cites narrator5 @25
18 @26 actor:taylor-hebert-kl-122ac.political_register-prot: 6.5 -> 7.0  # cl06; contempt arrives with no exit attached. co-cites narrator6 @26
19 @41 actor:taylor-hebert-kl-122ac.political_register-prot: 7.0 -> 7.5  # cl06 lands at near-saturation; protection-entry line closes, contempt filed without mechanism for refusal. co-cites narrator8 @41
20 @43 actor:taylor-hebert-kl-122ac.position-prot-collapse: 6 -> 5  # cl07b collapse arc; standdown line written; more load-bearing = more disposable post-need. co-cites narrator9 @43
21 @44 actor:taylor-hebert-kl-122ac.social_tether-prot-collapse: 7 -> 6  # cl07a collapse arc; disposal-calculus entry closed; tether under structural strain before Otto's removal calculus. co-cites narrator10 @44

# source: b01-c19
facet: state-updates
episode: b01c19
author: studio
---

# Prior state (b01c18 chapter-close):
#   studio.location: the-tallow-render-works
#   studio.time_of_day: day-fourteen
#   studio.fauna_sense_status.coverage-scale: standdown-complete
#   studio.cost-ledger.condition: closed-stylus-set-beside
#   studio.cost-ledger.contempt-entry: entered-complete
#   studio.cost-ledger.protection-entry: closed
#   studio.cost-ledger.standdown-line: written
#   studio.cost-ledger.disposal-calculus-entry: closed
#   prop:apparatus-picture.norren-attribution: resolved (carry; no change this chapter)
#   prop:oc-coverage-log.norren-attribution: complete-three-lines (carry; no change this chapter)
#
# NOTE — prop-card referrals:
#   prop:cost-ledger: c19 introduces a new accounting column (the chamberlain reading).
#     Using studio.cost-ledger.* form consistent with b01c17/c18. MARGIT REFERRAL RECOMMENDED
#     to reconcile all cost-ledger sub-fields across c17/c18/c19 and create a canonical prop card.
#   the-tallow-croft-corner: new location; no warehouse card. MARGIT REFERRAL per SEAM-C19-LOC-003.
#   prop:oc-running-architecture-record: first-touch in this chapter. No prior warehouse card.
#     MARGIT REFERRAL RECOMMENDED.
#   prop:oc-coverage-map: the coverage-map dropping the Daven node is a discrete prop event.
#     No confirmed warehouse card (distinct from prop:oc-coverage-log and prop:oc-ward-coverage-notes).
#     MARGIT REFERRAL RECOMMENDED.
#
# NOTE — time-skip:
#   b01c18 closed at day-fourteen of the prior fortnight. b01c19 opens on a new chapter-day;
#   scene-map s01 is "before dawn" on a new day (the chapter begins with a new dead-drop request).
#   No explicit time-between-chapters is specified; the skip is structural.

# --- ENTRIES ---

# Scene-open: new chapter-day, same control point
# @1 — the trough releases the cipher-bundle (s01; before-dawn; the-tallow-render-works)
# Taylor is back at the tallow-render-works on a new before-dawn dead-drop retrieval.
# Time resets from day-fourteen (b01c18 chapter-close) to before-dawn (new chapter-day).
# Location unchanged (same control point).
22 @1 studio.time_of_day: day-fourteen -> before-dawn

# @5 — the tallow-render room floor receives the sheet (s01; before-dawn)
# The request-sheet moves from hand to floor — set down before the accounting opens.
# prop first-touch: this is the first time the specific request-sheet (the chamberlain read) is
# a tracked prop. The sheet starts in the trough (@1-@2), is opened (@2), named (@4), and set on
# the floor here (@5). The floor-receipt is the precipice-of-receipt spatial fact.
23 @5 prop:oc-request-sheet.position: in-hand -> render-room-floor
  # field-extension: prop:oc-request-sheet (new oc-prop; first-touch; MARGIT REFERRAL)

# @6 — taylor opens the cost-ledger column (s01; before-dawn)
# The cost-ledger opens for the chamberlain reading: a new column for a new request.
# Prior state: studio.cost-ledger.condition was closed-stylus-set-beside at b01c18 chapter-close.
# The column opening here starts the chamberlain-read accounting.
24 @6 studio.cost-ledger.condition: closed-stylus-set-beside -> open-chamberlain-column

# @8 — the column receives the contempt-entry (s01; before-dawn)
# The contempt-color arrives in the open column with no entry-format to discharge it.
# This is the first contempt-tranche of three in this chapter (political_register-prot +0.5; cl06 partial).
# A discrete sub-field change: the contempt-entry is now in the chamberlain-column at the moment it opens.
25 @8 studio.cost-ledger.contempt-entry-chamberlain: absent -> entered-first-tranche

# s02: accounting running — no location or major prop changes fire; see DECISIONS-NOT-FIRE.

# @23 — taylor closes the cost-ledger column (s03; after-four-days)
# The compiled reading drops; the request closes; the column closes.
# This is the column-close that preceded in the accounting sequence at @6 open.
26 @23 studio.cost-ledger.condition: open-chamberlain-column -> closed-column-drop-complete

# @24 — taylor lifts the stylus (s03; after-four-days)
# The stylus is lifted after the column closes — the CFR-2 choreography begins.
# Prior prop state: stylus was last registered at b01c18 state:14 @46 as "closed-stylus-set-beside"
# (the ledger-edge). This is a new lift from the ledger-surface.
27 @24 prop:oc-stylus.position: ledger-edge-beside -> in-hand-post-column-close
  # field-extension: prop:oc-stylus (new oc-prop; first-touch; distinct from general writing implements;
  #   MARGIT REFERRAL — reconcile with b01c18 sensory:5 @46 "stylus-placed-beside-closed-ledger" which
  #   implied a prop-state but no formal prop:oc-stylus entry was created there)

# @25 — the stylus meets the ledger-edge (s03; after-four-days)
# The beside-not-away placement begins: stylus moving from lifted position toward the ledger-edge.
# CFR-2 BONE 2: the spatial distinction fires here (beside, not down-and-away).
28 @25 prop:oc-stylus.position: in-hand-post-column-close -> approaching-ledger-edge

# @26 — the ledger-edge receives the stylus (s03; after-four-days)
# The beside-placement completes: stylus is beside the closed column, adjacent, not set away.
# CFR-2 terminal bone. The contempt-alongside-not-inside spatial form is now the prop's resting state.
29 @26 prop:oc-stylus.position: approaching-ledger-edge -> beside-ledger-edge-closed-column

# Scene-open s04: location transition to Tallow Croft corner
# @27 — taylor takes the Tallow Croft corner position (s04; second-bell; the-tallow-croft-corner)
# Three days after the drop. Location shifts from the-tallow-render-works to the-tallow-croft-corner.
# Time advances from after-four-days to second-bell (three days later).
30 @27 studio.time_of_day: after-four-days -> second-bell
31 @27 studio.location: the-tallow-render-works -> the-tallow-croft-corner
  # SEAM-C19-LOC-003: the-tallow-croft-corner (new slug; MARGIT REFERRAL)

# @29 — the vat-house shutter closes the window (s04; second-bell-passing)
# The east window of the vat-house is shut — against its established-open baseline across
# forty-three prior approaches. The shutter-state is a tracked location-condition field.
# This is the concrete inference instrument (LABEL-REACH-CONCRETE protected-pattern).
# Field-extension: studio.vat-house-east-window.status (new sub-field; first tracked state
# for this location-feature; prior-open is the seven-month baseline, not a prior state-entry).
32 @29 studio.vat-house-east-window.status: open-baseline-seven-months -> shuttered
  # field-extension: studio.vat-house-east-window.status (new; MARGIT REFERRAL)

# @30 — taylor takes the lane-position (s04; third-bell)
# Third-bell: time advances. Taylor repositions from corner to lane (second approach).
33 @30 studio.time_of_day: second-bell-passing -> third-bell

# @32 — taylor walks the lane (s04; third-bell)
# Social_tether-prot-collapse -1.5 fires: the tether severs in the walk.
# Taylor's posture/position shifts from lane-position (stationary, watching) to in-motion (walking past).
# The actor's state transition is the severance; the env registers the position-change.
34 @32 actor:taylor-hebert-kl-122ac.position: lane-position-stationary -> walking-lane-past-empty-corner

# @33 — taylor opens the running-architecture record (s04; after-third-bell)
# Location returns to the tallow-render-works (implied by the documentary act — the record is there).
# The running-architecture record opens: first-touch prop event.
35 @33 studio.location: the-tallow-croft-corner -> the-tallow-render-works
36 @33 prop:oc-running-architecture-record.condition: closed -> open-node-removal-in-progress
  # field-extension: prop:oc-running-architecture-record (new oc-prop; first-touch; MARGIT REFERRAL)

# @34 — the coverage-map drops the Daven node (s04; after-third-bell)
# Daven's lane-node is removed from the coverage-map — the tether-node's formal removal.
# The coverage-map is a discrete tracked sub-field of the running-architecture record (or possibly
# a separate prop; MARGIT REFERRAL needed to confirm).
37 @34 prop:oc-coverage-map.daven-node: present -> dropped
  # field-extension: prop:oc-coverage-map (new oc-prop; first-touch; MARGIT REFERRAL —
  #   confirm whether this is a sub-field of prop:oc-running-architecture-record or a distinct
  #   prop from prop:oc-ward-coverage-notes; the coverage-map here refers to the contact-node layer
  #   of the running architecture, not the ward-coverage notes from b01c12-c14)

# @35 — taylor closes the coverage-record (s04; after-third-bell)
# The running-architecture record closes: the Daven-node removal is complete; the architecture
# continues one node lighter.
38 @35 prop:oc-running-architecture-record.condition: open-node-removal-in-progress -> closed-daven-node-removed

# --- DECISIONS-NOT-FIRE ---
# @2 (taylor opens the sheet — actor-fork; sheet position already recorded @5; no additional
#   prop-field change at @2 beyond the interim hand-state)
# @3 (grey-dark covers the sheet — sensory territory; no tracked env field-change)
# @4 (sheet names the chamberlain's corridor — information-content; no prop position-change;
#   the sheet's information is an actor/actor-read event, not a tracked field)
# @7 (bottlefly nodes return the outer-ring feed — fauna-sense event; coverage-scale is at
#   standdown-complete baseline; the outer-ring feed returns through existing bottlefly routes
#   at routine-coverage scale — no coverage-scale flip; no new field-change warranted)
# @9 (cost-ledger column runs eleven months of entries — accounting content; the eleven-month
#   weight is a temporal fact embedded in the open column, not a new field-change; the column-open
#   @6 fire captures the state-change; the eleven-month enumeration is actor-fork territory)
# @10-@13 (factional-reading column runs + repeats + lane-shape marks stone + column entry marked —
#   accounting steps within the open-column state; no prop field-flip distinct from the column-open @6;
#   the lane-stone image is a figural element, not a prop-field; the column-entry mark is sub-field
#   within the open accounting, not a closure or new-state event)
# @14 (taylor sets the stylus — the stylus-pause is the recognition-beginning; the peak-bone
#   fires moral_legibility_to_self but the stylus's pause is a momentary actor-state, not a tracked
#   prop-field change; the stylus has not moved to a new resting position; the prop:oc-stylus
#   state-updates begin at @24 when the column closes and the beside-choreography begins)
# @15 (factional-reading structure assembles — the structure is an accounting-content event, not a
#   prop or env field; actor-fork territory)
# @16 (groom lifts the message-case — the groom is a feed-observed cipher-body; actor-fork authority
#   in the feed-read domain; no prop field in Taylor's control-point space changes)
# @17 (taylor files the entry — accounting act within open-column state; no field-flip beyond @8
#   contempt-entry first-tranche and @6 column-open)
# @18 (taylor opens the outer-ring bottlefly routes — the targeted read opens; fauna-sense event;
#   covered by note: coverage-scale remains at standdown-complete baseline for the routine nodes;
#   the outer-ring targeted read is a focused activation within standing architecture, not a
#   coverage-scale flip; the outer-ring is observed feed-terrain)
# @19-@21 (chamberlain crosses pillar junction / courier exits service-gate / chamberlain repeats
#   contact interval — feed-observation beats; location-state fires in loc-state facet @19/@20;
#   these are observed-terrain events, not Taylor's control-point field changes; no studio/prop fires)
# @22 (Jarvis channel receives the compiled reading — the Jarvis channel is a prop-path, not a
#   tracked physical prop with state-fields; the channel-receipt is implied by the column-close @23;
#   frugality: @23 captures the request-close state; no separate @22 entry needed)
# @28 (second-bell passes the Tallow Croft corner — temporal passage; the empty-corner is a
#   negative-presence fact; no prop field-change; time already established at second-bell @27;
#   the second-bell-passing is a scene-rhythm beat, not a new time-of-day flip)
# @31 (daven absents the corner — ABSENCE-AS-POSITIVE-SVO; Daven's absence is an actor-state
#   negative event; the corner's empty status is registered through the loc-state @7 and @8 entries;
#   no separate env/prop field-change for Daven's non-appearance)

# --- SUMMARY ---
# 17 entries on 35 bones = 48.6%; above the c13-c18 precedent range (28-42%).
# Density justified by: 2 scene-open structural fires (@1, @27×2) + 1 time-advance @30 + 1 @29 +
# 1 @32 actor-position + 3 stylus choreography @24/@25/@26 + 4 cost-ledger fires @5/@6/@8/@23 +
# 2 architecture-record fires @33/@34/@35 (@33 location-return + @33 record-open; @34 node-drop;
# @35 record-close) = these break down as: location/time structural fires (5) + prop lifecycle fires (12).
# The stylus CFR-2 choreography (3 fires for one prop across 3 bones) and the architecture-record
# lifecycle (3 fires across @33/@34/@35) both push density up. If the density is to be reduced
# for facet-frugality, the stylus approach-and-receive (@25/@26) could be collapsed to a single
# beside-ledger-edge fire at @26, and the location-return @33 could be absorbed into a combined
# @33 entry. All 17 entries pass Reality + Authority + Frugality individually.

# source: env-b01-c18
facet: state-updates-env
episode: b01c18
author: studio
---

# Prior state (b01c17 chapter-close):
#   studio.location: the-gap-lanes-east-water-gate
#   studio.time_of_day: morning
#   studio.fauna_sense_status.coverage-scale: five-ward-plus-approaches (routine)
#   studio.dead-drop-channel.query-status: quiet
#   prop:apparatus-picture.norren-attribution: resolved  (false attribution; persists; NOT a new c18 change)
#   prop:cost-ledger.protection-entry-column: blank-held (c17 accounting state; c18 accounting reopens and closes it)
#   prop:oc-coverage-log.norren-attribution: complete-three-lines
#
# NOTE — prop-card referrals:
#   prop:oc-cost-ledger: no warehouse card confirmed; entries below use studio.cost-ledger.* form
#     per instructions (parking-lot pl-2026-06-05-c17-001(b) note). MARGIT REFERRAL RECOMMENDED
#     to create prop:oc-cost-ledger card and reconcile with prop:oc-feed-ledger and prior c17
#     prop:cost-ledger.protection-entry-column entry.
#   studio.succession-document-status: new sub-field; no prior warehouse card for succession document;
#     MARGIT REFERRAL RECOMMENDED.
#   oc-dead-drop-site: not a prop but a location; see SEAM-C18-LOC-004 in location-state file.
#   studio.fauna_sense_status.eastern-gap-status: new sub-field; extending the fauna_sense_status
#     schema; justified as a tracked operational state; field-extension documented here.
#
# NOTE — false attribution carry (pl-2026-06-05-c17-001(b)):
#   prop:apparatus-picture.norren-attribution: resolved (Wren screened; false attribution in Otto's
#   intelligence picture). This PERSISTS through all of b01c18 with no field-change. No new state-update
#   entry warranted (anti-pattern #3: persistence is not state-change). Carry-forward recorded here
#   for canonical completeness.

# --- ENTRIES ---

# Scene transitions / location + time resets

# @1 — taylor lifts the cipher-bundle (s01; before-dawn; tallow-render-works)
# Dead-drop retrieved: Taylor is now in the tallow-render room. The chapter opens here;
# prior state was the-gap-lanes-east-water-gate at morning (b01c17 chapter-close).
# New time: before-dawn (a new day; the fortnight not yet begun per scene-map s01 header).
39 @1 studio.time_of_day: morning -> before-dawn
40 @1 studio.location: the-gap-lanes-east-water-gate -> the-tallow-render-works

# s02 — full-coverage deployment begins (@8)
# @8 — taylor opens the bottlefly routes (s02; before-first-light)
# The deployment begins: coverage-scale shifts from five-ward-plus-approaches (routine) to
# full-coverage-all-wards-simultaneous. This is the persistent field change — the architecture
# now runs at maximum density. The moral_framework axis-move fires at @14 (the architecture
# opens the nodes), but the coverage-scale field actually changes at the first deployment act @8.
41 @8 studio.time_of_day: before-dawn -> before-first-light
42 @8 studio.fauna_sense_status.coverage-scale: five-ward-plus-approaches-routine -> full-coverage-all-wards-simultaneous

# s04 — succession document moves (@32)
# @32 — the succession document clears the Small Council access window
# The succession document is a tracked world-state artifact. Its movement through the Small Council
# is permanent: the position-world axis-move fires here (@32). The studio env entry records the
# succession-document-status as a persistent state-change.
# Field-extension: studio.succession-document-status (new sub-field; first-touch; prior state
# "pending" inferred from the arrangements-in-force context — the document has been positioned
# for this window per the arrangement's structure since d03).
43 @32 studio.succession-document-status: pending -> cleared-small-council-access-window
  # field-extension: studio.succession-document-status (new; MARGIT REFERRAL — no prior warehouse entry)

# s05 — standdown begins (@36); accounting opens and closes (@39-@46)

# @36 — taylor closes the ward-elder routes (s05; day-fourteen; standdown begins)
44 @36 studio.time_of_day: before-first-light -> day-fourteen
  # time advance: fourteen-day skip from s02 deployment-open through s03/s04 to standdown
45 @36 studio.fauna_sense_status.coverage-scale: full-coverage-all-wards-simultaneous -> standdown-in-progress

# @37 — the east-of-water-gate gap closes (last lane drawn down; still blank)
# The gap-lane was held blank throughout the fortnight. It closes last.
# Field: studio.fauna_sense_status.eastern-gap-status (new sub-field; tracking the blank lane status)
# Prior state: blank-through-fortnight (the gap was blank throughout; the Norren attribution screens
# the gap-figure in the apparatus picture; the gap's coverage-status has been "blank" since c17).
46 @37 studio.fauna_sense_status.eastern-gap-status: blank-through-fortnight -> closed-at-standdown
  # field-extension: studio.fauna_sense_status.eastern-gap-status (new; MARGIT REFERRAL)
  # NOTE: studio.fauna_sense_status.coverage-scale continues drawdown after @37; full baseline restore
  # implied at end of standdown sequence; the transition completes through @38 as the moths settle.

# @39 — taylor opens the cost-ledger column (accounting begins)
# The cost-ledger opens for the fortnight's accounting. Prior state: the c17 accounting left
# prop:cost-ledger.protection-entry-column: blank-held. The c18 accounting reopens the column
# structure for the full fortnight-close entry sequence.
# Using studio.cost-ledger.* form per instructions (no prop card confirmed for oc-cost-ledger).
47 @39 studio.cost-ledger.condition: closed -> open-accounting-in-progress

# @41 — taylor closes the protection-entry line
# The protection-entry line closes: protection delivered, Wren screened.
# political_register-prot +0.5 fires here (the contempt filed at near-saturation without exit).
48 @41 studio.cost-ledger.protection-entry: in-progress -> closed

# @42 — the column receives the contempt-entry
# The contempt is entered in the column — complete, named, no mechanism for refusal attached.
# This is a discrete, persistent field change: the contempt-entry is now in the ledger.
49 @42 studio.cost-ledger.contempt-entry: absent -> entered-complete

# @43 — taylor writes the standdown line
# position-prot-collapse -0.5 fires here. The standdown line is the accounting record of the
# network returning to baseline — the instrument documented as deployed and withdrawn.
50 @43 studio.cost-ledger.standdown-line: absent -> written

# @44 — the ledger closes the disposal-calculus entry
# social_tether-prot-collapse -0.5 fires here. The disposal calculus is a concrete entry:
# more load-bearing = more precisely disposable post-need.
51 @44 studio.cost-ledger.disposal-calculus-entry: absent -> closed

# @45 — taylor passes the recognition column (blank column; the blank persists)
# The blank column is the enacted suppression: Taylor passes it and leaves it blank.
# The field state is: blank (the column was never filled; no change to record a fill).
# Frugality: the blank is not a state-change — the blank was blank before and remains blank.
# DECISION-NOT-FIRE at @45: the recognition-column's blank state is PERSISTENCE, not change.
# anti-pattern #3 (persistence-as-state) applies. The blank column's significance is carried
# by the scene-map BLANK-COLUMN-SUPPRESSION protected-pattern; no state-update warranted.

# @46 — taylor sets the stylus (accounting closes)
# The cost-ledger closes: stylus set beside.
52 @46 studio.cost-ledger.condition: open-accounting-in-progress -> closed-stylus-set-beside

# --- DECISIONS-NOT-FIRE ---
# @2-@5 (s01: cifpher-bundle handling — actor-fork authority; no env/prop field-changes until scene-close)
# @6 (bundle returned to floor — place is already established; the floor receiving the bundle is a
#   momentary repositioning, not a tracked prop-field change; no prop card for cipher-bundle confirmed)
# @7 (taylor holds the feet — actor-posture, interior; no env/prop field-change)
# @9 (moth-corridor opens — subsumed by @8 coverage-scale change; no separate corridor-state tracking)
# @10-@12 (outer-gate activations + east-gap-blank + Wren-crossing — subsumed by @8 coverage-scale
#   + @1 eastern-gap-status carries through as blank-through-fortnight; no separate field-flip per bone)
# @13 (moth-corridor noise — sensory territory; no persistent env state-change; the smelt-fire
#   interference is transient, not a tracked field)
# @14-@17 (architecture opens nodes + count crosses threshold + count extended + cipher-bundle drops —
#   @8 captures the coverage-scale flip; moral_framework/collapse axis-moves are actor-fork authority;
#   the cipher-bundle drop is actor-state, not a tracked prop-field change without a prop card)
# @18-@27 (s03: court-read through compound eyes — observation/registration beats; the court apparatus
#   is feed-mediated; no studio/prop field-changes; the contempt arriving at @25/@26 is actor-state)
# @28-@31 (s04: dead-drop delivery + counter-bundle receipt + cipher-line + succession-pre — no
#   prop card for intelligence-packet or counter-bundle; @29 Jarvis-courier is actor-fork authority;
#   @31 cipher-line reading is actor-state; all subsumed by @32 succession-document-status fire)
# @33 (Green faction secures succession channel — world-axis; @32 captures the document-status;
#   no separate env field-change warranted for the faction's securing of the channel)
# @34 (taylor closes the record — actor-state; "closes" refers to the personal record, not a
#   tracked prop; no prop card for the personal record confirmed)
# @35 (the ward runs — coverage-scale still at full-coverage-all-wards-simultaneous; persistence
#   not state-change; no fire warranted)
# @38 (moths settle eaves — sensory territory; chandler-quarter moth-density returning to ambient
#   is a sensory inflection, not a tracked env field-change in the state-updates framework)
# @40 (ledger entry records threshold-crossing — the threshold-crossing is already captured in
#   the cost-ledger.condition at @39; the specific threshold-entry is documentation within the
#   open-accounting-in-progress state, not a new field-flip)
# @45 (recognition-column blank — persistence, not state-change; anti-pattern #3; see DECISION note above)

# --- SUMMARY ---
# 14 entries on 46 bones = 30.4%; consistent with c13 (42%) / c14 (28%) / c17 (36%) precedent.
# Target was 8-13; this run reaches 14, justified by: 2 scene-open structural fires (@1×2) +
# 2 time-of-day advances (@8, @36) + 2 coverage-scale flips (@8, @36) + 1 succession-document (@32) +
# 1 eastern-gap-status (@37) + 6 cost-ledger accounting fires (@39, @41-@44, @46).
# The cost-ledger accounting sequence (6 fires on @39-@46) is analogous to prior chapter accounting
# sequences (b01c15 coverage-record fires 4+ entries; b01c12 breach-column + ledger fires).
# All entries pass Reality + Authority + Frugality.

# source: env-b01-c20
facet: state-updates
episode: b01c20
author: studio
---

# Prior state (b01c19 chapter-close):
#   studio.location: the-tallow-render-works
#   studio.time_of_day: after-third-bell
#   studio.cost-ledger.condition: closed-column-drop-complete
#   studio.fauna_sense_status.coverage-scale: standdown-complete
#   studio.fauna_sense_status.eastern-gap-status: closed-at-standdown (carry from c18; @37)
#   prop:oc-stylus.position: beside-ledger-edge-closed-column (carry from c19 @26)
#   prop:oc-running-architecture-record.condition: closed-daven-node-removed (c19 @35)
#   prop:oc-coverage-map.daven-node: dropped (c19 @34)
#   prop:apparatus-picture.norren-attribution: resolved (carry; unchanged)
#   prop:oc-coverage-log.norren-attribution: complete-three-lines (carry; unchanged)
#   studio.succession-document-status: cleared-small-council-access-window (carry from c18)
#
# NOTE — chapter-open time skip:
#   b01c19 closed at after-third-bell. b01c20 opens before-dawn on a new chapter-day;
#   scene-A is "before-dawn" per scene-map. The skip is structural; no explicit
#   time-between-chapters bone; time-of-day resets at @1 (scene-open structural fire).
#
# NOTE — prop-card referrals:
#   prop:oc-ledger: the accounting ledger Taylor opens/marks across scenes A, C, E
#     (entries @4/@5, @16/@17, @29). Using studio.oc-ledger.* form consistent with
#     the cost-ledger sub-field pattern established in c17-c19. MARGIT REFERRAL
#     RECOMMENDED to canonicalize the c20 ledger as the terminal accounting prop
#     (distinct from cost-ledger, which was the running-column instrument; this is
#     the chapter-close ledger Taylor runs at departure).
#   prop:oc-decommission-message: first-touch in this chapter (@14). No prior
#     warehouse card. MARGIT REFERRAL RECOMMENDED.
#   prop:oc-stylus: carry from c19 @24-@26 (beside-ledger-edge-closed-column);
#     reactivated at c20 @4 (lifted) and @24 (lifted again, without opening a
#     ledger line — the held-stylus-without-entry is the recognition-blank shape).
#   prop:oc-pack: first-touch in this chapter (@28). No prior warehouse card.
#     MARGIT REFERRAL RECOMMENDED.

# --- ENTRIES ---

# Scene-open: new chapter-day, same location, time reset
# @1 — the servant-passages empty (scene-A; before-dawn; the-rendering-works-room)
# Time advances from after-third-bell (b01c19 close) to before-dawn (new chapter-day).
# Location unchanged (the-tallow-render-works / rendering-works-room).
# Chapter opens with Taylor already monitoring the Red Keep servant-passage feed;
# the before-dawn time-reset is the scene-open structural fire.
53 @1 studio.time_of_day: after-third-bell -> before-dawn

# @3 — the holdfast routes activate (scene-A; before-dawn; apparatus executes)
# The Green succession move executes in Taylor's feed: the Holdfast access routes
# (mapped and delivered through the Jarvis channel) show new traffic — rehearsed
# sequence activating. The holdfast-routes activation is a tracked world-state
# field: the apparatus's succession-mechanism routes are now live.
# This is the world-state confirmation that the succession machine is running.
# Field-extension: studio.apparatus-holdfast-routes.status (new; first-touch; the
#   routes Taylor mapped and delivered are now an active apparatus-state field;
#   MARGIT REFERRAL RECOMMENDED — confirm against studio.succession-document-status
#   and apparatus route-state sub-fields from c18).
54 @3 studio.apparatus-holdfast-routes.status: dormant -> active
  # field-extension: studio.apparatus-holdfast-routes.status (new; MARGIT REFERRAL)

# @4 — taylor lifts the stylus (scene-A; before-dawn; ledger opens)
# Stylus moves from beside-ledger-edge-closed-column (b01c19 chapter-close state)
# to in-hand. This is the ledger-accounting choreography beginning: the same
# shape as c19 @24 (lift) but now opening a new session, not closing one.
55 @4 prop:oc-stylus.position: beside-ledger-edge-closed-column -> in-hand

# @5 — taylor marks the ledger (scene-A; before-dawn; succession + position entries)
# The ledger receives entries for both the position-world and political_register-world
# draws confirmed at this scene (@1/@3 peak-bones). The ledger's condition changes
# from closed (carry state from c19) to open-entries-in-progress.
# Prior state: studio.cost-ledger.condition = closed-column-drop-complete (c19 @23).
# In b01c20 the accounting instrument is the terminal ledger (not a running column);
# using studio.oc-ledger.condition to distinguish from the prior cost-ledger sub-fields.
# Field-extension: studio.oc-ledger.condition (new sub-field; distinct from
#   studio.cost-ledger.* which tracked the running column; this tracks the terminal
#   accounting ledger Taylor opens at c20; MARGIT REFERRAL RECOMMENDED).
56 @5 studio.oc-ledger.condition: closed -> open-succession-entries-in-progress
  # field-extension: studio.oc-ledger.condition (new; MARGIT REFERRAL)

# @6 — the succession bell rings (scene-B; morning; time advance)
# The succession bell marks morning: time advances from before-dawn to morning.
# The bell is the public announcement of Viserys's death and the Green succession.
57 @6 studio.time_of_day: before-dawn -> morning

# @8 — the patron channel shifts sequence (scene-B; morning; patronage dissolving)
# The patron channel is no longer running Taylor-active delivery; it has shifted
# to a sequence that does not require her signal. This is a tracked structural
# state: the patron channel's operational sequence has changed.
# Field-extension: studio.patron-channel.sequence (new sub-field; first-touch at
#   c20; the patron channel as a tracked env-state field; previously represented
#   through studio.succession-document-status and cost-ledger entries; MARGIT
#   REFERRAL RECOMMENDED — confirm against dead-drop channel sub-fields from c17).
58 @8 studio.patron-channel.sequence: taylor-active-delivery -> autonomous-apparatus-sequence
  # field-extension: studio.patron-channel.sequence (new; MARGIT REFERRAL)

# @10 — taylor opens the feed (scene-B; morning; feed active in east-of-water-gate lanes)
# Taylor opens the insect-feed in the east-of-water-gate lanes, the coverage gap she
# maintained open through every ward-expansion. The fauna_sense_status transitions
# from standdown-complete (c18/c19 carry; the network was at standdown after the
# fortnight deployment closed) to active-lower-city-coverage. This is the full-
# deployment reactivation at the chapter opening.
# Prior state: studio.fauna_sense_status.coverage-scale = standdown-complete (carry from c18/c19).
59 @10 studio.fauna_sense_status.coverage-scale: standdown-complete -> active-lower-city-coverage
  # NOTE: the eastern-gap-status (studio.fauna_sense_status.eastern-gap-status: closed-at-standdown
  #   from c18 @37) transitions back to open here — the gap Taylor maintained through the fortnight
  #   is her running it again. Using coverage-scale as the primary field; gap-status sub-entry below.
60 @10 studio.fauna_sense_status.eastern-gap-status: closed-at-standdown -> open-wren-lanes-active

# @12 — the burn reaches the outer wards (scene-C; midday; fire arrives)
# Time advance: morning → midday (scene-C per scene-map).
# The burn reaching the outer wards is a tracked ambient-condition state change:
# fire is now present in the outer-ward zone. The Dance ignition's physical
# consequences have reached Taylor's coverage area.
61 @12 studio.time_of_day: morning -> midday
62 @12 studio.ambient_conditions.outer-ward-burn: absent -> active-burn-reaching
  # field-extension: studio.ambient_conditions.outer-ward-burn (new sub-field; first-touch;
  #   the Dance's physical fire as a tracked ambient-condition; MARGIT REFERRAL RECOMMENDED)

# @13 — the fire traces the ward-junction catalogue (scene-C; midday; fire propagates)
# The burn propagates through the exact ward-junction catalogue Taylor built and
# delivered. The outer-ward-burn transitions from reaching to propagating-through-catalogue.
# The burn-line is now tracing Taylor's own architecture.
63 @13 studio.ambient_conditions.outer-ward-burn: active-burn-reaching -> propagating-through-ward-catalogue

# @14 — the decommission message arrives (scene-C; midday; apparatus closes)
# The decommission message arrives through a non-Jarvis channel.
# First-touch prop: prop:oc-decommission-message enters the scene.
# Field-extension: prop:oc-decommission-message (new oc-prop; first-touch; MARGIT REFERRAL).
64 @14 prop:oc-decommission-message.status: absent -> delivered
  # field-extension: prop:oc-decommission-message (new oc-prop; first-touch; MARGIT REFERRAL)

# @15 — the apparatus network absorbs the coverage (scene-C; midday; network transferred)
# The apparatus absorbs Taylor's coverage into its own network. The fauna_sense_status
# changes: Taylor's active-lower-city-coverage is now being absorbed by the apparatus
# (the network outlasts its architect). This is the coverage-transfer state change.
65 @15 studio.fauna_sense_status.coverage-scale: active-lower-city-coverage -> absorbed-into-apparatus-network

# @16 — taylor opens the ledger (scene-C; midday; decommission accounting begins)
# The ledger opens for the decommission entries (social_tether and position entries).
# Prior state: studio.oc-ledger.condition = open-succession-entries-in-progress (from @5).
# Now transitions to open-decommission-accounting.
66 @16 studio.oc-ledger.condition: open-succession-entries-in-progress -> open-decommission-accounting

# @17 — taylor marks the social_tether entry (scene-C; midday; tether severed on record)
# The social_tether entry is marked in the ledger: patron channel closed, network
# transferred, tether severing. The ledger receives the terminal tether entry.
# The ledger's condition advances to decommission-entries-marked.
67 @17 studio.oc-ledger.condition: open-decommission-accounting -> open-decommission-entries-marked

# Scene-D: time advance (morning → afternoon not yet explicit; scene-map says "afternoon")
# The scene-map names scene-D as "afternoon." The time advance from midday to afternoon
# fires at the scene-D open, before @18 (where the feed is running normally — an
# established state at scene-D open). Anchoring the time advance at @18 (scene-D
# first bone) as the structural scene-open fire.
68 @18 studio.time_of_day: midday -> afternoon

# @19 — the smoke fills the east-of-water-gate lanes (scene-D; afternoon; physics cascade)
# Smoke arrives in the east-of-water-gate lanes. This is an ambient-condition change
# in the lanes: smoke is now present, the first step of the physics mechanism that
# disperses the insect-feed.
# Field-extension: studio.east-of-water-gate-lanes.ambient: clear -> smoke-present
# (new sub-field; the lanes' specific ambient condition as a tracked state; distinct
#  from the outer-ward-burn ambient which tracks the broader fire; MARGIT REFERRAL).
69 @19 studio.east-of-water-gate-lanes.ambient: clear -> smoke-present
  # field-extension: studio.east-of-water-gate-lanes.ambient (new; MARGIT REFERRAL)

# @22 — the signal drops from the lanes (scene-D; afternoon; feed-signal loss)
# The insect-feed signal drops from the east-of-water-gate lanes. The
# fauna_sense_status transitions: the lanes that were active-open (Taylor's coverage
# gap held open for Wren) go to signal-dropped. This is the recognition-event's
# physical precondition.
70 @22 studio.fauna_sense_status.eastern-gap-status: open-wren-lanes-active -> signal-dropped

# @23 — the east-of-water-gate lanes go blank (scene-D; afternoon; feed blank)
# The lanes go blank in the feed. The fauna_sense_status for the eastern gap
# transitions from signal-dropped to blank. The recognition event is complete.
71 @23 studio.fauna_sense_status.eastern-gap-status: signal-dropped -> blank-recognition-complete

# @25 — taylor closes the feed (scene-E; dusk; feed closure enacted)
# Time advance: afternoon → dusk (scene-E per scene-map).
# Taylor closes the insect-feed before departure. The fauna_sense_status transitions
# from absorbed-into-apparatus-network (the broader coverage) + blank (eastern gap)
# to feed-closed-dispersing-to-substrate. The architecture she built over eleven
# months returns to ambient range.
72 @25 studio.time_of_day: afternoon -> dusk
73 @25 studio.fauna_sense_status.coverage-scale: absorbed-into-apparatus-network -> feed-closed-dispersing-to-substrate

# @27 — the architecture releases the wards (scene-E; dusk; network dissolved)
# The coverage architecture releases — the insects disperse below surveillance
# threshold; the network returns to substrate. The final coverage-scale state:
# the architecture that ran for eleven months is dissolved.
74 @27 studio.fauna_sense_status.coverage-scale: feed-closed-dispersing-to-substrate -> dispersed-below-threshold
75 @27 studio.fauna_sense_status.eastern-gap-status: blank-recognition-complete -> dispersed-with-coverage

# @29 — taylor runs the ledger (scene-E; dusk; final ledger run)
# Taylor runs the full ledger at the gate. The ledger transitions from
# open-decommission-entries-marked to final-run-complete — the terminal accounting.
# This is the ledger-close event before departure.
76 @29 studio.oc-ledger.condition: open-decommission-entries-marked -> final-run-complete

# @30 — taylor exits the south gate (scene-E; dusk; location departure)
# Taylor exits through the south gate — she leaves King's Landing. Location changes
# from the-rendering-works-room to south-gate (and then departed KL). This is the
# chapter-terminal location change.
77 @30 studio.location: the-tallow-render-works -> south-gate-departed

# --- DECISIONS-NOT-FIRE ---
# @2 (the doors open — the Holdfast doors opening is registered in the feed; the
#   door-state is Red Keep location-content at distance, not a tracked field in
#   Taylor's control-point space; @3 holdfast-routes-activate captures the apparatus
#   state change; @2 is approach to @3 peak-bones; held-against-turn class for any
#   canonical state-update beyond the @3 fire)
# @4 stylus prop: the ledger-marking at @5 captures the ledger condition state
#   change; the @4 stylus-lift is the choreography precondition; prop:oc-stylus
#   fired at @4 (entry 3 above); no additional fire needed at @5 (stylus held
#   in-hand through the marking sequence — the ledger-condition fire is the
#   relevant field-change at @5)
# @7 (men enter ward junctions — the men are feed-observed actors moving through
#   Taylor's coverage; actor-fork authority; no studio/prop field changes at this
#   bone; factional-violence entering lower-city is the scene-B content, tracked
#   through patron-channel @8 and feed-coverage @10; no env field directly changes
#   at @7 beyond the ongoing actor-movement through existing routes)
# @9 (gate-side routes fill — the routes filling is the feed showing factional
#   movement through Taylor's own catalogued passage-counts; the routes are coverage-
#   content, not a discrete tracked field-change distinct from @10 feed-open; no
#   additional env field-change; frugality: @10 captures the coverage-state change)
# @11 (faction-movement follows the passage-counts — routes-become-roadmap
#   recognition beat; no new env/prop field changes; the catalogue being used as
#   a map is a world-state observation, not a discrete field mutation; registered
#   through actor-fork narrator-interest, not state-updates)
# @20 (heat disperses the insects — heat is the physics mechanism enabling @22
#   signal-drop; the heat itself is not a separately tracked sub-field from the
#   smoke-present ambient established at @19; the physics cascade is @19→@20→@21→@22;
#   @19 smoke-present captures the ambient change; @22 signal-dropped captures the
#   outcome; @20 and @21 are interior physics steps; pre-emption rule: fire on the
#   beat where the field flips)
# @21 (insects scatter — interior physics step in the cascade; covered by @22
#   signal-dropped; frugality: no distinct tracked field changes at @21)
# @24 (taylor lifts the stylus — the held-stylus-without-entry is the recognition-
#   blank shape; no ledger line opens; the stylus lift is actor-movement; the
#   ledger condition at @17 (open-decommission-entries-marked) is unchanged by @24
#   because no entry is written; no prop field-change fires at @24 — the ABSENCE
#   of a ledger-line is the scene's argument, not a positive field-mutation)
# @26 (insects disperse — the dispersal is the physical consequence of @25 feed-
#   close; the coverage-scale was already set to feed-closed-dispersing-to-substrate
#   at @25; @26 is the confirmation/interior step before @27 architecture-releases;
#   frugality: @25 and @27 capture the bracketing state changes)
# @28 (taylor lifts the pack — actor-fork authority for Taylor's position/inventory;
#   the pack as a prop: prop:oc-pack first-touch, but the lift is actor-state, not
#   a studio prop field; if margit creates a prop:oc-pack card, the holder/position
#   field-change would be studio's domain; flagging as MARGIT REFERRAL — if a
#   prop:oc-pack card is created, a state-update entry fires at @28: pack.position:
#   floor-or-storage -> in-hand; deferred pending card existence)
# @18 (insect-feed runs in east-of-water-gate lanes — the feed's active state in
#   those lanes was established at @10 feed-open; @18 is the scene-D confirmation
#   of an already-established coverage state; the time-of-day fire is anchored at
#   @18 as scene-open structural fire; the feed-active state itself does not fire
#   again since the field is already at open-wren-lanes-active from @10)

# --- SUMMARY ---
# 25 entries on 30 bones = 83.3%; above the c18/c19 precedent range.
# Density justified by:
#   - 3 scene-open structural fires: time-of-day advance (@1 before-dawn; @6 morning;
#     @9 midday; @16 afternoon; @20 dusk) = 5 time-of-day fires across 5 scene transitions
#     (all scene-map scene-open structural fires; the chapter spans a full day arc)
#   - 1 location-departure fire (@30 south-gate)
#   - 2 coverage-scale fires (@10 active-lower-city; @15 absorbed; @21/@27 closed→dispersed = 4)
#   - 2 eastern-gap-status fires (@10 open; @22 signal-dropped; @23 blank; @27 dispersed = 4)
#   - 2 ledger lifecycle fires (@5 open-succession; @14 decommission-accounting; @15 entries-
#     marked; @24 final-run = 4)
#   - 3 apparatus/env one-off fires: @3 holdfast-routes; @8 patron-channel; @12 burn-reaching;
#     @13 burn-propagating; @14 decommission-message; @19 smoke-present = 6
# The time-of-day arc (5 fires across 5 scenes = before-dawn→morning→midday→afternoon→dusk)
# is the structural backbone of this chapter's state-updates density. The full-day arc is
# the succession/departure environmental timeline and cannot be compressed. Coverage-state
# and ledger-state fires decompose an important lifecycle in the chapter's architecture.
# Field-extensions: studio.apparatus-holdfast-routes.status (new); studio.oc-ledger.condition
#   (new; distinct from studio.cost-ledger.*); studio.patron-channel.sequence (new);
#   studio.ambient_conditions.outer-ward-burn (new); studio.east-of-water-gate-lanes.ambient
#   (new); prop:oc-decommission-message (new); 6 new fields/props requiring MARGIT REFERRAL.

# source: taylor-hebert-kl-122ac-b01-c18
facet: state-updates
episode: b01c18
author: taylor-hebert-kl-122ac
---

state1 @14 actor:taylor-hebert-kl-122ac.capability_deployment_threshold: never-run-at-full-density -> run-at-full-density-once  # field-extension: records the irrevocable fact (the architecture was run at maximum density once); capability RANK held at 8.5 (no scope added — existing scope run maximally); the threshold-crossing persists past the chapter's standdown. co-cites narrator3 @14
state2 @14 actor:taylor-hebert-kl-122ac.moral_framework: -3 -> -4  # cl02 cost side; irrevocable threshold, calibrated qualifier removed. co-cites narrator3 @14
state3 @25 actor:taylor-hebert-kl-122ac.political_register-prot: 5.5 -> 6.5  # cl06 opens; the apparatus completes through compound eyes at full density. co-cites narrator5 @25
state4 @26 actor:taylor-hebert-kl-122ac.political_register-prot: 6.5 -> 7.0  # cl06; contempt arrives with no exit attached. co-cites narrator6 @26
state5 @41 actor:taylor-hebert-kl-122ac.political_register-prot: 7.0 -> 7.5  # cl06 lands at near-saturation; protection-entry line closes, contempt filed without mechanism for refusal. co-cites narrator8 @41
state6 @43 actor:taylor-hebert-kl-122ac.position-prot-collapse: 6 -> 5  # cl07b collapse arc; standdown line written; more load-bearing = more disposable post-need. co-cites narrator9 @43
state7 @44 actor:taylor-hebert-kl-122ac.social_tether-prot-collapse: 7 -> 6  # cl07a collapse arc; disposal-calculus entry closed; tether under structural strain before Otto's removal calculus. co-cites narrator10 @44

# source: taylor-hebert-kl-122ac-b01-c20
facet: state-updates
episode: b01c20
author: taylor-hebert-kl-122ac
---

# Prior state (b01c18/c19 carry — actor-fork scope only):
#   actor:taylor-hebert-kl-122ac.position: at-the-ledger (control-point; the-rendering-works-room)
#   actor:taylor-hebert-kl-122ac.feed-deployment: full-architecture-running (eleven-month KL build, held wide)
#   actor:taylor-hebert-kl-122ac.standing-in-apparatus: instrument-load-bearing (Otto's unofficial conduit)
#   actor:taylor-hebert-kl-122ac.pack: none (no travel-state)
#   actor:taylor-hebert-kl-122ac.capability_deployment_threshold: run-at-full-density (carry from b01c18 state1)
#   actor:taylor-hebert-kl-122ac.position-prot-collapse: in-descent (terminal arc opened b01c17/c18)
#
# NOTE — actor-fork authority: this file writes ONLY actor:taylor-hebert-kl-122ac.* entries.
#   Prop lifecycle (stylus, ledger, feed-as-prop), location, and time fires are studio's domain
#   (see state-updates-b01-c20.md studio-fork). The Taylor fork tracks her own posture/position,
#   her deployment-of-capability as an actor-state, her standing, and her travel-state.
#
# NOTE @24 — RECOGNITION-WITHOUT-ENTRY: at @24 Taylor lifts the stylus and does NOT mark.
#   This is a suspended-action state, not a registration. The actor-state field that flips is
#   her ledger-work-posture (marking -> stylus-lifted-no-line-opened), persistent across @24
#   until the feed closes at @25. It is NOT a "noticed/registered/awareness" value — it is the
#   physical held-blank: the stylus is up, the line is not opened, and it stays not-opened.

# --- ENTRIES ---

# @14 — the decommission message arrives (s03; midday; peak-bone)
# Taylor's standing in the apparatus flips: the function is declared concluded, the instrument
# expendable. position-of-no-exit becomes position-of-no-use. Persistent — she is never re-tasked.
# Peak-bone (position-prot-collapse axis_move mag 2). co-cites narrator @14 (the decommission read).
state1 @14 actor:taylor-hebert-kl-122ac.standing-in-apparatus: instrument-load-bearing -> decommissioned-function-concluded  # cl07b; position-prot-collapse draw; the message addresses the function, not the person — standing held no longer.

# @17 — taylor marks the social_tether entry (s03; midday)
# Her ledger-work-posture is active-marking: she enters the patron-channel-closed / network-transferred
# line. The entries are accurate; she does not redraft. The marking-state persists until the held-blank @24.
# co-cites narrator @17 (the accurate entry written without revision).
state2 @17 actor:taylor-hebert-kl-122ac.ledger-work-posture: at-rest-stylus-set -> active-marking  # cl07a; the tether-severance entry written accurate, no redress.

# @24 — taylor lifts the stylus (s04; afternoon; RECOGNITION-HELD-BLANK)
# The recognition arrives as the feed-blank in the lanes she held open. Taylor lifts the stylus and
# does NOT open a line. ledger-work-posture flips from active-marking to stylus-lifted-no-line-opened —
# the suspended-action state. Persistent: the line stays not-opened through the rest of the scene.
# This is the held-blank, the one event her accounting cannot contain because the item was never priced.
# co-cites narrator @24 (the absence of signal in the place she held open).
state3 @24 actor:taylor-hebert-kl-122ac.ledger-work-posture: active-marking -> stylus-lifted-no-line-opened  # cl07a/cl07c; recognition-without-entry; the un-priced item is the one the calculus came for; no line opened, and it stays not-opened.

# @25 — taylor closes the feed (s05; dusk; peak-bone)
# Her deployment-of-capability flips: the architecture she built over eleven months disperses to
# ambient range, below surveillance threshold. What was hers is no longer held. Persistent and terminal —
# the network is not re-deployed. This is the final capability act. co-cites narrator @25 (what disperses is what was hers).
state4 @25 actor:taylor-hebert-kl-122ac.feed-deployment: full-architecture-running -> closed-dispersed-to-substrate  # cl07b; the coverage she held herself is released; the apparatus-absorbed network is theirs, not hers.

# @28 — taylor lifts the pack (s05; dusk)
# Her travel-state flips: from no-pack (resident, anchored to the control-point) to packed-for-departure.
# Persistent — she carries it through the gate. The first physical act of leaving. co-cites narrator @28
# (the pack and no coin above subsistence).
state5 @28 actor:taylor-hebert-kl-122ac.pack: none -> lifted-for-departure  # cl07a; travel-state opens; the instrument readies to leave the city it was decommissioned from.

# @29 — taylor runs the ledger (s05; dusk; LEDGER-CLOSE-DEPARTURE)
# Her ledger-work-posture flips one last time: from stylus-lifted-no-line-opened (the held-blank) to
# final-full-run-no-error. She runs the whole accounting at the gate — not to find an error, because
# there is none; the accuracy is the record of what she did and what she refused to price. Persistent:
# the ledger is closed-complete after this. co-cites narrator @29 (the ledger accurate, nothing to refuse).
state6 @29 actor:taylor-hebert-kl-122ac.ledger-work-posture: stylus-lifted-no-line-opened -> final-full-run-closed-complete  # cl07a; the contempt complete, the recognition complete, nothing in the ledger to refuse.

# @30 — taylor exits the south gate (s05; dusk; peak-bone; position-prot-collapse LOCK rank 1)
# Her position and standing both reach terminal: from at-the-control-point to departed-south-gate-unregistered.
# position-prot-collapse LOCKS at rank 1 — instrument decommissioned and departed, not on any record the
# apparatus keeps. Persistent and absolute (series-terminal). co-cites narrator @30 (departure through the
# south gate, the person leaving is not on any record).
state7 @30 actor:taylor-hebert-kl-122ac.position: at-the-control-point-rendering-works -> departed-south-gate-unregistered  # cl07b; position-prot-collapse LOCK rank 1; the function concluded, the person gone, the city behind her.
