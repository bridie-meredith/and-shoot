# studio state

episode: b01c09
last_updated: 2026-06-01
action: location-state R1 blind authoring — /and-facets b01-c09 Phase 1

## Current set
location: the-feed-station (scene-C close; end of day)
time_of_day: end-of-day (late-morning for scene-A; evening for scenes B + C)
weather: none
ambient_conditions:
  - oc-stitch-house-lane lanes accessible (scene-A; stitch-shop door open at lane-mouth)
  - oc-dragonpit-margin outer circuit active (scene-B; supply cart on gate-road; stone-post at lower gate side-exit)
  - lower-gate occupied: Corwick at stone-post with second man (scene-B mid; cleared by chapter-close)
  - feed-station surface: ward-coverage notes (left) + sealed Jarvis-channel packet (right); seal dry (scene-C close)

## Chapter-close spatial anchors
  - Taylor: feed-station; accounting closed; sealed packet on station surface; internal map held separately
  - Wren: in coverage; daily circuit (stitch-shop → water-sellers → bread-seller corner) mapped in internal map; not in deliverable
  - Corwick: at lower-gate stone-post (scene-B); observed, logged internally, withheld from Jarvis
  - The sealed Jarvis packet: contains boundary geometry + lane-density + Rushwick intercept fragments; does NOT contain Wren's pattern or courier observation

## Location-state sequence locked (b01c09) — 5 entries, 0 cull
  loc-state:1 @1  — oc-hook-precinct | late-morning | none | lane-open | the lane-mouth south of the Hook (scene-A place-anchor)
  loc-state:2 @3  — oc-stitch-house-lane | late-morning | none | door-open | the stitch-shop door standing open at the lane-mouth (state-change)
  loc-state:3 @8  — oc-dragonpit-margin | evening | none | lane-open, outer-circuit | the outer lane below the Dragonpit margin (scene-B place-anchor)
  loc-state:4 @11 — oc-dragonpit-margin | evening | none | courier-at-stone-post | Corwick at the lower-gate stone-post (state-change: new entrant)
  loc-state:5 @17 — the-feed-station | end-of-day | none | station-surface-clear | the station surface with unsealed packet and ward-coverage notes (scene-C place-anchor)
  No continuity-carry entries: scene-A rhythm-shape rising-to-quiet-peak (excluded); scene-B rhythm-shape rising-to-quiet-peak (excluded); scene-C rhythm-shape falling-to-thesis-image (not flat-low/resolving/release-only; excluded)
  Cull: 0 entries removed — all 5 survive strip / pointing / frugality / previous-entry tests

## Last recorded change (b01c09)
  @1  — Taylor enters lane-south-of-the-hook (scene-A circuit open)
  @3  — stitch-shop door opens the lane-mouth (state-change; threshold condition shifts)
  @8  — Taylor enters dragonpit-margin outer lane (scene-B circuit; time-of-day: evening)
  @11 — insect-feed returns Corwick at lower-gate stone-post (state-change: new entrant at stone-post / side-exit)
  @17 — Taylor takes the feed-station (scene-C; end-of-day accounting open)
  @23 — seal dries (chapter terminal: split-substrate architecture enacted; both omissions sealed into separate records)
  Location-state R1 blind authored 2026-06-01 — theater/facets/location-state-b01-c09.md (5 entries)
  _inflight: theater/facets/_inflight/proto-lines-loc-state.md filed (citations @1, @3, @8, @11, @17)

## Coverage state (b01c09 chapter-close)
  coverage_active_range: hook-ward + stitch-shop-lanes + dragonpit-margin (south-extended) + oswyn-watcher-network integrated
    - oc-hook-precinct (c01–c03 baseline)
    - oc-pig-tallow-lane (c04 day-1)
    - oc-stitch-house-lane (c04 day-1)
    - oc-ropers-court (c04 day-2)
    - the-rushwick (c05)
    - oswyn-watcher-network corridors integrated (c08 s01)
    - dragonpit-margin outer lanes (c09 s02 evening circuit; Rushwick-south extension)

## Seams flagged for R2
  - oc-dragonpit-margin: no warehouse card confirmed; slug drawn from bones `locations:` field; margit referral may be needed
  - the-feed-station: no warehouse card confirmed (carry from b01c08 seam; still unresolved)
  - oc-hook-precinct vs the-hook-ward slug: b01c08 used `the-hook-ward` for scene-A/C; b01c09 uses `oc-hook-precinct` for the lane-south entry; R2 reviewer should confirm slug consistency across chapters or flag for margit canonicalization
  - Corwick bare-slug (@11 and in bones): pl-2026-06-01-001 (b01c08 precedent) resolved this as acceptable in bones; loc-state:4 uses `corwick` as focus-element name in sensory note — consistent with bones discipline

## State-updates-env locked (b01c09) — 4 entries, 0 cull
  state:1 @7  — prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-corridors -> hook-rushwick-oswyn-corridors-plus-south-extension
  state:2 @18 — prop:oc-jarvis-packet.physical-condition: assembled -> folded
  state:3 @19 — prop:oc-jarvis-packet.seal-condition: unsealed -> sealed
  state:4 @23 — prop:oc-jarvis-packet.seal-condition: sealed -> dry
  Cull: 0 entries removed — all 4 survive strip / persistence / authority / frugality tests
  Field-extensions (2): prop:oc-ward-coverage-notes.content (new oc-prop field; b01c09 first-touch; margit referral pending)
                         prop:oc-jarvis-packet.physical-condition (new field on existing oc-prop established at b01c08; extends lifecycle tracking)
  Margit referrals pending: oc-ward-coverage-notes.card.md (new); oc-jarvis-packet.card.md (carry from b01c08 — still pending)

## Prop state at b01c09 chapter-close
  - prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-corridors-plus-south-extension (@7; persistent into downstream chapters)
  - prop:oc-jarvis-packet (b01c09 packet): physical-condition=folded (@18), seal-condition=dry (@23; persistent at chapter-close; packet sits on station surface right of ward-coverage notes)
  - studio.fauna_sense_status.oswyn-watcher-network: integrated-into-coverage (carry from b01c08 @8; unchanged this chapter)
  - studio.fauna_sense_status.feed-edge-geometry: aemond-edge-lit (carry from b01c08 @15; unchanged this chapter)
  - studio.spatial_layout.water-point-position: watcher-boy-absent (carry from b01c08 @23; unchanged this chapter)
  - studio.fauna_sense_status.water-point-geometry: insect-feed-covered (carry from b01c08 @24; unchanged this chapter)

  State-updates-env R1 authored 2026-06-01 — theater/facets/state-updates-env-b01-c09.md (4 entries)
  _inflight: theater/facets/_inflight/proto-lines-state-env.md filed (citations @7, @18, @19, @23)

## Sensory facet filed (b01c09) — 2 entries
  sensory:1 @8  — thermal: stone-lane-late-morning-warmth -> hill-lane-evening-cool (down)
  sensory:2 @23 — tactile: wax-soft-warm -> wax-set-firm (down)
  Density: 2/23 = 8.7% — short-chapter exemption ACTIVE (23 < 30; modality-count = floor = 2; ceiling relaxed to max(6%, 2/23) = 8.7%; ADVISORY not blocking)
  Modalities: thermal + tactile (2; meets ≥2 floor exactly)
  Per-scene cap check: scene-A=0, scene-B=1 (@8), scene-C=1 (@23) — all within ≤3 cap
  Priority brief honoured: @8 addresses BONES-AIRLESS-RISK (scene-B opening grounded physically before @11 apparatus-feed); @23 addresses terminal-image tactile anchor
  Old-state anchors: sensory:1 from scene-map time-of-day annotation (late-morning scene-A → evening scene-B + Dragonpit hill location; follows b01c08 SEAM-009/010 carve-out precedent); sensory:2 entailed by @19 sealing-act (wax applied soft-warm, hardens by @23)
  SEAM-011: sensory:1 old-state "stone-lane-late-morning-warmth" has no prior loc-state anchor in b01c09; R2 reviewer must confirm loc-state:3 baseline does not contradict; if it does, revise or delete sensory:1
  Cull: 2 entries refused at file-shape pass — @3 smell (genuine but activates 3-modality standard ceiling; priority brief does not call for scene-A grounding) and @19 smell (genuine but same-scene pair with @23 weakens separation; @8+@23 two-scene distribution is stronger)
  Files: theater/facets/sensory-b01-c09.md (facet) + theater/facets/_inflight/proto-lines-sensory.md (inflight)
