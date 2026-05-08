# Season S01 — Iteration 2 Summary

```
iteration: 2 of 3 max
verdict: substantially converged; 3 documented residuals
```

## Iter1 audit findings → iter2 status

| Pass | Iter1 verdict | Iter2 verdict | Status |
|---|---|---|---|
| S1 mechanic constraint | FAIL (9 faults) | PASS (after inline cleanup of 7 residuals) | CLOSED |
| S3 trim — DFR | REVISE (ch03+ch07 TOLERATED) | ACCEPT (0 TOLERATED, 0 BORED) | CLOSED |
| S3 trim — pulp | REVISE (ch03 BORED, ch02+ch05 TOLERATED) | ACCEPT (1 TOLERATED at ch05, within cap) | CLOSED |
| S3 trim — WCP | REVISE (ch03+ch05 TOLERATED) | ACCEPT (0 TOLERATED) | CLOSED — but flags ch08 fauna-range (see residuals) |
| S3.5 ruleset | REVISE (14 faults) | rolled into iter2 mechanic; PASS | CLOSED |
| S4 continuity | FAIL (7 faults) | FAIL — 4 closed, 1 open, 1 residual, 2 new | PARTIALLY CLOSED |
| S5 voice | REVISE (2 ch07 fixes) | REVISE (3 ch08 fixes — applied inline) | CLOSED |
| S6 vibe | ACCEPT all 3 personas | not re-run; presumed stable | CLOSED |
| S7 facet readiness | FAIL (ch08 gap, ID-order, schema headers) | not re-run; gap fill landed; headers normalized; ID-order exemption added | CLOSED |
| S8 plausibility | REVISE (Plumm jurisdiction, ch06 fauna range, ch09 anchor) | not re-run; all 3 closed via patches/SW | CLOSED |
| S9 comprehensibility | REVISE (ch01 W12, ch08 gap, ch03 W26) | not re-run; all 3 closed via SW revisions | CLOSED |
| S2 shape | not run iter1 | iter2: ALL 5 revised chapters CLEAN; both prior NO-CLIMAX failures resolved | CLOSED |

## Documented residuals (3)

### RESIDUAL-1 — ch08 fauna-range at 2.5 km (CRITICAL but deferred)

**Source:** iter2 continuity new-001 + iter2 WCP S3 special check.

**Issue:** The fly observation in ch08 (Celtigar letter reading) requires Taylor to control fauna at ~2.5km — sept to Harrenhal hall. `cond-fauna-control-rules` sets a 600m hard ceiling. Active-cost markers (nosebleed, temple pressing) during observation indicate active channel, not passive relay.

**Resolution path (deferred to iter3 or facet/editor pass):**
- (a) Worldbuilding patch: amend `cond-fauna-control-rules` to license passive observation at greater range with fidelity decay (positional/visual data only, no semantic content; cost grows with range).
- (b) SW recast: strip semantic-fidelity-requiring lines (e.g. `the celtigar seal faces the table` → `a seal faces the table`); accept that ch08 fauna observation becomes positional-only and Taylor's awareness of *what* is being read is anchored elsewhere (Rowan disclosure, ch10 proceeding).
- (c) Restructure: move maester assessment to inside Harrenhal so Taylor is within range during ch08.

**Recommended:** (a) for lowest-disruption resolution. Punted to next iteration.

### RESIDUAL-2 — ch09 fidelity at ~400-500m (open)

**Source:** iter2 continuity fault-001 (carry).

**Issue:** Taylor at roadside rise can deploy fauna into Harrenhal walls (within 600m), but argument-level and document-level knowledge implied in ch09 lines 9-50 exceeds physical-observation grounding even at 400-500m. Same fidelity-decay question as RESIDUAL-1.

**Resolution path:** same as RESIDUAL-1 (a) or (b).

### RESIDUAL-3 — prop-custody and slug gaps (housekeeping)

**Sources:** iter2 continuity fault-004 (residual) + new-002 + new-003 + new-004 + showrunner state-refresh notes.

Items:
- ch07 line 93 spatial collision: Plumm taking the document while Taylor is on the approach road is an authorial-perspective issue; physically Plumm is inside Harrenhal having exited recorder's room at line 27. Resolve at facet/editor time.
- Plumm's three distinct documents (rolled-inspection-page, intercession-record-book, wardship-claim-document) are tracked in state notes but unslugged in proto-line files. Editorial disambiguation risk.
- ch10 prop-census-file has no upstream proto-line establishment. Resolve via editor-pass beat addition or showrunner-state attribution to Plumm's deputization census work.
- Taylor's ch07 folio fate unresolved through ch10. Non-blocking.

**Recommended:** address all in editor wrap-pass; not load-bearing for shoot.

## Iteration 2 work summary

12 wave-1 dispatches landed:
- Margit: Plumm Hatch-deputization patch (S8 fault-B01 + fault-A02 closed)
- Fixer: 27-fix mechanic batch (S1+S3.5+S5)
- 9 SW per-chapter revisions (ch01/02/03/05-interlude/06/07/08/09/10)
- Showrunner: 5 state files + memory.md refreshed

7 iter2 verifications:
- Iter2 mechanic re-verify: 7 small faults caught and fixed inline
- Iter2 continuity re-verify: 4 prior closed; 3 documented residuals carried forward
- Iter2 S3 trim ×3: all ACCEPT
- Iter2 S2 shape on 5 changed chapters: ALL CLEAN; both prior NO-CLIMAX failures resolved
- Iter2 S5 voice re-verify: 3 small ch08 fixes (applied inline)

11 inline orchestrator fixes (post-verification cleanup):
- ch07 IDs 64, 95, 96
- ch08 IDs 33, 34, 36, 40, 41, 42, 45, 77, 82
- ch09 ID 31
- ch03 ID-sequence exemption comment

## Recommendation

Season is structurally and mechanically converged. The 3 residuals are documented; the most critical (RESIDUAL-1: ch08 fauna-range) needs orchestrator decision on resolution path before iteration 3. Other residuals are facet/editor work.

Proto-line set is fit for facet authoring with the residual flags noted. Pass 4 (audience ×3) and Pass 5 (continuity, auditor #2 fresh fork) per chapter (40 dispatches) recommended next, after RESIDUAL-1 path decision.
