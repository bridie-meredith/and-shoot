# Tournament-tuning retrospective — taylor-westeros-good-intentions (b01)

**Date:** 2026-06-23
**Type:** Retrospective calibration analysis (no active project; mines on-disk evidence from the completed `taylor-westeros-good-intentions` one-book series).
**Reads:** `design/tournament-tuning.md` (framework v1, 2026-05-27) + `schemas/tournament-scorecard.schema.md` (v1).
**Scope:** the renderer-voice tournament + cherry-pick + scorecard path at `/and-stitch` Phase 1.5, and whether its per-arm rubric scores predicted the Phase 9 cold-read CONTINUE ground truth across b01.

**Headline:** The tournament apparatus ran *live* on exactly **two** chapters of a 20-chapter book — c02 (tournament only) and c04 (full apparatus, but as a reverted ablation experiment). c05–c20 all shipped single-arm (N=1, tournament a no-op). The framework's accumulating "ledger across 5+ chapters" never accumulated. **Most of Q1–Q5 are still live-gated for want of data.** But the data that *does* exist points hard and consistently in one direction on the load-bearing question, and that one finding is the most valuable thing the book left behind.

---

## 1. Evidence inventory

### What exists

| Artifact class | What's on disk | Coverage |
|---|---|---|
| **Per-arm tournament verdicts (Layer 1)** | `staff/reviews/tournament-b01-c02-scene-{A,B,C}-2026-05-26.md` (3); `staff/ablation/multi-arm-vs-single-arm-b01-c04-audit-2026-05-27/tournament-b01-c04-scene-{A,B,C}-2026-05-27.md` (3) | **2 chapters** (c02, c04) |
| **Cherry-pick composition records (Layer 2)** | c04 only: `…/cherry-pick-b01-c04-scene-{A,B,C}-2026-05-27.md` (3) | **1 chapter** (c04). c02 had a cherry-pick *draft* + cold-read but no per-scene composition record persisted. |
| **Per-scene scorecards (Layer 3)** | c04 only: `…/scorecard-b01-c04-scene-{A,B,C}-2026-05-27.md` (3) + `…/comparative-scorecard-b01-c04-2026-05-27.md` (4-way) | **1 chapter** (c04) |
| **Cross-chapter scorecard ledger** | `…/multi-arm-vs-single-arm-b01-c04-audit-2026-05-27/tournament-scorecards.md` — **3 rows, c04 only, inside the ablation dir** | **1 chapter.** The canonical `staff/showrunner/tournament-scorecards.md` named by the schema **was never created.** |
| **Phase 9 cold-reads (Layer 4 — ground truth)** | `staff/reviews/coldread-*.md` — ~30 files spanning c01–c20 incl. revises/restitches | **~all 20 chapters** (the one layer with real coverage) |
| **Voice-exemplar ablation** | `staff/ablation/voice-exemplar-experiment-2026-05-26/` + `…-taste-aligned-2026-05-26/` (4-variant prime cold-read on c02 scene-A) | c02 scene-A |
| **Multi-judge verification** | `…/multi-judge-verification-2026-05-27.md` (3 independent blind judges, P3 vs P2 on c04) | c04 |
| **b01-c01 ablation** | `staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md` + `staff/ablation/b01-c01-*` | c01 (leave-one-out facets, not tournament) |
| **Book verdict (ground-truth aggregate)** | `staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md` = **PASS-WITH-NOTES** | book |

### What's missing (the thinness, stated plainly)

- **No scorecard ledger ever accumulated in the canonical location.** The schema's whole premise — `staff/showrunner/tournament-scorecards.md`, append-only, one row per scene per chapter, back-referenced to Phase 9 — has a population of **3 rows, for one chapter, inside an ablation directory the audit explicitly marked "retracted."**
- **The tournament was de-defaulted after c04.** On 2026-05-27 the audit reverted URI-STITCH-CHERRY-PICK-DEFAULT-ON and URI-STITCH-MULTI-ARM-DEFAULT-ON to opt-in. From c05 onward every render-log records `N=1 single-arm`, `cherry-pick: n/a (no-op)`. So the framework was effectively shelved 16 chapters before the book closed.
- **No Phase-9 back-reference was ever written into a ledger row** in the canonical flow (the c04 ledger's `cold_read_verdict` fields were hand-filled in the ablation dir; never wired through Phase 9.6 on a live chapter).
- **Cross-chapter trend (the schema's "5+ stitch runs" reading mode) is impossible** — there are not 5 tournament runs in the corpus, there are 2.

**Net:** the evidence base is **2 tournament chapters out of 20**, one of which (c04) was a deliberately-mis-defaulted experiment that the project then *reverted*. Every conclusion below is bounded by that.

---

## 2. Per-Open-Question findings

### Q1 — Should cherry-pick run on N=2 only? (cost vs. lift at N≥3)

**On-disk evidence:** Cherry-pick ran at N=2 on c04 (the only live cherry-pick with a persisted composition record). Result: **ceiling-collapse 3/3 scenes, K=0 substitutions** (`tournament-scorecards.md` rows A/B/C all `ceiling_collapse: true, substitutions: 0`). c02's cherry-pick (also N=2, per `coldread-b01-c02-2026-05-26-cherry-pick.md` + the c04 README's quote of commit `2d525d2`) likewise produced a draft that "fires same walkout-severity peeves as pure-winner." **N=3+ was never run anywhere in the corpus.**

**Sufficiency:** Insufficient to answer the question *as posed* (N=2 vs N≥3 cost/benefit), because N≥3 has zero data points. But there *is* a stronger adjacent finding: at N=2 on this substrate, cherry-pick bought **nothing** (100% ceiling-collapse — the per-scene tournament winners already swept the rubric paragraph-by-paragraph, so there was nothing to substitute in). The quadratic-correspondence-table cost the question worries about at N≥3 is moot when even N=2 yields K=0.

**Recommendation:** **(b) Insufficient to set an N≥3 policy — but calibratable on the narrower claim:** cherry-pick should be **gated on a non-collapse precondition**, not run unconditionally at any N. Concretely: if the first scene's cherry-pick returns `ceiling_collapse: true`, suppress cherry-pick for the remaining scenes of that chapter (the per-arm winner is already paragraph-optimal; the composer is doing dead work). This is supported by the only two cherry-pick chapters in the book both collapsing. To answer the *original* N≥3 question needs ≥2 more chapters where N=3 is actually run on a substrate with paragraph-level lift room (i.e. a chapter whose tournament does *not* sweep at the per-arm level). **Live-gated.**

### Q2 — Should the scorer be a different agent than the judge?

**On-disk evidence:** Both scorer and judge were `general-purpose` throughout c02 and c04. The one relevant signal is the **multi-judge verification** (`multi-judge-verification-2026-05-27.md`): 3 independent blind `general-purpose` judges on c04 P3-vs-P2 all agreed (3/3, P3 wins, spreads 9/14/16 pts, "consistent within sampling noise"). That tells us same-class judges were *reproducible* on a clear-separation case — but says nothing about whether a *different* (persona-card) scorer would calibrate severity better, because no persona-card scorer was ever dispatched.

**Sufficiency:** Insufficient. There is exactly one within-class reproducibility check and zero cross-class (persona vs general-purpose) comparisons. The framework's own worry — "importing the persona's biases" — has no evidence either way.

**Recommendation:** **(b) Insufficient — needs a live A/B.** What's missing: one chapter scored by `general-purpose` AND by an audience-card fork on the same drafts, with both severity vectors compared against the Phase 9 cold-read. The c04 multi-judge result is mild positive evidence that the *current* (general-purpose) scorer is at least self-consistent on clear cases, which lowers the urgency of changing it. **Live-gated; low priority** (the load-bearing failure mode below is upstream of scorer choice).

### Q3 — Voice-consistency seam-flagging: hard fence at composition or soft signal at scoring?

**On-disk evidence:** The trigger for tightening (per the schema's reading guide) is "`flag-seam` correlating with Phase 9 FAIL across 3+ chapters." In the corpus, **cherry-pick ceiling-collapsed on every scene it ran**, which means **zero cross-arm substitutions were ever made**, which means **no tonal seam was ever introduced** — voice-consistency was structurally `seamless`/n/a on every persisted scorecard (the c04 scorecards report no seam because the winner is a single arm's pure output). There is **no `flag-seam` event anywhere in the corpus** to correlate against anything.

**Sufficiency:** Insufficient — and not just thin, but *structurally empty*. The seam-flagging mechanism never had a chance to fire, because the precondition for seams (actual cross-arm paragraph mixing) never occurred.

**Recommendation:** **(b) Insufficient — keep it soft.** Do not tighten to a composition-time hard fence; there is no evidence `flag-seam` predicts anything because there are no `flag-seam` events. The current soft-signal setting costs nothing while the mechanism is dormant. To revisit needs chapters where cherry-pick actually substitutes across arms (K>0) — which itself requires escaping the ceiling-collapse regime (see Q1). **Live-gated, downstream of Q1.**

### Q4 — How does the framework interact with the audience-tournament (PROP-0005-A Phase 3) when it lands?

**On-disk evidence:** The audience-tournament never landed in this project (it is deferred under the impersonator-experiment evidence, per the framework's own scope note). `staff/ablation/audience-experiment-2026-05-26/` and `…/impersonator-experiment-2026-05-26/` exist as the experiments that *deferred* it, but no audience-tournament scorecard class was ever produced.

**Sufficiency:** No evidence — the thing the question asks about does not exist on disk.

**Recommendation:** **(b) Insufficient — unanswerable from this project.** Pure design question; needs the audience-tournament to actually land. The one transferable lesson the book *does* offer: the scorecard schema's `v<N>_extensions` versioning block was never exercised, so its forward-compatibility claim is untested. When the audience-tournament lands, the first per-persona-card scorecard is the test of whether the schema generalizes without rewrite. **Live-gated; out of reach until PROP-0005-A Phase 3 ships.**

### Q5 — Minimum scorecard count for a scorecard-driven admin process-critic auto-fire?

**On-disk evidence:** The framework says "implement after 5+ chapters of accumulated ledger evidence — premature now." The book accumulated **1 chapter** of ledger evidence (c04, 3 rows), in a retracted ablation dir. The admin process-critic *did* fire in this project — but off the **Phase 9 verdict** path (the existing per-verdict trigger) and off the **codification anti-pattern audit** (`admin-process-critic-codification-anti-pattern.md`), never off accumulated scorecard rows. The c04 ledger's own cross-run note even says so explicitly: "First chapter result; not yet enough data to trigger reconsideration. Watch on next 2-3 chapters." Those next chapters were all single-arm — the watch never resolved.

**Sufficiency:** Insufficient by an order of magnitude (1 chapter vs the 5+ the framework itself names as the floor).

**Recommendation:** **(b) Insufficient — do not implement scorecard-driven auto-fires.** The framework's own precondition (5+ chapters of ledger) was never approached. Worse, the project demonstrated the *opposite* risk: the one time a process change was codified off thin tournament evidence (the URI-STITCH-CHERRY-PICK-DEFAULT-ON codification 12 minutes after the c02 experiment), it **inverted the experiment's actual conclusion** and had to be reverted (c04 README + `admin-process-critic-codification-anti-pattern.md`). That is direct evidence that **auto-firing process changes off thin tournament data is dangerous**, which argues for *raising* the bar, not lowering it. Keep the per-Phase-9-verdict trigger as the sole admin auto-fire until a real ledger exists. **Live-gated; the project's history actively cautions against early implementation.**

---

## 3. Core-hypothesis assessment — did per-arm tournament scores predict cold-read CONTINUE?

**The framework's load-bearing bet:** make Layers 1–3 (per-arm rubric, cherry-pick, scorecard) predictive of Layer 4 (cold-read CONTINUE). The c02 finding that motivated the framework was that the two layers *diverged*. Did b01 vindicate or refute that?

**Verdict: the divergence held, and then some. The hypothesis did NOT hold up. Per-arm tournament rubric scores did not predict CONTINUE outcomes — and the project itself concluded as much and shelved the tournament.**

Evidence, in order of weight:

1. **c02 — direct refutation.** Three different stitches of c02 (original / single-arm voice-primed / multi-arm tournament+cherry-pick) all passed/swept the tournament rubric, and **all three returned CONTINUE = no** (`coldread-b01-c02-2026-05-26.md`, `…-multi-arm.md`, `…-revise.md`, `…-cherry-pick.md` — every one a "No"). The tournament cleanly ranked arms (scene-A→P1, scene-B→P2, scene-C→P1); the rubric was discriminating *something*; that something was not continue-rate. The cherry-pick cold-read says it outright: it "fires same walkout-severity peeves as pure-winner because cost-legibility lives in bones SVO authoring, not stitch paragraph composition."

2. **c04 — the strongest single piece of evidence, and it points the same way.** Full tournament + cherry-pick + Phase-7 (P2) was ranked **dead against** the plain single-arm draft (P3) by a 4-way blind comparative scorer (P3 −8 rank 1; P2 −26 rank 2; an 18-point regression), then **confirmed 3/3 by independent blind judges** (spreads 9/14/16, "direction robust"). The full apparatus did not just fail to help — on this chapter it actively *lost* to doing nothing, because cherry-pick ceiling-collapsed (no lift available) and Phase-7 then over-trimmed the multi-arm path, cutting the exact reader-orientation detail (chest-height parchment, brim-touch, Otto/Sera/three-month-window) that the single-arm path happened to keep. The tournament selected the right per-arm winners and the pipeline still regressed.

3. **The book-wide cold-read trajectory confirms the disease is upstream, not at stitch.** The CONTINUE ledger across b01: c01 yes-barely, c02 **no** (×4 stitches), c03 yes, c04 tentative-yes, c05 **no** (×3), c06 marginal-yes, c07 barely-yes, c08 **no** (×2), c09 **no** (×2), c10 mixed, c11 **no**, c12 **no**, c13 yes-barely, c15 **no**, c16 **no**, c17 **no**, c18 **no**, c19 no/barely, c20 barely-yes. The recurring failure cause is identical every time and is *never* a stitch-paragraph problem: "no person to hold onto, no concrete event, ledger/accounting register holds the reader at arm's length." This is the **ABSTRACTION-AS-SUBJECT / ledger-register** failure that DEC-0115 (2026-06-08) later retired project-wide. It originates in **bones authoring**, exactly where the framework's Loop D and anti-pattern "bones-blaming" already pointed.

4. **The project's own meta-conclusion.** The book closed at **PASS-WITH-NOTES** with the back-third (c14–c20) accounting-register quality logged as *design-inherent* — and the verdict (note 5) flags this as the empirical case for PROP-0037's hard-gate (3+ consecutive shipped-with-caveats → stop). The cold-read layer was the truth the whole way; the tournament rubric, where it ran, measured prose-surface craft that could not move that truth.

**What the tournament DID get right (don't over-condemn it):** within its own lane it was *sound* — per-scene blind judges picked the right per-arm winners on both c02 and c04, and the multi-judge replication shows the rubric is self-consistent on clear-separation cases. The tournament is a competent **craft proxy**. It is just not a **continue-rate predictor**, and on a substrate whose failure is upstream-structural (the King's-Landing-Taylor ledger register), the craft proxy and the reader-truth measured different things — precisely the c02 finding, now confirmed across a second chapter and a 20-chapter cold-read arc.

**Is the tournament worth its cost?** On this project's evidence: **no, not as a default**, and the project agreed by reverting it to opt-in after c04. Its value is real but narrow — (a) a craft-comparison instrument for *opt-in* A/Bs when you genuinely have two viable voice primes and a chapter with paragraph-level lift room, and (b) the structured per-criterion attribution that lets Loop D route a failure upstream. The framework's most load-bearing loop turned out to be **Loop D (cold-read FAIL + bones-level cause → `/and-write revise --from-signals`)** and the framework's most load-bearing *anti-pattern* ("tournament-as-gospel") was the one the project had to enforce against its own codification mistake.

---

## 4. Recommended calibration settings (those the evidence supports)

Only three settings have enough on-disk support to set now. All are conservative.

1. **Keep the tournament + cherry-pick + multi-arm OPT-IN, not default.** Already the state post-c04-audit; the retrospective ratifies it. Two live chapters, both showing the full apparatus failing to beat single-arm (c04: net −18, 3/3 judges; c02: 3 stitches all CONTINUE=no), is sufficient to *not revert the revert*. (Evidence: c04 README, multi-judge verification, c02 cold-reads.)

2. **Gate cherry-pick on a non-collapse precondition.** When the first scene's cherry-pick returns `ceiling_collapse: true`, suppress cherry-pick for the rest of the chapter (the winner is already paragraph-optimal; the composer is dead work). Both cherry-pick chapters in the book collapsed 100%. This addresses the *measurable* part of Q1 without taking a position on N≥3. (Evidence: c04 `tournament-scorecards.md` — 3/3 ceiling-collapse; c02 cherry-pick cold-read.)

3. **Prefer Loop D over rubric-tuning for ledger-register / abstraction failures.** The framework already says this; the book confirms it empirically and DEC-0115 later codified the project-wide fix at the bones layer. Any future tournament run on this register-class should route a low-`reader-orientation` / PEEVE-9-walkout result to `/and-write revise --from-signals`, **not** to a rubric edit — the rubric edit cannot reach the cause. (Evidence: c02 cherry-pick cold-read finding; c04 comparative "upstream load is real"; book-wide CONTINUE ledger; verdict-b01 + DEC-0115.)

**Plus one process guardrail (not a tournament setting, but earned here):** do **not** codify a tournament-derived default change off a single experiment — the URI-STITCH-CHERRY-PICK-DEFAULT-ON codification inverted its own evidence and was reverted within the day. Hold the framework's existing "2+ chapters / 5+ scenes" promotion floor as hard, and treat single-chapter tournament evidence as record-only. (Evidence: `admin-process-critic-codification-anti-pattern.md`.)

---

## 5. What remains live-gated

| Question | Status | What specifically is missing |
|---|---|---|
| **Q1** (N≥3 cost/benefit) | **Live-gated** (narrow non-collapse gate calibratable now) | ≥2 chapters where N=3 is actually run on a substrate with paragraph-level lift room (tournament not sweeping at arm level) |
| **Q2** (scorer ≠ judge) | **Live-gated**, low priority | 1 chapter scored by both general-purpose and an audience-card fork, severity vectors compared vs Phase 9 |
| **Q3** (seam-flag hard vs soft) | **Live-gated** (keep soft), downstream of Q1 | Any chapter where cherry-pick makes K>0 cross-arm substitutions so a seam can exist to flag |
| **Q4** (audience-tournament interaction) | **Live-gated** (unanswerable now) | The audience-tournament (PROP-0005-A Phase 3) to actually land + produce its first per-persona scorecard |
| **Q5** (scorecard-driven admin auto-fire) | **Live-gated; do NOT implement** | 5+ chapters of *canonical* ledger (have 1, in a retracted dir); project history cautions against early implementation |
| **Core hypothesis** (rubric → CONTINUE) | **Settled NEGATIVE on this project** | n/a — the two layers diverged on both tournament chapters and across the 20-chapter cold-read arc; tournament is a craft proxy, not a continue-rate predictor |

The single most important thing a future tuning session needs is **a real cross-chapter ledger** — ≥5 chapters where the tournament actually runs (multi-arm, N≥2, on chapters with genuine lift room), with Phase-9 back-references wired through. The taylor-westeros book did not produce it; it produced two data points and a cautionary tale, both of which say the same thing: the tournament optimizes craft the cold-read isn't failing on.
