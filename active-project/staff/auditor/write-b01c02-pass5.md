# /and-write phase 5 continuity audit — b01c02
scope: 27 bones across 3 scenes (post-Phase-4 trim; s01n01 deleted; slug-gap expected)
date: 2026-05-21

## verdict
CONTINUITY-OK (0 faults, 2 flags)

## findings

### FAULT-REACHABILITY
No faults found.

Chapter goal coverage:
- Prohibition tested against genuine threat: s01n05 (hinge-pivot, first deployment). Covered.
- Technically held / verdict construction: s03n02–s03n05 (opens ledger → writes line → strikes line → underlines entry). Covered.
- Accounting cannot close cleanly: s03n07 (closes ledger, chatter, cl-unpriced-cost-bearer surface) + s03n08 (sets the pen, pressure-arrives beat, cl-unpriced-cost-bearer). Covered.

Handoff-out reachability per thread:
- "two street witnesses have seen insect-density anomaly": s01n08 (near witness faces alley-mouth) + s02n05 (near witness crosses lane; heart-rate above settled, vocabulary-gap). Reachable.
- "Wren now specifically attached to Taylor's block presence": s02n03 (Wren faces Taylor; magnitude-2 social-tether) + s02n07 (Wren speaks to Taylor) + s02n08 (Taylor speaks to Wren). Reachable.
- "Coll saw the alley geometry": s02n01 (Coll lifts the eyes, face-to-Taylor glance, non-naming enacted). Reachable. Note: handoff-out says "Coll saw the alley geometry" but the bones express this only as Coll's single eye-find at Taylor's face, not an explicit geometry-read. The chapter chunk prose ("his reading of the alley's changed angles, the lane's traffic-weighting") provides the interpretive context. The bone is consistent; the handoff-out language is a prose-summary of what the bones ground.
- "prohibition flexed but Taylor's accounting holds it as compliant": s03n04 (strikes line — 'compliant, defensible, cost-acknowledged' verdict) + s03n06 (holds the hand — dual-discipline). Reachable.
- "city watch sweep pattern now mapped": s01n07 (city-watch passes the Hook; count, route, press-levy timing confirmed). Reachable.

Handoff-out world_state reachability:
- "insect capability now at first-deployment level; covered approximately two-block radius": s01n05 (insects close lane-mouths; capability 3→4). Reachable.
- "Coll maintains non-interpretive witness role; did not name what he saw": s02n01 (lifts eyes, non-naming enacted) + s02n02 (pulls net, returns to work, no speech). Reachable.

Handoff-out character_state reachability:
- taylor: capability 4 — s01n05. moral-framework 3 (strained) — s03n06 axes_held. social-tether 2.5 — cumulative s01+s02+s03 social-tether moves summing to +0.5. knowledge 4 — cumulative knowledge moves. All values reachable from bone-set.
- wren: rescued, present, unnamed as significant — s01n06 (enters alley), s02n03+s02n07+s02n08 (attached, speaks, receives reply), no bone enters Wren into ledger as significant node.
- otto: offstage — no bone references otto-hightower or any off-stage antagonist. Confirmed.

### FAULT-STATE
No faults found.

Time / location consistency:
- s01: daytime sweep (boots-on-stone approach, watch column visible). s02: immediate aftermath same day (sweep clears, street returns to itself). s03: night interior (s03n01 lights the lamp — explicit nighttime anchor). No within-scene time-skips needed; scene transitions are sequential same-day. Per schema, scene boundaries are carried by the scene-map facet; no blank-numbered lines required inside any scene's bone-set. Confirmed.

Prop / location usage: No props are referenced in b01c02 that require prior placement or inventory state. The ledger (s03n02, s03n04, s03n05, s03n07) and lamp (s03n01) are interior domestic objects; the chapter chunk establishes "Taylor's rent corner interior" as the s03 set. No state-file dependency violation.

Actor location: All three chapter actors (taylor-hebert-kl-122ac, coll-net-mender-flea-bottom, wren-stitch-maker-flea-bottom-ward) are present at the Hook corner / alley / Taylor's interior — consistent with handoff_in world_state ("Taylor holds a rent corner off the Hook"; Coll provides social cover by proximity). No location inconsistency.

### FAULT-REFERENCE
No faults found.

Cast slug resolution:
- taylor-hebert-kl-122ac: in cast_roster. Licit.
- coll-net-mender-flea-bottom: in cast_roster. Licit.
- wren-stitch-maker-flea-bottom-ward: in cast_roster. Licit.
- the water-carrier: `the <noun>` ambient slot. s01n03 — street social-compression readable from watch pressure-front; Taylor is at the scene. Observable. Licit.
- the city-watch: `the <noun>` ambient slot. s01n07 — sweep passes; watch at close range. Observable. Licit.
- the near witness: `the <noun>` ambient slot. s01n08 + s02n05 — stands at lane-mouth (visible from Coll's corner per scene chunk), crosses lane. Observable. Licit.
- the insects: Taylor's deployed instrument. Observable by Taylor as the agent. Licit (see POV note below).

Off-stage cast confirmed absent from bones: otto-hightower, aemond-targaryen-122ac, sera-hightower-kl-122ac, gylda-saltwater-flea-bottom, corvan-archmaester-retrospective-coda. None appear. Confirmed.

### FAULT-POV
No faults found.

POV is taylor-hebert-kl-122ac. All non-Taylor bones verified observable from Taylor's position:

- Coll bones (s02n01, s02n02): Coll is physically co-present at the corner. Observable.
- Wren bones (s01n06, s02n03, s02n07): Wren is at the alley-mouth and then visible from the corner. Observable.
- The water-carrier (s01n03): Street-level body-reorientation readable from the same corner. Observable.
- The city-watch (s01n07): Passes the Hook at close range. Observable.
- The near witness (s01n08, s02n05): Stands at lane-mouth visible from Coll's corner (per scene chunk); crosses lane in aftermath. Observable.
- The insects (s01n02, s01n05): Taylor's own deployed instrument. Object-as-subject form (`the insects fill the lane`, `the insects close the lane-mouths`) is used here where the actor is Taylor. Schema § field rules permit object-as-subject when the actor is unknown/ambient; optional `by <slug>` tail when the actor matters. Ruling: the actor here is not unknown or ambient — it is Taylor. However, the insect-bones function as Taylor's proprioceptive extension: Taylor perceives insect-movement the way a person perceives their own limb. The object-as-subject form is idiomatic for this capability type across both chapters (b01c01s02n04: `the insects fill the block` — same form, same actor, already established and not flagged). The schema flag criterion is ambiguous: "optional" tail is schema language. Classifying this as FLAG (not fault) — see flag-002.

No bone implies an off-stage POV. No perception-verb leak on the POV character detected.

Note on s03 interiority: The scene chunk header carries `# NOTE: interior scene — all bones are physical framing acts; no interiority; interiority to facets`. All s03 bones are physical acts (lights, opens, writes, strikes, underlines, holds, closes, sets). No interiority verb appears in any bone SVO. Confirmed consistent with the note.

### FAULT-HANDOFF-IN-MISMATCH
No faults found.

Handoff_in threads honored:

1. "Taylor's operating rule intact but not yet tested against an external ask" — b01c02 is the first test against a threat (not an external ask; the handoff language says "external ask," which is the Otto-arrangement that comes later). The bones show capability dormant at chapter open: s01n02 (`the insects fill the lane`) is still a sense-read, not yet deployment; s01n04 (`taylor lifts the eyes`) is visual confirmation layered onto the insect-read. Deployment occurs at s01n05. Prohibition intact at chapter open: confirmed.

2. "Wren introduced as recurring street presence; relationship not yet named" — s01n06 (`wren enters the alley`) presents Wren as finding the open exit; the bone notes describe her as "Wren-as-known-variable in deployment" — she is already present in Taylor's insect-range as a named heat-and-motion signature (s01n04 notes: "wren's heat-and-motion signature legible at thirty yards"). This is consistent with her being a recurring street presence from b01c01 (not a fresh introduction). No bone treats Wren as a new face. Confirmed.

3. "insect-sense passive; Flea Bottom ward-geography mapped to block level" — chapter opens with insects in passive read mode at s01n02 (heat-signatures legible at column-formation density, reading sweep-geometry). s01n11 (threshold-crossing bone — body-turn toward alley-mouth commits capability from passive to active) is the deliberate orientation that makes s01n05 a deployed consequence. Passive baseline honored at chapter open; deployment at s01n05. Confirmed.

4. "Coll provides social cover by proximity; no explicit arrangement" — s01n10 (`coll works the net`; non-response, eyes do not find alley) + s02n01 (`coll lifts the eyes`; single glance, Flea Bottom courtesy) + s02n02 (`coll pulls the net`; returns to work without speaking). No bone establishes an arrangement or dialogue between Coll and Taylor in this chapter. Confirmed.

### FLAG ITEMS

- id: flag-001
  type: flag
  what: bone b01c02s01n08 notes + handoff_out open_threads entry "two street witnesses have seen insect-density anomaly"
  why: The bones file uses `the near witness` (singular) throughout (s01n08, s02n05); the chapter chunk plural "two witnesses" is confirmed in s01n08 notes ("witnesses register the anomaly") and s02n05 notes ("witnesses move on"). The SVO subject is singular (`the near witness`), but the plural is embedded in notes. No structural fault — the SVO is the schema-facing surface and `the near witness` as a class-representative ambient subject is licit. Editor / stitch layer should ensure the prose renders plurality without requiring a second named ambient slot. No fixer dispatch required.

- id: flag-002
  type: flag
  what: bones b01c02s01n02 (`the insects fill the lane`) and b01c02s01n05 (`the insects close the lane-mouths`) — object-as-subject form where the actor is taylor-hebert-kl-122ac
  why: Schema permits object-as-subject when actor is unknown/ambient, with optional `by <slug>` tail when actor matters. Here the actor is Taylor and the form is used without the tail. This is an established cross-chapter convention (b01c01s02n04 uses same form; was not flagged at b01c01 audit). Inconsistency between "optional" schema language and the precedent established at b01c01 means this is a pipeline-convention question, not a single-chapter fault. No corrective action warranted at b01c02 scope — document for schema clarification upstream if desired.

## handoff-in honored
Yes.

All four handoff_in open_threads honored (see FAULT-HANDOFF-IN-MISMATCH section above for per-thread notes). No mismatch found. The phrase "not yet tested against an external ask" in thread 1 uses "external ask" to mean an Otto-arrangement offer (which arrives later), while b01c02 provides a threat-driven first-test. This is consistent: the handoff records "external ask not yet occurred," and b01c02's test is self-initiated (protective act), not ask-driven.

## handoff-out reachability
All open_threads, world_state entries, and character_state values are reachable from the surviving 27-bone set. See FAULT-REACHABILITY section for per-entry coverage notes.

## POV consistency
Consistent throughout. All non-Taylor subjects are observable from Taylor's position at the Hook corner / alley-mouth / interior scene. Object-as-subject form on insect bones is an established convention; flagged at flag-002 for schema clarification only. No perception-verb leak detected. s03 bones are physical-act-only per the scene chunk's explicit note; confirmed.
