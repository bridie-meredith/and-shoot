# studio state

episode: b01c13
last_updated: 2026-06-03
action: state-updates-env R1 authoring — /and-facets b01-c13 Phase 1

## Location-state sequence locked (b01c13) — 7 entries, 0 cull
  loc-state:1 @1  — the-hook-upper-provisioning | morning | none | loading-platform-open | crate-ledge at the platform edge (place-anchor; scene-A; Thursday mid-morning)
  loc-state:2 @2  — the-hook-upper-provisioning | morning | none | trestle-table-active, household-agent-posted | trestle-table where agent stands (state-change: apparatus-component takes position)
  loc-state:3 @10 — the-magistrate-hall | morning | none | rented-back-room-active, ceiling-corner-above | ceiling-corner of the chandler's rented back room (place-anchor; scene-B; four days later)
  loc-state:4 @11 — the-magistrate-hall | morning | none | document-at-table-edge, clerk-posted | table edge where clerk placed the list-output before proceedings (state-change: apparatus-component takes position)
  loc-state:5 @19 — the-hook-lane | evening | none | lane-open, circuit-mid | lane Taylor walks on ordinary circuit (place-anchor; scene-C; that evening)
  loc-state:6 @24 — the-hook-lower-water-trough | afternoon | none | trough-open | water-trough at lower Hook where chandler's row meets fishmongery open-space (place-anchor; scene-D; two days later)
  loc-state:7 @29 — the-hook-lower-water-trough | afternoon | none | trough-behind, lane-open-ahead | lane-mouth past trough's edge — threshold crossed mid-speech (state-change: Taylor departs while Halvard still speaking)
  Continuity-carry: none filed — scene-A (low-heat establishment / fusion-run @1-@2 fully covered by entries 1+2); scene-B (rising / excluded); scene-C fusion-run @21-@22 only 2 bones (below 3-bone floor; excluded); scene-D fusion-run @24-@25 only 2 bones (excluded); scene-D rhythm-shape held-breath-enactment (not flat-low/resolving/release-only)
  Cull: 0 entries removed — all 7 survive strip / pointing / frugality / previous-entry tests

## Current set (b01c13 chapter-close)
  location: the-hook-lower-water-trough (Taylor departed; Halvard still present)
  time_of_day: afternoon
  weather: none
  ambient_conditions:
    - trough open at lower Hook (chandler's row / fishmongery open-space junction)
    - Taylor departed mid-speech (@29; walked the route @30)
    - Halvard still at trough filling water-skin (@31)

## Location-state R1 authored (b01c13) — 2026-06-03
  theater/facets/location-state-b01-c13.md (7 entries, 0 cull)
  _inflight: theater/facets/_inflight/proto-lines-loc-state.md filed (citations @1, @2, @10, @11, @19, @24, @29)

## Seams flagged for R2 (b01c13)
  SEAM-C13-LOC-001: the-hook-upper-provisioning — new slug; no confirmed warehouse card; drawn from bones `locations:` field. R2 reviewer confirm slug canonicalization or flag for margit.
  SEAM-C13-LOC-002: the-magistrate-hall — new slug; no confirmed warehouse card; drawn from bones `locations:` field. Scene-map describes as "rented back room of a chandler's house." R2 confirm slug or flag for margit.
  SEAM-C13-LOC-003: the-hook-lane — new slug; no confirmed warehouse card; this is the familiar lane Taylor walks as ordinary circuit (distinct from oc-hook-precinct / the-hook-ward slug family used in prior chapters). R2 confirm whether this should canonicalize to oc-hook-precinct or remain a distinct slug.
  SEAM-C13-LOC-004: the-hook-lower-water-trough — new slug; no confirmed warehouse card; lower end of the Hook at chandler's row / fishmongery junction. R2 confirm slug or flag for margit.
  SEAM-C13-LOC-005: time-of-day for scene-D set as "afternoon" by inference from "ordinary circuit" / water-carrying context. Scene-map says "two days later" with no explicit time named. R2 confirm or adjust if bones-review establishes a different time.

## State-updates-env locked (b01c13) — 13 entries, 1 cull
  state:1  @1  — studio.time_of_day: end-of-day -> mid-morning
  state:2  @1  — studio.location: the-feed-station -> the-hook-upper-provisioning
  state:3  @7  — prop:oc-fish-account-ledger.condition: open -> closed
  state:4  @10 — studio.time_of_day: mid-morning -> morning
  state:5  @10 — studio.location: the-hook-upper-provisioning -> the-magistrate-hall
  state:6  @11 — prop:oc-d06-document.holder: green-apparatus-possession -> table-surface
  state:7  @13 — prop:oc-procedural-form.condition: blank -> inscribed
  state:8  @15 — prop:oc-d06-document.holder: table-surface -> magistrate-hand
  state:9  @19 — studio.time_of_day: morning -> evening
  state:10 @19 — studio.location: the-magistrate-hall -> the-hook-lane
  state:11 @24 — studio.time_of_day: evening -> morning
  state:12 @24 — studio.location: the-hook-lane -> the-hook-lower-water-trough
  state:13 @31 — prop:oc-water-skin.condition: empty -> filled
  Cull (1 entry removed): @8 prop:oc-empty-crate (first-touch; no downstream canonical relevance; @7 fish-account-close captures transaction canonical state; crate-pickup is physical-correlate of already-recorded close)
  Decisions-not-fire: @2/@3/@4/@5/@6 (approach/tally-in-progress; no persistent field-changes until @7); @9 (actor-fork / fauna-sense domain); @12 (actor-fork; no prop change distinct from scene-B state); @14 (held-against-turn: immediately adjacent to peak @15; cord-holder-change REJECT); @16/@17/@18 (actor-fork / posture; no studio/prop field change); @20 (tallow-smoke ambient transient — sensory territory, not tracked field); @21/@22/@23 (scene-C interior; lane unchanged before/after; no env/prop changes); @25/@26/@27/@28/@29/@30 (actor-state + dialogue; water-trough is environmental fixture = location-card content, not state-update)
  Field-extensions (4 new oc-props / new fields; margit referrals needed):
    prop:oc-fish-account-ledger.condition (opposing-force accounting ledger; no prior warehouse card)
    prop:oc-d06-document.holder (the Taylor-delivered ward-elder list; no prior prop state entry)
    prop:oc-procedural-form.condition (magistrate's verdict form; scene-local prop; no prior card)
    prop:oc-water-skin.condition (halvard's water-carrying vessel; no prior prop state entry)
  Density: 13/31 = 42%; above s01e01 mechanical band (8-18%) but justified by 4×(location + time-of-day) = 8 structural scene-transition fires + 5 prop fires (peak-bone and peak-shadow co-citations); b01c12 precedent 38%; b01c11 precedent 52%
  State-updates-env R1 authored 2026-06-03 — theater/facets/state-updates-env-b01-c13.md (13 entries)
  _inflight: theater/facets/_inflight/proto-lines-state-env.md filed (citations @1×2, @7, @10×2, @11, @13, @15, @19×2, @24×2, @31)

## Prop state at b01c13 chapter-close (projected from state-updates-env R1)
  - studio.time_of_day: morning (@11; scene-D; persistent at chapter-close — no further time advance recorded)
  - studio.location: the-hook-lower-water-trough (@12; chapter-close location; Taylor departed @29)
  - prop:oc-fish-account-ledger.condition: closed (@3; permanent; Green-faction transaction archived)
  - prop:oc-d06-document.holder: magistrate-hand (@8; persistent — document not returned to table in any subsequent bone; chapter-close state)
  - prop:oc-procedural-form.condition: inscribed (@7; irreversible; verdict pre-inscribed)
  - prop:oc-water-skin.condition: filled (@13; persistent; Halvard carries filled skin after chapter-close)
  - All b01c12 carry-forward entries unchanged: studio.time_of_day reset at @1; studio.fauna_sense_status.coverage-scale: five-ward-plus-approaches; prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-plus-south-plus-both-clusters; feed-ledger entries (gap/anchor/breach-column all closed/permanent); studio.spatial_layout.lane-junction-patrol: Gold-Cloak-pair-posted; studio.fauna_sense_status.lower-gate-road-coverage: corwick-absent

## Seams flagged for R2 (b01c13 state-updates-env)
  SEAM-C13-ENV-001: prop:oc-d06-document.holder old-state "green-apparatus-possession" is inferred (delivered to Jarvis at d06; no prior explicit state-update entry on this prop); R2 confirm adequacy or trace to prior chapter delivery bone
  SEAM-C13-ENV-002: studio.time_of_day @10 old-state "morning" — scene-B has no explicit time-of-day in scene-map ("four days later"); value inferred from proceeding context; carve-out preamble in facet file applies; R2 confirm or revise
  SEAM-C13-ENV-003: studio.time_of_day @24 old-state "morning" — scene-D has no explicit time-of-day in scene-map ("two days later"); value inferred from circuit-walk context; carve-out preamble in facet file applies; R2 confirm or revise; note: scene-D location-state fires "afternoon" (SEAM-C13-LOC-005) — R2 must reconcile state-updates-env @24 vs location-state if both fire time-of-day on the same bone
  SEAM-C13-ENV-004: prop:oc-procedural-form.condition — form inscribed at @13; confirm form does not exit the scene in a changed condition requiring a follow-up entry (magistrate's handling post-@15 not explicitly boned)
  SEAM-C13-ENV-005: cross-facet consistency — location-state:6 @24 fires "afternoon" as time-of-day annotation; state-updates-env state:11 @24 fires "morning" as the new-state for studio.time_of_day; these values must be reconciled at R2 cross-facet consistency pass

## Prior set state (b01c12 chapter-close)

## Location-state sequence locked (b01c12) — 8 entries, 0 cull
  loc-state:1 @1  — the-hook-ward | morning | none | lane-mouth-open, overhang-geometry-active | overhang-joints at lane-mouth (place-anchor; morning circuit open)
  loc-state:2 @3  — the-hook-ward | morning | none | gate-tower-shadow-west, rendering-yard-wall-east | gate-tower shadow thrown west across the lane (body placed inside gap's west boundary)
  loc-state:3 @8  — the-feed-station | morning | none | ledger-surface-open, stylus-lifted | ledger surface at the station (sub-anchor; body moved from lane circuit to accounting surface)
  loc-state:4 @11 — the-feed-station | morning | none | ledger-surface-open, packet-at-surface-edge | station surface edge where packet lands (state-change: Jarvis/opposing-force arrives)
  loc-state:5 @17 — the-feed-station | midday | none | ledger-surface-open, gap-column-pending | ledger surface at midday (time-advance: morning → midday; refusal sit-down begins)
  loc-state:6 @23 — the-feed-station | midday | none | ledger-surface-clear, sealed-packet-departing | station surface edge as sealed packet is taken (state-change: Jarvis exits, withholding in motion)
  loc-state:7 @29 — the-feed-station | afternoon | none | ledger-surface-open, muddy-way-extension-in-motion | ledger surface late-afternoon as fifth-ward cluster extends (time-advance: midday → afternoon; muddy-way first enters feed)
  loc-state:8 @42 — the-feed-station | end-of-day | none | breach-column-receiving, accounting-closed | breach column at accounting-close (time-advance: afternoon → end-of-day; threshold entry filed in flat register)
  Continuity-carry: none filed — scene-D rhythm-shape is rising-to-interior-climax (excluded from license); no flat-low/resolving/release-only runs applicable
  Cull: 0 entries removed — all 8 survive strip / pointing / frugality / previous-entry tests

## Current set (b01c12 chapter-close)
  location: the-feed-station (accounting closed)
  time_of_day: end-of-day
  weather: none
  ambient_conditions:
    - breach-column entry filed (cost recorded; architecture-entry closed)
    - feed-station surface: accounting closed, ledger at rest
    - all five wards + Flea Bottom approaches in feed at full-circuit density (new threshold state from @31)
    - muddy-way ward-cluster: active (new from @29)

## Location-state R1 authored (b01c12) — 2026-06-03
  theater/facets/location-state-b01-c12.md (8 entries, 0 cull)
  _inflight: theater/facets/_inflight/proto-lines-loc-state.md filed (citations @1, @3, @8, @11, @17, @23, @29, @42)

## Seams flagged for R2 (b01c12)
  SEAM-C12-LOC-001: the-hook-ward slug used for east-water-gate lanes (@1, @2, @3); prior chapters used `oc-hook-precinct` for the lane-south entry — R2 reviewer should confirm slug consistency or flag for margit canonicalization (carry from SEAM-C11-LOC-004)
  SEAM-C12-LOC-002: @6 `insects return the stitch-house route` — mediated feed-perception beat; no loc-state fired (rejected as perception/feed beat, not Taylor's physical transition); R2 confirm the inherited env from @3 is sufficient for Wren-as-boundary rendering
  SEAM-C12-LOC-003: @8 sub-anchor for feed-station — prior b01c11 loc-state sequencing puts Taylor at the feed-station throughout; b01c12 scene-A starts in the lanes and moves to the feed-station; @8 stylus-lift is the first explicit ledger-surface beat; no prior state-update records the lane→station transition; R2 confirm the sub-anchor is adequate or whether a explicit entry at @3→@8 transition gap is needed
  SEAM-C12-LOC-004: the-feed-station warehouse card still unconfirmed (carry from SEAM-C11-LOC-001; b01c12 fires 6 entries on this slug)

## Prior set state (b01c11 chapter-close)
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

## State-updates-env locked (b01c12) — 16 entries, decisions-not-fire documented
  state:1  @1  — studio.time_of_day: end-of-day -> morning
  state:2  @9  — prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-plus-south -> hook-rushwick-oswyn-plus-south-plus-northern-cluster-1
  state:3  @11 — prop:oc-jarvis-packet.holder: jarvis-coin-kl-courier -> station-surface
  state:4  @12 — prop:oc-jarvis-packet.seal-condition: sealed -> broken
  state:5  @13 — prop:oc-jarvis-packet.physical-condition: folded-closed -> covering-sheet-open
  state:6  @17 — studio.time_of_day: morning -> midday
  state:7  @19 — prop:oc-feed-ledger.gap-column-entry: absent -> boundary-refusal-written
  state:8  @22 — prop:oc-feed-ledger.gap-column-entry: boundary-refusal-written -> closed
  state:9  @23 — prop:oc-jarvis-packet.holder: station-surface -> jarvis-coin-kl-courier
  state:10 @26 — prop:oc-feed-ledger.anchor-column-entry: absent -> settlement-written
  state:11 @27 — prop:oc-feed-ledger.anchor-column-entry: settlement-written -> closed
  state:12 @29 — studio.time_of_day: midday -> late-afternoon
  state:13 @30 — prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-plus-south-plus-northern-cluster-1 -> hook-rushwick-oswyn-plus-south-plus-both-clusters
  state:14 @32 — studio.fauna_sense_status.coverage-scale: partial-multi-ward -> five-ward-plus-approaches
  state:15 @42 — prop:oc-feed-ledger.breach-column-entry: absent -> threshold-filed
  state:16 @42 — studio.time_of_day: late-afternoon -> end-of-day
  Decisions-not-fire: @2 (fauna motion / registration not state), @3 (actor-fork gate-tower shadow), @4-@5 (map-closes = perception/recognition, gap excludes not adds), @6-@7 (feed/map read — registration, actor-fork), @8 (actor-fork motor), @10 (water-gate ledger entry — low-stakes archival, culled for density), @14 (covering-sheet-turned — fine-grain continuation of @13 state; culled), @15 (packet set — holder returns to station-surface but actor is the agent; transient cycle), @16 (stylus set — actor-fork), @17 (actor-fork takes stylus), @18 (gap-column open — collapsed into @19 first-touch entry; no separate column-open/close fired), @20-@21 (actor-fork holds-hand / stylus-lifts), @24 (gap-column close — column-open not fired so no old-state for close; entries @19/@22 cover the entry-lifecycle), @25 (anchor-column open — collapsed into @26 first-touch entry), @28 (actor-fork lifts hand), @29 (actor-fork extends cluster; content fires at @30 completion), @31 (fifth-ward-circuit ledger — coverage-scale @32 carries the state), @33-@37 (accounting-traversal — transient/held-against-turn; no persistent field-flips), @38-@39 (interior event / actor-fork suppression), @40 (architecture-entry — coverage-notes @13/@30 + coverage-scale @32 carry the state; ledger echo culled), @41 (full-circuit-count — subsumed by @42 breach-column; culled for density)
  Field-extensions (6 new fields): prop:oc-feed-ledger.gap-column-entry (new); prop:oc-feed-ledger.anchor-column-entry (new); prop:oc-feed-ledger.breach-column-entry (new); studio.fauna_sense_status.coverage-scale (new sub-field); prop:oc-jarvis-packet.physical-condition first-use on c12 incoming packet (parallel to c09 field-extension); prop:oc-ward-coverage-notes.content extended values (two new value states: northern-cluster-1 added, then both-clusters)
  Margit referrals pending: oc-feed-ledger schema extension (3 new fields + carry from b01c11 8-field extension); oc-ward-coverage-notes content-value canonicalization; oc-jarvis-packet.card.md (carry from b01c09)
  Density: 16/42 = 38%; above the mechanical s01e01 band (8-18%) but justified by 4 time-of-day transitions + 2 coverage-extension events + 2 ledger arcs (4 peak-bones) + 1 five-ward threshold; b01c11 precedent 14/27 = 52%
  State-updates-env R1 authored 2026-06-03 — theater/facets/state-updates-env-b01-c12.md (16 entries)
  _inflight: theater/facets/_inflight/proto-lines-state-env.md filed (citations @1, @9, @11, @12, @13, @17, @19, @22, @23, @26, @27, @29, @30, @32, @42 x2)

## Prop state at b01c12 chapter-close (projected from state-updates-env R1)
  - studio.time_of_day: end-of-day (@16; chapter-close)
  - studio.fauna_sense_status.coverage-scale: five-ward-plus-approaches (@14; first-touch; persistent into downstream chapters)
  - prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-plus-south-plus-both-clusters (@13; persistent)
  - prop:oc-jarvis-packet.holder: jarvis-coin-kl-courier (@9; departed with refusal-response; persistent-out)
  - prop:oc-jarvis-packet.seal-condition: broken (@4; b01c12 incoming packet; irrecoverable)
  - prop:oc-jarvis-packet.physical-condition: covering-sheet-open (@5; b01c12 incoming packet; read-state at chapter-open; note the packet departs @23 with Jarvis, so this physical-condition is on the chapter-close-departed packet)
  - prop:oc-feed-ledger.gap-column-entry: closed (@8; permanent; refusal archived in the ledger)
  - prop:oc-feed-ledger.anchor-column-entry: closed (@11; permanent; cl-d06 settlement archived)
  - prop:oc-feed-ledger.breach-column-entry: threshold-filed (@15; permanent; Khepri-cost recorded)
  - prop:oc-soap-lane-report-packet.physical-condition: sealed (carry from b01c11 state:8; no c12 state-update fired)
  - prop:oc-soap-lane-report-packet.holder: taylor-hebert-kl-122ac (carry from b01c11 state:6; no c12 departure bone)
  - All b01c10-carry entries unchanged: studio.spatial_layout.lane-junction-patrol: Gold-Cloak-pair-posted; studio.fauna_sense_status.lower-gate-road-coverage: corwick-absent; prop:oc-feed-record.corwick-entry: persisting-post-closure

## Seams flagged for R2 (b01c12 state-updates-env)
  SEAM-C12-ENV-001: prop:oc-jarvis-packet.seal-condition old-state "sealed" — inferred from delivery convention and b01c09 state:3 lifecycle (prior packets sealed before delivery); no explicit b01c11/c12 upstream seal-state entry on this specific packet; R2 confirm adequacy
  SEAM-C12-ENV-002: prop:oc-ward-coverage-notes.content prior-value abbreviation — "hook-rushwick-oswyn-plus-south" abbreviates the b01c09 state:1 canonical value ("hook-rushwick-oswyn-corridors-plus-south-extension"); showrunner must reconcile at write-back (both refer to the same state)
  SEAM-C12-ENV-003: prop:oc-jarvis-packet physical-condition @5 (covering-sheet-open) — this applies to the b01c12 INCOMING packet read by Taylor; the packet departs at @23 with this state still "covering-sheet-open" (Taylor read it but did not re-fold it); showrunner should note at write-back that the departed packet is in covering-sheet-open state, carried out by Jarvis
  SEAM-C12-ENV-004: two entries on @42 (breach-column-entry + time_of_day) — both distinct targets; no frugality conflict; confirmed licit per rubric
