# Feeling-Flags Facet Tuning — Final Package

End-to-end pipeline run for the **feeling-flags** facet, applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md`. Run 2026-05-07.

**Headline:** locked V1 rubric (with seven user-supplied requirements absorbed pre-Phase-0) + per-character writer-forks (taylor + mira + edric + officer-zero + clerk-zero) + mechanic auditor + dialect audience (hybrid review with independent gates) produces a co-deployable pipeline at **4/4 = 100% mechanic + 4/4 = 100% dialect** on s01e01 (77 beats), with seven residual caveats (none blocking). The somatic-tell-not-labeled-feeling form discipline (the user's load-bearing pre-Phase-0 nudge) plus the two-question defensibility gate (Q1 audience-cannot-otherwise-read + Q2 meaningful-enough) plus the per-character per-scene cap ≤1 + multi-justification ≥3 of 5 + Reading-B-with-cap (POV included) together produce a frugal-by-design facet whose form discipline is enforced at the schema level (the `feels:` field is retired in the same commit).

This is the **first facet whose schema content shape was substantively revised at ship-time** — `<character-slug> feels <feeling> | expressed: ... | <clause>` deprecated to `<character-slug>: <somatic-tell-one-clause> | expressed: ...`. The retired-field model is sensory's rename precedent extended (sensory: §rename + content-shape revision; feeling: §field-retirement + scope-expansion to POV).

---

## Trajectory

| Round | Stage | Author / Reviewer | Result | Notes |
|---|---|---|---|---|
| 0 | Corpus + V1 rubric | — | rubric authored with 7 user nudges absorbed: frugal / disambiguation-on-interior / somatic-tell-not-labeled / POV-included / make-it-count / no-feeling-naming / no-comparisons-or-hedges | 5-character corpus stratified |
| 1 V1 | Lenient form review of naive baseline | mechanic | 44/44 = 100% | form is easy to satisfy under schema-current shape |
| 1 V2 | Strict review of naive baseline | mechanic | **0/44 = 0%** | lowest baseline-to-beat in run-set; 6 systemic faults named (AP5 procedural-flat at 35/44 entries; AP1 form universal; AP2 redundancy; AP8 cap; @39 SKIP-MISSED structural; AP9 multi-justification) |
| 2 forks | Five per-character writer-forks (parallel, blind) | mechanic + dialect | **3/3 = 100% mechanic; 3/3 = 100% dialect (2 advisory MIXED)** | +100pp; SHAPE-OK; officer-zero + clerk-zero correctly refused (AP5) |
| 3 | Adversarial seams | hostile-mode | 3 STRONG (Taylor @39 AP6; Edric @57 finds+two-clause; SKIP-MISSED Taylor @73) + 2 MODERATE (Mira @6 idiom; curve) + 1 THIN (vocab-saturation) + STRONG cross-facet (state-updates @57) | seam-2 (Taylor @39 AP6 content-level) load-bearing |
| 4 | Defense or revise | per-fork (3 active) | 1 DEFEND (Taylor @39 with content-level argument) + 1 NEW FIRE (Taylor @73 SKIP-MISSED repair) + 2 REVISIONS (mira tracks→find; edric finds→takes + two-clause→one-clause) | sparsity 3.9% → 5.2% (honest revision) |
| 5 mech | Final adjudication | mechanic | **4/4 = 100%** | SHAPE-OK with notation; SHIP-WITH-CAVEATS |
| 5 dial | Final adjudication | dialect | **4/4 = 100%** | all VOICE-OK; Phase 2 advisory MIXEDs both resolved |
| 5 combined | | both gates | **4/4 = 100%** | SHIP |

**Lift from V2 baseline: 0% → 100% = +100pp.** Largest absolute lift in the run-set.

| Facet | Baseline V2 | Final | Lift |
|---|---|---|---|
| dialogue | 40% | 100% | +60pp |
| loc-state | 53.8% | 100% | +46.2pp |
| tensometer | 50.6% | 100% | +49.4pp |
| narrator-interest | 22.2% | 100% | +77.8pp |
| state-updates | 6.7% | 100% | +93.3pp |
| memory-flags | 19.0% | 100% | +81.0pp |
| sensory | 33.3% | 100% | +66.7pp |
| **feeling** | **0%** | **100%** | **+100pp** |

Feeling-flags' baseline at 0% is the floor of the run-set. The naive baseline survives 0/44 under V2 strict because (a) the schema-current "feels <feeling>" shape forces 100% AP1 form failure regardless of judgment quality, and (b) the schema's "non-POV character" framing without character-card structural-flat-register awareness produces 35 procedural-flat AP5 violations (officer + clerk) before any author judgment is exercised. The contamination is structural in the schema text itself, not in author taste — exactly where the schema-revision-at-ship discipline does its load-bearing work.

---

## What the user-supplied requirements added

### Pre-Phase-0 nudges (handoff message + early Phase 0)

The user supplied seven rubric-shaping nudges before authoring (the most pre-Phase-0 absorption of any facet to date; absorbs sensory's six and extends):

1. **Frugal.** Per-character per-scene cap ≤1 (hard); per-scene total cap ≤3 (soft); sparsity 2-5%.

2. **Disambiguation-on-interior.** Q1-equivalent transposed to interior: would the audience know what the character feels WITHOUT the flag? Default refuse where proto-line + sensory + dialogue + (for POV) NI already convey the interior. The proto-line @52 "mira drops her eyes to the flagstones" IS the tell — flagging on top is redundant.

3. **Somatic-tell-not-labeled-feeling.** Form discipline absolute. Body register only; the named feeling is forbidden in description; the somatic tell IS the entry. ("preferably the flag will never be (taylor felt sad) but instead (taylor went still) or (george wiped his eyes).")

4. **POV included** (Reading B-with-cap; the user's mid-Phase-0 first nudge: "narrator only gets one feeling per scene max"). Schema's "non-POV only" framing reversed; Taylor gets feeling-flags too, capped at ≤1 per scene.

5. **Make it count.** Multi-justification ≥3 of 5 (somatic-tell-card-match + Q1 + Q2 + scene-eligible + functional-register ≥2 of 4 from {realization / grim humor / social commentary / painting characterization}).

6. **No naming the feeling at all** (the user's mid-Phase-0 second nudge: "make it count. flag needs to capture character showing feeling, not just the name of the feeling. actually, avoid naming the feeling altogether"). The schema's `| feels: <feeling> |` metadata field RETIRED. Description forbids named-feeling vocabulary, hedged vocabulary, and synonym-ladder evasion. Anti-pattern #1.

7. **No comparisons, similes, hedges, metaphors** (the user's mid-Phase-0 third nudge: "NEVER use like or kind of or almost or comparisons/metaphors to 'show' feeling"). Forbidden: { like / as if / as though / kind of / sort of / almost / nearly / faintly / vaguely } + similes + original-figure metaphors + idioms-for-feeling. Body register only; the action is what it is, not what it resembles. Anti-patterns #14–17.

### Pattern: pre-Phase-0 + early-Phase-0 absorption (sensory pattern extended)

This run absorbed all seven user requirements before Phase 1 authoring. Sensory absorbed six pre-Phase-0; memory-flags absorbed five mid-Phase-4. Both works; pre-Phase-0 is preferred when the user's framing is available pre-authoring. Feeling-flags' three nudges arrived in three separate user messages during Phase 0 (handoff + two mid-Phase-0 follow-ups); the rubric was edited live and re-locked before Phase 1. No re-run cost.

**Recommendation locked:** front-load user-rubric-tightenings to Phase 0 in future runs when possible. Sensory + feeling both confirm the cleaner trajectory.

---

## What worked

1. **Schema-revision-at-ship pattern transfers and extends.** Sensory shipped a §rename (loudness → sensory) and content-shape revision (`<modality>: <old> -> <new>`) in same commit. Feeling-flags ships a §field-retirement (`| feels: <feeling> |` removed) and §scope-expansion (non-POV-only → POV+non-POV). Same commit lifecycle. Pattern: when the rubric mandates a content-shape that the schema does not currently encode, schema edit ships at Phase 5 with the locked facet file. Future-facet tunings should anticipate same structure.

2. **Reading B-with-cap (POV included) is the right interpretation.** The user's mid-Phase-0 nudge resolved the schema-conservative Reading A in favor of Reading B-with-hard-cap. NI/feeling double-fire risk handled by AP6 (POV duplicate-with-NI) anti-pattern + content-level Q1-interior gate. Phase 5 verified: Taylor's two fires (@39, @73) are both NI-non-redundant at content level (NI present-tactical vs FF historical-cape-body-doubled-register; NI environmental-perceptual vs FF cape-deploy somatic). Pattern transfer back to NI: NI is POV-only registration; feeling-flags is POV-or-non-POV somatic-show. Cross-facet contract is mandatory for POV.

3. **Somatic-tell-not-labeled discipline holds end-to-end.** Phase 1 baseline: 44/44 = 100% AP1 form failure (the schema's "feels <feeling>" shape STRUCTURALLY forces it). Phase 5: 0/4 form failures. The schema retirement closes the door on AP1; future-episode authors literally cannot fall into labeled-feeling-leak from the schema alone.

4. **Per-character per-scene cap ≤1 forces selection and disciplines density.** Edric @55-@56-@57 cluster: cap forces selection of @57 (largest beat) over registration-only precedents. Taylor: cap forces selection of @39 over adjacent commit-stance candidates @37/@38. Mira: cap forces single fire on Scene 3 evaluation (refused both @52 anchor and @53 held-pose extension); Scene 1 fire is mira's single establishing register. Hard cap is the rubric's load-bearing density-discipline structure.

5. **Multi-justification ≥3 of 5 functions as both fire-defense and refuse-pressure.** All four shipped fires defend 5/5; all sub-3 refusals are correct under multi-justification. The gate is the right shape because it is not pure-binary (a 3 of 5 fire is acceptable; the file lands all 5 of 5 as honest revision toward maximum defense).

6. **Procedural-flat-character refusal (AP5) holds structurally.** Officer + clerk persona cards forbid interior performance; expected output 0 fires. Phase 2 forks correctly produced 0 fires for both. Phase 5 verified all 35+ refusals are AP5-correct. The cards do the work; the rubric formalizes what the cards already say. Pattern transfers: future projects with procedural-flat characters (administrative functionaries, distance-keeping NPCs) inherit the AP5 structural-zero-fire expectation.

7. **Mid-Phase-0 nudge absorption tested live.** Three user messages arrived during Phase 0 (after handoff, mid-rubric-author, mid-rubric-author). The rubric was edited (in two cycles) and re-locked before Phase 1 dispatched. Total absorption: seven nudges, zero re-run cost. The pipeline tolerates Phase-0 nudge sequences cleanly. Memory-flags' Phase-4 mid-tuning absorption was also tolerable but expensive (Phase 4 re-run); Phase-0 absorption is the cheaper path when the framing arrives during planning.

8. **Hybrid mechanic + dialect-audience review with independent gates held cleanly.** Mechanic catches form, AP6 content-level, multi-justification, cross-facet. Dialect audience catches per-character voice register, AP7 vocabulary saturation, and (Phase 2) the "tracks" idiom-import + edric two-clause concerns. Independent signal confirmed: dialect's Phase 2 MIXEDs surfaced revisions the mechanic accepted; revisions cleared at Phase 5 dialect re-review. Same precedent as narrator-interest and memory-flags. No bleeding into mechanic-domain adjudication.

9. **Adversarial Phase 3 surfaced load-bearing structural seam (AP6 content-level test).** Phase 2 mechanic accepted 3/3 with 5/5 multi-justification each; Phase 3 hostile mode pressed AP6 from anatomical-loci to interior-content level — load-bearing seam. Phase 4 answered at content level: NI present-tactical vs FF historical-cape-body-doubled-register. Phase 3 also surfaced SKIP-MISSED Taylor @73 (Phase 2 refused on AP6 collision claim; Phase 3 pressure pointed out NI @73 has zero somatic content). Phase 4 fired @73. Pattern: Phase 3 doing real work, not redundant work; same as prior-runs.

10. **Hard fences held end-to-end.** Zero Earth-Bet proper-noun leaks in description fields across baseline, Phase 2, Phase 4, Phase 5. The variant card's "swarm" and "cape" never named; cape-deploy somatic (@73) and cape-trained body register (@39) are rendered through behavior-card vocabulary only ("breath empties" / "shoulders go down and back").

---

## Residual caveats (from Phase 5)

Seven items the auditor flagged before declaring shippable; all carried into the locked facet file's footer:

1. **Caveat-001 (notation-only):** Sparsity 5.2% sits 0.2pp above 2-5% target ceiling; SKIP-MISSED-repair driven; ship with notation. Future-episode authors target lower half of band.

2. **Caveat-002 (soft watch):** "Takes" at @57 carries lower-amplitude AP16 residual than "finds" but working-language defense holds. Fallback: "shifts to" or "settles onto."

3. **Caveat-003 (stitcher instruction):** Verbatim base-card §Non-verbal tics lift at @39. Stitcher must integrate, not transcribe.

4. **Caveat-004 (stitcher instruction):** @57 triple-coverage (proto-line + state-updates 8+9 + feeling-flag). Render once: act → texture → silent canonical writes.

5. **Caveat-005 (advisory; per-season):** All four e01 fires in controlled-body-discipline-before-action semantic register. Future episodes diversify (involuntary tell, post-act cost, realization, distress) to prevent season-level monoculture.

6. **Caveat-006 (advisory):** Taylor's two e01 fires both peak-cluster (t=3 / terminus). Future Taylor fires include at least one quiet-beat or post-act fire.

7. **Caveat-007 (schema):** `schemas/facet.schema.md` § feeling-flags `feels` field retired same commit. Schema content shape revised. **Applied this commit.**

---

## What needs doing next (if continuing)

1. **Schema rename ALREADY APPLIED** (caveat-007). `schemas/facet.schema.md` § feeling flags revised in same commit as feeling-flags ship.

2. **Pilot feeling-flags on s01e02 or s01e03 for stretch-sample.** s01e01 is 77 beats; e03 is 232. Verify the 2-5% band scales (likely stays sparser per per-character per-scene cap × low-fire-eligible-character count); verify per-season semantic-register diversification starts to land (caveat-005); verify Taylor-fire distribution diversifies away from peak-cluster (caveat-006).

3. **Pilot the next facet in sequence.** Open candidates per the original sequence:
   - **metaphor flags** (editor-authored at stitch-time; downstream of memory-flags + sensory-flags + feeling-flags). Tuning would validate the licensing-layer contract from the consumer side: every shipped metaphor must co-cite a memory-flag fire (mandatory per memory-flags), MAY co-cite a sensory-flag, and SHOULD interact with feeling-flag fires for cross-facet figurative-rendering coherence. Capstone facet.
   - **vibes-updates** (showrunner-authored; cross-cutting). Different shape from per-beat facets; likely different five-phase shape.
   - **audience interest-flags** (per-persona). High coupling to project audience.

4. **Retroactive evaluation of memory-flags gates against earlier facets (caveat-005 from memory-flags).** Still deferred. Sensory and feeling tunings did not surface NI co-citation problems (sensory independent of NI; feeling-flags cross-facet contract has POV non-redundancy — Phase 5 confirmed @48 NI fire is POV foreknowledge-clamp interior, NOT a feeling-flag candidate). Memory-flags' caveat-005 retroactive check stays deferred until metaphor-tuning surfaces concrete cross-facet contradictions.

5. **Address residual caveats.** Schema retirement (caveat-007 — applied this commit); per-season register-diversification tracking (caveat-005 — advisory); Taylor distribution-diversification tracking (caveat-006 — advisory); stitcher instructions (caveat-003, 004 — applied to stitcher's brief at integration time); sparsity-upper-edge notation (caveat-001 — applied); takes-watch (caveat-002 — applied as advisory).

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-feeling.md` (V1 LOCKED 2026-05-07; seven user-supplied requirements absorbed Phase 0)
- Schema: `schemas/facet.schema.md` (feeling section — REVISED THIS COMMIT)
- Process doc: `design/shoot-v2/facet-tuning-process.md`
- Cross-facet authorities: `active-project/theater/facets/interest-narrator.md` (locked; AP6 content-level mandatory for POV), `active-project/theater/facets/state-updates.md` (locked; @57 stitcher integration), `active-project/theater/facets/sensory.md` (locked; @72 adjacency cleared), `active-project/theater/facets/tensometer.md` (locked; correlative observation only)

### Phase 0
- Corpus: `design/shoot-v2/feeling-corpus.md`
- V1 rubric: `design/shoot-v2/rubric-feeling.md`

### Phase 1
- Naive baseline (rubric-blind): `design/shoot-v2/phase1-feeling-baseline-naive.md`
- V1 lenient + V2 strict review: `active-project/staff/auditor/phase1-feeling-baseline-review.md`

### Phase 2
- Per-fork outputs:
  - `design/shoot-v2/phase2-feeling-output-taylor.md`
  - `design/shoot-v2/phase2-feeling-output-mira.md`
  - `design/shoot-v2/phase2-feeling-output-edric.md`
  - `design/shoot-v2/phase2-feeling-output-officer.md` (zero fires; AP5)
  - `design/shoot-v2/phase2-feeling-output-clerk.md` (zero fires; AP5)
- Aggregate: `design/shoot-v2/phase2-feeling-output.md`
- Mechanic audit: `active-project/staff/auditor/phase2-feeling-audit.md`
- Dialect audience review: `active-project/audience/feeling-phase2-review.md`

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-feeling-seams.md`

### Phase 4
- Per-fork defenses:
  - `design/shoot-v2/phase4-feeling-defense-taylor.md`
  - `design/shoot-v2/phase4-feeling-defense-mira.md`
  - `design/shoot-v2/phase4-feeling-defense-edric.md`
- Aggregate: `design/shoot-v2/phase4-feeling-aggregated.md`

### Phase 5
- Final mechanic adjudication: `active-project/staff/auditor/phase5-feeling-final.md`
- Final dialect audience review: `active-project/audience/feeling-phase5-review.md`

### Shipped
- Locked feeling facet: `active-project/theater/facets/feeling.md` (s01e01, 4 entries, READY-WITH-CAVEATS)

### This package
- `design/shoot-v2/feeling-tuning-package.md`

---

## Co-deployment note

Per dialogue, loc-state, tensometer, narrator-interest, state-updates, memory-flags, and sensory packages: writer + reviewer ships as a co-deployed unit. For feeling-flags, the unit has FIVE components reflecting the per-character split-authorship architecture and the hybrid review:

- **Writer (per-character dialogue-writer fork; one per character).** POV (taylor) loads behavior pack + variant + persona card + locked NI (mandatory non-redundancy check for AP6) + locked sensory/state-updates/tensometer (soft) + this rubric. Non-POV (mira / edric / officer / clerk / etc.) loads only that character's persona card + this rubric. Two-pass authoring (per-beat → file-shape audit). Per-beat decisions evaluate Q1 + Q2 + multi-justification (≥3 of 5) under per-character per-scene cap ≤1 + functional-register ≥2 of 4. File-shape audit verifies sparsity (2-5%), per-character/per-scene caps, vocabulary distinctness, no labeled-feeling-leak, no simile/hedge/metaphor/idiom/synonym-ladder, AP6 content-level for POV.

- **Reviewer (mechanic auditor).** Single mechanic auditor with the rubric as authority. Per-entry verdicts (CORRECT / INCORRECT-{axis-or-anti-pattern}); per-skip verdicts (SKIP-CORRECT / SKIP-MISSED); curve verdict (SHAPE-OK / SHAPE-FAIL); cross-facet contract pre-ship check. Cross-fork dependency check at Phase 5 (per state-updates pattern). Voice fidelity is checked at the axis level but the reviewer does not have the dialect audience's per-character calibration.

- **Reviewer (dialect audience, voice-fidelity-only mode).** Worm-canon-pedant primary (POV cape-trained-body lift; base-card register fidelity); dark-fantasy-reader and pulp-enthusiast secondary (genre-specific non-POV calibration; pacing density). Per-entry verdicts: VOICE-OK / VOICE-FAIL / VOICE-MIXED with citation to behavior-pack / persona-card §. Calibrated per-character: each character's persona-card §Voice / §Look / §Signature Moves provides the voice-vocabulary check. Domain restricted to voice fidelity; does not adjudicate firing decision, channel selection, Q1/Q2, multi-justification, per-scene cap, or cross-facet contract.

- **Verdict combination.** Mechanic + dialect verdicts are independent gates. Both must pass for ACCEPT. They cannot substitute. Phase 5 confirmed independent-signal architecture working: mechanic catches form / AP6 / multi-justification / cross-facet; dialect catches per-character voice register / vocabulary saturation across fires.

- **Adversarial pass (Phase 3).** Same mechanic auditor in hostile mode, one strongest seam per entry plus one curve-level seam plus one cross-facet seam plus one Q1-interior-integrity seam plus one vocabulary-saturation seam plus SKIP-MISSED candidate seams. Catches what passes naive mechanic review.

The five parts (per-character writer-forks + mechanic + dialect + adversarial-pass) are not separable. The writer's affirmative-citation discipline (multi-justification ≥3 of 5 with somatic-tell-card-match anchor) only works because the mechanic auditor tests citations and content-level AP6. The dialect audience's voice-fidelity verdict only works because the writer produces entries that *demonstrate* per-character somatic-tell vocabulary rather than merely avoid violations. The mechanic auditor's strict rubric is only meaningful because the writer can produce entries that survive multi-justification ceiling-defense and content-level AP6 challenge. The adversarial pass surfaces what the others accept.

The dialect audience IS part of the feeling-flags pipeline — fidelity-only, voice-only, per-character calibration, no scope creep into mechanic adjudication. Calibration to each character's persona-card §Voice / §Look / §Signature Moves preserved across the run.

The schema-revision-at-ship pattern is the structural addition for this facet relative to memory-flags' rubric-only revision pattern. The pipeline tolerates schema-revision-at-Phase-5 cleanly: the locked facet file uses the new shape; the schema text is revised in the same commit; the rubric § Locked notation flags the schema edit at Phase 0 so the schema change is anticipated by Phase 1. **Recommendation locked: future facet tunings should evaluate at Phase 0 whether the schema content shape needs revision; if yes, ship in same commit as Phase 5 facet file.**
