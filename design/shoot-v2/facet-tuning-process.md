# Facet Tuning Process — Replicable Pattern

How we tuned the dialogue facet from 40% → 100% audience-accept under a strict rubric. This document abstracts the process so the same pattern can be applied to other facets (voice, prose, blocking, environment-perception, action-cost, etc.).

**Companion docs**
- `round-trip-method.md` — running catalog of changes to writers and reviewers (the in-flight log this process emerged from).
- `dialogue-corpus.md`, `audience-review-originals*.md`, `round2-output-*.md`, `round3-defense-*.md`, `audience-*.md` — the worked example artifacts.

---

## When to use this process

You have a facet that:
- has at least one **behavior card or equivalent rubric** authored (or near-authored)
- has **existing project content** that can be sampled as a training corpus, *or* you can synthesize one
- has an **active audience** (3 personas) that can review per-line / per-unit
- you suspect is contaminated or under-performing — the rubric exists, the output isn't honoring it

If no rubric exists yet, you build the rubric first (separate problem). This process tunes a writer + reviewer against an existing rubric.

---

## The process — five phases

### Phase 0 — Prep

1. **Sample the corpus.** Extract every unit of the facet from existing project content (e.g. for dialogue: every quoted line, with speaker + locator). Save as a flat list grouped by the rubric's primary axis (for dialogue: behavior card; for prose: voice register; etc.).
2. **Confirm rubric authority.** Every unit must be assignable to one rubric category. Ambiguous units are a rubric problem — surface them explicitly.
3. **Convert source content to training format if needed.** *(For shoot-v2 facets, this is the proto-line / SVO split — splitting current active content into the new format will precede facet tuning. Rough is fine for training; precision can be improved later.)*

### Phase 1 — Reviewer tuning *(always before writer tuning)*

The reviewer is the source of truth for "did the writer do the job." Tune it first or you will tune the writer against a soft target.

1. **V1 lenient pass** — review the corpus under "does the unit not violate its assigned rubric category?" Record accept rate.
2. **V2 strict pass** — same corpus, tightened to "does the unit affirmatively demonstrate at least one signature feature of its assigned category, AND not violate it?" Inoffensive ≠ on-rubric. Record accept rate; this becomes the **baseline to beat**.
3. **Defend the floor.** If the audience pushes back on rejecting specific units (because they genuinely earn it), accept the pushback. *The audience refusing to over-reject is what makes the rubric trustworthy.* A rubric that rejects everything is as broken as one that accepts everything.
4. **Lock the rubric.** Once V2 is set, do not soften it for later rounds. Lift numbers are only honest under fixed rubrics.

**Output of Phase 1:** baseline accept rate, defensible floor, six-or-so systemic faults named (the failure modes the corpus exhibits).

### Phase 2 — Writer fork

The writer takes intent + cards and authors fresh units, *blind to the originals*.

1. **One fork per rubric category.** Cross-contamination at generation time is the original failure mode — structurally prevent it by never letting a single writer hold multiple categories at once.
2. **Card stack load order:** leaf → parent (if present) → universal overlay → adjacent referenced cards → speaker/scope persona. Writer reads all of it before drafting.
3. **Blind to originals.** Forbid reading the corpus being regenerated and the source files. Author from intent + cards only. Eliminates paraphrase bias.
4. **Intent specifies state, not text.** The intent describes:
   - the unit's job (what it accomplishes / moves)
   - register / mode / mask state (e.g. for Taylor: mask ON / SLIPPING / OFF)
   - rung within the category (functionary vs. knight-administrator within noble-courtly)
   - context (distance, public/private, paired-unit relationships)
   - **never** a softened paraphrase of the original.
5. **Multi-draft + chosen mark + cited signatures.** Writer produces 2–3 drafts, marks chosen, justifies rejected. Per chosen unit, lists which card-§ signatures are demonstrated. Makes the unit *falsifiable* — the reviewer can test the claims.
6. **Explicit anti-patterns.** Brief lists what *not* to do, with the project-specific contamination named (for dialogue: em-dash + semicolon-spine; for other facets: identify the dominant-POV voice tells).
7. **Calibration anchor.** Include one intent that maps to a known-strong original. Gives the writer a target and the reviewer a control point.

**Sample size:** 3–4 per rubric category is enough for tuning; ~15–20 total. Cheap to re-run.

**Output of Phase 2:** regenerated units. Re-run reviewer under the same locked rubric. Compare accept rates.

### Phase 3 — Adversarial seam-finding

Even on accepts, the audience produces hostile counter-arguments — the strongest single attack per unit ("the seam"). Output is *defense scaffolding*, not new verdicts.

1. **All units challenged**, accepts included. Accepts can be brittle under load.
2. **Persona-distinct seams.** Each persona attacks through its lens (atmosphere / board-move / voice-precision-and-source-material-fidelity). The seam isn't generic craft criticism.
3. **Aggregate to one seam per unit.** The strongest single attack — what the writer must answer.
4. **Pressure the contradictions hardest.** Where the rubric carries a load-bearing tension (for dialogue: Taylor's doubled register), weight challenges there.

**Output of Phase 3:** one seam per unit, audience-blind to writer.

### Phase 4 — Defense or revision

Writer fork (per category) reads the seams and either:

- **DEFEND** with card citation in 2–4 sentences. Use only if the seam misreads the card or the intent.
- **REVISE** with multi-draft + chosen mark + how the seam is answered + signatures demonstrated.

**Both outcomes are valid signal.** A defended accept stays as is — that means the seam was attacking an intended feature. A revision means the seam was load-bearing.

The seam-finding pass also functions as a **sorting mechanism**: it separates "the unit is doing something the rubric didn't credit" from "the unit is doing something it shouldn't." Both kinds of seam appeared in our run.

### Phase 5 — Final adjudication

Audience reviews defended/revised units under the **same locked rubric**. Reports:

- Final accept rate.
- Whether each defense's card-citation actually licenses the move.
- Whether each revision answers the seam or just shifts the failure.
- **Cross-unit dependency check.** Pairs of units that depend on each other (e.g. one character's slip + another character's recognition of it) get adjudicated *together*, not in isolation.
- **Shippability assessment.** Residual failure modes named honestly. The audience must be straight about what didn't fully close.

---

## Trajectory pattern

The dialogue facet ran:

| Round | Stage | Accept | Notes |
|---|---|---|---|
| 1 | Originals, V1 lenient | 57% | rubric too soft |
| 1.5 | Originals, V2 strict | 40% (floor ~17%) | locked rubric |
| 2 | Regenerated, V2 strict | 94% | +54 lift |
| 3 | Defended/revised, V2 strict | 100% | seams closed |

If your trajectory looks substantially different — Phase 2 doesn't lift, Phase 3 produces no useful seams, Phase 4 can't close them — read the diagnosis section of `round-trip-method.md`.

---

## Best-practice principles *(facet-agnostic)*

1. **Tune reviewer before writer.** A soft reviewer makes the writer look good and ships broken units.
2. **Same rubric across all rounds being compared.** Lift is only meaningful under a locked rubric.
3. **Reviewer pushback is signal.** A rubric that defends its floor is more trustworthy than one that ratchets toward 0%.
4. **Per-category writer forks.** Single-writer setups inherit a dominant chassis and contaminate everything. Parallel forks at generation time are cheap structural prevention.
5. **Blind input prevents anchor drift.** Writer never sees what's being regenerated.
6. **Intent specifies state, not text.** Text-paraphrase intents collapse back to the original.
7. **Multi-draft + cited signatures makes units falsifiable.** Reviewer tests claims, not just impressions.
8. **Anti-patterns are first-class brief content.** Naming the contamination does real work.
9. **Calibration anchor in every batch.** Prevents whole-batch upward drift that feels fine but isn't.
10. **Seams ≠ verdicts.** Phase 3 is for surfacing load-bearing attacks, not overturning Phase 2. Defense and revision are both valid responses.
11. **Cross-unit dependency is a planning concern.** Discovering paired-unit dependencies in the defense phase is late. Flag at intent time when possible.
12. **Audience honesty at adjudication.** "Substantially ready, with these named residual risks" is more useful than a clean 100%.

---

## Open questions for replication

- **Surface-area floor.** Can a category be demonstrated on units below ~3 words? Our "Twelve." → "Twelve. Counted." patch suggests yes, but only with a second word doing structural work. Watch for this in facets with naturally short units.
- **Source-material fluency assumption.** Our v2 rubric did not check whether a category-demonstration requires source-material fluency to perceive (Worm-fluency vs. Westerosi-fluency in the Taylor block). Add a fourth rubric criterion at Phase 1: *is the demonstration accessible to a reader with project-fluency but without source-material fluency?*
- **Cross-unit dependencies.** Worth a paired-unit Phase 1 review pass when units are known to depend on each other.
- **Reviewer/writer asymmetry.** Both reload cards. Both cite the same rubric. Open: would a separate "card-mechanic auditor" (just checks cited signatures appear; no taste call) reduce reviewer load and free taste-judgment for higher-order critique? Worth trying on the next facet.

---

## Co-deployment note

The audience adjudication concluded the writer + reviewer pipeline is **substantially shippable as a co-deployed unit**. The two halves are not separable artifacts — the writer's affirmative-citation discipline only works because the reviewer tests citations; the reviewer's strict rubric is only meaningful because the writer can produce units that demonstrate signatures rather than merely avoid violations. Ship together, tune together, version together.

---

## Next facets

This process will be repeated for other facets. Sequence assumed:

1. **Prep step shared across all facets:** split current active content into the new SVO / proto-line format described in `schemas/proto-line.schema.md`. Rough is acceptable for training; the SVO extractor/author itself is on the improvement backlog.
2. Per-facet tuning loops re-running this five-phase process against the new training format.
