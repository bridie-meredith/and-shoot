---
reviewer: cape-fic-reader
facet: state-updates
cycle: 1
episode: b01c11
date: 2026-06-03
verdict: accept
---

## Dispatch note

19 entries total: env 1-14, taylor 15-19. Reviewing both slices as consolidated.

## Entry-level callouts

ENV SLICE (1-14):

[state:1 @1] prop:oc-jarvis-packet.holder: station-surface -> jarvis-coin-kl-courier. The packet changes hands. Board-state mandatory: without this flip the canonical holder remains at the station into b01c12. Clean.

[state:2 @5] prop:oc-feed-ledger.condition: closed -> open. The ledger opens at the first writing beat. Required: @3 (source-field-entry) fires at @6 and needs the ledger open to be coherent. The old-state "closed" sourced from b01c10's chapter-close. Clean.

[state:3 @6] prop:oc-feed-ledger.source-field-entry: absent -> lane-pattern-only. This is the canonical record of the wool-dyer withhold: the source-field holds the lane-pattern but not the source-name. Board-state: downstream chapters (and Otto) receive a ledger entry that routes the observation without attributing it. This field-flip carries the tether's operational secret. The "lane-pattern-only" value is the precise canonical state the withhold creates. Strong entry.

[state:4 @11] prop:oc-cloth-merchant-paper.physical-condition: intact -> burned. The paper is destroyed. The Dragonstone-signal is permanent — the burn is a one-way event that changes the board permanently. Strip-test: the canonical paper state must read "burned" into b01c12. Clean.

[state:5 @16] prop:oc-feed-ledger.cloth-merchant-entry: absent -> timestamp-marked. The withhold is recorded. The timestamp exists in the ledger; what is NOT in the ledger is the routing to Jarvis. Board-state: Taylor has a logged observation she is not routing. This is the substrate-split state the chapter's antag-tether tranche builds on. Clean.

[state:6 @18] prop:oc-soap-lane-report-packet.holder: soap-lane-contact -> taylor-hebert-kl-122ac. New prop, first-touch at @18. The delivery is a board-state event — the packet is now in Taylor's hands. Clean.

[state:7 @20] prop:oc-soap-lane-report-packet.content: nighttime-visitor-report -> precinct-pattern-sourcing-added. The packet's content state after Taylor writes into it. This is the canonical state that persists sealed into b01c12. Board-state: whatever the recipient opens will contain Taylor's precinct-pattern sourcing. Clean.

[state:8 @21] prop:oc-soap-lane-report-packet.physical-condition: opened -> sealed. Packet sealed. Persists into b01c12. The old-state "opened" is correctly derivable from @19's physical act (held-against-turn rejection at @19 was correct). Clean.

[state:9 @22] studio.time_of_day: afternoon -> end-of-day. The scene-D time-advance. The accounting-close's temporal anchor. Without this flip the time-of-day state carries "afternoon" from scene-C into scene-D which has a different mood and function. Clean.

[state:10-13 @23-@26] Four arm-close field-flips on prop:oc-feed-ledger (jarvis-entry, oswyn-entry, contacts-entry, arrangement-entry: open -> closed). The sequential accounting-close is the chapter's terminal board-state operation. Each entry is one field-flip at one bone. The four distinct closings are exactly what the scene-map's ACCOUNTING-IN-MOTION-NOT-CATALOG protected-pattern requires — four separate canonical facts, not one summary. Any attack on density here is answered by the absolute-count-ceiling rationale in the rubric-carve-out preamble: 14 entries is the absolute ceiling from the density band calibrated for a longer chapter.

[state:14 @27] prop:oc-feed-ledger.condition: open -> closed. The ledger closes at chapter-close. Persists into b01c12 as the canonical ledger state. Required.

TAYLOR SLICE (15-19):

[state:15 @6] actor:taylor-hebert-kl-122ac.social_tether_prot_rise_axis: 3 -> 3.5. The first tether-rise tranche. Board-state: the axis is now at 3.5. Clean.

[state:16 @16] actor:taylor-hebert-kl-122ac.social_tether_antag_axis: 0 -> 0.5. First antag-tether entry in the chapter. Board-state: the substrate-split begins accumulating on the antag axis. New field (social_tether_antag_axis) — the field-extension is documented. Clean.

[state:17 @16] actor:taylor-hebert-kl-122ac.withholding_pattern: single-instance -> established. Second consecutive withhold establishes the pattern. Board-state: the substrate-split is now a standing operational pattern, not a one-off. The field-extension is documented. This is the canonical state the downstream chapters read when evaluating Taylor's routing discipline. Clean.

[state:18 @20] actor:taylor-hebert-kl-122ac.social_tether_antag_axis: 0.5 -> 1.0. Second antag-tether tranche. Board-state: chapter's social_tether-antag +1.0 complete. Clean.

[state:19 @25] actor:taylor-hebert-kl-122ac.social_tether_prot_rise_axis: 3.5 -> 4. Second tether-rise tranche. Board-state: chapter's social_tether-prot-rise +1.0 complete, cumulative at near-peak rank 8. Clean.

## Convergence trace

SEAM-C11-ENV-001 (cloth-merchant-paper old-state "intact" — no prior entry): the first-touch inference is standard for new props; "intact" is the only defensible pre-burn state. Not a blocking finding. SEAM-C11-ENV-002 (soap-lane-report-packet first-touch @18): same logic. SEAM-C11-ENV-003 (afternoon old-state for @22 inferred from scene-map): the inference chain from scene-map "early afternoon" for scene-C is adequate. SEAM-C11-ENV-004 (arm-close fields "open" old-state inferred from ledger.condition=open @5): the ledger open at @5 is sufficient to establish the arm-entry fields as open; individual arm-open back-fills would be excess density.

## Verdict rationale

19 entries, all board-state changes with canonical persistence. The four arm-close field-flips are individually necessary per the scene-map's protected-pattern (four distinct sequential closings, not a catalog). The prop-chain coverage is complete: packet holder, ledger condition, paper destroyed, packet content and seal. The Taylor axis updates correctly track both the prot-rise and antag-tether tranches with the new field-extensions. No established limits bypassed; no unmotivated state. Accept.
