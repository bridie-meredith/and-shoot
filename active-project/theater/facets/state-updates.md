---
facet: state-updates
sources: [env, coll-net-mender-flea-bottom, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates-env
episode: b01c01
author: studio
scope: environment / location / prop (studio domain only; actor-state is per-character fork)
---

1 @7 prop:pack.holder: taylor -> deposited-corner-room
2 @11 prop:basket.holder: unspecified -> taylor
3 @13 prop:needle.condition: unthreaded -> threaded
4 @16 studio.ambient.thermal: ambient-day -> cooling
5 @20 prop:net.condition: worked-extended -> folded

# source: coll-net-mender-flea-bottom
---
facet: state-updates
episode: b01-c01
target-class: actor:coll-net-mender-flea-bottom
author: impersonator-coll-net-mender-flea-bottom (facet-authoring mode, R1)
---

6 @8 actor:coll-net-mender-flea-bottom.social-engagement-with-taylor: unspoken-block-stranger -> minimal-verbal-exchanged # field-extension: social-engagement-with-taylor (new field for tracking first-touch verbal contact between block-fixture and Taylor; tracked-state aspect, not perception; persistence absolute past beat — they have spoken)
7 @12 actor:coll-net-mender-flea-bottom.work-state: between-days -> at-work-on-net # field-extension: work-state (new field for tracking daily-work-cycle; tracked-state aspect; @12 opens scene-B working-day cycle for Coll; persistence holds across @12-@19)
8 @20 actor:coll-net-mender-flea-bottom.work-state: at-work-on-net -> day-packed-net-folded # work-cycle close at end of scene-B working-day; persistence holds past beat (Coll is done for the day)

# source: taylor-hebert-kl-122ac
facet: state-updates
episode: b01-c01
author: taylor-hebert-kl-122ac (impersonator, facet-authoring mode)
target-scope: actor:taylor-hebert-kl-122ac.* only
---

9 @1 actor:taylor-hebert-kl-122ac.position: arrival-transient -> hook-district-corner-room
10 @2 actor:taylor-hebert-kl-122ac.lodging-payment-status: unpaid -> paid-current-period
11 @6 actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-geometry: arrival-baseline -> hook-block-route-mapped
12 @7 actor:taylor-hebert-kl-122ac.inventory.pack: carried -> grounded-at-corner-room
13 @8 actor:taylor-hebert-kl-122ac.social-state.with-coll: unobserved-block-fixture -> acknowledged-once-by-block-fixture
14 @13 actor:taylor-hebert-kl-122ac.inventory.needle: not-held -> in-hand
15 @20 actor:taylor-hebert-kl-122ac.inventory.needle: in-hand -> returned-to-work-set
16 @20 actor:taylor-hebert-kl-122ac.knowledge.coll-pattern: unread -> day-cycle-pattern-read
17 @25 actor:taylor-hebert-kl-122ac.social-state.with-wren: unknown-ward -> spoken-once
18 @29 actor:taylor-hebert-kl-122ac.inventory.needle: returned-to-work-set -> in-hand

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

# source: wren-stitch-maker-flea-bottom-ward
facet: state-updates
episode: b01-c01
author: impersonator-wren-stitch-maker-flea-bottom-ward
target-scope: actor:wren-stitch-maker-flea-bottom-ward
---

19 @22 actor:wren-stitch-maker-flea-bottom-ward.location: stitch-maker-household-hook-district -> flea-bottom-street-near-taylor
20 @23 actor:wren-stitch-maker-flea-bottom-ward.social-engagement: not-engaging -> engaging-taylor # field-extension: social-engagement (new field for scene-C wren-taylor interaction tracking; tracked-state-aspect per scene goal; persistence across @23-@27)
21 @28 actor:wren-stitch-maker-flea-bottom-ward.location: flea-bottom-street-near-taylor -> flea-bottom-street-crossed-away-from-taylor
22 @28 actor:wren-stitch-maker-flea-bottom-ward.social-engagement: engaging-taylor -> not-engaging
