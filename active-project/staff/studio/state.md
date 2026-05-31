# studio state

episode: b01c06
last_updated: 2026-05-31
action: sensory R1 authoring — /and-facets b01-c06 Phase 1

## Current set
location: oc-stitch-house-lane (south-court working position)
time_of_day: morning (single time-of-day throughout)
weather: none
ambient_conditions:
  - south-court-working-position (established at @5)
  - lane-mouth-blocked-handcart (scene-A only; @1–@4)
  - angle-gap-passable (workaround route used at @5)

## Chapter-close spatial anchors
  - Taylor: south-court working position (@26 chapter-close; closed ward-coverage notes)
  - Wren: last known — crossed crowd at lane-mouth junction, spoke to Taylor (@3–@4); not tracked after scene-A
  - the-courier: took jarvis-channel form at @24; exited south court; not tracked after
  - handcart: blocking lane-mouth through scene-A; not tracked after

## Location-state sequence locked (b01c06) — 2 entries
  loc-state:1 @1  — oc-stitch-house-lane | morning | none | lane-mouth-blocked-handcart (chapter-open place-anchor; north exit sealed, foot traffic backed up)
  loc-state:2 @5  — oc-stitch-house-lane | morning | none | south-court-working-position (threshold crossing; angle-gap workaround; establishes scene-B/C working base)
  Cull (authoring phase): 1 entry removed (@3 wren-crosses-crowd — frugality REJECT; crowd already established at @1; no new state-change; strip test passes in inherited @1 env)
  No continuity-carry entries: all fusion-eligible-runs excluded by rhythm-shape (scene-A @1-@2 = rising-to-peak; scene-B @11-@12 = flat-tense, not flat-low/resolving/release-only; scene-C @16-@17, @21-@22 = rising-to-peak)

## Last recorded change (b01c06)
  @5 — taylor-hebert-kl-122ac enters south court via angle-gap workaround; lane-blocked side behind her; working position established
  @24 — the-courier takes jarvis-channel form and exits; south-court working position otherwise unchanged to chapter-close
  Location-state R1 authored 2026-05-31 — theater/facets/location-state.md (2 entries)
  _inflight: theater/facets/_inflight/proto-lines-loc-state.md confirmed (citations @1 [loc-state:1], @5 [loc-state:2])

## Coverage state (carried forward from b01c05 + b01c07 interleave — b01c06 revise only)
  coverage_active_range: four-ward + rushwick-extension
    - oc-hook-precinct (c01–c03 baseline)
    - oc-pig-tallow-lane (c04 day-1)
    - oc-stitch-house-lane (c04 day-1)
    - oc-ropers-court (c04 day-2)
    - the-rushwick (c05)

## Pending margit referrals (b01c06-specific)
  - SEAM-006 oc-ward-coverage-notes.card.md (prop card; first-touch @6; priority before stitch)
  - SEAM-007 oc-jarvis-channel-form.card.md (prop card; first-touch @11; priority before stitch)
  - SEAM-008 oc-accounting-ledger.card.md (prop card; first-touch @16; priority before stitch)

## State-updates-env locked (b01c06) — 17 entries (1 cull)
  state:1  @1  — studio.spatial_layout.lane-mouth: clear -> handcart-blocking
  state:2  @6  — prop:oc-ward-coverage-notes.state: closed -> open (oc field-extension; SEAM-006)
  state:3  @7  — prop:oc-ward-coverage-notes.contact-role-field: blank -> ward-resident-hook-routine
  state:4  @9  — prop:oc-ward-coverage-notes.state: open -> closed
  state:5  @10 — prop:oc-jarvis-channel-form.state: absent -> arrived (oc field-extension; SEAM-007)
  state:6  @11 — prop:oc-jarvis-channel-form.state: arrived -> opened
  state:7  @14 — prop:oc-jarvis-channel-form.content: blank -> filled-four-ward-elder-names
  state:8  @15 — prop:oc-jarvis-channel-form.position: in-hand -> set-down-unsent
  state:9  @16 — prop:oc-accounting-ledger.state: closed -> open (oc field-extension; SEAM-008)
  state:10 @17 — prop:oc-accounting-ledger.content: blank-entry -> ward-elder-names-written
  state:11 @18 — prop:oc-accounting-ledger.content: ward-elder-names-written -> ward-elder-names-and-sera-coverage-written
  state:12 @21 — prop:oc-accounting-ledger.state: open -> closed
  state:13 @22 — prop:oc-jarvis-channel-form.position: set-down-unsent -> in-hand
  state:14 @23 — prop:oc-jarvis-channel-form.state: filled -> sealed
  state:15 @24 — prop:oc-jarvis-channel-form.holder: taylor-hebert-kl-122ac -> the-courier
  state:16 @25 — prop:oc-ward-coverage-notes.state: closed -> open
  state:17 @26 — prop:oc-ward-coverage-notes.state: open -> closed
  Cull (authoring phase): 1 entry removed (@19 marks-red-keep-coverage-record — frugality CULL: third consecutive content-write to prop:oc-accounting-ledger within @16-@21 sequence; strip test passes (content already progressed at @17+@18 which cover both accounting arms per scene-map peak-shadow-bones); density-on-flat anti-pattern if included; culled as weakest of the three ledger content-writes)
  Density: 17/26 = 65.4% (above rubric band; defended — this is the chapter's accounting/delivery sequence; all three major props first-touched this chapter; all entries strip-test clean; field-mutation-dense by design because prop-state IS the substance delivery mechanism for this chapter)

## Prop state at b01c06 chapter-close
  - prop:oc-ward-coverage-notes: state=closed (@26); contact-role-field=ward-resident-hook-routine; contact-source-field=blank-by-choice (not tracked — blank→blank no state change per rubric)
  - prop:oc-jarvis-channel-form: state=sealed (@23); holder=the-courier (@24); position=with-courier; content=filled-four-ward-elder-names
  - prop:oc-accounting-ledger: state=closed (@21); content=ward-elder-names-and-sera-coverage-written
  - studio.spatial_layout.lane-mouth: handcart-blocking (set @1; not resolved on-page this chapter)

  State-updates-env R1 authored 2026-05-31 — theater/facets/state-updates-env.md (17 entries)
  _inflight: theater/facets/_inflight/proto-lines-state-env.md filed

## Sensory facet filed (b01c06) — 3 entries
  sensory:1 @2  — pressure: lane-passable-morning-flow -> crowd-backed-body-compression (up)
  sensory:2 @17 — sound: drain-water-trickle-ambient -> stylus-on-board-rhythm (up)
  sensory:3 @20 — sound: stylus-on-board-rhythm -> silence (drop)
  Density: 3/26 = 11.5% (above standard 6% ceiling; above 7.7% short-chapter advisory; defended — modality floor requires ≥2; @17+@20 are a coherent paired inflection (up/drop) anchored to each other; @2 pressure is the only clean non-sound fire available in the chapter; see rubric-carve-out preamble in sensory-b01-c06.md re @2 old-state sourcing)
  Modalities: pressure + sound (2; meets ≥2 floor)
  Per-scene cap check: scene-A=1 (@2), scene-B=0, scene-C=2 (@17+@20) — all within ≤3 cap
  Old-state anchor check: sensory:1 old-state sourced from location card §Hazards baseline (documented carve-out); sensory:2 old-state from loc-state:2 @5 sensory vocabulary (drain-water-trickle per location card oc-stitch-house-lane); sensory:3 old-state from sensory:2 new-state (stylus-on-board-rhythm → paired drop)
  Cull: 0 entries removed post-cull (all 3 survive four-axis rubric check)
  SEAM-009: @2 pressure old-state anchor sourced from location card rather than loc-state entry — rubric-carve-out preamble documents the justification; flagged for R2 reviewer attention
  Files: theater/facets/sensory-b01-c06.md (facet) + theater/facets/_inflight/proto-lines-sensory-b01-c06.md (inflight)
