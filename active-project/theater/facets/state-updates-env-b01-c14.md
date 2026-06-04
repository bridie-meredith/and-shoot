facet: state-updates-env / episode: b01-c14 / author: studio / ---

# Studio authors: studio.* and prop:*.* entries only.
# Actor-fork entries (actor:taylor.*) are NOT authored here.
# POV-restriction honored: actor-fork fields (ledger writing-acts as posture,
# stylus motor events, internal accounting beats) = actor-fork authority.
#
# Old-state baseline: b01c13 chapter-close
#   studio.time_of_day: morning (b01c13 state:11 @24)
#   studio.location: the-hook-lower-water-trough (b01c13 state:12 @24)
#   prop:oc-jarvis-packet: c14 incoming packet; seal-condition=sealed (by delivery
#     convention; c12/c13 precedent for sealed-delivery packets)
#   prop:oc-feed-ledger.breach-column-entry: threshold-filed (b01c12 state:15 @42;
#     held through c13 — no c13 breach-column entry fired)
#
# Field-extensions in this file (flag for margit):
#   prop:oc-response-sheet — new oc-prop (the outgoing confirmation sheet; no prior card)
#   prop:oc-feed-ledger.rushwick-cloth-stall-node-entry — new field on oc-feed-ledger
#   prop:oc-feed-ledger.cl04-outcome-entry — new field on oc-feed-ledger
#   prop:oc-feed-ledger.exit-column — new field on oc-feed-ledger
#   studio.fauna_sense_status.gap-lane-bottlefly-coverage — new sub-field on fauna_sense_status

1 @1 studio.location: the-hook-lower-water-trough -> oc-rushwick-cloth-stall
# Taylor's insect-feed circuit opens at the Rushwick cloth stall. Location change persistent
# through @9 (S01 close). No time-of-day advance (b01c13 closed at morning; b01c14 S01
# opens in working morning — same category; no fire on time_of_day).

2 @9 prop:oc-feed-ledger.rushwick-cloth-stall-node-entry: active -> foreclosed
# Taylor closes the passive-count entry for the cloth-merchant stall. Irreversible record
# mutation. Peak-bone @9 (S01 central event: passive-node foreclosed). First-touch field.
# # field-extension: prop:oc-feed-ledger.rushwick-cloth-stall-node-entry (new; c14 first-touch)

3 @10 studio.location: oc-rushwick-cloth-stall -> the-channel-station
# Taylor moves from the Rushwick circuit to the channel-station for the Jarvis packet.
# Location change persistent through S02-S03 (body remains at the channel-station through
# chapter-close; the S04 gap-lane observation is fauna-feed, not a body-location change).

4 @10 prop:oc-jarvis-packet.holder: jarvis-coin-kl-courier -> station-surface
# Jarvis deposits the c14 incoming packet at the station surface. Holder change persistent
# to @11. First-touch on c14 incoming packet.

5 @11 prop:oc-jarvis-packet.seal-condition: sealed -> broken
# Taylor breaks the seal on the incoming packet. Irreversible. Fires on the break-beat,
# not the approach (@10 deposit is approach; @11 seal-break is the canonical prop-mutation).

6 @28 prop:oc-response-sheet.seal-condition: unsealed -> wax-pressed
# Taylor presses the wax seal on the outgoing confirmation response-sheet. Irreversible
# prop-mutation. Peak-shadow bone for S03 (@28). First-touch on prop:oc-response-sheet.
# Old-state "unsealed" inferred from response-sheet being blank at @16 (set beside packet).
# # field-extension: prop:oc-response-sheet (new oc-prop; no prior warehouse card)

7 @29 prop:oc-response-sheet.position: working-surface -> station-edge
# Taylor sets the sealed response-sheet at the station edge for Jarvis pickup. Position
# change persistent through chapter-close (no departure bone in c14; see SEAM-C14-ENV-005).

8 @30 prop:oc-feed-ledger.breach-column-entry: threshold-filed -> cl04-added
# Taylor enters the cl04 breach-column record. Additive irreversible mutation: the breach
# column now holds both the threshold-filed entry (b01c12) and the cl04 confirmation record.
# Value "cl04-added" indicates both entries coexist in the column.

9 @32 studio.time_of_day: morning -> evening
# Time advance to the following evening (S04 scene-map header). Persistent through chapter-close.

10 @32 studio.fauna_sense_status.gap-lane-bottlefly-coverage: absent -> bottlefly-at-overhang-timber-active
# Bottlefly grips the overhang timber above the second junction of the east-water-gate
# gap-lane. First explicit placement of fauna coverage at this location.
# # field-extension: studio.fauna_sense_status.gap-lane-bottlefly-coverage (new sub-field; c14 first-touch)

11 @39 studio.fauna_sense_status.gap-lane-bottlefly-coverage: bottlefly-at-overhang-timber-active -> bottlefly-released
# Taylor releases the bottlefly after the detention resolves and the lane empties.
# Coverage at the second junction closes; gap-lane feed ends.

12 @40 prop:oc-feed-ledger.cl04-outcome-entry: open -> closed
# Taylor closes the cl04 outcome-entry. Peak-bone for S04 (@40 central event;
# relational_anchor +0.5). Irreversible record closure. First-touch field.
# # field-extension: prop:oc-feed-ledger.cl04-outcome-entry (new field; c14 first-touch)

13 @44 prop:oc-feed-ledger.exit-column: in-progress -> complete
# Taylor runs the exit-column to the bottom entry. Peak-shadow bone for S04 (@44;
# social_tether-antag completion witness). Terminal record event for the chapter's
# accounting arc. First-touch field.
# # field-extension: prop:oc-feed-ledger.exit-column (new field; c14 first-touch)

# Decisions-not-fire:
# @2-@8: S01 circuit-reading — insect sweeps and positioning are actor-fork/registration;
#   no persistent studio/prop field-flips until @9 node-foreclosure
# @12-@15: S02 feed-observation of the figure (rounds corner, raises chin, pauses,
#   adjusts strap) — feed-perception beats; actor-fork / narrator-interest authority;
#   no studio/prop field change distinct from @10 location-establishment
# @16-@19: response-sheet and stylus surface preparation — @16 packet repositioned
#   within station surface (sub-threshold; absorbed into @10 deposit); @17-@19 stylus
#   and hand positioning = actor-fork motor/posture
# @20-@27: accounting writing beats — actor-fork authority (writing acts, stylus movement,
#   wrist posture); no studio/prop field-flip; the written content is carried by prop
#   fields at the commit-beats @28-@30, not the intermediate writing gestures
# @31: stylus lifted above breach-entry — held-above (held-against-turn class; approach to
#   the S04 convergence; canon state does not flip at @31)
# @33-@38: feed-observed detention geometry — actor-fork / perception-feed; @38 lane-empty
#   is an environmental state but no tracked studio field maps to lane-occupancy-state;
#   registered through the bottlefly-coverage field at @39 instead
# @41-@43: column-positions held and hand-off-surface — actor-fork authority; no prop
#   field-change distinct from @40 cl04-close; the Wren-adjacent item is not entered
#   (W07: recognition present, text acknowledges, suppression active; no entry = the
#   canonical state; no prop field fires for the non-entry)
# @45: second-junction lane clears — environmental state captured in loc-state:4 @38;
#   no additional tracked studio field requires a writeback entry for the lane-clear
# @46: stylus released — actor-fork motor; terminal posture, not an irreversible prop
#   mutation; no prop position change that requires canonical writeback
#
# Density: 13/46 = 28%; above the mechanical s01e01 band (8-18%) consistent with
# b01c12 (38%) and b01c13 (42%) precedent; justified by 2×location-transition +
# 1×time-advance + 5×prop-mutations at peak/peak-shadow bones + 2×fauna-coverage
# changes + 1×node-foreclosure + 1×response-sheet-position.
# All 13 entries: Reality confirmed (persistent field-changes), Authority confirmed
# (studio domain: all studio.* and prop:*), Frugality confirmed (one per field per beat).

# SEAM-C14-ENV-001: prop:oc-response-sheet first-touch; no prior warehouse card;
#   old-state "unsealed" inferred from blank-response-sheet context; R2 confirm.
# SEAM-C14-ENV-002: prop:oc-jarvis-packet old-state "sealed" — inferred from delivery
#   convention (c12/c13 precedent); no explicit c14 upstream seal-state entry; R2 confirm.
# SEAM-C14-ENV-003: prop:oc-feed-ledger.breach-column-entry old-state "threshold-filed"
#   traces to b01c12 state:15 @42; held through c13 (no c13 breach-column fire);
#   chain unbroken; R2 confirm.
# SEAM-C14-ENV-004: Four new oc-feed-ledger fields — margit referrals needed for schema
#   extension documentation (rushwick-cloth-stall-node-entry, cl04-outcome-entry,
#   exit-column, breach-column-entry value extension).
# SEAM-C14-ENV-005: prop:oc-response-sheet.position holds at station-edge through
#   chapter-close; no c14 departure bone; showrunner note for c15: Jarvis collects
#   off-screen between chapters (consistent with sealed-packet-dispatch pattern).
# SEAM-C14-ENV-006: studio.location at chapter-close = the-channel-station (Taylor's
#   body; the gap-lane feed is a fauna_sense event, not a body-location change). This
#   differs from prior chapters where the feed-station and the channel-station may be
#   the same physical space — R2 confirm if the-channel-station and the-feed-station
#   are the same location slug or distinct. If the same, reconcile slug to whichever
#   is canonical (the-feed-station has b01c12 precedent across 6 entries).
