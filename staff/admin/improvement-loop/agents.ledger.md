# Agents improvement-loop ledger

Round-robin tuning log. One entry per pass. Agents rotate in alphabetical order across
`.claude/agents/` and `staff/*/card.md`; each gets a turn before any repeats.

---

## Pass 001 — 2026-06-12

**Survey order:** .claude/agents/admin.md surveyed first (alphabetically first); no critical drift found.

**Agent tuned:** `.claude/agents/auditor.md`

**Change:** Dispatch Pattern section — "At dispatch time, showrunner provides" → "At dispatch time, the dispatching command body provides". Updated stale Task example ("episode wrap audit for s01e02" → "facets mechanical audit for b01c01") and stale Target description ("show file path, episode plan path, or specific line/bullet" → "bones file path, facet graph path, or specific element") and Report path example to match current pipeline conventions.

**Rationale:** Direct Rule 2 violation. CLAUDE.md §2: "Showrunner does NOT orchestrate and does NOT have the Agent tool — command bodies do." Auditor is dispatched by command bodies (/and-facets Phase 4, /and-write Phase 6, /and-review bones, /and-review pipeline), not by showrunner. Stale examples reinforced the wrong mental model.

**Next in rotation:** `.claude/agents/audience.md`

---
