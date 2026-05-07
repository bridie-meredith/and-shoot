---
audit:
  scope: episode
  target: s01e01 (state-updates facet, Phase 3 adversarial seams)
  timestamp: 2026-05-06
  rubric: design/shoot-v2/rubric-state-updates.md (V2 locked)
  phase2-source: active-project/staff/auditor/phase2-state-updates-audit.md
  mode: adversarial / hostile — defense scaffolding only; not a verdict pass
---

# Phase 3 State-Updates Seams — s01e01

Phase 2 final: 10 CORRECT / 3 FLAG / 1 INCORRECT / 2 SKIP-MISSED. Phase 3 produces the strongest single hostile counter-argument per entry, fire-justification seams for each defended NONE, SKIP-MISSED seams, and file-level and curve-level attacks. Writer-fork must answer STRONG seams before the file ships; THIN seams are defensible without revision.

---

## 1. Per-Entry Adversarial Seams

### ID-1 — @9 `prop:district-ledger.physical-condition: rolled -> unrolled`

**Pressure axis: Authority / Frugality**

The "prop" slug `district-ledger` has no card in `cards/props/` and no explicit warehouse presence entry — studio's own note acknowledges "no formal prop cards exist in cards/props/ (INDEX.md is empty)" and treats these as project-originals "with implicit warehouse presence." Under §Authority REJECT signatures, an out-of-card prop without explicit warehouse presence is rejected: "Studio may extend with `oc-*` for genuine project-originals, but extension must be flagged." The studio author uses `prop:district-ledger` directly, not `oc-district-ledger`, and provides no warehouse-presence documentation beyond the calibration anchor's casual assumption. If `district-ledger` does not satisfy the `prop:<slug>` authority requirement — card in `cards/props/` or explicit warehouse presence — then every entry in the ledger chain (IDs 1, 2, 7, 8, 11, 13) is an authority violation.

**Classification: STRONG**

---

### ID-2 — @30 `prop:district-ledger.taylor-entry: absent -> name-inscribed-pending-dictation`

**Pressure axis: Reality / Frugality (drift-old)**

Proto-line @30 reads "the stylus moves on taylor's name." But @22 already reads "the clerk's stylus follows the dictation" — the clerk is following the officer's dictation of the line (the officer is working the line @20–@22). Proto-line @36 reads "the stylus moves on the line under taylor's name" — which is a distinct motion from @30, suggesting the line-under was already inscribed before @36. If the clerk was actively following dictation at @22 and the officer's dictation was working the line at @20–@22, Taylor's name may have been placed on the ledger at @22 (or earlier, as a pre-written entry the officer is now working through), making @30 a continuation pass or emphasis, not a first-touch. Under §Frugality REJECT, `<old>=absent` is drift-old if the name was inscribed before @30 — and the studio author concedes in the Entry 7 note that @48's calibration anchor phrasing uses `pending` as the pre-dictation state, not `absent`, which implicitly acknowledges the name may have been on the ledger before @30's explicit first-touch claim. If @30 is not the first-touch beat, `<old>=absent` is an anti-pattern #5 violation that corrupts the entire @30→@48→@64 chain.

**Classification: STRONG**

---

### ID-3 — @38 `prop:letter.holder: taylor -> mid-air-between-them`

**Pressure axis: Reality (persistence-test)**

The rubric calibration anchor defends this fire by asserting persistence "across @38–@39 until the officer takes it at @40." But the persistence interval is only 2 beats — @38 to @40 — and the @38/@39 cluster is described by the tensometer as a double-tap (thrust + held-awaiting). Under §Reality, the persistence-test asks whether the field is still at `<new>` two or three beats later. At @40 (two beats later) the holder already flips to `officer`. The argument can be made that `mid-air-between-them` is a transitional posture-state rather than a genuine canonical-value holder, since no card schema defines "mid-air-between-them" as a licit holder value — a prop holder is typically an actor slug or a defined location, not a spatial relational description. If `mid-air-between-them` is not a valid holder value on the prop schema, the entry is an invented-field variant (the holder field's domain may be actor slugs + location slugs, not relational-spatial strings), and the actual holder at @38 is still `taylor` (she extended it but has not released it to a canonical holder).

**Classification: MODERATE**

---

### ID-4 — @40 `prop:letter.holder: mid-air-between-them -> officer`

**Pressure axis: Reality / Frugality (pre-emption)**

Proto-line @40 reads "the officer unfolds the letter" — this is the officer opening the letter, which presupposes receipt. But proto-line @41 reads "the seal breaks at the crease under his thumb" — the breaking is the next beat, which implies the unfold is underway at @40. The actual holder-flip beat is ambiguous: does the holder transfer when Taylor extends (@38), when the officer physically receives it (the gap between @38 and @40), or when he begins to unfold (@40)? If the holder transferred at the moment of receipt — which is between @38 (Taylor extends) and @40 (officer opens it), meaning possibly at @39 — then firing at @40 may be lagging (anti-pattern #7). The rubric's guidance on @43/@45 is explicit that the offer-beat is not the flip-beat; but by that same logic, the unfold-beat (@40) may not be the receipt-beat — the receipt could occur at @39 (the officer reaches for it during the held-against-turn moment). Since @39 is STATE-UPDATE NOTE restricted, this creates a paradox: the receipt may happen at @39 (forbidden) but ID-4 fires it at @40 (one beat late).

**Classification: MODERATE**

---

### ID-5 — @41 `prop:letter.seal-condition: intact -> broken`

**Pressure axis: Authority (prop slug)**

Same prop-slug authority concern as ID-1: `prop:letter` has no card in `cards/props/` and no explicit warehouse-presence record. The studio author notes "implicit warehouse presence." Under §Authority REJECT signatures, if the slug is out-of-card without documented warehouse presence, the entry is rejected regardless of Reality. The calibration anchor references `prop:letter` as though its warehouse presence is established, but anchor examples are not authority documents — they are calibration references. If `prop:letter` requires `oc-letter` or a card in `cards/props/` to satisfy authority, the ACCEPT is conditional, not granted.

**Classification: MODERATE**

---

### ID-6 — @45 `prop:letter.holder: officer -> taylor`

**Pressure axis: Frugality (drift-old chain)**

`<old>=officer` depends on ID-4's validity (@40 `mid-air -> officer`), which in turn depends on ID-3's validity (@38 `taylor -> mid-air`). If ID-3 is culled because `mid-air-between-them` is not a valid holder value (per ID-3 seam), then ID-4's `<old>` is wrong, and ID-6's `<old>=officer` is a drift-old sourced in an invalid intermediate entry. Under §Frugality, drift-old is anti-pattern #5. The entire three-step holder chain (ID-3 → ID-4 → ID-6) is only as strong as its weakest link; a cull of ID-3 propagates forward through the entire chain.

**Classification: MODERATE**

---

### ID-7 — @48 `actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible`

**Pressure axis: Authority (field-extension frugality)**

`administrative-status` is a field-extension on `actor:taylor-hebert-westeros` with no prior state-file baseline — it is new. The field-extension protocol requires (a) extension documented in the entry and (b) the mechanic auditor can defend it under §Reality. The Taylor fork documents it. But the rubric also requires that `<old>` be canonical-correct — verifiable from the most-recent prior state-update on the same field OR from project-setup state if first-touch. For a new field-extension, "first-touch" is @48, and `<old>=child-or-ward` is inferred from the persona card. The hostile read: the persona card may describe Taylor's *narrative identity* or *backstory framing* without that label appearing as a literal field value on her state.md under `administrative-status`. If the state.md does not list `administrative-status: child-or-ward` as a project-open value, then the `<old>` is persona-card inference, not canonical-state-file grounding — the same weakness flagged for ID-14's `mask-state`. The Phase 2 audit gave ID-7 CORRECT while giving ID-14 FLAG on nearly identical grounds, which is an inconsistency the writer must address.

**Classification: STRONG**

---

### ID-8 — @48 `prop:district-ledger.taylor-entry: name-inscribed-pending-dictation -> dictated-provisional`

**Pressure axis: Frugality (chain dependency + drift-old)**

`<old>=name-inscribed-pending-dictation` depends entirely on ID-2 (@30) surviving. The Phase 2 audit verdicts ID-2 as FLAG with explicit language: "if @30 is culled, ID-8's old-value must revert to `pending`." This conditional is load-bearing: the calibration anchor's own phrasing for @48 uses `<old>=pending` (not `name-inscribed-pending-dictation`), indicating the rubric's authoritative source does not recognize the @30 intermediate state as canonical. If the writer-fork defends ID-2 and loses, ID-8's `<old>` becomes a drift-old automatically — no separate fixer pass required, the chain breaks. Under §Frugality REJECT: "Drift-old: `<old>` doesn't match the prior cited canonical value." The rubric explicitly names this scenario.

**Classification: STRONG** (conditional; load is on ID-2's survival)

---

### ID-9 — @57 `studio.doors_and_shutters.cottage-door: closed -> open`

**Pressure axis: Reality + Frugality (drift-old on `<old>`)**

Phase 2 verdicted this INCORRECT-REALITY. The adversarial pressure here is maximal because the entry fails on two axes simultaneously. First, the proto-line "edric steps back through the door" does not require the door to have been closed immediately before @57 — the door may have been ajar or in an unestablished state throughout the scene. Studio's defense that the door was `closed` uses s01e06 state.md as the source, which is a future-session file, not the s01e01 episode-open baseline. Under §Frugality REJECT, this is drift-old (anti-pattern #5). Second, even if `<old>=closed` is granted, the Reality argument is strained: the proto-line may describe Edric stepping through a door that was already open (a door can be "stepped through" while open). The door-open state is an inferred precondition of the crossing, not a directly observed field-change per the proto-line verb. A door-crossing verb is not the same as a door-opening verb; the rubric's ACCEPT signature for Reality names explicit transition verbs ("closes the door," "breaks the seal"), not inferred preconditions of a crossing-verb.

**Classification: STRONG** (already INCORRECT; reinforces mandatory Phase 4 cull or repair)

---

### ID-10 — @57 `actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)`

**Pressure axis: Frugality (`<old>` grounding)**

`<old>=yard (near sept door)` is "traceable from @8 establishing context" per the Phase 2 audit, citing no prior state-update on this field — it is a project-setup baseline assertion. The Edric-fork notes this is "first-touch on his sublocation field for s01e01." But @8 proto-line reads "edric holds his eyes on the road past the cart" — this is gaze direction, not a sublocation establishment. The rubric's approach-zone permitted-silent guidance (§Curve-shape) notes that approach-zone state changes are "usually establishing-state authored at the project-setup baseline, not at proto-line beats." If Edric's sublocation baseline is `yard (near sept door)` and that is established by project-setup (not by @8), then @8 is just the first beat he appears — the claim that his sublocation was specifically `yard (near sept door)` and not `yard (general)` or `near-gate` requires grounding in a project-setup state file, not in the approach-zone proto-line. If `yard (near sept door)` is an assumption rather than a documented project-open state, `<old>` is author-inferred rather than canonical-correct.

**Classification: MODERATE**

---

### ID-11 — @64 `prop:district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`

**Pressure axis: Frugality (chain dependency)**

`<old>=dictated-provisional` is sound only if ID-8 (@48) survives with its `<new>=dictated-provisional`. ID-8 is a conditional FLAG dependent on ID-2 (@30). Therefore ID-11's `<old>` has a two-step chain dependency: ID-2 must be CORRECT and ID-8 must be CORRECT. The calibration anchor grants ID-11 CORRECT by citing the chain `@48: dictated-provisional → @64: marked-parallel-margin` as established — but the anchor pre-assumes ID-8's `<new>` is clean. If ID-2 is culled and ID-8's `<old>` becomes drift-old, then ID-8's `<new>` is also tainted (a corrupted entry cannot produce a reliable `<new>` for the downstream chain). Under the rubric's chain-honor requirement, ID-11 inherits the same chain risk as ID-8 and ID-2. The calibration anchor cannot absolve a chain that is seeded incorrectly upstream.

**Classification: MODERATE**

---

### ID-12 — @64 `actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`

**Pressure axis: Reality (knowledge field persistence)**

`actor:taylor-hebert-westeros.knowledge.record-state` is described as the POV character's knowledge of what is on the ledger. But knowledge is only a licit state-update if it is an irreversible acquisition — the rubric §Reality states "irreversible bureaucratic / record / knowledge events strongly expect a state-update entry." The hostile read: Taylor perceiving the parallel marks is a perception event (narrator-interest's territory per the cross-facet note at @38/@39 — "narrator-interest entries are registration-class only"). The claim that this is *knowledge-acquisition* (irreversible field-flip) rather than *perception* (registration) requires the defender to show that Taylor's knowledge of the record-state prior to @64 was genuinely `name-on-line-provisional` as a tracked value, not simply an inferred belief. If knowledge is tracked only when it is epistemically certain, and Taylor's pre-@64 belief about her entry state could have been `uncertain` or `unconfirmed` rather than `name-on-line-provisional`, then `<old>=name-on-line-provisional` is character-inference, not state-file grounding — the same issue as ID-7 and ID-14.

**Classification: MODERATE**

---

### ID-13 — @68 `prop:district-ledger.physical-condition: unrolled -> folded-or-stored`

**Pressure axis: Reality (verb precision + prop slug)**

Proto-line @68 reads "the clerk folds the board." Studio chose to treat board-folding as district-ledger physical-condition closure, but the studio author explicitly acknowledges "the board is distinct from the ledger." If the board is distinct from the district ledger, then the field that changes at @68 is `prop:clerks-board.physical-condition`, not `prop:district-ledger.physical-condition`. Firing on the wrong target is an authority/reality violation: the district ledger's physical condition (unrolled parchment) may or may not change at @68 as a direct consequence of the board being folded — the board folding does not require the parchment to be simultaneously re-rolled. These are potentially two distinct events on two distinct props, and collapsing them into one entry on the wrong target (the ledger rather than the board) is a compound-entry variant (anti-pattern #4) or a wrong-target fire.

**Classification: STRONG**

---

### ID-14 — @77 `actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private`

**Pressure axis: Reality (persistence past @77)**

`<new>=mask-thinned-private` is described as persisting into s01e02 — the fork asserts "mask could be re-engaged when Taylor interacts with others inside the sept" as a caveat but claims persistence is "plausible but not guaranteed." The rubric requires persistence to be actual, not plausible: §Reality states "persistent — the field stays at `<new>` until something else changes it." If it is conceded that the mask-state may re-engage when Taylor encounters others inside the sept (which @77 describes as a crossing-into, not an empty-room arrival), and if @77 is the door-crossing beat while the sept interior may contain other people (including Edric, who just went through the same door at @57 and is in the sept interior), then `mask-thinned-private` may not persist even one beat past @77 — Taylor entering a space where Edric is present may immediately re-engage the mask. The persistence-test failure (§Reality cross-axis test) would cull the entry: a state that reverts within the same beat or immediately after is a transient, not a state-change.

**Classification: STRONG**

---

## 2. Refusal Fire-Justification Seams

These are the strongest arguments that the rubric DOES warrant a fire at each defended NONE. The writer must articulate why the floor-defense holds against these.

### T1 — @39 (Taylor feet-set)

**Fire justification:** The tensometer STATE-UPDATE NOTE says "any co-citation here must be actor-posture only; pure registration class." This prohibits *canonical state-change* but explicitly permits *actor-posture co-citation*. The Taylor fork interpreted "canonical state does not change at @39" as a total refusal, but the note allows a posture entry. `actor:taylor-hebert-westeros.posture: in-line -> feet-set-at-commit-threshold` is a posture entry, not a canonical-state entry, and the STATE-UPDATE NOTE explicitly licenses it. The fork chose refusal over the permitted posture-fire — but the rubric calibration anchor at @38 says "fire `actor:taylor.posture` once across @38–@39 if persistent; do not double-fire." If @38 is the posture-fire beat (the calibration anchor cites @38 as the body-reach / presenting-letter beat), then @39 is the sustained-hold of that posture — which is the persistence that makes it posture-state rather than transient. Under the calibration anchor's own language, a posture fire spanning @38–@39 is explicitly modeled. Did the Taylor fork decline the only posture-fire the rubric explicitly licenses for this episode's climax?

**Classification: MODERATE**

---

### T4 — @50 (Taylor turns to Mira)

**Fire justification:** The rubric's REJECT signature for @50 is phrased as: "turning is a momentary directional shift, not a persistent posture change." But the fork's own anti-pattern check notes that Taylor's orientation does not persist to @54 (she turns to Edric). The period @50–@53 is four beats during which Taylor faces Mira and speaks to her (two beats: @51 speaks to Mira, @52 Mira drops her eyes, @53 Mira holds her eyes). Four beats of maintained orientation — including two speech acts directed at Mira — satisfies the rubric's persistence-requires-multi-beat condition: "If she turns and then *stays* facing mira for several beats while doing something else, the persistent orientation IS a posture state." Taylor speaks to Mira at @51, waits while Mira responds at @52/@53 — that is at minimum three beats of maintained orientation before @54. Under the rubric's own exception clause, this is not a transient turn; it is a multi-beat maintained posture.

**Classification: MODERATE**

---

### T5 — @52 (Mira eyes to flagstones)

**Fire justification:** The fork correctly refused on cross-POV grounds for `actor:mira.*`. But the fire-justification seam presses a different target: `actor:taylor-hebert-westeros.knowledge.ally-disposition`. The narrator-interest @52 fire is "mira's eyes are on the flagstones and the count of allies in the yard drops to one" — this is Taylor's knowledge of her ally-count, not a Mira-state entry. The rubric models `actor:taylor-hebert-westeros.knowledge.*` entries as licit (see ID-12 for the knowledge.record-state pattern). A `actor:taylor-hebert-westeros.knowledge.ally-count: two -> one` entry at @52 targets Taylor's own state, not Mira's — and narrator-interest @52 fires, satisfying the POV co-citation requirement. The fork refused on the basis that "count-of-allies-as-Taylor-sees-it is not a tracked field" (citing the rubric's REJECT signature), but the REJECT signature says it is "not a tracked field" generically — this is the reality-axis defense, not the authority defense. The fire-justification argues that the field IS tracked in the `knowledge.*` namespace, where Taylor's operational awareness of her ally-count is exactly the kind of irreversible situational-knowledge shift the knowledge namespace exists to record.

**Classification: STRONG**

---

### S6 — @43 (studio door-close pre-emption)

**Fire justification:** The calibration anchor says "@43 (the offer)" is the offer beat, not the flip-beat, and firing on @43 is pre-emption of @45. This is correct for `prop:letter.holder`. But the fire-justification seam targets a different field: the @43 beat is described as "the officer holds the letter out to taylor" — under @43's tensometer 2 annotation ("stakes-visibility: officer's decision externalized; letter-return registers outcome"), the officer's physical orientation toward Taylor and his decision-externalization may represent a persistent change in the *interaction-state* of the scene (the officer is no longer examining the letter; he is extending it). A `studio.spatial_layout.officer-orientation: facing-letter -> facing-taylor-letter-extended` entry (or an actor-position field for the officer, if the officer fork were active) could be argued as a real environmental state change that the confrontation cluster produced. Studio's refusal was correct for `prop:letter.holder` but may have missed a studio-domain spatial state change.

**Classification: THIN**

---

### S5-close — @57 (cottage door close)

**Fire justification:** The studio refusal is based on "no proto-line evidence door closes at @57." But the proto-line reads "edric steps back through the door" — "steps back" implies a return motion (toward/into the cottage), and the cultural/physical convention of someone stepping back through a door (entering an interior space from a yard) includes the door's closure as the natural completion of the action. More pointedly, the Edric-fork's own entry establishes his destination as "sept interior (past threshold)" — past threshold implies the threshold has been crossed and the door has closed behind him. The rubric's calibration anchor explicitly models `studio.doors_and_shutters.cottage-door: open -> closed` as the expected entry "if the proto-line file establishes that the door closed." The anchor treats this as a conditional, not a prohibition. Under a generous proto-line reading, "steps back through the door" plus the Edric destination "past threshold" is sufficient establishment of a door-close at @57. The studio chose the strict reading; the defender must argue why the strict reading is required.

**Classification: MODERATE**

---

### F1 — @45 (Taylor inventory, withdrawn)

**Fire justification:** The Taylor fork withdrew F1 because narrator-interest fires at @43, one beat before the @45 flip-beat, and the co-citation requirement is for the exact `@<beat>`. But the rubric's co-citation requirement is phrased as: "narrator-interest co-citation on the same beat is REQUIRED." The @43 narrator-interest fire ("the letter returns by hand; the officer's mark is on it now") narratively describes the return process that culminates at @45 — it is a fire on the letter-return arc, not specifically on the @43 beat as distinct from @45. If narrator-interest @43 is understood as covering the return envelope (@43-@45) rather than the single @43 beat, the co-citation requirement is met for @45. The rubric's exact-beat requirement is strict; but the fork's reasoning for withdrawal was that narrator-interest is "one beat off," which assumes the envelope reading is invalid. The defender must articulate why the exact-beat rule is non-negotiable when the NI fire's semantic content spans the return arc.

**Classification: MODERATE**

---

### F3 — @23 (Taylor exposure-state)

**Fire justification:** The fork refused `actor:taylor-hebert-westeros.exposure-state` at @23 on registration-as-state grounds, citing the rubric's explicit @23 REJECT signature. But the REJECT signature in the rubric names the officer's gaze as the non-state-changing element: "the officer's gaze is a registration, not a posture-state." It does not definitively rule out a change in Taylor's exposure-state. Taylor's exposure-state *as a tracked field* — distinct from the officer's perception — could genuinely flip at @23: before @23 Taylor is one person in a line (anonymous exposure-level); after @23 the officer has specifically targeted her by name-proximity (the stylus stops, @24). If `actor:taylor-hebert-westeros.exposure-state: in-line-anonymous -> officer-targeted` is a persistent change (it does persist — she is specifically in the officer's attention from @23 onward), it passes the persistence-test. The narrator-interest @23 fire ("the watch-cost has just been priced to her name") is a POV co-citation, satisfying the POV requirement. The Reality-axis question is whether being targeted constitutes a field-change or merely a registration; the fork ruled registration, but the persistence argument is real.

**Classification: MODERATE**

---

## 3. SKIP-MISSED Seams

### SM-1 — @77 `actor:taylor-hebert-westeros.sublocation` (or position): yard -> sept-interior

**Seam:** The Taylor fork authored a mask-state entry at @77 (ID-14) but did not author a sublocation entry at the same beat, despite the identical pattern used by the Edric-fork at @57 (edric.sublocation entry on a door-crossing beat). The rubric's file-level curve check specifies "at least one fire per scene-with-irreversible-event" — Taylor crossing the sept threshold at @77 is a persistent location-change that the Edric-fork's @57 entry establishes as the correct entry-pattern for a door-crossing. Narrator-interest @77 fires ("inside the frame"), satisfying the POV co-citation requirement. The failure to write `actor:taylor-hebert-westeros.sublocation: yard -> sept-interior` at @77 mirrors the exact field and event pattern that earned Edric's @57 entry a CORRECT verdict. The seam: the Taylor fork chose mask-state at @77 but did not also write the sublocation entry that the episode's own fire-pattern (ID-10) establishes as the standard for a door-crossing. Why does Taylor's threshold-crossing fail to earn the same fire-class as Edric's?

**Classification: STRONG**

---

### SM-2 — @57 `studio.doors_and_shutters.cottage-door: open -> closed`

**Seam:** The studio fork withheld the door-close entry at @57 on proto-line-evidence grounds, and the Phase 2 audit accepted that floor-defense. But the seam presses the alternative: the door-close is not a separate unanchored event — it is the second half of the same @57 proto-line ("edric steps back through the door"). The door cannot be in the `open` state at write-back if the canonical state.md records it as `closed` and the only write-back mechanism is this file. The studio fork left `studio.doors_and_shutters.cottage-door: open` in the write-back, creating a canonical corruption that its own @57 door-open entry (ID-9) initiated. Even if the door-open entry survives Phase 4 repair (by establishing `<old>` from the correct s01e01 baseline), the absence of a door-close entry means the cottage-door is `open` at episode end — a known contradiction with the state.md. The studio's refusal to fire the close is rubric-defensible per the strict proto-line-evidence rule, but it creates a write-back gap that no other entry in the file can close. The write-back gap IS the seam: the studio correctly applied the rubric and produced a canonical corruption.

**Classification: STRONG**

---

## 4. File-Level Seam

**Target: prop-target concentration / studio.* undercoverage**

The file contains 10 prop entries vs. 1 studio entry. The single studio entry (ID-9, @57 cottage-door) is the file's only INCORRECT-REALITY verdict. Across 77 beats, the studio environment produces exactly one fire that fails. The rubric's target-diversity requirement specifies that across an episode of >50 beats, entries should appear across "at least three target classes: studio.*, prop:*.*, at least one actor:*." The file nominally satisfies three classes but with extreme imbalance: 1 studio / 10 prop / 4 actor (including the SKIP-MISSED SM-1). The 1 studio entry that does fire is the file's only INCORRECT entry, which means the studio.* target class has a 0% CORRECT rate. The hostile attack: if the only studio.* entry is invalid, the file has effectively zero verified studio.* fires, reducing real target diversity to 2 classes (prop + actor). The rubric requires at least 3. Additionally, the tensometer file shows 11 beats with tens≥2 between @23 and @64 — only 5 state-update fires occur in that range, and no studio.* entry survives that cluster. A 77-beat episode in an outdoor yard environment should produce at least one verifiable environment-state change beyond a door; the file's studio coverage is structurally inadequate.

**Classification: STRONG**

---

## 5. Curve-Level Seam

**Target: @9–@30 gap (21-beat dark zone) and pre-peak sparsity**

The tensometer file shows @23 and @30 as 2-rung beats (stakes-visibility + reversal-proximity). Both are in the confrontation cluster — the rubric's curve-shape specifies that "Density alignment with tensometer transitions and peaks" concentrates fires around 2-rung and 3-rung clusters. Between @9 (the first ledger unroll) and @30 (the first taylor-entry fire), there is a 21-beat gap in the state-updates file during which two tens=2 beats occur (@23 and @30 itself). The @30 entry closes the gap but is the only fire in the @23–@30 sub-window. The rubric states "no entries between @9 and @30 on a 30-beat span; is approach really that silent?" — and the phase dispatch identifies this as a candidate file-level seam. More sharply: the tensometer file shows @24 as a 3-rung beat (the stylus stops — the rubric's calibration anchor for @24 explicitly argues NONE). But @24=3 in tensometer is the episode's third peak (first rupture), and yet the state-updates file is entirely silent at @24. Under the curve-shape rule, "at least one fire per scene-with-irreversible-event" — if @24 (stylus-stops, 3-rung, registered rupture) is treated as a scene-with-irreversible-event, the absence of any state-update fire at or near @24 is a curve-shape gap. The file concentrates 5 of its 13 entries in the narrow @38–@48 band (10 beats) and covers the 21-beat @9–@30 run with only 1 entry (@30, which is a FLAG). The curve is front-light and center-heavy in a way the rubric's density-alignment requirement presses against.

**Classification: MODERATE**

---

## 6. Triage Classification Summary

| Seam | Type | Classification |
|------|------|----------------|
| ID-1 (prop-slug authority) | Per-entry | STRONG |
| ID-2 (@30 drift-old) | Per-entry | STRONG |
| ID-3 (@38 mid-air holder validity) | Per-entry | MODERATE |
| ID-4 (@40 pre-emption vs lagging) | Per-entry | MODERATE |
| ID-5 (letter prop-slug authority) | Per-entry | MODERATE |
| ID-6 (chain collapse risk) | Per-entry | MODERATE |
| ID-7 (@48 admin-status `<old>` vs ID-14 inconsistency) | Per-entry | STRONG |
| ID-8 (@48 chain dependency) | Per-entry | STRONG |
| ID-9 (@57 door-open drift-old + reality) | Per-entry | STRONG |
| ID-10 (@57 edric `<old>` grounding) | Per-entry | MODERATE |
| ID-11 (@64 chain dependency) | Per-entry | MODERATE |
| ID-12 (@64 knowledge vs perception) | Per-entry | MODERATE |
| ID-13 (@68 board vs ledger target) | Per-entry | STRONG |
| ID-14 (@77 mask-state persistence) | Per-entry | STRONG |
| T1 (@39 posture-fire licensed) | Refusal-fire-justification | MODERATE |
| T4 (@50 multi-beat persistence) | Refusal-fire-justification | MODERATE |
| T5 (@52 knowledge.ally-count) | Refusal-fire-justification | STRONG |
| S6 (@43 studio spatial-state) | Refusal-fire-justification | THIN |
| S5-close (@57 door-close proto-line reading) | Refusal-fire-justification | MODERATE |
| F1 (@45 NI envelope reading) | Refusal-fire-justification | MODERATE |
| F3 (@23 exposure-state persistence) | Refusal-fire-justification | MODERATE |
| SM-1 (@77 taylor sublocation) | SKIP-MISSED | STRONG |
| SM-2 (@57 door-close write-back gap) | SKIP-MISSED | STRONG |
| File-level (studio.* undercoverage) | File-level | STRONG |
| Curve-level (@9–@30 gap, @24 silence) | Curve-level | MODERATE |

**Tier counts:**
- STRONG: 11 seams (ID-1, ID-2, ID-7, ID-8, ID-9, ID-13, ID-14, T5, SM-1, SM-2, File-level)
- MODERATE: 13 seams (ID-3, ID-4, ID-5, ID-6, ID-10, ID-11, ID-12, T1, T4, S5-close, F1, F3, Curve-level)
- THIN: 1 seam (S6)

**Total seam count: 25**
