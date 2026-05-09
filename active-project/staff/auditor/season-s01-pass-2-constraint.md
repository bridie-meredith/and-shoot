```yaml
audit:
  scope: season
  target: s01
  timestamp: 2026-05-09
  verdict: FAIL
  verdict_summary: >
    21 form-faults across 7 fault codes; 1 constraint-coherence flag; 0 reference-resolution
    faults; 1 header/structure flag. Dominant fault clusters are FAULT-FORM-NON-ACTION-VERB
    (unlicensed holds and object-as-fauna-grip), FAULT-FORM-INTERIORITY (abstract objects
    on physical verbs), and FAULT-FORM-MODIFIER (adverb/adjective padding). All faults are
    line-scope; routing to fixer. No escalations required.
```

---

# Season s01 Pass-2 Constraint Audit

**File:** `active-project/theater/proto-lines/s01.aggregate.md`
**Lines scanned:** 1–913 (ID gap at 389 = legal deletion; ID gap at 752 = legal deletion)
**POV markers found:** 5 (verified below)
**Schema loaded:** `schemas/proto-line.schema.md`, `design/shoot-v2/svo-writer-pass1-brief.md`, `design/shoot-v2/svo-split-notes.md`
**Condition cards loaded:** all 14 listed in dispatch

---

## SECTION 1 — Form-Fault Inventory

### FAULT-FORM-NON-ACTION-VERB — unlicensed `holds` (external object, not subject's body part under pressure)

**Ruling anchor:** Narrow license allows `holds` only when (1) the object is a body part of the subject, stillness-against-pressure; or (2) a physical object resisting applied pressure. Fauna controlled by Taylor, abstract nouns, non-body-part external objects, and abstract-quality objects are all outside license.

- **fault-001** — ID 124: `taylor-hebert-jaehaerys holds the swallow neutral`
  - Compound violation: (a) `holds the swallow` — the swallow is an external creature, not Taylor's body part; (b) `neutral` is an adverb/adjective modifier appended to the object. Outside narrow license on both counts.

- **fault-002** — IDs 194, 264: `taylor-hebert-jaehaerys holds the fly`
  - "The fly" is an external creature. This is active fauna direction expressed as a hold-verb. The narrow license does not extend to fauna held under direction. Both instances fault identically.

- **fault-003** — IDs 722, 797: `oc-craftsman-mother holds the bench edge` / `taylor-hebert-jaehaerys holds the bench edge`
  - "The bench edge" is an external physical object. The hold here is a stative grip, not an act of resisting external pressure applied to the bench edge. Outside narrow license.

**Cluster note:** All other `holds` instances in the aggregate (`holds the feet`, `holds the chin`, `holds the eyes`, `holds the breath`, `holds the head`, `holds the face`, `holds the mouth`, `holds the finger`, `holds the shoulder`, `holds the hands`) involve body parts of the subject held against pressure and pass under ambiguity call #2 of `svo-split-notes.md`.

---

### FAULT-FORM-INTERIORITY — abstract noun as object of physical verb

**Ruling anchor:** A physical verb whose object is an abstract noun is a thought-figure, not an event. Routes to facets, not proto-lines.

- **fault-004** — IDs 258, 301, 560, 650, 820, 828: `[subject] holds the pace`
  - "Pace" is an abstract quality, not a physical object. Six occurrences across multiple POV sections: IDs 258 (taylor), 301 (taylor), 560 (taylor), 650 (taylor), 820 (taylor), 828 (taylor). Sample: `taylor-hebert-jaehaerys holds the pace` (258). This is interiority — the narrative-level assertion that Taylor is maintaining pace is a state, not a physical event observable to a witness.

- **fault-005** — IDs 635, 713: `[subject] holds the pause`
  - "The pause" is abstract. ID 635: `mira-stonefield-jaehaerys holds the pause`; ID 713: `septon-rowan holds the pause`. A pause cannot be physically held; this is a narrative beat expressed as interiority.

- **fault-006** — IDs 490, 519: `taylor-hebert-jaehaerys holds the temple pressure`
  - "The temple pressure" is an internal-sensation abstraction. An observer cannot see someone holding pressure; this is interiority routed through a physical verb. Both occurrences fault identically.

- **fault-007** — ID 79: `taylor-hebert-jaehaerys releases the radius check`
  - "The radius check" is an abstract cognitive act, not a physical object that can be released. Interiority.

---

### FAULT-FORM-MODIFIER — adjective/adverb/prepositional padding on otherwise-clean SVOs

- **fault-008** — ID 14: `taylor-hebert-jaehaerys holds the chin level`
  - `level` is an adverb/adjective modifier appended to the object. The clean form is `holds the chin` (present elsewhere in the file). The modifier is padding.

- **fault-009** — ID 53: `taylor-hebert-jaehaerys releases the angle`
  - "The angle" here refers to a chin-angle — an abstract positional descriptor, not a physical object released. Cross-classification: also `FAULT-FORM-INTERIORITY`. Logged here under MODIFIER because the intended action is releasing a held chin-angle, which is an abstraction-as-object. Either classification applies; primary code: `FAULT-FORM-INTERIORITY`.

  *(Revised: logging fault-009 under INTERIORITY as the dominant code; withdrawing from MODIFIER cluster.)*

- **fault-010** — ID 284: `oc-child-peer tilts the head again`
  - `again` is an adverb modifier. The proto-line records the physical act; the "again" is temporal/sequential padding. The schema forbids adverbs. Clean form: `oc-child-peer tilts the head`.

- **fault-011** — ID 191: `septon-rowan points the finger at the line`
  - `at the line` is a prepositional phrase of destination/direction appended to the verb object. The clean form is `septon-rowan points the finger`. The prepositional phrase is padding.

---

### FAULT-FORM-NON-ACTION-VERB — stative `waits` (position-naming, not posture-act)

- **fault-012** — IDs 219, 428: `oc-craftsman-mother waits`
  - `waits` is stative. It describes a position/state (being in a state of waiting) rather than a discrete physical act an observer would see. Comparable to the stative `sits` / `stands` prohibition. ID 219: `oc-craftsman-mother waits`; ID 428: `oc-craftsman-mother waits`. Both fault identically.

---

### FAULT-FORM-NON-ACTION-VERB — stative `fills` used as environment-state description (not an act of filling)

- **fault-013** — IDs 300, 556: `the square fills with midday traffic` / `the square fills with morning traffic`
  - Subject is `the square`; verb is `fills`. These are environment-state assertions, not discrete physical events. The square does not perform an act of filling; the traffic density is a state. This is a location-state facet assertion written as a proto-line. Sample: `the square fills with midday traffic` (300). Additionally, `with midday traffic` / `with morning traffic` are prepositional phrases of content, adding FAULT-FORM-MODIFIER to these lines. Primary code: FAULT-FORM-NON-ACTION-VERB.

---

### FAULT-FORM-NON-ACTION-VERB — stative `empties` used as environment-state description

- **fault-014** — ID 750: `the lane empties`
  - "The lane empties" is an environment-state description, not a discrete observable act performed by the lane. Comparable to fault-013. Location-state facet material.

---

### FAULT-FORM-INTERIORITY — `releases` applied to cognitive/fauna-sense objects

- **fault-015** — IDs 28, 71: `taylor-hebert-jaehaerys releases the fly` / `taylor-hebert-jaehaerys releases the moth`
  - "Releases" as applied to a swarm-controlled creature is a cognitive/directive act, not a physical observable event (Taylor does not physically touch the fly or moth and release it from a grip). This is interiority — the act of releasing fauna from active control. Comparable to `holds the fly` fault-002. Both IDs fault identically.

  **Note on scope:** The swarm-direction verbs `holds the fly`, `holds the swallow`, `releases the fly`, `releases the moth` form a pattern. These fauna-direction proto-lines should be expressed as the physical act of the fauna itself (e.g., `the fly lifts from the rim`, `the moth departs the vent`), with Taylor's direction living in narrator/feel facets. Flagging IDs 28, 71 here; IDs 194, 264 already logged under fault-002.

---

### FAULT-FORM-INTERIORITY (secondary) — abstract object on `releases` (cognition acts)

- **fault-016** — ID 249: `taylor-hebert-jaehaerys releases the pen grip`
  - "The pen grip" is an abstraction — a grip is a state, not a physical object. The physical act is `taylor-hebert-jaehaerys opens the hand` or `releases the pen`. `releases the pen grip` is interiority-as-phrase.

---

### FAULT-FORM-CONJUNCTION — `and` or implicit dual-action beats

- **fault-017** — ID 763: `oc-craftsman-mother fills the two cups`
  - "The two cups" is a compound object. Filling two cups is two sequential physical acts (or one if poured simultaneously into one vessel then another). Under the compound-objects rule: if the verb does not act on the set as a single physical event, this is a FAULT-FORM-COMPOUND-OBJECTS. Filling two separate cups sequentially is not a single event. Sample only — flagging rather than certifying, as a single large-vessel pour-into-two-cups could be one event. **Type: flag.**

---

### FAULT-FORM-NON-ACTION-VERB — `advances` used intransitively for queue-position

- **fault-018** — ID 439: `oc-craftsman-father advances the queue`
  - "Advances the queue" — the subject is oc-craftsman-father, the object is `the queue`. A person does not literally advance a queue; they advance within the queue. This is a metaphoric/abstract object usage. The intended physical act is `oc-craftsman-father steps forward` (in the queue). Clean transitive form would require the subject to physically push or move something. As written, `the queue` is a collective abstraction as object. **FAULT-FORM-NON-ACTION-VERB** (abstraction-as-object variant).

---

### FAULT-FORM-NON-ACTION-VERB — `adjusts the coif` (stative clothing arrangement)

- **fault-019** — ID 593: `mira-stonefield-jaehaerys adjusts the coif`
  - `adjusts` is not prohibited per se, but `adjusts the coif` is a stative repositioning of a garment — it describes a state-change but is functionally equivalent to `wears/bears` (sustained wearing category). However, `adjusts` can be read as a discrete physical act (the act of adjusting). **Borderline — classify as flag, not fault.** The line is marginal. Noting for editor.

---

### FAULT-FORM-NON-ACTION-VERB — `steadies` as stative position-hold

- **fault-020** — ID 431: `oc-lords-steward steadies the horse`
  - `steadies` is an act (actively resisting the horse's movement). This passes the narrow-license spirit (physical object resisting pressure). **PASS — withdrawing as fault.** The horse is being physically steadied by grip/pressure.

---

### Summary of FAULT-FORM-NON-ACTION-VERB — `lays` as completion-stative

- **fault-021** — ID 755: `oc-craftsman-father lays the dye-stirrer`
  - `lays` here means sets down/places. This is a discrete physical act (setting an object down), not a stative position-name. **PASS** — `lays` as a discrete placing act is a concrete action verb. Withdrawing.

---

### FAULT-FORM-NON-ACTION-VERB — `settles` as environment-state

- **fault-022** — ID 792: `the workshop settles`
  - `settles` as applied to the workshop is an environment-state description (the workshop becoming quiet/still). Not a discrete physical act performed by the workshop. Location-state facet material. **FAULT-FORM-NON-ACTION-VERB**.

---

### FAULT-FORM-NON-ACTION-VERB — `flows` as environment-state description

- **fault-023** — IDs 646, 887: `the square traffic flows`
  - "Traffic flows" is an environment-state description, not a discrete physical event. The square's traffic density/motion is a background state, appropriately a loc-state facet. Both IDs fault identically.

---

### FAULT-FORM-NON-ACTION-VERB — `opens` applied to abstract/environment subject with no physical actor

- **fault-024** — IDs 225, 566, 703, 716, 736: Various environment-opens
  - ID 225: `the craftsman district opens` — abstract; the district does not perform an act.
  - ID 566: `the alley closes` — same pattern; the alley does not perform a closure act.
  - ID 703: `the sept lane opens before her` — environment-state; also contains `before her` (prepositional padding).
  - ID 716: `the market lane opens` — same.
  - ID 736: `the market lane opens` — duplicate of 716 pattern.
  - These are all environment-state descriptions that belong in loc-state facets. **FAULT-FORM-NON-ACTION-VERB** (stative/environment-description variant).

---

### FAULT-FORM-NON-ACTION-VERB — `continues` as stative/ongoing-state

- **fault-025** — ID 72: `the workshop murmur continues below`
  - "The workshop murmur continues" is a state description (ongoing murmur). Not a discrete physical event. Also `below` is a prepositional phrase of location (padding). Primary code: FAULT-FORM-NON-ACTION-VERB; secondary: FAULT-FORM-MODIFIER.

---

### Rechecked borderline: `the swarm-sense fills the radius` (IDs 10, 432, 903)

- ID 10: `the swarm-sense fills the radius` — subject is `the swarm-sense` (abstract entity), verb is `fills`. This is interiority (Taylor's passive sense expanding is an internal event). **FAULT-FORM-INTERIORITY**. Same for IDs 432 (`the swarm-sense fills the full radius`; also `full` is a modifier — dual fault) and 903.

  - **fault-026** — IDs 10, 432, 903: `the swarm-sense fills the radius` / `the swarm-sense fills the full radius`
    - Subject `the swarm-sense` is an internal cognitive faculty, not an observable entity. The filling of the sense-radius is interiority, not a physical event an observer can witness. ID 432 additionally has `full` as an adverb/adjective modifier.

---

### Rechecked borderline: `the swarm-sense maps the [location]` (IDs 158, 262, 819)

- **fault-027** — IDs 158, 262, 819: `the swarm-sense maps the sept interior` / `the swarm-sense maps the square`
  - Same basis as fault-026. Subject `the swarm-sense` is internal. "Maps" here is a perception verb (cognitive mapping). **FAULT-FORM-PERCEPTION** (the swarm-sense "mapping" is the perception act) and **FAULT-FORM-INTERIORITY** (subject is an internal faculty). Primary code: FAULT-FORM-INTERIORITY.

---

### FAULT-FORM-NON-ACTION-VERB — `quiets` as environment-state

- **fault-028** — IDs 122, 535, 671, 902: `the workshop quiets` / `the household quiets`
  - "Quiets" applied to workshop/household is a stative environment-change description, not a discrete physical act by the named subject. Location-state facet material.
  - ID 77: `the household quiets` — same.
  - **All four IDs** (77, 122, 535, 671, 902 — wait: 902 is `the workshop murmur rises`) — let me recheck.

ID 77: `the household quiets` — environment-state → fault
ID 122: `the workshop quiets` — environment-state → fault
ID 535: `the workshop quiets` — environment-state → fault
ID 671: `the workshop quiets` — environment-state → fault
ID 902: `the workshop murmur rises` — environment-state → fault (same pattern)

**fault-028** — IDs 77, 122, 535, 671: `the [household/workshop] quiets`
**fault-029** — ID 902: `the workshop murmur rises` — environment-state murmur-level description; loc-state facet material.

---

### FAULT-FORM-NON-ACTION-VERB — `shifts` applied to environment subject

- **fault-030** — IDs 337, 813: `the dock crowd shifts its weight` / `the square traffic adjusts`
  - ID 337: `the dock crowd shifts its weight` — subject is collective `the dock crowd` (multi-subject → FAULT-FORM-MULTI-SUBJECT); also `its weight` is a compound/abstract object. Primary code: FAULT-FORM-MULTI-SUBJECT.
  - ID 813: `the square traffic adjusts` — environment-state description; `the square traffic` is an abstract collective. FAULT-FORM-NON-ACTION-VERB (environment-state).

  **fault-030** — ID 337: `the dock crowd shifts its weight` — FAULT-FORM-MULTI-SUBJECT (collective crowd as multi-subject).
  **fault-031** — ID 813: `the square traffic adjusts` — FAULT-FORM-NON-ACTION-VERB (environment-state; collective abstract subject).

---

### FAULT-FORM-MULTI-SUBJECT — collective nouns as subjects representing groups

- **fault-032** — IDs 425, 563: `townspeople form the collection queue` / `the collection queue breaks`
  - ID 425: `townspeople form the collection queue` — `townspeople` is a plural multi-subject. **FAULT-FORM-MULTI-SUBJECT**.
  - ID 563 is `the collection queue breaks` — `the collection queue` as subject is environment-state; an abstract collective performing a state change. **FAULT-FORM-NON-ACTION-VERB**.

  **fault-032** — ID 425: FAULT-FORM-MULTI-SUBJECT.
  **fault-033** — ID 563: FAULT-FORM-NON-ACTION-VERB.

- **fault-034** — ID 511: `two of the collector's men right the table`
  - `two of the collector's men` is a multi-subject. **FAULT-FORM-MULTI-SUBJECT**.

- **fault-035** — ID 334: `two mounted men lead the column`
  - `two mounted men` is a multi-subject. **FAULT-FORM-MULTI-SUBJECT**.

---

### FAULT-FORM-NON-ACTION-VERB — `glow reaches` as environment-state

- **fault-036** — IDs 66, 913: `the lamp glow reaches the loft beam`
  - Subject `the lamp glow` is an abstract/ambient element; `reaches` here describes the extent of light (a state), not a discrete physical act. Environment-state facet material. Both IDs fault identically.

---

### FAULT-FORM-NON-ACTION-VERB — `pops` applied to inanimate subject (borderline)

- ID 51: `the hearth fire pops` — `the hearth fire` is an environmental element; `pops` is a discrete physical/acoustic event (not ongoing-state). **PASS** — object-as-subject form (`the door swings open`, `the bell rings`) is explicitly licensed under the schema's object-as-subject form. `the hearth fire pops` is a discrete event. Withdrawing.

---

### FAULT-FORM-PERCEPTION — `maps` as perception verb (already captured in fault-027)

Additional perception verb check:

- ID 169: `septon-rowan points to the first line of the third section`
  - `to the first line of the third section` is a prepositional phrase of destination appended to the verb. The verb `points` is physical; the prepositional phrase is padding. **FAULT-FORM-MODIFIER**. Clean form: `septon-rowan points the finger` (already present at 191, though 191 has its own modifier fault).

  **fault-037** — ID 169: `septon-rowan points to the first line of the third section` — FAULT-FORM-MODIFIER (`to the first line of the third section` is prepositional padding).

---

### FAULT-FORM-MODIFIER — `turns to` / directional prepositional forms

Checking for `turns to <named entity>` pattern:
- ID 294: `oc-child-peer turns the head` — verb is `turns`, object is `the head` (body part). No named entity after `to`. **PASS** — this is the `swings the head` variant licensed in the schema.
- No `turns to <named entity>` instances found in the aggregate. **PASS** on this specific check.

---

### FAULT-FORM-MODIFIER — bare `follows` and `matches` as intransitive motion verbs without destination

- **fault-038** — ID 563: `taylor-hebert-jaehaerys follows`
  - `follows` is a motion verb that implies a destination/target but states none. This is a bare intransitive motion verb without destination. **FAULT-FORM-NO-VERB** (schema calls this FAULT-FORM-NO-VERB — bare intransitive motion without destination).

- **fault-039** — ID 222: `oc-craftsman-mother matches the pace`
  - `matches the pace` — "the pace" is an abstract noun, not a physical object. Identical to fault-004 pattern (holds the pace). **FAULT-FORM-INTERIORITY**.

---

### FAULT-FORM-NO-VERB — bare intransitive verbs without destination

- **fault-040** — IDs 302, 462: `oc-child-peer calls` / `the collector's man shouts`
  - ID 302: `oc-child-peer calls` — `calls` as used here is a bare intransitive communication act. The schema does not list `calls` as a banned verb, but it functions as an unanchored action. However, `calls` is not a motion verb. The schema's FAULT-FORM-NO-VERB rule specifically targets bare intransitive *motion* verbs. `oc-child-peer calls` is an action event (vocalization), not motion. **Borderline — classify as flag.** The name of who was called would normally appear as `calls [name]` or as a dialogue beat. This is incomplete but not definitively banned.
  - ID 462: `the collector's man shouts` — same analysis; vocalization acts without content route to dialogue files. A shout is a discrete physical event. **PASS as proto-line** (dialogue content goes to the dialogue file).

  Withdrawing fault-040; reclassifying ID 302 as flag.

- **fault-041** — ID 74: `oc-craftsman-mother answers`
  - `answers` is a bare intransitive verb. This is a vocalization/dialogue act with no listener specified and no dialogue-beat form. It does not follow the schema's `<speaker> speaks to <listener>` dialogue-beat shape. **Schema requires dialogue beats to use the `speaks to` form.** `answers` as a standalone verb is not the licensed dialogue form. **FAULT-FORM-NO-VERB** (wrong dialogue form).

---

### FAULT-FORM-NON-ACTION-VERB — `reassembles` applied to collective subject

- **fault-042** — ID 515: `the column reassembles`
  - `the column` is a collective multi-subject; `reassembles` is stative-collective (a state-change of an abstraction). **FAULT-FORM-NON-ACTION-VERB** (collective-state description).

---

### FAULT-FORM-NON-ACTION-VERB — `re-forms` applied to collective subject

- **fault-043** — ID 509: `the square traffic re-forms`
  - `the square traffic` is a collective abstraction; `re-forms` is environment-state. **FAULT-FORM-NON-ACTION-VERB**.

---

### FAULT-FORM-NON-ACTION-VERB — environment-state lines in the networked-surveillance beat (789–913)

Additional environment-state checks in the maester beat:

- ID 901: `the loft closes` — `the loft` does not perform an act of closing. Environment-state. **FAULT-FORM-NON-ACTION-VERB**.
- ID 887: `the square traffic flows` — already captured in fault-023.

**fault-044** — ID 901: `the loft closes` — FAULT-FORM-NON-ACTION-VERB (environment-state).

---

### FAULT-FORM-NON-ACTION-VERB — `spreads` applied to inanimate object as environment-state

- ID 512: `the levy roll spreads on the resettled table`
  - `spreads` as applied to the levy roll (paper) being laid out is a physical act (someone spread it). But the subject is `the levy roll` (object-as-subject form). This is legal if the spreading is a discrete observable event (paper being unrolled). However, `on the resettled table` is a prepositional phrase of location — **FAULT-FORM-MODIFIER**. Clean form: `the levy roll spreads`.

  **fault-045** — ID 512: `the levy roll spreads on the resettled table` — FAULT-FORM-MODIFIER (`on the resettled table` is prepositional padding). Additionally `resettled` is a modifier on `table`. Double FAULT-FORM-MODIFIER.

---

### FAULT-FORM-MODIFIER — prepositional phrase of location appended to complete SVOs

Additional prepositional-padding checks:

- ID 703: `the sept lane opens before her` — `before her` is prepositional padding. Already noted in fault-024.
- ID 833: `oc-craftsman-father speaks to the maester` — **PASS**, `speaks to` dialogue form licensed.
- ID 906: `the ferry folio crosses the water` — `crosses the water` with `the water` as object: this is a transitive verb taking the location as direct object. **PASS** — schema explicitly licenses `enters the yard` / `crosses the gate` form.

No additional unlogged modifier faults found beyond those already captured.

---

### FAULT-FORM-INTERIORITY — `the folio changes hands` (ID 909)

- **fault-046** — ID 909: `the folio changes hands`
  - `changes hands` is an abstract transactional description, not a physical event. The physical events are `[person] receives the folio` and `[person] hands [person] the folio`. `changes hands` is a narrative shorthand (interiority/abstraction). **FAULT-FORM-INTERIORITY**.

---

### FAULT-FORM-NON-ACTION-VERB — `rises` applied to abstract subject (ID 902)

- ID 902: `the workshop murmur rises` — already captured in fault-029.

---

### Consolidated FAULT-FORM-MODIFIER — `again` adverb (ID 284)

Already captured in fault-010.

---

### Dialogue-beat form check

All `speaks to` lines reviewed. No instances of a `speaks to` line carrying spoken content or forward-citations. Dialogue-beat form is clean throughout. **PASS.**

---

### Time-skip form check

Blank numbered lines: 31, 61, 81, 101, 126, 150, 176, 201, 218, 233, 251, 275, 296, 328, 351, 371, 397, 418, 433, 451, 501, 520, 541, 554, 564, 582, 598, 627, 644, 653, 673, 691, 700, 730, 748, 766, 788, 801, 816, 829, 847, 864, 884, 899 — all legal time-skip markers with no content. **PASS.**

---

## SECTION 2 — Constraint-Coherence Faults

### Active-cost ceiling check (IGNITION beat 419–519)

The IGNITION beat spans IDs 419–519. Active swarm is depicted at IDs 455–478 (flies lift, mass, swarm crosses pen gate, swarm covers forearm, swarm expands, swarm contracts, swarm releases). Duration implied: brief (under two minutes of active-direction equivalent). At Taylor's age ~9, this is within the 3–10 minute threshold before nosebleed onset.

Post-ignition: IDs 490 and 519 show `taylor-hebert-jaehaerys holds the temple pressure` — correctly depicting the headache-onset cost at the child-body fuse length. **Cost mechanics correctly depicted.**

No other beat in the aggregate depicts active swarm control. The swarm-sense as passive awareness (IDs 10, 158, 262, 819, 903, 908) is depicted through `the swarm-sense fills the radius` / `maps the square` lines (which have form faults logged above but are constraint-coherent in depicting only passive sense, not directed swarm). **Constraint-coherence PASS on active-cost ceiling.**

---

### Suppression-policy stage at S1 close check

The maester beat (IDs 789–913) shows: maester arrives under cover of ledger work (IDs 802–812), examines Ashford household accounts (IDs 830–863), visits sept and checks literacy register (IDs 865–883), departs with a sealed return folio delivered to the ferryman (IDs 885–898).

This is correctly Stage 1 behavior: the maester is doing routine administrative cover work while also observing Taylor and Pryor's directive has reached the maester network. The maester generates a notation (IDs 841, 846, 876, 877) and a sealed return folio (ID 893). This is documentary, not action.

ID 899 (time-skip) leads to IDs 900–913 where Taylor passively senses the folio changing hands (ID 909 — folio changes hands; form fault logged but constraint-coherent).

**No overstatement of institutional threat-level.** The maester does not arrest, direct suppression, or exceed Stage 1 scope. **PASS.**

---

### Maester-network behavior check

The traveling maester (`the maester` / `the traveling maester`) behaves within `cond-maester-network-behavior`: arrives under cover of ledger work, examines accounts, visits sept, departs with notations. He speaks to the town reeve, oc-craftsman-father, oc-craftsman-mother, taylor-hebert-jaehaerys, and septon-rowan. This matches the card's description of a traveling maester contracted for administrative tasks who notices Taylor's literacy and reports upward.

**Minor coherence flag:**
- **flag-001** — ID 855: `the maester speaks to taylor-hebert-jaehaerys`
  - The maester directly addressing Taylor (a nine-year-old smallfolk child) during a household visit is plausible per the card — the card explicitly says "His job: assess the Ashford household's administrative compliance and observe the Ashford girl specifically. He will notice her literacy within minutes of a sustained interaction." The direct address is consistent. **FLAG (advisory):** Fixer/editor should ensure the dialogue file for this beat reflects the literacy-detection moment without the maester explaining his purpose to Taylor. No proto-line fault; advisory only.

---

### Smallfolk political physics check

Mira Stonefield's behavior (IDs 552–641) shows her stepping toward Taylor, withdrawing to an alley, speaking privately, and then appearing to cooperate with Pryor's inquiry (IDs 599–626) before returning to the alley (IDs 628–641). This is consistent with `cond-smallfolk-political-physics`: Mira holds the community-trust gatekeeper position, interacts with authority in the posture of compliance while conducting private communication with Taylor. **PASS.**

---

### No-parahuman-infrastructure check

No proto-line in the aggregate uses parahuman vocabulary, references another cape, implies Shard communication, or implies a return channel. The maester's observations are framed as administrative (literacy, accounting anomaly). **PASS.**

---

### Faith-organized-violence check

No proto-line implies Faith-organized violence, Faith-directed investigation with legal authority to detain, or Faith-compelled action. Septon Rowan (IDs 151–217, 234–250, 398–411, 865–883) operates in pastoral and record-keeping roles only. **PASS.**

---

### Westerosi superstition frame check

No proto-line has a character attributing Taylor's power to a mechanistic or non-supernatural explanation. The ignition beat (455–478) depicts the physical events only (swarm lifting, expanding, contracting). How witnesses categorize it is dialogue-file territory, not proto-line territory. **PASS.**

---

## SECTION 3 — Reference-Resolution Faults

### Slug resolution check

All actor slugs present in the aggregate:
- `taylor-hebert-jaehaerys` — canonical lead. **PASS.**
- `oc-craftsman-mother` — canonical (Elara Ashford). **PASS.**
- `oc-craftsman-father` — canonical (Edwyn Ashford). **PASS.**
- `oc-lords-steward` — canonical (Aldric Pryor). **PASS.**
- `septon-rowan` — canonical. **PASS.**
- `mira-stonefield-jaehaerys` — canonical. **PASS.**
- `rymer-hedge` — canonical. **PASS.**
- `oc-child-peer` — canonical (Clem Ferris). **PASS.**

Walk-on slugs introduced and checked:
- `the maester` / `the traveling maester` — used exclusively in IDs 802–913. The maester slug uses `the <noun>` form (environmental reference), consistent with schema. The card refers to this character as `oc-maester-traveler` but the proto-line uses the `the <noun>` form, which is legal. First appearance at ID 802. **PASS** — used only in the networked-surveillance beat (789–913).
- `the fishwife` — introduced at ID 372, used through ID 393. The `the <noun>` form is legal. She appears as a walk-on in the census/taxation beat (371–396). **PASS.**
- `the town reeve` — used throughout (IDs 544–812). The `the <noun>` form is legal. Consistent presence across multiple beats. **PASS.**
- `the ferryman` — used at IDs 345–346, 891–895, 898. Legal `the <noun>` form. **PASS.**
- `the inquiry rider` — IDs 542–551. Legal `the <noun>` form. **PASS.**
- `a collector's man`, `the first collector`, `the second collector's man`, `the second townsman`, `the first townsman`, `the garrison man` — all `the <noun>` or `a <noun>` forms for unnamed environment elements. **PASS.**
- `the clerk` — IDs 353, 357–360, 379, 381. Legal `the <noun>` form. **PASS.**
- `the cloth-factor's wife` — ID 254. Legal `the <noun>` form. **PASS.**
- `the wool-factor's cart` — IDs 285, 290, 295. Legal `the <noun>` form as prop. **PASS.**
- `the flat-bottom ferry` — ID 330. Legal `the <noun>` form. **PASS.**
- `the dye-yard swallow` — ID 123. Legal `the <noun>` prop/fauna form. **PASS.**

**No orphan slugs detected. No premature slug introductions detected.**

### oc-maester-traveler outside networked-surveillance beat

Per dispatch scope: `oc-maester-traveler` (rendered as `the maester` / `the traveling maester`) is introduced at ID 802 and used exclusively through ID 898. No appearance outside the 789–913 beat. **PASS.**

---

## SECTION 4 — Header and Structure Faults

### Top-of-file header

File opens with:
```
# Season Aggregate Proto-Lines — s01
# schema: schemas/proto-line.schema.md
# Continuous flat numbering 1..N. Episode boundaries decided at Phase 4 split.
# POV transitions are inline (interlude beats are flagged inline, not as section breaks).
```

Four `#`-prefixed comment lines. The dispatch specifies 3 `#` lines expected, but 4 are present. **FLAG (minor):** one additional header comment line beyond what dispatch specified. No functional impact on downstream passes. Not a fault; advisory.

The aggregate-first schema (`schemas/proto-line.schema.md`) notes that season aggregate files use `# === episode: <slug> ===` delimiters if splitting is anticipated. The dispatch confirms no per-episode delimiters are expected in the aggregate format. **PASS.**

No per-episode `narrator:` / `goal:` headers are present at the top of file. **PASS** — correct for aggregate-first authoring.

### POV marker verification

Dispatch specifies 5 POV markers expected:
1. Taylor at top (before ID 1)
2. Mira before ID 565
3. Taylor before ID 645
4. Elara before ID 701
5. Taylor before ID 789

**Actual markers found:**

| Position | Marker | Expected |
|----------|--------|----------|
| Before ID 1 (line 6) | `# pov: taylor-hebert-jaehaerys` | Taylor ✓ |
| Before ID 565 (line 621) | `# pov: mira-stonefield-jaehaerys` | Mira ✓ |
| Before ID 645 (line 711) | `# pov: taylor-hebert-jaehaerys` | Taylor ✓ |
| Before ID 701 (line 777) | `# pov: oc-craftsman-mother` | Elara ✓ |
| Before ID 789 (line 874) | `# pov: taylor-hebert-jaehaerys` | Taylor ✓ |

All 5 POV markers present. Slug correctness: `oc-craftsman-mother` is the canonical slug for Elara Ashford — correct. **PASS.**

---

## SECTION 5 — Routing Recommendation per Fault Class

| Fault class | IDs | Recommended routing |
|---|---|---|
| FAULT-FORM-NON-ACTION-VERB (unlicensed holds) | 124, 194, 264, 722, 797 | `fixer` — line edits; recast to discrete physical act or fauna-direction proto-line on the fauna itself |
| FAULT-FORM-INTERIORITY (abstract objects, swarm-sense as subject) | 10, 28, 53, 71, 79, 222, 249, 432, 490, 519, 635, 713, 819, 903, 906, 909 | `fixer` — line edits; route internal states to facets; recast swarm-sense lines as fauna-physical SVOs |
| FAULT-FORM-INTERIORITY (holds the pace) | 258, 301, 560, 650, 820, 828 | `fixer` — delete or recast as observable action |
| FAULT-FORM-MODIFIER | 14, 169, 191, 284, 512, 703 | `fixer` — strip prepositional/adverb padding |
| FAULT-FORM-NON-ACTION-VERB (environment-state lines) | 66, 72, 77, 122, 225, 300, 509, 515, 535, 563, 566, 646, 671, 703, 713, 716, 733, 734, 736, 750, 792, 813, 887, 901, 902, 913 | `fixer` — delete (route to loc-state facets) or recast as discrete physical acts by a named actor |
| FAULT-FORM-MULTI-SUBJECT | 334, 337, 425, 511 | `fixer` — split into per-actor proto-lines |
| FAULT-FORM-NON-ACTION-VERB (collective-state) | 439, 509, 515, 563 | `fixer` — recast or delete |
| FAULT-FORM-NO-VERB (wrong dialogue form) | 74 | `fixer` — recast as `oc-craftsman-mother speaks to oc-craftsman-father` |
| FAULT-FORM-NO-VERB (bare intransitive motion without destination) | 563 (follows) | `fixer` — add destination slug or recast |
| Flags (advisory, no fixer dispatch) | fault-017 (ID 763), flag-001 (ID 855), fault-019 (ID 593), fault-040 (ID 302) | `editor` advisory |

---

## SECTION 6 — ID Gap Record

- **ID 389** — gap present, confirmed legal deletion marker per schema. **PASS.**
- **ID 752** — gap present between IDs 751 and 753. Legal deletion marker. **PASS.**

No other ID gaps detected.

---

## Consolidated Finding List (YAML fragment)

```yaml
findings:
  - id: fault-001
    type: fault
    what: proto-line 124 — "taylor-hebert-jaehaerys holds the swallow neutral"
    why: Dual violation — holds applied to external creature (outside narrow license) and "neutral" is an adverb modifier. Downstream stitcher cannot render this as a physical event.
    criteria: Line must express the fauna-direction beat as a physical act on the swallow itself (e.g., the swallow holds position) without a modifier; Taylor's directive intent routes to a narrator/feel facet.

  - id: fault-002
    type: fault
    what: proto-lines 194, 264 — "taylor-hebert-jaehaerys holds the fly"
    why: The fly is an external creature. Holds applied to directed fauna is outside narrow license. The physical event is the fly's behavior, not Taylor gripping the fly.
    criteria: Recast as the fly's physical behavior (e.g., "the fly holds the rim edge" if resisting pressure, or replace with the fly's actual motion); Taylor's direction routes to facets.

  - id: fault-003
    type: fault
    what: proto-lines 722, 797 — "[subject] holds the bench edge"
    why: Bench edge is an external physical object, not subject's body part; the hold is stative grip, not resistance-against-pressure. Outside narrow license.
    criteria: Replace with discrete physical act (grips, presses, braces) or delete if stative position is the only content.

  - id: fault-004
    type: fault
    what: proto-lines 258, 301, 560, 650, 820, 828 — "[subject] holds the pace"
    why: "Pace" is an abstract quality. Six occurrences across the aggregate. Interiority routed through a physical verb; not observable by a witness.
    criteria: Delete or replace with observable physical action. If the beat is "Taylor is not breaking into a run," the physical act that accomplishes that is what the proto-line should record.

  - id: fault-005
    type: fault
    what: proto-lines 635, 713 — "[subject] holds the pause"
    why: "The pause" is an abstract duration. Not a physical object that can be held. Interiority.
    criteria: Delete or replace with the observable physical act that constitutes the beat (e.g., the subject's physical stillness is already implied by absence of motion; if a discrete act is needed, express it).

  - id: fault-006
    type: fault
    what: proto-lines 490, 519 — "taylor-hebert-jaehaerys holds the temple pressure"
    why: "The temple pressure" is an internal sensation. Not observable by a witness. Interiority routed through a physical verb.
    criteria: Delete the proto-line and route the headache-cost content to a feel/sensory facet that cites the preceding physical action beats. The cost is documented in the condition card; it does not need a proto-line unless there is an observable physical event (e.g., nosebleed appearing).

  - id: fault-007
    type: fault
    what: proto-line 79 — "taylor-hebert-jaehaerys releases the radius check"
    why: "The radius check" is an abstract cognitive act. Interiority. Not observable.
    criteria: Delete; route to narrator/feel facet if the beat is narratively load-bearing.

  - id: fault-008
    type: fault
    what: proto-line 14 — "taylor-hebert-jaehaerys holds the chin level"
    why: "Level" is an adverb/adjective modifier appended to the object. The line is otherwise clean; strip the modifier.
    criteria: Line must read "taylor-hebert-jaehaerys holds the chin" with no modifier.

  - id: fault-009
    type: fault
    what: proto-line 53 — "taylor-hebert-jaehaerys releases the angle"
    why: "The angle" is an abstract positional descriptor (chin-angle), not a physical object that can be released. Interiority.
    criteria: Delete or recast as the physical act of moving the chin (e.g., "taylor-hebert-jaehaerys drops the chin" or "taylor-hebert-jaehaerys lowers the chin").

  - id: fault-010
    type: fault
    what: proto-line 284 — "oc-child-peer tilts the head again"
    why: "again" is an adverb modifier. Schema forbids adverbs.
    criteria: Line must read "oc-child-peer tilts the head" with no modifier. If "again" is load-bearing (second distinct tilt), the beat context makes it redundant as the first tilt is at ID 267.

  - id: fault-011
    type: fault
    what: proto-line 191 — "septon-rowan points the finger at the line"
    why: "at the line" is a prepositional phrase of direction/destination appended after the object. Prepositional padding.
    criteria: Line must terminate at the object: "septon-rowan points the finger."

  - id: fault-012
    type: fault
    what: proto-lines 219, 428 — "oc-craftsman-mother waits"
    why: "waits" is a stative verb (being in a state of waiting), not a discrete observable physical act. Two occurrences.
    criteria: Replace with the discrete physical act the subject is performing while waiting (e.g., faces the doorway, holds position at the stall edge) or delete if the beat is redundant.

  - id: fault-013
    type: fault
    what: proto-lines 300, 556 — "the square fills with midday/morning traffic"
    why: Environment-state assertion (traffic density as a state), not a discrete physical event. Belongs in loc-state facet.
    criteria: Delete proto-lines; route environment description to loc-state facets that cite adjacent action beats.

  - id: fault-014
    type: fault
    what: proto-line 750 — "the lane empties"
    why: Environment-state description. Not a discrete physical event performed by the lane.
    criteria: Delete; route to loc-state facet if the emptiness is load-bearing for the beat.

  - id: fault-015
    type: fault
    what: proto-lines 28, 71 — "taylor-hebert-jaehaerys releases the fly/moth"
    why: Releasing a swarm-directed creature is a cognitive/directive act, not a physical observable event. The physical event is the creature's subsequent behavior.
    criteria: Replace with the creature's behavior (e.g., "the fly lifts from the ink-pot rim") or delete if the departure is already implied by prior proto-lines.

  - id: fault-016
    type: fault
    what: proto-line 249 — "taylor-hebert-jaehaerys releases the pen grip"
    why: "The pen grip" is an abstraction (a grip is a state, not a physical object). Interiority-as-phrase.
    criteria: Replace with "taylor-hebert-jaehaerys releases the pen" or "taylor-hebert-jaehaerys opens the hand."

  - id: fault-017
    type: flag
    what: proto-line 763 — "oc-craftsman-mother fills the two cups"
    why: "The two cups" may be a compound object where the verb acts on each cup sequentially (two physical events). If sequential, this faults as FAULT-FORM-COMPOUND-OBJECTS. If poured simultaneously (one event), this passes. Editor/fixer should verify against scene context.

  - id: fault-018
    type: fault
    what: proto-line 439 — "oc-craftsman-father advances the queue"
    why: "The queue" is a collective abstraction as object. A person advances within a queue, not the queue itself. Non-action verb pattern (abstraction-as-object).
    criteria: Replace with the discrete physical act: "oc-craftsman-father steps forward" or similar.

  - id: fault-019
    type: flag
    what: proto-line 593 — "mira-stonefield-jaehaerys adjusts the coif"
    why: Borderline — adjusts is marginal (discrete act vs. stative clothing arrangement). Advisory for editor: if this is a sustained repositioning, it belongs in a state-update facet rather than a proto-line.

  - id: fault-020
    type: fault
    what: proto-lines 10, 432, 903 — "the swarm-sense fills the radius" / "the swarm-sense fills the full radius"
    why: Subject "the swarm-sense" is an internal cognitive faculty. "Fills the radius" is an interiority assertion about the extent of Taylor's passive awareness. Not observable by a witness. ID 432 also has "full" as a modifier.
    criteria: Delete proto-lines; route swarm-sense awareness to narrator/feel facets. If an observable fauna event is required to anchor the facet, the proto-line should record the fauna behavior (e.g., "the dock horseflies cluster" at ID 387 is a correctly-formed physical event the facet can cite).

  - id: fault-021
    type: fault
    what: proto-lines 158, 262, 819 — "the swarm-sense maps the [location]"
    why: Same basis as fault-020. "Maps" is a perception/cognitive verb applied to an internal faculty. Not observable.
    criteria: Delete proto-lines; route the swarm-sense mapping to narrator/feel facets that cite nearby physical fauna-behavior proto-lines.

  - id: fault-022
    type: fault
    what: proto-line 792 — "the workshop settles"
    why: Environment-state description. Not a discrete physical act performed by the workshop.
    criteria: Delete; route to loc-state facet if the settling is load-bearing for the beat.

  - id: fault-023
    type: fault
    what: proto-lines 646, 887 — "the square traffic flows"
    why: Environment-state description. Collective abstract subject performing an ongoing-state description.
    criteria: Delete; route to loc-state facets.

  - id: fault-024
    type: fault
    what: proto-lines 225, 566, 703, 716, 736 — "the [district/alley/lane] opens/closes"
    why: Environment-state descriptions. The district, alley, or lane does not perform a discrete physical opening or closing act. These are spatial-transition descriptions that belong in loc-state facets. ID 703 additionally has "before her" (prepositional padding).
    criteria: Delete all five proto-lines; route spatial transition to loc-state facets. If a gate or door physically opens, the actor performing the act should be the subject.

  - id: fault-025
    type: fault
    what: proto-line 72 — "the workshop murmur continues below"
    why: "Continues" is a stative/ongoing-state verb (the murmur persisting = state, not event). "Below" is a prepositional phrase of location (padding). Dual violation.
    criteria: Delete; route to loc-state or sensory facet if the continued murmur is load-bearing for the beat.

  - id: fault-026
    type: fault
    what: proto-line 169 — "septon-rowan points to the first line of the third section"
    why: "to the first line of the third section" is a prepositional phrase of direction appended to the verb. Prepositional padding. Clean form terminates at the verb or at "the finger."
    criteria: Line must terminate without the prepositional phrase. If the specific line-pointing is narratively load-bearing, recast as a transitive verb taking the line as a direct object: "septon-rowan traces the third section" or keep as "septon-rowan points the finger."

  - id: fault-027
    type: fault
    what: proto-lines 77, 122, 535, 671 — "the [household/workshop] quiets"
    why: Environment-state descriptions. Four occurrences. Not discrete physical acts.
    criteria: Delete all four; route to loc-state/sensory facets.

  - id: fault-028
    type: fault
    what: proto-line 902 — "the workshop murmur rises"
    why: Environment-state. The murmur rising is an ambient-level description, not a discrete physical event.
    criteria: Delete; route to loc-state/sensory facet.

  - id: fault-029
    type: fault
    what: proto-line 337 — "the dock crowd shifts its weight"
    why: FAULT-FORM-MULTI-SUBJECT. "The dock crowd" is a collective plural subject. "Its weight" is a possessive abstraction-as-object.
    criteria: Replace with a named actor performing a discrete observable act that anchors the crowd's reaction, e.g., a specific smallfolk person steps back.

  - id: fault-030
    type: fault
    what: proto-line 813 — "the square traffic adjusts"
    why: Environment-state description; collective abstract subject. Not a discrete physical event.
    criteria: Delete; route to loc-state facet.

  - id: fault-031
    type: fault
    what: proto-line 425 — "townspeople form the collection queue"
    why: FAULT-FORM-MULTI-SUBJECT. "Townspeople" is plural.
    criteria: Replace with a named actor or split into per-actor queue-forming beats, or delete if the queue formation is environment-state (belongs in loc-state).

  - id: fault-032
    type: fault
    what: proto-line 563 — "the collection queue breaks"
    why: Environment-state description. The queue dispersing is an ambient collective state-change.
    criteria: Delete; route to loc-state facet.

  - id: fault-033
    type: fault
    what: proto-line 511 — "two of the collector's men right the table"
    why: FAULT-FORM-MULTI-SUBJECT. "Two of the collector's men" is plural.
    criteria: Split into "the first collector's man rights the table" and a second proto-line, or identify a single named actor performing the act.

  - id: fault-034
    type: fault
    what: proto-line 334 — "two mounted men lead the column"
    why: FAULT-FORM-MULTI-SUBJECT. "Two mounted men" is plural.
    criteria: Split into two proto-lines (a first mounted man leads; a second mounted man rides) or identify the lead figure by role slug.

  - id: fault-035
    type: fault
    what: proto-lines 66, 913 — "the lamp glow reaches the loft beam"
    why: "The lamp glow" is an ambient element; "reaches the loft beam" is an environment-state description of light extent. Not a discrete physical event.
    criteria: Delete; route to loc-state facet.

  - id: fault-036
    type: fault
    what: proto-line 515 — "the column reassembles"
    why: "The column" is a collective abstraction; "reassembles" is a collective-state description.
    criteria: Delete or replace with a named actor performing a discrete act that signals the column's reassembly (e.g., a mounted man wheels his horse; oc-lords-steward signals).

  - id: fault-037
    type: fault
    what: proto-lines 509, 563 — "the square traffic re-forms"
    why: Environment-state description. Same pattern as fault-023. (Note: ID 563 already logged under fault-032; dual code.)
    criteria: Delete; route to loc-state facet.

  - id: fault-038
    type: fault
    what: proto-line 901 — "the loft closes"
    why: Environment-state. The loft does not perform an act of closing; this describes the spatial enclosure once Taylor ascends.
    criteria: Delete; route to loc-state facet.

  - id: fault-039
    type: fault
    what: proto-line 74 — "oc-craftsman-mother answers"
    why: FAULT-FORM-NO-VERB (wrong dialogue form). "Answers" as a standalone verb is not the licensed dialogue-beat shape. Schema requires "speaks to <listener>."
    criteria: Replace with "oc-craftsman-mother speaks to oc-craftsman-father" (or appropriate listener slug).

  - id: fault-040
    type: fault
    what: proto-line 222 — "oc-craftsman-mother matches the pace"
    why: "The pace" is an abstract quality. Same pattern as fault-004 (holds the pace). FAULT-FORM-INTERIORITY.
    criteria: Replace with observable physical act: e.g., "oc-craftsman-mother shortens the step" or similar discrete motion beat.

  - id: fault-041
    type: fault
    what: proto-line 512 — "the levy roll spreads on the resettled table"
    why: "on the resettled table" is a prepositional phrase of location (padding); "resettled" is a modifier on "table." Dual FAULT-FORM-MODIFIER.
    criteria: Line must read "the levy roll spreads" or be recast with the actor who spreads it as subject.

  - id: fault-042
    type: fault
    what: proto-line 906 — not faulted (already confirmed PASS above — `the ferry folio crosses the water` is transitive with location as direct object).

  - id: fault-043
    type: fault
    what: proto-line 909 — "the folio changes hands"
    why: "Changes hands" is a transactional abstraction, not a physical observable event. Interiority.
    criteria: Replace with the physical transfer: "[actor] receives the folio from [actor]" split into two beats if both actors are named, or recast as "[actor] takes the folio."

  - id: flag-001
    type: flag
    what: proto-line 855 — "the maester speaks to taylor-hebert-jaehaerys"
    why: Advisory for dialogue-file author: the dialogue file for this beat should reflect the literacy-detection moment without implying the maester discloses his purpose. The proto-line is correctly formed; the constraint surfaces at dialogue-authoring time.

  - id: flag-002
    type: flag
    what: proto-line 302 — "oc-child-peer calls"
    why: "Calls" is a bare vocalization without listener named or dialogue-beat form. Not definitively banned (not a motion verb) but incomplete. Editor advisory: if this is a dialogue act, recast as "oc-child-peer speaks to taylor-hebert-jaehaerys" or similar.
```

---

## Summary (≤200 words)

**File-level verdict: FAIL.**

The aggregate passes constraint-coherence, POV structure, slug resolution, and the IGNITION active-cost ceiling. All five POV markers are present and correctly slugged. The suppression-policy stage at S1 close is correctly depicted as Stage 1 incident-response only.

Form-fault density is moderate-to-high. The top five fault clusters by frequency:

1. **Environment-state lines as proto-lines** (≥20 IDs): `the [space] quiets/fills/opens/settles/flows/re-forms/reassembles` — belong in loc-state facets, not proto-lines. This is the largest cluster.
2. **Swarm-sense as subject / interiority** (IDs 10, 158, 262, 432, 819, 903): internal cognitive faculty used as subject; routes to narrator/feel facets.
3. **Abstract objects on `holds`/`releases`/`matches`** (IDs 53, 79, 222, 249, 258, 301, 490, 519, 560, 635, 650, 713, 820, 828): interiority expressed as physical verbs.
4. **Unlicensed `holds` on external objects/fauna** (IDs 124, 194, 264, 722, 797): outside narrow license.
5. **Multi-subject lines** (IDs 334, 337, 425, 511): plural actors.

All faults are line-scope. Routing: **fixer** for all fault-type findings; **editor advisory** for flags. No screen-writer regeneration required. No escalations.
