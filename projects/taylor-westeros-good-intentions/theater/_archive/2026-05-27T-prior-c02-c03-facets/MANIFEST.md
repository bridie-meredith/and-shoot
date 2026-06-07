# Archive MANIFEST — prior c02 + c03 facet working set

archived_at: 2026-05-27T00:00:00Z
archived_by: /and-facets b01-c04 Phase 0 step 5 (cross-chapter facet-namespace clearance)
reason: c02 + c03 facet files present in theater/facets/ at start of c04 facet run; auto-archived per URI-FACETS-CROSS-CHAPTER-ARCHIVE.

## Contents
- facets/: 16 chapter-namespaced facets (c02: 8 + c03: 8) + 7 shared-name facets (which belonged to c03, the most recent chapter per _cite-index.md header)
- proto-lines/: 2 files (b01-c02.md + b01-c03.md)
- facets/_inflight/: if present, stale working dir

## NOT archived (per spec)
- scene-map-b01-c04.md (current chapter)
- theater/bones/ (cross-chapter persistent)
- staff/exposition-author/glossed-terms.md (cross-chapter register)
- All card.md files (cross-chapter persistent)
- staff/auditor/ + staff/audience/ verdicts (cross-chapter audit trail)

## Restore command
cp -rn /home/user/and-shoot/active-project/theater/_archive/2026-05-27T-prior-c02-c03-facets/facets/* /home/user/and-shoot/active-project/theater/facets/
cp -rn /home/user/and-shoot/active-project/theater/_archive/2026-05-27T-prior-c02-c03-facets/proto-lines/* /home/user/and-shoot/active-project/theater/proto-lines/

(Restore is to undo the archive; only use if you need to recover c02 or c03 facets — they remain in this archive intact for /and-stitch or post-hoc inspection.)
