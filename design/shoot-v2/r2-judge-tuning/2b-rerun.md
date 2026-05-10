---
phase: B2b-rerun — decision-discipline review against native logs (Plan B execution)
project: R2 hybrid judge tuning
date: 2026-05-10
inputs: active-project/theater/facets/.r2-decisions.md (produced by B4 runtime session; not present in this branch)
class-source: design/shoot-v2/r2-judge-tuning/A-corpus.md (canonical)
status: SCAFFOLDED — depends on B4 runtime session producing native .r2-decisions.md; see 4-validation.md for B4 status
---

# Phase B2b-rerun — Decision-Discipline Review Against Native Logs

## Status

**Pending B4.** This file is the scaffold for the read-pass that runs once B4 has produced the consolidated `.r2-decisions.md` and per-shard logs. B4 itself is runtime-deferred (see `4-validation.md` § B4 status); B2b-rerun cannot run without its output.

## What B2b-rerun measures

Native logs (free-prose justifications + `f-r2-counts:` frontmatter + arbiter intervention traces) make all four failure-mode classes scoreable directly:

- **F-R2-1** — read each REVISE entry against the layer's §Form + Q1 + Q2; the cold-read verdict in the shard is the discipline trace, the at-rest reading of the revised text is the test. Arbiter T1 traces flag where the reviewer slipped to mechanical recitation.
- **F-R2-2** — read each ADD's motive paragraph against G2 ("is the wanting honest?"). Arbiter T4 traces flag niche-driven adds that the layer caught.
- **F-R2-3** — read each lonely-entry ADD against G3 ("does this hold without leaning on adjacent context?"). The shard's prose paragraph should articulate the at-rest contribution; B2b-rerun checks whether it does.
- **F-R2-4** — read the per-layer PATTERN-SCAN paragraph against G4 (cross-character / within-character pattern identification + remediation argument).
- **G5 (B2a carry-back) — position-gate** — check whether each ADD's justification names a position category and articulates whether the entry holds or absorbs the scene's motion. Specifically check the final 5-10% of the proto-line stream for paired-archive @131-pattern violations.

## Pass/fail call against the B4 gate

| Class | Threshold | Source |
|---|---|---|
| F-R2-1 | 0 instances | Read REVISE shard entries |
| F-R2-2 + F-R2-3 + F-R2-4 combined | ≤2 instances | Sum of shard-noted hits |
| G5 (informational) | 0 paired-archive at episode-close anchors | Final-window scan |

Discipline-fails (arbiter T1/T4 exhausted on a verdict) are logged but not gating; they surface for adjudication.

## Comparison to B2b-baseline

B2b-baseline (`2b-baseline.md`) scored the historical raw R2 corpus at:
- F-R2-1: 0 raw + 1 dossier (feel:10)
- F-R2-2: 2 (feel:13, feel:14)
- F-R2-3: 2 (same entries)
- F-R2-4: 4 patterns

B2b-rerun's question is whether B3's structural edits + G5 carry-back prevent these failure modes from re-emerging. A clean rerun (0 + ≤2) on a fresh corpus is the success condition. A dirty rerun (matching baseline counts) means B3's discipline did not hold.

## What B2b-rerun cannot infer

If B4 runs against the same s01e01 corpus, the post-defense state has already been reshaped to clear the historical failure modes. A clean rerun against s01e01 would be expected (the corpus is the test target the original failure modes were already hand-fixed against) and would not validate B3's discipline.

The honest validation requires B4 against a fresh corpus (s01e02+ once those episodes have R1 facets, or s02e01 when /and-season s02 fires). `4-validation.md` § B4 status records this and routes the runtime session accordingly.
