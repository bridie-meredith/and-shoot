# Improvement-loop / agents ledger

Round-robin log of per-agent tuning passes. Agents are drawn from `.claude/agents/*.md` and `staff/*/card.md`.

**Full rotation list (alphabetical):**
1. `.claude/agents/admin.md`
2. `.claude/agents/audience.md`
3. `.claude/agents/auditor.md`
4. `.claude/agents/coach.md`
5. `.claude/agents/dramatist.md`
6. `.claude/agents/editor.md`
7. `.claude/agents/fixer.md`
8. `.claude/agents/impersonator.md`
9. `.claude/agents/margit.md`
10. `.claude/agents/renderer-minimal.md`
11. `.claude/agents/screen-writer.md`
12. `.claude/agents/showrunner.md`
13. `.claude/agents/studio.md`
14. `staff/admin/card.md`
15. `staff/auditor/card.md`
16. `staff/coach/card.md`
17. `staff/editor/card.md`
18. `staff/exposition-author/card.md`
19. `staff/fixer/card.md`
20. `staff/margit/card.md`
21. `staff/orchestrator-critic/card.md`
22. `staff/screen-writer/card.md`
23. `staff/showrunner/card.md`
24. `staff/stitcher/card.md`
25. `staff/studio/card.md`

---

## Pass log

### Pass 1 — 2026-06-12

**Agent tuned:** `.claude/agents/admin.md`

**Change:** In the process-critic decision procedure §2 ("Check the proposals log"), the bullet for an open proposal match said `Return OK-MERGED-INTO PROP-<NNNN>` — a non-canonical verdict token. The return-format block in the same file, CLAUDE.md Rule 13, and the calling command bodies (`and-write.md` Phase 6.5, `and-facets.md` Phase 4.5) all use the canonical form `OK-MERGED` with the proposal id in the separate `proposal_id:` field. Changed to: `Return OK-MERGED with proposal_id: PROP-<NNNN>`.

**Next agent in rotation:** `.claude/agents/audience.md` (rotation position 2)
