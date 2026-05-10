# Audit Report Schema

Audit reports are returned by auditor to showrunner. They are never stored in the show file. The format is a classified list of findings, each with enough information for fixer to act on.

---

## Format

```yaml
audit:
  scope: episode | season | series
  target: <episode slug, season slug, or series>
  timestamp: <ISO date>
  findings:
    - id: <fault-NNN>
      type: pass | flag | fault | escalate
      what: <what showed the problem — specific line number, bullet number, card slug, or plan section>
      why: <why it matters — what downstream consequence this creates>
      criteria: <what fixer must achieve to resolve — only required for fault and escalate>
```

---

## Finding types

**pass** — no problem found. No action. May be omitted from the report entirely if there are no annotations needed.

**flag** — noted for editor or future reference. Does not block. Editor receives flags as advisory notes. No fixer dispatch.

**fault** — problem found that can be fixed at the current scope (episode or below). Routed to fixer with the criteria field. Showrunner does not resolve faults directly.

**escalate** — problem scope exceeds the current level. An episode-scope audit that finds a season-level planning failure returns an escalation. Routed to showrunner for human decision.

---

## What auditor checks

Auditor receives a task (what to check), context (relevant constraints, plan, memory), and a thing to review. It checks the following axes:

**Constraints** — are laws, lore, and behavior constraints obeyed? Each fault names the specific constraint violated and the specific line or bullet where the violation occurred.

**State** — does the show file reflect what state and memory records say is true? If a character moves without their state file recording the move, that is a state fault. If an object is used that the inventory says they don't have, that is a state fault.

**Drift** — does a delivered line match the bullet it was supposed to execute? If a bullet says "X confronts Y" and the delivered line is X and Y having a pleasant exchange, that is drift. Auditor names the bullet and the line.

**Plan quality** — if audience and dramatist both returned `revise` on a plan but screen-writer proceeded (three-attempt exhaustion), the audit notes this as a flag. If the resulting episode shows structural problems traceable to the rejected plan, this escalates to a fault.

**Audience protocol** — were audience rejections properly handled? If a rejected line was not deleted before the retry, auditor flags the show file inconsistency.

---

## Criteria field

The criteria field is what fixer must achieve, not how to achieve it. Write it as an outcome, not a prescription.

Good:
```
criteria: the delivered line must reflect the constraint that X cannot enter government buildings without authorization
```

Not:
```
criteria: rewrite line 47 to say X waits outside
```

Fixer determines the minimum change to meet the criteria. Auditor does not prescribe the fix.

---

## Example

```yaml
audit:
  scope: episode
  target: s01e02
  timestamp: 2026-05-04
  findings:
    - id: fault-001
      type: fault
      what: show file line 23
      why: Mira uses a keycard she lost in episode 1 (state file shows inventory: empty since s01e01 close)
      criteria: line must not require Mira to possess or use the keycard
    - id: fault-002
      type: flag
      what: episode script bullet 14
      why: bullet calls for interior monologue but actor has no established interiority in this scene — editor may want to address tone
    - id: fault-003
      type: escalate
      what: season plan chunk for s01e02
      why: episode chunk requires resolving the Mira trust arc but season plan placed that resolution in s01e04; the episode cannot deliver its chunk without contradicting the season plan
      criteria: showrunner must decide whether to advance the season resolution or revise the episode chunk
```

---

## R2 decision-shard frontmatter (URI-026 follow-on, 2026-05-10)

`/and-facets-r2` emits per-layer decision shards at `active-project/staff/<facet>/r2-decision-shard.md` (per-character for the feeling layer). These shards are consolidated at Phase 6 of `/and-facets` into `active-project/theater/facets/.r2-decisions.md`. The consolidated file is the cross-pipeline contract that `/and-season`'s orchestrator-critic Phase 6 verdict reads to surface F-R2-* counts in F7.

### Shard format

```
---
report: r2-decision-shard
facet: <facet slug>             # e.g. memory | feeling-taylor | sensory | vibes | ...
episode: <episode slug>          # e.g. s01e01
date: <ISO date>
f-r2-counts: {f-r2-1: N, f-r2-2: N, f-r2-3: N, f-r2-4: N}
---

# R2 decision shard — <facet> — <episode>

<one free-prose entry per R2 decision/add. Each entry ends with a verdict line:
VERDICT: KEEP | DELETE | ADD — F-R2-<n>:<class> if classified, else clean.>
```

### Consolidated file

`active-project/theater/facets/.r2-decisions.md` is built by summing every per-shard `f-r2-counts` mapping into a single top-of-file frontmatter block:

```
---
report: r2-decisions-consolidated
episode: <episode slug>
date: <ISO date>
shards: <list of source shard paths>
f-r2-counts: {f-r2-1: N, f-r2-2: N, f-r2-3: N, f-r2-4: N}
---

# R2 decisions — <episode>

<concatenation of shard bodies, headed by their facet slug>
```

### F-R2-* class definitions

The four failure classes are defined in `design/shoot-v2/r2-judge-tuning/A-corpus.md`. Summary for the reader of this schema:

- **F-R2-1** — rubric-form discipline failure: R2 revision/add violates the locked R1 form for the layer.
- **F-R2-2** — motive-honesty failure: stated decision motive doesn't match what the diff actually changed.
- **F-R2-3** — niche-driven add: R2 added an entry that the layer's rubric does not warrant.
- **F-R2-4** — graph-incoherence: R2 mutation breaks the cite-index DAG or contradicts a sibling layer.

### Consumer contract

`staff/orchestrator-critic/card.md` Phase 6 verdict reads `f-r2-counts` from the consolidated file when present. Threshold: `f-r2-1 > 0` is HARD; `f-r2-2 + f-r2-3 + f-r2-4 > 2` is SIGNAL. HARD trips F7 with `/and-facets` attribution.
