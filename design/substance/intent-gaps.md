# Plan Intent Gaps vs. Active-Project Feedback

**Source:** Critical read of `design/substance/plan.md` against `active-project/feedback.md` (s01e01–s01e03 user feedback).
**Status:** Open. Surface for next session before plan execution.
**Date:** 2026-05-16.

The plan's "Triggering feedback" header (`plan.md:5-12`) excerpts 7 lines from the 19-line feedback file. Some of the feedback that wasn't excerpted points at real architectural questions the plan currently glosses or punts on. Below: where the plan misses or partly misses the user's intent, organized by severity.

---

## INTENT-MISS — bones-too-fine-grained vs. plan-adds-a-deeper-level

**Feedback:** "The plot is very very weak. I believe that the protolines aren't being focused enough or the bones are too fine grained." + "protolines should cover the action and movement of a scene."

**Plan response:** Introduces a new **beat** level *below* scene. Bones are now authored at beat level by `/and-write`, where previously protolines were authored at episode level by `/and-protolines`. Net effect: bones are **finer-grained** than protolines were.

**Why this misses:** The user's diagnosis is "too granular" + their prescription is "scene-scoped action+movement." The plan structurally moves in the opposite direction — beat-scoped, smaller, more numerous. The plan reads "your bones are wrong-sized" as "you need more chunking levels"; the user said "your bones are wrong-sized" meaning "make the bone unit cover a whole scene's worth of motion."

**Suggested resolutions (pick one):**
- **A.** Drop the beat level entirely. Five chunk levels → four (series → book → chapter → scene). `/and-write` reads scene chunks; one bones list per scene; each bone covers a meaningful scene-action. Matches "protolines should cover the action and movement of a scene" literally.
- **B.** Keep the beat level as a *planning* aid but author bones per *scene*. Beats decompose a scene's substance contract; bones aggregate beats into scene-scoped action units. The beat → bone mapping is many-to-few (a scene's 3-5 beats become 1-3 bones).
- **C.** Keep current plan and add a hard bone-coarseness floor: each bone must describe scene-significant action (i.e., it changes a tracked axis by ≥1 rank, no chatter-bones, no breath-bones).

This is the **single most important question** for the plan; it should be a top-level open question, not buried in spec detail.

---

## INTENT-MISS — scene-should-be-most-of-chapter vs. plan-encourages-many-small-scenes

**Feedback:** "Scenes were way way too small. A scene should be a significant (like most) of a chapter."

**Plan response:** Introduces a `scenes_per_chapter: <range>` field but doesn't set a default or articulate a guideline. The recursive `/and-substance` model with a dedicated scene level structurally invites many small scenes (else why have the level?).

**Why this misses:** The user is saying scenes should be **substantial units that fill most of a chapter** (1-3 scenes/chapter, not 6-10). The plan's architecture doesn't bias toward this and could easily produce the same too-small-scene problem.

**Suggested resolutions:**
- Spec the default `scenes_per_chapter: 1-3` in `design/substance/delta-targets.md`.
- State explicitly in `design/substance/README.md`: "Scenes are substantial; a typical chapter has 1-3 scenes, each consuming most of a chapter's content. Many small scenes is an anti-pattern."
- Audience review at `/and-substance chapter` Phase 5 should flag "scenes-too-small" as a HARD finding when scene_count > 3 or scene_chunks are slight.

This couples tightly with the bones-grain question above. If scenes are big and bones cover scene-action, the chunking lands at the right size.

---

## INTENT-MISS — substance-flat as SIGNAL, not HARD

**Feedback:** "Episodes felt empty and meaningless and like a puff of air, there was no substance" — the user's headline complaint.

**Plan response:** `/and-write` Phase 6 (substance bone-gate) classifies `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>`. The plan says "HARD findings block emission; SIGNAL findings record but pass" but **does not classify which findings are HARD vs. SIGNAL.**

**Why this misses:** If `SUBSTANCE-FLAT` is a SIGNAL finding, the bone-gate logs flatness and lets the chapter ship — which is exactly the failure mode that produced s01e01-s01e03. The single feature most designed to address the user's feedback may not actually block on it.

**Suggested resolution:** Explicitly classify:
- `SUBSTANCE-FLAT-<axis>` → **HARD** (blocks emission; revise required).
- `SUBSTANCE-SUSPECT-cheap-gain-<axis>` → **HARD** (cost-ledger gap; revise required).
- `SUBSTANCE-FELT` → PASS.
- Cost-paid violation (declared cost not visible in bones) → **HARD**.
- Per-scene Δ within ±1 rank but bones-count below density-target → **SIGNAL**.

Document this in `/and-write` Phase 6 spec.

---

## INTENT-MISS — stitcher-formatting feedback explicitly punted

**Feedback (s01e02):** "Dialogue was decent, but everything was smashed together. Should be new lines for when different characters speak."
**Feedback (s01e03):** "Calling out scenes breaks immersion."

**Plan response:** `/and-stitch` is declared **unchanged**. Polish is deferred entirely. The plan acknowledges this is intentional.

**Why this partly misses:** The user's summary line is "the prose reads decently, the dialogue is on point" — meaning the issue is **not** prose polish requiring `/and-wrap`. The issues are **structural rendering**: speaker-turn paragraph breaks + suppression of scene callouts. Both are `/and-stitch` Phase 5 (local flow) / Phase 8 (finalize) concerns, not editor-pass polish concerns.

The plan punts these to "polish deferred" but they're not polish — they're stitcher rendering bugs. Leaving `/and-stitch` literally unchanged means s01e04 ships with the same two problems.

**Suggested resolution:** Carve out a narrow `/and-stitch` patch (separate from the substance overhaul, or a small section in the plan):
- Speaker-paragraph rule: any new speaker starts a new paragraph.
- Scene-callout suppression: no `## Scene N` headers or `[SCENE BREAK]` markers in rendered prose. Scene boundaries are conveyed by paragraph break only.

Or explicitly add to plan's "Out of scope": "These two `/and-stitch` formatting issues from s01e02/s01e03 feedback are NOT addressed by this overhaul; track separately."

---

## INTENT-MISS — "too short" not addressed structurally

**Feedback:** "All the episodes were too short." + "Way too short. What even was the point of this chapter?"

**Plan response:** Bone-count bands and density targets are mentioned (`design/substance/delta-targets.md`) but the plan never sets a minimum-length floor. Δ + density can be satisfied in a small absolute volume.

**Why this misses:** A chapter can hit its substance contract in 800 words and still feel "way too short." Density is a ratio; absolute length is not tracked.

**Suggested resolution:** Add to `series.structure.book_length`:
- `chapter_word_count_floor: <int>` (e.g., 3000 words)
- `scene_word_count_floor: <int>` (e.g., 1500 words)
Verified at `/and-stitch` output (post-render) — Phase 8 finalize emits a length warning if below floor. Or verified earlier at `/and-write` Phase 6 via bones-count × bones-per-word estimate.

Cleaner: tie the floor to the chunk-count × per-chunk-bones × per-bone-word estimate so it falls out of the existing schema rather than being a separate field.

---

## INTENT-MISS — cross-chapter continuity / "episodes barely fit together"

**Feedback:** "The episodes barely fit together, and the protagonist suddenly getting relay bugs (which is a big deal) for no reason is odd."

**Plan response:** `/and-write` Phase 5 does state-thread continuity *within a chapter*. Book-level Δ exists but doesn't structurally enforce per-chapter handoff (chapter N+1 inheriting state + open threads from chapter N).

**Why this misses:** "Episodes barely fit together" + "relay bugs for no reason" is a cross-chapter continuity failure. State changes that pop up without prior chapter setup. Within-chapter state-thread doesn't catch this.

**Suggested resolution:** Add to chapter-level chunk schema:
- `handoff_in:` — state inherited from prior chapter (open threads, world-state, character-state).
- `handoff_out:` — state passed to next chapter (resolved/unresolved threads, axis ranks at chapter end).
- `/and-substance book` Phase 5 dramatist verifies `handoff_out` of chapter N matches `handoff_in` of chapter N+1.
- `/and-review consistency` adds a cross-chapter-handoff sweep.

---

## INTENT-MISS — emotional-substance not required orthogonally to plot-substance

**Feedback (s01e01):** "There should be some harsh feels with protagonist coming back to life after 3 days."

**Plan response:** The substance signature lists state axes (wealth, health, community, emotional, ...). Axes are picked per-chunk. There's no constraint that emotional axes must move when plot-stakes-events occur.

**Why this misses:** A chapter could satisfy its contract entirely on wealth/community axes while a plot event of "protagonist returns from the dead" produces zero emotional Δ — which is exactly the s01e01 failure mode the user flagged.

**Suggested resolution (pick one):**
- **A.** Require per-chapter Δ to span ≥2 axis classes (e.g., one plot axis + one emotional axis), where axes are pre-tagged with class in `series.substance.state_axes[].class`.
- **B.** Add an "emotional-resonance check" to audience review at the bone-gate: when a chapter contains a stakes-event (death, return, betrayal, revelation), the audience must verify emotional-axis Δ landed; SUBSTANCE-EMOTIONALLY-FLAT is a HARD finding.

---

## PARTIAL-MISS — plot-arc-completion vs. "what was the point of this chapter?"

**Feedback (s01e02 + s01e03):** "What even was the point of this chapter?" / "I'm not really sure what this chapter was supposed to do."

**Plan response:** `/and-substance chapter` Phase 4 authors "chapter dramatic shape (rising / climax / falling / hinge)." Phase 5 dramatist checks shape.

**Why this partly misses:** A dramatic-shape tag is not the same as a complete dramatic-arc unit. "Rising" describes a curve, not whether the chapter has setup + complication + something-changed-by-end. A chapter could be tagged "rising" and still leave the reader asking "what was the point?"

**Suggested resolution:** `/and-substance chapter` Phase 5 dramatist check should verify, in addition to shape, that the chapter has a **dramatic-arc completion**: identifiable setup beat, identifiable complication beat, identifiable resolution-or-cliffhanger beat. Chapter chunk text must answer "what changed by the end?" in one line.

This is close to existing dramatist rubric but needs to be made explicit.

---

## PARTIAL-MISS — world-law / setting-detail consistency

**Feedback (s01e01):** "The bowl is weird." / "Do smallfolk have salt?"

**Plan response:** `/and-project` Phase 2 1d does "world-law finalization (condition cards)." `/and-review consistency` is generic.

**Why this partly misses:** "Do smallfolk have salt?" is class-level economic detail — finer than world-law, coarser than prop-card. The current plan's consistency surface doesn't have an obvious home for "does this object/resource belong in this setting for this class of character."

**Suggested resolution:** `/and-review consistency` adds a `--world-detail` axis: dispatches against location card + condition cards + relevant persona cards to check whether per-line props/resources fit the setting at the class/economic level. Or add a world-detail-audit pass inside `/and-write` Phase 5 (continuity) that checks bones for setting-anachronism.

---

## CLARIFICATION-NEEDED — "episode" → "chapter" mapping for user mental model

**Feedback throughout** refers to "episodes" (s01e01, s01e02, s01e03). The plan dissolves "season"/"episode" framing; under the new chain those become "books" and "chapters."

**Plan gap:** No statement of how the new "chapter" maps to the old "episode" in user terms. Should a chapter be roughly the length of an episode (~3000 words)? More? Less? Is the chapter the **terminal unit of consumption** (the thing the user reads in one sitting)?

**Suggested resolution:** Add to `design/substance/README.md`:
- "A chapter is the terminal unit of consumption — one chapter ≈ one previous episode in scope and length (~3000-5000 words, 1-3 scenes)."
- The user's "episode" feedback maps to chapter-level concerns in the new chain.

This isn't a deep design question but it removes ambiguity.

---

## OBSERVATION — no scene-level antagonist pressure

**Feedback:** "Scenes should have meaningful suspense and action with something against something."

**Plan response:** Antagonist pressure is in `series.substance.antagonist_pressure[]` (series-level signature). Scene contracts inherit axes but the plan doesn't require scene contracts to name what-is-against-what at the scene level.

**Why this partly misses:** Series-level antagonist pressure can be satisfied across the arc without every scene having "something against something." Scene-level conflict is what produces "meaningful suspense" — the user's specific ask.

**Suggested resolution:** Add to scene chunk schema:
- `scene_conflict: { protagonist_force: <one line>, opposing_force: <one line>, stakes: <axis-slug> }`
- `/and-substance chapter` Phase 5 dramatist verifies every scene chunk has a `scene_conflict` populated and that the opposing force is concrete (not "fate" or "circumstance" hand-waves).

---

## Summary of recommended next-session actions

1. **Top-priority redesign question:** bones-grain (per-beat vs. per-scene). This is the user's central complaint and the plan currently moves in the wrong direction. Resolve before any implementation.
2. **Substance-flat HARD/SIGNAL classification** in `/and-write` Phase 6. Cheap fix; high impact.
3. **Scenes-are-big guideline** in `design/substance/README.md` + delta-targets.md.
4. **Stitcher formatting carve-out** for the two stitcher-rendering bugs the user flagged (speaker breaks + scene-callout suppression). Either patch `/and-stitch` minimally or explicitly carve them as out-of-scope-tracked-separately.
5. **Cross-chapter handoff fields** in chapter chunk schema.
6. **Emotional-substance-required** rule (axis-class spanning OR emotional-resonance check).
7. **Plot-arc-completion** in `/and-substance chapter` Phase 5 dramatist rubric.
8. **Chapter ≈ episode** mapping documented for user mental model.
9. **Scene-level antagonist pressure** field on scene chunks.
10. **Absolute-length floor** mechanism (either word-count floor or derived from bones × words-per-bone estimate).
11. **World-detail consistency** under `/and-review consistency` or `/and-write` Phase 5.

Items 1–4 are the heavy hitters. Items 5–11 are smaller tightening.
