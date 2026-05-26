---
reviewer: cape-fic-reader
facet: state-updates
episode: b01-c02
cycle: r1
date: 2026-05-25
verdict: accept
---

# Cape-Fic Reader — State-Updates Adversarial Verdict (b01-c02)

## Stance

Tracking the board. State-updates is the layer that tells me whether the chapter actually moved anything — whether the operational state of the game has changed or whether the chapter was just atmosphere. For this chapter: one mechanism-flip, one relational-categorization, one recognition-event, one suppression. That is the right shape for a chapter about Taylor building a coverage map she then has to pretend she didn't build.

## Per-entry readings

**[state:1] @20 — `studio.time_of_day: dawn -> end-of-day`**

The chapter's only env entry. The carve-out preamble earns it: no prop cards, no location transition, no door states. The one field that actually flips is the time-of-day at @20. The entry passes its own strip test — without it, the canonical `studio.time_of_day` would carry a dawn-to-day-sweep state through chapter close, which the scene-map contradicts. Persistent through @29 (confirmed). Clean.

SEAM-001 in the preamble (b01c01 authored zero env state-updates, so the `<old>` value "dawn" derives from handoff_out baseline rather than a prior chain entry) is a process seam, not an entry fault. This reader cares when information chains break; the chain here is intact via handoff_out, just undocumented at the prior chapter level. Note it and move on.

`CORRECT`

**[state:2] @6 — `actor:taylor.deployment-state: ambient-subsistence-reading -> systematic-precinct-coverage-deliberate`**

The chapter's mechanism-establishment anchor. This is the board-state flip the whole chapter produces at the scene-A level: Taylor stops reading ambient and starts running a deliberate coverage architecture. The `<old>` carries forward from b01c01 (handoff implied). The `<new>` persists — handoff_out confirms the coverage map is active across approximately 40 bodies at chapter close. The NI co-citation is present at narrator:1 @6 (cite-index confirms).

One cite-index flag: back=N — the proto-line @6 (`taylor-hebert-kl-122ac extends the range`) does not carry an inline `[state:2]` citation token. That is a citation-hygiene gap in the proto-lines file, not an error in this entry. The state-update itself anchors correctly.

A cape-fic reader tracking who-has-what-operational-mode wants this entry. The shift from passive to systematic is the chapter's opening board change. `CORRECT`

**[state:3] @17 — `actor:taylor.internal-accounting.wren-status: unknown -> filed-as-ward-junction-contact-unnamed`**

Scene-B peak. This is the information-asymmetry beat the chapter is built around: Taylor categorizes Wren as a function-node in her coverage map without knowing who she is. From my perspective, this is exactly the state entry I want: the board now records that Taylor has a slot for a person she cannot name. The value `filed-as-ward-junction-contact-unnamed` captures the double-register precisely — Wren is in the ledger, but the ledger entry has no name attached.

First-touch on this field (`<old>` is `unknown`) — no prior chain to verify, but there is no prior chapter entry that would have established a different value. Persistence: handoff_out confirms "Wren: inside coverage map; no direct contact; named internally as ward-junction contact." The strip test: without this entry, downstream chapters receive no canonical record that Taylor has categorized Wren. That matters.

NI co-citation at narrator:4 @17 present. Back=N same citation-gap note as state:2. The field-extension (`internal-accounting.wren-status`) is documented in the entry comment.

`CORRECT`

**[state:4] @24 — `actor:taylor.internal-accounting.coverage-map-recognition-event: not-yet-occurred -> occurred`**

Scene-C peak. The recognition-event flip. The field is `not-yet-occurred -> occurred` — an irreversible binary. The fact that recognition occurred is not undone by the subsequent suppression at @25 (state:5 correctly files the suppression as a separate field on a separate entry at a separate bone). From a lore-tracking standpoint this is the right call: what is tracked is the occurrence of the event, not the character's response to it.

NI co-citation at narrator:6 @24 present. Back=N. Field-extension documented.

`CORRECT`

**[state:5] @25 — `actor:taylor.internal-accounting.coverage-map-recognition-status: unsuppressed -> suppressed-under-harm-reduction`**

The suppression-mechanism entry, decomposed from the recognition-event at @24. The rubric's SOFT-WATCH(1) required these to be structurally separate bones; they are (@24 recognition fires, @25 suppression fires). The entry correctly does not reverse state:4 — recognition having occurred is permanent; what state:5 records is the active filing-discipline Taylor applies to that recognition.

From a cape-fic reader perspective: this is the mechanism of how Taylor operates. The suppression-under-harm-reduction framing is the operative logic — she knows what she built, she files it under a category that makes it bearable, and continues. The canonical state needs to record both the knowing and the filing. It does. NI co-citation at narrator:7 @25 present. Back=N.

`CORRECT`

## File-level read

Five entries on 29 bones. One env, four POV-actor field-extensions. All four POV-actor entries have NI co-citations. The density is below the rubric's nominal 8-18% band (17.2% including env; the env slice alone is below floor at 3.4% with a defended carve-out). The auditor correctly flagged this as a SIGNAL under flag-004 — the carve-out preamble earns the sparse env fire. The actor entries collectively hit the band; the env sparsity is structural.

The chapter's two HARD findings (fault-002 vibes forward-citation, fault-003 loc-state continuity-misplacement) do not touch state-updates. This file is clean.

Back=N on state:2, 3, 4, 5 is a citation-hygiene pattern worth noting for Phase 2 correction — the proto-lines should carry inline state citation tokens at the four actor-state bones. This is not a state-updates entry error; it is a Phase 2 / cite-index maintenance gap.

The board has moved in the right places: mechanism established at @6, first relational-categorization at @17, recognition at @24, suppression at @25. The ledger entries are irreversible and correctly chained. A lore-tracking reader can follow what Taylor built and what she did about it from these five entries alone.

## Convergence trace

No auditor HARD findings map against state-updates entries. fault-002 is vibes; fault-003 is loc-state. flag-004 (env density below floor) is a carve-out-defended SIGNAL — preamble is thorough. The back=N pattern on state:2-5 is visible in the cite-index but the auditor did not escalate it to a state-updates fault (correctly — it is a proto-lines citation-hygiene issue, not a state-updates authoring failure). No divergence between my per-entry readings and the auditor's findings on this facet.
