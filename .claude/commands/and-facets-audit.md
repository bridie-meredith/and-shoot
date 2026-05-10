---
description: Final cross-cutting audit of the facet graph. Step G of the Beta three-pass facet pipeline. Flag-only mode (auditor not yet tuned for delete-authority). Output - active-project/staff/auditor/facets-final-audit.md. Usage - /and-facets-audit [episode-slug]
---

Final audit of the facet graph for one episode. Cross-cutting constraint check, dedup, superfluous-removal candidates, contradiction detection. Reads the full graph as a unit; reports classified findings.

**Mode: flag-only.** Per `design/shoot-v2/three-pass-alpha-design.md` § "Final audit teeth": until the auditor itself is tuned (rubric, thresholds, refusal discipline), findings are routed back to facet authors as flags rather than executed as deletes. Once tuned (separate work), the auditor's deletions become final and cross-facet — but not yet.

You are the orchestrator. One dispatch to the auditor with the whole graph in payload.

## Args

- `$1` — optional. Episode slug. If omitted, use `active.episode` from showrunner memory.

---

## Phase 0 — Validate

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - Episode status: `faceted-r2` or `faceted-r3` (either is acceptable input — R3 is optional per Step I default-skip when R2 converged).
3. Confirm all nine facet files + `_cite-index.md` exist.
4. If cite-index is stale (older than the most recent facet mutation), rebuild:
   ```bash
   python3 active-project/staff/cite-index/build_cite_index.py <slug>
   ```

Print:
```
Episode: <slug>
Status: <faceted-r2 | faceted-r3> → entering final audit (flag-only)
Cite-index: post-final-round (verified)
Beginning Step G — single auditor dispatch with full nine-facet graph.
```

---

## Audit dispatch

Dispatch **auditor** (fork) with:

**Read inputs (full graph):**
- Proto-lines: `active-project/theater/proto-lines/<slug>.md` (with all citations accrued).
- All nine facet files at `active-project/theater/facets/`:
  - `tensometer.md`, `location-state.md`, `interest-narrator.md`, `sensory.md`, `state-updates.md`, `memory.md`, `feeling.md`, `metaphor.md`, `vibes.md`.
- Cite-index: `active-project/theater/facets/_cite-index.md`.
- All active warehouse cards (`active-project/warehouse/*.card.md`) — for constraint checks against cond-* and loc-* cards.
- Series + season plans (showrunner memory) — for series-law constraint checks.
- Schema: `schemas/facet.schema.md` — for cross-facet contract verification.
- Audit report schema: `schemas/audit-report.schema.md` — for output structure.

**Forbid loading:** behavior cards, vibes-as-bias, audience personas, source prose. The auditor reads the graph mechanically against constraints, not aesthetically.

**Auditor task — eight classes of finding:**

1. **STRUCTURAL** — Schema/format/integrity defects. Mechanical scan:
   - Header presence: every facet file MUST carry `facet:`, `episode:`, `author:` (or `authors:`), and `round:` (or equivalent round-marker). Missing or malformed fields fault.
   - Line shape: every numbered entry matches `<id> @<proto-id> <content>` (or off-anchor `<id> <content>` for vibes). Malformed lines fault.
   - ID monotonicity: IDs strictly increasing within each facet file. Deletion gaps allowed; duplicates and out-of-order IDs fault.
   - Anchor resolution: every `@<proto-id>` points to an actual content-bearing protoline ID (not a deleted gap, not a time-skip blank line). Orphan anchors fault.
   - Bidirectional citation: if entry X anchors at @P with content, then @P MUST have `[<facet-prefix>:X]` in its citation list (documented exception: tens entries with rating=1 do not back-cite by convention). Missing back-cites and orphan back-cites both fault.
   - Protoline body integrity: SVO sentences must NOT have changed since extraction; only the trailing `[...]` citation lists may grow or shrink. Body changes fault.

2. **FREQUENCY-BAND** — Per-rubric quantitative gates. Compute and compare against the rubric's stated bands:
   - **tensometer** rubric § "Frequency band": 60-75% rung-1 / 20-30% rung-2 / 5-10% rung-3. Compute the actual distribution; flag every rung outside band.
   - **sensory** rubric: sparsity 3-6%; modality coverage ≥2 per episode.
   - **memory** rubric: sparsity ~5-12% (or 1-5% per the older spec — read the current rubric to see which is locked).
   - **feeling** rubric: sparsity 2-5% per character.
   - **metaphor** rubric: sparsity 0-3% (zero-fires acceptable).
   - **NI** rubric: density expectation (typically 15-25%).
   - **state-updates**: no fixed band but tens-coherence soft-gate.
   - **vibes**: liberal; no upper ceiling per schema (don't flag).
   These are signal-flags not auto-faults, but record the actual numbers so the human can read settling vs miscalibration.

3. **METADATA-INCONSISTENCY** — File headers / round-notes / r1_to_r2 / r2_to_r3 summary lines that contradict the file's actual content. Examples:
   - Header `round: N` doesn't match the latest mutation.
   - `r2_to_r3: K=N D=N A=N` counts that don't match the actual entries plus deletion gaps.
   - Round-note claims like "all entries at tens=1 or trailing-edge" when at least one entry demonstrably is not.
   - Authoring discipline notes that don't match actual content.

4. **CURVE-SHAPE** — Tens-rubric § "Curve-shape rubric (episode-level)" verdict. Mandatory under the locked tens rubric:
   - Scene-level: each loc-state-defined scene contains at least one tens=3 (or an explicit dramatist-flagged exception). Flag scenes that have no peak.
   - Rise-to-peak: 1→3 direct jumps flag for review (either misrating or sudden-turn).
   - Release-after-peak: 3→3 immediately flagged unless defensible double-tap.
   - No flatlining: 30+ contiguous content-bearing beats with no 2 or 3 flags as kickback candidate.
   - Episode-level act structure: visible major rise toward climax. Climax beat exists and is unique-or-near-unique (densest 3-cluster).
   - Output: SHAPE-OK or SHAPE-FAIL with named scene/episode failure mode.

5. **CONTRADICTION** — Two facet entries set incompatible state on the same anchor. Examples:
   - Two state-updates with same `<target>.<field>: <old> -> <new-A>` and `... -> <new-B>` on the same protoline.
   - location-state at one protoline that conflicts with a referenced loc card's spatial layout.
   - location-state time-labels that run backward in chronological order across consecutive entries.
   - tens rating that contradicts a co-cited state-update peak (tens=1 with state change suspicious; tens=3 without state change suspicious — both flag).
   - Schema § "Cross-facet consistency": "**delete both, flag for re-author. Do not pick a winner.**" — at flag-only mode, both flagged.

6. **DEDUP** — Two entries that say the same thing.
   - **Cross-facet same-anchor**: NI@X register paraphrasing feeling@X somatic-tell; memory@X gloss paraphrasing NI@X register; vibes@X token-bundle duplicating state-update@X field-flip semantics.
   - **Within-facet different-anchor**: two memory entries firing the same monument on different beats without distinct callback content; two NI entries with identical register-language across protolines.
   - **Within-facet same-anchor**: two entries from the same facet at the same anchor (rare but should fault if found).

7. **SUPERFLUOUS** — Entries that earn nothing in the graph. Inputs:
   - Cite-index "Lonely entries" list (zero co-location, zero inbound license).
   - Cross-check against per-facet rubric: is the entry rubric-licensed independent of co-location? (E.g., a tens=2 entry with no NI co-cite may still be earned via stakes-visibility; not all lonelies are superfluous.)
   - Convention: tens entries with rating=1 are NEVER superfluous (they ARE the silence baseline).
   - Off-anchor vibes entries are NEVER superfluous (they're scope-targeted, not anchor-targeted).
   - The auditor's call is whether the lonely entry survives rubric scrutiny — flag if not.

8. **CONSTRAINT** — Cross-facet contract violations. Examples (per facet rubrics):
   - memory entry without NI-spine co-citation on the same protoline (§memory mandatory spine).
   - metaphor entry without `licensed-by:` anchor that resolves to an existing memory:N or feeling:N entry (§metaphor mandatory anchor).
   - feeling entry that duplicates POV NI register on same protoline (§feeling POV non-redundancy).
   - vibes entry with `licensed-by:` source that doesn't resolve OR forward-cites (source anchored AFTER the vibe's anchor) (§vibes machine-resolvable mandatory; gate-4).
   - **Mechanical resolvability scan: read every `licensed-by:` clause across metaphor and vibes; verify each cited (facet:id) exists and is anchored at-or-before the citing entry's anchor.**
   - state-updates entry with `<old>` that contradicts the prior state-update or state.md baseline.
   - Series-law violations on any facet (e.g., a memory gloss that breaches Earth-Bet hard fence — scan memory entry text for forbidden proper nouns: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, etc.).
   - **POV-perceptual access** on NI: every NI entry must anchor on a protoline where the POV character can perceive (POV present per cast/loc-state, not in another room).

9. **PILE-UP REVIEW** — Protolines with >4 co-located facets. Cite-index lists these. Verdict per pile-up: warranted (load-bearing peak) or over-decoration (recommend cull). Per the locked tens cross-facet contract, peak protolines earn dense co-location.

**Audit output — classified findings report:**

Write to `active-project/staff/auditor/facets-final-audit.md` per `schemas/audit-report.schema.md`. Structure:

```
audit: facets-final-r1
episode: <slug>
date: <YYYY-MM-DD>
mode: flag-only
status: <CLEAN | FINDINGS-PRESENT>
totals: <count> findings across <count> facets

---

## CONTRADICTION findings (<count>)
- [facet:id] @<proto> — <one-clause description> — paired with [facet:id] @<proto>.
- ...

## DEDUP findings (<count>)
- [facet:id] @<proto> — <one-clause description> — duplicates [facet:id].
- ...

## SUPERFLUOUS findings (<count>)
- [facet:id] @<proto> — lonely entry; rubric scrutiny: <pass | fail with rationale>.
- ...

## CONSTRAINT findings (<count>)
- [facet:id] @<proto> — <constraint name> — <violation description>.
- ...

## PILE-UP REVIEW (<count>)
- @<proto> (<n> facets) — verdict: <warranted | over-decoration> — <rationale>.
- ...

---

## Audit summary

- Total entries reviewed: <count>
- CONTRADICTION: <count>  (recommend: flag both for re-author)
- DEDUP: <count>          (recommend: cull lower-fidelity entry, keep higher)
- SUPERFLUOUS: <count>    (recommend: cull at next round if still lonely)
- CONSTRAINT: <count>     (recommend: route to original facet author for fix)
- PILE-UP REVIEW: <warranted-count> warranted / <over-count> over-decoration

## Routing

For each finding, name the facet author who owns the entry. In flag-only mode, no deletes are executed; the report is the deliverable.

## Mode note

This audit ran in flag-only mode per Step G design. Once auditor is tuned for delete-authority, findings of class CONTRADICTION/DEDUP/SUPERFLUOUS/CONSTRAINT will be executed as deletes (with citation cascade); PILE-UP REVIEW remains advisory.
```

**Auditor deliverable:** the report. No mutations to facet files. No protoline edits.

**Auditor return to orchestrator:** path to report; finding counts per class; one-line headline (CLEAN | FINDINGS-PRESENT with count).

---

## Phase 6 — Persist

1. Confirm `facets-final-audit.md` written.
2. Update `active-project/staff/showrunner/memory.md`:
   - Status: `faceted-r3` (or `faceted-r2`) → `audited-r1`.
   - Add `audit_path: active-project/staff/auditor/facets-final-audit.md`.
   - Add `audit_complete: true`.
   - Add `audit_findings: <count>` if non-zero.
3. Print summary:

```
--- FINAL AUDIT COMPLETE: <episode-slug> ---

Mode: flag-only

Findings:
  CONTRADICTION: <count>
  DEDUP:         <count>
  SUPERFLUOUS:   <count>
  CONSTRAINT:    <count>
  PILE-UP REVIEW: <warranted> warranted / <over> over-decoration

Total: <count> findings (CLEAN if zero)

Report: active-project/staff/auditor/facets-final-audit.md

Status: <slug> audited-r1 (Step G shipped — flag-only;
        delete-authoritative requires auditor tuning, separate work)
```

---

## Notes

- **Single-dispatch design.** The auditor reads the full graph in one fork. No layered review — that's redundant when each facet author has already done per-facet cull.
- **Flag-only is intentional.** The design defers delete-authority until auditor itself is tuned (rubric + threshold + refusal-discipline calibration via the same five-phase facet-tuning process applied to other facets). Until then, the report is the artifact and the facet authors handle remediation.
- **Routing back to facet authors is downstream.** When a CONSTRAINT finding names `[mem:<id>]` as missing NI-spine, the remediation runs through the memory facet author (POV impersonator). For now, this routing is left to the human; once auditor is tuned, it can be automated.
- **Audit re-run is cheap.** If facet files mutate (e.g., a fix round happens), re-run `/and-facets-audit` and overwrite the report. The audit is stateless beyond its inputs.
