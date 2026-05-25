---
description: Universal review primitive with subcommand router. Subcommands - chunk / bone / contract / signature / bones / facets / cast / consistency / tree / feedback / verdict / prose (deferred). Verdict subcommand absorbs the former /and-judge-book and fires the orchestrator-critic. All reports persist to staff/reviews/<subcommand>-<target>-<timestamp>.md. Usage - /and-review [<subcommand> [<args>]]
---

Top-level router. Dispatches to one of the listed subcommands. Bare invocation (`/and-review` with no subcommand, or `/and-review --help` or `/and-review help`) prints the subcommand-discovery table and exits without firing any review.

You are the orchestrator. All review primitives are existing reviewer infrastructure (audience, dramatist, auditor, orchestrator-critic, per-facet rubric runners) — this command wires them together. All dispatches use the Agent tool.

Re-runnable (idempotent — each invocation persists a new timestamped report; nothing else is mutated). See `design/substance/rerun-protocol.md § Idempotent commands`.

---

## Subcommand discovery (F5)

When invoked bare or with `--help`:

```
/and-review — universal review primitive

Subcommands:
  chunk <slug>                  audience + dramatist + auditor on a chunk (series / book / chapter / scene)
  bone <slug>                   auditor + audience-fork on a single bone (b<NN>c<MM>s<KK>n<II>)
  contract <slug>               dramatist + auditor on a substance contract (any chunk level)
  signature                     audience + dramatist + auditor on the series signature
  bones <chapter-slug>          bones critics + substance bone-gate on a chapter
  facets <chapter-slug>         per-facet rubric runners on a chapter
  cast                          dramatist + auditor on the roster
  consistency [<root-slug>]     cross-level + cross-chapter sweep (defaults to series)
  pipeline                      schema ↔ command-body ↔ rubric tri-walk; catches cross-file drift
  tree [<root-slug>]            full review sweep at and below root (defaults to series)
  feedback <feedback-file> [<root-slug>]   reviewers fire carrying named feedback as context
  staging <chapter-slug>        additive editorial pass (EXPAND/GROUND/STAGE/NEEDS-BEAT) on a stitched chapter
  verdict <book-slug>           orchestrator-critic on a book; absorbs former /and-judge-book
  prose <chapter-slug>          DEFERRED. polish-revival un-defer target pre-pinned

Recommended next-actions:
  To verify your latest book is ship-ready:        /and-review verdict <book-slug>
  To inspect SIGNAL findings on a chapter:         /and-review bones <chapter-slug>
  To check a planning chunk you just wrote:        /and-review chunk <chunk-slug>
  To sweep an in-progress book:                    /and-review tree <book-slug>
  To audit pipeline drift after schema/rubric edits: /and-review pipeline

All reports persist to active-project/staff/reviews/<subcommand>-<target>-<timestamp>.md
```

---

## Common phases (every subcommand)

1. **Phase 0 — Parse subcommand.** Validate target exists in showrunner memory / on disk per the subcommand's preconditions. Abort on bad input. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-review` + `target.scope` = `<subcommand> <slug>` or `*` wildcard + `status: open`): HARD → abort unless this run resolves; SOFT → carry to the Phase 4 persisted report. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.
2. **Phase 1 — Compose review brief.** Per-subcommand: which reviewers, which rubric, what scope. Per `design/substance/rerun-protocol.md`, the review brief is composed from showrunner memory only — no full-file reads of upstream artifacts the reviewer doesn't need.
3. **Phase 2 — Dispatch reviewers in parallel.** Audience persona forks per persona; dramatist; auditor; orchestrator-critic for `verdict`; per-facet rubric runners for `facets`.
4. **Phase 3 — Aggregate findings.** Structured report. Classify HARD / SIGNAL / TASTE per `schemas/audit-report.schema.md`.
5. **Phase 4 — Persist.** `active-project/staff/reviews/<subcommand>-<target>-<timestamp>.md`. Surface summary + path. Optionally offer to materialize findings into a fix queue for the appropriate authoring command (e.g. HARD findings on `chunk b01c03` → fix queue for `/and-substance chapter b01c03 revise`).
6. **Phase 4.5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC, 2026-05-25; non-blocking).** If the persisted report contains any HARD finding OR if the subcommand emitted a REVISE / FAIL / NOT-SUCCESSFUL verdict (e.g. `verdict` subcommand orchestrator-critic NOT-SUCCESSFUL; `bones` subcommand FAIL on fidelity; `staging` subcommand BLOCK-level findings), dispatch admin in process-critic mode. Non-blocking — the run exits per Phase 4 whether or not admin returns.
   - `subagent_type: admin`
   - prompt carries:
     - `mode: process-critic`
     - `trigger.reason: failure`
     - `trigger.source_report: <Phase 4 persist path>`
     - `trigger.source_verdict: <verdict string + HARD/SIGNAL counts>`
     - `gate_path: .claude/commands/and-review.md#<subcommand>` (named subcommand the verdict came from)
     - Optional: `secondary_gate_paths: [<the upstream command-body or rubric the subcommand was reviewing, e.g. .claude/commands/and-write.md#phase-6 when reviewing bones>]`
   - Admin's return logged in the report tail under `## admin-process-critic`. New proposals land in `staff/admin/process-proposals.md`. See CLAUDE.md Rules §13 and `schemas/admin-proposal.schema.md`.
   - On clean PASS / ACCEPT / SUCCESSFUL across all reviewers: skip the dispatch.

---

## Subcommands

### `chunk <slug>`

Target: any chunk slug (`series`, `b01`, `b01c01`, `b01c01s01`).

Reviewers: audience (3 personas) + dramatist + auditor.

What it reviews:
- Does the chunk match its substance contract?
- Is it the right depth for its level (series chunk substance-bearing without per-book detail; chapter chunk substance-bearing without per-bone detail)?
- Does it feel meaningful?
- Cost language honest?
- For scene-level: is `scene_conflict` populated with concrete forces (not generic "tension")?

Lift basis: pre-overhaul `/and-season` Phase 1 step 1e review-dispatch pattern; adapted to the substance-chain hierarchy (series → book → chapter → scene chunks; per-chunk-level dispatch).

### `bone <slug>`

Target: bone slug (e.g. `b01c01s01n01`).

Reviewers: auditor + audience-fork.

What it reviews:
- Bonefide check: does the SVO actually cause the declared Δ?
- Is the cost real (cost-ledger anchored)?
- Substance-flat?
- Speech-bone form correctness if applicable.

Lift basis: `/and-write` Phase 6 bone-gate per-bone subroutine (extracted).

### `contract <slug>`

Target: any chunk slug.

Reviewers: dramatist + auditor.

What it reviews:
- Is the substance contract well-formed?
- Do per-axis Δ-magnitudes sum correctly to parent?
- Cost-ledger consistent?
- No rank claims without backing?
- **Thematic-axis-coverage (URI-CONTRACT-THEMATIC-AXIS — chapter-level).** For a chapter chunk, does the contract declare — in `axes_in_motion[]` or `axes_held[]` — the axis the chapter `goal` names as its thesis? A chapter whose `goal` is about a moral-framework turn but whose contract never lists `moral-framework` at chapter level is under-declaring its own thesis. Flag `THEMATIC-AXIS-UNDECLARED-<axis>`. This is the check the purely-mechanical sum/enum review never makes — it asks whether the contract is about what the chapter is about.

Lift basis: pre-overhaul `/and-season` Pass S1 constraint audit + Pass S3.5 ruleset compliance; adapted to per-chunk dispatch across the substance-chain hierarchy.

### `signature`

Target: series-only (no slug arg).

Reviewers: audience + dramatist + auditor.

What it reviews:
- Series signature health: are the axes the right axes for this story?
- Anchors honest? (Rank 1 / 5 / 9 sentences calibrated to the story-world?)
- Cost ledger paid across the arc?
- Antagonist pressure named per axis?
- Chunk_targets bands sane?

Lift basis: pre-overhaul `/and-season` Phase 3 sweep-A shape pattern; adapted to series-signature scope under the substance overhaul.

### `bones <chapter-slug>`

Target: chapter slug.

Reviewers: bones critics (SVO craft) + bone-gate logic re-fire.

What it reviews:
- Per-bone axis-movement bonefide?
- Per-scene Δ delivered?
- Cost-paid?
- `SUBSTANCE-FELT` / `-FLAT` per scene.

Output includes per-bone SIGNAL list from `chapters[].scenes[].bones[].gate_verdict.signals[]` with explicit suggestion: `/and-write <chapter> revise --from-signals` to address. Re-fire clears SIGNALs that no longer apply.

**Independent chunk→bones fidelity review (URI-WRITE-BONES-REVIEW-GATE).** Beyond the bone-gate re-fire, this subcommand runs the fidelity check the Phase 6 mechanical gate cannot: does the bone set, read as a whole, actually carry the scene chunks' events? Reviewers read each scene chunk and its `event_map[]` and confirm the decomposition did not hollow the chunk (the b01c02 failure: a chunk's load-bearing events dropped between chunk and bones while every mechanical gate passed). Verdict: PASS / PASS-WITH-NOTES / FAIL.

**Mandatory-step record.** On completion this subcommand writes `chapters[<slug>].bones_review` to showrunner memory: `{reviewed_at, report_path, verdict, bones_file_mtime_at_review: mtime(theater/bones/<book>-<chapter>.md), stale_since: null}`. `/and-facets` Phase 0 HARD-aborts if this record is absent or stale — `/and-review bones` is the required gate between `/and-write` and `/and-facets`, not an optional spot-check.

Lift basis: `/and-write` Phase 6 substance bone-gate (post-hoc re-fire).

### `facets <chapter-slug>`

Target: chapter slug.

Reviewers: per-facet rubric runners.

What it reviews: facet-by-facet review against rubric (`design/shoot-v2/rubric-*.md`).

Lift basis: `/and-facets` R1 fanout per-facet rubric runners (extracted into named subroutine; called from both `/and-facets` and `/and-review facets`).

### `cast`

No target slug.

Reviewers: dramatist + auditor.

What it reviews:
- Does the roster have carriers for every signature axis perspective?
- Viability check (axis-orphans, archetype clashes).

Lift basis: `/and-cast` Phase 3 dramatist viability check (post-hoc fork).

### `consistency [<root-slug>]`

Target: optional root (defaults to series).

Reviewers: dramatist + auditor.

What it reviews:
- Cross-level: do per-book Δ aggregates sum to series Δ? Do chapter dramatic shapes honor book drama? Do scene contracts fit within chapter contract?
- Cost-ledger entries paid?
- Cyclical commitments honored?
- **Cross-chapter handoff sweep:** for every adjacent chapter pair under root, verify `handoff_out` ↔ `handoff_in` consistency (open-threads / world-state / character-state lists align); flag orphans, drops, or character-axis discontinuities.

Lift basis: pre-overhaul `/and-season` Phase 1 step 1g cross-season audit; generalized to cross-level + cross-chapter sweep under root in the substance-chain hierarchy.

### `pipeline` (URI-REVIEW-PIPELINE, A10 — 2026-05-21)

Target: none (operates on the entire pipeline meta-state).

Reviewers: auditor (single fork, schema-audit mode).

What it reviews — the schema-vs-command-body-vs-rubric tri-walk:
1. **Schema vs command bodies.** For every field reference in `.claude/commands/*.md`, verify the field exists in the appropriate schema under `schemas/` (`showrunner-memory.schema.md`, `bones.schema.md`, `facet.schema.md`, `scene-map.schema.md`, `audit-report.schema.md`, `dialogue.schema.md`, `stitch-*.schema.md`). Flag stale field names, paths, enum values; deprecated direction encoding (`+|-|null` vs `up|down`); ghost references to dropped concepts (tensometer, `tens:`, URI-026, `/and-season`, etc.).
2. **Schema vs rubrics.** For every schema-field reference in `design/shoot-v2/rubric-*.md`, verify the field exists in the relevant schema. Particularly: `axes_held[]`, `axes_in_motion[]`, `dramatic_shape` enum values, `rhythm-shape`, `peak-bones`, `chapter_class`.
3. **Command bodies vs rubrics.** For every rubric reference in command bodies, verify the rubric path exists and the named rubric clauses are present at current version. Flag stale "Schema rename (pending)" notices, V3-lock-date inconsistencies, dispatch payloads referencing dropped facet types.
4. **Residue scan.** Grep for known-deprecated terms across `schemas/`, `.claude/commands/`, `design/shoot-v2/rubric-*.md`, `active-project/`. Known-deprecated set: `tensometer`, `tens:` (as load-bearing prefix), `URI-026`, `tens-gate`, `/and-season`, `/and-judge-book`, `/and-shoot` (the legacy season-shoot), `direction: + | -`, `direction: null` (in non-historical contexts), `chapter_class` (if referenced but not in schema). Legitimate historical references in `archive/`, `design/substance/plan-holes-*.md`, etc. are TASTE-FLAGs, not HARDs.
5. **CLAUDE.md sync.** Verify the agent routing table, schema authority table, directory map all reflect current state. Particularly the `theater/` subdir map and the schema authority table's coverage.

Output: classified findings report at `active-project/staff/reviews/pipeline-<timestamp>.md` per `schemas/audit-report.schema.md`. Findings classes:
- `STRUCT-<NNN>` for schema-vs-command-body / schema-vs-rubric / command-body-vs-rubric drift.
- `RESIDUE-<NNN>` for deprecated-term residue (tensometer / `tens:` / URI-026 / etc.).
- `TASTE-FLAG` for intentional historical documentation that looks like drift.

HARD findings block the immediate next chain dispatch (e.g. `/and-substance chapter b<NN>c<MM>` aborts if `pipeline` returned HARDs since its last clean run); SIGNAL findings are reported but pass. The user is expected to dispatch `pipeline` after any significant schema / rubric / command-body change OR before the first chapter of every new book.

Lift basis: the auditor-fork `pipeline-adaptation-audit-2026-05-21.md` worked example. Promoted from reactive-fork to a routine subcommand under URI-REVIEW-PIPELINE (A10 from `run-action-plan-b01c01-2026-05-20.md`).

**When to run.** Recommended before each new book's first chapter (catches drift from the prior book's command-body / rubric edits) AND after any session that touched 3+ command-body / schema / rubric files (the audit catches cross-file inconsistencies the per-file fixer pass missed).

### `tree [<root-slug>]`

Target: optional root.

Reviewers: composition of `chunk` + `contract` + `consistency` + `bones` (for chapters with bones) scoped to the subtree.

Full review sweep at and below root. Defaults to whole series.

### `feedback <feedback-file> [<root-slug>]`

Target: feedback file + optional root.

Reviewers: audience + auditor, dispatched with the named feedback file as context.

Use case: "review s01 against the notes I left in `active-project/feedback.md`."

Lift basis: `design/shoot-v2/audience-review-originals-v2.md` workflow.

### `staging <chapter-slug>` (URI-REVIEW-STAGING — the additive editorial pass)

Target: chapter slug. Precondition: `draft/<book>-<chapter>.md` exists (chapter stitched).

Reviewers: auditor + dramatist, graph-aware (read the assembled draft + the chapter's bones + scene chunks + `event_map[]`).

**Why it exists.** Every editorial motion in the pipeline is subtractive — `/and-stitch` routes only to `CUT` / `CUT-CLAUSE` / `CUT-ASININE` / `CUT-HOLLOW` / `CUT-BONE` / `RESHOW` / `REWORD` / `SIMPLIFY-PUNCT`. A pipeline whose only editorial verbs cut and compress monotonically thins prose and certifies the thinnest survivable version as clean. `staging` is the one pass whose verbs *add*. It does not edit the draft — it cannot (the bone-faithfulness fence forbids the stitcher adding content, and this command is post-hoc). It produces findings that route back to `/and-write revise` as decomposition signals.

What it reviews — finding verbs (the additive counterpart to the stitcher's cut verbs):
- `EXPAND` — a beat the draft compressed past legibility; the bones need more decomposition here.
- `GROUND` — an abstract / nominalized stretch with no physical or sensory anchor; the scene needs grounding bones (see also the sensory-grounding ownership rule).
- `STAGE` — an event narrated as already-over or glossed in the abstract; it needs to be staged as an on-page causal sequence.
- `NEEDS-BEAT` — a causal gap: the draft jumps from state A to state C with no B; a bridging bone is missing.

Output: classified findings at `staff/reviews/staging-<chapter>-<timestamp>.md`. Findings are SIGNAL-class (non-blocking — `/and-review` never blocks), surfaced with a fix-queue offer for `/and-write <chapter> revise`. The `/and-stitch` Phase 9 terminal gate fires this subcommand's reviewer routine alongside the cold-read.

Lift basis: net-new under the b01c02 postmortem (the pipeline had no additive editorial motion).

### `verdict <book-slug>`

Target: book slug.

Reviewers: orchestrator-critic (`staff/orchestrator-critic/card.md`, version per `project.staff.orchestrator_critic`).

**Phase 0 HARD-aborts if:**
- (a) The book has no `chunk`, no `drama`, or no `chapters[]` populated.
- (b) Any chapter under the book is missing `chunk`, `dramatic_shape`, `scenes[]`, or any scene is unsubstanced (missing `substance_delta` or `scene_conflict`).
- (c) Any chapter under the book has no `bones_file` recorded or that file does not exist on disk, or any scene under any chapter has empty `bones[]`.
- (d) The orchestrator-critic card version recorded in `project.staff.orchestrator_critic` is missing from the library.

On pass, dispatches the critic against:
- Chunks at every level under the book (book chunk + chapter chunks + scene chunks).
- Bones files for every chapter under the book: `[theater/bones/<book-slug>-<chapter-slug>.md for chapter in books[<slug>].chapters]`.
- Per-chapter facet outputs at `theater/facets/<facet>-<book-slug>-<chapter-slug>.md` for each chapter.
- Rendered prose at `draft/<book-slug>-<chapter-slug>.md` only if the `prose` spot-check is enabled (default: skip — `prose` subcommand is deferred).

Verdict: PASS / PASS-WITH-NOTES / FAIL.

Persisted to:
- `books[<slug>].orchestrator_critic_verdict.{ruling, report_path, verdict_at, stale_since: null}`.
- Report at `staff/reviews/verdict-<book-slug>-<timestamp>.md`.

**Stale-clear rule:** re-running `verdict` clears the existing `stale_since` flag on PASS/PASS-WITH-NOTES/FAIL re-issue.

**Resume-condition:** Phase 0 warns (not blocks) if it sees an existing stale verdict.

**Lift-source mapping (Hole G).** The lift target is `/and-season.md` Phase 6 (lines 577-609) with per-field rescoping:

| `/and-season.md` Phase 6 reference | New target under `/and-review verdict <book-slug>` |
|---|---|
| `seasons[<slug>].orchestrator_critic_verdict.*` | `books[<slug>].orchestrator_critic_verdict.*` |
| "per-episode bones files for the season" | `[theater/bones/<book-slug>-<chapter-slug>.md for chapter in books[<slug>].chapters]` |
| "season plan" | book chunk + per-chapter chunks + book drama + book substance_delta |
| "per-episode tens / facet outputs" | per-chapter facet outputs at `theater/facets/<facet>-<book-slug>-<chapter-slug>.md` |
| Verdict report path (was `staff/orchestrator-critic/verdicts/<season-slug>-<timestamp>.md`) | **canonical:** `staff/reviews/verdict-<book-slug>-<timestamp>.md` |
| "drafts" if read | per-chapter `draft/<book-slug>-<chapter-slug>.md`; default skips draft-reading (prose subcommand DEFERRED) |
| Phase 0 abort precondition "all episodes under the season are protolined + faceted" | all chapters under the book have `status >= bones-written` (facet-completion not required for verdict; absence recorded as SIGNAL) |

### `prose <chapter-slug>` — DEFERRED

Target: chapter slug.

Reviewers: audience + auditor.

What it would review: felt-substance per scene + `SUBSTANCE-COVERAGE` audit on rendered prose.

**Not implemented in this overhaul.** Listed here so the eventual subcommand has a home. Un-defer lift target pre-pinned: `archive/commands/and-wrap-polish-deferred.md` Phases 1 (audience review) + 2 (8-class auditor pass).

Invoking `/and-review prose <chapter>` prints:

```
/and-review prose is DEFERRED under the substance overhaul.

Polish concerns are deferred entirely until the upstream chain (project → series → substance → cast → substance recursive → write → facets → stitch → draft) is proven end-to-end. /and-stitch's draft/<chapter>.md is the current deliverable.

Un-defer lift target: archive/commands/and-wrap-polish-deferred.md Phases 1-2.
```

---

## Relationship to inline reviews

Authoring commands have inline review *gates* that catch problems before persistence:
- `/and-substance` Phase 5 — substance contracts.
- `/and-write` Phases 5 (continuity) + 6 (substance bone-gate).
- `/and-cast` Phase 5 — series-level audit checkpoint.

`/and-review` is **post-hoc** — fires AFTER persistence. Never blocks an authoring command's own flow. Same reviewer infrastructure shared.

The inline gates can call into the same review subroutines `/and-review` dispatches. Subroutines are owned by the existing reviewer agents; this command is a router.

---

## `/and-cast` Phase 5 vs `/and-review tree --series-scope`

The series-level audit checkpoint inside `/and-cast` is a **synchronous blocking gate** — on FAIL it halts before persisting cast handoff. `/and-review` is post-hoc — fires after persistence, never blocks. They share auditor infrastructure but are not interchangeable. Keep the inline auditor fork inside `/and-cast` Phase 5; use `/and-review tree` for later spot-checks.

---

## Report format

Every persist phase writes `staff/reviews/<subcommand>-<target>-<timestamp>.md` per `schemas/audit-report.schema.md`. Verdict subcommand writes the orchestrator-critic verdict format documented in `staff/orchestrator-critic/card.md`.

Print summary to user:

```
/and-review <subcommand> <target>: <PASS|PASS-WITH-NOTES|FAIL|N findings>

  HARD: <N> (<class-list>)
  SIGNAL: <N> (<class-list>)
  TASTE: <N> (<class-list>)

Report: staff/reviews/<subcommand>-<target>-<timestamp>.md

[Optional fix-queue offer for the appropriate revise command if HARDs > 0]
```
