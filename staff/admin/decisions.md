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

---

## DEC-0052 | 2026-05-30 | SLOW (user-proxy)

question: |
  b01c07 /and-write has failed the substance bone-gate TWICE. Revise made it worse (7 HARD from 6).
  The chapter is an argument chapter — two people talking at a sept corner; moving axes are
  RELATIONAL/INTERIOR. Two attempts could not produce schema-clean concrete SVOs for the interior
  argument beats. Diagnostic: the discriminator between PASS and FAIL is the VERB being
  physical-observable, not the object being fully concrete (attempt-1's "taylor stays in the
  argument" PASSED; "the argument completes" FAILED). Disposition: (A) tightly-constrained 3rd
  recast with hard form constraints derived from auditor fault reasons + hard cap of one attempt
  then escalate; (B) escalate to human now as a design-tension question; (C) checkpoint and defer
  c07 given session length.

context: |
  Attempt 1 (38-bone decomposition): FAIL, 6 HARD — 4 argument-spine interiority bones
  (FAULT-FORM-INTERIORITY / EVENT-NOT-CONCRETE). WATCH-1 dialogue, speech bones, grounding all
  PASSED.
  DEC-0051 / PROP-0024: gate working correctly; over-fire NOT real; concrete-witnessing alternatives
  exist via operational/relational correlates. Phase 1 brief gap is the process change proposed.
  Attempt 2 (revise: 8 audience-deletes + recast 4 HARD bones to concrete SVOs): FAILED WORSE —
  7 HARD. Screen-writer's recasts produced NEW schema violations: holds-license gaze violation,
  multi-subject + holds-on-abstraction, interiority + modifier, 4 NEW HARDs from advisory recasts
  ("stand in the lane cold" multi-subject, "carries the open account", "holds the answer back",
  "sets the answer aside"). Only 2 of ~7 recasts cleared.
  Key diagnostic: "taylor stays in the argument" PASSED (physical-positional verb; stays);
  "the argument completes" FAILED (cognitive-object). Discriminator is verb physicality, not
  object concreteness. Path exists: fold the interior moving-beats onto physical-observable-verb
  bones (faces/stays/steps/sets-down/enters/leaves/speech bones).
  Session is long. PROP-0024 is open-untriaged.

options: |
  A: Tightly-constrained 3rd recast. Brief contains HARD form constraints from auditor fault
     reasons: single subject only; physical-observable verb only (faces/stays/steps/turns-the-body/
     enters/leaves/sets-down — NOT holds-on-abstraction, NOT cognitive verbs); no prepositional/
     adverb modifier tails; speech bones are concrete (use them). Witness axis-moves via
     physical-observable-verb bones (pol-reg +0.3 ← "taylor faces halvard"; soc-tether +0.5 ←
     "taylor stays at the sept-corner"). HARD cap: ONE attempt; if it fails, escalate to human.
     Cost: ~2 dispatches.
  B: Escalate to human now. Two failures + recast-worse is evidence in-loop fix isn't converging.
     The gate's concrete-SVO requirement vs. an argument-chapter relational/interior axis may be a
     design question requiring principal judgment. Costs 1 interruption.
  C: Checkpoint and defer c07. Leave at "scened + decomposition-failed-gate"; clean handoff;
     resume later (possibly after PROP-0024 triage). Costs: c07 stays incomplete this session;
     saves session budget.

decision: Option A — tightly-constrained 3rd recast with one-attempt hard cap, then escalate.

basis: |
  methodology:3a (reversibility — A preserves optionality; if it fails, escalation happens at
  the same cost B would have cost now, minus ~2 dispatches; B burns the escalation interrupt without
  trying the bounded path) + methodology:3b (cost — A is cheaper than B when the bounded path has
  a clear diagnostic) + goal:1 (pipeline correctness — DEC-0051 / PROP-0024 already confirmed
  concrete-witnessing alternatives exist; the physical-observable-verb discriminator is specifically
  from the passing attempt-1 example "taylor stays in the argument"; the path is not untested) +
  methodology:3d (optionality — A is B with a first attempt; B is A minus the attempt)

rationale: |
  Three reasons option A is right over B and C at this moment.

  1. THE DIAGNOSTIC IS CONCRETE AND VALIDATED. Attempt 1 itself produced a passing example of the
     exact form needed: "taylor stays in the argument" — physical-positional verb (stays), concrete
     actor (taylor), semi-abstract object (the argument) — PASSED. "The argument completes" (no
     actor, cognitive-object, abstract-subject) — FAILED. The discriminator is not ambiguous: it
     is verb physicality. The reason attempt 2 failed worse is that the screen-writer's recast
     defaulted to holds-on-abstraction verbs (holds/carries/sets-on-abstraction) and modifier
     chains — the exact same class of errors, just relabeled. The fix is not architectural; it is a
     brief-discipline constraint the screen-writer did not have. Option A gives that constraint
     explicitly: single subject; physical-observable verb only; verb list enumerated; modifier
     prohibition explicit; use speech bones for the thesis/argument-complete events. This is a
     qualitatively different brief than attempt 2's, which lacked these form constraints.

  2. B IS PREMATURE WITHOUT TRYING THE BOUNDED PATH. Escalating to the human requires the claim
     that the gate's concrete-SVO requirement is incompatible with argument-chapter interior axes.
     DEC-0051 explicitly resolved this: "concrete witnessing of relational/interior axis-moves is
     achievable without physical-prop invention." The auditor's own report enumerated per-bone
     alternatives (enacted physical postures, speech bones with concrete objectives, leave-taking
     beats, stillness-against-pressure forms). The evidence base says the path exists. Escalating
     before a correctly-briefed attempt would surface a problem that does not yet exist in evidence.
     The human's likely response to B would be "try it with the correct form constraints first."
     Option A IS that attempt. B should follow A if A fails.

  3. C IS STRICTLY WORSE THAN A. Deferring saves ~2 dispatches at the cost of leaving c07 in
     decomposition-failed state requiring a cold-session resume — which adds orientation cost.
     The physical-observable-verb diagnostic is live and clear in this session's context. Running
     A now costs ~2 dispatches; running A next session costs ~2 dispatches + context reconstruction
     overhead. C has no advantage over A unless the session is critically budget-constrained, which
     the caller flagged as a concern but not a hard block.

  BRIEF CONSTRAINTS FOR ATTEMPT 3 (mandatory, verbatim for the screen-writer):
  - Single named actor per bone SVO. No multi-subject ("taylor and halvard" prohibited).
  - Verb must be physical-observable: faces / stays / steps / turns (body, not argument) / enters /
    leaves / sets-down (physical object) / reaches / leans / looks / speaks / waits. NOT: holds-on-
    abstraction (holds the silence, holds the answer), carries-abstraction, sets-on-abstraction,
    cognitive verbs (considers, weighs, accepts, completes, receives).
  - No prepositional/adverb modifier tails in the SVO text. "taylor faces halvard" not "taylor
    faces halvard across the sept-corner stone."
  - Speech bones are concrete and authorable. Use them for the thesis-lands and argument-completes
    events. "halvard speaks the thesis to taylor" is concrete. "taylor stays at the sept corner"
    witnesses axis-move without cognitive-object form.
  - Axis-move witnesses: pol-reg +0.3 and soc-tether +1.0 must be witnessed by physical-observable-
    verb bones per the above. "taylor stays at the sept corner" form PASSED in attempt 1 — that
    form is the template.
  - On attempt fail (any HARD at Phase 6 after this brief): STOP. Do not revise again in this
    session. Surface a clean checkpoint and escalate to human.

  ONE-ATTEMPT CAP is mandatory. If attempt 3 fails, the question is genuinely architectural — the
  concrete-SVO requirement vs. this specific chapter's interior substance contract requires a
  principal judgment call that admin cannot make from goals + LTM. That escalation is not premature
  after a correctly-briefed third attempt.

trade-off: |
  Option A vs B: B costs the same escalation interrupt at session-close without the bounded attempt.
  If A succeeds (which the diagnostic evidence suggests it should), B was unnecessary. If A fails,
  escalation happens at A's cost (2 dispatches) + B's cost — a small premium over B directly. The
  expected value calculation favors A because the probability of success on a correctly-briefed
  form-constrained brief (with the exact discriminating example from attempt 1 available) is non-
  trivial. Methodology:3a and 3b both favor A.

  Option A vs C: 2 dispatches now vs cold-resume later + same 2 dispatches. A is strictly better
  unless session is hard-limited. The caller flagged session length as a concern, not a hard block;
  2 dispatches is minimal additional spend.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0053 | 2026-05-30 | SLOW (user-proxy)

question: |
  /and-review bones b01c07 returned aggregate FAIL (3 HARD SVO-form findings) after a premature
  verdict write committed by the main session. Routing decision: (A) /and-write b01c07 revise
  (surgical recast of flat15/22/16), then re-run /and-review bones, then resume cascade; (B)
  accept the 3 forms as bone-gate-passed and proceed to /and-facets past the HARD notes; (C)
  escalate to human.
  Sub-questions: 1-attempt cap for the revise? Acceptable witness forms for soc-tether +0.5
  on argument-staying bones? Process note on the premature-verdict error?

context: |
  The 3 HARD findings per auditor:
    - flat22 "taylor-hebert-kl-122ac stays at the sept-corner" [MOVING soc-tether +0.5]:
      PP modifier "at the sept-corner" — bones.schema.md line 57 bans PP modifiers of place.
      Unambiguous violation.
    - flat15 "taylor-hebert-kl-122ac stays in the argument" [MOVING soc-tether +0.5]:
      PP modifier "in the argument" + "the argument" as abstraction-as-object. Defensible HARD.
    - flat16 "septon-halvard-flea-bottom holds the silence" [HELD]:
      "the silence" is abstraction-as-object under holds-verb. Held bone, no Δ-arithmetic impact.
  flat15 and flat22 are the sole carriers of soc-tether +1.0 for the chapter.
  DEC-0052 authorized attempt-3 brief with "taylor stays at the sept corner" as the template
  form for soc-tether witnessing — that exact form is now flagged HARD for the PP modifier.
  The /and-write Phase 6 bone-gate passed all three forms on rev2. /and-review bones caught them
  independently — the mandatory gate working as designed.
  Premature-verdict error: main session wrote aggregate verdict "PASS-WITH-NOTES /and-facets
  cleared" before the auditor fork returned. Record corrected at commit 8c69892.

options:
  A: /and-write b01c07 revise — surgical recast of flat15/flat22/flat16 to PP-free/concrete-object
     forms. Re-run /and-review bones. Resume cascade. Honors schema + gate.
  B: Accept 3 forms as bone-gate-passed; proceed to /and-facets knowingly past schema-violating bones.
  C: Escalate to human — reopens DEC-0052 territory; process error may warrant human attention.

decision: |
  Option A. Route to /and-write b01c07 revise (surgical: flat15/flat22/flat16 only).
  1-attempt hard cap then escalate to human.
  Acceptable witness forms for soc-tether +0.5: bare intransitive "taylor stays" (no PP,
  no object) or reassign one Δ to a speech bone. flat16: "septon-halvard-flea-bottom waits"
  or equivalent bare intransitive. No PP modifiers; no abstraction-as-direct-object.
  Process note on premature-verdict error: operator/session discipline failure; no spec or
  process change warranted — the downstream gate caught the pass-through as designed.

basis: |
  goal:1 (pipeline correctness — option B knowingly ships schema-violating bones; that sets
  precedent that /and-review HARDs are advisory, which erases the gate's authority) +
  methodology:3a (reversibility — A is targeted 3-bone revise; B is irreversible precedent) +
  DEC-0052 (1-attempt-cap-then-escalate is the established protocol on this chapter's
  argument-bone difficulty)

rationale: |
  Option B is not viable. The /and-review bones gate exists as an independent SVO-form check
  on /and-write's Phase 6. Knowingly proceeding past its HARD findings because Phase 6 passed
  them would erase the gate's function — the system caught three schema violations precisely
  because the independent re-fire is separate from Phase 6. Accepting them as "bone-gate-passed"
  (a term that belongs to Phase 6, not /and-review) is a category error that would corrupt
  downstream facets and stitch. Schema line 57 is not ambiguous on PP modifiers of place.

  Option C is not warranted. The schema is unambiguous; the recast options are clear; the
  DEC-0052 precedent already governs the 1-attempt-cap protocol. This is not a design question
  requiring the principal — it is an operational recast with clear form constraints. The
  principal's attention should be reserved for when the attempt fails (at which point the claim
  is genuinely architectural: PP-ban + abstraction-ban + argument-interior content = irreconcilable
  constraint on soc-tether witnessing).

  Form guidance for the revise brief (mandatory):
    flat22: "taylor-hebert-kl-122ac stays" (bare intransitive) witnesses soc-tether +0.5.
            Zero PP tail. This form is distinct from attempt-3's "stays at the sept-corner"
            (which added the HARD PP) — remove the location phrase entirely.
    flat15: "taylor-hebert-kl-122ac stays" (same bare form, different scene-beat witnesses
            the second +0.5). Two separate "stays" bones at different beats is not duplication;
            they witness distinct moments of commitment. Alternatively, reassign one +0.5 to
            a speech bone ("taylor speaks to halvard" with soc-tether +0.5) if the screen-writer
            judges two bare-stays too close in a 3-bone window.
    flat16: "septon-halvard-flea-bottom waits" or "septon-halvard-flea-bottom stands" or
            "septon-halvard-flea-bottom turns" — any bare physical-positional intransitive.
            HELD bone; only form correction required; Δ is already 0.

  Hard prohibitions for all three recasts: no "at X" / "in X" / "with X" PP tails; no
  abstraction-as-direct-object (the silence / the argument / the answer / the offer as
  direct objects of holds/carries/sets). Intransitive or speech-bone forms are the safe lane.

  DEC-0052's brief explicitly nominated "taylor stays at the sept-corner" as the soc-tether
  template. That brief was produced under the diagnostic that "stays" was the physical verb
  carrying the +0.5 — correct. The schema violation was the PP modifier, not the verb. The
  lesson distilled: verb physicality was the right discriminator; location PP adds a schema
  violation even when the verb passes. "taylor stays" (no location) is the clean form.

  Premature-verdict note: the main session wrote an aggregate verdict before all reviewer
  forks returned. The corrective commit (8c69892) properly restores the record. No PROP
  warranted: (1) operator/session error, not a spec gap; (2) the gate architecture already
  handles it — /and-review bones is designed to catch what Phase 6 misses and did; (3) a
  "wait-for-all-forks" spec note to /and-review would be redundant with the gate's own
  precondition ordering (the gate IS the catch). The corrected commit is the resolution.

trade-off: |
  Option A vs B: B saves ~4-6 dispatches at the cost of the gate-authority contract and
  downstream contamination. Cost of B's precedent is unbounded across future chapters.
  Option A vs C: C costs principal attention on a question admin can answer from schema line 57
  + prior rulings. If the 1-attempt revise fails, C fires at that point — the correct moment.
  1-attempt cap: narrower sub-problem than DEC-0052 (3 bones, clearer constraints, "stays" bare
  form validated by being the near-miss that almost passed). If the screen-writer cannot produce
  3 schema-clean witnesses in one attempt with this brief, that is the architectural claim.

follows: DEC-0052
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0054 | 2026-05-30 | SLOW (process-critic)

question: |
  /and-review bones b01c07 FAIL: 3 HARD SVO-form faults (flat15 PP "in the argument",
  flat22 PP "at the sept-corner", flat16 holds-abstraction). All three passed the /and-write
  Phase 6 bone-gate on rev2. Process questions: (1) is there a recurring gap where Phase 6
  trusts the author's form self-assessment rather than re-deriving it? (2) does a mechanical
  PP/abstraction-object lint belong in /and-write Phase 6? (3) does the premature-verdict
  commit warrant a process change?

context: |
  source_report: active-project/staff/reviews/bones-b01c07-2026-05-30.md
  source_verdict: FAIL (3 HARD: flat15/22/16)
  gate_path: .claude/commands/and-review.md#bones
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]

  Key facts:
  - All three HARD SVO-form violations are mechanical (PP-of-place, PP-of-abstract-location,
    abstraction-as-object) banned by bones.schema.md lines 57/60.
  - Rev2 draft explicitly self-asserted "unchanged PASS" (flat15) and "exact form that passed
    at attempt 1" (flat22) for the two MOVING bones. Phase 6 auditor accepted these annotations
    without re-deriving from raw text.
  - The DEC-0052 one-attempt cap contributed context pressure but is independent of the spec gap.
  - Premature aggregate verdict was committed (6e6f0f6) before the auditor fork returned; corrected
    at 8c69892. DEC-0053 noted this was operator/session error, not a spec gap — no process change.
  - /and-review bones re-fire caught all three. The gate-chain functioned as designed.

options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0025

basis: |
  Content-vs-process discrimination Q1 (recurring self-assessment bypass?): yes, the gap is
  real. The Phase 6 brief instructs "classify each bone as CORRECT or FAULT-{class}" but does
  not instruct the auditor to re-derive form from raw text independently of author annotations.
  In revise mode, when the author labels unchanged bones "unchanged PASS" or cites prior-pass
  status, the auditor's independent classification is at risk of collapsing into annotation-
  acceptance. This happened: flat15 and flat22 were accepted on their annotations, not re-
  derived. The gate that should have caught them (Phase 6) did not; the next gate (bones re-fire)
  did. A one-sentence re-derivation instruction in the Phase 6 brief closes the gap.

  Q2 (mechanical PP lint belong in Phase 6?): yes, optionally. The bones.schema.md form rules
  are mechanical enough to admit a regex pre-screen (preposition + noun-phrase on MOVING bones;
  abstraction-noun objects). This would make re-derivation self-enforcing. Surfaced in the
  proposal but deferred to principal on whether to implement as a formal sub-step vs. an
  auditor-dispatch note.

  Q3 (premature verdict commit): DEC-0053 correctly disposed this as operator/session error, not
  a spec gap. /and-review already has the downstream catch architecture; the /and-review bones
  re-fire IS the gate that caught the pass-through. Adding "wait for all forks" to the spec would
  be redundant with the gate's own ordering. OK — no proposal warranted.

  Prior proposals check: PROP-0009 (Phase 1 cadence-reference guidance) and PROP-0024 (Phase 1
  argument-spine constraint) both target Phase 1. PROP-0007 (Phase 1 compound-noun economy +
  Phase 6 SIGNAL table) targets Phase 1 step 5 and a SIGNAL addition. None targets Phase 6
  auditor re-derivation discipline. No prior open proposal matches target.path +
  change_type for this specific gap. Proceeding to author.

  Recurrence count: 1 first cross-chapter instance. Non-catastrophic (caught by /and-review
  bones). Proposing at first occurrence because: (a) spec omission is precisely discriminated;
  (b) the bypass risk exists on every revise cycle where author labels unchanged bones; (c) S-cost.

rationale: |
  The /and-review bones subcommand is designed to be the independent re-fire that catches what
  Phase 6 misses. That is exactly what happened here — system functioned as designed. The
  process question is whether Phase 6 should have caught these forms first (avoiding the re-fire
  loop). It should: bones.schema.md lines 57 and 60 are unambiguous mechanical rules the auditor
  can apply from raw text in under two seconds per bone. The bypass was the author's self-
  annotation reaching the auditor as a pre-classified verdict rather than as a raw SVO to verify.

  The fix is not a new gate — it is a re-derivation instruction on the existing gate. The
  instruction is: "treat the raw bone text as the evidence; treat author annotations as noise."
  This is S-cost: one paragraph added to the Phase 6 auditor brief, at the opening of the Per-
  bone verification section, before the moving/held/chatter sub-sections.

trade-off: |
  Proposing at first occurrence vs. waiting for recurrence: the bypass risk is structural (exists
  on every revise cycle) and the fix is S-cost. The "wait for recurrence" rule exists to prevent
  premature promotion of taste calls; this is not a taste call. The bones.schema.md form rules
  are mechanical. The escape happened because the brief lacked one instruction. Cost of not
  proposing: the same bypass is possible on every future revise cycle where the author labels
  unchanged bones with prior-pass annotations.

  On the premature-verdict process question: the correct answer is OK. The gate architecture
  already ensures correctness — /and-review bones is the designed catch, and it caught. Adding
  a spec rule to the review command about fork-return ordering would address the correct-but-
  early commit artifact, not the gate gap. The correction commit is sufficient.

follows: DEC-0053
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0055 | 2026-05-31 | SLOW (process-critic)

question: |
  /and-facets b01c07 Phase 5b cycle-1 FAIL (7 PASS / 4 FAIL); resolved at cycle-2 PASS.
  Three patterns to evaluate:
  (1) Dialogue substance fault (no-winner invariant in argument chapter) surfacing only at
      Phase 5b — is there a process gap where argument-chapter substance invariants aren't
      checked at the R2 dialogue-judge stage?
  (2) Fixer-introduced schema-invalid sensory modality (proprioceptive, not in closed enum
      sound|light|smell|thermal|humidity|pressure|tactile) caught at cycle-2 Phase 5 audit
      but not at cycle-1 Phase 5 audit — is there a fixer brief gap or auditor scope gap?
  (3) Grounding-ledger satisfied_by stale on fixer recast (the entry the ledger pointed to
      was recast, making the satisfied_by reference stale) — is there a process gap in the
      fixer protocol for ledger-coupled records?

context: |
  source_report: active-project/staff/audience/facets-audience-gate-r1.md
  source_verdict: FAIL (7/4; remediated cycle-2 PASS; 2 cycles, cap not reached)
  gate_path: .claude/commands/and-facets.md#phase-5b
  secondary_gate_paths: [.claude/commands/and-facets.md#phase-4.6,
                         .claude/commands/and-write.md#phase-1.5]

  Chapter class: HINGE/ARGUMENT, PASS-CHUNK-VOICE-RISK.
  Pattern 1 detail: dialogue-taylor @19 "She's why I'm in Flea Bottom at all" — two independent
    reviewers (dark-fantasy, worm-canon) converged on SAME finding: the line converts Wenna Cobb's
    death from cost to self-justification, breaking the chapter's no-winner invariant. The
    dialogue-writer (Phase 1.5) and R2 dialogue-judge (Phase 3) both passed it. Phase 5 mechanical
    audit passed it (no card-fence violation). Phase 5b audience found it.
  Pattern 2 detail: cycle-1 fixer recast sensory:4@22 to modality `proprioceptive` (not in closed
    enum). Cycle-1 Phase 5 re-audit did not catch it. Cycle-2 Phase 5 re-audit caught it; fixer
    corrected to `pressure`. Gate ordering worked but one cycle late.
  Pattern 3 detail: grounding-ledger grd-002 entry's satisfied_by pointed to sensory:4@22. When
    the fixer recast sensory:4@22, satisfied_by became stale (pointing to an entry that now has
    different content). The ledger itself is a new mechanism (PROP-0022; first live chapter).

options: n/a (process-critic mode)

decision: |
  PROCESS-CHANGE-PROPOSED PROP-0026 (Pattern 1 — dialogue R2 brief lacks argument-chapter
    substance invariants);
  OK-FIRST-OCCURRENCE-MARKER (Pattern 2 — fixer schema-invalid modality);
  PROCESS-CHANGE-PROPOSED PROP-0027 (Pattern 3 — grounding-ledger satisfied_by stale on
    fixer recast)

basis: |
  Pattern 1 — PROP-0026:
    Content-vs-process discrimination: could a stricter version of the existing R2 dialogue-judge
    gate have caught this? Yes — if the R2 judge brief carried chapter-class substance invariants
    (no-winner, cost-vs-justification prohibition on argument chapters), the judge would have
    classified the line as a substance fault, not just evaluated Q1 (card-affirmative) + Q2
    (card-fence). The rubric's Q2 is limited to behavior-card fences (forbidden vocabulary,
    Earth-Bet fence, monument rules). The no-winner invariant is a chapter-substance contract
    property, not a behavior-card fence. There is no existing gate between Phase 1.5 dispatch and
    Phase 5b that checks dialogue content against chapter-level substance contracts.
    Distinct from PROP-0024 (argument-spine bone-authoring at Phase 1 step 2) — that targets
    what the bones record; this targets what dialogue says relative to chapter-substance invariants.
    Different gate (Phase 3 R2 judge brief vs. Phase 1 screen-writer brief), different agent
    (dialogue-writer vs. screen-writer), different constraint source (chapter substance contract vs.
    bone schema). First occurrence, non-catastrophic. Proposing at first occurrence because: the
    gap is a precise spec omission (argument-chapter invariants not in the R2 brief); the failure
    class is structurally guaranteed on any argument chapter with a no-winner / cost-vs-justification
    invariant; the fix is S-cost (one constraint block added to Phase 3 R2 dialogue-judge dispatch
    brief conditioned on chapter_class or PASS-CHUNK-VOICE-RISK predicate).

  Pattern 2 — OK, first-occurrence marker:
    The Phase 5 STRUCTURAL audit class covers schema/format/integrity per facet.schema.md. The
    closed modality enum (sound|light|smell|thermal|humidity|pressure|tactile, line 88) is an
    explicit schema constraint. The cycle-1 Phase 5 audit missed it; cycle-2 caught it. Gate
    ordering ultimately worked (non-catastrophic). Two candidate fix sites: (a) fixer brief
    pre-write validation for ADD/RECAST operations on schema-enum fields; (b) auditor STRUCTURAL
    class explicit enumeration of the sensory modality closed enum. Standard first-occurrence hold
    applies — non-catastrophic, gate worked (one cycle late). Mark first occurrence; if the same
    class (fixer introduces schema-invalid enum value; Phase 5 auditor misses it cycle-1) recurs
    on any field, promote to PROP with change_type: modify on both the fixer brief and the
    auditor STRUCTURAL scan spec. The candidate fix is small and known; hold does not lose it.

  Pattern 3 — PROP-0027:
    Content-vs-process discrimination: the grounding-ledger satisfied_by coupling is a new
    mechanism (PROP-0022, first live chapter). Any fixer modification to a sensory entry that
    a grounding-ledger line references via satisfied_by creates a stale reference — this is
    deterministic. The fixer dispatch protocol at Phase 5b remediation does not include a
    coupled-record-update step for the grounding-ledger. The fixer brief tells the fixer what
    to fix (facet callouts) but not to check whether any modified entry is a grounding-ledger
    satisfied_by target. First occurrence, non-catastrophic. Proposing at first occurrence because:
    the failure is deterministic (every fixer recast of a ledger-referenced entry produces stale
    satisfied_by); the ledger mechanism is brand-new (no prior chapter tested this coupling);
    the fix is S-cost (one coupled-record-update instruction in the Phase 5b fixer dispatch brief).

rationale: |
  Three structurally distinct patterns. Pattern 1 is a gate-absence for dialogue + argument-chapter
  substance contracts (no existing gate covers it). Pattern 2 is a Phase 5 STRUCTURAL scope
  narrowness (or fixer discipline gap) — first occurrence, non-catastrophic, gate ultimately
  worked. Pattern 3 is a fixer-protocol ledger-coupling gap — deterministic recurrence given the
  new ledger mechanism.

  Pattern 1 and Pattern 3 pass the first-occurrence override criteria: both have deterministic
  recurrence mechanisms, both have precisely-named fixes, both are S-cost. Pattern 2 is held at
  first occurrence: gate did catch it (one cycle late), the fault class requires two-agent
  coincidence (fixer introducing enum error + auditor structural scan missing it cycle-1), and
  the candidate fix can be applied on second occurrence without loss.

trade-off: |
  Proposing PROP-0026 at recurrence_count=1: justified by deterministic recurrence on any argument
  chapter with substance invariants not in behavior-card fences. Cost of hold: the same miss
  recurs at c08+ if c08 is also argument-class. The R2 dialogue-judge is dispatched at EVERY
  /and-facets invocation on argument chapters; the brief gap fires every time.

  Holding Pattern 2: justified because the Phase 5 STRUCTURAL scan already nominally covers
  schema integrity. The gap may be an auditor execution miss (not a spec gap), or a scope
  narrowness. Second occurrence will discriminate which. Cost of hold: at most one future cycle
  of late-catch (same pattern, non-catastrophic).

  Proposing PROP-0027 at recurrence_count=1: justified because the grounding-ledger mechanism
  is new and untested in prior chapters. The satisfied_by coupling was not part of the overhaul
  design's tested paths. No prior chapter established whether the fixer updates the ledger on
  recast.

first_occurrence_markers:
  - Pattern 2 (fixer schema-invalid enum + Phase 5 STRUCTURAL scope miss):
      first_occurrence: b01c07 sensory:4@22 recast to `proprioceptive` by cycle-1 fixer;
        cycle-1 Phase 5 audit missed it; cycle-2 Phase 5 audit caught it + fixer corrected to `pressure`
      candidate_fix_on_recur:
        A: fixer brief — pre-write validation step for ADD/RECAST on schema-enum fields (check field
           value against schema's declared closed enum before committing)
        B: auditor STRUCTURAL scan — add explicit sensory modality enum validation to the scan spec
           (enumerate each modality field value against `sound|light|smell|thermal|humidity|pressure|tactile`)
      recur_threshold: 2 occurrences triggers PROP; candidate_fix target is both A + B (small, paired);
        single-site fix (fixer brief) is sufficient if the STRUCTURAL scan is already nominally in scope
        and the miss was execution-variance not spec-gap

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0056 | 2026-05-31 | SLOW (user-proxy)

question: |
  Principal invoked `/and-write b01c06 revise --from-signals` today (2026-05-31). This is the
  depth pass deferred by DEC-0050. Two prior preconditions from DEC-0050 are (nominally) unmet:
  (1) PROP-0023 is still open/untriaged; (2) `--from-signals` flag is mechanically wrong-targeting
  (Phase-6 SIGNALs ≠ cold-read AIRLESS bones). Disposition: P1 (proceed now, interpret as depth-pass
  intent) or P2 (hold pending PROP-0023 triage, escalate)?

context: |
  DEC-0048: b01c06 shipped PASS-WITH-DEPTH-PASS-REQUIRED. COMPLETENESS PASS, READABILITY AIRLESS.
  Memory carries depth_pass_pending: true, note "de-abstract @16-@21; escalation clause: next cold-read
  still AIRLESS-on-central-event → FAIL/re-decompose."
  DEC-0050: Deferred depth pass to before book-close. Conditions: PROP-0023 triaged AND correct brief
  specified (cold-read-signal-driven, targeting @16-@21 apparatus SVOs). Brief specified verbatim in
  DEC-0050's rationale. PROP-0023 triage explicitly named as precondition.
  Status today: b01c07 is written and shipped (DEC-0050's "proceed to b01c07" leg done). PROP-0023
  status: open, triaged_at: null. Principal typed the command explicitly today.

options: |
  P1: Proceed. Treat explicit invocation as override of deferral. Interpret --from-signals as
      depth-pass intent. Run authorized depth pass: scene-s03-scoped revise, de-abstract @16-@21,
      brief driven by cold-read AIRLESS + ABSTRACTION-DOMINANT signal set. Re-cascade /and-facets
      + /and-stitch. Honor DEC-0048 escalation clause. ~40 dispatches, uncertain outcome.
  P2: Hold. PROP-0023 untriaged; DEC-0050 named it as precondition; escalate to principal to confirm
      override or triage PROP-0023 first.

decision: P1 — Proceed. Interpret explicit invocation as override of the DEC-0050 deferral.

basis: |
  explicit-principal-invocation (strongest signal, overrides prior deferral) + methodology:3d
  (optionality — the remaining "precondition" is a form-stamp on a proposal whose substantive
  content is fully specified in DEC-0050; deferring further consumes a dispatch without adding
  information) + goal:1 (pipeline correctness — depth pass IS the correct authorized repair;
  running it is not acting on an untriaged proposal, it is executing a scheduled content action)

rationale: |
  DEC-0050's two preconditions examined in light of today's state:

  PRECONDITION (1): PROP-0023 triaged.
  PROP-0023 prescribes a modification to /and-facets Phase 4.6's ALIVE verdict criteria for
  apparatus-dominant chapters — a FUTURE-GATE change. Running the b01c06 depth pass is NOT
  implementing PROP-0023. The depth pass is a content action on one chapter; PROP-0023 is a
  process change that would canonize routing for future chapters. These are separable actions.
  DEC-0050's concern was that "acting on PROP-0023's logic" before triage would be "premature
  implementation of an un-triaged proposal." That concern was valid when the brief was unspecified.
  But DEC-0050 itself wrote the brief: "cold-read-signal-driven, targeting @16-@21 apparatus SVOs
  specifically — ABSTRACTION-DOMINANT + GROUNDING-REQUIRED + Phase 4.6 re-reviewer scene notes."
  The brief is no longer ad-hoc; it is in the decision record. The remaining "precondition" is
  purely a form-stamp — triaging PROP-0023 would not change the brief one word. Blocking on it
  is blocking on a form-stamp.
  Additionally: the principal's explicit invocation today constitutes implicit authorization of the
  repair action PROP-0023 would have canonized. The triage question for PROP-0023 (whether to
  modify the gate for future chapters) can and should proceed in parallel or as a tail step.

  PRECONDITION (2): Correct brief.
  This IS satisfied. DEC-0050's rationale section contains the complete brief:
    - Scope: scene s03, bones @16-@21 (apparatus-dominant accounting middle)
    - Target: de-abstract apparatus-verb SVOs to concrete actor-verb-object forms
    - Signal set: cold-read AIRLESS findings + ABSTRACTION-DOMINANT SIGNAL from Phase 6 +
      GROUNDING-REQUIRED entries from grounding-ledger + Phase 4.6 re-reviewer scene notes
    - Escalation clause: if next cold-read still AIRLESS-on-central-event -> FAIL/re-decompose

  FLAG INTERPRETATION (`--from-signals`):
  `--from-signals` mechanically reads Phase-6 gate_verdict.signals[], which are the wrong signals
  for this chapter (moral_legibility floor + s03 stakes-tie, not the apparatus-airless bones).
  Interpret the flag as DEPTH-PASS INTENT, not literal Phase-6-signal targeting. The depth pass
  runs as a scene-s03-scoped `/and-write b01c06 revise` with the DEC-0050 brief, NOT as a literal
  --from-signals pass that would target the wrong bones.

  DEC-0048 ESCALATION CLAUSE: remains active. If the re-stitched chapter cold-reads
  AIRLESS-on-central-event, route to FAIL/re-decompose rather than another depth pass. The
  accounting section may be abstract-by-contract; the escalation clause governs that outcome.

trade-off: |
  P1 vs P2: P2 costs one dispatch for admin to return ESCALATE + one dispatch for the principal
  to triage PROP-0023 + one dispatch for admin to receive the ruling. Net: ~3 additional dispatches
  of pure form overhead before the ~40-dispatch re-cascade begins anyway. If the principal had
  wanted to wait, they would not have typed the command today. The explicit invocation is a
  stronger signal than the prior deferral, which was made under a "brief unspecified" condition
  that no longer holds. Expected value of P1 over P2: non-trivial given the overhead cost of P2
  and the zero-information gain from the PROP-0023 triage on this chapter's brief.

  PROP-0023 TRIAGE NOTE: This decision does NOT constitute a triage of PROP-0023's proposed
  Phase 4.6 gate modification. The gate change is still open and still needs principal triage.
  Running the depth pass on b01c06 is an independent content action.

follows: DEC-0050 DEC-0048
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0057 | 2026-05-31 | SLOW (process-critic)

question: |
  /and-write b01c06 revise depth-pass Phase 6 bone-gate: HARD FAULT-FORM-NON-ACTION-VERB on
  @20 "holds the stylus" (narrow-holds-license misread; resolved in-invocation to "stills the
  hand"); 2 SIGNALs (signal-001 moral_legibility fractional-floor +0.5→+1.0; signal-002 s03
  stakes-axis tie mf=mls at 1.0) accepted-with-rationale identical to original c06 run. Does the
  process need to change?

context: |
  source_report: active-project/staff/auditor/write-b01c06-bone-gate-revise.md
  gate_path: .claude/commands/and-write.md#phase-6
  The 2 SIGNALs are identical to the original b01c06 bone-gate run, already OK-MERGED into
  PROP-0010 at DEC-0046 (recurrence_count: 2). The HARD was resolved in-invocation — no new
  proposal from the caller's framing of the gate working correctly.
  However: this is the THIRD occurrence of a holds-license misread across the project.
    Occ 1: b01c04 — "workers hold the smallfolk-hours murmur" (group-subject + abstract register;
            flagged advisory, not blocked; noted in bones-b01c04-2026-05-27.md)
    Occ 2: b01c07 — "septon-halvard-flea-bottom holds the silence" (abstraction-as-object HARD;
            caught at /and-review bones; resolved by recast; bones-b01c07-fidelity-2026-05-30.md)
    Occ 3: b01c06 revise — "holds the stylus" (non-body-part/non-pressure-resisting HARD; caught
            at Phase 6; resolved in-invocation)
  Three independent chapters, three distinct sub-type misreads of the same narrow holds license.
  The schema deny-list has one named example ("taylor holds the ledger"). The Phase 1 brief has
  no authoring-guidance on holds-license scope.

options: n/a (process-critic mode)

decision: |
  2 SIGNALs: OK-MERGED-INTO PROP-0010 (recurrence_count now 3; third chapter exhibiting the
    fractional-target-floor collision). No new proposal on signals — same disposition as DEC-0046.
  HARD (holds-license): PROCESS-CHANGE-PROPOSED PROP-0028.
  Gate working correctly on HARD: confirmed (no proposal against the gate itself).

basis: |
  Signals: ltm:DEC-0046 (prior merge into PROP-0010; same rationale; same structural artifact;
    third recurrence merges again rather than spawning a second proposal for the same upstream fix).
  HARD: recurrence-count-3 across independent chapters (Rule 11 recurrence threshold exceeded;
    first-occurrence hold is clearly released at 3) + gate-working-correctly discrimination
    (gate fires correctly; root is at authoring brief, not at the gate) + content-vs-process:
    the gate cannot structurally prevent author over-extension of the holds license — only a
    Phase 1 brief note can; change_type: modify at the authoring layer.

rationale: |
  Signals are structurally identical to those at DEC-0046: the fractional-target-floor collision
  between the +0.5 mls target and the 1.0 bone floor is deterministic. PROP-0010's upstream
  pre-flight fix is the correct closure; adding a third recurrence_ref to PROP-0010 is the
  correct update. No new gate machinery warranted.

  The holds-license misread pattern is now confirmed across three chapters with three distinct
  sub-types:
    (a) group subject + abstract-register object (c04 — pushed through advisory)
    (b) abstraction-as-object ("the silence" — c07 HARD, caught at /and-review bones)
    (c) non-body-part/non-pressure-resisting physical object ("the stylus" — c06r HARD, Phase 6)
  All three misread the holds license in different directions. The schema's deny-list example
  ("taylor holds the ledger") establishes the pattern for non-body-part physical objects but the
  author generated a parallel form despite the example. The Phase 1 brief has no positive
  instruction on holds-license scope — the author must derive the license from the schema,
  and the derivation is failing at recurrence-3.
  change_type: modify (Phase 1 brief addition; the Phase 6 gate already catches correctly); S-cost.

trade-off: |
  Proposing at recurrence_count=3: clearly past the first-occurrence hold. The three sub-types
  could be addressed by a single brief note that names both conditions exhaustively and provides
  negative examples parallel to the schema deny-list. Not proposing would allow a fourth occurrence
  on a future chapter. Expected cost of the fourth occurrence: one HARD + in-invocation cycle or
  /and-review-bones HARD + bones revise pass. The Phase 1 brief note costs S; the prevented HARDs
  cost 5-15 dispatches each on average.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0058 | 2026-05-31 | SLOW (user-proxy)

question: |
  b01c06 depth-pass re-cascade complete. Terminal Phase 9 cold-read: COMPLETENESS PASS +
  READABILITY AIRLESS (improved but still airless). DEC-0048 escalation clause fires: "next cold-read
  still AIRLESS → FAIL/re-decompose." New evidence: 0-mute prose-rationale-mute audit across 20 bones
  (every concrete rationale-named element IS staged in prose). Disposition fork: (A) FAIL →
  /and-write revise re-decompose, literal DEC-0048 clause; (B) /and-substance contract revision;
  (C) accept terminal, stamp abstract-by-contract; (D) escalate to principal.

context: |
  Depth pass ran full chain: /and-write b01c06 revise (s03 accounting de-abstracted, verdict-pause
  bone added) → /and-review bones PASS (BONES-AIRLESS-RISK CLEARED) → /and-facets (7/7 SUCCESS,
  all 10 facets ACCEPT 3-of-3) → /and-stitch (person-first voice-embodiment render).
  Terminal Phase 9 cold-read:
    COMPLETENESS: PASS — central event recovered, jeopardy present, causality tight, CONTINUE=yes,
      summary accurate. Step-2 FAIL conditions do not fire.
    READABILITY: AIRLESS — "There IS a person now… the crowd breathes" (improved vs. original);
      BUT "the moment the form arrives, the prose becomes a man describing his own bookkeeping in
      abstract nouns… the ledger metaphor is relentless… I never feel the four names as men…
      held at arm's length… the prose insists the choice was never a choice."
  0-mute audit: ZERO mutes across 20 bones with concrete rationale. Every rationale-named physical
    element (hand, stylus, board, blank field, seal) IS staged concretely in prose.
  Cold-reader's three complaints map to contract features:
    "I never feel the four names as men" → offstage victims by contract (Taylor's internal accounting)
    "inert dramatically" → no-real-choice framing IS the thesis (the ledger runs clean)
    "ledger metaphor relentless" → cold-utilitarian POV register (cond-taylor-pov-behavior)
  Project spine design-intent: "cold-utilitarian; affect suppressed not absent; theme never spoken";
    "the accuracy is the catastrophe"; "the road to hell is paved with good intentions."
  DEC-0048 escalation clause was written without the 0-mute evidence. It assumed "next cold-read
  AIRLESS" would mean de-abstraction failed. The 0-mute audit shows de-abstraction SUCCEEDED
  completely; the remaining airlessness is contract-origin.

options: |
  A: FAIL → /and-write revise re-decompose (DEC-0048 literal clause). ~40 dispatches. Hits same
     contract wall; bones already 0-mute; near-zero expected delta.
  B: /and-substance contract revision. Contract-level change; touches thesis; changes what the
     chapter is. Largest spend + principal design call required.
  C: Accept terminal. Stamp depth_pass_resolved, airlessness-abstract-by-contract. Cheapest.
  D: Escalate to principal on defect-vs-thesis-feature taste call.

decision: Option C — accept terminal; stamp depth_pass_resolved, airlessness abstract-by-contract.

basis: |
  goal:1 (pipeline correctness — the escalation clause's FAIL condition targeted a failure mode
    the 0-mute audit rules out; mechanical literalism is ruled out by DEC-0007 precedent) +
  goal:2 (cost discipline — Option A is ~40 dispatches against near-zero expected delta;
    methodology:3b applies strongly) +
  project-spine-design-intent (decisive signal: "cold-utilitarian; affect suppressed not absent;
    theme never spoken" + "the accuracy is the catastrophe" are the project spine entries for
    Taylor's accounting chapters; they confirm the cold register IS the intended effect) +
  methodology:3a (reversibility — accepting with a documented abstract-by-contract stamp is
    reversible; the principal can override; A/B are irreversible spends)

rationale: |
  The DEC-0048 escalation clause — "if next cold-read still AIRLESS → FAIL/re-decompose" — was
  written under the premise that a second AIRLESS result would mean the depth pass failed to
  de-abstract the bones. The 0-mute audit conclusively falsifies that premise: all 20 bones with
  concrete rationale have their named physical elements staged in prose. De-abstraction succeeded
  completely. The AIRLESS result persists because the chapter's contract (offstage victims, no-choice
  framing, ledger register) produces cold affect by design. This is the "abstract-by-contract" case
  DEC-0048's own trade-off note anticipated: "The accounting section may be abstract-by-contract…
  if bone-level de-abstraction is genuinely unavailable without content invention that violates the
  substance contract, that is the re-decompose case." BUT — Option A (re-decompose) is only
  correct when de-abstraction at the bone layer is still available. At 0 mutes, it is not. Running
  Option A would require inventing content the substance contract does not license.

  The defect-vs-feature question is answered by the project spine directly. The project's stated
  design intent for Taylor's POV behavior: "cold-utilitarian; affect suppressed not absent; theme
  never spoken." The project thesis: "the accuracy is the catastrophe"; "the road to hell is paved
  with good intentions." The cold-reader's specific complaints — "inert dramatically," "the prose
  insists the choice was never a choice," "held at arm's length" — are what those project spine
  entries describe. The cold ledger register working on a reader as "inert" is the intended
  phenomenology: the catastrophe of Taylor's choices is that they feel administrative. The chapter
  is achieving its thesis effect.

  DEC-0007 precedent: admin declines to apply a formal clause when the underlying mechanism is
  not the one the clause was designed to govern. DEC-0048's escalation clause governs failed
  de-abstraction. The 0-mute audit proves de-abstraction was not the failure. Applying the
  clause anyway would be the same mechanical literalism DEC-0007 blocked.

  Option B (contract revision) is not ruled out by admin — if the principal disagrees with the
  abstract-by-contract reading and wants to dramatize a victim or add a genuine choice-beat, that
  is a design direction the principal can take. But admin cannot authorize that spend unilaterally
  (human-only: architectural direction / strategic priorities). Option C is the correct default
  from goals + methodology + project spine. If the principal wants B, they direct it.

  Option D (escalate) would be correct if admin could not decide between C and the alternatives.
  The project spine design-intent is specific and decisive. The "is the cold register
  intentional?" question has a clear answer in the project documents admin has read.

trade-off: |
  Option C stamps a chapter as abstract-by-contract on the basis of admin's reading of the project
  spine. If the principal intended the accounting chapter to feel felt-rather-than-diagrammed (i.e.,
  the cold register is a rendering defect, not the thesis), admin has made a wrong call. Mitigated by:
  (a) the project spine evidence is explicit; (b) the 0-mute audit proves the bones cannot be
  de-abstracted further without contract invention; (c) the principal can override C at zero cost.
  The cost of Option A without override is ~40 dispatches with near-zero expected delta.

follows: DEC-0048 DEC-0050 DEC-0056
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0059 | 2026-05-31 | SLOW (process-critic)

question: |
  Process-critic dispatch on coldread-b01c06-2026-05-31.md (PASS-TERMINAL-DEPTH-RESOLVED).
  First depth-pass loop completion returning AIRLESS again. Key finding: 0-mute
  prose-rationale-mute audit — de-abstraction exhausted, not failed. DEC-0048 escalation
  clause (FAIL → re-decompose) was blocked by DEC-0007 anti-literalism + DEC-0058 admin ruling.
  Candidate: make the abstract-by-contract disposition a mechanical Phase 9 gate outcome
  instead of a per-chapter admin ruling.
context: |
  b01c06 depth-pass ran full chain: /and-write revise (s03 de-abstracted) → /and-review bones
  PASS (BONES-AIRLESS-RISK CLEARED) → /and-facets (7/7 SUCCESS) → /and-stitch re-cascade.
  Terminal Phase 9 cold-read: COMPLETENESS PASS + READABILITY AIRLESS (improved but persisting).
  Step 3.5 prose-rationale-mute audit: 0 mutes across 20 bones. DEC-0058 ruled Option C:
  accept terminal, depth_pass_resolved, abstract-by-contract (offstage victims + no-choice
  thesis + cold-utilitarian ledger register = project-spine commitments).
  Key structural finding: DEC-0048 escalation clause was written assuming "AIRLESS again"
  = de-abstraction failed. 0-mute audit conclusively falsified that premise. The literal
  clause would have ordered ~40-dispatch re-decompose against a contract wall.
  Gate reference: .claude/commands/and-stitch.md#phase-9 (readability-axis composition +
  depth-pass disposition). Secondary: .claude/commands/and-write.md#phase-6 (0-mute
  audit origin — ABSTRACTION-DOMINANT SIGNAL list that seeded the depth-pass targets).
  Proposals log check: no prior proposal against and-stitch.md Phase 9 depth-pass
  disposition. PROP-0023 (Phase 4.6 apparatus-dominance qualifier) is complementary
  upstream; different target, different phase.
options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0029

basis: |
  Proposals-log: no matching prior proposal (PROP-0023 covers Phase 4.6 pre-stitch; different
    target). No rejected proposal against this target.
  Discrimination: process failure, not content failure. A gate whose literal application would
    order a wasted ~40-dispatch re-decompose against a confirmed-exhausted de-abstraction
    state is a gate with a missing disposition branch. The 0-mute result is already a Phase 9
    gate output; the fix uses existing gate outputs without adding detection machinery.
  Recurrence override: first occurrence, but deterministic not probabilistic. Every apparatus-
    dominant chapter that hits depth-pass completion against a contract-register bone-set will
    produce this exact state. The 0-mute + AIRLESS + completeness-pass combination is
    mechanically unambiguous. S-cost modify closes the gap precisely.
  Methodology: reversibility (S-cost, mechanical branch; principal can override); cost
    (prevents ~40-dispatch re-decompose per future apparatus-dominant depth-pass completion);
    blast radius (narrow — fires only in depth-pass mode, only at 0-mute result).
  PROP-0023 interaction: complementary upstream proposal. PROP-0023 catches before stitch;
    PROP-0029 catches at depth-pass completion. Can be accepted independently.

rationale: |
  The content failure was correctly handled by DEC-0058 (b01c06 ships terminal; abstract-by-
  contract ruling is correct). The process failure is the absence of a mechanical gate outcome
  for this state. The Phase 9 readability-axis disposition currently has no branch for
  "0-mute + AIRLESS + completeness-pass in depth-pass mode." Without it, each occurrence
  requires an ad-hoc admin ruling invoking DEC-0007 anti-literalism against DEC-0048.
  The short-circuit (AIRLESS-ABSTRACT-BY-CONTRACT → PASS-TERMINAL-DEPTH-RESOLVED) makes
  the recognized exception a first-class gate outcome. The re-decompose route survives for
  non-zero mute counts (de-abstraction genuinely incomplete = DEC-0048 applies as written).
  Change_type: modify to existing Phase 9 composition block. Two new verdict values:
  AIRLESS-ABSTRACT-BY-CONTRACT and PASS-TERMINAL-DEPTH-RESOLVED (depth-pass-mode only).

trade-off: |
  Proposing at first occurrence. The anti-pattern guard (wait for recurrence on
  non-catastrophic first occurrence) is overridden by: (a) deterministic failure class;
  (b) fix uses only existing gate outputs; (c) the alternative is a repeating admin
  ruling invoking DEC-0007 on a gate whose own trade-off note anticipated this case.
  Risk if wrong: the principal decides abstract-by-contract is never the correct terminal
  disposition — but that would require overriding the proposal at triage (low cost) rather
  than burning dispatches on a known-wasteful re-decompose cycle.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0060 | 2026-05-31 | FAST (user-proxy)

question: |
  /and-substance chapter b01c08 Phase 5.5 chunk-cold-read returned CHUNK-CLASS-B (summary-maps +
  CONTINUE-strict=no). Disposition: (P) proceed-with-risk-recorded [Class B default], (R) revise
  chunk, or (S) escalate to substance-contract revision.

context: |
  b01c08 is a staging chapter in the b01 rise-zone (c07 hinge → c08 plant → c09-c10 develop → d07
  turn). Three obligations: cf-d10-courier-face beat 1 / Aemond-foreshadow / Oswyn-watcher-network
  integration as Khepri-echo (moral_framework held by design — reader sees the override-pattern;
  Taylor does not).
  Phase 5 reviewers: all PASS/ACCEPT (cape-fic-reader SUBSTANCE-FELT 3/3 + 3 ADVISORY; dark-fantasy-
  reader SUBSTANCE-FELT; worm-canon-pedant SUBSTANCE-FELT Earth-Bet-CLEAN; dramatist ACCEPT ("calibrated
  correctly as quiet plant; three low-intensity staging beats that accumulate reader recognition without
  advancing Taylor's own awareness"); auditor PASS 0 HARD 2 FLAG).
  Phase 5.5 cold-read confusions:
    - Most are contextual gaps resolved by c01-c07 for the real reader (insect-feed/Khepri,
      Oswyn/Wren established c01-c02; Aemond c06; Jarvis-Dragonpit-intercepts c04-c06).
    - "rank 3/5/0" and "axis labels" are YAML-block leakage (cold-reader saw contract YAML; real
      reader will not).
    - "Westeros + modern-spy register clash" is the project conceit — unfixable and intended.
    - "no decision, cost, reversal, or confrontation" — dramatist ACCEPT explicitly names this as
      correct staging function for the rise-zone position.
  Exact parallel to DEC-0044 (b01c06 Phase 5.5 CHUNK-CLASS-B → P).

options: |
  P: Proceed-with-risk-recorded. Class B default. Record cold_read_risk_carry for /and-stitch Phase 9.
  R: Revise chunk. Cost: 1 screen-writer + 5 reviewer re-dispatches. Risk: bumps c08 past staging function.
  S: Substance-contract revision. Highest cost. Not warranted.

decision: P — Proceed with risk recorded.

basis: ltm:DEC-0044 (exact same decision shape, same trade-off axis; Class B staging-chapter quietness)

rationale: |
  DEC-0044 resolved the materially identical question for b01c06. Summary maps to goal confirmed;
  strict-NO is mid-series context-noise + YAML leakage artifact (not real reader experience) + project
  conceit (register clash is intentional). Dramatist ACCEPT explicitly defends the staging function.
  (R) would re-author a non-defective chunk to compress something the chapter is structurally designed
  to do; at c08 the argument against (R) is slightly stronger than at c06 because the register-clash
  complaint is one more unfixable factor. (S) is not warranted — no contract defect identified by any
  informed reviewer.

trade-off: |
  (P) carries a known cold-read risk to /and-stitch Phase 9. This is the designed behavior of Class B:
  the cold-read→completeness-track handoff is the correct routing layer; Phase 9 scrutiny of the known
  risk is the mechanism for managing it. (R) would cost ~6 dispatches to produce a chunk less faithful
  to the chapter's rise-zone staging mandate. (S) would be nuclear on a PASS-clean contract.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0061 | 2026-05-31 | SLOW (process-critic)

> **2026-06-01 merge note:** session/audit-and-stitch-2026-05-31 also allocated DEC-0061 (cohere process-critic). Renumbered the session-branch entry to DEC-0064 (appended at the end of this file). This DEC-0061 (stitch-spine-staging, on main) is unchanged. The PROCESS-CHANGE-PROPOSED reference "PROP-0030" below is renumbered to PROP-0035 (session-branch had its own PROP-0030 for the cohere primitive; cohere PROP-0030 is more deeply integrated downstream, so staging PROP-0030 → PROP-0035).

question: /and-stitch b01-c08 Phase 9.5 process-critic dispatch. FAIL on two independent legs — (1) cold-read AIRLESS matching chunk_cold_read verbatim (Class B / matching-complaint → SHIPPED-WITH-CAVEATS on cold-read leg); (2) staging finding-002 STAGE on @6 axis-move central-event (BLOCKING under URI-STITCH-SPINE-STAGING independent of cold-read). Does process need to change?

context: |
  Full gate chain PASS except Phase 9. Voice-embodiment (PROP-0022) applied at stitch; produced
  AIRLESS anyway — rendered prose has no physical body-act for Taylor during the @6 integration
  mechanism because no such bone exists in the bones file. Third project chapter (c01 era / c05
  era / c08) where a concrete-SVO axis-move central-event bone lacks a physical body-act companion
  for the POV character during the mechanism. Prior proposals checked: no open/rejected proposal
  covers this specific pattern. Distinct from PROP-0024 (abstract-arrival cognitive bones),
  PROP-0023 (apparatus-dominant whole-chapter), PROP-0011 (held-axis-witnessing).

options: n/a (process-critic mode)

decision: PROCESS-CHANGE-PROPOSED PROP-0035

basis: |
  Q1 (staging vs. Class B routing): URI-STITCH-SPINE-STAGING governs the staging leg
  independently; finding-002 is a diagnosable addressable defect, not design-inherent. Staging
  override of SHIPPED-WITH-CAVEATS correct; no change to PROP-0018 Class B rule warranted.
  Q2 (voice-embodiment insufficient?): gap is bones-layer. Draft confirms Taylor's body absent
  during the @6 mechanism prose; voice-embodiment cannot supply a body-act the bones file does
  not contain.
  Q3 (mandate body-act companion for axis-move scenes): yes — third recurrence qualifies.

rationale: |
  The central-event bone "taylor traces the watcher-sightlines" is correctly concrete (passes
  EVENT-NOT-CONCRETE). The gap is absence of any companion physical-body-act bone for Taylor
  during the tracing. New failure sub-class: concrete-SVO axis-move bone without a body-act
  companion at the peak. URI-WRITE-EVENT-CONCRETENESS cannot catch it (the SVO IS concrete).
  PROP-0035 adds a Phase 1 authoring obligation + Phase 6 BODY-ACT-ABSENT-AT-PEAK SIGNAL check.
  S-cost; change_type modify; no new gate architecture. Recurrence_count 3.

trade-off: |
  Phase 1 companion obligation adds ~1 min/scene review for axis-move scenes; most will already
  satisfy it. Phase 6 SIGNAL (not HARD at first occurrence) limits false-fire damage from the
  physical-vs-cognitive SVO heuristic.

follows: DEC-0060
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0062 | 2026-05-31 | SLOW (user-proxy)

question: |
  /and-substance chapter b01c09 Phase 5.5 CHUNK-CLASS-B disposition. Summary maps to goal (Q6 confirmed).
  Strict-CONTINUE (Q7, no charity) = No. Options: (R) revise chunk, (P) proceed-with-risk-recorded,
  (S) substance-contract revision.

context: |
  b01c09 is a deliberately quiet "rising" omission-chapter (ch9/18; prohibition dissolves from inside —
  book drama line ~1602). All contextful reviewers PASSED: audience 3-of-3 SUBSTANCE-FELT (no HARD);
  dramatist ACCEPT (rise-peak-fall, s03 thesis-image legitimate); auditor CLEAR (0 HARD,
  cost-ledger + thematic-axis clean). Cold-reader's confusions fall into two classes:
  (A) prior-context dependencies — insect-feed/Taylor/Wren, Jarvis/Otto alias, Rushwick/Dragonpit
      proper nouns, lower-gate faction, "color accrues" metaphor, feed-record architecture — all
      resolved for a real reader by c01-c08.
  (B) Structural design complaints — "three instances of one behavior, not a chain"; "no motive for
      withheld" — the deliberate opacity IS the chapter's substance (omission-chapter thesis: Taylor
      holds two observations private; motive not named on the narrative surface by design).
  Neither class is an in-chunk cause-chain hole that (R) could cheaply fix without damaging the chapter's
  deliberate opacity or inserting the anti-exposition violation the project prohibits.
  Precedent: DEC-0060 (b01c08 CHUNK-CLASS-B → P, exact same failure mode — apparatus-vocabulary
  plus prior-context inaccessibility to a zero-context reader; dramatist ACCEPT explicitly defends
  staging function in both cases).

options: |
  P: Proceed-with-risk-recorded. Class B default. Record cold_read_risk_carry for /and-stitch Phase 9.
  R: Revise chunk. Cost: 1 screen-writer + 5 reviewer re-dispatches. Risk: forces motive onto the
     page, damaging deliberate opacity; inserts exposition the project anti-stance prohibits.
  S: Substance-contract revision. Highest cost. Not warranted — 0 HARD from all informed reviewers.

decision: P — Proceed with risk recorded.

basis: ltm:DEC-0060 (same decision shape, same trade-off axis; omission-chapter apparatus-vocabulary
  inaccessibility to zero-context reader; dramatist ACCEPT on staging function in both cases).
  Confirmed: "WHY she withholds" is deliberate narrative opacity (not in-chunk hole); "color accrues"
  is project metaphor vocabulary (not fixable by chunk revision without exposition violation).

rationale: |
  Both of the caller's flagged items are prior-context or design-inherent, not in-chunk defects.
  "Why she withholds — no motive on the page" is the chapter's thesis: the reader sees the
  override-pattern; Taylor does not name her motive; that's the deliberate opacity of an omission-
  chapter. A (R) that spells out motive would damage the chapter's design and contradict the
  dramatist's ACCEPT on the thesis-image. "Color accrues / resentment arrived with color" is
  project-metaphor vocabulary established in c01-c08 — inaccessible to a zero-context reader by
  construction, not by chunk deficiency. Both are the same class DEC-0060 dispositioned P.
  DEC-0060 applied because: (1) summary maps to goal confirmed; (2) strict-NO is pure mid-series
  context-noise and/or design-inherent structural complaint; (3) all informed reviewers PASS/ACCEPT;
  (4) (R) would re-author a non-defective chunk to violate its own design mandate. All four conditions
  hold identically for b01c09.

cold_read_risk_carry: |
  Items to arm downstream (context-weave track + /and-stitch Phase 9):
  1. strict-CONTINUE=No — design-inherent: omission-chapter with apparatus vocabulary; known-risk,
     not a delivery failure.
  2. motive-opacity: Taylor's withheld motive absent from narrative surface — context-weave pass
     should confirm implicit grounding exists OR license a minimal context-ledger add (not a bone
     rewrite); stitch Phase 9 should read this as design-intentional if no ledger add is made.
  3. "color" metaphor opacity — facet/context-weave pass should confirm c01-c08 anchor sufficient;
     if not, context-ledger may license a grounding phrase (not a new bone).
  4. Causality/payoff absent — cold-reader complaint is structurally correct AND structurally
     intentional (three parallel acts, not a chain; dramatist ACCEPT "rise-peak-fall, s03 thesis-image
     legitimate"); stitch Phase 9 should treat this as KNOWN-CLASS-B-DESIGN-INHERENT.

trade-off: |
  (P) carries known cold-read risk to /and-stitch Phase 9. This is Class B designed behavior.
  Downstream context-weave + stitch Phase 8.5/9 arming is the correct repair layer for
  prior-context-dependent and motive-opacity complaints. (R) would be a net regression: forces
  content onto the page that the chapter's design explicitly withholds.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0063 | 2026-06-01 | SLOW (user-proxy)

question: |
  /and-facets b01c09 pipeline option and parking-lot resolution.
  (A) Full faithful /and-facets — all phases, full Phase 5b 3-cycle adversarial gate. ~40-60 dispatches.
  (B) Streamlined single-pass — R1 fanout → Phase 2 merge → combined Phase 2.5 context+aliveness
      review → Phase 5 mechanical auditor (HARD-gate) → ONE-CYCLE Phase 5b audience gate → Phase 6.
      Skips R2 judging + multi-cycle remediation. ~15-20 dispatches.
  (C) c03-style cascade-budget — R1 fanout + merge only; skip Phase 2.5/3/5/5b. ~10 dispatches.
  Parking lot items: (i) corwick uncarded (same as c08 wenna-cobb); (ii) dragonpit-margin +
  lower-gate locations uncarded (canonical Westerosi geography).
  Recommended: Option B + carry-forward for both parking-lot items.

context: |
  b01c09 passed every upstream gate cleanly: audience 3/3 SUBSTANCE-FELT at /and-substance; bone-gate
  0 HARD + 9/9 SUBSTANCE-FELT at /and-write Phase 6; /and-review bones PASS fidelity + PASS-WITH-NOTES
  follow_check, 0 HARD. Silent chapter (no dialogue facet). Facets here are decoration over an already-
  validated spine — not load-bearing plot. BONES-AIRLESS-RISK (scene-B @8-@11) + one context-addable
  gap (@8 temporal marker) explicitly teed up for Phase 2.5.
  C03 compression cost: skipping Phase 2-6 audit chain caused pl-2026-05-27-001 SVO-form contamination
  that required c04 Phase-1 redo.
  Session risk: two silent subagent deaths in this session; large parallel audience blocks are highest
  risk surface.
  c08 parking-lot precedent: wenna-cobb + corwick uncarded, /and-facets ran to COMPLETE; Phase 5
  auditor deferred noun-form carry with zero chain impact.

options: |
  A: Full faithful. ~40-60 dispatches; highest silent-death exposure; full 3-cycle adversarial loop.
  B: Streamlined single-pass. Keeps Phase 5 HARD-gate + Phase 2.5 context/aliveness + one Phase 5b
     cycle. Skips R2 judging + multi-cycle remediation. ~15-20 dispatches. Caveat recorded.
  C: c03-style cascade-budget. ~10 dispatches. Known contamination risk; caused c04 redo. Eliminated.

decision: |
  Option B — streamlined single-pass.
  Parking lot: carry-forward for both (i) corwick and (ii) geo locations per c08 precedent.

basis: |
  goal:2 (cost discipline) + methodology:3b (cost) + c03 contamination lesson (option C eliminated) +
  c08 precedent (uncarded referenced figures + descriptive geography do not block /and-facets).

rationale: |
  Option C eliminated by c03→c04 evidence: the contamination it caused cost more to remediate than the
  compression saved. Option A is valid but burns 40-60 dispatches + 3 potential remediation cycles on a
  chapter that already has 9/9 SUBSTANCE-FELT bone validation and 0 HARD at fidelity review — a quiet
  silent omission-chapter whose facets are decorative reinforcement over a validated spine, not
  structural load-bearing. Option B keeps the three elements that matter most here: (1) Phase 5 HARD-
  gate (mechanical safety rail — the class that caught c03 contamination in later chapters); (2) Phase
  2.5 context+aliveness review (explicitly teed up: BONES-AIRLESS-RISK @8-@11 + temporal-marker gap @8);
  (3) one Phase 5b adversarial cycle (sufficient on a quiet chapter — 3/3 convergence signals real
  finding regardless of cycle count). R2 judging + multi-cycle remediation add value on chapters with
  high facet-complexity or contested substance spine; neither applies. Silent chapter eliminates the
  dialogue-R2 leg entirely.
  Parking lot: c08 set the exact precedent — wenna-cobb + corwick uncarded, /and-facets COMPLETE with
  Phase 5 deferral recorded, zero chain impact. Dragonpit + lower-gate locations are canonical
  Westerosi geography; descriptive noun forms work without loc cards. Margit dispatch costs dispatches
  for near-zero quality delta.

trade-off: |
  Option B forgoes R2 locked-graph review. On a quiet silent chapter with validated spine, this risk is
  low. If Phase 5 or Phase 5b surfaces something unexpected, a fixer loop may be needed that R2 would
  have pre-empted. Accept: expected cost of R2 omission is low; actual spend of Option A is guaranteed
  high; silent-death risk of large parallel blocks is real and demonstrated in this session.

---

## DEC-0064 | 2026-06-01 05:00 | SLOW (process-critic)

> **2026-06-01 merge note:** originally allocated DEC-0061 on session/audit-and-stitch-2026-05-31; renumbered to DEC-0064 at merge to avoid collision with main's DEC-0061 (stitch-spine-staging body-act-companion). The "PROP-0033 + OK + PROP-0034" disposition is unchanged.

question: |
  /and-cohere b01 c01-c07 converged to CAUTION-COHERE (load_bearing_fails=0; all load-bearing
  axes PASS; 5 non-load-bearing CAUTIONs). Three design questions raised at Phase 7.5:
  (1) Should Phase 6.5 aggregate emit fire on CAUTION-COHERE with zero load-bearing fails?
  (2) Does audience persona rotation surface noise rather than signal?
  (3) Should dramatist CAUTION threshold be re-evaluated for declared project design choices?

context: |
  First live /and-cohere run. PROP-0031 Amendment 1 (Phase 6.5 aggregate emit) and
  Amendment 2 (/and-stitch Phase 10) were implemented this session. Phase 6.5 was SKIPPED
  because its trigger requires PASS-COHERE strictly — CAUTION-COHERE does not fire it even
  when all load-bearing axes PASS. aggregate-state.md was not bootstrapped; /and-stitch
  Phase 10 on c08 falls back to reading the seven prior chapter drafts directly. The
  CAUTION axes are: naive Q5 sensory distribution (thin in c02/c04 middles), naive Q6
  apparatus-register (strained but not broken), dramatist axis3 antagonist pressure
  (interior-pressure structure), dramatist axis4 scene-shape (interior+transaction dominant),
  audience axis2 threshold discipline (insect-instrument never fails; no contesting force
  pre-c07). Axes 3 and 4 accurately describe declared project structural design choices.

options: |
  Q1: (a) keep strict PASS-COHERE-only for Phase 6.5; (b) relax to CAUTION-COHERE +
      load_bearing_fails==0 also fires Phase 6.5
  Q2: (a) no change; (b) add persona-consensus strength field to verdict aggregation
  Q3: (a) no change; (b) add ADVISORY tier + optional structural exemption mechanism;
      (c) hold for recurrence

decision: |
  Q1: PROCESS-CHANGE-PROPOSED PROP-0033
  Q2: OK — no proposal
  Q3: PROCESS-CHANGE-PROPOSED PROP-0034

basis: |
  Q1: methodology — reversibility (gap compounds on every future CAUTION-COHERE run;
  early fix cheaper than accumulated fallback cost) + cost (S-cost modify; minimal
  change) + blast-radius (one condition in one phase). State file diagnosed the gap
  itself at ship time. First occurrence but proposing because the gap is deterministic
  and mechanically precise.
  Q2: methodology — optionality (hold keeps design simpler; the report narrative already
  surfaces the distinction; no decision has been harmed by the current design). First
  occurrence; non-catastrophic; hold for recurrence.
  Q3: methodology — cost (recurring inactionable CAUTIONs erode the CAUTION tier's
  signal value over the project lifetime; S-cost to fix now < compounding signal erosion
  cost) + blast-radius (additive ADVISORY tier; does not change ACCEPT/CAUTION/FAIL
  semantics). First occurrence but proposing because the failure is deterministic (every
  future cohere run for this project) and the discriminating criterion is mechanically
  precise (licensed-by-declared-structure).

rationale: |
  Q1: A CAUTION-COHERE run with load_bearing_fails==0 is ship-clean on every axis that
  matters for forward-feed reliability. The non-load-bearing CAUTIONs are advisory taste
  signals, not evidence that the stretch's axis-state or hook-inventory are unreliable.
  Relaxing the Phase 6.5 fire condition to include this case closes a deterministic gap.
  --strict behavior is unchanged (under --strict, CAUTION routes to Phase 3 and convergence
  is not declared, so Phase 6.5 never fires under --strict regardless of load_bearing_fails).

  Q2: The CAUTION/FAIL distinction already encodes signal strength. A CAUTION that only
  one persona fires is lower-signal than one all three fire, and the report's narrative
  captures this. Adding a `persona_consensus` structural field to the aggregation schema
  would formalize what is already visible in the narrative without changing any downstream
  decision. First occurrence; hold for recurrence before adding infrastructure.

  Q3: CAUTION implies actionability — "this is a quality concern addressable by revise."
  Dramatist axis3/axis4 findings that accurately describe a declared structural choice are
  not actionable. Filing them as CAUTION on every cohere run trains the principal to ignore
  the CAUTION tier, which is a worse outcome than having fewer CAUTIONs. ADVISORY as a
  third tier ("accurate, inactionable, recorded for reference") + an optional structural
  exemption mechanism separates the two signal classes cleanly. The discriminating clause
  ("departure from licensed structure is not exempt") prevents the tier from swallowing
  legitimate structural concerns.

trade-off: |
  Q1: Relaxing Phase 6.5 means aggregate-state.md can be emitted from a "cautioned"
  run. Mitigated by last_updated_by: and-cohere-caution tag (downstream consumers see the
  emit source) and by load_bearing_fails==0 condition (structural facts are reliable).
  Q2: Holding means the current run's persona-rotation insight is noted but not acted on
  mechanically. Low cost.
  Q3: ADVISORY tier adds a third classification the dramatist must discriminate. Misclassifying
  a genuine CAUTION as ADVISORY loses the signal. Mitigated by the "departure from licensed
  structure is not exempt" clause, which keeps the exemption narrow.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0065 | 2026-06-01 | SLOW (user-proxy)

question: |
  Two decisions required before /and-stitch b01c08 Phase 10 can proceed.
  Decision 1: Wenna Cobb cast collision (c07 dead child vs. c08 living feed-body same slug).
    PATH A — rename c08 character to non-colliding slug (e.g. meryn-cobb or wenna-pratt).
    PATH B — recast c08 wenna-cobb as surviving family member of c07's dead child (adds
    substance, requires full re-cascade of c08: ~50-80 dispatches, reopens terminal chapter).
  Decision 2: Phase 10 execution method.
    OPTION (a) — re-run /and-stitch b01c08 from scratch (~50-80 dispatches, re-runs Phase 9).
    OPTION (b) — inline-execute Phase 10 only against the shipped draft (~5-10 dispatches).

context: |
  c07 SHIPPED: Wenna Cobb is the founding entry in Taylor's grave-count ledger — a dead
  six-year-old from Pig-Tallow Lane in the Hook. Load-bearing c07 substance.
  c08 SHIPPED-WITH-CAVEATS: wenna-cobb slug minted in c08 bones cast + bone 20 as a living
  body in the insect-feed return. No dialogue file for wenna-cobb in c08. No substance weight
  in c08 — pure coverage-map feed-return body. Collision was not caught by the bone-gate
  (cross-chapter slug collision is not a current gate).
  c08 already has a terminal draft (Phase 9 PASS). Phase 10 (forward-thread + aggregate-state
  initialization) is new pipeline that post-dates c08's stitch. /and-stitch is idempotent on
  render artifacts but would re-run Phase 9 cold-read if re-invoked from scratch. Production
  run is cap-bounded; currently finishing c08 cleanup before proceeding to c09.

options: |
  Decision 1: PATH A (slug rename, surgical, 0 re-cascade) vs. PATH B (family-relationship
  recast, adds substance, ~50-80 dispatches re-cascade, reopens shipped chapter).
  Decision 2: OPTION (a) full re-stitch from scratch vs. OPTION (b) inline Phase 10 only.

decision: |
  Decision 1: PATH A. Rename c08's wenna-cobb to meryn-cobb.
  Decision 2: OPTION (b). Inline-execute Phase 10 only against the shipped draft.

basis: |
  Decision 1: goal:2 (cost discipline) + methodology:3b (cost) + methodology:3a (reversibility).
  Decision 2: goal:2 (cost discipline) + methodology:3b (cost) + methodology:3a (reversibility).

rationale: |
  Decision 1: The collision is an authoring accident, not a planted irony. c08's living
  wenna-cobb carries zero substance weight — it is a fungible coverage-map feed-return body
  with no dialogue, no bone delta, no thematic setup pointing at a family connection. PATH B's
  thematic payoff (dead child's family still counted by the feed) is genuinely resonant but
  is unrequested scope expansion inside a cap-bounded finish run. PATH A is zero-cost,
  zero-risk, and fully preserves c07's load-bearing dead-Wenna intact.

  Slug choice: meryn-cobb (not wenna-pratt). The Cobb surname places this person in
  Pig-Tallow Lane / the Hook, same ward as the insect-feed coverage. Keeping the surname
  consistent with the neighborhood is more coherent than severing it entirely, and meryn-cobb
  makes no substance claim (no dialogue, no bone delta, no named relationship to Wenna Cobb
  established in the text). The living Cobb family presence option is preserved for future
  chapters if it ever becomes load-bearing substance.

  Decision 2: Phase 9 already PASSED on c08's terminal draft. Re-running all eight render
  phases + Phase 9 cold-read is a verified no-op at 10x the cost, with non-zero risk of
  a Phase 9 verdict difference from seed variance. Phase 10 is the only missing motion.
  Inline execution against the shipped draft is the correct bolt-on protocol for a
  missing phase on a terminal chapter.

trade-off: |
  Decision 1 PATH A gives up the thematic resonance of Wenna Cobb's surviving family being
  tracked by the same feed that counted her death. That resonance is real but currently
  unsetup and unrequested. It remains available as an explicit authoring choice in a future
  chapter's substance contract.
  Decision 2 OPTION (a) would yield a clean re-stitch record but at 10x cost with churn
  risk on a terminal deliverable. Not a meaningful trade-off.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0066 | 2026-06-01 | FAST (user-proxy, RUNBOOK R1)

question: |
  /and-stitch b01c09 Phase 9 terminal cold-read: uninformed cold-reader returned NO-CONTINUE.
  Disposition: (A) PASS-WITH-DEPTH-PASS-REQUIRED — ship terminal, record risk, cascade to
  Phase 10 + c10; (B) FAIL → /and-write b01c09 revise --from-signals (R2 1-retry).

context: |
  b01c09 is a deliberately quiet silent omission-chapter (Taylor surveilling Wren; courier-face
  advance; s03 double-omission thesis-image; moral_legibility HELD). Phase 5.5 chunk-cold-read
  was already adjudicated CHUNK-CLASS-B / disposition P / DEC-0062, which explicitly pre-recorded
  that strict-CONTINUE=no is DESIGN-INHERENT and the CONTINUE bar is tentative-yes.
  Upstream gates all clean: bone-gate 0 HARD + audience 9/9 SUBSTANCE-FELT; /and-review bones PASS
  + 0 HARD; /and-facets Phase 5 0 HARD + Phase 5b 3-of-3 ACCEPT; Phase 8.5 coherence PASS;
  Phase 9 Step 3.5 prose-rationale-mute audit 0 findings. The cold-reader recovered the surface
  events (watches Wren's route, sees Corwick at gate, seals packet) but rated the chapter
  NO-CONTINUE on grounds of jeopardy-absence and ungrounded proper nouns. The "ungrounded proper
  nouns" complaint is the context-stripped artifact the completeness track addresses for real readers
  carrying 8 prior chapters. Cold-read was harsher than c07's "barely-yes." Consecutive-airless
  chapters (c06/c07/c08/c09) are a book-level pattern.

options: |
  A: PASS-WITH-DEPTH-PASS-REQUIRED — ship terminal; record cold-read NO-CONTINUE as design-
     inherent Class-B cost; depth pass pending before book-close; cascade continues.
  B: FAIL → /and-write b01c09 revise --from-signals — R2 1-retry; risks same Class-B outcome
     on re-run since substance gates already clean.

decision: Option A — PASS-WITH-DEPTH-PASS-REQUIRED. Ship terminal. Cascade continues to Phase 10
  and then c10. Consecutive-airless pattern flagged for end-of-run summary as book-level /and-cohere
  concern.

basis: |
  DEC-0062 (CHUNK-CLASS-B pre-adjudication, exact match) + DEC-0060/DEC-0048 (Class-B precedent
  chain for quiet chapters) + methodology:3a (reversibility — re-decomposing a chapter that passed
  every substance + coherence + audience gate is irreversible spend against a design-inherent wall)
  + methodology:3b (cost — retry burns R2 cap on a chapter where all substance gates report clean).

rationale: |
  DEC-0062 explicitly pre-adjudicated this scenario. The chunk-cold-read adjudication already
  recorded: (1) strict-CONTINUE=No is design-inherent for this chapter; (2) the CONTINUE bar
  is tentative-yes; (3) cold_read_risk items were: strict-CONTINUE=No, motive-opacity,
  color-metaphor, causality-design-inherent. The Phase 9 NO-CONTINUE is exactly those items
  firing — not a new finding, not a delivery failure.

  All upstream substance+coherence gates are clean (0 HARD bone-gate, 9/9 audience SUBSTANCE-FELT,
  /and-review bones PASS, facets 3-of-3 ACCEPT, Phase 8.5 PASS, 0-mute audit PASS). A cold-reader
  context-stripped of 8 prior chapters cannot be expected to recover a surveillance chapter's
  architecture, the Wren cost-bearer setup, the Otto arrangement, or the moral collapse — all of
  which a real reader carries. The "ungrounded proper nouns" complaint is this structural condition
  manifesting, not a delivery failure in the draft.

  Re-decomposing (/and-write b01c09 revise --from-signals) would: (1) burn the R2 retry cap;
  (2) likely reproduce the same quiet design on a chapter whose substance contract mandates quiet;
  (3) risk substance gate re-fires on a bone-set that already passed every check; (4) not address
  the design-inherent cause of the NO-CONTINUE (the chapter IS two surveillance walks and a sealed
  letter — that IS the design). The only thing a revise could do is add false jeopardy or
  unnecessary exposition, both of which would contradict the substance contract.

  Consecutive-airless-chapter pattern (c06/c07/c08/c09 all drawing tentative/barely/NO cold-reads)
  is real but is a book-level arc concern, not a per-chapter delivery failure. The correct routing
  is /and-cohere at book-level, not per-chapter re-decompose. This goes to the end-of-run summary.

trade-off: |
  Option A accepts that the shipped draft will have a recorded NO-CONTINUE from the uninformed
  cold-reader, which is below the bar of c07's "barely-yes." The depth-pass-pending flag ensures
  this surfaces before project-stable. Option B would burn the retry without changing the design-
  inherent cause of the cold-read complaint and risks downstream churn on a clean substance spine.
  The precedent chain (DEC-0062/0060/0048/0058) consistently confirms that quiet-chapter design
  does not constitute a per-chapter FAIL obligation. The book-level /and-cohere concern is the
  right escalation path.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0067 | 2026-06-01 | SLOW (process-critic)

question: |
  /and-stitch b01c09 Phase 9.5 process-critic dispatch. Source verdict: PASS-WITH-DEPTH-PASS-REQUIRED
  (DEC-0066). b01c09 is the fourth consecutive Class-B quiet/omission chapter (c06/c07/c08/c09) to
  draw a tentative-or-worse uninformed cold-read and ship via the Class-B risk-recorded path.
  Three candidate process concerns: (1) cold-read gate mis-calibrated for mid-book Class-B quiet
  chapters; (2) book stacking too many consecutive low-event omission chapters; (3) depth-pass-
  pending accumulation across 4 chapters represents unresolved debt.

context: |
  source_report: active-project/staff/reviews/coldread-b01c09-20260601T163000Z.md
  source_verdict: PASS-WITH-DEPTH-PASS-REQUIRED
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-substance.md#phase-5.5, design/substance/staleness-cascade.md]
  Prior per-chapter dispositions: DEC-0058 (c06), DEC-0060 (c07 phase-5.5), DEC-0061 (c08 process-critic),
    DEC-0062 (c09 phase-5.5), DEC-0066 (c09 phase-9). Every per-chapter gate PASSED cleanly.
  Open relevant proposals: PROP-0018 (Phase 9 Class A/B discrimination, open), PROP-0025 (depth-pass
    AIRLESS sub-clause, open), PROP-0029 (depth-pass abstract-by-contract terminal, open), PROP-0030
    (/and-review cohere primitive, open), PROP-0031 (/and-cohere iteration loop, open).

options: n/a (process-critic mode)

decision: OK-MERGED-INTO PROP-0030 and PROP-0031. No new proposal. Three candidates resolved:

basis: |
  Candidate 1 (gate mis-calibration): The Phase 9 gate detected correctly (NO-CONTINUE) and
    disposition was per PROP-0018's pending Class-B logic (DEC-0062 pre-adjudicated this exact
    scenario; DEC-0066 applied it). Gate calibration is not the gap — the gate is firing correctly.
    PROP-0018 (open) already proposes the Class B disposition branch. No new proposal warranted.
    Return: OK (PROP-0018 already addresses this).

  Candidate 2 (consecutive quiet chapters / book-level dramatic-shape): Per-chapter processes all
    fired correctly; each quiet chapter was individually justified by informed-reviewer PASS + Class-B
    disposition. The book-level arc concern is precisely the failure class PROP-0030 (/and-review cohere)
    + PROP-0031 (/and-cohere iteration) were designed to surface and converge. DEC-0066 already named
    /and-cohere as the correct routing. The new evidence (four chapters now, not the seven from the
    original c01-c07 session audit) strengthens the case for triaging PROP-0030/PROP-0031 promptly.
    No new process gap — the proposed mechanism covers this. Merging evidence into PROP-0030 and
    PROP-0031 (recurrence_count incremented to 2 on both; new evidence_refs added).
    Return: OK-MERGED-INTO PROP-0030 and PROP-0031.

  Candidate 3 (depth-pass-pending debt accumulation, N=4): First cross-chapter occurrence of four
    simultaneous depth-pass-pending flags. Non-catastrophic. The designed resolution path is correct:
    (a) each chapter's flag is recorded in memory; (b) DEC-0066 named the accumulation pattern in the
    end-of-run summary for the principal; (c) /and-cohere before book-close is the designed aggregation
    mechanism (PROP-0030/0031). No gate failure — the debt tracking is working as designed. A new gate
    that fires on N-consecutive depth-pass-pending would duplicate the /and-cohere check at higher
    gate-complexity cost. First occurrence; non-catastrophic; the designed path handles it.
    Return: OK (hold for recurrence; re-evaluate if N reaches 6 before /and-cohere runs).

rationale: |
  Content vs. process discrimination: every per-chapter gate fired correctly. The cold-read
  detection is accurate — this chapter IS a surveillance-only, three-beats, jeopardy-absent
  design that will challenge a context-free reader. The per-chapter disposition (Class-B ship)
  was correct because all informed-reviewer gates were clean. The only question is whether the
  CROSS-CHAPTER accumulation pattern reveals a process gap.

  It does not reveal a new gap: PROP-0030 and PROP-0031 are already the proposed mechanism for
  cross-chapter accumulation. They are open and untriaged — the b01c09 evidence is the second
  cross-chapter recurrence (c01-c07 session audit was the first; c06-c09 is the second), which
  strengthens the triage case for both proposals without requiring a new one.

  The one question that might seem to warrant a new proposal — a preventive gate at /and-substance
  book that flags N-consecutive low-event chapters in the chapter plan — is premature at N=4,
  because: (a) each chapter was individually justified by dramatist ACCEPT; (b) the book's declared
  dramatic shape front-loaded a rise zone with multiple staging chapters; (c) /and-cohere is the
  correct resolution layer, not upstream prevention of deliberate staging decisions. A preventive
  cap at /and-substance book would penalize intentional quiet-chapter sequences that the dramatist
  has explicitly approved. The minimum-blast-radius handling is to triage PROP-0030/PROP-0031.

trade-off: |
  Not proposing a new depth-pass-pending accumulation gate accepts that the principal must track
  the N=4 accumulation via the end-of-run summary and /and-cohere scheduling. If /and-cohere is
  deferred past N=6, the accumulation becomes harder to resolve (more chapters carrying unresolved
  depth flags = larger cohere run). That would be the trigger for a new proposal (accumulation
  warning at N>=5 in /and-stitch Phase 0 parking-lot scan).

  Not proposing a preventive gate at /and-substance book accepts that consecutive-quiet-chapter
  decisions remain individual and dramatist-approved. If the book closes with c10-c18 also quiet
  and the /and-cohere run returns FAIL-COHERE, retroactive evidence would support a book-plan
  constraint. Hold for that signal.

follows: DEC-0066
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0068 | 2026-06-01 | FAST (user-proxy, RUNBOOK R1)

question: c09 depth pass completed end-to-end. Choose: (A) stamp depth_pass_resolved_at, ship terminal, proceed to Phase 10; or (B) iterate again — treat cold-read NO-CONTINUE as fresh FAIL and run a second depth-pass loop.
context: |
  c09 shipped at Phase 9 PASS-WITH-DEPTH-PASS-REQUIRED (DEC-0066). DEC-0066 pre-adjudicated the
  cold-read NO-CONTINUE as design-inherent Class-B cost (surveillance-only chapter; no on-page
  jeopardy; apparatus register; withheld motive; assumes 8 chapters of prior context). Depth pass
  ran end-to-end: /and-write revise added 4 embodiment/grounding bones (person-on-cold-lane open,
  cold-stiffened-hand DE-FOG of abstract filing line, grounded watch), bone-gate CLEAN 0 HARD;
  /and-review bones PASS + BONES-AIRLESS-RISK RESOLVED→ADVISORY-CONTAINED; /and-facets Phase 2.5
  Axis-2 ALIVE (deficit RESOLVED — de-fog lands); Phase 5 0 HARD; Phase 5b 3-of-3 all facets
  (trio endorsed de-fog + calendar fold); /and-stitch Phase 8.5 PASS ("airlessness resolved;
  person now present, hung on a felt body; fog gone"); Phase 9 Step 3.5 0-mute PASS (15/15
  concrete elements staged). Phase 9 Step 1 cold-read still NO-CONTINUE — same shape, same
  design-inherent reasons. RUNBOOK R2 cap: 1 depth-pass retry — spent.
options: (A) DEPTH-PASS DELIVERED — stamp resolved, ship, Phase 10; (B) iterate again.

decision: (A) — depth pass delivered; stamp depth_pass_resolved_at; ship terminal; proceed to Phase 10.
basis: ltm:DEC-0066 (exact match — this cold-read NO was pre-adjudicated as design-inherent Class-B cost before the depth pass ran; that ruling has not been disturbed by anything the depth pass revealed) + methodology:3a (reversibility — a second loop is irreversible spend with zero expected delta: the improvement that can be made within the design has been made and confirmed by four independent gates; iterating reproduces the identical cold-read NO without moving the design)
rationale: Four gates confirm the readability improvement landed (the fog is gone; a person is now present). The cold-read still says NO for the same recorded design-inherent reasons it said NO before DEC-0066 adjudicated them. Nothing in the depth-pass results disturbs that adjudication. R2 cap is spent. Option (B) is a loop with known outcome.
trade-off: Shipping with a cold-read NO on record is the accepted Class-B cost per DEC-0066. The consecutive-airless accumulation concern (N=4) is carried forward for /and-cohere before book-close per DEC-0067.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0069 | 2026-06-02 | SLOW (process-critic)

question: /and-write b01c10 Phase 6.5 — does this bone-gate run reveal process changes needed? Two candidate patterns: (1) recurring audience-trio dispatch death (socket+timeout x2 consecutive chapters); (2) HELD-AXIS-NOT-WITNESSED as recurring decomposition gap (9 axes at c10, same class as c04 + c06).
context: |
  Bone-gate report: write-b01-c10-bone-gate.md. Verdict: PASS after cycle-1 fix.
  4 HARD HELD-AXIS-NOT-WITNESSED (all resolved cycle-1; fixer added 9 axes_held[] entries to
  named held bones). 7 SIGNAL (2 remediated, 5 accept-with-rationale). Audience 3-of-3 ACCEPT
  all scenes (split single-persona dispatch used after two full-trio deaths).
options: n/a

decision: PROCESS-CHANGE-PROPOSED PROP-0036 (new; audience trio dispatch death — modify /and-write Phase 4+6 default topology) + OK-MERGED-INTO PROP-0011 (recurrence_count 2->3; rollup-attribution note added to proposed_diff).
basis: methodology:3a (reversibility — dispatch death is irreversible wasted spend; split-dispatch is always cheaper) + recurrence threshold (PROP-0036 at count=2 consecutive; PROP-0011 merge is mandatory per matching rules at count=3).
rationale: |
  Pattern 1 (dispatch death): No prior proposal covered this failure mode. Recurrence_count = 2
  (c09 incident + c10 two-failure sequence). Two consecutive chapters rules out one-off noise.
  The split-dispatch is the proven-working alternative (used twice, no quality loss, ~90sec each).
  change_type: modify (topology only; aggregation rule unchanged). Cost S. Proposed at count=2
  rather than waiting for count=3 because (a) consecutive chapters rule out infrastructure noise;
  (b) failure cost is high (40+ minutes wasted per death); (c) fix is proven and S-cost.

  Pattern 2 (HELD-AXIS-NOT-WITNESSED): PROP-0011 already open, same target.path + change_type.
  Merged per matching rules. recurrence_count 2->3. Recurrence_ref added (write-b01-c10-bone-gate.md).
  proposed_diff extended with an explicit note that rollup-level "implicit" attribution does not
  satisfy the gate — the bone must carry the axis in its bone-level axes_held[] field. This is the
  specific root cause at c10 (screen-writer attributed via rollup, not per-bone).
trade-off: |
  On dispatch death: proposing at count=2 rather than the default count>=3 threshold for non-
  catastrophic SIGNALs. Justified: consecutive-chapter pattern + high failure cost + proven fix.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0070 | 2026-06-02 | SLOW (process-critic)

question: |
  /and-stitch b01c10 Phase 9.5 — PASS-WITH-DEPTH-PASS-REQUIRED. Two candidate patterns:
  (1) Acts-of-commission staging gap: staging reviewer found STAGE on @2/declare, @11/route, @21/inscribe —
  all acts-of-commission — while observation/receipt bones staged well throughout. Pattern note: "all three
  STAGE findings occur at act-transmission moments; observation and receipt land; the staging deficit is
  specific to the ACTS OF COMMISSION." Should this be caught upstream at /and-write Phase 6 bone-decomposition?
  (2) Apparatus-density cross-chapter accumulation (c06-c10): cold-reader "dense and repetitive, arm's-length
  throughout; barely yes." Fifth chapter in the consecutive-airless sequence. Relevant per DEC-0067's N=6
  re-evaluation threshold.

context: |
  source_report: active-project/staff/reviews/coldread-b01-c10-2026-06-02.md
  source_verdict: PASS-WITH-DEPTH-PASS-REQUIRED
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]
  Chapter shipped terminal. Staging review found STAGE on @2/declare, @11/route, @21/inscribe + GROUND on
  @18. Cold-reader: dense, repetitive, arm's-length; barely-yes continue; world-register confusion (Gold
  Cloaks in surveillance apparatus); "I felt the narrator's residue more than I felt the loss." Phase 8.5
  coherence PASS. chunk_cold_read was PASS-CHUNK-VOICE-RISK with airlessness flagged design-inherent for
  the climax. Recurrence context: DEC-0067 established consecutive-airless watch at c06-c09 (N=4); c10 is
  N=5. DEC-0067 set re-evaluation threshold at N=6. Open relevant proposals: PROP-0035 (body-act companion
  on axis-move central-event bones; recurrence_count: 4; open), PROP-0030 (cohere primitive; recurrence_count:
  2; open), PROP-0031 (cohere iteration loop; recurrence_count: 2; open).

options: n/a (process-critic mode)

decision: |
  Pattern 1 (acts-of-commission staging gap): OK — recurrence_count = 1 for this specific class;
  non-catastrophic; no upstream gate can discriminate staged-vs-summarized on pre-stitch bones without
  becoming the staging reviewer; hold for second occurrence.
  Pattern 2 (apparatus-density cross-chapter c06-c10): OK-MERGED-INTO PROP-0030 + PROP-0031 — recurrence_count
  2→3 on both; N=5 does not cross DEC-0067's N=6 new-proposal threshold; PROP-0030/0031 remain the correct
  closure mechanism.

basis: |
  Pattern 1: methodology:3a (reversibility — premature gate erodes bone-gate signal quality; wait
  for recurrence at count=1 non-catastrophic per standing procedure). Content-vs-process discrimination:
  the staging reviewer caught the commission-verb pattern correctly at Phase 9; no upstream gate could
  have discriminated staged-vs-summarized on bones (bones are pre-render scaffolding; the stitcher's
  rendering determines whether a commission SVO reads as enacted or glossed). PROP-0035 covers the
  body-act companion gap on axis-move central-event bones; the c10 commission-verb gap may or may not
  intersect PROP-0035's scope (depends on axis-move classification of @2/@11/@21 — cannot determine
  from the cold-read report alone). Hold for second occurrence; if c11+ produces same commission-verb
  STAGE pattern, target a modify of /and-write Phase 1 SVO guidance for commission-verb bones.
  Pattern 2: ltm:DEC-0067 (threshold N=6 before new proposal; N=5 does not cross it; merge into
  PROP-0030/PROP-0031 per matching rules).

rationale: |
  Pattern 1 is genuinely a new named sub-class: observation/receipt staging is clean while
  commission-verb bones (declare, route, inscribe) consistently miss the enactment and render as
  conclusion/summary. This is distinct from PROP-0035 (which addresses cognitive/mechanism SVOs on
  axis-move central-event bones and requires a physical body-act companion in ±2). The c10 class is:
  commission-verb SVO that is itself concrete but rendered as already-done rather than in-progress —
  the gap is enacted-vs-concluded, not physical-body-act-companion. No existing gate catches this;
  the staging reviewer at Phase 9 is the correct first-catch surface; an upstream check would need
  to make staged-vs-summarized judgments on bone text alone, which is intrinsically post-stitch
  because the stitcher's rendering choice determines the enacted/concluded quality of the output.
  First occurrence; non-catastrophic; hold per procedure.

  Pattern 2: the c10 cold-read is the fifth chapter-level instance of apparatus-register airlessness
  (c06/07/08/09/10) and the third cross-chapter recurrence for PROP-0030/PROP-0031 (first: c01-c07
  session audit; second: DEC-0067 merge at c09; third: this dispatch at c10). The merge increments
  recurrence_count to 3 on both proposals. DEC-0067's threshold logic stands: the preventive gate
  (accumulation warning at N>=5 in /and-stitch Phase 0 parking-lot scan) is triggered at N=6, not
  N=5. The correct action is triage of PROP-0030/0031, not a new proposal.

trade-off: |
  Pattern 1: not proposing accepts that the commission-verb enacted/concluded gap will require a depth
  pass on any chapter where it fires. If c11+ also draws commission-verb STAGE findings, the gap
  becomes codifiable and a targeted Phase 1 modify can be proposed with a clean two-chapter evidence
  base. The cost of waiting is one depth pass; the cost of a premature gate is a bone-gate that makes
  pre-stitch rendering judgments, which is architecture drift.
  Pattern 2: merging into PROP-0030/PROP-0031 instead of proposing an accumulation warning at N=5
  accepts that the principal must triage the two open proposals before c10-c13 chapters ship, or the
  accumulation grows toward N=6 where a separate warning gate becomes warranted. This is the same
  trade-off DEC-0067 accepted; nothing at c10 changes the calculus.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0071 | 2026-06-02 | FAST (user-proxy, RUNBOOK R1)

question: |
  b01c11 /and-substance chapter Phase 3 — disposition for two HARD parking-lot items.
  Item 1 (pl-2026-06-02-stitch-thread-001): UNPAID-HOOK hook-0007 (Halvard counter-argument).
    Opened c07; payoff slipped c10; c10+c11 hold Halvard offstage. Reached/passed window.
    c13 contract states "Halvard appears... engagement foreclosed"; c11/c12/c13 handoffs carry
    "Halvard: counter-argument thinning in Taylor's engagement."
  Item 2 (pl-2026-06-02-stitch-thread-002): UNPAID-HOOK cl-d06 relational_anchor_status +2 (2nd +1.0 tranche).
    First +1.0 settled c06. 2nd +1.0 window c08-c10 expired unsettled. c11 holds axis flat.
    c12 moves relational_anchor_status +1.0 (mechanism: cl-d08 "Wren structurally necessary to coverage map").

context: |
  Silent chapter-production run for b01c11 (RUNBOOK Rule 1). Items flagged for Phase 3 resolution.
  Established pattern: prior parking-lot re-windows (pl-2026-05-25-001, pl-2026-05-30-001) re-windowed
  to the chapter where the axis next moves or the hook's downstream contract settles it.

options:
  - re-window: carry the item forward to a specific future chapter
  - resolve-here: settle the item in Phase 3 in-substance (not possible given offstage constraints)
  - foreclose: declare the hook retired via downstream authored contract
  - ESCALATE: surface to principal

decision: |
  Item 1 (hook-0007 Halvard counter-argument): FORECLOSE.
    The c13 authored contract ("engagement foreclosed") is the payoff. The c11/c12/c13 handoffs
    already carry the thinning trajectory. Phase 3 should stamp: foreclosed-at-c13, citing c13 handoff
    language. No re-window needed — the downstream authored contract IS the resolution.
  Item 2 (cl-d06 2nd +1.0 relational_anchor_status tranche): RE-WINDOW to c12.
    c12 delivers relational_anchor_status +1.0. That axis-move is the settlement event for the
    outstanding cl-d06 tranche regardless of which ledger entry (cl-d08) describes the mechanism.
    The axis does not track mechanism attribution per tranche — movement settles debt.

basis: |
  Item 1: methodology:3e (convention — prior hooks whose downstream authored contracts carry explicit
  "foreclosed/thinning" language are stamped FORECLOSE at the point they reach/pass window; the
  resolution is already authored, not deferred). The c13 contract is unambiguous ("engagement
  foreclosed"); the handoff language confirms it; no new authoring required at Phase 3.
  Item 2: methodology:3e (convention — established re-window pattern re-windows to the chapter
  where the axis next moves; c12 is that chapter). The mechanism-attribution distinction (cl-d08 vs.
  cl-d06) does not create a separate axis-move; relational_anchor_status +1.0 in c12 settles whatever
  cl-d06 balance is outstanding.

trade-off: |
  Item 1: FORECLOSE vs. RE-WINDOW-to-c13. FORECLOSE is correct because c13 doesn't just open a new
  window — its authored contract explicitly delivers the resolution text. Re-windowing implies the
  hook is still open and awaits content not yet written; foreclosing recognizes the content is
  already written and designated.
  Item 2: The cl-d08/cl-d06 distinction is a ledger-mechanism detail, not an axis-movement gating
  condition. Treating it as a gate would require tracking which ledger entry "authorized" a given
  unit of axis movement, which the substance framework does not do.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0072 | 2026-06-02 | SLOW (user-proxy, RUNBOOK R1)

question: |
  b01c11 /and-substance chapter Phase 5.5 cold-read disposition (Step 3).
  CHUNK-CLASS-B: summary maps to goal; strict-CONTINUE=No on attempt 2 (after revise).
  Residual complaints: (a) low on-page jeopardy / nobody at risk / nothing goes wrong;
  (b) load-bearing proper nouns (Otto, Rhaenyra, Dragonstone, Corwick, Halvard) introduced
  without context. All upstream gates PASS (audience 3/3 ACCEPT, dramatist ACCEPT on attempt 2,
  auditor 0 HARD). One revise attempt remaining in 3-try cap.
  Counter: consecutive-airless concern (DEC-0066/0067; N=5 c06-c10). Does the
  consecutive-quiet pattern change the call from P to R?

context: |
  Silent chapter-production run for b01c11 (RUNBOOK Rule 1). c11 is a RISING consolidation
  chapter between two CLIMAX chapters (c10, c12). Design: surveillance architecture at peak
  load before collapse phase opens. Dramatist ACCEPT (attempt 2) explicitly confirms
  "genuine stakes-accumulation; rising shape correct, does not over-climax."
  Substance contract: 3/3 audience SUBSTANCE-FELT, 0 FLAT, 0 SUSPECT, Earth-Bet CLEAN.

options:
  R: burn last revise to add on-page jeopardy / reduce proper-noun opacity
  P: proceed; record as CHUNK-CLASS-B SHIPPED-WITH-RISK-RECORDED; carry risk to /and-stitch
  S: substance-contract redo (not warranted — no reviewer faults the delta)
  ESCALATE: surface to principal

decision: P — proceed with risk recorded (CHUNK-CLASS-B / SHIPPED-WITH-RISK-RECORDED)

basis: ltm:DEC-0060 + ltm:DEC-0062 (exact same decision shape; both P)
+ methodology:3a (reversibility — burning last revise risks over-torquing into false climax)
+ methodology:3c (blast radius — R affects c12 structural relationship; P does not)

rationale: |
  The cold-read objection splits cleanly into two non-fixable-at-chunk-level categories:
  (a) Low jeopardy is the contractual design of a RISING consolidation chapter sitting between
  two CLIMAX chapters. All three audience reviewers felt substance; the dramatist endorsed the
  rising shape explicitly on attempt 2. Burning the last revise to manufacture jeopardy would
  violate the substance design that every upstream gate endorsed, and risks making c11 step on
  c12's earned climax. This is design-inherent, not a chunk delivery failure.
  (b) Cold-context proper-noun opacity is universal for chapter 11 of a serial. An invested reader
  (c01-c10) arrives with full context; the uninformed cold-reader is not the target audience.
  Both complaint categories are correctly routed to /and-stitch Phase 8.5 Check 3 (cold-context
  risk arming) and Phase 9 jeopardy scrutiny — not to a chunk revise that would only damage the
  design.
  Counter-consideration (consecutive-airless N=5): the concern is about *prose airlessness*
  (apparatus-density in rendered stitch), not about dramatic jeopardy or proper-noun opacity.
  These are distinct failure classes. If c11 ships with airless prose, that is a stitch-layer
  issue properly addressed by /and-cohere (flagged in DEC-0070). R would apply a chunk-revise
  to a prose-layer problem — wrong layer, wrong tool.

trade-off: |
  P accepts that the cold-read remains at strict-CONTINUE=No on the assembled draft. Mitigation:
  /and-stitch Phase 8.5 + Phase 9 have explicit jeopardy-scrutiny and cold-context-risk tooling
  armed by cold_read_risk_carry; /and-cohere is on-deck after c11 for the consecutive-airless
  pattern. R would spend the last revise attempt and risk a false-climax that undercuts c12.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0073 | 2026-06-02 | PROCESS-CRITIC (b01c11 bone-gate — ABSTRACTION-DOMINANT fire-and-accept on feed-POV chapter)

mode: process-critic
trigger: /and-write b01c11 Phase 6 bone-gate — 0 HARD / 2 SIGNAL (ABSTRACTION-DOMINANT s02 + s03, both ACCEPTED-with-rationale); Chapter PASS, 3/3 SUBSTANCE-FELT
gate_path: .claude/commands/and-write.md#phase-6
verdict: OK-MERGED-INTO PROP-0030 + PROP-0031 (recurrence_count 3→4 on both)

question: |
  Does ABSTRACTION-DOMINANT firing-and-accepting on feed-POV chapters warrant a process change?
  Candidates: (1) feed-POV grounding-quota carve-out at Phase 6; (2) tighter coupling to /and-cohere
  apparatus-density tracker; (3) stitch-layer obligation rather than bones-layer SIGNAL; (4) OK.

decision: OK-MERGED-INTO PROP-0030 + PROP-0031

rationale: |
  The existing process is functioning correctly on all three dimensions:

  (1) Gate behavior. ABSTRACTION-DOMINANT is correctly classified as a SIGNAL (not HARD) on
  architecture-licensed abstract bones. The accept-with-rationale path is the designed handling
  when abstraction is design-intrinsic (feed relay structure + behavioral ABSENCE as central event),
  not authoring laziness. The gate fires, the rationale is logged, the stitch-carry obligation is
  set. This is the process working.

  (2) Downstream handling. The stitch-carry to /and-stitch Phase 4 physical-materiality
  reinforcement is the designed downstream obligation for accepted ABSTRACTION-DOMINANT SIGNALs.
  3/3 audience SUBSTANCE-FELT confirms the chain is delivering on that obligation. A feed-POV
  carve-out that suppressed the SIGNAL would *remove* the stitch-carry trigger — net-negative,
  because the SIGNAL is load-bearing as an advisory arm to stitch.

  (3) Cross-chapter accumulation. The consecutive-abstract concern (c10+c11 both abstract;
  consecutive-airless N=6, the threshold named in DEC-0067) is PROP-0030/0031's designed target.
  Both proposals are open and await principal triage. Adding a new accumulation-warning gate at
  the bones layer would duplicate PROP-0030/0031 rather than addressing their root cause (chapter-
  isolated scoring cannot see cross-chapter accumulation — that is structural, not a gap in the
  Phase 6 gate). The correct action is to merge c11 as evidence into the two open proposals and
  note that N=6 is at the DEC-0067 threshold, not to author a third accumulation-warning proposal.

  Process discrimination: could a stricter existing gate have caught a process failure here?
  No. There is no process failure: the SIGNAL fired, the rationale was logged, the audience
  confirmed substance delivery. The stitch layer will carry the physical-materiality obligation.
  The only potential concern — cross-chapter accumulation — is already the target of open
  proposals PROP-0030/PROP-0031.

  DEC-0067 named N=6 as the threshold for "a separate warning gate becomes warranted." N is now
  6 (c06/c07/c08/c09/c10/c11). However: the DEC-0067 framing was "no new proposal at N=5;
  threshold for potential new proposal is N=6." At N=6 the consideration is whether to open a
  new proposal or continue merging into the existing open proposals. Assessment: PROP-0030/PROP-0031
  are already open and their proposed_diff already addresses the cross-chapter accumulation class
  precisely (cross-chapter cold-read primitive + iteration loop). The accumulation debt at N=6 is
  the case for triage urgency on those proposals, not a case for a third overlapping proposal.
  Proposing a new accumulation-warning gate at N=6 when N=1 open proposals exist for the same
  class is noise, not signal. Merge and flag triage urgency.

  Triage urgency note: PROP-0030 + PROP-0031 have been open since 2026-05-31. Accumulation-count
  N is now at 6 (the DEC-0067 threshold). If both proposals remain untriaged through c12-c13,
  the accumulation debt will be larger and the /and-cohere convergence run more expensive.
  Principal triage of PROP-0030/PROP-0031 is strongly recommended before c13.

trade-off: |
  Merging vs. proposing a new accumulation-warning gate:
  - A new gate (e.g., "after 2 consecutive ABSTRACTION-DOMINANT chapters, HARD-abort at /and-write
    unless principal acknowledges") would be high-blast-radius, would require /and-write to read
    cross-chapter state it does not currently read, and would fire on design-intrinsic content
    (the project's feed-POV architecture deliberately produces abstract chapters). False-positive
    rate would be high; the carve-out logic needed to avoid false-positives would reproduce the
    accept-with-rationale path that already exists at Phase 6.
  - Merging into PROP-0030/PROP-0031 accepts that the per-chapter gate is not the right instrument
    for a cross-chapter accumulation problem. The accumulation problem requires a cross-chapter
    review primitive (/and-review cohere) + iteration loop (/and-cohere) — both of which
    PROP-0030/PROP-0031 define. The cost of not merging is a premature gate that would suppress
    the stitch-carry trigger without solving the accumulation problem.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0074 | 2026-06-03 | FAST (user-proxy: Phase 9 terminal-gate disposition)

question: /and-stitch b01c11 Phase 9 terminal-gate disposition. Cold-read recovered all central events; CONTINUE=No ("almost nothing happens / no question pulling me forward"); staging PASS (all 4 central-event bones on-page); readability READABLE; Phase 8.5 PASS; 2 LOW advisories (design-inherent). Class-B FAIL maps exactly onto DEC-0072 carried categories: (1) low on-page jeopardy / design-inherent RISING chapter; (2) cold-context proper-noun load. Disposition candidates: SHIPPED-WITH-CAVEATS / FAIL-REVISE / ESCALATE.
context: Phase 9 coupling rule: chunk_cold_read.verdict == SHIPPED-WITH-RISK-RECORDED (DEC-0072); live Class-B FAIL hits ONLY the carried categories → ships terminal as SHIPPED-WITH-CAVEATS without re-asking. DEC-0072 dispositioned both items explicitly. Staging clean, readability READABLE; no structural or airlessness FAIL. Consecutive-abstract N=6 already flagged for /and-cohere before c13 (DEC-0073).
options: SHIPPED-WITH-CAVEATS | FAIL-REVISE (1 retry via /and-write revise --from-signals) | ESCALATE

decision: SHIPPED-WITH-CAVEATS

basis: ltm: DEC-0072 (chunk-level carried disposition authorizes terminal ship on exact-category match) + Phase 9 coupling rule. Runbook R2's generic FAIL-REVISE path is overridden by the coupling rule when the FAIL is design-inherent and pre-dispositioned at chunk level.

rationale: DEC-0072 pre-adjudicated both FAIL drivers: low jeopardy is the substance contract of a RISING consolidation chapter (endorsed by 3/3 audience SUBSTANCE-FELT + dramatist ACCEPT + auditor 0 HARD), and proper-noun opacity is serial mid-point context-noise not in-chunk holes. The coupling rule exists precisely to prevent a retry that would consume 1 cap and risk a false-climax undercutting c12, against a finding that cannot be fixed without violating the endorsed substance contract. Staging is clean and readability is READABLE — the two conditions that would warrant a structural retry (URI-STITCH-SPINE-STAGING gap or AIRLESS) are both absent.

trade-off: FAIL-REVISE would spend the 1 retry cap on a diagnosable non-fixable finding, with seed-variance risk and potential false-climax undercutting c12. ESCALATE is unnecessary — the coupling rule and DEC-0072 together constitute a pre-authorization that removes the irreversibility / uncertainty conditions warranting escalation.

caveat-string: "Class-B FAIL: CONTINUE=No — low on-page jeopardy (design-inherent RISING chapter between c10-CLIMAX and c12-CLIMAX; substance contract endorsed 3/3 audience + dramatist + auditor) + cold-context proper-noun load (serial mid-point; Halvard/Corwick/Otto/Rhaenyra opacity is context-noise, not in-chunk hole). Carried from DEC-0072 chunk-level disposition. Consecutive-abstract N=6 (c10+c11) flagged for /and-cohere before c13 per DEC-0073. Staging clean; readability READABLE."

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0075 | 2026-06-03 | SLOW (process-critic)

mode: process-critic
trigger: /and-stitch b01c11 Phase 9.5 — SHIPPED-WITH-CAVEATS (DEC-0074 coupling-rule ship); 2nd consecutive low-jeopardy/abstract cold-read chapter (c10+c11); consecutive-abstract N=6. Question: is the process working, or does recurrence of low-jeopardy cold-read FAILs across consecutive chapters warrant a new process change (book-level jeopardy-distribution check, tighter /and-cohere coupling, or consecutive-design-inherent-low-jeopardy cap)?
gate_path: .claude/commands/and-stitch.md#phase-9
secondary_gate_paths: [.claude/commands/and-substance.md#phase-5.5]
verdict: OK-MERGED-INTO PROP-0030 + PROP-0031

question: |
  Does the RECURRENCE of low-jeopardy cold-read FAIL (c10+c11 consecutive) constitute a process
  failure warranting a new gate — book-level jeopardy-distribution check, tighter /and-cohere
  coupling, or a cap on consecutive design-inherent-low-jeopardy chapters before a cohere gate
  fires? Or is the process working correctly?

context: |
  c10 and c11 both shipped via SHIPPED-WITH-CAVEATS (DEC-0070 / DEC-0074). Both had Class-B
  FAIL cold-reads (CONTINUE=No). Both had the same design-inherent signature: low on-page
  jeopardy endorsed 3/3 audience + dramatist + auditor 0 HARD, and cold-context proper-noun
  load. Coupling rule fired correctly on both. DEC-0073 already merged b01c11 as N=6 into
  PROP-0030 + PROP-0031 with triage-urgency note. /and-cohere before c13 on-deck per DEC-0073.

decision: OK-MERGED-INTO PROP-0030 + PROP-0031 (recurrence evidence already appended by
DEC-0073; this dispatch confirms no new signal beyond that merge)

basis: |
  methodology:3e (convention — DEC-0073 same-session performed this exact discrimination and
  reached OK-MERGED) + methodology:3c (blast radius — a new proposal for the same target/class
  adds noise without adding signal; the existing open proposals already subsume all three
  candidate process changes)

rationale: |
  Three candidate process changes evaluated:

  1. BOOK-LEVEL JEOPARDY-DISTRIBUTION CHECK. Would require /and-stitch to read cross-chapter
     state it does not hold, and would fire on design-intrinsic content (RISING chapter low
     jeopardy IS the contractual design; carve-out logic would reproduce the existing coupling
     rule). Same discrimination as DEC-0073 applied to accumulation-warning gate: wrong
     instrument class; PROP-0030 /and-cohere primitive is the right instrument.

  2. TIGHTER /AND-COHERE COUPLING. Already the proposal surface of PROP-0030 + PROP-0031
     (recurrence_count: 4 on both). PROP-0030 Phase 1 Q2 (setup→payoff distribution) + Q7
     (sub-section feel) + Q6 (apparatus-register load) collectively address jeopardy-
     distribution concerns. Duplicating into a new proposal adds no value.

  3. CONSECUTIVE-DESIGN-INHERENT-LOW-JEOPARDY CAP WITH AUTO-COHERE TRIGGER. DEC-0073 already
     named /and-cohere before c13 as the designed response to N=6 — the cap is effectively
     operative via the triage-urgency note and the principal's stated intent. Wiring it
     mechanically (cross-chapter counter + HARD-abort) has S-M cost and small marginal benefit
     given the principal already has the intent written. Wait for triage on PROP-0030/0031
     first; if they are accepted, the /and-cohere trigger mechanism becomes available and a
     mechanical cap can be proposed as a lightweight modification then.

  PROCESS WORKING CORRECTLY. Coupling rule prevented a retry on a non-fixable finding.
  Upstream gates endorsed the design unanimously. Cross-chapter accumulation debt is PROP-0030/
  0031's designed target; those are open and triage-urgent at N=6. No new proposal warranted.

trade-off: |
  Risk of OK: jeopardy-distribution as a distinct dimension of accumulation is not explicitly
  named in PROP-0030/0031 — it is subsumed under apparatus-register accumulation. Mitigated
  by: (a) PROP-0030 Q2/Q7 would surface it in a cohere run; (b) the two failure classes co-
  occur in this run (same /and-cohere instrument addresses both); (c) separating them into
  a new proposal adds a third open proposal for the same fix.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0076 | 2026-06-03 | FAST (user-proxy, RUNBOOK R1)

mode: user-proxy
trigger: /and-substance chapter b01c12 Phase 5.5 chunk cold-read disposition
context: |
  b01c12 (d08 climax: coverage-gap refusal protecting Wren + Khepri-repetition threshold
  surfacing-and-suppression) returned CHUNK-CLASS-B. Cold-reader summary maps to chapter goal
  (Q6-level pass). Strict-CONTINUE (Q7 post-no-charity) = NO. Three decomposed causes:
  (1) Cold-context holes — all established across c01–c11; Khepri/Gold-Morning opacity is the
      Earth-Bet proper-noun fence operating by design (worm-canon-pedant ruled s04 surfacing
      CLEAN).
  (2) s04 seam — cold-reader calls s04 "a different chapter's climax stapled on." Dramatist
      independently examined and ACCEPTED as climax-sound (s04 = terminal interior coda,
      consequence-train of s03 refusal). Defensible design; prose-rendering risk.
  (3) Apparatus-register density — "coverage/ledger/tranche/architecture" apparatus-metaphor
      opacity. Recurring concern; DEC-0073/0075 flagged N=6 for /and-cohere before c13.

decision: P — Proceed with risk recorded (SHIPPED-WITH-RISK-RECORDED)

cold_read_risk_carry items for /and-stitch Phase 8.5 + Phase 9:
  1. strict-CONTINUE=No (Class-B design-inherent; pre-dispositioned)
  2. s04 seam — verify threshold-trigger lands as causally-earned consequence of s03 refusal,
     not an arbitrary scene-pivot; stitcher must render the interior coda's causal chain legible
     without expository bridge.
  3. apparatus-register density — ledger/tranche/architecture vocabulary must not muffle the
     Khepri beat; Phase 8.5 central-event-muffle check must explicitly test whether Khepri's
     name/presence registers through the accounting register at the beat where it appears.
  4. Khepri/Gold-Morning proper-noun opacity — design-inherent; Phase 9 may not FAIL on this
     cause alone (coupling rule: cold-context gaps on a climax chapter mid-serial are not
     delivery failures).

basis: |
  DEC-0072 (b01c11 Class-B) + DEC-0074 (c11 Phase 9 ship) + DEC-0060 (b01c08) exact precedent
  chain. All three same pattern: summary maps, dramatist ACCEPT, upstream gates clean (2-of-3
  audience SUBSTANCE-FELT; auditor PASS 0 HARD), strict-CONTINUE=No driven by cold-context +
  design-inherent causes. (R) is the Class-A default, not the Class-B default. (S) is reserved
  for when (P) is unacceptable — upstream gates at PASS unanimous, so (P) is acceptable. The
  s04 seam concern is a prose-rendering risk that /and-stitch Phase 8.5 is designed to catch;
  it does not belong at the chunk revision layer. The apparatus-density concern is the same
  N=6 /and-cohere accumulation (DEC-0073/0075) — a chunk-layer re-author would not address it.

trade-off: |
  Risk of P: s04 seam may not render as causally-earned under stitch. Mitigated by: (a) cold_
  read_risk_carry item 2 explicitly arms Phase 8.5 with the causal-chain test; (b) Phase 9
  coupling rule pre-dispositions cold-context-caused CONTINUE=No; (c) if stitch fails the seam
  test, /and-write revise targets only s04 bones, not full re-chunk. Apparatus-density risk
  mitigated by item 3 (Khepri-beat explicit) + /and-cohere on deck before c13.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0077 | 2026-06-03 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c12-bone-gate.md
  source_verdict: FAIL — 3 HARD (fault-001/003/004; single structural gap: s04 HELD-AXIS-NOT-WITNESSED for political_register-prot + social_tether-antag); 2 SIGNAL accept-with-rationale (ABSTRACTION-DOMINANT s04; REGISTER-AS-MANNERISM). Resolved in-cycle.
  gate_path: .claude/commands/and-write.md#phase-6
context: |
  Two distinct patterns in b01c12's /and-write run:

  PATTERN A — HELD-AXIS-NOT-WITNESSED (Phase 6 HARD): s04 scene contract declared
  political_register-prot + social_tether-antag as held axes; zero bones in s04 carried
  either axis in axes_held[]. Resolved in-cycle (fixer attached axes_held to two existing
  bones). Fourth chapter-level occurrence of this class (c04: 5 axes; c06: 1 axis;
  c10: 9 axes; c12: 2 axes). PROP-0011 covers this class.

  PATTERN B — 15 unpaid-chatter bones (Phase 2 FAULT-BONE-DELTA-MALFORMED): screen-writer
  authored grounding/setup bones as shape=chatter with null cost_ledger_anchor AND empty
  axes_held[] across all 4 scenes (15/42 = 36%). Required a Phase 2 fixer pass. No prior
  proposal covers this specific failure class at this scale (c09: 2; c04's FAULT-BONE-
  DELTA-MALFORMED was magnitude pair-splits, not null-anchor chatter).

decision: |
  (A) OK-MERGED-INTO PROP-0011. Increment recurrence_count 3→4. Add b01c12 evidence ref.
      Proposed_diff unchanged (Phase 1 step 4a completion gate for held-axis witnessing).
      In-cycle fix confirms root cause is Phase 1 brief gap, not bone-count deficiency.

  (B) OK — hold at first occurrence. Pattern B is a first-occurrence at scale. Phase 2 caught
      it correctly; in-cycle fixer resolved all 15 at low cost. No gate failed to catch it;
      no irreversible consequence. Non-catastrophic first occurrence → hold for recurrence.

basis: |
  (A) PROP-0011 mandatory merge (same change_type, same target, same root cause, 4th occurrence).
  (B) Methodology: first-occurrence rule for non-catastrophic gate-caught failures. Gate chain
      functioning as designed. Phase 1 self-check addition would be a second mandated completion
      gate alongside step 4a; overhead cost exceeds periodic fixer-pass cost at single occurrence.

rationale: |
  PROP-0011 fully addresses Pattern A. The rollup-attribution note already added at count=3
  covers the b01c12 root cause (axes were declared but omitted from bone-level axes_held[]).
  No new proposed_diff content needed; the merge is administrative.

  Pattern B: 15 is anomalous (36% of bones) but mechanically simple to fix — every chatter
  bone needs either a held-axis or an anchor. Phase 2 is the correct catching gate; it fired.
  Adding a Phase 1 self-check creates friction for a pattern that appeared at scale only once
  across 12 chapters. Hold until recurrence at c13+ to determine if it's systematic.

trade-off: |
  (A) None — merge is mandatory by schema.
  (B) Not proposing risks a repeat fixer pass at c13+. Proposing prematurely risks adding
  Phase 1 overhead for a pattern that may not recur (absent from c05–c11 at scale).
  Phase 2 fixer pass for 15 chatter bones costs less than a mandated completion-gate.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0078 | 2026-06-03 | FAST (user-proxy, RUNBOOK R1)

mode: user-proxy
trigger: /and-stitch b01c12 Phase 9 terminal-gate disposition
context: |
  b01c12 Phase 9 split picture:
  - Completeness PASS: central events recovered (ledger-refusal blank-source-field, five-ward
    deployment, breach-column cost-entry withholding "older word"). 0 spine-staging-gaps,
    0 FAIL, 7/7 central-event clusters STAGED. Prose-rationale-mute CLEAN. Phase 8.5 PASS
    (@38 recognition registers through apparatus register, s04 causal-seam reads CAUSED).
    No Step-4 cluster fired.
  - Cold-read CONTINUE=No + low jeopardy + "airless" read: cold-reader complaint categories
    are (1) cold-context proper-noun opacity (Khepri/Gold-Morning/Wren/Otto — prior-chapter-
    resident + Earth-Bet fence by design); (2) design-inherent low jeopardy (CLIMAX of
    internal/offstage stakes by substance contract); (3) apparatus-register density. All three
    categories are explicitly named in DEC-0076 cold_read_risk_carry items 1/3/4. No new
    complaint categories.
  Precedent: DEC-0072 (c10 Phase 9) + DEC-0074 (c11 Phase 9) = SHIPPED-WITH-CAVEATS on
  identical pattern. DEC-0076 coupling rule explicitly states "Phase 9 may NOT FAIL on
  cold-context cause alone."
  Phase 4 voice-embodiment: 0 VOICE-APPARATUS-DEFAULT, 0 EMBODIMENT-BLOCKED.
  Grounding adds: prose-rationale-mute CLEAN.
  Phase 8.5 context-aware: person present — "airlessness" is cold-context reader effect.
  N=7 apparatus-density already routed to /and-cohere before c13 (DEC-0073/0075/0077, HIGH).

options:
  - (A) SHIPPED-WITH-CAVEATS: terminal ship; CONTINUE=No on pre-authorized categories;
        apparatus-density routes to /and-cohere (not per-chapter depth pass).
  - (B) PASS-WITH-DEPTH-PASS-REQUIRED: terminal ship but mandate /and-write revise
        --from-signals + re-cascade before book-close.

decision: (A) SHIPPED-WITH-CAVEATS. Apparatus-density confirmed routed to /and-cohere before c13.

basis: |
  ltm:DEC-0074 (c11 coupling rule) + ltm:DEC-0072 (c10 coupling rule) + DEC-0076 (b01c12
  pre-authorization of Phase 9 disposition on exact these categories). All three cold-read
  CONTINUE=No categories are pre-authorized design-inherent or cold-context categories.
  methodology:3a (reversibility) — (B) is costlier and targets the wrong layer; apparatus-density
  is a cross-chapter cross-stitch concern, not a per-bone failure at c12.

rationale: |
  The coupling rule (DEC-0076 item 4) is deterministic: Phase 9 may not FAIL on cold-context
  gaps on a climax chapter mid-serial. All three CONTINUE=No categories are pre-authorized:
  (1) cold-context proper-noun opacity — design-inherent Earth-Bet fence; (2) design-inherent
  low jeopardy — internal CLIMAX offstage stakes by substance contract; (3) apparatus-density —
  N=7 cross-chapter accumulation, /and-cohere is the correct resolution layer. No new complaint
  category exists that would distinguish c12 from c10/c11. Phase 4 applied person-first
  throughout (0 apparatus-default bones), grounding-ledger satisfied (prose-rationale-mute
  CLEAN), Phase 8.5 found the person present with context — the "airless" read is cold-context
  reader effect, not a bone-layer or stitch-layer failure. (B) would mandate a depth pass
  targeting apparatus-density at the per-chapter layer when the correct fix is already scheduled
  at the cross-chapter /and-cohere layer; that is the wrong repair surface. c10 and c11 both
  shipped SHIPPED-WITH-CAVEATS on this exact pattern; consistency requires the same verdict.

trade-off: |
  Accepting SHIPPED-WITH-CAVEATS without a depth pass means the apparatus-density concern is
  not addressed until /and-cohere. Risk: if /and-cohere is skipped or deferred past book-close,
  c12's airlessness remains unaddressed in the terminal draft. Mitigated by: (a) /and-cohere is
  already stamped HIGH urgency (DEC-0073/0075/0077) and is the explicitly suggested next step
  after the chapter-production run ends; (b) the depth pass under (B) would target bones in
  isolation and cannot address the cross-chapter register accumulation — it would be lower-value
  spend on the same content.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0080 | 2026-06-03 | FAST (user-proxy, RUNBOOK R1)

question: Branch choice at b01c12 chapter boundary: (A) /and-cohere b01 before c13, or (B) produce b01c13 now. Principal said "continue."

context: |
  c12 just shipped SHIPPED-WITH-CAVEATS (DEC-0078) — 3rd consecutive on same cause
  (apparatus-register density / cold-context / design-inherent). N=7 consecutive
  apparatus-dense chapters (c06-c12). /and-cohere has been a standing HIGH-urgency
  recommendation reaffirmed five times (DEC-0073, DEC-0075, DEC-0077, DEC-0078,
  DEC-0079). PROP-0037 (DEC-0079) explicitly proposes a HARD-abort at /and-substance
  chapter Phase 0 when consecutive_shipped_with_caveats >= 3 without cohere acknowledgment
  — not yet implemented, so c13 is not mechanically blocked, but the process-critic intent
  is unambiguous. Producing c13 now would very likely produce a 4th SHIPPED-WITH-CAVEATS on
  the same unaddressed accumulation.

options: (A) /and-cohere b01 first; (B) produce b01c13 now

decision: (A) /and-cohere b01 first.
basis: ltm:DEC-0073/0075/0077/0078 (same ruling every time; no new signal favoring B)
rationale: |
  Five prior dispatches ruled cohere-before-c13. At N=3 consecutive SHIPPED-WITH-CAVEATS
  on the same cross-chapter accumulation problem (which per-chapter gates cannot address),
  "continue" means run the outstanding HIGH-urgency obligation before starting the next
  chapter — not defer it a sixth time. The process-critic proposal (PROP-0037) gives the
  same answer from the process side. The cross-chapter airless-read is a known accumulation
  that only /and-cohere addresses; producing c13 into that accumulation is not forward motion.
trade-off: |
  /and-cohere is a sizable operation; the principal may have intended "continue" to mean
  "next chapter." But five consistent prior rulings at this same boundary make the intent
  unambiguous: cohere was already the declared obligation before c13 ran. Option B here
  would be the sixth consecutive bypass of the same HIGH-urgency flag on the same cause.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0079 | 2026-06-03 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01c12-2026-06-03.md
  source_verdict: SHIPPED-WITH-CAVEATS (DEC-0078) — 3rd consecutive SHIPPED-WITH-CAVEATS on apparatus-density / cold-context / design-inherent low-jeopardy pattern (c10 DEC-0072, c11 DEC-0074, c12 DEC-0078); N=7 consecutive-abstract chapters (c06-c12).
gate_path: .claude/commands/and-stitch.md#phase-9
verdict: PROCESS-CHANGE-PROPOSED PROP-0037

question: |
  Does the 3rd consecutive SHIPPED-WITH-CAVEATS on apparatus-register density warrant a
  process change — specifically, making /and-cohere a HARD gate before the next chapter when
  N consecutive SHIPPED-WITH-CAVEATS >= 3 — rather than a standing HIGH-urgency recommendation
  that keeps deferring? Or is this already covered by an open cohere-cadence proposal
  (PROP-0030/0031) and should be merged?

context: |
  DEC-0075 (2nd consecutive SHIPPED-WITH-CAVEATS at N=6/2-consecutive) evaluated three
  candidate process changes including "consecutive-design-inherent-low-jeopardy cap with
  auto-cohere trigger" and deferred it: "Wait for triage on PROP-0030/0031 first; if they
  are accepted, the /and-cohere trigger mechanism becomes available and a mechanical cap can
  be proposed as a lightweight modification then." Condition: PROP-0030/0031 triage first.
  PROP-0030 + PROP-0031 remain status: open / untriaged as of this dispatch. N is now 7
  consecutive-abstract; consecutive SHIPPED-WITH-CAVEATS is now 3 (c10/c11/c12).

decision: PROCESS-CHANGE-PROPOSED PROP-0037

basis: |
  Step 2 (proposals matching): No open proposal covers the specific mechanism proposed —
  HARD-abort at /and-substance chapter Phase 0 when consecutive SHIPPED-WITH-CAVEATS >= 3.
  PROP-0030 targets a new /and-review cohere subcommand (the cold-read primitive). PROP-0031
  targets a new /and-cohere command body (the iteration loop). Neither targets a Phase 0
  HARD-abort on the next chapter production command as the enforcement mechanism.

  Step 3 (content vs. process): The per-chapter pipeline (Phase 4 voice-embodiment + grounding-
  ledger + Phase 9 cold-read gate) applied correctly at c10/c11/c12 — it caught the airlessness
  and dispositioned it correctly via the coupling rule. The process failure is not in any
  individual gate: it is that the coupling rule, while technically correct per-chapter, is
  now absorbing a cross-chapter accumulation that the chain has no structural mechanism to force
  resolution on. /and-cohere is the correct remedy, and it is on-deck, but the process has no
  gate that PREVENTS the principal from starting c13 without running it. The recommendation is
  durable-but-bypassable. Three consecutive SHIPPED-WITH-CAVEATS on the same pattern means the
  recommendation has been bypassed twice already (c10 to c11 without /and-cohere; c11 to c12
  without /and-cohere). The process needs a HARD enforcement point.

  Step 4 (DEC-0075 deferral re-examined): DEC-0075's deferral condition was "wait for PROP-0030/
  0031 triage first, THEN propose the mechanical cap." That condition has not been met, but
  PROP-0037 is discriminated from the DEC-0075 mechanism: DEC-0075 was about wiring the
  auto-trigger inside the not-yet-implemented /and-cohere command body. PROP-0037 targets a
  different, smaller, immediately-implementable enforcement surface: a Phase 0 HARD-abort in
  /and-substance chapter that halts chapter production and surfaces the /and-cohere obligation
  to the principal BEFORE the chapter runs. This does not require /and-cohere to exist as a
  command — the HARD-abort instructs the principal to run it (whether that means the
  implemented /and-cohere, or a manual sub-section coherence review, or any equivalent). It
  is the "obligation-surfaces-at-the-right-moment" gate; PROP-0030/0031 are the
  "obligation-execution" machinery. They are orthogonal.

  Step 5 (methodology): reversibility (HARD-abort is bypassable by principal via an explicit
  acknowledgment stamp — lowest-cost non-destructive enforcement) + blast radius (single Phase
  0 check; does not touch the chapter authoring chain itself) + optionality (principal can
  proceed by running /and-cohere first, or by stamping explicit acknowledgment) support this
  as the minimum viable change. S-cost.

rationale: |
  At N=3 consecutive SHIPPED-WITH-CAVEATS the pattern is no longer noise — it is a recurring
  cross-chapter debt the chain's per-chapter gates are structurally incapable of addressing
  (by design: they are isolated). The coupling rule correctly ships each chapter; the
  /and-cohere recommendation is correctly stamped HIGH; but the process has no point where it
  says STOP and requires the cohere to run before proceeding. Three consecutive bypasses is
  the threshold at which the standing recommendation becomes an active liability. Adding a
  Phase 0 HARD-abort at /and-substance chapter Phase 0 closes that gap at minimum cost without
  requiring PROP-0030/0031 to be implemented first.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0081 | 2026-06-03 | SLOW (user-proxy)

question: |
  /and-cohere b01 c06-c12 iteration 1 returned FAIL-COHERE (load-bearing fail: naive cold-reader
  Q6 apparatus-register cumulative load, localized to italic chapter-prologues by cape-fic). Three
  options: (A) full /and-write revise --from-signals on c08/c09/c11 + re-cascade (~40+ dispatches),
  (B) targeted prologue-variation pass on all 7 prologues + route structural CAUTIONs to
  parking-lot/book-substance + re-cohere, (C) record FAIL-COHERE as diagnostic, hold loop, route
  everything to back-half, proceed to c13.

context: |
  - Design-tension (apparatus-register density) pre-dispositioned 3x as design-inherent (DEC-0072/
    0074/0078). Substance-aware cape-fic audience: 3x SUBSTANCE-FELT — body earns the 7-chapter run.
  - Load-bearing Q6 FAIL localized by cape-fic to the italic per-chapter prologues (7x near-identical
    restatement of standing conditions — skim-formula by c09). Naive cold-reader: prologues "glue
    rather than flow."
  - Structural CAUTIONs (Halvard counter-argument drift, c11 antagonist-pressure gap, Sera hole,
    Dragonstone-receipt deferred) are book-substance / back-half items — not per-chapter bones-revise
    targets.
  - Option A risk: per-chapter bones already carry the correct deltas; bones-revise cannot address
    cumulative cross-chapter prologue repetition; structural items are wrong layer; ~40+ dispatches
    against a design-tension dispositioned 3x at near-zero expected movement on Q6.
  - DEC-0079: PROP-0037 just proposed a Phase 0 HARD-abort at /and-substance chapter when consecutive
    SHIPPED-WITH-CAVEATS >= 3; /and-cohere first is the current obligation.

options:
  A: full /and-write revise --from-signals c08/c09/c11 + re-cascade each + re-cohere (~40+ dispatches)
  B: targeted prologue-variation pass (all 7 prologues) + route structural CAUTIONs to parking-lot +
     re-run /and-review cohere to see if Q6 clears
  C: record FAIL-COHERE as diagnostic, hold loop (status: held), route everything to back-half + c13

decision: (B) targeted prologue-variation pass on all 7 prologues + route structural CAUTIONs to
  parking-lot/book-substance + re-cohere

basis: |
  Goal:2 (cost discipline) + methodology 3b (cost: cheapest path that addresses the convergent
  finding) + 3c (blast radius: per-chapter bones-revise touches 3 chapters + re-cascades, vs.
  prologue variation is scoped to 7 prologue blocks only) + 3a (reversibility: option B is fully
  reversible — if re-cohere still FAILs, A remains available). Option C abandons a fix with a
  known low-cost execution path; the diagnostic work is done — the fix target is identified.
  Option A is high-cost against the wrong layer for the localized finding.

rationale: |
  The convergent evidence from both forks points at one specific structural element: the 7 italic
  prologues restate near-identical standing conditions across c06-c12. That is the "skim-formula"
  and the "glue rather than flow" complaint. The apparatus-density of the BODY is not the complaint
  — the cape-fic audience calls that SUBSTANCE-FELT. The prologues are separable from the bone-layer
  substance and can be varied without touching the bones-revise layer. Vary the 7 prologues to break
  skim-formula (break identical restatement of standing conditions), route the structural CAUTIONs
  (Halvard-return, c11-antagonist-pressure, Sera, Dragonstone-receipt) to the parking lot with
  back-half / /and-review verdict b01 as the resolving scope, then re-run /and-review cohere.
  If Q6 clears, the cohere loop closes at far lower cost than option A. If Q6 does not clear after
  prologue variation, the diagnostic is richer and option A remains available as a next step.

  The structural CAUTIONs are not "ignore and defer" — they are wrong layer for the cohere loop.
  The correct layer is book-substance + /and-review verdict b01. Parking-lot with explicit back-half
  scope is the right routing. Notably, option A cannot fix the structural items either — bones-revise
  on c08/c09/c11 cannot supply Halvard's return or a c11 antagonist move. Both B and A defer them;
  B is cheaper on the one item that can be fixed now.

trade-off: |
  Option B does not guarantee Q6 clears. If re-cohere still FAILs after prologue variation, a
  second loop will be needed (possibly escalating to A). This is accepted: option B is a low-cost
  probe that either resolves the loop cheaply or produces sharper evidence before committing to A.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no
