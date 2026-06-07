facet: state-updates
episode: b01-c03
author: impersonator:jarvis-coin-kl-courier
target-scope: actor:jarvis-coin-kl-courier
---

1 @3 actor:jarvis-coin-kl-courier.contact-stage: out-of-scene -> observing-target
2 @6 actor:jarvis-coin-kl-courier.contact-stage: observing-target -> addressed-target
3 @8 actor:jarvis-coin-kl-courier.contact-stage: addressed-target -> coverage-named
4 @10 actor:jarvis-coin-kl-courier.contact-stage: coverage-named -> location-time-stated
5 @15 actor:jarvis-coin-kl-courier.location: lower-city-in-transit -> cooper-yard-eel-alley-three-steps-from-mouth
6 @15 actor:jarvis-coin-kl-courier.delivery-state: pre-delivery -> mid-delivery
7 @16 actor:jarvis-coin-kl-courier.contact-stage: location-time-stated -> patron-named-otto
8 @18 actor:jarvis-coin-kl-courier.contact-stage: patron-named-otto -> terms-delivered
9 @20 actor:jarvis-coin-kl-courier.contact-stage: terms-delivered -> sera-named
10 @27 actor:jarvis-coin-kl-courier.delivery-state: mid-delivery -> post-delivery-waiting
11 @31 actor:jarvis-coin-kl-courier.contact-stage: sera-named -> return-arrangement-confirmed
12 @32 actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley-three-steps-from-mouth -> lane-departed-unhurried
13 @32 actor:jarvis-coin-kl-courier.contact-stage: return-arrangement-confirmed -> departed

# field-extension: contact-stage, delivery-state — tracked operational-state aspects on actor:jarvis-coin-kl-courier; defended under §"Field-extension protocol" (courier function is the structured exchange transaction; the stages and delivery-state are the canonical record of where the transaction is, not perceptions or stylistic flourishes). location field is on-card (state.md baseline).
# Cross-facet contract: actor:jarvis-coin-kl-courier is non-POV (Taylor is POV per bones header). Narrator-interest co-citation NOT required for any entry per state-updates rubric §"Cross-axis tests" — non-POV actor-state shifts do not require narrator-interest co-citation.
# Persistence: every entry's <new> value persists past the anchor beat through chapter close OR until the next entry on the same field. contact-stage advances monotonically through the chapter (no reversions). location flips twice — into the yard at @15, out of the yard at @32. delivery-state moves pre → mid (@15) → post-waiting (@27); return-arrangement-confirmed is recorded on contact-stage at @31 because the verbal commit on the return is the contact-stage transition, not a delivery-state transition.
# Strip-test: every entry passes — without the fire, downstream canonical state would mis-track Jarvis's transactional progress through this delivery and his exposure-risk node-state for the d10 latent cost arrival.
# Peak-bones honored: scene-A peak @8 carries a state-update FIRE (entry 3 — coverage-named, the irreversible verbal commit). Scene-B peak @23 and scene-C peak @29 are Taylor-POV peaks and are not Jarvis fires; Jarvis's load-bearing scene-B fires concentrate on the @16/@18/@20 verbal-commit cluster (peak-shadow bones where Jarvis names Otto, terms, Sera in sequence). Scene-C @31 carries Jarvis's confirm-return commit (peak-shadow to @29).
# Held-against-turn honored: @4 (Taylor's feed registers Jarvis's stillness) NOT fired — that is Taylor-POV registration, not a Jarvis canonical change. @17, @22, @28, @30 NOT fired — Jarvis holds position without verbal commit (registration / posture-hold, not field-flip). @33 NOT fired — Jarvis has departed; no further state changes on him in-chapter.
# Frugality: 13 entries on 36 bones = 36% density on Jarvis target; rubric band is file-level 8-18% but that band is computed across all targets — for a single non-POV actor in a chapter where the actor's transactional progress IS the chapter substance, the contact-stage stair-step is the canonical record. Each step is a real irreversible verbal commit on a tracked operational field. No fires on motion-verbs without field-flip; no fires on registration beats; no fires on transient posture.
# Posture explicitly NOT fired as state: rubric §"Posture-as-state" requires multi-beat persistence AND load-bearing for next move. Jarvis's hands-at-sides posture is his baseline professional register (per card §Voice "courier-dryness" + §Look "Movement decisive and contained") — not a posture-state-change but his off-the-shelf posture. Firing hands-at-sides as state would be anti-pattern #8 (posture-as-state) and anti-pattern #10 (stylistic noting).
