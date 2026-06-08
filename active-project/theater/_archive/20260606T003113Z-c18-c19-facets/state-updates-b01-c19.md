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
1 @1 studio.time_of_day: day-fourteen -> before-dawn

# @5 — the tallow-render room floor receives the sheet (s01; before-dawn)
# The request-sheet moves from hand to floor — set down before the accounting opens.
# prop first-touch: this is the first time the specific request-sheet (the chamberlain read) is
# a tracked prop. The sheet starts in the trough (@1-@2), is opened (@2), named (@4), and set on
# the floor here (@5). The floor-receipt is the precipice-of-receipt spatial fact.
2 @5 prop:oc-request-sheet.position: in-hand -> render-room-floor
  # field-extension: prop:oc-request-sheet (new oc-prop; first-touch; MARGIT REFERRAL)

# @6 — taylor opens the cost-ledger column (s01; before-dawn)
# The cost-ledger opens for the chamberlain reading: a new column for a new request.
# Prior state: studio.cost-ledger.condition was closed-stylus-set-beside at b01c18 chapter-close.
# The column opening here starts the chamberlain-read accounting.
3 @6 studio.cost-ledger.condition: closed-stylus-set-beside -> open-chamberlain-column

# @8 — the column receives the contempt-entry (s01; before-dawn)
# The contempt-color arrives in the open column with no entry-format to discharge it.
# This is the first contempt-tranche of three in this chapter (political_register-prot +0.5; cl06 partial).
# A discrete sub-field change: the contempt-entry is now in the chamberlain-column at the moment it opens.
4 @8 studio.cost-ledger.contempt-entry-chamberlain: absent -> entered-first-tranche

# s02: accounting running — no location or major prop changes fire; see DECISIONS-NOT-FIRE.

# @23 — taylor closes the cost-ledger column (s03; after-four-days)
# The compiled reading drops; the request closes; the column closes.
# This is the column-close that preceded in the accounting sequence at @6 open.
5 @23 studio.cost-ledger.condition: open-chamberlain-column -> closed-column-drop-complete

# @24 — taylor lifts the stylus (s03; after-four-days)
# The stylus is lifted after the column closes — the CFR-2 choreography begins.
# Prior prop state: stylus was last registered at b01c18 state:14 @46 as "closed-stylus-set-beside"
# (the ledger-edge). This is a new lift from the ledger-surface.
6 @24 prop:oc-stylus.position: ledger-edge-beside -> in-hand-post-column-close
  # field-extension: prop:oc-stylus (new oc-prop; first-touch; distinct from general writing implements;
  #   MARGIT REFERRAL — reconcile with b01c18 sensory:5 @46 "stylus-placed-beside-closed-ledger" which
  #   implied a prop-state but no formal prop:oc-stylus entry was created there)

# @25 — the stylus meets the ledger-edge (s03; after-four-days)
# The beside-not-away placement begins: stylus moving from lifted position toward the ledger-edge.
# CFR-2 BONE 2: the spatial distinction fires here (beside, not down-and-away).
7 @25 prop:oc-stylus.position: in-hand-post-column-close -> approaching-ledger-edge

# @26 — the ledger-edge receives the stylus (s03; after-four-days)
# The beside-placement completes: stylus is beside the closed column, adjacent, not set away.
# CFR-2 terminal bone. The contempt-alongside-not-inside spatial form is now the prop's resting state.
8 @26 prop:oc-stylus.position: approaching-ledger-edge -> beside-ledger-edge-closed-column

# Scene-open s04: location transition to Tallow Croft corner
# @27 — taylor takes the Tallow Croft corner position (s04; second-bell; the-tallow-croft-corner)
# Three days after the drop. Location shifts from the-tallow-render-works to the-tallow-croft-corner.
# Time advances from after-four-days to second-bell (three days later).
9 @27 studio.time_of_day: after-four-days -> second-bell
10 @27 studio.location: the-tallow-render-works -> the-tallow-croft-corner
  # SEAM-C19-LOC-003: the-tallow-croft-corner (new slug; MARGIT REFERRAL)

# @29 — the vat-house shutter closes the window (s04; second-bell-passing)
# The east window of the vat-house is shut — against its established-open baseline across
# forty-three prior approaches. The shutter-state is a tracked location-condition field.
# This is the concrete inference instrument (LABEL-REACH-CONCRETE protected-pattern).
# Field-extension: studio.vat-house-east-window.status (new sub-field; first tracked state
# for this location-feature; prior-open is the seven-month baseline, not a prior state-entry).
11 @29 studio.vat-house-east-window.status: open-baseline-seven-months -> shuttered
  # field-extension: studio.vat-house-east-window.status (new; MARGIT REFERRAL)

# @30 — taylor takes the lane-position (s04; third-bell)
# Third-bell: time advances. Taylor repositions from corner to lane (second approach).
12 @30 studio.time_of_day: second-bell-passing -> third-bell

# @32 — taylor walks the lane (s04; third-bell)
# Social_tether-prot-collapse -1.5 fires: the tether severs in the walk.
# Taylor's posture/position shifts from lane-position (stationary, watching) to in-motion (walking past).
# The actor's state transition is the severance; the env registers the position-change.
13 @32 actor:taylor-hebert-kl-122ac.position: lane-position-stationary -> walking-lane-past-empty-corner

# @33 — taylor opens the running-architecture record (s04; after-third-bell)
# Location returns to the tallow-render-works (implied by the documentary act — the record is there).
# The running-architecture record opens: first-touch prop event.
14 @33 studio.location: the-tallow-croft-corner -> the-tallow-render-works
15 @33 prop:oc-running-architecture-record.condition: closed -> open-node-removal-in-progress
  # field-extension: prop:oc-running-architecture-record (new oc-prop; first-touch; MARGIT REFERRAL)

# @34 — the coverage-map drops the Daven node (s04; after-third-bell)
# Daven's lane-node is removed from the coverage-map — the tether-node's formal removal.
# The coverage-map is a discrete tracked sub-field of the running-architecture record (or possibly
# a separate prop; MARGIT REFERRAL needed to confirm).
16 @34 prop:oc-coverage-map.daven-node: present -> dropped
  # field-extension: prop:oc-coverage-map (new oc-prop; first-touch; MARGIT REFERRAL —
  #   confirm whether this is a sub-field of prop:oc-running-architecture-record or a distinct
  #   prop from prop:oc-ward-coverage-notes; the coverage-map here refers to the contact-node layer
  #   of the running architecture, not the ward-coverage notes from b01c12-c14)

# @35 — taylor closes the coverage-record (s04; after-third-bell)
# The running-architecture record closes: the Daven-node removal is complete; the architecture
# continues one node lighter.
17 @35 prop:oc-running-architecture-record.condition: open-node-removal-in-progress -> closed-daven-node-removed

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
