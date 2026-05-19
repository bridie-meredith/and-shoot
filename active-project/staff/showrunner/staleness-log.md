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
