---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 1
episode: s01e03
date: 2026-05-12
verdict: revise
---

# Verdict reasoning

Five of eight sensory entries carry old-state fields with no traceable loc-state lineage — they are invented, inferred from proto-line narrative action, or contradicted by the most recent loc-state for that location. The two clean entries (sensory:6 and sensory:7) demonstrate the pattern works when the author actually sources from loc-state; the failures are not edge cases but a systematic authoring gap. The facet cannot pass with five unanchored old-states out of eight fires.

# Entry-level callouts

- [sensory:1] @11 — old-state `market-side-alley-ambient` has no loc-state lineage. Most recent prior loc-state entries are loc-state:1 @1 (`predawn | cold | room-quiet`) and loc-state:2 @3 (`morning | clear | junction-open`); neither names a thermal baseline called `market-side-alley-ambient`. First thermal fire in the episode; no prior thermal sensory entry to inherit from. Baseline is invented.

- [sensory:2] @34 — old-state `eastern-quarter-alley-cold` fires in a frame loc-state never set up. No loc-state entry for the eastern-quarter alley exists before @34. The nearest prior loc-state is loc-state:5 @26 (`loc-flea-bottom-base | dawn | cold`) — a different location entirely. `eastern-quarter-alley-cold` cannot be derived from any prior loc-state entry; the baseline is unanchored.

- [sensory:4] @67 — old-state `open-palm-air` describes the tactile state of Taylor's extended palm. No loc-state entry establishes a tactile baseline at loc-flea-bottom. Most recent prior loc-state is loc-state:9 @64 (`loc-flea-bottom | afternoon | clear | street-mouth, alley-exit`); no tactile field. No prior tactile sensory entry in the episode. Old-state is inferred from proto-line @66 (`taylor-hebert-flea-bottom extends the palm`), not sourced from loc-state. Proto-line narrative is not a loc-state substitute.

- [sensory:5] @90 — old-state `pen-scratch-on-parchment` has no loc-state lineage. Most recent prior loc-state is loc-state:12 @86 (`loc-eastern-quarter-apothecary | afternoon | clear | apothecary-door-open, stair-base`); no sound baseline named. No prior sound sensory entry in the episode. Old-state is inferred from proto-line @89 (`the beetles relay the pen-scratch`), not sourced from loc-state. Baseline unanchored.

- [sensory:8] @148 — old-state `room-ambient` contradicts the most recent loc-state for loc-flea-bottom-base. loc-state:16 @118 establishes `loc-flea-bottom-base | dawn | cold | waking, log-at-wall`; the thermal descriptor is `cold`, not ambient. `room-ambient` is a generic invented name that ignores the `cold` baseline the loc-state set. Cross-facet contract broken.

# Convergence trace

None of the above findings correspond to auditor findings in the r2 report. The auditor's flag-012 (CURVE-001) notes 1→3 jumps at @11 and @162 but does not address sensory old-state lineage. The auditor's TF-001 (flag-019) pre-flags the @162 pile-up for audience adversarial gate but that is a vibes matter, not sensory. The auditor ran no per-entry loc-state baseline scan against sensory.md; these five callouts are exclusive to this reviewer's scope and represent the seam the mechanical scan did not cover.

Note: sensory:3 @43 old-state `apothecary-interior-warm` inherits correctly from sensory:2's new-state on the thermal modality — that inheritance chain is formally traceable. However the chain originates from sensory:2's unanchored `eastern-quarter-alley-cold` old-state, so the downstream entry is built on a broken foundation; if sensory:2 is revised, sensory:3's old-state must also be revised.
