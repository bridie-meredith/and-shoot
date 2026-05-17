---
description: Activate a new and-shoot project. Scaffolds active-project/, runs boundary-scoping (Phase 1.4 fork), taste selection (Phase 1.5 taste-judge), world-building, and series planning (steps 1a–1d + series plan), and presents output for human audit. Season planning is out of scope — run /and-season s01 after activation. No titles. Usage: /and-project ["<brief>"]
---

Full project activation for the and-shoot pipeline. Phases: scaffold (mechanical, direct), boundary scoping (isolated fork), taste selection (taste-judge single-card critic fork), brief expansion (screen-writer), audience selection, planning (you orchestrate directly). **Single human checkpoint:** series-level audit (Phase 3, after planning). Boundary scope and taste selection both run as isolated forks before any editorial work — the boundary fork enumerates what the prompt fixed vs. what it left open, and the taste-judge picks story-type and archetypes from the boundary fork's menus by entertainment fit. The taste-judge is a single audience/critic dispatch loading `staff/audience/taste-judge/card.md` in single-card configuration (the user's pre-installed stand-in card); the user is not asked to select. The orchestrator never picks inline — that contamination path is what these two forks exist to prevent.

**Scope.** /and-project ends at the series-level audit. Season planning (drama, vibe-cloud delta, content beats) is owned by `/and-season <slug>` Phase 1, which auto-fires when no `season-<slug>-plan.md` exists. After human approval at the audit checkpoint, the next command is `/and-season s01` (which plans the season then continues into bone authoring + interpretive split). Separation of duties: /and-project = world + series; /and-season = season planning + bone authoring + interpretive split.

You are the orchestrator for this command. You dispatch subagents directly — screen-writer, margit, dramatist, audience, auditor, fixer. Do not dispatch showrunner. Showrunner is not in the orchestration chain here.

**All dispatches use the Agent tool.** Inline generation is not a valid substitute. An agent not spawned in its own isolated context will not have the role constraints the pipeline depends on.

## Args

- `$1` — optional. The human brief, quoted as a single string. Everything the human said about the project: source world, destination world, characters, constraints, tone, anything. Pass verbatim. If omitted or empty, run in **random-brief mode** — screen-writer generates the brief with no input constraints.

Audience selection is automatic — do not accept audience slugs as arguments. The orchestrator selects audience personas in Phase 1.6 based on the brief content. This cannot be overridden at the command line.

---

## Phase 1 — Scaffold

Execute mechanically. Do not delegate. Complete before proceeding to Phase 1.5.

### 1. Validate

Check whether $1 is provided. If absent or empty, note that random-brief mode will run in Phase 1.5. No other validation — audience slugs are not args and are not validated here.

### 2. Shelve previous active-project

If `active-project/` exists and contains any content beyond empty stub files (i.e., a prior project was run):
1. Determine the next serial: list `projects/` for existing `project_NN` directories, take the highest N, increment by 1. First project shelves to `projects/project_01/`.
2. Move `active-project/` to `projects/project_NN/`.
3. Print: `Shelved previous project → projects/project_NN/`

If `active-project/` does not exist or is empty (first run), skip this step.

### 3. Create directory tree

```bash
mkdir -p active-project/actors
mkdir -p active-project/warehouse
mkdir -p active-project/staff/showrunner
mkdir -p active-project/staff/studio
mkdir -p active-project/staff/auditor
mkdir -p active-project/staff/fixer
mkdir -p active-project/staff/margit
mkdir -p active-project/staff/editor
mkdir -p active-project/theater
mkdir -p active-project/polish
```

### 4. Write stub files

Write each with minimal valid content. Do not write empty files.

**`active-project/staff/showrunner/memory.md`**
```yaml
# showrunner memory — schema: schemas/showrunner-memory.schema.md

routing:
  show_file: active-project/theater/show.md
  episode_plan: active-project/theater/episode-plan.md
  series_plan: active-project/staff/showrunner/series-plan.md
  season_plan: ~

series:
  theme: ~
  laws: []
  lore: []
  behaviors: []
  plot:
    start: ~
    end: ~
    protagonist_arc: ~
    series_question: ~
  cast_roster: []
  stage_elements: []

seasons: []

active:
  season: ~
  episode: ~
```

**`active-project/staff/showrunner/series-plan.md`**
```
# Series Plan — detail companion to memory.md
```

**`active-project/staff/showrunner/world-notes.md`**
```
# World Notes — Decided Constraints
# Internal. Written in step 1a. One constraint per line. Law/Lore/Behavior prefix where applicable.
```

**`active-project/staff/showrunner/open-questions.md`**
```
# Open Questions
# Internal. Written in step 1a. Ordered by dependency. Each resolved OQ moves to world-notes.md.
```

**`active-project/staff/studio/ltm.md`**
```
# Studio LTM — schema: schemas/memory.schema.md §LTM
```

**`active-project/staff/studio/stm.md`**
```
STM:
```

**`active-project/staff/studio/state.md`**
```
STATE:
  active_location: ~
  active_conditions: []
  prop_positions: {}
  time_of_day: ~
  weather: ~
```

**`active-project/staff/studio/vibes.md`**
```
VIBES:
```

**`active-project/staff/margit/margit.memory.md`**
```
# Margit Working Memory — cards authored, indexed, and promoted this project.
```

### 5. Confirm card library

Verify `cards/personas/INDEX.md` and `cards/locations/INDEX.md` exist. Print line counts.

### 6. Print scaffold complete

```
Scaffold complete.
```

If a brief was provided ($1 non-empty), proceed to Phase 1.4. If absent, proceed to Phase 1.2 (random-brief generation) first.

---

## Phase 1.2 — Random-brief generation (conditional; only if $1 was empty)

If a brief was provided, skip this phase entirely.

If not: dispatch screen-writer with no constraints. Screen-writer reads `staff/audience/INDEX.md` and `cards/` to get a sense of available material, then proposes any premise — any genre, any source world, any structural register. Output written to `active-project/staff/showrunner/brief-generated.md`. From this point forward, the generated brief is the brief — Phase 1.4, Phase 1.5, Phase 1.6, and all downstream phases use it identically to a user-supplied brief.

This phase exists because Phase 1.4 (boundary scoping) requires a brief to scope. The original /and-project routed brief-generation through Phase 1.5 brief-expansion; that ordering was inverted when Phase 1.4 was added. Brief generation now happens once, up front, before any analytical work.

Print:
```
Brief generated. Running boundary scope.
```

If a brief was provided and this phase was skipped, follow Phase 1's "Scaffold complete." with a transition print before Phase 1.4:
```
Running boundary scope.
```

---

## Phase 1.4 — Boundary scoping (fork; isolated)

This phase exists to surface the load-bearing decisions implicit in the brief BEFORE any editorial work begins. It runs as an isolated fork — never inline. The fork writes its report and the pipeline continues; the user is not asked to select anything at this phase. Selection happens at Phase 1.5 via the taste-judge dispatch.

**Critical rule: NEVER INLINE.** All boundary analysis happens inside the fork. If the main session ever does its own boundary analysis (e.g., "let me also think about what's required..."), the isolation property is broken and downstream decisions will silently carry the contamination.

### 1. Dispatch the fork

Use the Agent tool with `subagent_type: general-purpose`. The fork's prompt MUST:

- Pass the user's brief VERBATIM (no paraphrase, no compression).
- Pass the structural end-requirement framing line where applicable ("the protagonist ends in a [bad-place / good-place / ambiguous-place], and the reason is [<cause structure>]").
- Forbid editorial choices: "If the prompt does not fix it, mark it OPEN. Do not invent setting specifics, factions, range numbers, neighborhoods, timelines, antagonists, or closing images."
- Forbid reading any prior /and-project artifacts (no world-notes.md, no series-plan.md, no boundary-scope.r*.md from prior revise loops, no shelved `projects/` content).
- Require four output sections, in this order, with these headings verbatim:
  1. **BOUNDARIES (what the prompt FIXES)** — every load-bearing decision the prompt fixes. For each: value + source phrase from the prompt + confidence (HIGH/MEDIUM/LOW). Fields to scan include but are not limited to: protagonist, protagonist condition at story-open, start-location, time-period, world-physics constraints, format/length, thematic spine, end-requirement, tonal register, audience.
  2. **OPEN PARAMETERS (what the prompt does NOT fix)** — enumerate every load-bearing decision the pipeline will need to make that the prompt does not specify. For each: name the decision and (one line) what kinds of values are admissible. Aim for completeness over brevity. Do not pick.
  3. **STORY TYPE (that fits the boundaries)** — 2–3 structural shapes that fit the boundaries. One-line distinction each. The end-requirement is the strongest determinant.
  4. **CHARACTER ARCHETYPES (that fit the boundaries and story type)** — per implied role (protagonist characterization, foil, false-ally, true-ally, antagonist-as-person, antagonist-as-institution, victim-by-which-cost-is-paid, witness, opposite-number), 2–4 archetype options.

The fork writes its full report to `active-project/staff/showrunner/boundary-scope.md`. Length budget: under 800 words total.

### 2. Read the report

Main session reads `boundary-scope.md` for handoff to Phase 1.5. **Do not re-analyze, re-rank, or compress.** Do not pick from the menus. Do not present anything to the user. Compression and pre-selection by the orchestrator are both contamination vectors — the taste-judge at Phase 1.5 sees the fork's report as the fork produced it.

### 3. Print phase-complete

```
Boundary scope written. Dispatching taste-judge.
```

---

## Phase 1.5 — Taste selection (taste-judge fork; isolated)

The taste-judge picks story-type and archetypes from the menus the boundary-scope fork produced. The user does not pick — a single stand-in agent picks based on entertainment fit. This is the design decision that keeps the pipeline moving without forcing the user to choose between equally-valid framings, while still surfacing those framings (via `boundary-scope.md`) for review at the Phase 3 series-level audit if the user wants to redirect.

**Critical rule: SINGLE AGENT, ISOLATED FORK.** The taste-judge is one audience/critic fork loaded with one persona card — the user-stand-in card. The audience class is the right dispatch because the critic already does what's needed with a persona card: load it, read the input, return a verdict (here: menu picks + per-pick reason). Single-card config, not the standing 3-persona plan-review triad — the plan-review triad is a separate Phase 1.7 selection. Not an inline main-session decision (that defeats the purpose — main session interpolation is what Phase 1.4 was added to prevent).

### 1. Locate the taste-judge persona card

The user-stand-in persona card lives at `staff/audience/taste-judge/card.md`. It is pre-installed (not project-scoped) and represents the user's entertainment taste as a single persona. If absent, halt Phase 1.5 and escalate to the user with: "Taste-judge persona card not found. Author `staff/audience/taste-judge/card.md` representing your entertainment taste, then re-run /and-project from Phase 1.5."

### 2. Dispatch the taste-judge

Use the Agent tool with `subagent_type: audience`. Dispatch ONE fork in single-card configuration. The fork's prompt MUST:

- Identify the persona card path: `staff/audience/taste-judge/card.md`. This is the only persona loaded for this dispatch — not the project's 3-persona triad.
- Identify the input path: `active-project/staff/showrunner/boundary-scope.md`.
- Frame the task as menu selection. "Read the boundary-scope. Apply the persona's selection discipline (§ in the card). Pick one option per menu — story-type, then each archetype role. One sentence of reason per pick, naming the structural fit, not the taste preference. Write picks to the taste-selection file. Do not write to any other file. Do not return prose review; return picks."
- Require these output sections, written to `active-project/staff/showrunner/taste-selection.md`:
  1. **Story-type pick** — the chosen story-type from the fork's STORY TYPE menu. One sentence: why this is most entertaining for the persona.
  2. **Archetype picks (per role)** — for each role the fork enumerated, the chosen archetype. One sentence per role: why this archetype is most entertaining for the persona.
  3. **Notes** — optional. Any tension the persona felt between story-type and archetype fit; any open parameter the persona has a strong preference on (advisory only — not pinning).

Length budget: under 400 words.

### 3. Read the taste-judge's picks

Main session reads `taste-selection.md`. Validate that:
- Story-type pick appears in the boundary-scope's STORY TYPE menu (verbatim slug or near-verbatim).
- Each archetype pick appears in the boundary-scope's corresponding role menu.

If a pick is off-menu, dispatch the taste-judge again with a constraint clarification ("your prior pick `<name>` is not in the menu; pick from these options: <list>"). Two retries max. After two retries, escalate to user.

### 4. Print the picks (informational; no checkpoint)

Print a one-line summary of the picks for transparency. This is NOT a checkpoint — the pipeline does not pause. Format:

```
Taste-judge picks:
  story-type: <chosen>
  archetypes: <role>: <pick>; <role>: <pick>; ...
Continuing.
```

### 5. Write the prompt-binding sheet

Write `active-project/staff/showrunner/prompt-binding.md`:

```
# Prompt Binding Sheet — generated at Phase 1.5
# This is the canonical input for all downstream phases.

## Original prompt (verbatim)
<the user's brief as supplied, character-for-character>

## Boundaries (fixed by prompt — verbatim from boundary-scope.md §1)
<copied verbatim from the fork's report>

## Story-type (taste-judge pick at Phase 1.5)
<chosen-name>
reason: <one-sentence reason from taste-selection.md>

## Archetype picks per role (taste-judge picks at Phase 1.5)
- <role>: <pick> — <reason>
- <role>: <pick> — <reason>
...

## Pinned open parameters
(none at Phase 1.5; pinning is reserved for user override at the Phase 3 audit checkpoint)

## Remaining open parameters
- <name>
- <name>
...
```

The binding sheet is the operative contract for everything downstream. Brief-expansion reads it. 1a reads it. 1b loops only on remaining-open parameters that need OQs. 1c/1d/series-plan all consume it.

### 6. Print phase-complete

```
Taste selection written. Binding sheet written.
Running brief expansion within the confirmed bounds.
```

---

## Phase 1.6 — Brief expansion

Random-brief mode no longer interacts with this phase. Brief generation runs at Phase 1.2 (before boundary scope); by the time this phase runs, the brief exists at `active-project/staff/showrunner/brief-generated.md` (random-brief mode) or as the user-supplied `$1` argument.

Dispatch screen-writer with the brief AND the binding sheet at `active-project/staff/showrunner/prompt-binding.md`. Screen-writer reads the binding sheet first. Screen-writer does **not** generate a plan. It maps the concept-space the brief opens — the full range of stories this brief could become INSIDE THE BOUNDS established at Phase 1.4 and the story-type/archetype picks made at Phase 1.5.

**Binding-sheet discipline:**
- Alternative framings must respect the chosen story-type. Framings stay inside the taste-judge's pick.
- Building blocks must respect the archetype picks. The chosen archetypes for each role are decided facts for this expansion, not variables to range over.
- Adjacent concepts and unframed material can range freely over remaining-open parameters; this is where the expansion does its most useful work.

Screen-writer produces three sections:

**1. Alternative framings (4–6)**
Other stories this brief could be telling. Not variations on the obvious reading — genuinely different genre registers, structural emphases, protagonist framings, tonal postures. Each gets one sentence on what changes if the story goes that way.

**2. Building blocks (8–12)**
Themes, tensions, dynamics, structural ingredients available in the material. Raw concepts, not plot beats. "Identity-without-context" not "Jack hides his powers." These are the atoms that can be combined in ways the first-order reading wouldn't reach.

**3. Adjacent concepts**
For each major term or core concept in the brief: 3–5 words or ideas in the same semantic cluster — synonyms, near-synonyms, adjacent registers. These are the handles for shifting the story's tone or emphasis without changing its subject.

Screen-writer writes output to `active-project/staff/showrunner/brief-expansion.md`.

**This is not a planning step and produces no binding decisions.** It is the field the planning draws from. Print:

```
Brief expansion complete. Selecting audience.
```

---

## Phase 1.7 — Audience selection

Read `staff/audience/INDEX.md`. From the **Full personas** table, select 3 personas whose axes best cover the story's subject matter, tone, and genre expectations as revealed by the brief and brief expansion.

**Note:** the audience triad selected here is for plan-review duty (in 1b, 1c, series plan). The taste-judge at Phase 1.5 is a SEPARATE single-persona dispatch loading `staff/audience/taste-judge/card.md` — do not confuse the two roles. The taste-judge picks story-type and archetypes from a menu; the audience triad reviews plans and lines for entertainment and quality.

Selection criteria:
- **Coverage:** the 3 should cover different reader axes. Do not select three momentum-focused or three character-focused personas — variety across axes produces more useful signal.
- **Subject match:** personas tied to specific source material (e.g., `worm-canon-pedant` for Worm) should only be selected if that source material is central to the brief.
- **Tone match:** grimdark material needs a reader who can sit with weight; pulpy material needs a momentum reader; character-driven material needs an interiority reader.
- **Only select full personas.** Stubs (marked as stubs in INDEX.md) require expansion before use. If a stub is clearly the best match and no full persona covers the axis, expand it first using margit, then select it.

After selecting:
1. Create `active-project/audience/<slug>/` directories for the three personas
2. Copy persona card: `staff/audience/<slug>/card.md` → `active-project/audience/<slug>/card.md`
3. Write `active-project/audience/<slug>/memory.md` stub: `# Audience Working Memory — <slug>`
4. Write `active-project/audience/<slug>/stm.md` stub: `# Audience STM — <slug>\nSTM:`

Log the selection to `active-project/staff/showrunner/audience-selection-log.md`:
```
## Audience selection
brief axes: <what subject, tone, and genre dimensions the brief opens>
selected:
  - <slug>: <one line — which axis this covers and why it fits the material>
  - <slug>: <one line — which axis this covers and why it fits the material>
  - <slug>: <one line — which axis this covers and why it fits the material>
rejected: <slugs not selected and one-line reason>
```

Print:
```
Audience selected: <slug-1>, <slug-2>, <slug-3>
Beginning activation planning.
```

---

## Phase 2 — Planning

You orchestrate all planning steps directly. At each step that dispatches a subagent, record the result in the log file for that step before continuing. A missing log file means the step did not run.

**Standing audience memory rule (applies to every audience dispatch in this phase):** Before dispatching audience to review a plan, pass them the path to their STM files (`active-project/audience/<slug>/stm.md`) so they load prior feedback first. After the planning loop for that step concludes (accepted or exhausted), audience writes the session verdicts — which persona accepted/rejected, what the specific feedback was, and whether prior complaints were addressed — to each `active-project/audience/<slug>/stm.md`. A planning step whose audience dispatch did not write to STM has not completed correctly.

---

**1a (internal):** Read `active-project/staff/showrunner/prompt-binding.md` FIRST. This is the canonical contract — boundaries the prompt fixed, parameters the user pinned at the Phase 1.4 checkpoint, and parameters that remain open. Then read `active-project/staff/showrunner/brief-expansion.md` for the concept-space material.

Seed `active-project/staff/showrunner/world-notes.md` directly from the binding sheet:
- Every Boundary becomes a decided constraint (annotate source: `[boundary]`).
- Every Pinned Open Parameter becomes a decided constraint (annotate source: `[pinned at Phase 1.4 checkpoint]`).

Seed `active-project/staff/showrunner/open-questions.md` from the binding sheet's Remaining Open Parameters list (dependency-ordered). Do NOT open OQs for anything already in the boundaries or pinned. Opening an OQ for an already-decided parameter is a contamination bug — it gives the orchestrator a second chance to overwrite a user decision under the guise of "resolving" it.

If the brief expansion suggests a framing that would require contradicting a boundary or pin, do not silently absorb it. Either drop the framing or escalate as a sub-checkpoint to the user. The expansion informs OQ phrasing inside the open-parameters; it does not override the binding sheet.

Proceed immediately to 1b — do not surface these to the human.

---

**1b — Open question resolution.** For each OQ in dependency order:
1. Dispatch screen-writer with: the open question, the full decided constraints from `world-notes.md`, the brief verbatim, and `active-project/staff/showrunner/brief-expansion.md`. Screen-writer proposes 2–3 concrete options, each stated as a decided fact — not a rationale, not a narrative. "The setting is X" not "The setting could be X because Y."
2. Dispatch dramatist and audience in parallel to review screen-writer's options.
3. Record the loop result and decision.
4. Append decision to `world-notes.md`.

**Log file: `active-project/staff/showrunner/1b-log.md`**
Append one block per OQ:
```
## OQ-N: <title> — [RESOLVED | ESCALATED]
screen-writer advocate: <one line — which option and why>
dramatist: <accept/revise> — <one line reason>
audience: <accept/revise> — <one line reason>
attempts: <number>
decision: <what was decided and why>
```

Escalate to the human only if options represent fundamentally incompatible story premises with no basis in the brief for choosing.

---

**1c — Candidate menu and cast selection.**
1. Dispatch margit for candidate menu (personas, locations, conditions).
2. Save the full menu to `active-project/staff/showrunner/1c-candidate-menu.md`.
3. Propose a starter cast and key locations from the menu.
4. Dispatch screen-writer with: the full candidate menu from `1c-candidate-menu.md`, the proposed cast, and the series constraints from `world-notes.md`. Screen-writer reviews for dramatic range — does the cast cover the tension axes the series needs? Dispatch dramatist to check structural viability. Run standard accept/revise loop (3-try max).
5. Have margit provision selected actors into `active-project/actors/` and selected locations into `active-project/warehouse/`. Audience cards copied from `staff/audience/<slug>/card.md` into `active-project/audience/<slug>/card.md`. **Actor dirs must be named by the card's `name` field — the active slug.** For variant cards, the dir name is the variant slug (e.g., card `name: taylor-hebert-westeros` → dir `active-project/actors/taylor-hebert-westeros/`), not the base card slug. Mismatched dir names cause path resolution failures in coach and impersonator dispatches.
6. Populate each actor's `vibes.md`. For each actor: read their card and the series vibe-cloud. If the card contains a `## Vibe Seeds` section, read it — it carries accumulated history and private associations that the vibe-cloud should draw from. Derive their personal vibe-cloud — which world keys does this character activate, and what are their private associations? Write to `active-project/actors/<slug>/vibes.md`. Do not leave stubs. A stub is a silent failure.

   **For characters with defined power or ability mechanics** (a power with usage rules, cost curves, or scope limits): add a vibe key encoding how that power presents in prose — specifically its ambient vs. directed quality, its cost signature, and what it is NOT. Example: a character with an always-on passive sense needs a key like `passive-sense-texture: [always-on-not-active, ambient-not-directed, she-knows-without-choosing-to-know]` to prevent impersonators from writing it as deliberate active surveillance. Without this key, impersonators default to framing powers as deliberate actions with channels, which causes audience mechanics-rejection.

   **For characters arriving from source material with significant audience weight** (a protagonist with a full published story behind them, a canon character whose arc readers know): the vibe-cloud must reflect what they are carrying from that history, not only their situation at story open. Ask: what has this character already done, survived, lost, and done to others before this story begins? That accumulated weight shapes every key they activate. A character who has been through a war does not hold "cost-accounting" the same way a character who has only read about war does. The vibe-cloud must register the difference.
7. Write cast to `series.cast_roster` in `active-project/staff/showrunner/memory.md`.

**Log file: `active-project/staff/showrunner/1c-log.md`**
```
## Cast selection
screen-writer range verdict: <accept/revise> — <one line>
dramatist viability verdict: <accept/revise> — <one line>
attempts: <number>
final cast: <slug list>
rejected candidates: <slug list, one line reason each>
```

---

**1d — World-law finalization.**
1. Dispatch margit to author law/lore/behavior constraint cards. Save to `active-project/warehouse/` AND add to the library: condition-class cards go to `cards/conditions/` and are indexed in `cards/conditions/INDEX.md`. Every card lives in the library as soon as it is authored — the warehouse copy is a working reference, not the primary store.
2. Dispatch auditor (fork) for constraint-consistency check on the full constraint card set.
3. Route any faults to fixer. Fixer writes a session log to `active-project/staff/fixer/fixer-log.md` for every fault resolved — even a one-line entry per fault. A silent fixer run is an incomplete fixer run. Escalate only if unresolvable at this scope.

**Log file: `active-project/staff/auditor/1d-audit.md`**
Auditor saves its full classified report here (schema: `schemas/audit-report.schema.md`). Even a clean pass must produce a report — a clean report proves the check ran.

---

**Series plan.**
1. Build series vibe-cloud. Write to `active-project/staff/studio/vibes.md`.
2. Establish series drama.
3. Dispatch screen-writer with: the world-notes from `world-notes.md`, the series drama statement, the series vibe-cloud, the brief, and `active-project/staff/showrunner/brief-expansion.md`. Screen-writer writes one chunk statement per planned season. **Chunk format: name the collision and what cannot survive it. State what forces are building against each other and what the season's pressure costs or breaks. External and structural — not character psychology. Name stakes and collision shape, not why anyone feels or decides anything. Two sentences maximum. "X's operation grinds through the same ground Y is embedded in before the armies cross" not "X pursues Y because they want Z."** **Do not author season titles.** Seasons are referenced by slug only (`s01`, `s02`...).
4. Dispatch audience and dramatist in parallel to review. Run accept/revise loop (3-try max).
5. Write final series plan to `active-project/staff/showrunner/series-plan.md`. Update `active-project/staff/showrunner/memory.md`: write `series.theme`, `series.laws`, `series.lore`, `series.behaviors`, `series.plot` (start/end/protagonist_arc/series_question), and `series.stage_elements`. Do not write a `title` field on the series or on any season entry.

**Log file: `active-project/staff/showrunner/series-plan-log.md`**
Append one block per attempt:
```
## Attempt N
audience verdict: <accept/revise> — <one line reason>
dramatist verdict: <accept/revise> — <one line reason>

## Final verdict: accepted at attempt N
```

---

**Season 1 plan: REMOVED.** Season planning is owned by `/and-season s01` Phase 1, which auto-fires when no `season-s01-plan.md` exists. /and-project ends at the series-level audit below. `active.season` stays `~` until `/and-season s01` Phase 1 sets it.

---

**Formal series-level audit.**
Dispatch auditor (fork) against the completed series plan.

**Log file: `active-project/staff/auditor/series-audit.md`**
Auditor saves its full classified report here (schema: `schemas/audit-report.schema.md`). Route any faults to fixer before proceeding.

---

**Episode 1 chunk: REMOVED.** Under the emergent-split rule, episode boundaries are not authored at activation. The season is one continuous content-beat list; `/and-season` Phase 4 produces actual episode boundaries (multiple of 3) by interpretive split after the aggregate is authored and reviewed. Activation ends at the series-level audit + season-1 content-beats output. `active.episode` stays `~`; it is set to the new first-episode slug by `/and-season` Phase 5.

---

## Phase 3 — Present results

Present to the human as the activation output — this is the series-level audit checkpoint.

```
--- ACTIVATION COMPLETE ---

SERIES
  Theme: ...
  Question: ...
  Cast: <slug> — role / <slug> — role / ...
  Seasons (slug + chunk; no titles):
    s01 — ...
    s02 — ... (sketch only)
    ...

SEASON 1
  Not authored at activation. /and-season s01 Phase 1 produces the season
  drama, vibe-cloud delta, and content beats; the same command then authors
  the bones and splits into episodes (multiple of 3) by interpretive cut.

LOG FILES
  active-project/staff/showrunner/boundary-scope.md
  active-project/staff/showrunner/prompt-binding.md
  active-project/staff/showrunner/brief-expansion.md
  active-project/staff/showrunner/audience-selection-log.md
  active-project/staff/showrunner/world-notes.md
  active-project/staff/showrunner/open-questions.md
  active-project/staff/showrunner/1b-log.md
  active-project/staff/showrunner/1c-candidate-menu.md
  active-project/staff/showrunner/1c-log.md
  active-project/staff/auditor/1d-audit.md
  active-project/staff/auditor/series-audit.md
  active-project/staff/fixer/fixer-log.md
  active-project/staff/showrunner/series-plan.md
  active-project/staff/showrunner/series-plan-log.md
  active-project/staff/showrunner/memory.md

[Audit checkpoint. Review the above. Reply to proceed to /and-season s01, or give notes for revision.]
```

If there are escalations requiring human decision, present them before the audit checkpoint line with: `ESCALATIONS REQUIRING YOUR DECISION:` followed by each one.

---

## Notes

- Actor working dirs are created by margit in step 1c, not in the scaffold.
- Audience working dirs (including stm.md stubs) are created in the scaffold; margit copies the persona cards into them in step 1c.
- Log files are the audit trail, not the outputs. The human sees summaries; the log files prove execution.
- Season planning is not part of activation. Activation ends at the series-level audit. Human approval at the audit checkpoint triggers `/and-season s01`, whose Phase 1 auto-plans the season (drama + vibe-cloud delta + content beats) before continuing into bone authoring + interpretive split into episodes (multiple of 3).
- No titles are authored at any planning level (series, season, beat, episode). Slugs only.
- **Boundary-scope fork must never run inline.** The fork's isolation is the load-bearing property that prevents the orchestrator from contaminating boundary analysis with its own interpolations. If the main session ever does "let me also think about what's required from the brief" outside the fork, the property is broken and downstream phases will silently carry the contamination. Re-dispatch a fresh fork; never substitute the main session.
- **The prompt-binding sheet is the contract.** Downstream phases read `prompt-binding.md`, not the raw brief. The brief is preserved verbatim inside the binding sheet for traceability; phases consume the synthesized contract. Bypassing the binding sheet to re-read the brief is equivalent to re-litigating Phase 1.4/1.5 silently.
- **Taste-judge persona card.** Phase 1.5 requires `staff/audience/taste-judge/card.md` to exist. This card represents the user's entertainment taste as a single persona; it is pre-installed (not project-scoped) and reused across every /and-project run. If the user wants to redirect what counts as "entertaining," they edit this card — not the /and-project command, not the per-project artifacts. Until this card is authored, Phase 1.5 escalates and the pipeline halts.
