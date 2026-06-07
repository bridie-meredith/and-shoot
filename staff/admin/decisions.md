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

---

## DEC-0082 | 2026-06-03 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: cohere-converged-caution
  source_report: active-project/staff/reviews/cohere-naive-b01-c06-c12-20260603T152850Z.md
  source_verdict: CAUTION-COHERE (converged, iteration 2; load-bearing naive-Q6 FAIL->CAUTION via DEC-0081 prologue-variation)
gate_path: .claude/commands/and-cohere.md#phase-2
secondary_gate_paths: [.claude/commands/and-stitch.md#phase-9, .claude/commands/and-facets.md#phase-2.5]

question: |
  /and-cohere b01 c06-c12 converged at CAUTION-COHERE in 2 iterations via targeted prologue-variation
  (DEC-0081 option B, not full per-chapter revise-cascade). Three process candidates:
  (1) Should /and-facets exposition @0 bridge carry cross-chapter prologue-variation discipline
      so skim-formula doesn't accumulate in the first place?
  (2) Should the cohere-triage heuristic (FAIL localizes to prologues → targeted presentation-pass
      preferred over per-chapter bones-revise) be codified in the cohere command body?
  (3) Does the cohere successfully discharging the c10-c12 SHIPPED-WITH-CAVEATS accumulation
      change PROP-0037's framing?

context: |
  Iteration 1 FAIL-COHERE: load-bearing Q6 apparatus-register cumulative load localized by
  cape-fic audience to 7 near-identical italic prologues (skim-formula). Iteration 2 ran after
  a targeted prologue-variation pass on all 7 chapter openings. Q6 moved from FAIL to CAUTION
  (body-register tipping in c10-c12 remains, but formula-problem is solved). Total cost: ~10
  dispatches vs. ~40 dispatches for option A (full per-chapter bones-revise). Cohere converged.

decision: |
  Candidate 1: OK — no proposal. First occurrence, non-catastrophic, cohere architecture is the
    correct catch for this class.
  Candidate 2: OK — no proposal. First occurrence. Would layer on untriaged PROP-0031.
  Candidate 3: OK — PROP-0037 unchanged. Cohere discharge is confirmatory, not a framing problem.

basis: |
  Candidate 1: process-critic-recurrence-discipline (first occurrence of cross-chapter prologue
    skim-formula; non-catastrophic; cohere caught and fixed it at low cost) + gate-discrimination
    (the fix requires per-chapter exposition authors to load N prior chapters' exposition facets
    at dispatch time — a new cross-chapter context dependency with non-trivial cost; the cohere
    loop is already the designated architecture for cross-chapter presentation accumulation) +
    methodology:3d (optionality — prevention would foreclose the current clean architecture where
    per-chapter authoring is context-isolated; that isolation is structurally load-bearing for
    parallelism across facet authors).
  Candidate 2: process-critic-recurrence-discipline (recurrence_count = 1 for prologue-localization
    triage path) + PROP-0031-not-triaged (layering a triage heuristic on an untriaged base
    proposal increases blast radius before the principal has accepted the base).
  Candidate 3: methodology:3c (blast radius of zero — PROP-0037 is not a framing problem;
    the cohere discharging the c10-c12 accumulation is the intended behavior of the proposed
    mechanism, confirmation not counterevidence; no proposal amendment warranted).

rationale: |
  CANDIDATE 1 (upstream prologue-variation gate): The per-chapter exposition author produces
  `episode-open` entries that became 7 near-identical restatements of standing conditions.
  Each entry was correct in isolation — the skim-formula emerged only across the full sequence.
  A cross-chapter diversity check at authoring time would require loading prior chapters'
  exposition facets into the dispatch context window, creating a new N-prior-chapters dependency
  not present anywhere in the current per-chapter authoring chain. This is a meaningful
  architecture change (all per-chapter agents currently operate blind to sibling chapters by
  design — this enables parallelism and limits context-window cost). The cohere loop exists
  precisely to catch cross-chapter presentation problems post-section. That it caught and fixed
  this at iteration 2 for ~10 dispatches is the mechanism working as designed. First-occurrence
  hold applies per Rule 11: non-catastrophic (cohere resolved it), single-occurrence, cleanly
  caught by designated architecture. If a future project sees the same skim-formula accumulate
  across its section and the cohere loop is not run before it becomes a book-close problem, that
  second occurrence warrants a cross-chapter awareness rule at authoring time. Not now.

  CANDIDATE 2 (cohere-triage heuristic): DEC-0081's option B judgment — "FAIL localizes to
  prologues (presentation layer), therefore targeted presentation-pass is preferred over
  per-chapter bones-revise" — was an operator triage call made correctly on the evidence at hand.
  The cohere Phase 3 triage queue already provides the structural surface where this judgment
  lives (read the chapter-revise queue, coalesce by chapter + axis, order by dependency). Making
  it a named heuristic in the command body would commit future runs to "presentation-localized
  FAIL → presentation-pass always" before the operator has seen what the specific failing axes
  contain. On this project the localization was clear (italic-prologue skim-formula); on a
  different project or a different Q6 failure shape, the localization might look similar but
  require bone-layer changes. One data point is insufficient. Additionally: PROP-0031 (the
  /and-cohere command body proposal) is still status: open / untriaged. Adding a triage heuristic
  to an untriaged base proposal increases the scope the principal must evaluate at triage. The
  correct sequence is triage PROP-0031 first, then consider triage-heuristic additions. Hold.

  CANDIDATE 3 (PROP-0037 interaction): PROP-0037 proposes a Phase 0 HARD-abort at /and-substance
  chapter when consecutive_shipped_with_caveats >= 3 without cohere_acknowledgment. Under
  PROP-0037's proposed mechanism, the /and-cohere persist phase (Phase 7) stamps
  cohere_acknowledgment in showrunner memory after a successful convergence — this clears the
  HARD-abort gate. The cohere converging at CAUTION-COHERE (0 load-bearing fails) is exactly
  the successful resolution that the mechanism is designed to enable: the cohere ran, resolved
  the load-bearing Q6 FAIL, converged, stamps acknowledgment, gate clears, c13 can proceed.
  This is not a framing problem; it is confirmatory evidence that PROP-0037's proposed mechanism
  has the right shape. PROP-0037 remains correctly framed: the problem was the recommendation
  being bypassable (bypassed twice, c10→c11→c12); the proposed fix is a HARD-abort that requires
  cohere acknowledgment. That the cohere then worked efficiently (10 dispatches, 2 iterations)
  confirms the mechanism's expected cost is acceptable. No amendment.

trade-off: |
  Not proposing Candidate 1 means the per-chapter exposition author will continue to author
  prologues blind to the accumulating sequence. Mitigation: /and-review cohere is the correct
  architectural catch, and the cost of catching it there (~10 dispatches per section) is low.
  If the principal runs /and-cohere per-section (as now established), the skim-formula will
  always be caught within one iteration. The prevention cost (cross-chapter context loading at
  each /and-facets exposition dispatch, plus architectural dependency) exceeds the expected
  repair cost at the cohere layer.

  Not proposing Candidate 2 means the triage judgment remains operator-level. Mitigation:
  DEC-0081 is a well-documented operator decision that future dispatches can reference. If
  the same localization pattern recurs on a second cohere run, that is the correct second data
  point for a heuristic proposal.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0083 | 2026-06-03 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c13-bone-gate.md
  source_verdict: |
    /and-write b01c13 Phase 6 bone-gate FAIL(1-HARD) -> remediated to PASS.
    Contextual patterns: (1) s03 interior-naming scene re-decomposition; (2) s04
    all-held foreclosure speech bones flagged FAULT-BONE-DELTA-MALFORMED — adjudicated
    PASS by orchestrator as held-discipline speech is licit.
  gate_path: .claude/commands/and-write.md#phase-6

question: |
  Two patterns from /and-write b01c13: (1) interior-naming scene (s03) required
  Phase 2 re-decomposition because the chunk's central event is an abstract cognitive
  act — should /and-substance chapter Phase 3 flag interior-central-event scenes for
  concrete-correlate-first decomposition at /and-write Phase 1? (2) all-held
  foreclosure speech bones fired false-positive FAULT-BONE-DELTA-MALFORMED because
  bones.schema.md has no held-discipline speech license — should the schema be amended?

decision: |
  Pattern 1 (interior-naming scene flagging upstream): OK. First occurrence,
    non-catastrophic. Wait for recurrence.
  Pattern 2 (held-discipline speech bone schema amendment): PROCESS-CHANGE-PROPOSED
    PROP-0038. Second adjudication ruling on same schema section. Deterministic gap;
    precision-writable; S-cost; no existing open proposal covers it.

basis: |
  Pattern 1: process-critic-recurrence-discipline (count=1; non-catastrophic; one
    recast cycle resolved in-pass; PROP-0024 covers argument-spine but its predicate
    does not fire on solo interior-naming scenes -- a real gap but first-occurrence-holds).
  Pattern 2: step 2 proposals check found no open proposal covering bones.schema.md
    held-discipline speech (pl-2026-05-30-003 covers axis-slug generalization only,
    not the axis_moves:[] held-discipline form). Step 3: gate exists and fires but
    produces false positive on licit bone class — change_type: modify (add license).
    Step 4: recurrence = 2 (pl-2026-05-30-003 b01c06 + b01c13 adjudications on same
    schema section); override first-occurrence-hold on deterministic-gap grounds.

rationale: |
  Pattern 1. s03 re-decomposition resolved correctly in one Phase 2 recast cycle.
  The mechanism is documented in the b01c13 gate report (orchestrator adjudication).
  A future proposal targeting /and-substance chapter Phase 3 with an interior-central-
  event predicate would be the correct shape — but at count=1, the cost of a second
  occurrence (another ~14-bone recast) is acceptable exchange for not adding a Phase 3
  detection predicate on first evidence. PROP-0024 provides the structural template
  (Phase 1 brief constraint on PASS-CHUNK-VOICE-RISK chapters) for any future proposal.

  Pattern 2. bones.schema.md §Dialogue-anchor bones rule 1 now requires two adjudication
  rulings in 7 chapters. Both rulings correctly resolved to PASS; the schema is simply
  incomplete. The Phase 2 auditor cannot distinguish licit held-discipline speech from
  malformed speech without an explicit schema license. The fix is narrow: add sub-rule
  1(b) for held-discipline form with a three-part predicate (scene axes_in_motion: [],
  axes_held[] declares a communication-class axis, rationale names the discipline). The
  additional pl-2026-05-30-003 axis-slug generalization text can be co-applied at the
  same schema-edit pass; both are S-cost; principal may bundle them.

trade-off: |
  Pattern 1: next interior-naming scene will hit Phase 2 before Phase 1 can prime for it.
  Acceptable — re-decomposition pattern is on disk; orchestrator can apply it manually;
  recast cost is low.
  Pattern 2: not proposing would risk a third false-positive FAULT-BONE-DELTA-MALFORMED
  on the next all-held dialogue scene, requiring a third adjudication ruling. Schema-edit
  cost (S) is lower than repeated orchestrator adjudication overhead.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0084 | 2026-06-04 | SLOW (process-critic + user-proxy)

mode: process-critic (primary) + user-proxy (lenient-tie ratification)
trigger:
  reason: failure (11 HARD at /and-write Phase 6 bone-gate, all remediated in-cycle)
  source_report: active-project/staff/auditor/write-b01c14-bone-gate.md
  source_verdict: |
    11 HARD remediated (5 SVO form recasts + signal-002 modifier sweep + 3 held-axis
    fixes + mover-reduction reconcile) + 4 SIGNAL dispositioned. Bone-gate PASS after
    remediation. S04 convergence-climax co-dominant tie (4 axes × +1.0) accepted via
    lenient interpretation; queued for admin user-proxy ratification.
gate_path: .claude/commands/and-write.md#phase-6

question: |
  (A) Process-critic: c14 exhibited the floor-vs-fractional-target structural tension for
  the second time (first: c03/c04, cf. PROP-0010). Root cause: every fractional scene-target
  (0.25/0.5) was enacted by a 1.0-floor moving bone, causing chapter bone-sum overshoot AND
  axis-ties at 1.0 within S03/S04. Three candidate process changes offered: (a) /and-substance
  guidance that scene-targets should be >=1.0 for multi-arc convergence chapters; (b) /and-write
  Phase 1 rule that a fractional scene-target uses a SINGLE chapter-level mover (not per-scene);
  (c) an auditor-rule clarifying that STAKES-AXIS-NOT-DOMINANT uses delivered-bone-magnitude
  (ties = co-dominant). Does the process need to change?

  (B) User-proxy: The S04 convergence-climax has 4 axes at +1.0 each. S02/S03 were reconciled
  to strict single-mover dominance. S04 relies on the lenient reading: gate fires only if a
  non-stakes axis delivers *strictly more* than the stakes axis; ties are co-dominant. Does the
  principal accept this disposition for c14 ship?

context: |
  Bone-gate report: active-project/staff/auditor/write-b01c14-bone-gate.md
  11 HARD, all resolved in-cycle. Audience 3/3 SUBSTANCE-FELT all 4 scenes.
  Dramatist ACCEPT (shape; 2 non-blocking renderer flags).
  S04 is a 4-arc simultaneous completion scene: cl-antag-d10 + cl-d07a + cl04 +
  relational arc all close here. Strict single-dominance structurally impossible
  when N arcs complete at the 1.0 floor.
  Measured-delta tracks the contract exactly:
    relational_anchor_status +1.0, social_tether-antag +1.5, position-prot-rise +1.0,
    moral_legibility_to_self +0.5.
  Relevant open proposals: PROP-0010 (magnitude-floor pre-flight at /and-substance chapter;
    recurrence_count: 3, third chapter exhibiting fractional-target-floor collision).
  PROP-0010 proposed diff already includes "consolidate scenes so the full target is
  delivered in fewer scenes each with >=floor per-axis target" -- covers candidates (a) + (b)
  from the dispatch but does not specifically flag multi-arc convergence chapters as
  requiring this consolidation path.
  No existing open proposal addresses the STAKES-AXIS-NOT-DOMINANT co-dominant-tie
  clause for simultaneous N-arc completion scenes.

options: |
  Process-critic:
    (i) OK-MERGED-INTO PROP-0010 for the floor-vs-fractional-target recurrence
    (ii) PROCESS-CHANGE-PROPOSED PROP-0039 for the lenient-tie co-dominant clause
    (iii) Some combination or OK-only verdict
  User-proxy:
    (I) Accept the c14 lenient-tie disposition -- ship as-is
    (II) ESCALATE to human -- require strict single-dominance (would force S04 revise)

decision: |
  Process-critic:
    (i) OK-MERGED-INTO PROP-0010 (recurrence_count 3->4; multi-arc convergence
        consolidation guidance added to recurrence_refs).
    (ii) PROCESS-CHANGE-PROPOSED PROP-0039 (new; lenient-tie co-dominant clause for
        simultaneous N-arc completion at the 1.0 floor; change_type: modify on
        Phase 6 STAKES-AXIS-NOT-DOMINANT criterion).
  User-proxy:
    (I) ACCEPT the lenient-tie disposition for c14 ship.

basis: |
  Process-critic step 2 (proposals-log check):
    Floor-vs-fractional: PROP-0010 is open and matches target + change_type. Merge mandatory.
    Lenient-tie: no open proposal covers STAKES-AXIS-NOT-DOMINANT tie-clause. No rejected
    proposal matches. PROP-0039 is net-new.
  Process-critic step 3 (content vs. process):
    Floor-vs-fractional: the multi-arc consolidation note is a precision gap in PROP-0010's
    proposed_diff (covers the mechanism but does not call out convergence chapters by name);
    c14 is the recurrence that confirms the guidance needs to be more explicit on this path.
    Lenient-tie: the Phase 6 gate spec reads "MUST be the largest delivered delta in the scene"
    with no carve-out for N-axis simultaneous completion at the bone floor. The current spec
    would HARD on any future convergence-climax tie. The auditor resolved correctly via
    context-sensitive judgment; but without a spec change, that judgment is non-reproducible
    and the gate remains structurally inconsistent with the project's multi-arc closure design.
    change_type: modify (add co-dominant-tie clause).
  Process-critic step 4 (recurrence):
    Floor-vs-fractional: count=4 (c04 DEC-0031, c06 DEC-0046/0057, c06-revise DEC-0057,
    c14 this dispatch). Merge is mandatory.
    Lenient-tie: count=1. Non-catastrophic (resolved in-cycle; 3/3 audience PASS). But:
    first-occurrence-hold override applies -- the failure is deterministic. Every future
    convergence-climax scene completes N cost-arcs simultaneously at the 1.0 floor; strict
    single-dominance is structurally impossible by design in those scenes. Without a spec
    amendment, the gate will hard-fire on every convergence climax. Deterministic gap
    + precise fix = propose at count=1 per methodology recurrence-override.
  User-proxy (lenient-tie):
    goal:1 (pipeline correctness) -- the gate's purpose is to prevent a non-stakes axis
    delivering MORE than the stakes axis. That purpose is satisfied in S04: relational
    (stakes) is not under-delivered; no axis outscores it; they co-complete. Firing HARD
    on a tie at the 1.0 floor when all four completing axes are structurally constrained
    to 1.0 violates the gate's intent.
    goal:2 (cost discipline) -- audience 3/3 SUBSTANCE-FELT; forcing revise burns caps on
    a chapter that delivered by every measurement including the informed critic standard.
    methodology:3a (reversibility) -- accepting the lenient tie is reversible (PROP-0039
    proposes the gate amendment; can be revisited if the clause proves too permissive).
    No escalation triggers: not architectural direction, not irreversible at meaningful cost,
    not human-only territory. Within admin authority.

rationale: |
  PROP-0010 MERGE: The c14 floor-vs-fractional pattern is structurally identical to
  prior recurrences: sub-1.0 scene-targets authored at /and-substance chapter, 1.0-floor
  bones at /and-write, chapter-sum overshoot of contract. PROP-0010's proposed pre-flight
  check at /and-substance chapter Phase 4/5 (surface SUBSTANCE-CONTRACT-FLOOR-CONFLICT
  when any scene's per-axis target < bone.delta_per_axis.floor) would have surfaced this
  before decomposition. The multi-arc convergence case is the most consequential sub-case:
  when a chapter is designed to close 3+ cost-arcs simultaneously, the scene-target author
  must consolidate delivery into one scene with >=1.0 per axis rather than splitting
  0.25/0.5 residuals across multiple scenes (since each scene enacts a 1.0-floor mover).
  This precision note belongs in PROP-0010's recurrence_refs; it is not a separate proposal.

  PROP-0039 (new): The Phase 6 gate spec says the stakes axis "MUST be the largest" with
  no exception. The S04 co-dominant tie is not a gate miss -- the auditor correctly applied
  context-sensitive reasoning. But the spec as written cannot support that reasoning
  reproducibly: a future auditor following the gate spec literally would HARD on a tie
  even in a structurally identical convergence scene. The fix is a single clause: when >=2
  axes complete simultaneously at the 1.0 floor in a single scene, co-dominant ties are
  accepted -- the gate fires HARD only when a non-stakes axis delivers strictly greater
  magnitude than the stakes axis. Small, precise, closes the spec gap without relaxing the
  gate's actual enforcement intent (stakes-axis under-delivery).

  LENIENT-TIE ACCEPTANCE: S02 and S03 were correctly reconciled to strict single-mover
  dominance -- there the mover-to-held conversions were achievable without violating the
  delivery contract. S04 is structurally different: all four arcs are at 1.0 by design.
  No single axis can be made sole mover without under-delivering the contracted +1.0 on
  the others -- which would itself produce AXIS-DELTA-MISMATCH or AXIS-UNDERDELIVERED.
  The gate cannot simultaneously require (a) each axis delivers its contracted +1.0 AND
  (b) only one axis delivers in S04. That is a contradiction built into the multi-arc
  convergence structure. Accepting the co-dominant tie is the only internally-consistent
  outcome.

trade-off: |
  Merging into PROP-0010 rather than a separate "multi-arc guidance" proposal: the
  proposed_diff on PROP-0010 already contains the consolidation language; adding a
  recurrence_ref is minimum-blast-radius. A separate proposal would duplicate the
  core mechanism.

  Proposing PROP-0039 at count=1: accepted on deterministic-gap grounds. The alternative
  means the next convergence-climax chapter hits the same structural HARD, requires the
  same orchestrator adjudication, and the spec remains inconsistent with the project's
  multi-arc closure design. Fix is S-cost; delay has no benefit.

  Accepting lenient-tie for c14: if the co-dominant tie clause proves too permissive
  in a future chapter, PROP-0039's amendment can be narrowed at that point. The
  acceptance is reversible at the process level; c14's ship is supported by 3/3
  SUBSTANCE-FELT + measured-delta-on-contract evidence.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0085 | 2026-06-04 | FAST (user-proxy, RUNBOOK R1)

mode: user-proxy
trigger: /and-stitch b01c14 Phase 9 terminal-gate disposition (Class-B FAIL; CONTINUE=no; central event recovered; cause: abstract ledger-register + cold-context name-unfamiliarity)

question: |
  Phase 9 cold-read returned CONTINUE=no on b01c14. Class-B: central event recovered
  (Taylor confirms courier → detained → refuses to price Wren). FAIL cause: (1) relentlessly
  abstract ledger-metaphor, no concrete courier-as-person, no Sera-as-stake; (2) Otto/Sera/
  Jarvis/faction name-unfamiliarity (c14-read-in-isolation artifact).
  Phase 8.5 returned PASS (central events land concrete at spine; weave + followability clean;
  @42 Gold-Morning fence-clean). Bone-gate audience 3/3 SUBSTANCE-FELT. /and-facets 9/9 ACCEPT.
  Chapter GOAL explicitly licenses accounting register as designed nature.
  PASS-CHUNK-VOICE-RISK was armed from /and-substance chapter (Signal-B: ledger-abstraction
  risk). Options: (A) SHIPPED-WITH-CAVEATS + mandatory depth pass before book-close,
  (B) structural re-write now, (C) ESCALATE.

context: |
  DEC-0072 (b01c11 chunk cold-read + Phase 9), DEC-0074 (c11 Phase 9), DEC-0078 (c12 Phase 9)
  are exact coupling-rule precedents. All three: Class-B FAIL, CONTINUE=no, central event
  recovered, causes = design-inherent abstract register + cold-context name-opacity. All three
  shipped SHIPPED-WITH-CAVEATS. The accounting register is the moral_legibility series signature
  ("the accounting is explicit" is c14's stated GOAL). Cold-context name-unfamiliarity (Otto/
  Sera/Jarvis) is serial mid-point noise — an invested reader has c01-c13 context.
  Phase 8.5 substance-aware check confirmed followability clean and concreteness at spine.
  The c14 case has one additional carried item not present in c10-c12: courier-as-person +
  Sera-as-stake concreteness gaps are addressable via depth pass (not structural-unfixable),
  making the depth-pass mandatory flag load-bearing.

options:
  - (A) SHIPPED-WITH-CAVEATS + mandatory depth pass (/and-write b01c14 revise --from-signals) before book-close
  - (B) Structural re-write now (~40 dispatches, re-cascade /and-facets + /and-stitch)
  - (C) ESCALATE to human (queued to end-of-run summary)

decision: (A) SHIPPED-WITH-CAVEATS. Depth pass flagged mandatory before book-close.

basis: |
  ltm:DEC-0072 + ltm:DEC-0074 + ltm:DEC-0078 — coupling rule exact match: Class-B FAIL,
  CONTINUE=no, central event recovered, causes = design-inherent abstract register +
  cold-context name-opacity. All three prior cases shipped SHIPPED-WITH-CAVEATS.
  methodology:3e (convention) — the established project disposition for this failure class
  is terminal-ship + recorded-risk + depth-pass flag; consistency requires same verdict.
  methodology:3b (cost) — (B) burns ~40 dispatches to re-derive a chapter whose bones,
  facets, and Phase 8.5 all PASS; wrong repair layer (bone-layer re-decompose cannot address
  cold-context name-opacity, which is non-fixable).

rationale: |
  The coupling rule established across DEC-0072/0074/0078 is deterministic on the c14 facts:
  (1) central event recovered — the step-2 diff gate did NOT fire; (2) all CONTINUE=no causes
  fall into pre-authorized categories (design-inherent abstract register per chapter GOAL;
  cold-context name-opacity as serial mid-point noise). Phase 8.5 (substance-aware, context-
  held) returned PASS, which is the informed standard the cold-read cannot replicate.
  The accounting register is not a defect introduced at stitch — it is the chapter's declared
  moral_legibility axis ("accounting is explicit" is the GOAL text). Re-writing now would
  violate the substance contract that 3/3 audience + 9/9 facets all endorsed.
  The c14 depth-pass (courier-as-person concrete detail; Sera-stake staged) is addressable at
  /and-write revise --from-signals and should be flagged mandatory-before-book-close, consistent
  with PASS-WITH-DEPTH-PASS-REQUIRED semantics. Option (B) is wrong repair layer + wrong cost.
  Option (C) is unnecessary — prior rulings decide this without human judgment.

trade-off: |
  Accepting (A) means the courier-as-person and Sera-stake gaps ship in the terminal draft
  pending depth pass. Risk: if the depth pass is skipped before book-close, those texture
  gaps persist. Mitigated by: (a) mandatory depth-pass flag in this entry + run summary;
  (b) the gaps are texture-level (bone-delivered substance is clean), not event-delivery
  failures; (c) /and-postop can surface them in the gap between ship and book-close.

depth_pass_mandatory: yes — /and-write b01c14 revise --from-signals before book-close.
  Targets: courier-as-person concreteness (@courier-anchored bones); Sera-stake staged
  (visible in at least one concrete body-act or consequence bone); cold-read-flagged
  abstraction-dominant passages that survived Phase 8.5 as texture-level (not spine) gaps.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0086 | 2026-06-04 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01c14-2026-06-04.md
  source_verdict: SHIPPED-WITH-CAVEATS (Phase 9 Class-B cold-read FAIL CONTINUE=no; fourth application of coupling rule across c10/c11/c12/c14 — DEC-0072/0074/0078/0085)
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]
verdict: PROCESS-CHANGE-PROPOSED PROP-0040

question: |
  At the fourth identical coupling-rule application (c10/c11/c12/c14 all shipped
  SHIPPED-WITH-CAVEATS via admin user-proxy on the same Class-B pattern), should the
  process mechanize any part of that ruling? Three specific candidate questions:
  (a) auto-ship for known-voice-risk chapter class when complaint categories are all
  covered by carried risk; (b) depth-pass debt accumulation concern (4 chapters?);
  (c) interior-accounting chapter class upstream grounding-ledger default.

decision: PROCESS-CHANGE-PROPOSED PROP-0040 (candidate a). Candidate b: OK (no new signal
— depth-pass debt is c10 + c14 only; c11/c12 have no pending depth passes). Candidate c: OK
(first occurrence; hold for recurrence per standard rule).

basis: |
  Step 1 (evidence): The report shows identical Class-B pattern at c14: central event
  recovered, CONTINUE=no, causes = design-inherent accounting-abstraction + cold-context
  name-opacity, Phase 8.5 PASS. The c14 case adds one new dimension absent from c10-c12:
  tractable texture gaps (courier-as-person, Sera-stake) that DEC-0085 flagged for a
  mandatory depth pass. This produces a Case 1 / Case 2 distinction not encoded in the spec.

  Step 2 (proposals log): No existing open proposal covers Phase 9 Case 1 auto-ship. PROP-0018
  added the Class A/B discrimination and the "admin default: (P)" rule. DEC-0085's Case 2
  is consistent with PROP-0018's admin-dispatch path. The Case 1 path (all complaints covered,
  no tractable items, no admin dispatch needed) is new and not in any existing proposal. No
  rejected or deferred proposal matches this target.

  Step 3 (content vs. process): Could a stricter existing gate have caught this? No. The
  coupling rule works correctly at every application. The gap is efficiency, not correctness:
  the Phase 9 harness routes to admin user-proxy even when the answer is fully deterministic.
  Case 1 is a process-efficiency gap, not a process-correctness gap. change_type: modify on
  Phase 9 Step 2 (add the complaint-coverage check + auto-ship path).

  Step 4 (recurrence): count=4 across c10/c11/c12/c14. Rule says "prefer to return OK and
  wait for recurrence" at count=1. At count=4 with two sub-cases discriminated, the
  mechanism is stable enough to codify. Automating a deterministic ruling is not premature
  promotion of a one-off signal.

  Step 5 (methodology): S-cost (add a complaint-coverage check and a conditional branch to
  Phase 9 Step 2 + Step 4 verdict block; no new dispatches, no schema changes). Blast radius:
  low — only affects Class-B FAIL chapters with PASS-CHUNK-VOICE-RISK carry, which is a
  structurally narrow class. Reversibility: adding a Case 2 fallback preserves full admin
  involvement whenever the classification is ambiguous or a tractable item appears.

  Candidate b (depth-pass debt): The trigger's "4 chapters" framing is inaccurate. Checking
  memory.md directly: c10 depth_pass_pending: true (PASS-WITH-DEPTH-PASS-REQUIRED, bone-level
  staging targets — @2/@11/@21); c11 SHIPPED-WITH-CAVEATS, readability READABLE, no mandatory
  depth pass; c12 SHIPPED-WITH-CAVEATS, DEC-0078 explicitly resolved apparatus-density to
  /and-cohere not per-chapter depth pass; c14 depth_pass_pending: true (DEC-0085, texture-
  level targets). Actual debt = c10 + c14. The SHIPPED-WITH-CAVEATS / PASS-WITH-DEPTH-PASS-
  REQUIRED distinction is working correctly. No new process change warranted.

  Candidate c (interior-accounting upstream grounding): c14's courier-as-person + Sera-stake
  gaps are first-occurrence at this specific class. Not catastrophic. Standard first-occurrence
  hold. No proposal.

rationale: |
  PROP-0040 targets the only confirmed process gap: Phase 9 routinely fires an admin user-proxy
  dispatch on a deterministic Class 1 ruling (all complaints covered, answer already in DEC
  history), adding per-chapter overhead without changing the outcome. The Case 1 / Case 2
  discrimination surfaces for the first time at c14 (where DEC-0085 identified tractable items).
  The Case 2 path (admin dispatch with depth-pass brief) is exactly where admin value was
  delivered at c14. Encoding Case 1 as auto-ship preserves that value while eliminating the
  overhead on chapters where the coupling rule is fully deterministic.

trade-off: |
  Risk: the auto-ship path could miss a tractable item if the harness over-classifies a
  complaint as COVERED. Mitigated by: (a) conservative matching rule (UNCOVERED wins when in
  doubt); (b) the existing Phase 9.5 process-critic dispatch fires regardless and can flag
  if a Chapter 1 auto-ship was mis-classified; (c) the Case 2 fallback is always available
  for any ambiguous classification.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0088 | 2026-06-04 | process-critic (signal-accepted)

mode: process-critic
trigger:
  reason: signal-accepted
  source_report: active-project/staff/auditor/write-b01c15-bone-gate.md
  source_verdict: |
    /and-write b01c15 Phase 6 bone-gate PASS (0 HARD). signal-002 ACCEPTED:
    REGISTER-AS-MANNERISM — [fly-population + verb + location] template in 5 bones,
    flagged to /and-stitch Phase 4 for structural variation; no bone revision.
  gate_path: .claude/commands/and-write.md#phase-6
verdict: OK

question: |
  Does the b01c15 accepted REGISTER-AS-MANNERISM signal (insect-feed POV chapter
  producing [fly-population + verb + location] template repetition at 5 bones, dispositioned
  accept-and-flag-to-stitcher) indicate a process gap? Specifically: should the screen-writer
  Phase 1 brief pre-empt feed-template repetition in insect-POV chapters?

decision: OK — no proposal. The accept-and-flag-to-stitcher disposition is correct
and the gate is functioning as intended. The pattern is first-occurrence at this exact
shape; prior insect-feed REGISTER-AS-MANNERISM instances (c04, c05, c09) were structurally
distinct and all accepted-with-rationale. A screen-writer Phase 1 brief constraint is
both unnecessary (the gate already catches + routes) and counterproductive (the SVO
discipline fence is what forces template convergence in the first place).

basis: |
  Step 1 (evidence): signal-002 fires on 5 bones across s02/s03/s04 where the grammatical
  shape [fly-population + verb + location] repeats with varying verbs but identical
  subject-class and object-class. The auditor dispositioned ACCEPTED with flag to
  /and-stitch Phase 4. No bone revision. The gate performed its detection function correctly;
  the disposition is the right one (structural variation belongs at the prose render layer,
  not the SVO bones layer where the schema requires concrete subject-verb-object form).

  Step 2 (proposals log): No prior proposal targets REGISTER-AS-MANNERISM feed-template
  repetition, feed-POV screen-writer briefs, or insect-POV SVO constraint. The existing
  proposal at line 1046 (PROP-0039 context only) references register-as-mannerism as an
  "existing analog this change extends" — that reference is incidental (PROP-0039 targets
  a different gate: Phase 6 per-axis-Δ floor vs. fractional). No rejected or deferred
  proposal materially covers this shape.

  Step 3 (content vs. process): Is this a process failure? The gate detected the pattern,
  the auditor applied correct disposition (accept + forward to stitcher), the stitcher Phase 4
  voice-embodiment discipline is exactly the right resolution point. Nothing fell through.
  The question is whether the pipeline should move the catch earlier (screen-writer brief).
  Answer: no, because the cause is architectural, not authorable-away at the chunk layer.

  WHY A SCREEN-WRITER BRIEF WOULD NOT HELP: The [fly-population + verb + location] template
  arises from two mandatory constraints operating together: (a) the bones SVO discipline fence
  requires a concrete syntactically complete subject-verb-object triple with no directional PP,
  no intransitive motion, no abstract predicate; (b) in a fly/insect POV chapter the feed
  subject is always some variant of fly-population, and the action is necessarily positional
  (they occupy, cluster, cover, settle on a location). The intersection of these two constraints
  is a structurally narrow morphological corridor. Telling the screen-writer "vary the SVO
  template" at chunk level either (1) produces chunk descriptions that violate the SVO fence
  when the bones author tries to honor them, or (2) produces abstract-or-intransitive bones
  that trip ABSTRACTION-DOMINANT or CENTRAL-EVENT-CONCRETENESS. The stitcher Phase 4 render
  layer is the structurally correct point to introduce surface-level variation (synonym
  substitution, inverted syntax, compressed compound) without violating the SVO contract.

  Step 4 (recurrence): The insect-feed REGISTER-AS-MANNERISM pattern appeared in:
  - c02: "takes the drain angle" x3 — accepted (architectural boundary-transition marker)
  - c04: "[insect-feed]-returns-[entity]" x4 — accepted (canonical feed-output verb by design)
  - c04: "exits-[location]" x4, "enters-[location]" x5 — accepted (only compliant transitive
    departure/arrival form under SVO discipline)
  - c09: "marks" x3 (verb-frequency, not strict VERB+OBJECT pair) — signal advisory, accepted
  - c10: "corwick-squares" x3 diff-objects — light-REMEDIATED + carry
  - c12: "closes the X" x5, "reaches the X" x3 — accepted as intentional accounting-refrain
  - c15: [fly-population + verb + location] x5 — current, accepted

  This is occurrence N=7 of REGISTER-AS-MANNERISM firing and being accepted. However,
  the previous occurrences do not aggregate into a single recurrence class — they are
  architecturally distinct causes (feed-output verb, transitive-departure form, accounting
  refrain, feed-position template). The c15 instance is first-occurrence for the specific
  shape [feed-population + verb + location] as a subject-class + object-class template
  (as distinct from exact VERB+OBJECT pair). Standard first-occurrence hold applies.

  The process-critic "wait for recurrence" rule specifically requires the same failure class
  to recur, not just the same gate firing. Multiple architecturally distinct
  accept-with-rationale dispositions at the same gate is the gate functioning correctly —
  each accepted instance is the gate doing its job. That is not a failure-class accumulation.

  Step 5 (methodology): A screen-writer brief add would be M-cost (new constraint text in
  /and-substance + the screen-writer agent card) and medium-blast-radius (fires on every
  insect-POV chapter). The current accept-and-forward path is zero-cost in the absence of
  actual stitcher failure. Per methodology, prefer reversible + lower-cost path when outcomes
  are comparable. The stitcher Phase 4 flag is already positioned to handle this — if it
  fails to resolve the variation at render, THAT would be the triggering evidence for a
  process change. No failure has occurred at the stitch layer on any prior REGISTER-AS-
  MANNERISM accepted carry.

  CONCLUSION: The accept-and-flag-to-stitcher disposition is architecturally correct. The
  stitcher Phase 4 voice-embodiment + structural-variation directive is the right resolution
  surface. This is the gate functioning as designed. No proposal warranted.

rationale: |
  The gate caught the pattern (correct detection), auditor applied correct disposition
  (accept + carry to stitcher, not bones-revise), stitcher Phase 4 is exactly calibrated
  to produce surface-level variation without violating SVO bones. A screen-writer Phase 1
  brief constraint would be upstream of the only feasible resolution point and would create
  a schema-constraint tension (vary the template vs. honor the SVO fence). First occurrence
  at this specific shape. No prior proposal covers this target. Standard first-occurrence
  hold: return OK.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0089 | 2026-06-04 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01-c15-2026-06-04.md
  source_verdict: |
    SHIPPED-WITH-CAVEATS — /and-stitch b01c15 Phase 9 cold-read FAIL (CONTINUE=no;
    events recovered + summary maps to goal; categories = event-poverty/jeopardy-offstage/
    nothing-changes, ALL pre-authorized in chunk_cold_read.cold_read_risk_carry per DEC-0087).
    Auto-shipped terminal per Phase-9 Step-4 SHIPPED-WITH-RISK-RECORDED coupling. Phase 8.5
    confirmed central-event-muffle NOT-MATERIALIZED. Mandatory depth-pass logged
    (pl-2026-06-04-c15-004). Readability axis READABLE (CONTINUE=no is event-poverty/
    uninformedness, not airlessness).
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-substance.md#phase-5.5]
verdict: OK

question: |
  Second consecutive SHIPPED-WITH-CAVEATS (c14 DEC-0085 + c15 now — both deliberately-quiet
  falling/accounting chapters). Is the back-to-back-quiet accumulation a process signal worth
  a proposal — specifically: (a) should two consecutive SHIPPED-WITH-CAVEATS auto-arm
  /and-cohere, or (b) should the falling-arc run of c13-c15 have been compressed at
  /and-substance book, or (c) is the coupling functioning as designed and the accumulation
  handler already named?

decision: OK — no new proposal.

basis: |
  Step 1 (evidence):
    c15 cold-read data (from showrunner memory — report file not on disk, data embedded in
    memory.md cold_read block): CONTINUE=no. Event-poverty + jeopardy-offstage (by design)
    + nothing-changes. Fail categories ALL in cold_read_risk_carry (per DEC-0087 Phase 5.5
    P-disposition). Phase 8.5 PASS. Readability axis READABLE. Central-event-muffle NOT-
    MATERIALIZED (c14 failure did not recur). 3/3 audience SUBSTANCE-FELT (bone-gate).
    9/9 facets ACCEPT. The SHIPPED-WITH-CAVEATS auto-shipped under the PROP-0040-proposed
    Case 1 path: zero tractable complaints, all complaints covered by carried risk. Mandatory
    depth-pass logged for both c14 and c15.

    Consecutive-quiet count: c14 + c15 = 2. Prior run: c10/c11/c12 (3 consecutive) triggered
    PROP-0037 at N=3. /and-cohere ran after c12 (before c13) and converged at CAUTION-COHERE
    (DEC-0081/0082), stamping cohere_acknowledgment, clearing PROP-0037's proposed gate.
    c13-c15 are the new run of quiet chapters post-cohere. Current consecutive count = 2 (c14 +
    c15); this is below the N=3 threshold PROP-0037 proposes.

  Step 2 (proposals log):
    PROP-0037 (status: open): targets /and-substance chapter Phase 0 HARD-abort at
    consecutive_shipped_with_caveats >= 3 without cohere_acknowledgment. Current count is 2.
    Not triggered yet. No prior proposal covers a two-consecutive auto-cohere-arm rule.
    PROP-0040 (status: open): targets Phase 9 Case 1 auto-ship (all complaints covered →
    no admin dispatch). c15 executed exactly as Case 1 — the mechanism proposed in PROP-0040
    worked correctly here.
    No rejected or deferred proposal matches a "two-consecutive triggers cohere" rule.

  Step 3 (content vs. process):
    Is this a process failure? No. The gate chain executed correctly at every level:
      — /and-substance chapter Phase 5.5: Class-B disposition P per DEC-0087 (7-consecutive
        precedent; dramatist ACCEPT; informed 3/3 SUBSTANCE-FELT; execution watches HARD into
        /and-write).
      — /and-write: bones-gate PASS, audience 3/3 SUBSTANCE-FELT (DEC-0088 context).
      — /and-review bones: FOLLOW-PASS, fidelity PASS.
      — /and-facets: 9/9 ACCEPT (cycle 2 after spurious cycle-1 file-path miss).
      — /and-stitch Phase 8.5: PASS, central-event-muffle NOT-MATERIALIZED.
      — /and-stitch Phase 9: SHIPPED-WITH-CAVEATS via Case 1 auto-ship (PROP-0040 mechanism).
    The coupling functioned as designed. DEC-0087 explicitly named /and-cohere before book-close
    as the accumulation handler for consecutive-quiet fatigue. That is correct.

    Candidate (a) — two-consecutive SHIPPED-WITH-CAVEATS auto-arms /and-cohere:
      PROP-0037's threshold is N=3, derived from three-chapter evidence (c10/c11/c12). That
      threshold was deliberately chosen over N=2 because: (a) two quiet chapters in a falling-arc
      is designed behavior, not accumulation requiring cross-chapter intervention; (b) the
      /and-cohere mechanism has non-trivial cost (~10 dispatches minimum per DEC-0081); (c) the
      falling arc for b01 was known to span c13-c15 when book substance was authored. Dropping
      the threshold from 3 to 2 would fire /and-cohere in the middle of a deliberately-designed
      3-chapter falling arc — the exact chapter class the informed critics (dramatist + audience)
      consistently endorse. Lowering the threshold to 2 is a regression against an established
      ruling, not a process improvement. No new evidence supports overriding PROP-0037's N=3.

    Candidate (b) — falling-arc c13-c15 should have been compressed at /and-substance book:
      The c13-c15 falling arc was structurally authored at /and-substance book with explicit
      dramatic_shape annotations. Three chapters of falling action for a 17-chapter book is
      architecturally standard (17% of book, comparable to the rising-action proportion). The
      book-substance series-audit (DEC series) approved this structure. The cold-reader's
      event-poverty/nothing-changes complaint is the designed cold-reader cost of a falling arc
      with interior-accounting chapters — not evidence of a book-level design failure. No gate
      in the existing chain is positioned to catch this at /and-substance book level; and
      adding one (e.g. a "no more than N consecutive falling chapters" gate) would be a
      taste-gate on architectural story structure, which is human-only territory per methodology.
      First-occurrence hold applies; the falling arc completed at c15 without the c14 central-
      event-muffle failure recurring (Phase 8.5 NOT-MATERIALIZED).

    Candidate (c) — system is working:
      Affirmative. The chunk-cold-read correctly pre-identified the risk at Phase 5.5 (DEC-0087).
      The principal pre-authorized via the Class-B P-disposition. The terminal gate shipped
      without re-litigation (PROP-0040 Case 1 path). Mandatory depth-passes are logged for both
      c14 and c15. The /and-cohere accumulation handler is already named as the before-book-close
      obligation. At N=2 the PROP-0037 gate has not fired. The consecutive-quiet run is 2 chapters
      below a designed 3-chapter threshold. Nothing broke.

  Step 4 (recurrence):
    This is the second consecutive SHIPPED-WITH-CAVEATS on the Class-B quiet-chapter pattern
    (c14 + c15). The first consecutive run was c10/c11/c12 (N=3), which produced PROP-0037
    at N=3. The current N=2 run is below that threshold. Per process-critic rule: "prefer to
    return OK and wait for recurrence" when count < threshold and failure is non-catastrophic.
    Count=2 is explicitly below the previously-established N=3 threshold. Standard hold.

  Step 5 (methodology):
    Reversibility: adding a lower threshold would be harder to undo once baked into the chain.
    Cost: /and-cohere at 2 consecutive chapters would fire mid-falling-arc at non-trivial cost
    (~10 dispatches) on chapters the informed critics ACCEPT by design.
    Blast radius: modifying PROP-0037's threshold affects every future book with falling-arc
    chapters.
    Optionality: DEC-0087 already named /and-cohere before book-close; keeping that as the
    timing preserves optionality to run it when the arc completes rather than mid-arc.
    Convention: PROP-0037 N=3 is the established threshold from three data points. N=2 would
    be counter-conventional without new evidence.

rationale: |
  The c14+c15 back-to-back-quiet is the designed behavior of a falling arc, not a process
  failure. The coupling functioned as designed at every stage. PROP-0037 (N=3 threshold) and
  DEC-0087 (/and-cohere before book-close) are the correct existing mechanisms — both remain
  valid and neither requires amendment at N=2. The mandatory depth-pass debt (c14 + c15) is
  logged and gates /and-substance book b02 Phase 0 + /and-review verdict b01. No new proposal
  warranted; the process signal does not exceed what the existing machinery already handles.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0087 | 2026-06-04 | FAST (user-proxy, RUNBOOK R1)

question: b01c15 Phase 5.5 CHUNK-CLASS-B — disposition R (revise chunk) / P (proceed with risk recorded) / S (substance-contract redo). Back-to-back quiet chapter after c14 SHIPPED-WITH-CAVEATS: does the consecutive-quiet pattern change the call from the standard Class-B default?
context: Cold-reader: event-poverty / no-jeopardy / "nothing delivered, nothing changes." Confusions mostly uninformedness (series context absent). Informed 3-of-3 audience SUBSTANCE-FELT; dramatist ACCEPT; auditor clean. Falling-arc dramatic_shape chapter; S4 plateau-close is architecturally required. c14 was also a Class-B SHIPPED-WITH-CAVEATS (DEC-0085); c15 is the second consecutive quiet chapter. Cold-reader complaints are execution-layer (event-poverty via abstraction), not chunk-design holes.
options:
  - R: revise chunk — inject on-page jeopardy/event beat
  - P: proceed with risk recorded — carry execution watches into /and-write as HARD; arm stitch Phase 8.5 + Phase 9
  - S: substance-contract redo — high cost, reserved for unacceptable P

decision: P — proceed with risk recorded; carry the feed-texture contrast + S4 ledger-act-not-conclusion watches HARD into /and-write bones authoring; arm stitch Phase 8.5 + Phase 9.
basis: DEC-0060/0062/0072/0074/0076/0078/0085 — seven consecutive Class-B chunk dispositions all went P; ruling is settled. The consecutive-quiet fatigue signal is real but the lever is execution concreteness (bones layer), not chunk design. R would inject events that break the falling-arc the dramatist + audience endorsed; the c14 lesson was exactly that de-abstraction at the bones layer resolves event-poverty on quiet chapters. S is wrong-layer + high cost.
rationale: Informed reviewer consensus (3/3 SUBSTANCE-FELT + dramatist ACCEPT + auditor clean) outweighs the cold-reader's structural complaint. The cold-reader's confusions are uninformedness, not design holes. The back-to-back-quiet concern is addressed by making the bones-layer execution watches explicit and HARD entering /and-write — the same carry-forward applied to c14 at DEC-0085. Two consecutive SHIPPED-WITH-CAVEATS chapters do not warrant escalating the risk classification above Class-B; they warrant tighter watch specification at the bone-gate. Cumulative quiet is the designed scope for /and-cohere before book-close.
trade-off: Two consecutive chapters with HARD execution watches entering /and-write. Fatigue accumulation handled at /and-cohere, not by breaking individual falling-arc chapters at the chunk layer.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0090 | 2026-06-04 | FAST (user-proxy, RUNBOOK R1)

question: b01c16 Phase 5.5 CHUNK-CLASS-B — disposition R (revise chunk) / P (proceed with risk recorded) / S (substance-contract redo). If P, specify the risk-carry list.
context: Phase 5 informed reviewers all PASS: 3/3 SUBSTANCE-FELT, dramatist ACCEPT (shape sound for falling chapter, correctly ARMS c17 collapse axes without pre-spending), auditor PASS 0 HARD. Cold-reader strict-CONTINUE=No, but decomposed: (1) series-context holes are uninformedness, not real defects; (2) s03 closing-paragraph over-explains thesis (narrator-voice restatement of already-shown behavior) — flagged by ALL Phase 5 reviewers; (3) cold-reader-only: old-man+stunted-child props in s01 dropped (Chekhov), position-arithmetic rendered as abstract left/right numbers, Halvard "applies no pressure" (disclaims wanting anything). Central event is already a concrete physical act (body turning, walking out of clearing while man is mid-sentence) — better bones-entry shape than c14/c15.
options:
  - R: revise chunk — re-author at chunk layer (Class A default)
  - P: proceed with risk recorded — advance to /and-write with findings as authorized known-risk
  - S: substance-contract redo — high cost, reserved for genuine contract failure

decision: P — proceed with risk recorded. Risk-carry list below.
basis: DEC-0060/0062/0072/0074/0076/0078/0085/0087 — eight consecutive Class-B chunk dispositions all went P; ruling is settled. c16 is in better bones-entry shape than c14/c15 (central event already concrete physical act). Informed reviewer consensus (3/3 SUBSTANCE-FELT + dramatist ACCEPT + auditor 0 HARD) is decisive.
rationale: Same decision shape as the eight prior Class-B dispositions. The cold-reader's confusions are decomposed and explained: series-context uninformedness (not design holes), one prose-register item shared by Phase 5 reviewers (correctly surfaced as a bones/stitch target, not a chunk hole), and cold-reader-only catches that are rendering concerns. R would be wrong-layer (the chunk design is sound per informed critics); S is wrong-layer + high cost. Thematic-demonstration chapter with concrete physical central event is the best Class-B entry in the book.
trade-off: Four risk-carry items enter /and-write (3 HARD) and one enters /and-stitch. Accepted; this is the established mechanism.

risk-carry:
  1. [/and-write — HARD concreteness target] s01: old-man + stunted-child props staged in the opening — they must either fire (earn a callback beat at bones level) or be cut before the bones file ships. Chekhov unfired is a bones-layer error; Phase 6 bone-gate should catch as EVENT-NOT-CONCRETE / FAULT-BONE-DELTA-MALFORMED if these props vanish without a bones-level callback.
  2. [/and-write — HARD concreteness target] Position-arithmetic (the moral counter-argument): must be rendered as a concrete image or spatial metaphor at the central-event bone, not abstract "left/right numbers" or pure cognition-narration. Phase 6 EVENT-NOT-CONCRETE fires if the central-event bone presents this as abstraction-dominant.
  3. [/and-write — HARD concreteness target] Halvard's pressure: the disclaimer-not-wanting framing must coexist with a visible on-page cost for Taylor of staying vs. leaving — Halvard does not need to threaten; the clearing must feel non-neutral to her body. The bones must carry a physical-behavioral signal (posture, spatial proximity, breath, weight) not only interior arithmetic.
  4. [/and-stitch — trim target, Phase 4 + Phase 9] s03 closing paragraph: the narrator-voice thesis restatement ("That is not the same thing. She knows the difference" or equivalent) must be cut or recast as behavior-only in the stitch pass. All Phase 5 reviewers flagged this as over-explanation of already-shown behavior. Phase 9 auditor should treat survival of explicit thesis-narrator-voice in the closing paragraph as a HARD finding.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0091 | 2026-06-04 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: signal-accepted
  source_report: active-project/staff/auditor/write-b01c16-bone-gate.md
  source_verdict: |
    HARD 0; SIGNAL 2 both accepted (signal-001 marks-repetition advisory ≥3 threshold,
    advisory to stitch; signal-002 taylor-has-full-counter occasion-carrier mapping,
    interior-state delivery to narrator-interest facet). Phase 3 MT-2 SOFT accepted
    (no feed-tracking bone during s03 walk — inference carries, n08 delivers
    foreclosure-not-flight).
  gate_path: .claude/commands/and-write.md#phase-6
verdict: OK

question: |
  /and-write b01c16 bone-gate passed clean (0 HARD; 3/3 SUBSTANCE-FELT all scenes).
  Two advisory SIGNALs and one Phase-3 SOFT accepted at emit. Should the process change?
  Specific question: "marks" prop-anchor verb-repetition has now appeared as an advisory
  across c09 / c10 / c11 / c15 / c16 (5 chapters). Does that 5-chapter recurrence
  warrant a process note (Rule 11 promotion: ≥3 occurrences)?

decision: OK — no process change proposed.

basis: |
  Step 1 (proposals log): No prior proposal targets "marks"-verb advisory,
  verb-frequency advisory for instrument/record/environment SVO class, or
  any screen-writer-brief constraint for this verb class. No rejected or deferred
  proposal covers this target. No open proposal with matching target+change_type.

  Step 2 (content vs. process): The gate at Phase 6 is already performing the
  detection function that a new AP-SCAN would encode. REGISTER-AS-MANNERISM fires
  on ≥3 of the same VERB+OBJECT pair; the "marks" occurrences across all five chapters
  have distinct objects in every case except the c16 within-chapter exact repeat (×2,
  below the ≥3 HARD threshold). The existing SIGNAL path catches the advisory at the
  correct severity and routes it to /and-stitch Phase 3/4 — the only structurally
  viable resolution point. No gate gap exists.

  Step 3 (Rule 11 promotion check): Rule 11 says taste flags that recur ≥3 times
  across reviews should graduate to mechanical AP-SCAN checks. The "marks" advisory
  has fired 5 times (c09/c10/c11/c15/c16). However, the Rule 11 promotion path requires
  the same FAILURE CLASS to recur — not just the same gate firing. The prior
  DEC-0088 (c15 insect-feed template) made this discrimination explicitly: "Multiple
  architecturally distinct accept-with-rationale dispositions at the same gate is the
  gate functioning correctly — each accepted instance is the gate doing its job." The
  "marks" advisory is the same architectural root across all five chapters: the SVO
  discipline fence requires concrete transitive verbs for instrument/record/environment
  bones, and "marks" (concrete physical act: leaves a trace on a surface) is one of
  the narrowly compliant verb forms in that semantic class. The recurrence is not a
  process failure — it is the gate correctly flagging an SVO-constraint artifact and
  correctly routing it to prose-variation resolution at the stitch layer.

  Step 4 (stitcher resolution evidence): The c09 render-log explicitly shows the stitcher
  varied the "marks" verb at all three occurrences. The c10 fixer log shows
  "corwick marks → corwick walks the errand-corridor" specifically to avoid marks-mannerism
  (resolved at the fixer level before the stitcher even needed to act). There is no
  evidence of stitch-layer failure on any prior "marks" carry-forward. The
  advisory-and-resolve path is functioning correctly.

  Step 5 (c16 new element — exact VERB+OBJECT pair repeat): "marks the storehouse wall"
  appears at s01n02 and s03n05 — the same exact pair twice. The formal REGISTER-AS-MANNERISM
  gate fires at ≥3 of the same pair; 2 is below the HARD threshold. The auditor correctly
  called it advisory and flagged it as the highest-risk instance, routing to Phase 3
  redundancy cull and Phase 8 editorial reflection. This is the correct disposition.
  The within-chapter exact-pair repeat is a new severity sub-class, but the gate caught
  it and routed it at the right severity. A stricter threshold (≥2 as HARD) would
  over-fire on legitimate bookend-callback pairs. Advisory-plus-flag is the correct
  calibration; no gate-criterion gap.

  Step 6 (signal-002 occasion-carrier mapping): Gate correctly identified that the
  event_map entry for "taylor-has-full-counter" is mapped to an occasion-carrier bone
  without an omission_rationale annotation. The gate correctly routed interior-state
  delivery to the narrator-interest facet. No fixer action required; no bone revision.
  Pure content flow, not a process gap.

  Step 7 (Phase-3 MT-2 SOFT — no feed-tracking bone during s03 walk): SOFT findings
  are non-blocking by design. The inference carries via n08 (foreclosure-not-flight).
  The gate correctly classified this as SOFT and accepted it with rationale.
  Not a process failure.

rationale: |
  Three independent findings, three clean OK judgments. Signal-001 ("marks" advisory):
  the gate is functioning as designed; the SVO fence structurally constrains the verb
  set for instrument/record/environment bones; the stitcher resolves the advisory at
  prose layer; the existing SIGNAL detection is already the AP-SCAN equivalent for this
  class; adding a new AP-SCAN would duplicate live gate logic. Signal-002 (occasion-carrier
  mapping): routing-gap identification with correct facet-resolution routing; not a
  process gap. Phase-3 SOFT: correctly dispositioned non-blocking with inference carry.

  On the 5-chapter "marks" recurrence: the recurrence count does not override the
  content-vs-process discrimination. What matters is whether the SAME FAILURE CLASS
  recurs, and the "marks" advisory is architecturally forced (SVO fence + instrument-class
  verb set), not an authoring error. The stitcher has not failed on any prior carry.
  A screen-writer brief constraint would conflict with the SVO fence; a new AP-SCAN would
  replicate existing gate logic. Standard hold: the appropriate trigger for a process
  change is stitch-layer failure on a "marks" advisory carry, not bone-gate advisory
  recurrence. This entry is the N=5 occurrence marker.

  The c16 within-chapter exact-pair repeat ("marks the storehouse wall" ×2) is the most
  novel element in this dispatch. It is adjacent to REGISTER-AS-MANNERISM territory
  (one below the ≥3 HARD threshold). The auditor's advisory-plus-flag route is correctly
  calibrated. If a future chapter produces an exact-pair count of ≥2 AND the stitcher
  fails to vary it in the draft, that is the triggering evidence to revisit the ≥3
  HARD threshold (or add a ≥2 SIGNAL-with-stitch-block disposition).

trade-off: |
  Not proposing means the "marks" advisory pattern is not formally tracked as a
  promotion candidate in the proposals log. Mitigated by: this decisions-log entry
  explicitly counts N=5 and records the architectural root cause; the stitcher has
  resolved every prior instance; if stitch-layer failure occurs on c16 or a future
  chapter, that is the triggering evidence and the evidence trail is here.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0092 | 2026-06-04 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/audience/ (Phase 5b cycle-1 FAIL b01c16 NI:6 thesis-narrating; Phase 5 HARD moral_legibility Drift-old)
  source_verdict: |
    Phase 5b cycle 1 FAIL: interest-narrator REVISE 3-of-3 on NI:6 @20 thesis-narrating
    the foreclosure-vs-suppression distinction (DEC-0090 item 4). Resolved cycle 2.
    Phase 5 HARD: state-updates @19 moral_legibility recorded 4->4.5 (series-baseline)
    instead of 6.0->6.5 (chapter-entry value); fixed.
  gate_path: .claude/commands/and-facets.md#phase-5b

question: |
  Two judgment calls:
  Q1: Does the NI:6 thesis-narrating catch indicate a process gap -- specifically, should
      the no-thesis-restatement watch (DEC-0090 item 4) be promoted to a RUBRIC-FIDELITY
      REJECT entry in the NI rubric so Phase 5 catches it mechanically (Rule 11 path)?
  Q2: Does the moral_legibility 4-vs-6.0 mismatch indicate the Phase 1 state-updates-actor
      dispatch payload needs the current per-axis chapter-entry value supplied explicitly?

decision: Q1 -> OK (first-occurrence hold, no process change). Q2 -> PROCESS-CHANGE-PROPOSED PROP-0041.

basis: |
  Q1: Step 2 (content vs. process discrimination).
  Phase 5b IS the correct catch point for the thesis-narrating class. Discriminating
  a legitimate channel-registration from a moral-category-parse restatement requires
  loading the chapter's substance contract + behavior pack -- inputs the Phase 5
  mechanical auditor does not receive and is not structured to process. Moving this
  catch to Phase 5 would require the auditor to become a different gate. The gate
  worked correctly (Phase 5b caught what DEC-0090 item 4 pre-flagged). N=1;
  Rule 11 threshold (>=3) not met. First-occurrence hold.

  Q2: Step 2 (content vs. process discrimination).
  Drift-old HARD per state-updates rubric: "<old> must match the most-recent prior cited
  value." The Phase 1 state-updates-actor dispatch payload (and-facets.md Phase 1 item 5)
  names: character stack + base proto-lines + per-chapter substance_delta + rubric.
  Current per-axis entry values are NOT named. The substance_delta gives delta targets,
  not the current-entry anchor. Without an explicit payload route to the character's current
  axis values, the impersonator defaults to the series-baseline start_rank (the most visible
  rank in the axis definition). Deterministic spec omission; S-cost fix; N=1 first-occurrence
  proposal warranted per PROP-0027 analogy (first live test, deterministic gap).

rationale: |
  Q1: Gate over-performed (caught at Phase 5b a risk DEC-0090 item 4 had flagged as a
  stitch-layer watch). No structural gap. The NI rubric's existing anti-patterns 1+3 cover
  the general Author-voice-intrusion + Generic-curiosity class; the no-thesis-restatement
  sub-case requires contextual judgment Phase 5 is not equipped for. Hold at N=1.

  Q2: After 16 chapters, a substance axis can be 2+ units above its series-baseline. The
  dispatch payload gives delta targets (how much it moves this chapter) but not the anchor
  (where it stands entering the chapter). The impersonator used the only available value --
  the series-baseline start_rank -- and produced a Drift-old HARD. Adding the character's
  actor state file to the dispatch payload closes this deterministically.

trade-off: |
  Q1 trade-off: holding means a future chapter could re-emit thesis-narrating NI at the
  same gate. Mitigated by DEC-0090 item 4 standing watch + Phase 5b remaining armed.
  N=1 occurrence marker logged here; N=3 triggers Rule 11 promotion.

  Q2 trade-off: PROP-0041 adds one payload file per per-actor state-updates dispatch.
  Slightly larger impersonator context; eliminates a deterministic Drift-old class.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0093 | 2026-06-04 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01-c16-2026-06-04.md
  source_verdict: |
    SHIPPED-WITH-CAVEATS (Class-B; DEC-0090 SHIPPED-WITH-RISK-RECORDED coupling auto-ship;
    CONTINUE=no on event-poverty/quiet-aftermath; central event recovered; Phase 8.5 PASS).
    FOURTH consecutive quiet falling chapter to ship SHIPPED-WITH-CAVEATS (c13 was PASS;
    c14 DEC-0085 / c15 DEC-0087 / c16 DEC-0090). Consecutive count since last
    cohere_acknowledgment clearance: c14+c15+c16 = 3.
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]
verdict: OK-MERGED-INTO PROP-0037

question: |
  Four consecutive quiet falling chapters shipping SHIPPED-WITH-CAVEATS. Two sub-questions:
  (A) Is the repeated single-chapter Class-B disposition still the right lever, or has evidence
      accumulated to the point where /and-cohere b01 c13-c16 should be the recommended
      resolution for the whole run of depth-passes rather than per-chapter /and-write revise
      --from-signals?
  (B) Does the recurring quiet-falling-chapter pattern indicate a book-structural issue (too
      many consecutive falling chapters before the c17 cascade) that should surface to the
      principal?

decision: OK-MERGED-INTO PROP-0037 (recurrence_count 3 -> 4).

basis: |
  Step 1 (proposals log):
    PROP-0037 (status: open) targets /and-substance chapter Phase 0 HARD-abort at
    consecutive_shipped_with_caveats >= 3 without cohere_acknowledgment. That threshold has
    now been hit for a SECOND independent run (c10/c11/c12 was the first; c14/c15/c16 is the
    second). No rejected or deferred proposal overlaps. No proposal covers the sub-questions
    (A) resolution-layer choice or (B) book-structural surface separately from PROP-0037.
    recurrence_count merges into PROP-0037: 3 -> 4.

  Step 2 (content vs. process — question A):
    The per-chapter depth-pass obligations for c14/c15/c16 are MANDATORY before book-close
    (they gate /and-substance book b02 Phase 0 + /and-review verdict b01) and are
    chapter-scoped at the bone/texture level. c14 targets courier-as-person + Sera-stake.
    c15 targets event-poverty texture. c16 targets position-arithmetic concreteness +
    Halvard-pressure physical signal + s01 props + s03 thesis-restatement trim. These are
    three independently-specified bone-level briefs. /and-cohere c13-c16 would be a
    cross-chapter cold-read, not a bone-level revise — it cannot deliver the per-chapter
    depth passes. The correct resolution order is: (1) per-chapter depth passes (mandatory,
    chapter-scoped), then (2) /and-cohere on the whole arc (cross-chapter accumulation
    handler, before book-close). /and-cohere is additive and complementary, not a substitute.
    No process gap: existing decisions (DEC-0087/0089) already name /and-cohere before
    book-close as the accumulation handler. This is not a process failure — it is a
    question of sequencing the two existing mechanisms. The answer is: depth passes first,
    then /and-cohere.

  Step 3 (content vs. process — question B):
    The c13-c16 falling arc was structurally endorsed at /and-substance book with explicit
    dramatic_shape annotations. Dramatist ACCEPT on each individual chapter. The cold-reader's
    event-poverty/quiet-aftermath complaints are all pre-authorized design-inherent costs of
    a deliberate multi-chapter falling arc. DEC-0089 dispositioned the identical question at
    N=2 (c14+c15): "adding a structural gate on 'no more than N consecutive falling chapters'
    would be a taste-gate on architectural story structure, which is human-only territory per
    methodology." N=3 does not change this ruling. The book structure is the principal's domain;
    no gate in the existing chain is positioned to catch this without overriding a series-audit-
    approved structural contract. First-occurrence hold on book-structural escalation: DEC-0089
    explicitly held at N=2 and the evidence at N=3 is qualitatively identical.

  Step 4 (recurrence):
    PROP-0037 was authored at N=3 (c10/c11/c12). The current c14/c15/c16 run is a second
    independent N=3 sequence post-cohere-clearance. This is the 4th data point confirming
    the N=3 threshold is correctly calibrated. The failing class matches exactly (quiet falling
    chapters, design-inherent cold-reader complaints, coupling-rule auto-ship). Merge is
    mandatory per process-critic procedure (same target.path + change_type as an open proposal).

  Step 5 (methodology):
    Reversibility: no new proposal needed; merging into the existing open proposal is lower
    blast radius than a new redundant entry.
    Cost: incremental update to PROP-0037 is S-cost.
    Optionality: the /and-cohere c13-c16 recommendation (before book-close) is already
    named in decisions.md. No process change required to surface it; it is in the existing
    end-of-run summary machinery.
    Convention: DEC-0089 held at N=2; DEC-0079 proposed at N=3; both cases are exact
    precedent for the current ruling.

rationale: |
  Question A: /and-cohere is the right resolution for cross-chapter accumulation, but it
  is NOT a replacement for the mandatory per-chapter depth passes. The three depth-pass
  briefs (c14/c15/c16) target specific bone-level defects that /and-cohere does not touch.
  The correct sequence — per-chapter depth passes first, then /and-cohere c13-c16 before
  book-close — is already encoded in the existing decisions and the depth-pass obligation
  records in showrunner memory. No process change needed; the recommendation is: run the
  three mandatory depth passes, then run /and-cohere c13-c16.

  Question B: The c13-c16 falling-arc structure is a series-audit-approved design choice.
  Surfacing it as a structural problem to the principal would be proposing a taste-gate on
  endorsed architecture. DEC-0089's exact reasoning applies. Hold.

  PROP-0037 merge: The second independent N=3 run confirms the threshold is correctly
  calibrated. recurrence_count increments to 4. No new evidence argues for changing N=3
  to N=2 (DEC-0089 explicitly rejected that — mid-arc cohere firing at N=2 would violate
  the falling-arc endorsement). No new evidence argues for changing N=3 to N=4.

trade-off: |
  Merging into PROP-0037 rather than proposing a new entry means no additional triage
  burden for the principal. The recommendation to run /and-cohere c13-c16 (after depth
  passes) lives in this decisions entry and DEC-0087/0089 — not in a new proposal, which
  is correct because it is an operational recommendation, not a process-change proposal.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

id: DEC-0094
date: 2026-06-04
mode: user-proxy
question: |
  b01c17 Phase 5.5 CHUNK-CLASS-B disposition: R (revise chunk), P (proceed with risk recorded),
  or S (substance-contract revision)? Phase 5 passed 3/3 with irony judged enacted-not-declared;
  cold-read strict-no dominated by uninformed-reader artifacts + known event-density risk;
  event-density risk already targeted by write-time enactment carries flowing into /and-write;
  three chapters of direct precedent (DEC-0085/0087/0090).
decision: P — proceed with risk recorded
basis: prior-ruling (DEC-0085/0087/0090 exact precedent family) + methodology-3b (cost) + methodology-3a (reversibility)
rationale: |
  Fourth consecutive Class-B P in the c14/c15/c16/c17 sequence. Pattern identical each time:
  uninformed-reader cold-read returns strict-no on (a) withheld serial context (Earth-Bet fence /
  prior-chapter backstory) and (b) event-density / interior-accounting-dominant staging. Both
  categories pre-dispositioned as design-inherent across the entire book.

  Phase 5 signal is decisive and points opposite to revision: 3/3 SUBSTANCE-FELT on all 4 scenes,
  dramatist ACCEPT, auditor 0-HARD. "The irony is enacted, not declared" is exactly the test the
  substance contract sets for this chapter, and the informed reviewers returned a clean PASS.

  The cold-read's load-bearing genuine finding — item (d), four scenes restating the same internal
  ledger-recalculation with little physical action — is already addressed by the write-time
  enactment carries (recognition-as-physical-feed-events / hand-acts / enacted-absence) flowing
  into /and-write as the correction layer. Fixing this at the chunk layer would either (i) be
  redundant, or (ii) damage the substance contract by forcing staging additions that alter
  axis-movement math.

  (R) is wrong layer — chunk design is not broken.
  (S) is wrong layer and wrong cost — substance contract passes all informed gates.
  (P) with cold_read_risk_carry is correct: preserve the cold-read finding as targeting brief
  for /and-write; arm /and-stitch Phase 8.5/9 for the same complaint class.

  cold_read_risk_carry items for /and-write:
    1. (HARD watch) Recognition of moral_framework mirror must be ENACTED via physical feed-event
       or observable hand-act, not restated as interiority across multiple scenes.
    2. (HARD watch) Norren-attribution act: concrete physical write-action required — the forgery
       must be staged as a thing Taylor does with her hands/tools, not summarized as decision.
    3. (SOFT) Wren-identity context: single grounded detail (role/relationship) per scene-entry
       to anchor the uninformed reader; licensed by context-ledger.
    4. (design-inherent CONTINUE=No) Cold-reader strict-no on jargon (stitch-house, Hook,
       ward-read) and withheld prior-chapter motive — pre-authorized serial mid-point categories;
       stitch Phase 4+9 carry.

trade-off: |
  Only cost of P is forwarding the event-density risk to /and-write. Write-time carries already
  target exactly this risk. No realistic scenario where R or S produces a better chapter at lower
  total cost given the clean substance contract.
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0095 | 2026-06-05 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01-c17-2026-06-05.md
  source_verdict: |
    SHIPPED-WITH-CAVEATS (Class-B; DEC-0094 SHIPPED-WITH-RISK-RECORDED coupling auto-ship;
    CONTINUE=no on event-poverty / interior-accounting-density / withheld-prior-chapter-motive /
    jargon-opacity — all pre-authorized in cold_read_risk_carry per DEC-0094). Fourth
    consecutive in the c14-c17 sequence; fifth data point overall across both independent runs
    (c10/c11/c12 + c14/c15/c16/c17).
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]
verdict: OK-MERGED-INTO PROP-0037 (recurrence_count 4->5)

question: |
  Four consecutive Class-B SHIPPED-WITH-CAVEATS (c14/c15/c16/c17) auto-shipping on the
  same uninformed-reader-artifact family (event-poverty, interior-accounting-density,
  withheld prior-chapter motive). Is this (a) a correctly-functioning pre-authorization
  mechanism doing its job, or (b) a process gap where the auto-ship coupling is masking
  accumulating real readability debt that /and-cohere should be catching at the stretch
  level?

decision: OK-MERGED-INTO PROP-0037 (recurrence_count 4->5). No new proposal.

basis: |
  Step 1 (proposals log):
    PROP-0037 (status: open) targets /and-substance chapter Phase 0 HARD-abort at
    consecutive_shipped_with_caveats >= 3 without cohere_acknowledgment. DEC-0093 merged
    c16 as count 3->4 for the second independent run. C17 is the fourth consecutive in this
    run; recurrence_count increments to 5. No other open proposal overlaps this target +
    change_type. No rejected proposal covers it.

  Step 2 (framing question — option A vs B):
    Option A (mechanism working correctly): confirmed. The cold-reader's CONTINUE=No findings
    map entirely to pre-authorized categories established at DEC-0094: (a) event-poverty /
    interior-accounting-density = design-inherent multi-chapter falling arc contract
    (series-audit-approved); (b) withheld prior-chapter motive = Earth-Bet fence + serial
    mid-point context noise; (c) jargon opacity = design-inherent serial mid-point. The
    cold-reader is structurally uninformed — no serial context, no prior chapters. The
    coupling rule was designed to discriminate exactly this artifact from a genuine delivery
    failure. The cold-read report confirms the central event was recovered (§6 summary
    accurate) and the moral turn maps to goal. The coupling is doing its job.

    Option B (masking accumulating debt): the accumulation handler is /and-cohere, not the
    per-chapter coupling rule. The per-chapter depth passes (c14/c15/c16/c17) target bone-
    level defects. /and-cohere is the cross-chapter accumulation handler. The correct
    resolution sequence — mandatory depth passes per chapter, then /and-cohere c13-c17
    before book-close — is identical to the DEC-0093 ruling at N=3 and DEC-0089 ruling at
    N=2. Not a process gap; correct sequence already encoded in existing decisions.

  Step 3 (book-structural question):
    DEC-0089 ruled "adding a structural gate on 'no more than N consecutive falling chapters'
    would be a taste-gate on architectural story structure, which is human-only territory."
    DEC-0093 confirmed at N=3. N=4 does not change this ruling — the c14-c17 arc is
    series-audit-approved with dramatist ACCEPT on each chapter. No escalation warranted.

  Step 4 (recurrence and merge):
    Fifth data point across two independent N=3+ runs. Merge mandatory (same target.path +
    change_type, status: open). recurrence_count 4->5.

  Step 5 (methodology):
    Reversibility: merge into existing open proposal. Cost: S-cost append.
    Optionality: /and-cohere c13-c17 before book-close named in DEC-0087/0089/0093 — no
    additional process change needed to surface it.
    Convention: DEC-0089 (N=2), DEC-0093 (N=3), this dispatch (N=4) — consistent hold.

rationale: |
  The pre-authorization mechanism is functioning correctly. The coupling correctly
  discriminated uninformed-reader artifacts from genuine delivery failures. Auto-ship is
  not masking debt — the debt is tracked via mandatory per-chapter depth-pass obligations
  in the parking lot. /and-cohere is the named accumulation handler; the correct sequence
  is: depth passes first, then /and-cohere c13-c17 before book-close.

  PROP-0037 merge: second independent N=4 run confirms N=3 threshold is correctly
  calibrated. No evidence for changing the threshold in either direction.

trade-off: |
  Merging into PROP-0037 keeps triage burden minimal. The /and-cohere c13-c17
  recommendation is an operational call, not a process-change proposal — it lives in
  this decisions entry and DEC-0087/0089/0093.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

id: DEC-0096
date: 2026-06-05
mode: user-proxy
track: FAST (RUNBOOK R1)
question: |
  b01c18 Phase 5.5 CHUNK-CLASS-B disposition: R (revise chunk), P (proceed with risk recorded),
  or S (substance-contract revision)? Climax chapter — irrevocable-Khepri-repetition deployment
  (Dance-pulse 2). Phase 5: 3/3 audience ACCEPT (SUBSTANCE-FELT; design enacts, not explains;
  irrevocable threshold lands in physical action; contempt near-saturation earned; s05
  accounting-close names catastrophe through form), dramatist ACCEPT (correct climax shape),
  auditor 2 HARD bookkeeping-text faults being corrected. Cold-read CHUNK-CLASS-B: strict
  CONTINUE=no on event-poverty/no-dialogue/no-on-page-resistance + anti-climax-by-design;
  majority of no is uninformed-reader artifact (unknown characters, unknown insect-control
  mechanism, unnamed prior-city). Surviving signals: (1) five scenes flawless-operator execution,
  no antagonist on-page, no dialogue, no scene-level reversal; (2) ends on accounting-close
  form, catastrophe asserted not dramatized.
decision: P — proceed with risk recorded
basis: prior-ruling (DEC-0094/0090/0087/0085 exact precedent family) + methodology-3b (cost) + methodology-3a (reversibility)
rationale: |
  Fifth consecutive Class-B P in the c14/c15/c16/c17/c18 sequence. Pattern identical each time:
  uninformed-reader cold-read returns strict-no on (a) withheld serial context (Earth-Bet fence /
  character/mechanism backstory) and (b) event-density / interior-accounting-dominant staging.
  Both categories pre-dispositioned as design-inherent across the entire book.

  Phase 5 signal is decisive and points opposite to revision: 3/3 SUBSTANCE-FELT across all 5
  scenes, dramatist ACCEPT on correct climax shape (precipice → irrevocable act → consequence-
  running → accounting close), auditor 0-HARD on design/prose/thematic. The "design enacts rather
  than explains" and "the accounting-close names the catastrophe through form" verdicts are exactly
  the test the substance contract sets for the climax chapter — the catastrophe-of-accuracy IS the
  ledger closing cleanly. That IS the dramatized event. The informed reviewers returned a clean PASS.

  The surviving cold-reader signals are both subcategories of event-poverty:
  (1) No-dialogue / no-on-page-resistance is design-inherent on an irrevocable-deployment chapter
  where the antagonist faction is OFFSTAGE and the opposition is the operator's own moral reckoning —
  putting an antagonist on-page would falsify the substance contract.
  (2) Anti-climax-by-design / catastrophe-asserted-not-dramatized — this is the c18 analog to
  c17's "irony enacted not declared." The accounting close IS the dramatization; the cold-reader
  cannot see this without 17 chapters of context establishing what "the ledger closes cleanly"
  means for this character and this chapter's irrevocable threshold.

  (R) is wrong layer — chunk design is not broken; it passed every informed gate.
  (S) is wrong layer and wrong cost — substance contract passes all informed gates; auditor HARDs
  are bookkeeping-text, not design.
  (P) with cold_read_risk_carry is correct: preserve surviving signals as /and-write targeting
  brief; arm /and-stitch Phase 8.5/9 for the same complaint class.

  cold_read_risk_carry items for /and-write:
    1. (HARD watch) Irrevocable-threshold moment must be ENACTED as a concrete physical act
       (the deployment decision/action must be staged as something Taylor does with her hands/tools/
       body at the moment of no-return), not solely rendered as interiority or ledger-accounting.
    2. (HARD watch) At least one scene must carry a physical resistance signal — even if antagonist
       is offstage, the op itself must encounter friction (technical, environmental, or self-imposed)
       that makes the "flawless execution" read as chosen precision, not narrative convenience.
    3. (SOFT) The accounting-close s05 form must make the "both facts are true" structure concrete
       enough that a reader 17 chapters deep cannot miss it — pair it with at least one specific
       physical outcome named in the scene (not abstract moral summary).
    4. (design-inherent CONTINUE=No) Cold-reader strict-no on unknown characters (Otto/Sera/Wren/
       Norren/Jarvis), insect-control mechanism opacity, unnamed prior-city (Earth-Bet fence) —
       pre-authorized serial mid-point categories; stitch Phase 4+9 carry.

trade-off: |
  Only cost of P is forwarding the event-poverty risk to /and-write. The write-time carries
  (items 1-3) directly target the diagnosable residue. No realistic scenario where R or S
  produces a better climax chapter at lower total cost given the clean substance contract.
  Climax chapters carry the highest substance-contract precision requirement; revising at chunk
  layer against three full-pass informed reviewers risks false-repair that damages the contract.
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0097 | 2026-06-05 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: signal-accepted-at-emit
  source_report: active-project/staff/auditor/write-b01c18-bone-gate.md
  source_verdict: |
    /and-write b01c18 Phase 6 bone-gate PASS — 0 HARD; 4 SIGNALs all accepted-not-remediated
    (signal-001 s04 abstraction-dominance 1/8; signal-002 s05 abstraction-dominance 2/11 +
    s03 movers non-grounding; signal-003 s03n09 "the contempt arrives" abstract-subject;
    signal-004 s03n06/n10 byte-identical SVOs intentional-refrain).
  gate_path: .claude/commands/and-write.md#phase-6
verdict: OK

question: |
  (A) Is the recurring ABSTRACTION-DOMINANT fire-and-accept pattern for accounting/cipher chapters
  (s04 cipher-delivery + s05 accounting-close in c18; cf. c17 s02, c11 s02/s03, c08/c16 airless-risk)
  a signal that the bone-gate->stitch-Phase-4 handoff needs structural modification for
  abstraction-heavy design-inherent chapters, or is per-chapter carry working as designed?
  (B) Is the byte-identical intentional-refrain SVO pattern (s03n06/s03n10 "files the court-entry")
  something the bone-gate needs a first-class disposition category for rather than per-chapter SIGNAL?

decision: OK on both questions. No new proposal. No merge required.

basis: |
  Step 1 (proposals log):
    Searched for open proposals targeting abstraction-dominance + stitch-Phase-4 handoff:
    PROP-0023 (apparatus-dominant whole-chapter airlessness — bone-level cure; status: open)
    PROP-0030/PROP-0031 (cross-chapter apparatus-register accumulation; status: open, both)
    None of these has the same target + change_type as what this dispatch would propose.
    No rejected proposal covers either candidate.

  Step 2 (Question A — abstraction-dominance fire-and-accept structural fix):
    DEC-0073 is the controlling prior ruling on this class. It established definitively:
    (1) The SIGNAL is load-bearing as the stitch-carry trigger. A carve-out or mechanical
        fix that eliminated the SIGNAL would remove that trigger — net-negative.
    (2) The accept-with-rationale path is the designed handling when abstraction is
        design-intrinsic. That path is functioning correctly.
    (3) Cross-chapter accumulation is PROP-0030/PROP-0031's designed scope. Per-chapter
        gates cannot see cross-chapter accumulation by construction.
    (4) Audience 3-of-3 SUBSTANCE-FELT confirms downstream delivery is succeeding.

    The b01c18 evidence is not meaningfully different from b01c11 (DEC-0073). The two
    scenes (s04 cipher/packet, s05 accounting-close) are design-inherent: the intelligence-
    delivery mechanism IS sparse ciphers and packets; the accounting-close IS the s05 form
    by substance contract. The mover-level signal-003 (s03n09 "the contempt arrives") is
    also earned (compound-eye n01-n04 supply the grounding; n09 is a synthesis vehicle).
    All four signals carry appropriate stitch-Phase-4 obligations. The grounding-ledger (if
    open from prior chapters) covers s05's accounting-close need. The existing mechanism
    is doing its job.

    Could a stricter version of the existing gate have caught a process failure? No — there
    is no process failure. The gate fired correctly. The rationales are logged. The carries
    are targeted. Audience confirmed delivery. Pure content-handling, not a process gap.

    Discrimination: is the multi-point abstraction-dominance within a climax chapter a new
    class? It is structurally denser than c11 (two distinct scene types + a mover-level
    abstract-subject in the same chapter). However: (a) c18 is a PASS with 0 HARD and
    audience 3/3 SUBSTANCE-FELT; (b) the multi-point fires are explained by distinct scene
    designs (cipher-delivery = sparseness by design; accounting-close = ledger-register by
    design; mover-level contempt-synthesis = upstream-grounded by n01-n04); (c) the stitch-
    Phase-4 carries name each specific bone/scene. No pattern failure at gate level.

    Cross-chapter accumulation data point: c18 is a climax chapter structurally distinct
    from the apparatus-register-accumulation falling-arc stretch (c02-c17). Its abstract
    register is the catastrophe-enacted-through-form; the cold-reader cannot see this
    without the prior 17 chapters. Not a merge-qualifying recurrence for PROP-0030's
    cross-chapter apparatus-density concern. Standard OK.

  Step 3 (Question B — byte-identical intentional-refrain disposition category):
    First occurrence of intentional verbatim SVO repetition as a design-refrain (below the
    >=3 mannerism threshold). The gate caught it correctly (SIGNAL-004 with design-intent
    rationale). The stitch-Phase-4 carry ("render as perceptibly-the-same-act, not
    accidentally-repeated prose") is the correct downstream obligation. The pattern is
    chapter-specific (s03 "seventh-day filing = first-day filing" contempt-as-form design);
    not architectural to the project. No prior chapter has used byte-identical SVOs as a
    design refrain.

    A first-class disposition category would add specificity at the cost of modifying
    /and-write.md Phase 6 for a first-occurrence chapter-specific pattern. The existing
    SIGNAL path IS a disposition — it names the design intent, flags the stitch obligation,
    and does not block. Standard first-occurrence hold per process-critic Rule step 4.

  Step 4 (methodology):
    Reversibility: per-chapter SIGNAL carry is reversible at stitch if it over-fires.
    A new gate category is lower-reversibility (once added, always fires).
    Cost: OK is S-cost; a gate modification on /and-write Phase 6 is M-cost at minimum.
    Blast radius: per-chapter carry affects this chapter only; a gate modification
    affects every future invocation of Phase 6. Methodology favors OK at N=1 on both.

rationale: |
  Both patterns are handled correctly by the existing process. The bone-gate->stitch-Phase-4
  carry IS the structural fix — it is the designed handoff for accepted SIGNALs. Audience
  3/3 SUBSTANCE-FELT confirms downstream delivery is landing. DEC-0073 is the controlling
  ruling; b01c18 adds no new evidence class that would change it. The byte-identical-refrain
  is a first-occurrence chapter-specific design choice; the gate caught it and named the
  stitch obligation; no first-class disposition category is warranted at N=1.

trade-off: |
  Cost of OK on Question A: a future chapter where abstraction-dominance is NOT design-inherent
  but the gate accepts it anyway would not be caught by a structural fix. However, the accept-
  with-rationale discipline IS the structural fix; it requires the rationale to name the design
  license. A failure of accept-with-rationale discipline is a gate-execution failure, not a
  gate-design gap.
  Cost of OK on Question B: a future intentional-refrain pair without clear design-rationale
  would only be caught as a below-threshold advisory. Acceptable at N=1.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0098 | 2026-06-05 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01-c18-2026-06-05.md
  source_verdict: |
    SHIPPED-WITH-CAVEATS (Phase 9 cold-read CONTINUE=no; all complaint categories pre-authorized
    in chunk_cold_read.cold_read_risk_carry per DEC-0096; auto-ship, no retry). Fifth consecutive
    Class-B cold-read CONTINUE=no in the c14-c18 stretch (c14 DEC-0085 / c15 DEC-0087 /
    c16 DEC-0090 / c17 DEC-0094 / c18 DEC-0096). Complaints: event-poverty / no-dialogue /
    no-on-page-resistance / anti-climax-by-design. c18 is the CLIMAX chapter.
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]
verdict: OK-MERGED-INTO PROP-0037 (recurrence_count 5->6)

question: |
  Two sub-questions from the trigger:
  (a) Is the 5-consecutive-chapter Class-B accumulation across the collapse arc a signal that
      the depth-pass-before-book-close mechanism needs strengthening, or that /and-cohere b01
      c13-c18 (the accumulation handler per DEC-0095) should be elevated from optional to a
      book-close precondition?
  (b) Is shipping 5 consecutive chapters with CONTINUE=no — even pre-authorized — a quality-debt
      accumulation the per-chapter Class-B disposition is structurally blind to (each chapter is
      locally justified; the STRETCH is the problem /and-cohere is designed to catch)?

decision: OK-MERGED-INTO PROP-0037 (recurrence_count 5->6). No new proposal. No threshold change.

basis: |
  Step 1 (proposals log):
    PROP-0037 (status: open, recurrence_count: 5) targets /and-substance chapter Phase 0
    HARD-abort at consecutive_shipped_with_caveats >= 3 without cohere_acknowledgment.
    DEC-0095 merged c17 as count 4->5 for the second independent run. C18 is the fifth
    consecutive in this run; recurrence_count increments to 6. No other open proposal
    overlaps this target + change_type. No rejected proposal covers it.

  Step 2 (question a — depth-pass-before-book-close mechanism):
    Current per-chapter depth-pass obligations as of c18 ship:
      - c10: PASS-WITH-DEPTH-PASS-REQUIRED (bone-level staging, from DEC-0066/0070)
      - c14: mandatory per DEC-0085 (texture-level: courier-as-person, Sera-stake)
      - c18: mandatory per DEC-0096 (HARD watches: enacted irrevocable-threshold physical act
               + op-friction signal; SOFT accounting-close concreteness)
      - c15/c16/c17: Case 1 SHIPPED-WITH-CAVEATS, no mandatory depth pass (all complaints
               fully covered by design-inherent/cold-context carries; DEC-0087/0090/0095)
    The per-chapter mechanism is correctly discriminating which chapters need depth passes
    and which do not. The three mandatory passes (c10, c14, c18) are logged in the parking
    lot; they are not invisible to the process — they are precisely tracked. The mechanism
    is not blind to the stretch; the stretch has two distinct components:
      (i) the design-inherent Class-B shipments (c11/c12/c15/c16/c17) which correctly carry
          no depth-pass obligation because all complaints are covered by the substance contract
      (ii) the tractable-residue chapters (c10/c14/c18) which correctly carry mandatory
           depth passes because tractable gaps were identified
    Strengthening the book-close mechanism would mean adding a gate that fires when these
    mandatory depth passes remain unresolved at book-close. That gate already has a natural
    home: /and-review verdict (the orchestrator-critic pass, which is the canonical
    book-close command). The parking-lot items for c10/c14/c18 are the signal. No new
    structural mechanism is needed — the existing /and-review verdict pass is the
    enforcement surface, and PROP-0037's consecutive-counter gate fires the /and-cohere
    obligation at chapter-start. The two-layer enforcement (PROP-0037 at chapter-start +
    /and-review verdict at book-close) is already the correct architecture.

  Step 3 (question b — is the stretch structurally invisible to the per-chapter disposition?):
    No. The stretch is visible at two levels:
      (i) PROP-0037 (open, untriaged) is exactly the gate that makes it visible at
          chapter-start: consecutive_shipped_with_caveats >= 3 fires a HARD-abort unless
          cohere_acknowledgment is present. This gate has been open since DEC-0079 (c12)
          and is the correct enforcement surface for "the stretch is the problem."
      (ii) The /and-cohere recommendation (run c13-c18 before book-close) has been named
           as the accumulation handler in DEC-0087/0089/0093/0095. It is not a per-chapter
           call; it is an explicit book-level obligation recorded in the decisions log.
    The question "should /and-cohere be elevated from optional to book-close precondition"
    is correctly answered: it is NOT optional under the current process. DEC-0080 established
    that /and-cohere is required before the next chapter when consecutive count >= 3;
    DEC-0095 names it as the mandatory accumulation handler before book-close. The process
    already encodes the obligation; PROP-0037 is the gate that enforces it mechanically.
    The gap is that PROP-0037 is untriaged and unimplemented — that is a triage-urgency
    issue, not a new process-change proposal.

  Step 4 (c18 climax chapter signal — does it change the analysis?):
    c18 is the climax chapter. This is the highest-stakes ship in the stretch. However,
    the climax PASSED every informed gate: 3/3 SUBSTANCE-FELT (Phase 5), dramatist ACCEPT
    on correct climax shape, auditor 0-HARD on design/prose/thematic. The cold-reader's
    CONTINUE=no is structurally identical to prior chapters — uninformed-reader artifact
    on design-inherent causes (offstage antagonist, accounting-close IS the dramatized event,
    Earth-Bet fence). DEC-0096 correctly identified the surviving tractable signals (items 1-3)
    and wrote targeted cold_read_risk_carry. The climax chapter being the fifth consecutive
    is evidence that PROP-0037 should be triaged urgently before book-close — not evidence
    that a new proposal is needed. The right call is urgency escalation on existing open work,
    not a new process-change proposal.

  Step 5 (book-close enforcement surface question):
    The trigger asks whether /and-cohere should become a "book-close precondition." The
    correct book-close enforcement surface is /and-review verdict — the orchestrator-critic
    pass. That command is the canonical checkpoint for "is the book ready to close." Adding
    /and-cohere as a HARD-abort at /and-review verdict Phase 0 when the consecutive counter
    is >= 3 AND no cohere_acknowledgment is present would be a clean, natural fit. However,
    this would be a modify to /and-review verdict, and PROP-0037 is already the primary
    enforcement proposal (targeting /and-substance chapter Phase 0). A companion proposal
    targeting /and-review verdict is logically distinct but likely redundant with PROP-0037
    if PROP-0037 is implemented — because PROP-0037 fires the HARD at chapter-start, which
    means the consecutive counter cannot exceed 3 without an explicit bypass acknowledgment.
    If PROP-0037 is not implemented, /and-review verdict is the correct fallback. But
    authoring a second proposal now, before PROP-0037 is triaged, would add triage overhead
    on an unsettled foundation. Hold: if PROP-0037 is rejected at triage, then a companion
    /and-review verdict proposal becomes warranted. For now, the correct action is to surface
    triage urgency on PROP-0037, not to author a new proposal.

  Step 6 (recurrence and merge):
    Sixth data point across two independent N=3+ runs. Merge mandatory (same target.path +
    change_type, status: open). recurrence_count 5->6.

rationale: |
  The pre-authorization mechanism is functioning correctly for the fifth consecutive time.
  The per-chapter coupling correctly discriminates design-inherent cold-reader artifacts from
  delivery failures. The stretch is NOT structurally invisible — it is tracked at three levels:
  (a) mandatory depth-pass obligations logged in the parking lot for c10/c14/c18,
  (b) the /and-cohere accumulation handler explicitly named as a book-close obligation in
      DEC-0087/0089/0093/0095, and (c) PROP-0037 (open, untriaged) as the mechanical gate.
  The process gap is not that the mechanisms are absent — it is that PROP-0037 is untriaged.
  The climax chapter being the fifth consecutive auto-ship is the strongest triage-urgency
  signal yet for PROP-0037; it does not warrant a new proposal.

  TRIAGE URGENCY NOTE for principal: PROP-0037 is the open proposal with the highest
  accumulated evidence (recurrence_count: 6). c18 is the climax chapter. Book-close is the
  next major milestone. PROP-0037 should be triaged before /and-review verdict b01 is invoked.
  Companion consideration (adding a /and-review verdict Phase 0 check as a book-close fallback
  if PROP-0037 is rejected) is noted here as a conditional follow-on, not a separate proposal.

trade-off: |
  Merging into PROP-0037 means no new triage item. The /and-cohere c13-c18 recommendation
  and the conditional /and-review verdict fallback are operational calls living in this
  decisions entry. If PROP-0037 is rejected at triage, the conditional follow-on surfaces
  and a new proposal would be warranted.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0099 | 2026-06-05 | FAST (user-proxy, RUNBOOK R1)

question: |
  b01c19 Phase 5.5 chunk cold-read disposition. CHUNK-CLASS-B (summary maps to goal;
  strict-continue=no). Three cold-reader complaints: (a) three-of-four scenes are the
  same beat (emotional stasis / escalating abstraction), (b) heavy proprietary vocabulary
  (the accounting / bottlefly nodes / contempt-color / a different column) — followability
  risk, (c) s04 stakes-jump (label reaching upper city) is inferred off-page / asserted
  not dramatized. Options: (R) revise chunk, (P) proceed with risk recorded, (S) substance
  contract revision.

context: |
  b01c19 is the penultimate (falling) chapter of book 1. Thesis: contempt-without-refusal
  at completion — register locked, continuation unchanged — and the first non-terminal
  recognition event. Phase 5 PASSED cleanly: 3/3 SUBSTANCE-FELT (cape-fic, dark-fantasy,
  worm-canon), dramatist ACCEPT (falling-arc sound; recognition correctly non-terminal —
  does not steal c20's climax), auditor 0-HARD (axis sums exact; thesis axes declared).
  Caller's recommended option: (P), arm voice-risk carry to /and-stitch Phase 8.5 + carry
  s04-dramatization concern to /and-write.

options:
  R: Revise chunk. ~1 screen-writer cycle + re-review.
  P: Proceed with risk recorded. SHIPPED-WITH-RISK-RECORDED; arm downstream carries.
  S: Substance contract revision. High cost; reserved for unacceptable (P).

decision: P — proceed with risk recorded, arm downstream carries.

basis: |
  Step 1 (LTM precedent + decisions log):
    DEC-0090/0094/0095/0096 are the exact precedent family: c14/c15/c16/c17/c18 all disposed
    P on CHUNK-CLASS-B with the same complaint categories (emotional stasis / abstraction-
    dominant / jargon-opacity / event-poor). Every one passed Phase 5 3/3 SUBSTANCE-FELT +
    dramatist ACCEPT + auditor 0-HARD. All complaints were pre-authorized as design-inherent
    for the deliberate falling interior collapse architecture.

  Step 2 (goals):
    Goal:1 (pipeline correctness): the informed gates all PASSED — 3/3 SUBSTANCE-FELT,
    dramatist ACCEPT, auditor 0-HARD on design. The uninformed cold-reader's CONTINUE=no is
    explicitly authorized as design-inherent output on this book-level architecture. Chunk
    revision would fight the substance contract the informed gates just endorsed.
    Goal:2 (cost discipline): (R) burns ~1 screen-writer cycle against a non-defective chunk
    and risks de-jargoning at the wrong layer. Jargon/abstraction handling belongs at
    /and-write (concrete SVO bone-staging) + /and-stitch (voice-embodiment + grounding-ledger,
    PROP-0022). (S) is high cost with no indication the contract is broken.

  Three specific complaint dispositions:
    (a) "Three of four scenes are the same beat (naming changed nothing)" — design-inherent.
        The continuation IS unchanged; that is the contempt-without-refusal thesis. The
        accounting-register sameness is the horror, per dark-fantasy-reader's endorsement.
        cl06 cost-paid across four scenes is the structural achievement, not a repetition flaw.
    (b) Proprietary vocabulary followability risk — exactly the recurring jargon-opacity risk
        carried from c17 (DEC-0094). The chain's declared handling is /and-write Phase 6
        (EVENT-NOT-CONCRETE / ABSTRACTION-DOMINANT SIGNAL) + /and-stitch Phase 4
        (voice-embodiment discipline + grounding-ledger). This is NOT a chunk-layer fix.
    (c) s04 stakes-jump (label reaching upper city) asserted not dramatized — this is
        tractable and belongs in /and-write: s04 scene decomposition should include a
        concrete SVO bone that makes the upper-city reach visible on-page rather than inferred.
        This is a cold_read_risk_carry HARD watch into /and-write, not a chunk revision.

  (S) is off the table: auditor 0-HARD + dramatist ACCEPT + 3/3 SUBSTANCE-FELT.
  (R) is wrong-layer. Correct downstream carry:
    — voice-risk carry (jargon/abstraction ABSTRACTION-DOMINANT → /and-stitch Phase 8.5
       central-event-muffle, arm the check) per PROP-0019/CLAUDE.md Rule 17 precedent.
    — s04-dramatization concern → /and-write cold_read_risk_carry HARD watch: s04 upper-city-
       reach bone must be a concrete SVO (off-page landing is not a dramatized event bone).

rationale: |
  Sixth consecutive Class-B P in the c14-c19 stretch. All upstream informed gates passed.
  Uninformed cold-reader's complaints are structurally identical to the pre-authorized
  categories on every prior chapter. The "sameness" complaint is a feature of the thesis
  (contempt-without-refusal = register unchanged, continuation unchanged); de-abstracting
  at chunk layer would violate the endorsed substance contract. The two tractable items
  (jargon-opacity and s04 off-page landing) are correctly staged to /and-write + /and-stitch,
  not chunk revision. This is the penultimate chapter of the falling arc; the design-inherent
  CONTINUE=no is load-bearing context for the terminal recognition at c20.

trade-off: |
  Shipping the cold_read_risk_carry intact: if the downstream /and-write + /and-stitch chain
  fails to concretize s04 or fails to address jargon-opacity at the stitch layer, Phase 9
  will fire. The coupling rule then applies: Phase 9 FAIL on these complaint categories is
  pre-authorized as Class B and ships as SHIPPED-WITH-CAVEATS automatically if s04 carries
  through. The risk is recorded, not ignored.

downstream-arms:
  - target: /and-write b01c19
    arm: cold_read_risk_carry HARD watch — s04 upper-city-label-reach must be a concrete SVO
         bone on-page; inferred-off-page is FAULT at Phase 6 (EVENT-NOT-CONCRETE).
  - target: /and-stitch b01c19 Phase 8.5
    arm: voice-risk carry — jargon/abstraction ABSTRACTION-DOMINANT SIGNAL from chunk cold-read;
         arm central-event-muffle check per PROP-0019/CLAUDE.md Rule 17.
  - target: Phase 9 coupling
    arm: If Phase 9 FAIL fires and all complaint categories map to (a)+(b) (design-inherent
         thesis sameness + jargon) without new complaint classes, auto-disposition as
         SHIPPED-WITH-CAVEATS per the established coupling rule (DEC-0085/0090/0094/0096).
         s04-concrete failure would be a tractable new finding — not auto-dispositioned.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0100 | 2026-06-05 | FAST (process-critic)

mode: process-critic
trigger:
  reason: signal-accepted
  source_report: active-project/staff/auditor/write-b01c19-bone-gate.md
  source_verdict: |
    /and-write b01c19 Phase 6 bone-gate PASS — 0 HARD; 2 SIGNALs accepted-not-remediated:
    signal-001 ABSTRACTION-DOMINANT (s02 grounding 22.2%, below 25% soft floor; chapter-wide
    33% clean); signal-002 REGISTER-AS-MANNERISM ("opens" ×4 + "receives" ×4 chapter-wide).
    Context: sixth consecutive Class-B interior chapter (c14-c19); pl-2026-06-05-c19-001
    HARD watch (s04 concreteness) RESOLVED; pl-2026-06-05-c19-002 SOFT abstraction-muffle
    already armed for /and-stitch Phase 8.5.
  gate_path: .claude/commands/and-write.md#phase-6
verdict: OK

question: |
  (A) Does signal-001 ABSTRACTION-DOMINANT (s02 grounding 22.2%) fire-and-accept on this
  design-inherent recognition-naming scene warrant a process change — e.g., a scene-type
  carve-out for the accounting-reads-its-own-pattern class, or a structural fix to the
  bone-gate -> stitch-Phase-4 handoff for abstract design-inherent scenes?
  (B) Does signal-002 REGISTER-AS-MANNERISM ("opens" ×4 + "receives" ×4) fire-and-accept
  with distinct-SVOs-same-verb rationale warrant a process change — e.g., a gate criterion
  for accounting-register-refrain, or a screen-writer-brief constraint for verb diversity
  in accounting-intensive chapters?

decision: OK — no process change proposed on either signal. Gate and carry mechanism are
functioning as designed.

basis: |
  Step 1 (proposals log):
    Searched for open proposals targeting ABSTRACTION-DOMINANT fire-and-accept disposition,
    stitch-Phase-4/8.5 handoff structure, or REGISTER-AS-MANNERISM accept-and-carry. No
    open proposal covers either signal class with the same target.path + change_type as
    what either candidate would propose. No rejected proposal covers either target. No
    deferred proposal is past its defer_until. No merge required.

  Step 2 (question A — ABSTRACTION-DOMINANT s02 scene-type carve-out or handoff fix):
    DEC-0073 is the controlling prior ruling, confirmed by DEC-0097. Both establish:
    (1) The SIGNAL is load-bearing as the stitch-carry trigger. Removing or suppressing
        it via a carve-out would remove the trigger that arms /and-stitch Phase 4/8.5
        physical-materiality reinforcement — net-negative.
    (2) Accept-with-rationale IS the structural fix for design-inherent abstraction. It
        requires the rationale to license the abstract register explicitly. A gate carve-out
        would remove the rationale-logging discipline.
    (3) 3/3 SUBSTANCE-FELT confirms downstream delivery is landing on ABSTRACTION-DOMINANT
        accepted chapters. No evidence of stitch-layer failure on any prior accepted carry.
    (4) The chapter-wide count (33%) is clean. The s02 borderline (22.2%) is structural:
        the accounting-reads-its-own-pattern scene (CFR-1 recognition-naming) is inherently
        the most enumeration-dense, least place-situated scene in this chapter's design.
    The c19 instance is less severe than c18 (which had multi-signal ABSTRACTION-DOMINANT
    across two distinct scene types and a mover-level abstract-subject; DEC-0097, OK). A
    single-scene borderline 3pp below threshold does not warrant a merge into PROP-0030/0031:
    those proposals target chapter-wide apparatus-density accumulation across the collapse arc,
    not per-scene soft-floor proximity.

    Process discrimination: could a stricter gate have caught a process failure? No. The gate
    fired correctly, rationale logged, stitch-carry (pl-2026-06-05-c19-002) was already armed
    by the auditor. No process gap.

  Step 3 (question B — REGISTER-AS-MANNERISM accept-and-carry):
    DEC-0088 is the controlling prior ruling. It established:
    (1) Accept-and-flag-to-stitcher is architecturally correct. The stitcher Phase 3/8
        voice-embodiment + structural-variation directive is the only feasible resolution
        point for verb-frequency artifacts arising from SVO discipline constraints.
    (2) The SVO fence forces concrete transitive verbs. In an accounting-intensive chapter,
        "opens" and "receives" are narrow-corridor compliant verbs for their respective object
        classes — each instance in c19 is a structurally distinct concrete act (confirmed by
        the auditor's own assessment). The repetition is the accounting register, not a tic.
    (3) A screen-writer Phase 1 brief constraint would conflict with the SVO discipline fence
        and would be upstream of the only feasible resolution surface.
    (4) No stitch-layer failure has occurred on any prior REGISTER-AS-MANNERISM accepted carry.

    The c19 pattern is accounting-register-refrain, the same architectural root as c12 ("closes"
    x5, "reaches" x3 — accepted, DEC-0088's recurrence review) and c18 (signal-004 byte-identical
    intentional refrain, DEC-0097). The standard hold: the appropriate trigger for a process
    change is stitch-layer failure on a REGISTER-AS-MANNERISM accepted carry, not bone-gate
    accept-and-carry recurrence.

  Step 4 (recurrence count):
    ABSTRACTION-DOMINANT fire-and-accept: ≥10 occurrences across the book, all
    accepted-with-rationale; all delivered SUBSTANCE-FELT confirmed. REGISTER-AS-MANNERISM
    accept-and-carry: ≥9 occurrences. Both have high recurrence counts but zero failure class
    instances. Rule 11 promotion requires ≥3 recurrences as FAILURES, not as correct-gate-
    firings. DEC-0088/0091 established this discrimination explicitly.

  Step 5 (methodology):
    Both candidates are gate-functioning-correctly situations. A process change would add
    blast radius (modifying /and-write Phase 6 fires on every future chapter) for zero
    catch-quality improvement. Reversibility: carve-out is lower-reversibility. Cost:
    gate modification is M-cost, neither warranted. Blast radius: per-chapter SIGNAL carry
    is chapter-scoped; gate modification is pipeline-wide. OK in both dimensions.

rationale: |
  Both signals are correctly dispositioned. DEC-0073 (ABSTRACTION-DOMINANT) and DEC-0088
  (REGISTER-AS-MANNERISM) are the controlling rulings; c19 adds no evidence class that
  changes either. The sixth consecutive Class-B interior chapter context is the accumulation
  concern already tracked by PROP-0037 (DEC-0098, count 6); the /and-stitch Phase 9.5 dispatch
  for c19 will handle that increment. This bone-gate dispatch produces no new proposal.

trade-off: |
  Holding means no additional gate protection against a future chapter where accept-with-rationale
  discipline lapses. Mitigated by: the rationale-text requirement enforces explicit design-license
  per accepted SIGNAL; stitcher Phase 4/8 carries are armed per-chapter. A failure of auditor
  accept-with-rationale discipline is a gate-execution failure, not a gate-design gap.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0101 | 2026-06-05 | FAST (process-critic)

mode: process-critic
trigger:
  reason: failure (Phase 9 SHIPPED-WITH-CAVEATS, Class-B; CONTINUE=no on pre-disposed categories only)
  source_report: active-project/staff/reviews/coldread-b01c19-2026-06-05.md
  source_verdict: SHIPPED-WITH-CAVEATS (Class-B; auto-promoted via DEC-0099 coupling)
  gate_path: .claude/commands/and-stitch.md#phase-9
verdict: OK-MERGED-INTO PROP-0037 (recurrence_count confirmed at 7; evidence_ref pre-authored)

question: |
  Does the 6th consecutive Class-B chapter (c14-c19) warrant any new process change, or is it
  the expected shape of the falling-collapse stretch (c14-c20, with c20 as catastrophe-climax
  that breaks the interior-sameness)?

decision: OK-MERGED-INTO PROP-0037 — no new proposal warranted. PROP-0037 recurrence_count
already stamped at 7 (pre-authored in the proposals file with c19 evidence_ref). No amendment
required.

basis: |
  Step 1 (proposals log):
    PROP-0037 already contains the c19 evidence_ref and recurrence_count: 7 as pre-authored
    at lines 5087-5101 of staff/admin/process-proposals.md. The DEC-0101 entry was anticipated
    and pre-written into PROP-0037's evidence_refs block. No separate merge operation is needed;
    the record is already consistent.

  Step 2 (content vs. process discrimination):
    The Phase 9 cold-read CONTINUE=no rested exclusively on the two pre-disposed categories:
    (a) interior-sameness — "one filing action narrated five times" — pre-authorized as design-
        inherent thesis (continuation-unchanged = the horror; DEC-0099 complaint disposition (a)).
    (b) abstraction-density — "relentless abstraction" — pre-authorized as design-inherent for
        the falling interior collapse penultimate (DEC-0099 complaint disposition (b)).
    The one non-auto-dispositioned category (s04 label-reach-rendered-abstract / EVENT-NOT-
    CONCRETE) did NOT fire: the Daven severance LANDED shown-not-told. Phase 8.5 coherence
    confirmed central-event-muffle NOT-MATERIALIZED on both spine events.
    No new complaint class emerged. This is correct gate behavior on a chapter the substance
    contract intentionally made cold-reader-hostile.

  Step 3 (c14-c20 arc context):
    c19 is the penultimate chapter of the falling arc. c20 is the catastrophe-climax that
    structurally breaks the interior-sameness and delivers the terminal recognition. The 6th
    consecutive Class-B is the expected shape of this arc: each chapter in c14-c19 narrows the
    register until c20 cracks it. DEC-0098 (c18 climax, 5th consecutive) already held: the
    accumulation concern is correctly handled by /and-cohere as the accumulation handler and
    /and-review verdict b01 as the book-close enforcement surface. That ruling stands unchanged.

  Step 4 (PROP-0037 triage urgency):
    PROP-0037 remains open, untriaged. Triage urgency: HIGH before /and-review verdict b01.
    N=7 (6th consecutive in c14-c19 run; 7th data point overall across c10/c11/c12 +
    c14/c15/c16/c17/c18/c19). Gate design correct; enforcement timing is the open triage question.
    After c20 ships, /and-review verdict b01 is the natural triage moment.

  Step 5 (methodology):
    No new proposal: redundant proposal on a gate already correctly tracked. PROP-0037 is the
    correct and only outstanding action item. N=3 threshold calibration confirmed correct at N=7
    (DEC-0093 conclusion stands). No argument for threshold change.

rationale: |
  Pure recurrence-increment dispatch. The coupling rule (all Phase 9 CONTINUE=no categories
  pre-authorized -> auto-ship SHIPPED-WITH-CAVEATS) functioned correctly. s04 — the only
  tractable item — was delivered concretely, confirming the /and-write + /and-stitch chain
  addressed the HARD watch from DEC-0099. The 6th consecutive Class-B is structural cost of
  the deliberate falling-interior penultimate design, not a process failure.
  PROP-0037 recurrence_count is already 7 in the file. No file changes needed beyond this
  decisions log entry and the STM update.

trade-off: |
  No new proposal means PROP-0037 triage obligation continues to accumulate. Mitigated by:
  (a) PROP-0037 is complete and pre-populated with c19 evidence; (b) c20 + /and-review verdict
  b01 is the natural triage moment; (c) a new proposal would be redundant and add principal
  triage overhead with no additional information.

follows: DEC-0098 DEC-0100
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0102 | 2026-06-05 | FAST (user-proxy, RUNBOOK R1)

mode: user-proxy
context: |
  /and-substance chapter b01c20 Phase 5.5 chunk cold-read gate, Step 3 disposition.
  b01c20 is the terminal chapter of the one-book series: catastrophe-climax, falling arc,
  Dance ignites, Wren dies, Taylor expelled, ledger closes. CHUNK-CLASS-B: summary MAPS
  to goal; CONTINUE=no on two grounds: (1) prior-investment dependency (Wren + ledger
  conceit require 19 chapters the uninformed cold-reader lacks; Wren named only in scene 4);
  (2) interiority/abstraction-density ("four of five scenes are one woman reading a feed
  and declining to react, in dense abstract register"). Dramatist ACCEPTED structure.
  Audience 3/3 SUBSTANCE-FELT on all five scenes including worm-canon-pedant confirming
  affect-suppressed-not-absent. Causal ambiguity at expulsion trigger is deliberate
  thematic ambiguity. Established precedent: c14-c19 all shipped as Class-B cohort
  (DEC-0087/0090/0094/0096/0099), each SHIPPED-WITH-CAVEATS, each with depth-pass gated
  to BOOK-CLOSE.

question: |
  Which disposition for b01c20 Phase 5.5 CHUNK-CLASS-B: (R) Revise chunk, (P) Proceed with
  risk recorded [Class-B default], or (S) Substance-contract revision? If (P), which specific
  cold-read findings go into cold_read_risk_carry for /and-stitch Phase 9?

decision: P — Proceed with risk recorded. SHIPPED-WITH-RISK-RECORDED, depth-pass gated to
BOOK-CLOSE (not per-chapter). Same disposition as c14-c19.

cold_read_risk_carry (five items for /and-stitch Phase 9 to read as already-dispositioned):
  1. HARD-WATCH | CONTINUE=NO: prior-investment dependency. Cold-reader lacks the 19-chapter
     Wren investment + ledger conceit context by construction. Terminal chapter of a series
     cannot supply that in-chapter. Pre-authorized as design-inherent Class-B cost.
  2. HARD-WATCH | CONTINUE=NO: interiority/abstraction-density ("four of five scenes: one
     woman reading a feed and declining to react, in dense abstract register"). Same interior-
     accounting register as c14-c19; pre-authorized across that cohort. Stitch Phase 4
     voice-embodiment is the carry layer, not chunk revise.
  3. HARD-WATCH | Wren name-opacity (named only in scene 4; cold-reader has no context for
     who she is or why her death matters). Same character-opacity pattern as every c14-c19
     carry. Design-inherent: the insect-feed-mediated POV withholds affect because the
     apparatus withholds affect.
  4. SOFT | Escalation-in-kind flatness ("little escalation in kind" across five scenes).
     Stitch Phase 4 + Phase 9 voice-embodiment target: c20 must register as breaking the
     sameness of c14-c19, even within the affect-suppressed register. Not a chunk-design
     hole (dramatist ACCEPT + 3/3 SUBSTANCE-FELT confirm structure and affect delivered at
     substance layer); execution risk is stitch-layer. Phase 9 should enforce this scene-by-
     scene and verify c20 registers the break.
  5. DESIGN-INHERENT (no stitch fix required) | Expulsion-trigger ambiguity (discovered OR
     no longer needed). Deliberate thematic ambiguity — the apparatus's indifference to
     Taylor means even she gets no determinate cause. Pre-authorized. Phase 9 must NOT
     attempt to clarify; flagged to prevent false-FAIL on this axis.

basis: |
  LTM (DEC-0087 through DEC-0099): 6 consecutive Class-B P dispositions on c14-c19.
  All share the same two complaint categories: (a) prior-investment dependency and (b)
  interior-abstraction-density. c20 is structurally identical to this cohort with three
  additional factors that make Class-B even more expected:
  (a) Series-terminal chapter: prior-investment dependency is maximal by design.
  (b) Catastrophe-climax register-break is a stitch-layer execution challenge, not a
      chunk-design hole. Substance confirmed delivered (3/3 SUBSTANCE-FELT).
  (c) Dramatist ACCEPTED; audience confirmed Khepri-echo is shape-language-only.
  (R): chunk design is not broken. (S): contract produced 3/3 SUBSTANCE-FELT; redo is
  wrong layer. (P): exact precedent match for c14-c19.

trade-off: |
  Continues depth-pass debt accumulation. Mitigated by BOOK-CLOSE depth-pass obligation
  and /and-cohere accumulation handler (DEC-0087/0089/0093/0095). PROP-0037 triage: HIGH
  before /and-review verdict b01.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0103 | 2026-06-05 | FAST (process-critic)

mode: process-critic
trigger:
  reason: failure (SIGNAL-accepted-not-remediated)
  source_report: active-project/staff/auditor/write-b01c20-bone-gate.md
  source_verdict: "PASS — 0 HARD, 1 SIGNAL (signal-001, b01c20s05n06, political_register-world magnitude ~1.1 units over strict scene proportionality; ACCEPT-WITH-RATIONALE)"
  gate_path: .claude/commands/and-write.md#phase-6

question: |
  Does signal-001 ACCEPT-WITH-RATIONALE on b01c20s05n06 (dual-axis LOCK-confirmation bone:
  position-prot-collapse LOCK + political_register-world LOCK at the same physical exit act)
  reflect a recurring process gap worth a proposal? Or is it a structural artifact of
  terminal-chapter LOCK bones?

decision: OK — no process change proposed.

basis: |
  First-occurrence hold (non-catastrophic; methodology:3c). Content-vs-process
  discrimination: pure structural artifact, not a gate failure.

rationale: |
  The gate worked correctly: it detected the per-scene proportional skew (~1.1 units
  over strict proportionality), correctly classified it as SIGNAL not HARD, and the
  ACCEPT-WITH-RATIONALE disposition is substantively sound. Both axes (position-prot-collapse
  and political_register-world) lock at the same physical act — Taylor exits the south gate.
  The departure IS both LOCKs simultaneously. Reducing political_register-world magnitude on
  this bone would require a separate LOCK-confirmation bone, adding count without resolving
  any substance problem. The chapter-level aggregate is correct; the per-scene skew is an
  artifact of the 3-magnitude integer system combined with dual-axis LOCK coupling at a
  terminal exit bone. No prior proposal covers this class. N=1, non-catastrophic. The series
  is complete, so no future b01 chapter can produce recurrence evidence; any gate modification
  would be purely speculative. First-occurrence hold is the correct calibration.

trade-off: |
  If a future project uses LOCK bones at series-terminal scale, this class could recur and
  would be the first evidence for a gate carve-out proposal at that time.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0104 | 2026-06-06 | FAST (process-critic)

mode: process-critic
trigger:
  reason: failure (Phase 9 SHIPPED-WITH-CAVEATS; PASS-WITH-DEPTH-PASS-REQUIRED equivalent)
  source_report: active-project/staff/reviews/coldread-b01c20-2026-06-06.md
  source_verdict: SHIPPED-WITH-CAVEATS — completeness PASS; readability AIRLESS-leaning
    (pre-authorized Class-B DEC-0102); 7th consecutive Class-B (c14-c20); prose-rationale-mute=1
    (below soft-block); 2 non-spine NEEDS-BEAT signals.
  gate_path: .claude/commands/and-stitch.md#phase-9
verdict: OK-MERGED-INTO PROP-0037 (recurrence_count incremented 7->8; c20 evidence_ref appended)

question: |
  Does b01c20's 7th consecutive Class-B verdict (completing the c14-c20 cohort) warrant any
  new process proposal, or is everything already captured by PROP-0037 (depth-pass-before-
  book-close HARD-abort), DEC-0099 (cohort acceptance), and the PROP-0022 readability
  machinery?

decision: OK-MERGED-INTO PROP-0037 — no new proposal. c20 evidence_ref appended to
PROP-0037's evidence_refs block; recurrence_count incremented from 7 to 8.

basis: |
  Step 1 (proposals log):
    PROP-0037 is open, untriaged, with recurrence_count: 7. No other open or rejected
    proposal covers this failure class. The c19 evidence_ref was pre-authored; c20 was not
    (it was anticipated but the file was written before c20 shipped). Merge is the correct
    operation.

  Step 2 (content vs. process discrimination):
    All cold-reader negatives map without remainder to DEC-0102 cold_read_risk_carry:
    - "buried under abstraction / does not land emotionally / airless / tired turning page"
      carry item #2 (interiority/abstraction-density), pre-authorized.
    - "central mechanism took most of chapter to parse" carry item #1 (prior-investment
      dependency), pre-authorized.
    - "Wren's death implied, 80% sure" carry item #3 (Wren name-opacity-by-design; the
      80%-inference IS the intended effect; goal reads "not a named loss").
    No new complaint category emerged. PROP-0022 readability machinery fired correctly:
    grounding-ledger + voice-embodiment discipline + separated completeness/readability
    scoring all engaged. 2 non-spine NEEDS-BEAT signals are non-blocking. Prose-rationale-
    mute=1 is below the soft-block threshold. Pure recurrence-increment dispatch.

  Step 3 (c14-c20 arc closure):
    c20 is the SERIES-TERMINAL chapter. The c14-c20 cohort is now complete. The 7th
    consecutive Class-B is the expected terminus of the falling-interior-collapse arc:
    DEC-0098 (c18 climax) and DEC-0101 (c19 penultimate) both confirmed this structural
    logic. Cold-reader recovered the central event (Wren feed-blank), CONTINUE=yes,
    JEOPARDY=yes. Chapter executed within its envelope.

  Step 4 (PROP-0037 triage urgency — now CRITICAL):
    PROP-0037 is now CRITICAL urgency. The c14-c20 cohort it was written to address is
    complete. Depth-pass obligations (c14 mandatory, c18 mandatory, c20 mandatory as
    series-terminal) are due at book-close. /and-review verdict b01 is the next natural
    step and the designated triage moment. PROP-0037 cannot be deferred past book-close.

  Step 5 (methodology):
    No new proposal: redundant against PROP-0037. Recurrence increment is the correct
    and only action.

rationale: |
  The Phase 9 SHIPPED-WITH-CAVEATS on b01c20 is structurally identical to c14-c19: all
  complaints pre-authorized, no new complaint class, central event recovered, CONTINUE=yes.
  The process worked correctly at every checkpoint. The 7th consecutive Class-B closes
  the cohort rather than extending a concern. PROP-0037 is the mechanical enforcement
  surface for the obligation that flows from this cohort; it needs only a triage decision
  before /and-review verdict b01.

trade-off: |
  No new proposal means no new principal triage overhead. The only outstanding action is
  PROP-0037 triage, now CRITICAL-urgency with the cohort complete. Deferring past
  /and-review verdict b01 leaves the depth-pass obligation mechanically unenforced.

follows: DEC-0101 DEC-0102 DEC-0103
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0105 | 2026-06-06 | FAST (user-proxy)

question: Before /and-review verdict b01: (A) run book-close depth-pass revise loop on Class-B cohort (c14-c19 +/- /and-cohere), or (B) accept the pre-authorized Class-B cohort caveat per DEC-0099 and run /and-review verdict b01 now, surfacing the caveat in the report?
context: b01 COMPLETE (b01c20 SERIES-TERMINAL, shipped 2026-06-06). HARD parking-lot item pl-2026-06-05-c19-deptpass gates book-close on depth-pass resolution. DEC-0099 pre-authorized the Class-B disposition for c14-c19; DEC-0102 extended to c20. Option A (depth-pass before verdict) = ~50-90 dispatches for one chapter re-cascade; full c14-c19 cohort = 6x that. Option B = run /and-review verdict b01 now (read-only, non-blocking); orchestrator-critic judges the book with the caveat on record; depth-pass can follow if verdict FAILs on Class-B specifically.
options:
  A: book-close depth-pass revise loop before verdict (expensive, unsolicited, ~300-540 dispatches for cohort)
  B: accept pre-authorized caveat, run /and-review verdict b01 now, surface caveat in report

decision: B — accept the pre-authorized Class-B cohort caveat and run /and-review verdict b01 now.
basis: methodology:human-only (spend commitments past routine) blocks option A; goal:2 (cost discipline) strongly favors B; methodology:3a (reversibility) favors B (verdict is read-only; depth-pass remains available post-verdict if critic FAILs on this axis); DEC-0099 + prior cohort authorizations are the explicit pre-authorization.
rationale: Option A commits ~300-540 dispatches on a blind --from-signals sweep over 6 chapters the principal knowingly accepted with Class-B caveats. No new information has arrived since those acceptances to make the spend warranted. The verdict run IS the designated acceptance point — the parking lot item's own path (B) names it as such. If the orchestrator-critic PASS-WITH-NOTES or FAIL specifically calls out the Class-B stretch as degrading the book's verdict, THAT finding provides a targeted brief for depth-pass work; acting without it is uninformed expenditure. Option A's spend range (300-540 dispatches) qualifies as "meaningful slice of project budget on a single operation" and is explicitly human-only territory per methodology §spend-commitments-past-routine — absent an explicit principal request, admin cannot authorize it.
trade-off: Option A risks nothing quality-wise but costs enormous model spend and defers the verdict; option B runs the verdict on a book with a known quality caveat in the record. If the critic FAILs hard on the Class-B cohort, depth-pass work will still be needed but at least it will be scoped by specific findings rather than a blind cohort sweep.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0106 | 2026-06-06 | FAST (process-critic)

mode: process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md
  source_verdict: "PASS-WITH-NOTES — 4 open HARD caveats (Class-B depth-pass cohort c14/c15/c16/c19) accepted-as-caveat per DEC-0105; dominant note: 7-consecutive SHIPPED-WITH-CAVEATS (c14-c20)"
gate_path: .claude/commands/and-review.md#verdict
secondary_gate_paths: [.claude/commands/and-stitch.md#phase-9, .claude/commands/and-substance.md#phase-0]

question: Does the book-close outcome (7 consecutive SHIPPED-WITH-CAVEATS, c14-c20, pre-authorized chapter-by-chapter and accepted at book-close per DEC-0105) warrant a NEW process-change proposal, or does it merge into the existing PROP-0037? Judge whether the existing pre-authorization + book-close-acceptance machinery is the correct handling or whether the process itself has a gap.

context: /and-review verdict b01 returned PASS-WITH-NOTES (series-terminal, sole book). Substance trajectory and cost ledger delivered strongly (all 12 axes to designed close-states). Back-third Class-B cohort (c14-c20): 7 consecutive SHIPPED-WITH-CAVEATS on design-inherent grounds (interior-sameness + accounting-abstraction-density + event-poverty/jeopardy-offstage). Each chapter pre-authorized at its own DEC (DEC-0085 through DEC-0104). Cohort accepted at book-close per DEC-0105. Orchestrator-critic B2 finding explicitly named PROP-0037 as the correct gate for this class of behavior. An earlier 3-consecutive run (c10-c12) was interrupted by /and-cohere before c13 → clean PASS; the back-third run was not interrupted — it was knowingly accepted chapter by chapter. PROP-0037 is open (status: open, untriaged) with recurrence_count already updated to 8 (evidence_refs through DEC-0104 pre-authored, including the DEC-0106 reference pre-written into the block).

decision: OK-MERGED-INTO PROP-0037 — evidence already pre-authored into PROP-0037 at lines 5113-5122 of staff/admin/process-proposals.md; recurrence_count confirmed at 8; no new proposal needed.
basis: methodology:step-1-proposals-log-precedent (open proposal with same target + change_type)
rationale: |
  Step 1 (proposals log check): PROP-0037 is open (status: open, triaged_at: null), targets
  .claude/commands/and-substance.md Phase 0, change_type: modify, and was authored precisely
  to enforce a HARD-abort when consecutive_shipped_with_caveats >= 3 without a cohere
  acknowledgment stamp. The DEC-0106 evidence_ref was pre-authored into PROP-0037's
  evidence_refs block during c20 processing (DEC-0104), recurrence_count already reads 8.
  The proposals-log matching rule (open proposal with same target + change_type → merge,
  do not duplicate) applies without ambiguity. No new operation on PROP-0037 is required
  beyond confirming that the pre-authored entry is accurate.

  Step 2 (content vs. process discrimination): The 7-consecutive run is NOT a pure content
  failure that the process could not have caught. The orchestrator-critic's verdict
  (report line 168: "Process signal: the 7-consecutive Class-B chain is the empirical case
  PROP-0037 wants hard-gated") confirms this is exactly the class PROP-0037 targets. The
  process gap that let the run go uninterrupted is the absence of the PROP-0037 gate in
  /and-substance chapter Phase 0. The per-chapter DEC-acknowledgments (DEC-0085 through
  DEC-0104) are precisely the "path b: one-chapter-at-a-time acknowledgment" that
  PROP-0037's proposed_diff licenses — the book's behavior is confirmatory of the
  proposal's design, not contradictory to it.

  The pre-authorization + book-close-acceptance machinery (DEC chain + DEC-0105) worked
  correctly as the MANUAL bypass of what PROP-0037 would enforce mechanically. This is
  not a case where the process handled the situation correctly and no change is needed:
  the correct handling was manual and expensive (10 individual DEC entries, explicit
  chapter-by-chapter acknowledgment). PROP-0037's value is making that obligation surface
  automatically at the right phase. The book's outcome is strong evidence FOR triage,
  not evidence that the existing machinery is sufficient.

  No new proposal class: the evidence is purely confirmatory of the existing proposal.
  Triage urgency shifts from CRITICAL (pre-verdict) to GENERAL-PIPELINE-RULE — applies
  to any future book/project with a falling-arc back third. b01 is closed.
trade-off: A new proposal would duplicate PROP-0037 with no additional specificity. OK would
  misrepresent the finding — the process gap is real and evidenced by 8 data points across
  two independent runs. OK-MERGED correctly records the book-close confirmation without
  adding noise to the proposals log.

follows: DEC-0104 DEC-0105
stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0107 | 2026-06-06 | SLOW (user-proxy)

question: Principal said "Next chapter." Series is COMPLETE (20/20 chapters shipped, b01c20 SERIES-TERMINAL, /and-review verdict b01 PASS-WITH-NOTES today). No "next chapter" exists in the pipeline. What do they actually want, and is there a sensible default to execute?

context: Single-book series (book_count:1). All 20 chapters b01-c01 through b01-c20 on disk as terminal drafts. b01c20 is the designed series-terminal (Dance ignites, Flea Bottom burns, cost-bearer dies; d14 burn from series-trajectory.md). Chapter count 20 within declared 18-22 band. Book/series close-out verdict ran today: PASS-WITH-NOTES. Most recent commits: verdict + admin DEC-0105/0106 process-critic merges. "Next chapter" appears to be reflex/momentum at series close.

options:
  (a) Report completion, surface post-completion option menu — reversible, zero cost, pipeline-correct
  (b) Extend series to b02 — irreversible architectural + scope change; requires reopening series structure (book_count:1, series designed to terminate at burn); human-only strategic priority call
  (c) New project/series (/and-project) — irreversible new scope; human-only strategic priority
  (d) Depth-pass / revise on existing late chapters — reversible; several open SOFT parking-lot items for Class-B back-third c14-c20 cohort; could execute without human input, but "which chapter(s)" is still a choice

decision: Execute option (a) — report completion, surface the option menu. ESCALATE the directional question of what post-completion step the principal actually wants, because options (b)/(c)/(d-scoped) are each a strategic priority call that goals + methodology cannot resolve without the principal's direction. Do NOT auto-produce c21 (violates series-terminal design regardless of reflex phrasing).

basis: goal:1 (pipeline correctness — c21 violates series-terminal design contract) + goal:2 (cost discipline — executing an irreversible scope extension on ambiguous phrasing is maximum-cost error) + methodology:human-only (strategic priorities + spend commitments) + methodology:3a (reversibility — option (a) is fully reversible; all alternatives are not)

rationale: "Next chapter" against a series-terminal state has no pipeline-correct interpretation that produces a chapter. The default the caller proposed (report completion, do not auto-produce c21) is the only non-destructive answer and is clearly authorized by goal:1 + goal:2. The follow-on directional question (b02 vs. new project vs. cohere/postop vs. archive) is a strategic-priorities call per methodology §human-only — admin cannot rank those options without the principal's expressed intent. One human question costs less than any of the irreversible alternatives executed without authorization.

trade-off: One human round-trip. Accepted: cost of proceeding on any of (b)/(c)/(d) without direction would either extend the series beyond its designed terminus or commit spend on depth-passes the principal may not want now.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

## DEC-0109 | 2026-06-06 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: cohere-fail-but-design-accepted
  source_report: active-project/staff/reviews/cohere-b01-all-20260606T215813Z.md
  source_verdict: "FAIL-COHERE; load_bearing_fails=2 (naive-q6 dropped at triage as DEC-0105 design-accepted; dramatist-promise-payoff Sera-weight survives); iteration_count=1"
  gate_path: .claude/commands/and-cohere.md#phase-2
  secondary_gate_paths: [.claude/commands/and-review.md#cohere, .claude/commands/and-write.md#phase-6, .claude/commands/and-stitch.md#phase-9]

question: |
  Does the Sera Hightower payoff-weight drop — a whole-book-scope structural finding that
  survived ~20 per-chapter ship-gates + a book-level orchestrator verdict + three sub-section
  coheres and surfaced ONLY at the terminal full-book cohere — indicate a missing earlier
  checkpoint? Candidates: (a) a payoff-inventory gate at book-substance time; (b) mandatory
  full-book cohere before /and-review verdict rather than after; (c) working as intended —
  no process change needed.

context: |
  First-ever whole-book /and-cohere (b01 all, 20 chapters) on a COMPLETE, shipped,
  verdict-PASSED (PASS-WITH-NOTES; Class-B cohort accepted DEC-0105) book. Phase 3 triage
  dropped naive-q6 (apparatus-register cumulative load) as design-inherent + principal-accepted
  (DEC-0060/0062/0066/0072/0074/0085/0087/0090/0096/0099/0104/0105; OK-MERGED PROP-0030/0031).
  Surviving fresh finding: dramatist-promise-payoff — Sera Hightower payoff-weight drop.
  The finding: Sera is the cost-justification of the Otto arrangement (introduced c03),
  the reader never feels her weight, she never appears as a person, her threat is never staged,
  and the c20 decommission does not confirm she was protected. The moral engine's human face
  is a ledger entry. Secondary: Norren c17 false-attribution consequence deferred-then-unpaid.
  Audience fork PASSED (SUBSTANCE-FELT). This is distinct from the on-page non-naming design
  decision (pl-2026-05-28-002, verified c05 — Taylor never articulates the Sera-link by design).

decision: OK-MERGED-INTO PROP-0042 (recurrence_count 3 → 4; full-book-cohere evidence appended).
  No new proposal. Mandatory-before-verdict sequencing rejected on current evidence.
  /and-cohere is working as designed.

basis: |
  Step 1 (proposals log):
    PROP-0042 (status: open, triaged_at: null, recurrence_count: 3) targets
    .claude/commands/and-substance.md Phase 5 — Chunk-quality review (book level),
    change_type: add — PROTECT-TARGET-ABSENT-FROM-BOOK-PLAN SOFT flag at the dramatist
    review. PROP-0042 was authored at the c13-c15 cohere after two consecutive sub-section
    coheres flagged "Sera never appears on-page (c06-c15); the guarantee fires hollow; the
    protection object is a name in a prologue, never a felt person."
    The current finding is the third independent /and-review cohere instance flagging Sera
    absent-as-felt-person at a reader-reception/whole-book-payoff scope: the full-book cohere
    (all 20 chapters) confirms what the sub-section coheres caught and routed to
    /and-review verdict b01. Same target + change_type → merge, do not duplicate.

  Step 2 (content vs. process discrimination):
    Is this a process failure? Yes — structural: no gate at /and-substance book Phase 5 catches
    protect-target absent from the book plan at planning time. The full-book cohere correctly
    caught it retrospectively. The question is whether the class needed to reach terminal cohere,
    or whether an earlier gate could have surfaced it without becoming a different kind of gate.
    Answer: yes — /and-substance book Phase 5 dramatist review is the correct upstream catch
    point. PROP-0042 already proposes it. The new evidence confirms the gap is structural and
    project-independent (any book whose protect-target is planned absent will hit this).

    Is the surviving finding different in kind from what PROP-0042 already covers?
    No. PROP-0042 targets: "Sera never appears on-page as a participant in a scene; the
    cost-ledger guarantee fires hollow." The current finding adds: "the reader never feels her
    weight; the c20 decommission does not confirm protection." This is the same root — the
    protect-target is a ledger entry, not a felt person — at the whole-book scope. The proposed
    SOFT flag at /and-substance book Phase 5 would have surfaced this at planning time, forcing
    an authorial decision (hollow-by-design irony vs. on-page appearance). That is exactly the
    fix PROP-0042 proposes.

  Candidate (b) — mandatory full-book cohere before /and-review verdict:
    Rejected. Three reasons:
    (i) /and-cohere is an ITERATION loop: it fires /and-review cohere, builds a chapter-revise
        queue, and runs /and-write revise → bones → facets → stitch per chapter. Mandating it
        before verdict means mandating either: (a) a full iteration loop (re-cascade cost equal
        to producing several chapters) or (b) a read-only cohere pass (but that IS /and-review
        cohere, which already runs inside /and-review verdict as supplementary input per the
        /and-cohere relationship spec). A separate mandatory /and-cohere-converge-to-PASS gate
        before verdict would be L-cost architectural gate sequencing — human-only territory.
    (ii) The Sera finding is the kind of structural observation the analysis step is designed
         to process (DEC-0108). The finding is a reader-reception payoff gap — not a bone-level
         delivery failure and not fixable by the per-chapter re-cascade chain without an explicit
         authorial decision to add Sera on-page. Mandating /and-cohere convergence before verdict
         would require it to PASS on this finding, which it cannot (it cannot force Sera on-page
         without a substantive new authoring decision).
    (iii) The more upstream fix (PROP-0042) prevents the gap at planning time, which is strictly
          better than mandating a terminal diagnostic that cannot itself author the fix.

  Step 3 (is the per-chapter chain + sub-section cohere working as designed?):
    Yes. The per-chapter gates (Phase 9 cold-read, audience SUBSTANCE-FELT, bone-gate, facets
    Phase 5b) are not designed to catch whole-book payoff gaps. They gate per-chapter delivery.
    The sub-section coheres (c01-c07, c06-c12, c13-c15) correctly flagged Sera's absence but
    correctly noted it was "not chapter-fixable" and routed it to /and-review verdict b01.
    The full-book cohere confirms and concretizes the finding at whole-book scope. This is
    exactly what /and-cohere is designed to catch. The process worked correctly at every layer:
    per-chapter gates protect chapter delivery; sub-section coheres surface cross-chapter arcs;
    full-book cohere surfaces whole-book payoff gaps. The absence of a PLANNING-TIME gate is
    the only structural gap — and PROP-0042 already proposes to fill it.

  Step 4 (recurrence):
    The Sera-absent finding has now appeared in THREE independent /and-review cohere runs:
    (1) c06-c12 cohere → pl-2026-06-03-006 (first cohere flag)
    (2) c13-c15 cohere → PROP-0042 authored (recurrence_count: 3 at authoring)
    (3) b01-all cohere → this dispatch (recurrence_count: 4)
    This is the recurrence class PROP-0042 was designed to track. The full-book scope adds
    the terminal confirmation: the gap persisted to book-close despite three cohere runs.
    PROP-0042's proposed SOFT flag at /and-substance book Phase 5 would have surfaced this
    at book-authoring time, before any chapter was written.

  Step 5 (methodology):
    Reversibility: merging into PROP-0042 is reversible; a new proposal or a mandatory-before-
    verdict gate is larger-blast-radius and lower-reversibility.
    Cost: OK-MERGED is S-cost; mandatory-before-verdict sequencing is L-cost architectural.
    Blast radius: PROP-0042 adds one SOFT check at /and-substance book Phase 5 (one gate, one
    file); mandatory sequencing affects /and-review verdict + /and-cohere + their relationship.
    Convention: PROP-0042 already tracks this class with correct change_type and proposed_diff;
    merge is the mechanically required action.

rationale: |
  PROP-0042 is the correct and sufficient process response. The Sera payoff-weight finding at
  the full-book cohere is the third independent cohere-run confirming the same root gap: no gate
  at /and-substance book Phase 5 checks whether the book plan places a declared protect-target /
  cost-bearer on-page as a participant before the climax fires the structural guarantee. The
  full-book cohere performed exactly its designed function — it surfaced a whole-book payoff gap
  that no per-chapter gate and no sub-section cohere (which correctly knew it was "not chapter-
  fixable" and routed upstream) could see in full. This is not a sign the process failed; it is
  the sign it worked. The only structural failure the evidence supports is the planning-time gap
  PROP-0042 already targets. Mandatory-before-verdict sequencing would add large-blast-radius
  architectural overhead for a finding class that (a) the cohere correctly caught and (b) cannot
  be auto-fixed by the cohere loop without a new authoring decision.

trade-off: |
  Merging into PROP-0042 rather than proposing mandatory-before-verdict sequencing means the
  Sera gap remains catchable only at /and-substance book Phase 5 (at planning) or retrospectively
  at cohere. If the principal defers PROP-0042 triage, a future book can hit the same gap. The
  cost of deferral is one /and-cohere run surfacing the same finding — exactly what happened here.
  Mandatory-before-verdict would prevent the gap from surviving to book-close but at L-cost
  architectural complexity and the structural problem that /and-cohere cannot self-fix protect-
  target absences; it can only flag them for author action. PROP-0042 is the correct layer.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0110 | 2026-06-07 | SLOW (process-critic)

mode: process-critic
trigger:
  reason: principal-initiated-retro
  source_report: active-project/staff/auditor/cohere-b01-all-aggregate-audit.md
  source_verdict: retro (session retrospective on the /and-cohere b01 all cycle, 2026-06-06)
  gate_path: N/A (retro-initiated, not a gate-fired trigger)

question: |
  Formalize three process-change candidates from the /and-cohere b01 all session retro.
  All share root cause TRUST-WITHOUT-VERIFY. Author as separate proposals or merge/reject
  per the normal process-critic procedure.
  (A) Subagent output-persistence check — dispatcher never checks that a contracted emit
      artifact was actually written to disk; auditor returned findings in-message only,
      file absent until principal reconstructed it.
  (B) Post-async-agent shared-state read-back — admin DEC-0108 edit introduced a duplicate
      YAML result: key into cohere-state; dispatcher committed without reading the diff.
  (C) Pre-commit self-check on hand-authored aggregates — cohere aggregate shipped with
      citation error (fault-001), self-contradictory parking-lot item (fault-004), and
      systematic schema-id format drift (fault-003); all visible at authoring time.

decision: |
  PROCESS-CHANGE-PROPOSED PROP-0043 (Candidate A — subagent output-persistence check)
  PROCESS-CHANGE-PROPOSED PROP-0044 (Candidate B — post-async-agent shared-state read-back)
  PROCESS-CHANGE-PROPOSED PROP-0045 (Candidate C — pre-commit RECONCILE on hand-authored aggregates)

basis: |
  Step 1 (proposals log scan): Grepped for: output-persistence, existence-check, file emitter,
  subagent write, emit verify (Candidate A); shared-state diff, async agent edit, YAML duplicate
  (Candidate B); pre-commit, self-check, hand-authored, rollup audit, citation check, DEC citation
  (Candidate C). No open proposal with matching target.path + change_type for any of the three.
  No rejected proposal materially covering any of the three. No deferred proposal past its
  defer_until. All three warrant new entries.

  Step 2 (content vs. process): All three are process failures, not content failures:
    (A) No gate exists for the dispatcher→filesystem persistence check class. The auditor's
        in-message return was consumed as authoritative; the absent file would have been
        permanent data loss at the next context window boundary. Gate absence: change_type add.
        Target: CLAUDE.md §Rules (new Rule 19 — applies across all commands and dispatches).
    (B) No rule requires the dispatcher to read-back shared state after async agent mutation.
        The admin Edit/Write dispatch mutated cohere-state; the committed result had a duplicate
        YAML key. Gate absence: change_type add. Target: CLAUDE.md §Rules (new Rule 20 — applies
        wherever async agents have Edit/Write to shared state).
    (C) No pre-commit self-check sub-step exists at /and-cohere Phase 3/4 or /and-review verdict.
        Three simultaneously present defects (citation error, self-contradiction, schema-id drift)
        all visible at authoring time. Gate absence: change_type add. Target: and-cohere.md Phase
        3/4 (RECONCILE sub-step); secondary: and-review.md verdict subcommand.

  Step 3 (first-occurrence overrides): All three propose at N=1. Override rationale per standard:
    (A) Failure mode is silent data loss (permanent, no gate fires). Fix is trivially cheap (stat/ls).
        First-occurrence hold does not apply under catastrophic/silent-loss conditions.
    (B) Failure is silent (defect shipped committed). Fix is trivially cheap (read). Same rationale.
    (C) Three defects simultaneously in one artifact (structural pattern, not isolated slip).
        Fault-003 is systematic across 6 items (not a one-off). Fix is near-zero cost (read + assert).
        Principal cited this explicitly as a formalization candidate in the retro dispatch.

  Step 4 (methodology): All three: S or M cost, low blast radius, high reversibility, no
  methodology contradiction. Cost estimates: A=S (one CLAUDE.md rule), B=S (one CLAUDE.md rule),
  C=M (two command body edits: and-cohere.md + and-review.md). Ordered by value: A > B > C
  (A closes the most dangerous class; B closes the next; C closes the authoring-discipline gap).

rationale: |
  Three structurally distinct TRUST-WITHOUT-VERIFY instances, each with a precise gate absence
  and a cheap fix. Filing atomically as the dispatch requested: each covers a different
  execution layer (dispatcher→filesystem, dispatcher→shared-state, author→aggregate-content)
  and a different target file. No overlaps, no merges warranted. All three pass the standard
  first-occurrence-override criteria for non-catastrophic-but-cheap-to-close gaps.

trade-off: |
  All three at N=1: cost is three triage decisions. Benefit is closing three silent-loss classes
  before a second project begins. The alternative (hold for recurrence) risks a second instance
  of silent data loss (A), a second defective committed state (B), or a continued pattern of
  visible-at-authoring-time defects shipping to the auditor layer (C). All three costs exceed
  one triage decision per proposal.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0111 | 2026-06-07 | FAST (user-proxy)

question: STRUCT-025 — exposition facet (and-facets Phase 1 item 10) references `design/shoot-v2/rubric-exposition.md` which does not exist. Close via (a) author rubric-exposition.md, (b) de-reference it / point at the real authority sources already in use, or (c) park as known-debt to b02-activation?

context: The exposition facet is active and has shipped all 20 b01 chapters without rubric-exposition.md. Its actual operating authority is: schema §exposition + audience-gap test + context-ledger discipline + staff/exposition-author/glossed-terms.md. b01 is COMPLETE and SERIES-TERMINAL. No b02 is currently authorized. The rubric reference is a dangling pointer — a nonexistent file named in a command body — but has not caused a quality failure in 20 chapters. (a) is M-cost speculative authoring on a complete book with no b02 and no observed exposition-quality failure. (b) is S-cost, edits and-facets.md item 10 to name the real authority sources, removes the dead path, trivially reversible. (c) defers via parking-lot note.

options:
  (a) Author rubric-exposition.md now — M-cost speculative authoring
  (b) De-reference: edit and-facets.md item 10 to name the actual authority sources; remove dead rubric pointer — S-cost, reversible
  (c) Park as known-debt to b02-activation — do nothing now

decision: Option (b): de-reference. Edit and-facets.md Phase 1 item 10 to name the actual authority sources (schema §exposition + audience-gap test + context-ledger + glossed-terms.md). Remove the dead rubric-exposition.md pointer. Optionally add a one-line comment noting rubric-exposition.md is deferred to b02-activation if it would aid future readers.

basis: goal:2 (cost discipline) + goal:4 (lean architecture) + methodology:3a (reversibility) + methodology:3b (cost)

rationale: The dangling pointer is the actual defect: a command body citing a nonexistent file. Option (b) fixes that defect at S-cost by naming what the facet has actually operated on for 20 chapters — which is already the ground truth. Option (a) authors a rubric the facet has demonstrably not needed, on a series that is SERIES-TERMINAL with no authorized b02; this is the anti-pattern goal:4 warns against. Option (c) leaves the dead pointer in the command body, which means every future pipeline-review or STRUCT-scan continues to fire STRUCT-025. (b) closes the finding, matches reality, and is trivially reversible — if b02 is activated and the team wants a formal rubric, rubric-exposition.md can be authored then with 20 chapters of actual exposition behavior as evidence.

trade-off: A formal rubric-exposition.md would provide a more complete design surface and could catch future exposition-quality failures mechanically. That value is deferred to b02-activation at zero cost: the facet has shipped 20 chapters on its existing authority and the sources being named in the de-reference (schema + ledger + glossed-terms + audience-gap test) are functional.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0108 | 2026-06-06 | SLOW (user-proxy)

question: /and-cohere b01 all returned FAIL-COHERE. After Phase 3 triage, one actionable finding survives (Sera Hightower payoff-weight drop). Should I fire the Phase 4 revise queue on that one item — mutating finished, shipped drafts — or accept the book as cohesion-verified-with-documented-notes and fold the finding into the analysis the principal asked for next?

context: Book b01 is COMPLETE: 20 chapters shipped, b01c20 SERIES-TERMINAL, /and-review verdict b01 PASS-WITH-NOTES (today). Principal's standing instruction this session: "make sure everything is cohesive and then start doing an analysis." Cohere was the cohesion step; analysis is the declared next step. FAIL-COHERE verdict had 2 load-bearing fails: (1) naive-q6 apparatus-register cumulative load — DROPPED at triage as design-inherent Class-B, pre-adjudicated across DEC-0060/0062/0066/0072/0074/0085...0105, accepted at book-close; OK-MERGED into PROP-0030/0031. (2) dramatist-promise-payoff — surviving fresh item: Sera Hightower payoff-weight drop (court-tier protect-target introduced c03, never appears as a person, threat never staged, c20 decommission doesn't confirm she was protected). Distinct from on-page non-naming which is BY DESIGN per pl-2026-05-28-002. Secondary: Norren c17 false-attribution unpaid. Audience axis (worm-canon-pedant) PASSED: SUBSTANCE-FELT. Voice consistent, Earth-Bet fence clean. Firing Phase 4 would re-cascade c03 (+c20) through /and-write revise → /and-review bones → /and-facets → /and-stitch (~24+ dispatches), substantively changing shipped, accepted terminal drafts. Irreversible mutation of a finished artifact.

options:
  (a) DEFER / accept-with-notes: close cohere as FAIL-COHERE-but-design-accepted; record Sera finding as documented structural note (SOFT); proceed to the analysis the principal requested, incorporating cohere findings as material. No draft mutation.
  (b) FIRE Phase 4 on the Sera item: revise c03+c20 to add reader-facing Sera weight, re-cascade, re-run cohere.

decision: Option (a). Accept the book as cohesion-verified-with-documented-notes. Record the Sera payoff-weight finding as a SOFT parking-lot item. Proceed to the analysis the principal requested. Do NOT fire Phase 4.

basis: methodology:3a (reversibility) + methodology:3b (cost) + goal:2 (cost discipline) + goal:1 (pipeline correctness — cohere is a diagnostic, not a mandatory revise trigger when findings are structural/design-adjacent on a closed artifact)

rationale: Three independent lines converge on (a). First, reversibility: Phase 4 mutates terminal, shipped, PASS-WITH-NOTES-accepted drafts. The principal accepted book-close at DEC-0105 with pre-authorized Class-B caveats; re-opening that decision to act on a single surviving cohere finding is a meaningful irreversibility without a clear principal mandate. Second, the Sera finding is a reader-reception / whole-book payoff observation — exactly the kind of structural observation the analysis step is designed to surface and process. Surfacing it AS analysis is the correct routing. Third, the principal's declared next step is explicitly "analysis," not "revise." Firing Phase 4 delays the declared next step by ~24+ dispatches to mutate a closed artifact over a soft structural note that was not flagged at any upstream gate (bones-gate, Phase 9 cold-read, verdict pass). The cohere step has completed its mandate: it found what was there to find. The Sera weight drop is a genuine finding, but it is the analysis's job to evaluate whether it constitutes a design flaw the principal cares about enough to act on — admin cannot make that aesthetic judgment.

trade-off: The Sera payoff-weight gap stays in the draft as written. If the principal reads the analysis and decides the gap materially damages the book's moral engine, Phase 4 remains available on demand — the chain is re-runnable. The cost of accepting (a) is approximately zero; the cost of executing (b) without authorization is ~24+ dispatches plus irreversible draft mutation.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no

---

## DEC-0112 | 2026-06-07 | SLOW (user-proxy)

question: b01 manuscript consolidated into a single file. Principal says "begin revisions." What is the FIRST revision target + method? Standing evidence-backed queue: pl-2026-06-06-cohere-001 (c03 Sera establish-leg) + pl-2026-06-06-cohere-002 (c20 Sera confirm-leg), both SOFT, deferred by DEC-0108 when principal's next step was "analysis." "Begin revisions" appears to un-defer DEC-0108. Options: (a) fire Sera queue now via /and-cohere b01 cross-chapter loop; (b) fire Sera queue via two per-chapter re-cascades; (c) present manuscript + queue, confirm target before firing.

options:
  (a) Fire Sera queue now via /and-cohere b01 — cross-chapter loop, c03+c20, re-coheres to confirm; ~140-180 dispatches, irreversible draft mutation; pre-queued, evidence-backed
  (b) Fire Sera queue via two per-chapter re-cascades — c03 then c20; same irreversibility + cost; mechanism different from (a)
  (c) Present consolidated manuscript + standing queue; confirm principal's first target before spending — one conversation turn, fully reversible, preserves all options

decision: Option (c). Present the consolidated manuscript and the Sera queue to the principal. Confirm which revision target they want to lead with — the pre-queued Sera arc vs. their own reading-driven findings — before firing any re-cascade on shipped drafts.

basis: methodology:3a (reversibility) + methodology:3b (cost) + methodology §human-only (spend commitments past routine) + DEC-0108 (partial reversal — posture has shifted from "analysis" to "revisions," but the specific first target + mechanism is genuinely ambiguous)

rationale: "Begin revisions" reverses DEC-0108's analysis-posture deferral — that much is clear. What it does NOT specify: (1) whether the principal wants to lead with the Sera arc specifically vs. targets they identify from reading the consolidated manuscript, and (2) which mechanism (cohere loop vs. per-chapter re-cascade) they prefer for the Sera arc if it IS the first target. The instruction sequence was consolidate-first, which implies a reading intent — the principal may have their own manuscript-read findings that rank ahead of Sera in their judgment. Firing 140-180 dispatches irreversibly on shipped drafts without knowing which finding the principal wants addressed first violates methodology §human-only (spend commitments past routine) and methodology:3a (prefer reversible when uncertain). Option (c) costs one conversation turn and preserves full optionality. If the principal confirms "yes, Sera first," option (a) is the correct mechanism (cross-chapter Sera arc favors the cohere loop over two sequential per-chapter re-cascades). If the principal has read the manuscript and has different targets, the queue can be re-ordered accordingly.

trade-off: One human round-trip delayed at the start of revision work. Accepted: the cost of firing 140-180 dispatches in the wrong order on finished shipped drafts is materially higher than the cost of a single confirm. Sera remains fully available as the first target the moment the principal confirms it.

stm-written: yes
ltm-written: no
goals-update-proposed: no
methodology-update-proposed: no
