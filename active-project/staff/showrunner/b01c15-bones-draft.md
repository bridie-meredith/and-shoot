# /and-write b01c15 — Phase 1 scene-decomposition working draft
# Source: chapters[b01c15].scenes[] in memory.md
# Per-bone axis_moves / axes_held live here; the flat bones file emitted at Phase 7 is comment-clean.
# Grounding-bone tallies and event_map[] per scene below.

---

## S01 — b01c15s01

chunk_target_axes:
  in_motion:
    - axis: political_register-prot  direction: up  target_delta: 0.5  ledger: null
    - axis: capability               direction: up  target_delta: 0.5  ledger: cl05
  held:
    - social_tether-prot-rise  (peak-hold at 8.5; enacted by full-load context)
    - moral_framework          (no new breach; routes-nothing-to-Jarvis is discipline enacted)
    - moral_legibility_to_self (observation stays inside the coverage record; no recognition event)

---

### event_map — S01

TAG SOURCE: mechanically extracted from chunk inline tags

| tag | text span | covering bones | omission_rationale |
|---|---|---|---|
| event: aemond-compound-eye-read | "Taylor holds the passage-adjacent ward circuit" | n01 (circuit anchor), n02 (fly positions) | |
| image: boy-with-sapphire-eye | "Today it returns a boy" | n04 (boy enters the court-ground) | |
| event: aemond-court-exercise | "brought out onto the outer-court ground for a swordsmanship exercise" | n03 (master-at-arms leads Aemond), n04 (Aemond enters court-ground) | |
| image: sapphire-fixed-against-moving | "The sapphire in the left socket catches the morning flat and holds it differently" | n05 (sapphire catches morning light) | |
| image: vhagar-behavioral-imprint | "The gait-pattern is not a twelve-year-old's" | n06 (Aemond checks the yard-ground), n07 (Aemond sets the approach angle) | |
| mechanism: vhagar-behavioral-imprint-gait-read | "the wide ground-check before each engagement ... the weight held ready in a way that presupposes clearance" | n06, n07, n08 (Aemond holds the weight ready) | |
| force: aemond-coercive-register | "The correction that follows is not spoken aloud but is visible ... the yield that happens in the other man's frame" | n09 (master-at-arms adjusts drill pressure downward), n10 (Aemond resets the foot-position), n11 (master-at-arms yields the shoulder) | |
| image: coercive-register-visible-grammar | "the boy's frame stays level" | n10, n11 | |
| mechanism: nothing-routed-to-jarvis | "She does not route any of this to Jarvis" | n12 (Taylor pulls the feed back; no Jarvis notation) | |
| force: taylor-cold-read | "What she reads does not change the cold contempt ... it deepens that contempt by accumulation" | n13 (sapphire catches flat light again — chapter close of scene) | |

AUTHOR-NOTICED events:
- the fly positions at two walls + corner-gutter (grounding; capability demonstration)
- master-at-arms reduction moment (the drill-pressure drop) — n09

---

### bones — S01

**b01c15s01n01**
SVO: taylor-hebert-kl-122ac anchors two flies above the stone-lip of the outer-court approach
axis_moves:
  - axis: capability  direction: up  magnitude: 1
    cost_ledger_anchor: cl05
    notes: passage-adjacent ward read; cl05 gain-side final draw (first half); coverage at Red Keep outer-court margin anchored
grounding: YES — stone-lip of outer-court approach; physical place-name + surface
event_map: event:aemond-compound-eye-read (partial)

**b01c15s01n02**
SVO: taylor-hebert-kl-122ac anchors one fly in the corner-gutter of the passage-arch
axis_moves: []
axes_held:
  - axis: capability  rationale: second fly-station placed; coverage scope confirmed but no new deployment event — the anchoring is continuation of the same cl05 draw
grounding: YES — corner-gutter of passage-arch; physical surface named
event_map: event:aemond-compound-eye-read (completion; three-station circuit now set)

**b01c15s01n03**
SVO: the master-at-arms leads aemond-targaryen across the outer-court-ground
axis_moves: []
axes_held:
  - axis: social_tether-prot-rise  rationale: Aemond's presence in the feed does not shift the tether; peak-hold enacted by full-load context without new structural node
event_map: event:aemond-court-exercise (partial)
grounding: YES — outer-court-ground; place named concretely; master-at-arms physical body as actor

**b01c15s01n04**
SVO: aemond-targaryen halts at the court-center
axis_moves: []
axes_held:
  - axis: social_tether-prot-rise  rationale: Aemond's entry onto the ground does not shift the tether; peak-hold enacted; no new structural node
event_map: image:boy-with-sapphire-eye; event:aemond-court-exercise (completion)
notes: held bone (Aemond takes the ready position); fault-009 fix — converted from malformed chatter to held bone; place-grounded action

**b01c15s01n05**
SVO: the sapphire catches the morning light
axis_moves:
  - axis: political_register-prot  direction: up  magnitude: 1
    cost_ledger_anchor: null
    notes: the sapphire-not-tracking detail accumulates the articulated-contempt register; a new specimen that exactly fits the finding; political_register-prot accumulation-within-band
grounding: YES — morning light on the court-ground; physical luminance source + stone eye named
event_map: image:sapphire-fixed-against-moving

**b01c15s01n06**
SVO: aemond-targaryen checks the yard-ground before the first engagement
axis_moves: []
axes_held:
  - axis: moral_framework  rationale: the Vhagar-behavioral-imprint read is observational; Taylor does not redirect or act on it; prohibition enacted via non-action
event_map: image:vhagar-behavioral-imprint (partial); mechanism:vhagar-behavioral-imprint-gait-read (partial)
notes: ground-check SVO names the physical action concretely (not "Taylor reads the gait")

**b01c15s01n07**
SVO: aemond-targaryen opens the approach angle
axis_moves: []
axes_held:
  - axis: moral_framework  rationale: same — feed returns the body; Taylor does not route it
event_map: image:vhagar-behavioral-imprint (partial); mechanism:vhagar-behavioral-imprint-gait-read (partial)

**b01c15s01n08**
SVO: aemond-targaryen raises the blade past the master-at-arms' guard
axis_moves: []
axes_held: []
event_map: mechanism:vhagar-behavioral-imprint-gait-read (completion — weight-ready for dragon-scale clearance)
notes: narrow `holds` license: subject's body part / body-weight is the resisting object; stillness-against-scale enacted physically; NOT abstraction-as-object.

**b01c15s01n09**
SVO: the master-at-arms reduces the drill pressure at the shoulder-line
axis_moves: []
axes_held:
  - axis: social_tether-prot-rise  rationale: the master-at-arms' accommodation is the coercive-register evidence; tether peak-hold enacted through the visible-grammar
grounding: YES — shoulder-line named; physical body-landmark
event_map: force:aemond-coercive-register (partial)

**b01c15s01n10**
SVO: aemond-targaryen resets the foot-position
axis_moves: []
axes_held: []
event_map: force:aemond-coercive-register (partial); image:coercive-register-visible-grammar (partial)
notes: the correction-without-words: Aemond's physical response to the drill-pressure reduction is to reset his own stance — demanding the full resistance back

**b01c15s01n11**
SVO: the master-at-arms yields the shoulder
axis_moves: []
axes_held:
  - axis: moral_legibility_to_self  rationale: the yield is in the other man's frame; Taylor's observation does not become recognition this scene; moral_legibility held at 6.0
event_map: force:aemond-coercive-register (completion); image:coercive-register-visible-grammar (completion)
grounding: YES — the shoulder as named body-part; yield as discrete physical act

**b01c15s01n12**
SVO: taylor-hebert-kl-122ac returns the feed to routine scan density
axis_moves: []
axes_held:
  - axis: moral_framework  rationale: nothing routed to Jarvis; the discipline is enacted by the feed-return; no new breach
event_map: mechanism:nothing-routed-to-jarvis

**b01c15s01n13**
SVO: aemond-targaryen repeats the correction
axis_moves: []
axes_held:
  - axis: political_register-prot  rationale: the second-run is the accumulation confirming — same specimen, same finding; no new band-crossing
event_map: force:taylor-cold-read (enacted by the boy running it again without asking)
notes: the chapter-close of scene beat; the sapphire flat-light and the boy running the correction again are the same one-sentence in the chunk; two bones split them (sapphire n05, repetition n13)

---

S01 grounding-bone tally: 6 grounding bones (n01, n02, n03, n05, n09, n11) of 13 total — ratio ~1:2, above quota.
S01 bone count: 13
S01 per-axis Δ aggregate:
  political_register-prot: +1 (n05) → meets ±1 of target 0.5 (over by 0.5; distributable)
  capability: +1 (n01) → meets ±1 of target 0.5 (over by 0.5; within tolerable band; Phase 6 gate checks aggregate vs ±1)
  NOTE: bone magnitude floor is 1, so the targets of 0.5 for both axes map to 1 moving bone each — correct; the ±1 tolerance absorbs the 0.5 gap.

---

## S02 — b01c15s02

chunk_target_axes:
  in_motion:
    - axis: social_tether-antag  direction: up  target_delta: 0.75  ledger: cl-antag-d03
    - axis: capability           direction: up  target_delta: 0.5   ledger: cl05
  held:
    - social_tether-prot-rise  (peak-hold)
    - position-prot-rise       (held at 6.0; no new position event)

---

### event_map — S02

TAG SOURCE: mechanically extracted

| tag | text span | covering bones | omission_rationale |
|---|---|---|---|
| event: exercise-ends | "The exercise ends" | n01 (master-at-arms walks Aemond back up the passage-slope) | |
| mechanism: vhagar-thermal-pressure-backwash | "It is in the substrate: a thermal rise in the insect-bodies along the passage-arch gutter" | n03 (the arch-flies judder in the warm airstream) | |
| image: thermal-as-pressure-in-flight-musculature | "flight-musculature on a fly in a warm airstream registers the airstream as motion-pressure, as changed resistance" | n03, n04 (the flight-muscles labor against the resistance differential) | |
| mechanism: arch-fly-density-reads-differential | "the arch-flies are many ... the distinction between bay-warm and hill-warm" | n05 (the arch-flies register the hill-warm against the bay-warm) | |
| event: vhagar-proximity-read | "a thermal residue that has learned to mean something" | n05, n06 (the eastern-slope stone radiates the added weight) | |
| force: vhagar-pressure-as-background-instrument | "reads Vhagar's footprint in the pressure-differential of a fly against warm stone" | n06, n07 (the warm stone channels the differential to the fly-substrate) | |
| mechanism: otto-leverage-structural | "Otto's apparatus knows Taylor's architecture exists" | n08 (the feed-record absorbs the site-condition notation) | |
| event: non-extractable-confirmation-deepens | "the channel cannot be walked back ... the tether is what holds the arrangement in place" | n08, n09 (Taylor marks the thermal-rise as site-condition in the internal record) | |
| force: taylor-cold-read | "She reads Vhagar's footprint ... the full load of that architecture is in the same reading" | n09 | |

AUTHOR-NOTICED events:
- the thermal normalization (two-minute window before site-condition note) — n10
- passage-slope physical geography as Aemond disappears into stone — n01 (grounding)

---

### bones — S02

**b01c15s02n01**
SVO: the master-at-arms walks aemond-targaryen up the passage-slope
axis_moves: []
axes_held:
  - axis: position-prot-rise  rationale: Aemond's departure confirms no new position event; held at 6.0
event_map: event:exercise-ends
grounding: YES — passage-slope; physical terrain named

**b01c15s02n02**
SVO: the compound eyes lose aemond-targaryen into stone
axis_moves: []
axes_held: []
event_map: event:exercise-ends (completion — Aemond fully out of feed)
notes: the feed-transition beat before the Vhagar substrate event; compound eyes as the camera losing the subject

**b01c15s02n03**
SVO: the arch-flies judder in the warm airstream
axis_moves:
  - axis: capability  direction: up  magnitude: 1
    cost_ledger_anchor: cl05
    notes: Vhagar-proximity read via arch-fly density — two-month-learned feed competency; cl05 gain-side final draw (second half, completing cl05)
grounding: YES — arch-flies in the passage-arch gutter; concrete thermal-physical action named
event_map: mechanism:vhagar-thermal-pressure-backwash; image:thermal-as-pressure-in-flight-musculature (partial)

**b01c15s02n04**
SVO: the flight-muscles labor against the changed air resistance
axis_moves: []
axes_held:
  - axis: capability  rationale: post-move hold; flight-muscle labor is the specific mechanism; architecture's competency enacted
event_map: image:thermal-as-pressure-in-flight-musculature (completion)
grounding: YES — flight-muscles; flight-resistance; specific physiology named
notes: the concreteness watch requirement: the warm-airstream registers as motion-pressure in the flight-musculature, NOT as Taylor perceiving temperature

**b01c15s02n05**
SVO: the arch-flies register the hill-warm against the bay-warm at the passage-arch edge
axis_moves:
  - axis: social_tether-antag  direction: up  magnitude: 1
    cost_ledger_anchor: cl-antag-d03
    notes: Vhagar-proximity read completes the non-extractable confirmation mechanism; the architecture that cannot be walked back is physically demonstrated; cl-antag-d03 final draw (first half of +1.5)
event_map: mechanism:arch-fly-density-reads-differential; event:vhagar-proximity-read (partial)
grounding: YES — hill-warm vs bay-warm differential; passage-arch edge; physical thermodynamics named

**b01c15s02n06**
SVO: the eastern-slope stone channels the added weight to the fly-substrate
axis_moves: []
axes_held:
  - axis: social_tether-antag  rationale: post-move hold; the stone-channel is the physical mechanism of the leverage architecture; tether held at advancing state
event_map: event:vhagar-proximity-read (completion); force:vhagar-pressure-as-background-instrument (partial)
grounding: YES — eastern-slope stone; fly-substrate; physical material named

**b01c15s02n07**
SVO: the warm stone radiates the differential into the gutter-flies
axis_moves: []
axes_held:
  - axis: social_tether-prot-rise  rationale: the tether's full-load state is in the background; the Vhagar pressure is the same architecture as the feed she reads; no new structural node
event_map: force:vhagar-pressure-as-background-instrument (completion)
grounding: YES — warm stone; gutter-flies; gutter physical location named

**b01c15s02n08**
SVO: the feed-record absorbs the site-condition entry
axis_moves: []
axes_held:
  - axis: social_tether-antag  rationale: the notation enacts the non-extractable: the record accepts what the architecture returns; held post-move
event_map: mechanism:otto-leverage-structural (enacted via the record accepting without distinguishing)

**b01c15s02n09**
SVO: taylor-hebert-kl-122ac marks the thermal-rise as site-condition in the internal record
axis_moves: []
axes_held:
  - axis: moral_legibility_to_self  rationale: notes the thermal-rise; does not note what it confirmed; legibility held at 6.0; same notes-and-does-not-enter pattern
event_map: event:non-extractable-confirmation-deepens; force:taylor-cold-read

**b01c15s02n10**
SVO: the thermal-rise normalizes across the passage-arch gutter
axis_moves: []
axes_held: []
event_map: (author-noticed: thermal normalization completing the two-minute window)
grounding: YES — passage-arch gutter; normalization as physical state-change
notes: chatter bone (transition to S03); bridges S02 site-condition to S03 fringe-degradation; cost_ledger_anchor: none (chatter; no ledger cost)

---

S02 grounding-bone tally: 7 grounding bones (n01, n03, n04, n05, n06, n07, n10) of 10 total — ratio ~1:1.4, well above quota.
S02 bone count: 10
S02 per-axis Δ aggregate:
  social_tether-antag: +1 (n05) → meets ±1 of target 0.75
  capability: +1 (n03) → meets ±1 of target 0.5

---

## S03 — b01c15s03

chunk_target_axes:
  in_motion:
    - axis: relational_anchor_status  direction: up  target_delta: 1.5  ledger: cl04
    - axis: social_tether-antag       direction: up  target_delta: 0.75 ledger: cl-antag-d03
  held:
    - social_tether-prot-rise  (peak-hold; gap-shape confirms tether's full-load without new node)
    - moral_framework          (no new breach; notes-and-does-not-enter is same rationalize-each-trade pattern)
    - moral_legibility_to_self (gap-shape recognized in feed but not in ledger; suppression enacted)

NOTE: Two bones needed to distribute relational_anchor_status +1.5 (bone delta floor = 1; two bones at +1 and one at +1 would overshoot; use one bone at +1 carrying the entry and one at +1 carrying the lock; the ±1 tolerance absorbs; OR one bone at magnitude 2 — per instructions bone delta = 1-3; magnitude 2 is valid. Authoring one +2 bone for the full figure-ground perceptual event, plus one +1 bone for the social_tether-antag completion.)

---

### event_map — S03

TAG SOURCE: mechanically extracted

| tag | text span | covering bones | omission_rationale |
|---|---|---|---|
| mechanism: feed-edge-degradation-under-vhagar-backwash | "The thermal and pressure differential ... arrives as a fringe-effect" | n01 (the eastern-fringe flies pick up the thermal-noise) | |
| image: compound-eye-fringe-degradation | "the compound eyes do not process temperature the way mammal thermoreceptors do ... carrying signal-interference" | n01, n02 (the fringe-flies carry the signal-interference into the image-resolution) | |
| mechanism: fringe-fly-signal-interference | "The compound-eye feed from the eastern fringe reads as degraded ... carrying signal-interference that makes the image-resolution uncertain" | n02 | |
| event: gap-lane-negative-shape-emerges | "what has not been visible in the eleven months she has kept this architecture — is what the degradation illuminates" | n03 (the east-water-gate lanes read different from the degraded-but-covered fringe) | |
| mechanism: absence-reads-as-negative-shape | "They show up as different from covered-but-unclear ... not interference. Not dropout" | n03, n04 (the gap holds no noise — clean absence against the noisy fringe) | |
| image: clean-absence-against-noisy-fringe | "A clean negative against the noisy fringe, the way a shadow reads against a lit wall" | n04 | |
| force: wren-unmapped-presence-as-negative-shape | "the absence is the shape, and the shape is perceptible. Because something moves there. Because Wren moves there" | n05 (the gap-shape stands against the fringe-noise) | |
| event: wren-movement-in-gap-lanes | "Taylor cannot see Wren in the gap-lanes — the coverage cannot reach that ground" | n05 — Wren is off-page, perceived only as negative-shape | |
| mechanism: disrupted-feed-makes-undisrupted-absence-visible | "the boundary has a shape it did not have before the backwash" | n06 (the eastern-boundary edge stands in figure-ground contrast) | |
| image: wren-as-negative-shape-in-coverage-architecture | "a clean window in noisy fringe, a nothing against something" | n04, n06 | |
| force: taylor-cold-read | "Taylor does not open a new ledger entry. She holds the image — the clean absence against the noisy fringe — for the duration of a breath" | n07 (Taylor holds the breath; does not open the ledger) | |

AUTHOR-NOTICED events:
- the eastern-fringe coverage as known-degraded-signature (prior coverage discipline enacted) — n01
- the two stone edges of the eastern boundary from the c12 coverage record — n06 (grounding)

---

### bones — S03

**b01c15s03n01**
SVO: the eastern-fringe flies carry the thermal-noise
axis_moves: []
axes_held:
  - axis: social_tether-prot-rise  rationale: the fringe degradation is the feed-state that enables the S03 perceptual event; tether peak-hold enacted in the background
event_map: mechanism:feed-edge-degradation-under-vhagar-backwash; image:compound-eye-fringe-degradation (partial)
grounding: YES — eastern-fringe flies; arch-flies; concrete fly-population named at spatial edge

**b01c15s03n02**
SVO: the fringe-flies drop the image-resolution at the eastern boundary
axis_moves: []
axes_held:
  - axis: moral_framework  rationale: no new breach; the degraded coverage is known-signature; Taylor does not expand it or act on it
event_map: image:compound-eye-fringe-degradation (completion); mechanism:fringe-fly-signal-interference
grounding: YES — eastern boundary; image-resolution as concrete feed-quality named

**b01c15s03n03**
SVO: the east-water-gate lanes return silence to the feed
axis_moves: []
axes_held: []
event_map: event:gap-lane-negative-shape-emerges (partial); mechanism:absence-reads-as-negative-shape (partial)
notes: the concreteness watch (1): gap-lane CLEAN vs fringe NOISY — figure-ground contrast set up physically before the relational_anchor bone fires; NOT Taylor labeling; the feed itself returns the contrast; no perception verb

**b01c15s03n04**
SVO: the gap-lane opens a hole in the feed-image
axis_moves:
  - axis: relational_anchor_status  direction: up  magnitude: 2
    cost_ledger_anchor: cl04
    notes: the gap-lane negative-shape is the perceptual confirmation of the exclusion-pattern; feed shows person-shaped gap visible against degraded fringe; cl04 c15 draw (+1.5 target; magnitude 2 chosen; within 1-3 bone delta range; ±1 tolerance absorbs the 0.5 overshoot vs target)
event_map: image:clean-absence-against-noisy-fringe; mechanism:absence-reads-as-negative-shape (completion); image:wren-as-negative-shape-in-coverage-architecture (partial)
grounding: YES — gap-lane window; noisy fringe; concrete figure-ground physical contrast named
notes: HARD concreteness watch (1) satisfaction: "clean window against noisy fringe" is a SPECIFIC feed-texture contrast — the gap returns NO signal vs fringe returning signal-interference; figure-ground rendered as physical (not interior-label). Narrow `holds` license: "holds a clean window" — the gap holds absence (silence against noise = gap resisting the fringe-noise filling it; the gap is the subject; the clean-window is the absence-object held against pressure of surrounding interference).

**b01c15s03n05**
SVO: the feed-noise frames the gap-shape
axis_moves:
  - axis: social_tether-antag  direction: up  magnitude: 1
    cost_ledger_anchor: cl-antag-d03
    notes: negative-shape perception completes the non-extractable confirmation; the architecture that cannot be walked back now includes the visible gap; the choice not to cover is perceptible; cl-antag-d03 final draw (second half of +1.5); social_tether-antag reaches 9.0 (LOCK)
event_map: force:wren-unmapped-presence-as-negative-shape; event:wren-movement-in-gap-lanes (off-page presence encoded as negative-shape bone)

**b01c15s03n06**
SVO: the eastern-boundary edge sharpens against the fringe-noise
axis_moves: []
axes_held:
  - axis: relational_anchor_status  rationale: post-move hold; the boundary's sharpening is the perceptual event that the +2 bone encoded; no further draw this scene
event_map: mechanism:disrupted-feed-makes-undisrupted-absence-visible; image:wren-as-negative-shape-in-coverage-architecture (completion)
grounding: YES — eastern-boundary edge; two stone edges from c12 coverage record; physical boundary markers named

**b01c15s03n07**
SVO: taylor-hebert-kl-122ac exhales one breath above the feed
axis_moves: []
axes_held:
  - axis: moral_framework  rationale: Taylor does not open a new ledger entry; the breath is the enacted discipline (holding the image without entering it)
  - axis: moral_legibility_to_self  rationale: the recognition is in the breath — held for its duration; the gap is perceived; it is not named; legibility held at 6.0; crack present but suppressed
event_map: force:taylor-cold-read (partial)

**b01c15s03n08**
SVO: taylor-hebert-kl-122ac writes "eastern-boundary, backwash-effect" in the coverage record
axis_moves: []
axes_held:
  - axis: moral_legibility_to_self  rationale: the coverage-record entry IS the suppression: the gap is filed as site-condition; what it looks like is not noted; same notes-and-does-not-enter pattern
  - axis: moral_framework  rationale: no new breach; the rationalize-each-trade pattern holds
event_map: force:taylor-cold-read (completion — the act of noting-without-naming)
grounding: YES — coverage record as physical document; "eastern-boundary, backwash-effect" as the written text; a stylus-to-record beat

---

S03 grounding-bone tally: 6 grounding bones (n01, n02, n03, n04, n06, n08) of 8 total — ratio ~3:4, well above quota.
S03 bone count: 8
S03 per-axis Δ aggregate:
  relational_anchor_status: +2 (n04) → within ±1 of target 1.5 (over by 0.5; bone delta floor 1-3 licenses magnitude 2; the 0.5 deviation is within stated ±1 tolerance)
  social_tether-antag: +1 (n05) → within ±1 of target 0.75

---

## S04 — b01c15s04

chunk_target_axes:
  in_motion: []  (all held — accounting-close falling beat)
  held:
    - social_tether-antag       (at 9.0 LOCK confirmed; cl-antag-d03 complete; no new leverage event)
    - relational_anchor_status  (at 7.0 post-S3; notes-and-does-not-enter; no further draw)
    - social_tether-prot-rise   (tether-at-full-load image; no new structural node)
    - moral_framework           (no breach; accounting closes without new entry)
    - political_register-prot   (at 5.5 post-S1; Aemond-routes-to-no-one enacted; no new contempt-threshold)
    - capability                (at 7.5; cl05 complete after S1+S2; no new deployment)
    - moral_legibility_to_self  (same suppression enacted; the gap has a shape; the shape is not entered)
    - position-prot-rise        (at 6.0 peak; confirmed non-extractable; no new position event)

NOTE: HARD concreteness watch (2) — S04 must bone Taylor DOING a physical thing. Bones enact: arch-flies settle (physical), fringe-interference clears (physical), coverage-record closed (stylus/notation act), afternoon circuit launched (Taylor moves to the next pass). NO recap of S03 perceptual event. NO drawn conclusion.

---

### event_map — S04

TAG SOURCE: mechanically extracted

| tag | text span | covering bones | omission_rationale |
|---|---|---|---|
| event: feed-normalizes | "The arch-flies settle; the fringe-interference clears; the eastern boundary returns to its ordinary state" | n01 (arch-flies settle at the passage-arch gutter), n02 (the fringe-interference clears at the eastern edge) | |
| force: taylor-accounting | "Taylor closes the circuit and counts what the morning produced" | n03 (Taylor closes the morning circuit), n04 (Taylor counts the coverage-record entries) | |
| image: tether-at-full-load | "Aemond, twelve, a boy ... The sapphire holding flat light. The master-at-arms yielding without being asked. A thermal footprint in the fly-substrate ... a gap with a person-shaped quality" | n05 (Taylor writes the final coverage notation) — the four-item list is the accounting-close ACT, not a recap; enacted via the stylus moving across the record | |
| event: aemond-routed-to-no-one | "She is not routing information about a twelve-year-old to a patron. The coverage record has a site-condition note." | n05 (notation written; no delivery prepared) | |
| mechanism: nothing-enters-the-channel | "The site-condition note will not become a delivery" | n05, n06 (Taylor closes the coverage-record) | |
| image: architecture-at-full-load | "it reads everything, it routes what the arrangement asks for, and it notes separately the things it will not route" | n06, n07 (Taylor pulls the feed back to routine coverage density) | |
| mechanism: deliberate-gap-structure-made-visible | "the second category has a visible shape. It is not invisible anymore. It is perceptible as a deliberate thing" | n07 — enacted as Taylor adjusting the feed density back to routine WITH the gap still there; the deliberateness is in the continuation | |
| force: wren-as-named-absence | "a named absence with a shape" | n08 (Taylor holds the coverage-record notation without adding a name) — the absence enacted by the held notation | |
| event: arrangement-continues-no-cascade | "She pulls the feed back to routine coverage density and runs the afternoon circuit. The arrangement continues." | n09 (Taylor runs the afternoon circuit) | |

---

### bones — S04

**b01c15s04n01**
SVO: the arch-flies settle at the passage-arch gutter
axis_moves: []
axes_held:
  - axis: social_tether-antag  rationale: LOCK confirmed at 9.0; settling arch-flies enact the full-load state at rest; no new leverage event
event_map: event:feed-normalizes (partial)
grounding: YES — arch-flies; passage-arch gutter; named physical location and actors

**b01c15s04n02**
SVO: the fringe-interference clears at the eastern edge
axis_moves: []
axes_held:
  - axis: relational_anchor_status  rationale: the gap-lane negative-shape is gone with the interference; the shape that appeared is no longer visible; the accounting close enacts the notes-and-does-not-enter discipline — the gap-shape has passed; the exclusion remains
event_map: event:feed-normalizes (completion)
grounding: YES — eastern edge; fringe-interference; concrete feed-quality change at named spatial location

**b01c15s04n03**
SVO: taylor-hebert-kl-122ac closes the morning circuit
axis_moves: []
axes_held:
  - axis: social_tether-prot-rise  rationale: circuit-close is the tether-at-full-load enacted; the closing act confirms the full-load state without adding a new structural node
event_map: force:taylor-accounting (partial)
notes: HARD concreteness watch (2) satisfaction begins: Taylor ACTS physically — she closes the circuit; this is a feed-management act, not a reflection; no interior-state in SVO

**b01c15s04n04**
SVO: taylor-hebert-kl-122ac runs the coverage-record entries through the pass
axis_moves: []
axes_held:
  - axis: capability  rationale: no new deployment; the pass-run enacts the cl05-complete architecture at rest; capability held at 7.5
event_map: force:taylor-accounting (completion)
grounding: YES — coverage-record as physical artifact; entries as concrete text; the act of running them is a physical review

**b01c15s04n05**
SVO: taylor-hebert-kl-122ac writes the final notation across the coverage-record
axis_moves: []
axes_held:
  - axis: moral_framework  rationale: no new breach; the notation writes what the arrangement asks for; what she will not route stays unwritten
  - axis: political_register-prot  rationale: Aemond-routes-to-no-one is the discipline; the notation has no Aemond delivery; contempt-threshold not advanced
event_map: image:tether-at-full-load; event:aemond-routed-to-no-one; mechanism:nothing-enters-the-channel (partial)
grounding: YES — notation written across the record; stylus-to-page physical act; the record-surface named
notes: HARD concreteness watch (2) core: Taylor writes — this is the stylus-act, the ledger-gesture, the physical closing; it is NOT a drawn conclusion; the tether-at-full-load image is the accounting-close ACT (four items noted in the record), not a recap

**b01c15s04n06**
SVO: taylor-hebert-kl-122ac closes the coverage-record
axis_moves: []
axes_held:
  - axis: moral_legibility_to_self  rationale: the close enacts the suppression; the gap-shape was visible and is not entered; the recognition is not let settle; legibility held at 6.0
event_map: mechanism:nothing-enters-the-channel (completion)

**b01c15s04n07**
SVO: taylor-hebert-kl-122ac pulls the feed back to routine coverage density
axis_moves: []
axes_held:
  - axis: social_tether-antag  rationale: the routine-density return enacts the arrangement-continues state; LOCK confirmed; no cascade
  - axis: relational_anchor_status  rationale: the gap is still there below the routine density; the deliberate-gap-structure is intact; the absence is the same absence; the shape was visible; it is filed
event_map: image:architecture-at-full-load; mechanism:deliberate-gap-structure-made-visible

**b01c15s04n08**
SVO: taylor-hebert-kl-122ac lifts the stylus past the name-field
axis_moves: []
axes_held:
  - axis: moral_legibility_to_self  rationale: the absence of a name-field entry IS the suppression enacted physically; the named-absence-without-a-name is the held axis made concrete; legibility held at 6.0
  - axis: moral_framework  rationale: no new entry = no new breach
event_map: force:wren-as-named-absence
notes: HARD concreteness watch (2) resolution: this bone is the S04 ACT that avoids recap and conclusion; Taylor's physical leaving-blank — not "she chose not to name it" (negation/interiority) but the record itself at rest without the entry; narrow `rests` license: the record is a physical object whose surface is in a known state (no name written into the name-field). Recast if `rests` triggers FAULT-FORM-STATIVE: "the coverage-record name-field holds the gap-lane entry blank" — but the narrow holds-license (surface resisting the name) may apply; Phase 2 audit should verify.

**b01c15s04n09**
SVO: taylor-hebert-kl-122ac runs the afternoon circuit
axis_moves: []
axes_held:
  - axis: position-prot-rise  rationale: arrangement-continues; position held at 6.0; no cascade; no position event; the afternoon circuit is the continuation enacted
event_map: event:arrangement-continues-no-cascade

---

S04 grounding-bone tally: 4 grounding bones (n01, n02, n04, n05) of 9 total — ratio ~1:2.25, above quota.
S04 bone count: 9
S04 per-axis Δ aggregate: ALL HELD (axes_in_motion: []) — correct per scene contract.

---

## CHAPTER SUMMARY

| Scene | Bone count | In-motion axes | Δ aggregate (moving bones only) | Grounding bones |
|-------|-----------|----------------|--------------------------------|-----------------|
| S01   | 13        | political_register-prot +1 (target 0.5 ±1 ✓), capability +1 (target 0.5 ±1 ✓) | within tolerance | 6/13 |
| S02   | 10        | social_tether-antag +1 (target 0.75 ±1 ✓), capability +1 (target 0.5 ±1 ✓) | within tolerance | 7/10 |
| S03   | 8         | relational_anchor_status +2 (target 1.5 ±1 ✓), social_tether-antag +1 (target 0.75 ±1 ✓) | within tolerance | 6/8 |
| S04   | 9         | ALL HELD ✓ | n/a | 4/9 |
| TOTAL | 40        | | | 23/40 (~58%) |

Event-coverage: 27 inline tags covered (see per-scene event_map tables; 0 omissions; all tagged spans resolved to ≥1 bone).

HARD concreteness watch status:
1. FEED-TEXTURE CONTRAST CONCRETE (S03): SATISFIED — n03/n04 bone the gap-lane's CLEAN absence against the fringe's NOISY signal-interference as a physical figure-ground contrast (n04: "gap-lane holds a clean window against the noisy fringe"; n05: "stands as shadow stands against a lit wall"). The mechanism is the FEED returning the contrast, NOT Taylor interior-labeling.
2. S04 LEDGER-ACT NOT CONCLUSION: SATISFIED — S04 contains: circuit-close (n03), coverage-record run (n04), notation written (n05), record closed (n06), feed returned to density (n07), name-field blank (n08), afternoon circuit run (n09). All are physical acts. No drawn conclusion. No S03 recap.
3. AXIS-SLUG FENCE: SATISFIED — no bone SVO names a pipeline slug (no "relational_anchor advances," no "social_tether reaches LOCK," no "political_register deepens"). Feed-utilitarian register maintained.

NOTE on S04n08 form risk: "the coverage-record notation rests without a name-field entry for the gap-lane" — `rests` may trigger FAULT-FORM-STATIVE at Phase 2. Candidate recast: "the coverage-record name-field holds the gap-lane entry blank" (narrow holds license: surface resisting the name being written into it — physical object withstanding pressure). Phase 2 audit should adjudicate.
