---
phase: D — critic-tuning carry-back
date: 2026-05-10
run: and-season-tuning-r2
input: B-r2-seams.md (4 SLEEPERs, all 4 hypotheses confirmed) + C-auditor-self-review.md (3 ranked refinements; 6 of 11 classes need no change)
status: closed
---

# Phase D — Critic-Tuning Carry-Back

R2 produced two reviewer-side findings worth landing as V2 candidates:

1. The audience personas need a **Threshold Discipline** section in the `class: persona` schema so the tightened attack standard is durably codified rather than dispatched ad-hoc per round.
2. The auditor's 11-class taxonomy needs **3 targeted sub-classes** (1 in CURVE-SHAPE, 2 in CONSTRAINT, 1 in AP-SCAN). The other 7 classes are correctly calibrated.

Plus one process finding worth memorializing:

3. The **meta-tuning loop pattern** R2 used (tightened-audience attack against R1 output → auditor self-review → carry-back synthesis) is reusable for future tuning projects. Worth documenting as a standalone process so the next tuning project doesn't have to invent it.

---

## Carry-back item URI-017 — Persona-card "Threshold Discipline" section

**Category:** Schema (per-persona card sections).

**Source:** R2 A-tightening-brief + B-r2-seams Block 2 (R1 worm-canon-pedant ACCEPT on U1, U2 was identifiable as formulaic deference; R2 worm flipped to REJECT under tightened brief on the same units without changes to the corpus).

**The gap:** The `class: persona` audience role currently has three sections (Voice / Hot Buttons / Fatigue Signals). None of them addresses what the persona does when a rubric threshold is technically satisfied but the persona's taste says the unit should fail. R1 worm tolerated U1 (escalation curve) and U2 (e01 OPEN-ENGAGES) under "the worm reader tolerates slow open construction when the latent-cost register is honest" — that toleration was a threshold accommodation, not a taste verdict. The tightened brief made this distinction explicit and the persona behaved differently. Codify the discipline so it doesn't depend on per-round briefing.

**Candidate V2 schema addition:**

> Add to `class: persona` audience role body sections:
>
> **Threshold Discipline** — what the persona does when rubric thresholds permit a defense the persona's taste rejects. Three explicit rules:
> - Rubric arithmetic is advisory; taste is authoritative. If the count says "within tolerance" but the bones read wrong, the bones read wrong.
> - Season-plan / tone-law / project-condition citations cover what the rubric explicitly licenses, NOT what the persona's lens registers as a fault. A defense that cites a tone-law clause to defeat a structural seam the persona's taste finds is rejected.
> - Carry-forwards are open until adjudicated clean. "Previously identified / known residual" parking does not close a seam.

**Effect on existing audience cards:** the three active cards (`dark-fantasy-reader`, `pulp-enthusiast`, `worm-canon-pedant`) gain the new section. Per-persona content of the section is small (the three rules apply uniformly across personas).

**Effect on future tuning runs:** the "tightened brief" no longer needs to be reissued per round; it's the default. R1's formulaic-scoring path is the special case (rubric-arithmetic-permitted defenses), not the tightened-brief path. This inverts the burden.

**Cost:** small. Schema edit + per-card update for 3 audience cards (and any future audience cards).

---

## Carry-back item URI-018 — Auditor class CURVE-SHAPE-EPISODE-INTERIOR

**Category:** Auditor class refinement (URI-006 progress).

**Source:** R2 C-auditor-self-review Refinement 1; SLEEPER-1 (U5 dark-fantasy SHAPE-COHERENT failure).

**The gap:** R1's CURVE-SHAPE class ran at season scope only — it produced signal-010 (peak position at 50% of aggregate, borderline back-half) and signal-011 (denouement 43% of aggregate, no V1 maximum). It did NOT run at episode scope. SLEEPER-1's 89-bone post-IGNITION SHAPE-COHERENT failure was an episode-interior question that the season-scope CURVE-SHAPE class had no mechanic for.

**Candidate V2 sub-class:**

> **CURVE-SHAPE-EPISODE-INTERIOR** — for each episode in the post-split state, compute:
> - Peak beat position (the episode's highest-stakes board-change line, identified per URI-011's SHAPE-COHERENT mechanic).
> - Post-peak section length and board-change density.
> Threshold candidates (validate against s01 corpus during V2 session): if the post-peak section exceeds 50% of episode length AND contains fewer than 2 board-changes, classify HARD `CURVE-SHAPE-EPISODE-FLAT-AFTERMATH-{episode}`. If post-peak is 40-50% with <2 board-changes, classify SIGNAL.
> The sub-class operates on episode-level data and is independent of season-plan defenses — citing season-plan mandate does not override a structural HARD verdict.

**Validation against s01:** The threshold should produce HARD on e04 (89-bone post-IGNITION, 1 board-change in aftermath = SLEEPER-1) and SIGNAL on e02 (40+ bones post-Rowan-claim aftermath, low density), e03 (48-bone post-Rymer aftermath), e06 (Elara 100-bone competent-action sequence before any board-change). All four match audience-confirmed seams.

**Dependency:** URI-011 must define the per-episode peak-beat mechanic first (or co-produce with this sub-class).

**Cost:** medium. Sub-class authoring + threshold calibration on s01 + integration into the audit-report schema.

---

## Carry-back item URI-019 — Auditor classes CONSTRAINT-BEHAVIOR-SEQUENCE + CONSTRAINT-RESPONSE-BONE-REQUIRED

**Category:** Auditor class refinement (URI-006 progress).

**Source:** R2 C-auditor-self-review Refinement 2; SLEEPER-2a (U3 worm cost-inversion at line 203) + SLEEPER-3 (U2 absent response-bones after apprentice-mark).

**The gap:** R1's CONSTRAINT class checked series laws and cast-presence consistency but did NOT check behavior-card compliance at the sequence-ordering or required-presence level. Both SLEEPERs are behavior-card compliance failures the class could not see.

**Candidate V2 sub-classes (paired):**

> **CONSTRAINT-BEHAVIOR-SEQUENCE** — for actors with a behavior card specifying cost-processing-order or sequence-ordering rules (e.g., "accept first, register cost after"), check each multi-bone interaction against the order. Inversions (cost-signal firing before decisive action) classify SIGNAL by default, HARD when occurring at a season-plan-named cost-bearing beat (e.g., shard-load).
>
> **CONSTRAINT-RESPONSE-BONE-REQUIRED** — for actors with a behavior card specifying state-change-tracking-obligations (e.g., "tracks information-asymmetry as operational-priority updates"), check that named state-changes (apprentice-mark, pastoral-claim, surveillance-record, debt, letter-event) are followed within the same chunk by at least one bone in physical-register signaling that the state-change is in working memory. Absence classifies SIGNAL by default, HARD when the state-change is a season-plan-named board-change.

**Validation against s01:**
- CONSTRAINT-BEHAVIOR-SEQUENCE: catches SLEEPER-2a (Taylor jaw-tightens at 203 before Rowan offers volume at 206 — inversion of cost/decision sequence at a pastoral-claim beat). HARD because the season-plan §D names sept-access as a managed-relationship beat.
- CONSTRAINT-RESPONSE-BONE-REQUIRED: catches SLEEPER-3 (apprentice-mark at episode 99 followed by 30 bones of domestic routine with zero response-bones from Taylor in operational-tracking register). HARD because the season-plan §D names early-baseline as a beat with one required cost-running and the apprentice-mark is the named change.

**Dependency:** URI-003 (margit referrals) — Taylor's behavior card needs explicit `cost-processing-order` and `state-change-tracking-obligation` fields. The sub-classes cannot run mechanically against a card that lacks these fields. The fields are simple to add (one or two lines per card per pattern), but they require margit dispatch.

**Cost:** medium for the auditor sub-classes. Card additions are part of URI-003 (already queued).

---

## Carry-back item URI-020 — Auditor class AP-SCAN-POST-PEAK-WINDOW-QUALITY

**Category:** Auditor class refinement (URI-006 progress).

**Source:** R2 C-auditor-self-review Refinement 3; SLEEPER-2b (U4 fishwife misdirection at lines 372–393).

**The gap:** R1's AP-SCAN ran S3-style window-quality checks at episode scope with the rubric's ~10% TOLERATED budget. The fishwife sequence was a single TOLERATED window in a 168-line episode where the aggregate count was within budget. AP-SCAN had no mechanism to weight TOLERATED windows by their position relative to the episode peak. A TOLERATED window 22 bones AFTER the episode's highest-stakes beat is materially worse than a TOLERATED window in low-stakes territory — the former actively displaces consequence from reader working memory.

**Candidate V2 sub-class:**

> **AP-SCAN-POST-PEAK-WINDOW-QUALITY** — once CURVE-SHAPE-EPISODE-INTERIOR identifies the peak beat for an episode, scan the 20-line window immediately following the peak. Threshold candidates: any TOLERATED window of 15+ lines within 20 lines after the peak classifies HARD `AP-SCAN-POST-PEAK-MISDIRECTION-{line-range}`. Any TOLERATED of any length within 10 lines of peak classifies SIGNAL.

**Validation against s01:** SLEEPER-2b is the test case. Episode e03 peak = Rymer faces Taylor at line 370. Lines 372–393 = 22-line TOLERATED window starting 2 lines after peak. Under the candidate threshold: HARD `AP-SCAN-POST-PEAK-MISDIRECTION-372-393`.

**The "formulaic-scoring bypass" pattern this catches:** S3's threshold is computed across the full episode. The fishwife window is one TOLERATED in a 168-line episode where 10% TOLERATED = 16.8 lines budget; one 22-line window technically exceeds budget but is an isolated count. The post-peak quality modifier reweights the same data: the same 22 lines are now positioned-as-misdirection rather than budgeted-as-tolerated. This is the meta-tuning insight: thresholds composed across full units suppress position-dependent severity.

**Dependency:** URI-018 (CURVE-SHAPE-EPISODE-INTERIOR) for the peak-beat anchor.

**Cost:** small-to-medium. Sub-class authoring + threshold validation on s01.

---

## Carry-back item URI-021 — Meta-tuning loop pattern documentation

**Category:** Process documentation (reusable for future tuning projects).

**Source:** R2 as a whole — the run itself is the artifact.

**The gap:** R2 invented a meta-tuning loop on the fly: tighten the audience brief → re-run adversarial → audit self-review → critic-tuning carry-back synthesis. The pattern works (it surfaced 4 SLEEPERs and 3 auditor refinements). Future tuning projects (any /and-X command tuning, future facet rounds, or even future /and-season tuning rounds with new corpora) would benefit from running the same loop. Without documentation, the next project has to invent it again.

**Candidate V2 documentation:**

> Add `design/shoot-v2/meta-tuning-loop.md` (or fold into `design/shoot-v2/facet-tuning-process.md` as a new section). Documents the four-phase loop:
> 1. **Tightening brief** — articulate which formulaic thresholds the next round suspends and what hypotheses the run tests.
> 2. **Tightened audience attack** — re-attack the same units with rubric-arithmetic deference suspended. New verdict category: SLEEPER (R1 MODERATE/missed → R2 STRONG).
> 3. **Auditor self-review** — auditor reviews its own prior audit against the new audience output, identifying classes that had the right territory but the wrong threshold.
> 4. **Critic-tuning carry-back** — produce schema/class refinements as URI entries. Goes to the upstream-tuning-queue as the deliverable.
>
> Includes hypothesis-discipline: state predictions before the run; report results against predictions after. R2 confirmed all 4 of its hypotheses, which is signal that the formulaic-scoring concern was real and the meta-loop is responsive to it.

**Cost:** small. Doc-only edit; no schema or rubric impact.

---

## Updated run status

R2 closes cleanly.

| Run | Status | Output |
|---|---|---|
| R1 | SHIPPABLE-PENDING-EXECUTION (closed by Phase I user verdicts) | 18 unit decisions + 10 V2 carry-backs + 0 human escalations remaining |
| R2 | SHIPPABLE-AS-IS (closed by this Phase D) | 4 SLEEPERs surfaced + 3 auditor refinements + 1 schema addition + 1 process pattern; 5 new V2 carry-backs (URI-017 through URI-021) |

**Total V2 candidates queued from R1+R2:** 15 items (URI-007 through URI-021).

**Hypothesis discipline confirmed:** R2's A-tightening-brief.md predicted 4 specific outcomes; all 4 confirmed. The formulaic-scoring concern was not overstated; the meta-loop demonstrates measurable critic improvement potential.

**Where R1 audience and auditor were honestly strong:** R2 did NOT find that R1 was broadly miscalibrated. 6 of 11 auditor classes need no refinement; 12 of 18 unit-aggregate verdicts hold; only 4 per-persona verdicts actually upgraded under the tightened brief. R1's structure was correct; R1's thresholds were too permissive at specific points. The meta-tuning is targeted, not wholesale.

**No corpus mutations from R2.** All R1 routed subtasks (screen-writer bones, dramatist boundary-rebalance, showrunner-self header updates) still apply. R2 produces critic improvements only.

---

## Mirror to upstream-tuning-queue.md

The 5 R2 carry-back items are mirrored as URI-017 through URI-021. See queue file for canonical entries.

## Phase D complete

Tuning R1 + R2 close at decision level. The next sessions are:
1. **Execution session** for R1's routed subtasks (screen-writer / dramatist / showrunner-self).
2. **V2 rubric session** for landing URI-007 through URI-021 (15 items; medium-to-large session).
3. **Future tuning rounds** can reuse the URI-021 meta-tuning loop pattern as a standard module.
