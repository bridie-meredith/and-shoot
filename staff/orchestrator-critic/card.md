---
name: orchestrator-critic
class: critic
subclass: run-judge
scope: library
persona-purpose: [orchestrator-critic]
quality: full
origin: authored — 2026-05-10, post R1+R2 tuning of /and-season; user direction "establish an orchestrator-level critic card meant to judge performance by results and run time. it will be the standard to satisfy for and-season to be considered a success"
note: outside the cards/ taxonomy. The cards/ schema authority (schemas/card.schema.md) defines five story-facing classes (persona, location, prop, condition, behavior). This card is staff-facing, not story-facing — it judges the production of fiction, not anything inside the fiction. Lives under staff/, mirrors to active-project/orchestrator-critic/ when a project is activated, but is not subject to the cards/ schema's class-list rule.
---

# Orchestrator Critic — Run Judge

The orchestrator-critic judges a `/and-season` run against a fixed standard of **results and runtime**. It is the boss-level review: a run is "successful" if and only if this card returns PASS or PASS-WITH-NOTES.

The audience persona cards judge whether the bones are good. The auditor judges whether the bones are mechanically sound. The orchestrator-critic judges whether the *orchestration* did its job — converged on time, converged honestly, produced what a production needs to ship.

---

## Purpose

This card answers one question: **was the run a success?**

Not "are the bones good" (audience), not "is the file schema-compliant" (auditor), not "is the plan dramatically shaped" (dramatist). Those are inputs. This card weighs them against the budget the run had and the standard the project is held to.

Use this card:
- At end of `/and-season` Phase 5, after the per-episode files are written and showrunner memory is persisted.
- At end of `/and-season-plan` (when implemented).
- At end of `/and-protolines-v2` (per-episode orchestration analog).
- Whenever the user asks "did the run succeed?"

---

## Invocation protocol

**Who runs the card:** the orchestrating command body (main session). No subagent dispatch is required. The card is a spec, not a roleplay; the orchestrator reads its actual run state and produces a verdict against the card.

**Inputs to the verdict:**
1. The full audit-report set under `active-project/staff/auditor/season-<slug>-pass-*.md`.
2. The Phase 4 split-proposal + split-review files.
3. Showrunner memory (`active-project/staff/showrunner/memory.md`) — for iteration counts, dispatch counts, status flags, carry-back queue entries.
4. The audience seam files (if a tuning round produced them) — for adversarial-pass results.
5. The per-episode proto-line files post-split.
6. The aggregate file post-Phase-3.
7. The session itself — wall-clock and dispatch counts since `/and-season` started.

**Output:** a run report at `active-project/staff/auditor/season-<slug>-orchestrator-verdict.md`. The report follows the template in §"Run report template" below.

**Verdict line:** the report's last line is one of:
- `VERDICT: PASS`
- `VERDICT: PASS-WITH-NOTES — <one-clause notes summary>`
- `VERDICT: FAIL — <one-clause failure summary>`

The verdict line is also written into `seasons[<slug>].orchestrator_verdict` in showrunner memory.

---

## Success criteria

A run achieves PASS when **all three categories** below return clean. Any single failure across categories drops the run to PASS-WITH-NOTES (recoverable) or FAIL (disqualifying — see §"Failure modes").

### Category A — Convergence

A1. **Phase 2 (aggregate authoring) converged in ≤3 full-pipeline iterations.** If iterations hit 3 without convergence, the run aborted to user; that is FAIL on Category A.

A2. **Phase 3 (season-scope review) converged in ≤3 full-iteration sweeps** with all passes returning clean verdicts in a single end-to-end run. The relevant passes (V2 LIVE post-2026-05-10):

- S1 constraint: `PASS`
- S2 shape: `CLEAN` (no `STRUCTURAL-FAILURE`; `LATE-WEIGHT` flag at most allowed if licensed-by-condition-card)
- S3 trim ×3: `ACCEPT` from ≥2 of 3 personas
- S3.5 ruleset: `RULESET-CLEAN`
- S4 continuity: `SEASON-CONTINUITY-OK`
- S4.5 post-split continuity (after Phase 4): `POST-SPLIT-CONTINUITY-OK`
- S5 voice: `VOICE-COHERENT`
- S6 vibe ×3: `VIBE-ALIGNED` from ≥2 of 3 personas, OR `VIBE-DRIFT-{reason}` only when the season-plan acknowledges the pattern explicitly per URI-015 carry-forward rule
- S7 facet-readiness: `FACET-READY`
- S8 plausibility: `PLAUSIBLE` at file level (split-verdicts permitted only with explicit licensing-card citation per URI-016)
- S9 comprehensibility ×3: `COMPREHENSIBLE` from ≥2 of 3 personas

A3. **Phase 4 split converged in ≤3 split iterations** with ≥2-of-3-persona `SPLIT-ACCEPT`.

A4. **Episode count is multiple of 3** (3, 6, 9, 12...).

### Category B — Quality

B1. **All Phase 4 Step 2 mechanic-bearing verdicts pass:**
- No `OPEN-ENGAGES-FAIL` flags.
- No `CLOSE-EARNS-NEXT-AFTERMATH-DRIFT-{N}` flags with N>20.
- No `SHAPE-COHERENT-FLATLINE-{line-range}` flags.
- No `SHAPE-COHERENT-FLAT-AFTERMATH-{episode}` HARD flags. SIGNAL flags permitted with rationale.

B2. **Auditor 11-class scan: 0 HARD findings open at end-of-run.**
A HARD finding is "open" unless one of:
- It was resolved during the run by user verdict and the resolution is recorded in showrunner memory.
- It was routed to a Phase H carry-back queue entry AND the queue entry has a `USER-VERDICT-RECEIVED` status OR the auditor-self-review confirmed it is not a current-corpus blocker.
- It was a predictable post-execution fault routed to a downstream subtask with explicit verification step.

B3. **All forward-flag commitments from `season-<slug>-plan.md` are visible in the bones.**
Each `season-plan.md` content beat has a corresponding stretch in the aggregate where its named state-changes appear. Forward-flag breaches are FAIL conditions (see §"Failure modes").

B4. **Adversarial pass results, if a tuning round was run:**
- ≥80% of audience attack units return ACCEPT or ACCEPT-WITH-CAVEAT after the final showrunner re-pass.
- 0 R1-style ACCEPTs flip to STRONG/REJECT under R2-style tightened-brief re-attack (if a tightened-audience round ran). If they do, the run is PASS-WITH-NOTES — the rubric's threshold language is leaning on formulaic deference and a future round should re-tune.
- ≥1 STRONG defense survives — if zero STRONG defenses survive (every STRONG seam was conceded to REVISE), the rubric is too soft; PASS-WITH-NOTES with explicit "rubric-too-soft" note.

B5. **Schema compliance.**
- Every per-episode file has the seven required header fields in order.
- `aggregate_range` fields are non-overlapping and (via legal ID-deletion gaps) cover 1..N.
- `narrator:` field per URI-009 plan-designated rule.
- Body comment-clean per the proto-line schema.

### Category C — Routing

C1. **All HARD-finding routings are explicit.**
Every HARD finding from the auditor has a named owner: fixer / screen-writer / dramatist / showrunner-self / human escalation / V2 carry-back. No HARD findings sit in "we'll figure it out" status at end-of-run.

C2. **All boundary-rebalance subtasks have specific cut-point candidates.**
If Phase 4 surfaced over-band episodes that route to dramatist boundary-rebalance, the rebalance routing must include candidate cut-points to evaluate, not just "dramatist resolves." A cut-point must be a specific aggregate ID, not a range.

C3. **Carry-back queue is honest.**
- Every queued URI item names its category, source, and cost estimate.
- DEFEND-with-carry-back classifications are valid only when V1 has no mechanic — if V1 has a partial mechanic, the classification is wrong (per R2 SLEEPER-3 lesson). The verdict-producer cross-checks: for each DEFEND-with-carry-back, the cited "no V1 mechanic" claim is examined against the actual V1 rubric language.

C4. **Showrunner memory is current.**
- `seasons[<slug>].protolines_complete` flag set with timestamp.
- `seasons[<slug>].episodes[]` populated for every produced episode.
- `seasons[<slug>].orchestrator_verdict` field receives this run's verdict.
- `tuning_<slug>_status` field present if any tuning round ran during this orchestration.

---

## Runtime budgets

### Hard caps (FAIL if exceeded)

R1. **Total dispatch ceiling: 60 dispatches per /and-season run.**
Phase 2 ≤15 (5 sub-passes × 3 max iterations), Phase 3 ≤30 (10 passes × 3 max iterations), Phase 4 ≤9 (split + 3-persona review × 3 max iterations), Phase 5 ≤2 (memory + verdict). Cushion: 4. Exceeding 60 indicates the run is thrashing and should escalate to user instead of continuing.

R2. **Iteration cap: ≤3 per phase, hard.**
Phase 2 ≤3 full-pipeline iterations; Phase 3 ≤3 full-iteration sweeps; Phase 4 ≤3 split iterations. The existing /and-season language already encodes this; the orchestrator-critic enforces it as a budget condition.

R3. **No single pass iterates 3+ times without forward progress.**
"Forward progress" = the verdict moved (FAIL → PASS, REVISE → ACCEPT, or the finding count strictly decreased). Three iterations on the same FAIL with no diff in finding category indicates rubric-vs-corpus mismatch; the run aborts with explicit mismatch routing to rubric carry-back.

### Soft thresholds (PASS-WITH-NOTES if exceeded)

S1. **Soft dispatch budget: 30 dispatches.**
30 is the typical successful-run ceiling. 30–60 is permitted but generates a "high-dispatch" note in the verdict.

S2. **Wall-clock soft budget: 8 hours of orchestration time.**
Beyond 8 hours, the run gets a "long-run" note. This is advisory only; no hard wall-clock enforcement.

S3. **Audit re-run count.**
If any audit pass needed an `r3` or later iteration (e.g., `season-s01-pass-S3-trim-pulp-enthusiast-r4.md`), the run gets a "deep-iteration" note naming which pass and how many rounds.

---

## Failure modes (disqualifying — VERDICT: FAIL)

F1. **Non-convergence:** Phase 2, Phase 3, or Phase 4 hit their iteration cap without clean verdict. Required to escalate to user.

F2. **Forward-flag breach:** a season-plan-named beat (per §D content beats) has no corresponding stretch in the bones. The plan's commitments are not negotiable at orchestrator scope; failure to deliver is structural.

F3. **Hard-rule violation that is not resolved at end-of-run:**
- Episode count not multiple of 3.
- POV-coherent stretch bisected (no cut may bisect; if Phase 4 produced one, FAIL).
- A slug fails to resolve to a canonical card.
- A condition card or series law violated without explicit licensing.

F4. **HARD-finding open at end-of-run with no routing:**
A HARD finding from the auditor that has no owner, no carry-back queue entry, and no user-verdict resolution. This is not "we ran out of time"; it's "we don't know what to do with this finding." Required to escalate to user.

F5. **Cap-thrash without rubric carry-back routing:**
A pass iterates 3 times with no forward progress AND the rubric mismatch is not routed to a carry-back URI. Indicates the orchestration silently accepted a stuck state.

F6. **Convergence claimed but residuals masked:**
Any state where showrunner memory reports `protolines_complete` AND there are unrouted HARD findings, unresolved REJECT verdicts, or unacknowledged carry-forwards. The orchestration cannot lie that it converged.

---

## Verdict format

The card produces one of three verdicts:

### PASS
- All three categories return clean.
- All hard caps respected.
- All soft thresholds within bounds OR exceeded with explicit rationale.

### PASS-WITH-NOTES
- All three categories return clean.
- One or more soft thresholds exceeded, OR ≥1 carry-back queue entry produced, OR ≥1 audit pass required deep iteration (r3+), OR R2-tightened-brief surfaced SLEEPERs that the next round should address.
- The notes are factual: "high-dispatch" / "long-run" / "deep-iteration on Sn pass" / "rubric-too-soft" / "n SLEEPERs surfaced for next-round re-tune".

### FAIL
- Any failure mode (F1–F6) triggered.
- Required action: escalate to user with the failure-mode citation and the specific finding(s) that triggered it.

The verdict line is canonical. Do not fabricate "PASS" when the criteria are not met.

---

## Run report template

The orchestrator-critic verdict file at `active-project/staff/auditor/season-<slug>-orchestrator-verdict.md` follows this structure:

```
---
report: orchestrator-verdict
season: <slug>
date: <date>
card: staff/orchestrator-critic/card.md
inputs: <list of audit reports + memory file + session metrics>
---

# Orchestrator Verdict — Season <slug>

## Convergence (Category A)

- A1 Phase 2 iterations: <n of 3 max> — <PASS/FAIL>
- A2 Phase 3 passes:
  - S1 constraint: <verdict>
  - S2 shape: <verdict>
  - S3 trim ×3: <per-persona verdicts>
  - S3.5 ruleset: <verdict>
  - S4 continuity: <verdict>
  - S4.5 post-split: <verdict | skipped>
  - S5 voice: <verdict>
  - S6 vibe ×3: <per-persona verdicts; carry-forward citations if any>
  - S7 facet-readiness: <verdict>
  - S8 plausibility: <verdict; split-verdict citations if any>
  - S9 comprehensibility ×3: <per-persona verdicts>
- A3 Phase 4 split iterations: <n of 3 max>
- A4 Episode count: <count> — <multiple of 3? PASS/FAIL>

## Quality (Category B)

- B1 Phase 4 Step 2 mechanic verdicts: <list any FAIL/AFTERMATH-DRIFT/FLATLINE/FLAT-AFTERMATH flags or "all pass">
- B2 Open HARD findings: <count + per-finding routing or "0 open">
- B3 Forward-flag honor: <each season-plan beat → aggregate stretch IDs covering it; or "BREACH: <beat>">
- B4 Adversarial-pass results: <"no tuning round" | "X of N units accept; M SLEEPERs surfaced; rubric soundness assessment">
- B5 Schema compliance: <PASS/FAIL with itemized issues>

## Routing (Category C)

- C1 HARD-finding routings: <every HARD finding has owner; or "n unrouted">
- C2 Boundary-rebalance specifics: <each rebalance has candidate cut-point IDs; or "n vague">
- C3 Carry-back queue: <count + cross-check on any DEFEND-with-carry-back classifications>
- C4 Showrunner memory current: <PASS/FAIL with field-by-field check>

## Runtime

- R1 Total dispatches: <count> — <within 60 hard cap? PASS/FAIL>
- R2 Iteration caps: <Phase 2 / Phase 3 / Phase 4 iteration counts; PASS if all ≤3>
- R3 Forward progress per pass: <PASS or "stuck on Sn pass with no diff">
- S1 Soft dispatch budget: <count vs 30>
- S2 Wall-clock: <approximate hours>
- S3 Audit re-run depth: <list r3+ passes>

## Notes (PASS-WITH-NOTES details, if any)

- <each note: factual one-line entry>

## Failure summary (FAIL details, if any)

- <which F1–F6 triggered + specific evidence>

---

VERDICT: <PASS | PASS-WITH-NOTES — <notes summary> | FAIL — <failure summary>>
```

The verdict-producer (main session of `/and-season`) writes this report at end of Phase 5. The verdict line goes to `seasons[<slug>].orchestrator_verdict` in showrunner memory.

---

## Honesty discipline

This card has the same honesty discipline as the audience Threshold Discipline section:

- **Verdict arithmetic is authoritative; orchestration narrative is not.** A run's commit messages or status notes saying "converged" do not establish convergence; the cited audit verdicts do.
- **PASS-WITH-NOTES is not a fallback for "I want this to PASS."** Each note must be factual and specific. "Long-run" with no hour count, "high-dispatch" with no count, "rubric-too-soft" with no STRONG-defense audit — these are hand-waves and should disqualify.
- **FAIL is not a punishment.** It is information. A FAIL verdict tells the user the run did not satisfy the standard; the user decides whether to fix the run, accept the failure-mode and update the standard (Phase H carry-back), or escalate to a different operating mode.
- **Cross-check DEFEND-with-carry-back classifications.** Per R2 SLEEPER-3 lesson: a run that classifies a real seam as "V1 has no mechanic" when V1 partial mechanics exist is not honestly converged. The orchestrator-critic verifies this before granting PASS.

---

## Versioning

- v1 — 2026-05-10: initial card; calibrated against R1+R2 of /and-season s01. Hard cap 60 dispatches; soft 30; iteration cap 3; failure modes F1–F6 named.
- Future revisions: when a `/and-season` run produces verdict-discipline data (e.g., a PASS that should have been FAIL, or a FAIL that should have been PASS-WITH-NOTES), a meta-tuning round on this card itself can adjust thresholds. Calibration is empirical — the card does not pretend its thresholds are platonic.
