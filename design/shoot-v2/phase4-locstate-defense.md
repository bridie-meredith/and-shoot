---
phase: 4 (defense or revision)
author: studio
rubric-version: V2 locked (design/shoot-v2/rubric-location-state.md)
date: 2026-05-06
---

# Phase 4 — Location-State Defense / Revision

---

### Intent C

PHASE-3 SEAM: PL10's own SVO names the lantern and implies the half-league distance; the sensory note "amber smear at half league" re-states what the proto-line already establishes; strip test may pass on the line's own content.
ACTION: DEFEND

DEFENSE: The strip test is not satisfied by the proto-line alone because the proto-line operates as a rendered perception-line, not as a spatial fact the subsequent beats can inherit. The loc-state entry's job is to establish the Harrenhal exterior as a named, cited sub-location in a predawn cold-clear state with a single active light — this is what licenses PL11 ("the lantern reads as a smear at distance"), PL12 ("Harrenhal holds the one warmth in the field"), and PL13 ("taylor watches the smear through the bird") in inherited environment without re-firing. The proto-line names what Taylor perceives through the bird; the loc-state entry names what the location *is* — those are not the same information. The rubric's necessity ACCEPT signature explicitly covers "the first beat anchoring the bird's perception-channel at Harrenhal distance" as a new-location anchor; that is this entry's job, and PL10 is the beat where it fires.

---

### Intent 1

PHASE-3 SEAM: The conditions slot carries `cond-impressment-census-120ac` — a political/administrative condition slug, not an observable physical state; conditions slot is location-state, not administrative context.
ACTION: REVISE

The seam is load-bearing. `cond-impressment-census-120ac` is a card-slug for an off-stage legal authorization, not a perceptible physical state the body encounters at the gate threshold. The conditions-slot examples throughout the rubric are all body-perceptible: `door-shut`, `lantern-on-far-wall`, `mud-recent`. An impressment-census authorization is not something an actor runs into with the foot or reads with the eye at the gate — it is a legal context. The seam correctly identifies this as form-contamination. The entry still fires on necessity and interestingness grounds; the fix is to drop `cond-impressment-census-120ac` from conditions and, if the census context needs a home, route it to the state-updates or vibes facet.

Note on slug accuracy: `oc-sept-yard` does not appear in the locations INDEX. The authored card `loc-harrenhal-sept-environs` covers the yard-between-buildings as a named sub-zone ("the yard between buildings: hard-packed earth... enclosed on three sides"). Option (a) applies: replace `oc-sept-yard` with `loc-harrenhal-sept-environs` and localize within it using conditions.

DRAFT-A: 1 @s01e01-pl11 loc-harrenhal-sept-environs | morning | none | gate-open | gate threshold, packed-dirt yard beyond
DRAFT-B: 1 @s01e01-pl11 loc-harrenhal-sept-environs | morning | none | gate-open, yard-empty | officer's entry through the timber gate
DRAFT-C: 1 @s01e01-pl11 loc-harrenhal-sept-environs | morning | none | gate-open | packed dirt past the gate-threshold

CHOSEN: A
REJECTED: DRAFT-B — "yard-empty" is actor-state (absence of bodies is an inferred social condition, not an observable location physical state); "officer's entry through the timber gate" paraphrases the anchor verb rather than pointing at the location fact. DRAFT-C — "packed dirt past the gate-threshold" is marginally weaker than Draft-A; it elides the "gate threshold" as the specific focus-element in favor of describing what's on the far side; the threshold itself is the perceptible thing the crossing turns on.
SEAM-ANSWERED: The conditions slot now carries only the observable physical state (gate-open); the administrative-context slug is removed; the slug is corrected to an authored indexed card.
SIGNATURES:
- necessity: PL11 is the episode-open movement anchor; officer entering through the gate; strip test fails — no spatial ground for PL14 or the line-up at PL15–20 without an established location-and-state.
- interestingness: one focus-element — the gate threshold with the packed-dirt yard behind it; this is the specific perceptible thing the entry-verb turns on; it is new, not inherited.
- frugality: no prior entry in this episode; scene-anchor; licenses all subsequent yard beats until next state-change.

---

### Intent 2

PHASE-3 SEAM: No prior loc-state entry in the Phase 2 corpus establishes a `door-shut` state for the granary; the frugality defense cites a ghost prior entry at PL9; the previous-entry test has no real prior entry to compare against.
ACTION: REVISE

The seam is partially load-bearing on the frugality justification but does not overturn the necessity or interestingness claims. The Phase 2 output declared "INHERITED: granary-exterior door-shut (assumed established at PL9)" — but PL9 reads "plumms-man steps forward," which is not a door-state anchor. There is no prior cited loc-state for the granary exterior in this corpus. The consequence: the entry cannot claim "records state-change since the last cited entry" — instead it is the *first* cited entry for this sub-location, and it fires on the new-location first-beat exception (PL10 is Plumm's-man arriving at the granary door, which is a new sub-location anchor). The frugality justification needs correction; necessity and interestingness survive intact.

Note on slug accuracy: `oc-granary-exterior` does not appear in the locations INDEX. The granary is described on `loc-harrenhal-sept-environs` ("a small wood store" and "a low shed that has been used at various points for animals, storage, and as overflow sleeping space") — this is functionally the granary-exterior zone. Option (a) applies: replace `oc-granary-exterior` with `loc-harrenhal-sept-environs`, using conditions to localize.

DRAFT-A: 2 @s01e02-pl10 loc-harrenhal-sept-environs | morning | none | granary-door-open | swept granary floor past the threshold
DRAFT-B: 2 @s01e02-pl10 loc-harrenhal-sept-environs | morning | none | door-open, granary-sub | swept floor revealed by the opened door
DRAFT-C: 2 @s01e02-pl10 loc-harrenhal-sept-environs | morning | none | granary-door-open | granary threshold, swept floor inside

CHOSEN: A
REJECTED: DRAFT-B — "granary-sub" in the conditions slot is a zone-descriptor, not an observable physical state; the conditions slot must record perceptible conditions, not location taxonomy. DRAFT-C — "granary threshold, swept floor inside" names two elements in the sensory note; must pick one; the swept floor is the more load-bearing because it is what PL12 and PL14 depend on.
SEAM-ANSWERED: Frugality justification is corrected — this is the new-location first-beat anchor for the granary sub-zone (not a state-change from a ghost prior entry); slug corrected to indexed card with conditions localizing the sub-zone.
SIGNATURES:
- necessity: PL10 is the first movement beat at the granary door; the opening reveals the interior; Plumm's-man's crouch at PL12 and reach at PL14 both require established aperture and visible floor; strip test fails.
- interestingness: one focus-element — the swept granary floor; new information revealed by the door's opening; selected over the doorway geometry itself.
- frugality: first cited entry for this sub-location in this episode; new-location anchor; licenses subsequent granary beats.

---

### Intent 3

PHASE-3 SEAM: `oc-sept-nave-arch` does not appear in the locations INDEX; using `oc-` does not automatically create an indexed card; the slug reference is unresolvable.
ACTION: REVISE

The seam is correct and load-bearing on form. `oc-sept-nave-arch` is not in the locations INDEX. The authored card `loc-harrenhal-sept-environs` covers the nave ("single nave, five-pointed star carved above the door... the interior floor is cracked stone") and the sept's internal zones including the chancel and side alcoves. The arch threshold is a sub-zone of the nave entry — it falls under `loc-harrenhal-sept-environs`. Option (a) applies: replace slug with `loc-harrenhal-sept-environs`, use conditions to localize.

The sensory note "arch threshold distinct from side door" also carries a mild form concern (the "distinct from side door" clause is explanatory, not purely perceptible — the Phase 2 audit noted this as marginal). The revision addresses both.

DRAFT-A: 3 @s01e03-pl12 loc-harrenhal-sept-environs | morning | none | arch-open, rushes-underfoot | nave arch threshold
DRAFT-B: 3 @s01e03-pl12 loc-harrenhal-sept-environs | morning | none | arch-open, rushes-underfoot | the arch opens on rushes
DRAFT-C: 3 @s01e03-pl12 loc-harrenhal-sept-environs | morning | none | nave-arch-open, rushes-underfoot | arch threshold, rush-floor beneath

CHOSEN: B
REJECTED: DRAFT-A — "nave arch threshold" is architectural naming without a perceptible fact; it describes the element's identity, not what the crossing turns on. DRAFT-C — "arch threshold, rush-floor beneath" is two elements in the sensory note; must pick one; the rush-floor is the more load-bearing tactile fact (it is what the foot encounters on crossing the arch, and it distinguishes this zone from the flagstone entry area).
SEAM-ANSWERED: Slug replaced with indexed card `loc-harrenhal-sept-environs`; conditions localize to the arch-open + rushes-underfoot state; sensory note now names one perceptible focus-element without the explanatory "distinct from side door" clause.
SIGNATURES:
- necessity: three bodies cross the arch threshold at PL12; this is a distinct zone-boundary from the side-door area Taylor has held since PL2; new sub-location anchor is warranted; strip test fails — without this entry, reader cannot distinguish which threshold the inspection party breaches.
- interestingness: one focus-element — the rushes underfoot as the arch opens on them; this is new tactile information, the first tactile fact of the nave-proper as opposed to the stone doorframe Taylor has held at.
- frugality: first entry for the nave arch zone in this episode; the prior inherited state covers only Taylor's position at the side-door frame; this entry licenses the subsequent nave beats for the inspection party.

---

### Intent 4

PHASE-3 SEAM: The inherited state cites "sept-chancel at predawn, cold (alcove-warmth-gone), candle-on-table" but no such entry appears in the Phase 2 corpus; the first term of the interior/exterior differential (alcove-warmth-gone) has never been formally cited; "cold air at the threshold" may not be new information if interior warmth was never established.
ACTION: DEFEND

The seam misreads what the entry needs to accomplish. The interestingness axis asks whether the sensory note names "new information at this anchor" — new relative to the prior loc-state in the same scene, not relative to a full interior-warmth chain. The prior inherited state for this scene (predawn, chancel location) would have been established at the scene-open, whether or not that specific entry appears in the 19-intent sample; studio is authoring against the episode's full proto-line sequence, not only the sampled intents. The seam's attack — that the interior warmth was never formally registered — does not speak to whether "cold air at the threshold" is new information at PL56's anchor beat; the door was shut until PL56 by the plain text of the proto-line ("taylor opens the side door" at PL56, followed by "the cold arrives" at PL57). The door-shut state is what the scene has inherited since the chancel-entry; the door opening at PL56 is a genuine state-change — door-shut → door-open — and the cold air at the threshold is the new, specific perceptible thing that change delivers. The rubric's necessity ACCEPT signature covers "door-state changes from shut to open; PL57 'the cold arrives' requires established aperture"; this entry does that work. The seam does not identify a rubric violation; it identifies a gap in the sampled-corpus's prior entries, which is a corpus-sampling gap, not a facet-entry fault.

Note on slug accuracy: `oc-sept-side-door` is not in the locations INDEX. The side door is a feature of `loc-harrenhal-sept-environs` ("the chancel... the yard between buildings"). The slug should be corrected to `loc-harrenhal-sept-environs` with conditions localizing to the side-door boundary — but this is a form correction, not a seam-driven content revision. Recording it here for completeness; the slug repair is the same fix as Intents 1, 2, 3.

---

### Intent 5

PHASE-3 SEAM: (FIRE-INCORRECT per Phase 2 audit — confirmed revise.) Chosen Draft-A carries `channel-reindexed` in the conditions slot — the same interiority defect the audit cited against Draft-C. The draft-selection process did not apply the conditions-slot rule uniformly.
ACTION: REVISE

This is the FIRE-INCORRECT case from Phase 2. Both faults are confirmed: (1) the sensory note "nave interior, yard drops off the plane" has two focus-elements; (2) the conditions slot carries `channel-reindexed`, which is actor-internal perceptual state, not an observable location condition. Draft-A was the worst available choice and was chosen — this is a selection error.

The correct approach: the entry fires on Taylor crossing from exterior (cold-clear yard) to interior (nave) at PL72. The operative location fact is the door closing behind her, which seals the exterior. The single focus-element is the sealed interior — specifically, the door standing closed behind her, which is what the location now shows. `channel-reindexed` belongs in the state-updates or feeling facet.

Note on slug accuracy: `oc-sept-nave-interior` is not in the locations INDEX. `loc-harrenhal-sept-environs` covers the nave. Option (a) applies.

DRAFT-A: 5 @s01e06-pl72 loc-harrenhal-sept-environs | predawn | none | door-shut-behind, nave-dark | door closed behind her, yard gone
DRAFT-B: 5 @s01e06-pl72 loc-harrenhal-sept-environs | predawn | none | door-shut-behind | the door stands closed, nave interior
DRAFT-C: 5 @s01e06-pl72 loc-harrenhal-sept-environs | predawn | none | door-shut-behind | closed door between nave and yard

CHOSEN: C
REJECTED: DRAFT-A — "door closed behind her, yard gone" is two focus-elements and introduces a subjective framing ("yard gone" is interior perception, not location state); "nave-dark" in conditions adds an atmospheric condition that does little additional work and edges toward mood-painting. DRAFT-B — "the door stands closed, nave interior" names two things — the door's state and the zone — and uses the article "the" which reads as description rather than a schema field value; less crisp than Draft-C.
SEAM-ANSWERED: No `channel-reindexed` in conditions slot — actor's perceptual reindexing is removed entirely; sensory note names one focus-element (the closed door between nave and yard); both Phase 2 audit faults are resolved; slug corrected to indexed card.
SIGNATURES:
- necessity: Taylor crosses from yard to nave-interior at PL72 and closes the door; without this entry the inherited state (yard predawn cold-clear) would persist into PL74–91 nave beats; strip test fails.
- interestingness: one focus-element — the closed door between nave and yard; this is the specific location fact the crossing turns on; it is what seals the exterior and changes what the subsequent beats inherit.
- frugality: new sub-location (nave interior vs. yard exterior); the prior entry held the yard; this is the first interior entry in this episode; licenses PL74–91.

---

### Intent 6

PHASE-3 SEAM: PL40 "three women stand along the kiln wall" is a stillness/hold beat, not a transitional or positioning verb; the necessity REJECT signature covers hold-beats; the new-location first-beat exception does not override the hold-beat restriction.
ACTION: DEFEND

The seam misreads the rubric's scope for the new-location first-beat exception. The necessity axis REJECT signature ("anchor is a stillness/hold beat") applies to beats within an established location where the movement is absent — the concern is that firing on a hold beat would be parasitic because the location is already established and the hold adds nothing. The new-location first-beat exception exists precisely for cases where *no prior entry* covers this location, and the scene-anchor must be placed at the first beat where the new location can be cited. PL40 is Taylor's first beat at the village-common — she arrives, and PL40 is the first thing she perceives there. The question the rubric asks of a new-location first-beat entry is not "is there a transitional verb?" but "does the entry establish spatial ground without which subsequent beats cannot resolve?" Strip test: remove the entry; PL44 (trestle), PL42 (bench), and PL73 (Rowan's four-pace crossing) have no inherited spatial ground for the common at all. That is the strip-test failure for a new-location anchor, and the rubric explicitly provides for it: "a non-movement beat earns an entry only if it is the *first* beat in a new location-and-moment (entry serves as place-anchor for subsequent inherited beats)." Three women standing along the kiln wall is the first observable thing at the common; the hold-beat restriction is inapplicable when the location itself is new.

---

### Intent 7

PHASE-3 SEAM: "South face of the sept wall at the yard" is a fixed geometric fact about the wall (location-card content), not a perceptible state the move turns on; under the herald/cart heuristic, a wall's south face is a cart, not a herald.
ACTION: REVISE

The seam is load-bearing on interestingness. The rubric's herald/cart heuristic distinguishes between things that *are* location-card content (fixed geometry) and things that constitute a perceptible state because an actor's positioning *at* that thing activates it. The wall's south face is fixed geometry; PL1 is Taylor already at the wall (the anchor reads "the stone holds the cold against taylor's back" — a hold beat, not a crossing). The sensory note "south face of the sept wall at the yard" describes a fixed architectural fact rather than a perceptible state the move turns on.

However, the entry's necessity claim is sound: this is the episode-open scene-anchor for PL1–71; without any first entry the entire predawn watch sequence is spatially unanchored. The fix is to the sensory note: replace the architectural description with a perceptible fact the wall delivers at this beat that is *not* location-card content — specifically the cold the stone transmits, which is what PL1 names and what PL25 ("the wall takes the measure of taylor's warmth") and PL2 ("taylor holds the wall-weight at the hip") depend on.

Note on slug accuracy: `oc-sept-yard-wall` is not in the locations INDEX. The wall is a feature of `loc-harrenhal-sept-environs` (the yard's low stone wall; the building walls enclosing the yard on three sides). Option (a) applies.

DRAFT-A: 7 @s01e06-pl1 loc-harrenhal-sept-environs | predawn | cold-clear | frost-ground | cold stone at the back
DRAFT-B: 7 @s01e06-pl1 loc-harrenhal-sept-environs | predawn | cold-clear | frost-ground | the wall delivers cold through the linen
DRAFT-C: 7 @s01e06-pl1 loc-harrenhal-sept-environs | predawn | cold-clear | frost-ground | stone-cold at the contact point

CHOSEN: A
REJECTED: DRAFT-B — "the wall delivers cold through the linen" starts to become description; the article "the" and the prepositional "through the linen" are prose-tending; the sensory note should be a field value, not a sentence. DRAFT-C — "stone-cold at the contact point" is less specific than Draft-A; "contact point" is vague; "at the back" from PL1's SVO ("the stone holds the cold against taylor's back") is the specific perceptible location.
SEAM-ANSWERED: Sensory note no longer names a fixed geometric fact (south face); it names the cold the stone delivers at the specific contact point — a perceptible state the wall-lean turns on; slug corrected to indexed card.
SIGNATURES:
- necessity: episode-open scene-anchor; PL2 ("taylor holds the wall-weight at the hip"), PL5 ("taylor holds the line from the wall to the post"), and PL25 ("the wall takes the measure of taylor's warmth") all require an established wall-position; strip the entry and the episode opens spatially and thermally unanchored.
- interestingness: one focus-element — the cold the stone delivers at the back; this is the specific perceptible thing the wall-lean turns on; it is new at episode-open; it is what makes the wall more than architecture (it is a thermal event).
- frugality: no prior entry; episode-anchor; licenses PL1–71 in inherited environment until a state-change fires.

---

### Intent 8

PHASE-3 SEAM: The sensory note "second lantern kindles beside the first" paraphrases what PL34 already states ("a second amber bleed lights beside the first"); the rubric rejects re-naming features already established by the prior loc-state or the anchor line itself.
ACTION: DEFEND

The seam misapplies the "re-naming" REJECT signature. That signature targets re-naming a feature established by "location card or prior loc-state entry" — not by the anchor proto-line itself. The anchor proto-line is a rendered perception-line; it is what the impersonator produces. The loc-state entry is a facet-level fact record. The entry's job is not to add new prose information beyond the proto-line; it is to record the state-change at the Harrenhal exterior (light count: one → two) so that PL35 ("a third light kindles at the road's end") has a prior-state to fire against. If the loc-state entry were absent, PL35's state-change ("a third light") would have no prior count to be "third" against in the facet layer. The seam conflates "information the reader already has from the prose" with "information the facet layer already has from a prior cited loc-state" — these are different registers. The rubric's previous-entry test asks: would this entry render identically in inherited state? The inherited state from PL10 has one light; this entry records two. That is a genuine state-change in the facet layer, regardless of what the prose line says.

---

### Intent 9

PHASE-3 SEAM: PL54 ("the bar lifts halfway out of the brackets") is the immediately preceding proto-line; the sensory note "bar half-out of the brackets" re-names what PL54 already established as its own SVO; this may be inherited from PL54 rather than new at PL55.
ACTION: DEFEND

The seam confuses proto-line order with loc-state inheritance. PL54 is a proto-line — a rendered action-line — not a loc-state entry. The loc-state layer does not inherit from proto-lines; it inherits from prior cited loc-state entries. The previous-entry test is: "compare against the last accepted loc-state in the same scene" — the last accepted entry is Intent 8 at PL34, which recorded `gatehouse-two-lights`. Neither `gate-parting` nor `bar-half-out` appears in that entry or in the inherited state it licenses. PL54's SVO ("the bar lifts halfway out of the brackets") is a prose action-line; it does not constitute a loc-state citation. The loc-state entry at PL55 is the first place the gate-parting state is formally recorded in the facet layer, and that record is what PL60 ("the gate opens outward") depends on for a prior-state contrast. The seam's logic — that a proto-line's SVO establishes location state — would mean no loc-state entry could ever fire at the same beat a proto-line describes the relevant action. That would eliminate most warranted entries, which is not the rubric's intent.

---

### Intent 10

PHASE-3 SEAM: `oc-drying-yard` does not appear in the locations INDEX; the slug reference is unresolvable.
ACTION: REVISE

The seam is correct and decisive on form. `oc-drying-yard` is not indexed. The drying yard is a smallfolk-village space — the `westerosi-smallfolk-village-common` card covers "drying yards / lanes" in its smallfolk-village context (the card covers the village common and its immediate surrounding functional spaces including kitchen gardens at field borders). However, looking at the card more carefully: the common card's scope is "the central outdoor space... where the village gathers" for collective authority occasions — not a private drying yard. The s01e02 drying yard, based on the proto-line context (Taylor stopping at a rack of chamomile, s01e02-pl86, in what appears to be the sept environs area given the lane established at PL17 "the lane opens around Taylor"), is more plausibly a yard adjacent to the sept than a village common. `loc-harrenhal-sept-environs` covers the area around the sept buildings including the kitchen garden against the south wall of the cottage and the road approach. This is Option (c) territory: the specific drying yard is a project-original sub-zone not explicitly named in any indexed card — but `loc-harrenhal-sept-environs` is close enough to serve as parent slug (Option (a)), with conditions localizing to the rack/drying context. Flagging for margit: a dedicated `oc-sept-drying-yard` or `oc-sept-outbuildings-yard` sub-zone card may be warranted if this location recurs.

DRAFT-A: 10 @s01e02-pl86 loc-harrenhal-sept-environs | morning | clear | chamomile-drying, rack-at-yard | chamomile on the rack
DRAFT-B: 10 @s01e02-pl86 loc-harrenhal-sept-environs | morning | clear | drying-rack-active | chamomile on the rack
DRAFT-C: 10 @s01e02-pl86 loc-harrenhal-sept-environs | morning | clear | rack-in-drying-yard | chamomile at the rack's height

CHOSEN: B
REJECTED: DRAFT-A — "rack-at-yard" is a redundant location descriptor; the conditions slot shouldn't double as a location identifier when the slug already carries the parent zone. DRAFT-C — "chamomile at the rack's height" specifies the height rather than the chamomile itself; the chamomile is the load-bearing focus-element (PL88 names it directly), not the rack's elevation.
SEAM-ANSWERED: Slug corrected to indexed card `loc-harrenhal-sept-environs`; conditions localize to the drying-rack-active state; form fault resolved; margit flag noted.
SIGNATURES:
- necessity: Taylor arrives at a new sub-location (the drying-rack yard) on physical contact with the rack at PL86; new-location anchor; PL87 and PL88 both require established sub-location; strip test fails.
- interestingness: one focus-element — chamomile on the rack; this is what physical contact delivers; the specific perceptible thing the "takes Taylor's shoulder" moment turns on; new (the lane did not have chamomile).
- frugality: first cited entry for this sub-location in this episode; new-location anchor; licenses PL87–88.

---

### Intent 11

PHASE-3 SEAM: "steps in the seam" is a positioning verb; the seam-at-hip-level is a specific sub-element not covered by the PL1 anchor; rubric does not categorically exclude animal positioning beats; the perception-feed classification may be over-applied.
ACTION: NONE-CONFIRMED

DEFENSE: The seam correctly identifies that "steps in the seam" is a positioning verb — but the rubric's necessity axis asks whether the *actor's (or salient object's) movement* depends on a *location fact*. The mouse moving in a wall-seam at hip height does not depend on a location fact the reader lacks; the wall-seam is a feature of the sept wall that PL1's scene-anchor already licenses (the wall holds many seams — that is location-card content per the sept-environs card's description of the stone construction). The seam's strongest argument is that hip-level specificity is new sub-element information, but the rubric's herald/cart heuristic applies here: the seam-in-the-wall is a static architectural feature (a cart, not a herald) — the mouse moving through it is what PL19 renders, and that is a perception-feed event at an established location, not a state-change in the location itself. PL1's scene-anchor licenses the wall and its sub-features at this location; the mouse's arrival is a fauna-event resolved in inherited environment. The rubric §1 REJECT signature "interiority pushed into physical SVO (perception-feed beats per Phase 0 note #1)" applies: Taylor perceiving a mouse-shape in the seam is a perception-feed event, not a location state-change.

---

### Intent 12

PHASE-3 SEAM: PL12 places an actor at "the center of the yard" — a specific spatial coordinate that subsequent crossing and line-formation beats reference geometrically; the center-point may be a new sub-feature warranting an entry.
ACTION: NONE-CONFIRMED

DEFENSE: The officer's position at the center of the yard is actor-state, not location-state. The center-of-the-yard is a geometric property of the yard itself (inherited from the PL11 scene-anchor, which licenses the full yard space); it is not a new environmental condition that the location introduces. The rubric's §3 frugality ACCEPT signature requires "a state-change since the last cited loc-state (door opens, light shifts, weather changes, new entrant changes the focus-element)." The officer stepping to the center does not change any of those: door state is unchanged, light is unchanged, weather is unchanged, and "new entrant changes the focus-element" refers to an entrant changing what the location presents — not an already-present actor repositioning within the established yard. The PL11 scene-anchor establishes the gate-threshold and packed-dirt yard; the yard's geometric center is already within that established space. Firing an entry for every actor movement to a named yard-position would violate frugality (anti-pattern 4, inherited re-naming).

---

### Intent 13

PHASE-3 SEAM: If PL37 precedes PL14 in read-order, the "twelve feet of packed dirt" inherited justification fails; the channel-narrowing at PL37 may not have been formally established.
ACTION: NONE-CONFIRMED

DEFENSE: PL37 does not precede PL14. The proto-line file for s01e01 shows the sequence clearly: PL14 ("taylor crosses the twelve feet of packed dirt"), PL15 ("taylor enters the line"), ... PL37 ("taylor steps into the path of the officer's shoulder"). PL37 is a later beat in the same scene, not an earlier one. The seam's strongest attack — "if PL37 precedes PL14 in read-order" — is contingent on a sequence the file does not show. PL14 establishes "twelve feet of packed dirt" as a named spatial fact within the inherited scene, and PL37's actor-positioning ("steps into the path of the officer's shoulder") is a subsequent beat that resolves in that inherited spatial ground. The channel-narrowing at PL37 is two actors repositioning relative to each other within an established twelve-foot span — that is actor-state, not a location state-change. The yard holds its shape; the actors reposition within it.

---

### Intent 14

PHASE-3 SEAM: `authority-day-configuration` in the conditions slot of Intent 6 does not explicitly name the trestle; the trestle may not be a formally inherited condition; the steward spreading the scroll at PL44 could introduce the trestle as a newly active location element.
ACTION: NONE-CONFIRMED

DEFENSE: The seam depends on `authority-day-configuration` failing to establish the trestle as a present element — but the `westerosi-smallfolk-village-common` card explicitly describes "benches or trestles stacked against the wall when not in use" and its movement-pattern note states "on authority-day (tax collection, knight's visit, naming-census): the village contracts. People gather but maintain two body-lengths from whoever is conducting the authority business." The trestle is the canonical furniture of authority-day on a common; it is part of what authority-day-configuration means. Intent 6's conditions slot fires `authority-day-configuration` at the scene-anchor — a reader who inherits that condition also inherits the trestle's presence, because the trestle is what authority-day deploys. PL44's steward spreading the scroll across the trestle is a prop-placement action at an already-present location feature, not an introduction of a new location element. Routing to state-updates facet is correct.

---

### Intent 15

PHASE-3 SEAM: Rowan arriving at the trestle side re-configures the trestle's social geometry (sight-line change); sight-line changes are location-dependent facts; the rubric allows "new entrant changes the focus-element."
ACTION: NONE-CONFIRMED

DEFENSE: The "new entrant changes the focus-element" warrant applies when a new entrant physically changes what the location presents — not when an actor moves within an already-established space and creates a social arrangement. Rowan walking four paces to the trestle does not change the location; the trestle is already established, the common is already established, the bench-and-trestle geometry is already established. The sight-line re-arrangement the seam describes (maester on far side, Taylor seated, Rowan arriving at Taylor's side) is a social-actor configuration change, not a location state-change. The four-paces distance is established by the proto-line itself ("rowan walks the four paces to the trestle" — the distance is in the anchor). The rubric's frugality test: this would render identically in inherited state from the Intent 6 scene-anchor. Anti-pattern 4 (inherited re-naming of the common for a movement within it) correctly applies.

---

### Intent 16

PHASE-3 SEAM: "The granary holds its three-week shape" may be a specific observable condition Taylor reads as she passes — a first-encounter perception beat for this observable; extending the new-location first-beat exception to first-encounter perception.
ACTION: NONE-CONFIRMED

DEFENSE: The seam's strongest form is that PL21 is a first-encounter perception of an observable condition. But the rubric's necessity axis is explicit: location-state fires on *movement, positioning, or physical-action beats* whose legibility depends on a location fact. PL21 is neither — it is an environmental persistence beat, the exact content of anti-pattern 3. The proposed extension of the new-location first-beat exception to "first-encounter perception beats" is not in the rubric and would substantially expand the exception's scope. The seam itself acknowledges this argument "requires extending the new-location exception to a context it was not designed for." Strip test: Taylor continues walking at PL22 without any spatial fact from PL21; the granary's shape is not required for any subsequent beat's legibility. NONE stands.

---

### Intent 17

PHASE-3 SEAM: PL94 ("the grey holds the road") could be a narrator-camera cut to the exterior rather than Taylor's POV; if omniscient-narrator, the imperceptibility argument doesn't apply.
ACTION: NONE-CONFIRMED

DEFENSE: PL94 is Taylor-POV. The proto-line file for s01e06 establishes the consistent POV throughout: Taylor is inside the sealed nave after PL73, PL91–93 explicitly name the instrument stopping ("the feed stops at the door," "the closing took the instrument dark"), and PL94 ("the grey holds the road") follows immediately. In this episode's POV construction, "the grey holds the road" is Taylor's interior knowledge of what the road holds — the memory or inference that the road is still there in its grey predawn state — not a narrator cut. PL95 ("a man on the road can be read at distance") and PL96 ("the window closes on the room") continue in the same interior-reflective register. The episode does not shift to omniscient narrator at PL94; it continues Taylor's interior assessment of what she cannot currently perceive. Firing a loc-state entry for an exterior location the POV character cannot reach through any active perception-channel is a contradiction of the necessity axis. NONE stands on two independent grounds: imperceptibility and persistence-not-change.

---

### Intent 18

PHASE-3 SEAM: PL67 ("a shod hoof strikes the cobbles half a league north") is the first auditory confirmation that the Harrenhal exterior now has a rider in motion on cobbles; prior entries established lantern-states and gate-parting, not that a horse is on cobbles; this may be a new condition at loc-harrenhal-exterior under the "new entrant changes the focus-element" warrant.
ACTION: NONE-CONFIRMED

DEFENSE: The "new entrant changes the focus-element" warrant applies to the *location's state* changing because of an entrant — it does not apply to every event a character auditorily detects from an established remote location. PL67 is not a movement beat at loc-harrenhal-exterior; it is an auditory detection beat at Taylor's current location (the sept-yard-wall). The rider on cobbles does not change the location-state entry for the yard-wall, and the rider's location (Harrenhal cobbles) is already established in the inherited harrenhal-exterior state (the cobbles are a fixed feature of the gatehouse exterior; the prior entries cover that station from PL10 through PL55). The seam's distinction — that prior entries covered lanterns and gate-parting but not a horse on cobbles — conflates "new event at an established location" with "new location state." A new rider sound at an established remote location is not a state-change requiring a new entry; it is a perception-feed event resolved in inherited environment. The gate-parting at PL55 licenses the cobble-contact at PL67: the gate opened, a horse would exit onto cobbles, and that exit is the next step in the inherited state sequence. A new loc-state entry is not required for Taylor to perceive the consequence of the gate's opening. NONE stands.

---

## Phase 4 Summary

### Slugs to correct (all Option (a) — replace with `loc-harrenhal-sept-environs`)

All `oc-sept-*` slugs in the corpus are sub-zones of `loc-harrenhal-sept-environs`. Affected intents: 1, 2, 3, 4, 5, 7. Intent 10's `oc-drying-yard` also maps to `loc-harrenhal-sept-environs` as closest parent (margit flag: consider authoring `oc-sept-outbuildings-yard` if the drying-yard recurs as a distinct operational location).

### Confirmed revises: 1, 2, 3, 5, 7, 10 (six entries)

### Confirmed defends: C, 4, 6, 8, 9 (five entries)

### Confirmed NONE: 11, 12, 13, 14, 15, 16, 17, 18 (eight entries)

### Intent 4 note

Phase 3 seam on Intent 4 is defended on content grounds. However the slug `oc-sept-side-door` requires the same correction as the other `oc-sept-*` slugs: replace with `loc-harrenhal-sept-environs`, localize in conditions. This is a form-only repair, not a content revision — the entry as written (minus the slug) is defensible. Recording the correction here; the cleaned form entry would be:

`4 @s01e04-pl56 loc-harrenhal-sept-environs | predawn | none | side-door-open, exterior-cold | cold air at the threshold`
