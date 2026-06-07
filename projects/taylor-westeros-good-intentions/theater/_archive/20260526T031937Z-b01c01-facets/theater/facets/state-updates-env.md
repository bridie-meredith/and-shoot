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
