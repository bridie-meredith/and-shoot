# Plan A — A1 staging draft

**Status:** drafted, awaiting Plan B sentinel `## Done — persona cards released` in `design/shoot-v2/r2-judge-tuning/4-validation.md` before applying.

**Discovery:** the plan refers to "Pass S4.5 dispatch brief" but the actual location of the inlined tens-attack vocabulary is `.claude/commands/and-season.md` Phase 4 **Step 2** dispatch brief — specifically lines 327–332 (the four tens-attack categories the persona may raise). Pass S4.5 itself is post-split continuity, unrelated. Staged edits target the actual location regardless of the plan's terminology.

---

## Edit 1 — `active-project/audience/dark-fantasy-reader/card.md`

**Append to body, after `season_scope_adversarial:` block:**

```
## Tens-attack vocabulary

When reviewing a Phase 4 Step 2 split with per-proposed-episode tensometer data, the categories you raise alongside taste verdicts:

- `RUNG-DISTRIBUTION-FLATLINE-{line-range}` — a long contiguous rung-1 run with no rung-2 inflection is the world going slack. The dark register requires consequence to propagate; a flat tens-distribution stretch is hostility that stopped pushing back. Flag the line range where the run begins to where rung-2 finally inflects (or where the stretch ends without inflecting).
- `FALSE-PEAK-{line}` — a tens=3 beat with no rung-2 precursor in the preceding ~5 bones is a darkness asserted, not built. Catharsis-not-earned in single-line form. Flag the peak line.
- `DENOUEMENT-FLAT-{episode}` — a post-peak window with zero tens=3 and zero board-changes is catharsis-deferral becoming catharsis-avoidance — the cost stops being legible as cost. Flag the episode slug.
- `RUNG-CLUSTER-OVERSATURATION-{line-range}` — multiple tens=3 adjacent without release is darkness shouted, not earned. The world cannot be only-peak; the reader's exhale needs space to land. Flag the line range of the cluster.
```

---

## Edit 2 — `active-project/audience/pulp-enthusiast/card.md`

**Append to body, after `season_scope_adversarial:` block:**

```
## Tens-attack vocabulary

When reviewing a Phase 4 Step 2 split with per-proposed-episode tensometer data, the categories you raise alongside taste verdicts:

- `RUNG-DISTRIBUTION-FLATLINE-{line-range}` — a long contiguous rung-1 run with no rung-2 inflection is the toll exceeding what the payoff returns. Momentum is net-negative across the stretch. Flag the line range from where the flat run begins to where rung-2 finally inflects.
- `FALSE-PEAK-{line}` — a tens=3 with no rung-2 setup in the preceding ~5 bones is the punch without the windup. The reader sees the impact line and feels nothing, because the body didn't load up. Flag the peak line.
- `DENOUEMENT-FLAT-{episode}` — a post-peak window with zero tens=3 and zero board-changes is aftermath-drift in its purest form: the world handling what the peak did, instead of the peak doing more. Flag the episode slug.
- `RUNG-CLUSTER-OVERSATURATION-{line-range}` — multiple tens=3 adjacent without release is the climax repeating itself. Reads as the writer not knowing where to stop, or stacking peaks because each one didn't quite land. Flag the line range of the cluster.
```

---

## Edit 3 — `active-project/audience/worm-canon-pedant/card.md`

**Append to body, after `season_scope_adversarial:` block:**

```
## Tens-attack vocabulary

When reviewing a Phase 4 Step 2 split with per-proposed-episode tensometer data, the categories you raise alongside taste verdicts:

- `RUNG-DISTRIBUTION-FLATLINE-{line-range}` — a long contiguous rung-1 run with no rung-2 inflection is operational-calculus erosion at the bone level. Canon-Taylor's tactical register requires inflection beats; their absence flattens into generic-character behavior. Flag the line range.
- `FALSE-PEAK-{line}` — a tens=3 with no rung-2 precursor in the preceding ~5 bones is a state-change asserted without operational tracking. Canon-Taylor would not register a peak that lacks a setup; the response-bone discipline requires the precursor. Flag the peak line.
- `DENOUEMENT-FLAT-{episode}` — a post-peak window with zero tens=3 and zero board-changes following a named state-change (apprentice-mark, surveillance-record, debt, shard-event) is the operational-tracking gap. Information-asymmetry tracking demands response-bones; their absence breaks canonical character behavior. Flag the episode slug.
- `RUNG-CLUSTER-OVERSATURATION-{line-range}` — multiple tens=3 adjacent without release is shard-load mis-calibration. Canon distinguishes cost-bearing-peak from peak-stack; the cluster cannot stop carrying cost-signal or the distinction collapses. Flag the line range.
```

---

## Edit 4 — `.claude/commands/and-season.md` brief reduction (Phase 4 Step 2, ~line 327)

**Replace the inlined block** (the four bullet entries under "Tens-attack categories the persona may raise (carried in the dispatch brief until promoted to persona-card body in Phase 1.5):"):

- Old: four bullets enumerating `RUNG-DISTRIBUTION-FLATLINE`, `FALSE-PEAK`, `DENOUEMENT-FLAT`, `RUNG-CLUSTER-OVERSATURATION`.
- New: single line — "Consult your persona card's `## Tens-attack vocabulary` section. The categories (`RUNG-DISTRIBUTION-FLATLINE-{line-range}`, `FALSE-PEAK-{line}`, `DENOUEMENT-FLAT-{episode}`, `RUNG-CLUSTER-OVERSATURATION-{line-range}`) are defined per-persona in your card body; raise them with persona-specific reasoning. Promotion landed Plan A A1, 2026-05-10."

---

## Verification (post-apply)

1. `grep -c "Tens-attack vocabulary" active-project/audience/*/card.md` → 3 (one per persona file).
2. `grep -c "RUNG-DISTRIBUTION-FLATLINE\|FALSE-PEAK\|DENOUEMENT-FLAT\|RUNG-CLUSTER-OVERSATURATION" .claude/commands/and-season.md` → 1 (the single-line reference; was previously 4 bullets ≈ 4+ hits).
3. The brief at Phase 4 Step 2 no longer enumerates the categories inline.
