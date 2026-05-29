# SOURCE SLICE — NOT CANONICAL. IDs in this file are slice-local. The canonical authority for cross-facet citation is state-updates.md (consolidated; monotonic IDs 1-12). The cite-index resolves [state:N] tokens against the consolidated.

facet: state-updates
episode: b01c05
author: studio
scope: environment + prop (no actor-state; actor:taylor.* is dialogue-writer fork authority)
---

# rubric-carve-out — field-extension for oc-prop targets pending margit cards
#
# design/shoot-v2/rubric-state-updates.md § Authority / Field-extension protocol
#
# Carve-out scope: entries targeting prop:oc-enforcement-report-entry and prop:oc-courier-body-map
# Carve-out rule: both are project-original props (oc-* slug class) with no card yet authored;
#   prop cards are pending margit referrals per studio state.md (SEAM-002 + SEAM-003).
#   Authority § "Studio may extend with oc-* for genuine project-originals, but extension must be flagged."
#   Each entry carries an inline # field-extension comment per rubric protocol.
# Coverage justification: oc-enforcement-report-entry is first-touched at @17 (filing event, irreversible
#   bureaucratic mutation; rubric calibration anchor: "irreversible bureaucratic / record / knowledge events
#   strongly expect a state-update entry"). oc-courier-body-map is first-touched at @21 (body-record initiation,
#   cf-d10 thread anchor; persists to b01c06+). Both props are tracked-state-aspects with genuine persistence.
#   Refusing on no-card-yet grounds would miss irreversible record-events the rubric explicitly flags for co-citation.
#
# Per-entry annotations:
#   state:3 @17: carve-out clause A — oc-enforcement-report-entry, field-extension, SEAM-002 pending
#   state:4 @21: carve-out clause B — oc-courier-body-map first-touch, field-extension, SEAM-003 pending
#   state:7 @31: carve-out clause B — oc-courier-body-map field-transition, SEAM-003 pending

1 @2 studio.location: oc-stitch-house-lane -> the-rushwick
2 @3 studio.coverage_active_range: four-ward-complete -> rushwick-included
3 @17 prop:oc-enforcement-report-entry.state: absent -> filed-with-jarvis # field-extension: state (new prop; first-touch @17; oc-card pending margit SEAM-002; irreversible filing event)
4 @21 prop:oc-courier-body-map.state: absent -> initiated # field-extension: state (new prop; first-touch @21; cf-d10 anchor; oc-card pending margit SEAM-003)
5 @23 studio.location: the-rushwick -> taylor-lodging
6 @23 studio.time_of_day: morning -> evening
7 @31 prop:oc-courier-body-map.state: initiated -> filed # field-extension: state (cf-d10 thread confirmed; SEAM-003 pending)
