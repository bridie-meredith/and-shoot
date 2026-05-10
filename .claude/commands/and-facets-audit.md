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

**Auditor task — five classes of finding:**

1. **CONTRADICTION** — Two facet entries set incompatible state on the same anchor. Examples:
   - Two state-updates with same `<target>.<field>: <old> -> <new-A>` and `... -> <new-B>` on the same protoline.
   - location-state at one protoline that conflicts with a referenced loc card's spatial layout.
   - tens rating that contradicts a co-cited state-update peak (tens=1 with state change is suspicious; tens=3 without state change is suspicious — both flag for review).
   - Schema § "Cross-facet consistency": "**delete both, flag for re-author. Do not pick a winner.**" — at flag-only mode, auditor does not delete; both are flagged.

2. **DEDUP** — Two entries (same or different facets) that say the same thing on the same anchor. Examples:
   - NI@X register that paraphrases feeling@X somatic-tell.
   - memory@X gloss that paraphrases NI@X register.
   - vibes@X token-bundle that duplicates state-update@X field-flip semantics.

3. **SUPERFLUOUS** — Entries that earn nothing in the graph. Inputs:
   - Cite-index "Lonely entries" list (zero co-location, zero inbound license).
   - Cross-check against per-facet rubric: is the entry rubric-licensed independent of co-location? (E.g., a tens=2 entry with no NI co-cite may still be earned via stakes-visibility; not all lonelies are superfluous.)
   - The auditor's call is whether the lonely entry survives rubric scrutiny — flag if not.

4. **CONSTRAINT** — Cross-facet contract violations. Examples (per facet rubrics):
   - memory entry without NI-spine co-citation (§memory rubric mandatory spine).
   - metaphor entry without licensed-by anchor that resolves (§metaphor mandatory anchor).
   - feeling entry that duplicates POV NI register on same protoline (§feeling POV non-redundancy).
   - vibes entry with `licensed-by:` source that doesn't resolve (§vibes machine-resolvable mandatory).
   - state-updates entry with `<old>` field that contradicts the prior state-update or state.md baseline.
   - Series-law violations on any facet (e.g., a memory gloss that breaches Earth-Bet hard fence).

5. **PILE-UP REVIEW** — Protolines with >6 co-located facets. Cite-index lists these. The auditor judges whether each is a load-bearing peak (warranted) or over-decoration (recommend cull). Per the locked tens cross-facet contract, peak protolines (@99, @35, @119, @69, @130) earn dense co-location; the audit verifies each pile-up is structurally justified.

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
