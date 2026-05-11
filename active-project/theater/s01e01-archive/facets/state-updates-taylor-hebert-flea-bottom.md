# slice file — facet: state-updates  episode: s01e01  author: dialogue-writer-fork-taylor-hebert-flea-bottom  target-class: actor:taylor-hebert-flea-bottom
# Plain comments here so build_cite_index does not stack YAML blocks in the consolidated state-updates.md (r3-signal-001).

1 @22 actor:taylor-hebert-flea-bottom.research_log_active: false -> true
# field flips at first log-write (@22); persists through episode close (every subsequent log open/write/close beat depends on log being active). @21 is open-without-content; the entry-write at @22 is the flip-beat (anti-pattern #7 avoidance).
2 @90 actor:taylor-hebert-flea-bottom.placement-status: tanner-village-ward -> flea-bottom-placed
# field-extension: placement-status (new field for s01e01 — tracks Taylor's village→KL administrative placement by the elder). Subject of @90 is the elder; field on Taylor flips per @48-anchor precedent (other-subject acts on Taylor's tracked field). Tens@90=3 reversal-proximity (the routing itself is the irreversible turn). Persistence: she does not return to the village.
3 @91 actor:taylor-hebert-flea-bottom.inventory: [] -> [travel-pack]
# inventory acquires travel-pack; persists @91 through @104 setting-down. Anchor verb `lifts` is the flip-beat.
4 @98 actor:taylor-hebert-flea-bottom.location: loc-tanner-village -> loc-flea-bottom
# location field flips at the `enters` verb; transit beats (@94 gate-crossing, @96 road-walking) are non-persistent on this field. Persists until @103 enters-base.
5 @103 actor:taylor-hebert-flea-bottom.location: loc-flea-bottom -> loc-flea-bottom-base
# location field flips at `enters loc-flea-bottom-base`. Persists through episode close (she does not exit the base after @103).
6 @104 actor:taylor-hebert-flea-bottom.inventory: [travel-pack] -> []
# inventory empties at `sets the travel pack`. Persists through episode close — the pack lives at the base.
7 @154 actor:taylor-hebert-flea-bottom.network-anchor: none -> dock-runner-contact-established
# field-extension: network-anchor (new field for s01e01 — tracks Taylor's KL contact network nodes). Anchored on Taylor's speech-back (her irreversible social commit), not on @151 (dock-runner-to-her) or @153 (dock-runner-to-her again). Tens cluster @151=3 reversal-proximity supports the commit-beat fire. Persistence: contact established for downstream s01e02+ network work.
