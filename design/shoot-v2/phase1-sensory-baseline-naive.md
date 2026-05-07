# Phase 1 — Sensory-Flags Naive Baseline (rubric-blind)

Phase 1 baseline writer-fork, rubric-blind. Authored against the schema's pre-rename "loudness flags" definition only:

> ### loudness flags (`facets/loudness.md`)
>
> Volume spikes and drops. Sparse — only at inflection points.
>
> ```
> <id> @<proto-line-id> <up|down|spike|drop> <one-clause description>
> ```
>
> **Author:** studio.

The author has access to the proto-line file (`active-project/theater/proto-lines/s01e01.md`), the locked location-state file, and the locked tensometer file. The author does NOT have access to: the V1 sensory rubric, the corpus-selection note, the user's pre-Phase-0 framing, the multi-modal rename, the disambiguation-not-redundancy gate, the magnitude-sufficiency gate, or any of the four mid-Phase-0 user nudges.

This output is the **baseline to beat** for Phase 1 review. Expected naive failure modes per corpus § "Predicted naive failure modes":

1. Charged-word redundant flagging (sound-equivalents only here since schema is volume-only)
2. Sustained-as-inflection (multiple officer-speech beats)
3. Fauna-feed-extension fires
4. Density-on-charged-tens
5. Modality-monoculture (sound-only — but here that's by-design since schema says volume; the rename to multi-modal is a tuning addition, not naive baseline failure)
6. Generic descriptions

---

```
facet: loudness
episode: s01e01
author: studio (Phase 1 baseline; rubric-blind)
---
1 @13 up the officer's voice rises over the yard murmur
2 @21 up the officer continues addressing each ward
3 @24 drop the stylus stops abruptly on the board
4 @30 up the stylus resumes on taylor's name
5 @38 spike the moment of the letter pressed forward goes quiet
6 @41 spike the wax seal cracks under the officer's thumb
7 @47 up the officer's voice returns dictating the entry
8 @57 drop edric's footsteps recede through the doorway
9 @58 up the stylus resumes its rhythm on the board
10 @64 spike two parallel lines marked beside the entry
11 @67 spike the officer's foot moves toward the horse
12 @69 drop the wheel-tremor leaves the verge-beetles east
```

12 entries on 77 beats = 15.6%.

---

## Notes from naive author

- Schema says "volume spikes and drops" — interpreted as sound-only.
- Schema says "sparse — only at inflection points" — interpreted as: fire wherever volume changes are detectable in the proto-line text.
- Studio author uses environmental description style.
- Tagged each entry per the schema's `<up|down|spike|drop>` enumeration.
- Did not consult any rubric beyond the schema definition (no rubric was provided).
