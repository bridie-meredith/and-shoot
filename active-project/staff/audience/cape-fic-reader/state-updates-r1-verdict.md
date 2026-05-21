---
reviewer: cape-fic-reader
facet: state-updates
cycle: 1
episode: b01c02
date: 2026-05-21
verdict: revise
---

# Verdict reasoning

The state-updates graph reads mostly clean from a rules-and-asymmetry angle. The env entries (state:1-9) are physical-state bookkeeping that don't affect the tactical picture; I don't care about a lamp going lit or a ledger opening and closing. The deployment entries (state:2, state:11) are the ones I'm actually watching, and state:11 mostly holds — the first capability deployment is tagged correctly as defensive-flea-bottom with the dormant prior baseline. The power was used within apparent constraints.

Two things stop me.

First: state:10 at @12. The comment says "hard fence 1/2 honored." I'm reading this as: there are two hard fences on Coll's registration behavior, and one of them is satisfied. That means one is not satisfied. If a constraint fence is only half-honored, that's a rule bending without acknowledgment, and that is my walkout trigger. The comment doesn't clarify which fence is broken or why — it just asserts 1/2 and moves on. I need to know whether the "not yet honored" fence is a future-beat issue, a deferred resolution, or an actual violation sitting in the graph right now. As written, the notation is ambiguous in exactly the way that makes me stop reading and ask "wait, when did she know that" — except it's "wait, which rule did that break?"

Second: state:13 at @25. `knowledge.flea-bottom-social-physics: observational-sweep-pattern -> categorical-structural`. The bones show Taylor watching one watch-sweep, routing bugs around it, and then doing a ledger accounting. The reclassification to categorical-structural is a significant knowledge upgrade. I can accept fast synthesis when the setup earns it — if this chapter has been building toward a comprehension event, fine. But the field label "categorical-structural" is doing a lot of work: it implies Taylor has moved from "I've seen the pattern" to "I understand the governing structure." One sweep accounting is a single data point. The bones don't show her drawing on prior observations from other chapters or cross-referencing broader data. I accept this only if the proto-lines or bones elsewhere in the chapter establish that this isn't her first encounter with sweep-physics — but from the bone list, I count @22-@29 as the accounting sequence following a single deployment event. If this is the first sweep she's directly observed, the jump is too fast and the knowledge entry is overclaiming.

The lamp-ledger-pen prop state chain (state:4-9) is fine mechanically but read as administrative overhead. Six entries to track Taylor writing and closing a personal ledger is state-tracking for the author's benefit, not mine.

# Entry-level callouts

[state-updates:10] @12 — "hard fence 1/2 honored" in the trailing comment is unresolved ambiguity on a rule-compliance claim. Which fence is the un-honored one? Is it a carry-forward to a later beat, a known gap, or a violation? The notation reads like one constraint isn't satisfied and the author decided to note it and move on. That's the kind of thing that makes me stop the read and check the rulebook.

[state-updates:13] @25 — `observational-sweep-pattern -> categorical-structural` is a significant knowledge upgrade anchored to a single sweep-and-accounting event. The chapter bones don't establish prior sweep observations that would warrant "categorical." If this is Taylor's first direct observation of sweep mechanics, the jump overclaims what one event yields. Needs either a qualifying note that prior exposure exists, or a more conservative target value that doesn't claim structural understanding yet.

# Convergence trace

- [state-updates:10] overlaps with auditor finding flag-003 (class CONTRADICTION) where the auditor examined the @5 deployment entries but did not separately examine the state:10 hard-fence notation. The auditor's constraint class (CN-001, CN-002) addresses Earth-Bet proper noun fences but not power-mechanics fences. This callout is in the seam the auditor's mechanical scan does not cover.

- [state-updates:13] overlaps with auditor finding fault-002 / RF-001 (now resolved — state:13 was re-anchored from @26 to @25 in cycle-2). The re-anchor resolved the NI co-citation gap but did not revisit whether the knowledge value itself is earned by the chapter's action. The auditor's rubric-fidelity pass checked form (co-citation present); I'm attacking substance (knowledge claim vs. chapter evidence).
