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
