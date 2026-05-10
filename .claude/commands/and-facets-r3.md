---
description: Round 3 relaxation judge — repeat hybrid judge against post-Round-2 state. Step E of the Beta three-pass facet pipeline. Output - mutates active-project/theater/facets/ + rebuilds _cite-index.md. Usage - /and-facets-r3 [episode-slug]
---

Round-3 facet pipeline. Re-runs the four **midband** facet authors against the post-R2 graph + refreshed cite-index. Same operation as Round 2 (per-entry judge: keep / delete / add); the difference is that R3 reads the post-R2 state, not the post-R1 state. R3 is the **relaxation** iteration that lets the system settle after R2 mutations cascade.

You are the orchestrator. Showrunner is read-only memory.

**Convergence hypothesis (per `design/shoot-v2/three-pass-alpha-design.md` § "Empirical measurement plan"):**
- R3 diff per facet should be **smaller** than R2 diff (system settling).
- Per-facet zero-change rate is the signal for whether R3 is structurally necessary; high zero-change rate per facet → that facet can skip R3 in production (Step I decision input).
- Oscillation (R2 added X → R3 deletes X; or R2 deleted Y → R3 re-adds Y) is the diagnostic for whether the rounds converge or hunt. Single-pass R3 surfaces this; if oscillation rate is high, Step I adds Gamma machinery.

## Args

- `$1` — optional. Episode slug. If omitted, use `active.episode` from showrunner memory.

---

## Phase 0 — Validate

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - Episode status: `faceted-r2`.
   - `round_2_complete: true` flag present.
3. Confirm all nine facet files + `_cite-index.md` exist.
4. Read `_cite-index.md` to confirm it is a post-R2 build (mtime newer than R2 facet mutations).
5. If cite-index is stale (built before R2 mutations), rebuild first:
   ```bash
   python3 active-project/staff/cite-index/build_cite_index.py <slug>
   ```

Print:
```
Episode: <slug>
Status: faceted-r2 → entering Round 3 (relaxation judge)
Cite-index: post-R2 (verified)
Beginning Round 3 — 4 midband facets, judge mode, sequential.
```

---

## Round 3 — Relaxation judge

**Same dispatch discipline as Round 2:**
- Sequential within Round 3 (shared protoline file).
- Full nine-facet graph + cite-index in every dispatch payload.
- Self-scoped deletion only.
- Citation cascade on delete.
- Per-entry decision logged.
- No reordering of existing IDs; deleted IDs leave gaps; new entries take next-available IDs.

**R3-specific cap (tighter than R2):**
- NI: ≤3
- memory: ≤3
- feeling: ≤3 per character
- metaphor: ≤2

R3 is the settling pass; tighter caps favor convergence over enrichment. If an author has more than the cap of strong candidates, that's a signal R2 underdelivered and the surplus surfaces as flags for the final audit (Step G).

**Each dispatch returns:** R2 → R3 diff (keep / delete / add), zero-change verdict (Y if no mutations), oscillation flags (entries reverted from R2 add or re-added from R2 delete), cap-refusals.

---

### Layer R3.1 — narrator-interest (POV impersonator, relaxation judge)

Dispatch **impersonator** loaded with the POV character with the same payload as R2.1 plus:
- Read the **post-R2 NI file** (24 entries; narrator:22-26 are R2 adds; narrator:5 + narrator:8 IDs are deletion gaps).
- Read the **post-R2 cite-index** for current lonely + pile-up state.

**Task — per existing post-R2 NI entry:**
- KEEP — R2 decision still holds; the R3 read does not surface a reason to revisit.
- DELETE — R2 add that, on second look against the now-stable graph, fails the rubric or is structurally redundant. **Oscillation flag**: if you delete an R2 add, log it explicitly so Step I can measure.

**Task — adds (cap ≤3):**
- Niches that R2 missed AND that the post-R2 graph reveals as load-bearing.
- New IDs continue from current max.

**Citation cascade + add-write** as R2.

**Output:** mutated `active-project/theater/facets/interest-narrator.md`. Header: bump `round:` to 3; add `r2_to_r3:` summary.

---

### Layer R3.2 — memory (POV impersonator, relaxation judge)

Same shape as R3.1, for memory.

**Task — per post-R2 memory entry:** KEEP / DELETE.
**Task — adds (cap ≤3):** new niches.

**Output:** mutated `active-project/theater/facets/memory.md`. Header bumps.

---

### Layer R3.3 — feeling (per-character impersonators, relaxation judge)

For each slug in `cast:`, dispatch as R2.3 with:
- Read post-R2 feeling file (12 entries across 3 characters).
- Same per-character self-scope (Taylor judges only Taylor's section, etc.).
- Cap ≤3 per character (tighter than R2's ≤5).

**Output:** mutated `active-project/theater/facets/feeling.md`. Header bumps.

**Sequence cast in `cast:` order; one fork at a time.**

---

### Layer R3.4 — metaphor (editor, relaxation judge)

Same shape as R2.4, for metaphor.

**Task — per post-R2 metaphor entry:** KEEP / DELETE.
**Task — adds (cap ≤2):** new niches; refuse-by-default discipline tighter at R3.

**Output:** mutated `active-project/theater/facets/metaphor.md`. Header bumps.

---

## Phase 6 — Persist

1. Confirm all nine facet files exist; protoline body unchanged.
2. Update `active-project/staff/showrunner/memory.md`:
   - Status: `faceted-r2` → `faceted-r3`.
   - Add `round_3_complete: true`.
3. Print summary (below).

## Phase 7 — Rebuild cite-index + measurement

```bash
python3 active-project/staff/cite-index/build_cite_index.py <slug>
```

The rebuilt cite-index reflects R3 mutations. Measurement deltas to capture:
- **Per-facet R2→R3 diff size** (should be smaller than R1→R2 diff for that facet).
- **Per-facet R3 zero-change rate** (KEEP-only decisions; no D/A).
- **Oscillation count** (entries flipped between R2 and R3 across the same anchor).

These feed Step I (oscillation measurement / convergence machinery decision).

### Print summary:

```
--- ROUND 3 FACETS COMPLETE: <episode-slug> ---

Per-facet R3 decisions (keep / delete / add):
  narrator-interest:    K=<n> D=<n> A=<n>  (cap-refusals: <n>; zero-change: <Y/N>; oscillation: <n>)
  memory:               K=<n> D=<n> A=<n>  (cap-refusals: <n>; zero-change: <Y/N>; oscillation: <n>)
  feeling:              K=<n> D=<n> A=<n>  (per-character: <slug>=K<n>/D<n>/A<n>; zero-change: <slug>=<Y/N>)
  metaphor:             K=<n> D=<n> A=<n>  (cap-refusals: <n>; zero-change: <Y/N>)

Diff comparison R2→R3 vs R1→R2 (settling check):
  narrator-interest:    R1→R2 = +<n>;  R2→R3 = +<n>  (settling: <Y/N>)
  memory:               R1→R2 = +<n>;  R2→R3 = +<n>  (settling: <Y/N>)
  feeling:              R1→R2 = +<n>;  R2→R3 = +<n>  (settling: <Y/N>)
  metaphor:             R1→R2 = +<n>;  R2→R3 = +<n>  (settling: <Y/N>)

Citation accrual: R2 <count> protolines decorated → R3 <count> (delta <±n>)

Cite-index rebuilt: active-project/theater/facets/_cite-index.md
  Pile-ups: <count>  (R2: <count>; delta <±n>)
  Lonely entries: <count>  (R2: <count>; delta <±n>)
  Bare protolines: <count>  (R2: <count>; delta <±n>)

Status: <slug> faceted-r3 (Round 3 complete; Step E shipped — final audit Step G deferred)
```

---

## Convergence

R3 is single-pass. The convergence question is empirical: does R3 produce smaller diffs than R2, and do facets approach zero-change?

**Decision points after R3 (Step I input):**
- If R3 zero-change rate is high across all four facets → R3 is structurally unnecessary; default-skip in production unless flagged.
- If R3 produces meaningful diffs but no oscillation → R3 is doing settling work; keep.
- If oscillation rate is non-trivial → R3 is hunting; Step I adds Gamma machinery (oscillation detector + zero-change skip + settling criterion).

If an author refuses to judge, log under `active-project/staff/<author>/` and continue. Summary lists refusals; episode is not blocked.

---

## Notes

- **Step E scope only.** Final audit (Step G) deferred.
- **Oscillation flags are diagnostic, not punitive.** R3 is allowed to revert an R2 decision if the rubric reads cleaner against the post-R2 graph. The flag exists so Step I can decide if the system is converging or hunting.
- **No cite-index mid-layer rebuild.** Same default as R2 — protoline state is read fresh by each next dispatch.
- **R3 caps are tighter than R2.** This biases toward settling. If an author wants to author beyond cap, the surplus surfaces as flags for Step G.
