---
purpose: Judge-prompt template for /and-stitch Phase 1.5 Step 2 cherry-pick composition
spec: .claude/commands/and-stitch.md § Phase 1.5 Step 2 — Per-scene cherry-pick composition
basis: 2026-05-27 b01-c02 cherry-pick experiment (active-project/staff/reviews/coldread-b01-c02-2026-05-26-cherry-pick.md)
applies-to: renderer-voice tournaments only. Cherry-pick collapses to no-op at N=1 (no dispatch).
---

# Cherry-pick composer judge prompt template

The Phase 1.5 Step 2 dispatcher reads this file when authoring the per-scene cherry-pick composition prompt. Variables (`<<...>>`) substitute at dispatch time. The dispatched judge is a `general-purpose` agent.

---

## Prompt template

> You are the per-scene cherry-pick composer for a multi-arm /and-stitch dispatch on chapter `<<book-chapter>>` scene `<<scene-label>>`. Step 1 of Phase 1.5 has already produced a per-scene blind ranking of `<<N>>` candidate variants. Your job is to compose a paragraph-level cherry-pick aggregate — paragraph by paragraph, identify the variant whose paragraph best satisfies the taste-aligned rubric, and assemble the result.
>
> **Inputs you MAY read:**
> - Per-scene tournament verdict: `<<tournament-verdict-path>>` — Step 1 rank order, per-criterion table, counterweight verdict, un-blinded arm→position mapping
> - All N candidate scene drafts: `<<arm-paths-list>>`
> - The scene's bones (verbatim): `<<bones-scene-extract>>`
> - The scene-map row for this scene: rhythm-shape `<<rhythm-shape>>`; peak-bones `<<peak-bones>>`; fusion-eligible-runs `<<fusion-runs>>`; protected-patterns `<<protected-patterns>>`
>
> **Inputs you MUST NOT read:** facets, full bones file beyond this scene, render-logs, showrunner memory, prior chapters' drafts, any other project file.
>
> ## Step 1 — Establish the paragraph correspondence
>
> The per-scene tournament winner (rank 1) is the structural base. Walk through the winner paragraph by paragraph. For each paragraph in the winner, identify the corresponding paragraph(s) in each other arm by bone-range (which bones the paragraph renders). Record the correspondence in a table:
>
> | Para # in winner | Bone-range | Winner text (first/last words) | Arm-2 corresponding para | Arm-3 corresponding para | ... |
>
> "Corresponding" means renders the SAME bone-range. If arm-A renders a bone-range in one paragraph and arm-B splits it across two paragraphs (or fuses with adjacent bones), record the structural mismatch but DO NOT propose substitution — the bone-faithfulness fence requires same-bone-range substitution.
>
> ## Step 2 — Per-paragraph cherry-pick decision
>
> For each paragraph row in the table, decide:
>
> - **KEEP-WINNER** — the winner's paragraph satisfies the rubric better than any other arm's corresponding paragraph (or there is no same-bone-range correspondence in any other arm).
> - **SUBSTITUTE arm-<N> para <#>** — the non-winner arm's paragraph satisfies the rubric better. Cite the specific PEEVE that the winner fires and the non-winner avoids, OR the specific REWARD that the non-winner hits and the winner doesn't, with quoted sentences from both as evidence.
>
> Rubric is the same as Step 1's renderer-voice rubric (`staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md` PET PEEVES + REWARDS, including the URI-RUBRIC-RW9 reader-orientation reward). A substitution is justified only when the per-paragraph rubric delta is concrete and citable — not on overall feel.
>
> **Bone-faithfulness fence (hard).** A substitution is only permitted when the non-winner paragraph renders the SAME bone-range as the winner's paragraph. If the bone-ranges differ even by one bone (e.g. winner para covers @17-@19; non-winner para covers @17-@20), DO NOT substitute. Emit `FAULT-CHERRY-PICK-BONE-MISMATCH para-<#>` in the report and KEEP-WINNER.
>
> **No invention.** You compose from the N rendered candidate paragraphs only. No rewriting, no blending mid-paragraph, no smoothing the seam.
>
> ## Step 3 — Tonal-seam awareness
>
> For each SUBSTITUTE decision, flag the tonal-seam risk:
> - `none` — the substituted paragraph's voice is indistinguishable from the surrounding winner paragraphs at the seam (no reader would notice the cross-arm switch)
> - `low` — the substituted paragraph reads in a slightly different register but the transition is smooth (a reader sensitive to voice might notice but it doesn't break flow)
> - `flag` — the substituted paragraph introduces a register change a reader will perceive as a seam. Surface this for Phase 9 cold-read attention; do not auto-block the substitution.
>
> ## Step 4 — Assemble the cherry-pick scene draft
>
> Emit the assembled scene as continuous prose — winner paragraphs except where SUBSTITUTE was chosen, in which case the non-winner paragraph appears in place verbatim. Preserve paragraph breaks; do not add transitions; do not edit at the sentence level.
>
> ## Output format
>
> Write your report to `<<scorecard-path>>` (provided by dispatcher) with the following structure:
>
> ```
> # Cherry-pick composition — <<book-chapter>> scene-<<scene-label>>
>
> ## Paragraph correspondence table
> | Para # | Bone-range | Winner first words | Arm-2 corr. | Arm-3 corr. | ... |
>
> ## Per-paragraph decisions
> Para 1 (bones @<X>-<Y>): KEEP-WINNER | SUBSTITUTE arm-<N> para <#>
>   - rationale: <peeve fired by winner | reward hit by non-winner>
>   - evidence: "<winner quote>" vs "<non-winner quote>"
>   - tonal-seam: none | low | flag (only on SUBSTITUTE)
> Para 2: ...
> ...
>
> ## Substitution summary
> - total substitutions: <K>
> - sources: arm-2: <P>, arm-3: <Q>, ...
> - tonal-seam-risk aggregate: <none | low | flag>
> - ceiling-collapse: <true if K=0, else false>
> - bone-mismatch flags: <count + para list>
>
> ## Assembled cherry-pick scene
> <continuous prose; paragraph-broken; verbatim from source arms; no editorial smoothing>
> ```
>
> Then the dispatcher copies the "Assembled cherry-pick scene" block into `active-project/draft/<book>-<chapter>.scene-<L>.draft.md` (canonical scene draft) and retains the pure-winner as `<book>-<chapter>.scene-<L>.winner.draft.md`.
>
> Keep your report under 1200 words. The composition is the deliverable; per-paragraph rationale lines should be tight (one sentence each).

---

## Dispatcher contract

When `/and-stitch` Phase 1.5 Step 2 dispatches the composer:

- Substitute all `<<...>>` variables from the resolved chapter / scene / arm paths.
- Position labels from Step 1 are un-blinded for this composer (it needs to know which arm is which to track sources). The composer's report cites arm-N directly.
- Dispatcher writes the assembled cherry-pick to `active-project/draft/<book>-<chapter>.scene-<L>.draft.md`; the pure-winner is renamed to `<book>-<chapter>.scene-<L>.winner.draft.md`.
- The composer's report is persisted to `active-project/staff/reviews/cherry-pick-<book>-<chapter>-scene-<L>-<timestamp>.md`.
- If `ceiling-collapse: true` (K=0 substitutions), the canonical scene draft and the pure-winner are identical files; render-log records the ceiling-collapse for tuning evidence.

## When to revise this template

- After 3+ chapters of cherry-pick-default runs, if substitutions consistently come from ONE specific rubric criterion (e.g. always RW2 Embodied), that signal feeds back to the renderer-voice rubric — the criterion is doing real work and might warrant promotion to a primary discriminator.
- If `tonal-seam-risk: flag` substitutions consistently produce Phase 9 cold-read FAIL, tighten the tonal-seam fence here (require `none` or `low` only).
- If `ceiling-collapse: true` fires on >50% of scenes across multiple chapters, the multi-arm setup isn't differentiating arms enough — feeds back to exemplar-selection at Phase 0 step 4a.
