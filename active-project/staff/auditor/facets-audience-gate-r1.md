report: facets-audience-gate-r1
episode: b01c01
date: 2026-05-19
mode: facet-adversarial; strict 3-of-3 aggregation per URI-AUDIENCE-AGGREGATION-RULE
parent_audit: active-project/staff/auditor/facets-final-audit.md + facets-final-audit-r2-verify.md
cycle: 1 of 3 (user-requested early stop; cap_burned at cycle 1)
status: PARTIAL — 7 facets ACCEPT, 5 facets REVISE/FAIL

---

## Per-facet aggregate (cycle 1)

| Facet | Reviewers fired | Aggregate | Notes |
|---|---|---|---|
| location-state | cape-fic / dark-fantasy / worm-canon | **REVISE** (2R/1A) | loc-state:3 @11 absent-stillness anchor; loc-state:4 @13 AP3 register-mismatch (thermal under "no-change"); cite-index back=N pair |
| interest-narrator | cape-fic / dark-fantasy / worm-canon | **REVISE** (2R/1A) | converges with auditor AP-001 (NI "X is what Y" template ×3); narrator:3 reader-only seam |
| sensory | sensory-disambiguation-pedant / sensory-modality-coverage / sensory-old-state-reader (specialists) | **REVISE** (2A/1R) | modality-coverage: @13 thermal gap (loc-state:4 explicit cooling event; sensory file 67% sound-dominant); 3-entry count breaches 3-6% band |
| state-updates | cape-fic / dark-fantasy / worm-canon | **FAIL** (3R/0A) | 5 revision targets: :8 vouching-vector framing too early; :10 active-holding semantic ambiguity + back=N; :13 recurring forward-projection; :15 auto-initiating canon-deviation needing condition-card cite; :17 @26 anchor lag vs @22 |
| memory | cape-fic / dark-fantasy / worm-canon | **REVISE** (3R-ish — see notes) | file-level single-register (Earth-Bet-only) clamp gap; mem:1 placement; mem:2 missing monument-card via margit referral |
| feeling | dark-fantasy / worm-canon / pulp-enthusiast | **ACCEPT** (3/3) | shared sparsity-denominator note (cape-fic-reader substituted by pulp-enthusiast — PROCESS DEVIATION) |
| metaphor | dark-fantasy / worm-canon / pulp-enthusiast | **ACCEPT** (3/3) | dark-humor register held; one stitcher advisory at @23 (no warmth); cape-fic substituted (PROCESS DEVIATION) |
| vibes | cape-fic / dark-fantasy / worm-canon | **ACCEPT** (3/3) | three advisories: vibes:21 @25 cite vs off-anchor; vibes:4 token-in-isolation; vibes:17 world-build slug doesn't resolve (warehouse card not renamed) |
| exposition | cape-fic / dark-fantasy / worm-canon | **ACCEPT** (3/3) | cold-start override validated; two non-blocking ADD advisories ("the Hook"; swarm/pattern-read forward-watch) |
| dialogue-taylor | cape-fic / dark-fantasy / worm-canon | **ACCEPT** (3/3) | V2 affirmative; V3 seams all upstream (state/feel proximity at @25) |
| dialogue-coll | cape-fic / literary-snob / pulp-enthusiast | **ACCEPT** (3/3) | dark-fantasy + worm-canon substituted (PROCESS DEVIATION); architecture-dependent (chapter payback structurally present) |
| dialogue-wren | cape-fic / dark-fantasy / worm-canon | **ACCEPT** (3/3) | V2 affirmative; three V3 seams all upstream (narrator:5 @21 + state-wren:@22 + feel-wren:@22) |

**Aggregate: 7 ACCEPT / 5 REVISE-or-FAIL / 12 facets total.**

## Process deviations

The audience-subagent dispatches in facet-adversarial mode did not consistently load the project's configured trio (cape-fic-reader + dark-fantasy-reader + worm-canon-pedant). Substitutions observed:
- `metaphor` review fired with pulp-enthusiast in place of cape-fic-reader.
- `feeling` review fired with pulp-enthusiast in place of cape-fic-reader.
- `dialogue-coll-net-mender-flea-bottom` review fired with literary-snob + pulp-enthusiast in place of dark-fantasy-reader + worm-canon-pedant.

All three facets accepted unanimously under their substituted lineup, so the ACCEPT verdict is not invalidated, but the convergence-trace counts that follow exclude these substitutions from the "trio convergence" computation. The pattern reads as audience-subagent default trio-loader picking from `staff/audience/INDEX.md` rather than `active-project/audience/` when the dispatch prompt did not explicitly enumerate persona slugs. Recommendation for follow-on: enumerate persona slugs explicitly in every Phase 5b dispatch prompt; or tune the audience subagent's facet-adversarial mode to require active-project membership read first.

## Convergence trace

- Auditor findings (Phase 5 final): 9 (2 HARD remediated cycle-0; 7 SIGNAL standing)
- Audience callouts (across all reviewers, deduped at entry granularity): ~21 (5 state-updates + 2 loc-state + 2 NI + 2 sensory + 3 memory + 7 advisories from accepted facets)
- Shared findings (audience + auditor both flagged the same entry):
  - **AP-001 (NI X-is-what-Y template ×3)** — auditor AP-SCAN + cape-fic-reader + dark-fantasy-reader on interest-narrator. CONVERGED.
  - **FB-002 (sensory 3-entry count vs 1-2 band)** — auditor FREQUENCY-BAND + sensory-modality-coverage. CONVERGED.
  - **C-001 vibes:21 citation residue** — auditor CONSTRAINT (remediated cycle-0) + cape-fic-reader vibes verdict (residual @25 cite advisory). PARTIAL-CONVERGED.
  - **C-002 vibes:17 keyword fence** — auditor CONSTRAINT (remediated cycle-0) + worm-canon-pedant vibes verdict (warehouse slug rename gap). PARTIAL-CONVERGED.
- Audience-only findings: ~17 (most state-updates callouts; memory file-level register clamp; loc-state stillness anchor; sensory thermal gap)
- Auditor-only findings: ~4 (FB-001 exposition over-band; S-001/S-002 structural housekeeping; TF-001 bare work-bone gap)

**Bidirectional loop verdict: VALIDATED.** At least one shared finding (AP-001 NI template) corroborated by both the mechanical scan and the adversarial reading. Multiple partial-convergences strengthen the loop. Not all signals shared, but the cross-checks fired.

## Disposition (per user instruction)

User selected **early cap-burn** at cycle 1 (cycle cap is 3; full cycle 2 would have required fixer remediation across 5 facets + scaffolding a new monument-card for memory via margit referral + re-firing ~9-15 dispatches). Status:

- Showrunner-memory status remains `audited-r1-mechanical` (NOT promoted to `audited-r1`).
- `audience_gate_cap_burned: true` (semantic: early-cap at cycle 1 by user election, not protocol-cap at cycle 3).
- `audience_gate_cycles: 1`.
- Orchestrator-critic verdict expected: NOT-SUCCESSFUL (5 facets not ACCEPT-3-of-3).

## Standing callouts (carry-forward; not actioned this run)

**REVISE-CLASS (5 facets):**
1. location-state — loc-state:3 @11 anchor: re-anchor or supply absent-stillness rationale; loc-state:4 @13 thermal-under-no-change AP3 register-fix.
2. interest-narrator — collapse one of the three "X is what Y" closes (narrator:2 / narrator:4 / narrator:6); R2 self-flagged risk has now caught.
3. sensory — author thermal entry at @13 (loc-state:4 licenses); drop one sound entry if 3-entry count budget overruns.
4. state-updates — 5 targeted edits enumerated above.
5. memory — Westerosi-monument clamp file-level gap; mem:1 placement defense; margit referral for monument-card to back mem:2.

**ADVISORIES from accepted facets (do not block; surface to downstream):**
- vibes:21 @25 residual cite (advisory only post-fixer; off-anchor is schema-valid).
- vibes:17 `world-build:override-architecture-residue-122ac` reference resolution (warehouse slug rename or alias entry).
- exposition "the Hook" forward-watch.
- exposition swarm / pattern-read forward-watch.
- /and-stitch: @23 metaphor: no warmth in voice-transform.
- /and-stitch: bare work-bone runs @6-@7, @16-@17 — fusion-eligible by inference (scene-map no longer carries fusion-eligible-runs under URI-SUBSTANCE-OVERHAUL).
- /and-stitch: dialogue-Taylor @25 — feel:1 + mem:2 + narrator:6 proximity at the hinge for restraint-felt-as-earned.
