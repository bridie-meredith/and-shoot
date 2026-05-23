# /and-facets b01c02 — R2 shared judge brief

chapter: b01c02  (file-form: b01-c02)
cite_index_sha: 7fb82f0caa9c055b998f3e5ea32bda516cd64f170329d49a22f8fb11a39d08f6
  → every R2 decision-shard MUST carry `cite_index_hash: 7fb82f0caa9c055b998f3e5ea32bda516cd64f170329d49a22f8fb11a39d08f6`
    in its frontmatter (URI-FACETS-R2-STALE-SHARD / A6).

## What R2 is

R2 is GRAPH-AWARE judging. Every judge sees the full locked R1 graph:
- All facet files: active-project/theater/facets/{location-state,interest-narrator,sensory,
  state-updates,memory,feeling,metaphor,vibes,exposition-b01-c02}.md
- Per-character dialogue files: active-project/theater/dialogue/{taylor-hebert-kl-122ac,
  wren-stitch-maker-flea-bottom-ward}.md
- Cite-index: active-project/theater/facets/_cite-index.md
- Canonical proto-lines: active-project/theater/proto-lines/b01-c02.md
- Scene-map: active-project/theater/facets/scene-map-b01-c02.md
- Locked rubric: design/shoot-v2/r2-judge-tuning/B-locked-rubric.md (gates G1-G5 as taste-questions)
- Arbiter protocol: design/shoot-v2/r2-judge-tuning/C-arbiter-protocol.md (T1, T4)

## Discipline

- Single-pass per judge. No mid-layer rebuild. You see the locked R1 graph; you do NOT
  see other judges' R2 mutations.
- Self-scoped deletion only — you may delete only your own facet's entries. Deleted IDs
  leave gaps (no renumbering). New entries take next-available IDs.
- Add-cap ≤5 per judge (metaphor ≤3; dialogue ≤3 per character). Cap-refusals logged in shard.
- §Form re-test before every KEEP / DELETE / REVISE verdict (operationalises G1).
- Position-gate (G5) on adds: every add carries a position-category note
  (approach-zone / peak / trailing-edge / post-peak / quiet-beat / denouement).
- Provisional-anchor binding: R1 metaphor/vibes/dialogue entries with descriptive or
  `DEFERRED-TO-R2` `licensed-by:` / facet-license hints get resolved here against the
  locked graph. A hint that cannot resolve cleanly → DELETE the entry as unanchorable.

## R1 seams flagged for R2 attention

- metaphor meta:1 @28 cites `feeling:PROVISIONAL` — resolve against feel:2 @28 (exists).
- dialogue entries carry `facet-licenses: [DEFERRED-TO-R2]` — resolve each to a concrete
  `<facet>:<id> @<anchor>` in the locked graph or SIGNAL per rubric.
- memory mem:2 @25 is a peak-bone fire (scene-C peak-bones @25 @28) — contested; the R1
  author defends it under the displacement-clamp exception. R2.2 adjudicates explicitly.
- exposition entries 2 (water-carrier @2) and 3 (near-witness @8) — thin definite-description
  individuals; R2.5 checks whether loc-state / narrator-interest lens facets already carry them.
- vibes culled the @28 atonement entry — scene-C @28 carries no vibe; note only.

## Output per judge

- Mutated facet file in place (deletes leave gaps; adds take next ID).
- Decision-shard at staff/<facet>/r2-decision-shard.md (feeling: r2-decision-shard-<slug>.md;
  dialogue: r2-decision-shard-<character>.md) — frontmatter MUST carry the cite_index_hash
  above, plus per-shard `f-r2-counts:` and verdict justifications (name concrete entry
  content, quote phrases — avoid rubric-label-only justifications, which trip arbiter T1).
- Annotated proto-lines copy under active-project/theater/facets/_inflight-r2/ reflecting
  your citation cascades + adds:
    proto-lines-<facet>.md           (single-file facets)
    proto-lines-feel-<character-slug>.md      (feeling per-character)
    proto-lines-dialogue-<character-slug>.md  (dialogue per-character — character-slug, NOT card-slug)
  Copy the canonical proto-lines BYTE-IDENTICAL; append/strip only your own facet-prefix tokens.

Honor the Earth-Bet hard fence absolutely. Return: mutated facet path, shard path,
_inflight-r2 copy path, K/D/A counts, cap-refusals, flagged seams.
