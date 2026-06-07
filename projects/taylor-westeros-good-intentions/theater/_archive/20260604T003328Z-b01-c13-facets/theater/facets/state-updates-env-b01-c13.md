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

1  @1  studio.time_of_day: end-of-day -> mid-morning  # chapter-open time reset; new day (Thursday); b01c12 chapter-close was end-of-day
2  @1  studio.location: the-feed-station -> the-hook-upper-provisioning  # scene-A place anchor; chapter opens at the provisioning-store loading platform; first location transition from b01c12
3  @7  prop:oc-fish-account-ledger.condition: open -> closed  # household-agent's tally-ledger closes at account-complete; peak-bone co-citation (@7 is the central event / satisfied-coercion body — the shoulder-drop IS the account-close confirmation); irreversible bureaucratic close; first-touch field-extension: oc-fish-account-ledger (opposing-force prop; no prior warehouse card; margit referral needed)
4  @10 studio.time_of_day: mid-morning -> morning  # scene-B time reset; four-day gap (Thursday mid-morning -> following Monday or later); magistrate proceeding takes place during daytime working hours; carve-out applies (see preamble)
5  @10 studio.location: the-hook-upper-provisioning -> the-magistrate-hall  # scene-B location transition; the rented back room of a chandler's house at the Hook-to-ward-network fringe
6  @11 prop:oc-d06-document.holder: green-apparatus-possession -> table-surface  # green-faction clerk sets the document at the table's edge before the proceeding opens; document enters the physical scene; first-touch (d06-document delivered at c06, now in apparatus hands; old-state inferred — SEAM-C13-ENV-001)
7  @13 prop:oc-procedural-form.condition: blank -> inscribed  # magistrate writes the procedural-form before Aldric finishes speaking; verdict pre-inscribed; irreversible bureaucratic mutation; peak-shadow bone in rising zone (not immediately adjacent to peak — clear of held-against-turn class); first-touch field-extension
8  @15 prop:oc-d06-document.holder: table-surface -> magistrate-hand  # magistrate lifts the d06-document to decide the verdict; peak-bone co-citation (@15 is the central event / political_register-world delivery — the list-output operationally used); the list-used-operationally moment is the canonical state-change
9  @19 studio.time_of_day: morning -> evening  # scene-C time advance; "that evening" — explicit in scene-map; the naming scene on the lane Taylor has walked five hundred times
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
