# Admin LTM — Long-Term Memory

Append-only record of the principal's standing rulings, recurring preferences, and durable decisions. Read at every session open.

Format per entry:

```
[YYYY-MM-DD] PREFERENCE | <one-line ruling> | <context / why> | <source: human-escalation | user-statement | stm-pattern-promotion>
```

Never rewrite or delete entries. If a preference reverses, append the reversal with reasoning and a `supersedes: <date>` pointer.

---

[2026-05-24] PREFERENCE | Admin handles routine questions; escalates only on irreversible / wide-blast / human-only territory | Foundational ruling — admin agent created with this contract | source: user-statement
