facet: state-updates-env
episode: b01c10
author: studio
---

# rubric-carve-out — oc-prop field-extensions (two new props + one new field)
#
# design/shoot-v2/rubric-state-updates.md § Field-extension protocol
#
# Carve-out scope: state:2 (prop:oc-jarvis-packet-out) and state:5 + state:7 (prop:oc-feed-ledger)
# Carve-out rule: three oc-prop fields are first-touch this chapter; <old> is derived from
#   chapter-open baseline (prior chapters did not log these props), not from a prior
#   state-update entry within the episode. Field-extensions are flagged below.
# Coverage justification: prop:oc-jarvis-packet-out is the outgoing routed piece Taylor seals
#   at @11-@12; it is a distinct physical artifact from the incoming c10 packet (prop:oc-jarvis-packet).
#   prop:oc-feed-ledger is Taylor's accounting surface referenced in scene-D; no prior chapter
#   logged its physical-condition or content; baseline = closed / accounting-open (prior-to-corwick).
#   All three extensions satisfy the field-extension protocol: tracked-state-aspect, not perception.
#   Margit referral flagged for oc-jarvis-packet-out.card.md and oc-feed-ledger.card.md.
#
# Per-entry annotations:
# - state:2 @12: field-extension — prop:oc-jarvis-packet-out (new oc-prop, outgoing piece; first-touch b01c10)
# - state:5 @20: field-extension — prop:oc-feed-ledger.physical-condition (new field; first-touch b01c10; baseline=closed)
# - state:6 @21: field-extension — prop:oc-feed-ledger.content (new field; first-touch b01c10; baseline=accounting-open pre-corwick)
# - state:7 @25: field-extension follows from state:5 @20 open; closes the ledger at chapter-scene close

1 @1 prop:oc-jarvis-packet.holder: jarvis -> station-surface
2 @12 prop:oc-jarvis-packet-out.seal-condition: sealed -> dry
3 @15 studio.ambient_conditions.lower-gate-stone-post: corwick-present -> corwick-absent
4 @17 studio.ambient_conditions.lane-junction: unposted -> gold-cloak-pair-posted
5 @20 prop:oc-feed-ledger.physical-condition: closed -> opened
6 @21 prop:oc-feed-ledger.content: accounting-open -> includes-corwick-entry
7 @25 prop:oc-feed-ledger.physical-condition: opened -> closed
