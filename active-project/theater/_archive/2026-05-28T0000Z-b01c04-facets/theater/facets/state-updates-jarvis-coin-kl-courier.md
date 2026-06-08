facet: state-updates
episode: b01c04
author: impersonator:jarvis-coin-kl-courier
slice: actor:jarvis-coin-kl-courier.*
---

# rubric-carve-out — none; baseline V2 rubric § actor-state applies.
#
# Field-extensions (per §"Field-extension protocol" of rubric-state-updates.md):
#   - actor:jarvis-coin-kl-courier.stats.active_deliveries (new) — integer counter tracking live
#       delivery assignments in-progress; operational load indicator; not a standard actor-state
#       field on jarvis-coin-kl-courier's state.md baseline; field-extension justified as a
#       tracked-state-aspect (irreversible increment at each accept-delivery event; persistence
#       required for downstream chapter continuity); NOT perception/mood/register.
#   - actor:jarvis-coin-kl-courier.stats.exposure_risk (new) — categorical risk tier tracking
#       operational exposure level for the courier once he physically carries Taylor's intelligence;
#       field-extension justified as a tracked-state-aspect (latent → operational flip is an
#       irreversible canonical state change that chapter handoff_out must propagate); NOT perception/
#       mood/register.
#   Both field-extensions are propagated by chapter handoff_out (memory.md chapters[b01c04].
#   handoff_out.character_state / open_threads) per the standard field-extension protocol.

1 @5 actor:jarvis-coin-kl-courier.location: lower-city-in-transit -> cooper-yard-eel-alley-lane-mouth
2 @9 actor:jarvis-coin-kl-courier.stats.active_deliveries: 0 -> 1
3 @11 actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley-lane-mouth -> lower-city-in-transit
4 @29 actor:jarvis-coin-kl-courier.location: lower-city-in-transit -> cooper-yard-eel-alley
5 @29 actor:jarvis-coin-kl-courier.inventory: [] -> [otto-confirmation-note]
6 @32 actor:jarvis-coin-kl-courier.inventory: [otto-confirmation-note] -> [otto-confirmation-note, taylor-movement-pattern-report]
7 @36 actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley -> lower-city-in-transit
8 @36 actor:jarvis-coin-kl-courier.stats.exposure_risk: latent -> operational
