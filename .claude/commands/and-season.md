---
description: Season-scope orchestrator. Takes a season chunk (from season-plan.md), decomposes into episode-plans, expands the chunk list into a single aggregate SVO proto-line object, iterates the five-pass SVO pipeline + nine-pass season-scope review against that aggregate, then splits to canonical per-episode files. Usage - /and-season [season-slug]
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

## Phase 2 — Aggregate proto-line authoring

Coming into Phase 2 you have a list of episode chunks (from `season-<slug>-plan.md`) plus per-episode `episode-plan.md` files (from Phase 1) carrying the structural fields each chunk implies — `narrator`, `goal`, `actors`, `constraints`, `change`, `theme`. Phase 2 expands this list into a **single aggregate SVO object** that covers the entire season, then iterates the five-pass SVO-writer pipeline against that one object before any per-episode split.

The aggregate is the canonical artifact through review and revision. Per-episode files are derived from it at Phase 4 (split), not before.

### Output path

`active-project/theater/proto-lines/<season-slug>.aggregate.md`

Internal section delimiters per episode (or per chapter, when the season is decomposed chapter-scoped):

```
# === episode: s01e01 ===
narrator: <slug>
goal: <one sentence from episode-plan.md>

1 ...
2 ...

# === episode: s01e02 ===
narrator: <slug>
goal: ...

1 ...
```

ID numbering restarts at 1 per section. Section delimiters are load-bearing: they are how Phase 4 splits the aggregate back into canonical per-episode files.

### Sub-passes (mirror of `/and-protolines-v2` five-pass pipeline, run against the aggregate)

1. **Pass 1 — Inventory write.** Single SVO-writer dispatch. Inputs: the full chunk list, all episode-plans, series/season vibes, constraints, behavior cards. Output: the aggregate file with all sections populated in one pass. Audience STM threads naturally within the writer's own context — no cross-dispatch threading needed since this is one dispatch.
2. **Pass 2 — Constraint audit.** Auditor fork against the aggregate. Sweep all sections against condition cards, series laws, harsh-SVO discipline.
3. **Pass 3 — Shape.** Dramatist against the aggregate. Each section's per-episode shape AND the cross-section escalation arc.
4. **Pass 4 — Trim.** Audience ×3 against the aggregate. Per-section ENGAGED/TOLERATED/BORED + season-wide entertainment-density check.
5. **Pass 5 — Continuity.** Auditor #2 fork against the aggregate. Cross-section state, prop chains, POV transitions, reachability.

Faults route to fixer (line edits) or screen-writer (section regenerations or cross-section restructures). Each fix invalidates downstream passes for the affected scope; downstream re-runs from the changed point.

Convergence cap: **3 full pipeline iterations.** Non-convergence aborts the season chain and surfaces for human review with the failing-pass list.

### Why aggregate-first

- Cross-episode coherence is *built in* at write time, not bolted on after the fact. The writer sees the whole season at once and never has to retrofit cross-section consistency.
- Audience STM threading happens within the writer's own context, removing the sequential-only constraint that previous per-episode chaining required.
- Review operates on a single object, which matches how downstream readers consume the season (continuously, not episode-by-episode with hidden seams).
- Splitting at Phase 4 is mechanical (delimiter scan), not interpretive — no information is lost.

### Relationship to `/and-protolines-v2`

`/and-protolines-v2` remains the per-episode standalone authoring command for ad-hoc work or single-episode revision. Its five passes are the *template* for Phase 2's sub-passes here, scaled up to season scope. The pipeline does not invoke `/and-protolines-v2` per episode anymore.

---

## Phase 3 — Comprehensive season-scope review

After Phase 2 produces a converged aggregate proto-line file, run the **nine-pass season-scope review** against that single aggregate. Same reviewer roles as per-episode review, same dispatch shape, same convergence definition (all passes clean in one end-to-end run) — the scope of "the file under review" is the season aggregate and its sections; the criteria each pass applies are season-scope (cross-section coherence, season escalation arc, season-wide entertainment density, etc.).

This is the structural complement to the per-episode pipeline. Where per-episode catches per-line and per-arc faults, season-scope catches cross-episode faults that no single-episode review can detect by design.

### Pass S1 — Constraint audit (auditor #season-1)

Dispatch **auditor** (fork, fresh context) with:
- The season aggregate proto-line file (`active-project/theater/proto-lines/<season-slug>.aggregate.md`). Sections delimit per-episode scope inside it.
- All per-episode `episode-plan.md` files.
- All active condition cards under `active-project/warehouse/`.
- Series laws and lore from showrunner memory.
- Schema + harsh-SVO discipline.

Brief: every line in every episode must remain legal under SVO mechanics AND constraint-coherent across the season. Sweep:
- **Per-line mechanic re-check** at season scope catches drift (an episode that converged in isolation may now read against another episode's established slug or fact).
- **Cross-episode constraint coherence:** no episode violates a constraint established by another. Series laws and condition cards are honored consistently across all episodes.
- **Slug + reference resolution:** every actor / prop / location slug used in any episode resolves to the canonical card; no episode introduces a slug another episode lacks setup for.

Output: `active-project/staff/auditor/season-<slug>-pass-S1-constraint.md`. File-level: `PASS` or `FAIL` with classified findings. Faults route to fixer; cross-episode constraint faults that require chunk-statement revision route as `escalate` (surface to user).

### Pass S2 — Shape (dramatist, season scope) — STRICT

Dispatch **dramatist** with:
- The season aggregate proto-line file. Sections appear in canonical season order.
- All episode-plans (chunk + change + theme + narrator + goal per episode).
- `season-<slug>-plan.md` (escalation spine, forward flags).
- `series-plan.md` (escalation spine).
- Behavior cards (full inheritance stack) for the season's full active cast.

You are a **strict** structural critic. Your job is to enforce dramatic shape at season scale — not approve it. A season that does not have an identifiable buildup, climax, and denouement is a structural failure regardless of how clean each chapter reads.

#### Mandatory structural identification (must be filled in)

Before any other check, label the season's three structural acts by **citing specific chapters** (and where load-bearing, specific proto-line IDs):

- **Season buildup (rising chapters):** chapters `<from>`–`<to>`. The chapters where season stakes are introduced and the season's question is posed. If you cannot name a buildup, flag `NO-SEASON-BUILDUP`.
- **Season climax (peak chapter):** chapter `<n>` (and the specific proto-line IDs within that chapter that constitute the peak beat). The single highest-stakes chapter where the season's tension turns. If you cannot point to a single peak chapter, flag `NO-SEASON-CLIMAX`.
- **Season denouement (falling chapters):** chapters `<from>`–`<to>`. The post-peak release. If absent, flag `NO-SEASON-DENOUEMENT`.

Additionally, for **each chapter individually**, restate the dramatist's per-chapter Pass-3 structural identification (buildup IDs, climax ID, denouement IDs) at season scope. A chapter that converged at Pass 3 in isolation may now read differently against its neighbors — re-evaluate. If you cannot fill in a chapter's buildup/climax/denouement here at season scope, flag `CHAPTER-STRUCTURAL-FAILURE-<n>`.

#### Per-chapter role in season arc

Each chapter must play one and only one of: `setup` / `rising-1` / `rising-2` / `midpoint` / `complication` / `crisis` / `climax` / `falling` / `resolution`. Assign each chapter exactly one role and state what the chapter delivers to that role. A chapter whose role is unclear or duplicated is `REDUNDANT-CHAPTER-<n>`.

#### Sweep checks

- **Season-level rise-peak-fall:** per-chapter peaks escalate cumulatively per the season escalation spine. The terminal peak lands at the climax chapter, not earlier.
- **Cross-chapter flatlines:** 3+ consecutive chapters without an inflection beat is a season flatline.
- **Forward-flag honor:** commitments from `season-plan.md` (e.g. "E4: active attempt required; E5: irreversible board action required") are visible in the corresponding chapters' proto-lines. A missing commitment is a structural fault.
- **Inter-chapter tempo:** density and weight of inter-chapter transitions match the season's pacing register.
- **Premature peak / late peak:** climax chapter must be in the back half of the season (chapters 6–9 of 10 typical). Earlier or later flags `EARLY-SEASON-PEAK` or `LATE-SEASON-PEAK`.

Output: `active-project/staff/auditor/season-<slug>-pass-S2-shape.md`. Verdict: `CLEAN` / `RE-ORDER-OR-REVISE` / `STRUCTURAL-FAILURE`. Include the mandatory structural identification table (season + per-chapter roles) at the top. Reorders at season scope may move beats *between* chapters (a beat written at end-of-N moves to start-of-N+1) — these route to fixer with chapter-pair scope. `STRUCTURAL-FAILURE` cannot be cleared by reorders alone — escalate to user with the named structural fault.

Bias: when in doubt, flag. The cost of a false-positive is one revision; the cost of a false-negative is a structurally weak season that no facet authoring can rescue.

### Pass S3 — Trim (audience ×3, season scope)

Dispatch the three audience personas in parallel, each with:
- The season aggregate proto-line file.
- The **season goal** — distilled by orchestrator from `season-plan.md` season chunk + season theme + season escalation spine. Pinned at top of the season-scope trim brief, north star for trim decisions.
- Per-episode `goal:` headers (the per-episode north stars, still active but subordinate to season goal at this scope).
- All active actor vibes, studio vibes, persona cards, behavior cards.
- Full series-plan and season-plan prose.

Brief: walk every numbered non-blank line across every chapter. Apply the trim test against the **season goal** rather than the per-chapter goal. A line that serves its chapter's local goal but actively distracts from the season arc is a deletion candidate. Voice-load-bearing test still applies (the actor's behavior signature licenses keeps).

**Entertainment-per-chapter check (MANDATORY).** You are a strict entertainment critic at season scale. For each chapter, log a one-line verdict:
- **ENGAGED** — your taste finds the chapter delivers a hook your persona is paid to want; you would lean forward to read the next chapter.
- **TOLERATED** — the chapter is functional but not entertaining in its own right.
- **BORED** — your taste actively disengages; the chapter is dead weight or off-register or violating something your persona card cares about.

Cap: a season may carry at most **one TOLERATED chapter** (typically a connective/setup chapter). Two or more TOLERATED chapters → REVISE with reason `season-attention-flatline-{chapter-range}`. Any BORED chapter → REVISE with reason `season-attention-failure-{chapter-n}` and a named cause.

Apply your **persona-specific** taste hard. A season that satisfies the season-goal generically but fails *your* persona's appetite is a failure for *you* — say so.

≥2-persona threshold for auto-accept deletion across chapters. File-level verdict per persona: `ACCEPT` or `REVISE-{one-clause-reason}`.

Bias: when in doubt, REVISE. The cost of a false-positive REVISE is one screen-writer revision. The cost of a false-negative is a season readers will skim.

Output: `active-project/staff/auditor/season-<slug>-pass-S3-trim-{persona}.md` × 3.

If all three personas ACCEPT in one round, Pass S3 terminates. If any REVISE, the named entertainment problem (a beat or full episode is missing, the season rhythm fails, the season goal is not delivered) routes to screen-writer for episode-level addition; the affected episode re-runs through its per-episode pipeline; then Pass S3 re-runs.

### Pass S3.5 — Ruleset compliance (auditor #season-3, dedicated)

**The mechanic-strictness pass.** Per-episode Pass 2 catches mechanic faults at episode scope; this pass re-checks the **entire season's proto-line set** against the harsh-SVO ruleset to catch verbs that survived per-episode review by being borderline in isolation but reading as a season-wide pattern of compliance drift.

Dispatch **auditor** (fork, fresh context, dedicated to ruleset-compliance) with:
- The season aggregate proto-line file.
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
- The post-trim, post-shape season state (the season aggregate proto-line file + all episode-plans).
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
- The season aggregate proto-line file.
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

**Per-chapter vibe verdict (MANDATORY):** for each chapter, log one of:
- `VIBE-ALIGNED` — the chapter sustains the active vibe-cloud and supports neighbor chapters' tones.
- `VIBE-DRIFT-{reason}` — the chapter reads off-tone (pulp where institutional was needed, comic where dread was building, etc.). Name the reason concretely.

Per-persona output: `season-<slug>-pass-S6-vibe-{persona}.md`. File-level: `VIBE-ALIGNED` (all chapters aligned) or `VIBE-DRIFT-{reason}` (one or more chapters drifted). Same ≥2-persona threshold for accepting drift flags.

Bias: when in doubt, flag drift. Vibe drift compounds across chapters; catching it at S6 is cheaper than at facet authoring.

### Pass S7 — Facet-readiness (auditor #season-4, dedicated)

The point of harsh-SVO discipline is that downstream facets cite proto-lines as load-bearing physical events. This pass verifies the season's proto-line set is *primed for facet authoring*.

Dispatch **auditor** (fork, fresh context, dedicated to facet-readiness) with:
- The season aggregate proto-line file.
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

Inputs: the season aggregate proto-line file, all chapter-plans, all behavior cards, all condition cards, series-plan + season-plan prose, active actor vibes.

Output: `season-<slug>-pass-S8-plausibility.md`. Per-beat verdicts: `PLAUSIBLE` / `IMPLAUSIBLE-CHARACTER-{slug}` / `IMPLAUSIBLE-EVENT-{condition-or-law}`. File-level: `PLAUSIBLE` or `IMPLAUSIBLE` with classified findings.

Faults route to fixer for line-level recast; structural implausibility (a chapter built on an implausible premise) routes as `escalate`.

### Pass S9 — Comprehensibility (audience ×3, third invocation)

Dispatch the three audience personas in parallel (third invocation; distinct from S3 trim and S6 vibe). Brief: read the season as a comprehensibility test for a reader who only has the proto-line set + downstream stitched prose to work with. **You are also the entertainment-at-every-step gate of last resort.** If a reader would skim, disengage, or fail to track what is happening, the season is not shippable.

Per-beat questions:
- If this beat were *missed* by the reader (skim, distraction, flagged inattention), would the rest of the chapter still cohere? A beat whose absence would break comprehension is **load-bearing** — flag it as a candidate for emphasis, parallel anchoring (a second beat that conveys the same fact), or relocation to a more attention-prominent position.
- Is the cause-effect chain between this beat and the next legible without exposition? If reader-comprehension requires interiority, narrator-summary, or off-stage knowledge, the chain is **fragile** — flag for either an additional bridge proto-line or a richer downstream facet investment.
- Does the proto-line as written carry enough information for a reader to know *what happened* and *who did what to whom*? Ambiguous slugs, under-specified verbs (`taylor moves` with no destination), and pronoun-equivalent referents are flagged.

Per-window entertainment check (~10 lines per window) for the entire season: log `ENGAGED` / `TOLERATED` / `BORED` per window. Two consecutive `BORED` windows OR three consecutive `TOLERATED` windows OR any single chapter where ≥30% of windows are `BORED`-or-`TOLERATED` → file-level `COMPREHENSIBILITY-RISK-attention-{detail}`.

Per-persona output: `season-<slug>-pass-S9-comprehensibility-{persona}.md`. File-level: `COMPREHENSIBLE` or `COMPREHENSIBILITY-RISK-{reason}`. Bias: when in doubt, flag — this is the last gate before the season is shippable.

Faults at this pass are particularly important because they predict facet-authoring pain. A beat that requires an explicit narrator-interest fire to be comprehensible is OK; a beat that requires a *miracle* of stitcher-rendering to be comprehensible is not.

### Convergence

Phase 3 converges when **all nine season-scope passes return clean verdicts in a single end-to-end run** (S1 constraint, S2 shape, S3 trim, S3.5 ruleset, S4 continuity, S5 voice, S6 vibe, S7 facet-readiness, S8 plausibility, S9 comprehensibility). The same iteration loop applies — a change at any pass invalidates downstream passes for that run; downstream re-runs from the changed point. If end-to-end convergence is not reached after **3 full season-scope iterations**, ship with a header comment noting non-convergence and surface for user review.

The four-pass season-scope review is the load-bearing piece for "chapters feel natural and less jarring." It is the same architecture as per-episode review, applied at the right scope to catch the right faults.

---

## Phase 4 — Split aggregate to canonical per-episode files

Run after Phase 3 converges. Mechanical, not interpretive.

1. Read `active-project/theater/proto-lines/<season-slug>.aggregate.md`.
2. Scan for section delimiters of the form `# === episode: <slug> ===` (or `# === chapter: NN ===` when the season is decomposed chapter-scoped).
3. For each section, write the section body (header lines `narrator:` + `goal:` + numbered bones) to `active-project/theater/proto-lines/<slug>.md`.
4. Validate: each per-episode file has `narrator`, `goal`, contiguous-or-blank ID numbering starting at 1, and no orphan content outside its section.
5. The aggregate file is preserved as the canonical pre-split artifact. Per-episode files are derived; if downstream work needs to revise a section, edit the aggregate and re-run the split.

Splitting is the *last* mutation in the pipeline. After this phase the proto-lines are ready for facet authoring (which cites per-episode files) or for /and-shoot (which reads the active episode's per-episode file).

---

## Phase 5 — Persist

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

- This command **mirrors but does not invoke** /and-protolines-v2's five-pass pipeline. The five passes are run against the season aggregate as a single object — not chained per-episode. /and-protolines-v2 remains the standalone per-episode authoring command for ad-hoc work or single-section revision.
- Episode-decomposition (Phase 1) and aggregate authoring (Phase 2) are deliberately separated — the decomposition is a fast structural pass that runs in parallel; aggregate authoring is one writer dispatch for the whole season followed by review-and-revise on the single object. Audience STM threading happens within the writer's own context (single dispatch) rather than across separate dispatches.
- The aggregate-first architecture means cross-episode coherence is built in at write time rather than retrofitted at audit time. Phase 3's job shifts from "catch cross-section drift" to "verify the season's seamlessness was preserved through revision."
- The comprehensive auditor at Phase 3 is what makes "chapters feel natural and less jarring" — it surfaces cross-episode seams that no per-episode pipeline can catch by design (the per-episode pipeline is blind to neighbors). When this audit fires faults, the cost of repair scales with how late they're caught; running this audit at season-protolines-complete (before facet authoring or shoot) is the cheapest correction point.
- Prerequisites:
  1. `/and-protolines-v2` promoted to `/and-protolines`.
  2. `schemas/proto-line.schema.md` updated with per-episode path convention + header fields + harsh-SVO discipline.
  3. `schemas/episode-plan.schema.md` updated with required `narrator` and `goal` fields.
  4. The active project has a season-plan.md with per-episode chunk paragraphs (current `/and-project` produces this for season 1).
- Subsequent-season equivalent: when season N+1 is activated, /and-season N+1 can be invoked. The comprehensive audit at Phase 3 only checks intra-season coherence; cross-season coherence is the showrunner's job at season-start (re-reading series-plan.md against the previous season's outcomes).
