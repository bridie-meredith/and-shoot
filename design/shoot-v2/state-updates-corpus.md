# State-Updates Corpus — s01e01 (Phase 0 prep)

Corpus selection for the state-updates facet tuning run on s01e01 (77 proto-lines).

## Authority

- Proto-lines: `active-project/theater/proto-lines/s01e01.md`
- Locked tensometer file: `active-project/theater/facets/tensometer.md`
- Locked narrator-interest file: `active-project/theater/facets/interest-narrator.md`
- Rubric: `design/shoot-v2/rubric-state-updates.md`
- Studio state schema: `active-project/staff/studio/state.md` (sections: location, time_of_day, weather, active_conditions, prop_positions, actor_positions, doors_and_shutters, spatial_layout, ambient, fauna_sense_status)
- Actor cards: `active-project/actors/{taylor-hebert-westeros,census-officer,clerk,mira-stonefield,edric-cray,septon-dying-protector}/`
- Prop cards: scan `cards/props/` for any letter / ledger / stylus / district-ledger / wardship-document / etc. (Project notes: most s01e01 props are warehouse-only `oc-*` extensions, not card-authored.)

## Sample shape

Phase 1 (baseline): unfiltered naive author authors a state-updates file across all 77 proto-lines, blind to this rubric. Mechanic auditor reviews under V1 lenient + V2 strict.

Phase 2 (writer-fork): stratified intent set, ~12 intents covering the full target × authorship matrix:

| Stratum | Anchors | Author class | Reality call (rubric prediction) |
|---|---|---|---|
| Calibration: irreversible bureaucratic registration | @64 (parallel marks) | studio (prop:district-ledger) + Taylor fork (actor:taylor.knowledge) | FIRE both |
| Calibration: prop holder-flip | @38 (Taylor presents letter), @45 (Taylor receives back) | studio (prop:letter) | FIRE @38, FIRE @45 |
| Held-against-turn (forbidden) | @39 (Taylor's feet committed) | Taylor fork (actor:taylor.posture or none) | NONE per tensometer @39 STATE-UPDATE NOTE |
| Registration-only (forbidden) | @23 (officer's gaze fixes), @24 (stylus stops) | various | NONE on all (perception/momentary; no field change) |
| Position-change | @14 (Taylor crosses 12 feet), @19 (stops in line), @37 (steps into officer's path) | Taylor fork (actor:taylor.position) | NONE on @14 @19 (within-scene movement, position is approximate), MAYBE @37 (steps into shoulder-path; persistent across @38–@39) |
| Non-POV actor position-change | @57 (edric steps back through door) | Edric fork (actor:edric.position) + studio (door state if applicable) | FIRE @57 on actor:edric.position; FIRE on studio.cottage-door if door-close beat establishes |
| Knowledge-acquisition (POV actor-state) | @48 (officer dictates "provisional") | Taylor fork (actor:taylor.administrative-status); studio (prop:district-ledger.entry) | FIRE both; narrator-interest co-citation REQUIRED on actor:taylor entry (narrator-interest @48 confirmed) |
| Cross-POV authority violation (anti-pattern test) | @52 (Taylor sees Mira's eyes drop) | Taylor fork attempts actor:mira.engagement-state | REJECT (cross-POV authoring) |
| Studio environment-state (rare) | @11 (officer comes through gate — yard population shifts) | studio (studio.actors_in_yard) | MAYBE FIRE — persistence across the rest of the scene; verify cross-facet |
| Stylistic-noting trap | @50 (Taylor turns to mira) | Taylor fork attempts actor:taylor.facing | NONE (transient turn, not persistent posture) |
| Compound-trap | @38–@39 combined | Taylor fork attempts compound entry | REJECT (compound; must split) |
| Drift-old trap | @43 prop:letter.holder cited as `taylor -> taylor` (drift-old) | studio | REJECT |

Total target: ~12 intents, decision matrix exercised across reality / authority / frugality + cross-facet contract + POV-restriction.

## Phase 1 baseline approach

A naive author writes a state-update entry for every proto-line they can plausibly read as an action/transition beat. Author is blind to the rubric. Expected naive-baseline behavior:

- Fires on every motion verb (`crosses`, `steps`, `stops`, `turns`) — high density-on-flat contamination.
- Fires on registrations (`gaze fixes`, `stylus stops`) — registration-as-state contamination.
- May write cross-POV entries (Taylor fork writes `actor:officer.posture`).
- Likely fields are mostly position / posture; under-cites prop:* and knowledge.*.

Expected V2 strict accept rate: low (≤25%), since registration-as-state and density-on-flat are the dominant naive failure modes for this facet.

Expected V2 strict naive baseline file size: 30–60 entries on 77 beats (high density).

## Field universe (Phase 0 enumeration)

Tracked-state fields the rubric admits (s01e01 specific):

**`actor:taylor`:**
- position (which sub-region of yard / line / threshold)
- posture (when persistent across beats, load-bearing)
- inventory (letter held / not held)
- knowledge.record-state (what she knows about the canonical record)
- knowledge.officer-disposition (what she knows about how the officer ruled)
- administrative-status (`unenrolled` → `provisional-labor-eligible` at @48)
- mask-state (mask-on / mask-thinning) — narrator-interest @77 confirms a mask shift; corresponding state may fire
- exposure-state (low / committed / paid) — @38 commits exposure

**`actor:officer`, `actor:clerk`, `actor:mira`, `actor:edric`:**
- position (in/out of yard, through-door, etc.)
- posture (when persistent)
- focus / attention-target (when persistent and load-bearing)
- (other actor-specific fields per their persona card)

**`studio`:**
- actors_in_yard (membership set; changes on entry/exit)
- doors_and_shutters.* (open/closed)
- prop_positions.* (delegated to `prop:*` entries; studio writes positions when no individual prop card)
- active_conditions.* (rare in s01e01; possible at @48 if administrative-status acquisition activates a condition flag)
- time_of_day (rare in scene-internal beats)
- weather (rare in scene-internal beats)

**`prop:letter`:**
- holder (`taylor` → `mid-air-between-them` → `officer-hand` → `mid-air-between-them` → `taylor`)
- physical_condition (sealed → unsealed at @41)
- seal-condition (intact → broken at @41)

**`prop:district-ledger` (oc-* extension):**
- taylor-entry (pending → dictated-provisional → marked-parallel-margin)
- pen-state (writing → stopped @24 → resumed @58 → resting @59 — only if persistence holds; many of these are transient)

**`prop:stylus`:**
- (mostly transient motor states; few persistent state-changes; usually NOT a state-update target unless something locks)

## Anti-corpus (intentional negative cases)

The corpus deliberately includes anchors that should NOT fire under V2:

- @23, @24: registration-only beats (officer's gaze, stylus-stop)
- @39: tensometer-locked NONE (held-against-turn)
- @50, @55, @56: transient turns / momentary gaze-shifts
- @1–@10: ambient establishing (stable state, no deltas)
- @60: officer's near foot angled (charged stillness, body-charge per tensometer; not canonical state)

These exercise the auditor's REJECT signatures and the SKIP-CORRECT verdict path.

## Notes for Phase 1

- The naive baseline author should NOT see this corpus note. They see only the proto-line file and the schema's state-updates entry-form.
- The mechanic auditor sees: rubric, locked tensometer, locked narrator-interest, this corpus note, the proto-line file, the relevant actor/studio/prop schemas.
- Decision-accuracy stratum is the SECONDARY measurement (FIRE-CORRECT / NONE-CORRECT across the 12 stratified intents); rubric-correctness is the PRIMARY measurement.
