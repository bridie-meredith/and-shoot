# Run Postmortem — Review Gating, First End-to-End Run Through b01c01
date: 2026-05-20
scope: every review surface fired during the first end-to-end pass from `/and-project` through `/and-stitch b01-c01`
project: taylor-hebert-westeros-good-intentions

---

## 0. Surfaces audited

| Surface | Fired? | Pass at terminal? |
|---|---|---|
| Series-level human audit (`/and-cast` Phase 5) | YES | APPROVED |
| Audience trio — series chunk | YES (Phase 1d, pre-overhaul, archived) | ACCEPT 3-of-3 |
| Audience trio — signature + b01 chunk | YES (2 passes, single-card override) | 3-of-3 SUBSTANCE-FELT / ACCEPT |
| Audience trio — b01 book chunks | YES (2 passes) | REVISE → ACCEPT 3-of-3 |
| Audience trio — b01c01 chapter chunk | YES (1 pass) | SUBSTANCE-FELT 3-of-3 |
| Audience trio — b01c01 bones (Phase 6 audience read) | YES | SUBSTANCE-FELT 3-of-3 across s01/s02 (s03 not separately voted) |
| Audience-gate — b01c01 facets (Phase 5b adversarial) | YES (3 cycles) | **CAP-BURNED — 10/12 pass, 2 FAIL** |
| Dramatist | YES at 1b, cast (Phase 3), signature (2 passes), b01 plan, b01c01 chapter | All ACCEPT (after revise) |
| Auditor — signature | YES (2 passes) | PASS pass 2 |
| Auditor — b01 plan | YES (2 passes) | PASS pass 2 |
| Auditor — b01c01 chapter chunk | YES | HARD-block (density mismatch) → PASS post-fixer |
| Auditor — /and-write Phase 2 SVO | YES | FAULTS-3 → fixer → PASS |
| Auditor — /and-write Phase 5 continuity | YES | CONTINUITY-OK |
| Auditor — /and-write Phase 6 bone-gate | YES | PASS (27/27 bones bonefide) |
| Auditor — facets mechanical (r1, r2, r3, cycle2, cycle3-closure) | YES (5 reports) | CLEAN at r3 / cycle3-closure |
| Fixer | YES (~20 sessions, ~80 individual fault resolutions) | All RESOLVED or SKIPPED-by-design |
| Orchestrator-critic (`/and-review verdict`) | NO formal `/and-review verdict` dispatch. Inline orchestrator-critic verdict embedded in facets-audience-gate-r3.md + and-facets-b01c01-summary.md | **NOT-SUCCESSFUL** (cap-burn) |

Files referenced throughout this report live under `/home/user/and-shoot/active-project/staff/reviews/`, `/home/user/and-shoot/active-project/staff/auditor/`, `/home/user/and-shoot/active-project/staff/fixer/`, and `/home/user/and-shoot/active-project/audience/`.

---

## 1. Series-level human audit checkpoint (the only blocking human gate)

**Fired:** YES. Report at `/home/user/and-shoot/active-project/staff/reviews/series-audit-2026-05-18T120000Z.md`. Findings: 2 HARD, 4 SIGNAL, 3 TASTE, plus 15 PASS cross-checks (cast roster integrity, antagonist coverage, F&B canon, end-place hard fence honored, etc.).

**Human verdict:** APPROVED. `/home/user/and-shoot/active-project/staff/showrunner/memory.md` lines 32–36:

```
series_audit:
  approved_at: 2026-05-18T123000Z
  approved_by: user
  report_path: active-project/staff/reviews/series-audit-2026-05-18T120000Z.md
  stale_since: ~
```

Timestamped and recorded in showrunner memory per the substance framework. The 2 HARD findings (cond-road-to-hell-chain-shape Nessa→Wren rename + Aemond age contradiction) were resolved by fixer pre-approval (`fixer-log.md` SESSION 2026-05-18T12:30:00Z — `fault-001`, `fault-002`, `fault-005`, `fault-006`). All four pre-approval faults: RESOLVED. Approval is clean and matches the substance framework requirement.

**Anomaly:** None at this checkpoint. The blocking human gate functioned as designed.

---

## 2. Audience trio reviews per chunk level

Trio: `cape-fic-reader`, `dark-fantasy-reader`, `worm-canon-pedant`.

### 2a. Series chunk
Pre-overhaul (Phase 1d). Two attempts: attempt 1 REVISE (dramatist returned REVISE — missing recognition beat at s03); attempt 2 ACCEPT 3-of-3 with all carry-forwards satisfied. Trail under `active-project/staff/showrunner/1b-audience-review.md` + git log entries `f7f6f35`, `36ffcfd`, `68ec455` (PASS-WITH-NOTES with 2 SOFT dismissals).

### 2b. Signature (`/and-substance series`)
Two passes — all per-reviewer files at `active-project/staff/reviews/series-signature-review-{persona}-{date}.md`.

| Reviewer | Pass 1 | Pass 2 |
|---|---|---|
| cape-fic-reader | SUBSTANCE-FELT | SUBSTANCE-FELT |
| dark-fantasy-reader | SUBSTANCE-FELT | SUBSTANCE-FELT |
| worm-canon-pedant | SUBSTANCE-SUSPECT-cheap-gain-capability + SUBSTANCE-SUSPECT-cheap-gain-moral-framework | accept |

Pass 1 single-fail forced full re-author (capability "Khepri-in-miniature" framing replaced with surveillance/unconsented-instrumentalization; d03 single-beat accept replaced with two-beat refuse-then-accept). Pass 2 cleared 3-of-3 SUBSTANCE-FELT. **Gate functioned: a single dissenting reviewer changed the signature.**

### 2c. b01 book chunk
Two passes. Pass 1 verdict file `substance-b01-audience-2026-05-18.md`: REVISE / REVISE / REVISE (per-reviewer). HARDs forced revision. Pass 2 (`substance-b01-audience-pass2-2026-05-18.md`): ACCEPT 3-of-3. **Both HARDs RESOLVED at 3-of-3.**

### 2d. b01c01 chapter chunk
Single pass. `substance-b01c01-audience-2026-05-18.md`: SUBSTANCE-FELT / SUBSTANCE-FELT / SUBSTANCE-FELT — aggregated 3-of-3 ACCEPT.

### 2e. Bones (Phase 6 audience read inside `/and-write`)
Each persona authored a `write-b01c01-bone-gate.md` in their working dir (`active-project/audience/{persona}/write-b01c01-bone-gate.md`). All three rendered SUBSTANCE-FELT for both s01 and s02. **s03 was not separately voted by any of the three audience cards in their bone-gate files** — only the auditor's substance bone-gate report covers s03. Treat as a coverage gap, not a fail.

### 2f. Facets (Phase 5b)
See §6.

**Anomaly across audience trio:** Bone-gate audience reads do not cover s03 in the active-audience persona files. The auditor's bone-gate report covers all 27 bones; the audience verdict files cover only s01–s02. The trio rubber-stamped bones in aggregate without explicit s03 verdicts.

---

## 3. Dramatist structural reviews

Dramatist fired at five levels. All ACCEPT verdicts after revise (no carve-out overrides).

| Dispatch | File | Verdict |
|---|---|---|
| `/and-project` Phase 1b | `active-project/staff/showrunner/1b-dramatist-review.md` | ACCEPT with carry-forwards |
| Cast composition (`/and-cast` Phase 3) | `active-project/staff/showrunner/cast-dramatist-review.md` | REVISE-WITH-FLAGS (5 flags) |
| Signature pass 1 | `series-signature-review-dramatist-20260517.md` | REVISE (5 structural issues; 2 schema-contradictions) |
| Signature pass 2 | `series-signature-review-dramatist-20260517-pass2.md` | ACCEPT |
| b01 plan (Phase 5) | `substance-b01-dramatist-2026-05-18.md` | shape verdict rise-peak-fall — ACCEPT |
| b01c01 chapter | `substance-b01c01-dramatist-2026-05-18.md` | ACCEPT (across 9 checks; `hinge` shape accepted as legitimate project-specific designation) |

**Anomalies:** None at the dramatist surface. Every REVISE produced an actual revision before ACCEPT. The b01c01 dramatist explicitly accepted a non-standard `hinge` shape — that's a carve-out, but it is escalation-recorded as a TASTE-FLAG by the auditor for AP-SCAN promotion if it recurs (`substance-b01c01-audit-2026-05-18.md` finding-004). Not a silent override.

---

## 4. Auditor + fixer loop

### Audits run on b01c01 bones (`/and-write`)
1. **Phase 2 (constraint audit, SVO form):** `write-b01c01-pass2.md` — FAULTS-3 (FAULT-FORM-MODIFIER × 3: `pulls the net taut`, `draws the needle through the mesh`, `sets the net aside`). All three substance deltas preserved; fixer corrected SVO form.
2. **Phase 5 (continuity audit):** `write-b01c01-pass5.md` — CONTINUITY-OK (all 6 classes pass: reachability / state / reference / POV / handoff_in / handoff_out).
3. **Phase 6 (substance bone-gate):** `write-b01c01-bone-gate.md` — PASS, 27/27 bones bonefide. Per-scene Δ delivery within band (s01 0.19/target 0.2, s02 0.24/target 0.2, s03 0.10/target 0.1). No HARD `SUBSTANCE-FLAT-<axis>` or `SUBSTANCE-SUSPECT-cheap-gain-<axis>`.

### Audits run on b01c01 facets (`/and-facets`)
Five reports under `active-project/staff/auditor/facets-final-audit{*}.md`:
- **r1** (initial): 6 HARD + 15 SIGNAL across 9 facets + cross-facet surface. Classes: CONSTRAINT × 4 (memory NI-spine; exposition × 3), AP-SCAN × 1 (NI template saturation), RUBRIC-FIDELITY × 1 (state-updates POV co-citation).
- **r2** (re-audit after fixer pass): 1 HARD (state-updates carve-out hand-applied to slice not consolidated). Plus carry-forward SIGNAL.
- **cycle2** (after broader cycle-2 remediation): 3 HARD (scene-map bone count mismatch; mem:1 free-text target; mem:1+mem:3 per-scene cap violation) + 5 SIGNAL.
- **r3** (verify cycle-2): CLEAN, 0 HARD, 1 FLAG (missing "resolves F-006" sentence) + carry-forward SIGNAL.
- **cycle3-closure**: PASS (fault-C3-001 unanchored old-state on sensory:2 @15 CLOSED).

**Total auditor cycles for facets: 5.** **Total HARD findings raised across all audits: ~10 (across r1+r2+cycle2). All RESOLVED before audience-gate cycle progression.**

### Fixer activity
`fixer-log.md` contains 113 `##` headers across 20+ named sessions: 1d-audit, series-audit, b01-schema-migration, write-b01c01-pass2/pass5, facets-b01c01-hard-remediation (twice), pipeline-adaptation-audit-fix (17 finds), tensometer-translation-cleanup, write-b01c01-phase2-svo, facets-b01c01-cycle2-remediation (10 sub-targets), cycle2-signal002-physical-delete, facets-b01c01-hard-r1-six-findings (× 2 cont), facets-b01c01-audience-gate-cycle2 (F-007 through F-013), facets-b01c01-cycle3 (F-014 + F-015a + F-015b + memory SKIPPED), facets-rejected-removal (sensory:3 + mem:1 removed by user directive post-cap-burn).

Class breakdown of resolved findings:
- HARD CONSTRAINT findings: all RESOLVED (e.g., F-002 / F-003 / F-004 exposition embedded-noun gloss, F-005 NI template saturation, F-006 state-updates POV co-citation carve-out)
- HARD RUBRIC-FIDELITY findings: all RESOLVED, including F-010 carve-out hand-applied + propagated, F-011 monument card created (cards/conditions/monument-override-architecture-prohibition-122ac.card.md)
- HARD AP-SCAN: NI template saturation RESOLVED via cycle-2 narrator:2/4 rewrites
- SUBSTANCE-FLAT / cheap-gain: never triggered at bone-gate
- Single SKIPPED-by-design: memory cycle-3 (cap-burn — see §6)

**What fixer changed in real terms:**
- Renamed Nessa→Wren across the chain-shape card; created cond-cost-bearer-scene-frequency
- Replaced Khepri-architecture-in-miniature framing throughout signature + chunk + trajectory with surveillance/unconsented-instrumentalization
- Inserted two-beat refuse-then-accept structure at d03 in trajectory + chunk
- Three SVO form fixes on bones (no substance change)
- ~30 facet entry edits across cycle-1 + cycle-2 + cycle-3 (cut, renumber, rewrite, anchor old-state, add monument target slugs)
- Two final entry deletions (sensory:3, mem:1) at user direction after cap-burn — see §8

---

## 5. Substance bone-gate at `/and-write` Phase 6

**Report:** `active-project/staff/auditor/write-b01c01-bone-gate.md`. **Verdict: PASS.**

Per-axis per-scene table:

| Scene | Axis | Bones sum | Target | Band | Verdict |
|---|---|---|---|---|---|
| s01 | knowledge | 0.19 | 0.20 | 0.15–0.25 | PASS |
| s01 | capability | all null/0 | null/0 | — | PASS |
| s02 | knowledge | 0.24 | 0.20 | 0.15–0.25 | PASS |
| s02 | capability | all null/0 | null/0 | — | PASS |
| s03 | knowledge | 0.10 | 0.10 | 0.07–0.13 | PASS |
| s03 | capability | all null/0 | null/0 | — | PASS |

Opposing-force-visible: PASS each scene (s01n04 coll-lifts-eyes; s02n04 insects-fill-block + s02n05 walls-cool; s03n01–s03n03 entry/speech triggering Taylor's automatic assessment).
Cost-ledger: clean — all `cost_ledger_anchor: ~` per the pre-arrangement chapter contract.
Substance-flat / cheap-gain: zero HARDs.

**Anomaly:** None. This is the bones-first authoring gate working as designed — auditor enumerated each bone, identified anchor / opposing-force / cost roles, and verified Δ matches SVO causality.

---

## 6. Audience-gate at `/and-facets` Phase 5b (adversarial 3-of-3)

**Report:** `active-project/staff/auditor/facets-audience-gate-r3.md`. **Verdict: CAP-BURNED (NOT-SUCCESSFUL).**

Cycles fired: **3 of 3**. 12 facets / sub-facets evaluated (9 standard + 3 per-character dialogue files).

| Facet | Cycle 1 | Cycle 2 | Cycle 3 | Final |
|---|---|---|---|---|
| location-state | revise (3) | accept (3) | — | ACCEPT |
| interest-narrator | revise (3) | revise (1: dark-fantasy doubled-register) | accept (3) | ACCEPT |
| **sensory** | revise (1) + fail (2) | accept (1) + revise (1) + fail (1) | accept (2) + revise (1: new HARD on sensory:3 lineage) | **FAIL** |
| state-updates | revise (3: carve-out position) | accept (3) | — | ACCEPT |
| **memory** | revise (3: feel-as-spine + slug-form) | revise (3: feel-as-spine fundamentally rejected) | NOT RE-RUN (no actionable fix) | **FAIL (cap-burn)** |
| feeling | accept (3) | — | — | ACCEPT |
| metaphor | accept (3) | — | — | ACCEPT |
| vibes | accept (3) | — | — | ACCEPT |
| exposition | accept (3) | — | — | ACCEPT |
| dialogue/coll | accept (3) | — | — | ACCEPT |
| dialogue/taylor | revise (3: sidecar citation) | accept (3) | — | ACCEPT |
| dialogue/wren | accept (2) + revise (1: "your hand") | accept (3) | — | ACCEPT |

Cycle counts: 12 facets fired cycle 1 (5 pass / 7 fail). 7 fired cycle 2 (4 pass / 3 fail). 2 fired cycle 3 — memory deliberately not re-run because all three remediation paths were blocked (add NI @9 → band breach; delete mem:1 → SHAPE-FAIL; rubric-authority ruling → out of scope). Sensory cycle 3 fix added sensory:3 @17 to clear modality silent-gap; the add introduced a NEW HARD (unanchored mid-afternoon time-of-day old-state) — cycle 3 audit could not catch it, only cycle 3 audience did.

**Cap-burn outcome:** Per the spec the verdict is NOT-SUCCESSFUL. `audience_gate_cap_burned: true` recorded. Status stayed `audited-r1-mechanical` — NOT advanced to `audited-r1`. The two failing facets (sensory, memory) remain on disk in their cycle-3 state. **Downstream stitcher consumed them anyway** — the user directive (`fixer/and-facets-rejected-removal.md`) was to DELETE sensory:3 @17 and mem:1 @9 outright rather than fix or carry. That removed the rejected entries from the facet graph cleanly, so stitcher consumed an audit-clean (post-removal) facet set; the cap-burn verdict on the gate itself stands in the record.

---

## 7. Orchestrator-critic / `/and-review verdict`

**Formal `/and-review verdict b01` was NOT dispatched.** No file under `active-project/staff/reviews/` matches the `verdict-<book>-<timestamp>.md` shape. The orchestrator-critic card was instead executed *inline* by the orchestrating command body at two surfaces:

1. `active-project/staff/auditor/facets-audience-gate-r3.md` § Recommendation invokes the orchestrator-critic explicitly: "The orchestrator-critic verdict (below in master summary) is NOT-SUCCESSFUL per the critic card's explicit hot-button: 'Cap-burn is a NOT-SUCCESSFUL verdict, not a ship anyway license.'"
2. `active-project/staff/showrunner/and-facets-b01c01-summary.md` § "/and-facets orchestrator-critic verdict — b01-c01": Result: **NOT-SUCCESSFUL**. Criteria met 6 / 7. Cap-burn rationale enumerated. Recommendation: ESCALATE (queue rubric authority ruling on feel-as-spine; queue sensory loc-state baseline add).

The orchestrator-critic's hot-button anti-pattern (ship-anyway on cap-burn) was honored — the status did not flip to `audited-r1` and the failure was logged.

**Anomaly:** `/and-review verdict` as a discrete dispatch has not been run on this book. Whether that matters depends on intent: `/and-facets` Phase 6 already fires the orchestrator-critic inline at chapter granularity. A book-level `/and-review verdict b01` is meaningful only after multiple chapters exist. b01c01 is the only chapter completed.

---

## 8. Cross-cutting: where review feedback CHANGED the artifact vs. got noted-and-ignored

### Changed the artifact (genuine gate)
- Signature pass 1 worm-canon-pedant single-fail (cheap-gain-capability) forced full re-author of capability framing across signature, chunk, trajectory, and d04/d12 cause language. Real change.
- b01 plan pass 1 audience REVISE × 3 forced screen-writer revise; pass 2 cleared 3-of-3.
- b01c01 chapter audit HARD (density envelope mismatch) forced chapter `density_target` revision before persist.
- /and-write Phase 2 SVO FAULTS-3 forced three bone-form rewrites (semantically null but procedurally enforced).
- Facets cycle 1 (6 HARD) and cycle 2 (3 HARD) drove ~30 facet entry edits + creation of monument-override-architecture-prohibition-122ac card.
- Audience-gate dialogue-wren cycle 1 "your hand" → "you" rewrite (worm-canon-pedant catch — single dissent enforced under 3-of-3 rule).
- Audience-gate state-updates cycle 1 → carve-out block authored (rubric-citation defense; F-006).

### Noted-but-not-fixed (carve-out / signal carry-forward / cap-burn)
- **b01c01 substance audit finding-002 (Khepri double-naming in s03):** classified SIGNAL not HARD because "Khepri-haunted without naming Khepri" was a chunk register note, not a series hard fence. **ACCEPTED at chunk level; routed forward to `/and-write` Phase 4 voice pass for bone-level smoothing.** Carve-out.
- **b01c01 substance audit finding-004 (hinge dramatic shape):** TASTE-FLAG only. Dramatist accepted as project-specific designation. Re-fires only if `hinge` recurs across consecutive pre-arrangement chapters. Carve-out with monitoring.
- **State-updates F-006 (POV co-citation gap 8/9):** option (c) carve-out applied — wrote a `# rubric-carve-out` annotation block citing the rubric's own scoping clause, classifying 8 entries as exempt mechanical-action OR accepted-with-defense rather than adding 8 NI entries (which would breach the NI band ceiling). This is a **legitimate gate-internal carve-out** (audience accepted it cycle 2 after the annotation block was hand-applied to the consolidated file). The state-updates rubric itself authorized this resolution path.
- **Facets cycle-3 memory:** all three remediation paths blocked. Fixer **SKIPPED** by orchestrator decision rather than attempting a fourth cycle. Cap-burn documented in the orchestrator-critic verdict. Then **the user issued a post-cap-burn directive to DELETE mem:1 @9 outright** (`fixer/and-facets-rejected-removal.md`) — sidestepping the rubric authority ruling entirely. This is the single instance where a fail was resolved by *removal* rather than fix.
- **Facets cycle-3 sensory:3:** same shape. Cycle-3 ADD introduced a new HARD that cycle-3 audit didn't catch; sensory-old-state-reader specialist surfaced it in cycle-3 audience. Cap-burned. User directed deletion of sensory:3 @17. Removal-as-resolution.
- **Pipeline-adaptation audit (17 findings):** all RESOLVED in the pipeline-adaptation-audit-fix session. This was upstream pipeline adaptation, not b01c01 content — not a gate override.
- **15 SIGNAL findings from facets r1 audit:** all carried forward unchanged. SIGNAL by definition does not block; carry-forward is per spec.

### Anomalies / honest gate failures
1. **Audience bone-gate did not vote on s03.** All three persona files at `active-project/audience/{persona}/write-b01c01-bone-gate.md` cover s01 and s02 only. The bone-gate auditor covered all 27 bones; the audience did not. This is a coverage gap, not a structural override, but it means the bone-gate audience verdict for b01c01 is effectively 2-scenes-of-3.
2. **Cap-burn resolved by deletion at user direction.** The orchestrator-critic correctly flagged NOT-SUCCESSFUL. The downstream resolution (delete sensory:3 + mem:1 outright) was a *human override* of the rubric-authority-ruling-required path. The cap-burn verdict remains in the record, but the file state was changed via removal rather than rubric resolution. This is the single case in the run where a fail was carve-out-overridden rather than fixed — and it was an explicit user directive, not an agent decision.
3. **No formal `/and-review verdict b01` dispatch.** Orchestrator-critic was exercised inline at `/and-facets` chapter granularity but not at book granularity. Acceptable for a single-chapter book-in-progress, but the dedicated subcommand has not yet been load-tested.

---

## 9. Net assessment

The gate stack functioned as a real gate at: series-level human audit, signature audience (single-dissent enforced), b01 plan audience (single-pass revise forced), all auditor mechanical passes (every HARD cleared by fixer before progression), bone-gate substance check (PASS clean), and most facet audience-gate facets (10 of 12 cleared 3-of-3 within cap).

The gate stack rubber-stamped at: bone-gate audience coverage for s03 (no votes filed).

The gate stack was overridden by user fiat at: cap-burned sensory and memory facets (deleted rather than fixed). This was the explicit user-directive path; the orchestrator-critic correctly held NOT-SUCCESSFUL in the record.

The gate stack has a known structural gap at: rubric-authority ruling for feel-as-spine substitution in memory cross-facet contract. This is queued for upstream tuning per the orchestrator-critic carry-forwards.
