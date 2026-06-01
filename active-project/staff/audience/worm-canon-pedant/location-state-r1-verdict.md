---
reviewer: worm-canon-pedant
facet: location-state
cycle: 1
episode: b01-c09
date: 2026-06-01
depth-pass: yes
verdict: accept
---

# Verdict: ACCEPT

## Reading

Five entries. Checking for: location facts consistent with established world-geography; no apparatus-register contamination in the state fields; correct baseline-state sourcing.

**Depth-pass re-anchor check:**

The file header confirms this is a depth-pass re-anchor: "prior 5 entries remapped old→new flat-ids; sensory-baseline fields preserved." Content is stable; anchors shifted to match the 27-bone flat-ID scheme. I'm checking whether the anchor re-maps are correct.

- loc-state:1 @1: "taylor-hebert-kl-122ac enters the lane-south-of-the-hook" → @1 is the correct first bone. The lane entry is the opening move of the circuit. Correct.
- loc-state:2 @5: "the stitch-shop door opens the lane-mouth" → @5 is the stitch-shop door bone. Confirmed.
- loc-state:3 @11: "taylor-hebert-kl-122ac enters the dragonpit-margin lane" → @11 is the scene-B opening bone (Taylor enters the Dragonpit-margin lane). Confirmed.
- loc-state:4 @14: "the insect-feed returns corwick" → @14 is the courier-appears bone. The loc-state fires on the courier-resolves-at-stone-post event. The feed "returning" a body is not apparatus-contamination in the location-state file; this is the feed providing the perceptual event that anchors the location-state update. Confirmed.
- loc-state:5 @21: "taylor-hebert-kl-122ac takes the feed-station" → @21 is the feed-station bone. Confirmed.

All anchors re-map correctly.

**Sensory-baseline field check:**

The mechanized check from the Phase-5 audit confirms all 6 sensory entries have loc-state-sourced old-states. The depth-pass added 3 new sensory entries (sensory:4 @3, sensory:5 @9, sensory:6 @15), all anchoring to loc-state baselines named in the loc-state file. The chain is complete: loc-state names the baseline → sensory entry cites the baseline as old-state → sensory entry fires on the new-state change.

No Taylor-prior-knowledge leakage in the location-state entries. The locations named (hook-ward, stitch-shop lane, dragonpit-margin, lower-gate, feed-station) are all chapter-internal staging locations, consistent with b01c09 bones header and scene-map coverage.

## Convergence trace

Auditor: RUBRIC-FIDELITY PASS. Sensory old-state lineage ANCHORED all 6 (pl-2026-06-01-002 mechanized check). No location-state findings in Phase-5 report.
