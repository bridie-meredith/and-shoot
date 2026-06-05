facet: state-updates-env
episode: b01c17
author: studio
---

# rubric-carve-out — solitary chapter: no actor-fork POV co-citation needed
#
# schemas/facet.schema.md § state updates
#
# Carve-out scope: all entries (no dialogue-writer actor-fork for this chapter)
# Carve-out rule: b01c17 is a solitary chapter (0 dialogue-anchor speakers; no on-stage
#   characters other than Taylor). Actor-state co-citation with the dialogue-writer fork is
#   N/A; all state-updates entries in this file are studio-only (env/prop). The
#   coverage-log entries at @22/@23/@28 record prop state, not actor state; they are within
#   studio authority.
# Coverage justification: scene-map header confirms "solitary chapter — Taylor alone;
#   Jarvis is a dead-drop courier channel, no on-page speech; 0 dialogue-anchor speakers."

1 @1 studio.time_of_day: morning -> dusk
2 @1 studio.location: oc-hook-precinct-circuit -> the-hook-lower-water-trough
3 @9 studio.time_of_day: dusk -> night
4 @9 studio.location: the-hook-lower-water-trough -> the-hook-southern-edge
5 @18 studio.location: the-hook-southern-edge -> the-tallow-render-works
6 @22 prop:oc-coverage-log.norren-attribution: absent -> first-line-written
7 @23 prop:oc-coverage-log.norren-attribution: first-line-written -> complete-three-lines
8 @28 prop:oc-coverage-log.condition: writing-active -> open-unreclosed
9 @29 studio.time_of_day: night -> morning
10 @29 studio.location: the-tallow-render-works -> the-gap-lanes-east-water-gate
11 @29 studio.dead-drop-channel.query-status: active -> quiet
12 @30 prop:apparatus-picture.norren-attribution: absent -> resolved
13 @34 prop:cost-ledger.protection-entry-column: in-progress -> blank-held

# Field notes and old-state lineage:
#
# state:1 @1 — studio.time_of_day old-state "morning" from b01c16 chapter-close (state.md:
#   "time_of_day: morning"). New-state "dusk" per scene-map s01 "dusk, end of a coverage circuit."
#
# state:2 @1 — studio.location old-state "oc-hook-precinct-circuit" from b01c16 chapter-close
#   (@27 circuit-resumed). New-state "the-hook-lower-water-trough" per bones locations: field
#   and scene-map s01 header. This slug is established in b01c13 loc-state:6 @24 — consistent
#   with the slug family.
#
# state:3 @9 — studio.time_of_day old-state "dusk" from state:1. New-state "night" per scene-map
#   s02 header "night, continuous from the dusk retrieval." @9 "taylor crosses the Hook's southern
#   edge" is the transitional bone that carries the dusk→night advance as the walk moves away
#   from the trough toward the s02 location.
#
# state:4 @9 — studio.location old-state "the-hook-lower-water-trough" from state:2. New-state
#   "the-hook-southern-edge" per bones locations: field and scene-map s02 header. The crossing
#   at @9 is the positioning verb that licenses this location-change.
#
# state:5 @18 — studio.location old-state "the-hook-southern-edge" from state:4. New-state
#   "the-tallow-render-works" per bones locations: field and scene-map s03 header. @18 "taylor
#   enters the room above the tallow-render works" — entry verb licenses this fire.
#   NOTE: No studio.time_of_day advance at @18; scene-map s03 is "continuous, the same night"
#   — the time_of_day remains "night" from state:3.
#
# state:6 @22 — prop:oc-coverage-log.norren-attribution first-touch; old-state "absent" = the
#   coverage-log held no Norren attribution before @22; the log's prior content was accurate
#   observation data (the eleven-day Wren entry-cluster). First-touch derives from the chapter
#   chunk: "she adjusts the network to screen the question — routes a different figure through
#   the gap documentation, attributes the gap-movements to a different ward-elder." The prop
#   oc-coverage-log is Taylor's personal coverage instrument (distinct from prop:oc-coverage-record
#   which is the circuit session record from b01c15; this is the log she maintains and submits
#   via Jarvis's channel). MARGIT REFERRAL: prop:oc-coverage-log requires new card authoring.
#
# state:7 @23 — prop:oc-coverage-log.norren-attribution old-state "first-line-written" from
#   state:6. New-state "complete-three-lines" per scene-map peak-bones @22+@23: "the first
#   Norren-attribution-line (@22), then the pen adds two supplementary observation lines (@23).
#   The false record now sits in the log." This is the prop's terminal irreversible state for
#   this chapter. NOTE: both collapse axes activate at @23 (position-prot-collapse -1.0 +
#   social_tether-prot-collapse -1.0); this prop state-change is the physical substrate of
#   both collapse-axis activations. Structural record: the false entry sits in the log; extraction
#   requires resolving what she wrote.
#
# state:8 @28 — prop:oc-coverage-log.condition old-state "writing-active" inferred from the
#   @19-@28 sequence (log pulled @19, entries written @22/@23, pen set down @24, log readied
#   @26, departed @28). New-state "open-unreclosed" per scene-map LEAVE-THE-OPEN-LOG
#   protected-pattern / DEC-0094 enactment-gate point 4: "she leaves the open log (@28 — the
#   entry unclosed, the enacted close)." The log is physically open; the entry is written but
#   the log has not been formally closed. This is a permanent state for the chapter-close
#   (the log is readied for the dead-drop at @26 as an open log segment).
#
# state:9 @29 — studio.time_of_day old-state "night" from state:3. New-state "morning" per
#   scene-map s04 header "three days after the deployment." The three-day gap is the
#   scene-map's explicit time-skip. @29 "the dead drop returns the quiet channel" is the
#   scene-open bone that opens s04.
#
# state:10 @29 — studio.location old-state "the-tallow-render-works" from state:5. New-state
#   "the-gap-lanes-east-water-gate" per scene-map s04 header and bones locations: field.
#   This slug is established in b01c14 loc-state:3 @32 and b01c15 (SEAM-C15-LOC-003). Taylor's
#   body is in the gap-lanes for the morning ward-read; @29's dead-drop-channel-quiet registers
#   there (the channel carries information observable from her ward-read position).
#
# state:11 @29 — studio.dead-drop-channel.query-status old-state "active" (the apparatus's
#   use-vector query was active from s01 delivery and through s02-s03). New-state "quiet" per
#   scene-map s04 header "The dead drop returns the quiet channel (@29) — no follow-up query,
#   the apparatus's question resolved against Norren." This is the environmental confirmation
#   that the protection succeeded through the channel. FIELD NOTE: new sub-field on
#   studio.dead-drop-channel; first-touch; old-state "active" inferred from s01 query-delivery
#   status. MARGIT REFERRAL: schema extension for studio.dead-drop-channel.
#
# state:12 @30 — prop:apparatus-picture.norren-attribution old-state "absent" (the apparatus
#   picture did not previously carry a Norren attribution; the gap-figure slot was pattern-only
#   from the original query, per scene-map s01: "The query is pattern-only — no name, no
#   description beyond height-and-gait"). New-state "resolved" per scene-map s04 peak-bone:
#   "the apparatus picture resolves the Norren attribution — relational_anchor +0.5: the
#   protection landed." @30 is the relational_anchor +0.5 co-cite bone. NOTE: this is the
#   downstream environmental confirmation of the prop:oc-coverage-log write at @22/@23: the
#   false attribution in the coverage-log has propagated to the apparatus's intelligence picture.
#   MARGIT REFERRAL: prop:apparatus-picture requires new card authoring; this is Otto's
#   intelligence picture of the east-of-water-gate gap-lanes (distinct from any prior prop).
#
# state:13 @34 — prop:cost-ledger.protection-entry-column old-state "in-progress" (the
#   cost-ledger's protection-entry column was open from @33 "taylor lifts the pen" — the
#   accounting was being held in suspension). New-state "blank-held" per scene-map ENACTED-
#   ABSENCE-POSITIVE-FORM protected-pattern / DEC-0094 enactment-gate point 4: "the cost-ledger
#   column holds the blank slot (@34 — the enacted absence, positive form: she runs the accounting
#   in her head and does not inscribe it; the blank IS the accounting)." The blank column is a
#   specific prop state: a column opened for inscription that was deliberately left unwritten.
#   This is selective non-recording — a different kind of information management. FIELD NOTE:
#   new prop; MARGIT REFERRAL: prop:cost-ledger (may be the same as prop:oc-feed-ledger or a
#   separate instrument; the bones and scene-map use "cost-ledger" specifically and distinguish
#   it from the coverage-log; reconcile at R2 with prior cost-accounting props in b01c12-b01c14).

# Decisions-not-fire:
#   @1/@2/@3/@4/@5/@6/@7/@8 — s01 loc/time fires land at @1; @2-@8 are retrieval/read/fold/
#     query-return/data-return/dexterity SVO; no persistent env/prop field-changes until @18 write
#   @9 fires two (loc + time-of-day) — the scene-transition from trough-dusk to edge-night; both
#     are structural fires on the same transitional bone; accepted per prior precedent (@1 in
#     b01c15/c16 fires two entries)
#   @10-@17 — s02 interior accounting; no persistent env/prop field-changes during the walk
#   @18 fires one (loc only) — time_of_day unchanged (still night per scene-map s03 "same night")
#   @19/@20 — coverage log pulled and returns cluster; dexterity + data-return; no field flip
#   @21 — opens Norren entry-cluster; interior-addressing of the log; no field change until @22
#   @24 — sets pen down; dexterity; no field change; @23 already records completion
#   @25 — coverage log carries attribution; confirmation bone; frugality-axis skip (state:7 @23
#     captures the completion; @25 is restatement)
#   @26 — readies updated log segment; staging-for-departure; field change is not distinct from
#     @28 open-unreclosed state which captures the departure condition
#   @27 — coverage log returns false-attribution-override-architecture-match; data-return; REJECT
#   @29 fires three (time + loc + dead-drop-channel) — major scene-transition (three-day skip);
#     three simultaneous field-changes on the scene-open bone; accepted per structural-fire logic
#   @31 — wren crosses the corridor; actor-position (Wren's body, not Taylor's); not studio
#     authority; corridor env unchanged from @29 loc-state
#   @32 — morning ward-read returns second-step hesitation; data-return; REJECT
#   @33 — taylor lifts the pen; dexterity (pen-lift); no field-change until @34 blank-held
#   @35 — coverage log keeps attribution; confirmation restatement of @23/@30; frugality-axis skip
#   @36 — accounting returns protection-override-architecture-match; data-return; REJECT

# Field-extensions (4 new fields / props; margit referrals noted above):
#   prop:oc-coverage-log (new prop; Taylor's personal coverage instrument — distinct from
#     prop:oc-coverage-record from b01c15; reconcile at R2)
#   prop:apparatus-picture (new prop; Otto's intelligence picture of the gap-lanes)
#   prop:cost-ledger (new prop or possible identity with prop:oc-feed-ledger; margit referral)
#   studio.dead-drop-channel.query-status (new sub-field)

# Density: 13/36 = 36.1%
# Justified by: 4×(location + time-of-day) = 8 structural scene-transition fires + 3 prop
#   lifecycle fires at central irreversible state-changes (@22/@23/@28) + 2 downstream
#   confirmation fires (@30/@34)
# Consistent with b01c13 (42%) and b01c14 (28%) precedent for chapters with dense prop lifecycles

# Seams for R2:
#   SEAM-C17-ENV-001: prop:oc-coverage-log first-touch — old-state "absent" for norren-attribution
#     and "writing-active" for condition both inferred from @19-@28 sequence; no prior card;
#     R2 confirm first-touch adequacy and reconcile with prop:oc-coverage-record (b01c15)
#   SEAM-C17-ENV-002: studio.dead-drop-channel.query-status old-state "active" inferred from
#     s01 channel-delivery; no explicit prior state-update records query-active onset; R2 confirm
#     inference adequacy
#   SEAM-C17-ENV-003: prop:apparatus-picture — new prop; no prior card; slug "apparatus-picture"
#     is inferred from scene-map "Otto's apparatus / the apparatus picture"; R2 confirm slug
#     or flag for margit
#   SEAM-C17-ENV-004: prop:cost-ledger — reconcile with prop:oc-feed-ledger from b01c12-b01c14
#     (these may be the same prop under a different name; the bones use "cost-ledger" which
#     suggests a separate instrument from the feed-ledger); margit referral at R2
#   SEAM-C17-ENV-005: studio.location @29 old-state "the-tallow-render-works" — Taylor's body
#     is at the tallow-render-works at chapter-close of s03 (@28); the three-day skip to @29
#     does not show Taylor's transit to the gap-lanes; the transition is implied by the time-skip
#     and the scene-map "three days after the deployment"; R2 confirm the location-change at @29
#     is the correct anchor for the transition (vs. an implied off-screen transit)
