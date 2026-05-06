---
phase: 2 (writer-blind)
facet: location-state (locational facet only — no other facet types)
rubric: design/shoot-v2/rubric-location-state.md (V2 locked)
---

# Phase 2 — Location-State Author Intents (Blind)

You are authoring location-state facet entries for the shoot-v2 pipeline. Read the rubric first; it is the authority for whether to fire an entry at all.

**Output discipline.** Location-state entries only. No other facet types. Per intent, output exactly one of:

1. **One chosen entry** in the schema shape `<intent-letter> @<proto-line-id> <slug> | <time> | <weather> | <conditions> | <one-clause sensory note>`, plus 1–2 rejected drafts (each on its own line, prefixed `REJECTED:`), and a citation block listing which axes (necessity / interestingness / frugality) the chosen entry affirmatively demonstrates with a one-line justification each.

2. **`NONE`** with a one-line reason citing which axis the anchor fails. Refusing to fire is a valid and often-correct output. Do not invent loc-state to fill a slot.

If you produce an entry, the schema fields are mandatory and pipe-delimited. Time / weather / conditions / sensory-note must each do operative work. The sensory note is the most load-bearing field — name one perceptible focus-element in five words or fewer when possible.

**Anti-patterns to refuse (named in the rubric):**
1. Set-dressing sweep (multiple focus-elements in one note).
2. Mood-painting on stillness (atmosphere as substitute for a perceptible focus).
3. Persistence-as-state (firing on holds, stays, stands, sits — environmental continuity).
4. Inherited re-naming (re-citing established environment without state-change).
5. Plan-bullet residue (prop-placements, scene-summaries — these belong elsewhere).
6. Time/weather padding (label variation that does no work).

**Tests to run before each fire decision:**
- Strip test — remove the entry; does the proto-line still resolve in inherited environment?
- Pointing test — can you name one perceptible focus-element in five words or fewer?
- Previous-entry test — would this render identically under the inherited state?
- Herald/cart heuristic — is the focus *the herald at the wall* or *the cart by the wall*?

---

## Calibration anchor

### Intent C
- **Episode/proto-lines:** `active-project/theater/proto-lines/s01e06.md`, anchor PL10.
- **Anchor:** `10 the gatehouse lantern bleeds amber at half a league`
- **Surrounding:** PL7–12 (read in file).
- **Inherited loc-state:** sept-yard-wall predawn cold-clear (scene-anchor at PL1).
- **What the move turns on:** the bird's perception layer reaches a new remote location at half-a-league distance. The lantern is the keystone perceptible focus.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md`, `cards/conditions/cond-fauna-control-rules.card.md`, `active-project/staff/studio/ltm.md`.
- **Task:** decide; if yes, draft.

---

## Anchors

### Intent 1
- **Anchor:** s01e01 PL11 — `the officer comes through the gate`
- **Surrounding:** PL8–13 (read in file `active-project/theater/proto-lines/s01e01.md`).
- **Inherited loc-state:** none — episode-open, no prior entries in this scene.
- **What the move turns on:** the officer's entry through the gate. Gate-state and threshold are the load-bearing facts.
- **Cards:** `cards/locations/westerosi-smallfolk-village-common.card.md` (closest analogue — adapt to sept-yard); Riverlands 120 AC.

### Intent 2
- **Anchor:** s01e02 PL10 — `the granary door opens under plumms-man's left hand`
- **Surrounding:** PL7–12 in `s01e02.md`.
- **Inherited loc-state:** assume an entry has fired at PL9 establishing granary-exterior with door-shut.
- **What the move turns on:** door-state changing from shut to open; the swept floor is what the opening reveals.
- **Cards:** `cards/locations/westerosi-smallfolk-village-common.card.md` (granary as village outbuilding).

### Intent 3
- **Anchor:** s01e03 PL12 — `three bodies cross the threshold of the arch`
- **Surrounding:** PL10–15 in `s01e03.md`.
- **Inherited loc-state:** assume morning sept-nave with side-door-open + light-on-rushes is established at an earlier beat.
- **What the move turns on:** new entrants crossing the arch threshold from courtyard into nave. Arch is a different sub-location from the side door.

### Intent 4
- **Anchor:** s01e04 PL56 — `taylor opens the side door`
- **Surrounding:** PL53–58 in `s01e04.md`.
- **Inherited loc-state:** sept-chancel at predawn, cold (alcove-warmth-gone), candle-on-table.
- **What the move turns on:** the door opens. The differential between interior-warmth-fading and exterior-cold is the operative condition the move releases.

### Intent 5
- **Anchor:** s01e06 PL72 — `taylor enters the sept`
- **Surrounding:** PL70–75 in `s01e06.md`.
- **Inherited loc-state:** sept-yard at predawn cold-clear, yard-frozen.
- **What the move turns on:** crossing from yard exterior to nave interior. The door-shut-behind is the threshold-state-change; the channel re-indexing is interior fauna coming online.

### Intent 6
- **Anchor:** s01e05 PL40 — `three women stand along the kiln wall`
- **Surrounding:** PL37–42 in `s01e05.md`.
- **Inherited loc-state:** assume eastern-track at sun-up is established at PL37. PL40 is the first beat at a new location (village-common).
- **What the move turns on:** scene-anchor at a new location-and-moment. Note: the proto-line verb is "stand" — apply the rubric's first-beat-in-new-location exception carefully and ensure the focus-element is a *location feature*, not the actors.
- **Cards:** `cards/locations/westerosi-smallfolk-village-common.card.md`.

### Intent 7
- **Anchor:** s01e06 PL1 — `the stone holds the cold against taylor's back`
- **Surrounding:** PL1–5 in `s01e06.md`.
- **Inherited loc-state:** none — episode-open, predawn winter.
- **What the move turns on:** scene-anchor for an episode opening at the sept-yard wall in predawn cold.
- **Cards:** Riverlands sept exterior; cold-winter conditions.

### Intent 8
- **Anchor:** s01e06 PL34 — `a second amber bleed lights beside the first`
- **Surrounding:** PL32–37 in `s01e06.md`.
- **Inherited loc-state:** harrenhal-gatehouse-distant predawn cold-clear, gatehouse-lantern-on (one light) — established at calibration anchor C.
- **What the move turns on:** state-change at the same remote location — light count goes 1 → 2.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md`.

### Intent 9
- **Anchor:** s01e06 PL55 — `the seam between the gate-leaves opens`
- **Surrounding:** PL52–57 in `s01e06.md`.
- **Inherited loc-state:** harrenhal-gateyard at fifty-feet (close-resolved), three-lights, work-faces-south.
- **What the move turns on:** gate state changes from closed to parting; bar half-out is the mechanism.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md`.

### Intent 10
- **Anchor:** s01e02 PL86 — `the drying rack takes Taylor's shoulder`
- **Surrounding:** PL83–88 in `s01e02.md`.
- **Inherited loc-state:** sept-wall-exterior morning clear (Taylor cleared the sept wall earlier and walked the lane).
- **What the move turns on:** Taylor arrives at a new sub-location (drying-yard) — physical contact with the rack. The chamomile-air is what the rack delivers.

### Intent 11
- **Anchor:** s01e06 PL19 — `a mouse-shape steps in the seam at taylor's hip`
- **Surrounding:** PL16–21 in `s01e06.md`.
- **Inherited loc-state:** sept-yard-wall predawn cold-clear (scene-anchor at PL1).
- **What the move turns on:** Taylor's passive feed registers a movement at a specific micro-location. The feed-spike depends on the spatial and thermal resolution.
- **Cards:** `cards/conditions/cond-fauna-control-rules.card.md` is critical here.

### Intent 12
- **Anchor:** s01e01 PL12 — `the officer steps to the center of the yard`
- **Surrounding:** PL11–14 in `s01e01.md`.
- **Inherited loc-state:** assume Intent 1's entry fired at PL11 (gate-open, sept-yard at dawn).
- **What the move turns on:** the officer continues into the yard he just entered.

### Intent 13
- **Anchor:** s01e01 PL37 — `taylor steps into the path of the officer's shoulder`
- **Surrounding:** PL35–38 in `s01e01.md`.
- **Inherited loc-state:** sept-yard at dawn (assume one prior entry holds).
- **What the move turns on:** confrontation-blocking. Two actors narrowing the channel between them.

### Intent 14
- **Anchor:** s01e05 PL44 — `the steward spreads the scroll across the trestle`
- **Surrounding:** PL42–46 in `s01e05.md`.
- **Inherited loc-state:** village-common at morning (assume scene-anchor at PL40 holds — Intent 6 if accepted).
- **What the move turns on:** prop placement.

### Intent 15
- **Anchor:** s01e05 PL73 — `rowan walks the four paces to the trestle`
- **Surrounding:** PL71–75 in `s01e05.md`.
- **Inherited loc-state:** village-common at morning (assume scene-anchor and one state-change have fired earlier).
- **What the move turns on:** within-scene navigation.

### Intent 16
- **Anchor:** s01e02 PL21 — `the granary holds its three-week shape`
- **Surrounding:** PL18–22 in `s01e02.md`.
- **Inherited loc-state:** village-lane at morning, granary-exterior known.
- **What the move turns on:** Taylor reads the granary's accustomed shape from the lane.

### Intent 17
- **Anchor:** s01e06 PL94 — `the grey holds the road`
- **Surrounding:** PL92–96 in `s01e06.md`.
- **Inherited loc-state:** sept-nave-interior predawn (Taylor has just sealed herself inside; the feed has stopped at the door).
- **What the move turns on:** Taylor's perception of the dawn-grey on the road. Note: Taylor cannot directly perceive the road from inside the sealed nave — the channel has dropped.

### Intent 18
- **Anchor:** s01e06 PL67 — `a shod hoof strikes the cobbles half a league north`
- **Surrounding:** PL65–70 in `s01e06.md`.
- **Inherited loc-state:** sept-yard-wall predawn cold-clear.
- **What the move turns on:** auditory detection at distance.
- **Cards:** `cards/locations/loc-harrenhal-exterior.card.md`; `cards/conditions/cond-fauna-control-rules.card.md`.

---

End. Author all 19 (calibration C + intents 1–18).
