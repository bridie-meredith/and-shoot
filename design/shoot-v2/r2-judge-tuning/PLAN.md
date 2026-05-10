---
doc: R2 judge tuning — terminal plan v3 (project CLOSED)
date: 2026-05-10
revision: v3-terminal — Plan B B3+B5+B2a landed in parallel-session; B4+B2b-rerun executed at Plan C C1 (single-session unified replacement for Plan A+B parallel). Project closed.
supersedes: PLAN v2 (parallel-session structure); PLAN v1 (replaced)
canonical-execution-plan: design/shoot-v2/plan-c-2026-05-10-unified.md C1 + C2 (replaces Plan B; parallel-session Plan B retired with reconciliation overhead — see archive/notes/problems.md P17)
historical-execution-plan: design/shoot-v2/plan-and-facets-r2-2026-05-10.md (Plan B; superseded)
purpose: tight action list + decision points + honest risk register; terminal version retained for trace.
status: CLOSED 2026-05-10. URI-023 #9 landed and closed. URI-023 #1-8 remain open under feeling-rubric V2.1 parent.
---

## v3-terminal status note (top-of-file)

**This project is CLOSED.** Plan B's parallel-session execution landed B3 (§Form re-test + decision-shard emission), B5 (queue hygiene partial), B2a (audience review + G5 position-gate). Plan C C1 (single-session unified) executed B4 (validation re-run on s01e01 against R1 baseline) and B2b-rerun (decision-discipline scoring against native logs). Gate PASS: 0× F-R2-1; F-R2-2/3/4 sum=2.

Native log evidence is in `active-project/theater/facets/.r2-decisions.md`. Discipline scoring in `2b-rerun.md`. Validation summary in `4-validation.md`.

**URI-023 item 9 (§Form re-test mandatory before any verdict): CLOSED.**
**URI-023 items 1-8 (feeling rubric V2.1 carry-back): remain open** for a future feeling-rubric session.
**URI-027 (F-R2-* schema reconciliation): patch lands at Plan C C5.**

### Historical action map (v2 → Plan B → Plan C)

Plan B (`design/shoot-v2/plan-and-facets-r2-2026-05-10.md`) was the v2-era canonical execution path. Action mapping:

| v2 Action | Plan B step | Status |
|---|---|---|
| Action 1 — cite-index inspection + baseline reconstruction | B1 | **landed** (cite-index summary authored; baseline reconstruction blocked — see `1-baseline-reconstruction.md`) |
| Action 2a — audience entry-quality review | B2a | **deferred to runtime session** (≤6 dispatches; scaffolding only) |
| Action 2b — main-session decision-discipline review (baseline) | B2b-baseline | **deferred** (depends on B1 baseline; falls back to single-instance dossier evidence per `1-baseline-reconstruction.md`) |
| Action 3 — carry-back synthesis + command edits | B3 | **landed** (see `3-carry-back.md`) |
| Action 4 — validation re-run | B4 | **deferred to runtime session** (~20 dispatches; revert blocked; see `4-validation.md`) |
| (post-Action 4) Action 2b-rerun against native logs | B2b-rerun | **deferred** (depends on B4 producing `.r2-decisions.md`) |
| Project close + sentinel | B5 | **landed** (queue updated, sentinel in `4-validation.md`, this file → v3) |

URI-023 item 9 (mandatory blind §Form re-test on R2 revisions) **landed unconditionally** at B3 per HARD-002 fix. The other items 1–8 remain in-queue as `rubric-feeling.md` V2.1 carry-back work, scope-separate from R2 discipline.

URI-025 status: superseded by URI-026 (already in queue text). v1's "URI-025 unblocked by R2 close" framing is stale; Plan B v3 no longer claims to unblock URI-025. F7 emission contract per `staff/orchestrator-critic/card.md` (Plan A A2) is what consumes Plan B's `.r2-decisions.md` frontmatter at orchestrator Phase 6.

---

# R2 Judge Tuning — Plan v2

## Goal

R2 (the graph-aware hybrid judge in `.claude/commands/and-facets-r2.md`) systematically drifts from rubric discipline when revising entries to close seams, and substitutes graph-revealed niches for at-rest evidence when adding entries. Confirmed: 1 named regression in feeling (feel:10 form-violation introduced by revision); pattern of NI-spine adjacency-dependence across 4+ memory entries + 2 feeling entries. Goal: make R2 produce decisions that survive audience adjudication on the first pass.

### Metric (revised — addresses HARD-001)

We do **not** have a clean R2-raw-decision baseline. The 75% figure cited in v1 was post-revision adjudication, not pre-revision raw R2 accuracy. Two consequences:

1. **Headline metric is failure-mode-hit count, not accept rate.** Validation passes when audience adjudication of R2-touched entries surfaces **0 instances of F-R2-1 (form-drift on revisions)** and **≤2 instances of F-R2-2 / F-R2-3 / F-R2-4 combined**. This directly tests whether the gates work; it does not require a clean baseline.
2. **Accept rate tracked as secondary signal only.** We record clean-ACCEPT % on R2-touched entries but use it as movement indicator, not pass/fail.

Action 1 includes attempting baseline reconstruction from git history of pre-Phase-4 facet states; if the data exists, accept-rate becomes a real metric. If not, we proceed on failure-mode-hit count alone.

## What we have

- **Corpus**: memory R2 cycle (8 entries, audience-adjudicated post-revision) + feeling Phase 5 findings (1 named regression: feel:10; 9 process items) + s01e01 cite-index R1→R2 diff (uninspected; Action 1 inspects).
- **R1 authors**: tuned, all 10 facets at 100% on s01e01 post-tuning.
- **Audit (cross-cutting)**: untuned (URI-006); flag-only.
- **Audience**: 3 personas active. Tuned for entry-quality review during R1 facet work. **Not tuned for decision-discipline review** (load-bearing constraint, see Action 2 split below).

## What we don't have

- Clean pre-revision baseline for R2 raw decision accuracy.
- Empirical dispatch cost for arbited reviews (the +20–30% in C is a guess).
- Held-out corpus. Memory + feeling are already adjudicated; the other 8 facets ran R2 untuned and are the only unadjudicated R2 outputs available.

## Plan (4 actions)

### Action 1 — Inspect the cite-index diff + attempt baseline reconstruction

Read `active-project/theater/facets/_cite-index.md` (current, post-R2) and the equivalent from git history pre-R2. Produce a one-page summary: per facet, count of R2 mutations (REVISE / ADD / DELETE), citation deltas, lonely-entry deltas.

**Also attempt baseline reconstruction:** check git history for pre-Phase-4 versions of memory.md and feeling.md. If pre-revision R2 raw decisions are recoverable, count how many were accepted by audience without modification. This is the missing baseline.

**Output**: `1-cite-index-summary.md` + (if data available) `1-baseline-reconstruction.md`. ~30–60 minutes, no dispatches.

**Decision points (HARD-002 fix applied):**
- If R2-touched entries across non-memory-non-feeling facets < 20: scope narrows to memory + feeling. Action 4 validation runs but is acknowledged corpus-internal (SIGNAL-003 fix); generalization claim is held back. Project still closes properly; it does not skip Action 4.
- If pre-revision baseline data is unavailable: confirmed; metric falls back to failure-mode-hit count only. Project continues.
- **The only way the project closes after Action 1 with no command edit is if cite-index inspection shows R2 was effectively no-op across all 10 facets (no mutations to evaluate). Even then, URI-023 item 9 still lands as a command edit per HARD-002 fix.**

### Action 2 — Split validation: audience for entry-quality, main-session for decision-discipline

**SIGNAL-001 + SIGNAL-002 fix.** Audience personas are not equipped to evaluate decision discipline (motive-honesty, lonely-entry isolation, form-drift on revisions). They evaluate entry quality. Action 2 splits accordingly:

**Action 2a — Audience entry-quality review.** Dispatch the 3 audience personas against R2-touched entries on s01e01. Standard R1-style review: did the entry earn its place by audience taste? Free-form per-entry verdicts. **Arbiter does not run on persona output** (SIGNAL-002 fix — triggers don't fit prose-reasoning personas). Output: clean-ACCEPT %, named seams. ~6 dispatches.

**Action 2b — Main-session decision-discipline review.** I (main session) read R2's existing decision logs against gates G1–G4 in `B-locked-rubric.md`. Per R2-touched entry, evaluate:
- F-R2-1: did revision close the seam without introducing form-drift? (Read entry pre and post revision.)
- F-R2-2: did the add justify itself with at-rest evidence, or work backward from a graph-revealed niche?
- F-R2-3: does the lonely-entry decision hold when adjacent context is set aside?
- F-R2-4: across the facet, do patterns I shouldn't see appear?

Output a count per failure mode + flagged instances. No dispatches; main-session reading. ~30 minutes per facet × number of facets with R2 mutations.

**Decision points:**
- If 2a finds clean-ACCEPT % < 70: entry quality is the load-bearing problem; tuning shifts to per-facet R1 author re-tuning, not R2 judge tuning. Project re-scopes.
- If 2a clean and 2b finds 0 F-R2-1 + ≤2 F-R2-2/3/4 hits: existing R2 already meets target. Project closes after Action 3 lands URI-023 item 9 (the ratchet-up fix the queue already commits to) and skips Action 4.
- Otherwise: proceed to Action 3.

### Action 3 — Carry-back synthesis; edit `and-facets-r2.md`

From Action 2 findings, identify command-side edits. Required minimum (HARD-002 fix): land URI-023 item 9 — the mandatory blind §Form re-test on R2 revisions. This lands regardless of Action 2's other findings.

Additional candidates depending on Action 2 evidence:
- Add G1–G3 (and G4 — HARD-003 fix; G4 was misread in v1 and is non-mechanical) as required brief content in R2 layer dispatches.
- Simplify decision log format to free-prose-with-verdict-line (SIGNAL-004 fix; current B template's labeled subfields are themselves checklist-shaped).
- Reduce arbiter triggers in C from 6 to the 2–3 that Action 2 evidence shows fire usefully.

**Output**: `3-carry-back.md` + edits to `.claude/commands/and-facets-r2.md` + targeted edits to `B-locked-rubric.md` (decision log format) and `C-arbiter-protocol.md` (trigger reduction). No new dispatches.

### Action 4 — Validation re-run

Re-run R2 on s01e01 with the edited command. Dispatch all 4 R2 layers (NI, memory, feeling, metaphor) sequentially. Arbiter active on R2 layer dispatches only — **not** on audience persona dispatches (SIGNAL-002 fix). Audience adjudication of new R2 output (Action 2a-style review).

**Output**: `4-validation.md` + mutated `active-project/theater/facets/`. Budget: ~20 dispatches (4 R2 layers + 6 audience + intervention overhead).

**Validation passes when**: 0 instances of F-R2-1, ≤2 combined F-R2-2/3/4, and (if scope is narrow per Action 1) acknowledgment that result is corpus-internal.

**Caveat (SIGNAL-003 explicit):** if the corpus is memory + feeling only, this validation is corpus-internal — it shows the gates work on the data we tuned against. Generalization claim requires next-episode validation when s01e02+ have R2 runs to evaluate. URI-025 tensometer-promotion **still gates on this validation passing**, but the queue entry should record the corpus-internal caveat (Phase 6 close note).

**Decision point**: validation passes → Action 5 (close + URI-025 unblock). Validation fails → diagnosis + targeted gate revision; re-run. Three failed iterations exhausts budget; surface as DISCIPLINE-FAIL for human adjudication.

## What got cut from v1 (audit-driven)

- **G4-drop instruction (HARD-003).** v1 said drop G4 because count-thresholds. Those thresholds aren't in current G4. G4 stays.
- **"No command edit" exit branch in Action 3 (HARD-002).** URI-023 item 9 lands regardless. Project doesn't close without honoring the queue commitment.
- **Arbiter on audience personas (SIGNAL-002).** Triggers calibrated for rubric-using reviewers; personas write prose. Arbiter runs only on R2 layer dispatches.
- **Single audience-validation gate covering both quality + discipline (SIGNAL-001).** Split into 2a (audience for entry quality) + 2b (main session for decision discipline).
- **Risk 5 parallel-path language (SIGNAL-005).** URI-025 contingency stands. Tensometer-promotion does not start in parallel.
- **Decision log labeled-subfield format (SIGNAL-004).** Action 3 simplifies to free-prose-with-verdict-line if Action 2 evidence supports.

## Risks (revised)

1. **Corpus thinness.** Memory + feeling are the only adjudicated R2 cycles. If non-memory-non-feeling facets had R2 effectively no-op, narrow-scope path triggers and validation is corpus-internal.
2. **No clean baseline.** Falls back to failure-mode-hit count metric. Headline number is "0 F-R2-1 instances," not "X% accept rate."
3. **Audience personas not tuned for decision-discipline.** Action 2b (main-session decision-discipline review) is single-source. No second-line check on my reading. If I misjudge a verdict, no one catches it.
4. **R2 is not facets-shaped.** Five-phase facet template assumes a domain rubric and writer authoring against it. R2 is a meta-judge. Plan analogy may be load-bearing in places it shouldn't be.
5. **Tensometer promotion gated on this project closing.** URI-025 contingency holds. If R2 tuning takes 3+ sessions, tensometer is blocked. This is the chosen tradeoff per recorded user direction.

## Action sequencing (sessions)

| Session | Actions | Dispatches |
|---|---|---|
| S+1 | Action 1 + Action 2b (both no-dispatch) | 0 |
| S+2 | Action 2a | ≤6 |
| S+3 | Action 3 (always lands URI-023 #9; other edits Action-2-driven) | 0 |
| S+4 | Action 4 | ~20 |

## Success criteria for project close

R2 tuning closes when:

1. URI-023 item 9 has landed in `.claude/commands/and-facets-r2.md`.
2. Action 4 validation has produced 0 F-R2-1 + ≤2 combined F-R2-2/3/4 on s01e01 R2-touched entries.
3. Clean-ACCEPT % is recorded as secondary signal (not gating).
4. Corpus-internal vs. generalizable scope is explicitly stated.
5. URI-023 closes; URI-025 tensometer-promotion is unblocked (with the corpus-internal caveat if applicable).

## What this plan is NOT

- Not a full audit of /and-facets — that's URI-006.
- Not a content-rubric edit — items 1–8 of URI-023 land separately as feeling-rubric V2.1.
- Not a guarantee R2 needs deep tuning — it is a structured way to find out and to land at minimum URI-023 item 9.
