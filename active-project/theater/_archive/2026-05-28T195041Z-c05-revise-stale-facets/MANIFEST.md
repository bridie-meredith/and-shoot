# Archive manifest

timestamp: 2026-05-28T195041Z
reason: |
  /and-facets b01c05 Phase 0 anchor-refresh HARD-ABORT gate triggered.
  Bones file was re-emitted by /and-write revise --from-signals on 2026-05-28
  with full re-numbering of flat_ids 1-31 → 1-35 (4 new bones inserted into
  s02 + s03). All facet entries authored against pre-revise flat_ids are stale.
  facets_stale_since: 2026-05-28T00:00:00Z was set in showrunner memory at
  /and-write Phase 7 emit; this archive resolves the gate so /and-facets can
  re-author against the new 35-bone scaffold.

contents:
  - theater/facets/_cite-index.md (post-R2 cite-index from pre-revise run)
  - theater/facets/_inflight/ (R1 author proto-line copies from pre-revise run)
  - theater/facets/_inflight-r2/ (R2 judge proto-line copies from pre-revise run)
  - theater/facets/exposition-b01-c05.md (3 entries; pre-revise)
  - theater/facets/feeling-taylor-hebert-kl-122ac.md (per-character slice)
  - theater/facets/feeling.md (consolidated)
  - theater/facets/interest-narrator.md (8 entries post-cycle-2)
  - theater/facets/location-state.md (9 entries)
  - theater/facets/memory.md (2 entries post-cycle-2)
  - theater/facets/metaphor.md (0 entries — chapter has no metaphor licenses)
  - theater/facets/sensory.md (3 entries post-cycle-2)
  - theater/facets/state-updates-env.md (env slice)
  - theater/facets/state-updates-taylor-hebert-kl-122ac.md (Taylor slice)
  - theater/facets/state-updates.md (consolidated; 15 entries)
  - theater/facets/vibes.md (18 entries)
  - theater/proto-lines/b01-c05.md (canonical proto-lines with [<facet>:<id>] citations)
  - theater/proto-lines/_inflight-r2/ (intermediate working dir)
  - staff/auditor/facets-final-audit.md (Phase 5 mechanical audit; cycle 2 CLEAN)
  - staff/auditor/facets-audience-gate-r2.md (Phase 5b audience gate; cycle 2 3-of-3 ACCEPT)
  - staff/auditor/facets-orchestrator-critic-b01-c05.md (Phase 6c critic verdict)

not_archived:
  - theater/facets/scene-map-b01-c05.md (NEW; bones-co-emitted at /and-write Phase 7 revise 2026-05-28; fresh against new 35-bone scaffold)
  - staff/exposition-author/glossed-terms.md (cross-chapter persistent register)
  - cards/ and active-project/warehouse/ persona/location/condition cards
  - theater/bones/b01-c05.md (new 35-bone scaffold; current canonical)
  - active-project/staff/audience/<persona>/stm.md (audience persona STMs preserved; per-character history not archived per chapter)

restore_command: |
  cp -rn theater/_archive/2026-05-28T195041Z-c05-revise-stale-facets/theater/facets/* active-project/theater/facets/
  cp -rn theater/_archive/2026-05-28T195041Z-c05-revise-stale-facets/theater/proto-lines/* active-project/theater/proto-lines/
  cp -rn theater/_archive/2026-05-28T195041Z-c05-revise-stale-facets/staff/auditor/* active-project/staff/auditor/

triggering_event: /and-write b01-c05 revise --from-signals (2026-05-28)
