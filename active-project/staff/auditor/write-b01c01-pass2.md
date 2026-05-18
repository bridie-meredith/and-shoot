audit:
  scope: /and-write Phase 2 constraint audit
  target: b01c01
  timestamp: 2026-05-18
  chapter: b01c01
  bones_audited: 23
  verdict: FAULTS-4

# Classified Report — /and-write Phase 2 — b01c01

---

## Per-bone classification table

| bone       | SVO form                                                                               | axis / delta    | classification        | rationale |
|------------|----------------------------------------------------------------------------------------|-----------------|-----------------------|-----------|
| b01c01s01n01 | taylor-hebert-kl-122ac enters the corner-room                                        | knowledge +0.03 | CORRECT               | Valid transitive motion; `the corner-room` permitted unnamed-noun form; axis and sub-rank magnitude accepted per tuning notes; cost_ledger_anchor `~` correct. |
| b01c01s01n02 | taylor-hebert-kl-122ac pays the-door-keeper                                          | knowledge +0.03 | CORRECT               | `pays` is concrete-physical transitive; `the-door-keeper` resolves as unnamed building fixture under `the <noun>` form; no cast slug exists for this entity; consistent with chapter chunk's anonymous-building framing; cost_ledger_anchor `~` correct. |
| b01c01s01n03 | coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac                         | knowledge +0.05 | CORRECT               | Valid speech bone; both speaker and listener in cast roster; `knowledge` is a communication-class axis satisfying the speech-bone substance requirement; cost_ledger_anchor `~` correct. |
| b01c01s01n04 | taylor-hebert-kl-122ac takes the needle coll-net-mender-flea-bottom extends          | knowledge +0.02 | FAULT-FORM-CONJUNCTION | The trailing phrase `coll-net-mender-flea-bottom extends` is a relative clause that embeds a second action (coll extending the needle) within a single bone. Two discrete events — coll's extension and taylor's taking — are compressed into one line. Schema requires: if two things happen, they are two bones. |
| b01c01s01n05 | taylor-hebert-kl-122ac threads the needle                                            | knowledge null 0 | CORRECT              | Concrete-physical transitive; null delta at sub-rank magnitude is accepted per tuning notes for this establishment chapter; cost_ledger_anchor `~` correct. |
| b01c01s01n06 | the insects move                                                                      | knowledge +0.03 | FAULT-FORM-NO-VERB    | `move` is a motion verb; the bone supplies no destination. Schema rule is categorical: bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB. The landing-clean exception (`taylor exhales`) does not extend to motion verbs implying destination. `the insects move` does not satisfy the narrow intransitive exception because motion implies a terminus that is absent. |
| b01c01s01n07 | taylor-hebert-kl-122ac handles the nets                                              | knowledge +0.02 | CORRECT               | `handles` in craft context (net-mending) denotes active hand-manipulation — a discrete physical act, not sustained carrying or stative possession. Not on explicit deny-list; closer to `works` than `carries` in semantic class. |
| b01c01s01n08 | coll-net-mender-flea-bottom faces the street                                         | knowledge +0.02 | CORRECT               | `faces <X>` is explicitly licensed as a valid transitive recast (cited in schema's `turns to` ban section). `the street` is a valid unnamed-noun object. |
| b01c01s02n01 | taylor-hebert-kl-122ac threads the needle                                            | knowledge null 0 | CORRECT              | Same form as s01n05; CORRECT for same reasons. |
| b01c01s02n02 | the insects move                                                                      | knowledge +0.04 | FAULT-FORM-NO-VERB    | Same form as s01n06. `move` without destination; bare intransitive motion verb; categorical ban applies. |
| b01c01s02n03 | the walls cool                                                                        | knowledge +0.03 | CORRECT               | `cool` is an intransitive verb describing thermal state-change, not a motion verb implying destination. Analogous to `taylor exhales` — complete without a terminus. No modifier, no negation, no abstraction as object. |
| b01c01s02n04 | taylor-hebert-kl-122ac handles the nets                                              | knowledge +0.03 | CORRECT               | Same form as s01n07; CORRECT for same reasons. |
| b01c01s02n05 | the city-watch passes the hook                                                        | knowledge +0.04 | CORRECT               | `passes <object>` is transitive with `the hook` as direct object/destination landmark; `the city-watch` and `the hook` are valid unnamed-noun forms; concrete-physical motion with destination supplied. |
| b01c01s02n06 | taylor-hebert-kl-122ac holds the feet                                                | knowledge null 0 | CORRECT               | Narrow `holds` license satisfied: (1) `the feet` is a body part of the subject taylor-hebert-kl-122ac, and (2) the action is stillness-against-pressure (seated working posture, feet held still during needlework). License conditions met. |
| b01c01s02n07 | the needle moves                                                                      | knowledge +0.03 | FAULT-FORM-NO-VERB    | `move` is a motion verb; no destination supplied. Same categorical ban as s01n06/s02n02. The needle progressing through net-mesh is an observable event but `moves` without destination fails the schema rule; a transitive form with the net as object would satisfy (`the needle crosses the mesh`, `the needle pierces the net`). |
| b01c01s02n08 | taylor-hebert-kl-122ac drops the nets                                                | knowledge +0.03 | CORRECT               | `drops` is a concrete-physical transitive verb; `the nets` is a valid unnamed-noun form object; no modifier, no abstraction. |
| b01c01s03n01 | wren-stitch-maker-flea-bottom-ward enters the street                                 | knowledge +0.02 | CORRECT               | Valid transitive motion with destination; wren in cast roster; cost_ledger_anchor `~` correct. |
| b01c01s03n02 | wren-stitch-maker-flea-bottom-ward approaches taylor-hebert-kl-122ac                 | knowledge +0.02 | CORRECT               | `approaches <person>` is transitive — taylor-hebert-kl-122ac is the destination terminus. Not bare intransitive. Both in cast. |
| b01c01s03n03 | wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac                  | knowledge +0.02 | CORRECT               | Valid speech bone; both in cast; `knowledge` satisfies communication-class axis requirement. |
| b01c01s03n04 | taylor-hebert-kl-122ac faces wren-stitch-maker-flea-bottom-ward                     | knowledge null 0 | CORRECT               | `faces <X>` explicitly licensed as valid transitive recast per schema. |
| b01c01s03n05 | taylor-hebert-kl-122ac holds the eyes                                                | knowledge null 0 | CORRECT               | Narrow `holds` license satisfied: (1) `the eyes` is a body part of the subject taylor-hebert-kl-122ac, and (2) stillness-against-pressure (holding the gaze fixed under social pressure of Wren's attention, resisting the impulse to break or reassess). License conditions met. |
| b01c01s03n06 | taylor-hebert-kl-122ac speaks to wren-stitch-maker-flea-bottom-ward                 | knowledge +0.02 | CORRECT               | Valid speech bone; both in cast; `knowledge` satisfies communication-class axis requirement. |
| b01c01s03n07 | wren-stitch-maker-flea-bottom-ward leaves the street                                 | knowledge +0.02 | CORRECT               | `leaves <object>` is transitive — `the street` is the origin object; not bare intransitive motion. |

---

## Scene aggregate verification

| scene   | bone-sum knowledge | target | match |
|---------|--------------------|--------|-------|
| b01c01s01 | 0.03+0.03+0.05+0.02+0+0.03+0.02+0.02 = 0.20 | 0.20 | CORRECT |
| b01c01s02 | 0+0.04+0.03+0.03+0.04+0+0.03+0.03 = 0.20   | 0.20 | CORRECT |
| b01c01s03 | 0.02+0.02+0.02+0+0+0.02+0.02 = 0.10         | 0.10 | CORRECT |

Note: The three FAULT-FORM-NO-VERB bones (s01n06, s02n02, s02n07) currently carry knowledge deltas of +0.03, +0.04, +0.03 respectively. If fixer rewrites these bones, the knowledge delta values on those bones must be preserved so scene aggregates continue to match their targets.

---

## Constraint audit (active conditions)

No constraint violations found. Checked:

- **cond-khepri-residue-122ac**: No bone names Khepri or Earth-Bet parahuman terminology. Insect-sense is represented as physical observation only (the insects move, the walls cool, the city-watch passes the hook). PASS.
- **cond-earth-bet-noun-fence**: No parahuman jargon in any bone. Bones are pre-dialogue; constraint applies at dialogue-authoring time but no leakage in bone text. PASS.
- **cond-westerosi-magic-dormant-122ac**: No bone moves capability above null/0 this chapter. All capability deltas null at 0. Insect-sense stays passive. PASS.
- **cond-kl-witch-label-formation-122ac**: No bone positions Taylor as visibly anomalous to on-scene witnesses in a way that would form a witch-label. The `the insects move` bones are scene-internal; no witness reaction bone present. PASS.
- **cond-dragon-proximity-122ac**: No dragons on-stage. PASS.
- **cond-kl-social-physics-122ac**: Vouching-through-proximity satisfied by s01n02 (pays the door-keeper), s01n03 (coll speaks), s01n08 (coll faces the street). The chapter chunk notes (SIGNAL-003) that at least one s01 bone must make vouching-knowledge acquisition explicit — s01n03 (coll speaks, knowledge +0.05) addresses this. PASS.
- **cond-taylor-pov-behavior**: No interiority in bones; no bone reports Taylor's thoughts or feelings as SVO events. All interiority is correctly deferred to facets. PASS.
- **cond-westerosi-witness-vocabulary**: No anachronistic vocabulary in bone text. PASS.
- **cond-road-to-hell-chain-shape**: Establishment chapter; no antagonist pressure present; hinge shape correctly absent of escalation. PASS.
- **cond-cost-bearer-scene-frequency**: Wren appears in s03 (enters, approaches, speaks, leaves) — one scene of three, well within frequency bounds for an establishment chapter. PASS.

---

## Cost ledger audit

All 23 bones declare `cost_ledger_anchor: ~`. Per dispatch context, no cost ledger entries resolve at or below b01c01. All anchors correctly null. No FAULT-COST-LEDGER-UNRESOLVED findings.

---

## Physical / state audit

- taylor-hebert-kl-122ac: present in all three scenes as subject or listener. State consistent with handoff_in (position 1, Flea Bottom anonymous). PASS.
- coll-net-mender-flea-bottom: present in s01 as speaker and observer. State consistent with chapter chunk (block fixture, street-facing corner). PASS.
- wren-stitch-maker-flea-bottom-ward: enters at s03. State consistent with handoff_in ("Wren not yet named as significant; present at chapter edge"). PASS.
- No props in active-project/warehouse requiring inventory check. Unnamed entities (the corner-room, the nets, the needle, the insects, the walls, the street, the hook, the city-watch, the eyes, the feet) are all permitted under schema's `the <noun>` form. PASS.

---

## Bone-delta malformation audit

- All axes declared are `knowledge` or `capability` (null). Both are in series.substance.state_axes[].slug. PASS.
- All magnitudes are sub-rank (0.02–0.05) or zero. Per dispatch tuning notes, sub-1 magnitudes are accepted for this establishment chapter. No FAULT-BONE-DELTA-MALFORMED raised on magnitude grounds.
- All capability deltas are null/0, correctly reflecting cond-westerosi-magic-dormant-122ac and the chapter's dormant baseline. PASS.

---

## Findings

findings:
  - id: fault-001
    type: fault
    what: b01c01s01n04 — "taylor-hebert-kl-122ac takes the needle coll-net-mender-flea-bottom extends"
    why: The relative clause `coll-net-mender-flea-bottom extends` embeds a second discrete action (coll extending the needle) inside a bone whose subject is taylor. Two agents perform two actions; compressing them into one line violates the one-bone-one-action rule and produces a compound subject-action structure that downstream facet authoring cannot cleanly cite. The dialogue facet and narrator-interest facet would have ambiguous anchor targets.
    criteria: The bone must be split into two clean SVO bones — one recording coll's extension of the needle, one recording taylor's taking of it — such that each bone has a single subject performing a single discrete action. The two bones together must carry the same aggregate knowledge delta (+0.02) as the current single bone, distributed between them so the scene sum remains 0.20.

  - id: fault-002
    type: fault
    what: b01c01s01n06 — "the insects move"
    why: `move` is a motion verb and the bone supplies no destination. The schema ban on bare intransitive motion without destination is categorical; the landing-clean exception (`taylor exhales`) does not extend to motion verbs. A downstream stitcher rendering `the insects move` has no directional or spatial anchor to render; the facet chain (sensory, location-state) cannot attach specific environmental data to a terminally vague motion event.
    criteria: The bone must supply a destination or be recast with a transitive verb that takes the environment as its object (e.g., the insects cross a surface, the insects fill a gap, the insects thread a crack), such that the motion event is spatially anchored and facets can cite a specific location-state event. Knowledge delta +0.03 must be preserved.

  - id: fault-003
    type: fault
    what: b01c01s02n02 — "the insects move"
    why: Identical form to fault-002. Bare intransitive motion verb without destination. Same downstream consequence.
    criteria: Same as fault-002 criteria. Knowledge delta +0.04 must be preserved.

  - id: fault-004
    type: fault
    what: b01c01s02n07 — "the needle moves"
    why: `move` is a motion verb and the bone supplies no destination. `the needle moves` during net-mending is a concrete in-scene event, but the bone fails to anchor where the needle moves (through the mesh, across the net, along a seam). Bare intransitive motion; same categorical schema violation as fault-002 and fault-003.
    criteria: The bone must supply a destination or be recast with a transitive verb that takes the net or mesh as its object (e.g., the needle crosses the mesh, the needle pierces the net, the needle threads the cord), such that the motion event has a spatial anchor. Knowledge delta +0.03 must be preserved.

---

## Gotcha resolutions (auditable record of close calls)

- **s01n02 the-door-keeper hyphen**: Hyphenated unnamed entity form; schema permits `the <noun>` for unnamed environment elements; the door-keeper is an unnamed building fixture consistent with the chapter chunk's anonymous-building framing. Not a violation; hyphen is punctuation, not a compound-subject form.
- **s01n04 compound-form detection**: Classified as FAULT-FORM-CONJUNCTION (two actions in one line). Not FAULT-FORM-MULTI-SUBJECT — the subjects are distinct agents (taylor / coll) performing distinct actions; the violation is the compression of two actions, not a multi-subject subject-slot.
- **s01n06 / s02n02 / s02n07 `moves` vs. `exhales` exception**: The schema's landing-clean intransitive exception is illustrated by `taylor exhales` — a verb that is complete without a destination. `Move` is semantically incomplete without destination (it implies spatial relocation); the exception does not extend to it. Classified FAULT-FORM-NO-VERB on all three.
- **s01n07 / s02n04 `handles`**: Not on explicit deny-list; `handles` in active craft context (turning, pulling, checking mesh) denotes a discrete physical act rather than sustained carrying or stative possession. CORRECT.
- **s01n08 `faces the street`**: `faces <X>` is explicitly named in schema as a valid transitive recast for the banned `turns to` form. CORRECT.
- **s02n03 `the walls cool`**: Thermal state-change intransitive; not a motion verb; no destination implied; analogous to `taylor exhales`. CORRECT.
- **s02n05 `the city-watch passes the hook`**: Transitive motion with `the hook` as destination-object. Not bare intransitive. CORRECT.
- **s02n06 `holds the feet` / s03n05 `holds the eyes`**: Narrow `holds` license applies to both. s02n06: feet are subject's body part; stillness-against-pressure (working posture). s03n05: eyes are subject's body part; stillness-against-pressure (gaze held under social pressure). Both CORRECT.
- **s03n02 `approaches taylor`**: Transitive — taylor is the destination terminus. Not bare intransitive. CORRECT.
- **s03n07 `leaves the street`**: Transitive — the street is the origin-object. Not bare intransitive. CORRECT.
- **Scene aggregates**: All three scene sums match targets exactly (0.20, 0.20, 0.10). Fixer must preserve the per-bone delta values on all four faulty bones when recasting SVO form.

---

VERDICT: FAULTS-4
Bones with clean FAULT: fault-001 (b01c01s01n04), fault-002 (b01c01s01n06), fault-003 (b01c01s02n02), fault-004 (b01c01s02n07).
19 of 23 bones CORRECT. All scene aggregates CORRECT. No constraint, physical, cost-ledger, or aggregate-delta findings.
