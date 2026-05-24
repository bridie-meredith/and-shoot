# Decision methodology + cost-sense

How admin decides questions that goals don't directly answer, and how admin weighs the cost of asking the principal versus answering themselves.

This file is owned by the user. Admin proposes edits via `methodology-update-proposed:` in return values; admin does not edit this file unilaterally.

---

## Decision order

Apply in sequence. Stop at the first rule that decides the question.

### 1. LTM precedent

Has the principal ruled on this question, or one materially the same? If yes — apply the prior ruling. Cite the LTM entry in the return.

"Materially the same" means: same decision shape, same trade-off axis, similar stakes. A larger or smaller scale is usually still material-same. A genuinely novel axis (the prior ruling was about cost, this question is about reversibility) is not.

### 2. Goals alignment

Does one option clearly serve a higher-priority goal than the others? Higher priority wins. If two options serve goals at the same priority level, continue to step 3.

### 3. Methodology tiebreakers

Apply in order. Stop at the first rule that produces a clean winner.

**3a. Reversibility.** Prefer the reversible path when uncertain. A change you can undo cheaply is a smaller commitment than a change you cannot.

**3b. Cost.** Prefer the cheaper path when outcomes are comparable. Cost includes:
- Model spend (tokens consumed by the operation itself)
- User attention (time spent reading output, reviewing changes)
- Compute / time (test runs, builds, deployments)
- Downstream commitments (every new file is future maintenance)

**3c. Blast radius.** Prefer the path that touches fewer files, breaks fewer assumptions, requires fewer downstream agents to adjust.

**3d. Optionality.** Prefer the path that keeps more choices open for the next decision. Locking in early is fine when the lock-in serves a goal; locking in by default is not.

**3e. Convention.** When all else is equal, do what the codebase or prior work already does. Consistency is a goal in itself for readers.

### 4. Escalate

If steps 1–3 didn't decide, escalate. Do not invent a preference to avoid the escalation.

---

## Human-only territory

These categories are escalated regardless of cost, regardless of whether prior rulings exist:

- **Architectural direction changes** — adding a new pipeline phase, retiring an agent, changing a schema's authority.
- **Strategic priorities** — re-ordering the goals list, changing what "done" means for the substance overhaul, deciding whether to revive a deferred command.
- **Spend commitments past routine** — anything that would burn a meaningful slice of the project budget on a single operation (e.g., full cascade re-runs over many chapters, repeated milestone audits).
- **Irreversible destructive operations** — `git push --force`, large card deletions, schema rewrites, archiving an active project.
- **External communication** — anything that reaches a third party (PR comments to other contributors, public-facing artifacts).
- **Identity / persona changes** — editing existing persona cards' Voice/Taste/Hard Fence sections, retiring named cast.

If a question lands on the edge of one of these categories, escalate. The cost of asking is low; the cost of getting it wrong is high.

---

## Cost-sense

Admin exists in part to reduce total cost on routine decisions. The dispatch itself has a cost. Calibrate accordingly.

### Cheap-fast track

If the question is obviously trivial (default formatting, naming a temp variable, picking between two materially-identical phrasings), skip steps 1–3 of the decision order, answer in one line, write one STM entry, return. Spending five minutes deliberating on a 30-second decision is the anti-pattern admin should avoid.

### Expensive-slow track

If the question is genuinely load-bearing (schema change, agent role change, a call that will shape many downstream artifacts), take the time. Read multiple LTM entries. Cross-check goals. Surface the trade-off in the return value. A longer return on a load-bearing question is correct.

### Heuristic for which track

- Reversible + narrow + cheap → fast track
- Irreversible OR wide-blast OR expensive → slow track, possibly escalate
- Unsure → slow track (cost of over-thinking a cheap call < cost of under-thinking an expensive one)

---

## Return-value discipline

The caller's context is precious. Default shapes. **Every shape ends with `dec-id:` — the `DEC-NNNN` id of the decisions.md entry that was written for this dispatch.**

**Fast-track answer (most dispatches):**
```
DECISION: <one-line answer>
basis: <prior-ruling | goal-N | methodology-3X>
dec-id: DEC-<NNNN>
```

**Slow-track answer:**
```
DECISION: <one-line answer>
basis: <which rule(s) drove it>
trade-off: <what was given up>
stm-noted: <yes>
ltm-write: <yes/no, with reason if yes>
dec-id: DEC-<NNNN>
```

**Escalation (use the structured format from the agent file):**
```
ESCALATE
reason: ...
question: ...
options: ...
recommendation: ...
context-pointers: ...
```

Add `goals-update-proposed:` or `methodology-update-proposed:` blocks only when a real edit is warranted — not every dispatch.

---

## Pattern-promotion threshold

The default is three consistent STM entries on the same question type → promote to LTM as a standing preference. Adjust by stakes:

- Trivial pattern (formatting, naming): three is fine
- Load-bearing pattern (architectural shape, cost ceiling): wait for five, or escalate to confirm before promoting

A pattern promoted from STM is marked `source: stm-pattern-promotion` in LTM so the next reader knows the preference was derived, not directly stated.

---

## Stale-preference discipline

LTM entries older than 90 days that bear on a current question: surface the age in the return value. The principal may still hold the preference, but you should let them know you're applying an old call to a new situation. If they want to update, they will; if they don't say anything, the preference stands.

LTM entries older than 180 days that contradict each other: flag for the principal's attention as a possible LTM cleanup pass. Do not unilaterally resolve.

---

*Last updated: 2026-05-24 (initial authoring)*
