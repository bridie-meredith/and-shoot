# Improvement-loop: AGENTS ledger

Tracks which agent definition was tuned each pass and what changed.
Round-robin — every agent gets a turn before any repeats.

## Rotation order (alphabetical, .claude/agents/ first, then staff/*/card.md)

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
15. `staff/margit/card.md`

---

## Pass log

### Pass 1 — 2026-06-12

**Agent tuned:** `.claude/agents/admin.md`

**Change:** Decision procedure step 2 (Check proposals log) said `Return \`OK-MERGED-INTO PROP-<NNNN>\`` — a verdict token not in the formal return-format vocabulary. The return format block (line 177), CLAUDE.md Rule 13, and all dispatching command bodies (`and-write.md`, `and-stitch.md`, `and-facets.md`, `and-postop.md`) agree the verdict is `OK-MERGED` with the proposal ID in the separate `proposal_id` field. Changed to: `Return \`OK-MERGED\`; set \`proposal_id: PROP-<NNNN>\` in the structured return block.`

**Why this matters:** The agent was producing `OK-MERGED-INTO PROP-<NNNN>` in its own decisions.md audit trail (following the decision procedure instruction) while callers parsing a formal return block expected `verdict: OK-MERGED`. Verified in historical render-logs and cohere-state files: some calls returned the long form, some the short form — inconsistent behaviour driven by the ambiguous instruction. The fix canonicalises the return token to match the formal vocabulary everywhere.

**Next agent in rotation:** `.claude/agents/audience.md`
