# Archive — b01c01 faceted output

archived: 2026-05-21T222252Z
reason: /and-facets b01c02 Phase 0 — facet pipeline writes to chapter-unnamespaced
  shared paths (theater/facets/<facet>.md, _cite-index.md, theater/dialogue/<char>.md,
  staff/<facet>/r2-decision-shard.md). Running b01c02 in place would overwrite
  b01c01's faceted output. b01c01 is at status `audited-r1-mechanical` (audience-gate
  cap-burned cycle 3; 10/12 facets passed) and its facets are still needed as input
  for /and-stitch b01-c01.

## Contents (paths relative to active-project/, mirrored under this archive root)

- theater/facets/        — all b01c01 facet files, _cite-index.md, .r2-decisions.md,
                           _inflight/, _inflight-r2/  (scene-map-b01-c02.md NOT moved)
- theater/proto-lines/b01-c01.md
- theater/dialogue/      — b01c01 per-character dialogue files
- staff/auditor/facets-*.md            — audit + audience-gate reports
- staff/<facet>/r2-decision-shard*.md  — R2 decision shards
- staff/dialogue-writer/*.drafts.md
- staff/fixer/{and-facets,facets}-*.md
- staff/audience/<persona>/*verdict*.md
- staff/showrunner/and-facets-b01c01-summary.md
- assorted cycle-2/cycle-3 ratification + monument-referral files

NOT archived (cross-chapter persistent): staff/exposition-author/glossed-terms.md,
all persona/agent card.md files, theater/bones/.

## Restore (before /and-stitch b01-c01)

From active-project/:
  cp -rn theater/_archive/20260521T222252Z-b01c01-facets/theater/* theater/
  cp -rn theater/_archive/20260521T222252Z-b01c01-facets/staff/* staff/

Restoring b01c01's facets will collide again with b01c02's. The durable fix is the
systemic change codified in /and-facets Phase 0 (auto-archive of prior-chapter facet
output) — see .claude/commands/and-facets.md Phase 0 step 5.
