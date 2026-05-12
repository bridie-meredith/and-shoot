# source: state-updates-oc-broken-maester

facet: state-updates
episode: s01e03
target-scope: actor:oc-broken-maester
author: dialogue-writer-fork:oc-broken-maester
---

# Per-character slice. Single-pass author + cull complete.
#
# Floor-defense note: oc-broken-maester is sparse on-stage in s01e03 outside the closing
# log-construction beat. The on-stage cluster (@73-90: market trip, return, pen-set)
# consists of micro-position transitions within the eastern-quarter location anchor and a
# terminal motor event at @90 (pen-set, tens 3).
#
# Prior-pass culls (this pass):
#
# - CULL @74 location: upper-room-above-apothecary -> eastern-quarter-street. Authority
#   mismatch + transient. The actor's state.md `location` field carries the location-card
#   slug (loc-eastern-quarter-apothecary), not sub-position labels. The eastern-quarter-
#   street sub-position is studio's spatial_layout, not actor:slug.location. Reality check
#   compounds: the card-slug doesn't change across the market trip — he stays in the
#   eastern quarter complex throughout. Persistence test REJECT: reverts at @88, ~14
#   beats later. Anti-pattern #8 (transient-posture as state) + authority cross-license.
#
# - CULL @88 location: eastern-quarter-street -> upper-room-above-apothecary. Same
#   issue: paired revert beat with @74 cull above. Authority + transience.
#
# - REANCHOR documentation_status flip from @90 to @164. Per the brief: "ambient signal
#   (e02) to formal log-entry register (e03 close: 'two log entries written side-by-
#   side')". The "two log entries written side-by-side" is Taylor's log pairing the
#   maester's anomaly with the Hightower file at season terminus. The maester's own pen-
#   activity at @90 closes one writing session in his own records — but his records have
#   always been formal log entries (stm: "Keeps active records of everything he observes;
#   thirty years of such records"), so the "ambient -> formal" delta does not describe
#   his own register at all; it describes how this character exists in the protagonist's
#   record. The flip-beat is the writing beat at @164, not the pen-set at @90. Anti-
#   pattern #7 (pre-empting / lagging) honored — fire on the flip-beat where the field
#   actually mutates.
#
# Skips with floor defense:
#
# - @90 pen-set: tens 3 beat. Posture (`actor:oc-broken-maester.posture: writing ->
#   pen-set-down`) would be transient — no subsequent maester move within e03 for the
#   posture to load-bear into. Anti-pattern #8 (posture-as-state requires multi-beat
#   persistence AND load-bearing). A `stats.record_anomaly_logged` flip is unavailable —
#   the stat is already true at e03 open. A per-session entry counter would be a field-
#   extension too granular to defend. The 3-rating earns tensometer co-citation and
#   narrator-interest fire on Taylor's side (the pen-scratch she hears); no maester-
#   actor-state delta. Refusal-CORRECT per ceiling-defense.
#
# - @73, @75, @77-78, @83-88: sub-position walks (descend stair, alley, market, stall,
#   ascend stair, upper room). Studio's spatial_layout authority. No maester actor-state
#   field flips.
#
# - awareness_of_taylor stays `low` through e03 per card hard fence 2 ("He does not know
#   what Taylor is") + stm ("Has not yet correlated the insect anomaly with the Flea
#   Bottom girl"). No delta.
#
# - Upper-room surveillance condition: per card §"Through-wall observation (load-
#   bearing)", Taylor's insect network has been reaching his upper room from story open.
#   The e03 density-up (beetles relay pen-scratch at @89) is a studio fauna_sense_status
#   delta on the network's coverage of him, not a condition delta on the maester actor
#   target. Register-shift, not state-change.
#
# - Brake-position structural state: "still un-heard" per the brief and card hard fence 4
#   ("Nothing he says lands until too late"). No delta in e03.
#
# Single fire below: the brief's explicitly-flagged meaningful delta — the crossing from
# ambient signal (e02) to formal log-entry register at e03 close.

1 @164 actor:oc-broken-maester.documentation_status: ambient-signal -> named-in-protag-log-paired-with-hightower
# field-extension: documentation_status (new field for s01e03 close-state register-shift; tracked-state aspect — describes how this actor exists in the protagonist's record at the season terminus; not a perception by the maester himself, who remains unaware; not a stylistic flourish; defensible under Reality — persistence absolute past @164, the paired log entry is irreversible in Taylor's record; flagged for margit schema referral)
# cross-facet: actor:<non-POV>.*, narrator-interest co-citation NOT required per rubric §"Cross-axis tests"; tensometer @164 reads 1 in the per-episode file (the terminal log close is a settling beat; the season's reader-asymmetry was committed at @162 wall-facing, tens 3); fire on the flip-beat where the field mutates (@164 writes the entry that pairs the records), not on the upstream decision beat (@162) per anti-pattern #7
