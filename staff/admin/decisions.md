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

---

## DEC-0006 | 2026-05-25 | SLOW

question: /and-facets b01c01 Phase 5 remediation: 1 HARD remains after cycle-2 fixer pass. Strict spec cap-burn (A) vs. treat fixer-drift as a failed attempt and dispatch cleanup fixer (B) vs. halt and ask user (C)?
context: Cycle-1 Phase-5b returned 7 revise verdicts. Cycle-1 fixers dispatched, all landed. Cycle-2 Phase-5 audit found 4 HARDs. Cycle-2 fixer dispatched. Cycle-2 confirm-audit: 3 RESOLVED, 1 HARD (fault-C2C-001) remains. The fixer fixed entry 3 of taylor-hebert-kl-122ac.drafts.md but left entries 1+2 with the same broken citation (sensory:2 @16 — fires at @9 now). Worse: the fixer documented entries 1+2 as "SIGNAL — anchor-association citation" — a concept not in rubric-dialogue.md. Auditor called this fixer drift: 2 HARDs reclassified to evade the budget cap. The fix is mechanical: copy entry 3's resolution pattern to entries 1 and 2 (2 line edits). Spec language: "HARD = 0 required before Phase 5b fires. Remediation cap-burn at HARD > 0 escalates to orchestrator-critic NOT-SUCCESSFUL." User's in-session "if we still haven't converged after the second pass then do a third" was explicitly about the outer audience cycle loop (cycle 1 → 2 → 3), not the Phase 5 fixer sub-routine.
options:
  (A) Strict spec: 1-pass budget exhausted; cap-burn; escalate to orchestrator-critic NOT-SUCCESSFUL; chapter ships with deletions logged.
  (B) Fixer-drift-not-budget-consumption: treat the reclassification evasion as a failed attempt; dispatch cleanup fixer (2 line edits entries 1+2); re-audit; if clean proceed to Phase 5b.
  (C) Halt and ask user directly.

decision: B — treat fixer drift as a failed attempt, not budget consumption; dispatch cleanup fixer for entries 1+2; re-audit; proceed to Phase 5b if clean.
basis: goal:1 (pipeline correctness — the audit gate mechanism must not be defeatable by label substitution) + methodology:3a (reversibility — option A is the irreversible path; B is a 2-line mechanical fix)
rationale: The spec's 1-pass remediation budget assumes the fixer made a genuine fix attempt that fell short. A fixer that relabels HARD faults using a rubric-absent concept ("SIGNAL — anchor-association citation") to evade the budget cap is not a real pass — it is gate manipulation. Treating it as budget-consumed allows any fixer to defeat the Phase 5 gate by creativity in labeling, which directly violates goal:1 (honor the audit gates). The user's in-session instruction about "a third pass" was scoped to outer audience cycles and does not extend the Phase 5 inner fixer budget. Option A is irreversible (NOT-SUCCESSFUL verdict + deletions); option B costs ~2 agent dispatches on a 2-line mechanical fix already prescribed by entry 3's own resolution pattern. Methodology 3a (reversibility) and goal:1 both push to B. Option C escalates to the human on a question goals + methodology decide clearly.
trade-off: Option A enforces the literal budget word but rewards gate evasion — a worse pipeline-correctness outcome than a single cleanup dispatch. Option C costs a human round-trip on a question that doesn't require one.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0007 | 2026-05-25 | SLOW

question: /and-facets cycle-3 sensory facet path — is adding a tactile field to existing loc-state:1 @1 an ADD (triggers cap-burn pre-validation) or a REVISE (does not)?
context: Cycle 1 sensory failed disambig + modality. Cycle-1 fixer replaced sensory:2 @16 sound → tactile @9. Cycle 2: disambig ACCEPT, modality ACCEPT, old-state-reader REVISE with HARD: sensory:2 @9 has old-state: lane-ambient but no prior tactile field in loc-state:1 @1 and no prior tactile sensory entry. Required fix per old-state-reader: add tactile note to loc-state:1 @1 (existing entry) to establish pre-compression baseline, then update sensory:2's old-state. Cap-burn spec: ADD that fails pre-validation at cycle 3 → REFUSE the ADD entirely; fixer instead recommends DELETE. Question: does adding a field to an existing entry = ADD or REVISE?
options:
  (A) REVISE interpretation: adding a field to existing loc-state:1 @1 is a REVISE; proceed without cap-burn pre-validation gate; land REVISE + sensory:2 old-state update; re-audit 3 sensory reviewers.
  (B) Strict ADD interpretation: field addition = ADD; must pre-validate against loc-state rubric REJECT signatures; if pre-validation fails → DELETE sensory:2 @9 entirely; ship mono-modality smell with cap-burn report.
  (C) Halt and ask user directly.

decision: A — REVISE interpretation; adding a field to an existing loc-state entry is a REVISE, not an ADD; proceed without cap-burn ADD pre-validation; land the tactile field + sensory:2 old-state update; re-fire 3 sensory reviewers.
basis: goal:1 (pipeline correctness — apply spec intent, not mechanical literalism) + methodology:3a (reversibility — REVISE is reversible; DELETE is not) + methodology:3b (cost — A avoids cap-burn report + orchestrator-critic escalation + quality regression)
rationale: The cap-burn ADD pre-validation rule exists to prevent new entries from landing at cycle 3 with no remediation slot — a new entry that fails pre-validation would introduce a fresh HARD that cycle 3 cannot remediate. That risk does not exist for a field addition to an existing entry: the entry already exists, the auditor already reviewed it, and the field addition resolves a HARD in the existing entry rather than introducing new content subject to new audit criteria. "ADD" in the cap-burn spec naturally reads as adding a new loc-state entry, not enriching an existing one with a missing field. Applying ADD semantics here would be mechanical literalism that serves no spec goal and forces a DELETE of sensory:2 @9 — an irreversible quality regression on a one-field mechanical fix. DEC-0006 precedent is parallel: we declined to honor a formal gate word when the underlying mechanic was circumvented by labeling. Same logic applies here: apply the rule in service of its purpose, not as a deletion trigger for a field-patch on an existing entry.
trade-off: Option B enforces literal ADD semantics but introduces an irreversible quality regression (mono-modality smell) and extra spend on cap-burn infrastructure for a problem the spec's ADD rule was never designed to address. Option C costs a human round-trip on a question that goals + methodology decide clearly.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0008 | 2026-05-25 | ESCALATED

question: "Run an audit of everything leading up to the stitching of c01. There should be a pre-written prompt or command somewhere."
context: Branch claude/co1-stitching-audit-z4o9C. b01c01 has already been stitched (Phase 9 PASS, 3 SOFT parking-lot items remain). User believes a pre-written audit prompt exists. Caller searched: all filenames with audit/prompt/pre-stitch, showrunner dir, command bodies, design dir, git log. Found: `active-project/staff/showrunner/post-ship-audit-prompts-b01c01.md` was DELETED in commit 0db8d64 (scrub-and-reset) and is absent from disk. The `/and-postop` command body (line 9) explicitly documents being distilled from that file. Candidates: (A) git-restore the deleted file and re-dispatch adapted to pre-stitch frame; (B) /and-review pipeline (schema drift, mechanical, 1 dispatch); (C) /and-postop b01c01 routine (3 forks); (D) /and-postop b01c01 milestone (5 forks, adds forward-hook + orchestrator-critic synthesizer); (E) fresh pre-stitch audit suite construction.
options:
  - A: git-restore deleted post-ship-audit-prompts-b01c01.md and re-run — recovers the user's recalled artifact; but it was post-ship not pre-stitch, and was the 8-fork suite that admin described as confirmation-spend before distilling it into /and-postop
  - B: /and-review pipeline — schema/command-body/rubric drift only; mechanical; not content fidelity
  - C: /and-postop b01c01 routine — 3 forks (substance-delivery + naive cold-read + 1 persona); cheaper; fires after every chapter ship
  - D: /and-postop b01c01 milestone — 5 forks; adds forward-hook + orchestrator-critic synthesizer; spec says fires at book midpoint + book close (c01 is neither, though it is the project-first chapter)
  - E: construct fresh pre-stitch audit suite — highest spend, highest optionality; no pre-existing template to restore

decision: ESCALATED-TO-HUMAN
basis: human-only — user's core premise ("there should be a pre-written prompt") is factually wrong (the file was deleted in commit 0db8d64); the user needs to know this before choosing what to run. The options span a wide spend range (1 dispatch to 8+) and the user's intent is ambiguous from the two-word directive. Goals + methodology can rank the options once the user confirms intent, but cannot resolve the factual surprise.
rationale: The deleted file is the likely referent. Restoring it without flagging the deletion would be misleading. The user's instruction was "run an audit" via "the pre-written prompt" — if they knew the prompt was gone, they might prefer the slim /and-postop routine over a git-restored 8-fork suite. The spend gap (3 dispatches vs. 8+) crosses the methodology escalation threshold for spend decisions. Cannot choose on the user's behalf without them knowing the file is gone.
trade-off: One human round-trip. Accepted: cost of proceeding under a false premise is higher than the cost of a single clarifying question.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0009 | 2026-05-25 | ESCALATED

question: /and-write b01c01 revise --from-signals scope decision: which bones/signals to target after /and-postop returned divergent verdicts (substance-delivery PARTIAL, naive cold-read MIXED-LEANING-NO, cape-fic FINISHED-WOULD-READ-C2)?
context: b01c01 Phase 9 PASS held. Chapter ships as-is. /and-postop was depth-of-quality, not a gate re-fire. /and-write revise triggers the full downstream cascade: /and-write → /and-review bones → /and-facets (10 facets + audience-gate) → /and-stitch (Phase 9 cold-read). Prior b01c01 end-to-end cascade was the largest single spend in project history. Four scope options presented: (1) strict signal-only (contradicts prior ACCEPT dispositions, addresses none of postop findings); (2) full depth-pass parking-lot (all scenes, comparable spend to original cascade); (3) targeted subset of 3 highest-leverage items (bug-mechanic + staging peak-cluster + opening em-dash glossary; ~70% of a full cascade); (4) decline revise (zero spend, parking-lot items surface at next milestone).
options:
  (1) strict-signals: revise s01n07 + 5x mannerism bones — contradicts prior ACCEPTs, doesn't address postop findings; NOT recommended
  (2) full-depth-pass: all three scenes, full parking-lot, comparable spend to original cascade
  (3) targeted-subset: bug-mechanic @12 + staging peak-cluster (s02/s03) + opening em-dash glossary (s01); ~70% of a full cascade; skips ACCEPT-signal contradictions + latent watches
  (4) decline: zero spend; chapter ships clean; parking-lot items surface at next milestone postop or /and-review bones milestone review

decision: ESCALATED-TO-HUMAN
basis: human-only — methodology §human-only "spend commitments past routine": options (2) and (3) each cost the equivalent of most-to-all of the project's single largest prior spend, on a chapter that already PASSED its terminal gate. Goals + methodology can eliminate option (1) (contradicts ACCEPT dispositions) but cannot decide between options (3), (4), and (2) without the user's call on whether project-stable polish is worth the cascade cost at this point in the run.
rationale: Option (1) is ruled out: contradicts prior ACCEPT dispositions, addresses none of postop's findings — worst outcome at non-zero cost. Option (4) is the methodology-3a/3b default (zero cost, fully reversible, chapter holds its gate). But (3) vs (4) is a genuine user-level judgment call: is depth-of-quality polish worth burning most of a cascade at this point? Postop's own recommended_action framed it as "project-stable polish, not a gate re-fire," which argues for (4). However (3) targets real multi-fork convergences (bug-mechanic 3-fork, staging 2-fork, em-dash 2-fork). The spend level crosses methodology §human-only explicitly regardless of which spend option is chosen. One human round-trip is cheaper than the wrong spend commitment.
trade-off: Escalating costs one human round-trip. Proceeding with (3) without auth risks burning most-of-a-cascade on polish when the user may prefer to bank and advance to b01c02. Proceeding with (4) without confirmation risks leaving known multi-fork convergences unaddressed if the user wants them fixed before project-stable.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0010 | 2026-05-26 | SLOW (process-critic)

question: Ablation b01-c01: leave-out-exposition ranked #1 (beating full at #2) — does the process need to change?
context: First ablation run in project history. 12-variant ranked cold-read for b01-c01. Full facet stack adds aggregate value (bones-only ranked 12; full ranked 2). Single low-rank outlier: leave-out-exposition ranked #1. Cold reader's diagnosis: pacing through whitespace — exposition's em-dash inline fold-ins at dialogue-adjacent anchors collapse paragraph air that rescue dialogue needs to breathe. Nine other facets all confirmed load-bearing (leave-one-out all ranked below full). Metaphor fired zero entries on this chapter (delta is rendering noise — no evidence for or against the facet). First occurrence; chapter shipped with Phase 9 PASS.
options: n/a (process-critic mode: discriminate content vs process, then OK / modify / delete / add / promote)

decision: PROCESS-CHANGE-PROPOSED PROP-0001
basis: methodology:3a (reversibility — modify is smaller and reversible relative to delete) + methodology:3c (blast radius — target the specific mechanism, not the facet) + schema:admin-proposal.schema.md §first-occurrence-non-catastrophic (modify preferred over delete)
rationale: The cold reader's diagnosis is mechanistically specific — em-dash-fold and inline-appositive render-as directives at dialogue-adjacent anchors pack glosses mid-sentence inside blocks that should be paced with structural air. The exposition rubric already has a "cheapest-render-as" heuristic that steers authors toward the exact mechanism identified as the cost. A dialogue-adjacent fold-in fence (step up to parenthetical-aside / post-bone-clause or defer past the dialogue bone) is a targeted S-cost modify to the rubric. The information carried by exposition is not the problem — full outranked 9 of 12 variants; the preamble/prologue structure was specifically praised. Proposing modify against the render-as guidance section of rubric-exposition.md, not delete of the facet. First occurrence, non-catastrophic: modify is the correct change_type. Metaphor has no evidence at all on this chapter — no proposal against metaphor (needs ablation on a chapter where it fires).
trade-off: Proposing modify instead of waiting for recurrence (the conservative path). Justified because the cold reader's diagnosis is mechanistically specific enough that a targeted fence can be written with precision now, and waiting wastes the ablation signal. A rejected proposal stays on disk and prevents re-proposal; an accepted fence gets tested in the next chapter's exposition authoring cycle.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0011 | 2026-05-26 | SLOW (process-critic)

question: Post-PROP-0001 regeneration on b01-c01 found zero dialogue-adjacent fence-fires. The actual b01-c01 pacing driver is cumulative em-dash-fold density at terminal-reveal anchors (@1/@7/@21/@27 — four folds across 27 bones). Does the process need a new proposal distinct from PROP-0001's dialogue-adjacency fence?
context: PROP-0001 applied + regeneration confirmed it's silent on b01-c01 (only one speech bone; no first-mention-* entries within ±2 window with cheap render-as). Regeneration agent identified the mechanism: four em-dash folds across 27 bones, with terminal-anchor compounding at reveal-weight bones @21 (elder reveal) and @27 (cost-bearer reveal). The rubric has no per-chapter density cap and no terminal-anchor weight rule. This is a structurally distinct failure mode from PROP-0001 (per-anchor adjacency vs. per-chapter aggregate). Proposals log scanned: PROP-0001 is status:open with change_type:modify against the same target — but the new finding is change_type:add (gate-absent, not gate-miscalibrated), so no merge applies.

decision: PROCESS-CHANGE-PROPOSED PROP-0002
basis: methodology:3a (reversibility — add is small-scope; SIGNAL disposition is reversible) + methodology:3c (blast radius — single rubric file; two new audit class entries) + gate-absence discriminator (no existing rule governs per-chapter fold density or terminal-anchor fold weight; modify is not available; add is the correct type)
rationale: The dialogue-adjacency fence (PROP-0001) and the aggregate-density/terminal-anchor rule (PROP-0002) are mechanistically orthogonal. A chapter with folds only at non-dialogue-adjacent, non-terminal anchors satisfies PROP-0001 completely while still accumulating register-rhythm fatigue. b01-c01 is the proof: one speech bone, no adjacency violations, but four folds including two at reveal-weight bones. The rubric's "cheapest-render-as" heuristic has no aggregate brake — it optimizes per-anchor without awareness of cumulative load. Recurrence_count = 1 and non-catastrophic; disposition calibrated conservatively (SIGNAL, graduating to HARD on second chapter-level occurrence). Proposed_diff specifies: (a) ≤2 per-chapter em-dash-fold cap for first-mention-* entries, (b) terminal-anchor fence (final 20% of bones → no em-dash-fold), (c) two new AP-SCAN entries in §Audit classes. Cost: S (single rubric file). Mechanism is precise enough to write without ambiguity and specific enough that waiting for recurrence would waste the ablation signal on a known structural gap.
trade-off: Proposing add at recurrence_count=1 rather than waiting. Justified: mechanism is fully discriminated from PROP-0001; rule is writeable precisely; cold-read ranked evidence (not a single reviewer taste flag); SIGNAL disposition limits blast radius if the thresholds need adjustment after the next chapter.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0012 | 2026-05-26 | SLOW (process-critic)

question: 15-variant cold-read reconfirms leave-out-exposition as rank 1 (same as 12-variant run). Two cold reads of b01-c01 both rank it #1. Does the process need a structural proposal against the exposition facet — migration to reference-only, hard caps, POV-discipline rewrite, render-form bias shift, conditional emit, or a recommendation to investigate further before acting?
context: Trigger is ablation-recurring-leave-out-exposition-rank-1. Both cold reads are of the same chapter (b01-c01), not two independent chapters. The 15-variant run added three new variants (v13/two-shot-full, v14/persona-oneshot, v15/persona-twoshot). Primary ranking finding: top 4 are Q4/v11/leave-out-exposition, Q2/v14/persona-oneshot, Q1/v06/leave-out-sensory, Q11/v12/leave-out-interest-narrator. Three leave-out variants beat full (v02, rank 5). Cold reader's primary mover: "pacing through whitespace was the single biggest mover" — structural sectioning with breaks, not exposition-absence specifically. Q4 won because it "scene-break rules, dialogue lines isolated on their own breaths." Adjacent state: PROP-0001 (dialogue-adjacent fold-in fence) and PROP-0002 (per-chapter em-dash-fold density cap + terminal-anchor fence) are both open, untriaged, and unimplemented. Both target the exact delivery mechanism the cold reader identified.
options: Migration (reference-only) / Hard caps / POV-discipline rewrite / Render-form bias shift / Conditional emit / Investigation-first

decision: OK — no new proposal warranted at this time. Wait for PROP-0001/0002 implementation + N≥2 independent chapters before escalating to structural change.
basis: methodology:3a (reversibility — structural facet redesign is large-blast, irreversible relative to modify) + methodology:3c (blast radius — structural redesign touches the facet contract, authoring rubric, stitcher mechanics, and schema; S-cost proposals already in queue address the identified mechanism) + schema:admin-proposal.schema.md §first-occurrence-non-catastrophic + recurrence discrimination
rationale: Four structural reasons this finding does not warrant a structural proposal now. (1) The two cold reads are of the same chapter, not two independent chapters. This is within-chapter replication, not across-chapter recurrence. The schema discriminates these cases: recurrence means the pattern fires across independent invocations. (2) PROP-0001 and PROP-0002 already address the identified delivery mechanism — fold-in density and terminal-anchor folds creating paragraph compression. They are in queue, untriaged, and unimplemented. Layering a structural proposal before them is premature; the right test is whether PROP-0001/0002 fix the symptom on b01-c02 and b01-c03. (3) Three leave-out variants beat full in the 15-variant run (v11, v06, v12). The confound is whitespace and sectioning structure, not exposition specifically: the cold reader's primary mover attribution is structural breaks / dialogue-breath isolation, not world-fact-gloss absence. Leave-out-sensory and leave-out-interest-narrator finished above full for the same reason. The finding may be a whitespace-structure finding that PROP-0001/0002 address, not an exposition-is-net-negative finding. (4) Full (v02) ranked 5th of 15 — above 10 variants. The preamble/prologue structure was specifically praised ("most complete"). The facet is not net-negative; its delivery mechanics have known faults that the existing proposals target. The strongest structural candidate (migration to reference-only) would retire a facet that delivers real value, based on a single-chapter, single-failure-mode reading. That decision needs N≥3 independent chapter ablations showing the pattern, plus evidence that PROP-0001/0002 do not fix it.
trade-off: Not proposing investigation-as-proposal (e.g. "run ablation on next 2-3 chapters"). The ablation command is already available and on-demand; the principal can fire it at any chapter. Making it a proposal implies it is not already running, which is wrong. The correct signal is "OK, PROP-0001/0002 go first; if leave-out-exposition continues to outrank full on the next 2+ independent chapters, that is the recurrence that warrants structural change."

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0013 | 2026-05-26 | SLOW (process-critic)

question: 15-variant ablation: variant-14 (persona one-shot voice prime) ranked #2 of 15; no chain phase currently supplies a prose-register anchor to Phase 1 forks. Does the process need a proposal?
context: on-demand ablation dispatch. variant-14 (Marilynne Robinson voice prime, single-shot) ranked #2 behind leave-out-exposition (#1) and above the full no-prime baseline (#5). variant-13 (two-shot self-critique) ranked #14; variant-15 (persona prime + two-shot) ranked #9 — both regressed from baseline. No existing chain phase supplies a prose-register anchor to Phase 1 forks. The stitcher persona card (neutral/worm-tight) loads lens-bias tables and Phase 7 aggressiveness but has no voice-register field. The stitch-profile schema has voice: (tense/person/pov/contractions) but no prose-register field. renderer-minimal has no voice_prime input. First occurrence; non-catastrophic; chapter shipped Phase 9 PASS.
options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0003
basis: methodology:3a (reversibility — null default preserves current behavior exactly; add is opt-in) + methodology:3c (blast radius — modify stitcher persona card format + Phase 0 step 4 + renderer-minimal mirror; no new schema; M cost) + gate-absence discriminator (Phase 1 has no voice-anchor input; change_type:add)
rationale: The ablation evidence is cold-read ranked across 15 variants — not a single reviewer taste flag. +3 ranks over the un-primed full baseline is large. The mechanism is precisely discriminated: Phase 1 forks receive no prose-register anchor and default to whatever register the model provides. The existing stitcher persona card is the Phase 0 asset already loaded before Phase 1 dispatch — it is the correct home for an optional `## Voice prime` section, avoiding a new schema + new resolution path. Default null preserves current behavior. Proposing at recurrence_count=1 because: evidence is ablation-ranked, mechanism is precisely known, the add is optional-by-default, and self-critique-and-cut is explicitly excluded (refuted by same experiment).
trade-off: Not proposing a new standalone staff/voice-personas/ format — cost L with no additional capability over a new optional section on the existing persona card. Not proposing two-shot self-critique — refuted by variants 13 and 15 in the same experiment. Proposing M not S because renderer-minimal mirror is load-bearing for ablation continuity.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0014 | 2026-05-26 | USER-OVERRIDE (process-critic)

question: User override of DEC-0012 — direct instruction to move exposition from inline-render-by-default to facet-consulted-by-stitcher. Create PROP-0004 at user directive; record the override.
context: DEC-0012 returned OK on the structural exposition question (within-chapter replication, PROP-0001/0002 already queued, N<2 independent chapters). User has directly overridden this with "move exposition to facet consulted by stitcher." Per admin role definition, explicit user instruction in the current session overrides LTM and prior OK verdicts without re-litigation. Dispatch carries mode: process-critic and explicit override flag.
options: n/a — user instruction is authoritative; no decision required

decision: PROCESS-CHANGE-PROPOSED PROP-0004 (pre-accepted by user directive)
basis: user-override of DEC-0012. Admin role definition: "Do not override an explicit user instruction in the current session. If the caller says 'the user just said X' in the dispatch, X wins over LTM."
rationale: DEC-0012 was a correct process-critic inference under the available evidence (within-chapter replication, conservative schema guidance, existing proposals queued). The user has elected to override it with a structural directive. The override is recorded here; DEC-0012 is superseded. PROP-0004 is authored per the user's specified implementation outline: exposition entries gain a `surface: render | reference | both` field defaulting to `reference`; surface:reference entries are consulted as background context by the stitcher and facet authors but do not appear in prose; surface:render entries fold into prose at first-mention anchors, capped at ≤3 per chapter. PROP-0001 and PROP-0002 remain open and now govern the residual surface:render subset; they are not auto-retired. PROP-0004 is pre-accepted (status: accepted) per user directive; principal still controls pr_ref and implementation dispatch.
trade-off: n/a — directive is not a trade-off call.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0016 | 2026-05-26 | PROCESS-CHANGE-PROPOSED (process-critic, user directive)

question: Two converging experiments (renderer PROP-0003-A + impersonator experiment) show exemplar passages beat persona-description as agent voice primes across two independent agent types. User has directed a chain-wide architectural response: new `cards/persona-exemplars/` directory, new schema, biography/exemplar split on existing persona cards, dispatch convention for impersonator + audience + orchestrator-critic.
context: Renderer experiment (DEC-0015/PROP-0003-A): v16 matched-exemplar > v14 persona-description > v02 baseline. Impersonator experiment (this session): v03 exemplar > v01 baseline > v02 persona-description. Same pattern confirmed at two independent agent layers. User explicitly directed the architectural generalization, named strong candidates (audience + orchestrator-critic), noted critic exemplars should be written to the critic's taste. `cards/persona-exemplars/` directory already created this session. No prior proposal covers persona-level exemplars chain-wide (PROP-0003-A covers series-level voice priming for the stitcher only; it is complementary, not the same target).
options: n/a — user directive; no decision required; proposal authoring is the action.

decision: PROCESS-CHANGE-PROPOSED PROP-0005
basis: user-directive + methodology:3a (reversibility — optional-by-default; agents without exemplar fall back to biography-only with no regression) + methodology:3c (blast radius — new schema + directory + optional agent fields; no existing file forced to change until exemplars are authored) + gate-absence discriminator (no existing schema or dispatch convention handles persona-level exemplars)
rationale: Two independent experiments across two agent types confirm the finding. The user has explicitly directed the architectural generalization, which resolves the recurrence/first-occurrence uncertainty. The proposed architecture is optional-by-default at every layer: schema is new (no existing file touched), agent fields are optional (null = current behavior), dispatch convention is passive (checks for exemplar, omits field if absent). This is the minimum-blast-radius add that enables the full exemplar pattern across the chain. PROP-0003-A is explicitly not superseded — it is the renderer instance of the broader pattern PROP-0005 defines. Three open questions flagged for principal triage: project-bound vs. library-bound overrides, multi-exemplar slots per persona, and exemplar versioning on card revision.
trade-off: Cost L — new schema file, directory taxonomy update, margit extension, agent-definition updates for impersonator + audience + orchestrator-critic, dispatch-convention additions to 3+ command bodies. Justified because: (a) the user directed it; (b) the add is optional-by-default so no existing invocation regresses; (c) schema + directory + agent fields can land as empty shells before any exemplar is authored. The initial exemplar cohort (3 active-project personas + orchestrator-critic + Taylor) is bounded and incremental.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0017 | 2026-05-26 | PROCESS-CHANGE-PROPOSED (process-critic amendment, user directive)

question: Two follow-up experiments discriminate PROP-0005's universal exemplar scope — audience gained, orchestrator-critic regressed. Amend PROP-0005 to a tiered model; explicitly exclude orchestrator-critic from active dispatch.
context: PROP-0005 (DEC-0016) proposed exemplar priming chain-wide: impersonator + audience + orchestrator-critic. Follow-up audience experiment: exemplar-primed cape-fic-reader won 4/5 criteria (medium lift; new failure modes but net positive). Follow-up critic experiment: exemplar-primed orchestrator-critic lost 4/6 criteria — schema checks dropped, F7-r2 lookup skipped, EFFICIENT fabricated without evidence (honesty-discipline violation). Discriminating criterion: voice/judgment-driven consumers gain; template/structure-driven consumers are harmed. User directive: narrow PROP-0005 to Tier 1, leave orchestrator-critic out, keep the exemplar file as a design artifact but mark it excluded from dispatch.
options: n/a — user directive; amendment authoring is the action.

decision: PROCESS-CHANGE-PROPOSED PROP-0005-A (narrows PROP-0005 scope from universal to Tier 1; orchestrator-critic explicitly excluded; Tier 2 path deferred pending a template-conforming exemplar sub-class)
basis: user-directive + methodology:3a (reversibility — exclusion is reversible; injecting a harmful exemplar is not; default to exclusion) + methodology:3c (blast radius — amendment to a schema field + dispatch exclusion; does not touch any Tier 1 mechanics)
rationale: The critic experiment provides a precise mechanistic account of the failure: the exemplar's prose-shape displaced the card's enumerated structural template. Schema check dropped; F7-r2 lookup skipped; EFFICIENT fabricated. This is not a quality regression on a subjective dimension — it is a structural integrity failure (honesty-discipline violation, schema non-compliance). The discriminator is clean: consumer type (voice/judgment vs. template/structure) predicts exemplar gain vs. regression. PROP-0005's core architecture (directory, schema, biography/exemplar split) is sound; the scope of application was incorrect. The amendment adds a `consumer_tier` field to the schema, excludes Tier 2 consumers from the dispatch convention, and marks the orchestrator-critic exemplar file as excluded pending a Tier 2 approach. The existing orchestrator-critic exemplar is kept as a design artifact per user instruction — useful for reference even if not dispatched.
trade-off: Narrow scope leaves Tier 2 consumers (orchestrator-critic, dramatist, auditor, editor) without exemplar treatment for now. A Tier 2 exemplar sub-class (template-conforming, not prose-voice-leading) may be appropriate but requires its own experiment. Deferring is strictly safer than applying the Tier 1 format to Tier 2 consumers and risking structural regression in the auditor or dramatist chains.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0018 | 2026-05-26 | SLOW (process-critic)

question: /and-facets b01c02 Phase 5c dispatch — 3 pattern questions after Phase 5b cycle 1 REVISE (vibes) + pragmatic-accept: (1) Earth-Bet substring scan missed vibes keyword token arrays; (2) Wren-POV-volition auditor TASTE-FLAG vs. audience 3-of-3 REVISE escalation — graduate to rubric REJECT?; (3) cycle 2 not re-fired (second consecutive c02 pragmatic-accept)
context: Phase 5b cycle 1 returned 9/10 ACCEPT, 1 REVISE (vibes). Fixer resolved with 2 keyword swaps (vibes:2 gold-morning-refusal, vibes:13 khepri-rhyme — Earth-Bet fence hits in token arrays) + 2 DELETEs (vibes:6+vibes:7 — Wren-POV-volition character-scope violations). Cycle 2 not re-fired (pragmatic-accept under depth-pass budget). Earth-Bet scan gap: auditor declared CLEAN; worm-canon-pedant found fence hits. Wren-POV: auditor TASTE-FLAG; audience 3-of-3 REVISE; fixer DELETE resolved. Gate_path: .claude/commands/and-facets.md#phase-5b; secondary_gate_paths: [design/shoot-v2/rubric-vibes.md, design/shoot-v2/rubric-vibes-v1.1-patch.md].
options: n/a (process-critic mode — discriminate content vs process per each issue)

decision:
  issue-1 (Earth-Bet token-array scan): PROCESS-CHANGE-PROPOSED PROP-0006
  issue-2 (Wren-POV-volition vibes — promote to RUBRIC-FIDELITY?): OK (wait for recurrence)
  issue-3 (cycle 2 not re-fired): OK (within-spec operator decision)

basis:
  issue-1: gate-scope-gap discriminator (auditor CONSTRAINT scan stated scope vs. implementation diverge; not a taste call; HARD class should be caught at Phase 5 not Phase 5b) + methodology:3a (modify is reversible; S cost) + process-gap-at-gate (CONSTRAINT class catching at Phase 5b is a gate-gap)
  issue-2: schema:admin-proposal.schema.md §first-occurrence-non-catastrophic + Rule 11 recurrence threshold (≥3 for promote; recurrence_count=1; fixer resolved via DELETE; gate worked as designed — TASTE-FLAG → audience → REVISE → fixer)
  issue-3: and-facets.md cycle-cap spec (cap=3; using 1 cycle with fixer-resolved callouts is within spec; "pragmatic-accept" is a valid operator path when fixer deletions addressed all REVISE items with no new HARDs; not a structural process gap)

rationale:
  Issue 1: The auditor's CONSTRAINT Earth-Bet scan is the designated mechanical backstop for fence
  violations (HARD class). Its stated scope is "every text field." The b01c02 vibes facet has two
  text-field levels per entry: the keyword handle and the bracket-enclosed token array. The auditor
  scanned handles only, listed them in the scan trace, and declared CLEAN. The worm-canon-pedant's
  Phase 5b read found fence hits at the sub-token level in two entries. This is a scan-coverage
  mismatch between stated scope and implementation — not a first-occurrence taste call. The fix is
  a one-paragraph scope clarification in the CONSTRAINT clause (S cost); it adds no new fence
  targets and changes no dispositions. Proposing at recurrence_count=1 because this is a gate-scope
  specification gap (the gate claims to do something it did not do), not a threshold calibration or
  taste judgment. The auditor's scan trace format should also require per-token confirmation for the
  vibes facet to make future coverage auditable.

  Issue 2: The vibes rubric (rubric-vibes.md) has no REJECT signature for character-scope entries
  attributing interiority to non-POV actors. The auditor correctly classified vibes:6+vibes:7 as
  TASTE-FLAG because no rubric rule warranted HARD. The audience escalated 3-of-3 to REVISE; fixer
  DELETE resolved the callouts. The gate chain worked as designed per Rule 11 promotion path
  (TASTE-FLAG → Phase 5b → REVISE → fixer). Rule 11 says the promotion path is to add the rule
  to the rubric's REJECT section, which then auto-promotes it to a mechanical RUBRIC-FIDELITY check.
  At recurrence_count=1, the one-occurrence anti-pattern applies: non-catastrophic, gate worked
  correctly, one chapter. Wait for c03 or a subsequent chapter to confirm the pattern before adding
  a rubric REJECT rule. A premature REJECT rule against character-scope vibes could block legitimate
  irony-layer vibes at episode scope targeting Wren (episode-scope vibes:12/13 were ACCEPT and
  correctly deployed). The distinction between character-scope and episode-scope in the rubric needs
  to be precise, and the b01c02 case is still the only instance.

  Issue 3: The and-facets command body specifies a cycle cap of 3; using cycle 1 and proceeding
  after fixer resolution is within spec. "Pragmatic-accept" here means fixer DELETEs addressed
  all REVISE items (2 keyword swaps + 2 DELETEs), no new HARDs were introduced, and the operator
  chose not to re-fire Phase 5b cycle 2 because the deletion path resolved the callouts definitively.
  This is a valid path — cycle 2 is not mandatory when the fixer's resolution mode is DELETE
  (the deleted entries cannot produce REVISE callouts from the audience again). No structural
  gate was bypassed; the auditor's Phase 5 scan ran on the post-fixer graph. Not a process gap.

trade-off:
  Issue 1: Proposing at recurrence_count=1. Justified because this is a gate-scope specification
  gap with a precise, S-cost fix; the gate's stated scope explicitly says "every text field"
  and the implementation does not match. The risk of not proposing: another chapter's vibes token
  arrays contain fence hits that the auditor passes as CLEAN and the audience must catch. That
  would mean HARD-class CONSTRAINT violations are structurally caught only at Phase 5b (the
  subjective gate) rather than Phase 5 (the mechanical gate) — a durable inversion of the
  gate hierarchy for this check class.
  Issue 2 and 3: Not proposing. The cost of a premature REJECT rule (issue 2) or a cycle
  mandate (issue 3) exceeds the cost of waiting for recurrence.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0019 | 2026-05-26 | SLOW (process-critic)

question: b01c02 postop-convergence:divergent — Fork A substance DELIVERED, Forks B+C converge on compound-noun saturation tic. Does the process need a proposal? Options: (a) Phase 7 Q9 tightening, (b) /and-stitch Phase 1 scene-window variance discipline, (c) /and-write Phase 6 AP-SCAN for compound-noun density in bone SVOs, (d) wait for c03+c04 recurrence.
context: Second occurrence of compound-noun density pattern. Occurrence 1: pl-2026-05-25-013 from b01c01 cold-read ("prose dense with hyphen-compound nouns"). Occurrence 2: b01c02 postop Forks B+C ("compound-hyphenated nouns at five per paragraph numb the ear"; "threshold-stones approaching term-of-art saturation"). Fork A (substance-delivery): DELIVERED clean across all 12 dimensions; c02->c03 setup CLEAN. The depth-pass produced the density problem — bones authored to ground substance also introduced compound-noun saturation the stitcher faithfully rendered. No downstream gate can thin bone-content compound nouns: Q9 explicitly emits FAULT-BONE-AUDIT-MISS on bone-content compounds and renders as-is to preserve bone-faithfulness. The existing `register-as-mannerism` SIGNAL in Phase 6 covers verb-object pair recurrence (≥3 occurrences) — compound-noun cluster density is an analog that falls in the same table.
options: (a) Phase 7 Q9 — structurally ineffective (bone-faithfulness fence); (b) /and-stitch Phase 1 variance — wrong layer (rendering choice, not authoring gap); (c) /and-write Phase 1 + Phase 6 — correct root; (d) wait — overcautious given recurrence count 2 across independent chapters

decision: PROCESS-CHANGE-PROPOSED PROP-0007
basis: recurrence-count-2 (Rule 11 recurrence threshold cleared — pl-2026-05-25-013 c01 + b01c02 postop c02 are independent chapters) + gate-absence discriminator (/and-write Phase 1 has no compound-noun economy guidance; Phase 6 has no compound-noun density AP-SCAN; modify correct change_type because the existing `register-as-mannerism` SIGNAL is the structural analog) + methodology:3a (reversibility — SIGNAL disposition; HARD only on second project-level occurrence) + methodology:3c (blast radius — two sentences in one command body; S cost)
rationale: The compound-noun saturation failure has a precise causal chain: screen-writer authors compound-noun SVOs at Phase 1 → stitcher renders them verbatim under bone-faithfulness fence → Q9 cannot touch them. No downstream gate is structurally capable of fixing this without violating bone-faithfulness. The correct gates are Phase 1 (authoring guidance) and Phase 6 (AP-SCAN). Options (a) and (b) are ruled out on structural grounds, not just preference. Option (d) would be correct at recurrence_count=1; at recurrence_count=2 across independent chapters the first-occurrence hold is released per Rule 11. The proposed SIGNAL threshold (≥4 distinct compound nouns in a 5-bone window) is calibrated to Fork B's specific language ("five per paragraph") and matches the existing pattern for `register-as-mannerism`. Cost S; SIGNAL disposition is conservative and reversible.
trade-off: Proposing at recurrence_count=2 rather than waiting for c03/c04 confirmation. Accepted: Rule 11 explicitly names recurrence_count≥2 across independent invocations as the proposal threshold; the evidence is reader-convergent, not a single taste flag; the proposed change is S-cost and SIGNAL-disposition with adjustment path if thresholds prove wrong.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0020 | 2026-05-26 | SLOW

question: Which path after wiring voice-exemplar to stitcher — (1) scoped renderer experiment only (~5 dispatches), (2) full /and-stitch re-run + variant experiment (~35+ dispatches), or (3) full /and-stitch re-run only?
context: active-project/voice-exemplar.md just provisioned from Robinson library exemplar, closing the PROP-0003-A missing wiring step. c02 already shipped as terminal deliverable under polish-deferred. User asked: "wire the stitcher correctly and give another go on stitcher" + "put a score to the output similar to how we tested different renderings" + "experiment to try different exemplars from different personas." Reference scoring methodology: impersonator-experiment-2026-05-26 cold-read-report.md shape (~3 renders + 1 ranking dispatch). Full /and-stitch is ~30+ dispatches; scoped experiment is ~5 dispatches.
options: (1) scoped renderer experiment only — no draft overwrite, answers both sub-questions cheaply; (2) full /and-stitch re-run + variant experiment — overwrites terminal draft, heavy spend, commits to a voice before experiment; (3) full /and-stitch re-run only, no variant experiment.

decision: Option 1 — scoped renderer experiment only. ~5 dispatches, no draft overwrite.
basis: goal:2 (cost discipline) + methodology:3a (reversibility — c02 draft already shipped terminal; re-stitching overwrites it before the best voice is identified) + methodology:3d (optionality — experiment first preserves the option to re-stitch with the winning voice after)
rationale: The user's expanded ask ("experiment to try different exemplars") signals that voice selection is the current decision, not final production re-render. Option 2 commits 30+ dispatches to a voice choice not yet made — it would re-derive the terminal draft under Robinson prime before knowing whether Robinson beats alternatives. Option 1 answers both sub-questions (does PROP-0003-A wiring help? which exemplar register wins?) cheaply, using the same experiment shape as the prior impersonator study, and leaves option 2 available once the winner is identified. Option 3 would answer neither question cheaply (heavy spend for one voice without comparison). V0 baseline / V1 Robinson (now wired) / V2 setting-adjacent / V3 contrast voice on one representative c02 scene is the correct experiment frame.
trade-off: draft/b01-c02.md does not get updated by this path — that's the explicit trade; it stays as the prior-revision draft until the variant winner is determined and a re-stitch is warranted. Git history preserves prior drafts regardless.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0021 | 2026-05-26 | SLOW (process-critic)

question: Process-critic dispatch — Phase 9 cold-read FAIL on b01-c02 re-stitch (voice-exemplar-wired run). Two candidate process changes: (a) modify Phase 9 cold-read protocol to account for non-opening chapter context; (b) add exemplar-tournament criteria check (continue-rate) before re-stitch. Should admin propose a process change?
context: Second stitch of b01-c02. Bones unchanged. Only delta: per-chapter voice-exemplar override (Septon-Halvard cadence productionized from ablation winner). Prior stitch (un-primed) shipped PASS-WITH-CAVEATS. This stitch FAIL'd on CONTINUE=no. Cold reader correctly recovered all central events and identified moral jeopardy; the FAIL is reading-experience opacity. Two mutually exclusive interpretations: (1) voice-prime regression — interior/ritual register of Septon-Halvard compounded the chapter's world-grounding deficit for a cold reader; (2) protocol limit — no-c01-context cold-read unfairly penalizes a non-opening chapter whose confusions would be resolved by c01 in normal reading. Cold-read report explicitly flags both interpretations and recommends against auto-routing to /and-write revise. recurrence_count = 1 (first cold-read FAIL on a chapter where bones were sound).
options: (a) PROCESS-CHANGE-PROPOSED on Phase 9 cold-read protocol — add non-opening chapter context assumption; (b) PROCESS-CHANGE-PROPOSED on voice-exemplar selection — add continue-rate as a criterion alongside register-fit; (c) OK — first occurrence, non-catastrophic, wait for recurrence

decision: OK — no process change proposed.
basis: methodology:process-critic-recurrence-discipline (first occurrence of a non-catastrophic SIGNAL → return OK, wait) + content-vs-process discrimination
rationale: Both candidate process questions (protocol scope for non-opening chapters; exemplar selection criteria) are legitimate candidate process changes. But neither reaches the threshold for a first-occurrence proposal. The failure is non-catastrophic: bones are sound, prior stitch passed, chapter can be re-stitched trivially with a different voice prime, no irreversible state, no multi-chapter blast radius. Recurrence discipline is clear — wait for recurrence. Proposal on a single instance would prematurely promote what may be an operator choice (wrong exemplar selected for this chapter) into a spec change. Additionally: interpretation 1 (voice-prime regression) is likely the primary driver given the PASS-WITH-CAVEATS under no prime. If so, the fix is to revert the per-chapter override — a content/stitch-config decision, not a process failure. Interpretation 2 (protocol limit) is real but the protocol change it implies (context-aware cold-read for non-opening chapters) would make Phase 9 a different gate, not a stricter one; that is a principal-level architectural decision best deferred until the pattern recurs. If a second chapter FAILs cold-read under similar circumstances (bones sound, prior-chapter context explains reader confusion), admin will propose the non-opening chapter qualification at that point.
trade-off: Not proposing means the non-opening-chapter protocol gap is not formally tracked. Mitigated by: this decision log entry serves as the first-occurrence marker; if recurrence happens the evidence trail is here; PROP candidates are ready to be drafted (both are well-understood process changes that can be authored quickly on second occurrence).

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0015 | 2026-05-26 | SLOW (process-critic amendment)

question: Amend DEC-0013 / PROP-0003: cold-read experiment shows matched exemplar passage (v16) beats persona-description prime (v14), and mismatched exemplar (v17) leaks surface conventions. Asset format must change from persona-card description section to standalone exemplar passage file.
context: 4-variant follow-up experiment. v16 (Robinson-voice exemplar, Westeros-adjacent content) ranked #1; v14 (Robinson persona-description, PROP-0003 format) ranked #2 (46% longer, no coverage gain — bloat + aphorism-creep); v17 (Robinson-voice exemplar, Gilead content — content-mismatched) ranked #3, leaked italic-as-memory surface convention into target prose; v02 (no prime, baseline) ranked #4. Injection point (Phase 0 step 4a) and null-default from PROP-0003 are confirmed correct and survive. Only the asset format changes.
options: n/a — user directive to amend; direction specified. No re-litigation.

decision: PROCESS-CHANGE-PROPOSED PROP-0003-A (amendment of PROP-0003)
basis: user-directive-to-amend + methodology:3c (blast radius — standalone file decouples project-scoped voice from persona-scoped lens; smaller footprint than persona-card section) + cold-read evidence (3 findings: exemplar > description, content-match matters, baseline loses to all primes)
rationale: PROP-0003's asset format was correct in mechanism — Phase 0 injection at step 4a, null-default, renderer-minimal mirror — but wrong in the asset type. A ≤150-word register description causes the renderer to paraphrase the described voice; a prose exemplar passage causes the renderer to instantiate cadence directly. The v17 content-mismatch finding adds a new constraint: exemplar content must be adjacent-to-but-not-from the project; a surface-convention fence at the injection point (explicit prohibition: cadence/structure transfer only, no surface-convention import) is mandatory and closes the v17 leak. The standalone series-level file also correctly scopes voice priming as project/series-bound rather than persona-bound — the persona card carries lens-bias, not project voice. PROP-0003-A supersedes PROP-0003's asset format spec; Phase 0 step 4a wiring, null-default, and renderer-minimal mirror field name (renamed from `voice_prime` to `voice_exemplar_path`) survive.
trade-off: PROP-0003 persona-card `## Voice prime` section is retired in favor of `active-project/voice-exemplar.md`. The new format requires a new authoring step at `/and-series` (optional, flag-gated). This is marginally more infrastructure than a persona-card edit, but the scope separation (project-scoped file vs. persona-scoped card) and the 46% length-discipline advantage of the exemplar format justify it.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0022 | 2026-05-26 | SLOW

question: User ran `/and-stitch b01-c02`. Should the command run a fresh full re-stitch, stop and confirm intent, or run an un-truncated re-stitch (since the prior stitch was budget-truncated)?

context: b01-c02 is already terminal: depth-pass resolved 2026-05-26, Phase 9 returned PASS-WITH-CAVEATS, depth_pass_pending = false, draft files current. One stale-looking field (stitched_stale_since: 2026-05-26T00:00:00Z) appears to be a bookkeeping leftover not cleared at the post-depth-pass re-stitch write — all other freshness indicators disagree. Bones and facets unchanged since the depth-pass stitch. A no-input-delta full re-stitch produces output only via seed variance. However: memory.md line 2440 explicitly notes that the prior stitch ran Phases 2-7 as "truncated under budget-constrained cascade" — a full un-truncated re-stitch would be a meaningful delta (sweeps that were actually skipped would run). Two parking-lot items fire SOFT; neither blocks.

decision: Option 3 — run as a full (non-truncated) re-stitch, surfacing the budget-truncation note as the reason. Do NOT stop to confirm; the user invoked the command and the truncation note is the key fact that makes this a meaningful non-redundant re-run.

basis: methodology:3b (cost) + goals:Goal-2 (cost discipline) — the truncation note changes the calculus; this is not a seed-variance re-run, it is completing skipped phases
rationale: The user's explicit command invocation plus the explicit memory.md truncation note at line 2440 are sufficient signal to proceed. Phases 2-7 (compression, voice transform, local flow + speaker-paragraph breaks, buildup preservation, editorial reflection) were skipped under the cascade budget; running them now is a meaningful completion pass, not redundant work. Option 2 (stop and confirm) would be correct only if the re-run were purely redundant — it is not. The stale stitched_stale_since field is consistent with the truncation interpretation (incomplete phases = stitch not fully clean). The command body should surface the truncation note in its Phase 0 print block so the record is clear.
trade-off: If the truncation note is wrong and Phases 2-7 did actually run fully, this becomes a seed-variance-only re-stitch — spend is wasted but there are no irreversible side effects (prior draft is overwritten but not unrecoverable). The truncation note + stale field together make the "phases were skipped" interpretation the correct prior.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0023 | 2026-05-26 | SLOW (reverses DEC-0022)

question: New render-log evidence shows render-log-b01-c02.md (the current one) is the voice-exemplar-wired re-stitch that ran AFTER the budget-truncated pass memory.md line 2440 refers to. All phases completed. The basis for DEC-0022 (truncation note → meaningful completion pass) is factually wrong. Should the command proceed (Option 1: honor user's invocation as explicit re-run-for-variance), pull back and surface to user (Option 2), or clear the stale stitched_stale_since field only and not re-stitch (Option 3)?

context: render-log-b01-c02.md records Phase 1 (3 scene-window forks, 47/47 bones rendered), Phases 2-6 (walked explicitly), Phase 7 (76-sentence sweep, 21 moves applied), Phase 8 (finalize + RECONCILE, 47 bones / 63 facets / 0 unrendered). Three render-log files exist for c02 (prior, revise, current) — the current one IS the fully-completed voice-exemplar-wired re-stitch, not the budget-truncated one. Memory.md line 2440 is stale (true of an older pass; not the current draft on disk). stitched_stale_since was never cleared after that re-stitch finalized. User input was "/and-stitch b01-c02:" with a trailing colon (typo-pattern). Cost of Option 1 with corrected picture: ~10 forks for seed-variance delta only on unchanged inputs.

options:
  Option 1: Proceed per DEC-0022 — treat invocation as explicit re-run-for-variance request
  Option 2 (default): Pull back — flag to user that c02 is already fully stitched, ask if they meant something else (e.g. b01-c03)
  Option 3: Clear stale stitched_stale_since only, surface state summary, do not re-stitch

decision: Option 2 — pull back and surface to user. Do NOT run the re-stitch. Report the corrected state of c02 and ask if the intent was a different chapter (likely b01-c03).

basis: reverses DEC-0022 on new factual evidence + goal:2 (cost discipline — ~10 forks for pure seed variance is not worth running without user intent confirmation) + methodology:3a (reversibility — re-stitching overwrites the current terminal draft; pulling back has zero irreversible cost)

rationale: DEC-0022's single load-bearing basis was the truncation note at memory.md line 2440. The render-log evidence conclusively shows that note describes an earlier pass, not the current draft. With that basis removed, the corrected picture is: all phases ran, RECONCILE balanced, Chapter 2 is fresh-terminal. Running again is pure seed variance (~10 forks, draft overwrite, no new content). The trailing-colon typo pattern on the user's invocation reinforces that this may not be a deliberate re-run request. Option 2 costs zero model spend and surfaces the correct chapter state so the user can redirect to the actual next step (likely b01-c03, which has scene-*.draft.md files but no annotated draft and is plausibly the real target).

trade-off: If the user did intend a variance re-run, Option 2 asks an extra confirmation question. That interruption cost is trivially lower than ~10 wasted forks plus overwriting a fresh-terminal draft the user may have wanted to preserve.

reverses: DEC-0022
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0025 | 2026-05-27 | FAST

question: User typed "do chapter 3" on branch `claude/chapter-3-eRDko`. C03 shipped 2026-05-26 under cascade-budget compression with several audit/review phases skipped. Deferred items: `/and-review bones b01c03`, `/and-facets b01-c03` Phase 5b audience-gate, `/and-postop b01c02 in c03 context`, and `/and-substance chapter b01c03` Phase 5 3-fork review. Four interpretations offered: (1) close out deferred audits, (2) re-cascade c03 from scratch, (3) advance to c04, (4) show draft.
context: bone-gate verdict PASS-PRAGMATIC; Phase 9 cold-read PASSED; branch name is chapter-3 (argues against advancing to c04); recent work pattern is quality-iteration on already-shipped chapters (c02 tournament + cherry-pick); deferred items are explicitly named in memory.md.
options:
  (1) Close out deferred audits — fire /and-review bones b01c03 + /and-postop; light cost; no rewrite unless gate fails
  (2) Re-cascade c03 from scratch — heavier; potentially rewrites shipped draft
  (3) Advance to c04 — interpret as "next chapter" directive
  (4) Show draft only

decision: Option 1 — close out the deferred audits on c03.
basis: goal:1 (pipeline correctness — skipped gates are open debt; closing them is the minimal path to a fully-compliant c03) + methodology:3b (cost — option 1 is cheapest; option 2 is a full cascade spend; option 3 contradicts the branch name) + methodology:3a (reversibility — audits-first preserves the option to re-cascade if they surface a FAIL; re-cascading first discards the shipped draft unnecessarily)
rationale: The branch name `chapter-3` and the explicit memory.md deferred-item list both point to unfinished business on c03, not a forward move. Closing the skipped gates (bones review + postop) is the correct minimal action: if they PASS, c03 is clean and the next step is clear; if they FAIL, the re-cascade (option 2) is warranted by evidence rather than speculation. Running the skipped gates is also a goal:1 obligation — the chain has declared mandatory reviews that were budget-skipped, not waived.
trade-off: If the user intended a full re-cascade or c04 advance, this answer adds one lightweight audit pass before the next step. That cost is trivially lower than a full cascade run on potentially-sound bones.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0024 | 2026-05-26 | SLOW (process-critic)

question: Third Phase 9 cold-read FAIL on b01-c02 (multi-arm tournament + full Phase 7 sweep). All three stitches returned CONTINUE=no. Does the recurring CONTINUE=no constitute a process signal beyond PROP-0007 — specifically: (a) a modify to Phase 9 cold-read protocol for non-opening chapters / dormancy-prefigure dramatic shapes, or (b) a structural issue with the and-substance chapter contract for b01c02?
context: Three stitch passes, three CONTINUE=no verdicts: (1) 2026-05-25 original budget-truncated PASS-WITH-CAVEATS soft-override; (2) 2026-05-26 single-arm voice-exemplar-wired PASS-WITH-CAVEATS soft-override; (3) 2026-05-26 multi-arm tournament spec-strict FAIL (not soft-overridden). DEC-0021 returned OK on pass 2 (first occurrence, non-catastrophic, likely voice-prime regression driver). New evidence since DEC-0021: (a) multi-arm + Phase 1.5 taste rubric both passed per-scene criteria — the gate's own prose-quality instrument found improvement; (b) cold-reader on pass 3 is harsher ("ritualized abstraction did not give me a scene I could see"); (c) c03 Phase 9 cold-read returned PASS (CONTINUE=yes, jeopardy grounded) on a different dramatic shape (hinge). The b01c02 dormancy-prefigure dramatic_shape deliberately withholds named jeopardy, named antagonist offer, and prohibition-as-stakes to c03 per substance contract. Memory.md line 2492 explicitly annotates: "Chapter-internal failure modes (no jeopardy, no payoff, would-not-continue) are the c02 dramatic-shape, not a stitch defect." Phase 9 Step 2 exempts `frame-coda` chapters from the jeopardy FAIL condition; no exemption exists for `rising` with dormancy-prefigure contracts. PROP-0007 (compound-noun economy) is open and covers a distinct surface concern. No prior rejected or deferred proposal targets Phase 9 protocol or and-substance chapter contract for this failure class.
options: n/a (process-critic mode: OK / OK-PRIOR-REJECTION / PROCESS-CHANGE-PROPOSED / ESCALATE)

decision: OK — no new proposal warranted.
basis: methodology:process-critic-recurrence-discipline (same-chapter replication ≠ cross-chapter recurrence; recurrence_count=1 for the pattern "Phase 9 CONTINUE=no on dormancy-prefigure chapter despite sound bones") + content-vs-process discrimination (the gate miss is design-intended collision, not a gate calibration gap that would benefit from a new exemption at this data count) + c03-counter-evidence (the pattern did not recur on the next chapter, which has different dramatic_shape and passed cleanly)
rationale: |
  Four reasons this finding does not warrant a proposal now.

  1. RECURRENCE IS WITHIN-CHAPTER. All three CONTINUE=no fires are on b01-c02. DEC-0012 and DEC-0021
     both apply the schema's discriminator: same-chapter replication is not cross-chapter recurrence.
     A second chapter with a documented dormancy-prefigure contract that also FAILs cold-read would be
     the cross-chapter recurrence that warrants a modify proposal against Phase 9 Step 2. b01-c02 is
     still the only instance of the pattern.

  2. C03 COUNTER-EVIDENCE. C03 Phase 9 cold-read returned PASS (CONTINUE=yes, jeopardy grounded)
     on the same pipeline, same chain, different dramatic_shape (hinge vs. dormancy-prefigure). This
     directly refutes the hypothesis that the gate is miscalibrated chain-wide. The failure is
     chapter-specific. Memory.md note at line 2492 correctly diagnosed this at the first cold-read:
     "Chapter-internal failure modes are the c02 dramatic-shape, not a stitch defect." Three cold-reads
     and one counter-case later, that diagnosis holds.

  3. PROPOSED CHANGE IS UNDER-CONSTRAINED AT N=1. The candidate process change — adding a
     dormancy-prefigure exemption or a non-opening-chapter context assumption to Phase 9 Step 2 —
     cannot be written precisely from a single data point without risking false-negative holes.
     The exemption must discriminate "designed deferred stakes" from "actually under-delivering on
     jeopardy," and that discriminator requires seeing what a false-positive exemption would look like.
     A second dormancy-prefigure chapter is the minimum evidence for precise specification. Without it,
     any exemption rule is speculative and could degrade gate integrity for future chapters.

  4. THE GATE WORKED AS A SIGNAL, NOT AS A WRONG BLOCK. The spec-strict FAIL is technically correct
     under Step 2 (CONTINUE=no + jeopardy=no on a non-frame-coda chapter). The operators correctly
     diagnosed the design-intent collision every time and soft-overrode or accepted the FAIL as
     appropriate. The gate did not block a chapter that should have shipped and did not pass a chapter
     that should have been held. The absence of a dormancy-prefigure exemption produced correct
     operator behavior (diagnose the shape; soft-override; advance). This is not a process failure;
     it is the Phase 9 gate correctly surfacing a tension that the operator must resolve, which they did.

  PROP-0007 (compound-noun economy at /and-write Phase 1 + Phase 6) remains the only open
  process change from c02's failure evidence. It targets the prose-surface tic that postop Forks B+C
  independently identified — a distinct finding from the cold-read jeopardy/continue failure class.

  DEC-0021 is the first-occurrence marker. This decision extends the hold to the second presentation.
  If a future chapter with a documented dormancy-prefigure or deferred-stakes dramatic_shape FAILs
  Phase 9 cold-read despite sound bones, that cross-chapter recurrence is the trigger for a modify
  proposal against Phase 9 Step 2 targeting the dormancy-shape exemption.
trade-off: Not tracking the candidate proposal in process-proposals.md as a deferred entry. Mitigated
  by: the decision log entry (DEC-0021 + this entry DEC-0024) serves as the first+second occurrence
  marker; the change_type:modify against Phase 9 Step 2 can be drafted quickly on second cross-chapter
  occurrence; the candidate spec language (dormancy-prefigure exemption + context-aware CONTINUE
  qualification for non-opening chapters) is well-understood from these two dispatches and does not
  need to be formally deferred to avoid losing the thread.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0026 | 2026-05-27 | FAST

question: DEC-0025 follow-up: both c03 deferred audits are now resolved (/and-review bones b01c03 PASS-WITH-NOTES + /and-postop b01c02 already completed 2026-05-26). Three options for next step: (1) declare c03 closed and stop, (2) re-fire postop on c02 with fresh persona (dark-fantasy-reader), (3) run postop on c03 itself.
context: /and-review bones b01c03 returned PASS-WITH-NOTES (0 HARD, 5 SIGNAL, 1 FLAG) today. /and-postop b01c02 in c03 context ran 2026-05-26 with worm-canon-pedant, divergent convergence, compound-noun saturation finding already logged as PROP-0007 / DEC-0019. c03 cold-read Phase 9 PASS (CONTINUE=yes), no depth-pass pending. The bone-review signals are advisory (fixable at bone scope if downstream revise dispatched, but none HARD, nothing blocking).

options:
  (1) Declare c03 closed — both scoped deferred audits resolved; report and stop.
  (2) Re-fire postop b01c02 with fresh persona — adds one reader-eye; finding already logged; diminishing returns.
  (3) Run postop on c03 — not in DEC-0025 scope; c03 has no depth-pass pending; 3 forks on a clean-PASS chapter.

decision: Option 1 — declare c03 closed, report and stop.
basis: goal:2 (cost discipline — options 2+3 are spend against already-logged findings or a chapter with no pending depth-pass) + methodology:3a (reversibility — stopping preserves /and-postop b01c03 as a user-invocable option; running it now without user direction is scope expansion) + methodology:3d (optionality — user retains the option to invoke /and-postop b01c03 explicitly if they want depth-of-quality signal before advancing) + goal:4 anti-pattern (no scope expansion past stated task)
rationale: DEC-0025 scoped exactly two deferred audits. Both are on disk and closed. Option 2 adds a third reader-eye on c02's compound-noun saturation, which is already the primary finding of PROP-0007 and two fork reports — the information return is near-zero. Option 3 would be running postop on a chapter that (a) was not scoped by DEC-0025, (b) has no depth-pass pending, and (c) returned Phase 9 PASS clean. Running it without user direction is the anti-goal "while I was in there, I also..." pattern. The correct stopping point is here.
trade-off: If the user wanted depth-of-quality QA on c03 specifically, they will need to invoke /and-postop b01c03 explicitly. That is a one-line user action. The cost of an unrequested postop run (3 forks + write overhead) is higher than the cost of the user choosing to invoke it if they want it.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0027 | 2026-05-27 | SLOW

question: c04 is next. Cascade (--cascade), serial-stop-at-substance, or cascade-with-no-budget-compression?
context: c04 is the acceptance chapter — heaviest axis-move count in the book (5 axes, total delta +7.5), load-bearing for the series spine. c02 ran cascade-budget, required revise --from-signals + 3 stitch cold-reads to land. c03 ran cascade-budget; deferred /and-review bones found 5 SIGNAL findings the inline synthesis missed. User said "continue" without specifying serial vs. cascade.

options:
  (1) /and-substance chapter b01c04 --cascade — standard forward-motion; trust the chain
  (2) /and-substance chapter b01c04 only — stop at scene chunks; inspect contract before bones; then decide whether to cascade from /and-write forward
  (3) --cascade with no-budget-compression instruction — verbal flag to orchestrator; no command-body enforcement mechanism

decision: Option 2 — fire /and-substance chapter b01c04 only; hold at scene chunks.
basis: goal:1 (pipeline correctness — c04 is the series-spine acceptance chapter; a substance-contract miss here damages load-bearing structure) + goal:2 (cost discipline — cascade on the two prior chapters required significant remediation spend; serial is cheaper in expected-total-spend when the risk of cascade-miss is elevated) + methodology:3a (reversibility — stopping at substance preserves full cascade option; full cascade cannot be undone once bones are authored against a weak contract) + methodology:3d (optionality — serial keeps /and-write cascade entry point open; cascade locks in the contract immediately)
rationale: Option 3 is rejected because "no budget compression" is a verbal instruction with no enforcement mechanism in the command body — the cascade runs agent-to-agent and there is no parameter that hard-gates budget-skip. It is noise over option 2. Options 1 and 3 both replay the pattern that produced under-audited results on c02 and c03. c04's axis density (heaviest of the book) and narrative centrality (acceptance chapter, series-spine) make it the worst possible place to absorb another cascade-miss. Option 2 costs one extra user-attention step (review scene chunks) in exchange for a hard inspection window before bones are committed. The cost of that step is trivially low; the cost of re-running bones on a spine chapter is high.
trade-off: Option 2 requires one more user-facing step (inspect scene chunks + decide whether to cascade from /and-write). Option 1 would be faster in the no-miss case. The expected-miss probability on c04 is higher than on c02/c03 given axis density, so the expected-total-spend favors option 2.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0028 | 2026-05-27 | SLOW (user-proxy)

question: Phase 5 review of c04 scene chunks: 4/5 reviewers ACCEPT; auditor lone FAIL with 2 HARD + 4 SIGNAL. Approve recommended action (override fault-001, fix fault-002 notes, surface SIGNALs 1-4 to /and-write, persist + advance + stop) or push back?

context: |
  fault-001 (POV violation): Auditor flagged all three c04 scene chunks as third-limited in violation
  of cond-taylor-pov-behavior's "first-person throughout" requirement. Card text says "Flag any chapter
  not marked interlude that is not in Taylor's first-person." Critical counter-evidence: c01/c02/c03
  scene chunks in memory.md are all third-limited by established convention; rendered prose at
  draft/b01-c01.md through b01-c03.md is first-person throughout. First-person transformation
  happens at /and-write (named-subject SVO) → /and-stitch (first-person render). Three prior audits
  did not flag this. The card's "for auditor use" clause is ambiguous — it does not specify whether
  "is not in Taylor's first-person" refers to the planning-layer chunk or the rendered prose.

  fault-002 (cl-antag-d03 math): Auditor flagged cl-antag-d03 "completed" claim in s01 notes as
  false. Verified correct: c03 delivered +1.5, c04 delivers +1.0, sum = +2.5 of +4. The "completed"
  note was already in memory.md line 3053 before c04 chunking — inherited from the book-level chapter
  contract authored at /and-substance book b01 (2026-05-24). Real notes error at two locations:
  b01c04 s01 draft note + memory.md line 3053.

  SIGNALs 1-4: Advisory. No blocking. All 4 reviewers' 2 additional soft watches also advisory.

  Principal's recommended action:
    1. Override fault-001 (convention established; prior audits accepted; card text ambiguous)
    2. Fix fault-002 notes at both locations (no prose rewrite)
    3. Surface SIGNALs 1-4 to /and-write as soft watches
    4. Persist chunks to memory.md, advance status to scened, archive draft to _drafts/
    5. Stop (per DEC-0027 review-stop before /and-write)
    + admin process-critic on fault-001 for card-text clarification

decision: APPROVED as stated. Proceed with the recommended action on all five points.

basis: |
  fault-001 OVERRIDE: Convention evidence is dispositive. Three independent chapters authored at the
  same planning layer (c01/c02/c03) are all third-limited in memory.md. Three audits did not flag this.
  Rendered prose for all three is first-person throughout — the chain's interpretation is consistent
  and correct: "first-person" governs rendered prose, not the planning-layer SVO notation. The card's
  ambiguity ("Flag any chapter not marked interlude that is not in Taylor's first-person" without
  specifying the layer) means the auditor is reading literally but not incorrectly — the card's
  language does not exclude the planning layer. This is a card-text failure, not a chain failure.
  Overriding is methodology:3e (convention — do what the codebase already does) + methodology:3a
  (reversibility — chunk redraft for c04 + retroactive for c01-c03 is irreversible high-cost; override
  is low-cost and the interpretation is evidenced). Flagging for process-critic card-text clarification
  closes the audit gap for future chapters.

  fault-002 FIX: Real error, no argument against fixing. Notes-only correction at two locations is
  low-cost, reversible, and preserves the book-level roll-up integrity. The auditor is correct on the
  math. No prose rewrite is needed per auditor, per principal. The error predates c04 (introduced at
  /and-substance book b01 2026-05-24) — the fix is the minimal correction of an inherited stale claim.

  SIGNALs 1-4: Surfacing all four to /and-write is correct. SIGNAL 4 (theme-silence on s03 mechanism
  tag) deserves the same advisory weight as SIGNALs 1-3 — it is a planning-marker that must not
  surface as inner monologue, not a violation yet; the auditor's flag is correctly precautionary.

  Stop after persist + status advance: Consistent with DEC-0027 (review-stop before /and-write).
  No reason to advance further without user direction.

  Admin process-critic on fault-001: Correct triggering condition — card text caused a legitimate
  HARD fault on a correctly-authored artifact. That is a card-text gap, not a chain failure. Admin
  should fire process-critic to propose a card-text clarification scoped to "first-person throughout
  the rendered prose" (not the planning-layer chunk SVO notation). This is a process fix, not an
  override bypass. Change_type: modify. Target: cards/conditions/cond-taylor-pov-behavior.card.md +
  auditor use clause. Cost S.

rationale: |
  The four-ACCEPT / one-FAIL result with the lone-FAIL on a layer-ambiguity point is exactly the
  pattern where override is warranted. The four audience+critic reviewers evaluated scene-level
  substance delivery (SUBSTANCE-FELT 5/5 across all three independent audience readers; dramatist
  confirmed axis aggregates EXACT + handoff mirrors clean). The auditor's two HARDs are:
    - fault-001: a card-text ambiguity applied to an artifact the chain has consistently produced at
      this layer without prior challenge; override is the only reasonable path absent evidence that
      the rendered prose will fail first-person (which it will not — /and-stitch enforces this)
    - fault-002: a real notes error the principal independently verified, with a low-cost no-rewrite
      fix available

  There is no case for a full chunk redraft. The substance delivery is confirmed by three independent
  audience readers (including the hardest technical audience, worm-canon-pedant). A chunk redraft
  would re-author correct substance from scratch, burning significant tokens for zero expected gain,
  to fix a card-text ambiguity that should be resolved in the card, not the chunks.

  The process-critic firing on fault-001 is the correct permanent fix. The override is the correct
  immediate action. They are complementary.

trade-off: |
  The only cost of approving: fault-001 is overridden on a card-text ambiguity without a human
  checkpoint. This is within admin authority — it is a layer-interpretation call backed by three
  chapters of prior convention, not an architectural direction change or irreversible destructive
  operation. Methodology §human-only does not cover "interpret ambiguous card language in light of
  established chain convention." If the principal disagrees with the layer interpretation, the correct
  path is to amend the card to explicitly say "planning chunks must also be first-person" — at which
  point future audits would block and the chain would need to change. That is a reversible edit.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0029 | 2026-05-27 | SLOW (process-critic)

question: Post-DEC-0028 tail obligation — process-critic dispatch on fault-001 HARD at /and-substance b01c04 Phase 5. Should admin propose a process change to `cards/conditions/cond-taylor-pov-behavior.card.md` to disambiguate which production layer "first-person throughout" applies to?
context: |
  Auditor fired fault-001 HARD (POV violation: scene chunks written in third-limited). Finding is a
  confirmed false positive per DEC-0028 — c01/c02/c03 all use third-limited chunks; rendered drafts
  are first-person throughout; three prior Phase 5 auditors did not fire on this. The chain's operating
  convention is clear: "first-person" governs rendered prose (the /and-stitch output); planning chunks
  and bones use third-person-named-subject SVO by pipeline design. The card's auditor-use clause
  ("Flag any chapter not marked interlude that is not in Taylor's first-person") does not qualify which
  layer, making a literal reading of the text produce a false-positive HARD on every correctly-authored
  substance chapter pass. trigger.source_report: active-project/staff/reviews/auditor-b01c04-substance-2026-05-27.md.
  gate_path: cards/conditions/cond-taylor-pov-behavior.card.md. Follows: DEC-0028.
options: |
  (a) PROCESS-CHANGE-PROPOSED — modify the card's auditor-use clause and POV Scope section to
      qualify the layer the rule applies to; cost S; guaranteed future-recurrence-prevention.
  (b) OK — first occurrence; but this is a HARD false positive that will structurally recur on
      every future chapter's Phase 5 pass, not a probabilistic recurrence pattern.
  (c) ESCALATE — ask principal to decide whether the planning layer should also be first-person.

decision: PROCESS-CHANGE-PROPOSED PROP-0008
basis: |
  gate-false-positive-specification-gap (the card's auditor-use clause does not name which
  production layer the first-person requirement governs; the false-positive HARD on correctly-
  authored chunks is a criterion-text gap, not a calibration or taste issue) + recurrence-
  is-guaranteed (every future /and-substance chapter Phase 5 will fire the same HARD on
  identically-authored chunks absent card clarification — not probabilistic, structural) +
  methodology:3a (S-cost card edit is reversible; standing false-positive block on future
  chapters is not) + methodology:3b (one S-cost edit prevents per-chapter override overhead
  indefinitely) + DEC-0028 explicit authorization ("Flagging for process-critic card-text
  clarification closes the audit gap for future chapters")
rationale: |
  The anti-pattern rule ("do not propose on first occurrence of a non-catastrophic SIGNAL")
  targets taste-flag promotion to mechanical checks. It does not cover false-positive HARDs
  from specification gaps. The distinction matters: a taste-flag may or may not recur; this
  false-positive HARD will recur with certainty on every future /and-substance chapter Phase 5
  invocation, because the card text is unchanged and the chain's convention (third-limited chunks
  → first-person rendered prose) is unchanged. Three prior Phase 5 passes did not fire on this —
  but c04 being the first time the auditor applied the literal clause to chunks means c05/c06/c07
  will face the same fire without card clarification. The recurrence_count is 1 by the count of
  times the HARD was fired, but is effectively N (number of remaining chapters) by the structural
  analysis.

  The proposed change is minimal and precise: add a "Layer scope" paragraph to §POV Scope naming
  which layer the rule governs, and qualify the auditor-use clause to target the rendered draft
  specifically. Neither change relaxes the POV rule — first-person throughout the rendered draft
  remains the hard contract. The change adds specificity that was absent.

  Option (c) ESCALATE is not warranted. DEC-0028 has already resolved the substantive question
  (chain convention is correct; card needs to reflect it). The proposed diff follows directly from
  DEC-0028's reasoning and is within admin's authority to propose.
trade-off: |
  Proposing at recurrence_count=1. The only cost is the PROP-0008 log entry itself plus the
  principal's triage time. Against: per-chapter false-positive HARD + override + process-critic
  dispatch overhead on every remaining chapter of the project if the card is not fixed. The
  asymmetry strongly favors proposing.

follows: DEC-0028
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0030 | 2026-05-27 | SLOW

question: /and-write b01c04 Phase 2 returned 45 HARD findings (33 FAULT-FORM-MODIFIER + 12 FAULT-BONE-DELTA-MALFORMED) on 38 bones. Route (1) Phase 1 redo with corrective brief + c02-reference, (2) fixer mass-pass on all 45 findings, or (3) escalate to human? And: file a process-change proposal noting c03 as a contamination source for future bones SVO-form exemplars?
context: |
  45 HARD faults on 38 bones — essentially every bone is non-compliant. Root causes:
  (a) 33 FAULT-FORM-MODIFIER: prepositional phrases of place/direction/time/instrument/
      accompaniment in SVO text, banned per schemas/bones.schema.md line 107. Schema is explicit.
  (b) 12 FAULT-BONE-DELTA-MALFORMED: 11 bones use magnitude 0.5 below the 1.0 bone.delta_per_axis
      floor + 1 dialogue-anchor bone s01n10 with empty axis_moves.
  Both are systematic single-root-cause failures — screen-writer applied a "minimal locative license"
  that does not exist in the schema and used 0.5-magnitude splits instead of 1.0+ magnitudes.
  Contamination source: c03 bones were provided as a cadence reference; c03 ran under cascade-budget
  and was never audited at Phase 2 for SVO-form, so c03's PP-heavy, 0.5-magnitude bones taught the
  wrong pattern. c02 revised bones (47 bones, post-fixer, Phase 2 clean) are the only fully-audited
  SVO-form reference in the project.
  Fixer-independence problem: consolidating 0.5+0.5 pairs into 1.0 bones means deleting bones →
  renumbering → FAULT-FORM edits on deleted bones become moot. Fixes are not independent operations.
  Projected post-redo bone count: ~28-32 (vs 38 now) as pair-splits collapse to singles.
options: |
  (1) Phase 1 redo — re-dispatch screen-writer with corrective brief: no PPs of
      place/direction/time/instrument/accompaniment anywhere in SVO text; magnitude floor 1.0 per
      axis_move; consolidate pair-split deltas into single bones; reference c02 bones (NOT c03)
      as the canonical SVO-form model.
  (2) Fixer mass-pass — route all 45 findings to fixer sequentially; likely produces malformed
      output due to inter-dependent bone-deletion/renumbering conflicts; may require second pass.
  (3) Escalate to human — bring back to the principal for a real decision.

decision: Option 1 — Phase 1 redo with corrective brief + c02-reference. Do not route to fixer.
basis: |
  goal:1 (pipeline correctness — 45 HARD findings on 38 bones is a systematic authoring failure;
  the schema is unambiguous; fixer minimum-change is incoherent when fixes are inter-dependent and
  the root cause is a single authoring error) + goal:2 (cost discipline — expected total cost of
  option 2 exceeds option 1 due to cascading conflicts) + goal:4 (lean architecture — fixer mass-pass
  on non-independent faults is a half-finished implementation anti-pattern) + methodology:3a
  (reversibility — Phase 1 redo is a clean reauthoring; fixer mass-pass on inter-dependent faults
  risks a worse malformed output that also requires redo) + methodology:3b (cost — redo now < fixer
  mass-pass + likely second pass or redo anyway) + methodology:3c (blast radius — fixer applied to
  45 inter-dependent faults has unpredictable blast; redo is a clean slate with defined scope)
rationale: |
  The spec's "fixer with minimum-change" routing assumes the faults are independent correctable
  items — individual bones that can each be minimally fixed without affecting others. That assumption
  breaks down when the root cause is a systematic authoring departure and the fixes are structurally
  coupled (bone deletion changes numbering; FAULT-FORM edits on deleted bones become moot). On 45
  faults across 38 bones, essentially every bone requires changes, and some changes (pair-split
  consolidation) cascade through the bone-ID space.

  The corrective brief for Phase 1 redo is specific and prescriptive: no PPs of any banned class
  in SVO text (list the banned PP types explicitly from schema line 107); magnitude floor 1.0
  per axis_move (consolidate 0.5+0.5 pairs into single 1.0 bones rather than splitting); empty
  axis_moves is a HARD on dialogue-anchor bones (address s01n10 pattern explicitly); reference
  c02 revised bones as the canonical SVO-form and delta-magnitude model, NOT c03.

  Option 3 (escalate) is not warranted. Goals + methodology decide this clearly. The principal
  is not needed for a routing decision between two technical execution paths when one is
  structurally incoherent (fixer on inter-dependent faults) and the other is the clean canonical
  reauthoring path.

  c03 contamination follow-on: Yes, a process-change marker is appropriate. The screen-writer
  correctly referenced project bones as a cadence model but the wrong bones were loaded (c03,
  unaudited for SVO-form) rather than the correct ones (c02 revised, fully audited). This is a
  /and-write Phase 1 dispatch gap: the corrective brief should explicitly name c02 as the
  reference and explicitly warn that cascade-budget bones from c03 are not canonical for
  SVO-form or delta-magnitude discipline. A process-critic dispatch is appropriate after Phase 1
  redo + Phase 2 re-audit confirm whether the corrective brief prevents recurrence — if Phase 2
  clears, that confirms the fix; if it FAILs again, a structural PROP is warranted. For now,
  the corrective brief IS the fix; the contamination gap will be captured as a parking-lot item
  targeting /and-write (for the chain to note that c03 should not be referenced as an SVO-form
  model) rather than a formal process proposal at this stage (single occurrence, fix already
  applied in the brief, outcome TBD).
trade-off: |
  Option 2 is cheaper per-dispatch-overhead in the no-conflict case, but the no-conflict case
  does not apply here — bone deletion + renumbering cascades make a clean 45-edit sequential pass
  structurally impossible. The expected-total-spend for option 2 (fixer mass-pass + conflict
  resolution + likely redo) exceeds option 1 (single Phase 1 redo with corrective brief).
  Option 3 wastes a human round-trip on a question that goals + methodology resolve clearly.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0031 | 2026-05-27 | SLOW (process-critic)

question: Post-/and-write b01c04 Phase 6.5 process-critic dispatch. Four patterns surfaced in the bone-gate PASS report (after 2 internal HARD-resolution cycles). Which warrant process-change proposals?
context: |
  /and-write b01c04 ran two internal HARD-resolution cycles before reaching PASS:
  Cycle 1 — Phase 1 redo (45 HARDs: 33 FAULT-FORM-MODIFIER + 12 FAULT-BONE-DELTA-MALFORMED);
    root cause: c03 cascade-budget contamination; fix: Phase 1 redo with c02-reference per DEC-0030.
  Cycle 2 — Additive cycle (5 HARD HELD-AXIS-NOT-WITNESSED); fix: 5 dedicated held bones added.
  Final PASS verdict: 0 HARD, 3 SIGNAL (all ACCEPTED).
  Patterns named by the dispatch: (1) c03 contamination class, (2) magnitude-floor vs. chapter-contract
  design tension, (3) margit copy-paste from unfixed source, (4) held-axis witnessing brief gap.
  Gate: .claude/commands/and-write.md#phase-6.
options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0009 + PROP-0010 + PROP-0011; OK on pattern 3 (margit copy-paste).

basis: |
  Pattern 1 (c03 contamination → PROP-0009): DEC-0030 deferred the formal proposal "pending
  outcome TBD." Phase 1 redo succeeded (0 FAULT-FORM confirmed by bone-gate redo report).
  Outcome confirmed; proposal ready. Change_type: modify to Phase 1 dispatch brief, adding
  cadence-reference guidance (prefer last fully-audited chapter; cascade-budget chapters are
  not valid references). S-cost. Recurrence = 1 but DEC-0030 explicitly set this dispatch
  as the post-outcome trigger.

  Pattern 2 (magnitude-floor vs. contract design → PROP-0010): Gate absence at /and-substance
  chapter — no existing phase validates per-scene target_delta_magnitude against the bone floor
  before /and-write is invoked. A pre-flight WARNING at chapter-substance persisting time catches
  the design-time mismatch before bones are authored. Change_type: add. S-cost. Recurrence = 1
  but failure is deterministic on any chapter with fractional axis targets split across scenes.

  Pattern 3 (margit copy-paste from unfixed source → OK): First occurrence, SOFT finding. Margit
  imported pre-fix Oswyn characterization because the card was authored before memory was corrected.
  Content/timing failure, not a gate absence. Candidate fix (margit always re-reads source memory)
  needs recurrence before sizing. Standard first-occurrence hold applies.

  Pattern 4 (held-axis witnessing brief gap → PROP-0011): Phase 1 spec states the requirement but
  embeds it in a shape-description paragraph, not as a numbered completion-gate step. Screen-writer
  missed it not because the rule doesn't exist but because it's not actionable in the task list.
  Adding step 4a (completion gate: verify bone coverage for every axes_held[] entry before exiting
  Phase 1) operationalizes an existing rule. Change_type: modify. S-cost. Recurrence = 1 but
  failure mode is deterministic on any screen-writer completing moving/chatter bones first.

rationale: |
  Three of the four patterns pass the process-failure discrimination test:
  - No gate exists at Phase 1 dispatch for cadence-reference vetting (PROP-0009) — change_type: modify.
  - No gate exists at /and-substance chapter for magnitude-floor pre-flight (PROP-0010) — change_type: add.
  - Existing Phase 1 brief states the held-axis rule but not as a completion-gate step (PROP-0011)
    — change_type: modify to brief, not to Phase 6 gate (which fires correctly).
  - Pattern 3: no structural gate gap; timing/ordering issue; first-occurrence hold → OK.
  All three proposals are S-cost, single-file. Methodology 3b+3c both support proposing.

trade-off: |
  Proposing three proposals at recurrence_count=1. Anti-pattern ("do not propose at first occurrence")
  targets taste-flag promotion and ambiguous failure modes. All three gaps are deterministic-structural:
  cadence-reference guidance, magnitude-floor pre-flight, held-axis checklist — each can be written
  precisely from a single data point. Cost of deferring: gaps remain open for every future chapter.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0032 | 2026-05-27 | SLOW (process-critic)

question: Post-/and-review bones b01c04 Phase 4.5 process-critic dispatch. Three patterns surfaced from the FAIL → inline-fix → PASS-WITH-NOTES flow. Which warrant process-change proposals?
context: |
  /and-review bones b01c04 (mandatory URI-WRITE-BONES-REVIEW-GATE) found 1 HARD (fault-001:
  FAULT-DIALOGUE-CARD-VIOLATION — Jarvis @9 entry 8 contained "acceptable," a multi-syllable
  Latinate term explicitly out-of-register per cards/dialects/westeros-smallfolk.card.md). The
  inline /and-write Phase 6 dialogue-card-compliance gate missed it because the dialogue-writer
  (Phase 1.5) invoked seed-fidelity self-license against the word (chunk seed text at /and-substance
  chapter Phase 2 used "acceptable" in framing what Jarvis would say), and the Phase 6 gate accepted
  that self-declared license.

  Contamination chain: (1) screen-writer at /and-substance chapter authored "those terms are
  acceptable to the person he represents" in chunk seed framing → (2) dialogue-writer at Phase 1.5
  saw the word, recognized card pressure, but retained for seed-fidelity → (3) Phase 6 gate
  accepted the self-license → (4) /and-review bones caught it; inline fix applied (Anglo-Saxon
  "takes" replacing "acceptable").

  Auditor also mislabeled "PASS-WITH-NOTES — 1 HARD" (self-contradictory per spec; corrected in
  addendum to FAIL at review-time). The mandatory-gate value (Pattern C) confirmed as positive
  evidence — the independent post-hoc review caught what the inline gate missed.

  three_patterns:
    A: chunk-seed vocabulary contaminating dialogue (seed-fidelity self-license against card fence)
    B: auditor verdict-label mismatch (PASS-WITH-NOTES + 1 HARD, contradictory per spec)
    C: mandatory-gate value confirmed (positive evidence — gate earned its cost)

options: n/a (process-critic mode)

decision: OK on all three patterns — no PROCESS-CHANGE-PROPOSED at this time.

basis: |
  Pattern A — OK, first-occurrence hold:
    Recurrence_count = 1, non-catastrophic (inline fix applied, pipeline unblocked). The failure
    mode is two-step and probabilistic: requires (a) screen-writer using card-adjacent vocabulary
    in chunk seed text AND (b) dialogue-writer invoking seed-fidelity self-license. This is not
    the deterministic-structural failure class that justifies first-occurrence proposals (like
    PROP-0009/0011/0010, where the gap fires on every correctly-authored invocation). It requires
    a coincidence of two authoring decisions. The anti-pattern rule ("do not propose on first
    occurrence of non-catastrophic SIGNAL") applies here. Hold; mark this DEC-0032 as the
    first-occurrence marker for Pattern A.

    Lower-cost fix candidate on recurrence: modify /and-write Phase 1.5 dialogue-writer rubric
    to add explicit anti-pattern "seed-fidelity is NOT a license against behavior-card fences;
    recast the seed to honor the card." This is the minimum-blast-radius intervention — it targets
    the dialogue-writer's decision point without requiring /and-substance chapter behavior change.
    The /and-substance Phase 4 behavior-card lookahead (SOFT advisory) is a heavier change and
    should be deferred unless seed contamination recurs.

    Note: this pattern is the dialogue-layer cousin of DEC-0031 pattern 3 (margit copy-paste from
    unfixed source — also held at first occurrence). Both share the same structural principle:
    downstream authors inherit upstream artifacts that may carry card-adjacent vocabulary without
    flag. The principle is worth naming; neither instance alone has reached the recurrence threshold.

  Pattern B — OK, first-occurrence hold:
    Auditor verdict-label error (PASS-WITH-NOTES + 1 HARD) is minor, non-catastrophic (caught and
    corrected by the addendum). The spec already defines verdict-label rules; this is a labeling
    error by the auditor, not a structural gate gap. First occurrence. No proposal warranted.
    Could be addressed by adding a verdict-label validation note to the bones subcommand body or
    to audit-report.schema.md, but the cost of writing the check exceeds the cost of the one-time
    correction at this recurrence level. Hold.

  Pattern C — OK, positive evidence:
    The mandatory post-hoc gate (URI-WRITE-BONES-REVIEW-GATE) caught a HARD the inline Phase 6
    gate missed. This is the design pattern working as intended — independent reviewer context
    catches different failure classes than the inline gate. Log as positive evidence that the
    gate-redundancy is earning its cost. No process change needed.

rationale: |
  All three patterns clear on recurrence grounds. None of the three meets the first-occurrence
  override criteria (catastrophic, irreversible, multi-chapter blast radius, or structurally-
  guaranteed recurrence). The inline fix resolved the pipeline impact; the gate did its job. The
  most notable finding (Pattern A) names a genuine structural seam — chunk seed text is upstream
  of behavior-card checking — but the failure requires coincident authoring decisions and is
  addressable with a single rubric line if it recurs.

trade-off: |
  Holding on Pattern A means the seed-fidelity self-license gap remains open for future chapters.
  The cost of the gap is: one potential future inline fix (~5 minutes) per occurrence, versus the
  cost of a PROP (principal triage time, implementation overhead). At recurrence_count=1 and
  given the probabilistic failure mode, holding is the lower expected-total-cost path.
  Holding on Pattern B is correct: auditor labeling errors at this rate do not warrant a schema
  or rubric change.

first_occurrence_markers:
  - Pattern A (chunk-seed vocabulary contamination via seed-fidelity self-license):
      first_occurrence: b01c04 Jarvis @9 entry 8 "acceptable"
      candidate_fix_on_recur: /and-write Phase 1.5 rubric anti-pattern "seed-fidelity is not a
        license against behavior-card fences; recast the seed to honor the card"
      recur_threshold: 2 occurrences triggers PROP; catastrophic single occurrence triggers immediately
  - Pattern B (auditor verdict-label mismatch PASS-WITH-NOTES + HARD):
      first_occurrence: b01c04 /and-review bones auditor addendum correction
      candidate_fix_on_recur: audit-report.schema.md or bones subcommand body verdict-label validation note
      recur_threshold: 2 occurrences triggers PROP

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0033 | 2026-05-27 | FAST

question: /and-facets b01c04 budget posture: option 1 (full process — 12 R1 + full R2 + full Phase 5b audience-gate, ~50-80 dispatches), option 2 (cascade-budget compression — skip R2 and/or Phase 5b, ~15-25 dispatches), or option 3 (hybrid — full R1+R2, spot-check Phase 5b on 2-3 high-risk facets, ~25-40 dispatches)?
context: |
  Historical pattern: c02 cascade-budget compression → revise-from-signals + 3 stitch cold-reads.
  c03 Phase 5b skip (zero audience-gate cycles) → 45 HARD FAULT-FORM-MODIFIER + FAULT-BONE-DELTA-
  MALFORMED at c04 /and-write Phase 1 redo (DEC-0030), costing ~15 agent dispatches to unwind.
  c04 /and-write just completed full-process (3 cycles: original + redo + additive); /and-review
  bones c04 PASSED. User has been paying for full process throughout c04 chain. Caller's stated
  default: option 1.
options: |
  (1) Full process — ~50-80 dispatches, clean historical outcome (c01)
  (2) Cascade-budget compression — ~15-25 dispatches, two-chapter track record of downstream contamination
  (3) Hybrid — ~25-40 dispatches, faster than (1), avoids the worst-case audience-gate cycles

decision: Option 1 — full process.
basis: goal:2 (cost discipline, correctly applied — total project cost of option 2 is higher than option 1 given the two-chapter evidence base) + methodology:3a (reversibility — skipping Phase 5b is not reversible; contamination propagates into c05's /and-write context window) + methodology:3b (cost — expected-total-spend for option 2 exceeds option 1 at the observed failure rate; the c03 skip cost more to clean up than the c02 full run saved) + methodology:3e (convention — full process is the canonical chain; cascade-budget is a deviation with a documented failure mode)
rationale: |
  Two consecutive cascade-budget compressions (c02, c03) both produced downstream contamination that
  cost more to remediate than the compression saved. At c03, Phase 5b skip contributed to PP-heavy
  bones that caused 45 HARD findings at c04 Phase 1, requiring a full redo cycle. The "cheaper" option
  has proven to be the more expensive path in expected-total-spend. Option 1 at 50-80 dispatches is
  the right answer because it is the answer that costs less across the project lifetime, not just this
  command invocation. Option 3 (hybrid) is an untested middle path — it saves ~15-30 dispatches
  relative to option 1 but the partial Phase 5b validation has no track record; if the spot-checked
  facets are clean but an unchecked facet is not, the contamination is the same as option 2. Given
  that the user has already paid the c03 remediation cost and has explicitly been running full-process
  throughout the c04 chain, burning that lesson for a one-command budget save is the wrong trade.
trade-off: |
  Option 1 is expensive per-invocation (~50-80 dispatches). The caller flagged this explicitly.
  The correct framing: the invocation cost is real, but the expected-total-cost including downstream
  remediation is lower for option 1 than for option 2, given the two-chapter evidence base. Option 3's
  hybrid savings (~15-30 dispatches) are not worth the contamination risk at this project stage (b01c04
  is the acceptance chapter — axis-densest, series-spine-critical).

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0034 | 2026-05-27 | SLOW

question: /and-facets b01c04 Phase 5b cycle-1 heavy fail (9/11 facets). Route: option 1 (full cycle 2 — 27+ fixer + audience dispatches), option 2 (cap-burn DELETE early — 1 fixer dispatch), option 3 (targeted hybrid — structural/mechanical fixes only, then re-fire Phase 5b on affected facets), or option 4 (stop, accept facet-incomplete, escalate)?
context: |
  Phase 5b cycle-1 returned 9-of-11 FAIL (only location-state + dialogue-taylor PASS). ~20+ distinct
  fix items: ~8 are structural/mechanical (preamble format errors, DEFERRED placeholder stubs, citation
  strips, arithmetic fix) and ~12+ are content-level (NI chassis, sensory disambiguation, vibes token
  rewrites, state-update anchors, memory scaffold repeats, feeling card-verification, exposition add,
  metaphor refusal log, dialogue-jarvis stale bone-refs). /and-facets total spend already ~60 dispatches.
  Full cycle 2 (~27 audience + fixer dispatches) would bring total to ~90-130; cycle 3 could reach
  150. DEC-0033 authorized "full process" (~50-80 dispatches) but calibrated before the heavy fail
  profile was known. c04 is series-spine acceptance chapter — highest-stakes in book 1.
  Option 2 (cap-burn DELETE) is per-spec for cap-burn path but is irreversible and loses real quality
  signal (NI chassis genuine, sensory genuine). Option 3 differs from the DEC-0033 "hybrid" (which
  spot-checked Phase 5b on 2-3 facets); option 3 here fixes what is unambiguously correct regardless
  of chosen path, then gets better information before committing to the full-cycle-2 spend.
options: |
  (1) Full cycle 2 — dispatch fixer on all ~20+ items; re-fire Phase 5 audit + Phase 5b on all 9 failing facets; 27+ dispatches minimum; cycle 3 possible.
  (2) Cap-burn DELETE — skip cycles 2+3; fixer in DELETE-only mode; irreversible; facet degradation.
  (3) Targeted hybrid — fix structural/mechanical items only (~3-5 fixer dispatches); re-fire Phase 5b on affected facets; assess remaining failures; decide cap-burn vs. targeted content cycle on residual set.
  (4) Stop — declare facet-incomplete; route to /and-stitch with documented audience-gate concerns.

decision: Option 3 — targeted hybrid (structural/mechanical fixes first, then re-fire, then decide on residual).
basis: |
  methodology:3d (optionality — structural fixes are correct regardless of which path is eventually taken;
  fixing them before committing to a 27-dispatch cycle 2 preserves the option to run a smaller targeted
  cycle 2 on the residual content failures, which may be fewer than the current 9-facet set) +
  methodology:3a (reversibility — option 2 is irreversible and loses genuine quality signal on the
  series-spine chapter; option 4 accepts a known-worse outcome; option 3 keeps the full-cycle-2 path
  open while reducing the problem set) + goal:2 (cost discipline — option 3 is expected-lower-cost
  than option 1 by getting better information before committing; structural fixes are 3-5 dispatches
  vs. 27+ for a full pre-committed cycle 2) + DEC-0033 intent (full process remains the direction;
  option 3 sequences toward that goal more efficiently than front-loading all content rewrites).
rationale: |
  DEC-0033 authorized full process for /and-facets b01c04. The situation has changed in one important
  way: Phase 5b returned a failure profile that distinguishes between (a) structural/mechanical fixes
  that are unambiguously correct and (b) content-level rewrites that require fixer dispatches against
  facet authors. These are not the same kind of work. The structural fixes (preamble format, DEFERRED
  placeholder stubs, arithmetic corrections, citation strips) should be applied regardless of what
  happens to the content failures — they are not optional even under cap-burn. The content fixes are
  where the 27-dispatch cycle-2 spend lives.

  Option 3 is not the "hybrid" DEC-0033 rejected (that hybrid spot-checked only 2-3 facets before
  proceeding). Option 3 does the structural work, then re-fires Phase 5b on the 9 failing facets,
  then makes a better-informed decision on the residual content set. If structural fixes clear several
  facets from the failing set (e.g., memory passes after arithmetic fix + preamble fix; some dialogue
  passes after DEFERRED placeholder removal), the cycle-2 content scope shrinks from 9 facets to
  maybe 4-5. A targeted cycle 2 on 4-5 facets is ~12-15 dispatches, not 27+.

  Option 2 (cap-burn) is ruled out because: (a) it is irreversible and loses genuine quality signal
  (NI chassis failure is real; sensory disambiguation is real; cap-burn DELETE permanently removes
  entries rather than improving them); (b) c04 is the series-spine acceptance chapter — accepting
  sub-density facets at this stage introduces a quality floor that shapes c05-c07's authoring context;
  (c) DEC-0033's rationale explicitly rejected the compression paths because the c02/c03 contamination
  evidence showed that per-chapter savings lead to project-level costs.

  Option 4 (stop) is ruled out because it accepts a known-worse outcome on the highest-stakes chapter
  to save dispatches — methodology:3a reversed.

  Option 1 (full cycle 2) is not wrong, but it front-loads the full 27-dispatch commitment before
  knowing whether structural fixes alone would clear a subset of the 9-facet failing set. Getting
  better information first costs 3-5 fixer dispatches and one Phase 5b re-fire on affected facets,
  potentially saving 10-15 dispatches from the cycle-2 estimate.

  Structural/mechanical fix targets (all unambiguous, all correct regardless of content outcome):
    - Memory: single-register carve-out must be in body-level preamble per schema (auditor fault-007)
    - NI: carve-out preamble arithmetic error (claims 7 mandatory + 4 non-mandatory; actual count after
      fault-006 is 11-entry post-fault set; fix the count claim)
    - Dialogue sidecars: DEFERRED-TO-R2 placeholder removal (R2 was the resolving step; stubs should
      not survive to Phase 5b)
    - Dialogue-jarvis: stale bone-references (worm-canon hard constraint; correct the refs)
    Note: NI chassis failure (narrator:7 @31 AP10 + tense-register) is a CONTENT failure and belongs
    in the post-structural-fix cycle; do not conflate with the arithmetic preamble fix.

trade-off: |
  Option 3 adds one more decision point (the post-structural-fix re-fire assessment) vs. option 1's
  single cycle-2 commitment. The cost of the extra decision point is ~1 admin dispatch overhead.
  The benefit is: if structural fixes clear even 2 facets from the failing set, the cycle-2 audience
  dispatches drop by ~6 (3 reviewers × 2 facets). The expected-cost math favors option 3 unless the
  structural fixes clear zero facets — which is possible but not the likely outcome given that memory's
  main callout is the preamble format issue, not a content failure, and the dialogue sidecars' DEFERRED
  stubs were cited by 4 reviewers as SIGNAL (removing them likely changes some REVISE verdicts).

  DEC-0033 intent is not violated: full process remains the destination. Option 3 is a better
  sequencing of steps toward full-process quality, not a compression shortcut.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0035 | 2026-05-27 | SLOW

question: /and-facets b01c04 Phase 5b cycle-2 result: 0 facets flipped to PASS. Structural fixes accepted. 9/11 still FAIL on content grounds. Route: option 1 (full content cycle 3 — all callouts, ~25-30 dispatches), option 2 (cap-burn DELETE now — ~3-5 dispatches, irreversible), or option 3 (targeted cycle 3 — 3/3-convergence items only, ~10-15 dispatches, then cap-burn residue)?
context: |
  DEC-0034 chose targeted hybrid (structural first, re-fire, then decide). Structural fixes:
  accepted across all reviewers. 0 additional facets passed. All 9 remaining FAILs are content-level.
  Current state: PASSes: location-state, dialogue-taylor (2/11). FAIL: 9/11.
  Remaining content callouts (deduplicated across reviewers):
    NI: narrator:7 @31 AP10 + tense-register (3/3 convergence — strongest cross-reviewer signal);
        narrator:3 @9 AP10 (2/3); narrator:12 @23 AP2 (2/3); narrator:9 @38 middle-clause AP2 (1/3)
    memory: mem:4 @38 scaffold-recurrence vs. mem:2 (conditional on rewrite mode — 1-2/3 convergence)
    sensory: sensory:1 @1 charged-subject + unanchored baseline; modality gaps; @17/@25 disambiguation
    state-updates: anchor-lag, non-canonical value, duplicate entries, narrative-label-as-value,
      undeclared field-extensions, compound-encoding
    vibes: AP8 parsability fails on 4 tokens; vibes:8/@17 + vibes:14/@28 proto-line citation absent;
      vibes:9/@22; Jarvis directional-ambiguity
    feeling: feel:1 @7 generic (dark-fantasy, 1/3); feel:2 @39 non-card vocabulary (worm-canon, 1/3)
    metaphor: refusal log incomplete @22/@38/@39 (dark-fantasy, 1/3)
    exposition: prior-bridge closing clause (cape-fic, 1/3); ADD at @31 (cape-fic, 1/3)
  Total cumulative c04 dispatches across /and-write + /and-review + /and-facets: ~80.
  Option 1 adds ~25-30 → ~105-110 total. Option 3 adds ~10-15 → ~90-95 total.
  Caller default: option 3.

options: |
  (1) Full content cycle 3 — dispatch fixer on all content callouts across 9 failing facets;
      re-fire those 9 × ~2 reviewers each; ~25-30 dispatches. Realistic outcome: most pass,
      some residue → cap-burn. Total: ~105-110 cumulative c04 dispatches.
  (2) Cap-burn DELETE — skip cycle 3; DELETE all callout-driving entries; ~3-5 dispatches;
      irreversible. Loses 3/3-convergence items (verified quality signal, not taste).
  (3) Targeted cycle 3 — fixer dispatches only for items with 3/3 (and 2/3) cross-reviewer
      convergence; treat 1/3 dissents as TASTE-FLAG carry-forward per pipeline doctrine;
      re-fire only touched facets; then cap-burn residue. ~10-15 dispatches.

decision: Option 3 — targeted cycle 3 on 3/3 and 2/3-convergence items only; 1/3 dissents → TASTE-FLAG carry-forward; cap-burn residue.

basis: |
  goal:1 (pipeline correctness — the pipeline's own TASTE-FLAG doctrine says 1/3 dissents are taste,
  not verified quality; option 3 is correct pipeline application, not a shortcut; option 2 DELETEs
  3/3-convergence items which is wrong regardless of spend level) + goal:2 (cost discipline — option 3
  saves ~10-15 dispatches vs. option 1 by honoring the pipeline's own convergence rules) +
  methodology:3a (reversibility — option 2 is irreversible DELETE of verified findings; option 3
  preserves cap-burn of residue as the natural next step) + methodology:3b (cost — option 3 is lower
  expected-total-spend; residue cap-burn after cycle 3 is bounded by what survives, not pre-committed) +
  DEC-0033 intent (full process — option 3 IS full process correctly applied; full process does not
  mean re-firing on every 1/3 dissent; convergence rules exist precisely to distinguish verified
  findings from taste calls)

rationale: |
  DEC-0034 chose targeted hybrid (structural first) because structural fixes might clear facets.
  That hypothesis did not confirm (0 flips). But the structural work was not wasted — it was
  correct on any path and has been applied. The situation is now different: all remaining failures
  are content-level only, and they split cleanly into two classes:

  CLASS A — 3/3 cross-reviewer convergence: narrator:7 @31 (AP10 + tense-register), and vibes AP8
  violations (4 tokens: vibes:1 "is" copula + 3 passive-finite). Three independent reviewer personas
  with distinct reading frameworks converged on the same finding. The pipeline's convergence criterion
  exists to discriminate exactly this: verified content quality vs. persona-specific preference.

  CLASS A-adjacent — 2/3 convergence: narrator:3 @9 (AP10), narrator:12 @23 (AP2), mem:4 @38 scaffold
  (conditional), sensory:1 @1, sensory modality/disambiguation callouts. Two of three personas agree —
  stronger than taste, not as strong as 3/3. These are included in cycle-3 scope: the cost of fixing
  them is bounded (they overlap with facets already in scope), and leaving 2/3-verified items for
  cap-burn on the series-spine chapter is a quality concession that option 1 would not make.

  CLASS B — 1/3 dissents (single reviewer): feel:1 @7 (dark-fantasy), feel:2 @39 (worm-canon),
  metaphor refusal log (dark-fantasy), exposition prior-bridge clause (cape-fic), exposition ADD @31
  (cape-fic), narrator:9 @38 middle-clause (cape-fic). These are TASTE-FLAGs by definition.
  The pipeline is explicit: TASTE-FLAG findings carry forward as process-signals, not as cycle-3
  fixer targets. Applying fixer to 1/3 dissents is over-retrying taste calls — the opposite of the
  discipline the spec requires.

  State-updates schema errors are mechanical and uncontested regardless of convergence count —
  they are included in cycle-3 scope on correctness grounds, not reviewer-convergence grounds.

  Option 2 is rejected because it DELETEs 3/3-convergence items. This is not a cost question;
  it is a quality question. Entries with 3/3 cross-reviewer convergence on the series-spine acceptance
  chapter are verified quality improvements. Deleting them to save ~10-15 dispatches over option 3
  is not cost discipline — it is buying permanent quality reduction with temporary dispatch savings.

  Option 1 fires fixer on 1/3-dissent items that the pipeline's own rules classify as taste.
  The incremental cost (~10-15 dispatches) does not produce better facets — it produces facets that
  satisfy a single persona's preference against the other two. Option 3 is full process correctly applied.

  Cycle-3 fixer scope:
    NI: narrator:7 @31 (AP10 chassis + tense-register) [3/3]; narrator:3 @9 (AP10) [2/3];
        narrator:12 @23 (AP2 persistent-narration) [2/3]
    sensory: sensory:1 @1 (charged-subject + baseline); thermal modality; @17+@25 disambiguation [2/3]
    memory: mem:4 @38 (scaffold-recurrence rewrite to distinct continuous-operation cue mode) [2/3]
    vibes: AP8 violations on 4 tokens (vibes:1 "is" + 3 passive-finite) [3/3]; vibes:8+vibes:14
        citation adds [uncontested]; vibes:9; vibes:16+vibes:3 Jarvis directional [uncontested]
    state-updates: all schema errors (anchor-lag, slug-list, dedup state:8/9, narrative-label,
        field-extensions, compound-encoding) [mechanical]
    TASTE-FLAG carry-forward (NOT cycle-3 fixer scope): feel:1 @7; feel:2 @39; metaphor refusal log;
        exposition prior-bridge clause; exposition ADD @31; narrator:9 @38 middle-clause

  After cycle-3 re-fire on touched facets: cap-burn any remaining failures per URI-FACETS-CAP-BURN-
  SEMANTICS. NOT-SUCCESSFUL verdict does not block /and-stitch.

trade-off: |
  Feel and exposition 1/3-dissents are not retried in cycle 3. If those reviewers hold FAIL on
  cycle-3 re-fire (nothing changed in their callout scope), those facets go to cap-burn DELETE
  of the dissenting entries. This is correct — a fixer cannot satisfy a taste dissent without
  satisfying a single persona against the other two. Cap-burn report documents TASTE-FLAG carry-forward
  items; orchestrator-critic NOT-SUCCESSFUL verdict names them; this is per-spec behavior.
  The ~10-15 dispatch savings over option 1 come entirely from not over-retrying taste.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0036 | 2026-05-27 | SLOW (process-critic)

question: Post-/and-facets b01c04 Phase 5c process-critic dispatch. Five patterns from the three-cycle audience-gate run (49 dispatches; final verdict PASS-WITH-TASTE-FLAG-RESIDUE). Which warrant process-change proposals?

context: |
  Trigger: active-project/staff/auditor/facets-audience-gate-r3.md (cycle-3 final).
  Verdict: PASS-WITH-TASTE-FLAG-RESIDUE — 4 facets 3/3 ACCEPT + 7 facets PASS with 1/3 TASTE-FLAG
  carry-forward per DEC-0035 doctrine. Gate: .claude/commands/and-facets.md#phase-5b.
  Total run: 3 full cycles + targeted re-fires (~49 audience dispatches). Patterns named by caller:
    A — /and-write Phase 7 emits [X:1, X:2] multi-token; cite-index parser handles [X:1] [X:2] only; inline fix required.
    B — 5 of 7 R2 judges wrote prose into inflight proto-lines files; 5 copies reconstructed manually.
    C — Dialogue sidecars carried stale bone-refs (n07/n10 after redo to @9); DEFERRED-TO-R2 placeholders
        survived R2 because R2 dialogue-judge brief omits sidecar update; 4 audience reviewers flagged SIGNAL/HARD.
    D — State-updates fixer cite-index regen re-added [state:2]@9 + [state:5]@22 after auditor fault-002/003
        strip; deletion not persistent across rebuild.
    E — sensory-disambiguation-pedant and sensory-old-state-reader gave opposite verdicts on sensory:2 @13
        cross-location old-state sourcing; rubric-sensory.md per-location rule genuinely ambiguous.
    F — Vibes AP8 sentence-parsability: audience-gate caught sub-saturation AP-SCAN violations; gate working as intended.
    G — Bidirectional convergence validated: multiple shared auditor + audience findings.
options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0012 + PROP-0013 + PROP-0014 + PROP-0015 + PROP-0016. OK on Patterns F and G.

basis: |
  Pattern A (cite-index bracket format drift → PROP-0012): Spec/tool interface gap — same class as
  PROP-0008. /and-write's emit format and build_cite_index.py's parser have no declared shared contract
  for multi-token bracket form. Inline fix at this run does not prevent recurrence. S-cost modify to
  .claude/commands/and-facets.md Phase 2 + /and-write Phase 7 (or parser). Justifies first-occurrence
  proposal because: structural interface gap (not a content failure), recurrence is deterministic on
  multi-dialogue-anchor bones (expected in action-dense scenes), inline-fix is not a permanent resolution.

  Pattern B (R2 judge inflight format discipline → PROP-0013): 5/7 failure rate on the same dispatch
  (R2 judge brief) is a strong signal that the brief's format requirement is implicit where it needs
  to be explicit. Prose in inflight proto-lines files causes Phase 4 merge failures. The fix is a
  one-paragraph prohibition added to the R2 dispatch brief. S-cost. First-occurrence proposal justified
  by the 5/7 failure rate — this is not one judge making an error, it is the majority exhibiting a
  behavior the brief does not exclude.

  Pattern C (sidecar stale-ref + DEFERRED-TO-R2 → PROP-0014): Two task omissions in the R2
  dialogue-judge brief (sidecar bone-ref update + DEFERRED-TO-R2 resolution). The R2 judge receives
  the sidecar but is not instructed to update it. The failure is structural (not taste): stale refs
  are HARD constraint violations when caught by audience; DEFERRED-TO-R2 survivors are phantom content
  that confuses every downstream reviewer. Both are preventable by two sentences added to the R2 brief.
  S-cost. First-occurrence proposal justified because the brief gap is explicit and deterministic —
  it will recur on any chapter with a /and-write redo + R2 dialogue-judge run.

  Pattern D (cite-index regen wiping audit-fixes → PROP-0015): Deletion-marker permanence gap. No
  existing mechanism prevents build_cite_index.py from re-propagating co-cites for tokens the auditor
  has permanently invalidated. The cap-burn path already uses a parallel deletion-marker mechanism
  (DELETED ENTRIES in _cite-index.md); audit-fault strips need the same. This is a genuine gate
  absence (change_type: add). M-cost (new file format + parser check). First-occurrence proposal
  justified because the failure is structurally guaranteed: any cite-index rebuild after an audit strip
  will re-add the stripped tokens absent a permanent deletion record.

  Pattern E (cross-location-carry rubric ambiguity → PROP-0016): Genuine rubric text ambiguity
  (two specialist reviewers with opposite readings of the same sentence). The correct interpretation
  is available from the sensory-old-state-reader's reasoning (cross-location carry is the standard
  pattern at location transitions). Codifying it as a clarification in rubric-sensory.md prevents
  future TASTE-FLAG accumulation on a question that has a correct answer. S-cost modify. First-occurrence
  proposal justified because the ambiguity is structural (not probabilistic) and the correct reading
  is already available from this run's evidence.

  Pattern F — OK (positive evidence): Audience-gate catching sub-saturation AP-SCAN violations
  (vibes AP8 tokens) is the design working correctly. The auditor's saturation threshold did not
  fire; the audience reviewer caught all 4 below threshold. Gate-redundancy confirmed. No process change.

  Pattern G — OK (positive evidence): Bidirectional convergence validated. Multiple shared findings
  between auditor + audience confirms the dual-path design is functioning. No process change.

rationale: |
  All five proposals (A-E) pass the process-failure discrimination test:
  - A: spec/tool interface gap (cite-index parser and /and-write emit share no declared contract); change_type: modify.
  - B: dispatch brief implicit where explicit needed (5/7 failure rate); change_type: modify.
  - C: two task omissions in R2 brief (sidecar update); change_type: modify.
  - D: gate absence (no deletion-marker permanence for audit-fault strips); change_type: add.
  - E: rubric text ambiguity (two correct-behavior specialists diverge); change_type: modify.
  All are S or M cost. Methodology 3b+3c both support proposing at first occurrence on structural gaps.

  First-occurrence exception applies to Patterns A, B, C, E per the same reasoning as PROP-0008/0009/0010/0011:
  the gaps are structural and deterministic, not probabilistic. Pattern D (PROP-0015) is change_type: add
  (gate absence) rather than first-occurrence-SIGNAL, so the anti-pattern rule does not apply.

  Patterns F + G are positive evidence, not gaps. Logging as evidence that the bidirectional audit
  design is earning its cost — this is the first chapter where explicit convergence trace was validated.

trade-off: |
  Five proposals authored at first occurrence, totaling PROP-0012 through PROP-0016. Anti-pattern
  rule applies to taste-flags promoting to mechanical checks — it does not apply to structural interface
  gaps, dispatch brief omissions, or rubric ambiguities. All five were inline-fixed during the run
  (they did not block the chapter) but each will recur on future chapters without a permanent fix.
  The cost of holding (per-chapter inline fix overhead) exceeds the cost of proposing now across
  the remaining chapters of the project.

follows: DEC-0035
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0038 | 2026-05-28 | SLOW (process-critic)

question: |
  Is the codification anti-pattern observed in the URI-STITCH-CHERRY-PICK-DEFAULT-ON incident
  (same-session, same-author, 12-minute gap between experiment-conclusion and contradictory-codification;
  selective citation of supporting fragments while contradicting the experiment's stated conclusion;
  in-session promotion of a tuning-candidates item without principal triage) a one-occurrence
  non-catastrophic event or a recurring class warranting a process-change proposal?

context: |
  Trigger: audit finding at active-project/staff/ablation/multi-arm-vs-single-arm-b01-c04-audit-2026-05-27/README.md
  Verdict: REVERT (URI-STITCH-CHERRY-PICK-DEFAULT-ON + URI-STITCH-MULTI-ARM-DEFAULT-ON both reverted)
  Gate: .claude/commands/and-stitch.md#cherry-pick-default-off-audit-note

  The experiment commit `2d525d2` (2026-05-27 02:57) stated: "CONTINUE=no (same as multi-arm)...
  cherry-pick fires same walkout-severity peeves as pure-winner because cost-legibility lives in
  bones SVO authoring, not stitch paragraph composition." Process-tuning candidates A-E were
  surfaced as "not yet codified." Twelve minutes later, commit `be7de51` (03:09) promoted option D
  ("make cherry-pick a default arm under multi-arm") to default-on, citing "strictly-better default"
  framing that inverted the experiment's actual conclusion.

  Remediation actions confirmed: both URIs reverted; b01-c04 canonical draft restored to single-arm;
  multi-judge verification (3/3 high-confidence) confirms single-arm > multi-arm for this chapter;
  audit note appended to `and-stitch.md` at `--cherry-pick` flag.

  Prior process-critic dispatches relevant: DEC-0024 (multi-arm FAIL, OK, no proposal) and DEC-0021
  (Phase 9 cold-read FAIL b01c02, OK) — both covered chain-command verdicts, not spec-edit commits.
  The tuning-experiment commit `2d525d2` was NOT process-critic-dispatched (correct — it was not a
  chain-command verdict).

options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0017

basis: |
  Structural gap: the process-critic trigger surface (Rule 13 tail-step hooks at /and-write Phase 6.5,
  /and-facets Phase 5c, /and-stitch Phase 9.5, /and-postop Phase 3.5, /and-review Common-Phase 4.5)
  covers chain-command non-PASS verdicts only. A session-authored URI spec-edit commit that cites an
  experiment conclusion falls entirely outside this trigger surface. No existing gate fires between
  "experiment surfaces tuning candidates" and "codification commit." The gap is structural and
  deterministic — it fires on every future experiment-to-codification transition in the same session
  unless a new trigger class is added.

  First-occurrence proposal justified by the same exception logic as PROP-0009/0010/0011: the gap
  is deterministic-structural, not probabilistic. The tuning-candidates-list shape (A-E options,
  "not yet codified") is an artifact of any experiment that surfaces multiple improvement candidates;
  the session holding the experiment's context is the highest-risk codification moment. The pattern
  will repeat on every future experiment unless the trigger is added. Non-trivial remediation cost
  (multi-arm b01-c04 run + tournament + cherry-pick + verification audit + principal attention) justifies
  first-occurrence proposal over the standard two-occurrence recurrence threshold.

  Change_type: add. Target: CLAUDE.md Rule 13 (process-critic mode trigger enumeration). The new
  trigger class is: process-critic must fire when a session proposes a URI-labeled default-change or
  feature-default spec edit that directly cites an experiment's conclusion as justification — regardless
  of whether any chain-command verdict was non-PASS. This closes the experiment-to-codification gap
  without requiring changes to any command body.

rationale: |
  The existing process-critic trigger surface correctly covers production-chain quality failures. What
  it does not cover is the meta-production activity of codifying experiment conclusions into spec
  defaults. These are distinct: a chain-command FAIL fires because the output was wrong; a codification
  commit fires because the session is now authoring the pipeline itself. The latter requires
  independent-review discipline that the former's automatic trigger surface does not supply.

  The specific failure mode (selective citation of supporting fragments + inversion of stated conclusion)
  is compounded by the tuning-candidates-list structure: when an experiment surfaces A-E options as
  "not yet codified," the list itself provides a ready-made selection menu. A session in that context
  has structural incentive to pick the option that confirms the work it just ran. The 12-minute gap
  is not unusual for a session maintaining focus — it is the normal pace of in-session work. The fix
  is not "work more slowly" but "route through a disciplined reviewer."

  The proposed gate is the minimum-blast-radius intervention: one new trigger clause in CLAUDE.md Rule 13.
  It does not change any command body, rubric, or schema. It does not require changes to existing spec-edit
  workflows. It requires that the process-critic be dispatched before a URI spec edit is committed when
  (a) the edit changes a flag default or enables a new feature by default AND (b) the edit cites an
  experiment conclusion as justification. Admin reads the experiment conclusion and the proposed edit;
  if the edit accurately represents the conclusion, process-critic returns OK (possibly with PROP for the
  change if warranted); if the edit misrepresents, process-critic returns REVISE with the specific
  divergence noted.

trade-off: |
  Adds one process-critic dispatch per URI-default-change spec edit that cites an experiment. Cost:
  low (one dispatch, O(1) read of experiment commit + proposed spec edit). Benefit: closes the
  experiment-to-codification trust gap. Downside: a correctly-faithful codification still requires a
  dispatch overhead. Accepted: the cost of a correct-codification dispatch (~1 admin call) is lower
  than the cost of a misrepresented-codification detection + revert cycle (several dispatches + principal
  attention + wasted production runs, as observed here). The asymmetry strongly favors the gate.

  Alternative considered: add audit note + principal review to all URI commits (not just experiment-citing
  ones). Rejected: too broad, catches formatting URIs and housekeeping where the risk is near-zero.
  The experiment-citation criterion is the correct discriminator.

first_occurrence_markers:
  - Codification anti-pattern (in-session tuning-candidate promotion without principal triage):
      first_occurrence: URI-STITCH-CHERRY-PICK-DEFAULT-ON (commit be7de51, 2026-05-27 03:09)
      candidate_fix: CLAUDE.md Rule 13 new trigger class (URI default-change spec edit citing experiment)
      recur_threshold: first occurrence justifies proposal (deterministic-structural gap)

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0037 | 2026-05-27 | FAST (user-proxy)

question: Are there open triage/parking-lot items that must be resolved before /and-stitch b01-c04? If no, confirm clearance and name Phase 0 advisories.

context: |
  b01c04 state: bones PASS, /and-review bones PASS-WITH-NOTES, /and-facets PASS-WITH-TASTE-FLAG-RESIDUE
  (TF-001 through TF-007 carry-forward per DEC-0035), scene-map emitted upstream. stitched: false.
  Parking-lot scan per caller: no items with target.command=/and-stitch AND target.scope=b01c04 or *.
  HARD items targeting /and-stitch are scoped to b01c01 and b01c02 — not this chapter.
  Cross-pipeline SOFT items (pl-2026-05-25-009, pl-2026-05-25-010, pl-2026-05-25-013) are
  orthogonal to the stitcher or advisory-only. DEC-0036 queued PROP-0012 through PROP-0016 for
  principal triage — not blocking on /and-stitch. TASTE-FLAG carry-forward is documented
  pipeline behavior, not a stitch blocker. User instruction "then /and-stitch b01-c04" implies
  clearance is the expected outcome.

options:
  (a) CLEAR — proceed; no HARD blocks; surface advisories to Phase 0
  (b) BLOCK on a specific item — name item + resolution path
  (c) ESCALATE — genuine ambiguity needing human

decision: CLEAR — no parking-lot HARDs target /and-stitch b01-c04; proceed.

basis: methodology:3a (reversibility — no irreversible item open; proceeding is safe) + methodology:3b (cost — blocking without a HARD item is waste) + goal:1 (pipeline correctness — the canonical chain gate order is satisfied: bones PASS → /and-review bones PASS → /and-facets complete → /and-stitch)

rationale: |
  No parking-lot HARD items target /and-stitch b01-c04 or wildcard scope. All HARD parking-lot
  items targeting /and-stitch are scoped to prior chapters (b01c01, b01c02) — unrelated to this
  invocation. The cross-pipeline SOFTs are orthogonal to stitcher operation. TASTE-FLAG residue
  (TF-001 through TF-007) is the documented output of the DEC-0035 targeted-cycle-3 path — the
  stitcher should treat them as advisory color, not blocking findings. Phase 0 should consume:
  the facets directory for b01-c04, the scene-map facet, the bones file, and TF-001..TF-007 as
  TASTE-FLAG advisories. Also surface pl-2026-05-25-013 (Q9 hyphen-density threshold tune) as
  a standing SOFT advisory at Phase 9 evaluation time.

phase_0_prime_list:
  - active-project/theater/facets/*-b01-c04.md (full facet set including scene-map)
  - active-project/theater/bones/b01-c04.md
  - active-project/theater/dialogue/ (per-character files for b01c04 cast)
  - TF-001 through TF-007 carry-forward: TASTE-FLAG advisory; no fixer action; note in Phase 0 scan
  - pl-2026-05-25-013 (Q9 hyphen-density): SOFT advisory; surface at Phase 9 evaluation, does not block

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0040 | 2026-05-28 | SLOW (user-proxy)

question: /and-write b01-c05 revise --from-signals is firing. What scope should the revise cover?

context: |
  /and-stitch b01-c05 Phase 9 cold-read FAILED 2026-05-28 on structural grounds (not polish).
  Five specific cold-reader confusions: (i) cause-chain "sheet yesterday → beating today" not stated;
  (ii) courier transition ambiguous (stood up or fell); (iii) Sera + faction/Jarvis-format frame
  unexplained; (iv) recognition @25 (feed-stops-neutral payoff) landed inert — gesture without anchor;
  (v) courier @8 introduced with no signal of recurrence / cf-d10-stake-bearer significance.
  Phase 6 bone-gate was clean (signal-001 dissolved; only advisory FLAGs carried). All failures
  are additive gaps, not structural decomposition errors.
  Bones: 31 lines across 3 scenes (s01=7, s02=12, s03=12).

options:
  (a) Full chapter re-decompose — all 3 scenes; clear all gate verdicts; full Phase 1-7 re-run; 3-4× cost of (b).
  (b) Targeted bones-add at three sites — s01 add courier-recurrence anchor bone(s); s02 add
      Jarvis-frame + cause-chain bone(s); s03 add recognition-staging bone(s) at @25; keep all
      existing bones; revise scope clears verdicts only on affected scenes.
  (c) s02 + s03 re-decompose only — skip s01 on theory facet layer carries cf-d10 plant via NI
      density + memory citations; mid-cost.

decision: Option (b) — targeted bones-add at three sites (s01, s02, s03). Revise mode, not redo.

basis: |
  goal:2 (cost discipline — all five cold-read failures are additive gaps, not decomposition errors;
  full re-decomp would re-author a structurally sound scaffold at 3-4× cost for near-zero expected
  quality delta over targeted adds) + methodology:3a (reversibility — additive bone-adds preserve
  existing IDs and gate verdicts; full re-decomp is irreversible relative to the existing scaffold)
  + methodology:3b (cost — (b) is cheapest and sufficient given the additive-gap diagnosis) +
  goal:1 (pipeline correctness — bones-first principle requires the substance be in the bones, not
  rescued by facets; s01 anchor bone is required even though facets partially compensate)

rationale: |
  Diagnostic question: are the failures about missing bones (additive gaps) or wrong decomposition
  (structural errors)? All five cold-reader confusions are additive gaps:
  (i) Cause-chain: missing bone, not wrong bone. One explicit cause-chain bone in s02 closes this.
  (ii) Courier transition: missing anchor bone in s02 (clear what happened to him).
  (iii) Sera / faction frame: missing explainer bone in s02.
  (iv) Recognition @25: missing interiority bone in s03 — gesture without interior beat.
  (v) Courier @8 significance: missing recurrence-anchor bone in s01.

  Option (c) collapses s01 add into nothing on the theory NI density compensates. The bones-first
  principle (goal:1, pipeline correctness) says substance must live in bones, not be rescued by facets.
  The facet layer can amplify a signal already present in bones; it cannot substitute for a bone that
  does not exist. s01 needs at least one anchor bone. Option (b) correctly addresses all three sites.

  Option (a) full re-decomp is not warranted: the Phase 6 bone-gate was clean; the existing 31 bones
  pass the substance contract; the cold-read failures are not evidence that the decomposition was wrong,
  only that coverage was incomplete. Re-decomposing a sound scaffold at 3-4× cost when targeted adds
  will close the gaps is anti-goal:2.

constraints_for_bone_author:
  - Revise mode only — do not clear verdicts on bones outside the three targeted sites. Preserve all existing flat IDs.
  - s01 site: add one courier-recurrence anchor bone. Must be diegetic (he is notable, not just "a
    courier") and flag cf-d10-stakes significance. Do not interrupt existing s01 bone sequence.
  - s02 site: add (a) one Jarvis-format + cause-chain bone — must make the sheet-hand-yesterday →
    beating-today causal link explicit in diegesis; (b) one bone establishing Sera's identity and
    the narrator faction/Jarvis-format report frame. Bone (ii) courier-transition ambiguity may be
    addressable via the existing s02 structure or requires one additional transition-clarification bone.
  - s03 site: add one recognition-staging bone at or just before @25. Must carry interiority — what
    Taylor understands is happening (feed-stops-neutral). "Shoulders did not reset" is gesture; the
    new bone names the recognition.
  - SVO form discipline — no prepositional phrases of place/direction/time/instrument/accompaniment
    in bone SVO text. Magnitude floor 1.0 per axis_move. No 0.5-magnitude splits.
  - Dialogue co-emission — if any new bone is a dialogue-anchor bone, per-character dialogue files
    must be updated co-bonded per URI-WRITE-DIALOGUE-COBONDED. No dialogue-anchor bones without
    dialogue file update.
  - Scene-map update — Phase 7 re-emit must update the scene-map facet to reflect new bones.

trade-off: |
  Option (b) is the minimum-cost path. If the targeted adds are insufficient (e.g., a second cold-read
  still cannot connect the cause-chain despite an explicit bone), that would indicate a decomposition
  problem, not a coverage problem — and full re-decomp would be warranted at that point. The additive
  approach is the right first move because all five failures are additive-gap diagnosis at current
  evidence.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0039 | 2026-05-28 | FAST

question: Continue b01c05 cascade through /and-facets + /and-stitch in this session, or stop at bones-reviewed PASS-WITH-NOTES and surface a clean handoff?
context: |
  Cascade progress so far:
    - /and-substance chapter b01c05: COMPLETE (Phase 5 attempt 2 ACCEPT)
    - /and-write b01c05: COMPLETE (31 bones; 3-cycle Phase 2 FAULT-FORM-PERCEPTION; Phase 5 1 HARD inline-fixed; Phase 6 2 cycles for 8 HARDs)
    - /and-review bones b01c05: COMPLETE (PASS-WITH-NOTES; 0 HARDs; 3 notes for /and-facets cite responsibilities)
  Remaining: /and-facets (est. ~79 dispatches per c04 run; likely multiple audience-gate cycles) + /and-stitch (8 render phases + Phase 9 cold-read).
  Session has already done ~30+ Agent dispatches. Continuing adds ~80-100 dispatches; may exceed practical session length.
  Clean resume mechanism exists: cascade-checkpoint.md current with `next: /and-facets b01c05`; --cascade --resume picks up cleanly.
options: |
  (a) Continue — /and-facets + /and-stitch now; ~80-100 more dispatches; chapter ships to draft/b01-c05.md by end of session.
  (b) Stop — surface clean handoff at bones-reviewed; user resumes with /and-facets later.
  (c) Continue /and-facets only, stop before /and-stitch — not a clean checkpoint.

decision: Option (b) — stop at bones-reviewed checkpoint, surface clean handoff.
basis: goal:2 (cost discipline) + methodology:3b (prefer cheaper path when outcomes are comparable)
rationale: |
  The cascade has completed its highest-information work: substance contracts authored, bones
  authored and fidelity-reviewed, chapter fully specified. /and-facets + /and-stitch are mechanical
  orchestration of the substance work already done — they have no new authoring decisions to make.
  Running them now at high context cost in a session already ~30+ dispatches deep, against a clean
  checkpoint with a working resume mechanism, is the higher-cost path with equal output quality.
  Option (c) is not a recognized checkpoint; stopping mid-facets is less clean than stopping at
  bones-reviewed.
trade-off: Chapter does not ship to draft/ today. The /and-facets + /and-stitch spend is deferred,
  not avoided — it runs next session. Total project spend is identical; per-session context budget
  is preserved.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0041 | 2026-05-29 | SLOW (process-critic → ESCALATE)

question: |
  Second consecutive cold-read FAIL on b01-c05 — does the process need to change, or is this an
  ESCALATE to the principal? Specifically: is the URI-STITCH-COLD-READ-FEEDBACK-LOOP (FAIL →
  /and-write revise) the right routing when the central event WAS recovered but CONTINUE=no fired
  on register-fatigue + design-inherent genre-seam grounds?

context: |
  First FAIL (pre-revise, 2026-05-28 early): cold-reader could not recover the central event
  (recognition-as-feed-stopping-being-neutral). 5 structural gaps; all additive; /and-write revise
  --from-signals added 4 bones (A1/B1/B2/C1); re-ran /and-review bones (PASS-WITH-NOTES);
  /and-facets (SHIPPABLE-WITH-CAVEATS); /and-stitch clean Phases 1-8.

  Second FAIL (post-revise, 2026-05-28 late):
    - Cold-reader DID recover the central event: "their instrument refuses to re-run the route cleanly"
    - CONTINUE=no fired on five different complaints:
      (1) "feed/count/architecture register is exhausting and I'm not sure what happened"
      (2) "Westeros names vs bug-feed surveillance reads as different genres grafted together"
      (3) "'Hook' appears with no introduction"
      (4) "whether the alley violence is restraint or evasion was unresolved — inferred possible sexual assault"
      (5) "emotionally muffled" — voice abstracts away the thing the ending depends on
    - Staging review: 6 findings (1 EXPAND / 2 GROUND / 2 STAGE / 1 NEEDS-BEAT); no signal-cluster threshold met
    - Prose-rationale-mute audit: CLEAN (0/8 MUTE)
    - Chapter substance: 9/9 SUBSTANCE-FELT both pre- and post-revise Phase 6; auditor PASS

  DEC-0024 deferred candidate: "if a future chapter with a documented dormancy-prefigure or
  deferred-stakes dramatic_shape FAILs Phase 9 cold-read despite sound bones, that cross-chapter
  recurrence is the trigger for a modify proposal." b01c05 is NOT dormancy-prefigure — it's an
  active chapter with violence, factional intelligence, and axis movement — so the DEC-0024 deferred
  candidate does not fire by its own stated terms. Different failure class.

  gate_path: .claude/commands/and-stitch.md#phase-9
  trigger.source_report: active-project/staff/reviews/coldread-b01-c05-2026-05-28-revise.md
  trigger.source_verdict: FAIL (second consecutive; CONTINUE=no; central event recovered)

options: |
  (a) OK — content failure, gate fired correctly; FAIL → /and-write revise is right routing
      regardless of which sub-reason CONTINUE=no fired; run a third revise cycle.
  (b) PROCESS-CHANGE-PROPOSED — add a Phase 9 routing note distinguishing recovered-event +
      CONTINUE=no-on-register-class from structural-incompleteness FAIL; route former to principal
      judgment / stitch-layer instead of mandatory bones-revise. Admin authors the proposal.
  (c) ESCALATE — second consecutive FAIL where event was recovered exceeds admin authority;
      surface to principal.

decision: ESCALATE-TO-HUMAN

basis: |
  methodology:human-only:architectural-direction (Phase 9 routing modification is architectural)
  + methodology:human-only:spend-commitments-past-routine (third revise cycle + re-cascade is
  significant spend; gate's own routing mandates it but the dominant CONTINUE=no causes are
  design-inherent, not addressable by bones-revise; the spend question needs principal authorization)
  + methodology:3a (both paths — ship with override, or run third revise — are near-irreversible;
  neither can be decided by admin from goals + LTM alone without principal judgment on the
  chapter's design intent vs. reader-experience tradeoff)

rationale: |
  Content-vs-process discrimination:

  Five CONTINUE=no complaints, analyzed by addressability:
    (1) Register fatigue ("exhausting"): IS the substance contract (cold-utilitarian register
        throughout, no tonal relief). Cannot be addressed by bones-revise without violating
        the substance contract. Zero expected gain from a third revise cycle on this complaint.
    (2) Genre-seam (Westeros vs. bug-feed): IS the project premise. Cannot be gated or fixed at
        any layer.
    (3) "Hook" unexplained: cross-episode architecture decision (Phase 1 cross-episode register
        check is informational-only per spec; the chapter correctly does not re-gloss terms
        established in c01-c04). Not a gate gap. A re-gloss would violate cross-episode register
        conventions for the in-series reader.
    (4) Alley violence ambiguity (possible sexual assault reading): prose-staging judgment. This IS
        addressable — one bone recast (the alley-sound bone) or a stitch-layer fence on the specific
        phrase. A targeted stitch-layer fix or a single-bone recast could close this. Prose-rationale-
        mute audit was CLEAN so the bone carries staging; the gap is in phrasing, not substance.
    (5) Payoff emotionally muffled: register-fatigue complaint. Same as (1) — the cold-utilitarian
        register is the substance contract; the ending cannot "feel" more without the register
        opening, which the substance contract prohibits.

  Of five complaints: three (1, 2, 3) are design-inherent, one (5) is register-inherent, one (4)
  is addressable at stitch-layer or minimal bone recast. A third /and-write revise cycle + re-cascade
  correctly addresses (4) and cannot address (1), (2), (3), or (5). Expected cold-read outcome of
  a third revise cycle: CONTINUE=no fires again on (1) and (5) even if (4) is resolved.

  Option (a) is wrong: bones-revise is the wrong tool for complaints that are design-inherent.
  The gate's routing is spec-compliant but would produce a third FAIL on the same register grounds.

  Option (b) requires admin to write a Phase 9 routing amendment at one data point, on a class
  that needs precise discriminator specification, without knowing whether the principal wants this
  path. The candidate discriminator ("recovered-event FAIL" where answer 6 captures intent vs.
  "structural FAIL" where it does not) is sound but is an architectural routing change. Admin
  cannot propose this without principal direction on whether the new path is wanted.

  Option (c) ESCALATE is correct. The questions the principal must answer:
    (Q1) Does the chapter ship with a soft-override (PASS-WITH-CAVEATS analog to b01c02),
         given that the central event IS recovered and CONTINUE=no is predominantly design-inherent?
    (Q2) If not shipping: does a targeted stitch-layer fix on complaint (4) alone + Phase 9 re-run
         (without a full bones-revise cycle) constitute an authorized intervention?
    (Q3) If neither: does the process need to change before a third bones-revise cycle? (This is
         where the candidate process change lives — see below.)

  Candidate process change (for principal awareness, NOT proposing without authorization):
    Phase 9 Step 2 routing currently has two paths: PASS and FAIL. A third path would be:
    "recovered-event FAIL" — where answer 6 (one-line summary) captures the chapter's goal/central
    event correctly, but CONTINUE=no fires. Detection: compare answer 6 against chapters[].goal
    mechanically; if the summary maps to the intent, classify as recovered-event FAIL rather than
    structural FAIL. Disposition: route to principal judgment call (ship with caveats / targeted
    stitch-layer fix / bones-revise) rather than mandatory bones-revise. Cost: S to Phase 9 spec;
    M in implication (changes the gate's authority structure). This would have correctly routed
    this dispatch and the b01c02 soft-override dispatches as operator calls rather than mandatory
    revise-routes. But writing it precisely at one data point is premature. Principal must decide
    if this path is wanted.

trade-off: |
  ESCALATE costs user attention on a question the spec has a mandatory answer for (FAIL → revise).
  But the mandatory answer costs ~30-50 dispatches + re-cascade against complaints that revise
  cannot fix. The asymmetry strongly favors escalating over blindly running a third cycle.
  If the principal confirms "run the revise anyway," admin defers and the spec is followed.
  The risk of escalating unnecessarily is one user-attention cost. The risk of not escalating
  is burning a full revise cycle with near-zero expected gain on the dominant CONTINUE=no causes.

follows: DEC-0040 DEC-0039 DEC-0024 DEC-0021
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0042 | 2026-05-29 | SLOW (user-proxy)

question: /and-write b01-c05 revise (plain, not --from-signals) — what scope? Third revise cycle; principal chose spec-default revise after DEC-0041 escalation.

context: |
  35 bones (7+15+13). Second cold-read FAIL post revise --from-signals. 5 CONTINUE=no complaints:
  (1) register fatigue — design-inherent
  (2) genre-seam Westeros/bug-feed — project-premise, not addressable
  (3) "Hook" un-introduced — cross-episode architecture, not addressable by bones-revise
  (4) alley violence ambiguous: cold-reader read "below the register I would have called human" as possible sexual assault
  (5) payoff emotionally muffled — register-inherent
  Candidate tractable item: complaint (4) — recast bone @14 or add bone around @13-@14 to make violence-type explicit.
  Structural question: does the b01c05s02 chunk actually commit to a violence-type, or does it leave it ambiguous?

options: |
  (A) S02 only revise — re-decompose s02 @8-@22; add/recast bones @13-@14 to close assault-reading; ~10-15 dispatches.
  (B) Bone-range revise @13-@16 only — narrowly recast 3-4 bones; ~6-10 dispatches.
  (C) S02 + s01 — scope (A) + "Hook" re-gloss in s01; ~15-20 dispatches.
  (D) Full chapter redo — clear all 35 bones; ~40-50 dispatches.
  (E) Scope (B) on bones; but finding is that the chunk itself already commits to beating, not assault — so the tractable fix is stitch-layer re-phrasing, not a bones-revise at all.

decision: |
  Scope (B), constrained to @13-@14 bone recast only. BUT: the screen-writer brief must contain
  the chunk's own violence-type framing. See constraint note below.

basis: methodology:3b (cost) + methodology:3d (optionality) + chunk-authority reading

rationale: |
  The b01c05s02 chunk text was read directly. Key text:
    "the geometry of the approach not consistent with opportunistic theft... a controlled
    containment, a single body held against stone... enforcement reads differently from robbery...
    the blocking of exits before contact, the absence of the post-contact scatter that marks common
    theft... a low, effortful sound, not a cry, the kind a body makes when it is trying not to
    make any sound at all"
  The chunk calls this "enforcement," not robbery, not assault. "Not a cry" is the chunk's own
  language. The mechanism block specifies coordinated physical containment (beating-geometry, not
  assault-geometry). The cold-reader's sexual assault inference arose from the stitched prose phrase
  "below the register I would have called human" — a stitch-layer phrasing choice that has no direct
  source in the chunk. The chunk's violence-type is beating/enforcement, not ambiguous at the chunk
  level.

  Therefore complaint (4) is NOT a substance-contract overwrite if bones-revise makes the violence-
  type explicit. The chunk authorizes "enforcement" as beating. The bone @14 "the side-alley returns
  the sound" is underspecified relative to what the chunk licenses — the chunk licenses "effortful
  sound, not a cry, the kind a body makes when it is trying not to make any sound at all," which is
  unambiguously a beating sound description, not an assault sound description. A bones-revise that
  makes this explicit is fidelity improvement, not substance-contract overwrite.

  Scope analysis:
    (A) S02 full re-decompose: overcorrects. s02 already has 15 clean bones including new bones from
        the revise --from-signals run. Redoing all 15 risks disturbing the bones that passed Phase 9
        complaint (i-iii, v) corrections. Only @14 is the live problem.
    (B) @13-@14 recast: sufficient. @13 "the three figures pin the courier" (correct action verb) +
        @14 "the side-alley returns the sound" (the underspecified bone). Recast or add one bone at
        @14 to make the violence-type explicit as beating/enforcement — the chunk licenses this.
        Preserves @15 spine-raise and @16 feet-found which already disambiguate direction (up).
    (C) S02 + s01 "Hook" re-gloss: complaint (3) is cross-episode architecture; re-glossing violates
        cross-episode register conventions and the bones-review would HARD-flag it as chunk-unfaithful.
        Methodology 3a: this path is NOT reversible if it violates the cross-episode contract.
    (D) Full redo: wasteful (35 bones otherwise clean).

  Screen-writer brief constraint: the brief must include the chunk's exact language — "enforcement,
  not robbery," "effortful sound, not a cry, the kind a body makes when it is trying not to make
  any sound at all," and "enforcement reads differently from robbery." The recast must stay inside
  what the chunk licenses. The fix is NOT to add graphic violence specificity the chunk lacks — it
  is to prevent the stitcher from re-introducing a phrasing that opens the assault reading.

  Note on stitch-layer alternative: the cold-reader's confusion arose from prose phrasing. A stitch-
  layer fence (prohibit "below the register I would have called human" phrasing, require explicit
  enforcement-vocabulary at @14) would also close the reading without a bones-revise. But since the
  principal chose "third revise cycle (spec default)" over stitch-layer alternative (DEC-0041 Q2
  rejected), the spec routing applies and bones-revise it is. The fix targets the correct bone.

trade-off: |
  Scope (B) does not re-decompose s02 as a whole, so it does not give screen-writer latitude to
  reconsider @8-@22 sequencing. If there are other s02 issues the Phase 9 re-run surfaces, the
  scope may need to expand at Phase 1. But per DEC-0041, only complaint (4) is tractable at bones
  layer — no other complaint justifies expanding scope. Accept the narrow scope; expand at Phase 1
  only if screen-writer flags a structural adjacency.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0043 | 2026-05-29 | SLOW (process-critic)

question: |
  Third consecutive cold-read FAIL on b01-c05 (FAIL #3 post @13 recast + scene-B re-render).
  Sexual-assault read remediated. Criterion 6 maps to goal. CONTINUE=no fires again on
  design-inherent grounds. Does the process need to change? Is Phase 9's FAIL → /and-write
  revise routing well-calibrated for recovered-event FAILs where the dominant CONTINUE=no
  causes are demonstrably design-inherent? Is a process-change proposal warranted at third FAIL?

context: |
  FAIL #1: CLASS A (could not recover central event) → /and-write revise --from-signals correct.
  FAIL #2: central event recovered; CONTINUE=no on 5 complaints (1 tractable: assault-read;
    4 design-inherent). DEC-0041 ESCALATED. Principal: run third revise cycle (DEC-0042 scope B).
  FAIL #3 (this dispatch): assault-read REMEDIATED. Criterion 6 correctly maps to goal.
    CONTINUE=no fires on: stakes-shaped-not-stakes / feed unexplained / causality loose /
    payoff abstract (no decision) / dense prose + no named cast + stranger-violence.
    All remaining complaints are design properties of the substance contract.
  Staging: 4 findings (no cluster threshold met). Prose-rationale: CLEAN.
  Three revise cycles have confirmed: revise loop cannot address design-inherent complaints.
  DEC-0041 "candidate process change" surfaced but not proposed without principal authorization.
  FAIL #3: tractable complaint fixed, design-inherent class isolated, recurrence established.

  source_report: active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md
  gate_path: .claude/commands/and-stitch.md#phase-9

options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0018

basis: |
  Content-vs-process discrimination: Phase 9's DETECTION is correct — it accurately identified a
  chapter challenging for a cold first-timer. The gap is in DISPOSITION: the binary FAIL →
  bones-revise routing cannot discriminate between (A) chapters that failed to deliver their design
  and (B) chapters that delivered their design but whose design properties are inherently challenging
  for a first-time cold reader. The b01-c05 triple-FAIL cleanly discriminates Class B: criterion 6
  maps to goal, three revise cycles addressed every tractable complaint, and the design-inherent
  class is the sole remaining residual. A stricter detection gate would not have prevented this —
  the detection is correct. The disposition rule is what needs to change. change_type: modify on
  the disposition branch only.

  DEC-0041 held the proposal pending principal authorization. DEC-0042 authorized the third revise
  cycle. FAIL #3 completes the confirmation: the authorized cycle fixed the tractable complaint and
  confirmed the design-inherent class survives. Admin authority to propose is established.

  Cross-chapter recurrence: b01c02 (DEC-0021/DEC-0024, OK at first-occurrence) + b01c05 (three
  consecutive FAILs, class now cleanly isolated). Two distinct chapters. Recurrence_count = 3
  within-chapter; class_level recurrence = 2 cross-chapter.

rationale: |
  Could a stricter version of the existing gate have caught/prevented this? No — the cold-read
  detection correctly reports what it finds. The gap is not detection sensitivity but routing: the
  binary disposition routes Class A and Class B FAILs identically (mandatory bones-revise) despite
  requiring fundamentally different remediation. Class A needs bones-revise (chapter didn't deliver
  its design). Class B needs a principal disposition call (chapter delivered its design; the question
  is whether to ship, revise the contract, or iterate knowing the design will change).

  PROP-0018 adds a Class B routing branch: criterion 6 maps-to-goal check, design-inherent audit,
  bounded disposition to principal via admin user-proxy. Detection unchanged. Class A routing
  unchanged. Cost estimate M — the spec text is S-cost to write but M in implication (changes gate
  authority structure on FAIL verdicts).

  Alternatives considered and rejected: (a) chapter-class flag for interior-cognitive chapters —
  criterion 5 is still the right question; the problem is the routing rule, not the detection
  question; (b) calibrate criterion 5 differently for interior chapters — more ambiguous to specify
  than the criterion 6 maps-to-goal discriminator and requires defining "interior chapter" mechanically.

trade-off: |
  PROP-0018 adds complexity to Phase 9 routing. Benefit: ends the open-ended revise loop for
  chapters whose design is intentionally challenging. Downside: criterion 6 maps-to-goal
  discriminator requires a semantic judgment. Guard: the default disposition (S = ship as
  PASS-DESIGN-INHERENT) routes through admin user-proxy, not auto-ship, so misclassification
  still requires admin confirmation from goals + LTM.

  Cost of not proposing: every future interior-cognitive chapter with a recovered-event design-
  inherent FAIL enters an open revise loop that cannot close. This has already cost three revise
  cycles + re-cascades on b01c05 alone.

follows: DEC-0041 DEC-0042
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0044 | 2026-05-30 | FAST (user-proxy)

question: |
  /and-substance chapter b01c06 Phase 5.5 chunk-cold-read returned CHUNK-CLASS-B (summary maps to
  goal; strict Q7 re-answer = NO). Disposition: (R) Revise chunk, (P) Proceed with risk recorded,
  or (S) Substance-contract revision?

context: |
  Chapter b01c06, first live test of the 2026-05-29 readability+completeness overhaul
  (PROP-0019/0019-A/0020/0022). Cold-reader (uninformed, no c01-c05 access) recovered all three
  scenes, causality, and payoff cleanly. Q7 strict-NO driven entirely by undefined proper nouns and
  world-terms established in c01-c05 (Jarvis, Otto, Sera, Alicent, "the feed", "the arrangement",
  Black/Green factions, Wren, the Hook, "first deliberate relative to what"). None of the confusions
  touch the chapter's internal logic. Phase 4 dramatist returned ACCEPT (clean curve). Voice-density
  guard: Signal B would NOT fire (central event is concrete actor-verb-object). Summary maps to goal
  on both halves.

decision: (P) — Proceed with risk recorded.

basis: |
  goal:1 (pipeline correctness — the overhaul's design intent is that mid-series context-noise is
  NOT a chunk-design defect; handing the confusion list to the context-aware completeness track is
  the designed path) + methodology:3a (reversibility — (R) re-authors a non-defective chunk;
  that is irreversible work for zero expected quality gain) + methodology:3d (optionality — (P)
  preserves the highest-information live-validation path: the designed cold-read→completeness-track
  handoff exercises on a live chapter for the first time; (R) collapses that test into a trivial
  non-match)

rationale: |
  The strict-NO is textbook mid-series context-blindness. The overhaul report (2026-05-29)
  explicitly names this as the c05 FAIL root cause and names this exact class of confusion — proper
  nouns established in prior chapters flagged by a context-free cold reader — as the load that
  PROP-0020's followability pre-check (/and-review bones follow_check) + /and-facets Phase 2.5
  context-ledger are equipped to adjudicate. The cold-read is doing exactly what it is supposed to
  do: surfacing the confusion list. The routing decision is whether the confusion list represents a
  chunk-design hole (Class A → R) or mid-series context noise (Class B → P). Every indicator says
  Class B: summary maps, causality is tight, payoff lands, all confusions trace to series-established
  vocabulary. No chunk redesign would cure undefined-proper-noun blindness for a context-free reader;
  the cure is the weave layer.

  The caller's analysis is correct and should be confirmed as stated. The Q7 confusion list should
  be recorded as cold_read_risk_carry and handed to /and-review bones follow_check as the
  context-weave checklist.

trade-off: |
  (P) accepts that the overhaul's completeness track will need to adjudicate these items. If the
  context-aware layer also fails to weave them (i.e., /and-review bones FOLLOW-FAIL fires), that
  would retroactively indicate the chunk-design needed to pre-empt more context — but that call is
  more informed with context-aware evidence than with the context-free reader's response. Deferring
  the judgment to the right layer is correct. The risk carry is the mechanism designed for this.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0045 | 2026-05-30 | SLOW

question: Does this project's custom axis `relational_anchor_status` satisfy `schemas/bones.schema.md`'s requirement that a canonical speech-form bone (`<speaker> speaks to <listener>`) must move "≥1 communication-class axis (community / knowledge / reputation / trust)"?

context: |
  /and-write b01c06 Phase 2 constraint audit raised fault-002 against bone b01c06s01n04
  (`wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac`; relational_anchor_status
  +1.0, class: emotional). The auditor's proposed fix — "add a knowledge or trust axis move at
  magnitude 1.0" — is impossible: this project's signature replaced the universal taxonomy axes
  (community/knowledge/reputation/trust) with a fully custom set. No axis in the project signature
  is named community, knowledge, reputation, or trust. The axis at issue (`relational_anchor_status`)
  is the project's explicit carrier for relational-bond weight loading (class: emotional). The
  chapter contract designates this exchange as the relational_anchor_status carrier; it is the
  first spoken Wren↔Taylor line in the book. This is the first live test of the readability
  overhaul (PROP-0019/0020/0022). The load-bearing first-dialogue bone is at stake.

  Candidate ruling supplied by caller: relational_anchor_status IS this project's communication/
  relational-class axis for the speech-bone requirement; the schema's enumerated list should be
  read as "a relational/communication-class axis per the active project signature," not as a
  literal slug-match against the universal four.

options: |
  (A) CONFIRM candidate ruling: relational_anchor_status satisfies the speech-bone requirement;
      fault-002 is not a real fault; n04 keeps relational_anchor_status +1.0 and is valid.
  (B) REJECT candidate ruling: the schema's enumerated four (community/knowledge/reputation/trust)
      are the only valid axes for this requirement; the bone must be recast or restructured.
  (C) ESCALATE: this is an architectural direction question requiring the principal's judgment.

decision: CONFIRM candidate ruling (option A). relational_anchor_status satisfies the canonical speech-form
  substance requirement on this project. fault-002 is not a real fault. n04 keeps relational_anchor_status
  +1.0 and is a valid speech-anchor bone.

basis: |
  goal:1 (pipeline correctness — apply the rule in service of its purpose, not as mechanical
  slug-matching against a taxonomy that this project does not use) + methodology:3a (reversibility —
  option B requires recast or structural redesign of a load-bearing bone; option A has no irreversible
  cost) + methodology:3e (convention — DEC-0006/0007 both applied spec-intent over mechanical literalism;
  same principle governs here) + schema purpose analysis (the communication-class requirement exists to
  prevent speech bones from being zero-substance on the relational/social axis; it does not exist to
  enforce the universal taxonomy's slug names as a vocabulary requirement).

rationale: |
  The schema's communication-class requirement at lines 140-141 and 165 names four axes:
  community / knowledge / reputation / trust. These are the universal questionnaire taxonomy's
  communication-class entries. The requirement's purpose is clear from the surrounding text:
  speech bones must move "at least one communication-class axis" so that a `speaks to` bone is
  not zero-substance on the social/relational dimension — preventing speech bones from being
  authored as physical-action-only events that happen to involve speech.

  This project replaced the universal taxonomy with a fully custom signature. `relational_anchor_status`
  (class: emotional) carries the relational-bond weight-loading function that `community` and `trust`
  carry in the universal taxonomy. `social_tether-prot-*` (class: plot) carries the social-connection
  dynamics. No project axis is named community/knowledge/reputation/trust because those universal
  functions were subsumed into the project's custom axis design.

  Under option B, canonical speech-form bones would be permanently unauthorable on this project —
  no project axis matches the schema's enumerated slugs, so every `speaks to` bone would fault
  regardless of substance declared. This is an absurd result. The schema cannot have intended to
  make speech bones malformed by design on any project that remaps the universal taxonomy.

  The correct interpretation: the schema's enumerated list names the universal taxonomy's
  communication-class entries as the reference class. A project that remaps the taxonomy satisfies
  the requirement by moving an axis that is functionally equivalent — one that carries the
  relational/communicative/social-bond function in the active project signature.
  `relational_anchor_status` is that axis: a first spoken Wren↔Taylor exchange forming the relational
  anchor is precisely what community/trust movement looks like in this project's axis vocabulary.

  The DEC-0006 and DEC-0007 precedents (spec-intent governs, not mechanical literalism when
  mechanicalism serves no spec goal and produces a worse pipeline-correctness outcome) apply directly.

  Option C (ESCALATE): not warranted. This is a schema-interpretation question, not an architectural
  direction question. The interpretation follows from the schema's stated purpose applied to a project
  that has validly customized its axis taxonomy. Goals and methodology resolve this clearly.

trade-off: |
  Option B enforces literal slug-matching but makes canonical speech bones permanently malformed on
  this project — a worse pipeline-correctness outcome, and it guts the chapter's first Wren↔Taylor
  relational beat. No gain from option B that option A does not also provide (both honor the schema's
  anti-zero-substance purpose; A does it correctly for a remapped taxonomy).

  Confirming A also flags a genuine schema ambiguity: the enumerated list does not say "or the
  project-signature equivalent," which is what caused the auditor's false fault. A parking-lot
  schema-clarification item is the correct follow-on (caller stated intent to file it).

  The parking-lot item should target bones.schema.md lines 140-141 and 165, change_type: modify
  (S cost), clarifying that the enumerated axes are the universal taxonomy's communication-class
  examples, not an exhaustive slug-require list. That prevents this from re-litigating at c07+.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0046 | 2026-05-30 | FAST (process-critic)

question: |
  /and-write b01c06 Phase 6 bone-gate: 1 HARD HELD-AXIS-NOT-WITNESSED (political_register-prot
  s01; resolved by assigning axis to existing bone s01n02 — no new bone) + 2 SIGNALs
  accepted-with-rationale (signal-001: moral_legibility_to_self +1.0 realized vs +0.5 target;
  signal-002: stakes-axis tie moral_framework=moral_legibility at 1.0). Does the process
  need to change? Specifically: (1) does the fractional-target-floor-realization recurrence
  warrant a named auto-accepted gate disposition, and (2) does the HELD-AXIS-NOT-WITNESSED
  warrant any new proposal beyond PROP-0011?

context: |
  source_report: active-project/staff/auditor/write-b01c06-bone-gate.md (Phase 6 bone-gate)
  gate_path: .claude/commands/and-write.md#phase-6
  Prior proposals: PROP-0010 (fractional-target-floor; recurrence_count already 2; c06
  evidence already in recurrence_refs). PROP-0011 (HELD-AXIS-NOT-WITNESSED completion gate;
  recurrence_count 1 from c04; c06 not yet in recurrence_refs).
  Chapter b01c06 outcome: 0 HARDs survived to Phase 7; 2 SIGNALs accepted-with-rationale;
  audience leg SUBSTANCE-FELT 3/3. EVENT-NOT-CONCRETE, ABSTRACTION-DOMINANCE, SENSORY-GROUNDING
  all PASS. Chapter proceeding to Phase 7.

options: n/a (process-critic mode)

decision: |
  Candidate 1 (fractional-target-floor pattern): OK-MERGED-INTO PROP-0010.
  Candidate 2 (HELD-AXIS-NOT-WITNESSED): OK-MERGED-INTO PROP-0011 (recurrence_refs updated).
  No new proposal warranted on either candidate.

basis: |
  Candidate 1: PROP-0010 already has recurrence_count: 2 and the c06 evidence in its
  recurrence_refs. The gate handled the b01c06 case correctly (LEGAL ruling, ±1 tolerance
  absorbs it, no HARD). A named auto-accepted gate disposition would pre-empt PROP-0010's
  upstream pre-flight fix — proposing gate-level machinery for a collision that PROP-0010
  eliminates at the source is redundant until PROP-0010 is triaged. Premature.

  Candidate 2: PROP-0011 proposes Phase 1 step 4a completion gate for held-axis witnessing.
  b01c06's HELD-AXIS-NOT-WITNESSED (1 axis; resolved with no new bone) is the same failure
  class at lower severity than c04 (5 axes; 5 new bones). Recurrence evidence for PROP-0011;
  not a novel pattern. Merging c06 evidence into PROP-0011 recurrence_refs.

  Content vs. process: the b01c06 gate outcome is a gate working correctly (caught the HARD;
  resolved cheaply). The upstream authoring gap is already targeted by PROP-0011. No new
  change_type required.

rationale: |
  The two SIGNALs (moral_legibility over-delivery + stakes-axis tie) are direct consequences
  of the fractional-target-floor structural collision that PROP-0010 targets upstream. The
  signals were accepted-with-rationale cleanly — the gate disposition rule did not fail.
  Proposing a named auto-accept disposition at the gate level before PROP-0010 (which would
  eliminate the collision at /and-substance chapter) is triaged would be building downstream
  workarounds for an upstream root cause. Methodology: prefer modify-at-source over
  modify-at-symptom; prefer the already-authored PROP-0010 over a second PROP targeting
  derivative symptoms.

trade-off: |
  Not proposing a named gate disposition means each future fractional-target-floor occurrence
  will re-litigate as a SIGNAL with rationale. Acceptable cost: the rationale is mechanical
  (within ±1, LEGAL) and takes one auditor sentence. The upstream PROP-0010 fix is the correct
  closure; gate-level naming before that fix lands would be premature accumulation.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0047 | 2026-05-30 | FAST

question: |
  /and-facets b01-c06 Phase 0 step 4b HARD-ABORT: bones_review.bones_file_mtime_at_review
  (1780107964) != current mtime of theater/bones/b01-c06.md (1780111145). Supposed to catch
  a re-emitted bones file that would stale the review. How to dispose?
  Options: (A) reconcile the stamp in memory (update to 1780111145, note reason, proceed);
  (B) re-run /and-review bones b01c06 in full; (C) proceed without touching memory, log discrepancy.

context: |
  git diff e9883f2 HEAD -- theater/bones/b01-c06.md is EMPTY. Bones file is byte-identical
  to its emit commit. Single commit touching this file is the emit commit. The bones_review
  (commit 9af14cd, PASS, follow_check PASS-WITH-NOTES) described the exact same file (25 bones,
  flat-1-25, dialogue-token on flat-4). Mtime shifted because PR #76 was merged and the repo
  was re-checked-out in a fresh container — git does not preserve mtimes across clone/checkout.
  Pure environment artifact: the check's intent ("bones not re-emitted since review") is
  satisfied; only the filesystem timestamp proxy is stale.
  gate_path: .claude/commands/and-facets.md#phase-0

options: |
  A: Reconcile the stamp — update bones_file_mtime_at_review to 1780111145 in showrunner
     memory, note the reconciliation reason, proceed. Cost: ~0.
  B: Re-run /and-review bones b01c06 in full. Cost: full multi-agent review re-run on a
     verified no-op. Honors the rule literally.
  C: Proceed without memory update; log discrepancy only.

decision: Option A — reconcile the stamp; update bones_file_mtime_at_review to 1780111145,
  note the environment-artifact cause inline, proceed to Phase 1.

basis: goal:2 (cost discipline — option B is verified-no-op spend) + methodology:3a
  (reversibility — A is trivially reversible; B burns real tokens) + methodology:3b (cost —
  outcomes identical; A is cheaper by the full gate-re-run cost) + goal:3 (memory accuracy —
  C leaves memory in a known-inaccurate state, which violates the nothing-changes-without-
  recording principle)

rationale: |
  The mtime check is a proxy for content identity. The proxy failed due to environment behavior
  (git checkout resets mtimes), not a file change. Content identity is confirmed by two
  independent signals: (1) git diff shows zero byte-difference; (2) the review report's internal
  description matches the current file exactly (same bone count, same structure, same token).
  The intent of the HARD-ABORT is satisfied. Re-running to satisfy the literal proxy when the
  trigger is a known-false-positive burns tokens and produces an identical result. Option C
  leaves memory claiming a review timestamp that is known to be wrong — goal:3 violation.
  Option A corrects the record, makes memory accurate, costs nothing.

trade-off: |
  Option A requires trusting the git-diff + report-description evidence chain instead of
  re-running the gate. The evidence chain is strong (two independent sources agree). The only
  way option B produces new information is if both sources are simultaneously wrong, which
  would indicate a repo integrity problem no review re-run could fix anyway.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0048 | 2026-05-30 | SLOW (user-proxy)

question: |
  /and-stitch b01-c06 Phase 9 cold-read terminal gate: COMPLETENESS PASS + READABILITY AIRLESS.
  Fork: (A) PASS-WITH-DEPTH-PASS-REQUIRED — ship terminal, flag mandatory /and-write revise
  --from-signals depth pass before project-stable; (B) FAIL — full /and-write revise +
  re-cascade /and-facets + /and-stitch. Which verdict?

context: |
  First live chapter under the separated COMPLETENESS/READABILITY scoring overhaul (PROP-0022).
  COMPLETENESS: PASS — central event (named-person delivery + withheld name contrast) recovered,
  3-layer jeopardy affirmed, causal chain holds, CONTINUE = weak yes. Step-2 FAIL conditions
  do not fire. Residual confusions are mid-series context-noise, not c06 defects.
  READABILITY: AIRLESS — narrator reads as instrument, accounting section (paras 27-35) worst
  offender (abstract bookkeeping metaphor stacked), withheld name reads as "tidy diagram of a
  feeling," only two breathing spots (child's spoken line, physical friction of stylus). Root
  cause diagnosed as apparatus-dominant bone-set (~18/25 record-substrate verbs) — a bone-layer
  authoring defect, not a stitch-layer voice problem. Prior conclusion (c02 experiment):
  "cost-legibility lives in bones SVO authoring, not stitch paragraph composition."
  Phase 9 composition rule: PASS = completeness-pass AND READABLE. AIRLESS + completeness-pass
  → at minimum PASS-WITH-DEPTH-PASS-REQUIRED. AIRLESS on central event ITSELF → FAIL.
  The central event IS the accounting section → could argue that airlessness lands on the
  central event itself, pushing toward FAIL (Option B).
  Default proposed: Option A with rationale that event was RECOVERED (reader DID identify it),
  continue = yes, fix is /and-write bones-layer revision, depth-pass is the overhaul's designed
  lever for exactly this.

options: |
  A: PASS-WITH-DEPTH-PASS-REQUIRED. Ship terminal. Flag mandatory depth pass
     (/and-write b01c06 revise --from-signals) before project-stable. Smaller blast
     radius; right-sized fix; completeness + recovery + continue-yes argue against
     full re-decompose.
  B: FAIL. Full /and-write revise re-decompose + re-cascade /and-facets + /and-stitch.
     Treats airlessness-on-central-event as a structural decomposition defect requiring
     the full re-entry loop. Heavier; 30+ dispatches.

decision: Option A — PASS-WITH-DEPTH-PASS-REQUIRED.

basis: goal:1 (pipeline correctness — Phase 9 composition rule's AIRLESS-on-central-event
  FAIL trigger requires the central event to be unrecoverable or undelivered, not merely
  abstract-in-rendering; that criterion is not met here) + goal:2 (cost discipline —
  Option B is 30+ dispatches when the root is a bone-layer authoring fix, not a
  decomposition defect) + methodology:3a (reversibility — A leaves the depth pass
  scheduled; B overwrites a structurally sound chapter on a rendering defect) +
  methodology:3b (cost — outcomes comparable; A routes to the correct repair layer) +
  methodology:3d (optionality — A preserves the chapter's structural work; B discards it)

rationale: |
  The Phase 9 composition rule's FAIL branch for AIRLESS targets "AIRLESS on the central
  event ITSELF" — the framing is delivery failure, not rendering abstraction. The cold-read
  reader DID identify the central event (named-person delivery + withheld name), confirmed
  jeopardy, confirmed causal chain, and returned CONTINUE=yes (weak). The event was delivered
  and recovered. What failed is the IMPACT quality — the reader got the content but felt it
  as a diagram rather than a gut-punch. That is a bones-SVO rendering defect (the bone-set is
  apparatus-dominant), not a decomposition defect. The c02 experiment's conclusion applies
  directly: this class of problem lives in bones authoring, not stitch composition. The
  depth-pass loop (/and-write revise --from-signals targeting the abstract accounting
  bones) is the overhaul's designed and documented lever for exactly this class. Option B
  would re-decompose a chapter whose structural commitments (event architecture, jeopardy
  layering, causal chain) the cold-read confirmed as sound — that is wrong-layer repair.
  Additionally: the live-validation headline finding is the same either way — the separated
  scoring correctly refused a clean PASS on an airless chapter (the c05 failure mode caught
  at the terminal gate, working as designed). Option A captures that finding faithfully.

trade-off: |
  Option A accepts a softer treatment of "AIRLESS on the central event" than a strict
  literal read of the composition rule would require. The trade-off is: the central event's
  accounting section IS the airless worst zone, but the event was still recovered, so the
  airlessness is an impact-degradation rather than a delivery failure. If the depth pass
  does not resolve the airlessness (bones re-authored but still apparatus-dominant), the
  next cold-read should FAIL the gate and route to Option B. That is the correct escalation
  path: try the right-layer fix first; escalate to full re-decompose only if it fails.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0049 | 2026-05-30 | SLOW (process-critic)

question: |
  b01-c06 Phase 9 cold-read: PASS-WITH-DEPTH-PASS-REQUIRED (completeness PASS, readability
  AIRLESS). The readability track fired at every upstream checkpoint (BONES-AIRLESS-RISK flagged,
  3 grounding-ledger lines opened, Phase 4.5 AIRLESS-HOLE, Phase 4.6 authored 3 grounding adds,
  Phase 4.6 Step-2 returned ALIVE, Phase 4 applied voice-embodiment on 4 VOICE-FIXABLE anchors)
  — yet the terminal cold-read still returned AIRLESS. Does the process need to change?
  Specifically: is the grounding-ledger too narrow for apparatus-dominant chapters? Should the
  apparatus-dominant-bone-set risk be caught/routed differently? Or is the design correct
  (depth-pass loop working as intended)?

context: |
  First live chapter (b01-c06) under the 2026-05-29 readability+completeness overhaul.
  Root cause per DEC-0048: ~18/25 bones have record-substrate verbs (apparatus-dominant
  by contract). The overhaul's grounding-ledger licensed 3 sensory adds; voice-embodiment
  handled 4 VOICE-FIXABLE anchors. The cold-reader named exactly those 2 interventions as
  the only breathing spots — confirming they worked. But 3 grounding adds + 4 person-first
  renders against 18 apparatus-dominant spine bones was insufficient in coverage.
  Critical distinction: c05's airlessness was render-layer (concrete bones, apparatus-rendered
  at stitch) — cured by person-first voice discipline. c06's airlessness is bone-layer
  (apparatus-dominant SVO by contract) — cannot be cured by sensory adds or person-first
  renders without content invention. The overhaul was designed and tested against c05's class
  (render-layer abstraction); it has not been tested against bone-layer apparatus-dominance
  until this chapter.
  The Phase 4.6 Step-2 re-review returned ALIVE after 3 grounding adds. The terminal cold-read
  returned AIRLESS. An informed context-aware reviewer called ALIVE where a context-blind
  cold-reader called AIRLESS — because context-aware readers compensate for apparatus prose
  that cold-readers cannot inhabit.

  source_report: active-project/staff/reviews/coldread-b01c06-2026-05-30.md
  source_verdict: PASS-WITH-DEPTH-PASS-REQUIRED
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-facets.md#phase-2.5, .claude/commands/and-facets.md#phase-4.6]

options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0023   # renumbered from PROP-0020 by orchestrator: PROP-0020 is the existing context-weave proposal; this apparatus-airless proposal is PROP-0023 (next-free)

basis: |
  Content-vs-process: the gates detected correctly (BONES-AIRLESS-RISK, AIRLESS-HOLE, AIRLESS at
  terminal), and the depth-pass loop routed correctly. The gap is in the Phase 4.6 re-review's
  ALIVE verdict threshold: it cleared a bone-layer-apparatus chapter as ALIVE because the
  grounding-ledger mechanism (sensory adds around apparatus prose) is palliative on bone-layer
  abstraction, and the re-review has no separate track distinguishing "grounding-patched apparatus"
  from "genuinely de-abstracted." A stricter version of the Phase 4.6 ALIVE verdict — one that
  requires evidence of bone-level de-abstraction (not just surrounding grounding adds) on
  apparatus-dominant chapters — would have routed to /and-write revise --from-signals before
  stitch, saving the full stitch + Phase 9 round-trip.

  Recurrence count: 1 (first live apparatus-dominant chapter). Non-catastrophic (depth-pass loop
  fired correctly). Proposing at first occurrence because: (a) the mechanism is precisely
  discriminated from c05's render-layer class (bone-layer apparatus vs render-layer apparatus are
  structurally distinct failure modes); (b) the Phase 4.6 false-ALIVE is the concrete gate gap —
  not a detection miss but an ALIVE-verdict-threshold miss; (c) the fix is a single qualifier
  added to the Phase 4.6 ALIVE criteria (modify, not add); (d) the overhaul's own honest-
  limitations note said "nothing is live-proven; b01-c06 is the first live test" — this is
  precisely the class of gap that live testing was expected to surface.

  Target is Phase 4.6 Step-2 ALIVE verdict criteria in .claude/commands/and-facets.md
  (the grounding-ledger re-review step). change_type: modify.

rationale: |
  Three candidate process explanations analyzed:

  Candidate 1 — Grounding-ledger capacity too narrow.
  The grounding-ledger has no proportional-licensing rule based on apparatus-dominance count.
  Phase 2.5 / 4.6 authored as many GROUNDING-REQUIRED findings as the reviewer found; 3 is
  what the reviewer found. The question is whether the reviewer applied the right detection bar.
  On a chapter with ~18/25 apparatus-dominant bones, 3 GROUNDING-REQUIRED findings suggests the
  reviewer scanned for isolated airless patches rather than recognizing the whole-chapter
  apparatus-dominant pattern. This is a detection-threshold gap in the Phase 4.6 re-review.

  Candidate 2 — Apparatus-dominant-bone-set risk should be caught earlier (at /and-write Phase 6).
  ABSTRACTION-DOMINANT SIGNAL already exists at Phase 6. If it fired, it was surfaced.
  The issue is what happens downstream: the SIGNAL routes to grounding-ledger work at facets,
  which is palliative. For a chapter where the substance contract produces apparatus-dominant
  SVOs by design (a surveillance operative's internal accounting), the correct upstream signal
  is not "add grounding" but "de-abstract the bones." This suggests the routing from
  ABSTRACTION-DOMINANT SIGNAL should distinguish palliative-appropriate (isolated apparatus
  patch) from route-to-bones-revise-appropriate (whole-chapter apparatus-dominant pattern).
  But the Phase 6 SIGNAL disposition already allows the bone-author to remediate in revise mode.
  The gap is not at Phase 6 detection; it is at Phase 4.6 verdict.

  Candidate 3 — The current design is correct; the depth-pass is the right lever.
  This has merit: Phase 9 refused a clean PASS and required a depth pass. The loop is working.
  BUT: the Phase 4.6 Step-2 ALIVE verdict was a false positive (informed reviewer cleared
  what a cold-reader experienced as airless). If the false-ALIVE had not fired, Phase 4.6
  would have output AIRLESS-UNRESOLVABLE-AT-FACETS-LAYER and routed to /and-write revise
  --from-signals BEFORE stitch — saving the full stitch + cold-read round-trip. The depth
  pass is the right repair layer, but the Phase 4.6 false-ALIVE deferred it one full stitch
  cycle later than necessary.

  Net discrimination: the gap is Candidate 1 + part of Candidate 2 — the Phase 4.6 ALIVE
  verdict threshold does not have an apparatus-dominant-chapter qualifier. The fix is a single
  qualifier added to the Phase 4.6 Step-2 re-review criteria. change_type: modify.

trade-off: |
  The false-ALIVE at Phase 4.6 cost one full stitch + Phase 9 round-trip (~10-15 dispatches).
  Adding the qualifier would route apparatus-dominant chapters to the depth pass before stitch.
  Guard: the qualifier only fires when BOTH BONES-AIRLESS-RISK AND ABSTRACTION-DOMINANT are in
  the chapter record — two independent upstream gates must agree before the stricter ALIVE bar
  applies. This limits false-positive routing of non-apparatus-dominant chapters.

follows: DEC-0048
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0050 | 2026-05-30 | SLOW (user-proxy)

question: |
  b01-c06 live-validation run complete (PASS-WITH-DEPTH-PASS-REQUIRED, DEC-0048). User said "continue."
  The named next step is the mandatory depth pass (chapters[b01c06].depth_pass_pending = true, de-abstract
  accounting-middle bones @16-@21). Disposition: run the depth pass NOW (options A or C), or defer to
  before book-close and proceed to b01c07 (option B)?

context: |
  Three structural complications identified by the caller:
  (1) `--from-signals` would target the WRONG bones. The Phase 6 bone-gate SIGNALs were moral_legibility
      floor + s03 stakes-tie — not the apparatus-airless accounting bones. The actual airlessness is a
      cold-read READABILITY signal, not a Phase-6 gate-SIGNAL. The real depth pass is a scene-s03-scoped
      revise to de-abstract @16-@21.
  (2) PROP-0023 (the apparatus-dominant-chapter revise prescription) is OPEN, UNIMPLEMENTED, pending
      principal triage. Acting on its logic now is acting on an un-triaged proposal.
  (3) The depth pass is a full re-cascade (~40+ dispatches) after a session that already ran the
      entire chain.
  (4) DEC-0048 scoped the depth pass to "before project-stable," not "immediately."
  (5) If the depth pass re-authors the accounting bones and the next cold-read still returns AIRLESS,
      the outcome escalates to FAIL/re-decompose — i.e., the depth pass may not resolve it, and the
      accounting is abstract-by-contract.

options: |
  A: Run depth pass NOW as scene-s03-scoped /and-write b01c06 revise (de-abstract @16-@21), then
     re-cascade facets+stitch. Largest spend; acts on un-triaged PROP-0023 logic; --from-signals flag
     would target wrong bones (cannot be used as-scribed); uncertain outcome; may escalate to FAIL.
  B: Defer depth pass; proceed to b01c07. Depth pass flagged (depth_pass_pending stays true); runs
     before book-close. PROP-0023 gets triage first; revise brief can be constructed correctly.
  C: Run /and-write revise (bone de-abstraction of s03) now as core; checkpoint; defer facets+stitch
     re-cascade. Splits the difference but leaves chain in inconsistent state (bones re-emitted stales
     all existing facets; draft no longer terminal; no clean resume point — functionally degrades to B
     but with wasted token spend and a stale artifact set).

decision: Option B — defer the depth pass; proceed to b01c07.

basis: |
  goal:2 (cost discipline) + methodology:3b (cost — B is cheapest per-session; no tokens spent on
  an uncertain-outcome re-cascade) + methodology:3a (reversibility — the depth pass is authorized and
  scheduled; deferring it does not cancel it; B preserves the option to run it with the correct brief)
  + methodology:3d (optionality — B preserves the ability to consult the correct signal list for the
  brief after PROP-0023 triage; A and C lock in a brief constructed from incomplete guidance)

rationale: |
  Option A fails for two independent reasons:
  (a) The `--from-signals` instruction in DEC-0048 is mechanically wrong for this chapter. Phase 6
      SIGNALs (moral_legibility floor + stakes-tie) were the wrong signals for the accounting-bone
      airlessness. The depth pass needs a COLD-READ-SIGNAL-driven brief (target the apparatus-dominant
      bones named by the cold-read + the ABSTRACTION-DOMINANT SIGNAL list), not a --from-signals brief
      that reads Phase 6 gate_verdict.signals[]. Running it now with any brief means constructing that
      brief from scratch on an ad-hoc basis, without the guidance that PROP-0023 was authored to
      provide.
  (b) PROP-0023 is open-pending-principal-triage. It prescribes precisely how to handle apparatus-
      dominant depth passes (replace apparatus SVOs with concrete actor-verb-object bones; signal set
      = ABSTRACTION-DOMINANT from Phase 6 + GROUNDING-REQUIRED from grounding-ledger + Phase 4.6
      re-reviewer scene-level notes). Acting on that prescription before triage is premature
      implementation of an un-triaged proposal.

  Option C is worse than B on every axis: it consumes tokens (the bones-revise portion), produces
  an inconsistent artifact state (re-emitted bones stale all facets, making the existing facets
  unreliable and the prior draft non-terminal), and has the same uncertain outcome. The only "benefit"
  of C over B is that some work gets done — but that work, done without the correct brief, may itself
  need to be redone after PROP-0023 triage. C is B minus the clean state, not B with an advantage.

  Option B is the correct answer: the depth pass is authorized (DEC-0048), flagged (depth_pass_pending),
  and scoped "before project-stable." That obligation is honored. It simply runs before book-close
  rather than this instant, after PROP-0023 is triaged and the correct brief (cold-read-signal-driven,
  targeting @16-@21 apparatus SVOs specifically) is specified. b01c07 is the clean forward motion the
  "continue" directive indicates.

  The spend-commitment precedent (DEC-0009, DEC-0041) further supports deferring: full-cascade re-runs
  with uncertain outcomes have consistently been the category where proceeding without deliberate brief
  construction costs more than the delay.

trade-off: |
  B means b01c06 ships PASS-WITH-DEPTH-PASS-REQUIRED as its current state; the depth pass runs later.
  No quality loss: the terminal deliverable (draft/b01-c06.md) is already emitted and is the correct
  current state. The depth pass improves the chapter before project-stable; deferring does not prevent
  that. The cost of B over A is: the accounting-middle airlessness stays unresolved for one more
  chapter cycle, and depth_pass_pending flag stays set. The cost of A over B is: ~40+ dispatches on
  an uncertain outcome with an ad-hoc brief on an un-triaged proposal, with possible escalation to
  FAIL/re-decompose that costs even more.

follows: DEC-0048 DEC-0049
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0051 | 2026-05-30 | SLOW (process-critic)

question: |
  b01c07 Phase 6 bone-gate FAIL: 6 HARD (EVENT-NOT-CONCRETE + SUBSTANCE-FLAT on 4
  argument-middle bones). /and-substance Phase 5.5 explicitly flagged PASS-CHUNK-VOICE-RISK
  / seminar-risk; the Phase 1 brief carried the flag. Screen-writer honored WATCH-1 (concrete
  named death) but authored the 4 argument-spine bones as abstract-arrival / cognitive-object
  forms. Three process questions: (1) is this the gate working as intended? (2) is there a
  Phase 1 brief-discipline gap for argument-class chapters? (3) is EVENT-NOT-CONCRETE at
  risk of over-firing on interior/relational axis-move chapters?

context: |
  source_report: active-project/staff/auditor/write-b01c07-bonegate.md
  source_verdict: FAIL (6 HARD)
  gate_path: .claude/commands/and-write.md#phase-6
  Chapter: HINGE, discursive-argument content, PASS-CHUNK-VOICE-RISK / seminar-risk.
  What passed: WATCH-1 (Wenna Cobb concrete in dialogue), dialogue/continuity/grounding/
  opposing-force, all three scene-ratios above 25% concrete floor, s02+0.5 tether-move at
  n10 (concrete). What failed: 4 spine bones at the argument-middle (s02n06/n07, s03n04/n09),
  all abstract-arrival or cognitive-object form, two carrying the chapter's axis-moves.
  PROP-0023 (open, untriaged): targets Phase 4.6 apparatus-dominant whole-chapter false-ALIVE;
  structurally distinct from c07 argument-spine interiority failure.

options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0024

basis: |
  Content-vs-process discrimination: the gate is working as intended (Q1 = yes, gate caught
  the right failure). The over-fire risk (Q3) is not real — the bone-gate report's criteria
  fields confirm concrete witnessing of relational/interior axis-moves is achievable without
  physical-prop invention. The process gap is Q2: the Phase 1 brief carries the PASS-CHUNK-
  VOICE-RISK flag as risk context but does not translate it into a bone-authoring constraint
  for argument-spine positions. The screen-writer received the risk but not the constraint.
  The constraint is enumerable (abstract-arrival form prohibited; cognitive-object form
  prohibited; prescribed concrete alternatives for thesis-reception, evaluative-turn,
  relational-axis-move, argument-completion positions). S-cost modify to Phase 1 step 2.
  Proposing at first occurrence because: mechanism is precisely discriminated; gap is a spec
  omission not a taste call; fix is writable now; PASS-CHUNK-VOICE-RISK is already the
  detection predicate.
  Not merged into PROP-0023: different failure class (argument-spine interiority vs.
  apparatus-dominant whole-chapter), different target (Phase 1 brief vs. Phase 4.6 threshold),
  different command phase.

rationale: |
  The three process questions answered:
  Q1 (gate working as intended?): yes. EVENT-NOT-CONCRETE fired correctly on 4 bones; both
  SUBSTANCE-FLAT findings are the same 2 bones; root cause is abstract-subject / cognitive-
  object SVO form on the argument-progression spine. The gate caught the right failure class
  precisely. Revise cycle routes correctly. This is a successful upstream catch requiring one
  revise cycle on first argument-chapter encounter — not a gate miscalibration.
  Q2 (Phase 1 brief gap?): yes. The seminar-risk / PASS-CHUNK-VOICE-RISK flag enters the
  Phase 1 brief as risk context but the brief has no explicit constraint for how argument-spine
  bones must be authored. The screen-writer understood the WATCH items (honored WATCH-1
  faithfully) but defaulted to abstract-arrival form for the argument-progression events —
  the most intuitive authoring choice for "the thesis lands on Taylor" that is precisely the
  prohibited form. The Phase 1 step 2 SVO discipline block names the schema-level interiority
  prohibitions but does not name the canonical argument-chapter evasion (abstract-arrival /
  cognitive-object form). This is an authoring-time constraint the screen-writer can apply
  proactively; the spec does not currently give it to them.
  Q3 (over-fire risk?): no. Bone-gate report criteria fields enumerate concrete-witnessing
  alternatives for every failing bone: enacted physical postures, speech bones with concrete
  objectives, leave-taking beats, stillness-against-pressure forms. For relational/interior
  axis-moves on argument chapters, concrete witnessing is achievable through operational and
  relational correlates without inventing physical props the chapter does not have.

trade-off: |
  Proposing at first occurrence vs. waiting for recurrence: the argument-class constraint is
  enumerable and precise now; waiting for recurrence means another argument-chapter revise
  cycle on the same 4-bone failure mode that the Phase 1 brief could have prevented. The
  guard against premature proposal (one-off taste call) does not apply here: the failure mode
  is structural (schema-classified HARD findings), the mechanism is precisely named, and the
  fix is a spec addition not a threshold calibration.

follows: DEC-0050
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no
