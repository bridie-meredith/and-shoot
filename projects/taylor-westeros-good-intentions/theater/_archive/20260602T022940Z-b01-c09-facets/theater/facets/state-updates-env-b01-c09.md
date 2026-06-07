facet: state-updates-env
episode: b01c09
author: studio
source: theater/proto-lines/b01-c09.md (27 bones; revise --from-signals depth pass)
generated: 2026-06-01 (depth-pass re-anchor; prior 4 env entries remapped old→new flat-ids; content stable)
---

# rubric-carve-out — oc-prop field extensions (ward-coverage-notes + jarvis-packet lifecycle)
#
# design/shoot-v2/rubric-state-updates.md § Field-extension protocol
#
# Carve-out scope: entries state:1 (prop:oc-ward-coverage-notes), state:2/3/4 (prop:oc-jarvis-packet)
# Carve-out rule: both props are oc-* project-originals with explicit chapter presence; no authored
#   prop cards exist yet (margit referrals pending per b01c08 state.md). Field extensions documented
#   per-entry per §Field-extension protocol. Standard prop-state fields used where applicable
#   (physical-condition, seal-condition, dry/wet per rubric §Authority ACCEPT signatures).
# Coverage justification: oc-ward-coverage-notes is the deliverable substrate that is the chapter's
#   structural fact; oc-jarvis-packet is the physical artifact of the seal-down thesis-image (peak-bones
#   @23 + @27); both field changes are canonical write-back events persisting downstream.
#
# Per-entry annotations:
# - state:1 @10: field-extension: prop:oc-ward-coverage-notes.content (new field; tracks the
#     boundary-geometry record state; the deliverable substrate's record of the southward extension
#     is canonical — it shapes what Jarvis receives and what routes downstream). RE-ANCHOR (was @7).
# - state:2 @22: field-extension: prop:oc-jarvis-packet.physical-condition (new field; tracks
#     the packet lifecycle from assembled to folded to sealed to dry; standard lifecycle state
#     for a document-bearing prop; precedent from b01c08 oc-jarvis-packet seal-condition extension).
#     RE-ANCHOR (was @18).
# - state:3 @23: seal-condition is a standard prop-state field per rubric §Authority ACCEPT
#     signatures (seal-condition for seal-bearing props); no carve-out required. RE-ANCHOR (was @19).
# - state:4 @27: dry/wet is a standard prop-state field per rubric §Authority ACCEPT
#     signatures (dry/wet for ink-bearing props); seal drying qualifies; no carve-out required.
#     RE-ANCHOR (was @23).

1 @10 prop:oc-ward-coverage-notes.content: hook-rushwick-oswyn-corridors -> hook-rushwick-oswyn-corridors-plus-south-extension
# field-extension: content (oc-ward-coverage-notes; new field; records deliverable boundary state; the southward extension to the stitch-shop and water-seller lanes is written into the notes here; persistent — the notes retain this content at chapter close and into downstream chapters; old state sourced from b01c08 coverage_active_range: hook-ward + rushwick-extension + oswyn-watcher-network integrated). RE-ANCHOR: new @10 ("the ward-coverage notes receive the boundary geometry") is the exact bone for the content-write (was @7 in pre-depthpass numbering).

2 @22 prop:oc-jarvis-packet.physical-condition: assembled -> folded
# field-extension: physical-condition (oc-jarvis-packet; new b01c09 packet — distinct from b01c08 packet consumed within that chapter; assembled = contents gathered from deliverable substrate, not yet folded; folded = packet folded for sealing; persistent past @22 through seal-down at @23). RE-ANCHOR (was @18).

3 @23 prop:oc-jarvis-packet.seal-condition: unsealed -> sealed
# RE-ANCHOR (was @19). @23 = "taylor-hebert-kl-122ac seals the packet" (central event; the physical act that makes the substrate boundary real).

4 @27 prop:oc-jarvis-packet.seal-condition: sealed -> dry
# RE-ANCHOR (was @23). @27 = "the seal dries" (terminal image; the omission permanent in the hardening wax). dry/wet standard prop-state field.
