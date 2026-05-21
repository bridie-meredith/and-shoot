# Staleness log — one entry per cascade event
- timestamp: 2026-05-19T000000Z
  command: /and-write b01c01 redo
  invoked_by: user
  marked_stale:
    - block: theater/facets/exposition-b01-c01.md
      reason: parent redo (facets derive from bones; bones file regenerating)
    - block: theater/facets/feeling-b01-c01.md
      reason: parent redo
    - block: theater/facets/feeling-coll-net-mender-flea-bottom.md
      reason: parent redo
    - block: theater/facets/feeling-taylor-hebert-kl-122ac.md
      reason: parent redo
    - block: theater/facets/feeling-wren-stitch-maker-flea-bottom-ward.md
      reason: parent redo
    - block: theater/facets/interest-narrator-b01-c01.md
      reason: parent redo
    - block: theater/facets/location-state-b01-c01.md
      reason: parent redo
    - block: theater/facets/memory-b01-c01.md
      reason: parent redo
    - block: theater/facets/metaphor-b01-c01.md
      reason: parent redo
    - block: theater/facets/scene-map-b01-c01.md
      reason: parent redo (will be re-emitted at Phase 7)
    - block: theater/facets/sensory-b01-c01.md
      reason: parent redo
    - block: theater/facets/state-updates-b01-c01.md
      reason: parent redo
    - block: theater/facets/state-updates-coll-net-mender-flea-bottom.md
      reason: parent redo
    - block: theater/facets/state-updates-env.md
      reason: parent redo
    - block: theater/facets/state-updates-taylor-hebert-kl-122ac.md
      reason: parent redo
    - block: theater/facets/state-updates-wren-stitch-maker-flea-bottom-ward.md
      reason: parent redo
    - block: theater/facets/vibes-b01-c01.md
      reason: parent redo
    - block: theater/bones/b01-c01.md
      reason: regenerating at Phase 7
  user_choice: mark-stale
  notes: |
    Redo full rebuild. Pre-existing PASS bones (24 bones, gate HARD:0/SIGNAL:2)
    and downstream r1-mechanical-audited facets are being invalidated. New bones
    file emitted at Phase 7 may converge to similar shape but is not guaranteed
    identical; facets must be re-derived.

- timestamp: 2026-05-21T000000Z
  command: schema-revision (manual; outside command body)
  invoked_by: user
  scope: axis-bookkeeping split + actor_baselines authoring
  marked_stale:
    - block: .claude/commands/and-substance.md Phase 3 template
      reason: shows pre-split `axes_in_motion: [<axis-slug>, ...]` form; needs update to explicit object shape + axes_held sibling
    - block: .claude/commands/and-write.md Phase 6 bone-gate (FAULT-BONE-DELTA-MALFORMED, AXIS-DELTA-MISMATCH, SUBSTANCE-FLAT, SUBSTANCE-SUSPECT)
      reason: must accept axes_held as satisfying scene_conflict.stakes_axis; must reject direction:null + magnitude:0 entries; must treat chapter_class:frame-coda as exempt
    - block: facet rubrics (sensory + memory)
      reason: A7 + A8 unresolved from 2026-05-20 action plan; cap-burn root causes not yet addressed by harness pass
  user_choice: mark-stale (surfacing-only; does not block)
  notes: |
    See active-project/staff/reviews/run-action-plan-b01c01-2026-05-21-followup.md for the
    full follow-on action plan. Items F1-F3 (command body sync + facet tuning + remaining
    BLOCKING items from 2026-05-20) must land before /and-substance chapter b01c02.

    Schema authority files updated this session:
      - schemas/showrunner-memory.schema.md (axes_in_motion shape, axes_held block, actor_baselines block, direction:up|down)
      - design/substance/delta-targets.md (three-bone-shape table)
      - active-project/staff/showrunner/memory.md (converted all null/zero entries; added actor_baselines[] for 8 cast members)
