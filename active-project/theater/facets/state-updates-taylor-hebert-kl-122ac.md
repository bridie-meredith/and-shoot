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
#   - actor:taylor-hebert-kl-122ac.knowledge.wren-in-coverage-map      (new) — tracks anchor-discipline canonical state: wren's presence in feed coverage (registration fact)
#   - actor:taylor-hebert-kl-122ac.knowledge.wren-report-inclusion      (new) — tracks anchor-discipline canonical state: whether wren is included in the patron report (decision fact; separable from registration; load-bearing for d14)
#   - actor:taylor-hebert-kl-122ac.knowledge.intelligence-routing-state (new) — tracks first-upward-routing operational state
#   - actor:taylor-hebert-kl-122ac.stats.capability_axis: existing integer field on state.md; mutates here at axis_move bones flat 15 and flat 27.
#   All field-extensions are tracked-state aspects propagated by chapter handoff_out (memory.md chapters[b01c04].handoff_out.character_state /
#   open_threads); NOT perception/mood/register.
#
# Cross-facet co-citation expectations (POV-restriction rule §"Cross-facet contract"):
#   Every actor:taylor-hebert-kl-122ac.* entry below REQUIRES a narrator-interest co-citation on the same @<anchor>.
#   Flagged at end-of-file under "Flagged seams" for cross-facet review.

1 @9 actor:taylor-hebert-kl-122ac.stats.position_in_kl: smallfolk-anonymous -> named-conduit-at-courier-tier
2 @9 actor:taylor-hebert-kl-122ac.knowledge.arrangement-state: licensed-exception-considered -> licensed-exception-active
3 @15 actor:taylor-hebert-kl-122ac.stats.capability_axis: 2 -> 3
4 @18 actor:taylor-hebert-kl-122ac.knowledge.oswyn-as-unknowing-coverage-node: absent -> present
5 @22 actor:taylor-hebert-kl-122ac.knowledge.wren-in-coverage-map: absent -> present-but-outside-report
6 @27 actor:taylor-hebert-kl-122ac.stats.capability_axis: 3 -> 4
7 @31 actor:taylor-hebert-kl-122ac.knowledge.intelligence-routing-state: dormant -> routing-to-jarvis-active

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
