# /and-write Phase 2 — constraint audit — b01c01

audit:
  scope: /and-write Phase 2 constraint audit
  target: b01c01
  timestamp: 2026-05-19
  bones_audited: 27
  verdict: FAULTS-3

---

## Per-bone classification (27 rows)

| bone | svo | classification | rationale |
|------|-----|----------------|-----------|
| b01c01s01n01 | `taylor-hebert-kl-122ac enters the corner-room` | PASS | `enters` is directed-motion transitive with named destination. No copula, negation, perception, non-action, modifier, conjunction, or multi-subject fault. No constraint violation. |
| b01c01s01n02 | `taylor-hebert-kl-122ac pays the building-keeper` | PASS | `pays` is direct-action transitive. `the building-keeper` is a licensed unnamed-noun form. Copper-stars payment consistent with cond-kl-social-physics-122ac (Taylor at copper-star level at story open). No Earth-Bet jargon. |
| b01c01s01n03 | `the building-keeper pockets the copper-stars` | PASS | `pockets` is direct-action transitive. Ambient subject licensed. Copper-stars as smallest currency unit consistent with cond-kl-social-physics-122ac. No constraint violation. |
| b01c01s01n04 | `coll-net-mender-flea-bottom faces the street` | PASS | `faces <X>` is explicitly licensed as a valid transitive recast for `turns to <X>`. No fault applies per dispatch narrow-license catalog. No constraint violation. |
| b01c01s01n05 | `taylor-hebert-kl-122ac crosses the yard` | PASS | `crosses` is directed-motion transitive with named space as object. No fault-form. No constraint violation. |
| b01c01s01n06 | `coll-net-mender-flea-bottom works the net` | PASS | `works` is direct-action transitive. Net is Coll's prop consistent with role slug. No constraint violation. |
| b01c01s01n07 | `taylor-hebert-kl-122ac circles the block` | PASS | `circles` is directed-motion transitive with named spatial object. Flea Bottom consistent with cond-kl-geography-122ac. No Earth-Bet jargon. |
| b01c01s01n08 | `taylor-hebert-kl-122ac drops the pack` | PASS | `drops` is direct-action transitive. Pack is a physical prop consistent with arrival context. Axis null/0 correct for non-knowledge-bearing settling beat. |
| b01c01s01n09 | `coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac` | PASS | Licensed speech-bone form `<speaker> speaks to <listener>`. Moves knowledge (communication-class axis). Licensed. Both actors present in Flea Bottom. |
| b01c01s01n10 | `taylor-hebert-kl-122ac holds the feet` | PASS | Narrow `holds` license applies: object is a body part of subject AND action is stillness-against-pressure. Explicitly licensed per dispatch. Capability null/0 correct for discipline/stillness beat. |
| b01c01s02n01 | `taylor-hebert-kl-122ac lifts the basket` | PASS | `lifts` is direct-action transitive. Basket consistent with working-day labor context. Axis null/0 correct for non-knowledge-bearing opening beat. |
| b01c01s02n02 | `coll-net-mender-flea-bottom pulls the net taut` | FAULT-FORM-MODIFIER | `taut` is a resultative adjective appended to the direct object. The dispatch FAULT-FORM-MODIFIER catalog prohibits adjectives as modifiers on the object. The complete SVO is `pulls the net`; `taut` extends it with a result-state descriptor that does not belong in the bone field. |
| b01c01s02n03 | `taylor-hebert-kl-122ac threads the needle` | PASS | `threads` is direct-action transitive. Needle is a working prop consistent with net-mending context. Knowledge up 0.03 valid. |
| b01c01s02n04 | `the insects fill the block` | PASS | `fill` is an ambient-drift transitive verb. Subject `the insects` is a licensed unnamed collective. No active-sweep verb. Passive-ambient description consistent with rank-3 ceiling in cond-override-architecture-residue-122ac. No Earth-Bet jargon. Dual axis (knowledge up 0.05; capability null 0) both valid. |
| b01c01s02n05 | `the walls cool` | PASS | `cool` is an ambient-drift intransitive verb describing environmental thermal change; not a position-naming stand/sit/lie form. Consistent with passive insect-sense thermal registration at rank 3. No Earth-Bet jargon. Dual axis (knowledge up 0.04; capability null 0) both valid. |
| b01c01s02n06 | `taylor-hebert-kl-122ac draws the needle through the mesh` | FAULT-FORM-MODIFIER | `through the mesh` is a prepositional phrase extending the direct object with a path description. The dispatch FAULT-FORM-MODIFIER catalog prohibits prepositional padding on the object. The complete SVO is `draws the needle`; the prepositional phrase does not belong in the bone field. |
| b01c01s02n07 | `the city-watch passes the hook` | PASS | `passes` is directed-motion transitive with named location as object. `the city-watch` is a licensed unnamed collective. The Hook is a canonical Flea Bottom street per cond-kl-geography-122ac. Watch patrolling the Hook consistent with cond-kl-social-physics-122ac. Knowledge up 0.05 valid. |
| b01c01s02n08 | `taylor-hebert-kl-122ac holds the eyes` | PASS | Narrow `holds` license applies: object is a body part of subject AND action is stillness-against-pressure. Explicitly licensed per dispatch. Dual axis null/0 correct for discipline/stillness beat. |
| b01c01s02n09 | `coll-net-mender-flea-bottom sets the net aside` | FAULT-FORM-MODIFIER | `aside` is an adverb appended to the verb naming the result-direction of the action. The dispatch FAULT-FORM-MODIFIER catalog prohibits adverbs. The complete SVO is `sets the net`; `aside` extends it with a directional result-modifier that does not belong in the bone field. |
| b01c01s03n01 | `wren-stitch-maker-flea-bottom-ward enters the street` | PASS | `enters` is directed-motion transitive with named destination. wren-stitch-maker-flea-bottom-ward is a listed cast member. No constraint violation. Dual axis (knowledge up 0.02; capability null 0) both valid. |
| b01c01s03n02 | `wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` | PASS | Licensed speech-bone form. Moves knowledge (communication-class axis). Licensed. Both actors present. |
| b01c01s03n03 | `taylor-hebert-kl-122ac faces wren-stitch-maker-flea-bottom-ward` | PASS | `faces <X>` is explicitly licensed as a valid transitive recast for `turns to <X>`. No fault applies per dispatch narrow-license catalog. No constraint violation. |
| b01c01s03n04 | `taylor-hebert-kl-122ac speaks to wren-stitch-maker-flea-bottom-ward` | PASS | Licensed speech-bone form. Moves knowledge (communication-class axis). Licensed. Both actors present. |
| b01c01s03n05 | `wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` | PASS | Licensed speech-bone form. Moves knowledge (communication-class axis). Licensed. Both actors present. |
| b01c01s03n06 | `taylor-hebert-kl-122ac holds the eyes` | PASS | Narrow `holds` license applies: body-part-of-subject, stillness-against-pressure. Explicitly licensed per dispatch. Capability null 0 correct. |
| b01c01s03n07 | `wren-stitch-maker-flea-bottom-ward crosses the street` | PASS | `crosses` is directed-motion transitive with named space as object. Axis null/0 correct for departure beat. |
| b01c01s03n08 | `taylor-hebert-kl-122ac lifts the needle` | PASS | `lifts` is direct-action transitive. Needle is a working prop consistent with net-mending context. Capability null 0 correct for closing beat. |

---

## Per-scene aggregate verification

| scene | axis | bone-level sum | target | delta from target | result |
|-------|------|---------------|--------|-------------------|--------|
| s01 | knowledge | 0.02+0.03+0.01+0.04+0.02+0.02+0.04+0+0.02+0 = **0.20** | 0.20 | 0.00 | PASS (exact) |
| s01 | capability | all null/0 | null | — | PASS |
| s02 | knowledge | 0+0+0.03+0.05+0.04+0.03+0.05+0+0.03 = **0.23** | 0.20 | +0.03 | PASS (within ±0.1 tolerance) |
| s02 | capability | all null/0 | null | — | PASS |
| s03 | knowledge | 0.02+0.03+0.01+0.02+0.02+0+0+0 = **0.10** | 0.10 | 0.00 | PASS (exact) |
| s03 | capability | all null/0 | null | — | PASS |

No FAULT-AGGREGATE-DELTA-MISMATCH findings.

---

## Constraint audit

| constraint card | verdict | notes |
|----------------|---------|-------|
| cond-override-architecture-residue-122ac | PASS | No bone implies Khepri-mantle (human coordination/override). All capability deltas null/0. Ambient-drift bones (s02n04 `fill`, s02n05 `cool`) use passive-ambient verbs only; no active-sweep verb present. No range violation implied. KL passive-awareness load (s02n04, s02n05) is consistent with the card's description of Flea Bottom as high-density requiring suppression. No parahuman terms. |
| cond-earth-bet-noun-fence | PASS | No Worm-canon proper noun, power-classification term, institutional term (PRT, Protectorate, Wards, Undersiders, Cauldron), cape-name, or Earth-Bet geography in any bone SVO. "Khepri" absent. Gold Morning absent. |
| cond-westerosi-magic-dormant-122ac | PASS | No Westerosi native magic mechanism invoked. No glass-candle, greenseer, shadowbinding, or faceless-man element in any bone. |
| cond-kl-witch-label-formation-122ac | PASS | No bone positions Taylor as visibly anomalous to witnesses in a label-accumulating way. Ambient-drift bones are internal-perspective reads, not observer-visible events. No single-observation label formation implied. No behavioral-foreknowledge flicker trigger. |
| cond-kl-court-state-122ac | PASS | No court-level characters on-stage. Daemon not present. Lucerys not referenced. Otto Hightower not present. No scene implies Taylor has direct court-level intelligence. |
| cond-kl-geography-122ac | PASS | All bones set in Flea Bottom / the Hook / adjacent streets. `the city-watch passes the hook` (s02n07) correctly names the Hook as a canonical Flea Bottom street. No geographic placement errors. |
| cond-kl-social-physics-122ac | PASS | Payment in copper-stars (s01n02–n03) consistent with Taylor's story-open economic position. Watch patrolling the Hook (s02n07) consistent with district-patrol patterns. No gold dragons. No Watch response faster than latency permits. |
| cond-taylor-pov-behavior | PASS | No interiority, thought-figures, or abstraction-as-object in any bone SVO. All bones are external action. No theme-narration present at bone level. |
| cond-westerosi-witness-vocabulary | PASS | No Westerosi character uses parahuman vocabulary in any bone. No mechanism-correct identification present. No dragon-connection attribution. |
| cond-road-to-hell-chain-shape | PASS | Chapter b01c01 is the story-open establishment chapter. No auditable-mistake beat required here. Wren (the closing-image cost-bearer) is correctly introduced at s03. No bone enacts or approaches thematic irony as a statement. No authorial-correction framing at bone SVO level. |

---

## Findings

findings:
  - id: fault-001
    type: fault
    what: b01c01s02n02 — svo `coll-net-mender-flea-bottom pulls the net taut`
    why: `taut` is a resultative adjective appended to the direct object, naming the result-state achieved by the action. FAULT-FORM-MODIFIER. The bone field must contain the action on the object only; result-state descriptors are not permitted in the SVO field. The rhythm-anchor function of this bone and its null knowledge delta are not affected by the form fault; substance is well-formed.
    criteria: the corrected SVO must carry the action on the direct object without appending a resultative adjective or result-state modifier; the null knowledge delta and rhythm-anchor function must be preserved

  - id: fault-002
    type: fault
    what: b01c01s02n06 — svo `taylor-hebert-kl-122ac draws the needle through the mesh`
    why: `through the mesh` is a prepositional phrase extending the direct object with a path description. FAULT-FORM-MODIFIER. The dispatch catalog enumerates prepositional padding (into, onto, towards, in the X, with the X, by the X) as a fault; `through the mesh` is the same class. The complete bone action is `draws the needle`; the path phrase does not belong in the SVO field. The knowledge delta (+0.03) is well-formed and must be preserved.
    criteria: the corrected SVO must carry the action on the direct object without a prepositional phrase extending the object or path; knowledge delta +0.03 must be preserved in the corrected form

  - id: fault-003
    type: fault
    what: b01c01s02n09 — svo `coll-net-mender-flea-bottom sets the net aside`
    why: `aside` is an adverb appended to the verb naming the result-direction of the action. FAULT-FORM-MODIFIER. The dispatch catalog explicitly prohibits adverbs. The complete bone action is `sets the net`; the directional adverb does not belong in the SVO field. The knowledge delta (+0.03) is well-formed and must be preserved.
    criteria: the corrected SVO must carry the action on the direct object without an adverb or result-direction extension; knowledge delta +0.03 must be preserved in the corrected form

---

## Verdict

FAULTS-3

24 of 27 bones PASS. All three scene aggregate deltas PASS. All 10 constraint cards PASS. No FAULT-PHYSICAL, no FAULT-CONSTRAINT, no FAULT-BONE-DELTA-MALFORMED, no FAULT-AGGREGATE-DELTA-MISMATCH, no FAULT-COST-LEDGER-UNRESOLVED findings. The three faults are form-only (FAULT-FORM-MODIFIER in the SVO field); all three bones carry well-formed substance deltas that fixer must preserve. `faces` bones (s01n04, s03n03) are LICENSED per dispatch narrow-license catalog — not faulted. `holds` bones (s01n10, s02n08, s03n06) are LICENSED — not faulted. Speech bones (s01n09, s03n02, s03n04, s03n05) are LICENSED — not faulted.
