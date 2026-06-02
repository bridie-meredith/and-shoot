---
reviewer: worm-canon-pedant
facet: location-state
episode: b01c08
phase: 5b-adversarial
round: r1
date: 2026-05-31
verdict: accept
entries-reviewed: 6
entries-attacked: 2
callouts-blocking: 0
callouts-advisory: 2
convergence-auditor-findings: flag-004 (partial), flag-005
---

# Worm-Canon-Pedant — Location-State b01c08 — Adversarial R1 Verdict

## Earth-Bet Hard-Fence Scan

Word-by-word scan of all six entries: location-slug, time, weather, conditions, sensory note.

Checked for: Brockton Bay, Skitter, Khepri, Gold Morning, PRT, Protectorate, Endbringer, parahuman, trigger event, shard, shard terminology (Manton effect, shaker ratings, cluster trigger), cape-ratings language, any other Earth-Bet proper noun or Worm-specific jargon.

Result: zero hits. The six slugs name Westeros-specific geography. The sensory notes name physical things — a broken sightline on a stone skirt, a posted position, a basket-woman's angle, a fixed-point receipt surface, a water-point approach, a vacated position. None of it activates the fence.

The feed-station and Jarvis-channel intake are project-canon constructs, cleared per dispatch mandate. "Intake" is used correctly as a receipt-surface descriptor. No Earth-Bet contamination.

**Earth-Bet fence: CLEAR.**

---

## Dance-Era / Pre-Dance Proper-Noun Scan

122 AC King's Landing, pre-Dance. Scope check: the loc-state facet references the-hook-ward (Flea Bottom canal district, consistent with pre-Dance Hook geography), the-lane-junction-rushwick-margin (Rushwick as named Flea Bottom sub-area, Pig Tallow Lane adjacency — consistent with 122 AC street topology), and the-feed-station (project-original construct).

Aemond Targaryen's name is live in the bones at @13 but does NOT appear in the loc-state file. The loc-state facet at @9 (nearest bone) reads only "the Jarvis channel's intake station — a fixed-point receipt location inside the Hook coverage radius." No proper noun, no leak.

No Dance-era character names, event-names, or location-proper-nouns in any field of any entry.

**Dance-era proper-noun fence: CLEAR.**

---

## Per-Entry Adversarial Review

### [loc-state:1] @1 — the-lane-junction-rushwick-margin

Anchor: `taylor-hebert-kl-122ac enters the lane-junction-rushwick-margin`. Entry verb. First beat in the chapter's first location. First-beat-in-new-location necessity slot passes without further test.

Sensory note: `the junction's broken sightline on the north side where the hill's stone skirt cuts the view`. One focus-element. The broken sightline is selected, not swept — every other feature of the junction is implicitly omitted. The stone skirt is the mechanism. The element is not location-card content (the location-card names the junction; this entry names what cuts visibility within it). Strip test: remove the entry; @1 resolves but the sightline geometry that @6's watcher-trace depends on is absent. Forward-justified necessity.

Frugality: first entry in the chapter. No inheritance to compare.

**No callout. ACCEPT.**

---

### [loc-state:2] @3 — the-hook-ward

Anchor: `the watcher-boy faces the water-point`. Positioning verb. Scene-map confirms @3 is a peak-shadow bone — body-anchor for the scene-C closing image, and the geometry source that @6's sightline-trace turns on.

Sensory note: `the watcher-boy's posted position at the water-point, visible from the junction approach`. One focus-element: the posted position and its visibility from the approach. The visibility qualifier is not ambient — it is the specific geometric fact that makes the later sightline-trace at @6 legible. Not a re-name of the location-card.

Frugality: new sub-location (water-point within the-hook-ward); prior cite was at the junction. State has changed.

**No callout. ACCEPT.**

---

### [loc-state:3] @4 — the-hook-ward

Anchor: `the basket-woman faces the lane-mouth`. Positioning verb. Second body in Oswyn's watcher-network.

Sensory note: `the basket-woman angled toward the lane-mouth opening, facing outward`. One focus-element: the angle and outward orientation. The orientation-direction is exactly what makes this a watcher-position rather than a woman with a basket in a lane. Strip test: remove the entry; @4 resolves as a bare positioning beat with no location anchor for what "faces the lane-mouth" means in the environment.

Frugality: new sub-location (lane-mouth vs. water-point at @3). Not a repeat.

**No callout. ACCEPT.**

---

### [loc-state:4] @9 — the-feed-station — ADVISORY

Anchor: `the jarvis-packet arrives at the feed-station`. Entry of a salient object at a new location. First-beat-in-new-location necessity slot passes.

Sensory note: `the Jarvis channel's intake station — a fixed-point receipt location inside the Hook coverage radius`.

**Attack:** The sensory note has two clauses: (a) the intake station as a physical thing, and (b) the coverage-radius geographic relationship. The rubric's pointing test: what is this entry pointing at? "The intake station" is the perceptible focus-element — the surface the packet arrives on. "Inside the Hook coverage radius" is relational-geographic content — it names the station's position within a larger operational schema, not a perceptible thing the arrival at @9 turns on. The coverage-radius clause is location-card content, not state-change content.

The entry still passes all three axes — first-beat-in-new-location holds; the intake station is a valid focus-element; no prior inheritance. But the coverage-radius clause is excess that edges toward plan-bullet residue (anti-pattern 5). The focus-element carries the entry; the second clause adds nothing perceptible that @12's `feed-geometry meets coverage-gap` doesn't do in its own SVO.

**Severity: ADVISORY.** Not a REJECT. The clause does not break the entry. The stitcher should render the perceptible intake-surface, not the geographic-relational category. Watch item for stitch.

**Convergence trace:** Auditor flag-004 (prop:oc-jarvis-packet and prop:oc-feed-station-ledger lack warehouse cards) is related — the feed-station is underspecified at the prop-object layer, and the loc-state entry's geographic-relational clause echoes that underspecification by reaching for a category label (Hook coverage radius) instead of a physical surface. Same root: the station hasn't been fully materialized as a thing in this project's object-layer.

---

### [loc-state:5] @16 — the-hook-ward

Anchor: `taylor-hebert-kl-122ac enters the hook-ward`. Return entry to the-hook-ward after the feed-station interlude. Time has advanced from afternoon to evening. First-beat-in-new-location-and-moment (same location, new moment — evening shift licenses re-citation per the frugality axis).

Sensory note: `the ward at return-circuit pass: evening register, the water-point approach where the watcher-boy's station holds by habit`. This is slightly multi-clause. The conditions field carries "water-point lit low, chandler-corner-adjacent" — those are environmental conditions, not sensory-note focus-elements. The sensory note itself runs: the approach + the habit-hold. I read this as one unified focus: this is where Taylor will look and what she will find. "By habit" is a structural qualifier naming persistence-in-environment, not a second perceptible thing. On-the-edge but not a sweep.

Frugality: time has advanced to evening; this is a re-entry after a scene-B interlude. The environment has turned over in time. Re-citation earned.

**No callout. ACCEPT.**

---

### [loc-state:6] @23 — the-hook-ward — ADVISORY

Anchor: `the watcher-boy-position falls from the water-point`. Departure/removal positioning event. State-change: the water-point moves from occupied (loc-state:5) to vacated. Necessity passes.

Sensory note: `the watcher-boy-position absent from the water-point — the contact geometry that had been present at @3 no longer occupying the approach`.

**Attack — Khepri-echo landing check.** The dispatch mandate flags this entry specifically: loc-state:6 carries part of the Khepri-echo close; the reader-Taylor recognition gap must land via geometry-completing-itself-smooth at @24 without Taylor naming consent/override/Khepri.

The entry passes the fence check — no Worm-vocabulary enters. Taylor is not named. Oswyn's unknowing is not named. The protected-pattern from the scene-map (worm-canon WATCH-3: @23 and @24 must stay structurally separate; no because-clause bridge) is honored in the loc-state facet: loc-state:6 anchors only to @23 (the vacancy); @24 (the insect-feed fills the geometry) carries no loc-state cite, correctly.

**The seam:** the sensory note's second clause — `the contact geometry that had been present at @3 no longer occupying the approach` — cross-references a prior loc-state entry rather than naming a perceptible-as-present thing. This is not a re-naming violation per the interestingness axis (it names absence against a baseline, not the baseline itself). But the `had been present at @3` phrasing is retrospective — it is written from the perspective of the reader who knows what @3 established, not purely as a feed-return of vacancy.

The scene-map's protected-patterns include: `Taylor does not name Oswyn's unknowing in either bone; "Oswyn does not know this. He is still talking when Taylor leaves" is reader-framing in the chunk but must enact through physical-departure-and-feed-coverage at stitch, NOT through interior Taylor recognition`. The loc-state:6 sensory note does not name Oswyn's unknowing — it names geometric vacancy. But the retrospective clause (`had been present at @3`) introduces the same register risk: if the stitcher renders this note literally, the `had been present` back-cast reads as Taylor-retrospective rather than feed-return. The stitcher needs to render the vacancy as present-tense feed-observation — `the water-point empty / the position gone` — not as geometric-accounting with a prior-state cross-reference.

**Severity: ADVISORY.** This is a stitch-rendering risk embedded in the sensory note's phrasing, not a rubric fail at the facet level. The entry passes necessity (departure/removal beat; genuine state-change), interestingness (absence as perceptible fact against baseline; single focus-element), and frugality (state-change from occupied to vacated). The Khepri-echo structural close is not broken here — the vacancy is correctly staged as world-fact at @23, the fill at @24 is correctly left without loc-state citation. No revision required at the facet level. Travel this note to the stitcher: render present-tense vacancy, not retrospective geometry-accounting.

**Convergence trace:** Scene-map protected-pattern worm-canon WATCH-3 is the direct resonance — `@23 is the world-fact / @24 is the structural completion; Taylor does not name Oswyn's unknowing in either bone`. The `had been present at @3` clause is the exact seam that could generate an accidental reader-framing register at stitch. No auditor finding maps here — this is a seam the mechanical scan cannot see, which is the adversarial mandate's zone.

---

## Aggregate

| entry | Earth-Bet | Dance-era | necessity | interestingness | frugality | verdict |
|-------|-----------|-----------|-----------|-----------------|-----------|---------|
| loc-state:1 @1 | clean | clean | pass | pass | pass | ACCEPT |
| loc-state:2 @3 | clean | clean | pass | pass | pass | ACCEPT |
| loc-state:3 @4 | clean | clean | pass | pass | pass | ACCEPT |
| loc-state:4 @9 | clean | clean | pass | pass (advisory) | pass | ACCEPT |
| loc-state:5 @16 | clean | clean | pass | pass (narrow) | pass | ACCEPT |
| loc-state:6 @23 | clean | clean | pass | pass (advisory) | pass | ACCEPT |

Six entries reviewed. Six ACCEPT. Zero blocking callouts. Two advisory callouts (loc-state:4 coverage-radius clause excess; loc-state:6 retrospective sensory-note phrasing as stitch-rendering risk).

The Khepri-echo geometry is correctly staged: loc-state:6 names the vacancy at @23 without Worm-vocabulary, without Taylor naming, and without bridging the structural separation between @23 and @24. @24 correctly carries no loc-state cite. The reader who knows Khepri reads geometry completing itself. Taylor's voice stays at geometry-filed / circuit-continues.

---

## Verdict

**ACCEPT**

Two advisory notes travel to the stitcher:
1. loc-state:4 — render the intake-surface as the physical perceptible focus; omit the coverage-radius relational clause.
2. loc-state:6 — render the vacancy as present-tense feed-return (`the position gone`), not as retrospective geometry-accounting (`had been present at @3`). The back-cast register is the only seam where the Khepri-echo smooth-geometry landing could muffle into Taylor-retrospective at stitch. The facet itself is clean; this is a render instruction, not a revision flag.

The author knows where not to put Brockton Bay. Wiki tab stays closed.
