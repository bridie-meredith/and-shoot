# Run postmortem — harness behavior, first end-to-end through `b01c01`

**Date:** 2026-05-20
**Auditor:** harness-postmortem fork
**Scope:** /and-project → /and-series → /and-substance series/book/chapter → /and-cast → /and-write → /and-facets → /and-stitch for chapter `b01c01` of `taylor-hebert-westeros-good-intentions`
**Terminal artifact:** `/home/user/and-shoot/active-project/draft/b01-c01.md` (599 words, accepted with caveats)
**Headline verdict:** Chapter shipped, but `/and-facets` cap-burned (orchestrator-critic verdict: `NOT-SUCCESSFUL`). Pipeline accomplished the end-to-end traversal **only because the user accepted two rejected items and the human did manual surgery** to break a dependency knot the harness could not resolve.

---

## 1. Breakages — where commands halted, retried, or escalated

### B-1. `/and-stitch b01c01` HARD-ABORT at Phase 0.5 (commit `2b372ee`, 2026-05-19)
- Render-log: `/home/user/and-shoot/active-project/staff/stitcher/render-log-b01-c01.md`
- Root cause: a prior `/and-write b01c01 redo` (commit `b2e992b`) regenerated the bones file from 24→27 bones, shifting every flat anchor ID. The staleness-cascade marked downstream facets stale (`/home/user/and-shoot/active-project/staff/showrunner/staleness-log.md`), but the cascade is **surfacing-only**; nothing automatically refreshed facet anchors. The intervening `/and-facets` cycles authored content against rubrics, not against current bones IDs.
- Symptom on disk at stitch-time:
  - 3 of 4 dialogue speech bones bare (no utterance at @8, @23, @26).
  - Coll dialogue keyed to @3 when current @3 was Taylor's bone.
  - Wren dialogue at @22 when @22 was now `wren-enters`, not a speech bone.
  - @26 (new bone from redo) had no utterance authored at all.
  - Exposition entries 2/3/4/5 anchored at @3/@15/@20/@20 — none matched the now-current bone IDs where their referents first appeared (@4/@18/@22/@22).
- Resolution: user issued `/and-facets b01-c01` to re-author the *whole graph* against the new bones; this kicked off the second `/and-facets` traversal (commits `e25c2a3` onward).

### B-2. `/and-facets b01c01` Phase 5b cap-burn at cycle 3 — orchestrator-critic `NOT-SUCCESSFUL` (commit `0e09c24`)
- Summary report: `/home/user/and-shoot/active-project/staff/showrunner/and-facets-b01c01-summary.md`
- Audience-gate report: `/home/user/and-shoot/active-project/staff/auditor/facets-audience-gate-r3.md`
- 10/12 facets reached 3-of-3 ACCEPT. **`sensory` and `memory` did not** and could not within the 3-cycle cap.
- `memory` failure was structural: rubric mandates NI co-citation on every memory-flag entry, NI was silent at @9, and the three remediation paths all violated some other rubric — (a) add NI @9 → breaches 25% band ceiling; (b) delete mem:1 → SHAPE-FAIL single-Westerosi-register; (c) rubric authority ruling was declared out of scope.
- `sensory` failure was iatrogenic: cycle-3 *added* `sensory:3 @17` to satisfy modality floor; the add itself produced a new HARD on unanchored old-state. Cycle-N fixer add → cycle-N+1 audience surface; with cycle 3 = cap, no remediation slot remained.

### B-3. Phase 5b cycle counts (signal of high friction)
- Audience-gate ran **3 cycles** (cap-burn) across roughly **60 dispatches** (12 facets × 3 personas × ≤3 cycles).
- Final pass-count by facet (from the summary):
  - cycle-1 ACCEPT 3-of-3: `feeling`, `metaphor`, `vibes`, `exposition`, `dialogue-coll` (5/12)
  - cycle-2 ACCEPT 3-of-3: `location-state`, `state-updates`, `dialogue-taylor`, `dialogue-wren` (4/12)
  - cycle-3 ACCEPT 3-of-3: `interest-narrator` (1/12)
  - never reached 3-of-3: `sensory`, `memory` (2/12)
- Phase 5 (mechanical audit) also required **2 fixer iterations** before Phase 5b was even allowed to start.

### B-4. `/and-write b01c01` was re-run (`redo`, not `revise`) mid-flow
- The redo (`b2e992b`) reshaped bones 24→27 *after* a prior `/and-write` had emitted 24 bones (`a6a54c5`) and an entire `/and-facets` traversal had completed against those 24 bones (commits `374988b` through `eced5cf`).
- This is what stale-marked the entire facet graph (see `staleness-log.md` for the 17 stale-marks) and ultimately produced B-1.

### B-5. `/and-stitch` Phase 0 stale-cite degradation accepted silently
- The 2026-05-20 stitch run (`616b3d4`) shipped with stale cite-index entries for `sensory:2`, `sensory:3`, `mem:1` and noted them as "expected; excluded from scope per prior audit dispatch + rejected-items fixer." This is a stale graph being papered over with a comment rather than rebuilt.

---

## 2. Ad-hoc fixes — mid-run edits outside documented phase plans

### A-1. Pipeline-adaptation audit + 15-finding fix-pass (commits `3c2a0df`, `ac2b1cb`, `132fdf1`, `73e416e`, 2026-05-19)
The substance overhaul (commit `64ae3f8`) renamed/removed tensometer but **left stale tensometer language in five places that the live pipeline still reads**:
- `/home/user/and-shoot/schemas/facet.schema.md` — tensometer section read as live
- `/home/user/and-shoot/schemas/scene-map.schema.md` — full schema in pre-overhaul terms (fusion-eligible-runs defined as tensometer scalars)
- `/home/user/and-shoot/design/shoot-v2/rubric-memory-flags.md`, `rubric-sensory.md`, `rubric-state-updates.md`, `rubric-narrator-interest.md` — all loaded tensometer file
- `/home/user/and-shoot/.claude/commands/and-facets.md` Phase 5 / Phase 5b / Phase 6b — tensometer in read-inputs, gate table, summary count
- `/home/user/and-shoot/staff/orchestrator-critic/card.md` B6 — pointed at retired path `.claude/commands/and-facets-audit.md`

Discovered *while* `/and-facets b01c01` was running. Full audit at `/home/user/and-shoot/active-project/staff/auditor/pipeline-adaptation-audit.md` (15 HARD + 4 SIGNAL + 4 CONTRA). 18 separate fixer line-edits applied (fixer-log sessions `pipeline-adaptation-audit-fix` and `tensometer-translation-cleanup`). This was **schema / rubric / command-body surgery during a live authoring run.**

### A-2. New audit class `RUBRIC-FIDELITY` invented mid-run (commit `73e416e`)
Audience caught faults that the auditor missed (because rubrics' REJECT enumerations weren't class-checked). Solution introduced a brand-new audit class (#12) directly in `.claude/commands/and-facets.md` Phase 5 *during* the b01c01 run. This is the rule-11 "promotion path" being exercised for the first time — and it required editing the live command body.

### A-3. Seven RUBRIC-FIDELITY entries promoted from cycle-1 taste calls into rubrics (commit `29cc9a3`)
Cycle-1 audience taste calls were promoted into REJECT-section rubric rules across `rubric-location-state.md`, `rubric-narrator-interest.md`, `rubric-state-updates.md`, `rubric-sensory.md`, `rubric-memory-flags.md`, `rubric-exposition.md` *between* cycle-1 and cycle-2. Cycle-2 audience then re-checked against the promoted rules. The rubric promotion was done by hand, not by a documented command phase.

### A-4. Schema patch: rename `cond-khepri-residue-122ac` → `cond-override-architecture-residue-122ac` (commit `ffbb08f`, vibes.md C-002)
`vibes:17` keyword `khepri-residue` was a substring fence breach against `cond-earth-bet-noun-fence`. The warehouse slug was renamed mid-run; vibes.md keyword + licensed-by reference were patched. Not driven by a phase, but by a HARD audit finding.

### A-5. `F-006` rubric carve-out annotation (commit `e88777e`)
State-updates POV co-citation requirement applied to 8/9 entries; adding 8 NI entries would breach the band ceiling. Resolution: a hand-authored "rubric-carve-out" comment block inserted at the top of `state-updates.md` citing the rubric's own scoping language and exempting mechanical-action entries. **The carve-out narrowed a rubric mandate, but it lives as a file-local comment, not as a rubric edit.** Fixer-log notes the cite-index builder lacks `# pragma carve-out` preamble support and required manual top-of-file insertion plus a "do NOT rerun builder" instruction.

### A-6. User-directive removal of two cycle-3-rejected items post-cap-burn (commits `6497934`, `f62df36`)
After cap-burn, the user directed the fixer to **delete** `sensory:3 @17` and `mem:1 @9` rather than chase a fourth cycle or escalate for rubric authority ruling. Report: `/home/user/and-shoot/active-project/staff/fixer/and-facets-rejected-removal.md`. Documented tradeoffs:
- `sensory.md` is back to **one modality** (light only); rubric's 2-modality floor unmet.
- `memory.md` is single-Westerosi-register; the chapter's Khepri-residue substance-hinge at @9 carries no memory-monument.

Both deletions are **user-blessed losses**, not pipeline-resolved.

### A-7. `/and-stitch` Phase 0.5 dialogue-gate added mid-run? (verify)
The URI-DIALOGUE-COVERAGE-GATE that fired the HALT in B-1 was already in the stitch command, but the **first /and-facets traversal completed without it firing** because the bones file had not yet been redone. The HALT only manifested when the second traversal hit the gate. This is not strictly an ad-hoc fix, but it is a previously-unexercised gate.

### A-8. Cite-index hand-rebuild after each cap-burn deletion
Fixer-log entries 2026-05-19T10:01:00Z and 2026-05-20T13:10:00Z record manual cite-index edits (header counts, co-citation strips). The cite-index *builder* exists but reportedly cannot tolerate carve-out preambles, so the human kept the index consistent by hand.

---

## 3. Cap-burn / NOT-SUCCESSFUL exits — what actually happened

| Phase | Cap | Outcome | Disposition |
|---|---|---|---|
| `/and-write` Phase 2 (SVO audit) | n/a | 5 faults → 5 fixer recasts in one pass | accepted |
| `/and-write` Phase 5 (continuity) | n/a | 1 FAULT-STATE → 1 fixer fix | accepted |
| `/and-write` Phase 6 (substance bone-gate) | n/a | PASS | accepted |
| `/and-facets` Phase 5 (mechanical audit) | n/a | cycle-1 6 HARD → 2 fixer passes → cycle-3 CLEAN | accepted |
| `/and-facets` Phase 5b (audience-gate) | 3 cycles | **CAP-BURN** at cycle 3; 10/12 facets pass | **NOT-SUCCESSFUL** verdict shipped |
| `/and-stitch` Phase 0.5 (dialogue-gate) | n/a | HARD-ABORT → user re-ran `/and-facets` to recover | recovered out-of-band |
| `/and-stitch` Phase 8 finalize | n/a | PASS — but accepted stale-cite carveouts | shipped with caveats |

The cap-burn was **papered over** by user directive: the orchestrator-critic verdict remained `NOT-SUCCESSFUL` (per memory.md `orchestrator_critic_verdict: NOT-SUCCESSFUL`) but the rejected items were deleted by hand so the stitcher could proceed. Per critic card hot-button quoted in the cap-burn report, "Cap-burn is a NOT-SUCCESSFUL verdict, not a 'ship anyway' license." It was shipped anyway.

---

## 4. Systematic improvements — what will keep biting until fixed

### S-1. **Staleness cascade must enforce bones-anchor refresh on facets, not just stale-mark.** [BLOCKING]
- **Where:** `/home/user/and-shoot/.claude/commands/and-write.md` Phase 0/7 + `/home/user/and-shoot/design/substance/staleness-cascade.md` + `/home/user/and-shoot/.claude/commands/and-facets.md` Phase 0.
- The 2026-05-19 stitch HALT (B-1) happened because stale-marking is surfacing-only and `/and-facets` cycles 1-3 (on the redone bones) authored content **without first migrating anchors from the prior bones IDs**.
- Fix: `/and-facets` Phase 0 should HARD-ABORT (not warn) if `theater/bones/<book>-<chapter>.md` is newer than the existing facets and the facets contain anchor IDs not present in the current bones file. OR: `/and-write` `redo` must delete the downstream facets it stale-marks rather than leave them on disk.

### S-2. **Tensometer-removal landed only halfway in the substance overhaul.** [BLOCKING — must be done before next chapter]
- **Where:** confirmed fixed by commits `ac2b1cb`/`132fdf1`/`73e416e`, but the original substance-overhaul commit (`64ae3f8`) did not include the schema/rubric/command-body translation. **Next time an overhaul ships, the schema + rubric + command-body lockstep audit (the same one captured in `pipeline-adaptation-audit.md`) must run as part of the overhaul, not after the first chapter exposes the breakage.**
- Process artifact missing: there is no skill/checklist that says "after a vocabulary rename, sweep schemas + rubrics + commands + orchestrator-critic card + all rubric calibration anchors."

### S-3. **`/and-facets` Phase 5b cap=3 is unprovably-too-small AND has no graceful degradation.** [BLOCKING]
- **Where:** `/home/user/and-shoot/.claude/commands/and-facets.md` Phase 5b.
- Cap-burn produced `NOT-SUCCESSFUL` then the user deleted the offending entries and shipped. That means the cap is teaching the harness "if you can't fix it in 3 cycles, the user will delete content for you" — not the intended discipline. The orchestrator-critic verdict is `NOT-SUCCESSFUL` in memory but `stitched: true` proceeded anyway (memory.md b01c01 entry shows both).
- Fix options (pick one and codify):
  - (a) Cap-burn → automatic deletion of offending entries with logged tradeoffs (formalize what the user did manually).
  - (b) Cap-burn → automatic escalation for rubric-authority ruling (formalize a new mini-phase).
  - (c) Raise cap to 4 with the explicit rule "cycle-N fixer ADD operations must be audience-validated in cycle-N before re-audit" (closes the `sensory:3 cycle-3 add → cycle-4 verdict missing` gap named in summary process-gap #5).

### S-4. **Cycle-N fixer adds can introduce findings the same cycle's audit cannot catch.** [HIGH]
- **Where:** `/and-facets` Phase 5b iteration logic.
- `sensory:3 @17` was added by the cycle-3 fixer to clear modality-floor → introduced a new HARD on unanchored old-state → no slot to fix it. Named in `and-facets-b01c01-summary.md` as process-gap #5.
- Fix: each fixer add inside cycle N must be locally audience-tested before re-audit advances to cycle N+1; OR the rule should explicitly state "fixer may DELETE in the final cycle but may not ADD."

### S-5. **Cite-index builder cannot tolerate carve-out preambles.** [MED]
- **Where:** wherever the cite-index builder script lives + `state-updates.md` rubric-carve-out workflow.
- F-006 required a manual top-of-file insertion + a "do NOT rerun builder" instruction. Named in `and-facets-b01c01-summary.md` as process-gap #2.
- Fix: builder must skip lines matching `^# pragma carve-out` or `^# rubric-carve-out` preamble blocks.

### S-6. **Sparsity-band vs. modality-floor arithmetic collision in short chapters.** [MED]
- **Where:** `rubric-sensory.md` + `/and-facets` Phase 5 RUBRIC-FIDELITY checks.
- 27-bone chapter: 2-modality floor + 3-6% sparsity band ⇒ exactly 1–2 sensory entries permitted but ≥2 modalities required. Means at least one modality has zero entries. Named in `and-facets-b01c01-summary.md` as process-gap #3.
- Fix: rubric must either (a) drop the 2-modality floor for short chapters, (b) raise the sparsity ceiling, or (c) declare which modality is required as a function of dramatic_shape.

### S-7. **Memory-flag rubric has no carve-out for substance-interior-to-feeling beats.** [MED]
- **Where:** `/home/user/and-shoot/design/shoot-v2/rubric-memory-flags.md`.
- `mem:1 @9` was rejected by 3 reviewers across 2 cycles because the rubric mandates NI co-citation and no carve-out exists for feel-as-spine substitution. Named in `and-facets-b01c01-summary.md` as process-gap #4.
- Fix: add explicit feel-as-spine equivalence clause OR explicit rubric authority ruling escalation phase.

### S-8. **R2 stale-shard cross-session vulnerability.** [HIGH]
- **Where:** `/home/user/and-shoot/design/substance/rerun-protocol.md` + `/and-facets` Phase 3/4.
- The R2 shards from one session were re-used in a different session against changed R1 content; "the prior session R2 shards referenced different draft R1" per summary. Named in summary as process-gap #1.
- Fix: rerun-protocol Phase 0 must verify R2 shards against cite-index before Phase 3 is allowed to proceed.

### S-9. **`/and-write redo` policy: should it allow downstream facets to survive?** [HIGH]
- **Where:** `/home/user/and-shoot/.claude/commands/and-write.md` redo mode.
- Currently `redo` stale-marks downstream; everything else is up to the operator. This is what caused B-1 (the stitch HALT). If redo is destructive of bone IDs, it must be destructive of downstream artifacts too — not surfacing-only.

### S-10. **Cap-burn ship-anyway semantics need codifying.** [MED]
- **Where:** orchestrator-critic card + `/and-stitch` Phase 0.
- Currently `orchestrator_critic_verdict: NOT-SUCCESSFUL` coexists with `stitched: true`. Either the stitcher should refuse to proceed on `NOT-SUCCESSFUL` upstream, or the verdict semantics need updating to acknowledge "ship-with-caveats" is a valid terminal state.

### S-11. **Per-bone state-delta has no schema-enforced sanity check on direction=null vs target_delta_magnitude=0.** [LOW]
- Observed across b01c01: many bones have `direction: null, target_delta_magnitude: 0` for "dormancy enacted" or "stillness against pressure." Bone-gate PASS but reviewers consistently flagged these as risk-zone. No mechanical check that a sequence of all-null/0 bones still satisfies the chapter's `target_delta_magnitude`.

### S-12. **Schema audit was never run as a gate — only as a reactive fork.** [HIGH]
- `pipeline-adaptation-audit.md` is auditor-fork output, not a phase deliverable. There is no command that *would* surface STRUCT-001 through STRUCT-012 as a deliverable. It was only run because the human asked.
- Fix: `/and-review consistency` or new `/and-review pipeline` subcommand should run schema-vs-command-body-vs-rubric tri-walk and surface drift before any authoring command fires.

---

## 5. Things that worked but only because the human did them

1. **The pipeline-adaptation audit (commit `3c2a0df`).** Auditor fork was hand-dispatched mid-run after the b01c01 cycle-1 audience-gate failures pointed at stale tensometer references in rubrics. Without the human noticing the audience reviewers were referring to a "tensometer file this run does not have," none of STRUCT-001 through STRUCT-012 would have surfaced — and `/and-facets` would have continued to give the audience the wrong rubric. No command body would have caught this.

2. **The rejected-items removal (commit `6497934`).** User issued an explicit "delete rather than chase fourth cycle" directive. The fixer would not have done this autonomously — the spec is "cap-burn → NOT-SUCCESSFUL, user notified." The user resolved the cap-burn by **lossy deletion**, which is not in any command's phase plan.

3. **The rubric promotion (commit `29cc9a3`).** CLAUDE.md rule 11 names a promotion path from taste-call → RUBRIC-FIDELITY, but the human had to (a) identify which 7 cycle-1 taste calls were ready for promotion, (b) author the rubric REJECT sections, (c) decide between cycles. No command runs this promotion.

4. **The `/and-write redo` decision.** First `/and-write` produced 24 bones that passed Phase 6. A second `/and-write redo` rebuilt to 27 bones for reasons not captured in the fixer-log. The redo decision was operator judgement; the resulting cascade (B-1) was the consequence.

5. **The user accepted cap-burn caveats and proceeded to stitch.** Per critic card, this should have been a hard stop. Memory.md `b01c01.orchestrator_critic_verdict: NOT-SUCCESSFUL` coexists with `stitched: true`. The terminal deliverable exists because the user chose to ship; the harness would have stayed in cap-burn limbo.

6. **The schema/rubric drift fix (A-1) was applied mid-run with no rollback path.** If those edits had broken upstream content, there was no test to catch it; the b01c01 facet authoring continued to use the corrected rubrics, while every prior chapter (none exist yet) would have been authored against the stale rubrics. Pure luck that b01c01 was the first chapter to hit this.

7. **Cite-index hand-rebuild after every deletion.** The builder script exists but operators kept the index consistent by hand because the builder cannot handle carve-out preambles. Every cap-burn deletion ad-hoc was followed by a hand-edit to `_cite-index.md`.

---

## Recommended next-chapter pre-flight

Before `/and-substance chapter b01c02`:

1. **Codify rejected-items removal as a phase** (or refuse to ship). S-3 + S-10.
2. **Add S-1 anchor-refresh gate to `/and-facets` Phase 0** — block any traversal that would write against bones older than its facets.
3. **Run a fresh pipeline-adaptation audit** (S-12) — there may be more drift no one has noticed yet.
4. **Decide and document the cycle-N add policy** (S-4) — either ban late-cycle adds or reserve a final validation slot.
5. **Bring the cite-index builder up to the carve-out world** (S-5) so future cap-burns don't require hand-surgery.
6. **Resolve the memory-rubric feel-as-spine question** (S-7) — it will fire again the next time substance-hinge sits on feeling.

The harness reached the terminal artifact, but only by absorbing one user-directed deletion, one mid-run schema overhaul, one new audit class, seven rubric promotions, and a hand-rebuilt cite-index. **None of that scales to a 17-chapter book without systematic fixes to the command bodies and schemas above.**
