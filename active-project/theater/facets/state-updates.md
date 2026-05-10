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

11 @23 actor:taylor-hebert-jaehaerys.position-in-household: floor-child-register -> ledger-bench-stool  # tens=2; NI@23 co-cite; load-bearing across @23-@30 ledger work
12 @83 actor:taylor-hebert-jaehaerys.hair-state: loose -> apprentice-thread-bound  # field-extension: hair-state (new field; tens=3 peak; mother binds the apprentice-thread — domestic ratification of the mark; persists into @86+)
13 @99 actor:taylor-hebert-jaehaerys.public-role: child-of-house -> apprentice-of-house  # field-extension: public-role (new field; tens=3 peak; irreversible — the household-visible role the mark fixes; co-cites prop:oc-account-ledger.apprentice-mark @99)
14 @103 actor:taylor-hebert-jaehaerys.inventory: [] -> [cloth]  # tens=2; NI@103 co-cite; cloth carried through workshop re-entry @108
15 @83 actor:oc-craftsman-mother.apprentice-ratification: not-performed -> thread-bound  # field-extension: apprentice-ratification (new field; tens=3 peak; the domestic ratification act — mother binds the apprentice-thread into Taylor's hair, irreversible household-symbolic act; non-POV, no NI co-cite required; pairs with state:12 on Taylor's hair-state)
16 @99 actor:oc-craftsman-mother.relationship-role-toward-taylor: mother-of-child -> mother-of-apprentice  # field-extension: relationship-role-toward-taylor (new field; tens=3 peak; structural household-role shift consequent to the mark — mother's role re-fixes when Taylor's public-role re-fixes; non-POV, no NI co-cite required; co-cites prop:oc-account-ledger.apprentice-mark @99 and Taylor state:13)
