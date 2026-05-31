facet: state-updates
episode: b01c07
author: impersonator:taylor-hebert-kl-122ac
target-class: actor:taylor-hebert-kl-122ac (POV actor-state slice; physical/posture fields only)
---

# rubric-carve-out — field-extension declarations (position, posture)
#
# rubric-state-updates.md (design/shoot-v2/rubric-state-updates.md) § Field-extension protocol
#
# Carve-out scope: the `position` and `posture` fields on actor:taylor-hebert-kl-122ac.
# Carve-out rule: Taylor's state.md schema tracks district-level `location` (Flea Bottom Hook,
#   unchanged this chapter) and the semantic `position_in_kl` role; it does NOT carry a
#   fine-grained within-scene `position` or `posture` field. Both are authored here as
#   field-extensions licit under § Field-extension protocol: posture and position are
#   enumerated by the rubric (§Authority, anti-pattern #8) as tracked-state-aspects, NOT
#   perceptions. Mood/register/voice-tone are excluded; these are not those.
# Coverage justification: chunk_cold_read = PASS-CHUNK-VOICE-RISK; interiority was routed off
#   the bones to the narrator-interest facet (rev2 deletions D1-D8). Posture is therefore the
#   load-bearing physical layer of this chapter — the going-still → facing → planting-feet
#   commitment (13-15) and the steadying-feet → leaving (22-23) ARE the engagement, enacted in
#   body. Each posture fire below is persistent past its beat AND load-bearing on the next move
#   (anti-pattern #8 defense), not a transient rotation.
#
# Per-entry annotations:
# - state:2 @13: field-extension posture; arrest-onset persists through the s02 exchange.
# - state:3 @15: field-extension posture; planted-commit, load-bearing for staying-in-argument (n07 soc-tether +0.5).
# - state:4 @22: field-extension posture; re-steadied settle-to-stay, load-bearing for n05 soc-tether +0.5 (non-departure).
# - state:1 @7, state:5 @23, state:6 @25: field-extension position; within-scene position, persistent flips.

1 @7 actor:taylor-hebert-kl-122ac.position: on-ward-circuit-flea-bottom -> at-sept-corner
2 @13 actor:taylor-hebert-kl-122ac.posture: mobile-on-circuit -> arrested-squared-to-halvard
3 @15 actor:taylor-hebert-kl-122ac.posture: arrested-squared-to-halvard -> feet-planted-committed-to-stay
4 @22 actor:taylor-hebert-kl-122ac.posture: feet-planted-committed-to-stay -> feet-resteadied-staying-past-close
5 @23 actor:taylor-hebert-kl-122ac.position: at-sept-corner -> departing-into-lane
6 @25 actor:taylor-hebert-kl-122ac.position: departing-into-lane -> clear-of-the-hook

# --- Deliberate skips (skip-discipline record; not entries) ---
# @1 completes the ward-coverage circuit — SKIP-CORRECT. s01 flat-low approach zone; position
#    baseline is project-setup/prior-chapter carry (on-ward-circuit). Firing here = anti-pattern #9
#    density-on-flat / establishing-state-at-a-bone-beat. The first real position flip is @7.
# @14 faces septon-halvard-flea-bottom — SKIP-CORRECT. The facing is the orientation WITHIN the
#    held posture (arrested @13 → planted @15); firing posture on 13+14+15 is the double-fire
#    anti-pattern (#8: "fire posture once across the window; do not double-fire"). Orientation is
#    subsumed under the @13 arrest and @15 plant. (The +0.3 pol-reg read from the facing is NI
#    territory, not a physical-state field.)
# @18-19 names the body count / speaks to halvard — SKIP-CORRECT. No physical/posture field flips;
#    she is already planted (@15) and has not re-settled (@22) yet. The register-sharpening
#    (+0.2 pol-reg) is interiority/voice = narrator-interest, NOT a tracked physical-state field
#    (anti-pattern #1 registration-as-state; anti-pattern #6 invented-field if forced as posture).
# studio/prop targets and actor:septon-halvard-flea-bottom: OUT OF LICENSE for this fork
#    (authority §: each character writes their own actor-state; studio writes environment/props).
