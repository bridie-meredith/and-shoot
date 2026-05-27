---
reviewer: worm-canon-pedant
facet: state-updates
chapter: b01c04
phase: 5b-adversarial
cycle: 3
mode: facet-adversarial (URI-AUDIENCE-AGGREGATION-RULE; single-reviewer verdict; any revise or fail blocks)
timestamp: 2026-05-27
prior-verdict: revise (cycle-1)
---

# state-updates — cycle-3 re-review (b01c04)

*[re-walk only. Five callouts from cycle-1. DEC-0035 lists the fixes. I verify each fix, then give a verdict. I am not re-reading the whole file — the clean entries passed cycle-1 and I have no new reason to touch them.]*

---

## Re-walk: callout by callout

---

### Callout 1 — state:6 anchor lag (@26 → @25)

**Cycle-1 finding:** studio.active_location fired at @26 (actor-entry bone) instead of @25 (scene-open env-frame; loc-state:4 co-fires here). One-bone lag, anti-pattern #7.

**Stated fix:** anchor moved @26 → @25.

**Verification:**

State-updates.md (env slice), entry 6:
```
6 @25 studio.active_location: oc-pig-tallow-lane → oc-ropers-court
```

Cite-index:
```
state:6 @25 back=Y co=[loc-state:4, sensory:3, state:5]
```

Proto-line @25:
```
25 the early-morning grey empties Roper's Court [loc-state:4] [sensory:3] [state:5] [state:6]
```

The anchor is now @25. Co-citations with loc-state:4 and sensory:3 confirmed — the env-frame entries land on the same beat. state:5 (time_of_day flip) also @25; the two env-frame entries co-fire. Back=Y in cite-index confirmed — proto-line @25 carries [state:6]. The one-bone contradiction window is closed.

The old @26 entry is gone. The cite-index no longer shows a @26 entry for state:6. Proto-line @26 ("taylor-hebert-kl-122ac enters Roper's Court") carries no state citations — correct; it is now bare at this field. The strip-test: at @25, studio.active_location record was oc-pig-tallow-lane; the proto-line establishes Roper's Court; the entry fires; the field is now oc-ropers-court from @25 forward through @28. Then state:8 @29 fires the next transition (oc-ropers-court → oc-cooper-yard-eel-alley) when Jarvis enters the yard scene.

**Fix verified. Callout 1 closed.**

---

### Callout 2 — state:7 non-canonical value form ("four-ward-complete" descriptor)

**Cycle-1 finding:** coverage_active_range <new> value "four-ward-complete" breaks the zone-set format established by states:3 and :4. Showrunner write-back carries a label, not a parseable zone-set; b01c05 cannot chain from it.

**Stated fix:** value changed to slug-list (zone-set format).

**Verification:**

State-updates.md (env slice), entry 7:
```
7 @27 studio.coverage_active_range: oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane → oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane + oc-ropers-court # field-extension
```

The descriptor "four-ward-complete" is gone. The new value is an explicit zone-set: oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane + oc-ropers-court. Format is consistent with states:3 and :4. Chain-correctness check: state:4 established oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane as the <new> value; state:7's <old> matches exactly. The fourth zone (oc-ropers-court) is added, consistent with Taylor extending to Roper's Court at @27 per proto-line 27 ("taylor-hebert-kl-122ac extends the insect-range"). The showrunner write-back now receives a concrete zone-set the b01c05 author can chain from directly.

**Fix verified. Callout 2 closed.**

---

### Callout 3 — state:8 + state:9 identical duplicate

**Cycle-1 finding:** Two identical entries at @29: studio.actors_in_yard: [] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]. One-field-one-resolution-per-beat rule violated. Recommended decomposition: [] → [taylor-hebert-kl-122ac] and [taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier].

**Stated fix (DEC-0035):** state:9 old-state changed [] → [taylor].

Wait — let me read this carefully. The DEC-0035 fix is narrower than my recommendation. My recommendation was full incremental decomposition with potentially separate anchor beats. The fix changes only the <old> value of state:9 from [] to [taylor-hebert-kl-122ac], keeping both entries at @29.

**Verification:**

State-updates.md (env slice):
```
8 @29 studio.active_location: oc-ropers-court → oc-cooper-yard-eel-alley
9 @29 studio.actors_in_yard: [taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]
```

Hold on. Entry 8 here is not studio.actors_in_yard — it is studio.active_location: oc-ropers-court → oc-cooper-yard-eel-alley. The numbering has shifted. The former state:8 (actors_in_yard duplicate) has been renumbered or reorganized. Let me re-read the env slice top-to-bottom with the new numbering:

```
1 @1   studio.time_of_day
2 @13  studio.active_location: eel-alley → pig-tallow-lane
3 @15  studio.coverage_active_range (hook → hook+pig-tallow)
4 @22  studio.coverage_active_range (hook+pig-tallow → hook+pig-tallow+stitch-house)
5 @25  studio.time_of_day (day-2)
6 @25  studio.active_location (pig-tallow → ropers-court)
7 @27  studio.coverage_active_range (three zones → four zones)
8 @29  studio.active_location: oc-ropers-court → oc-cooper-yard-eel-alley
9 @29  studio.actors_in_yard: [taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]
```

There is now a studio.active_location entry at @29 (entry 8). That is a new entry — it was not in the cycle-1 file. In cycle-1, the @29 beat had two studio.actors_in_yard entries (old states:8 and :9). Now it has one studio.active_location entry and one studio.actors_in_yard entry.

Let me verify what happened: the old duplicate pair (both studio.actors_in_yard: [] → [taylor, jarvis]) has been replaced. The actors_in_yard entry (now numbered 9) has its <old> changed to [taylor-hebert-kl-122ac]. But where is the [] → [taylor-hebert-kl-122ac] entry? That would be the first incremental step.

Looking at the sequence: Taylor enters the yard earlier in the chapter (she's there throughout scene-B and scene-C). The studio.actors_in_yard field at chapter open would track Taylor's presence. There is no entry recording Taylor entering the yard — her presence in the yard appears to be the baseline state for scene-A and after. Jarvis enters the yard at @29. So the correct reading is: prior to @29, actors_in_yard = [taylor-hebert-kl-122ac] (Taylor was already in the yard from scene-A). At @29, Jarvis enters → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier].

That is coherent: state:9 with <old> = [taylor-hebert-kl-122ac] is the correct incremental form. The [] → [taylor] step is not needed because Taylor's presence in the yard was never an empty-to-Taylor transition in this episode's bones — she's there from @3 onward. The old-state [] was wrong; [taylor-hebert-kl-122ac] is the correct canonical baseline at @29.

Now state:8 @29 studio.active_location: oc-ropers-court → oc-cooper-yard-eel-alley. This entry is new relative to cycle-1. In cycle-1, I noted that the scene-C-to-yard-return location transition needed tracking. The @25 entry moves active_location to oc-ropers-court. At @29, Jarvis enters the yard — but proto-line @29 is "jarvis-coin-kl-courier enters the cooper's yard." This implies the active_location shifts back to oc-cooper-yard-eel-alley at @29. The entry is anchored correctly on the bone where the transition fires.

But wait: was this location transition present in cycle-1? In cycle-1 I counted 14 env entries. Let me recount the current env slice: 14 entries (1–14). Same count. The renumbering within the env slice means one of the former entries was replaced, not added. The cycle-1 file's old state:8 and state:9 were both studio.actors_in_yard: [] → [taylor, jarvis]. The current state:8 is studio.active_location @29 (new content) and state:9 is studio.actors_in_yard with corrected <old>. So the dedup fix replaced one of the two identical actors_in_yard entries with the location transition that was apparently missing.

This is correct behavior. The duplicate was removed, the <old> value on the surviving actors_in_yard entry was fixed to the canonical prior state, and the location transition that belongs at @29 was added in the freed slot. Entry count holds at 14 per the carve-out.

Cross-check: state:12 @36 chains from state:9. studio.actors_in_yard: [taylor-hebert-kl-122ac, jarvis-coin-kl-courier] → [taylor-hebert-kl-122ac]. The <old> of state:12 matches the <new> of state:9. Chain holds.

The cite-index confirms:
```
state:8 @29 back=Y co=[loc-state:5, state:4, state:5, state:9]
state:9 @29 back=Y co=[loc-state:5, state:4, state:5, state:8]
```

Both at @29, co-citing each other and the loc-state:5 cluster. Proto-line @29 now carries [loc-state:5] [state:4] [state:5] [state:8] [state:9] — consistent with the cite-index.

**Fix verified. Callout 3 closed.** The decomposition approach differs from my recommended form (I said separate anchor beats; the fix instead uses the correct canonical <old> at a single beat), but that difference is correct — Taylor was already in the yard; there was no [] → [taylor] transition to record. The fix is precise.

---

### Callout 4 — state:14 narrative label as <new> value

**Cycle-1 finding:** studio.active_location <new> value "chapter-close-stitch-house-lane-exit" is a narrative event label, not a location slug. Canonical write-back sets b01c05 baseline to this non-slug value.

**Stated fix:** value changed to oc-stitch-house-lane.

**Verification:**

State-updates.md (env slice), entry 14:
```
14 @39 studio.active_location: oc-cooper-yard-eel-alley → oc-stitch-house-lane
```

The narrative label is gone. The <new> value is oc-stitch-house-lane — a location slug consistent with the format of all other active_location entries in this file. Back=Y confirmed in cite-index (state:14 @39). Proto-line @39 ("taylor-hebert-kl-122ac exits the stitch-house lane [feel:2] [loc-state:6] [state:14]") carries the citation.

Chain from state:8 @29 (oc-ropers-court → oc-cooper-yard-eel-alley): the intermediate location is oc-cooper-yard-eel-alley; state:14's <old> = oc-cooper-yard-eel-alley. Chain is unbroken.

The showrunner write-back now receives oc-stitch-house-lane as the terminal active_location for b01c04. A b01c05 author chaining from this field gets a parseable slug.

**Fix verified. Callout 4 closed.**

---

### Callout 5 — state:16 + state:22 undeclared field-extensions (Jarvis slice)

**Cycle-1 finding:** actor:jarvis-coin-kl-courier.stats.active_deliveries and .stats.exposure_risk used without field-extension declarations in the Jarvis slice preamble (which declared no extensions in cycle-1). Anti-pattern #6 risk if fields not on Jarvis's state.md schema.

**Stated fix (DEC-0035):** Jarvis slice preamble added with field-extension declarations for active_deliveries + exposure_risk.

**Verification:**

The state-updates.md Jarvis slice preamble (lines 68–82 in the consolidated file):

```
# rubric-carve-out — none; baseline V2 rubric § actor-state applies.
#
# Field-extensions (per §"Field-extension protocol" of rubric-state-updates.md):
#   - actor:jarvis-coin-kl-courier.stats.active_deliveries (new) — integer counter tracking live
#       delivery assignments in-progress; operational load indicator; not a standard actor-state
#       field on jarvis-coin-kl-courier's state.md baseline; field-extension justified as a
#       tracked-state-aspect (irreversible increment at each accept-delivery event; persistence
#       required for downstream chapter continuity); NOT perception/mood/register.
#   - actor:jarvis-coin-kl-courier.stats.exposure_risk (new) — categorical risk tier tracking
#       operational exposure level for the courier once he physically carries Taylor's intelligence;
#       field-extension justified as a tracked-state-aspect (latent → operational flip is an
#       irreversible canonical state change that chapter handoff_out must propagate); NOT perception/
#       mood/register.
#   Both field-extensions are propagated by chapter handoff_out (memory.md chapters[b01c04].
#   handoff_out.character_state / open_threads) per the standard field-extension protocol.
```

Both fields are now declared. Each declaration names the field as new, confirms it is not on the baseline state.md schema, and provides the rubric justification: tracked-state-aspect (not perception/mood/register), persistence-required, propagated by handoff_out.

The rubric §"Field-extension protocol" requires: (1) documented inline, (2) tracked-state aspect not perception or stylistic flourish, (3) defensible under the Reality axis. All three conditions are met by the preamble text.

The standalone file (state-updates-jarvis-coin-kl-courier.md) carries the same preamble. The consolidated file reproduces it. The declarations are present in both.

active_deliveries as a tracked-state-aspect: an integer counter that increments at accept-delivery events. Irreversibility holds — each accepted delivery is a committed operational obligation; the count cannot decrement without a delivery-completion or cancellation event (neither of which fires in b01c04). Persistence past the beat: yes, the count remains at 1 through the chapter close.

exposure_risk latent → operational: the categorical flip at @36 (Jarvis exits carrying Taylor's intelligence). This is an irreversible operational-exposure crossing. Once Jarvis physically carries the report, the exposure is real — there is no un-carrying event in b01c04. The latent → operational value form is categorical and parseable. The field name is precise for what it tracks.

Both fields pass the field-extension protocol. The CONDITIONAL rating from cycle-1 can now be resolved.

**Fix verified. Callout 5 closed.**

The state-updates-jarvis-coin-kl-courier.md standalone file carries the same preamble text as the consolidated file. I verified both. Consistent.

---

## Residual checks

**New entry at state:8 @29 (studio.active_location: oc-ropers-court → oc-cooper-yard-eel-alley):** This was added during the callout-3 fix process (replacing one of the two duplicate actors_in_yard entries). I check it independently since it was not in the cycle-1 file.

- Reality: the scene returns to the cooper's yard at @29 (Jarvis enters the yard; proto-line @29 is "jarvis-coin-kl-courier enters the cooper's yard"). The active_location field should transition from oc-ropers-court (scene-C) to oc-cooper-yard-eel-alley. That tracks — the yard scene and Roper's Court are different locations; scene-C ends and the yard meeting begins at @29.
- Authority: studio. Correct.
- Frugality: <old> = oc-ropers-court, which is state:6's <new> at @25. Chain from @25 through @28 (four bones of Roper's Court coverage work). No intermediate active_location entry in the gap. Chain is unbroken.
- Persistence: oc-cooper-yard-eel-alley persists from @29 through state:14 at @39 (terminal entry). Cross-check with state:14 <old> = oc-cooper-yard-eel-alley — confirmed.

New entry: CORRECT.

**state:30 @31 (actor:taylor-hebert-kl-122ac.knowledge.wren-report-inclusion: na → excluded):** Added in cycle-3 per DEC-0035 (decomposition of the former compound value present-but-outside-report). Not in my cycle-1 callouts; not in scope of this re-walk. I note it exists and passes the back=Y cite-check (cite-index: state:30 @31 back=Y). The decomposition (wren-in-coverage-map tracks presence fact; wren-report-inclusion tracks decision fact) is structurally clean — two separable canonical facts, two entries. No concern.

**Proto-line @26 is now bare:** cycle-1 state:6 was at @26 and is now at @25. Proto-line @26 ("taylor-hebert-kl-122ac enters Roper's Court") carries no state citations. The cite-index confirms @26 is bare. That is correct — the actor-entry bone is not the state-change bone for studio.active_location. The field already flipped at @25. No fire needed at @26.

**Cite-index state:6 cross-citation:** In cycle-1 I noted the auditor's flag-001 identified a dual-anchor cite-index gap (the @27 cross-citation of state:6 not in state:6's own entry). The cite-index now shows state:6 @25 back=Y co=[loc-state:4, sensory:3, state:5]. State:7 @27 co=[narrator:13, state:6, vibes:13] — state:6 appears in state:7's co-list. That is the cross-citation the flag-001 noted. Now that state:6 is at @25, it is properly declared there; the @27 reference in state:7's co-list is a cross-facet note (state:7 builds on the field established by state:6). No contradiction.

---

## Verdict assessment

All five cycle-1 callouts have been addressed:

1. **state:6 anchor lag** — moved to @25. One-bone contradiction window closed. Cite-index back=Y confirmed.
2. **state:7 value form** — explicit zone-set replacing the descriptor. Showrunner write-back now carries a parseable chain-compatible value.
3. **state:8 + state:9 duplicate** — resolved by fixing <old> of actors_in_yard entry to canonical prior state and replacing the freed slot with the missing active_location @29 transition.
4. **state:14 narrative label** — replaced with oc-stitch-house-lane slug. Canonical format restored.
5. **state:16 + state:22 undeclared fields** — full field-extension declarations added to Jarvis slice preamble in both standalone and consolidated files. Both fields pass the tracked-state-aspect test.

No new violations introduced by the fixes. The new state:8 @29 entry is clean. The state:30 addition is in scope of DEC-0035 and structurally sound.

The Taylor NI co-citation contract verified in cycle-1 is unaffected by all cycle-3 changes. The carve-out defense for env-slice density is unchanged.

---

## VERDICT

**accept**

All five cycle-1 callouts resolved. No residual violations. The file is cleared for canonical write-back.
