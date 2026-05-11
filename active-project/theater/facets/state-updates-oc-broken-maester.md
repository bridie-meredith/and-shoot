facet: state-updates
episode: s01e01
author: dialogue-writer-fork:oc-broken-maester
target-scope: actor:oc-broken-maester
---

# (no entries)

# Authoring notes — SKIP-CORRECT for all maester-anchored beats
#
# oc-broken-maester proto-line anchors in s01e01: @114, @129, @130, @133.
# Per rubric § Reality / Anti-pattern #1 (registration-as-state) and
# Anti-pattern #10 (stylistic noting), none of these beats carry a
# persistent mutation of a tracked field on the maester's state schema
# (location / condition / inventory / stats{awareness_of_taylor,
# record_current_year, record_anomaly_logged}).
#
# - @114 "the maester speaks to the room" — verbalization. No field flips.
#   Speech is not a tracked state. SKIP-CORRECT.
# - @129 "the maester crosses the room" — intra-location position shift
#   inside his upper apothecary room. His tracked `location` field stays
#   at loc-eastern-quarter-apothecary across the beat; no sub-position
#   field exists on his state schema and the shift fails the persistence
#   test (no load-bearing persistent orientation past the beat). Refusing
#   field-extension per the conservative-move clause; this is a transient,
#   not a tracked-state aspect. SKIP-CORRECT.
# - @130 "oc-broken-maester speaks to the room" — verbalization. No field
#   flips. The maester does not know Taylor is the listener and does not
#   correlate her to the insect anomaly (STM: "Has not yet correlated the
#   insect anomaly with the Flea Bottom girl"). `awareness_of_taylor`
#   stays at `low`. SKIP-CORRECT.
# - @133 "the maester laughs" — momentary motor event (rubric § Reality
#   REJECT-signature "stylistic noting" / "transient-posture"). Tensometer
#   reads the rupture through the network's response at @134 (`the beetles
#   fall silent`, ID 518 upstream) — that rupture is the *insect-network's*
#   absence-act and routes to studio / non-maester targets, not to the
#   maester's canonical state. The laugh itself does not persistently flip
#   any maester-field. SKIP-CORRECT.
#
# No `awareness_of_taylor: low -> *` fire in this episode: the maester's
# correlation of insect-anomaly to Taylor is structurally deferred past
# s01e01 (card § "Nothing he says lands until too late"; STM "has not yet
# correlated"). Firing here would pre-empt the season arc.
#
# No `record_anomaly_logged: false -> true` fire: per STM the anomaly is
# already logged at episode open ("Has been aware of unusual insect
# behavior in his upper rooms for some weeks; noted in records"). First-
# touch baseline is already `true`; no flip.
#
# No `location: * -> *` fire: maester remains at
# loc-eastern-quarter-apothecary throughout the episode (he never exits
# the room in the proto-line file; the room is established as his upper
# room of the apothecary).
#
# Cross-facet check: tensometer cluster at proto-lines @129-@134 carries
# rungs 2/2/3/2/2/1 with rupture at upstream ID 518 (`the beetles fall
# silent`) — that rupture is honored by studio's fauna_sense_status /
# insect-network state, not by maester-actor state. No @64-class strong-
# expect on oc-broken-maester in this episode. Cross-facet contract
# satisfied with zero fires.

# entries: 0
# pre-cull authored: 0
# cull deletions: 0
# seams flagged: none (see authoring notes)
