# Phase 2 — State-Updates Writer Output (Edric fork)

Author: dialogue-writer fork for `edric-cray`, state-update output mode.
Scope: `actor:edric-cray.*` entries only.
Inputs loaded: rubric V2 locked; locked tensometer; locked narrator-interest; proto-lines/s01e01.md; actors/edric-cray/state.md.

---

## INTENT-ID: E1

BEAT: @57 — edric steps back through the door

DECISION: FIRE

DRAFTS:
- (a) `@57 actor:edric-cray.position: in-yard-near-sept-door -> inside-sept-past-threshold`
- (b) `@57 actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)`

CHOSEN: (b)

Rationale for choice: `sublocation` is the field already present on edric's state schema (`active-project/actors/edric-cray/state.md`), so (b) cites the canonical-schema field directly without invoking a field-extension. (a) would require a `position` extension where `sublocation` already covers the same delta. Frugality + Authority both prefer (b).

ENTRY (final, schema form):

```
1 @57 actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)
```

RATIONALE:
- **Reality.** The proto-line verb ("steps back through the door") is a transition verb that mutates a tracked spatial field. Persistence holds: edric does not return to the yard for the remainder of s01e01 (no later proto-line shows him back outside; his canonical state.md already records "sept interior ... yard out of sightline"). Strip-test: without this entry, his sublocation would stay at "yard" — corrupting downstream memory. The fire is non-parasitic.
- **Authority.** `actor:edric-cray` exists in `active-project/actors/edric-cray/`. `sublocation` is on his current state.md. Author license is satisfied: this fork is the licensed writer for `actor:edric-cray.*`.
- **Frugality.** One entry, one (target, field). `<old>` matches the project-setup baseline (edric established at @8 with eyes on the road, in-yard near the cottage/sept door — first-touch on his sublocation field for s01e01). `<new>` matches the post-beat state confirmed by his canonical state.md.
- **Cross-facet contract.** Tensometer @57=2 (reversal-proximity + stakes-visibility — the social reversal is edric's retreat); the rubric's calibration anchor for @57 explicitly accepts this fire. Narrator-interest @57 fires ("the door takes the last adult cover with it") — POV-character registration of the consequence; **no co-citation requirement for non-POV actor-state per POV-restriction rule.** The door-state itself (`studio.doors_and_shutters.sept-door` / cottage-door) is studio's authority, not authored here.
- **Anti-pattern check.** Not registration-as-state (real persistent shift). Not held-against-turn (tens=2, not @39-class). Not transient-posture (persists past beat to episode close). Not compound (one field). Not invented-field (`sublocation` is on schema). Clean.

---

## Free additions (up to 2)

Considered candidates on edric's other on-screen beats — none survives the strip-test or persistence-test:

- **@8 edric holds his eyes on the road past the cart.** NONE. Anti-pattern: registration-as-state / posture-as-state. Gaze direction is registration; no persistent posture-state field flips at @8 (this is establishing-state, authored at project-setup baseline, not at a proto-line beat).
- **@55 edric looks at the officer.** NONE. Same — gaze-shift; transient; no field flips.
- **@56 edric looks at taylor.** NONE. Same — gaze-shift; immediately superseded by @57's commit-action. Firing here would be pre-empting (anti-pattern #7) and posture-as-state (#8).

No defensible free additions. Edric's footprint in s01e01 is one canonical state-shift (the @57 retreat).

---

## Final entry list

```
1 @57 actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)
```

---

## Curve check

- Total fires this batch: 1.
- Target diversity: 1 (`actor:edric-cray`). Expected — fork scope is single-actor.
- Cross-facet self-check: tensometer @57=2 carries the social-reversal annotation; rubric calibration anchor for @57 accepts this fire; narrator-interest co-citation NOT required (non-POV actor-state under POV-restriction). No anti-pattern fires. Sparsity is correct: edric is largely off-screen for s01e01 and the rubric's curve-shape note explicitly anticipates thin output for this fork.
