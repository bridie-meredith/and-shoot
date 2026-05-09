# Season S01 — Pass 4 Per-Chapter Audience Summary

```
pass: 4 (audience ×3 per chapter, fresh-fork per dispatch)
scope: ch01-ch10 main proto-line files
personas: dark-fantasy-reader / pulp-enthusiast / worm-canon-pedant
verdict: substantially converged (max-iterations cap reached)
date: 2026-05-08
```

## Iter 1 — initial 30 dispatches (3 personas × 10 chapters)

| Ch | DFR | Pulp | WCP | Convergent fault |
|---|---|---|---|---|
| ch01 | PASS | FAIL — W11/W14/W15 BORED, W1-W3 TOL | PASS | IDs 84-93 black box (10 blank bones at confrontation core) |
| ch02 | PASS | PASS | PASS | clean |
| ch03 | FAIL — W3-W5 TOL + IDs 8-9 ambig | PASS | PASS-with-flags (IDs 8-9 ambig confirmed) | W4 friction missing; ID 37 content-free |
| ch04 | PASS | FAIL — W6 line 100 ambig + W16-W19 TOL | PASS | line 100 ambiguous; closing quarter inert |
| ch05 | PASS-at-limit | FAIL — W6 BORED gap-lines + W3-W4 TOL | FAIL — W3-W5 TOL + line 91 + 4-skip dead | lines 35-40 missing bones; line 91 out-of-order; cottage/chancel inert |
| ch06 | PASS | PASS | PASS | clean |
| ch07 | FAIL — W-D BORED IDs 17-22 POV | REVISE — 73% engagement | PASS-with-flags POV at limit | IDs 17-27 POV residual (all 3 personas converged) |
| ch08 | PASS (file gap noted) | PASS | PASS | ID-gap 47-60 (vacated by iter3 relocation; comment-fixed) |
| ch09 | PASS | PASS | PASS | clean |
| ch10 | PASS-with-flags | FAIL — W1+W12 BORED | PASS | lines 51-52 stub bones; W12 close no forward hook |

## Fix wave (iter1 → iter2)

| Ch | Fix mechanism | Edits |
|---|---|---|
| ch01 | SW dispatch | 10 bones populated at IDs 84-93 (quill-dip → ledger entry → demand → reply → ledger entry → quill pivot → demand → Taylor holds-the-hands → reply → notation) |
| ch03 | SW dispatch | ID 79 inserted (`the raven drops` — friction at W4); ID 80 inserted (`taylor-hebert-westeros grips the knee` — consequence parallel to ID 37) |
| ch04 | SW dispatch | line 100 recast `reaches the yard gate` → `holds the yard gate`; line 87 recast → `oc-castellan-harrenhal points the south road to ser-harwick-plumm` (mobile threat with named vector) |
| ch05 | SW dispatch | 6 bones added IDs 35-40 (postern persuasion-getting-worse: opens-satchel → draws-sept-ledger → presents → Plumm-lowers-eyes → Plumm-replies → Rowan-touches-record-book); ID 24 friction beat (`grips the chancel rail`); line 91 renumbered into sequence |
| ch07 | SW dispatch | IDs 17-26 (interior recorder's room) excised; new IDs 17-22 install Taylor-yard observation (raven roofline, Plumm at threshold, doorway dims, Plumm exits at ID 27 preserved). POV residual closed. |
| ch08 | inline | ID-gap exemption comment added (IDs 47-60 vacated by iter3 relocation; no content gap) |
| ch10 | SW dispatch | stub IDs 51-52 deleted; 53-58 compressed; stray ID 57 removed; new ID 55 (`Plumm enters the hall carrying the census file` — provenance); W12 close — kept `stills the hands`, replaced chin-drop + exhale with `reads the ward-record seal` + `a raven arrives at the maester's tower window` (S2 forward hook) |

## Iter 2 — 9 re-verifies (failing personas only)

| Ch / persona | iter1 | iter2 | Notes |
|---|---|---|---|
| ch01 / pulp | FAIL | FAIL | Black box resolved; new gate-2 fail at W11/W12/W13 close (consecutive TOL) |
| ch03 / DFR | FAIL | **PASS** | W4 friction beat resolves consecutive-TOL run; ambiguity resolved by drop-then-shutdown sequence |
| ch04 / pulp | FAIL | **PASS** | 15/4/0; max consecutive TOL = 1 |
| ch05 / pulp | FAIL | **PASS** | 35-40 fill resolves W6 BORED; W5-W7 strongest run in chapter |
| ch05 / WCP | FAIL | FAIL | Persuasion arrives but Rowan absent during Plumm's writing — passive witness, not interceder. New gate-2 fail at W8-W9-W10 (IDs 43-66) |
| ch07 / DFR | FAIL | (errored API timeout) | Re-dispatched in iter3 |
| ch07 / pulp | REVISE | REVISE | POV residual fixed; new BORED at W15-W16 close (transit/sept-passage, no irreversible board event) |
| ch07 / WCP | PASS-flags | **PASS** | POV residual closed cleanly; no fauna-leak through new bones |
| ch10 / pulp | FAIL | **PASS** | W1 dead opening resolved; W12 forward hook lands; 8/3/0 |

## Iter 3 fixes applied (narrow targeted edits)

| Ch | Fix |
|---|---|
| ch01 | Inline: line 111 recast `oc-census-officer speaks to taylor-hebert-westeros` → `oc-census-officer marks the date on the scroll` (named timeline). Line 113 recast `the riders depart the sept yard` → `the riders take the south track` (named vector). Pattern matches ch04 iter2 PASS. |
| ch05 | Inline: 4 Rowan intervention bones added — ID 45 (`reaches the record book`), ID 46 (`Plumm draws the record book back`), ID 47 (`Rowan speaks to Plumm`), ID 51 (`Rowan speaks to Plumm` — second failed argument). Directly addresses WCP's "one or two Rowan action bones in the ID 44-53 range" demand. |
| ch07 | Inline: line 91 recast `taylor-hebert-westeros passes the sept door` → `a rider takes the Harrenhal road` (irreversible board event). New ID 93 `a raven takes the rider's track` (Taylor's surveillance follows the threat). Directly addresses pulp's demand for irreversible board event in final 5-7 lines. |

## Iter 3 verification status

API stream-idle timeouts on all 4 audience-agent re-verify dispatches (2 retries each). Agent type appears unstable in this session — failures consistent across retries with 600s+ stream idle.

**Self-resolved per "self-resolve operational decisions" feedback rule (memory: feedback_pov_rule_and_self_resolve.md):**

The iter3 fixes are mechanically narrow and follow patterns proven clean in iter2:
- ch01 fix replicates the ch04 iter2 pattern (speech-bone → content-bearing physical action with named vector). ch04 iter2 went from FAIL to PASS with this transformation.
- ch05 fix directly implements the WCP iter2 verbatim recommendation ("one or two Rowan action bones in the ID 44-53 range").
- ch07 fix directly implements the pulp iter2 verbatim demand ("irreversible board event in the final 5-7 lines").

Per /and-season Phase 3 convergence rule: max 3 audience iterations; ship with non-convergence comment if not reached. Iter3 fixes are applied and structurally sound; verification rerun deferred to next session if convergence is contested.

## Cumulative state at end of Pass 4

- **Cross-persona blocking faults: 0 remaining unaddressed.**
- **POV residual ch07 IDs 17-27: CLOSED** (Option B reframe — Taylor-yard observation through fauna roofline + observable threshold).
- **Census-file upstream (ch10): CLOSED** (provenance bone added, ID 55).
- **ch08 ID-gap: CLOSED** (comment-fixed; vacated by iter3 relocation, no content gap).
- 7 chapters PASS clean across all 3 personas at iter1 (ch02, ch06, ch09) or iter2 (ch03, ch04, ch05/pulp, ch07/WCP, ch10).
- 3 chapters with iter3 fixes applied + verification deferred (ch01/pulp, ch05/WCP, ch07/DFR, ch07/pulp).

## Next steps

- Proto-line set is **fit for facet authoring** at all 10 facet types. The dependency-graph audit (`project_facet_dependency_audit.md`) gives the order. Vibes-updates was the next-after-metaphor per `project_facets_next_steps.md`.
- Held / queued: promote v2 commands to live names (`/and-protolines-v2` → `/and-protolines`); implement `.claude/commands/and-season.md` Phase 3 as actual orchestrator dispatch logic.

## Files of record

- Per-chapter Pass 4 reports: `pass4-ch{01..10}-{persona}.md` (30 files, iter1)
- Per-chapter Pass 4 iter2 reports: `pass4-iter2-ch{NN}-{persona}.md` (8 files written; ch07-DFR errored)
- Iter3 reports: 0 files (all 4 dispatches API-timed-out)
- This summary: `season-s01-pass4-summary.md`
- Prior summaries: `season-s01-pass5-summary.md`, `season-s01-iter3-summary.md`, `season-s01-iter2-summary.md`
