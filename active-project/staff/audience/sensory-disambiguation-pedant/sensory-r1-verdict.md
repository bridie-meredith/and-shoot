---
reviewer: sensory-disambiguation-pedant
facet: sensory
cycle: 1
episode: b01c10
date: 2026-06-02
verdict: revise
---

# Sensory Disambiguation Pedant — R1 Verdict

**Verdict: REVISE**

One entry carries an unanchored old-state that does not survive the disambiguation gate. The remaining six entries pass my lens. Detail below.

---

## Entry-level callouts

### [sensory:7] @25 — REVISE — unanchored old-state; disambiguation failure on the sound-arc's prior-state claim

`sound: ledger-accounting-writing-sound -> silence-on-ledger-close`

Proto-line: `taylor-hebert-kl-122ac closes the ledger`.

The old-state is `ledger-accounting-writing-sound`. The trace in the facet notes names two anchors: sensory:2 @10 (prior sound fire) and loc-state:8 @23 (station mid-accounting).

**The trace fails on both anchors.**

Anchor 1 — sensory:2 @10: new-state was `stylus-on-channel-surface`. This is a channel-surface routing act, 15 bones earlier, in a different physical context (body-map-to-channel, scene-B). The sound fire at @25 renames this `ledger-accounting-writing-sound`. These are not the same named state. The rubric requires the old-state to match "the most recent prior sensory-flag entry on the same modality" — the prior entry's new-state must be the current entry's old-state for the chain to hold. `stylus-on-channel-surface` ≠ `ledger-accounting-writing-sound`. The name change is not cosmetic: one is routing a body-map into a distribution channel; the other is writing a ward's name into a personal ledger. Different surfaces, different acts, different sonic textures.

Anchor 2 — loc-state:8 @23 and loc-state:7 @20: both loc-state entries name the sensory-baseline of scene-D as "indoor station surface, still air, day's-end quiet." The word "quiet" appears in loc-state:7 explicitly. If the loc-state says the baseline is quiet and still air, then the old-state for any sound fire in scene-D is `end-of-day-still-air` or `day's-end-quiet` — not `ledger-accounting-writing-sound`. The writing sound during the accounting is implied by the action but is not a named loc-state baseline. The "implied ambient" argument in the facet notes is an inference, not an anchor.

**What the old-state is doing:** the entry claims a sound was ongoing (writing-sound) so that its cessation (ledger-close → silence) reads as an inflection. But if the ongoing sound is not established as a named state in any prior fire or loc-state entry, the inflection is asserted against a baseline the file does not hold. This is the rubric's HARD pattern: "Unanchored old-state — entry's old-state does not resolve to the most recent loc-state file's § sensory or § conditions baseline... OR the most recent prior sensory-flag entry on the same modality."

**The disambiguation question directly:** what is the perceptual referent of `ledger-accounting-writing-sound`? The reader cannot locate this sound in the established sensory record of scene-D. Loc-state:7 says the scene opens in "still air, day's-end quiet." There is no fire between @20 and @25 that names writing-sound as the new ambient. The old-state is a free-floating inference dressed as a named state. The stitcher cannot anchor this fire to a prior established perceptual register.

**Fix path:** Two options. (A) Revise the old-state to `end-of-day-still-air` and the new-state to `ledger-close-sound` — the ledger closing into the existing quiet produces a discrete audible event (cover-thump), which is a genuine sound-spike against day's-end-quiet, not a sound-drop. This changes the tag from `drop` to `spike`. (B) Alternatively, add a sound fire at @21 (taylor writes corwick — refused in the cull) to establish `end-of-day-quiet -> stylus-on-ledger-surface`, then @25 can fire legitimately as `stylus-on-ledger-surface -> silence-on-ledger-close`. The cull note refused @21 on scene-D restraint grounds, but the old-state problem at @25 may require reconsidering that cull or re-anchoring @25's old-state against the existing quiet.

The inflection-pair arc argument (sensory:2 @10 brackets with sensory:7 @25) is structurally appealing but does not substitute for a valid old-state anchor. The bracket is a design intention; the rubric requires an established baseline.

**Convergence trace:** the auditor's Phase 5 SUPERFLUOUS review notes sensory:7@25 as a lonely grounding-ledger entry (grd-007) and passes it on grounding-exemption grounds. The auditor correctly did not examine old-state-derivation lineage at the SUPERFLUOUS pass — that is my lane. The auditor's CONSTRAINT and RUBRIC-FIDELITY sections have no finding on sensory:7. This is a seam the mechanical scan did not reach. The rubric's Axis 1 (Modality-inflection) REJECT signature "Unanchored old-state (HARD)" was not triggered in the Phase 5 report because the finding requires tracing the sound-state lineage from loc-state:7 against the old-state claim — a disambiguation-specific chain-walk.

---

## Entries passing my lens (no callout)

**[sensory:1] @3** — `the morning-stone holds the bay-cold`. "holds" is bare. Cold-on-stone is the single thermal referent. Old-state `station-indoor-morning-ambient` is tight against loc-state:1 @1 ("cold carried off the bay to the working surface... cold-season morning stone, tactile/thermal"). The ambient before the cold registers = indoor-morning ambient. Clean chain. The referent does not split. PASS.

**[sensory:2] @10** — `taylor-hebert-kl-122ac translates the body-map`. "translates" is abstract; does not self-carry sound. Old-state `station-morning-quiet` is inferred by absence from loc-state:1 ("no competing ambient sound named") — a weaker anchor than an explicit loc-state sound-field, but the inference is defensible given that the morning-station-quiet is the scene-A register and no competing sound is established. The new-state `stylus-on-channel-surface` resolves to a single audible referent (instrument marking surface). PASS. Advisory note only: `station-morning-quiet` is anchored by absence, not by explicit loc-state language. If the auditor were to revisit anchor-strength across the file, this entry is the second-most exposed after sensory:7.

**[sensory:3] @13** — `the supply cart marks the lower-gate road`. "marks" is bare (geometric presence). The old-state `outdoor-morning-stone-air` anchors directly to loc-state:4 @13 which explicitly names "cold-morning outer-road stone, supply-cart odor" as the sensory-baseline. The olfactory referent is the cart's odor-arrival at the circuit-pass. Single referent. Clean. PASS.

**[sensory:4] @15** — `the lower-gate road loses corwick`. "loses" is bare (absence verb, not a visual charged-word). The light-drop is the visual negative-space read: the errand-corridor mouth returning empty against the established circuit-geometry. Old-state `outer-circuit-ordinary-distribution` anchors to loc-state:4 @13 ("outer circuit in its ordinary rhythm"). One referent: the visual field's empty slot. PASS.

**[sensory:5] @19** — `the bay-cold presses the lower road`. "presses" is bare. The thermal referent is the cold foregrounded as physical pressure on the walking body at the circuit-deviation point. Old-state `outer-road-cold-morning-ambient` anchors to loc-state:4 @13 (cold-morning outer-road baseline). I noted this as borderline on the sustained-as-inflection test: the cold was already the scene-C ambient. The "pressing" quality is a genuine inflection from ambient-background to foregrounded-bodily-pressure at the deviation moment — the body walking into the pass at the deviation point makes the cold register differently. I hold this as a genuine up-inflection (ambient → foregrounded-pressure), not a restatement. PASS, with the observation that the `up` tag is doing work: if the stitcher renders this as ambient weather-description rather than bodily-pressure, the inflection collapses. The stitcher Phase 4 voice-embodiment should render the cold as bodily register, not ambient note.

**[sensory:6] @22** — `the feed-station stone grounds the wrist`. "grounds" is bare (contact verb). Tactile referent: cold-firm stone surface under the wrist. Old-state `wrist-above-station-surface` anchors to loc-state:7 @20 ("indoor station surface"). Contact-onset from no-contact to stone-contact: single tactile referent, unambiguous chain. PASS.

---

## Density exemption acknowledgment

Per the dispatch binding exemption (PROP-0022): I have not attacked any entry on density grounds. The grounding-ledger grd-001..grd-007 (all status: satisfied) are acknowledged. My REVISE finding on sensory:7 is a craft finding — an old-state derivation failure, not a density objection.

---

## Aggregation note

Per facet-adversarial aggregation rule (URI-AUDIENCE-AGGREGATION-RULE, 2026-05-11): this is a per-reviewer verdict file. Any single `revise` blocks the facet. This reviewer returns REVISE. Orchestrator reads this file directly; no internal aggregation performed here.

**Verdict: REVISE — sensory:7 @25 old-state unanchored; fix path named above.**
