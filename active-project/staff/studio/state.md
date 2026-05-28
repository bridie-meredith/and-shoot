# studio state

episode: b01c05
last_updated: 2026-05-28
action: state-updates-env R1 authoring — /and-facets b01-c05 Phase 1 (location-state + sensory R1 prior)

## Current set
location: the-rushwick (no oc-card; pl-2026-05-28-001 open for margit)
time_of_day: evening (scene-C close; Taylor on room-floor)
weather: none recorded
ambient_conditions:
  - the-rushwick (outdoor junction + lane-mouth + east-exit side-alley): morning ambient, no special conditions recorded
  - the-rushwick (indoor lodging room): evening; door shut; feed-review only

## Chapter-close spatial anchors
  - Taylor: room-floor of Rushwick-adjacent lodging (@20 onward; scene-C close @31)
  - courier: last known position — junction-corner (@19); not tracked past that
  - three enforcement figures: last known position — east exit corridor (@17); departed

## Location-state sequence locked (b01c05) — 9 entries
  loc-state:1 @1  — the-rushwick | morning | lane-mouth open, stone skirt at grade (world-before-protagonist anchor)
  loc-state:2 @4  — the-rushwick | morning | junction open, provisioner-train mid-cross
  loc-state:3 @6  — the-rushwick | morning | junction clearing, message-runner in-transit
  loc-state:4 @7  — the-rushwick | morning | lane-mouth at coverage-edge (far transit boundary)
  loc-state:5 @8  — the-rushwick | morning | lane-mouth threshold (courier entry, inward direction)
  loc-state:6 @10 — the-rushwick | morning | side-alley mouth open, east exit adjacent
  loc-state:7 @11 — the-rushwick | morning | alley-mouth blocked, alley-interior contained
  loc-state:8 @17 — the-rushwick | morning | alley-mouth open, east exit restored
  loc-state:9 @20 — the-rushwick | evening | indoor, room-floor, door shut
  Cull (authoring phase): 4 candidates removed
    @2 — enters rushwick (culled: @1 world-anchor already licenses ward-interior inheritance; threshold covered)
    @5 — provisioner-train takes east-lane (culled: bone self-carries direction; junction-inherited env sufficient)
    @14 — courier finds feet (culled: strip test passes in inherited alley-interior; body-state not loc-state)
    @19 — courier takes junction-corner (culled: junction established thoroughly in scenes A; alley-mouth-open @17 sufficient)
  No continuity-carry entries: all three scenes excluded by rising/rising-to-peak rhythm-shape (transition-run license does not fire)

## Coverage state (carried forward from b01c04)
  coverage_active_range: four-ward + rushwick-extension
    - oc-hook-precinct (c01–c03 baseline)
    - oc-pig-tallow-lane (c04 day-1)
    - oc-stitch-house-lane (c04 day-1)
    - oc-ropers-court (c04 day-2)
    - the-rushwick (c05; second morning after Roper's Court report; abuts Red Keep servant passages)

## Sensory facet locked (b01c05) — 2 entries
  sensory:1 @4  — tactile: lane-stone-surface-baseline -> provisioner-cart-load-on-stone (spike)
  sensory:2 @13 — sound: alley-stone-contained-silence -> courier-effortful-body-sound (spike)
  Density: 2/31 = 6.45% (ADVISORY; modality-floor priority; note-003 mandatory carry)
  Modalities: tactile + sound (2; meets ≥2 floor)
  note-003 effortful-qualifier carry: CONFIRMED at sensory:2 @13
  note-001 courier-walk visual/spatial: NOT CARRIED by sensory (rubric-ineligible; seam routed to narrator-interest)

## Prop state (state-updates-env; chapter-close)
  - prop:oc-report-sheet: holder = jarvis-coin-kl-coat (b01c04 carry; no change this chapter)
  - prop:oc-enforcement-report-entry: state = filed-with-jarvis (new prop; first-touch @16; field-extension; oc-card pending margit)
  - prop:oc-courier-body-map: state = filed (initiated @18; promoted to filed @27; cf-d10 thread confirmed; oc-card pending margit)

## Pending margit referrals
  - oc-rushwick-lodging.card.md (SEAM-001; location card for taylor's-lodging slug; priority: before stitch)
  - oc-enforcement-report-entry.card.md (SEAM-002; prop card; first-touch @16)
  - oc-courier-body-map.card.md (SEAM-003; prop card; persists to b01c06+; cf-d10 thread carrier; priority: before b01c06 facets)

## State-updates-env locked (b01c05) — 7 entries
  state:1 @2  — studio.location: oc-stitch-house-lane -> the-rushwick
  state:2 @3  — studio.coverage_active_range: four-ward-complete -> rushwick-included
  state:3 @16 — prop:oc-enforcement-report-entry.state: absent -> filed-with-jarvis (field-extension)
  state:4 @18 — prop:oc-courier-body-map.state: absent -> initiated (field-extension; cf-d10 anchor)
  state:5 @20 — studio.location: the-rushwick -> taylor's-lodging
  state:6 @20 — studio.time_of_day: morning -> evening
  state:7 @27 — prop:oc-courier-body-map.state: initiated -> filed (cf-d10 confirmed)
  Density: 7/31 = 22.6% (above band; defended — record-creation events; all entries strip-test clean)

## Last recorded change
  @31 — courier-walk holds the rushwick-pass; chapter close; Taylor on room-floor; evening review complete
  Sensory R1 authored 2026-05-28 — theater/facets/sensory.md (2 entries)
  State-updates-env R1 authored 2026-05-28 — theater/facets/state-updates-env.md (7 entries)
