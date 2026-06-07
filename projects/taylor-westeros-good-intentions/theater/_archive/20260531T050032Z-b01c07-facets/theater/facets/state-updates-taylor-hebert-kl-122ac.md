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
#   commitment (13-15) IS the engagement, enacted in body. The single posture fire below is
#   persistent past its beat AND load-bearing on the next move (anti-pattern #8 defense), fired
#   ONCE across the approach-to-peak commitment window, not on each rotation.
#
# Per-entry annotations:
# - state:2 @15: field-extension posture; the going-still(@13)→facing(@14)→planting(@15)
#   commitment fired ONCE at the planted-stance peak-bone (soc-tether +0.5); orientation
#   (facing-halvard) folded into the new value; persists through the exchange to @22.
# - state:1 @7, state:3 @23, state:4 @25: field-extension position; within-scene position,
#   persistent flips, fired on the flip-beat.

1 @7 actor:taylor-hebert-kl-122ac.position: on-ward-circuit-flea-bottom -> inside-the-sept-corner
2 @15 actor:taylor-hebert-kl-122ac.posture: in-passing-stride -> planted-facing-halvard
3 @23 actor:taylor-hebert-kl-122ac.position: inside-the-sept-corner -> departing-into-the-lane
4 @25 actor:taylor-hebert-kl-122ac.position: departing-into-the-lane -> clear-of-the-hook

# --- Deliberate skips (skip-discipline record; not entries) ---
# @1 completes the ward-coverage circuit — SKIP-CORRECT. s01 flat-low approach zone; position
#    baseline is project-setup/prior-chapter carry (on-ward-circuit). Firing here = anti-pattern #9
#    density-on-flat / establishing-state-at-a-bone-beat. The first real position flip is @7 (entry).
# @5 receives the plain acknowledgment / @8 acknowledges halvard — SKIP-CORRECT. Perception and
#    reciprocal-social-contact beats; no field on Taylor flips (already inside-the-sept-corner from
#    @7; orientation not yet committed). Registration-as-state (anti-pattern #1). flat-low zone.
# @13 goes still — SKIP-CORRECT. The arrest is the transition INTO the posture-commitment sequence
#    (@13 still → @14 faces → @15 plants), not the persistent posture. Per anti-pattern #8 the
#    going-still verb is not state; fire on the planted stance (@15), once across the window. The
#    interior thesis-landing is narrator-interest territory.
# @14 faces septon-halvard-flea-bottom — SKIP-CORRECT. The facing is the orientation WITHIN the
#    commitment window (@13 arrest → @15 plant). Firing posture on 13+14+15 is the double-fire
#    anti-pattern (#8). Orientation is folded into the single @15 posture value. The +0.3 pol-reg
#    read from the facing is NI territory, not a physical-state field.
# @18-19 names the body count / speaks to halvard — SKIP-CORRECT. No physical/posture field flips;
#    she is already planted (@15). pol-reg +0.2 register-sharpening is interiority/voice =
#    narrator-interest, NOT a tracked physical-state field (anti-pattern #1; #6 if forced as posture).
# @22 steadies the feet — SKIP-CORRECT (NONE-CONFIRMED). soc-tether +0.5 peak-bone, BUT the
#    steadying re-affirms the already-planted stance (@15) and DISSOLVES one beat later at the @23
#    departure. Persistence test fails: the re-steadied value does not survive past @23. This is
#    held-against-turn / body-charge — the @39-class calibration anchor ("sets her feet ... where
#    his next pace commits" — NONE-CONFIRMED). The +0.5 tether-completion is witnessed by the
#    positional hold but is NOT a persistent posture field-flip; the canonical posture-state was
#    set at @15. Floor-defense invoked: over-firing a transient corrupts canonical memory.
# studio/prop targets and actor:septon-halvard-flea-bottom: OUT OF LICENSE for this fork
#    (authority §: each character writes their own actor-state; studio writes environment/props).
