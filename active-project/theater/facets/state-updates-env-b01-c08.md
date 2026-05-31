facet: state-updates
episode: b01c08
author: studio
source: env
---

# rubric-carve-out — field-extensions for six new sub-fields
#
# design/shoot-v2/rubric-state-updates.md § Field-extension protocol
#
# Carve-out scope: all six field-extensions below (oswyn-watcher-network,
#   feed-edge-geometry, water-point-geometry, water-point-position,
#   prop:oc-jarvis-packet.*, prop:oc-feed-station-ledger.*).
# Carve-out rule: each extension tracks a tracked-state aspect first-touched this
#   chapter; field is persistent, not a perception or stylistic flourish; author
#   may extend under § Field-extension protocol and flags for margit referral.
# Coverage justification: no prior studio state entry has recorded these fields;
#   the chapter makes them real and persistent; margit referrals noted inline.
#
# Per-entry annotations (cite which carve-out clause applies):
# - state:1 @8: field-extension studio.fauna_sense_status.oswyn-watcher-network
#     (first-touch; Oswyn network integration is a persistent coverage-map mutation;
#     tracked-state-aspect, not a perception; margit referral: fauna_sense_status extension)
# - state:2 @9: prop:oc-jarvis-packet (new oc-prop; analogous to oc-jarvis-channel-form
#     at b01c06; delivered and consumed within chapter; margit referral: oc-jarvis-packet.card.md)
# - state:3 @10: prop:oc-jarvis-packet.seal-condition (standard seal-bearing prop field)
# - state:4 @13: prop:oc-feed-station-ledger (new oc-prop; first-touch; persistent ledger entry;
#     margit referral: oc-feed-station-ledger.card.md)
# - state:5 @15: field-extension studio.fauna_sense_status.feed-edge-geometry
#     (first-touch; Aemond-adjacent edge now present in feed map; persistent structural change)
# - state:6 @23: field-extension studio.spatial_layout.water-point-position
#     (first-touch this chapter; watcher-boy stationed @3, vacated @23; spatial fact persists)
# - state:7 @24: field-extension studio.fauna_sense_status.water-point-geometry
#     (distinct from @8 network-level integration; tracks specific geometry-occupancy at
#     the water-point after watcher-boy vacates; chapter terminal image enacted as field-state)

1 @8 studio.fauna_sense_status.oswyn-watcher-network: uncharted -> integrated-into-coverage
2 @9 prop:oc-jarvis-packet.state: absent -> arrived-at-feed-station
3 @10 prop:oc-jarvis-packet.seal-condition: sealed -> broken
4 @13 prop:oc-feed-station-ledger.aemond-entry: absent -> logged
5 @15 studio.fauna_sense_status.feed-edge-geometry: pre-aemond-entry -> aemond-edge-lit
6 @23 studio.spatial_layout.water-point-position: watcher-boy-stationed -> watcher-boy-absent
7 @24 studio.fauna_sense_status.water-point-geometry: oswyn-network-managed -> insect-feed-covered
