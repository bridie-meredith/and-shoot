## SESSION-START — 2026-05-25T00:00:00Z — fault-001-b01c01s03
dispatch: partial-settlement notation fix for cl01b in b01c01s03 social_tether-prot-rise notes
target: active-project/staff/showrunner/b01c01-draft.md
audit-report: active-project/staff/reviews/b01c01-scenes-audit-2026-05-25.md
findings-queued: 1

## fault-001 — RESOLVED — 2026-05-25T00:00:00Z
fault: s03 notes claimed full settlement of cl01b (+1 delivered) with no partial-delivery qualification; ledger declares gain +2; one rank unanchored
scope: line
change: (1) b01c01s03 axes_in_motion[social_tether-prot-rise].notes rewritten to declare partial-settlement (+1 of +2, ward-layer half — Oswyn), name b01c03 as downstream anchor for remaining +1, and include DOWNSTREAM-WATCH flag that b01c03 chapter contract does not yet reflect cl01b in axes_in_motion; (2) authoring notes cl01b refinement block updated from single-scene anchor to split-anchor notation [b01c01s03, b01c03] with note that b01c03 anchor entry is to be added at next /and-substance chapter b01c03 run
criteria met: yes — scene notes now explicitly declare partial settlement, name the downstream anchor chapter, and flag the b01c03 contract gap; no target_delta_magnitude changed; no cost ledger changed; no chapter contract changed

## SESSION-END — 2026-05-25T00:00:00Z — fault-001-b01c01s03
findings-applied: 1
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T01:00:00Z — write-b01c01-pass2-svo-recasts
dispatch: minimum-change SVO recasts for 15 FAULT-FORM faults from write-b01c01-pass2 audit; patch svo: fields only in b01c01-bones-draft-pass1.md
target: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
audit-report: active-project/staff/auditor/write-b01c01-pass2.md
findings-queued: 15

## /and-write b01c01 Phase 2 — 2026-05-25

- bone: b01c01s01n01
  before: "the drain water threads under the angle"
  after: "the drain water threads the angle-gap"
  fault_class: FAULT-FORM-MODIFIER
  rationale: 'threads' carries transitive sense taking 'the angle-gap' as direct object, eliminating the banned prepositional phrase 'under the angle' while preserving the drain-water threading motion; no adverb, no preposition, no new deny-list verb introduced.

- bone: b01c01s01n02
  before: "the tallow smoke drifts from the stitch-house"
  after: "the tallow smoke crosses the stitch-house lane"
  fault_class: FAULT-FORM-MODIFIER
  rationale: eliminates banned source-preposition 'from the stitch-house' by recasting to transitive 'crosses' with 'the stitch-house lane' as direct object — the stitch-house remains a named concrete entity in the bone, preserving the pl-002 SOFT anchor; no new fault introduced.

- bone: b01c01s01n04
  before: "the insects propagate at the edge of range"
  after: "the insects propagate"
  fault_class: FAULT-FORM-MODIFIER
  rationale: strips the banned place-prepositional phrase 'at the edge of range'; bare intransitive 'propagate' is a physical-process verb that lands cleanly without implying a stated destination, exactly as the intransitive-lands-cleanly exception permits; range-threshold context is facet material.

- bone: b01c01s01n05
  before: "taylor lifts the eyes"
  after: [DROPPED]
  fault_class: FAULT-FORM-PERCEPTION
  rationale: no honest non-perception recast available in a solo scene — eye-lifting is the mechanism of the scanning/observational act the event_map names; dropping the bone removes the perception-surrogate; the bone count for s01 drops from 7 to 6 (within the 5-15 schema range); political_register-prot held rationale relocated to s01n07 as a third axes_held entry with a note marking the relocation source.

- bone: b01c01s01n06
  before: "the cobbles press the angle-wall"
  after: "the angle-wall narrows the lane"
  fault_class: FAULT-FORM-INTERIORITY
  rationale: recasts the interiority-as-environment-action (stative cobbles-pressing-wall geometry-figure) to a concrete transitive geometry-action — 'narrows' describes a physical dimensional fact as a discrete verb, subject is the wall, object is the lane; no place-preposition, no abstraction-as-object; social_tether-prot-rise held rationale (anonymity enacted by physical geometry) survives unchanged at the axes_held layer.

- bone: b01c01s02n01
  before: "the fish-cart blocks the lane crosswise"
  after: "the fish-cart blocks the lane"
  fault_class: FAULT-FORM-MODIFIER
  rationale: drops the banned adverb 'crosswise'; 'the lane' remains as direct object; crosswise geometry is implied by a cart blocking a lane and can be carried in loc-state facet; no new fault introduced.

- bone: b01c01s02n02
  before: "the ground carries the child's breath"
  after: "the ground transmits the child's breath"
  fault_class: FAULT-FORM-NON-ACTION-VERB
  rationale: replaces banned verb 'carries' (sustained-carrying deny-list) with 'transmits' — a discrete directional action not on any deny list; subject, object, and physical-fact semantic are preserved; 'the child's breath' as object remains borderline (breath transmitted through ground is a sensory-physical fact, not an abstraction) and is not separately faulted.

- bone: b01c01s02n06
  before: "the insects propagate inward"
  after: "the insects propagate"
  fault_class: FAULT-FORM-MODIFIER
  rationale: strips the banned directional adverb 'inward'; bare intransitive 'propagate' is a physical-process verb landing cleanly without destination; the deployment semantics are preserved because 'propagate' records the spread event — the direction (into the crowd) is scene context, not needed in the bone; substance_delta (capability +1, cl01a) transfers unchanged; HIGH PRIORITY bone confirmed clean.

- bone: b01c01s02n08
  before: "the gap propagates outward"
  after: "the gap propagates"
  fault_class: FAULT-FORM-MODIFIER
  rationale: strips the banned directional adverb 'outward'; same bare-intransitive logic as s02n06 — 'propagate' is a physical-process verb that lands cleanly; no destination implied, no new fault introduced.

- bone: b01c01s02n11
  before: "taylor gives the instruction"
  after: "taylor raises the voice"
  fault_class: FAULT-FORM-INTERIORITY
  rationale: replaces abstraction-as-object 'the instruction' with a physical vocal-act recast — 'raises' is transitive and not on any deny list; 'the voice' is the physical sound-production output, not an abstract communication-content object; moral_legibility_to_self held rationale ("voice-of-instruction is the deployment's final act") survives because the physical vocal act is still the deployment's closing gesture; auditor's 'projects the voice' is equally valid — 'raises' chosen to avoid the 'lifts/raises/projects' verb-pattern mannerism already noted in decomposer_notes.

- bone: b01c01s03n02
  before: "the man with the fish-cart watches taylor"
  after: "the fish-cart man faces taylor"
  fault_class: FAULT-FORM-PERCEPTION
  rationale: replaces banned perception verb 'watches' with 'faces' — licensed as a discrete transitive posture-act (confirmed CORRECT at s02n09 and s03n07 in the audit); subject recasts from 'the man with the fish-cart' (prepositional disambiguator) to 'the fish-cart man' (compound-noun unnamed-entity, cleaner per unnamed-entity convention); auditor's hint 'the fish-cart holder turns toward taylor' was rejected because 'turns toward' reintroduces a prepositional phrase.

- bone: b01c01s03n03
  before: "the two women from the upper alley stay"
  after: "the two women face the lane"
  fault_class: FAULT-FORM-NON-ACTION-VERB
  rationale: replaces banned stative verb 'stay' with 'face' — licensed transitive posture-act; 'the lane' as direct object; holders-remaining semantic preserved as a body-direction toward the scene rather than a stative naming of position; subject-disambiguator 'from the upper alley' dropped per cleaner unnamed-entity form (auditor declined to fault subject-disambiguating tags, but the recast body-direction already identifies their orientation, making the disambiguator redundant); 'the two women' treated as collective-singular unnamed-entity, same pattern as 'the crowd'.

- bone: b01c01s03n04
  before: "oswyn-mudway-flea-bottom-elder stands at the lane-mouth"
  after: "oswyn-mudway-flea-bottom-elder takes the lane-mouth"
  fault_class: FAULT-FORM-NON-ACTION-VERB + FAULT-FORM-MODIFIER
  rationale: replaces both faults in one recast — 'takes' is transitive and discrete (not stative position-naming), 'the lane-mouth' becomes a direct object (no prepositional phrase of place); the deliberate-positioning semantic (Oswyn arriving at the lane-mouth and claiming the position) is preserved; substance_delta (social_tether-prot-rise +1, cl01b) transfers unchanged; HIGH PRIORITY bone confirmed clean.

- bone: b01c01s03n05
  before: "the child departs"
  after: "the child clears the lane"
  fault_class: FAULT-FORM-NO-VERB
  rationale: adds 'the lane' as direct object to the bare intransitive motion verb, resolving the FAULT-FORM-NO-VERB — 'clears' is transitive, implies departure and freeing of the space without stating where the child goes; slightly more concrete than 'leaves the lane' because it records the physical result (lane cleared) rather than just the departure direction.

- bone: b01c01s03n08
  before: "the tallow smoke settles at the lane-level"
  after: "the tallow smoke layers the lane-floor"
  fault_class: FAULT-FORM-MODIFIER
  rationale: replaces banned place-prepositional phrase 'at the lane-level' with transitive 'layers' taking 'the lane-floor' as direct object — a concrete physical noun, not a prepositional phrase; the stitch-house smoke as a continuing lane-level physical fact is preserved (the settling-at-floor-level semantic is carried by 'layers the lane-floor'); pl-002 SOFT load-bearing continuity maintained; auditor's 'settles the lane' alternative rejected as causative-odd ('settles' transitive reads as causing the lane to settle).

---

Summary:
- Bones patched: 14 (s01n01, s01n02, s01n04, s01n06, s02n01, s02n02, s02n06, s02n08, s02n11, s03n02, s03n03, s03n04, s03n05, s03n08)
- Bones dropped: 1 (s01n05 — FAULT-FORM-PERCEPTION; perception-surrogate in solo scene; no honest non-perception recast available)
- Held-axis rationale relocation: political_register-prot rationale from s01n05 relocated to s01n07 as a third axes_held entry
- Note: 9 of the 15 faults were already applied in the draft before this session; 6 faults required patching in this session (s02n08, s02n11, s03n02, s03n03, s03n04, s03n05, s03n08 — 7 patches, all 6 remaining faults plus s03n08 which was also not yet applied)

## b01c01s01n01 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'under the angle' prepositional phrase of place/direction (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the drain water threads under the angle" to "the drain water threads the angle-gap"
criteria met: yes

## b01c01s01n02 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'from the stitch-house' prepositional phrase of source (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the tallow smoke drifts from the stitch-house" to "the tallow smoke crosses the stitch-house lane"; stitch-house named entity preserved
criteria met: yes

## b01c01s01n04 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'at the edge of range' prepositional phrase of place (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the insects propagate at the edge of range" to "the insects propagate"
criteria met: yes

## b01c01s01n05 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'lifts the eyes' perception-surrogate in solo scene (FAULT-FORM-PERCEPTION)
scope: line
change: bone dropped; political_register-prot held rationale relocated to s01n07 as third axes_held entry; s01 bone count drops from 7 to 6 (within 5-15 range)
criteria met: yes

## b01c01s01n06 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'the cobbles press the angle-wall' is interiority dressed as environment-action; stative geometry figure (FAULT-FORM-INTERIORITY)
scope: line
change: svo recast from "the cobbles press the angle-wall" to "the angle-wall narrows the lane"; social_tether-prot-rise held rationale unchanged
criteria met: yes

## b01c01s02n01 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'crosswise' adverb of manner (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the fish-cart blocks the lane crosswise" to "the fish-cart blocks the lane"
criteria met: yes

## b01c01s02n02 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'carries' is on the sustained-carrying deny list (FAULT-FORM-NON-ACTION-VERB)
scope: line
change: svo recast from "the ground carries the child's breath" to "the ground transmits the child's breath"
criteria met: yes

## b01c01s02n06 — RESOLVED — 2026-05-25T01:30:00Z
fault: 'inward' directional adverb (FAULT-FORM-MODIFIER); HIGH PRIORITY moving bone
scope: line
change: svo recast from "the insects propagate inward" to "the insects propagate"; substance_delta (capability +1, cl01a) unchanged
criteria met: yes

## b01c01s02n08 — RESOLVED — 2026-05-25T01:32:00Z
fault: 'outward' directional adverb (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the gap propagates outward" to "the gap propagates"
criteria met: yes

## b01c01s02n11 — RESOLVED — 2026-05-25T01:33:00Z
fault: 'the instruction' is abstraction-as-object (FAULT-FORM-INTERIORITY)
scope: line
change: svo recast from "taylor gives the instruction" to "taylor raises the voice"; physical vocal-act semantic preserved; moral_legibility_to_self rationale unchanged
criteria met: yes

## b01c01s03n02 — RESOLVED — 2026-05-25T01:34:00Z
fault: 'watches' is on the perception-verb deny list (FAULT-FORM-PERCEPTION)
scope: line
change: svo recast from "the man with the fish-cart watches taylor" to "the fish-cart man faces taylor"; 'faces' licensed as transitive posture-act; subject compound-noun form cleans the disambiguating prepositional tag
criteria met: yes

## b01c01s03n03 — RESOLVED — 2026-05-25T01:35:00Z
fault: 'stay' is stative position-naming (FAULT-FORM-NON-ACTION-VERB)
scope: line
change: svo recast from "the two women from the upper alley stay" to "the two women face the lane"; holders-remaining semantic preserved as body-direction
criteria met: yes

## b01c01s03n04 — RESOLVED — 2026-05-25T01:36:00Z
fault: 'stands' stative position-naming + 'at the lane-mouth' prepositional phrase of place (FAULT-FORM-NON-ACTION-VERB + FAULT-FORM-MODIFIER); HIGH PRIORITY moving bone
scope: line
change: svo recast from "oswyn-mudway-flea-bottom-elder stands at the lane-mouth" to "oswyn-mudway-flea-bottom-elder takes the lane-mouth"; substance_delta (social_tether-prot-rise +1, cl01b) unchanged
criteria met: yes

## b01c01s03n05 — RESOLVED — 2026-05-25T01:37:00Z
fault: 'departs' is bare intransitive motion verb without destination (FAULT-FORM-NO-VERB)
scope: line
change: svo recast from "the child departs" to "the child clears the lane"; direct object added
criteria met: yes

## b01c01s03n08 — RESOLVED — 2026-05-25T01:38:00Z
fault: 'at the lane-level' prepositional phrase of place (FAULT-FORM-MODIFIER); load-bearing for pl-002 SOFT
scope: line
change: svo recast from "the tallow smoke settles at the lane-level" to "the tallow smoke layers the lane-floor"; stitch-house continuity preserved; 'settles the lane' alternative rejected as causative-odd
criteria met: yes

## SESSION-END — 2026-05-25T01:38:00Z — write-b01c01-pass2-svo-recasts
findings-applied: 15 (14 SVO patches + 1 bone drop with rationale relocation)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T02:00:00Z — write-b01c01-pass2-round2
dispatch: minimum-change patches for 3 faults from write-b01c01-pass2 round 2 re-audit (fault-001 s02n05 'inward', fault-002 s03n06 'in the lane', fault-003 s01 event_map stale reference)
target: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
audit-report: active-project/staff/auditor/write-b01c01-pass2.md
findings-queued: 3

## fault-001 — RESOLVED — 2026-05-25T02:01:00Z
fault: b01c01s02n05 svo contained banned adverb 'inward' (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the lane-mouth presses the crowd inward" to "the lane-mouth presses the crowd"; adverb stripped, direct object retained; axes_held (political_register-prot) and rationale unchanged; no deviation from recast_hint
criteria met: yes

## fault-002 — RESOLVED — 2026-05-25T02:02:00Z
fault: b01c01s03n06 svo contained banned prepositional phrase of place 'in the lane' (FAULT-FORM-MODIFIER)
scope: line
change: svo recast from "the gap closes in the lane" to "the gap closes"; bare intransitive chosen over transitive recast (lower-risk minimum change; parallels 'the crowd thins', 'the insects propagate', 'the gap propagates' already passing); axes_held (moral_framework) and rationale unchanged; no deviation from recast_hint (bare intransitive was primary recommended candidate)
criteria met: yes

## fault-003 — RESOLVED — 2026-05-25T02:03:00Z
fault: s01 event_map entry 'ward read only at surfaces' had covered_by: [b01c01s01n05] — dead reference to dropped bone (FAULT-EVENT-MAP-STALE-REFERENCE)
scope: line
change: covered_by updated from [b01c01s01n05] to [b01c01s01n02, b01c01s01n07]; s01n02 carries the smell surface-read (tallow smoke / stitch-house lane); s01n07 carries the relocated political_register-prot rationale naming the ward-read held at structural baseline; omission_rationale remains null (event has live coverage); no deviation from dispatch recommendation
criteria met: yes

## /and-write b01c01 Phase 2 round 2 — 2026-05-25

- fault-001 (b01c01s02n05): "the lane-mouth presses the crowd inward" → "the lane-mouth presses the crowd" — adverb stripped
- fault-002 (b01c01s03n06): "the gap closes in the lane" → "the gap closes" — bare intransitive, prep phrase of place stripped
- fault-003 (s01 event_map): covered_by [b01c01s01n05] → [b01c01s01n02, b01c01s01n07] — dead reference replaced with two existing bones covering the ward-surface-read event

## SESSION-END — 2026-05-25T02:03:00Z — write-b01c01-pass2-round2
findings-applied: 3
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T03:00:00Z — write-b01c01-pass5
dispatch: Phase 5 continuity audit fixes — 1 FAULT-STATE (add b01c01s03n10) + flag-001 (decomposer_notes total correction) + flag-002 (deferred, outside /and-write scope)
target: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
audit-report: active-project/staff/auditor/write-b01c01-pass5.md
findings-queued: 3 (1 FAULT-STATE + 2 documentation flags; flag-002 deferred on dispatch)

## /and-write b01c01 Phase 5 — 2026-05-25

- bone_added: b01c01s03n10
  svo: "wren-stitch-maker-flea-bottom-ward faces taylor"
  position: appended after s03n09
  axes_held: [relational_anchor_status]
  fault_addressed: FAULT-STATE (handoff_out 'Wren has seen Taylor's face' had no bone delivering the perceptual event)
  rationale: "chapter-goal-clause-2 plant ('plant Wren's presence before it becomes legible as a cost') delivered at chapter-close; un-priced anchor's perceptual presence to reader, structural dormancy in Taylor's calculus"

- event_map_updates_s03:
  - added: "load-bearing image: Wren orients toward Taylor across the dispersing crowd (chapter-close cost-bearer plant)" covered_by [b01c01s03n10]
  - amended: "stitch-house smell still present ..." covered_by add b01c01s03n10

- decomposer_notes_corrections:
  - s01: 7 → 6 (s01n05 dropped at Pass 2 round 1)
  - s03: 9 → 10 (s03n10 added at Phase 5)
  - chapter total: 27 (unchanged but redistribution noted)

- flag-002 deferred (cast-selection.md staleness): outside /and-write scope; surface to /and-cast or margit catalog rebuild

Closing summary: 1 bone added; 2 event_map entries updated; 1 decomposer_notes block corrected; 1 flag deferred.

## FAULT-STATE (b01c01s03n10 add) — RESOLVED — 2026-05-25T03:05:00Z
fault: handoff_out character_state "Wren has seen Taylor's face" had no bone delivering the perceptual event; bones established Wren's presence only through environmental rationale notes and sensory-plant bones where Wren was not a subject
scope: line
change: bone b01c01s03n10 appended as final bone of s03; svo "wren-stitch-maker-flea-bottom-ward faces taylor"; axes_held relational_anchor_status; s03 event_map updated with new cost-bearer-plant entry and amended stitch-house-smell entry to add n10 to covered_by; s03 header updated to Bone count: 10 with n10 note; decomposer_notes updated to reflect 6+11+10=27 with per-scene rationale
criteria met: yes — bone makes Wren a subject performing a posture-act toward Taylor; slug identifies her to the reader; Taylor reads orientation-without-recognition (structural dormancy preserved); handoff_out claim grounded

## flag-001 (decomposer_notes total correction) — RESOLVED — 2026-05-25T03:05:00Z
fault: decomposer_notes chapter-level total claimed 7+11+9=27 bones but s01n05 was dropped (s01=6) and s03n10 was added (s03=10); totals were internally inconsistent
scope: line
change: decomposer_notes updated to read 6 (s01) + 11 (s02) + 10 (s03) = 27; per-scene corrections annotated with phase-of-change; held-axis coverage for s03 updated to include n10 as third relational_anchor_status covering bone; density math re-affirmed
criteria met: yes

## flag-002 (cast-selection.md staleness) — ESCALATED — 2026-05-25T03:05:00Z
fault: cast-selection.md carries ward-elder slot as '[original] ward-elder, name TBD' (pre-Phase 4); bones file and memory.md use committed slug oswyn-mudway-flea-bottom-elder
scope: escalate
change: none — deferred as outside /and-write scope; cast-selection.md is /and-cast territory (or margit catalog rebuild); no edit made
criteria met: n/a — deferred to /and-cast next invocation or margit catalog rebuild

## SESSION-END — 2026-05-25T03:05:00Z — write-b01c01-pass5
findings-applied: 2 (FAULT-STATE resolved; flag-001 resolved)
findings-skipped: 1 (flag-002 deferred — outside /and-write scope; cast-selection.md is /and-cast / margit territory)
exit: CLEAN

## SESSION-START — 2026-05-25T04:00:00Z — write-b01c01-phase6-bone-gate
dispatch: Phase 6 substance bone-gate repairs — 3 HARD (HELD-AXIS-UNCONTRACTED on s02n02, s02n04, s02n08) + 1 SIGNAL remediate (s01n04 SVO recast) + 2 SIGNAL accept-with-rationale (faces verb, s01n07 axes-per-bone)
target: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
audit-report: active-project/staff/auditor/write-b01c01-bone-gate.md
findings-queued: 6 (3 HARD + 3 SIGNAL)

## fault-001 (s02n02 HELD-AXIS-UNCONTRACTED) — RESOLVED — 2026-05-25T04:05:00Z
fault: b01c01s02n02 held capability, which is in s02 axes_in_motion not axes_held; HELD-AXIS-UNCONTRACTED
scope: line
change: axes_held[0] changed from axis: capability to axis: moral_framework; rationale rewritten as prohibition-intact / baseline-perception-not-deployment (capability-as-baseline-perception → moral_framework-as-prohibition-intact)
criteria met: yes — s02n02 no longer carries capability in axes_held; moral_framework is a contracted held axis for s02

## fault-002 (s02n04 HELD-AXIS-UNCONTRACTED) — RESOLVED — 2026-05-25T04:06:00Z
fault: b01c01s02n04 held both moral_framework (clean) and capability (uncontracted for s02); HELD-AXIS-UNCONTRACTED on capability entry
scope: line
change: capability axes_held entry dropped; moral_framework rationale extended to absorb threshold-crossing-legibility note ("the threshold-crossing at the next bone reads as a crossing because this bone holds the line right before it"); axes_held reduced from 2 to 1 entry
criteria met: yes — s02n04 axes_held contains only moral_framework, a contracted held axis for s02

## fault-003 (s02n08 HELD-AXIS-UNCONTRACTED) — RESOLVED — 2026-05-25T04:07:00Z
fault: b01c01s02n08 held capability, which is in s02 axes_in_motion not axes_held; HELD-AXIS-UNCONTRACTED
scope: line
change: axes_held[0] changed from axis: capability to axis: moral_framework; rationale rewritten as crack-continuing / deployment-cascade-extending-prohibition-violation (capability-as-deployment-mechanism → moral_framework-as-crack-extending)
criteria met: yes — s02n08 no longer carries capability in axes_held; moral_framework is a contracted held axis for s02

## signal-001 (s01n04 propagate mannerism) — RESOLVED — 2026-05-25T04:08:00Z
fault: bare intransitive 'propagate' appeared 3× chapter-wide (s01n04, s02n06, s02n08); URI-WRITE-REGISTER-MANNERISM ≥3 threshold hit; s01n04 and s02n06 were also identical SVOs
scope: line
change: s01n04 svo recast from "the insects propagate" to "the insects swell"; rationales unchanged; propagate count drops to 2× (s02n06, s02n08) — below threshold; identical-SVO pair eliminated
criteria met: yes

## signal-002 (faces-verb mannerism) — ACCEPTED-WITH-RATIONALE — 2026-05-25T04:09:00Z
fault: verb 'faces/face' appears 5× chapter-wide across 4 distinct VERB+OBJECT pairs
scope: n/a (no patch)
change: none — ACCEPT-WITH-RATIONALE recorded; no single VERB+OBJECT pair hits ≥3 threshold (max 'faces taylor' at 2); body-orientation register is load-bearing for ward-categorization beats (witnesses face the foreign woman; the foreign woman faces her work; Wren faces Taylor); replacing 'faces' with synonyms would reintroduce banned prepositional forms ('turns to', 'pivots toward') or damage the posture-vocabulary register
criteria met: yes — disposition recorded; no mechanical threshold crossed; register rationale documented

## signal-003 (s01n07 axes-per-bone overage) — ACCEPTED-WITH-RATIONALE — 2026-05-25T04:10:00Z
fault: b01c01s01n07 carries 3 axes_held entries (moral_legibility_to_self, moral_framework, political_register-prot); chunk_targets.bone.axes_per_bone: 1-2
scope: n/a (no patch)
change: none — ACCEPT-WITH-RATIONALE recorded; third axis (political_register-prot) is a repair-move consequence of s01n05 drop at Pass 2 round 1; removing it would require either a new s01 political_register-prot held bone (over-engineering) or losing scene-level held-coverage on political_register-prot (HELD-AXIS-NOT-WITNESSED fault); /and-facets flagged to distribute the three axes across separate facet entries
criteria met: yes — disposition recorded; over-commitment is a documented repair-move artifact, not a substantive authoring choice

## /and-write b01c01 Phase 6 — 2026-05-25

- HARD-fix s02n02:
  axes_held_before: [capability]
  axes_held_after: [moral_framework]
  rationale_change: "capability-as-baseline-perception → moral_framework-as-prohibition-intact"

- HARD-fix s02n04:
  axes_held_before: [moral_framework, capability]
  axes_held_after: [moral_framework]
  rationale_change: "merged threshold-crossing-legibility into moral_framework rationale; dropped redundant capability entry"

- HARD-fix s02n08:
  axes_held_before: [capability]
  axes_held_after: [moral_framework]
  rationale_change: "capability-as-deployment-mechanism → moral_framework-as-crack-extending"

- SIGNAL-remediate s01n04:
  svo_before: "the insects propagate"
  svo_after: "the insects swell"
  reason: "URI-WRITE-REGISTER-MANNERISM — propagate ∅ at 3× chapter-wide; recast lowest-stakes instance (s01n04); s02n06 moving bone and s02n08 deployment-cascade bone preserved"

- SIGNAL-accept faces-verb mannerism:
  disposition: accept-with-rationale
  rationale: "no VERB+OBJECT pair hits ≥3 threshold (max faces taylor 2); body-orientation register is load-bearing for ward-categorization beats; synonyms would reintroduce banned forms or damage register"

- SIGNAL-accept s01n07 3-axes-held overage:
  disposition: accept-with-rationale
  rationale: "third axis political_register-prot relocated from dropped s01n05 at Pass 2 round 1; removing would force authoring a new s01 political_register-prot held bone or losing scene-level held-coverage; repair-move consequence, not substantive over-commitment"

Closing summary: 3 HARD repairs applied; 1 SIGNAL remediated; 2 SIGNALs accept-with-rationale.

## SESSION-END — 2026-05-25T04:10:00Z — write-b01c01-phase6-bone-gate
findings-applied: 4 (3 HARD patched; 1 SIGNAL remediated)
findings-skipped: 2 (2 SIGNALs accepted-with-rationale — no patch required by disposition)
exit: CLEAN

## SESSION-START — 2026-05-25T05:00:00Z — facets-b01c01-phase5-remediation
dispatch: remediate 5 HARD findings from facets-final-audit.md — 3 proto-lines citation-ID remappings (fault-001/002/003), 1 dialogue per-speaker cap decision (fault-004), 1 vibes token parsability fix (fault-005)
target: active-project/theater/proto-lines/b01-c01.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 5

## fault-001 — RESOLVED — 2026-05-25T05:15:00Z
fault: proto-lines @12 cited [state:1][state:2] (Oswyn's pre-consolidation IDs); Taylor's deployment-state (state:3) and capability_axis (state:4) had back=N; Oswyn state entries decorated the wrong bone
scope: line
change: proto-lines @12 citation changed from [state:1][state:2] to [state:3][state:4]; cite-index updated: state:3 back=N→back=Y @12; state:4 back=N→back=Y @12; co-citations corrected throughout; narrator:4 and vibes:3/4/8 co-lists updated to replace state:1,state:2 with state:3,state:4
criteria met: yes — state:3 back=Y anchored @12; state:4 back=Y anchored @12

## fault-002 — RESOLVED — 2026-05-25T05:15:00Z
fault: proto-lines @10 cited [feel:1][feel:2]; feel:1 is Oswyn's @21 entry; spurious citation placed Oswyn's somatic tell at the wrong bone
scope: line
change: proto-lines @10 citation changed from [feel:1][feel:2] to [feel:2]; cite-index updated: feel:2 back=Y exclusively @10 (no spurious @10 back-link for feel:1); feel:2 now lonely (correct — sole decoration at @10)
criteria met: yes — feel:1 back=Y exclusively @21; feel:2 back=Y exclusively @10

## fault-003 — RESOLVED — 2026-05-25T05:15:00Z
fault: proto-lines @24 cited [feel:2][feel:3][narrator:8][state:5]; feel:2 belongs to @10 (Taylor breath-empties-out from scene-B); state:5 is Taylor's posture @17, not body-orientation @24; also: @17 cited [state:3] (Taylor deployment @12) instead of [state:5] (Taylor posture @17); @21 cited [state:4] (Taylor capability @12) instead of [state:6] (Taylor social_tether @21); @26 cited [state:6] (Taylor social_tether @21) instead of [state:8] (Taylor ward-recognition @26); @27 missing [state:9] (Wren relational_anchor @27)
scope: line
change: five proto-lines corrected — @17: state:3→state:5; @21: state:4→state:6; @24: feel:2 removed, state:5→state:7; @26: state:6→state:8; @27: state:9 added — cite-index regenerated; all state:5/@17, state:6/@21, state:7/@24, state:8/@26, state:9/@27 now back=Y; feel:3 @24 co-list corrected; feel:4 @27 co-list updated with state:9
criteria met: yes — state:5 back=Y @17; state:6 back=Y @21; state:7 back=Y @24; state:8 back=Y @26; state:9 back=Y @27; feel:2 back=Y exclusively @10; feel:3 back=Y exclusively @24

## fault-004 — RESOLVED (DOWNGRADED) — 2026-05-25T05:20:00Z
fault: 3 utterances from taylor-hebert-kl-122ac all anchored @16; per-speaker per-anchor sub-cap "no two utterances of the same speaker at the same anchor unless deliberate single-turn split documented in drafts sidecar" appeared to be breached
scope: n/a (no file change)
change: none — rubric (staff/dialogue-writer/rubric-dialogue.md § "Per-anchor caps") grants exception for "deliberate single-turn split... justified in the drafts sidecar." Sidecar (active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md) documents: (a) three distinct board-moves required by s02 chunk (fever/air/known-adult); (b) per-entry Q1+Q2 rationale for each utterance; (c) explicit per-anchor count "3 (cap = 3; at cap)." The three utterances are a deliberate three-part information-delivery sequence matching the chunk's explicit three-part delivery specification — not an arbitrary multi-split of one message. Exception path satisfied. Fault downgraded to flag with rubric citation.
criteria met: yes — rubric-grounded decision documented; no reduction required; per-speaker exception path confirmed satisfied

## fault-005 — RESOLVED — 2026-05-25T05:22:00Z
fault: vibes:3 @12 token "instinct-preceded-the-ledger-entry" parses as complete sentence (subject + finite verb + object); vibes schema forbids sentence-parseable tokens
scope: line
change: vibes-b01-c01.md vibes:3 token changed from "instinct-preceded-the-ledger-entry" to "instinct-preceding-the-ledger-entry" (gerund form; no finite verb; "preceding" is a present participle modifying "instinct" — not a predication); semantic content preserved (instinct acting before the ledger-entry exists)
criteria met: yes — "instinct-preceding-the-ledger-entry" does not parse as subject+finite-verb+object; gerund form is a noun-phrase for word-algebra operator use

## SESSION-END — 2026-05-25T05:22:00Z — facets-b01c01-phase5-remediation
findings-applied: 5 (fault-001 resolved; fault-002 resolved; fault-003 resolved; fault-004 downgraded per rubric exception; fault-005 resolved)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T10:00:00Z — and-facets-cycle1-fixes-feeling
dispatch: Phase 5b cycle-1 remediation — feeling facet; 1 dissent from dark-fantasy-reader (feel:3 @24 Q1 fail / NI:8 body-register redundancy); apply minimum revise or delete + URI-FACETS-CYCLE-N-ADD pre-validation; do not touch other facets
target: active-project/theater/facets/feeling-taylor-hebert-kl-122ac.md (primary), active-project/theater/facets/feeling.md (consolidated)
audit-report: active-project/staff/audience/dark-fantasy-reader/feeling-r1-verdict.md
findings-queued: 1 (feel:3 REVISE/DELETE) + ADD pre-validation check

## SESSION-START — 2026-05-25T06:00:00Z — facets-cycle1-remediation-location-state
dispatch: Phase 5b cycle-1 remediation for location-state facet — address dark-fantasy-reader's two entry-level callouts (SEAM-LOC-CARDS-ABSENT @1–@6; SEAM-TRANSITION-RUN-BARE @1–@6) with minimum change
target: active-project/theater/facets/location-state-b01-c01.md
audit-report: active-project/staff/audience/dark-fantasy-reader/location-state-r1-verdict.md
findings-queued: 2 (two callouts from dark-fantasy-reader; cape-fic-reader and worm-canon-pedant ACCEPTED)

## SESSION-START — 2026-05-25T06:30:00Z — facets-cycle1-dialogue-taylor
dispatch: /and-facets Phase 5b cycle-1 remediation — dialogue facet, character taylor-hebert-kl-122ac; 1 HARD finding from worm-canon-pedant (entry 2 facet-license feel:1 @10 is wrong per locked cite-index)
target: active-project/theater/dialogue/taylor-hebert-kl-122ac.md
audit-report: active-project/staff/audience/worm-canon-pedant/dialogue-taylor-hebert-kl-122ac-r1-verdict.md
findings-queued: 1

## SESSION-START — 2026-05-25T10:10:00Z — facets-cycle1-dialogue-taylor (RESUME — prior run incomplete)
dispatch: resume incomplete cycle-1 remediation; prior SESSION-START written but no per-fault or SESSION-END logged; verify fix state and close
target: active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md (sidecar — carries facet-license citations)
audit-report: active-project/staff/audience/worm-canon-pedant/dialogue-taylor-hebert-kl-122ac-r1-verdict.md
findings-queued: 1 (entry 2 feel:1 @10 citation DELETE/REVISE)

## dialogue-entry-2-feel1-citation — RESOLVED — 2026-05-25T10:15:00Z
fault: entry 2 facet-licenses cited feel:1 @10; locked cite-index has feel:1 @21 (not @10); @10 carries feel:2 only; citation walk fails to resolve — HARD per URI-FACETS-CYCLE-1
scope: line
change: DELETE path confirmed executed. Verified sidecar Entry 2 facet-licenses field: contains only `sensory:2 @16`; feel:1 @10 is absent. The prior session removed the bad citation from the per-entry block and documented the deletion in the sidecar bottom-summary citation-completeness note ("feel:1 @10 citation deleted at cycle-1 remediation — feel:1 fires at @21, not @10; feel:2 fires at @10 but describes foot-plant, not breath-tell; citation could not be salvaged by remapping"). Dialogue file (taylor-hebert-kl-122ac.md) carries only utterance text — no citation fields there; no change needed. Q1 for entry 2 ACCEPTED by worm-canon-pedant; spoken text unchanged.
criteria met: yes — entry 2 facet-licenses no longer names an anchor where the cited facet does not fire; sensory:2 @16 is the sole surviving license and resolves correctly in the locked cite-index (back=Y, co=[taylor-hebert-kl-122ac:1, taylor-hebert-kl-122ac:2, taylor-hebert-kl-122ac:3])

## SESSION-END — 2026-05-25T10:15:00Z — facets-cycle1-dialogue-taylor
findings-applied: 1 (entry 2 feel:1 @10 citation DELETE — confirmed complete; prior session applied the change, this session verified and closed the log)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T07:00:00Z — facets-cycle1-state-updates-remediation
dispatch: Phase 5b cycle-1 remediation for state-updates facet — all 3 reviewers dissented; cross-reviewer dedupe + minimum-change fixes to per-character slice files and consolidated state-updates.md
target: active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + state-updates-wren-stitch-maker-flea-bottom-ward.md + state-updates.md
audit-report: active-project/staff/audience/{cape-fic-reader,dark-fantasy-reader,worm-canon-pedant}/state-updates-r1-verdict.md
findings-queued: tbd (deduping across 3 verdicts)

## SESSION-START — 2026-05-25T08:00:00Z — facets-cycle1-remediation-sensory
dispatch: Phase 5b cycle-1 remediation for sensory facet — 2 dissenting reviewers (sensory-disambiguation-pedant REVISE; sensory-modality-coverage REVISE); dedupe by [sensory:id], apply minimum change per rubric, pre-validate any ADDs per anti-pattern #14; loc-state cross-facet anchor edits must precede any sensory ADD
target: active-project/theater/facets/sensory-b01-c01.md
audit-report: active-project/staff/audience/sensory-disambiguation-pedant/sensory-r1-verdict.md + active-project/staff/audience/sensory-modality-coverage/sensory-r1-verdict.md
findings-queued: tbd (reading verdicts now)

## facets-cycle1-sensory — WORKING — 2026-05-25T08:10:00Z
note: deduping across 2 dissenting reviewers; resolving sensory:2 disambiguation-HARD + tactile-silent-gap; pre-validating tactile ADD under anti-pattern #14; loc-state cross-facet impact assessed (no new edit required — existing carve-out covers new tactile entry)

## SESSION-START — 2026-05-25T09:00:00Z — facets-cycle1-fixes-memory
dispatch: Phase 5b cycle-1 remediation for memory facet — all 3 reviewers dissented; dedupe callouts by [memory:id] and resolve with minimum change; ADD pre-validation per URI-FACETS-CYCLE-N-ADD
target: active-project/theater/facets/memory-b01-c01.md
audit-report: active-project/staff/auditor/facets-final-audit-r2.md (flags carried by reference); verdicts: cape-fic-reader + dark-fantasy-reader + worm-canon-pedant memory-r1-verdict.md
findings-queued: 2 entries (mem:1, mem:2) deduped from 3 verdict files

## SESSION-START — 2026-05-25T10:00:00Z — and-facets-cycle1-fixes-state-updates
dispatch: /and-facets Phase 5b cycle-1 remediation — state-updates facet, all 3 reviewers dissented; cross-reviewer dedupe + minimum-change fixes
target: active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + state-updates-wren-stitch-maker-flea-bottom-ward.md + state-updates.md
audit-report: active-project/staff/audience/cape-fic-reader/state-updates-r1-verdict.md + dark-fantasy-reader/state-updates-r1-verdict.md + worm-canon-pedant/state-updates-r1-verdict.md
findings-queued: tbd — deduplication pass required

## SESSION-START — 2026-05-25T11:00:00Z — and-facets-cycle1-fixes-vibes
dispatch: Phase 5b cycle-1 remediation for vibes facet — all 3 reviewers dissented; cross-reviewer dedupe by [vibes:id]; minimum-change fixes per dispatch callouts; ADD pre-validation per URI-FACETS-CYCLE-N-ADD
target: active-project/theater/facets/vibes-b01-c01.md
audit-report: active-project/staff/audience/cape-fic-reader/vibes-r1-verdict.md + dark-fantasy-reader/vibes-r1-verdict.md + worm-canon-pedant/vibes-r1-verdict.md
findings-queued: 6 (vibes:1, vibes:2, vibes:5, vibes:8, vibes:9, vibes:10) + volume-ADD 2 entries pre-validation

## vibes:1 — RESOLVED — 2026-05-25T11:05:00Z
fault: tokens diagnostic not felt-residue; dark-fantasy-reader gate 6: no operator-actionable compression of 3 weeks suppression-work labor
scope: line
change: added token "argument-made-so-often-it-precedes-the-needing" to bundle; AP8 pass; biases dialogue-writer register toward self-justification preceding conscious-decision
criteria met: yes

## vibes:2 — RESOLVED — 2026-05-25T11:06:00Z
fault: "range-ceiling-felt-as-sharpening-not-as-pain" names phenomenology only; dark-fantasy-reader gate 6 fail (no operator-behavior encoding)
scope: line
change: replaced "range-ceiling-felt-as-sharpening-not-as-pain" with "range-edge-as-focus-not-pain"; AP8 pass; biases NI toward attention-at-ceiling and studio away from pain-register
criteria met: yes

## vibes:5 — RESOLVED — 2026-05-25T11:07:00Z
fault: "ward-elder-building-the-category-in-real-time" is time-indexed process-description, not a durable mark; dark-fantasy-reader: time-pressure evaporates
scope: line
change: replaced "ward-elder-building-the-category-in-real-time" with "the-witness-who-keeps-the-incomplete-account"; AP8 pass; permanent mark biasing Oswyn NPC dialogue-writer toward incomplete-ledger-keeper register
criteria met: yes

## vibes:8 — RESOLVED — 2026-05-25T11:08:00Z
fault: tokens 1+3 semantic overlap with vibes:4 / vibes:6 (crowd-consent and ward-record vocabulary restatement); location should carry location-specific content
scope: line
change: replaced token 1 "crowd-moved-here-without-consent" with "place-pressed-into-service-without-asking"; replaced token 3 "foreign-woman-in-the-ward-record" with "ward-space-holding-the-event-in-its-texture"; middle token retained; both replacements AP8 pass
criteria met: yes

## vibes:9 — RESOLVED — 2026-05-25T11:09:00Z
fault: "reader-knowing-before-taylor-does" is meta-narrative; worm-canon-pedant: no downstream operator can act on reader-epistemics; category error in word-algebra
scope: line
change: deleted "reader-knowing-before-taylor-does"; remaining two tokens unchanged
criteria met: yes

## vibes:10 — RESOLVED — 2026-05-25T11:10:00Z
fault: ++ on tragic-causal cites only in-episode protos; V1.1 Patch 1 requires world-build source confirming pre-seeded status; worm-canon-pedant
scope: line
change: added "world-build:taylor-kl122ac-vibes-preseed" to licensed-by; verified tragic-causal pre-seeded in actors/taylor-hebert-kl-122ac/vibes.md; ++ op confirmed correct
criteria met: yes

## vibes:11 ADD — ADD-LANDED — 2026-05-25T11:11:00Z
fault: volume floor shortfall (10 < 12); cape-fic-reader; capability dimension first-expenditure event unrepresented
scope: line
change: added vibes:11 actor:taylor-hebert-kl-122ac + capability-first-expenditure [first-deployment-as-opening-of-the-account, range-as-resource-not-refilling, cost-unpriced-by-the-ledger-at-this-point]; pre-validation PASS; count 11
criteria met: yes

## vibes:12 ADD — ADD-LANDED — 2026-05-25T11:12:00Z
fault: volume floor shortfall (11 < 12); cape-fic-reader; loc:loc-flea-bottom witch-label-formation absent as permanent location charge
scope: line
change: added vibes:12 loc:loc-flea-bottom + the-witch-label-assembled-here [ward-as-the-naming-space, place-of-first-foreign-knowing, the-location-carrying-stage-1-permanently]; pre-validation PASS; count 12; volume floor met
criteria met: yes

## SESSION-END — 2026-05-25T11:12:00Z — and-facets-cycle1-fixes-vibes
findings-applied: 8 (vibes:1 token-add, vibes:2 token-replace, vibes:5 token-replace, vibes:8 two-token-replace, vibes:9 token-cut, vibes:10 license-add, vibes:11 ADD-LANDED, vibes:12 ADD-LANDED)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T12:00:00Z — and-facets-cycle1-fixes-location-state
dispatch: Phase 5b cycle-1 remediation — location-state facet; 1 dissent from dark-fantasy-reader; two callouts: SEAM-LOC-CARDS-ABSENT @1–@6 + SEAM-TRANSITION-RUN-BARE @1–@6; apply minimum ADD after URI-FACETS-CYCLE-N-ADD pre-validation
target: active-project/theater/facets/location-state-b01-c01.md
audit-report: active-project/staff/audience/dark-fantasy-reader/location-state-r1-verdict.md
findings-queued: 2 callouts (treated as one ADD operation — one entry at @1 addresses both)

## SESSION-START — 2026-05-25T13:00:00Z — and-facets-cycle1-fixes-memory
dispatch: Phase 5b cycle-1 remediation — memory facet; all 3 reviewers dissented; cross-reviewer dedupe by [memory:id]; minimum-change resolve; ADD pre-validation per URI-FACETS-CYCLE-N-ADD
target: active-project/theater/facets/memory-b01-c01.md
audit-report: active-project/staff/audience/{cape-fic-reader,dark-fantasy-reader,worm-canon-pedant}/memory-r1-verdict.md
findings-queued: 2 entries deduped (mem:1 SIGNAL-only; mem:2 REVISE — spineless fire at @26)

## mem:2 — WORKING — 2026-05-25T13:05:00Z
note: mem:2 spine gap requires upstream narrator-interest ADD at @26 first; then cite-index + proto-lines update; then per-task log write

## feel:3-delete — RESOLVED — 2026-05-25T10:15:00Z
fault: feel:3 @24 taylor Q1 fails — NI:8 @24 "set the body to the alley-mouth" already names body-direction event in somatic register; feel:3 "her head fixes toward the alley-mouth, away from the stitch-house lane" covers same direction with no distinct finer-grain tell; dark-fantasy-reader REVISE verdict (flag-011 overlap)
scope: line
change: DELETE feel:3; updated: feeling-taylor-hebert-kl-122ac.md (entry 2 deleted), feeling.md consolidated (entry deleted), proto-lines/b01-c01.md (@24 [feel:3] removed), _cite-index.md (feel:3 entry removed; narrator:8 + state:7 co-lists cleaned; feel section 4→3 entries; totals 44→43; density table 3-citation row decremented)
criteria met: yes — Q1 redundancy eliminated; Taylor drops to 1 fire (feel:2 @10 = 3.7%, within 2-5% band); over-band flag auto-resolved; no other facets touched

## ADD-pre-validation — RESOLVED — 2026-05-25T10:15:00Z
fault: URI-FACETS-CYCLE-N-ADD pre-validation required before any ADD
scope: n/a
change: none — no ADD justified; 3 fires on 27 bones after deletion; default-to-silence applies
criteria met: yes

## SESSION-END — 2026-05-25T10:15:00Z — and-facets-cycle1-fixes-feeling
findings-applied: 1 (feel:3 deleted) + ADD pre-validation clean
findings-skipped: 0
exit: CLEAN

## sensory:1 — RESOLVED (no-change) — 2026-05-25T08:20:00Z
fault: sensory-old-state-reader advisory only (negative-inference old-state for lane-ambient); no HARD; disambiguation-pedant confirmed CLEAN; modality-coverage no per-entry callout
scope: n/a (no change required)
change: none — entry defended in place under existing carve-out; advisory noted but non-blocking under current rubric
criteria met: yes

## sensory:2 (anchor move @16→@9; modality sound→tactile) — RESOLVED — 2026-05-25T08:25:00Z
fault: (1) disambiguation-pedant HARD: sensory:2 @16 "raises the voice" is action-verb self-charge — English idiom "raise one's voice" means louder; sound inflection IS the phrase; Q1 fails; (2) modality-coverage: tactile silent-gap at bones 8-14 (crowd-compression run with zero tactile fires); together these require replacing sensory:2 with a tactile fire on a genuinely bare-verb bone
scope: line (sensory facet file + proto-lines + cite-index)
change: (1) sensory:2 DELETED from @16 (sound: crowd-ambient-murmur -> taylor-raised-voice); (2) new sensory:2 ADDED at @9 (tactile: lane-ambient -> crowd-compression # tag: up); (3) sensory facet carve-out header updated: new per-entry annotation for sensory:2 @9 with full anti-pattern #14 pre-validation; (4) proto-lines: [sensory:2] removed from @16, added to @9; (5) cite-index: sensory:2 line updated @16→@9 co-list removed; sensory:2 added to lonely entries at @9; @9 removed from bare protolines list; totals: 16/27 decorated; density distribution updated (bare 12→11, 1-cite 9→10, 3-cite 1→2)
criteria met: yes — action-verb self-charge HARD cleared; tactile silent-gap addressed; modality floor met (smell + tactile = 2); anti-pattern #14 pre-validation passed; no loc-state edit required (existing carve-out covers new tactile entry's old-state from scene-internal bones 1-8)

## SESSION-END — 2026-05-25T08:25:00Z — facets-cycle1-remediation-sensory
findings-applied: 2 (sensory:1 defended no-change; sensory:2 replaced — sound@16→tactile@9)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-25T10:00:00Z — and-facets-cycle1-fixes-state-updates
dispatch: /and-facets Phase 5b cycle-1 remediation — state-updates facet, all 3 reviewers dissented; cross-reviewer dedupe + minimum-change fixes
target: active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + state-updates-wren-stitch-maker-flea-bottom-ward.md + state-updates.md
audit-report: active-project/staff/audience/cape-fic-reader/state-updates-r1-verdict.md + dark-fantasy-reader/state-updates-r1-verdict.md + worm-canon-pedant/state-updates-r1-verdict.md
findings-queued: 5 (deduped from 3 verdicts: 4 DELETE + 1 REVISE)

## fault-SU-001 (state:4 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: capability_axis @12 — chapter-aggregate substance delta posted as mid-bone canonical field-flip; anti-pattern #7 (ledger-as-state / pre-empting); REJECT worm-canon-pedant; CONTESTED dark-fantasy-reader
scope: line
change: entry deleted from state-updates-taylor-hebert-kl-122ac.md and state-updates.md; [state:4] removed from proto-lines @12; cite-index state:4 removed; co-citation lists stripped of state:4
criteria met: yes — ledger-as-state entry removed; handoff_out capability-rank-3 record unchanged

## fault-SU-002 (state:5 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: posture @17 — POV actor-state entry with no narrator-interest co-citation at @17; lonely entry; rubric cross-facet contract violated; REJECT dark-fantasy-reader
scope: line
change: entry deleted from state-updates-taylor-hebert-kl-122ac.md and state-updates.md; [state:5] removed from proto-lines @17 (bone now bare); cite-index state:5 removed; @17 added to bare-protolines; deletion note: re-add pending NI author providing @17 entry
criteria met: yes — cross-facet-contract-violating entry removed

## fault-SU-003 (state:6 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: social_tether_prot_axis @21 — field not on actor:taylor state.md (anti-pattern #6: invented field); also ledger-as-state; also registration framing; REJECT worm-canon-pedant; CONTESTED dark-fantasy-reader; FLAG cape-fic-reader
scope: line
change: entry deleted from both files; [state:6] removed from proto-lines @21; cite-index state:6 removed; co-citation lists stripped of state:6; @21 pile-up drops 8→7
criteria met: yes — invented-field + ledger-as-state entry removed

## fault-SU-004 (state:8 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: ward-recognition @26 — cross-POV authority violation (Oswyn's categorization on Taylor's slice; already canonical in Oswyn slice state:2); NI co-citation absent; REJECT worm-canon-pedant and dark-fantasy-reader; FLAG cape-fic-reader
scope: line
change: entry deleted from both files; [state:8] removed from proto-lines @26; cite-index state:8 removed; co-citation lists stripped of state:8; Oswyn state:2 unchanged
criteria met: yes — cross-POV authority violation + double-filing removed

## fault-SU-005 (state:9 REVISE) — RESOLVED — 2026-05-25T10:20:00Z
fault: wren relational_anchor_to_taylor — missing field-extension comment; value "observation-traced-d01-deterrence" contains authoring metadata + inaccurate affect charge; soft-flag worm-canon-pedant; value notes from dark-fantasy-reader and cape-fic-reader
scope: line
change: field-extension comment added; value changed to "observation-traced-chapter-1"; applied to state-updates-wren-stitch-maker-flea-bottom-ward.md and state-updates.md; cite-index state:9 back-link unchanged
criteria met: yes — field-extension documented; clean value, no metadata, no inaccurate affect

## SESSION-END — 2026-05-25T10:20:00Z — and-facets-cycle1-fixes-state-updates
findings-applied: 5 (4 DELETE + 1 REVISE)
findings-skipped: 0
exit: CLEAN
cross-facet-impact: narrator-interest author must add @17 NI entry before state:5 (taylor.posture) can be re-authored; @17 is now a bare protoline; all other changes are self-contained state-updates cleanup

## mem:1 — NO-ACTION-DEFENDED — 2026-05-25T13:20:00Z
fault: target-reference slug cond-override-architecture-residue-122ac uses cond-* class, not monument-* convention (flag-013); all 3 reviewers SIGNAL only — not HARD, not a revise verdict on the entry itself
scope: n/a (no file change)
change: none — SIGNAL flag carried forward as-is; margit referral required for slug-class correction; entry accepted on all other axes by all reviewers; fixer does not rename card slugs without margit authority
criteria met: yes — SIGNAL disposition documented; margit referral flagged to showrunner

## mem:2 — RESOLVED — 2026-05-25T13:25:00Z
fault: spineless fire at @26; mem:2 co-cited only [state:2, state:8]; no narrator-interest at @26; no feel-flag at @26; V3 feel-as-spine carve-out fails condition (3); R2 judge's "graph spine" language conflated state-update co-citation with licensing-spine
scope: line (upstream-first: interest-narrator-b01-c01.md ADD, then proto-lines, then cite-index)
change: (1) narrator:9 @26 added to interest-narrator-b01-c01.md: "the chin-lift filed her in a category she recognized the shape of without needing the country's name for it." (2) [narrator:9] added to proto-lines/b01-c01.md @26 citation list (3) cite-index updated: narrator:9 @26 back=Y co=[mem:2, state:2]; mem:2 co-list updated to include narrator:9; memory-b01-c01.md unchanged
criteria met: yes — mem:2 spine is narrator:9 @26; NI register-consistent (clinical, no feeling-word, inventory-tell); file-level checks pass post-repair (doubled-register, sparsity, pressure-signal inversion, per-scene cap)

## SESSION-END — 2026-05-25T13:30:00Z — and-facets-cycle1-fixes-memory
findings-applied: 1 (mem:2 spine repaired via narrator:9 ADD upstream + proto-lines + cite-index)
findings-skipped: 1 (mem:1 NO-ACTION-DEFENDED: SIGNAL only; margit referral, not fixer scope)
exit: CLEAN
