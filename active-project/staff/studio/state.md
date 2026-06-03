# studio state

episode: b01c12
last_updated: 2026-06-03
action: location-state R1 blind authoring — /and-facets b01-c12 Phase 1

## Current set (b01c11 chapter-close)
location: the-feed-station (end-of-day; accounting closed)
time_of_day: end-of-day
weather: none
ambient_conditions:
  - feed-station surface: feed-ledger closed, soap-lane-report-packet sealed (on surface or with Taylor)
  - Gold-Cloak-pair-posted at lane-junction-patrol (carry from b01c10; unchanged)
  - oc-jarvis-packet (b01c10 packet): in transit with jarvis-coin-kl-courier (departed @1)
  - studio.fauna_sense_status.lower-gate-road-coverage: corwick-absent (carry from b01c10)

## Location-state sequence locked (b01c11) — 6 entries, 0 cull
  loc-state:1 @1  — the-feed-station | morning | none | station-surface-packet-at-hand-off | sealed packet at surface edge where Jarvis takes it (place-anchor; time-of-day reset to morning)
  loc-state:2 @8  — oc-cloth-merchant-shop | morning | none | back-worktable-open, rushlight-lit | narrow back-worktable open in low rushlight (scene-B place-anchor)
  loc-state:3 @9  — oc-cloth-merchant-shop | morning | none | back-worktable-open, messenger-at-threshold | threshold carrying off-hour body (state-change: new entrant)
  loc-state:4 @17 — oc-soap-rendering-lane | afternoon | none | cross-lane-open | cross-lane at soap-rendering lane mouth, open to approach (scene-C place-anchor)
  loc-state:5 @22 — the-feed-station | end-of-day | none | station-surface-clear, accounting-in-motion | feed-station surface bare, ledger open before arm-closes (scene-D place-anchor + time-of-day advance)
  loc-state:6 @23 — the-feed-station | end-of-day | none | accounting-in-motion | continuity-from loc-state:5: accounting surface still under hand through the four arm-close sequence (continuity-carry)
  Continuity-carry: @23 qualifies — scene-D fusion-eligible-run (@23-@26); falling-to-close-image (resolving posture; not in excluded list)
  Cull: 0 entries removed — all 6 survive strip / pointing / frugality / previous-entry tests

## Sensory facet filed (b01c11) — 2 entries, 0 cull
  sensory:1 @11 — smell: shop-ambient -> paper-burning-char (scene-B; burn-beat smell onset)
  sensory:2 @27 — sound: stylus-on-surface-rhythm -> silence (scene-D terminal; accounting-close cutoff)
  Density: 2/27 = 7.4% — SHORT-CHAPTER EXEMPTION ACTIVE (27 < 30; modality-count = floor = 2; ceiling relaxed to max(6%, 7.4%) = 7.4%; ADVISORY not blocking)
  Modalities: smell + sound (2; meets ≥2 floor)
  Per-scene cap: scene-A=0, scene-B=1 (@11), scene-C=0, scene-D=1 (@27) — all within ≤3
  SEAM-C11-SENSORY-001: @13/@14 grounding-ledger anticipation cannot be satisfied by sensory-flags (fauna-feed-extension reject); narrator-interest must carry the insect-feed thermal/smoke relay materiality
  SEAM-C11-SENSORY-002: sensory:2 old-state partial lineage; R2 confirm or add loc-state sensory-note at @22

## State-updates-env locked (b01c11) — 14 entries, 6 decisions-not-fire
  state:1  @1  — prop:oc-jarvis-packet.holder: station-surface -> jarvis-coin-kl-courier
  state:2  @5  — prop:oc-feed-ledger.condition: closed -> open
  state:3  @6  — prop:oc-feed-ledger.source-field-entry: absent -> lane-pattern-only
  state:4  @11 — prop:oc-cloth-merchant-paper.physical-condition: intact -> burned
  state:5  @16 — prop:oc-feed-ledger.cloth-merchant-entry: absent -> timestamp-marked
  state:6  @18 — prop:oc-soap-lane-report-packet.holder: soap-lane-contact -> taylor-hebert-kl-122ac
  state:7  @20 — prop:oc-soap-lane-report-packet.content: nighttime-visitor-report -> precinct-pattern-sourcing-added
  state:8  @21 — prop:oc-soap-lane-report-packet.physical-condition: opened -> sealed
  state:9  @22 — studio.time_of_day: afternoon -> end-of-day
  state:10 @23 — prop:oc-feed-ledger.jarvis-entry: open -> closed
  state:11 @24 — prop:oc-feed-ledger.oswyn-entry: open -> closed
  state:12 @25 — prop:oc-feed-ledger.contacts-entry: open -> closed
  state:13 @26 — prop:oc-feed-ledger.arrangement-entry: open -> closed
  state:14 @27 — prop:oc-feed-ledger.condition: open -> closed
  Decisions-not-fire: @2 (fine-grain folding), @7 (withhold physical-completion stylistic), @8 (scene-local worktable), @9 (scene-local visitor), @10 (held-against-turn), @12 (scene-local iron-dish ash), @13/@14 (instrument-subject/actor-fork), @15 (routine bolt-ticket), @17 (actor-fork authority), @19 (held-against-turn), @15 (see above)
  Field-extensions (8): oc-cloth-merchant-paper (new prop), oc-soap-lane-report-packet (new prop), feed-ledger.source-field-entry, feed-ledger.cloth-merchant-entry, feed-ledger.jarvis-entry, feed-ledger.oswyn-entry, feed-ledger.contacts-entry, feed-ledger.arrangement-entry
  Margit referrals pending: oc-cloth-merchant-paper.card.md (new); oc-soap-lane-report-packet.card.md (new); oc-feed-ledger schema extension (8 new fields); oc-cloth-merchant-shop.card.md (location)

## Seams flagged for R2
  SEAM-C11-LOC-001: oc-cloth-merchant-shop — no confirmed warehouse card; margit referral
  SEAM-C11-LOC-002: oc-soap-rendering-lane — no confirmed warehouse card; margit referral
  SEAM-C11-LOC-003: feed-POV interpretation of @3/@4 and @13/@14 — physical vs. mediated spaces; R2 ruling needed
  SEAM-C11-LOC-004: cloth-merchant-shop slug consistency with hook-ward / oc-hook-precinct umbrella
  SEAM-C11-SENSORY-001: @13/@14 grounding-ledger anticipation — fauna-feed-extension reject; narrator-interest vehicle
  SEAM-C11-SENSORY-002: sensory:2 @27 old-state partial lineage
  SEAM-C11-ENV-001: oc-cloth-merchant-paper first-touch old-state "intact" — no prior anchor
  SEAM-C11-ENV-002: oc-soap-lane-report-packet first-touch at @18 — no prior anchor
  SEAM-C11-ENV-003: studio.time_of_day afternoon old-state at @22 — inferred from scene-map; no explicit prior state-update for afternoon
  SEAM-C11-ENV-004: four arm-close fields old-state "open" — inferred from @5 ledger-open + circuit work; R2 confirm adequacy



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

## State-updates-env locked (b01c10) — 7 entries, 5 decisions-not-fire
  state:1 @12 — prop:oc-jarvis-packet.wax-condition: pliable -> dry
  state:2 @15 — studio.fauna_sense_status.lower-gate-road-coverage: corwick-present -> corwick-absent
  state:3 @17 — studio.spatial_layout.lane-junction-patrol: unposted -> Gold-Cloak-pair-posted
  state:4 @20 — prop:oc-feed-ledger.condition: closed -> open
  state:5 @21 — prop:oc-feed-ledger.corwick-entry: absent -> written
  state:6 @25 — prop:oc-feed-ledger.condition: open -> closed
  state:7 @27 — prop:oc-feed-record.corwick-entry: logged-withheld -> persisting-post-closure
  Culled (not-fired): @1 holder (first-touch low canonical value), @2 seal-condition (intermediate), @4 physical-condition (intermediate), @6 physical-condition (intermediate), @11 feed-record surrender (intermediate; subsumed by @27 terminal)
  Field-extensions (5): prop:oc-jarvis-packet.wax-condition; studio.fauna_sense_status.lower-gate-road-coverage; studio.spatial_layout.lane-junction-patrol; prop:oc-feed-ledger.condition + corwick-entry (new oc-prop); prop:oc-feed-record.corwick-entry (new oc-prop)
  Margit referrals pending: oc-feed-ledger.card.md (new); oc-feed-record.card.md (new); oc-jarvis-packet.card.md (carry from b01c08/c09 — still pending)
  Density note: 7/27 = 26%; absolute count within s01e01 band ceiling (14); all 7 clear Reality+Authority+Frugality; no density-on-flat contamination
  State-updates-env R1 authored 2026-06-02 — theater/facets/state-updates-env-b01-c10.md (7 entries)
  _inflight: theater/facets/_inflight/proto-lines-state-env.md filed (citations @12, @15, @17, @20, @21, @25, @27)

## Prop state at b01c10 chapter-close (projected from state-updates-env R1)
  - prop:oc-jarvis-packet (b01c10 incoming): wax-condition=dry (@12; persistent)
  - prop:oc-feed-ledger.condition: closed (@25; persistent)
  - prop:oc-feed-ledger.corwick-entry: written (@21; permanent)
  - prop:oc-feed-record.corwick-entry: persisting-post-closure (@27; terminal canonical fact)
  - studio.fauna_sense_status.lower-gate-road-coverage: corwick-absent (@15; persistent into downstream chapters)
  - studio.spatial_layout.lane-junction-patrol: Gold-Cloak-pair-posted (@17; posted/stationary; persistent)
  - All b01c09 carry-forward entries unchanged (fauna_sense_status.oswyn-watcher-network, feed-edge-geometry, water-point-geometry; spatial_layout.water-point-position)

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
