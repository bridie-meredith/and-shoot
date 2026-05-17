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
- **And-wrap** (URI-WRAP-V2, 2026-05-13) — opt-in, single or bulk. Three phases on the stitcher draft: audience review (advisory), auditor pass (rendered-prose-against-graph audit), editor pass (whole-text prose work + flag/finding remediation). Reads from `draft/<slug>.md` and the upstream graph (render-log, scene-map, facets, dialogue, exposition); writes to `polish/<slug>.md`. The editor is the only phase with whole-episode view. v1 (per-line `show.md`) archived at `archive/commands/and-wrap.md`.

---

## Agent routing table

| Agent | Role | Owned by |
|-------|------|----------|
| showrunner | Memory holder. Reads/writes series memory and state files. Does NOT orchestrate — command bodies do. No Agent tool. | `staff/showrunner/` |
| screen-writer | Plan generator. Series/season/episode bullet plans. | `staff/screen-writer/` |
| coach | Prompt translator. Bullet → impersonator prompt. | `staff/coach/` |
| impersonator | Character primitive. One per active actor per episode. | spawned per-actor |
| studio | Set and environment manager. Records all state changes. | `staff/studio/` |
| audience | Critic config. Default 3 persona cards for plan and line review (active-project/audience/). Override modes: facet-adversarial review at `/and-facets` Phase 5b (per-reviewer verdicts, 3-of-3 accept) and taste-judge at `/and-project` Phase 1.5 (single-card from `staff/audience/taste-judge/`, returns menu picks). | `active-project/audience/` + `staff/audience/taste-judge/` |
| dramatist | Structural critic. Plans and wrap review. | stateless |
| auditor | Fault-finder. Constraint/state/drift audit. Returns report. | `staff/auditor/` |
| fixer | Targeted correction. Meets auditor criteria with minimum change. | `staff/fixer/` |
| margit | Card warehouse. Stores, indexes, validates, promotes. | `staff/margit/` |
| editor | Final draft. `/and-wrap` v2 (URI-WRAP-V2) only. Reads stitcher draft + render-log + scene-map + audience flags + auditor SIGNAL findings. Whole-text view: cross-scene percussion, voice consistency, repetition cull, continuity, prose economy. Writes ship-ready manuscript to `polish/<slug>.md`. Allowed-moves contract enforces graph respect (no plot invention, dialogue verbatim, exposition gloss verbatim, scene-map fixed, peak-shadow standalone). | `staff/editor/` |
| orchestrator-critic | Run-judge card. Defines the standard `/and-season` must satisfy to be considered a success — convergence + quality + routing + runtime. Library-only; not a subagent (main session reads the card and produces a verdict at Phase 6 of `/and-season`). | `staff/orchestrator-critic/` |

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
  audience/       — audience persona library (19 personas; INDEX.md; 3 selected per project for plan-review duty; `taste-judge/` is a single-card library entry reserved for `/and-project` Phase 1.5 menu picks and never copied into active-project)
  orchestrator-critic/ — run-judge card (`card.md`); library-only standard for `/and-season` success at Phase 6

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
  draft/          — stitcher output (pre-editor; clean + annotated drafts)
  polish/         — editor output / closed manuscripts (post-/and-wrap)

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
| Scene-map (derived structural facet, shoot-v2) | `schemas/scene-map.schema.md` |

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
8. Card schema authority is `schemas/card.schema.md`. Margit validates against it. No card class outside the five defined (persona, location, prop, condition, behavior). **Exception:** `staff/orchestrator-critic/card.md` is staff-facing (judges production, not story content) and is explicitly outside the cards/ taxonomy. Staff-facing critic cards are documented in their own card frontmatter.
9. All agent dispatches use the Agent tool. Inline generation is not a substitute for a dispatch — an agent that is not spawned in isolation does not have the context isolation the pipeline depends on.
10. `/and-season` runs are gated at Phase 6 by `staff/orchestrator-critic/card.md`. PASS/PASS-WITH-NOTES/FAIL is the verdict on whether the run satisfied the standard. FAIL escalates to user; downstream work is gated on user decision. **Bone-gate (URI-026, 2026-05-10):** `/and-season` Phase 4 Step 1.5 (tens authoring) + Step 2 (audience+mechanic combined verdict) is the upstream bone-gate. Tens-gate residual HARD findings auto-trigger F7 (FAIL) per the card's failure-mode enumeration — bones-first principle: deformed proto-lines cannot be rescued by downstream facet skin.
11. **Shared reviewer resources (URI-026, 2026-05-10).** Reviewer assets are authored once and consumed from both `/and-season` and `/and-facets`. The audience persona cards' `Threshold Discipline` and `Season-Scope Adversarial` body sections, the auditor class library (`CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND` definitions in `.claude/commands/and-facets-audit.md`), and the tens rubric (`design/shoot-v2/rubric-tensometer.md`) are the canonical shared surfaces. No pipeline-specific reimplementation. Patterns the audience flags at `/and-season` bone-gate graduate into AP-SCAN entries via the shared auditor's TASTE-FLAG → AP-SCAN promotion path; auditor class refinements land once and benefit both pipelines.

---

## Commands

Project-local slash commands in `.claude/commands/`.

| Command | Purpose |
|---------|---------|
| `/and-project <title-slug> "<brief>" <audience-1> <audience-2> <audience-3>` | Project activation. Scaffolds `active-project/`, runs world-building (1a–1d) and series plan, presents output at the series-level audit checkpoint for human review. Season planning is owned by `/and-season s01` Phase 1 (auto-fires when no season plan exists). |
| `/and-season <season-slug>` | Season-scope orchestrator. Auto-plans the season in Phase 1 if no `season-<slug>-plan.md` exists (handles s01 and subsequent seasons; reads previous-season terminal state when applicable), then expands content beats into bones, runs full season-scope review with bone-gate, judges at Phase 6 (orchestrator-critic), writes per-episode files at Phase 7. |
| `/and-facets <slug>` | Per-episode facet pipeline. Produces ten facet files + per-character dialogue files under `theater/dialogue/<slug>.md` + scene-map derived structural facet at `theater/facets/scene-map-<slug>.md` (URI-SCENE-WINDOW, 2026-05-13 — emitted at Phase 4d, coverage-validated at Phase 5 CONSTRAINT). **Dialogue-coverage gate (URI-DIALOGUE-COVERAGE-GATE, 2026-05-12):** if proto-lines contains any `speaks to` bones, every such bone MUST be cited by ≥1 dialogue entry AND every speaker MUST have a non-empty dialogue file before `audited-r1` is set at Phase 6a. Phase 5 CONSTRAINT emits HARD findings on bare bones / missing files; Phase 6a re-verifies. **Scene-map coverage gate (URI-SCENE-WINDOW):** every bone must land in exactly one scene; gaps/overlaps/dangling-anchors are HARD findings re-verified at Phase 6a. |
| `/and-stitch <slug>` | Per-episode stitcher. Reads proto-lines + facets + dialogue + exposition + scene-map; produces `draft/<slug>.md` (clean) + `draft/<slug>.annotated.md` (traced). Output lands in `draft/` because stitcher output is pre-editor; the `/and-wrap` editor pass writes the ship-ready manuscript to `polish/`. **Phase 1 modes (URI-SCENE-WINDOW, 2026-05-13):** `scene-window` (default) dispatches one fork per dramatist-marked scene with overlap-read context (back-look on prior rendered scene; forward-look on next scene's bones+facets), breaking multi-bone percussion within bone-faithfulness; the fork runs a mandatory per-bone discipline walk to catch invention-by-summary faults. `per-anchor` (fallback, `--phase-1-mode per-anchor` or `phase-1.mode: per-anchor` in profile) dispatches one fork per anchor; used when the scene-map facet is absent, the episode has low percussion accumulation, or fork-isolation debugging is wanted. **Dialogue gate (URI-DIALOGUE-COVERAGE-GATE):** if proto-lines has `speaks to` bones and the dialogue facet is empty/missing or any speech bone is bare, Phase 0.5 HARD-ABORTS. Opt-in `--allow-bare-speech` reroutes to legacy silent-action fallback (pre-2026-05-12 episodes only). |
| `/and-wrap [slug \| --all-stitched \| s01e01..s01e05]` | Per-episode editor pass. Wraps stitcher draft into ship-ready manuscript. **URI-WRAP-V2 (2026-05-13).** Three phases: (1) audience review of rendered prose by the project's three audience personas — advisory flags only, not blocking; (2) auditor pass — rendered-prose-against-graph audit, eight classes (BONE-COVERAGE, DIALOGUE-VERBATIM, EXPOSITION-VERBATIM, NO-INVENTION, CONTINUITY, BLOCKING, SCENE-MAP-RESPECT, EARTH-BET-HARD-FENCE); HARD findings block the editor; (3) editor pass — single Agent dispatch with whole-text view; allowed-moves: prose economy, cross-scene variance, continuity, repetition cull, audience-flag remediation, audit-finding remediation, paragraph adjustments, voice consistency; forbidden: plot invention, dialogue/exposition modification, scene reordering, peak-shadow fusion, protected-pattern abolition. Mandatory per-bone discipline walk; `lost=0` required. Reads `draft/<slug>.md` + render-log + scene-map + facets + audience cards; writes `polish/<slug>.md`. v1 archived at `archive/commands/and-wrap.md` (built around v1 `show.md`; not applicable to shoot-v2). |

---

## Not in scope

- Gacha system — deferred
- Workshop-artifact card class — excluded
