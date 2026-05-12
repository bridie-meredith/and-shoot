---
persona: worm-canon-pedant
facet: state-updates
episode: s01e02
round: r1
verdict: ACCEPT (with flags)
---

# Worm Canon Pedant — state-updates adversarial review

## Lens: Earth-Bet leakage / schema precedent / beat-anchor authority

I'm checking three things. First: do any field names, old-states, or new-states import Earth-Bet vocabulary that has no business in a Flea Bottom setting. Second: do the field-extensions have precedent in the actor card schemas, or are they manufactured outside the schema. Third: are the state-flips firing on the right beats per the rubric — specifically, is the beat-anchor the change-beat, not the approach beat or the aftermath.

---

## Earth-Bet leakage check

**fauna_control_radius_m / fauna_sense_status.operational_radius.**
The field name `fauna_control_radius_m` is on Taylor's state.md at project setup. The base-state schema uses "fauna_control" terminology. For canon: the power is bugs/insects/arachnids, not generic "fauna." In Worm proper the field would be something like arthropod sensorium range or bug control range. "Fauna" is a generalizing term — it includes vertebrates that Taylor absolutely cannot control. This is a schema-level vocabulary choice that was baked in at project setup, not introduced here, but I'm flagging it as an Earth-Bet precision concern. Taylor's power is specifically over insects, spiders, and similar; "fauna_control" admits too broad a class. This flag does not block the s01e02 state-update (the field exists in the schema; the update is correct against the schema), but it's a margit referral candidate for the schema itself.

**physical_condition: intact -> migraine-onset.**
"Migraine-onset" is a contemporary medical term. Taylor experiences severe headaches from overextension in the source text, but "migraine" is a clinical label that's Earth-Bet medical vocabulary rather than Flea Bottom vocabulary. Since this is an actor state-file (not prose), the label is arguably a production descriptor rather than in-world text. The state-file won't appear verbatim in prose. Marginal concern — the rubric doesn't require medieval nomenclature in state files. But if the prose renders this as "migraine" without transformation, that's an Earth-Bet leak into the Westerosi environment. Flagging for stitcher/editor attention, not a state-update fault.

**No other Earth-Bet vocabulary in field names or values.**
research_log_active, knowledge.*, vigil-state, wage-claim-state, transactional-posture — all neutral vocabulary. record_anomaly_logged uses "record" in a general sense that works in both registers. Nothing else leaks.

---

## Schema precedent check

**fauna_control_radius_m on Taylor's state.md.** Precedent: yes. The field is at `stats.fauna_control_radius_m: 300` in the state file at project setup. The @117 update (300 -> 400) is changing an existing field. No extension flag needed. The studio's parallel entry under `studio.fauna_sense_status.operational_radius` is a field-extension (new field on studio schema), but it's the environmental tracking of a canon-established power mechanic. The extension is justified.

**physical_condition on Taylor's state.md.** Precedent: yes. `stats.physical_condition: intact` at project setup. Same as above — this is a state-change on an existing field, not an extension. Clean.

**research_log_active on Taylor's state.md.** Precedent: yes. `stats.research_log_active: false` at project setup. Clean.

**record_anomaly_logged true -> phrase-isolated on oc-broken-maester.** The field `stats.record_anomaly_logged: true` exists in oc-broken-maester's state.md. The extension is a value-set widening: from boolean to ordinal. This is unusual — the entry's defense describes it as "boolean-logged-flag to documentation-sharpening ordinal." The rubric allows field-extension if the extension is a tracked-state aspect, not perception. A record's documentation granularity is a tracked state. My concern: the old-state `true` is a boolean, and the new-state `phrase-isolated` is an ordinal value in what is now treated as an ordinal sequence. This creates a schema inconsistency — the baseline value `true` is not part of the ordinal sequence being constructed. If this is an ordinal (anomaly-not-logged < true < phrase-isolated), then `true` should be renamed to something like `anomaly-noted` in the write-back, not left as the literal boolean. The entry as written has `true -> phrase-isolated` which implies `true` is the canonical prior-state label. That's a type mismatch: boolean vs. string-ordinal. This needs to be resolved in the canonical write-back — either the old-state is renamed or the extension is rejected and the entry is re-authored as a proper ordinal starting from `anomaly-noted`.

**knowledge.* fields on non-Taylor actors.** 
- `oc-tanner-elder.knowledge.taylor-placement-external-claimants: none -> tanner-family-customary-wage-claim-established` — no prior field on the elder's state.md (state.md shows `location`, `condition`, `inventory`, nothing else). This is first-touch extension. The extension defense cites "ledger-monitoring aspect of his card stats (network_depth + acceptance_mode)." That's a card-stats citation, not a state-schema citation. The state.md doesn't have a `stats:` block for the elder. So this is an extension adding a `knowledge.*` field to an actor who has no established `knowledge:` section in state.md. The field-extension protocol requires the extension to be a tracked-state aspect. I'll pass it as an implicit first-touch — knowledge fields are standard on actor schemas even when not yet populated. But the write-back should establish the `knowledge:` section in state.md, not just write a single value without a block.

**stance-on-tya-category, proximity-to-taylor, transactional-posture, wage-claim-state on oc-tanner-father.** All field-extensions on a state.md that shows only `location`, `condition`, `inventory`. All are first-touch. The extensions are defended in the file. My concern about stance-on-tya-category: the prior-state value `privately-concluded-not-tya` is not previously established anywhere. A field-extension protocol requires the old-state to be "verifiable from the most recent prior state-update on the same field, OR from project setup state if first-touch." For first-touch, the old-state is the project-setup baseline. The project-setup state.md for oc-tanner-father doesn't carry this field at all. So what is the canonical old-state? It can't be `privately-concluded-not-tya` unless the actor card established that value. This is the same concern the dark-fantasy reader flagged from a different angle. For the canon-pedant: the old-state value on a first-touch field-extension must be derivable from the actor card or prior episode state. If the card says "He is withdrawing from her" as a behavioral description, the baseline state is the behavioral description's implicit prior condition — which would be something like `not-yet-concluded` or `actively-grieving-for-tya`. The label `privately-concluded-not-tya` implies a prior inference state that has no explicit canonical anchor.

**vigil-state on oc-tanner-mother.** First-touch. Old-state `kept-for-tya` — the defense notes this is baseline "burning since Tya's death, pre-episode-1." That's an episode-0 / world-setup baseline. The vigil candle burning since Tya's death is a world-establishment fact (pre-episode). Old-state derivation: defensible if the actor card or world notes establish Tya's death and the vigil as a pre-episode fact. I'll pass this one with a notation that the card needs to cite Tya's death as a pre-episode event for the old-state to have canonical grounding.

---

## Beat-anchor authority check

State-update fires should be on the beat where the field flips, not the approach or aftermath. Rubric anti-pattern #7: pre-empting / lagging.

**fauna_control_radius_m 300 -> 400 at @117** — the proto-line is "the flies spread the autumn-density network." The defense says the network deployment @60-@76 established the radius and the perimeter walk @73 confirmed it, but the Taylor actor-state fires at @117. The studio fires at @73 (perimeter-walk confirmation). The split: @73 is when the radius exists in the world (environmental confirmation); @117 is when Taylor deploys a further spread. I'd expect the Taylor actor-state to fire at @73 alongside the studio entry — the perimeter walk is the beat where the radius is confirmed as 400m. Firing at @117 is either lagging (the radius already existed at @73) or the intent is that @117 is a second expansion beat. The proto-line text at @117 is "the flies spread the autumn-density network" — that's another spread event, not the original radius establishment. If the episode has two radius expansions (300->400 at @73, then a further extension at @117), the entry should say so. If @117 is documenting the same 300->400 transition that @73 already locked in on the studio side, then the Taylor actor-state should be at @73 with the studio entry, not @117. This is a potential lagging violation that needs clarification.

**record_anomaly_logged true -> phrase-isolated at @149** — the proto-line is "the beetles relay the phrase." The defense argues this is the beat where the maester's documentation state changes, because the phrase is articulated at @149. The approach beats @148 and @150 are "the beetles relay the rhythm." @149 is the specific phrase event between two rhythm beats. The fire at @149 is correct as the phrase-isolation beat. Not pre-empting or lagging.

**knowledge.tanner-claim informal-grief -> named-trade-stance at @22** — "oc-tanner-father steps back." The defense says @20 is the elder's response acknowledging the claim, and @22 is the father stepping back (visit concluded). Taylor's knowledge update fires at @22. But when does Taylor actually receive the information that updates her knowledge? The elder speaks to the father at @20; the father steps back at @22. Taylor's knowledge change should fire when she processes the trade-stance formalization, which most plausibly happens in the exchange at @20 (elder acknowledges) through @22 (resolution). @22 is the close of the scene. Firing at the scene-close rather than the disclosure beat is defensible as "knowledge solidifies at scene resolution." Not a flag.

**knowledge.broken-maester ambient-signal -> named-log-entry at @145** — "taylor-hebert-flea-bottom writes the entry." The write is the formalization act. The preceding @139 ("the beetles relay the register") is the detection beat. @145 is when she writes the entry into the log — the canonical shift from ambient-to-logged. Correct beat. Not pre-empting.

**oc-tanner-father.transactional-posture informal-grief-claim -> formalized-wage-claim at @100** — "oc-tanner-father speaks to taylor-hebert-flea-bottom." The speech at @100 is the formalization act per the narrator-interest co-cite. The prior approach is @97-@99 (enters junction, faces Taylor). @100 is when the formal claim is named. Correct beat.

**oc-tanner-father.wage-claim-state claim-extended -> first-payment-accepted at @107** — "oc-tanner-father takes the coins." Taking the coins is the acceptance act. Correct beat.

---

## Summary of flags

1. **Soft flag (schema vocabulary):** `fauna_control_radius_m` is a schema-level imprecision — "fauna" over-generalizes Taylor's power scope. Not a blocker for s01e02 but a margit referral candidate.

2. **Hard flag (type mismatch):** `record_anomaly_logged: true -> phrase-isolated` on oc-broken-maester. The old-state `true` is a boolean; `phrase-isolated` is a string ordinal. The write-back cannot cleanly apply this as a delta without resolving the type mismatch. Options: (a) re-author old-state as `anomaly-noted` (renaming the boolean as part of the field-extension), or (b) reject the extension and re-author as a new field `record_anomaly_detail` with old-state `none` -> `phrase-isolated`, leaving `record_anomaly_logged` boolean at `true`.

3. **Moderate flag (old-state grounding):** `actor:oc-tanner-father.stance-on-tya-category: privately-concluded-not-tya -> bodily-committed-withdrawal` — old-state value `privately-concluded-not-tya` lacks a canonical anchor in any prior state-update or project-setup baseline. If the actor card establishes this as the pre-episode behavioral state in explicit terms, the old-state is defensible. If not, this is a drift-old violation.

4. **Moderate flag (beat asymmetry):** `actor:taylor-hebert-flea-bottom.fauna_control_radius_m: 300 -> 400 at @117` when the studio fires the same conceptual transition at @73. Either both should fire at @73 (perimeter-walk confirmation), or the @117 entry is a distinct second-expansion event that should be labeled as such. As currently written, the asymmetry looks like a lagging violation.

5. **Soft flag (migraine terminology):** `physical_condition: intact -> migraine-onset` — "migraine-onset" is contemporary medical vocabulary. State-file production descriptor, not in-world text. Stitcher/editor should transform to Westerosi-register equivalent in prose.

---

## Verdict

**ACCEPT with flags.**

Flag 2 (type mismatch on record_anomaly_logged) is the only hard flag that needs resolution before canonical write-back. It cannot be applied as-is without corrupting the type of the field. All other flags are moderate or soft — they don't block the write-back but they should be addressed before the field-extensions become canonical baselines.

The anchor authority is mostly sound. The beat-fire sequence for the tanner-family arc and the maester-recognition arc is correct. The main structural concern is the fauna_control_radius split between @73 and @117, which needs to be resolved as either a sequenced two-step expansion or a single-fire (studio @73, Taylor @73 rather than @117).
