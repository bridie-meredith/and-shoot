---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 1
episode: b01-c09
date: 2026-06-01
verdict: revise
---

# Sensory Old-State Reader — Cycle 1 Verdict

## Episode b01-c09

---

## Reading stance

I hold two files open: the sensory facet and the location-state file. For every fire, I walk the lineage: where did the old-state come from? Does it trace to a prior loc-state entry? Does the loc-state baseline at that beat match what the sensory entry claims it inherited? If the old-state is invented — no prior loc-state lineage, no prior sensory entry on the same modality — I flag HARD. This is the cross-facet contract, and I do not bend it.

No exemplar loaded. Baseline card behavior only.

---

## Per-entry lineage walk

### [sensory:1] @8 — thermal: stone-lane-late-morning-warmth -> hill-lane-evening-cool

**Old-state claimed:** "stone-lane-late-morning-warmth"

**Lineage walk:**

The most recent prior loc-state entry at or before @8 is loc-state:3 @8 itself: "oc-dragonpit-margin | evening | none | lane-open, outer-circuit." loc-state:3 was co-authored at @8 (cite-index: loc-state:3 @8 co=[exposition:3, sensory:1]).

Does loc-state:3 carry a thermal field? No. loc-state:3 records: location, time-of-day, conditions, lane-state — no sensory field.

Does a prior loc-state entry establish a thermal baseline for the lane Taylor is entering? loc-state:1 @1 and loc-state:2 @3 cover scene-A (hook-ward / stitch-shop lane, late morning). Neither carries a sensory field. No loc-state entry in b01c09 names "stone-lane-late-morning-warmth" or any thermal baseline.

Is there a prior sensory fire on the thermal modality in this chapter? No. sensory:1 @8 is the first thermal fire in b01c09. There is no prior sensory:thermal entry to inherit from.

The facet's own entry (rubric notes) acknowledges this gap at SEAM-011: "old-state 'stone-lane-late-morning-warmth' has no prior loc-state entry in b01c09 yet." The author cites a b01c08 precedent (old-state sourced from scene-map time-of-day transition; SEAM-009/010 carve-out) and a cross-chapter logic: scene-A time-of-day is "late morning" per the scene-map; the stone-lane warmth from the morning hook-ward circuit is the prior thermal register.

Is this baseline derivation valid under the rubric?

The rubric (Axis 1, old-state anchor): "Source the old-state from the locked location-state for the most recent loc-state-cited beat, OR from the prior sensory-flag entry if the modality has fired earlier in the episode." Neither applies here: there is no loc-state thermal field at any prior beat, and there is no prior sensory-thermal entry in b01c09.

The author's argument is a cross-chapter / scene-map time-of-day inference: scene-A is "late morning" in the scene-map; stones in morning sun retain warmth; therefore the old-state is scene-map-derived. This is not one of the two permitted old-state sources in the rubric. The rubric does not enumerate "scene-map time-of-day inference" as a valid old-state anchor.

The b01c08 precedent (SEAM-009/010 carve-out) may have permitted this derivation in b01c08, but I am reading b01c09 against the b01c09 loc-state file, which does not carry a thermal field at any scene-A entry.

**Attack:** [sensory:1] @8 — old-state "stone-lane-late-morning-warmth" has no loc-state lineage in b01c09. loc-state:1 @1, loc-state:2 @3 (scene-A entries) carry no thermal field. No prior sensory-thermal entry exists. The old-state is inferred from scene-map time-of-day, not sourced from loc-state or a prior sensory entry. This is an unanchored old-state per rubric Axis 1 (URI-FACETS-CYCLE-1).

Severity: HARD — rubric explicitly names "Unanchored old-state" as a HARD reject signature (Axis 1 REJECT: "Entry's old-state does not resolve to (a) the most recent loc-state file's § sensory or § conditions baseline for the beat's location, OR (b) the most recent prior sensory-flag entry on the same modality. A free-floating old-state is a fictive baseline.").

Remedy: loc-state:1 @1 or loc-state:2 @3 (whichever covers the hook-ward / stitch-shop area in scene-A) needs a `sensory: thermal: stone-lane-late-morning-warmth` field added. Then sensory:1 @8's old-state traces to that loc-state entry and the lineage is clean. Alternatively, the SEAM-009/010 carve-out logic from b01c08 must be explicitly imported and named in the b01c09 loc-state entries so the lineage resolves. The carve-out alone in the sensory file's notes section is not a loc-state fix.

---

### [sensory:2] @23 — tactile: wax-soft-warm -> wax-set-firm

**Old-state claimed:** "wax-soft-warm"

**Lineage walk:**

Most recent prior loc-state entry at or before @23: loc-state:5 @17 — "the-feed-station | end-of-day | none | station-surface-clear | the station surface — ward-coverage notes and the unsealed packet."

Does loc-state:5 carry a tactile field? No. loc-state:5 names the station surface condition (surface-clear, items on it) but no sensory/tactile field.

Is there a prior sensory-tactile entry in b01c09? No. sensory:2 @23 is the first (and only) tactile fire.

The author's argument: old-state "wax-soft-warm" is entailed by the @19 sealing-act ("taylor-hebert-kl-122ac seals the packet"). The wax is necessarily soft-warm at application; no prior tactile fire conflicts with it.

Is "entailed by prior bone action" a valid old-state source under the rubric? The rubric specifies loc-state sensory/conditions field OR prior sensory entry on the same modality. "Entailed by bone action" is not enumerated.

However, there is a meaningful structural difference between sensory:1 and sensory:2. The tactile:2 old-state ("wax-soft-warm") is a prop-level state, not a room-level ambient state. The wax is applied at @19; it cannot be anything other than soft-warm at that moment. The old-state is not invented — it is physically entailed by the sealing action at @19. The prop's state before @23 is derivable without ambiguity from the event at @19.

The rubric does not explicitly license this "prop-state entailed by prior bone action" derivation. But the rubric's concern is with baselines that are "fictive" — invented against nothing. Here the old-state is not fictive; it is materially determined by what occurred at @19. The wax was applied soft-warm at @19; it hardens to set-firm by @23. No loc-state entry would contradict this; no alternative wax-state is possible between @19 and @23.

I am skeptical but not certain. The rubric's HARD signature is for "free-floating old-states" — baselines asserted against no prior established condition. The wax-soft-warm old-state is not free-floating: it is physically grounded in the @19 application. The question is whether the rubric's two permitted sources are exhaustive or whether physically-entailed-by-prior-event is a permitted third.

My reading: the rubric enumerates two sources; it does not say "including but not limited to." But the purpose of the anchor requirement is to prevent invented baselines. "Wax-soft-warm at application" is not invented; it is physically necessary. I will note this as a SOFT FLAG rather than a HARD finding — the old-state is physically grounded even though it lacks a formal loc-state lineage.

**Attack (SOFT):** [sensory:2] @23 — old-state "wax-soft-warm" has no explicit loc-state field in b01c09 and no prior sensory-tactile entry. The derivation is physically entailed by @19 bone action (sealing-act necessitates soft-warm wax at application). Not a fictive baseline, but lacks formal rubric lineage. Recommend: loc-state:5 @17 (or a new loc-state entry at @19) add a tactile/prop note confirming wax is soft-warm at application stage. This would formalize the lineage the author clearly intends but has not locked.

Severity: SOFT FLAG — the old-state is defensible on physical-entailment grounds; the lineage is informal but not fictive.

---

### [sensory:3] @11 — light: lane-ambient-empty-distribution -> corwick-body-resolving

**Old-state claimed:** "lane-ambient-empty-distribution"

**Lineage walk:**

Most recent prior loc-state entry at or before @11: loc-state:3 @8 — "oc-dragonpit-margin | evening | none | lane-open, outer-circuit." loc-state:4 @11 itself: "oc-dragonpit-margin | evening | none | courier-at-stone-post | Corwick at the lower-gate stone-post beside the side-exit." (Co-emitted with sensory:3 at @11 per cite-index: loc-state:4 @11 co=[narrator:3, sensory:3].)

Does loc-state:3 @8 or loc-state:4 @11 carry a light field? No. loc-state:3 @8 records "lane-open, outer-circuit" — no visual-baseline field. loc-state:4 @11 records "courier-at-stone-post" — this names Corwick's presence, which IS the new-state the sensory entry describes. This is notable: loc-state:4 @11 was authored simultaneously with sensory:3 @11 and names the same event (Corwick at the stone-post) from the state-update side.

Is the old-state "lane-ambient-empty-distribution" anchored by a prior loc-state entry that establishes the empty-lane visual baseline? The old-state describes the lane's visual condition BEFORE @11 — no body-form present. The bones @8-@10 establish the lane orientation: supply cart at @9, stone-post at @10, Taylor entering at @8. None of these are represented in loc-state entries with a visual/light field.

Is there a prior sensory-light entry in b01c09? No. sensory:3 @11 is the first (and only) light fire.

The author's argument: old-state "lane-ambient-empty-distribution" is anchored to the feed-baseline established by @8-@10 (lane entry + orientation beats with no body-return). The scene-B bones @8-@10 establish an empty-lane condition implicitly.

Is "implicitly established by the absence of body-return in prior bones" a valid old-state source? The rubric specifies loc-state sensory field or prior sensory entry. Neither applies.

SEAM-012 flags this explicitly: "old-state 'lane-ambient-empty-distribution' has no prior loc-state entry for scene-B pre-@11 visual baseline."

The empty-lane old-state is more structurally analogous to sensory:1's problem than sensory:2's: it is not a prop-level physically-entailed state; it is an ambient environmental state that would normally be established by a loc-state sensory field. The loc-state file at @8 could have named a visual condition (e.g., "evening lane, no persons in feed return at entry") but did not.

However, there is a meaningful distinction: loc-state:4 @11 records "courier-at-stone-post" — meaning loc-state itself names Corwick's presence at @11 as the state condition. The sensory entry's new-state "corwick-body-resolving" aligns with this loc-state change. The old-state "lane-ambient-empty-distribution" is the implicit prior condition before loc-state:4 was written. The delta direction (empty → courier-present) is consistent with what the loc-state records at @11.

This does not formally anchor the old-state in a loc-state sensory field. But the old-state is derivable from the absence: loc-state has no prior body-presence recorded for this lane stretch (loc-state:3 @8 is "lane-open, outer-circuit" with no person named). The absence of a person in the lane's prior loc-state is the implicit old-state.

I still flag this: the rubric's requirement is explicit loc-state sensory field or prior sensory entry, not "implied by absence in loc-state conditions field." The old-state is unanchored by the rubric's formal sources.

**Attack (HARD):** [sensory:3] @11 — old-state "lane-ambient-empty-distribution" has no prior loc-state light/visual field and no prior sensory-light entry. The baseline is derived from the implicit absence of body-presence in @8-@10 bones, not from a named loc-state sensory condition. SEAM-012 flags this explicitly. Per rubric Axis 1, an old-state that does not resolve to (a) loc-state sensory/conditions baseline or (b) prior sensory entry on the same modality is a HARD finding (unanchored old-state / fictive baseline).

However: the dispatch binding exemption instructs me not to fault on density or cap grounds. I may still attack on craft: does it contradict prior state? Does it actually ground the courier resolving as a seen body? On old-state lineage, my attack stands: the exemption covers density and frequency-band, not old-state correctness. The exemption does not forgive a loc-state lineage failure.

Mitigating factor: the empty-lane old-state is factually accurate (loc-state:3 @8 does not name any body in the lane; @9-@10 bones name a cart and a stone-post, not a person). The derivation is correct even though it is informal. A loc-state sensory note at @8 naming "no-body-in-feed-return" would anchor this formally.

Remedy: loc-state:3 @8 needs a sensory/visual field added: something like "sensory: lane-ambient-empty-distribution" or "visual: no-body-presence in feed-return." Then sensory:3 @11's old-state traces to loc-state:3 @8 and the lineage is clean. Alternatively, the empty-lane condition can be established in loc-state:1 @1 as the scene-B entry state.

Severity: HARD — formal rubric lineage is absent. The factual accuracy of the inferred baseline is not a rubric substitute.

---

## Summary of findings

| entry | old-state | loc-state lineage | finding | severity |
|-------|-----------|-------------------|---------|----------|
| sensory:1 @8 | stone-lane-late-morning-warmth | no thermal field in any loc-state entry; no prior sensory-thermal | unanchored old-state | HARD |
| sensory:2 @23 | wax-soft-warm | no tactile field in loc-state:5 @17; no prior sensory-tactile; physically entailed by @19 | informal / physically grounded | SOFT FLAG |
| sensory:3 @11 | lane-ambient-empty-distribution | no light/visual field in loc-state:3 @8; no prior sensory-light; SEAM-012 flagged by author | unanchored old-state | HARD |

**Two HARD findings (sensory:1 and sensory:3) on old-state lineage.**

---

## Convergence trace vs. signal-fb-001

signal-fb-001 flags density 13% as advisory. My findings are independent of density — they concern old-state lineage, not how many fires exist. My two HARD findings would stand regardless of whether the density advisory existed.

My HARD findings partially converge with the seam-flags the author embedded in the facet file (SEAM-011, SEAM-012): the author explicitly acknowledged the lineage gaps and instructed the R2 reviewer to confirm or revise. I am the R2 reviewer on the old-state axis. My confirmation is: the old-states are unanchored by the rubric's permitted sources.

---

## Verdict

**REVISE**

Two HARD findings on old-state lineage:

- **[sensory:1] @8** — old-state "stone-lane-late-morning-warmth" unanchored. No loc-state thermal field in scene-A. Remedy: add thermal sensory note to loc-state:1 @1 or loc-state:2 @3 (whichever governs scene-A lane ambient), or add to loc-state:3 @8 as a prior-state annotation. Then revise sensory:1 to cite that loc-state field as its old-state source.

- **[sensory:3] @11** — old-state "lane-ambient-empty-distribution" unanchored. No loc-state visual/light field for scene-B pre-@11. Remedy: add visual/sensory field to loc-state:3 @8 naming the empty-lane feed-distribution baseline. Then sensory:3 @11's old-state resolves to that loc-state field.

One SOFT FLAG (sensory:2 @23): physically grounded but lacks formal loc-state lineage. Recommend adding a tactile/prop note to loc-state:5 @17 or a new loc-state entry at @19. Not a blocking finding.

The content of the fires is accurate. The perceptual deltas are real. The problem is documentation: the loc-state file does not carry the fields that formally anchor these old-states. The fix is loc-state additions, not sensory entry deletions — but the sensory entries cannot be accepted as-is without the loc-state anchor being present.
