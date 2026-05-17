---
description: Activate a new and-shoot project. Scaffolds active-project/, binds staff personas + audience trio + orchestrator-critic version, runs boundary-scope + taste-judge forks, runs world-building (1a–1d), and presents output for human audit. Series chunk + structural prompts owned by /and-series; substance signature by /and-substance series; cast + series-level audit by /and-cast. Brief may be empty — Phase 1.5 generates one if omitted. Usage - /and-project <title-slug> ["<brief>"] <audience-1> <audience-2> <audience-3> [--screen-writer <slug>] [--dramatist <slug>] [--auditor <slug>] [--editor <slug>] [--orchestrator-critic <version>]
---

Project activation under the substance overhaul. Three jobs: scaffold, project scope (world-building), staff binding.

You are the orchestrator for this command. You dispatch subagents directly — screen-writer, margit, dramatist, audience, auditor, fixer. Do not dispatch showrunner; showrunner is read-mostly memory.

**All dispatches use the Agent tool.** Inline generation is not a valid substitute.

This command **cannot be re-run**. Phase 0 hard-aborts if `active-project/staff/showrunner/memory.md` exists with `project.brief` populated. To redo a project, archive `active-project/` and start over.

## Args

Three positional + three positional audience slugs + five optional staff override flags:

```
/and-project <title-slug> "<brief>" <audience-1> <audience-2> <audience-3>
             [--screen-writer <persona-slug>]
             [--dramatist <persona-slug>]
             [--auditor <persona-slug>]
             [--editor <persona-slug>]
             [--orchestrator-critic <card-version>]
```

- `$1` (title-slug) — required. Short kebab-case identifier (e.g. `flea-bottom-dance`). Used as the directory name under `projects/` when the project closes.
- `$2` (brief) — optional. The user's elevator-pitch brief in quotes (subject + setting + central tension). If empty, Phase 1.5 (random-brief generation) generates one before any analytical work begins.
- `$3 $4 $5` (audience slugs) — required, exactly three. Pick from `staff/audience/INDEX.md`. Audience reviews every chunk and chapter for substance-felt; pick three that read differently for blind-spot coverage.
- `--screen-writer <slug>` (optional) — override the library-default screen-writer persona.
- `--dramatist <slug>` (optional) — override the library-default dramatist persona.
- `--auditor <slug>` (optional) — override the library-default auditor persona.
- `--editor <slug>` (optional) — override the library-default editor persona (library-only under polish-deferred chain; bound for revival).
- `--orchestrator-critic <version>` (optional) — pin a specific `staff/orchestrator-critic/card.md` version string (e.g. `v3`).

---

## Phase 0 — Validate

1. Confirm `$1`, `$3`, `$4`, `$5` are present. (`$2` is optional — if empty, random-brief mode is triggered at Phase 1.5.) If any required arg is missing, print usage and exit.
2. Confirm `$1` (title-slug) is kebab-case (`^[a-z0-9]+(-[a-z0-9]+)*$`). Reject otherwise.
3. Confirm each audience slug exists at `staff/audience/<slug>/card.md`. Reject any missing slug.
4. If `active-project/staff/showrunner/memory.md` exists and contains a non-null `project.brief`, **HARD-ABORT** with: `/and-project cannot re-run. Archive active-project/ to projects/<title>/ and start over.`

---

## Phase 1 — Scaffold

Execute mechanically. Do not delegate. Complete before proceeding to Phase 2.

### 1. Shelve previous active-project

If `active-project/` exists and contains content beyond empty stub files:
1. Determine next serial: list `projects/` for existing `project_NN` directories, take the highest N, increment. First project shelves to `projects/project_01/`.
2. Move `active-project/` to `projects/project_NN/`.
3. Print: `Shelved previous project → projects/project_NN/`

If `active-project/` does not exist or is empty, skip this step.

### 2. Create directory tree

```bash
mkdir -p active-project/actors
mkdir -p active-project/warehouse
mkdir -p active-project/audience/<aud-1>
mkdir -p active-project/audience/<aud-2>
mkdir -p active-project/audience/<aud-3>
mkdir -p active-project/staff/showrunner
mkdir -p active-project/staff/studio
mkdir -p active-project/staff/auditor
mkdir -p active-project/staff/fixer
mkdir -p active-project/staff/margit
mkdir -p active-project/staff/screen-writer
mkdir -p active-project/staff/editor
mkdir -p active-project/staff/reviews
mkdir -p active-project/theater/bones
mkdir -p active-project/theater/facets
mkdir -p active-project/theater/dialogue
mkdir -p active-project/draft
mkdir -p active-project/polish
```

### 3. Write stub files

**`active-project/staff/showrunner/memory.md`** — initialize per `schemas/showrunner-memory.schema.md`:

```yaml
# showrunner memory — schema: schemas/showrunner-memory.schema.md

project:
  brief: <verbatim $2>
  constraints:
    settings: []
    themes_as_bounds: []
    hard_fences: []
  staff:
    audience: [<aud-1>, <aud-2>, <aud-3>]
    screen_writer: <--screen-writer or library default>
    dramatist: <--dramatist or library default>
    auditor: <--auditor or library default>
    editor: <--editor or library default>
    orchestrator_critic: <--orchestrator-critic or library default version>
  series_audit:
    approved_at: ~
    approved_by: ~
    report_path: ~
    stale_since: ~

series:
  chunk: ~
  structure:
    book_count: ~
    book_length:
      chapters_per_book: ~
      scenes_per_chapter: ~
      bones_per_scene: ~
    cyclical: ~
    pov: ~
    cross_book_continuity:
      recurring_antagonists: []
      ongoing_subplots: []
    world_evolution: ~
    series_end_shape: ~
  laws: []
  lore: []
  behaviors: []
  substance: ~
  vibe_cloud:
    keys: []
  cast_roster: []
  stage_elements: []

books: []

active:
  book: ~
  chapter: ~
  cascade_in_progress: false

routing:
  series_plan: active-project/staff/showrunner/series-plan.md
  staleness_log: active-project/staff/showrunner/staleness-log.md
  cascade_checkpoint: active-project/staff/showrunner/cascade-checkpoint.md
  reviews: active-project/staff/reviews/
  bones_dir: active-project/theater/bones/
  facets_dir: active-project/theater/facets/
  dialogue_dir: active-project/theater/dialogue/
  draft_dir: active-project/draft/
```

**`active-project/staff/showrunner/series-plan.md`** — `# Series Plan — detail companion to memory.md`

**`active-project/staff/showrunner/world-notes.md`** — `# World Notes — Decided Constraints`

**`active-project/staff/showrunner/open-questions.md`** — `# Open Questions`

**`active-project/staff/showrunner/staleness-log.md`** — `# Staleness log — one entry per cascade event`

**`active-project/staff/showrunner/cascade-checkpoint.md`** — empty (written by `/and-substance --cascade` when invoked).

**`active-project/staff/studio/{ltm,stm,state,vibes}.md`** — schema-conformant stubs as in `schemas/memory.schema.md`.

**`active-project/staff/margit/margit.memory.md`** — `# Margit Working Memory`

**Audience working dirs.** For each of the three audience slugs:
1. Copy `staff/audience/<slug>/card.md` → `active-project/audience/<slug>/card.md`.
2. Write `active-project/audience/<slug>/memory.md` stub: `# Audience Working Memory — <slug>`.
3. Write `active-project/audience/<slug>/stm.md` stub: `# Audience STM — <slug>\nSTM:`.

### 4. Confirm card library

Verify `cards/personas/INDEX.md`, `cards/locations/INDEX.md`, `cards/conditions/INDEX.md` exist. Print line counts.

Print:
```
Scaffold complete. Running brief-stage gates.
```

---

## Phase 1.5 — Random-brief generation (conditional)

If `$2` was provided, skip this phase entirely and proceed to Phase 1.7.

If `$2` was empty: dispatch screen-writer with no constraints. Screen-writer reads `staff/audience/INDEX.md` and `cards/` to get a sense of available material, then proposes any premise — any genre, any source world, any structural register. Output written to `active-project/staff/showrunner/brief-generated.md`. From this point forward, the generated brief is the brief — Phase 1.7, Phase 1.8, Phase 2, and all downstream phases use it identically to a user-supplied brief.

Brief generation runs **before** boundary scope because boundary scope requires a brief to scope.

Print:
```
Brief generated. Running boundary scope.
```

If `$2` was provided and this phase was skipped, print before Phase 1.7:
```
Running boundary scope.
```

---

## Phase 1.7 — Boundary scoping (fork; isolated)

This phase exists to surface the load-bearing decisions implicit in the brief BEFORE any editorial work begins. It runs as an isolated fork — never inline. The fork writes its report and the pipeline continues; the user is not asked to select anything at this phase. Selection happens at Phase 1.8 via the taste-judge dispatch.

**Critical rule: NEVER INLINE.** All boundary analysis happens inside the fork. If the main session ever does its own boundary analysis (e.g., "let me also think about what's required..."), the isolation property is broken and downstream decisions will silently carry the contamination.

### 1. Dispatch the fork

Use the Agent tool with `subagent_type: general-purpose`. The fork's prompt MUST:

- Pass the user's brief VERBATIM (no paraphrase, no compression). Read from `$2` if provided, or from `active-project/staff/showrunner/brief-generated.md` if Phase 1.5 generated one.
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

Main session reads `boundary-scope.md` for handoff to Phase 1.8. **Do not re-analyze, re-rank, or compress.** Do not pick from the menus. Do not present anything to the user. Compression and pre-selection by the orchestrator are both contamination vectors — the taste-judge at Phase 1.8 sees the fork's report as the fork produced it.

### 3. Print phase-complete

```
Boundary scope written. Dispatching taste-judge.
```

---

## Phase 1.8 — Taste selection (taste-judge fork; isolated)

The taste-judge picks story-type and archetypes from the menus the boundary-scope fork produced. The user does not pick — a single stand-in agent picks based on entertainment fit. This is the design decision that keeps the pipeline moving without forcing the user to choose between equally-valid framings, while still surfacing those framings (via `boundary-scope.md`) for review at the `/and-cast` Phase 5 series-level audit if the user wants to redirect.

**Critical rule: SINGLE AGENT, ISOLATED FORK.** The taste-judge is one audience/critic fork loaded with one persona card — the user-stand-in card. The audience class is the right dispatch because the critic already does what's needed with a persona card: load it, read the input, return a verdict (here: menu picks + per-pick reason). Single-card config, not the project's standing 3-persona audience triad — the triad is bound at Phase 1 from `$3 $4 $5` and reviews plans/chunks/lines downstream. Not an inline main-session decision (that defeats the purpose — main session interpolation is what Phase 1.7 was added to prevent).

### 1. Locate the taste-judge persona card

The user-stand-in persona card lives at `staff/audience/taste-judge/card.md`. It is pre-installed (not project-scoped) and represents the user's entertainment taste as a single persona. If absent, halt Phase 1.8 and escalate to the user with: "Taste-judge persona card not found. Author `staff/audience/taste-judge/card.md` representing your entertainment taste, then re-run /and-project from Phase 1.8."

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
# Prompt Binding Sheet — generated at Phase 1.8
# This is the canonical input for all downstream phases.

## Original prompt (verbatim)
<the user's brief as supplied, character-for-character — or the random-brief from brief-generated.md if Phase 1.5 ran>

## Boundaries (fixed by prompt — verbatim from boundary-scope.md §1)
<copied verbatim from the fork's report>

## Story-type (taste-judge pick at Phase 1.8)
<chosen-name>
reason: <one-sentence reason from taste-selection.md>

## Archetype picks per role (taste-judge picks at Phase 1.8)
- <role>: <pick> — <reason>
- <role>: <pick> — <reason>
...

## Pinned open parameters
(none at Phase 1.8; pinning is reserved for user override at the /and-cast Phase 5 audit checkpoint)

## Remaining open parameters
- <name>
- <name>
...
```

The binding sheet is the operative contract for everything downstream. Phase 2 brief-expansion reads it. 1a reads it. 1b loops only on remaining-open parameters that need OQs. 1d/series chunk/cast all consume it.

### 6. Print phase-complete

```
Taste selection written. Binding sheet written.
Running brief expansion within the confirmed bounds.
```

---

## Phase 2 — Project scope (world-building)

### 2.1 — Brief expansion (screen-writer fork)

Dispatch screen-writer with the brief AND the binding sheet at `active-project/staff/showrunner/prompt-binding.md`. Screen-writer reads the binding sheet first. Screen-writer does NOT generate a plan. It maps the concept-space the brief opens — the full range of stories this brief could become INSIDE THE BOUNDS established at Phase 1.7 and the story-type/archetype picks made at Phase 1.8.

**Binding-sheet discipline:**
- Alternative framings must respect the chosen story-type. Framings stay inside the taste-judge's pick.
- Building blocks must respect the archetype picks. The chosen archetypes for each role are decided facts for this expansion, not variables to range over.
- Adjacent concepts and unframed material can range freely over remaining-open parameters; this is where the expansion does its most useful work.

Screen-writer produces three sections, written to `active-project/staff/showrunner/brief-expansion.md`:

**1. Alternative framings (4–6).** Other stories this brief could be telling. Each gets one sentence on what changes if the story goes that way.

**2. Building blocks (8–12).** Themes, tensions, dynamics, structural ingredients in the material. Raw concepts.

**3. Adjacent concepts.** For each major term in the brief: 3–5 words in the same semantic cluster.

This is not a planning step. It is the field planning draws from.

### 2.2 — Brief expansion follow-up questions (3–5 prompts; user-interactive)

After the brief expansion lands, ask the user 3–5 follow-up questions about the world-frame. Surface decisions that will save continuity revisions later. Examples (calibrate to the brief):
- Currency: what coin system? What buys a loaf, what buys a house?
- Class structure: how many strata? What's the local class language?
- Geography: where does this take place? What are the proximate places?
- Hard fences: any out-of-world fences (e.g. proper-noun bans for crossover stories)?
- Tone bounds: any tonal commitments the world enforces (no comic relief / always-comic / fairytale-stasis)?

User answers route to `project.constraints.{settings, themes_as_bounds, hard_fences}` in memory.

### 2.3 — Step 1a: Decided constraints + open questions (internal)

Read the brief verbatim + the brief expansion + user answers from 2.2. Write decided constraints to `world-notes.md`. Write open questions (dependency-ordered) to `open-questions.md`. Proceed immediately to 2.4 — do not surface to user.

### 2.4 — Step 1b: Open question resolution

For each OQ in dependency order:
1. Dispatch screen-writer with: the OQ, full decided constraints from `world-notes.md`, the brief verbatim, and `brief-expansion.md`. Screen-writer proposes 2–3 concrete options, each stated as a decided fact.
2. Dispatch dramatist and audience in parallel to review.
3. Record loop result and decision in `staff/showrunner/1b-log.md`.
4. Append decision to `world-notes.md`.

Escalate to user only if options represent fundamentally incompatible story premises with no basis in the brief for choosing.

### 2.5 — Step 1d: World-law finalization

1. Dispatch margit to author law / lore / behavior constraint cards. Save to `active-project/warehouse/` AND add to the library (`cards/conditions/`). Every card lives in the library; the warehouse copy is a working reference.
2. Dispatch auditor (fork) for constraint-consistency check on the full constraint card set.
3. Route any faults to fixer. Fixer writes to `active-project/staff/fixer/fixer-log.md` per fault.

Auditor saves full classified report to `active-project/staff/auditor/1d-audit.md` per `schemas/audit-report.schema.md`.

After 1d completes, write `project.constraints.{settings, themes_as_bounds, hard_fences}` (extended from 2.2) + `series.laws`, `series.lore`, `series.behaviors` to showrunner memory.

---

## Phase 3 — Staff binding

Audience slugs already wired in Phase 1 step 3. Non-audience staff:
- Each of `screen_writer`, `dramatist`, `auditor`, `editor` resolves to the override flag value if provided, else the library default.
- `orchestrator_critic` resolves to the override flag value if provided, else the library default version.

Confirm each non-audience persona slug exists at `staff/<role>/card.md` (or for audience-library overrides, at `staff/audience/<slug>/card.md`).

Write final `project.staff.*` block to showrunner memory.

---

## Phase 4 — Present activation output

This is the project-scope-approval checkpoint. The full series-level audit checkpoint is owned by `/and-cast` Phase 5 — `/and-project` only presents the scope + staff binding.

```
--- /and-project COMPLETE: <title-slug> ---

PROJECT
  Brief: <one-line distill of the brief>
  Constraints:
    Settings: <comma-list>
    Themes-as-bounds: <comma-list>
    Hard fences: <comma-list>
  Laws: <N> condition cards in cards/conditions/

STAFF
  Audience trio: <aud-1>, <aud-2>, <aud-3>
  Screen-writer: <slug or library default>
  Dramatist: <slug or library default>
  Auditor: <slug or library default>
  Editor: <slug or library default>  [library-only under polish-deferred chain]
  Orchestrator-critic: <version>

LOG FILES
  active-project/staff/showrunner/brief-generated.md (if Phase 1.5 ran)
  active-project/staff/showrunner/boundary-scope.md
  active-project/staff/showrunner/taste-selection.md
  active-project/staff/showrunner/prompt-binding.md
  active-project/staff/showrunner/brief-expansion.md
  active-project/staff/showrunner/world-notes.md
  active-project/staff/showrunner/open-questions.md
  active-project/staff/showrunner/1b-log.md
  active-project/staff/auditor/1d-audit.md
  active-project/staff/fixer/fixer-log.md (if any faults routed)

next: /and-series
```

If there are escalations requiring user decision, present them before the `next:` line under `ESCALATIONS REQUIRING YOUR DECISION:`.

---

## Notes

- Cast roster, series chunk, structural prompts, substance signature, and the series-level audit are NOT in `/and-project`. The next command is `/and-series`.
- Actor working dirs are NOT created here; margit provisions them in `/and-cast` Phase 4.
- This command does not author titles at any level — slugs only.
- `/and-project` is the only non-re-runnable command.
