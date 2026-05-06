---
phase: 2
facet: location-state (locational facet only — no other facet types)
process: design/shoot-v2/facet-tuning-process.md
rubric: design/shoot-v2/rubric-location-state.md (V2 locked)
---

# Phase 2 — Location-State Writer-Fork Intents

18 stratified anchors for the studio fork to author against. Each anchor specifies:
- proto-line ID and verbatim text
- 3–5 surrounding proto-lines for context
- which prior entries (if any) are currently inherited at this anchor
- what the move at the anchor turns on
- the writer's *task* (which is always: decide whether this anchor earns a loc-state entry, and if yes, draft 2–3 candidates)

**Output discipline.** The studio fork produces *location-state facet entries only*. No other facet types. The only acceptable outputs per intent are:
1. One chosen loc-state entry in the schema shape `<id> @<proto-line-id> <slug> | <time> | <weather> | <conditions> | <one-clause sensory note>` plus 1–2 rejected drafts and a per-axis signature citation, OR
2. `NONE` with one-line reason citing which axis the anchor fails.

If the anchor fails the rubric, the writer **must say NONE**. Refusing to fire is a valid output and is exactly what the frugality + necessity axes are for. Do not invent loc-state to fill a slot.

**Stratification.** The 18 anchors split:
- 5 boundary-crossings / new-location entries (rubric expects ACCEPT-shape)
- 2 scene-anchors at episode/scene open (rubric expects ACCEPT-shape — first beat in new location-and-moment exception)
- 3 state-change beats within established locations (rubric expects ACCEPT-shape)
- 1 fauna-feed beat (floor-defense candidate)
- 4 within-scene-movement traps (rubric expects NONE — environment is inherited)
- 2 persistence/atmosphere traps (rubric expects NONE — anti-patterns 2 and 3)
- 1 sound-arrival herald-at-wall beat (floor-defense candidate)

Plus calibration anchor (#1) is a known-strong target — the writer should arrive at an entry close to the V2-accepted reference for it. Calibration is for reviewer triangulation.

**The writer is blind.** Do not read: `design/shoot-v2/loc-state-candidates.md`, any `loc-state-v[12]-review.md`, `design/shoot-v2/phase1-locstate-report.md`, the rejected/accepted lists, or this intents file's expected-disposition column. Author from the cards + the rubric + the per-anchor spec only. (The expected-disposition column below is for the orchestrator's reconciliation; the writer's prompt strips it.)

---

## Calibration anchor

### Intent C — calibration

- **Episode/proto-lines:** `active-project/theater/proto-lines/s01e06.md`, anchor PL10.
- **Anchor proto-line:** `10 the gatehouse lantern bleeds amber at half a league`
- **Context (surrounding proto-lines):** `7 the bird holds the head toward the road / 8 the bird holds the small tilt / 9 the road north stays empty / 10 the gatehouse lantern bleeds amber at half a league / 11 the lantern reads as a smear at distance / 12 harrenhal holds the one warmth in the field`
- **Inherited loc-state:** sept-yard-wall predawn, cold-clear no-wind, wall-stone-cold, frozen-ground (scene-anchor at PL1 already established).
- **What the move turns on:** the bird's perception layer reaches a *new remote location* (Harrenhal gatehouse) at *half a league distance*. The lantern is the keystone perceptible focus that the entire ensuing surveillance sequence will inherit from.
- **Cards to consult:** `cards/locations/loc-harrenhal-exterior.card.md`, `cards/conditions/cond-fauna-control-rules.card.md`, `active-project/staff/studio/ltm.md`.
- **Writer task:** decide; if yes, draft.
- **Expected-disposition (orchestrator only):** ACCEPT — first citation of harrenhal-gatehouse-distant; the half-a-league distance is load-bearing for the subsequent recon block.

---

## Boundary-crossings / new-location entries (5)

### Intent 1
- **Anchor:** s01e01 PL11 — `the officer comes through the gate`
- **Context:** PL8 `edric holds his eyes on the road past the cart` / PL9 `the clerk unrolls the parchment` / PL10 `the clerk counts the yard` / PL11 (anchor) / PL12 `the officer steps to the center of the yard` / PL13 `the officer speaks to the yard`
- **Inherited loc-state:** none — episode-open, no prior entries in this scene.
- **What the move turns on:** the officer's entry through the gate. Gate-state and threshold are the load-bearing facts.
- **Cards:** `cards/locations/westerosi-smallfolk-village-common.card.md` (closest analogue — adapt to sept-yard) or `active-project/warehouse/` if a sept-yard card exists. Riverlands 120 AC.
- **Expected-disposition:** ACCEPT — boundary-crossing with state-change (gate going from shut to open as the officer arrives).

### Intent 2
- **Anchor:** s01e02 PL10 — `the granary door opens under plumms-man's left hand`
- **Context:** PL7 `plumms-man closes the small book` / PL8 `plumms-man marks the page with his thumb` / PL9 `plumms-man steps forward` / PL10 (anchor) / PL11 `plumms-man scans the granary floor` / PL12 `plumms-man crouches at the threshold`
- **Inherited loc-state:** assume an entry has fired at PL9 establishing granary-exterior with door-shut. The PL10 entry is the next move.
- **What the move turns on:** door-state changing from shut to open; the swept floor is what the opening reveals.
- **Cards:** `cards/locations/westerosi-smallfolk-village-common.card.md` (granary is village outbuilding; smallfolk register).
- **Expected-disposition:** ACCEPT — explicit state-change (door shut → open); reveals new perceptible focus (swept floor).

### Intent 3
- **Anchor:** s01e03 PL12 — `three bodies cross the threshold of the arch`
- **Context:** PL10 `the raven compresses on the sill` / PL11 `the raven holds the wing against the stone` / PL12 (anchor) / PL13 `the inspector enters the arch` / PL14 `the inspector carries the ledger board under the arm` / PL15 `the scribe enters behind the inspector`
- **Inherited loc-state:** assume morning sept-nave with side-door-open + light-on-rushes is established at an earlier beat (the light-event entry).
- **What the move turns on:** new entrants crossing the arch threshold from courtyard into nave. Arch is a different sub-location from the side door already established.
- **Cards:** Riverlands sept; smallfolk register.
- **Expected-disposition:** ACCEPT — boundary-crossing into nave from a different threshold than the inherited side-door context; population-change is load-bearing.

### Intent 4
- **Anchor:** s01e04 PL56 — `taylor opens the side door`
- **Context:** PL53 `taylor holds the eyes on the page` / PL54 `taylor slides the folio against the ribs under the shirt` / PL55 `the shelf stands empty` / PL56 (anchor) / PL57 `the cold arrives` / PL58 `taylor passes the bench`
- **Inherited loc-state:** sept-chancel at predawn, cold (alcove-warmth-gone), candle-on-table.
- **What the move turns on:** the door's opening is itself the state-change event; the cold yard arriving through the open door is the consequence the move releases.
- **Cards:** Riverlands sept; predawn cold context.
- **Expected-disposition:** ACCEPT — explicit state-change (door shut → open); but trap: do not let the consequence (cold-arriving) become the focus-element. The pre-existing condition the door-open turns on is the differential between interior-warmth and exterior-cold.

### Intent 5
- **Anchor:** s01e06 PL72 — `taylor enters the sept`
- **Context:** PL70 `the rider walks toward the gate` / PL71 `taylor reaches the door` / PL72 (anchor) / PL73 `taylor closes the door behind her` / PL74 `the channel re-indexes on the sept interior` / PL75 `the yard drops off the still plane`
- **Inherited loc-state:** sept-yard at predawn cold-clear (yard-frozen) — established from Taylor's earlier crossing.
- **What the move turns on:** crossing from yard exterior to nave interior. The door-shut-behind is the threshold-state-change; the channel re-indexing is interior fauna coming online.
- **Cards:** Riverlands sept (interior); smallfolk register.
- **Expected-disposition:** ACCEPT — new location (sept-nave-interior) at a new moment (predawn return); first interior citation in this episode.

---

## Scene-anchors at episode/scene open (2)

### Intent 6
- **Anchor:** s01e05 PL40 — `three women stand along the kiln wall`
- **Context:** PL37 `the cart rounds the bend on the eastern track` / PL38 `the cart passes the threshold-stone` / PL39 `taylor walks the cart-track to the common` / PL40 (anchor) / PL41 `a carter stands at the post` / PL42 `the headman waits at the bench-end`
- **Inherited loc-state:** assume eastern-track at sun-up is established at PL37 (cart-rounds-bend entry). PL40 is the first beat at a new location (village-common).
- **What the move turns on:** scene-anchor at a new location-and-moment. Trap: the proto-line verb is "stand" (stillness). But the rubric's necessity-axis exception for first-beat-in-new-location applies — if and only if the entry serves as place-anchor for subsequent inherited beats. The kiln wall is a real location feature; the women are scene-population.
- **Cards:** `cards/locations/westerosi-smallfolk-village-common.card.md` exactly fits.
- **Expected-disposition:** ACCEPT under place-anchor exception, BUT the focus-element must be a *location feature*, not the actors. Watch for actor-state laundered as loc-state.

### Intent 7
- **Anchor:** s01e06 PL1 — `the stone holds the cold against taylor's back`
- **Context:** PL1 (anchor) / PL2 `taylor holds the wall-weight at the hip` / PL3 `the bird sits on the gatepost` / PL4 `taylor placed the bird on the gatepost` / PL5 `taylor holds the line from the wall to the post`
- **Inherited loc-state:** none — episode-open, predawn winter.
- **What the move turns on:** scene-anchor for an episode opening at the sept-yard wall in predawn cold. The wall-stone-cold and frozen-ground conditions establish what the body is paying for the surveillance posture.
- **Cards:** Riverlands sept exterior; cold-winter; cond-series-tone-constraints if relevant.
- **Expected-disposition:** ACCEPT under place-anchor exception. Trap: the verb "holds" is stillness — but this is the first beat in a new location-and-moment for the episode, and the cold-stone-against-back is a perceptible physical fact tied to the location. Single focus-element discipline.

---

## State-change beats within established locations (3)

### Intent 8
- **Anchor:** s01e06 PL34 — `a second amber bleed lights beside the first`
- **Context:** PL32 `taylor holds the back in place` / PL33 `the wire hums the same note` / PL34 (anchor) / PL35 `a third light kindles at the road's end` / PL36 `the gap separates the second light from the third` / PL37 `three lights ignite in sequence`
- **Inherited loc-state:** harrenhal-gatehouse-distant predawn cold-clear, gatehouse-lantern-on (one light) — established at the calibration anchor #C.
- **What the move turns on:** state-change at the same remote location — light count goes 1 → 2.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md`.
- **Expected-disposition:** ACCEPT — discrete state-change at established location. Trap: must name the *change* (second light beside the first), not just re-cite the gatehouse.

### Intent 9
- **Anchor:** s01e06 PL55 — `the seam between the gate-leaves opens`
- **Context:** PL52 `two men work the girth and bridle on one horse` / PL53 `a third man works the gate-leaves` / PL54 `the bar lifts halfway out of the brackets` / PL55 (anchor) / PL56 `a second horse stands at loose tether against the inner wall` / PL57 `the second horse stands saddled`
- **Inherited loc-state:** harrenhal-gateyard at fifty-feet (close-resolved via bird approach), three-lights, work-faces-south.
- **What the move turns on:** gate state changes from closed to parting; bar half-out is the mechanism.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md`.
- **Expected-disposition:** ACCEPT — threshold state-change at established remote location.

### Intent 10
- **Anchor:** s01e02 PL86 — `the drying rack takes Taylor's shoulder`
- **Context:** PL83 `the horse walks at measured pace` / PL84 `the satchel rides plumms-man's hip` / PL85 `the sparrow at the cote eave passes Taylor the picture` / PL86 (anchor) / PL87 `Taylor holds against the rack` / PL88 `the chamomile fills Taylor's air`
- **Inherited loc-state:** sept-wall-exterior morning clear (Taylor cleared the sept wall at PL16 and walked the lane).
- **What the move turns on:** Taylor arrives at a new sub-location (drying-yard) — physical contact with the rack. The chamomile-air is what the rack delivers.
- **Cards:** smallfolk village; outdoor working-yard.
- **Expected-disposition:** ACCEPT — new sub-location entry; the chamomile rack is a concrete focus-element the body's contact turns on.

---

## Fauna-feed (1, floor-defense candidate)

### Intent 11
- **Anchor:** s01e06 PL19 — `a mouse-shape steps in the seam at taylor's hip`
- **Context:** PL16 `the frozen ground gives back nothing through the soles` / PL17 `the clock runs on taylor` / PL18 `the cost hangs on a hook behind the door` / PL19 (anchor) / PL20 `the mouse repositions in the seam` / PL21 `the feed takes the spike of the mouse`
- **Inherited loc-state:** sept-yard-wall predawn cold-clear (scene-anchor at PL1).
- **What the move turns on:** Taylor's passive feed registers a movement at a specific micro-location (seam-at-hip). The feed-spike depends on the spatial and thermal resolution.
- **Cards:** `cards/conditions/cond-fauna-control-rules.card.md` is critical here.
- **Expected-disposition:** ACCEPT under floor-defense — fauna-feed beats earn loc-state when the perception's mechanic depends on a named location fact. Trap: must name the *spatial* fact (seam-at-hip), not just describe the mouse.

---

## Within-scene movement traps (4)

These anchors should NOT get loc-state entries. The environment is inherited; nothing has turned over. The writer's correct output is `NONE` with a one-line reason. Firing on any of these is a frugality violation per anti-pattern 4.

### Intent 12
- **Anchor:** s01e01 PL12 — `the officer steps to the center of the yard`
- **Context:** PL11 (officer comes through the gate — Intent 1's anchor) / PL12 (this anchor) / PL13 `the officer speaks to the yard` / PL14 `taylor crosses the twelve feet of packed dirt`
- **Inherited loc-state:** assume Intent 1's entry fired at PL11 (gate-open, sept-yard at dawn).
- **What the move turns on:** the officer continues into the yard he just entered. No new state.
- **Expected-disposition:** NONE — within-scene movement, no state-change since the inherited PL11 entry.

### Intent 13
- **Anchor:** s01e01 PL37 — `taylor steps into the path of the officer's shoulder`
- **Context:** PL35 `the officer's weight shifts back to the heel facing the clerk` / PL36 `the stylus moves on the line under taylor's name` / PL37 (anchor) / PL38 `taylor puts the letter into the air in front of the officer`
- **Inherited loc-state:** sept-yard at dawn (multiple prior entries possible; assume one is held).
- **What the move turns on:** confrontation-blocking. Two actors narrowing the channel between them. This is actor-blocking, not location condition.
- **Expected-disposition:** NONE — actor-state, not loc-state. Anti-pattern 4 (actor-state laundered as loc-state).

### Intent 14
- **Anchor:** s01e05 PL44 — `the steward spreads the scroll across the trestle`
- **Context:** PL42 `the headman waits at the bench-end` / PL43 `the headman holds his hands flat on the bench` / PL44 (anchor) / PL45 `the steward works the curl flat with his palm` / PL46 `the maester remains on the cart`
- **Inherited loc-state:** village-common at morning (assume scene-anchor entry at PL40 holds — Intent 6).
- **What the move turns on:** prop-placement (scroll on trestle). The trestle's existence is location-card content; the scroll's spreading is prop-state, belongs in state-update facet, not location-state.
- **Expected-disposition:** NONE — prop-placement, not loc-state. Anti-pattern 5 (plan-bullet residue).

### Intent 15
- **Anchor:** s01e05 PL73 — `rowan walks the four paces to the trestle`
- **Context:** PL71 `the maester speaks to the common` / PL72 `rowan speaks to the maester` / PL73 (anchor) / PL74 `rowan lowers the folio to his side` / PL75 `rowan takes his place beside taylor`
- **Inherited loc-state:** village-common at morning (assume scene-anchor and one state-change have fired earlier).
- **What the move turns on:** within-scene navigation. Four paces is actor-blocking, not a location feature.
- **Expected-disposition:** NONE — within-scene movement; the four-paces distance is actor-blocking, not a loc-state.

---

## Persistence/atmosphere traps (2)

These anchors should NOT get loc-state entries. They are stillness/persistence beats describing things that are not changing.

### Intent 16
- **Anchor:** s01e02 PL21 — `the granary holds its three-week shape`
- **Context:** PL18 `the sparrows hold the eaves` / PL19 `the rat holds the barrow at the south wall` / PL20 `the beetles hold the road-edge stone` / PL21 (anchor) / PL22 `Taylor keeps walking`
- **Inherited loc-state:** village-lane at morning, granary-exterior known.
- **What the move turns on:** nothing. The granary is in its accustomed state; Taylor reads its persistence.
- **Expected-disposition:** NONE — persistence-as-state, anti-pattern 3. The three-week shape is location-card content, not loc-state.

### Intent 17
- **Anchor:** s01e06 PL94 — `the grey holds the road`
- **Context:** PL92 `the closing took the instrument dark` / PL93 `the clock continues to run outside` / PL94 (anchor) / PL95 `a man on the road can be read at distance` / PL96 `the window closes on the room`
- **Inherited loc-state:** sept-nave-interior predawn (Taylor has just sealed herself inside; the feed has stopped at the door).
- **What the move turns on:** Taylor's *imagined* perception of the dawn-grey on the road outside. Atmospheric persistence; she cannot see this directly (the channel has dropped).
- **Expected-disposition:** NONE — mood-painting on stillness, anti-pattern 2. Also: the location-slug would be wrong (Taylor is inside; the road outside is not her current loc-state).

---

## Sound-arrival herald-at-wall (1, floor-defense candidate)

### Intent 18
- **Anchor:** s01e06 PL67 — `a shod hoof strikes the cobbles half a league north`
- **Context:** PL65 `the frozen ground lays out under taylor's pace` / PL66 `the door stands at the end of the cross` / PL67 (anchor) / PL68 `the still field carries the note to taylor` / PL69 `the rider walks toward the gate` / PL70 `the rider walks toward the gate`
- **Inherited loc-state:** sept-yard-wall predawn cold-clear.
- **What the move turns on:** auditory detection at distance. The cold-still field and the cobble-surface together are what makes the hoof-strike audible at half-a-league. Without those conditions named, the sound-arrival is unanchored.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md` (Harrenhal road); `cards/conditions/cond-fauna-control-rules.card.md`.
- **Expected-disposition:** ACCEPT under floor-defense — herald-at-wall canonical case. Sound-carrying + cobble-surface as named conditions.

---

## End of intents

The studio fork sees this file with the **expected-disposition lines stripped**. Its job is to derive disposition from the rubric, not from a cheat sheet.
