---
description: Three-pass facet pipeline — Step A (Phase 0 + Round 1 only). Dispatches the nine tuned facet authors against one episode's proto-lines in DAG order. Output - active-project/theater/facets/. Usage - /and-facets [episode-slug]
---

Round-1 facet authoring against one episode's bones. Step A of the Beta three-round pipeline (`design/shoot-v2/three-pass-alpha-design.md`). Steps B–I (cite-index, gap-logs, Round 2/3, final audit, season rollout) are out of scope here.

You are the orchestrator. Each layer is one or more Agent dispatches. Showrunner is read-only memory; do not dispatch showrunner to drive the pipeline. The vibes-updates dispatch in Layer 6 is the **one exception** — vibes-updates is showrunner-authored per `schemas/facet.schema.md`.

**Pipeline shape:**

```
proto-lines/<slug>.md  (bones; citations accrue here as facets are authored)
        │
        ▼
   LAYER 1 — tens, loc-state          (dramatist, studio)
   LAYER 2 — narrator-interest, sensory   (POV impersonator, studio)
   LAYER 3 — state-updates, memory     (studio + per-actor impersonators, POV impersonator)
   LAYER 4 — feeling                   (per-character impersonators)
   LAYER 5 — metaphor                  (editor)
   LAYER 6 — vibes-updates             (showrunner)
        │
        ▼
   active-project/theater/facets/<facet-type>.md  (×9 files)
```

Round 1 is **blind**: no facet author reads other facets' files. Each author reads (a) the proto-lines file as it currently stands (with whatever citations have accrued from earlier layers in this run), (b) their own rubric, (c) per-rubric upstream cards/state/vibes. Cross-facet citation graph (`_cite-index.md`) is **not** built — that is Step B.

## Args

- `$1` — optional. Episode slug (e.g. `s01e01`). If omitted, use `active.episode` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - The episode appears in the active season's episode list with `status: protolined`.
   - Its `proto_lines_path` resolves (default `active-project/theater/proto-lines/<slug>.md`).
3. Read the proto-lines file. Lift the seven extended-header fields verbatim:
   - `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`.
4. Confirm `active-project/theater/facets/` is empty (or does not exist). If facet files already exist for this episode, abort with the path printed; archive first to re-run.
5. Confirm the active warehouse loc cards for every slug in `locations:` resolve under `active-project/warehouse/`.
6. Confirm every `cast:` slug resolves under `active-project/actors/<slug>/` (persona card + STM + LTM + state + vibes).
7. Read `schemas/facet.schema.md` and `schemas/proto-line.schema.md` once (orchestrator reference).

Print:
```
Episode: <slug>
Narrator: <slug>
Goal: <one sentence>
Cast: <slug>, <slug>, ...
Locations: <slug>, ...
Proto-lines: <path>  (<count> bones, <count> time-skips)
Beginning Round 1 — nine facet authors, layered dispatch.
```

Create `active-project/theater/facets/`.

---

## Round 1 — Blind authoring

**Dispatch discipline (applies to every layer):**

- **Sequential within a layer.** All Round-1 authors append citations to the shared proto-lines file. R7 (citation write-race) is mitigated by serializing within a layer; layers themselves run in DAG order.
- **Citation write-back is mandatory.** Each author appends `[<facet-prefix>:<id>]` to every proto-line they decorated, per `schemas/proto-line.schema.md` § "Citations". Prefixes: `tens`, `loc-state`, `narrator`, `sensory`, `state`, `mem`, `feel`, `meta`, `vibes`. Citation accrues; existing citations on the line are preserved.
- **Forbid loading other Round-1 facet files.** Each author reads only its rubric + the inputs the rubric names + the proto-lines file. No cross-facet peeking.
- **Per-file cull is the author's last act.** Per `schemas/facet.schema.md` § "Per-file cull" — delete-only, one pass. Author reports cull count.
- **Each dispatch returns:** path to written facet file, entry count, cull count, any flagged seams or rubric gaps.

---

### Layer 1 — tens, loc-state

#### 1a. tensometer (dramatist — read-only; orchestrator writes)

**Dramatist is Read-only** per agent definition. It cannot author files. The orchestrator dispatches dramatist for the *judgment* and writes the file from the returned payload. This is the only such inversion in the pipeline; every other author has Write/Edit.

Dispatch **dramatist** with:
- Proto-lines file (bones; no facet citations yet).
- Episode `narrator`, `goal`, chunk + theme from showrunner memory.
- Series + season escalation spines (from `series-plan.md` and `season-s01-plan.md`).
- Rubric: `design/shoot-v2/rubric-tensometer.md` (V2 locked).
- Schema: `schemas/facet.schema.md` § tensometer.

**Forbid loading:** other facet rubrics, behavior cards, vibes (tensometer is a single-rater scalar; vibes-as-bias enters in Round 2+ if/when retune-minor lands).

**Dramatist task (two-pass authoring; payload return only):**
1. Per-beat pass — assign 1/2/3 per content-bearing proto-line; cite axis per non-trivial entry.
2. Curve-shape pass — verify scene-level rise→peak→release and episode-level act-shape + frequency band 60-75/20-30/5-10. Do not inflate to manufacture shape; flag screen-writer kickback for structural gaps.

**Return payload** (text, in the body of the reply — do not attempt to Write):
- Ratings table: entry-id → proto-id → scalar [→ optional terse axis-citation].
- Distribution: 1s/2s/3s counts and percentages.
- Curve verdict: SHAPE-OK | SHAPE-FAIL with named failure modes.
- Frequency-band verdict: in-band | soft-fail (which rung; by how much).
- Cull deltas (per-beat-pass → curve-shape-pass changes).
- Flags: screen-writer kickback candidates, scene-boundary issues, rubric gaps.

**Orchestrator writes** `active-project/theater/facets/tensometer.md` from the dramatist's payload, in schema § tensometer form. Citation write-back: orchestrator appends `[tens:<entry-id>]` to every proto-line that received a 2 or 3 (1-rated lines do NOT need a back-citation; absence of `tens:` on a proto-line means rung 1 by convention).

#### 1b. location-state (studio)

Dispatch **studio** with:
- Proto-lines file.
- All loc cards named in `locations:`.
- `loc-state` field rules from `schemas/facet.schema.md` § location-state.
- Rubric: `design/shoot-v2/rubric-location-state.md` (locked).
- Movement-verb necessity gate.

**Forbid loading:** other facet rubrics, vibes (Round 1 is blind to bias-cite).

**Studio task:** author one entry per environmental anchor (location/time/weather/conditions/sensory note). Fire only where the environment is load-bearing for the action; bones-only proto-lines render in the most-recent cited environment.

Output: `active-project/theater/facets/location-state.md`. Citation write-back: append `[loc-state:<id>]` to each proto-line whose environment is load-bearing.

---

### Layer 2 — narrator-interest, sensory

#### 2a. narrator-interest (POV impersonator)

Dispatch **impersonator** loaded with the POV character (`<narrator>` slug):
- Persona card + behavior card stack (per `cards/dialects/INDEX.md`) + LTM + STM + state.
- Proto-lines file (now carries `[tens:*]`, `[loc-state:*]` accruals from Layer 1).
- Locked tensometer file (mandatory upstream per DAG).
- Locked location-state file (mandatory upstream).
- Rubric: `design/shoot-v2/rubric-narrator-interest.md`.
- Schema: § interest flags — narrator.

**Override the impersonator's default contract:** this is a facet-authoring run, not a line-generation run. The impersonator authors POV-spotlight one-clauses against proto-lines, not show-file lines. Do not append to `show.md`. Do not declare action costs.

**Forbid loading:** other characters' cards, audience personas, source prose.

Output: `active-project/theater/facets/interest-narrator.md`. Citation write-back: append `[narrator:<id>]` to each cited proto-line.

#### 2b. sensory (studio)

Dispatch **studio** (fresh fork) with:
- Proto-lines file.
- Locked location-state file (mandatory baseline; `<old-state>` for sensory deltas comes from here).
- Locked tensometer file (correlative-only — sensory deltas tend to cluster ≥2).
- Rubric: `design/shoot-v2/rubric-sensory.md`.
- Disambiguation gate: bare-word fires; charged-word refuses (see schema § sensory).
- Per-scene cap ≤3; sparsity 3-6%; modality-coverage ≥2 per episode.

**Forbid loading:** other facet rubrics beyond the two named upstreams.

Output: `active-project/theater/facets/sensory.md`. Citation write-back: append `[sensory:<id>]` to each cited proto-line.

---

### Layer 3 — state-updates, memory (sequential within layer)

#### 3a. state-updates — environment side (studio)

Dispatch **studio** (fresh fork) with:
- Proto-lines file.
- Locked tens (`@<id>` 3-beats expected to co-cite; 1-beat state-updates suspicious).
- Locked NI (POV-character co-citation context).
- Locked location-state (frame context).
- All loc cards + prop cards present in the warehouse.
- Rubric: `design/shoot-v2/rubric-state-updates.md`.
- Schema § state updates: `<target>.<field>: <old> -> <new>` form, `target` ∈ {`studio`, `prop:<slug>`}.

**Studio's scope here:** environmental + location + prop state changes only. Actor state is the per-character impersonator's job (3b).

Output: prepend entries to `active-project/theater/facets/state-updates.md`. Citation write-back: append `[state:<id>]` per cited proto-line.

#### 3b. state-updates — actor side (per-character impersonators)

For each slug in `cast:`:

Dispatch **impersonator** loaded with that character with:
- Persona card + LTM + STM + state + vibes for that character.
- Proto-lines file.
- Locked tens, NI, loc-state.
- Rubric: `design/shoot-v2/rubric-state-updates.md` § actor-state section.

**Override impersonator default:** facet-authoring mode (no show.md write).

Each impersonator appends to `active-project/theater/facets/state-updates.md` and writes back `[state:<id>]` citations.

**Sequence cast in the order they appear in `cast:`** (i.e., first-appearance ID). Wait for one to finish before dispatching the next — they share the state-updates file and the proto-lines file.

#### 3c. memory (POV impersonator)

Dispatch **impersonator** loaded with the POV character (fresh fork from 2a; do not re-use the NI fork's STM):
- Persona card + behavior card stack + LTM + STM + state.
- Proto-lines file (now carries Layer-1, Layer-2, and Layer-3 state-updates accruals).
- Locked tens (inverted-tens density gate — memory clusters at transitions and peaks).
- Locked NI (mandatory spine co-citation; memory entries that don't co-cite a narrator entry are flagged).
- Rubric: `design/shoot-v2/rubric-memory-flags.md`.
- Schema § memory flags.

**Override impersonator default:** facet-authoring mode.

Output: `active-project/theater/facets/memory.md`. Citation write-back: `[mem:<id>]`.

---

### Layer 4 — feeling (per-character impersonators)

For each slug in `cast:` (POV and non-POV both eligible):

Dispatch **impersonator** loaded with that character (fresh fork; do not re-use the state-updates 3b fork's STM) with:
- Persona card + behavior card stack + LTM + STM + state + vibes.
- Proto-lines file.
- Locked NI (mandatory POV non-redundancy check — POV-character feeling entries that duplicate a NI entry on the same proto-line are cut).
- Locked sensory (soft-supporting).
- Locked state-updates (soft-supporting).
- Rubric: `design/shoot-v2/rubric-feeling.md`.
- Schema § feeling flags — per-character per-scene cap ≤1 hard; sparsity 2-5%; multi-justification ≥3 of 5.

**Forbid loading:** named-feeling vocabulary, hedges, similes (see schema). Body register only.

**Override impersonator default:** facet-authoring mode.

Each impersonator appends to `active-project/theater/facets/feeling.md`. Citation write-back: `[feel:<id>]`.

**Sequence cast in `cast:` order; one fork at a time** (shared file).

---

### Layer 5 — metaphor (editor)

Dispatch **editor** with:
- Proto-lines file.
- Locked memory (one-of mandatory anchor).
- Locked feeling (one-of mandatory anchor).
- Locked tens (curve-discipline; AP7 default-refuse at tens ≠ 3 unless dark-humor register defends).
- Locked sensory (permitted co-cite).
- Locked NI (anti-duplication AP3).
- Rubric: `design/shoot-v2/rubric-metaphor.md`.
- Schema § metaphor flags. Sparsity 0-3% (zero-fires acceptable). Per-scene cap ≤1 cross-character.

**Editor task:** taste call; refuse-by-default. For each candidate, name the licensed-by anchor (memory:<id> or feeling:<id>) and ≥1 supporting layer. Per-file cull (delete-only) is the editor's last act.

**Forbid loading:** vibes (Round 1 blind), audience personas, behavior cards.

Output: `active-project/theater/facets/metaphor.md`. Citation write-back: `[meta:<id>]`.

---

### Layer 6 — vibes-updates (showrunner)

Dispatch **showrunner** with:
- Proto-lines file (full Round-1 citation accrual visible).
- Locked tens, locked state-updates, locked memory, locked feeling (the four primary licensing sources per schema § vibes-updates).
- All actor vibes files (`active-project/actors/<slug>/vibes.md`).
- All loc card VIBES sections (`active-project/warehouse/loc-*.card.md`).
- `active-project/staff/studio/vibes.md`.
- Rubric: `design/shoot-v2/rubric-vibes.md` + `rubric-vibes-v1.1-patch.md`.
- Schema § vibes-updates: entity-target-primary form; `licensed-by:` mandatory and machine-resolvable; `++`-or-skip default for pre-loaded keywords (RF-001 STRICT gate-2).

**Showrunner-as-author note:** showrunner has Read/Write/Edit and is the only agent with all-vibe-cloud visibility. This dispatch authors a **facet file**, not a memory write-back. Vibe-cloud propagation to actor/loc/studio files is a downstream task (caveat-004 from vibes Phase 5; deferred to and-wrap or to a follow-on showrunner dispatch).

Output: `active-project/theater/facets/vibes.md`. Citation write-back: `[vibes:<id>]` only on proto-lines where a vibe is on-screen-licensed (anchor optional per schema).

---

## Phase 6 — Persist

1. Confirm all nine facet files exist under `active-project/theater/facets/`:
   - `tensometer.md`, `location-state.md`, `interest-narrator.md`, `sensory.md`, `state-updates.md`, `memory.md`, `feeling.md`, `metaphor.md`, `vibes.md`.
2. Confirm the proto-lines file's body is unchanged in line count and ID assignment; only the trailing `[...]` citation lists may have grown.
3. Update `active-project/staff/showrunner/memory.md`:
   - Episode status: `protolined` → `faceted-r1`.
   - Add a `facets_path: active-project/theater/facets/` field under the episode entry.
   - Add a `round_1_complete: true` flag under the episode entry.

## Phase 7 — Cite-index (default)

Build `active-project/theater/facets/_cite-index.md` from the nine facet files + the proto-lines citation accrual. This is **deterministic transformation, not authoring** — no agent dispatch needed.

```bash
python3 active-project/staff/cite-index/build_cite_index.py <episode-slug>
```

The cite-index is a derivation of the current facet + proto-line state. It surfaces:

- **Density distribution** — protolines bucketed by citation count.
- **Per-facet entries** — each entry's anchor, back-citation status, co-located facet entries on the same protoline, outbound `licensed-by:` references, and inbound license references.
- **Pile-ups** — protolines with >4 co-located facets (over-decoration risk; or just the load-bearing peaks).
- **Lonely entries** — facet entries with no co-location and no inbound licensing link. Round-2 deletion candidates.
- **Bare protolines** — protolines with no citations accrued. Round-2 add candidates if the rubric licenses a fire.

Convention: tens entries with `rating=1` are NOT flagged as lonely (they don't accrue back-cites by convention; absence is expected). Off-anchor vibes entries are also excluded from the lonely classifier.

The cite-index is rebuilt at the end of every facet round (Round 2 and Round 3 dispatch overwrite the existing file). Round 2 dispatch payload to midband authors MUST include this file.

### Print summary:

```
--- ROUND 1 FACETS COMPLETE: <episode-slug> ---

Proto-lines decorated: <count> / <total>  (citation accrual)

Per-facet entry counts (post-cull):
  tensometer:            <count>  (1s/2s/3s = X/Y/Z; SHAPE-OK | SHAPE-FAIL)
  location-state:        <count>
  interest-narrator:     <count>
  sensory:               <count>  (modality coverage: <list>)
  state-updates:         <count>  (env <count> + actor <count>)
  memory:                <count>
  feeling:               <count>  (per-character: <slug>=<count>, ...)
  metaphor:              <count>  (zero-fires acceptable)
  vibes:                 <count>  (on-anchor <count> / off-anchor <count>)

Flags raised:
  - <flag-line>
  - <flag-line>

Cite-index: active-project/theater/facets/_cite-index.md
  Pile-ups (>4 facets/protoline): <count>
  Lonely entries (zero co-location, zero inbound license): <count>
  Bare protolines (no citations): <count>

Output: active-project/theater/facets/
Status: <slug> faceted-r1 (Round 1 only; Round 2/3 + final audit not run — Step A scope)
```

---

## Convergence

Step A is single-pass. Each facet author runs once, culls once. There is **no** Round-1 retry loop and no cross-facet consistency pass. Faults discovered post-hoc are out-of-scope here; they surface when Step D (Round 2 hybrid judge) lands and reads the full citation graph + gap-logs.

If a facet author refuses to author (rubric gap, structural fault, blocking input missing), it logs the refusal under `active-project/staff/<author>/` and the orchestrator continues with the remaining layers. The summary lists refusals; the episode is not blocked.

---

## Round 2 directive (carried forward to Step D build)

When Round 2 is implemented, every midband facet author (NI, memory, feeling, metaphor) MUST receive the **full** Round-1 facet graph as input — not just the DAG-upstream subset their rubric names. Round 1 is **blind by design** (each author sees only its rubric-named upstreams); Round 2 is **graph-aware by design** (each author judges keep / delete / add against the complete cross-facet graph).

Enforcement at build time: the Round-2 dispatch payload for any midband author must include all nine Round-1 facet files (`tensometer.md`, `location-state.md`, `interest-narrator.md`, `sensory.md`, `state-updates.md`, `memory.md`, `feeling.md`, `metaphor.md`, `vibes.md`) plus the cite-index. A Round-2 author dispatched without the full graph is a build defect, not an authoring defect.

Same rule for the final audit (Step G): the auditor reads the full graph; partial-graph audit is structurally wrong.

**Gap-logs are NOT part of the default Round 2 payload.** Per user direction (2026-05-10b), gap-logs are reclassified from "Round-2 enrichment input" to "optional debug instrumentation, off by default." The Round-2 author gates additions through the per-facet rubric; the rubric is sufficient. Gap-log emission (Step C in the original Beta build order) is deferred indefinitely and only enabled when a debug session needs to surface what Round-1 authors wanted to fire on but couldn't.

User direction (2026-05-10): "ensure the facets are actually using all previous facets" in second pass. Directive captured here so the Step D build honors it.

---

## Notes

- **Step A scope only.** Round 2/3, final audit, cite-index, gap-logs are deferred to Steps B–G per `design/shoot-v2/three-pass-alpha-design.md` § "Build order".
- **Single-episode only.** Season-wide rollout is Step H. To run on a different episode, archive `active-project/theater/facets/` first.
- **Audience interest-flags are skipped.** Per `cards/dialects/INDEX.md` and the dependency audit, audience-interest is unbuilt at the rubric level. When tuned, it becomes Layer 2b' (read tens + loc-state + NI; one file per persona).
- **Dialogue / stitch render is not a Round-1 facet.** It is the Layer-7 terminal consumer. Stitching to a written chapter is a separate command, downstream of Round 3 + final audit.
- **Vibe-cloud write-back is deferred.** Caveat-004 from vibes Phase 5: post-author propagation of vibe deltas to actor/loc/studio files happens in and-wrap (or in a follow-on showrunner dispatch). This command produces only the facet file.
