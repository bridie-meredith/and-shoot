# Postop — b01c02 full-process audit

date: 2026-05-22
scope: /and-substance chapter b01c02 → /and-write b01c02 → /and-facets b01c02 → /and-stitch b01-c02
method: process audit (showrunner thread) + 4 forked content reviews (one per command output); stitched piece additionally reviewed for readability + entertainment
deliverable under audit: active-project/draft/b01-c02.md (675 words)

---

## Verdict

**b01c02 is a structural failure. The terminal deliverable is missing its three core events.** The chapter does not deliver its `goal` ("the prohibition in its first real test — deployed against a genuine threat"). It is not a polish problem and not a salvageable draft — it needs re-decomposition from the bones up.

The pipeline did not malfunction in the ordinary sense: every gate passed, every command logged a clean run, the orchestrator-critic returned SUCCESS 7/7. That is the finding. **A hollow chapter walked the whole pipeline green.**

---

## Root cause

The chapter chunk authored by `/and-substance` is rich and correct. The bone decomposition at `/and-write` Phase 1 dropped the chapter's three load-bearing events. Every command downstream then faithfully processed the hollowed bone set. No gate caught it because **no gate tests whether the chunk's named events are present as bones** — they test SVO form, axis-tick aggregates, citation integrity, and facet taste. The chapter was hollow before `/and-facets` ever ran, and ~55 facet dispatches polished the hollow.

The single most consequential defect is **C2 below**: the substance bone-gate measures axis-*tick* movement, not event-*presence*. It is a pipeline-level blind spot, not a one-chapter slip.

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

## What worked (for balance)

- `/and-substance` chunk authoring is genuinely strong — rich, correct, and it avoids the cheap version (it stages routing-without-override and makes the *accounting* the dramatic object).
- Scene 3 (the ledger scene) *is* faithfully decomposed and rendered — the reflective scene works on the page.
- The stitcher executed cleanly: 0 cut-bones, caught and cut the `@28` fence-stretch (an impersonator-invented clause contradicting narrator:6). The stitcher did its job correctly — its job was rendering a hollow bone set.
- The pipeline's deletion/exemption markers are *honest*; it documents its compromises rather than hiding them. Honesty about a defect is not a fix, but it made this audit possible.

---

## Recommendations

1. **`/and-write b01c02 redo`** — re-decompose s01 and s02. Add bones for: the sweep reaching toward bodies (threat materialized); the rescue as an *ordered* causal sequence (Wren needs an exit → Taylor closes the wrong lanes → Wren takes the open one → Wren clear); the two witnesses embodied; Coll's recognition-and-silence staged. Then re-cascade `/and-facets` + `/and-stitch`.
2. **Bone-gate event-presence check (follow-on issue)** — the gate must verify the chunk's `scene_conflict.protagonist_force` and named central event appear as bone(s), not only that axis ticks aggregate. This is the structural fix; without it the next chapter repeats C1.
3. **Escalate the modality-floor breach as a `/and-write` defect.** Stop accepting per-chapter sensory exemptions. If bones yield nothing physical, that is a bones-revise trigger, not a facet trade-off.
4. **Route `/and-write` Phase 6 SIGNALs to fixer before emit** — do not ship known-fragile bones (C11).
5. **Tighten the ±1 axis band**, or require an explicit rationale when delivered delta is <50% of target (C10).
6. **Make `/and-review bones` a mandatory step** between `/and-write` and `/and-facets` (C14).
7. **Add a thematic-axis-coverage check to the contract review** — does the contract declare the axis the `goal` names? (C8)
8. **Register or cut the "Tickler's Lane" reference** (C12).

Items 2, 3, and 5 connect to the already-OOS follow-on items in CLAUDE.md ("absolute-length floor mechanism", "plot-arc-completion dramatist check"). The bone-gate event-presence gap (item 2) is the highest-leverage fix surfaced by this audit.
