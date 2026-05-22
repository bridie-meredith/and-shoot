---
reviewer: sensory-modality-coverage
facet: sensory
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: fail
---

# Verdict reasoning

Two entries across 27 proto-lines = 7.4% density. Rubric band ceiling is 6%. Breach-high — already flagged as auditor S-008 (r1 FREQUENCY-BAND SIGNAL). I read frequency-band breach as a structural fail, not an advisory, when combined with what the distribution looks like.

Modality tally: 1 light (sensory:1 @3), 1 thermal (sensory:2 @16). Two modalities — passes the ≥2 floor on paper. But this is a cosmetically satisfying number that conceals three real problems.

First: sensory:2 @16 is suspect. The proto-line is "the walls cool" — "cool" names the thermal event. If the disambiguation-pedant strikes it as a charged-verb redundancy (and the gate analysis supports that reading), the file collapses to 1 entry and 1 modality (light only). Single-channel; coverage fails outright.

Second: the episode has two explicit audible inflection beats with no sound fires at all. At @15 (`the insects fill the block`) the scene's atmosphere shifts — a swarm filling a block is a discrete environmental sound onset, bare proto-line verb, audience-perceptible. At @17 (`the boots strike the cobbles`) the city-watch passage generates a specific sound cue — "boots strike cobbles" is locomotion-bare with respect to the sound-register (the proto-line names the action, not the audible quality or volume of the strike). Both are missed fires. Zero sound coverage in a Flea Bottom episode with a watch-patrol and an insect-swarm is a silent gap in the most audience-accessible modality.

Third: loc-state:3 @11 explicitly names a smell event — "tallow-smoke from the rendering-alley still threading across the yard." That is a loc-state author describing a discrete environmental smell presence. No sensory fire at @11 for smell. The rubric's cross-facet contract section (§ Cross-facet modality silent-gap) is unambiguous: a loc-state sensory note that names a discrete perceptual event must be accompanied by a sensory-flag at the same anchor, or the loc-state language must be downgraded to non-event ambient. Neither happened. The file skips a smell inflection the loc-state author directly named.

The result: an episode with no sound, no smell, the sole thermal entry suspect on disambiguation grounds, and a density breach on top. The sensory file does not texture this episode; it places two entries and leaves the location's actual perceptual palette — rain-recent mud, tallow-smoke, insect-swarm, watch-boots on cobbles — unfired. That is a fail, not a revise. The required fixes are not minor rebalancing; they require additions at @11 (smell), @15 (sound), @17 (sound), and culling or reauthoring of sensory:2 to bring density inside the band.

# Entry-level callouts

[sensory:--] @11 — tallow-smoke silent-gap. loc-state:3 @11 names "tallow-smoke from the rendering-alley still threading across the yard" — discrete smell event, named by the loc-state author. No sensory fire. Rubric §Cross-facet modality silent-gap: add `smell:` entry at @11 or downgrade loc-state:3 language to non-event ambient.

[sensory:--] @15 — insect-swarm sound silent-gap. `the insects fill the block` — bare proto-line; a swarm filling a block is a discrete audible onset; audience-perceptible; no sound fire. Add ≥1 sound entry at @15.

[sensory:--] @17 — boots-on-cobbles sound silent-gap. `the boots strike the cobbles` — bare locomotion verb; the watch-patrol's audible presence is register-distinguishable from street-ambient; no sound fire. Candidate for sound spike entry.

[sensory:--] FILE-LEVEL — 0 sound fires across entire episode. Sound is the most accessible modality; its absence is a coverage failure. Flea Bottom + city-watch-passage + insect-swarm with no sound fires is not a discipline of sparsity — it is a category miss.

# Convergence trace

- FILE-LEVEL density breach — convergent with auditor S-008 (r1, FREQUENCY-BAND: sensory 7.4% vs ceiling 6%). Auditor called it advisory SIGNAL; I read it as a fail driver because the distribution context makes it structurally worse than arithmetic.
- @11 smell silent-gap — convergent with rubric §Cross-facet modality silent-gap (URI-FACETS-CYCLE-1, 2026-05-19, promoted to rubric from prior audience-gate attacks). The rubric explicitly names this failure mode; my callout applies the rubric's language to loc-state:3's tallow-smoke note. Not surfaced by the r1 or r2 auditor — original to this review.
- @15 and @17 sound silent-gaps — original to this review. The r1 auditor did not compute per-modality distribution or flag sound absence.
