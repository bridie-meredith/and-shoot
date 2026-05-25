# write-b01c01-pass5 audit report
phase: /and-write b01c01 Phase 5 continuity audit
date: 2026-05-25
auditor: auditor
artifact_audited: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
prior_chapter: none

summary:
  total_bones: 26
  faults: 1
  fault_breakdown:
    FAULT-REACHABILITY: 0
    FAULT-STATE: 1
    FAULT-REFERENCE: 0
    FAULT-POV: 0
    FAULT-HANDOFF-IN-MISMATCH: 0
  flags: 2

faults:
  - bone_or_chapter_level: chapter
    class: FAULT-STATE
    rule: "handoff_out character_state asserts a perceptual event for Wren ('has seen Taylor's face') that no bone delivers."
    detail: |
      handoff_out character_state line: "Wren: has seen Taylor; no contact; no named awareness"
      The bones establish Wren's physical presence in the crowd via environmental rationale
      notes at s02n09 ("Wren is in this crowd — the cost-bearer is in the frame as Taylor faces
      the child") and via the stitch-house smell bones (s01n02, s03n08). No bone makes Wren a
      SUBJECT performing any act, and no bone delivers a Taylor-observable fact establishing
      that Wren's face was directed toward Taylor or that Wren registered Taylor's appearance.
      s02n10 ("taylor lifts the hands") establishes Taylor was visible as the crowd-opener, and
      s02n11 ("taylor raises the voice") establishes Taylor was audible — the inference that a
      crowd member present at the scene would have seen Taylor is reasonable, but the handoff_out
      states this as a committed character_state ("has seen Taylor's face"), not as an inference.
      Under the bones-are-the-authority rule, a character_state in handoff_out that is not
      grounded in a delivered bone is unverifiable state. The handoff_out's claim about Wren
      is stronger than what the bones authorize.
    recast_hint: "Either add a bone in s02 or s03 where Wren's face-direction toward Taylor is
      observable within Taylor's perceptual range (e.g., Taylor reads the crowd-shape and
      registers a specific figure's orientation toward her without naming it — consistent with
      structural dormancy), or soften the handoff_out assertion to 'Wren was in the crowd during
      the intervention; no contact; no named awareness' — which the bones do support."

flags:
  - id: flag-001
    bone_or_chapter_level: chapter
    class: documentation
    what: "decomposer_notes chapter-level total claims 7+11+9=27 bones (line 564), but s01n05 was
      explicitly dropped (line 71), making s01 have 6 surviving bones and the correct total 26.
      The dispatch's bone count (26) is correct; the notes are internally inconsistent."
    why: "No bones impact. Documentation confusion could mislead downstream Phase 6 substance
      bone-gate which references total bone counts. No block."

  - id: flag-002
    bone_or_chapter_level: chapter
    class: documentation
    what: "cast-selection.md carries the ward-elder slot as '[original] ward-elder, name TBD'
      (Phase 3 authoring, pre-Phase 4). The bones file uses slug 'oswyn-mudway-flea-bottom-elder'
      and memory.md handoff_out records 'Oswyn Mudway' by name — confirming the Phase 4 slug
      commitment. cast-selection.md has not been updated to reflect the committed slug."
    why: "Not a bones fault; bones resolve correctly against memory.md. But cast-selection.md
      as a reference document is stale at this slug entry. Future audits reading cast-selection.md
      as the roster authority for this slot will find 'TBD.' No block; documentation lag only."

reachability_check:
  goal_clause_1_delivery: |
    Clause: "first act of control — the instinct that survives every prohibition"
    Bones carrying delivery:
      - s02n03: crowd compresses (opposing force enacted; prohibition running against crowd-physics)
      - s02n04: taylor holds the feet (last prohibition-held moment; threshold legibility bone)
      - s02n06: the insects propagate (capability +1, cl01a — the deployment; the act of control)
      - s02n07: nearest dozen bodies yield (bodies yield to insect-pressure — the act of control confirmed; moral_framework crack visible to reader, not to Taylor)
      - s02n11: taylor raises the voice (deployment's final act; accounting has not yet run)
    Verdict: DELIVERED
    Note: The threshold structure (n03/n04 prohibition held → n06 crossing → n07 crack visible but unfiled)
    makes the "instinct that survives every prohibition" legible as a threshold-crossing, not a lapse.

  goal_clause_2_delivery: |
    Clause: "plant the witch-label and Wren's presence before either becomes legible as costs"
    Bones carrying delivery:
      Witch-label plant:
        - s03n04: oswyn takes the lane-mouth (social_tether +1, cl01b; Oswyn's awareness layer receives Taylor)
        - s03n09: oswyn lifts the chin (categorization completing; "the word composing")
        - s03n02, s03n03: fish-cart man and two women watching (corroborating observers; label's accumulation condition)
      Wren's presence plant:
        - s01n02: tallow smoke crosses the stitch-house lane (relational_anchor_status held; "cost-bearer's location real before it is named")
        - s02n09: taylor faces the child (rationale notes Wren is in this crowd, present-but-unregistered)
        - s03n08: tallow smoke layers the lane-floor (stitch-house smell still there; anchor dormancy enacted concretely)
      Neither witch-label nor Wren's presence is legible as a cost within the chapter:
        - moral_framework held as load-bearing dormancy (crack not filed by Taylor)
        - relational_anchor_status held as structural dormancy (Wren absent from Taylor's calculus)
    Verdict: DELIVERED
    Qualification: Wren's-presence plant is delivered at the environmental/sensory level
    (smell-plant + crowd-presence note in rationale). The handoff_out claim "Wren has seen
    Taylor's face" overreaches what the bones deliver — see FAULT-STATE above. The goal
    clause itself ("plant Wren's presence") is delivered; the handoff_out's specific
    articulation of Wren's state is where the fault lives.

  handoff_out_consistency:
    open_threads:
      verdict: PASS with qualification
      detail: |
        - "witch-label formation active in Hook precinct" — PASS: s03n04/n09 deliver Oswyn's
          categorization beginning; consistent with cond-kl-witch-label-formation-122ac stage 1
          starting (single significant observation + ward-elder's categorization = formation
          process beginning, not instant completion).
        - "Wren has seen Taylor's face in the crowd; no exchange, no names" — FAULT (see
          FAULT-STATE above): bones do not deliver the directional perception claim.
        - "Oswyn Mudway observed the intervention; Taylor on his ward-elder awareness layer" —
          PASS: s03n04/n09 deliver.
        - "capability has moved: first deployment is behind Taylor; the prohibition's first crack
          is unacknowledged" — PASS: s02n06 (capability+1), s02n07 (crack visible, not filed).
    world_state:
      verdict: PASS
      detail: |
        - "KL 122 AC; Hook precinct now has a category for Taylor: known-unknown-witch-adjacent"
          — PASS: s03n04/n09 deliver the category-formation beat.
        - "Otto Hightower unaware; no court-tier awareness of Taylor" — PASS: Otto absent from
          all bones; political_register-prot held at baseline across all three scenes; no
          court-material enters any bone.
    character_state:
      verdict: PASS with one line qualified
      detail: |
        - "Taylor: capability rank 3 (one deployment); prohibition intact but cracked; no court
          position; no patron contact; social tether starting (Oswyn-layer)" — PASS: capability
          +1 at s02n06 (from rank 2 to rank 3 consistent); moral_framework held as load-bearing
          dormancy; political_register-prot and social_tether-prot-rise consistent.
        - "Wren: has seen Taylor; no contact; no named awareness" — QUALIFIED: "no contact; no
          named awareness" PASS; "has seen Taylor" is the asserted state not grounded in a bone
          (see FAULT-STATE).
        - "Oswyn: Taylor on his observation layer; not yet an active contact" — PASS: s03n04/n09.

handoff_in_check:
  open_threads_picked_up: PASS
  detail: |
    - "Taylor has been surviving subsistence-anonymous in Flea Bottom for three weeks with no
      contacts and no plan" — s01 opens with Taylor in the drain angle; ward does not know her
      name (s01n01: drain water at the angle; s01n06: angle-wall — geometry of the drain angle
      as the anonymity posture); anonymity enacted by physical location. PASS.
    - "prohibition intact: insects held at minimum range; no systematic reading conducted" —
      s01n03/n04 enact prohibition-maintenance (Taylor holds feet; insects at range-threshold;
      suppression by discipline, not incapacity). PASS.

  world_state_honored: PASS
  detail: |
    - "KL 122 AC; Viserys I on the throne; Rhaenyra named heir" — no bones contradict political
      world-state. No court-tier material enters s01. PASS.
    - "Flea Bottom: Hook precinct anchored by Oswyn Mudway's ward network" — Oswyn's role as
      ward-elder is enacted at s03n04/n09 without being established before s01 (correct — s01
      is the pre-event scene; Oswyn's network anchoring is world-state prior knowledge, not
      something s01 bones need to enact). PASS.
    - "Green faction dominant informally; no formal Taylor-awareness at any court tier" —
      political_register-prot held at baseline in all three scenes; no court material enters
      any bone. PASS.

  character_state_honored: PASS
  detail: |
    - "Taylor: prohibition intact; capability suppressed at rank 2; no court position; no Otto
      contact; no Wren contact; no coin above subsistence" — s01n03 rationale: "suppression by
      discipline, not incapacity"; s01n07 rationale: "the exhalation closes the morning scan
      without a court-encounter." Otto absent. Wren not registered as a person (only as
      stitch-house smell). Location is drain angle (consistent with no-coin, subsistence only).
      PASS.
    - "Wren: no Taylor awareness" — Wren is not a bone subject in s01 or s02; registered only
      as the stitch-house smell (Taylor's perception of an environment, not a person). s02n09
      rationale notes Wren is in the crowd but "anchor enacted as structural dormancy — Taylor
      does not turn toward the cost-bearer." PASS.
    - "Otto: leverage rank 1 (Taylor unknown to him)" — Otto does not appear anywhere in the
      chapter. PASS.

pov_check:
  narrator: taylor-hebert-kl-122ac
  perception_leaks_found: 0
  out_of_range_bones: []
  verdict: CLEAN
  detail: |
    All 26 bones checked. Subject categories:
      Taylor-as-subject: s01n03, s01n07, s02n04, s02n09, s02n10, s02n11, s03n07 (7 bones)
      Taylor's insects / insect-mechanism: s01n04, s02n06, s02n07, s02n08 (4 bones)
      Environment in Taylor's immediate location: s01n01, s01n06, s02n01, s02n05, s03n01,
        s03n06 (6 bones)
      Environment within Taylor's sensory range (smell, ground-transmission): s01n02, s02n02,
        s03n08 (3 bones — all within 200m; stitch-house "two lanes over" is well within
        operational range)
      Observable actors/crowd in Taylor's perceptual range: s02n03, s02n09 (crowd + child at
        arrival), s03n02, s03n03, s03n04, s03n05, s03n09 (6 bones)
    No bone places any subject outside Taylor's perceptual range. No perception verbs leak
    internal states of non-Taylor subjects. Oswyn's chin-lift (s03n09) is read as a body-read
    ("the body tells her she has moved from invisible to present in his accounting" — scene chunk
    framing), consistent with Taylor's pattern-recognition precog expressed as analytical
    observation per cond-override-architecture-residue-122ac. CLEAN.
    Range note: cond-override-architecture-residue-122ac establishes 200m normal range.
    The stitch-house "two lanes over" is within this. Flea Bottom lane geometry per
    cond-kl-geography-122ac places Hook-adjacent lanes well within 200m. PASS.

state_consistency:
  location_track:
    s01: "drain angle off the Hook — covered angle where drain water threads; angle-wall geometry (s01n01, s01n06)"
    s02: "lane where crowd has formed around collapsed child — Taylor moves to this location between s01 and s02 (scene break carries transition; no contradiction)"
    s03: "lane aftermath — Taylor at alley-mouth after crowd dispersal (s03n07: 'taylor faces the alley-mouth')"
    contradictions: []
  prop_track: "no props in chapter — no prop bones authored or referenced; no prop cards in play"
  time_skips: "none (no blank-numbered lines in bones file; no time-skip markers)"

reference_check:
  cast_subjects_resolved: PASS
  detail: |
    - taylor-hebert-kl-122ac: in cast roster as protagonist. PASS.
    - oswyn-mudway-flea-bottom-elder: slug committed at Phase 4 (memory.md handoff_out records
      'Oswyn Mudway' by name; chapter substance notes reference him); cast-selection.md slot
      reads 'TBD' (Phase 3 pre-authoring document, not updated post-Phase 4). Resolution via
      memory.md is authoritative. See flag-002.
    - wren-stitch-maker-flea-bottom-ward: in cast roster as cost-bearer; structurally dormant
      (not a bone subject); referenced only through environmental sensory plant. PASS.
  unnamed_environment_forms:
    - "the drain water" (s01n01)
    - "the tallow smoke" (s01n02, s03n08)
    - "the angle-wall" (s01n06)
    - "the fish-cart" (s02n01)
    - "the ground" (s02n02)
    - "the crowd" (s02n03, s03n01)
    - "the lane-mouth" (s02n05, s03n04)
    - "the insects" (s01n04, s02n06)
    - "the gap" (s02n08, s03n06)
    - "the child" (s02n02, s02n09, s03n05)
    - "the nearest dozen bodies" (s02n07)
    - "the fish-cart man" (s03n02)
    - "the two women" (s03n03)
    - "the alley-mouth" (s03n07)
    All licensed as unnamed environment / unnamed crowd figure / unnamed prop forms.
  verdict: CLEAN

verdict: FAULTS-PRESENT
fault_count: 1
fault_class: FAULT-STATE
fault_location: chapter level (handoff_out character_state)
