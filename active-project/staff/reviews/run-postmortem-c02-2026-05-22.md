# Postop — b01c02 full-process audit

date: 2026-05-22
scope: /and-substance chapter b01c02 → /and-write b01c02 → /and-facets b01c02 → /and-stitch b01-c02
method: process audit (showrunner thread) + 4 forked content reviews (one per command output) + element-leakage trace; stitched piece additionally reviewed for readability + entertainment
deliverable under audit: active-project/draft/b01-c02.md (675 words)
companion: run-postmortem-c02-rootcause-2026-05-22.md (mechanism diagnosis — why the prose reads as it does)

---

## RECOMMENDATIONS

### A — Immediate (b01c02-specific)

**A1.** `/and-write b01c02 redo` — re-decompose s01 and s02. Add bones for: the sweep reaching toward bodies (threat materialized); the rescue as an *ordered causal sequence* (Wren needs an exit → Taylor closes the wrong lanes → Wren takes the open one → Wren clear); the two witnesses embodied with a reaction; Coll's recognition-and-silence staged. Then re-cascade `/and-facets` + `/and-stitch`.

**A2.** Register the "Tickler's Lane two days gone" reference as a continuity commitment in showrunner memory, or cut it from Wren's dialogue — currently invented backstory the reader cannot verify (C12).

### B — Process changes (ranked by leverage)

**B1 — Add a cold-read gate before a chapter is terminal. (Highest leverage.)** One agent reads the finished `draft/<chapter>.md` with no bones, no facets, no chunk, and answers the reader's questions. If it cannot recover the chapter's central event, or would not continue, the chapter fails and routes to `/and-write revise`. One dispatch; catches the entire class of defect that ~55 facet dispatches and 7 review cycles missed, because it is the only check that measures the whole instead of a part. **Prompt below.**

**B2 — Event-coverage contract + bone-gate event-presence check.** At authoring time, `/and-write` Phase 1 must map every named event in a scene chunk to ≥1 bone, or log a deliberate omission with rationale. At gate time, Phase 6 must verify the chunk's `scene_conflict.protagonist_force` and central event appear as bone(s) — not only that axis ticks aggregate. This is the structural fix for the C1/C2 root cause; without it the next chapter repeats it.

**B3 — Make the substance gate stakes-aware; tighten the ±1 band.** The declared `stakes_axis` must be the largest delivered delta in its scene, or the gate fails. Require an explicit rationale whenever a delivered delta is below 50% of target. A ±1 band wide enough to pass a 40%-realized headline axis is not a binding target (C10).

**B4 — Assign ownership of the physical world.** Stop accepting per-chapter sensory exemptions — c01 and c02 both breached the modality floor, so the floor is fictional. Either the decomposer carries a per-scene sensory-grounding bone quota, or the facet layer gets explicit license to author un-bone-anchored sensory beats. A sensory-empty bone set must be a bones-revise trigger, not a facet trade-off (C6).

**B5 — Add one additive editorial pass.** The pipeline's editorial verbs are all subtractive (CUT/CULL/COMPRESS/REWORD). Add exactly one pass whose verbs are EXPAND / GROUND / STAGE / NEEDS-BEAT. It cannot live in the stitcher (the bone-faithfulness fence forbids the stitcher adding content) — its findings route back to `/and-write` as revise signals.

**B6 — Make variance abstraction-aware.** Bar the stitcher's anti-repetition variance rule from trading a concrete verb for an abstract one (the render-log shows `"lifts the eyes" → "turned my reading outward"` as a free move). Repeated physical actions are an upstream bones problem, not a render-time abstraction license.

**B7 — Route `/and-write` Phase 6 SIGNALs to disposition before emit.** Phase 6 SIGNALs are currently logged, not actioned — `@13`'s fragile proxy-hold shipped unremediated. A SIGNAL must be either remediated or explicitly accepted with rationale before bones emit (C11).

**B8 — Make `/and-review bones` mandatory** between `/and-write` and `/and-facets`. The decomposition is the highest-consequence step and currently has no independent review — only the mechanical bone-gate (C14).

**B9 — Add a thematic-axis-coverage check to the contract review.** The review must ask whether the contract declares the axis the chapter `goal` names. moral-framework — c02's thesis axis — was absent from chapter-level deltas and the mechanical review never noticed (C8).

**B10 — Fix render-log accounting honesty.** Reconcile rendered + dropped against the cite-index entry count; a non-zero unrendered remainder must surface as a flag, not a silence (vibes 14 + state-updates 15 vanished from the accounting). Add a `RENDERED-ILLEGIBLE` bone disposition, distinct from `CUT-BONE`, for bones whose action survives as a label but not as a dramatized event.

B2/B4/B3 connect to the already-OOS follow-on items in CLAUDE.md ("absolute-length floor mechanism", "plot-arc-completion dramatist check"). The full mechanism behind these recommendations is in the companion doc.

---

## COLD-READ PROMPT (recommendation B1)

Drop-in agent prompt. Dispatch once, after `/and-stitch`, before a chapter is declared terminal. Use a `general-purpose` agent.

> You are a first-time reader. You have been handed one chapter of a novel and nothing else — no outline, no synopsis, no notes. Read it once, at reading pace, the way someone who picked up the book would.
>
> Read ONLY this file: `active-project/draft/<book>-<chapter>.md`. Do not open bones, facets, scene chunks, render-logs, showrunner memory, or any other project file. If you read anything else, the test is void — your value here is that you are uninformed.
>
> Then answer, from the text alone:
> 1. **EVENTS** — What physically happens in this chapter? List the events in order, plainly. If a stretch of the chapter contains no event you can name, say so explicitly.
> 2. **JEOPARDY** — Is anyone at risk of anything? Who, of what, and how do you know it from the text? If nothing is at stake, answer "no jeopardy."
> 3. **CAUSALITY** — Does each scene connect to the next by cause? Point to any place where you could not tell why something happened, or why a character did what they did.
> 4. **PAYOFF** — Does the chapter end on something earned — a consequence, a decision, a turn? Did the ending land, given what the chapter actually showed you (not what it gestured at)?
> 5. **CONTINUE?** — Would you, as a reader, turn to the next chapter? Answer yes or no, one sentence why.
> 6. **ONE-LINE SUMMARY** — Summarize the chapter in one sentence, the way you would to a friend.
>
> Be blunt. Do not be generous. If you were confused, say you were confused and where. Report under 500 words.

Harness step after the agent returns: diff answer 1 + answer 6 against the chapter's `goal` and `scene_conflict` in showrunner memory. **Fail the terminal gate** — route to `/and-write revise` — if the cold reader's recovered events do not include the chapter's central event, or if answer 5 is "no," or if answer 2 is "no jeopardy" on a chapter whose `dramatic_shape` is not a pure coda.

---

## Verdict

**b01c02 is a structural failure. The terminal deliverable is missing its three core events.** The chapter does not deliver its `goal` ("the prohibition in its first real test — deployed against a genuine threat"). It is not a polish problem and not a salvageable draft — it needs re-decomposition from the bones up.

The pipeline did not malfunction in the ordinary sense: every gate passed, every command logged a clean run, the orchestrator-critic returned SUCCESS 7/7. That is the finding. **A hollow chapter walked the whole pipeline green.**

Readability / entertainment verdict (stitched piece): a cold reader cannot follow what physically happens — disconnected gestures, no connecting story. No tension, because no jeopardy. The ledger scene cannot satisfy, because the reader never saw the act being accounted for. Most readers would not continue to chapter 3.

---

## Root cause

The chapter chunk authored by `/and-substance` is rich and correct. The bone decomposition at `/and-write` Phase 1 dropped the chapter's three load-bearing events. Every command downstream then faithfully processed the hollowed bone set. No gate caught it because **no gate tests whether the chunk's named events are present as bones** — they test SVO form, axis-tick aggregates, citation integrity, and facet taste. The chapter was hollow before `/and-facets` ever ran, and ~55 facet dispatches polished the hollow.

The single most consequential defect is **C2 below**: the substance bone-gate measures axis-*tick* movement, not event-*presence*. It is a pipeline-level blind spot, not a one-chapter slip. The companion doc traces the full mechanism — how the pipeline systematically converts events into gestures, gestures into perception, and perception into abstraction.

---

## Findings (ranked)

### C1 — CRITICAL — The Wren rescue is dissolved
The chapter's central event — Taylor uses insect-sense to route the child Wren clear of a conscription sweep — does not exist in the finished prose. The chunk is explicit ("Wren... is in the path of it... Taylor uses insect-sense to locate and pull Wren clear"). The bones render it as: `@5 the insects close the lane-mouths` / `@6 wren enters the alley`. There is no bone for Wren-in-danger, none for the rescue as causal sequence, none for Wren-reaching-safety. In the draft the insects seal the lanes (L11) *before* Wren appears (L13) — causally the prose shows Taylor sealing an alley and a child then wandering into a sealed box. **It reads as a trap, not a rescue.** A cold reader cannot tell a rescue occurred.

### C2 — CRITICAL — The substance bone-gate verifies ticks, not events
`write-b01c02-bone-gate.md` passes `@6 wren enters the alley` with the note "routing worked with Wren as variable; social-tether seed crystallization has visible cause." The bone contains no routing, no danger, no rescue — the gate imported the chunk's intent *into* a bone that carries none of it. The gate would pass insects closing lanes for no reason. "Axes moved" and "the scene happened" are different claims; only the first is gated. This is the structural fix the next chapter depends on.

### C3 — HIGH — The threat never materializes on-page
The pressed-labor sweep is glossed in the abstract (L8–L9) and then narrated as already-over (L15 "The Watch passed the Hook"; L25 "well past now"). No watchman is shown reaching for anyone; no smallfolk is taken. The "genuine threat" the goal promises has no body. There is no jeopardy, therefore no test, therefore the chapter's premise is inert.

### C4 — HIGH — The two witnesses (thematic payload) are phantoms
The "two witnesses with a question they cannot name" are the chapter's *unpriced cost* — the entire accounting scene exists to weigh them. In the prose they are "Two faces held the wrongness a beat too long" (L17) and "The near witness crossed the lane" (L29). No bodies, no reaction. The ledger scene weighs a cost the reader never saw incurred.

### C5 — HIGH — Coll's "saw it, stayed silent" beat is absent
The chunk calls for Coll seeing Taylor's hand in the alley's geometry and choosing not to name it — a social-tether anchor the substance contract leans on. The prose gives only "Coll worked the net" (L21) and Coll lifting his eyes / pulling up the net (L23). No recognition, no withheld knowledge. The beat survived into the s02 chunk text and died between bones and prose.

### C6 — HIGH — The sensory modality-floor breach is recurring, not a trade-off
`/and-facets` shipped a sound-only sensory facet (sensory:2 deleted, "no valid anchor"), framed as a one-time "audience-accepted documented trade-off." It is not one-time — b01c01 *also* collapsed to a single modality. When the exemption fires every chapter, the floor is fictional and the "trade-off" vocabulary is laundering a recurring upstream defect. Root cause is the bones: 27 near-identical posture verbs ("lifts the eyes," "faces the alley-mouth," "works the net") give the facet layer almost nothing physical to anchor to.

### C7 — MEDIUM — Over-abstraction; Flea Bottom vanished as a place
~30 of 45 body sentences are abstract or nominalized ("My body was catching up to a thing already filed"; "The count of who had seen was set by faces I had not picked"; "The reach was cleared"). b01c01 had mud, drain-channels, tallow-smoke, a meat-stall, copper coins. c02 has "eaves," "threshold," "lane-depth" — generic geometry nouns. The slum is gone. This is a regression from the prior chapter.

### C8 — MEDIUM — moral-framework under-declared in the substance contract
The chapter's thematic axis — the prohibition "flexing" — appears in *no* chapter-level `axes_in_motion` or `axes_held`; it surfaces only at s03 as held-at-3. The contract under-declares its own thesis, and the contract review (`contract-b01c02-*.md`) is purely mechanical (sum-checks, enum-checks) — it never asks whether the contract declares the axis the `goal` names.

### C9 — MEDIUM — Effort allocation is inverted
`/and-write` — the command that could have caught the lost rescue — got 7 commits and one mechanical gate. `/and-facets` — which can only decorate — got ~25 commits, 3 audience-gate cycles + 4 audit cycles, ~55 dispatches. The orchestrator-critic called 55 dispatches "healthy iteration"; it was defensive churn (relocating then deleting sensory:2, recasting narrator:6, marker hygiene) whose net content change was one deletion. The review apparatus spent its budget polishing facets on an already-hollow chapter.

### C10 — MEDIUM — Headline axis under-delivered 60%; the ±1 band makes targets non-binding
Capability — the chapter's central arc move (first deployment of the prohibition) — target 1.0, delivered 0.4. The gate passed it "within ±1 rank." Knowledge over-delivered 160% (target 0.5, delivered 1.3, 13 ticks). The numbers confirm the prose: a chapter of *watching*, not *doing*. A ±1 band wide enough to pass a 40%-realized headline axis is not a binding target.

### C11 — MEDIUM — Phase 6 SIGNAL never remediated
The bone-gate flagged `@13` (Coll, capability held, "proxy-hold") as a fragile non-licit hold form and recommended fixer reclassify it. It was carried forward unremediated into the shipped bones and into stitch. `/and-write` Phase 6 SIGNALs are logged, not actioned.

### C12 — LOW — Continuity: unanchored "Tickler's Lane" reference
Wren's dialogue references "Tickler's Lane two days gone, and the lane went quiet after" — an off-page event with no anchor in b01c01, no anchor in c02, registered nowhere in showrunner memory. Invented backstory the reader cannot verify; either register it as a continuity commitment or cut it.

### C13 — LOW — Audit report internally contradicts itself
`facets-final-audit.md` asserts "two distinct modalities... Cross-modal coverage met" (stale pre-deletion text) while the final state is sound-only. The report was never reconciled across its 4 cycles.

### C14 — PROCESS — No independent chunk→bones fidelity review ran
`/and-review bones` / `/and-review chunk` were not invoked for c02. The only check on the decomposition was the mechanical bone-gate (C2). The contract was reviewed; the bones were not.

---

## Element-leakage trace (summary)

A forked trace walked every authored element forward to the draft. **~28 elements never arrive.** Highlights beyond C1/C3/C4/C5:
- The ledger scene's *content* — the classification question, the verdict, the cost line entered — was never decomposed into the s03 bones. The s03 bones are pen-choreography ("writes the line," "strikes the line," "underlines the entry"). The chunk's designated load-bearing scene is rendered as opaque gesture.
- **All 14 vibes entries and all 15 state-updates entries reach the draft as zero citations** — and the render-log lists them under neither "rendered" nor "dropped." 29 authored, R2-survived entries fell out of the accounting.
- The render-log's `bones dropped: 0` / `facets dropped: 0` are false-clean. The pipeline tracks what it *deletes* (every R2 tombstone has a rationale); it is blind to what it *never picks up*.

---

## What worked (for balance)

- `/and-substance` chunk authoring is genuinely strong — rich, correct, and it avoids the cheap version (it stages routing-without-override and makes the *accounting* the dramatic object).
- Scene 3 (the ledger scene) is faithfully decomposed *structurally* — the bone count and SVO are sound; the failure there is content-depth (the accounting's reasoning was never atomized in), not structure.
- The stitcher executed cleanly: 0 cut-bones, caught and cut the `@28` fence-stretch (an impersonator-invented clause contradicting narrator:6). The stitcher did its job correctly — its job was rendering a hollow bone set.
- The pipeline's deletion/exemption markers are *honest*; it documents its compromises rather than hiding them. Honesty about a defect is not a fix, but it made this audit possible.
