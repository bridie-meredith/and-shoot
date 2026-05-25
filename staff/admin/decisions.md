# Admin Decisions Log

Append-only audit trail. Every dispatch writes one entry with full rationale, regardless of how it was decided (fast-track, slow-track, or escalation).

This is the full record. STM is the running "what's on top of mind"; LTM is the compact "standing preferences"; this file is the complete history with reasoning.

Never rewrite or delete entries. If a prior decision is reversed, append a new entry with `reverses: <id>` and the reasoning for the reversal.

---

## Entry format

```
## DEC-<NNNN> | <YYYY-MM-DD HH:MM> | <FAST | SLOW | ESCALATED>

question: <as received from caller, verbatim if short>
context: <what the caller provided — what's been tried, stakes, reversibility>
options: <if the caller gave candidates, list them; otherwise "n/a">

decision: <one-line answer, or ESCALATED-TO-HUMAN>
basis: <which rule fired — ltm:DEC-NNNN | goal:N | methodology:3X | human-only:<category>>
rationale: <why this rule produced this answer; what specifically about the
question matched the rule. Two or three sentences for slow-track and
escalations; one sentence for fast-track is fine.>
trade-off: <what was given up by this choice — what the rejected options would
have offered. "n/a" if there was no real alternative.>

stm-written: <yes>
ltm-written: <yes | no — if yes, cite the LTM entry created>
goals-update-proposed: <yes | no — if yes, include the diff>
methodology-update-proposed: <yes | no — if yes, include the diff>
```

---

## Numbering

`DEC-<NNNN>` is monotonic across the project lifetime. Read the bottom of this file at session-open to find the highest existing number; the next dispatch is that + 1.

---

## DEC-0001 | 2026-05-24 18:47 | FAST

question: Initial admin agent setup — establish decisions log file
context: User requested decisions + rationale be logged; admin files had STM/LTM but no dedicated audit-trail log
options: (a) extend STM format, (b) extend LTM format, (c) add separate decisions.md file
decision: Add separate `staff/admin/decisions.md` as append-only full audit trail; keep STM/LTM as working memory.
basis: methodology:3c (blast radius — separating concerns keeps STM short for prune cycles and LTM compact for read-at-open, while letting decisions.md grow indefinitely without affecting either)
rationale: STM is pruned to ~20 entries; piling rationale into STM defeats the prune. LTM is meant to be a compact rule-set; piling rationale there defeats the read-at-open cost target. A separate append-only log keeps each file fit for its purpose.
trade-off: Three memory files to maintain instead of two. Accepted because the marginal write cost is one append per dispatch and the read cost is zero unless you're auditing.

stm-written: yes
ltm-written: yes (see ltm.md 2026-05-24 entry on logging discipline)
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0002 | 2026-05-24 | SLOW

question: Should the actor_baselines draft at `active-project/staff/showrunner/actor-baselines-draft.md` be ACCEPTED, REVISED, or ESCALATED?
context: Step 4d of /and-substance series. 11-actor × 12-axis (132-cell) matrix. Gating: /and-substance book b01 HARD-aborts until matrix is dense and persisted. Four open judgment calls surfaced by screen-writer. All four are reversible via /and-substance series revise actor_baselines. Downstream auditors will surface misfires at /and-substance book Phase 5 bone-gate.
options: (a) ACCEPT — persist matrix, proceed; (b) REVISE — redispatch screen-writer with per-cell changes (~50-80k tokens); (c) ESCALATE — user attention on taste calls admin can decide from precedent

decision: ACCEPT
basis: ltm:2026-05-24 (handle routine; escalate only irreversible/wide-blast/human-only) + methodology:3a (reversibility) + methodology:3b (cost)
rationale: Read the full 132-cell draft and cross-checked against state_axes lines 87-220. Structural commitments are unambiguously correct — Taylor's 9 protagonist moves lifted directly from state_axes, Wren as sole relational_anchor_status carrier, Otto as sole social_tether-antag carrier, Alicent/Otto as the two world-axis movers. The four open calls are all fine-grained taste decisions that the auditor's downstream gate will catch if wrong: (1) Rhaenyra INVERTED CARRIER on position-world and political_register-world is defensible and structurally coherent — the notes document it clearly so the auditor won't misread it as ambiguous; not-applicable would erase the road-not-taken irony that is visible in the narrative; (2) Aemond static 8→8 on position-world is the correct choice — his enforcement-ceiling standing IS relevant to the matrix contrast with Otto/Alicent's movement toward 9, and static at 8 expresses that accurately; (3) Criston static 8→8 on position-world is parallel logic, same conclusion; (4) Sera static 6→6 is a fine-grained rank inference — 5 or 7 would also be defensible but 6 is not wrong, and the note ("court-tier, protected, not a faction agent") is the right framing. None of the four calls lock in anything that costs more to fix later than a revise redispatch. REVISE would burn 50-80k tokens with near-zero expected change in the structural commitments.
trade-off: Accepting before a human eyes the four open calls. Mitigated by: (a) all four are reversible; (b) Rhaenyra's INVERTED CARRIER notation is explicit in the draft notes — downstream auditors will see it; (c) the static-vs-not-applicable calls for Aemond/Criston are fully commutative for the downstream bone-gate; (d) Sera's rank inference is pinned at a defensible midpoint. Not-applicable alternative for Rhaenyra would silently erase the structural irony — the INVERTED CARRIER approach preserves it with explicit labeling, which is the better information-forward choice.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0003 | 2026-05-25 | FAST

question: What is the next step after /and-substance chapter b01c01 Phase 7 + parking-lot system landing?
context: b01c01 fully scened (status: scened), parking-lot system live with 3 entries (pl-002 SOFT targets /and-write b01c01, pl-003 SOFT targets /and-write *), Phase 7 exit state named `next: /and-write b01c01`. Branch clean and pushed. Three distinct work units completed today.
options: (1) /and-write b01c01 — canonical chain advance, pulls in SOFTs at Phase 0 scan; (2) /and-substance chapter b01c02 — populate next chapter while context warm, defer bones; (3) /and-cut — checkpoint, pause; (4) other (test parking-lot mechanism, etc.)

decision: /and-write b01c01
basis: goal:1 (pipeline correctness — honor the chain's declared next: pointer) + methodology:3e (convention — canonical chain advance is what the command body declared)
rationale: The Phase 7 exit state is the pipeline's own declared next step. The two SOFT parking-lot entries targeting this run (pl-002 Wren prose texture, pl-003 moral_framework + naming) are correctly staged for bone authoring — they are bone-level concerns, not scene-chunking concerns, so advancing to c02 before bones would defer the SOFTs past their natural resolution point. No irreversibility consideration favors waiting; bones for c01 must be authored before /and-facets can run regardless.
trade-off: Higher per-command cost than a /and-substance chapter run. Accepted: the canonical chain is the only path to a shippable c01 draft, and the parking-lot SOFTs are well-targeted for this phase. Advancing to c02 instead would widen the unboned-chapter debt without reducing overall spend.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no
