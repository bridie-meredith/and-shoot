# Scene Map Schema

The scene-map is a derived structural artifact emitted at `/and-facets` Phase 4c (alongside cite-index rebuild). It enumerates the episode's scenes as machine-readable ranges over proto-line IDs. The stitcher's Phase 1 scene-window mode reads this file to resolve fork boundaries; the auditor reads it to verify per-scene caps (sensory ≤3 per scene, feeling ≤1 per character per scene, metaphor ≤1 cross-character per scene, exposition `scene-open-orient` ≤1 per scene).

Schema authority: this file.

Status: **draft (2026-05-13)** — promoted from tensometer scene-footer prose to first-class facet emission per URI-SCENE-WINDOW.

---

## File path

```
active-project/theater/facets/scene-map-<episode-slug>.md
```

One file per episode. Auto-derived; not human-authored.

---

## Authoring

**Author:** `/and-facets` Phase 4c orchestrator (mechanical derivation; not an Agent dispatch).

**Sources combined:**
- `theater/facets/tensometer-<slug>.md` — scene-footer section names canonical scenes (A, B, E, H, L, …) with file-position ranges; scene-map uses these names verbatim.
- `theater/facets/location-state.md` — location-card transitions mark scene boundaries when the tensometer prose is sparse.
- `theater/facets/interest-narrator.md` — sparsity gradient and time-skip cognition mark soft scene boundaries.
- `theater/proto-lines/<slug>.md` — blank lines (time-skip markers) mark hard scene boundaries.

**Derivation algorithm (Phase 4c emits in this order):**
1. Walk proto-lines; record blank-line positions as candidate boundaries.
2. Walk loc-state entries; merge any location transitions onto the candidate boundary list.
3. Walk NI sparsity gradient; merge any time-of-day cognition entries onto the candidate boundary list.
4. Read tensometer scene-footer; reconcile canonical labels (A, B, …) against candidate boundaries. The tensometer is the labelling authority — its named scenes win when candidate boundaries disagree on count.
5. For each scene, derive `<location-slug>` from the scene's plurality loc-state entry, `<time-of-day>` from NI cognition or scene-open exposition, and `<one-line>` from the tensometer's narrated description (truncated to ≤80 chars).
6. Validate coverage: every bone in proto-lines falls inside exactly one scene's range.

---

## File structure

YAML-ish frontmatter, body of structured scene-blocks (one block per scene), coverage footer.

```
scene-map: <episode-slug>
generated: <ISO date>
source: derived from tensometer + location-state + interest-narrator + proto-lines
auto-derived: true
total-scenes: <N>
total-bones: <N>
---

scene-A @<start>-@<end> | <location-slug> | <time-of-day> | <one-line>
  rhythm-shape: <flat-low | rising | rising-to-peak | peak-and-release | double-peak | flat-mid | resolving | release-only>
  peak-bones: <@<id>=<tens>, @<id>=<tens>, ...> | none
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

- **`<scene-label>`** — `scene-A`, `scene-B`, …, `scene-Z`. Inherits naming from the tensometer's scene-footer. New scenes detected by derivation but absent from the tensometer's footer get labels continuing the alphabetic sequence.
- **`@<start>-@<end>`** — closed range over proto-line IDs (inclusive both ends). `<start>` and `<end>` are bone IDs as written in `theater/proto-lines/<slug>.md`. Single-bone scenes use `@<id>-@<id>`.
- **`<location-slug>`** — slug of the location card most-cited by loc-state entries in the scene's range. Multi-location scenes use the location of the scene's anchor-cluster (first non-transitional bone). `<location-slug>: unstated` is permitted for purely interior/perceptual scenes.
- **`<time-of-day>`** — `dawn | morning | midday | afternoon | dusk | night | overnight | continuous` (continuous = no time-jump from prior scene). Free-form descriptors permitted only when the listed values do not fit (e.g. `late-morning`).
- **`<one-line>`** — ≤80 characters. The tensometer's narrated description of the scene, condensed. NOT a plot summary; a structural orienter (e.g. "first tanner-visit; father presents trade goods; mother addresses Taylor with Tya-name").

### Per-scene tens-aware fields (URI-SCENE-RHYTHM, 2026-05-13)

Each scene's header line is followed by an indented block of structural descriptors derived from the tensometer's per-bone tens scores within the scene's range. These give the stitcher concrete bone-level rhythm guidance without changing tens authoring upstream.

- **`rhythm-shape`** — structural descriptor of the scene's tens topology. One of:
  - `flat-low` — all bones in the scene are tens=1 (transition scenes; relay sweeps; logged-and-moved).
  - `flat-mid` — sustained tens=2 across the scene with no rupture (pressure beats; stakes visible, no peak).
  - `rising` — tens climbs from tens=1 to tens=2 over the scene's body, no tens=3 (approach scenes; setup beats).
  - `rising-to-peak` — tens climbs to a tens=3 by the scene's end or near-end (full arc with rupture at climax).
  - `peak-and-release` — tens=3 in the scene's first or middle third with low tail (rupture early, settle after).
  - `double-peak` — two tens=3 bones with separation (rare; complex scene with two ruptures).
  - `resolving` — descending from a prior-scene-carried tens to flat-low (release after climax in prior scene).
  - `release-only` — short scene of flat-low bones acting as post-peak settle from prior scene.

- **`peak-bones`** — comma-separated list of bone IDs with tens ≥ 2 in this scene, each with its tens value: `@<id>=<2|3>`. `none` when the scene is flat-low. Peak bones MUST be rendered standalone (no fusion across peak-bone boundaries) — this is the long-standing peak-stands-alone discipline, formalized here so the stitcher reads it from the scene-map rather than re-deriving it.

- **`peak-shadow-bones`** — comma-separated list of tens=1 bone IDs immediately adjacent to a peak bone (±1 bone). `none` when the scene has no peaks. Peak-shadow bones inherit the standalone discipline — they are the charge-and-release pacing around the peak. The stitcher MUST NOT fuse these even across consecutive tens=1 bones, because the short-sentence rhythm flanking a peak is load-bearing pacing.

- **`fusion-eligible-runs`** — comma-separated list of bone-range subsegments that are runs of 3+ consecutive tens=1 bones, none of which are in `peak-shadow-bones`. `none` when no run meets the criteria. The stitcher MAY fuse aggressively across these runs (multi-bone same-subject merge, em-dash continuation, semicolon parallel-list); fusion does NOT need to refuse on peak-adjacency grounds because the derivation already excluded peak-shadow bones. This field is the lever that addresses bone-percussion in low-charge stretches — it tells the stitcher exactly where the fusion-license is safe to spend.

- **`protected-patterns`** — comma-separated list of structural patterns detected in the scene, each with its bone range. Format: `<pattern-name> @<start>-@<end>`. Examples: `log-trio @45-@47`, `three-note-buildup @148-@150`, `cardinal-quartet @60-@63`, `routing-countdown @75-@78`. `none` when no protected pattern fires. Protected patterns stay protected regardless of fusion-eligibility — a log-trio that overlaps a fusion-eligible-run is still a log-trio; the stitcher picks a variant within the protected-pattern's variant set (canonical / compressed / single-verb / truncated-tail) rather than collapsing it. Pattern detection is the same as `phase-1.protected-patterns` in the stitch profile; the scene-map pre-computes the locations.

### Field-derivation algorithm

The orchestrator (no Agent dispatch) computes these fields mechanically at `/and-facets` Phase 4d, after the scene boundaries are reconciled:

1. **For each scene**, walk the tensometer's per-bone entries inside the scene's `@<start>-@<end>` range.
2. **Determine `rhythm-shape`**: classify the tens topology per the descriptors above. Use simple rules:
   - All tens=1 → `flat-low`.
   - All tens=2 → `flat-mid`.
   - Has a tens=3 in last 33% of scene → `rising-to-peak`.
   - Has a tens=3 in first 33% of scene → `peak-and-release`.
   - Has two or more tens=3 → `double-peak`.
   - Tens climbs (max increases monotonically) without hitting 3 → `rising`.
   - Tens descends from a prior-scene-carried peak → `resolving`.
   - Otherwise short flat-low post-peak → `release-only`.
3. **Compute `peak-bones`**: enumerate every bone with tens ≥ 2 in the scene; format `@<id>=<tens>`.
4. **Compute `peak-shadow-bones`**: for each peak bone, include the immediately-prior and immediately-next bone IDs (if they exist within the scene's range AND have tens=1). Deduplicate.
5. **Compute `fusion-eligible-runs`**: walk the scene's tens=1 bones; group consecutive runs of length ≥3; exclude any bone in `peak-shadow-bones`. Emit each surviving run as `@<start>-@<end>`. A run interrupted by a peak-shadow bone splits into two shorter runs (each of which only emits if it independently has length ≥3).
6. **Compute `protected-patterns`**: run pattern detectors against the scene's bone sequence (log-trio: 3+ bones matching `S opens/writes/closes log` morphology; cardinal-quartet: 4 sequential `<fauna> spread <area>` bones; three-note-buildup: 3 bones with monotonic ordinal verbs on same subject; etc.). Emit detected patterns with their bone ranges. Pattern definitions follow `phase-1.protected-patterns` from the stitch-profile schema.

### Boundary-carry note (for season-spanning episodes)

When an episode opens with bones carrying through from the prior episode's close (per `/and-season` Phase 3 S10 Step 4 boundary-carry discipline), the first scene's `@<start>` is the boundary-carry bone's ID (which may not be `@1`). The frontmatter's `total-bones` counts all bones in this episode's proto-lines, including boundary-carries.

---

## Coverage validation

Phase 5 audit (`/and-facets`) enforces:

| Check | Severity | Fault |
|---|---|---|
| Every bone in `proto-lines/<slug>.md` falls inside exactly one scene's range | HARD | `FAULT-SCENE-MAP-COVERAGE-GAP @<id>` (uncovered) or `FAULT-SCENE-MAP-COVERAGE-OVERLAP @<id>` (in 2+ scenes) |
| Every scene's `@<start>` and `@<end>` resolve to existing bone IDs | HARD | `FAULT-SCENE-MAP-DANGLING-ANCHOR scene-<label> @<id>` |
| Scene-labels are unique within the file | HARD | `FAULT-SCENE-MAP-DUPLICATE-LABEL scene-<label>` |
| Scene-labels are monotonic alphabetic (A < B < C < …) | SIGNAL | `WARN-SCENE-MAP-LABEL-ORDER` (out-of-sequence labels are derivation-correct but harder to read) |
| Total-scenes in frontmatter matches body line count | HARD | `FAULT-SCENE-MAP-COUNT-MISMATCH` |
| Total-bones in frontmatter matches proto-lines bone count | HARD | `FAULT-SCENE-MAP-BONE-COUNT-MISMATCH` |

These checks land under the auditor's CONSTRAINT class. Coverage gaps and overlaps are non-bypassable — `/and-facets` cannot reach `audited-r1` with an unclean scene-map.

---

## Consumers

| Consumer | Reads | Uses for |
|---|---|---|
| `/and-stitch` Phase 1 (scene-window mode) | Full file | Fork boundaries (one fork per scene); back-look context (rendered prior scene); forward-look context (next scene's bones+facets); per-scene `rhythm-shape` (variance posture); `peak-bones` + `peak-shadow-bones` (standalone discipline); `fusion-eligible-runs` (multi-bone fusion license); `protected-patterns` (variant selection within protection) |
| `/and-stitch` Phase 0.5 pre-flight | Frontmatter | Scene count for the user-visible summary line |
| `/and-facets` Phase 5 audit (CONSTRAINT) | Full file | Per-scene caps (sensory ≤3, feeling ≤1/char, metaphor ≤1 cross-char, exposition scene-open-orient ≤1) — each cap reads the scene boundary from this file |
| `/and-wrap` editor (future) | Full file | Scene-cut marker placement; rhythm-shape informs scene-level prose pass |

---

## What this schema does not cover

- **Sub-scene beats.** A scene's internal structure (rising action, peak, release, etc.) is the tensometer's domain. Scene-map is boundaries only.
- **Cross-episode scene continuity.** When scene-N of episode E continues from scene-N of episode E-1 (e.g. an interrupted exchange resuming after a chapter break), there is no machine link — both episodes' scene-maps stand alone. Continuity is the reader's perception, not a graph relation.
- **Authored override.** The scene-map is purely derived. Human override of a scene boundary requires editing the underlying tensometer/loc-state/NI source and re-running Phase 4c. No direct edits to the scene-map file (any such edit would be overwritten on next `/and-facets` run).
