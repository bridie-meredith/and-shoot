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
