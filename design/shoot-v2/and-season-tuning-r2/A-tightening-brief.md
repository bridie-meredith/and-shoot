---
run: and-season-tuning-r2
date: 2026-05-10
status: ACTIVE
parent-run: and-season-tuning-r1
type: meta-tuning of review critics
trigger: user direction 2026-05-10 — "keep tuning. include antagonistic feedback based on tighter audience rather than formulaic scoring. this should also tune our review critics within the process itself"
---

# Run R2 — Meta-Tuning of Review Critics

R1 produced rubric-grounded decisions, but the audience and auditor leaned on **formulaic thresholds** to land their verdicts:

- S3 cap: ~10% TOLERATED + zero BORED + two-consecutive-BORED.
- S9 threshold: ≥30% B-or-T in 100-line stretch.
- S3.5 threshold: verb appearing 5+ times across the season.
- Phase 4 Step 1(b) "back half" for climax position.

These thresholds let defenses dodge real seams on technicalities ("the count was within tolerance"; "the threshold wasn't met"; "the formula doesn't classify this verb"). R1's three REJECTs in Phase F (U1, U2, U17) all turned on showrunner defenses that cited rubric language to defeat seams the audience had already named in plain English.

The user's directive: the next round attacks **without leaning on formulaic scoring**. The audience's taste is the criterion; the rubric's thresholds are advisory, not exculpatory. The act of running this also serves as **critic-tuning** — the delta between R1 (formulaic-permitted) and R2 (taste-only) tells us where the persona cards and the auditor classes need refinement.

---

## What R2 changes

### 1. Audience tightening directive

The three audience personas attack under a **tightened brief** that explicitly suspends formulaic-deference:

> **Tightened attack standard for R2:**
> - Do NOT use rubric thresholds as backstops. The S3 ~10% TOLERATED cap, the S9 ≥30% B-or-T threshold, the S3.5 5+ instance count, and the Phase 4 "back half" rule are advisory only for this round. If your taste registers a fault, attack it — even if the rubric arithmetic technically passes.
> - Do NOT defer to season-plan mandates as cover. If the season-plan §B says "early baseline" and your taste says the open is dead-air, attack the dead-air. The plan permits the register; it does not absolve the bones.
> - Do NOT defer to tone-law citations as cover. If `cond-series-tone-constraints-84ac` prohibits catharsis, the post-peak arc still has to deliver consequence-immediacy at every ratchet-click; attack ratchets that don't tighten.
> - Do NOT defer to "previously identified / known residual" parking. A carry-forward is open until adjudicated clean. Attack carry-forwards as if they were fresh seams.
> - Do NOT defer to convergence-call shippability. R1 declared SHIPPABLE-PENDING-EXECUTION; this round attacks the pre-execution corpus, including the bones the showrunner agreed to revise — if the *current* state has a seam you find unacceptable, attack it.
> - Lean toward **STRONG** verdicts. R1 produced 12 STRONG / 4 MODERATE / 1 THIN; R2 expects more STRONG and fewer MODERATE. MODERATE is a pity verdict you owe nothing to.
> - **One additional category: SLEEPER.** A seam that R1 surfaced but classified MODERATE or that you yourself missed in R1's pass — and that, on second read, is actually a STRONG fault. Mark these `SLEEPER-{R1-source}`. SLEEPERs are the meta-signal: they tell us where R1's formulaic scoring let a real seam pass.

### 2. Auditor self-review directive

The auditor reviews its own R1 audit (`active-project/staff/auditor/season-tuning-r1-audit.md`) against the corpus AND the R2 audience seam output. For each R2 seam — especially SLEEPERs — the auditor asks:

> Did one of my 11 classes mechanically point at this in R1? If yes — was the threshold the reason I didn't classify it HARD? If no — what class refinement would catch it next time?

Output: per-class refinement candidates for the audit upgrade (URI-006 Step G design item).

### 3. Critic-tuning carry-backs

Where R2 finds that R1's audience or auditor missed a seam due to formulaic deference, R2 produces:

- **Persona-card additions** — `tightened-attack-standard` section for `class: persona` (if not already in `class: persona` schema).
- **Auditor class refinements** — adjusted thresholds, new sub-classes, or replaced mechanisms.

These land as new URIs (URI-017+) in `design/shoot-v2/upstream-tuning-queue.md`.

---

## What R2 does NOT do

- **Does not move the locked V1 rubric.** The rubric stays as anchored in R1. R2's tightened attack happens *despite* the rubric's formulaic thresholds, not by editing them.
- **Does not re-author the s01 corpus.** R2 produces critic improvements + additional seam findings; corpus mutations queued for R1 execution still apply.
- **Does not re-run all of R1's phases.** R2 is focused: tightened-audience attack + auditor self-review + carry-back synthesis. No new Phase E/F adjudication; the meta-tuning is the deliverable.

---

## Phases

| Phase | Output |
|---|---|
| A — Tightening brief (this file) | `design/shoot-v2/and-season-tuning-r2/A-tightening-brief.md` |
| B — Tightened audience attack | `design/shoot-v2/and-season-tuning-r2/B-r2-seams.md` |
| C — Auditor self-review | `design/shoot-v2/and-season-tuning-r2/C-auditor-self-review.md` |
| D — Critic-tuning carry-backs | `design/shoot-v2/and-season-tuning-r2/D-critic-carry-back.md` + queue updates |

Total: 2 dispatches (audience + auditor). One commit per phase.

---

## Expected deltas (hypothesis to test)

Predictions for the meta-loop, against which we measure the run:

1. **At least 2 SLEEPER seams will surface** — R1's MODERATEs (U7, U8, U12, U16) are the natural candidates. If the tightened audience treats them as STRONG, the R1 MODERATE classification was a formulaic-scoring concession.
2. **At least 1 R1 ACCEPT will get re-attacked** — the most likely candidate is U5 (e04 dramatic shape; pulp REJECTed in F-final; F overruled to ACCEPT-WITH-CAVEAT). R2's tightened pulp may STRONG it.
3. **Auditor's S3.5 5+ threshold will need refinement** — fault-AP-1 named 18+ instances of `holds the feet`; R2 may show that the threshold should be a per-context-differentiator rate, not a count. This is also URI-007's territory.
4. **At least 1 new auditor class candidate** — possibly a "formulaic-scoring-bypass" class that flags when other classes report PASS but consume a threshold-budget that taste would reject.

If R2 does NOT produce these deltas, the formulaic-scoring concern is overstated. The run measures itself.

---

## Phase A complete

Proceed to Phase B.
