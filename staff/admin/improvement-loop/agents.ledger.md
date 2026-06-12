# Agents Improvement-Loop Ledger

Round-robin tuning log. One entry per pass. Every agent in `.claude/agents/` and `staff/*/card.md` gets a turn before any repeats.

---

## Rotation order (established 2026-06-12)

### .claude/agents/ (13 agents)
1. admin.md
2. audience.md
3. auditor.md
4. coach.md
5. dramatist.md
6. editor.md
7. fixer.md
8. impersonator.md
9. margit.md
10. renderer-minimal.md
11. screen-writer.md
12. showrunner.md
13. studio.md

### staff/*/card.md (select staff cards, non-audience)
14. staff/admin/card.md
15. staff/auditor/card.md
16. staff/coach/card.md
17. staff/editor/card.md
18. staff/exposition-author/card.md
19. staff/fixer/card.md
20. staff/margit/card.md
21. staff/orchestrator-critic/card.md
22. staff/screen-writer/card.md
23. staff/showrunner/card.md
24. staff/stitcher/card.md
25. staff/studio/card.md

---

## Log

### Pass 1 — 2026-06-12

| Field | Value |
|-------|-------|
| Agent tuned | `.claude/agents/admin.md` |
| Change | In process-critic decision procedure step 2, corrected verdict token from non-canonical `OK-MERGED-INTO PROP-<NNNN>` to `OK-MERGED` with `proposal_id: PROP-<NNNN>`. The old string was not in admin.md's own return-format enum nor in the caller expectation lists (CLAUDE.md Rule 13, `and-write.md` Phase 6.5). A caller logging the verdict against the expected `OK-MERGED` token would never match `OK-MERGED-INTO PROP-0001`. |
| Finding class | Return-format inconsistency — decision-procedure prose diverged from the agent's own return-format schema |
| Next agent | `.claude/agents/audience.md` |
