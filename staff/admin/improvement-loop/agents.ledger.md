# agents improvement-loop ledger

Tracks the round-robin tuning rotation for agent definitions in `.claude/agents/` and `staff/*/card.md`.
One agent per pass; every agent gets a turn before any repeats.

## Rotation order (alphabetical within tier)

### Tier A — `.claude/agents/`
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

### Tier B — `staff/*/card.md` (non-audience)
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

## History

### 2026-06-11 — pass 1

**Agent:** `.claude/agents/admin.md`

**Finding:** Verdict-string mismatch in Step 2 (§ Decision procedure — process-critic mode). The procedure
text said `Return OK-MERGED-INTO PROP-<NNNN>` but the return format box (line 177), Step 7's decisions-log
reference (line 172), and the caller in `and-write.md` Phase 6.5 all parse for `OK-MERGED`. An admin
following Step 2 verbatim would emit an unparseable verdict string; the `proposal_id` field already
carries the PROP number, making the inline `PROP-<NNNN>` in the verdict string both redundant and
destructive.

**Change:** Normalized Step 2 verdict to `OK-MERGED`; added explicit note that `proposal_id` carries
the existing proposal's id. No persona/voice content touched.

**Next:** `.claude/agents/audience.md`
