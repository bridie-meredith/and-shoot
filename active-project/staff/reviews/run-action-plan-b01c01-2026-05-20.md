# Action plan — first end-to-end run, `taylor-westeros-good-intentions / b01c01`

**Date:** 2026-05-20
**Status:** Chapter shipped. `/and-facets` capped-burned and was resolved by human surgery. The chain is alive but it does **not** scale to the next 17 chapters without 4-6 systematic fixes.
**Source postmortems (all in `active-project/staff/reviews/`):** `run-narrative-b01c01-`, `run-postmortem-harness-`, `run-postmortem-output-vs-intent-`, `run-postmortem-review-gating-` (all dated 2026-05-20).

---

## 1. Where we landed — by the numbers

```
PROJECT             taylor-westeros-good-intentions
BOOK                b01  (1 book, 18 chapters planned)
CHAPTER SHIPPED     b01c01  →  active-project/draft/b01-c01.md
                    599 words · 14 paragraphs (2 preamble + 12 body) · 22 sentences
                    3 scenes · 27 bones · 4 dialogue lines · single POV (Taylor)
                    Cast on stage: 3 of 8 (taylor + coll + wren)

SUBSTANCE DELTA     declared      measured      verdict
                    capability 0  capability 0   PASS
                    knowledge +0.5 knowledge +0.53  PASS

ORCHESTRATOR-CRITIC VERDICT     NOT-SUCCESSFUL  (cap-burn at /and-facets)
STITCH FELT VERDICT             PASS 3-of-3 across all 3 scene-windows
TERMINAL DELIVERABLE STATE      shipped with caveats; 4 surfaced faults rendered as-is
```

---

## 2. The chain, annotated

```
  ┌─────────────────┐
  │ /and-project    │  ✓ scaffolded, staff bound, world-notes seeded
  └────────┬────────┘    ⚠ world-notes.md:48-50 still names stripped Lucerys/Nessa
           │
  ┌────────▼────────┐
  │ /and-series     │  ✓ 6-path brainstorm, composed lens, 14-delta trajectory
  └────────┬────────┘    ⚠ 3 carry-forwards from series-log never executed
           │
  ┌────────▼────────┐
  │ /and-substance  │  ✓ 9 axes × 3 perspectives, 6-entry cost ledger,
  │  series         │    chunk_targets, per-book Δ
  └────────┬────────┘    ⚠ signature-draft.md carries wrong cost-ledger id
           │              (`cl-knowledge-contempt` vs canonical
           │              `cl-intelligence-arrangement`); SUPERSEDED notice mitigates
  ┌────────▼────────┐
  │ /and-cast       │  ✓ 8 actors provisioned, series-level human audit APPROVED
  └────────┬────────┘    (only blocking human checkpoint — timestamp 2026-05-18T123000Z)
           │
  ┌────────▼────────┐
  │ /and-substance  │  ✓ 18 chapter chunks, handoff_in/out, per-chapter Δ
  │  book b01       │    audience pass-2 ACCEPT 3-of-3
  └────────┬────────┘
           │
  ┌────────▼────────┐
  │ /and-substance  │  ✓ pov_narrator + dramatic_shape "hinge" + goal
  │  chapter b01c01 │    3 scenes with scene_conflict + density_target
  └────────┬────────┘    ⚠ SIGNAL-002 Khepri-naming carved to bone-smoothing
           │
  ┌────────▼────────┐
  │ /and-write      │  ⚠ RE-RUN (`redo`) mid-flow: bones 24 → 27
  │  b01c01         │    bone-gate PASS 27/27, every axis in band
  └────────┬────────┘    ⚠ audience bone-gate verdicts filed for s01+s02 only — s03 SKIPPED
           │
  ┌────────▼────────┐
  │ /and-facets     │  ⚠ Phase 5 mechanical: 6 HARD → all RESOLVED across 5 audit reports
  │  b01c01         │  ✗ Phase 5b adversarial: CAP-BURNED at cycle 3 — 10/12 facets passed
  └────────┬────────┘    sensory + memory FAILED → resolved by user-directive DELETION
           │              (sensory:3 @17 + mem:1 @9)
  ┌────────▼────────┐
  │ /and-stitch     │  ✗ first attempt: HARD-ABORT Phase 0.5 (stale dialogue anchors
  │  b01c01         │    from /and-write redo — bones IDs shifted, facets weren't refreshed)
  └─────────────────┘  ✓ second attempt after re-facet: 8 phases clean,
                         persona=neutral, profile=schema-default,
                         4 FAULT-AUDIT-MISS rendered as-is in annotated draft
```

Legend: `✓` ran clean · `⚠` ran with caveats · `✗` halted and required out-of-band recovery.

---

## 3. Internal review surfaces — verdict trail

| Surface | Fired? | Verdict | Real gate or rubber-stamp? |
|---|---|---|---|
| Series-level human audit (`/and-cast` Phase 5) | YES | APPROVED | **Real** — 2 HARD cleared pre-approval |
| Audience trio · signature | 2 passes | pass 1 single-fail forced full re-author | **Real** — one dissent rebuilt the signature |
| Audience trio · b01 book chunk | 2 passes | pass 1 REVISE×3 → pass 2 ACCEPT 3-of-3 | **Real** |
| Audience trio · b01c01 chapter chunk | 1 pass | SUBSTANCE-FELT 3-of-3 | Real |
| Audience trio · bones (Phase 6) | YES on s01+s02 | SUBSTANCE-FELT | **Coverage gap** — s03 never voted by trio |
| Dramatist (5 dispatches) | YES | every REVISE produced a real revision before ACCEPT | **Real** |
| Auditor · mechanical (bones + facets) | 5 reports | ~10 HARD raised, all RESOLVED before progression | **Real** |
| /and-write Phase 6 substance bone-gate | YES | PASS 27/27 | **Real** |
| /and-facets Phase 5b audience-gate | 3 cycles | **CAP-BURNED — 2/12 fail** | **Overridden by deletion** |
| Orchestrator-critic | inline only | NOT-SUCCESSFUL | **Recorded but not enforced** |
| `/and-review verdict b01` (formal) | NO | — | **Never dispatched** |

---

## 4. The audience-gate convergence — where the chain bled

12 facets, 3 personas each, 3 cycles cap. Cleared rows accumulate downward.

```
Facets passing 3-of-3 audience-gate

cycle 1 ████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  5 / 12   42%
                feeling · metaphor · vibes · exposition · dialogue-coll

cycle 2 ████████████████████████████████████░░░░░░░░░░░░  9 / 12   75%
        + location-state · state-updates · dialogue-taylor · dialogue-wren

cycle 3 ████████████████████████████████████████░░░░░░░░ 10 / 12   83%
        + interest-narrator

stuck   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  2 / 12   17%
        sensory  (cycle-3 ADD introduced new HARD that cycle-3 audit couldn't catch)
        memory   (feel-as-spine substitution rejected uniformly across cycles 1+2;
                  three remediation paths all blocked; rubric-authority ruling OOS)

Resolution      DELETE sensory:3 @17 + DELETE mem:1 @9  ← user directive after cap-burn
                cite-index hand-rebuilt to match
                orchestrator_critic_verdict = NOT-SUCCESSFUL retained in record
                stitched = true proceeded anyway
```

**This is the single most important number in the run.** The harness handled 10/12 within spec. The remaining 2/12 had no documented exit path other than "the human deletes the rejected items." Until that path is codified, every chapter will require human surgery at the same place.

---

## 5. What broke + how it was patched (ad-hoc inventory)

| # | Break | Where | Fix that was applied | Documented? |
|---|---|---|---|---|
| 1 | `/and-stitch` HARD-ABORT — bones 24→27 redo left facets pointing at dead anchors | stitch Phase 0.5 | full `/and-facets` re-traversal against new bones | no |
| 2 | `/and-facets` Phase 5b CAP-BURN on sensory + memory | facets cycle 3 | user directive: **delete** sensory:3 @17 and mem:1 @9 | yes (fixer/and-facets-rejected-removal.md) |
| 3 | Substance overhaul shipped half-done: tensometer refs stranded in schemas + 4 rubrics + and-facets command + orchestrator-critic card | 5 files, mid-run | pipeline-adaptation-audit + 18 fixer line-edits across commits `ac2b1cb` `132fdf1` `73e416e` | yes (pipeline-adaptation-audit.md) |
| 4 | Audience flagged faults auditor missed (no class) | mid-run | invented audit class **RUBRIC-FIDELITY** during the b01c01 run; edited live command body | yes (commit `73e416e`) |
| 5 | 7 cycle-1 taste calls had to be promoted into rubrics so cycle-2 could re-check | mid-run | hand-promoted 7 REJECT entries across 6 rubrics | yes (commit `29cc9a3`) |
| 6 | Slug `cond-khepri-residue-122ac` was substring-fence breach | warehouse + vibes:17 | hand-renamed to `cond-override-architecture-residue-122ac` | yes (commit `ffbb08f`) |
| 7 | State-updates POV co-citation rule would force 8 NI adds → breach band ceiling | F-006 | hand-authored carve-out comment block at top of `state-updates.md` | yes (commit `e88777e`) |
| 8 | Cite-index builder can't tolerate carve-out preambles | every cap-burn delete | rebuilt cite-index by hand each time | yes (fixer-log) |
| 9 | Audience bone-gate verdicts filed for s01+s02 only | /and-write Phase 6 | none — discovered post-hoc | no |
| 10 | `/and-write redo` is bone-id-destructive but only surfacing-only stale-marks downstream | staleness cascade | none in pipeline; human re-ran /and-facets | partial |

**Tally:** 1 mid-run schema overhaul · 1 new audit class invented · 7 hand-promoted rubric entries · 2 user-directive deletions · 1 hand-renamed slug · 1 file-local carve-out · multiple hand-rebuilds of the cite-index. **None of this scales.**

---

## 6. Fixer / auditor effort (the actual labor cost)

```
                  sessions  entries
fixer-log.md         20+      113   ← sessions named in the log

audit reports        ~12            ← 5 facets-final-audit reports + 5 write-phase
                                      audits + 1 series-audit + 1 pipeline-adaptation

audience dispatches  ~60            ← 12 facets × ≤3 personas × ≤3 cycles
                                      (Phase 5b alone)

dramatist dispatches  5             ← 1b, cast, signature×2, b01 plan, b01c01 chapter
                                      every REVISE produced a real revision
```

Findings raised across the run, by class:

```
HARD CONSTRAINT      ████████████████  ~12  all RESOLVED
HARD RUBRIC-FIDELITY ████████░░░░░░░░   ~6  invented mid-run; all RESOLVED
HARD AP-SCAN         █░░░░░░░░░░░░░░░    1  NI template saturation; RESOLVED
SUBSTANCE-FLAT       ░░░░░░░░░░░░░░░░    0  never triggered
SUBSTANCE-SUSPECT    █░░░░░░░░░░░░░░░    1  worm-canon-pedant on signature pass 1 (RESOLVED)
FAULT-AUDIT-MISS     ███░░░░░░░░░░░░░    4  surfaced as-is in stitch annotated draft
SIGNAL (carry-fwd)   ████████████████░░ ~20  per spec; no block
```

---

## 7. Action plan — priority-ranked

Each item carries (priority · effort · where to fix · which postmortem flagged it).

### BLOCKING — must land before `/and-substance chapter b01c02`

**A1. Anchor-refresh gate at `/and-facets` Phase 0.** [P0 · M effort]
Single biggest one. After any `/and-write redo`, `/and-facets` Phase 0 must HARD-ABORT (not warn) if `theater/bones/<book>-<chapter>.md` is newer than the facets and the facets contain anchor IDs not present in current bones. Or: `/and-write redo` must delete downstream facets it stale-marks rather than leave them on disk.
→ Edit: `.claude/commands/and-facets.md` Phase 0 + `design/substance/staleness-cascade.md`.
→ From: harness S-1 + S-9 + output-vs-intent §9 + gating §0.

**A2. Codify cap-burn ship-anyway semantics.** [P0 · S effort]
Currently `orchestrator_critic_verdict: NOT-SUCCESSFUL` coexists with `stitched: true`. Pick one and write it down:
- (a) cap-burn → automatic deletion of offending entries with logged tradeoffs (formalize what the user did);
- (b) cap-burn → automatic rubric-authority-ruling mini-phase;
- (c) cap-burn → hard stop, `/and-stitch` refuses.
→ Edit: `.claude/commands/and-facets.md` Phase 5b + `staff/orchestrator-critic/card.md`.
→ From: harness S-3 + S-10 + output-vs-intent §8 + gating §6.

**A3. Ban cycle-N fixer ADD operations (or audience-validate them in-cycle).** [P0 · S effort]
Cycle-3 fixer added `sensory:3 @17` to clear modality floor → introduced new HARD on unanchored old-state → no slot to fix it → cap-burn. Either ban ADD in the final cycle (DELETE-only), or each fixer ADD inside cycle N must be locally audience-tested before re-audit advances.
→ Edit: `.claude/commands/and-facets.md` Phase 5b iteration logic.
→ From: harness S-4 + gating §6.

**A4. Run a fresh pipeline-adaptation audit before c02.** [P0 · S effort]
The substance overhaul commit (`64ae3f8`) left 15 HARD findings stranded. Three commits' worth of mid-run surgery cleaned the worst of it, but there is no command that *would* surface STRUCT-001 through STRUCT-012 as a deliverable — it was found by hand. Run it once more before c02 to flush remnants, then promote to a `/and-review pipeline` subcommand.
→ Edit (later): `.claude/commands/and-review.md` to add `pipeline` subcommand.
→ From: harness S-2 + S-12.

### HIGH — needed within the next 2-3 chapters

**A5. Cite-index builder must tolerate carve-out preambles.** [P1 · S effort]
Builder skips lines matching `^# pragma carve-out` or `^# rubric-carve-out`. Removes the hand-rebuild loop after every cap-burn deletion.
→ Edit: cite-index builder script.
→ From: harness S-5 + A-8.

**A6. R2 stale-shard verification at `/and-facets` Phase 3.** [P1 · S effort]
The R2 shards from one session were re-used in a different session against changed R1 content. Rerun-protocol Phase 0 must verify R2 shards against cite-index before Phase 3 proceeds.
→ Edit: `design/substance/rerun-protocol.md` + `.claude/commands/and-facets.md` Phase 3.
→ From: harness S-8 + summary process-gap #1.

**A7. Resolve memory rubric feel-as-spine question.** [P1 · S effort]
`mem:1 @9` would have failed indefinitely without the deletion. The substance-hinge in this chapter lives in feeling, not memory; rubric mandates NI co-citation with no carve-out. Add explicit feel-as-spine equivalence clause OR formalize rubric-authority-ruling escalation phase.
→ Edit: `design/shoot-v2/rubric-memory-flags.md`.
→ From: harness S-7 + gating §6.

**A8. Resolve sparsity-band vs. modality-floor collision for short chapters.** [P1 · S effort]
27 bones + 2-modality floor + 3-6% sparsity band → 1-2 sensory entries permitted but ≥2 modalities required. Either drop modality floor for short chapters, raise sparsity ceiling, or make required modality a function of dramatic_shape.
→ Edit: `design/shoot-v2/rubric-sensory.md`.
→ From: harness S-6.

**A9. Patch the bone-gate audience to cover all scenes.** [P1 · S effort]
s03 was never voted by the audience trio in their bone-gate files; only the auditor covered it. Either require per-scene audience verdict files or aggregate into a single multi-scene verdict file with explicit per-scene blocks.
→ Edit: `.claude/commands/and-write.md` Phase 6.
→ From: gating §2e + §8 anomaly 1.

### MEDIUM — should be done before book completes

**A10. Schema-vs-command-body-vs-rubric tri-walk (`/and-review pipeline`).** [P2 · M effort]
Promote A4 into a formal subcommand. Catches the next vocabulary rename's residue automatically.
→ Edit: `.claude/commands/and-review.md`.
→ From: harness S-12.

**A11. Prune persist-time intermediates.** [P2 · XS effort]
`signature-draft.md` (384 lines) and `b01-draft.md` (1057 lines) are working files left in `staff/showrunner/` after the substance command persisted to memory. SUPERSEDED notice mitigates risk but they are noise. Either delete on persist or move to a `_drafts/` subdir.
→ Edit: `.claude/commands/and-substance.md` persist phase.
→ From: output-vs-intent §3, §5.

**A12. Clean stale upstream references** (`world-notes.md:48-50` Lucerys/Nessa). [P2 · XS]
Was flagged by `/and-series` for upstream cleanup, never executed.
→ Edit: file by hand or `/and-project revise`.
→ From: output-vs-intent §1, §2.

**A13. Formal `/and-review verdict b01` once 2+ chapters exist.** [P2 · S effort]
Inline orchestrator-critic at chapter granularity worked. The book-level subcommand has not yet been load-tested. Run it as soon as b01c02 ships.
→ Edit: none; dispatch the existing command.
→ From: gating §7 + §8 anomaly 3.

### LOW — quality of life

**A14. Inline `# rubric-carve-out` schema support in `schemas/facet.schema.md`.** [P3 · XS]
F-006 documented its carve-out as a file-local comment block. Promote to a schema-supported form so multiple files can use it cleanly.
→ From: harness A-5.

**A15. Per-bone state-delta sanity check on `direction=null + magnitude=0` runs.** [P3 · S]
Many b01c01 bones have null/0 deltas (dormancy enacted). Bone-gate PASS but reviewers consistently flagged risk-zone. Add a mechanical check that an all-null sequence still satisfies the chapter target.
→ From: harness S-11.

**A16. Tune a project-scoped `stitch-profile.md` + persona card.** [P3 · M]
`/and-stitch` ran with schema-default profile and `neutral` persona. The command's own Phase 0 calls this the canonical failure mode, though it's consistent with the polish-deferred boundary. Tuning is unused work; revisit when polish is undeferred.
→ From: output-vs-intent §9.

---

## 8. Pre-flight checklist for `/and-substance chapter b01c02`

Before the next chapter authors a single bone, the following should be true:

```
[ ] A1  anchor-refresh gate at /and-facets Phase 0 (HARD-ABORT, not warn)
[ ] A2  cap-burn semantics codified (pick a, b, or c — write it down)
[ ] A3  cycle-N fixer ADD policy decided and codified
[ ] A4  pipeline-adaptation audit run again (manual is fine; catch tensometer remnants)
[ ] A5  cite-index builder handles carve-out preambles
[ ] A7  memory feel-as-spine question resolved (rubric edit OR escalation phase)
[ ] A9  bone-gate audience covers all scenes in c02 (no s03-style skips)
[ ] A12 world-notes.md Lucerys/Nessa references cleaned up
```

Everything else (A6, A8, A10, A11, A13-A16) can land asynchronously across the next 2-3 chapters.

---

## 9. The honest summary

The chapter shipped. It is well-formed prose; the substance contract held; the felt verdict was PASS 3-of-3 at stitch. What is true is that we proved the substance-driven chunking idea works — **knowledge moved +0.53 against a target of +0.5, capability held at 0 against a target of 0**, and the bones-first gate caught zero substance-flat findings across 27 bones.

What is also true is that **the harness reached the terminal artifact only because the user accepted one cap-burn-by-deletion, one mid-run schema overhaul, one new audit class, seven rubric promotions, one hand-renamed slug, and a hand-rebuilt cite-index after each surgery.** Eight items above (A1, A2, A3, A4, A5, A7, A9, A12) need to land before c02 or the same surgery repeats — and 17 more chapters means the same surgery repeats 17 more times.

The good news is the gate stack mostly *worked*: every dramatist REVISE produced a real revision, every HARD constraint was cleared by fixer, the series-level human audit functioned cleanly, and the orchestrator-critic correctly held NOT-SUCCESSFUL even when the deliverable shipped anyway. The system tells you when something is wrong; it just doesn't yet know how to resolve all the wrong things without you.

**Next step:** pick the four BLOCKING items, decide each, edit the four files. Then `/and-substance chapter b01c02` and see whether the next chapter goes the same way or cleaner.
