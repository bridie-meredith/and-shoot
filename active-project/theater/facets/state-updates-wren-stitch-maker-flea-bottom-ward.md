facet: state-updates-actor
episode: b01c01
author: wren-stitch-maker-flea-bottom-ward (character fork)
---

# State-Updates (Actor: wren-stitch-maker-flea-bottom-ward) — b01c01
# Scope: actor:wren-stitch-maker-flea-bottom-ward.* targets only.
# Wren appears in scene C only (@22-29). Her actor_baselines:
#   capability: static 1/1 (child, no power)
#   position: static 1/1 (smallfolk-ward, no court layer)
#   social-tether: moves 5→1 (across the book; b01c01 is her introduction at 5)
#   relational-anchor-status: moves 3→1 (across the book; b01c01 seeding at 3)
#   knowledge: static 3/3 (distributed-attention habit established at b01c01)

# @22: Wren enters the alley-mouth. First appearance — first-touch on position field.
1 @22 actor:wren-stitch-maker-flea-bottom-ward.position: off-stage -> flea-bottom-alley-mouth-adjacent

# @22: First face-registration. Taylor's insect-sense picks up the new face at alley-mouth.
# This is Wren's in-chapter introduction — her presence state initializes.
# field-extension: in_scene (new field tracking on-stage presence for cost-bearer management)
2 @22 actor:wren-stitch-maker-flea-bottom-ward.in_scene: false -> true # field-extension: in_scene (cost-bearer scene-frequency tracking)

# @28: Wren crosses the street. Position state changes from alley-mouth to far-pavement.
# She departs un-filed. The position change is persistent past the beat (she leaves the scene).
3 @28 actor:wren-stitch-maker-flea-bottom-ward.position: flea-bottom-alley-mouth-adjacent -> flea-bottom-street-far-side

# @28: in_scene reverts to false as Wren departs.
4 @28 actor:wren-stitch-maker-flea-bottom-ward.in_scene: true -> false

# NOTE: relational-anchor-status does NOT advance in this chapter.
# Wren's relational-anchor-status starts at 3 (b01c01 handoff_in: "not yet named as significant
#   node"). Taylor declines to file Wren as a node (@27, rule-catches-assessment). The chapter
#   ends with Wren at rank 3 — named outside the ledger but not yet advanced to load-bearing
#   (that is d02). No state-update on relational-anchor-status.
#
# knowledge: Wren's distributed-attention habit (knowledge:3) is ESTABLISHED in this chapter
#   per actor_baselines source: scene-pinned-b01c01. However, "established" means the baseline
#   is confirmed, not that it changes from a prior value. It is a first-touch initialization,
#   not a delta. Writing this as a state-update would be persistence-as-state (anti-pattern #9).
#   Routing to REFUSE.
