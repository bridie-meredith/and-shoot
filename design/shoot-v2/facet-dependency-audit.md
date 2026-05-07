---
audit: facet-dependency-graph
date: 2026-05-07
scope: 10 tuned facets + dialogue render layer + SVO upstream
trigger: end of vibes-updates Phase 5 (10th facet shipped); user direction at end of vibes session — dependency-graph audit before any further tuning or audience-interest work
status: PASS-1 ANALYSIS — DAG canonical; gap classifications recommended; no re-tuning executed (awaiting user confirmation per gotchas section)
author: main session synthesis (Explore agent extracted contracts; main session synthesized DAG)
---

# Facet Dependency-Graph Audit

## Audit shape

One consolidated report. Per-facet sub-sections below the DAG. Three gap classes: CROSS-FACET-NOTE (already correct, document only), RE-TUNE-MINOR (rubric edit + Phase 5 retune), RE-TUNE-MAJOR (full re-pass after upstream tuning settles).

Audit is standalone. Does not depend on new SVO writer artifacts. Re-tune-against-new-SVO is a separate downstream pass once SVO lands.

---

## TL;DR

- **Canonical DAG built.** It is NOT the user's predicted order. State-updates and memory are SIBLINGS at layer 3, not sequenced. Loc-state is a layer-1 root, not downstream of state-updates. NI is downstream of tens+loc-state, not sibling.
- **No RE-TUNE-MAJOR identified.** All ten shipped rubrics' structural integrity holds in dependency order. Eight facets were tuned without explicit vibes-cite, but vibes-as-bias was *implicit and present* during their authoring (world-build pre-seeded vibe-clouds were loaded by the dialogue-writer / studio / NI / feeling / metaphor authors at their tuning time). Their structural correctness does not depend on vibes-cite. Their bias-completeness documentation does.
- **Nine RE-TUNE-MINOR.** Each prior facet's rubric should add `vibes:<keyword>` as an optional supporting cite (advisory, not gate). Rubric edit + Phase 5 mechanic re-verify on s01e01 corpus is sufficient. No structural retune.
- **Five CROSS-FACET-NOTE.** Documentation-only entries where contracts are correct but live in tuning packages, not in canonical rubric/schema.
- **One STRUCTURAL FINDING.** Vibes occupies a *dual role*: pre-seed (world-build authority — upstream of all author forks) AND vibes-updates facet (downstream cross-cutting consumer of state-update + memory + feeling + tens). The DAG must distinguish the two.
- **Tuning-readiness order ≠ dependency order.** Shipped order put vibes 10th (capstone) because the vibes-updates *facet* requires all upstream facets to be locked first. But pre-seed-vibes was active from project activation. The two roles ship together at the same artifact (vibes.md) but enter the DAG at opposite ends.

---

## Canonical DAG

```
                    proto-lines / SVO file (root upstream artifact)
                              │
              ┌───────────────┼───────────────┐
              │               │               │
            tens          loc-state     [pre-seed vibes]   ← LAYER 1 (no facet deps)
              │               │               │
              └────┬──────────┴────┬──────────┘
                   │               │
                  NI           sensory                      ← LAYER 2
                (tens+ls)      (loc-state mandatory;
                                tens correlative)
                   │
            ┌──────┴──────┐
            │             │
      state-updates    memory                               ← LAYER 3 (siblings; both depend on tens+NI)
            │             │
            └──────┬──────┘
                   │
                feeling                                     ← LAYER 4 (NI mandatory POV; SU+sensory soft)
                   │
                metaphor                                    ← LAYER 5 (memory OR feeling anchor mandatory)
                   │
           vibes-updates (facet)                            ← LAYER 6 (cross-cutting; consumes SU+memory+feeling+tens+proto)
                   │
        dialogue / stitch render                            ← LAYER 7 (terminal; consumes ALL)
```

### DAG vs user's predicted order

User predicted (from task framing): `vibes → tens → state-updates → loc-state → memory → feeling → sensory → NI → metaphor → dialogue`.

Audit's actual:

| User's slot | User's pick | Audit-correct slot | Reason for divergence |
|---|---|---|---|
| 1 | vibes | LAYER-1 PRE-SEED *and* LAYER-6 facet (split role) | Vibes has a dual role; user collapsed both into one slot |
| 2 | tens | LAYER 1 sibling of loc-state | Correct that tens is upstream-leaning; not literally first-after-vibes |
| 3 | state-updates | LAYER 3 | State-updates depends on NI mandatory co-cite; cannot precede NI |
| 4 | loc-state | LAYER 1 sibling | Loc-state has no facet deps; reads SVO/proto only — root, not downstream of SU |
| 5 | memory | LAYER 3 sibling of SU | Memory and SU share NI+tens deps; sibling, not sequenced after SU |
| 6 | feeling | LAYER 4 | Correct |
| 7 | sensory | LAYER 2 (loc-state-only dep) | Sensory could have been tuned at LAYER 2; nothing required NI/SU/feeling first |
| 8 | NI | LAYER 2 | NI's only mandatory deps are tens + loc-state — much earlier than user placed it |
| 9 | metaphor | LAYER 5 | Correct |
| 10 | dialogue | LAYER 7 terminal | Correct |

**Bottom line:** user's intuition about endpoints (vibes-as-bias upstream; metaphor + dialogue terminal) was right. Middle layer ordering was off.

### Tuning-readiness order (shipped)

1. SVO writer pipeline (upstream artifact; not strictly a facet)
2. dialogue (deferred — render layer; not yet tuned as a facet)
3. loc-state
4. tensometer
5. narrator-interest
6. state-updates
7. memory
8. sensory
9. feeling
10. metaphor
11. vibes-updates

### Dependency-correct order (one valid topo-sort)

1. SVO / proto-lines
2. {tens, loc-state} parallel (LAYER 1)
3. {NI, sensory} parallel (LAYER 2; sensory needs only loc-state)
4. {state-updates, memory} parallel (LAYER 3; both need tens + NI)
5. feeling (LAYER 4)
6. metaphor (LAYER 5)
7. vibes-updates (LAYER 6)
8. dialogue / stitch render (LAYER 7)

**Shipped order is a valid topological sort of the DAG with two minor inversions:**
- Sensory shipped 7th but only needs loc-state (LAYER-1 dep). Could have shipped 3rd. No structural cost — sensory's tuning was clean either way; loc-state was already locked when sensory was tuned.
- NI shipped 5th but is LAYER 2; this is correct.

No invalid orderings. No retune-major required for ordering reasons.

---

## Per-facet contract review

Each entry: current contract (READS, WRITES, LICENSING) → intended contract → gap class → recommended action.

### 1. tensometer (root LAYER 1)

- **Current READS:** SVO/proto-lines only.
- **Current WRITES:** scalar 1|2|3 per proto-line; downstream consumer list documented in §"Cross-facet contract".
- **Intended READS:** SVO/proto-lines + episode-scope vibes (curve-shape bias: "high-charge episode" vibes nudge ceiling distribution toward 3-cluster).
- **Gap:** RE-TUNE-MINOR. Rubric should add optional `vibes:episode-scope` as a soft bias signal for curve-shape calibration. No mandatory cite; tens is still a single-rater scalar.
- **Recommended action:** Add §"Optional bias signals" to rubric-tensometer.md naming episode-scope vibes. Phase-5 mechanic re-verify on s01e01 corpus (expected: zero changes; rubric documentation only).

### 2. location-state (root LAYER 1)

- **Current READS:** SVO/proto-lines; movement-verb necessity gate.
- **Current WRITES:** environmental fact entries; sensory-flags consumes old-state baseline.
- **Intended READS:** SVO/proto-lines + loc-scope vibes (location vibe-set biases environmental palette — e.g., the-machinery-arrives keyword for harrenhal-sept-environs biases sterile-witness register over warm-domestic).
- **Gap:** RE-TUNE-MINOR. Rubric should reference loc-scope vibes as advisory for the "one-clause sensory note" content selection. Already implicit (studio reads loc card, which now has a VIBES section after vibes write-back).
- **Recommended action:** Add §"Optional bias signals" naming loc-scope vibes. Phase-5 re-verify on s01e01.

### 3. pre-seed vibes (root LAYER 1; world-build authority)

- **Current READS:** N/A — this IS the root for vibes-as-bias.
- **Current WRITES:** vibe-clouds at `actors/*/vibes.md`, `loc-*.card.md § VIBES`, `staff/studio/vibes.md`.
- **Intended:** unchanged.
- **Gap:** STRUCTURAL FINDING (already documented). RF-001 from vibes Phase 3-4: pre-loaded vibe-clouds constitute authoritative existing state. `++`-or-skip is the default op for pre-loaded keywords. Gate-2 STRICT reading.
- **Recommended action:** Promote RF-001 from rubric-vibes V1.1 patch §1 into schemas/facet.schema.md § vibes-updates as canonical text (already applied in schema revision per the Phase 5 ship — verify).

### 4. narrator-interest (LAYER 2)

- **Current READS:** locked tens, locked loc-state, base behavior card, variant behavior card, persona card, proto-lines.
- **Current WRITES:** POV one-clause spotlight; consumed by memory (mandatory spine), feeling (POV non-redundancy), metaphor (anti-duplication).
- **Intended READS:** all current + actor-scope vibes for POV character (vibes bias *what registers* — e.g., taylor's the-machinery-arrives keyword biases NI toward authority-counter perception channels).
- **Gap:** RE-TUNE-MINOR. Vibes-as-supporting-bias-signal for the POV character's NI registration. Already implicit in dialogue-writer fork's pre-load (fork reads actor vibe-cloud); not currently named in rubric.
- **Recommended action:** Add `vibes:actor:<pov-slug>` as soft-supporting cite under §"Perceptual access". Phase-5 re-verify on s01e01.

### 5. sensory (LAYER 2)

- **Current READS:** locked loc-state (mandatory baseline), locked tens (correlative-only).
- **Current WRITES:** modality deltas; old-state cross-facet contract with loc-state.
- **Intended READS:** all current + loc-scope vibes (location vibe biases sensory frugality vs density — sterile-yard vs charged-yard).
- **Gap:** RE-TUNE-MINOR. Add loc-scope vibes as soft-supporting bias.
- **Recommended action:** Rubric edit + Phase-5 re-verify.

### 6. state-updates (LAYER 3)

- **Current READS:** locked tens (mandatory @39 held-against-turn class; @64 irreversible registration class), locked NI (mandatory POV-character co-citation), locked loc-state (frame context), proto-lines.
- **Current WRITES:** canonical-memory deltas; consumed by vibes-updates (state-update:<id> licensing source for vibe-writes).
- **Intended READS:** all current + actor-scope vibes (vibes bias what registers as canonical — e.g., the-mask-thinning vibe biases mask-state field to track exposure deltas more aggressively).
- **Gap:** RE-TUNE-MINOR. Add actor-scope vibes as soft-supporting bias for tracked-field selection.
- **Recommended action:** Rubric edit + Phase-5 re-verify.
- **Cross-facet-note:** vibes-updates consumes state-updates as a primary licensing source. This is correctly documented in vibes-updates rubric. The reverse arrow (state-updates citing vibes) is the gap above.

### 7. memory (LAYER 3, sibling of state-updates)

- **Current READS:** base behavior card, variant behavior card, persona card, locked tens (inverted-tens density gate), locked NI (mandatory spine co-citation).
- **Current WRITES:** monument-callback license; consumed by metaphor (mandatory anchor option).
- **Intended READS:** all current + actor-scope vibes (vibes bias which monuments light — e.g., taylor's the-machinery-arrives biases authority-monument lighting over trauma-monument lighting in the same beat).
- **Gap:** RE-TUNE-MINOR. Add actor-scope vibes as soft-supporting bias for monument selection. NI mandatory spine remains the structural gate.
- **Recommended action:** Rubric edit + Phase-5 re-verify.

### 8. feeling (LAYER 4)

- **Current READS:** behavior pack + persona card, locked NI (POV mandatory non-redundancy), locked sensory (soft), locked state-updates (soft).
- **Current WRITES:** somatic-tell; consumed by metaphor (mandatory anchor option).
- **Intended READS:** all current + per-character vibes (vibes bias somatic register — e.g., the-mask-thinning vibe biases interior-readable form discipline).
- **Gap:** RE-TUNE-MINOR. Add per-character vibes as soft-supporting bias for somatic register selection.
- **Recommended action:** Rubric edit + Phase-5 re-verify.

### 9. metaphor (LAYER 5)

- **Current READS:** memory OR feeling (mandatory anchor; one of the two), tens (curve-discipline; AP7 default-refuse at tens=3), sensory (permitted co-cite), NI (anti-duplication AP3).
- **Current WRITES:** capstone licensing-consumer; consumed only by stitch render.
- **Intended READS:** all current + per-character vibes + loc-scope vibes (vibes bias callback vs dark-humor register selection — e.g., the-machinery-arrives biases dark-humor authority-monument figures over warm-callback figures).
- **Gap:** RE-TUNE-MINOR. Add vibes as soft-supporting bias for register selection (callback vs dark-humor functional gate). Mandatory memory-OR-feeling anchor remains.
- **Recommended action:** Rubric edit + Phase-5 re-verify. Likely zero metaphor entries change on s01e01 (zero-fire episode); future-episode bias-completeness benefits.

### 10. vibes-updates (LAYER 6, cross-cutting)

- **Current READS:** state-update, memory, feeling, tens, proto, canon, world-build (all named in `licensed-by:` source enum).
- **Current WRITES:** persistent operator-bias deltas; pre-render hazard clause (V1.1 patch §4) prevents retroactive invalidation of locked upstream facets.
- **Intended READS:** unchanged. Vibes-updates is the cross-facet consumer; its contract is the most explicit in the system.
- **Gap:** CROSS-FACET-NOTE only. The vibes-updates contract is correct. The gap is that vibes-as-bias (the *pre-seed* role, distinct from the *facet-fires* role) is not explicitly documented as a separate node in the schema. RF-001 covers the structural finding; the schema text could be clarified.
- **Recommended action:** Add a §"Vibes' dual role" note to schemas/facet.schema.md § vibes-updates: "(1) pre-seeded vibe-clouds (world-build authored) bias all downstream author forks before facet authoring begins; (2) vibes-updates facet entries fire post-everything as cross-cutting consumers of locked upstream facets. The same artifact (vibes-cloud files) holds both. Pre-seeded keywords are STRICT gate-2 — `++`-or-skip default per RF-001."

### 11. dialogue / stitch render (LAYER 7 terminal)

- **Current READS:** ALL facets at stitch time. SVO/proto-lines are the upstream artifact; render consumes proto-line plus citation graph. SVO-writer pipeline is tuned (5 passes); stitch render is NOT tuned as a facet — it is the consumer of all facets.
- **Current WRITES:** final manuscript.
- **Intended READS:** all current. Vibes is consumed wholesale by stitcher as ambient bias context, not as render content (vibes never appear in prose per their definition).
- **Gap:** CROSS-FACET-NOTE. Dialogue/stitch was not tuned as a facet because it is the render layer. The SVO-writer pipeline that produces the upstream artifact IS tuned. The stitcher's contract — "facets are selection signals, not paraphrase sources; only 'and' edit budget" — is documented in schemas/facet.schema.md § "Stitch interface" but not in any rubric.
- **Recommended action:** Defer to user. Either tune stitch render as the 11th facet (would test stitcher discipline against locked facets) or accept that stitch is constrained enough by schema § "Stitch interface" that no rubric is needed. Default per facets-next-steps memory: dependency audit FIRST; this finding falls out as a doc-only update if stitch tuning is deferred.

### 12. SVO writer pipeline (root upstream artifact)

- **Current state:** five-pass pipeline tuned end-to-end 2026-05-07 against s01e01 (6.1 → 100; +93.9pp); v2 command and locked artifacts not yet promoted to /and-protolines per facets-next-steps memory.
- **Gap:** CROSS-FACET-NOTE. New SVO writer artifacts are incoming from a parallel session per user direction. When they land, re-run each shipped facet's Phase 2 fork blind to prior output against new SVO; mechanic verifies. If a rubric breaks against new SVO, that's a structural finding — capture it, re-tune that facet only.
- **Recommended action:** Per user direction step 6 — defer until new SVO lands. This is a SEPARATE downstream pass after this dependency audit.

---

## Gap summary table

| Facet | Class | Action |
|---|---|---|
| tensometer | RE-TUNE-MINOR | Add `vibes:episode-scope` as optional bias signal |
| location-state | RE-TUNE-MINOR | Add loc-scope vibes as advisory |
| narrator-interest | RE-TUNE-MINOR | Add actor-scope vibes (POV) as soft-supporting |
| sensory | RE-TUNE-MINOR | Add loc-scope vibes as soft-supporting |
| state-updates | RE-TUNE-MINOR | Add actor-scope vibes as soft-supporting |
| memory | RE-TUNE-MINOR | Add actor-scope vibes as soft-supporting |
| feeling | RE-TUNE-MINOR | Add per-character vibes as soft-supporting |
| metaphor | RE-TUNE-MINOR | Add vibes as soft-supporting (register selection) |
| vibes-updates | CROSS-FACET-NOTE | Document vibes' dual role in schema |
| dialogue / stitch | CROSS-FACET-NOTE | Defer (no rubric) or tune stitch as 11th facet |
| SVO upstream | CROSS-FACET-NOTE | Re-tune-against-new-SVO when artifacts land |

**Counts:** 8 RE-TUNE-MINOR, 3 CROSS-FACET-NOTE, 0 RE-TUNE-MAJOR.

---

## Reusable rubric components (carry-forward)

From vibes Phase 4 V1.1 patch:

- **AP8 sentence-parsability test** — applies to any facet using hyphenated word-algebra tokens. Currently vibes-only; if any other facet gains extension semantics, apply.
- **AP11 string-formal + semantic-advisory split** — applies to any extension op. Currently vibes-only.
- **Cross-facet pre-render clause** — any future bias-layer facet. Currently vibes-only; would apply to any future *bias* facet (vibes is the only one).
- **RF-001 STRICT gate-2 reading** — any pre-seeded artifact-state. Promote into schema text.

From metaphor Phase 4:

- **Monument-scope determination** — memory anchors license full monument's semantic domain, not just image-domain. Already canonical in metaphor rubric. No carry-forward needed (already applied where relevant).

---

## Recommended retune ordering (if user confirms)

If RE-TUNE-MINOR work proceeds, dependency order is:

1. tens (LAYER 1; rubric edit + Phase-5 re-verify)
2. loc-state (LAYER 1; rubric edit + Phase-5 re-verify)
3. NI, sensory (LAYER 2; parallel)
4. state-updates, memory (LAYER 3; parallel)
5. feeling (LAYER 4)
6. metaphor (LAYER 5)
7. vibes-updates schema clarification (no facet retune; schema text only)

Rationale: dependency-order so that downstream rubrics can reference upstream rubrics' newly-documented vibes-cite. Sibling layers can run in parallel.

Estimated cost per facet: rubric edit (small; one §"Optional bias signals" section added) + Phase-5 mechanic re-verify on s01e01 corpus (small; expected zero entries change since vibes-as-bias was implicit during prior tunings). Total: 8 small passes.

If new SVO writer artifacts land mid-retune, sequence becomes: complete current RE-TUNE-MINOR pass against current SVO → on new SVO landing, re-run each facet's Phase 2 fork blind against new SVO (separate pass per user direction step 6).

---

## Open questions for user (before executing any retune)

The following are NOT routine; user direction recommended before dispatching:

1. **Retune-minor scope.** Confirm: rubric edit + Phase-5 mechanic re-verify only, or full Phase 1-5 cycle? Default: rubric-edit + Phase-5 re-verify (cheap; structural integrity already proven).
2. **Stitch render tuning.** Tune as 11th facet or defer? Default: defer (schema § "Stitch interface" plus svo-writer pipeline already discipline the render path).
3. **New SVO timing.** Run RE-TUNE-MINOR against current SVO now, or wait for new SVO and run against new directly? Default: wait — running against current SVO and then again against new SVO is wasted motion. Audit findings can be applied as rubric edits NOW (cheap, no re-verify); Phase-5 re-verify deferred until new SVO.
4. **Vibes write-back.** Caveat-004 from vibes ship — 12 deltas across 6 actor vibe-files + 1 loc card (with new VIBES section) + studio EPISODE_1_VIBES. Block s01e02 facet authoring on this. Default: dispatch margit + showrunner write-back now, as a separate task from this audit. See §"Write-back action" below.

---

## Write-back action (separate from audit; per caveat-004)

Twelve vibe-deltas to apply:

- `actors/mira-stonefield/vibes.md` — append the-yard-as-witness ++ tokens
- `actors/edric-cray/vibes.md` — append the-yard-as-witness ++ tokens
- `actors/taylor-hebert-westeros/vibes.md` — append ++ tokens to the-machinery-arrives, the-letter, the-septon-as-absence
- `actors/census-officer/vibes.md` — append the-machinery-arrives ++ tokens
- `actors/septon-dying-protector/vibes.md` — add the-septon-as-absence keyword + bundle (fresh `+`)
- `cards/locations/loc-harrenhal-sept-environs.card.md` — add VIBES section with the-machinery-arrives + the-septon-as-absence keywords + bundles (fresh `+` × 2)
- `staff/studio/vibes.md` EPISODE_1_VIBES — append ++ tokens to the-machinery-arrives, the-letter, the-yard-as-witness

Authority: showrunner for actor + studio writes; margit for loc card edit. Tokens copied verbatim from `active-project/theater/facets/vibes.md` entries 1-12.

---

## Findings summary

- **Canonical DAG: 7 layers, 12 nodes (incl. SVO root + dialogue-render terminal).**
- **0 RE-TUNE-MAJOR.** Shipped tuning order is a valid topological sort (modulo two minor inversions that cost nothing).
- **8 RE-TUNE-MINOR.** All vibes-cite-as-supporting-bias additions. Cheap to apply (rubric edit + Phase-5 re-verify).
- **3 CROSS-FACET-NOTE.** Dual-role vibes documentation; stitch tuning deferred; SVO re-verify deferred.
- **1 STRUCTURAL FINDING.** Vibes' dual role (pre-seed bias = LAYER 1; vibes-updates facet = LAYER 6). Schema text revision recommended to make this explicit.

**No re-tuning executed in this audit.** Per user gotchas anticipation: "the DAG is what matters; document it cleanly; flag anything that needs re-tuning but don't actually re-tune until I confirm." Audit hands off to user for confirmation on retune-minor sequence and SVO-timing decision.
