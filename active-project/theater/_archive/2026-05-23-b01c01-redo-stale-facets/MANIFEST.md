# Archive — 2026-05-23 b01c01 redo stale facets

**Timestamp:** 2026-05-23T00:39:12Z (bones file mtime)
**Reason:** /and-write b01c01 redo emitted a new bone set (Phase 1 fresh decomposition; Phase 4 trim deleted 2 chatter bones; Phase 7 emitted new flat_ids). Existing facets cite anchors that now resolve to different bone content. /and-facets Phase 0 anchor-refresh HARD-aborts on this state; archiving the stale facets clears the way for a clean re-traversal against the new bones.

**Triggered by:** orchestrator (/and-write b01c01 redo follow-up, before /and-facets b01-c01).

**Contents:**

### facets/
Un-suffixed b01c01-era facet files (pre-substance-overhaul naming convention, all carrying b01c01 entries):
- feeling.md
- interest-narrator.md
- location-state.md
- memory.md
- metaphor.md
- sensory.md
- state-updates.md
- vibes.md

Per-character feeling + state-updates files (additive across chapters; b01c01 entries stale):
- feeling-coll-net-mender-flea-bottom.md
- feeling-taylor-hebert-kl-122ac.md
- feeling-wren-stitch-maker-flea-bottom-ward.md
- state-updates-coll-net-mender-flea-bottom.md
- state-updates-env.md
- state-updates-taylor-hebert-kl-122ac.md
- state-updates-wren-stitch-maker-flea-bottom-ward.md

Cite-index (cross-chapter; will be rebuilt by /and-facets Phase 2):
- _cite-index.md

In-flight working dirs:
- _inflight/
- _inflight-r2/

### dialogue/
Per-character dialogue files (additive across chapters; b01c01 entries stale):
- taylor-hebert-kl-122ac.md
- wren-stitch-maker-flea-bottom-ward.md

(coll-net-mender-flea-bottom.md was absent from the prior b01c01 run — a coverage gap that the redo's /and-facets pass will close.)

**NOT archived (preserved in active-project/):**
- theater/facets/scene-map-b01-c01.md — just emitted by /and-write Phase 7 for the redo bones; this is the input for /and-facets, not stale.
- theater/facets/exposition-b01-c02.md — b01c02 chapter's facet; b01c01 redo does not invalidate.
- theater/facets/scene-map-b01-c02.md — b01c02 chapter's facet.
- theater/proto-lines/b01-c02.md — b01c02-specific.
- staff/exposition-author/glossed-terms.md — cross-chapter persistent.
- All persona / agent / behavior cards.
- theater/bones/b01-c01.md — the new emit; canonical source.
- theater/bones/b01-c02.md (if it exists).

**Restore command** (if needed before /and-facets consumes):
```
cp -rn active-project/theater/_archive/2026-05-23-b01c01-redo-stale-facets/facets/* active-project/theater/facets/
cp -rn active-project/theater/_archive/2026-05-23-b01c01-redo-stale-facets/dialogue/* active-project/theater/dialogue/
```

The b01c02 chapter's dialogue files are not in this archive — meaning if the b01c02 draft needs to be re-stitched, dialogue would need to be re-authored. b01c02 is currently at status `audited-r1` with `stitched: true`; its draft exists at `active-project/draft/b01-c02.md` as the artifact. The b01c02 facet files preserved (exposition + scene-map) are sufficient to re-stitch.
