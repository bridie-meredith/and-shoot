# Plan A — `/and-season` bone-gate follow-on (Phase 1.5 + Phase 2)

**Date:** 2026-05-10
**Pipeline:** `/and-season`
**Predecessor:** `session-plan-2026-05-10-bone-gate.md` Phase 1 (LANDED, commit `6a5e4db`).
**Parallel sibling:** Plan B — `plan-and-facets-r2-2026-05-10.md` (R2 judge tuning).
**Supersedes:** the "Phase 1.5" and "Phase 2 (later)" stubs at the tail of `session-plan-2026-05-10-bone-gate.md`.

---

## Context

URI-026 bone-gate landed Phase 1 on 2026-05-10: Pass S4.5 (per-episode tens authoring after split), Phase 4 Step 2 split-review, F7 in `staff/orchestrator-critic/card.md`, URI-025 IP-2 superseded. Two pieces were intentionally deferred:

1. **Persona-card body edits** — held while Plan B was reading the cards in flight.
2. **Phase 2 migrations** — sensory + state-updates env + loc-state into `/and-season`; deletion of `/and-facets-r1` Layer 1.

This plan executes both, plus the cross-pipeline reconciliation seams the comparison session surfaced.

---

## Outcome

- Tens-attack vocabulary lives in persona-card body text (not duplicated in Pass S4.5 brief).
- `/and-facets-r1` Layer 1 (tens authoring) deleted; `/and-shoot` Phase 0 rename contract is the only handoff.
- Sensory + state-updates env + loc-state hard-gated at `/and-season`, same shape as tens.
- F7 emission contract is concrete: `/and-facets` runs surface F-R2-* counts in a Phase-6-consumable shape.
- s02 first-fire produces the first cross-corpus tens-rated bones outside s01.

---

## Action sequence

| # | Name | Owns | Locked-shared | Dispatches |
|---|---|---|---|---|
| A1 | Persona-card promotion (Phase 1.5) | `active-project/audience/*/card.md` | tens rubric, audit class library | 0 |
| A2 | F-R2-* → F7 emission contract | `staff/orchestrator-critic/card.md` (verdict template), `schemas/audit-report.schema.md` (R2-decision-shard format) | `/and-facets-r2.md` (read-only) | 0 |
| A3 | s02 first-fire | active-project working tree (write-locked vs Plan B) | tens rubric, persona cards (post-A1) | ~30 |
| A4 | Phase 2 migrations | `.claude/commands/and-season.md` (new passes), `/and-facets-r1.md` (Layer 1 deletion) | sensory / state-updates / loc-state rubrics | 0 (spec); ~6 (validation re-fire) |
| A5 | URI close + queue update | `design/shoot-v2/upstream-tuning-queue.md` | — | 0 |

### A1 — persona-card promotion (Phase 1.5)

Single coordinated edit across all three `active-project/audience/<persona>/card.md` files. Promote the tens-attack categories currently inlined in the Pass S4.5 dispatch brief (`.claude/commands/and-season.md`) into a new body section per persona. Section name fixed: `## Tens-attack vocabulary`. Result: the brief at Pass S4.5 reduces to "consult your `Tens-attack vocabulary` section" instead of carrying duplicated content.

**Precondition:** Plan B Action 4 has completed (R2 re-run done, no further reads of persona-card body during R2 mutation). Coordination signal: Plan B writes a sentinel line to `design/shoot-v2/r2-judge-tuning/4-validation.md` `## Done — persona cards released` when finished. A1 reads for the sentinel before opening any persona-card file.

**Verification:** `grep -c "Tens-attack vocabulary" active-project/audience/*/card.md` returns 3. Pass S4.5 brief in `.claude/commands/and-season.md` no longer enumerates the categories inline.

### A2 — F-R2-* → F7 emission contract

The bone-gate Phase 1 left `OWNER:` tags in Phase 4 Step 2 reports but never specified how `/and-facets`-side failure modes (F-R2-1..4 from `design/shoot-v2/r2-judge-tuning/A-corpus.md`) reach `/and-season`'s Phase 6. This action defines the contract:

1. **Schema clause in `schemas/audit-report.schema.md`:** R2-decision-shards (the `.r2-decisions.md` Plan B Action 3 emits) carry a top-of-file `f-r2-counts:` frontmatter line: `{f-r2-1: N, f-r2-2: N, f-r2-3: N, f-r2-4: N}`.
2. **Verdict template in `staff/orchestrator-critic/card.md`:** Phase 6 verdict line `f-r2-counts` reads from `active-project/theater/facets/.r2-decisions.md` if present. Threshold: `f-r2-1 > 0` is HARD; `f-r2-2 + f-r2-3 + f-r2-4 > 2` is SIGNAL.
3. **F7 amendment:** F7 fires on tens-gate residual HARD **or** any f-r2-counts HARD. Card-level edit only; no new failure-mode number (preserves enumeration discipline).

**Owner clarity:** A2 belongs to Plan A because the schema + critic card are `/and-season`-side. Plan B's only obligation is to emit the frontmatter line in the format A2 specifies — that obligation is recorded in Plan B Action 3.

**Verification:** synthetic `.r2-decisions.md` with `f-r2-1: 1` causes Phase 6 to print F7 with attribution to `/and-facets`.

### A3 — s02 first-fire

`/and-season-plan s02` then `/and-season s02`. First live-fire of Pass S4.5 + Phase 4 Step 2 + F7 against a fresh corpus.

**Concurrency contract with Plan B:** Plan B Action 4 mutates `active-project/theater/facets/` (R2 re-run on s01e01). Plan A A3 mutates `active-project/theater/proto-lines.md` and writes `active-project/theater/facets/tensometer-<s02-slug>.md`. Path-disjoint at the file level, but both touch `active-project/staff/showrunner/memory.md`. Serialization rule: **A3 starts only after Plan B Action 4 has committed.** Plan B records the commit SHA in `4-validation.md`; A3 reads it as the start signal.

(If A1 is sequenced before A3 — which the precondition requires — this is automatic, since A1 also gates on Plan B Action 4 completion.)

**Verification:** Phase 5 print summary contains `tens-gate: PASS`; `theater/facets/tensometer-<s02e01-slug>.md` etc. exist; Phase 6 verdict prints `f-r2-counts` line (likely empty for fresh-corpus run, but the line is present).

### A4 — Phase 2 migrations

Promote sensory + state-updates env + loc-state to `/and-season` hard-gates, mirroring the tens promotion. For each of the three:

1. New `/and-season` pass (analogous to S4.5) authoring the facet on the per-episode aggregate post-split.
2. Phase 4 Step 2 mechanic section invokes `/and-facets-audit.md` as library against the new per-episode file.
3. Corresponding `/and-facets-r1` Layer is **deleted**, not deprecated. (`/and-facets-r1` retains feeling, vibes, memory, NI, metaphor.)
4. `/and-shoot` Phase 0 rename contract extended: `<facet>-<slug>.md → <facet>.md` for each migrated facet.

**Schema:** `schemas/facet.schema.md` already notes dual provenance for tens (Phase 1); extend the same note to sensory / state-updates env / loc-state.

**Validation re-fire:** `/and-season s02` runs again with all four bone-gates active. Budget ~6 added dispatches per facet × 3 facets = ~18, but parallelizable per-episode.

**Risk noted:** rubric-portability is unverified for state-updates and loc-state at aggregate-then-split scope. The tens rubric required per-episode-post-split because of unique-climax calibration (§Context line 13 of bone-gate Phase 1 plan). Audit each rubric for the same structural incompatibility before promoting; if found, route the same way (per-episode post-split, not aggregate).

### A5 — queue close

Close URI-026 Phase 1 → Phase 2 in `design/shoot-v2/upstream-tuning-queue.md`; mark Plan A complete. Leave Open question 4 from bone-gate plan (two orchestrator-critic cards) as a separate URI for a future session — not in scope here.

---

## Files this plan edits

- `active-project/audience/<persona-1>/card.md`, `<persona-2>/card.md`, `<persona-3>/card.md` — A1
- `.claude/commands/and-season.md` — A1 (brief reduction), A4 (new passes)
- `.claude/commands/and-facets-r1.md` — A4 (Layer 1 deletion + sensory/state-updates env/loc-state Layer deletions)
- `.claude/commands/and-shoot.md` — A4 (Phase 0 rename contract extension)
- `staff/orchestrator-critic/card.md` — A2 (verdict template, F7 amendment)
- `schemas/audit-report.schema.md` — A2 (`.r2-decisions.md` frontmatter)
- `schemas/facet.schema.md` — A4 (dual-provenance notes for migrated facets)
- `design/shoot-v2/upstream-tuning-queue.md` — A5

## Files this plan does NOT touch (Plan B territory)

- `.claude/commands/and-facets-r2.md`
- `design/shoot-v2/r2-judge-tuning/B-locked-rubric.md`, `C-arbiter-protocol.md`, `PLAN.md`
- `active-project/theater/facets/*.md` until A3 (after Plan B Action 4 commit)

## Concurrency contracts (summary)

| Resource | Plan A access | Plan B access | Serialization |
|---|---|---|---|
| `active-project/audience/*/card.md` body | A1 writes | reads in A2a / A4 | A1 waits for Plan B sentinel in `4-validation.md` |
| `active-project/theater/facets/` | A3 writes new files | A4 mutates s01e01 files | A3 waits for Plan B Action 4 commit |
| `active-project/staff/showrunner/memory.md` | A3 writes | not touched | none needed |
| `staff/orchestrator-critic/card.md` | A2 writes | not touched | none needed |
| `schemas/audit-report.schema.md` | A2 writes | reads format | A2 lands before Plan B Action 3 emits |

A2 is the one Plan A item that needs to land **before** a Plan B step (Action 3 needs the schema). Sequence: A2 → (Plan B runs to completion) → A1 → A3 → A4 → A5.

---

## Verification (end-to-end)

1. `grep -c "Tens-attack vocabulary" active-project/audience/*/card.md` → 3.
2. Pass S4.5 brief in `.claude/commands/and-season.md` is reduced (no inlined attack categories).
3. Synthetic `.r2-decisions.md` with `f-r2-1: 1` triggers F7 with `/and-facets` attribution.
4. s02 run produces per-episode `tensometer-<slug>.md` and Phase 6 verdict line `f-r2-counts`.
5. After A4: `/and-facets-r1` no longer authors tens / sensory / state-updates env / loc-state; `/and-season` does; `/and-shoot` Phase 0 renames all four; s02 second run still PASS.
6. URI-026 marked Phase 2 complete in queue.

---

## Risks

1. **A4 rubric portability.** Sensory / state-updates env / loc-state rubrics may share the tens rubric's per-episode calibration constraint. Plan: audit each before promotion; route per-episode-post-split if so.
2. **A3 dispatch budget.** Bone-gate Phase 1 worst-case is ~60 dispatches; A4 adds three more facet passes per episode. May breach card limit. Mitigate by parallelizing per-episode dispatches and recalibrating after A3.
3. **Unification of two orchestrator-critic cards** (Open question 4 in bone-gate Phase 1 plan) is deferred. F7 emission contract here works around the duplication; full unification is a separate URI.
