# Pass S9 — Comprehensibility Review (season scope)
# Reviewer: cape-fic-reader
# Input: active-project/theater/proto-lines/s01.bones.md + active-project/staff/showrunner/season-s01-plan.md
# Date: 2026-05-11

---

## File-level verdict

COMPREHENSIBILITY-RISK-fragile-chains

Three fragile cause-effect chains require prose-level anchoring to survive stitching. One structural integrity issue (non-sequential bone numbering) creates downstream processing risk. No attention-floor failure.

---

## Structural anomaly — out-of-sequence bone numbering

The file header states "Continuous flat numbering 1..N." This is violated. High-number bones (495–508) are interpolated throughout the low-number sequence at their intended narrative positions:

- 495, 504 — inserted in beat-6 block (around bones 83–92)
- 506 — inserted in beat-7 block (around bones 128–134)
- 500, 501, 502, 508 — inserted in beat-10 block (around bones 200–207)
- 505 — inserted in beat-14 block (around bones 266–278)
- 496 — inserted in beat-16 block (around bones 296–301)
- 497 — inserted in beat-19 block (around bones 344–359)
- 503 — inserted in beat-22 block (around bones 416–422)
- 498, 499, 507 — inserted in beat-24 block (around bones 438–453)

Any downstream pass that reads by bone number rather than file position will misorder these proto-lines. File position is the correct read order; numbering is not reliable for sequential reconstruction.

---

## Load-bearing beats

The following beats are load-bearing — their absence or misreading breaks cohesion downstream.

**Beat 3 / bones 36–55 — mother's song test**
Load-bearing for the mother-arc and village-foreclosure sequence. The entire mother-side closure depends on the reader registering that Taylor did not finish the song. The bones render this as "taylor-hebert-flea-bottom holds the eyes" (bone 42) followed by "oc-tanner-mother drops the song" (bone 43). "Holds the eyes" does not obviously mean "failed to respond to the song." The cause-effect chain — Taylor silent → mother drops song → mother's foreclosure completes — must be anchored at prose level. This is the most fragile single chain in the file. If the prose renders "holds the eyes" as a neutral beat rather than a non-response, the mother's walk home (beat 9, bone 178) and the vigil scene (beat 17) lose their established cause. Flagged for emphasis/explicit anchoring in prose.

**Beat 5 / bones 62–77 — lord's man file opens**
Load-bearing for the Hightower arc. Two-scene structure: reeve observes Taylor in the yard (bones 62–68), then lord's man receives the reeve's information off-stage and writes his entry (bones 71–76). The hinge (reeve tells lord's man about Taylor) is an off-stage transfer visible only to the reader who tracked the reeve's hesitation in bones 66–68. If the reeve's slowed step (bone 66) is not registered as the notice-event, the lord's man's entry at bones 74–75 has no legible origin. Prose must make bones 66–68 a clear decision point.

**Beat 9 / bone 164 — unidentified "arrival" at the junction**
Bones 163–166: Taylor approaches the junction, then "the arrival enters the junction," Taylor pivots toward the arrival, father holds his step. The identity of "the arrival" is unclear. Two possible readings: (a) "the arrival" is Taylor's arrival registered from the father's perspective — but Taylor is already "approaching" in bone 163, and her perspective is the POV throughout; (b) a third unnamed party enters the junction. If (a), the bones create a POV split without marking it. If (b), there is an unnamed actor whose appearance causes the father's strategic-scan catch. The plan describes the father registering a "half-second strategic-scan Taylor does before turning to a speaker" — which implies the arrival is someone Taylor pivots toward (a speaker), not Taylor herself. Prose must resolve the identity of "the arrival" and make the father's scan of Taylor's reaction to the arrival legible as the catch.

**Beat 20 / bones 361–375 — the naming event**
Load-bearing for the Hightower arc's point of no return. The apothecary owner names Taylor to the second clerk. At bones level, beats 18 and 20 read as structurally similar: clerk enters, speaks to someone, writes, leaves, flies relay, Taylor logs. The distinction that makes beat 20 dangerous rather than routine — the owner naming her specifically, the profile match — is invisible in bones. Prose must signal that bone 366 (apothecary owner's second exchange with the clerk) is the moment the name transfers, and that this is categorically different from beat 18's "reliable, strange, no known affiliations" entry. If prose renders both beats in the same register, the reader will not register that beat 20 forecloses the possibility of being wholly unknown.

---

## Fragile chains (not load-bearing but at risk)

**Beat 4 / bones 48–60 — father's labor redistribution as architecture**
The plan requires this to read as a structural pattern Taylor eventually identifies, not as three unrelated task assignments. At bones level it is three task assignments (father assigns Taylor yard-edge, routes mother, routes neighbor-boy). Prose must establish the distribution as deliberate design without Taylor explicitly naming it as such — interiority-light rendering of structural observation.

**Beat 8 / bones 136–155 — dock-runner temporal gap**
The plan specifies "two days later" between the runner's recalibration (bones 136–143) and the runner's approach through the elder (bones 145–155). The bones have a single blank separator (bone 144) between these sequences. The bones read as continuous or same-day. Prose must establish the temporal gap; without it the runner's caution (going through the elder rather than direct approach) has no established reason.

**Beat 16 / bones 296–313 — maester named**
The transition from "the maester" (unnamed) to "oc-broken-maester" (named actor designation) at bones 305–313 is the information upgrade the cape-fic-reader will track. The bones correctly make this transition. Prose must render the naming beat (chain-stripped, systematic record) explicitly enough that the reader registers the upgrade. The prior bones (296–298: beetles relay rhythm/phrase/rhythm) set up the information cascade; prose must make the "decades-organized information" legible from insect-relay data alone.

---

## Entertainment windows

12 windows surveyed across the full bones sequence.

| Window | Bones range | Beat(s) | Verdict | Note |
|--------|-------------|---------|---------|------|
| 1 | 1–23 | 1 | ENGAGED | Micro-tell sequence, tight |
| 2 | 24–60 | 2–4 | ENGAGED | Song test is sharp |
| 3 | 61–92 | 5–6 | ENGAGED | Dual-scene file-opens structure works |
| 4 | 93–126 | 7 | ENGAGED | Insect-type differentiation carries tactical interest |
| 5 | 127–155 | 8 | ENGAGED | First transaction; maester ambient |
| 6 | 156–207 | 9–10 | TOLERATED | "Arrival" ambiguity; abstract information-routing without visible stakes |
| 7 | 209–264 | 11–13 | ENGAGED | Range expansion + eviction + wage-claim: three distinct registers |
| 8 | 266–313 | 14–16 | TOLERATED | Second range expansion structurally identical to beat 11; relieved by maester naming |
| 9 | 315–359 | 17–19 | ENGAGED | Vigil scene; Hightower clerk; expansion with new apothecary-ground-floor detail |
| 10 | 360–422 | 20–22 | ENGAGED | Naming event; network cost; maester buys nothing |
| 11 | 423–453+507 | 23–24 | ENGAGED | Wage-claim on record; Red Keep facing lands as ceiling-statement |
| 12 | 454–494 | 25–26 | ENGAGED | Peak-to-denouement arc clean |

TOLERATED count: 2/12 (16.7%). No BORED. No consecutive BORED. No consecutive TOLERATED. Attention floor holds.

**Pattern flag — range-expansion structural repeat:**
Four expansion sequences (beats 11, 14, 19, 24) use near-identical bones architecture: insect-type spread x4 → perimeter walk → write × 2 → exhale → headache → log. Each sequence adds a distinguishing detail, but the structure does not vary. This is within tolerance at bones level (each expansion has a differentiating element). At prose level, if the four expansions render with the same syntactic skeleton and similar sentence cadence, windows 7, 8, 9, and 11 will accumulate TOLERATED ratings that the bones level does not yet trigger. This is an execution-level risk, not a structural blocker — but the prior cape-fic-reader flag at attempt 2 on beats 7/14/19 (11.5% TOLERATED) will extend to four beats (7/14/19/24) if prose does not vary the register.

---

## Summary of flags

| Flag type | Location | Severity |
|-----------|----------|----------|
| Structural anomaly | Out-of-sequence bone numbering throughout | Downstream processing risk |
| Load-bearing fragile chain | Beat 3, bones 36–55: song test cause-effect | Requires prose anchoring |
| Load-bearing fragile chain | Beat 5, bones 62–77: lord's man file origin | Requires prose anchoring |
| Load-bearing fragile chain | Beat 9, bone 164: "arrival" identity ambiguous | Requires resolution |
| Load-bearing fragile chain | Beat 20, bones 361–375: naming event indistinguishable from beat 18 | Requires differentiated register |
| Fragile (non-load-bearing) | Beat 4, bones 48–60: redistribution as architecture | Prose-level rendering risk |
| Fragile (non-load-bearing) | Beat 8, bones 136–155: temporal gap invisible | Prose-level rendering risk |
| Fragile (non-load-bearing) | Beat 16, bones 296–313: naming upgrade legibility | Prose-level rendering risk |
| Pattern flag (execution) | Beats 11/14/19/24: range-expansion structural repeat | Prose-level TOLERATED accumulation risk |
| Entertainment | Window 6: TOLERATED | Below threshold; no action required |
| Entertainment | Window 8: TOLERATED | Below threshold; no action required |
