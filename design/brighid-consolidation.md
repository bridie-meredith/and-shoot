# Brighid → and-shoot consolidation manifest

**Status.** v1 — 2026-06-13. Authored on principal direction: "bring brighid-creative-writing's improvement infrastructure over to and-shoot; port the whole pyramid; consolidate into a single routine that runs several times a day."

**What this is.** The controlling record for importing brighid-creative-writing's meta-layer (improvement / hygiene / tuning machinery) into and-shoot. Every brighid asset gets one disposition: **PORT** (bring over, adapt to the substance architecture), **FOLD** (its function is absorbed by an and-shoot routine/command, not a standalone file), or **DROP** (board/campaign/CYOA-specific; no and-shoot analog).

**Why adaptive, not copy.** The two repos share a meta-layer *shape* (a pyramid of named seats + cadence routines) but not a *vocabulary*. brighid authors prose through boards / campaign-map / gameboard / CYOA / wrap-C1.5 / vibe-cards / peeve-critics. and-shoot authors through substance contracts → bones → facets → stitch. A literal copy would import dead vocabulary. Everything PORTed is re-expressed in and-shoot terms.

---

## The consolidation target

A single recurring routine — **`/and-tend`** — plays the cadence work the brighid routines did, several times a day, work-queue + cadence driven, deferring when a chapter cascade is in flight. It dispatches the ported specialist seats. The pyramid lands as distinct agents (principal direction "port the whole pyramid"); `/and-tend` is the conductor.

```
                         /and-tend  (the recurring conductor — several times/day)
                              │
        ┌───────────┬─────────┼─────────┬───────────┬──────────┐
     ingrid       oskar      artur     margit      arbiter     admin
  (retrospective (foreman/  (janitor/ (librarian) (judge/   (proposer/
   + improvement  triage +   hygiene)             arbiter)   user-proxy)
   coordinator)   patterns)
```

- **ingrid** — surveys all signal sources, ranks improvement asks at book/series scope, dispatches the fixes. Brighid-delegated authority (may edit non-persona agent `.md`, specs/schemas, greenlight non-persona card mutations). Persona content → Brighid (non-delegable).
- **oskar** — per-run routing optimizer: triages findings by impact-to-cost, tracks patterns across chapters, writes save-as-new non-persona card mutations (margit reconciles), owns meta-layer housing (memory schemas, STM formats, tooling). Distinct from and-shoot's existing `studio` (set/environment manager).
- **artur** — repo-wide hygiene: taxonomy audits over `cards/`, index integrity, STM/LTM sweeps, parking-lot hygiene, state-file structural reconciliation. Trivial-fix allowlist; everything else routes.
- **margit** — already present. Unchanged role (card warehouse / catalog / validation / exemplar QC).
- **arbiter** — NEW seat (principal direction "an agent to act as judge and arbiter"). Judge mode = the dedicated tournament/harness scorer (replaces `general-purpose`). Arbiter mode = rules disputes, enforces the DEC-0115 design-inherent circuit breaker.
- **admin** — already present. Unchanged (user-proxy + process-critic / proposer).
- **`/and-forge`** — NEW command. Agent-parameterized training harness (the "harness to improve the editor and revisor"). Generates config variants → arbiter judges → winners promote. Subsumes brighid's `editor-persona-tuning` + `critic-persona-tuning`.

---

## Agent dispositions

| brighid seat | disposition | and-shoot landing | notes |
|---|---|---|---|
| naomi (director) | **DROP** | — | and-shoot orchestration is command-bodies + showrunner (CLAUDE.md Rule 2). The director seat is structurally already filled; importing it would duplicate the RUNBOOK protocol. |
| oskar (foreman/studio) | **PORT** | `.claude/agents/oskar.md` + `staff/oskar/` | Routing optimizer + pattern tracker + non-persona card mutations + meta-layer housing. "Studio housing" renamed to "meta-layer housing" to avoid collision with and-shoot's `studio` set-manager. |
| margit (librarian) | **already present** | `.claude/agents/margit.md` | No change. Reconciles oskar's save-as-new mutations. |
| artur (janitor) | **PORT** | `.claude/agents/artur.md` + `staff/artur/` | Hygiene ops re-pointed at `cards/`, `staff/*/`, `active-project/` memory + parking-lot. |
| ingrid (retrospective) | **PORT** | `.claude/agents/ingrid.md` + `staff/ingrid/` | Four signal sources re-mapped (below). "Project close" → and-shoot "book/series close." Feedback-intake folds into `/and-postop` + principal feedback. |
| (judge/arbiter — new) | **NEW** | `.claude/agents/arbiter.md` + `staff/arbiter/` | Principal-requested. Closes tournament-tuning Open Question #2. |

### ingrid's four signal sources — re-mapped

| brighid source | and-shoot source |
|---|---|
| `oskar.memory.md` triage + rut-class patterns | `staff/oskar/` triage memory + `staff/admin/process-proposals.md` (open / recurring) |
| `persona-review-queue.md` | `active-project/staff/showrunner/parking-lot.md` (open items) + auditor reports + the persona-content ESCALATE queue |
| `audience/*/ltm.md` cumulative stink | audience reactions in `/and-postop` convergence reports + `/and-stitch` Phase 9 cold-reads + `staff/arbiter/rulings.md` |
| `naomi.memory.md` session notes | `active-project/staff/showrunner/memory.md` + `cascade-checkpoint.md` + `staff/admin/decisions.md` |

---

## Workshop-routine dispositions (brighid's 18 `*.routine.md`)

| routine | disposition | and-shoot landing |
|---|---|---|
| `card-library-audit` (7 taxonomy scans) | **FOLD** | artur ops (`taxonomy_audit`, `index_sweep`) dispatched by `/and-tend` |
| `persona-efficiency-pass` | **FOLD** | margit op dispatched by `/and-tend` (card-bloat trim) |
| `editor-persona-tuning` | **FOLD** | `/and-forge editor` |
| `critic-persona-tuning` (evidence-pack, ≥80% catch-rate) | **FOLD** | `/and-forge <critic-target>` — catch-rate convergence carried as a forge success metric |
| `retake-tuning` (paired global+deliverable mutation) | **FOLD** | oskar save-as-new mutation + admin proposal (the global leg) + `/and-write revise` (the deliverable leg); ingrid coordinates |
| `parroting-tuning` / `subtraction-pass-tuning` / `pov-discipline-tuning` | **FOLD** | the *pattern* (harden a recurring prose failure into a mechanical gate) → admin process-proposal against the owning rubric + AP-SCAN promotion (Rule 11). Not ported as files; the and-shoot equivalent is the proposal/rubric system. |
| `vibe-tuning` | **DROP** | vibe cards are a brighid class; and-shoot uses substance vibe-clouds at series/book level, authored upstream. |
| `noise-packet-card` | **DROP** | Sable/creative-force-critic is brighid-specific. |
| `close-to-next-board` | **DROP** | board lifecycle; and-shoot uses `/and-stitch` Phase 10 forward-thread + aggregate-state. |
| `intake-to-gamemaster` | **DROP** | already superseded in brighid; no and-shoot analog. |
| `director-clone-merge` | **DROP** | naomi state merge; naomi not ported. |
| `naomi-intake-library-scan` | **DROP** | `/and-project` Phase 1c margit candidate-menu already covers intake card lookup. |
| `fandom-harvest` / `large-migration` | **FOLD** | margit harvest/migration capability already exists; on-demand, not cadence. |
| `gameboard-stress-test` | **DROP** | gameboard is brighid-specific. |
| `remote-workshop-improvement` | **FOLD** | `/and-tend` is itself the remote-improvement vehicle. |

---

## Schemas / plans ported

- `schemas/tournament-scorecard.schema.md` — already in and-shoot. Arbiter judge mode + `/and-forge` reuse it (no new scorecard schema).
- Feedback-routing / retake-attic / project-close-memo schemas — **FOLD**. and-shoot's parking-lot + process-proposals + showrunner-memory schemas cover the equivalent state; ingrid's memo lands as a plain report under `staff/ingrid/`.

## Deferred (NOT in this pass — flagged for principal)

- **Rewiring `/and-stitch` Phase 1.5 / Phase 3 tournament to dispatch `arbiter` instead of `general-purpose`.** This is a behavior change to a live chapter-production gate, not an import. The arbiter is ready and `/and-forge` uses it; adopting it inside the shipping stitch chain deserves its own validation run. Recommended next, flagged here.

---

## New artifacts created this pass

- `.claude/agents/arbiter.md`, `.claude/agents/artur.md`, `.claude/agents/ingrid.md`, `.claude/agents/oskar.md`
- `.claude/commands/and-forge.md`, `.claude/commands/and-tend.md`
- `staff/arbiter/{card,ltm,stm,rulings}.md`, `staff/artur/{card,ltm,stm}.md`, `staff/ingrid/{card,ltm,stm}.md`, `staff/oskar/{card,ltm,stm}.md`
- `staff/ingrid/tend-state.md` — the `/and-tend` work-queue + cadence ledger
- `CLAUDE.md` + `RUNBOOK.md` edits (routing table, commands table, new Rule 23, trigger map)
