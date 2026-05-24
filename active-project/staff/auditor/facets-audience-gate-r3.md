---
report: facets-audience-gate
chapter: b01c01
cycle: 3
of_cycles_cap: 3
date: 2026-05-24
mode: facet-adversarial (strict 3-of-3 ACCEPT per facet; URI-AUDIENCE-AGGREGATION-RULE)
reviewers_fired: 6 dispatches (interest-narrator × 3 active-audience + vibes × 3 active-audience; dialogue-coll did not re-fire — cap-burn DELETE executed pre-Phase 5b; 9 cycle-2-resolved facets did not re-fire)
aggregate: PASS-WITH-CAP-BURN (8 facets ACCEPT 3-of-3 + 3 deferred-with-attribution + 1 cap-burn DELETE / 0 fail)
stage: cycle-3-complete-with-cap-burn
---

# Audience-gate Report — b01c01 cycle 3

The third and final cycle of Phase 5b adversarial review fired 6 reviewer dispatches across 2 facets (interest-narrator + vibes). The third failing facet (dialogue-coll) did NOT re-fire — its single offending entry was DELETED at cycle-3 ADD pre-validation failure per URI-FACETS-CAP-BURN-SEMANTICS A2 (see cap-burn report). Strict 3-of-3 ACCEPT aggregation rule applied per URI-AUDIENCE-AGGREGATION-RULE.

**Verdict tally (per-reviewer):** ACCEPT 6 / REVISE 0 / FAIL 0.

---

## Per-facet aggregate (cycle 3)

| Facet | cape-fic | dark-fantasy | worm-canon | Aggregate | Cycle-2 |
|---|---|---|---|---|---|
| interest-narrator | ACCEPT | ACCEPT | ACCEPT | **ACCEPT** ✓ | FAIL |
| vibes | ACCEPT | ACCEPT | ACCEPT | **ACCEPT** ✓ | FAIL |
| dialogue-coll | (did not re-fire) | (did not re-fire) | (did not re-fire) | **CAP-BURN-DELETE** | FAIL |

Both cycle-3 audience-gate dispatches cleared 3-of-3 cleanly. Cycle-3 fixer changeset (A1/A2 NI content recasts; B1-B5 vibes token + license trim) resolved the dark-fantasy and cape-fic dissents that drove the cycle-2 FAILs.

---

## Cycle-3 fixer outcome — facets cleared

The cycle-3 fixer pass landed:

- **A1** `narrator:7 @20` recast from ledger-satisfaction ("the day closed under the count she had been running with nothing moved that needed not to be moved") to ledger-cost ("the day held under the count she had been running and the weight of what she had not done was in the count"). Three reviewers cleared cleanly:
  - cape-fic: "held" correctly flags the prohibition as live load rather than archived.
  - dark-fantasy: cycle-2 demand met — surfaces the weight of the withheld action as a cost carried in the ledger, not an audit-result.
  - worm-canon: "held" correctly models a prohibition running under weight rather than filed; post-Khepri accounting consistent.

- **A2** `narrator:5 @24` recast from author-annotation ("observation-radius confirmed before she named it a radius; the circuit count was already in the entry before she decided not to enter it") to completed-fact interior register ("she had already mapped the observation-radius and run the circuit count before the held label registered that she had"). Three reviewers cleared cleanly:
  - cape-fic: completed-fact pre-calc makes the approach-to-payload sequence tactically legible.
  - dark-fantasy: cycle-2 demand met — fires from inside the automatic-assessment reflex rather than annotating it from above; matches rubric calibration anchor form.
  - worm-canon: pre-calc completed-fact tense with interior-discipline self-catch is consistent with Taylor's canonical automatic-assessment architecture.

- **B1** `vibes:2 @6` `licensed-by` trim — `state-update:2` removed; chain is now `state-update:1, proto:6` (both operative). Cape-fic cycle-2 cleared; fault-017 MOOT on vibes:2.

- **B2** `vibes:5 @13` `confirmed-on-screen-b01c01` → `overhead-that-runs-without-charging-the-ledger` (disposition: idle-surveillance cost as suppression-texture; downstream feeling-fork selectable). Dark-fantasy cycle-2 cleared.

- **B3** `vibes:7 @26` `first-on-screen-naming-of-what-she-saw` + `the-flies-report-as-demonstration` → `names-the-proximate-not-the-meaning` + `withholds-the-frame-delivers-the-data` (dispositions: Wren's noticing-class + reporting-shape; distinct downstream-operator behaviors). Dark-fantasy cycle-2 cleared.

- **B4** `vibes:8 @26` `the-follow-up-withheld-on-screen` → `question-the-ward-keeps-to-itself`; `first-confirmed-shape-of-the-mutual-silence` → `shape-of-the-mutual-silence-going-forward` (dispositions: relationship-rule going forward, stripped of provenance flavor). Dark-fantasy cycle-2 cleared.

- **B5** `vibes:9 @27` `the-anomaly-confirmed-on-screen` → `the-gap-in-the-ledger-that-does-not-close` (disposition: unadministered-relationship as accumulating-cost at the chapter's payload beat). Dark-fantasy cycle-2 cleared; load-bearing edit at the densest beat.

Auditor AP8 sentence-parsability PASS on both borderline new tokens (`names-the-proximate-not-the-meaning`, `withholds-the-frame-delivers-the-data`) — precedent-consistent with `holds-the-eyes-does-not-file` form. Dark-fantasy gate-6 operator-actionability PASS on all five replaced tokens. Worm-canon canon-register PASS on the `ward` slot (Planetos social-designation, not PRT-Earth-Bet).

These landings cleared 2 of 2 retried facets to 3-of-3 ACCEPT.

---

## Cap-burn DELETE — dialogue-coll

The third failing facet (dialogue-coll) was resolved via cap-burn DELETE per URI-FACETS-CAP-BURN-SEMANTICS A2, executed proactively at the cycle-3 fixer dispatch (the fixer's state-updates-Coll ADD candidate at @8 failed pre-validation on three rubric axes — Reality / AP#9 density-on-flat / Authority-invented-field — per URI-FACETS-CYCLE-N-ADD A3). The DELETE removed entry 1 (`coll-net-mender-flea-bottom:1 @8`) from `theater/dialogue/coll-net-mender-flea-bottom.md` and triggered the cite-index cascade (`[coll-net-mender-flea-bottom:1]` stripped from proto-line @8). Phase 5b cycle-3 did not re-fire on dialogue-coll — the cycle-2 dissent was resolved by entry removal, not by adversarial re-clearance.

Trade-off accepted at cap-burn:
- bare speech bone @8 (URI-DIALOGUE-COVERAGE-GATE; auditor fault-030)
- Coll speaker file body empty / zero entries (Phase 6 ≥1-entry gate; auditor fault-031)

Both faults are ACCEPTED-AT-CAP-BURN in the Phase 5 cycle-3 auditor report. Cap-burn report at `staff/auditor/facets-cap-burn-b01c01-20260524T021822Z.md`.

---

## Cycle-3 final aggregate (post-arbitration + post-cap-burn)

| Facet | Resolution path | Verdict | Cycle |
|---|---|---|---|
| location-state | cleared cycle-2 (post-F2 carry-license reclassification) | **ACCEPT 3-of-3** | 2 |
| interest-narrator | cleared cycle-3 (A1+A2 content recasts) | **ACCEPT 3-of-3** | 3 |
| sensory | deferred-with-attribution (pulp-enthusiast arbiter ruling A on shape-level) | **ACCEPT-DEFERRED** | 2 |
| state-updates | cleared cycle-2 (post-F6 prop card; post-H4 state:10 strip) | **ACCEPT 3-of-3** | 2 |
| memory | deferred-with-attribution (pulp-enthusiast arbiter ruling A on mem:1) | **ACCEPT-DEFERRED** | 2 |
| feeling | cleared cycle-2 (post-fault-008 per-slice repair) | **ACCEPT 3-of-3** | 2 |
| metaphor | cleared cycle-2 (no callouts surfaced post-fixer) | **ACCEPT 3-of-3** | 2 |
| vibes | cleared cycle-3 (B1 license trim + B2-B5 token replacements) | **ACCEPT 3-of-3** | 3 |
| exposition | cleared cycle-2 (no callouts surfaced post-fixer) | **ACCEPT 3-of-3** | 2 |
| dialogue-coll | cap-burn DELETE (cycle-3 ADD pre-validation failed) | **CAP-BURN-DELETE** | 3 |
| dialogue-taylor | deferred-with-attribution (pulp-enthusiast arbiter ruling A on taylor:2) | **ACCEPT-DEFERRED** | 2 |
| dialogue-wren | cleared cycle-1 (held cycle-2 + cycle-3) | **ACCEPT 3-of-3** | 1 |

**Tally:** 8 ACCEPT 3-of-3 + 3 ACCEPT-DEFERRED + 1 CAP-BURN-DELETE / 0 FAIL.

Phase 5b gate semantics: 8 facets passed under strict 3-of-3; 3 facets passed under arbiter override with dissent attribution; 1 facet resolved via cap-burn DELETE with trade-off attribution. **Strict-aggregation gate: not met (3 facets deferred + 1 cap-burned).** **Resolution-path gate: met (all 12 facets carry a documented disposition).**

---

## Convergence trace (Phase 5 auditor ↔ Phase 5b audience, cycle 3)

- Auditor HARD findings (post-cycle-3): 3 — all ACCEPTED (fault-030 bare-speech-bone cap-burn; fault-031 empty speaker file cap-burn; fault-021 sensory exemption carry).
- Auditor SIGNAL findings: 7 (cycle-2 carry-through; fault-017 + fault-020 MOOT post-fixer).
- Audience callouts (cycle 3, across all 6 reviewers, deduped): 0 distinct revise-grounds. All cycle-2 callouts resolved by A1/A2/B1-B5 edits.
- Shared findings (auditor + audience both flag the same entry/seam at cycle 3): cap-burn faults (fault-030 + fault-031) — auditor flagged structurally; audience would have flagged dialogue-coll @8 had it re-fired (cycle-2 dark-fantasy DEMAND escalation). Resolution is the DELETE itself; convergence is on the cap-burn disposition rather than on a callout-share.
- Audience-only findings (cycle 3): none new.
- Auditor-only findings (cycle 3): the two cap-burn HARDs; sensory exemption carry.

**Bidirectional loop verdict: VALIDATED (preserved from cycle-2).** Cycle-3 changes resolve or cap-burn-accept all shared findings. No new shared-finding gaps introduced.

---

## Stall / underdmanned-facet incidents

None. All 6 cycle-3 dispatches returned verdicts within the agent watchdog window. No URI-AUDIENCE-CYCLE-2-MEMORY-STALL events fired.

---

## Phase 6 persistence gate evaluation

Per `.claude/commands/and-facets.md` § Phase 6 6a, the four gates:

1. **Phase 5 = 0 HARD** — NOT MET. 2 HARDs ACCEPTED-AT-CAP-BURN (fault-030, fault-031); 1 HARD carry-as-adjudicated (fault-021). Gate is bypassed via cap-burn disposition per URI-FACETS-CAP-BURN-SEMANTICS A2.
2. **Phase 5b = ACCEPT (3-of-3 per facet)** — PARTIAL. 8 facets met under strict 3-of-3; 3 facets met via arbiter override (deferred-with-attribution); 1 facet met via cap-burn DELETE. Gate is bypassed via documented resolution paths.
3. **Dialogue-coverage gate (URI-DIALOGUE-COVERAGE-GATE)** — NOT MET. Coll's speech bone @8 has zero dialogue citations post-DELETE; the speaker file body is empty. Both faults ACCEPTED-AT-CAP-BURN per A2.
4. **Scene-map coverage gate (URI-SCENE-WINDOW)** — MET. No changes from cycle-2; scene-map remains validated.

**Phase 6 disposition: persist with NOT-SUCCESSFUL orchestrator-critic verdict per cap-burn semantics step 5.** Status flip `audited-r1-mechanical` → `audited-r1` per step 6 (cap-burn DELETE treated as a resolution path; status reflects audience-gate resolved-even-if-NOT-SUCCESSFULly). `audience_gate_cap_burned: true` is the audit trail.

---

## Output to disk (cycle 3)

- Per-reviewer verdict files (cycle 3, written this dispatch):
  - `active-project/staff/audience/cape-fic-reader/interest-narrator-r3-verdict.md`
  - `active-project/staff/audience/dark-fantasy-reader/interest-narrator-r3-verdict.md`
  - `active-project/staff/audience/worm-canon-pedant/interest-narrator-r3-verdict.md`
  - `active-project/staff/audience/cape-fic-reader/vibes-r3-verdict.md`
  - `active-project/staff/audience/dark-fantasy-reader/vibes-r3-verdict.md`
  - `active-project/staff/audience/worm-canon-pedant/vibes-r3-verdict.md`
- Consolidated report: this file (`active-project/staff/auditor/facets-audience-gate-r3.md`).
- Cap-burn report: `active-project/staff/auditor/facets-cap-burn-b01c01-20260524T021822Z.md`.
- Phase 5 cycle-3 audit: `active-project/staff/auditor/facets-final-audit-cycle3.md`.
- Showrunner-memory status: `audited-r1-mechanical` → `audited-r1`; `audience_gate_cycle: 3`; `audience_gate_complete: true`; `audience_gate_cap_burned: true`; `cap_burn_deletions: [coll-net-mender-flea-bottom:1 @8]`; `audience_gate_facets_passed` extends to include interest-narrator + vibes.

Phase 6 persistence proceeds with orchestrator-critic NOT-SUCCESSFUL verdict per cap-burn semantics. NOT-SUCCESSFUL is recorded but is NOT a HARD-BLOCK against `/and-stitch`.
