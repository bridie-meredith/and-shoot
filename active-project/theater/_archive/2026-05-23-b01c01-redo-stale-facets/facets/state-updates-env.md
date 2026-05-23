facet: state-updates
episode: b01c02
author: studio
scope: env
---

# rubric-carve-out — oc-prop field-extensions for Taylor's accounting kit and deployment fauna
#
# rubric-state-updates.md (design/shoot-v2/rubric-state-updates.md) § Field-extension protocol
#
# Carve-out scope: prop:oc-lamp, prop:oc-ledger, prop:oc-pen entries (entries 4, 5, 7, 8, 9, 10)
# Carve-out rule: these props are Taylor's personal tools (lamp, ledger, pen) with no pre-authored
#   prop card in cards/props/ and no warehouse presence established prior to this chapter. Extended
#   per §Field-extension protocol as project-originals with oc-* slugs. Fields (state, current-entry)
#   are standard prop-state fields (physical condition, record content), not perceptions or stylistic.
# Coverage justification: the lamp-lit, ledger-open/closed, and pen-set-down transitions are all
#   persistent, persistent-past-the-beat changes on real objects that appear in the bones file
#   and the shared brief. Refusing them would leave scene-C with zero prop coverage despite three
#   peak-bone-class beats loading on ledger content. Extension is the conservative write rather
#   than the card-schema referral deferral.
#
# Per-entry annotations:
# - state:4 @22: oc-lamp.state — oc-prop extension; field is physical-state (unlit/lit)
# - state:5 @23: oc-ledger.state — oc-prop extension; field is physical-state (closed/open)
# - state:7 @25: oc-ledger.current-entry — oc-prop extension; field is record-content-state
# - state:8 @26: oc-ledger.current-entry — oc-prop extension; field is record-content-state
# - state:9 @27: oc-pen.state — oc-prop extension; field is physical-state (in-hand/set-down)
# - state:10 @29: oc-ledger.state — oc-prop extension; field is physical-state (open/closed)

1 @1 studio.fauna_sense_status: ambient-passive -> lane-filling-active

2 @5 studio.fauna_sense_status: lane-filling-active -> lane-mouths-closed-routing-active

3 @22 studio.time_of_day: watch-press-day -> watch-press-night

4 @22 prop:oc-lamp.state: unlit -> lit
# field-extension: oc-lamp (Taylor's accounting lamp, project-original; state field standard)

5 @23 prop:oc-ledger.state: closed -> open
# field-extension: oc-ledger (Taylor's personal ledger, project-original; state field standard)

6 @25 prop:oc-ledger.current-entry: blank -> struck
# field-extension: oc-ledger.current-entry (record-content-state field); fires at @25 (the verdict
# strike) not @24 (the write-before-strike); persistence: struck entry persists through @26-@29

7 @26 prop:oc-ledger.current-entry: struck -> struck-categorical-underlined
# field-extension: oc-ledger.current-entry; the underline is a discrete delta from the strike —
# categorical distinction marked, persistent through @29

8 @27 prop:oc-pen.state: in-hand -> set-down
# field-extension: oc-pen (Taylor's writing pen, project-original; state field standard);
# persistent: pen stays down through @28 (hand-held bone does not pick it up)

9 @29 prop:oc-ledger.state: open -> closed
# field-extension: oc-ledger.state; accounting session closes, ledger closed — persistent
