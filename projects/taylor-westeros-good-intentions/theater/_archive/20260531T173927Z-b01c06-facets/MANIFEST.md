archive: b01c06 facet working set
created_at: 2026-05-31T17:39:27Z
reason: /and-facets b01c08 Phase 0 step 5 cross-chapter collision auto-archive (URI-FACETS-CROSS-CHAPTER-ARCHIVE, 2026-05-21)
trigger: shared theater/facets/ + theater/dialogue/ namespaces held b01c06 working files when /and-facets b01c08 dispatched

contents:
  - theater/facets/ — 16 files (all b01c06 R1+R2 facet outputs + _cite-index.md + scene-map-b01-c06.md)
  - theater/dialogue/wren-stitch-maker-flea-bottom-ward.md — b01c06 dialogue
  - theater/proto-lines/ — canonical merged proto-line file
  - staff/auditor/ — c06 audit reports
  - staff/audience/<persona>/ — c06 verdict files
  - staff/dialogue-writer/ — c06 drafts sidecars
  - staff/fixer/ — c06 remediation logs
  - r2-decision-shards (where present)

NOT archived (cross-chapter persistent):
  - cards/, schemas/ (library-global)
  - theater/bones/ (per-chapter, immutable history)
  - staff/exposition-author/glossed-terms.md (cross-episode register)
  - theater/facets/scene-map-b01-c08.md (current chapter)
  - active-project/theater/dialogue/oswyn-mudway-flea-bottom-elder.md (RESTORED — was tagged b01c08, was b01c08 dialogue file co-emitted by /and-write Phase 7; only filename shape collided with c06 archive sweep)

restore command (full chapter recovery):
  cp -rn active-project/theater/_archive/20260531T173927Z-b01c06-facets/theater active-project/
  cp -rn active-project/theater/_archive/20260531T173927Z-b01c06-facets/staff active-project/
