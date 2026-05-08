# Vibes-Updates Facet Tuning — Final Package

End-to-end pipeline run for the **vibes-updates** facet (the cross-cutting showrunner-authored bias-layer facet — distinct in shape from the nine prior per-beat facets). Run 2026-05-07, applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md` with structural adaptations for showrunner-cross-cutting authorship.

**Headline:** locked V1 + V1.1 patch (with six user-supplied requirements absorbed pre-Phase-0) + single showrunner fork + mechanic-only audit (no dialect audience) produces a co-deployable pipeline at **12/12 = 100%** mechanic on s01e01 (77 beats), with five residual caveats (none blocking). Schema content-shape revision shipped same commit (formal entity-target slugs added; `licensed-by:` field formalized; `++` op introduced; sentence-parsability AP8 test formalized).

**Lift:** 0/29 = 0% (Phase 1 V2 strict baseline) → 12/12 = 100% (Phase 5). **+100pp**, ties feeling-flags and metaphor-flags as largest absolute lift in the run-set.

This is the **first cross-cutting / showrunner-authored facet** tuned — distinct in shape from the nine prior facets (all per-beat-anchored, all studio/dialogue-writer-fork/editor-authored). The Phase 3 RF-001 finding (world-build pre-load tension) is the load-bearing structural finding: **pre-seeded vibe-clouds force `++`-or-skip op behavior on pre-loaded keywords on all targets including episode/season/series scope.** This principle generalizes: any future facet that consumes pre-seeded artifact-state must apply the same op-coherence reading.

---

## Trajectory

| Round | Stage | Author / Reviewer | Result | Notes |
|---|---|---|---|---|
| 0 | Corpus + V1 rubric | — | rubric authored with 6 user nudges absorbed pre-Phase-0: vibes are permanent (not drifting) / entity-targets primary / off-screen-licensed valid / liberal sparsity / not rendered in prose / machine-readable word-algebra (not human prose) | corpus assumed clean-slate (16 expected fires); pre-loaded clouds not consulted at corpus-time (Phase-0 oversight surfaced at Phase 2) |
| 1 V2 strict | Naive baseline review | mechanic | **0/29 = 0%** | rubric-blind showrunner authored 29 entries on 16 beats using schema-current text; six systemic faults named (licensed-by absent universally + entity-targets absent + duplicate-adds throughout + content-shape malformed + scope-only authoring + beat-anchor scatter) |
| 2 fork | Rubric-aware showrunner fork blind to Phase 1 | mechanic | **6/11 = 54.5%** | +54.5pp; SHAPE-OK; correctly enforced gate-2 on actor targets (pre-load → `++`-or-skip); MISSED gate-2 on episode-scope (5 episode `+` entries duplicated EPISODE_1_VIBES pre-load); RF-001 surfaced |
| 3 | Adversarial seams | hostile-mode mechanic | 7 cross-cutting seams + per-entry seams | RF-001 escalated to load-bearing; STRICT/RELAXED/HYBRID readings argued; SEAMS 2-7 surfaced |
| 4 | Defense or revise + rubric V1.1 patch | showrunner | 12 final entries (3 DEFEND + 3 REVISE + 2 DELETE + 4 NEW) + V1.1 patch (4 edits: gate-2 pre-seed clause + AP8 sentence-parsability + AP11 string/semantic split + cross-facet pre-render clause) | RF-001 resolved as STRICT; corpus addendum authored; V1.1 ships same commit |
| 5 | Final adjudication | mechanic | **12/12 = 100%** | SHAPE-OK; 5 residual caveats; SHIP-WITH-CAVEATS; read-side coherence verified |

**Lift from V2 baseline 0/29 = 0% to Phase 5 strictly-clean 12/12 = 100%: +100pp.** Ties feeling-flags + metaphor-flags as largest absolute lift in the run-set.

| Facet | Baseline V2 | Final | Lift |
|---|---|---|---|
| dialogue | 40% | 100% | +60pp |
| loc-state | 53.8% | 100% | +46.2pp |
| tensometer | 50.6% | 100% | +49.4pp |
| narrator-interest | 22.2% | 100% | +77.8pp |
| state-updates | 6.7% | 100% | +93.3pp |
| memory-flags | 19.0% | 100% | +81.0pp |
| sensory | 33.3% | 100% | +66.7pp |
| feeling | 0% | 100% | +100pp |
| metaphor | 0% | 100% | +100pp |
| **vibes** | **0%** | **100%** | **+100pp** |

Three 0%-baseline facets in a row (feeling / metaphor / vibes). All three: schema-current-text-only baselines produce output strict-rubric reviewers reject completely. For vibes specifically, the schema-current `<scope>:<key> <op> <value>` form does not surface the `licensed-by:` requirement, the entity-target option, or the cross-target fan-out gate; the rubric-blind showrunner reasonably produced 29 entries that all fail gate 4 (licensed-by absent), gate 7 (fan-out skipped), AP9 (scope-only authoring), and AP5 (duplicate-adds throughout).

---

## What the user-supplied requirements added

### Pre-Phase-0 nudges (handoff message + first reframe + word-algebra clarification)

The user supplied **six rubric-shaping nudges** before Phase 0 dispatch, plus one mid-Phase-0 clarification on machine-readable form:

1. **Vibes are permanent stickers, not drifting tone-clouds.** Reframes the entire facet from event-anchored shifts to durable entity-tags. (Replaced the initial "trigger-event with `>>` gradual-op" framing.)

2. **Entity-targets primary; scope targets secondary.** Reframes the schema's episode/season/series scope as not the primary axis. Actors / locations / props are where vibes stick. The schema content-shape revision is therefore larger than metaphor's — not a field-add but a target-axis-change.

3. **Independent of screen time.** Off-screen / pre-episode / inter-episode reflective adds are valid. The schema must permit `@<proto-line-id>` to be optional.

4. **Liberal sparsity.** No upper ceiling. Vibes are not rendered in prose; cost-per-fire is structurally lower than any other facet.

5. **Not rendered in prose; bias the operators writing prose.** Reviewer competence is mechanic-only — no dialect audience. Vibes are not voice-bearing in the way NI/feeling/metaphor are. The mechanic checks form / op-coherence / licensed-by / fan-out / operator-bias-actionability.

6. **Machine-readable word-algebra, not human prose.** Tokens are hyphenated phrases, optimized for machine consumption by downstream operators. Prose tokens are AP8. Sentence-parsability is the formal test (V1.1 patch).

### Pattern: pre-Phase-0 absorption (sensory/feeling/metaphor pattern continues)

This run absorbed all six user requirements before Phase 1 authoring. Sensory absorbed six, feeling seven, metaphor eight, vibes six — all front-loaded. The schema-revision-at-ship pattern is now confirmed across **four facets** (sensory rename, feeling field-retirement, metaphor formal-content-shape-introduction, **vibes target-axis-change + op-extension**).

**Recommendation locked:** front-load user-rubric-tightenings to Phase 0 in future runs. Sensory + feeling + metaphor + vibes all confirm.

---

## What worked

1. **Schema-revision-at-ship pattern transfers and extends to cross-cutting facet.** Sensory shipped a §rename + content-shape revision. Feeling shipped a §field-retirement + scope-expansion. Metaphor shipped a §formal-content-shape-introduction (`licensed-by:` field). Vibes ships a **target-axis-change** (scope-only → entity-target-primary) + **op-extension** (`+/-/=` → `+/-/++` with `=` removed) + **anchor-optional** (`@<proto-line-id>` → `[@<proto-line-id>]`). Same commit lifecycle. Schema content-shape revision is the largest of the four.

2. **Refuse-by-default showrunner discipline holds for cross-cutting authorship.** The rubric-aware Phase 2 fork correctly refused to fire `+` on pre-loaded actor targets, hewing to gate 2 strictly. Phase 2 authored 11 entries (down from corpus-expected 16) — 6 correct, 5 INCORRECT. The 5 INCORRECTs were not contamination; they were extension of the gate-2 reasoning to actor targets only, missing episode-scope. Phase 4 closed the gap. The discipline held; it just needed one more application.

3. **RF-001 (world-build pre-load tension) is the load-bearing structural finding.** Analogous to metaphor's monument-scope determination: a hidden rubric premise surfaced at Phase 3 that retroactively governs op-coherence semantics. Three readings argued; STRICT committed. The V1.1 patch §1 makes the pre-seed behavior explicit. Generalizes: any future facet consuming pre-seeded artifact-state must apply the same op-coherence reading.

4. **AP8 sentence-parsability test (V1.1 patch §2).** Phase 3 SEAM 6 surfaced the prose-vs-word-algebra tension on long tokens (`the-door-she-can-open-after-the-machine-leaves` 9 segments). Phase 4 committed the formal test: parsability, not length. Long compressions structured as noun-phrase-with-modifiers PASS; sequences of independent clauses joined by hyphens FAIL. Generalizes to any future facet using hyphenated word-algebra tokens.

5. **AP11 formal/advisory split (V1.1 patch §3).** Phase 3 SEAM 4 surfaced string-overlap-vs-semantic-overlap tension on `++` extensions. Phase 4 committed: string-overlap is the formal mechanic gate; semantic-adjacency is an authoring advisory. Author may add comment-line justifying event-frame distinctness on borderline cases. Allows the rubric to be machine-checked while preserving authoring quality.

6. **Cross-facet pre-render clause (V1.1 patch §4).** Phase 3 SEAM 7 raised: do `++` extensions retroactively invalidate the locked s01e01 facets that license them? Phase 4 committed: NO. Locked upstream facets are content-layer authority; vibes-updates is operator-bias state. The two layers do not conflict. `++` extensions bias FUTURE renders (s01e02+); they do not alter the s01e01 record. This generalizes to any future bias-layer facet.

7. **Showrunner-as-author + mechanic-only-reviewer architecture worked cleanly.** No dialect audience needed. Vibes are read-side bias; voice-fidelity does not apply. The mechanic catches form / gates / AP-axes / fan-out / licensing. The single showrunner fork (cross-cutting visibility) is the licensing premise. No per-character forks (which would defeat the design).

8. **Pre-Phase-0 corpus oversight surfaced productively at Phase 2.** The corpus assumed clean-slate; Phase 2 fork hewed to gate 2 and exposed the assumption. Phase 4 documented the addendum. The pattern: Phase 0 corpus is a *target*, not authority; Phase 2-5 may legitimately revise corpus expectations against rubric-coherent reasoning. Generalizes: future facet runs should expect Phase 2-5 to potentially surface corpus oversights as Phase 4-revision priorities.

9. **The two NEW SKIP-MISSED additions (edric `++ the-yard-as-witness` + mira `++ the-yard-as-witness`) are textbook fan-out coherence wins.** Both are pre-loaded keywords; both license off existing somatic / state-update events; both add genuinely non-duplicate tokens at the operator-bias-distinct register. The edric add (state-update:9 sublocation-confirmation) is STRONG; the mira add (feeling:1 pre-positioning) is MODERATE. Both shipped.

---

## Residual caveats (from Phase 5)

Five items the auditor flagged before declaring shippable; all carried into the locked facet file's footer:

1. **Caveat-001 (rubric merge):** V1.1 patch text appends to main rubric file at this commit. Future auditor coherence depends on V1.1 being readable inline.

2. **Caveat-002 (margit referral, contingent):** `prop:oc-letter` has no card. Prop-level vibe entry deferred pending margit referral. Joins memory's monument list and state-updates' prop list.

3. **Caveat-003 (pre-seeded-project notation):** Sparsity 15.6% within addendum's pre-seeded expected range (9-14 for `++`-and-fresh-add subset). RF-001 STRICT reading. See V1.1 patch §1.

4. **Caveat-004 (showrunner write-back action):** 12 deltas to apply across 6 actor vibe-files + 1 loc card + studio EPISODE_1_VIBES section before s01e02 facet authoring. Specific target file map in facet file footer.

5. **Caveat-005 (read-side coherence — verified):** Phase 5 read-side check passed. `++` extensions do not retroactively invalidate locked s01e01 upstream facets. Per V1.1 patch §4 cross-facet pre-render clause.

---

## What needs doing next (if continuing)

Per the user's mid-run direction: vibes is the load-bearing facet for dialogue + behavior-pack character voice. After vibes ships, dependency-graph audit (deferred from prior runs) is next.

1. **Schema revision ALREADY APPLIED** (caveat-001 + part of vibes' core ship).

2. **Showrunner write-back (caveat-004).** The 12 delta entries must be applied to actor and studio vibe-cloud files at the cross-facet → stitch boundary, before s01e02 facet authoring begins.

3. **Dependency-graph audit.** Per user direction (recorded in `project_facets_next_steps.md` memory): explicit one-pass review of all ten facets + dialogue. What each currently uses vs should use. Surface gaps requiring re-tune vs cross-facet-note. Vibes' upstream/downstream contract is part of the audit input. Vibes consumes state-updates / memory / feeling / tens / proto / canon / world-build (read side); biases dialogue-writer / studio / NI / feeling / metaphor / behavior-pack (write side). The audit will likely surface that the eight prior facets implicitly assume vibes-as-upstream-signal but were tuned without explicit vibes-cite licensing.

4. **Audience interest-flags (TABLED).** Last remaining facet. Re-evaluated after dependency-graph audit and after new SVO writer artifacts land.

5. **New SVO writer artifacts incoming.** Parallel session producing new SVO files. When they land, evaluate whether vibes rubric (and other facet rubrics) generalize cleanly. Vibes specifically: its corpus is event-derived, not proto-line-shape-dependent; rubric should generalize.

6. **Address residual caveats.** Margit referral for prop:oc-letter (caveat-002 — joins memory's monument list); showrunner write-back (caveat-004 — applied at cross-facet → stitch boundary); rubric V1.1 merge (caveat-001 — applied this commit).

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-vibes.md` (V1 LOCKED 2026-05-07; V1.1 patch appended same file this commit)
- Schema: `schemas/facet.schema.md` § vibes updates (REVISED THIS COMMIT — content shape `<id> [@<proto-line-id>] <target> <op> <keyword>: [<token>, ...] | licensed-by: <source>[, ...]`; targets extended; `licensed-by:` formalized; `++` op introduced; sentence-parsability text added)
- Process doc: `design/shoot-v2/facet-tuning-process.md`
- V1.1 patch source: `design/shoot-v2/rubric-vibes-v1.1-patch.md`
- Cross-facet authorities: `active-project/theater/facets/state-updates.md`, `memory.md`, `feeling.md` (all locked; cited as `licensed-by:` sources)

### Phase 0
- Corpus: `design/shoot-v2/vibes-corpus.md` (16 reference fires; clean-slate assumption; surfaced as Phase-0 oversight at Phase 2)
- V1 rubric: `design/shoot-v2/rubric-vibes.md`

### Phase 1
- Naive baseline (rubric-blind): `design/shoot-v2/phase1-vibes-baseline-naive.md` (29 entries; scope-only; licensed-by absent universally)
- V2 strict review: `active-project/staff/auditor/phase1-vibes-baseline-review.md` (0/29 = 0%)

### Phase 2
- Showrunner fork output: `design/shoot-v2/phase2-vibes-output.md` (11 entries; 5 episode-scope INCORRECT due to RF-001)
- Mechanic audit: `active-project/staff/auditor/phase2-vibes-audit.md` (6/11 = 54.5%; RF-001 surfaced)

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-vibes-seams.md` (7 cross-cutting seams + per-entry; RF-001 escalated load-bearing)

### Phase 4
- Revised facet file: `design/shoot-v2/phase4-vibes-revised.md` (12 final entries; per-entry decisions documented)
- Rubric V1.1 patch: `design/shoot-v2/rubric-vibes-v1.1-patch.md` (4 edits)
- Corpus addendum: `design/shoot-v2/vibes-corpus-addendum.md` (clean-slate-vs-pre-seeded note)

### Phase 5
- Final mechanic adjudication: `active-project/staff/auditor/phase5-vibes-final.md` (12/12 = 100%; 5 caveats)

### Shipped
- Locked vibes facet: `active-project/theater/facets/vibes.md` (s01e01, 12 entries, READY-WITH-CAVEATS)
- Schema revision: `schemas/facet.schema.md` § vibes updates (THIS COMMIT)
- Rubric V1.1 merge: `design/shoot-v2/rubric-vibes.md` (V1.1 patch appended THIS COMMIT)

### This package
- `design/shoot-v2/vibes-tuning-package.md`

---

## Co-deployment note

Per dialogue, loc-state, tensometer, narrator-interest, state-updates, memory-flags, sensory, feeling, and metaphor packages: writer + reviewer ships as a co-deployed unit. For vibes-updates, the unit has THREE components reflecting the showrunner-author + mechanic-only-review architecture (notably distinct from metaphor's four-component hybrid):

- **Writer (single showrunner fork; refuse-by-default, cross-cutting visibility).** Loads V1 + V1.1 rubric + corpus + cross-facet locked files + ALL pre-loaded vibe-clouds (`actors/*/vibes.md`, `staff/studio/vibes.md`, location card VIBES sections). Two-pass authoring (per-event decisions across affected entities → file-shape audit). Per-event decisions evaluate: target-validity / op-coherence (against pre-loaded clouds — gate 2 critical) / licensed-by-resolvable / token-bundle word-algebra (AP8 sentence-parsability) / operator-bias-actionability / cross-target fan-out coherence. File-shape audit verifies per-target / per-op / per-anchor distribution against rubric expectations and pre-seed addendum.

- **Reviewer (mechanic auditor).** Single mechanic auditor with V1 + V1.1 rubric as authority. Per-fire verdicts (CORRECT / INCORRECT-{gate-or-AP} / REFUSE-CORRECT). Per-skip verdicts (SKIP-MISSED). File-shape verdict (SHAPE-OK / SHAPE-FAIL). Cross-facet contract pre-ship check (licensed-by resolution; pre-render hazard verification; pre-load coherence). NO dialect audience — vibes are not voice-bearing.

- **Adversarial pass (Phase 3).** Mechanic auditor in hostile mode. One strongest seam per fire; per-skip seams; cross-cutting seams (RF-001 / AP8 prose / AP11 string-vs-semantic / cross-facet pre-render / loc:-pre-load gap / multi-clause-token / SKIP-MISSED candidates). Catches what passes naive mechanic. The Phase 3 RF-001 escalation surfaced the load-bearing pre-seed structural finding — among the most consequential seams in the run-set.

The three parts (showrunner-fork + mechanic + adversarial-pass) are not separable. The showrunner's refuse-by-default discipline only works because the mechanic tests gate 2 strictly across all targets including pre-loaded scope. The mechanic's strict rubric is only meaningful because the showrunner can produce entries that survive RF-001 + AP8 sentence-parsability + AP11 string + AP12 fan-out challenges. The adversarial pass surfaces what the others accept.

The schema-revision-at-ship pattern is now confirmed across **four facets** (sensory + feeling + metaphor + vibes). The pipeline tolerates schema-revision-at-Phase-5 cleanly: the locked facet file uses the new shape; the schema text is revised in the same commit; the rubric § Locked notation flags the schema edit at Phase 0 so the schema change is anticipated by Phase 1. **Recommendation locked:** future facet tunings should evaluate at Phase 0 whether the schema content shape needs revision; if yes, ship in same commit as Phase 5 facet file.

The RF-001 (world-build pre-load) determination at vibes Phase 3-4 is the **second capstone-derived structural finding** that retroactively governs op-coherence across all targets (after metaphor's monument-scope determination). Specifically: any future facet consuming pre-seeded artifact-state must apply gate-2 op-coherence to all target classes including scope targets without exception. This finding generalizes beyond vibes and should be referenced in the facet-tuning process doc next time it is updated.

The AP8 sentence-parsability test + AP11 string-vs-semantic split + cross-facet pre-render clause (V1.1 patches §2-§4) generalize to any future facet using hyphenated word-algebra tokens, semantic-adjacency-aware extension ops, or downstream-bias write semantics. These are now reusable rubric components, not vibes-specific.
