# Sensory-Flags Facet Tuning — Final Package

End-to-end pipeline run for the **sensory-flags** facet (renamed from "loudness"; the schema's loudness definition was a misnomer), applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md`. Run 2026-05-07.

**Headline:** locked V1 rubric (with six user-supplied requirements absorbed pre-Phase-0 and early-Phase-0) + studio writer-fork (state-update-aligned delta shape, two-pass author) + mechanic auditor (single-gate, no dialect audience) produces a co-deployable pipeline at **5/5 = 100% mechanic** on s01e01 (77 beats), without requiring any mid-Phase-4 rubric retune. The disambiguation-not-redundancy framing (the user's load-bearing pre-Phase-0 nudge) plus the two-question defensibility gate (Q1 audience-without-flag + Q2 magnitude-large-enough) plus the tensometer-independence rule together produce a frugal-by-design facet that disambiguates bare environmental language without redundantly intensifying language that already self-carries weight.

This is the **first facet whose rename was substantive.** The schema's "loudness flags" definition (sound-only, `<up|down|spike|drop>` tag-set) was generalized to "sensory flags" covering seven modalities (sound / light / smell / thermal / humidity / pressure / tactile) with state-update-aligned `<modality>: <old> -> <new>` delta shape. Schema update (caveat-004) ships in same commit.

---

## Trajectory

| Round | Stage | Author / Reviewer | Result | Notes |
|---|---|---|---|---|
| 0 | Corpus + V1 rubric | — | rubric authored with 4 axes (modality-inflection, disambiguation-discipline, magnitude-sufficiency, audience-side-perceptibility) | corpus stratifies 77 beats by modality × bare/charged × tens-zone (correlative) |
| 1 V1 | Lenient form review of naive baseline | mechanic | 12/12 = 100% | form is easy to satisfy |
| 1 V2 | Strict review of naive baseline | mechanic | **4/12 = 33.3%** | baseline-to-beat; 6 systemic faults named (sustained-as-inflection, sub-threshold-magnitude, density-on-charged-tens, fauna-feed-extension, charged-word-redundancy, no-modality-fire) |
| 2 mech | Writer-fork output (rubric-aware, blind to baseline) | mechanic | **5/5 = 100%** | +66.7pp; SHAPE-OK with sparsity-upper-edge notation |
| 3 | Adversarial seams | hostile-mode | 5 STRONG + 2 MOD per-entry + curve-STRONG + cross-facet-MOD + disambiguation-STRONG | seam-5 (@72 magnitude) load-bearing |
| 4 | Defense or revise | writer-fork | 1 revise (@41 naming) + 4 defends + structural decision (per-season modality-coverage) + cross-facet annotation | no mid-Phase-4 user nudges; Phase 0 absorbed all six tightenings |
| 5 mech | Final adjudication | mechanic | **5/5 = 100%** | SHIP with caveats 1-5 |

**Lift from V2 baseline: 33.3% → 100% = +66.7pp.**

| Facet | Baseline V2 | Final | Lift |
|---|---|---|---|
| dialogue | 40% | 100% | +60pp |
| loc-state | 53.8% | 100% | +46.2pp |
| tensometer | 50.6% | 100% | +49.4pp |
| narrator-interest | 22.2% | 100% | +77.8pp |
| state-updates | 6.7% | 100% | +93.3pp |
| memory-flags | 19.0% | 100% | +81.0pp |
| **sensory** | **33.3%** | **100%** | **+66.7pp** |

Sensory's baseline is the highest in the run-set (33.3%) because the schema-blind naive author lands four obvious sound-fires (@13, @24, @30, @41) by sound-following discipline alone. The contamination concentrates at the sub-threshold / sustained / fauna-feed-extension / charged-word edges — exactly where the V1 rubric's two-question defensibility gate does its load-bearing work. The lift (66.7pp) is the smallest in the run-set despite a clean ship; the smaller lift reflects the higher baseline, not weaker rubric.

---

## What the user-supplied requirements added

### Pre-Phase-0 nudges (handoff message + early Phase 0)

The user supplied four rubric-shaping nudges before authoring:

1. **Rename: sensory-flags.** "loudness" was a misnomer — the facet captures cross-modal sensory inflection (lightning, thunder, smells, temperature, humidity, pressure), not just sound. Schema update pending (caveat-004).

2. **Independent of tensometer.** Sensory-flags do not gate on tensometer ≥ 2. Fires may occur in any tens-zone. Tens-correlation is observation, not gating. **This is the inverse of memory-flags' inverted-tens-density rule** — sensory-flags inherits no tens-discipline from tensometer.

3. **Closer to state change flags.** Sensory-flags adopts state-updates' delta shape `<target>: <old> -> <new>` generalized to `<modality>: <old> -> <new>`. Both facets are studio-authored (sensory entirely; state-updates partially); both record changes in environmental/perceptual state. Distinct: state-updates writes back to canonical memory; sensory does not (selection signal only).

4. **Disambiguation-not-redundancy.** "thunder is booming loud, yes everyone knows, the word thunder carries all the weight on its own. blistering wind is required to separate just wind into something that swelters." The load-bearing rubric framing: sensory-flags fire where the proto-line word is *bare* and the audience needs the flag; refuse where the proto-line word is *charged* and self-carries.

### Early Phase-0 nudges

5. **Frugal, no more than 3 a scene.** Per-scene cap ≤ 3 (hard, not guideline). Most scenes carry 0-1 fires; 2-3 reserved for confrontation-class scenes with multiple genuine cross-modal inflections.

6. **Two-question defensibility gate.** Every flag needs justification answering: Q1 — would the audience know the difference WITHOUT the flag? Q2 — is the difference LARGE ENOUGH to justify a flag? Both AND-gate; default is silence.

### Pattern: pre-Phase-0 vs mid-Phase-4 absorption

This run absorbed all six user requirements before Phase 1 authoring (Phase 0). Memory-flags absorbed five user requirements *mid*-Phase-4 with Phase 4 re-run. Both worked; Phase 0 is preferred when the user's framing is available pre-authoring (cleaner trajectory, no re-run needed). Mid-Phase-4 absorption works when the framing emerges through the tuning process; the pipeline tolerates it cleanly via Phase 4 re-run.

The Phase 0 absorption reduced sensory's run-cost vs memory-flags' run-cost by one Phase 4 iteration. **Recommendation for future facets: front-load user-rubric-tightenings to Phase 0 when possible.**

---

## What worked

1. **State-update-aligned delta shape.** `<modality>: <old> -> <new>` mirrors state-updates' `<target>.<field>: <old> -> <new>` cleanly. Pattern transfer landed at the form level — the writer-fork's two-pass authoring (per-beat then file-shape) inherited cleanly from state-updates' studio component. The single change (target → modality) honors the user's "closer to state change flags" framing.

2. **Two-question defensibility gate is the rubric's load-bearing test.** Q1 (audience-without-flag = bare-not-charged) + Q2 (magnitude-large-enough). The naive baseline failed predominantly on these two axes — sub-threshold magnitudes (@57, @64, @67) and charged-word redundancy at the @58 edge. The Q1+Q2 gate strips them cleanly. The rubric exemplars (thunder = charged; blistering wind = bare-needs-flag) calibrate the gate at exactly the user's intended discipline.

3. **Tensometer-independence is the right structural relationship.** Sensory inflections may correlate with high-tens beats (rupture, peak) but do not require it. The s01e01 file demonstrates the distribution: t=1 fires (@13, @41, @72), t=2 fire (@30), t=3 fire (@24). Three of five fires are NOT at peaks; the gating-on-tens rule (which would have applied if sensory inherited memory-flags' tens-discipline) would have stripped @13 and @72, killing the file's establishment fire and modality-coverage fire. The user's tensometer-independence call is structurally load-bearing.

4. **Per-scene cap ≤ 3 with one-modality-prefer rule.** Hard frugality discipline. Scene 2 (confrontation) lands at exactly the cap (3 fires); other scenes well under. The cap forces selection across competing fires when scenes are inflection-rich; sound-only-scene-2 plus tactile-scene-4 honors modality-diversity-prefer-over-modality-repeat without inflating the cap.

5. **Mechanic-only single-gate review (no dialect audience) preserves precedent.** Sensory is studio-authored, environmental, voice-light. The description names a perceptual cue, not character voice. Same precedent as state-updates and loc-state. The mechanic auditor handles modality-correctness, Q1+Q2 defensibility, sustained-vs-inflection, audience-side-perceptibility, and cross-facet contracts. No dialect-audience scope creep into mechanic-domain adjudication.

6. **Modality-coverage health-check produces structural finding.** s01e01's natural inflection density does not honor both per-episode sparsity (3-6%) and per-episode modality-coverage (≥2) at the same time without overshooting band by 0.5pp. The Phase 4 structural decision (yield on per-episode modality-coverage; treat as per-season tracking) mirrors memory-flags' single-register-per-episode + per-season-tracking finding. **Result: per-season modality-coverage tracking caveat across s01e01-e06.**

7. **Modality-specific old-state convention transfers cleanly.** The Phase 4 Seam-3 defense established the principle: old-state names the most-recent **modality-specific** audible state, not the broader scene state. This makes inflection-pair coherence (@24 drop / @30 up) traceable on a per-modality channel. Convention will transfer to multi-modal episodes (where multiple modalities fire in sequence and need to be tracked independently).

8. **Cross-facet annotation pattern (deviation from locked-upstream).** Locked tens contract names @64 as sensory anchor-expected; sensory rubric Q2 strips it on sub-threshold magnitude. The deviation is annotated in shipped sensory frontmatter rather than amending the locked tens contract. Pattern: when a downstream facet's locked rubric contradicts an upstream facet's locked anchor-expectation, prefer annotation over upstream amendment if the upstream language already admits deviation ("anchor-expected" not "anchor-required"). This pattern will transfer to other facets that may surface similar cross-facet expectation conflicts.

9. **Frugal-by-design facet shipping at upper-edge of band.** 6.5% vs 3-6% band is honest revision per facet-tuning-process precedent (tensometer's 2-rung soft-fail at 15.6% vs 20-30% band shipped with notation). Per-fire ceiling-defense is the test that matters; band is target-not-hard. The structural conflict between sparsity and modality-coverage at this episode's natural inflection density yielded on sparsity (0.5pp overshoot) rather than on modality-coverage (1-modality monoculture).

---

## Residual caveats (from Phase 5)

1. **Caveat-001 (advisory; per-season tracking):** Per-season modality-coverage. s01e01 lands 2 modalities (sound + tactile). Season-level expectation: ≥3 modalities across s01e01-e06. Future episodes should bring light, smell, thermal, humidity, or pressure entries.

2. **Caveat-002 (cross-facet annotation):** Locked tens @64 anchor-expectation deferred (Q2 sub-threshold magnitude; correlative-not-gating per V1 rubric). Deviation annotated in shipped frontmatter; locked tens contract not amended.

3. **Caveat-003 (sparsity at upper-edge):** File ships at 6.5% vs 3-6% band. Honest-revision; per-fire ceiling-defense holds.

4. **Caveat-004 (schema rename — mandatory pre-s01e02):** `schemas/facet.schema.md` § "loudness flags" requires update before s01e02 sensory authoring. Required edits:
   - Rename section to "sensory flags".
   - Update file path `facets/loudness.md` → `facets/sensory.md`.
   - Update content shape `<up|down|spike|drop> <one-clause description>` → `<modality>: <old-state> -> <new-state>` with optional `# tag: <up|down|spike|drop>` annotation.
   - Add modality enumeration (sound / light / smell / thermal / humidity / pressure / tactile).

5. **Caveat-005 (process; rubric tightening at Phase 0 vs mid-Phase-4):** Six user-supplied rubric tightenings absorbed pre-Phase-0 and early-Phase-0. Contrast: memory-flags absorbed five mid-Phase-4 with Phase 4 re-run. Both work; Phase 0 is preferred when user's framing is available pre-authoring (cleaner trajectory, no re-run cost). Pattern note: front-load user nudges to Phase 0 in future runs when possible.

---

## What needs doing next (if continuing)

1. **Schema rename (caveat-004).** Update `schemas/facet.schema.md` § "loudness flags" to § "sensory flags" with new content shape and modality enumeration. Mandatory pre-s01e02 sensory authoring.

2. **Pilot sensory on s01e02 or s01e03 for stretch-sample.** Verify the 3-6% band scales (likely stays sparser); verify per-season modality-coverage starts to land (light, smell, thermal, humidity, pressure inflections may surface in different episode-scenes).

3. **Pilot the next facet in sequence.** Open candidates per the original sequence:
   - **feeling flags** (non-POV character writer-fork). Higher complexity; pattern transfer from state-updates' actor-fork pattern to a free-text-content variant. Tests whether two-question defensibility gate (Q1 audience-without-flag) applies to non-POV interior content.
   - **metaphor** (editor-authored at stitch-time; downstream of memory-flags + sensory-flags). Tuning would validate the licensing-layer contract from the consumer side: every shipped metaphor must co-cite a memory-flag fire (mandatory per memory-flags) and *may* co-cite a sensory-flag fire (permitted per sensory). Capstone facet.
   - **vibes-updates** (showrunner-authored; cross-cutting). Different shape from per-beat facets; likely different five-phase shape.
   - **audience interest-flags (per-persona)** (one file per audience persona; requires three persona cards active). High coupling to project audience.

4. **Retroactive evaluation of memory-flags gates against earlier facets (caveat-005 from memory-flags).** Still deferred until metaphor-tuning surfaces a concrete co-citation problem. Sensory tuning did not surface NI co-citation issues (sensory is independent of NI), so the deferral remains valid.

5. **Address residual caveats.** Schema rename (caveat-004 — mandatory); per-season modality-coverage tracking (caveat-001 — advisory); sparsity-upper-edge notation (caveat-003 — applied); cross-facet @64 annotation (caveat-002 — applied); rubric-tightening-phase finding (caveat-005 — process advisory).

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-sensory.md` (V1 LOCKED 2026-05-07; six user-supplied requirements absorbed Phase 0)
- Schema: `schemas/facet.schema.md` (sensory section — rename pending caveat-004)
- Process doc: `design/shoot-v2/facet-tuning-process.md`
- Cross-facet authorities: `active-project/theater/facets/location-state.md` (locked; old-state baseline match), `active-project/theater/facets/tensometer.md` (locked; correlative-not-gating)

### Phase 0
- Corpus selection: `design/shoot-v2/sensory-corpus.md`
- V1 rubric: `design/shoot-v2/rubric-sensory.md`

### Phase 1
- Naive baseline (rubric-blind): `design/shoot-v2/phase1-sensory-baseline-naive.md`
- V1 lenient + V2 strict review: `active-project/staff/auditor/phase1-sensory-baseline-review.md`

### Phase 2
- Writer-fork output: `design/shoot-v2/phase2-sensory-output.md`
- Mechanic audit: `active-project/staff/auditor/phase2-sensory-audit.md`

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-sensory-seams.md`

### Phase 4
- Defense / revise: `design/shoot-v2/phase4-sensory-defense.md`

### Phase 5
- Final adjudication: `active-project/staff/auditor/phase5-sensory-final.md`

### Shipped
- Locked sensory facet: `active-project/theater/facets/sensory.md` (s01e01, 5 entries, READY-WITH-CAVEATS)

### This package
- `design/shoot-v2/sensory-tuning-package.md`

---

## Co-deployment note

Per dialogue, loc-state, tensometer, narrator-interest, state-updates, and memory-flags packages: writer + reviewer ships as a co-deployed unit. For sensory, the unit has two components reflecting the simpler review architecture (single-gate, no dialect audience):

- **Writer:** studio writer-fork. Loads: locked location-state file (old-state baseline), locked tensometer file (correlative observation only — NOT gating), proto-lines file, the V1 rubric, the corpus-selection note. Two-pass authoring: per-beat → file-shape audit. Per-beat decisions evaluate the four-axis rubric (modality-inflection + disambiguation-discipline + magnitude-sufficiency + audience-side-perceptibility) under the two-question defensibility gate (Q1 audience-without-flag + Q2 magnitude-large-enough). File-shape audit verifies sparsity (3-6%, target-not-hard), modality-coverage (≥2 per episode, ≥3 per season), bare-not-charged, sustained-vs-inflection, inflection-pair coherence, per-scene cap ≤3.

- **Reviewer (mechanic auditor):** single mechanic auditor with the rubric as authority. Per-entry verdicts (CORRECT / INCORRECT-{axis-or-anti-pattern}); per-skip verdicts (SKIP-CORRECT / SKIP-MISSED); curve verdict (SHAPE-OK / SHAPE-FAIL); cross-facet contract pre-ship check (loc-state baseline match; tens correlation observation; independence from NI/memory-flags/state-updates). No dialect audience invoked.

- **Adversarial pass (Phase 3):** same mechanic auditor in hostile mode, one strongest seam per entry plus one curve-level seam plus cross-facet seam plus disambiguation-layer integrity seam. Catches what passes naive mechanic review.

The two parts (writer + mechanic) are not separable. The writer's affirmative-citation discipline (multi-justification under Q1+Q2) only works because the mechanic auditor tests citations. The mechanic auditor's strict rubric is only meaningful because the writer can produce entries that survive multi-justification ceiling-defense. The adversarial pass surfaces what passes naive review.

The dialect audience is **NOT** part of the sensory pipeline — sensory is studio-authored, environmental, voice-light. Per state-updates / loc-state precedent, dialect audience is not invoked for facets whose descriptions name perceptual / environmental cues rather than character voice. Same architecture as those two facets.

The Phase 0 absorption of all six user-supplied rubric tightenings is the structural addition for this facet relative to memory-flags' mid-Phase-4 absorption pattern. The pipeline tolerates either timing; pre-Phase-0 absorption is cleaner (no re-run cost).
