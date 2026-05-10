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

10. **AP-SCAN — per-rubric anti-pattern detection.** Each facet rubric names anti-patterns the writer must resist (e.g., tens AP1 ambient-escalation, AP2 speech-beat-default, AP3 climax-bleed; memory AP-functional-callback; feeling AP-named-feeling-vocab; metaphor AP3 figurative-already-in-NI, AP7 default-refuse-at-tens-≠-3, AP12 non-POV-interior). Mechanically scan each entry against its rubric's named anti-patterns and flag any plausible AP-violation. The auditor cannot make the full taste call (some APs require persona context the auditor lacks), but can flag candidate AP-violations as signal for the audience-tuning loop.

   Examples:
   - tens entry rated 2 or 3 with no axis-citation → AP4 plot-importance-inflation candidate.
   - memory entry whose description paraphrases a co-located NI entry → AP-figurative-already-in-NI candidate.
   - feeling entry containing forbidden vocabulary (named-feeling words: "anxious", "nervous", "happy", "sad", "afraid", "tense", "calm", "angry", etc.; hedges: "like", "as if", "almost", "kind of"; "feels" verb) → AP-named-feeling-vocab violation.
   - metaphor entry on tens=2 or tens=1 without trailing-edge / dark-humor argument → AP7 default-refuse-violation.
   - vibes entry whose `licensed-by:` source list contains only a single source → AP-multi-source-preferred candidate (single-source is permitted but flagged for multi-source preference).
   - vibes entry whose token-bundle contains a sentence-parsable token (subject + finite verb + object) → AP8 sentence-parsability-violation.

11. **TASTE-FLAG — audience-attack-anticipation candidates.** Per user direction 2026-05-10e ("the auditor should be able to catch the same sort of mistakes we penalize during tuning"), this class anticipates seam-attacks that the audience would produce in adversarial-tuning mode. Flag entries that are mechanically suspicious for taste-level weakness even though the auditor cannot fully execute the taste call:

   - **atmosphere-thin** — entries that read as informational rather than load-bearing in the project's dark-fantasy register. Particularly NI on ostensibly-charged beats that doesn't carry the doubled-register weight; sensory deltas that fail the disambiguation gate; feeling tells that don't card-match.
   - **momentum-stall** — entries whose register repeats the prior entry's register on adjacent protolines without distinct functional contribution. Particularly NI/memory entries that fire similar registers across consecutive beats.
   - **voice-fidelity** — entries that fail to honor character voice or source-material register. Particularly memory entries whose Earth-Bet displacement reads as generic-veteran rather than project-specific (Taylor's control-calculus / swarm-monument / cape-reflex patterns).

   TASTE-FLAG is signal-only at flag-only mode. Patterns surfaced here become tuning input — the audience-tuning runs validate or refute the auditor's flag. Over time, refined patterns become AP-SCAN entries (mechanical) once they're codified in the rubric. **The audit + tuning loop is bidirectional: tuning surfaces patterns; auditor codifies them; auditor catches them next time mechanically.**

**Audit output — classified findings report:**

Write to `active-project/staff/auditor/facets-final-audit.md` per `schemas/audit-report.schema.md`. Structure:

```
audit: facets-final-r<N>
episode: <slug>
date: <YYYY-MM-DD>
mode: flag-only
status: <CLEAN | FINDINGS-PRESENT>
totals: <count> findings across <count> facets

---

## STRUCTURAL findings (<count>)
- [facet:id] — <missing-header | malformed-line | id-non-monotonic | orphan-anchor | missing-back-cite | orphan-back-cite | body-changed> — <description>.

## FREQUENCY-BAND findings (<count>)
- <facet>: actual <n%>; band <range>%; <within | breach-low | breach-high>.
- Per-facet table: tens 1-rung %, 2-rung %, 3-rung %; sensory sparsity; memory sparsity; feeling per-character sparsity; metaphor sparsity; NI density.

## METADATA-INCONSISTENCY findings (<count>)
- <file>: <header-claim> contradicts <file-content-fact>.

## CURVE-SHAPE verdict
- Episode-level: <SHAPE-OK | SHAPE-FAIL with named failure mode>.
- Per-scene: scene-1 <peak-present | no-peak>, scene-2 ..., etc.
- Adjacency: <count> 1→3 jumps; <count> 3→3 sequences (defensible / suspect).
- Flatlining: <count> stretches of 30+ contiguous beats with no 2 or 3.

## CONTRADICTION findings (<count>)
- [facet:id] @<proto> — <one-clause description> — paired with [facet:id] @<proto>.

## DEDUP findings (<count>)
- [facet:id] @<proto> — <one-clause description> — duplicates [facet:id]; type: <cross-facet-same-anchor | within-facet-different-anchor | within-facet-same-anchor>.

## SUPERFLUOUS findings (<count>)
- [facet:id] @<proto> — lonely entry; rubric scrutiny: <pass | fail with rationale>.

## CONSTRAINT findings (<count>)
- [facet:id] @<proto> — <constraint name> — <violation description>.

## AP-SCAN findings (<count>)
- [facet:id] @<proto> — AP<N> <name> — candidate violation; <description>.

## TASTE-FLAG findings (<count>)
- [facet:id] @<proto> — <atmosphere-thin | momentum-stall | voice-fidelity> — <rationale>; signal-only.

## PILE-UP REVIEW (<count>)
- @<proto> (<n> facets) — verdict: <warranted | over-decoration> — <rationale>.

---

## Audit summary

- Total entries reviewed: <count>
- STRUCTURAL: <count>            (HARD — fix before any next round)
- FREQUENCY-BAND: <count>        (signal — investigate before shipping)
- METADATA-INCONSISTENCY: <count> (fix at next file-touch)
- CURVE-SHAPE: <SHAPE-OK | SHAPE-FAIL>
- CONTRADICTION: <count>         (recommend: flag both for re-author)
- DEDUP: <count>                 (recommend: cull lower-fidelity entry)
- SUPERFLUOUS: <count>            (recommend: cull at next round if still lonely)
- CONSTRAINT: <count>             (recommend: route to original facet author)
- AP-SCAN: <count>                (recommend: route to original facet author or escalate to audience-tuning)
- TASTE-FLAG: <count>             (signal-only; tuning input)
- PILE-UP REVIEW: <warranted> warranted / <over> over-decoration

## Routing

For each finding, name the facet author who owns the entry. In flag-only mode, no deletes are executed; the report is the deliverable.

## Mode note

This audit ran in flag-only mode per Step G design. Once auditor is tuned for delete-authority, HARD-class findings (STRUCTURAL, CONTRADICTION, DEDUP, SUPERFLUOUS, CONSTRAINT) will be executed as deletes (with citation cascade). FREQUENCY-BAND, METADATA-INCONSISTENCY, AP-SCAN, TASTE-FLAG, PILE-UP REVIEW remain advisory.

The audit + tuning loop is bidirectional: tuning surfaces seam-attack patterns; the auditor codifies them as new AP-SCAN entries; the auditor catches them mechanically next time. TASTE-FLAG is the staging area for patterns that are taste-suspicious but not yet codified — audience-tuning runs validate or refute, then graduate them to AP-SCAN.
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
Curve-shape verdict: <SHAPE-OK | SHAPE-FAIL — <reason>>

HARD findings (block any next round if not addressed):
  STRUCTURAL:           <count>
  CONTRADICTION:        <count>
  DEDUP:                <count>
  SUPERFLUOUS:          <count>
  CONSTRAINT:           <count>

SIGNAL findings (advisory):
  FREQUENCY-BAND:        <count>  (per-facet bands; investigate before ship)
  METADATA-INCONSISTENCY: <count>
  AP-SCAN:                <count>  (rubric anti-pattern candidates)
  TASTE-FLAG:             <count>  (audience-attack-anticipation)
  PILE-UP REVIEW:         <warranted> warranted / <over> over-decoration

Total: <count> findings (CLEAN if zero hard)

Report: active-project/staff/auditor/facets-final-audit.md

Status: <slug> audited-r<N> (Step G; flag-only mode;
        delete-authoritative requires auditor tuning, separate work)
```

---

## Notes

- **Single-dispatch design.** The auditor reads the full graph in one fork. No layered review — that's redundant when each facet author has already done per-facet cull.
- **Flag-only is intentional.** The design defers delete-authority until auditor itself is tuned (rubric + threshold + refusal-discipline calibration via the same five-phase facet-tuning process applied to other facets). Until then, the report is the artifact and the facet authors handle remediation.
- **Routing back to facet authors is downstream.** When a CONSTRAINT finding names `[mem:<id>]` as missing NI-spine, the remediation runs through the memory facet author (POV impersonator). For now, this routing is left to the human; once auditor is tuned, it can be automated.
- **Audit re-run is cheap.** If facet files mutate (e.g., a fix round happens), re-run `/and-facets-audit` and overwrite the report. The audit is stateless beyond its inputs.
