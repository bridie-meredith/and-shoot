# Tournament Scorecard Schema

Schema for per-scene scorecards emitted by `/and-stitch` Phase 1.5 Step 3 (cherry-pick scorer). Scorecards accumulate as the tuning signal — admin process-critic reads accumulated scorecards to detect rubric mis-calibrations and feed back to upstream gates.

**File location:** `active-project/staff/reviews/scorecard-<book>-<chapter>-scene-<scene-label>-<timestamp>.md`
**Aggregate ledger:** `active-project/staff/showrunner/tournament-scorecards.md` (append-only; one row per scene per chapter)

---

## Per-scene scorecard format

YAML frontmatter + structured markdown body. Required fields:

```yaml
---
schema: schemas/tournament-scorecard.schema.md
book: <book-slug>                    # e.g. b01
chapter: <chapter-slug>              # e.g. b01-c02
scene: <scene-label>                 # e.g. A, B, C
scored_at: <iso-timestamp>           # YYYY-MM-DDTHH:MM:SSZ
scorer_dispatch: phase-1.5-step-3-cherry-pick-scorer
source_draft_path: <relative-path>   # path to the assembled cherry-pick scene draft
n_arms: <integer>                    # 1 = single-arm collapse; 2+ = multi-arm
ceiling_collapse: <true|false>       # true when Step 2 made 0 substitutions
---

# Cherry-pick scorecard — <book>-<chapter> scene-<scene-label>

## Scene-level score

reward_score: <integer>              # sum of REWARD hit_counts
peeve_weight_sum: <integer>          # sum over PEEVES of (fire_count × severity_weight)
scene_score: <integer>               # reward_score − peeve_weight_sum
voice_consistency: <seamless | minor-seam | flag-seam>

## PET PEEVE fires

| # | Peeve | Severity | Fire count | Anchor sentences |
|---|-------|----------|------------|------------------|
| 1 | theme-as-statement | strong | <N> | "<quote>" |
| 2 | heavy-handed-metaphor | strong | <N> | "<quote>" |
| 3 | symbolic-relationships | strong | <N> | "<quote>" |
| 4 | setting-dressing-as-meaning | soft|strong | <N> | "<quote>" |
| 5 | compound-noun-saturation | strong | <N> | "<quote>" |
| 6 | metronome-tic-regularity | strong | <N> | "<quote>" |
| 7 | repetition-as-cadence-when-verbs-run-out | strong | <N> | "<quote>" |
| 8 | gestured-at-recognition | strong | <N> | "<quote>" |
| 9 | protagonist-arc-cost-not-legible | walkout | <N> | "<quote>" |

All 9 rows MUST appear even when fire_count = 0 (the absence-of-fire is itself signal).

## REWARD hits

| # | Reward | Hit count | Anchor sentences |
|---|--------|-----------|------------------|
| 1 | person-in-voice | <N> | "<quote>" |
| 2 | embodied | <N> | "<quote>" |
| 3 | sensory-grounded | <N> | "<quote>" |
| 4 | variance-in-sentence-length | <N> | "<quote>" |
| 5 | quiet-lines-carrying-scenes | <N> | "<quote>" |
| 6 | setup-payoff-recognizable-not-announced | <N> | "<quote>" |
| 7 | restraint-and-confidence | <N> | "<quote>" |
| 8 | bone-faithfulness | <N> | "<quote>" |
| 9 | reader-orientation | <N> | "<quote>" |

All 9 rows MUST appear.

## Voice-consistency notes

<2-4 sentences. Name specific paragraph transitions if a seam is detected.>

## Tuning signal flags (for admin process-critic)

- peeves-firing-on-every-arm: [<peeve-slug>, ...]
  # peeves the per-scene tournament verdicts noted as firing across ALL arms — indicates
  # rubric-criterion-too-broad OR bones-authoring-producing-failure-for-every-prime
- rewards-no-arm-hit: [<reward-slug>, ...]
  # rewards that scored 0 across this scorecard despite scene having room — indicates
  # rubric-measuring-something-rendering-cannot-produce
- cherry-pick-source-concentration: <rubric-slug | n/a>
  # if Step 2 made substitutions: the rubric dimension that drove most of them
- ceiling-collapse-context: <pure-winner-already-paragraph-optimal | n-equals-1-no-op | n/a>
```

---

## Severity weights (numeric)

For computing `peeve_weight_sum`:

| Severity | Weight |
|----------|--------|
| blocker  | 10     |
| walkout  | 5      |
| strong   | 2      |
| soft     | 1      |

The weights are calibrated such that:
- One walkout-severity fire (cost-not-legible, blocker) outweighs two strong fires
- One blocker fires outweighs five strong fires
- Soft fires accumulate; one soft fire is noise, three soft fires of the same peeve approach a strong

The absolute `scene_score` number is less meaningful than:
1. Its delta across scenes within a chapter (intra-chapter consistency)
2. Its delta across chapters at the same scene position (inter-chapter trend)
3. The PEEVE/REWARD count distribution (where the score is coming from)

---

## Chapter-aggregate ledger format

`active-project/staff/showrunner/tournament-scorecards.md` is an append-only markdown table. One row per scene per chapter per stitch run:

```markdown
# Tournament Scorecards — append-only ledger

Schema: schemas/tournament-scorecard.schema.md (per-row fields summarized below)

| Chapter | Scene | Scored at | N arms | Ceiling collapse | Scene score | Reward score | Peeve weight | Voice consistency | Phase 9 verdict | Phase 9 continue | Scorecard path |
|---------|-------|-----------|--------|------------------|-------------|--------------|--------------|-------------------|-----------------|------------------|----------------|
| b01-c02 | A | 2026-05-27T... | 2 | true | <N> | <N> | <N> | seamless | PASS-WITH-CAVEATS | no | staff/reviews/scorecard-b01-c02-scene-A-<ts>.md |
| b01-c02 | B | 2026-05-27T... | 2 | false | <N> | <N> | <N> | minor-seam | PASS-WITH-CAVEATS | no | ... |
| b01-c02 | C | 2026-05-27T... | 2 | true | <N> | <N> | <N> | seamless | PASS-WITH-CAVEATS | no | ... |
```

The Phase 9 fields are filled in after Phase 9 completes (Phase 9.6 step writes the back-reference into the ledger row that Phase 1.5 Step 3 created).

---

## Reading the scorecards

**Per-chapter (one stitch run):** scan the 3+ scene rows. Look for:
- Consistent peeve-fires on the same peeve across scenes → upstream bones issue
- Wildly different scene scores within a chapter → uneven cherry-pick lift (some scenes had room, others didn't)
- Voice-consistency degradation across scenes → cherry-pick is over-mixing arms

**Cross-chapter (5+ stitch runs):** scan the ledger. Look for:
- Same peeve at the top fire-count for every chapter → rubric criterion needs re-calibration OR upstream gate gap
- Same reward at hit-count 0 for every chapter → rubric measuring something the layer can't produce
- `ceiling-collapse: true` on >50% of scenes → multi-arm setup not differentiating arms enough; exemplar selection issue at Phase 0 step 4a
- Voice-consistency `flag-seam` correlating with Phase 9 cold-read FAIL → tighten composer tonal-seam fence

**Cross-chapter / Phase-9-correlation:**
- Phase 9 cold-read FAILs that correlate with low `reader-orientation` hits → RW9 is doing real predictive work; consider promoting to a primary discriminator
- Phase 9 FAILs that DON'T correlate with any scorecard signal → the rubric is blind to the failure mode; surface to admin process-critic for a rubric-gap proposal

---

## Schema versioning

This schema is at v1 (2026-05-27 initial). Future revisions should:
1. Preserve all v1 fields (don't break existing scorecards)
2. Add new fields under a `v<N>_extensions:` block in frontmatter to keep parsers backwards-compatible
3. Document the version bump rationale here

The PEEVE and REWARD lists themselves are versioned by `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md`. The scorecard format references those lists by name — if a peeve or reward is added/removed in the rubric, the scorecard table grows/shrinks rows accordingly. The schema enforces "all current peeves/rewards represented" not "exactly 9 peeves and 9 rewards."

---

## Provenance

- 2026-05-27 — v1 — initial schema. Drawn from the b01-c02 cherry-pick experiment evidence: the cherry-pick captured paragraph-level lift the pure-winner could not (scene-B substitutions); the cold-read still returned CONTINUE=no; the pet-peeve audit fired protagonist-arc-cost-not-legible (walkout) + symbolic-relationships (strong) + setting-dressing-as-meaning (strong recurrence). The scorecard formalizes that audit into a per-scene structured artifact so the signal accumulates rather than evaporating after each run.
