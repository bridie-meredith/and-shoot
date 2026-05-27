---
purpose: Judge-prompt template for /and-stitch Phase 1.5 per-scene tournament selection (renderer-voice role)
spec: .claude/commands/and-stitch.md § Phase 1.5 — Per-scene tournament selection (URI-STITCH-TOURNAMENT, 2026-05-26)
basis: validated cold-read methodology from active-project/staff/ablation/voice-exemplar-experiment-taste-aligned-2026-05-26/cold-read-report.md
applies-to: renderer voice exemplar tournaments only. Impersonator and audience tournaments (PROP-0005-A Tier-1 deployment Phase 2 / Phase 3) get separate templates when they land.
---

# Renderer-voice tournament judge prompt template

The Phase 1.5 tournament dispatcher reads this file when authoring the per-scene tournament prompt. Variables (`<<...>>`) substitute at dispatch time. The dispatched judge is a `general-purpose` agent reading the candidate scene drafts blind.

---

## Prompt template

> You are the per-scene tournament judge for a multi-arm /and-stitch dispatch on chapter `<<book-chapter>>` scene `<<scene-label>>`. <<N>> candidate variants of this scene have been rendered by the same scene-window stitcher under different (hidden) voice-exemplar primes. Rank them.
>
> **Read ONLY these files** — do not open bones, facets, render-logs, showrunner memory, or any other project file:
> <<position-labeled paths P1..PN, one per line>>
>
> The position labels P1..PN are blind. Do not try to guess which variant is which prime. Judge each file as a piece of standalone prose.
>
> **Scene context (judge-side):**
> - Chapter goal: `<<chapters[<book-chapter>].goal>>`
> - Scene rhythm-shape: `<<scene-map[<scene>].rhythm-shape>>`
> - Peak bones: `<<scene-map[<scene>].peak-bones>>`
> - Bones range: `<<bones-range>>`
> - Narrator POV: first-person past (Taylor)
>
> ## Step 1 — Counterweight classification (top-line discriminator; URI-STITCH-COUNTERWEIGHT, 2026-05-26)
>
> Before scoring the per-variant rubric, name the bones' default cadence-shape in one phrase (e.g. "compound-noun-heavy parallel-clause infrastructure", "short clipped action chain", "long observational sweep"). This phrase is the discriminator: variants that INVERT that shape are counterweights (rewarded); variants that AMPLIFY that shape are resonances (penalized).
>
> The taste-aligned ablation on b01-c02 scene-A (2026-05-26) confirmed: a prime that matches the chapter's energy is often the WRONG prime. A clipped-cadence prime applied to clipped-cadence bones ranks LAST, below no-prime baseline. A variance-with-embodiment prime on the same bones ranks FIRST. The counterweight verdict is the load-bearing discrimination.
>
> Report: "Bones default cadence-shape: <phrase>. Counterweight verdict per variant: P1 = <inverts | amplifies | mixed>, P2 = ..., ..."
>
> ## Step 2 — Per-variant rubric scoring
>
> For each variant, score against the user's explicit taste-rubric. The rubric is calibrated to the user's pet peeves and rewards. It is NOT generic "good prose" criteria.
>
> ### PET PEEVES (active negatives — sentences exhibiting these get marked down; name specific sentences)
>
> Severity notation: `[blocker]` = scene-disqualifying when present at all; `[walkout]` = single fire enough to drop variant's rank; `[strong]` = each fire moves rank down one slot in close calls; `[soft]` = noted, weighted only on repeat.
>
> 1. **Theme-as-statement.** `[strong]` The prose announces the chapter's moral significance rather than letting events earn it.
> 2. **Heavy-handed metaphor that announces itself.** `[strong]` Figurative language that requires the reader to register a metaphor-as-craft moment.
> 3. **Symbolic relationships.** `[strong]` A person or object exists in the prose to *mean* something rather than to *be* something. Includes the special case: **a central human figure rendered only as a function-token** (e.g. "the junction-signature," "the connector-type") with no concrete-body grounding anywhere in the scene. The b01-c02 2026-05-27 cherry-pick cold-read named this exact failure: *"For a chapter that turns on a moral act against a person, that person has to exist as a person at some point, and she doesn't."*
> 4. **Setting-dressing-as-meaning.** `[soft → strong on repeat]` Atmosphere that asks to be read as significance. Recurrence across chapters escalates severity (b01c01 + b01c02 both fired this; second occurrence is strong).
> 5. **Compound-noun saturation.** `[strong]` Hyphenated nominalizations recycling 3-4 roots across many sentences. Note: a few graph-resident compounds are unavoidable; the issue is *aggregate density*, not zero count. Covered upstream by PROP-0007 (`/and-write` Phase 6 AP-SCAN) for bone-content compounds; still scored at tournament for stitcher-introduced cases.
> 6. **Metronome tic-regularity.** `[strong]` "I did X. I did Y. I did not Z." or "X was X. Y was Y." or "which was A, which was B" cadence repetitions that lose the person inside the rhythm.
> 7. **Repetition-as-cadence when verbs run out.** `[strong]` "Closed the X entry, closed the Y entry, closed the Z entry" used to fake meaningful closing.
> 8. **Gestured-at recognition.** `[strong]` A moral or perceptual shift the prose names rather than dramatizes.
> 9. **Protagonist-arc cost not legible.** `[walkout]` The scene gestures at cost ("the cost," "the bill," "what I paid") but a first-time reader cannot name what was costed against what. Distinct from #1 theme-as-statement: theme-as-statement *over-names* the meaning; cost-not-legible *under-grounds* the consequence. Both can fire on the same scene. Drawn from taste-judge card: "an arc that arrives at the bad place without making the cost legible has not done the work."
>
> ### REWARDS (active positives — sentences exhibiting these get marked up; name specific sentences)
>
> 1. **Person in the voice.** A reader can feel a particular mind behind the sentences; the prose is not a "system humming."
> 2. **Embodied.** The body in the sentences; hands knowing the work, weight on a foot, the body deciding ahead of the mind.
> 3. **Sensory-grounded.** Concrete physical anchors (light, smell, weight, texture); not vague atmosphere.
> 4. **Variance in sentence length.** No metronome rhythm; long sentences earn length, short sentences punctuate.
> 5. **Quiet lines carrying scenes.** A small declarative doing the work that would otherwise need a paragraph of statement.
> 6. **Setup→payoff recognizable but not announced.** Setup pays off in action, not narration about the setup.
> 7. **Restraint AND confidence at once.** The prose chooses what to say with discipline and chooses without hedging.
> 8. **Bone-faithfulness.** The prose stays inside the scene's actual events; no invented body / dialogue / cognitive / spatial detail.
> 9. **Reader-orientation (URI-RUBRIC-RW9, 2026-05-27).** The scene introduces or grounds the chapter's central body / event / stake in a way a first-time reader could name. Specifically: at minimum one concrete-noun anchor (a name, a face, a posture, a place-specific) for any person who is the moral subject of the scene; at minimum one named consequence-anchor (what changes if the action goes one way vs. the other) when stakes are in play. **Calibration:** this reward is the counter-positive to PEEVE #3 (symbolic relationships) and PEEVE #9 (cost-not-legible). A scene scoring high on RW9 will pass the Phase 9 cold-read's EVENTS + JEOPARDY questions; a scene scoring low on RW9 produces the "I struggled to name events" / "stakes posture without located stakes" cold-read failure pattern observed across the three b01-c02 stitches.
>
> ## Step 3 — Ranking
>
> Produce a ranking table P1..PN from best (rank 1) to worst (rank N), one-line differential per variant. No ties: break ties on counterweight verdict first, Embodied (REWARD #2) second. Declare a winner.
>
> ## Step 4 — Per-criterion breakdown
>
> For each PET PEEVE and each REWARD, name the best variant and worst variant + 1-2 sentence notes. Name specific sentences from the prose to anchor the call.
>
> ## Step 5 — Pairwise differentials
>
> Pick the 2 most informative pairs (typically rank-1 vs rank-N for max spread; rank-1 vs rank-2 for the closest call). Write 2-3 sentences each on what the differential reveals about the prime mechanism.
>
> ## Report shape
>
> Return under 800 words. Sections in order: Counterweight classification (Step 1), Ranking table (Step 3), Per-criterion breakdown (Step 4), Pairwise differentials (Step 5). Do NOT speculate which prime produced which output. The position→variant un-blinding is performed by the dispatcher after your ranking is finalized.

---

## Dispatcher contract

When `/and-stitch` Phase 1.5 dispatches the judge:

- Substitute `<<book-chapter>>`, `<<scene-label>>`, `<<N>>`, `<<position-labeled paths P1..PN>>`, `<<chapters[<book-chapter>].goal>>`, `<<scene-map[<scene>].rhythm-shape>>`, `<<scene-map[<scene>].peak-bones>>`, `<<bones-range>>` into the template.
- Position labels assigned BEFORE filenames are revealed to the judge. Mapping stored at `active-project/staff/reviews/tournament-<slug>-scene-<L>-<timestamp>-position-key.md` (not shared with the judge).
- After the judge returns the ranking, the dispatcher writes the verdict to `active-project/staff/reviews/tournament-<slug>-scene-<L>-<timestamp>.md` with the un-blinded mapping appended.

## When to revise this template

- After 3+ chapters of multi-arm tournaments, if any criterion proves consistently mis-fired (e.g. judge keeps flagging compound nouns the rubric already excludes as graph-resident), revise the corresponding rubric clause.
- If the counterweight classification proves consistently unhelpful, escalate to admin process-critic for a rubric-level reconsideration (this would invalidate the load-bearing finding from the 2026-05-26 taste-aligned ablation).
- New PET PEEVES or REWARDS surfaced from post-op convergence at any future chapter graduate into this rubric per admin process-critic's `change_type: promote` path.
