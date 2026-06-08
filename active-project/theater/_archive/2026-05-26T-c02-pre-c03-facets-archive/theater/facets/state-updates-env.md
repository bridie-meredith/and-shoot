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
