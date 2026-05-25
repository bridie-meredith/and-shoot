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
