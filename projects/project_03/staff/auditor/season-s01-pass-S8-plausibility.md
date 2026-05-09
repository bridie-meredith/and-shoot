# Season S01 — Pass S8 Plausibility Audit

```
scope: season
target: s01 (chapter-01 through chapter-10 + 3 interludes)
timestamp: 2026-05-07
axes:
  A: character-action plausibility
  B: event-in-world plausibility
verdict: REVISE
fault_counts:
  fault-A01: 1 (range violation)
  fault-B01: 1 (institutional standing gap, propagates 5/7/10)
  fault-A02: 1 (linked to B01)
  flags: 4 (1 escalates if unresolved)
```

---

## VERDICT: REVISE

Two faults require resolution before chapters 05/06/07/10 can shoot cleanly. One linked fault depends on the worldbuilding resolution of fault-B01. One flag escalates to fault if chapter-09 proceeds without a location anchor. Two flags advisory only.

---

## FAULTS

### fault-A01 — Axis A — character-action

**What:** chapter-06.md lines 56–105 — Taylor deploys two raven groups against couriers from the sept bell tower.

**Why:** Sept is half a league (~2.5 km) from Harrenhal. `cond-fauna-control-rules` sets Taylor's hard ceiling at 600m with immediate blackout risk above. The couriers she harasses are on the Harrenhal approach road — within the castle's immediate approaches, not within 600m of the sept. Deployment as written = operation at 4× her maximum range.

**Criteria:** chapter-06 must (a) establish Taylor's position at open within 600m of the target road segment, OR (b) revise mechanics so pre-positioned ravens are driven from a nearer point. Physical position and cost curve must both cohere with the condition card.

### fault-B01 — Axis B — event-in-world

**What:** Plumm (Lannister-affiliated extraction officer) files and wins a wardship claim through Hatch's (Hightower castellan's) administrative machinery. Affects chapter-05, chapter-07, chapter-10.

**Why:** Wardship claims process through the lord's administrative record — Hatch's record at Harrenhal. Plumm holds a supply-and-requisition commission from Lannister command; he is not a member of Hatch's household or administrative staff. No worldbuilding establishes his standing to file in Hatch's record system. The recorder accepting Plumm's filing (ch07) requires that standing; Hatch adjudicating in Plumm's favor (ch10) requires it. Lannister-Hightower political alignment in 120 AC is canon-plausible but does not automatically produce cross-institutional administrative filing rights.

**Criteria:** Establish Plumm's institutional standing before ch07 and ch10 shoot. Three routes:
- (a) Worldbuilding note: Plumm holds a concurrent commission from Hatch deputizing him to assist with the census and anomaly record in the Harrenhal shadow settlements. Grants standing in Hatch's record system. **Resolves fault-A02 simultaneously.**
- (b) Revise the claim mechanic so Plumm files through a Lannister record that Hatch then adjudicates against, requiring explicit cross-house claim recognition.
- (c) Condition card note in `cond-westerosi-customary-authority` establishing cross-institutional filing standing for Lannister officers in Hightower-administered territory at 120 AC.

### fault-A02 — Axis A — character-action (linked to B01)

**What:** chapter-05.md lines 30–70 — Septon Rowan intercedes with Plumm at the Harrenhal gatehouse rather than with Hatch.

**Why:** An ecclesiastical challenge to ward status goes to the party with administrative authority over wardship classification — Hatch, not Plumm. Absent the worldbuilding established by fault-B01, Plumm holds no authority in Hatch's wardship system. Rowan going to Plumm misroutes the intercession. If the chapter intends Rowan's wrongness to be the dramatic mechanism, that failure needs to be legible in the text.

**Resolution dependency:** If fault-B01 resolved by route (a), Plumm holds partial authority over the anomaly record and Rowan's intercession is plausible. fault-A02 resolves automatically. If routes (b) or (c) are taken, ch05 must revise Rowan's intercession target to Hatch, or make the misdirection an explicit character failure.

**Criteria:** Resolve alongside fault-B01.

---

## FLAGS

### flag-A01 — Axis A — advisory

**What:** chapter-01.md line 71 — "septon-dying-protector rises".

**Why:** Septon card sets physical capacity at near zero, hard fence against physical action. Line 71 records rise; line 72 records fall. Defensible as partial/abortive attempt, but "rises" as bare proto-line implies completed physical action. At shoot, impersonator brief must constrain as failed attempt, not successful stand.

### flag-A02 — Axis A — escalates to fault if ch09 shoots without resolution

**What:** chapter-09.md lines 1–2 and 78 — Taylor dispatches raven, sparrow, and fly toward/into Harrenhal with no location anchor for her position at chapter open.

**Why:** If Taylor is at the sept, all three deployments require range beyond her 600m maximum — matching fault-A01. Chapter provides no spatial anchor. Advisory because ch07 established Taylor can walk to Harrenhal; she could have repositioned near the walls.

**Criteria:** ch09 must establish Taylor's position at open before shoot. If she is at the sept, lines 1–2 and 78 are a range fault. If within 400–600m of Harrenhal's walls, a location-anchor beat is required at chapter open. Shoot blocker.

### flag-B01 — Axis B — advisory

**What:** chapter-09.md lines 66–76 — Celtigar arrives with a cart through the postern gate.

**Why:** A crown agent of Celtigar's standing arriving through the postern rather than the main gate is unusual. Plausible under reduced-garrison conditions if postern is the primary controlled entry point under Hatch. If a Harrenhal exterior location card is authored before pass 5, it should specify the active controlled entry.

### flag-B02 — Axis B — advisory

**What:** chapter-10.md — Bracken absent at the wardship resolution.

**Why:** Bracken filed counter-claim in ch09. Ch10 resolves without him. His holding is at the western edge of Bracken lands. If Hatch moves to resolve the same day as Celtigar's arrival, Bracken may not have received notice. The procedural basis for resolving a contested wardship without the counter-claimant present should be reviewed against `cond-westerosi-customary-authority` before ch10 shoots.

---

## CLEAN PASSES (summary)

- ch02 administrative circuit + report-before-copy structure: consistent with feudal survey mechanics.
- ch02 fauna cost curve (headache 29–31, nosebleed 52): correctly tracks 5–15 min / 15–30 min thresholds.
- ch02 starlings around hamlet girl (62–64): ambient fauna, plausible observer inference.
- ch03 fauna disturbance-without-source: within passive-sense mechanics.
- ch04 castellan's personal inspection: within Hatch's adaptability-5 character.
- ch04 raven on Taylor's arm: within "going direct" last-resort action menu.
- ch06 fauna cost curve (nosebleed 82): tracks 15–30 min threshold (passes independently of fault-A01).
- ch07 Plumm's counter-claim timing: consistent with character.
- ch08 maester assessment (word list, counting board, sketch): consistent with Citadel toolkit; armed man consistent with Hatch's contested-status protocol.
- ch09 Bracken's counter-claim entry: consistent with leverage/secondary-position strategy.
- ch10 Celtigar forcing administrative resolution: consistent with institutional posture.
- ch10 Taylor at formalization (holds chin / stills hands / exhales): consistent with default stance under institutional processing.
