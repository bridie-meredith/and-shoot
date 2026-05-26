facet: state-updates
episode: b01-c03
author: dialogue-writer-fork/taylor-hebert-kl-122ac
target-scope: actor:taylor-hebert-kl-122ac
---

1 @4 actor:taylor-hebert-kl-122ac.observation-status: anonymous -> observed-by-courier
2 @7 actor:taylor-hebert-kl-122ac.body-posture: market-mobile -> still-on-recognition
3 @8 actor:taylor-hebert-kl-122ac.observation-status: observed-by-courier -> observed-by-patron
4 @8 actor:taylor-hebert-kl-122ac.position-with-patron: anonymous -> courier-named-function
5 @8 actor:taylor-hebert-kl-122ac.tether-prot-rise-ledger: street-only -> court-layer-added-partial
6 @10 actor:taylor-hebert-kl-122ac.tether-prot-rise-ledger: court-layer-added-partial -> court-layer-added-full
7 @14 actor:taylor-hebert-kl-122ac.body-posture: still-on-recognition -> still-on-shed-wall
8 @19 actor:taylor-hebert-kl-122ac.feed-mode: ambient-passive -> actively-counting-inventory
9 @22 actor:taylor-hebert-kl-122ac.feed-mode: actively-counting-inventory -> mapping-against-coverage
10 @23 actor:taylor-hebert-kl-122ac.moral_framework-position: prohibition-as-fence -> prohibition-as-variable
11 @29 actor:taylor-hebert-kl-122ac.moral_framework-position: prohibition-as-variable -> prohibition-price-tagged
12 @31 actor:taylor-hebert-kl-122ac.position-with-patron: courier-named-function -> engaged-interlocutor
13 @33 actor:taylor-hebert-kl-122ac.feed-mode: mapping-against-coverage -> confirming-Jarvis-exit
14 @36 actor:taylor-hebert-kl-122ac.body-posture: still-on-shed-wall -> leaving-yard
15 @36 actor:taylor-hebert-kl-122ac.feed-mode: confirming-Jarvis-exit -> still-running

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
