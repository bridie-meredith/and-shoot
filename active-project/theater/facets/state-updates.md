---
facet: state-updates
sources: [env-b01-c13, taylor-hebert-kl-122ac-b01-c13]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env-b01-c13
facet: state-updates (env/prop scope)
episode: b01-c13
author: studio
generated: 2026-06-03

# rubric-carve-out — multi-bone time-of-day old-state inferred from scene-map
#
# design/shoot-v2/rubric-state-updates.md § 3. Frugality / § Cross-axis tests / Frugality
#
# Carve-out scope: studio.time_of_day entries at @10 and @24
# Carve-out rule: scene-B ("four days later") and scene-D ("two days later") carry no explicit
#   time-of-day annotation in the scene-map. Old-state values are inferred from scene context
#   (magistrate proceeding = daytime = morning; circuit-walk at fishmongery = daytime = morning).
#   Both entries are first-in-scene-block resets on a multi-day gap; the inferred value is the
#   most defensible canonical reading. If loc-state R1 contradicts either baseline, revise or
#   delete the affected entry at R2.
# Coverage justification: scene-map does not carry explicit time-of-day for scenes B and D;
#   firing a time-of-day reset is canonical-correct behavior at a multi-day gap-scene-open even
#   without a scene-map time anchor. R2 reviewer must ratify both values.
#
# Per-entry annotations:
# - state:5 @10: carve-out clause applies — scene-B time-of-day inferred from proceeding context
# - state:10 @24: carve-out clause applies — scene-D time-of-day inferred from circuit-walk context

---

1 @1 studio.time_of_day: end-of-day -> mid-morning  # chapter-open time reset; new day (Thursday); b01c12 chapter-close was end-of-day
2 @1 studio.location: the-feed-station -> the-hook-upper-provisioning  # scene-A place anchor; chapter opens at the provisioning-store loading platform; first location transition from b01c12
3 @7 prop:oc-fish-account-ledger.condition: open -> closed  # household-agent's tally-ledger closes at account-complete; peak-bone co-citation (@7 is the central event / satisfied-coercion body — the shoulder-drop IS the account-close confirmation); irreversible bureaucratic close; first-touch field-extension: oc-fish-account-ledger (opposing-force prop; no prior warehouse card; margit referral needed)
4 @10 studio.time_of_day: mid-morning -> morning  # scene-B time reset; four-day gap (Thursday mid-morning -> following Monday or later); magistrate proceeding takes place during daytime working hours; carve-out applies (see preamble)
5 @10 studio.location: the-hook-upper-provisioning -> the-magistrate-hall  # scene-B location transition; the rented back room of a chandler's house at the Hook-to-ward-network fringe
6 @11 prop:oc-d06-document.holder: green-apparatus-possession -> table-surface  # green-faction clerk sets the document at the table's edge before the proceeding opens; document enters the physical scene; first-touch (d06-document delivered at c06, now in apparatus hands; old-state inferred — SEAM-C13-ENV-001)
7 @13 prop:oc-procedural-form.condition: blank -> inscribed  # magistrate writes the procedural-form before Aldric finishes speaking; verdict pre-inscribed; irreversible bureaucratic mutation; peak-shadow bone in rising zone (not immediately adjacent to peak — clear of held-against-turn class); first-touch field-extension
8 @15 prop:oc-d06-document.holder: table-surface -> magistrate-hand  # magistrate lifts the d06-document to decide the verdict; peak-bone co-citation (@15 is the central event / political_register-world delivery — the list-output operationally used); the list-used-operationally moment is the canonical state-change
9 @19 studio.time_of_day: morning -> evening  # scene-C time advance; "that evening" — explicit in scene-map; the naming scene on the lane Taylor has walked five hundred times
10 @19 studio.location: the-magistrate-hall -> the-hook-lane  # scene-C location transition; the lane at evening after the two feed-events are held together
11 @24 studio.time_of_day: evening -> morning  # scene-D time reset; "two days later" multi-day gap; Halvard-encounter scene opens during Taylor's ordinary circuit-walk (daytime); carve-out applies (see preamble)
12 @24 studio.location: the-hook-lane -> the-hook-lower-water-trough  # scene-D location transition; the lower end of the Hook where chandler's row meets the open space before the fishmongery
13 @31 prop:oc-water-skin.condition: empty -> filled  # septon-halvard fills the water-skin at the trough; peak-shadow bone in post-peak cold-close zone (not held-against-turn; @31 is post-departure, resolving); persistent state: the water-skin is filled and Halvard carries it forward; first-touch field-extension

---

# Decisions-not-fire (b01c13 env/prop scope)
#
# @8  prop:oc-empty-crate — supplier's-son picks the empty-crate; genuine holder-change (loading-platform
#     -> suppliers-son) and persistent, but culled for density: first-touch oc-prop with no downstream
#     canonical relevance; @7 fish-account-close already records the transaction's canonical state change;
#     crate-pickup is the physical correlate of the already-recorded close. Density-cull defensible.
#
# @14 prop:oc-cord — aldric lifts the cord (presents evidence); held-against-turn class (@14 is
#     immediately adjacent to peak @15); canonical state-change fire forbidden by rubric
#     § held-against-turn. Actor-posture permitted but cord-holder change on this beat is REJECT.
#     The cord is the pretext, not the mechanism; the list (@15) is the mechanism.
#
# @2, @3, @4, @5, @6 — scene-A approach/dexterity/tally-in-progress; no persistent field-changes
#     until the account closes at @7; all inherit @1 scene-A anchors.
#
# @9  — taylor releases blowfly; actor-fork authority (fauna_sense_status is actor-fork's
#     domain for Taylor's insect deployment); no studio prop involved.
#
# @12 — aldric takes the chair; actor-fork authority; no prop or studio field change distinct
#     from scene-B opening state.
#
# @16, @17, @18 — fly grips ceiling-corner / aldric grips table / fly works ceiling-corner;
#     actor-fork (Taylor's feed-deployment) + actor-posture (Aldric's grip); no studio/prop
#     field changes distinct from scene-B state. @17 Aldric grips the table is a peak-shadow
#     posture (consequence-image); actor-fork for aldric; not studio.
#
# @20, @21, @22, @23 — scene-C interior hinge; tallow-smoke crosses lane (ambient transient,
#     not a persistent tracked field), two-breaths / jaw-set / lane-resumes are actor-state
#     and interior events; lane is unchanged before and after the naming; no studio/prop fires.
#
# @25, @26, @27, @28, @29, @30 — scene-D trough/dialogue/departure; actor-state + dialogue;
#     the water-trough is environmental fixture (location-card content, not state-update);
#     no prop changes until @31 water-skin fill.
#
# Field-extensions (4 new oc-props / new fields; margit referrals needed):
#   oc-fish-account-ledger.condition (opposing-force accounting ledger; no prior warehouse card)
#   oc-d06-document.holder (the Taylor-delivered ward-elder list; no prior prop state entry)
#   oc-procedural-form.condition (magistrate's verdict form; scene-local prop; no prior card)
#   oc-water-skin.condition (halvard's water-carrying vessel; no prior prop state entry)
#
# Seams flagged for R2:
#   SEAM-C13-ENV-001: prop:oc-d06-document.holder old-state "green-apparatus-possession" is
#     inferred (delivered to Jarvis at d06; no prior explicit state-update entry on this prop);
#     R2 confirm adequacy or trace to prior chapter delivery bone
#   SEAM-C13-ENV-002: studio.time_of_day @10 old-state "morning" — scene-B has no explicit
#     time-of-day in scene-map ("four days later"); value inferred from proceeding context;
#     carve-out preamble applies; R2 confirm or revise
#   SEAM-C13-ENV-003: studio.time_of_day @24 old-state "morning" — scene-D has no explicit
#     time-of-day in scene-map ("two days later"); value inferred from circuit-walk context;
#     carve-out preamble applies; R2 confirm or revise
#   SEAM-C13-ENV-004: prop:oc-procedural-form.condition — form is described as written before
#     Aldric finishes speaking; @13 fires on the inscribed state; confirm form does not exit
#     the scene in a different condition that would require a follow-up entry
#   SEAM-C13-LOC-001: the-hook-upper-provisioning and the-magistrate-hall slug canonicalization
#     — both are new slugs in b01c13 (bones `locations:` header); no confirmed warehouse cards;
#     margit referral needed
#   SEAM-C13-LOC-002: the-hook-lane slug — bones `locations:` header uses "the-hook-lane";
#     confirm this is distinct from "the-hook-ward" / "oc-hook-precinct" slugs used in prior
#     chapters or flag for margit canonicalization (carry from SEAM-C12-LOC-001 lineage)

# source: taylor-hebert-kl-122ac-b01-c13
facet: state-updates
episode: b01-c13
author: taylor-hebert-kl-122ac (dialogue-writer fork — actor-state, POV-restricted)
target-class: actor:taylor-hebert-kl-122ac
---
# rubric-carve-out — POV co-citation dependency forwarded; field-extensions declared
#
# rubric-state-updates.md (design/shoot-v2/rubric-state-updates.md) § "Field-extension protocol" + § Cross-facet contract (POV co-citation)
#
# Carve-out scope: all actor:taylor-hebert-kl-122ac.* entries below.
# Carve-out rule: every entry is POV-character actor-state and REQUIRES a narrator-interest
#   co-citation on the same @anchor (rubric § Cross-facet contract). The locked NI file
#   (interest-narrator-b01-c13.md) IS present at this authoring; co-citation is RESOLVED, not
#   forwarded. Two POV register-state entries are re-anchored from the scene-map prot peak-bone
#   to the adjacent POV-interior NI-fire beat, because the political_register-prot axis is a
#   POV-interior register-state and must anchor where Taylor's interiority registers, which the
#   locked NI places one beat off the scene-map's consequence-image peak-bone:
#     - s02 prot increment: re-anchored @17 -> @16. NI:4 @16 ("his name on her list, his hands
#       on the table; she holds the connection ... and does not move it to the accounting column")
#       IS the operational-specificity registration. Scene-map @17 (Aldric grips the table) is the
#       non-POV consequence-image with no NI fire; single fire across the @16-@17 rising-to-peak
#       window per § Cross-facet "fire once across the approach-peak window; do not double-fire."
#     - s04 Halvard-foreclosure: re-anchored @29 -> @30. NI:7 @30 ("the feet stay on the circuit;
#       the gap Halvard opened is one she does not turn toward, and the not-turning has the shape
#       of walking") IS the foreclosure made body-state — and satisfies the s04 CARRY_TO_WRITE
#       requirement that the not-turning-toward-the-ledger take physical bone-form. @29 (leaves the
#       trough) has no NI fire; @30 is the scene-map CARRY peak-shadow-bone.
# Field-extension: knowledge.apparatus-assessment + knowledge.halvard-engagement are NEW
#   tracked-state fields (knowledge is a tracked-state aspect per § Field-extension protocol;
#   register/mood/emotional-tenor are NOT — the contempt is written back as a knowledge/finding
#   field + the canonical political_register_prot_axis rank, NEVER as a register/mood field).
# Coverage justification: the chapter's spine is the political_register-prot progression
#   (resentment-object-fixed @7 -> operational-specificity @17 -> named-contempt @19, standing
#   thereafter) + the s04 Halvard-engagement foreclosure. Both are persistent canonical
#   mutations on Taylor's own state, licensed by handoff_out (prot rank 5; Halvard foreclosed).
#
# Per-entry annotations (carve-out clause | rubric clause | defensibility):
# - state:1/2 @7  : POV-co-cite-RESOLVED (NI:1 @7)  | § Cross-facet (POV requires NI) | s01 peak-bone @7; axis +0.5 measured
# - state:3/4 @16 : POV-co-cite-RESOLVED (NI:4 @16) | § Cross-facet (POV requires NI) | re-anchored @17->@16 per carve-out; operational-specificity registration (@15 is the WORLD axis, not authored here; @17 is non-POV consequence-image, no NI fire)
# - state:5/6 @19 : POV-co-cite-RESOLVED (NI:5 @19) | § Cross-facet (POV requires NI) | s03 HINGE peak-bone @19; articulate-contempt threshold crossed to rank 5
# - state:7  @30 : POV-co-cite-RESOLVED (NI:7 @30) | § Cross-facet (POV requires NI) | re-anchored @29->@30 per carve-out; foreclosure as body-state (CARRY peak-shadow-bone; the not-turning-toward-the-ledger in physical form); persistent (handoff_out: will not engage Halvard at substance)

14 @7 actor:taylor-hebert-kl-122ac.political_register_prot_axis: 3.5 -> 4.0   # field-extension: tracked stat (state.md stats.political_register_prot_axis); entering value 3.5 from b01c12 handoff_in (state.md figure 2.5 is c05-stale); s01 peak-bone @7 (the household-agent drops the shoulders — satisfied-coercion posture); resentment-color shifts from ambient to specific-object. NI-co-cite REQUIRED.
15 @7 actor:taylor-hebert-kl-122ac.knowledge.apparatus-assessment: diffuse-resentment -> resentment-fixed-on-object   # field-extension: knowledge (tracked); the apparatus-coercion acquires a specific object; persistent past @7. NI-co-cite REQUIRED.
16 @16 actor:taylor-hebert-kl-122ac.political_register_prot_axis: 4.0 -> 4.5   # re-anchored @17->@16 (carve-out): @16 (fly grips ceiling-corner; she holds the connection between her list and Aldric's charge) is the POV-interior registration; NI:4 fires here. prot +0.5. (@15 list-lift is the political_register-WORLD axis — studio/world-state author, NOT this fork; scene-map @17 Aldric-grips-table is the non-POV consequence-image, no NI fire.) NI-co-cite RESOLVED (NI:4 @16).
17 @16 actor:taylor-hebert-kl-122ac.knowledge.apparatus-assessment: resentment-fixed-on-object -> operationally-specified   # field-extension: the assessment acquires operational specificity — her own d06 list seen put a named body on the table; persistent. NOTE: operational-specificity acquired, NOT a moral_legibility filing — the watches-without-filing hold stands (the crack does not open; no self-ledger entry; recognition-of-repetition foreclosed). NI-co-cite RESOLVED (NI:4 @16).
18 @19 actor:taylor-hebert-kl-122ac.political_register_prot_axis: 4.5 -> 5.0   # s03 HINGE peak-bone @19 (Taylor stops the lane — the naming-threshold made physical); articulate-contempt threshold crossed; rank 5 = articulate-contempt (handoff_out authoritative). The big jump is the threshold-crossing. NI-co-cite REQUIRED.
19 @19 actor:taylor-hebert-kl-122ac.knowledge.apparatus-assessment: operationally-specified -> named-contempt-standing   # field-extension: the word arrives in the functional register and becomes a STANDING internal finding-state (contempt, a verdict-about-quality with specific evidence); directed OUTWARD at the apparatus, NOT turned on her own ledger (moral_legibility held; recognition-of-repetition foreclosed; Khepri/shape-word ABSENT). Persists for the rest of the chapter (s04 enacts, does not revise it). This is the chapter spine. NI-co-cite REQUIRED.
20 @30 actor:taylor-hebert-kl-122ac.knowledge.halvard-engagement: counter-open-pending-response -> foreclosed-response-unneeded   # re-anchored @29->@30 (carve-out): the leave (@29) opens the foreclosure; @30 (walks the route — CARRY peak-shadow-bone, the not-turning-toward-the-ledger in body-form) is where it becomes the persistent engagement-state; NI:7 fires here. The engagement-state flips from "counter held, his response still notionally open" to "foreclosed — response cannot change what she does next and is not needed"; persistent (handoff_out: Taylor will not engage Halvard again at substance). The route-walk is the contempt-without-refusal made physical. NI-co-cite RESOLVED (NI:7 @30).
