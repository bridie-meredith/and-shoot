# Plan Audit Findings — to address next session

**Source:** Self-audit of `design/substance/plan.md`, 2026-05-16.
**Status:** Open. Address before the plan is executed.

21 findings total. CRITICAL (10) must be fixed before any implementation work begins; IMPORTANT (5) need spec before execution; SHOULD-FIX (4) are consistency cleanup; DEFER (4) are worth noting.

---

## CRITICAL — stale references to dropped commands

These will mislead the implementer because they reference commands that no longer exist in the plan.

1. **`plan.md:40`** — Goal section: "the per-chapter bones file that `/and-facets`, `/and-stitch`, `/and-wrap` consume." `/and-wrap` is dropped; remove from the list.
2. **`plan.md:110, :112`** — Boundary table header: "Three commands are being restructured (`/and-project` shrinks, `/and-season` is dissolved, `/and-wrap` extends)." `/and-wrap` doesn't extend — dropped. Count is also wrong (`/and-protolines` is restructured into `/and-write` too).
3. **`plan.md:140`** — Boundary table row "Phase 6 orchestrator-critic verdict | `/and-judge-book <slug>`" — `/and-judge-book` is dropped; reference `/and-review verdict <book>`.
4. **`plan.md:188`** — Archive README placeholder text still says "→ shoot chain → `/and-wrap` (substance-aware)" and doesn't mention `/and-wrap`/`/and-judge-book`/`/and-protolines` dissolution. Needs a full rewrite.
5. **`plan.md:326`** — Schema YAML comment: `# book-level field filled by /and-judge-book` — should be `/and-review verdict`.
6. **`plan.md:431`** — `/and-review` section: "Authoring commands (`/and-substance` Phase 5, `/and-write` Phases 5/6, `/and-wrap` Phases 1/2) still have inline review gates." `/and-wrap` is dropped; reference is stale.
7. **`plan.md:475`** — Out-of-scope says "Tens-gate in URI-026 is replaced by the substance bone-gate at `/and-substance scene` Phase 5." Bone-gate is at `/and-write` Phase 6, not `/and-substance` Phase 5 (which is chunk-quality review, not bone-gate).
8. **`plan.md:485`** — Open question 1 says "`-pre-substance` for `/and-project` + `/and-wrap`" — `/and-wrap` is dissolved, not pre-substance (archive plan uses `-dissolved`). Inconsistent with archive plan.
9. **`plan.md:489`** — Open question 5 still says "Settled on separate `/and-judge-book <slug>` command" — that decision was reversed (absorbed into `/and-review verdict`). Rewrite or remove.

## CRITICAL — schema gaps that block /and-write

10. **`plan.md:260-263`** — `cost_ledger[].anchor: <book-slug>` — but `/and-write` Phase 6 verifies "for each scene under the chapter: cost-ledger entries are paid by visible bones." Cost-ledger needs at least scene-level granularity, not just book. Schema needs `anchor: { book, chapter, scene }` or similar fine-grained anchor.
11. **No chunk-count fields in schema.** Plan says `/and-substance book` produces per-chapter chunks but doesn't specify where the count decision lands. `series.structure.book_length.chapters_per_book` is a range — so each book picks. But schema doesn't show `books[].structure.chapter_count` populated by `/and-substance series`, nor `chapters[].structure.scene_count`, nor `scenes[].structure.beat_count`. Implementer won't know where each chunk-count decision lives.

## IMPORTANT — spec gaps

12. **Vibe-clouds not addressed.** CLAUDE.md's memory rules say "Vibe-clouds are built at each planning level. Series, season, and episode each have a vibe-cloud." With recursive `/and-substance`, do vibes get authored at each level (series/book/chapter/scene/beat)? Deprecated? Plan is silent — implementer has no guidance.
13. **URI-DIALOGUE-COVERAGE-GATE and URI-SCENE-WINDOW** (per CLAUDE.md) are bone-level constraints enforced at `/and-facets`. Plan doesn't say whether `/and-write`'s output structure preserves the `speaks to` bone shape these gates need, or whether `/and-write` should pre-verify before emission to prevent downstream `/and-facets` aborts.
14. **`/and-write` is not just renamed `/and-protolines`.** Existing `/and-protolines` takes an "episode chunk"; new `/and-write` reads per-beat chunks. Different input structure → different prompt construction → not a simple rename. Plan should call this out as substantive overhaul, not just a rename.
15. **`/and-review verdict <book>` Phase 0 validation.** Plan says verdict "fires when both `/and-substance book` and `/and-write` (all chapters) are complete" but doesn't specify Phase 0 abort behavior if chapters are missing bones. Inherited from dropped `/and-judge-book` spec but not re-stated.
16. **Staleness cascade does not invalidate `orchestrator_critic_verdict`.** Re-running `/and-substance` at any level under a book makes the verdict stale; plan doesn't say the verdict block gets `stale_since` marked. Verdict could sit at PASS while substance underneath has been redone.

## SHOULD-FIX — terminology + Phase clarifications

17. **"Four levels" vs "five levels" disambiguation.** `/and-substance` "fires at four levels (series / book / chapter / scene)" (line 359), but the chunk hierarchy is "five levels (series → book → chapter → scene → beat)" — beats are chunks produced but not invoked. State explicitly: 5 chunk levels, 4 invocation levels.
18. **`/and-cast` Phase 5 inline auditor fork vs `/and-review`** (plan.md:382). `/and-review` now exists; should this checkpoint use `/and-review tree --series-scope` for consistency, or keep the inline auditor fork? Pick one and document the rationale.
19. **Staleness "surfacing" is vague** (plan.md:165, :168). What does "surfaced" mean? Print warning? Block run? Force review? Define behavior under staleness.
20. **`/and-cast revise` mode** (plan.md:377): "swap/add/retire — preserves untouched actors" doesn't say whether new actors get fresh margit Phase 4 provisioning (LTM/STM/state/vibes) or skip. Specify.
21. **CLAUDE.md update plan is thin** (plan.md:467). Misses Rule 11 (URI-026 shared reviewer resources with tens-rubric), Memory rules (vibe-clouds), directory map (`theater/proto-lines/` → `theater/bones/`), pipeline-summary text, and the `/and-wrap`/`/and-judge-book`/`/and-protolines*` rows that need removal. Enumerate the full CLAUDE.md change set.

## DEFER — worth noting

- **Dispatch budget concern.** Naive estimate: 6 books × 6 chapters × 4 scenes × 5 beats with per-level Phase 5 reviews (audience ×3 + dramatist + auditor) × up to 3 retries ≈ 3000+ subagent dispatches per series. Worth a sizing note + possibly a dispatch-budget open question (parallelize? cap retries lower? batch reviews?).
- **No `/and-cut` interaction notes.** Long `--cascade` runs would benefit from explicit checkpointability.
- **Filesystem migration** (`theater/proto-lines/` → `theater/bones/`) not explicit. Current active project (flea-bottom-dance) is out-of-scope, but worth one line confirming old projects keep their layout.
- **Estimated sizes are loose** (`/and-substance` ~400-500 lines might be optimistic given recursive 4-level + 7-phase + reviewers + cascade flag).

---

## Suggested fix order next session

1. Apply CRITICAL fixes (#1–#11) — single revision pass through the plan.
2. Spec the IMPORTANT gaps (#12–#16) — may require user input (vibes? gate behavior?).
3. Apply SHOULD-FIX consistency edits (#17–#21).
4. Add an "open question" or note for each DEFER item.
5. Re-audit. Commit + push the cleaned plan before any implementation.
