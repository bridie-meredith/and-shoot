---
facet: state-updates
sources: [env, coll-net-mender-flea-bottom, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
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

# source: coll-net-mender-flea-bottom
facet: state-updates
episode: b01c01
source: coll-net-mender-flea-bottom
author: impersonator-coll-net-mender-flea-bottom
target-class: actor:coll-net-mender-flea-bottom
---

6 @3 actor:coll-net-mender-flea-bottom.block_baseline_new_faces: none-this-week -> one-new-face-fish-gate-lane # field-extension: block_baseline_new_faces (tracks Coll's accumulating non-interpretive register of new presences on the block; first-day appearance is block-data, not pattern-data; pattern registration deferred to ~d06 per card stats.taylor_pattern_registered)

# source: taylor-hebert-kl-122ac
facet: state-updates
episode: b01c01
author: taylor-hebert-kl-122ac (impersonator, facet-mode)
source: taylor-hebert-kl-122ac
round: r1
---

7 @2 actor:taylor-hebert-kl-122ac.social-tether.coll-block-presence: none -> paying-resident-at-corner-room
8 @3 actor:taylor-hebert-kl-122ac.knowledge.coll-as-vouching-vector: unmapped -> registered-as-block-fixture-with-verbal-contact
9 @5 actor:taylor-hebert-kl-122ac.work-role.coll-block: outside -> needle-handler-at-coll-block
10 @8 actor:taylor-hebert-kl-122ac.insect-sense-discipline.active-holding: ambient-passive -> threshold-held-against-density-spike
11 @12 actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively
12 @15 actor:taylor-hebert-kl-122ac.knowledge.watch-patrol-cadence-hook: unknown -> patrol-pattern-read-passively
13 @18 actor:taylor-hebert-kl-122ac.work-role.coll-block: needle-handler-at-coll-block -> recurring-needle-handler-coll-block
14 @22 actor:taylor-hebert-kl-122ac.knowledge.wren-presence: unregistered -> face-with-voice-registered
15 @24 actor:taylor-hebert-kl-122ac.insect-sense-discipline.pattern-reading: auto-initiating -> caught-by-rule-not-deployed
16 @25 actor:taylor-hebert-kl-122ac.relational-anchor-status.wren: stranger -> face-not-node
17 @26 actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper

# source: wren-stitch-maker-flea-bottom-ward
facet: state-updates
episode: b01c01
source: wren-stitch-maker-flea-bottom-ward
target: actor:wren-stitch-maker-flea-bottom-ward
author: impersonator-wren-stitch-maker-flea-bottom-ward
---

18 @20 actor:wren-stitch-maker-flea-bottom-ward.location: stitch-maker-household-hook-district -> flea-bottom-street-outside-coll-corner-room
19 @22 actor:wren-stitch-maker-flea-bottom-ward.stats.taylor_awareness: unencountered -> noticed-as-presence-on-block  # field-extension: prior value reset from project-baseline-listed (observed-and-decided-not-to-ask is d01+ value); chapter is pre-d01 per shared-brief; this fire is first-registration only, not identification
20 @26 actor:wren-stitch-maker-flea-bottom-ward.location: flea-bottom-street-outside-coll-corner-room -> returning-to-stitch-maker-household-hook-district
