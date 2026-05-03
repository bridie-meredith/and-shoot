---
description: Activate a new and-shoot project. Scaffolds active-project/, runs world-building and planning (steps 1a–1d, series plan, season 1 plan, episode 1 chunk), and presents output for human audit. Usage: /and-project <project-title-slug> "<brief>" <audience-slug-1> <audience-slug-2> <audience-slug-3>
---

Full project activation for the and-shoot pipeline. Two phases: scaffold (mechanical, direct), then planning (dispatched to showrunner subagent). Human sees the planning output at the end — not the deliberation that produced it.

## Args

- `$1` — project title slug (lowercase-hyphenated). Required.
- `$2` — the human brief, quoted as a single string. Everything the human said about the project: source world, destination world, characters, constraints, tone, anything. Pass verbatim — showrunner reads it in step 1a.
- `$3 $4 $5` — the three audience persona slugs. Must exist as directories under `staff/audience/`. Audience membership is fixed at activation and does not change.

All five arguments are required. If any are missing or any audience slug does not exist as a directory under `staff/audience/`, print:

```
Usage: /and-project <title-slug> "<brief>" <audience-slug-1> <audience-slug-2> <audience-slug-3>
Invalid: <list any missing or unrecognized args>
```

Stop. Do not proceed with a partial configuration.

---

## Phase 1 — Scaffold

Execute mechanically. Do not delegate. Complete before dispatching showrunner.

### 1. Validate

Verify $1 is provided and is a valid slug (lowercase, hyphens only). Verify each of $3/$4/$5 exists as a directory under `staff/audience/`. Fail with usage message if anything is missing or invalid.

### 2. Create directory tree

Do not archive or move any existing active-project directory.

```bash
mkdir -p active-project/actors
mkdir -p active-project/hopefuls
mkdir -p active-project/warehouse
mkdir -p active-project/audience/<audience-slug-1>
mkdir -p active-project/audience/<audience-slug-2>
mkdir -p active-project/audience/<audience-slug-3>
mkdir -p active-project/staff/showrunner
mkdir -p active-project/staff/studio
mkdir -p active-project/staff/auditor
mkdir -p active-project/staff/fixer
mkdir -p active-project/staff/margit
mkdir -p active-project/staff/editor
mkdir -p active-project/theater
mkdir -p active-project/polish
```

### 3. Write stub files

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
# Internal. Written by showrunner in step 1a. One constraint per line. Law/Lore/Behavior prefix where applicable.
```

**`active-project/staff/showrunner/open-questions.md`**
```
# Open Questions
# Internal. Written by showrunner in step 1a. Ordered by dependency. Each resolved OQ moves to world-notes.md.
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

**`active-project/audience/<slug>/memory.md`** — one per audience persona:
```
# Audience Working Memory — <slug>
```

**`active-project/audience/<slug>/stm.md`** — one per audience persona:
```
# Audience STM — <slug>
STM:
```

### 4. Confirm card library

Verify `cards/personas/INDEX.md` and `cards/locations/INDEX.md` exist. Print line counts.

### 5. Print scaffold complete

```
Scaffold complete. Running brief expansion.
```

---

## Phase 1.5 — Brief expansion

Dispatch screen-writer with the brief verbatim. Screen-writer does **not** generate a plan. It maps the concept-space the brief opens — the full range of stories this brief could become before any direction is chosen.

Screen-writer produces three sections:

**1. Alternative framings (4–6)**
Other stories this brief could be telling. Not variations on the obvious reading — genuinely different genre registers, structural emphases, protagonist framings, tonal postures. Each gets one sentence on what changes if the story goes that way.

**2. Building blocks (8–12)**
Themes, tensions, dynamics, structural ingredients available in the material. Raw concepts, not plot beats. "Identity-without-context" not "Jack hides his powers." These are the atoms showrunner can combine in ways the first-order reading wouldn't reach.

**3. Adjacent concepts**
For each major term or core concept in the brief: 3–5 words or ideas in the same semantic cluster — synonyms, near-synonyms, adjacent registers. These are the handles for shifting the story's tone or emphasis without changing its subject.

Screen-writer writes output to `active-project/staff/showrunner/brief-expansion.md`.

**This is not a planning step and produces no binding decisions.** It is the field the planning draws from. Print:

```
Brief expansion complete. Dispatching showrunner for activation.
```

---

## Phase 2 — Planning

Dispatch showrunner as a subagent. Pass the brief and the locked configuration. Showrunner runs the full activation pattern agent-to-agent with no further input from this command.

**Prompt to showrunner:**

> Read `active-project/staff/showrunner/memory.md` before proceeding. That is your working state.
>
> You are activating a new project. The scaffold is complete. Audience is locked: `<audience-slug-1>`, `<audience-slug-2>`, `<audience-slug-3>`.
>
> The brief:
> `<brief verbatim>`
>
> Run project activation steps 1a through first season planning. At each step that dispatches a subagent, **record the subagent's verdict in the log file for that step** before continuing. Details below.
>
> **Standing audience memory rule (applies to every audience dispatch in this activation):** Before dispatching audience to review a plan, pass them the path to their STM files (`active-project/audience/<slug>/stm.md`) so they load prior feedback first. After the planning loop for that step concludes (accepted or exhausted), audience writes the session verdicts — which persona accepted/rejected, what the specific feedback was, and whether prior complaints were addressed — to each `active-project/audience/<slug>/stm.md`. This is what makes their feedback persistent across iterations. A planning step whose audience dispatch did not write to STM has not completed correctly.
>
> ---
>
> **1a (internal):** Read the brief. Read `active-project/staff/showrunner/brief-expansion.md` — this is the concept-space the brief opens. Before writing constraints and open questions, ask: does your first instinct cover the full space, or only the first-order reading? The expansion is not binding — it is a check. If a building block or alternative framing is more interesting than the obvious direction, let it shape what you extract. Write decided constraints to `active-project/staff/showrunner/world-notes.md`. Write open questions (dependency-ordered) to `active-project/staff/showrunner/open-questions.md`. Do not surface these to the caller — proceed immediately to 1b.
>
> ---
>
> **1b — Open question resolution.** For each OQ in dependency order:
> 1. Dispatch screen-writer with: the open question, the full decided constraints from `world-notes.md`, the brief verbatim, and `active-project/staff/showrunner/brief-expansion.md`. Screen-writer proposes 2–3 concrete options, each stated as a decided fact — not a rationale, not a narrative. "The setting is X" not "The setting could be X because Y."
> 2. Dispatch dramatist and audience in parallel to review screen-writer's options.
> 3. Record the loop result and decision.
> 4. Append decision to `world-notes.md`.
>
> **Log file: `active-project/staff/showrunner/1b-log.md`**
> Append one block per OQ:
> ```
> ## OQ-N: <title> — [RESOLVED | ESCALATED]
> screen-writer advocate: <one line — which option and why>
> dramatist: <accept/revise> — <one line reason>
> audience: <accept/revise> — <one line reason>
> attempts: <number>
> decision: <what was decided and why>
> ```
>
> Escalate to caller only if options represent fundamentally incompatible story premises with no basis in the brief for choosing.
>
> ---
>
> **1c — Candidate menu and cast selection.**
> 1. Dispatch margit for candidate menu (personas, locations, conditions).
> 2. Save the full menu to `active-project/staff/showrunner/1c-candidate-menu.md`.
> 3. Propose a starter cast and key locations from the menu.
> 4. Dispatch screen-writer with: the full candidate menu from `1c-candidate-menu.md`, the proposed cast, and the series constraints from `world-notes.md`. Screen-writer reviews for dramatic range — does the cast cover the tension axes the series needs? Dispatch dramatist to check structural viability. Run standard accept/revise loop (3-try max).
> 5. Have margit provision selected actors into `active-project/actors/` and selected locations into `active-project/warehouse/`. Audience cards copied from `staff/audience/<slug>/card.md` into `active-project/audience/<slug>/card.md`.
> 6. Populate each actor's `vibes.md`. For each actor: read their card and the series vibe-cloud. Derive their personal vibe-cloud — which world keys does this character activate, and what are their private associations? Write to `active-project/actors/<slug>/vibes.md`. Do not leave stubs. A stub is a silent failure.
> 7. Write cast to `series.cast_roster` in `active-project/staff/showrunner/memory.md`.
>
> **Log file: `active-project/staff/showrunner/1c-log.md`**
> ```
> ## Cast selection
> screen-writer range verdict: <accept/revise> — <one line>
> dramatist viability verdict: <accept/revise> — <one line>
> attempts: <number>
> final cast: <slug list>
> rejected candidates: <slug list, one line reason each>
> ```
>
> ---
>
> **1d — World-law finalization.**
> 1. Dispatch margit to author law/lore/behavior constraint cards. Save to `active-project/warehouse/`.
> 2. Dispatch auditor (fork) for constraint-consistency check on the full constraint card set.
> 3. Route any faults to fixer. Escalate only if unresolvable at this scope.
>
> **Log file: `active-project/staff/auditor/1d-audit.md`**
> Auditor saves its full classified report here (schema: `schemas/audit-report.schema.md`). Even a clean pass must produce a report — a clean report proves the check ran.
>
> ---
>
> **Series plan.**
> 1. Build series vibe-cloud. Write to `active-project/staff/studio/vibes.md`.
> 2. Establish series drama.
> 3. Dispatch screen-writer with: the world-notes from `world-notes.md`, the series drama statement, the series vibe-cloud, the brief, and `active-project/staff/showrunner/brief-expansion.md`. Screen-writer writes one chunk statement per planned season. **Chunk format: external observable state-change — what a witness could report happening across that season. No motivation or causation embedded. "X and Y collide at Z" not "X pursues Y because they want Z."**
> 4. Dispatch audience and dramatist in parallel to review. Run accept/revise loop (3-try max).
> 5. Write final series plan to `active-project/staff/showrunner/series-plan.md`. Update `active-project/staff/showrunner/memory.md`: write `series.theme`, `series.laws`, `series.lore`, `series.behaviors`, `series.plot` (start/end/protagonist_arc/series_question), and `series.stage_elements`.
>
> **Log file: `active-project/staff/showrunner/series-plan-log.md`**
> Append one block per attempt:
> ```
> ## Attempt N
> audience verdict: <accept/revise> — <one line reason>
> dramatist verdict: <accept/revise> — <one line reason>
>
> ## Final verdict: accepted at attempt N
> ```
>
> ---
>
> **Season 1 plan.**
> 1. Derive season vibe-cloud. Note deltas from series vibe-cloud. Append season section to `active-project/staff/studio/vibes.md`.
> 2. Establish season drama.
> 3. Dispatch screen-writer with: the series plan from `series-plan.md`, the season drama statement, the series and season vibe-clouds, the series constraints from memory, and `active-project/staff/showrunner/brief-expansion.md`. Screen-writer writes one chunk statement per episode. **Chunk format: external observable event, concrete and specific. No motivation or causation embedded. "X freezes the doorway and gets on the road" not "X runs because they fear being caught."**
> 4. Dispatch audience and dramatist in parallel to review. Run accept/revise loop (3-try max).
> 5. Write season plan to `active-project/staff/showrunner/season-s01-plan.md`. Update `active-project/staff/showrunner/memory.md`: set `routing.season_plan: active-project/staff/showrunner/season-s01-plan.md`; add the season to the `seasons` array with `status: active` and all episode slugs with `status: planned`; set `active.season: s01`.
>
> **Log file: `active-project/staff/showrunner/season-s01-plan-log.md`**
> Same format as series-plan-log.md.
>
> ---
>
> **Formal series-level audit.**
> Dispatch auditor (fork) against the completed series plan and season 1 plan.
>
> **Log file: `active-project/staff/auditor/series-audit.md`**
> Auditor saves its full classified report here (schema: `schemas/audit-report.schema.md`). Route any faults to fixer before returning.
>
> ---
>
> **Episode 1 chunk:** Take the episode 1 chunk statement from the season plan. Do not expand it to shoot-level bullets — that is episode start, not activation. The chunk statement is the output.
>
> ---
>
> **Return to caller (concise — no transcripts, no deliberation):**
> - Series: theme, series_question, season chunk statements (one line each)
> - Season 1: drama statement, episode chunk statements (one line each), key cast (slug + one-line role)
> - Episode 1: chunk statement only
> - Any escalations that require human decision
> - Log files written (list of paths)

### On return

Take showrunner's return. Present it to the human as the activation output — this is the series-level audit checkpoint.

Format for human:

```
--- ACTIVATION COMPLETE: <title-slug> ---

SERIES
  Theme: ...
  Question: ...
  Seasons:
    S01 — ...
    S02 — ... (sketch only)
    ...

SEASON 1
  Drama: ...
  Cast: <slug> — role / <slug> — role / ...
  Episodes:
    E01 — ...
    E02 — ...
    ...

EPISODE 1 (chunk — not yet expanded for shoot)
  ...

LOG FILES
  active-project/staff/showrunner/brief-expansion.md
  ...

[Audit checkpoint. Review the above. Reply to proceed to episode start, or give notes for revision.]
```

If showrunner returned escalations, present them before the audit checkpoint line with: `ESCALATIONS REQUIRING YOUR DECISION:` followed by each one.

---

## Notes

- Actor working dirs are created by margit in step 1c, not in the scaffold.
- Audience working dirs (including stm.md stubs) are created in the scaffold; margit copies the persona cards into them in step 1c.
- Log files are the audit trail, not the outputs. The human sees summaries; the log files prove execution.
- The episode 1 chunk is an output of season planning, not a new planning act. Episode start (which expands it to shoot-level bullets) is triggered by human approval at the audit checkpoint.
- Showrunner must read `active-project/staff/showrunner/memory.md` at the top of the dispatch. The dispatch prompt opens with this instruction.
