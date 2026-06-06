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
1 @1 studio.time_of_day: morning -> before-dawn
2 @1 studio.location: the-gap-lanes-east-water-gate -> the-tallow-render-works

# s02 — full-coverage deployment begins (@8)
# @8 — taylor opens the bottlefly routes (s02; before-first-light)
# The deployment begins: coverage-scale shifts from five-ward-plus-approaches (routine) to
# full-coverage-all-wards-simultaneous. This is the persistent field change — the architecture
# now runs at maximum density. The moral_framework axis-move fires at @14 (the architecture
# opens the nodes), but the coverage-scale field actually changes at the first deployment act @8.
3 @8 studio.time_of_day: before-dawn -> before-first-light
4 @8 studio.fauna_sense_status.coverage-scale: five-ward-plus-approaches-routine -> full-coverage-all-wards-simultaneous

# s04 — succession document moves (@32)
# @32 — the succession document clears the Small Council access window
# The succession document is a tracked world-state artifact. Its movement through the Small Council
# is permanent: the position-world axis-move fires here (@32). The studio env entry records the
# succession-document-status as a persistent state-change.
# Field-extension: studio.succession-document-status (new sub-field; first-touch; prior state
# "pending" inferred from the arrangements-in-force context — the document has been positioned
# for this window per the arrangement's structure since d03).
5 @32 studio.succession-document-status: pending -> cleared-small-council-access-window
  # field-extension: studio.succession-document-status (new; MARGIT REFERRAL — no prior warehouse entry)

# s05 — standdown begins (@36); accounting opens and closes (@39-@46)

# @36 — taylor closes the ward-elder routes (s05; day-fourteen; standdown begins)
6 @36 studio.time_of_day: before-first-light -> day-fourteen
  # time advance: fourteen-day skip from s02 deployment-open through s03/s04 to standdown
7 @36 studio.fauna_sense_status.coverage-scale: full-coverage-all-wards-simultaneous -> standdown-in-progress

# @37 — the east-of-water-gate gap closes (last lane drawn down; still blank)
# The gap-lane was held blank throughout the fortnight. It closes last.
# Field: studio.fauna_sense_status.eastern-gap-status (new sub-field; tracking the blank lane status)
# Prior state: blank-through-fortnight (the gap was blank throughout; the Norren attribution screens
# the gap-figure in the apparatus picture; the gap's coverage-status has been "blank" since c17).
8 @37 studio.fauna_sense_status.eastern-gap-status: blank-through-fortnight -> closed-at-standdown
  # field-extension: studio.fauna_sense_status.eastern-gap-status (new; MARGIT REFERRAL)
  # NOTE: studio.fauna_sense_status.coverage-scale continues drawdown after @37; full baseline restore
  # implied at end of standdown sequence; the transition completes through @38 as the moths settle.

# @39 — taylor opens the cost-ledger column (accounting begins)
# The cost-ledger opens for the fortnight's accounting. Prior state: the c17 accounting left
# prop:cost-ledger.protection-entry-column: blank-held. The c18 accounting reopens the column
# structure for the full fortnight-close entry sequence.
# Using studio.cost-ledger.* form per instructions (no prop card confirmed for oc-cost-ledger).
9 @39 studio.cost-ledger.condition: closed -> open-accounting-in-progress

# @41 — taylor closes the protection-entry line
# The protection-entry line closes: protection delivered, Wren screened.
# political_register-prot +0.5 fires here (the contempt filed at near-saturation without exit).
10 @41 studio.cost-ledger.protection-entry: in-progress -> closed

# @42 — the column receives the contempt-entry
# The contempt is entered in the column — complete, named, no mechanism for refusal attached.
# This is a discrete, persistent field change: the contempt-entry is now in the ledger.
11 @42 studio.cost-ledger.contempt-entry: absent -> entered-complete

# @43 — taylor writes the standdown line
# position-prot-collapse -0.5 fires here. The standdown line is the accounting record of the
# network returning to baseline — the instrument documented as deployed and withdrawn.
12 @43 studio.cost-ledger.standdown-line: absent -> written

# @44 — the ledger closes the disposal-calculus entry
# social_tether-prot-collapse -0.5 fires here. The disposal calculus is a concrete entry:
# more load-bearing = more precisely disposable post-need.
13 @44 studio.cost-ledger.disposal-calculus-entry: absent -> closed

# @45 — taylor passes the recognition column (blank column; the blank persists)
# The blank column is the enacted suppression: Taylor passes it and leaves it blank.
# The field state is: blank (the column was never filled; no change to record a fill).
# Frugality: the blank is not a state-change — the blank was blank before and remains blank.
# DECISION-NOT-FIRE at @45: the recognition-column's blank state is PERSISTENCE, not change.
# anti-pattern #3 (persistence-as-state) applies. The blank column's significance is carried
# by the scene-map BLANK-COLUMN-SUPPRESSION protected-pattern; no state-update warranted.

# @46 — taylor sets the stylus (accounting closes)
# The cost-ledger closes: stylus set beside.
14 @46 studio.cost-ledger.condition: open-accounting-in-progress -> closed-stylus-set-beside

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
