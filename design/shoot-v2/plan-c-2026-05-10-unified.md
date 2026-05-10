---
plan: C
date: 2026-05-10
status: PROPOSED
supersedes:
  - design/shoot-v2/plan-and-season-followon-2026-05-10.md (Plan A)
  - design/shoot-v2/plan-and-facets-r2-2026-05-10.md (Plan B)
predecessor-state: parallel two-session execution ran 2026-05-10; mixed results; coordination overhead > parallelism win.
---

# Plan C — `/and-season` bone-gate follow-on + `/and-facets` R2 tuning (unified single-session)

## Why this plan replaces Plan A + Plan B

Plan A and Plan B were authored as parallel remote sessions with explicit concurrency contracts (sentinel files, branch SHAs, file-disjoint write zones). The 2026-05-10 run executed most of the gate machinery cleanly, but the coordination contracts produced:

- A post-merge reconciliation commit (`1b6dda0` — B3 emission re-aligned to A2 schema after merge).
- Schema-definition drift between `A-corpus.md` and `audit-report.schema.md` (logged as URI-027) traceable to two sessions independently asserting frozen contracts.
- A3's single-fork dispatch on Step 1.5 (disclosed budget-driven deviation) — fork-budget bookkeeping that the unified-session would have caught at planning.
- A4 / A5 / B4 deferred because A3 failed F7-bone, and the two plans had no shared "what's the next move after gate-fires" branch.

The serialization both plans actually require (A2 → B3 → B4 → A1 → A3 → A4 → A5) is linear. Parallelizing it added contracts without adding parallelism. Plan C runs the same actions in one session, drops every cross-session coordination contract, and adds explicit branch points for the gate-fire cases the parallel plans elided.

## Carry forward — preserve, don't redo

### Landed cleanly (do not touch)

- **A1** — persona-card `## Tens-attack vocabulary` body sections + Pass S4.5 brief reduction. (PR #8 / commit `50a8f6d`.) Brief-reduction pattern carries to C4.
- **A2** — F-R2-* → F7 emission contract: `f-r2-counts` frontmatter clause in `schemas/audit-report.schema.md`; F7 amendment in `staff/orchestrator-critic/card.md`. (PR #6 / commit `58af716`, supplemented by `bdb676d`.) Schema is the upstream contract for C1.
- **B3** — `/and-facets-r2.md` §Form re-test per-layer (cold-read), decision-shard emission, mid-layer cite-index rebuild flipped mandatory, Phase 5.5 arbiter glue (T1 + T4 only). Post-merge reconcile (`1b6dda0`) aligned B3 emission format to A2 schema. **URI-023 #9 already landed here.**
- **B2a** — audience entry-quality review + **G5 position-gate added to `B-locked-rubric.md`** (`aa183a4`). Rubric refinement is permanent.
- **B5 partial** — PLAN.md / queue hygiene partial; cross-session sentinel obsoleted by Plan C.
- **A5 partial** — URI-026 Phase 1.5 marked LANDED in queue (`cddfc13`).

### Pre-staged drafts to reuse

- `8c64bd9` — A4 spec edits draft (`.claude/commands/and-season.md` new passes for sensory + state-updates env + loc-state).
- `e94837a` — A4 portability audit (`plan-a-a4-rubric-portability-audit.md`).
- `8a198e8` — A4 staging: auditor class library coverage question resolved.

### Validated discoveries

- **A3 mechanism validation** — the bone-gate caught s02e01 inert stretch (31 contiguous rung-1 bones at 122–162) + s02e02 undercharged gathering scenes (358–396, 461–489) with per-episode actionable kickback. Pre-bone-gate review surfaces (S3/S4 audience) would not have produced the same precision. **URI-026 is doing exactly what it was designed to do.** The FAIL is a positive signal: the gate held the s02 corpus out of downstream facet contamination.
- **B-locked-rubric.md G5 position-gate** (from B2a) is a permanent improvement; reuse in C1.

### Process lessons (encoded into Plan C structure)

1. Parallelism across remote sessions costs more than it saves when the work is linear. Plan C runs single-session.
2. A3's single-fork dispatch on Step 1.5 was a disclosed budget deviation. **C3 must use per-spec parallel-fork** for round-trip verification of the gate.
3. Phase 2 iter-2 was not formally re-audited and Phase 3 was skipped in the A3 run (disclosed). **C3 either runs both or explicitly re-discloses.**
4. URI-025 supersession by URI-026 is settled; URI-027 (F-R2-* class drift) logged from reconciliation. Both leave as-is; URI-027 is decided "option 1 — patch schema to match A-corpus.md."

## Outcome

- Plan B project closed: `.r2-decisions.md` produced natively, F-R2-* counts available for F7 consumption.
- s02 corpus passes the bone-gate (round-trip verification of URI-026 mechanism on a fresh corpus, with the s02e01 / s02e02 regen as the kickback signal).
- Phase 2 migrations land: sensory + state-updates env + loc-state hard-gated at `/and-season`, mirroring tens.
- `/and-facets-r1` Layer 1 (and Layers 1b / 2b / 3a per A4 spec staging) deleted; `/and-shoot` Phase 0 rename contract extended.
- URI-023, URI-026, URI-027 closed; URI-025 IP-3 (per-episode flag-driven facet pass) re-opens for Phase 3 if desired.

## Action sequence (linear)

| # | Name | Owns | Reads | Gate |
|---|---|---|---|---|
| C1 | B4 validation re-run | `active-project/theater/facets/*` (s01e01), `r2-judge-tuning/4-validation.md`, `.r2-decisions.md` | A2 schema, B-locked-rubric, persona cards | 0× F-R2-1, ≤2 combined F-R2-2/3/4 |
| C2 | B2b-rerun + Plan B close | `r2-judge-tuning/2b-rerun.md`, `r2-judge-tuning/PLAN.md` → v3, `upstream-tuning-queue.md` (URI-023 close) | C1 outputs | URI-023 #9 closed; #1-8 deferred |
| C3a | s02 regen — screen-writer on s02e01 + s02e02 | `active-project/theater/proto-lines.md` | `tens-mega.md` kickback criteria | regen accepted by tens re-fire |
| C3b | Phase 2 iter-2 audit + Phase 3 (A3 disclosed deviations) | `active-project/staff/auditor/season-s02-pass-{2,3}-*.md` | s02 aggregate | both phases produce reports |
| C3c | Re-fire Phase 4 Step 1.5 **per-spec parallel-fork** | `active-project/theater/facets/tensometer-s02e{01..06}.md`, `season-s02-pass-S4-step1.5-tens-mega.md` | persona cards (post-A1), tens rubric | all six episodes SHAPE-OK or band-only SIGNAL |
| C3d | Step 2 (audience + mechanic) + Step 3 (mechanical write-out) | `active-project/staff/auditor/season-s02-step2-*.md`, per-episode bone files | s02 aggregate, tens facets | combined SPLIT-ACCEPT all six episodes |
| C3e | Phase 5 (Persist) + Phase 6 (Orchestrator verdict) | `staff/showrunner/memory.md`, `staff/auditor/season-s02-orchestrator-verdict.md` | orchestrator-critic card | verdict PASS or PASS-WITH-NOTES |
| C4 | Phase 2 migrations | `.claude/commands/and-season.md` (new passes), `/and-facets-r1.md` (Layer deletions), `.claude/commands/and-shoot.md` (Phase 0 rename), `schemas/facet.schema.md` (dual-provenance notes) | `plan-a-a4-spec-staging.md`, `plan-a-a4-rubric-portability-audit.md` | s02 second run still PASS with all four bone-gates active |
| C5 | URI-027 schema patch + final close | `schemas/audit-report.schema.md` (F-R2-* class definitions aligned to A-corpus), `upstream-tuning-queue.md` (URI-023 + URI-026 + URI-027 closed) | URI-027 entry | queue items closed; PLAN.md v3 |

### C1 — B4 validation re-run

1. `git branch r2-tuning-pre-rerun` (save).
2. `git checkout 3cd53e5 -- active-project/theater/facets/` (revert to pre-R2 baseline for clean re-run).
3. `/and-facets-r2 s01e01` with the edited command (B3 already landed).
4. Rebuild cite-index.
5. Audience adjudication of new R2 output (3 personas, 1 sweep — pattern from `memory-tuning-r2-final.md`).
6. Score F-R2-* counts; emit `.r2-decisions.md` with `f-r2-counts:` frontmatter conformant to A2 schema (using **A-corpus class definitions**, per URI-027 deferred decision).

**Pass:** 0× F-R2-1, ≤2 combined F-R2-2/3/4 across all R2-touched entries.
**Fail (≤3 iterations):** diagnose, edit, re-fire. After third failure → DISCIPLINE-FAIL surfaced; escalate to user before C2.

**Dispatch budget:** ~20 (6 R2 layers including feeling × 3 + 6 audience + ~3 arbiter + cite rebuilds).

### C2 — B2b-rerun + Plan B close

1. Score `.r2-decisions.md` against `B-locked-rubric.md` G1–G4 across the full 10-facet corpus (native logs make F-R2-2 motive-honesty scoreable, which B2b-baseline could not do).
2. Write `r2-judge-tuning/2b-rerun.md`.
3. PLAN.md → v3 in `design/shoot-v2/r2-judge-tuning/`.
4. `upstream-tuning-queue.md`: URI-023 #9 marked CLOSED; #1-8 remain open (feeling-rubric V2.1 carry-back; out of scope for Plan C).

**Dispatch budget:** 0.

### C3 — A3 retry on s02 (the gate round-trip)

**C3a — regen s02e01 + s02e02.** screen-writer dispatch with kickback criteria from `active-project/staff/auditor/season-s02-pass-S4-step1.5-tens-mega.md`:
- s02e01: break the rung-1 stretch at bones 122–162; introduce scene peaks in monitoring-folio + Mira-common scenes.
- s02e02: introduce rupture beat in gathering scenes (358–396, 461–489); lift antagonist-axis charge above 3.

**C3b — Phase 2 iter-2 audit + Phase 3.** Address A3's disclosed deviations: Phase 2 iter-2 was not formally re-audited; Phase 3 was skipped entirely. Both run before Step 1.5 re-fires so the input corpus is convergence-verified.

**C3c — re-fire Step 1.5 per-spec.** Parallel-fork dispatch (not single-fork as in A3). Re-rate s02e01–e06 against the tens rubric.

**Pass:** all six episodes SHAPE-OK or band-only SIGNAL. **Fail second attempt** → escalate before C4 (regen may not be sufficient for structural inertness; user adjudication required).

**C3d — Step 2 + Step 3.** Combined audience + mechanic verdict (SPLIT-ACCEPT requires both ≥2-persona ACCEPT and MECHANIC-CLEAN per persona). Mechanical write-out to per-episode bone files.

**C3e — Phase 5 + Phase 6.** Persist; orchestrator verdict.

**Dispatch budget:** ~30 (regen × 2 + audit × 2 + parallel-fork tens × 6 + audience × 3 personas × 6 episodes + mechanic × 6 + write-out + verdict). Per-window inner iteration cap 2 per URI-026.

### C4 — Phase 2 migrations

Gated on C3 PASS. Use `plan-a-a4-spec-staging.md` + `plan-a-a4-rubric-portability-audit.md` as drafts — do not redraft from scratch.

For each of sensory / state-updates env / loc-state:

1. New `/and-season` pass authoring the facet on the per-episode aggregate post-split (or aggregate-scope if rubric-portability audit clears it).
2. Phase 4 Step 2 mechanic section invokes `/and-facets-audit.md` library against the new per-episode file.
3. Corresponding `/and-facets-r1` Layer deleted (Layer 1 for tens already gone in URI-026; Layers 1b / 2b / 3a for sensory / state-updates / loc-state per A4 spec staging).
4. `/and-shoot` Phase 0 rename contract extended: `<facet>-<slug>.md → <facet>.md`.
5. `schemas/facet.schema.md` dual-provenance note extended.
6. Reuse A1 brief-reduction pattern: tens-attack vocabulary lived in card body; same pattern for sensory / state-updates / loc-state attack vocabulary if persona-card body sections need new sub-sections.

**Validation:** `/and-season s02` re-fires with all four bone-gates active. Must still PASS.

**Dispatch budget:** ~18 (~6 added per facet × 3 facets, parallelizable per-episode).

### C5 — URI-027 patch + close

1. Patch `schemas/audit-report.schema.md` F-R2-* class definitions to match `A-corpus.md` (option 1 per URI-027). One paragraph edit.
2. `upstream-tuning-queue.md` updates:
   - URI-023 → CLOSED (item 9 lands C2; items 1–8 remain open as separate URI-NN, renumbered out).
   - URI-026 → Phase 2 LANDED (C4).
   - URI-027 → CLOSED.
3. PLAN.md v3 in r2-judge-tuning dossier marked terminal.
4. Open question 4 (orchestrator-critic two-card unification) carries forward as a new URI for a future session — explicitly out of scope.

## Stop conditions

- **C1 fails after 3 iterations** → DISCIPLINE-FAIL surfaced; escalate to user before C2. Native R2 emission is the load-bearing capability for F7; if it cannot converge, F7 is unreliable and downstream `/and-season` gates inherit that.
- **C3c fails second attempt** → escalate to user before C4. The s02e01 inert stretch is structural; if a second screen-writer regen also produces SHAPE-FAIL HARD, the diagnosis is "the proposed split itself is bad" or "the season-plan chunk for s02e01 doesn't carry shape" — both are user-decision.
- **Dispatch budget breach** at any C-step → `/and-cut` checkpoint; resume in next session. Do not fork to a parallel session.

## Files this plan edits

- `active-project/theater/facets/*.md` — C1, C3 (s01e01 R2 outputs + s02 per-episode tensometer files)
- `active-project/theater/proto-lines.md` — C3a (s02e01 + s02e02 regen)
- `active-project/staff/auditor/season-s02-*.md` — C3
- `active-project/staff/showrunner/memory.md` — C3e
- `design/shoot-v2/r2-judge-tuning/{2b-rerun,4-validation,PLAN}.md` — C1, C2
- `.claude/commands/and-season.md` — C4 (new passes)
- `.claude/commands/and-facets-r1.md` — C4 (Layer deletions)
- `.claude/commands/and-shoot.md` — C4 (Phase 0 rename contract)
- `schemas/facet.schema.md` — C4 (dual-provenance notes)
- `schemas/audit-report.schema.md` — C5 (URI-027 patch)
- `design/shoot-v2/upstream-tuning-queue.md` — C2, C5

## Concurrency contracts

None. Single session. The prior plans' contract tables collapse to: "do these steps in order in the same session."

## Risks

1. **C3 may fail again.** s02e01 inert stretch may be structural. Stop condition above; do not iterate blindly.
2. **C4 dispatch budget.** Combined run with all four bone-gates active may breach the orchestrator-critic R1 hard cap. Mitigation: parallelize per-episode dispatches; recalibrate cap empirically; per-window inner iteration cap 2 (already in URI-026).
3. **URI-027 schema patch is small but cross-cuts B-locked-rubric.md citations.** C5 edit must verify no surviving citations in `.r2-decisions.md` files emitted in C1 use the old framing. Spot-check after the patch lands.
4. **A4 rubric portability for state-updates / loc-state unknown.** Pre-stage audit at `plan-a-a4-rubric-portability-audit.md` covers tens. C4 must extend the audit for the other three before promotion. Route per-episode-post-split if calibration constraint matches tens.
5. **Orchestrator-critic two-card unification** (Open question 4 from bone-gate Phase 1 plan) remains deferred. F7 emission contract is the workaround. Becomes urgent if C1 surfaces a stubborn F-R2-1 the s01e01 corpus cannot resolve.

## Verification (end-to-end)

1. `cat active-project/theater/facets/.r2-decisions.md` shows per-entry decisions; `f-r2-counts:` frontmatter conforms to A2 schema.
2. `grep "URI-023.*CLOSED\|URI-026.*CLOSED\|URI-027.*CLOSED" design/shoot-v2/upstream-tuning-queue.md` → 3 hits (post-C5).
3. `active-project/staff/auditor/season-s02-orchestrator-verdict.md` reads PASS or PASS-WITH-NOTES.
4. `ls active-project/theater/facets/tensometer-s02e*.md` → 6 files.
5. After C4: `/and-facets-r1` has no tens / sensory / state-updates env / loc-state Layers; `/and-season s02` re-fire still PASSes.
6. `grep -A 5 "F-R2-2\|F-R2-4" schemas/audit-report.schema.md` matches definitions in `design/shoot-v2/r2-judge-tuning/A-corpus.md`.
