# Phase 2 — Sensory-Flags Mechanic Audit

Mechanic auditor review of `design/shoot-v2/phase2-sensory-output.md` (5 entries) under V1 LOCKED rubric. Single-gate review (no dialect audience per rubric § Author/reviewer notes).

---

## Per-entry verdicts

| # | Beat | Modality | Delta | Q1 | Q2 | Sustained? | Audience-side | Loc-state match | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | @13 | sound | yard-ambient-murmur → officer-command-voice | bare ✓ | large ✓ | inflection ✓ | yes ✓ | yes ✓ | **CORRECT** |
| 2 | @24 | sound | stylus-on-wax-rhythm → silence | bare ✓ | large ✓ | inflection ✓ | yes ✓ | yes ✓ | **CORRECT** |
| 3 | @30 | sound | silence → stylus-on-wax-rhythm | bare ✓ | large ✓ | inflection ✓ | yes ✓ | yes ✓ | **CORRECT** |
| 4 | @41 | sound | yard-quiet → wax-crack | bare ✓ | large ✓ | inflection ✓ | yes ✓ | yes ✓ | **CORRECT** |
| 5 | @72 | tactile | dirt-yielding → stone-firm | bare ✓ | large ✓ | inflection ✓ | yes ✓ | yes ✓ | **CORRECT** |

**Per-entry: 5/5 = 100%.**

---

## Refusal-set audit (skipped beats — checking for missed fires)

The writer-fork's silence-list against the corpus § Predicted refusals + corpus § Mid-priority candidates:

| Skipped beat | Why writer skipped | Auditor verdict |
|---|---|---|
| @58 stylus resumes | "resumes" charged-leaning Q1 | SKIP-CORRECT |
| @64 stylus marks | sub-threshold Q2 | SKIP-CORRECT |
| @38 letter forward | no-modality | SKIP-CORRECT |
| @50 turns to Mira | no-modality | SKIP-CORRECT |
| @57 Edric exits | sub-threshold Q2 | SKIP-CORRECT |
| @67 foot toward horse | no-modality | SKIP-CORRECT |
| @69 wheel-tremor leaves | fauna-feed-extension | SKIP-CORRECT |
| @73 step into shadow | "shadow" charged Q1 | SKIP-CORRECT (calibration anchor for charged-word redundancy) |
| @11 officer through gate | no-modality / sub-threshold | SKIP-CORRECT |
| @47 officer's voice returns | sustained-as-inflection | SKIP-CORRECT |
| @21 officer to each ward | sustained | SKIP-CORRECT |
| @77 through door | no-discrete-inflection-at-beat | SKIP-CORRECT |

**Refusal-set: 12/12 = 100%.** All skipped beats correctly silent under V1 rubric.

---

## File-shape audit

| Check | Target | Observed | Verdict |
|---|---|---|---|
| Sparsity | 3-6% | 6.5% (5/77) | SHAPE-OK with notation (upper-edge; ceiling-defense per fire) |
| Modality coverage | ≥2 | sound + tactile = 2 | ✓ |
| Bare-not-charged | 0 charged | 0 charged | ✓ |
| Magnitude-sufficiency | 0 sub-threshold | 0 sub-threshold | ✓ |
| Inflection-not-sustained | 0 sustained | 0 sustained | ✓ |
| Inflection-pair coherence | drops paired with ups | @24 drop / @30 up coherent | ✓ |
| Per-scene cap ≤3 | each scene | scene 1: 1, scene 2: 3, scene 3: 0, scene 4: 1 | ✓ |
| Tens correlation (observation) | distributed | t=1: 3, t=2: 1, t=3: 1 | distributed (no gating concerns) |
| Loc-state baseline match | each fire | all match | ✓ |

**File-shape: SHAPE-OK with notation** (sparsity at upper edge — accepted as honest revision per facet-tuning-process precedent; tensometer's 2-rung soft-fail-vs-band-shipped-with-notation is the precedent).

---

## Cross-facet contract pre-ship check

- **Loc-state (upstream):** all old-states match loc-state baseline ✓.
- **Tensometer (correlative-not-gating):** @24 anchor-expected per locked tens cross-facet contract — fired ✓. @64 mentioned in locked tens contract as "smaller volume-event" candidate — refused on Q2 sub-threshold; deviation from anchor-expectation is rubric-driven (Q2 magnitude gate strips it). Documented as expected deviation; locked tens contract was anchor-expectation, not anchor-requirement, per the V1 rubric's correlative-not-gating clause. ✓.
- **Independent of NI / memory-flags / state-updates:** no co-citation requirements; no cross-facet violations ✓.

---

## Phase 2 summary

| Stage | Result |
|---|---|
| V1 lenient baseline | 12/12 = 100% |
| V2 strict baseline | 4/12 = 33.3% |
| Phase 2 writer-fork (mechanic) | **5/5 = 100%** |

**Lift from V2 baseline: 33.3% → 100% = +66.7pp.** Comparable to prior runs (dialogue +60, loc-state +46.2, tens +49.4, NI +77.8, state-updates +93.3, memory-flags +81.0). Sensory's lift is the smallest because the baseline was the highest (33.3% — naive author hits four obvious fires by sound-following without rubric).

Phase 2 output ready for Phase 3 adversarial pass.

---

## Notes for Phase 3 (forwarded to hostile-mode auditor)

The writer-fork's anticipated-seams section names:
- @72 magnitude borderline (softest fire)
- @13 inflection-vs-sustained read
- Density at upper-edge band
- Cross-modal coverage thinness (only 2 of 7 modalities)

Hostile-mode pass should produce strongest single seam per entry plus cross-facet seam plus curve seam, per Phase 3 protocol.
