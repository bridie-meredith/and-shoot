audience-gate: facets-audience-gate-r1
episode: b01c10
date: 2026-06-02
cycle: 1
aggregation: strict 3-of-3 ACCEPT per facet (URI-AUDIENCE-AGGREGATION-RULE; single dissent fails)

## Per-facet aggregate (cycle 1)

| facet | cape-fic-reader | dark-fantasy-reader | worm-canon-pedant | aggregate |
|-------|-----------------|---------------------|-------------------|-----------|
| location-state    | accept | accept | accept | ACCEPT 3/3 |
| interest-narrator | revise | accept | revise | FAIL |
| state-updates     | accept | accept | accept | ACCEPT 3/3 |
| memory            | accept | accept | revise | FAIL |
| feeling           | accept | accept | accept | ACCEPT 3/3 |
| metaphor          | accept | accept | accept | ACCEPT 3/3 (0-entry refuse-by-default confirmed) |
| vibes             | accept | accept | accept | ACCEPT 3/3 |
| exposition        | accept | accept | accept | ACCEPT 3/3 (binding ctx-001 exemption honored by all 3) |

| facet | sensory-disambiguation-pedant | sensory-modality-coverage | sensory-old-state-reader | aggregate |
|-------|-------------------------------|---------------------------|--------------------------|-----------|
| sensory | revise | accept | revise | FAIL |

PASS (6): location-state, state-updates, feeling, metaphor, vibes, exposition.
FAIL (3): interest-narrator, memory, sensory.

## Consolidated revise callouts (deduped) → cycle-2 fixer

1. [sensory:7] @25 — old-state `ledger-accounting-writing-sound` unanchored. CONVERGENT (sensory-disambiguation-pedant + sensory-old-state-reader, independently, same entry, same fix). Fix: old-state `end-of-day-station-quiet` -> new-state `ledger-cover-close`, modality sound, tag spike, anchored loc-state:7 @20. No loc-state edit required.
2. [mem:2] @24 + [narrator:8] @24 — doubled closing-simile structure ("X closing the way Y closed") at the same anchor. CONVERGENT (worm-canon-pedant flagged on BOTH interest-narrator and memory; metaphor-R2 judge corroborated via AP4; dark-fantasy-reader noted as deliberate-chord stitch-carry). Fix: reword mem:2 @24 to approach the override-architecture displacement from a non-closing-simile angle, preserving the Khepri-ABSENT echo + the displacement semantics. Resolves worm-canon's memory revise AND the narrator:8 doubling in one edit.
3. [narrator:7] @16 — inert spine-provision; reads as infrastructure not earned attention-landing (cape-fic-reader). Fix: reword narrator:7 to a genuine attention-landing at the side-exit apparatus-recognition beat, KEEPING the mem:1 @16 NI-spine (do NOT trim — relocation fallback is circular: no co-cited anchor exists at @19). NI stays at 7 fires; the 25.9% band-stretch is the documented spine-over-band tradeoff (FREQUENCY-BAND SIGNAL, not a gate-fail driver).

## Audience-side ADDs proposed (non-mandatory, SIGNAL)
- dark-fantasy-reader, interest-narrator @21: optional minimal NI fire on the inscription act's permanence in accounting-register (NOT via Taylor interior; via ledger-as-form). SIGNAL weight; deferred — @21 memory-silence is a deliberate Khepri-ABSENT protected pattern and NI-at-@21 risks the same affirmation-by-naming. NOT actioned cycle 2.

## Named carries to /and-stitch (not revise triggers)
- narrator:8 @24 / mem:2 @24 figurative proximity: Phase 4 render as deliberate chord, not accidental rhyme (resolved at facet layer by callout 2 reword; stitch still honors the chord).
- state-updates @21 moral_framework floor-crossing (0.5->0): Phase 4 must not render @21 texture-equivalent to @10 (decrement).
- exposition @0 "column/closes" near-rhyme (Phase 1); exposition:4 @2 "consideration the function is owed against" prepositional inversion (Phase 4 craft).
- (carried from Phase 4.5) VF-1 surrender @10/@11; VF-2 detention @15/@17/@18; VF-3 terminal face @27; VF-4 @13 interval bridge.

## Convergence trace
- Auditor (Phase 5) findings: 16 (0 HARD, 16 SIGNAL).
- Audience callouts (deduped): 3 (sensory:7 @25; @24 doubling; narrator:7 @16).
- Shared findings (audience + auditor both flagged same entry): DEDUP advisory @24 (auditor flagged mem:2/@24 + narrator:8/@24 figurative-register proximity as DEDUP advisory; audience worm-canon escalated it to revise). -> overlap present.
- Audience-only: sensory:7 @25 old-state (auditor passed it under grounding-exemption without old-state lineage walk — the specialists' lane); narrator:7 @16 inert (auditor noted 25.9% band as SIGNAL but did not drill per-entry merit).
- Auditor-only: the 14 other SIGNALs (band, carve-outs, margit-referral, actor-state NI advisory).
- Bidirectional loop verdict: VALIDATED (≥1 shared finding: the @24 doubling, flagged by both paths).
