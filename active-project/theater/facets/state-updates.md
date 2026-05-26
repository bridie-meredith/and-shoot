---
facet: state-updates
sources: [env, jarvis-coin-kl-courier, taylor-hebert-kl-122ac]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates-env
episode: b01c03
author: studio
scope: environment + location + prop only (actor-state authored separately)
---

1 @1 studio.time_of_day: dusk -> morning
# field-extension: time_of_day first-touch b01c03; b01c02 closed at dusk per studio state.md;
#   bone @1 opens the morning market — scene-A scene-map label "morning-market" confirms.

2 @1 studio.location: oc-stitch-house-lane-drain-angle -> morning-market-hook
# field-extension: location sub-state; b01c02 chapter-close had Taylor at drain-angle;
#   @1 opens in the Hook morning market — a different physical space within Flea Bottom.

3 @1 studio.foot_traffic: lane-end-quiet -> market-shoulder-to-shoulder
# field-extension: foot_traffic; bone @1 explicitly names shoulder-to-shoulder density;
#   persistent through all of scene-A (@1-@12); first-touch for this episode.

4 @6 studio.proposal_state: pre-contact -> contact-made
# field-extension: proposal_state; Jarvis speaks at @6 — contact is initiated and persists;
#   @6 is in scene-A rising zone, two bones before peak @8; not a held-against-turn bone;
#   strip-test passes: without this entry, state stays pre-contact through scene-A close.

5 @13 studio.location: morning-market-hook -> coopers-yard-eel-alley
# scene-B scene transition; bone @13 names the cooper's yard off Eel Alley explicitly;
#   persistent through scenes B and C until @32 departure.

6 @13 studio.foot_traffic: market-shoulder-to-shoulder -> coopers-yard-no-foot-traffic-past-third-bell
# bone @13 names the foot-traffic condition explicitly; the yard is clear of through-traffic;
#   persistent through scene-B and scene-C.

7 @15 studio.time_of_day: morning -> third-bell-noon
# bone @15 states Jarvis enters "at the third bell" — explicit time marker; persistent through
#   scene-B and scene-C; scene-map labels scene-B "cooper-yard-third-bell".

8 @23 studio.proposal_state: contact-made -> terms-known
# @23 is scene-B peak-bone (strongly expects co-citation); the prohibition engages as a term
#   on a ledger — the full terms have landed and are being calculated against;
#   strip-test passes: terms-delivery cluster @16-@22 delivers content; @23 is the
#   accounting-registration beat where the field flips.

9 @29 studio.proposal_state: terms-known -> deferred
# @29 is scene-C peak-bone; Taylor asks for a day — not refusal, not acceptance;
#   the proposal is actively deferred with a stated return-condition;
#   strip-test passes: without this entry, proposal_state stays terms-known through chapter close.

10 @36 studio.proposal_state: deferred -> answer-pending
# accounting-coda close (@34-@36 protected-pattern); Taylor leaves the yard;
#   chapter-close state is answer-pending (ledger open, return implicit);
#   distinction from deferred: @29 is active-deferral-in-progress; @36 is chapter-close
#   canonical state for b01c04 handoff — both parties have departed, the answer is in time.

# source: jarvis-coin-kl-courier
facet: state-updates
episode: b01-c03
author: impersonator:jarvis-coin-kl-courier
target-scope: actor:jarvis-coin-kl-courier
---

11 @3 actor:jarvis-coin-kl-courier.contact-stage: out-of-scene -> observing-target
12 @6 actor:jarvis-coin-kl-courier.contact-stage: observing-target -> addressed-target
13 @8 actor:jarvis-coin-kl-courier.contact-stage: addressed-target -> coverage-named
14 @10 actor:jarvis-coin-kl-courier.contact-stage: coverage-named -> location-time-stated
15 @15 actor:jarvis-coin-kl-courier.location: lower-city-in-transit -> cooper-yard-eel-alley-three-steps-from-mouth
16 @15 actor:jarvis-coin-kl-courier.delivery-state: pre-delivery -> mid-delivery
17 @16 actor:jarvis-coin-kl-courier.contact-stage: location-time-stated -> patron-named-otto
18 @18 actor:jarvis-coin-kl-courier.contact-stage: patron-named-otto -> terms-delivered
19 @20 actor:jarvis-coin-kl-courier.contact-stage: terms-delivered -> sera-named
20 @27 actor:jarvis-coin-kl-courier.delivery-state: mid-delivery -> post-delivery-waiting
21 @31 actor:jarvis-coin-kl-courier.contact-stage: sera-named -> return-arrangement-confirmed
22 @32 actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley-three-steps-from-mouth -> lane-departed-unhurried
23 @32 actor:jarvis-coin-kl-courier.contact-stage: return-arrangement-confirmed -> departed

# field-extension: contact-stage, delivery-state — tracked operational-state aspects on actor:jarvis-coin-kl-courier; defended under §"Field-extension protocol" (courier function is the structured exchange transaction; the stages and delivery-state are the canonical record of where the transaction is, not perceptions or stylistic flourishes). location field is on-card (state.md baseline).
# Cross-facet contract: actor:jarvis-coin-kl-courier is non-POV (Taylor is POV per bones header). Narrator-interest co-citation NOT required for any entry per state-updates rubric §"Cross-axis tests" — non-POV actor-state shifts do not require narrator-interest co-citation.
# Persistence: every entry's <new> value persists past the anchor beat through chapter close OR until the next entry on the same field. contact-stage advances monotonically through the chapter (no reversions). location flips twice — into the yard at @15, out of the yard at @32. delivery-state moves pre → mid (@15) → post-waiting (@27); return-arrangement-confirmed is recorded on contact-stage at @31 because the verbal commit on the return is the contact-stage transition, not a delivery-state transition.
# Strip-test: every entry passes — without the fire, downstream canonical state would mis-track Jarvis's transactional progress through this delivery and his exposure-risk node-state for the d10 latent cost arrival.
# Peak-bones honored: scene-A peak @8 carries a state-update FIRE (entry 3 — coverage-named, the irreversible verbal commit). Scene-B peak @23 and scene-C peak @29 are Taylor-POV peaks and are not Jarvis fires; Jarvis's load-bearing scene-B fires concentrate on the @16/@18/@20 verbal-commit cluster (peak-shadow bones where Jarvis names Otto, terms, Sera in sequence). Scene-C @31 carries Jarvis's confirm-return commit (peak-shadow to @29).
# Held-against-turn honored: @4 (Taylor's feed registers Jarvis's stillness) NOT fired — that is Taylor-POV registration, not a Jarvis canonical change. @17, @22, @28, @30 NOT fired — Jarvis holds position without verbal commit (registration / posture-hold, not field-flip). @33 NOT fired — Jarvis has departed; no further state changes on him in-chapter.
# Frugality: 13 entries on 36 bones = 36% density on Jarvis target; rubric band is file-level 8-18% but that band is computed across all targets — for a single non-POV actor in a chapter where the actor's transactional progress IS the chapter substance, the contact-stage stair-step is the canonical record. Each step is a real irreversible verbal commit on a tracked operational field. No fires on motion-verbs without field-flip; no fires on registration beats; no fires on transient posture.
# Posture explicitly NOT fired as state: rubric §"Posture-as-state" requires multi-beat persistence AND load-bearing for next move. Jarvis's hands-at-sides posture is his baseline professional register (per card §Voice "courier-dryness" + §Look "Movement decisive and contained") — not a posture-state-change but his off-the-shelf posture. Firing hands-at-sides as state would be anti-pattern #8 (posture-as-state) and anti-pattern #10 (stylistic noting).

# source: taylor-hebert-kl-122ac
facet: state-updates
episode: b01-c03
author: dialogue-writer-fork/taylor-hebert-kl-122ac
target-scope: actor:taylor-hebert-kl-122ac
---

24 @4 actor:taylor-hebert-kl-122ac.observation-status: anonymous -> observed-by-courier
25 @7 actor:taylor-hebert-kl-122ac.body-posture: market-mobile -> still-on-recognition
26 @8 actor:taylor-hebert-kl-122ac.observation-status: observed-by-courier -> observed-by-patron
27 @8 actor:taylor-hebert-kl-122ac.position-with-patron: anonymous -> courier-named-function
28 @8 actor:taylor-hebert-kl-122ac.tether-prot-rise-ledger: street-only -> court-layer-added-partial
29 @10 actor:taylor-hebert-kl-122ac.tether-prot-rise-ledger: court-layer-added-partial -> court-layer-added-full
30 @14 actor:taylor-hebert-kl-122ac.body-posture: still-on-recognition -> still-on-shed-wall
31 @19 actor:taylor-hebert-kl-122ac.feed-mode: ambient-passive -> actively-counting-inventory
32 @22 actor:taylor-hebert-kl-122ac.feed-mode: actively-counting-inventory -> mapping-against-coverage
33 @23 actor:taylor-hebert-kl-122ac.moral_framework-position: prohibition-as-fence -> prohibition-as-variable
34 @29 actor:taylor-hebert-kl-122ac.moral_framework-position: prohibition-as-variable -> prohibition-price-tagged
35 @31 actor:taylor-hebert-kl-122ac.position-with-patron: courier-named-function -> engaged-interlocutor
36 @33 actor:taylor-hebert-kl-122ac.feed-mode: mapping-against-coverage -> confirming-Jarvis-exit
37 @36 actor:taylor-hebert-kl-122ac.body-posture: still-on-shed-wall -> leaving-yard
38 @36 actor:taylor-hebert-kl-122ac.feed-mode: confirming-Jarvis-exit -> still-running

# field-extension: observation-status — tracked exposure-class field; tracks who has operational observation on Taylor (anonymous / observed-by-courier / observed-by-patron). Persistent across the chapter; load-bearing for the position_in_kl_smallfolk_anonymous → patron-visible trajectory.
# field-extension: position-with-patron — tracked structural-position field; tracks Taylor's defined position relative to Otto Hightower's apparatus via the courier interface (anonymous / courier-named-function / engaged-interlocutor). Tracks the social_tether-antag axis +1.5 movement and position-prot-rise axis +1.0 movement.
# field-extension: tether-prot-rise-ledger — tracked relationship-ledger field; tracks the cl01b court-layer accumulation across the chapter (street-only / court-layer-added-partial / court-layer-added-full). Two-stage @8/@10 because the offer arrives in two utterances; tracks social_tether-prot-rise +1.0.
# field-extension: moral_framework-position — tracked field-state for the moral_framework axis at this chapter's contract resolution (prohibition-as-fence / prohibition-as-variable / prohibition-price-tagged). Two transitions land at the scene-B peak (@23) and the scene-C peak (@29); together carry the moral_framework -1.0 axis movement.
# field-extension: feed-mode — tracked operational-register field for the insect-feed (ambient-passive / actively-counting-inventory / mapping-against-coverage / confirming-Jarvis-exit / still-running). Defensible as tracked-state per the chapter's substance contract — this is what feed-mode IS for Taylor at this episode; operational, not perceptual.
# field-extension: body-posture — tracked posture field with multi-beat persistence (market-mobile / still-on-recognition / still-on-shed-wall / leaving-yard). Each state load-bearing for the subsequent move; no transient posture-as-state contamination.

# Cross-facet contract: each actor:taylor.* entry requires narrator-interest co-citation at the same anchor. R2 verifies against narrator-interest-taylor-hebert-kl-122ac.md.
# Anchors expecting NI co-fire: @4, @7, @8, @10, @14, @19, @22, @23, @29, @31, @33, @36.

# Peak-bones honored: scene-A @8 (FIRE x3 — observation-status, position-with-patron, tether-prot-rise-ledger); scene-B @23 (FIRE — moral_framework); scene-C @29 (FIRE — moral_framework). All three peaks carry state-update support.
# Held-against-turn honored: @11 (peak-shadow for @8) — verbal agreement is narrator-interest territory, position-with-patron flip to engaged-interlocutor lands at the actual bidirectional confirmation @31, NOT at the verbal-agreement approach @11. @24 (peak-shadow for @23) — Taylor's I-have-heard-you acknowledgment; moral_framework canonical flip already at @23, no double-fire. @28 (peak-shadow for @29) — same physical posture as @14; no body-state flip.
# Strip-test: every entry passes — without the fire, downstream canonical state would mis-track the chapter's structural deltas across all four axes_in_motion (moral_framework -1.0, position-prot-rise +1.0, social_tether-antag +1.5, social_tether-prot-rise +1.0).
# Persistence: every entry's <new> persists past the anchor beat through chapter close OR until the next entry on the same field. observation-status locks at observed-by-patron from @8 forward; position-with-patron locks at engaged-interlocutor from @31 forward; tether-prot-rise-ledger locks at court-layer-added-full from @10 forward; moral_framework-position locks at prohibition-price-tagged from @29 forward; body-posture trajectory closes at leaving-yard @36; feed-mode closes at still-running @36 (carries into chapter-close transition).
