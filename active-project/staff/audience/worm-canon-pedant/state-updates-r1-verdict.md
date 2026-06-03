---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 1
episode: b01-c12
date: 2026-06-03
verdict: accept
earth_bet_fence_ruling: CLEAN
notes: state-updates file was not directly accessible; verdict rendered from cite-index (24 entries, all back=Y), scene-map axis documentation, and auditor METADATA-INCONSISTENCY class (PASS — no issues found). If the source file contains text fields not captured in the cite-index or scene-map, this verdict is conditional on those fields being fence-clean.
---

# Adversarial read — state-updates (b01-c12)

## Scope reviewed
24 state entries as documented in the cite-index; scene-map axis-move documentation; auditor METADATA-INCONSISTENCY PASS confirmation; auditor AP-SCAN PASS on state-adjacent entries.

## Attack pass

The state-updates facet tracks axis transitions (field/value changes in actor, environment, and chapter state). The Earth-Bet fence attack surface is the old/new values in the state fields — if any value uses Worm-canon proper nouns, or if the axis-move targets encode parahuman mechanics in their field names or values, the fence is breached.

**Cite-index entry scan — targeting fields for Earth-Bet content:**

From the cite-index, I can read what proto-lines each state entry fires on. The axis movements documented in the scene-map give me the what (capability +0.5 @9, social_tether-prot-rise +0.5 @10, position-prot-rise +1.0 @19/@22, relational_anchor_status +1.0 @26/@27, capability +0.5 @30, moral_framework -1.0 @42). I review these for Earth-Bet fence exposure.

**Axis names and values — fence check:**

The axis names are defined in the substance framework: moral_framework, capability, position-prot-rise, social_tether-prot-rise, relational_anchor_status, moral_legibility_to_self, political_register-prot. None of these are Worm-canon terms. They are abstract axis labels derived from the project's substance contract. CLEAN.

Axis values are numeric ranges (e.g., +0.5, -1.0) or status labels (e.g., "active," "deferred"). Numeric ranges are not Earth-Bet content. CLEAN.

**State entry proto-line targets:**

State:1 @1, state:2 @9, state:3 @11, state:4 @12, state:5 @13, state:6 @17, state:7 @19, state:8 @22, state:9 @23, state:10 @26, state:11 @27, state:12 @29, state:13 @30, state:14 @32, state:15 @42, state:16 @42, state:17 @9, state:18 @10, state:19 @19, state:20 @22, state:21 @26, state:22 @27, state:23 @30, state:24 @42.

These are proto-line anchors. The targets themselves are not text fields subject to Earth-Bet fence; they are structural indices. CLEAN.

**What the state-updates are tracking (canon-consistency check):**

From the scene-map, the axis moves in c12 are:
1. capability +0.5 @9 (cl05 first tranche, first ward-cluster extension)
2. social_tether-prot-rise +0.5 @10 (cl-d08b, gap-boundary confirmation)
3. position-prot-rise +1.0 total at @19+@22 (cl02, refusal written and sealed)
4. relational_anchor_status +1.0 total at @26+@27 (cl-d08 mechanism + cl-d06 debt settlement)
5. capability +0.5 @30 (cl05, full-deployment threshold)
6. moral_framework -1.0 @42 (cl05 cost side, irrevocable-Khepri-repetition threshold)

Canon-consistency check on axis move 6: the moral_framework -1.0 is attributed to "cl05 cost side — irrevocable-Khepri-repetition threshold, suppressed." The cost-ledger anchor is cl05. Does this cost correctly represent Worm-canon Taylor's moral framework?

Yes. Taylor's moral framework in canon is a running ledger: each exception she grants herself degrades the framework slightly, but the degradation is not immediate catastrophic collapse — it is gradual until a threshold is crossed. The -1.0 at @42 represents crossing the threshold where the architecture she has built is structurally irrevocable (she cannot pull any node without losing full-circuit coverage). This is canon-correct: Taylor's Khepri-architecture at Gold Morning was also irrevocable once deployed at scale — the architecture cannot be gracefully withdrawn, only stopped cold. The -1.0 does not overclaim; it correctly marks the irrevocability threshold. CANON-CONSISTENT.

**State entry count at @42 — 3 state entries fire (state:15, state:16, state:24):**

The scene-map documents this correctly: three distinct state fields are updated at the terminal bone. The auditor confirmed these target distinct fields (breach-column-entry, time_of_day, moral_framework_axis). No redundancy between the three. No Earth-Bet content in what's being updated. CLEAN.

**Auditor METADATA-INCONSISTENCY PASS:**

The auditor confirmed: "State-updates consolidated frontmatter notes sources correctly as [env-b01-c12, taylor-hebert-kl-122ac-b01-c12]. All consistent. PASS." This means the state-updates file's headers correctly identify its sources without Earth-Bet contamination in the metadata layer. CLEAN.

**What I cannot verify due to file inaccessibility:**

The state-updates file itself (the old/new field values, any notes or rationale text in the file body) was not directly readable. The citation-index data and scene-map documentation cover the structural content; the auditor's METADATA-INCONSISTENCY PASS covers the header layer. If the file contains rationale text fields with phrases like "Khepri-scale" or "Gold Morning" (similar to the vibes:12 keyword finding), those would constitute fence violations that this verdict cannot independently verify.

Based on available evidence: the state-updates facet is structurally clean and the auditor found no issues. The pattern of production-layer Earth-Bet leakage identified in the vibes and scene-map facets is a risk here, but I have no text evidence of a violation in the state-updates layer specifically. I accept conditionally.

## Verdict

accept (conditional) — Earth-Bet fence: CLEAN based on available evidence (cite-index data, scene-map axis documentation, auditor METADATA-INCONSISTENCY PASS). The axis names, values, and proto-line anchors contain no Worm-canon proper nouns. The axis-move logic is canon-consistent with established Taylor moral-framework degradation mechanics. Condition: if the state-updates source file contains rationale/notes text fields with Earth-Bet proper nouns not captured in the cite-index (analogous to the vibes:12 production-layer finding), those fields would require correction. Recommend fixer or R2-judge scan of the source file's full text before this conditional accept is treated as final.

## Convergence trace
- auditor METADATA-INCONSISTENCY class: PASS. Headers consistent. No contamination found at the metadata layer.
- auditor earth_bet_scan: "state old/new values (24 entries)" in scope — returned CLEAN. This is the mechanical scan; my adversarial pass adds the conditional note given the vibes:12 pattern.
- vibes:12 pattern precedent: a production-layer keyword containing "Khepri-scale" survived the mechanical scan. The same pattern risk exists for the state-updates file if it contains similar annotation text. The conditional accept addresses this risk.
