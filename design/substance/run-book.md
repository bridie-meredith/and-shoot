# Run Book — Executing a New Project End-to-End

**Audience:** the user, executing a fresh project under the substance-overhaul chain. Not the implementer.
**Scope:** one project, from terminal-open to first finished book draft.
**Companion:** `design/substance/plan.md` (the full design); `design/substance/README.md` (substance framework reference); `design/substance/delta-targets.md` (the default bands you'll be accepting at prompts); `design/substance/questionnaire.md` (the rubric the screen-writer uses while proposing your signature).

Read once before your first project; refer back on each command.

---

## What you'll be doing, at a glance

```
/and-project ...                ← scope + staff (5 min)
/and-series                     ← series chunk + structural prompts (10 min)
/and-substance series           ← signature: state axes + per-book Δ + book chunks (15 min — most of your authoring input lands here)
/and-cast                       ← assemble cast; series-level audit checkpoint blocks here (10 min)
                                  → audit checkpoint approval; downstream blocked until you `y`
/and-substance book b01         ← book drama + per-chapter Δ + chapter chunks (5 min)
loop per chapter:
  /and-substance chapter b01cNN ← per-scene chunks + scene_conflict + handoff (3 min)
  /and-write b01cNN             ← decompose scenes into bones + bone-gate (5 min)
  /and-facets b01cNN            ← ten facets + dialogue + scene-map validation (10 min)
  /and-stitch b01cNN            ← render draft/<book>-<chapter>.md (5 min)
/and-review verdict b01         ← orchestrator-critic on the book (5 min)
                                  → PASS / PASS-WITH-NOTES / FAIL
```

Total wallclock for one full book (1 series + 1 book × 4–8 chapters): roughly **2–4 hours**, dominated by the per-chapter `/and-facets` and `/and-stitch` fork dispatches. Most of your *input* is in `/and-substance series` (the signature) — everything below it is mostly accept-the-default and proofread-on-failure.

If you want to walk away mid-chain: `/and-substance book b01 --cascade` chains chapter → write → facets → stitch for every chapter under the book. `/and-cut` mid-cascade saves a resume checkpoint; come back and run `/and-substance book b01 --cascade --resume`.

---

## Step 1 — `/and-project`

**Invocation:**

```
/and-project <title-slug> "<one-line brief>" <audience-1> <audience-2> <audience-3>
             [--screen-writer <slug>] [--dramatist <slug>] [--auditor <slug>]
             [--editor <slug>] [--orchestrator-critic <card-version>]
```

**What you provide:**
- `title-slug` — short kebab-case identifier (e.g. `flea-bottom-dance`); becomes the directory name under `projects/` when the project closes.
- `"<brief>"` — one-line series brief in quotes. Subject + setting + central tension. *"A young woman raised in Flea Bottom learns she's a bastard Targaryen and must survive the Red Keep before her presence destabilizes the realm."* Don't write a synopsis — write the elevator pitch.
- Three audience slugs from `staff/audience/INDEX.md`. The audience trio reviews every chunk and every chapter for substance-felt. Pick three that read *differently* — if all three are the same archetype (e.g. all critical-distance), you'll lose blind-spot coverage. Browse `staff/audience/INDEX.md` first; the README at the top groups personas by reading-stance.
- *(optional)* Override flags for the non-audience staff slots. Skip them unless you have a specific reason — the library defaults are good first picks.

**What you'll see:**
1. Phase 1 scaffold prints the directory tree it created.
2. Phase 1.5 — brief expansion. The command asks you 3-5 follow-up questions about the brief (settings, themes-as-bounds, hard fences). This is where "the bowl is weird" type questions get answered up front: what currency exists, what classes exist, what's the geography. Take your time here — getting the world-frame right early saves continuity revisions later.
3. Phase 2 1a + 1b — constraints + open questions. Same shape; expect 5-10 prompts.
4. Phase 2 1d — world-law finalization. Auto-emits condition cards under `cards/conditions/`.
5. Staff bound to project. Output: `project.scope` + `project.staff` blocks in `staff/showrunner/memory.md`.

**Exit state:** you see `next: /and-series`. Run that.

**Re-run:** `/and-project` is the only command that **cannot** re-run. The Phase 0 hard-aborts if scope is populated. To redo a project, archive `active-project/` and start over.

---

## Step 2 — `/and-series`

**Invocation:**

```
/and-series [revise|redo]
```

**What you provide:** answers to seven structural prompts, each with a default in brackets (press enter to accept):

| prompt | default | notes |
|---|---|---|
| `book_count` | **no default** | required; an integer. Multiple of 3 if you flag `cyclical: true`. |
| `chapters_per_book` | `[4-8]` | range; accept the default unless you have a strong opinion. |
| `scenes_per_chapter` | `[1-3]` | range; **don't widen this** — scenes are substantial under the new chain. |
| `bones_per_scene` | `[5-15]` | range; the bone-gate trims under-density at the high end. |
| `cyclical` | `[false]` | true only for HP-style book-as-school-year. |
| `pov` | **no default** | `single` / `multi` / `rotating-per-book`. Required. |
| `cross_book_continuity` | `[empty]` | recurring antagonists + ongoing subplots; you can add later via `revise`. |
| `world_evolution` | `[evolving]` | static for fairytale-stasis; evolving for everything modern. |
| `series_end_shape` | **no default** | one of: `definitive` / `open-ended` / `ambiguous` / `tragic` / `triumphant`. Required. |

Then a screen-writer agent proposes the series chunk (a substance-bearing paragraph in Star-Wars-trilogy register). Audience + dramatist review; 3-try cap.

**What you'll see:** the proposed series chunk; audience verdicts; persisted to `series.chunk` + `series.structure.*`.

**Exit state:** `next: /and-substance series`. Run that.

**Re-run:** `/and-series revise` — keeps your structural answers, re-proposes the chunk; `/and-series redo` — re-prompts everything from Phase 1.

---

## Step 3 — `/and-substance series`

**Invocation:**

```
/and-substance series [revise|redo]
```

No slug arg at series level.

**What you provide:** edits to a proposed signature draft. This is the *most authoring-heavy step* in the chain — get the signature right and everything below is autopilot; get it wrong and the bone-gate will keep failing chapter after chapter.

**Flow:**
1. **Phase 4a — screen-writer proposes signature.** Reads your brief + series chunk. Proposes 1-9 ranks for each of ~9 universal axes (wealth / health / community / emotional / capability / knowledge / reputation / agency / trust), across protagonist + antagonist + world perspectives. Drafts cost-ledger entries (gain ↔ cost pairings) and antagonist-pressure entries.
2. **Phase 4b — you edit.** The draft is written to `staff/showrunner/signature-draft.md`. The shell shows a rendered table; the YAML is on disk. Open the YAML in your editor, change any rank, add or remove axes, rewrite cost-ledger entries. The proposal is a starting point — the questionnaire (`design/substance/questionnaire.md`) shows the questions the screen-writer was answering on your behalf; read it if a proposal feels off.
3. **Phase 4c — type `accept`.** Edited draft moves to `series.substance.*`.
4. **Phase 5 — audience + dramatist + auditor review the accepted signature.** Up to 3 revise loops if reviewers flag substance-flat / cost-cheap / pressure-missing.

**What you'll see:** Phase 6 persists per-book chunks (one paragraph per book under the series) + per-book Δ targets. Book slugs auto-generated: `b01`, `b02`, …, `bN`.

**Exit state:** `next: /and-cast`. Run that.

**Re-run:** `revise` to re-tune ranks while keeping book chunks; `redo` to re-author from scratch.

---

## Step 4 — `/and-cast`

**Invocation:**

```
/and-cast [revise|redo] [--retire <slug>]... [--add <slug>]... [--swap <old>=<new>]...
```

No positional args on a fresh run.

**What you provide:** consent on the screen-writer's roster proposal + Y/N on the series-level audit.

**Flow:**
1. Screen-writer composes a brief: which axes need which carriers (protagonist for emotional / community; antagonist for reputation / agency; etc.).
2. Margit lists candidates from `cards/personas/INDEX.md`.
3. Screen-writer selects; dramatist verifies viability.
4. Margit provisions actor working dirs under `active-project/actors/`.
5. **Phase 5 audit checkpoint** — the series-level human checkpoint. Auditor produces a report. You see:

   ```
   Series-level audit complete. <N> findings (<H> HARD, <S> SIGNAL, <T> TASTE).
   Report: staff/reviews/series-audit-<timestamp>.md

   Approve and proceed? [y/N/feedback]
   ```

   - **`y`** — approval stamped to `project.series_audit.approved_at`. You move on.
   - **`N`** (default) — exit. Read the report. Run whichever revise command addresses the findings: `/and-cast revise`, `/and-substance series revise`, `/and-series revise`, etc.
   - **`feedback`** — type free-text notes; they save to `staff/reviews/series-audit-<timestamp>-feedback.md`; run a revise command that reads the feedback file.

   This is the ONLY blocking human checkpoint in the chain. Everything from `/and-substance book b01` onward is agent-resolved by default.

**Exit state on `y`:** `next: /and-substance book b01`.

**Re-run:** `revise` with `--retire / --add / --swap` flags, or bare `revise` for interactive selection. `redo` decommissions the full roster and re-runs from scratch.

---

## Step 5 — `/and-substance book b01`

**Invocation:**

```
/and-substance book b<NN> [revise|redo|add] [--cascade [--resume|--restart]]
```

**What you provide:** nothing manually unless review fires revise. Optionally `--cascade` to drive all the way to draft.

**Flow:**
1. Reads `books[b01].chunk` + `books[b01].substance_delta` (authored by `/and-substance series` Phase 3).
2. Authors `books[b01].drama` ("what cannot survive this book" statement).
3. Authors per-chapter chunks (chapter slugs `b01c01` … `b01cM`) + per-chapter Δ targets + per-chapter `handoff_in` / `handoff_out` blocks.
4. Reviews: audience + dramatist + auditor. Dramatist additionally verifies cross-chapter handoff coherence (chapter N's `handoff_out` matches chapter N+1's `handoff_in`).

**With `--cascade`:** after Phase 6 persist, fires `/and-substance chapter b01cMM` → `/and-write b01cMM` → `/and-facets b01cMM` → `/and-stitch b01cMM` for every chapter in order. Halts on first FAIL; checkpoint at `staff/showrunner/cascade-checkpoint.md`.

**Exit state:** `next: /and-substance chapter b01c01` (or, with `--cascade`, the chain runs and you come back to a finished `draft/b01-c01.md` … `draft/b01-cM.md`).

---

## Step 6 — `/and-substance chapter b01c01`

**Invocation:**

```
/and-substance chapter b<NN>c<MM> [revise|redo|add] [--cascade]
```

**What you provide:** nothing manually unless review fires revise.

**Flow:** authors per-scene chunks + per-scene `substance_delta` + per-scene `scene_conflict` (protagonist_force / opposing_force / stakes_axis) + chapter `pov_narrator` + chapter `dramatic_shape` + chapter `goal`. Reviews fire.

**With `--cascade`:** chains into `/and-write` → `/and-facets` → `/and-stitch` for this chapter only.

**Exit state:** `next: /and-write b01c01`.

---

## Step 7 — `/and-write b01c01`

**Invocation:**

```
/and-write b<NN>c<MM> [revise|redo] [--from-signals]
```

**What you provide:** nothing on a fresh run. On revise, optionally `--from-signals` to scope revise to the bones with SIGNAL findings.

**Flow:** decomposes each scene into 5-15 bones with declared per-bone Δ; runs five-pass SVO discipline; substance bone-gate (Phase 6) verifies every bone causes the declared Δ; HARD findings block emission and force revise inside the run; SIGNAL findings record but pass.

**What you'll see at emit:**

```
/and-write b01c01: PASS. 37 bones across 2 scenes. Bones file: theater/bones/b01-c01.md
                                                   Scene-map: theater/facets/scene-map-b01-c01.md

Bone-gate verdict: PASS (HARD: 0, SIGNAL: 3, TASTE: 0).
3 SIGNAL findings recorded — see `/and-review bones b01c01` to inspect, or
                              `/and-write b01c01 revise --from-signals` to address.
```

If you care about the 3 SIGNALs, run the inspect command, decide, then optionally revise. If the chapter feels strong enough as-is, move on; SIGNALs are recorded and re-surface on `/and-review`.

**Exit state:** `next: /and-facets b01c01`.

---

## Step 8 — `/and-facets b01c01`

**Invocation:**

```
/and-facets b<NN>c<MM> [revise|redo]
```

**Flow:** R1 fanout → R1 fanin → R2 fanout → R2 fanin → mechanical audit → audience-gate (URI-DIALOGUE-COVERAGE-GATE + URI-SCENE-WINDOW). Outputs land at `theater/facets/<facet>-b<NN>-c<MM>.md` and `theater/dialogue/b<NN>-c<MM>.md`.

This is the longest single command per chapter (~10 minutes of dispatched forks). Walk away.

**Exit state:** `next: /and-stitch b01c01`.

---

## Step 9 — `/and-stitch b01c01`

**Invocation:**

```
/and-stitch b<NN>c<MM>
```

**Flow:** eight-phase render: lens-anchored render → redundancy cull → compression → voice transform → local flow (enforces speaker-paragraph breaks) → buildup preservation → editorial reflection → finalize (strips any surviving scene-callout markers).

**Outputs:**
- `draft/b<NN>-c<MM>.md` — clean draft. The deliverable.
- `draft/b<NN>-c<MM>.annotated.md` — traced view with bone citations preserved.

This is `draft/`, not `polish/` — polish is deferred under this overhaul. The clean draft is the ship-ready manuscript for the current chain.

**Exit state:** `next: /and-substance chapter b01c02` (loop), or after the last chapter: `next: /and-review verdict b01`.

---

## Step 10 — `/and-review verdict b01`

**Invocation:**

```
/and-review verdict b<NN>
```

**Flow:** orchestrator-critic fires against the whole book. Reads every chapter's chunk + bones + facets + drafts. Verdict: PASS / PASS-WITH-NOTES / FAIL.

**Outputs:**
- `staff/reviews/verdict-b<NN>-<timestamp>.md`
- `books[b<NN>].orchestrator_critic_verdict.ruling` persisted.

**On PASS or PASS-WITH-NOTES:** book is shipped under the new chain. Move on to `b02` (loop back to Step 5).
**On FAIL:** human decision required. Read the report, run targeted revise commands at the failing level.

---

## Useful side commands

| command | when to use |
|---|---|
| `/and-cut` | mid-session save-and-stop. Prints `next: <command>` and `resume: <command>` (the latter only in cascade mode). |
| `/and-review` (no args) | discovery — lists every subcommand + recommended next-action. |
| `/and-review bones <chapter>` | spot-check a chapter's bones; surfaces SIGNAL findings + suggested revise command. |
| `/and-review consistency [<root>]` | cross-level + cross-chapter handoff sweep. Run after a stretch of chapters to catch drift. |
| `/and-review tree [<root>]` | full review sweep at and below root. Defaults to whole series. |
| `/and-review feedback <feedback-file> [<root>]` | re-fire reviewers carrying your free-text feedback as context. Use case: "review this book against the notes I left in `active-project/feedback.md`." |

---

## Cascade mode — drive everything to draft

```
/and-substance book b01 --cascade
```

Chains: `/and-substance chapter` (per chapter) → `/and-write` → `/and-facets` → `/and-stitch`. For a 4-chapter book, expect ~1 hour wallclock. Halts on first FAIL; resume with `--resume`.

```
/and-substance book b01 --cascade --resume    # after halt or /and-cut
/and-substance book b01 --cascade --restart   # discard checkpoint, start over
```

To cascade the entire series in one shot: `/and-substance series --cascade` (does series → all books → all chapters → all writes/facets/stitches in one chain). Use sparingly — long cascades make it harder to spot a chapter that's drifting until many chapters later.

---

## When something goes wrong

| symptom | most likely cause | recovery |
|---|---|---|
| `/and-substance book b01` Phase 0 hard-abort: "series audit not approved" | You skipped Step 4's `y` prompt. | Run `/and-cast`, get to Phase 5, type `y`. |
| `/and-write` repeatedly HARD-fails with `SUBSTANCE-FLAT-<axis>` | Scene contract is asking for Δ the bones can't deliver. Often a too-ambitious per-scene contract. | Run `/and-substance chapter b01c01 revise`; lower the per-scene Δ on the offending axis OR re-think the scene chunk's conflict. |
| `/and-facets` HARD-fails with URI-DIALOGUE-COVERAGE-GATE | `speaks to` bones have unresolved speakers or listeners. | Check `chapters[].scenes[].bones[]` SUBJECTs vs. cast roster; usually a slug typo. Run `/and-write revise` to fix. |
| `/and-stitch` produces a draft that "feels smashed together" | Speaker-paragraph rule failed to fire (rare). | Re-run `/and-stitch <chapter>`; if it persists, file the case against the Phase 5 local-flow fork's rendering rule. |
| Cross-chapter relay bugs ("character has X for no reason") | `handoff_in` / `handoff_out` mismatch the dramatist didn't catch. | Run `/and-review consistency b01`; address handoff drift via `/and-substance chapter <prior> revise` on the offending chapter. |
| You don't know what to run next | `/and-cut` (prints `next:`) or `/and-review` (lists everything). |

---

## What this run book does NOT cover

- Substance framework deep-dive — see `design/substance/README.md`.
- Default-band rationale — see `design/substance/delta-targets.md`.
- Questionnaire details — see `design/substance/questionnaire.md`.
- Re-runnability protocol details — see `design/substance/rerun-protocol.md`.
- Staleness cascade details — see `design/substance/staleness-cascade.md`.
- Implementer-level command body specifics — see `design/substance/plan.md`.
