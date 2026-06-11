# Improvement-loop / agents ledger

Tracks which agent was tuned, what changed, and who is next in the round-robin.

---

## Round 1

### 2026-06-11 — admin.md

**Change:** In Process-critic decision procedure Step 2, corrected the return instruction from `Return \`OK-MERGED-INTO PROP-<NNNN>\`` to `Return \`OK-MERGED\`, \`proposal_id: PROP-<NNNN>\``.

**Why:** The body used "OK-MERGED-INTO" but every other surface — CLAUDE.md Rule 13, the admin.md return-format schema (line 177), the `and-write.md` caller log template, and `cohere-state.schema.md` — uses `OK-MERGED` (no "INTO"). Callers that pattern-match the return value against `OK-MERGED` would never see a match, silently forking logging and downstream routing.

**Next in rotation:** audience.md
