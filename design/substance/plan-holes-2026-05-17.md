# Plan Holes — Reuse-Pass Review

**Source:** End-to-end review of `design/substance/plan.md` post-reuse-mutation (commit `92bffd8`), 2026-05-17.
**Status:** RESOLVED 2026-05-17 (plan-holes pass). Holes A–D, F–H applied as plan edits; Hole E user-ruled split (carve in #4 #6 #10; OOS-track #5 #7 #8 #11) applied. See plan.md "Plan-holes pass 2026-05-17" revision marker in the header.
**Companion docs:** `audit-findings.md` (RESOLVED), `bones-facets-compatibility.md` (RESOLVED), `intent-gaps.md` — items 4-8, 10, 11 disposition decided here per Hole E split: #4 #6 #10 carved into plan; #5 #7 #8 #11 listed under plan.md "Out of scope" with explicit follow-on tracking.

---

## Summary

The reuse-pass plan revision (commit `92bffd8`) successfully reframes ~55-60% of the substance overhaul as lift-and-adapt rather than net-new. But the end-to-end pipeline trace surfaces eight categories of holes that need resolution before implementation:

- **A-D, F-H** — mechanical / spec gaps. Tractable in plan-revision; ~half-day of careful editing during implementation.
- **E** — intent-gaps OPEN items 4-8, 10, 11 (re-surfaced). Bigger swallow: each is either scope-add, OOS-tracked-with-followon, or accepted-defect-with-explicit-decision. Needs user input on disposition.

**Headline risk if not resolved:** the new chain is structurally better on substance (user's #1 complaint) but at parity-or-worse on rendering quality and cross-chapter coherence — the specific complaints the user flagged about s01e02 and s01e03 are unaddressed. First chapter shipped through the new chain may still exhibit the dialogue-mashed-together and "barely fit together" problems.

---

## Hole A — Path-rename impact on `/and-facets` and `/and-stitch` is under-spec'd

The plan moves bones from `theater/proto-lines/<slug>.md` to `theater/bones/<book>-<chapter>.md`. Downstream commands have not been updated for the new path.

**Concrete edits needed:**
- `.claude/commands/and-facets.md:73-84` Phase 0 step 1 — reads `proto-lines/<slug>.md`; update to `bones/<book>-<chapter>.md`. Plus all references to `_inflight/` paths under that tree.
- `.claude/commands/and-stitch.md:81` Phase 0 step 1 — same.
- `schemas/proto-line.schema.md:9-17` (post-rename: `bones.schema.md`) — currently documents 3 path conventions (per-episode, per-chapter, season-aggregate). Add a 4th: per-chapter book-scoped `<book>-<chapter>.md` (e.g. `b01-c01.md`). Or rationalize to one canonical convention.
- Facet output paths (`<facet>.md`, `<facet>-<character>.md`) and the cite-index (`_cite-index.md`) — does each chapter get its own subdirectory under `theater/facets/<book>-<chapter>/`? Or do paths stay flat with `<facet>-<book>-<chapter>.md` naming? **Convention not specified. Decide and document.**

**Plan edits:** add a path-rename row to both the `/and-facets` light-mutation list and the `/and-stitch` light-mutation list under "Pipeline restructure" / "Command specs." Add a facets-output-path-convention subsection.

---

## Hole B — `/and-facets` Phase 0 step 4 hard-aborts on missing tens

`.claude/commands/and-facets.md:80` — *"Locate `tensometer-<season-slug>e<NN>.md`. Copy/rename to `tensometer.md` as the working surface. **Abort with the resolution path if missing** — facets cannot run without the bone-gate tens output."*

Plan removes tensometer entirely. This step needs explicit removal, not just R1-rubric input edits. The plan's "/and-facets light mutation" section mentions R1 input changes; it should also enumerate Phase 0 step 4 deletion.

**Plan edits:** add bullet to `/and-facets` light-mutation list: "Phase 0 step 4 (tens-precondition abort) removed alongside tens-fanout drop."

---

## Hole C — Showrunner memory has no chapter-status enum

`schemas/showrunner-memory.schema.md:48` declares `episodes[].status: written | active | planned | protolined`. Plus extended statuses are state-machine markers in `/and-facets:74-78` (`faceted-r1`, `faceted-r2`, `audited-r1-mechanical`, `audited-r1`) and `/and-stitch:100` (`stitched`).

Plan dissolves "episode" but doesn't define the chapter-status equivalents:
- `chapters[].status: planned | bones-written | faceted-r1 | faceted-r2 | audited-r1-mechanical | audited-r1 | stitched | wrapped`?
- Resume-point detection in `/and-facets` Phase 0 and `/and-stitch` Phase 0 reads these markers; transitions need to be valid for chapters.

**Plan edits:** add `chapters[].status:` to the schema YAML in plan.md "schemas/showrunner-memory.schema.md (updated)" subsection. Enumerate the enum values. Add to Verification on completion checklist.

---

## Hole D — Pass briefs in lifted `/and-protolines-v2` read inputs that don't exist in the new chain

Verbatim lift of Passes 1-5 won't run because input shapes change. The asset-reuse map says "lift Passes 1-5 verbatim" — true for the dispatch shape and SVO discipline, **not** for the input lists.

**Per-pass adaptations needed:**

| Pass | Currently reads | Needs to read under new chain |
|---|---|---|
| Pass 1 (inventory) | `theater/episode-plan.md` chunk/change/theme/actors/constraints | scene chunks + substance contracts + scene_conflict from `chapters[].scenes[]` in showrunner memory |
| Pass 3 (shape) | `series-plan.md` + `season-s01-plan.md` (season escalation spine) | `series.substance` + `books[<slug>].substance_delta` + `chapters[].dramatic_shape` + `chapters[].goal` |
| Pass 4 (trim) | `active-project/staff/studio/vibes.md` + per-actor vibes | series + book vibes only (chapter/scene/bone vibes deprecated per plan vibe-cloud decision); studio vibes? — needs ruling |
| Pass 5 (continuity) | within-episode state-thread | within-chapter state-thread + (per Gap 6, possibly) cross-chapter handoff |

**Plan edits:** add a "Pass input adaptations" subsection under the `/and-write` Asset reuse map table. Enumerate per-pass input swaps. Also flag: forbid-loading lists in each pass — do they continue to forbid loading other chapters' bones files? Probably yes; state it.

---

## Hole E — Intent-gaps OPEN items still unresolved

From `intent-gaps.md`, items 4-8 and 10-11 were flagged OPEN and the prior audit said they "need to be addressed before implementation." None have been resolved in the reuse-pass revision.

**Re-surfaced for decision:**

| # | Gap | User feedback source | Disposition needed |
|---|---|---|---|
| 4 | Stitcher rendering: speaker-paragraph breaks + scene-callout suppression | s01e02: "everything smashed together. New lines for different speakers." / s01e03: "calling out scenes breaks immersion." | **Carve into /and-stitch narrow patch** (separate from substance overhaul) OR **explicit OOS-tracked** with a follow-on issue. NOT addressable by "polish deferred" — user said prose is decent; these are rendering bugs. |
| 5 | Absolute length floor | "All episodes too short" + "Way too short. What even was the point?" | Add `chapter_word_count_floor` to `series.structure.book_length`. Verified at `/and-stitch` Phase 8 or estimated at `/and-write` Phase 6 via bones-count × words-per-bone. **Decide: in-scope or OOS-tracked?** |
| 6 | Cross-chapter handoff | "Episodes barely fit together. Relay bugs appear for no reason." | Add `chapters[].handoff_in:` / `chapters[].handoff_out:`. `/and-substance book` Phase 5 dramatist verifies N+1 inherits from N. `/and-review consistency` adds cross-chapter sweep. **Decide: in-scope or OOS-tracked?** |
| 7 | Emotional-substance orthogonal to plot-substance | s01e01: "Should be harsh feels with protagonist coming back to life after 3 days." | Two options: (A) require per-chapter Δ to span ≥2 axis classes (one plot + one emotional), tagging axes with class in `state_axes[].class`; (B) audience-fork emotional-resonance check at bone-gate when stakes-events present, `SUBSTANCE-EMOTIONALLY-FLAT` HARD. **Decide: in-scope or OOS-tracked?** |
| 8 | Plot-arc-completion | s01e02 + s01e03: "What even was the point of this chapter?" | `/and-substance chapter` Phase 5 dramatist check verifies setup beat + complication beat + resolution-or-cliffhanger beat. Chapter chunk text answers "what changed by the end?" in one line. **Decide: in-scope or OOS-tracked?** |
| 10 | Chapter ≈ episode mapping for user mental model | n/a (clarification) | Add to `design/substance/README.md`: "A chapter is the terminal unit of consumption — one chapter ≈ one previous episode (~3000-5000 words, 1-3 scenes)." Cheap. **Recommend: include.** |
| 11 | World-detail consistency | s01e01: "The bowl is weird. Do smallfolk have salt?" | Class/economic-level detail check. Add to `/and-review consistency` as `--world-detail` axis, OR add world-detail-audit step inside `/and-write` Phase 5 continuity. **Decide: in-scope or OOS-tracked?** |

**Recommended split (for user confirmation):**
- **Carve in (do now):** items 4, 6, 10. These are the closest to triggering-feedback substance and the cheapest to add. Item 4 is the biggest risk if punted — the very first new-chain chapter will exhibit the s01e02 problem.
- **OOS-tracked with follow-on:** items 5, 7, 8, 11. Each warrants its own design pass; bundling them with the substance overhaul will stretch scope. Acceptable to defer with explicit acknowledgement that they're known shipped-defects against user feedback.
- **Open question for user:** confirm this split or rebalance.

---

## Hole F — Re-runnability ambiguities

Three sub-items:

1. **`/and-write revise` "re-decompose specific scenes flagged SIGNAL"** — Phase 6 classifies SIGNAL findings as records-but-passes. What surface escalates a SIGNAL into a revise trigger? `/and-review bones` re-fire? Explicit fix-queue from `/and-review`? Plan doesn't connect.
2. **`/and-substance --cascade` checkpoint payload** — cascade halts on failure; resume requires a checkpoint schema. Plan says "land in command body, not in this plan." Implementer needs at minimum a sketch: `next: /and-substance chapter b01c05` vs `next: /and-write b01c05` vs `next: /and-substance book b01 --cascade --resume-from b01c05`.
3. **`gate_verdict` partial-revise lifecycle** — cleared at Phase 0 on revise/redo, filled at Phase 6 on PASS. What about per-scene partial-revise where some scenes pass and others fail? Per-scene clear-and-refill, or per-chapter clear all? Decide.

**Plan edits:** add a "Re-runnability edge cases" subsection under "Re-runnability."

---

## Hole G — Asset reuse map lift-source ambiguity (`/and-review verdict`)

The map says `/and-review verdict` lifts `/and-season.md` Phase 6 verbatim. Phase 6 references `staff/orchestrator-critic/card.md` (preserved) and a season-scope output. Rescoping "season" → "book" needs explicit field mapping:

- `seasons[<slug>].orchestrator_critic_verdict` → `books[<slug>].orchestrator_critic_verdict` (already in plan's schema, ✓)
- "per-episode bones files for the season" → "per-chapter bones files for the book" — needs listing
- Verdict report path convention: plan says `staff/reviews/verdict-<book-slug>-<timestamp>.md`; current `/and-season` uses different paths. Pick one, document explicitly.

**Plan edits:** add a "Rescoping table" to the `/and-review verdict` lift specification.

---

## Hole H — `cards/dialects/INDEX.md` reference + behavior rename

`/and-protolines-v2.md:56` Phase 0 step 6 confirms `cards/dialects/INDEX.md` exists. `/and-write` lift should preserve this. But `CLAUDE.md` Agent routing table notes "Directory rename to behaviors/ pending" for dialects/.

**Decide:** rename `dialects/ → behaviors/` in lockstep with the substance overhaul, or leave the lift target using current path. If lockstep, add to Archive plan + CLAUDE.md update set. If deferred, mention in the lifted Phase 0 step that the dialects/ path is current and the rename is a follow-on.

---

## Recommended resolution order (for next session)

1. **User decision on intent-gaps splits (Hole E).** Surface the 7 items + recommended split (carve in 4, 6, 10; OOS-track 5, 7, 8, 11). Get a ruling before further plan edits — these change scope.
2. **Apply Holes A-D as direct plan edits** (path rename, tens-precondition removal, chapter status enum, per-pass input adaptations). These are mechanical; ~1-2 hours.
3. **Apply Holes F-H as direct plan edits** (re-runnability edge cases, `/and-review verdict` rescoping table, dialects→behaviors decision). ~30 min.
4. **Apply user's ruling on E** as plan edits — either spec the carve-ins or document the OOS tracking with follow-on issues.
5. **Re-audit.** A clean re-audit pass that finds no new CRITICAL holes is the green light to start implementation per the Order-of-operations Step 5 (shared protocol docs) and Step 6 (command body writes).
6. **Commit + push** revised plan.

---

## Notes on what was NOT a hole

Confirmed clean during this review:
- Bones file body format preserved → cite-index / body-integrity / citation accrual all work.
- Speech-bone form preserved → URI-DIALOGUE-COVERAGE-GATE works.
- Scene-map facet emitted upstream by `/and-write` Phase 7 → URI-SCENE-WINDOW works; `/and-facets` Phase 4d coverage-validates cleanly; `/and-stitch` Phase 0 step 2a finds the file.
- Five-pass SVO discipline preserved (subject to Hole D adaptations).
- `staff/orchestrator-critic/card.md` consumed unchanged.
- Audience persona library + cards (personas, locations, props, conditions) unchanged.
- Agents (showrunner, screen-writer, coach, impersonator, studio, auditor, fixer, margit, dramatist) reused as-is.
- 7-field bones-file header sourced from `chapters[].pov_narrator` + `chapters[].goal` (authored by `/and-substance chapter` Phases 3, 4).
- Tens-citation prefix removed from recognized list in `bones.schema.md § citation prefixes`.

These are the asset-reuse wins the plan correctly identifies. The holes above are gaps in following through on the reuse claim, not failures of the reuse principle itself.
