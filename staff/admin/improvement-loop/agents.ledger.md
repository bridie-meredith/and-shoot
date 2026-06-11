# Agents improvement-loop ledger

Round-robin tuning log. One pass per agent before any repeats.

## Agent roster (alphabetical rotation)

1. `.claude/agents/admin.md` + `staff/admin/card.md`
2. `.claude/agents/audience.md`
3. `.claude/agents/auditor.md` + `staff/auditor/card.md`
4. `.claude/agents/coach.md` + `staff/coach/card.md`
5. `.claude/agents/dramatist.md`
6. `.claude/agents/editor.md` + `staff/editor/card.md`
7. `.claude/agents/fixer.md` + `staff/fixer/card.md`
8. `.claude/agents/impersonator.md`
9. `.claude/agents/margit.md` + `staff/margit/card.md`
10. `.claude/agents/renderer-minimal.md`
11. `.claude/agents/screen-writer.md` + `staff/screen-writer/card.md`
12. `.claude/agents/showrunner.md` + `staff/showrunner/card.md`
13. `.claude/agents/studio.md` + `staff/studio/card.md`
14. `staff/exposition-author/card.md`
15. `staff/orchestrator-critic/card.md`
16. `staff/stitcher/card.md`

---

## Log

### 2026-06-11 — `.claude/agents/admin.md`

**File tuned:** `.claude/agents/admin.md`

**Change:** In "Decision procedure — process-critic mode" Step 2, the "open proposal" bullet said "Return `OK-MERGED-INTO PROP-<NNNN>`" — a verdict form not recognized by any caller. CLAUDE.md Rule 13, all command-body dispatch wiring (and-write Phase 6.5, and-facets Phase 4.5, and-stitch Phase 9.5, and-review Phase 4.5), and the agent's own return-format section all use `OK-MERGED`. The `-INTO` suffix created a fork where a literal reading of step 2 would output an unrecognized string. Fixed to `OK-MERGED PROP-<NNNN>` — matching the `OK-RE-SURFACED PROP-<NNNN>` pattern in step 2c, keeping the proposal id for caller traceability, and aligning with the established verdict enum.

**Next in rotation:** #2 — `.claude/agents/audience.md`

---

### 2026-06-11 (pass 2) — `.claude/agents/audience.md`

**File tuned:** `.claude/agents/audience.md`

**Change:** YAML `description` field listed two stale capability claims visible to every caller at
dispatch time: (1) "and line review" — line review is part of the archived per-line shoot
(coach is legacy-only); (2) "facet-adversarial review (per-reviewer verdicts, 3-of-3 accept
required)" listed as an active override mode — it is retired under DEC-0116 (the agent body already
has a RETIRED section, but the description contradicted it). Corrected to: plan review only in
default config; one active override mode (taste-judge); retired status of facet-adversarial noted
inline.

**Next in rotation:** #3 — `.claude/agents/auditor.md` + `staff/auditor/card.md`
