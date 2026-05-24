# Post-ship audit suite — b01c01

Generated: 2026-05-24
Context: `/and-stitch b01-c01` cycle-3-cap-burn-redo shipped to main (PR #57, merge commit c3e1d2d). Cold-read Phase 9 verdict PASS. 11 SIGNAL staging findings recorded non-blocking. This audit suite is the post-ship multi-angle assessment.

## Dispatch shape

- **Wave 1 (parallel)**: Fork 1 (auditor) + Fork 2 (general-purpose, graph-aware) + Fork 3 (general-purpose, graph-blind)
- **Wave 2 (parallel)**: Fork 4a/4b/4c (3 audience-persona reads — run `ls active-project/audience/` first to get the slugs) + Fork 5 (dramatist) + Fork 6 (general-purpose)

Total: 8 agent dispatches (Fork 4 fans out to 3 sub-forks).

## What each fork informs

| Fork | Output | Decision it informs |
|---|---|---|
| 1 | Pipeline-fidelity audit report | Whether to add new FAULT-* classes to the /and-stitch spec for c02+ |
| 2 | Substance-delivery diff | Whether axes_moved/held claims are honest; calibrates future substance audits |
| 3 | Naive pleasure cold-read | Reader-pleasure baseline; distinct from Phase 9 diagnostic |
| 4 (×3) | Per-audience-persona reads | Whether the audience cards predict shipped-prose reception |
| 5 | Forward-hook audit | Whether c01 set up c02-c18 properly; queues hook-debt before c02 starts |
| 6 | Orchestrator-critic post-ship verdict | Depth-of-quality call separate from Phase 9 gate |

Convergence rule: if multiple forks flag the same SIGNAL (e.g. the @19 watch-pass under-rendering), that's the strongest case for `/and-write b01c01 revise --from-signals` before c02. If they diverge, the staging signals stay deferred and c02 starts clean.

---

## Fork 1 — Pipeline-fidelity audit · `subagent_type: auditor`

```
You are the auditor running a post-merge pipeline-fidelity audit of /and-stitch b01-c01 cycle-3-cap-burn-redo. The chapter shipped to main with cold-read PASS. Verify the pipeline executed per spec — phases-vs-card, faults-vs-discipline, RECONCILE-vs-schema — and flag any phase that papered over a problem.

Inputs (READ-ONLY): active-project/staff/stitcher/render-log-b01-c01.md, active-project/draft/b01-c01.md, active-project/draft/b01-c01.annotated.md, active-project/staff/showrunner/memory.md (chapters[b01c01]), staff/stitcher/card.md, .claude/commands/and-stitch.md, schemas/stitch-render-log.schema.md, schemas/stitch-feedback.schema.md, schemas/stitch-profile.schema.md, staff/auditor/card.md.

Check: FAULT-PHASE-7-NO-SWEEP (verify 37 per-sentence Q-lines, one per post-Phase-6 sentence); FAULT-RECONCILE-IMBALANCE (verify both RECONCILE equalities balance against authored bones=27 and cite-index facets=49); FAULT-PHASE-1-CONSOLIDATED (verify Phase 1 dispatched 3 real Agent forks, not orchestrator inline-generation); FAULT-EXPOSITION-AUDIT-MISS and FAULT-DIALOGUE-AUDIT-MISS (verify Phase 7 carve-outs applied correctly); bone-faithfulness fence respected at every phase (dialogue/body/spatial/route/scene-prose/cognitive all =no); cap-burn @8 carried through correctly (logged as LEGACY-SILENT-SPEECH + BARE-SPEECH-BONE-CAP-BURN, NOT as FAULT-DIALOGUE-MISSING); Phase 8 scene-callout HARD-strip executed (clean draft contains no ## Scene N / [SCENE BREAK] / --- SCENE --- literals); Phase 9 cold-read agent was uninformed (read only the clean draft, did not open bones/facets/render-log); intermediate-draft pruning executed (no .phase-1/6/7.draft.md files remain); showrunner memory writeback scoped to stitcher metadata only.

Write your report to active-project/staff/auditor/stitch-pipeline-audit-b01c01-<timestamp>.md per schemas/audit-report.schema.md. Findings classified HARD / SOFT / SIGNAL. If everything passes, emit a PIPELINE-CLEAN verdict block and explicitly enumerate each check that passed — silent passes are not acceptable.

Return one paragraph: total checks run, HARD/SOFT/SIGNAL counts, overall verdict.
```

---

## Fork 2 — Substance-contract delivery audit · `subagent_type: general-purpose`

```
You are running the substance-contract delivery audit for b01c01 post-merge. Your question: does the prose deliver the substance contract authored upstream (axes_moved, axes_held, scene_conflict, dramatic_shape, goal), or does it merely look-like substance?

Read the prose (active-project/draft/b01-c01.md) against the contract (active-project/staff/showrunner/memory.md chapters[b01c01]). Use the annotated draft (active-project/draft/b01-c01.annotated.md) for sentence-IDs.

Diff: (1) substance_delta_measured.axes_moved (knowledge: 0.48) — does the prose actually move the knowledge axis 0.48 ranks? Cite prose evidence per scene (s01 0.19 / s02 0.20 / s03 0.09). (2) axes_held_verified [capability] — do each of the 9 held-capability bones show opposing-force-named-and-resisted in prose, or did some held bones land as bare assertion without the pressure? (3) dramatic_shape: hinge — does the prose read as hinge, or drift toward rising/falling/coda? (4) Per-scene scene_conflict.protagonist_force — does each of the 3 scenes deliver its protagonist_force on the page? (5) goal triplet (operating rule intact, the ward, the child who will pay) — landed?

Cite specific paragraphs + sentence numbers for each diff point. Bonus: the staging review (active-project/staff/reviews/staging-b01c01-20260524T1.md) flagged a systematic body-staging gap on held bones @9/@19/@24/@29 (5 of 11 SIGNAL findings). Does your independent read confirm or contradict that pattern?

Write to active-project/staff/reviews/substance-delivery-b01c01-<timestamp>.md. Verdict: DELIVERED / PARTIAL / SHORTFALL with per-dimension calls.
```

---

## Fork 3 — Naive pleasure cold-read · `subagent_type: general-purpose`

```
You are a first-time reader. Someone handed you a novel and you opened chapter 1. Read it once at reading pace. Read ONLY this file: active-project/draft/b01-c01.md. Do NOT open any other project file.

DIFFERENT from the Phase 9 diagnostic cold-read — your question here is purely: was it fun to read?

Answer six questions:
1. Did you enjoy reading it? (yes/no/mixed — one sentence why)
2. Where did your attention drift? (cite the paragraph and what you were skimming past)
3. Where did the prose grab you? (cite the paragraph and the specific image/phrase that hooked)
4. Did the voice feel like a person, or like prose-machinery? (one sentence — what tells you which)
5. Did the chapter end in a way that made you want more, or did you close the book? (one sentence why)
6. Genre / tone read — what kind of book is this, based on this chapter alone?

Be honest, not generous. If the prose was tedious in places, name the places. If a sentence read awkward, quote it.

Write to active-project/staff/reviews/pleasure-read-b01c01-<timestamp>.md. Under 400 words. After writing, return your six answers verbatim.
```

---

## Fork 4 — Audience-persona threshold read · `subagent_type: general-purpose` · dispatch ×3

Run `ls active-project/audience/` first to get the three slugs. Substitute `<PERSONA-SLUG>` per fork.

```
You are loading the audience persona card at active-project/audience/<PERSONA-SLUG>/card.md (+ ltm.md + stm.md if present). Read those three files first, then read the chapter at active-project/draft/b01-c01.md.

Read in-character — voice, taste-thresholds, attention pattern, all the things the card commits you to. This is NOT the /and-facets adversarial gate; this is post-ship reader-experience.

Answer:
1. Did you finish the chapter? (yes — read to last sentence; mixed — skipped or skimmed parts; no — closed early)
2. Where did your Threshold Discipline fire? (per your card's body section — cite the sentence and which threshold)
3. What did you like? (specific quote)
4. What did you dislike or distrust? (specific quote)
5. Would you read chapter 2? (yes/no + one sentence why, in your voice)
6. One sentence to a friend describing the chapter, in your persona's voice.

Write to active-project/staff/reviews/audience-<PERSONA-SLUG>-b01c01-<timestamp>.md. Return your six answers verbatim.
```

---

## Fork 5 — Forward-hook audit · `subagent_type: dramatist`

```
You are the dramatist running a forward-hook audit on b01c01. The series is an 18-chapter slow-prevention tragedy. Your question: did c01 plant the hooks the downstream chapters need?

Inputs (READ-ONLY): active-project/draft/b01-c01.md, active-project/staff/showrunner/memory.md (read chapters[b01c01] AND chapters[b01c02..b01c18], or at minimum c02-c05 if c06+ are still ~/stub), the book-level handoff_in/handoff_out, staff/dramatist/card.md.

For each downstream chapter that has an authored chunk (or scene chunks), check:
1. What does that downstream chapter assume about Wren? Did c01 plant the right Wren-state (observation-radius proven; flies-detail surfaced; ward-of-stitch-maker-household established)?
2. What does it assume about Taylor's operating-rule discipline? Did c01 plant the rule's intact-form load-bearingly enough to make a later break legible as break?
3. What does it assume about the watch / hook geography? Did c01 plant enough Flea Bottom spatial detail?
4. What does it assume about Coll? Coll's bare-speech-bone @8 was cap-burned to silence — does any downstream chapter assume the deleted line was rendered? If yes, that's a hook-debt the cap-burn deferred.
5. Are there hooks c01 planted that NO downstream chapter picks up? Wasted setup is a structural fault as much as missing setup is.

Write to active-project/staff/reviews/forward-hook-b01c01-<timestamp>.md. Per-downstream-chapter verdict: HOOK-LANDED / HOOK-WEAK / HOOK-MISSING / NO-DOWNSTREAM-DEMAND. Under 800 words.
```

---

## Fork 6 — Orchestrator-critic post-ship verdict · `subagent_type: general-purpose`

```
You are firing the orchestrator-critic against the b01c01 deliverable as it shipped. Load staff/orchestrator-critic/card.md — that card defines the standard a /and-review verdict <book> must satisfy to PASS. You are running the per-chapter analogue.

Inputs (READ-ONLY): staff/orchestrator-critic/card.md (your judging standard), active-project/draft/b01-c01.md (deliverable), active-project/staff/showrunner/memory.md chapters[b01c01] (substance contract + measured deltas), active-project/staff/reviews/coldread-b01c01-20260524T1.md (Phase 9 cold-read), active-project/staff/reviews/staging-b01c01-20260524T1.md (Phase 9 staging signals).

Apply the orchestrator-critic's rubric. The verdict at /and-facets cap-burn was NOT-SUCCESSFUL on the facets layer. Does the stitched prose layer raise it to SUCCESSFUL, hold it at NOT-SUCCESSFUL, or land somewhere in between?

Be explicit about which rubric criteria the prose satisfies and which it does not. Cite paragraphs / sentence-IDs.

Write to active-project/staff/reviews/orchestrator-critic-b01c01-<timestamp>.md. Verdict: SUCCESSFUL / NOT-SUCCESSFUL / SUCCESSFUL-WITH-RESERVATIONS. The verdict is advisory post-ship (the chapter has already passed Phase 9; this is the depth-of-quality call, not a re-gating).

Return: verdict + 3-sentence rationale.
```
