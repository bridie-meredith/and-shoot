# Phase 2 constraint sweep — s01

audit:
  scope: season
  target: s01
  timestamp: 2026-05-11
  auditor-fork: 2-A (constraint sweep, cycle 2)

---

## Cycle 2

### Counts

- Lines audited: 464 (excludes time-skip markers and preserved gaps at IDs 157, 158, 189, 191, 193, 203, 204, 282, 283)
- New bones audited: 9 (IDs 495–503)
- Surgical edits audited: 3 (IDs 86, 310, 412)
- FAULT-FORM-PERCEPTION: 0
- FAULT-FORM-MODIFIER: 13 (residual/new — see findings)
- FAULT-FORM-INTERIORITY: 0 confirmed faults; 2 border flags (IDs 310, 412)
- FAULT-FORM-NON-ACTION-VERB: 2 (IDs 256, 469 — cycle-1 misses)
- FAULT-FORM-COPULA: 0
- FAULT-FORM-NEGATION: 0
- FAULT-FORM-CONJUNCTION: 0
- FAULT-FORM-MULTI-SUBJECT: 0
- FAULT-FORM-NO-VERB: 0
- FAULT-FORM-COMPOUND-OBJECTS: 0
- FAULT-TURNS-TO: 0
- FAULT-REFERENCE-DRIFT: 0
- FAULT-SLUG-UNRESOLVED: 0
- FAULT-LAW-*: 0
- FAULT-COND-*: 0

### File-level verdict

FAIL — 15 findings (13 FAULT-FORM-MODIFIER, 2 FAULT-FORM-NON-ACTION-VERB). The major structural faults from cycle 1 (PERCEPTION, REFERENCE-DRIFT, INTERIORITY, SLUG-UNRESOLVED) are fully resolved. Remaining faults are line-scope modifier and non-action-verb issues: mix of cycle-1 misses that survived fixer pass, and one new fault introduced in the regen (ID 502). Two border flags on nominalized event nouns at IDs 310 and 412 require fixer decision.

---

### Cycle-1 re-check results

| Re-check item | Result |
|---|---|
| Zero `marks` left (was 17) | PASS — 0 instances confirmed |
| Zero `reads aloud` (was 2) | PASS — 0 instances confirmed |
| Zero `maps` (was 3) | PASS — 0 instances; gaps at IDs 189/191/193 preserved |
| All prepositional padding cleaned (was 45) | PARTIAL — cycle-1-listed 45 instances resolved; 13 additional modifier faults found (cycle-1 misses or regen-introduced) |
| `the maester` only at IDs ≤301 | PASS — IDs 111, 128, 129, 285, 286, 280 (possessive in location phrase) all ≤301 |
| `oc-broken-maester` at IDs ≥303 | PASS — IDs 303–415 all use `oc-broken-maester` |
| ID 164 reads `the arrival` | PASS — `the arrival enters the junction` confirmed |
| ID 237 no longer `fill the doorways` | PASS — `the neighbors press the doorways` confirmed |
| New bones 495–503 pass deny-list | PARTIAL — IDs 495–501, 503 pass; ID 502 has MODIFIER fault |
| Surgical edits IDs 86, 310, 412 clean | PARTIAL — ID 86 clean; IDs 310 and 412 have border-flag on nominalized event noun |
| Relay-verb pattern (~35 lines) | NOTED — closed policy decision, not a fault (see policy note below) |

---

### Findings

#### FAULT-FORM-NON-ACTION-VERB

- **fault-C2-001**
  - id: fault-C2-001
  - type: fault
  - what: ID 256 — `oc-tanner-father receives the coins` — `receives` is a possession/state-acquisition verb, not a physical observable act.
  - why: Same class as cycle-1 faults 020–021 (lines 203/204 `receive` deleted). The physical act is the father's hand closing on the coins or Taylor's release of them; `receive` encodes the outcome state, not the act.
  - criteria: Recast to a physical act. Options: `oc-tanner-father takes the coins`, `oc-tanner-father closes the hand`, or render the transfer entirely on Taylor's side (`taylor-hebert-flea-bottom releases the coins`) and let the father's side be a facet state-update.
  - route: fixer

- **fault-C2-002**
  - id: fault-C2-002
  - type: fault
  - what: ID 469 — `the middleman receives the sealed account` — same class as fault-C2-001.
  - why: The physical act is oc-tanner-elder extending the account and the middleman taking it; `receive` encodes the transfer outcome, not the discrete physical motion.
  - criteria: Recast to physical act. Options: `the middleman takes the sealed account`, `the middleman lifts the sealed account`, or render as `oc-tanner-elder extends the sealed account` + `the middleman exits the writing room`.
  - route: fixer

---

#### FAULT-FORM-MODIFIER — cycle-1 misses (unresolved in fixer pass)

- **fault-C2-003**
  - id: fault-C2-003
  - type: fault
  - what: ID 139 — `the flies relay oc-dock-runner's position` — `oc-dock-runner's` is a possessive modifier on the object noun. Same pattern as cycle-1 fault on `the beetles relay the maester's footfall` (ID 307, resolved).
  - why: Schema licenses `the <noun>` objects; possessive-modified objects encode relational information that belongs in a facet.
  - criteria: Recast: `the flies relay the position` if context is established, or `the flies relay oc-dock-runner`. Drop possessive.
  - route: fixer

- **fault-C2-004**
  - id: fault-C2-004
  - type: fault
  - what: ID 143 — `the flies relay oc-dock-runner's exit path` — `oc-dock-runner's` possessive modifier + `exit path` compound noun encoding a nominalized movement event.
  - why: Double modifier fault: possessive modifier on relay-object + event-noun object. `exit path` encodes a trajectory abstraction, not a physical entity.
  - criteria: Recast: `the flies relay oc-dock-runner` (if the relay of departure is what's needed) or delete if the exit at ID 141 (`oc-dock-runner exits the Fish Gate margin`) already covers the beat.
  - route: fixer

- **fault-C2-005**
  - id: fault-C2-005
  - type: fault
  - what: ID 217 — `the spiders relay the apothecary south window` — `apothecary` adjective modifier + `south` adjective modifier on `window`. Two compounding adjectives.
  - why: Same class as cycle-1 fault on `the flies relay the apothecary doorframe` (ID 107, resolved to `the flies relay the doorframe`). Two adjective modifiers remain here.
  - criteria: Recast: `the spiders relay the window`. Location context is carried by surrounding beats.
  - route: fixer

- **fault-C2-006**
  - id: fault-C2-006
  - type: fault
  - what: ID 280 — `the visitor arrives at the maester's side-alley door` — prepositional phrase (`at`) + possessive modifier (`maester's`) + compound adjective (`side-alley`) on `door`.
  - why: Three layered modifier violations in one line: prepositional padding, possessive, and compound adjective. This is the densest modifier fault in the file. The physical act and destination can be rendered more cleanly.
  - criteria: Recast: `the visitor enters the side alley` or `the visitor approaches the stairwell door` (drop `maester's` possessive, drop `at` preposition). If building-attribution is load-bearing, it belongs in the loc-state or a facet note, not in the proto-line SVO.
  - route: fixer

- **fault-C2-007**
  - id: fault-C2-007
  - type: fault
  - what: ID 287 — `the beetles relay the upper-room register` — `upper-room` adjective modifier on `register`. Same pattern as cycle-1 fault on `the beetles relay the upper-room sound` (ID 112, resolved to `the beetles relay the sound`).
  - why: Adjective modifier on relay-object. `upper-room` location qualifier belongs in facet context, not the proto-line object.
  - criteria: Recast: `the beetles relay the register`.
  - route: fixer

- **fault-C2-008**
  - id: fault-C2-008
  - type: fault
  - what: ID 338 — `the flies relay the clerk's departure path` — `clerk's` possessive modifier + `departure path` nominalized event noun.
  - why: Possessive on relay-object (same class as cycle-1 IDs 307/403/412, resolved). `departure path` is additionally a nominalized event trajectory (abstract).
  - criteria: Recast: `the flies relay the clerk` (the clerk's movement is the relay-event, not the abstracted path). Or delete if the clerk's exit at ID 337 is sufficient.
  - route: fixer

- **fault-C2-009**
  - id: fault-C2-009
  - type: fault
  - what: ID 371 — `the flies relay the apothecary doorframe exchange` — `apothecary` adjective modifier on `doorframe exchange`. Compound object `doorframe exchange` also encodes an event (the exchange that happened at the doorframe).
  - why: Same adjective-modifier class as cycle-1 ID 107 (`the flies relay the apothecary doorframe`, resolved). `exchange` additionally encodes the event, making the object doubly abstract.
  - criteria: Recast: `the flies relay the doorframe` or `the flies relay the exchange`. Drop `apothecary` adjective; pick the concrete noun.
  - route: fixer

- **fault-C2-010**
  - id: fault-C2-010
  - type: fault
  - what: ID 372 — `the flies relay the second clerk's departure path` — `second clerk's` possessive modifier + `departure path` event noun. Same double-fault class as fault-C2-008.
  - why: Possessive + event-noun compound. The underlying beat (second clerk left) is already encoded at ID 370 (`the second clerk exits the apothecary`).
  - criteria: Recast: `the flies relay the second clerk` or delete (exit beat at ID 370 is sufficient; the relay adds no physical SVO).
  - route: fixer

- **fault-C2-011**
  - id: fault-C2-011
  - type: fault
  - what: ID 461 — `the flies relay the messenger's arrival path` — `messenger's` possessive modifier + `arrival path` event noun.
  - why: Same class as fault-C2-008 and fault-C2-010. The messenger's arrival is already encoded at ID 455 (`the messenger enters the market-side junction`).
  - criteria: Recast: `the flies relay the messenger` or delete (arrival beat at ID 455 covers the physical event).
  - route: fixer

- **fault-C2-012**
  - id: fault-C2-012
  - type: fault
  - what: ID 462 — `the flies relay the messenger's departure path` — `messenger's` possessive modifier + `departure path` event noun.
  - why: Same class. The messenger's exit is already encoded at ID 460 (`the messenger exits the junction`).
  - criteria: Recast: `the flies relay the messenger` or delete.
  - route: fixer

---

#### FAULT-FORM-MODIFIER — new regen bone

- **fault-C2-013**
  - id: fault-C2-013
  - type: fault
  - what: ID 502 (new regen bone) — `the wasps relay the labor-web pass` — `labor-web` compound adjective modifier on `pass`.
  - why: Same class as cycle-1 `the beetles relay the pen-scratch rhythm` (resolved at IDs 296/298 by dropping `pen-scratch`). `labor-web` is an adjective qualifying `pass`; the relay-object should be a bare noun.
  - criteria: Recast: `the wasps relay the pass`. If `labor-web` context is load-bearing for the beat, encode it in the surrounding bones or a facet note, not as an adjective on the relay-object.
  - route: fixer

---

#### FAULT-FORM-MODIFIER — non-standard transitive verb (cycle-1 miss)

- **fault-C2-014**
  - id: fault-C2-014
  - type: fault
  - what: ID 490 — `taylor-hebert-flea-bottom returns loc-flea-bottom-base` — non-standard transitive use of `returns` with a location slug as direct object; the `to` preposition has been elided.
  - why: Same construction as cycle-1 fault on old ID 308 (`the maester returns the stairwell`, resolved to `oc-broken-maester enters the stairwell`). `returns` is intransitive or requires `to` + location; `returns loc-flea-bottom-base` is a syntactic artifact that cannot be reliably parsed by downstream facet authoring.
  - criteria: Recast: `taylor-hebert-flea-bottom enters loc-flea-bottom-base`.
  - route: fixer

---

#### FAULT-FORM-MODIFIER — ID 488 (duplicate of fault-C2-005 pattern)

- **fault-C2-015**
  - id: fault-C2-015
  - type: fault
  - what: ID 488 — `the spiders relay the apothecary south window` — identical construction to fault-C2-005 (ID 217). `apothecary` + `south` adjective modifiers on `window`.
  - why: Two instances of the same fault exist in the file (IDs 217 and 488). Both must be resolved.
  - criteria: Recast: `the spiders relay the window`.
  - route: fixer

---

#### FLAGS — nominalized event-noun objects (border, INTERIORITY class)

- **flag-C2-001**
  - id: flag-C2-001
  - type: flag
  - what: ID 310 — `the beetles relay the ascent` — `ascent` is a nominalized movement event (the act of ascending). The MODIFIER fault from cycle-1 (old: `the return footfall`, `return` as adjective) was resolved by the surgical edit, but the resulting object `ascent` is in the same abstract-event-noun class as cycle-1 fault-012 (`the south-wall return`).
  - why: If `ascent` is read as an abstract event noun (the act of going up), the proto-line encodes an internal perception of the maester's movement, not a physical SVO. Facet authors would double-encode the ascending event (once here, once in a sensory facet citing `oc-broken-maester ascends the stair` at ID 414 — same movement encoded twice).
  - note: Less severe than the old `return footfall` fault since `ascent` is more concrete than `return`, and the beat genuinely differs from the visual SVO of the maester ascending (the beetle relay is the acoustic/tactile signal, not the visual). Fixer should determine whether `the beetles relay the ascent` adequately encodes the physical relay-beat or whether a more concrete noun is available (e.g., `the beetles relay the stair-vibration` — though that introduces a new compound).
  - route: fixer (decision call, not mandatory recast)

- **flag-C2-002**
  - id: flag-C2-002
  - type: flag
  - what: ID 412 — `the beetles relay the return` — `return` as a standalone noun object is the nominalized event of oc-broken-maester returning from the errand. Same class as cycle-1 fault-012 (`the south-wall return`). The MODIFIER fault (old: `the maester's return footfall`, `return` as adjective + possessive) was resolved, but the resulting bare `return` is itself an abstract event noun.
  - why: `return` encodes the event of coming back, not a physical thing. The maester's physical re-entry is covered at IDs 413–415 (`enters the apothecary`, `ascends the stair`, `enters the upper room`). If those physical beats exist, `the beetles relay the return` is redundant event-noun coverage.
  - note: May be intentional (the relay beat signals to Taylor that the errand is complete before she can see it). If so, a more concrete noun is preferable: `the beetles relay the footfall` or `the beetles relay the stair-approach`.
  - route: fixer (decision call, not mandatory recast)

---

### Policy note — relay verb pattern

Per task brief: approximately 35 `<insect> relay <X>` lines are a closed policy decision by screen-writer. These are not faulted as FAULT-FORM-PERCEPTION. The relay-verb pattern is noted here for the record. The 15 findings above are distinct from the relay-policy decision; they concern the objects of relay lines (modifier faults on those objects) or non-relay lines entirely.

---

### Constraint audit — cycle-2 additions

No new condition card violations detected in the 9 new bones or the surgical edits. The constraint-card passes from cycle-1 carry forward unchanged.

- ID 501 (`oc-tanner-elder speaks to the carter`) — no parahuman infrastructure, no smallfolk-physics violation at proto-line level. PASS.
- ID 502 (`the wasps relay the labor-web pass`) — fauna within 300m-range scope. PASS on constraint. FAULT on modifier (fault-C2-013 above).
- All other new IDs: PASS on all condition cards.

---

### Summary table — cycle 2

| Class | Count | Verdict |
|---|---|---|
| FAULT-FORM-PERCEPTION | 0 | PASS |
| FAULT-FORM-MODIFIER | 13 | FAIL |
| FAULT-FORM-INTERIORITY | 0 confirmed | PASS (2 border flags) |
| FAULT-FORM-NON-ACTION-VERB | 2 | FAIL |
| FAULT-FORM-COPULA | 0 | PASS |
| FAULT-FORM-NEGATION | 0 | PASS |
| FAULT-FORM-CONJUNCTION | 0 | PASS |
| FAULT-FORM-MULTI-SUBJECT | 0 | PASS |
| FAULT-FORM-NO-VERB | 0 | PASS |
| FAULT-FORM-COMPOUND-OBJECTS | 0 | PASS |
| FAULT-TURNS-TO | 0 | PASS |
| FAULT-REFERENCE-DRIFT | 0 | PASS |
| FAULT-SLUG-UNRESOLVED | 0 | PASS |
| FAULT-LAW-* | 0 | PASS |
| FAULT-COND-* | 0 | PASS |
| Flags (border/event-noun) | 2 | FLAG |

---

## Cycle 1 [archived]

audit:
  scope: season
  target: s01
  timestamp: 2026-05-11
  auditor-fork: 2-A (constraint sweep)

---

### Counts

- Lines audited: 455 (excludes 39 time-skip markers)
- FAULT-FORM-PERCEPTION: 19
- FAULT-FORM-MODIFIER: 45
- FAULT-FORM-INTERIORITY: 11
- FAULT-FORM-NON-ACTION-VERB: 3
- FAULT-FORM-COPULA: 0
- FAULT-FORM-NEGATION: 0
- FAULT-FORM-CONJUNCTION: 0
- FAULT-FORM-MULTI-SUBJECT: 0
- FAULT-FORM-NO-VERB: 0
- FAULT-FORM-COMPOUND-OBJECTS: 0
- FAULT-TURNS-TO: 0
- FAULT-REFERENCE-DRIFT: 1 (systematic — affects ~30+ lines)
- FAULT-SLUG-UNRESOLVED: 1
- FAULT-LAW-*: 0
- FAULT-COND-*: 0

### File-level verdict

FAIL — 79 individual-line faults across six classes; one systematic slug fault (the-maester vs oc-broken-maester) affecting all scenes involving the cast-roster character; no constraint-card violations at proto-line level.

---

### Findings (by class)

#### FAULT-FORM-PERCEPTION

`marks` appears 17 times as a perception verb assigned to human subjects observing Taylor's behavior or to Taylor recording grid data. `reads aloud` appears twice on the maester. All are observation verbs that record internal perception, not external acts.

- **fault-001** — Line 14: `oc-tanner-father marks the stillness` — `marks` is perception. Father observes and notes; the physical act is his eye-movement or posture-freeze, not a marking. Suggested recast: `oc-tanner-father stills` or let Taylor's hold-of-the-chin (line 13) be the only SVO; the father's noticing is a sensory/narrator facet. route: fixer
- **fault-002** — Line 17: `oc-tanner-father marks the pivot angle` — same class. Recast: `oc-tanner-father tilts the head` (the observable act of tracking). route: fixer
- **fault-003** — Line 66: `the reeve marks taylor-hebert-flea-bottom` — `marks` is observation. Recast: `the reeve turns the head` or `the reeve slows the step`. route: fixer
- **fault-004** — Line 109: `taylor-hebert-flea-bottom marks the grid notation` — Taylor recording a grid position is a writing act, not a `marks`-as-perception act; but `marks` here blurs with the next note-taking group. If distinct from the log-write beats, recast: `taylor-hebert-flea-bottom inscribes the grid notation`. route: fixer
- **fault-005** — Line 111: `the maester reads aloud in the upper room` — `reads` is explicitly on the perception deny-list. Also carries two FAULT-FORM-MODIFIER violations (`aloud` + `in the upper room` — see MODIFIER section). Recast: `the maester opens the page` + separate beat for vocalization, or render the vocalization as `the maester speaks to the room` (aloud delivery = speaking act). route: fixer

... + 14 more instances:
- Line 113: `marks the grid notation` — same as fault-004 pattern.
- Line 123: `marks the grid notation`
- Line 129: `the maester reads aloud` — same as fault-005 pattern, stripped of location padding.
- Line 166: `oc-tanner-father marks the half-second` — `the half-second` is a duration abstraction; marks = perception. Double fault (also INTERIORITY — see below).
- Line 170: `oc-tanner-father marks the scan pattern`
- Line 171: `oc-tanner-mother marks the scan pattern`
- Line 223: `marks the grid notation`
- Line 224: `marks the grid notation`
- Line 271: `marks the grid notation`
- Line 272: `marks the grid notation`
- Line 352: `marks the grid notation`
- Line 353: `marks the grid notation`
- Line 446: `marks the grid notation`
- Line 447: `marks the grid notation`

**Pattern note:** The `marks the grid notation` form recurs identically at lines 109, 113, 123, 223, 224, 271, 272, 352, 353, 446, 447 — eleven identical bones. This is a structural repetition question as well: if these are genuinely distinct beats (Taylor notating grid data at eleven separate moments across the season), each should be distinguishable. If they are the same beat reused, they are redundant. Flag for fixer and Pass 4 (trim). route: fixer

---

#### FAULT-FORM-MODIFIER

Prepositional padding, adverb intrusions, and adjective modifiers on objects. 45 confirmed instances. Representative 5 + count note:

- **fault-006** — Line 1: `taylor-hebert-flea-bottom wakes in the tanner-family bed` — `in the tanner-family bed` is prepositional padding. Recast: `taylor-hebert-flea-bottom wakes` (intransitive); bed position is loc-state territory. route: fixer
- **fault-007** — Line 8: `taylor-hebert-flea-bottom extends the arm toward the salt` — `toward the salt` is prepositional padding. Recast: `taylor-hebert-flea-bottom extends the arm` (intransitive) or `reaches the salt` (transitive, location as direct object). route: fixer
- **fault-008** — Line 49: `oc-tanner-father routes oc-tanner-mother toward the pit` — `toward the pit` is prepositional padding. Pattern repeats lines 50, 56, 57. Recast: `oc-tanner-father routes oc-tanner-mother` if the destination is already established, or split into `oc-tanner-father routes oc-tanner-mother` + `oc-tanner-mother enters the pit`. route: fixer
- **fault-009** — Line 52: `oc-tanner-father crosses the yard toward the pit` — `toward the pit` padding on otherwise-clean `crosses the yard`. Recast: `oc-tanner-father crosses the yard` (drop the destination). route: fixer
- **fault-010** — Line 91: `oc-tanner-elder walks the road toward King's Landing` — `toward King's Landing` padding. Recast: `oc-tanner-elder walks the road`. route: fixer

... + 40 more instances:
- Line 42: `holds the eyes forward` — `forward` adverb. Recast: `holds the eyes` (the body-part hold is licensed; the adverb is not).
- Line 56: `routes oc-tanner-mother toward the central work`
- Line 57: `routes the neighbor-boy toward the central work`
- Line 65: `crosses the far side of the yard` — `far` adjective + `of the yard` prepositional phrase on object. Recast: `crosses the yard` (specific position is loc-state).
- Line 105: `walks the 300m perimeter` — `300m` is a measurement modifier. Recast: `walks the perimeter`.
- Line 107: `the flies relay the apothecary doorframe` — `apothecary` adjective modifier. Recast: `the flies relay the doorframe`.
- Line 108: `the spiders spread the apothecary ceiling corners` — `apothecary ceiling` adjective phrase. Recast: `the spiders spread the ceiling corners`.
- Line 111: `the maester reads aloud in the upper room` — `aloud` (adverb) + `in the upper room` (prepositional phrase). (Also FAULT-FORM-PERCEPTION.)
- Line 112: `the beetles relay the upper-room sound` — `upper-room` adjective modifier. Recast: `the beetles relay the sound`.
- Line 122: `the spiders relay the apothecary upper room` — `upper` adjective modifier. Recast: `the spiders relay the room`.
- Line 128: `the maester crosses the upper room` — `upper` adjective modifier. Recast: `the maester crosses the room`.
- Line 129: `the maester reads aloud` — `aloud` adverb. (Also FAULT-FORM-PERCEPTION.)
- Line 157: `oc-tanner-father enters King's Landing via the south gate` — `via the south gate` prepositional padding.
- Line 158: `oc-tanner-mother enters King's Landing via the south gate` — same.
- Line 222: `taylor-hebert-flea-bottom walks the new perimeter` — `new` adjective. Recurs at lines 270, 351, 445.
- Line 232: `the lords-man enters the alley two blocks south` — `two blocks south` positional qualifier.
- Line 235: `the lords-man's man moves the family possessions into the alley` — `into the alley` prepositional padding.
- Line 240: `the flies relay the room-adjacent wall` — `room-adjacent` adjective modifier.
- Line 255: `taylor-hebert-flea-bottom extends the coins toward oc-tanner-father` — `toward oc-tanner-father` prepositional padding. Recast: `taylor-hebert-flea-bottom extends the coins` or `taylor-hebert-flea-bottom offers oc-tanner-father the coins`.
- Line 296: `the beetles relay the pen-scratch rhythm` — `pen-scratch` adjective. Recurs at line 298.
- Line 297: `the beetles relay the spoken phrase` — `spoken` adjective.
- Line 304: `the maester descends the interior stair` — `interior` adjective. Recurs at line 400.
- Line 307: `the beetles relay the maester's footfall` — possessive modifier `maester's`. Recurs at lines 403, 412.
- Line 308: `the maester returns the stairwell` — non-standard transitive use of `returns` with location object; the implied `to` has been elided leaving a syntactic artifact. Recast: `the maester enters the stairwell` or `the maester re-enters the stairwell`.
- Line 310: `the beetles relay the return footfall` — `return` adjective modifier.
- Line 315: `oc-tanner-mother arrives at loc-flea-bottom-base` — `at loc-flea-bottom-base` prepositional padding. Recast: `oc-tanner-mother enters loc-flea-bottom-base`.
- Line 405: `the maester approaches the dried-goods stall` — `dried-goods` adjective modifier.
- Line 410: `the maester faces the dried-beetle jars` — `dried-beetle` adjective modifier.
- Line 412: `the beetles relay the maester's return footfall` — `return` + possessive modifiers.
- Lines 416–419: `the beetles relay the pen-scratch onset / continuation` — `pen-scratch` adjective modifier (×4).
- Line 442: `the flies spread the Fish Gate comprehensive pass` — `comprehensive` adjective modifier.
- Line 443: `the wasps spread the Fish Gate margin south approach` — `south` adjective modifier.

route (all): fixer

---

#### FAULT-FORM-INTERIORITY

Cognitive verbs (planning, mapping, calculating) and abstract-noun objects that encode thought or plan rather than physical action.

- **fault-011** — Line 86: `oc-tanner-elder routes the labor-web placement` — `the labor-web placement` is an abstract plan-noun, not a physical object. `routes` here means "decides the arrangement of." Recast: `oc-tanner-elder directs the family` (each direction a separate beat with named subject). route: fixer
- **fault-012** — Line 130: `the beetles relay the south-wall return` — `the south-wall return` is an abstract event (the act of returning), not a physical object relayed. The beetle-relay of a sound or position is borderline perception; the object being relayed is a categorized summary of movement, not a sensory signal. Recast: `the beetles relay the south-wall footfall` (concrete noun) if the beat must remain; or render the maester's return as its own physical SVO. route: fixer
- **fault-013** — Line 140: `oc-dock-runner recalculates the route` — `recalculates` is a cognitive verb. The physical act is unobservable. Recast: `oc-dock-runner pauses` (the observable beat of route-reconsideration) + `oc-dock-runner turns the head` (the route-scan). route: fixer
- **fault-014** — Line 145: `oc-tanner-elder routes the inquiry` — `the inquiry` is abstract. Recast: `oc-tanner-elder speaks to oc-dock-runner` (the physical act that initiates the inquiry routing). route: fixer
- **fault-015** — Line 166: `oc-tanner-father marks the half-second` — `the half-second` is a duration abstraction. Also FAULT-FORM-PERCEPTION (marks). Double-faulted. The observable physical act: `oc-tanner-father slows` or `oc-tanner-father holds the step`. route: fixer
- **fault-016** — Lines 174, 381: `oc-tanner-elder routes the trade` / `routes the Fish Gate task` — both objects are abstract. Recast: `oc-tanner-elder speaks to [counterparty]` or split into the specific physical acts of trade-routing. route: fixer
- **fault-017** — Lines 189, 191, 193: `taylor-hebert-flea-bottom maps the junction relay node` / `maps the Fish Gate relay node` / `maps the north relay node` — `maps` is a cognitive/recording verb. The physical act that produces a mental map is either a walk (already rendered) or a writing act (already rendered via log entries). These three lines encode internal cognition that belongs in narrator or sensory facets. Recast: delete these bones and route the mapping act to the narrator facet citing the surrounding walk and log-write bones. route: fixer (delete) or route: screen-writer if the mapping beats are load-bearing scene structure.
- **fault-018** — Line 386: `taylor-hebert-flea-bottom routes the information hand-off` — `the information hand-off` is abstract. The physical act: `taylor-hebert-flea-bottom speaks to the dock-side cluster` (if speech) or `taylor-hebert-flea-bottom extends the hand` (if physical pass). route: fixer
- **fault-019** — Line 390: `the flies thin the dock-side relay` — `the dock-side relay` is an abstract communications relay, not a physical thing the flies thin. If the physical beat is flies dispersing, recast: `the flies withdraw the dock-side cluster` or `the flies retract`. route: fixer

---

#### FAULT-FORM-NON-ACTION-VERB

- **fault-020** — Line 203: `the carters receive the weather-pattern data` — `receive` is a possession/state-acquisition verb. The physical observable act: `taylor-hebert-flea-bottom extends the weather note` to the carters, or render the carters' side as `the carters take the note`. route: fixer
- **fault-021** — Line 204: `the dock workers receive the Watch-movement timing` — same class. route: fixer
- **fault-022** — Line 237: `the neighbors fill the doorways` — `fill` encodes occupancy/containment (the neighbors are present in the doorways) more than a discrete action. Recast: `the neighbors crowd the doorways` (action of gathering) or `the neighbors appear in the doorways` is still stative. Best recast: `the neighbors press the doorways` or `the neighbors lean the doorframes`. route: fixer

---

#### FAULT-REFERENCE-DRIFT

- **fault-023** — `the maester` used as subject/object throughout the file in place of the cast-roster slug `oc-broken-maester`. Per schema, subjects must be actor slugs when a cast-roster actor is intended. Using `the <noun>` form is licensed only for unnamed environment elements. The broken maester is a named cast member with the slug `oc-broken-maester`. This fault affects every scene involving the character: lines 111, 128, 129 (confirmed from reading), and continuing through the apothecary-watch stretch (lines 303–310) and the dried-goods errand (lines 400–419). Estimated scope: 30+ line occurrences.

  why: downstream facet authoring (dialogue files, sensory files, state-update files) must cite the character by slug. If the proto-line uses `the maester`, the facet author has no unambiguous slug to cite — they must infer the slug, which contaminates the facet-authoring contract. The slug mismatch is systematic and will propagate to every facet and state file that references these lines.

  criteria: all occurrences of `the maester` as subject or named listener in a `speaks to` form must be replaced with `oc-broken-maester`.

  route: fixer

---

#### FAULT-SLUG-UNRESOLVED

- **fault-024** — Line 164: `a new arrival enters the junction` — `a new arrival` uses the indefinite article form. Schema licenses `the <noun>` for unnamed entities; the indefinite `a <noun>` form is not in scope. If the arrival is a character who will receive a slug (e.g., the clerk who appears later), this line should use `the arrival` or be held until the character is named. If this is genuinely a one-time unnamed individual, recast: `the arrival enters the junction`.

  why: facet authors and the slug-grep that populates episode-header `cast:` cannot reliably extract an indefinite-article noun as an actor reference.

  criteria: recast to `the <noun>` form or replace with the character's slug if the identity is resolved.

  route: fixer

---

#### PATTERN FLAG — `relay` verb (systemic)

- **flag-001** — The `relay` verb appears in approximately 35 lines (flies relay, beetles relay, wasps relay, spiders relay). `relay` is not on the explicit perception deny-list and is not a banned verb. However, svo-split-notes ambiguity call #1 explicitly flags this pattern: "render as `the mouse repositions in the seam` — physical SVO with `the <noun>` subject — and let the perception live in narrator/feel facet citations." By that call, all fauna-relay lines should be recast as the physical SVO of what the creature physically does (spreads, approaches, withdraws) rather than the sensory transmission act. In the current file, `spread` beats (e.g., line 26: `the flies spread the yard perimeter`) are already correctly cast as physical acts. The `relay` beats encode the sensory-transmission event, which belongs in sensory/narrator facets.

  This is a systematic authoring pattern that the rough-pass tolerated but which faults against the schema's spirit and svo-split-notes call #1. Whether to reclassify all `relay` lines as FAULT-FORM-PERCEPTION is a fixer/screen-writer call. Flagged here for that decision.

  why: if relay lines are left as proto-lines, the facet author will double-encode the perception event (once in the proto-line, once in the sensory facet citing it). The proto-line becomes redundant and the sensory facet has nothing unique to contribute.

  route: screen-writer (the relay-line pattern is structural to how the insects-as-sensor system is represented; recasting requires a policy decision, not just line-level fixing)

---

### CONSTRAINT AUDIT — all active condition cards

All nine active condition cards were checked against every non-blank proto-line.

**cond-no-parahuman-infrastructure:** No PRT, Dragon, Tattletale, or other parahuman infrastructure references. No second parahumans appear. PASS.

**cond-fauna-control-rules-125ac-addendum:** Fauna activity in the bones is consistent with 300m story-open range. No Khepri-mantle-class human coordination appears in s01 bones (no proto-line shows Taylor directing human bodies). Species in use (flies, beetles, wasps, spiders) are within scope. Range expansion beats are present (multiple `spread` + perimeter-walk cycles). PASS.

**cond-shard-behavioral-weight:** Proto-line level only records physical acts. Taylor's internal decision-making is not auditable at SVO level. No fence violations detectable. PASS.

**cond-reincarnation-mechanics-125ac:** No line implies Taylor recalls Tya's memories, accepts a Westerosi name, or pursues a return channel. PASS.

**cond-smallfolk-political-physics:** Organizing beats (lines 203–204: carters/dock-workers receiving data) are present. No scene treats smallfolk as having formal legal recourse or acting without internalized cost. PASS at proto-line level; facet-level register must be audited separately.

**cond-feudal-hierarchy-law:** Authority encounters (reeve, lords-man, clerk, second clerk) are structurally correct — they arrive, interact with intermediaries (oc-tanner-father, oc-tanner-elder), record, and leave. No line implies Taylor has legal recourse. PASS.

**cond-westerosi-customary-authority-125ac:** KL-configuration social physics consistent. No Gold Cloak encounter visible in bones (Watch patrol crosses Fish Gate margin at line 136 but does not interact with Taylor directly). PASS.

**cond-clinical-self-erasure:** At proto-line level, the research log entries are represented as generic write-the-entry beats. Actual log content (whether subjects are named, whether Taylor records physiological data) is facet-level content and not auditable from SVO bones. No fence violation detectable at this level. NOTE: Pass 5 continuity auditor should audit the log-entry facet content against this card when facets are authored.

**cond-crownlands-superstition-frame-125ac / cond-series-tone-constraints-125ac / cond-westerosi-superstition-frame:** These cards govern prose register and community vocabulary — facet and dialogue territory. No proto-line-level violations detectable. PASS.

---

### Summary table — cycle 1

| Class | Count | Verdict |
|---|---|---|
| FAULT-FORM-PERCEPTION | 19 | FAIL |
| FAULT-FORM-MODIFIER | 45 | FAIL |
| FAULT-FORM-INTERIORITY | 11 | FAIL |
| FAULT-FORM-NON-ACTION-VERB | 3 | FAIL |
| FAULT-FORM-COPULA | 0 | PASS |
| FAULT-FORM-NEGATION | 0 | PASS |
| FAULT-FORM-CONJUNCTION | 0 | PASS |
| FAULT-FORM-MULTI-SUBJECT | 0 | PASS |
| FAULT-FORM-NO-VERB | 0 | PASS |
| FAULT-FORM-COMPOUND-OBJECTS | 0 | PASS |
| FAULT-TURNS-TO | 0 | PASS |
| FAULT-REFERENCE-DRIFT | 1 (30+ lines) | FAIL |
| FAULT-SLUG-UNRESOLVED | 1 | FAIL |
| FAULT-LAW-* | 0 | PASS |
| FAULT-COND-* | 0 | PASS |
| Pattern flag — relay verb | ~35 lines | FLAG |
