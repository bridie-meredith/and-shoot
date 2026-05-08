---
audit:
  scope: episode
  target: s01e01 / vibes-updates facet / Phase 2
  timestamp: 2026-05-07
  reviewer: mechanic-auditor
  rubric: design/shoot-v2/rubric-vibes.md (V1 LOCKED)
  phase2-output: design/shoot-v2/phase2-vibes-output.md
  corpus: design/shoot-v2/vibes-corpus.md
---

# Phase 2 Vibes-Updates Audit — s01e01

## Summary

**Accept rate: 6/11 = 54.5%.** Five entries are INCORRECT due to AP5 duplicate-add / gate-2 violations on episode-scope targets (entries 2–6). The Phase 2 fork's authoring note correctly diagnosed the actor-level pre-load problem and handled it right, but missed that `studio/vibes.md` carries an `EPISODE_1_VIBES` section with all five s01e01 keywords already loaded — making every `episode + <keyword>` fire in this file a duplicate-add. The six entries that survive are mechanically clean.

---

## Per-fire verdicts

### Entry 1 — `@33 actor:septon-dying-protector + the-septon-as-absence`

**Verdict: CORRECT**

Gate 2: `septon-dying-protector/vibes.md` carries `dying`, `protection`, `kindness`, `ward`, `the-septon-failing`, `observer-arriving`. Keyword `the-septon-as-absence` is absent. `+` is the correct op.

Token-bundle: `[present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold]` — word-algebra, no prose tokens, no AP7 vagueness, no AP8 multi-clause. PASS.

Licensed-by: `proto:32, proto:33, canon:osmynd-bedridden-pre-episode` — all sources resolve. PASS.

Gate 6 (operator-bias actionability): biases dialogue-writer fork on septon's residual scenes, behavior-pack register for the absent/cannot-act archetype. PASS.

Gate 7 (fan-out): septon is one of three E4 targets. Episode-scope is handled elsewhere in the file (entry 5 — though that entry fails; see below). Calibration anchor C2 satisfied.

---

### Entry 2 — `@11 episode + the-machinery-arrives`

**Verdict: INCORRECT-AP5 / INCORRECT-Gate2**

`active-project/staff/studio/vibes.md` carries:

```
EPISODE_1_VIBES:
  the-machinery-arrives: [efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person]
```

The episode-scope target already carries `the-machinery-arrives` with an identical token bundle. `+` violates gate 2 (keyword not absent) and AP5 (duplicate-add). Rubric §"Op coherence" requires `++` to extend an existing keyword; `+` is malformed here.

The authoring note in the Phase 2 file's header correctly identifies the actor-level pre-load problem but fails to extend that diagnosis to the episode-scope targets in `studio/vibes.md`.

---

### Entry 3 — `@45 episode + the-letter`

**Verdict: INCORRECT-AP5 / INCORRECT-Gate2**

`studio/vibes.md` carries:

```
EPISODE_1_VIBES:
  the-letter: [the-useless-object, what-he-could-give, held-at-her-side, traveling-back-unchanged, the-form-that-does-not-fit-the-rule]
```

`+` on a keyword already present in the episode-scope target. Same failure mode as entry 2.

Note: the token bundle authored here `[the-useless-object, what-he-could-give, held-at-her-side, traveling-back-unchanged, the-form-that-does-not-fit-the-rule]` is IDENTICAL to the pre-loaded bundle — this would fail AP11 (token-overlap on `++`) if re-authored as `++`. Any correction here must supply genuinely non-duplicate tokens.

---

### Entry 4 — `@48 episode + the-naming`

**Verdict: INCORRECT-AP5 / INCORRECT-Gate2**

`studio/vibes.md` carries:

```
EPISODE_1_VIBES:
  the-naming: [the-moment-of-being-asked, the-name-given-aloud, the-dictation-as-finality, the-door-that-closes-on-its-own-momentum]
```

Token bundle authored here is IDENTICAL to the pre-loaded bundle. Same failure mode. If corrected to `++`, new tokens must be genuinely non-duplicate from the existing bundle.

Calibration anchor C4 (`episode +the-naming`) is technically satisfied by the world-build pre-load in `studio/vibes.md`, not by this entry. The rubric's C4 check requires only that the episode scope carries `the-naming` — which it does, via pre-load. The entry as authored cannot satisfy C4 because it is malformed.

---

### Entry 5 — `@33 episode + the-septon-as-absence`

**Verdict: INCORRECT-AP5 / INCORRECT-Gate2**

`studio/vibes.md` carries:

```
EPISODE_1_VIBES:
  the-septon-as-absence: [present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold]
```

Token bundle is IDENTICAL to the pre-loaded bundle. Same failure mode as entries 2–4.

---

### Entry 6 — `@57 episode + the-yard-as-witness`

**Verdict: INCORRECT-AP5 / INCORRECT-Gate2**

`studio/vibes.md` carries:

```
EPISODE_1_VIBES:
  the-yard-as-witness: [mira-delivering-verdict-before-it-happens, edric-watching-the-road-without-watching, what-everyone-already-knew]
```

Token bundle authored here is IDENTICAL to the pre-loaded bundle. Same failure mode.

---

### Entry 7 — `@11 loc:westerosi-smallfolk-village-common + the-machinery-arrives`

**Verdict: CORRECT**

Gate 1 (target validity): `loc:westerosi-smallfolk-village-common` is confirmed in `cards/locations/INDEX.md`. PASS.

Gate 2: No active-project warehouse vibes file for this location. The library card carries no `VIBES:` section. Keyword is absent from target's vibe-set. `+` is the correct op. PASS.

Token-bundle: `[the-space-that-makes-smallfolk-legible, authority-day-contracted-into-two-body-lengths, the-ground-where-the-lord-collects, the-yard-that-cannot-claim-ignorance]` — word-algebra, no prose tokens, specific biases (studio environmental palette, sensory-flag selection, NI interest-pattern). PASS gates 3, 6, 7.

Licensed-by: `proto:11, proto:12, proto:13, world-build:smallfolk-common-authority-day-function` — all resolve. The `world-build:` gloss matches the location card's `Movement pattern: On authority-day` section. PASS.

Note: corpus marks this as optional; its authoring here is a quality positive (demonstrates entity-target preference per AP9).

---

### Entry 8 — `@64 actor:taylor-hebert-westeros ++ the-machinery-arrives`

**Verdict: CORRECT**

Gate 2: Taylor carries `the-machinery-arrives: [the-officer-as-instrument-not-enemy, forms-have-no-slot-for-her-situation, the-refusal-that-requires-no-malice, bureaucratic-weight-she-cannot-argue-with]`. `++` is the correct op.

Token overlap check (AP11): new tokens `[the-marks-beside-her-name-invisible-to-her, the-notation-the-machine-added-without-her-knowledge]` — no overlap with existing bundle. PASS.

Licensed-by: `state-update:10, state-update:11, proto:64` — state-updates 10 and 11 both fire at @64 (ledger annotation and Taylor's knowledge-state update). PASS.

Gate 6: biases dialogue-writer on Taylor's post-naming register (she doesn't know the margin marks exist); NI interest-pattern on foreknowledge gap. Actionable. PASS.

---

### Entry 9 — `@74 actor:taylor-hebert-westeros ++ the-letter`

**Verdict: CORRECT**

Gate 2: Taylor carries `the-letter` with bundle `[the-thing-that-wont-work-before-she-tries-it, held-at-her-side, presenting-it-anyway-because-what-else, traveling-back-to-her-unchanged, the-form-of-what-he-could-give]`. `++` is the correct op.

Token overlap check (AP11): new tokens `[still-in-her-fist-at-the-threshold, the-object-she-carries-through-the-door]` — no overlap. PASS.

Licensed-by: `proto:49, proto:74, proto:77, state-update:12` — state-update:12 fires at @77 (Taylor's sublocation change). The anchor proto:74 is the approach beat; proto:77 is the threshold-cross. Licensing chain is coherent: the letter persists through the episode-close into the sept. PASS.

Gate 6: biases dialogue-writer and feeling fork on Taylor carrying the useless object past the threshold; metaphor-licensing context deepens. PASS.

---

### Entry 10 — `@77 actor:taylor-hebert-westeros ++ the-septon-as-absence`

**Verdict: CORRECT**

Gate 2: Taylor carries `the-septon-as-absence: [what-he-could-not-give, the-closed-doors-as-answer, kindness-running-out-before-it-could-hold, the-letter-she-prepared-that-did-not-fit]`. `++` correct op.

Token overlap check (AP11): new tokens `[the-door-she-can-open-after-the-machine-leaves, the-return-to-find-what-waits]` — no overlap with existing bundle. PASS.

Licensed-by: `state-update:12, memory:3, proto:70, proto:77` — state-update:12 exists (@77 sublocation change). Memory:3 exists (`@73 a threshold whose far side does not yield`). Proto references anchor the approach-and-enter sequence. PASS.

Gate 6: biases dialogue-writer on Taylor's post-episode register (what she finds inside the sept); behavior-pack tic on the-protector-who-cannot-act shifts from external absence to confirmed absence after threshold-cross. Actionable. PASS.

---

### Entry 11 — `@64 actor:census-officer ++ the-machinery-arrives`

**Verdict: CORRECT**

Gate 2: Census-officer carries `the-machinery-arrives: [efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person]`. `++` correct op.

Token overlap check (AP11): new tokens `[the-two-parallel-lines-as-notation-not-judgment, the-annotation-that-travels-with-her-name]` — no overlap with existing bundle. PASS.

Licensed-by: `state-update:10, proto:64` — state-update:10 exists (ledger annotation at @64). PASS.

Gate 6: biases dialogue-writer fork on census officer's post-exit register (she does not know she added something load-bearing); NI interest-pattern on the gap between officer's function and Taylor's consequence. PASS.

Note: this is the most specific and well-calibrated `++` extension in the file — the officer-as-unknowing-mechanism framing is precisely the qualitative-consequence layer the rubric requires.

---

## Per-skip verdicts

### Fan-out completeness check against rubric gate 7

**E1 (the-machinery-arrives) fan-out — affected: taylor, mira, edric, census-officer, episode**

- `actor:taylor ++ the-machinery-arrives` — authored (entry 8). PRESENT.
- `actor:mira + the-machinery-arrives` — pre-loaded in `mira/vibes.md`. Not re-fired (correct; `+` would be AP5). No `++` extension authored. See SKIP-MISSED analysis below.
- `actor:edric + the-machinery-arrives` — pre-loaded in `edric/vibes.md`. Not re-fired (correct). No `++` extension authored. See SKIP-MISSED analysis below.
- `actor:census-officer ++ the-machinery-arrives` — authored (entry 11). PRESENT.
- `episode + the-machinery-arrives` — authored (entry 2) but INCORRECT (AP5). The episode-scope vibe IS pre-loaded; if s01e01 on-screen beats add non-duplicate tokens, a `++ extension` was required here, not a `+`. The entry as authored fails; no valid `++` replacement was supplied.

**E2 (the-letter) fan-out — affected: taylor, episode**

- `actor:taylor ++ the-letter` — authored (entry 9). PRESENT.
- `episode + the-letter` — authored (entry 3) but INCORRECT (AP5). Valid `++` replacement not supplied.

**E3 (the-naming) fan-out — affected: taylor, episode**

- `actor:taylor + the-naming` or `++ the-naming` — SKIPPED. Taylor's vibes.md carries `the-naming: [giving-her-name-aloud-to-a-ledger, the-moment-the-window-closes, the-irrevocable-action-she-takes-herself, she-said-it, no-going-back-in-that-specific-direction]`. The pre-load bundle is dense and covers the event's qualitative-consequence layer. Whether s01e01 on-screen beats add genuinely non-duplicate tokens is the deciding question. State-update:7 fires at @48 (administrative-status change), which is the primary canonical anchor. The existing bundle already encodes `the-irrevocable-action-she-takes-herself` and `no-going-back-in-that-specific-direction`. A `++ extension` with non-duplicate tokens is plausible (e.g., the form-compliance angle) but not certain. **SKIP-MISSED: flag-level.** The rubric does not require `++` where the existing bundle already covers the event; it requires that no genuinely non-duplicate tokens are omitted. This is a Phase 3 seam question.
- `episode + the-naming` — authored (entry 4) but INCORRECT (AP5). Valid `++` replacement not supplied.

**E4 (the-septon-as-absence) fan-out — affected: taylor, septon-dying-protector, episode**

- `actor:taylor ++ the-septon-as-absence` — authored (entry 10). PRESENT.
- `actor:septon-dying-protector + the-septon-as-absence` — authored (entry 1). PRESENT.
- `episode + the-septon-as-absence` — authored (entry 5) but INCORRECT (AP5). Valid `++` replacement not supplied.

**E5 (the-yard-as-witness) fan-out — affected: taylor, mira, edric, episode**

- `actor:taylor + the-yard-as-witness` or `++ the-yard-as-witness` — SKIPPED. Taylor's vibes.md carries `the-yard-as-witness: [mira-who-looked-at-the-stones, edric-who-stepped-back, the-yard-that-held-silence, she-asked-and-no-one-moved, this-is-what-unattached-means]`. Pre-load bundle is dense and event-specific. No `++` extension authored. SKIP-MISSED: flag-level (same reasoning as E3 above — pre-load may cover it).
- `actor:mira + the-yard-as-witness` or `++ the-yard-as-witness` — pre-loaded. No `++` authored. Flag-level (see below).
- `actor:edric + the-yard-as-witness` — pre-loaded. No `++` authored. Flag-level.
- `episode + the-yard-as-witness` — authored (entry 6) but INCORRECT (AP5). Valid `++` replacement not supplied.

### Co-witness `++` extensions (mira, edric)

The Phase 2 fork did not author `++` extensions for mira or edric on any pre-loaded keyword. Both actors' pre-loaded bundles for `the-machinery-arrives` and `the-yard-as-witness` are event-complete: mira's `[the-ask-that-came-to-her, the-yard-stones-she-looked-at, the-officer-still-present-when-she-said-nothing, the-cost-she-assessed-before-she-decided, self-preservation-in-a-hierarchical-world]` covers the full E5 qualitative range. Edric's bundles are similarly complete.

**Verdict: SKIP-MISSED at flag level, not fault.** The rubric does not mandate `++` extensions where the existing bundle already fully encodes the licensing event's qualitative-consequence range. The Phase 2 fork's decision to skip `++` on mira/edric is defensible. Phase 3 seam should pressure-test whether state-update:8 (edric sublocation change at @57, confirmed exit) adds a non-duplicate token to edric's `the-yard-as-witness` bundle. Currently edric's bundle ends with `one-exit-and-he-used-it` — this covers the state-update. No novel token.

### Entity targets with empty vibe-set

`loc:westerosi-smallfolk-village-common` — correctly targeted by entry 7 (CORRECT). No other location or prop entity has an empty vibe-set that the rubric's fan-out logic would require.

`prop:oc-letter` — not targeted. The corpus marks this as optional. No card currently exists (margit referral outstanding from state-updates audit). Since there is no active-project prop vibe file to check for pre-load, and the prop card is not yet authored, absence is not a fault — it is contingent on margit referral resolution.

---

## File-shape verdict

**SHAPE-FAIL (partial)**

The file header correctly identifies the structural authoring problem (world-build pre-load forces `++` ops) and the `@<proto-line-id>` anchor format is correctly applied. Required `---` metadata block is present and complete.

However: the five INCORRECT entries (2–6) have malformed op fields (`+` where `++` was required or where no entry was warranted). These entries fail gate 2 and AP5. The file as authored is not a valid Phase 2 output — it requires revision of entries 2–6 before Phase 3 seam testing.

The six CORRECT entries (1, 7, 8, 9, 10, 11) are individually shape-compliant.

---

## Rubric findings (Phase 4 candidates)

### RF-001 — World-build pre-load vs in-episode license-event tension (load-bearing)

**Finding:** The V1 rubric describes `++` as requiring "keyword present; new tokens must not duplicate existing tokens" (gate 2), and AP5 prohibits `+` when the keyword is already present. But the rubric's Phase 0 corpus was authored assuming `+` fires across all affected entities, including episode-scope, on the premise that s01e01 is the first episode and no vibes exist yet. The rubric does NOT account for the fact that `studio/vibes.md` is populated at world-build / project-activation time with `EPISODE_1_VIBES`, `SEASON_1_VIBES`, and `SERIES_VIBES` sections — meaning the episode-scope target carries keywords BEFORE the episode-authoring pass.

**The fork's reading (extend pre-loaded entity keywords with `++`)** is the correct rubric-coherent behavior for actor-level targets, but was not extended to episode-scope targets (where the same pre-load applies).

**The rubric ambiguity:** the rubric does not specify what the showrunner does when the episode-scope keyword is pre-loaded with a complete token bundle and the s01e01 on-screen beats add no genuinely non-duplicate tokens. There are three possible interpretations:
1. `++` extension with non-duplicate tokens (if the on-screen beat adds anything new to the semantic range).
2. No entry required (the pre-load already licenses the vibe; in-episode authoring only adds genuinely new tokens).
3. Fresh `+` add regardless of pre-load, treating the episode-scope targets as distinct from the actor-scope targets (i.e., the world-build pre-load is a planning artifact, not a vibe-authoring event, and the in-episode authoring reinstates it with on-screen licensing). This is the reading the Phase 2 fork implicitly took, but it conflicts with gate 2.

**Recommendation for Phase 4:** the rubric should explicitly address world-build pre-load on episode/season/series scope targets. The most rubric-coherent resolution: interpretation 2 (no entry required if pre-loaded bundle already covers the event's qualitative-consequence range; `++` required only when on-screen beats add genuinely non-duplicate tokens). This reading is consistent with gate 2 as written, preserves AP5, and removes the expectation that episode-scope keywords are always re-fired per episode. The Phase 2 fork should have checked `studio/vibes.md` before firing `episode +` entries, exactly as it checked `actors/*/vibes.md`.

---

## Findings

```yaml
findings:
  - id: fault-001
    type: fault
    what: entry 2 — "episode + the-machinery-arrives" with token bundle identical to studio/vibes.md EPISODE_1_VIBES pre-load
    why: AP5 duplicate-add / gate-2 violation; episode-scope target already carries this keyword; `+` is malformed; if on-screen beats add non-duplicate tokens a `++` extension is required; if they do not, no entry is warranted
    criteria: entry 2 must be revised to either (a) a valid `++` extension supplying genuinely non-duplicate tokens licensed by s01e01 on-screen beats, or (b) deleted if the existing pre-loaded bundle already covers the event's full qualitative-consequence range

  - id: fault-002
    type: fault
    what: entry 3 — "episode + the-letter" with token bundle identical to studio/vibes.md EPISODE_1_VIBES pre-load
    why: same failure mode as fault-001; additionally the authored token bundle is token-for-token identical to the pre-load, so a `++` replacement would itself fail AP11 unless genuinely new tokens are found
    criteria: entry 3 must be revised to a valid `++` extension with non-duplicate tokens or deleted; if revised to `++`, new tokens must not duplicate the pre-loaded bundle `[the-useless-object, what-he-could-give, held-at-her-side, traveling-back-unchanged, the-form-that-does-not-fit-the-rule]`

  - id: fault-003
    type: fault
    what: entry 4 — "episode + the-naming" with token bundle identical to studio/vibes.md EPISODE_1_VIBES pre-load
    why: same failure mode as fault-001; token bundle is token-for-token identical to the pre-load
    criteria: entry 4 must be revised to a valid `++` extension with non-duplicate tokens or deleted; the distinction between the world-build pre-load (planning-register) and the in-episode fire (on-screen-licensed) may warrant a `++` extension adding, e.g., the on-screen event's specific anchoring detail, but only if genuinely non-duplicate

  - id: fault-004
    type: fault
    what: entry 5 — "episode + the-septon-as-absence" with token bundle identical to studio/vibes.md EPISODE_1_VIBES pre-load
    why: same failure mode as fault-001; token bundle is token-for-token identical to the pre-load
    criteria: same as fault-001 criteria; note that entry 1 (septon-dying-protector entity target) is unaffected — only the episode-scope fire is malformed

  - id: fault-005
    type: fault
    what: entry 6 — "episode + the-yard-as-witness" with token bundle identical to studio/vibes.md EPISODE_1_VIBES pre-load
    why: same failure mode as fault-001; token bundle is token-for-token identical to the pre-load
    criteria: same as fault-001 criteria

  - id: flag-001
    type: flag
    what: taylor's `the-naming` and `the-yard-as-witness` keywords — no `++` extension authored in Phase 2
    why: the-naming is anchored by state-update:7 (administrative-status change, load-bearing); the-yard-as-witness is anchored by feeling:1, memory:2; both events may yield non-duplicate tokens for taylor's bundles that would deepen downstream operator bias; Phase 3 seam should test whether the pre-loaded bundles are already complete
    criteria: n/a (flag); Phase 3 seam should surface whether either keyword warrants a `++` extension with non-duplicate, genuinely episode-grounded tokens

  - id: flag-002
    type: flag
    what: mira and edric — no `++` extensions authored on any pre-loaded keyword
    why: both actors have pre-loaded bundles for `the-machinery-arrives` and `the-yard-as-witness`; the Phase 2 fork skipped these on the grounds that the pre-load bundles are complete; this is defensible but should be pressure-tested at Phase 3 seam; specifically edric's `the-yard-as-witness` and state-update:9 (his confirmed sublocation exit) may warrant a notation
    criteria: n/a (flag); Phase 3 seam question only

  - id: flag-003
    type: flag
    what: rubric V1 — gap on world-build pre-load vs in-episode episode-scope license-event handling
    why: the rubric corpus assumed all s01e01 vibes fire as fresh `+` adds; it does not address the case where `studio/vibes.md` pre-populates `EPISODE_1_VIBES` keywords at world-build; the fork correctly handled actor-level pre-load but missed the episode-scope parallel; this is a rubric ambiguity, not a fork error alone
    criteria: n/a (flag); Phase 4 rubric resolution required (see RF-001 in rubric findings section above)
```

---

## Headline metrics

| Metric | Value |
|---|---|
| Phase 2 entries authored | 11 |
| CORRECT | 6 (entries 1, 7, 8, 9, 10, 11) |
| INCORRECT-AP5/Gate2 | 5 (entries 2, 3, 4, 5, 6) |
| REFUSE-CORRECT | 0 |
| Accept rate | **6/11 = 54.5%** |
| Phase 1 baseline | 0/29 = 0% |
| Lift | +54.5pp (Phase 2 vs Phase 1) |
| Fault count | 5 (all episode-scope duplicate-adds) |
| Flag count | 3 |
| Escalation | 0 |

Expected Phase 3 seam yield (post-fault correction): ~8–12 valid entries, depending on whether episode-scope `++` extensions survive with non-duplicate tokens. The six correct entries already satisfy calibration anchors C2 (entry 1), C1 (entry 8 via pre-load + extension), C3 (pre-loaded on mira/edric, not re-fired), and C4 (pre-loaded in `studio/vibes.md` — the episode-scope `+` fix must either produce a valid `++` or confirm deletion).
