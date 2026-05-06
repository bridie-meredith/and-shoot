---
facet: location-state
episodes: s01e01-s01e06 (Phase 1 training corpus)
author: orchestrator (corpus-prep, permissive draft)
purpose: Phase 1 reviewer-tuning training data for the location-state facet rubric.
note: |
  Drafted permissively per the Phase 1 corpus-prep call: any anchor proto-line that
  plausibly warrants a location-state entry got a candidate, including known-bad
  shapes (set-dressing sweep, persistence, atmosphere) so the V1→V2 lift is visible.
  Location slugs are working slugs; reconciliation against canonical location cards
  happens post-Phase-1.
---

# Location-State Candidate Corpus

Format per `schemas/facet.schema.md`:
```
<id> @<proto-line-id> <location-slug> | <time> | <weather> | <conditions> | <one-clause sensory note>
```

`<id>` is corpus-scoped (1..N). `@<proto-line-id>` cites the anchor in the corresponding episode's `proto-lines/<slug>.md`. Episode boundaries marked as comments.

---

## s01e01 — sept yard, census officer

1 @1 sept-yard | dawn | clear | gate-shut, banner-furled | the cart sits at the timber gate with banner furled
2 @4 sept-yard | dawn | clear | flagstone-gaps, beetles | beetles hold the seams in the flagstone
3 @11 sept-yard | dawn | clear | gate-open, line-forming | the officer crosses the timber threshold into the yard
4 @12 sept-yard | dawn | clear | flagstone-dry, line-forming | the yard clears a path to the officer's center stance
5 @14 sept-yard | dawn | clear | packed-dirt-line | twelve feet of packed dirt to the line's open spot
6 @23 sept-yard | dawn | clear | line-formed, far-end-open | the line stretches the full yard to its far end
7 @31 sept-yard | dawn | clear | sept-door-shut | the sept door's closed face at the yard's east edge
8 @37 sept-yard | dawn | clear | yard-narrowed | a body-width opens between officer and clerk
9 @70 sept-yard | dawn | clear | sept-door-shut, yard-empty | the sept door at the yard's east edge with the cart gone
10 @73 sept-doorway | dawn | clear | frame-shadow | the doorframe shadow falls across the threshold

## s01e02 — smallfolk village, granary, lanes

11 @9 granary-exterior | morning | clear | door-shut, lane-worn | the granary's outer door at one stride
12 @10 granary-threshold | morning | clear | door-open, swept-floor | the door swings inward onto the swept granary floor
13 @12 granary-threshold | morning | clear | threshold-cold | the threshold-line between lane and granary floor
14 @16 sept-wall-exterior | morning | clear | wall-low, lane-beyond | the sept's south wall passes behind Taylor
15 @17 village-lane | morning | clear | lane-empty | the lane stretches between dwellings with no one in sight
16 @21 granary-exterior | morning | clear | granary-three-week-shape | the granary holds its three-week shape
17 @38 granary-threshold | morning | clear | doorway-open, lane-worn | the threshold-stone gives onto the worn lane
18 @42 village-track-north | morning | clear | track-firm | the worn northbound track leaves the granary at plumms-man's back
19 @76 village-track-north | morning | clear | track-firm, hoofbeats-near | the northbound track at the village edge under the horse's pace
20 @86 drying-yard | morning | clear | rack-hung, chamomile-air | the chamomile-hung drying rack at Taylor's shoulder

## s01e03 — sept nave, side door, arch (inspector)

21 @5 sept-nave | morning | clear | sill-still, raven-perched | the raven sits on the sill
22 @7 sept-nave | morning | clear | side-door-open, light-on-rushes | a wedge of morning light crosses the rushes
23 @8 sept-nave | morning | clear | wedge-of-light, doorframe-shadow | the wedge of light lies between Taylor and the arch
24 @12 sept-arch | morning | clear | arch-open, three-bodies-entering | the arch opens onto the nave from the courtyard
25 @22 sept-nave | morning | clear | side-door-shut, bench-empty | the side door past the empty bench
26 @35 sept-nave | morning | clear | rushes-dry, doorframe-released | the rushes give underfoot one step from the doorframe
27 @60 sept-side-passage | morning | clear | passage-narrow, sightline-cut | the side-passage cuts off the line of sight to the bench

## s01e04 — sept interior at predawn → yard → lodge

28 @19 sept-nave-doorframe | predawn | cold | doorframe-cold, alcove-warmth-fading | the doorframe bites cold through Taylor's shoulders
29 @26 sept-nave | predawn | cold | rushes-cold, alcove-warmth-gone | the cold rushes give under the heel
30 @34 sept-chancel | predawn | cold-deepening | altar-table-edge | the altar table's edge meets the hip at the round
31 @39 sept-chancel | predawn | cold | candle-on-table, register-on-shelf | the candle on the chancel table beside the register shelf
32 @55 sept-chancel | predawn | cold | shelf-empty | the shelf stands empty
33 @56 sept-side-door | predawn | cold | door-opening, yard-cold-arriving | the cold yard floods through the side door
34 @59 sept-yard | predawn | cold-clear | gate-ahead, lodge-doorway-occupied | the lodge doorway holds Rowan at the gate
35 @64 sept-yard | predawn | cold-clear | open-ground, frost-on-flag | frost-flagged open ground between sept-door and lodge
36 @73 lodge-threshold | predawn | cold-clear | threshold-stone, doorstep-stone | the lodge threshold-stone where yard meets doorstep
37 @50 sept-chancel | predawn | cold | candle-holding | taylor stops at the page

## s01e05 — sept threshold → cart-track → village common

38 @1 sept-doorway | dawn | clear | door-open, candlelight-on-stone | the candlelight reaches across the threshold-stone
39 @14 sept-doorway | dawn | clear | wedge-of-light-on-stone | the wedge of light rests on the stone
40 @15 sept-yard | dawn | clear | yard-east-angle | the yard's east angle past the bench
41 @22 eastern-road | dawn | clear | road-empty | the eastern road holds the silence
42 @37 eastern-track | dawn | sun-cresting | bend-in-track, treeline-clearing | the cart rounds the bend where the eastern track turns toward the sept
43 @38 sept-yard-edge | dawn | sun-up | threshold-stone, cart-passing | the threshold-stone at the cart's wheel
44 @39 cart-track | morning | clear | track-firm, common-ahead | the cart-track between sept and common
45 @40 village-common | morning | clear | kiln-wall-south, three-women | the kiln wall at the common's south edge with three women along it
46 @44 village-common | morning | clear | trestle-set, scroll-flat | the trestle set at the common's center with the scroll spreading
47 @50 village-common | morning | clear | headman-table, satchel-set | the headman's table at the bench-end
48 @73 village-common | morning | clear | trestle-near, four-paces | four paces of common between Rowan and the trestle
49 @80 village-common | morning | clear | chair-at-trestle-far-side | the maester's chair at the trestle's far side

## s01e06 — sept-yard wall, remote recon to Harrenhal, return to nave

50 @1 sept-yard-wall | predawn | cold-clear, no-wind | wall-stone-cold, frozen-ground | the cold dressed stone at Taylor's back
51 @9 sept-yard-wall | predawn | cold-clear | road-north-empty | the north road runs empty past the gatepost
52 @10 harrenhal-gatehouse-distant | predawn | cold-clear, no-wind | gatehouse-lantern-on | the gatehouse lantern bleeds amber at half a league
53 @19 sept-yard-wall | predawn | cold-clear | seam-at-hip, mouse-warm | a mouse-shape steps in the seam at Taylor's hip
54 @34 harrenhal-gatehouse-distant | predawn | cold-clear | second-light-on | a second amber lights beside the first at the gatehouse
55 @37 harrenhal-gatehouse-distant | predawn | cold-clear | three-lights-sequenced | three amber bleeds at the gatehouse, sequenced
56 @51 harrenhal-gateyard | predawn | cold-clear | gateyard-lit-fifty-feet | the gate-yard resolves under the gatehouse lights at fifty feet
57 @55 harrenhal-gate | predawn | cold-clear | gate-leaves-parting, bar-half-out | the gate-leaves part along the seam
58 @64 sept-yard | predawn | cold-clear | yard-frozen, sept-door-ahead | the frozen yard between wall and sept-door
59 @71 sept-doorway | predawn | cold-clear | door-ahead, threshold | the sept door at the end of the cross
60 @72 sept-nave-interior | predawn | cold-interior | door-shut-behind, mice-grain-crate | the cold dark of the nave settling against the closed door
61 @79 sept-nave | predawn | cold-interior | dark-no-light, rowan-five-paces | five paces of dark between Taylor and Rowan, no lamp
62 @94 harrenhal-distant | predawn | cold-clear | grey-on-road | the grey holds the road
63 @67 sept-yard-wall | predawn | cold-clear | sound-carrying, hoof-on-cobble | a shod hoof strikes the cobbles half a league north
64 @86 sept-nave | predawn | cold-interior | floor-cold, stone-floor | the nave-cold settles in the stone of the floor
65 @96 sept-nave | predawn | cold-interior | no-window, room-sealed | the room holds no window
