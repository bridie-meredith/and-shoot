facet: state-updates
episode: b01-c01
author: taylor-hebert-kl-122ac (impersonator, facet-authoring mode)
target-scope: actor:taylor-hebert-kl-122ac.* only
---

1 @1 actor:taylor-hebert-kl-122ac.position: arrival-transient -> hook-district-corner-room
2 @2 actor:taylor-hebert-kl-122ac.lodging-payment-status: unpaid -> paid-current-period
3 @6 actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-geometry: arrival-baseline -> hook-block-route-mapped
4 @7 actor:taylor-hebert-kl-122ac.inventory.pack: carried -> grounded-at-corner-room
5 @8 actor:taylor-hebert-kl-122ac.social-state.with-coll: unobserved-block-fixture -> acknowledged-once-by-block-fixture
6 @13 actor:taylor-hebert-kl-122ac.inventory.needle: not-held -> in-hand
7 @20 actor:taylor-hebert-kl-122ac.inventory.needle: in-hand -> returned-to-work-set
8 @20 actor:taylor-hebert-kl-122ac.knowledge.coll-pattern: unread -> day-cycle-pattern-read
9 @25 actor:taylor-hebert-kl-122ac.social-state.with-wren: unknown-ward -> spoken-once
10 @29 actor:taylor-hebert-kl-122ac.inventory.needle: returned-to-work-set -> in-hand

# field-extension notes (per rubric § Field-extension protocol):
# - lodging-payment-status: new tracked-state field; persistent canonical (she is now a paying tenant of the corner-room; persists past the chapter)
# - knowledge.flea-bottom-geometry: tracked-state knowledge field; carries the substance_delta knowledge +0.5 increment
# - knowledge.coll-pattern: tracked-state knowledge field; observation accreted across a full working-day cycle, legible from this point forward
# - inventory.pack: pack is a generic possession (no prop card); ground vs carried is a tracked possession-state
# - inventory.needle: net-mending needle held during work; possession cycles within the chapter
# - social-state.with-coll: tracks the vouching threshold (block-fixture has acknowledged her once); persistent
# - social-state.with-wren: tracks the un-priced relationship-open (the chapter's central seam); persistent
#
# cull notes (per-file cull, delete-only):
# - dropped: @3 yard-crossing (transient locomotion within established residency; not a canonical position-shift past the @1 hook-district-corner-room residency-establishment)
# - dropped: @4 coll-lifts-eyes (transient eye-movement; the persistent acknowledgment-threshold lands at @8 spoken-to, not @4 looked-at)
# - dropped: @9 holds-the-feet (held-against-turn body-charge; posture-as-state anti-pattern unless persistent past-beat with load-bearing on next move; the stillness resolves into ordinary residency)
# - dropped: @11 basket-lifted (momentary motor; basket cycles within working-day with no persistent possession-state past the work-cycle close at @20)
# - dropped: @15 insects-fill-the-block (registration-as-state anti-pattern; insect-feed density is Taylor's perception of Flea Bottom baseline, not a tracked-field flip; capability axis at-rest per substance_delta)
# - dropped: @18 city-watch-passes-the-hook (transient visibility-to-watch; no persistent social-state change past the beat; capability deployment-threshold remains uncrossed = NON-event, no fire)
# - dropped: @19 holds-the-eyes (transient posture under watch-passage; eye-hold resolves within the beat)
# - dropped: @24 lifts-the-eyes (transient eye-movement registering wren's approach; NI territory)
# - dropped: @27 holds-the-eyes (transient posture during wren-exchange; the persistent social-state flip is at @25 spoken-to, not @27 held-gaze)
#
# capability-discipline NON-event (intentional silence):
# - insect-sense remains at-passive throughout chapter; deployment-threshold uncrossed at @15 (Flea Bottom density), @18 (watch passage), @22 (wren approach). substance_delta capability null, magnitude 0 -- NO fire on capability fields. The discipline holding is the chapter; the absence of a state-update on capability is the structural fact.
#
# POV co-citation expectation (R2 will resolve):
# - all 10 entries are NI-coverable on Taylor's POV (she registers each: arrival, payment, geometry-walked, pack-down, coll's first words, needle-in-hand, work-day-close + coll-pattern, wren's first words, needle-back-in-hand)
# - R1 stays blind to NI file; flagging here for cross-facet seam resolution
