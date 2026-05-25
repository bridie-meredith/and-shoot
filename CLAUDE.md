# and-shoot

Autonomous fiction pipeline. The system authors creative fiction across a series → book → chapter → scene hierarchy with declared substance contracts at every level. Reviews fire inline at each authoring command; the only blocking human checkpoint is the series-level audit inside `/and-cast`.

**Human role:** approve at the series-level audit checkpoint (Phase 5 of `/and-cast`). Book-, chapter-, and scene-level loops run agent-to-agent with no required human checkpoints unless an audit escalates past series scope.

---

## Primary pattern

```
/and-project                            ← scope + staff binding
  ↓
/and-series                             ← series chunk + structural prompts
  ↓
/and-substance series                   ← signature (state axes + cost ledger + antagonist pressure + chunk_targets) + per-book Δ + book chunks
  ↓
/and-cast                               ← roster + series-level audit checkpoint  ← ONLY blocking human checkpoint
  ↓
/and-substance book b01                 ← book drama + per-chapter Δ + chapter chunks + handoff_in/out
  ↓
loop per chapter:
  /and-substance chapter b01c01         ← per-scene chunks + scene_conflict + pov_narrator + dramatic_shape + goal
  /and-write b01c01                     ← scene-decomposition into bones-with-deltas + event-coverage map + five-pass SVO + substance bone-gate
  /and-review bones b01c01              ← MANDATORY chunk→bones fidelity review (gates /and-facets)
  /and-facets b01c01                    ← ten facets + dialogue + scene-map validation (tensometer dropped)
  /and-stitch b01c01                    ← draft/b01-c01.md + Phase 9 cold-read terminal gate (terminal deliverable; polish deferred)
  [optional] /and-postop b01c01         ← post-ship depth-of-quality review (3-fork routine; milestone mode at book mid + close)
  [optional] /and-review verdict b01    ← orchestrator-critic on the book
```

`/and-substance --cascade` chains chapter → write → facets → stitch for every chapter under the named root. `/and-cut` mid-cascade saves a resume checkpoint.

**Polish / `/and-wrap` is deferred** under this overhaul until upstream substance machinery is proven end-to-end. `/and-stitch`'s `draft/<book>-<chapter>.md` is the terminal deliverable. `/and-review prose <chapter>` is stubbed-deferred; un-defer lift target pre-pinned to `archive/commands/and-wrap-polish-deferred.md` Phases 1-2.

---

## Agent routing table

| Agent | Role | Owned by |
|-------|------|----------|
| showrunner | Memory holder. Reads/writes series memory and state files. Does NOT orchestrate — command bodies do. No Agent tool. | `staff/showrunner/` |
| screen-writer | Plan generator. Series / book / chapter / scene chunk authoring + signature proposal. | `staff/screen-writer/` |
| coach | Prompt translator. Used in legacy per-line shoot only (archived). | `staff/coach/` |
| impersonator | Character primitive. Used in legacy per-line shoot + facet authoring (state-updates, narrator-interest, feeling, memory). | spawned per-actor |
| studio | Set and environment manager. State + location-state + sensory facet authors. | `staff/studio/` |
| audience | Critic config. 3 persona cards. Reviews chunks, bones, plans. Override modes: facet-adversarial review at `/and-facets` Phase 5b (per-reviewer verdicts, 3-of-3 accept) and taste-judge at `/and-project` (single-card from `staff/audience/taste-judge/`, returns menu picks). | `active-project/audience/` + `staff/audience/taste-judge/` |
| dramatist | Structural critic. Plans, handoff, dramatic-shape review. | stateless |
| auditor | Fault-finder. Constraint / state / drift audit; substance bone-gate. | `staff/auditor/` |
| fixer | Targeted correction. Meets auditor criteria with minimum change. | `staff/fixer/` |
| margit | Card warehouse. Stores, indexes, validates, promotes. | `staff/margit/` |
| editor | Final draft. Library-only under polish-deferred chain; not currently dispatched. Bound at `/and-project` for future revival. | `staff/editor/` |
| orchestrator-critic | Run-judge card. Defines the standard `/and-review verdict <book>` must satisfy to PASS. Library-only; not a subagent. | `staff/orchestrator-critic/` |
| admin | User proxy. Receives questions the main session would otherwise route to the human; answers from persistent goals + methodology + LTM, or returns a structured escalation. Cross-session memory (`ltm.md` / `stm.md` / `goals.md` / `methodology.md`). **Default channel for every user-facing prompt** — the main session does not call `AskUserQuestion` directly. Questions go to admin first; admin answers in the user's voice or returns a structured escalation, at which point the main session forwards the escalation to the human (this is the only legitimate use of `AskUserQuestion`). See Rules §13. | `staff/admin/` |

---

## Directory map

```
schemas/          — schema authority

staff/            — production staff: agent homes + audience persona library
  showrunner/     — agent home: card.md + ltm.md + stm.md
  margit/         — agent home
  coach/          — agent home (legacy per-line shoot)
  screen-writer/  — agent home
  studio/         — agent home
  auditor/        — agent home
  fixer/          — agent home
  editor/         — agent home (library-only; polish-deferred)
  audience/       — audience persona library (22 personas; INDEX.md; 3 selected per project; `taste-judge/` is a single-card library entry reserved for `/and-project` menu picks and never copied into active-project)
  orchestrator-critic/ — run-judge card

cards/            — story-facing card library (on-stage characters, locations, props, conditions, behaviors)
  personas/       — on-stage character cards
  locations/      — location cards
  props/          — prop cards
  conditions/     — condition cards
  dialects/       — behavior cards (rename to behaviors/ pending; deferred under this overhaul)

active-project/   — sole active project
  actors/         — active cast (provisioned by /and-cast Phase 4)
  warehouse/      — active locations, props, conditions
  audience/       — 3 active audience persona working dirs
  staff/          — showrunner / studio / auditor / fixer / margit / screen-writer / editor working memory
    reviews/      — /and-review reports (canonical reports directory)
  theater/
    bones/        — bones files: <book>-<chapter>.md (emitted by /and-write Phase 7)
    facets/       — facets per chapter: <facet>-<book>-<chapter>.md (flat naming convention; tensometer dropped)
    proto-lines/  — canonical merged proto-line file with [<facet>:<id>] citations from R1+R2 union (intermediate artifact written by /and-facets Phase 2 / build_cite_index.py; consumed by /and-facets Phase 5 auditor + /and-stitch Phase 0/1)
    dialogue/     — per-character dialogue files (per character, per chapter)
  draft/          — stitcher output (terminal deliverable; polish deferred)
  polish/         — not written by the current chain (polish-deferred)

projects/         — completed series archive
archive/          — archived commands, rubrics, and historical specs
  commands/       — archived command bodies (see archive/commands/README.md)
  rubrics/        — archived rubrics (see archive/rubrics/README.md)
```

---

## Schema authority

All file formats are defined in `schemas/`.

| File type | Schema |
|-----------|--------|
| Cards | `schemas/card.schema.md` |
| Actor memory (LTM/STM/state/vibes) | `schemas/memory.schema.md` |
| Showrunner memory | `schemas/showrunner-memory.schema.md` |
| Audit report | `schemas/audit-report.schema.md` |
| Per-character dialogue file | `schemas/dialogue.schema.md` |
| Bones file | `schemas/bones.schema.md` |
| Facet file | `schemas/facet.schema.md` |
| Scene-map (upstream-emitted by /and-write Phase 7) | `schemas/scene-map.schema.md` |
| Stitcher profile | `schemas/stitch-profile.schema.md` |
| Stitcher feedback | `schemas/stitch-feedback.schema.md` |
| Stitcher render-log | `schemas/stitch-render-log.schema.md` |
| Substance framework | `design/substance/{README,questionnaire,delta-targets,rerun-protocol,staleness-cascade,run-book,plan}.md` |

Legacy schemas preserved for reference: `episode-plan.schema.md`, `show-file.format.md` (pre-substance; no longer authored).

---

## Memory rules

**Nothing changes without being recorded.** If an actor moved, their state file records it. If a prop changed hands, studio's state file records it. If a change is not in a state file, it did not happen.

**Showrunner memory is cross-session.** `active-project/staff/showrunner/memory.md` is read at every session open. It is the fast path to reconstructing full working context.

**Actor memory lives in active-project.** At project close, the active-project directory is archived to `projects/<title>/`. Actor memory travels with it.

**Vibe-clouds are built at series and book level.** Both are active during authoring; book-level takes priority on key conflicts. Chapter / scene / bone-level shaping comes from the substance contract, not a vibe-cloud.

**Per-bone state-delta lives in showrunner memory only.** `chapters[].scenes[].bones[].substance_delta` is the source of truth; the flattened bones file is comment-clean.

**Staleness cascade.** Re-running an upstream command stale-marks downstream artifacts (per `design/substance/staleness-cascade.md`). The cascade is surfacing-only (warns, does not block) except for `project.series_audit.stale_since`, which HARD-aborts `/and-substance book` until re-approved.

---

## Rules

1. Read the relevant schema before writing any new schema-typed file.
2. Command bodies (`/and-project`, `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-facets`, `/and-stitch`, `/and-review`) are the orchestrators. They dispatch sub-agents directly. Showrunner does NOT orchestrate and does NOT have the Agent tool — it is a memory holder only.
3. Screen-writer authors chunks at every level. `/and-substance` is the chunker-only command (stops at scene chunks). `/and-write` is the bone-authoring command (decomposes scenes into bones with per-bone deltas).
4. Nothing moves without being recorded (state rule — absolute).
5. Bones files are append-only during a single `/and-write` invocation. Re-running `revise` or `redo` clears `gate_verdict` on bones in scope and re-runs the SVO + bone-gate; flat IDs are preserved for unchanged bones in revise mode.
6. Audience membership is defined at `/and-project`. It does not change mid-project except via `/and-cast revise --swap`.
7. Human checkpoints: series-level audit only (inside `/and-cast` Phase 5). `/and-substance book b<NN>` Phase 0 HARD-aborts if `project.series_audit.approved_at` is missing or `stale_since` is set.
8. Card schema authority is `schemas/card.schema.md`. Margit validates against it. No card class outside the five defined (persona, location, prop, condition, behavior). **Exception:** `staff/orchestrator-critic/card.md` is staff-facing (judges production, not story content) and is explicitly outside the cards/ taxonomy.
9. All agent dispatches use the Agent tool. Inline generation is not a substitute.
10. **`/and-write` Phase 6 substance bone-gate is the bones-first authoring gate.** Per-bone axis-movement verification + per-scene aggregate Δ delivery + cost-paid check + opposing-force-visible. Replaces URI-026 tens-gate. `SUBSTANCE-FLAT-<axis>` and `SUBSTANCE-SUSPECT-cheap-gain-<axis>` are HARD findings. Deformed substance contracts cannot be rescued by downstream facet skin.
11. **Shared reviewer resources.** The audience persona cards' `Threshold Discipline` body sections and the auditor class library (`CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND` / `RUBRIC-FIDELITY` definitions in `.claude/commands/and-facets.md`) are the canonical shared surfaces. No pipeline-specific reimplementation. Patterns the audience flags at `/and-write` bone-gate graduate into AP-SCAN entries via the auditor's TASTE-FLAG → AP-SCAN promotion path. Patterns the audience flags at `/and-facets` Phase 5b graduate into RUBRIC-FIDELITY entries by adding the rule to the relevant facet rubric's REJECT / anti-pattern / cross-facet contract section — the auditor enumerates those sections at audit time, so a rubric edit promotes a taste call to a mechanical check.
12. **Re-runnability.** Every command except `/and-project` is re-runnable per `design/substance/rerun-protocol.md`. Phase 0 of every re-runnable command implements the same shape: read upstream → check own output (prompt mode) → surface cascade → run.
13. **User prompts go to admin, not the human.** The main session must not call `AskUserQuestion` to ask the user directly. Every prompt the main session would have asked the human is dispatched to the admin subagent (`subagent_type: admin`) with question + context + options + default. Admin answers in the user's voice from goals + methodology + LTM, or returns a structured `ESCALATE` block. Only on `ESCALATE` does the main session forward the question to the human via `AskUserQuestion` — and only the question admin escalated, not a re-derived one. This rule applies to all routine flow control (mode prompts, accept/redraft prompts, pipeline branch choices, optional-step gating). Hard human checkpoints declared in command bodies (e.g. `/and-cast` Phase 5 series-level audit) remain human-only and bypass admin.

---

## Commands

Project-local slash commands in `.claude/commands/`.

| Command | Purpose |
|---------|---------|
| `/and-project <title-slug> "<brief>" <aud-1> <aud-2> <aud-3> [--screen-writer ...] [--dramatist ...] [--auditor ...] [--editor ...] [--orchestrator-critic ...]` | Project activation. Scaffolds `active-project/`, world-building (1a-1d), staff binding. Series chunk + structural prompts owned by `/and-series`. Non-re-runnable. |
| `/and-series [revise\|redo]` | Series chunk (Star-Wars-trilogy paragraph) + structural prompts (book count, length ranges, cyclical, POV, cross-book continuity, world evolution, series-end shape). |
| `/and-substance series\|book <slug>\|chapter <slug> [revise\|add\|redo] [--cascade [--resume\|--restart]]` | Recursive chunker. Three invocation levels; four chunk levels produced (series → book → chapter → scene). At series level: authors the signature. At chapter level: authors `pov_narrator` + `dramatic_shape` + `goal`. `--cascade` chains through `/and-write` + `/and-facets` + `/and-stitch` to `draft/<chapter>.md`. |
| `/and-cast [revise\|redo] [--retire ...] [--add ...] [--swap ...]` | Cast roster + series-level audit checkpoint (the only blocking human checkpoint). |
| `/and-write <chapter-slug> [revise\|redo] [--from-signals]` | Decompose scenes into bones-with-deltas + event-coverage map + five-pass SVO + substance bone-gate (event-presence + stakes-aware + SIGNAL-disposition) + emit flattened bones file + scene-map facet. Replaces `/and-protolines`. |
| `/and-facets <book>-<chapter>` | Per-chapter facet pipeline. Ten facets + dialogue + scene-map validation (downgraded from derivation under URI-SUBSTANCE-OVERHAUL). Tensometer dropped. URI-DIALOGUE-COVERAGE-GATE + URI-SCENE-WINDOW + bones-review precondition enforced. |
| `/and-stitch <book>-<chapter>` | Per-chapter stitcher. Eight render phases (lens-anchored → redundancy cull → compression → voice transform → local flow + speaker-paragraph breaks → buildup preservation → editorial reflection → finalize + scene-callout strip + RECONCILE) + Phase 9 cold-read terminal gate (blocking; FAIL routes to `/and-write revise`). Phase 9 Step 4 includes the URI-STITCH-SIGNAL-CLUSTER soft-gate (2026-05-24) — a verdict of PASS-WITH-DEPTH-PASS-REQUIRED ships terminal but flags the chapter for `/and-write revise --from-signals` before project-stable. Tensometer-fallback removed from Phase 0. Output: `draft/<book>-<chapter>.md` — **terminal deliverable** under the polish-deferred chain. |
| `/and-postop <book>-<chapter> [milestone] [--persona <slug>]` | Post-op review for a shipped chapter. Routine mode runs 3 forks (substance-delivery + naive cold-read + one audience persona); milestone mode adds forward-hook + orchestrator-critic synthesizer. Not a gate — depth-of-quality call on shipped chapters. Distilled from the b01c01 8-fork post-ship audit suite (`active-project/staff/showrunner/post-ship-audit-prompts-b01c01.md`); ~60% less spend, same signal. |
| `/and-review [<subcommand> [<args>]]` | Universal review primitive with subcommand router. Subcommands: `chunk` / `bone` / `contract` / `signature` / `bones` / `facets` / `cast` / `consistency` / `pipeline` / `tree` / `feedback` / `staging` / `verdict` / `prose` (DEFERRED). `bones` is the mandatory chunk→bones fidelity review between `/and-write` and `/and-facets`; `staging` is the additive editorial pass (EXPAND/GROUND/STAGE/NEEDS-BEAT). Verdict subcommand absorbs the former `/and-judge-book` and fires the orchestrator-critic against a book. Pipeline subcommand runs the schema-vs-command-body-vs-rubric tri-walk that catches cross-file drift (URI-REVIEW-PIPELINE; 2026-05-21). |
| `/and-cut` | Mid-pipeline stop. Saves resume checkpoint; prints "you are here" with `next:` and (if cascade was in-progress) `resume:` lines. |

---

## Not in scope

- Gacha system — deferred.
- Workshop-artifact card class — excluded.
- Polish / `/and-wrap` revival — deferred until substance machinery is proven.
- Absolute-length floor mechanism — OOS, follow-on issue.
- Emotional-substance orthogonality check — OOS, follow-on issue.
- Plot-arc-completion dramatist check — OOS, follow-on issue.
- World-detail consistency — OOS, follow-on issue.
- `cards/dialects/` → `cards/behaviors/` directory rename — deferred (not lockstep with substance overhaul).
- **Name-novelty enforcement for original characters** — OOS, follow-on issue. Library persona slugs (e.g. `mira-stonefield`) leak into downstream forks through three vectors: (a) `boundary-scope.md` embeds library slugs by archetype tag, (b) `prompt-binding.md` carries those tags forward, (c) screen-writer / margit forks at `/and-project` 1b OQ-7 (cost-bearer naming) and `/and-cast` cast composition aren't isolated from `projects/` or library cards by name. Result: original characters get named for library archetype exemplars (observed: "Mira" used as an original Flea Bottom ward in `taylor-westeros-good-intentions` after appearing as `mira-stonefield` in projects 02/04/05). Candidate fixes — strip library slugs from boundary-scope before downstream consumption, add a no-prior-name-reuse clause to `/and-cast` margit and to `/and-project` 1b OQ-name-pick dispatches, or make margit responsible for name-novelty when proposing original characters.
