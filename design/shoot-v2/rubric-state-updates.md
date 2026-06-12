# State-Updates Facet Rubric

Authoring + review rubric for `facets/state-updates.md` entries. Phase 1 reviewer-tuning artifact for the shoot-v2 facet-tuning process. Authority for the **split authorship** model: studio writes `studio.*` and `prop:<slug>.*` entries; the **dialogue-writer fork for character X** writes `actor:<x>.*` entries (POV-restricted). Single mechanic auditor reviews all entries against this rubric regardless of author.

Status: **V2 locked** at end of Phase 1 (2026-05-07). Phase 1 baseline review verified the V2 axes hold without softening (V1 lenient = 78.9%, V2 strict = 6.7% on naive baseline; the gap is rubric-blind contamination, not over-strict calibration). V1 lenient retained at end-of-file for round-trip lift comparison only.

The rubric is **POV-restriction-aware** and **canonical-state-aware**. It depends on the scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) and the locked narrator-interest file for cross-facet contract. It does NOT depend on (and must not be folded into) the open V3 rubric work for tensometer (body-charge POV scope, negative-event reversal-proximity).

The pressure-signal surface for cross-facet contract checks is `per-bone substance_delta.axis_moves.magnitude` surfaced through the scene-map's `rhythm-shape` + `peak-bones` fields. Bones listed in the scene's `peak-bones` array are the "hinge beats" (formerly @64-class beats in tensometer language) that strongly expect state-update co-citation. Bones in `rising` or `flat-mid` zones without peak-bones membership that are nonetheless approaching a hinge beat may be held-against-turn class (formerly @39-class) where canonical state-update co-citation is withheld.

---

## What state-updates is for

State-updates is the **canonical-memory write-back layer**. Entries describe deltas that the showrunner applies to canonical state files at the phase boundary between cross-facet consistency and stitch. **An entry is a promise to the canonical state.** If the entry ships, the field changes. If the entry doesn't ship, the field doesn't change.

It serves three jobs, in priority order:

1. **Canonical write-back signal.** Every shipped entry is consumed by the showrunner as a mutation against the named target's state file. Wrong entries corrupt canonical state for downstream episodes. **This makes state-updates the highest-stakes facet.** The reviewer's strictness reflects that.
2. **Cross-facet integrity check.** State-updates is the consumer-side validator for the scene-map pressure-signal surface — `peak-bones` strong-expect (irreversible registrations get co-cited) and held-against-turn class (bones in rising zone approaching a peak-bone but not themselves peak-bones — registration-only, not canonical change). It is also the consumer-side validator for narrator-interest's POV-restriction: an actor-state shift on the POV character requires a narrator-interest co-citation; state shifts on other actors and on environment do not.
3. **Stitch-time selection signal.** Beats with a state-update fire are render-anchors for the stitcher: irreversible turns. The stitcher uses the presence of a state-update as a hint that the beat is load-bearing for memory and should render in full (subject to narrator-interest weight).

State-updates is **not** registration. It is not perception. It is not POV-character interiority logging. It is the structured delta the world owes to canonical memory.

**The test for any beat is simple: does a tracked field on a real card change at this beat — and is the change persistent past this beat?** If yes, fire. If the change is a perception, a registration, an in-the-moment posture without persistence, or a stylistic noting — silence.

---

## Form

Per `schemas/facet.schema.md`:

```
<id> @<proto-line-id> <target>.<field>: <old> -> <new>
```

- **`<target>`** is `actor:<slug>` | `studio` | `prop:<slug>`.
  - `actor:<slug>` — slug of an active actor (under `active-project/actors/`).
  - `studio` — environment-state target (location, time, weather, conditions, doors_and_shutters, ambient, fauna_sense_status, spatial_layout fields per `staff/studio/state.md`).
  - `prop:<slug>` — slug of an authored prop card (under `cards/props/`) OR an `oc-*` slug for project-original props with explicit warehouse presence.
- **`<field>`** — a tracked field on the target's state schema. Examples: `actor:taylor.position`, `actor:taylor.inventory`, `actor:taylor.knowledge.rider-departed`, `studio.actors_in_yard`, `studio.doors_and_shutters.sept-main-door`, `prop:letter.holder`, `prop:letter.seal-condition`. Field MUST exist on the target (or be a justified extension; see below).
- **`<old>`** — the value of the field immediately prior to this beat. Must be canonical-correct (verifiable from the most recent prior state-update on the same field, OR from project setup state if first-touch).
- **`<new>`** — the value the field takes at this beat. Persistent past the beat (until the next state-update on the same field, or until episode close).

Form is necessary but not sufficient — a well-formed entry on a beat where state did not actually change is a violation.

### Field-extension protocol

If a beat genuinely changes a state aspect not currently tracked on the target's card/state schema, the author may extend with a new field — but only if:

- The extension is documented in the entry (e.g., `# field-extension: knowledge.rider-departed (new field for s01e01 rider-event tracking)` as a trailing comment).
- The field is a tracked-state aspect, not a perception or stylistic flourish (knowledge, mask-state, exposure-state, posture, inventory ARE tracked; mood, register, voice-tone are NOT).
- The mechanic auditor can defend the extension under §"Reality" axis. Extensions that fail Reality become anti-pattern #6 (invented-field).

The conservative move is to refuse the entry and flag a margit referral for card-schema work. Extension is a soft path, not the default.

---

## V2 rubric (locked at end of Phase 1) — three axes

A state-update entry passes review iff it **affirmatively demonstrates** all three of reality, authority, and frugality, AND does not violate any anti-pattern.

### 1. Reality

A real state change actually occurred at this beat, persistent past the beat. Strip the entry: if the field on the target would still be in the `<new>` state at the next beat without this entry having fired, the entry is parasitic.

ACCEPT signatures:
- The anchor proto-line's verb describes a transition that mutates a tracked field: `crosses` (position), `enters` (location), `puts the letter into the air` (prop holder/position), `unfolds` (prop physical condition), `breaks the seal` (prop seal-condition), `dictates ... as provisional` (actor knowledge / record), `steps back through the door` (position), `closes the door` (door state).
- The change is **persistent** — the field stays at `<new>` until something else changes it. Posture-shifts that resolve within the same beat are not state-updates; they are tensometer's territory (body-charge).
- Irreversible bureaucratic / record / knowledge events strongly expect a state-update entry: `the officer dictates taylor's name as provisional labor-eligible` is the canonical example (record-state changes irreversibly; Taylor's knowledge-of-record-state changes too if she perceives it).
- Cross-facet honor: bones listed in a scene's `peak-bones` array in the scene-map (peak-bones-class beats — irreversible registration) almost always carry a state-update; narrator-interest fires on actor:POV.knowledge.* shifts.

REJECT signatures:
- **Registration-as-state.** The proto-line is a *perception* beat — the POV character notices something — but no field on any target changes. *the officer's gaze fixes on taylor at the yard's far end* (@23) does not change a field on `actor:officer` (his gaze is a registration, not a posture-state); it is narrator-interest territory, not state-updates.
- **Held-against-turn (approach-to-peak class).** Beats where someone holds a charged position without resolving — *taylor sets her feet on the dirt where his next pace commits* (@39) — these are registration / body-charge, not canonical state-change. A bone in a `rising` or `flat-mid` scene zone that is immediately adjacent to a peak-bones-class beat (an approach bone, not the peak itself) is held-against-turn class: canonical state-update co-citation is withheld; actor-posture co-citation is permitted if the posture persists past the beat.
- **Transient-posture.** *taylor turns to mira* (@50) — turning is a momentary directional shift, not a persistent posture change. (If she turns and then *stays* facing mira for several beats while doing something else, the persistent orientation IS a posture state — but the *turn-verb* itself is not.)
- **Stylistic noting.** *the stylus stops on the board* (@24) — the stylus is a prop, but "stops" is a momentary motor event; the stylus's holder, position, and condition are unchanged at this beat. The clerk's *recording-state* IS in transition (mid-dictation pause), but the field that resolves is the parallel-marks field at @64, not the stylus-position at @24.
- **Perception-side-effect-as-state.** *the count of allies in the yard drops to one* (narrator-interest @52) — this is Taylor's *perception* of an ally count. The canonical state of `actor:edric.position` may change at @57 when he steps back through the door; the *count-of-allies-as-Taylor-sees-it* is not a tracked field.

### 2. Authority

The target and field are on a real, authoritative source AND the author is licensed to write this target.

ACCEPT signatures (target/field):
- `actor:<slug>` exists in `active-project/actors/<slug>/`. Field is in the actor's state.md schema (or a justified extension per §"Field-extension protocol").
- `studio` field is in `staff/studio/state.md` schema (location, time_of_day, weather, active_conditions, prop_positions, actor_positions, doors_and_shutters, spatial_layout, ambient, fauna_sense_status).
- `prop:<slug>` exists in `cards/props/` or has explicit warehouse presence. Field is on the prop card OR is a standard prop-state field (holder, position, physical_condition, seal-condition for seal-bearing props, dry/wet for ink-bearing props, marked/unmarked for record-bearing props).

ACCEPT signatures (POV / authorship):
- `actor:<slug>.*` entries are authored by the dialogue-writer fork for that character. **Each character writes their own actor-state.** The Taylor fork writes `actor:taylor.*`; the Mira fork writes `actor:mira.*`; etc.
- `studio.*` and `prop:<slug>.*` entries are authored by studio.
- For environment props that have a holder (letter, stylus, ledger), holder-changes are authored by **studio** (props are studio's domain regardless of who is holding them).

REJECT signatures (target/field):
- **Invented target.** `actor:edric` written when no `active-project/actors/edric-cray/` directory exists. (For s01e01, edric does have an actor card; verify slug exactly: `edric-cray`.)
- **Invented field.** `actor:taylor.bravery: low -> high` — bravery is not a tracked field on Taylor's state schema. Mood, register, voice-tone, emotional-state are NOT tracked-state fields on any actor in this project.
- **Out-of-card prop.** `prop:officer-stylus` when no stylus prop card exists and no warehouse presence. Studio may extend with `oc-*` for genuine project-originals, but extension must be flagged.

REJECT signatures (POV / authorship):
- **Cross-POV authoring.** A Taylor-fork-authored entry that writes `actor:mira.posture: standing -> downcast`. Mira's state is Mira's fork's authority. Taylor's fork registers Mira's downcast eyes via narrator-interest (@52), not state-updates.
- **Authorship-mismatch on environment.** A character fork writing `studio.doors_and_shutters.sept-main-door: closed -> open` — door-state is studio. Character forks may write the *consequences* of crossing through a door (their own position-update) but not the door-state itself.

### 3. Frugality

One entry per real change. Old and new are canonical-correct.

ACCEPT signatures:
- `<old>` matches the most-recent prior cited value on the same field (or the project-setup baseline if first-touch).
- `<new>` matches what the proto-line establishes as the post-beat state.
- One entry per (target, field) pair per beat. If a beat changes multiple fields on the same target, multiple entries are licit (one per field).
- Multi-beat compound transitions (door-opening + actor-passing-through + door-closing across @57–@58) decompose into per-beat entries on the *beat the field actually flips*.

REJECT signatures:
- **Drift-old.** `<old>` doesn't match the prior cited canonical value. (E.g., writing `prop:letter.holder: officer -> taylor` at @43 when the most-recent prior cited holder is `taylor` — the letter went from Taylor (initial) to officer at @38, then to officer's-hand at @40, then back to Taylor at @43. The chain must be honored.)
- **Compound entry.** Multiple field-changes packed into one entry. *actor:taylor.position-and-inventory: standing-with-letter -> seated-with-empty-hand* — split into two entries.
- **Repeated entry on stable field.** Citing the same `<old> -> <new>` on the same field in two consecutive entries.
- **Pre-empting a future beat.** Writing the @64 parallel-marks state-update at @63. The change has not occurred yet at @63; @63 is approach (rising zone, pause-before-commit).

---

## Cross-axis tests

- **The strip test.** Remove the entry. If the field on the target would still be at `<new>` at the next beat without this entry having fired, REJECT (parasitic / registration-only).
- **The persistence test.** Read forward two or three beats. Is the field still at `<new>`? If it reverts to `<old>` immediately, REJECT — this was a transient, not a state-change.
- **The authority test.** Locate the field on the target's source-of-truth file. If you cannot point to a line/section that establishes the field, REJECT or refuse the entry and flag the gap.
- **The author-license test.** Is the author the licensed writer for this target? Studio for `studio.*` and `prop:*`; the character's own fork for `actor:<character>.*`. Cross-license = REJECT.
- **The cross-facet test.** Check the scene-map and narrator-interest for the anchor bone:
  - Load the scene-map file (`theater/facets/scene-map-<book>-<chapter>.md`). If the anchor bone is in a `rising` or `flat-mid` zone immediately adjacent to a peak-bones-class bone (held-against-turn / approach-to-peak class), state-update REJECT (canonical state-change forbidden; actor-posture permitted if persistent).
  - If the anchor bone is listed in the scene's `peak-bones` array (peak-bones-class beat — irreversible registration), state-update on the affected target is strongly EXPECTED; absence is a flag.
  - If the entry is `actor:<POV-character>.*` (POV-character actor-state shift, e.g., `actor:taylor.knowledge.*` or `actor:taylor.mask-state`), narrator-interest co-citation on the same beat is REQUIRED. Absence = REJECT or flag back to narrator-interest author.
  - If the entry is `actor:<non-POV>.*`, narrator-interest co-citation is NOT required (Taylor may or may not perceive the other actor's shift).
  - If the entry is `studio.*` or `prop:*`, narrator-interest co-citation is NOT required.

---

## Anti-patterns (named for the rubric)

1. **Registration-as-state.** Writing a state-update for a perception or registration beat where no field actually changes. The dominant naive contamination — narrator-interest, scene-map (pressure-signal surface), and audience-interest are all *registration* facets; only state-updates is structural-delta.
2. **Cross-POV authoring.** A character fork writing another character's state. A studio entry on an actor:* target. Authority violations.
3. **Held-against-turn fire.** State-update on an approach-to-peak bone (in `rising`/`flat-mid` zone, adjacent to a `peak-bones`-class bone) without the posture-persistent defense. Held-against-turn class forbids canonical state-change; honor.
4. **Compound entry.** Multi-field deltas in one line. Split.
5. **Drift-old.** `<old>` value is wrong relative to the canonical prior state. Often emerges when the author paraphrases the SVO without consulting the upstream entry chain.
6. **Invented field.** Writing a state-update against a field that is not on the target's schema and is not a plausible state-extension. Mood, register, voice-tone, emotional-tenor are NOT tracked-state fields.
7. **Pre-empting / lagging.** Firing the entry on a beat adjacent to the actual change-beat. Fire on the beat where the field flips, not before, not after.
8. **Posture-as-state.** Treating every body-rotation, gaze-shift, weight-redistribution as a state-update. Posture is state only when it persists for multiple beats AND the persistence is load-bearing for the next move (e.g., *taylor's feet planted facing the officer* sustained across @38–@39 IS a posture state if persistence is the load; but *taylor turns to mira* at @50 immediately resolved is not).
9. **Density-on-flat.** Firing on every motion-verb in the bones file. State-updates is sparse — irreversible turns and persistent shifts only. The `flat-low` zones (e.g., the approach stretch in s01e01) are nearly silent; the `rising`, `flat-mid`, and peak-bones-class bones hold most fires.
10. **Stylistic noting.** Decorating beats that are "interesting" but do not change a field. Aesthetic salience does not earn a state-update — only persistent field-mutation does.

---

## Curve-shape rubric (file-level)

The state-updates file as a whole should demonstrate canonical-write-back shape across the episode. The mechanic auditor checks the curve in addition to per-entry correctness, but the curve is **lighter** than narrator-interest's — state-updates is fundamentally per-beat fire-or-don't-fire decoration, with file-level density a downstream consequence.

### Episode-level shape

- **Sparsity.** State-updates fires sparser than narrator-interest. Estimated band for s01e01: **8–18% of proto-lines** (~6–14 entries on 77 beats), distributed across all targets. Outside the band, investigate. Above the band: density-on-flat or compound contamination. Below the band: missed irreversible registrations.
- **Density alignment with scene-map pressure-signal.** State-updates concentrates around `rising`, `flat-mid`, and `peak-bones`-class bones; the `flat-low` approach zone is nearly silent. Ratio of fires-per-bone in non-`flat-low` scenes should exceed ratio in `flat-low`-only scenes by at least 2×, ideally 3×. Load the scene-map file (`theater/facets/scene-map-<book>-<chapter>.md`) to classify.
- **Target diversity across the file.** Across an episode of >50 beats, expect entries across at least three target classes: `studio.*`, `prop:*.*`, at least one `actor:*` (and ideally the POV character + at least one non-POV character). A file that fires only on `studio.*` is undercovering actor-state; a file that fires only on `actor:taylor.*` is undercovering environment.
- **POV-character actor-state must have narrator-interest co-citation.** File-level check: every `actor:<POV>.*` entry pairs with a narrator-interest entry on the same beat. Mismatch = flag for cross-facet review.

### Scene-level shape

- **At least one fire per scene-with-irreversible-event.** A scene that contains a `peak-bones`-class beat (bone in the scene's `peak-bones` array) should usually carry a state-update on that bone or its immediate aftermath. Absence is a flag.
- **Approach-zone permitted-silent.** A long `flat-low` approach zone is permitted-silent; state changes in approach are usually establishing-state authored at the project-setup baseline, not at bone beats.

### When curve-shape fails

The author's response to a failing curve is **not** to inflate fires to hit density. The response is:

- **Reality-axis re-pass.** If the curve is too dense, the file likely contains registration-as-state contamination. Strip-test every entry; the parasitic ones cull.
- **Authority re-pass.** If target diversity is low, audit which actors / environment / props had legitimate field-changes the author missed, and add (with cross-facet check).
- **Cross-facet kickback.** If the scene-map shows a `peak-bones`-class cluster with no state-update support, either the rubric is missing a target the author should have written, or the scene-map classification is overstated for the substance at hand. Flag both ways for cross-facet review.

Inflating fires to hit density without each fire passing all three axes is the prohibited move.

---

## Cross-facet contract

State-updates is the consumer-side validator for the scene-map pressure-signal surface and narrator-interest, and the producer-side input to canonical write-back.

### Anchor expectations (consumer side, inherited from upstream facets)

- **Scene-map (upstream — pressure-signal for cross-facet contract).** Per the scene-map's `peak-bones` and `rhythm-shape` fields (loaded from `theater/facets/scene-map-<book>-<chapter>.md`):
  - **Peak-bones-class bones strongly expect co-citation.** "Irreversible registration" — bones listed in the scene's `peak-bones` array. State-update on the affected target(s), `actor:taylor.knowledge.record-state` (POV-character knowledge of the record, requires narrator-interest co-citation), and relevant field mutations are all expected at a peak-bones-class bone.
  - **Approach-to-peak bones (held-against-turn class) forbid canonical state-update co-citation.** Held-against-turn class: a bone in a `rising` or `flat-mid` zone immediately adjacent to a peak-bones bone, where the posture is held for effect. Actor-posture co-citation is permitted (e.g., `actor:taylor.posture: ` if persistent), but canonical state-change is not.
  - **Bones adjacent to peak-bones (body-charge context).** Actor-posture co-citation permitted (the body-reach is a posture); the irreversible *commit* is in tension with the approach bone's hold. Author convention: fire `actor:taylor.posture` once across the approach–peak window if persistent; do not double-fire.
- **Narrator-interest (locked).** Per the narrator-interest cross-facet contract:
  - **POV-character actor-state shifts require co-citation.** Every `actor:taylor.knowledge.*`, `actor:taylor.mask-state`, `actor:taylor.exposure-state` entry must have a narrator-interest entry on the same `@<proto-line-id>`. Narrator-interest's @52 fire (e.g., *"she has one position of cover left and Mira is it"* — concrete-actor form per NI AP-011; apparatus-as-subject form *"the count of allies drops to one"* is rejected under DEC-0115) signals an interior-knowledge shift; if the matching state-update doesn't fire, the cross-facet contract is broken.
  - **Non-POV actor-state shifts and environment shifts do NOT require co-citation.** The narrator-interest file may be silent on `actor:edric.position: in-yard -> through-door` at @57; that's fine.
  - **POV-restriction on state-updates author license.** This is the rule narrator-interest's revised @52 baked in: Taylor's narrator-interest fire registers her *perception* of Mira's disengagement; the canonical `actor:mira.engagement-state` field-change (if any) is the Mira fork's authority, not Taylor's. Honor.
- **Location-state (soft).** Loc-state fires at environment-frame turnover; state-updates may co-cite `studio.active_location` shifts on the same beats. Soft alignment.

### Back-contract (what state-updates owes to canonical memory)

- **Canonical mutation.** Showrunner reads the locked state-updates file at the cross-facet → stitch boundary and applies every entry as a mutation against the named target's state file. Wrong entries = corrupted canonical memory. **The reviewer's strictness reflects this stake.**
- **No mid-beat ambiguity.** Each (target, field) at each beat resolves to exactly one new value. Contradictions across entries on the same (target, field, beat) trigger the schema's contradiction rule: delete both, flag for re-author. Do not pick a winner.
- **Persistence guarantee.** Entries promise persistence past the beat. A field set to `<new>` at @38 stays at `<new>` until a subsequent entry on the same field flips it. If the field "would have flipped back" within the same beat, the entry is invalid (transient, not state).

### What state-updates does NOT condition

- Scene-map fields. State-updates does not change scene-map `rhythm-shape` or `peak-bones`. If a beat's state-update suggests different charge than the scene-map classification, the auditor flags for cross-facet review — but the scene-map stays locked (override is via /and-write re-run).
- Narrator-interest fires (forward). State-updates does not author narrator-interest content. (It does *expect* narrator-interest fires on POV actor-state beats, per the consumer-side rule.)
- Vibes. Vibe shifts are showrunner's call; state-updates is structural-delta only.

---

## Calibration anchors (drawn from s01e01 corpus)

Six worked examples spanning the rubric. Used during Phase 1 reviewer tuning and Phase 2 writer-fork.

- **`s01e01:24 the stylus stops on the board` — NONE.** Reality: the stylus stopping is a momentary motor event; no field changes (stylus position holds, ledger contents unchanged at @24). The clerk's *dictation-state* is in pause but resolves at @47 dictation, not at @24. @24 in peak-bones (a registration peak — her pre-calc surfaces); the irreversible bureaucratic mutation lives at @64, not @24. Refusal-CORRECT.

- **`s01e01:38 taylor puts the letter into the air in front of the officer` — FIRE: `prop:letter.holder: taylor -> mid-air-between-them`** (or `actor:taylor.posture: in-line -> presenting-letter` if posture persists across @38–@39 and is load-bearing for @40 unfolding). Authority: studio writes the prop holder; Taylor fork writes the posture. **Two entries are licit, one each.** Reality: the holder genuinely changes (Taylor's hand to the air-between-them); persistence holds across @38–@39 until the officer takes it at @40. Cross-facet: @38 in peak-bones, body-charge + reversal-proximity, posture co-citation permitted; narrator-interest @38 fires (age-mismatch + cost-tracking) — POV actor-state requires co-citation, narrator-interest provides it. ACCEPT.

- **`s01e01:39 taylor sets her feet on the dirt where his next pace commits` — NONE-CONFIRMED.** Reality: posture-shift but @39 is the held-against-turn bone (a bone inside a `rising` zone immediately adjacent to a peak-bones-class bone, i.e. @39 in rising rhythm-shape). Held-against-turn class explicitly forbids canonical state-update co-citation ("any co-citation here must be actor-posture only; pure registration class — canonical state does not change at @39"). Narrator-interest @39 fires on the calculation surfacing. State-updates correctly silent. Refusal-CORRECT.

- **`s01e01:43 the officer holds the letter out to taylor` → @45 `taylor's palm closes on the letter` — FIRE @45: `prop:letter.holder: officer -> taylor`.** Reality: the holder genuinely changes back; persistence holds (Taylor carries the letter forward through the rest of the episode). Authority: studio. Cross-facet: @43 in rising rhythm-shape (stakes-visibility + reversal-proximity); narrator-interest @43 fires. The handover technically begins at @43 (officer extends), passes through @44 (return-trajectory), and the holder-flip lands at @45 (her palm closes). Fire on @45 (the flip-beat), not @43 (the offer) or @44 (the trajectory). ACCEPT. **Pre-emption note:** firing on @43 would be anti-pattern #7.

- **`s01e01:48 the officer dictates taylor's name as provisional labor-eligible` — FIRE: `actor:taylor.administrative-status: child-or-ward -> provisional-labor-eligible`** + **`prop:district-ledger.taylor-entry: pending -> dictated-provisional`**. Two entries on two targets. Reality: irreversible bureaucratic mutation; persistence guaranteed (Taylor's status is locked for the season's administrative arc). Authority: Taylor fork for actor:taylor; studio for prop:district-ledger. Cross-facet: @48 in rising rhythm-shape (locked DEFENDED, documents prior turn); narrator-interest @48 fires (foreknowledge-clamp on "provisional"). POV actor-state requires co-citation, narrator-interest provides it. ACCEPT both. **Field-extension note:** `administrative-status` and `taylor-entry` are field-extensions licit under §"Field-extension protocol" — both are tracked-state-aspects, not perceptions.

- **`s01e01:57 edric steps back through the door` — FIRE: `actor:edric.position: in-yard-near-cottage-door -> inside-cottage-door-closed`** + **`studio.doors_and_shutters.cottage-door: open -> closed`** (if the proto-line file establishes that the door closes; check). Authority: edric fork writes actor:edric; studio writes the door. Reality: position-change persists (edric does not return to the yard for the rest of the episode); door-state changes if the door closed (verify against subsequent proto-lines). Cross-facet: @57 in rising rhythm-shape (the social reversal — edric's retreat); narrator-interest @57 fires ("the door takes the last adult cover with it"). POV-restriction: Taylor's narrator-interest registers the loss-of-cover; the canonical `actor:edric.position` is edric-fork's authority (not Taylor's), and `studio.cottage-door` is studio's. **No narrator-interest co-citation requirement on actor:edric or studio.** ACCEPT.

- **`s01e01:64 the stylus moves on the line under taylor's name` (parallel-marks beat) — FIRE: `prop:district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`** + **`actor:taylor.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`**. Reality: irreversible record-mutation; persistence absolute. Authority: studio for the ledger; Taylor fork for her knowledge of the record-state. Cross-facet: @64 is a bone inside the scene's `peak-bones` array (peak-bones-class beat — irreversible registration); "co-citation strongly expected here — irreversible registration"; narrator-interest @64 fires ("two strokes; the determination is on the record and on her"). POV actor-state with co-citation. ACCEPT both. This is the canonical state-update bone for s01e01 (a bone inside a `peak-bones` array in a `rising-to-peak` scene).

---

## Author / reviewer notes

- **Author (split):**
  - **Studio.** Authors `studio.*` and `prop:*.*` entries. Loads: scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) (for peak-bones-class / held-against-turn classification), locked narrator-interest, locked location-state, the bones file, the studio state schema, the relevant location/prop cards. Per-bone pass: walk the bones file, identify field-mutations on environment or props, write entries.
  - **Dialogue-writer fork (per character).** Authors `actor:<that-character>.*` entries. Loads: scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) (for peak-bones-class / held-against-turn classification), locked narrator-interest, the bones file, the character's persona card + state schema + behavior pack (if present). For the POV character (Taylor): also loads the locked narrator-interest file as a co-citation check (every `actor:taylor.*` entry must have a `@<beat>` match in narrator-interest). Per-bone pass for the character's own state.
- **Reviewer:** single mechanic auditor. Per-entry verdict: CORRECT (all three axes earned, no anti-pattern fired) or INCORRECT (named axis-failure or anti-pattern). Per-skip verdict: SKIP-CORRECT (no field changed at this beat) or SKIP-MISSED (a field genuinely changed and no entry fired). File-level verdict: SHAPE-OK / SHAPE-FAIL with named density / target-diversity / cross-facet failure mode. Cross-facet contract pre-ship check is mandatory.
- **No dialect audience.** State-updates is mechanic-dense, not voice-dense. Dialect-audience calibration is preserved for dialogue/prose/narrator-interest work; state-updates does not invoke it.
- **Verdict combination:** single-gate. Mechanic auditor's verdict is final.
- **Cull:** state-updates has per-file cull (per `schemas/facet.schema.md`). Cull is delete-only — entries that fail any axis or any anti-pattern are deleted. No rewrites at cull time. The Phase 2 writer outputs ARE the cull-stage authoring; revision happens in Phase 4 only.
- **Floor defense.** If an author defends a NONE against a reviewer push to FIRE by citing rubric (no field changed; or field-change but @39-class held-against-turn forbids), accept the defense. Sparsity is load-bearing; over-firing corrupts canonical memory by writing back transients as state.
- **Ceiling defense.** If an author defends a FIRE that the reviewer would push to NONE, the burden is on the author to name (a) which field on which target changed, (b) the persistence past this beat, (c) the cross-facet contract slot the entry serves (peak-bones co-citation expectation; narrator-interest co-citation if POV actor-state). A FIRE that survives ceiling defense should also pass the strip-test and the persistence-test.
- **Cross-author dependencies.** Where two authors co-write the same beat (studio writes `prop:letter.holder` at @38; Taylor fork writes `actor:taylor.posture` at @38), the entries must be consistent. Phase 5 cross-unit dependency check is mandatory; pairs of entries that interact on the same beat get adjudicated together, not in isolation.

---

## V1 lenient form (retained for lift comparison only)

V1: ACCEPT iff the entry is form-correct (well-formed target, field, old, new, anchored to a real proto-line) AND the anchor proto-line is plausibly an action-or-transition beat. No reality test, no cross-facet check, no POV-restriction check, no curve-shape check.

V1 exists only to produce a baseline accept-rate for round-trip comparison after writer-tuning. It is not an authoring target. Do not soften V2 toward V1 between rounds.

---

## What state-updates is not

- Not registration. Narrator-interest, scene-map pressure-signal, and audience-interest carry registration. State-updates carries the structural delta.
- Not perception. The POV character's perception of state-changes lives in narrator-interest; the canonical state-change lives here.
- Not posture-noting. Most posture is body-charge territory (reads from substance_delta). Posture-as-state requires multi-beat persistence AND load-bearing on the next move.
- Not editable after cross-facet consistency. Once locked, entries are an input to the showrunner's canonical write-back; cannot be retuned without restarting the consistency pass.
- Not symmetric across POV authors. Each author writes their own target class. Cross-target writing is an authority violation.
- Not asymmetric across episodes. The rubric's structure transfers across episodes; the calibration anchors and the field-extensions for s01e01 do not transfer mechanically — each episode's anchors and extensions are re-derived.
