# Agent Improvement-Loop Ledger

Round-robin rotation. Every agent gets a pass before any repeats.
Agents in rotation (alphabetical by filename):
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

---

## Pass log

### 2026-06-12 — auditor.md
**Change:** Dispatch pattern section, line "At dispatch time, showrunner provides:" → "At dispatch time, the dispatching command body provides:" — direct Rule 2 alignment (command bodies are the orchestrators; showrunner does NOT orchestrate and does NOT have the Agent tool).
**Rationale:** auditor is actively dispatched by `/and-facets` Phase 4, `/and-review` subcommands, and `/and-cast` Phase 5 — never by showrunner. The legacy text contradicted Rule 2 and could fork behavior for any session reasoning about dispatch authority from the agent definition.
**Next agent:** coach.md
