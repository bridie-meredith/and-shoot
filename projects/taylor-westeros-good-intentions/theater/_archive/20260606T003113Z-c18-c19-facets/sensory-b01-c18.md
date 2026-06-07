facet: sensory
episode: b01c18
author: studio
---

# Standard entries (2): within 3-6% sparsity band
# Grounding-licensed entries (3): GROUNDING-REQUIRED / PROP-0022 / exempt from frequency-band cap
# Total: 5/46 = 10.9%; standard-only = 2/46 = 4.3% (within band)
# Modalities: tactile + light + sound (3 distinct; ≥2 floor MET)
# Per-scene caps: s01=1, s02=2, s03=0, s04=0, s05=2 — all ≤3
# Old-state lineage: see per-entry notes
#
# grounding-ledger cross-refs:
#   sensory:3 @13 -> grd-001 (moth-corridor noise node; s02-op-friction grounding)
#   sensory:4 @38 -> grd-002 (chandler-quarter moths settling; s05 grounding)
#   sensory:5 @46 -> grd-003 (stylus beside closed ledger; s05 grounding)

# --- STANDARD ENTRIES ---

# @1 — taylor lifts the cipher-bundle (s01; before-dawn; the-tallow-render-works)
# Verb "lifts" is bare; no tactile register in proto-line.
# Old-state: loc-state:1 conditions include "floor-bare" and "tallow-smell-saturated" — the floor of the
# tallow-render room; tactile baseline is tallow-render-room-floor-ambient (stone/board underfoot,
# no object in hand yet). The cipher-bundle lifted from the floor is a discrete tactile inflection:
# cold, stiff paper in the dark before dawn.
# Q1: audience does not know the difference without the flag (bare verb "lifts"; no tactile language).
# Q2: magnitude — the paper's cold-dry stiffness in a dark room before dawn is audience-register-shifting;
# it materializes the dead-drop retrieval as a physical act, not an abstract information-receipt.
# Audience-side perceptible: universally legible.
1 @1 tactile: tallow-render-room-floor-ambient -> cipher-bundle-paper-cold-dry # tag: up

# @10 — the feed-lines activate the outer-gate corridors (s02; before-first-light; oc-ward-network-full-coverage)
# Verb "activate" is bare; no light language in proto-line.
# Old-state: loc-state:3 establishes "before-first-light" with no weather; the ward-ambient in the hour
# before dawn is solid dark — outer-gate corridors not yet catching any light.
# The outer-gate corridors activating "before first light" (scene-map s02 header) implies the feed opens
# into corridors that are in the specific grey of the last pre-dawn dark before first light bleeds in.
# Q1: bare ("activate"); audience receives the mechanical act without the light-register.
# Q2: pre-dawn grey at stone gate-mouth vs. full dark — audience-register-shifting at this density.
# The light shift names the deployment's hour and embeds the architectural reach in a physical moment.
2 @10 light: ward-ambient-full-dark -> outer-gate-corridor-pre-dawn-grey # tag: up

# --- GROUNDING-REQUIRED ENTRIES ---
# licensed-grounding-exception: grd-001 / grd-002 / grd-003
# See grounding-ledger-b01-c18.md for full license records

# @13 — the moth-corridor feed returns noise (s02; before-first-light; chandler-quarter)
# GROUNDING-REQUIRED: scene-map names @13 as the op-friction bone — "one node returns noise
# [a smelt-fire degrading the chandler-quarter passage]." The architecture routes around it.
# Without a sensory fire, the moth-corridor noise reads as pure mechanical report (the feed returns noise).
# The smelt-fire interference is the grounding anchor that makes the op-friction physically real —
# the deployment is not frictionless competence; the sound-register (a low, acrid interference
# rather than the clean moth-corridor ambient) embeds the architectural friction in the world.
# Old-state: moth-corridor-ambient-clear (the channel's baseline; the moth-corridor established at @9
# as newly opened; its ambient prior to interference is the clear-channel register the deployment expects).
# New-state: smelt-fire-interference-low-register (the chandler-quarter smelt-fire's thermal noise
# bleeding into the moth-corridor feed; a low, acrid register against the expected clean moth-passage).
# Q1: bare ("returns noise"); audience receives an abstract report without the smelt-fire's register.
# Q2: the shift from clean-channel to smelt-fire interference is audience-register-shifting; the smelt-fire
# as physical cause of the friction lands the op-friction as an environmental fact, not a system flag.
# licensed-grounding-exception: grd-001
3 @13 sound: moth-corridor-ambient-clear -> smelt-fire-interference-low-register # tag: spike; licensed-grounding-exception: grd-001

# @38 — the chandler-quarter moths settle the eaves (s05; day-fourteen; the-tallow-render-works/chandler-quarter)
# GROUNDING-REQUIRED: scene-map names @38 as a GROUNDING-REQUIRED anchor (explicit) —
# "the physical fact of the network standing down into the buildings it lives in."
# This is the standdown's only concrete environmental fact before the accounting-close sequence begins.
# Old-state: chandler-quarter-deployment-active (two weeks of full-coverage density; the moths
# operating at sustained deployment-mode across the chandler-quarter eaves; the sound signature
# is the active-coverage register, not ambient moth-presence).
# New-state: moth-eaves-ambient-settling (the moths returning to ambient density as the architecture
# withdraws; the distinctive sound of insects resettling into the eaves' natural ambient after
# sustained operational deployment — the architecture's physical withdrawal audible in the insect layer).
# Q1: bare ("settle the eaves"); audience does not register the shift from deployment-mode to
# ambient-settling without the flag; "settle" is generic-movement, not a sound-carrying verb.
# Q2: two-week deployment-active density → ambient-settling is a register-shifting contrast; the
# physical withdrawal of the architecture is audible at eaves level.
# licensed-grounding-exception: grd-002
4 @38 sound: chandler-quarter-deployment-active -> moth-eaves-ambient-settling # tag: down; licensed-grounding-exception: grd-002

# @46 — taylor sets the stylus (s05; day-fourteen; the-tallow-render-works)
# GROUNDING-REQUIRED: scene-map names @46 as the second grounding anchor of s05 accounting-close —
# "the stylus beside the closed ledger." The accounting-as-discipline completing in a physical act.
# Old-state: ledger-wax-working-rhythm (the stylus in use through the accounting-close sequence @39-@45;
# the physical state of active ledger-work — tactile baseline from the cost-ledger open at @39).
# New-state: stylus-placed-beside-closed-ledger (the stylus set beside, not away; the act completed
# in the specific physical gesture of a discipline that has run its course; still on the surface,
# adjacent to the work).
# Q1: bare ("sets"); the verb does not carry the tactile register of completion — "sets beside"
# vs. "sets down" vs. "puts away" are different gestures; the audience needs the flag to read this
# as the accounting-as-discipline completing, not as the act of abandonment.
# Q2: ledger-wax-working-rhythm → stylus-placed-beside is audience-register-shifting; the shift
# from the rhythmic working-contact to the final resting placement enacts the discipline closing.
# licensed-grounding-exception: grd-003
5 @46 tactile: ledger-wax-working-rhythm -> stylus-placed-beside-closed-ledger # tag: drop; licensed-grounding-exception: grd-003

# Inflection-pair coherence:
#   sensory:3 @13 (sound:up/spike: chandler-quarter noise onset at deployment) and
#   sensory:4 @38 (sound:down: chandler-quarter moths settling at standdown) form a loose
#   deployment-open / standdown-close pair. New-state of :3 = smelt-fire-interference-low-register;
#   old-state of :4 = chandler-quarter-deployment-active. These are not direct mirror-pairs (14 days
#   apart; different events in the same location). The pair is coherent in direction (noise-up at
#   deployment, density-down at standdown) but not required to share a modality midpoint.
#   Pair coherence CHECK: the two entries bracket the fortnight at the same architectural location
#   (chandler-quarter moth-corridor); the sound register is the physical fact of the deployment at
#   both ends. The pair is structurally coherent.
#
# Modality-coverage health-check:
#   tactile: sensory:1 @1 + sensory:5 @46
#   light: sensory:2 @10
#   sound: sensory:3 @13 + sensory:4 @38
#   3 distinct modalities — ≥2 floor MET; cross-modal discipline confirmed.
