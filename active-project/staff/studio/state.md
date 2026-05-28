# studio state

episode: b01c05
last_updated: 2026-05-28
action: location-state R1 authoring — /and-facets b01-c05 Phase 1

## Current set
location: oc-stitch-house-lane (Taylor exits @39; chapter close; walk-back through Hook)
time_of_day: early-morning (first-bell at oc-cooper-yard-eel-alley; pre-dawn grey at oc-ropers-court)
weather: none recorded
ambient_conditions:
  - oc-cooper-yard-eel-alley: tallow-damp from lane-caulking (persistent; first-bell working-hours)
  - oc-pig-tallow-lane: middens-discard-compound + carter-work-ambient (working-hours)
  - oc-ropers-court: near-silence, pre-dawn grey (early-morning; rope-walk not yet started)
  - oc-stitch-house-lane: tallow-lamp smoke at floor level (working hours); drain-water trickle

## Chapter-close spatial anchors
  - report-sheet: in jarvis-coin-kl-courier's possession (pocketed @32)
  - jarvis departed cooper's yard @36
  - taylor exiting stitch-house-lane @39 running four-ward feed

## Sensory baselines locked (b01c04)
  smell — chapter-open: eel-alley-dawn-air → tallow-damp-lane-caulking (sensory:1 @1)
  smell — scene-B entry: tallow-damp-lane-caulking → middens-discard-compound (sensory:2 @13)
  sound — scene-C entry: carter-work-ambient → roper's-court-near-silence (sensory:3 @25)

## Location-state sequence locked (b01c04) — 6 entries
  loc-state:1 @1  — oc-cooper-yard-eel-alley | predawn | tallow-damp reaches shed-wall before yard visible
  loc-state:2 @4  — oc-cooper-yard-eel-alley | predawn | shed-wall cover: back to timber, lane-mouth across open yard
  loc-state:3 @13 — oc-pig-tallow-lane | morning | three alleys converge at junction-mouth; discard-air heaviest
  loc-state:4 @25 — oc-ropers-court | predawn | early-morning grey; court sight-clear to all tributary mouths
  loc-state:5 @29 — oc-cooper-yard-eel-alley | first-bell | Jarvis at lane-mouth; half-yard open air to shed-wall
  loc-state:6 @39 — oc-stitch-house-lane | morning | north-end lane-mouth; last threshold before Hook opens out
  Cull: 2 deleted (@17 carter-parks — no subsequent actor-movement turns on it; @36 Jarvis-exits — exit legible in inherited env)

## Coverage state (state-updates-env; new field: studio.coverage_active_range)
  coverage_active_range: four-ward-complete
    - oc-hook-precinct (pre-existing; c01–c03 baseline)
    - oc-pig-tallow-lane (added state:3 @15; day-1 first-ward extension)
    - oc-stitch-house-lane (added state:4 @22; day-1 second-ward extension)
    - oc-ropers-court (added state:7 @27; day-2 completion; four-ward-complete at this entry)

## Prop state (state-updates-env; chapter-close)
  - prop:oc-report-sheet: holder = jarvis-coin-kl-coat (pocketed state:11 @32; exited scene with Jarvis @36)

## Arrangement state (state-updates-env)
  proposal_state: operational (acceptance delivered @9; first report delivered @31–@32; routing confirmed)
  routing_schedule: first-bell, three-day interval, oc-cooper-yard-eel-alley

## Last recorded change
  @39 — Taylor exits stitch-house lane; chapter close (location-state + sensory + state-updates-env all locked)
