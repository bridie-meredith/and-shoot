# Fixer Report — Phase 2 Collation, s01
# target: active-project/theater/proto-lines/s01.bones.md
# session: 2026-05-11T09:00:00Z — season-s01-pass-2-fix-round2
# audit sources: season-s01-pass-2-constraint.md + season-s01-pass-2-continuity.md

---

## Group counts

| Group | Fault | Count | Status |
|-------|-------|-------|--------|
| GROUP 1 — REFERENCE-DRIFT | FAULT-SLUG-DRIFT-01 | ~30 lines | RESOLVED (prior session) |
| GROUP 2 — POV-LEAKS | FAULT-POV-LEAK-01/02/03 | 6 lines | RESOLVED (prior session) |
| GROUP 3 — PROP-STATE | FAULT-PROP-STATE-01 | structural gap | FLAGGED-FOR-SCREEN-WRITER |
| GROUP 4 — FORM-PERCEPTION | marks ×17, reads aloud ×2 | 19 | RESOLVED (mix of prior + this session) |
| GROUP 5 — FORM-MODIFIER | prepositional padding | 45 | RESOLVED |
| GROUP 6 — FORM-INTERIORITY | maps ×3, recalculates, routes-abstract, relay-abstract, thin-abstract | 11 | RESOLVED |
| GROUP 7 — FORM-NON-ACTION-VERB | receive ×2 (deleted), fill ×1 | 3 | RESOLVED |
| GROUP 8 — SLUG-UNRESOLVED | "a new arrival" | 1 | RESOLVED |
| GROUP 9 — RELAY-POLICY | ~35 relay bones | policy flag | FLAGGED-FOR-SCREEN-WRITER |

---

## Group 1 — REFERENCE-DRIFT

Confirmed resolved in prior session. All 25+ post-beat-16 bones now use `oc-broken-maester`; IDs 111–301 correctly retain `the maester` for the pre-naming period. No occurrences of `the maester` appear at ID 303 or later.

---

## Group 2 — POV-LEAKS

Confirmed resolved in prior session:
- IDs 157, 158: blank (south gate entry deleted — offstage outside 300m radius)
- IDs 203, 204: blank (recipient-state assertions deleted — no relay coverage)
- IDs 282, 283: blank (stairwell pause beats deleted — stairwell interior coverage not established)

Beat structure remains coherent: 159 (junction crossing) → 281 (enters stairwell) → 284 (enters upper room) without the offstage/uncovered beats.

---

## Group 3 — PROP-STATE — FLAGGED FOR SCREEN-WRITER

**FAULT-PROP-STATE-01:** Log opened at ID 201, written at ID 202 — no close-log bone — then opened again at ID 205. IDs 203/204 are now blank (deleted under Group 2 POV-LEAK-03). The close-log bone that belongs between ID 202 and ID 205 cannot be inserted by fixer (fixer does not introduce new IDs).

**Screen-writer REGEN-ADD required:** Author `taylor-hebert-flea-bottom closes the log` between IDs 202 and 205. Since IDs 203 and 204 are deletion gaps, the close-log can occupy one of those ID slots (IDs are stable — a previously-deleted ID can be repurposed by screen-writer per approval, or a new ID sequence can be inserted with the next available ID). Recommend: screen-writer proposes the close-log bone at one of the gap IDs and confirms with showrunner before committing. The beat-10 transmission gap (carters/dock-workers receiving data) also needs screen-writer attention as noted in the continuity audit.

---

## Group 4 — FORM-PERCEPTION

All 19 faults resolved. Breakdown:

**Resolved in prior session (pre-existing fixes confirmed):**
- ID 14: `marks the stillness` → `stills`
- ID 17: `marks the pivot angle` → `tilts the head`
- ID 66: `marks taylor-hebert-flea-bottom` → `slows the step`
- IDs 109, 113, 123, 223, 224, 271, 272, 352, 353, 446, 447: `marks the grid notation` → `writes the entry` (11 instances)
- ID 111: `reads aloud in the upper room` → `speaks to the room`
- ID 129: `reads aloud` → `speaks`
- ID 166: `marks the half-second` → `holds the step`

**Resolved this session:**
- ID 170: `oc-tanner-father marks the scan pattern` → `oc-tanner-father stills`
- ID 171: `oc-tanner-mother marks the scan pattern` → `oc-tanner-mother stills`

**Judgment calls:**
- IDs 170/171 recasting to `stills` is consistent with the parent pattern (father and mother registering a behavioral tell externally observable). The auditor's suggested recast for the `marks` pattern on observing-parents was `stills` or `holds the step`. `stills` chosen as minimum change (same as ID 14).

---

## Group 5 — FORM-MODIFIER

All 45 auditor-listed instances resolved. Line-by-line:

| ID | Old form | New form | Note |
|----|----------|----------|------|
| 1 | `wakes in the tanner-family bed` | `wakes` | intransitive; bed is loc-state |
| 8 | `extends the arm toward the salt` | `reaches the salt` | transitive verb takes location as direct object |
| 42 | `holds the eyes forward` | `holds the eyes` | drop adverb |
| 49 | `routes oc-tanner-mother toward the pit` | `routes oc-tanner-mother` | drop destination |
| 50 | `routes the neighbor-boy toward the pit` | `routes the neighbor-boy` | drop destination |
| 52 | `crosses the yard toward the pit` | `crosses the yard` | drop destination |
| 56 | `routes oc-tanner-mother toward the central work` | `routes oc-tanner-mother` | drop destination |
| 57 | `routes the neighbor-boy toward the central work` | `routes the neighbor-boy` | drop destination |
| 65 | `crosses the far side of the yard` | `crosses the yard` | drop adjective + prep phrase |
| 91 | `walks the road toward King's Landing` | `walks the road` | drop destination |
| 105 | `walks the 300m perimeter` | `walks the perimeter` | drop measurement modifier |
| 107 | `the flies relay the apothecary doorframe` | `the flies relay the doorframe` | drop adjective |
| 108 | `the spiders spread the apothecary ceiling corners` | `the spiders spread the ceiling corners` | drop adjective |
| 112 | `the beetles relay the upper-room sound` | `the beetles relay the sound` | drop adjective |
| 122 | `the spiders relay the apothecary upper room` | `the spiders relay the room` | drop adjective compound |
| 128 | `the maester crosses the upper room` | `the maester crosses the room` | drop adjective |
| 222 | `walks the new perimeter` | `walks the perimeter` | drop adjective (replace_all applied to 222, 270, 351, 445 simultaneously) |
| 232 | `the lords-man enters the alley two blocks south` | `the lords-man enters the alley` | drop positional qualifier |
| 235 | `the lords-man's man moves the family possessions into the alley` | `the lords-man's man moves the family possessions` | drop prepositional destination |
| 240 | `the flies relay the room-adjacent wall` | `the flies relay the wall` | drop adjective |
| 255 | `taylor-hebert-flea-bottom extends the coins toward oc-tanner-father` | `taylor-hebert-flea-bottom extends the coins` | drop prepositional destination |
| 270 | `walks the new perimeter` | `walks the perimeter` | (covered by replace_all above) |
| 296 | `the beetles relay the pen-scratch rhythm` | `the beetles relay the rhythm` | drop adjective |
| 297 | `the beetles relay the spoken phrase` | `the beetles relay the phrase` | drop adjective |
| 298 | `the beetles relay the pen-scratch rhythm` | `the beetles relay the rhythm` | drop adjective |
| 303 | `oc-broken-maester crosses the upper room` | `oc-broken-maester crosses the room` | drop adjective |
| 304 | `oc-broken-maester descends the interior stair` | `oc-broken-maester descends the stair` | drop adjective |
| 307 | `the beetles relay oc-broken-maester's footfall` | `the beetles relay the footfall` | drop possessive modifier |
| 308 | `oc-broken-maester returns the stairwell` | `oc-broken-maester enters the stairwell` | fix non-standard transitive returns; enter is the correct transitive |
| 310 | `the beetles relay the return footfall` | `the beetles relay the footfall` | drop adjective modifier |
| 315 | `oc-tanner-mother arrives at loc-flea-bottom-base` | `oc-tanner-mother enters loc-flea-bottom-base` | fix prepositional arrival; enters takes location as direct object |
| 351 | `walks the new perimeter` | `walks the perimeter` | (covered by replace_all above) |
| 400 | `oc-broken-maester descends the interior stair` | `oc-broken-maester descends the stair` | drop adjective |
| 403 | `the beetles relay oc-broken-maester's footfall` | `the beetles relay the footfall` | drop possessive modifier |
| 405 | `oc-broken-maester approaches the dried-goods stall` | `oc-broken-maester approaches the stall` | drop adjective |
| 410 | `oc-broken-maester faces the dried-beetle jars` | `oc-broken-maester faces the jars` | drop adjective |
| 412 | `the beetles relay oc-broken-maester's return footfall` | `the beetles relay the footfall` | drop possessive + adjective modifiers |
| 414 | `oc-broken-maester ascends the interior stair` | `oc-broken-maester ascends the stair` | drop adjective |
| 416 | `the beetles relay the pen-scratch onset` | `the beetles relay the onset` | drop adjective |
| 417 | `the beetles relay the pen-scratch continuation` | `the beetles relay the continuation` | drop adjective |
| 418 | (same) | (same) | drop adjective |
| 419 | (same) | (same) | drop adjective |
| 442 | `the flies spread the Fish Gate comprehensive pass` | `the flies spread the Fish Gate pass` | drop adjective |
| 443 | `the wasps spread the Fish Gate margin south approach` | `the wasps spread the Fish Gate approach` | drop positional adjective |
| 445 | `walks the new perimeter` | `walks the perimeter` | (covered by replace_all above) |

**Items 157/158 counted in modifier list:** Resolved by Group 2 deletion. Via-the-south-gate padding eliminated with the bone.

**Retained:** `pivots toward <X>` forms (IDs 9, 11, 16, 165, 178, 179) — schema explicitly licenses `pivots toward <X>` when motion-in-progress is required. Not faulted.

**Structural side-effect noted for screen-writer:** After dropping possessive/adjective modifiers, multiple beetle-relay bones in beat 16 (IDs 307 and 310) now both read `the beetles relay the footfall`, and in beat 22 (IDs 403 and 412) both also read `the beetles relay the footfall`. These are contextually distinct beats (maester descending vs. returning; maester going to market vs. returning from market) but are now worded identically. Screen-writer should differentiate with distinct concrete objects if the beats are load-bearing.

---

## Group 6 — FORM-INTERIORITY

All 11 auditor-identified interiority faults resolved:

| ID | Old form | New form | Method |
|----|----------|----------|--------|
| 86 | `oc-tanner-elder routes the labor-web placement` | `oc-tanner-elder speaks to oc-tanner-father` | abstract plan-noun → speech-act |
| 130 | `the beetles relay the south-wall return` | `the beetles relay the south-wall footfall` | abstract event-noun → concrete sensory object |
| 140 | `oc-dock-runner recalculates the route` | `oc-dock-runner pivots` | cognitive verb → observable physical act |
| 145 | `oc-tanner-elder routes the inquiry` | `oc-tanner-elder speaks to oc-dock-runner` | abstract routing → speech-act |
| 174 | `oc-tanner-elder routes the trade` | `oc-tanner-elder speaks to oc-tanner-father` | abstract routing → speech-act |
| 189 | `taylor-hebert-flea-bottom maps the junction relay node` | (blank — deleted) | cognitive mapping is narrator-facet territory |
| 191 | `taylor-hebert-flea-bottom maps the Fish Gate relay node` | (blank — deleted) | same |
| 193 | `taylor-hebert-flea-bottom maps the north relay node` | (blank — deleted) | same |
| 381 | `oc-tanner-elder routes the Fish Gate task` | `oc-tanner-elder speaks to taylor-hebert-flea-bottom` | abstract routing → speech-act |
| 386 | `taylor-hebert-flea-bottom routes the information hand-off` | `taylor-hebert-flea-bottom speaks to the dock-side cluster` | abstract routing → speech-act |
| 390 | `the flies thin the dock-side relay` | `the flies retract` | abstract communications-relay object → physical creature-act |

**Judgment calls:**

- **ID 86** recast to `speaks to oc-tanner-father` creates a pair with ID 83 (`oc-tanner-elder speaks to oc-tanner-father`). Two adjacent speak-to-father beats are structurally redundant. Flagged for screen-writer to differentiate (different recipients, or a more concrete elder-directive act).

- **ID 130** retained as a bone (not deleted) because the auditor's guidance was "recast: `the beetles relay the south-wall footfall` (concrete noun) if the beat must remain; or render the maester's return as its own physical SVO." The surrounding context (ID 128: maester crosses room, ID 131: Taylor straightens spine) supports retaining a relay beat. `footfall` is a concrete sensory object, resolving the abstract-event-noun fault.

- **IDs 189, 191, 193** deleted (blank gaps) per auditor recommendation. The mapping acts are internal cognition delivered by the surrounding relay bones (IDs 187, 188, 190, 192). No structural gap results: the relay bones establish what was observed; the mapping was always a facet-level interpretation of those observations.

- **ID 381** creates a third `speaks to taylor-hebert-flea-bottom` for the elder within this stretch (IDs 378, 381, 392). Structurally redundant. Flagged for screen-writer.

- **ID 386** — `dock-side cluster` is an insect cluster, not a named character. `speaks to the dock-side cluster` uses the `the <noun>` form correctly for an unnamed environment-element group. The dialogue content (what Taylor says to the cluster) is facet territory.

---

## Group 7 — FORM-NON-ACTION-VERB

All 3 faults resolved:
- IDs 203, 204 (`receive`): resolved by Group 2 deletion
- ID 237 (`fill the doorways`): recasted to `press the doorways`

**Judgment call on ID 237:** `press` is an active physical verb (the neighbors pushing into the doorway space). `lean the doorframes` (auditor's alternative) was not chosen — `press the doorways` captures the crowd motion with the doorway as the target of the action, consistent with SVO form.

---

## Group 8 — SLUG-UNRESOLVED

- ID 164: `a new arrival enters the junction` → `the arrival enters the junction`

Indefinite article eliminated. `the arrival` uses the `the <noun>` form licensed by schema for unnamed environment elements. The character does not appear to receive a slug elsewhere in the bones.

---

## Group 9 — RELAY-POLICY — FLAGGED FOR SCREEN-WRITER

**flag-001:** ~35 `<insect> relay <X>` bones are technically permitted under current schema but svo-split-notes #1 suggests fauna-perception-transmission belongs in sensory/narrator facets, with the bone representing only the physical creature-act.

**No modification applied.** This is a structural policy decision, not a line-level fault.

**Screen-writer question:** Does the production policy for the insect-relay system keep `relay` bones as proto-lines (current state), or strip them to physical-creature-act bones (e.g., `the beetles reposition`, `the flies spread`) with the sensory-transmission content moving entirely to sensory/narrator facets? The answer affects ~35 bones and the facet-authoring contract for all insect-coverage scenes. This should be decided before Phase 3 (shape pass) consumes the bones file.

---

## Additional flags not in audit (out of scope — noted only)

These were observed during the fix pass but are NOT in the auditor's report. They are flagged here for awareness; no edit was applied:

- **ID 29:** `the wasps relay the south-wall return` — same abstract-event pattern as ID 130 (south-wall return) but not listed in the audit. Post-fix audit may catch this.
- **ID 256:** `oc-tanner-father receives the coins` — `receives` is a non-action verb (same class as faulted IDs 203/204). Not listed in audit.
- **ID 469:** `the middleman receives the sealed account` — same class, not listed.
- **ID 411:** `oc-broken-maester exits the dried-goods stall` — `dried-goods` adjective modifier on object, same class as faulted ID 405. Not listed in audit.
- **ID 490:** `taylor-hebert-flea-bottom returns loc-flea-bottom-base` — `returns` with location as object (same non-standard pattern as audited ID 308). Not listed.
- **IDs 338, 372:** `relay the clerk's departure path`, `relay the second clerk's departure path` — possessive modifiers, same class as audited IDs 307/403/412. Not listed.
- **ID 280:** `the visitor arrives at the maester's side-alley door` — compound adjective + prepositional padding. Not listed.
- **ID 165:** `pivots toward the arrival` — `pivots toward` is schema-licensed; not a fault.

These are candidates for a follow-up Pass 2 sweep.

---

## Structural repetition flags (for screen-writer)

After this fix pass, the following sets of identically-worded bones now exist. Each pair or group represents distinct physical moments but the bone-level wording is identical. Screen-writer should differentiate them with concrete objects when the distinction matters for facet authoring:

1. **IDs 307 and 310:** Both now `the beetles relay the footfall` (maester descending from room vs. returning from stairwell)
2. **IDs 403 and 412:** Both now `the beetles relay the footfall` (maester going to market vs. returning)
3. **IDs 83 and 86:** Both `oc-tanner-elder speaks to oc-tanner-father` (introduction vs. labor-routing directive)
4. **IDs 378 and 381 and 392:** All `oc-tanner-elder speaks to taylor-hebert-flea-bottom` within beat 19-21 stretch
5. **11 bones across season:** `taylor-hebert-flea-bottom writes the entry` for grid-notation moments (IDs 109, 113, 123, 223, 224, 271, 272, 352, 353, 446, 447) — range-expansion-formula repetition; pre-existing issue from prior session

---

## Screen-writer REGEN-ADD task list

1. **Close-log bone (ID gap 203 or 204):** `taylor-hebert-flea-bottom closes the log` between IDs 202 and 205 to fix FAULT-PROP-STATE-01. Fixer cannot introduce new IDs. Screen-writer may repurpose a gap ID or add the next available ID with showrunner approval.

2. **Beat-10 transmission gap:** With IDs 203/204 deleted, the carters and dock-workers receiving the data is no longer represented in bones. Screen-writer should decide whether a replacement bone is needed (e.g., `the flies relay the carter receipt` from a covered handoff point) or whether the transmission gap is acceptable as documented.

3. **Relay-policy decision (Group 9):** Define whether `relay` bones stay as proto-lines or strip to physical-creature-act bones before Phase 3.

4. **Structural repetition differentiation (above):** Differentiate identically-worded beetle-relay footfall bones (307/310, 403/412) and adjacent elder-speaks bones (83/86) using concrete distinguishing objects.

---

## Final verdict

**ALL-CRITERIA-MET** for the 78 individually-listed fault instances (Groups 1–8) that fixer was responsible for resolving.

**PARTIAL-{2-unresolved}:** The two items that cannot be resolved at fixer scope:
1. FAULT-PROP-STATE-01 close-log bone (requires screen-writer REGEN-ADD)
2. GROUP9 relay-policy (requires screen-writer policy decision, not a line fault)

Both unresolved items are structural/policy matters correctly routed to screen-writer. All individual line faults in the audit are resolved.
