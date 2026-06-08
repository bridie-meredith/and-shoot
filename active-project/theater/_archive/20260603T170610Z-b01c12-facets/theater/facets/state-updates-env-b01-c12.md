facet: state-updates-env
episode: b01-c12
author: studio
note: environment/location/prop scope only (actor-state authored separately)
---

# rubric-carve-out — studio authority; actor-state excluded per author-license
#
# design/shoot-v2/rubric-state-updates.md § Authority
#
# Carve-out scope: all actor:* entries
# Carve-out rule: studio does not author actor:* targets; actor-state (taylor, jarvis) is actor-fork authority
# Coverage justification: chapter is silent (zero dialogue-anchor bones); actor-fork state entries authored separately;
#   all studio entries in this file target studio.* or prop:oc-* only
#
# POV co-citation carve-out: studio entries do not require narrator-interest co-citation
# (narrator-interest co-citation required only for actor:<POV-character>.* entries per rubric § Cross-axis tests)

# Field-extension note (new fields on oc-feed-ledger):
#   prop:oc-feed-ledger.gap-column-entry — new field (first-touch b01c12; refusal-response arc)
#   prop:oc-feed-ledger.anchor-column-entry — new field (first-touch b01c12; cl-d06/cl-d08 settlement arc)
#   prop:oc-feed-ledger.breach-column-entry — new field (first-touch b01c12; moral_framework -1.0 Khepri-cost arc)
# Field-extension note (new fields on oc-ward-coverage-notes):
#   prop:oc-ward-coverage-notes.content prior state value: "hook-rushwick-oswyn-corridors-plus-south-extension"
#     (last set b01c09 state:1 @7; abbreviated here as "hook-rushwick-oswyn-plus-south" for canonicalization)
# Field-extension note (new field on studio):
#   studio.fauna_sense_status.coverage-scale — new sub-field (first-touch b01c12; five-ward aggregate threshold)
# Margit referrals: oc-feed-ledger schema extension (3 new fields); oc-ward-coverage-notes content-value canonicalization

1 @1 studio.time_of_day: end-of-day -> morning
# chapter-open reset: b01c11 closed end-of-day; b01c12 opens on the morning circuit east of the water-gate
# field-extension: n/a (studio.time_of_day is an established tracked field — b01c11 state:9 / b01c10 state anchors)

2 @9 prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-plus-south -> hook-rushwick-oswyn-plus-south-plus-northern-cluster-1
# first ward-cluster addition: taylor extends northern ward-cluster off the water-gate approach
# peak-bone @9 co-citation: capability +0.5 (cl05 first tranche); the ward-cluster is a persistent coverage addition
# persistence: this content value holds through scene-B and scene-C; second addition fires at @30

3 @11 prop:oc-jarvis-packet.holder: jarvis-coin-kl-courier -> station-surface
# jarvis delivers the b01c12 incoming packet to the feed-station surface
# prior state "jarvis-coin-kl-courier": Jarvis carried this packet to the meeting; the handoff at @11 completes
# persistence: packet remains at station-surface through @12-@15; holder re-flips at @23

4 @12 prop:oc-jarvis-packet.seal-condition: sealed -> broken
# taylor breaks the wax seal; irreversible; seal-condition cannot return to sealed
# prior state "sealed": consistent with incoming packet state (Otto's apparatus standard; wax intact on delivery)
# persistence: broken-seal persists through scene-B (packet is opened, read, and set down)

5 @13 prop:oc-jarvis-packet.physical-condition: folded-closed -> covering-sheet-open
# taylor opens the covering-sheet; the gate-tower corridor designation is now visible
# peak-bone @13 co-citation: the collision becomes visible — the apparatus names the lanes by their exact boundary-marks
# persistence: covering-sheet-open persists through @14 (turning) and @15 (packet set); closes as carried-state

6 @17 studio.time_of_day: morning -> midday
# scene-C opens at midday (the refusal / response-writing); scene-A and scene-B were both morning-circuit
# the scene-map names scene-C "midday (the refusal)"; time-of-day advance fires on the scene-C open bone
# persistence: midday holds through scene-C; late-afternoon fires at @29

7 @19 prop:oc-feed-ledger.gap-column-entry: absent -> boundary-refusal-written
# taylor writes the boundary entry into the gap-column: the east-water-gate lanes are not accessible, structural limit
# peak-bone @19 co-citation: position-prot-rise +0.5 (cl02); the refusal written into the channel as a named gap
# field-extension: gap-column-entry first-touch b01c12 (new field on oc-feed-ledger; covers both column-open and entry-written)
# persistence: boundary-refusal-written persists to @22; the entry closes (sealed) at the response-entry-close beat

8 @22 prop:oc-feed-ledger.gap-column-entry: boundary-refusal-written -> closed
# taylor closes the response entry; the refusal is finalized in the channel record
# peak-bone @22 co-citation: position-prot-rise +0.5 (cl02 second tranche); withholding now load-bearing in the record
# persistence: closed; gap-column-entry remains closed at chapter-end

9 @23 prop:oc-jarvis-packet.holder: station-surface -> jarvis-coin-kl-courier
# jarvis takes the sealed response packet; the apparatus accepts the coverage limit and will route an alternate
# prior state "station-surface": set at @11 (delivery); the same physical packet (now containing the refusal response)
# persistence: jarvis-coin-kl-courier carries the packet out; packet departs the feed-station at this beat

10 @26 prop:oc-feed-ledger.anchor-column-entry: absent -> settlement-written
# taylor writes the anchor-column entry; relational_anchor +0.5 (cl-d08 mechanism: Wren's free movement = coverage boundary)
# peak-shadow @26 co-citation: the weight settling as a decision about what the map can reach (not a name)
# field-extension: anchor-column-entry first-touch b01c12 (new field on oc-feed-ledger; covers both column-open and entry-written)
# persistence: settlement-written persists to @27; the entry closes at @27

11 @27 prop:oc-feed-ledger.anchor-column-entry: settlement-written -> closed
# taylor closes the anchor-column entry; cl-d06 settlement complete (second tranche settled, DEC-0071)
# peak-bone @27 co-citation: relational_anchor +0.5; the long-deferred cl-d06 debt closes without a name written
# persistence: closed; anchor-column-entry remains closed at chapter-end; her hand lifts at @28

12 @29 studio.time_of_day: midday -> late-afternoon
# scene-D opens in the late afternoon (second ward-cluster addition and accounting-close)
# scene-map names scene-D "late afternoon / accounting-close"; time-of-day advance fires on the scene-D open bone
# persistence: late-afternoon holds through scene-D accounting; end-of-day fires at @42

13 @30 prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-plus-south-plus-northern-cluster-1 -> hook-rushwick-oswyn-plus-south-plus-both-clusters
# muddy-way upper-margin cluster added; full-deployment threshold achieved as the insects fill the new coverage zone
# peak-shadow @30 co-citation: capability +0.5 (cl05 second tranche); the second ward-cluster completes the architecture
# prior state: hook-rushwick-oswyn-plus-south-plus-northern-cluster-1 (set at @9 this chapter)
# persistence: five-ward-plus-approaches coverage holds at chapter-end (the feed runs on at full deployment)

14 @32 studio.fauna_sense_status.coverage-scale: partial-multi-ward -> five-ward-plus-approaches
# for the first time all five wards and the Flea Bottom approaches are mapped simultaneously
# field-extension: coverage-scale first-touch b01c12 (new sub-field under studio.fauna_sense_status; tracks aggregate-scale threshold)
# peak-shadow @32 co-citation: the aggregate-scale threshold is the Khepri-rhyming fact — the architecture complete in scope
# prior state "partial-multi-ward": the prior chapters (c01-c11) had progressively expanded coverage but not all-five-simultaneous
# persistence: five-ward-plus-approaches holds at chapter-end and into downstream chapters

15 @42 prop:oc-feed-ledger.breach-column-entry: absent -> threshold-filed
# the breach column receives its threshold entry: the Khepri-repetition cost recorded in flat ledger register
# peak-bone @42 co-citation: moral_framework -1.0 (cl05 cost side); the word is not in the entry; the cost is
# field-extension: breach-column-entry first-touch b01c12 (new field on oc-feed-ledger; Khepri-threshold ledger arc)
# persistence: threshold-filed is permanent — the breach column entry cannot be un-filed

16 @42 studio.time_of_day: late-afternoon -> end-of-day
# the accounting closes; the feed runs on; the chapter ends at end-of-day
# two entries on @42: one prop-field (breach-column-entry), one studio-field (time_of_day) — distinct targets, both licit
# persistence: end-of-day is the chapter-close time_of_day (carried into b01c13 as baseline)
