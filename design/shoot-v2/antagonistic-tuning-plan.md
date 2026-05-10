---
design: antagonistic-facet-tuning-plan
date: 2026-05-10
relates-to: facet-tuning-process.md, three-pass-alpha-design.md, rubric-*.md
status: PLAN — not yet executed
trigger: user direction 2026-05-10d — "put a plan together to use the antagonistic facet tuners as well, now that we have a second pass with different inputs to train on"
---

# Antagonistic Facet Tuning — Plan

## Premise

We have two passes of facet output on s01e01:

- **R1 entries** — authored blind against bones-only protolines.
- **R2 entries** — kept / deleted / added by graph-aware judge dispatches reading the full Round-1 graph + cite-index.

Plus 5 residual soft-flag findings from the post-remediation audit.

This is **two-population training corpus**:
- R1-kept-by-R2 — entries that survived graph review. Adversarial attack tests rubric floor.
- R1-deleted-by-R2 — entries that failed graph review. Adversarial validates the deletion call.
- R2-added — entries authored under full-graph visibility. Adversarial tests whether the add is rubric-defensible.

The user direction reframes Phase 3 of `facet-tuning-process.md` (adversarial seam-finding) as the natural next move: now that there are two distinct authoring conditions producing facet entries on the same source material, the audience can attack across both populations and the rubric's robustness becomes measurable.

## What "antagonistic facet tuners" means in this codebase

Phase 3 of `facet-tuning-process.md`:

> "Even on accepts, the audience produces hostile counter-arguments — the strongest single attack per unit ('the seam'). Output is *defense scaffolding*, not new verdicts."

The "antagonistic facet tuners" are the **3 active audience personas** firing in adversarial mode against facet entries:

- `dark-fantasy-reader` (atmosphere lens)
- `pulp-enthusiast` (board-move / momentum lens)
- `worm-canon-pedant` (voice-precision + source-material-fidelity lens)

In tuning mode, each persona reads each unit (facet entry) and attacks through its lens. Aggregate to **one strongest seam per unit**. Then the facet author defends or revises.

This is the same shape as `audience-review-originals*.md` and `round2-output-*.md` artifacts under `design/shoot-v2/`, generalized from dialogue to facets.

## Why now

Three reasons:

1. **Two populations to compare.** R1 and R2 give the audience contrastive signal — "why was this kept vs deleted? was the kept one really stronger, or did R2 miss something the audience would catch?" Single-pass corpora don't carry this signal.

2. **Audit findings name the soft floor.** The 5 residual audit flags (mem:2/3/8 approach-zone; mem:5/8 paraphrase) are exactly the kind of seams the audience would press on. The audit caught structural and rubric-mechanical issues; the audience pressure-tests the *taste* layer the rubric can't formalize alone.

3. **Rubric ambiguity has surfaced.** "Release-zone" in the memory rubric is unquantified; "trailing-edge" in metaphor is unquantified. Adversarial pass with audience defense scaffolding produces the discrimination cases the rubric needs to quantify these.

## Scope of first run

**Single facet, one episode.** Pick the facet with the densest unresolved tension. Memory is the natural target:

- 8 entries (small, tractable)
- 3 of 8 have soft-flag concerns from the audit
- 2 of 8 have DEDUP soft-flags with NI
- The "release-zone" rubric ambiguity sits here

Memory's R1 set was 4 entries; R2 added 4 (mem:5-8); R3 zero-change held. The R2 adds are the test cases — under-the-graph authoring against under-the-bones authoring, same author (Taylor impersonator), different inputs.

## Plan — five phases per `facet-tuning-process.md`

### Phase A — Corpus prep

1. **Sample.** Lift the 8 memory entries (mem:1-8) from `active-project/theater/facets/memory.md` plus their context:
   - Anchor protoline + adjacent ±2 protolines
   - Co-located NI / feeling / vibes entries on the anchor
   - Tens rating at anchor + ±2
   - Loc-state environment frame
   - Author-time provenance: `R1` (mem:1-4) or `R2` (mem:5-8)
2. **Group by rubric category.** The memory rubric has `monument-clamp` vs `intra-episode-callback` vs `world-build-reference` types. Each entry assigned one type for adversarial framing.
3. **Lock the rubric snapshot.** `design/shoot-v2/rubric-memory-flags.md` as it stands today is the V2 locked rubric. The audience attacks under this rubric; rubric does not move during the run.

Output: `design/shoot-v2/memory-tuning-r2-corpus.md` — the 8 entries with full context.

### Phase B — Reviewer baseline (skipped — already done)

R1 and R2 dispatches already locked the rubric and produced reviewer verdicts (audit r1 + r2). The Phase-2-equivalent regenerated-units accept rate is 100% (audit cleared 4 of 4 hard findings; 5 soft remain).

This phase is the floor we're attacking from. Document the floor:

- 8 entries; locked rubric; 5 soft flags from audit-r2.
- Adversarial seams should pressure the soft flags hardest.

Output: `design/shoot-v2/memory-tuning-r2-baseline.md` — 1-paragraph summary of where the file stands entering adversarial pass.

### Phase C — Adversarial seam dispatch

**Three audience persona forks, one fork per persona.** Each fork:

- Loads its persona card (`active-project/audience/<persona>/card.md`).
- Reads the 8 memory entries with full context (Phase A output).
- Reads the locked rubric.
- For each of the 8 entries, produces:
  - **Seam-one-clause:** the strongest single attack through its persona lens.
  - **Severity:** STRONG / MODERATE / THIN.
  - **Rubric-line cited:** what specific rubric clause the seam pressures.

Forbidden: persona may not propose deletes, may not write new entries, may not redirect to another facet. Adversarial scope is attack-only.

Output per persona: `design/shoot-v2/memory-tuning-r2-seams-<persona>.md` — 8 attacks.

### Phase D — Aggregate to single seam per entry

A fourth dispatch (auditor or main-session synthesis — TBD which is cleaner) reads all three persona seam files and aggregates:

For each entry:
- The strongest single seam across the three personas.
- If two personas converge on the same seam, weight increases.
- If personas split (different attack vectors), pick the one whose rubric-line citation is sharpest.

Output: `design/shoot-v2/memory-tuning-r2-seams-aggregated.md` — 8 strongest seams.

### Phase E — Defense or revision

The memory facet author (POV impersonator, fresh fork) reads:

- The 8 entries.
- The aggregated seams from Phase D.
- The rubric.

For each entry:

- **DEFEND** (with rubric citation in 2-4 sentences) — entry stays as authored; the seam attacks an intended rubric feature, not a fault.
- **REVISE** (multi-draft + chosen mark + how the seam is answered + which rubric signatures are demonstrated) — entry is rewritten; the seam was load-bearing.
- **WITHDRAW** (delete; cascade-strip from protoline) — the seam exposed a fault the entry cannot defend.

Output: mutated `active-project/theater/facets/memory.md` + a `design/shoot-v2/memory-tuning-r2-defense.md` log of decisions.

### Phase F — Final adjudication

Three audience persona forks (fresh) re-review the post-Phase-E memory file under the same locked rubric. Verdict per entry: ACCEPT / REJECT-{reason}. Aggregate accept rate.

**Cross-unit dependency check:** mem:5 + narrator:26 (DEDUP soft flag from audit) gets adjudicated together; mem:8 + narrator:25 same.

**Shippability assessment:** named residual failure modes; honest call on what didn't fully close.

Output: `design/shoot-v2/memory-tuning-r2-final.md` — accept rate + named residuals.

### Phase G — Rubric carry-back (if surfaced)

If the run reveals rubric gaps (likely: "release-zone" beat-distance quantification; "trailing-edge" definition), capture them as proposed rubric edits:

- New rubric version: `design/shoot-v2/rubric-memory-flags.md` V2.1 (or fork to V3 if structural).
- Rubric edits documented in `design/shoot-v2/memory-tuning-r2-rubric-deltas.md`.
- Lock V2.1; do NOT re-tune mem:1-8 against V2.1 in the same pass (lift comparisons require fixed rubric).

The next episode through the pipeline will run against V2.1 and serve as the validation corpus.

## Deliverables

After Phase G, the run has produced:

1. Mutated `memory.md` (entries refined under adversarial pressure).
2. Six tuning artifacts under `design/shoot-v2/memory-tuning-r2-*.md`.
3. Optional: rubric V2.1 if seams surface a rubric gap.
4. Final accept rate and named residuals.

## Estimated cost

- Phase A: 1 dispatch (corpus prep — synthesis-style work).
- Phase C: 3 parallel persona dispatches (audience).
- Phase D: 1 dispatch (aggregate — auditor or main).
- Phase E: 1 dispatch (memory author defense/revise).
- Phase F: 3 parallel persona dispatches (audience adjudicate).

Total: 9 dispatches plus orchestration. Comparable to one R2 round (which was 6 dispatches). Tractable.

## Sequencing across facets

If the memory run produces useful signal:

1. **Memory** (this plan) — densest unresolved tension; smallest entry count for first pass.
2. **Feeling** — 12 entries across 3 characters; per-character scenes; harder coordination but useful.
3. **Narrator-interest** — 24 entries; spine of the facet graph; substantial work but high-value.
4. **Metaphor** — 0 entries currently; nothing to tune until R2 produces something to attack.
5. **Vibes** — 21 entries; cross-facet bias layer; tune last because the rubric's `licensed-by:` machine-resolvability is mechanical, not adversarial.

The audit's per-facet rubrics (tens, loc-state, sensory, state-updates) are mechanic-rated facets; adversarial tuning is less applicable. They benefit more from the audit's mechanical scan upgrades (see `and-facets-audit.md`).

## Open questions for the user

1. **Start with memory** as proposed, or pick a different first facet?
2. **Run R2 corpus only** (mem:5-8) or **full R1+R2 corpus** (mem:1-8)? The R2 corpus is the new training data; R1 is the comparison baseline.
3. **Audience aggregation** (Phase D) — auditor fork or main-session synthesis?
4. **Rubric carry-back** (Phase G) — should rubric edits land in this run, or be deferred to a separate rubric-tuning session that uses this run's seam-output as input?
5. **Build a `/and-facets-tune` command**, or run the plan as ad-hoc dispatches the first time and command-ize after we know the shape?

## Build vs run sequencing

Recommended:

1. Confirm plan (this document) — quick user review of the 5 open questions.
2. **Run ad-hoc on memory** for the first pass — too many open questions to commit to a command yet.
3. **Capture the actual flow** during the run — what worked, what didn't, where the briefs needed expansion.
4. **Command-ize as `/and-facets-tune <facet-slug>`** after the memory run produces working artifacts. Then the feeling and NI runs can use the command.

This mirrors the `/and-facets` build trajectory: Step A → Step D → Step G → consolidation. The first pass surfaces the brief-shape problems (e.g., explicit absolute paths required for impersonator dispatches); the consolidated command bakes in the lessons.

## Not in scope (this plan)

- **Auditor tuning.** Step G design says auditor-tuning is a separate facet-tuning-process run. Worth scheduling but not part of this plan.
- **Rubric tuning across all 9 facets.** This plan is per-facet. The cross-facet rubric coherence question (e.g., "release-zone" semantics shared between memory and metaphor) is a follow-on once individual rubrics have been pressure-tested.
- **Re-running on s01e02+.** This plan targets s01e01's output; the next-episode validation corpus is a follow-on once s01e01 stabilizes.
