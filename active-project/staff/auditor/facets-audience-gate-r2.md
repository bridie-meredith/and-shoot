---
audit: facets-audience-gate-r2
episode: s01e02
date: 2026-05-11
cycle: 2
mode: blocking
status: FINDINGS-PRESENT — 5 of 9 facets revise; 4 of 9 facets accept
remediation-context: cycle-2 fixer-only pass (user direction; 5 minimum-change items applied)
totals:
  facets-accept-cycle-2: 4    # tensometer (newly cleared), metaphor + feeling + vibes (carried from cycle 1 ACCEPT)
  facets-revise-cycle-2: 5    # location-state, interest-narrator, sensory, state-updates, memory
  facets-fail: 0
  reviewers-fired-cycle-2: 8 dispatches (1 stalled; mechanically inferred — memory)
  cycles-remaining: 1 (3 cycle cap; cycle 3 budget available but user elected fixer-only-then-verdict)
---

# Phase 5b cycle 2 audience-gate aggregate report

## Per-facet aggregate verdicts (cycle 1 → cycle 2)

| Facet | Cycle 1 | Cycle 2 | Delta |
|-------|---------|---------|-------|
| tensometer | REVISE | **ACCEPT** | ✓ cleared (tens:70 @83 retune; A-001/T-001 closed) |
| location-state | REVISE | REVISE | unchanged (dark-fantasy escalated; 3 atmosphere-thin sensory notes carry-forward) |
| interest-narrator | REVISE 3/3 | REVISE 1/3 | narrator:27 Khepri-fix cleared 3-of-3; narrator:32 @177 dark-fantasy demand persists |
| sensory | REVISE | REVISE | unchanged (sensory:3 loc-state-gap carry-forward; 2 specialists ACCEPT) |
| state-updates | REVISE | REVISE | state:1 type-mismatch repair confirmed clean; state:8 stance-on-tya old-state ungrounded persists (dark-fantasy escalated to demand); state:6 fauna-radius asymmetry closed 3/3 ACCEPT on re-read |
| memory | REVISE 3/3 | REVISE (predicted) | mem:2 + mem:10 cleared; mem:9 relocate + mem:12 contest + Westerosi-clamp gap carry-forward |
| metaphor | ACCEPT 3/3 | ACCEPT (not re-fired) | held |
| feeling | ACCEPT 3/3 | ACCEPT (not re-fired) | held |
| vibes | ACCEPT (single) | ACCEPT (not re-fired) | held |

## Cycle-2 fixer-pass outcome summary

5 minimum-change items applied + verified by audit r3 (CLEAN HARD=0; recalibrated Earth-Bet proper-noun scan clean):
- tens:70 @83 r=1 → r=2 ✓
- narrator:27 @149 "Khepri-threshold" → "foreknowledge-band threshold" ✓
- mem:10 @125 DELETE (Gold Morning hard-fence) ✓
- mem:2 @30 DELETE (condition-card-not-monument) ✓
- state:1 @149 (broken-maester) record_anomaly_logged old-state `true` → `anomaly-noted` ✓

Audit r3 recalibrated CONSTRAINT scan returned CLEAN across all 27 Earth-Bet proper nouns in all facet entry content fields.

## Carry-forward escalations (cycle 2 → user direction terminated; cycle-3 budget unused)

These items exceed minimum-change fixer scope and require R1/R2 author re-dispatch. Documented for orchestrator-critic + user escalation.

### Location-state (atmosphere)
- **[loc-state:5] @83** — sensory note names lintel rather than door-latch-intact condition that ruptures at @85. Dark-fantasy demand.
- **[loc-state:7] @132** — sensory note restates condition (door shut) instead of perceptible meaning.
- **[loc-state:9] @156** — generic "narrow between buildings" instead of Eastern-Quarter-discriminating sensory register (lamp-dark window or side-alley geometry).
- Repair path: loc-state R1 author re-dispatch with cycle-1 callouts + audit r3 backdrop.

### Interest-narrator (channel-saturation)
- **[narrator:32] @177** — apparatus-log-as-instrument channel saturated; entry at @177 r=1 procedural log-write with no co-facets; dark-fantasy demand: author ceiling-defense memo OR delete entry.
- Repair path: NI author/judge defense OR fixer DELETE if no defense forthcoming.

### Sensory (loc-state-gap)
- **[sensory:3] @125** — no loc-state entry anchors Taylor's return to base in @110→@132 window; old-state `stylus-on-wax-rhythm` unanchored. Sensory-old-state-reader strong demand.
- Repair path (a, recommended): loc-state R1 author adds a re-entry beat in @113-@122 band.
- Repair path (b): sensory R1 re-anchor old-state to a loc-state slug with adjacency note.

### State-updates (write-back canonicity)
- **[state:8 stance-on-tya-category]** (oc-tanner-father slice, @22) — old-state `privately-concluded-not-tya` is card-characterization-derived, not anchored in canonical memory or s01e01 state. Dark-fantasy demand: (a) old-state `none` with init-note; (b) anchor to specific s01e01 state entry (doesn't exist); (c) delete + route to margit for card-schema work.
- Repair path: tanner-father impersonator defense pass OR fixer DELETE with margit referral.

### Memory (structural rebuild)
- **[mem:9] @87** — relocate from @87 (tens=3 peak) to @89-@90 (trailing-edge tens=1).
- **[mem:12] @173** — author ceiling-defense memo: witness/action distinction at @173, resonance-not-action argument, why @174 doesn't serve better. If defense holds, KEEP; else DELETE.
- **File-level Westerosi-monument clamp gap** — zero Westerosi fires in 6 surviving entries; doubled-register rubric hard-fail. Add at least one Westerosi-clamp at: broken maester's Citadel-form correspondence, tanner-family customary-wage-claim language, or @149 phrase-the-beetles-carried.
- Repair path: R2 memory judge re-dispatch with structural revision brief OR margit-canonicalization of mem:3/mem:7 monument families.

## Bidirectional loop verdict: VALIDATED (URI-035 first validation)

This is the first validation run of Phase 5b's adversarial gate per URI-035 (deferred from s01e01).

**Shared findings (audience + auditor on same entry, across both paths):**
- tens:70 @83 (A-001 / T-001 ↔ cape-fic-reader cycle-1) — full convergence. RESOLVED by cycle-2 fixer.

**Audience-only findings the auditor's mechanical scan missed:**
- narrator:27 @149 "Khepri-threshold" Earth-Bet proper-noun fence (3-persona) — auditor r1/r2 missed; caught by audience cycle 1; auditor r3 CONSTRAINT scan recalibrated and now substring-scans entry content.
- mem:10 @125 "Gold Morning" Earth-Bet proper-noun in target-reference free-text gloss (worm-canon) — same pattern as narrator:27.
- 5 other audience-only callouts (location-state atmosphere ×3; sensory loc-state-gap; state-updates old-state ungrounded; memory placement+ceiling+register-gap).

**Auditor-only findings the audience did not directly raise on the same entry:**
- 5 SIGNAL-class items (F-002 feeling density, M-001 NI taxonomy, M-002 elder shard taxonomy, A-002 metaphor AP7, S-002 cosmetic merge) — all advisory.

**System verdict:** the adversarial gate worked as designed. Two real hard-fence violations that the mechanical scan missed were caught and routed to cycle-2 fix. The CONSTRAINT scan recalibration recommendation (substring match across entry content) is the durable improvement; filed as URI-AUDITOR-CONSTRAINT-CALIBRATION.

## Cycle-2 status summary

- **Facets ACCEPT (cycle 2):** 4 of 9 — tensometer (newly cleared), metaphor, feeling, vibes.
- **Facets REVISE (cycle 2):** 5 of 9 — location-state, interest-narrator, sensory, state-updates, memory.
- **HARD findings post-audit:** 0 (audit r3 CLEAN).
- **Audience-gate convergence:** 4 of 9 facets at 3-of-3 ACCEPT.
- **Cycle cap status:** 2 of 3 used; cycle 3 budget unused (user direction: fixer-only-then-verdict).

## Status flip

Per spec, status flips to `audited-r1` only on Phase 5b ACCEPT 3-of-3 for ALL 9 facets. That gate is NOT met. Status remains `audited-r1-mechanical` with `audience_gate_cycle_2: revise` and `audience_gate_cap_burned: false` (not at cap; user-terminated).
