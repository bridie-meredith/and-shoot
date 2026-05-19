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
# field-extension clarification (cycle-2 fixer, 2026-05-19): `active-holding` = management of attentional allocation and deployment decision ONLY — passive insect-sense data continues to arrive (insects always transmit; Taylor cannot turn off reception); what is HELD is the act of consciously processing that data into tactical knowledge or directing insect movement; this is NOT suppression of the passive sense, which is not in Worm canon. Downstream authors must read `threshold-held-against-density-spike` as: Taylor is consciously capping her use of the arriving data at a threshold level, not as: the data has been blocked. [worm-canon-pedant cycle-1 flag on ambiguity; resolved by this note]
# cite-index back=N note: @8 proto-line does not back-cite this entry; the discipline-hold is interior-state only (not demonstrated externally on the proto-line); cite-index correctly shows back=N; this is an interior-only state mutation

# entry 11 DELETED (cycle-2 fixer pass-2, 2026-05-19 — SIGNAL-002 physical cut): ID gap 10→12 intentional; cite-index references state:11 in co= fields of state:17 and state:20; IDs 12+ not renumbered to preserve cite-index integrity.

12 @15 actor:taylor-hebert-kl-122ac.knowledge.watch-patrol-cadence-hook: unknown -> patrol-first-sighting-logged
# revised from `patrol-pattern-read-passively` (cycle-2 fixer, 2026-05-19): one Watch pass at @15 is a first sighting, not an established cadence or pattern; `patrol-pattern-read` implies recurrent multi-pass temporal pattern — not supportable from one observation; revised to `patrol-first-sighting-logged` (discrete, accurate, does not claim pattern-knowledge from single data point); cape-fic-reader correct that the original value pre-empted pattern-registration from one pass

13 @18 actor:taylor-hebert-kl-122ac.work-role.coll-block: needle-handler-at-coll-block -> needle-handler-at-coll-block-day-one-complete
# revised from `recurring-needle-handler-coll-block` (cycle-2 fixer, 2026-05-19): "recurring" requires ≥2 sessions and a signal from Coll that return is expected; bones file shows nets set-down at @18 (session end) with no Coll utterance inviting return; dark-fantasy-reader correct that "recurring" awards social standing the terrain has not granted after one afternoon; revised to `day-one-complete` (accurate: first session concluded; recurrence claim deferred to subsequent chapter when return is established)

14 @22 actor:taylor-hebert-kl-122ac.knowledge.wren-presence: unregistered -> face-with-voice-registered

15 @24 actor:taylor-hebert-kl-122ac.insect-sense-discipline.pattern-reading: auto-initiating -> caught-by-rule-not-deployed
# field-extension note (cycle-2 fixer, 2026-05-19): `auto-initiating` is a post-Khepri residue effect — the shard's architecture altered by the scale of the Gold Morning override has reduced the latency between passive-data-receipt and pattern-analysis-initiation; pattern-read now fires before Taylor's conscious trigger in high-salience contexts (child → protector-read trigger). This is an AU departure from baseline Worm canon and is licensed by `cond-khepri-residue-122ac` (warehouse). This entry CITES `cond-khepri-residue-122ac` as the mechanism; the departure is marked, not implicit. [worm-canon-pedant cycle-1 flag on unmarked departure; resolved by citation]

16 @25 actor:taylor-hebert-kl-122ac.relational-anchor-status.wren: stranger -> face-not-node

# entry 17 CUT (cycle-2 fixer, 2026-05-19): `actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper` — (a) `ward-layer-deeper` is a direction, not a state value (cape-fic: cannot apply as clean write-back; rubric requires discrete new field values like `provisional-labor-eligible`, `ward-present`); (b) no bones-supported acquisition at @26 (Wren's departure direction) — if ward-layer information was acquired it was at @22 (the speech beat), not @26; entry fires against its own facet's prohibition-catch at @24 (pattern-read caught by rule); (c) entry 14 @22 already captures the Wren-registration; a deeper ward-layer read at @26 without bones-anchor is inferred knowledge, not acquired knowledge. Defer to subsequent chapter when Taylor has accumulated more observations.

# source: wren-stitch-maker-flea-bottom-ward
facet: state-updates
episode: b01c01
source: wren-stitch-maker-flea-bottom-ward
target: actor:wren-stitch-maker-flea-bottom-ward
author: impersonator-wren-stitch-maker-flea-bottom-ward
---

18 @20 actor:wren-stitch-maker-flea-bottom-ward.location: stitch-maker-household-hook-district -> flea-bottom-street-outside-coll-corner-room
19 @22 actor:wren-stitch-maker-flea-bottom-ward.stats.taylor_awareness: unencountered -> noticed-as-presence-on-block  # field-extension: prior value reset from project-baseline-listed (observed-and-decided-not-to-ask is d01+ value); chapter is pre-d01 per shared-brief; this fire is first-registration only, not identification
# arrival-timing specification (cycle-2 fixer, 2026-05-19 — state-judge dispatch for dark-fantasy + worm-canon-pedant specificity gap): Wren's arrival at the street is established by state:18 @20 (location: stitch-maker-household -> flea-bottom-street-outside-coll-corner-room); she was NOT present during scene-B (@8-@18); she arrived at @20, approached at @21, and speaks at @22; the insect-work of @8 and @12 predates her arrival by the full scene-B duration; therefore the "pre-anomaly opener" premise of the dialogue sidecar is state-supported: Wren has been on-street for ≤2 bones (@20 arrival, @21 approach) before speaking; at @22 she is a fresh arrival to the corner room's field, not a long-duration observer of the insect-atmosphere; the vibes at @22 (back=Y persistent-state cloud) are atmosphere she walks into, not atmosphere she has been accumulating. The observation-before-action (per her card §Default Stance) operates on: (a) the knot she sees Taylor working, (b) Coll's presence as the known elder, (c) Taylor as the unknown; she has NOT had time to register the insect-anomaly as anomalous vs. normal-for-this-block on her first approach. State entry supports the sidecar's claim.
20 @26 actor:wren-stitch-maker-flea-bottom-ward.location: flea-bottom-street-outside-coll-corner-room -> returning-to-stitch-maker-household-hook-district
