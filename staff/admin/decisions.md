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
