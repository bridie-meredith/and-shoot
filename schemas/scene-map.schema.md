# Scene Map Schema

The scene-map is a structural artifact emitted by `/and-write` Phase 7 from `chapters[].scenes[].bones[].substance_delta.axis_moves.magnitude` in showrunner memory, plus per-scene `dramatic_shape` declarations. It enumerates the chapter's scenes as machine-readable ranges over bone IDs. The stitcher's Phase 1 scene-window mode reads this file to resolve fork boundaries; the auditor reads it to verify per-scene caps (sensory ≤3 per scene, feeling ≤1 per character per scene, metaphor ≤1 cross-character per scene, exposition `scene-open-orient` ≤1 per scene).

Schema authority: this file.

Status: **revised 2026-05-19 (URI-SUBSTANCE-OVERHAUL)** — rewritten from tensometer-derived shape to substance-delta-derived shape. Authoring agent is now `/and-write` Phase 7; `/and-facets` Phase 4d validates (does not derive).

---

## File path

```
active-project/theater/facets/scene-map-<book>-<chapter>.md
```

One file per chapter. Emitted by `/and-write` Phase 7; not human-authored; not subject to R1/R2 review or audience-gate.

---

## Authoring

**Author:** `/and-write` Phase 7 orchestrator (emitted from substance_delta data in showrunner memory; not an Agent dispatch).

**Sources:**
- `chapters[<slug>].scenes[].bones[].substance_delta.axis_moves.magnitude` from showrunner memory — the pressure-signal source replacing the pre-overhaul tensometer per-bone scalar.
- `chapters[<slug>].scenes[].dramatic_shape` declarations from showrunner memory — scene-level shape intent.
- `theater/bones/<book>-<chapter>.md` — bone IDs and sequence used to compute ranges.

**Emission algorithm (Phase 7 emits in this order):**
1. Walk `chapters[<slug>].scenes[]` from showrunner memory. Each scene entry names its bone range.
2. For each scene, read the `substance_delta.axis_moves.magnitude` values across all bones in the scene's range.
3. Derive `rhythm-shape` from aggregated magnitudes (see field definitions below).
4. Derive `peak-bones` as the set of bones whose magnitude crosses the scene-window's 75th percentile OR magnitude ≥ 0.15.
5. Derive `peak-shadow-bones` as the bones immediately adjacent (±1 bone) to each peak bone, if those neighbors exist within the scene range and are not themselves peak bones.
6. Derive `fusion-eligible-runs` as contiguous runs of bones inside a single `flat-low` or `resolving` rhythm zone with no per-bone `substance_delta` cost-ledger-anchor citations (i.e., bones that are pure orientation/work with no axis-moving costs paid). Minimum run length: 3 bones.
7. Detect `protected-patterns` in the scene's bone sequence per the pattern definitions in the stitch-profile schema.
8. Validate coverage: every bone in the bones file falls inside exactly one scene's range.

**Override path:** revise the underlying substance contract in showrunner memory or re-run `/and-write`. No direct edits to the scene-map file (any such edit would be overwritten on next `/and-write` Phase 7 re-run).

---

## File structure

YAML-ish frontmatter, body of structured scene-blocks (one block per scene), coverage footer.

```
scene-map: <chapter-slug>
generated: <ISO date>
source: substance_delta.axis_moves.magnitude from showrunner memory + per-scene dramatic_shape declarations
emitted-by: /and-write Phase 7
total-scenes: <N>
total-bones: <N>
---

scene-A @<start>-@<end> | <location-slug> | <time-of-day> | <one-line>
  rhythm-shape: <flat-low | rising | rising-to-peak | peak-and-release | double-peak | flat-mid | resolving | release-only>
  peak-bones: <@<id>, @<id>, ...> | none
  peak-shadow-bones: <@<id>, @<id>, ...> | none
  fusion-eligible-runs: <@<start>-@<end>, @<start>-@<end>, ...> | none
  protected-patterns: <log-trio @<ids>, three-note-buildup @<ids>, cardinal-quartet @<ids>, ...> | none

scene-B @<start>-@<end> | <location-slug> | <time-of-day> | <one-line>
  rhythm-shape: ...
  ...

...

scene-N @<start>-@<end> | <location-slug> | <time-of-day> | <one-line>
  rhythm-shape: ...
  ...

---
coverage: <N>/<N> bones in exactly one scene
gaps: <empty | comma-separated list of uncovered bone IDs>
overlaps: <empty | comma-separated list of bones in multiple scenes>
```

### Per-scene header line shape

```
<scene-label> @<start>-@<end> | <location-slug> | <time-of-day> | <one-line>
```

- **`<scene-label>`** — `scene-A`, `scene-B`, …, `scene-Z`. Names inherited from `chapters[<slug>].scenes[].scene_id` in showrunner memory. New scenes detected in the bones file that have no matching memory entry get labels continuing the alphabetic sequence.
- **`@<start>-@<end>`** — closed range over bone IDs (inclusive both ends). `<start>` and `<end>` are bone flat_ids as written in `theater/bones/<book>-<chapter>.md`. Single-bone scenes use `@<id>-@<id>`.
- **`<location-slug>`** — slug of the location card dominant in the scene's range per showrunner memory. Multi-location scenes use the location of the scene's anchor cluster (first non-transitional bone). `<location-slug>: unstated` is permitted for purely interior/perceptual scenes.
- **`<time-of-day>`** — `dawn | morning | midday | afternoon | dusk | night | overnight | continuous` (continuous = no time-jump from prior scene). Free-form descriptors permitted only when the listed values do not fit (e.g. `late-morning`).
- **`<one-line>`** — ≤80 characters. A structural orienter derived from the scene's `dramatic_shape` and goal declarations (e.g. "first tanner-visit; father presents trade goods; mother addresses Taylor with Tya-name"). NOT a plot summary.

### Per-scene substance-delta-derived fields

Each scene's header line is followed by an indented block of structural descriptors derived from `substance_delta.axis_moves.magnitude` values for the bones in the scene's range. These give the stitcher concrete bone-level rhythm guidance without requiring any tensometer file.

The **pressure-signal source** for all field derivations is `per-bone substance_delta.axis_moves.magnitude` as stored in `chapters[<slug>].scenes[].bones[]` in showrunner memory, surfaced here through the `rhythm-shape` and `peak-bones` fields. This replaces the pre-overhaul tensometer per-bone scalar (1/2/3).

- **`rhythm-shape`** — structural descriptor of the scene's substance-delta pressure topology. One of:
  - `flat-low` — max magnitude across all bones in the scene ≤ 0.05. Transition scenes; relay sweeps; logged-and-moved.
  - `flat-mid` — magnitudes are sustained in the 0.05–0.10 band with no peak bone. Pressure beats; stakes visible, no rupture.
  - `rising` — magnitudes ascend toward the scene's end but no bone crosses the `peak-bones` threshold. Approach scenes; setup beats.
  - `rising-to-peak` — magnitudes ascend to a peak bone at or near the scene's end. Full arc with rupture at climax.
  - `peak-and-release` — one or more peak bones in the scene's first or middle third, with low-magnitude tail. Rupture early, settle after.
  - `double-peak` — two or more peak-bone clusters separated by lower-magnitude bones. Complex scene with two ruptures.
  - `resolving` — magnitudes descend from a prior-scene-carried elevation toward flat-low. Release after climax in prior scene.
  - `release-only` — short scene of flat-low bones acting as post-peak settle from the prior scene; no bone clears the peak threshold.

- **`peak-bones`** — comma-separated list of bone IDs whose `substance_delta.axis_moves.magnitude` crosses the scene-window's 75th percentile OR magnitude ≥ 0.15. `none` when the scene is `flat-low` or no bone clears either threshold. Peak bones MUST be rendered standalone (no fusion across peak-bone boundaries) — the peak-stands-alone discipline, formalized here so the stitcher reads it from the scene-map rather than re-deriving it.

- **`peak-shadow-bones`** — comma-separated list of bone IDs immediately adjacent (±1 bone) to a peak bone, if those neighbors are within the scene's range and are not themselves peak bones. `none` when the scene has no peak bones. Peak-shadow bones inherit the standalone discipline — the short-sentence rhythm flanking a peak is load-bearing pacing; the stitcher MUST NOT fuse these even across consecutive low-magnitude bones.

- **`fusion-eligible-runs`** — comma-separated list of bone-range subsegments that are contiguous runs of 3+ bones inside a `flat-low` or `resolving` rhythm zone with no per-bone `substance_delta` cost-ledger-anchor citations (i.e., bones that are pure orientation/work, no axis-moving costs paid). `none` when no run meets the criteria. The stitcher MAY fuse aggressively across these runs (multi-bone same-subject merge, em-dash continuation, semicolon parallel-list); fusion does NOT need to refuse on peak-adjacency grounds because the derivation already excluded peak-shadow bones. This field is the lever that addresses bone-percussion in low-magnitude stretches — it tells the stitcher exactly where the fusion-license is safe to spend.

- **`protected-patterns`** — comma-separated list of structural patterns detected in the scene, each with its bone range. Format: `<pattern-name> @<start>-@<end>`. Examples: `log-trio @45-@47`, `three-note-buildup @148-@150`, `cardinal-quartet @60-@63`, `routing-countdown @75-@78`. `none` when no protected pattern fires. Protected patterns stay protected regardless of fusion-eligibility — a log-trio that overlaps a fusion-eligible-run is still a log-trio; the stitcher picks a variant within the protected-pattern's variant set (canonical / compressed / single-verb / truncated-tail) rather than collapsing it. Pattern detection follows `phase-1.protected-patterns` from the stitch-profile schema.

### Pressure-signal translation reference

For rubrics and auditors reading rhythm-shape or peak-bones fields:

| Pre-overhaul language | Scene-map equivalent |
|---|---|
| `tens=1` / "quiet beat" / "low-charge" | scene in `rhythm-shape: flat-low` OR `rhythm-shape: resolving` |
| `tens=2` / "building" / "ramp" | scene in `rhythm-shape: rising` |
| `tens=3` / "peak" / "high-charge" | bone listed in scene's `peak-bones` |
| `tens=2 trailing edge` / "release zone" | scene in `rhythm-shape: release-only` OR `resolving` |
| "inverted tens-density alignment" | "inverted pressure-signal alignment" (memory fires concentrate in `flat-low` / `resolving` zones; NI fires concentrate in `rising` zones and on `peak-bones`) |

---

## Coverage validation

`/and-facets` Phase 4d enforces:

| Check | Severity | Fault |
|---|---|---|
| Every bone in `theater/bones/<book>-<chapter>.md` falls inside exactly one scene's range | HARD | `FAULT-SCENE-MAP-COVERAGE-GAP @<id>` (uncovered) or `FAULT-SCENE-MAP-COVERAGE-OVERLAP @<id>` (in 2+ scenes) |
| Every scene's `@<start>` and `@<end>` resolve to existing bone IDs | HARD | `FAULT-SCENE-MAP-DANGLING-ANCHOR scene-<label> @<id>` |
| Scene-labels are unique within the file | HARD | `FAULT-SCENE-MAP-DUPLICATE-LABEL scene-<label>` |
| Scene-labels are monotonic alphabetic (A < B < C < …) | SIGNAL | `WARN-SCENE-MAP-LABEL-ORDER` |
| Total-scenes in frontmatter matches body line count | HARD | `FAULT-SCENE-MAP-COUNT-MISMATCH` |
| Total-bones in frontmatter matches bones file bone count | HARD | `FAULT-SCENE-MAP-BONE-COUNT-MISMATCH` |

These checks land under the auditor's CONSTRAINT class. Coverage gaps and overlaps are non-bypassable — `/and-facets` cannot reach `audited-r1` with an unclean scene-map.

---

## Consumers

| Consumer | Reads | Uses for |
|---|---|---|
| `/and-stitch` Phase 1 (scene-window mode) | Full file | Fork boundaries (one fork per scene); back-look context (rendered prior scene); forward-look context (next scene's bones+facets); per-scene `rhythm-shape` (variance posture); `peak-bones` + `peak-shadow-bones` (standalone discipline); `fusion-eligible-runs` (multi-bone fusion license); `protected-patterns` (variant selection within protection) |
| `/and-stitch` Phase 0.5 pre-flight | Frontmatter | Scene count for the user-visible summary line |
| `/and-facets` Phase 4d validation (CONSTRAINT) | Full file | Coverage check (every bone in exactly one scene; no dangling anchors; no duplicate labels; frontmatter counts match body) |
| `/and-facets` Phase 5 audit (CONSTRAINT) | Full file | Per-scene caps (sensory ≤3, feeling ≤1/char, metaphor ≤1 cross-char, exposition scene-open-orient ≤1) — each cap reads the scene boundary from this file |
| `/and-wrap` editor (future) | Full file | Scene-cut marker placement; rhythm-shape informs scene-level prose pass |

---

## What this schema does not cover

- **Sub-scene beats.** A scene's internal structure (rising action, peak, release, etc.) is derivable from the per-bone substance_delta values in showrunner memory, which are the source of record. The scene-map provides scene-level aggregates only.
- **Cross-chapter scene continuity.** When scene-N of chapter C continues from scene-N of chapter C-1, there is no machine link — both chapters' scene-maps stand alone. Continuity is the reader's perception, not a graph relation.
- **Authored override.** The scene-map is substance-delta-derived. To correct a scene boundary or rhythm-shape classification, revise the underlying substance contract in showrunner memory or re-run `/and-write`. No direct edits to the scene-map file.
