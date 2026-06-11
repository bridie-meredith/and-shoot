# Agents improvement-loop ledger

Round-robin log. One entry per pass. Agents tuned before repeating any.

Agent inventory (`.claude/agents/` + `staff/*/card.md`):
- admin, audience, auditor, coach, dramatist, editor, fixer, impersonator,
  margit, renderer-minimal, screen-writer, showrunner, studio

---

## Pass 1 — 2026-06-11

**Agent tuned:** `admin`
**File:** `.claude/agents/admin.md`

**Change:** Decision Procedure Step 2 used `OK-MERGED-INTO PROP-<NNNN>` as the
return value for the "open proposal — merge" case. The canonical return format
block (same file) and all caller command bodies (`and-write.md` Phase 6.5,
`and-facets.md` Phase 4.5, `and-review.md` Phase 4.5, `and-postop.md`
Phase 3.5) specify `OK-MERGED` as the verdict string, with `proposal_id:
PROP-<NNNN>` as a separate field. The non-canonical `-INTO` suffix is not in
the verdicts enum and would produce a mismatch if any caller pattern-matches on
the verdict string. Fixed to: `Return verdict \`OK-MERGED\` with
\`proposal_id: PROP-<NNNN>\` (per return format block below).`

**Next agent in rotation:** `audience`
