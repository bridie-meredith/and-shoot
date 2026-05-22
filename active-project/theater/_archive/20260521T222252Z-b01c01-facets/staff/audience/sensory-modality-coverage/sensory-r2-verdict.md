---
reviewer: sensory-modality-coverage
facet: sensory
cycle: 2
episode: b01-c01
date: 2026-05-20
verdict: fail
---

# Verdict reasoning

Cycle-1 I failed this file on three counts: density breach (7.4% vs 6% ceiling), zero sound coverage (no fires at @15 or @17 despite insect-swarm and boots-on-cobbles), and smell silent-gap at @11 (loc-state:3 named tallow-smoke with no sensory fire). I demanded additions at @11 (smell), @15 (sound), @17 (sound) and culling or reauthoring of sensory:2 to bring density inside band.

The cycle-2 fixer addressed exactly one of those demands: sensory:2 was cut on the disambiguation-pedant's charged-verb finding. The cut resolves the density breach — 1/27 = 3.7% is inside band. That part is done.

What was not addressed: sound and smell.

The three modality silent-gaps I named — @11 smell, @15 sound, @17 sound — are now documented in a `# audience-gate-cycle-1-defer` block inside the sensory file. The fixer did not add the entries. It documented the omission and gave a minimum-change rationale: adding three new entries would re-open the sparsity question and expand the facet substantially.

I read that rationale and do not accept it as a resolution. Unaddressed feedback in round 2 is an escalation per the audience's operating rules. I did not accept the modality gaps in cycle-1. In cycle-2, the fixer has explicitly documented that the gaps remain and deferred them. That is not a fix — it is a carry-forward dressed as a resolution.

The specific problems that drove my cycle-1 fail verdict still exist in the file:

Sound: zero fires across the episode. The file has one modality: light. The ≥2 modality floor requires at least two distinct modalities. A single-modality sensory file fails coverage outright. The disambiguation-pedant's acceptance of sensory:1 on light-modality grounds does not change this — light alone is one modality.

Smell: @11 is now a bare loc-state gap (loc-state:3 was deleted at F-007). The smell cue that loc-state:3 had named ("tallow-smoke from the rendering-alley still threading across the yard") no longer exists in the location-state file — it was removed as part of a different fault. The smell silent-gap complaint loses its loc-state:3 anchor. That specific rationale for a smell fire at @11 is weakened by the F-007 deletion.

However: the sound silent-gap at @15 and @17 is independent of loc-state:3. Those protolines are `the insects fill the block` (@15) and `the boots strike the cobbles` (@17). Neither depends on a loc-state event; they are straightforwardly bare proto-lines with audible content that the file has left unfired. My cycle-1 sound callout stands unmodified.

The result: the file exits cycle-2 with 1 entry, 1 modality (light), 0 sound coverage in a Flea Bottom episode that contains an insect-swarm onset at @15 and a city-watch cobble-strike at @17. The ≥2 modality floor is not met. A defer block is not a modality. The carry-forward documentation tells me the gap is known; it does not tell me the gap is acceptable.

The cycle-1 demand for ≥1 sound entry has not been met. I hold the fail.

# Entry-level callouts

[sensory:--] @15 — ESCALATED from cycle-1. `the insects fill the block` — bare proto-line; insect-swarm filling a block is a discrete audible onset; audience-perceptible; no sound fire. Cycle-1 I named this as a miss. Cycle-2 the fixer documented it as a defer. I read the defer as an unaddressed cycle-1 finding, which escalates to a demand: add `sound: street-ambient -> insect-fill` (or equivalent) at @15, or provide a rubric defense that this bare verb self-carries its audible content. A defer block is not a defense.

[sensory:--] @17 — ESCALATED from cycle-1. `the boots strike the cobbles` — bare locomotion verb; the city-watch's audible presence is register-distinguishable from street-ambient; no sound fire. Cycle-1 I named this as a candidate. Cycle-2 the fixer documented it as a defer. Same escalation: add ≥1 sound entry at @17 or provide rubric defense. "Would expand the facet substantially" is not a rubric defense for a coverage miss.

[sensory:FILE-LEVEL] — ESCALATED from cycle-1. 1 entry / 27 proto-lines = 3.7% density (inside band — this is resolved). But 1 modality only (light). ≥2 modality floor is unmet. Single-channel. The file does not satisfy the file-level modality-coverage health-check stated in the rubric's § Curve-shape rubric / Episode-level shape section.

[sensory:--] @11 smell — cycle-1 callout weakened by F-007 (loc-state:3 deleted, removing the loc-state anchor for the tallow-smoke smell event). I do not escalate the @11 smell callout as a demand because the loc-state authority for it has been removed. I carry it forward as an advisory: if a future loc-state entry reintroduces the tallow-smoke cue, the sensory file must address it.

# Convergence trace

- Sound silent-gap @15 and @17 — original to cycle-1 review; not surfaced by the mechanical auditor in either r1 or r2. Cycle-2 fixer acknowledged but deferred. This review escalates.
- FILE-LEVEL modality — ≥2 floor: the rubric states this explicitly in § Curve-shape rubric / Episode-level shape / Modality-coverage health-check. One modality does not satisfy the floor. Not surfaced by the mechanical auditor.
- @11 smell — original to cycle-1; weakened by F-007 loc-state:3 deletion. No escalation.
- Density breach — RESOLVED. sensory:2 cut brings sparsity to 3.7%. Convergent with auditor S-008 resolution.
