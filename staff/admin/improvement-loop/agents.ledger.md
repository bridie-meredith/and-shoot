# Improvement-loop / agents ledger

Round-robin log of agent tuning passes. Every entry records which agent was tuned, the single change made, and who's next.

---

## Rotation order (alphabetical, .claude/agents/ first, then staff/*/card.md)

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
14. staff/auditor/card.md
15. staff/editor/card.md
16. staff/fixer/card.md
17. staff/margit/card.md
18. staff/orchestrator-critic/card.md
19. staff/screen-writer/card.md
20. staff/showrunner/card.md
21. staff/studio/card.md

---

## Pass log

### 2026-06-12 — admin.md

**Agent:** `.claude/agents/admin.md`
**Change:** Corrected broken verdict string in process-critic mode Step 2 (Open-proposal branch). Was `OK-MERGED-INTO PROP-<NNNN>` — a verb not listed in the return format block or CLAUDE.md §13. Fixed to `OK-MERGED` with `proposal_id: PROP-<NNNN>` carried in the return block, matching the canonical verdict enum in both the agent's own return-format spec and CLAUDE.md Rule 13.
**Why it matters:** Any caller parsing for `OK-MERGED` would silently miss the `OK-MERGED-INTO` string, treating a successful merge as an unrecognised verdict.

**Next in rotation:** `audience.md`
