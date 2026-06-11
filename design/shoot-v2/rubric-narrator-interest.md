# Narrator Interest-Flag Facet Rubric

Authoring + review rubric for `facets/interest-narrator.md` entries. Phase 1 reviewer-tuning artifact for the shoot-v2 facet-tuning process. Authority for the dialogue-writer Taylor-POV fork (interiority output mode) when authoring narrator-interest entries, and for the mechanic auditor + dialect audience when reviewing them.

Status: V1 draft (Phase 0). Will be locked at end of Phase 1.

The rubric is **POV-character-specific** — each project's POV character gets its own narrator-interest rubric instance because the behavior pack is the authoring authority. This rubric instance is for `taylor-hebert-westeros` (s01e01–e06). Reusing the structure for a different POV character requires re-authoring §"Voice fidelity" and the calibration anchors against that character's behavior pack.

---

## What narrator-interest is for

Narrator-interest is a **spotlight** layer. It marks the beats the POV character actually cares about and registers what she registered. Most beats get nothing. Fires are sparse on purpose: the *contrast* between fired and silent beats is the signal.

It serves three jobs, in priority order:

1. **Spotlight signal for the stitcher.** A fired beat gets weight: the stitcher renders it in full, may quote the narrator-interest content, and treats it as render-anchor for surrounding compression. A silent beat gets baseline weight and is eligible for compression or selection-out. **The contrast between fire and silence is what gives the stitcher render-density gradient.** A file that fires on most beats has no gradient and no signal.
2. **Cross-facet anchor.** Memory-flag callbacks, audience-interest density, loudness perception, and state-update interior-side registrations anchor on narrator-interest fires. A fire is an invitation for downstream facets to attach; silence withholds the invitation.
3. **Doubled-register fidelity ledger.** For a POV character with doubled register (Taylor's Westerosi-child mask outside, base-register cognition + Earth-Bet shadow + Dance-foreknowledge clamp inside), the fired entries make the doubled register visible across the episode. The interior register only shows here; everywhere else the spoken/external layer dominates.

Narrator-interest is **not** narration. It is not paraphrase. It is not a summary of the scene. It is a one-clause spotlight on a beat that earned her attention, written in her voice.

**The test for any beat is simple: does she care about this enough that a reader should weigh it more than the surrounding beats?** If yes, fire and write the registration. If no, silence — basic nothing.

---

## Form

Per `schemas/facet.schema.md`:

```
<id> @<proto-line-id> <one-clause description of what the narrator registers>
```

- **One observation per fire.** The interest-flag is a single registration on a single beat; multiple independent observations stacked into one entry are anti-pattern (split or cut). Sentence chassis is unconstrained — semicolons, em-dashes, and clause-coordination are permitted when they fit the POV character's base-register cadence; the rule is observation-count, not punctuation-shape. (Semicolon-spine restriction removed 2026-05-23 per user directive; semicolons are now governed by base-card cadence patterns only — see §Voice fidelity ACCEPT signature "Em-dash or semicolon used per base-card pattern.")
- **POV-restricted.** Speaker is always the POV character. No third-person omniscient registration (no "the officer thinks").
- **Anchored.** Every entry must anchor to an existing proto-line ID via `@`.
- **Sparse.** Not every proto-line fires. Sparsity is a load-bearing rubric property; see §"Curve-shape rubric" for density targets.
- **Refusal is a valid output.** A NONE on a proto-line is a real authoring decision — it asserts the POV character did not attend to this beat in a way that earned a registration.

Form is necessary but not sufficient — a well-formed entry that fails voice fidelity, perceptual access, or cross-facet earning is still a violation.

---

## V2 rubric (locked at end of Phase 1) — three axes

A narrator-interest entry passes review iff its content **affirmatively demonstrates** at least one signature on each of three axes (perceptual access, voice fidelity, earning) and does not violate any anti-pattern.

### 1. Perceptual access

Does the SVO proto-line afford something the POV character would actually *notice*, given their behavior-pack sensory channels and attention patterns?

For `taylor-hebert-westeros`, the named channels are (from `cards/dialects/taylor-hebert.card.md` §"Voice tells" and `cards/dialects/taylor-hebert-westeros.card.md`):

- **Passive fauna-feed.** Insects (base) + corvids and rats (Westeros variant). She perceives ambient fauna across a ~30m radius continuously; weather/movement patterns in the bird-roost or insect-seam are her low-level register.
- **Eyes-to-the-exits sweep.** On entering any room she clocks egress before people. The sweep is fast and habitual.
- **Two-input pause / fauna-track tilt.** Her head tilts fractionally toward sounds the room hasn't registered. In Westeros, this gets covered as *strange watchful child*.
- **Pre-calculation.** She is operating on tactical timelines ahead of the scene's present. *She had already calculated the clearance.* The clearance was already calculated; the present beat is when it surfaces.
- **Cost-tracking.** Watch-cost, exposure, leverage, threshold are her resting unit of measure. She rates beats by their cost-load to herself or to others.
- **Refusal-to-look-directly.** Earth-Bet monuments produce gaps in her attention. The narration moves around them; if a Westerosi beat triggers a displacement (enclosed space, child-harm, fire-at-scale, sudden fauna silence), the gap-pattern surfaces.
- **Mask-thinning at Septon Aldric proximity.** The interior register relaxes when he is in scene; voice tells become slightly more visible.
- **Doubled-register foreknowledge.** Westerosi monuments she has read but not lived (Dance, Hour of the Wolf, Doom, Conquest dating) clamp visibly when proximate; the interior knows, the spoken line never tells, and the narrator-interest entry can register the clamp without naming the content.
- **Age-mismatch tell.** Moments where her cognition reaches a word the body cannot voice; where she catches herself sitting too still; where the body's affordances diverge from her interior plan.

ACCEPT signatures:
- The entry names which channel licenses the registration (passive fauna, eyes-to-exits, pre-calc, cost, refusal, mask-thin, foreknowledge-clamp, age-mismatch). Channel may be implicit if obvious from content; preferred-explicit for ambiguous cases.
- The channel is plausibly active for *this beat*. (Example: passive fauna at @4 — beetles in flagstone seam — is licit; passive fauna at @43 when the officer is committing a record-decision is not the channel that lights, even if beetles are still around.)

REJECT signatures:
- Author-voice intrusion. Registration without a behavior-pack channel license. ("She wonders if the cart will move." → no channel; reject.)
- Channel-misfit. Citing a channel that does not plausibly fire on this beat.
- Generic curiosity. *She notices the X.* Notice is not a channel.

### 2. Voice fidelity

Does the entry's content read in the POV character's register, per the behavior pack?

For `taylor-hebert-westeros` — interior register is **base-card register, unmodified** per the variant's own §"Register markers". The Westerosi mask register applies to *spoken* output, NOT to interiority. Narrator-interest is interior. Fidelity is judged against base-card voice tells.

ACCEPT signatures:
- **Inventory-tell register.** What the fauna are doing, what the body is doing, what the cost is — instead of what the feeling is. *The corvids hold the bell-tower roost; the wing-shift signals nothing yet.* Not *she feels watched.*
- **Cost-language.** Watch-cost, threshold, leverage, exposure, budget appear naturally. Not as ornament — as her resting register.
- **Pre-calculation tense.** Past-perfect for actions she completed before the present beat. *She had already counted the four spans of dirt to the gate.*
- **Specificity.** Distances in paces or counts (Westeros register), durations in concrete spans, observations that name the chemistry or mechanics rather than the impression.
- **Trailing fragment ending on the load-bearing word.** No softener tail.
- **Clinical-of-the-horrible.** When the registration is dark, the prose stays flat; the gap between the content and the register is the load.
- **Em-dash or semicolon used per base-card pattern** — not as ornament, only when the structural function fires.

REJECT signatures:
- **"I feel" / emotional declaration.** *She felt afraid.* Reject. Emotion appears as event, not as report.
- **Hyperbole / softeners.** *Always, never, totally, honestly, just* used non-load-bearingly. Reject.
- **Performance vocabulary.** *Amazing, incredible.* Reject.
- **Apology language unless meant.** Reject ornamental sorrys.
- **Anachronistic idiom slipping into interior.** Interior is base register, but base register itself avoids slang and post-medieval idiom; *okay, fine, sure* are still rejects.
- **Mask-register bleed into interiority.** *I do not know, ser* style softeners or *if it please you* in *interior* prose. The mask is performance. Interior does not perform. Reject.

### 3. Earning (does she care about this beat?)

The earning axis is the spotlight test. **Most beats do not fire.** The author must be able to answer "why does her attention land *here* and not on the beats around it?"

The canonical reasons attention lands are below; they are the *typical* triggers, not an exhaustive list. The underlying test is whether the beat earned the spotlight relative to its neighbors.

ACCEPT signatures (typical triggers):
- **Peak-bones-class beat.** Bone listed in the scene's `peak-bones` array in the scene-map (ruptures, commits, irreversible registrations). Her attention almost always lands here. A peak-bones-class bone with no narrator-interest fire requires explicit rationale (narrator disengaged / off-screen / explicitly looking away).
- **Approach to peak (rising zone transition).** A bone in a `rising` scene zone where magnitude is ascending toward peak, or the first bone where the scene transitions from `flat-low` to `rising`. Approach to a turn is where pre-calc surfaces and cost gets priced.
- **Behavior-pack trigger fires.** Displacement triggers (enclosed space, child-harm, fire-at-scale, sudden fauna silence, helpless-protector-figure); mask-thinning (Septon Aldric proximity, peer-children); foreknowledge-clamp (Westerosi-monument-adjacency, Dance-timeline brush); fauna-track tilt (sound the room hasn't registered yet).
- **Cross-facet anchor demand.** A downstream facet (memory-flag, sensory, audience-interest, interior state-update) needs to attach here, and narrator-interest is the spine.

REJECT signatures:
- **Density-on-flat.** Firing on a `flat-low` ambient bone with no transition, no behavior-pack trigger, no cross-facet need. Ambient bones are *correctly silent.* Silence is the default.
- **Plot-importance inflation.** Firing because the writer knows the beat is load-bearing for the season. Narrative weight does not earn the spotlight; her attention does.
- **Fire-because-it's-charged.** Firing on every bone in a `rising` zone by default. Many such bones do not earn — the charge may be the scene's, not hers. A bone in a `rising` zone earns a fire when the charge is perceptually *hers*.
- **Persistent-narration.** Same registration sustained across consecutive bones. One fire per registration. If something keeps mattering, the next fire must register *change*, not repetition.
- **No-contrast firing.** Firing such that the file has no contrast — every other bone fires, every approach bone fires, every transition bone fires. The contrast between fire and silence is the signal; saturating the file destroys the signal.

---

## Cross-axis tests

- **The channel test.** Name the perceptual channel in five words or fewer. *Passive corvid feed*, *eyes-to-exits*, *pre-calc surfacing*, *cost on Mira*, *fauna-track tilt*, *foreknowledge-clamp*. If you cannot name a channel, do not fire.
- **The base-register test.** Read the entry alongside the base-card sample box. Does it read in the same register without breaking? If a base-card sample could be substituted in voice and rhythm, the entry passes. If the entry reads as omniscient-narrator or as a different character's voice, it fails.
- **The earning test.** Name the trigger in five words or fewer. *Scene-map transition flat-low → rising*, *peak-bones entry*, *displacement on enclosed space*, *Septon-proximity mask-thin*, *foreknowledge-clamp on king-name*, *cross-facet anchor for memory-flag*. If you cannot name a trigger, do not fire.
- **The doubled-register test (POV-character-variant-specific).** For Taylor-Westeros: does the entry hold the doubled register? The interior knows; the spoken layer does not leak. A narrator-interest entry that reads as something Taylor *would say aloud in mask register* is a fail — it should be base-register interiority. Conversely, a narrator-interest entry that *names* an Earth-Bet monument or a Dance specific (date, name, content) is a hard fence violation.
- **The density test.** Across the chapter, expect the narrator-interest density curve to align with scene-map pressure-signal transitions and behavior-pack triggers (load the scene-map facet file `theater/facets/scene-map-<book>-<chapter>.md` for `rhythm-shape` and `peak-bones` context). A full-corpus run should fire on roughly **15–25% of bones** for a Taylor-POV variant — sparser than location-state, denser than memory-flags (rare callbacks). Spotlight, not ledger. Outside that band, investigate: too dense = density-on-flat / no-contrast contamination; too sparse = mask-too-perfect / narrator-disengaged-episode.

---

## Anti-patterns (named for the rubric)

These are the contamination patterns the writer must resist and the reviewer must call out.

1. **Author-voice intrusion.** Narrator-interest written as omniscient narrator commentary, not as POV-character registration. *The officer's authority hangs over the yard.* No channel license. Reject.
2. **Summary-of-the-beat.** Paraphrasing the SVO instead of registering what's behind it. SVO: *the stylus stops on the board.* Bad entry: *the stylus stops on the board, registering decision.* The SVO already says the stylus stops. The entry must add the *interior layer* — *the parallel-mark threshold has just passed in the clerk's hand* (cost-tracking + pre-calc).
3. **Generic curiosity.** *She notices the X.* Notice is the verb that hides the missing channel. Replace with the specific perceptual channel or refuse to fire.
4. **Monument-leak.** Naming an Earth-Bet proper noun or a Dance specific in interest-flag content. Hard fence; reject and require revise.
5. **Mask-bleed.** Writing the entry in spoken Westerosi-mask register instead of base-register interiority. Reject.
6. **Density-on-flat-1.** Firing on ambient 1-beats without transition, trigger, or cross-facet need. The ambient open of an episode (s01e01 @1–@4 establishing) does NOT fire by default; sparse fires here are licensed only by explicit displacement trigger.
7. **Persistent-narration.** Same registration carrying across beats. *She tracks the corvids* at @1, @2, @3, @4. Reject all but the first; the rest must register *change*.
8. **Plot-importance inflation.** Firing because the writer knows the beat is load-bearing for the season. Scene-map `peak-bones` membership reads on-face structural-charge; narrator-interest reads on-face *attention*. A plot-load-bearing beat that does not carry her attention is correctly silent.
9. **Mask-too-perfect (file-level).** Across an episode, if there are zero mask-thin moments, zero foreknowledge clamps, zero displacement registrations, the file is overproducing the cover and underproducing the doubled register. The audit-flag fires at the file level, not the entry level.
10. **Inverted-predicate template recurrence (form-level).** Entries built on the *"X is what Y"* / *"the X is the Y"* / *"the X is what the Z means today"* template — a definitional-collapse cadence that resolves a perception into a rule. The template is rubric-licit when fired once per file as a register-defining move (typically near a peak or threshold beat), but recurs as a chassis. **Cap: ≤1 entry per file may use the inverted-predicate template.** Two or more is an authorial pressure-tell that the AP-001 chassis is doing structural work the entries do not individually defend. Audit enumerates form-pattern matches against `is what`, `is the`, and `means today` constructions at sentence-final position. (URI-FACETS-CYCLE-1, 2026-05-19 — promoted from audience-gate cycle-1 attack on b01c01 narrator:2/4/6: cape-fic-reader + dark-fantasy-reader independently flagged the chassis-recurrence the mechanical AP-SCAN could not see at file scope.)

11. **Apparatus-as-subject registration (no-ledger discipline — DEC-0115, 2026-06-08).** A NI entry whose grammatical subject is the apparatus, network, count, or abstraction rather than the POV character's concrete perception. *The count closes over the face.* *The node flags a discontinuity on the north wing.* *The feed returns the pattern.* The apparatus is a *lens*, not an actor — narrating the apparatus's inner life instead of what the POV character perceives *through* it. **Reject.** Rewrite to foreground the concrete percept the lens mediates: *the face I counted is gone — north-wing seam, third bracket* or *the line breaks on the north wing; she's lost one*. Per DEC-0115: apparatus-as-subject is retired across all authoring surfaces; NI entries authored apparatus-first fail RUBRIC-FIDELITY at Phase 4 audit with no accept-with-rationale escape (the former "stylized instrument-POV intentional" rationale is explicitly retired by DEC-0115).

---

## Curve-shape rubric (file-level)

The narrator-interest file as a whole must demonstrate doubled-register shape across the episode. The mechanic auditor checks the curve in addition to per-entry correctness.

### Episode-level shape

The full narrator-interest file across an episode must satisfy:

- **Contrast.** Fires must be visibly sparser than silences. The stitcher reads fires as render-weight; if every beat fires, there is no weight gradient and the spotlight has no value. The single most important file-level test.
- **Density alignment with scene-map pressure-signal.** Density should be visibly higher around `rising` zones and bones in `peak-bones` arrays. Ratio of fires-per-bone in non-`flat-low` scenes should exceed ratio in `flat-low`-only scenes by at least 2×. Load the scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) for classification.
- **Doubled-register visibility.** Across the file, both registers should show: (a) Westerosi-mask cover register visible in cross-facet contract anchors (mask-thinning at Septon-proximity, mask-too-perfect under adult observation); (b) base-register interior with Earth-Bet shadow and Dance-foreknowledge-clamp visible at displacement triggers and at Westerosi-monument adjacency. **A file with only one register visible is a fail.**
- **Behavior-pack channel diversity.** Across an episode of >50 beats, expect at least three distinct channels exercised across the fires: passive fauna-feed, eyes-to-exits, pre-calc, cost-tracking, refusal-to-look, mask-thin, foreknowledge-clamp, fauna-track tilt, age-mismatch. A file that uses only one or two channels (e.g. all passive-fauna registrations) is undercovering. (Coverage is *across the fires that earn*, not coverage by inflating fires to hit channels.)
- **Frequency band.** 15–25% of proto-lines fire (s01e01 expected: ~12–19 entries on 77 beats). Outside band, investigate: too dense = density-on-flat / no-contrast contamination; too sparse = mask-too-perfect file-level OR narrator-disengaged-episode (kickback signal to screen-writer).

### Scene-level shape

For each scene (per the scene-map file's `@<start>-@<end>` ranges):

- **At least one fire per scene.** A scene where the POV character registers nothing is structurally suspicious. Default expectation: every scene contains at least one perceptual registration. Refusal must be flagged with explicit rationale (scene-as-respite, scene-as-pure-transit).
- **Peak-cluster density.** A scene that contains a `peak-bones`-class bone must have a narrator-interest entry on or adjacent to that bone. The narrator notices ruptures.
- **Approach-zone permitted-sparse.** A long `flat-low` approach zone is permitted-sparse but not zero — the approach is where the eyes-to-exits sweep, the passive-fauna establishment, and the pre-calc surfacing are licensed even in `flat-low` bones.

### When curve-shape fails

The author's response to a failing curve is **not** to inflate fires to hit density. The response is:

- **Channel-coverage fix.** If the curve is undercovered on channels, audit which channels are missing and add fires where their triggers light.
- **Doubled-register fix.** If only one register shows, audit Westerosi-monument-adjacency beats and displacement-trigger beats; add foreknowledge-clamp and Earth-Bet-shadow registrations where licensed.
- **Screen-writer kickback.** If the proto-line file does not contain beats that would license the channels needed for full coverage, flag a kickback. (Rare for narrator-interest; the SVO file usually carries enough perceptual surface.)

Inflating fires to hit density without earning each fire is the prohibited move. The cross-facet contract assumes fires are honest.

---

## Cross-facet contract

Narrator-interest's downstream consumers. Once narrator-interest is locked, these other facets condition on it.

### Anchor expectations (consumer side)

- **Stitcher (primary consumer).** Fires are render-weight signals. Beats with a fire render in full SVO and may have the narrator-interest content quoted or paraphrased into the stitched output. Beats without a fire are baseline-weight: eligible for compression under "and", or selection-out if narratively redundant. The contrast between fired and silent beats is the gradient the stitcher uses to set rendering density.
- **Memory flags.** Memory-flag entries (callback to prior story content, Earth-Bet monument, Dance foreknowledge) are anchored on narrator-interest fires. A memory-flag without a co-cited narrator-interest entry on the same beat is suspicious — the narrator should have registered the trigger before the memory fired. Memory-flag author should treat narrator-interest as the spine entry.
- **Audience-interest flags.** Aggregate audience-interest density should align with narrator-interest density at peaks. Persona-specific divergence is permitted off-peaks (a worm-canon-pedant fire that the narrator does not register is licit — the audience perceives a thing the narrator does not). But three audiences firing on a beat where the narrator is silent is a flag for cross-facet review.
- **Loudness flags.** A loudness flag (volume change perceived) should usually have a narrator-interest co-citation — the narrator perceives the change. Exceptions: loudness changes outside the narrator's perceptual range (rare in this project; she has the passive fauna-feed extending her range).
- **State-updates (interior-side).** State-updates on the POV character's actor-state (mood-shift, posture, knowledge-acquisition) should have a narrator-interest co-citation registering the shift. State-updates on the environment or other actors do not require narrator-interest co-citation.

### Back-contract (what narrator-interest owes to upstream facets)

- **Scene-map pressure-signal alignment.** Density must align with the scene-map's `rhythm-shape` transitions and `peak-bones` entries per §"Curve-shape rubric". Narrator-interest is the consumer-side test that the substance-delta pressure curve is *perceptually load-bearing* and not just structurally drawn.
- **Location-state alignment (soft).** Loc-state fires at environment-frame turnover; narrator-interest density at loc-state fires is expected (the narrator notices when the frame changes). Soft alignment, not hard gate.

### What narrator-interest does NOT condition

- Dialogue file content. Dialogue fires on its own register; narrator-interest is interiority. A line of dialogue may be content-rich without a narrator-interest co-citation (the speaker is the narrator's interlocutor, the narrator hears the line, but the entry fires only if she perceives *more* than the line says).
- Scene-map (forward). Narrator-interest does not change scene-map fields. If a beat's narrator-interest entry suggests different charge than the scene-map classification, the auditor flags for cross-facet review — but the scene-map stays locked (override is via /and-write re-run).
- Vibes-updates. Vibe shifts are showrunner's call; narrator-interest is one signal among many.

---

## Calibration anchors (drawn from s01e01 corpus)

Five worked examples spanning the rubric. Used during Phase 1 reviewer tuning and Phase 2 writer-fork.

- `s01e01:4 the beetles hold the seam in the flagstone gaps` — **fire.** Channel: passive fauna-feed (base-card primary channel); Westeros-variant: insects still part of her continuous register, this is establishing baseline. Voice: inventory-tell, reads in base register. Earning: `flat-low` zone (ambient), but episode-opening; one of three approach-zone fires expected to establish channel coverage. Entry shape: *the beetles' seam-hold is steady; the wheel-tremor has not arrived.*

- `s01e01:23 the officer's gaze fixes on taylor at the yard's far end` — **fire.** Channel: cost-tracking + eyes-to-exits (he is the threat-vector; her exit-sweep just got narrowed). Voice: cost-language, clinical. Earning: scene-map `rising` zone (first non-flat bone in the scene — transition into rising pressure). Entry shape: *the watch-cost has just been priced to her name.*

- `s01e01:24 the stylus stops on the board` — **fire.** Channel: pre-calc surfacing (she had already calculated the parallel-mark threshold; this is the beat where the calc surfaces). Voice: pre-calc tense, specificity. Earning: bone listed in scene's `peak-bones` array (climax peak). Entry shape: *she had already counted what the pause would commit; the pause has just committed.*

- `s01e01:38 taylor puts the letter into the air in front of the officer` — **fire.** Channel: cost-tracking + age-mismatch (the body's eleven-year-old reach versus the cognition's evaluation of the commit threshold). Voice: cost-language, body-physical-fact. Earning: bone listed in scene's `peak-bones` array (climax peak). Entry shape: *the exposure is paid; the body reaches at the height the cognition has already cleared.*

- `s01e01:33 the door stays shut` — **fire.** Channel: refusal-to-look-directly (Osmynd on the pallet, dying — Earth-Bet displacement trigger: child-harm-adjacent, helpless-tutor-figure). Voice: clinical-of-the-horrible, gap-narration. Earning: scene-map `rising` zone with behavior-pack displacement trigger (not peak-bones-class, but the displacement trigger earns the fire). Entry shape: *the threshold holds and what is on the other side stays the size she will not name.* (This is the doubled-register exemplar: Earth-Bet shadow surfaces via the dying-protector-figure pattern without naming a monument.)

- `s01e01:50 taylor turns to mira` — **NONE.** Channel: none lights (turning is transitional; no perceptual channel is invoked). Voice: n/a. Earning: `flat-low` zone, no transition, no behavior-pack trigger, no cross-facet anchor demand. Refusal-CORRECT.

- `s01e01:67 the officer's near foot lifts toward the horse` — **NONE.** Channel: arguably eyes-to-exits (his exit-vector is the next move) but the scene has just shifted to `release-only` and the scene is closing; her attention has shifted past the officer. Voice: n/a. Earning: `release-only` zone, no transition, narrator-disengaging from the threat. Refusal-CORRECT (boundary case; defensible on disengagement).

---

## Author / reviewer notes

- **Author:** dialogue-writer fork for the POV character (interiority output mode of the same fork that writes spoken dialogue). For `taylor-hebert-westeros`, the fork loads: base behavior card, Westeros-variant card, persona card, the scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) (for `rhythm-shape` + `peak-bones` transition/peak alignment — replaces pre-overhaul tensometer scalar), the locked location-state file (for frame-turnover alignment), and this rubric. Two-pass authoring:
  1. **Per-beat pass.** Walk the proto-line file. For each beat, decide FIRE or NONE. If FIRE, write the entry, name the channel, name the trigger.
  2. **File-shape pass.** Read the file as a curve. Check episode-level density alignment, doubled-register visibility, behavior-pack channel coverage. Either fix misfires (NONE→FIRE add for missing coverage; FIRE→NONE strip for density-on-flat-1) or flag screen-writer kickback for structural gaps. **Do not inflate to hit density.**
- **Reviewer (mechanic auditor):** under this rubric. Per-entry verdict for fires: CORRECT (all three axes earned, no anti-pattern fired) or INCORRECT (named axis-failure or anti-pattern). Per-entry verdict for refusals: CORRECT (no axis earned a fire) or MISSED (a channel + trigger combination earned a fire that the author skipped). File-level verdict: SHAPE-OK / SHAPE-FAIL with named density / coverage / register failure mode. Cross-facet contract pre-ship check.
- **Reviewer (dialect audience):** under this rubric, fidelity-only mode. Worm-canon-pedant primary; dark-fantasy-reader and pulp-enthusiast secondary. Per-entry verdict: VOICE-OK / VOICE-FAIL with citation to base-card or variant-card section. The dialect audience does NOT adjudicate the firing decision (mechanic does) or the cross-facet contract (mechanic does). Their domain is voice fidelity to the behavior pack.
- **Verdict combination.** Mechanic + dialect verdicts are independent gates. Both must pass; either reject = revise. They cannot substitute. (This is the test the user named: dialect audience reactivated for the right facet without bleeding into mechanic-facet adjudication.)
- **Cull:** narrator-interest has per-file cull (per `schemas/facet.schema.md`). Cull is delete-only — entries that fail any axis or any anti-pattern are deleted. No rewrites at cull time. The Phase 2 writer-fork output IS the cull-stage authoring; revision happens in Phase 4 only.
- **Floor defense.** If the author defends a NONE against a reviewer's push to FIRE by citing rubric (no channel earned, no trigger lit), accept the defense. Sparsity is load-bearing; over-firing breaks the cross-facet contract by saturating the memory/audience-interest anchors.
- **Ceiling defense.** If the author defends a FIRE that the reviewer would push to NONE, the burden is on the author to name (a) the channel, (b) the trigger, (c) the cross-facet contract slot the entry serves. A FIRE that survives ceiling defense should also satisfy the doubled-register test — entries that earn on perceptual access alone but break voice fidelity do not survive.

---

## V1 lenient form (retained for lift comparison only)

V1: ACCEPT iff the entry is form-correct (single clause, anchored, POV-restricted) AND any axis is plausibly invoked at any reading. No anti-pattern check, no curve-shape check, no doubled-register test, no dialect-audience pass.

V1 exists only to produce a baseline accept-rate for round-trip comparison after writer-tuning. It is not an authoring target. Do not soften V2 toward V1 between rounds.

---

## What narrator-interest is not

- Not narration. Not paraphrase of the SVO. Not author commentary.
- Not editable after cross-facet consistency. Once locked, entries are an input to the stitcher and to memory-flag authoring; cannot be retuned without restarting the consistency pass.
- Not the only registration of POV. Dialogue (spoken-side) carries its own POV-fingerprint; loudness, audience-interest, and memory carry distinct registrations. Narrator-interest is the *interior-perception* layer specifically.
- Not symmetric across POV characters. Each POV character's narrator-interest rubric instance must be re-authored against that character's behavior pack. The structure transfers; the channels, voice signatures, and calibration anchors do not.
