# Improvement-loop / agents ledger

Round-robin tuning log. One entry per pass. Never delete entries.
Rotation order: alphabetical within `.claude/agents/`, then `staff/*/card.md` non-audience entries.

---

## Rotation order

### .claude/agents/
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

### staff/*/card.md (non-audience)
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

### 2026-06-12 — Pass 1

**Agent tuned:** `.claude/agents/admin.md`

**Finding:** Internal inconsistency between the "Check the proposals log" procedure body (step 2, process-critic mode) and both the agent's own return-format table and CLAUDE.md Rule 13. The body text said `Return \`OK-MERGED-INTO PROP-<NNNN>\`` while the return format specifies `OK-MERGED` and CLAUDE.md Rule 13 specifies `OK-MERGED`. A caller pattern-matching the canonical `OK-MERGED` verdict string would not detect the body text's `OK-MERGED-INTO` variant — a real behavior-fork risk.

**Change made:** `.claude/agents/admin.md` body step 2 — changed `OK-MERGED-INTO PROP-<NNNN>` → `OK-MERGED PROP-<NNNN>`.

**Next agent in rotation:** `.claude/agents/audience.md` (pass 2)
