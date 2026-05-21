---
report: facets-audience-gate
episode: b01-c01
date: 2026-05-20
cycle: 3-of-3 (CAP-BURNED)
mode: facet-adversarial-strict-3-of-3
auditor-input: active-project/staff/auditor/facets-final-audit-r3.md
fixer-inputs: [active-project/staff/fixer/and-facets-r1-fixes.md, active-project/staff/fixer/and-facets-cycle2-fixes.md, active-project/staff/fixer/and-facets-cycle3-fixes.md]
status: PARTIAL-PASS
facets-passed: 10
facets-failed: 2
gate-verdict: CAP-BURNED
---

# /and-facets b01-c01 — Phase 5b consolidated audience-gate report

## Per-facet final verdicts

| Facet | Cycle 1 | Cycle 2 | Cycle 3 | Final |
|---|---|---|---|---|
| location-state | revise (3) | accept (3) | — | **ACCEPT** |
| interest-narrator | revise (3) | revise (1: dark-fantasy doubled-register) | accept (3) | **ACCEPT** |
| sensory | revise (1) + fail (2) | accept (1) + revise (1) + fail (1) | accept (2) + revise (1: old-state lineage on sensory:3) | **FAIL** |
| state-updates | revise (3: carve-out position) | accept (3) | — | **ACCEPT** |
| memory | revise (3: feel-as-spine + slug-form) | revise (3: feel-as-spine fundamentally rejected) | NOT RE-RUN (no actionable fix in scope) | **FAIL (cap-burn)** |
| feeling | accept (3) | — | — | **ACCEPT** |
| metaphor | accept (3) | — | — | **ACCEPT** |
| vibes | accept (3) | — | — | **ACCEPT** |
| exposition | accept (3) | — | — | **ACCEPT** |
| dialogue / coll | accept (3) | — | — | **ACCEPT** |
| dialogue / taylor | revise (3: sidecar citation-completeness) | accept (3) | — | **ACCEPT** |
| dialogue / wren | accept (2) + revise (1: worm-canon "your hand") | accept (3) | — | **ACCEPT** |

**Aggregate:** 10 PASS / 2 FAIL across 12 facets (9 standard facets + 3 per-character dialogue files).

## Reviewer membership

- **Sensory specialists (3)** under `staff/audience/`: sensory-disambiguation-pedant, sensory-modality-coverage, sensory-old-state-reader.
- **Active-project audience (3)** under `active-project/audience/`: cape-fic-reader, dark-fantasy-reader, worm-canon-pedant — used for all non-sensory facets.

## Cycle counts

- Cycle 1: 12 facets fired (all). 5 passed, 7 failed.
- Cycle 2: 7 failing facets re-fired. 4 passed, 3 failed.
- Cycle 3: 2 failing facets re-fired (memory deliberately skipped — no in-scope remediation available). 1 passed (interest-narrator), 1 still failed (sensory).

## Cap-burn rationale

Cycle cap (3 per /and-season convention) reached without 3-of-3 across all facets.

- **sensory:** cycle-3 fixer added sensory:3 sound entry at @17 to clear modality silent-gap. Old-state-reader specialist accepted the loc-state:1 light-field add (cleared sensory:1 lineage) but flagged a NEW HARD on sensory:3's `street-quiet-of-mid-afternoon` old-state — unanchored to any prior loc-state or sensory entry. The fix introduced a new finding that would require a fourth cycle to address (out of scope per cap).

- **memory:** all three reviewers across cycles 1 and 2 rejected the `# defense: feel-as-spine` annotation. The rubric mandates narrator-interest co-citation for memory entries; no carve-out exists for feeling-as-spine substitution. Three resolution paths exist, all blocked:
  - Add NI @9 → breaches band ceiling (NI would push to 25.9%, over 25% cap; cycle-1 dark-fantasy already escalated doubled-register absence at the band ceiling).
  - Delete mem:1 @9 → memory file becomes single-Westerosi-register; loses the Khepri-residue lighting at the chapter's substance-hinge; SHAPE-FAIL named explicitly by all three reviewers.
  - Rubric-authority ruling on feel-as-spine equivalence — out of scope for this run.

  Cycle-3 fixer deliberately skipped memory remediation per orchestrator decision; the cap-burn for memory is documented rather than chased through a fourth cycle with no clean path.

## Convergence trace

- **Auditor HARD findings (r3 final):** 0
- **Auditor SIGNAL findings (carried forward across r1/r2/r3):** ~15 (slug inconsistencies, frequency-band integer-floor breaches, metadata-inconsistencies, vibes dual-anchor citations, exposition cold-start advisory, CURVE-SHAPE hinge-label vocabulary collision, TASTE-FLAG advisories)
- **Audience callouts (deduped across cycles 1-3):** 7 cycle-1 facets failed + 3 cycle-2 + 1 cycle-3 (the new sensory:3 lineage HARD)
- **Shared findings (audience + auditor):** F-005 NI template saturation (auditor HARD + 3/6 reviewers; addressed cycle 2); F-006 state-updates POV co-citation (auditor RUBRIC-FIDELITY HARD + 3 reviewers; addressed cycles 1-2); F-002/F-003/F-004 exposition (auditor CONSTRAINT HARD + 3-of-3 audience accept post-cycle-1 fix)
- **Audience-only findings:** loc-state:3 @11 dexterity verb (auditor missed); NI-1 @4 "the network" label (auditor missed atmosphere-thin); NI-6 @27 policy-declaration vs gap-narration register (auditor missed); memory feel-as-spine vs NI mandate (auditor accepted defense; audience rejected); dialogue sidecar citation-completeness (auditor missed); dialogue-wren "your hand" lore-leak (auditor missed); sensory modality silent-gaps and old-state lineage (auditor missed across cycles 1-3)
- **Auditor-only findings:** SIGNAL-class metadata + slug inconsistencies that audience did not surface (not their lens)
- **Bidirectional loop verdict:** VALIDATED — multiple shared findings across the two paths; the audience caught seams the auditor's mechanical scan could not articulate; the auditor caught structural integrity issues the audience didn't reach for.

## Pipeline process observations (carry-forward to upstream tuning)

1. **R2 stale-shard problem.** Pre-session R2 shards in `staff/*/r2-decision-shard.md` were authored against an earlier R1 draft whose anchors did not match the locked R1 cite-index. The shards' add-justifications referenced anchors that don't resolve. Phase 4a consolidation captured this as a `graph-reconciliation-note` in `.r2-decisions.md` but the shard reasoning's substantive content was wasted relative to canonical state. Queue: rerun protocol must include "if any prior R2 shards exist on disk, verify against current cite-index BEFORE Phase 3 dispatch; stale shards force re-judge."

2. **Cite-index builder vs top-of-file annotations.** `build_cite_index.py` regenerates consolidated facets (feeling.md, state-updates.md) from per-source slices each time it runs, wiping inter-slice annotations. F-010 carve-out was inserted directly into the consolidated state-updates.md with explicit "do NOT rerun the builder" instruction. Queue: builder should support a preserved `# pragma carve-out` preamble between frontmatter and first source block.

3. **Modality vs. sparsity band collision in sparse-chapter authoring.** Sensory facet's 2-modality floor + 3-6% sparsity band collide arithmetically on a 27-bone chapter — both 1 entry (under-band) and 2 entries (slightly over-band) are arithmetically problematic. Cap-burn on sensory rests partly on this collision. Queue: rubric needs explicit per-chapter-size handling or integer-floor exemption for sparse chapters.

4. **Feel-as-spine rubric gap.** Memory's cross-facet contract requires NI co-citation. The cycle 1+2+3 audience uniformly rejected the feel-as-spine defense even when the substance is interior-feeling-of-rule-catching (which IS rendered structurally by feel:1 + vibes:17). The rubric needs either (a) explicit feel-as-spine carve-out clause for substance-interior-to-feeling beats in flat-low zones, OR (b) explicit forbidden-pattern enumeration so authors cannot attempt the defense. Queue for rubric authority.

5. **Cycle-3 fixer introduced a new HARD.** Adding sensory:3 @17 to clear modality silent-gap created an old-state lineage gap (no prior sound/time baseline at @17). Pattern: an add-fix at cycle N can produce a new finding that the same cycle's audit doesn't catch (only the next cycle's audience surfaces it). Queue: fixer dispatches that ADD entries should run a self-check against the rubric REJECT signatures before completing.

## Recommendation

Status `audited-r1-mechanical` stays. Status `audited-r1` is NOT set per spec. `audience_gate_cap_burned: true`. The two failing facets (sensory, memory) remain in their cycle-3 state on disk; they ARE consumable by downstream stitcher with the awareness that the audience has flagged unresolved issues. The orchestrator-critic verdict (below in master summary) is NOT-SUCCESSFUL per the critic card's explicit hot-button: "Cap-burn is a NOT-SUCCESSFUL verdict, not a 'ship anyway' license."
