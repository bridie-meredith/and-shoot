audit:
  scope: /and-write Phase 6 substance bone-gate (mechanical)
  target: b01c01
  timestamp: 2026-05-19
  bones_audited: 27
  verdict: PASS

---

## Per-bone bonefide

| slug | svo | declared_delta | bonefide | note |
|---|---|---|---|---|
| s01n01 | taylor-hebert-kl-122ac enters the corner-room | knowledge +0.02 | PASS | Threshold-crossing registers building geometry and social texture. Δ caused by SVO. |
| s01n02 | taylor-hebert-kl-122ac pays the building-keeper | knowledge +0.03 | PASS | Transaction reveals anonymous-entry rules and keeper temperament. Payment is an information event. |
| s01n05 | taylor-hebert-kl-122ac crosses the yard | knowledge +0.02 | PASS | Traversal maps yard geometry and occupancy at walking pace. |
| s01n04 | coll-net-mender-flea-bottom lifts the eyes | knowledge +0.04 | PASS | Surveillance response makes vouching-physics externally observable. OPPOSING-FORCE bone. |
| s01n06 | coll-net-mender-flea-bottom works the net | knowledge +0.02 | PASS | Work-while-watching is coded ambient monitoring; secondary opposing-force signal confirming Taylor's presence is being socially calibrated. |
| s01n07 | taylor-hebert-kl-122ac circles the block | knowledge +0.04 | PASS | Perimeter walk maps exit geometry and sightlines. |
| s01n08 | taylor-hebert-kl-122ac drops the pack | knowledge null/0 | PASS | Anchor bone. No axis movement declared and none caused by the SVO. |
| s01n09 | coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac | knowledge +0.02 | PASS | Speech bone. Knowledge is a communication-class axis; satisfies bones-schema speech-bone rule. |
| s01n10 | taylor-hebert-kl-122ac holds the feet | capability null/0 | PASS | `holds` licensed: subject body-part, stillness-against-pressure (dormancy). Capability non-movement is a valid structural anchor. |
| s02n01 | taylor-hebert-kl-122ac lifts the basket | knowledge null/0 | PASS | Rhythm anchor bone. Physical action with no axis movement declared and none caused. |
| s02n02 | coll-net-mender-flea-bottom pulls the net | knowledge null/0 | PASS | Rhythm anchor bone. Same reasoning as s02n01. |
| s02n03 | taylor-hebert-kl-122ac threads the needle | knowledge +0.03 | PASS | Manual task focus; cover-pattern practice registers as knowledge gain through sustained spatial attention. |
| s02n06 | the needle crosses the mesh | knowledge +0.03 | PASS | Prop-as-subject physical event; mesh-crossing registers spatial pattern and cover-confirmation parallel to threading. |
| s02n04 | the insects fill the block | knowledge +0.05, capability null/0 | PASS | Insect-spread is a physical event revealing block geometry. Capability null/0 is the OPPOSING-FORCE signal: capability is available and ward geometry is legible, but the prohibition holds the gap open. |
| s02n05 | the walls cool | knowledge +0.04, capability null/0 | PASS | Environmental shift marking time-of-day and geometry transition. Secondary OPPOSING-FORCE on capability axis. |
| s02n10 | the boots strike the cobbles | knowledge +0.01 | PASS | Auditory physical event; approach footfall is a bridge cue for watch arrival. |
| s02n07 | the city-watch passes the hook | knowledge +0.05 | PASS | Physical movement; patrol route reveals watch-pattern timing and geography. |
| s02n08 | taylor-hebert-kl-122ac holds the eyes | knowledge null/0, capability null/0 | PASS | `holds` licensed: subject body-part, stillness-against-pressure (discipline-catch). Dual null is a valid catch anchor. |
| s02n09 | coll-net-mender-flea-bottom folds the net | knowledge +0.03 | PASS | Physical close action; scene-closing transaction. |
| s03n01 | wren-stitch-maker-flea-bottom-ward enters the street | knowledge +0.02, capability null/0 | PASS | Physical arrival shifts observable social geometry. The entry is the external trigger that initiates the automatic assessment pattern. OPPOSING-FORCE bone. |
| s03n02 | wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac | knowledge +0.03 | PASS | Speech bone. Communication-class axis. Speech completes the external trigger package. |
| s03n03 | taylor-hebert-kl-122ac lifts the eyes | knowledge +0.01, capability null/0 | PASS | Physical gaze-raise; the involuntary assessment-pattern initiation is the OPPOSING-FORCE bone (Taylor's own trained pattern-reading fires automatically). |
| s03n04 | taylor-hebert-kl-122ac speaks to wren-stitch-maker-flea-bottom-ward | knowledge +0.02 | PASS | Speech bone. Communication-class axis. |
| s03n05 | wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac | knowledge +0.02 | PASS | Speech bone. Communication-class axis. |
| s03n06 | taylor-hebert-kl-122ac holds the eyes | capability null/0 | PASS | `holds` licensed: subject body-part, stillness-against-pressure (catch — rule intercepting the assessment-pattern). |
| s03n07 | wren-stitch-maker-flea-bottom-ward crosses the street | knowledge null/0 | PASS | Physical exit. No axis movement declared and none caused. |
| s03n08 | taylor-hebert-kl-122ac lifts the needle | capability null/0 | PASS | Physical close action returning to cover-activity. Closing dormancy anchor. |

---

## Per-scene mechanical

### s01
- Δ-delivery (knowledge): 0.02 + 0.03 + 0.02 + 0.04 + 0.02 + 0.04 + 0.00 + 0.02 + 0.00 = 0.19. Target 0.2, band 0.15–0.25. **PASS**
- Δ-delivery (capability): all null/0. Target null/0. **PASS**
- Opposing-force visible: s01n04 (coll lifts the eyes) surfaces vouching-physics as external social pressure requiring a stranger to be vouched in. **PASS**
- Cost-ledger: no entries resolve at b01c01. All bones cost_ledger_anchor null. **PASS**

### s02
- Δ-delivery (knowledge): 0.00 + 0.00 + 0.03 + 0.03 + 0.05 + 0.04 + 0.01 + 0.05 + 0.00 + 0.03 = 0.24. Target 0.2, band 0.15–0.25. **PASS**
- Δ-delivery (capability): all null/0. Target null/0. **PASS**
- Opposing-force visible: s02n04 (the insects fill the block) + s02n05 (the walls cool) — capability available and ward geometry legible, prohibition holding the gap. **PASS**
- Cost-ledger: no entries resolve at b01c01. All bones cost_ledger_anchor null. **PASS**

### s03
- Δ-delivery (knowledge): 0.02 + 0.03 + 0.01 + 0.02 + 0.02 + 0.00 + 0.00 + 0.00 = 0.10. Target 0.1, band 0.07–0.13. **PASS**
- Δ-delivery (capability): all null/0. Target null/0. **PASS**
- Opposing-force visible: s03n01–s03n03 (entry / speech sequence) constitute the external trigger package activating Taylor's trained assessment-pattern; s03n03 (taylor lifts the eyes) is the explicit OPPOSING-FORCE bone. **PASS**
- Cost-ledger: no entries resolve at b01c01. All bones cost_ledger_anchor null. **PASS**

---

## HARD findings

(none)

---

## SIGNAL findings

(none)

---

## Verdict

PASS

All 27 bones bonefide: every non-zero Δ has a physically plausible SVO cause; every null-magnitude bone functions as a legitimate structural anchor (dormancy, rhythm, catch, or close). All three scenes deliver axis-Δ within band. Opposing force is visible in each scene via explicitly labeled bones. No cost-ledger entries resolve at this chapter; no cost-not-paid or cheap-gain risk. HARD count: 0. SIGNAL count: 0.
