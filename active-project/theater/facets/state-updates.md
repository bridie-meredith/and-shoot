---
facet: state-updates
sources: [env, oswyn-mudway-flea-bottom-elder, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
# slice: state-updates-env
# episode: b01c01

# rubric-carve-out — zero-fire defended: env-only, static chapter, no prop cards
#
# design/shoot-v2/rubric-state-updates.md § "What state-updates is for" + § "Curve-shape rubric"
#
# Carve-out scope: all 27 bones in b01c01
# Carve-out rule: zero studio.* and prop:* fires for this chapter; density-band target (8-18%
#   of proto-lines) is not met — this is a floor-defended zero per the rubric's sparsity
#   discipline, not a calibration failure.
# Coverage justification: the rubric states "Inflating fires to hit density without each fire
#   passing all three axes is the prohibited move" and "the flat-low approach zone is nearly
#   silent." b01c01 is an exterior Flea Bottom lane chapter with no tracked prop exchanges,
#   no door-state changes, no time-of-day shift within the chapter, and no weather event.
#   The environment is static from dawn through the chapter close: same lane, same tallow
#   smoke (continuous ambient, present at @2 and @25 unchanged — no flip from a prior
#   canonical value), same drain geometry. The only candidate prop (the fish-cart, @7) has
#   no prop card in cards/props/ and no oc-* warehouse entry; the conservative ruling under
#   §"Field-extension protocol" is to refuse and flag for margit rather than author against
#   an unestablished oc- slug. The crowd-dynamics (gap opening, gap closing, crowd-density
#   shifts) are transient — they revert to the baseline lane-state within the episode and do
#   not map to a named field on the studio state schema. Oswyn's positional change at @21
#   (peak-bone) is actor-state, out of scope for studio.
#
# Per-entry annotations: none (zero entries authored)
#
# Flagged seams:
#   SEAM-001: prop:oc-fish-cart — the fish-cart at @7 has no prop card and no warehouse
#     presence. If the stitcher or a downstream chapter needs the cart as a tracked prop,
#     a margit referral is warranted. Current ruling: no fire, no oc-* extension, seam flagged.
#   SEAM-002: studio.time_of_day baseline — chapter opens at dawn (handoff_in confirms
#     dawn) and no within-chapter time-shift bone fires. No time_of_day state-update entry
#     is authored here; the studio state file for b01c01 should be initialized at project-setup
#     baseline (dawn, stitch-house-lane, tallow-smoke ambient) rather than via a bone-anchored
#     entry. Showrunner/studio should confirm baseline initialization is handled at episode-open
#     rather than mid-chapter.

# --- ENTRIES ---
# (none authored; see rationale above)

# source: oswyn-mudway-flea-bottom-elder
# slice: state-updates-oswyn-mudway-flea-bottom-elder
# episode: b01-c01
---
facet: state-updates
episode: b01-c01
author: impersonator:oswyn-mudway-flea-bottom-elder
---

1 @21 actor:oswyn-mudway-flea-bottom-elder.location: mudway-alley-hook-district -> lane-mouth-of-rescue-site
2 @26 actor:oswyn-mudway-flea-bottom-elder.relationship_to_taylor: regular-contact-no-awareness-of-function -> categorized-known-unknown-witch-adjacent  # field-extension: relationship_to_taylor value-space extended to carry categorization-shift (was tracked-state on state.md; the chin-lift is the somatic expression of an awareness change that persists past the chapter per handoff_out world_state)

# source: taylor-hebert-kl-122ac
# slice: state-updates-taylor-hebert-kl-122ac
# episode: b01-c01

3 @12 actor:taylor-hebert-kl-122ac.deployment-state: passive-subsistence-range -> active-crowd-yield-deployment  # field-extension: deployment-state (tracked-state aspect; tracks active-vs-suppressed posture of insect-network; cl01a canonical axis-move anchor); persistence absolute through chapter close — deployment is acknowledged-active in handoff_out
4 @12 actor:taylor-hebert-kl-122ac.capability_axis: 2 -> 3  # canonical-axis stat increment matching chapter substance_delta capability+1.0 cl01a at anchor_bone b01c01s02n06; handoff_out specifies "Taylor: capability rank 3"
5 @17 actor:taylor-hebert-kl-122ac.posture: in-the-gap -> hands-up-mouth-shut-witness-facing  # field-extension: posture (tracked per rubric §form); persistent across @17-@22 — load-bearing for the witness-categorization beats at @19, @20, @21 (the chunk: "the foreign woman who made the opening with her hands up and her mouth shut"); resolves at @24 when she turns toward the alley-mouth
6 @21 actor:taylor-hebert-kl-122ac.social_tether_prot_axis: 1 -> 2  # canonical-axis stat increment matching chapter substance_delta social_tether-prot-rise+1.0 cl01b at anchor_bone b01c01s03n04; Oswyn's lane-mouth take is the bone the axis-move locks against — Taylor enters Oswyn's awareness layer and the tether-account opens
7 @24 actor:taylor-hebert-kl-122ac.body-orientation: facing-the-child -> facing-the-alley-mouth-away-from-stitch-house  # field-extension: body-orientation (tracked-state aspect; not posture — this is the cardinal direction of attention); persistent through chapter close; bone rationale explicitly names "body-direction that excludes the stitch-house" — the not-looking is enacted as a direction-toward
8 @26 actor:taylor-hebert-kl-122ac.ward-recognition: invisible-foreign-woman -> categorized-by-oswyn-as-something-other  # field-extension: ward-recognition (tracked-state aspect; the ward's category for Taylor); persistent — handoff_out specifies "Hook precinct knows the foreign woman who moved the crowd"; Oswyn's chin-lift is the categorization-completing body-tell, but the persistent field-shift is in Taylor's social-recognition status, not Oswyn's gesture

# source: wren-stitch-maker-flea-bottom-ward
# slice: state-updates-wren-stitch-maker-flea-bottom-ward
# episode: b01-c01
facet: state-updates
episode: b01-c01
author: impersonator:wren-stitch-maker-flea-bottom-ward
---

9 @27 actor:wren-stitch-maker-flea-bottom-ward.relational_anchor_to_taylor: nascent -> observation-traced-d01-deterrence
