# pitch-lab RUNBOOK — prompt → plan → rework-until-best

**This is the deliverable.** A repeatable process that takes a one-sentence story prompt, fleshes it into a substance-backed story plan, summarizes the plan in a fixed schema, evaluates the summary against an escalating-difficulty rubric, and reworks the plan until it passes at the highest tier — or is eliminated. Run it over a field of prompts and it functions as a tournament that converges on the few best.

It is a deliberately lighter-weight sibling of the main and-shoot planning chain (`/and-project → /and-series → /and-substance → /and-cast`). It borrows that chain's *discriminators* (substance contracts, dramatic shape, the DEC-0115 concreteness law) but not its full apparatus, so a single operator can run a wide field cheaply.

---

## The motion (one prompt)

```
PROMPT (one sentence)
  │
  ▼
[1] EXPAND  — screen-writer fleshes the prompt into a story plan
  │           (premise lens → trajectory → substance signature → structural shape)
  ▼
[2] SUMMARIZE — fixed-schema one-paragraph summary  (summarizer-spec.md)
  │
  ▼
[3] EVALUATE — rubric critic scores the summary on 5 axes at the current tier
  │           (evaluator-rubric.md)
  ▼
[4] GATE
  ├─ PASS at tier → promote to next tier (raise difficulty)
  ├─ NEAR-MISS (1-2 axes short, no fatal flaw) → REWORK and re-evaluate (cap 2 reworks/tier)
  └─ FAIL (fatal flaw, or far short) → ELIMINATE (log why)
  ▼
[5] CONVERGE — repeat [3]-[4] at rising tiers until the field is the target size (~3)
```

The loop's engine is **step 4's three-way gate**. A plan is never silently kept or dropped — it is promoted, reworked, or eliminated *with a logged reason*. The "rework until bestest" the principal asked for **is step 4's REWORK branch, applied at successively harder tiers.**

---

## The tournament (a field of prompts)

```
N prompts
  │
  ▼  Round 0:  EXPAND all → PLAN all          (pitch-lab/plans/)
  │
  ▼  Round 1 (Tier 1 — Open):     SUMMARIZE + EVALUATE all → cut to ~⅓
  │
  ▼  Round 2 (Tier 2 — Standard): EVALUATE survivors, harder → cut to ~½
  │           (NEAR-MISS survivors get one REWORK before the cut)
  │
  ▼  Round 3 (Tier 3 — Hard):     EVALUATE survivors, harder still → cut toward target
  │           (REWORK is now the main activity — close plans are lifted, not dropped)
  │
  ▼  Round 4 (Tier 4 — Bestest):  adversarial pass; only plans that survive an
  │           active attempt to reject them pass. Target ~3.
  ▼
BEST 3  +  process-improvements harvested at every round
```

**Escalating difficulty is the whole point.** The evaluator is not a fixed bar that plans clear or don't; it is a bar that *rises every round* (higher axis floors, higher total floor, and — critically — a shift in the critic's stance from "find what's good" to "find the reason to reject"). A plan that is "good" in Round 1 must become "the best" by Round 4 or it is cut. See `evaluator-rubric.md` for the four tiers.

---

## The five discriminator axes (constant across tiers; only the bar moves)

Borrowed directly from what the and-shoot pipeline has built and validated:

| Axis | What it tests | Pipeline lineage |
|------|---------------|------------------|
| **C — Concreteness / followability** | Can a naive reader reconstruct what physically happens? Is the engine concrete action, not abstraction/bookkeeping? | DEC-0115 / CLAUDE.md Rule 22; `/and-stitch` Phase 9 naive-follow |
| **D — Dramatic shape** | Real escalation curve, a turn, a road-to-hell — not a static premise held in stasis. | dramatist; `/and-substance` dramatic_shape |
| **S — Substance** | Does the protagonist pay an *escalating, mechanical* cost (cost ledger), and does antagonist pressure escalate? Is the tragedy built into the premise's own rules, not bolted on? | substance signature (cost ledger + antagonist pressure); `/and-write` bone-gate |
| **O — Originality** | Is the central *mechanism* fresh, or a recombination of familiar tropes wearing new paint? | taste-judge; audience novelty |
| **A — Aliveness** | Sensory/emotional pulse, a voice, a reason to care — not airless. | PROP-0022 aliveness twin; `/and-facets` Phase 2.5 ALIVE axis |

Each axis is scored 0–5. The **fatal-flaw** gate (any axis at or below the tier's floor, or a tier-specific disqualifier) eliminates regardless of total — this is what stops a high-total-but-broken plan from surviving.

---

## Operating rules (binding for an autonomous run)

These mirror the chapter-production protocol's R1–R5 discipline, adapted to the tournament:

- **T1 — No `AskUserQuestion`.** Every flow-control prompt goes to admin user-proxy (CLAUDE.md Rule 13). Admin `ESCALATE` is queued to the end-of-run summary, not prompted.
- **T2 — The gate is mandatory and three-way.** Every plan at every round is promoted, reworked, or eliminated *with a logged reason*. No plan is carried on vibes. No plan is dropped without a recorded fatal flaw or score.
- **T3 — Rework is cap-bounded.** A plan gets at most 2 reworks per tier. A plan that cannot clear a tier in 2 reworks is eliminated (its near-miss status is logged — it may be a process-improvement signal, not just a loss).
- **T4 — Escalate the critic, not just the threshold.** Each round raises the numeric bar AND the critic's adversarial stance. Round 4's critic is instructed to *try to reject every plan* and pass only what survives.
- **T5 — Harvest process improvements continuously.** Every round that produces a surprising elimination, a rework that worked, or a rubric ambiguity is logged to `process-improvements.md`. The tournament tunes itself.
- **T6 — Verify emitted artifacts (Rule 19) and read-back shared-state edits (Rule 20).** Any agent contracted to write a plan/eval file: stat the path before consuming. Never build on an in-message-only result.

---

## Why these axes and not "is it good"

"Is it good" is unfalsifiable and drifts with mood. The five axes are *each independently checkable*, and three of them (C, D, S) are the same discriminators the and-shoot pipeline gates real chapters on. A plan that scores high on all five is good in a way that survives a second reader, a hostile reader, and a naive reader — which is exactly the property the principal wants from "the bestest."

The single most load-bearing axis is **C (concreteness)**, per DEC-0115: a beautiful, original, dramatically-shaped premise that a naive reader cannot physically follow is the project's signature failure mode (Book 1's ledger-register collapse). Tier 3+ makes C a hard gate: a plan whose central engine is an abstraction ("the count closes," "the gap propagates") rather than concrete human/physical action cannot reach the best-3 no matter how high its other axes score.

---

## Artifacts

| File | Role |
|------|------|
| `00-pitches.md` | the 33 single-sentence prompts (the field) |
| `summarizer-spec.md` | the fixed summary schema + summarizer instructions |
| `evaluator-rubric.md` | the 5-axis rubric + the 4 escalating tiers + critic stances |
| `plans/plan-NN-<slug>.md` | one fleshed story plan per prompt (Round 0 output) |
| `eval/round-N.md` | per-round scorecards + gate decisions + cut list |
| `best-3/` | the three winners (final plan + summary + why-it-won) |
| `process-improvements.md` | running log of process + content improvements harvested |
| `RESULTS.md` | the end-of-run summary: field → best-3, with the convergence trace |
