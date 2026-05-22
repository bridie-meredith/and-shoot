# Postop companion — b01c02 readability root-cause

date: 2026-05-22
companion to: run-postmortem-c02-2026-05-22.md
scope: WHY the b01c02 draft reads as abstract, disconnected, and jeopardy-free — mechanism diagnosis + process-change recommendations
inputs: command-body rules (.claude/commands/and-write.md, and-stitch.md); the element-leakage trace (28 lost/degraded elements)

---

## The symptom, restated precisely

The first postop recorded the readability finding as an observation. It is worth stating exactly, because each clause has a separate cause:

> A cold reader can't follow what physically happens — disconnected gestures, no connecting story. No tension because no jeopardy. The ledger scene can't satisfy because the reader never saw the act being accounted for.

This is not a prose-quality problem. The sentences are competently built. It is a **content-architecture** problem: the chapter's events, stakes, causal links, and physical world were removed by the pipeline before the prose was ever written. The stitcher rendered faithfully — it rendered an empty room faithfully.

The leakage trace puts a number on it: **~28 authored elements never reach the 675-word draft.** The chapter chunk in showrunner memory is rich and correct. What the reader receives is a competent stylist describing the aftermath of a scene that was never written.

---

## Why the content is this way — the mechanism

The draft reads as it does because of **five compounding pipeline behaviors, each individually defensible, that together convert events into abstraction.** None is a bug. The failure is emergent — which is why every gate passed.

### Mechanism 1 — Decomposition has no event-coverage contract

`/and-write` Phase 1 (`and-write.md:87`) instructs: "Decompose the scene chunk into N bones, N inside `bones_per_scene` range." That is the entire fidelity requirement. The decomposer must produce bones that pass **SVO form** and the **substance gate** — it is *never* required to produce bones that cover the chunk's *events*.

SVO form bans perception verbs and interiority in bones (`and-write.md:120`). So the decomposer atomizes what is cleanly SVO-able. In a first-person chapter whose protagonist is a watcher *by design* (the prohibition makes her observe-not-act), the SVO-legible atoms are dominated by her **perceptual postures**: "lifts the eyes," "faces the alley-mouth," "works the net," "opens the ledger." Those decompose cleanly. The chapter's actual *event* — Taylor routing Wren clear of a sweep — does **not** decompose, because a rescue is not an action. It is a *causal relation between* actions (Wren is endangered → Taylor closes the wrong lanes → Wren takes the open one). The bone format stores actions, not the relations between them. Causality, stakes, and intent live in the gaps between bones, and the gaps have no schema slot.

So the decomposer captured the easy thing (Taylor observing) and dropped the hard thing (the rescue). The leakage trace confirms it precisely: no bone exists for Wren-in-danger, none for the rescue causality, none for Wren-reaching-safety. **And the same failure hit the reflective scene** — s03's bones are "writes the line / strikes the line / underlines the entry," the *postures of accounting*, while the *content* of the accounting (the classification question, the verdict, the cost line — the chunk's stated "chapter's weight") was never atomized into them. The decomposer atomizes visible posture and drops whatever the posture is *about*. That is true whether the posture is a rescue or a moral verdict.

### Mechanism 2 — The substance gate rewards the cheapest axis

Every perception bone delivers a `knowledge` tick — Taylor noticed something, knowledge moves. `knowledge` is the **cheapest axis in the system**: it costs only a noticing. `capability` costs a deployment — hard to decompose, gate-risky. So the path of least resistance to hit `density_target` and the declared axis deltas is to write more perception bones.

The measured result (`memory.md:1040-1042`): `knowledge` delivered **+1.3 against a +0.5 target** (13 ticks — a 160% overrun); `capability`, the chapter's *declared headline axis*, delivered **+0.4 against +1.0** (a 60% shortfall). The gate's ±1 band passed both. The incentive gradient of the substance machinery points straight at a watching protagonist — and the gate's tolerance band is wide enough that it never pushes back.

### Mechanism 3 — The renderer is forbidden to add what the bones lack

The bone-faithfulness fence (`and-stitch.md:419`) bars the stitcher from inventing "body, dialogue, spatial, route, scene-prose, or cognitive detail outside the graph." This is **correct design** — it stops the renderer confabulating. But its consequence is absolute: a bone set missing the rescue, the jeopardy, and the physical world yields a chapter missing them, and the stitcher is *rule-bound to keep it that way*. Hollow in, hollow out, by fence. The render-log's clean run (`0 cut-bones`, `0 faults`) is the fence working as designed on defective input.

### Mechanism 4 — The variance machinery converts repetition into abstraction

Because the bones are repetitive perceptual postures (multiple "lifts the eyes," "faces the alley-mouth," "works/pulls the net"), they trigger the stitcher's anti-percussion **variance rules**. Breaking repetition is the entire reason scene-window mode exists (`and-stitch.md:359`: the per-anchor fork "is structurally unable to break percussion ... stilling-trios rendered as three identical 'went still' verbs").

But when the repeated thing is a *concrete physical action*, the variance lever's only move is a *less concrete* re-rendering. The render-log shows it happening: `@3 "lifts the eyes" → "turned my reading outward" (avoid literal eye-lift repetition)`. The pipeline's repetition-fix is an **abstraction generator** when fed repetitive concrete bones. It trades concreteness for variety because variety is what it is built to measure.

### Mechanism 5 — Every editorial pass subtracts; none add

The stitcher's editorial phases route only to **CUT / CUT-CLAUSE / CUT-ASININE / CUT-HOLLOW / CUT-BONE / RESHOW / REWORD / SIMPLIFY-PUNCT** (`and-stitch.md:62-63`). Phase 2 culls, Phase 3 compresses, Phase 7 — named "the only taste pass" (`and-stitch.md:61`) — has an entirely subtractive-or-lateral verb set. There is no `EXPAND`, no `GROUND`, no `STAGE`, no `NEEDS-BEAT`.

`project.hollow-prose-patterns` exists (`and-stitch.md:281`) — so the pipeline *has* a concept of hollow prose — but it is a phrase-level blocklist applied at render-cut ("fork must not produce these surface forms; cut at render"), not a scene-level substance check. A pipeline whose only editorial motions are cut/cull/compress/trim will **monotonically thin prose** and certify the thinnest survivable version as "clean."

### The capstone — nothing reads the assembled scene as a reader

This is why the five mechanisms were never caught. Every gate in the chain measures a **part**:

| Gate | Unit measured |
|---|---|
| `/and-write` substance bone-gate | per-bone axis ticks |
| `/and-facets` Phase 5 audit | per-facet mechanical compliance |
| `/and-facets` Phase 5b audience-gate | per-facet taste (3-of-3) |
| `/and-stitch` Phase 7 | per-sentence cut-worthiness |
| `/and-review verdict` orchestrator-critic | run-health criteria |

Readability, jeopardy, and "did the scene happen" are **emergent properties of the assembled scene**. No stage holds the assembled scene and asks the reader's questions: *Can I follow this? Is anyone in danger? Did the payoff pay off?* The defect that matters most is the one class of defect nothing in the pipeline is looking for. ~55 facet dispatches and 7 review cycles all ran *beside* it.

---

## Mapping the symptom to the mechanism

| Reader symptom | Cause |
|---|---|
| "Can't follow what physically happens — disconnected gestures" | The bones *are* disconnected gestures (M1: causality unstored between bones). The renderer can't supply the connective tissue (M3). Variance abstracts the gestures further (M4). |
| "No tension because no jeopardy" | No "someone is at risk" bone was decomposed (M1 — leakage trace 1.1, the threat is fully absent). The renderer can't invent jeopardy (M3). No gate checks for it (capstone). |
| "Ledger scene can't satisfy — reader never saw the act" | The act was never dramatized (above). *And* the ledger scene's own content — the verdict, the reasoning — was never decomposed into the s03 bones either (M1; leakage trace 1.6). The bones are pen-choreography; the accounting is gone. |

The sharp point: the decomposition failure is **not specific to action scenes**. It atomized visible posture and dropped the substance everywhere. The s03 ledger bones are as hollow as the s01 rescue bones — they just *look* fine, because pen-choreography reads as competent prose.

---

## Supporting observation — the accounting itself is dishonest-by-omission

The render-log reports `bones dropped: 0` and `facets dropped: 0 stitcher-side`. The leakage trace shows both are false-clean:

- `bones dropped: 0` is true only in CUT-BONE bookkeeping. Multiple bones (@8, @10, @12, @13, @24–26) reached the draft with their **dramatic action abstracted to invisibility** — the bone label survives, the bone's meaning does not. The log has no category for this.
- `facets rendered` lists six facet types and **silently omits vibes (14 entries) and state-updates (15 entries)** — 29 authored, R2-survived entries that appear in neither the "rendered" nor the "dropped" column. They fall out of the accounting entirely.

The pipeline tracks what it **deletes** well (every R2 tombstone carries a rationale). It is blind to what it **never picks up**. That blindness is the same blindness as Mechanism 1, surfacing in the log instead of the prose.

---

## Recommendations — process changes

Mapped to the mechanism each fixes. R1, R6 overlap the first postop's recommendations 1–2 and are stated here at the mechanism level.

### R1 — Event-coverage contract at decomposition (fixes M1)
`/and-write` Phase 1 must, after decomposing, verify the scene chunk's named events appear as bones. The chunk's `scene_conflict.protagonist_force`, its explicit plot beats, and its load-bearing images become a checklist; each must map to ≥1 bone or be logged as a deliberate omission with rationale. This is an **authoring-time** requirement, distinct from a gate check — the decomposer should not be *able* to finish without it.

### R2 — Make the substance gate stakes-aware (fixes M2)
The declared `stakes_axis` must be the **largest delivered delta** in its scene, or the gate fails. A chapter whose headline axis under-delivers 60% while a non-stakes axis triples its target must not PASS. Separately, tighten the ±1 tolerance band, or require an explicit rationale whenever a delivered delta is below 50% of target.

### R3 — Assign ownership of the physical world (fixes M3 + the recurring modality-floor breach)
The bone-faithfulness fence is correct, so the fix is upstream. *Something* must be responsible for sensory/spatial grounding. Either: (a) the decomposer carries a sensory-grounding quota (N grounding bones per scene), or (b) the facet layer gets an explicit license to author un-bone-anchored sensory beats. Today nothing owns it — which is why c01 *and* c02 both breached the modality floor and both breaches were re-accepted as "documented trade-offs." A defect that recurs every chapter is not a trade-off; it is the system's actual output.

### R4 — Make variance abstraction-aware (fixes M4)
The variance rule must be barred from trading a concrete verb for an abstract one. `"lifts the eyes" → "turned my reading outward"` should be a **flagged** move, not a free one. If two bones repeat a physical action, the correct fix is upstream (the bones should differ, or one is redundant) — not a render-time abstraction. Add an abstraction-direction check to the Phase 1 variance-move log.

### R5 — Add one additive editorial pass (fixes M5)
The pipeline needs exactly one pass whose verbs are `EXPAND` / `GROUND` / `STAGE` / `NEEDS-BEAT`, not `CUT`. It cannot live in the stitcher (the fence forbids the stitcher adding content) — its findings must route back to `/and-write` as revise signals. Best placed as a new `/and-write` review step or a `/and-review` subcommand fired before a chapter is declared terminal.

### R6 — Add a cold-read of the assembled draft (fixes the capstone — highest leverage)
Before a chapter is terminal, one agent reads `draft/<chapter>.md` **cold** — no bones, no facets, no chunk — and answers three questions: *What physically happened? Who was at risk? Did the chapter deliver its `goal`?* The cold read's recovered summary is then diffed against the chapter `goal` and `scene_conflict`. If the cold reader cannot recover the goal, the chapter fails and routes to `/and-write revise`. This is **one dispatch**. It catches the entire class of defect that 55 facet dispatches and 7 review cycles missed, because it is the only check that measures the whole instead of a part.

### R7 — Fix render-log accounting honesty (fixes the dishonest-by-omission observation)
`facets dropped: 0` and `bones dropped: 0` must be reconciled against the cite-index: rendered + dropped must equal authored, and any non-zero unrendered remainder surfaces as a flag, not a silence. Add a `RENDERED-ILLEGIBLE` disposition for bones whose action survives as a label but not as a dramatized event — distinct from `CUT-BONE`.

---

## Bottom line

The b01c02 draft is abstract, disconnected, and jeopardy-free because the pipeline **systematically converts events into gestures, gestures into perception, and perception into abstraction** — and then certifies the result, because every gate measures a part and no gate measures the whole. The chunk was good. The decomposition was the first cut, and everything downstream faithfully processed the wound. The single highest-leverage fix is **R6**: make one agent read the finished chapter as a reader before calling it done.
