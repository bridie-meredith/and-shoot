# and-shoot RUNBOOK

**For Claude, at session start.** When the user says "write" / "continue" / "what's next" / "next chapter" (or anything implying forward motion through the pipeline), DO NOT ask them what to do. Run this protocol.

---

## 60-second orientation

Read these in order; stop when you have enough state to act:

1. `active-project/staff/showrunner/memory.md` — single source of truth for project state. The `## State` block names the current chapter, the last completed phase, and any blocking conditions.
2. `active-project/staff/showrunner/parking-lot.md` — open HARD items that must resolve at named phases. Surface them; HARD items at the current phase abort.
3. `git log --oneline -10` — what shipped recently. Confirms memory.md isn't stale.
4. `ls active-project/draft/` — what chapters are actually on disk.

If `active-project/` is empty: no project active. Tell the user and ask whether to activate a new one (`/and-project`) or restore a shelved one from `projects/`.

---

## Pipeline state machine

```
/and-project (one-time)
  └─> /and-series
        └─> /and-substance series  →  /and-cast  →  series-audit (HUMAN CHECKPOINT)
                                                          │
                                                          ▼
              /and-substance book b<NN>
                    │
                    ▼
              loop per chapter b<NN>c<MM>:
                /and-substance chapter b<NN>c<MM>
                  └─> /and-write b<NN>c<MM>
                        └─> /and-review bones b<NN>c<MM>     (MANDATORY gate)
                              └─> /and-facets b<NN>c<MM>
                                    └─> /and-stitch b<NN>c<MM>   ← terminal deliverable
                                          └─> [optional] /and-postop b<NN>c<MM>
```

`/and-substance --cascade` chains chapter → write → facets → stitch automatically. Prefer it for routine forward motion; serial commands only when debugging or re-running.

---

## Trigger → action map

| User says | Do this |
|---|---|
| "write" / "continue" / "next" / "go" | Read memory.md, find the current chapter's last completed phase, run the next phase. Don't ask. |
| "write the next chapter" | Run `/and-substance chapter b<NN>c<MM> --cascade` for the next chapter slug. |
| "ship it" / "stitch" | If facets are done: `/and-stitch <slug>`. Else: figure out what's missing and route there. |
| "review the chapter" | `/and-review verdict b<NN>` (book-level) or `/and-postop b<NN>c<MM>` (chapter-level depth-of-quality). |
| "what's next" / "where are we" | Just print the state summary. Don't act. |
| "fix this" / "this is wrong" | Read the user's specific concern. Don't just rerun a phase blindly. |

---

## Common gotchas (check before advancing)

- **`project.series_audit.stale_since` is set** → `/and-substance book` HARD-aborts. Series-level audit needs re-approval at `/and-cast` Phase 5.
- **`active-project/` exists but no `series_audit.approved_at`** → cannot author book content yet. Run `/and-cast` Phase 5.
- **Parking-lot HARD item matching current phase** → must resolve at this run, not later.
- **PROP-0002 (em-dash-fold caps) and PROP-0004 (exposition surface field) are in queue, not implemented.** Don't pretend the gates exist.
- **PROP-0003-A voice exemplar at `active-project/voice-exemplar.md`** is optional but recommended for `/and-stitch`. Absence is fine; just note `voice-exemplar: ABSENT` in pre-flight.
- **PROP-0005 persona-exemplars auto-resolve at agent dispatch.** Tier-1 agents (impersonator, audience) self-load from `cards/persona-exemplars/` or `active-project/persona-exemplars/` — no dispatcher action needed.
- **Polish / `/and-wrap` is deferred.** `draft/<book>-<chapter>.md` is the terminal deliverable. Don't try to author polish.

---

## Hard human checkpoints (never auto-advance past)

- **`/and-cast` Phase 5 — series-level audit.** Only blocking human checkpoint in the chain. If the user hasn't approved at this gate, you cannot proceed to book authoring.

Every other prompt that *looks* like a human checkpoint (accept/redraft, mode picks, branch choices) routes to admin user-proxy per Rule 13. The main session does not call `AskUserQuestion` directly except on admin's explicit ESCALATE.

---

## When you're truly stuck

- Memory.md disagrees with the filesystem → trust the filesystem, propose a memory update, ask admin.
- A command body references a phase that doesn't exist → check `archive/commands/` for migrated names.
- An agent dispatch returns nonsense → check whether the agent's persona-exemplar exists and isn't excluded (PROP-0005).
- User says "no, not that" twice → stop. Ask admin user-proxy what they actually want.

---

## What NOT to do at session start

- Don't ask "what do you want to work on" if memory.md has a clear `current_chapter` + `last_phase`. Just continue.
- Don't re-litigate prior decisions by reading `staff/admin/decisions.md` end-to-end. Trust DEC entries; only read details if relevant to the current action.
- Don't run `/and-postop` reflexively after `/and-stitch`. It's optional; only fire if the user asks or it's a book-mid/close milestone.
- Don't open a new ablation/experiment unless asked. They're on-demand.

---

## Authority

This runbook is operational guidance, not a schema. `CLAUDE.md` and `schemas/` are authoritative on rules and formats. When this runbook disagrees with them, they win — and this file needs updating.
