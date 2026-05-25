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

---

## DEC-0004 | 2026-05-25 | SLOW

question: Four pre-Phase-1 proceed questions for /and-facets b01c01: (1) restore build_cite_index.py from git? (2) route pl-2026-05-25-004 bone-16 dialogue call to author? (3) full-run vs phase-1-only vs reconsider? (4) empty locations: header — surface or fix upstream?
context: Phase 0 complete. Chapter b01c01, status bones-written. 27 bones / 3 scenes. Bones-review PASS-WITH-NOTES. Zero speech-bone SVOs. Parking-lot item pl-2026-05-25-004 (SOFT) flags bone 16 with three routing options. BLOCKER: build_cite_index.py missing from disk — over-deleted in scrub commit 0db8d64; intact in git history and project_05 mirror. Bones header locations: empty; loc-state facet will likely return near-empty. Full run estimated 60-100 Agent dispatches, hours of wall-clock.
options:
  Q1: (a) restore script from git before Phase 1 [default YES]; (b) skip (pipeline non-functional without it — not a real option)
  Q2: (a) surface three options to dialogue-facet author at dispatch time [default]; (b) pre-decide option (a) cite-as-is; (c) pre-decide option (c) /and-write revise [caller says OOS for /and-facets]
  Q3: (a) full-run end-to-end; (b) phase-1-only checkpoint and pause; (c) reconsider/defer
  Q4: (a) surface as Phase 5 audit process note; (b) edit bones file header to add loc slug [default surface-only]

decision:
  Q1: YES — restore build_cite_index.py from git before Phase 1.
  Q2: Surface options (a) and (b) to the dialogue-facet author; exclude (c) as explicitly OOS. Let author choose.
  Q3: Full-run end-to-end.
  Q4: Surface as Phase 5 audit process note only; do not edit the bones file.

basis:
  Q1: goal:1 (pipeline correctness — restoring a known-good infrastructure artifact from git is mechanical and reversible) + methodology:3a
  Q2: methodology:3d (optionality — let the agent closest to the artifact decide) + methodology:3c (blast radius — surfacing options costs nothing extra)
  Q3: goal:1 (pipeline correctness — /and-stitch is blocked on /and-facets clearing; partial stop adds coordination cost without reducing spend) + methodology:3e (convention — command body specifies end-to-end)
  Q4: goal:1 (pipeline correctness — bones are upstream artifacts; /and-facets is read-only-on-bones) + methodology:3c (blast radius — editing bones mid-pipeline violates the command contract)

rationale:
  Q1: The script is not a content decision — it is infrastructure the pipeline cannot run without. The over-deletion was a side-effect of the scrub commit, not an intentional removal. Restoring from git is fully reversible and has no downstream content impact.
  Q2: The dialogue-facet author has the bones file, chunk text, and rubric in context. Admin does not have the chunk text verbatim. Surfacing options (a) and (b) with the caller's reasoning attached costs one extra line in the dispatch prompt and keeps the author's judgment in the loop. Option (c) is OOS and correctly excluded.
  Q3: A phase-1-only stop saves no meaningful spend (Phase 1 is the expensive fanout regardless) and creates a resume-checkpoint coordination cost. Full-run is what the command body declares. The spend level is high but routine for /and-facets; it does not cross the methodology escalation threshold ("meaningful slice of project budget on a single operation" — this is a single chapter's facet run, not a multi-chapter cascade).
  Q4: The bones file is an upstream artifact owned by /and-write. Editing it from within /and-facets violates the command contract and could invalidate the bones-review result. The loc-state facet noting the empty header and the Phase 5 auditor surfacing it as a process note is the correct path. If it is a genuine gap, the parking lot or a /and-write revise call is the resolution — not a mid-run bones edit.

trade-off:
  Q1: n/a — restoring a deleted infrastructure file from git history has no meaningful trade-off.
  Q2: Author may still choose (a) cite-as-is (caller's prediction), so surfacing options costs marginally more prompt length. Accepted: preserving optionality for the agent closest to the artifact is worth the marginal cost.
  Q3: Higher wall-clock and token spend than a phase-1-only stop. Accepted: the chain is blocked on this clearing; a mid-run stop adds coordination cost without reducing total spend. /and-facets is re-runnable per rerun-protocol.md if something fails mid-run.
  Q4: Loc-state facet will likely return near-empty entries. Accepted: that is an accurate reflection of the bones file's declared locations scope, and the auditor is the correct surface for the gap — not a mid-run upstream edit.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0005 | 2026-05-25 | ESCALATED

question: "Do a third pass" — which interpretation should drive the /and-facets b01c01 pipeline advance?
context: Mid-/and-facets b01c01, Phase 5b audience-gate cycle 1 in progress. 5 of 10 facets returned: 2 PASS (interest-narrator, metaphor), 2 REVISE (loc-state, memory), 5 still pending. Memory's dissent is unanimous on a structural gap (spine gap @26, slug convention). Loc-state's dissent converges with auditor flag-017. The cap-burn DELETE path is spec-reserved for cycle 3; cycle 2 has not yet run; cycle 1 is not yet complete. Caller proposed 5 interpretations; default was option (a): complete cycle 1, run cycle 2, run cycle 3, with cap-burn as the spec-prescribed terminal.
options:
  (a) Spec path: complete cycle 1, fixer-pass for cycle-2 remediation, cycle-2 gate, cycle-3 gate, cap-burn DELETE as terminal if needed
  (b) Cap-burn jump: treat structural-dissent pattern as cycle-3-equivalent now; skip cycles 2 actual; invoke override path
  (c) Wait for cycle 1 fully, then re-ask
  (d) Escalate to human — directive doesn't map cleanly to spec mechanics

decision: ESCALATED-TO-HUMAN
basis: human-only — ambiguous short directive against a non-trivial spec-governed pipeline decision; jumping the cap-burn path is effectively an irreversible shortcut (deleted facet entries cannot be recovered without re-running the full facet authoring chain); goals + methodology do not cleanly decide between (a) and (b) because the directive's meaning is genuinely ambiguous and option (b) would constitute an out-of-spec pipeline deviation requiring explicit authorization.
rationale: "Do a third pass" is a two-word instruction against a multi-cycle spec-governed gate. Interpretation (a) is the safe-path answer but it is not clearly what the user said. Interpretation (b) is plausible but would involve skipping spec-mandated cycle 2 and invoking cap-burn DELETE before the spec authorizes it — that is an irreversible pipeline deviation per methodology §human-only (irreversible destructive operations). I cannot confidently eliminate (b) vs (a) from goals alone, and acting on (b) without confirmation risks corrupting the facet file. Methodology 3a (reversibility) pushes against (b) decisively; but if the user meant (b), proceeding with (a) is also wrong. The ambiguity is genuine, the stakes are meaningful, and this is exactly the escalation threshold the admin contract defines.
trade-off: Escalating adds one human round-trip. Accepted: the cost of guessing wrong on a cap-burn DELETE path is higher than the cost of asking once.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no
