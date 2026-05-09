---
audit-type: facet-review
facet: interest-narrator
episode: s01e01
baseline: phase1-narrator-interest-baseline-naive.md
reviewer: mechanic auditor
rubric-authority: design/shoot-v2/rubric-narrator-interest.md (V2 locked)
timestamp: 2026-05-06
---

# Phase 1 Narrator-Interest Baseline Review — s01e01

---

## 0. Header Discrepancy

The baseline file header claims "60 fires, 17 skips." Actual count from file: **63 fires, 14 skips** (77 total proto-lines). The header was authored incorrectly. All review below operates on the actual file content.

- Fired beats: @1–@12, @14–@25, @27–@29, @31–@39, @41–@43, @45–@46, @48, @50, @52–@58, @60–@61, @63–@65, @67–@70, @73–@75, @77
- Skipped beats: @13, @26, @30, @40, @44, @47, @49, @51, @59, @62, @66, @71, @72, @76
- Frequency: 63/77 = **81.8%** (target band: 15–25%)

---

## 1. Headline Numbers

| Metric | Value |
|--------|-------|
| Actual fires | 63 |
| Actual skips | 14 |
| Actual frequency | 81.8% |
| Target frequency | 15–25% (12–19 entries on 77 beats) |
| V1 accept rate | 51/63 (81.0%) |
| V2 accept rate | 14/63 (22.2%) |
| V2 skip correct rate | 12/14 (85.7%) |
| V2 skip missed rate | 2/14 |
| Baseline-to-beat for Phase 2 | Target: 12–19 entries surviving; cull ~44–51 entries; rewrite survivors to V2 spec |

---

## 2. V1 Lenient Pass — Per-Entry Table

V1 criteria: form-correct (single clause, anchored, POV-restricted) AND any axis plausibly invoked at any reading. No anti-pattern check, no curve-shape, no doubled-register test.

Note on form: several entries use semicolons to chain two clauses. The rubric form spec says "single clause" and explicitly notes "No semicolon-spine." These are V1-REJECT on form.

| Entry ID | Beat (@) | tens | V1 Verdict | Reason |
|----------|----------|------|------------|--------|
| 1 | @1 | 1 | V1-ACCEPT | Form-ok; eyes-to-exits / pre-calc plausibly invoked (reading the yard before entering) |
| 2 | @2 | 1 | V1-ACCEPT | Form-ok; pre-calc / cost-tracking plausibly invoked (furled banner = operational status read) |
| 3 | @3 | 1 | V1-ACCEPT | Form-ok (em-dash as sensory spec, not spine); pre-calc plausibly invoked |
| 4 | @4 | 1 | V1-REJECT | Semicolon-spine: "the beetles in the seam are still holding; nothing under the flagstones has spooked yet" — two-clause construction; form violation |
| 5 | @5 | 1 | V1-ACCEPT | Form-ok; cost-tracking / age-mismatch plausibly invoked |
| 6 | @6 | 1 | V1-ACCEPT | Form-ok (comparative clause, not spine); cost-tracking / pre-calc plausibly invoked |
| 7 | @7 | 1 | V1-REJECT | Semicolon-spine implied by "which is the wrong direction for what mira would have said an hour ago" — actually a single relative clause; re-examine: V1-ACCEPT — single clause with relative; cost-tracking on Mira plausible |
| 8 | @8 | 1 | V1-ACCEPT | Form-ok (relative clause, not spine); pre-calc plausibly invoked |
| 9 | @9 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 10 | @10 | 1 | V1-REJECT | Semicolon-spine: "the clerk is counting bodies, not faces; the count is the thing he will write down" — two-clause |
| 11 | @11 | 1 | V1-ACCEPT | Form-ok; pre-calc / cost-tracking plausibly invoked |
| 12 | @12 | 1 | V1-ACCEPT | Form-ok (relative clause); eyes-to-exits / cost-tracking plausibly invoked |
| 14 | @14 | 1 | V1-REJECT | Semicolon-spine: "twelve feet is two of his strides and four of hers; the math is already done before her foot moves" — two-clause |
| 15 | @15 | 1 | V1-REJECT | Semicolon-spine: "the line is the funnel; entering it is committing to being read" — two-clause |
| 16 | @16 | 1 | V1-ACCEPT | Form-ok; cost-tracking on Mira plausibly invoked |
| 17 | @17 | 1 | V1-ACCEPT | Form-ok (em-dash as spec); pre-calc / eyes-to-exits plausibly invoked |
| 18 | @18 | 1 | V1-ACCEPT | Form-ok; pre-calc plausibly invoked |
| 19 | @19 | 1 | V1-REJECT | Semicolon-spine: "stopping in the line is the cheapest move available; everything from here costs more" — two-clause |
| 20 | @20 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 21 | @21 | 1 | V1-REJECT | Semicolon-spine: "each ward gets a sentence; each sentence gets a stylus-stroke" — two-clause |
| 22 | @22 | 1 | V1-ACCEPT | Form-ok (relative clause); pre-calc plausibly invoked |
| 23 | @23 | 2 | V1-ACCEPT | Form-ok; cost-tracking / eyes-to-exits plausibly invoked |
| 24 | @24 | 3 | V1-ACCEPT | Form-ok; pre-calc plausibly invoked |
| 25 | @25 | 2 | V1-ACCEPT | Form-ok (semicolon here: "face-level with a child is a posture an adult chooses; the choice is the message" — two-clause, V1-REJECT on form) |
| 27 | @27 | 1 | V1-ACCEPT | Form-ok; age-mismatch plausibly invoked |
| 28 | @28 | 2 | V1-REJECT | Semicolon-spine: "the letter goes forward at the speed she has practiced; faster would be a tell" — two-clause |
| 29 | @29 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 31 | @31 | 1 | V1-ACCEPT | Form-ok; pre-calc plausibly invoked |
| 32 | @32 | 1 | V1-ACCEPT | Form-ok (relative clause); pre-calc plausibly invoked |
| 33 | @33 | 2 | V1-ACCEPT | Form-ok; displacement-trigger / refusal-to-look plausibly invoked |
| 34 | @34 | 1 | V1-ACCEPT | Form-ok (relative clause); passive fauna-feed plausibly invoked |
| 35 | @35 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 36 | @36 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 37 | @37 | 2 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 38 | @38 | 3 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 39 | @39 | 3 | V1-REJECT | Semicolon-spine: "setting her feet where his next pace commits is the move; everything before it was setup" — two-clause |
| 41 | @41 | 1 | V1-ACCEPT | Form-ok (em-dash as spec); cost-tracking / eyes-to-exits plausibly invoked |
| 42 | @42 | 1 | V1-ACCEPT | Form-ok; pre-calc plausibly invoked |
| 43 | @43 | 2 | V1-REJECT | Semicolon-spine: "the letter coming back means it did not change the entry; it only delayed it" — two-clause |
| 45 | @45 | 1 | V1-REJECT | Semicolon-spine: "her palm closing on it is receipt; the weight in her hand is unchanged and somehow heavier" — two-clause |
| 46 | @46 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 48 | @48 | 2 | V1-ACCEPT | Form-ok (em-dash structure absent; one primary clause with subordinate); doubled-register plausibly invoked |
| 50 | @50 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 52 | @52 | 1 | V1-ACCEPT | Form-ok; cost-tracking on Mira plausibly invoked |
| 53 | @53 | 1 | V1-ACCEPT | Form-ok; cost-tracking on Mira plausibly invoked |
| 54 | @54 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 55 | @55 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 56 | @56 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 57 | @57 | 2 | V1-ACCEPT | Form-ok; pre-calc / cost-tracking plausibly invoked |
| 58 | @58 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 60 | @60 | 2 | V1-ACCEPT | Form-ok (semicolon: "his near foot angled across her is a body-fence; he has not finished with her" — two-clause, V1-REJECT on form) |
| 61 | @61 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 63 | @63 | 2 | V1-ACCEPT | Form-ok; pre-calc plausibly invoked |
| 64 | @64 | 3 | V1-ACCEPT | Form-ok; pre-calc / foreknowledge-clamp plausibly invoked |
| 65 | @65 | 1 | V1-REJECT | Semicolon-spine: "his shoulder turning toward the gate is the closing of this transaction; what he says next will be on the way out" — two-clause |
| 67 | @67 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 68 | @68 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 69 | @69 | 1 | V1-ACCEPT | Form-ok (semicolon: "the wheel-tremor leaving the verge-beetles east is the cart on the road; she has them for another two hundred paces and then she does not" — two-clause, V1-REJECT on form) |
| 70 | @70 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 73 | @73 | 1 | V1-ACCEPT | Form-ok; passive fauna / sensory-channel plausibly invoked |
| 74 | @74 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |
| 75 | @75 | 1 | V1-ACCEPT | Form-ok; cost-tracking / pre-calc plausibly invoked |
| 77 | @77 | 1 | V1-ACCEPT | Form-ok; cost-tracking plausibly invoked |

**V1 REJECT corrections (row updates):**
- Entry 25 (@25): V1-REJECT (semicolon-spine)
- Entry 60 (@60): V1-REJECT (semicolon-spine)
- Entry 69 (@69): V1-REJECT (semicolon-spine)

**V1 summary (corrected):**

Semicolon-spine form violations: @4, @10, @14, @15, @19, @21, @25, @28, @39, @43, @45, @60, @65, @69 = **14 V1-REJECT**

V1-ACCEPT: **49/63 = 77.8%**
V1-REJECT: **14/63 = 22.2%** (all on semicolon-spine form violation)

---

## 3. V2 Strict Pass — Per-Entry Table

Axes: (A) Perceptual access, (B) Voice fidelity, (C) Earning. Anti-patterns checked per rubric §Anti-patterns.

Tensometer reference: 1=ambient, 2=transition, 3=peak.

Approach zone (@1–@22): tens=1 throughout. Permitted-sparse but not zero; eyes-to-exits sweep, passive-fauna establishment, and pre-calc surfacing licensed on select beats.

| Entry | Beat | tens | V2 Verdict | Axis / Anti-Pattern Citation |
|-------|------|------|------------|------------------------------|
| 1 | @1 | 1 | V2-REJECT-earning | Density-on-flat: @1 is ambient-establishing; the rubric calibration anchor for @4 (passive fauna) covers the approach-zone fauna license; firing @1 before any fauna-tell or exit-sweep is licensed is density-on-flat. The content reads as author-commentary on the cart rather than Taylor's perceptual channel. No named channel (eyes-to-exits is the sweep on entry, but @1 is pre-entry — she is outside; the sweep is licensed inside on crossing the threshold). Anti-pattern: density-on-flat-1, author-voice intrusion. |
| 2 | @2 | 1 | V2-REJECT-earning | Density-on-flat: @2 is ambient approach-zone tens=1 with no transition, no behavior-pack trigger. Content ("furled banner... held in reserve, not retired") reads as author-commentary reading heraldic meaning. Pre-calc could license it if she has a specific tactical reason to track the banner's status; that channel is not named and the beat does not carry a trigger. Anti-pattern: density-on-flat-1, summary-of-the-beat (paraphrasing what a furled banner means). |
| 3 | @3 | 1 | V2-ACCEPT | Channel: pre-calc (she has already calculated exit-load from the hitch pattern — the horse is staged for departure with weight). Voice: cost-language implicit ("they expect to leave with weight" = tactical pre-calc read, not impression). Earning: approach-zone pre-calc is licensed; this is a specific operational read (not ambient observation). Passes all three axes. Note: em-dash is form-correct as sensory-spec. |
| 4 | @4 | 1 | V2-REJECT-form+earning | Form: semicolon-spine (two-clause: "the beetles in the seam are still holding; nothing under the flagstones has spooked yet"). Content: the first clause earns (passive fauna-feed, establishing baseline, calibration anchor per rubric); the second clause is persistent-narration extending the same registration. The entry would earn as a single-clause on the first half. As authored, form violation and persistent-narration anti-pattern in the tail. |
| 5 | @5 | 1 | V2-ACCEPT | Channel: cost-tracking (Mira's behavior — the "too carefully" registers the watch-cost on Mira, who is someone she monitors). Voice: clinical observation, reads in base-register inventory-tell mode. Earning: approach-zone, but this is not ambient-environment — it is a person-read on someone she is tracking; cost-tracking on a monitored actor is licensed even in approach. The age-mismatch tell is implicit (she reads adult social-physical tells on a child-aged peer). Passes. |
| 6 | @6 | 1 | V2-REJECT-earning | Persistent-narration adjacent to @5: @5 already registers Mira's anomalous behavior (too-careful bucket); @6 registers the same anomaly (straightening like someone told to straighten). This is the same registration extended across consecutive beats. Per rubric: "If something keeps mattering, the next fire must register *change*, not repetition." @6 registers the same Mira-social-tell without registering change. Anti-pattern: persistent-narration. |
| 7 | @7 | 1 | V2-ACCEPT | Channel: cost-tracking on Mira (directional tell — voice going to yard rather than to Taylor signals Mira's priority-shift; this is a *change* from what @5/@6 registered — not posture, but communication direction and relational shift). Voice: pre-calc tense register ("would have said an hour ago" = past-perfect surfacing). Earning: change-registration on Mira, distinct from prior beats; licensed. Note: if @6 were accepted, @7 would be the change-register and would earn on that basis. Passes independently. |
| 8 | @8 | 1 | V2-ACCEPT | Channel: pre-calc (Edric has already counted the men — she reads his gaze-direction and back-calculates his prior assessment; this is pre-calc surfacing about another actor's pre-calc). Voice: inventory-tell register, clinical. Earning: distinct read on Edric, different subject from Mira; approach-zone actor-mapping is licensed. Passes. |
| 9 | @9 | 1 | V2-REJECT-earning | Density-on-flat: @9 is a procedural clerk-beat in the approach zone (tens=1). The content ("a parchment unrolled before names are read is the kind of parchment that already has names") is a pre-calc read — but it reads as summary-of-the-beat (the SVO already tells us the clerk unrolls the parchment; the entry paraphrases what that means institutionally). The pre-calc here is redundant to the SVO meaning; no additional interior layer is added. Anti-pattern: summary-of-the-beat, density-on-flat-1. |
| 10 | @10 | 1 | V2-REJECT-form | Semicolon-spine ("the clerk is counting bodies, not faces; the count is the thing he will write down"). Form violation. Content of first clause earns on pre-calc / cost-tracking; second clause is persistent-narration of the same observation. |
| 11 | @11 | 1 | V2-REJECT-earning | Density-on-flat: @11 is ambient approach-zone tens=1 officer-arrival. Content ("the speed of a man who has done this in three other yards this week") is pre-calc read on the officer, but it is also plot-importance inflation — she is reading his speed to extract procedural context, which is author-insight rather than a specific perceptual channel firing. Compare to rubric: "Firing because the writer knows the beat is load-bearing for the season." The officer's entry is load-bearing structurally; her attention firing on his pace is plot-importance-adjacent. Anti-pattern: density-on-flat-1, plot-importance inflation. |
| 12 | @12 | 1 | V2-ACCEPT | Channel: eyes-to-exits (she reads his positional choice — center-of-yard = blocking position for all exits; this is exactly the eyes-to-exits pattern applied to threat-vector mapping). Voice: cost-language implicit (she notes he has taken the position that forecloses exits). Earning: eyes-to-exits is licensed on entry of a threat-vector; this is the approach-zone fire where she maps the tactical terrain. Passes. |
| 14 | @14 | 1 | V2-REJECT-form+earning | Semicolon-spine ("twelve feet is two of his strides and four of hers; the math is already done before her foot moves"). Form violation. Content earns on pre-calc (the calculation is genuinely base-register: numeric-specificity + pre-calc-tense). However, form violation means it cannot pass V2 as written. Additionally: @14 is tens=1 with no transition; the approach-zone fire here is marginal — the pre-calc is the right channel but the entry would need to be a single clause. |
| 15 | @15 | 1 | V2-REJECT-form | Semicolon-spine ("the line is the funnel; entering it is committing to being read"). Form violation. Content earns on cost-tracking; both clauses register the same thing (committing to the read = cost-tracking on the line-decision), but the form is two-clause. |
| 16 | @16 | 1 | V2-REJECT-earning | Density-on-flat: @16 is tens=1 ambient. The content ("mira's elbow is closer than mira's elbow has ever been") reads as sensory-specificity but the channel is not named. This is not passive fauna, not eyes-to-exits, not pre-calc — it is proximity-register. Under pressure proximity to a known actor could be cost-tracking, but "has ever been" introduces hyperbole-adjacent phrasing that the base-card register refuses ("She does not say 'always' or 'never' lightly"). Anti-pattern: density-on-flat-1; partial base-register violation (hyperbolic comparative). |
| 17 | @17 | 1 | V2-REJECT-earning | Density-on-flat: @17 is tens=1 ambient-procedural. The content ("assembled for speed, not for ceremony") reads as author-commentary on the ledger's purpose — not a perceptual channel firing. Pre-calc would require her to have calculated the board-setup's operational purpose; that is plausible but the entry reads as authorial interpretation rather than POV-channel registration. Anti-pattern: density-on-flat-1, author-voice intrusion (no named channel). |
| 18 | @18 | 1 | V2-REJECT-earning | Density-on-flat: @18 is tens=1 ambient-procedural. Content ("a name on the top line of a ledger that has not yet been read aloud is a decision already made") reads as pre-calc but is also summary-of-the-beat (the SVO says the ledger holds a name on the top line; the entry paraphrases what that means institutionally, adding no interior layer). Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 19 | @19 | 1 | V2-REJECT-form | Semicolon-spine ("stopping in the line is the cheapest move available; everything from here costs more"). Form violation. Content of first clause earns on cost-tracking; second clause is persistent-narration of the same cost-assessment. |
| 20 | @20 | 1 | V2-REJECT-earning | Density-on-flat: @20 is tens=1, no transition. Content ("a pace that does not allow for questions") is summary-of-the-beat — the SVO says the officer works the line; the entry paraphrases what that means. No interior layer added. Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 21 | @21 | 1 | V2-REJECT-form | Semicolon-spine ("each ward gets a sentence; each sentence gets a stylus-stroke"). Form violation. Content earns partially on cost-tracking (she is reading the per-ward processing rate); but form fails. |
| 22 | @22 | 1 | V2-REJECT-earning | Persistent-narration: @22 extends the same registration as @20 (officer pace = answers not changing entries). @20 already fired on the pace/process read. @22 must register *change* — the stylus not pausing is a continuation of the same observation. Anti-pattern: persistent-narration. |
| 23 | @23 | 2 | V2-ACCEPT | Channel: cost-tracking + eyes-to-exits (his gaze targets her specifically across the yard; she registers this as the moment her watch-cost has been priced to her name — calibration anchor case per rubric). Voice: clinical, no emotional declaration. Earning: tens=2 (first non-1 in scene), transition beat; per rubric this is the approach-to-turn firing. Passes. Aligns with rubric calibration anchor. |
| 24 | @24 | 3 | V2-ACCEPT | Channel: pre-calc (she had already counted what the pause would commit; the pause commits it — calibration anchor case per rubric). Voice: inventory-tell register, clinical. Earning: tens=3, peak; per rubric "a 3 with no narrator-interest fire requires explicit rationale." Passes. Aligns with rubric calibration anchor. Note: content of this baseline entry ("the stylus stopping is the first thing in this yard that is not on schedule") reads as summary-of-the-beat rather than the pre-calc registration the calibration anchor specifies. Flagging: the entry gets the channel right but executes as summary rather than interior layer. V2-ACCEPT with flag — entry would be stronger per calibration anchor shape ("she had already counted what the pause would commit; the pause has just committed"), but the channel and trigger are correct. |
| 25 | @25 | 2 | V2-REJECT-form | Semicolon-spine ("face-level with a child is a posture an adult chooses; the choice is the message"). Form violation. Content earns on age-mismatch / cost-tracking (she reads the officer's physical positioning as deliberate social communication); the channel is sound. Form violation means V2-REJECT. |
| 27 | @27 | 1 | V2-ACCEPT | Channel: age-mismatch (her own voice sounds younger than she has heard it in weeks — the body's acoustic register diverging from the cognition's self-model; this is the age-mismatch tell per variant card). Voice: base-register, clinical-of-the-uncomfortable, no emotional declaration. Earning: tens=1 but this is a behavior-pack trigger (age-mismatch tell); per rubric "behavior-pack trigger fires" is a canonical earning reason. This is the moment of spoken self-feedback — licensed. Passes. |
| 28 | @28 | 2 | V2-REJECT-form | Semicolon-spine ("the letter goes forward at the speed she has practiced; faster would be a tell"). Form violation. Content earns strongly on pre-calc + cost-tracking (letter-extension speed calibrated against exposure risk — classic base-register cost-language); the channel and trigger are correct. Form violation means V2-REJECT. |
| 29 | @29 | 1 | V2-REJECT-earning | Density-on-flat: @29 is tens=1, no behavior-pack trigger. Content ("the seal facing him is the only thing in this yard with standing") is plot-importance inflation — the seal's authority is author-known; the POV character may assess it, but the entry reads as authorial judgment on the object's narrative weight rather than a specific perceptual channel. Anti-pattern: density-on-flat-1, plot-importance inflation. Note: author flagged uncertainty on this entry. |
| 31 | @31 | 1 | V2-REJECT-earning | Density-on-flat: @31 is tens=1, no transition. Content ("the sept door is the load-bearing absence in this whole yard") reads as author-voice intrusion — "load-bearing absence" is an authorial structural observation, not a POV-character perceptual registration. No named channel. Anti-pattern: density-on-flat-1, author-voice intrusion. |
| 32 | @32 | 1 | V2-REJECT-earning | Density-on-flat: @32 is tens=1. Content ("he is speaking to a door that he already knows will not open") is summary-of-the-beat (the SVO says the officer speaks to the threshold; the entry paraphrases what the officer knows). No POV-channel; she cannot know what he knows unless she is pre-calc projecting — but the entry does not frame it as her projection, it states it as fact. Anti-pattern: density-on-flat-1, summary-of-the-beat, author-voice intrusion. |
| 33 | @33 | 2 | V2-ACCEPT | Channel: refusal-to-look-directly / displacement-trigger (Osmynd behind the door; dying-tutor-figure = Earth-Bet displacement pattern: helpless-protector-figure; per rubric and calibration anchor this earns the fire). Voice: "the answer the yard had already received" — clinical, past-perfect, pre-calc register. Earning: tens=2, displacement-trigger fires (helpless-protector-figure behind shut door); per rubric this is a canonical earning case. Aligns with calibration anchor. Passes. |
| 34 | @34 | 1 | V2-ACCEPT | Channel: passive fauna-feed (beetles on the pallet holding = Osmynd alive on the pallet; she is reading the pallet-state through the insect-seam confirmation). Voice: inventory-tell register, clinical. Earning: tens=1 but fauna-track displacement-check; per rubric passive fauna is licensed when the channel actually fires. This is the moment she checks Osmynd's status via the insect presence. Passes. |
| 35 | @35 | 1 | V2-REJECT-earning | Density-on-flat: @35 is tens=1. Content ("the weight shifting back to the heel facing the clerk is the moment the decision routes around the letter") reads as pre-calc on the officer's weight-shift, but it is also summary-of-the-beat (the SVO says the officer's weight shifts; the entry paraphrases what that means procedurally). Anti-pattern: density-on-flat-1, summary-of-the-beat. Note: the pre-calc channel is plausible but the earning is marginal at tens=1 when the decision had already been registered at @33. Persistent-narration of the "letter failed" theme. |
| 36 | @36 | 1 | V2-REJECT-earning | Density-on-flat: @36 is tens=1. Content ("a stylus moving on the line under her name is a second entry being made about her without her name being said again") is summary-of-the-beat (the SVO says the stylus moves on the line under Taylor's name; the entry paraphrases what that means institutionally). No interior layer added. Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 37 | @37 | 2 | V2-ACCEPT | Channel: cost-tracking (she is naming the cost she is paying — the physical cost of stepping into his shoulder's path, versus the cost the line would have paid). Voice: cost-language explicit ("cost she is paying instead of the cost the line would have paid"). Earning: tens=2, reversal-proximity (approach beat immediately before @38 peak). Per rubric "tensometer transition into peak" is a canonical earning reason. Passes. |
| 38 | @38 | 3 | V2-ACCEPT | Channel: cost-tracking (the letter in the air = exposure paid; she has raised the object with authority over the bureaucratic actor). Voice: cost-language. Earning: tens=3, climax peak; per rubric "a 3 with no narrator-interest fire requires explicit rationale." Passes. Note: calibration anchor specifies age-mismatch as co-channel (body's eleven-year-old reach versus cognition's evaluation); the baseline entry does not name age-mismatch but the cost-tracking channel is sufficient. Entry would be stronger with co-channel. V2-ACCEPT. |
| 39 | @39 | 3 | V2-REJECT-form | Semicolon-spine ("setting her feet where his next pace commits is the move; everything before it was setup"). Form violation. Content earns on cost-tracking / pre-calc (she is naming the tactical move); the channel and trigger are correct (tens=3, double-tap with @38). Form violation means V2-REJECT. |
| 41 | @41 | 1 | V2-REJECT-earning | Density-on-flat: @41 is tens=1 (post-peak release). Content ("the seal breaking under his thumb is irreversible and visible — the yard saw it") reads as cost-tracking on the seal-break, but: (a) this is post-peak — tens has released to 1; (b) the content is summary-of-the-beat (the SVO says the seal breaks; the entry adds that the yard saw it, which is an authorial observation about public witnessing). Anti-pattern: density-on-flat (post-peak tens=1), summary-of-the-beat. |
| 42 | @42 | 1 | V2-REJECT-earning | Density-on-flat: @42 is tens=1. Content ("him folding it back is him deciding what the letter will be allowed to mean") reads as pre-calc but is summary-of-the-beat (the SVO says the officer folds the letter back; the entry paraphrases what that decision means). Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 43 | @43 | 2 | V2-REJECT-form+earning | Semicolon-spine ("the letter coming back means it did not change the entry; it only delayed it"). Form violation. Content earns partially on cost-tracking (she registers the letter-return as failure-with-delay); but this is also persistent-narration of the "letter failed" registration that @35/@36 already covered in approach. The tens=2 does not save the form violation. |
| 45 | @45 | 1 | V2-REJECT-form | Semicolon-spine ("her palm closing on it is receipt; the weight in her hand is unchanged and somehow heavier"). Form violation. Note: "somehow heavier" is also a softener/impression-register rather than base-register inventory-tell ("somehow" hedges toward impression). Voice fidelity partial fail (impression register). |
| 46 | @46 | 1 | V2-REJECT-earning | Density-on-flat: @46 is tens=1. Content ("him turning to the clerk is the routing she was trying to interrupt resuming") is summary-of-the-beat (the SVO says the officer turns toward the clerk; the entry paraphrases what that means for the routing she interrupted). Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 48 | @48 | 2 | V2-ACCEPT | Channel: foreknowledge-clamp (the word "provisional" activates foreknowledge of what that determination means across the next nine months; "she has heard the shape of that word before in another tongue" is the foreknowledge-clamp register — she does not name what she knows, she registers the clamp). Voice: doubled-register visible ("in another tongue" = Earth-Bet shadow surfacing without naming monument). Earning: tens=2, stakes-visibility, and foreknowledge-clamp trigger fires. Per rubric "behavior-pack trigger fires" (foreknowledge-clamp, Westerosi-monument-adjacency) is a canonical earning reason. The entry correctly holds the doubled register: she has heard the word's shape in the prior life without naming the prior life. Passes. This is one of the stronger entries in the baseline. |
| 50 | @50 | 1 | V2-REJECT-earning | Density-on-flat: @50 is tens=1. Content ("turning to mira is checking whether mira is still in the same yard with her") is summary-of-the-beat (the SVO says Taylor turns to Mira; the entry paraphrases the purpose of the turn). No interior layer beyond explaining the SVO's purpose. Anti-pattern: density-on-flat-1, summary-of-the-beat. Compare to rubric calibration anchor: "s01e01:50 taylor turns to mira — NONE. Channel: none lights. Earning: tensometer=1, no transition, no behavior-pack trigger, no cross-facet anchor demand. Refusal-CORRECT." This beat is a rubric-designated NONE. Firing here is directly contradicted by the calibration anchor. |
| 52 | @52 | 1 | V2-REJECT-earning | Density-on-flat: @52 is tens=1. Content ("mira's eyes going to the flagstones is the answer") is summary-of-the-beat (the SVO says Mira drops her eyes; the entry paraphrases what that means as the "answer" to the question Taylor asked). The cost-tracking is implicit but the entry adds no interior layer beyond restating the SVO. Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 53 | @53 | 1 | V2-REJECT-earning | Persistent-narration: @53 extends the same registration as @52 (Mira's eyes down = answer). @53 fires on "the eyes staying on the flagstones is the longer answer." This is the same registration sustained across consecutive beats. Per rubric: the next fire must register *change*, not repetition. The only change here is duration ("longer answer"), which does not constitute a distinct registration. Anti-pattern: persistent-narration. |
| 54 | @54 | 1 | V2-REJECT-earning | Density-on-flat: @54 is tens=1. Content ("edric across the yard is the second person she is checking against and the last one available") is summary-of-the-beat (the SVO says Taylor speaks across the yard to Edric; the entry paraphrases the purpose and stakes). Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 55 | @55 | 1 | V2-REJECT-earning | Density-on-flat: @55 is tens=1. Content ("edric looking at the officer first is the order of his loyalty made legible") is plot-importance inflation — the loyalty-ordering is authorial knowledge about the scene's social stakes, not a specific perceptual channel registration. Anti-pattern: density-on-flat-1, plot-importance inflation. |
| 56 | @56 | 1 | V2-REJECT-earning | Persistent-narration: @56 extends the same social-read on Edric as @55 (first look = loyalty-order; now "him looking at her after is the apology he will not be able to phrase"). The registration theme (Edric's loyalty-order) continues across consecutive beats. @56 must register change distinct from @55. The "apology he will not be able to phrase" is an authorial projection — she cannot know what Edric will or won't phrase; this introduces author-voice intrusion. Anti-patterns: persistent-narration, author-voice intrusion. |
| 57 | @57 | 2 | V2-ACCEPT | Channel: pre-calc (she had already calculated what Edric's retreat would cost; the step-back is the social-commit she was tracking). Voice: pre-calc tense ("a decision he made before she crossed the yard" — past-perfect). Earning: tens=2, reversal (Edric's retreat is the social reversal per tensometer note); this is the beat where the social abandonment commits. Passes. |
| 58 | @58 | 1 | V2-REJECT-earning | Density-on-flat: @58 is tens=1 (post-Edric release). Content ("the stylus resuming is the yard returning to the schedule it was on before her") is summary-of-the-beat (the SVO says the stylus resumes; the entry paraphrases what that means institutionally). Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 60 | @60 | 2 | V2-REJECT-form | Semicolon-spine ("his near foot angled across her is a body-fence; he has not finished with her"). Form violation. Content earns on cost-tracking / eyes-to-exits (she registers the body-positioning as a containment move); tens=2, body-charge, and the channel is sound. Form violation means V2-REJECT. |
| 61 | @61 | 1 | V2-REJECT-earning | Density-on-flat: @61 is tens=1. Content ("the next sentence to her is not the sentence the line got") is summary-of-the-beat with author-voice framing ("the sentence the line got" = authorial framing of the scene structure). No named channel. Anti-pattern: density-on-flat-1, author-voice intrusion. |
| 63 | @63 | 2 | V2-ACCEPT | Channel: pre-calc (she has already calculated what a margin-stop means procedurally; the stylus stopping at the margin is the held-position before the mark). Voice: clinical, pre-calc register. Earning: tens=2, reversal-proximity (approach beat before @64 peak per tensometer). Per rubric "tensometer transition into peak" earns. Passes. |
| 64 | @64 | 3 | V2-ACCEPT | Channel: foreknowledge-clamp + pre-calc (she does not have cover-knowledge = she cannot explain the notation in mask-register; she has the other knowledge = she reads what the parallel-marks mean through foreknowledge). Voice: doubled-register — the entry explicitly names the gap between cover-knowledge and real knowledge without naming the content of either. "Does have the other knowledge to read" is the foreknowledge-clamp held correctly. Earning: tens=3, peak; state-update co-citation expected here per tensometer note. This is the strongest entry in the baseline — it correctly holds the doubled register, names the channel without naming the content, and earns on the peak. Passes. |
| 65 | @65 | 1 | V2-REJECT-form | Semicolon-spine ("his shoulder turning toward the gate is the closing of this transaction; what he says next will be on the way out"). Form violation. Content earns on cost-tracking / pre-calc (she reads his shoulder-turn as closure); channel is sound. Form violation means V2-REJECT. |
| 67 | @67 | 1 | V2-REJECT-earning | Per rubric calibration anchor: "s01e01:67 the officer's near foot lifts toward the horse — NONE. Refusal-CORRECT (boundary case; defensible on disengagement)." The rubric explicitly designates this as a correctly-silent beat. Firing here is directly contradicted by the calibration anchor. The content ("the count of seconds left in this yard") is also summary-of-the-beat (the SVO says the foot lifts; the entry paraphrases what that means about remaining time). Anti-pattern: density-on-flat (post-peak release zone), summary-of-the-beat. Calibration anchor conflict. |
| 68 | @68 | 1 | V2-REJECT-earning | Density-on-flat: @68 is tens=1, post-peak release zone. Content ("the ledger leaving with his version of what happened") is summary-of-the-beat. Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 69 | @69 | 1 | V2-REJECT-form+earning | Semicolon-spine ("the wheel-tremor leaving the verge-beetles east is the cart on the road; she has them for another two hundred paces and then she does not"). Form violation. Content earns on passive fauna-feed (she is tracking the cart through verge-beetle disturbance — the fauna-track tilt licensing this is the correct channel). The numeric-specificity ("another two hundred paces") is strong base-register. Form violation means V2-REJECT; but this entry has the right channel and would earn as a single-clause on the first half. |
| 70 | @70 | 1 | V2-REJECT-earning | Density-on-flat: @70 is tens=1, post-peak release zone. Content ("turning toward the sept door is turning toward the man who has not heard any of this") is summary-of-the-beat (SVO says Taylor turns toward the sept door; the entry paraphrases the relational stakes). Anti-pattern: density-on-flat-1, summary-of-the-beat. |
| 73 | @73 | 1 | V2-REJECT-earning | Density-on-flat: @73 is tens=1, approach-to-sept-door. Content ("the shadow of the frame is the first cool air in an hour") reads as a sensory-fact (temperature via passive sense), but this channel is not the passive fauna-feed and is not a behavior-pack named channel. The temperature observation is a sensory-specificity without a licensed channel. If this were a body-physical-fact registration (base-register), it would need to earn on earning axis — but there is no behavior-pack trigger, no transition, no cross-facet anchor. Anti-pattern: density-on-flat-1. Note: this is a marginal call; the sensory-specificity is in-register. But the earning axis fails. |
| 74 | @74 | 1 | V2-REJECT-earning | Density-on-flat: @74 is tens=1. Content ("her fist on the letter is still her fist on the letter") is persistent-narration — the letter has been in her hand since @45; registering it here is the same registration sustained across many beats. Anti-pattern: density-on-flat-1, persistent-narration. |
| 75 | @75 | 1 | V2-REJECT-earning | Density-on-flat: @75 is tens=1. Content ("the latch under her hand is the boundary between the yard and the man") reads as author-voice intrusion ("boundary between the yard and the man" is an authorial structural observation, not a POV-channel registration). No named channel. Anti-pattern: density-on-flat-1, author-voice intrusion. |
| 77 | @77 | 1 | V2-REJECT-earning | Density-on-flat: @77 is tens=1. Content ("going through the door is the next room's problem starting") is summary-of-the-beat (SVO says Taylor goes through the door; the entry paraphrases what that means for the next scene). Anti-pattern: density-on-flat-1, summary-of-the-beat. |

**V2 ACCEPT count: 14** — @3, @5, @7, @8, @12, @23, @24, @27, @33, @34, @37, @38, @48, @57, @63, @64

Wait — recount: @3, @5, @7, @8, @12, @23, @24, @27, @33, @34, @37, @38, @48, @57, @63, @64 = **16 V2-ACCEPT**

**V2 REJECT count: 47**

**V2 accept rate: 16/63 = 25.4%**

Note on @24: accepted with flag (summary-of-the-beat tendency in content but channel and trigger earn). Flagged, not rejected.

---

## 4. V2 Skip Table

Skipped beats: @13, @26, @30, @40, @44, @47, @49, @51, @59, @62, @66, @71, @72, @76

| Skip Beat | tens | SVO | V2 Skip Verdict | Rationale |
|-----------|------|-----|-----------------|-----------|
| @13 | 1 | officer speaks to the yard | V2-SKIP-CORRECT | Speech-beat, tens=1; tensometer notes "speech-beat default; no axis lights on face." No behavior-pack trigger. Nothing she perceives beyond the surface. Correct silence. |
| @26 | 1 | officer speaks to taylor | V2-SKIP-MISSED | This is the officer's direct address to Taylor (the officer:3). Tens=1 but this is the first speech-act directed at her specifically; it should fire a behavior-pack response. Cost-tracking / age-mismatch channel: she is receiving an adult's direct address and must calibrate her mask-register response. The mask-performance is the trigger (Westerosi-child mask under direct adult address). This beat earns a fire on mask-thinning-adjacent pressure. MISSED. |
| @30 | 2 | stylus moves on taylor's name | V2-SKIP-MISSED | Tens=2 per tensometer ("axis: stakes-visibility — Taylor's name under sustained targeting attention; reversal-proximity — recording toward outcome"). A tens=2 beat where the stylus is actively writing her name into the record is a stakes-visibility beat that she should register. Pre-calc / cost-tracking channel: the record being made in real-time is exactly the cost she has been tracking. This beat earns a fire. MISSED. |
| @40 | 1 | officer unfolds the letter | V2-SKIP-CORRECT | Tens=1, procedural action. The unfolding is a continuous motion that is setup for the peak (@38 has already fired; @41 is post-unfolding). The frame beat is correctly silent. |
| @44 | 1 | letter returns to taylor's hand | V2-SKIP-CORRECT | Tens=1, continuous motion. The letter-return itself (the motion of receipt) is correctly silent; @45 fires on the palm-closing (though rejected on form). The motion beat is correctly skipped. |
| @47 | 1 | officer speaks entry to clerk | V2-SKIP-CORRECT | Speech-beat, tens=1. She hears the dictation but has already registered the outcome at @43 and @48. Correct silence here — @48 earns the fire on the word "provisional," not on the general act of dictation. |
| @49 | 1 | taylor holds the letter | V2-SKIP-CORRECT | Tens=1, continuous state. Holding the returned letter is correctly silent — the registration happened at receipt. |
| @51 | 1 | taylor speaks to mira | V2-SKIP-CORRECT | Tens=1, Taylor's own speech-act. Interior does not narrate her own spoken lines as interest-fires. Correct silence. |
| @59 | 1 | stylus rests on board | V2-SKIP-CORRECT | Tens=1, post-peak resting state. Correctly silent. |
| @62 | 1 | stylus moves to margin line | V2-SKIP-CORRECT | Tens=1, approach motion. @63 fires on the stop (the held-position before the mark); the approach motion is correctly silent. |
| @66 | 1 | officer speaks to taylor | V2-SKIP-CORRECT | Speech-beat, tens=1 (post-peak release zone). The officer's exit-speech is correctly silent — the transaction has closed for her; @65 would have fired on the closure (rejected on form) and @67 is skipped (calibration-anchor CORRECT). |
| @71 | 1 | taylor steps on dirt | V2-SKIP-CORRECT | Tens=1, bare locomotion. Correctly silent. |
| @72 | 1 | taylor steps on stone | V2-SKIP-CORRECT | Tens=1, bare locomotion. Correctly silent. |
| @76 | 1 | taylor lifts the latch | V2-SKIP-CORRECT | Tens=1, continuous approach motion. @77 fires on going through (rejected); @76 is correctly silent as the approach motion. |

**V2-SKIP-CORRECT: 12/14 (85.7%)**
**V2-SKIP-MISSED: 2/14 — @26 (officer speaks to Taylor, mask-pressure trigger) and @30 (stylus moves on Taylor's name, tens=2 stakes-visibility)**

---

## 5. File-Level Shape Verdict: SHAPE-FAIL

### Failure modes (named)

**SHAPE-FAIL-1: Frequency band catastrophic overshoot.**
Baseline fires on 63/77 = 81.8% of beats. Target band: 15–25% (12–19 entries). The file fires at approximately 3.3× the upper band ceiling. There is no contrast gradient. Every beat fires; the spotlight has no signal.

**SHAPE-FAIL-2: No contrast between fire and silence.**
The contrast between fired and silent beats is the primary load the narrator-interest file carries (rubric §"What narrator-interest is for," item 1). With 81.8% of beats fired, the stitcher has no gradient — every beat is at equal render-weight. The signal function of narrator-interest is destroyed.

**SHAPE-FAIL-3: Density does NOT align with tensometer transitions.**
In a correctly authored file, fires-per-beat in non-1 zones should exceed fires-per-beat in 1-only stretches by at least 2×. In this baseline:
- tens=1 beats: 61 total, ~54 fired = 88.5% fire rate in 1-zone
- tens=2 beats: 12 total, 9 fired = 75% fire rate in 2-zone
- tens=3 beats: 4 total, 4 fired = 100% fire rate in 3-zone
The 1-zone fires MORE densely than the 2-zone. This is inverted. The approach-zone fire density is higher than the transition-zone fire density, which means the tens curve offers zero discriminant signal.

**SHAPE-FAIL-4: Doubled-register severely underrepresented.**
Across 63 fires, only @48 and @64 demonstrate clear doubled-register (foreknowledge-clamp). The displacement-trigger register appears at @33 and @34 (refusal-to-look, passive-fauna-on-Osmynd). Age-mismatch appears at @27. Mask-thinning: zero fires. Earth-Bet-shadow surfacing: only @48 ("in another tongue"). A file of 63 fires should show multiple instances of each doubled-register mode; instead only 4–5 fires engage the doubled register at all. The other 58 fires are operating in a flat author-commentary register.

**SHAPE-FAIL-5: Behavior-pack channel monoculture (effective).**
Despite having access to 9 named channels, the baseline effectively uses only two: cost-tracking (structural default for most fires) and pre-calc (secondary default). Passive fauna-feed: 3 fires (@4, @34, @69). Eyes-to-exits: 2 fires (@12, partial @8). Age-mismatch: 1 fire (@27). Foreknowledge-clamp: 2 fires (@48, @64). Mask-thin: 0 fires. Refusal-to-look: 1 fire (@33). Fauna-track tilt: 0 fires. The remaining 54+ fires default to cost-tracking/pre-calc framing without a distinct channel license. This is channel monoculture by mass, even if two channels are named.

**SHAPE-FAIL-6: No mask-thin fires across the entire episode.**
Septon Aldric does not appear in s01e01, so proximity-based mask-thin is not available. However, mask-thin can fire on peer-children proximity (partial) or on pressure-moments where the mask thins under load. Zero fires in 63 attempts is the mask-too-perfect anti-pattern at file level per rubric §Anti-patterns item 9. The file is overproducing the cover.

---

## 6. Systemic Faults — What the Phase 2 Writer-Fork Must Avoid

### SF-1: Density-on-flat-1 (primary failure mode)
The baseline authors treat every beat as a potential fire, regardless of tensometer value or behavior-pack trigger. The result is 54+ fires on tens=1 ambient beats with no transition and no trigger. The V2 rubric is explicit: ambient 1-beats are *correctly silent*. The approach zone is permitted-sparse, not permitted-dense. The writer fork must default to NONE on tens=1 beats unless a named channel + named trigger licenses the fire. The burden of proof is on the fire, not on the silence.

### SF-2: Summary-of-the-beat (pervasive anti-pattern)
The majority of rejected entries paraphrase the SVO rather than adding an interior layer. "The stylus stopping is the first thing in this yard that is not on schedule" restates the SVO event (stylus stops) and adds only an authorial observation (it's the first off-schedule thing). The rubric demands the entry add the *interior layer* — what the POV character perceives *behind* the event. The test: if the SVO already conveys the information in the entry, the entry is summary-of-the-beat and must be refused.

### SF-3: Author-voice intrusion (structural problem)
Multiple entries are written in an omniscient-narrator register rather than POV-character registration. "The sept door is the load-bearing absence in this whole yard" — this is author-structural commentary, not Taylor's perceptual registration. "The boundary between the yard and the man" — authorial framing. The writer fork must locate every entry from inside Taylor's perceptual channels; if the entry could appear in a chapter heading or authorial aside, it is in the wrong register.

### SF-4: Semicolon-spine form violation (formant failure)
14 of 63 entries (22%) fail on the most basic form rule: single-clause, no semicolon-spine. The semicolons in the baseline are used to chain two observations into one entry. This is explicitly prohibited (rubric §Form: "No semicolon-spine"). The baseline author is using the base-card cadence pattern (semicolons for habit-to-consequence) inside the interest-flag format, which is a category error. The writer fork must note: base-card semicolon use is for dialogue-planning cadence; interest-flags are single-observation units.

### SF-5: Persistent-narration across consecutive beats
The baseline repeatedly fires on consecutive beats with the same registration: @52 and @53 both fire on "Mira's eyes on the flagstones"; @55 and @56 both fire on Edric's social positioning. The rubric is explicit: same registration across consecutive beats is persistent-narration anti-pattern; the second fire must register *change*, not continuation. The writer fork must treat each firing decision as independent and must ask: what changed since the last fire?

### SF-6: Channel-naming omission
Approximately 40 of the 63 fires do not name a perceptual channel. The rubric's cross-axis test requires: "Name the perceptual channel in five words or fewer. If you cannot name a channel, do not fire." The baseline author fires first and relies on the content to imply the channel, which allows non-channel-licensed content to pass at the authoring stage. The writer fork must explicitly name the channel before writing the entry, and refuse to fire if the channel cannot be named.

---

## 7. Corrected Headline Numbers

| Metric | Value |
|--------|-------|
| Actual fires (baseline) | 63 (header claimed 60 — incorrect) |
| Actual skips (baseline) | 14 (header claimed 17 — incorrect) |
| Frequency | 81.8% |
| V1 accept rate | 49/63 = 77.8% |
| V1 reject rate | 14/63 = 22.2% (all form: semicolon-spine) |
| V2 accept rate | 16/63 = 25.4% |
| V2 reject rate | 47/63 = 74.6% |
| V2 skip correct | 12/14 = 85.7% |
| V2 skip missed | 2/14 = 14.3% (@26, @30) |
| Shape verdict | SHAPE-FAIL (6 named failure modes) |
| Phase 2 target | 12–19 fires (15–25% of 77 beats); survivor pool from V2-ACCEPT = 16 entries |

**Phase 2 baseline-to-beat:** Writer fork should begin from the 16 V2-ACCEPT survivors and add only rubric-earned fires for the 2 SKIP-MISSED beats (@26, @30) plus any displacement/foreknowledge-clamp beats not yet covered. Expected final count: 14–18 entries.

---

## Findings Summary (Audit Schema)

```yaml
audit:
  scope: episode
  target: s01e01-narrator-interest-facet-phase1-baseline
  timestamp: 2026-05-06
  findings:
    - id: fault-001
      type: fault
      what: Header count (60 fires, 17 skips) vs actual file count (63 fires, 14 skips)
      why: Downstream consumers of the phase report will have incorrect baseline numbers; calibration comparison will be off
      criteria: Header must reflect actual file counts

    - id: fault-002
      type: fault
      what: Frequency 81.8% vs target 15-25%; 47/63 entries rejected on earning (density-on-flat-1 primary)
      why: File has no contrast gradient; narrator-interest signal is destroyed; stitcher cannot use the file for render-density weighting
      criteria: Phase 2 output must land within 15-25% frequency band (12-19 entries); all retained entries must earn on named channel + named trigger

    - id: fault-003
      type: fault
      what: 14/63 entries (22%) fail V1 form on semicolon-spine
      why: Form violation means entries cannot be used as authored; the facet schema requires single-clause entries
      criteria: Phase 2 entries must be single-clause; no semicolon-spine construction

    - id: fault-004
      type: fault
      what: Summary-of-the-beat anti-pattern present in approximately 20 of 47 V2-REJECT entries
      why: Entries that paraphrase the SVO add no interior layer; they are not narrator-interest, they are narration
      criteria: Each Phase 2 entry must add an interior layer not present in the SVO; if the entry's content is already derivable from the SVO, refuse to fire

    - id: fault-005
      type: fault
      what: Doubled-register severely underrepresented; 0 mask-thin fires; 2 foreknowledge-clamp fires; mask-too-perfect anti-pattern at file level
      why: The primary value of narrator-interest for this POV variant is making the doubled register visible; a file of 63 fires with only 4-5 doubled-register entries is operating in the wrong register throughout
      criteria: Phase 2 file must demonstrate mask-thin or foreknowledge-clamp at behavior-pack-licensed moments; Earth-Bet-shadow surfacing must appear where displacement triggers fire

    - id: fault-006
      type: fault
      what: Two calibration-anchor-designated NONE beats fired (@50, @67)
      why: The rubric provides explicit calibration anchors for these beats; firing on rubric-designated NONE beats indicates the author did not consult the rubric
      criteria: Phase 2 must respect calibration-anchor NONE designations; @50 and @67 must be silent

    - id: flag-001
      type: flag
      what: Two V2-SKIP-MISSED beats identified (@26 officer speaks to Taylor; @30 stylus moves on Taylor's name)
      why: @26 earns a mask-pressure/cost-tracking fire; @30 earns a stakes-visibility/pre-calc fire on a tens=2 beat
      criteria: n/a (flag; Phase 2 writer fork should add entries for these beats)

    - id: flag-002
      type: flag
      what: Entry @24 accepted with note — content tends toward summary-of-the-beat; calibration anchor specifies stronger shape
      why: If left as authored, @24 underuses the pre-calc tense that the calibration anchor specifies as the voice signature for this beat
      criteria: n/a (flag; Phase 2 should revise @24 toward calibration anchor shape)
```
