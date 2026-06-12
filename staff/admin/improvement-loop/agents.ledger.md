# Agents improvement-loop ledger

Round-robin rotation across `.claude/agents/*.md` + `staff/*/card.md`.
Each pass tunes exactly one agent; agents cycle before any repeats.

---

## Rotation order (alphabetical, first pass)

`.claude/agents/`: admin, audience, auditor, coach, dramatist, editor, fixer, impersonator, margit, renderer-minimal, screen-writer, showrunner, studio

`staff/*/card.md`: admin/card, auditor/card, coach/card, editor/card, exposition-author/card, fixer/card, margit/card, orchestrator-critic/card, screen-writer/card, showrunner/card, stitcher/card, studio/card

---

## Log

### 2026-06-12 — `.claude/agents/admin.md`

**Change:** Fixed `OK-MERGED-INTO PROP-<NNNN>` → `OK-MERGED` (with `proposal_id:` field) in process-critic Step 2 procedure text. The procedure text used a non-existent verdict string that no caller checks for; the return-format enum and all dispatching command bodies (`and-write.md` Phase 6.5, `and-stitch.md` Phase 9.5, etc.) expect `OK-MERGED`. The inconsistency would cause the main session to receive an unrecognized verdict string when admin merges into an existing proposal.

**Next agent:** `.claude/agents/audience.md`
