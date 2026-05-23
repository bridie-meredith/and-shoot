---
facet: state-updates
sources: [coll-net-mender-flea-bottom, env-b01-c01, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: coll-net-mender-flea-bottom
facet: state-updates-actor
episode: b01c01
author: coll-net-mender-flea-bottom (character fork)
---

# State-Updates (Actor: coll-net-mender-flea-bottom) — b01c01
# Scope: actor:coll-net-mender-flea-bottom.* targets only.
# Coll's actor_baselines: all applicable axes are static (capability 1/1, position 1/1,
#   social-tether 5/5, knowledge 4/4). No state changes expected per actor_baselines.
# Rubric check: reality axis — no field on Coll's state card changes persistently in b01c01.
# Coll is stationary throughout; his net-work is his default state from chapter open.

# @3: Coll lifts the eyes. First-touch registration.
# This is NOT a state-update — it is a registration-beat (perception); Coll's eyes-lift
#   is an action within his existing observation-mode, not a persistent field change.
# REFUSE: registration-as-state anti-pattern. Eyes-lift resolves within the beat.

# @4: Coll works the net. Held bone.
# NOT a state-update — this is his default state. Persistence is the baseline, not a change.
# REFUSE: persistence-as-state anti-pattern.

# @8: Coll speaks. Speech act.
# NOT a state-update — speech is not a tracked field. No field changes on Coll's state card.
# REFUSE.

# @20: Coll folds the net. Day-close marker.
# This IS a persistent state change: Coll's working-state transitions from net-mending-active
#   to net-folded-day-close. However, per actor_baselines, Coll's state is static
#   (social-tether 5/5; capability 1/1). The fold is a temporal transition, not a
#   substantive actor-state change. The field that matters here is studio.time_of_day
#   (already captured in state-updates-env entry 5 @20). Coll himself has no tracked field
#   that changes at this beat beyond what studio covers.
# REFUSE: stylistic-noting anti-pattern — the fold is the day-close's environmental signal,
#   not a persistent actor-state mutation.

# RESULT: 0 entries. Coll's state is static throughout b01c01 per actor_baselines.
# This is the correct sparse outcome for a fixture character in a pre-arrangement chapter.

# (file intentionally contains no entries — this is a valid empty state-updates file for a
#   static fixture character)

# source: env-b01-c01
facet: state-updates-env
episode: b01c01
author: studio
---

# State-Updates (Environmental) — b01c01
# Scope: studio.* and prop:* targets only. Environmental + location + prop state changes.
# Fires are persistent field-mutations. No actor-state entries (those are per-character files).

# @1: Taylor pays the building-keeper. First beat — chapter open.
# studio.location establishes Flea Bottom as the active location from chapter open.
1 @1 studio.active_location: null -> flea-bottom
2 @1 studio.time_of_day: null -> morning

# @7: Taylor drops the pack.
# The pack is a prop (carried item); it transitions from carried to set-down.
# This is a persistent state-change (the pack stays at the working corner through s01 and s02).
3 @7 prop:oc-taylor-pack.position: carried -> set-at-working-corner

# @18: City-watch passes the Hook.
# Environmental condition: watch-rotation-active is a studio.active_conditions field change.
# Persistent while the watch is in sight; resolves when they pass.
# NOTE: the fire is on @18 (the patrol passing = the presence peak); the condition
#   activates here and persists through @19 (holds-eyes), then resolves at chapter-ambient.
4 @18 studio.active_conditions.watch-rotation: absent -> passing-the-hook

# @20: Coll folds the net. Day-close marker.
# Time-of-day advances from midday toward the afternoon transition.
5 @20 studio.time_of_day: midday -> afternoon

# NOTE on time-of-day progression:
# The chapter covers morning (@1-9), midday (@11-20), afternoon (@22-29).
# The time-skip blank at flat 10 marks morning→midday; the blank at flat 21 marks midday→afternoon.
# The studio.time_of_day state above fires at the canonical transition beats:
#   @1: chapter open (morning); @20: day-close fold (afternoon per scene-map).
# The @22 scene window (scene C) is already in the afternoon state set at @20.

# source: taylor-hebert-kl-122ac
facet: state-updates-actor
episode: b01c01
author: taylor-hebert-kl-122ac (character fork)
---

# State-Updates (Actor: taylor-hebert-kl-122ac) — b01c01
# Scope: actor:taylor-hebert-kl-122ac.* targets only.
# POV-character state shifts require narrator-interest co-citation per rubric.
# Chapter substance_delta: knowledge 3→3.5 (measured 0.48); capability held at 3.
# No moral-framework, agency, position, social-tether, relational-anchor, or
#   moral-legibility-to-self shifts in b01c01 — pre-arrangement chapter.

# @1: Taylor pays the building-keeper. First-touch on position field.
# Position rank 1 (Flea Bottom anonymous) established from chapter open.
# Field-extension: actor:taylor.position established at project open; first-touch in b01c01.
6 @1 actor:taylor-hebert-kl-122ac.position: null -> flea-bottom-anonymous

# @1: Occupation established. Taylor's cover-work state initialized.
7 @1 actor:taylor-hebert-kl-122ac.occupation: null -> net-mender-flea-bottom-corner

# @7: Pack dropped. Inventory state change.
# The pack is set down at the working corner; Taylor's inventory shifts.
8 @7 actor:taylor-hebert-kl-122ac.inventory.pack: carried -> set-at-working-corner

# @9: Knowledge state updated. First day's passive ward-read complete through the held-feet beat.
# Narrator-interest co-citation: narrator:2 @9 fires on this beat (the inverted-establishing-fact
#   registration is the interior side of the knowledge state shift).
# field-extension: knowledge.ward-geometry (new field for b01c01 ward-orientation tracking)
9 @9 actor:taylor-hebert-kl-122ac.knowledge.ward-geometry: null -> flea-bottom-block-level-passive # field-extension: ward-geometry (b01c01 passive orientation layer)

# @20: Knowledge state updated at the day-close ledger beat.
# The working-day read has delivered: population density, temperature/occupation patterns,
#   well-step movement corridors, watch-rotation geometry.
# Narrator-interest: no fire at @20 (Coll folds the net; it's a chatter bone; narrator is not
#   reaching forward). This is a studio-side environmental state change that produces a knowledge
#   consequence — state-updates-actor fires on the character's knowledge without NI co-citation
#   because the knowledge shift is not interior-registered at this beat (it accumulates through
#   the day's bones; @20 is the session-close, not the acquisition peak).
# NOTE: the substance_delta knowledge gain is measured across all s02 bones; the @20 entry
#   records the daily-ledger close, not a single-bone acquisition.
10 @20 actor:taylor-hebert-kl-122ac.knowledge.ward-geometry: flea-bottom-block-level-passive -> flea-bottom-block-level-day-count-complete

# source: wren-stitch-maker-flea-bottom-ward
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
11 @22 actor:wren-stitch-maker-flea-bottom-ward.position: off-stage -> flea-bottom-alley-mouth-adjacent

# @22: First face-registration. Taylor's insect-sense picks up the new face at alley-mouth.
# This is Wren's in-chapter introduction — her presence state initializes.
# field-extension: in_scene (new field tracking on-stage presence for cost-bearer management)
12 @22 actor:wren-stitch-maker-flea-bottom-ward.in_scene: false -> true # field-extension: in_scene (cost-bearer scene-frequency tracking)

# @28: Wren crosses the street. Position state changes from alley-mouth to far-pavement.
# She departs un-filed. The position change is persistent past the beat (she leaves the scene).
13 @28 actor:wren-stitch-maker-flea-bottom-ward.position: flea-bottom-alley-mouth-adjacent -> flea-bottom-street-far-side

# @28: in_scene reverts to false as Wren departs.
14 @28 actor:wren-stitch-maker-flea-bottom-ward.in_scene: true -> false

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
