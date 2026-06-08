# Multi-arm vs single-arm b01-c04 — audit + ablation evidence
## Date: 2026-05-27 (remediation)

This directory contains the b01-c04 multi-arm + tournament + cherry-pick run artifacts produced under the (now-reverted) URI-STITCH-CHERRY-PICK-DEFAULT-ON + URI-STITCH-MULTI-ARM-DEFAULT-ON spec. The artifacts are preserved as ablation evidence and as a record of the audit finding. They are NOT in the canonical active-project path.

## Why this exists

The audit traced URI-STITCH-CHERRY-PICK-DEFAULT-ON to commit `be7de51` (2026-05-27 03:09), which codified cherry-pick as the default 12 minutes after the b01-c02 cherry-pick experiment commit `2d525d2` (02:57) whose own conclusion was:

> Cold-read verdict: CONTINUE=no (same as multi-arm). Reader recovered the woman as a woman + clocked moral-line callback to stitch-maker's ward, but structural failure unchanged — stakes posture without located stakes, ledger-vocabulary without grounded mechanism.
>
> **Key finding: cherry-pick fires same walkout-severity peeves as pure-winner because cost-legibility lives in bones SVO authoring, not stitch paragraph composition. Per-paragraph craft optimization is not predictive of continue-rate.** Tournament rubric is blind to reader-orientation + person-presence criteria.

The codification commit cherry-picked option D ("make cherry-pick a default arm under multi-arm") from a list of process-tuning candidates and promoted it to default-on, citing the experiment as evidence of "strictly-better default" — which inverts the experiment's actual conclusion.

A subsequent rewire (URI-STITCH-MULTI-ARM-DEFAULT-ON, this session) compounded the misread by making multi-arm the practical default through auto-alt-authoring at Phase 0 step 4b.

## What was run on b01-c04 under the misrepresented defaults

- Phase 0 step 4b auto-alt-authoring fired → +1 procedural-with-pressure alt counterweighting the series-Robinson primary. N=2.
- 6 Phase 1 scene-window forks (2 arms × 3 scenes), 3 waves serialized.
- Phase 1.5 tournament: arm-2 procedural won scenes A + B; arm-1 Robinson won scene C.
- Phase 1.5 cherry-pick: ceiling-collapse 3/3 (K=0 substitutions). Per-scene tournament winners swept the rubric paragraph-by-paragraph.
- Phase 1.5 scorer: scene-A −11, scene-B −14, scene-C −27 (WALKOUT-flagged on PEEVE-9 cost-not-legible).
- Phase 7 aggressive on the multi-arm cherry-pick output: 1355 words (vs single-arm 1694; 339 words tighter).
- Phase 9 cold-read: PASS but harsher than single-arm cold-read on payoff ("Thin. Nothing turns. No one resists.") + prose-density wading.

## Comparative-scorer verdict (4-way blind ranking on taste-rubric)

- P1 ARM-1 RAW (Robinson all-scenes; pre-tournament, pre-Phase-7): rank 4, score −42
- P2 CHERRY-PICK FINAL (multi-arm + tournament + cherry-pick K=0 + Phase-7): rank 2, score −26
- P3 ORIGINAL SINGLE-ARM (Robinson + Phase-7; restored as canonical): **rank 1, score −8**
- P4 ARM-2 RAW (procedural all-scenes; pre-tournament, pre-Phase-7): rank 3, score −38

Net: single-arm outranked multi-arm + cherry-pick + Phase-7 by 18 points on this chapter.

Caveat: single comparative-scorer dispatch is a noisy single-judge ranking. Multi-judge verification (3 independent blind judges) is at `comparative-2026-05-27/` and the multi-judge verification report.

## Remediation actions (2026-05-27)

1. **URI-STITCH-CHERRY-PICK-DEFAULT-OFF** — `.claude/commands/and-stitch.md` `--cherry-pick` flag default reverted from `paragraph` to `off`. Audit note appended documenting the misrepresentation.
2. **URI-STITCH-MULTI-ARM-DEFAULT-OFF** — Phase 0 step 4b auto-alt-authoring removed from /and-stitch.md. Multi-arm is opt-in by user-authored alts on disk.
3. **URI-STITCH-COLD-READ-FEEDBACK-LOOP emphasis added at Phase 9 Step 4** — codifies option E from the c02 experiment (the lever the experiment actually pointed at): cold-read findings route to `/and-write revise --from-signals` because cost-legibility lives in bones SVO authoring, not stitch composition.
4. **b01-c04 canonical draft restored to P3** (single-arm version from commit `2c97461`); multi-arm artifacts moved to this ablation dir.
5. **Multi-judge verification** of the comparative finding (P3 > P2) — see `multi-judge-verification-2026-05-27.md` in this dir.
6. **admin process-critic dispatch** on the codification anti-pattern (12-minute gap between experiment-conclusion and contradictory codification by the same session) — see `admin-process-critic-codification-anti-pattern.md` in this dir.

## What's preserved in this dir

- `b01-c04.scene-{A,B,C}.arm-{1,2}.draft.md` — per-arm Phase 1 raw outputs (Robinson + procedural-with-pressure)
- `b01-c04.scene-{A,B,C}.winner.draft.md` — per-scene tournament winners (= canonical post-tournament, pre-Phase-7 for scenes where ceiling-collapse fired)
- `tournament-b01-c04-scene-{A,B,C}-2026-05-27.md` — Phase 1.5 Step 1 blind tournament verdicts
- `cherry-pick-b01-c04-scene-{A,B,C}-2026-05-27.md` — Phase 1.5 Step 2 cherry-pick composer reports (all returned ceiling-collapse)
- `scorecard-b01-c04-scene-{A,B,C}-2026-05-27.md` — Phase 1.5 Step 3 cherry-pick scorer per-scene scorecards
- `coldread-b01-c04-2026-05-27-multiarm.md` — Phase 9 cold-read of the multi-arm assembled draft
- `prose-rationale-audit-b01-c04-2026-05-27-multiarm.md` — Phase 9 Step 3.5 prose-rationale-mute audit (10/10 PASS, same as single-arm)
- `comparative-scorecard-b01-c04-2026-05-27.md` — single-judge 4-way blind comparative ranking
- `comparative-2026-05-27/` — blind-staged artifacts P1-P4 used for the 4-way comparison
- `tournament-scorecards.md` — the cross-chapter scorecard ledger (one row per scene, retracted by audit)
- `voice-exemplar-b01-c04.alt-auto-1.md` — the procedural-with-pressure auto-alt exemplar authored at Phase 0 step 4b
- `multi-judge-verification-2026-05-27.md` — Phase D multi-judge ranking (to be added)
- `admin-process-critic-codification-anti-pattern.md` — Phase E admin process-critic verdict (to be added)
