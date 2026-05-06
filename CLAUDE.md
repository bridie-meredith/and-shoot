# and-shoot

Autonomous fiction pipeline. The system authors creative fiction across a series → season → episode hierarchy with minimal human orchestration.

**Human role:** gatekeeper at series-level audit only. Season and episode loops run agent-to-agent with no required human checkpoints unless an audit escalates past season scope.

---

## Primary pattern

```
project activation → season start → (episode start → shoot)* → bulk and-wrap → repeat
```

**Default flow is shoot → shoot → shoot.** /and-wrap is opt-in and typically run in bulk after a stretch of episodes is shot. /and-shoot Phase 0 auto-archives the previous episode's theater files into `theater/<slug>-archive/` so they survive until wrap is called.

- **Project activation** — archive previous active-project, scaffold new one, world-build, plan series and first season, human audit checkpoint, first episode start.
- **Season start** — revisit series plan, establish season drama, plan episodes.
- **Episode start** — screen-writer expands episode chunk into script, audience and dramatist review, shoot begins.
- **Shoot** — showrunner reads bullets, coach translates to prompts, impersonators and studio execute, audience reviews each line. Phase 0 of the next /and-shoot archives this episode's theater files.
- **And-wrap** — opt-in, single or bulk. Dramatist marks scene boundaries and reviews thresholds, audience flags entertainment, auditor reviews constraints, editor produces final draft. Reads from `theater/<slug>-archive/` for already-archived episodes.

---

## Agent routing table

| Agent | Role | Owned by |
|-------|------|----------|
| showrunner | Memory holder. Reads/writes series memory and state files. Does NOT orchestrate — command bodies do. No Agent tool. | `staff/showrunner/` |
| screen-writer | Plan generator. Series/season/episode bullet plans. | `staff/screen-writer/` |
| coach | Prompt translator. Bullet → impersonator prompt. | `staff/coach/` |
| impersonator | Character primitive. One per active actor per episode. | spawned per-actor |
| studio | Set and environment manager. Records all state changes. | `staff/studio/` |
| audience | Critic config. 3 persona cards. Reviews lines and plans. | `active-project/audience/` |
| dramatist | Structural critic. Plans and wrap review. | stateless |
| auditor | Fault-finder. Constraint/state/drift audit. Returns report. | `staff/auditor/` |
| fixer | Targeted correction. Meets auditor criteria with minimum change. | `staff/fixer/` |
| margit | Card warehouse. Stores, indexes, validates, promotes. | `staff/margit/` |
| editor | Final draft. Wrap only. Scene cuts, prose pass, continuity. | `staff/editor/` |

---

## Directory map

```
schemas/          — schema authority (read this before writing any new file format)

staff/            — production staff: agent homes + audience persona library
  showrunner/     — agent home: card.md + ltm.md + stm.md
  margit/         — agent home
  coach/          — agent home
  screen-writer/  — agent home
  studio/         — agent home
  auditor/        — agent home
  fixer/          — agent home
  editor/         — agent home
  audience/       — audience persona library (18 personas; INDEX.md; 3 selected per project)

cards/            — story-facing card library (on-stage characters, locations, props, conditions, behaviors)
  personas/       — on-stage character cards (flat; INDEX.md for lookup by world/quality/trope/OC)
  locations/      — location cards (flat; INDEX.md)
  props/          — prop cards (flat; INDEX.md)
  conditions/     — condition cards (flat; INDEX.md)
  dialects/       — behavior cards (class: behavior — voice + non-verbal tics + memory monuments; flat; INDEX.md). Directory rename to behaviors/ pending.

active-project/   — sole active project
  actors/         — active cast (persona card + ltm/stm/state/vibes per actor)
  warehouse/      — active locations, props, conditions
  audience/       — 3 active audience persona working dirs
  staff/          — showrunner/studio/auditor/fixer/margit working memory
  theater/        — episode-plan.md + show.md (current episode)
  polish/         — closed manuscripts

projects/         — completed series archive
```

---

## Schema authority

All file formats are defined in `schemas/`. Read the relevant schema before creating any new schema-typed file.

| File type | Schema |
|-----------|--------|
| Cards | `schemas/card.schema.md` |
| Actor memory (LTM/STM/state/vibes) | `schemas/memory.schema.md` |
| Showrunner memory | `schemas/showrunner-memory.schema.md` |
| Episode plan | `schemas/episode-plan.schema.md` |
| Show file | `schemas/show-file.format.md` |
| Audit report | `schemas/audit-report.schema.md` |
| Per-character dialogue file (shoot-v2) | `schemas/dialogue.schema.md` |
| Proto-line file (shoot-v2) | `schemas/proto-line.schema.md` |
| Facet file (shoot-v2) | `schemas/facet.schema.md` |

---

## Memory rules

**Nothing changes without being recorded.** If an actor moved, their state file records it. If a prop changed hands, studio's state file records it. If a change is not in a state file, it did not happen.

**Showrunner memory is cross-session.** `active-project/staff/showrunner/memory.md` is read at every session open. It is the fast path to reconstructing full working context without scanning history.

**Actor memory lives in active-project.** At project close, the active-project directory is archived to `projects/<title>/`. Actor memory travels with it.

**Vibe-clouds are built at each planning level.** Series, season, and episode each have a vibe-cloud. All three are active during shoot; episode-level takes priority on key conflicts. Agents check vibes before generating output; vibes bias but do not override constraints.

---

## Rules

1. Read the relevant schema before writing any new schema-typed file.
2. Command bodies (`/and-project`, `/and-shoot`, `/and-wrap`) are the orchestrators. They dispatch sub-agents directly. Showrunner does NOT orchestrate and does NOT have the Agent tool — it is a memory holder only. Cascading dispatch through showrunner is the inline-simulation failure mode and is structurally prevented.
3. Coach is the sole translator of bullets into prompts. The command body does not write impersonator prompts directly.
4. Nothing moves without being recorded (state rule — absolute).
5. The show file is append-only during shoot. Rejected lines are deleted before retry. Failed lines (budget exhausted) are marked [NEEDS_EDIT:] and left.
6. Audience membership is defined at project activation. It does not change mid-episode.
7. Human checkpoints: series-level audit only. Everything else is agent-resolved unless an escalation requires human decision.
8. Card schema authority is `schemas/card.schema.md`. Margit validates against it. No card class outside the five defined (persona, location, prop, condition, behavior).
9. All agent dispatches use the Agent tool. Inline generation is not a substitute for a dispatch — an agent that is not spawned in isolation does not have the context isolation the pipeline depends on.

---

## Commands

Project-local slash commands in `.claude/commands/`.

| Command | Purpose |
|---------|---------|
| `/and-project <title-slug> "<brief>" <audience-1> <audience-2> <audience-3>` | Full project activation. Scaffolds `active-project/`, then dispatches showrunner to run world-building (1a–1d), series plan, season 1 plan, and episode 1 chunk. Presents output at the series-level audit checkpoint for human review. |

---

## Not in scope

- Gacha system — deferred
- Workshop-artifact card class — excluded
