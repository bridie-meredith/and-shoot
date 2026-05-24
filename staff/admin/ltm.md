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
