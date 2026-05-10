---
queue: upstream-tuning
date: 2026-05-10
status: ACCRUING — items added as audit / tuning / facet runs surface upstream issues
purpose: collect upstream issues that cannot be fixed at line-level. Do NOT block downstream work; flag and continue.
---

# Upstream Tuning Queue

When facet-tuning or audit runs surface issues that require **upstream intervention** (rubric edits, protoline re-authoring, card authoring, agent-definition changes), they're flagged here rather than blocking the active work. The queue is processed as a separate session.

Categories:

1. **Rubric tuning** — locked rubric files (`design/shoot-v2/rubric-*.md`) need edits validated against tuning corpus.
2. **Protoline upstream** — `/and-protolines-v2` or `/and-season` produced output that doesn't carry the dramatic shape downstream facets need.
3. **Card authoring** — warehouse cards (props, monuments, conditions) referenced as free-text glosses need to be promoted to formal slugs.
4. **Agent definition** — agent permissions (e.g., dramatist Read-only) need adjustment.
5. **Schema** — schema text needs clarification or extension.
6. **Audit** — the audit command itself needs further coverage upgrades.

---

## Open queue items

### URI-001 — Memory rubric V2.1 carry-back (3 audience-confirmed)

- **Category:** Rubric tuning.
- **Source:** `design/shoot-v2/memory-tuning-r2-final.md` Phase 5 audience adjudication, 2026-05-10.
- **Items:**
  1. **Tens=2 zone-class scene-frame anchor.** The quiet-beat test cannot classify a tens=2 beat as rising-edge or trailing-edge without a mechanical scene-frame anchor. Currently relies on judgment. Need a quantified rule for episodes without dramatist-locked scene boundaries.
  2. **Mask-bleed vs clinical-of-the-horrible.** Anti-pattern §10 does not sharply separate somatic-fact registration from mask-bleed (voice-register performance). Rubric needs a positive carve-out definition.
  3. **AP §3a — analytical-frame primary-noun extension.** Anti-pattern §3 (stage-named-cue) covers act-of-remembering labels but not analytical-frame primary-nouns naming the cue's mechanism (map / apparatus / performance / system / mechanism). Extension warranted.
- **Action:** rubric edit + Phase-5 mechanic re-verify on s01e01 corpus + rubric-carry-back validation against next-episode tuning data.
- **Cost:** small. Rubric-only edit; no facet retune needed (lift was already audience-validated under V2).

### URI-002 — Protoline scene-peak coverage gap (s01e01)

- **Category:** Protoline upstream (`/and-protolines-v2` or `/and-season`).
- **Source:** `active-project/staff/auditor/facets-final-audit.md` audit-r3, 2026-05-10. CURVE-SHAPE verdict: SHAPE-FAIL.
- **Issue:** 6 of 8 scenes in s01e01 lack any rung-3 peak with no dramatist-flagged exception. Direct 1→3 jump at @83 with no rung-2 precursor at @81/@82. Episode-level act structure is sound (climax @99, not inverted); failure is scene-level coverage.
- **Where the gap originates:** the protoline file as authored does not carry enough peak-quality beats per scene. Either the scene boundaries need re-thinking (some "scenes" are transit/respite and should be flagged as scene-exceptions), or the protolines need additional charged beats added by screen-writer.
- **Action:** dramatist re-pass on s01e01 protolines with scene-exception authority (allow scenes to be flagged as transit/respite explicitly), OR screen-writer kickback to add peak beats. Update tens facet with re-rated beats. Re-run cite-index and audit.
- **Cost:** medium. Touches protolines + tens facet. Cascade implications for any facet citing affected protolines.
- **Frequency-band linkage:** the tens 1-rung breach-high (77.5% > 75%) and 3-rung breach-low (2.0% < 5%) trace to the same root cause. Resolving URI-002 likely resolves the FREQUENCY-BAND finding too.

### URI-003 — Margit referrals from R1 (cards to author)

- **Category:** Card authoring.
- **Source:** R1 facet authoring reports, 2026-05-10.
- **Items:**
  - Prop card: `oc-account-ledger` (used by env state-updates 4-6 via field-extensions on `prop:oc-account-ledger.{cover-state,entry-state,apprentice-mark}`).
  - Field-extension formalization on actor cards:
    - Taylor: `hair-state`, `public-role`.
    - Mother: `apprentice-ratification`, `relationship-role-toward-taylor`.
    - Father: `household-economic-tracking`, `role-as-master`, `ledger-authority-state`.
  - Memory monument cards (referenced as free-text glosses in memory.md mem:3, mem:4, mem:6, mem:7):
    - `monument-cape-reflex-trained-body` (or fold into `cond-shard-behavioral-weight` adjacency).
    - `monument-parent-as-cost-vector` / `monument-annette-pattern` (or fold into Annette monument card if authored).
    - `monument-child-performance-grooves`.
    - `monument-control-as-evidence`.
- **Action:** margit dispatch — promote field-extensions to formal state-schema entries; author missing prop/monument cards.
- **Cost:** medium. Per-card authoring + cross-reference updates.
- **AP-SCAN linkage:** AP14 free-text gloss findings (4 entries) clear once monument cards land.

### URI-004 — Audit: per-section monotonicity acceptance

- **Category:** Audit (the command itself).
- **Source:** audit-r3 STRUCTURAL finding on feeling.md ID non-monotonicity, 2026-05-10.
- **Issue:** audit-r3 flagged feeling.md as STRUCTURAL HARD violation because IDs run 1,2,3,4,13 (Taylor) | 5,6,7,14 (mother) | 9,10,11 (father) — not monotone top-to-bottom. But the schema only requires file-scoped monotonicity (no duplicates, no out-of-order WITHIN a logical sub-section). Per-character section grouping is intentional; the audit's STRUCTURAL check is over-strict.
- **Action:** update `.claude/commands/and-facets-audit.md` STRUCTURAL class to allow per-section monotonicity for facets that organize by sub-section (feeling per-character; state-updates env vs actor). Document the per-section convention.
- **Cost:** small. Command-file edit only.

### URI-005 — AP-SCAN remediation (5 candidates from audit-r3)

- **Category:** Per-facet author work; route to next facet-tuning round.
- **Source:** audit-r3 AP-SCAN class findings, 2026-05-10.
- **Items:**
  - AP5 stillness-inflation: tens:29 @34 (`Taylor holds the feet`) — dramatist re-rating.
  - AP7 persistent-narration: NI @23/@24 consecutive "had already read" — NI revision.
  - AP5/voice-fidelity: NI:23 @94 externalized-observer construction — NI revision.
  - AP8 prose-token: vibes:7 @15 token contains finite-verb construction — showrunner revision.
  - AP14 free-text gloss on 4 memory target-references — clears with URI-003.
- **Action:** route to next per-facet tuning round (NI is next in the queue). The AP7 + AP5/voice-fidelity items will be addressed when NI tuning runs.

### URI-006 — Auditor itself needs tuning (Step G design item)

- **Category:** Agent tuning.
- **Source:** Step G design (`design/shoot-v2/three-pass-alpha-design.md` § Final audit teeth). Audit currently runs flag-only because auditor is not yet tuned for delete-authority.
- **Action:** apply the same five-phase facet-tuning process (`design/shoot-v2/facet-tuning-process.md`) to the auditor. Corpus = the audit-r1/r2/r3 reports we have plus next-episode audits. Goal: tune the auditor's rubric + threshold + refusal discipline so deletes can be authorized.
- **Cost:** large. Multi-session tuning project.
- **Linkage:** this is the gating item for moving the audit from flag-only to delete-authoritative.

### URI-007 — /and-season rubric: idiom depletion as named fault class

- **Category:** Rubric tuning.
- **Source:** `design/shoot-v2/and-season-tuning-r1/H-carry-back.md` Item 1. C-seams U17 (worm + dark-fantasy STRONG), E-r2 U17 REVISE, auditor fault-AP-1 HARD.
- **Issue:** V1 has 3 partial mechanics (S3.5 5-instance threshold, S5 first-to-last voice, S6 live carry-forward) but no formalism for idiom-depletion-through-overuse as distinct from drift-through-inconsistency or state-verb deny-list violation. `holds the feet` 18+ instances on s01; full physical-stasis cluster 60+. Schema's narrow-license `holds` exemption is satisfied per-instance but cumulative pattern flattens cost-register.
- **Action:** rubric edit + schema reconciliation (does narrow-license `holds` extend to depletion-at-scale?) + 20-named-instance validation on s01 corpus + screen-writer regeneration deferred to separate session.
- **Cost:** medium. Candidate mechanic drafted in H-carry-back.

### URI-008 — /and-season rubric: denouement-share quantification

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 2. C-seams U1, E-r2 U1 REVISE.
- **Issue:** S2 names "back half of the aggregate" for climax position but no max denouement share. s01 denouement at 43% triggered audience attack; rubric had no V1 answer.
- **Action:** rubric clause edit. Candidate: `LATE-WEIGHT` flag if denouement >40% of aggregate; tone-law-licensed exception when season-plan explicitly designates the post-peak arc as cost-bearing.
- **Cost:** small. Clause-only edit.

### URI-009 — /and-season rubric: narrator-field rule for interlude episodes

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 3. B-baseline Gap 8 (corrected per auditor signal-006: e05 is compliant; only e06 is anomalous), auditor fault-005 HARD.
- **Issue:** Phase 4 Step 3 spec says `narrator:` is dominant POV by line count; s01e06 names interlude POV (Elara) against dominant Taylor (~122 vs ~86). Spec ambiguity.
- **Action:** rubric verdict — Option A (interlude-POV-wins clause) or Option B (literal dominant-line-count rule). H-carry-back recommends adjudication path. **Blocks fault-005 closure.**
- **Cost:** small. Clause edit + at most one per-episode header + memory.md correction (Option B path only).

### URI-010 — Schema clarification: aggregate non-monotonic IDs

- **Category:** Schema.
- **Source:** H-carry-back Item 4. Auditor fault-001 HARD (NEW); requires human escalation.
- **Issue:** s01 aggregate contains 21 900-range IDs interspersed in e01-range content. Schema "stable IDs / re-ordering preserves IDs" rule is in tension with "monotonic positive integer, file-scoped" rule when bones get reordered. Fixer formula `aggregate_id = aggregate_range_start + episode_id - 1` mis-maps for any episode covering the out-of-order region.
- **Action:** schema decision — Option A (stable-overrides-monotonic; legal survivors; fixer formula must be position-aware) or Option B (monotonic-overrides-stable; reorder triggers renumbering pass). Human reviewer to check pass-2/pass-3 reorder history.
- **Cost:** small for schema edit; medium for s01 corpus impact (Option B requires renumbering).
- **Blocks:** fixer routing for any s01e01 bone in the non-monotonic region. Human escalation gating.

### URI-011 — /and-season rubric: episode-shape mechanics for Phase 4 Step 2

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 5. B-baseline Gaps 1+3, C-seams Axis 2 + Axis 4 (9 of 12 STRONG seams pressured one of these).
- **Issue:** Phase 4 Step 2 names verdicts (`OPEN-ENGAGES`, `CLOSE-EARNS-NEXT`, `SHAPE-COHERENT`) without mechanics for testing them. Audience surfaced specific candidate close-points; rubric gave them no triage.
- **Action:** rubric edit — three candidate sub-mechanics drafted (5a OPEN-ENGAGES test, 5b CLOSE-EARNS-NEXT test, 5c SHAPE-COHERENT test). Validate against s01e01–e06.
- **Cost:** medium. Three new clauses + 6-episode validation.

### URI-012 — /and-season rubric: post-split continuity pass (S4.5)

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 6. B-baseline Gap 2, C-seams Axis 3 (5 of 5 boundary continuity units returned STRONG/MODERATE).
- **Issue:** S4 covers within-aggregate continuity; nothing checks the split's effect on continuity across post-split episode boundaries.
- **Action:** new rubric pass S4.5. Per-boundary verdict: `BOUNDARY-CARRIES` or `BOUNDARY-DROPS-{state}`. File-level: `POST-SPLIT-CONTINUITY-OK` or `POST-SPLIT-CONTINUITY-FAIL-{boundary-list}`.
- **Cost:** medium. New pass + 5-boundary validation on s01 + integration into /and-season command.

### URI-013 — /and-season rubric: S3 vs S9 entertainment-density reconciliation

- **Category:** Rubric tuning (clarification).
- **Source:** H-carry-back Item 7. B-baseline Gap 6.
- **Issue:** S3 caps at ~10% TOLERATED + zero BORED; S9 caps at ≥30% B-or-T in 100-line stretch. Two non-aligned thresholds; on s01 S3 reached ACCEPT but S9 still triggered.
- **Action:** rubric clarification — recommended Option A (explicit different purposes: S3 = entertainment cap; S9 = attention floor; non-aligned verdicts both valid).
- **Cost:** small. Clause clarification only.

### URI-014 — /and-season + card schema: season-scope adversarial criteria per persona

- **Category:** Schema (per-persona card sections).
- **Source:** H-carry-back Item 8. B-baseline Gap 7.
- **Issue:** Per-line and per-episode adversarial habits implicit in persona cards; season-scope adversarial habits not separately documented. Phase C subagent had to derive them.
- **Action:** add `season-scope-adversarial` section to `class: persona` cards under `schemas/card.schema.md`. 3–5 named attack categories per persona. Candidate categories drafted in H-carry-back.
- **Cost:** small. Schema edit + per-active-persona card update.

### URI-015 — /and-season rubric: S6 vibe-drift resolution path

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 9. B-baseline Gap 4. Observed in s01 (S6 r1 fired 2-of-3 drift; resolution was carry-forward without re-pass).
- **Issue:** Rubric says "≥2-persona threshold for accepting drift flags" but does not specify resolution path. Carry-forward used by default; not always rubric-permitted.
- **Action:** rubric clause edit — localizable drift routes to screen-writer for stretch regeneration; non-localizable drift routes to season-scope screen-writer pass OR Phase H carry-back; carry-forward only when season-plan acknowledges the pattern.
- **Cost:** small. Clause edit only.

### URI-016 — /and-season rubric: S8a/S8b split-verdict adjudication

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 10. B-baseline Gap 5. Observed in s01 (S8a IMPLAUSIBLE on Elara visit; S8b PLAUSIBLE on same beat).
- **Issue:** When character (S8a) and event (S8b) lenses disagree on the same beat, rubric does not describe what to do. Reader does not compute lens-by-lens.
- **Action:** rubric clause edit — divergence triggers `S8-SPLIT-VERDICT-{slug}-{beat}` flag; more restrictive verdict wins by default; condition-card override converts to `S8-LICENSED-DIVERGENCE-{card-slug}`.
- **Cost:** small. Clause edit only.

---

## How items leave the queue

An item is closed when:
- **Rubric tuning** — rubric-version-bumped, validated on next-episode corpus, rubric-carry-back-deltas captured.
- **Protoline upstream** — re-pass produced new protolines, downstream facets re-run, new audit clean on the affected scope.
- **Card authoring** — margit promoted the card, INDEX.md updated, downstream references updated.
- **Agent definition** — agent permissions changed (out of scope for this codebase; would require Anthropic-side change).
- **Schema** — schema-version-bumped, downstream consumers updated.
- **Audit** — command-file edit landed, next audit run validates.

Items are **never silently abandoned**. If the team decides a queued item is no longer needed, the queue entry is updated to status `ABANDONED — <reason>` and stays for trace.
