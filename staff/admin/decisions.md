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
