# studio state

episode: b01c08
last_updated: 2026-05-31
action: location-state R1 blind authoring — /and-facets b01-c08 Phase 1

## Current set
location: the-hook-ward (water-point approach, chandler-corner-adjacent)
time_of_day: evening (scene-C; afternoon for scenes A + B)
weather: none
ambient_conditions:
  - lane-junction-rushwick-margin active (scene-A circuit entry)
  - water-point occupied by watcher-boy (scene-A; vacated scene-C @23)
  - feed-station intake position (scene-B)
  - watcher-boy-position vacated from water-point (scene-C @23)

## Chapter-close spatial anchors
  - Taylor: completed circuit; chapter-close at hook-ward (evening return; walked away after @22)
  - Oswyn: still talking at water-point approach when Taylor leaves (@24)
  - Corwick (the-courier): at water-point location with Oswyn; Taylor does not follow him
  - watcher-boy: position vacated from water-point (@23; now inside Taylor's coverage matrix)

## Location-state sequence locked (b01c08) — 6 entries, 0 cull
  loc-state:1 @1  — the-lane-junction-rushwick-margin | afternoon | none | lane open, circuit-start
  loc-state:2 @3  — the-hook-ward | afternoon | none | water-point occupied
  loc-state:3 @4  — the-hook-ward | afternoon | none | lane-mouth watched
  loc-state:4 @9  — the-feed-station | afternoon | none | packet on intake surface
  loc-state:5 @16 — the-hook-ward | evening | none | water-point approach, return-circuit
  loc-state:6 @23 — the-hook-ward | evening | none | water-point vacated (state-change)
  No continuity-carry entries: scene-A rhythm-shape is rising-to-low-peak (license excluded); scene-B rhythm-shape is flat-tense-with-edge-acquisition-at-close (NOT flat-low/resolving/release-only; excluded); scene-C rhythm-shape is rising-to-quiet-peak (excluded)
  Cull: 0 entries removed — all 6 survive strip / pointing / frugality / previous-entry tests

## Last recorded change (b01c08)
  @1  — Taylor enters lane-junction-rushwick-margin (scene-A circuit open)
  @3  — watcher-boy at water-point (sub-location established)
  @4  — basket-woman at lane-mouth (sub-location established)
  @9  — Jarvis packet arrives at feed-station (scene-B location transition)
  @16 — Taylor enters hook-ward evening return
  @23 — watcher-boy-position vacated from water-point (state-change: position now inside coverage matrix)
  Location-state R1 blind authored 2026-05-31 — theater/facets/location-state-b01-c08.md (6 entries)
  _inflight: theater/facets/_inflight/proto-lines-loc-state.md filed (citations @1, @3, @4, @9, @16, @23)

## Coverage state (b01c08 chapter-close)
  coverage_active_range: hook-ward + rushwick-extension + oswyn-watcher-network integrated
    - oc-hook-precinct (c01–c03 baseline)
    - oc-pig-tallow-lane (c04 day-1)
    - oc-stitch-house-lane (c04 day-1)
    - oc-ropers-court (c04 day-2)
    - the-rushwick (c05)
    - oswyn-watcher-network corridors integrated (c08 s01; three approach-corridors)

## Seams flagged for R2
  - The-feed-station (@9): no authored location card in warehouse; location slug drawn from bones header `locations:` field; R2 reviewer should confirm card-existence or flag margit referral for oc-feed-station.card.md
  - Sub-location slug canonicity: `the-water-point`, `the-lane-mouth`, `the-chandler-corner`, `the-lane-junction-rushwick-margin` all drawn from bones OBJECT fields and may be sub-locations of `the-hook-ward` or `oc-rushwick` rather than independent cards; R2 auditor should verify slug resolution against warehouse inventory
