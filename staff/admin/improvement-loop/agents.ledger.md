# Improvement-loop / agents ledger

Round-robin log of per-agent tuning passes. One entry per pass; never delete entries.

---

## Pass 001 — 2026-06-12

**agent tuned:** `admin` (`.claude/agents/admin.md`)
**surveyed:** all agents in `.claude/agents/` + `staff/*/card.md` (first pass; ledger created this run)
**agent pool (round-robin order):**
1. admin
2. audience
3. auditor
4. coach
5. dramatist
6. editor
7. fixer
8. impersonator
9. margit
10. renderer-minimal
11. screen-writer
12. showrunner
13. studio
14. staff/exposition-author (card only)
15. staff/orchestrator-critic (card only)
16. staff/stitcher (card only)

**change made:**
Step 2 of the process-critic decision procedure used non-schema verdict strings in its return instructions:
- `OK-MERGED-INTO PROP-<NNNN>` (verdict name differs from schema enum value `OK-MERGED`; would fail caller string-match)
- `OK-RE-SURFACED PROP-<NNNN>` (ID embedded inline rather than in separate `proposal_id` field)

Both step 2 bullet returns now match the return-format schema (lines 177–181): verdict is `OK-MERGED` / `OK-RE-SURFACED` from the enum; `proposal_id: PROP-<NNNN>` is the separate field. CLAUDE.md Rule 13 and both command-body dispatch sites (`and-write.md` Phase 6.5, `and-facets.md` Phase 4.5) already expected the schema-canonical `OK-MERGED` form.

**next agent in rotation:** `audience` (`.claude/agents/audience.md`)
