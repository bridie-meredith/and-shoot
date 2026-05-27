---
facet: state-updates
sources: [env, jarvis-coin-kl-courier, taylor-hebert-kl-122ac]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
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

# source: jarvis-coin-kl-courier
facet: state-updates
episode: b01c04
author: impersonator:jarvis-coin-kl-courier
slice: actor:jarvis-coin-kl-courier.*
---

# rubric-carve-out — none; baseline V2 rubric § actor-state applies.
#
# Field-extensions (per §"Field-extension protocol" of rubric-state-updates.md):
#   - actor:jarvis-coin-kl-courier.stats.active_deliveries (new) — integer counter tracking live
#       delivery assignments in-progress; operational load indicator; not a standard actor-state
#       field on jarvis-coin-kl-courier's state.md baseline; field-extension justified as a
#       tracked-state-aspect (irreversible increment at each accept-delivery event; persistence
#       required for downstream chapter continuity); NOT perception/mood/register.
#   - actor:jarvis-coin-kl-courier.stats.exposure_risk (new) — categorical risk tier tracking
#       operational exposure level for the courier once he physically carries Taylor's intelligence;
#       field-extension justified as a tracked-state-aspect (latent → operational flip is an
#       irreversible canonical state change that chapter handoff_out must propagate); NOT perception/
#       mood/register.
#   Both field-extensions are propagated by chapter handoff_out (memory.md chapters[b01c04].
#   handoff_out.character_state / open_threads) per the standard field-extension protocol.

15 @5 actor:jarvis-coin-kl-courier.location: lower-city-in-transit -> cooper-yard-eel-alley-lane-mouth
16 @9 actor:jarvis-coin-kl-courier.stats.active_deliveries: 0 -> 1
17 @11 actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley-lane-mouth -> lower-city-in-transit
18 @29 actor:jarvis-coin-kl-courier.location: lower-city-in-transit -> cooper-yard-eel-alley
19 @29 actor:jarvis-coin-kl-courier.inventory: [] -> [otto-confirmation-note]
20 @32 actor:jarvis-coin-kl-courier.inventory: [otto-confirmation-note] -> [otto-confirmation-note, taylor-movement-pattern-report]
21 @36 actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley -> lower-city-in-transit
22 @36 actor:jarvis-coin-kl-courier.stats.exposure_risk: latent -> operational

# source: taylor-hebert-kl-122ac
facet: state-updates
episode: b01-c04
author: dialogue-writer-fork:taylor-hebert-kl-122ac
slice: actor:taylor-hebert-kl-122ac only
---

# Slice contract:
#   - This file authors actor:taylor-hebert-kl-122ac.* entries ONLY (POV-character actor-state).
#   - studio.* and prop:* entries authored by studio in a separate slice.
#   - Non-POV actor:* entries (jarvis-coin-kl-courier, oswyn-mudway-flea-bottom-elder,
#     wren-stitch-maker-flea-bottom-ward) authored by their own forks in separate slices.
#   - To be merged at Phase 2 consolidation into facets/state-updates-b01-c04.md.
#
# Field-extensions (per §"Field-extension protocol" of rubric-state-updates.md):
#   - actor:taylor-hebert-kl-122ac.knowledge.arrangement-state         (new) — tracks moral_framework state-character within rank 1
#   - actor:taylor-hebert-kl-122ac.knowledge.oswyn-as-unknowing-coverage-node  (new) — tracks routing-architecture named-human entries
#   - actor:taylor-hebert-kl-122ac.knowledge.wren-in-coverage-map      (new) — tracks anchor-discipline canonical state (load-bearing for d14)
#   - actor:taylor-hebert-kl-122ac.knowledge.intelligence-routing-state (new) — tracks first-upward-routing operational state
#   - actor:taylor-hebert-kl-122ac.stats.capability_axis: existing integer field on state.md; mutates here at axis_move bones flat 15 and flat 27.
#   All field-extensions are tracked-state aspects propagated by chapter handoff_out (memory.md chapters[b01c04].handoff_out.character_state /
#   open_threads); NOT perception/mood/register.
#
# Cross-facet co-citation expectations (POV-restriction rule §"Cross-facet contract"):
#   Every actor:taylor-hebert-kl-122ac.* entry below REQUIRES a narrator-interest co-citation on the same @<anchor>.
#   Flagged at end-of-file under "Flagged seams" for cross-facet review.

23 @9 actor:taylor-hebert-kl-122ac.stats.position_in_kl: smallfolk-anonymous -> named-conduit-at-courier-tier
24 @9 actor:taylor-hebert-kl-122ac.knowledge.arrangement-state: licensed-exception-considered -> licensed-exception-active
25 @15 actor:taylor-hebert-kl-122ac.stats.capability_axis: 2 -> 3
26 @18 actor:taylor-hebert-kl-122ac.knowledge.oswyn-as-unknowing-coverage-node: absent -> present
27 @22 actor:taylor-hebert-kl-122ac.knowledge.wren-in-coverage-map: absent -> present-but-outside-report
28 @27 actor:taylor-hebert-kl-122ac.stats.capability_axis: 3 -> 4
29 @31 actor:taylor-hebert-kl-122ac.knowledge.intelligence-routing-state: dormant -> routing-to-jarvis-active

# Cull-log (delete-only per facet schema; one pass):
#   Pre-cull set: 13 candidate entries. Post-cull: 7 entries. 6 deletions.
#   DEL @3  actor:taylor.location: hook-district -> oc-cooper-yard-eel-alley
#           — location-tracking density-on-flat risk; chapter has 5 entrance bones; not load-bearing irreversible registration.
#             Studio location-state facet carries the environment-frame; actor.location reverts to studio's tracking.
#   DEL @14 actor:taylor.location: oc-cooper-yard-eel-alley -> oc-pig-tallow-lane         (same reason)
#   DEL @26 actor:taylor.location: oc-pig-tallow-lane -> oc-ropers-court                  (same reason)
#   DEL @15 actor:taylor.stats.coverage_wards: hook -> hook+pig-tallow-lane               — invented field; capability_axis numeric carries
#           the canonical state; coverage-set extension breaks bone-level magnitude anchoring (the second-ward jump at @22 is
#           a peak-shadow registration, not a magnitude-bearing bone). Conservative refusal per Field-extension protocol.
#   DEL @27 actor:taylor.stats.coverage_wards: ... -> hook+...+ropers-court               (same reason)
#   DEL @31 actor:taylor.knowledge.arrangement-state: licensed-exception-active -> licensed-exception-running-as-routine
#           — within-rank polish duplicates the @31 intelligence-routing-state flip; routing-state IS the form
#             running-as-routine takes. Parasitic against the strip-test (the operational flip carries the canonical change).
#
# Skip-correct (no fire; rubric defense):
#   SKIP @7  speech-acceptance bone carries social_tether-antag +1.0 — Otto's lever, Otto-fork's authority (cross-POV).
#            Taylor's interior crossing at @7 is captured by the @9 entries (peak-bone, position_in_kl + arrangement-state).
#   SKIP @8  body-stillness bone "holds the feet" — peak-shadow registration; moral_framework axis HELD at scene-level;
#            posture-as-state would need multi-beat persistence load-bearing on the next move that the @9 position-flip
#            does not already carry.
#   SKIP @23 "holds the feet" at second-ward junction — held-against-turn class (rising zone immediately adjacent to peak-bone @22 / @24
#            cluster); rubric explicitly forbids canonical state-update co-citation. Wren-anchor-discipline registers
#            via @22 perception-flip, not the @23 not-walking posture.
#   SKIP @28 "runs the four-ward feed" — operational enactment of the @27 capability-axis flip; strip-test fails (field
#            still at <new> at next beat regardless of this entry).
#   SKIP @36 jarvis-coin-kl-courier exits with the report — substance_delta carries position-world +1.0, which is world-axis
#            (Green-faction consolidation), not Taylor's actor-state. The world-axis flip is studio's authority via
#            studio.position_world or environment-frame tracking.
#   SKIP @37 "runs the ward-feed" — same enactment-after-flip class as @28.
#   SKIP @38 insect-feed returns wren — second-fire on the @22 knowledge-flip; field already at <new>.
#   SKIP @39 chapter-close exit — trail-bone; not a canonical irreversible flip on Taylor.

# Flagged seams (cross-facet review at consolidation):
#   SEAM-NI-CO-CITATION  All 7 entries above require narrator-interest co-citation on the same @<anchor>.
#                        Specifically: NI MUST fire at @9, @15, @18, @22, @27, @31.
#                        Absence of any of these in narrator-interest is REJECT per §Cross-facet contract (POV actor-state).
#   SEAM-PEAK-BONE-9     @9 is a peak-bone (per scene-map-b01-c04.md scene-A); two state-updates co-cite (position + arrangement-state).
#                        Strong-expect satisfied; cross-facet test should confirm.
#   SEAM-PEAK-BONE-18    @18 is a peak-bone (scene-B); oswyn-as-unknowing-coverage-node co-cites. Strong-expect satisfied.
#   SEAM-PEAK-BONE-36    @36 is a peak-bone (scene-C) but Taylor slice DOES NOT fire (world-axis, not actor-state).
#                        Studio slice expected to fire here on prop:report-sheet.holder or studio.position_world.
#                        If neither studio nor any actor fork fires @36, cross-facet review flag — peak-bone with no
#                        state-update support.
#   SEAM-FIELD-EXTENSIONS All four knowledge-* fields are extensions. Margit referral may be appropriate if these recur across
#                        b01c05+. For now, declared inline per §"Field-extension protocol".
#   SEAM-CAPABILITY-RANK Chapter contract sums capability +2.0 across c04 (target_delta_magnitude); bone-level fires at @15 (+1.0)
#                        and @27 (+1.0) = +2.0 EXACT. The +0.5 nudge to chapter handoff_out rank 4.5 is downstream-rendered,
#                        not bone-anchored — consistent with substance_delta_measured.
#   SEAM-WREN-ANCHOR-DISCIPLINE  @22 entry (knowledge.wren-in-coverage-map) is the chapter's load-bearing future-cost-collateral
#                        plant per chapter goal. Cross-facet expectation: narrator-interest @22 + memory @22 (Wren callback to
#                        b01c01s03 + b01c03 anchor-status) + feeling @23 (somatic tell of not-walking). State-update slice
#                        carries the canonical write-back; downstream facets carry the interior load.
