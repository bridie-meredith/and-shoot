---
description: Season-scope orchestrator. Takes a season chunk (from season-plan.md), decomposes into episode chunks, authors episode-plans, runs /and-protolines-v2 chained across all episodes, then runs a comprehensive cross-episode auditor for constraint and state coherence. Usage - /and-season [season-slug]
---

The season is the natural authoring unit. Episodes are decompositions of the season's escalation arc, not independently-planned chunks chained after the fact. This command builds the season top-down and produces a coherent, non-jarring proto-line set for every episode in one shot.

You are the orchestrator. All work routes through subagent dispatches.

## Args

- `$1` — optional. Season slug (e.g. `s01`). If omitted, use `active.season` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve season slug.
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - Season exists in `seasons[]` with status `active`.
   - `season-<slug>-plan.md` exists with season chunk, escalation spine, and per-episode chunk paragraphs.
3. Build the work list — every episode under the season. Capture each episode's existing status:
   - `planned` (chunk authored but no episode-plan.md yet) — needs full decomposition.
   - `protolined` (episode-plan.md exists, proto-lines file exists, status set) — skip; do not re-run.
   - `shot` / `wrapped` — abort with the slug; the season is already past the protolines phase for this episode and re-running would conflict.
4. Print the work list and proceed.

```
Season: <slug>
Episodes to draft: <list with current status per episode>
```

---

## Phase 1 — Episode decomposition

For episodes that lack `episode-plan.md` (status `planned`), dispatch **screen-writer** in **season-decomposition mode**.

Inputs:
- Full prose of `series-plan.md` and `season-<slug>-plan.md`.
- Series.theme + laws + lore + behaviors from showrunner memory.
- Active cast roster (series.cast_roster).
- Active stage_elements (locations, props, conditions registered at series scope).
- Per-episode chunk paragraphs (from season-plan.md).

Forbidden:
- Past shoot artifacts (show files, prior proto-lines, deprecated v1 script bullets in any existing episode-plan.md — read top frontmatter only on existing episode-plans).

Task:
- For each episode in scope, author `active-project/theater/<slug>/episode-plan.md` with required fields: `episode`, `chunk`, `change`, `theme`, `actors`, `constraints`, `narrator`, `goal`. The `narrator` and `goal` fields are mandatory under shoot-v2.
- The chunk text comes verbatim from the season-plan.md per-episode paragraph; screen-writer's authoring work is the *other* fields — `change`, `theme`, `actors`, `constraints`, `narrator`, `goal` — derived from the chunk + season escalation spine.
- Cast (`actors`) is per-episode (not the full series roster) — drawn from who the chunk implies is on-stage.
- Constraints reference active condition cards by slug.
- Narrator is a single slug (POV character for the episode); orchestrator may override if a specific decomposition is preferred.
- Goal is one sentence — what the episode shows the audience.

Output: `active-project/theater/<slug>/episode-plan.md` for each episode in scope.

Dispatch all in-scope episodes **in parallel** (each is independent given the season chunk). Audience review is not invoked here — the decomposition is structural, and any taste calls happen at proto-lines authoring.

---

## Phase 2 — Per-episode proto-lines (chained)

For each episode in scope, in **canonical season order** (s01e01, s01e02, ...):

1. Set `active.episode = <slug>` in showrunner memory.
2. Invoke `/and-protolines-v2 <slug>` and wait for completion. The five-pass pipeline runs internally; this command does not re-implement the passes.
3. On convergence: confirm output exists at `active-project/theater/proto-lines/<slug>.md` (per-episode subdir convention). Confirm episode status is `protolined`.
4. If the pipeline fails to converge (3 internal iterations exhausted), halt the season chain and surface for human review. Do NOT continue — cross-episode drift is harder to repair than partial progress.

Sequential is the default. Parallel mode is not offered at season scope: the audience persona STM threads across episodes (a key part of taste calibration), and parallel breaks the thread.

---

## Phase 3 — Comprehensive season-scope review

After all episodes have individually converged, run the **same four-pass structure** that vetted each episode at episode scope, now scaled up to the entire season's chunks and proto-line files together. Same reviewer roles, same dispatch shape, same convergence definition (all four passes clean in one end-to-end run) — what changes is the scope of "the file under review" (now: all chunks + all proto-lines together) and the criteria each pass applies.

This is the structural complement to the per-episode pipeline. Where per-episode catches per-line and per-arc faults, season-scope catches cross-episode faults that no single-episode review can detect by design.

### Pass S1 — Constraint audit (auditor #season-1)

Dispatch **auditor** (fork, fresh context) with:
- All per-episode proto-line files (`active-project/theater/proto-lines/<slug>.md` × N).
- All per-episode `episode-plan.md` files.
- All active condition cards under `active-project/warehouse/`.
- Series laws and lore from showrunner memory.
- Schema + harsh-SVO discipline.

Brief: every line in every episode must remain legal under SVO mechanics AND constraint-coherent across the season. Sweep:
- **Per-line mechanic re-check** at season scope catches drift (an episode that converged in isolation may now read against another episode's established slug or fact).
- **Cross-episode constraint coherence:** no episode violates a constraint established by another. Series laws and condition cards are honored consistently across all episodes.
- **Slug + reference resolution:** every actor / prop / location slug used in any episode resolves to the canonical card; no episode introduces a slug another episode lacks setup for.

Output: `active-project/staff/auditor/season-<slug>-pass-S1-constraint.md`. File-level: `PASS` or `FAIL` with classified findings. Faults route to fixer; cross-episode constraint faults that require chunk-statement revision route as `escalate` (surface to user).

### Pass S2 — Shape (dramatist, season scope)

Dispatch **dramatist** with:
- All per-episode proto-line files in canonical season order.
- All episode-plans (chunk + change + theme per episode).
- `season-<slug>-plan.md` (escalation spine, forward flags).
- `series-plan.md` (escalation spine).
- Behavior cards (full inheritance stack) for the season's full active cast.

Brief: assess the season as one curve. Sweep:
- **Season-level rise-peak-fall:** per-episode peaks should escalate cumulatively per the season escalation spine. The terminal peak lands at the season-cap episode, not earlier.
- **Episode-as-act structure:** each episode plays a structural role in the season's arc (setup / rising / midpoint / crisis / climax / falling). No episode is structurally redundant.
- **Cross-episode flatlines:** 3+ consecutive episodes without an inflection beat is a season flatline.
- **Forward-flag honor:** commitments from `season-plan.md` (e.g. "E4: active attempt required; E5: irreversible board action required") are visible in the corresponding episodes' proto-lines.
- **Inter-episode tempo:** density and weight of inter-episode transitions (the time-skip and chunk-boundary moments) match the season's pacing register.

Output: `active-project/staff/auditor/season-<slug>-pass-S2-shape.md` with `CLEAN` / `RE-ORDER-OR-REVISE` verdict, plus per-episode shape commentary if reorders are proposed. Reorders at season scope may move beats *between* episodes (a beat written at end-of-N moves to start-of-N+1) — these route to fixer with episode-pair scope.

### Pass S3 — Trim (audience ×3, season scope)

Dispatch the three audience personas in parallel, each with:
- All per-episode proto-line files.
- The **season goal** — distilled by orchestrator from `season-plan.md` season chunk + season theme + season escalation spine. Pinned at top of the season-scope trim brief, north star for trim decisions.
- Per-episode `goal:` headers (the per-episode north stars, still active but subordinate to season goal at this scope).
- All active actor vibes, studio vibes, persona cards, behavior cards.
- Full series-plan and season-plan prose.

Brief: walk every numbered non-blank line across every episode. Apply the trim test against the **season goal** rather than the per-episode goal. A line that serves its episode's local goal but actively distracts from the season arc is a deletion candidate. Voice-load-bearing test still applies (the actor's behavior signature licenses keeps).

≥2-persona threshold for auto-accept deletion across episodes. File-level verdict per persona: `ACCEPT` or `REVISE-{one-clause-reason}`.

Output: `active-project/staff/auditor/season-<slug>-pass-S3-trim-{persona}.md` × 3.

If all three personas ACCEPT in one round, Pass S3 terminates. If any REVISE, the named entertainment problem (a beat or full episode is missing, the season rhythm fails, the season goal is not delivered) routes to screen-writer for episode-level addition; the affected episode re-runs through its per-episode pipeline; then Pass S3 re-runs.

### Pass S3.5 — Ruleset compliance (auditor #season-3, dedicated)

**The mechanic-strictness pass.** Per-episode Pass 2 catches mechanic faults at episode scope; this pass re-checks the **entire season's proto-line set** against the harsh-SVO ruleset to catch verbs that survived per-episode review by being borderline in isolation but reading as a season-wide pattern of compliance drift.

Dispatch **auditor** (fork, fresh context, dedicated to ruleset-compliance) with:
- All per-episode proto-line files.
- Schema: `schemas/proto-line.schema.md`.
- SVO discipline (full): `svo-writer-pass1-brief.md` §"SVO discipline" — every clause, especially the non-action-verb deny-list and the narrow `holds` license.
- The 15 ambiguity calls: `svo-split-notes.md`.

Brief — explicit ruleset checklist:
- Walk every numbered, non-blank line across every chapter.
- For each line, evaluate against the **non-action-verb deny-list**: `has`, `had`, `have`, `having`, `owns`, `owned`, `belongs to`, `possesses`, `carries`, `carried`, `carrying`, `bears`, `bore`, `wears`, `wore`, `keeps`, `kept`, `contains`, `houses`, `occupies`, `inhabits`, `consists of`, `comprises`, `lies`, `sits`, `stands` (position-naming), and disallowed `holds` uses.
- For each `holds` instance, license-check: body-part-object (license #1) or physical-object-resisting-pressure (license #2). Otherwise FAULT-FORM-NON-ACTION-VERB.
- Re-check the harsh-SVO discipline mechanically: copulas, negations, perception verbs, modifiers, conjunctions, abstractions-as-objects.
- Report drift patterns: a verb that appears 5+ times across the season as a borderline state-verb is a *pattern* — flag for systematic recast, not just per-line repair.

Output: `active-project/staff/auditor/season-<slug>-pass-S3.5-ruleset.md`. File-level: `RULESET-CLEAN` or `RULESET-FAIL` with classified findings + drift-pattern report.

This pass exists because the user surfaced the failure mode explicitly: a high-quality proto-line set is what makes every downstream facet easier. State-verbs that read as actions (`carries`, `holds the ledger`, `has the letter`) corrupt facet authoring because facets cite proto-lines as physical events; if the cited "event" is a state, the facet becomes a state-of-state, doubled.

### Pass S4 — Continuity (auditor #season-2)

Dispatch **auditor** (fork, fresh context, distinct from S1's auditor invocation) with:
- The post-trim, post-shape season state (all proto-line files + all episode-plans).
- Season chunk + season change (if season-level change is named in `season-plan.md`).
- Series laws.
- Active location cards.

Brief — same four sweeps as per-episode Pass 5, scaled up:
- **Reachability:** season-start state → season-end state. The opening of the season's first episode and the close of its last episode bracket a delta the season-plan promises; the surviving proto-line set must traverse it.
- **State:** track every prop and every actor across the season (not just within one episode). A prop introduced in episode 1 is either consumed/explicitly released by season's end or persists through the season as a recurring object. Actors enter and exit the season's stage coherently.
- **Reference:** every slug used resolves; no episode references an actor or prop another episode hasn't set up.
- **POV:** narrator-consistency across episode boundaries. If episode N narrator is Taylor and episode N+1 narrator is Plumm, the POV transition is honest (Plumm is on-stage at end of N or arrives at start of N+1; the chunk handles the handoff).

Output: `active-project/staff/auditor/season-<slug>-pass-S4-continuity.md`. File-level: `SEASON-CONTINUITY-OK` or `SEASON-CONTINUITY-FAIL`. Faults route to fixer; structural reachability faults at season scope route as `escalate`.

### Pass S5 — Voice register coherence (dramatist, second invocation)

Dispatch **dramatist** (second invocation, distinct from S2) with:
- All per-episode proto-line files.
- Behavior cards (full inheritance stack) for every actor active anywhere in the season.
- Per-actor vibes.

Brief: each actor's voice register must stay consistent across the season's chapters per their behavior card. Specifically:
- The verbs an actor *takes* across all their proto-lines should match the actor's voice signature (e.g. Taylor's hold-against-pressure pattern; Plumm's administrative-action pattern; Mira's observable-paralysis pattern).
- An actor that performs an out-of-register act in one chapter (e.g. Taylor performing a register-foreign action that breaks her behavior card) is flagged.
- Across the season, actors don't drift: their first-chapter voice and their last-chapter voice are recognizably the same person modulo arc-driven change.

Output: `active-project/staff/auditor/season-<slug>-pass-S5-voice-coherence.md`. Verdict: `VOICE-COHERENT` or `VOICE-DRIFT` with per-actor flags.

### Pass S6 — Vibe and theme alignment (audience ×3, second invocation against vibe layer)

Dispatch the three audience personas in parallel (second invocation, distinct from S3 which trims against goal). Brief: read the season as a tonal arc.
- Each chapter's beats honor the active vibe-cloud (per-actor vibes + studio vibes for that chapter's setting).
- The series.theme propagates into chapter-level beats; no chapter reads off-theme against neighbors.
- The season's tonal register is consistent — pulp fast/dramatic at the spine; institutional cold at the customary-authority moments; etc.

Per-persona output: `season-<slug>-pass-S6-vibe-{persona}.md`. File-level: `VIBE-ALIGNED` or `VIBE-DRIFT-{reason}`. Same ≥2-persona threshold for accepting drift flags.

### Pass S7 — Facet-readiness (auditor #season-4, dedicated)

The point of harsh-SVO discipline is that downstream facets cite proto-lines as load-bearing physical events. This pass verifies the season's proto-line set is *primed for facet authoring*.

Dispatch **auditor** (fork, fresh context, dedicated to facet-readiness) with:
- All per-episode proto-line files.
- The facet schemas: `schemas/facet.schema.md`, `schemas/dialogue.schema.md`.
- The locked facet rubrics for already-tuned facets (`design/shoot-v2/rubric-{location-state,tensometer,narrator-interest,state-updates,memory-flags,sensory,feeling-flags,dialogue}.md`).

Brief — for each load-bearing beat:
- Is there a proto-line a location-state facet author can cite for environment changes?
- Is there a proto-line a state-updates facet author can cite for canonical-state shifts?
- Is there a proto-line a tensometer author can rate without ambiguity?
- Are dialogue beats shaped as `<speaker> speaks to <listener>` with valid listener entities?
- Are the chapters' peaks the kind of beats narrator-interest can spotlight?
- Are there over-dense stretches (10+ beats per scene with no inflection) that will resist tens curve-shape rubric?
- Are there under-dense stretches (a chunk-statement-implied beat with zero supporting proto-lines) that will leave facets nothing to cite?

Output: `season-<slug>-pass-S7-facet-readiness.md`. Verdict: `FACET-READY` or `FACET-GAPS` with the facet name(s) that will struggle.

### Pass S8 — Plausibility (dramatist + auditor hybrid)

Two distinct plausibility tests, dispatched as a single hybrid review:

**S8a — Character-action plausibility (dramatist).** For every line where a named actor performs an action: would this character actually do that, given their behavior card, persona card, vibes, and prior-chapter actions? An action that a character *could* legally take per their cards but would not realistically choose under the chapter's circumstances is flagged. This is sharper than voice register (S5) — voice register asks "does this sound like the character?", plausibility asks "is this what the character would *do*?".

**S8b — Event-in-world plausibility (auditor).** For every beat: is this event plausible in the world given the active condition cards, series laws, and lore? An event that doesn't violate a constraint but would not realistically occur given how the world works (an institutional move that never would have been authorized; a fauna behavior outside what the species actually does; a procedural sequence that elides a step administrators would never skip) is flagged.

Inputs: all per-episode proto-lines, all chapter-plans, all behavior cards, all condition cards, series-plan + season-plan prose, active actor vibes.

Output: `season-<slug>-pass-S8-plausibility.md`. Per-beat verdicts: `PLAUSIBLE` / `IMPLAUSIBLE-CHARACTER-{slug}` / `IMPLAUSIBLE-EVENT-{condition-or-law}`. File-level: `PLAUSIBLE` or `IMPLAUSIBLE` with classified findings.

Faults route to fixer for line-level recast; structural implausibility (a chapter built on an implausible premise) routes as `escalate`.

### Pass S9 — Comprehensibility (audience ×3, third invocation)

Dispatch the three audience personas in parallel (third invocation; distinct from S3 trim and S6 vibe). Brief: read the season as a comprehensibility test for a reader who only has the proto-line set + downstream stitched prose to work with.

Per-beat questions:
- If this beat were *missed* by the reader (skim, distraction, flagged inattention), would the rest of the chapter still cohere? A beat whose absence would break comprehension is **load-bearing** — flag it as a candidate for emphasis, parallel anchoring (a second beat that conveys the same fact), or relocation to a more attention-prominent position.
- Is the cause-effect chain between this beat and the next legible without exposition? If reader-comprehension requires interiority, narrator-summary, or off-stage knowledge, the chain is **fragile** — flag for either an additional bridge proto-line or a richer downstream facet investment.
- Does the proto-line as written carry enough information for a reader to know *what happened* and *who did what to whom*? Ambiguous slugs, under-specified verbs (`taylor moves` with no destination), and pronoun-equivalent referents are flagged.

Per-persona output: `season-<slug>-pass-S9-comprehensibility-{persona}.md`. File-level: `COMPREHENSIBLE` or `COMPREHENSIBILITY-RISK-{reason}`.

Faults at this pass are particularly important because they predict facet-authoring pain. A beat that requires an explicit narrator-interest fire to be comprehensible is OK; a beat that requires a *miracle* of stitcher-rendering to be comprehensible is not.

### Convergence

Phase 3 converges when **all nine season-scope passes return clean verdicts in a single end-to-end run** (S1 constraint, S2 shape, S3 trim, S3.5 ruleset, S4 continuity, S5 voice, S6 vibe, S7 facet-readiness, S8 plausibility, S9 comprehensibility). The same iteration loop applies — a change at any pass invalidates downstream passes for that run; downstream re-runs from the changed point. If end-to-end convergence is not reached after **3 full season-scope iterations**, ship with a header comment noting non-convergence and surface for user review.

The four-pass season-scope review is the load-bearing piece for "chapters feel natural and less jarring." It is the same architecture as per-episode review, applied at the right scope to catch the right faults.

---

## Phase 4 — Persist

1. Update `active-project/staff/showrunner/memory.md`:
   - Each episode: status `planned` → `protolined`.
   - Season: add `season.protolines_complete` field with timestamp + comprehensive audit path.
   - Season: status remains `active` (the season isn't `wrapped` until /and-wrap runs).
2. Print summary:

```
--- SEASON PROTO-LINES COMPLETE: <season-slug> ---

Episodes drafted: <list>
Total proto-lines: <count across all episodes>
Total time-skips: <count>
Total deletions: <count>
Total transitions added: <count>

Per-episode trajectory:
  <slug> | <iterations to converge> | <pass-2-final> | <pass-5-verdict>
  ...

Season-scope review (4 passes, mirror of per-episode):
  S1 constraint audit:   <PASS | FAIL with fault count by class>
  S2 shape (dramatist):  <CLEAN | RE-ORDER-OR-REVISE>
  S3 trim (audience ×3): <ALL-ACCEPT | REVISE-{persona}>
  S4 continuity audit:   <SEASON-CONTINUITY-OK | SEASON-CONTINUITY-FAIL>
  iterations to converge: <n>
  file-level: <SEASON-CONVERGED | SEASON-FAIL with failing pass names>

Files:
  active-project/theater/<slug>/episode-plan.md (× N)
  active-project/theater/proto-lines/<slug>.md (× N)
  active-project/staff/auditor/season-<slug>-pass-S1-constraint.md
  active-project/staff/auditor/season-<slug>-pass-S2-shape.md
  active-project/staff/auditor/season-<slug>-pass-S3-trim-{pulp,pedant,dark}.md
  active-project/staff/auditor/season-<slug>-pass-S4-continuity.md

Next: facet authoring per episode (/and-locstate, /and-dialogue, etc.) or /and-shoot for performance pass, or /and-wrap for season close.
```

---

## Notes

- This command **does not re-implement** /and-protolines-v2's five-pass pipeline. It chains the existing pipeline and adds the season-scope decomposition (Phase 1) and coherence audit (Phase 3) layers.
- Episode-decomposition (Phase 1) and per-episode protolines (Phase 2) are deliberately separated — the decomposition is a fast structural pass that can run in parallel; protolines is the slower five-pass-per-episode chain that must run sequentially to thread audience STM and detect drift early.
- The comprehensive auditor at Phase 3 is what makes "chapters feel natural and less jarring" — it surfaces cross-episode seams that no per-episode pipeline can catch by design (the per-episode pipeline is blind to neighbors). When this audit fires faults, the cost of repair scales with how late they're caught; running this audit at season-protolines-complete (before facet authoring or shoot) is the cheapest correction point.
- Prerequisites:
  1. `/and-protolines-v2` promoted to `/and-protolines`.
  2. `schemas/proto-line.schema.md` updated with per-episode path convention + header fields + harsh-SVO discipline.
  3. `schemas/episode-plan.schema.md` updated with required `narrator` and `goal` fields.
  4. The active project has a season-plan.md with per-episode chunk paragraphs (current `/and-project` produces this for season 1).
- Subsequent-season equivalent: when season N+1 is activated, /and-season N+1 can be invoked. The comprehensive audit at Phase 3 only checks intra-season coherence; cross-season coherence is the showrunner's job at season-start (re-reading series-plan.md against the previous season's outcomes).
