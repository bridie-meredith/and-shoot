---
description: Round 2 hybrid judge — graph-aware per-entry keep/delete/add against the locked Round-1 output. Step D of the Beta three-pass facet pipeline. Output - mutates active-project/theater/facets/ + rebuilds _cite-index.md. Usage - /and-facets-r2 [episode-slug]
---

Round-2 facet pipeline. Re-runs the four **midband** facet authors against the full Round-1 graph + cite-index. Each author judges per-entry: keep, delete (self-scoped), or add. Citations cascade on delete; new entries follow the same per-facet rubric as Round 1.

You are the orchestrator. Each layer is one or more Agent dispatches. Showrunner is read-only memory.

**Pipeline shape (sequential within layer; layers in DAG order):**

```
locked Round-1 facets + _cite-index.md + proto-lines (citation-accrued)
        │
        ▼
   LAYER R2.1 — narrator-interest (POV impersonator, judge mode)
   LAYER R2.2 — memory (POV impersonator, judge mode)
   LAYER R2.3 — feeling (per-character impersonators × N, judge mode)
   LAYER R2.4 — metaphor (editor, judge mode)
        │
        ▼
   mutated facets + protolines + rebuilt _cite-index.md
```

**Round 2 is graph-aware by design.** Per the captured directive (and the Round-2 design in `design/shoot-v2/three-pass-alpha-design.md`), every midband author MUST receive the **full** Round-1 facet graph as input — all nine facet files plus the cite-index. Partial-graph dispatch is a build defect.

**Self-scoped deletion.** Each author can delete only entries from their own facet (memory can delete `mem:7` but cannot delete `feel:3`). Cross-facet deletion authority is reserved for the Step G final audit.

**Citation cascade on delete.** When an author deletes `<own>:<id>`, every protoline that has `[<own>:<id>]` in its citation list also has that citation stripped. The cite-index makes affected protolines cheap to identify.

**Per-facet per-round add-cap (R2 mitigation):** ≤5 new entries per facet per Round-2 run. Cap is enforced by the author at decision time.

## Args

- `$1` — optional. Episode slug (e.g. `s01e01`). If omitted, use `active.episode` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - The episode appears in the active season's episode list with `status: faceted-r1` (Round 1 must be complete).
   - `round_1_complete: true` flag present.
   - `facets_path` resolves.
3. Confirm all nine facet files exist under `active-project/theater/facets/`.
4. Confirm `active-project/theater/facets/_cite-index.md` exists. If missing, rebuild it first:
   ```bash
   python3 active-project/staff/cite-index/build_cite_index.py <slug>
   ```
5. Read the proto-lines file to confirm citation accrual is present.

Print:
```
Episode: <slug>
Status: faceted-r1 → entering Round 2 (hybrid judge)
Cite-index: active-project/theater/facets/_cite-index.md
Round-1 entries: <total> across 9 facets
Beginning Round 2 — 4 midband facets, judge mode, sequential.
```

---

## Round 2 — Hybrid judge

**Dispatch discipline (applies to every layer):**

- **Sequential within Round 2.** All authors mutate the shared protolines file (citation strip + add) and may strip co-located facets' anchors indirectly via cascade. Serialize.
- **Full nine-facet graph + cite-index in every dispatch payload.** Non-negotiable.
- **Self-scoped deletion only.** Author may delete only their own facet's entries.
- **Citation cascade on delete.** Author strips `[<own>:<deleted-id>]` from every protoline that referenced it (cite-index lists these).
- **Add-cap ≤5 per author per round.** Hard cap. Author refuses additional adds beyond cap; the lowest-priority candidate is logged for next-round consideration.
- **Per-entry decision logged.** Each existing entry gets one of: KEEP, DELETE-<reason>. Each new entry: ADD with rubric-cited justification.
- **No reordering of existing IDs.** Deleted IDs leave gaps. New entries take the next available ID per facet.
- **Each dispatch returns:** decision summary (keep/delete/add counts), citation-cascade strip count, refused additions (over-cap or rubric-fail), any flagged seams.

---

### Layer R2.1 — narrator-interest (POV impersonator, judge mode)

Dispatch **impersonator** loaded with the POV character (`narrator` slug from proto-lines header):

**Read:**
- Persona stack: `active-project/actors/<pov>/card.md`, `ltm.md`, `stm.md`, `state.md`, `vibes.md`.
- Behavior cards: `cards/dialects/INDEX.md` for the POV stack.
- Proto-lines file (Round-1 citation-accrued).
- All nine Round-1 facet files: `active-project/theater/facets/{tensometer,location-state,interest-narrator,sensory,state-updates,memory,feeling,metaphor,vibes}.md`.
- Cite-index: `active-project/theater/facets/_cite-index.md`.
- Rubric: `design/shoot-v2/rubric-narrator-interest.md`.

**Override default impersonator contract:** facet-judge mode. No show.md write. No action costs. No prose dialogue.

**Task — per existing NI entry, decide:**
- **KEEP** — entry is rubric-compliant, perceptual access holds, density-fit is honest.
- **DELETE** — entry duplicates the proto-line surface, fails perceptual access, reads as feeling/memory rather than register, or is rubric-non-compliant in light of the full graph (e.g., redundant with sensory:N at same protoline). Self-scoped — only NI entries.

**Task — for unfilled niches the graph reveals, decide:**
- Read the cite-index's "Bare protolines" and "Lonely entries" sections.
- For protolines where tens=2/3 + memory or feeling fired but NI did not, consider adding NI to spine-anchor.
- For lonely entries on adjacent protolines, consider whether NI presence would license cross-facet co-location.
- New entries follow the same rubric as Round 1: terse one-clause spotlight, perceptual-access gate, density expectation.

**Add-cap ≤5.**

**Citation cascade on delete:** for each deleted `narrator:<id>`, strip `[narrator:<id>]` from the protoline that referenced it (the cite-index says which one).

**Add-write:** for each new `narrator:<id>`, append `[narrator:<id>]` to the protoline.

**Output:** mutated `active-project/theater/facets/interest-narrator.md` (existing IDs preserved; deletions leave gaps; new entries appended with next-available IDs).

---

### Layer R2.2 — memory (POV impersonator, judge mode)

Dispatch **impersonator** loaded with the POV character (fresh fork; do not carry STM from R2.1):

**Read:** same stack as R2.1 plus all warehouse cond-* cards relevant to monuments (e.g., `cond-reincarnation-mechanics-84ac.card.md`, `cond-suppression-policy-progression.card.md`, `cond-shard-behavioral-weight.card.md`, `condition-swarm-in-foreign-ecology.card.md`).

**Override default impersonator contract:** facet-judge mode.

**Task — per existing memory entry, decide:**
- **KEEP** — monument-grade callback, NI-spine co-cited, target reference machine-resolvable or defensible gloss.
- **DELETE** — functional callback rather than monument, NI-spine missing without defense, target reference unresolvable and gloss too thin.

**Task — adds:**
- NI added in R2.1 may unlock new memory anchors. Re-read post-R2.1 cite-index (the orchestrator rebuilds it if needed; or read fresh from disk after R2.1 completes its protoline writes).
- For tens-transitions and tens=3 peaks without memory and with NI present, consider adding.
- Hard fences: no Earth-Bet proper nouns.

**Add-cap ≤5.**

**Citation cascade + add-write** as R2.1.

**Output:** mutated `active-project/theater/facets/memory.md`.

---

### Layer R2.3 — feeling (per-character impersonators, judge mode)

For each slug in `cast:` (POV and non-POV both eligible):

Dispatch **impersonator** loaded with that character (fresh fork) with:
- That character's persona stack + behavior cards.
- Proto-lines (post-R2.2 mutations).
- All nine Round-1 facets + cite-index.
- Rubric: `design/shoot-v2/rubric-feeling.md`.

**Override default impersonator contract:** facet-judge mode.

**Task — per existing feeling entry for this character, decide:**
- **KEEP** — somatic-tell card-matched, multi-justification ≥3 of 5, expressed-field correct, per-character per-scene cap ≤1 honored.
- **DELETE** — duplicates POV NI register (POV-only check), uses forbidden vocabulary, fails multi-justification on second look, exceeds scene cap.

**Task — adds:**
- For protolines where memory or NI fired (post-R2.2) and the somatic register would land but didn't, consider adding.
- Per-character per-scene cap remains ≤1 (HARD).

**Add-cap ≤5 per character.** (5 entries per character, not 5 total.)

**Citation cascade + add-write** as R2.1.

**Sequence cast in `cast:` order; one fork at a time** (shared file).

**Output:** mutated `active-project/theater/facets/feeling.md`.

---

### Layer R2.4 — metaphor (editor, judge mode)

Dispatch **editor** with:
- Proto-lines (post-R2.3 mutations).
- All nine Round-1 facets + cite-index (post-R2.3 rebuild if cascading deletes orphaned a metaphor anchor).
- Rubric: `design/shoot-v2/rubric-metaphor.md`.

**Task — per existing metaphor entry, decide:**
- **KEEP** — anchor still resolves (memory:<id> or feeling:<id> not deleted in R2.2/R2.3), tens-discipline holds, register is callback or dark-humor.
- **DELETE** — anchor deleted upstream (orphan; metaphor cannot stand without anchor), AP3 anti-duplication violation, AP7 default-refuse at tens ≠ 3 without dark-humor defense.

**Task — adds:**
- New memory or feeling entries from R2.2/R2.3 may license a new metaphor. Refuse-by-default; only add when ≥2 layers of multi-justification cleanly clear.
- Sparsity 0-3% (zero-fires acceptable).
- Per-scene cap ≤1 cross-character.

**Add-cap ≤3** (metaphor's per-rubric refuse-by-default discipline keeps cap tighter).

**Citation cascade + add-write** as R2.1.

**Output:** mutated `active-project/theater/facets/metaphor.md`.

---

## Phase 6 — Persist

1. Confirm all nine facet files still exist (R2 may have deleted entries but not files).
2. Confirm proto-lines body unchanged (line count + IDs); only `[...]` citation lists may have shrunk (cascades) or grown (adds).
3. Update `active-project/staff/showrunner/memory.md`:
   - Episode status: `faceted-r1` → `faceted-r2`.
   - Add `round_2_complete: true` flag under the episode entry.
4. Print summary (below).

## Phase 7 — Rebuild cite-index

```bash
python3 active-project/staff/cite-index/build_cite_index.py <slug>
```

The rebuilt cite-index reflects R2 mutations. Compare diff against R1 cite-index (kept under git history) for oscillation/drift signal — input for Step I (oscillation measurement).

### Print summary:

```
--- ROUND 2 FACETS COMPLETE: <episode-slug> ---

Per-facet R2 decisions (keep / delete / add):
  narrator-interest:    K=<n> D=<n> A=<n>  (cap-refusals: <n>)
  memory:               K=<n> D=<n> A=<n>  (cap-refusals: <n>)
  feeling:              K=<n> D=<n> A=<n>  (per-character: <slug>=K<n>/D<n>/A<n>, ...)
  metaphor:             K=<n> D=<n> A=<n>  (cap-refusals: <n>)

Citation-cascade strips: <total> across <count> protolines.
Citation accrual delta: R1 <count> → R2 <count> (delta <±n>)

Cite-index rebuilt: active-project/theater/facets/_cite-index.md
  Pile-ups (>4 facets/protoline): <count> (R1: <count>; delta <±n>)
  Lonely entries: <count> (R1: <count>; delta <±n>)
  Bare protolines: <count> (R1: <count>; delta <±n>)

Status: <slug> faceted-r2 (Round 2 complete; Round 3 + final audit deferred — Steps E-G)
```

---

## Convergence

Round 2 is single-pass. Each midband author runs once. There is no Round-2 retry loop; if an author returns issues that need re-decision, they're surfaced in the summary for human review and addressed in Round 3 (Step E) or final audit (Step G).

If an author refuses to judge (rubric gap, structural fault, blocking input missing), it logs the refusal under `active-project/staff/<author>/` and the orchestrator continues. The summary lists refusals; the episode is not blocked.

---

## Notes

- **Step D scope only.** Round 3 is Step E (mostly identical to Round 2 — relaxation pass against post-R2 state). Final audit is Step G. Both are deferred until R2 produces measurable output.
- **Self-scope is the structural safety.** Cross-facet deletion authority belongs to the final audit only. R2 authors who try to delete other facets' entries are committing a build defect.
- **Cite-index rebuild is mandatory at end of Round 2.** Without rebuild, Round 3 (when built) reads stale signal.
- **Mid-layer cite-index rebuild is optional.** R2.2 (memory) may benefit from a cite-index refresh after R2.1 (NI) completes its protoline writes — but this adds dispatch overhead. Default: don't rebuild between layers; the in-memory protoline state is read fresh by each next dispatch anyway.
- **Add-cap is per-facet per-round per-episode.** Tunable per-facet at Step I once oscillation data is in. Defaults: NI 5, memory 5, feeling 5/character, metaphor 3.
