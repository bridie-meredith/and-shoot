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

## State-updates-env locked (b01c08) — 7 entries, 0 cull
  state:1 @8  — studio.fauna_sense_status.oswyn-watcher-network: uncharted -> integrated-into-coverage
  state:2 @9  — prop:oc-jarvis-packet.state: absent -> arrived-at-feed-station
  state:3 @10 — prop:oc-jarvis-packet.seal-condition: sealed -> broken
  state:4 @13 — prop:oc-feed-station-ledger.aemond-entry: absent -> logged
  state:5 @15 — studio.fauna_sense_status.feed-edge-geometry: pre-aemond-entry -> aemond-edge-lit
  state:6 @23 — studio.spatial_layout.water-point-position: watcher-boy-stationed -> watcher-boy-absent
  state:7 @24 — studio.fauna_sense_status.water-point-geometry: oswyn-network-managed -> insect-feed-covered
  Cull: 0 entries removed — all 7 survive strip / persistence / authority / frugality tests
  Field-extensions (6): oswyn-watcher-network (fauna_sense_status), feed-edge-geometry (fauna_sense_status),
    water-point-geometry (fauna_sense_status), water-point-position (spatial_layout),
    prop:oc-jarvis-packet (new oc-prop), prop:oc-feed-station-ledger (new oc-prop)
  Margit referrals pending: oc-jarvis-packet.card.md, oc-feed-station-ledger.card.md

## Prop state at b01c08 chapter-close
  - prop:oc-jarvis-packet: state=opened (post @10); seal-condition=broken; contents-read; consumed within chapter
  - prop:oc-feed-station-ledger.aemond-entry: logged (@13; persistent)
  - studio.fauna_sense_status.oswyn-watcher-network: integrated-into-coverage (@8; persistent)
  - studio.fauna_sense_status.feed-edge-geometry: aemond-edge-lit (@15; persistent into downstream chapters)
  - studio.spatial_layout.water-point-position: watcher-boy-absent (@23; watcher-boy vacated; insect-feed covers)
  - studio.fauna_sense_status.water-point-geometry: insect-feed-covered (@24; chapter terminal image enacted)

  State-updates-env R1 authored 2026-05-31 — theater/facets/state-updates-env-b01-c08.md (7 entries)
  _inflight: theater/facets/_inflight/proto-lines-state-env.md filed (citations @8, @9, @10, @13, @15, @23, @24)

## Sensory facet filed (b01c08) — 2 entries
  sensory:1 @10 — sound: feed-station-working-quiet -> wax-seal-crack (spike)
  sensory:2 @16 — light: afternoon-stone-lane-light -> evening-lane-dusk-fall (down)
  Density: 2/24 = 8.3% — above standard 6% ceiling; at short-chapter exemption ceiling max(6%, 2/24) = 8.3%; ADVISORY not blocking
  Modalities: sound + light (2; meets ≥2 floor exactly)
  Per-scene cap check: scene-A=0, scene-B=1 (@10), scene-C=1 (@16) — all within ≤3 cap
  Old-state anchor check: sensory:1 old-state sourced from series-established indoor-administrative-quiet vocabulary (carve-out preamble filed); sensory:2 old-state from scene-map time-of-day afternoon->evening transition (carve-out preamble filed); both follow b01c06 SEAM-009 precedent; loc-state ratification expected when loc-state fork completes
  Cull: 0 entries removed post-cull (both survive four-axis rubric check)
  SEAM-010: sensory:1 @10 + sensory:2 @16 old-state anchors sourced from series-vocabulary and scene-map respectively; rubric-carve-out preamble in sensory-b01-c08.md; flagged for R2 reviewer attention; if loc-state contradicts either baseline, revise or delete the affected entry
  Files: theater/facets/sensory-b01-c08.md (facet) + theater/facets/_inflight/proto-lines-sensory-b01-c08.md (inflight)
