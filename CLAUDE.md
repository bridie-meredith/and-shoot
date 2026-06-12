# and-shoot

**Session-start protocol: read `RUNBOOK.md` first.** When the user says "write" / "continue" / "next" / anything implying forward motion through the pipeline, follow the runbook's 60-second orientation and trigger map. Do NOT ask the user what to do if the state files name a clear next phase. The runbook is operational; this file (and `schemas/`) is authoritative.

---

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
  /and-facets b01c01                    ← single R1 authoring round + context/aliveness review + mechanical audit (R2 round + Phase 5b audience-gate RETIRED — DEC-0116)
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
| audience | Critic config. 3 persona cards. Reviews chunks, bones, plans. Override modes: facet-adversarial review (RETIRED at `/and-facets` under DEC-0116 — the audience-gate is gone; the adversarial prose read now lives at `/and-stitch` Phase 9 cold-read + naive-follow against rendered prose) and taste-judge at `/and-project` (single-card from `staff/audience/taste-judge/`, returns menu picks). | `active-project/audience/` + `staff/audience/taste-judge/` |
| dramatist | Structural critic. Plans, handoff, dramatic-shape review. | stateless |
| auditor | Fault-finder. Constraint / state / drift audit; substance bone-gate. | `staff/auditor/` |
| fixer | Targeted correction. Meets auditor criteria with minimum change. | `staff/fixer/` |
| margit | Card warehouse. Stores, indexes, validates, promotes. | `staff/margit/` |
| editor | Final draft. Library-only under polish-deferred chain; not currently dispatched. Bound at `/and-project` for future revival. | `staff/editor/` |
| orchestrator-critic | Run-judge card. Defines the standard `/and-review verdict <book>` must satisfy to PASS. Library-only; not a subagent. | `staff/orchestrator-critic/` |
| renderer-minimal | Lean prose renderer for facet-ablation studies. Given a bones file + a subset of facet files, single-shot renders the chapter. No chain phases, no polish, no RECONCILE. Used only by `/and-ablate` to produce comparable variants. NOT used by the authoring chain. | `.claude/agents/renderer-minimal.md` |
| admin | Two-mode agent. (1) User proxy — receives questions the main session would otherwise route to the human; answers from persistent goals + methodology + LTM, or returns a structured escalation. **Default channel for every user-facing prompt** — the main session does not call `AskUserQuestion` directly. (2) Process critic — auto-fired on non-PASS chain verdicts + after every `/and-postop` convergence; reads the report + the upstream gate + the proposals log; appends process-change proposals to `staff/admin/process-proposals.md` (schema: `schemas/admin-proposal.schema.md`) for principal triage. Cross-session memory (`ltm.md` / `stm.md` / `goals.md` / `methodology.md` / `decisions.md` / `process-proposals.md`). See Rules §13. | `staff/admin/` |

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

cards/            — story-facing card library (on-stage characters, locations, props, conditions, behaviors) + paired persona-exemplars
  personas/       — on-stage character cards (biography layer)
  persona-exemplars/ — persona-exemplar library (live channel for Tier-1 consumers; PROP-0005)
  locations/      — location cards
  props/          — prop cards
  conditions/     — condition cards
  dialects/       — behavior cards (rename to behaviors/ pending; deferred under this overhaul)

active-project/   — sole active project
  actors/         — active cast (provisioned by /and-cast Phase 4)
  warehouse/      — active locations, props, conditions
  audience/       — 3 active audience persona working dirs
  persona-exemplars/ — optional project-bound exemplar overrides (beats library on dispatch resolution)
  voice-exemplar.md  — optional series-level renderer voice exemplar (PROP-0003-A; separate format)
  staff/          — showrunner / studio / auditor / fixer / margit / screen-writer / editor working memory
    reviews/      — /and-review reports (canonical reports directory)
  theater/
    bones/        — bones files: <book>-<chapter>.md (emitted by /and-write Phase 7)
    facets/       — facets per chapter: <facet>-<book>-<chapter>.md (flat naming convention; tensometer dropped)
    proto-lines/  — canonical merged proto-line file with [<facet>:<id>] citations from the single R1 authoring round (intermediate artifact written by /and-facets Phase 2 / build_cite_index.py; consumed by /and-facets Phase 4 auditor + /and-stitch Phase 0/1)
    dialogue/     — per-character dialogue files (per character, per chapter). **Co-emitted with bones by /and-write Phase 7 under URI-WRITE-DIALOGUE-COBONDED (2026-05-25).** The bones file + scene-map facet + per-character dialogue files are the atomic /and-write Phase 7 emit set; dialogue is no longer authored at /and-facets.
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
| Persona-exemplar | `schemas/persona-exemplar.schema.md` |
| Scene-map (upstream-emitted by /and-write Phase 7) | `schemas/scene-map.schema.md` |
| Stitcher profile | `schemas/stitch-profile.schema.md` |
| Stitcher feedback | `schemas/stitch-feedback.schema.md` |
| Stitcher render-log | `schemas/stitch-render-log.schema.md` |
| Parking-lot (cross-chunk watch items) | `schemas/parking-lot.schema.md` |
| Admin process-change proposal | `schemas/admin-proposal.schema.md` |
| Tournament scorecard (per-scene cherry-pick scoring) | `schemas/tournament-scorecard.schema.md` |
| Substance framework | `design/substance/{README,questionnaire,delta-targets,rerun-protocol,staleness-cascade,run-book,plan}.md` |
| Tournament tuning framework | `design/tournament-tuning.md` |

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
11. **Shared reviewer resources.** The audience persona cards' `Threshold Discipline` body sections and the auditor class library (`CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND` / `RUBRIC-FIDELITY` definitions in `.claude/commands/and-facets.md`) are the canonical shared surfaces. No pipeline-specific reimplementation. Patterns the audience flags at `/and-write` bone-gate graduate into AP-SCAN entries via the auditor's TASTE-FLAG → AP-SCAN promotion path. The `/and-facets` Phase 5b audience-gate is RETIRED (DEC-0116), so the audience no longer flags facet patterns there; the promotion path into RUBRIC-FIDELITY survives for patterns surfaced anywhere (the `/and-stitch` Phase 9 prose read, `/and-postop`, or principal review) — add the rule to the relevant facet rubric's REJECT / anti-pattern / cross-facet contract section, and the `/and-facets` Phase 4 auditor enumerates those sections at audit time, promoting a taste call to a mechanical check on the next run.
12. **Re-runnability.** Every command except `/and-project` is re-runnable per `design/substance/rerun-protocol.md`. Phase 0 of every re-runnable command implements the same shape: read upstream → check own output (prompt mode) → surface cascade → **scan parking lot (Rule 14)** → run.
13. **User prompts go to admin, not the human (user-proxy mode).** The main session must not call `AskUserQuestion` to ask the user directly. Every prompt the main session would have asked the human is dispatched to the admin subagent (`subagent_type: admin`, `mode: user-proxy` or omitted) with question + context + options + default. Admin answers in the user's voice from goals + methodology + LTM, or returns a structured `ESCALATE` block. Only on `ESCALATE` does the main session forward the question to the human via `AskUserQuestion` — and only the question admin escalated, not a re-derived one. This rule applies to all routine flow control (mode prompts, accept/redraft prompts, pipeline branch choices, optional-step gating). Hard human checkpoints declared in command bodies (e.g. `/and-cast` Phase 5 series-level audit) remain human-only and bypass admin.

    **Admin process-critic mode.** Admin has a second mode that auto-fires on (a) any non-PASS verdict from a chain command (FAIL / REVISE / PASS-WITH-DEPTH-PASS-REQUIRED from `/and-review`, `/and-write` bone-gate, the `/and-facets` Phase 5 orchestrator-critic verdict (NOT-SUCCESSFUL / SHIPPABLE-WITH-CAVEATS), `/and-stitch` Phase 9) and (b) every `/and-postop` convergence write. Dispatch carries `mode: process-critic` + `trigger.reason` + `trigger.source_report` + `gate_path` (per `schemas/admin-proposal.schema.md`). Admin reads the report + the upstream gate + the proposals log, judges whether the *process itself* needs to change, and returns `OK` / `OK-MERGED` / `OK-PRIOR-REJECTION` / `OK-RE-SURFACED` / `PROCESS-CHANGE-PROPOSED PROP-<NNNN>` / `ESCALATE`. New proposals append to `staff/admin/process-proposals.md` for principal triage. Admin does not implement accepted proposals — that's a separate session the principal dispatches. Tail-step wiring lives at `/and-write` Phase 6.5, `/and-facets` Phase 4.5 (renamed from the retired Phase 5c under DEC-0116), `/and-stitch` Phase 9.5, `/and-postop` Phase 3.5 (always-fires), and `/and-review` Common-Phase 4.5.
14. **Parking lot — cross-chunk watch items.** `active-project/staff/showrunner/parking-lot.md` (schema: `schemas/parking-lot.schema.md`) is the canonical surface for findings whose resolution belongs in a later command invocation. Phase 0 of every re-runnable command MUST scan the parking lot for items where `target.command` equals the current command and `target.scope` matches the current invocation (exact slug or `*` wildcard) and `status: open`. **Phase 0 surfaces matching items in its print block; it does not abort on existence.** The HARD-abort fires at the named resolving phase (or final-summary if `target.phase` is null) if matching HARD items remain open at that point. Resolution stamps `resolved_at` + `resolved_by` + `resolution_note`; entries are never deleted. **SOFT items** are surfaced in the Phase 7 exit summary; they do not block. Any command body, auditor, fixer, or screen-writer may append parking-lot items; resolution is the resolving command's responsibility, not the author's. Pre-existing inline `# Downstream watch-items` comment blocks in `memory.md` are legacy narrative; new findings go to the parking lot.

15. **Dialogue ships with bones (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25).** The dialogue facet is inseparable from the bones it anchors to — per-character dialogue files at `theater/dialogue/<character-slug>.md` are co-emitted by `/and-write` Phase 7 alongside the bones file, NOT authored downstream by `/and-facets`. `/and-write` Phase 1.5 fans out per-behavior-card dialogue-writer dispatches; Phase 6 verifies (FAULT-DIALOGUE-MISSING-AT-ANCHOR / FAULT-DIALOGUE-CARD-VIOLATION / FAULT-DIALOGUE-OBJECTIVE-MISSING / FAULT-DIALOGUE-EARTH-BET-FENCE / FAULT-DIALOGUE-COVERAGE — all HARD); Phase 7 emits the bones file with `[<character-slug>:<id>]` citation tokens already attached on dialogue-anchor bones. `/and-review bones` enforces dialogue-coverage as a HARD gate (subsumes the former `/and-facets` dialogue-coverage gate). `/and-facets` Phase 1 dialogue R1 author is REMOVED; the R2 dialogue judge is also RETIRED under DEC-0116 (the entire R2 round is gone). Its one non-mechanical concern — a dialogue line duplicating a lens facet rendering the same content at the same anchor — is absorbed by the `/and-facets` Phase 4 auditor's DEDUP class; dialogue-coverage + card-compliance + Earth-Bet-fence are mechanical auditor checks there. Cap-burn DELETE of dialogue at `/and-facets` was already retired; cap-burn now happens at `/and-write` if at all. Dialogue is therefore NOT a separable facet for `/and-ablate` — the bones-only variant includes dialogue.

16. **Persona representation is biography + exemplar (URI-PERSONA-EXEMPLAR, 2026-05-26).** Per PROP-0005 / DEC-0016 (narrowed by PROP-0005-A / DEC-0017), personas have two layers:
    - **Biography card** at `cards/personas/<slug>.card.md` (or `staff/audience/<slug>/card.md` for audience personas) — identity, voice description, taste, fences. Authoritative for what the persona *is* and *cannot do*.
    - **Persona-exemplar** at `cards/persona-exemplars/<slug>.md` (library) or `active-project/persona-exemplars/<slug>.md` (project-bound override) — concrete 150-350 word demonstration of voice in known-good form. The live channel for Tier-1 consumers.
    
    **Tier-1 consumers** (auto-resolve exemplar at every dispatch): impersonator, audience (3-persona reviewer trio + taste-judge override), renderer voice (`/and-stitch` Phase 0 step 4a — uses parallel `active-project/voice-exemplar.md` format, not this schema).
    
    **Tier-2 deferred** (template/structure-driven; exemplar-priming actively regressed output in the 2026-05-26 critic experiment): orchestrator-critic, dramatist, auditor, editor. Do NOT author exemplars for these without a fresh experimental basis.
    
    **Tier-3 out of scope** (no persona/voice channel): showrunner, margit, fixer.
    
    Exemplar resolution at dispatch (project-bound → library → absent) is automatic per agent definition; dispatcher command bodies do NOT need to be modified. The surface-convention fence (no exemplar content import; only cadence/structure transfers) is non-negotiable wherever exemplars are loaded. See `schemas/persona-exemplar.schema.md` (schema) and `staff/margit/exemplar-authoring-process.md` (authoring + QC). Margit gates: `/and-project` Phase 1c blocks on missing audience exemplars; `/and-cast` Phase 5 blocks on missing actor exemplars.

17. **Completeness + readability are gated progressively, not only at stitch (PROP-0019/0020/0022 + spine-legibility pair, 2026-05-29).** The b01-c05 three-FAIL trace's root cause was a context+voice gap caught only at the terminal cold-read. Two paired upstream tracks now address it, both surfaced as a *second axis* riding existing checkpoints — they do NOT add commands:
    - **Completeness / context-weave (PROP-0020):** `/and-review bones` followability pre-check (`follow_check`; `FOLLOW-FAIL` HARD-gates `/and-facets`) → `/and-facets` Phase 2.5 post-R1 context review → **context-ledger** (`active-project/staff/showrunner/context-ledger-<book>-<chapter>.md`; licenses exposition adds past the anti-exposition penalty) → Phase 3 conditional remediation on open **spine** holes + fixer/WARN (slimmed under DEC-0116 — the old Phase 4.5 re-check / Phase 4.6 R3 collapse into one conditional pass fired off Phase 2.5; the R2-era re-review gate is gone). `/and-stitch` Phase 9 naive-follow is the terminal backstop.
    - **Readability / aliveness twin (PROP-0022):** the same Phase 2.5 checkpoint carries an aliveness axis (`ALIVE`/`AIRLESS`) → **grounding-ledger** (`grounding-ledger-<book>-<chapter>.md`; licenses sensory grounding past the frequency-band cap) → `/and-stitch` Phase 4 **voice-embodiment discipline** (prefer the person-first faithful rendering over apparatus-register, within the bone-faithfulness fence; calibrated against `active-project/voice-exemplar.md`). `/and-facets` Phase 2.5 scores the two axes separately (FOLLOWABLE×ALIVE), and `/and-stitch` Phase 9 re-scores them on rendered prose and requires BOTH.
    - **Spine-legibility pair (unnumbered; URI-WRITE-EVENT-CONCRETENESS + URI-STITCH-SPINE-STAGING):** `/and-write` Phase 6 `EVENT-NOT-CONCRETE` (HARD — central-event bone must be concrete SVO) + `ABSTRACTION-DOMINANT` (SIGNAL); `/and-stitch` Phase 9 promotes a single staging finding on a central-event/stakes-axis bone to blocking.
    - **PROP-0019/0019-A** (the chunk-cold-read leg) is upstream of these at `/and-substance chapter` Phase 5.5 (`chunk_cold_read` + `PASS-CHUNK-VOICE-RISK` arming `/and-stitch` Phase 8.5 central-event-muffle). Status: all wired; validated against the c05 evidence archive but NOT yet proven on a *live* chapter — b01-c06 is the first live test. See `staff/admin/readability-completeness-overhaul-report-2026-05-29.md`.

18. **Chapter production follows the RUNBOOK protocol verbatim (PROP-0032, 2026-05-31).** The project's primary operation — "produce a chapter" — has a single canonical protocol in `RUNBOOK.md § Producing a chapter — end-to-end protocol`. Triggers: "produce c<MM>" / "do chapter X" / "write the next chapter" / "walk away while you do c<MM>" / any phrasing meaning "give me a finished chapter." The protocol binds five rules:
    - **R1** — no `AskUserQuestion` for the duration of the run; admin user-proxy is the only channel; admin `ESCALATE` is queued to the end-of-run summary, not prompted.
    - **R2** — drive through cap-bounded gate FAILs within their existing caps: bones FAIL (1 retry), stitch Phase 9 FAIL (1 retry); cap exhaustion halts. (The `/and-facets` audience-gate cycle is RETIRED under DEC-0116 — the facet layer's gate is now the Phase 4 mechanical auditor, which self-remediates ≤2 passes internally; HARD-persist past that is a NOT-SUCCESSFUL halt, not a principal-facing retry loop.)
    - **R3** — pre-flight check + print, then go silent. No interim narration, no mid-run check-ins.
    - **R4** — single end-of-run summary block on completion or halt. All verdicts, ESCALATE queue, process-critic findings, checkpoint, next-step suggestion.
    - **R5** — hard halts always abort cleanly with checkpoint: cap exhaustion, pre-flight HALT, mid-run parking-lot HARD discovery, `/and-cut`, `/and-substance chapter` Phase 0 unacknowledged-substantive HARD-abort, any documented chain HARD-abort not in R2's table, unretryable tool failure.
    
    The chain itself is `--cascade` over `/and-substance chapter` → `/and-write` → `/and-review bones` → `/and-facets` → `/and-stitch` (through Phase 9 cold-read AND Phase 10 forward-thread). `/and-postop` is NOT in the chain — opt-in depth-of-quality check, surfaces in the end-of-run summary. `/and-cohere` is NOT in the per-chapter chain but IS mandatory at book-thirds milestones (~1/3 and ~2/3 of planned chapters); a `FAIL-COHERE` on interior-sameness blocks further ships until addressed (PROP-0050); the pre-flight check enforces this. R1–R5 supersede any command-body behavior that would prompt the principal mid-run. When command-body docs conflict with the runbook protocol on chapter-production behavior, the runbook wins for chapter-production runs.

19. **Subagent output-persistence check (TRUST-WITHOUT-VERIFY gate; PROP-0043, 2026-06-07).** Any command body or main-session dispatch that sends work to a Write-capable agent contracted to emit one or more specific artifacts MUST existence-check each declared output path on disk BEFORE consuming the in-message result or building on it downstream. After the agent returns: stat/ls each declared emit path; if present, proceed; if absent (in-message-only result), treat the artifact as **NOT DELIVERED** — persist it from the return text or re-dispatch with an explicit write instruction, then confirm existence before proceeding. The contracted emit path is determinable from the agent routing table (auditor → `staff/auditor/<scope>-audit.md`; screen-writer / studio / margit / renderer / editor / fixer similarly) or from explicit path declarations in the phase brief. The check is one stat/ls — always cheap, never optional. (Earned: the b01-all aggregate auditor returned a full report in-message but never wrote the file; caught one step from permanent loss.)

20. **Post-async-agent shared-state read-back (PROP-0044, 2026-06-07).** When an async agent is dispatched with Edit/Write access to a SHARED state file — any file the main session has also written or will write in the same invocation (cohere-state files, `parking-lot.md`, showrunner `memory.md`, `decisions.md`, `process-proposals.md`, and any path named in the agent brief as a mutation target) — the session MUST read the resulting state of every touched path (read the file or `git diff HEAD -- <path>`) BEFORE treating that state as settled or committing on top of it. If the result introduces schema violations, duplicate keys, unexpected field mutations, or unauthorized content: correct before committing. Do NOT commit on top of an unreviewed agent mutation. Distinct from Rule 19: Rule 19 catches a *missing* artifact; Rule 20 catches a *defective* mutation of a file that was successfully written. Both apply independently. (Earned: an admin user-proxy edit introduced a duplicate YAML `result:` key into a cohere-state file, committed unreviewed, caught only by a later auditor.)

21. **Pre-commit RECONCILE on hand-authored aggregates (PROP-0045, 2026-06-07).** Before committing a hand-authored rollup/triage artifact — `/and-cohere` aggregate (triage note + state write + parking-lot items) or `/and-review verdict`/`cohere` rollup — run three checks: **(1) Citation resolution** — every cited `DEC-`/`PROP-`/`pl-` id exists in its owning file AND the claim the aggregate makes about it matches what it actually says (a DEC cited as "authority for X" must actually adjudicate X); every generated parking-lot id matches `schemas/parking-lot.schema.md`. **(2) Report↔state field-equality** — `load_bearing_fails`, `failed_axes`, `caution_axes`, and `revise_queue[*]` in the report equal the state file's. **(3) Self-contradiction scan** — an item whose text names N atomic resolution points must be filed as N items (RESOLUTION-COUNT-MISMATCH → split before commit). Any check FAIL blocks commit until corrected. Wired into `.claude/commands/and-cohere.md` (Phase 3/4 RECONCILE sub-step) and `.claude/commands/and-review.md` (verdict/cohere aggregate authoring). (Earned: the b01-all aggregate shipped a mis-cited DEC, a two-point fix filed as one item, and a systematic id-format drift — all visible at authoring time.)

22. **No ledger register — prose renders concrete action, never bookkeeping (DEC-0115 / PROP-0046–0050, 2026-06-08).** The cold ledger/accounting/apparatus register is **retired as a prose mode**, project-wide and forward. When a narrator perceives the world through an apparatus (a feed, a count, a ledger, a column, an insect-network, a sense-power), that apparatus is a **lens** — it may NOT be the grammatical subject of narration nor the unit by which events are reported. Events render as **concrete physical/human action first** ("I sent the flies across their hands and the nearest dozen stepped back," not "the gap propagated"; "they took him away down the corridor," not "I wrote him into the ledger as a closed entry"). Coldness, control-instinct, and analytical distance survive as **character**, not as bookkeeping vocabulary. This is the root-cause fix for the b01 readability failure (Book 1 narrated nearly every event as its accounting-trace until a naive reader could not reconstruct the scene; verdict-PASS-WITH-NOTES masked it as "design-inherent signature" across ~16 dispositions with no circuit breaker — DEC-0115 reverses DEC-0105/DEC-0114). The fence is enforced at every authoring surface, not one gate:
    - **`/and-write` Phase 6 (origin):** `ABSTRACTION-AS-SUBJECT` (a bone whose subject is the apparatus/an abstraction, e.g. "the count closes") is a **HARD** bone-gate finding; each scene must hold a concreteness floor (default ≥ 0.6 concrete-SVO bones), else `SCENE-ABSTRACT-DOMINANT` HARD. The disease originates in abstract bones — the stitcher cannot un-abstract what the bones never made concrete.
    - **`/and-stitch` Phase 4:** ledger/accounting/apparatus register is **PROHIBITED** (was: person-first merely *preferred* under PROP-0022). `LEDGER-REGISTER` findings re-render concrete, or route upstream as `EMBODIMENT-BLOCKED` (≥ K on a chapter → `/and-write revise`, since the fix is content bones must supply). Calibrate to `active-project/voice-exemplar.md` (the "dense-but-breathing" target).
    - **`/and-stitch` Phase 9 + audience cards:** the cold-read carries a **naive-follow** sub-gate — a fork with NO signature/contract context must be able to write a one-paragraph plain-English "what physically happens here"; if it cannot, `FOLLOW-FAIL` (blocking → `/and-write revise`). No reviewer may excuse opacity as "intended register/signature"; followability is judged against a naive reader.
    - **Disposition (the circuit breaker):** a single defect class may be dispositioned "design-inherent / accepted-caveat" at most **N=2 consecutive** chapters; the (N+1)th auto-promotes NOTE → BLOCKING and forces a depth-pass or explicit principal escalation before further ships. "Design-inherent" is no longer a renewable license.
    - **Signature constraint:** a substance signature (`/and-substance series`) may NOT be satisfiable by a prose register, and must declare a readability/concreteness floor as a non-negotiable constraint the register coexists with — no single-axis register-as-substance optimization.

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
| `/and-facets <book>-<chapter>` | Per-chapter facet pipeline (SLIM — URI-FACETS-SLIM / DEC-0116). Single R1 authoring round (the facets, exposition `surface:reference` by default) → cite-index → Phase 2.5 context/aliveness review (+ context/grounding ledgers) → Phase 3 conditional spine-hole remediation → Phase 4 single mechanical auditor (the facet-layer gate; 12 classes incl. scene-map coverage + dialogue dedup/coverage sanity + Earth-Bet fence) → Phase 5 persist + orchestrator-critic verdict. The R2 judging round and the Phase 5b adversarial audience-gate are RETIRED; the adversarial prose read moves to `/and-stitch` Phase 9. ~10-12 dispatches (was ~60-100). bones-review precondition + URI-SCENE-WINDOW enforced; dialogue is upstream from `/and-write` Phase 7. |
| `/and-stitch <book>-<chapter>` | Per-chapter stitcher. Eight render phases (lens-anchored → redundancy cull → compression → voice transform → local flow + speaker-paragraph breaks → buildup preservation → editorial reflection → finalize + scene-callout strip + RECONCILE) + Phase 9 cold-read terminal gate (blocking; FAIL routes to `/and-write revise`). Phase 9 Step 4 includes the URI-STITCH-SIGNAL-CLUSTER soft-gate (2026-05-24) — a verdict of PASS-WITH-DEPTH-PASS-REQUIRED ships terminal but flags the chapter for `/and-write revise --from-signals` before project-stable. Tensometer-fallback removed from Phase 0. Output: `draft/<book>-<chapter>.md` — **terminal deliverable** under the polish-deferred chain. |
| `/and-postop <book>-<chapter> [milestone] [--persona <slug>]` | Post-op review for a shipped chapter. Routine mode runs 3 forks (substance-delivery + naive cold-read + one audience persona); milestone mode adds forward-hook + orchestrator-critic synthesizer. Not a gate — depth-of-quality call on shipped chapters. Distilled from the b01c01 8-fork post-ship audit suite (`active-project/staff/showrunner/post-ship-audit-prompts-b01c01.md`); ~60% less spend, same signal. |
| `/and-review [<subcommand> [<args>]]` | Universal review primitive with subcommand router. Subcommands: `chunk` / `bone` / `contract` / `signature` / `bones` / `facets` / `cast` / `consistency` / `pipeline` / `tree` / `feedback` / `staging` / `verdict` / `prose` (DEFERRED). `bones` is the mandatory chunk→bones fidelity review between `/and-write` and `/and-facets`; `staging` is the additive editorial pass (EXPAND/GROUND/STAGE/NEEDS-BEAT). Verdict subcommand absorbs the former `/and-judge-book` and fires the orchestrator-critic against a book. Pipeline subcommand runs the schema-vs-command-body-vs-rubric tri-walk that catches cross-file drift (URI-REVIEW-PIPELINE; 2026-05-21). |
| `/and-cut` | Mid-pipeline stop. Saves resume checkpoint; prints "you are here" with `next:` and (if cascade was in-progress) `resume:` lines. |
| `/and-ablate <book>-<chapter>` | Facet-ablation study. 12 prose variants (bones-only + full + 10 leave-one-out) rendered by the `renderer-minimal` agent; one ranked-comparison cold-read returns ranking + per-variant differential. Output at `staff/reviews/ablation-<book>-<chapter>-<timestamp>.md`. Feeds admin process-critic — recurring low-rank facets become `delete`/`modify` proposals. On-demand only; not part of the chain; not a gate. ~14 dispatches per run. |

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
