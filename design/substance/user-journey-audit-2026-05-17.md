# User-Journey Audit — Plan Walkthrough from New-Project Start

**Source:** Read of `design/substance/plan.md` (post-Holes-2026-05-17 pass, commit `6fed2fc`) through the lens of a user about to execute a new project end-to-end.
**Status:** NEW. Surface for triage.
**Lens:** What does the user type next? What do they see? Where do they trip? This audit is strictly about user-facing surface — implementation-level concerns are covered by prior audits (`audit-findings.md`, `bones-facets-compatibility.md`, `plan-holes-2026-05-17.md`).

---

## Imagined run-through

A user starting a fresh project with the new chain would, per the plan's Pipeline-restructure ASCII diagram, type roughly:

```
/and-project <slug> "<brief>" <aud1> <aud2> <aud3>
/and-series
/and-substance series
/and-cast
                                ← [series-level audit checkpoint]
/and-substance book b01
/and-substance chapter b01c01
/and-write b01c01
/and-facets b01c01
/and-stitch b01c01
                                ← loop chapter b01c02, b01c03, ...
/and-review verdict b01
                                ← repeat for b02, b03, ...
```

Walking each step against the plan as written, eleven user-facing friction points and four flat blockers surface. They are mechanically small and would be cheap to spec but they will eat a session each if hit cold.

---

## BLOCKER — user cannot proceed without further spec

### B1 — `/and-project` argument shape is under-specified for the new chain

**Current spec.** Plan §"Command specs"→`/and-project`: "Three jobs only: scaffold, project scope, staff selection (audience ×3 + screen-writer / dramatist / auditor / editor / orchestrator-critic library defaults bound to this project)."

**What's missing.** CLAUDE.md today documents the invocation as `/and-project <title-slug> "<brief>" <audience-1> <audience-2> <audience-3>`. Under the new chain `/and-project` ALSO binds screen-writer / dramatist / auditor / editor / orchestrator-critic — five additional staff slots. The plan does not say whether these are:
- (a) positional args after the audience trio (`/and-project <slug> "<brief>" <a1> <a2> <a3> <sw> <dr> <au> <ed> <oc>` — nine positional args),
- (b) interactive prompts (Phase 1.5 brief-expansion-style),
- (c) library-default-only (user never picks; CLAUDE.md unchanged; plan's "library defaults bound to this project" means the command auto-picks),
- (d) some hybrid (audience positional, other-staff library-default + override flag).

**Why it's a blocker.** The first command the user types in a fresh project must work. Without the argument shape, the user either guesses wrong (silent default they didn't want) or guesses too wide (slash-command parse error).

**Recommended resolution.** Plan should state explicitly: `/and-project <title-slug> "<brief>" <audience-1> <audience-2> <audience-3> [--screen-writer <slug>] [--dramatist <slug>] [--auditor <slug>] [--editor <slug>] [--orchestrator-critic <slug>]` — three positional + five optional flags, all defaulting to library-default. Add the same syntax line to CLAUDE.md's Commands table.

### B2 — Substance questionnaire (1–9 axis ranking) has no specified user-flow

**Current spec.** Plan §"New artifacts"→`design/substance/questionnaire.md`: "1–9 archetype questionnaire (story / protagonist / world / antagonist) used by `/and-substance` at any level to pin axis ranks honestly. Per-archetype question banks. Example scoring trace."

**What's missing.** The questionnaire is referenced as a framework but its user-flow ownership is unstated. When `/and-substance series` Phase 4 authors the series signature (state axes + 1-9 anchors per axis), does it:
- (a) interactively prompt the user through each axis × archetype (potentially 30+ questions),
- (b) hand the questionnaire to the screen-writer agent which infers rankings from the series chunk + project brief (no user input),
- (c) the user fills out a YAML stub the command pre-emits, then runs `/and-substance series` again to consume it,
- (d) the user reads the questionnaire doc and types their answers as one prose block at a Phase-4 prompt.

**Why it's a blocker.** This is the substance-overhaul's central authoring loop. If the questionnaire's user-flow is wrong, the signature is wrong, and every downstream chunker reads the wrong constraints. The "Triggering notes" line 7 ("1–9 scale questionnaire on protagonist state (and world, and antagonist, and story)") is the user's own framing — they will expect to actually be asked questions.

**Recommended resolution.** Spec `/and-substance series` Phase 4 explicitly. Recommended: option (b) with override — the screen-writer agent proposes per-axis 1-9 ranks from the series chunk + brief; Phase 5 review surfaces the proposal to the user for one accept-or-edit pass; user can rewrite any rank inline before persistence. Avoids 30+ prompts but keeps human in the loop. Document the trace in `questionnaire.md`.

### B3 — Series-level audit checkpoint approval mechanic isn't specified

**Current spec.** Plan §"Command specs"→`/and-cast` Phase 5: "Auditor (fork) against full picture... Result to user. On approval, `/and-substance book b01` next."

**What's missing.** What does the user actually do to "approve"? Options the plan does not pick between:
- (a) `/and-cast` Phase 5 ends with a Y/N prompt; on Y, command persists `project.audit_approval: <timestamp>` and exits; user then runs `/and-substance book b01` manually,
- (b) approval is implicit — `/and-substance book b01` Phase 0 just looks for `series.cast_roster` populated and assumes audit passed,
- (c) explicit slash command (`/and-approve series` or similar) the user types,
- (d) approval is a free-text reply the user gives after `/and-cast` reports findings; the command interprets the reply.

**Why it's a blocker.** Plan rule 7 says "Human checkpoints: series-level audit only." This is THE human checkpoint of the whole pipeline. If the mechanic isn't spelled out, the user either skips it (fails to enforce) or stalls waiting for the command to ask (fails to advance).

**Recommended resolution.** Pick (a): `/and-cast` Phase 5 ends with a Y/N prompt; on Y, persist `project.series_audit.approved_at: <iso-timestamp>` + `approved_by: user` to showrunner memory and exit cleanly with "next: `/and-substance book b01`" printed. On N, user types feedback inline and `/and-cast revise` re-runs against the feedback. `/and-substance book b01` Phase 0 hard-aborts if `project.series_audit.approved_at` is missing.

### B4 — User-facing run book is missing

**Current spec.** Plan §"Pipeline restructure" has an ASCII flow diagram. CLAUDE.md will get an updated Commands table.

**What's missing.** A user-facing "type these commands in this order, expect these prompts, here are sensible defaults" walkthrough. The plan reads as implementer specs; nowhere is there a one-page "if you're starting a project, do this." Equivalent of a README quickstart.

**Why it's a blocker.** First-time use will require the user to read the entire plan to assemble the sequence. The plan is 800+ lines.

**Recommended resolution.** Add `design/substance/run-book.md` (or as a new section in `README.md`): linear command sequence, one section per command with the literal invocation + expected prompts + recommended defaults + "exit-state means next command is" hand-off line. ~80-120 lines of pure user-facing content. Trivial to author from the existing command specs in the plan.

---

## FRICTION — user proceeds but stumbles

### F1 — `/and-substance --cascade` stops at bones; user mental-model expects "drive to draft"

**Current spec.** Plan §"`--cascade` flag (book/chapter levels)": "With `--cascade`, `/and-substance book b01` auto-fires `/and-substance chapter` for each chapter under b01, then `/and-write` for each chapter."

**The trip.** A user typing `/and-substance book b01 --cascade` and walking away will expect to come back to `draft/b01-c01.md` ... `draft/b01-c0N.md`. They will come back to bones files only — `/and-facets` and `/and-stitch` are NOT in the cascade.

**Recommended resolution.** Either (a) extend `--cascade` through `/and-facets` + `/and-stitch` (consistent with user mental-model), with checkpoint flushes at each chapter completion, OR (b) keep the current scope but rename the flag to `--cascade-bones` (signals the bones-only boundary) and add a separate `--cascade-draft` flag that goes the full way. Recommendation: (a) — checkpoint after each `/and-stitch` completion; resume re-fires from the next chapter's `/and-substance chapter`. Document in the `--cascade` subsection.

### F2 — `/and-cast revise` actor-selection mechanic isn't specified

**Current spec.** Plan §"`/and-cast`" Phase 0: "prompt `revise` (swap/add/retire — untouched actors are preserved as-is; added actors flow through Phases 1–4 normally; retired actors are decommissioned by margit...)."

**The trip.** The user picks `revise` mode. Then what? Does the user type slugs at an interactive prompt (`retire: maya, add: tomas`)? Does the screen-writer agent re-read the brief and propose changes? Are there flags (`/and-cast revise --retire maya --add tomas`)?

**Recommended resolution.** Spec the interactive flow: Phase 0 prints the current roster; user enters three lists (retire / add / swap) at a single multi-line prompt; remaining phases scope to the delta. Add a `--retire <slug>` / `--add <slug>` / `--swap <old>=<new>` flag-form for scripted use.

### F3 — `/and-write revise --from-signals` requires knowing SIGNALs exist

**Current spec.** Plan §"Re-runnability edge cases (F1)": "`/and-write revise` mode accepts a `--from-signals` flag (or, by default at Phase 0, prompts the user when SIGNAL findings are present): list the SIGNAL-flagged bones / scenes, offer to re-decompose only those."

**The trip.** A user who finished `/and-write b01c01` and saw bones emit successfully will not know SIGNALs accrued in `chapters[].scenes[].bones[].gate_verdict.signals[]`. There's no surface that says "you have 3 SIGNAL findings open on b01c01." When they re-run later in the next session, the Phase 0 prompt picks up — but if they decide "this chapter feels off" they have no surface to discover the SIGNALs by name without grepping memory.

**Recommended resolution.** `/and-review bones <chapter-slug>` (existing subcommand) should report SIGNAL findings as part of its standard output, with the explicit suggestion "to revise, run `/and-write <chapter> revise --from-signals`." Also: `/and-write` Phase 7 emit-summary line should print "N SIGNAL findings recorded; see `/and-review bones <chapter>` to inspect" on completion.

### F4 — `/and-cut` ↔ resume mechanic is implicit

**Current spec.** Plan §"Re-runnability edge cases (F2)": Cascade-checkpoint schema includes `next.command` field. `/and-cut` writes `reason: halted-on-cut`.

**The trip.** Plan doesn't say `/and-cut` prints the resume command. User comes back next session, runs `/and-cut` again to remind themselves where they were? Or are they supposed to remember the cascade-checkpoint file path?

**Recommended resolution.** `/and-cut`'s exit summary (per the existing skill description: "prints a clean 'you are here' summary") prints the literal resume command from `next.command` field. Cross-reference in plan §"Re-runnability edge cases" subsection F2.

### F5 — `/and-review` subcommand discovery

**Current spec.** Plan §"`/and-review`" lists 12 subcommands in a table.

**The trip.** User types `/and-review` with no args. What happens? Plan doesn't say. Options: (a) parse error; (b) prints subcommand list + usage; (c) interactive subcommand picker.

**Recommended resolution.** (b) — bare `/and-review` prints the subcommand table + one-line usage hint per subcommand. Cheap.

### F6 — `/and-series` Phase 1 has 7 interactive prompts and no defaults

**Current spec.** "Interactive: book count, book length (chapters per book + scenes per chapter + bones per scene), cyclical?, POV, cross-book continuity, world evolution, series-end shape."

**The trip.** User answers seven prompts cold. Some have natural defaults (`scenes_per_chapter: 1-3` per plan; `bones_per_scene: 5-15` per plan; `cyclical: false`; `world_evolution: evolving`). Others don't (`book_count`, `pov`, `series_end_shape`, `cross_book_continuity`).

**Recommended resolution.** Each prompt offers a default in brackets (`[1-3]`, `[5-15]`, `[false]`, `[evolving]`, etc.); the user presses enter to accept. No-default prompts (`book_count`, `pov`, `series_end_shape`) are required entries. List the defaults explicitly in the `/and-series` Phase 1 spec or in `delta-targets.md`.

### F7 — First-chapter `handoff_in` flow isn't shown

**Current spec.** Schema: "`source_chapter: <prior-chapter-slug> | null — null only for the first chapter of the first book.`" `/and-substance book` Phase 5 dramatist verifies adjacent-chapter consistency.

**The trip.** What populates the first chapter's `handoff_in`? Conceptually it's "empty + whatever the user wants the world to look like at chapter 1 open." Authored from the project brief? From `books[b01].drama`? Left empty?

**Recommended resolution.** Spec: `/and-substance chapter b01c01` Phase 3, when `source_chapter` resolves to null, populates `handoff_in` from `series.substance.state_axes[].start_rank` (the project's literal starting state) + an empty `open_threads` list. Dramatist Phase 5 cross-check skips the first-chapter pair. Document this fallback in the schema YAML comment.

### F8 — `--cascade` warning surface vs. checkpoint payload

**Current spec.** Plan §"Surfacing — defined" prints downstream artifacts + offers stale-mark options. Plan §"F2" cascade checkpoint records `reason: halted-on-failure`. These are two different surfaces.

**The trip.** When `--cascade` fails mid-way on a chapter, does the user see surfacing prose AND a checkpoint write? Or does the cascade halt silently with only the checkpoint? User won't know whether to look in shell output or in `cascade-checkpoint.md`.

**Recommended resolution.** Spec: on cascade failure, the user sees (a) the failing command's normal failure output, (b) a "cascade halted — checkpoint written to `staff/showrunner/cascade-checkpoint.md`; resume with `/and-substance <root> --cascade --resume`" line. The checkpoint file is for the command to resume; the shell line is for the user to act.

---

## GAP — implementer has to guess but probably converges

### G1 — Chapter status reset on partial revise

**Current spec.** Plan §"`chapters[].status` enum": "Re-running a command that has already advanced past its own status... Phase 0 of the re-running command resets status to the earliest value it owns." Plan §"F3" says per-scene gate_verdict clearing only.

**The gap.** A `stitched`-status chapter where the user `/and-write revise --from-signals` patches two scenes — does chapter status drop to `bones-written` (because bones changed)? If so, `/and-facets` and `/and-stitch` need to re-run for the chapter to ship — implicit cascade not spelled out.

**Probable resolution.** Yes, status drops to `bones-written` (any bone change invalidates downstream); staleness cascade marks the facets + draft stale; user re-runs `/and-facets` + `/and-stitch` to advance. Spell this out in the status enum subsection.

### G2 — Re-run mode syntax: positional arg or Phase 0 prompt?

**Current spec.** Throughout the plan, re-run modes are written as both `/and-write b01c01 revise` (positional) and as Phase 0 interactive prompts. Inconsistent.

**Probable resolution.** Support both: `/and-write b01c01` (Phase 0 prompts mode) and `/and-write b01c01 revise` (mode preselected, Phase 0 skips the prompt). Same shape for all re-runnable commands. Document in the shared `rerun-protocol.md`.

### G3 — Book/chapter slug auto-generation timing

**Current spec.** Schema YAML shows `books[].slug: b01`, `chapters[].slug: b01c01`. No explicit "who assigns these."

**Probable resolution.** `/and-substance series` Phase 6 persist generates book slugs `b01`...`bN` from `series.structure.book_count`. `/and-substance book b01` Phase 6 generates chapter slugs `b01c01`...`b01cM` from `books[b01].structure.chapter_count`. `/and-substance chapter b01c01` Phase 6 generates scene slugs `b01c01s01`...`b01c01sP`. Mechanical; should be stated in each command's persist phase.

### G4 — `cost_ledger` scene-anchor refinement: who, when

**Current spec.** Plan schema: "`cost_ledger[].anchor.{book, chapter, scene}` — fine-grained anchor; populate from the level where the cost is paid... Authored top-down: `/and-substance series` writes book-anchored entries; `/and-substance chapter`/`scene` may refine them by populating the deeper fields."

**The gap.** `/and-substance scene` does NOT exist (scenes are produced by `/and-substance chapter`, decomposed by `/and-write`). So "scene"-level cost-anchor refinement has no owner.

**Probable resolution.** `/and-substance chapter` Phase 3 (per-scene chunk authoring) refines scene-level anchors when a per-scene `substance_delta.cost` is paid by a specific scene. Document this explicitly in `/and-substance chapter` Phase 3.

### G5 — `/and-project` staff-field defaults vs. interactive selection

**Current spec.** "Staff selection (audience ×3 + screen-writer / dramatist / auditor / editor / orchestrator-critic library defaults bound to this project)."

**The gap.** Are non-audience staff slots always library-default, or can the user override? The schema shows `<persona-or-default>` for each, suggesting override is possible.

**Probable resolution.** Library-default unless user passes the override flags from B1. Document in `/and-project` spec.

### G6 — `staff/reviews/` directory creation

**Current spec.** `/and-review` writes reports to `staff/reviews/<subcommand>-<target>-<timestamp>.md`.

**The gap.** Who creates `staff/reviews/`? `/and-project` Phase 1 scaffold doesn't list it in directory-tree output (because the directory-tree write-up doesn't enumerate the post-overhaul tree).

**Probable resolution.** Add to `/and-project` Phase 1 scaffold list. Add to plan §"Directory map" CLAUDE.md update.

### G7 — `/and-substance --cascade` invocation precondition

**Current spec.** "With `--cascade`, `/and-substance book b01` auto-fires..."

**The gap.** Can the user pass `--cascade` to `/and-substance chapter b01c01`? Plan says "book/chapter levels" — cascading from a single chapter to `/and-write` for that one chapter is degenerate (one chapter). Probably a no-op or a thin convenience. Not spelled out.

**Probable resolution.** `/and-substance chapter b01c01 --cascade` = `/and-substance chapter b01c01` + `/and-write b01c01` (+ `/and-facets b01c01` + `/and-stitch b01c01` if F1 resolves toward full cascade). Trivial convenience; document.

---

## Suggested resolution order

1. **B1-B4 first.** These are the four flat blockers. Combined plan-edit cost: ~80-100 lines (mostly user-facing surface, no design changes). Without them, the first session of the first project will halt.
2. **F1-F8 next.** Friction items; each is a ~10-30 line spec extension. F1 (cascade scope) is the largest decision; F2-F8 are mechanical.
3. **G1-G7 last.** Gaps the implementer will converge correctly on without spec; recommended to document for the record but not blocking.

Total plan-edit estimate for full resolution: ~250-300 lines added (mostly to existing sections; one new doc — `design/substance/run-book.md` — for B4).

---

## Notes on what's not in this audit

- **Implementation correctness.** Covered by `audit-findings.md` (RESOLVED) and `plan-holes-2026-05-17.md` (RESOLVED).
- **Substance design.** Covered by `intent-gaps.md` (RESOLVED).
- **Bones-facets compatibility.** Covered by `bones-facets-compatibility.md` (RESOLVED).

This audit is strictly: *"if I open the terminal and type, will the next 30 minutes be productive?"*

The answer today is "no, I'll be stuck on B1 within five minutes."
