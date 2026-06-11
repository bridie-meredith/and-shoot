# Improvement-Loop / Agents Ledger

Tracks which agent definition was tuned last, what was changed, and who is next in rotation.

**Rotation order (alphabetical within .claude/agents/, then staff/*/card.md):**
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

## Log

### 2026-06-11

**Agent tuned:** `.claude/agents/admin.md`

**Change:** Fixed verdict-string drift in process-critic mode Step 2. Instruction said `Return \`OK-MERGED-INTO PROP-<NNNN>\`` — but the declared return-format schema (admin.md §Return format), CLAUDE.md Rule 13, and every calling command body (and-write Phase 6.5, and-facets Phase 4.5, and-stitch Phase 9.5) all use `OK-MERGED` as the verdict token with `proposal_id` as a separate field. The spurious `INTO` suffix would cause any caller pattern-matching the verdict string to fail. Corrected to `OK-MERGED` (proposal_id: `PROP-<NNNN>`).

**Cross-check basis:** admin.md return-format schema (line 177); CLAUDE.md Rule 13 verdict list; and-write.md line 382; and-facets.md Phase 4.5; and-stitch.md Phase 9.5.

**Next in rotation:** `.claude/agents/audience.md`
