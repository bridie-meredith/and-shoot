# /and-project process change recommendations

Notes saved 2026-05-17 during the taylor-hebert-westeros run on branch `claude/test-writing-process-L8Ge7`.
Not blocking; not actioned this session. Capture for future protocol revision.

---

## 1. Per-OQ vs batched OQ resolution

**Observation.** Phase 1b says "For each OQ in dependency order" but the 18 OQs on this run clustered into 5 tightly-coupled groups (setup-state / political-placement / plot-spine / cost-and-close / presentational-layer). Running them per-OQ would have meant ~54 fork dispatches (18 × screen-writer + dramatist + audience). I batched to 5 rounds = ~15 dispatches.

**Cost of the deviation.** The `1b-log.md` audit trail is per-batch, not per-OQ. Recovering "what argued for what" on a single parameter requires reading the batch's full transcript.

**Recommendation.** Either (a) update the protocol to permit explicit batching with named dependency-clusters, or (b) keep per-OQ as default but admit "if OQ N depends on OQ N–1 and resolves identically across all candidate answers, fold into the same dispatch." The implicit pressure under the current protocol is to be honest about the batching anyway, which means the protocol's strict reading is already not what the runs do.

---

## 2. Series-vibe-cloud / actor-vibes ordering bug

**Observation.** Phase 1c step 6 says "populate actor vibes from the series vibe-cloud." The series vibe-cloud is built later, at the Series Plan step 1. On this run I used `world-notes.md` tonal constraints as a stand-in.

**Recommendation.** Move "build series vibe-cloud" to the end of 1d (after world-laws are stable, before cast-vibes need to read it) — OR move "populate cast vibes" to the start of Series Plan (after the cloud exists). Either fixes the circular dependency. The first option is structurally cleaner: the cloud is derivable from world-notes alone.

---

## 3. Reviewer-disagreement tie-breaking

**Observation.** Audience uses 2-of-3 internally. Cross-agent (audience triad vs dramatist) is not specified. Hit this twice on this run:
- Batch E: audience Bundle 2 (3-of-3) / dramatist Bundle 1 — resolved on convergent re-reading (the dramatist's caveat was actually compatible with Bundle 2).
- Series Plan attempt 1: audience ACCEPT (3-of-3) / dramatist REVISE — resolved by routing through a revise loop on the dramatist's structural fault.

Both resolutions were ad-hoc. The pattern that emerged: **dramatist veto on structural faults; audience veto on taste/cohort fit**. The dramatist's domain is shape; the audience's is reception.

**Recommendation.** Codify the split: structural-fault findings from the dramatist override audience accept. Taste/register/cohort findings from the audience override dramatist accept. Where the dispute is over the same axis (both are taste calls, or both are structural), 2-of-3 across the four-agent set (audience triad + dramatist) wins.

---

## 4. Long subagent wall-clock

**Observation.** Margit authoring forks ran 15–25 minutes each. Three parallel margit forks (personas + locations + conditions) totaled ~25 min wall-clock dominated by the slowest. The whole /and-project run was ~80–90 min of actual wall-clock with most of it inside subagent forks.

**Recommendation.** This is acceptable for activation but worth noting: speculative "do more in parallel" optimizations on /and-project provide diminishing returns because the slowest-fork wall-clock dominates. The lever that would help most is reducing the **scope per fork** (more, smaller, faster forks) rather than parallelizing fewer large forks.

---

## 5. Shared-file race risk on parallel margit forks

**Observation.** Three parallel margit forks all wrote to `margit.memory.md`. They appended sequentially in this run with no conflict, but a real race could lose data.

**Recommendation.** Give each parallel fork a unique log path: `margit-personas.memory.md`, `margit-locations.memory.md`, `margit-conditions.memory.md`. Margit reconciles into the canonical `margit.memory.md` at a sync step. Or: prohibit shared-file writes inside any parallel margit fan-out.

---

## 6. Screen-writer self-review contamination

**Observation.** On series-plan attempt 1, the screen-writer dispatch returned its own embedded "audience review" and "dramatist review" sections inside its response — fabricating reviewer verdicts the actual reviewers had not given. I ignored that and dispatched the real reviewers.

**Recommendation.** Tighten the screen-writer card / dispatch wording to explicitly prohibit self-review or simulated reviewer output. The screen-writer is the author; reviewers are separate dispatches.

---

## 7. Audience triad 2-of-3 ACCEPT can hide substantive single-persona concerns

**Observation.** Pedant flagged Silverwing canon-claim arc as a lore-leak risk at series plan attempt 1. The 3-of-3 ACCEPT did not gate on it. I propagated the flag manually as a carry-forward.

**Recommendation.** Make audience output a structured carry-forward list separate from the triad-accept verdict. The orchestrator must process each persona's carry-forward as a required revision even when the triad accepts. (This is already done de facto on this run; the recommendation is to make it explicit in the protocol.)

---

## 8. Token-budget on large reference reads

**Observation.** `1c-candidate-menu.md` was 631 lines / ~25k tokens — exceeded a single Read call. Had to segment.

**Recommendation.** Candidate menus this large should be split into per-section files by margit (`1c-candidate-menu.personas.md`, `1c-candidate-menu.locations.md`, `1c-candidate-menu.conditions.md`) — already isomorphic to the three margit fan-out forks. Removes the segment-read overhead and aligns the menu structure with the parallel authoring forks.

---

## 9. Pre-existing artifacts from prior aborted runs

**Observation.** On this run, margit found `loc-flea-bottom-mirror` and `loc-velaryon-kl-townhouse` already present in the library before the location-authoring fork wrote them. Multiple fixer findings reported as "already resolved on read." Suggests an earlier /and-project pass on this concept space left partial artifacts.

**Recommendation.** Phase 1 step 2 ("shelve previous active-project") only shelves the active-project directory — it does not touch library cards authored during prior aborted runs that may have already been promoted to `cards/`. Add an optional "library check" step that flags cards in `cards/` whose mtimes match the prior aborted run's window, for human review before re-authoring. Low priority; mostly cosmetic.

---

## 10. Stop-hook git-check creates per-fork turn overhead

**Observation.** Repo's stop hook requires commit+push after every uncommitted change. Each subagent fork that writes files (which is most of them) triggers a hook → commit → push cycle. Adds 3–5 turns of overhead per phase outside the /and-project work itself.

**Recommendation.** Outside the scope of /and-project to fix. Note the cost. If the harness ever offers a "batch commits across a multi-fork phase" option, /and-project is a natural beneficiary.

---

## Summary

None of these are blockers. /and-project ran successfully on the protocol-as-written. The recommendations are tightenings that would reduce ambiguity at decision points (1, 3, 7), close a circular-dependency footgun (2), and remove a small contamination/race surface (5, 6).
