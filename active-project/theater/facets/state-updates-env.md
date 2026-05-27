facet: state-updates
scope: env (studio.* and prop:* only; actor:* authored separately)
episode: b01c04
author: studio
---

# rubric-carve-out — above-band density justified by multi-ward / multi-day chapter structure
#
# design/shoot-v2/rubric-state-updates.md § Curve-shape rubric
#
# Carve-out scope: all 14 env entries in this file
# Carve-out rule: rubric band 8-18% (3-7 fires on 39 bones) calibrated for a single-location
#   single-day episode (s01e01 archetype). b01c04 covers 4 locations across 2 calendar days
#   with a prop handoff chain. The elevated fire rate (14 entries, ~36%) reflects structural
#   chapter geography, not registration-as-state or density-on-flat contamination. Each entry
#   passes the strip test, the persistence test, and the authority test independently.
#   Reality-axis re-pass performed at authoring: all 14 entries survive. Density is structural.
# Coverage justification: all location transitions require active_location fire to maintain
#   canonical state for downstream chapters; all 3 coverage_active_range extensions are the
#   chapter's architectural substance per b01c04 chapter goal; report-sheet prop chain is
#   the chapter's peak-cluster material; time_of_day fires track a day-skip and a chapter-
#   open reset that cannot be inferred from other fields.
#
# Per-entry annotations (field-extension entries):
# - state:3 @15: field-extension: coverage_active_range (new field; tracks geographic scope
#     of Taylor's insect-feed as an env-observable fact under studio.fauna_sense_status;
#     not a Taylor actor-state field — actor:taylor.capability tracks the deployment scale;
#     studio.coverage_active_range tracks which ward-zones are under live feed coverage as
#     an environmental fact the location state must record; field-extension justified under
#     §"Field-extension protocol" as a tracked-state-aspect, not a perception or flourish)
# - state:4 @22: same field-extension clause as state:3
# - state:7 @27: same field-extension clause as state:3; this is the completion entry
# - state:10 @31: field-extension: prop:oc-report-sheet.holder (new prop; no warehouse card;
#     oc- slug used per rubric §Authority ACCEPT signature for project-original props with
#     explicit scene presence; prop is physically named and passed in bones @31-@32;
#     holder is a standard prop-state field per rubric)
# - state:11 @32: same oc-report-sheet field-extension clause as state:10

1 @1 studio.time_of_day: third-bell-noon → first-bell-morning
2 @13 studio.active_location: oc-cooper-yard-eel-alley → oc-pig-tallow-lane
3 @15 studio.coverage_active_range: oc-hook-precinct → oc-hook-precinct + oc-pig-tallow-lane # field-extension: coverage_active_range (new field; see carve-out preamble)
4 @22 studio.coverage_active_range: oc-hook-precinct + oc-pig-tallow-lane → oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane # field-extension
5 @25 studio.time_of_day: first-bell-morning-day-1 → early-morning-grey-day-2
6 @25 studio.active_location: oc-pig-tallow-lane → oc-ropers-court
7 @27 studio.coverage_active_range: oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane → oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane + oc-ropers-court # field-extension
8 @29 studio.active_location: oc-ropers-court → oc-cooper-yard-eel-alley
9 @29 studio.actors_in_yard: [taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]
10 @31 prop:oc-report-sheet.holder: taylor-hebert-kl-122ac → in-transit-yard-air # field-extension: prop:oc-report-sheet.holder
11 @32 prop:oc-report-sheet.holder: in-transit-yard-air → jarvis-coin-kl-coat # field-extension
12 @36 studio.actors_in_yard: [taylor-hebert-kl-122ac, jarvis-coin-kl-courier] → [taylor-hebert-kl-122ac]
13 @37 studio.actors_in_yard: [taylor-hebert-kl-122ac] → []
14 @39 studio.active_location: oc-cooper-yard-eel-alley → oc-stitch-house-lane
