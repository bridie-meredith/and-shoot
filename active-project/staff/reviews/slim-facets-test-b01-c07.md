# Slim /and-facets live test — b01-c07 (DEC-0116 validation)

Date: 2026-06-08 · Branch: claude/ecstatic-volta-14ixm1 · Scope: validate the URI-FACETS-SLIM /and-facets (R2 round + Phase 5b audience-gate retired) on a live chapter, against the archived old-pipeline run for the SAME chapter.

## Why c07
Small (25 bones), clean, 2-cast, hinge "breathing" chapter — and it has an archived old-pipeline run to compare against: `active-project/theater/_archive/20260531T050032Z-b01c07-facets/` (footprint: **76 per-reviewer audience verdict files + 9 R2 decision shards + 2 audit cycles**; reached **0 HARD / 5 SIGNAL**).

## What the test had to do first (the rebuild left c07 half-migrated)
The no-ledger rebuild re-emitted c07 bones (2026-06-08) as a render shortcut, skipping scene-map + dialogue + a fresh bones review. Setup (legitimate, minimal):
- scene-map authored (orchestrator-emitted per schema; 3 scenes; 25/25 coverage).
- dialogue authored in-voice (2 impersonators; 3 utterances; fence-clean; Halvard's compounding-rot doctrine in septon idiom, Taylor's named-child "Pia" counter).
- `/and-review bones` → **FAILed: 6 HARD SVO-form faults** in the rebuilt bones (bones 2/3/8/13/19/25 — perception/stative/abstraction-object/PP forms). Spine clean. Fixer recast all 6 per reviewer specs (DEC-0115 concrete forms) → re-cleared. *(Independent finding: the no-ledger rebuild's bones are not gate-clean.)*

## The slim /and-facets run

| Phase | What ran | Result |
|---|---|---|
| 1 — R1 authoring | facet authors (bundled to 6 dispatches for test economy; production fans to ~12 blind authors) | Full 12-file graph, **~44 facet entries** (vs old run's ~47). metaphor correctly **refused (0 entries)**. |
| 2 — cite-index merge | **SKIPPED** (stitcher convenience; harness shortcut) | see caveat 1 |
| 2.5 — context/aliveness | 1 reviewer | **FOLLOWABLE** + **AIRLESS-HOLE** (1 spine grounding line). Reviewer refused to inherit the prior verdict and caught that the no-ledger re-emit reopened the @16/@17 bare pivot the old run had closed via Phase 4.6. |
| 3 — conditional remediation | 1 sensory add | `sensory:3 @17` proprioceptive bracing-weight (licensed grd-001); airless hole **closed**. |
| 4 — mechanical auditor (THE GATE) | 1 auditor | 4 HARD reported → **2 false-positive (retracted)** + **2 genuine** (trivial format). |
| 4-fixer | orchestrator, inline | exposition id-monotonicity + vibes non-resolvable token → **0 HARD**. |
| 5 — persist + critic | orchestrator | gate PASS. |

### Phase 4 audit detail
- **Reported 4 HARD; real 2.** fault-002/003 ("feeling + actor-state files absent") were **FALSE** — all four files exist (verified on disk, Rule 19). The auditor searched abbreviated slugs (`feeling-taylor-...`) instead of full actor slugs. Root cause: the skipped Phase 2 cite-index merge (caveat 1), which in production consolidates per-character slices into `feeling.md`/`state-updates.md` with a manifest the auditor reads. Harness artifact, not a graph defect.
- **2 genuine HARD, both trivial format:** exposition id non-monotonic (renumbered); vibes:1 `licensed-by: peak-bone:scene-A-2` non-resolvable (scene A has no peaks — token removed). Fixer-cleared in 1 pass.
- **5 SIGNAL (non-blocking):** NI 28% denominator-driven carve-out; sensory 8% denominator-driven; exposition dual-scope tag; vibes peak-bone format off-schema-but-resolvable; @16 undecorated → VOICE-FIXABLE to /and-stitch. **These match the old run's SIGNAL dispositions** (the old run also dispositioned the NI 28% carve-out SIGNAL).
- CURVE-SHAPE SHAPE-OK; Earth-Bet fence CLEAN.

## Orchestrator-critic verdict (slim acceptance criteria)
```
Result: SUCCESS (with one harness caveat)
Criteria met: 6/7  (cite-index merge skipped for test economy — caveat 1, not a pipeline miss)
HARD findings post-audit: 0  (after 1 fixer pass)
Phase 2.5: completeness FOLLOWABLE, readability ALIVE (AIRLESS-HOLE remediated + closed)
Dispatch count (facets only): ~9 this test / ~15 true-slim (full R1 fan-out)
Recommendation: ship
```

## Head-to-head

| | OLD pipeline (archived c07) | SLIM pipeline (this run) |
|---|---|---|
| R1 authoring | ~12 blind authors | ~12 (unchanged; bundled to 6 for the test) |
| R2 judging round | 9 decision shards (6 judges) | **0 — retired** |
| Phase 5b audience-gate | **76 per-reviewer verdict files, 2 cycles** | **0 — retired** |
| Audit | 2 cycles | 1 + 1 fixer pass |
| Readability remediation | Phase 4.6 sensory adds | Phase 2.5 → Phase 3 grounding add (kept, slimmed) |
| **Total dispatches** | **~60–90** | **~9–15** |
| **Quality outcome** | 0 HARD / 5 SIGNAL | **0 HARD / 5 SIGNAL — same dispositions** |

## Conclusion
The slim pipeline reached the **same quality outcome** (0 HARD, same SIGNAL dispositions, same readability remediation of the same airless hole) at roughly **1/6 the dispatch cost**. The R2 round's culling was **not needed** to reach clean — the R1 per-author cull + the single mechanical auditor caught the only real defects (2 trivial format faults), and Phase 2.5 + the slimmed conditional remediation carried the DEC-0115-class readability fix that matters. **DEC-0116 validated on a live chapter.**

## Honest caveats / process findings
1. **Cite-index merge skipped (test harness).** Caused the auditor's 2 false-positive "absent file" HARDs (abbreviated-slug resolution). In production the Phase 2 merge runs and this class doesn't arise — BUT it's a real robustness lesson: either the auditor brief should resolve per-character slice files by full actor slug, or the merge must always precede the audit. Candidate parking-lot/hardening item.
2. **R1 bundled to 6 dispatches** for test economy (vs ~12 blind authors in production). Does not affect the R2/5b-removal conclusion (R1 is unchanged by DEC-0116), but the true slim facets cost is ~15, not ~9.
3. **No-ledger rebuilt bones are not gate-clean** — c07 carried 6 SVO-form faults the rebuild introduced/retained. Independent of DEC-0116, but worth noting for the broader book state (the other rebuilt chapters likely carry similar form debt).
