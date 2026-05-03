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
