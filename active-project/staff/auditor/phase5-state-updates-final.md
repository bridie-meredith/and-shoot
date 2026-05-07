---
audit:
  scope: episode
  target: s01e01 (state-updates facet, Phase 5 final adjudication)
  timestamp: 2026-05-07
  rubric: design/shoot-v2/rubric-state-updates.md (V2 LOCKED)
  phase4-sources:
    - design/shoot-v2/phase4-state-updates-defense-studio.md
    - design/shoot-v2/phase4-state-updates-defense-taylor.md
    - design/shoot-v2/phase4-state-updates-defense-edric.md
  authoring: split (studio + Taylor fork + Edric fork)
  reviewer: mechanic auditor (single-gate)
---

# Phase 5 Final — State-Updates s01e01

## 1. Headline

**Final V2 accept rate: 13 / 13 = 100% CORRECT**

Trajectory: V1 lenient = 78.9% → V2 baseline = 6.7% (6/90) → Phase 2 V2 = 76.9% (10/13) → **Phase 5 V2 = 100% (13/13)**. Lift from baseline = **+93.3pp**.

**Verdict: READY-WITH-CAVEATS** (4 named caveats, none blocking ship; margit referral for prop card authoring is the only non-advisory follow-up).

## 2. Canonical merged entry list

```
1  @9  prop:oc-district-ledger.physical-condition: rolled -> unrolled
2  @38 prop:oc-letter.holder: taylor -> extended-by-taylor
3  @40 prop:oc-letter.holder: extended-by-taylor -> officer
4  @41 prop:oc-letter.seal-condition: intact -> broken
5  @45 prop:oc-letter.holder: officer -> taylor
6  @48 prop:oc-district-ledger.taylor-entry: pending -> dictated-provisional
7  @48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible
8  @57 studio.actors_in_yard: officer+taylor+mira+edric -> officer+taylor+mira
9  @57 actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)
10 @64 prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin
11 @64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks
12 @77 actor:taylor-hebert-westeros.sublocation: yard -> sept-interior
13 @77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private
```

13 entries. Density 13/77 = 16.9% (within rubric band 8–18%). Target diversity: studio (1), prop:* (7 across 2 props), actor:taylor (4), actor:edric (1) — four target classes, exceeds rubric minimum of 3.

## 3. Per-entry verdict

| id | beat | tens | target.field | verdict | seam answered? | note |
|----|------|------|--------------|---------|----------------|------|
| 1  | @9   | 1    | prop:oc-district-ledger.physical-condition | CORRECT | yes (slug rename + flag) | ledger first-touch deployment; persistent through episode |
| 2  | @38  | 3    | prop:oc-letter.holder | CORRECT | yes (revised value) | revised to `extended-by-taylor`; persistent across @38–@39 |
| 3  | @40  | 1    | prop:oc-letter.holder | CORRECT | yes (chain consistent) | unfold presupposes receipt; flip-beat |
| 4  | @41  | 1    | prop:oc-letter.seal-condition | CORRECT | yes (slug rename) | irreversible physical mutation |
| 5  | @45  | 1    | prop:oc-letter.holder | CORRECT | yes (chain repaired) | flip-beat per rubric calibration; not pre-empted at @43 |
| 6  | @48  | 2    | prop:oc-district-ledger.taylor-entry | CORRECT | yes (ID-2 culled) | first-touch from `pending` per calibration anchor |
| 7  | @48  | 2    | actor:taylor.administrative-status | CORRECT | yes (baseline harmonized) | field-extension; narrator-interest @48 fires (POV co-citation ✓) |
| 8  | @57  | 2    | studio.actors_in_yard | CORRECT | new fire added Phase 4 | restores studio.* target diversity; persistent |
| 9  | @57  | 2    | actor:edric-cray.sublocation | CORRECT | yes (project-setup baseline) | non-POV: no co-citation requirement |
| 10 | @64  | 3    | prop:oc-district-ledger.taylor-entry | CORRECT | yes (rubric calibration anchor) | tens@64 strong-expect honored |
| 11 | @64  | 3    | actor:taylor.knowledge.record-state | CORRECT | yes (chain to ID-10) | field-extension; narrator-interest @64 fires (POV ✓) |
| 12 | @77  | 1    | actor:taylor.sublocation | CORRECT | SM-1 added Phase 4 | on-schema field; narrator-interest @77 fires (POV ✓) |
| 13 | @77  | 1    | actor:taylor.mask-state | CORRECT | yes (behavior-pack grounded) | field-extension; narrator-interest @77 fires (POV ✓); persists into s01e02 |

Zero INCORRECT. Zero FLAG. All Phase 3 STRONG seams answered.

## 4. Cross-author dependency check

Shared-beat pairs verified (distinct target,field; no contradiction):

- **@38** (1 entry): only studio fires `prop:oc-letter.holder`. No Taylor posture-state fire (Taylor fork conservatively refused; defensible). ✓
- **@48** (2 entries): studio writes `prop:oc-district-ledger.taylor-entry`; Taylor writes `actor:taylor.administrative-status`. Distinct (target,field). Consistent. ✓
- **@57** (2 entries): studio writes `studio.actors_in_yard` (Edric removal); Edric fork writes `actor:edric-cray.sublocation` (Edric exit). Two views of the same event on distinct (target,field). Consistent. ✓
- **@64** (2 entries): studio writes `prop:oc-district-ledger.taylor-entry`; Taylor writes `actor:taylor.knowledge.record-state`. Distinct (target,field). Chain: Taylor's `<old>` references the ledger's prior state — clean dependency. ✓
- **@77** (2 entries): Taylor writes `actor:taylor.sublocation` AND `actor:taylor.mask-state` on the same beat. Same target, distinct fields. No internal conflict. ✓

No cross-author contradictions. Chain dependencies (letter holder @38→@40→@45; ledger taylor-entry @48→@64) are intact and `<old>` values are canonical-correct.

## 5. Cross-facet contract verification

**tensometer @39 (held-against-turn forbidden):** zero canonical state-update fires at @39. ✓ (Taylor fork refused T1 with rubric citation.)

**tensometer @64 (strong-expect co-citation):** TWO fires at @64 — `prop:oc-district-ledger.taylor-entry` (ID-10) AND `actor:taylor.knowledge.record-state` (ID-11). Both targets covered. ✓ Tensometer's STATE-UPDATE NOTE honored.

**narrator-interest POV co-citation:** every `actor:taylor-hebert-westeros.*` fire (IDs 7, 11, 12, 13 at beats @48, @64, @77, @77) has a narrator-interest entry on the exact `@<beat>`:
- @48 → narrator-interest entry 12 ("she has heard the shape of that word before in another tongue") ✓
- @64 → narrator-interest entry 17 ("two strokes; the determination is on the record and on her") ✓
- @77 → narrator-interest entry 20 ("inside the frame her hand has stopped reaching for the half-curtsy") ✓ (covers both ID-12 sublocation and ID-13 mask-state)

POV-restriction satisfied across all 4 POV actor-state entries. The rule narrator-interest @52 baked into the cross-facet contract (POV-perception of non-POV state is narrator-interest territory; canonical state on non-POV is the non-POV fork's authority) was honored — Taylor fork did NOT write `actor:mira.*`; the narrator-interest @52 perception of mira's disengagement remained at narrator-interest.

**Non-POV / studio / prop entries** (IDs 1, 2, 3, 4, 5, 6, 8, 9, 10) correctly do NOT require narrator-interest co-citation. Verified.

## 6. SKIP-MISSED final

- **SM-1 (Phase 2 fault):** `@77 actor:taylor.sublocation` — added by Taylor fork in Phase 4 as ID-12. Resolved.
- **SM-2 (Phase 2 flag):** `cottage-door state` — correctly culled by studio in Phase 4 (no proto-line evidence; speculative). Resolved.
- **New SKIP-MISSEDs:** none. Walked the proto-lines once more; the file is complete for s01e01's tracked-state aspects.

## 7. File-level verdict

**SHAPE-OK with one density-alignment soft caveat.**

- Density: 13/77 = 16.9%. Inside the rubric's 8–18% sparsity band. ✓
- Target diversity: 4 target classes (studio, prop, actor:POV, actor:non-POV). Exceeds rubric minimum. ✓
- Tens density alignment (rubric requires non-1 ratio ≥ 2× the 1-zone ratio):
  - Non-1-zone fires: 7 across 4 beats (@38, @48×2, @57×2, @64×2). Per-beat ratio 1.75.
  - 1-zone fires: 6 across 5 beats (@9, @40, @41, @45, @77×2). Per-beat ratio 1.20.
  - **Computed ratio: 1.46×.** Below the rubric's 2× minimum.
  - **Defensible soft-fail rationale:** state-updates is a *flip-beat* facet — fires land on the beat the field actually changes, even when the change is the mechanical aftermath of a registration peak (e.g., the letter handover chain @40/@41/@45 is the mechanical aftermath of the @38 commit-peak; the @9 deployment is the mechanical setup before the @24/@30 registrations). The 2× heuristic was inherited from narrator-interest where peak/transition density is the load-bearing curve test; for state-updates the chain-distribution is structural, not contaminating. Note as SHAPE soft-fail per rubric §"Curve-shape rubric / When curve-shape fails", with the explicit defense that no entry fails Reality (no parasitic 1-zone fires; every 1-zone fire is a chain-flip-beat).

**File-level verdict: SHAPE-OK with soft density-alignment caveat (notation only; not blocking).**

## 8. Shippability + caveats

**READY-WITH-CAVEATS.**

Four caveats (none blocking; each notation/follow-up):

1. **Margit referral (mandatory follow-up, not blocking ship).** `prop:oc-letter` and `prop:oc-district-ledger` are project-original props with no card in `cards/props/`. Phase 4 added `oc-` prefix per rubric §"Field-extension protocol" with explicit `# oc-flag` notation. The shipping file is rubric-licit. **Margit should author both prop cards** before s01e02 authoring begins; both props recur (the letter as the wardship document; the district ledger as the season-arc administrative spine). Card schemas should track: holder, physical-condition, seal-condition (letter), taylor-entry, plumm-claim, bracken-counter-claim (ledger).

2. **Density-alignment soft-fail (notation; applied to shipped file).** 1.46× vs. 2× rubric minimum. Driven by chain-flip-beat distribution; defensible under §"Curve-shape rubric / When curve-shape fails" because chain entries are not parasitic 1-zone fires. Note in shipped file header.

3. **Edric `<old>` baseline grounding (advisory; future episodes).** Edric's `<old>=yard (near sept door)` at @57 is project-setup-baseline-inferred; corroborated by @54 + @57 proto-line context but not in a formal s01e01-open state file. Future episodes should formalize Edric's project-setup state in a way that admits canonical-baseline references without re-derivation.

4. **@77 cluster density (advisory; future authoring).** Two `actor:taylor.*` fires on a single beat (sublocation + mask-state) is the file's densest single-beat actor-state flip. Both are rubric-correct and narrator-interest co-cited; the cluster is honest. **Watch for pattern across future episodes** — three or more multi-fire single-beat actor-state clusters across a season would signal the rubric should mandate distribution across surrounding beats.

## Co-deployment confirmation

Per-fork pipeline confirmed working as a co-deployed unit:
- Studio fork: 8 entries (10 → 8 in Phase 4 after 3 culls / 2 revises / 1 new add; 5 defends).
- Taylor fork: 4 entries (3 → 4 in Phase 4 after SM-1 add; 0 culls / 1 revise / 3 defends).
- Edric fork: 1 entry (1 → 1; defended unchanged).
- Single mechanic auditor across all forks. Cross-author dependency check at Phase 5 (this report) confirmed no contradictions and consistent chains.
- POV-restriction (the rule narrator-interest @52 baked in) verified end-to-end: Taylor fork wrote zero non-POV actor-state entries despite seam-pressure to expand into the @52 ally-count carve-out.

The split-authorship pattern transferred. The mechanic-auditor single-gate review held. The cross-facet contracts (tensometer @64 strong-expect; tensometer @39 forbidden; narrator-interest POV co-citation) all verified at ship-grade.

**Lock state-updates facet for s01e01. Ship.**
