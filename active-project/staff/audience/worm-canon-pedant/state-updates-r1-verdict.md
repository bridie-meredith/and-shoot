---
reviewer: worm-canon-pedant
facet: state-updates
episode: b01-c02
cycle: r1
date: 2026-05-25
verdict: accept
---

# Worm Canon Pedant — State-Updates Adversarial Verdict (b01-c02)

## Stance

Keeping the tally. State-updates is where the power mechanics land in canonical memory — it is the record of what actually changed versus what the chapter claimed changed. My primary lens is whether the entries are consistent with established canon for this character's capabilities and with the field-extension architecture established in prior chapters. My secondary lens is chain integrity: do the `<old>` values trace cleanly?

The b01c01 state-updates file introduced `deployment-state` as a field-extension on actor:taylor. That extension carries forward here. The chapter introduces three new field-extensions under `internal-accounting`. I will track whether those extensions are consistent with canon-Taylor's established cognitive register.

## Per-entry readings

**[state:1] @20 — `studio.time_of_day: dawn -> end-of-day`**

The env entry. Time-of-day is a studio field with established schema authority. The chapter opens at dawn (b01c01 handoff_out baseline) and closes at end-of-day; the field flips at @20 (scene-C open, Taylor returns to the drain angle). Persistence: confirmed through @29. The strip test passes. The carve-out preamble covers all silent env bones with documented rationale.

SEAM-001: b01c01 authored zero env state-updates, so the `<old>` value "dawn" derives from handoff_out baseline rather than from a prior state-update chain entry. From a canon-chain perspective this is the concern I want on record: the chain from the series-baseline through b01c01 to this entry exists only via handoff_out documentation, not via a prior `studio.time_of_day` state-update. That is a chain-integrity gap that the preamble acknowledges correctly. It is a SIGNAL, not an entry fault. The chain is traceable; it is just not documented in the state-updates layer for b01c01.

`CORRECT`

**[state:2] @6 — `actor:taylor.deployment-state: ambient-subsistence-reading -> systematic-precinct-coverage-deliberate`**

The deployment-state field was introduced at b01c01 as a field-extension. The b01c01 entry established `passive-subsistence-range` (or equivalent) as the starting value; the b01c01 handoff_out confirmed the chapter-close deployment-state as the carry-forward value into b01c02. The b01c02 entry opens with `ambient-subsistence-reading` as `<old>` — this should match the b01c01 handoff_out canonical value. If the handoff_out reads `passive-subsistence-after-crowd-yield` or similar, the `<old>` nomenclature here (`ambient-subsistence-reading`) needs to match exactly, not rephrase. The entry's own comment says "chapter-open value was passive-subsistence-after-crowd-yield" — the comment acknowledges the prior value; the `<old>` field uses a slightly different phrasing. This is a Frugality flag (drift-old): the `<old>` value should be whatever the prior canonical entry set, verbatim, not a paraphrase.

From a canon-mechanics standpoint, the distinction being tracked — ambient-passive versus systematic-deliberate — is a valid and canon-consistent distinction for Taylor's insect-sense. In Worm source, Taylor can choose to focus her power actively or let it run passively. The "deliberate coverage" mode is the mode she uses when running tactical reconnaissance. The b01c02 chapter is the first time in this AU she runs deliberate reconnaissance in Flea Bottom. The field-extension tracks the right thing.

The back=N on the proto-line @6 is a citation-hygiene gap, not an entry error.

Mild flag on `<old>` value phrasing — should be verified against b01c01 handoff_out exact language. Not escalating to reject; the comment inside the entry acknowledges the prior value, which suggests the author knows what the chain should say.

`CORRECT (with note: verify <old> exact phrasing against b01c01 handoff_out canonical value; comment and entry field diverge slightly)`

**[state:3] @17 — `actor:taylor.internal-accounting.wren-status: unknown -> filed-as-ward-junction-contact-unnamed`**

New field-extension: `internal-accounting.wren-status`. I am checking whether this is canon-consistent.

In Worm source, Taylor maintains an internal organizational system for her insects and for the people she monitors. She categorizes people by function — "the guy with the crossbow," "the girl with the knife" — before she has names. The `internal-accounting.wren-status` field tracks Taylor's internal categorization of Wren in exactly this mode: a function-label for an unnamed person in her coverage architecture. This is canon-Taylor cognitive behavior.

The field-extension comment documents the extension. The `<old>` is `unknown` (first-touch; no prior entry). The `<new>` is `filed-as-ward-junction-contact-unnamed` — the naming convention is internally consistent with the clinical register established in the chapter. Persistence: handoff_out confirms the categorization persists.

This is a new field at a scene-B peak bone (@17 is in the peak-bones array, per the auditor's CURVE-SHAPE confirmation). State-update on a peak-bones-class bone is strongly expected by the rubric. The fire is correct and correctly timed.

NI co-citation at narrator:4 @17 present. Back=N.

`CORRECT`

**[state:4] @24 — `actor:taylor.internal-accounting.coverage-map-recognition-event: not-yet-occurred -> occurred`**

New field-extension: `internal-accounting.coverage-map-recognition-event`. This is the chapter's moral-axis event: Taylor recognizes that the coverage architecture she has built is surveillance over forty-three non-consenting people — the Khepri-pattern in miniature.

The field form `not-yet-occurred -> occurred` is a clean irreversible boolean. The naming (`coverage-map-recognition-event`) distinguishes the event of recognition from the status-of-recognition (state:5 at @25). That two-entry decomposition is the correct architecture for this moment: the event fires at @24 (the crack arrives), the suppression fires at @25 (the response to the crack).

From a canon-Taylor standpoint: the recognition pattern — "I built the thing I said I wouldn't build; I see it; I continue" — is the core arc of her Worm source characterization. The field-extension correctly captures an irreversible first-occurrence. `not-yet-occurred -> occurred` cannot be reversed; there is no entry type that writes it back to `not-yet-occurred`. This is the correct permanence.

NI co-citation at narrator:6 @24 present. Back=N. Field-extension documented.

`CORRECT`

**[state:5] @25 — `actor:taylor.internal-accounting.coverage-map-recognition-status: unsuppressed -> suppressed-under-harm-reduction`**

New field-extension: `internal-accounting.coverage-map-recognition-status`. The chapter's SOFT-WATCH(1) required the recognition-event and its suppression to be structurally separate bones. They are. @24 fires the event; @25 fires the discipline applied to the event.

The `<old>` is `unsuppressed` — a first-touch value implied by the recognition event having fired at @24. The entry comment notes the persistence ("absolute through chapter close") and the handoff_out confirmation ("first moral_legibility crack: coverage-map recognition suppressed under harm-reduction framing").

Worm canon check: the `harm-reduction framing` vocabulary is the AU-specific adaptation of Taylor's Worm-source suppression patterns. In Worm source, Taylor uses utilitarian cost-benefit accounting to suppress recognition of her own moral violations ("I am the lesser evil," "this is for the greater good"). The harm-reduction framing is the KL-122ac AU's version of that same cognitive mechanism, adapted to the Westerosi context. The AU acknowledges the divergence (KL geography, not Brockton Bay) without violating the character's established suppression architecture. This tracks.

NI co-citation at narrator:7 @25 present. Back=N. Field-extension documented.

`CORRECT`

## File-level read

Five entries. No stat-increments posted as mid-chapter canonical state flips (the b01c01 concern with `capability_axis: 2 -> 3` and `social_tether_prot_axis: 1 -> 2` is not replicated here). The b01c02 actor entries are all field-extensions on `internal-accounting.*` — a sub-namespace that cleanly separates Taylor's ledger-operations from operational-mode fields (`deployment-state`) and physical-state fields (position, orientation). The sub-namespace architecture is consistent with canon-Taylor's established cognitive register.

Chain integrity: the `<old>` phrasing on state:2 deserves verification against b01c01 handoff_out exact language (noted above as a soft concern). All other `<old>` values are first-touch or cleanly derived.

SEAM-001 (env chain) is an acknowledged process gap in the preamble. The author knows it is there and has documented it. The chain is traceable via handoff_out; the gap is a citation-layer issue, not a content error.

Back=N on state:2, 3, 4, 5 is a proto-lines citation-hygiene pattern. It means four of the five actor-state entries have no inline citation token on their anchor proto-lines. This is worth correcting in the Phase 2 cite-index maintenance pass, but it is not an error in the state-updates entries themselves.

No power-mechanic legibility failures. No stat-increment-as-canonical-state-flip misuse. No cross-POV authority violations. No registration-as-state contamination. The file is clean.

The chapter's two HARD findings (fault-002 vibes forward-citation, fault-003 loc-state continuity-misplacement) do not touch state-updates. No convergence with state-updates entries.

## Convergence trace

| Concern | Auditor finding | Overlap |
|---|---|---|
| state:2 `<old>` phrasing vs. b01c01 handoff_out exact value | Not flagged by auditor (auditor found zero CONTRADICTION findings) | No convergence; soft concern only from chain-integrity read |
| SEAM-001 env chain gap | flag-004 (carve-out defended, SIGNAL) | Convergent — auditor and this reader reach same conclusion (process gap, not entry error) |
| back=N on state:2-5 | Cite-index pattern; not escalated by auditor to state-updates fault | Consistent non-escalation |
| No stat-increment misuse (per b01c01 concern) | Zero RUBRIC-FIDELITY findings on state-updates | Convergent |
