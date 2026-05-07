---
description: Five-pass SVO-writer pipeline. Inventory → Constraint audit → Shape → Trim → Continuity audit. Produces active-project/theater/proto-lines.md. Usage - /and-protolines-v2 [episode-slug]. v2 is under tuning; v1 remains the live shoot-v2 chain entry.
---

Five-pass SVO-writer pipeline. Replaces the two-phase `/and-protolines` v1 once tuned and promoted (see `design/shoot-v2/svo-writer-tuning-package.md` for the build-then-tune sequencing).

You are the orchestrator. Each pass is an Agent dispatch. Showrunner is read-only memory; do not dispatch showrunner to drive the pipeline.

**SVO Discipline (the spine all five passes enforce):**

A proto-line is **a subject doing something, optionally to object(s)**. Subject action, never subject non-action.

- Subject = one named entity (actor slug, prop slug, or `the <noun>`).
- Verb = one concrete physical action.
- Object(s) = zero or more named/quantified things acted upon.
- Object-as-subject form permitted when the actor is unknown/ambient (`the page tears`); optional `by <slug>` tail when the actor matters.
- **No modifiers** (no adjectives, adverbs, prepositional padding).
- **No copulas** (`is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being`).
- **No negations** (collapse to positive holds: `Plumm holds the page on the desk`, not `Plumm doesn't pick up the page`).
- **No interiority, no perception verbs** (`read`, `took`, `tracked`, `noted`, `counted`, `measured` recast as the physical event on the perceived entity).
- **No conjunctions** (no `and`, `but`, `while`, `as`).

**Output file shape:**

```
narrator: <slug>
goal: <one-sentence statement of what the chapter shows>

1 SUBJECT VERB [OBJECT]
2 SUBJECT VERB
3
4 SUBJECT VERB OBJECT
...
```

Numbered lines monotonic from 1, IDs stable. **Blank numbered line = time-skip.** Citations accrue at facet-authoring time; bone-only here.

## Args

- `$1` — optional. Episode slug (e.g. `s01e07`). If omitted, use `active.episode` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - The episode appears in the active season's episode list.
   - Its chunk statement is present.
   - Its status is `planned` (not `shot`, not `wrapped`).
3. Read `active-project/theater/episode-plan.md`. Confirm chunk, change, theme, actors, constraints fields are present.
4. Resolve `narrator` and `goal`:
   - If episode-plan has explicit fields, use them.
   - Else: `narrator` is inferred from POV pattern (orchestrator picks; defaults to the most-named POV character in the chunk). `goal` is distilled from chunk + theme into one sentence.
5. Confirm `active-project/theater/proto-lines.md` does not exist for this episode. If it does, abort with the path printed; archive first to re-run.
6. Confirm `cards/dialects/INDEX.md` exists.

Print:
```
Episode: <slug>
Narrator: <slug>
Goal: <one sentence>
Chunk: <chunk statement>
Beginning five-pass SVO pipeline.
```

---

## Pass 1 — Inventory (screen-writer)

Dispatch **screen-writer** with:
- `narrator` slug + `goal` statement.
- Episode chunk + `change` field (verbatim).
- Active cast roster (slugs only; no voice cards).
- Active constraint card slugs.
- Location card paths (full content available for set authority).
- Schema reference: `schemas/proto-line.schema.md`.
- The harsh-SVO rules from this command.
- Calls list: `design/shoot-v2/svo-split-notes.md`.

**Forbid loading:** behavior cards, vibes, audience personas, source prose, reference proto-lines (`active-project/theater/proto-lines/s01e0*.md`), deprecated v1 script bullets in `episode-plan.md`.

**Screen-writer task:**
- Write the header (`narrator:`, `goal:`).
- Author proto-lines for maximal coverage of beats required to traverse chunk-start → chunk-end.
- Over-generate: coverage > economy.
- Every line meets SVO discipline.
- Blank-numbered-line for time-skips between scenes.

Output: `active-project/theater/proto-lines.md`.

---

## Pass 2 — Constraint audit (auditor)

Dispatch **auditor** (fork) with:
- The Pass 1 output.
- Schema + harsh-SVO rules.
- Full content of every active cond-* card (under `active-project/warehouse/`).
- Series laws + lore from showrunner memory.
- Active location cards (physical-possibility checks).
- Calls list (15 calls promoted to mechanic checks).

**Auditor brief:** classify each line as CORRECT or FAULT-{class}. Fault classes:
- FAULT-FORM (SVO shape violation, copula, negation, conjunction, modifier, perception verb, interiority).
- FAULT-CONSTRAINT (violates a cond-* card, series law, or lore fact).
- FAULT-PHYSICAL (prop not on set, actor not present, exit doesn't exist).

Auditor returns a classified report at `active-project/staff/auditor/protolines-<slug>-pass2.md` per `schemas/audit-report.schema.md`.

**Fault routing:** Faults route to **fixer** with minimum-change directive (delete or split is the typical move; rewrite only if the underlying beat is salvageable). Fixer logs to `active-project/staff/fixer/fixer-log.md`.

**Pass 2 terminates** when the auditor's report is empty (no faults). Otherwise: fix, re-run pass 2 only.

---

## Pass 3 — Shape (dramatist)

Dispatch **dramatist** with:
- The constraint-clean file from Pass 2.
- Episode chunk + change + theme.
- Series escalation spine (from `series-plan.md`).
- Season escalation spine (from `season-s01-plan.md` or current season).
- Behavior cards for the active cast (composition stack per `cards/dialects/INDEX.md`).

**Forbid loading:** vibes, audience personas, raw constraint cards (already enforced).

**Dramatist task:**
- Output an ID order list reflecting the desired sequence.
- Output a flagged-missing-transition list: each entry names where a beat is missing and what state-change it should bridge.

**Dramatist may not author lines.** Missing transitions return to screen-writer with a one-line brief; screen-writer authors only the additions; pass 2 re-runs on additions only.

Apply the order list by re-arranging lines in `proto-lines.md`. **IDs do not change** — only line order.

**Pass 3 terminates** when dramatist returns an unchanged order list and an empty missing-transition list.

---

## Pass 4 — Trim (audience, 3 personas)

Dispatch the three audience personas in parallel, each loaded with:
- The re-shaped file from Pass 3.
- The episode `goal` (the north star).
- Series.theme + series.behaviors + episode theme.
- Per-actor vibes (`active-project/actors/<slug>/vibes.md`).
- Studio vibes (`active-project/staff/studio/vibes.md`).
- The persona's own card.

**Forbid loading:** raw constraints, calls list, behavior cards (dramatist already weighed voice).

**Per-persona output:**
- Per-line deletion proposals (a line that does not serve `goal` and is not voice-load-bearing).
- File-level verdict: ACCEPT or REVISE-{one-clause-reason}.

**Threshold for deletion:** ≥2 personas propose → auto-accept. 1 persona → advisory; orchestrator decides.

Apply deletions by removing entire lines. **Do not renumber.** Gaps in IDs are intentional.

**Pass 4 terminates** when all three personas ACCEPT in one round. Max 2 revise rounds; on the third, ship with audience flags annotated as comments at end of file and flag for human review.

---

## Pass 5 — Continuity audit (auditor)

Dispatch **auditor** (fork, second invocation, fresh context) with:
- The post-trim file.
- Episode chunk + change.
- `narrator` slug + `goal`.
- Active location cards.
- Active cast roster.
- Series laws.

**Forbid loading:** vibes, audience personas, behavior cards, calls list.

**Auditor brief:** classify the file as CONTINUITY-OK or report classified faults. Fault classes:
- FAULT-REACHABILITY (chunk-end not reachable from chunk-start through surviving beats; goal not delivered).
- FAULT-STATE (prop referenced after deletion of placement; actor in two locations; time/location inconsistency around blank-line skips).
- FAULT-REFERENCE (cast slug doesn't resolve; prop/location not on-set).
- FAULT-POV (perception-verb leak on POV character; narrator not consistent with what the file shows).

Auditor returns report at `active-project/staff/auditor/protolines-<slug>-pass5.md`.

**Fault routing:** route to fixer for targeted repair. After repair, re-run pass 5 only (do not re-trim or re-shape).

**Pass 5 terminates** when the auditor returns CONTINUITY-OK with empty faults.

---

## Phase 6 — Persist

1. Confirm `active-project/theater/proto-lines.md` is final.
2. Update `active-project/staff/showrunner/memory.md`:
   - Episode status: `planned` → `protolined`.
   - Add a `protolines` field under the episode entry pointing at the file.
3. Print summary:

```
--- PROTO-LINES COMPLETE: <episode-slug> ---

Total proto-lines: <count> (excluding time-skip blanks: <count>)
Time-skips: <count>
Pass 1 inventory size: <count>
Pass 2 constraint cuts: <count>
Pass 3 re-arrangements: <count>
Pass 3 transitions added: <count>
Pass 4 trim cuts: <count>
Pass 5 continuity repairs: <count>

Convergence: clean run on iteration <n>

File: active-project/theater/proto-lines.md
Logs: active-project/staff/auditor/protolines-<slug>-pass{2,5}.md
```

---

## Convergence

The pipeline converges when **all five passes produce clean verdicts in a single end-to-end run**. A change at any pass invalidates downstream passes for that run; downstream re-runs from the changed point.

If end-to-end convergence is not reached after **3 full pipeline iterations**, ship with a header comment noting non-convergence and flag for human review.

---

## Notes

- Citations in proto-lines stay empty here. They accrue at facet-authoring time per `schemas/proto-line.schema.md`.
- Proto-line IDs are stable from the moment they are first assigned. Re-running this command for the same episode is not supported — archive the existing file first if you need to re-author.
- Audience and dramatist are stateful between passes within a run. Their STM should be loaded at each dispatch and updated after each verdict.
- v2 is under tuning (`design/shoot-v2/svo-writer-tuning-package.md`). v1 (`/and-protolines`) remains the live entry until v2 promotes.
