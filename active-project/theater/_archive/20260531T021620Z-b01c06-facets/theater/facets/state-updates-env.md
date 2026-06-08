facet: state-updates
episode: b01c06
author: studio
scope: environment + prop (no actor-state; actor:taylor.* is dialogue-writer fork authority)
---

# rubric-carve-out — field-extension for oc-prop targets pending margit cards
#
# design/shoot-v2/rubric-state-updates.md § Authority / Field-extension protocol
#
# Carve-out scope: entries targeting prop:oc-ward-coverage-notes, prop:oc-jarvis-channel-form,
#   prop:oc-accounting-ledger
# Carve-out rule: all three are project-original props (oc-* slug class) with no card yet authored;
#   prop cards are pending margit referrals (see SEAM annotations below).
#   Authority § "Studio may extend with oc-* for genuine project-originals, but extension must be flagged."
#   Each entry carries an inline # field-extension comment per rubric protocol.
# Coverage justification:
#   oc-ward-coverage-notes — first-touched at @6 (open event); @8 is peak-bone (contact-source-field
#     blanked — irreversible omission); persists to b01c06 chapter-close and beyond.
#   oc-jarvis-channel-form — first-touched at @14 (fill event); @22 is peak-bone (sealed — the send;
#     moral_framework -1.0); persists as delivered artifact beyond chapter scope.
#   oc-accounting-ledger — first-touched at @16 (open event); @20 closes it; the open/close pair
#     is the canonical record of the rationalize-each-trade accounting sequence.
#   Refusing on no-card-yet grounds would miss irreversible record-events the rubric explicitly flags
#   for co-citation (calibration anchor: "irreversible bureaucratic / record / knowledge events
#   strongly expect a state-update entry").
#
# Per-entry annotations:
#   state:1 @6:  carve-out clause A — oc-ward-coverage-notes first-touch, SEAM-006 pending
#   state:2 @8:  carve-out clause A — oc-ward-coverage-notes contact-source-field (peak-bone)
#   state:3 @9:  carve-out clause A — oc-ward-coverage-notes close
#   state:5 @14: carve-out clause B — oc-jarvis-channel-form first-touch, SEAM-007 pending
#   state:6 @15: carve-out clause B — oc-jarvis-channel-form state (loaded-pause hinge)
#   state:7 @16: carve-out clause C — oc-accounting-ledger first-touch, SEAM-008 pending
#   state:8 @20: carve-out clause C — oc-accounting-ledger close
#   state:9 @22: carve-out clause B — oc-jarvis-channel-form peak-bone (the send)
#  state:10 @23: carve-out clause B — oc-jarvis-channel-form holder (dispatch)
#  state:11 @24: carve-out clause A — oc-ward-coverage-notes second open (peak-bone)
#  state:12 @25: carve-out clause A — oc-ward-coverage-notes second close (terminal)
#
# SEAM-006: oc-ward-coverage-notes.card.md (prop card; first-touch @6; contact-source-field tracked
#   as record-substrate; persists b01c06+; margit referral; priority: before b01c07 facets)
# SEAM-007: oc-jarvis-channel-form.card.md (prop card; first-touch @14; sealed and dispatched @22-@23;
#   deliverable artifact; margit referral; priority: before b01c07 facets)
# SEAM-008: oc-accounting-ledger.card.md (prop card; first-touch @16; accounting substrate;
#   margit referral; priority: before b01c07 facets)
#
# ENV SEAM — lane-mouth unblock: studio.spatial_layout.lane-mouth is blocked by handcart at episode-open
#   (world-before-protagonist anchor @1); no bone records the unblocking. The handcart obstruction is a
#   scene-A local condition (Taylor routes via south court @5; by scene-B the blocking is contextually
#   resolved but unrecorded). The @1 obstruction entry was culled (transient env condition, not
#   irreversible canonical write-back). SEAM: showrunner to confirm lane-mouth status at b01c07 open.

1 @6 prop:oc-ward-coverage-notes.state: closed -> open # field-extension: state (new prop; first-touch @6; oc-card pending margit SEAM-006)
2 @8 prop:oc-ward-coverage-notes.contact-source-field: unresolved -> blank-authored # field-extension: contact-source-field (peak-bone @8 — the authored omission; blank is not absent; persistent canonical record state; SEAM-006)
3 @9 prop:oc-ward-coverage-notes.state: open -> closed # field-extension: state (SEAM-006; chapter-A close; re-opens at @24)
4 @10 studio.time_of_day: morning -> late-morning
5 @14 prop:oc-jarvis-channel-form.content: blank -> filled-four-names # field-extension: content (new prop; first-touch @14; oc-card pending margit SEAM-007)
6 @15 prop:oc-jarvis-channel-form.state: filled -> lowered-unsent # field-extension: state (SEAM-007; scene-B loaded-pause hinge; send held; persists to @21)
7 @16 prop:oc-accounting-ledger.state: closed -> open # field-extension: state (new prop; first-touch @16; oc-card pending margit SEAM-008)
8 @20 prop:oc-accounting-ledger.state: open -> closed # field-extension: state (SEAM-008; accounting complete; peak-shadow @20)
9 @22 prop:oc-jarvis-channel-form.state: lowered-unsent -> sealed # field-extension: state (SEAM-007; peak-bone @22 — the send; moral_framework -1.0 anchor; irreversible dispatch-initiation)
10 @23 prop:oc-jarvis-channel-form.holder: taylor-hebert-kl-122ac -> the-courier # field-extension: holder (SEAM-007; physical dispatch; prop leaves Taylor's possession; peak-shadow @23)
11 @24 prop:oc-ward-coverage-notes.state: closed -> open # field-extension: state (SEAM-006; peak-bone @24 — contrast recognition; moral_legibility_to_self +1.0 anchor)
12 @25 prop:oc-ward-coverage-notes.state: open -> closed # field-extension: state (SEAM-006; terminal-bone @25; both substrates complete; chapter ends here)
