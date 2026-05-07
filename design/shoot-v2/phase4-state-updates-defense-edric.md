# Phase 4 — State-Updates Defense (Edric fork)

Author: dialogue-writer fork for `edric-cray`, state-update defense/revise mode.
Scope: ID-10 seam (MODERATE) on the sole entry from Phase 2.
Inputs re-verified: rubric V2 locked; phase3-state-updates-seams.md (ID-10); proto-lines @8, @54–@57; actors/edric-cray/state.md.

---

## ID-10 — @57 `actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)`

### Seam summary (Phase 3)

`<old>=yard (near sept door)` is project-setup-baseline assertion. Proto-line @8 ("edric holds his eyes on the road past the cart") is gaze-direction, not a sublocation establishment. The seam: if `yard (near sept door)` is author-inferred rather than canonical-state-grounded, `<old>` is not Frugality-clean.

### Verdict: DEFEND with minor refinement to baseline-citation language

### Defense

**1. Door identity verified — it is the sept door, not the cottage door.**

Re-read of `active-project/actors/edric-cray/state.md` confirms the canonical post-@57 sublocation:

> `sublocation: sept interior (door swung shut behind him; yard out of sightline)`

The canonical state-file names the destination as **sept interior**. The door Edric steps back through at @57 is therefore the sept door (the door whose far side is sept interior). The proto-line cluster supports this: @54 Taylor speaks across the yard to him; @55 he looks at the officer; @56 he looks at Taylor; @57 he steps back through the door — the door he steps through is the one that puts him into the sept interior recorded in state.md. No revise of door-identity required. The recommended-revise alternative (`cottage door` / `cottage-interior`) is rejected: it contradicts the canonical state-file's `sept interior` destination.

**2. `<old>` is licit under §Frugality ACCEPT first-touch baseline.**

Rubric §Frugality ACCEPT signature: "`<old>` matches the most-recent prior cited value on the same field, OR the project-setup baseline if first-touch."

@57 is first-touch on `actor:edric-cray.sublocation` for s01e01. The project-setup baseline for Edric at scene-open is presence in the yard adjacent to the sept door — established by:

- The episode's spatial frame: the registration scene plays out in the yard outside the sept; Edric is the cottage-affiliated male present at the registration encounter (mira-stonefield is also yard-side).
- Proto-line @8: while the verb is gaze-direction, gaze "on the road past the cart" places the gazer in the yard at a position with sightline to the road — i.e. yard-side, not interior. This is corroborating, not load-bearing.
- Proto-line @54: Taylor speaks **across the yard** to Edric — this confirms Edric's pre-@57 sublocation is yard-side. @54 is a stronger anchor than @8 for the `<old>` value: it is the most recent pre-@57 establishment that Edric is in the yard.
- The @57 proto-line itself ("steps **back** through the door") — the "back" particle entails a prior position on the outside of the threshold, i.e. yard-side adjacent to the sept door.

Under the rubric's first-touch baseline rule, the `<old>` does not require a separate prior state-update entry — it is satisfied by project-setup baseline grounded in scene-establishing context. The seam's pressure ("`<old>` is author-inferred") confuses "no prior state-update entry" with "no canonical grounding"; the rubric explicitly distinguishes these.

**3. Refinement of citation language (not a revise of the entry).**

To address the seam's specific concern that @8 was over-cited as the baseline anchor when @8 is gaze not sublocation, the entry's grounding is better cited to **@54 (Taylor speaks across the yard) + @57's "back" particle**, with @8 as corroborating. The entry itself is unchanged.

### Final entry (unchanged from Phase 2)

```
1 @57 actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)
```

### Anti-pattern re-check

- Not registration-as-state — door-crossing is a transition verb with persistent canonical aftermath in state.md.
- Not drift-old — `<old>` is project-setup baseline (rubric-licit for first-touch); no prior state-update on this field exists to drift from.
- Not author-inferred-without-grounding — @54 yard-citation + @57 "back" particle + state.md `<new>` corroboration triangulate the baseline.
- Not pre-emption / lagging — @57 is the verb-of-crossing beat.
- Persistence holds: state.md records `sept interior` with "yard out of sightline"; Edric does not return to yard for the remainder of s01e01.

---

## Summary

ID-10 defended. Entry unchanged. The seam's pressure on `<old>` grounding is answered by re-anchoring the baseline citation to @54 (Taylor speaks across the yard, an unambiguous yard-side placement of Edric) plus the @57 "back" particle, rather than to @8's gaze-direction; the canonical state.md confirms door-identity as the sept door, ruling out the cottage-door revise alternative.
