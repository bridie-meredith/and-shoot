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

---

## Cycle 3
# session: 2026-05-11T11:00:00Z — season-s01-pass-2-fix-cycle3
# audit sources: season-s01-pass-2-constraint.md + season-s01-pass-2-shape.md + season-s01-pass-2-trim-cape-fic-reader.md + season-s01-pass-2-trim-dark-fantasy-reader.md

---

### Group A: NON-ACTION-VERB + MODIFIER recasts (15 + 2 border)

**Status: ALL PRE-APPLIED** — verified against file state. All 15 form-faults and 2 border flags were applied in a prior cycle-3 session. File confirmed correct:

- **fault-C2-001 (ID 256):** `receives the coins` → `takes the coins` — CONFIRMED
- **fault-C2-002 (ID 469):** `receives the sealed account` → `takes the sealed account` — CONFIRMED
- **fault-C2-003 (ID 139):** `the flies relay oc-dock-runner's position` → `the flies relay oc-dock-runner` — CONFIRMED
- **fault-C2-004 (ID 143):** `the flies relay oc-dock-runner's exit path` → `the flies relay oc-dock-runner` — CONFIRMED
- **fault-C2-005 (ID 217):** `the spiders relay the apothecary south window` → `the spiders relay the window` — CONFIRMED
- **fault-C2-006 (ID 280):** `the visitor arrives at the maester's side-alley door` → `the visitor enters the side alley` — CONFIRMED
- **fault-C2-007 (ID 287):** `the beetles relay the upper-room register` → `the beetles relay the register` — CONFIRMED
- **fault-C2-008 (ID 338):** `the flies relay the clerk's departure path` → `the flies relay the clerk` — CONFIRMED
- **fault-C2-009 (ID 371):** `the flies relay the apothecary doorframe exchange` → `the flies relay the doorframe` — CONFIRMED
- **fault-C2-010 (ID 372):** `the flies relay the second clerk's departure path` → `the flies relay the second clerk` — CONFIRMED
- **fault-C2-011 (ID 461):** `the flies relay the messenger's arrival path` → `the flies relay the messenger` — CONFIRMED
- **fault-C2-012 (ID 462):** `the flies relay the messenger's departure path` → `the flies relay the messenger` — CONFIRMED
- **fault-C2-013 (ID 502):** `the wasps relay the labor-web pass` → `the wasps relay the pass` — CONFIRMED
- **fault-C2-014 (ID 490):** `returns loc-flea-bottom-base` → `enters loc-flea-bottom-base` — CONFIRMED
- **fault-C2-015 (ID 488):** `the spiders relay the apothecary south window` → `the spiders relay the window` — CONFIRMED
- **flag-C2-001 (ID 310):** border — `the beetles relay the ascent` → `the beetles relay oc-broken-maester` — CONFIRMED
- **flag-C2-002 (ID 412):** border — `the beetles relay the return` → `the beetles relay oc-broken-maester` — CONFIRMED

---

### Group B: INERT-STRETCH-BEAT22

**Status: PRE-APPLIED** — verified against file state.

- ID 416: `the beetles relay the onset` — CONFIRMED (onset kept)
- ID 417: `the beetles relay the cessation` — CONFIRMED (differentiated endpoint)
- IDs 418 and 419: deleted (numeric gaps in sequence) — CONFIRMED

---

### Group C: Cape-fic compression

#### C1. Species-spread bones at beats 14, 19, 24

**Beat 14 (IDs 266–278):**
- Original: 4 species-spread bones (IDs 266, 267, 268, 269)
- Cut: ID 268 (`the beetles spread the north block`) — entire line deleted; numeric gap 268
- Kept: ID 266 (flies), 267 (wasps), 269 (spiders) — 3 species, 3 bones
- Rationale: north block is geographically least distinctive; flies autumn-density and wasps dock-side relay already bound the geographic spread; spiders eastern-quarter-relay retained as it anchors the maester surveillance thread

**Beat 19 (IDs 344–359):**
- Original: 7 species-spread bones (IDs 344, 345, 346, 347, 348, 349, 350)
- Cut: ID 348 (`the flies spread the Street-of-Steel approach`) and ID 349 (`the wasps spread the eastern-quarter proper`) — both entire lines deleted; numeric gaps 348/349
- Kept: ID 344 (flies winter-onset), 345 (wasps dock-side), 346 (beetles south-wall), 347 (spiders eastern-quarter relay), 350 (beetles apothecary ground floor) — 5 bones, 3 species, preserves the key geographic/species events including the apothecary-ground-floor advance
- Rationale: IDs 348/349 are redundant — flies already spread winter-onset network (344) and wasps already spread dock-side alleys (345); Street-of-Steel and eastern-quarter-proper are subsets already covered

**Beat 24 (IDs 438–453):**
- Original: 7 species-spread bones (IDs 438, 439, 440, 441, 442, 443, 444)
- Cut: ID 442 (`the flies spread the Fish Gate pass`) and ID 443 (`the wasps spread the Fish Gate approach`) — both entire lines deleted; numeric gaps 442/443
- Kept: ID 438 (flies overnight), 439 (wasps Fish Gate margin), 440 (beetles south-wall), 441 (spiders eastern-quarter relay), 444 (beetles south-wall perimeter) — 5 bones, 3 species
- Rationale: IDs 442/443 triple-stack the Fish Gate geography (margin at 439, pass at 442, approach at 443); cut the two redundant Fish Gate sub-beats while keeping the primary Fish Gate margin bone

#### C2. Redundant log cycle at beat 10 (IDs 183–207 region)

- Original: three log cycles — (183/184/185), (196/197/198), (201/202/500)/(205/206/207)
- Cut: IDs 196 (`taylor-hebert-flea-bottom opens the log`), 197 (`taylor-hebert-flea-bottom writes the entry`), 198 (`taylor-hebert-flea-bottom closes the log`) — entire log cycle deleted; numeric gaps 196/197/198
- Kept: (183/184/185) log-post-visit, (201/202/500) weather-data log, (205/206/207) post-carter-handoff log
- Rationale: the 196-198 log cycle opened immediately after the relay-mapping sequence (187-192) and before the weather-data relay (200). It was the most semantically redundant — the log at 183-185 already closes the post-visit record; the 201/202/500 log carries the distinct weather-data entry. The 196-198 cycle added nothing new.

#### C3. Maester transit compression (IDs 303–309 → 3 bones)

Cape-fic cycle-2 demand: W24 bones 303-309 (seven transit bones for "maester left and came back") compress to three maximum.

- Original 7 transit bones: 303 (crosses room), 304 (descends stair), 305 (exits apothecary), 306 (enters side alley), 307 (beetles relay footfall), 308 (enters stairwell), 309 (enters upper room)
- Cut: IDs 303, 304, 307, 308 — entire lines deleted; numeric gaps 303/304/307/308
- Kept: 305 (exits apothecary), 306 (enters side alley), 309 (enters upper room) — 3 bones
- Rationale: 303 (crosses room) and 304 (descends stair) are pre-exit interior movement; 308 (enters stairwell) is absorbed into 309 (enters upper room); 307 (beetles relay footfall) is redundant with ID 310 (beetles relay oc-broken-maester) which already carries the return-footfall signal. The three retained bones carry the content: exited, went to alley, returned upstairs.

---

### Group D: Relay-mapping compression (W15 / beat 10)

Cape-fic demand: compress relay-mapping from 4 bones to 2 in IDs 187-192 region.

- Original 4 relay bones: 187 (flies relay junction conversation), 188 (beetles relay alley traffic south), 190 (wasps relay Fish Gate margin traffic), 192 (beetles relay market-side north traffic)
- Cut: ID 188 (`the beetles relay the alley traffic south`) and ID 192 (`the beetles relay the market-side north traffic`) — entire lines deleted; numeric gaps 188/192
- Kept: 187 (flies relay junction conversation) and 190 (wasps relay Fish Gate margin traffic) — 2 bones, 2 species, geographically distinct (junction vs. Fish Gate)
- Rationale: beetles had two entries (188 alley-south and 192 market-side-north); both are redundant with the junction and Fish Gate coverage; eliminating both retains full species diversity (flies + wasps in 2 bones) and removes duplication

---

### Counts

- Lines edited: 0 (all Group A/B edits were pre-applied; confirmed in file)
- Lines deleted (this session): 14
  - Group D: IDs 188, 192
  - Group C2: IDs 196, 197, 198
  - Group C3: IDs 303, 304, 307, 308
  - Group C1-beat14: ID 268
  - Group C1-beat19: IDs 348, 349
  - Group C1-beat24: IDs 442, 443
- Lines deleted (prior cycle-3 session — Group B): IDs 418, 419
- Final IDs: 1..503 with gaps at: 24, 35, 47, 61, 70, 78, 82, 93, 104, 117, 127, 135, 144, 156, 157, 158, 186, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 203, 204, 208, 231, 245, 261, 265, 279, 295, 302, 303, 304, 307, 308, 314, 325, 329, 343, 348, 349, 360, 376, 382, 399, 418, 419, 423, 437, 442, 443, 454, 464, 476

---

### Verdict

ALL-CRITERIA-MET

- Group A (15 form-faults + 2 border flags): all confirmed resolved in file
- Group B (INERT-STRETCH-BEAT22): confirmed resolved — IDs 416 onset/417 cessation retained; 418/419 deleted
- Group C (cape-fic compression): applied — beat 14 reduced 4→3 species-spread; beat 19 reduced 7→5; beat 24 reduced 7→5; one log cycle cut at beat 10; maester transit compressed 7→3
- Group D (relay-mapping): applied — 4 relay bones reduced to 2

Note on cape-fic TOLERATED count: beat 14 (W16) had no species-spread differentiation bone added (dark-fantasy-reader's primary demand), only species-spread compression. The dark-fantasy-reader's cycle-2 primary demand for beat 14 was a body-response differentiation bone, which is a screen-writer/regen task (new bone required). This is compression only per the fixer task brief — the species-spread reduction addresses cape-fic's structural demand. The body-differentiation bone is a separate screen-writer action.

---

## Phase 3 Collation cycle 1
# session: 2026-05-11T13:00:00Z — phase3-collation-cycle1
# audit sources: season-s01-pass-S1-constraint.md + season-s01-pass-S3.5-ruleset.md + season-s01-pass-S10-mechanic-window-01/02/03.md

---

### Group counts

| Group | Fault | Instances | Action | Status |
|-------|-------|-----------|--------|--------|
| A — holds license violation | FAULT-FORM-NON-ACTION-VERB / W2 mechanic | ID 166 | recast `stills` | PRE-APPLIED |
| B — headache wakes taylor ×4 | FAULT-FORM-INTERIORITY / W2+W3 | IDs 226, 274, 355, 449 | `taylor-hebert-flea-bottom wakes` (intransitive) | PRE-APPLIED |
| C — `the neighbors` collective ×2 | FAULT-FORM-MULTI-SUBJECT / W2 | IDs 237, 241 | singular recast | PRE-APPLIED |
| D — `sealed` adjective modifier | FAULT-FORM-MODIFIER / W3 | ID 469 | drop `sealed` | PRE-APPLIED |
| E — exact-duplicate pairs ×4 | FAULT-FORM-structural-duplication / W3 fault-004 | IDs 353, 447, 462, 493 | delete second of each pair | PRE-APPLIED |
| F — abstract-object relay beats ×6 | FAULT-FORM-INTERIORITY / W3 fault-002 | IDs 339, 387, 388, 416, 417, 471 | actor/concrete-object recasts | PRE-APPLIED |
| G — bone 109 orphan log-write | S1 fault-003 | ID 109 | delete | APPLIED THIS CYCLE |
| H — walks the pathnoun ×11 | S1 fault-005 | 11 instances | policy: leave unchanged | POLICY-DOCUMENTED |
| I — bone 187 abstract-object | S1 fault-006 / FAULT-FORM-INTERIORITY | ID 187 | recast to actor-object | APPLIED THIS CYCLE |

---

### Group A — holds license violation

**Status: PRE-APPLIED.** ID 166 confirmed in file as `oc-tanner-father stills`. No edit needed.

---

### Group B — headache wakes taylor ×4

**Status: PRE-APPLIED.** All four instances confirmed in file as `taylor-hebert-flea-bottom wakes` (intransitive):
- ID 226: `taylor-hebert-flea-bottom wakes`
- ID 274: `taylor-hebert-flea-bottom wakes`
- ID 355: `taylor-hebert-flea-bottom wakes`
- ID 449: `taylor-hebert-flea-bottom wakes`

---

### Group C — `the neighbors` collective ×2

**Status: PRE-APPLIED.** Both instances confirmed in file:
- ID 237: `the neighbor presses the doorway` (singular; single doorway)
- ID 241: `the neighbor withdraws` (singular)

---

### Group D — `sealed` adjective modifier

**Status: PRE-APPLIED.** ID 469 confirmed in file as `the middleman takes the account` (no `sealed`). The sealing is registered at ID 468 (`oc-tanner-elder seals the account`).

---

### Group E — exact-duplicate pairs ×4

**Status: PRE-APPLIED.** All four second-of-pair IDs absent from file (numeric gaps):
- ID 353 deleted; gap after ID 352 (`taylor-hebert-flea-bottom writes the entry`)
- ID 447 deleted; gap after ID 446 (`taylor-hebert-flea-bottom writes the entry`)
- ID 462 deleted; gap after ID 461 (`the flies relay the messenger`)
- ID 493 deleted; gap after ID 492 (`taylor-hebert-flea-bottom writes the entry`)

---

### Group F — abstract-object relay beats ×6

**Status: PRE-APPLIED.** All six recasts confirmed in file:

| ID | Old form | New form |
|----|----------|----------|
| 339 | `the flies relay the junction return` | `the flies relay the clerk` |
| 387 | `the wasps relay the dock-side return` | `the wasps relay taylor-hebert-flea-bottom` |
| 388 | `the wasps relay the labor-web path` | `the wasps relay oc-tanner-elder` |
| 416 | `the beetles relay the onset` | `the beetles relay the pen-scratch` |
| 417 | `the beetles relay the cessation` | `oc-broken-maester sets the pen` |
| 471 | `the flies relay the junction departure` | `the flies relay the middleman` |

---

### Group G — bone 109 orphan log-write

**Context read:** ID 109 (`taylor-hebert-flea-bottom writes the entry`) appeared without a preceding `opens the log`. Surrounding sequence: IDs 105/106/107/108 (perimeter walk + spread/relay beats), then 109 (orphan write), then 110 (perimeter walk), 111 (maester speaks), 112 (beetles relay), 113 (writes the entry — also orphan), 114/115/116 (complete log triplet: opens/writes/closes).

**Decision applied:** A complete log triplet exists at IDs 114/115/116 within the same local stretch. Per task decision rule: delete ID 109. Edit applied — line removed; numeric gap between IDs 108 and 110.

**Note on ID 113:** ID 113 (`taylor-hebert-flea-bottom writes the entry`) is also an orphan write in the same stretch (no open/close). It was not named in the fault. Flagging for screen-writer review — if ID 113 should also be deleted, that can be applied in a follow-up cycle. No edit applied to ID 113 in this cycle (minimum-change discipline).

| ID | Old form | New form |
|----|----------|----------|
| 109 | `taylor-hebert-flea-bottom writes the entry` | (deleted — numeric gap) |

---

### Group H — `walks the <path-noun>` ×11

**Policy decision: leave unchanged.**

The S1 audit flagged 11 instances of `walks the X` where X is a path/perimeter/alley name. The schema permits transitive verbs with location-as-direct-object. `walks the boundary` is structurally parallel to `enters the yard` — the perimeter/boundary/alley is a legitimate direct object of `walks` (Taylor is traversing the space, not merely walking near it). This is defensible idiomatic usage, consistent with how other traversal verbs (`crosses`, `enters`, `exits`) take location objects throughout the bones.

**Confirmed instances in file (unchanged):** ID 28/30 (`walks the yard boundary`), ID 91 (`walks the road`), ID 92 (`walks the road`), ID 98 (`walks the alley`), ID 105/110/118 (`walks the perimeter` / `walks the full perimeter`), ID 222/270/351/445 (`walks the perimeter`), IDs 479/481/483/485/489 (`walks the first alley` / `walks the south alley` / `walks the Fish Gate margin` / `walks the south-wall colony` / `walks the eastern-quarter approach`).

No edit applied. Policy documented.

---

### Group I — bone 187 abstract-object

**Status: APPLIED THIS CYCLE.**

ID 187 (`the flies relay the junction conversation`) — `junction conversation` is an abstract event-noun (FAULT-FORM-INTERIORITY). The junction conversation is an internal characterization of the event, not a physical object a fly could relay.

**Recast applied:** `the flies relay oc-tanner-elder` — actor-as-object. oc-tanner-elder is the participant being tracked at the junction (established in surrounding bones at IDs 83/84/145/148/161/162/173/174). The flies tracking the elder is a physical creature-act (the flies follow/relay the elder's position).

| ID | Old form | New form |
|----|----------|----------|
| 187 | `the flies relay the junction conversation` | `the flies relay oc-tanner-elder` |

**Note:** ID 339 was previously recast to `the flies relay the clerk` (W2 cycle). ID 187 now follows the same actor-as-object pattern for a different actor. Consistent with the relay-recast policy applied across Group F.

---

### Counts

- Lines edited (recasts): 1 (ID 187)
- Lines deleted: 1 (ID 109)
- Groups confirmed pre-applied (no new edits): A, B, C, D, E, F (15 individual instances confirmed)
- Policy decisions documented: 1 (Group H)
- Total fault instances addressed this cycle: 17 (15 pre-applied + 2 new edits)

---

### Verdict

**ALL-CRITERIA-MET**

- Group A (ID 166 holds→stills): confirmed pre-applied
- Group B (IDs 226, 274, 355, 449 headache-subject): confirmed pre-applied
- Group C (IDs 237, 241 neighbors→neighbor): confirmed pre-applied
- Group D (ID 469 sealed-modifier): confirmed pre-applied
- Group E (IDs 353, 447, 462, 493 duplicates): confirmed pre-applied
- Group F (IDs 339, 387, 388, 416, 417, 471 abstract-relay): confirmed pre-applied
- Group G (ID 109 orphan write): deleted this cycle
- Group H (walks-the-pathnoun ×11): policy documented — leave unchanged — defensible idiomatic usage
- Group I (ID 187 junction-conversation): recast to `the flies relay oc-tanner-elder` this cycle

Additional flag: ID 113 is a second orphan write in the same local stretch as ID 109, not named in the fault. Flagged for screen-writer review. No edit applied (minimum-change discipline).
