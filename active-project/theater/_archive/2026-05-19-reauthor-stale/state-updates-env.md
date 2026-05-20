facet: state-updates-env
episode: b01c01
author: studio (fresh fork, env-only)
round: r1
---

1 @1 prop:oc-corner-room.occupancy: vacant -> taylor-occupant
# field-extension: occupancy (new field; lodging-entry tracking; setup-baseline = vacant)

2 @2 prop:oc-corner-room.rent-status: unpaid -> paid
# field-extension: rent-status (new field; vouching-credential tracking; rent-paid is the social license to occupy without debt)

3 @5 prop:oc-needle.held-by: coll-net-mender-flea-bottom -> taylor-hebert-kl-122ac
# field-extension: held-by (new field; needle is oc-prop, no prior holder entry; Coll held it through @4 extension, Taylor takes it at @5; persists through @6, @11, @17)

4 @13 studio.thermal: ambient-day -> walls-cooling
# walls cool is a persistent ambient-temperature shift (Scene-B working-day advancing toward late afternoon/evening); persists through remainder of Scene-B

5 @18 prop:oc-nets.worked-state: in-progress -> set-down
# field-extension: worked-state (new field; nets are oc-prop; in-progress = being actively worked during Scene-B; set-down = work session complete, nets laid aside; persists across @19 time-skip into Scene-C)
