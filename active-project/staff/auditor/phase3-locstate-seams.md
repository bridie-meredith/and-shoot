---
phase: 3 (adversarial seam-finding)
author: auditor
task: one hostile counter-argument per Phase 2 entry — defense scaffolding, not verdict overturns
rubric-version: V2 locked (design/shoot-v2/rubric-location-state.md)
prior-audit: active-project/staff/auditor/phase2-locstate-audit.md
date: 2026-05-06
---

# Phase 3 — Location-State Adversarial Seams

---

### Intent C

ENTRY/DECISION: FIRE — `C @s01e06-pl10 loc-harrenhal-exterior | predawn | cold-clear | gatehouse-lantern-on | amber smear at half league`
SEAM TYPE: strip
LENS: selection-skeptic

SEAM: PL10 reads "the gatehouse lantern bleeds amber at half a league" — the proto-line itself names the lantern and implies the half-league distance. The strip test as applied argues the reader lacks "ground-truth for what scale 'half a league' resolves into," but the proto-line's own SVO carries both the focus-element (the amber bleed) and the distance directly; the sensory note "amber smear at half league" re-states what the line already establishes. Under the rubric's strip-test definition — "if the proto-line still resolves cleanly without it, REJECT" — PL10 is one of the more self-sufficient lines in the corpus. The defense must explain why the strip test genuinely fails here and does not merely confirm the line's own content.

---

### Intent 1

ENTRY/DECISION: FIRE — `1 @s01e01-pl11 oc-sept-yard | morning | none | gate-open, cond-impressment-census-120ac | gate threshold, packed-dirt yard beyond`
SEAM TYPE: anti-pattern-proximity
LENS: form-skeptic

SEAM: The conditions slot carries `cond-impressment-census-120ac` — a condition card slug referencing a named political/administrative condition rather than an observable physical state of the location. The rubric's conditions-slot examples are all perceptible physical states: `door-shut, lantern-on-far-wall, mud-recent`. A census-authorization card slug is not a perceptible environmental condition an actor can encounter with the body; it is an off-stage legal fact. This brushes anti-pattern 5 (plan-bullet residue) — the conditions slot becomes a vehicle for contextual scene-metadata rather than observable physical state. The form-skeptic challenge: conditions slot is location-state, not administrative-context; `cond-impressment-census-120ac` belongs in a state-updates or vibes facet, not here.

---

### Intent 2

ENTRY/DECISION: FIRE — `2 @s01e02-pl10 oc-granary-exterior | morning | none | door-open | swept granary floor past the threshold`
SEAM TYPE: inheritance
LENS: inheritance-skeptic

SEAM: The Phase 2 entry declares "INHERITED: granary-exterior door-shut (assumed established at PL9)" — but the proto-line file for s01e02 shows PL9 as "plumms-man steps forward," not a door-state anchor. No prior entry in the Phase 2 corpus establishes a `door-shut` state for this granary in this episode: the inherited state cited is an assumption, not a cited prior entry. Under the previous-entry test — "compare against the last accepted loc-state in the same scene" — there is no last accepted loc-state to compare against, meaning the frugality defense ("records a state-change since the last entry at PL9") is vacuous. The entry may still pass necessity and interestingness, but the frugality justification rests on a ghost prior entry.

---

### Intent 3

ENTRY/DECISION: FIRE — `3 @s01e03-pl12 oc-sept-nave-arch | morning | none | arch-open, rushes-underfoot | arch threshold distinct from side door`
SEAM TYPE: slug-accuracy
LENS: form-skeptic

SEAM: The location slug used is `oc-sept-nave-arch`. The locations INDEX lists `loc-harrenhal-sept-environs` and `westerosi-smallfolk-dwelling-interior` but no `oc-sept-nave-arch` — this slug does not appear in the authored card library. The rubric requires `<location-slug>` to be "slug of an authored location card (or `oc-…` for project-original)," but using `oc-` does not automatically create a card; margit must have indexed it. If `oc-sept-nave-arch` is not indexed as an authored card, the entry carries an unresolvable slug reference. Additionally, `oc-sept-yard` (Intent 1) is also absent from the INDEX, suggesting a systematic gap between the `oc-` slugs used in these entries and the actual library — a form fault that may apply to multiple entries.

---

### Intent 4

ENTRY/DECISION: FIRE — `4 @s01e04-pl56 oc-sept-side-door | predawn | none | door-open, exterior-cold | cold air at the threshold`
SEAM TYPE: anti-pattern-proximity
LENS: inheritance-skeptic

SEAM: The inherited state is described as "sept-chancel at predawn, cold (alcove-warmth-gone), candle-on-table" — but neither `oc-sept-chancel` nor the alcove-warmth-gone condition appears as an accepted entry in the Phase 2 corpus. The inheritance chain is cited as though a prior entry established these conditions, but no such entry exists in the 19 sampled intents. This means the necessity defense — "the differential between the interior alcove-warmth-gone and exterior-cold is what PL57 names" — relies on an environmental differential whose first term has never been established in a loc-state entry. The entry fires on a contrast that is one-sided: exterior-cold is established here, but interior-warmth-gone was never formally registered. The rubric requires the sensory note to name "new information at this anchor" — but is "cold air at the threshold" genuinely new if neither the interior warmth nor its absence has been cited?

---

### Intent 5

ENTRY/DECISION: FIRE-INCORRECT — `5 @s01e06-pl72 oc-sept-nave-interior | predawn | none | door-shut-behind, channel-reindexed | nave interior, yard drops off the plane`
SEAM TYPE: anti-pattern-proximity
LENS: form-skeptic

SEAM: The prior audit already called FIRE-INCORRECT on this entry, finding both a two-element sensory note and interiority in the conditions slot. The strongest residual seam — one the defense must address even when agreeing with the rejection — is that the chosen draft A is the worst of the three options rather than merely imperfect. Draft C's `channel-reindexed` is clearly interiority, and the audit properly rejected that; but Draft A carries `channel-reindexed` in the conditions slot as well ("door-shut-behind, channel-reindexed"), inheriting the same defect the audit cited against Draft C. The defense must explain how a draft containing the same conditions-slot fault as a rejected draft was chosen as the studio's output — this suggests the draft-selection process did not apply the conditions-slot rule uniformly.

---

### Intent 6

ENTRY/DECISION: FIRE — `6 @s01e05-pl40 westerosi-smallfolk-village-common | morning | none | kiln-wall, authority-day-configuration | kiln wall at the common's margin`
SEAM TYPE: focus-element
LENS: selection-skeptic

SEAM: The sensory note names "kiln wall at the common's margin" as the focus-element on the grounds that it is "where the three women stand and where authority-day peripheral positioning happens." But the pointing test asks: what does the *move* turn on? PL40 reads "three women stand along the kiln wall" — this is a stillness/hold beat, not a transitional or positioning verb by the actor performing the move. The rubric's necessity REJECT signatures include "Anchor is a stillness/hold beat (`X holds Y configuration`, `X stays`)" — three women standing along the kiln wall is structurally identical to "three women hold position at the kiln wall." The new-location first-beat exception saves this from a frugality failure, but it does not rescue a hold-beat from the necessity REJECT signature. The selection-skeptic challenge: the entry passes only via the new-location exception, and the exception does not override the hold-beat restriction on the necessity axis.

---

### Intent 7

ENTRY/DECISION: FIRE — `7 @s01e06-pl1 oc-sept-yard-wall | predawn | cold-clear | frost-ground | south face of the sept wall at the yard`
SEAM TYPE: strip
LENS: selection-skeptic

SEAM: PL1 reads "the stone holds the cold against taylor's back" — the proto-line's own SVO establishes wall-contact (stone), the cold, and Taylor's body position. The sensory note "south face of the sept wall at the yard" adds directional specificity (south face) not in the proto-line, but no subsequent proto-line in the PL1–71 window requires the south-wall orientation specifically; PL2, PL5, and PL25 reference wall-weight and warmth-measure without needing a compass bearing. Under the strip test, removing this entry leaves PL1 resolving cleanly on its own content, and the inherited environment would be absent — which passes the episode-anchor necessity argument. But the selection-skeptic challenge is narrower: the focus-element chosen is "south face of the sept wall at the yard," which is architectural description of a fixed geometric fact (the wall has a south face; this is location-card content per the rubric's herald/cart heuristic), not a perceptible state the move turns on.

---

### Intent 8

ENTRY/DECISION: FIRE — `8 @s01e06-pl34 loc-harrenhal-exterior | predawn | cold-clear | gatehouse-two-lights | second lantern kindles beside the first`
SEAM TYPE: focus-element
LENS: selection-skeptic

SEAM: The sensory note is "second lantern kindles beside the first." The pointing test response is that the "beside-ness is the spatial information (same gatehouse station, not a separate window)." But PL34 reads "a second amber bleed lights beside the first" — the beside-ness is already in the proto-line. The sensory note does not name a focus-element beyond what the anchor line states; it paraphrases the beat in slightly different words ("kindles" vs. "lights"), which the rubric explicitly rejects: "re-naming a feature already established by... prior loc-state entry — no incremental selection." The selection-skeptic challenge: the sensory note passes no incremental information beyond the anchor line itself; the focus-element selected is one that the anchor already provides.

---

### Intent 9

ENTRY/DECISION: FIRE — `9 @s01e06-pl55 loc-harrenhal-exterior | predawn | cold-clear | gate-parting | bar half-out of the brackets`
SEAM TYPE: focus-element
LENS: selection-skeptic

SEAM: The studio chose Draft C over Draft A on the grounds that the mechanism (bar coming out) is the focus-element rather than "the seam and the gateyard beyond." But PL55 reads "the seam between the gate-leaves opens" and PL54 reads "the bar lifts halfway out of the brackets" — the bar-half-out fact is stated in the immediately preceding proto-line, PL54. Under the rubric's interestingness REJECT signature — "re-naming a feature already established by... prior loc-state" — a sensory note that names what PL54 already established as its own SVO is redundant. The pointing test question becomes: is "bar half-out of the brackets" new information at PL55's anchor, or is it inherited from PL54? The defense must explain why the bar state is not already established by PL54 itself before a loc-state entry fires.

---

### Intent 10

ENTRY/DECISION: FIRE — `10 @s01e02-pl86 oc-drying-yard | morning | clear | chamomile-drying | chamomile on the rack`
SEAM TYPE: slug-accuracy
LENS: form-skeptic

SEAM: The location slug `oc-drying-yard` does not appear in the locations INDEX. Like `oc-sept-yard`, `oc-sept-nave-arch`, `oc-sept-side-door`, and `oc-sept-nave-interior`, this is an `oc-` slug used in Phase 2 without a corresponding indexed card. The schema requires `<location-slug>` to be "slug of an authored location card (or `oc-…` for project-original)" — but "project-original" implies the card has been authored and indexed by margit, not merely invented at facet-authoring time. The same slug-accuracy gap that applies to Intent 3 applies here. A stitcher reading `[loc-state:10]` cannot resolve `oc-drying-yard` to a card, which breaks the citation graph the facet schema is designed to support.

---

### Intent 11

ENTRY/DECISION: NONE — necessity fails, PL19 is perception-feed beat, wall-seam is location-card content
SEAM TYPE: fire-justification
LENS: inheritance-skeptic

SEAM: PL19 reads "a mouse-shape steps in the seam at taylor's hip" — the mouse's movement through the wall-seam at hip level is a small-animal positioning beat that changes Taylor's immediate sensory environment. The rubric's necessity ACCEPT signatures include "the anchor verb is a transitional or positioning verb" — "steps in the seam" is a positioning verb, and the location fact it turns on (a seam in the wall at hip height, within reach of Taylor's body) is not established by the scene-anchor at PL1 (which names the south face of the wall at the yard, not the seam topology at hip level). The strongest case for firing: the mouse's arrival in the seam is the first positioning event at a sub-element of the wall not covered by the PL1 anchor, and the seam-at-hip-level is a specific perceptible location feature distinct from "south face of the sept wall." Rubric does not categorically exclude animal positioning beats from the necessity axis; the perception-feed classification may be over-applied here.

---

### Intent 12

ENTRY/DECISION: NONE — frugality fails, within-scene continuation, officer's position is actor-state
SEAM TYPE: fire-justification
LENS: selection-skeptic

SEAM: The refusal cites the officer's positioning as actor-state, not location-state. However, the rubric's necessity ACCEPT signature includes "stops at" and "holds the line of sight to" as positioning verbs — and PL12 ("the officer steps to the center of the yard") places an actor at a named sub-feature of the established location (center of the yard). The center of the yard is a specific spatial coordinate that the clerk's subsequent line-up, Taylor's twelve-foot crossing at PL14, and the line formation at PL15–20 all reference geometrically. The strongest fire-justification: the yard's center-point is a location-state sub-feature (not on the location card) that, once occupied by the officer, activates a line-of-sight geometry that the subsequent PL14 crossing depends on. The defense must demonstrate that inherited environment from PL11 establishes the center-point as a known sub-feature rather than a new one.

---

### Intent 13

ENTRY/DECISION: NONE — necessity fails, actor-positioning within established location, yard holds its shape
SEAM TYPE: fire-justification
LENS: inheritance-skeptic

SEAM: The refusal cites "twelve feet of packed dirt" as established in PL14, but PL14 ("taylor crosses the twelve feet of packed dirt") comes after PL13 — the distance fact at PL37 ("taylor steps into the path of the officer's shoulder") is set in the same scene but at a later beat. The prior audit says "PL14 names 'twelve feet of packed dirt'" — but PL14 is in the same scene as PL37, not before it. If the scene-order runs PL11 → PL37 without an intermediate loc-state entry naming the channel width, the available distance at PL37 may not have been formally established by an inherited entry. The strongest fire-justification: if PL37 precedes PL14 in the read-order, the "twelve feet" inherited justification fails and the channel-narrowing may constitute a sub-location state change at PL37 that warrants an entry.

---

### Intent 14

ENTRY/DECISION: NONE — necessity fails, prop-placement beat, trestle already in inherited scene-anchor
SEAM TYPE: fire-justification
LENS: inheritance-skeptic

SEAM: The refusal depends on the trestle being "already present in the inherited scene-anchor (PL40 establishes authority-day configuration at the common)." But Intent 6's entry is the scene-anchor, and its conditions slot carries `kiln-wall, authority-day-configuration` — neither field explicitly names the trestle as an active location feature. `authority-day-configuration` is a condition slug, not a named perceptible object; a stitcher inheriting that condition must know what it implies. The strongest fire-justification: if `authority-day-configuration` does not explicitly include the trestle as an active condition, the steward spreading the scroll at PL44 introduces the trestle as a newly active location element — a state change from "common with kiln-wall positioning" to "common with trestle deployed." Under the rubric's state-change warrant, a new active element at the anchor beat could earn an entry.

---

### Intent 15

ENTRY/DECISION: NONE — frugality fails, within-scene navigation to established fixture
SEAM TYPE: fire-justification
LENS: selection-skeptic

SEAM: PL73 reads "rowan walks the four paces to the trestle" — the four-paces distance is specific and named in the proto-line. The rubric allows an entry when "a new entrant changes the focus-element" — Rowan arriving at the trestle side from the scene's margin is a new entrant (Taylor was seated; Rowan approaches from the yard side). The strongest fire-justification: Rowan's four-pace crossing re-configures the trestle's social geometry (maester on far side, Taylor seated, Rowan arriving at Taylor's side) in a way that changes who is visible to whom from the trestle — a sight-line change is exactly the kind of location-dependent fact that the rubric considers load-bearing. The defense must show that the sight-line geometry was already fully established by the scene-anchor at PL40 and has not changed with Rowan's arrival.

---

### Intent 16

ENTRY/DECISION: NONE — necessity fails, PL21 is environmental persistence beat (anti-pattern 3)
SEAM TYPE: fire-justification
LENS: inheritance-skeptic

SEAM: PL21 reads "the granary holds its three-week shape" — the refusal correctly identifies this as anti-pattern 3 (persistence-as-state). The strongest fire-justification, though thin, is this: the granary's "three-week shape" is not merely a persistence note — it is a specific observable condition of the exterior (three weeks of undisturbed accumulation visible in its profile, or three weeks of the same fill-level) that Taylor reads as she passes. Under a strict location-state reading, a location whose condition is actively observable and load-bearing for a character's inference ("the granary looks exactly as it did three weeks ago, which means no delivery has occurred") is a state-entry candidate at the first beat where the character reads it. The rubric's necessity axis focuses on movement beats, but the new-location first-beat exception also applies to first-encounter perception beats. However this argument requires extending the new-location exception to a context it was not designed for, which is why it is thin.

---

### Intent 17

ENTRY/DECISION: NONE — necessity fails, Taylor sealed inside nave, road not perceptible
SEAM TYPE: fire-justification
LENS: selection-skeptic

SEAM: The refusal turns on imperceptibility: Taylor cannot perceive the road from inside the sealed nave, so loc-state for the road exterior cannot fire. But PL91–93 establish that "the feed stops at the door" and "the closing took the instrument dark" — Taylor's instrument (fauna-channel) is what stops perceiving, not Taylor's body-senses. A loc-state entry for an external location when a character cannot perceive it via body-senses is clearly unwarranted. However, PL94 ("the grey holds the road") could be read not as Taylor perceiving the road but as the narrative camera cutting away from Taylor — a POV cut to the exterior. If the proto-line is an omniscient-narrator beat rather than a Taylor-POV beat, the imperceptibility argument does not apply and the road's grey morning state might warrant an entry as a new-location anchor for that omniscient beat. The defense must confirm that PL94 is Taylor-POV, not a narrator-cut.

---

### Intent 18

ENTRY/DECISION: NONE — necessity fails, auditory detection beat at already-established remote location
SEAM TYPE: fire-justification
LENS: inheritance-skeptic

SEAM: The refusal classifies PL67 ("a shod hoof strikes the cobbles half a league north") as a perception-feed beat at an already-established remote location. The strongest fire-justification: PL67 is not merely a perception-feed beat — it is the first auditory confirmation that the Harrenhal exterior now has a rider in motion on cobbles. The visual remote-location entries (C at PL10, 8 at PL34, 9 at PL55) established gatehouse-lantern states and gate-parting states. None of those entries established that the gate has fully opened and a horse is now on cobbles — that is a new condition at the Harrenhal exterior. Under the rubric's state-change warrant ("a new entrant changes the focus-element"), the rider's cobble-contact is a new active condition at loc-harrenhal-exterior not covered by inherited state. The defense must show that `gate-parting` at PL55 (Intent 9) is sufficient to license the cobble-hoof sound at PL67 without a new entry.

---

## SEAM SEVERITY ROLLUP

- Strong seams (likely revise): 3, 6, 8, 9, 10
- Moderate seams (likely defend): 1, 2, 4, 5, 7, 11, 18
- Thin seams (auto-defend): C, 12, 13, 14, 15, 16, 17
