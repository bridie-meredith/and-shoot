# Plan A — A4 rubric portability audit

**Date:** 2026-05-10
**Plan:** `design/shoot-v2/plan-and-season-followon-2026-05-10.md` §A4 risk note.
**Question:** do sensory / state-updates env / loc-state rubrics share the tens rubric's per-episode-post-split calibration constraint, or can they be authored at aggregate scope?

---

## Tens (baseline reference)

Per `design/shoot-v2/rubric-tensometer.md` and the URI-026 §Context line 13 invocation:
- Curve-shape rubric is **per-episode-scoped** — scene-level peak + episode-level act structure.
- Unique-climax-per-episode assumption: a single peak stretch per episode.
- Calibrated corpus: ~150 lines per episode.
- Routing: **per-episode post-split** (not aggregate). Step 1.5 authors `tensometer-<season-slug>e<NN>.md` per proposed episode after Phase 4 split proposal.

**This is the structural pattern A4 must mirror unless a rubric demonstrably runs at aggregate scope.**

---

## Sensory

Per `design/shoot-v2/rubric-sensory.md`:

**Per-entry axes (modality-inflection / disambiguation-discipline / magnitude / audience-side perceptibility) — aggregate-portable.** No episode-boundary dependence.

**Curve-shape rubric — episode-bound:**
- Sparsity: **3–6% of proto-lines fire**. Density band defined relative to episode size (~77 beats → ~2–5 entries).
- **Modality-coverage health-check: ≥2 modalities represented across the file.** "The file" is the per-episode file. Authoring at aggregate scope and splitting after risks producing post-split episode files that monoculture (e.g., aggregate has 6 modalities total, but episode-3-post-split has only sound).
- Per-scene cap ≤3 — scene-local, portable.
- Inflection-pair coherence — local, portable.

**Verdict: per-episode-post-split required.** Same routing as tens. Aggregate authoring cannot guarantee post-split modality coverage; the file-level health check is calibrated per-episode and must run per-episode.

**Routing recommendation:** new `/and-season` Pass S5.5 (or Step 1.6 in Phase 4) authors per-proposed-episode `sensory-<season-slug>e<NN>.md`. Same shape as tens Step 1.5; output path slug-suffixed; renamed to `sensory.md` by `/and-shoot` Phase 0.

---

## State-updates (env subset)

Per `design/shoot-v2/rubric-state-updates.md`:

**Per-entry axes (reality / authority / frugality) — aggregate-portable.**

**Curve-shape rubric — episode-bound and tens-coupled:**
- Sparsity band: **8–18% of proto-lines** (~6–14 entries on 77 beats). Per-episode density.
- **Density alignment with tensometer transitions and peaks:** "Ratio of fires-per-beat in non-1 zones should exceed ratio in 1-only stretches by at least 2×, ideally 3×." Tens-coupled. Since tens is per-episode-post-split, state-updates density-alignment must also be per-episode-post-split.
- **Target diversity across the file:** "Across an episode of >50 beats, expect entries across at least three target classes." Per-episode check.
- "At least one fire per scene-with-irreversible-event" — scene/episode-local.
- "Approach-zone permitted-silent" — episode-opening-local.

**Note:** the plan scopes A4 to "state-updates env" — i.e., `studio.*` and `prop:*.*` entries written by studio. The `actor:*.*` entries (POV-character actor-state) are a different authorship and may stay where they are. The env subset is what migrates.

**Verdict: per-episode-post-split required.** Tens-coupling alone forces per-episode scope. Density and target-diversity bands are also episode-calibrated.

**Routing recommendation:** new `/and-season` Pass S5.6 (or Step 1.7 in Phase 4) authors per-proposed-episode `state-updates-env-<season-slug>e<NN>.md` (env subset only — `studio.*` + `prop:*.*`). Same shape as tens Step 1.5. The actor subset is **not** migrated; `/and-facets-r1` retains the actor-state authoring path.

---

## Location-state

Per `design/shoot-v2/rubric-location-state.md`:

**Per-entry axes (necessity / interestingness / frugality) — aggregate-portable.**

**Curve-shape rubric — minimal episode-bound content:**
- "The default for any anchor proto-line is *no entry*. Sparse by design." No explicit density band.
- Frugality is **location-and-moment-local**: "One loc-state entry licenses every subsequent proto-line in the same location-and-moment until the move changes." Inheritance scope is location, not episode.
- No tens-coupling.
- No file-level shape rubric explicitly stated.

**Risk:** the implicit "first beat in a new location-and-moment" anchor depends on knowing which beat is "first." Across an aggregate, this is well-defined (read forward, fire on first entry to each location-and-moment). Across an episode-post-split, the first beat of an episode is also a first-beat-in-location-and-moment (regardless of whether the prior episode visited the same location). Aggregate authoring would under-fire on the first beats of post-split episodes.

**Verdict: per-episode-post-split required (lighter justification).** The justification is weaker than for sensory or state-updates — loc-state's rubric is mostly location-local — but the post-split episode-opening anchor matters. Routing per-episode-post-split is the safe-and-consistent choice that mirrors tens, sensory, and state-updates env.

**Routing recommendation:** new `/and-season` Pass S5.7 (or Step 1.8 in Phase 4) authors per-proposed-episode `location-state-<season-slug>e<NN>.md`. Same shape as tens Step 1.5.

---

## Aggregate verdict

All three migrated facets share the per-episode-post-split routing pattern:

| Facet | Per-entry axes | Curve/file shape | Tens-coupled | Routing |
|---|---|---|---|---|
| **tens** (already migrated) | aggregate-portable | per-episode (unique-climax + act-shape) | self | per-episode-post-split |
| **sensory** | aggregate-portable | per-episode (sparsity 3–6%, modality coverage ≥2) | no | **per-episode-post-split** |
| **state-updates env** | aggregate-portable | per-episode (sparsity 8–18%, density alignment, target diversity) | yes | **per-episode-post-split** |
| **location-state** | aggregate-portable | minimal episode-bound (location-and-moment-local) | no | **per-episode-post-split** (consistency) |

A4 spec implementation: each migrated facet gets a Step 1.x in Phase 4 mirroring tens Step 1.5 (parallel dramatist/studio fork per proposed episode), a Step 2 mechanic-arithmetic auditor invocation against the appropriate rubric class library, and `/and-shoot` Phase 0 rename contract `<facet>-<season-slug>e<NN>.md → <facet>.md`. `/and-facets-r1` Layer for each migrated facet is **deleted**, not deprecated.

**Open question for A4 implementation:** the auditor class library at `.claude/commands/and-facets-audit.md` defines FREQUENCY-BAND / CURVE-SHAPE / AP-SCAN classes. Are there equivalent class definitions for sensory / state-updates env / loc-state, or do we need to add them? If absent, the bone-gate mechanic-arithmetic invocation has no shared rubric to cite — A4 then includes a class-library extension as part of the spec edit.

---

## Implementation notes (staged for A4 execution)

When A4 fires (after A3 validates s02 with the existing tens bone-gate), the spec edits are:

1. **`.claude/commands/and-season.md` Phase 4:** add Step 1.6, Step 1.7, Step 1.8 mirroring Step 1.5. Each new step authors per-proposed-episode `<facet>-<season-slug>e<NN>.md`.
2. **`.claude/commands/and-season.md` Phase 4 Step 2:** extend the mechanic-arithmetic auditor invocation to consume the new per-episode files. Cite the class library in `.claude/commands/and-facets-audit.md`.
3. **`.claude/commands/and-facets-r1.md`:** delete Layer for each migrated facet.
4. **`.claude/commands/and-shoot.md` Phase 0:** extend the rename contract.
5. **`schemas/facet.schema.md`:** extend the dual-provenance note (currently tens-only) to sensory / state-updates env / loc-state.
6. **`.claude/commands/and-facets-audit.md`:** if absent, add CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN class definitions for sensory / state-updates env / loc-state. (Open question above.)
7. **Validation re-fire:** `/and-season s02` runs again with all four bone-gates active. Per the plan: ~6 added dispatches per facet × 3 facets = ~18, parallelizable.

Bone-gate dispatch budget after A4: tens (~6) + sensory (~6) + state-updates env (~6) + loc-state (~6) = ~24 just for Phase 4 Step 1.x authoring. Mechanic auditor invocations × 4 facets × per-episode = additional ~24. Total Phase 4 bone-gate ~48 dispatches at worst case (parallelized per-episode, wall-clock dominated by slowest fork). The orchestrator-critic R1 hard cap of 60 dispatches per `/and-season` run is **breached at worst case** — A4 implementation must include a dispatch-budget recalibration, either by raising R1 or by accepting tightened iteration caps on the new gates.
