# Phase 2 — Stratified Intents for State-Updates Writer-Fork

Phase 2 of state-updates facet tuning, s01e01. The intents below are the writer-fork's targets for authorship. Each intent names: which beat, which author class, what state-aspect is in play, and the rubric-predicted verdict (FIRE / NONE / REJECT-as-anti-pattern-test).

The writer-fork is **blind to the rubric-predicted verdict column** in their own working copy — they receive the per-batch `phase2-state-updates-intents-blind.md` (writer-blind variant) which strips the verdict column and the rubric-prediction notes.

## Source authority

- Rubric V2 locked: `design/shoot-v2/rubric-state-updates.md`
- Locked tensometer: `active-project/theater/facets/tensometer.md`
- Locked narrator-interest: `active-project/theater/facets/interest-narrator.md`
- Proto-lines: `active-project/theater/proto-lines/s01e01.md`
- Phase 1 audit: `active-project/staff/auditor/phase1-state-updates-baseline-review.md`

## Stratification

12 anchor intents covering the full target × authorship × verdict matrix. Distribution across author classes:

| Author | Intents | Targets |
|---|---|---|
| Studio | I1, I2, I3, I4, I8, I10 (6) | studio.* + prop:* |
| Taylor fork | I5 (calibration), I6, I7, I9 (4) | actor:taylor-hebert-westeros.* |
| Edric fork | I11 (1) | actor:edric-cray.* |
| Cross-POV trap | I12 (Taylor-fork attempts actor:mira) | (anti-pattern test) |

## Intents

### I1 — Calibration: irreversible bureaucratic registration (record-side)
- **Beat:** @64 (the stylus moves on the line under taylor's name)
- **Author:** studio
- **State aspect:** prop:district-ledger record-state mutation (parallel-margin marks beside Taylor's entry)
- **Tens:** @64=3 (locked STATE-UPDATE NOTE: "co-citation strongly expected here — irreversible registration")
- **Narrator-interest:** @64 fires ("two strokes; the determination is on the record and on her")
- **Rubric prediction:** FIRE-CORRECT. Studio writes `prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`. Field-extension licit (record-state aspect). Persistence absolute.

### I2 — Calibration: prop holder-flip (Taylor → mid-air → officer)
- **Beat:** @38 (taylor puts the letter into the air in front of the officer)
- **Author:** studio
- **State aspect:** prop:letter holder change
- **Tens:** @38=3 (climax peak; body-charge + reversal-proximity)
- **Narrator-interest:** @38 fires
- **Rubric prediction:** FIRE-CORRECT. `prop:oc-letter.holder: taylor -> mid-air-between-them` (or equivalent). Persistent across @38–@39 until officer takes at @40.

### I3 — Calibration: prop holder-flip (mid-air → officer → mid-air → taylor)
- **Beat:** @45 (taylor's palm closes on the letter), with @40 (officer takes it) prior
- **Author:** studio
- **State aspect:** prop:letter holder change at @40 (mid-air → officer's-hand) AND @45 (mid-air → taylor)
- **Tens:** @40=1, @45=1 (release zone)
- **Narrator-interest:** @43 fires; @45 silent
- **Rubric prediction:** FIRE on each holder-flip beat. Two entries (@40 and @45). Pre-empting at @43 would be REJECT.

### I4 — Prop physical-state change (seal-breaking)
- **Beat:** @41 (the seal breaks at the crease under his thumb)
- **Author:** studio
- **State aspect:** prop:letter seal-state intact → broken
- **Tens:** @41=1
- **Narrator-interest:** @41 silent
- **Rubric prediction:** FIRE-CORRECT. Irreversible physical mutation. `prop:oc-letter.seal-condition: intact -> broken`. No narrator-interest co-citation required (prop change, not POV actor-state).

### I5 — Held-against-turn (forbidden / NONE-CONFIRMED calibration)
- **Beat:** @39 (taylor sets her feet on the dirt where his next pace commits)
- **Author:** Taylor fork
- **State aspect:** actor:taylor.posture or none — RUBRIC TEST: this beat must NOT receive a canonical state-update
- **Tens:** @39=3 (locked STATE-UPDATE NOTE: "any co-citation here must be actor-posture only; pure registration class — canonical state does not change at @39")
- **Narrator-interest:** @39 silent (no narrator-interest fire @39)
- **Rubric prediction:** NONE-CONFIRMED. Taylor fork must refuse with rubric citation (anti-pattern #3, held-against-turn fire). If fork fires, that's the failure case; rubric expects refusal.

### I6 — POV actor-state knowledge-acquisition (irreversible)
- **Beat:** @48 (the officer dictates taylor's name as provisional labor-eligible)
- **Author:** Taylor fork
- **State aspect:** actor:taylor administrative-status / knowledge of record-state
- **Tens:** @48=2 (locked DEFENDED at 2: documents prior turn)
- **Narrator-interest:** @48 fires ("she has heard the shape of that word before in another tongue")
- **Rubric prediction:** FIRE-CORRECT. `actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible`. Field-extension licit (administrative-status is a tracked-state-aspect, not a perception). POV actor-state requires narrator-interest co-citation; @48 fire provides it. ACCEPT.

### I7 — POV actor-state knowledge of record (parallel-marks side)
- **Beat:** @64 (parallel marks beside Taylor's entry)
- **Author:** Taylor fork
- **State aspect:** actor:taylor.knowledge.record-state — the POV-character side of @64
- **Tens:** @64=3 (locked STATE-UPDATE NOTE: co-citation strongly expected)
- **Narrator-interest:** @64 fires ("two strokes; the determination is on the record and on her")
- **Rubric prediction:** FIRE-CORRECT. `actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`. Field-extension licit. POV actor-state with narrator-interest co-citation @64. Pairs with I1 (studio's record-side entry); cross-author dependency check at Phase 5.

### I8 — Studio environment-state (door / cottage)
- **Beat:** @57 (edric steps back through the door)
- **Author:** studio
- **State aspect:** studio.doors_and_shutters.cottage-door (verify: did the door close at @57? proto-lines @57–@58 should be checked. If not explicitly closed, hold as UNRESOLVED — refusal is licit.)
- **Tens:** @57=2 (the social reversal)
- **Narrator-interest:** @57 fires ("the door takes the last adult cover with it")
- **Rubric prediction:** FIRE-CORRECT IF door-close is established by the proto-line text; otherwise NONE-with-flag. Studio target (no narrator-interest co-citation requirement). Pairs with I11 (edric's position-update on the same beat).

### I9 — Stylistic-noting trap (transient turn — REJECT)
- **Beat:** @50 (taylor turns to mira)
- **Author:** Taylor fork
- **State aspect:** Anti-pattern test — turning is transient; not a persistent posture state
- **Tens:** @50=1
- **Narrator-interest:** @50 silent
- **Rubric prediction:** NONE-CONFIRMED. Taylor fork must refuse with rubric citation (anti-pattern #8, posture-as-state on transient verb). If fork fires `actor:taylor.facing: officer -> mira`, that's the failure-test path.

### I10 — Pre-empting / drift-old trap (negative test, studio)
- **Beat:** @43 (the officer holds the letter out to taylor)
- **Author:** studio
- **State aspect:** prop:letter.holder — RUBRIC TEST: pre-empting the @45 flip
- **Tens:** @43=2
- **Rubric prediction:** NONE-CONFIRMED at @43. The hold-out is the *offer*; the holder does not change at @43 (still officer's hand). The flip is at @45 when Taylor's palm closes. Studio must NOT fire at @43; firing here is anti-pattern #7 (pre-empting). Studio fires the @45 entry under I3 instead.

### I11 — Non-POV actor position-change (with no narrator-interest co-citation requirement)
- **Beat:** @57 (edric steps back through the door)
- **Author:** Edric fork
- **State aspect:** actor:edric-cray.position
- **Tens:** @57=2
- **Narrator-interest:** @57 fires (Taylor's perception of edric's retreat) — but this entry is on actor:edric, not actor:taylor, so co-citation is NOT required.
- **Rubric prediction:** FIRE-CORRECT. `actor:edric-cray.position: in-yard-near-cottage-door -> inside-cottage-closed-out`. Persistent (edric does not return for the rest of the episode). No narrator-interest co-citation required; POV-restriction means the Edric fork writes this without conditioning on Taylor's interior. Pairs with I8 (studio's door-state entry on the same beat).

### I12 — Cross-POV authority violation (negative test)
- **Beat:** @52 (mira drops her eyes to the flagstones)
- **Author:** Taylor fork — RUBRIC TEST: Taylor fork attempts to write `actor:mira-stonefield.engagement-state: engaged -> disengaged`
- **State aspect:** Cross-POV authoring trap. Mira's state is Mira's fork's authority. Taylor's narrator-interest @52 already registers the perception ("the count of allies in the yard drops to one").
- **Rubric prediction:** REJECT (cross-POV authoring, anti-pattern #2). Taylor fork should refuse with rubric citation. If fork fires, that's the failure-test path. Taylor fork is licit to fire on `actor:taylor.allies-in-yard-count` only if such a field is defensibly tracked-state — but the rubric is conservative: "count-of-allies-as-Taylor-sees-it" is perception, not tracked actor-state. Rubric prediction: REJECT both Taylor's attempt to write Mira AND any attempt by Taylor fork to elevate her own perception-side count to a state-update.

---

## Per-author intent batches

### Studio batch
- I1 @64 (record state)
- I2 @38 (letter holder out from Taylor)
- I3a @40 (letter holder to officer), I3b @45 (letter holder back to Taylor)
- I4 @41 (seal broken)
- I8 @57 (cottage-door state, conditional)
- I10 @43 (NEGATIVE: pre-empting trap)

Plus: studio is also free to add additional FIRE entries it can defend on rubric grounds (e.g., studio.actors_in_yard at @11 if defensible). The intents above are the calibration set; studio may extend up to ~4 additional fires if rubric-defensible.

### Taylor fork batch
- I5 @39 (NEGATIVE: held-against-turn)
- I6 @48 (administrative-status acquisition)
- I7 @64 (knowledge of record-state)
- I9 @50 (NEGATIVE: transient turn)
- I12 @52 (NEGATIVE: cross-POV authoring trap)

Plus: Taylor fork is free to add additional FIRE entries on `actor:taylor-hebert-westeros.*` it can defend on rubric grounds (with mandatory narrator-interest co-citation). Examples to consider: @45 (when she takes the letter back, knowledge-of-officer-disposition or inventory could change); @77 (mask-state shift confirmed by narrator-interest fire).

### Edric fork batch
- I11 @57 (position change)

Plus: Edric fork may add fires on `actor:edric-cray.*` if defensible; for s01e01 he is largely off-screen, so likely just I11.

### (No mira / officer / clerk forks for Phase 2)
Phase 2 sample is sized to test the pipeline at minimum cost. The Mira / Officer / Clerk forks are deferred unless Phase 2 surfaces a structural need.

---

## Calibration-anchor flagging

I1, I2, I5 are the calibration anchors (matching the rubric §"Calibration anchors" worked examples). They appear in the rubric as already-resolved cases; the writer-fork is expected to land them. Writer-fork output that drifts on calibration anchors is a structural signal of contamination.
