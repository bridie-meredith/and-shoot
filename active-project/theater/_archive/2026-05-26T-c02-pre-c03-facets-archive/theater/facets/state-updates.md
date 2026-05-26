---
facet: state-updates
sources: [env, taylor-hebert-kl-122ac]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates-env
episode: b01c02
author: studio
scope: environment + location + prop only (actor-state authored separately)
---

# rubric-carve-out — held-against-turn exemption for genuine peak-shadow env-dropout
#
# design/shoot-v2/rubric-state-updates.md § "Held-against-turn (approach-to-peak class)"
#
# Carve-out scope: entry 3 (@10, studio.suppression_cost_active)
# Carve-out rule: held-against-turn prohibition ("canonical state-update co-citation is withheld")
#   applies to approach bones where the tracked change has NOT YET occurred. @10 is not an
#   approach to the suppression-cost — the suppression-cost fires AT @10 (the alley-back dropout
#   is the event itself). The extend at peak @11 is Taylor's response to the cost already having
#   landed. The prohibition targets pre-emption; firing on the beat where the field actually flips
#   is correct even when that beat is a peak-shadow.
# Coverage justification: strip-test passes — without this entry, suppression_cost_active would
#   have no recorded flip, and the downstream feed-state coherence depends on knowing when cost
#   became active. Reality axis clear; authority axis clear; frugality axis clear.
#
# Per-entry annotations:
# - state-updates-env:3 @10: held-against-turn carve-out applies; the dropout IS the state-change,
#   not an approach to it; @11 extend is a distinct subsequent action.

1 @1 studio.time_of_day: night-b01c01-end -> dawn-grey-hour
# field-extension: time_of_day (first-touch b01c02 chapter-open; b01c01 ended in evening/night;
#   scene-A opens at dawn per scene-map "dawn-to-day" label)

2 @9 studio.coverage_map_extent: subsistence-range -> four-hundred-bodies-active

3 @10 studio.suppression_cost_active: false -> true
# held-against-turn carve-out applies (see preamble); @10 is the dropout-event, not its approach

4 @11 studio.fauna_sense_status: ambient-subsistence-passive -> deliberate-precinct-coverage
# field-extension: fauna_sense_status (insect-network deployment mode; first systematic precinct
#   sweep declared; peak bone @11 per scene-map — co-citation strongly expected)

5 @16 studio.active_conditions: baseline-no-smoke-marker -> tallow-smoke-stitch-house-lane-active
# field-extension: active_conditions first-touch for tallow-smoke condition at stitch-house-lane;
#   persistent throughout scene-B and into scene-C (lane identity marker)

6 @18 studio.day_cycle: day-1 -> multi-day-accumulation
# field-extension: day_cycle (multi-sweep time passage; scene-B declared "days-of-coverage" per
#   scene-map; @18 is first bone of fusion-eligible @18-@19 accumulation run; "return" verb at @18
#   signals repeated-pass pattern beginning)

7 @32 studio.time_of_day: dawn-to-day -> late-afternoon-end-of-day
# scene-C seam-bridge; "the shadow fills the drain angle" is the explicit light/time marker;
#   scene-map labels scene-C "end-of-day"

# source: taylor-hebert-kl-122ac
facet: state-updates
episode: b01-c02
author: impersonator:taylor-hebert-kl-122ac
target-scope: actor:taylor-hebert-kl-122ac
---

# rubric-carve-out — wren-recognition field uses operational vocabulary, not registration vocabulary
#
# state-updates rubric (design/shoot-v2/rubric-state-updates.md) § anti-pattern #1 (registration-as-state)
#
# Carve-out scope: actor:taylor-hebert-kl-122ac.wren-recognition entries (#4, #5)
# Carve-out rule: the field tracks operational categorization of Wren in Taylor's coverage-map ledger (a tracked knowledge-state extension), not Taylor's perceptual noticing. Vocabulary is operational/structural (registered-as-junction-body, filed-as-ward-junction-contact) per prompt directive forbidding `noticed`/`registered`/`awareness`/`baseline-new-faces` registration-as-state vocabulary. The "registered" prefix in the value-string is operational-ledger-state, not perception.
# Coverage justification: Wren entering the coverage map as a function-node is a persistent canonical knowledge-state change (anchor account opens per scene-B substance_delta relational_anchor_status +1.0); the categorization persists past the beat and is load-bearing for chapter close.
#
# Per-entry annotations:
# - state:4 @15: operational-ledger-state ("registered-as-junction-body" = filed-as-body-with-junction-signature, not perceptual noticing). POV co-cite required (paired with narrator-interest at @15).
# - state:5 @27: peak-bones-class beat (scene B peak); irreversible categorization-flip; POV co-cite required.

8 @11 actor:taylor-hebert-kl-122ac.coverage-mode: subsistence -> systematic-deliberate
9 @11 actor:taylor-hebert-kl-122ac.range-ceiling: working -> into-the-fours-under-suppression-cost
10 @12 actor:taylor-hebert-kl-122ac.prohibition-line: held -> re-affirmed-reads-not-directs
11 @15 actor:taylor-hebert-kl-122ac.wren-recognition: unaware -> registered-as-junction-body
12 @27 actor:taylor-hebert-kl-122ac.wren-recognition: registered-as-junction-body -> filed-as-ward-junction-contact
13 @40 actor:taylor-hebert-kl-122ac.moral_legibility_to_self: pre-crack -> crack-arriving
14 @41 actor:taylor-hebert-kl-122ac.moral_legibility_to_self: crack-arriving -> crack-held
15 @42 actor:taylor-hebert-kl-122ac.moral_legibility_to_self: crack-held -> crack-suppressed-under-harm-reduction
16 @43 actor:taylor-hebert-kl-122ac.body-posture: settled -> closed-against-drain-angle
17 @47 actor:taylor-hebert-kl-122ac.coverage-map-state: complete-with-stall -> ledger-closed
# field-extension: coverage-mode, range-ceiling, prohibition-line, wren-recognition, moral_legibility_to_self, body-posture, coverage-map-state — all tracked knowledge/operational/posture-state extensions on actor:taylor-hebert-kl-122ac state schema; defended under §"Field-extension protocol" (tracked-state aspects, not perceptions or stylistic flourishes).
# Cross-facet contract: POV actor-state requires narrator-interest co-citation at @11, @12, @15, @27, @40, @41, @42, @47. Entries 9 (body-posture @43) is body-charge posture-state — narrator-interest co-citation permitted but not required.
# Persistence: every entry's <new> value persists past the anchor beat through chapter close OR until the next entry on the same field. coverage-mode locks for chapter+series scope; range-ceiling locks for chapter (suppression-cost active throughout); prohibition-line state persists from @12 through @40 where tested, then re-affirmed-suppressed at @42; wren-recognition advances through three filed states; moral_legibility_to_self transitions in three consecutive load-bearing beats across the scene-C peak window; body-posture closed-against-drain-angle persists from @43 through ledger close (@44-@47); coverage-map-state ledger-closed locks at chapter close.
# Strip-test: every entry passes — without the fire, downstream canonical state would mis-track the chapter's structural deltas (relational_anchor_status +1.0 at @27, moral_legibility_to_self +1.0 across @40-@42, capability-mode shift at @11).
# Peak-bones honored: scene-A @11 (FIRE ×2), scene-B @27 (FIRE), scene-C @40 (FIRE) — all three peaks carry state-update support.
# Held-against-turn honored: @25 (peak-shadow approach to @27) NOT fired — categorization-flip lands at the peak @27. @39 (peak-shadow approach to @40) NOT fired — recognition lands at peak @40. @10 (peak-shadow approach to @11) NOT fired — range-ceiling flip lands at @11.
