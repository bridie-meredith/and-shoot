# Tensometer Tuning Corpus

Phase 0 corpus selection for the tensometer facet-tuning run.

## Choice: s01e01 full proto-line file (77 beats)

Rationale:

- **Self-contained episode.** Smallest of the six (77 vs. 100–310 beats). Manageable for full-curve authoring + review in one pass.
- **Strong dramatic shape.** Cold-open hostile-yard inspection with a clear arc: ambient establishing → procedural pressure → public confrontation → commit beat (Taylor presses the letter forward) → aftermath → exit through sept door. Provides natural 1/2/3 distribution and a legible peak.
- **Mixed beat types.** Environment beats (1–4), procedural beats (9–10, 17–18), positioning beats (11–12, 19), gaze beats (23–25), commit beats (38–39), dialogue beats (13, 21, 26–27, 32), aftermath beats (66–77). Exercises every rubric axis.
- **Tractable for curve-shape rubric.** 77 beats is enough to show act-shape but small enough that the auditor can verdict the whole curve in one read.

## Why not larger or stratified-only

The loc-state pipeline used 65 stratified anchors because loc-state is a *fire-or-don't-fire* per-beat decision; stratification across "should fire" cells exercised the decision space efficiently. Tensometer is different: every beat gets a scalar, and the *curve* over a real episode is a first-class output. Pulling 65 disconnected anchors would generate per-beat data but would not test curve-shape.

If Phase 1 baseline shows a need for more boundary-case data (e.g., the auditor is uncertain on rung-2-vs-3 cases), Phase 2 can supplement with stratified hard-case anchors from s01e02–e06.

## Naive baseline pass

Phase 1 has no existing tensometer entries to baseline against (no prior tensometer file exists for this project). Plan:

1. **Synthesize a contaminated baseline.** Dispatch dramatist with only `schemas/facet.schema.md` as guidance (the loose 1/2/3 definitions: "quiet / pressure / peak"). No rubric. No worked examples. Captures naive intuition, contaminated by whatever shape biases the agent already carries.
2. **Run V1 lenient + V2 strict reviews against the naive baseline.** Per-beat accuracy + curve-shape verdict. Establishes the floor to beat.

If the naive baseline is already curve-compliant and >85% per-beat accurate under V2, the rubric is over-engineered and we recommend stopping early.

## File map

- Source: `active-project/theater/proto-lines/s01e01.md` (77 lines)
- Naive baseline: `design/shoot-v2/phase1-tensometer-baseline-naive.md`
- V1 review: `active-project/staff/auditor/phase1-tensometer-v1-review.md`
- V2 review: `active-project/staff/auditor/phase1-tensometer-v2-review.md`
