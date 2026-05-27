---
purpose: Judge-prompt template for /and-stitch Phase 1.5 Step 3 cherry-pick scoring
spec: .claude/commands/and-stitch.md § Phase 1.5 Step 3 — Per-scene cherry-pick scoring
schema: schemas/tournament-scorecard.schema.md
basis: 2026-05-27 b01-c02 cherry-pick experiment pet-peeve audit; taste-judge card pet peeves; renderer-voice rubric
applies-to: renderer-voice tournaments. Scores the assembled cherry-pick scene draft (post-Step-2).
---

# Cherry-pick scorer judge prompt template

The Phase 1.5 Step 3 dispatcher reads this file when authoring the per-scene scoring prompt. Variables (`<<...>>`) substitute at dispatch time. The dispatched judge is a `general-purpose` agent.

The scorer's deliverable is a structured scorecard — the accumulating tuning signal across chapters, used by admin process-critic to identify rubric mis-calibrations and feed-back paths.

---

## Prompt template

> You are the per-scene cherry-pick scorer for `/and-stitch` chapter `<<book-chapter>>` scene `<<scene-label>>`. The cherry-pick composer (Step 2) has assembled the canonical scene draft from per-paragraph winners across N candidate arms. Your job is to score the assembled draft against the user's taste-aligned rubric and emit a structured scorecard.
>
> **Read ONLY these files:**
> - The assembled cherry-pick scene draft: `<<scene-draft-path>>`
> - The scene's bones (verbatim): `<<bones-scene-extract>>` — only to check bone-faithfulness, not to second-guess composition
>
> Do NOT read facets, render-logs, showrunner memory, prior chapters, or any other project file. The score is on the prose as it stands.
>
> ## Step 1 — Per-PEEVE scan
>
> For each PET PEEVE in the renderer-voice rubric, walk the scene paragraph by paragraph and count fires. Record:
>
> - fire count (integer)
> - severity per the rubric tag (blocker / walkout / strong / soft)
> - anchor sentences (verbatim quotes; up to 2 per peeve)
>
> The PEEVES (from `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md`):
>
> 1. Theme-as-statement `[strong]`
> 2. Heavy-handed metaphor that announces itself `[strong]`
> 3. Symbolic relationships `[strong]` — includes function-token-only renderings of central human figures
> 4. Setting-dressing-as-meaning `[soft → strong on repeat]`
> 5. Compound-noun saturation `[strong]`
> 6. Metronome tic-regularity `[strong]`
> 7. Repetition-as-cadence when verbs run out `[strong]`
> 8. Gestured-at recognition `[strong]`
> 9. Protagonist-arc cost not legible `[walkout]`
>
> ## Step 2 — Per-REWARD scan
>
> For each REWARD, count hits and cite anchor sentences. The REWARDS:
>
> 1. Person in the voice
> 2. Embodied
> 3. Sensory-grounded
> 4. Variance in sentence length
> 5. Quiet lines carrying scenes
> 6. Setup→payoff recognizable but not announced
> 7. Restraint AND confidence at once
> 8. Bone-faithfulness
> 9. Reader-orientation (URI-RUBRIC-RW9)
>
> ## Step 3 — Voice-consistency check (tonal-seam landing)
>
> The cherry-pick was composed from multiple arms. Read the assembled scene as a continuous unit and judge whether the cross-arm composition reads as one voice or two. Three-level verdict:
>
> - `seamless` — no perceptible voice shift; reader experiences single narrator throughout
> - `minor-seam` — one or two transitions where the register shifts but the reading experience holds
> - `flag-seam` — perceptible voice break at one or more substitutions; reads as composite
>
> Name the specific paragraph transition(s) if seam is detected, by paragraph number.
>
> ## Step 4 — Scene-level numeric score
>
> Compute:
>
> ```
> peeve_weight_sum  = sum over PEEVES of (fire_count × severity_weight)
> reward_score      = sum over REWARDS of hit_count
> scene_score       = reward_score − peeve_weight_sum
> ```
>
> Where severity weights are: blocker=10, walkout=5, strong=2, soft=1.
>
> Report the three values. The absolute score number is less meaningful than its delta across scenes / chapters — the tuning ledger uses these numbers to detect rubric drift and arm-differentiation patterns.
>
> ## Step 5 — Output the scorecard
>
> Write your report to `<<scorecard-output-path>>` following the schema at `schemas/tournament-scorecard.schema.md`. The minimum required block:
>
> ```yaml
> ---
> schema: schemas/tournament-scorecard.schema.md
> book: <book-slug>
> chapter: <chapter-slug>
> scene: <scene-label>
> scored_at: <iso-timestamp>
> scorer_dispatch: phase-1.5-step-3-cherry-pick-scorer
> source_draft_path: <<scene-draft-path>>
> ---
>
> # Cherry-pick scorecard — <book>-<chapter> scene-<scene-label>
>
> ## Scene-level score
> reward_score: <N>
> peeve_weight_sum: <N>
> scene_score: <N>
> voice_consistency: seamless | minor-seam | flag-seam
>
> ## PET PEEVE fires
> | # | Peeve | Severity | Fire count | Anchor sentences |
> |---|-------|----------|------------|------------------|
> | 1 | theme-as-statement | strong | <N> | "<quote>" / "<quote>" |
> | 2 | heavy-handed-metaphor | strong | <N> | ... |
> ... (all 9, including 0-count rows)
>
> ## REWARD hits
> | # | Reward | Hit count | Anchor sentences |
> |---|--------|-----------|------------------|
> | 1 | person-in-voice | <N> | "<quote>" |
> | 2 | embodied | <N> | ... |
> ... (all 9, including 0-count rows)
>
> ## Voice-consistency notes
> <2-4 sentences naming any seam locations + the reading-experience effect>
>
> ## Tuning signal flags (for admin process-critic)
> - peeves-firing-on-every-arm: <list any peeve that the per-scene tournament verdicts noted ALL arms firing — these indicate the rubric criterion is too broad or the bones authoring is producing the failure for every prime>
> - rewards-no-arm-hit: <list any reward that scored 0 across this scorecard despite the scene having room — these indicate the rubric is measuring something the rendering cannot produce>
> - cherry-pick-source-concentration: <if any substitutions in Step 2, which rubric dimension drove most of them — used to detect that cherry-pick lift consistently comes from one criterion>
> ```
>
> Keep the report under 1500 words. The structured fields above are the load-bearing output; prose commentary should be tight.

---

## Dispatcher contract

When `/and-stitch` Phase 1.5 Step 3 dispatches the scorer:

- Substitute `<<book-chapter>>`, `<<scene-label>>`, `<<scene-draft-path>>`, `<<bones-scene-extract>>`, `<<scorecard-output-path>>`.
- Scorer runs after Step 2 composition completes; reads only the assembled cherry-pick draft + the scene bones.
- Dispatcher writes the scorecard to `active-project/staff/reviews/scorecard-<book>-<chapter>-scene-<L>-<timestamp>.md`.
- Dispatcher appends a one-line summary row to the chapter-aggregate ledger at `active-project/staff/showrunner/tournament-scorecards.md` (append-only; see `design/tournament-tuning.md`).

## When to revise this template

- After 5+ chapters of scorecards, if `peeves-firing-on-every-arm` consistently names the same peeve, the rubric criterion needs re-calibration — escalate to admin process-critic with a `change_type: modify` proposal against the renderer-voice rubric.
- After 5+ chapters, if `rewards-no-arm-hit` consistently names the same reward, the rubric is measuring something the rendering layer cannot produce — escalate to admin with a `change_type: modify` (lower the reward bar) or `change_type: delete` (retire the reward) proposal.
- If voice-consistency `flag-seam` consistently correlates with Phase 9 cold-read FAIL, tighten the cherry-pick composer's tonal-seam fence (require `none` or `low` only at composition time).
