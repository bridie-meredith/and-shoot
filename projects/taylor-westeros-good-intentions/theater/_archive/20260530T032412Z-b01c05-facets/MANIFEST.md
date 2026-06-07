# Archive manifest

timestamp: 20260530T032412Z
reason: /and-facets b01-c06 Phase 0 step 5 (URI-FACETS-CROSS-CHAPTER-ARCHIVE) — prior-chapter (b01-c05 + older leftover) facet working set auto-archived to give the b01-c06 facet traversal a clean namespace.
moved: 133 files (theater/facets/* except scene-map-b01-c06.md; _inflight + _inflight-r2; theater/proto-lines/b01-c05.md; all staff r2-decision-shard*.md; staff/auditor/facets-* prior reports; staff/dialogue-writer drafts except c06 wren; staff/fixer/and-facets-*; staff/audience per-persona *verdict* files)
preserved (NOT archived): theater/facets/scene-map-b01-c06.md; theater/dialogue/wren-stitch-maker-flea-bottom-ward.md (c06); staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md (c06); staff/exposition-author/glossed-terms.md (cross-chapter persistent); all card.md; theater/bones/
restore: cp -rn from this archive root back into active-project/ (paths mirror active-project/ layout), e.g. `cp -rn <this-dir>/theater <this-dir>/staff active-project/`
