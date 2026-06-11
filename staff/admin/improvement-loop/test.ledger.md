# improvement-loop/test — ledger

Tracks which structural test lens was run each pass, so each lens gets a turn.

**Lens rotation order:** a → b → c → d → a → ...

| Lens | Description |
|------|-------------|
| a | `/and-review pipeline` — schema vs command-body vs rubric tri-walk |
| b | `/and-review consistency` or `/and-review tree` on a recent chapter or the and-experiment spine |
| c | `/and-ablate` on a shipped chapter (facet-value evidence) |
| d | Targeted auditor fork on the most-recently-changed artifact |

---

## Pass log

### Pass 1 — 2026-06-11

**Lens run:** a — `/and-review pipeline` (schema ↔ command-body ↔ rubric tri-walk)

**Verdict:** HARD-FINDINGS — 3 HARD, 1 SIGNAL, 4 TASTE-FLAGs

**Findings filed:**

| ID | Class | File | Description |
|----|-------|------|-------------|
| STRUCT-001 | HARD | `schemas/audit-report.schema.md` | §R2 decision-shard documents retired R2 machinery (DEC-0116). Phase 6 of /and-facets, .r2-decisions.md, f-r2-counts thresholds — none exist under current command body. |
| STRUCT-002 | HARD | `.claude/commands/and-stitch.md` | 9 occurrences of `proto-lines/<slug>.md` as the active bones input in body text; Phase 0 explicitly states bones path is `theater/bones/<book>-<chapter>.md`. Lines 419/427 are functional errors in scene-map validation. |
| STRUCT-003 | HARD | `schemas/bones.schema.md`, `and-facets.md`, `CLAUDE.md` | `theater/proto-lines/` path status three-way inconsistency: schema=legacy/dead, and-facets=live in clearance, CLAUDE.md=live with present-tense description. Requires principal determination. |
| STRUCT-004 | SIGNAL | `.claude/commands/and-facets.md` | "base proto-lines file" referenced in Phase 1 without path; blocked on STRUCT-003 resolution. |

**Parking-lot items opened:** `pl-2026-06-11-pipeline-001`, `pl-2026-06-11-pipeline-002`, `pl-2026-06-11-pipeline-003`

**Report path:** `active-project/staff/reviews/pipeline-2026-06-11T2310Z.md`

**Next lens:** b — `/and-review consistency` or `/and-review tree` on a recent chapter or the and-experiment spine
