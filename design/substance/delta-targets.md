# Delta Targets — Default Bands Per Chunk Level

Per-chunk Δ targets + bone-count bands. These are the **default bands** for `series.substance.chunk_targets.*`. The user may override at `/and-substance series` Phase 4; reviewers verify per-chunk Δ against the bands at each authoring level.

---

## Per-level Δ defaults

| level | delta_per_signature_axis | density_target | bone_count |
|---|---|---|---|
| **series** | 4–8 ranks | 0.6–0.9 | — (rolls up from books) |
| **book** | 2–4 ranks | 0.5–0.9 | — (rolls up from chapters) |
| **chapter** | 0.5–1.5 ranks | 0.5–0.9 | — (rolls up from scenes) |
| **scene** | 0–1.5 ranks | 0.6–0.9 | 5–15 bones |
| **bone** | ±1 typical, ±2–3 hinge | n/a | — (terminal) |

Where:
- **`delta_per_signature_axis`** — total Δ across the chunk, on the axes the chunk declares are in motion.
- **`density_target`** — ratio of substance-bearing bones to total bones in the chunk. 0.6 = 60% of bones cause declared Δ; remainder are setup / transition with cost-ledger ties.
- **`bone_count`** — typical number of bones per chunk at this level.

---

## Series Δ

A typical series moves the protagonist 4–8 ranks across the signature on at least one axis (commonly 2–3 axes). A series with a Δ-sum below ~4 ranks total across axes reads as a small story — fine if intended; signaled by reviewers if the chunk text suggests an epic but the contract delivers a vignette.

`series.substance.state_axes[].end_rank - state_axes[].start_rank` is summed per perspective. The series-level cost-ledger entries should account for the bulk of the gain.

---

## Book Δ — by position

Books are not interchangeable. A book's expected Δ depends on its position in the series structure:

| book position | typical Δ shape | density |
|---|---|---|
| **opening book (b01)** | 1–3 ranks; setup; high knowledge-Δ + low agency-Δ | 0.5–0.7 |
| **mid book** | 2–4 ranks; rising-action; reputation-Δ + capability-Δ peaks | 0.6–0.9 |
| **climax book** | 3–4 ranks across multiple axes; cost-ledger cashing happens here | 0.7–0.9 |
| **denouement book** | 1–2 ranks; settles the post-climax state; emotional-Δ + trust-Δ | 0.5–0.8 |

For cyclical structures (`series.structure.cyclical: true`), each book opens with the protagonist axes reset to a partial baseline (Hogwarts-school-year pattern) but world axes drift forward. Book-Δ shape adapts: each book has a rising-to-climax curve internally, with world-Δ accumulating across books.

---

## Chapter Δ

A chapter typically moves the protagonist ~1 rank on at least one axis. Some chapters move 0 ranks (atmosphere / transition — should be rare and explicitly justified). Some hinge chapters move 2+ ranks (signaled in `chapters[].dramatic_shape: climax` or `hinge`).

The chapter-Δ rolls up from its scenes — `chapters[].substance_delta.axes_in_motion[]` should equal the union of its scenes' axes in motion, with Δ summed per axis within ±1 rank.

A chapter whose contract claims Δ on an axis that none of its scenes touch is malformed (caught at `/and-substance book` Phase 5 dramatist check).

---

## Scene Δ

A scene moves the protagonist 0–1.5 ranks on the axes its `substance_delta` declares are in motion. Scenes are substantial — under the substance chain, scenes default to 1–3 per chapter. A scene that delivers no Δ at all is malformed (the scene contract's `scene_conflict` should have stakes; if stakes can't move the axes either direction, what is the scene for?).

A scene's `scene_conflict.stakes_axis` must appear in the scene's `substance_delta.axes_in_motion[]`. The scene's protagonist_force opposes its opposing_force; one wins, the stakes axis moves in that direction (or both lose and the axis moves down regardless).

---

## Bone Δ

A bone moves ±1 on one axis typically. Hinge bones (the scene's climactic action) may move ±2 or ±3 on one axis, or move two axes in one event.

**Typical:** `axis_moves: [{axis: community, direction: up, magnitude: 1}]`. One axis, direction-then-magnitude (no null direction, no zero magnitude).

**Hinge:** `axis_moves: [{axis: reputation, direction: up, magnitude: 2}, {axis: trust, direction: down, magnitude: 1}]`. Two axes, the second often paying the first.

A bone with three or more axis-moves is suspect — that much state-change in one SVO is rare; the bone is usually trying to do too much and should be split.

### Three bone shapes for "no Δ on this axis"

After the 2026-05-21 axis-bookkeeping split (`schemas/showrunner-memory.schema.md`), three distinct shapes encode "the bone did not move axis X" — and the bone-gate treats them differently:

| shape | encoding | meaning | bone-gate treatment |
|---|---|---|---|
| **Held bone** | `axes_held: [{axis: X, rationale: ...}]` | The axis was *deliberately* held flat by discipline; the holding is the scene's load-bearing event (e.g. "Taylor holds the feet" — capability held at rank 3 by choice, the prohibition enacted). | Counts toward density. The held axis is valid `scene_conflict.stakes_axis`. The rationale must name the discipline. |
| **Chatter bone** | `axis_moves: []` and no `axes_held` | Setup / transition. Does not pay an axis-move at this bone; must pay a later gain (cost-ledger link required). | Counts against density cap. Trim pass culls excess chatter. |
| **Malformed bone** | `axis_moves: [{axis: X, direction: null, magnitude: 0}]` | Rejected by schema. | HARD `FAULT-BONE-DELTA-MALFORMED` at `/and-write` Phase 2. Recast to held or chatter. |

The split exists because a chatter bone and a held-discipline bone are not the same thing — the first is incidental, the second is load-bearing — and conflating them at the bookkeeping layer hides the difference from the substance bone-gate. A held-discipline bone whose held axis is the scene's `stakes_axis` satisfies the scene contract; a chatter bone never does.

---

## Bone counts per scene

`series.structure.book_length.bones_per_scene` ranges typically `5-15`. Under the substance chain, bones are scene-action-sized — one meaningful scene-action per bone, not micro-beats.

| scene type | typical bone count |
|---|---|
| short transitional scene | 5–7 |
| standard scene | 8–12 |
| climactic / hinge scene | 12–15 |
| montage-y scene (multiple time-skips) | 10–15 with blank-numbered time-skip markers between |

Scenes under 5 bones are usually under-developed (caught at `/and-write` Phase 6 bone-gate as `BONE-COUNT-BELOW-TARGET` SIGNAL). Scenes over 15 bones risk losing the scene-action grain and should be split into two scenes (caught at `/and-substance chapter` Phase 5 dramatist check on excess `scene_count`).

---

## Density curve commentary

Density is a **curve** across a chunk, not a constant. Within a scene, bones cluster — opening bones may be lower-Δ (setup); climactic bones may be higher-Δ (the scene's hinge action). Within a chapter, scenes cluster — the opening scene may be density 0.5 (mostly setup), the climactic scene density 0.85.

Reviewers do not expect flat density across a chunk. They expect:
- **Setup chunks** (chapter opens, book opens, series-opens) — density toward the low end of the band (0.5–0.6).
- **Standard chunks** — density at band center (0.7).
- **Climactic chunks** — density toward the high end (0.8–0.9).

A chunk whose curve is inverted (climactic chunk with low density; setup chunk with high density) is flagged at Phase 5 review — the curve mismatches the chunk's stated dramatic role.

---

## Cost-ledger per-level expectations

| level | typical cost-ledger entries authored at this level |
|---|---|
| **series** | 3–8 series-spanning gain↔cost pairings (the big arc-shape costs) |
| **book** | 1–4 book-scoped entries refining series anchors to specific books |
| **chapter** | 0–2 chapter-scoped refinements (cost paid in a specific chapter) |
| **scene** | 0–1 scene-scoped refinements (cost paid in a specific scene) |

Most cost-ledger entries are authored at series level. Book/chapter/scene refinement adds specificity to existing entries (populating finer anchor fields) more than authoring new entries.

---

## Range overrides

The user can override these bands at `/and-substance series` Phase 4 by editing the `chunk_targets:` block in `signature-draft.md` before typing `accept`. The reviewer dispatches read the user-set bands; defaults only apply if the user doesn't edit.

A chunk delivering Δ outside its declared band triggers `AXIS-DELTA-MISMATCH` at the bone-gate (HARD if mismatch is beyond ±2 of band edge; SIGNAL if ±1–±2).
