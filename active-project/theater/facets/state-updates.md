---
facet: state-updates
sources: [env, taylor-hebert-kl-122ac]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates
slice: env
episode: b01c02
author: studio
---

# rubric-carve-out — sparse-fire defended: one env field-flip; near-zero prop activity; no physical prop cards in chapter
#
# design/shoot-v2/rubric-state-updates.md § "What state-updates is for" + § "Curve-shape rubric"
#
# Carve-out scope: 28 of 29 bones (all except @20)
# Carve-out rule: 1 entry on 29 bones (3.4%) is below the rubric's 8-18% density band. This is a
#   floor-defended sparse-fire, not a calibration failure. "Inflating fires to hit density without
#   each fire passing all three axes is the prohibited move." The chapter is almost entirely
#   interior-accounting and insect-feed mechanism — no physical environment fields flip except
#   the time_of_day transition at scene-C open (@20).
# Coverage justification:
#   Location: oc-stitch-house-lane throughout all three scenes. studio.active_location does not
#   flip — no location transition occurs.
#   Time-of-day: the chapter opens at dawn (b01c01 handoff_out baseline). Scene-A (@1-@9) is
#   dawn-to-day; Taylor leaves the drain angle and moves into the ward. No single bone in scene-A
#   carries a clean time_of_day field-flip — departure from the drain angle (@1) is Taylor's
#   actor-state position change, not a time-of-day event. Scene-B (@10-@19) is labeled
#   "days-of-coverage" in the scene-map: a multi-day compressed montage. No single beat in the
#   montage marks a persistent, discrete time_of_day state flip — the montage is the elapsed
#   time, not an event within a clock-frame. Scene-C (@20-@29) is labeled "end-of-day": Taylor
#   returns to the drain angle, which is her nighttime anchor position. @20 is the one bone
#   where studio.time_of_day genuinely flips from its last canonical value (dawn / day-sweep)
#   to end-of-day, and that state persists through the remaining 9 bones of the chapter close.
#   Persistence test: the field stays at end-of-day through @29 (no further time-flip in the
#   chapter). Strip test: without this entry, the canonical studio.time_of_day would remain in
#   the dawn-to-day sweep state for the duration of b01c02. Fire passes all three axes.
#   Props: no physical props with established prop cards or oc-* warehouse entries appear in
#   this chapter. The coverage map is Taylor's internal accounting (not a physical prop). The
#   threshold-stones, alleys, and drain angle are environmental geometry — not tracked prop
#   fields. The tallow smoke is a continuous ambient (unchanged from b01c01 baseline, same lane,
#   no flip). No prop fires authored; conservative ruling matches b01c01 precedent.
#   Scene-B peak @17 ("the insects file the ward-junction contact"): no studio or prop field
#   changes at this peak-bone. The filing is a data-layer / actor-interiority act. Absence
#   defended: no field on studio or any prop flips here.
#   Scene-C peak @24 ("taylor-hebert-kl-122ac stalls the count"): no studio or prop field
#   changes. Recognition-and-suppression is wholly interior. Absence defended.
#
# Per-entry annotations:
#   state:1 @20: time_of_day flip defended under Reality (field genuinely flips to end-of-day;
#     persistent through chapter close), Authority (studio.time_of_day is a tracked studio field),
#     Frugality (<old> matches last canonical value; <new> persists; one entry for one flip).
#     No carve-out clause needed — this entry passes all three axes in standard form.
#
# Flagged seams:
#   SEAM-001: studio.time_of_day <old> chain — b01c01 authored zero state-updates-env entries
#     (per b01c01 slice precedent, SEAM-002 from that file). The <old> value here ("dawn") is
#     derived from the b01c01 handoff_out canonical baseline, which reads "dawn" as the chapter-open
#     state. Showrunner should confirm that studio state file for b01c01 was initialized at the
#     project-setup baseline (dawn, stitch-house-lane, tallow-smoke ambient), so the chain from
#     b01c01 baseline → b01c02 @20 flip is unbroken.
#   SEAM-002: scene-B multi-day span — the "days-of-coverage" montage compresses multiple days
#     into a single scene. No time_of_day state-update is authored for the montage bones (@10-@19)
#     because no single bone marks a discrete, persistent time_of_day flip within the montage.
#     If a downstream chapter requires a precise time_of_day handoff state at b01c02 scene-B
#     exit, showrunner should confirm the canonical value is "day-sweep-compressed" or similar.
#     Current ruling: silent on montage bones; only the end-of-day state at @20 is canonical.

# --- ENTRIES ---

1 @20 studio.time_of_day: dawn -> end-of-day

# source: taylor-hebert-kl-122ac
# slice: state-updates-taylor-hebert-kl-122ac
# episode: b01-c02
# author: taylor-hebert-kl-122ac (impersonator, facet-authoring mode)
# phase: 1 R1

2 @6 actor:taylor-hebert-kl-122ac.deployment-state: ambient-subsistence-reading -> systematic-precinct-coverage-deliberate  # field-extension: deployment-state (tracked-state aspect; tracks active-mode of insect-network; carries forward from b01c01 state:1 chain — chapter-open value was passive-subsistence-after-crowd-yield; this scene flips to systematic deliberate-coverage); persistence absolute through chapter close — handoff_out confirms Hook coverage map active across ~40 bodies; cross-facet: NI co-citation required at @6, supplied by NI R1
3 @17 actor:taylor-hebert-kl-122ac.internal-accounting.wren-status: unknown -> filed-as-ward-junction-contact-unnamed  # field-extension: internal-accounting.wren-status (tracked-state aspect; records Taylor's internal categorization of Wren as a coverage-map node, distinct from her perceptual register); persistence absolute — handoff_out confirms "Wren: inside coverage map; no direct contact; named internally as ward-junction contact"; @17 is the scene-B peak (peak-bones membership); cross-facet: POV actor-state, NI co-citation required at @17, supplied by NI R1
4 @24 actor:taylor-hebert-kl-122ac.internal-accounting.coverage-map-recognition-event: not-yet-occurred -> occurred  # field-extension: internal-accounting.coverage-map-recognition-event (tracked-state aspect; records the irreversible occurrence of recognition that the coverage architecture is surveillance over forty-three non-consenting people); persistence absolute — recognition having occurred is not undone by subsequent suppression; @24 is scene-C peak (peak-bones membership) and the canonical bone for moral_legibility_to_self axis-crack arrival per chapter substance s03; cross-facet: POV actor-state, NI co-citation required at @24, supplied by NI R1
5 @25 actor:taylor-hebert-kl-122ac.internal-accounting.coverage-map-recognition-status: unsuppressed -> suppressed-under-harm-reduction  # field-extension: internal-accounting.coverage-map-recognition-status (tracked-state aspect; records the active filing-discipline applied to the recognition event); persistence absolute through chapter close — handoff_out confirms "first moral_legibility crack: coverage-map recognition suppressed under harm-reduction framing"; @25 is the decomposed-second-bone for the recognition-and-suppression mechanism (per chapter substance SOFT-WATCH (1): must be structurally separate from @24 recognition bone); cross-facet: POV actor-state, NI co-citation required at @25, supplied by NI R1
