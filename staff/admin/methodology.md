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

---

## Process-critic mode (added 2026-05-25)

Process-critic mode reuses the same decision order with one substitution at step 1–2 and an added discrimination step.

**Step 1 substitute — Proposals-log precedent.** Has admin already authored a proposal for this target + change_type? If yes and status is `open`, merge new evidence into the existing proposal (do not duplicate). If `rejected` and materially-same rationale, return `OK-PRIOR-REJECTION`. If `deferred` and `defer_until` has passed, re-surface.

**Step 2 substitute — Content vs. process discrimination.** Before invoking goals/methodology to weigh a proposal, ask: *is this a process failure or a content failure?*

- **Content failure** — the chain did its job; this specific chapter/scene/bone under-delivered. The gate would not have caught it without becoming a different gate. Return `OK`. Do not author a proposal.
- **Process failure** — the chain shipped a result it should not have shipped. One of:
  - No gate exists for this class → `add`
  - Gate exists but criteria/threshold missed → `modify` (detection)
  - Gate caught it but disposition let it ship → `modify` (disposition)
  - Gate fires too often without catching anything → `delete`
  - Taste flag has recurred ≥3 times → `promote` (Rule 11 path)

The discriminator question is: *could a stricter version of the existing gate have caught this without becoming a different kind of gate?* If yes — modify. If no and no gate exists for the class — add. If the gate did catch it but admin lets ship anyway — modify disposition, not detection.

**Step 3 (methodology tiebreakers) applies as written**, with one note: process changes have wide blast radius (affect every future invocation of the gate), so weight `3c. Blast radius` and `3a. Reversibility` more heavily than usual. Prefer rubric edits to command-body edits. Prefer command-body phase notes to schema changes.

**Recurrence discipline.** First occurrence of a non-catastrophic SIGNAL → return `OK` and wait. Premature promotion is the anti-pattern. Override only when the failure was catastrophic (irreversible, multi-chapter blast radius, or a known leakage class the chain was explicitly designed to prevent).

**Cost-estimate calibration for proposals:**
- `S` — single file edit, one rubric line or one phase note
- `M` — command + schema, or rubric + multiple command bodies
- `L` — schema rewrite, multi-file cascade, new command, new gate phase

`L` proposals from admin should be rare. If admin finds itself drafting an `L` proposal, prefer to escalate instead — the principal should size large architectural changes, not admin.

---

*Last updated: 2026-05-25 (process-critic mode added)*
