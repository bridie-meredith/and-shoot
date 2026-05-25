# Admin LTM — Long-Term Memory

Append-only record of the principal's standing rulings, recurring preferences, and durable decisions. Read at every session open.

Format per entry:

```
[YYYY-MM-DD] PREFERENCE | <one-line ruling> | <context / why> | <source: human-escalation | user-statement | stm-pattern-promotion>
```

Never rewrite or delete entries. If a preference reverses, append the reversal with reasoning and a `supersedes: <date>` pointer.

---

[2026-05-24] PREFERENCE | Admin handles routine questions; escalates only on irreversible / wide-blast / human-only territory | Foundational ruling — admin agent created with this contract | source: user-statement
[2026-05-24] PREFERENCE | Every dispatch logs a full entry to `staff/admin/decisions.md` with question + context + decision + rationale + basis + trade-off — mandatory, write-before-return | User explicit: "It should log decisions and rationale." | source: user-statement
[2026-05-24] PREFERENCE | All user-facing prompts route through admin by default; main session does not call `AskUserQuestion` directly except as the carrier for admin's escalation back to the human | User explicit: "Modify your scripts and memory so that user prompts go there instead of me." Codified as CLAUDE.md Rules §13. Hard human checkpoints declared in command bodies (e.g. /and-cast Phase 5 series-level audit) remain human-only and bypass admin. | source: user-statement
[2026-05-25] PREFERENCE | Admin has a process-critic mode; auto-fires on non-PASS chain verdicts + every /and-postop convergence; appends process-change proposals to `staff/admin/process-proposals.md` per `schemas/admin-proposal.schema.md` for principal triage; does not implement accepted proposals | User explicit: "go ahead and update admin" → "finish the tail-step hooks as well". Tail-step hooks wired at /and-write Phase 6.5, /and-facets Phase 5c, /and-stitch Phase 9.5, /and-postop Phase 3.5 (always-fires), /and-review Common-Phase 4.5. | source: user-statement
[2026-05-25] PREFERENCE | Parking lot at `active-project/staff/showrunner/parking-lot.md` (schema: `schemas/parking-lot.schema.md`) is under admin's care; admin is responsible for periodic review of its state — stale items (open across multiple eligible runs without resolution), recurring cross-chunk patterns (same finding class filed against multiple chapters → process-critic candidate), and items that should escalate. Admin does NOT resolve parking-lot items directly (resolution is the resolving command's responsibility per CLAUDE.md Rule 14) — admin's job is administration: surfacing staleness, promoting recurring patterns into process-change proposals, and flagging the principal when the lot is filling faster than it's draining. Read the parking lot at every dispatch in process-critic mode; read it on demand or at session-open scans otherwise. Cross-project carry of parking-lot items (when active-project shelves to projects/) is OOS for now — flag if it becomes load-bearing. | User explicit: "have admin remember that there is a parking lot that needs administration" | source: user-statement
