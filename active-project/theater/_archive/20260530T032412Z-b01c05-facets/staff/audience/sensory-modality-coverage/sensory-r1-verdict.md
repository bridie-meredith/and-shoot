---
reviewer: sensory-modality-coverage
facet: sensory
episode: b01-c04
cycle: r1
date: 2026-05-27
verdict: revise
---

# Sensory Modality Coverage — Phase 5b Adversarial Review
## b01c04 sensory-b01-c04.md

---

## Modality tally (file-level)

| id | proto | modality | delta |
|----|-------|----------|-------|
| sensory:1 | @1 | smell | eel-alley-dawn-air -> tallow-damp-lane-caulking |
| sensory:2 | @13 | smell | tallow-damp-lane-caulking -> middens-discard-compound |
| sensory:3 | @25 | sound | carter-work-ambient -> roper's-court-near-silence |

**Modality distribution: smell ×2 / sound ×1. Zero thermal. Zero tactile. Zero light.**

Total: 3 entries / 39 bones = 7.7%. Above the 3-6% band.

---

## Density — ADVISORY, not blocking

The auditor's flag-003 identifies the arithmetic: 3 scenes × 1 scene-open fire = 3/39 = 7.7% regardless of authoring choices. The V3 short-chapter floor-vs-ceiling exemption does NOT apply here — `bone_count = 39`, above the sub-30 threshold. The standard 6% ceiling is in effect and the file exceeds it. However, the scene-count floor argument is structurally real: a 3-scene chapter cannot achieve both modality-floor coverage and scene-open anchoring without exceeding the ceiling arithmetically. This reviewer treats the density overshoot as architectural-advisory, not as a primary attack.

The modality distribution is the primary attack.

> Convergence trace: overlaps auditor flag-003 (FREQUENCY-BAND — sensory geometry-floor conflict).

---

## Attack 1: smell-dominant file across a three-location dawn chapter

2 of 3 fires are smell. The chapter moves through eel-alley (scene-A), Pig Tallow Lane (scene-B), Roper's Court (scene-C). That lane-sequence is a smell-progression by location design — the middens drift follows Taylor through the geography. Both smell fires are defensible individually.

But a chapter of 39 bones crossing three exterior pre-dawn locations in King's Landing has zero thermal fires. Pre-dawn stone-yard, early-morning lane, open court at grey-light. The thermal palette of these locations — cold stone, pre-dawn chill, the warmth differential of bodies in a yard — is absent from the sensory file entirely. This reads single-channel across the opening two scenes.

> [sensory:file-gap-thermal] — zero thermal fires across 39 bones in a pre-dawn exterior chapter. The location palette (stone, pre-dawn hour, open lanes) licenses at least one thermal fire. The episode reads cold-free.
> Convergence trace: no direct auditor finding; this gap is uncaught by the mechanical scan.

---

## Attack 2: pre-dawn stone yard — thermal candidate missed at scene-A

Scene-A (@1-@12): smell:1 at @1. Nothing else for 12 bones.

Proto-line @4: "taylor-hebert-kl-122ac takes the shed-wall." This is Taylor placing her back against the shed-wall while waiting for Jarvis. A pre-dawn stone wall in King's Landing in the early morning is a thermal contact event — cold stone against a body is a discrete tactile/thermal inflection at audience-experiential scale. The verb "takes" is bare (does not self-carry the thermal register). Magnitude clears Q2 — cold stone on a pre-dawn morning is unambiguously register-shifting; it is not sub-threshold micro-grain. This was a fire the author bypassed.

The loc-state:2 anchors at @4 (back=Y in cite-index). The loc-state file for scene-A carries the cooper's yard as the active location. A thermal fire at @4 would need an old-state from the most recent loc-state for the beat's location. The episode's chapter-open thermal baseline (predawn air) is nameable from loc-state:1 @1. Old-state chain: predawn-air-thermal (from loc-state:1 @1 baseline) -> shed-wall-cold-contact (the inflection at @4). The old-state lineage is anchored.

> [sensory:missed-fire-A] @4 — taylor-hebert-kl-122ac takes the shed-wall; thermal candidate. Bare verb; pre-dawn stone-wall contact; audience-experiential magnitude clear. Old-state anchors to loc-state:1 @1 predawn baseline. Missed fire.
> Convergence trace: cite-index marks loc-state:2 @4 as a lonely entry (no co-citations, no inbound license). A thermal sensory fire at @4 would co-cite loc-state:2 and ratify the scene-A environmental state.

---

## Attack 3: scene-B working-lane — sound candidate missed at @17

Scene-B (@13-@24): smell:2 at @13. Zero other fires across 12 bones.

Proto-line @17: "the penny-a-barrel carter parks the middens cart." This is an active-motion bone in a pre-dawn working lane. Cart-wheel on lane-stone stopping, the physical noise of a cart being set in position — this is a sound event. The verb "parks" is bare (does not self-carry the audible register of a cart stopping on cobblestone). Magnitude: a cart stopping in a pre-dawn near-silence is audible at audience-experiential scale. The prior sound baseline for scene-B is the "carter-work-ambient" named in sensory:3's old-state — which means carter-work-ambient was the active sound register *before* @25, suggesting the cart was already in ambient motion earlier. If carter-work-ambient is the scene-B ambient, then @17 is a moment within that sustained ambient rather than an inflection. However: sensory:3 is anchored at @25 (scene-C open), not scene-B. The old-state "carter-work-ambient" in sensory:3 may be describing what Roper's Court transitions from — implying carter-work was the ambient at the scene-C arrival point, not throughout scene-B. Ambiguity is present; the author should confirm whether the carter-work sound was sustained throughout scene-B (loc-state job) or whether @17 was a discrete event within a quieter scene-B baseline.

If the carter-work sound was NOT the sustained scene-B ambient (i.e., the carter arrives and starts work at or near @17), then @17 is an inflection beat — silence-to-cart-noise — and a sound fire was earned and skipped. If the carter-work was the sustained ambient from scene-B open, @17 is sustained-as-inflection and the refusal is correct (inflection-not-sustained test).

This ambiguity is a revise finding, not a fail. The author needs to confirm the scene-B sound baseline in loc-state.

> [sensory:ambiguous-B] @17 — carter parks the middens cart; sound candidate. Whether this is an inflection or sustained-ambient depends on scene-B's loc-state sound baseline. If the carter's sounds were not the established scene-B ambient, this was a missed fire. Requires loc-state:3 @13 clarification of scene-B sound baseline.
> Convergence trace: no direct auditor finding.

---

## Attack 4: loc-state:4 names a light-level condition — sensory fires only sound at @25

Scene-C (@25-@39): sound:3 at @25 (carter-work-ambient -> roper's-court-near-silence). This is the scene-C open and the only sensory fire in a 15-bone scene.

Proto-line @25: "the early-morning grey empties Roper's Court." The language names a light condition — "early-morning grey" — as part of the scene-C open. The loc-state:4 fires at @25 (back=Y, co-cited with sensory:3 and state:5 in the cite-index). If loc-state:4's sensory section names the grey as a discrete light-level change from the eel-alley predawn darkness, that is a loc-state sensory note naming a perceptual event — which the rubric's Cross-facet modality silent-gap clause requires to be accompanied by a sensory-flag at the same anchor.

The sensory file fires only sound at @25. The early-morning-grey light condition goes unratified by the sensory facet.

The rubric states: a loc-state sensory note naming a discrete perceptual event (thermal release, audible texture change, smell drift) must be accompanied by a sensory-flag at the same anchor, OR the loc-state author must downgrade the sensory note to non-event ambient language. If "early-morning grey" is a sustained baseline (carried from before the chapter's open), no fire is required. But "empties Roper's Court" frames the grey as a qualifier of the court's specific atmospheric condition at scene-C open — it reads as a present-tense characterization, not a prior-established baseline. This is a cross-facet contract candidate.

> [sensory:cross-facet-gap] @25 — loc-state:4 names early-morning grey at scene-C open; sensory fires sound only. Light modality unratified. If loc-state:4's sensory note characterizes the grey as a discrete light-level change from the scene-A/B predawn, the cross-facet contract requires a sensory light fire at @25 OR a loc-state:4 downgrade to ambient language.
> Convergence trace: auditor pass-007 checks scene-map per-scene caps (sensory ≤3, PASS) — but the cap-pass does not evaluate the loc-state cross-facet contract. The auditor's pass is on the ceiling; this attack is on the floor. No auditor finding overlaps this callout.

---

## Summary of callouts

| id | proto | modality | attack | severity |
|----|-------|----------|--------|----------|
| [sensory:file-gap-thermal] | — | thermal | zero thermal fires across 39 pre-dawn exterior bones | revise |
| [sensory:missed-fire-A] | @4 | thermal | shed-wall cold-contact; bare verb; magnitude clear; old-state anchored | revise |
| [sensory:ambiguous-B] | @17 | sound | carter parks; sound candidate pending scene-B baseline confirmation | revise |
| [sensory:cross-facet-gap] | @25 | light | loc-state:4 names grey at scene-C open; light unratified by sensory | revise |

No fails. All callouts are revise. The three entries that exist are individually defensible — each fires on a bare verb at a scene-open anchor with a nameable old-state and a perceptible inflection. The attack is not against what was fired; it is against what the file leaves silent across 39 bones and three exterior pre-dawn locations.

---

## Modality-coverage floor verdict

Floor = 2 modalities. Met (smell + sound). This prevents a fail. But the floor being met does not mean the file is healthy — two distinct modalities across 39 bones with zero thermal, zero light, zero tactile, in a pre-dawn exterior chapter with stone walls and open courts, is coverage-at-floor only. The chapter's environmental palette licenses more. The stitcher will render this chapter sensory-flat on all modalities except smell-progression and one sound-drop.

---

## Prescription

**Minimum-change fix: add ≥1 thermal fire and resolve the @25 light question.**

1. Thermal fire at @4 (shed-wall-cold-contact): add `thermal: predawn-air-ambient -> shed-wall-cold-contact` anchored at @4. Verify old-state chains from loc-state:1 @1.
2. @25 light question: confirm whether loc-state:4 names early-morning-grey as a discrete inflection from predawn darkness. If yes, add `light: predawn-dark -> early-morning-grey` at @25 alongside the existing sound:3. If the per-scene cap (≤3) would be breached: scene-C currently has 1 fire; adding 1 more = 2 total, well within cap. The add is permitted.
3. @17 ambiguity: confirm scene-B sound baseline in loc-state:3. If carter-work was not the established scene-B ambient from @13, add a sound fire at @17. If it was sustained from @13, refusal stands and no add is required.

**Anti-pattern #14 (Cycle-N ADD without pre-validation) is in force for any adds.** Each proposed ADD must clear the full per-entry rubric — modality-inflection, disambiguation-discipline, magnitude-sufficiency, audience-side-perceptibility, AND old-state lineage — before writing to the file. If the thermal ADD requires a loc-state edit to anchor the old-state, the loc-state edit lands first.

Do NOT add fires on any other bones to hit density. The architectural-density issue (7.7% vs. 6% ceiling) is advisory; inflating to 4-5 entries without earning each on all four rubric axes is anti-pattern #12 (density-on-charged-beats).

---

VERDICT: **revise**

Grounds: smell-dominant file (×2 of 3 entries) with zero thermal and zero light across 39 bones of pre-dawn exterior chapter; missed thermal fire at @4 (shed-wall cold-contact; bare verb; anchored old-state); @25 loc-state:4 light condition unratified by sensory facet (cross-facet contract candidate); scene-B sound candidate at @17 pending baseline confirmation. Modality floor met (2 modalities) but cross-modal texture insufficient for the episode's environmental scope.
