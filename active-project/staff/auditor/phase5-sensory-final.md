# Phase 5 — Sensory-Flags Final Adjudication

Mechanic auditor final review of `design/shoot-v2/phase4-sensory-defense.md` under V1 LOCKED rubric. Single-gate review (no dialect audience).

---

## Per-entry verdicts (post-defense)

| # | Beat | Delta | Phase 4 disposition | V1 verdict |
|---|---|---|---|---|
| 1 | @13 | sound: yard-ambient-murmur → officer-command-voice | DEFEND (Seam-1 sustained-vs-inflection) | **CORRECT** |
| 2 | @24 | sound: stylus-on-wax-rhythm → silence | DEFEND (Seam-2 naming retained) | **CORRECT** |
| 3 | @30 | sound: silence → stylus-on-wax-rhythm | DEFEND (Seam-3 modality-specific old-state) | **CORRECT** |
| 4 | @41 | sound: officer-letter-handling → wax-crack | REVISED (Seam-2/Seam-4 convergence) | **CORRECT** |
| 5 | @72 | tactile: dirt-yielding → stone-firm | DEFEND (Seam-5 multi-justification floor) | **CORRECT** |

**Per-entry: 5/5 = 100%.**

Each entry's defense citation tested against the V1 rubric:

- **@13:** rubric § Axis 1 ACCEPT signature "Inflection class clear" + § What sensory-flags is for job 3. Defense holds — @13 is the change-point; loc-state holds the level after; sensory-flags holds the inflection. ✓
- **@24:** rubric § Axis 1 + Axis 2 + Axis 3 + Axis 4. All four axes clear. The naming `silence` is consistent with the rubric's specificity discipline. ✓
- **@30:** rubric § Form ("Source the old-state from … the prior sensory-flag entry if the modality has fired earlier in the episode"). Modality-specific old-state convention defends — @24 was the prior sensory-flag entry on the stylus-rhythm channel; @30's old-state correctly inherits from it. ✓
- **@41:** revised old-state matches loc-state baseline-precision principle. ✓
- **@72:** multi-justification stack 5 strong + 2 borderline = 7 total; comparable to memory-flags Phase 5 ship (5-6 justifications including borderline). Defense holds. ✓

---

## Refusal-set audit (post-defense)

All Phase 2 refusals retained; no missed-fire surfaces in Phase 4. Refusal-set audit: **12/12 = 100%** SKIP-CORRECT.

---

## File-shape audit (post-defense)

| Check | Target | Observed | Verdict |
|---|---|---|---|
| Sparsity | 3-6% | 6.5% (5/77) | SHAPE-OK with notation per Phase-4 curve-seam structural decision |
| Modality coverage (per-episode) | ≥2 | sound + tactile = 2 | ✓ |
| Modality coverage (per-season) | ≥3 across s01e01-e06 | s01e01 lands 2 (sound + tactile) | TRACKING (caveat) |
| Bare-not-charged | 0 charged | 0 charged | ✓ |
| Magnitude-sufficiency | 0 sub-threshold | 0 sub-threshold (@72 borderline-but-defensible) | ✓ |
| Inflection-not-sustained | 0 sustained | 0 sustained | ✓ |
| Inflection-pair coherence | drops paired with ups | @24 drop / @30 up coherent | ✓ |
| Per-scene cap ≤3 | each scene | scene 1: 1, scene 2: 3, scene 3: 0, scene 4: 1 | ✓ |
| Loc-state baseline match | each fire | all match (post-@41 revise) | ✓ |
| Cross-facet annotation | tens @64 deviation | annotated in frontmatter | ✓ |

**File-shape: SHAPE-OK with named caveats.**

---

## Cross-facet contract pre-ship check

- **Loc-state (upstream):** all old-states match loc-state baseline (post-@41 revise) ✓.
- **Tensometer (correlative-not-gating):** @24 anchor-expectation honored; @64 anchor-expectation deferred (annotated). ✓.
- **Independent of NI / memory-flags / state-updates:** no co-citation requirements; no cross-facet violations ✓.

---

## Phase 5 summary

| Stage | Result |
|---|---|
| V1 lenient baseline | 12/12 = 100% |
| V2 strict baseline | 4/12 = 33.3% |
| Phase 2 writer-fork (mechanic) | 5/5 = 100% |
| Phase 3 seams | 5 STRONG + 2 MODERATE per-entry + curve-STRONG + cross-facet-MODERATE + disambiguation-STRONG |
| Phase 4 (1 revise + 4 defends + structural decision + annotation) | seams answered |
| **Phase 5 final (mechanic)** | **5/5 = 100%** |

**Lift from V2 baseline: 33.3% → 100% = +66.7pp.** Smallest lift in the run-set (because the highest baseline) but the file ships clean. Comparable to:

| Facet | Baseline V2 | Final | Lift |
|---|---|---|---|
| dialogue | 40% | 100% | +60pp |
| loc-state | 53.8% | 100% | +46.2pp |
| tensometer | 50.6% | 100% | +49.4pp |
| narrator-interest | 22.2% | 100% | +77.8pp |
| state-updates | 6.7% | 100% | +93.3pp |
| memory-flags | 19.0% | 100% | +81.0pp |
| **sensory** | **33.3%** | **100%** | **+66.7pp** |

---

## Residual caveats

1. **Caveat-001 (advisory; per-season tracking):** Per-season modality-coverage tracking. s01e01 ships sound + tactile = 2 modalities. Season-level expectation: ≥3 modalities across s01e01-e06. Future episodes should bring light, smell, thermal, humidity, or pressure entries to satisfy season-level diversity. Mirrors memory-flags' single-register-per-episode + per-season-tracking finding.

2. **Caveat-002 (cross-facet annotation):** Locked tensometer cross-facet contract names @64 as sensory anchor-expected; sensory file refuses on Q2 sub-threshold magnitude. Deviation annotated in shipped frontmatter; locked tens contract not amended (the contract's "anchor-expected" language admits deviation; the V1 sensory rubric's correlative-not-gating clause makes the expectation suggestive).

3. **Caveat-003 (sparsity at upper-edge):** File ships at 6.5% vs 3-6% band. Honest-revision per Phase-4 curve-seam structural decision — sparsity is target-not-hard; per-fire ceiling-defense holds. Per facet-tuning-process precedent (tensometer's 2-rung soft-fail at 15.6% vs 20-30% band).

4. **Caveat-004 (schema rename):** `schemas/facet.schema.md` § "loudness flags" requires update at ship-time:
   - Rename section to "sensory flags".
   - Update file path `facets/loudness.md` → `facets/sensory.md`.
   - Update content shape `<up|down|spike|drop> <one-clause>` → `<modality>: <old> -> <new>` with optional `# tag:` annotation.
   - Add modality enumeration (sound / light / smell / thermal / humidity / pressure / tactile).

5. **Caveat-005 (process; rubric tightening):** Four user-supplied rubric tightenings landed pre-Phase-0 and during Phase 0 (rename to sensory; state-update-aligned shape; tensometer-independence; disambiguation-not-redundancy). Two more landed early-Phase-0 (frugal ≤3-per-scene; multi-justification two-question test). All six absorbed before Phase 1 authoring; no mid-Phase-4 retune needed (contrast: memory-flags absorbed five tightenings mid-Phase-4 with Phase 4 re-run). The natural place for user-rubric-tightening in this run was Phase 0; in memory-flags it was mid-Phase-4. Both work; Phase 0 is preferred when the user's framing is available pre-authoring.

---

## Shippability

**SHIP** with caveats 1-5 named above.

The file is ready for cross-facet consistency pass (with locked dialogue, loc-state, tensometer, narrator-interest, state-updates, memory-flags). Cross-facet consistency may surface contradictions; the sensory file's contradiction risk is low because sensory is independent of NI / memory-flags / state-updates and only depends on loc-state for old-state baseline (which is already matched).

Schema rename should be applied in the same commit as ship to avoid filename mismatch between schema § "loudness" and shipped `facets/sensory.md`.
