# Vibes-Updates Corpus — s01e01

Gold-standard reference for what an ideal showrunner authors as `active-project/theater/facets/vibes.md` for s01e01. Used as Phase 0 corpus for Phase 1 baseline review and Phase 2 fork target.

Episode: s01e01. 77 proto-line beats. Five vibe-causing events identified.

Format: V1 schema content shape per `design/shoot-v2/rubric-vibes.md`.

---

## Eligible-event-set (5 events; ~17 expected fires)

### E1: the-machinery-arrives — officer arrives and processes census

Beats: @11-@48 (officer-arrives @11, line-formed @14-@22, taylor-engaged @23-@30, letter-handled @38-@45, dictation @47-@48).

Affected entities:
- `actor:taylor-hebert-westeros` — the target of processing
- `actor:mira-stonefield` — co-witness, experienced bystander
- `actor:edric-cray` — co-witness, tactical assessor
- `actor:census-officer` — IS the machinery
- `episode` — ambient: this episode IS the machinery arriving

Expected fires: 5.

### E2: the-letter — Osmynd's wardship letter presented and returned unchanged

Beats: @28-@45 (presentation @28-@29, examination @40-@42, return @43-@45).

Affected entities:
- `actor:taylor-hebert-westeros` — holds, presents, receives back
- `episode` — ambient: the form-that-does-not-fit

Expected fires: 2.

### E3: the-naming — taylor entered as provisional-labor-eligible

Beats: @47-@48 (officer dictates the entry).

Affected entities:
- `actor:taylor-hebert-westeros` — named into the ledger
- `episode` — ambient: the moment of being-named

Expected fires: 2.

### E4: the-septon-as-absence — septon Osmynd does not emerge from the sept

Beats: @31-@33 (officer addresses threshold @32; door stays shut @33).

Affected entities:
- `actor:taylor-hebert-westeros` — relies on, sees absence
- `actor:septon-dying-protector` — IS the absence (cannot emerge)
- `episode` — ambient: protection-cannot-arrive

Expected fires: 3.

### E5: the-yard-as-witness — taylor asks mira/edric for help; both decline

Beats: @51-@57 (taylor speaks to mira @51, mira drops eyes @52-@53, taylor speaks to edric @54, edric steps back @57).

Affected entities:
- `actor:taylor-hebert-westeros` — the asker, the unmet
- `actor:mira-stonefield` — declined by silence
- `actor:edric-cray` — declined by exit
- `episode` — ambient: the yard that held silence

Expected fires: 4.

---

## Reference fires (gold-standard)

```
facet: vibes
episode: s01e01
author: showrunner
---

1  @48 actor:taylor-hebert-westeros + the-machinery-arrives: [the-officer-as-instrument-not-enemy, forms-have-no-slot-for-her-situation, the-refusal-that-requires-no-malice, bureaucratic-weight-she-cannot-argue-with] | licensed-by: state-update:7, memory:1, proto:11

2  @11 actor:mira-stonefield + the-machinery-arrives: [the-officer-on-a-schedule-that-does-not-bend, impressment-she-has-seen-this-version-before, the-calculus-of-who-gets-taken, she-named-the-unattached-ones-because-she-knows] | licensed-by: proto:11, world-build:mira-prior-burning-cycles

3  @11 actor:edric-cray + the-machinery-arrives: [impressment-officer-he-has-seen-this-kind-of-weight, the-lord-behind-the-commission, when-to-stay-at-the-gate-and-when-to-leave, the-calculation-that-required-no-drama] | licensed-by: proto:11, feeling:3, world-build:edric-prior-impressment-encounters

4  @11 actor:census-officer + the-machinery-arrives: [efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person] | licensed-by: proto:11, proto:13, proto:21

5  @11 episode + the-machinery-arrives: [efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person] | licensed-by: state-update:7, proto:11

6  @45 actor:taylor-hebert-westeros + the-letter: [the-thing-that-wont-work-before-she-tries-it, held-at-her-side, presenting-it-anyway-because-what-else, traveling-back-to-her-unchanged, the-form-of-what-he-could-give] | licensed-by: state-update:2, state-update:3, state-update:5, proto:43

7  @45 episode + the-letter: [the-useless-object, what-he-could-give, held-at-her-side, traveling-back-unchanged, the-form-that-does-not-fit-the-rule] | licensed-by: state-update:5, proto:43

8  @48 actor:taylor-hebert-westeros + the-naming: [giving-her-name-aloud-to-a-ledger, the-moment-the-window-closes, the-irrevocable-action-she-takes-herself, she-said-it, no-going-back-in-that-specific-direction] | licensed-by: state-update:6, state-update:7, proto:48

9  @48 episode + the-naming: [the-moment-of-being-asked, the-name-given-aloud, the-dictation-as-finality, the-door-that-closes-on-its-own-momentum] | licensed-by: state-update:6, state-update:7, proto:47, proto:48

10 @33 actor:taylor-hebert-westeros + the-septon-as-absence: [what-he-could-not-give, the-closed-doors-as-answer, kindness-running-out-before-it-could-hold, the-letter-she-prepared-that-did-not-fit] | licensed-by: memory:1, proto:33

11 @33 actor:septon-dying-protector + the-septon-as-absence: [present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold] | licensed-by: proto:32, proto:33, canon:osmynd-bedridden-pre-episode

12 @33 episode + the-septon-as-absence: [present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold] | licensed-by: proto:32, proto:33

13 @57 actor:taylor-hebert-westeros + the-yard-as-witness: [mira-who-looked-at-the-stones, edric-who-stepped-back, the-yard-that-held-silence, she-asked-and-no-one-moved, this-is-what-unattached-means] | licensed-by: feeling:1, feeling:3, memory:2, proto:52, proto:57

14 @52 actor:mira-stonefield + the-yard-as-witness: [the-ask-that-came-to-her, the-yard-stones-she-looked-at, the-officer-still-present-when-she-said-nothing, the-cost-she-assessed-before-she-decided, self-preservation-in-a-hierarchical-world] | licensed-by: feeling:1, proto:51, proto:52

15 @57 actor:edric-cray + the-yard-as-witness: [the-officer-at-the-gate, the-look-he-gave-the-officer-then-taylor, the-door-he-stepped-back-through, the-math-he-ran-before-he-moved, one-exit-and-he-used-it] | licensed-by: feeling:3, state-update:9, proto:55, proto:57

16 @57 episode + the-yard-as-witness: [mira-delivering-verdict-before-it-happens, edric-watching-the-road-without-watching, what-everyone-already-knew] | licensed-by: feeling:1, feeling:3, proto:52, proto:57
```

**Total: 16 fires.**

Per-target distribution:
- actor:taylor-hebert-westeros: 5 (E1, E2, E3, E4, E5)
- actor:mira-stonefield: 2 (E1, E5)
- actor:edric-cray: 2 (E1, E5)
- actor:census-officer: 1 (E1)
- actor:septon-dying-protector: 1 (E4)
- episode: 5 (E1, E2, E3, E4, E5)

Per-event distribution: E1:5, E2:2, E3:2, E4:3, E5:4 (matches eligible-event-set forecast).

Op distribution: 16 × `+`. No `-`, no `++` (s01e01 is the project's first episode; no prior vibes to retire or extend).

Anchor distribution: 16/16 anchored to a proto-line. Zero off-screen-only entries (s01e01 is the project's first episode; canon refs supplement but anchor lives in-episode).

---

## Calibration anchors

- **C1** Entry 1 `actor:taylor +the-machinery-arrives` — multi-source-licensed (state-update + memory + proto), multi-target fan-out anchor (E1 fans across 5 targets).
- **C2** Entry 11 `actor:septon-dying-protector +the-septon-as-absence` — non-POV co-target on E4. Tests whether the showrunner remembers off-stage actor whose absence IS the event.
- **C3** Entries 14-15 `mira / edric +the-yard-as-witness` — non-POV co-targets on E5 with character-relative token-bundles (tokens reflect each witness's framing).
- **C4** Entry 9 `episode +the-naming` — episode-scope target distinct from entity targets (tests scope-stratification).

---

## Anti-pattern cases (gold-standard refusals)

The following hypothetical fires are REFUSED at gold-standard authoring; reviewer should catch them as INCORRECT-FIRE:

- **REF1** `actor:taylor +nervous` — AP1 (transient mood, not durable vibe; this is a feeling-flag candidate at most).
- **REF2** `actor:taylor +provisional-labor-eligible: [...]` — AP2 (state-restated-as-vibe; the state-updates entry already captures the fact; vibes derive consequence not restate).
- **REF3** `actor:taylor +the-letter` (no token-bundle) — gate 3 (token-bundle required for `+`).
- **REF4** `actor:taylor + the-machinery-arrives` written without `licensed-by:` — gate 4 / AP4 (unlicensed).
- **REF5** `actor:taylor +the-naming: [intense, important, meaningful]` — AP7 (vague tokens; no operator can act on these).
- **REF6** `actor:taylor +the-letter: [the-letter-was-useless-and-she-knew-it-would-not-work-before-she-tried]` — AP8 (prose token; not word-algebra; multi-clause-as-token).
- **REF7** Skipping `actor:edric` on E5 (only firing on taylor + mira + episode) — gate 7 / AP12 (fan-out coherence violated; edric is on-stage and his step-back IS part of the witness-event).
- **REF8** Two entries `actor:taylor +the-machinery-arrives` and `actor:taylor +the-machinery-arrives: [extra-tokens]` (instead of `++` for the second) — AP5 / AP10 (duplicate-add; extension should use `++`).

---

## Phase 1 baseline expectation

Showrunner with **schema-current text only** (no rubric) is expected to:
- author EITHER nothing (refuse-by-default; the schema text says "vibes are persistent biases" but offers no examples and no operator-bias framing) — anti-pattern is **silent-refusal**; OR
- author a soft fan of episode-scope-only entries with prose-style tokens, missing entity targets, missing `licensed-by:` field — typical contamination set.

V2 strict review against this rubric expects:
- low fire-rate (3-6 fires authored)
- mostly fail on gates 4 (licensed-by missing), 6 (operator-bias actionability vague), 7 (fan-out skipped), and AP8 (prose tokens)
- baseline accept rate likely 0-25%, comparable to feeling/metaphor 0% V2 baselines.

Phase 2 with rubric-aware showrunner-fork is expected to land at 14-20 entries closely matching this corpus shape, with Phase 3 seams pressing edge cases (e.g., should `loc:westerosi-smallfolk-village-common` carry one of these vibes? should the `prop:oc-letter` get its own vibe-set or only have the keyword inherited via taylor's binding?).

---

## Status

Corpus locked 2026-05-07. Used as ground truth for Phase 1 review and Phase 2 fork target.
