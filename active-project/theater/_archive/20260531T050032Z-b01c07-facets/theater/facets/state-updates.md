---
facet: state-updates
sources: [env, septon-halvard-flea-bottom, taylor-hebert-kl-122ac]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates
episode: b01c07
author: studio
scope: ENVIRONMENTAL + LOCATION + PROP (studio.* and prop:* targets only; actor:* authored by dialogue-writer forks)
---

# rubric-carve-out — no actor:* entries authored here
#
# design/shoot-v2/rubric-state-updates.md § Authority
#
# Carve-out scope: all actor:<slug>.* targets
# Carve-out rule: studio does not author actor-state entries; actor-state entries for each character
#   are authored by the corresponding dialogue-writer fork. This file is studio scope only.
# Coverage justification: Per rubric §Authority ACCEPT signatures — studio authors studio.* and
#   prop:<slug>.* only. Actor:* entries are separate fork authority.

1 @2 studio.passage_choke.sept-corner-passage: unblocked -> blocked
2 @7 studio.passage_choke.sept-corner-passage: blocked -> unblocked
3 @7 studio.actor_positions.taylor-hebert-kl-122ac: en-route-ward-circuit -> at-sept-corner
4 @23 studio.actor_positions.taylor-hebert-kl-122ac: at-sept-corner -> departed-sept-corner

# source: septon-halvard-flea-bottom
facet: state-updates
episode: b01c07
author: impersonator:septon-halvard-flea-bottom
target-class: actor:septon-halvard-flea-bottom
---
# state-updates — actor:septon-halvard-flea-bottom — b01c07
#
# Author license (rubric §Authority): non-POV interlocutor fork writes only
# actor:septon-halvard-flea-bottom.* posture / position / encounter / relationship fields.
# Studio owns the sept-corner environment (location, ground, stone) and the handcart prop.
# No narrator-interest co-citation requirement (Halvard is non-POV; the rubric requires
# co-citation only for POV-character actor-state shifts — that is the Taylor fork's burden).
#
# Sparsity discipline: Halvard is the interlocutor, not the POV. His physical register is
# steady, unhurried, non-confrontational — an encounter, not a confrontation. Most of his
# bones are dialogue (n09/n10/n12/n21) or transient body-charge (n16 exhale, n20 absorption)
# that do not flip a persistent tracked field; those are SKIP-CORRECT, not silent omissions.
# Three persistent field-mutations fire across the chapter.

5 @3 actor:septon-halvard-flea-bottom.position: not-yet-established -> at-sept-corner-facing-handcart-man
# Reality: Halvard's chapter-entry position. He arrives already in conversation at the sept-corner;
# the facing-the-handcart-man orientation persists across n03-n04 (he names the sick child from this
# stance) until he turns to Taylor at n11. Posture-as-state (persists multiple beats, load-bearing for
# the encounter), not a transient turn. <old> is the state.md first-touch baseline (position untracked
# at story-open; direct_encounters_this_arc: 0). Authority: his own fork writes his position.

6 @4 actor:septon-halvard-flea-bottom.direct_encounters_this_arc: 0 -> 1
# Reality: naming the sick child to Taylor — extending plain acknowledgment as though she belongs here —
# is the first direct encounter of the arc opening from his side. Irreversible: the encounter-count does
# not revert; persists past episode close. <old> is the state.md stat baseline. Tracked stat field on the
# card (relationship_to_taylor / direct_encounters_this_arc). Authority: his own fork.

7 @4 actor:septon-halvard-flea-bottom.relationship_to_taylor: not-yet-established -> direct-encounter-engaged
# Reality: the card's one-encounter-per-act mandate (Hard Fence 3) lands here — the relationship moves from
# not-yet-established to an active direct encounter. Persistent: the relationship stays established for the
# rest of the arc (he is the counter-argument she stops engaging by d09; that requires the encounter to have
# happened). Fired once on the encounter-open beat to avoid double-firing on the engagement deepening across
# the conversation. Authority: his own fork. No NI co-citation required (non-POV).

8 @11 actor:septon-halvard-flea-bottom.position: at-sept-corner-facing-handcart-man -> at-sept-corner-turned-to-taylor
# Reality: turning from the sick-child account to address Taylor with the errand-man case is the load-bearing
# re-orientation — the encounter becomes the Halvard-Taylor argument here. Persistent: he holds the turned-to-
# Taylor orientation through n12 (thesis), n16 (exhale), n20 (absorbs the counter), n21 (cost-acknowledgment),
# until Taylor leaves at n23. Posture-as-state (multi-beat persistence + load-bearing on the next move).
# <old> matches the prior cited value (entry 1). Authority: his own fork.

# SKIP-CORRECT log (no persistent field flips at these beats):
#   @9  describes the fever's progress     — dialogue / plain accounting; orientation unchanged; no field flip.
#   @10 names the maester's cost            — dialogue; no field flip.
#   @12 speaks the thesis to Taylor          — dialogue (anchor [septon-halvard-flea-bottom:1]); orientation set at n11.
#   @16 exhales                              — transient breath-out (the not-pressing beat); resolves within the beat.
#                                              Anti-pattern #8 transient-posture / #10 stylistic-noting. Silence correct.
#   @20 absorbs the counter                  — reception / body-charge; he does not move; no canonical field mutates.
#                                              Anti-pattern #1 registration-as-state. Feeling/NI territory, not state-updates.
#   @21 speaks the cost-acknowledgment       — dialogue (anchor [septon-halvard-flea-bottom:2]); the stance he names is
#                                              card-constant (the slower method's cost he has decided to pay), not a
#                                              field-change at this beat. relationship already fired at n04.

# source: taylor-hebert-kl-122ac
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

9 @7 actor:taylor-hebert-kl-122ac.position: on-ward-circuit-flea-bottom -> inside-the-sept-corner
10 @15 actor:taylor-hebert-kl-122ac.posture: in-passing-stride -> planted-facing-halvard
11 @23 actor:taylor-hebert-kl-122ac.position: inside-the-sept-corner -> departing-into-the-lane
12 @25 actor:taylor-hebert-kl-122ac.position: departing-into-the-lane -> clear-of-the-hook

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
