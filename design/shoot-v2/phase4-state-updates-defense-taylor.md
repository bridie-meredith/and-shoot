# Phase 4 — State-Updates Defense (Taylor fork)

Author: dialogue-writer fork for `taylor-hebert-westeros`, defense/revise mode
Episode: s01e01
Scope: `actor:taylor-hebert-westeros.*` entries only
Authority: V2 locked rubric (`design/shoot-v2/rubric-state-updates.md`); locked tensometer; locked narrator-interest
Inputs reviewed: Phase 2 output (own); Phase 2 audit; Phase 3 seams (ID-7, ID-12, ID-14; T1, T4, T5, F1, F3; SM-1)

---

## 1. Per-entry defense / revise / cull

### ID-7 — @48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible

DECISION: **REVISE** (refine `<old>`); fire holds.

Phase 3 seam (STRONG, Authority / field-extension frugality): `<old>=child-or-ward` is persona-card inference rather than canonical-state grounding. Phase 2 audit gave ID-7 CORRECT while flagging ID-14 on near-identical grounds (persona-card-inferred `<old>` for a new field-extension). The inconsistency must be addressed.

Defense scaffold:
- The fire itself is locked-rubric calibration anchor — §"Calibration anchors" s01e01:48 explicitly authorizes `actor:taylor.administrative-status: child-or-ward -> provisional-labor-eligible`. The fire stands.
- The field-extension is licit per §"Field-extension protocol": `administrative-status` is a tracked-state-aspect (administrative classification), persistent past the beat, season-arc-load-bearing. Documented in field-extension note. Defensible.
- The `<old>` baseline question: rubric §Form requires `<old>` to be "verifiable from the most recent prior state-update on the same field, OR from project setup state if first-touch." For a project-setup baseline on a new field-extension, the persona card IS the project-setup source of truth — there is no other authority for the project-open value of a field that is being introduced for the first time. The persona card establishes Taylor as an unenrolled child entering this census event for the first time.

Refinement: the calibration anchor in the rubric uses `child-or-ward` precisely; the value matches the calibration anchor verbatim. However, to harden against the seam, the entry stays `child-or-ward` (rubric-anchor phrasing) AND the field-extension note is sharpened to make the project-setup grounding explicit (not just asserted). The `<old>` is the calibration-anchor value; its grounding is the persona card as project-setup baseline, which is the licit source per §Form for first-touch field-extensions.

Consistency with ID-14: ID-7 and ID-14 are now treated identically — both are first-touch field-extensions on actor:taylor whose `<old>` is grounded in the persona card as project-setup-baseline. Phase 2's asymmetric treatment was the error; both should carry the same field-extension-baseline note. ID-7 holds; ID-14 holds; the inconsistency is resolved by harmonizing the documentation, not by culling either.

DEFENDED entry (unchanged, with hardened note): `@48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible`
Field-extension baseline: persona-card project-setup state (Taylor as unenrolled child under Septon Osmynd's informal protection, never formally administratively classified prior to s01e01 census).

---

### ID-12 — @64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks

DECISION: **DEFEND** (with conditional `<old>` hardening if @30/@48 chain mutates).

Phase 3 seam (MODERATE, Reality / knowledge field persistence): the seam pressures whether `name-on-line-provisional` is genuinely Taylor's tracked knowledge prior to @64 or merely an inferred belief. Also raises the chain-dependency from ID-2 → ID-8 → ID-12 (ID-12's `<old>` references the post-@48 state, which depends on the studio chain).

Defense:
- This is the rubric's calibration anchor for s01e01 — §"Calibration anchors" s01e01:64 explicitly authorizes the entry verbatim. Highest-stakes Taylor-fork entry; survives.
- Reality axis: the rubric §Reality says "irreversible bureaucratic / record / knowledge events strongly expect a state-update entry." Taylor's perception of the parallel marks at @64 is not transient registration — it is irreversible knowledge-acquisition. She cannot un-know the marks once she has seen them. The strip-test passes: without this entry, her knowledge field at the next beat would be wrong (state.md would record her as unaware of the parallel marks; she demonstrably is aware, and that awareness is load-bearing for the s01e01 close + s01e02 mask-state reasoning).
- Persistence-test passes: the knowledge persists absolutely; there is no future beat where she un-knows the determination is recorded.
- Cross-facet: tensometer @64=3 with locked STATE-UPDATE NOTE "co-citation strongly expected — irreversible registration." Narrator-interest @64 fires (`two strokes; the determination is on the record and on her`). POV co-citation requirement satisfied. The entry honors the strongest cross-facet contract slot in the file.
- Knowledge-vs-perception distinction: rubric §Reality and §"Field-extension protocol" name `knowledge` as a tracked-state-aspect explicitly. The seam's "this is perception not knowledge" attack mis-reads the rubric — the rubric distinguishes registration (perception of a non-state-changing event, e.g., officer's gaze @23) from knowledge-acquisition (perception of an irreversible state-mutation). @64 is the latter. Taylor perceiving the parallel marks IS knowledge-acquisition because the marks are themselves an irreversible canonical event (ID-11 prop:district-ledger fires on the same beat). The POV-knowledge of an irreversible canonical event is itself irreversible knowledge.

`<old>` chain dependency: `name-on-line-provisional` is Taylor's knowledge-state after @48 (the dictation). This depends on ID-7 (administrative-status fire) and the studio chain (ID-8 ledger.taylor-entry: pending → dictated-provisional). ID-7 holds (defended above). If the studio chain on ID-2/ID-8 is revised at Phase 4 such that `<new>` at @48 changes phrasing (e.g., from `dictated-provisional` to `pending` or other), ID-12's `<old>` should track the studio chain's @48 `<new>` state. Conservative position: hold the rubric calibration anchor's exact phrasing (`name-on-line-provisional`), which the rubric authoritatively names; if the studio chain forces a phrasing change, accept that as a downstream chain-honor. The fire itself does not mutate.

DEFENDED entry: `@64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`

---

### ID-14 — @77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private

DECISION: **DEFEND** (Phase 2 FLAG → Phase 4 defended; persistence-test addressed).

Phase 3 seam (STRONG, Reality / persistence past @77): the seam claims `mask-thinned-private` may not persist if Taylor enters a sept interior containing Edric (who passed through at @57). If mask re-engages within one beat, the entry is transient.

Defense:
- The behavior pack §"Voice tells / Mask-thinning at Septon Aldric proximity" treats mask-thinning as a tracked behavioral state, not just a perception. The persona card licenses mask-state as a maintained-performance under cost; the release is a real state-shift.
- Field-extension is licit: §"Field-extension protocol" explicitly names `mask-state` in its example list of tracked-state-aspects.
- Cross-facet: narrator-interest @77 fires (`inside the frame her hand has stopped reaching for the half-curtsy`) — POV co-citation satisfied. The narrator-interest content is *specifically* mask-thin content (the half-curtsy is the cooperative-child performance gesture; her hand stopping reaching for it IS the mask-thin moment). The narrator-interest fire is co-citation evidence that the mask-state shift is the canonical event of @77, not an incidental.
- Persistence-test (the seam's main pressure): two responses.
  1. The sept interior at @77 is not yet established as containing Edric in Taylor's perceived field. Edric crossed at @57 and is in the sept interior, but @77 is the door-crossing beat — narrator-interest @77 is `inside the frame`, the half-curtsy stops reaching, which is the cooperative-child release. The release is the @77 beat's content. Whether Taylor re-engages mask later in the sept (s01e02 territory) does not retroactively make the @77 release transient.
  2. The rubric's persistence-test reads forward "two or three beats" — within s01e01 (which closes at @77 or shortly after), there are no further beats where mask re-engages. The episode-close state IS mask-thinned-private. Continuity-honored to s01e02: the next-episode showrunner sees the state at episode close as mask-thinned-private; if s01e02 opens with a re-engagement, that's an s01e02 fire, not retroactive invalidation of the s01e01 fire. The rubric §Reality says "the field stays at `<new>` until something else changes it" — within s01e01, nothing changes it. The persistence-test passes for the in-episode window.
- The Phase 2 audit FLAG was on `<old>` baselining (persona-card inferred). That is now harmonized with ID-7 (above): both are first-touch field-extensions whose `<old>` is the persona-card project-setup baseline, the licit source per §Form for first-touch.

DEFENDED entry: `@77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private`

---

## 2. Refusal seam responses

### T1 — @39 (feet-set, defended NONE)

Phase 3 fire-justification (MODERATE): the tensometer STATE-UPDATE NOTE permits actor-posture co-citation at @39 even while forbidding canonical state-update; the calibration anchor at @38 models a posture-fire spanning @38–@39; did the fork miss the licensed posture-fire?

Response: **Refusal HOLDS, with explicit acknowledgment of the cross-author convention.**

The rubric calibration anchor §s01e01:38 specifies: "fire `actor:taylor.posture` once across @38–@39 if persistent; do not double-fire." This means a single posture entry CAN be authored — but on @38, not @39. The locked tensometer @39 STATE-UPDATE NOTE permits actor-posture co-citation; it does not require it. The locked tensometer @38 annotation is where the posture-fire would land per the calibration anchor's "fire once across @38–@39" guidance.

The Taylor fork did not author a posture entry at @38 either, which the seam (correctly) presses as a possible omission. Re-evaluation:
- A `@38 actor:taylor-hebert-westeros.posture: in-line -> presenting-letter-extended` entry would be locally licit per the calibration anchor.
- However: the calibration anchor frames the @38 posture-fire as conditional ("if persistent" and "load-bearing for @40 unfolding"). The posture resolves at @40 when the officer takes the letter and Taylor's hand returns. The persistence window is @38 → @40 (two beats). Under §Reality persistence-test ("two or three beats"), this is borderline.
- The calibration anchor also names the `prop:letter.holder` fire on @38 as the alternative: "**Two entries are licit, one each.**" The studio fork authored the prop:letter.holder fire at @38 (ID-3). Per anchor convention "fire actor:taylor.posture once across @38–@39 if persistent; do not double-fire" — this reads as "if the posture is fired, fire once not twice across the cluster." It does NOT mandate firing the posture; it constrains how to fire if firing.
- The Taylor fork's choice to forgo the posture-fire at @38 is conservative-defensible: the prop holder chain already captures the structural delta at @38; adding a posture entry that resolves within two beats risks anti-pattern #8 (posture-as-state) and anti-pattern #9 (density-on-flat at the cluster).

Refusal at @39 specifically: **holds firmly.** Tensometer @39 STATE-UPDATE NOTE: "canonical state does not change at @39." A posture entry at @39 specifically would either duplicate a hypothetical @38 entry (forbidden by anchor: "do not double-fire") or be an isolated @39 entry (forbidden by note: posture-only, and the body-charge resolves at @40 not @39 — the @39 feet-set is registration of held-against-turn). Refusal-CORRECT.

T1 verdict: **Refusal HOLDS at @39.** The @38 posture-fire is not authored; this is conservative-defensible per anchor's "if persistent" qualifier and the cluster's borderline persistence window.

---

### T4 — @50 (turns to Mira, defended NONE)

Phase 3 fire-justification (MODERATE): four-beat maintained orientation (@50 turns, @51 speaks to Mira, @52 Mira drops eyes, @53 Mira holds eyes) with two speech acts may satisfy the rubric's "stays facing for several beats while doing something else" exception.

Response: **Refusal HOLDS, with re-grounded reasoning.**

The seam's read of "four beats of maintained orientation" overstates the persistence:
- @50 turns to Mira (the turn-verb itself, rubric REJECT signature for transient).
- @51 speaks to Mira (orientation incidental to speech act).
- @52 Mira drops her eyes (Mira's beat, not Taylor's posture).
- @53 Mira holds her eyes (Mira's beat).
- @54 Taylor turns to Edric — orientation flips.

The rubric's exception ("stays facing for several beats while doing something else") requires the orientation to be load-bearing — to enable a subsequent move that depends on the posture's persistence. Taylor turns to Mira to speak; the speech is the load. Once @51 finishes the speech, the orientation continues only because she is awaiting Mira's response (@52, @53). At @54 she turns to Edric — the orientation does not persist past the conversational beat that motivated it.

More importantly: the rubric REJECT signature for @50 is named explicitly: "*taylor turns to mira* (@50) — turning is a momentary directional shift, not a persistent posture change." The rubric pre-adjudicates this beat as a REJECT signature. The fork's refusal honors the rubric's named signature; reversing it would require overruling the rubric's explicit calibration. Floor-defense.

Additionally: tensometer @50=1, narrator-interest silent at @50. No cross-facet pressure to fire. No co-citation available even if a posture entry were attempted (POV actor-state requires narrator-interest co-citation; absent at @50).

T4 verdict: **Refusal HOLDS at @50.**

---

### T5 — @52 (Mira eyes to flagstones, defended NONE)

Phase 3 fire-justification (STRONG): the seam re-targets from `actor:mira.*` (cross-POV trap, correctly refused) to `actor:taylor-hebert-westeros.knowledge.ally-count: two -> one`. Knowledge-namespace is licit (per ID-12 pattern); narrator-interest @52 fires; POV co-citation satisfied.

Response: **Refusal HOLDS, but the seam is real and warrants explicit rubric-citation.**

This is the strongest refusal-seam in the dispatch. The defense:
- The rubric REJECT signature for @52 is named explicitly: "*the count of allies in the yard drops to one* (narrator-interest @52) — this is Taylor's *perception* of an ally count. The canonical state of `actor:edric.position` may change at @57... the *count-of-allies-as-Taylor-sees-it* is not a tracked field."
- The seam's argument that `knowledge.ally-count` IS a tracked field in the `knowledge.*` namespace presses against this REJECT signature. The rubric's response: tracked-state-aspects in §"Field-extension protocol" name knowledge, mask-state, exposure-state, posture, inventory — these are tracked-state aspects. But the rubric's REJECT signature for @52 names the ally-count specifically as not a tracked field, which is a specific carve-out within the knowledge namespace.
- Why the carve-out: ally-count-as-Taylor-perceives is a derived quantity over other actors' engagement-states. It is not a primary knowledge field; it is a roll-up of perceptions of others. The rubric §POV-restriction names this exact pattern: "Taylor's narrator-interest fire registers her *perception* of Mira's disengagement; the canonical `actor:mira.engagement-state` field-change (if any) is the Mira fork's authority, not Taylor's." A `actor:taylor.knowledge.ally-count` entry would require Taylor's fork to read the canonical state of `actor:mira.engagement-state` (which it cannot author), then derive a count from it. This is an indirect cross-POV authoring — the count is a function of Mira's state, which is the Mira fork's authority.
- Contrast with ID-12 (`knowledge.record-state`): the record-state is a knowledge of an irreversible canonical event on a prop (the ledger). The prop is studio's domain; Taylor's knowledge of the prop-state is licit because it is knowledge of an irreversible canonical mutation, not a roll-up of other actors' states. ID-12 is licit; the @52 ally-count entry is not.
- Persistence question: Mira's eyes-on-flagstones at @52 is a momentary registration (she may look up later in the conversation; the engagement-state is not necessarily a persistent canonical mutation — that is the Mira fork's call, not Taylor's). The persistence-test on a derived ally-count cannot pass because the underlying state (Mira's engagement) is not Taylor's to determine.

T5 verdict: **Refusal HOLDS at @52.** The knowledge-namespace re-target is a rubric REJECT signature carve-out (ally-count is named-as-not-tracked), and the field would be an indirect cross-POV authoring violating §POV-restriction.

---

### F1 — @45 (inventory, withdrawn)

Phase 3 fire-justification (MODERATE): narrator-interest @43 may cover the return-envelope (@43–@45) rather than only the @43 single-beat; co-citation requirement may be met under the envelope reading.

Response: **Withdrawal HOLDS.**

The cross-facet contract on POV actor-state requires narrator-interest co-citation on the **exact `@<beat>`**. Rubric §Cross-facet contract: "every `actor:<POV>.*` entry pairs with a narrator-interest entry on the same beat." The exact-beat rule is non-negotiable because:
- The mechanic auditor's check is per-beat; envelope readings introduce ambiguity that cannot be mechanically validated.
- Narrator-interest @43 fires on `the letter returns by hand; the officer's mark is on it now` — the content is the return-arc registration at the offer-beat (@43), not specifically the palm-closing receipt-beat (@45).
- The rubric's calibration anchor §s01e01:43→@45 explicitly distinguishes: "Fire on @45 (the flip-beat), not @43 (the offer)." The studio prop-side fires at @45. If the rubric models @43 as the offer (not the flip), then narrator-interest @43 is a fire on the offer beat, not the flip beat. The flip beat (@45) is narrator-interest-silent.
- Verification of NI silence at @45: per Phase 3 dispatch and Phase 2 audit confirmation, narrator-interest @45 does not fire. Co-citation on the exact flip-beat is unmet.
- Schema design tradeoff: Phase 2 audit flag-004 explicitly names this as advisory-only — Taylor's inventory at @45 can be inferred from `prop:letter.holder` (studio's @45 fire); the actor-side entry would be a duplicate write on a derivable field, and the cross-facet contract rejects it for lack of POV co-citation.

F1 verdict: **Withdrawal HOLDS.** The envelope-reading attempt does not overcome the rubric's exact-beat requirement; the prop-side studio entry captures the canonical mutation; the actor-side inventory is derivable but unauthored at the actor-level.

---

### F3 — @23 (exposure-state, refused)

Phase 3 fire-justification (MODERATE): `actor:taylor-hebert-westeros.exposure-state: in-line-anonymous -> officer-targeted` may be a persistent field-change (Taylor remains in the officer's specific attention from @23 onward), with narrator-interest @23 fire as POV co-citation.

Response: **Refusal HOLDS, with explicit re-evaluation.**

The seam is non-trivial. Re-evaluation:
- Persistence: Taylor IS specifically in the officer's attention from @23 onward through the climax cluster. The targeting persists. The persistence-test would pass.
- Cross-facet: narrator-interest @23 fires (`the watch-cost has just been priced to her name`); POV co-citation requirement met.
- Authority: `exposure-state` is a rubric-named tracked-state-aspect in §"Field-extension protocol." Field-extension is licit.

The seam's strongest argument is that the entry passes Reality and Authority. Why does the refusal hold?
- Rubric REJECT signature for @23 is named explicitly: "*the officer's gaze fixes on taylor at the yard's far end* (@23) does not change a field on `actor:officer` (his gaze is a registration, not a posture-state); it is narrator-interest territory, not state-updates." The REJECT signature is on the officer's gaze; the seam re-targets to Taylor's exposure-state (a symmetric reframe).
- The symmetric reframe is itself an anti-pattern variant: registration-as-state shifted to the perceiver (anti-pattern #1 perception-side-effect-as-state, named in REJECT signatures). Taylor's exposure is a function of being-perceived; perceiving-the-being-perceived is registration. The narrator-interest fire IS the registration. The state-update would be parasitic — the field that "changes" is the registration of the change.
- The rubric §Reality cross-axis test: "Strip the entry: if the field on the target would still be in the `<new>` state at the next beat without this entry having fired, the entry is parasitic." Taylor's exposure-state at @24 is officer-targeted regardless of whether ID-F3 fires — the targeting is established by the gaze-event (a narrator-interest registration), not by an entry on Taylor's state. The strip-test fails for ID-F3.
- Counter: doesn't this also apply to ID-7 (administrative-status)? No — ID-7 fires on a verbal dictation that creates a record-state (`prop:district-ledger.taylor-entry` flips canonically); the actor-side administrative-status flips because the record-state flips. There is an anchor canonical mutation (the ledger entry). For F3, there is no anchor canonical mutation — only the officer's gaze, which is registration. The exposure-state flip would have no anchor canonical mutation; it would be self-anchored on registration.
- The exposure-shift that has a real canonical anchor lands at @48 (the dictation creates the formal exposure as labor-eligible) — and that is captured by ID-7. The @23 exposure is registration-only; the @48 exposure is the canonical shift. ID-7 already covers the structural-delta arc.

F3 verdict: **Refusal HOLDS at @23.** Strip-test fails; symmetric reframe is registration-as-state on perceiver; the canonical exposure-shift is ID-7 at @48.

---

### SM-1 — @77 actor:taylor-hebert-westeros.sublocation (skip-missed)

Phase 3 SKIP-MISSED (STRONG): Phase 2 audit identified this as fault-002. The Edric-fork's @57 entry establishes the door-crossing → sublocation pattern as the standard; Taylor's @77 threshold-crossing fits the same pattern; narrator-interest @77 fires (POV co-citation available); persistent (Taylor stays in sept interior through episode close).

Response: **REVISE — add SM-1 entry.**

This is the Phase 4 obligation. Defense for adding:
- Symmetry with ID-10 (Edric-fork @57 sublocation entry, verdicted CORRECT). Same pattern: door-crossing produces a persistent sublocation flip.
- Reality: Taylor's position genuinely changes; persistence holds (state.md confirms she is inside the sept at episode close).
- Authority: Taylor fork is licensed for `actor:taylor-hebert-westeros.*`; `sublocation` is a state.md-tracked field (verified in audit; not a field-extension).
- Cross-facet: narrator-interest @77 fires; POV co-citation requirement satisfied. Same beat already carries ID-14 (mask-state) — two entries on two distinct fields on the same actor at the same beat is licit per rubric §Frugality ("If a beat changes multiple fields on the same target, multiple entries are licit").
- The mask-state and the sublocation are distinct fields capturing distinct aspects of the threshold-crossing: the spatial transit (sublocation) and the performance-release (mask-state). Both persist; both are load-bearing for s01e02 continuity.

NEW entry: `@77 actor:taylor-hebert-westeros.sublocation: yard -> sept-interior`

`<old>=yard` is the project-setup baseline (Taylor is in the yard from @14 onward; rubric's approach-zone permitted-silent for position establishes baseline at project-setup, and state.md tracks Taylor's sublocation in the yard cluster throughout s01e01). `<new>=sept-interior` matches the destination phrasing used by Edric-fork ID-10 modulo the door-context (Edric: `sept interior (past threshold)`; Taylor: `sept-interior` after threshold-crossing). For consistency with ID-10 phrasing convention, accept either; the entry uses the simpler `sept-interior` form.

---

## 3. Final revised entry list (Taylor fork output)

```
1 @48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible
2 @64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks
3 @77 actor:taylor-hebert-westeros.sublocation: yard -> sept-interior
4 @77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private
```

Field-extensions declared (per rubric §"Field-extension protocol"):
- `administrative-status` — new field for s01e01 census tracking; tracked-state-aspect (administrative classification, persistent past beat, season-arc-load-bearing). Project-setup baseline: persona card (Taylor as unenrolled child under Septon Osmynd's informal protection prior to s01e01).
- `knowledge.record-state` — new field for POV knowledge of bureaucratic record; tracked-state-aspect (knowledge is rubric-named). Chain-grounded: `<old>` matches studio's @48 `<new>` on `prop:district-ledger.taylor-entry` per cross-author convention.
- `mask-state` — new field for cooperative-child performance state; tracked-state-aspect (rubric-named in §"Field-extension protocol" example list). Project-setup baseline: persona card + behavior pack (`maintained-cooperative-child` is the active maintained-performance baseline).
- `sublocation` — NOT a field-extension; on-schema (state.md tracks). Baseline: project-setup (yard from @14 onward; approach-zone permitted-silent baseline).

Curve check (revised):
- Total fires: 4 on `actor:taylor-hebert-westeros.*` (was 3; +1 from SM-1 add).
- POV co-citation: all four entries have narrator-interest fires on the exact beat (@48 ✓, @64 ✓, @77 ✓ for both ID-3 and ID-4).
- Cross-facet contract: @39 refusal honored (no fire); @64 strong-expect honored (fire); @38 conservative-no-fire defensible; @48/@64/@77 POV co-citation all met.
- Refusals: 3 (T1 @39 held-against-turn; T4 @50 transient-posture; T5 @52 cross-POV/derived-knowledge carve-out). 2 considered-and-refused free additions (F1 @45 withdrawn on co-citation; F3 @23 exposure as registration-as-state).
- Sparsity: 4 / 77 = 5.2% on POV actor-state alone; aggregate file density adds the studio + Edric fires.

---

## Summary

Defends ID-12 (@64 knowledge.record-state, calibration anchor) and ID-14 (@77 mask-state, persistence-test passes within s01e01 window) without entry mutation; revises ID-7 (@48 administrative-status) by harmonizing field-extension baseline note with ID-14 (both grounded in persona-card project-setup); adds SM-1 (@77 actor:taylor.sublocation: yard -> sept-interior) per Phase 2 fault-002 obligation. Refusal verifications: T1 @39, T4 @50, T5 @52, F1 @45, F3 @23 all hold under Phase 3 fire-justification pressure with explicit rubric-citation responses; T5 (knowledge.ally-count re-target) addressed as REJECT-signature carve-out + indirect cross-POV authoring. Final list: 4 entries (1 added, 3 defended, 0 culled).
