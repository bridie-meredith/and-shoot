audience-gate: facets-audience-gate-r2
episode: b01c10
date: 2026-06-02
cycle: 2 (final)
aggregation: strict 3-of-3 ACCEPT per facet (URI-AUDIENCE-AGGREGATION-RULE)
final_status: ALL-FACETS-ACCEPT

## Per-facet final aggregate (cycle 2 where re-fired; cycle 1 otherwise)

| facet | cape-fic | dark-fantasy | worm-canon | aggregate | cycles |
|-------|----------|--------------|------------|-----------|--------|
| location-state    | accept (c1) | accept (c1) | accept (c1) | ACCEPT 3/3 | 1 |
| interest-narrator | accept (c2) | accept (c1) | accept (c2) | ACCEPT 3/3 | 2 |
| state-updates     | accept (c1) | accept (c1) | accept (c1) | ACCEPT 3/3 | 1 |
| memory            | accept (c1) | accept (c1) | accept (c2) | ACCEPT 3/3 | 2 |
| feeling           | accept (c1) | accept (c1) | accept (c1) | ACCEPT 3/3 | 1 |
| metaphor          | accept (c1) | accept (c1) | accept (c1) | ACCEPT 3/3 | 1 |
| vibes             | accept (c1) | accept (c1) | accept (c1) | ACCEPT 3/3 | 1 |
| exposition        | accept (c1) | accept (c1) | accept (c1) | ACCEPT 3/3 | 1 |

| facet | sensory-disambiguation-pedant | sensory-modality-coverage | sensory-old-state-reader | aggregate | cycles |
|-------|-------------------------------|---------------------------|--------------------------|-----------|--------|
| sensory | accept (c2) | accept (c1) | accept (c2) | ACCEPT 3/3 | 2 |

**All 9 facets: ACCEPT 3/3 strict aggregate.** 3 facets failed cycle-1 strict 3/3 (interest-narrator, memory, sensory); cycle-2 fixer pass (3 REVISEs) remediated all 3 to 3/3 ACCEPT. No cap-burn. Converged at cycle 2 of 3.

## Cycle-2 remediation → ACCEPT trace
- interest-narrator: cape-fic REVISE (narrator:7 @16 inert) → fixer reworded narrator:7 to earned attention-landing → cape-fic ACCEPT ("names the information asymmetry directly... attention-landing, not infrastructure"). worm-canon REVISE (narrator:8 @24 doubling) → resolved by mem:2 reword → worm-canon ACCEPT (narrator:8 now sole closing-simile, no rhyme). mem:1 @16 spine intact; NI held at 7 fires (25.9% accepted spine-over-band tradeoff).
- memory: worm-canon REVISE (mem:2 @24 doubled closing-simile) → fixer reworded mem:2 to continuation/accumulation construction (displacement + Khepri-ABSENT + "bodies it never asked" preserved) → worm-canon ACCEPT (monument-grade intact, fence held).
- sensory: disambiguation + old-state REVISE (sensory:7 @25 unanchored old-state) → fixer reframed to end-of-day-station-quiet → ledger-cover-close (spike), anchored loc-state:7 @20 → both specialists ACCEPT (traces verbatim to loc-state baseline).

## Targeted re-audit (Phase 5 re-fire, scoped to the 3 cycle-2 REVISEs)
The cycle-2 changes were 3 text-only REVISEs (no new entries, no anchor/ID changes, no structural changes). Targeted mechanical re-scan performed (not a full 60-entry auditor re-dispatch — disproportionate to scope):
- entry-text Earth-Bet hard-fence scan on reworded mem:2 @24 + narrator:7 @16: CLEAN.
- sensory:7 @25 old-state resolution to loc-state:7 @20: CONFIRMED.
- cite-index rebuild post-fixer: CLEAN (no stale; IDs/anchors/tokens unchanged).
- New HARD findings: 0. Phase 5 gate (HARD=0) holds.

## Convergence trace
- Auditor findings (Phase 5): 16 (0 HARD, 16 SIGNAL).
- Audience callouts cycle-1 (deduped): 3 (sensory:7 @25; @24 doubling; narrator:7 @16).
- Shared findings (audience + auditor both flagged same entry): @24 figurative-register proximity (auditor DEDUP advisory + worm-canon revise + metaphor-R2 AP4).
- Audience-only: sensory:7 @25 old-state lineage (specialists' lane; auditor passed under grounding-exemption); narrator:7 @16 per-entry merit (auditor flagged 25.9% band as SIGNAL but did not drill per-entry).
- Bidirectional loop verdict: VALIDATED (≥1 shared finding: the @24 doubling).

## Phase 5c — admin process-critic
SKIPPED. Final-cycle (cycle 2) Phase 5b is clean ACCEPT 3-of-3 across all 9 facets AND no cap-burn was used → per /and-facets Phase 5c skip rule, no process-critic dispatch.
