facet: state-updates
episode: s01e01
authors: studio (env-side, this dispatch) + per-character impersonators (actor-side, dispatched after)
round: 1
---

# === ENV (studio) ===

1 @8 studio.doors_and_shutters.workshop-shutter: shut -> open
2 @32 studio.doors_and_shutters.workshop-door: closed -> open
3 @58 studio.active_conditions.tallow-lamp: unlit -> lit
4 @93 prop:oc-account-ledger.cover-state: closed -> open  # field-extension: cover-state (new field; ledger physical open/close state for s01e01 bench-scene tracking)
5 @98 prop:oc-account-ledger.entry-state: blank -> marked  # field-extension: entry-state (new field; irreversible record-mutation — entry written in at the apprentice column)
6 @99 prop:oc-account-ledger.apprentice-mark: absent -> set  # field-extension: apprentice-mark (new field; tens=3 peak; irreversible bureaucratic registration — the mark that fixes Taylor's household role)
7 @122 studio.active_conditions.tallow-lamp: lit -> guttering
8 @126 studio.prop_positions.winter-candle: stored -> drawn
9 @130 studio.active_conditions.winter-candle: unlit -> lit
10 @130 studio.active_conditions.tallow-lamp: guttering -> dark

# === ACTOR (per-character impersonators) ===
# (this section will be appended by Layer 3.2 dispatches; leave it empty)
