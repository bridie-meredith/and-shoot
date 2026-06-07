# Archive manifest — b01c07 facet working set

timestamp: 20260531T050032Z
reason: |
  /and-facets b01c06 (depth-pass re-cascade) Phase 0 step 5 cross-chapter
  collision auto-archive. The shared facet namespace (theater/facets/*,
  theater/proto-lines/, theater/dialogue/, staff facet artifacts) was occupied
  by b01c07's working set (the prior shipped chapter). Archived to give b01c06
  a clean traversal. b01c07 already shipped (draft/b01-c07.md terminal); its
  facets are preserved here and restorable before any c07 re-stitch.
contents:
  - theater/facets/*  (all c07 facets: interest-narrator, sensory, memory,
    feeling[+per-char], state-updates[+per-char+env], metaphor, vibes,
    location-state, exposition-b01-c07, scene-map-b01-c07, _cite-index)
  - theater/facets/_inflight/* + _inflight-r2/*  (c07 R1/R2 proto-line copies)
  - theater/proto-lines/b01-c07.md
  - theater/dialogue/{taylor-hebert-kl-122ac, septon-halvard-flea-bottom}.md
  - staff/*/r2-decision-shard*.md  (c07 R2 shards)
  - staff/auditor/facets-*.md  (c07 audit + audience-gate reports)
  - staff/dialogue-writer/{taylor,halvard}.drafts.md
  - staff/audience/*/*verdict*.md  (mixed c06-original + c07 facet-gate verdicts)
kept_in_place (b01c06 current):
  - theater/facets/scene-map-b01-c06.md
  - theater/dialogue/wren-stitch-maker-flea-bottom-ward.md
  - staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md
  - theater/bones/*  (not a facet artifact)
restore: cp -rn <this-archive-root>/* active-project/   # before any c07 re-stitch
