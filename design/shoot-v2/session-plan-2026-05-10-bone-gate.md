# /and-season — Bones-First Hard Gate (tens-into-/and-season, fork-revised, shared-reviewer)

## Context

User direction this session (2026-05-10, concurrent with `/and-facets` tuning session):

1. **Move the tensometer facet into `/and-season`** as a hard gate the run must pass.
2. **Tens output is part of `/and-season`'s proto-lines deliverable.**
3. `/and-facets` will later lose tens authoring (read-only, then drop).
4. **Bones-first principle:** if the proto-lines are deformed, no facet skin saves the subject. Audience entertainment review must judge tens-rated bones, not bare bones or post-skin output.
5. **Shared reviewer resources (load-bearing).** Reviewer assets — audience persona cards (`Threshold Discipline`, `Season-Scope Adversarial` sections), the auditor class library (`CURVE-SHAPE`, `AP-SCAN`, `FREQUENCY-BAND`), tens rubric — are authored once and consumed from both pipelines. No fork. Patterns surfaced by `/and-season` audience runs feed `/and-facets` TASTE-FLAG codification; auditor class refinements (URI-018/019/020) land in the shared library and benefit both. This is URI-025's "carry-the-mechanism" principle made concrete.

**Rubric reality check (forced by fork):** `design/shoot-v2/rubric-tensometer.md` was calibrated **per-episode** (~150-line corpus, unique-climax-per-episode clause, scene-boundary by loc-state inheritance with TBD-boundary fallback). Aggregate-scope authoring (~900 lines, 3+ embedded climaxes) is structurally incompatible. **Tens authoring runs per-episode AFTER Phase 4 split**, not at aggregate-scope before split.

---

## Architecture (Option B — per-episode, post-split, shared-reviewer)

Position: tens authoring inserts as **new Pass 4.5** (per-episode, post-split). Audience review of tens-rated bones extends Phase 4 Step 2. **No aggregate-scope tens pass.**

### Pass 4.5 — Tens authoring (NEW, per-episode)

- After Phase 4 produces per-episode proto-line files, dispatch dramatist once per episode (parallel) to rate bones.
- **Same dispatch contract as `/and-facets-r1` Layer 1a:88** — fork-discipline forbids behavior cards, vibes, audience personas, source prose. Same rubric file, same fork-mode. The dispatch surface is shared; only the invocation point differs.
- Output: per-episode `theater/facets/tensometer-<episode-slug>.md` (slug-suffixed to avoid collision with `/and-facets-r1`'s `tensometer.md`).
- Rubric path: `design/shoot-v2/rubric-tensometer.md`.
- Total dispatch cost: 1 per episode = 3–6 dispatches per season.

### Phase 4 Step 2 — Split review (EXTENDED, shared-reviewer)

Each persona's review fork loads bones + tens-ratings + the *same* `Threshold Discipline` + `Season-Scope Adversarial` body sections that `/and-facets` audit consults via TASTE-FLAG. Per-persona report contains two **separately named, shared-source** sections:

- **Audience taste verdict** (audience-owned) — ENGAGED / TOLERATED / BORED per stretch + persona-specific tens-attack findings. Owner: persona.
- **Mechanic arithmetic verdict** (auditor-owned, shared class library) — calls into the same `CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND` classes defined in `.claude/commands/and-facets-audit.md`. **No /and-season-specific reimplementation.** The audit command is invoked in a dispatch-as-library mode against the per-episode tens file. Owner: rubric.

Dominance: audience taste wins for bone-regen routing; mechanic verdict gates re-rating after regen. Findings carry `OWNER:` tags so Phase 6 can attribute HARDs.

**Cross-pipeline feedback loop (explicit):** patterns the audience flags here that the mechanic rubric did not catch graduate into AP-SCAN entries via the same TASTE-FLAG → AP-SCAN promotion pipeline `/and-facets-audit.md:130` already documents. /and-season's audience runs become a training source for the shared auditor, paying for itself.

### Phase 6 — Orchestrator-critic verdict (EXTENDED)

- Add **failure mode F7 — Bone-gate residual:** any open tens-gate HARD at end-of-run = FAIL regardless of routing. Preserves F1–F6 enumeration discipline by extension.
- Verdict template grows `tens-gate-convergence` line with owner-attribution.

---

## Iteration policy

- Inner loop on flagged window: screen-writer regenerates bones → re-rate tens → re-audience.
- **Regen-mode discipline:** brief names mode — `REGEN-REPLACE` (preserve aggregate IDs of survivors per URI-010), `REGEN-ADD` (new bones get next-available 900-range IDs), `REGEN-BOTH`. Brief carries position-aware-mapping + `# pov:` preservation clauses.
- Per-window cap: 2 iterations (tightened from 3 per Open question 1 in prior revision — caps dispatch growth).
- Worst-case budget: tens-rate × 6 + audience × 3 × 6 + regen × 2 × 3 windows ≈ 30 added dispatches. Combined with rest of /and-season (~30) trends to ~60. Tight against the cap; recalibrate empirically after first fire.

---

## Cross-pipeline contract

- Per-episode `theater/facets/tensometer-<slug>.md` written by `/and-season` Pass 4.5.
- `/and-facets-r1` Layer 1 still writes `tensometer.md` (canonical) — **no path collision; no shared-writer guard required**.
- `/and-shoot` Phase 0 renames `tensometer-<slug>.md` → `tensometer.md` when starting that episode (single, atomic rename; no re-author dispatch).
- `/and-facets-audit.md` is invoked as library at Phase 4 Step 2 mechanic section — same command, same classes. **The audit command becomes the shared review surface, not just /and-facets's internal pass.**

---

## Persona-card edits — deferred to Phase 1.5 (shared-asset edit)

Persona cards (`active-project/audience/*/card.md`) are **shared reviewer assets**. The parallel facet session reads them in R2; this session must not change their body text mid-flight. Phase 1 ships with tens-attack vocabulary in the *dispatch brief* at Phase 4 Step 2, not in card body.

Phase 1.5 (post-facet-session merge): single coordinated edit promotes the brief-level tens-attack categories into card body text. Result is *one* shared body section that both `/and-season` Phase 4 Step 2 and any future `/and-facets` TASTE-FLAG hook consume.

---

## Files this session edits

1. `.claude/commands/and-season.md` — add Pass 4.5; extend Phase 4 Step 2 with shared-reviewer audience+mechanic invocation; mechanic section calls `/and-facets-audit.md` as library; Phase 5 print summary updated with `tens-gate` line.
2. `staff/orchestrator-critic/card.md` — add F7; extend verdict template `tens-gate-convergence` line with owner-attribution.
3. `schemas/facet.schema.md` — note tens dual provenance (per-slug primary path; flat-canonical legacy); note that audit class library is shared across pipelines.
4. `CLAUDE.md` — Rule 10 amended; new note on shared-reviewer-resources principle.
5. `design/shoot-v2/upstream-tuning-queue.md` — open URI-026 (tens-into-/and-season Phase 1, shared-reviewer); supersede URI-025 IP-2 author-mode tens block; cross-link URI-018/019/020 as shared-library beneficiaries.

**Not touched (concurrency / scope):**
- `.claude/commands/and-facets*.md` — facet-session territory. (Audit command's *use* as library at Phase 4 Step 2 is new wiring on /and-season's side; the audit command itself is unmodified.)
- `active-project/audience/*/card.md` — deferred to Phase 1.5.
- `design/shoot-v2/rubric-tensometer.md` — rubric unchanged in Phase 1.

---

## Actions (final, ordered)

1. Read `staff/orchestrator-critic/card.md` end-to-end to confirm F-mode numbering + verdict template structure.
2. Read `.claude/commands/and-facets-audit.md` invocation surface end-to-end to confirm it is callable as library (separable from /and-facets's internal dispatch). If not, scope a minimal refactor as part of Phase 1.
3. Add Pass 4.5 spec to `.claude/commands/and-season.md` — dispatch dramatist per episode in parallel; fork-discipline brief identical to /and-facets-r1 Layer 1a; output path slug-suffixed.
4. Extend Phase 4 Step 2 — audience reads bones+tens; per-persona report splits into audience-taste + mechanic-arithmetic sections with `OWNER:` tags; mechanic section invokes /and-facets-audit.md as library on per-episode tens file; brief carries tens-attack categories explicitly (since persona cards not edited yet).
5. Update `staff/orchestrator-critic/card.md` — add F7; extend verdict template.
6. Note dual provenance + shared-library status in `schemas/facet.schema.md`.
7. Amend `CLAUDE.md` Rule 10 + shared-reviewer principle paragraph.
8. Open URI-026 in `design/shoot-v2/upstream-tuning-queue.md`; supersede URI-025 IP-2 tens block; cross-link URI-018/019/020.
9. **Test path:** queue `/and-season-plan s02` then `/and-season s02` as first live-fire. Existing s01 corpus untouched.
10. **Phase 1.5 (post-facet-session merge):** promote tens-attack brief categories into shared persona-card body text — one coordinated edit.
11. **Phase 2 (later):** sensory + state-updates env + loc-state migration; /and-facets-r1 Layer 1 deletion; audit class library refinements (URI-018/019/020) land into the shared command and benefit both pipelines.

---

## Verification

- `/and-season s02` produces per-episode `tensometer-<slug>.md` at Pass 4.5; Phase 5 print summary shows `tens-gate: PASS / FAIL / NEEDS-ITER`.
- Phase 4 Step 2 per-persona reports name both verdict sections with `OWNER:` tags; mechanic section content provably comes from /and-facets-audit.md class library (audit-command-version stamped in the report).
- Phase 6 verdict reports `tens-gate-convergence`; F7 triggers correctly on synthetic residual-HARD.
- s01 corpus left untouched; `/and-facets-r1` continues to function unchanged.
- After Phase 1.5: persona-card body text contains tens-attack categories; /and-season's Pass 4.5 brief is reduced to pointing at the card's body section, with no duplicated content.

---

## Shared-reviewer accounting

| Asset | Owner location | Consumed by /and-season | Consumed by /and-facets |
|---|---|---|---|
| `rubric-tensometer.md` | `design/shoot-v2/` | Pass 4.5 (primary) | Layer 1a (legacy until Phase 2) |
| Audience persona cards | `active-project/audience/*/card.md` | S3 / S6 / S9 / Phase 4 Step 2 | TASTE-FLAG anticipation reads same |
| `/and-facets-audit.md` class library (CURVE-SHAPE / AP-SCAN / FREQUENCY-BAND) | `.claude/commands/and-facets-audit.md` | Phase 4 Step 2 mechanic section invokes as library | Internal audit pass |
| TASTE-FLAG → AP-SCAN promotion pipeline | `/and-facets-audit.md:130` | Patterns from Phase 4 Step 2 audience feed in | Codifies into AP-SCAN classes |
| Orchestrator-critic card | `staff/orchestrator-critic/card.md` | Phase 6 verdict (primary) | `staff/audience/and-facets-orchestrator-critic/card.md` is /and-facets's own — see Open question 4 |

**Tuning cost savings:** any future tightening of the audit class library (e.g. URI-018 CURVE-SHAPE-EPISODE-INTERIOR) lands once and is consumed by both pipelines. No duplicate tuning project per pipeline.

---

## Open questions

1. **Audit command as library — does its current shape permit invocation outside /and-facets?** Action 2 surfaces this; if not, minimal refactor needed to expose audit classes cleanly to /and-season Phase 4 Step 2.
2. **60-dispatch cap pressure.** Worst-case ~60 total dispatches; tight. Either tighten per-window iteration cap to 2 (current plan), parallelize more aggressively, or recalibrate cap empirically after first fire (card permits).
3. **/and-shoot Phase 0 rename vs re-author.** Renaming `tensometer-<slug>.md` → `tensometer.md` is current plan; couples /and-shoot to /and-season output layout. Acceptable coupling since both are first-party commands.
4. **Two orchestrator-critic cards.** /and-facets has its own at `staff/audience/and-facets-orchestrator-critic/card.md`. The shared-reviewer principle suggests one card serving both runs. Phase 2 candidate: unify the two cards' shared sections, keep pipeline-specific failure modes separate. Not blocking Phase 1.

---

## Fork critique findings — disposition (updated for shared-reviewer revision)

| ID | Severity | Disposition |
|---|---|---|
| C1 — path collision | CRITICAL | RESOLVED by per-episode slug-suffix path; no shared-writer guard needed |
| C2 — rubric filename | CRITICAL | RESOLVED throughout |
| C3 — scene-boundary depends on loc-state | CRITICAL | DOWNGRADED — rubric's TBD-boundary fallback applies; tens + loc-state run parallel layer in /and-facets-r1 today, status quo preserved at per-episode scope |
| C4 — aggregate vs per-episode rubric | CRITICAL | RESOLVED by moving authoring to per-episode (post-split) Pass 4.5 |
| C5 — forbidden-input leak | CRITICAL | RESOLVED — Pass 4.5 brief explicitly mirrors /and-facets-r1 Layer 1a fork-discipline |
| M6 — conflated reviewer voices in S3 | MEDIUM | RESOLVED — Phase 4 Step 2 (not S3) report has named audience-taste + mechanic-arithmetic sections, distinct owners; mechanic section invokes shared library not a re-implementation |
| M7 — HARD ⇒ FAIL contradicts F1–F6 | MEDIUM | RESOLVED via F7 extension |
| M8 — regen add-vs-replace + URI-010 | MEDIUM | RESOLVED via REGEN-{REPLACE,ADD,BOTH} brief discipline |
| M9 — single-writer guard contradiction | MEDIUM | RESOLVED via per-slug output path |
| M10 — first-fire destroys evidence | MEDIUM | RESOLVED — first-fire is s02 (fresh corpus) |
| M11 — persona-card mid-flight semantic change | MEDIUM | RESOLVED via Phase 1.5 deferral + shared-asset framing |
| L12 — `# pov:` preservation in regen | LOW | Specified in regen brief |
| L13 — Phase 5 print summary line | LOW | Specified in Pass 4.5 spec |
| L14 — dispatch budget audit | LOW | Tightened (per-window cap 2 not 3); captured in Open question 2 |
