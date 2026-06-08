---
facet: state-updates
sources: [env-b01-c20, taylor-hebert-kl-122ac-b01-c20]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env-b01-c20
facet: state-updates
episode: b01c20
author: studio
---

# Prior state (b01c19 chapter-close):
#   studio.location: the-tallow-render-works
#   studio.time_of_day: after-third-bell
#   studio.cost-ledger.condition: closed-column-drop-complete
#   studio.fauna_sense_status.coverage-scale: standdown-complete
#   studio.fauna_sense_status.eastern-gap-status: closed-at-standdown (carry from c18; @37)
#   prop:oc-stylus.position: beside-ledger-edge-closed-column (carry from c19 @26)
#   prop:oc-running-architecture-record.condition: closed-daven-node-removed (c19 @35)
#   prop:oc-coverage-map.daven-node: dropped (c19 @34)
#   prop:apparatus-picture.norren-attribution: resolved (carry; unchanged)
#   prop:oc-coverage-log.norren-attribution: complete-three-lines (carry; unchanged)
#   studio.succession-document-status: cleared-small-council-access-window (carry from c18)
#
# NOTE — chapter-open time skip:
#   b01c19 closed at after-third-bell. b01c20 opens before-dawn on a new chapter-day;
#   scene-A is "before-dawn" per scene-map. The skip is structural; no explicit
#   time-between-chapters bone; time-of-day resets at @1 (scene-open structural fire).
#
# NOTE — prop-card referrals:
#   prop:oc-ledger: the accounting ledger Taylor opens/marks across scenes A, C, E
#     (entries @4/@5, @16/@17, @29). Using studio.oc-ledger.* form consistent with
#     the cost-ledger sub-field pattern established in c17-c19. MARGIT REFERRAL
#     RECOMMENDED to canonicalize the c20 ledger as the terminal accounting prop
#     (distinct from cost-ledger, which was the running-column instrument; this is
#     the chapter-close ledger Taylor runs at departure).
#   prop:oc-decommission-message: first-touch in this chapter (@14). No prior
#     warehouse card. MARGIT REFERRAL RECOMMENDED.
#   prop:oc-stylus: carry from c19 @24-@26 (beside-ledger-edge-closed-column);
#     reactivated at c20 @4 (lifted) and @24 (lifted again, without opening a
#     ledger line — the held-stylus-without-entry is the recognition-blank shape).
#   prop:oc-pack: first-touch in this chapter (@28). No prior warehouse card.
#     MARGIT REFERRAL RECOMMENDED.

# --- ENTRIES ---

# Scene-open: new chapter-day, same location, time reset
# @1 — the servant-passages empty (scene-A; before-dawn; the-rendering-works-room)
# Time advances from after-third-bell (b01c19 close) to before-dawn (new chapter-day).
# Location unchanged (the-tallow-render-works / rendering-works-room).
# Chapter opens with Taylor already monitoring the Red Keep servant-passage feed;
# the before-dawn time-reset is the scene-open structural fire.
1 @1 studio.time_of_day: after-third-bell -> before-dawn

# @3 — the holdfast routes activate (scene-A; before-dawn; apparatus executes)
# The Green succession move executes in Taylor's feed: the Holdfast access routes
# (mapped and delivered through the Jarvis channel) show new traffic — rehearsed
# sequence activating. The holdfast-routes activation is a tracked world-state
# field: the apparatus's succession-mechanism routes are now live.
# This is the world-state confirmation that the succession machine is running.
# Field-extension: studio.apparatus-holdfast-routes.status (new; first-touch; the
#   routes Taylor mapped and delivered are now an active apparatus-state field;
#   MARGIT REFERRAL RECOMMENDED — confirm against studio.succession-document-status
#   and apparatus route-state sub-fields from c18).
2 @3 studio.apparatus-holdfast-routes.status: dormant -> active
  # field-extension: studio.apparatus-holdfast-routes.status (new; MARGIT REFERRAL)

# @4 — taylor lifts the stylus (scene-A; before-dawn; ledger opens)
# Stylus moves from beside-ledger-edge-closed-column (b01c19 chapter-close state)
# to in-hand. This is the ledger-accounting choreography beginning: the same
# shape as c19 @24 (lift) but now opening a new session, not closing one.
3 @4 prop:oc-stylus.position: beside-ledger-edge-closed-column -> in-hand

# @5 — taylor marks the ledger (scene-A; before-dawn; succession + position entries)
# The ledger receives entries for both the position-world and political_register-world
# draws confirmed at this scene (@1/@3 peak-bones). The ledger's condition changes
# from closed (carry state from c19) to open-entries-in-progress.
# Prior state: studio.cost-ledger.condition = closed-column-drop-complete (c19 @23).
# In b01c20 the accounting instrument is the terminal ledger (not a running column);
# using studio.oc-ledger.condition to distinguish from the prior cost-ledger sub-fields.
# Field-extension: studio.oc-ledger.condition (new sub-field; distinct from
#   studio.cost-ledger.* which tracked the running column; this tracks the terminal
#   accounting ledger Taylor opens at c20; MARGIT REFERRAL RECOMMENDED).
4 @5 studio.oc-ledger.condition: closed -> open-succession-entries-in-progress
  # field-extension: studio.oc-ledger.condition (new; MARGIT REFERRAL)

# @6 — the succession bell rings (scene-B; morning; time advance)
# The succession bell marks morning: time advances from before-dawn to morning.
# The bell is the public announcement of Viserys's death and the Green succession.
5 @6 studio.time_of_day: before-dawn -> morning

# @8 — the patron channel shifts sequence (scene-B; morning; patronage dissolving)
# The patron channel is no longer running Taylor-active delivery; it has shifted
# to a sequence that does not require her signal. This is a tracked structural
# state: the patron channel's operational sequence has changed.
# Field-extension: studio.patron-channel.sequence (new sub-field; first-touch at
#   c20; the patron channel as a tracked env-state field; previously represented
#   through studio.succession-document-status and cost-ledger entries; MARGIT
#   REFERRAL RECOMMENDED — confirm against dead-drop channel sub-fields from c17).
6 @8 studio.patron-channel.sequence: taylor-active-delivery -> autonomous-apparatus-sequence
  # field-extension: studio.patron-channel.sequence (new; MARGIT REFERRAL)

# @10 — taylor opens the feed (scene-B; morning; feed active in east-of-water-gate lanes)
# Taylor opens the insect-feed in the east-of-water-gate lanes, the coverage gap she
# maintained open through every ward-expansion. The fauna_sense_status transitions
# from standdown-complete (c18/c19 carry; the network was at standdown after the
# fortnight deployment closed) to active-lower-city-coverage. This is the full-
# deployment reactivation at the chapter opening.
# Prior state: studio.fauna_sense_status.coverage-scale = standdown-complete (carry from c18/c19).
7 @10 studio.fauna_sense_status.coverage-scale: standdown-complete -> active-lower-city-coverage
  # NOTE: the eastern-gap-status (studio.fauna_sense_status.eastern-gap-status: closed-at-standdown
  #   from c18 @37) transitions back to open here — the gap Taylor maintained through the fortnight
  #   is her running it again. Using coverage-scale as the primary field; gap-status sub-entry below.
8 @10 studio.fauna_sense_status.eastern-gap-status: closed-at-standdown -> open-wren-lanes-active

# @12 — the burn reaches the outer wards (scene-C; midday; fire arrives)
# Time advance: morning → midday (scene-C per scene-map).
# The burn reaching the outer wards is a tracked ambient-condition state change:
# fire is now present in the outer-ward zone. The Dance ignition's physical
# consequences have reached Taylor's coverage area.
9 @12 studio.time_of_day: morning -> midday
10 @12 studio.ambient_conditions.outer-ward-burn: absent -> active-burn-reaching
  # field-extension: studio.ambient_conditions.outer-ward-burn (new sub-field; first-touch;
  #   the Dance's physical fire as a tracked ambient-condition; MARGIT REFERRAL RECOMMENDED)

# @13 — the fire traces the ward-junction catalogue (scene-C; midday; fire propagates)
# The burn propagates through the exact ward-junction catalogue Taylor built and
# delivered. The outer-ward-burn transitions from reaching to propagating-through-catalogue.
# The burn-line is now tracing Taylor's own architecture.
11 @13 studio.ambient_conditions.outer-ward-burn: active-burn-reaching -> propagating-through-ward-catalogue

# @14 — the decommission message arrives (scene-C; midday; apparatus closes)
# The decommission message arrives through a non-Jarvis channel.
# First-touch prop: prop:oc-decommission-message enters the scene.
# Field-extension: prop:oc-decommission-message (new oc-prop; first-touch; MARGIT REFERRAL).
12 @14 prop:oc-decommission-message.status: absent -> delivered
  # field-extension: prop:oc-decommission-message (new oc-prop; first-touch; MARGIT REFERRAL)

# @15 — the apparatus network absorbs the coverage (scene-C; midday; network transferred)
# The apparatus absorbs Taylor's coverage into its own network. The fauna_sense_status
# changes: Taylor's active-lower-city-coverage is now being absorbed by the apparatus
# (the network outlasts its architect). This is the coverage-transfer state change.
13 @15 studio.fauna_sense_status.coverage-scale: active-lower-city-coverage -> absorbed-into-apparatus-network

# @16 — taylor opens the ledger (scene-C; midday; decommission accounting begins)
# The ledger opens for the decommission entries (social_tether and position entries).
# Prior state: studio.oc-ledger.condition = open-succession-entries-in-progress (from @5).
# Now transitions to open-decommission-accounting.
14 @16 studio.oc-ledger.condition: open-succession-entries-in-progress -> open-decommission-accounting

# @17 — taylor marks the social_tether entry (scene-C; midday; tether severed on record)
# The social_tether entry is marked in the ledger: patron channel closed, network
# transferred, tether severing. The ledger receives the terminal tether entry.
# The ledger's condition advances to decommission-entries-marked.
15 @17 studio.oc-ledger.condition: open-decommission-accounting -> open-decommission-entries-marked

# Scene-D: time advance (morning → afternoon not yet explicit; scene-map says "afternoon")
# The scene-map names scene-D as "afternoon." The time advance from midday to afternoon
# fires at the scene-D open, before @18 (where the feed is running normally — an
# established state at scene-D open). Anchoring the time advance at @18 (scene-D
# first bone) as the structural scene-open fire.
16 @18 studio.time_of_day: midday -> afternoon

# @19 — the smoke fills the east-of-water-gate lanes (scene-D; afternoon; physics cascade)
# Smoke arrives in the east-of-water-gate lanes. This is an ambient-condition change
# in the lanes: smoke is now present, the first step of the physics mechanism that
# disperses the insect-feed.
# Field-extension: studio.east-of-water-gate-lanes.ambient: clear -> smoke-present
# (new sub-field; the lanes' specific ambient condition as a tracked state; distinct
#  from the outer-ward-burn ambient which tracks the broader fire; MARGIT REFERRAL).
17 @19 studio.east-of-water-gate-lanes.ambient: clear -> smoke-present
  # field-extension: studio.east-of-water-gate-lanes.ambient (new; MARGIT REFERRAL)

# @22 — the signal drops from the lanes (scene-D; afternoon; feed-signal loss)
# The insect-feed signal drops from the east-of-water-gate lanes. The
# fauna_sense_status transitions: the lanes that were active-open (Taylor's coverage
# gap held open for Wren) go to signal-dropped. This is the recognition-event's
# physical precondition.
18 @22 studio.fauna_sense_status.eastern-gap-status: open-wren-lanes-active -> signal-dropped

# @23 — the east-of-water-gate lanes go blank (scene-D; afternoon; feed blank)
# The lanes go blank in the feed. The fauna_sense_status for the eastern gap
# transitions from signal-dropped to blank. The recognition event is complete.
19 @23 studio.fauna_sense_status.eastern-gap-status: signal-dropped -> blank-recognition-complete

# @25 — taylor closes the feed (scene-E; dusk; feed closure enacted)
# Time advance: afternoon → dusk (scene-E per scene-map).
# Taylor closes the insect-feed before departure. The fauna_sense_status transitions
# from absorbed-into-apparatus-network (the broader coverage) + blank (eastern gap)
# to feed-closed-dispersing-to-substrate. The architecture she built over eleven
# months returns to ambient range.
20 @25 studio.time_of_day: afternoon -> dusk
21 @25 studio.fauna_sense_status.coverage-scale: absorbed-into-apparatus-network -> feed-closed-dispersing-to-substrate

# @27 — the architecture releases the wards (scene-E; dusk; network dissolved)
# The coverage architecture releases — the insects disperse below surveillance
# threshold; the network returns to substrate. The final coverage-scale state:
# the architecture that ran for eleven months is dissolved.
22 @27 studio.fauna_sense_status.coverage-scale: feed-closed-dispersing-to-substrate -> dispersed-below-threshold
23 @27 studio.fauna_sense_status.eastern-gap-status: blank-recognition-complete -> dispersed-with-coverage

# @29 — taylor runs the ledger (scene-E; dusk; final ledger run)
# Taylor runs the full ledger at the gate. The ledger transitions from
# open-decommission-entries-marked to final-run-complete — the terminal accounting.
# This is the ledger-close event before departure.
24 @29 studio.oc-ledger.condition: open-decommission-entries-marked -> final-run-complete

# @30 — taylor exits the south gate (scene-E; dusk; location departure)
# Taylor exits through the south gate — she leaves King's Landing. Location changes
# from the-rendering-works-room to south-gate (and then departed KL). This is the
# chapter-terminal location change.
25 @30 studio.location: the-tallow-render-works -> south-gate-departed

# --- DECISIONS-NOT-FIRE ---
# @2 (the doors open — the Holdfast doors opening is registered in the feed; the
#   door-state is Red Keep location-content at distance, not a tracked field in
#   Taylor's control-point space; @3 holdfast-routes-activate captures the apparatus
#   state change; @2 is approach to @3 peak-bones; held-against-turn class for any
#   canonical state-update beyond the @3 fire)
# @4 stylus prop: the ledger-marking at @5 captures the ledger condition state
#   change; the @4 stylus-lift is the choreography precondition; prop:oc-stylus
#   fired at @4 (entry 3 above); no additional fire needed at @5 (stylus held
#   in-hand through the marking sequence — the ledger-condition fire is the
#   relevant field-change at @5)
# @7 (men enter ward junctions — the men are feed-observed actors moving through
#   Taylor's coverage; actor-fork authority; no studio/prop field changes at this
#   bone; factional-violence entering lower-city is the scene-B content, tracked
#   through patron-channel @8 and feed-coverage @10; no env field directly changes
#   at @7 beyond the ongoing actor-movement through existing routes)
# @9 (gate-side routes fill — the routes filling is the feed showing factional
#   movement through Taylor's own catalogued passage-counts; the routes are coverage-
#   content, not a discrete tracked field-change distinct from @10 feed-open; no
#   additional env field-change; frugality: @10 captures the coverage-state change)
# @11 (faction-movement follows the passage-counts — routes-become-roadmap
#   recognition beat; no new env/prop field changes; the catalogue being used as
#   a map is a world-state observation, not a discrete field mutation; registered
#   through actor-fork narrator-interest, not state-updates)
# @20 (heat disperses the insects — heat is the physics mechanism enabling @22
#   signal-drop; the heat itself is not a separately tracked sub-field from the
#   smoke-present ambient established at @19; the physics cascade is @19→@20→@21→@22;
#   @19 smoke-present captures the ambient change; @22 signal-dropped captures the
#   outcome; @20 and @21 are interior physics steps; pre-emption rule: fire on the
#   beat where the field flips)
# @21 (insects scatter — interior physics step in the cascade; covered by @22
#   signal-dropped; frugality: no distinct tracked field changes at @21)
# @24 (taylor lifts the stylus — the held-stylus-without-entry is the recognition-
#   blank shape; no ledger line opens; the stylus lift is actor-movement; the
#   ledger condition at @17 (open-decommission-entries-marked) is unchanged by @24
#   because no entry is written; no prop field-change fires at @24 — the ABSENCE
#   of a ledger-line is the scene's argument, not a positive field-mutation)
# @26 (insects disperse — the dispersal is the physical consequence of @25 feed-
#   close; the coverage-scale was already set to feed-closed-dispersing-to-substrate
#   at @25; @26 is the confirmation/interior step before @27 architecture-releases;
#   frugality: @25 and @27 capture the bracketing state changes)
# @28 (taylor lifts the pack — actor-fork authority for Taylor's position/inventory;
#   the pack as a prop: prop:oc-pack first-touch, but the lift is actor-state, not
#   a studio prop field; if margit creates a prop:oc-pack card, the holder/position
#   field-change would be studio's domain; flagging as MARGIT REFERRAL — if a
#   prop:oc-pack card is created, a state-update entry fires at @28: pack.position:
#   floor-or-storage -> in-hand; deferred pending card existence)
# @18 (insect-feed runs in east-of-water-gate lanes — the feed's active state in
#   those lanes was established at @10 feed-open; @18 is the scene-D confirmation
#   of an already-established coverage state; the time-of-day fire is anchored at
#   @18 as scene-open structural fire; the feed-active state itself does not fire
#   again since the field is already at open-wren-lanes-active from @10)

# --- SUMMARY ---
# 25 entries on 30 bones = 83.3%; above the c18/c19 precedent range.
# Density justified by:
#   - 3 scene-open structural fires: time-of-day advance (@1 before-dawn; @6 morning;
#     @9 midday; @16 afternoon; @20 dusk) = 5 time-of-day fires across 5 scene transitions
#     (all scene-map scene-open structural fires; the chapter spans a full day arc)
#   - 1 location-departure fire (@30 south-gate)
#   - 2 coverage-scale fires (@10 active-lower-city; @15 absorbed; @21/@27 closed→dispersed = 4)
#   - 2 eastern-gap-status fires (@10 open; @22 signal-dropped; @23 blank; @27 dispersed = 4)
#   - 2 ledger lifecycle fires (@5 open-succession; @14 decommission-accounting; @15 entries-
#     marked; @24 final-run = 4)
#   - 3 apparatus/env one-off fires: @3 holdfast-routes; @8 patron-channel; @12 burn-reaching;
#     @13 burn-propagating; @14 decommission-message; @19 smoke-present = 6
# The time-of-day arc (5 fires across 5 scenes = before-dawn→morning→midday→afternoon→dusk)
# is the structural backbone of this chapter's state-updates density. The full-day arc is
# the succession/departure environmental timeline and cannot be compressed. Coverage-state
# and ledger-state fires decompose an important lifecycle in the chapter's architecture.
# Field-extensions: studio.apparatus-holdfast-routes.status (new); studio.oc-ledger.condition
#   (new; distinct from studio.cost-ledger.*); studio.patron-channel.sequence (new);
#   studio.ambient_conditions.outer-ward-burn (new); studio.east-of-water-gate-lanes.ambient
#   (new); prop:oc-decommission-message (new); 6 new fields/props requiring MARGIT REFERRAL.

# source: taylor-hebert-kl-122ac-b01-c20
facet: state-updates
episode: b01c20
author: taylor-hebert-kl-122ac
---

# Prior state (b01c18/c19 carry — actor-fork scope only):
#   actor:taylor-hebert-kl-122ac.position: at-the-ledger (control-point; the-rendering-works-room)
#   actor:taylor-hebert-kl-122ac.feed-deployment: full-architecture-running (eleven-month KL build, held wide)
#   actor:taylor-hebert-kl-122ac.standing-in-apparatus: instrument-load-bearing (Otto's unofficial conduit)
#   actor:taylor-hebert-kl-122ac.pack: none (no travel-state)
#   actor:taylor-hebert-kl-122ac.capability_deployment_threshold: run-at-full-density (carry from b01c18 state1)
#   actor:taylor-hebert-kl-122ac.position-prot-collapse: in-descent (terminal arc opened b01c17/c18)
#
# NOTE — actor-fork authority: this file writes ONLY actor:taylor-hebert-kl-122ac.* entries.
#   Prop lifecycle (stylus, ledger, feed-as-prop), location, and time fires are studio's domain
#   (see state-updates-b01-c20.md studio-fork). The Taylor fork tracks her own posture/position,
#   her deployment-of-capability as an actor-state, her standing, and her travel-state.
#
# NOTE @24 — RECOGNITION-WITHOUT-ENTRY: at @24 Taylor lifts the stylus and does NOT mark.
#   This is a suspended-action state, not a registration. The actor-state field that flips is
#   her ledger-work-posture (marking -> stylus-lifted-no-line-opened), persistent across @24
#   until the feed closes at @25. It is NOT a "noticed/registered/awareness" value — it is the
#   physical held-blank: the stylus is up, the line is not opened, and it stays not-opened.

# --- ENTRIES ---

# @14 — the decommission message arrives (s03; midday; peak-bone)
# Taylor's standing in the apparatus flips: the function is declared concluded, the instrument
# expendable. position-of-no-exit becomes position-of-no-use. Persistent — she is never re-tasked.
# Peak-bone (position-prot-collapse axis_move mag 2). co-cites narrator @14 (the decommission read).
26 @14 actor:taylor-hebert-kl-122ac.standing-in-apparatus: instrument-load-bearing -> decommissioned-function-concluded  # cl07b; position-prot-collapse draw; the message addresses the function, not the person — standing held no longer.

# @17 — taylor marks the social_tether entry (s03; midday)
# Her ledger-work-posture is active-marking: she enters the patron-channel-closed / network-transferred
# line. The entries are accurate; she does not redraft. The marking-state persists until the held-blank @24.
# co-cites narrator @17 (the accurate entry written without revision).
27 @17 actor:taylor-hebert-kl-122ac.ledger-work-posture: at-rest-stylus-set -> active-marking  # cl07a; the tether-severance entry written accurate, no redress.

# @24 — taylor lifts the stylus (s04; afternoon; RECOGNITION-HELD-BLANK)
# The recognition arrives as the feed-blank in the lanes she held open. Taylor lifts the stylus and
# does NOT open a line. ledger-work-posture flips from active-marking to stylus-lifted-no-line-opened —
# the suspended-action state. Persistent: the line stays not-opened through the rest of the scene.
# This is the held-blank, the one event her accounting cannot contain because the item was never priced.
# co-cites narrator @24 (the absence of signal in the place she held open).
28 @24 actor:taylor-hebert-kl-122ac.ledger-work-posture: active-marking -> stylus-lifted-no-line-opened  # cl07a/cl07c; recognition-without-entry; the un-priced item is the one the calculus came for; no line opened, and it stays not-opened.

# @25 — taylor closes the feed (s05; dusk; peak-bone)
# Her deployment-of-capability flips: the architecture she built over eleven months disperses to
# ambient range, below surveillance threshold. What was hers is no longer held. Persistent and terminal —
# the network is not re-deployed. This is the final capability act. co-cites narrator @25 (what disperses is what was hers).
29 @25 actor:taylor-hebert-kl-122ac.feed-deployment: full-architecture-running -> closed-dispersed-to-substrate  # cl07b; the coverage she held herself is released; the apparatus-absorbed network is theirs, not hers.

# @28 — taylor lifts the pack (s05; dusk)
# Her travel-state flips: from no-pack (resident, anchored to the control-point) to packed-for-departure.
# Persistent — she carries it through the gate. The first physical act of leaving. co-cites narrator @28
# (the pack and no coin above subsistence).
30 @28 actor:taylor-hebert-kl-122ac.pack: none -> lifted-for-departure  # cl07a; travel-state opens; the instrument readies to leave the city it was decommissioned from.

# @29 — taylor runs the ledger (s05; dusk; LEDGER-CLOSE-DEPARTURE)
# Her ledger-work-posture flips one last time: from stylus-lifted-no-line-opened (the held-blank) to
# final-full-run-no-error. She runs the whole accounting at the gate — not to find an error, because
# there is none; the accuracy is the record of what she did and what she refused to price. Persistent:
# the ledger is closed-complete after this. co-cites narrator @29 (the ledger accurate, nothing to refuse).
31 @29 actor:taylor-hebert-kl-122ac.ledger-work-posture: stylus-lifted-no-line-opened -> final-full-run-closed-complete  # cl07a; the contempt complete, the recognition complete, nothing in the ledger to refuse.

# @30 — taylor exits the south gate (s05; dusk; peak-bone; position-prot-collapse LOCK rank 1)
# Her position and standing both reach terminal: from at-the-control-point to departed-south-gate-unregistered.
# position-prot-collapse LOCKS at rank 1 — instrument decommissioned and departed, not on any record the
# apparatus keeps. Persistent and absolute (series-terminal). co-cites narrator @30 (departure through the
# south gate, the person leaving is not on any record).
32 @30 actor:taylor-hebert-kl-122ac.position: at-the-control-point-rendering-works -> departed-south-gate-unregistered  # cl07b; position-prot-collapse LOCK rank 1; the function concluded, the person gone, the city behind her.
