# Substance Overhaul — Implementation Plan

**Status:** DRAFT, 2026-05-16 (revised 2026-05-17; plan-holes pass 2026-05-17). Awaiting user approval before execution.

**Revision 2026-05-17 (post intent-gaps audit):** beat level dropped; bones are now scene-children with their own per-bone state-delta, authored by `/and-write` during scene-decomposition. `/and-substance` shrinks from four invocation levels to three (`series` / `book` / `chapter`); the former `/and-substance scene` is absorbed into `/and-write` Phase 1. Scene-conflict block added to scene chunks. `SUBSTANCE-FLAT` classified HARD at the bone-gate. Scenes default to 1–3 per chapter. See `intent-gaps.md` for the surrounding rationale.

**Plan-holes pass 2026-05-17 (post end-to-end reuse-pass review):** addresses `plan-holes-2026-05-17.md` Holes A–H. Mechanical edits: path-rename impact on `/and-facets`+`/and-stitch` spelled out (Hole A); `/and-facets` Phase 0 step 4 tens-precondition abort removed (Hole B); `chapters[].status` enum added to schema (Hole C); `/and-write` per-pass input adaptations enumerated (Hole D); re-runnability edge cases (SIGNAL-triggered revise, cascade checkpoint sketch, partial-revise verdict lifecycle) specified (Hole F); `/and-review verdict` rescoping table added (Hole G); dialects→behaviors rename explicitly deferred (Hole H). User-ruled Hole E split: **carved in** items #4 (stitcher rendering patch: speaker-paragraph breaks + scene-callout suppression), #6 (cross-chapter handoff fields + dramatist check), #10 (chapter ≈ episode mapping in README); **OOS-tracked** items #5 (absolute length floor), #7 (emotional-substance orthogonality), #8 (plot-arc-completion check), #11 (world-detail consistency).

**Triggering feedback** (from `active-project/feedback.md`, s01e01–s01e03):
- "Episodes felt empty and meaningless and like a puff of air, there was no substance."
- "No meaningful plot."
- "The characters don't seem to have a desire."
- "Potential for drama, for the tension to cause movement... but not shown."
- "The plot is very very weak. I believe that the protolines aren't being focused enough or the bones are too fine grained."
- "Scenes should have meaningful suspense and action with something against something."
- "Next time maybe I need to check in on /and-project to make sure things are chunked at the right size."

**Triggering notes** (handwritten, three pages):
1. Measure gain and loss from a perspective (experience-ee + audience), via comparative poll (rank state at Start, rank state at End, difference = Δ).
2. Gain-without-cost vs gain-with-cost — only weighted gain matters.
3. Plot-by-states (has, is) + plot-by-action (did, do) — both required.
4. Status axes: wealth, health, community, emotional well-being (+ spent, possess, journeyed).
5. Δ State / Σ Bones — substance density.
6. Δ required per chunk depends on what chunk abstracts (series / book / chapter / scene).
7. 1–9 scale questionnaire on protagonist state (and world, and antagonist, and story).
8. Impersonator should know what is valued most — overlap with audience values.
9. Bounds → noise/clusters/themes/ideas → meets constraints (setting, protag, antag, clear theme) → expected project plot delta (Δ Start, Δ End, N directions) → plot check gate → reviewer/critic check.

---

## Goal

Bake a **declared, measurable, auditable substance contract** into the pipeline at every level of resolution (series → book → chapter → scene chunks, plus per-bone state-deltas inside each scene), so that:

- Every project has its scope (constraints/settings/themes) and staff (personas for planning/reviewing/editing/judging) explicitly bound before any content is authored.
- Every series has a brief substance-bearing chunk (Star-Wars-trilogy-style paragraph) plus structural commitments (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape).
- Every series has a substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets).
- Every cast is assembled to deliver named substance commitments.
- **One recursive command (`/and-substance`) authors substance and structure at every chunk level below series, stopping at scene** — book→chapter, chapter→scene. Each level fires its own review. /and-substance replaces the previous `/and-season` and is the chunker authoring chain from the series signature down to scene chunks.
- **Bones are scene-children that carry their own state-delta.** `/and-write` decomposes each scene into bones, each bone declaring one or two axis-movements with declared cost. The bone IS the beat — what used to be a separate "beat chunk" planning level is collapsed into the bone itself, authored by `/and-write` during scene decomposition.
- Every polished prose pass is audited for whether the substance lands (felt by audience, traceable to bones by auditor).

**Clean split between chunkers and bones.** `/and-substance` is a **chunker only** — it authors chunks at four levels (series → book → chapter → scene) and attaches a substance contract to each (Δ axes, costs, density target). It stops at scene chunks; it does NOT write SVO bones and does NOT decompose scenes into bones. Bones are authored by **`/and-write`** (renamed from `/and-protolines`), which reads scene chunks + their substance contracts and produces SVO bones — each bone carrying its own declared axis-movement (its per-bone state-delta) plus the SVO craft. This separation matters: chunking (how meaningful, what shifts, at what cost, in what nested unit) and bone-writing (decompose-scene-into-actions + subject-verb-object craft + line economy + continuity) are different jobs at different levels of resolution. Conflating them is the failure mode `/and-season` has today. The rename to `/and-write` also drops pipeline-jargon framing ("protolines") in favor of creative-writing language.

**Bones-grain principle: scene-action-sized, not micro.** A bone covers a meaningful scene-action — one declared axis-movement with declared cause. "Maya confronts her brother about the missing key, +2 community, −1 emotional" is one bone. A scene has 5–15 bones; each one earns its place by causing Δ. Chatter-bones (no declared Δ) do not survive Phase 4 trim. This directly addresses the user-feedback complaint that protolines were "too fine grained" — under the new contract, a bone-without-Δ is a schema violation, not a craft choice.

**Bones and facets preserved.** The shoot-v2 chain (bones → facets → stitcher) keeps its shape. `/and-write` consumes scene chunks instead of an "episode chunk," runs the existing five-pass SVO pipeline (inventory → constraint → shape → trim → continuity) with a new scene-decomposition pass at the front, and emits the per-chapter bones file that `/and-facets` and `/and-stitch` consume. **Exception:** the **tensometer facet is dropped** — the substance contract (per-bone Δ + per-scene aggregate + cost ledger + density target) is what tensometer was reaching for, more directly and with declared cause. Tensometer is removed from `/and-facets` output and its rubric is archived; URI-026 "tens-gate" is replaced by the **substance bone-gate** as a pass inside `/and-write`, which verifies the bones actually deliver the declared substance contract and that aggregate scene-Δ matches the scene's contract.

---

## Pipeline restructure

**Current chain (pre-overhaul):** `/and-project → /and-season → [shoot chain] → /and-wrap`

**New chain:**

```
/and-project (scope + staff)
  ↓
/and-series (series chunk + structural prompts)
  ↓
/and-substance series (signature + per-book Δ + book chunks)
  ↓
/and-cast (cast roster)
  ↓ [series-level human audit checkpoint]
/and-substance book b01 (book drama + per-chapter Δ + chapter chunks)
  ↓
/and-substance chapter b01c01 (dramatic shape + per-scene Δ + scene chunks)
                                  ← fires once per chapter; deepest chunker level
  ↓
/and-write b01c01 (decomposes each scene into bones with per-bone Δ;
                   produces SVO bones; substance bone-gate)
                                  ← fires once per chapter
  ↓
/and-facets b01c01 (per-facet runners; tensometer dropped; scene-map Phase 4d validates the upstream-emitted scene-map facet)
  ↓
/and-stitch b01c01 (eight-phase prose render → draft/<chapter>.md; tensometer-fallback path removed from Phase 0)
  ↓ [optional /and-review at any point for spot-checks / verdicts]

[final-edits / polish / ship-ready manuscript: deferred until upstream is proven]
```

**Six live commands; two dropped; one polish-deferred; one renamed. No command is built from scratch — every "new" command is a lift-and-adapt of an existing asset, identified in the Asset reuse map below.**

| command | status | scope | primary lift source |
|---|---|---|---|
| `/and-project` | **overhauled (shrinks)** | Scope + staff binding. No story content. | current `/and-project.md` Phases 1, 1.5, 1.6, 2 1a/1b/1d |
| `/and-series` | **extracted + extended** (was inline in `/and-project`) | Series chunk (Star-Wars-style paragraph) + structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape). | current `/and-project.md` Series Plan section + Phase 3 Present-results (relocated); structural prompts are the only net-new content |
| `/and-substance` | **generalized + recursive** | Single command body, fires at three invocation levels (`series`/`book`/`chapter`). Authors chunks + substance contracts at the four chunk levels (series, book, chapter, scene). Stops at scene chunks — does NOT decompose scenes into bones and does NOT write bones. | current `/and-season.md` Phase 1 (chunker authoring loop) + Phase 3 (review-sweep dispatch shape); recursion glue + substance-signature authoring + `--cascade` are net-new |
| `/and-cast` | **extracted + extended** (was inline in `/and-project`) | Cast roster + series-level human audit checkpoint. | current `/and-project.md` Phase 2 1c (cast selection) + Phase 3 (audit checkpoint); margit provisioning logic preserved from current `/and-project` Phase 1; `revise` decommission-routing is net-new |
| `/and-season` | **DROPPED** | Chunking jobs absorbed by `/and-substance`; bone-writing + scene-decomposition jobs absorbed by `/and-write`. Content lifted in pieces — see Asset reuse map. | n/a (source command) |
| `/and-write` | **lifted from `/and-protolines-v2` + 2 phases** | Five-pass SVO pipeline lifted verbatim from `/and-protolines-v2`. New Phase 1 scene-decomposition (front-loaded) and new Phase 6 substance bone-gate (replaces v2 Phase 6 persist; persist re-numbered to Phase 7 and extended with scene-map co-emit). Input shape changes (was "episode chunk" → now scene chunks with substance contracts from `/and-substance chapter`). | `/and-protolines-v2.md` Passes 1-5 verbatim; `/and-season.md` Pass S10 bone-gate (lines 460-499) adapted to substance contracts; `/and-season.md` Phase 7 Steps 1-3 (lines 616-676) lifted for flat_id assignment + file emission |
| `/and-review` | **router + thin wrappers over existing review primitives** | Universal review primitive with subcommand router. Every subcommand body invokes a review primitive that already exists somewhere in the codebase; router is the only originally-authored code. | router is net-new (~80 lines); subcommand bodies are wiring-only over existing primitives — see Asset reuse map for the primitive→subcommand mapping |
| `/and-judge-book` | **DROPPED** | Absorbed by `/and-review verdict <book>`. Note: `/and-judge-book` was never written as a standalone command; its content lived inside `/and-season.md` Phase 6. The lift target is `/and-season.md` lines 577-609. | n/a (never existed standalone) |
| `/and-facets` | overhauled (light) | Tensometer facet removed from R1/R2 fanout. Phase 4d scene-map downgrades from derivation to validation (consumes the upstream-emitted scene-map facet from `/and-write` Phase 7). R1 rubric input lists drop tens reads; substance-contract reads substitute where pressure-signal is needed. | current `/and-facets.md` (edit-in-place) |
| `/and-stitch` | overhauled (very light) | Eight-phase pipeline preserved; Phase 0 tensometer-derivation fallback removed as dead code under the new chain. Output is `draft/<chapter>.md` — the deliverable until upstream substance machinery is proven. | current `/and-stitch.md` (edit-in-place) |
| `/and-wrap` | **POLISH-DEFERRED** (not dissolved) | Polish concerns deferred entirely until upstream chain is working end-to-end. Command archived intact at `archive/commands/and-wrap-polish-deferred.md` with intent to revive as `/and-review prose` + future polish revival; Phase 2 (8-class auditor pass) and Phase 3 (editor allowed-moves contract + procedure) are the un-defer targets. | n/a (preserved for revival) |

### Why drop /and-judge-book; why polish-defer (not dissolve) /and-wrap

**`/and-judge-book`** existed only in draft form (its content lives inside `/and-season.md` Phase 6, lines 577-609). It fires the orchestrator-critic verdict against a finished book — a single review type. `/and-review` is the universal review primitive; folding the verdict into `/and-review verdict <book>` consolidates the review surface. The lift target for `/and-review verdict` is `/and-season.md` Phase 6 verbatim, rescoped to book.

**`/and-wrap`** wasn't pulling its weight at the moment because its editor pass produced marginal changes on top of `/and-stitch`'s Phase 7 (editorial reflection), and its audience+auditor phases were mandatory dispatch cost for a review the user might or might not want at that moment. Dropped from the live command set, **but archived as `-polish-deferred`, not `-dissolved`** — its Phase 2 (8-class auditor pass: BONE-COVERAGE, DIALOGUE-VERBATIM, EXPOSITION-VERBATIM, NO-INVENTION, CONTINUITY, BLOCKING, SCENE-MAP-RESPECT, EARTH-BET-HARD-FENCE) and its Phase 3 (editor allowed-moves contract + procedure + failure modes) are the future un-defer targets for `/and-review prose <chapter>` and any eventual polish revival. Preserving the spec saves a re-author later.

**Polish / final-edits is deferred entirely as a concern.** The substance overhaul ships when the upstream chain — `/and-project` → `/and-series` → `/and-substance series` → `/and-cast` → `/and-substance` (recursive) → `/and-write` → `/and-facets` → `/and-stitch` — produces a draft that is *substantively right*. Prose polish, cross-chapter percussion, repetition culling across the book, ship-ready manuscript work: all of that waits until the substance machinery is proven. `/and-stitch` is **structurally unchanged** by this overhaul (its eight-phase pipeline shape is preserved; the one narrow mutation is Phase 0 tensometer-fallback removal); `/and-review prose <chapter>` is **stubbed-deferred** with its un-defer lift target pre-pinned to `/and-wrap.md` Phases 2–3. The chain ends at `draft/<chapter>.md`; that's the deliverable until upstream is trusted.

### Why drop /and-season entirely

The previous plan kept `/and-season` because building `/and-substance` recursively was a bigger upfront lift than wiring it at the series level alone. But `/and-season`'s actual job — book→chapter chunking + chapter→scene chunking + scene→bones expansion + per-level review — is *structurally* what `/and-substance` + `/and-write` now do (chunker recursion + scene-decomposition). Compressing it into one inline command is a leaky abstraction: it hides the recursive substance contract from the model (and from re-run protocol, and from staleness cascade). Build the chunker and the bones-crafter as separate primitives and the abstraction is clean: `/and-substance` operates the same way at every chunk level above scenes; `/and-write` owns everything below.

Secondary benefit: the "season"/"episode" framing dissolves. `/and-substance` operates on `book`/`chapter`/`scene` arguments. The model never reads "episode" while planning or authoring.

---

## Boundary table — what moves where

Four commands are being restructured: `/and-project` shrinks, `/and-season` is dissolved, `/and-wrap` is dropped without replacement, and `/and-protolines` is renamed-and-overhauled to `/and-write` (substantive change, not a rename — new input shape; see `/and-write` spec below).

### Out of `/and-project`

| Current `/and-project` step | Stays / moves | Lands in |
|---|---|---|
| Phase 1 Scaffold | stays | `/and-project` |
| Phase 1.5 Brief expansion | stays | `/and-project` |
| Phase 1.6 Audience selection | stays | `/and-project` |
| Phase 2 1a — Decided constraints + open questions | stays | `/and-project` |
| Phase 2 1b — Open question resolution | stays | `/and-project` |
| Phase 2 1c — Candidate menu + cast selection | moves | `/and-cast` |
| Phase 2 1d — World-law finalization (condition cards) | stays | `/and-project` |
| Series Plan (theme + plot + protag arc + series Q + season chunks) | splits | series chunk → `/and-series`; signature + per-book Δ → `/and-substance series` |
| Series-level audit checkpoint | moves | after `/and-cast` |
| **NEW** — staff persona binding (planning/reviewing/editing/judging staff, beyond audience) | n/a | `/and-project` |
| **NEW** — structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape) | n/a | `/and-series` |
| **NEW** — substance signature + per-book Δ | n/a | `/and-substance series` |

### Out of `/and-season` (dissolved)

| Current `/and-season` step | Moves to |
|---|---|
| Phase 1 drama statement | `/and-substance book` Phase 4 (book drama authoring) |
| Phase 1 content beat authoring | `/and-substance book` Phase 3 (per-chapter chunks + per-chapter Δ) + `/and-substance chapter` Phase 3 (per-scene chunks + per-scene Δ) + `/and-write` Phase 1 (scene-decomposition: bones-with-deltas authored from each scene) |
| Phase 2 bone expansion (SVO writing) | `/and-write` Phases 2–4 (constraint audit → SVO craft → trim) |
| Phase 3 review sweeps (S1–S10, S11 substance) | chunk-quality reviews fire inside each `/and-substance` level (audience: meaningful? dramatist: shape? auditor: contract match?); decomposition + SVO + continuity reviews fire inside `/and-write`. |
| URI-026 bone-gate (tens-gate) | `/and-write` Phase 6 substance bone-gate — **replaces tens-gate**: per-bone axis-movement verification + per-scene aggregate Δ delivery + cost-paid check, against each scene's substance contract. Tens rubric retired. |
| Phase 6 orchestrator-critic verdict | `/and-review verdict <book-slug>` (subcommand of `/and-review`) — fires when both `/and-substance` (all chunks under the book) and `/and-write` (all chapter bones files) are complete for the book. |
| Phase 7 per-chapter file emission | `/and-write` Phase 7 (emit bones to `theater/bones/<book>-<chapter>.md`) |

After dissolution, no command body contains the literal word "season."

---

## Asset reuse map

Every "new" command in the table above is a lift-and-adapt of an existing asset, plus a small named delta. The implementer SHOULD open the source file, copy the relevant section into the new command body, and apply only the listed edits. Writing-from-scratch is reserved for the genuinely-new items called out in the "net new" column.

### `/and-write` (target: `.claude/commands/and-write.md`)

| target phase | lift from | adaptation |
|---|---|---|
| Phase 0 — Validate + mode select | `/and-protolines-v2.md` Phase 0 (lines 44-68) | replace "episode chunk" reads with "scene chunks under chapter"; add `revise`/`redo` mode prompt per shared re-run protocol |
| Phase 1 — Scene-decomposition | **net new** | the only original authoring in this command — decompose each scene chunk into 5-15 bones with per-bone Δ; ~80 lines |
| Phase 2 — Constraint audit | `/and-protolines-v2.md` Pass 2 (lines 94-116) verbatim | add per-bone Δ well-formedness checks + aggregate-bones-Δ ≈ scene-Δ check (lift verification logic from `/and-season.md` Pass S10) |
| Phase 3 — Shape (SVO writing) | `/and-protolines-v2.md` Pass 3 (lines 117-139) verbatim | speech-bone licensed-form check unchanged (URI-DIALOGUE-COVERAGE-GATE anchor preserved) |
| Phase 4 — Trim | `/and-protolines-v2.md` Pass 4 (lines 140-163) verbatim | rationale shifts from "chatter" to "no declared Δ → schema violation"; trim criterion changes but dispatch shape preserved |
| Phase 5 — Continuity audit | `/and-protolines-v2.md` Pass 5 (lines 164-189) verbatim | no change |
| Phase 6 — Substance bone-gate | `/and-season.md` Pass S10 bone-gate (lines 460-499) | replace tens-correlation with substance-contract verification (bonefide / per-axis Δ delivery / cost-paid / opposing-force visible) |
| Phase 7 — Emit + scene-map co-emit | `/and-season.md` Phase 7 Steps 1-3 (lines 616-676) | rescope from season-split-output to per-chapter; add scene-map facet co-emission; lift flat_id assignment logic verbatim |

**Net-new line count for `/and-write`:** ~150 lines (Phase 1 scene-decomposition + Phase 6 substance contract logic + Phase 7 scene-map co-emit). The remainder is verbatim or near-verbatim lift from `/and-protolines-v2` and `/and-season`. Total command size ~350-400 lines, of which ~200-250 are lifts.

**Pass input adaptations.** "Lift verbatim" applies to dispatch shape + SVO discipline, NOT to the per-pass input lists — input shapes change under the new chain. Per-pass adaptations the implementer must apply while lifting:

| Pass | Current input (`/and-protolines-v2`) | New input under `/and-write` |
|---|---|---|
| Pass 1 (Phase 2 here — Constraint audit) | `theater/episode-plan.md` chunk/change/theme/actors/constraints | scene chunks under `chapters[<chapter>].scenes[]` + per-scene `substance_delta` + per-scene `scene_conflict` + parent `chapters[].goal` + parent `chapters[].dramatic_shape` — read from showrunner memory, not from a flat episode-plan file |
| Pass 2 (constraint audit logic, run inside Phase 2 here) | episode-plan constraints list + `series.constraints` | scene-level `substance_delta.axis_moves` well-formedness + aggregate-bones-Δ ≈ scene-Δ check (per `/and-season` Pass S10 verification logic) + per-bone `substance_delta` schema check + cost-ledger anchor resolvability |
| Pass 3 (Phase 3 here — Shape / SVO writing) | `series-plan.md` + `season-s01-plan.md` (season escalation spine) | `series.substance.state_axes` + `series.substance.antagonist_pressure` + `books[<book>].substance_delta` + `chapters[<chapter>].dramatic_shape` + `chapters[<chapter>].goal` — escalation spine collapses to the parent-chunk Δ chain in memory |
| Pass 4 (Phase 4 here — Trim) | `active-project/staff/studio/vibes.md` + per-actor vibes + scene chatter heuristics | series vibe-cloud + book vibe-cloud only (chapter/scene/bone-level vibes deprecated per "Vibe-clouds under recursive substance" decision); studio vibes preserved unchanged (still authored at studio scope, still read by Pass 4 for environment-bias). Trim criterion shifts from "chatter" to "no declared Δ → schema violation" — drop bones with empty `substance_delta.axis_moves` and no cost-ledger-paying role |
| Pass 5 (Phase 5 here — Continuity audit) | within-episode state-thread | within-chapter state-thread (props move across scenes, actors track, conditions persist) PLUS cross-chapter handoff check per `chapters[].handoff_in` (carved in from intent-gaps item #6 — see schema below); reads prior chapter's `handoff_out` and verifies the current chapter's `handoff_in` is consistent |

**Forbid-loading lists preserved.** Each pass continues to forbid loading other chapters' bones files during its own fork — context isolation is part of why the five-pass shape works. The only cross-chapter read introduced is the Pass 5 read of the prior chapter's `handoff_out` field from showrunner memory (a structured field, not the bones file). Explicit in each pass brief: "do not load other chapters' bones files; consult showrunner memory's `chapters[].handoff_out` field only for the immediately-prior chapter."

### `/and-substance` (target: `.claude/commands/and-substance.md`)

| target phase | lift from | adaptation |
|---|---|---|
| Phase 0 — Validate + mode select | shared re-run protocol (`design/substance/rerun-protocol.md`) | reference, not duplicate |
| Phase 1 — Read parent | `/and-season.md` Phase 1 step 1a (lines 50-64) | generalize "prior season" to "parent chunk at next-higher level" |
| Phase 2 — Author sub-chunks | `/and-season.md` Phase 1 step 1d (lines 75-84) | generalize "content beats" to "child chunks at this level"; per-level dispatcher table picks the right screen-writer prompt |
| Phase 3 — Author sub-chunk substance contracts | **net new** | the substance-contract authoring (Δ axes, costs, density target, scene_conflict) is original to this overhaul; ~50 lines |
| Phase 4 — Level-specific extras | `/and-season.md` Phase 1 step 1c (book drama, lines 71-74) for book level | series level (signature authoring: state axes, anchors, cost ledger, antagonist pressure) is **net new** ~80 lines; chapter level (dramatic_shape + goal) is ~20 net-new lines |
| Phase 5 — Chunk-quality review | `/and-season.md` Phase 1 step 1e (lines 85-93) + Phase 3 sweep-A pattern (lines 224-302) | lift the fork-then-collate-then-fix-route shape verbatim; parameterize reviewer count by level |
| Phase 6 — Persist | `/and-season.md` Phase 1 step 1f (lines 94-103) + Phase 5 (lines 527-575) | rescope persistence target from season-plan to chunks-under-current-level in showrunner memory |
| `--cascade` flag | `/and-protolines-season-v2.md` (per-episode loop pattern) | adapt cross-episode loop to per-child-chunk cascade; checkpoint after each child completes |

**Net-new line count for `/and-substance`:** ~150-180 lines (substance-contract authoring + series-level signature authoring + recursion glue + cascade flag). Remainder ~200 lines is `/and-season` lift. Total ~350-400 lines.

### `/and-series` (target: `.claude/commands/and-series.md`)

| target phase | lift from | adaptation |
|---|---|---|
| Phase 0 | shared re-run protocol | reference |
| Phase 1 — Structural prompts | **net new** | book count, length ranges, cyclical, POV, cross-book continuity, world evolution, series-end shape — original prompts; ~30-50 lines |
| Phase 2 — Series chunk authoring | `/and-project.md` Series Plan section (the screen-writer-authored prose-paragraph step) | strip out per-season chunk authoring (handled by `/and-substance series` recursively); keep just the series-chunk-paragraph step |
| Phase 3 — Audience + dramatist review | `/and-project.md` review dispatch in the same section | verbatim |
| Phase 4 — Persist | `/and-project.md` series-plan persistence step | retarget to `series.chunk` + `series.structure.*` in showrunner memory |

**Net-new line count for `/and-series`:** ~50 lines (structural prompts). Total command ~100-130 lines.

### `/and-cast` (target: `.claude/commands/and-cast.md`)

| target phase | lift from | adaptation |
|---|---|---|
| Phase 0 | shared re-run protocol | reference; the `revise`/`redo` decommission-routing is net-new (~25 lines) |
| Phase 1 — Substance-driven cast brief | `/and-project.md` Phase 2 1c — Candidate menu + cast selection (lines 256-285) | feed brief from `series.chunk` + `series.substance.*` instead of from series plan |
| Phase 2 — Margit candidate menu | `/and-project.md` Phase 2 1c subsection | verbatim |
| Phase 3 — Screen-writer selection + dramatist viability | `/and-project.md` Phase 2 1c "Attempt N" subsection (lines 286-289) + dramatist viability check | verbatim |
| Phase 4 — Margit provisioning | `/and-project.md` Phase 1 step 4 margit-provisioning logic + the cast-side of Phase 2 1c | preserved; fresh-provisioning-for-added-only on `revise` is the documented branch |
| Phase 5 — Series-level audit checkpoint | `/and-project.md` Phase 3 — Present results (lines 311-342) | rescope checkpoint payload to include signature + per-book Δ + cast (broader than current `/and-project` Phase 3 payload) |

**Net-new line count for `/and-cast`:** ~30 lines (revise/redo decommission-routing + checkpoint-payload extension). Total ~150-180 lines, mostly lift.

### `/and-review` (target: `.claude/commands/and-review.md`)

The router is the only original code. Every subcommand body invokes a primitive that already exists.

| subcommand | primitive source | net-new wiring |
|---|---|---|
| `verdict <book-slug>` | `/and-season.md` Phase 6 (lines 577-609) verbatim | rescope target from season to book; Phase 0 abort-conditions list (already enumerated in plan); rescoping table immediately below; ~15 lines |
| `chunk <slug>` | `/and-season.md` Phase 1 step 1e review-dispatch pattern (lines 85-93) | parameterize target slug by chunk-level; ~20 lines |
| `bone <slug>` | `/and-season.md` Pass S10 bone-gate per-bone check (lines 460-499) | extract per-bone subroutine; ~20 lines |
| `contract <slug>` | `/and-season.md` Pass S1 constraint audit (lines 307-318) + Pass S3.5 ruleset compliance (lines 369-385) | per-chunk dispatch; ~25 lines |
| `signature` | `/and-season.md` Phase 3 sweep-A shape pattern at series scope (lines 319-345) | series-only; ~20 lines |
| `bones <chapter-slug>` | `/and-write.md` Phase 6 substance bone-gate (which itself lifts from S10) | post-hoc re-fire of the same bone-gate; ~15 lines |
| `facets <chapter-slug>` | `/and-facets.md` R1 fanout per-facet rubric runners | extract into named subroutine; call from both `/and-facets` and `/and-review facets`; ~25 lines wiring |
| `cast` | `/and-cast.md` Phase 3 dramatist viability check + auditor fork | post-hoc fork; ~15 lines |
| `consistency [<root>]` | `/and-season.md` Phase 1 step 1g cross-season audit (lines 104-115) | generalize "cross-season" to "cross-level under root"; ~30 lines |
| `tree [<root>]` | composition of the above subcommands scoped to subtree | dispatch loop; ~25 lines |
| `feedback <file> [<root>]` | `design/shoot-v2/audience-review-originals-v2.md` workflow | reviewer-with-named-context dispatch; ~25 lines |
| `prose <chapter-slug>` (STUBBED-DEFERRED) | `/and-wrap.md` Phase 1 (audience review, lines 77-128) + Phase 2 (8-class auditor, lines 129-194) | not implemented in this overhaul; un-defer lift target pre-pinned |
| router + Phase 0 parse + Phase 1-4 shared shape | **net new** | ~80 lines |

**Net-new line count for `/and-review`:** ~80 (router) + ~10-30 lines × 11 live subcommands ≈ ~280 lines total, of which router is ~80 and the rest is thin wiring. The actual review logic (audience-card forks, dramatist, auditor, orchestrator-critic) is reused infrastructure.

**`/and-review verdict` rescoping table (Hole G — season → book field mapping).** The Phase 6 lift from `/and-season.md` references several season-scoped fields and per-episode artifacts; under the new chain these resolve to book-scoped equivalents. Explicit per-field mapping the implementer applies while lifting:

| `/and-season.md` Phase 6 reference | New target under `/and-review verdict <book-slug>` |
|---|---|
| `seasons[<slug>].orchestrator_critic_verdict.*` | `books[<slug>].orchestrator_critic_verdict.*` (block already present in revised showrunner schema) |
| "per-episode bones files for the season" (the list the orchestrator-critic reads) | per-chapter bones files for the book: `[theater/bones/<book-slug>-<chapter-slug>.md for chapter in books[<slug>].chapters]` |
| "season plan" (read for substance-contract context) | book chunk + per-chapter chunks + book drama + book substance_delta — i.e., the subtree under `books[<slug>]` in showrunner memory |
| "per-episode tens / facet outputs" (consumed for cross-episode coherence) | per-chapter facet outputs at `theater/facets/<facet>-<book-slug>-<chapter-slug>.md` for each chapter under the book |
| Verdict report path — current `/and-season` writes to `staff/orchestrator-critic/verdicts/<season-slug>-<timestamp>.md` | **canonical** new path: `staff/reviews/verdict-<book-slug>-<timestamp>.md` (matches all other `/and-review` subcommand outputs, single reports directory). The prior `staff/orchestrator-critic/verdicts/` path is NOT used by the new chain. |
| "drafts" if read for prose spot-check | per-chapter `draft/<book-slug>-<chapter-slug>.md` files — read only if `prose` spot-check is enabled; `prose` subcommand itself remains DEFERRED, so verdict default skips draft-reading. |
| Phase 0 abort precondition "all episodes under the season are protolined + faceted" | all chapters under the book have `status >= bones-written` (i.e. bones file emitted; facet-completion is not required for verdict but the absence is recorded as a SIGNAL finding by orchestrator-critic). |

Field mapping is one-to-one; no orchestrator-critic card mutation is needed (the card already references "the target unit" abstractly — only the dispatch wrapper changes targets).

### Shared lifts factored out

Two protocols apply identically to multiple new commands and SHOULD be factored into one design-doc reference rather than re-specified per-command:

| protocol | source | factored to | referenced by |
|---|---|---|---|
| Phase 0 re-run protocol (read upstream → check own output → cascade warning → run) | this plan, "Re-runnability" section, steps 1-4 | `design/substance/rerun-protocol.md` (new design doc) | `/and-series`, `/and-substance` (all levels), `/and-cast`, `/and-write`, `/and-review` (idempotent variant) |
| Staleness-cascade rules (mark-stale / keep-fresh / abort surfacing; staleness-log; warn-not-block on stale parents; verdict-block invalidation) | this plan, "Surfacing — defined" + "Staleness cascade" + "Staleness also invalidates" subsections | `design/substance/staleness-cascade.md` (new design doc) | same five commands + `/and-review verdict` |

Factoring these two protocols cuts roughly ~150 lines of repeated specification across the five new command bodies.

### Existing infrastructure used unchanged

These assets stay exactly as-is — no edit required, no lift needed, the new commands simply call into them:

- `staff/orchestrator-critic/card.md` — consumed by `/and-review verdict`
- `staff/audience/` 18-persona library + per-project 3-persona selection — consumed by every review dispatch
- `staff/{showrunner, screen-writer, coach, impersonator, studio, auditor, fixer, margit, dramatist, editor}/card.md` — agents unchanged
- `design/shoot-v2/rubric-{feeling, memory-flags, narrator-interest, sensory, state-updates, metaphor, vibes, location-state}.md` — preserved; light edits to drop tens-correlation reads only
- `design/shoot-v2/svo-writer-pass{1..5}-brief.md` — preserved verbatim (SVO craft unchanged)
- `cards/` library (personas, locations, props, conditions, behaviors) — preserved
- Bones file body format (flat integer IDs, monotonic, 7-field extended header, no body markers, post-extraction citation accrual) — preserved
- `schemas/{card, memory, audit-report, dialogue, facet, scene-map, stitch-*}.schema.md` + `schemas/show-file.format.md` — preserved (only `proto-line.schema.md` → `bones.schema.md` rename + `tens:` prefix drop)

### Total net-new vs lifted

| command | total estimate | net-new | lifted |
|---|---|---|---|
| `/and-series` | ~100-130 | ~50 | ~50-80 |
| `/and-substance` | ~350-400 | ~150-180 | ~200 |
| `/and-cast` | ~150-180 | ~30 | ~120-150 |
| `/and-write` | ~350-400 | ~150 | ~200-250 |
| `/and-review` | ~280 | ~80 (router) + thin wiring | ~150-200 inside the subcommand wrappers (calling into existing primitives) |
| Shared protocol docs | ~150 (two design docs) | ~150 | factored from repeated per-command specs |
| **Totals** | **~1,400-1,540** | **~610-690** | **~770-880** |

Compared to the prior estimate (~1,450-1,750 lines treated as net-new across five commands), roughly **55-60% of the substance overhaul is a lift-and-adapt operation**, not original authoring. The plan's previous size estimates ("`/and-substance` ~350-450 lines net new", "`/and-write` ~450-550 lines net new", etc.) reflected total-size, not original-content. Reframe accordingly during implementation: open the lift source, copy the relevant section, apply the listed adaptation, then write only the net-new phases from scratch.

---

## Re-runnability

Every new command except `/and-project` is **re-runnable**. The authoring loop is: draft → review → revise → revise → settle. Hard-abort-on-existing would force manual state deletion to iterate, which is wrong for creative work.

| command | re-runnable? | re-run modes |
|---|---|---|
| `/and-project` | **NO** — exception | Phase 0 hard-aborts if scope already populated. Project scope is foundational; revising it requires a new project. (User-confirmed.) |
| `/and-series` | yes | `revise` / `redo`. |
| `/and-substance` (any of the three invocation levels) | yes | `revise` (refine in place — same children, retune contracts), `add` (add new sub-chunks or axes/costs without touching existing), `redo` (replace all children — current set kept as prior to avoid). |
| `/and-cast` | yes | `revise` (swap/add/retire; new actors get fresh margit Phase 4 provisioning — working dir + LTM + STM + state + vibes; retired actors are decommissioned to `actors/<slug>-decommissioned-<timestamp>/`; untouched actors are left as-is) / `redo` (margit decommissions full current roster, full re-provisioning from scratch). |
| `/and-write` | yes | Per-chapter. `revise` (re-decompose specific scenes flagged SIGNAL by bone-gate, or re-write specific bone ranges) / `redo` (full rewrite — preserves scene chunks, replaces all bones). |
| `/and-review` | yes (idempotent) | Any subcommand can be re-fired any number of times. Each invocation persists a new timestamped report; nothing else is mutated. `verdict` subcommand updates `books[<slug>].orchestrator_critic_verdict` in place. |
| `/and-stitch` | yes (lightly mutated) | Per-chapter. Re-running re-runs the full eight-phase pipeline. No new revise mode in this overhaul; the one narrow mutation is Phase 0 tensometer-fallback removal. |

**Phase 0 protocol for re-runnable commands:**

1. Read upstream inputs. Abort if upstream missing.
2. Check own output. If populated, prompt mode (`revise` / `add` where applicable / `redo`).
3. Cascade warning. Surface downstream blocks that depend on what's about to change; offer staleness-marking (see "Surfacing" below).
4. Run.

**Surfacing — defined.** When Phase 0 detects downstream work that depends on the about-to-change output, "surface" means: (a) print a numbered list of the affected downstream artifacts (chunks, bones files, verdict block) with their slugs and last-write timestamps; (b) prompt the user to choose `mark-stale` (write `stale_since: <iso-timestamp>` on each affected downstream block; leave content intact) / `keep-fresh` (leave staleness fields null; user accepts that downstream may be silently outdated) / `abort` (cancel the re-run). Default is `mark-stale`. The chosen mode is recorded in showrunner memory under `staff/showrunner/staleness-log.md` (one entry per cascade event: who-ran-what, what was marked, user choice).

When a downstream command next runs and reads a parent block with `stale_since` set, it prints a warning line ("parent <slug> stale since <timestamp>; consider re-running parent first") but does NOT block. Stale-marking is informational, not enforcing.

**Staleness cascade across /and-substance levels + /and-write.** Re-running `/and-substance series` `redo` stale-marks every `/and-substance book` output. Re-running `/and-substance book b01` `redo` stale-marks every `/and-substance chapter` under b01. Re-running `/and-substance chapter b01c01` `redo` stale-marks every `/and-write` bones file whose source scenes sit under b01c01. Each level's `stale_since: <iso-timestamp>` field is surfaced when that level next runs. No silent overwrites of downstream work.

**Staleness also invalidates the orchestrator-critic verdict.** Any `/and-substance` or `/and-write` re-run whose scope is at-or-under a book that already has an `orchestrator_critic_verdict.ruling` set MUST stale-mark that verdict block (`books[<slug>].orchestrator_critic_verdict.stale_since: <iso-timestamp>`). A PASS verdict sitting on top of substance that has been redone underneath is a false signal; the stale flag forces re-judgment via `/and-review verdict <book>` before the verdict is trusted again. `/and-review verdict` Phase 0 warns (not blocks) if it sees an existing stale verdict; re-running it clears the stale flag on PASS/PASS-WITH-NOTES/FAIL re-issue.

### Re-runnability edge cases (Hole F)

Three edge cases the bare re-run protocol leaves under-specified. Each resolved here so the implementer doesn't need to invent during command-body authoring.

**(F1) SIGNAL → revise trigger.** `/and-write` Phase 6 (substance bone-gate) classifies findings as HARD / SIGNAL / TASTE. HARD blocks emission and forces revise in the same `/and-write` run. SIGNAL records but passes — the bones ship. But SIGNAL findings should still be available as later revise triggers; otherwise SIGNAL becomes a "logged and forgotten" failure mode.

Resolution: every SIGNAL finding lands in `chapters[].scenes[].bones[].gate_verdict.signals[]` (the existing `gate_verdict` block extends to carry a `signals: [<finding-class>]` list alongside the `bonefide` / `flat` PASS-only fields). `/and-write revise` mode accepts a `--from-signals` flag (or, by default at Phase 0, prompts the user when SIGNAL findings are present): list the SIGNAL-flagged bones / scenes, offer to re-decompose only those. The user picks any subset; revise scopes to that subset. Without the flag, revise mode falls back to its current behavior (re-decompose explicitly-named scenes, or re-write explicitly-named bone ranges). `/and-review bones <chapter-slug>` post-hoc re-fire re-evaluates the same SIGNAL list against the current memory state; SIGNALs that no longer apply are auto-cleared from the gate_verdict block.

**(F2) `/and-substance --cascade` checkpoint payload (minimum sketch).** Implementation detail lands in the `/and-substance` command body, not here. But the implementer needs at minimum a sketch so the checkpoint format is consistent across resume scenarios:

```yaml
# staff/showrunner/cascade-checkpoint.md
# Written after each child chunk completes inside --cascade
cascade:
  root: <book-slug-or-chapter-slug>     # the slug --cascade was invoked at
  invoked_at: <iso-timestamp>
  invoked_command: /and-substance book b01 --cascade
  last_completed:
    level: book | chapter | scene | bones    # last unit successfully persisted
    slug: <slug>
    completed_at: <iso-timestamp>
  next:
    command: /and-substance chapter b01c05 | /and-write b01c05 | ...
    args: [<positional-args>]
  reason: continue | halted-on-failure | halted-on-cut
  failure: <one-line description if reason=halted-on-failure> | null
```

`/and-cut` mid-cascade writes the same file with `reason: halted-on-cut`. `/and-substance <root> --cascade --resume` reads the checkpoint and re-fires from `next.command`. `/and-substance <root> --cascade` (no `--resume`) without a fresh `last_completed` for the root runs from the beginning; with a stale checkpoint older than the root's `stale_since` it warns and offers `--resume` or `--restart`.

**(F3) `gate_verdict` lifecycle under partial revise.** Phase 0 of `/and-write revise` clears `gate_verdict` so Phase 6 can re-fill on PASS. But partial revise (re-decompose only scenes 2 and 4 of a 5-scene chapter) creates a mixed state — scenes 1, 3, 5 still have their prior PASS verdicts; scenes 2, 4 need re-verification.

Resolution: **per-scene clear, not per-chapter clear.** `/and-write revise` Phase 0 clears `gate_verdict` only on bones inside scenes scoped by the revise target. Scenes not in the revise scope keep their prior `gate_verdict.bonefide: true` / `flat: false`. Phase 6 re-runs the bone-gate against the union of (revised scenes' new bones) + (unchanged scenes' existing bones), but only the revised-scene bones can produce new gate_verdict writes; unchanged-scene verdicts are not touched. Phase 6 audience review (3 personas) per scene window still fires across the whole chapter — the scene-window audience is sensitive to cross-scene felt-substance, so re-evaluation across the full chapter is the right scope even when bones changed in only a subset. Aggregate `substance_bone_gate_verdict` at chapter level is PASS only if every scene's bones pass; on partial-revise FAIL on an unchanged scene (rare — implies prior verdict was wrong), the unchanged scene auto-promotes into the revise scope and its `gate_verdict` clears.

---

## Archive plan

```
git mv .claude/commands/and-project.md             archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md              archive/commands/and-season-dissolved.md
git mv .claude/commands/and-wrap.md                archive/commands/and-wrap-polish-deferred.md
git mv .claude/commands/and-protolines.md          archive/commands/and-protolines-pre-substance.md
git mv .claude/commands/and-protolines-v2.md       archive/commands/and-protolines-v2-lifted-to-and-write.md
git mv .claude/commands/and-protolines-season-v2.md archive/commands/and-protolines-season-v2-lifted-to-and-substance-cascade.md
```

**Archive suffix conventions (revised):**
- `-pre-substance` — overhaul or rename of a command that has a successor (`/and-project`, `/and-protolines`).
- `-dissolved` — command whose jobs migrated piecewise into other commands and isn't coming back as a standalone (`/and-season`).
- `-polish-deferred` — command whose spec is intentionally preserved for future revival (`/and-wrap`). Its Phase 2 (8-class auditor pass) and Phase 3 (editor allowed-moves contract + procedure) are the un-defer lift targets for `/and-review prose` + future polish revival. Do NOT mark this as dissolved — the spec is the deferral artifact.
- `-lifted-to-<command>` — command body is the primary lift source for a successor (`/and-protolines-v2` → `/and-write`; `/and-protolines-season-v2` → `/and-substance --cascade`). The archive copy is the canonical reference the implementer reads while writing the successor.

`/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review` are not "net new from scratch" — they are each a lift-and-adapt of one or more archived assets plus a small named delta. See "Asset reuse map" above for the per-command lift sources.

Update `archive/commands/README.md`:

> **2026-05-16 — substance overhaul.** Two reasons. (1) The pre-substance chain optimized per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but had no declared substance contract; episodes shipped through it were structurally clean and substance-flat. (2) `/and-project` conflated scope with series content; `/and-season` conflated recursive chunking (book→chapter→scene) with bone-writing and emission; `/and-wrap`'s editor pass produced marginal lift on top of `/and-stitch`'s existing Phase 7 editorial reflection. Replacement chain: `/and-project` (scope+staff) → `/and-series` (series chunk + structural prompts) → `/and-substance series` (signature + per-book Δ) → `/and-cast` (roster) → series-level audit checkpoint → `/and-substance book/chapter` (recursive chunker authoring; three invocation levels; four chunk levels stopping at scene) → `/and-write` (scene-decomposition into bones-with-deltas + five-pass SVO + substance bone-gate; emits flat-integer-ID bones file + scene-map facet; replaces `/and-protolines`) → `/and-facets` (tensometer dropped; scene-map derivation downgraded to validation) → `/and-stitch` (tensometer-fallback removed from Phase 0). The bone is the smallest substance unit — it carries its own declared axis-movement; the former "beat chunk" planning level is collapsed into the bone itself. `/and-review` is the universal review primitive with subcommand router (includes `verdict <book>`, absorbing the former `/and-judge-book`). Dissolved: `/and-season` (into `/and-substance` + `/and-write`); `/and-wrap` (polish concerns deferred entirely until upstream substance machinery is proven; `/and-stitch`'s `draft/<chapter>.md` is the terminal deliverable); `/and-judge-book` (into `/and-review verdict`). Renamed-overhauled: `/and-protolines` → `/and-write`. URI-026 tens-gate replaced by `/and-write` substance bone-gate; tensometer facet retired. See `design/substance/`.

---

## New artifacts

### `design/substance/README.md`

Framework reference. Authoring authority for substance terminology, state-axis catalog, 1–9 scale anchors, Δ/cost/density definitions, plot-by-states + plot-by-action duality, perspective-bound measurement, antagonist-pressure, failure-mode catalog, pipeline-threading map. **Includes the recursive `/and-substance` design at three invocation levels** (`series` / `book` / `chapter`) producing four chunk levels (series → book → chapter → scene), **plus the `/and-write` scene-decomposition principle**: the bone IS the smallest substance unit (each bone carries one axis-movement with declared cause), `/and-write` decomposes scene chunks into bones, the former "beat chunk" planning level is collapsed into the bone itself.

**Chapter ≈ episode mapping** (carved in from intent-gaps item #10, for user mental-model continuity): include a paragraph near the top of the README — *"A chapter is the terminal unit of consumption. One chapter ≈ one previous episode in scope and length — roughly 3000–5000 words across 1–3 scenes. Reader feedback authored against 'episodes' (s01e01, s01e02, ...) maps to chapter-level concerns under the new chain; books map to the prior season concept. The 'season'/'episode' framing is dropped from command bodies, schemas, and design docs, but is documented here once for the bridge."*

### `design/substance/questionnaire.md`

1–9 archetype questionnaire (story / protagonist / world / antagonist) used by `/and-substance` at any level to pin axis ranks honestly. Per-archetype question banks. Example scoring trace.

### `design/substance/delta-targets.md`

Per-chunk Δ targets + bone-count bands.
- Series-scale Δ across the signature.
- Book-scale Δ per book by position (opening / mid / climax / denouement).
- Chapter-scale Δ.
- Scene-scale Δ.
- Per-bone Δ — typical magnitude (one axis +/− one rank; occasionally two axes); guidance on when a bone earns more.
- Bones-per-scene target (5–15 default), scenes-per-chapter target (1–3 default — scenes are substantial, per user feedback).
- Curve commentary: density is a curve across a chunk, not a constant. Within a scene, bones cluster — opening bones may be lower-Δ (setup), climactic bones higher-Δ (the scene's hinge action).

### `schemas/showrunner-memory.schema.md` (updated)

New top-level `project:` block (scope+staff from `/and-project`):
```yaml
project:
  brief: <one-line distill>
  constraints:
    settings: [...]
    themes_as_bounds: [...]
    hard_fences: [...]
  staff:
    audience: [<slug>, <slug>, <slug>]
    screen_writer: <persona-or-default>
    dramatist: <persona-or-default>
    auditor: <persona-or-default>
    editor: <persona-or-default>
    orchestrator_critic: <card-version>
```

Restructured `series:` block:
```yaml
series:
  # from /and-series
  chunk: |
    <substance-bearing prose paragraph>
  structure:
    book_count: <N>
    book_length:
      chapters_per_book: <range>           # e.g. 4-8
      scenes_per_chapter: <range>          # e.g. 1-3 — scenes are substantial; per user feedback "a scene should be most of a chapter"
      bones_per_scene: <range>             # e.g. 5-15 — bones are scene-action-sized; each bone declares one axis-movement
    cyclical: true | false
    pov: single | multi | rotating-per-book
    cross_book_continuity: { recurring_antagonists: [...], ongoing_subplots: [...] }
    world_evolution: static | evolving
    series_end_shape: definitive | open-ended | ambiguous | tragic | triumphant
  laws: [...]
  lore: [...]
  behaviors: [...]

  # from /and-substance series
  substance:
    state_axes:
      - slug: <axis-slug>
        dimension: <one line>
        one_means: <one line>
        five_means: <one line>
        nine_means: <one line>
        perspective: protagonist | antagonist | world
        start_rank: <1-9>
        end_rank: <1-9>
    cost_ledger:
      - gain: <axis-slug> +<delta>
        cost: <axis-slug> -<delta> | opportunity-missed:<one line> | journey-required:<one line>
        anchor:                                # fine-grained anchor; populate from the level where the cost is paid
          book: <book-slug>
          chapter: <chapter-slug> | null       # null when cost spans the whole book
          scene: <scene-slug> | null           # null when cost spans the whole chapter
        # `/and-write` Phase 6 (substance bone-gate) verifies "for each scene under the chapter:
        # cost-ledger entries are paid by visible bones" — that check resolves against the
        # finest-grained anchor populated. Authored top-down: `/and-substance series` writes
        # book-anchored entries; `/and-substance chapter`/`scene` may refine them by populating
        # the deeper fields. See `design/substance/README.md` for the refinement protocol.
    antagonist_pressure:
      - axis: <axis-slug>
        pressure_source: <one line>
        cost_curve: <one line>
    chunk_targets:
      series:  { delta_per_signature_axis: <range>, density_target: <range> }
      book:    { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      chapter: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      scene:   { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      bone:    { delta_per_axis: <range>, axes_per_bone: <range> }   # typical 1-axis ±1 rank; occasionally 2-axis

  # from /and-cast
  cast_roster: [...]
  stage_elements: [...]
```

Recursive nesting under `books[]` (replaces `seasons[]`). Each chunk-count decision lands at its parent's invocation: `/and-substance series` decides `books[*].structure.chapter_count`; `/and-substance book` decides `chapters[*].structure.scene_count`. Scenes are the deepest chunker output; `/and-write` decomposes each scene into `bones[]` with per-bone deltas at write-time. Counts must fall inside the ranges declared in `series.structure.book_length`.

```yaml
books:
  - slug: b01
    chunk: |
      <book chunk authored by /and-substance series>
    structure:                             # populated by /and-substance series Phase 2
      chapter_count: <N>                   # picked inside series.structure.book_length.chapters_per_book
    substance_delta:                       # from /and-substance series Phase 3
      axes_in_motion: [...]
      density_target: <range>
    stale_since: <iso-timestamp> | null    # set when /and-substance series re-runs with `redo` after persistence
    # from /and-substance book
    drama: |
      <"what cannot survive this book" statement>
    chapters:
      - slug: b01c01
        chunk: |
          <chapter chunk authored by /and-substance book>
        structure:                         # populated by /and-substance book Phase 2
          scene_count: <N>                 # picked inside series.structure.book_length.scenes_per_chapter
        substance_delta:                   # from /and-substance book Phase 3
          axes_in_motion: [...]
          density_target: <range>
        stale_since: <iso-timestamp> | null
        status: planned                    # Hole C — chapter-status state machine (see enum below); set by each authoring/review phase as the chapter advances
        # from /and-substance chapter Phase 3 (pov_narrator) + Phase 4 (dramatic_shape, goal)
        pov_narrator: <actor-slug>         # resolved from series.structure.pov; populated on every chapter so /and-write can write the bones-file `narrator:` header
        dramatic_shape: <rising | climax | falling | hinge | ...>
        goal: <one-line "what this chapter shows the audience"; bones-file `goal:` header source>
        # carved in from intent-gaps item #6 (s01e02/e03 "episodes barely fit together") — cross-chapter handoff
        handoff_in:                        # state inherited from prior chapter; verified by /and-write Pass 5 continuity + /and-substance book Phase 5 dramatist
          open_threads: [...]              # plot threads carried over (e.g. "investigation of missing key unresolved")
          world_state: [...]               # world-state items relevant at chapter open (e.g. "siege siege-engine moved to north wall")
          character_state: [...]           # protagonist + cast axis ranks + active conditions at chapter open (e.g. "maya: emotional=3 grieving; tomas: trust-in-maya=2")
          source_chapter: <prior-chapter-slug> | null   # `null` only for the first chapter of the first book
        handoff_out:                       # state exposed to next chapter; same shape as handoff_in
          open_threads: [...]
          world_state: [...]
          character_state: [...]
          target_chapter: <next-chapter-slug> | null    # `null` only for the last chapter of the last book
        scenes:
          - slug: b01c01s01
            chunk: |
              <scene chunk authored by /and-substance chapter — substantial; one scene typically fills most of a chapter>
            substance_delta:               # from /and-substance chapter Phase 3
              axes_in_motion: [...]
              density_target: <range>
            scene_conflict:                # from /and-substance chapter Phase 3 — sibling of substance_delta; added per user-feedback "scenes should have meaningful suspense and action with something against something"
              protagonist_force: <one line>
              opposing_force: <one line>
              stakes_axis: <axis-slug>
            stale_since: <iso-timestamp> | null
            bones:                         # from /and-write Phase 1 (scene-decomposition); per-bone state-delta lives here in memory, NEVER in the flattened bones file
              - slug: b01c01s01n01        # n-prefix for bones (b would collide with book); the authoring/audit handle
                flat_id: <int>             # assigned at /and-write Phase 7 serialization (scene-order monotonic, file-scoped); the file/citation handle that /and-facets writes `[<facet>:<flat_id>]` against
                svo: |
                  <one-line subject-verb-object bone — scene-action-sized; e.g. "maya confronts tomas" or "taylor-hebert speaks to septon-dying-protector" for a dialogue bone>
                substance_delta:           # per-bone — the smallest substance unit; consumed by /and-write Phase 6 bone-gate and /and-review bone <slug>; NOT written to the flattened bones file
                  axis_moves:
                    - axis: <axis-slug>
                      direction: + | -
                      magnitude: <1-3>     # typical ±1; ±2-3 for hinge bones
                  cost:                    # may be null when the bone is paying a prior gain rather than incurring new cost
                    axis: <axis-slug> | null
                    direction: -
                    magnitude: <1-3>
                  cost_ledger_anchor: <cost-ledger-entry-id> | null  # link to series.substance.cost_ledger when this bone pays one
                gate_verdict:              # filled by /and-write Phase 6 ONLY on PASS; cleared at /and-write Phase 0 on revise/redo before re-firing Phase 6
                  bonefide: true           # does the SVO actually cause the declared Δ? Only PASS is persisted; HARD findings block Phase 7 emission so the bone doesn't ship.
                  flat: false              # SUBSTANCE-FLAT on this bone — only PASS state (false) is persisted
        # chapter-level fields filled by /and-write
        bones_file: theater/bones/b01-c01.md
        bones_count: <N>
        substance_bone_gate_verdict: PASS | FAIL-<reason>
        substance_delta_measured:          # post-bones aggregate
          axes_moved: [...]
          density_measured: <ratio>
          felt_verdict: SUBSTANCE-FELT | SUBSTANCE-FLAT-<axis> | SUBSTANCE-SUSPECT-cheap-gain-<axis>
    # book-level field filled by /and-review verdict <book-slug>
    orchestrator_critic_verdict:
      ruling: PASS | PASS-WITH-NOTES | FAIL
      report_path: staff/reviews/verdict-<book-slug>-<timestamp>.md
      verdict_at: <iso-timestamp>
      stale_since: <iso-timestamp> | null   # set when any /and-substance or /and-write under this book re-runs after the verdict was recorded
```

**Bones as scene-children, not flat-per-chapter.** The source of truth is `chapters[].scenes[].bones[]` in showrunner memory. The per-chapter file `theater/bones/<book>-<chapter>.md` is a **flattened view** emitted by `/and-write` Phase 7 for downstream `/and-facets`/`/and-stitch` consumption — bones serialized in scene order with flat integer IDs, no scene markers in body (the co-emitted scene-map facet at `theater/facets/scene-map-<book>-<chapter>.md` carries scene boundaries as flat_id ranges so `/and-facets` Phase 4d can validate coverage without re-deriving). If schemas and memory disagree, memory wins; both file artifacts are regenerated from memory.

**`chapters[].status` enum (Hole C — chapter-status state machine).** Replaces the per-episode status-line in the prior schema (`episodes[].status: written | active | planned | protolined`) and folds in the extended state-machine markers currently set inline by `/and-facets:74-78` and `/and-stitch:100`. Valid values, in monotonic order along the chapter's lifecycle:

| status | set by | meaning |
|---|---|---|
| `planned` | `/and-substance book` Phase 6 persist | Chapter chunk + per-chapter Δ written; scenes not yet authored. |
| `scened` | `/and-substance chapter` Phase 6 persist | Scene chunks + per-scene `substance_delta` + `scene_conflict` + `pov_narrator` + `dramatic_shape` + `goal` + `handoff_in/out` populated; bones not yet authored. |
| `bones-written` | `/and-write` Phase 7 emit (post-bone-gate PASS) | Bones authored across all scenes; bones file + scene-map facet emitted; `bones_file` + `bones_count` + `substance_bone_gate_verdict: PASS` recorded. |
| `faceted-r1` | `/and-facets` R1 fanin | R1 facet rubrics applied; per-facet outputs at `theater/facets/<facet>-<book>-<chapter>.md`. |
| `audited-r1-mechanical` | `/and-facets` mechanical-audit pass | Bone-citation accrual + body-integrity + slice consolidation passed. |
| `audited-r1` | `/and-facets` audience-gate verdict PASS | URI-DIALOGUE-COVERAGE-GATE + URI-SCENE-WINDOW + audience-gate re-verified. |
| `faceted-r2` | `/and-facets` R2 fanin | R2 facets applied (refinement pass). |
| `stitched` | `/and-stitch` Phase 8 finalize | `draft/<book>-<chapter>.md` (clean) + `draft/<book>-<chapter>.annotated.md` emitted. |

`wrapped` was on the prior episode-status table; it is omitted here because `/and-wrap` is dropped under this overhaul. If polish is revived (per the deferred `/and-review prose` un-defer target), a `polished` status appends to the tail of the enum at that time.

**State-machine transitions.** Each value advances monotonically; status only ever moves forward. Re-running a command that has already advanced past its own status (e.g. re-running `/and-facets` on a `stitched` chapter) is allowed in `revise`/`redo` modes — Phase 0 of the re-running command resets status to the earliest value it owns (`/and-facets` resets to `bones-written`, `/and-stitch` resets to `audited-r1` or whichever R2 state was last reached, etc.) and the staleness-cascade rules mark downstream as stale per "Surfacing — defined." Re-run mode-resets are recorded in `staff/showrunner/staleness-log.md` alongside the cascade entry.

**Resume-point detection.** `/and-facets` Phase 0 reads `chapters[<slug>].status` to determine whether to resume R1 / R2 / mechanical-audit / audience-gate. `/and-stitch` Phase 0 reads the same field to confirm `audited-r1` (or `faceted-r2`) is reached before running. Phase 0 of any command aborts if the parent status is below its own minimum precondition (e.g. `/and-stitch` aborts on `planned` or `scened`).

---

## Command specs

### `/and-project` (overhauled — strict scope + staff)

Three jobs only:

1. Scaffold (directory tree, stub files, audience working dirs).
2. Project scope (Phase 1.5 brief expansion, Phase 2 1a constraints, Phase 2 1b open-question resolution, Phase 2 1d world-law finalization). Output: `project.constraints` block + `staff/showrunner/world-notes.md` + condition cards.
3. Staff selection (audience ×3 + screen-writer / dramatist / auditor / editor / orchestrator-critic library defaults bound to this project). Output: `project.staff` block.

Does NOT do: cast, series chunk, structural prompts, substance signature, audit checkpoint.

Output: project-scope-approval checkpoint. Human reviews. On approval, `/and-series` next.

Estimated size: ~50% of current `/and-project`.

### `/and-series` (extracted from `/and-project` + structural prompts)

**Lift basis:** Open `archive/commands/and-project-pre-substance.md` Series Plan section + Phase 3 Present-results. Phases 2-4 below are content relocation from there. Phase 1 (structural prompts) is the only net-new authoring step.

1. Phase 0 — Validate + mode select. Read `project:` block; abort if scope/staff incomplete. If `series.chunk` populated, prompt `revise`/`redo`. If downstream populated, surface cascade and offer staleness-marking.
2. Phase 1 — Structural prompts. Interactive: book count, book length (chapters per book + scenes per chapter + bones per scene), cyclical?, POV, cross-book continuity, world evolution, series-end shape. Persist to `series.structure.*`.
3. Phase 2 — Series chunk authoring. Screen-writer takes project scope + structure. Produces a brief substance-bearing prose paragraph (Star-Wars-trilogy-style). Substance implicit, not yet measured.
4. Phase 3 — Review. Audience + dramatist accept/revise loop (3-try cap).
5. Phase 4 — Persist `series.chunk` + `series.structure.*`. No checkpoint here.

Estimated size: ~100-130 lines total — ~50 net-new (structural prompts) + ~50-80 lifted from `/and-project` Series Plan section.

### `/and-substance` (generalized + recursive, three invocation levels)

**Lift basis:** Open `archive/commands/and-season-dissolved.md` Phase 1 (lines 44-131) for the chunker authoring loop (read parent → author children → review → persist) and Phase 3 (lines 224-302) for the parallel-fork review-sweep dispatch pattern. Phases 1, 2, 5, 6 below are direct lifts with parameterization. Phase 3 (substance-contract authoring) and Phase 4 series-level signature authoring are the net-new work. `--cascade` flag adapts the per-episode loop from `archive/commands/and-protolines-season-v2-lifted-to-and-substance-cascade.md`.

**Four chunk levels exist** (series → book → chapter → scene); **three invocation levels** author them (`series` produces book chunks; `book` produces chapter chunks; `chapter` produces scene chunks). Scenes are produced but never invoke — they are the deepest chunks and are consumed by `/and-write`, which decomposes each scene into bones (the bones live in `scenes[].bones[]`; per-bone deltas are authored by `/and-write`, not `/and-substance`).

Single command body. Argument is the invocation level: `series` / `book <slug>` / `chapter <slug>`. Same seven-phase shape at every level.

**Common phases (every level):**

1. **Phase 0 — Validate + mode select.** Read upstream chunk + parent substance commitment. Abort if upstream missing. If own output populated, prompt `revise` / `add` (where applicable) / `redo`. If downstream chunks or `/and-write` bones exist, surface cascade + offer staleness-marking.
2. **Phase 1 — Read parent.** Series: read `series.chunk` + structural commitments. Book: read book chunk + per-book Δ. Chapter: read chapter chunk + per-chapter Δ.
3. **Phase 2 — Author sub-chunks.** One prose paragraph per child unit. Series → per-book chunks. Book → per-chapter chunks. Chapter → per-scene chunks (substantial; scenes typically fill most of a chapter, 1–3 scenes per chapter default).
4. **Phase 3 — Author sub-chunk substance contracts.** For each sub-chunk: which axes shift, direction, target Δ-magnitude, cost, density target. **Chapter level additionally authors per-scene `scene_conflict`** (protagonist_force / opposing_force / stakes_axis) so every scene has named opposition. **Chapter level also authors `chapters[].pov_narrator`** (per `series.structure.pov`: `single` → inherited from series; `rotating-per-book` → inherited from book; `multi` → picked per chapter from the cast roster); always populated on every chapter so `/and-write` Phase 7 can write the bones-file `narrator:` header without further lookup.
5. **Phase 4 — Level-specific extras.** Series: authors the signature itself (state axes, anchors, cost ledger, antagonist pressure). Book: authors the book drama statement. Chapter: authors the chapter dramatic shape (rising / climax / falling / hinge) and `chapters[].goal` — a one-line "what this chapter shows the audience" string distilled from the chapter's substance contract + dramatic-arc completion. The `goal` is the per-chapter north star Pass 4 (trim) and downstream `/and-facets` Phase 0 consume as the bones-file `goal:` header field.
6. **Phase 5 — Chunk-quality review.** Audience + dramatist + auditor at this level. Accept/revise loop (3-try cap). **Audience:** does this chunk feel substantive — does the named Δ feel earned, the cost feel real, the meaningfulness land? `SUBSTANCE-FELT` vs `SUBSTANCE-FLAT-<axis>` vs `SUBSTANCE-SUSPECT-cheap-gain-<axis>`. **Dramatist:** is the chunk shape sound? Do the children fit within the parent's Δ? Scenes-not-too-small (chapter-level check)? Cyclical / cross-book / structural commitments honored? Chapter has dramatic-arc completion? **Book-level dramatist additionally verifies cross-chapter handoff** (carved in from intent-gaps item #6, s01e02/e03 "episodes barely fit together"): for every chapter pair (N, N+1) under the book, `chapters[N].handoff_out` is consistent with `chapters[N+1].handoff_in` — same open-threads list, same world-state items, same character-axis ranks at the boundary. Mismatches (orphan threads in `handoff_in`, dropped threads in `handoff_out`, character-axis discontinuity without an authoring cause) HARD-fail and force revise on the offending chapter chunks. **Auditor:** does the chunk text match the substance contract (no rank claim without described cause; cost-ledger consistency)?
7. **Phase 6 — Persist.** Write chunks + contracts to showrunner memory at this level's nesting depth. **No bones at any level** — bones are written by `/and-write`.

**`--cascade` flag (book/chapter levels).** Default off (manual level-by-level invocation). With `--cascade`, `/and-substance book b01` auto-fires `/and-substance chapter` for each chapter under b01, then `/and-write` for each chapter (each `/and-write` invocation reads the chapter's scenes and authors bones). Reviews still fire at each level; failure at any level halts the cascade. Useful for late-stage runs where the substance contract is settled and the user wants one command to drive everything to bones.

Estimated size: ~350-400 lines total — ~150-180 net-new (substance-contract authoring + series-level signature authoring + recursion glue + cascade flag) + ~200 lifted from `/and-season` Phases 1, 3.

### `/and-cast` (extracted from `/and-project` Phase 2 1c + Phase 3 + revise routing)

**Lift basis:** Open `archive/commands/and-project-pre-substance.md` Phase 2 1c (Candidate menu + cast selection, lines 256-310) for Phases 1-4 below, and Phase 3 (Present results, lines 311-342) for Phase 5. Margit provisioning logic lifts from current `/and-project.md` Phase 1 step 4. The `revise`/`redo` decommission-routing is the only net-new authoring.

1. Phase 0 — Validate + mode select. Read `series.chunk` + `series.structure.*` + `series.substance.*`. Abort if upstream missing. If `series.cast_roster` populated, prompt `revise` (swap/add/retire — untouched actors are preserved as-is; added actors flow through Phases 1–4 normally; retired actors are decommissioned by margit to `actors/<slug>-decommissioned-<timestamp>/`; swapped actors are retire+add in one pass) / `redo` (margit decommissions the full current roster, then re-run Phases 1–4 from scratch).
2. Phase 1 — Substance-driven cast brief. Screen-writer composes brief from chunk + signature: which axes need which carriers. In `revise` mode, the brief is scoped to the requested swap/add/retire delta only.
3. Phase 2 — Margit candidate menu (filtered from `cards/personas/INDEX.md`). Skipped for actors being retired.
4. Phase 3 — Screen-writer selection + dramatist viability check. Viability check considers the full post-revise roster, not only the added actors.
5. Phase 4 — Margit provisioning (actor working dirs, LTM/STM/state/vibes). Fresh provisioning for every added actor; untouched actors keep their existing working dirs unchanged.
6. Phase 5 — Series-level audit checkpoint. Auditor (fork) against full picture (project scope + series chunk + structural commitments + signature + per-book Δ + cast). Result to user. On approval, `/and-substance book b01` next.

Estimated size: ~150-180 lines total — ~30 net-new (revise/redo decommission-routing + checkpoint-payload extension) + ~120-150 lifted from `/and-project` Phase 2 1c and Phase 3.

### `/and-write` (lifted from `/and-protolines-v2` + scene-decomposition + substance bone-gate)

**Lift basis:** Open `archive/commands/and-protolines-v2-lifted-to-and-write.md` and copy Passes 1-5 wholesale; the five-pass SVO pipeline is unchanged and the per-pass fork briefs at `design/shoot-v2/svo-writer-pass{1..5}-brief.md` are preserved as-is. Open `archive/commands/and-season-dissolved.md` Pass S10 bone-gate (lines 460-499) for Phase 6's verification-shape (adapt tens-correlation to substance-contract), and Phase 7 Steps 1-3 (lines 616-676) for the flat_id assignment + per-chapter file emission logic. Net-new authoring: Phase 1 scene-decomposition (front-loaded, ~80 lines) and the substance-contract verification logic inside Phase 6 (~80 lines) and scene-map co-emission inside Phase 7 (~30 lines).

Reads scene chunks + substance contracts produced by `/and-substance chapter`. **Decomposes each scene into bones-with-deltas, then SVOs them.** Produces the per-chapter bones file. Replaces `/and-protolines` as the shoot-v2 chain entry.

**Phases (per chapter):**

1. **Phase 0 — Validate + mode select.** Read all scene chunks under the chapter. Abort if any scene is unsubstanced (`substance_delta` missing or `scene_conflict` unpopulated). If `theater/bones/<book>-<chapter>.md` already exists, prompt `revise` (re-decompose specific scenes flagged SIGNAL by bone-gate, or re-write specific bone ranges) / `redo` (full rewrite — scene chunks preserved, all bones replaced). **Behavior-card directory (Hole H):** the lifted Phase 0 step that resolves voice/tic cards reads `cards/dialects/INDEX.md` (the current path). CLAUDE.md's Agent routing table flags a pending `dialects/ → behaviors/` rename — **deferred** under this overhaul, not lockstep. The lifted step continues to read `cards/dialects/INDEX.md`; the rename is a separate follow-on issue, tracked alongside the OOS items below. If the rename lands first independently, this Phase 0 step picks up the new path with a one-line edit.
2. **Phase 1 — Scene-decomposition (the work that used to be `/and-substance scene`).** For each scene chunk: decompose into N bones (within `series.structure.book_length.bones_per_scene` range, typical 5–15). Each bone declares one axis-movement (occasionally two) with declared cost and links to the cost-ledger when applicable. Bones are scene-action-sized — one scene-significant action per bone, not micro-beats. The scene's substance contract is the aggregation target: per-axis sum of bone-Δ must equal the scene's declared Δ within ±1 rank.
3. **Phase 2 — Constraint audit.** Verify each bone's declared Δ is well-formed (no rank claims without parent-cost backing; no axis movements outside the scene's contract; no costs unaccounted-for in the cost ledger). Verify aggregate-bones-Δ ≈ scene-Δ per axis.
4. **Phase 3 — Shape (SVO writing).** For each bone, author the SVO craft: subject-verb-object, line economy, voice-consistent, governed by `schemas/bones.schema.md § field rules` (harsh-SVO discipline: no copulas, no negations, no perception verbs, no modifiers, no conjunctions, no interiority, no compound objects). **Speech bones** — any bone whose declared axis-movement is communication-mediated (community / knowledge / reputation / trust class) — MUST take the licensed dialogue form `<speaker-slug> speaks to <listener-slug>`. This is the URI-DIALOGUE-COVERAGE-GATE anchor; non-`speaks to` speech forms (`says`, `tells`, `whispers`, etc.) are banned. Conversely, a `speaks to` bone whose substance_delta lists only physical-action axes is malformed — speech bones must move at least one communication-class axis.
5. **Phase 4 — Trim.** Drop bones that don't cause Δ (chatter bones — schema violation, not just style). Bones for setup/transition are allowed only if they pay a later gain (cost-ledger link required). Capped at density-target ratio.
6. **Phase 5 — Continuity audit.** State-thread check across bones (props move, actors track, conditions persist). Cross-scene continuity within the chapter (handoff from scene N to scene N+1).
7. **Phase 6 — Substance bone-gate.** **Replaces URI-026 tens-gate.** For each bone: verify the declared axis movement is **bonefide** (SVO actually causes named Δ; no rank claim without visible cause; otherwise `SUBSTANCE-FLAT-<axis>` HARD). For each scene: verify per-axis Δ delivered within ±1 rank of contract; verify `scene_conflict.opposing_force` is visible in the bones (something is *against* something). For each scene under the chapter: verify cost-ledger entries are paid by visible bones (`SUBSTANCE-SUSPECT-cheap-gain-<axis>` HARD if cost not visible). Audience review (3 personas) per scene window: `SUBSTANCE-FELT` PASS / `SUBSTANCE-FLAT-<axis>` HARD / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` HARD. **HARD/SIGNAL classification:** flat-bones, cost-not-paid, missing-opposing-force, per-axis-Δ-mismatch-beyond-±2 → HARD (blocks emission). Bones-count-below-density-target, per-axis-Δ-mismatch-within-±1-to-±2, chatter-bones-just-over-cap → SIGNAL (records but passes).
8. **Phase 7 — Emit + downstream-gate pre-verify + scene-map co-emit.** Two artifacts written, both derived from `chapters[].scenes[].bones[]` in showrunner memory (source of truth stays in memory):

   **(a) Flattened bones file** at `active-project/theater/bones/<book>-<chapter>.md`. Conforms to `schemas/bones.schema.md` (renamed from `schemas/proto-line.schema.md`; format preserved for downstream `/and-facets`/`/and-stitch` compatibility):
   - **Flat integer IDs.** At serialization, walk scenes in order and assign each bone a monotonic positive integer `flat_id`, starting at 1, file-scoped. The in-memory bone slug (`b01c01s01n01`) is the authoring/audit handle; the flat_id is the file/citation handle. The `flat_id ↔ slug` map is persisted on `bones[].flat_id: <int>` so reviewers can cross-walk. Re-running `/and-write redo` produces the same flat_ids as long as scene/bone counts are stable; revise mode preserves flat_ids for unchanged bones (revised bones get new flat_ids at end of the chapter or via gap-filling — pick gap-filling to keep monotonicity tight).
   - **Full 7-field header** (same as the existing schema's extended header — `/and-facets` Phase 0 reads all seven): `episode: <chapter-slug>` (the schema-field name stays `episode:` for compatibility; value is the chapter slug like `b01c01`), `narrator: <chapters[].pov_narrator>`, `goal: <chapters[].goal>`, `cast: <comma-list>` (computed via slug-grep over the chapter's bone SUBJECTs + `speaks to` listeners), `locations: <comma-list>` (computed via slug-grep over OBJECTs resolved against warehouse loc cards), `prior_episode: <prior-chapter-slug | none>` (the previous chapter in chapter order; `none` for the first chapter of the first book), `aggregate_range: 1-<N>` (kept for schema compatibility; trivially 1-N since `/and-write` authors the chapter directly).
   - **Body format unchanged.** Plain SVO lines, one bone per line, blank-numbered-ID lines as time-skip markers, no scene markers in the body, no YAML metadata, no facet pre-tags. Per-bone state-delta lives only in memory.

   **(b) Scene-map facet** at `active-project/theater/facets/scene-map-<book>-<chapter>.md`, conforming to `schemas/scene-map.schema.md`. Emitted directly from the in-memory `scenes[]` structure (one scene-map entry per `scenes[]` element; bone-range computed from the flat_ids of bones inside each scene). This **replaces** `/and-facets` Phase 4d's prior tensometer-based derivation; `/and-facets` Phase 4d downgrades to coverage-validation only (still fires the URI-SCENE-WINDOW coverage check, but no longer derives).

   **Downstream-gate pre-verify** (HARD, blocks write): (a) **URI-DIALOGUE-COVERAGE-GATE** — every `speaks to` bone has an addressee and a speaker resolvable from the cast roster. (b) **URI-SCENE-WINDOW** — every bone lands inside exactly one scene's flat_id range; no dangling anchors; no scene-spanning bones. Both pre-verifications run before write; SIGNAL versions are tolerated and recorded. On pass, both artifacts ship; `/and-facets` Phase 0 finds the bones file ready and the scene-map facet pre-emitted.

Estimated size: ~350-400 lines total — ~150 net-new (scene-decomposition + substance-contract verification + scene-map co-emit) + ~200-250 lifted from `/and-protolines-v2` (five-pass SVO body) and `/and-season` (bone-gate + Phase 7 emission logic). The size is roughly the same as the prior `/and-write` estimate; the framing change is that most of the body is lift, not original authoring.

### `/and-review` (router + thin wrappers over existing review primitives)

**Lift basis:** Only the router and the Phase 0-4 shared shape are net-new (~80 lines). Every subcommand body is a thin wrapper that invokes a review primitive that already exists in the codebase. See the Asset reuse map's `/and-review` table above for the per-subcommand lift source. Key targets: `/and-season.md` Phase 6 (verdict subcommand), Phase 1 step 1e (chunk subcommand), Pass S10 (bone subcommand), Pass S1/S3.5 (contract subcommand), Phase 1 step 1g (consistency subcommand); `/and-facets.md` R1 fanout (facets subcommand); `design/shoot-v2/audience-review-originals-v2.md` (feedback subcommand); `/and-wrap.md` Phases 1-2 (prose subcommand — STUBBED-DEFERRED).

Top-level router dispatches to one of N pre-defined review types. No authored writes; reports persist to `staff/reviews/<type>-<target>-<timestamp>.md`.

**Router subcommands:**

| subcommand | target | fires | what it reviews |
|---|---|---|---|
| `/and-review chunk <slug>` | any chunk slug (series / b01 / b01c01 / b01c01s01) | audience + dramatist + auditor | Does the chunk match its substance contract? Is it the right depth for its level? Does it feel meaningful? Cost language honest? For scene-level: is `scene_conflict` populated and concrete? |
| `/and-review bone <slug>` | bone slug (b01c01s01n01) | auditor + audience-fork | Does the SVO actually cause the declared Δ (bonefide check)? Is the cost real (cost-ledger anchored)? Substance-flat? |
| `/and-review contract <slug>` | any chunk slug | dramatist + auditor | Is the substance contract well-formed? Do per-axis Δ-magnitudes sum correctly to parent? Cost-ledger consistent? No rank claims without backing? |
| `/and-review signature` | series only | audience + dramatist + auditor | Series signature health: are the axes the right axes? Anchors honest? Cost ledger paid across the arc? Antagonist pressure named per axis? |
| `/and-review bones <chapter-slug>` | chapter slug | bones critics (SVO craft) + bone-gate logic | Per-bone axis-movement bonefide? Per-scene Δ delivered? Cost-paid? `SUBSTANCE-FELT`/`-FLAT` per scene. |
| `/and-review facets <chapter-slug>` | chapter slug | per-facet rubric runners | Facet-by-facet review against rubric. |
| `/and-review prose <chapter-slug>` | chapter slug | audience + auditor | **DEFERRED.** Felt-substance per scene + `SUBSTANCE-COVERAGE` audit on rendered prose. Not in scope until upstream chain produces drafts the user wants to spot-check. Listed here so the eventual subcommand has a home, but skipped during initial build. |
| `/and-review cast` | — | dramatist + auditor | Roster substance-fit: does the roster have carriers for every signature axis perspective? Viability check. |
| `/and-review consistency [<root-slug>]` | optional root (defaults to series) | dramatist + auditor | Cross-level: do per-book Δ aggregates sum to series Δ? Do chapter dramatic shapes honor book drama? Do scene contracts fit within chapter contract? Cost-ledger entries paid? Cyclical commitments honored? **Cross-chapter handoff sweep** (carved in from intent-gaps item #6): for every adjacent chapter pair under root, verify `handoff_out` ↔ `handoff_in` consistency (open-threads / world-state / character-state lists align); flag orphans, drops, or character-axis discontinuities. |
| `/and-review tree [<root-slug>]` | optional root | all of the above, scoped to the subtree | Full sweep at and below root. Defaults to whole series. |
| `/and-review feedback <feedback-file> [<root-slug>]` | feedback file + optional root | audience + auditor | Re-fires reviewers carrying named feedback as context. Use case: "review s01 against `active-project/feedback.md`." |
| `/and-review verdict <book-slug>` | book slug | orchestrator-critic | Fires the orchestrator-critic (`staff/orchestrator-critic/card.md`) against book-scope output. Phase 0 HARD-aborts if: (a) the book has no `chunk`, no `drama`, or no `chapters[]` populated; (b) any chapter under the book is missing `chunk`, `dramatic_shape`, `scenes[]`, or any scene is unsubstanced (missing `substance_delta` or `scene_conflict`); (c) any chapter under the book has no `bones_file` recorded or that file does not exist on disk, or any scene under any chapter has empty `bones[]`; (d) the orchestrator-critic card version recorded in `project.staff.orchestrator_critic` is missing from the library. On pass, dispatches the critic against chunks at every level + bones for every chapter + rendered prose if present. Verdict PASS / PASS-WITH-NOTES / FAIL persisted to `books[<slug>].orchestrator_critic_verdict.ruling`; report path + timestamp written alongside. Absorbs the former `/and-judge-book`. |

**Common phases (every subcommand):**

1. Phase 0 — Parse subcommand. Validate target exists in memory / on disk.
2. Phase 1 — Compose review brief specific to subcommand (which reviewers, what rubric, what scope).
3. Phase 2 — Dispatch reviewers in parallel (audience persona forks per persona; dramatist; auditor).
4. Phase 3 — Aggregate findings into a structured report. Classify HARD / SIGNAL / TASTE per the existing auditor taxonomy.
5. Phase 4 — Persist report to `staff/reviews/<subcommand>-<target>-<timestamp>.md`. Surface to user. Optionally offer to materialize findings into a fix queue for the appropriate authoring command (e.g., HARD findings on `chunk b01c03` → fix queue for `/and-substance chapter b01c03 revise`).

**Relationship to inline reviews.** Authoring commands (`/and-substance` Phase 5, `/and-write` Phases 5/6, `/and-cast` Phase 5) still have inline review *gates* that catch problems before persistence — `/and-write` Phase 5 is continuity, Phase 6 is the substance bone-gate. `/and-review` is for AFTER persistence — going back to spot-check or sweep on demand. Same reviewer infrastructure (audience cards, dramatist, auditor) is shared. The inline gates can call into the same review subroutines `/and-review` dispatches.

**`/and-cast` Phase 5 vs `/and-review tree --series-scope`.** The series-level audit checkpoint inside `/and-cast` is a synchronous blocking gate (the command body owns it; on FAIL the command halts before persisting cast handoff). `/and-review` is post-hoc — fires after persistence, never blocks an authoring command's own flow. They share auditor infrastructure but are not interchangeable: keep the inline auditor fork inside `/and-cast` Phase 5; use `/and-review tree` for later spot-checks against the same scope.

Estimated size: ~280 lines total — ~80 net-new (router + shared phases) + ~200 thin-wrapper wiring around existing review primitives. The actual review logic (audience-card forks, dramatist, auditor, orchestrator-critic, per-facet rubric runners) is not re-implemented; it's invoked via existing dispatch shapes lifted from `/and-season` and `/and-facets`.

### `/and-facets` (light mutation — five narrow edits beyond tensometer-drop)

Bones and the ten facets (location-state, narrator-interest, sensory, state-updates env, state-updates actor, memory, feeling, metaphor, vibes-updates, exposition) + per-character dialogue files are preserved. R1 fanout → R1 fanin → R2 fanout → R2 fanin → audit → audience-gate pipeline shape is preserved.

**Five mutations on top of tensometer-drop:**

1. **R1 author input list no longer includes `tensometer.md`.** Every R1 facet rubric that today reads upstream tensometer (correlative gate, peak-anchors, inverted-tens density, AP7 default-refuse, curve-discipline, etc.) is updated to read the **scene-map facet** (now upstream-emitted by `/and-write` Phase 7 — see below) where it needs scene-boundary information, and to drop the tens-correlation reads entirely. Rubrics that used tens as a substantive signal (memory inverted-tens density, metaphor AP7-at-tens-3, vibes peak-anchors) lose that signal; the substance contract upstream is the replacement (per-bone delta + per-scene aggregate is consulted from showrunner memory by the rubric author when scene-importance pressure matters). Rubric files updated alongside the facets command body.

2. **Phase 4d scene-map: derivation → validation.** `/and-write` Phase 7 already emits the scene-map facet directly from `chapters[].scenes[]`. `/and-facets` Phase 4d no longer derives — it validates: confirm the upstream-emitted `theater/facets/scene-map-<book>-<chapter>.md` exists; run the URI-SCENE-WINDOW coverage check (every bone in `theater/bones/<book>-<chapter>.md` lands in exactly one scene's flat_id range; no gaps; no overlaps; no dangling anchors); HARD-fault on coverage break. The tensometer-fallback path inside the Phase 4d derivation (which used candidate-boundary + sparsity-gradient walking) is removed as dead code.

3. **Phase 0 input-path rename: `theater/proto-lines/<slug>.md` → `theater/bones/<book>-<chapter>.md`.** Update `.claude/commands/and-facets.md:73-84` Phase 0 step 1 to read the new bones path. Update all `_inflight/` working-path references under that subtree (`theater/proto-lines/_inflight/...` → `theater/bones/_inflight/...`). Slug arg shape changes from `<season>e<NN>` to `<book>-<chapter>` (e.g. `b01-c01`); argument-parse and resume-state lookup updated accordingly.

4. **Phase 0 step 4 tens-precondition abort removed.** Current `.claude/commands/and-facets.md:80` aborts if `tensometer-<season-slug>e<NN>.md` is missing. Under the new chain tens is gone, so the precondition + abort branch are dead code — delete the whole step. Phase 0 numbering compresses by one.

5. **Facets output-path convention (flat).** Per-facet outputs land at `theater/facets/<facet>-<book>-<chapter>.md` (e.g. `theater/facets/memory-b01-c01.md`, `theater/facets/scene-map-b01-c01.md`). Per-character outputs land at `theater/facets/<facet>-<book>-<chapter>-<character>.md`. Cite-index lands at `theater/facets/_cite-index-<book>-<chapter>.md`. **Convention chosen:** flat naming under one `theater/facets/` directory — matches the bones-file convention (`theater/bones/<book>-<chapter>.md`) and keeps the directory tree shallow. Per-chapter subdirectories were considered and rejected (extra mkdir step + breaks glob patterns reviewers use today). Update `.claude/commands/and-facets.md` output-path templates throughout, and `schemas/facet.schema.md` + `schemas/scene-map.schema.md` path-convention sections.

Everything else in `/and-facets` is unchanged: Phase 0 still reads the 7-field bones-file header (which `/and-write` now emits); the body-integrity check, citation union, slice consolidation, stale-citation check still operate on flat integer IDs in the bones file (which `/and-write` now assigns at serialization); URI-DIALOGUE-COVERAGE-GATE still fires per `speaks to` bones (which `/and-write` Phase 3 still emits in the licensed form); R2 fanout + audit + audience-gate operate as today.

The `tens:` citation prefix is removed from the recognized list in `schemas/bones.schema.md § citation prefixes`. No other facet citation prefix is changed.

Estimated edit size: ~120–200 lines across `.claude/commands/and-facets.md` (drop tensometer fanout + Phase 0 step 4 abort removal + R1 rubric input updates + path renames throughout + slug-arg shape change), `design/shoot-v2/rubric-*.md` files (drop tens references; substitute scene-map + memory-consulted substance contract where pressure-signal is needed), and `schemas/{bones,facet,scene-map}.schema.md` (drop `tens:` citation prefix from bones; update path-convention sections in facet + scene-map).

### `/and-stitch` (light mutation — four narrow edits)

Eight-phase pipeline (lens-anchored render → redundancy cull → compression → voice transform → local flow → buildup preservation → editorial reflection → finalize). Output `draft/<chapter>.md` (clean) + `draft/<chapter>.annotated.md` (traced). The clean draft is the deliverable until upstream substance machinery is proven and the user wants to revisit polish.

**Four mutations on top of tensometer-drop:**

1. **Phase 0 scene-boundary detection: drop the tensometer-derivation fallback path.** Under the new chain, `/and-write` Phase 7 always emits the scene-map facet; `/and-facets` Phase 4d validates it. The fallback path (which previously parsed `tensometer-<slug>.md`'s scene-footer when the scene-map facet was missing) becomes dead code. Remove it. Pre-URI-SCENE-WINDOW episodes are out of scope (new chain only; existing flea-bottom-dance project keeps its layout).

2. **Phase 0 input-path renames.** `.claude/commands/and-stitch.md:81` Phase 0 step 1 reads `theater/proto-lines/<slug>.md` — update to `theater/bones/<book>-<chapter>.md`. Update all sibling reads of facets + dialogue + scene-map to the new flat naming convention (`theater/facets/<facet>-<book>-<chapter>.md`, `theater/dialogue/<book>-<chapter>.md`, `theater/facets/scene-map-<book>-<chapter>.md`). Slug arg shape changes from `<season>e<NN>` to `<book>-<chapter>`.

3. **Stitcher rendering patch — speaker-paragraph breaks** *(carved in from intent-gaps item #4, s01e02 feedback "everything smashed together").* Per the existing Phase 5 (local flow) / Phase 8 (finalize) forks: add a hard rendering rule — **any new speaker starts a new paragraph**. Each `speaks to` bone's rendered dialogue paragraph begins on its own line; back-to-back dialogue between two speakers always paragraph-breaks between speakers; mixed action-and-dialogue paragraphs are allowed only when the action is the same character's. Update Phase 5 local-flow fork prompts (which today govern paragraphing) and Phase 8 finalize-pass checks (which today catch literal markdown formatting issues). This is a rendering bug, not polish — addressing it does not violate the polish-deferred boundary because no `/and-wrap` editor pass or audit is invoked.

4. **Stitcher rendering patch — scene-callout suppression** *(carved in from intent-gaps item #4, s01e03 feedback "calling out scenes breaks immersion").* No `## Scene N` markdown headers, no `[SCENE BREAK]` literals, no `--- SCENE ---` separators in `draft/<chapter>.md`. Scene boundaries are conveyed by paragraph break only (an empty line between paragraphs, no extra inline marker). The `draft/<chapter>.annotated.md` MAY retain machine-readable scene markers (it's the traced/debug view, not reader-facing); the clean draft must not. Update Phase 8 finalize-pass checks to HARD-strip any surviving scene-callout literal from the clean draft.

R1 lens-anchored render forks, redundancy cull, compression, voice transform, buildup preservation, Phase 7 editorial reflection — all unchanged in shape (Phase 5 and Phase 8 take the rendering-patch edits above). No `revise --feedback` mode, no Phase 7 substance-allowed-moves enhancement; both deferred per the polish-deferred boundary.

Estimated edit size: ~80–130 lines (Phase 0 fallback removal + path-rename + slug-arg shape + Phase 5 speaker-paragraph rule + Phase 8 scene-callout strip + tens-reference cleanup in the stitcher fork prompts). The two carve-in edits (speaker-paragraph + scene-callout suppression) account for ~40–60 lines of the increase from the prior estimate.

---

## Decisions on spec gaps (resolved 2026-05-16 post-audit)

These were flagged as IMPORTANT spec gaps in the self-audit. Resolved in-plan rather than escalated to user, per "act independently" directive. Each decision should be re-confirmed at plan approval.

### Vibe-clouds under recursive substance

**Decision: keep series + book vibe-clouds; deprecate chapter/scene/bone vibes.** Substance contracts now carry the explicit-substance role vibes were biasing toward implicitly; preserving vibes at every recursive level would double up with no obvious lift and would blow up the dispatch budget. Series and book vibes remain because they carry tone/mood/genre-feel that substance contracts don't capture directly (e.g. "noir," "wry," "fairytale" — biasing word-choice, not measurable Δ).

- `/and-series` continues to author a series-level vibe-cloud as part of the series chunk.
- `/and-substance series` continues to author per-book vibe-cloud entries when authoring book chunks.
- `/and-substance chapter` and `/and-write` do NOT author vibe-clouds; chapter/scene/bone-level shaping comes from the substance contract.
- CLAUDE.md "Memory rules" line about vibe-clouds is updated to: "Vibe-clouds are built at series and book level. Both are active during authoring; book-level takes priority on key conflicts."

### URI gates compatibility from `/and-write`

**Decision: `/and-write` Phase 7 pre-verifies URI-DIALOGUE-COVERAGE-GATE and URI-SCENE-WINDOW before emission.** See `/and-write` spec Phase 7 above. Pre-verification HARD-aborts `/and-write` rather than letting `/and-facets` Phase 0 abort later; the abort surface stays close to the bone-writing pass that introduced the violation.

### Verdict block staleness invalidation

**Decision: any `/and-substance` or `/and-write` re-run scoped at-or-under a book stale-marks that book's `orchestrator_critic_verdict` block.** See "Staleness cascade" section above. The verdict's `stale_since` field forces re-judgment via `/and-review verdict <book>` before the verdict is trusted again.

### `/and-cast` Phase 5 stays inline

**Decision: keep the inline auditor fork; `/and-review tree --series-scope` is the post-hoc spot-check, not a replacement.** See `/and-review` "Relationship to inline reviews" subsection above.

### `/and-cast revise` provisioning

**Decision: new actors get fresh margit Phase 4 provisioning; untouched actors are left as-is.** See `/and-cast` Phase 0 and re-runnability table.

### Staleness "surfacing" behavior

**Decision: surfacing prints affected downstream artifacts with timestamps + prompts user for `mark-stale` / `keep-fresh` / `abort`; default `mark-stale`; choice logged to `staff/showrunner/staleness-log.md`; downstream commands warn (do not block) on stale parents.** See "Surfacing — defined" subsection above.

---

## Notes on deferred concerns

Items flagged as DEFER in the self-audit. Not blockers; recorded so the implementer knows the team is aware.

- **Dispatch budget.** Naive worst case under the revised plan (6 books × 6 chapters × 3 scenes × per-level reviews ×3 retries, plus per-chapter `/and-write` with internal bone-gate dispatches) is in the low hundreds of subagent dispatches per series — meaningfully lower than the prior plan's beat-level recursion (which multiplied dispatches by an additional 5× per scene). Mitigations available: per-level review parallelism (audience personas + dramatist + auditor fire concurrently — already the pattern), lower retry caps for `/and-write` revisions (capped at 2 instead of 3 since revise is targeted), `--cascade` flag with checkpoint flush every chapter (so `/and-cut` can resume). Treat as observation, not a redesign blocker; revisit after first end-to-end run produces real numbers.
- **`/and-cut` interaction.** `/and-substance --cascade` should checkpoint after every chapter completes (i.e. after `/and-substance chapter` finishes a chapter's scenes, or after `/and-write` finishes a chapter's bones — whichever the cascade is currently at). `/and-cut` mid-cascade saves the resume point (`next: /and-write b01c04` or `next: /and-substance chapter b01c05`). Detail to land in the `/and-substance` command body, not in this plan.
- **Filesystem migration.** Active project `flea-bottom-dance` is out-of-scope; its existing `theater/proto-lines/...` layout is left alone. New projects use `theater/bones/<book>-<chapter>.md`. No migration script needed.
- **Estimated sizes are loose.** `/and-substance` 350–450 lines (three invocation levels) and `/and-write` 400–500 lines (decomposition + SVO pipeline + bone-gate) are working estimates. Total command-body line count under the revised plan is similar to the prior plan — work just shifted from `/and-substance` to `/and-write`. Not a blocker — size will be what it is.

---

## Order of operations

1. **Plan approval.**
2. **Design docs.** `design/substance/README.md` (incl. full recursive design at three invocation levels / four chunk levels + the bone-is-the-beat principle) + `questionnaire.md` + `delta-targets.md`.
3. **Schema updates.**
   - `schemas/showrunner-memory.schema.md` — `project:` block, restructured `series:` with substance subblock, `books[]` nesting (chapters, scenes, scene_conflict block, scenes[].bones[] with per-bone state-delta, chunk-count fields at each authoring level, `bones_file` pointer, `stale_since` at each level, structured `orchestrator_critic_verdict` block).
   - `git mv schemas/proto-line.schema.md schemas/bones.schema.md` — rename to match `/and-write` output naming. Update internal references in the schema body (s/proto-line/bone/g where it refers to the unit itself; keep historical references in archived schemas alone). **Body format preserved as-is** (flat integer IDs, monotonic, file-scoped; 7-field extended header with field names unchanged; no body markers; post-extraction citation accrual) — downstream `/and-facets` Phase 0 / body-integrity check / citation union operate against the same shape. **Removed:** the `tens:` citation prefix from the recognized prefix list (tensometer is gone). Update CLAUDE.md's schema authority table accordingly.
4. **Archive current commands + tensometer rubric.**
   - `git mv .claude/commands/and-project.md      archive/commands/and-project-pre-substance.md`
   - `git mv .claude/commands/and-season.md       archive/commands/and-season-dissolved.md`
   - `git mv .claude/commands/and-wrap.md         archive/commands/and-wrap-dissolved.md`
   - `git mv .claude/commands/and-protolines.md   archive/commands/and-protolines-pre-substance.md`
   - `git mv .claude/commands/and-protolines-v2.md archive/commands/and-protolines-v2-pre-substance.md` (if present)
   - Move `/and-wrap` to `-polish-deferred` (not `-dissolved`); its Phase 2 (8-class auditor pass) and Phase 3 (editor allowed-moves contract + procedure) are the un-defer lift targets for `/and-review prose` and a future polish revival.
   - Rename `/and-protolines-v2` to `-lifted-to-and-write` (it IS the lift source for `/and-write` Passes 1-5); rename `/and-protolines-season-v2` to `-lifted-to-and-substance-cascade` (lift source for the `--cascade` flag).
   - `git mv design/shoot-v2/rubric-tensometer.md archive/rubrics/rubric-tensometer-replaced-by-substance.md`
   - Update `archive/commands/README.md` and (new) `archive/rubrics/README.md`.
   - Update `/and-facets` command body to drop tensometer from R1/R2 fanout + facet list. Update CLAUDE.md's URI-026 shared-resources line to remove tens-rubric reference.
5. **Author shared protocol design docs (factored from per-command repetition).**
   - `design/substance/rerun-protocol.md` — Phase 0 re-run protocol (read upstream → check own output → cascade warning → run). Referenced by `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review`. Pure factor-out from "Re-runnability" section of this plan; no original content.
   - `design/substance/staleness-cascade.md` — mark-stale / keep-fresh / abort surfacing; staleness-log location; warn-not-block-on-stale-parents rule; verdict-block invalidation. Pure factor-out from "Surfacing — defined" + "Staleness cascade" + "Staleness also invalidates" subsections.
   - Both docs are factored-out specs, not original work — saves ~150 lines of repeated specification across the five new command bodies.
6. **Write new + overhauled commands** in pipeline order. **Implementer protocol:** for each command below, open the listed lift source(s) FIRST, copy the relevant phase content into the new command body, then apply the listed adaptations and add only the net-new phases from scratch. The Asset reuse map above is the canonical lift index. Do NOT write any "new" command from a blank file.
   - `.claude/commands/and-project.md` (shrink current `/and-project` by extracting Series Plan to `/and-series` and Phase 2 1c + Phase 3 to `/and-cast`; add staff persona binding block)
   - `.claude/commands/and-series.md` (lift Series Plan section from `archive/commands/and-project-pre-substance.md`; net-new: structural prompts only)
   - `.claude/commands/and-substance.md` (lift `archive/commands/and-season-dissolved.md` Phase 1 + Phase 3 sweep-A pattern; net-new: substance-contract authoring + signature authoring at series level + recursion glue + cascade flag)
   - `.claude/commands/and-cast.md` (lift `archive/commands/and-project-pre-substance.md` Phase 2 1c + Phase 3; net-new: revise/redo decommission-routing only)
   - `.claude/commands/and-write.md` (lift `archive/commands/and-protolines-v2-lifted-to-and-write.md` Passes 1-5 verbatim + `archive/commands/and-season-dissolved.md` Pass S10 bone-gate + Phase 7 emission; net-new: Phase 1 scene-decomposition + substance-contract verification inside Phase 6 + scene-map co-emit inside Phase 7)
   - `.claude/commands/and-review.md` (lift `archive/commands/and-season-dissolved.md` Phase 6 for `verdict`, Phase 1 1e for `chunk`, Pass S10 for `bone`, Pass S1+S3.5 for `contract`, Phase 1 1g for `consistency`; lift `/and-facets.md` R1 fanout for `facets`; net-new: router + Phase 0-4 shared shape only; `prose` subcommand stubbed-deferred with un-defer lift target pre-pinned to `archive/commands/and-wrap-polish-deferred.md` Phases 1-2)

   **Lightly mutated** (narrow edits, not net-new): `/and-facets` (remove tensometer from R1/R2 fanout + downgrade Phase 4d scene-map from derivation to validation + update R1 rubric input lists to drop tens reads + substitute substance-contract reads where pressure-signal is needed) and `/and-stitch` (drop Phase 0 tensometer-derivation fallback path). Rubric files under `design/shoot-v2/rubric-*.md` updated alongside the facets command body.
7. **Update CLAUDE.md.** Full enumerated change set:
   - **Primary pattern section.** Replace the `project activation → season start → (episode start → shoot)* → bulk and-wrap → repeat` block with the new chain: `/and-project → /and-series → /and-substance series → /and-cast → [series audit checkpoint] → /and-substance book/chapter → /and-write (decomposes scenes into bones) → /and-facets → /and-stitch → draft/<chapter>.md (terminal deliverable; polish deferred)`. Remove "Season start," "Episode start," "Shoot," "And-wrap" prose subsections — the names no longer exist. Add a short paragraph noting that polish/`/and-wrap` is dropped and `/and-stitch`'s output is the deliverable until upstream is proven.
   - **Agent routing table.** No agent additions/removals expected (the new commands reuse existing agents: showrunner, screen-writer, audience, dramatist, auditor, fixer, margit, orchestrator-critic). Confirm `editor` row stays or is marked DEFERRED (since `/and-wrap` is dropped and `/and-stitch` Phase 7 is the standing in for editorial work for now); remove the `editor` row entirely or annotate it as `library-only; not currently dispatched` — pick the latter to preserve the card for the eventual polish revival.
   - **Directory map.** Update `theater/` line: replace `proto-lines.md` reference with `bones/<book>-<chapter>.md`. Keep `draft/` and `polish/` lines but annotate `polish/` as "not written by the current chain — polish deferred." Add `staff/reviews/` line for `/and-review` reports.
   - **Schema authority table.** Update `Proto-line file (shoot-v2)` row to `Bones file → schemas/bones.schema.md` (the renamed schema). Add row for the substance design docs: `Substance framework → design/substance/{README,questionnaire,delta-targets}.md`. Confirm or remove `Per-character dialogue file` and `Facet file` rows — unchanged.
   - **Memory rules section.** Replace the vibe-clouds line. Old: "Vibe-clouds are built at each planning level. Series, season, and episode each have a vibe-cloud. All three are active during shoot; episode-level takes priority on key conflicts." New: "Vibe-clouds are built at series and book level. Both are active during authoring; book-level takes priority on key conflicts. Chapter/scene/bone-level shaping comes from the substance contract, not a vibe-cloud."
   - **Rules section.** Update Rule 10 (URI-026 bone-gate): remove tens-gate language; replace with "`/and-write` Phase 6 substance bone-gate is the bones-first authoring gate. Deformed substance contracts cannot be rescued by downstream facet skin." Update Rule 11 (URI-026 shared reviewer resources): remove `design/shoot-v2/rubric-tensometer.md` reference; keep the audience persona `Threshold Discipline` and AP-SCAN promotion path lines.
   - **Commands table.** Remove rows for `/and-season`, `/and-wrap`, `/and-protolines`, `/and-protolines-v2`, `/and-protolines-season-v2`. Add rows for `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review`. Update `/and-facets` row to drop tensometer mention. Update `/and-stitch` row to mark its `draft/<chapter>.md` as the terminal deliverable.
   - **"Not in scope" section.** No change (gacha / workshop-artifact still excluded). Optionally add "Polish / `/and-wrap` revival — deferred until substance machinery is proven."
8. **Commit + push** to the active substance-overhaul branch at logical breakpoints.

---

## Out of scope

- **Retrofitting flea-bottom-dance.** Current active project keeps its state. New chain applies to the next `/and-project` run.
- **Facet rubric changes — partial.** Bones and facets (feeling, memory-flags, scene-map, dialogue, exposition, etc.) are preserved. **Tensometer is removed** — its purpose (per-bone substance-density signal) is now served directly by the per-bone state-delta + bone-gate. `/and-facets` no longer emits a tensometer file; `design/shoot-v2/rubric-tensometer.md` is archived; CLAUDE.md's "shared reviewer resources" line (URI-026) is updated to drop the tens rubric. The Tens-gate in URI-026 is replaced by the substance bone-gate at `/and-write` Phase 6 (per-bone axis-movement verification + per-scene aggregate Δ delivery + cost-paid check against the upstream scene contracts authored by `/and-substance chapter`). `/and-substance` is the chunker only (stops at scene chunks); scene-decomposition + bone-writing + bone-gate logic all live in `/and-write`.
- **Impersonator card "values block."** Deferred — follow-on card-schema task after one full new-chain run.
- **Shoot-v2 chain overhaul.** `/and-facets` and `/and-stitch` are **lightly mutated** (not unchanged): `/and-facets` drops tensometer from R1/R2 fanout AND downgrades Phase 4d scene-map from derivation to validation (the scene-map facet is now upstream-emitted by `/and-write` Phase 7); `/and-stitch` drops its Phase 0 tensometer-derivation fallback as dead code. Both edits are narrow (light command-body edits + rubric updates; full specs in the `/and-facets` and `/and-stitch` command-spec sections above). The shoot-v2 pipeline shape — bones → ten facets + dialogue → cite-index → stitcher draft — is preserved. Bones file format is preserved (flat integer IDs, 7-field header, no body markers, post-extraction citation accrual) so `/and-facets` Phase 0 + body-integrity checks + citation accrual all operate as today.
- **Final-edits / polish / ship-ready manuscript work.** Deferred entirely until the upstream chain (project → series → substance → cast → substance recursive → write → facets → stitch → draft) is proven to produce substantively-right drafts end-to-end. The whole "is the prose ready to ship?" question waits. `/and-wrap` is archived as `-polish-deferred` (not `-dissolved`) — its Phase 1 (audience review) + Phase 2 (8-class auditor pass) + Phase 3 (editor allowed-moves contract + procedure) are the future un-defer lift target for `/and-review prose <chapter>` and any polish revival. `/and-stitch` is structurally preserved (one narrow Phase 0 mutation only); `/and-review`'s `prose` subcommand is stubbed-deferred with its un-defer lift target pre-pinned. Whole-text concerns (cross-chapter percussion, repetition cull across the book, polish/ directory) come back after the substance machinery is trusted.
- **Persona library expansion for non-audience staff.** `/and-project` records library-default version; substantive variant composition is a follow-on.
- **Absolute-length floor mechanism** *(intent-gaps item #5, OOS-tracked per Hole E split).* User feedback ("Way too short. What even was the point?") points at chapters that hit substance contracts in too-few absolute words. The plan tracks density (a ratio) but not absolute length. Follow-on issue tracks the design choice between (a) explicit `chapter_word_count_floor` / `scene_word_count_floor` fields under `series.structure.book_length`, verified at `/and-stitch` Phase 8 finalize, vs. (b) derived floor from bones-count × words-per-bone estimate at `/and-write` Phase 6. Acknowledged shipped-defect against user feedback until follow-on lands.
- **Emotional-substance orthogonality to plot-substance** *(intent-gaps item #7, OOS-tracked).* A chapter could satisfy its contract entirely on wealth/community axes while a plot event of "protagonist returns from the dead" produces zero emotional Δ — exactly the s01e01 failure mode the user flagged. Follow-on issue tracks the design choice between (a) per-chapter Δ must span ≥2 axis classes (axes pre-tagged with `state_axes[].class` — plot vs. emotional), vs. (b) audience-fork emotional-resonance check at `/and-write` Phase 6 bone-gate that fires `SUBSTANCE-EMOTIONALLY-FLAT` HARD when stakes-events (death/return/betrayal/revelation) are present in the chunk but no emotional-class axis moved. Acknowledged shipped-defect against user feedback until follow-on lands.
- **Plot-arc-completion dramatist check** *(intent-gaps item #8, OOS-tracked).* `/and-substance chapter` Phase 4 tags `dramatic_shape` (rising/climax/falling/hinge) and Phase 5 dramatist verifies shape. But shape is a curve, not arc-completion — a chapter tagged "rising" can still leave the reader asking "what was the point?" (s01e02/e03 feedback). Follow-on issue extends the Phase 5 dramatist rubric to verify identifiable setup beat + complication beat + resolution-or-cliffhanger beat, with chapter chunk text required to answer "what changed by the end?" in one line. The `chapters[].goal` field carved into the current plan is a step in this direction but does NOT itself enforce arc-completion; the follow-on is the enforcing check.
- **World-detail consistency** *(intent-gaps item #11, OOS-tracked).* "The bowl is weird / do smallfolk have salt?" feedback points at class/economic-level setting detail — finer than world-law, coarser than prop-card. `/and-review consistency` currently has no dedicated axis for this. Follow-on issue tracks the design choice between (a) adding `--world-detail` axis to `/and-review consistency` (dispatches against location + condition + persona cards to check class/economic plausibility), vs. (b) inline world-detail audit step inside `/and-write` Phase 5 continuity (per-bone setting-anachronism check).
- **`cards/dialects/` → `cards/behaviors/` directory rename** *(Hole H, deferred).* CLAUDE.md flags this rename as pending. NOT lockstep with the substance overhaul — the lifted `/and-write` Phase 0 step continues to read `cards/dialects/INDEX.md` until a separate follow-on renames the directory. Once renamed, the Phase 0 step picks up the new path with a one-line edit; no other command touches the path.

---

## Open questions for user

1. **Archive suffix.** Four conventions: `-pre-substance` for overhauls/renames (`/and-project`, `/and-protolines`); `-dissolved` for commands whose jobs migrated piecewise into other commands and aren't coming back as standalones (`/and-season`); `-polish-deferred` for commands intentionally preserved for future revival (`/and-wrap` — its Phase 2 + Phase 3 are the un-defer lift target for `/and-review prose`); `-lifted-to-<command>` for command bodies that ARE the primary lift source for a successor (`/and-protolines-v2` → `-lifted-to-and-write`; `/and-protolines-season-v2` → `-lifted-to-and-substance-cascade`). OK?
2. **Universal axis set.** `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). Add / remove?
3. **Chunk-Δ defaults.** Default ratio (series Δ ≥ 6 ranks, book Δ = 2–3, chapter Δ ≈ 1, scene Δ = 0–1). Close enough for first run, or calibrate now?
4. **`/and-substance --cascade` default.** Recommend default OFF (manual level-by-level invocation preserves per-level review checkpoints and dispatch budget). `--cascade` as opt-in for late-stage runs. Confirm?
5. **Orchestrator-critic firing point.** Settled: `/and-review verdict <book-slug>` (subcommand of `/and-review`, absorbing the former `/and-judge-book`). Fires on demand once both `/and-substance book` (all chunks under the book) and `/and-write` (all chapter bones files under the book) are complete. Phase 0 of the subcommand hard-aborts if any chunk under the book is unsubstanced or any chapter is missing its bones file. Cleaner than auto-firing inside `/and-substance book` (which doesn't produce bones) and consolidates the review surface under one router. Confirm?
6. **Series-end shape values.** Five: definitive / open-ended / ambiguous / tragic / triumphant. Add / remove?
7. **Cyclical book semantics.** Cyclical applies to protagonist-perspective axes only (world axes can drift across cyclical books — HP pattern; Hogwarts evolves while Harry resets). Confirm?
8. **Re-run modes naming.** `revise` / `add` / `redo`. Acceptable, or different verbs (`amend` / `extend` / `restart`)?
9. **Vocabulary refactor scope.** "Season"/"episode" language still appears in legacy schemas, the shoot-v2 chain (`/and-protolines`, `/and-facets`, etc.), CLAUDE.md, and design docs. Recommended scope: **reading-context** — rename in command bodies, schemas, design docs, CLAUDE.md, and memory file templates the model reads while authoring. Keep filesystem slugs (`s01e01.md` style) and existing in-flight project state alone. Confirm scope, or wider (filesystem too) / narrower (just removed-command bodies)?

---

## Verification on completion

- `design/substance/{README,questionnaire,delta-targets}.md` exist; README documents the three-invocation / four-chunk-level design + the bone-is-the-beat principle (per-bone state-delta authored by `/and-write`, not by `/and-substance`).
- `schemas/showrunner-memory.schema.md` updated with: `project:` block; restructured `series:` (incl. `structure.book_length.{chapters_per_book, scenes_per_chapter, bones_per_scene}` ranges — note: `beats_per_scene` removed; `bones_per_scene` replaces it); `substance.cost_ledger[].anchor.{book, chapter, scene}` fine-grained anchors; `books[]` nesting down to scenes with `structure.{chapter_count, scene_count}` populated at each authoring level; `chapters[].pov_narrator` + `chapters[].goal` fields; `chapters[].status` enum (planned / scened / bones-written / faceted-r1 / audited-r1-mechanical / audited-r1 / faceted-r2 / stitched); `chapters[].handoff_in` + `chapters[].handoff_out` blocks; `scenes[].scene_conflict.{protagonist_force, opposing_force, stakes_axis}` block; `scenes[].bones[]` with `slug`, `flat_id`, `svo`, `substance_delta.{axis_moves, cost, cost_ledger_anchor}`, `gate_verdict.{bonefide, flat, signals[]}` (PASS-only persistence on bonefide/flat; signals list preserved across runs for SIGNAL-targeted revise; `facet_tags` removed per bones-facets compatibility resolution); `bones_file` pointer; `stale_since` field at each level; `orchestrator_critic_verdict.{ruling, report_path, verdict_at, stale_since}` block.
- `schemas/proto-line.schema.md` renamed to `schemas/bones.schema.md`; internal references updated; body format preserved (flat integer IDs, 7-field extended header, no body markers, post-extraction citation accrual); `tens:` citation prefix removed from the recognized list; in-memory bones-as-scene-children + per-bone state-delta documented in `showrunner-memory.schema.md` (not in bones.schema.md, which governs the file shape only); CLAUDE.md schema authority table reflects the rename.
- `archive/commands/and-project-pre-substance.md`, `and-season-dissolved.md`, `and-wrap-polish-deferred.md`, `and-protolines-pre-substance.md`, `and-protolines-v2-lifted-to-and-write.md`, `and-protolines-season-v2-lifted-to-and-substance-cascade.md` exist.
- `design/substance/rerun-protocol.md` and `design/substance/staleness-cascade.md` exist as factored-out shared-protocol references; each of the five re-runnable new commands references them rather than duplicating the spec inline.
- `archive/rubrics/rubric-tensometer-replaced-by-substance.md` exists; `design/shoot-v2/rubric-tensometer.md` gone.
- `/and-facets` command body no longer emits tensometer; CLAUDE.md URI-026 line no longer references tens rubric.
- `.claude/commands/and-{project,series,substance,cast,write,review}.md` exist and parse.
- `.claude/commands/and-facets.md` is **lightly edited** — tensometer fanout dropped from R1/R2; Phase 4d scene-map derivation downgraded to validation (consumes the upstream-emitted scene-map facet); R1 rubric input lists updated to drop tens reads.
- `.claude/commands/and-stitch.md` is **lightly edited** — Phase 0 tensometer-derivation fallback path removed (dead code under new chain); no Phase 7 enhancement, no revise mode.
- `/and-write` Phase 7 emits both `theater/bones/<book>-<chapter>.md` (flattened scene-ordered bones file with flat integer IDs + 7-field header) AND `theater/facets/scene-map-<book>-<chapter>.md` (scene-map facet derived directly from `scenes[]` in memory). Bones file body remains comment-clean (no scene markers, no YAML, no facet pre-tags); per-bone state-delta lives only in showrunner memory.
- Speech bones in the bones file use the licensed dialogue form `<speaker-slug> speaks to <listener-slug>`. Substance_delta on speech bones lists at least one communication-class axis (community / knowledge / reputation / trust).
- `chapters[]` in showrunner memory carries `pov_narrator` and `goal` fields, populated by `/and-substance chapter` Phases 3 and 4 respectively; `/and-write` Phase 7 reads them to populate the bones-file `narrator:` and `goal:` headers without further lookup.
- `chapters[]` carries a `status` field with valid enum values `planned | scened | bones-written | faceted-r1 | audited-r1-mechanical | audited-r1 | faceted-r2 | stitched`; each authoring/review phase advances the status monotonically; resume-point detection in `/and-facets` and `/and-stitch` Phase 0 reads the field.
- `chapters[]` carries `handoff_in` + `handoff_out` blocks (open_threads / world_state / character_state / source_chapter or target_chapter), populated by `/and-substance chapter` Phase 3; `/and-substance book` Phase 5 dramatist verifies adjacent-chapter consistency; `/and-write` Pass 5 continuity reads prior chapter's `handoff_out`; `/and-review consistency` adds cross-chapter handoff sweep.
- `.claude/commands/and-stitch.md` Phase 5 (local flow) enforces speaker-paragraph rule (any new speaker starts a new paragraph). Phase 8 (finalize) strips any surviving `## Scene N` / `[SCENE BREAK]` / `--- SCENE ---` markers from `draft/<book>-<chapter>.md` (clean). `draft/<book>-<chapter>.annotated.md` may retain machine-readable scene markers; the clean draft must not.
- `.claude/commands/and-facets.md` Phase 0 step 4 (tens-precondition abort) is removed; the Phase reads `theater/bones/<book>-<chapter>.md` (not `theater/proto-lines/<slug>.md`) and resolves the slug arg as `<book>-<chapter>` (not `<season>e<NN>`).
- Facet output paths use flat naming: `theater/facets/<facet>-<book>-<chapter>.md`, `theater/facets/<facet>-<book>-<chapter>-<character>.md`, `theater/facets/_cite-index-<book>-<chapter>.md`, `theater/facets/scene-map-<book>-<chapter>.md`. No per-chapter subdirectories under `theater/facets/`.
- `schemas/bones.schema.md` documents the per-chapter book-scoped path convention (`theater/bones/<book>-<chapter>.md`, e.g. `b01-c01.md`) alongside the prior path conventions.
- `design/substance/README.md` includes the "chapter ≈ episode" mapping paragraph for user mental-model continuity (~3000-5000 words, 1-3 scenes).
- `bones[].gate_verdict` carries a `signals: [<finding-class>]` list alongside the PASS-only `bonefide` / `flat` fields; `/and-write revise` Phase 0 surfaces SIGNAL-flagged bones/scenes for partial-revise targeting. Per-scene gate_verdict clearing on partial revise — unchanged scenes' verdicts are preserved.
- `/and-substance --cascade` writes `staff/showrunner/cascade-checkpoint.md` after each child chunk completes (sketch schema in plan); `/and-cut` mid-cascade writes the same file with `reason: halted-on-cut`; `--resume` re-fires from `next.command`.
- No active `.claude/commands/and-season.md`, `and-wrap.md`, `and-judge-book.md`, or `and-protolines*.md`.
- `/and-substance` command body contains NO bone-writing logic and NO scene-decomposition logic (chunker only — produces chunks + contracts; stops at scene chunks).
- `/and-substance` accepts exactly three invocation levels (`series` / `book` / `chapter`); a `scene` invocation is rejected with a clear error pointing the user at `/and-write`.
- `/and-write` command body contains NO chunk authoring above scene level (reads scene chunks; decomposes into bones; produces bones-with-deltas; writes SVO craft).
- `/and-write` Phase 6 substance bone-gate explicitly classifies `SUBSTANCE-FLAT-<axis>` and `SUBSTANCE-SUSPECT-cheap-gain-<axis>` as HARD findings (blocks emission), not SIGNAL.
- `/and-review` parses live router subcommands (chunk / bone / contract / signature / bones / facets / cast / consistency / tree / feedback / verdict); reports persist to `staff/reviews/`. `prose` subcommand stubbed as DEFERRED.
- `polish/` directory not touched by the new chain — manuscript is `draft/<chapter>.md`. Polish concerns deferred entirely.
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated — `/and-season` and `/and-wrap` rows removed; new rows for `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review`; primary-pattern line reflects new chain (`/and-project → /and-series → /and-substance series → /and-cast → /and-substance book/chapter → /and-write → /and-facets → /and-stitch`); polish deferred. Vibe-clouds line reflects series+book only.
- Each new command's Phase 0 validates upstream and supports re-run modes (except `/and-project`, which hard-aborts).
- Commit + push lands clean on `claude/improve-story-substance-CVi58`.
