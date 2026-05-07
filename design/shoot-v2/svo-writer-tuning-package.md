# SVO-Writer Pipeline Tuning — Package

Forward-looking tuning brief for the svo-writer pipeline. Drafted 2026-05-07. Adapts the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md` to a multi-pass writer pipeline (vs. a single-author facet).

**Scope:** the writer chain that takes an episode chunk (post-shoot-prep) and produces `active-project/theater/proto-lines.md` per `schemas/proto-line.schema.md`. Replaces `/and-protolines` Phase 1 + Phase 2 with a tuned five-pass pipeline.

**Status:** plan only. No phases run yet. Plan parent: `~/.claude/plans/we-start-at-input-agile-clarke.md`.

---

## What's new vs. facet tuning

The five facets tuned to date (loc-state, dialogue, tensometer, narrator-interest, state-updates, memory-flags, sensory) all generated *one artifact under one rubric*. The svo-writer is structurally different:

- The output is the **upstream artifact** every facet cites. Quality regressions here cascade into every facet.
- The "rubric" is **five sequenced rubrics**, one per pipeline pass, not one. A line surviving pass 2 (constraint legality) still has to survive pass 3 (shape), pass 4 (trim), and pass 5 (continuity).
- The writer is **chunk-only** at authoring time (no source prose, no reference proto-lines). The s01e01–e06 extracted corpus is for facet tuning, not for benchmarking the writer.
- **Convergence, not accept-rate, is the success metric.** The pipeline succeeds when all five passes produce clean verdicts in sequence. There is no "% accepted" axis; there is only "did the file ship."

---

## Pipeline

```
            ┌──────────────────────────────────────────────────────────┐
            │  episode-shoot-prep complete                             │
            │  (chunk, change, theme, cast, constraints, narrator,     │
            │   goal, location cards, condition cards, behavior cards) │
            └────────────────────────┬─────────────────────────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │  Pass 1 — Inventory             │
                    │  screen-writer                  │
                    │  produces raw proto-line file   │
                    │  (over-generates by design)     │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │  Pass 2 — Constraint audit      │
                    │  auditor (fork) → fixer         │
                    │  every line legal under         │
                    │  SVO mechanics + cond-* cards   │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │  Pass 3 — Shape                 │
                    │  dramatist                      │
                    │  re-order for escalation        │
                    │  flag missing transitions       │
                    │  (additions → screen-writer)    │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │  Pass 4 — Trim                  │
                    │  audience (3 personas)          │
                    │  drop what doesn't serve goal   │
                    │  ≥2-persona threshold           │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │  Pass 5 — Continuity audit      │
                    │  auditor (fork) → fixer         │
                    │  chunk-end reachable;           │
                    │  state consistent;              │
                    │  POV intact                     │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                       ┌─────────────────────────┐
                       │  locked proto-lines.md  │
                       └─────────────────────────┘
```

Convergence: each pass is "clean" when it produces no faults / no re-orderings / no deletions. Pipeline ships when all five report clean **in a single end-to-end run**. A change at any pass invalidates downstream passes for that run; downstream re-runs from the changed point.

---

## SVO Discipline (the spine all five passes enforce)

A proto-line is **a subject doing something, optionally to object(s)**. Nothing else.

**Subject action, never subject non-action.** Every banned form below is a non-action masquerading as one.

- **Subject** — exactly one named entity (actor slug, prop slug, `the <noun>`).
- **Verb** — exactly one concrete physical action.
- **Object(s)** — zero or more named/quantified things acted upon.
- **Object-as-subject form permitted** when the actor is unknown/ambient/unspecified (`the page tears`, `the door swings open`); optional `by <slug>` tail when the actor matters.
- **No modifiers** — no adjectives, adverbs, prepositional padding.
- **No copulas** — `is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being` are banned. State assertions belong in facets, not the SVO spine.
- **No negations** — never `<subject> didn't <verb>`. Collapse to positive holds (`Plumm holds the page on the desk`, not `Plumm doesn't pick up the page`).
- **No interiority** — thought, intent, feeling are facets.
- **No perception verbs** — `read`, `took`, `tracked`, `noted`, `counted`, `measured` are POV-leaks. Recast as the physical event happening to the perceived entity.
- **No conjunctions** — no `and`, `but`, `while`, `as`. Two beats = two proto-lines. (Comma-list-of-objects under one verb is the open exception.)

---

## File shape (output spec)

```
narrator: <slug>
goal: <one-sentence statement of what the chapter shows the audience>

1 SUBJECT VERB [OBJECT]
2 SUBJECT VERB
3
4 SUBJECT VERB OBJECT
...
```

- Header: `narrator:` + `goal:` mandatory.
- Body: numbered monotonically from 1, IDs stable from assignment.
- **Time-skip = a blank numbered line.** A line with just an ID and no SVO content marks elapsed time.
- Citations (`[<artifact>:<id>, ...]`) accrue at facet-authoring time, not here.

---

## Per-pass rubrics

### Pass 1 — Inventory rubric (screen-writer)

**Fires:** authors a raw proto-line file for the episode chunk.

**Inputs loaded:** chunk, change, narrator, goal, cast roster (slugs), constraint slugs, location cards, schema, calls list (`svo-split-notes.md`).

**Inputs forbidden:** behavior cards, vibes, audience personas, source prose, reference proto-lines, deprecated v1 script bullets.

**Coverage criteria:**
- Every entity transition implied by `change` is reachable through the listed beats.
- Every active actor in the cast roster has at least one fire (or is justified absent in a margin comment).
- Every constraint referenced in the chunk has a beat that demonstrates its operation (the constraint is "shown," not asserted).

**Discipline criteria:** every line meets the SVO spine above.

**Bias:** over-generate. Coverage > economy. Pass 4 will trim.

### Pass 2 — Constraint audit rubric (auditor #1)

**Fires:** classified faults on the inventory output. Routes to fixer.

**Per-line checks:**
- SVO form compliant (subject, verb, optional object(s), nothing else).
- No banned forms (copula, negation, perception verb, modifier, interiority, conjunction).
- Verb is concrete and physical.
- Subject and object(s) are named entities or `the <noun>`.

**Per-card checks:**
- No line violates any active cond-* card. Specifically: fauna mechanic costs honored, customary-authority forms respected, no-parahuman-infrastructure not implicitly assumed, lore/laws not contradicted.
- No prop named that isn't on the active set (per location cards) and not in any actor's inventory at episode-open.

**Verdicts:** per-line CORRECT / FAULT-{class}. Fixer applies minimum-change repair (delete or split is the typical move).

### Pass 3 — Shape rubric (dramatist)

**Fires:** ID-order list + flagged missing-transition list.

**Curve criteria:**
- Sequence supports the chunk's escalation arc (compression early, expansion at peak, release after).
- No flatlined stretches (long runs of low-tension beats with no inflection).
- Episode-position-in-season honored (per season escalation spine).
- Climax beat unique within the file (one peak, not three).

**Transition criteria:**
- No causal jumps without setup beats (a beat that depends on a state not established earlier is flagged).
- Scene-boundary beats present where location/time changes (or a blank-line time-skip is appropriate).

**Discipline:** dramatist may not author new lines. Missing transitions route back to screen-writer with a one-line brief; screen-writer authors the addition; pass 2 re-runs on additions only.

### Pass 4 — Trim rubric (audience, 3 personas)

**Fires:** per-persona deletion proposals + per-persona accept/revise verdict at file level.

**Per-line trim test:** does this line serve the chapter `goal`?
- YES → keep.
- NO but voice-load-bearing per the actor's behavior signature → keep.
- NO and not voice-load-bearing → propose deletion.

**Threshold:**
- ≥2 personas propose deletion → auto-accept.
- 1 persona → advisory, orchestrator decides.

**File-level verdict per persona:**
- ACCEPT → no further deletions, sequence reads as the chapter.
- REVISE → name the unsolved entertainment problem in one clause.

**Pass 4 terminates** when all three personas ACCEPT in one round. Max 2 revise rounds; a third forces a flag and orchestrator review.

### Pass 5 — Continuity audit rubric (auditor #2)

**Fires:** classified faults on the post-trim file. Routes to fixer; fixer-output re-runs pass 5 only.

**Reachability checks:**
- Chunk-end reachable from chunk-start through the surviving beats.
- Every actor named in the file has a coherent presence-arc (enters, acts, exits or remains).
- Goal-as-stated is delivered by the surviving beats.

**State checks:**
- No prop referenced after a deletion that removed its placement / handover.
- No actor in two locations at once.
- No location/time inconsistency around blank-line time-skips.

**Reference checks:**
- No proto-line ID referenced internally (no inline refs; citations are downstream-only).
- Every cast slug used resolves to an active actor card.
- Every prop/location named is on-set per its card.

**POV checks:**
- The narrator slug is consistent with what the file shows. POV-leak verbs (perception verbs applied to the POV character) are caught even if pass 2 missed them post-shape.

---

## Test episode

**s01e01** ("default to the smallest known target"). Rationale:
- 77 proto-lines extracted (smallest of the six). Bounded scope for a first run.
- Chunk + change + theme + constraints + cast all present in active-project (currently archived under `theater/s01e01-archive/`).
- The s01e01 extracted reference is *ignored at authoring* but exists as a downstream sanity check if needed (the writer authors blind; an end-of-run shape comparison can be informative without being scoring).
- Narrator is Taylor (POV pattern is well-established).

Open: re-run on s01e04 as second test (Plumm POV — different narrator validates the header field). Defer until s01e01 converges.

---

## Build-then-tune sequencing

The pipeline is implemented **before** tuning begins. Order:

1. **Pipeline implementation.** Author the five-pass orchestration as a slash command at `.claude/commands/and-protolines-v2.md`. Non-destructive to the v1 command; v1 stays live until v2 is tuned and promoted. Each pass is a real Agent dispatch with a real brief. The command is runnable end-to-end before any reviewer is tuned — it just won't produce shippable output yet.
2. **Phase 0 — Prep.** Lock per-pass rubrics (this document). Resolve open contract questions. Author per-pass briefs.
3. **Phase 1 — Reviewer tuning.** Tune each reviewer pass against a synthetic naive baseline.
4. **Phase 2 — Writer fork.** Run the tuned reviewers against a fresh screen-writer dispatch.
5. **Phase 3 — Adversarial seams.** Hostile-mode review.
6. **Phase 4 — Defense or revision.** Writer revises against seams.
7. **Phase 5 — Final adjudication.** End-to-end clean run.
8. **Promotion.** Swap `/and-protolines-v2` into `/and-protolines`; archive v1 under `archive/commands/and-protolines-v1.md`.

The pipeline-as-skill exists from step 1; the pipeline-as-trustworthy-skill exists from step 8.

## Phases (the meta-process — how we tune)

This pipeline-tuning effort itself follows the established five-phase pattern, adapted:

### Phase 0 — Prep
- Lock per-pass rubrics (this document is the v1 draft).
- Decide test episode (s01e01).
- Resolve open contract questions (narrator/goal source, plural-object handling, time-skip semantics, plan-prose breadth at pass 4, behavior card depth at pass 4).
- Author writer briefs and reviewer briefs per pass.

### Phase 1 — Reviewer tuning
Tune each reviewer pass independently before any writer dispatch:
- **Pass 2 auditor brief** — what constraint cards to load, what fault classes to recognize, fault-class → fixer-action mapping.
- **Pass 3 dramatist brief** — what shape criteria, how to write the order list, how to brief the screen-writer for transitions.
- **Pass 4 audience brief** — how to score against `goal`, when voice-load-bearing overrides, what counts as "interesting."
- **Pass 5 auditor brief** — distinct from pass 2; reachability/state/reference/POV focus.

Each reviewer pass gets a **lenient → strict** baseline against a synthetic naive-author output before the writer fork is engaged.

### Phase 2 — Writer fork
Screen-writer authors s01e01 inventory blind to: source prose, reference proto-lines, deprecated script bullets. Output runs through pass 2; first lift number recorded.

### Phase 3 — Adversarial seam-finding
Each reviewer pass hits the writer's output in hostile mode. Surfaces what the per-pass rubrics missed.

### Phase 4 — Defense or revision
Screen-writer revises against seams. Re-runs the affected passes.

### Phase 5 — Final adjudication
End-to-end clean run. Locked file ships to `active-project/theater/proto-lines.md`. Headline number: did the pipeline converge in ≤2 revise rounds at any single pass?

---

## Resolved contract decisions

The six open questions are resolved per the user constraint: **use active-project planning material; ignore past shoot artifacts.**

1. **Plan-prose breadth.** Series-plan.md and season-plan.md are *planning material*, not shoot artifacts — fair game. But the contamination risk is at *authoring*. Decision: pass 1 (screen-writer) gets memory one-liners only; passes 3 (dramatist) and 4 (audience) may load full series-plan + season-plan prose since they re-arrange and prune, not author.
2. **Old script bullets at pass 1.** STRICT BLIND. The script section in `episode-plan.md` is a v1 shoot artifact (it was written by the screen-writer during shoot-prep under the old chain). Pass 1 reads `chunk`, `change`, `theme`, `actors`, `constraints` from episode-plan.md but **not** the script section. The bullets are noise for an SVO author.
3. **Behavior card depth.** Full inheritance stack at passes 3 and 4 (per dialogue/facet-tuning precedent). Per-character leaf + parent + all referenced shared cards. Behavior cards are forbidden at pass 1 (mechanical) and pass 2 (legal-only) and pass 5 (state/reference).
4. **Plural-object handling.** Comma-list of objects under one verb permitted *only* when the verb acts on the set as one physical event (`Plumm gathers the page, the stylus, the seal`). Otherwise split. Pass 2 auditor adjudicates with a single-event test: would an observer see one motion or three?
5. **Narrator + goal source.** For this tuning run: orchestrator distills both from chunk + theme + change at Phase 0 of the pipeline. Downstream follow-up: add `narrator` and `goal` as required fields to `schemas/episode-plan.schema.md` after pipeline convergence; backfill for s01e01–s01e06 episode-plans once.
6. **Time-skip semantics.** Silent blank numbered line. Elapsed-time annotation lives in downstream state-update / location-state facets that cite the flanking proto-line IDs. Keeping the spine annotation-free preserves the bone-only contract.

**Hard rule across the pipeline (carried from this session):** the writer at every pass is **blind to past shoot artifacts** — `active-project/theater/show.md`, `active-project/theater/s01e01-archive/show.md`, `active-project/theater/proto-lines/s01e0{1..6}.md` (the rough-pass extractions), and the deprecated script bullets inside `episode-plan.md`. The writer is not blind to: chunk, change, theme, actors, constraints, cast cards, behavior cards, vibes, condition cards, location cards, audience persona cards, series-plan prose, season-plan prose, showrunner memory.

---

## Artifact map (planned)

### Phase 0 (this phase)
- This package: `design/shoot-v2/svo-writer-tuning-package.md`
- Per-pass rubrics: above (lift to standalone rubric files if they grow).
- Open-question resolutions: appended to this file or split per question.

### Phase 1
- Reviewer briefs: `design/shoot-v2/svo-writer-pass{2,3,4,5}-brief.md` (one per pass).
- Naive baseline outputs: `design/shoot-v2/phase1-svo-writer-baseline-naive.md`.
- Per-pass baseline reviews: `active-project/staff/auditor/phase1-svo-writer-pass{2,5}-baseline.md` (auditor passes); dramatist + audience baselines as separate files.

### Phase 2
- Screen-writer fork output: `active-project/theater/proto-lines.md` (s01e01, fresh).
- Per-pass audit: `active-project/staff/auditor/phase2-svo-writer-pipeline.md`.

### Phase 3
- Per-pass adversarial seams: `active-project/staff/auditor/phase3-svo-writer-seams.md`.

### Phase 4
- Defense/revision: `design/shoot-v2/phase4-svo-writer-defense.md`.

### Phase 5
- Final adjudication: `active-project/staff/auditor/phase5-svo-writer-final.md`.
- Locked output: `active-project/theater/proto-lines.md`.

### Downstream (post-tuning)
- Update `schemas/proto-line.schema.md` with header fields, blank-as-timeskip, harsh-SVO clauses (no copulas, no negations explicit).
- Update `.claude/commands/and-protolines.md` to reflect five-pass pipeline.
- Possible: `schemas/episode-plan.schema.md` extension for `narrator` + `goal` fields.

---

## Co-deployment note

The five passes are not separable. Pass 1's over-generation only works because pass 4 trims aggressively. Pass 4's aggression is only safe because pass 5 catches what trimming broke. Pass 3's re-ordering only serves the curve because pass 2 already culled illegal lines that would otherwise corrupt shape decisions. Ship the pipeline as a unit; tune the rubrics together; version them together.

The screen-writer + auditor + dramatist + audience are all existing roles in the and-shoot taxonomy. No new agent type is introduced. The svo-writer "agent" is the *pipeline*, not a single dispatch. This is the architectural shift from `/and-protolines` v1.
