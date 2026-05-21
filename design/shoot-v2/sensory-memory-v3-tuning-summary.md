# Sensory + Memory V3 Tuning Summary

**Date:** 2026-05-21
**Status:** V3 rubrics locked. `design/shoot-v2/rubric-sensory.md` and `design/shoot-v2/rubric-memory-flags.md` carry the V3 changes in place; this doc records the harness pass that produced them.
**Trigger:** b01c01 cycle-3 cap-burn (`active-project/staff/reviews/run-action-plan-b01c01-2026-05-20.md` items A7 + A8). Two of twelve facets failed the 3-cycle audience-gate; both root causes were rubric-side, not author-side.

---

## Method

A compressed Phase 0 + Phase 1 walk of the harness in `design/shoot-v2/facet-tuning-process.md`. The corpus is the cap-burn evidence itself — three cycle-3 sensory verdicts + two cycle-2 memory verdicts produced under locked V2. Audience pushback explicitly named the failure modes and proposed the structural fixes; V3 codifies those proposals as rubric clauses so the next chapter's cycle-1 audit catches them mechanically (per CLAUDE.md rule 11: rubric REJECT / anti-pattern edits promote taste calls to mechanical checks via the auditor's RUBRIC-FIDELITY enumeration).

Phases 2–5 of the harness (writer fork, adversarial seam-finding, defense/revise, final adjudication) are deferred to the next `/and-facets` run where the V3 rubrics drive actual authoring — that run IS the validation of these rule changes.

---

## Sensory cap-burn — two root causes (one new)

### Cap-burn evidence

`active-project/staff/audience/sensory-modality-coverage/sensory-r3-verdict.md` — verdict: accept, with:
- Modality floor (≥2) met by adding `sensory:3 @17` at cycle-3.
- Sparsity: 2 entries / 27 bones = 7.4%. Above 6% ceiling. Modality reviewer notes "irresolvable arithmetic consequence of meeting the floor on a short episode" — accepts anyway, but the rubric carries no documented carve-out.

`active-project/staff/audience/sensory-old-state-reader/sensory-r3-verdict.md` — verdict: revise, with:
- `sensory:3 @17`'s old-state `street-quiet-of-mid-afternoon` is unanchored. No prior loc-state entry on the sound modality. "mid-afternoon" is a forward-reference (loc-state:4 declares afternoon at @18, one beat AFTER @17).
- The cycle-3 fixer-ADD introduced this HARD finding on the very fix-path the modality-coverage reviewer demanded. The cycle-3 audit slot caught it; no slot remained to remediate.

### V3 fix 1 — short-chapter floor-vs-ceiling exemption

**Problem:** modality floor (≥2 modalities ⇒ ≥2 entries) and sparsity ceiling (≤6%) are arithmetically incompatible when `bone_count < 30`. The b01c01 case is 27 bones: 6% × 27 = 1.6 entries (≤1), but the floor demands ≥2. The locked V2 rubric had no carve-out; the modality reviewer accepted-with-advisory on first principles, but the asymmetric authority left the file in "accept under reviewer judgment / breach under mechanical scan" limbo.

**Fix:** new "Short-chapter floor-vs-ceiling exemption" clause under *Curve-shape rubric / Episode-level shape*. When `bone_count < 30` AND the file's modality count equals the floor (2), the effective sparsity ceiling relaxes to `max(6%, 2/bone_count)`. The modality floor takes precedence because monoculture is the load-bearing pathology, not marginal density. The exemption does NOT apply when modality count exceeds the floor (3+ modalities at 27 bones → cull to strongest cases under the standard ceiling).

**URI:** URI-FACETS-V3-SHORT-CHAPTER.

### V3 fix 2 — cycle-N ADD pre-validation (anti-pattern #14)

**Problem:** the cycle-3 fixer-ADD of `sensory:3 @17` (added to meet the modality-floor demand from cycle-2 escalation) introduced an unanchored old-state HARD that the same-cycle audit caught. The audience-gate cap was 3 cycles; cycle-4 didn't exist; the file cap-burned. This is the A3 failure mode from the parent action plan: cycle-N fixer ADDs need pre-validation against the full rubric (including old-state lineage) BEFORE committing, otherwise they can fail in a slot that has no remediation budget.

**Fix:** new anti-pattern #14 "Cycle-N ADD without pre-validation." Author / fixer side: validate the proposed ADD against the full rubric before writing — if the ADD requires a loc-state edit (because the old-state has no anchor), the loc-state edit lands FIRST. Auditor side: an ADD that lands at cycle N AND introduces a new finding the prior cycles did not surface is a process violation as well as a content one; report both.

**URI:** URI-FACETS-V3-CYCLE-N-ADD. Related to action-plan item A3 (command-body Phase 5b iteration logic carries the structural / orchestration fix; this rubric anti-pattern carries the rubric-side enforcement so the auditor can mechanically flag the pattern next cycle.)

### What V3 sensory does NOT fix

The `sensory:3 @17` entry in its current form still has the unanchored old-state problem. V3 provides:
- A way for the short-chapter modality-floor + sparsity-ceiling to coexist (resolves the arithmetic).
- A process rule that would prevent the cycle-3 fixer-ADD failure mode going forward.

The actual fix for `sensory:3 @17` (still required to clear the old-state-reader HARD) is one of: (a) add a sound-baseline studio note to loc-state:2 @3 establishing Hook exterior street-sound as "street-quiet" in the afternoon approach; (b) revise the sensory entry's old-state to trace to what loc-state:2 actually establishes; (c) revise the old-state away from time-of-day-stamped form. Option (a) is what the old-state-reader specialist named as the simplest fix. This is a chapter-level repair, not a rubric question.

---

## Memory cap-burn — one root cause (one carve-out)

### Cap-burn evidence

`active-project/staff/audience/cape-fic-reader/memory-r2-verdict.md` — verdict: revise.
`active-project/staff/audience/dark-fantasy-reader/memory-r2-verdict.md` — verdict: revise.

Both reviewers converged on the same finding: `mem:1 @9` carries the Earth-Bet displacement register the doubled-register file-level shape requires, but narrator-interest is silent at @9 because the substance-hinge of this chapter is **somatic, not narrated**. The body holds, the prohibition enacts, the architecture is the shape Taylor will not build. The substance lives in `feel:1 @9` ("she sets her weight even on both feet") rather than narrator-interest.

Three remediation paths blocked under V2:
1. Cull `mem:1 @9` → file goes single-register (only Westerosi clamp at mem:2 @18); file-level doubled-register shape fails.
2. Add narrator-interest at @9 → NI density rises from 22.2% to 25.9%, breaching the 25% ceiling.
3. Rubric-authority ruling on feel-as-spine equivalence → documented as the "preferred resolution" but never materialized; V2 has no escalation phase.

Result: cap-burn at cycle-2.

### V3 fix — feel-as-spine equivalence for held-discipline scenes

**Problem:** the memory rubric V2 mandates narrator-interest co-citation on the same anchor. The mandate doesn't account for held-discipline scenes (`dramatic_shape: hinge` chapters where the stakes axis is in `axes_held[]`) — those scenes have substance that lives in feeling rather than narrator-interest by construction. The interior is **held**, not reaching forward; narrator-interest fires sparsely; feeling carries the somatic load. Under V2, monument entries on these beats fail the spine requirement because the rubric doesn't recognize feel as a valid spine.

**Fix:** new feel-as-spine equivalence carve-out on the Licensing-discipline axis's Narrator-interest co-citation ACCEPT signature. When ALL FOUR conditions hold —
1. Chapter `dramatic_shape: hinge`
2. Scene's `scene_conflict.stakes_axis` is in scene's `axes_held[]` (per the 2026-05-21 axis-bookkeeping split)
3. Feel-flag fires on the same `@<proto-line-id>`
4. Every other discipline gate clears (displacement-cue, audience-meaningfulness, functional-register, multi-justification, per-scene cap)

— the memory-flag may co-cite the feel-flag as spine in place of narrator-interest. The carve-out replaces ONLY the spine; every other gate still applies unchanged.

The corresponding REJECT signature ("Missing spine") was updated to reject only when NEITHER narrator-interest is fired NOR the V3 carve-out conditions all hold. The Cross-axis test ("The narrator-interest spine test"), the anti-pattern #7 ("Spineless fire"), and the Ceiling defense protocol were all updated for consistency.

**URI:** URI-FACETS-V3-FEEL-AS-SPINE.

### Compatibility with the axis-bookkeeping split

The V3 carve-out is structurally dependent on the `axes_held[]` schema element shipped the same day. Without `axes_held[]`, condition (2) — "scene's `stakes_axis` is in `axes_held[]`" — would not be mechanically checkable. The two changes are co-deployed: held-discipline scenes are exactly the `axes_held[]` scenes the new schema makes explicit, and the V3 memory rubric is the first downstream consumer of the split.

### Re-audit of `mem:1 @9` under V3

Walking the four carve-out conditions against the existing entry:

| condition | check | result |
|---|---|---|
| 1. `dramatic_shape: hinge` | `chapters[b01c01].dramatic_shape` = `hinge` | ✓ |
| 2. `stakes_axis` in `axes_held[]` | s01 `stakes_axis: capability`; s01 `axes_held: [{axis: capability, …}]` | ✓ |
| 3. feel-flag on same anchor | `active-project/theater/facets/feeling.md` `1 @9 …she sets her weight even on both feet` | ✓ |
| 4. other gates clear | displacement-cue ("the feet hold and the architecture stays the shape she will not build"), audience-meaningfulness, functional-register (moment of realization + painting characterization), multi-justification, per-scene cap (1 entry in s01) — all clear under V2 | ✓ |

The entry would have passed the V3 carve-out. The b01c01 cap-burn is V3-resolvable retroactively; the file's doubled-register coverage is restored without culling `mem:1 @9`.

---

## What V3 ships

```
design/shoot-v2/rubric-sensory.md         — V3 locked 2026-05-21
  + Status header: V3 locked
  + V3 changes summary section
  + Curve-shape / Episode-level / Short-chapter floor-vs-ceiling exemption clause
  + Anti-pattern #14: Cycle-N ADD without pre-validation

design/shoot-v2/rubric-memory-flags.md    — V3 locked 2026-05-21
  + Status header: V3 locked
  + V3 changes summary section
  + Licensing-discipline / Narrator-interest co-citation ACCEPT — feel-as-spine carve-out
  + Licensing-discipline / Missing spine REJECT — updated for carve-out
  + Cross-axis test "The narrator-interest spine test" — updated for carve-out
  + Anti-pattern #7 "Spineless fire" — updated for carve-out
  + Ceiling defense protocol — updated for carve-out

design/shoot-v2/sensory-memory-v3-tuning-summary.md  — this file
```

No command body or schema changes ship with V3 — the rubric edits are sufficient because the auditor's RUBRIC-FIDELITY class enumerates REJECT / anti-pattern / cross-facet sections at audit time (per CLAUDE.md rule 11). The next `/and-facets` run will pick up the V3 rules automatically.

---

## Open items (not part of V3)

- **`/and-facets` cycle-N ADD pre-validation enforcement** (F1 / A3 in the parent followup) — the rubric anti-pattern #14 documents the rule, but the command-body Phase 5b iteration logic still needs the structural change (either ban late-cycle ADDs or audience-validate them in-cycle). Rubric edit alone doesn't prevent the failure mode at orchestration time; it only flags the pattern at audit time.
- **`sensory:3 @17` chapter-level repair** — V3 doesn't fix the unanchored old-state; a chapter-level loc-state edit is still needed before the file ships clean. The V3 cycle-N-ADD anti-pattern is the rule that would have caught this at pre-add time.
- **Re-audit of all 10 facet files under V3** — the other 10 facets (which passed V2) need a re-audit under V3 to confirm no V3 change introduces a regression elsewhere. Expected to be a no-op (V3 only relaxes constraints; no V2 PASS should become V3 FAIL).
- **Audience-gate cycle-1 validation of V3 carve-outs** — the next `/and-facets` run on b01c02 is where V3 actually gets exercised in the audience-gate loop. The cycle-1 verdicts will be the first real test of whether the V3 rules close the cap-burn cases without opening new ones.
