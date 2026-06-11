# Improvement-loop / agents — rotation ledger

Tracks which agent was tuned each pass so the round-robin stays fair.
Schema: `agent` | `tuned_at` | `change` | `next_agent`

---

## Rotation pool (alphabetical)

`.claude/agents/` — admin, audience, auditor, coach, dramatist, editor, fixer, impersonator, margit, renderer-minimal, screen-writer, showrunner, studio

`staff/*/card.md` — admin/card.md, auditor/card.md, coach/card.md, editor/card.md, exposition-author/card.md, fixer/card.md, margit/card.md, orchestrator-critic/card.md, screen-writer/card.md, showrunner/card.md, stitcher/card.md, studio/card.md

---

## Log

| # | Agent | Tuned at | Change | Next |
|---|-------|----------|--------|------|
| 1 | `.claude/agents/admin.md` | 2026-06-11 | Fixed non-canonical verdict strings in decision procedure Step 2: `OK-MERGED-INTO PROP-<NNNN>` → `OK-MERGED` (with `proposal_id` in return block); `OK-RE-SURFACED PROP-<NNNN>` → `OK-RE-SURFACED` (with `proposal_id`). Callers (CLAUDE.md §13, `and-write.md` Phase 6.5, return format block) all expect the short forms; the inline-ID variants were unrecognized. | `.claude/agents/audience.md` |
